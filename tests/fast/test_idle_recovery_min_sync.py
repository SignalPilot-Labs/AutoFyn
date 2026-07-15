"""Verify the dashboard's auto-recovery label matches the real kill timeout.

The IdleWarningBanner tells the user when auto-recovery fires. That number is
hardcoded in the frontend because config.yml is never served to it, so a bump
to subagent_idle_kill_sec silently leaves the banner lying — it read "10m"
for a 900s timeout.

config.yml is the source of truth; IDLE_RECOVERY_MIN must mirror it.
"""

import re
from pathlib import Path

import yaml

_REPO_ROOT = Path(__file__).resolve().parents[2]
_CONFIG_PATH = _REPO_ROOT / "config" / "config.yml"
_HELPERS_PATH = (
    _REPO_ROOT / "dashboard" / "frontend" / "components" / "feed" / "eventCardHelpers.ts"
)
_SECONDS_PER_MINUTE = 60
_IDLE_RECOVERY_RE = re.compile(r"IDLE_RECOVERY_MIN\s*=\s*(\d+)")


class TestIdleRecoveryMinSync:
    """IDLE_RECOVERY_MIN must equal subagent_idle_kill_sec in minutes."""

    def _config_kill_minutes(self) -> float:
        """Return subagent_idle_kill_sec from config.yml, in minutes."""
        config = yaml.safe_load(_CONFIG_PATH.read_text())
        return config["agent"]["subagent_idle_kill_sec"] / _SECONDS_PER_MINUTE

    def _frontend_recovery_minutes(self) -> int:
        """Return IDLE_RECOVERY_MIN as declared in eventCardHelpers.ts."""
        match = _IDLE_RECOVERY_RE.search(_HELPERS_PATH.read_text())
        assert match is not None, "IDLE_RECOVERY_MIN not found in eventCardHelpers.ts"
        return int(match.group(1))

    def test_banner_matches_kill_timeout(self) -> None:
        """A bump to subagent_idle_kill_sec must be mirrored in the banner."""
        assert self._frontend_recovery_minutes() == self._config_kill_minutes()
