# Build report — block-recursion-tievertex (round 4)

**Status: partial (CHANGES REQUESTED expected).** Committed to the INTEGRALITY route as
instructed; supplied the mechanism the reviewer demanded; one residual sub-case remains.

## What I did
Closed the cross-piece-tie residual DOWN TO a single crisp finite lemma, and proved everything
else in full:

1. **Reduction (fully proved):** the pure-cross-tie non-degenerate minimizer's values solve a
   square `0/1` system `Mv = (2^0,…,2^n)` (`(∗)`), with `t ≤ n+1` distinct values. No within-piece
   tie ⇒ `M` is genuinely `0/1` (this is why within vs cross matters — within-ties give entries `2`
   and non-integer vertices like `{4/3,4/3,4/3,2,1}`).
2. **Mechanism (the crux the reviewer asked for):** the vertex is integer because **`M` is
   unimodular (`det=±1`), equivalently `B(M)` has a UNIQUE perfect matching** ⇒ `v=M^{-1}d ∈ ℤ` ⇒
   Theorem F ⇒ `f ≥ 1`. This is NOT a bare numeric conjecture — it is a specific structural claim
   (Lemma UPM) with proof of: existence of a PM; `unique PM ⟺ det±1 ⟹ integer`; no equal columns
   (UPM-3); **no 2-regular even-cycle core** via the telescoping identity `Σ(-1)^i 2^{a_i}=0` being
   impossible for distinct exponents (UPM-4).
3. **Lemma BD** proved in full (one line: `σ_{a+j-1}=σ_a(-1)^{j-1}`).
4. **Within-piece-tie elimination** via BD simplex-vertex descent (shared prefix with self-similar;
   the divergence is the integrality finish).

## The residual gap (honest)
**Lemma UPM sub-case (UPM-5): chorded even cycles.** Positivity + distinct powers of two kill
2-regular cycles, but a cycle whose pieces carry EXTERNAL mass is not excluded by a local estimate.
Verified to never occur: **exhaustive** for n=2,3,4 (12/264/13800 pure-cross vertices, 0
non-integer, all `det=±1`, all unique PM — including 24+3120 that contain a chorded cycle yet keep
a unique matching); random n=5 (1781 vertices, all `det=±1`). Also confirmed integrality holds even
for *generic* increasing integer RHS (so it is pure unimodularity, not a powers-of-2 accident).

## Why this is a real hedge (not a redundant self-similar copy)
The wall is a **finite algebraic statement** (unimodularity of a feasible `0/1` system), closed for
forests and 2-regular cores — a genuinely DIFFERENT obstruction from self-similar-recursion's
infinite-descent **termination monovariant**. A proof of (UPM-5) closes the whole problem with no
no-cycle-of-moves argument. The routes do not share a wall.

## Spec concerns
- None on the target/reduction. The integrality reduction (`(∗)` + `det±1 ⇒ integer ⇒ F`) is fully
  rigorous and self-contained; it is worth certifying independently of UPM's residual.
- Lemma UPM is the clean next target for an explorer/builder: "a square `0/1` matrix admitting a
  strictly-positive solution with distinct positive-integer RHS is unimodular." Suggested levers:
  strengthen UPM-3 (distinct piece-sets) into a partial order on values that forbids augmenting
  cycles; or a global independence argument. This is far more tractable than a termination proof.

## Promotable lemmas
- **Lemma BD** (block-decomposition) — full proof; ready to certify.
- **Integrality reduction** (conditional on UPM) — reduction fully proved; certify the reduction.

## Verification artifacts
`/tmp/struct.py`, `/tmp/uni.py`, `/tmp/which.py`, `/tmp/n5.py`, `/tmp/cycle.py` (sympy/Fraction
exact arithmetic; det, perfect-matching counts, feasibility of cycles).
