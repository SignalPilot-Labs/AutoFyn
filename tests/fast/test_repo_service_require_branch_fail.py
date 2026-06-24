"""Regression test: _require_on_working_branch must fail() on a bad git result.

Without the fail() check, a stale-handle git failure returned an empty
branch name, which then mismatched the working branch and raised a
misleading "HEAD is on ''" conflict — masking the real cause (the remote
sandbox's filesystem vanished). fail() must surface the stale handle as a
clear 503 instead.
"""

import pytest
from unittest.mock import AsyncMock, patch

from aiohttp import web

from models import CmdResult, RepoState


class TestRequireOnWorkingBranchFail:
    """A failed git branch lookup surfaces as itself, not a wrong-branch error."""

    @pytest.mark.asyncio
    @patch("repo.service.REPO_WORK_DIR", "/fake/repo")
    @patch("repo.service.git", new_callable=AsyncMock)
    async def test_stale_handle_raises_503_not_conflict(
        self, mock_git: AsyncMock,
    ) -> None:
        from repo.service import RepoService

        svc = RepoService()
        svc._state = RepoState(
            repo="owner/name",
            base_branch="main",
            working_branch="af/work",
            base_sha="abc123",
        )
        mock_git.return_value = CmdResult(
            stdout="",
            stderr="[Errno 116] Stale file handle: '/home/agentuser/repo'",
            exit_code=-1,
        )

        with pytest.raises(web.HTTPServiceUnavailable):
            await svc._require_on_working_branch()
