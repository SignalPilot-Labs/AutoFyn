"""Regression test: read_dir must skip non-text files, not 500 the listing.

Agents download PDFs (arXiv papers) into working dirs. read_dir reads every
regular file under a dir as UTF-8 text; a single binary file used to raise an
unhandled UnicodeDecodeError and return 500, hiding every text file in the dir.
The endpoint's contract is text (round reports, memory) — a binary artifact is
skipped, the text files still come back.
"""

import json
from pathlib import Path
from unittest.mock import AsyncMock, patch

import pytest
from aiohttp import web

from api.file_system import handle_read_dir


def _request(path: str) -> web.Request:
    """A minimal aiohttp request whose json() returns {"path": path}."""
    req = AsyncMock(spec=web.Request)
    req.json.return_value = {"path": path}
    return req


class TestReadDirSkipsBinary:
    """handle_read_dir returns text files and skips non-UTF-8 ones."""

    @pytest.mark.asyncio
    async def test_binary_file_skipped_text_returned(self, tmp_path: Path) -> None:
        """A PDF beside a report: report returned, PDF skipped, no 500."""
        (tmp_path / "math-explorer.md").write_text("# report", encoding="utf-8")
        (tmp_path / "paper.pdf").write_bytes(b"%PDF-1.7\x00\xff\xfe binary \x80")

        with patch(
            "api.file_system.validate_fs_path", lambda raw: Path(raw)
        ):
            resp = await handle_read_dir(_request(str(tmp_path)))

        assert resp.status == 200
        assert isinstance(resp.body, bytes)
        data = json.loads(resp.body)
        assert data["exists"] is True
        assert data["files"]["math-explorer.md"] == "# report"
        assert "paper.pdf" not in data["files"]
