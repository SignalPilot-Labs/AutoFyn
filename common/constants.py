"""Provider and model domain constants — the single source of truth.

These describe the credential/model domain (which providers exist, which
models are served by which provider, how a model maps to SDK env vars), not
database schema. They live in ``common`` because every layer needs them:
the broker, the agent orchestrator, the sandbox session, the dashboard API,
and the CLI-adjacent settings all import from here.

Two-provider model (see docs/providers.md):
  - anthropic  — native, first-class. Claude via CLAUDE_CODE_OAUTH_TOKEN.
  - openrouter — gateway for non-Claude families (GPT-5.6). Routed through
                 OpenRouter's Anthropic-compatible endpoint.

A model belongs to exactly one provider, so a run is single-provider. Tiers
(opus/sonnet) are roles anchored on the native family: opus is the flagship,
sonnet the workhorse. Non-Claude families map into those roles (Sol plays the
opus role, Terra the sonnet role) so a developer's tier intent is preserved
across providers.
"""

# ── Providers ──
PROVIDER_ANTHROPIC: str = "anthropic"
PROVIDER_OPENROUTER: str = "openrouter"
# All credential providers the pool accepts. Anthropic is native; OpenRouter
# is the gateway for non-Claude families. LiteLLM appends here later.
VALID_PROVIDERS: tuple[str, ...] = (PROVIDER_ANTHROPIC, PROVIDER_OPENROUTER)
DEFAULT_PROVIDER: str = PROVIDER_ANTHROPIC
VALID_PROVIDERS_PATTERN: str = f"^({'|'.join(VALID_PROVIDERS)})$"

# OpenRouter's Anthropic-compatible endpoint base URL.
OPENROUTER_BASE_URL: str = "https://openrouter.ai/api"

# ── SDK credential env-var names ──
# Anthropic native: the OAuth token from `claude setup-token`.
ENV_CLAUDE_OAUTH_TOKEN: str = "CLAUDE_CODE_OAUTH_TOKEN"
# OpenRouter routing: point the SDK at OpenRouter, auth with the OpenRouter
# key, and blank ANTHROPIC_API_KEY so the SDK never falls back to a native
# Anthropic key that would bypass the gateway.
ENV_ANTHROPIC_BASE_URL: str = "ANTHROPIC_BASE_URL"
ENV_ANTHROPIC_AUTH_TOKEN: str = "ANTHROPIC_AUTH_TOKEN"
ENV_ANTHROPIC_API_KEY: str = "ANTHROPIC_API_KEY"
# Model-override env vars the SDK reads to route its opus/sonnet tiers to
# concrete provider model slugs (used for OpenRouter runs).
ENV_ANTHROPIC_DEFAULT_OPUS_MODEL: str = "ANTHROPIC_DEFAULT_OPUS_MODEL"
ENV_ANTHROPIC_DEFAULT_SONNET_MODEL: str = "ANTHROPIC_DEFAULT_SONNET_MODEL"

# ── Subagent tiers (roles) ──
# Each subagent declares a tier; the resolver binds it to a concrete model in
# the run's provider family. opus = flagship, sonnet = workhorse.
TIER_OPUS: str = "opus"
TIER_SONNET: str = "sonnet"
TIER_LEGACY: str = "legacy"

# ── Model IDs ──
# Anthropic native — exact SDK model IDs, no aliases, no translation layer.
SUPPORTED_FABLE: str = "claude-fable-5"
SUPPORTED_OPUS: str = "claude-opus-4-8"
SUPPORTED_SONNET: str = "claude-sonnet-4-6"
LEGACY_OPUS: str = "claude-opus-4-5"
# OpenRouter — exact OpenRouter model slugs (openai/gpt-5.6-*).
SUPPORTED_GPT_SOL: str = "openai/gpt-5.6-sol"
SUPPORTED_GPT_TERRA: str = "openai/gpt-5.6-terra"

VALID_MODELS: tuple[str, ...] = (
    SUPPORTED_FABLE,
    SUPPORTED_OPUS,
    SUPPORTED_SONNET,
    LEGACY_OPUS,
    SUPPORTED_GPT_SOL,
    SUPPORTED_GPT_TERRA,
)
DEFAULT_MODEL: str = SUPPORTED_OPUS
VALID_MODELS_PATTERN: str = f"^({'|'.join(VALID_MODELS)})$"

# Structured metadata for the /api/models endpoint — the single source of
# truth the dashboard fetches at runtime. The frontend defines no model list
# of its own; everything textual lives here.
#   id          — AutoFyn's stable model ID (picker, localStorage, DB Run.model_name)
#   api_model   — the slug the provider's API expects (injected into the SDK).
#                 Kept SEPARATE from id: the same conceptual model can have a
#                 different slug on a different gateway (OpenRouter vs. a future
#                 LiteLLM), so routing reads api_model, never id. For native
#                 Anthropic models the two coincide.
#   label       — full product name, shown in the picker
#   short       — compact name, shown on badges/run cards
#   description — one-line picker blurb
#   context     — context-window blurb
#   tier        — opus | sonnet | legacy (drives subagent tier resolution)
#   provider    — anthropic | openrouter (drives credential + routing)
SUPPORTED_MODELS: list[dict[str, str]] = [
    {
        "id": SUPPORTED_FABLE,
        "api_model": SUPPORTED_FABLE,
        "label": "Claude Fable 5",
        "short": "Fable 5",
        "description": "Most capable, for demanding agentic work",
        "context": "1M context",
        "tier": TIER_OPUS,
        "provider": PROVIDER_ANTHROPIC,
    },
    {
        "id": SUPPORTED_OPUS,
        "api_model": SUPPORTED_OPUS,
        "label": "Claude Opus 4.8",
        "short": "Opus 4.8",
        "description": "Highly capable, strong for agents",
        "context": "1M context",
        "tier": TIER_OPUS,
        "provider": PROVIDER_ANTHROPIC,
    },
    {
        "id": SUPPORTED_SONNET,
        "api_model": SUPPORTED_SONNET,
        "label": "Claude Sonnet 4.6",
        "short": "Sonnet 4.6",
        "description": "Fast and capable",
        "context": "1M context",
        "tier": TIER_SONNET,
        "provider": PROVIDER_ANTHROPIC,
    },
    {
        "id": LEGACY_OPUS,
        "api_model": LEGACY_OPUS,
        "label": "Claude Opus 4.5",
        "short": "Opus 4.5",
        "description": "Legacy Opus model",
        "context": "200K context",
        "tier": TIER_LEGACY,
        "provider": PROVIDER_ANTHROPIC,
    },
    {
        "id": SUPPORTED_GPT_SOL,
        "api_model": SUPPORTED_GPT_SOL,
        "label": "GPT-5.6 Sol",
        "short": "Sol",
        "description": "OpenAI flagship, top reasoning via OpenRouter",
        "context": "1M context",
        "tier": TIER_OPUS,
        "provider": PROVIDER_OPENROUTER,
    },
    {
        "id": SUPPORTED_GPT_TERRA,
        "api_model": SUPPORTED_GPT_TERRA,
        "label": "GPT-5.6 Terra",
        "short": "Terra",
        "description": "OpenAI balanced workhorse via OpenRouter",
        "context": "1M context",
        "tier": TIER_SONNET,
        "provider": PROVIDER_OPENROUTER,
    },
]

# Models that support effort="max". Others get downgraded to "high".
# Per family, only the flagship unlocks max reasoning.
MODELS_SUPPORTING_MAX_EFFORT: frozenset[str] = frozenset(
    {SUPPORTED_FABLE, SUPPORTED_OPUS, SUPPORTED_SONNET, SUPPORTED_GPT_SOL}
)

# Per-provider flagship (opus role) and workhorse (sonnet role) model IDs.
# The subagent tier resolver maps an opus-tier subagent to the flagship and a
# sonnet-tier subagent to the workhorse of whichever family the run is on.
_PROVIDER_TIER_MODELS: dict[str, dict[str, str]] = {
    PROVIDER_ANTHROPIC: {TIER_OPUS: SUPPORTED_OPUS, TIER_SONNET: SUPPORTED_SONNET},
    PROVIDER_OPENROUTER: {TIER_OPUS: SUPPORTED_GPT_SOL, TIER_SONNET: SUPPORTED_GPT_TERRA},
}

# Rate-limit fallback: flagship falls back to the workhorse; workhorse has none.
_FALLBACK_MAP: dict[str, str | None] = {
    SUPPORTED_OPUS: SUPPORTED_SONNET,
    SUPPORTED_SONNET: None,
    LEGACY_OPUS: SUPPORTED_SONNET,
    SUPPORTED_FABLE: SUPPORTED_SONNET,
    SUPPORTED_GPT_SOL: SUPPORTED_GPT_TERRA,
    SUPPORTED_GPT_TERRA: None,
}

# model id -> provider, derived from SUPPORTED_MODELS (single source of truth).
_MODEL_PROVIDER: dict[str, str] = {m["id"]: m["provider"] for m in SUPPORTED_MODELS}
# model id -> tier, derived from SUPPORTED_MODELS.
_MODEL_TIER: dict[str, str] = {m["id"]: m["tier"] for m in SUPPORTED_MODELS}
# model id -> gateway API slug (what the provider's API actually expects).
_MODEL_API: dict[str, str] = {m["id"]: m["api_model"] for m in SUPPORTED_MODELS}


def api_model_for(model: str) -> str:
    """Return the provider-API slug for an AutoFyn model ID. Fails loudly."""
    api = _MODEL_API.get(model)
    if api is None:
        raise ValueError(f"no api_model for model '{model}' (not in SUPPORTED_MODELS)")
    return api


def provider_for_model(model: str) -> str:
    """Return the provider that serves ``model``.

    Fails loudly for an unknown model rather than defaulting to a provider —
    a wrong default would silently route a model to the wrong gateway.
    """
    provider = _MODEL_PROVIDER.get(model)
    if provider is None:
        raise ValueError(f"no provider for model '{model}' (not in SUPPORTED_MODELS)")
    return provider


def tier_for_model(model: str) -> str:
    """Return the tier (role) of an AutoFyn model ID. Fails loudly if unknown."""
    tier = _MODEL_TIER.get(model)
    if tier is None:
        raise ValueError(f"no tier for model '{model}' (not in SUPPORTED_MODELS)")
    return tier


def fallback_model_for(model: str) -> str | None:
    """Return the rate-limit fallback model, or None. Fails loudly if unknown."""
    if model not in _FALLBACK_MAP:
        raise ValueError(f"no fallback entry for model '{model}'")
    return _FALLBACK_MAP[model]


def tier_model_for(provider: str, tier: str) -> str:
    """Resolve a (provider, tier) role to a concrete model ID. Fails loudly."""
    family = _PROVIDER_TIER_MODELS.get(provider)
    if family is None:
        raise ValueError(f"no tier models for provider '{provider}'")
    model = family.get(tier)
    if model is None:
        raise ValueError(f"provider '{provider}' has no model for tier '{tier}'")
    return model


def rotation_key_for(provider: str, base_key: str) -> str:
    """Per-provider rotation bookmark key.

    Each provider rotates over its own token subset, so each needs its own
    bookmark — a shared index would index the wrong subset once providers mix.
    """
    if provider not in VALID_PROVIDERS:
        raise ValueError(f"unknown provider '{provider}'")
    return f"{base_key}:{provider}"


def openrouter_model_env(model: str) -> dict[str, str]:
    """Build the SDK model-override env for an OpenRouter run.

    Routes the SDK's opus tier to the run's model and its sonnet tier to the
    family workhorse, so subagents resolve correctly through the gateway. Uses
    each model's gateway api_model slug, not its AutoFyn id. Fails loudly if
    handed a non-OpenRouter model.
    """
    if provider_for_model(model) != PROVIDER_OPENROUTER:
        raise ValueError(f"openrouter_model_env called with non-OpenRouter model '{model}'")
    return {
        ENV_ANTHROPIC_DEFAULT_OPUS_MODEL: api_model_for(model),
        ENV_ANTHROPIC_DEFAULT_SONNET_MODEL: api_model_for(
            tier_model_for(PROVIDER_OPENROUTER, TIER_SONNET)
        ),
    }
