"""Tests for the diff blob → file-list parsing (GitHub completed-run path).

parse_diff_blob_to_files turns a full unified diff blob into the same
{path, status, added, removed} shape the live sandbox temp-index path
returns, so completed and live runs share one frontend contract.
_files_from_blob then attaches bodies (null in list mode, one filled on
expand) and 404s on an unknown expand path.
"""

import pytest

from fastapi import HTTPException

from endpoints.diff import _files_from_blob
from utils.diff import parse_diff_blob_to_files

_BLOB = "\n".join([
    "diff --git a/src/main.py b/src/main.py",
    "index 1111111..2222222 100644",
    "--- a/src/main.py",
    "+++ b/src/main.py",
    "@@ -1,2 +1,3 @@",
    " import os",
    "+import sys",
    "diff --git a/new.txt b/new.txt",
    "new file mode 100644",
    "--- /dev/null",
    "+++ b/new.txt",
    "@@ -0,0 +1,1 @@",
    "+brand new",
    "diff --git a/gone.txt b/gone.txt",
    "deleted file mode 100644",
    "--- a/gone.txt",
    "+++ /dev/null",
    "@@ -1 +0,0 @@",
    "-was here",
])


class TestParseDiffBlobToFiles:
    """Blob → [{path, status, added, removed}]."""

    def test_parses_all_files_with_status(self) -> None:
        files = parse_diff_blob_to_files(_BLOB)
        by_path = {f["path"]: f for f in files}
        assert set(by_path) == {"src/main.py", "new.txt", "gone.txt"}
        assert by_path["src/main.py"]["status"] == "modified"
        assert by_path["new.txt"]["status"] == "added"
        assert by_path["gone.txt"]["status"] == "deleted"

    def test_counts_added_and_removed_ignoring_headers(self) -> None:
        files = parse_diff_blob_to_files(_BLOB)
        by_path = {f["path"]: f for f in files}
        # +import sys → 1 add; the +++ header line is not counted.
        assert by_path["src/main.py"]["added"] == 1
        assert by_path["src/main.py"]["removed"] == 0
        assert by_path["new.txt"]["added"] == 1
        assert by_path["gone.txt"]["removed"] == 1

    def test_empty_blob_returns_empty_list(self) -> None:
        assert parse_diff_blob_to_files("") == []


class TestFilesFromBlob:
    """Blob → {files:[...]} with null bodies, one filled on expand."""

    def test_list_mode_all_bodies_null(self) -> None:
        out = _files_from_blob(_BLOB, None)
        assert len(out["files"]) == 3
        assert all(f["body"] is None for f in out["files"])

    def test_expand_fills_only_matching_body(self) -> None:
        out = _files_from_blob(_BLOB, "src/main.py")
        by_path = {f["path"]: f for f in out["files"]}
        assert "+import sys" in by_path["src/main.py"]["body"]
        assert by_path["new.txt"]["body"] is None

    def test_expand_unknown_path_raises_404(self) -> None:
        with pytest.raises(HTTPException) as exc:
            _files_from_blob(_BLOB, "nope.py")
        assert exc.value.status_code == 404
