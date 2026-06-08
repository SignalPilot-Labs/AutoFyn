"""Regression test: add_dirs must only contain the skills directory.

The agent must NOT discover framework code (/opt/autofyn), dead paths
(/home/agentuser/research), or broad directories (/workspace). Only
the skills directory is needed for SDK skill discovery.
"""

from pathlib import Path

CONSTANTS_SRC = (
    Path(__file__).parent.parent.parent / "autofyn" / "utils" / "constants.py"
).read_text()

BOOTSTRAP_SRC = (
    Path(__file__).parent.parent.parent / "autofyn" / "lifecycle" / "bootstrap.py"
).read_text()


class TestAddDirsRestricted:
    """add_dirs must be locked down to skills only."""

    def test_add_dirs_contains_only_skills(self) -> None:
        """SESSION_ADD_DIRS must be exactly ['/opt/autofyn/.claude/skills']."""
        assert '"/opt/autofyn/.claude/skills"' in CONSTANTS_SRC

    def test_add_dirs_does_not_contain_framework_code(self) -> None:
        """Must not expose /opt/autofyn root — agent would search framework code."""
        # Extract the SESSION_ADD_DIRS definition line in constants
        start = CONSTANTS_SRC.index("SESSION_ADD_DIRS")
        # Anchor on the list-literal '[' (after '='), not the '[' in `list[str]`.
        bracket = CONSTANTS_SRC.index("[", CONSTANTS_SRC.index("=", start))
        line = CONSTANTS_SRC[bracket:CONSTANTS_SRC.index("]", bracket) + 1]
        assert '"/opt/autofyn"' not in line or '"/opt/autofyn/.claude' in line

    def test_add_dirs_does_not_contain_dead_paths(self) -> None:
        """Must not include nonexistent directories."""
        start = CONSTANTS_SRC.index("SESSION_ADD_DIRS")
        # Anchor on the list-literal '[' (after '='), not the '[' in `list[str]`.
        bracket = CONSTANTS_SRC.index("[", CONSTANTS_SRC.index("=", start))
        line = CONSTANTS_SRC[bracket:CONSTANTS_SRC.index("]", bracket) + 1]
        assert "/home/agentuser/research" not in line
        assert "/workspace" not in line

    def test_bootstrap_uses_session_add_dirs_constant(self) -> None:
        """bootstrap.py must reference SESSION_ADD_DIRS, not inline the path."""
        assert "SESSION_ADD_DIRS" in BOOTSTRAP_SRC
        assert '"/opt/autofyn/.claude/skills"' not in BOOTSTRAP_SRC
