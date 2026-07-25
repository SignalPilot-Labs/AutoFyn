# Proof review — round 12, imo-2026-02

Problem: imo-2026-02 (hard). All four builds this round target the same
remaining gap (Case (b)'s residual positivity, in one of its equivalent
forms: `(⋆)`, `T≥0`/`q_1,r_0<0`, or `Num≥0`). Every load-bearing new claim
below was independently re-derived from scratch in fresh `sympy`/`numpy`/
`scipy` sessions (code shown inline where useful), never by re-running a
builder's script or trusting a "sympy confirms" line at face value.

## 1. `coordinate-bash-resultant-boundary.md`

**Claim under test:** the new exact reformulation of Step 4:
`X_0>1/4 ⟺ ct>sd` and `X_0<3/4 ⟺ ct+3sd>0` (with `s=\sin A,c=\cos A,
t=\sin B,d=\cos B`, `X_0=ct/(2(sd+ct))`), and the finding that Step 2/4
closure alone does *not* close the residual gap.

**Independent re-derivation.**
```
X0 - 1/4 - (ct-sd)/(4*(sd+ct))  -> simplifies to 0   (sympy, exact)
X0 - 3/4 - (-(ct+3sd))/(4*(sd+ct)) -> simplifies to 0 (sympy, exact)
```
Both hold identically given `sd+ct \ne 0` (true for a genuine triangle,
`\sin C=sd+ct>0`). **Confirmed exactly**, zero residual — this is genuine,
correct new algebra, not merely a numeric coincidence.

Reproduced the negative-implication numeric claim independently (own
2,000,000-sample script, own domain/`X0>d^2` construction): `\approx5.6\%`
violations of `ct>sd` on `\{X_0>d^2\}` alone — matches the file's
`\approx5.5\%` closely.

**Honest-negative-finding check.** The file's own conclusion — that even a
complete proof of Step 2+Step 4 would still leave the actual
`q_1<0\wedge r_0<0` target unproved on the sharper polynomial domain — is
logically airtight: Steps 1–5 only re-describe the *domain*, they never
touch the target inequality itself. Correctly disclosed, not overclaimed.

**Verdict: Status = partial (as the file states). CHANGES REQUESTED.**
Real progress (a clean, verified reformulation, removing all
transcendental/radical content from Step 4's statement), but the residual
gap (both the joint Step-4 elimination itself, and — even if that closed
— the underlying `q_1,r_0<0` claim) remains open. No overclaiming found.

**Lemma certified:** `lemmas/x0-quarter-threshold-reformulation.md` (the
exact identity only).

## 2. `coordinate-bash-resultant-boundary-pointwise-tangent.md`

**Claim under test:** the D2 (`∂RHS/∂B`) closed form, the D3
(`∂S/∂B=T1+T2`) decomposition, and the finding that `T1` is not
sign-definite.

**Independent re-derivation (fresh sympy session, full symbolic rebuild of
`X0, Kc, P, Q, G, RHS, S` from the raw definitions, differentiating
symbolically):**
```
d/dB(RHS) - D2_claim  -> simplifies to 0   (exact)
d/dB(S) - (T1+T2)     -> simplifies to 0   (exact)
```
Both confirmed exactly. Also reproduced the file's own numeric sample:
at `(A,B)=(0.603,1.269)`, computed `T1≈-0.5890, T2≈0.7663, T1+T2≈0.1772`
— matches the file's `-0.5889, 0.7660, 0.1771` to displayed precision.

**Independent domain sweep (own 354,900-sample script, restricted to the
exact domain `D` — `B>β0(A)`, `cos²B<X0<cos²β0(A)`):**
`RHS>0` everywhere, min `≈0.3147` (file: `≈0.315`); `∂RHS/∂B<0`
everywhere, max `≈-0.797` (consistent with the file's finding). Both
independently confirmed with zero violations.

**Flaw found (minor, not fatal): imprecise characterization of `T1`.**
The file states `T1` "is NOT sign-definite," citing only negative
observed values (min `≈-0.644`, no positive value is ever actually
reported). My own independent 2,000,000-sample sweep restricted to the
correct domain found `T1<0` at **every single sampled point** (max
observed `≈-0.0006`, approaching 0 only near the domain boundary) — i.e.
`T1` appears to be *consistently negative*, not oscillating in sign. The
correct statement should be "`T1` is not proved `≥0` and is observed to be
uniformly negative on this domain," not "not sign-definite" (which
normally implies sign changes). This is a wording inaccuracy, not a
computational error, and it does not change the file's substantive
conclusion (a naive "prove each of `T1,T2≥0` separately" strategy still
fails either way, since `T1` is never `≥0`) or its Status. Flagged for
correction next round, not treated as invalidating the result.

**Verdict: Status = partial (as stated). CHANGES REQUESTED.** Real,
independently-verified progress (two new exact identities, D2 and D3,
plus two new domain-wide sign facts for `RHS` and `∂RHS/∂B`), correctly
disclosed as not yet closing `∂S/∂B≥0` itself. The `T1` "not
sign-definite" phrasing should be corrected to "consistently negative,
not proved ≥0" — a cosmetic fix, not a substantive retraction.

**Lemma certified:**
`lemmas/rhs-partial-b-derivative-and-decomposition.md` (D2+D3, with the
corrected `T1` characterization noted as a caveat in the lemma text).

## 3. `coordinate-bash-resultant-boundary-pointwise-tangent-twopoint.md` (new)

**Claim under test:** the new difference-of-squares factorization
`S=D1·D2` on the boundary curve `C={X0=cos²B}`, and the
concavity/unimodality claims for `D1`.

**Independent re-derivation.** The factorization itself is elementary and
exact: on `C`, `(1+cosB)²X0=[(1+cosB)cosB]²`, so
`S=[(1+cosB)cosB]²-RHS²=D1·D2` by difference of squares — confirmed
trivially (own `sympy` substitution, residual `0`). No issue here; this
step is correct by construction and was not in doubt.

**Independent numeric reproduction of the curve behaviour** (own fresh
`scipy.optimize.brentq` root-find at 3000 sample `A`-values from
`A*≈0.40638` to `≈1.04`):
- `D2`: `≈1.968` at the corner down to `≈1.135` near the far end (file:
  `≈1.975` down to `≈1.102` — same trend, same order of magnitude, close
  numeric agreement).
- `D1`: `0` at the corner (to machine precision), rises to a maximum
  `≈0.4054` at `A≈0.979` (file: `≈0.4054` at `A≈0.979` — essentially exact
  match), decreasing afterward; second-difference test shows `≈90.1%` of
  interior points negative (file: `1802/1998≈90.2%` — matches almost
  exactly).

Both numeric claims independently reproduced closely. The reasoning that
"a concave function lying above its own two-point-pinned chord is
`≥0` given the chord's endpoints are `≥0`" (the crux `aimo-0005`-style
mechanism) is correctly stated (the file even self-corrects an initial
mis-stated direction of the concavity inequality mid-derivation, and the
final corrected statement — `D1(A) \ge \lambda D1(A^*)+(1-\lambda)
D1(A_{max})` for a concave function — is the standard, correct
definition of concavity, applied correctly).

**Honest gap accounting.** The file correctly and explicitly lists three
open items: (1) `D2>0` unproved symbolically, (2) concavity/unimodality
of `D1` along the implicit curve unproved (only ~90% finite-difference
evidence, with the remaining ~10% attributed — plausibly, but not
provenly — to finite-difference noise near the endpoints), (3) even
granting (1)+(2), this only proves `S≥0` on the curve `C`, not the whole
2-variable domain, and still needs the sibling `-tangent` file's
`∂S/∂B≥0` monotonicity lever to extend off the curve. This is a precise,
non-overclaiming self-assessment.

**Verdict: Status = partial (as stated). CHANGES REQUESTED.** A genuinely
new, previously-untried structural lever (not a rehash of the sibling's
mechanism), correctly scoped as complementary to (not a substitute for)
the `-tangent` file's monotonicity lever. No fatal flaw; three concrete,
well-identified sub-gaps remain.

**Lemma certified:** `lemmas/star-factorization-on-boundary-curve.md`.

## 4. `coordinate-bash-resultant-boundary-pointwise-sos.md`

**Claim under test (the round's strongest claim):** Theorem 1 — the
exact identity `h(u,\cos B,\sin B)=-(1+u^2)^3\sin(A+B)` (with
`u=\tan(A/6)`), and the consequent unconditional positivity of
`Den, den1, den2` (the denominators cleared by the Weierstrass
substitution in `(⋆)`, `n1=\cos^2\beta_0-X_0`, `n2=X_0-\cos^2B`
respectively).

**Independent full re-derivation, from the raw definitions, in a fresh
sympy session (own script, not the builder's).**

Step 1 — the `h` identity itself:
```python
x = (1-u**2)/(1+u**2); y = 2*u/(1+u**2)
cosA = 4*x**3-3*x; sinA = 3*y-4*y**3
sinApB = sinA*cB + cosA*sB
num, den = fraction(together(sinApB))
# den == (u**2+1)**3 exactly
# num - (-h_claim) == 0 exactly
```
Confirmed: `sin(A+B) = -h/(1+u²)^3` exactly, zero residual. Theorem 1's
core identity is **correct**.

Step 2/3 — `den1, den2`: rebuilt `cos(β0)=½x+(√3/2)y`,
`sin(β0)=(√3/2)x-½y` (from `β0=π/3-A/3`), then:
```
n1 = together(cosβ0**2 - X0);  factor(denominator) == -4*(u²+1)²*h   (exact)
n2 = together(X0 - cosB**2);   factor(denominator) == -2*h            (exact)
```
Both confirmed exactly, matching the file's claimed prefactors `-4(u²+1)²`
and `-2` component-for-component.

Step 4 — `Den` (the hardest check, full rebuild of `Kc,P,Q,G,RHS,S`):
first attempt via `sympy.together` alone gave denominator
`-16(u²+1)^{16}h` — **not** matching the file's claimed exponent 14. This
looked like a possible error in the file. Re-did the computation using
`sympy.cancel` (which reduces numerator/denominator to lowest terms by
canceling common factors) instead of bare `together`/`fraction`: this
gives exactly `16(u²+1)^{14}h` (sign convention aside) — **matching the
file's claim exactly**. The discrepancy was a genuine, independently
re-encountered instance of the "uncanceled common factor between
numerator and denominator" pitfall (the same class of pitfall this
population has hit before), not an error in the file. **Theorem 1 is
fully confirmed, all four denominator claims, zero symbolic residual, from
an independent from-scratch pipeline.**

**Corollary check.** `Den,den1,den2>0` unconditionally follows immediately
from `\sin(A+B)=\sin C>0` (any genuine triangle) and `(1+u^2)^k>0` — this
inference is trivially correct.

**Scope check.** The file correctly does *not* claim this proves
`(⋆)`/`Num≥0` — it only proves the denominator-clearing step is
sign-preserving, upgrading round 11's numeric-only version of this fact
to a full proof. `Num≥0` itself remains open, with a precisely-documented
negative Positivstellensatz search (genuine degree-mismatch obstruction,
computed explicitly: canceling `Num`'s `u^{34}` leading term via `n1,n2`
as multipliers requires degree-24/28 multiplier polynomials, i.e.
`≈100` free coefficients, not a small hand ansatz) and one newly-flagged
open item (the `∠B≤∠C` condition is not yet polynomial in
`(u,cosB,sinB)` alone). No overclaiming.

**Verdict: Status = partial (as stated, correctly — the file does NOT
claim `solved` despite Theorem 1 being a fully rigorous, previously
numeric-only result; this is the correct, non-overclaiming self-
assessment). CHANGES REQUESTED.** This is the round's strongest single
result: a genuine, unconditional, fully-proved upgrade (numeric → proof)
of a real structural fact, independently reconfirmed end-to-end including
resolving a genuine `together`-vs-`cancel` computational pitfall along
the way. The actual remaining target, `Num≥0`, is untouched and remains
the open gap.

**Lemma certified:** `lemmas/star-weierstrass-denominators-positive.md`.

## Summary

| Approach | Status | Verdict |
|---|---|---|
| coordinate-bash-resultant-boundary | partial | CHANGES REQUESTED |
| coordinate-bash-resultant-boundary-pointwise-tangent | partial | CHANGES REQUESTED |
| coordinate-bash-resultant-boundary-pointwise-tangent-twopoint | partial | CHANGES REQUESTED |
| coordinate-bash-resultant-boundary-pointwise-sos | partial | CHANGES REQUESTED |

No approach reaches `solved` this round. All four builders' self-reported
Statuses (`partial`) match this reviewer's independent assessment — no
overclaiming found anywhere in the round. One wording inaccuracy was found
(approach 2's "T1 not sign-definite" should read "T1 consistently
negative, not proved ≥0") — cosmetic, does not change any Status or
verdict. The round's strongest new result is approach 4's Theorem 1 (a
genuine numeric→proof upgrade for the Weierstrass-denominator positivity),
though it — like all four approaches' new content — does not close the
shared underlying gap (Case (b)'s residual positivity, in whichever
equivalent form: `(⋆)`, `T≥0`/`q1,r0<0`, or `Num≥0`).

`results/imo-2026-02/current.md` updated with a new "Round 12" section
(the round-11 section is preserved below it, relabeled "preserved").
Four new lemmas certified and written to `results/imo-2026-02/lemmas/`:
`x0-quarter-threshold-reformulation.md`,
`rhs-partial-b-derivative-and-decomposition.md`,
`star-factorization-on-boundary-curve.md`,
`star-weierstrass-denominators-positive.md`.
