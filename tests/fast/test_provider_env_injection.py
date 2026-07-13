"""Tests for _provider_env — the per-provider SDK credential env builder.

Guards that each provider gets exactly the env vars its routing needs, and that
an unknown provider fails loudly rather than injecting a partial env. See
docs/providers.md.
"""

import pytest

from lifecycle.credentials import _provider_env
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


class TestProviderEnvInjection:
    """_provider_env produces the right env set per provider."""

    def test_anthropic_injects_only_oauth_token(self) -> None:
        env = _provider_env(PROVIDER_ANTHROPIC, SUPPORTED_OPUS, "sk-ant-oat01-xyz")
        assert env == {ENV_CLAUDE_OAUTH_TOKEN: "sk-ant-oat01-xyz"}

    def test_openrouter_injects_gateway_env(self) -> None:
        env = _provider_env(PROVIDER_OPENROUTER, SUPPORTED_GPT_SOL, "sk-or-v1-abc")
        assert env[ENV_ANTHROPIC_BASE_URL] == OPENROUTER_BASE_URL
        assert env[ENV_ANTHROPIC_AUTH_TOKEN] == "sk-or-v1-abc"
        # Explicitly empty so the SDK never falls back to a native Anthropic key.
        assert env[ENV_ANTHROPIC_API_KEY] == ""
        # Model overrides route both SDK tiers to OpenRouter slugs.
        assert env[ENV_ANTHROPIC_DEFAULT_OPUS_MODEL] == api_model_for(SUPPORTED_GPT_SOL)
        assert env[ENV_ANTHROPIC_DEFAULT_SONNET_MODEL] == api_model_for(SUPPORTED_GPT_TERRA)

    def test_openrouter_never_sets_claude_oauth_token(self) -> None:
        """A GPT run must not carry the native Claude OAuth var."""
        env = _provider_env(PROVIDER_OPENROUTER, SUPPORTED_GPT_SOL, "sk-or-v1-abc")
        assert ENV_CLAUDE_OAUTH_TOKEN not in env

    def test_unknown_provider_raises(self) -> None:
        with pytest.raises(ValueError):
            _provider_env("litellm", SUPPORTED_OPUS, "whatever")
