from __future__ import annotations

import pytest
from transformers import AutoTokenizer, PreTrainedTokenizerFast

from sequence_label import LabelSet, SequenceLabel
from sequence_label.transformers import get_alignments


@pytest.fixture
def tokenizer() -> PreTrainedTokenizerFast:
    return AutoTokenizer.from_pretrained("distilroberta-base")


@pytest.fixture
def label_set() -> LabelSet:
    return LabelSet({"ORG", "LOC", "PER", "MISC"})


@pytest.mark.parametrize(
    "text, tag_indices, expected",
    [
        (
            "Tokyo is the capital of Japan.",
            [[0, 1, 3, 0, 0, 0, 0, 4, 0, 0]],
            (
                SequenceLabel.from_dict(
                    tags=[
                        {"start": 0, "end": 5, "label": "LOC"},
                        {"start": 24, "end": 29, "label": "LOC"},
                    ],
                    size=30,
                ),
            ),
        ),
        (
            "John Doe",
            [[0, 16, 16, 0]],
            (
                SequenceLabel.from_dict(
                    tags=[
                        {"start": 0, "end": 4, "label": "PER"},
                        {"start": 5, "end": 8, "label": "PER"},
                    ],
                    size=8,
                ),
            ),
        ),
        (
            "John Doe",
            [[0, 13, 15, 0]],
            (
                SequenceLabel.from_dict(
                    tags=[{"start": 0, "end": 8, "label": "PER"}], size=8
                ),
            ),
        ),
    ],
)
def test_decoded_labels_are_valid(
    tokenizer: PreTrainedTokenizerFast,
    label_set: LabelSet,
    text: str,
    tag_indices: list[list[int]],
    expected: tuple[SequenceLabel, ...],
) -> None:
    batch_encoding = tokenizer(text)

    alignments = get_alignments(batch_encoding=batch_encoding, char_lengths=[len(text)])

    labels = label_set.decode(tag_indices=tag_indices, alignments=alignments)

    assert labels == expected


@pytest.mark.parametrize(
    "text, labels, expected",
    [
        (
            "Tokyo is the capital of Japan.",
            (
                SequenceLabel.from_dict(
                    tags=[
                        {"start": 0, "end": 5, "label": "LOC"},
                        {"start": 24, "end": 29, "label": "LOC"},
                    ],
                    size=30,
                ),
            ),
            [[0, 1, 3, 0, 0, 0, 0, 4, 0, 0]],
        ),
        (
            "Tokyo is the capital of Japan." * 100,
            (
                SequenceLabel.from_dict(
                    tags=[
                        {"start": start, "end": end, "label": "LOC"}
                        for i in range(100)
                        for start, end in (
                            (30 * i, 30 * i + 5),
                            (24 + 30 * i, 24 + 30 * i + 5),
                        )
                    ],
                    size=3000,
                ),
            ),
            [[0] + [1, 3, 0, 0, 0, 0, 4, 0] * 63 + [1, 3, 0, 0, 0, 0] + [0]],
        ),
    ],
)
def test_tag_indices_are_valid(
    tokenizer: PreTrainedTokenizerFast,
    label_set: LabelSet,
    text: str,
    labels: tuple[SequenceLabel, ...],
    expected: list[list[int]],
) -> None:
    batch_encoding = tokenizer([text], truncation=True)
    alignments = get_alignments(batch_encoding=batch_encoding, char_lengths=[len(text)])

    tag_indices = label_set.encode_to_tag_indices(labels=labels, alignments=alignments)

    assert tag_indices == expected


params = [
    (
        "The Tokyo Metropolitan Government is the government of the Tokyo Metropolis.",
        (
            SequenceLabel.from_dict(
                tags=[
                    {"start": 4, "end": 33, "label": "ORG"},
                    {"start": 4, "end": 9, "label": "LOC"},
                    {"start": 59, "end": 64, "label": "LOC"},
                ],
                size=76,
            ),
        ),
        [
            [
                [
                    True,  # O
                    False,  # B-LOC
                    False,  # I-LOC
                    False,  # L-LOC
                    False,  # U-LOC
                    False,  # B-MISC
                    False,  # I-MISC
                    False,  # L-MISC
                    False,  # U-MISC
                    False,  # B-ORG
                    False,  # I-ORG
                    False,  # L-ORG
                    False,  # U-ORG
                    False,  # B-PER
                    False,  # I-PER
                    False,  # L-PER
                    False,  # U-PER
                ],
                [  # The
                    True,  # O
                    False,  # B-LOC
                    False,  # I-LOC
                    False,  # L-LOC
                    False,  # U-LOC
                    False,  # B-MIS
                    False,  # I-MIS
                    False,  # L-MIS
                    False,  # U-MIS
                    False,  # B-ORG
                    False,  # I-ORG
                    False,  # L-ORG
                    False,  # U-ORG
                    False,  # B-PER
                    False,  # I-PER
                    False,  # L-PER
                    False,  # U-PER
                ],
                [  # Tokyo
                    False,  # O
                    False,  # B-LOC
                    False,  # I-LOC
                    False,  # L-LOC
                    True,  # U-LOC
                    False,  # B-MISC
                    False,  # I-MISC
                    False,  # L-MISC
                    False,  # U-MISC
                    True,  # B-ORG
                    False,  # I-ORG
                    False,  # L-ORG
                    False,  # U-ORG
                    False,  # B-PER
                    False,  # I-PER
                    False,  # L-PER
                    False,  # U-PER
                ],
                [  # Metropolitan
                    False,  # O
                    False,  # B-LOC
                    False,  # I-LOC
                    False,  # L-LOC
                    False,  # U-LOC
                    False,  # B-MIS
                    False,  # I-MIS
                    False,  # L-MIS
                    False,  # U-MIS
                    False,  # B-ORG
                    True,  # I-ORG
                    False,  # L-ORG
                    False,  # U-ORG
                    False,  # B-PER
                    False,  # I-PER
                    False,  # L-PER
                    False,  # U-PER
                ],
                [  # Government
                    False,  # O
                    False,  # B-LOC
                    False,  # I-LOC
                    False,  # L-LOC
                    False,  # U-LOC
                    False,  # B-MIS
                    False,  # I-MIS
                    False,  # L-MIS
                    False,  # U-MIS
                    False,  # B-ORG
                    False,  # I-ORG
                    True,  # L-ORG
                    False,  # U-ORG
                    False,  # B-PER
                    False,  # I-PER
                    False,  # L-PER
                    False,  # U-PER
                ],
                [  # is
                    True,  # O
                    False,  # B-LOC
                    False,  # I-LOC
                    False,  # L-LOC
                    False,  # U-LOC
                    False,  # B-MIS
                    False,  # I-MIS
                    False,  # L-MIS
                    False,  # U-MIS
                    False,  # B-ORG
                    False,  # I-ORG
                    False,  # L-ORG
                    False,  # U-ORG
                    False,  # B-PER
                    False,  # I-PER
                    False,  # L-PER
                    False,  # U-PER
                ],
                [  # the
                    True,  # O
                    False,  # B-LOC
                    False,  # I-LOC
                    False,  # L-LOC
                    False,  # U-LOC
                    False,  # B-MIS
                    False,  # I-MIS
                    False,  # L-MIS
                    False,  # U-MIS
                    False,  # B-ORG
                    False,  # I-ORG
                    False,  # L-ORG
                    False,  # U-ORG
                    False,  # B-PER
                    False,  # I-PER
                    False,  # L-PER
                    False,  # U-PER
                ],
                [  # government
                    True,  # O
                    False,  # B-LOC
                    False,  # I-LOC
                    False,  # L-LOC
                    False,  # U-LOC
                    False,  # B-MIS
                    False,  # I-MIS
                    False,  # L-MIS
                    False,  # U-MIS
                    False,  # B-ORG
                    False,  # I-ORG
                    False,  # L-ORG
                    False,  # U-ORG
                    False,  # B-PER
                    False,  # I-PER
                    False,  # L-PER
                    False,  # U-PER
                ],
                [  # of
                    True,  # O
                    False,  # B-LOC
                    False,  # I-LOC
                    False,  # L-LOC
                    False,  # U-LOC
                    False,  # B-MIS
                    False,  # I-MIS
                    False,  # L-MIS
                    False,  # U-MIS
                    False,  # B-ORG
                    False,  # I-ORG
                    False,  # L-ORG
                    False,  # U-ORG
                    False,  # B-PER
                    False,  # I-PER
                    False,  # L-PER
                    False,  # U-PER
                ],
                [  # the
                    True,  # O
                    False,  # B-LOC
                    False,  # I-LOC
                    False,  # L-LOC
                    False,  # U-LOC
                    False,  # B-MIS
                    False,  # I-MIS
                    False,  # L-MIS
                    False,  # U-MIS
                    False,  # B-ORG
                    False,  # I-ORG
                    False,  # L-ORG
                    False,  # U-ORG
                    False,  # B-PER
                    False,  # I-PER
                    False,  # L-PER
                    False,  # U-PER
                ],
                [  # Tokyo
                    False,  # O
                    False,  # B-LOC
                    False,  # I-LOC
                    False,  # L-LOC
                    True,  # U-LOC
                    False,  # B-MIS
                    False,  # I-MIS
                    False,  # L-MIS
                    False,  # U-MIS
                    False,  # B-ORG
                    False,  # I-ORG
                    False,  # L-ORG
                    False,  # U-ORG
                    False,  # B-PER
                    False,  # I-PER
                    False,  # L-PER
                    False,
                ],
                [  # Met
                    True,  # O
                    False,  # B-LOC
                    False,  # I-LOC
                    False,  # L-LOC
                    False,  # U-LOC
                    False,  # B-MIS
                    False,  # I-MIS
                    False,  # L-MIS
                    False,  # U-MIS
                    False,  # B-ORG
                    False,  # I-ORG
                    False,  # L-ORG
                    False,  # U-ORG
                    False,  # B-PER
                    False,  # I-PER
                    False,  # L-PER
                    False,  # U-PER
                ],
                [  # ropolis
                    True,  # O
                    False,  # B-LOC
                    False,  # I-LOC
                    False,  # L-LOC
                    False,  # U-LOC
                    False,  # B-MIS
                    False,  # I-MIS
                    False,  # L-MIS
                    False,  # U-MIS
                    False,  # B-ORG
                    False,  # I-ORG
                    False,  # L-ORG
                    False,  # U-ORG
                    False,  # B-PER
                    False,  # I-PER
                    False,  # L-PER
                    False,  # U-PER
                ],
                [  # .
                    True,  # O
                    False,  # B-LOC
                    False,  # I-LOC
                    False,  # L-LOC
                    False,  # U-LOC
                    False,  # B-MIS
                    False,  # I-MIS
                    False,  # L-MIS
                    False,  # U-MIS
                    False,  # B-ORG
                    False,  # I-ORG
                    False,  # L-ORG
                    False,  # U-ORG
                    False,  # B-PER
                    False,  # I-PER
                    False,  # L-PER
                    False,  # U-PER
                ],
                [
                    True,  # O
                    False,  # B-LOC
                    False,  # I-LOC
                    False,  # L-LOC
                    False,  # U-LOC
                    False,  # B-MIS
                    False,  # I-MIS
                    False,  # L-MIS
                    False,  # U-MIS
                    False,  # B-ORG
                    False,  # I-ORG
                    False,  # L-ORG
                    False,  # U-ORG
                    False,  # B-PER
                    False,  # I-PER
                    False,  # L-PER
                    False,  # U-PER
                ],
            ]
        ],
    ),
    (
        "John Doe is a multiple-use placeholder name.",
        (
            SequenceLabel.from_dict(
                tags=[
                    {"start": 0, "end": 4, "label": "PER"},
                    {"start": 5, "end": 8, "label": "PER"},
                    {"start": 0, "end": 8, "label": "PER"},
                ],
                size=44,
            ),
        ),
        [
            [
                [
                    True,  # O
                    False,  # B-LOC
                    False,  # I-LOC
                    False,  # L-LOC
                    False,  # U-LOC
                    False,  # B-MIS
                    False,  # I-MIS
                    False,  # L-MIS
                    False,  # U-MIS
                    False,  # B-ORG
                    False,  # I-ORG
                    False,  # L-ORG
                    False,  # U-ORG
                    False,  # B-PER
                    False,  # I-PER
                    False,  # L-PER
                    False,  # U-PER
                ],
                [  # John
                    False,  # O
                    False,  # B-LOC
                    False,  # I-LOC
                    False,  # L-LOC
                    False,  # U-LOC
                    False,  # B-MIS
                    False,  # I-MIS
                    False,  # L-MIS
                    False,  # U-MIS
                    False,  # B-ORG
                    False,  # I-ORG
                    False,  # L-ORG
                    False,  # U-ORG
                    True,  # B-PER
                    False,  # I-PER
                    False,  # L-PER
                    True,  # U-PER
                ],
                [  # Doe
                    False,  # O
                    False,  # B-LOC
                    False,  # I-LOC
                    False,  # L-LOC
                    False,  # U-LOC
                    False,  # B-MIS
                    False,  # I-MIS
                    False,  # L-MIS
                    False,  # U-MIS
                    False,  # B-ORG
                    False,  # I-ORG
                    False,  # L-ORG
                    False,  # U-ORG
                    False,  # B-PER
                    False,  # I-PER
                    True,  # L-PER
                    True,  # U-PER
                ],
                [
                    True,  # O
                    False,  # B-LOC
                    False,  # I-LOC
                    False,  # L-LOC
                    False,  # U-LOC
                    False,  # B-MIS
                    False,  # I-MIS
                    False,  # L-MIS
                    False,  # U-MIS
                    False,  # B-ORG
                    False,  # I-ORG
                    False,  # L-ORG
                    False,  # U-ORG
                    False,  # B-PER
                    False,  # I-PER
                    False,  # L-PER
                    False,  # U-PER
                ],
                [
                    True,  # O
                    False,  # B-LOC
                    False,  # I-LOC
                    False,  # L-LOC
                    False,  # U-LOC
                    False,  # B-MIS
                    False,  # I-MIS
                    False,  # L-MIS
                    False,  # U-MIS
                    False,  # B-ORG
                    False,  # I-ORG
                    False,  # L-ORG
                    False,  # U-ORG
                    False,  # B-PER
                    False,  # I-PER
                    False,  # L-PER
                    False,  # U-PER
                ],
                [
                    True,  # O
                    False,  # B-LOC
                    False,  # I-LOC
                    False,  # L-LOC
                    False,  # U-LOC
                    False,  # B-MIS
                    False,  # I-MIS
                    False,  # L-MIS
                    False,  # U-MIS
                    False,  # B-ORG
                    False,  # I-ORG
                    False,  # L-ORG
                    False,  # U-ORG
                    False,  # B-PER
                    False,  # I-PER
                    False,  # L-PER
                    False,  # U-PER
                ],
                [
                    True,  # O
                    False,  # B-LOC
                    False,  # I-LOC
                    False,  # L-LOC
                    False,  # U-LOC
                    False,  # B-MIS
                    False,  # I-MIS
                    False,  # L-MIS
                    False,  # U-MIS
                    False,  # B-ORG
                    False,  # I-ORG
                    False,  # L-ORG
                    False,  # U-ORG
                    False,  # B-PER
                    False,  # I-PER
                    False,  # L-PER
                    False,  # U-PER
                ],
                [
                    True,  # O
                    False,  # B-LOC
                    False,  # I-LOC
                    False,  # L-LOC
                    False,  # U-LOC
                    False,  # B-MIS
                    False,  # I-MIS
                    False,  # L-MIS
                    False,  # U-MIS
                    False,  # B-ORG
                    False,  # I-ORG
                    False,  # L-ORG
                    False,  # U-ORG
                    False,  # B-PER
                    False,  # I-PER
                    False,  # L-PER
                    False,  # U-PER
                ],
                [
                    True,  # O
                    False,  # B-LOC
                    False,  # I-LOC
                    False,  # L-LOC
                    False,  # U-LOC
                    False,  # B-MIS
                    False,  # I-MIS
                    False,  # L-MIS
                    False,  # U-MIS
                    False,  # B-ORG
                    False,  # I-ORG
                    False,  # L-ORG
                    False,  # U-ORG
                    False,  # B-PER
                    False,  # I-PER
                    False,  # L-PER
                    False,  # U-PER
                ],
                [
                    True,  # O
                    False,  # B-LOC
                    False,  # I-LOC
                    False,  # L-LOC
                    False,  # U-LOC
                    False,  # B-MIS
                    False,  # I-MIS
                    False,  # L-MIS
                    False,  # U-MIS
                    False,  # B-ORG
                    False,  # I-ORG
                    False,  # L-ORG
                    False,  # U-ORG
                    False,  # B-PER
                    False,  # I-PER
                    False,  # L-PER
                    False,  # U-PER
                ],
                [
                    True,  # O
                    False,  # B-LOC
                    False,  # I-LOC
                    False,  # L-LOC
                    False,  # U-LOC
                    False,  # B-MIS
                    False,  # I-MIS
                    False,  # L-MIS
                    False,  # U-MIS
                    False,  # B-ORG
                    False,  # I-ORG
                    False,  # L-ORG
                    False,  # U-ORG
                    False,  # B-PER
                    False,  # I-PER
                    False,  # L-PER
                    False,  # U-PER
                ],
                [
                    True,  # O
                    False,  # B-LOC
                    False,  # I-LOC
                    False,  # L-LOC
                    False,  # U-LOC
                    False,  # B-MIS
                    False,  # I-MIS
                    False,  # L-MIS
                    False,  # U-MIS
                    False,  # B-ORG
                    False,  # I-ORG
                    False,  # L-ORG
                    False,  # U-ORG
                    False,  # B-PER
                    False,  # I-PER
                    False,  # L-PER
                    False,  # U-PER
                ],
            ]
        ],
    ),
]


@pytest.mark.parametrize("text, labels, expected", params)
def test_tag_bitmap_is_valid(
    label_set: LabelSet,
    tokenizer: PreTrainedTokenizerFast,
    text: str,
    labels: tuple[SequenceLabel, ...],
    expected: list[list[list[bool]]],
) -> None:
    batch_encoding = tokenizer([text], truncation=True)
    alignments = get_alignments(batch_encoding=batch_encoding, char_lengths=[len(text)])

    tag_bitmap = label_set.encode_to_tag_bitmap(labels=labels, alignments=alignments)

    assert tag_bitmap == expected
