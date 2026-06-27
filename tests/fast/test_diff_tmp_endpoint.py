"""Regression tests for /diff/tmp — sandbox-first, archive-fallback behavior.

During round 1 the archive on the host volume is empty; round files live
inside the live sandbox at /tmp/round-N. Once the run completes, the files
are flushed to the archive and the sandbox is gone. The endpoint must
pick the right source based on whether a sandbox client exists.
"""

from pathlib import Path
from unittest.mock import AsyncMock, MagicMock

import pytest

from fastapi import HTTPException

from endpoints.diff import (
    _collect_tmp_from_archive,
    _collect_tmp_from_sandbox,
    _new_file_block,
    _tmp_files_response,
)


class TestTmpFilesResponse:
    """Shapes tmp entries into the unified {files:[...]} contract."""

    def test_empty_entries_returns_empty_file_list(self) -> None:
        assert _tmp_files_response([], None) == {"files": []}

    def test_list_mode_has_null_bodies_and_added_status(self) -> None:
        out = _tmp_files_response([("tmp/round-1/a.md", "line1\nline2")], None)
        assert out["files"] == [{
            "path": "tmp/round-1/a.md",
            "status": "added",
            "added": 2,
            "removed": 0,
            "body": None,
        }]

    def test_multiple_files_all_listed_bodies_null(self) -> None:
        out = _tmp_files_response([
            ("tmp/round-1/a.md", "x"),
            ("tmp/round-2/b.md", "y"),
        ], None)
        assert len(out["files"]) == 2
        assert all(f["body"] is None for f in out["files"])

    def test_expand_fills_only_the_matching_body(self) -> None:
        out = _tmp_files_response([
            ("tmp/round-1/a.md", "line1\nline2"),
            ("tmp/round-2/b.md", "other"),
        ], "tmp/round-1/a.md")
        by_path = {f["path"]: f for f in out["files"]}
        body = by_path["tmp/round-1/a.md"]["body"]
        assert "diff --git a/tmp/round-1/a.md b/tmp/round-1/a.md" in body
        assert "new file mode 100644" in body
        assert "+line1" in body
        assert by_path["tmp/round-2/b.md"]["body"] is None

    def test_expand_unknown_path_raises_404(self) -> None:
        with pytest.raises(HTTPException) as exc:
            _tmp_files_response([("tmp/round-1/a.md", "x")], "tmp/nope.md")
        assert exc.value.status_code == 404


class TestNewFileBlock:
    """Renders one file's content as a unified 'new file' diff block."""

    def test_header_and_body(self) -> None:
        out = _new_file_block("tmp/round-1/a.md", "line1\nline2")
        assert out.startswith("diff --git a/tmp/round-1/a.md b/tmp/round-1/a.md")
        assert "@@ -0,0 +1,2 @@" in out
        assert "+line1" in out
        assert "+line2" in out


class TestCollectTmpFromSandbox:
    """Reads /tmp/round-* and /tmp/memory/ from a live sandbox client."""

    @pytest.mark.asyncio
    async def test_filters_non_round_dirs(self) -> None:
        client = MagicMock()
        client.file_system.ls = AsyncMock(return_value=["round-1", "other", "cache"])
        client.file_system.read_dir = AsyncMock(side_effect=[
            {"report.md": "hi"},  # round-1
            None,  # memory dir
        ])
        entries = await _collect_tmp_from_sandbox(client)
        assert entries == [("tmp/round-1/report.md", "hi")]

    @pytest.mark.asyncio
    async def test_rejects_traversal_and_non_numeric_suffixes(self) -> None:
        client = MagicMock()
        client.file_system.ls = AsyncMock(return_value=[
            "round-..", "round-/etc", "round-abc", "round-", "round-1",
        ])
        client.file_system.read_dir = AsyncMock(side_effect=[
            {"x.md": "ok"},  # round-1
            None,  # memory dir
        ])
        entries = await _collect_tmp_from_sandbox(client)
        assert entries == [("tmp/round-1/x.md", "ok")]

    @pytest.mark.asyncio
    async def test_multiple_rounds_are_sorted(self) -> None:
        client = MagicMock()
        client.file_system.ls = AsyncMock(return_value=["round-2", "round-1"])
        client.file_system.read_dir = AsyncMock(side_effect=[
            {"a.md": "one"},   # round-1
            {"b.md": "two"},   # round-2
            None,  # memory dir
        ])
        entries = await _collect_tmp_from_sandbox(client)
        assert entries == [
            ("tmp/round-1/a.md", "one"),
            ("tmp/round-2/b.md", "two"),
        ]

    @pytest.mark.asyncio
    async def test_empty_round_dir_is_skipped(self) -> None:
        client = MagicMock()
        client.file_system.ls = AsyncMock(return_value=["round-1", "round-2"])
        client.file_system.read_dir = AsyncMock(side_effect=[
            None,  # round-1 empty
            {"x.md": "data"},  # round-2
            None,  # memory dir
        ])
        entries = await _collect_tmp_from_sandbox(client)
        assert entries == [("tmp/round-2/x.md", "data")]


class TestCollectTmpFromArchive:
    """Reads archived round files from the agent's host volume."""

    def test_missing_archive_returns_empty(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr("endpoints.diff.ROUND_ARCHIVE_AGENT_DIR", str(tmp_path))
        assert _collect_tmp_from_archive("nonexistent-run") == []

    def test_reads_all_rounds_sorted(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr("endpoints.diff.ROUND_ARCHIVE_AGENT_DIR", str(tmp_path))
        run_dir = tmp_path / "run-1"
        (run_dir / "round-2").mkdir(parents=True)
        (run_dir / "round-1").mkdir()
        (run_dir / "round-1" / "a.md").write_text("one")
        (run_dir / "round-2" / "b.md").write_text("two")
        entries = _collect_tmp_from_archive("run-1")
        assert entries == [
            ("tmp/round-1/a.md", "one"),
            ("tmp/round-2/b.md", "two"),
        ]

    def test_skips_non_file_entries(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr("endpoints.diff.ROUND_ARCHIVE_AGENT_DIR", str(tmp_path))
        run_dir = tmp_path / "run-1" / "round-1"
        run_dir.mkdir(parents=True)
        (run_dir / "keep.md").write_text("yes")
        (run_dir / "subdir").mkdir()  # nested dir — should be ignored
        entries = _collect_tmp_from_archive("run-1")
        assert entries == [("tmp/round-1/keep.md", "yes")]
