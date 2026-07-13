"""Tests for parse_token_pool: legacy entries upgrade, new dict entries round-trip.

The pool schema grew from list[str] -> list[Token{value,label}] -> +provider.
parse_token_pool must read every historical shape: bare strings (pre-pool) and
provider-less dicts (pre-provider) both upgrade to DEFAULT_PROVIDER; dicts with
an explicit provider keep it.
"""

from __future__ import annotations

from common.models import Token, parse_token_pool
from db.constants import DEFAULT_PROVIDER


class TestParseTokenPool:
    """parse_token_pool normalizes decrypted pools to list[Token]."""

    def test_legacy_string_entries_upgrade_to_default_provider(self) -> None:
        """Pre-pool bare strings upgrade to Tokens with label=None, default provider."""
        result = parse_token_pool(["sk-ant-a", "sk-ant-b"])

        assert result == [
            Token(provider=DEFAULT_PROVIDER, value="sk-ant-a", label=None),
            Token(provider=DEFAULT_PROVIDER, value="sk-ant-b", label=None),
        ]

    def test_provider_less_dicts_upgrade_to_default_provider(self) -> None:
        """Dicts written before the provider field default to DEFAULT_PROVIDER."""
        result = parse_token_pool(
            [{"value": "sk-ant-a", "label": "work"}, {"value": "sk-ant-b", "label": None}]
        )

        assert result == [
            Token(provider=DEFAULT_PROVIDER, value="sk-ant-a", label="work"),
            Token(provider=DEFAULT_PROVIDER, value="sk-ant-b", label=None),
        ]

    def test_explicit_provider_is_preserved(self) -> None:
        """A dict with an explicit provider keeps it."""
        result = parse_token_pool([{"provider": "anthropic", "value": "sk-ant-a", "label": "work"}])

        assert result == [Token(provider="anthropic", value="sk-ant-a", label="work")]

    def test_mixed_legacy_and_new_entries(self) -> None:
        """A pool mid-migration may hold both shapes at once."""
        result = parse_token_pool(
            ["sk-ant-a", {"provider": "anthropic", "value": "sk-ant-b", "label": "spare"}]
        )

        assert result == [
            Token(provider=DEFAULT_PROVIDER, value="sk-ant-a", label=None),
            Token(provider="anthropic", value="sk-ant-b", label="spare"),
        ]

    def test_empty_pool(self) -> None:
        """An empty decrypted pool yields an empty list."""
        assert parse_token_pool([]) == []
