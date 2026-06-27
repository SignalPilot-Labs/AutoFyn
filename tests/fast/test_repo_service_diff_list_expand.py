"""Tests for RepoService live diff: list + per-file expand via temp index.

diff_list stages the working tree into a THROWAWAY index (so untracked
files appear) and diffs --cached against base. diff_response shapes the
list with null bodies and fills exactly one body on expand, 404ing on an
unknown path. git/index commands are mocked — the temp-index git behavior
itself is verified separately; here we assert command shape and response
contract.
"""

import pytest
from unittest.mock import AsyncMock, patch

from aiohttp import web

from models import CmdResult, RepoState


def _ok(stdout: str = "") -> CmdResult:
    """Successful command result."""
    return CmdResult(stdout=stdout, stderr="", exit_code=0)


def _make_service():
    """RepoService with bootstrapped state pointing at a fake base sha."""
    from repo.service import RepoService

    svc = RepoService()
    svc._state = RepoState(
        repo="owner/repo",
        base_branch="main",
        working_branch="autofyn/x",
        base_sha="BASESHA",
    )
    return svc


_NUMSTAT = "1\t0\tnew.txt\n3\t1\ttracked.py\n"
_NAME_STATUS = "A\tnew.txt\nM\ttracked.py\n"


class TestDiffListExpand:
    """diff_list stages to temp index; diff_response shapes list + expand."""

    @pytest.mark.asyncio
    @patch("repo.service.REPO_WORK_DIR", "/fake/repo")
    @patch("repo.service.run_cmd", new_callable=AsyncMock)
    @patch("repo.service.git_indexed", new_callable=AsyncMock)
    async def test_diff_list_includes_untracked_and_tracked(
        self, mock_gi: AsyncMock, mock_run: AsyncMock,
    ) -> None:
        svc = _make_service()
        mock_run.return_value = _ok()  # cp real index → temp index
        mock_gi.side_effect = [_ok(), _ok(_NUMSTAT), _ok(_NAME_STATUS)]

        files = await svc.diff_list()

        by_path = {f["path"]: f for f in files}
        assert by_path["new.txt"]["status"] == "added"
        assert by_path["new.txt"]["added"] == 1
        assert by_path["tracked.py"]["status"] == "modified"
        # First git_indexed call stages the whole tree into the temp index.
        assert mock_gi.call_args_list[0].args[0] == ["add", "-A"]
        # The numstat diff is --cached against base (so untracked show up).
        numstat_args = mock_gi.call_args_list[1].args[0]
        assert numstat_args == ["diff", "--numstat", "--cached", "BASESHA"]

    @pytest.mark.asyncio
    @patch("repo.service.REPO_WORK_DIR", "/fake/repo")
    @patch("repo.service.run_cmd", new_callable=AsyncMock)
    @patch("repo.service.git_indexed", new_callable=AsyncMock)
    async def test_diff_response_list_mode_bodies_null(
        self, mock_gi: AsyncMock, mock_run: AsyncMock,
    ) -> None:
        svc = _make_service()
        mock_run.return_value = _ok()
        mock_gi.side_effect = [_ok(), _ok(_NUMSTAT), _ok(_NAME_STATUS)]

        out = await svc.diff_response(None)

        assert {f["path"] for f in out["files"]} == {"new.txt", "tracked.py"}
        assert all(f["body"] is None for f in out["files"])

    @pytest.mark.asyncio
    @patch("repo.service.REPO_WORK_DIR", "/fake/repo")
    @patch("repo.service.run_cmd", new_callable=AsyncMock)
    @patch("repo.service.git_indexed", new_callable=AsyncMock)
    async def test_diff_response_expand_fills_one_body(
        self, mock_gi: AsyncMock, mock_run: AsyncMock,
    ) -> None:
        svc = _make_service()
        mock_run.return_value = _ok()
        # list: stage, numstat, name-status; expand: stage, file-body diff.
        mock_gi.side_effect = [
            _ok(), _ok(_NUMSTAT), _ok(_NAME_STATUS),
            _ok(), _ok("diff --git a/new.txt b/new.txt\n+brand new\n"),
        ]

        out = await svc.diff_response("new.txt")

        by_path = {f["path"]: f for f in out["files"]}
        assert "+brand new" in by_path["new.txt"]["body"]
        assert by_path["tracked.py"]["body"] is None

    @pytest.mark.asyncio
    @patch("repo.service.REPO_WORK_DIR", "/fake/repo")
    @patch("repo.service.run_cmd", new_callable=AsyncMock)
    @patch("repo.service.git_indexed", new_callable=AsyncMock)
    async def test_diff_response_expand_unknown_path_raises_404(
        self, mock_gi: AsyncMock, mock_run: AsyncMock,
    ) -> None:
        svc = _make_service()
        mock_run.return_value = _ok()
        mock_gi.side_effect = [_ok(), _ok(_NUMSTAT), _ok(_NAME_STATUS)]

        with pytest.raises(web.HTTPNotFound):
            await svc.diff_response("does/not/exist.py")

    @pytest.mark.asyncio
    @patch("repo.service.REPO_WORK_DIR", "/fake/repo")
    @patch("repo.service.run_cmd", new_callable=AsyncMock)
    @patch("repo.service.git_indexed", new_callable=AsyncMock)
    async def test_tmp_index_is_unique_per_call_and_cleaned_up(
        self, mock_gi: AsyncMock, mock_run: AsyncMock,
    ) -> None:
        """Each diff uses a fresh index path (concurrency-safe) and rm's it.

        A shared index would let a concurrent poll+click corrupt each other's
        `git add -A`. The path must therefore be unique per call, and removed
        on exit so /tmp does not accumulate index files.
        """
        svc = _make_service()
        mock_run.return_value = _ok()
        mock_gi.return_value = _ok(_NUMSTAT)

        # The index path is the cp destination (run_cmd arg) and the rm target.
        await svc.diff_list()
        paths_run1 = [c.args[0] for c in mock_run.call_args_list]
        cp1 = next(a for a in paths_run1 if a[0] == "cp")[-1]
        rm1 = next(a for a in paths_run1 if a[0] == "rm")[-1]
        assert cp1 == rm1  # same call → copied into then removed
        assert cp1.startswith("/tmp/diff-index-")

        mock_run.reset_mock()
        await svc.diff_list()
        paths_run2 = [c.args[0] for c in mock_run.call_args_list]
        cp2 = next(a for a in paths_run2 if a[0] == "cp")[-1]
        assert cp1 != cp2  # a second call gets a DIFFERENT index path

    @pytest.mark.asyncio
    @patch("repo.service.REPO_WORK_DIR", "/fake/repo")
    @patch("repo.service.run_cmd", new_callable=AsyncMock)
    @patch("repo.service.git_indexed", new_callable=AsyncMock)
    async def test_expand_binary_file_returns_null_body(
        self, mock_gi: AsyncMock, mock_run: AsyncMock,
    ) -> None:
        """A binary file's body is null (matches the GitHub path contract)."""
        svc = _make_service()
        mock_run.return_value = _ok()
        binary_body = (
            "diff --git a/img.png b/img.png\n"
            "new file mode 100644\n"
            "index 0000000..2c4e118\n"
            "Binary files /dev/null and b/img.png differ\n"
        )
        # list: stage, numstat, name-status; expand: stage, file-body diff.
        mock_gi.side_effect = [
            _ok(), _ok("-\t-\timg.png\n"), _ok("A\timg.png\n"),
            _ok(), _ok(binary_body),
        ]

        out = await svc.diff_response("img.png")

        assert out["files"][0]["body"] is None

    @pytest.mark.asyncio
    @patch("repo.service.REPO_WORK_DIR", "/fake/repo")
    @patch("repo.service.run_cmd", new_callable=AsyncMock)
    @patch("repo.service.git_indexed", new_callable=AsyncMock)
    async def test_index_copy_failure_raises_not_silent(
        self, mock_gi: AsyncMock, mock_run: AsyncMock,
    ) -> None:
        """A failed `cp` of the real index must raise, not diff a stale index."""
        # cp fails; rm cleanup still returns ok.
        mock_run.side_effect = [
            CmdResult(stdout="", stderr="cp: no such file", exit_code=1),
            _ok(),
        ]
        svc = _make_service()

        with pytest.raises(web.HTTPInternalServerError):
            await svc.diff_list()
