"""Tests for _provider_env — the per-provider SDK credential env builder.

Guards that each provider gets exactly the env vars its routing needs, and that
an unknown provider fails loudly rather than injecting a partial env. See
docs/providers.md.
"""

import pytest

from lifecycle.credentials import _provider_env
from common.models import Token
from common.constants import (
    ENV_ANTHROPIC_API_KEY,
    ENV_ANTHROPIC_AUTH_TOKEN,
    ENV_ANTHROPIC_BASE_URL,
    ENV_ANTHROPIC_DEFAULT_OPUS_MODEL,
    ENV_ANTHROPIC_DEFAULT_SONNET_MODEL,
    ENV_CLAUDE_OAUTH_TOKEN,
    OPENROUTER_BASE_URL,
    PROVIDER_ANTHROPIC,
    PROVIDER_OPENROUTER,
    SUPPORTED_GPT_SOL,
    SUPPORTED_OPUS,
    api_model_for,
    SUPPORTED_GPT_TERRA,
)


def _token(provider: str, value: str) -> Token:
    return Token(provider=provider, value=value, label=None)


class TestProviderEnvInjection:
    """_provider_env produces the right env set for the selected token's provider."""

    def test_anthropic_injects_only_oauth_token(self) -> None:
        env = _provider_env(_token(PROVIDER_ANTHROPIC, "sk-ant-oat01-xyz"), SUPPORTED_OPUS)
        assert env == {ENV_CLAUDE_OAUTH_TOKEN: "sk-ant-oat01-xyz"}

    def test_openrouter_injects_gateway_env(self) -> None:
        env = _provider_env(_token(PROVIDER_OPENROUTER, "sk-or-v1-abc"), SUPPORTED_GPT_SOL)
        assert env[ENV_ANTHROPIC_BASE_URL] == OPENROUTER_BASE_URL
        assert env[ENV_ANTHROPIC_AUTH_TOKEN] == "sk-or-v1-abc"
        # Explicitly empty so the SDK never falls back to a native Anthropic key.
        assert env[ENV_ANTHROPIC_API_KEY] == ""
        # Model overrides route both SDK tiers to OpenRouter slugs.
        assert env[ENV_ANTHROPIC_DEFAULT_OPUS_MODEL] == api_model_for(
            SUPPORTED_GPT_SOL, PROVIDER_OPENROUTER
        )
        assert env[ENV_ANTHROPIC_DEFAULT_SONNET_MODEL] == api_model_for(
            SUPPORTED_GPT_TERRA, PROVIDER_OPENROUTER
        )

    def test_openrouter_never_sets_claude_oauth_token(self) -> None:
        """A GPT run must not carry the native Claude OAuth var."""
        env = _provider_env(_token(PROVIDER_OPENROUTER, "sk-or-v1-abc"), SUPPORTED_GPT_SOL)
        assert ENV_CLAUDE_OAUTH_TOKEN not in env

    def test_unknown_provider_raises(self) -> None:
        """A token whose provider has no env branch fails loud, not silently.

        Token validation blocks unknown providers at the pool boundary, so bypass
        it here (model_construct) to exercise _provider_env's own else-branch —
        the guard that catches a valid-in-pool provider we forgot to wire.
        """
        rogue = Token.model_construct(provider="litellm", value="whatever", label=None)
        with pytest.raises(ValueError):
            _provider_env(rogue, SUPPORTED_OPUS)
