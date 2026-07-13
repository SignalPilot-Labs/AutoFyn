# Credential Providers & Model Families

How AutoFyn decides which credential and which API endpoint a run uses. One source of truth for the two-provider design, so the next provider (LiteLLM) slots in without re-litigating any of this.

## The two choices

**Anthropic — native, first-class.** Claude models run directly against the Anthropic subscription via `CLAUDE_CODE_OAUTH_TOKEN` (from `claude setup-token`). No proxy, no translation layer, exact SDK model IDs. This is the home turf; every other family is measured against it.

**OpenRouter — gateway for non-Claude families.** Models Anthropic does not serve (today: GPT-5.6 Sol and Terra) reach the SDK through OpenRouter's Anthropic-compatible endpoint. OpenRouter is a transport for other vendors' models — it is **never** a second way to reach Claude. LiteLLM will later be a second gateway with the same shape.

**Claude is never served through OpenRouter.** Running Claude through a gateway is strictly worse (extra hop, extra margin, no upside), and — more importantly — it would let one model belong to two providers. Forbidding it keeps the core invariant below.

## Core invariant: one model, one provider → one run, one provider

Every model belongs to exactly one provider (`SUPPORTED_MODELS[*].provider`). A run's model therefore fixes its provider for the whole run. Consequences:

- The broker rotates only over that provider's tokens (`credentials.py` filters the pool by provider before leasing).
- Credential injection is provider-specific and needs **no cross-provider clearing** — a run never switches providers mid-flight, so there is no stale env to scrub.
- A GPT run with no OpenRouter tokens fails loudly (`no openrouter credentials configured`) instead of silently falling back to an Anthropic key.

## Tiers are roles, not vendor labels

AutoFyn has two capability tiers, anchored on the native family:

- `opus` — the flagship, for hard reasoning and flagship subagents.
- `sonnet` — the fast, capable workhorse for the bulk of subagents.

A tier is a **role**, so another family can be mapped into it. When a developer's subagent declares `tier: opus`, it means "use the flagship of whatever family this run is on" — not literally Claude Opus.

| AutoFyn tier (role) | Anthropic (native) | OpenAI via OpenRouter |
| ------------------- | ------------------ | --------------------- |
| `opus` (flagship)   | Opus 4.8 / Fable 5 | **Sol**               |
| `sonnet` (workhorse)| Sonnet 4.6         | **Terra**             |

So on a GPT run, an `opus`-tier subagent runs Sol and a `sonnet`-tier subagent runs Terra. The developer's opus-vs-sonnet intent is preserved across families. This is why the mapping is defensible: we are not claiming Sol *is* Opus, only that Sol *plays the opus role* in the GPT family. (`_resolve_subagent_model` in `autofyn/prompts/subagent.py` implements this via `tier_model_for(provider, tier)`.)

`GPT-5.6 Luna` is intentionally omitted — it is a third (cheap) tier and AutoFyn has no role for it, so leaving it out costs nothing.

Max-effort membership (`MODELS_SUPPORTING_MAX_EFFORT`) is **per model**, not per tier: only each family's flagship unlocks it (Opus, Fable, Sonnet, and Sol). Terra does not, and downgrades `max` → `high`.

## Model ID vs. gateway slug

Each `SUPPORTED_MODELS` entry carries two identifiers that must stay distinct:

- `id` — AutoFyn's stable identifier. Flows through the picker, `localStorage`, the DB (`Run.model_name`), and `VALID_MODELS`.
- `api_model` — the slug the provider's API actually expects, injected into the SDK.

Today they coincide for every model (`openai/gpt-5.6-sol` is both). They are kept separate on purpose: the **same conceptual model can have a different slug on a different gateway** — GPT-5.6 Sol is `openai/gpt-5.6-sol` on OpenRouter but may be something else under LiteLLM. Routing always reads `api_model` (`api_model_for()`), never `id`, so adding LiteLLM later is a new set of entries with the same conceptual ids and their own slugs — no translation layer, no guessing.

## Env-var contract per provider

Injected per round by `acquire_and_inject` → `_provider_env`:

| Provider   | Env vars set |
| ---------- | ------------ |
| anthropic  | `CLAUDE_CODE_OAUTH_TOKEN=<token>` |
| openrouter | `ANTHROPIC_BASE_URL=https://openrouter.ai/api`, `ANTHROPIC_AUTH_TOKEN=<key>`, `ANTHROPIC_API_KEY=""` (explicitly empty so the SDK never falls back to a native key and bypasses the gateway), `ANTHROPIC_DEFAULT_OPUS_MODEL=<run api_model>`, `ANTHROPIC_DEFAULT_SONNET_MODEL=<workhorse api_model>` |

## Where things live / adding a provider

Provider and model constants and helpers live in `common/constants.py` (the credential/model domain, shared across the agent, sandbox, dashboard, and broker). DB-row keys and cooldown timing stay in `db/constants.py`.

To add a provider or model:

1. `common/constants.py` — add `PROVIDER_<NAME>` and extend `VALID_PROVIDERS`; add model IDs, a `SUPPORTED_MODELS` entry per model (with `id`, `api_model`, `tier`, `provider`), and the tier mapping in `_PROVIDER_TIER_MODELS`; add flagship models to `MODELS_SUPPORTING_MAX_EFFORT`; give each model a `_FALLBACK_MAP` entry. Add any gateway env-var names + base URL.
2. `_provider_env` in `autofyn/lifecycle/credentials.py` — add the injection branch for the new provider (fail loud on unknown).
3. `dashboard/frontend/lib/constants.ts` — add the provider to `CREDENTIAL_PROVIDERS` and a `TOKEN_PLACEHOLDERS` entry; `ModelSelector.tsx` `PROVIDER_LABELS` for the group header.

Sync/regression tests enforce the contract: `tests/fast/test_model_sync.py` (every model has the required fields, matching the TS `ModelInfo` interface), `tests/fast/test_provider_model_mapping.py` (every `VALID_MODELS` entry maps to a valid provider, tier, and api_model — `provider_for_model` is total). See also `docs/design-system.md` for the frontend token/primitive rules the settings UI follows.
