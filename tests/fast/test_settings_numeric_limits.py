"""Tests for max_concurrent_runs / runs_page_size validation in UpdateSettingsRequest."""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from backend.models import UpdateSettingsRequest
from db.constants import (
    MAX_CONCURRENT_RUNS_MAX,
    MAX_CONCURRENT_RUNS_MIN,
    RUNS_PAGE_SIZE_MAX,
    RUNS_PAGE_SIZE_MIN,
)


def _req(payload: dict[str, str]) -> UpdateSettingsRequest:
    """Build an UpdateSettingsRequest the way the endpoint does — from a body dict."""
    return UpdateSettingsRequest.model_validate(payload)


class TestSettingsNumericLimits:
    """PUT /api/settings must only accept in-bounds integers for the numeric limits."""

    def test_valid_values_accepted(self) -> None:
        req = _req({"max_concurrent_runs": "10", "runs_page_size": "30"})
        assert req.max_concurrent_runs == "10"
        assert req.runs_page_size == "30"

    def test_unset_values_stay_none(self) -> None:
        req = _req({})
        assert req.max_concurrent_runs is None
        assert req.runs_page_size is None

    def test_bounds_are_inclusive(self) -> None:
        _req({"max_concurrent_runs": str(MAX_CONCURRENT_RUNS_MIN)})
        _req({"max_concurrent_runs": str(MAX_CONCURRENT_RUNS_MAX)})
        _req({"runs_page_size": str(RUNS_PAGE_SIZE_MIN)})
        _req({"runs_page_size": str(RUNS_PAGE_SIZE_MAX)})

    def test_non_integer_max_concurrent_runs_rejected(self) -> None:
        with pytest.raises(ValidationError):
            _req({"max_concurrent_runs": "five"})

    def test_negative_max_concurrent_runs_rejected(self) -> None:
        with pytest.raises(ValidationError):
            _req({"max_concurrent_runs": "-1"})

    def test_above_max_concurrent_runs_rejected(self) -> None:
        with pytest.raises(ValidationError):
            _req({"max_concurrent_runs": str(MAX_CONCURRENT_RUNS_MAX + 1)})

    def test_zero_runs_page_size_rejected(self) -> None:
        with pytest.raises(ValidationError):
            _req({"runs_page_size": "0"})

    def test_above_max_runs_page_size_rejected(self) -> None:
        with pytest.raises(ValidationError):
            _req({"runs_page_size": str(RUNS_PAGE_SIZE_MAX + 1)})

    def test_non_integer_runs_page_size_rejected(self) -> None:
        with pytest.raises(ValidationError):
            _req({"runs_page_size": "15.5"})
