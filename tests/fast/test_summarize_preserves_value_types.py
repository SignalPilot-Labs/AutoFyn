"""Regression test: truncation must never change a value's type.

The depth cap replaced any over-deep container with the string "...", so a
Write's structuredPatch[].lines — an array of diff lines sitting at depth 4 —
came back as a string. The dashboard maps over that array, and a string is
truthy, so its `(hunk.lines as string[]) || []` guard never fired: .map() threw
and the ErrorBoundary blanked the whole run timeline.

Observed on run 7867fceb, whose stored payload literally reads "lines": "...".

Consumers read these payloads by shape, so an emptied list stays a list and an
emptied dict stays a dict. That keeps the contract intact at any depth, rather
than moving the cliff one level deeper by raising the cap.
"""

from __future__ import annotations

import json

from constants import SUMMARY_MAX_DEPTH
from sdk.utils import summarize

# Verbatim shape of a Write tool result: lines sits at depth 4.
_WRITE_PAYLOAD = {
    "type": "update",
    "filePath": "/tmp/memory/run_state.md",
    "structuredPatch": [
        {
            "oldStart": 1,
            "oldLines": 9,
            "newStart": 1,
            "newLines": 21,
            "lines": ["+## Goal", "+solve it", "-old line"],
        }
    ],
}


class TestSummarizePreservesValueTypes:
    """A clamped payload must keep every value's type, whatever the depth."""

    def test_write_diff_lines_survive_as_a_list(self) -> None:
        """The dashboard maps over lines, so it must still be an array."""
        out = summarize(_WRITE_PAYLOAD)

        lines = out["structuredPatch"][0]["lines"]
        assert isinstance(lines, list)
        assert lines == ["+## Goal", "+solve it", "-old line"]

    def test_over_deep_list_is_emptied_not_stringified(self) -> None:
        """Past the cap a list becomes [], never a string."""
        payload: dict = {"leaf": ["a", "b"]}
        for _ in range(SUMMARY_MAX_DEPTH + 2):
            payload = {"nest": payload}

        out = summarize(payload)

        node = out
        while isinstance(node, dict) and "nest" in node:
            node = node["nest"]
        assert not isinstance(node, str)

    def test_over_deep_dict_is_emptied_not_stringified(self) -> None:
        """Past the cap a dict becomes {}, never a string."""
        payload: dict = {"leaf": {"k": "v"}}
        for _ in range(SUMMARY_MAX_DEPTH + 2):
            payload = {"nest": payload}

        out = summarize(payload)

        node = out
        while isinstance(node, dict) and "nest" in node:
            node = node["nest"]
        assert not isinstance(node, str)

    def test_cap_still_bounds_the_payload(self) -> None:
        """Preserving type must not stop the cap from dropping deep content."""
        payload: dict = {"leaf": ["X" * 5000] * 10}
        for _ in range(SUMMARY_MAX_DEPTH + 2):
            payload = {"nest": payload}

        out = summarize(payload)

        assert len(json.dumps(out)) < 500
