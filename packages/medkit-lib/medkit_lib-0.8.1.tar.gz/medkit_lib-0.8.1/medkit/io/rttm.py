__all__ = ["RTTMInputConverter", "RTTMOutputConverter"]

import csv
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

from medkit.core import (
    generate_id,
    Attribute,
    InputConverter,
    OutputConverter,
    OperationDescription,
    ProvTracer,
    Store,
)
from medkit.core.audio import AudioDocument, FileAudioBuffer, Segment, Span


logger = logging.getLogger(__name__)

# cf https://github.com/nryant/dscore#rttm
_RTTM_FIELDS = [
    "type",
    "file_id",
    "channel",
    "onset",
    "duration",
    "na_1",
    "na_2",
    "speaker_name",
    "na_3",
    "na_4",
]


class RTTMInputConverter(InputConverter):
    """Convert Rich Transcription Time Marked (.rttm) files containing diarization
    information into turn segments.

    For each turn in a .rttm file, a
    :class:`~medkit.core.audio.annotation.Segment` will be created, with an
    associated :class:`~medkit.core.Attribute` holding the name of the turn
    speaker as value. The segments can be retrieved directly or as part of an
    :class:`~medkit.core.audio.document.AudioDocument` instance.

    If a :class:`~medkit.core.ProvTracer` is set, provenance information will be
    added for each segment and each attribute (referencing the input converter
    as the operation).
    """

    def __init__(
        self,
        turn_label: str = "turn",
        speaker_label: str = "speaker",
        store: Optional[Store] = None,
        converter_id: Optional[str] = None,
    ):
        """
        Parameters
        ----------
        turn_label:
            Label of segments representing turns in the .rttm file.
        speaker_label:
            Label of speaker attributes to add to each segment.
        store:
            Optional shared store to hold the annotations when adding them to
            audio documents.. If none provided, an internal store will be used
            for each document.
        converter_id:
            Identifier of the converter.
        """

        if converter_id is None:
            converter_id = generate_id()

        self.uid = converter_id
        self.turn_label = turn_label
        self.speaker_label = speaker_label
        self.store = store

        self._prov_tracer: Optional[ProvTracer] = None

    @property
    def description(self) -> OperationDescription:
        """Contains all the input converter init parameters."""
        return OperationDescription(
            uid=self.uid,
            name=self.__class__.__name__,
            class_name=self.__class__.__name__,
        )

    def set_prov_tracer(self, prov_tracer: ProvTracer):
        """Enable provenance tracing.

        Parameters
        ----------
        prov_tracer:
            The provenance tracer used to trace the provenance.
        """

        self._prov_tracer = prov_tracer

    def load(
        self,
        rttm_dir: Union[str, Path],
        audio_dir: Optional[Union[str, Path]] = None,
        audio_ext: str = ".wav",
    ) -> List[AudioDocument]:
        """
        Load all .rttm file in a directory into a list of
        :class:`~medkit.core.audio.document.AudioDocument` objects.

        For each .rttm file, they must be a corresponding audio file with the
        same basename, either in the same directory or in an separated audio
        directory.

        Parameters
        ----------
        rttm_dir:
            Directory containing the .rttm files.
        audio_dir:
            Directory containing the audio files corresponding to the .rttm files,
            if they are not in `rttm_dir`.
        audio_ext:
            File extension to use for audio files.

        Returns
        -------
        List[AudioDocument]
            List of generated documents.
        """

        rttm_dir = Path(rttm_dir)
        if audio_dir is not None:
            audio_dir = Path(audio_dir)

        docs = []
        for rttm_file in sorted(rttm_dir.glob("*.rttm")):
            # corresponding audio file must have same base name with audio extension,
            # either in the same directory or in audio_dir if provided
            if audio_dir:
                audio_file = (audio_dir / rttm_file.stem).with_suffix(audio_ext)
            else:
                audio_file = rttm_file.with_suffix(audio_ext)

            doc = self.load_doc(rttm_file, audio_file)
            docs.append(doc)

        if len(docs) == 0:
            logger.warning(f"No .rttm found in '{rttm_dir}'")

        return docs

    def load_doc(
        self, rttm_file: Union[str, Path], audio_file: Union[str, Path]
    ) -> AudioDocument:
        """Load a single .rttm file into an
        :class:`~medkit.core.audio.document.AudioDocument`.

        Parameters
        ----------
        rttm_file:
            Path to the .rttm file.
        audio_file:
            Path to the corresponding audio file.

        Returns
        -------
        AudioDocument:
            Generated document.
        """

        rttm_file = Path(rttm_file)
        audio_file = Path(audio_file)

        rows = self._load_rows(rttm_file)
        full_audio = FileAudioBuffer(path=audio_file)
        turn_segments = [self._build_turn_segment(row, full_audio) for row in rows]

        doc = AudioDocument(audio=full_audio)
        for turn_segment in turn_segments:
            doc.anns.add(turn_segment)

        return doc

    def load_turns(
        self, rttm_file: Union[str, Path], audio_file: Union[str, Path]
    ) -> List[Segment]:
        """Load a .rttm file and return a list of
        :class:`~medkit.core.audio.annotation.Segment` objects.

        Parameters
        ----------
        rttm_file:
            Path to the .rttm file.
        audio_file:
            Path to the corresponding audio file.

        Returns
        -------
        List[:class:`~medkit.core.audio.annotation.Segment`]:
            Turn segments as found in the .rttm file.
        """

        rttm_file = Path(rttm_file)
        audio_file = Path(audio_file)

        rows = self._load_rows(rttm_file)
        full_audio = FileAudioBuffer(path=audio_file)
        turn_segments = [self._build_turn_segment(row, full_audio) for row in rows]
        return turn_segments

    @staticmethod
    def _load_rows(rttm_file: Path):
        with open(rttm_file) as fp:
            csv_reader = csv.DictReader(fp, fieldnames=_RTTM_FIELDS, delimiter=" ")
            rows = [r for r in csv_reader]

        file_id = rows[0]["file_id"]
        if not all(r["file_id"] == file_id for r in rows):
            raise RuntimeError(
                "Multi-file .rttm are not supported, all entries should have same"
                " file_id or <NA>"
            )

        return rows

    def _build_turn_segment(
        self, row: Dict[str, Any], full_audio: FileAudioBuffer
    ) -> Segment:
        start = float(row["onset"])
        end = start + float(row["duration"])
        audio = full_audio.trim_duration(start, end)
        segment = Segment(label=self.turn_label, span=Span(start, end), audio=audio)
        speaker_attr = Attribute(label=self.speaker_label, value=row["speaker_name"])
        segment.attrs.add(speaker_attr)

        if self._prov_tracer is not None:
            self._prov_tracer.add_prov(segment, self.description, source_data_items=[])
            self._prov_tracer.add_prov(
                speaker_attr, self.description, source_data_items=[]
            )

        return segment


class RTTMOutputConverter(OutputConverter):
    """Build Rich Transcription Time Marked (.rttm) files containing diarization
    information from :class:`~medkit.core.audio.annotation.Segment` objects.

    There must be a segment for each turn, with an associated
    :class:`~medkit.core.Attribute` holding the name of the turn speaker as
    value. The segments can be passed directly or as part of
    :class:`~medkit.core.audio.document.AudioDocument` instances.
    """

    def __init__(self, turn_label: str = "turn", speaker_label: str = "speaker"):
        """
        Parameters
        ----------
        turn_label:
            Label of segments representing turns in the audio documents.
        speaker_label:
            Label of speaker attributes attached to each turn segment.
        """

        super().__init__()

        self.turn_label = turn_label
        self.speaker_label = speaker_label

    def save(
        self,
        docs: List[AudioDocument],
        rttm_dir: Union[str, Path],
        doc_names: Optional[List[str]] = None,
    ):
        """Save :class:`~medkit.core.audio.document.AudioDocument` instances as
        .rttm files in a directory.

        Parameters
        ----------
        docs:
            List of audio documents to save.
        rttm_dir:
            Directory into which the generated .rttm files will be stored.
        doc_names:
            Optional list of names to use as basenames and file ids for the
            generated .rttm files (2d column). If none provided, the document
            ids will be used.
        """

        rttm_dir = Path(rttm_dir)

        if doc_names is not None:
            if len(doc_names) != len(docs):
                raise ValueError(
                    "doc_names must have the same length as docs when provided"
                )
        else:
            doc_names = [doc.uid for doc in docs]

        rttm_dir.mkdir(parents=True, exist_ok=True)

        for doc_name, doc in zip(doc_names, docs):
            rttm_file = rttm_dir / f"{doc_name}.rttm"
            self.save_doc(doc, rttm_file=rttm_file, rttm_doc_id=doc_name)

    def save_doc(
        self,
        doc: AudioDocument,
        rttm_file: Union[str, Path],
        rttm_doc_id: Optional[str] = None,
    ):
        """Save a single :class:`~medkit.core.audio.document.AudioDocument` as a
        .rttm file.

        Parameters
        ----------
        doc:
            Audio document to save.
        rttm_file:
            Path of the generated .rttm file.
        rttm_doc_id:
            File uid to use for the generated .rttm file (2d column). If none
            provided, the document uid will be used.
        """

        rttm_file = Path(rttm_file)
        if rttm_doc_id is None:
            rttm_doc_id = doc.uid

        turns = doc.anns.get(label=self.turn_label)
        self.save_turn_segments(turns, rttm_file, rttm_doc_id)

    def save_turn_segments(
        self,
        turn_segments: List[Segment],
        rttm_file: Union[str, Path],
        rttm_doc_id: Optional[str],
    ):
        """Save :class:`~medkit.core.audio.annotation.Segment` objects into a .rttm file.

        Parameters
        ----------
        turn_segments:
            Turn segments to save.
        rttm_file:
            Path of the generated .rttm file.
        rttm_doc_id:
            File uid to use for the generated .rttm file (2d column).
        """

        rttm_file = Path(rttm_file)

        rows = [self._build_rttm_row(s, rttm_doc_id) for s in turn_segments]
        rows.sort(key=lambda r: r["onset"])

        with open(rttm_file, mode="w", encoding="utf-8") as fp:
            csv_writer = csv.DictWriter(fp, fieldnames=_RTTM_FIELDS, delimiter=" ")
            csv_writer.writerows(rows)

    def _build_rttm_row(
        self, turn_segment: Segment, rttm_doc_id: Optional[str]
    ) -> Dict[str, Any]:
        speaker_attrs = turn_segment.attrs.get(label=self.speaker_label)
        if len(speaker_attrs) == 0:
            raise RuntimeError(
                f"Found no attribute with label '{self.speaker_label}' on turn segment"
            )

        speaker_attr = speaker_attrs[0]
        span = turn_segment.span

        row = {
            "type": "SPEAKER",
            "file_id": rttm_doc_id if rttm_doc_id is not None else "<NA>",
            "channel": "1",
            "onset": f"{span.start:.3f}",
            "duration": f"{span.length:.3f}",
            "na_1": "<NA>",
            "na_2": "<NA>",
            "speaker_name": speaker_attr.value,
            "na_3": "<NA>",
            "na_4": "<NA>",
        }
        return row
