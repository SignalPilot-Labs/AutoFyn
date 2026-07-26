# Round-4 proof-builder report — minimax-strategy-family

## 1. M2 XOR bug — FIXED and file internally consistent? YES.

**The bug:** §3.1's derivation of M2's D-value wrote `h=1` (meaning `𝟙_{[0,p_3)}`) on `[p_3, p_2)`, but `𝟙_{[0,p_3)}(t) = 0` for `t ≥ p_3`, so `f' = f ⊕ 0 = 0` there (not `1`). The derived integral was `p_1 − p_3` (WRONG); the actual M2 D-value is `p_1 − p_2`.

**The fix:** corrected the XOR row to `f=0, 𝟙_{[0,p_3)}=0, f'=0⊕0=0`, giving `∫ f' = p_1 − p_2`. The two tiny barely-split toggles (`B=[0,ε)⊂[0,p_3)` where `f'=0`, contrib `+ε`; `C=[p_1−ε,p_1)⊂[p_2,p_1)` where `f'=1`, contrib `−ε`) still cancel, so `D = p_1 − p_2` exact (for `ε < p_1 − p_2`). Sort-verified: the M2 multiset `{p_1−ε, ε, p_3/2, p_3/2, p_2}` gives `j(t) = 5,4,2,1,0` hence `D = ε + (p_1−ε−p_2) = p_1−p_2` exactly — max error 0 over 2000 configs (both full and ε→0 limit multisets).

**Reconciliation of all three locations:**
- §3.1 derivation: RE-DERIVED correctly → `D = p_1 − p_2`.
- §3 "menu statement" (the Promotable lemmas entry for the n=2 menu): corrected from `p_1 − p_3` → `p_1 − p_2`.
- §3.2 theorem statement + §3.3 dyadic table: ALREADY used `p_1 − p_2` (no change needed — they were the "correct" locations).

The §3.2 contradiction proof used `p_1 − p_2` (M2's corrected value) in step 3 all along — so the n=2 theorem was never actually wrong, only the §3.1 derivation of one member. **The n=2 upper bound stands, now internally consistent.** Re-verified: 0/30000 configs exceed 1/7 over the full 5-member menu.

## 2. G2-flat n≥3 — VERIFIED adaptive family for n=3? NO. Falsification results:

Ran the falsification sweep the outline-reviewer demanded BEFORE attempting a proof (all `fractions`-exact, sort-computed):

| Candidate family (n=3, target D ≤ 1/15) | Result |
|---|---|
| Naive (n−1)-mark chain `{p_4, |2p_1−1|}` | **4938/20000 flat configs exceed** (worst 0.138). INSUFFICIENT — confirms the single-gap-trap flag. |
| Full-peeling reachable finals + p_4 + |2p_1−1| | **4938/20000 exceed**. INSUFFICIENT. |
| 8-member clean family (p_4, p_3−p_4, p_2−p_4, p_1−p_4, |2p_1−1|, 3 peel-complements) | **4292/30000 exceed** (worst 0.138). INSUFFICIENT. |
| **Enriched 14-member clean family** (6 pairwise diffs + p_4 + |2p_1−1| + 6 peel-complements) | **204/30000 exceed (0.68%)**, worst 0.0876. CLOSE but INSUFFICIENT. |
| Rich fixed-fraction family (splits at {1/2,1/3,2/3,1/4,3/4,1/5,4/5,1/6,5/6}+BS+peel) | **0 fails / 879 flat configs. CAPS** — but via continuously-tuned splits. |

**Clean D-value formulas derived (regime-independent, verified 800/800 sort-match):**
- "EH two pieces `{p_i, p_j}`" → `D = p_a − p_b` (complement); all 6 pairwise diffs realizable (verified 6×2000 error 0).
- "EH p_1,p_2 + BS p_3" → `p_3 − p_4`.
- "BS p_1 + EH p_2,p_3" → `p_1 − p_4`.
- "peel p_1vp_2, peel p_3vp_4, peel remainders" → `|2(p_1+p_4)−1|` (and 2 analogs).

**Continuous optimum** on the hardest config `(0.397, 0.303, 0.184, 0.117)` is `D ≈ 0.017 ≪ 1/15`, attained by splitting p_1 at 0.488, p_2 at 0.390, p_4 barely — NOT a clean fraction. This confirms `c(3) = 8/15` is achievable but via continuously-tuned split points.

**No contradiction proof** — the clean §3.2-style contradiction does NOT generalize to n=3. The n=2 success (5 clean members cap exactly) is a low-dimensional coincidence; for n≥3 the slack structure is richer and clean telescoping does not reach.

## 3. Named gap(s) remaining
- **G2-upper-n≥3 (OPEN):** no clean finite regime-independent family caps at `1/D_n` for n=3. The enriched 14-member family gets within 0.68% but the residual failures (near-dyadic-flatter configs) require non-clean-fraction splits.
- **G1 (lower bound, shared):** splits-inequality `D ≥ 1/D_n` for Liu's dyadic config under arbitrary Xiang splits, n ≥ 3 — pending sibling `dyadic-induction` certification into `lemmas/splits-inequality.md`.
- **Unique-worst-at-dyadic n≥3 (conjecture):** proved n=2 (§4); open n≥3.

## 4. Spec concerns (the adaptive-chain outline is fundamentally flawed?)
**Partially.** The outline's mechanism (adaptive n-mark split-to-match chain with regime-independent D-values + minimax contradiction generalizing §3.2) is NOT fundamentally flawed in the sense that a capping family EXISTS (the rich fixed-fraction family caps, 0/879) — but the "regime-independent + clean contradiction" HOPE does not materialize for n≥3:
- The naive (n−1)-mark chain leaves TWO lone pieces (the outline's watch-out was correct); the n=2 M5 one-lone structure does not transfer.
- Clean regime-independent formulas (pairwise diffs, peel-complements) get within 0.68% but do not cap; capping requires continuously-tuned split points whose D-values are NOT clean telescoping formulas, so no §3.2-style finite contradiction.
- **The minimax-over-FINITE-family framing may be fundamentally insufficient for n≥3.** Recommendation: if a richer clean finite family cannot close (path 1, diminishing returns observed), the approach should concede G2-upper-n≥3 to a continuous-framing sibling (collapse-theorem's flattening, or an LP-dual per-regime argument) and keep the n=2 milestone + the certified regime `p_{n+1} ≤ 1/D_n` (equal-halve-n-largest, all n). The n=2 upper bound and the promotable n=3 pairwise-diff / peel-complement realizations stand regardless.
