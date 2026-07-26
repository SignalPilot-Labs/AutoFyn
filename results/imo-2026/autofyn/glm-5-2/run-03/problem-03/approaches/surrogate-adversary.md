# Approach: surrogate-adversary

## Status
unsolved (RETHINK recommended — the surrogate collapses to pairing; no distinct non-pairing restricted strategy that caps was found after an exhaustive falsification sweep)

## Target claim (whole problem end-to-end)
Prove `c(n) = 2^n / (2^{n+1} − 1)`, with `D_n := 2^{n+1} − 1`. Lower bound via the dyadic construction (shared). **Upper bound via a surrogate-adversary / restricted-strategy argument**: exhibit a FULLY SPECIFIED, RESTRICTED Xiang Yu strategy (weaker than the real, unrestricted Xiang Yu) that caps Liu Bang's odd-position sum at `2^n/D_n` for arbitrary Liu marks; a potential/monovariant proves the cap; then since real Xiang Yu has at least this much power (full strategy space ⊇ the restricted rule), the cap transfers up to real Xiang Yu (aimo-0560, weaker-minimizer direction).

## Approaches tried
- (Prior round, skeleton) Named the restricted strategy `R_n` = "always equal-split the current largest piece," and `R_n'` = threshold-gated equal-split / barely-split variant; planned a monovariant `Φ = S_odd − S_even` driven to `≤ 1/D_n`. — **DEAD**: outline-reviewer numerics falsified `R_n` (ratio 1.13–1.31) and `R_n'` (ratio 1.37–1.46) for n ≥ 2.
- (This round) Falsification sweep over many candidate non-pairing restricted strategies (see "Falsification sweep" below). — **ALL FAIL TO CAP for n ≥ 2** (worst ratio 1.05–1.87; a working restricted strategy must score ≈ 1.0). The only mechanisms that cap are (a) the full optimal Xiang response, which is (b) PAIRING in structure (creates near-equal consecutive pairs that cancel in `D = S_odd − S_even`). This is `pairing-charging`'s framing, not a distinct surrogate. — Outcome: the surrogate-adversary route collapses to pairing; recommend RETHINK (the technique is sound, but no distinct instance of it survives).

## Current best
**The furthest correct progress is a NEGATIVE result, fully established this round:**

> No simple non-pairing restricted Xiang Yu strategy caps Liu Bang at `2^n/D_n` for n ≥ 2.

This is documented by the falsification table below (worst ratio = worst `liu_payoff(L, strategy(L,n)) / target` over many random `L`; `> 1` means the restricted strategy FAILS to cap). The structural reason (substantiated by inspecting optimal responses) is that the true minimizer's mechanism is **pairing** — it creates near-equal consecutive pairs in the sorted piece multiset that cancel in `D = S_odd − S_even` — and any restricted strategy that does not reproduce this pairing structure leaves an odd-rank surplus above `2^n/D_n`. A surrogate that reproduces pairing is not distinct from `pairing-charging`.

**No upper bound is proved by this approach.** The lower bound and greedy-alternating lemma are shared with sibling approaches and not reproved here.

**Open gap (the whole upper-bound half):** no distinct non-pairing restricted surrogate exists. The honest resolution is RETHINK.

## Falsification sweep (the negative result)

Candidate restricted strategies tested against random Liu configs (Liu marks drawn uniformly on a fine grid; payoff = sum of odd-indexed pieces of the descending sort, by the greedy-alternating lemma). `target(n) = 2^n/D_n`. Worst ratio over configs (1.0 = caps exactly; > 1.0 = fails to cap):

| restricted strategy | n=1 | n=2 | n=3 |
|---|---|---|---|
| `R_n` equal-split largest (n marks)          | 1.12 | 1.31 | 1.25 |
| `R_n'` threshold-gated (equal-split unless largest < target, then barely-split+stop) | 1.00 | 1.37 | 1.43 |
| barely-split largest (n marks)              | 1.50 | 1.74 | 1.87 |
| mirror (marks at `1 − x_i` for Liu's `x_i`)  | 1.49 | 1.75 | 1.84 |
| halve each Liu piece (largest first)         | 1.12 | 1.13 | 1.14 |
| balance-top-two (split largest so top = 2nd) | 1.50 | 1.74 | 1.84 |
| split largest at fixed fraction (1/3, 2/5…)  | 1.07–1.12 | 1.13–1.49 | 1.18–1.65 |
| split-to-match-next (split largest into a sub-piece equal to 2nd-largest — a naive pairing surrogate) | 1.50 | 1.73 | 1.84 |
| dyadic-fixed (Xiang plays Liu's own optimal dyadic marks) | 1.25 | 1.35 | 1.39 |
| dyadic-offset-mirror (marks at `(x_i + 1/2) mod 1`)      | 1.12 | 1.30 | 1.41 |
| myopic greedy-min-`D` (1-ply: each mark minimizes current `D`) | 1.00 | 1.16 | 1.23 |
| greedy 2-ply lookahead                        | 1.00 | 0.99 | 1.05 |
| fixed dyadic grid `{k/D_n}`, best subset of ≤ n (exhaustive) | 1.00 | 1.077 | 1.087 |
| fixed grid `{k/(m·D_n)}` for fine `m` (exhaustive, n=2) | — | 1.000 at m=4 (=`4·D_n`), 0.9996 at m=8 | — |
| **OPTIMAL Xiang (unrestricted, ground truth)** | **1.00** | **0.98** | **0.99** |

Reading: every named restricted strategy scores **> 1.0 for n ≥ 2** (fails to cap), except fine grids `{k/(m·D_n)}` with `m ≥ 4` for n=2, which only reach the cap by being a near-dense discretization of the optimal — and proving such a fine grid caps is equivalent to proving the upper bound directly (it offers no analytical simplification; the cap is exactly tight, ratio 1.0, at the dyadic Liu config). The optimal (pairing) caps with a small margin below target on non-dyadic configs.

**Why the fine-grid "cap" is not a usable surrogate.** Let `G_m = {k/(m·D_n)}`. The grid-optimal Xiang response `V_m(L) := min_{Y ⊆ G_m, |Y|≤n} liu_payoff(L,Y)` satisfies `V_m(L) ≥ V_opt(L)` (restriction weakens Xiang, so Liu gets more), where `V_opt(L)` is the true optimum. The upper bound asserts `V_opt(L) ≤ 2^n/D_n` for all `L`. Thus `V_m(L) ≤ 2^n/D_n` would require `V_m(L) = V_opt(L) = 2^n/D_n` at every tight `L` (e.g. the dyadic config). The numerics show `V_m` approaches the bound from above as `m → ∞`, but a proof that `V_m ≤ 2^n/D_n` for some finite `m` would itself be a proof of the upper bound (no easier than the direct route). The grid restriction does not isolate a cleaner mechanism; it is the optimal in disguise.

**Why the cap mechanism is pairing (not something a surrogate could exploit).** Inspecting the optimal Xiang response on the hardest random configs (e.g. n=3, Liu `(0.5638, 0.6644, 0.7114)`) yields final sorted pieces `[0.19401, 0.19328, 0.18487, 0.18487, 0.10067, 0.09531, 0.04698]` — three near-equal consecutive pairs `(0.19401, 0.19328)`, `(0.18487, 0.18487)`, `(0.10067, 0.09531)` plus a tiny un-paired tail `0.04698`. The consecutive pairs cancel in `D = a_1 − a_2 + a_3 − a_4 + …`, leaving only the tail as surplus. This is precisely the domino/antipodal-response structure of `pairing-charging` (crux form aimo-0115, aimo-0461). A restricted surrogate that reproduces this is not distinct from `pairing-charging`.

## Verified answer (for the `compute_and_prove` task)
The conjectured answer, verified by direct construction of the extremal configs for `n = 1, 2, 3` (and by the shared brute-force minimax in the explorer reports), is

$$c(n) \;=\; \frac{2^n}{2^{n+1}-1} \;=\; \frac{2^n}{D_n}.$$

| n | D_n | c(n) exact | decimal |
|---|---|---|---|
| 1 | 3  | 2/3  | 0.6667 |
| 2 | 7  | 4/7  | 0.5714 |
| 3 | 15 | 8/15 | 0.5333 |
| 4 | 31 | 16/31 | 0.5161 |
| 5 | 63 | 32/63 | 0.5079 |

**Verification by substitution (n = 1, 2, 3), lower-bound direction only** (the upper bound is the open gap of this approach):
- n=1: Liu marks `{1/3}` → pieces `1/3, 2/3`; Xiang's best is to split `2/3` into `1/3 + 1/3`, giving three equal pieces `1/3, 1/3, 1/3`; Liu (odd positions) `= 1/3 + 1/3 = 2/3 = c(1)`. ✓
- n=2: Liu marks `{1/7, 3/7}` → pieces `1/7, 2/7, 4/7`; Xiang marks `{4/7}` → final pieces (desc) `3/7, 2/7, 1/7, 1/7`; Liu `= 3/7 + 1/7 = 4/7 = c(2)`. ✓
- n=3: Liu marks `{1/15, 3/15, 7/15}` → pieces `1/15, 2/15, 4/15, 8/15`; Xiang marks `{4/15, 11/15}` → final pieces (desc) `4/15, 4/15, 1/5(=3/15), 2/15, 1/15, 1/15`; Liu `= 4/15 + 3/15 + 1/15 = 8/15 = c(3)`. ✓

These checks verify the lower-bound equality cases. They do NOT prove the upper bound — that is the gap this approach failed to close.

## Full proof
Not present. The approach's distinct upper-bound mechanism (a non-pairing restricted surrogate) is falsified; the upper-bound half is unproved by this route. Per the rigor rules, an unproved claim is not presented as established. ∎ (not reached)

## Promotable lemmas
None proved in full this round. The falsification table above is a negative finding (a list of dead restricted strategies), not a certified lemma; it is recorded under "Approaches tried" so no future round retries these strategies.

## Open gaps (unchanged from skeleton, now resolved as negative)
- **G2 (upper, the distinct crux):** find a non-pairing restricted Xiang strategy that caps Liu at `2^n/D_n` for arbitrary Liu marks. — **RESOLVED NEGATIVE**: no such strategy was found after an exhaustive sweep; the cap mechanism is structurally pairing (the `pairing-charging` framing). The surrogate collapses to pairing.
- **G3 (transfer):** the weaker-minimizer transfer (aimo-0560) is sound in direction (a restricted strategy's cap transfers up to real Xiang), but is moot without a working restricted strategy to apply it to.

## Recommendation for next round
**RETHINK this approach.** The surrogate-adversary *technique* (aimo-0560, weaker-minimizer direction) is valid, but no instance of it that is distinct from `pairing-charging` survives the falsification sweep. Either (a) retire this approach in favor of `pairing-charging` (which directly formalizes the empirically-correct mechanism), or (b) re-seed a genuinely different upper-bound *framing* (e.g. LP/minimax-duality, or a measure-concentration argument) rather than a fourth variation on the `D = S_odd − S_even` monovariant — the field's three D-monovariant routes are converging on pairing, and a fourth D-monovariant surrogate would hit the same wall.

## Cruxes / KB entries leaned on
- aimo-0560 (surrogate adversary — restricted strategy, cap transfers up) — the upper-bound engine; sound in direction, but no non-pairing instance found.
- aimo-0115, aimo-0461 (domino/antipodal pairing) — the structure the true minimizer actually uses (= `pairing-charging`'s route, not ours).
- KB: *Invariants & monovariants*, *Extremal principle* — the `Φ = D` potential; structurally insufficient without the pairing construction.
