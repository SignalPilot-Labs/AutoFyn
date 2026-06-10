"""Regression test: get_repo_subagents merges core + cached user agents.

Settings shows the same list a run uses: core (shipped) agents (source=core)
plus the repo's cached user-defined agents (source=user), the user agent
winning on a name collision. User agents come from the cache the agent writes
at run time; a repo never run yet (no cache row) shows core agents only.
"""

from __future__ import annotations

import json
import sys
from contextlib import asynccontextmanager
from typing import Any
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

if "db.connection" not in sys.modules:
    sys.modules["db.connection"] = MagicMock()
if "db.models" not in sys.modules:
    sys.modules["db.models"] = MagicMock()

_auth_mock = MagicMock()
_auth_mock.verify_api_key = MagicMock(return_value=None)
sys.modules["backend.auth"] = _auth_mock

import backend.endpoints.settings as settings_mod  # noqa: E402
from config.loader import load_subagents  # noqa: E402
from db.constants import (  # noqa: E402
    DISABLED_SUBAGENTS_KEY_PREFIX,
    REPO_SUBAGENTS_CACHE_KEY_PREFIX,
)

_REPO_AGENT = {"name": "ml-trainer", "type": "build", "description": "trains models"}


def _session_ctx(values_by_key: dict[str, Any]) -> Any:
    """Async context manager whose session.get returns by key (None if absent)."""
    session_mock = AsyncMock()

    async def _get(_model: Any, key: str) -> Any:
        return values_by_key.get(key)

    session_mock.get = AsyncMock(side_effect=_get)

    @asynccontextmanager
    async def ctx():  # type: ignore[return]
        yield session_mock

    return ctx


def _setting(value: str) -> MagicMock:
    s = MagicMock()
    s.value = value
    return s


class TestGetRepoSubagentsMerge:
    """get_repo_subagents returns shipped + cached repo agents with source tags."""

    @pytest.mark.asyncio
    async def test_no_cache_returns_shipped_only(self) -> None:
        ctx = _session_ctx({})  # no cache row, no disabled row
        with patch.object(settings_mod, "session", ctx):
            result = await settings_mod.get_repo_subagents("org/repo")
        names = {a["name"] for a in result["agents"]}
        assert names == {s.name for s in load_subagents()}
        assert all(a["source"] == "core" for a in result["agents"])
        assert result["disabled"] == []

    @pytest.mark.asyncio
    async def test_cached_repo_agent_appears_with_source(self) -> None:
        cache_key = f"{REPO_SUBAGENTS_CACHE_KEY_PREFIX}org/repo"
        ctx = _session_ctx({cache_key: _setting(json.dumps([_REPO_AGENT]))})
        with patch.object(settings_mod, "session", ctx):
            result = await settings_mod.get_repo_subagents("org/repo")
        by_name = {a["name"]: a for a in result["agents"]}
        assert by_name["ml-trainer"]["source"] == "user"
        assert by_name["architect"]["source"] == "core"
        # User agent is additive on top of the full core set.
        assert len(result["agents"]) == len(load_subagents()) + 1

    @pytest.mark.asyncio
    async def test_repo_overrides_shipped_name(self) -> None:
        override = {"name": "code-reviewer", "type": "review", "description": "repo's reviewer"}
        cache_key = f"{REPO_SUBAGENTS_CACHE_KEY_PREFIX}org/repo"
        ctx = _session_ctx({cache_key: _setting(json.dumps([override]))})
        with patch.object(settings_mod, "session", ctx):
            result = await settings_mod.get_repo_subagents("org/repo")
        by_name = {a["name"]: a for a in result["agents"]}
        # Same name → user wins, count unchanged.
        assert by_name["code-reviewer"]["source"] == "user"
        assert by_name["code-reviewer"]["description"] == "repo's reviewer"
        assert len(result["agents"]) == len(load_subagents())

    @pytest.mark.asyncio
    async def test_disabled_list_returned(self) -> None:
        disabled_key = f"{DISABLED_SUBAGENTS_KEY_PREFIX}org/repo"
        ctx = _session_ctx({disabled_key: _setting(json.dumps(["ui-reviewer"]))})
        with patch.object(settings_mod, "session", ctx):
            result = await settings_mod.get_repo_subagents("org/repo")
        assert result["disabled"] == ["ui-reviewer"]

    @pytest.mark.asyncio
    async def test_disabled_ghost_name_is_pruned(self) -> None:
        # A user agent that was disabled, then removed from .autofyn/subagents.json
        # (no cache row, so it's not in the merged set), must not linger in the
        # returned disabled list — otherwise the "N of M enabled" count is wrong.
        disabled_key = f"{DISABLED_SUBAGENTS_KEY_PREFIX}org/repo"
        ctx = _session_ctx(
            {disabled_key: _setting(json.dumps(["ui-reviewer", "ml-trainer"]))}
        )
        with patch.object(settings_mod, "session", ctx):
            result = await settings_mod.get_repo_subagents("org/repo")
        # ui-reviewer is a real shipped agent (kept); ml-trainer is gone (pruned).
        assert result["disabled"] == ["ui-reviewer"]
