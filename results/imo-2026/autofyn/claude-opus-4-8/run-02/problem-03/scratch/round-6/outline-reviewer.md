# Outline review — round 6 — imo-2026-03

Context: whole problem is one gap from solved. UB certified; residual = LBL `f≥1` at the Φ-max
tied minimizer `P*`, sharpened to Gap A (forest/acyclicity of the multiplicity incidence multigraph)
+ Gap B (μ=3 even-block leaf). The two primal-integrality framings collapsed onto one wall (Gap A ≡
UPM-5). Plateau rule in force: at most ONE integrality-wall slug in the build set, plus ≥1 genuinely
different framing.

The outliner fielded exactly this shape: one integrality-wall representative (self-similar, advanced
with a new Gap-A weapon), one claimed-different framing (dual-integer-certificate), one different-genre
hedge (game-value). Verdicts below.

---

## self-similar-recursion — CHANGES REQUESTED (advance; the ONE integrality-wall slug — BUILD)

Sound spine: §0–§5 all certified (S-core `ker U=0`, M2/M3/M4, block formula `f=Σ_{μ odd}σ_{a_j}w_j`).
The two re-planned closures avoid every recorded dead end:
- **Gap A** attacked via full-cycle alternating block-sum ≠ 0 using distinct-power budgets
  (`2^{a_r} > Σ_{i<r} 2^{a_i}`, superincreasing) + rank-contiguity. This is NOT the refuted
  pure-kernel/linear-algebra closure (479-instance refutation) and NOT consecutive-ones/TU (refuted
  round 5). It correctly honours the round-5 rule that any closure MUST use the distinct-powers-of-two
  structure. Legitimate new mechanism — cannot pre-verify it closes, but it is not a recorded dead end.
- **Gap B** via a rank-tracked degenerate-Φ-dominator (Lemma BD), explicitly NOT the refuted uniform
  "bisect the leaf" one-liner and NOT the refuted V-kink `{v,v,v}→{v+s,v+s,v−2s}` move (which leaves
  the minimizer set). Good.

Issues to close while building (the open gaps, as flagged): (i) Gap A cycles that also touch off-cycle
pieces and multiplicity-≠1 cycle edges — the sign/extra-mass bookkeeping the S-core alone does not
exclude; (ii) Gap B general existence of the degenerate dominator staying in `G`. These are the honest
residual, not hidden. Build.

## dual-integer-certificate — APPROVE as the mandated different framing (NEW — BUILD)

**Assessment of the orchestrator's central question: does Gap D genuinely bypass Gap A AND Gap B, or
is it Gap A/UPM-5 in disguise? Verdict: it is a GENUINELY DIFFERENT, strictly-weaker object.**

I verified the logic and tested it numerically:
- The dual identity is exact and sound: `ker U=0` ⇒ rows of `U` span `ℝ^p` ⇒ `U^Tλ=s` is ℚ-solvable
  for every `s`; and for ANY such `λ`, `λ^Tb = λ^T(Uw) = (U^Tλ)^Tw = s^Tw = f`. Independent of the
  choice of `λ` because `b` is fixed. Confirmed on `{2,3,3}`: `U`, `s` built explicitly,
  `λ=(1,0,0,0)` solves `U^Tλ=s` and `λ·b = 1 = f`.
- **Why it is NOT Gap A in disguise.** Primal integrality (Gap A/forest) asks that the specific `w`
  solving `Uw=b` be integer — needs the incidence structure unimodular (det ±1). The dual asks only
  that the specific `s∈{−1,0,1}^p` lie in the integer row-lattice `U^Tℤ^{n+1}` — sufficient condition
  is gcd of the maximal (rank) minors of `U` = 1, which is **strictly weaker than det = ±1**. Concretely
  the round-5 obstruction `[[1,2],[2,1]]` has det = −3 (kills primal unimodularity), yet its dual is
  solvable for `s=(1,−1)` (λ=(−1,1)). So a chorded-even-cycle vertex that defeats Gap A need not defeat
  Gap D. This is a real, not cosmetic, gap between the two.
- **Why it bypasses Gap B.** At a μ=3 even leaf the block row `3λ_k + … = 0` leaves `λ_k` free rather
  than forcing a fraction, and the non-integer `w` continuum (round-4 refuter of primal Lemma W) still
  yields integer `f=λ·b` — I confirmed the non-integer `{a,2−a}` family is NOT S-core (`ker U≠0`,
  duplicated column), so it never reaches the dual step, consistent with S-core selection.
- Numerical spot-check (n=3, minimizer search): S-core near-minimizers tested had `U^Tλ=s`
  integer-solvable, 0 Gap-D failures; global min f = 1.000 re-confirmed.

Conclusion: dual-integer-certificate counts as the genuinely-different framing. It shares only the
certified `P*` prefix with self-similar; its wall (Gap D lattice condition) is a DIFFERENT wall from
Gap A. Fielding self-similar + dual does NOT violate the plateau rule.

**Two issues the builder MUST address (do not pass as "known"):**
1. **Positivity is NOT free.** `f∈ℤ` plus `f≥0` gives only `f≥0`. To reach `f≥1` the route needs
   `f≠0`. `f=0` (all blocks even) is exactly the certified surplus/bisect-all case — it is excluded
   only by the cut budget `b=n<m=n+1`, and proving that exclusion is itself part of the LBL. The
   outliner's Step 4 asserts "`f=m>0 ⇒ f≥1`" as if `f>0` were given; it is not. The builder must
   either (a) derive `λ_0` odd ⇒ `f=Σλ_k2^k` odd ⇒ `f≥1` (in `{2,3,3}`, `λ_0=1` odd — promising, but
   must be shown to hold generally from the bottom-block equation), or (b) supply an independent
   positivity argument tied to the cut budget. Flag this as a co-equal gap with Gap D, not an aside.
2. **Confirm Gap D on n≤4 exhaustively before over-committing** (outliner already mandates this). If
   some Φ-max S-core minimizer has `s` OUTSIDE `U^Tℤ^{n+1}`, that is the sharpened residual — still a
   NEW, non-Gap-A object; report it honestly, do not retreat to primal integrality.

Sole gap = Gap D (integer solvability), secondary gap = positivity `f≠0`. Technique sound and
genuinely diverse. Registered at cold-start; build.

## game-value-recursion — CHANGES REQUESTED (revise; keep live, NOT in build set)

The combinatorial-game genre is legitimate breadth, and harvesting Lemma R0 (`f(S)=a_1−f(S∖a_1)`) as
certified infra is cheap value. But the load-bearing BNF-involution is, by the outliner's own account,
HYPOTHETICAL — "no instantiation found this round," flagged exploratory, "value is genre-diversity,
not a likely close." That is a lemma named without a working mechanism (the obstruction: XY's cuts on
`T` and `R'` live at different scales than Liu Bang's marks, so no symmetric position is exhibited).
Not worth a builder slot this round against two stronger candidates. Keep the slug live in the
population; if either build slug stalls next round, revisit it (and opportunistically certify R0).

## Not fielded this round
block-recursion-tievertex (UPM-5 route refuted-adjacent, dominated), cut-budget-jacobsthal-recursion
(Jacobsthal driver refuted), majorization-smoothing (dormant) — all remain live in the population,
none built.

## Diversity check
Build set has one primal-integrality slug (self-similar: wall = Gap A forest/det±1) and one
strictly-weaker dual slug (dual: wall = Gap D lattice/gcd=1). Different walls — plateau rule satisfied.
The two are NOT variations of one framing at the crux. If BOTH stall next round, escalate to a
non-integrality-genre framing (game-value BNF, or cut-budget count-function profile Case B).

build set: self-similar-recursion, dual-integer-certificate
