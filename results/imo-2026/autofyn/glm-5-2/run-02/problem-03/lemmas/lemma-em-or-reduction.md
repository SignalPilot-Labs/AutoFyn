# Lemma — the reduction `L(n+1) ⟺ e_M ≤ o_R`

**Status: CERTIFIED** (round 3, reviewer). Pure-algebra reformulation (no induction); spot-confirmed by the reviewer on 50k random real marks at level 3 (0 violations).

**Setup.** Level-`(n+1)` dyadic config. `M = 2^{n+1}/D(n+1)` is the single largest piece (`M > 1/2`), `R = (1, 2, …, 2^n)/D(n+1) = (D(n)/D(n+1))·(level-n dyadic)`, `total(R) = D(n)/D(n+1)`, `R_largest = 2^n/D(n+1) = M/2`. The load-bearing identity `M − total(R) = 1/D(n+1) = α(n+1)` is verified separately.

Xiang refines by `≤ n` marks (the correct budget for `c(n+1)`): `k` marks land in `M` (splitting it into `k+1` sub-pieces `m_1 ≥ … ≥ m_{k+1}`, `Σ m_i = M`), and `≤ n−k` marks refine `R` into `R'` (so every `R'`-piece `≤ R_largest = M/2`). Merge the `k+1` `M`-sub-pieces with the `R'`-pieces into the global sorted-desc list `p_1 ≥ p_2 ≥ …`.

**Definitions.** Partition the global list by origin:
- `e_M` = sum of `M`-sub-pieces at *global EVEN* ranks `2, 4, 6, …`.
- `o_M` = sum of `M`-sub-pieces at *global ODD* ranks `1, 3, 5, …`. (`e_M + o_M = M`.)
- `e_R` = sum of `R'`-pieces at global EVEN ranks.
- `o_R` = sum of `R'`-pieces at global ODD ranks. (`e_R + o_R = total(R') = total(R)`.)

By Lemma G, `oddsum(global) = o_M + o_R` (Liu's take) and `evensum(global) = e_M + e_R` (Xiang's take).

**Reduction (the lemma).** Lemma `L(n+1)` is `oddsum(global) ≥ M = f(n+1)` (the lower bound). Now `oddsum(global) = o_M + o_R = (M − e_M) + o_R`, so
```
oddsum(global) ≥ M   ⟺   M − e_M + o_R ≥ M   ⟺   e_M ≤ o_R.
```
Equivalently, `evensum(global) = e_M + e_R ≤ total(R) = e_R + o_R ⟺ e_M ≤ o_R`. **Lemma `L(n+1)` is EXACTLY the inequality `e_M ≤ o_R`** — the sum of `M`-sub-pieces landing at global even ranks is at most the sum of `R'`-pieces landing at global odd ranks. ∎

This is independent of `k`: no per-`k` classification, no WLOG-`k` exchange. The interleaving obstruction is localized to proving `e_M ≤ o_R` on the merged sort — a single clean inequality between two sub-sums.

**Open step (honest).** The reduction is a REFORMULATION, not a proof of `e_M ≤ o_R`. The inequality `e_M ≤ o_R` is verified by exact enumeration (`n = 2, 3` grid, 0 violations) and by 500k random real marks at level 3 (0 violations; reviewer spot-confirmed 50k), but NO analytic proof for general `n` over the reals is known. The self-compensation pairing lemma (`lemmas/lemma-self-compensation.md`) reduces `e_M ≤ o_R` further to a residual Hall-type matching; that residual is the live open handle.

**Scope.** Applies to any approach using the `M ⊎ R` self-similar decomposition — replace the per-`k` classification of `L(n+1)` with this single inequality.

**Knowledge-base tool.** Invariants & monovariants (the `M`-vs-`R` split linearizes the global alternating sum into two sub-alternating sums).

**Where proved.** `approaches/pairing-partner.md` (round 3, §"The reduction `L(n+1) ⟺ e_M ≤ o_R`").
