# Round 18 proof-reviewer adjudication — imo-2026-02

Three built approaches reviewed independently. Full detail also written into
`results/imo-2026-02/current.md` (Round 18 section, prepended above Round 17)
and into the two affected files
(`results/imo-2026-02/approaches/coordinate-bash-resultant-boundary-pointwise-tangent.md`,
`results/imo-2026-02/lemmas/d1-nonnegative-on-boundary-curve.md`).

## 1. `coordinate-bash-resultant-boundary-pointwise-tangent`

**Verdict: CHANGES REQUESTED.** (Builder claimed `solved`; rejected again,
for a different reason than round 17.)

**Part 1 — Gap 6 is genuinely closed. CERTIFIED.**

Independently rebuilt every load-bearing claim from raw definitions, in a
fresh `sympy`/`mpmath` session (not reusing the builder's script):

- The identity `G_curve(u) = -8 sin(u) cos^2(u) * h(u)` (`u = A/3 + pi/6`,
  `h(A) := X_0(A, beta_0(A)) - cos^2(beta_0(A))`) — rebuilt `G_curve(A)` and
  `h(A)` directly from `X_0, beta_0, K_c, P, Q, G`'s raw trigonometric
  definitions and confirmed the identity exactly (`sympy.simplify`,
  residual 0). Matches the file's hand-derivation term for term.
- The closed form `A* = 3*arcsin(sqrt(6)/4) - pi/2`: own fresh `mpmath`
  (dps=50) gives `0.40637778068433032938717469032930926267100175019852`,
  matching the population's standing 40-digit numeric `A*` to all 40
  digits. Confirmed `u* = A*/3 + pi/6 ≈ 0.6591 ∈ (pi/6, pi/3)` by the
  file's own rational-comparison argument (`1/4 < 3/8 < 3/4`), so the
  cofactor `-8 sin(u*) cos^2(u*) ≠ 0` and `G_curve(A*)=0 ⟹ h(A*)=0` (fact
  (ii), round 17's missing piece) is a genuine algebraic consequence, not
  a citation to an unproved numeric coincidence.
- `D_1(A*, B*) = 0`: independently confirmed to ≈1e-42 from the raw
  `D_1, RHS` definitions (own script, not the file's).
- Steps 1-4 (certified `mpmath.iv` sweeps: `B*` enclosure, derivative bound
  `D_1' ≥ 4` near the corner, value bound `D_1 > 0` away from it, MVT
  gluing): spot-checked via an own finite-difference derivative sweep near
  `B*` (≈4.626, matching the file's certified ≈4.625) and an own dense
  value sweep on `[B*, pi/3]` (no violation found).

Certified `lemmas/d1-nonnegative-on-boundary-curve.md` in full — Open gap 6
is closed. This is a genuine strengthening over round 17's rejected
version, not a re-hash.

**Part 2 — a new, independent gap found in "Full proof" Step 3.**

Per the round-18 dispatch's item (f) (trace the entire dependency chain end
to end for any other silent gap or scope mismatch — motivated explicitly by
round 17's false claim on this same route), I found one.

"Full proof" Step 3 ("Case (a)", `beta_1 ∈ (0, beta_0(A)]`) cites Theorem A
of `lemmas/claim-I-closed-and-claim-II-caseA-closed.md` — which proves
`f(beta) > 0` for `beta ∈ (beta_0, gamma)` — to close Case (a). But Case
(a)'s `beta_1` lies in the **complementary** interval `(0, beta_0]`, which
Theorem A does not cover. The file's own text even flags the mismatch
inline ("`G(beta_1) ≥ G(beta_0)` for `beta_1 ≤ beta_0` is not directly what's
needed") and then simply asserts a reduction to Theorem A without ever
justifying it — an unproved logical leap.

Independent verification (fresh script, 2,000,000 random `(A,B)` samples,
domain built directly from the file's own Case-(a) definition: `0<A<pi`,
`0<B≤C`, `beta_0(A) < gamma`, `0≤X_0≤1`, `beta_1 := arccos(sqrt(X_0)) ∈
(0, beta_0(A)]`):

- `G(beta_1) ≥ 0` (the quantity Theorem A's machinery targets) is **false
  in ≈70% of genuine Case-(a) samples** (35,329 / 50,649 tested), minimum
  observed ≈ -0.70. So `G` is not even the correct target quantity in Case
  (a) — consistent with, and explaining, an aside elsewhere in this same
  file ("Case (b) ... equivalently G(beta_1), not f, is the relevant
  quantity") that implies `f`, not `G`, is what's actually relevant in
  Case (a).
- `f(beta_1) > 0` (the quantity that aside identifies as relevant in Case
  (a)) has **zero violations** across the same 2,000,000 samples (51,068
  valid), minimum observed ≈0.616. So the needed fact is very likely true
  — but it is **not established by Theorem A** (wrong sub-interval) **or by
  any other certified lemma anywhere in the population's 18-round
  history.**

A plausible fix, not yet completed by anyone: Theorem A's own proof already
establishes `f'(beta) > 0` on the *whole* interval `(0, gamma)`, not just
`(beta_0, gamma)` (this is visible in the lemma's own proof text). Combined
with `f(0) = sin(A) * (2*sin(A+B) - sin(B))`, which an independent
2,000,000-sample sweep finds `≥ 0` throughout the domain (minimum observed
≈2e-6, consistent with `≥0`, equality only approached in a limit) but which
**no file in the population has proved**, this would extend `f > 0` down to
all of `(0, gamma)` and genuinely close Case (a). This is flagged as the
route's next concrete target (Open gap 7).

**Files edited this round** (both changes are surgical, preserving all
correct content):
- `lemmas/d1-nonnegative-on-boundary-curve.md`: Status → Certified (scoped
  explicitly to Gap 6 only, with a note pointing to the separate Gap-7
  finding).
- `approaches/coordinate-bash-resultant-boundary-pointwise-tangent.md`:
  Status header `solved → partial` with a full correction note; inline flag
  at "Full proof" Step 3; new "Open gap 7"; "Not yet promotable" section
  corrected to point at the new gap; the round-18 "Approaches tried" bullet
  amended to state the true (partial, not solved) outcome without deleting
  the builder's original content (kept, clearly marked "as filed by the
  builder").
- `current.md`: new Round 18 section prepended, with full detail on both
  the Gap-6 closure and the Gap-7 finding, `record_outcome` calls made for
  all three slugs.

**Net assessment.** This route has made real progress two rounds running
(round 17: closed nothing net, but sharpened the gap precisely; round 18:
genuinely closed Gap 6, found and precisely diagnosed Gap 7). It is now
narrower than ever — exactly one open gap, and a much more mechanical-
looking one than Gap 6 ever was — but it is not `solved`. Status: `partial`.

## 2. `coordinate-bash-resultant-boundary-pointwise-sos`

**Verdict: CHANGES REQUESTED.** Status `partial` — accurate as filed, no
overclaiming.

Diagnostic-only round on the Gram-matrix degeneracy (3 tests dispatched).
Test 1 finds a real but witness-dependent (not uniform across the two
tested witnesses) single-direction explanation for most of the "3
unexplained near-null directions"; Test 2 rules out the round-17-flagged
complex-conjugate-pair hypothesis via a genuine near-double-real-root
finding instead. No certificate is claimed anywhere in the file; every
result is correctly labeled diagnostic/numeric, and the witness-inconsistency
in Test 1 is reported honestly as breaking a "clean uniform mechanism"
reading rather than being spun as a clean win. Not independently re-run in
full this round (would require standing up the same `cvxpy`/CLARABEL/SCS
SDP pipeline from scratch on a ~35-coefficient degree-34 target), but no
overclaiming found on inspection of the write-up. No lemma submitted
(correct — nothing proved this round).

## 3. `spiral-similarity-bootstrap`

**Verdict: CHANGES REQUESTED.** Status `partial` — honest, real progress,
no overclaiming.

First real build of this diversity/insurance approach. Independently
re-derived, by hand, term-for-term, every step:

- **General lemma**: if `∠(PX,PY) = ∠(QX,QZ)` then `∠(XP,XQ) = ∠(PY,QZ)`,
  proved via the directed-angle chain rule (`∠(PY,QZ) = ∠(PY,PX) +
  ∠(PX,QX) + ∠(QX,QZ)`, then substitute the hypothesis and simplify). Checks
  out exactly as written — a clean, general, elementary fact.
- **Lemma A** (apply with P=B,Q=N,X=L,Y=K,Z=C to H2: `∠(BL,BK)=∠(NL,NC)`):
  conclusion `∠(LB,LN)=∠(BK,NC)`, and since N is the midpoint of AC,
  line NC = line AC, giving `∠BLN = ∠(BK,AC)`. Verified.
- **Lemma B** (apply with P=C,Q=M,X=K,Y=L,Z=B to H3, rewritten
  `∠(CK,CL)=∠(MK,MB)`): conclusion `∠(KC,KM)=∠(CL,MB)`, and since M is the
  midpoint of AB, line MB = line AB, giving `∠CKM = ∠(CL,AB)`. Verified.
- **Corollary**: combining with H1 (`∠(BK,BA)=∠(CA,CL)`, i.e.
  `∠(BK,AB) = -∠(CL,AC)`) and the chain rule twice more gives
  `∠BLN = ∠(AB,CL)`, and comparing with Lemma B
  (`∠CKM = ∠(CL,AB) = -∠(AB,CL)`) gives `∠BLN + ∠CKM ≡ 0 (mod π)`.
  Verified — every substitution checks out exactly.

This is a genuine, correct new synthetic result, obtained with no
coordinate elimination anywhere — real diversity value against the
population's coordinate/resultant/SOS cluster, per CLAUDE.md's diversity
guidance. The file's own disclosure that this does not yet connect to
`O, M, N` (the load-bearing open gap, per its own "Open gaps" section) is
accurate; Status `partial` is honest and not overclaimed.

## Summary

| Slug | Verdict | Status |
|---|---|---|
| coordinate-bash-resultant-boundary-pointwise-tangent | CHANGES REQUESTED | partial (Gap 6 closed & certified; new Gap 7 found) |
| coordinate-bash-resultant-boundary-pointwise-sos | CHANGES REQUESTED | partial (honest diagnostics, no certificate) |
| spiral-similarity-bootstrap | CHANGES REQUESTED | partial (real new lemma, load-bearing gap to O/M/N still open) |

No APPROVE this round. `current.md`'s top-level Status remains `partial`.
