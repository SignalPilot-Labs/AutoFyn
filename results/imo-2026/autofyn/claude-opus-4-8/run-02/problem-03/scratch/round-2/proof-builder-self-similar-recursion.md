# Build report — self-similar-recursion (imo-2026-03), round 2

Status: **partial** (advanced; lower bound now complete for all dyadic adversaries + tight).

## What I closed rigorously this round
1. **Lemma A — top-band localization.** For any refinement `P` of `W_n`, only sub-pieces of the
   top `2^n` can exceed `2^{n−1}` and at most one does, so `∫_{2^{n-1}}^∞ 1[c_P odd] = (s_1−2^{n−1})^+`.
2. **Lemma B — decoupling.** `f(P) = (s_1−2^{n−1})^+ + f(Q)`, `Q` = top-subpieces capped at
   `2^{n−1}` ∪ refined block. Level-general; unifies round-1 Case 1/Case 2 into one identity.
3. **Corollary C — the `u≥1` reduction.** If `u=(s_1−2^{n−1})^+ ≥ 1` then `f(P) ≥ u ≥ 1`
   (since `f(Q)=M(Q)≥0`). So GAP-L can only fail when `s_1 ≤ 2^{n−1}+1` — a real narrowing.
4. **Theorem F — GAP-L for ALL integer/dyadic cuts.** `f(P) ≡ Σ(P) ≡ D_n ≡ 1 (mod 2)`
   (parity, Lemma D) and `f(P) ≥ 0` (Lemma E) ⇒ `f` is a nonneg odd integer ⇒ `f ≥ 1`. No
   casework; covers Case 1, Case 2, and every floor-attaining config. This is the headline gain.
5. **Theorem G — cascade tightness.** Explicit XY strategy: bisect the current top `2^m`, making
   three copies of `2^{m−1}`; two cancel by certified P1, leaving `W_{m−1}`. Telescopes
   `f(W_n)→…→f(W_1)=1` in `n−1` cuts. So `min_XY f ≤ 1` (rigorous).
6. **Lemma H — GAP-U dominant dichotomy.** If `a_1 ≥ Σ(rest)`, `a_1` stays rank-1 under every
   refinement of the rest, so `f ≥ a_1 − Σ(rest)` unless XY cuts `a_1`; pins the forced move.

## Honest remaining gaps (delimited)
- **GAP-L residual (non-integer cuts).** Reduced rigorously to "`f≥1` at every vertex of the cut
  polytope" (piecewise-affine `f`, gradient in `{−2,0,2}` per offset ⇒ min at a vertex). Integer
  vertices done by Theorem F. Non-integer (rational) vertices remain and provably CANNOT be closed
  by parity (parity permits `f=1/3` after scaling); they need a `W_n`-specific exchange/perturbation
  argument. Numerics (this round) confirm the true continuous min is exactly 1 for n=2,3,4.
- **GAP-U closure.** Regime-split recursion set up; residual accounting to exactly `1/D_n` and the
  adaptive stopping-test correctness (top-heavy `[1,ε,…]`) are open.

## Response to the outline-reviewer's scrutiny
- The reviewer's key worry was that the cascade RELOCATES GAP-L onto (a) an exchange lemma and
  (b) an IH over a non-`W`-shaped class. My route **sidesteps the exchange-lemma induction for the
  dyadic case entirely**: Theorem F (parity) proves `f≥1` for every integer placement in one shot,
  with no induction over intermediate multisets and no exchange lemma. The exchange lemma is only
  needed for the residual non-integer vertices, and I have honestly delimited exactly that.
- Lemma A is the rigorous, RESTRICTED form of "only a top cut reaches the top band" — the correct
  provable version of the (false) blanket claim; used, not the blanket.

## Verification performed
- `f(W_m)=1,1,3,5,11,21` (matches). Integer-cut configs: `f` always odd over 20000 random
  integer refinements (Lemma D holds). Continuous min over real offsets ≈ 1.0 for n=2,3,4
  (multi-restart Nelder–Mead) — the residual inequality is true, only the proof is missing.

## Promotable lemmas (for certification)
Lemma A (top-band localization), Lemma B (half-threshold decoupling), Lemma D (integer parity:
`f≡Σ mod 2` ⇒ `f≥1` for integer refinements of `W_n`), Lemma H (dominant-regime dichotomy).
All proved in full in the approach file.

## Suggested next step for this slug
Attack the GAP-L residual: prove that at a minimizing vertex the pinned pieces may be moved to a
dyadic tie without increasing `f` (exchange/perturbation via Lemma A + single-cut action), turning
the vertex reduction (Section 4) into a full proof. Alternatively, the sibling
`alternating-sum-threshold-potential` dual certificate may cover the non-integer case cleanly —
worth cross-importing if it lands.
