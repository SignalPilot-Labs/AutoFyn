"""Verify Python and TypeScript model ID lists stay in sync.

Python source of truth: db.constants.VALID_MODELS
TypeScript mirror: dashboard/frontend/lib/constants.ts MODEL_IDS array

A companion TypeScript test (models.test.ts) validates the frontend
constants internally. This test ensures the two languages agree.
"""

import re
from pathlib import Path

from db.constants import VALID_MODELS, DEFAULT_MODEL

TS_CONSTANTS_PATH = Path("dashboard/frontend/lib/constants.ts")


class TestModelSync:
    """Python VALID_MODELS must match TypeScript MODEL_IDS."""

    def _extract_ts_model_ids(self) -> list[str]:
        """Parse MODEL_IDS array from the TypeScript constants file."""
        content = TS_CONSTANTS_PATH.read_text(encoding="utf-8")
        match = re.search(
            r'export const MODEL_IDS.*?=\s*\[(.*?)\]',
            content,
            re.DOTALL,
        )
        assert match, "MODEL_IDS not found in constants.ts"
        raw = match.group(1)
        return re.findall(r'"([^"]+)"', raw)

    def _extract_ts_default(self) -> str:
        """Parse DEFAULT_MODEL from the TypeScript constants file."""
        content = TS_CONSTANTS_PATH.read_text(encoding="utf-8")
        match = re.search(
            r'export const DEFAULT_MODEL.*?=\s*"([^"]+)"',
            content,
        )
        assert match, "DEFAULT_MODEL not found in constants.ts"
        return match.group(1)

    def test_model_ids_match(self) -> None:
        """TypeScript MODEL_IDS must contain exactly the same IDs as Python VALID_MODELS."""
        ts_ids = set(self._extract_ts_model_ids())
        py_ids = set(VALID_MODELS)
        assert ts_ids == py_ids, (
            f"Model ID mismatch:\n"
            f"  Python only: {py_ids - ts_ids}\n"
            f"  TypeScript only: {ts_ids - py_ids}"
        )

    def test_default_model_matches(self) -> None:
        """TypeScript DEFAULT_MODEL must match Python DEFAULT_MODEL."""
        ts_default = self._extract_ts_default()
        assert ts_default == DEFAULT_MODEL, (
            f"DEFAULT_MODEL mismatch: Python={DEFAULT_MODEL}, TypeScript={ts_default}"
        )
