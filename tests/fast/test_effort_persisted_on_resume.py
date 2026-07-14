"""Regression test: the effort a run resolves to must reach the runs table.

create_run_starting is the only writer of runs.effort and is reached only from
POST /start. Resume builds a StartRequest and calls execute_run directly, so a
row predating the column stayed NULL forever: every resume re-hit the
legacy-NULL branch and silently restarted at DEFAULT_EFFORT.

_resolve_branch_and_clone already persists branch and status and runs on both
paths, so the effort write belongs beside them.
"""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from lifecycle.bootstrap import _resolve_branch_and_clone

_CLONE_ARGS = {
    "run_id": "r1",
    "custom_prompt": "do the thing",
    "github_repo": "org/repo",
    "base_branch": "main",
}


def _make_sandbox() -> MagicMock:
    """Build a sandbox mock that satisfies the clone path."""
    sandbox = MagicMock()
    sandbox.repo.bootstrap = AsyncMock()
    sandbox.file_system.read = AsyncMock(return_value="[]")
    return sandbox


class TestEffortPersistedOnResume:
    """Bootstrap must write the resolved effort on both start and resume."""

    @pytest.mark.asyncio
    async def test_effort_written_on_resume(self) -> None:
        """A resumed run backfills its row rather than leaving it NULL."""
        update = AsyncMock()
        with (
            patch("lifecycle.bootstrap.db.get_run_branch_name", new=AsyncMock(return_value="autofyn/x")),
            patch("lifecycle.bootstrap.db.update_run_status", new=AsyncMock()),
            patch("lifecycle.bootstrap.db.update_run_effort", new=update),
            patch("lifecycle.bootstrap.log_audit", new=AsyncMock()),
            patch("lifecycle.bootstrap.load_run_agent_config", new=AsyncMock()),
            patch("lifecycle.bootstrap.load_repo_subagents", new=AsyncMock()),
            patch("lifecycle.bootstrap._cache_repo_subagents_for_dashboard", new=AsyncMock()),
        ):
            _, is_resume, _, _ = await _resolve_branch_and_clone(
                _make_sandbox(), effort="low", **_CLONE_ARGS
            )

        assert is_resume is True
        update.assert_awaited_once_with("r1", "low")

    @pytest.mark.asyncio
    async def test_effort_written_on_fresh_run(self) -> None:
        """A fresh run records effort alongside its new branch."""
        update = AsyncMock()
        with (
            patch("lifecycle.bootstrap.db.get_run_branch_name", new=AsyncMock(return_value=None)),
            patch("lifecycle.bootstrap.db.update_run_branch", new=AsyncMock()),
            patch("lifecycle.bootstrap.db.update_run_effort", new=update),
            patch("lifecycle.bootstrap.log_audit", new=AsyncMock()),
            patch("lifecycle.bootstrap.load_run_agent_config", new=AsyncMock()),
            patch("lifecycle.bootstrap.load_repo_subagents", new=AsyncMock()),
            patch("lifecycle.bootstrap._cache_repo_subagents_for_dashboard", new=AsyncMock()),
        ):
            _, is_resume, _, _ = await _resolve_branch_and_clone(
                _make_sandbox(), effort="max", **_CLONE_ARGS
            )

        assert is_resume is False
        update.assert_awaited_once_with("r1", "max")
