"""Regression test: the _truncated flag must mean summarize clamped the payload.

summarize appended SUMMARY_TRUNCATED_KEY to the summarized dict without checking
whether the payload already carried that key. A tool sending its own _truncated
field had it silently overwritten with True whenever something else in the same
payload clamped, and preserved verbatim when nothing did — so the field's type
flipped between str and bool depending on the size of unrelated values.

The flag is now ours alone: an incoming _truncated is dropped, and dropping it
is itself a truncation, so the payload is reported as clamped rather than
quietly losing a field.
"""

from __future__ import annotations

from constants import INPUT_SUMMARY_MAX_LEN, SUMMARY_TRUNCATED_KEY
from sdk.utils import summarize


class TestSummarizeTruncatedFlagIsOurs:
    """A payload's own _truncated key must never be mistaken for our flag."""

    def test_incoming_flag_is_not_preserved_as_data(self) -> None:
        """A payload's own _truncated must not survive as its original value."""
        payload = {"task": {"x": 1}, SUMMARY_TRUNCATED_KEY: "user data here"}

        out = summarize(payload)

        assert out[SUMMARY_TRUNCATED_KEY] is True

    def test_dropping_the_incoming_flag_is_reported(self) -> None:
        """Losing a field is a truncation, so the payload is flagged as clamped."""
        payload = {"task": {"x": 1}, SUMMARY_TRUNCATED_KEY: "user data here"}

        out = summarize(payload)

        assert out[SUMMARY_TRUNCATED_KEY] is True
        assert out["task"] == {"x": 1}

    def test_flag_type_is_stable_regardless_of_other_values(self) -> None:
        """The flag stays bool whether or not something else in the payload clamps.

        This is the actual defect: the same incoming key rendered as a str when
        nothing clamped and as a bool when something did.
        """
        small = {"task": {"output": "ok"}, SUMMARY_TRUNCATED_KEY: "user data"}
        large = {
            "task": {"output": "A" * (INPUT_SUMMARY_MAX_LEN + 1)},
            SUMMARY_TRUNCATED_KEY: "user data",
        }

        assert summarize(small)[SUMMARY_TRUNCATED_KEY] is True
        assert summarize(large)[SUMMARY_TRUNCATED_KEY] is True

    def test_clean_payload_is_still_unflagged(self) -> None:
        """A payload without the key and without clamping carries no flag."""
        out = summarize({"task": {"output": "Report written to /tmp/round-1/x.md"}})

        assert SUMMARY_TRUNCATED_KEY not in out
