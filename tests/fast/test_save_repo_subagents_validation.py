"""Regression test: save_repo_subagents() validates the disabled list.

The endpoint must reject (1) unknown agent names and (2) the all-disabled
case — a run needs at least one subagent. A valid partial list is persisted;
an empty list deletes the setting (full roster re-enabled).
"""

from __future__ import annotations

import sys
from contextlib import asynccontextmanager
from typing import Any
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import HTTPException

# Stub out modules that require live services before importing settings endpoint.
if "db.connection" not in sys.modules:
    sys.modules["db.connection"] = MagicMock()
if "db.models" not in sys.modules:
    sys.modules["db.models"] = MagicMock()

_auth_mock = MagicMock()
_auth_mock.verify_api_key = MagicMock(return_value=None)
sys.modules["backend.auth"] = _auth_mock

import backend.endpoints.settings as settings_mod  # noqa: E402
from backend.models import SaveDisabledSubagentsRequest  # noqa: E402
from config.loader import load_subagents  # noqa: E402


def _make_session_ctx() -> Any:
    """Async context manager yielding a session that records upserts/deletes."""
    session_mock = AsyncMock()
    session_mock.get = AsyncMock(return_value=None)
    session_mock.commit = AsyncMock()
    session_mock.delete = AsyncMock()

    @asynccontextmanager
    async def ctx():  # type: ignore[return]
        yield session_mock

    return ctx, session_mock


class TestSaveRepoSubagentsValidation:
    """save_repo_subagents() rejects bad input and persists valid lists."""

    @pytest.mark.asyncio
    async def test_unknown_name_raises_422(self) -> None:
        body = SaveDisabledSubagentsRequest(disabled=["not-a-real-agent"])
        ctx, _ = _make_session_ctx()
        with patch.object(settings_mod, "session", ctx):
            with pytest.raises(HTTPException) as exc:
                await settings_mod.save_repo_subagents("org/repo", body)
        assert exc.value.status_code == 422
        assert "Unknown subagent" in exc.value.detail

    @pytest.mark.asyncio
    async def test_disabling_all_raises_422(self) -> None:
        all_names = [s.name for s in load_subagents()]
        body = SaveDisabledSubagentsRequest(disabled=all_names)
        ctx, _ = _make_session_ctx()
        with patch.object(settings_mod, "session", ctx):
            with pytest.raises(HTTPException) as exc:
                await settings_mod.save_repo_subagents("org/repo", body)
        assert exc.value.status_code == 422
        assert "at least one" in exc.value.detail

    @pytest.mark.asyncio
    async def test_valid_partial_list_upserts(self) -> None:
        body = SaveDisabledSubagentsRequest(disabled=["ui-reviewer"])
        ctx, session_mock = _make_session_ctx()
        with (
            patch.object(settings_mod, "session", ctx),
            patch.object(settings_mod, "upsert_setting", new_callable=AsyncMock) as upsert,
        ):
            result = await settings_mod.save_repo_subagents("org/repo", body)
        assert result["ok"] is True
        assert result["disabled_count"] == 1
        upsert.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_empty_list_deletes_setting(self) -> None:
        body = SaveDisabledSubagentsRequest(disabled=[])
        ctx, session_mock = _make_session_ctx()
        existing = MagicMock()
        session_mock.get = AsyncMock(return_value=existing)
        with patch.object(settings_mod, "session", ctx):
            result = await settings_mod.save_repo_subagents("org/repo", body)
        assert result["disabled_count"] == 0
        session_mock.delete.assert_awaited_once_with(existing)
