__all__ = ["DocPipeline"]

from typing import Dict, Generic, List, Optional, Tuple, cast

from medkit.core.annotation import AnnotationType
from medkit.core.document import Document
from medkit.core.operation import DocOperation
from medkit.core.pipeline import Pipeline
from medkit.core.prov_tracer import ProvTracer


class DocPipeline(DocOperation, Generic[AnnotationType]):
    """Wrapper around the `Pipeline` class that runs a pipeline on a list
    (or collection) of documents, retrieving input annotations from each document
    and attaching output annotations back to documents.
    """

    def __init__(
        self,
        pipeline: Pipeline,
        labels_by_input_key: Dict[str, List[str]],
        uid: Optional[str] = None,
    ):
        """Initialize the pipeline

        Parameters
        ----------
        pipeline:
            Pipeline to execute on documents.
            Annotations given to `pipeline` (corresponding to its `input_keys`) will
            be retrieved from documents, according to `labels_by_input`.
            Annotations returned by `pipeline` (corresponding to its `output_keys`)
            will be added to documents.
        labels_by_input_key:
            Labels of existing annotations that should be retrieved from
            documents and passed to the pipeline as input. One list of labels
            per input key.

            For the typical use case where the pipeline takes a text document
            raw segment as input with key "full_text":

            >>> doc_pipeline = DocPipeline(
            >>>     pipeline,
            >>>     labels_by_input={"full_text": [TextDocument.RAW_SEGMENT]},
            >>> )

            Because the values of `labels_by_input_key` are lists (one per
            input), it is possible to use annotation with different labels for
            the same input key.
        """

        # Pass all arguments to super (remove self)
        init_args = locals()
        init_args.pop("self")
        super().__init__(**init_args)

        self.pipeline = pipeline
        self.labels_by_input_key: Dict[str, List[str]] = labels_by_input_key

    def set_prov_tracer(self, prov_tracer: ProvTracer):
        self.pipeline.set_prov_tracer(prov_tracer)

    def run(self, docs: List[Document[AnnotationType]]) -> None:
        """Run the pipeline on a list of documents, adding
        the output annotations to each document

        Parameters
        ----------
        docs:
            The documents on which to run the pipeline.
            Labels to input keys association will be used to retrieve existing
            annotations from each document, and all output annotations will also
            be added to each corresponding document.
        """

        for doc in docs:
            self._process_doc(doc)

    def _process_doc(self, doc: Document[AnnotationType]):
        all_input_anns = []
        for input_key in self.pipeline.input_keys:
            labels = self.labels_by_input_key[input_key]
            input_anns = [ann for label in labels for ann in doc.anns.get(label=label)]
            all_input_anns.append(input_anns)
        all_output_anns = self.pipeline.run(*all_input_anns)

        # wrap output in tuple if necessary
        # (operations performing in-place modifications
        # have no output and return None,
        # operations with single output may return a
        # single list instead of a tuple of lists)
        if all_output_anns is None:
            all_output_anns = tuple()
        elif not isinstance(all_output_anns, tuple):
            all_output_anns = (all_output_anns,)

        # operations must return annotations of expected modality type
        all_output_anns = cast(Tuple[List[AnnotationType], ...], all_output_anns)

        # add output anns to doc
        for output_anns in all_output_anns:
            for output_ann in output_anns:
                doc.anns.add(output_ann)
