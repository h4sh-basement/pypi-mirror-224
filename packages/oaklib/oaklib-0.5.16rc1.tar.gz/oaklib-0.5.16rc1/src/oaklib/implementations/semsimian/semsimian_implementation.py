"""Rust implementation of semantic similarity measures."""
import inspect
import logging
import math
from dataclasses import dataclass, field
from typing import ClassVar, Dict, Iterable, Iterator, List, Optional, Tuple

from semsimian import Semsimian

from oaklib.datamodels.similarity import (
    TermPairwiseSimilarity,
    TermSetPairwiseSimilarity,
)
from oaklib.datamodels.vocabulary import OWL_THING
from oaklib.interfaces.basic_ontology_interface import BasicOntologyInterface
from oaklib.interfaces.obograph_interface import OboGraphInterface
from oaklib.interfaces.search_interface import SearchInterface
from oaklib.interfaces.semsim_interface import SemanticSimilarityInterface
from oaklib.types import CURIE, PRED_CURIE

wrapped_adapter: BasicOntologyInterface = None

__all__ = [
    "SemSimianImplementation",
]


@dataclass
class SemSimianImplementation(SearchInterface, SemanticSimilarityInterface, OboGraphInterface):
    """Rust implementation of semantic similarity measures."""

    delegated_methods: ClassVar[List[str]] = [
        BasicOntologyInterface.label,
        BasicOntologyInterface.labels,
        BasicOntologyInterface.entities,
        BasicOntologyInterface.curie_to_uri,
        BasicOntologyInterface.uri_to_curie,
        BasicOntologyInterface.ontologies,
        BasicOntologyInterface.obsoletes,
        BasicOntologyInterface.definition,
        BasicOntologyInterface.definitions,
        SearchInterface.basic_search,
        OboGraphInterface.node,
        OboGraphInterface.ancestors,
        OboGraphInterface.descendants,
        SemanticSimilarityInterface.get_information_content,
        SemanticSimilarityInterface.information_content_scores,
    ]

    semsimian_object_cache: Dict[Tuple[PRED_CURIE], Semsimian] = field(default_factory=dict)

    def __post_init__(self):
        slug = self.resource.slug
        from oaklib.selector import get_adapter

        slug = slug.replace("semsimian:", "")
        logging.info(f"Wrapping an existing OAK implementation to fetch {slug}")
        self.wrapped_adapter = get_adapter(slug)
        methods = dict(inspect.getmembers(self.wrapped_adapter))
        for m in self.delegated_methods:
            mn = m if isinstance(m, str) else m.__name__
            setattr(SemSimianImplementation, mn, methods[mn])

        self.term_pairwise_similarity_attributes = [
            attr
            for attr in vars(TermPairwiseSimilarity)
            if not any(attr.startswith(s) for s in ["class_", "_"])
        ]
        self.termset_pairwise_similarity_attributes = [
            attr
            for attr in vars(TermSetPairwiseSimilarity)
            if not any(attr.startswith(s) for s in ["class_", "_"])
        ]

    def _get_semsimian_object(
        self,
        predicates: List[PRED_CURIE] = None,
        attributes: List[str] = None,
        resource_path: str = None,
    ) -> Semsimian:
        """
        Get Semsimian object from "semsimian_object_cache" or add a new one.

        :param predicates: collection of predicates, defaults to None
        :return: A Semsimian object.
        """
        predicates = tuple(sorted(predicates))
        if predicates not in self.semsimian_object_cache:
            spo = [
                r
                for r in self.wrapped_adapter.relationships(
                    include_entailed=True, predicates=predicates
                )
            ]
            self.semsimian_object_cache[predicates] = Semsimian(
                spo, predicates, attributes, resource_path
            )

        return self.semsimian_object_cache[predicates]

    def pairwise_similarity(
        self,
        subject: CURIE,
        object: CURIE,
        predicates: List[PRED_CURIE] = None,
        subject_ancestors: List[CURIE] = None,
        object_ancestors: List[CURIE] = None,
        min_jaccard_similarity: Optional[float] = None,
        min_ancestor_information_content: Optional[float] = None,
    ) -> Optional[TermPairwiseSimilarity]:
        """
        Pairwise similarity between a pair of ontology terms

        :param subject:
        :param object:
        :param predicates:
        :param subject_ancestors: optional pre-generated ancestor list
        :param object_ancestors: optional pre-generated ancestor list
        :param min_jaccard_similarity: optional minimum jaccard similarity
        :param min_ancestor_information_content: optional minimum ancestor information content
        :return:
        """
        logging.debug(f"Calculating pairwise similarity for {subject} x {object} over {predicates}")
        semsimian = self._get_semsimian_object(
            predicates=predicates, attributes=self.term_pairwise_similarity_attributes
        )

        jaccard_val = semsimian.jaccard_similarity(subject, object)

        if math.isnan(jaccard_val):
            return None

        if min_jaccard_similarity is not None and jaccard_val < min_jaccard_similarity:
            return None

        _, ancestor_information_content_val = semsimian.resnik_similarity(subject, object)

        if math.isnan(ancestor_information_content_val):
            return None

        if (
            min_ancestor_information_content is not None
            and ancestor_information_content_val < min_ancestor_information_content
        ):
            return None

        sim = TermPairwiseSimilarity(
            subject_id=subject,
            object_id=object,
            ancestor_id=None,
            ancestor_information_content=None,
        )

        sim.jaccard_similarity = jaccard_val
        sim.ancestor_information_content = ancestor_information_content_val

        sim.phenodigm_score = math.sqrt(sim.jaccard_similarity * sim.ancestor_information_content)

        return sim

    def all_by_all_pairwise_similarity(
        self,
        subjects: Iterable[CURIE],
        objects: Iterable[CURIE],
        predicates: List[PRED_CURIE] = None,
        min_jaccard_similarity: Optional[float] = None,
        min_ancestor_information_content: Optional[float] = None,
    ) -> Iterator[TermPairwiseSimilarity]:
        """
        Compute similarity for all combinations of terms in subsets vs all terms in objects

        :param subjects:
        :param objects:
        :param predicates:
        :return:
        """
        objects = list(objects)
        logging.info(f"Calculating all-by-all pairwise similarity for {len(objects)} objects")
        semsimian = self._get_semsimian_object(
            predicates=predicates, attributes=self.term_pairwise_similarity_attributes
        )
        all_results = semsimian.all_by_all_pairwise_similarity(
            subject_terms=set(subjects),
            object_terms=set(objects),
            minimum_jaccard_threshold=min_jaccard_similarity,
            minimum_resnik_threshold=min_ancestor_information_content,
            # predicates=set(predicates) if predicates else None,
        )
        logging.info("Post-processing results from semsimian")
        for term1_key, values in all_results.items():
            for term2_key, result in values.items():
                # Remember the _ here is cosine_similarity which we do not use at the moment.
                jaccard, resnik, phenodigm_score, _, ancestor_set = result
                if len(ancestor_set) > 0:
                    sim = TermPairwiseSimilarity(
                        subject_id=term1_key,
                        object_id=term2_key,
                        ancestor_id=next(
                            iter(ancestor_set)
                        ),  # TODO: Change this: gets first element of the set
                    )
                    sim.jaccard_similarity = jaccard
                    sim.ancestor_information_content = resnik
                    sim.phenodigm_score = phenodigm_score
                else:
                    sim = TermPairwiseSimilarity(
                        subject_id=term1_key, object_id=term2_key, ancestor_id=OWL_THING
                    )
                    sim.jaccard_similarity = 0
                    sim.ancestor_information_content = 0
                yield sim

    def termset_pairwise_similarity_score_only(
        self,
        subjects: List[CURIE],
        objects: List[CURIE],
        predicates: List[PRED_CURIE] = None,
        labels=False,
    ) -> TermSetPairwiseSimilarity:
        """Return TermSetPairwiseSimilarity object.

        :param subjects: List of subject nodes.
        :param objects: List of object nodes.
        :param predicates: List of predicates, defaults to None
        :param labels: Boolean to get labels for all nodes from resource, defaults to False
        :param score_only: Boolean to return just the average score [TEMPORARY], defaults to False
        :return: TermSetPairwiseSimilarity object
        """
        semsimian = self._get_semsimian_object(
            predicates=predicates, attributes=self.termset_pairwise_similarity_attributes
        )
        sim = TermSetPairwiseSimilarity()
        # average_score = semsimian.termset_comparison(
        #     subject_terms=set(subjects),
        #     object_terms=set(objects),
        # )
        average_score = semsimian.termset_comparison(
            set(subjects),
            set(objects),
        )

        sim.average_score = average_score

        return sim
