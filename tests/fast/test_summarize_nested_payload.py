"""Regression test: summarize must clamp strings nested inside containers.

The Task tool returns {"task": {"output": <transcript>, "result": <same>}}. The
old summarize only clamped top-level strings and copied any non-string value by
reference, so a nested dict passed through whole: a subagent that died mid-stream
had its raw JSONL transcript stored twice, landing a 521 kB row in tool_calls
where a healthy Agent row is ~4 kB. Clamping now recurses into dicts and lists.
"""

from __future__ import annotations

import json

from constants import (
    INPUT_SUMMARY_MAX_LEN,
    SUMMARY_MAX_DEPTH,
    SUMMARY_MAX_ITEMS,
    SUMMARY_TRUNCATED_KEY,
)
from sdk.utils import summarize


class TestSummarizeNestedPayload:
    """summarize must bound nested payloads and flag that it truncated them."""

    def test_nested_task_transcript_is_clamped(self) -> None:
        """A Task payload carrying a 396k transcript must not pass through whole."""
        blob = "X" * 396869
        payload = {
            "task": {
                "output": blob,
                "result": blob,
                "status": "failed",
                "task_id": "aaef52323b62899c0",
            },
            "retrieval_status": "success",
        }

        out = summarize(payload)

        assert len(out["task"]["output"]) < len(blob)
        assert len(out["task"]["result"]) < len(blob)
        assert len(json.dumps(out)) < len(json.dumps(payload)) // 100
        assert out[SUMMARY_TRUNCATED_KEY] is True

    def test_clamped_payload_keeps_scalar_fields(self) -> None:
        """Truncation must preserve the small fields that identify the failure."""
        payload = {"task": {"output": "Y" * 5000, "status": "failed", "task_id": "abc"}}

        out = summarize(payload)

        assert out["task"]["status"] == "failed"
        assert out["task"]["task_id"] == "abc"

    def test_small_payload_is_untouched_and_unflagged(self) -> None:
        """A healthy pointer-sized result must survive byte-identical."""
        payload = {"task": {"output": "Report written to /tmp/round-1/x.md"}}

        out = summarize(payload)

        assert out == payload
        assert SUMMARY_TRUNCATED_KEY not in out

    def test_nested_list_of_strings_is_clamped(self) -> None:
        """Strings inside a list must be clamped, not copied by reference."""
        payload = {"task": {"messages": ["Z" * 5000, "Z" * 5000]}}

        out = summarize(payload)

        assert all(len(m) <= INPUT_SUMMARY_MAX_LEN + 3 for m in out["task"]["messages"])
        assert out[SUMMARY_TRUNCATED_KEY] is True

    def test_depth_bound_stops_runaway_nesting(self) -> None:
        """Nesting past SUMMARY_MAX_DEPTH must be replaced, not walked forever."""
        payload: dict = {"leaf": "W" * 5000}
        for _ in range(SUMMARY_MAX_DEPTH + 3):
            payload = {"nest": payload}

        out = summarize(payload)

        assert len(json.dumps(out)) < INPUT_SUMMARY_MAX_LEN
        assert out[SUMMARY_TRUNCATED_KEY] is True

    def test_width_bound_caps_item_count(self) -> None:
        """A dict wider than SUMMARY_MAX_ITEMS must be capped and flagged."""
        payload = {"task": {f"k{i}": "v" for i in range(SUMMARY_MAX_ITEMS + 25)}}

        out = summarize(payload)

        assert len(out["task"]) == SUMMARY_MAX_ITEMS
        assert out[SUMMARY_TRUNCATED_KEY] is True

    def test_barely_over_limit_is_still_flagged(self) -> None:
        """A clamp that barely shrinks the payload must still be reported.

        Inferring truncation by comparing serialized sizes missed this: cutting
        1001 chars to 1000 and appending "..." nets out the same length, so the
        flag was silently dropped for originals in a narrow band past the limit.
        """
        payload = {"task": {"output": "A" * (INPUT_SUMMARY_MAX_LEN + 1)}}

        out = summarize(payload)

        assert len(out["task"]["output"]) == INPUT_SUMMARY_MAX_LEN + 3
        assert out[SUMMARY_TRUNCATED_KEY] is True

    def test_escaped_content_that_inflates_is_flagged(self) -> None:
        """Truncation must be reported even when escaping inflates the JSON.

        A payload of quotes serializes to roughly twice its length, so the
        clamped result could serialize longer than the original — the size
        comparison then read that as "nothing was truncated".
        """
        payload = {"task": {"output": '"' * (INPUT_SUMMARY_MAX_LEN + 1)}}

        out = summarize(payload)

        assert out[SUMMARY_TRUNCATED_KEY] is True

    def test_cyclic_payload_does_not_raise(self) -> None:
        """A self-referential payload must clamp, not crash.

        summarize runs inside a PreToolUse hook, so raising here would break the
        tool call rather than just its logging. The depth bound already handled
        cycles; serializing the original to measure it was what raised.
        """
        cycle: dict = {"name": "loop"}
        cycle["self"] = cycle

        out = summarize({"task": cycle})

        assert out[SUMMARY_TRUNCATED_KEY] is True
        assert json.dumps(out)
