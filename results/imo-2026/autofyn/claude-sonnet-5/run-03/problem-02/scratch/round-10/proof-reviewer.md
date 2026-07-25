# Round 10 proof-reviewer adjudication — imo-2026-02

Reviewed both round-10 builds independently from scratch (own sympy/mpmath/numpy
sessions), per CLAUDE.md's rigor rules. Neither approach reaches `solved`;
both make real, verified progress. Both verdicts: **CHANGES REQUESTED**.

## 1. `coordinate-bash-resultant-boundary` — CHANGES REQUESTED (Status: partial)

Round-10 claims reviewed:

- **Steps 1-3 (P≤0 branch and E≥0 branch of Case (b), each closed
  unconditionally).** These are elementary algebra (no computer algebra
  needed). I independently re-derived every step by hand from the raw
  definitions: `expr1 = K + sinA sinB x > 0` (strict, sum of a strictly
  positive and a nonnegative term); if `P≤0`, `G = expr1 - Py ≥ expr1 > 0`
  trivially. The squaring-is-an-iff argument (both sides of `expr1 ≥ Py`
  nonnegative when `P>0`) is correct; expanding `D = expr1² - P²(1-x²)`
  gives exactly the displayed `Ac x² + Bc x + Cc`. `D'(x) = 2Ac x + Bc ≥ Bc
  > 0` for `x≥0`, so `D` is monotone increasing, giving `D(√X0) = E + Bc√X0`.
  If `E≥0`, `D≥0` trivially since `Bc>0`. All matches the file exactly, no
  gap. **Certified as `lemmas/case-b-p-le-0-and-e-ge-0-closed.md`.**

- **The `T`-factorization identity (the round's load-bearing new
  computational claim).** `T = c(dQ1(σ,τ) - cR0(σ,τ)) / (4sin²(A+B))`,
  where `q1, r0` are explicit degree-(4,3) polynomials. I independently
  built `T` from its raw definition (`Bc² X0 - E²`, itself built from `K,
  P, X0` as raw trig functions of `A,B` — not from any of the file's
  displayed intermediate forms) and compared to the claimed closed form.
  `sympy.simplify` of the difference did not collapse to an obviously-zero
  closed form (the expression is large and trig-heavy), so I instead did a
  high-precision numeric check: `mpmath`, 30-digit precision, 20
  independently-chosen random `(A,B)` pairs spanning the domain. **Relative
  error was <10⁻¹⁵ (often matching to >25 decimal digits) at every sample**
  — decisive evidence of an exact algebraic identity, not a numeric
  coincidence, for a polynomial identity of this degree. I also
  independently re-sampled the sign distributions of `q1, r0` over
  `(σ,τ)∈(0,1)²` (own 200,000-sample sweep, different seed): `q1>0` in
  ≈25.4% of samples (file: ≈25.6%), `r0>0` in ≈54.8% (file: ≈54.8%) — both
  match closely, confirming neither has a fixed sign, as claimed.
  **Certified as `lemmas/case-b-e-lt-0-t-factorization.md`** (as a genuine,
  verified structural reduction — it does NOT itself close the sign of `T`,
  and is not certified as doing so).

- **Overclaim check.** The file explicitly and correctly states Status
  `partial` and that the `E<0` branch is "NOT closed this round." No
  overclaiming found — this is an honest, precise gap disclosure.

- **Round-9 slip re-check.** Re-verified that `f'(β) = sin(A+β)cosB +
  sin(A+B-β)` (reused verbatim by this round's work) still holds exactly
  (fresh `sympy` session, zero residual) — round 9's certified `C2`
  constant-term cosmetic slip was in an unrelated part of the file, not
  touched this round, and had no bearing on the round-10 additions.

**Verdict: CHANGES REQUESTED.** True Status: `partial`. Exact remaining
gap: the sign of `4dst·q1(σ,τ) + c·r0(σ,τ)` on the residual `P>0∧E<0`
sub-case of Case (b) (≈4.5% of the corrected domain).

## 2. `coordinate-bash-resultant-boundary-pointwise` — CHANGES REQUESTED (Status: partial)

Round-10 claims reviewed:

- **Steps 1-4 (the MVT/Lipschitz reduction chain to `(⋆)`).** This is
  elementary calculus, and I independently re-derived every step by hand:
  Step 1's Lipschitz bound `f'(t) ≤ 1+cosB` (trivial, `sin ≤ 1`, `cosB>0`);
  Step 2's MVT bound `f(β1)-f(β0) ≤ (1+cosB)(β1-β0)` (direct integration of
  the Step-1 bound, valid since `β1>β0`); Step 3's second MVT bound
  `β1-β0 ≤ (cosβ0-cosβ1)/sinβ0` (from `sin` increasing on
  `[β0,β1]⊂(0,π/2)`, correctly used to bound `cosβ0-cosβ1` from below);
  Step 4's combination and the trivial-vs-square case split on
  `sign(RHS)`, ending in `(1+cosB)²X0 ≥ RHS²`. Every algebraic step matches
  the file exactly, no gap, and this reduction is explicitly presented as
  "suffices" (a one-directional sufficient reduction), not overclaimed as
  an equivalence — correct framing.

- **`f'`'s closed form** was independently re-verified symbolically
  (`sympy`, zero residual) — same identity used (correctly, unmodified) by
  the sibling approach.

- **Numeric corroboration (own from-scratch checks, not re-running the
  file's script).** Own 2,000,000-sample sweep over the true Case-(b)
  domain: 0 violations of `G(β1)≥0` (min ≈0.003) and, among samples with
  `RHS>0`, 0 violations of `(⋆)` (min ≈0.005) — both minima located near
  `(A,B)≈(0.407,0.914)`, matching the file's own reported global-
  optimization corner `(0.4064,0.9117)` closely, independently confirming
  the same degenerate-corner structure the file reports (not just a
  coincidence of one run).

- **Negative finding reproduced.** Independently confirmed the crude
  domain-width bound `G(β0) ≥ (1+cosB)(γ-β0)` is false: own sampling found
  a violation ≈-0.077 near `(A,B)≈(0.48,1.12)`, matching the file's
  reported witness and magnitude closely.

- **"Step 0" self-correction reproduced.** Independently confirmed
  `G(β0)>0` is false on a substantial fraction of the FULL `(A,B)` domain
  (own sampling: ≈11.5% negative, vs. the file's ≈23% — same qualitative
  finding; the differing exact percentage reflects a different sampling
  distribution and is not load-bearing for the proof) but has 0 violations
  restricted to the genuine Case-(b) domain (own 1,000,000-sample sweep) —
  confirming the file's honest correction of the outline dispatch's false
  premise is genuine, not a cover story, and that the final reduction
  correctly does not depend on `G(β0)>0` as an independently-required
  lemma.

- **Overclaim check.** The file explicitly states `(⋆)` is "NOT closed
  symbolically this round," backed only by numerics (including global
  optimization, honestly distinguished from random sampling but still
  disclosed as not a proof). No overclaiming found.

**Verdict: CHANGES REQUESTED.** True Status: `partial`. Exact remaining
gap: `(1+cosB)²X0 ≥ RHS²` (`⋆`), a single radical-free trig inequality in
`A,B`, over the WHOLE of Case (b) (not just a sub-case).

## Cross-pollination check (as directed)

The two new gaps do not accidentally close each other, and neither is
closed by the other's already-certified facts. `coordinate-bash-resultant-
boundary`'s residual target (`T≥0`, ⟺ sign of `4dst·q1+c·r0`) is scoped to
the narrow `P>0∧E<0` sub-case (≈4.5% of Case (b)). `coordinate-bash-
resultant-boundary-pointwise`'s `(⋆)` is scoped to the ENTIRE Case-(b)
domain via a different (lossier but simpler, one-squaring vs. two-squaring)
reduction. Neither is proved, so nothing closes yet — but it is worth
recording structurally: **`(⋆)`, if proved, would automatically imply
`G(β1)≥0` throughout all of Case (b), which strictly subsumes the narrower
`T≥0` sub-case** — so closing `(⋆)` alone would finish the whole
branch-selection gap (and hence the whole problem, via round 8's proven
structural-equivalence theorem across all live routes) without needing
`T≥0`'s factorization at all. The converse does not hold. This changes no
Status this round but should guide next round's prioritization toward
`(⋆)` as the single highest-value remaining target.

## Lemmas certified this round

- `lemmas/case-b-p-le-0-and-e-ge-0-closed.md` (from
  `coordinate-bash-resultant-boundary`, Steps 1-3) — certified, no gap,
  hand-verified elementary algebra.
- `lemmas/case-b-e-lt-0-t-factorization.md` (from
  `coordinate-bash-resultant-boundary`, the T-factorization) — certified as
  a genuine, numerically-decisive (<1e-15 relative error, 30-digit
  precision) verified reduction; explicitly NOT certified as closing the
  sign of T.
- `lemmas/mvt-lipschitz-reduction-case-b.md` (from
  `coordinate-bash-resultant-boundary-pointwise`, Steps 1-4) — certified,
  no gap, hand-verified elementary calculus; explicitly NOT certified as
  closing `(⋆)`.

## current.md

Updated `results/imo-2026-02/current.md` with a new "Round 10" entry at the
top of `## Approaches tried` (preserving all prior rounds' entries
unchanged below it, per the file's existing format). `## Status` remains
`partial` (no `## Full proof` section — not solved).

## Ranking

`record_outcome` called for both slugs, round 10, outcome `advanced` (both
made real, independently-verified, gap-narrowing progress; neither reached
solved or dead-ended).

## Verdicts

- `coordinate-bash-resultant-boundary`: **CHANGES REQUESTED** (Status:
  `partial`). Gap: sign of `4dst·q1(σ,τ) + c·r0(σ,τ)` on the residual
  `P>0∧E<0` sub-case (~4.5% of Case (b)).
- `coordinate-bash-resultant-boundary-pointwise`: **CHANGES REQUESTED**
  (Status: `partial`). Gap: `(1+cosB)²X0 ≥ RHS²` (`⋆`) over the whole of
  Case (b) — the recommended priority target for next round, since it is
  strictly more general than the sibling's residual gap.
