"""Regression tests for project MCP server loading in config/loader.py.

A repo declares external (stdio) MCP servers in `.autofyn/mcp.json`; before this
existed, the servers were referenced in subagents.json allowlists but never
launched, so agents fell back to shelling out to the server module directly.

Covers:
- Absent mcp.json returns empty (no crash)
- Well-formed mcp.json returns the mcpServers map
- Malformed JSON fails loud (does not silently drop the servers)
- Non-object mcpServers fails loud
- merge_mcp_servers: modal supersedes project by name, project-only survives
"""

from __future__ import annotations

import json

from pathlib import Path

import pytest

import config.loader as loader_module
from config.loader import load_project_mcp_servers, merge_mcp_servers


class TestProjectMcpServers:
    """load_project_mcp_servers() reads .autofyn/mcp.json; merge respects precedence."""

    def _point_at(self, monkeypatch: pytest.MonkeyPatch, path: Path) -> None:
        monkeypatch.setattr(loader_module, "_PROJECT_MCP", path)

    def test_absent_file_returns_empty(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        self._point_at(monkeypatch, tmp_path / "nonexistent.json")
        assert load_project_mcp_servers() == {}

    def test_wellformed_returns_servers_map(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        f = tmp_path / "mcp.json"
        f.write_text(json.dumps({
            "mcpServers": {
                "approach-ranker": {"command": "python3", "args": [".autofyn/approach_ranker.py"]}
            }
        }))
        self._point_at(monkeypatch, f)
        servers = load_project_mcp_servers()
        assert servers == {
            "approach-ranker": {"command": "python3", "args": [".autofyn/approach_ranker.py"]}
        }

    def test_missing_key_returns_empty(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        f = tmp_path / "mcp.json"
        f.write_text(json.dumps({"other": {}}))
        self._point_at(monkeypatch, f)
        assert load_project_mcp_servers() == {}

    def test_malformed_json_raises(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        f = tmp_path / "mcp.json"
        f.write_text("{ not valid json ")
        self._point_at(monkeypatch, f)
        with pytest.raises(RuntimeError, match="Malformed"):
            load_project_mcp_servers()

    def test_non_object_servers_raises(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        f = tmp_path / "mcp.json"
        f.write_text(json.dumps({"mcpServers": ["approach-ranker"]}))
        self._point_at(monkeypatch, f)
        with pytest.raises(RuntimeError, match="must be an object"):
            load_project_mcp_servers()

    def test_modal_supersedes_project_by_name(self) -> None:
        project = {"approach-ranker": {"command": "python3", "args": ["old.py"]}}
        modal = {"approach-ranker": {"command": "python3", "args": ["new.py"]}}
        merged = merge_mcp_servers(project, modal)
        assert merged == {"approach-ranker": {"command": "python3", "args": ["new.py"]}}

    def test_project_only_survives_merge(self) -> None:
        project = {"approach-ranker": {"command": "python3", "args": ["r.py"]}}
        merged = merge_mcp_servers(project, {"other": {"command": "node"}})
        assert merged["approach-ranker"] == {"command": "python3", "args": ["r.py"]}
        assert merged["other"] == {"command": "node"}

    def test_none_modal_returns_project(self) -> None:
        project = {"approach-ranker": {"command": "python3"}}
        assert merge_mcp_servers(project, None) == project
