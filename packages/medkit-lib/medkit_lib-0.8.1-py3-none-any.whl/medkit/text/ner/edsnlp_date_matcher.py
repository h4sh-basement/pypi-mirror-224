"""
This module needs extra-dependencies not installed as core dependencies of medkit.
To install them, use `pip install medkit-lib[edsnlp]`.
"""

__all__ = ["EDSNLPDateMatcher"]

from typing import Iterator, List, Optional

import spacy

from medkit.core.text.operation import NEROperation
from medkit.core.text import Segment, Entity
from medkit.core.text import span_utils
from medkit.text.spacy.edsnlp import build_date_attribute


class EDSNLPDateMatcher(NEROperation):
    """
    Date matcher based on `EDS-NPL's dates pipeline
    <https://aphp.github.io/edsnlp/latest/pipelines/misc/dates/>`_ which itself
    relies on regular expressions. Note that this operation is designed to run
    on french documents.

    Absolute dates (ex: "23/08/2021"), relatives dates (ex: "la semaine
    dernière") and durations (ex: "pendant quatre jours") will be matched.

    For each date that is found, an entity will be created with an attribute
    attached to it containing normalized values if the date components. The
    attribute label will always be "date", and the class of the attribute will
    be either class :class:`~medkit.text.ner.DateAttribute`,
    :class:`~medkit.text.ner.RelativeDateAttribute` or
    :class:`~medkit.text.ner.DurationAttribute`.
    """

    def __init__(
        self,
        output_label: str = "date",
        attrs_to_copy: Optional[List[str]] = None,
        uid: Optional[str] = None,
    ):
        """
        Parameters
        ----------
        output_label:
            Label to use for date entities created (the label of the
            attributes will always be "date")
        attrs_to_copy:
            Labels of the attributes that should be copied from the input segment
            to the created date entity. Useful for propagating context attributes
            (negation, antecedent, etc).
        uid:
            Identifier of the matcher
        """

        super().__init__(
            output_label=output_label, attrs_to_copy=attrs_to_copy, uid=uid
        )

        if attrs_to_copy is None:
            attrs_to_copy = []

        self.output_label = output_label
        self.attrs_to_copy = attrs_to_copy

        self._edsnlp = spacy.blank("eds")
        self._edsnlp.add_pipe("eds.dates")

    def run(self, segments: List[Segment]) -> List[Entity]:
        """Find and return date entities for all `segments`

        Parameters
        ----------
        segments:
            List of segments into which to look for date mentions

        Returns
        -------
        entities: List[Entity]
            Date entities found in `segments`, with
            :class:`~medkit.text.ner.DateAttribute`,
            :class:`~medkit.text.ner.RelativeDateAttribute` or
            :class:`~medkit.text.ner.DurationAttribute` attributes.
        """

        spacy_docs = self._edsnlp.pipe(s.text for s in segments)
        return [
            date_entity
            for segment, spacy_doc in zip(segments, spacy_docs)
            for date_entity in self._find_dates_in_segment(segment, spacy_doc)
        ]

    def _find_dates_in_segment(self, segment, spacy_doc) -> Iterator[Entity]:
        for spacy_span in spacy_doc.spans["dates"]:
            # convert span span start/end to medkit spans relative to doc
            text, spans = span_utils.extract(
                segment.text,
                segment.spans,
                [(spacy_span.start_char, spacy_span.end_char)],
            )
            # create attribute storing normalized date values
            attr = build_date_attribute(spacy_span=spacy_span, spacy_label="date")
            # create entity
            entity = Entity(
                label=self.output_label, spans=spans, text=text, attrs=[attr]
            )

            # handle provenance
            if self._prov_tracer is not None:
                self._prov_tracer.add_prov(
                    entity, self.description, source_data_items=[segment]
                )
                self._prov_tracer.add_prov(
                    attr, self.description, source_data_items=[segment]
                )

            # copy attrs from source segment to date entity
            for label in self.attrs_to_copy:
                for attr in segment.attrs.get(label=label):
                    copied_attr = attr.copy()
                    entity.attrs.add(copied_attr)
                    # handle provenance
                    if self._prov_tracer is not None:
                        self._prov_tracer.add_prov(
                            copied_attr, self.description, [attr]
                        )

            yield entity
