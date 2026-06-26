"""Tests for the diff stats endpoint and its _stats_response helper."""

import sys
from unittest.mock import AsyncMock, MagicMock

import pytest
from fastapi import HTTPException

from db.constants import RUN_STATUS_COMPLETED, RUN_STATUS_RUNNING


SAMPLE_DIFF_STATS = [
    {"path": "src/main.py", "added": 10, "removed": 2, "status": "modified"},
    {"path": "src/new.py", "added": 25, "removed": 0, "status": "added"},
]


def _import_runs_module():
    """Import backend.endpoints.runs with auth + db stubbed out.

    Saves and restores original sys.modules entries to avoid poisoning
    other tests that depend on real db.models, db.connection, etc.
    """
    stubs = ("backend.auth", "backend.db", "db.connection", "db.models")
    originals = {mod: sys.modules.get(mod) for mod in stubs}

    auth_mock = MagicMock()
    auth_mock._api_key = "test"
    auth_mock.require_api_key = MagicMock()
    auth_mock.require_api_key_qs = MagicMock()
    sys.modules["backend.auth"] = auth_mock

    sys.modules["backend.db"] = MagicMock()
    sys.modules["db.connection"] = MagicMock()
    sys.modules["db.models"] = MagicMock()

    import backend.endpoints.runs as runs_mod

    # Restore originals so other tests see real modules
    for mod, original in originals.items():
        if original is not None:
            sys.modules[mod] = original
        else:
            sys.modules.pop(mod, None)

    return runs_mod


runs = _import_runs_module()
_stats_response = runs._stats_response


class TestStatsResponse:
    """_stats_response packs a list of files + source into the API shape."""

    def test_source_is_passed_through(self) -> None:
        assert _stats_response([], "stored")["source"] == "stored"
        assert _stats_response([], "live")["source"] == "live"
        assert _stats_response([], "unavailable")["source"] == "unavailable"

    def test_counts_files(self) -> None:
        result = _stats_response(SAMPLE_DIFF_STATS, "stored")
        assert result["total_files"] == 2

    def test_sums_added_removed(self) -> None:
        result = _stats_response(SAMPLE_DIFF_STATS, "stored")
        assert result["total_added"] == 35
        assert result["total_removed"] == 2

    def test_empty_list(self) -> None:
        result = _stats_response([], "unavailable")
        assert result["total_files"] == 0
        assert result["total_added"] == 0
        assert result["total_removed"] == 0

    def test_passes_files_through(self) -> None:
        result = _stats_response(SAMPLE_DIFF_STATS, "stored")
        assert result["files"] is SAMPLE_DIFF_STATS


@pytest.fixture
def run_record() -> MagicMock:
    """Minimal Run model stand-in — only the fields get_run_diff reads."""
    r = MagicMock()
    r.diff_stats = None
    r.status = RUN_STATUS_RUNNING
    return r


@pytest.fixture
def db_session(monkeypatch: pytest.MonkeyPatch, run_record: MagicMock):
    """Patch backend.utils.session so `await s.get(Run, ...)` returns run_record."""
    s = MagicMock()
    s.get = AsyncMock(return_value=run_record)

    class _CtxMgr:
        async def __aenter__(self): return s
        async def __aexit__(self, *a): return None

    monkeypatch.setattr(runs, "session", lambda: _CtxMgr())
    return s


class TestGetRunDiffLivePath:
    """get_run_diff returns a source marker only — the file list and line
    counts are parsed from the /diff/repo blob by the frontend, never fetched
    as a second, drift-prone stat set. So this endpoint must NEVER call the
    agent for live runs; it reads the run status from the DB and nothing more.
    """

    @pytest.mark.asyncio
    async def test_stored_stats_short_circuit(
        self, monkeypatch: pytest.MonkeyPatch, db_session, run_record: MagicMock,
    ) -> None:
        # If DB has stored stats, those authoritative counts win.
        run_record.diff_stats = SAMPLE_DIFF_STATS
        agent = AsyncMock()
        monkeypatch.setattr(runs, "agent_request", agent)
        result = await runs.get_run_diff("run-1")
        agent.assert_not_called()
        assert result["source"] == "stored"
        assert result["total_files"] == 2

    @pytest.mark.asyncio
    async def test_active_run_returns_source_live_no_files(
        self, monkeypatch: pytest.MonkeyPatch, db_session, run_record: MagicMock,
    ) -> None:
        # Active run, no stored stats: source is "live" with an empty file
        # list. Membership comes from the diff blob, not this endpoint.
        run_record.diff_stats = None
        run_record.status = RUN_STATUS_RUNNING
        agent = AsyncMock()
        monkeypatch.setattr(runs, "agent_request", agent)
        result = await runs.get_run_diff("run-1")
        agent.assert_not_called()
        assert result["source"] == "live"
        assert result["files"] == []
        assert result["total_files"] == 0

    @pytest.mark.asyncio
    async def test_terminal_run_without_stats_is_unavailable(
        self, monkeypatch: pytest.MonkeyPatch, db_session, run_record: MagicMock,
    ) -> None:
        # Terminal run with no stored stats: sandbox is gone, so "unavailable".
        run_record.diff_stats = None
        run_record.status = RUN_STATUS_COMPLETED
        agent = AsyncMock()
        monkeypatch.setattr(runs, "agent_request", agent)
        result = await runs.get_run_diff("run-1")
        agent.assert_not_called()
        assert result["source"] == "unavailable"
        assert result["total_files"] == 0


class TestGetDiffRepoBranchGating:
    """get_diff_repo must refuse pre-bootstrap runs and route active/terminal
    runs to sandbox/github source respectively.
    """

    @pytest.mark.asyncio
    async def test_null_branch_returns_409_and_skips_agent(
        self, monkeypatch: pytest.MonkeyPatch, db_session, run_record: MagicMock,
    ) -> None:
        run_record.branch_name = None
        run_record.base_branch = "main"
        run_record.github_repo = "owner/repo"
        run_record.status = "starting"

        agent = AsyncMock()
        creds = AsyncMock()
        monkeypatch.setattr(runs, "agent_request", agent)
        monkeypatch.setattr(runs, "read_credentials", creds)

        with pytest.raises(HTTPException) as exc_info:
            await runs.get_diff_repo("run-1")

        assert exc_info.value.status_code == 409
        agent.assert_not_called()
        creds.assert_not_called()

    @pytest.mark.asyncio
    async def test_active_run_passes_source_sandbox(
        self, monkeypatch: pytest.MonkeyPatch, db_session, run_record: MagicMock,
    ) -> None:
        run_record.branch_name = "autofyn/real-branch"
        run_record.base_branch = "main"
        run_record.github_repo = "owner/repo"
        run_record.status = "running"

        agent = AsyncMock(return_value={"diff": "diff --git a/x b/x\n"})
        monkeypatch.setattr(runs, "agent_request", agent)
        monkeypatch.setattr(runs, "read_credentials", AsyncMock(return_value={"git_token": "tok"}))

        result = await runs.get_diff_repo("run-1")

        agent.assert_called_once()
        # agent_request(method, path, timeout, json_body, params, ...)
        call_params = agent.call_args[0][4]
        assert call_params["source"] == "sandbox"
        assert result["diff"].startswith("diff --git")

    @pytest.mark.asyncio
    async def test_terminal_run_passes_source_github(
        self, monkeypatch: pytest.MonkeyPatch, db_session, run_record: MagicMock,
    ) -> None:
        run_record.branch_name = "autofyn/real-branch"
        run_record.base_branch = "main"
        run_record.github_repo = "owner/repo"
        run_record.status = "completed"

        agent = AsyncMock(return_value={"diff": "diff --git a/x b/x\n"})
        monkeypatch.setattr(runs, "agent_request", agent)
        monkeypatch.setattr(runs, "read_credentials", AsyncMock(return_value={"git_token": "tok"}))

        await runs.get_diff_repo("run-1")

        call_params = agent.call_args[0][4]
        assert call_params["source"] == "github"
