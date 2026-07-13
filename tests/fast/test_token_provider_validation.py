"""Tests for Token.provider validation: the model is the single provider gate.

The provider field is validated on the Token model itself (not only at the API
boundary) so every write path — API, autofill, future callers — rejects an
unknown provider before it can reach the encrypted pool and mismatch the
provider the broker acquires under.
"""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from common.models import Token
from db.constants import DEFAULT_PROVIDER, PROVIDER_ANTHROPIC


class TestTokenProviderValidation:
    """Token rejects unknown providers and accepts the valid ones."""

    def test_known_provider_is_accepted(self) -> None:
        """An explicit valid provider constructs without error."""
        assert Token(provider=PROVIDER_ANTHROPIC, value="sk-ant-a", label=None).provider == PROVIDER_ANTHROPIC

    def test_default_provider_is_accepted(self) -> None:
        """The default provider is itself valid."""
        assert Token(value="sk-ant-a").provider == DEFAULT_PROVIDER

    def test_unknown_provider_is_rejected(self) -> None:
        """An out-of-set provider raises rather than silently persisting."""
        with pytest.raises(ValidationError, match="unknown provider"):
            Token(provider="openai", value="sk-ant-a", label=None)
