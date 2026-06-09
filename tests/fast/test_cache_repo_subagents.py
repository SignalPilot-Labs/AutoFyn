"""Regression test: cache_repo_subagents persists a repo's subagents.

The agent writes the repo's user-defined subagents (name/type/description) to
a Setting row at bootstrap so the dashboard can show them without a GitHub
fetch. New repo → insert; existing cache → overwrite; empty → clears (stores []).
"""

import json
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from db.constants import REPO_SUBAGENTS_CACHE_KEY_PREFIX
from utils.db import cache_repo_subagents

_AGENTS = [{"name": "ml-trainer", "type": "build", "description": "trains models"}]


def _factory_with_session(session: MagicMock) -> MagicMock:
    ctx = AsyncMock()
    ctx.__aenter__ = AsyncMock(return_value=session)
    ctx.__aexit__ = AsyncMock(return_value=False)
    return MagicMock(return_value=ctx)


class TestCacheRepoSubagents:
    """cache_repo_subagents upserts the repo-subagents cache Setting."""

    @pytest.mark.asyncio
    async def test_inserts_when_absent(self) -> None:
        session = AsyncMock()
        session.get = AsyncMock(return_value=None)
        session.add = MagicMock()
        session.commit = AsyncMock()
        factory = _factory_with_session(session)

        with patch("utils.db.get_session_factory", return_value=factory):
            await cache_repo_subagents("org/repo", _AGENTS)

        session.add.assert_called_once()
        added = session.add.call_args[0][0]
        assert added.key == f"{REPO_SUBAGENTS_CACHE_KEY_PREFIX}org/repo"
        assert json.loads(added.value) == _AGENTS
        assert added.encrypted is False
        session.commit.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_overwrites_when_present(self) -> None:
        existing = MagicMock()
        existing.value = json.dumps([{"name": "stale"}])
        session = AsyncMock()
        session.get = AsyncMock(return_value=existing)
        session.add = MagicMock()
        session.commit = AsyncMock()
        factory = _factory_with_session(session)

        with patch("utils.db.get_session_factory", return_value=factory):
            await cache_repo_subagents("org/repo", _AGENTS)

        # Existing row mutated in place, not re-added.
        session.add.assert_not_called()
        assert json.loads(existing.value) == _AGENTS
        session.commit.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_empty_list_clears_to_empty_array(self) -> None:
        session = AsyncMock()
        session.get = AsyncMock(return_value=None)
        session.add = MagicMock()
        session.commit = AsyncMock()
        factory = _factory_with_session(session)

        with patch("utils.db.get_session_factory", return_value=factory):
            await cache_repo_subagents("org/repo", [])

        added = session.add.call_args[0][0]
        assert added.value == "[]"
