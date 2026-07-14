"""Regression test: the effort a run actually used must be recorded and resumed.

effort was accepted per run but never persisted: it appeared in neither the
run_started audit nor the runs table, so "was this run high or max?" was
unanswerable after the fact. Worse, the resume path rebuilt StartRequest
without it, silently restarting a low/max run at DEFAULT_EFFORT.

resolve_effort is the single source of truth for the max->high downgrade, so
the value recorded is the one the model actually ran at, not the one requested.
"""

from __future__ import annotations

import pytest

from common.constants import (
    LEGACY_OPUS,
    SUPPORTED_GPT_SOL,
    SUPPORTED_GPT_TERRA,
    SUPPORTED_OPUS,
    resolve_effort,
)
from db.constants import EFFORT_HIGH, EFFORT_LOW, EFFORT_MAX


class TestRunEffortRecorded:
    """resolve_effort must report the effort a model will actually run at."""

    def test_max_survives_on_supporting_model(self) -> None:
        """A flagship keeps max."""
        assert resolve_effort(SUPPORTED_OPUS, EFFORT_MAX) == EFFORT_MAX
        assert resolve_effort(SUPPORTED_GPT_SOL, EFFORT_MAX) == EFFORT_MAX

    def test_max_downgrades_on_unsupported_model(self) -> None:
        """A non-flagship silently ran at high; that must be what we record."""
        assert resolve_effort(SUPPORTED_GPT_TERRA, EFFORT_MAX) == EFFORT_HIGH
        assert resolve_effort(LEGACY_OPUS, EFFORT_MAX) == EFFORT_HIGH

    @pytest.mark.parametrize("effort", [EFFORT_LOW, EFFORT_HIGH])
    def test_non_max_efforts_pass_through_unchanged(self, effort: str) -> None:
        """Only max is ever downgraded — nothing else is touched."""
        assert resolve_effort(SUPPORTED_GPT_TERRA, effort) == effort
        assert resolve_effort(SUPPORTED_OPUS, effort) == effort
