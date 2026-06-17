"""Verify the session-gate server name does not drift between layers.

`SESSION_GATE_SERVER_NAME` is defined in `sandbox/constants.py` (where the
gate MCP server is built) and mirrored in `config/constants.py` (the lowest
layer, which cannot import from sandbox). The repo-subagent validator uses the
config copy to reject a subagent that requests a session-gate tool — if the
sandbox renames the server and the config copy is not updated, that denylist
silently stops matching and a subagent could be granted `end_round`/
`end_session`. This test pins the two literals together, following the same
source-read pattern as `test_audit_event_sync.py` (importing sandbox.constants
requires sandbox env vars, so we read the source instead).
"""

import re
from pathlib import Path

from config.constants import SESSION_GATE_SERVER_NAME

_REPO_ROOT = Path(__file__).resolve().parents[2]
_SANDBOX_CONSTANTS = _REPO_ROOT / "sandbox" / "constants.py"
_SANDBOX_NAME_PATTERN = re.compile(
    r'^SESSION_GATE_SERVER_NAME:\s*str\s*=\s*"([^"]+)"', re.MULTILINE
)


class TestSessionGateNameSync:
    """The config mirror of SESSION_GATE_SERVER_NAME must match sandbox."""

    def test_config_matches_sandbox(self) -> None:
        source = _SANDBOX_CONSTANTS.read_text()
        match = _SANDBOX_NAME_PATTERN.search(source)
        assert match is not None, (
            "SESSION_GATE_SERVER_NAME not found in sandbox/constants.py — "
            "the sync test can no longer verify the mirror"
        )
        assert match.group(1) == SESSION_GATE_SERVER_NAME, (
            f"sandbox SESSION_GATE_SERVER_NAME={match.group(1)!r} != "
            f"config {SESSION_GATE_SERVER_NAME!r} — the session-gate denylist "
            f"in run_subagents would silently stop matching"
        )
