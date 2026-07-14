"""Regression test: summarize must clamp strings nested inside containers.

The Task tool returns {"task": {"output": <transcript>, "result": <same>}}. The
old summarize only clamped top-level strings and copied any non-string value by
reference, so a nested dict passed through whole: a subagent that died mid-stream
had its raw JSONL transcript stored twice, landing a 521 kB row in tool_calls
where a healthy Agent row is ~4 kB. Clamping now recurses into dicts and lists.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "sandbox"))

from constants import (  # noqa: E402
    INPUT_SUMMARY_MAX_LEN,
    SUMMARY_MAX_DEPTH,
    SUMMARY_MAX_ITEMS,
    SUMMARY_TRUNCATED_KEY,
)
from sdk.utils import summarize  # noqa: E402


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
