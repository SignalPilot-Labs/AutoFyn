"""Regression test: PR body must be passed via --body-file, not --body.

Bug: _create_or_update_pr passed the PR description as `--body <description>`.
A large body (the run-state grows unbounded across rounds) exceeds the kernel's
128KB per-argv limit, so `gh pr create` failed at exec time with
``[Errno 7] Argument list too long`` and no PR was created.

Fix: write the body to PR_BODY_FILE and pass `--body-file <path>` on both the
create and edit paths, so body size never lands on the command line.
"""

import pytest
from unittest.mock import AsyncMock, mock_open, patch

from models import CmdResult, RepoState


def _ok(stdout: str = "") -> CmdResult:
    return CmdResult(stdout=stdout, stderr="", exit_code=0)


def _state() -> RepoState:
    return RepoState(
        repo="owner/repo",
        base_branch="main",
        working_branch="autofyn/work",
        base_sha="deadbeef",
    )


class TestRepoServicePRBodyFile:
    """_create_or_update_pr passes --body-file and never --body."""

    @pytest.mark.asyncio
    @patch("repo.service.PR_BODY_FILE", "/tmp/test-pr-body.md")
    @patch("repo.service.REPO_WORK_DIR", "/fake/repo")
    @patch("builtins.open", new_callable=mock_open)
    @patch("repo.service.gh", new_callable=AsyncMock)
    async def test_create_uses_body_file(
        self, mock_gh: AsyncMock, mock_file: AsyncMock,
    ) -> None:
        """Creating a new PR passes --body-file, not --body."""
        from repo.service import RepoService

        svc = RepoService()
        svc._state = _state()
        # gh pr view -> no existing PR (exit 1); gh pr create -> success
        mock_gh.side_effect = [
            CmdResult(stdout="", stderr="", exit_code=1),
            _ok("https://github.com/owner/repo/pull/1"),
        ]

        url, err = await svc._create_or_update_pr("title", "x" * 200000, "main")

        assert err is None
        assert url == "https://github.com/owner/repo/pull/1"
        create_args = mock_gh.call_args_list[1].args[0]
        assert "--body-file" in create_args
        assert "--body" not in create_args
        assert "/tmp/test-pr-body.md" in create_args
        mock_file().write.assert_called_once_with("x" * 200000)

    @pytest.mark.asyncio
    @patch("repo.service.PR_BODY_FILE", "/tmp/test-pr-body.md")
    @patch("repo.service.REPO_WORK_DIR", "/fake/repo")
    @patch("builtins.open", new_callable=mock_open)
    @patch("repo.service.gh", new_callable=AsyncMock)
    async def test_edit_uses_body_file(
        self, mock_gh: AsyncMock, mock_file: AsyncMock,
    ) -> None:
        """Editing an existing PR passes --body-file, not --body."""
        from repo.service import RepoService

        svc = RepoService()
        svc._state = _state()
        # gh pr view -> existing PR url; gh pr edit -> success
        mock_gh.side_effect = [
            _ok("https://github.com/owner/repo/pull/9"),
            _ok(),
        ]

        url, err = await svc._create_or_update_pr("title", "y" * 200000, "main")

        assert err is None
        assert url == "https://github.com/owner/repo/pull/9"
        edit_args = mock_gh.call_args_list[1].args[0]
        assert "pr" in edit_args and "edit" in edit_args
        assert "--body-file" in edit_args
        assert "--body" not in edit_args
