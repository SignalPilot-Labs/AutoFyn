"""Tests for runs_page_size — the run-list page size setting with constant fallback."""

from __future__ import annotations

import sys
from unittest.mock import AsyncMock, MagicMock

import pytest

# Stub out modules that require live services before importing the runs endpoint.
if "db.connection" not in sys.modules:
    sys.modules["db.connection"] = MagicMock()
if "backend.auth" not in sys.modules:
    _auth_mock = MagicMock()
    _auth_mock.verify_api_key = MagicMock(return_value=None)
    sys.modules["backend.auth"] = _auth_mock

import backend.endpoints.runs as runs_mod  # noqa: E402
from backend.constants import RUNS_PAGE_SIZE  # noqa: E402


def _session_returning(setting: MagicMock | None) -> MagicMock:
    s = MagicMock()
    s.get = AsyncMock(return_value=setting)
    return s


class TestRunsPageSizeSetting:
    """The runs_page_size setting must win; unset falls back to RUNS_PAGE_SIZE."""

    @pytest.mark.asyncio
    async def test_uses_setting_when_set(self) -> None:
        setting = MagicMock()
        setting.value = "30"
        assert await runs_mod.runs_page_size(_session_returning(setting)) == 30

    @pytest.mark.asyncio
    async def test_falls_back_to_constant_when_unset(self) -> None:
        assert await runs_mod.runs_page_size(_session_returning(None)) == RUNS_PAGE_SIZE

    @pytest.mark.asyncio
    async def test_non_integer_setting_raises(self) -> None:
        """A corrupt DB value must fail loudly, not silently fall back."""
        setting = MagicMock()
        setting.value = "many"
        with pytest.raises(ValueError):
            await runs_mod.runs_page_size(_session_returning(setting))
