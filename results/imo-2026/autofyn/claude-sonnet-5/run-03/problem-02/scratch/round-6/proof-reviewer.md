# Round 6 proof-reviewer report — imo-2026-02

Adjudicated three built approaches: `coordinate-bash-resultant-boundary`,
`coordinate-bash-resultant-boundary-pointwise` (new fork), `ptolemy-trig-identity`.
Every new load-bearing symbolic/numeric claim was rebuilt independently from
scratch (own `sympy`/`numpy` scripts, never reusing the builders' code —
including re-deriving `G_{2a}, G_{3a}, G_{2b}` directly from the raw vector
definitions rather than trusting the displayed polynomials).

## 1. `coordinate-bash-resultant-boundary` — verdict: CHANGES REQUESTED (Status: partial)

**§12 (magnitude bound) claim of "fully closed": VERIFIED CORRECT, no gap.**
Independently rebuilt every load-bearing piece from scratch:
- `A_2 = A_3 = 2(u^2+1)(cc(u^2-1)-2bu)` exactly (symbolic subtraction = 0).
- Lemma 12.1's `Ñ_1(t_1) = -a·cc/2·(1+u^2) + t_1·(-cc·u^2+(2b-a)u+cc)`: exact
  match via independent cross-product computation from `A=(0,0),B=(a,0),
  C=(b,cc)`, `M=(a/2,0)`.
- Lemma 12.2's resultant identity `Res_{t1}(G3a, Ñ1) = (a/4)·u·A3·[(a-2b)²+4cc²]·F1`:
  reproduced exactly via `sympy.resultant`, zero symbolic remainder.
- Lemma 12.3's `Ñ_2(s_2)` and its resultant identity `Res_{s2}(G2a,Ñ2) =
  4u·A2·[(2a-b)²+cc²]·F2`: reproduced exactly, zero remainder.
- The quadratic-vs-linear resultant-value formula `Res(f,g)=lc(f)·g(r1)g(r2)`
  used throughout: independently verified as a generic symbolic identity.
- Lemma 12.4 (root-pairing lemma): elementary IVT argument, checked by hand,
  no gap.
- The three trig sign facts `Q^ptrig>0, Q^trig>0, R^trig<0` throughout the
  valid range: independently verified both the exact Weierstrass-to-trig
  conversion formulas (symbolic, zero remainder) and the closed-form
  boundary values at `β=∠ABC,∠ACB` (matched numerically on 5 random
  triangles to machine precision). The "larger angle opposite larger side"
  case-split logic and the single-crossing sinusoid sub-lemma are both sound
  elementary arguments, no gap.
- Theorem 12.6's combination (Lemma 12.4 applied with the correct
  slope-sign data) is logically valid: I traced through which root gets
  selected on each side and confirmed the containment test and the
  already-certified cross-product sign test provably select the same root.

This is a genuinely complete, gap-free, all-triangle, all-`β` (within the
valid range) result. **Certified**: `lemmas/magnitude-bound-and-sign-coincidence.md`,
`lemmas/root-pairing-lemma.md`.

**§13 (G2b true/supplementary parity, and the `s_2>0` scoping correction):
VERIFIED CORRECT.** Independently re-derived `G_{2b}` from scratch (built
the full squared-cosine polynomial `(†)` for hypothesis 2 directly from the
vector definitions, divided by `t_1²`, factored) — matches the file's
`G_{2b}` and its leading coefficient `B_2` exactly. Independently re-derived
`D_K, D_N` (the dot-product numerators) exactly. Independently computed
`Res_{s2}(G2b, D_K·D_N) = -4u(b²+cc²)²(1+u²)⁶·F2·[2a(u²-1)²-b(u²+1)²]²`
exactly, confirming `W(r1)W(r2)≥0` always — this is a **proved theorem**
(not numerics), correctly refuting the "generically one true, one
supplementary" guess. The "physical constraint `s_2>0`" correction is
independently reproduced: my own fresh 17,832-sample sweep (different code,
different seed) found 7,410 counterexamples to the joint exclusion
conjecture without the `s_2>0`+true-root filter, and **0** counterexamples
with it — matching the builder's diagnosis almost exactly (they report
15,962/46,542 without the filter and 0/26,146 with it at larger scale). This
confirms the correction is genuine and correctly scoped, not a
post-hoc rationalization. **Certified**: `lemmas/g2b-true-supplementary-parity.md`.

The full three-way symbolic combination (positivity + true-root filter +
containment/sign, jointly on `G_{2b}`'s roots) remains honestly open — the
file does not claim otherwise. **Status `partial` is accurate.** No
overclaiming found; if anything the file is conservative (§12 could almost
be read as inviting a premature "solved" claim for the whole problem, but
the file correctly does not make that leap, since G2b exclusion is
separately still needed).

## 2. `coordinate-bash-resultant-boundary-pointwise` — verdict: CHANGES REQUESTED (Status: partial)

New fork this round (registered via `copy_approach`). Lemma P1/P2 (the exact
translation of hypothesis-2-and-containment-and-angle-test into four
explicit conditions on `s_2` alone, without needing the `G_{2a}/G_{2b}`
factorization) has a complete, elementary, gap-free proof — verified by
hand, no issue.

**The "552 numerical samples, 0 counterexamples" claim is honestly
disclosed as NOT a symbolic proof, and this disclosure is accurate — it is
neither secretly closer to solved nor secretly further from it.**
Independently re-implemented Lemma P1's four conditions entirely from
scratch (own Python/numpy script — built the degree-4 polynomial in `s_2`
directly from the affine vector definitions, extracted real roots via
`numpy.polynomial.polynomial.polyroots`, tested conditions (2)-(4) via
direct coordinate computation, no resultant shortcuts, no code or formulas
copied from the builder) and ran 277 independent random (triangle, `β`)
samples: **277/277 had exactly one surviving candidate**, closely
corroborating (at a similar scale, via an entirely independent codebase)
the builder's own 552-sample, 0-counterexample report. The builder's
diagnosis of *why* Theorem 11.8's resultant/Vieta technique does not
directly extend (three joint conditions on a quartic's roots, one of which —
the matched-sign test — is not itself a polynomial factor of the quartic)
is a sound, precise gap analysis, not hand-waving disguised as a proof.

**Certified**: `lemmas/pointwise-branch-selection-criterion.md` (Lemma
P1/P2 only — the uniqueness claim itself is explicitly NOT certified, as
the file itself states).

**Status `partial` is accurate.**

## 3. `ptolemy-trig-identity` — verdict: CHANGES REQUESTED (Status: partial)

**Step 1 (multiplicative resultant identity) and Step 2 (sign lemma):
VERIFIED CORRECT.** Independently re-derived Step 1's identity
`Res_U(q1,Φ) = P1²P2²·∏_{i,j}(F(Ui,Vj)-4)` using **fully generic** symbols
`P1,Q1,R1,P2,Q2,R2,sinA,cosA` (not the triangle-specific setup) — a
strictly stronger check than a numeric/specific-triangle verification,
since it confirms the identity as a general algebraic consequence of
resultant multiplicativity + the roots-product formula, with zero symbolic
remainder. (Note: caught and fixed a bug in my own first attempt at this
check — an unexpanded `L` expression silently dropped the `-cosA·V` term
from `m`; after `sp.expand`, the check passed cleanly. This is exactly the
kind of tooling pitfall flagged in prior rounds' memory — worth reiterating
below.) Independently verified Step 2's sign lemma both by hand (elementary
`tan`-monotonicity case split, sound, no gap) and numerically on 5 random
triangles (both inequalities held with correct sign in every case).
Confirmed Step 3's combination correctly uses the round-5-corrected
resultant prefactor (no leading `4`), consistent with the certified
`lemmas/ptolemy-resultant-elimination-to-sextic.md` — the stale "4×"
constant is only preserved in the file's historical round-5 section text,
not reused in round 6's own derivation, so there is no residual
inconsistency in the current argument.

**Confirmed the parity claim (Step 4) is genuinely still open, not secretly
closable with what's already proven.** Independently reproduced the
odd-parity pattern on 2000 random domain samples (own script, rebuilding
`P̃1,...,R̃2` from the certified closed forms independently) — **0
exceptions**. This is strong corroborating evidence but not a proof; no
argument in the file, or found by the reviewer in this review, establishes
*why* specifically the genuine-genuine branch combination is the one
exceeding 4. The file's own two proposed directions (a: bound `F(U,V)` when
`U` is the spurious root; b: per-branch continuity/IVT) are both honestly
flagged as unattempted, not falsely claimed as "almost done."

**Certified**: `lemmas/ptolemy-sextic-parity-reduction.md`.

**Status `partial` is accurate.**

## Population-level observation (for next round's outliner)

All three approaches have converged, in round 6, to structurally similar
remaining gaps: each is now "prove a sign/parity/uniqueness pattern holds
across all roots of a higher-degree polynomial," backed by large-scale,
independently-reproduced numerics (0 counterexamples in every case) but no
proof. The routes themselves remain genuinely different (continuity/IVT
vs. pointwise-quartic vs. Ptolemy-sextic), so this is not (yet) the
single-shared-gap trap CLAUDE.md warns about — but if round 7 fails to close
any of the three via further resultant/Vieta variations, it may indicate a
common underlying obstruction (deciding a sign pattern on all roots of a
quartic/sextic without a closed-form per-root argument), worth trying a
technique genuinely orthogonal to root-counting for at least one approach
(e.g. a synthetic/geometric argument, or Sturm sequences set up properly
after ideal-reduction rather than on raw un-reduced coefficients, which
Step 0 of `ptolemy-trig-identity` found intractable in raw form).

## `current.md` updates made
- Added a "Round 6 (this round) — proof-reviewer adjudication" entry under
  `## Approaches tried` documenting all three verdicts and independent
  verifications above.
- Added a "## Round 6 update" section (before `## Full proof`) summarizing
  the newly-closed magnitude bound and the three approaches' converged
  parity-type remaining gaps, updating the "what remains" list.
- Updated the `## Full proof` placeholder note to reflect the magnitude
  bound's closure.
- `## Status` remains `partial` (unchanged — no APPROVE this round).

## Lemmas certified this round
- `lemmas/magnitude-bound-and-sign-coincidence.md` (Theorem 12.6)
- `lemmas/root-pairing-lemma.md` (Lemma 12.4, general/reusable)
- `lemmas/g2b-true-supplementary-parity.md` (§13's proved theorem)
- `lemmas/pointwise-branch-selection-criterion.md` (Lemma P1/P2)
- `lemmas/ptolemy-sextic-parity-reduction.md` (Steps 1-3)

## Ranker outcomes recorded
- `coordinate-bash-resultant-boundary`: `advanced`
- `coordinate-bash-resultant-boundary-pointwise`: `partial`
- `ptolemy-trig-identity`: `advanced`
