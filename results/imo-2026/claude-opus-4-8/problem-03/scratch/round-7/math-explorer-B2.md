# imo-2026-03 — B2 Terrain Report (Lens: upper-bound sub-case B2)

## Problem and context

**Answer:** c(n) = 2^n / (2^{n+1}−1) = 2^n/D (D = 2^{n+1}−1). Status: partial.

The Case-B hard regime: n+1 pieces a_1 ≥ … ≥ a_{n+1}, all > 1/D, all consecutive gaps > 1/D, sum = 1. Split on a_1:
- **B1-large** (a_1 > c(n)): XY halves a_1, active sum = 1-a_1 < (2^n-1)/D, giving IH(n). Closed through IH(4), with IH(q≥5) flat residual open.
- **B2** (a_1 ≤ c(n)): XY halving a_1 leaves active sum ≥ (2^n-1)/D — at or above the IH(n) boundary. This file maps the B2 terrain.

---

## Critical finding 1: Arithmetic error in approach file's B2 analysis

The approach file `upper-general-cascade.md` claims the double-cancel entry (cut a_1 at a_2 cancelling a_2, then cut the residual at a_3 cancelling a_3) "gives IH(n-1) provided a_2+a_3 > 2^{n-1}/D".

**This is WRONG.** After the double-cancel, n-1 active pieces remain with n-2 cuts. IH(n-1) requires sum < (2^{n-1}-1)/D. The correct condition is:

    1 - 2(a_2+a_3) < (2^{n-1}-1)/D
    ⟺ a_2+a_3 > (1 - (2^{n-1}-1)/D)/2 = (D - 2^{n-1}+1)/(2D)

With D = 2^{n+1}-1: (D-2^{n-1}+1)/(2D) = (2^{n+1}-2^{n-1})/(2D) = **3·2^{n-1}/(2D) = 3·2^{n-2}/D**.

The file computes "(1-(2^{n-1}-1)/D)/2 = 2^{n-1}/D" which is numerically wrong:
- n=3: correct threshold = 2/5 = 6/15; file's threshold = 4/15 (wrong)
- n=4: correct threshold = 12/31; file's threshold = 8/31 (wrong)
- n=5: correct threshold = 8/21 = 24/63; file's threshold = 16/63 (wrong)

The true double-cancel threshold is 3·2^{n-2}/D, which is **50% larger** than what the file states.

---

## Critical finding 2: The geometric config sits exactly at the true threshold

**Structural observation.** The geometric LB config a_k = 2^{n+1-k}/D has:
- a_1 = 2^n/D = c(n) (boundary of B2)
- a_2+a_3 = 2^{n-1}/D + 2^{n-2}/D = 3·2^{n-2}/D

This equals the correct double-cancel threshold exactly. Verified numerically for n=2,3,4,5:

| n | D | Geometric a_2+a_3 | True threshold | At boundary? |
|---|---|---|---|---|
| 2 | 7 | 3/7 | 3/7 | YES |
| 3 | 15 | 2/5 | 2/5 | YES |
| 4 | 31 | 12/31 | 12/31 | YES |
| 5 | 63 | 8/21 | 8/21 | YES |

After double-cancel on the geometric config, the active sum equals EXACTLY the IH(n-1) boundary (not strictly less):
- n=3: active sum = 1 - 2·(2/5) = 1/5 = (2^2-1)/15 = IH(2) boundary
- n=4: active sum = 1 - 2·(12/31) = 7/31 = IH(3) boundary

So the geometric config is the MARGINAL case where double-cancel gives a non-strict IH(n-1) instance (A = 1/D exactly achieved). For configs with a_2+a_3 > 3·2^{n-2}/D (strictly), double-cancel gives strict IH(n-1). For a_2+a_3 ≤ 3·2^{n-2}/D (the true residual), double-cancel leaves sum ≥ (2^{n-1}-1)/D, so IH(n-1) doesn't apply.

---

## Critical finding 3: Emptiness/nonemptiness of the true B2 residual by n

**True residual** = B2 hard-regime configs with a_2+a_3 ≤ 3·2^{n-2}/D (where double-cancel fails).

**LP analysis** (minimize a_2+a_3 in B2 hard regime at binding B2, i.e. a_1 = c(n)):
- With n+1 pieces, all gaps ≥ 1/D (excess ea, eg_1,…,eg_{n-1} ≥ 0):
  constraint: n·ea + (n-1)·eg_1 + … + 1·eg_{n-1} = (2^n-1)/D - n(n+1)/(2D)
  objective: min (2n-1)/D + 2·ea + 2·eg_1 + … + 2·eg_{n-2} + eg_{n-1}
- LP optimal (use all excess in ea, ratio n/2 is maximal): min(a_2+a_3) = (2n-1)/D + 2·rhs/n

Results:

| n | True threshold (3·2^{n-2}/D) | LP min(a_2+a_3) | True residual nonempty? |
|---|---|---|---|
| 2 | 3/7 ≈ 0.429 | 3/7 ≈ 0.429 | NO (min = threshold) |
| 3 | 2/5 = 0.400 | 17/45 ≈ 0.378 | YES |
| 4 | 12/31 ≈ 0.387 | 19/62 ≈ 0.306 | YES |
| 5 | 8/21 ≈ 0.381 | 11/45 ≈ 0.244 | YES |
| 6 | 48/127 ≈ 0.378 | 25/127 ≈ 0.197 | YES |

**The true B2 residual is EMPTY for n ≤ 2 and NONEMPTY for n ≥ 3.**

Why the approach file's smaller threshold (2^{n-1}/D) was not flagged: its stated residual (a_2+a_3 ≤ 2^{n-1}/D) is EMPTY for n ≤ 4 (LP infeasibility shown for n=3,4). The arithmetic error thus had no observable consequence for small n — the file's stated "B2 settled for n ≤ 2" is correct, but for the wrong reason (for n=2 the true residual is empty, so double-cancel works; for n≥3 the true residual is nonempty and the double-cancel proof is INCOMPLETE).

---

## Concrete hard-regime B2 true-residual examples

**n=3:** Config {47/90, 31/135, 43/270, 4/45} (exact fractions):
- a_1 = 47/90 ≤ 8/15 = c(3): B2 ✓
- All gaps = 19/270 ≈ 0.070 > 1/15 ≈ 0.067: hard regime ✓
- a_2+a_3 = 7/18 ≈ 0.389 < 2/5 = 0.400 = true threshold: in true residual ✓
- After double-cancel: active sum = 2/9 ≈ 0.222 > 1/5 = IH(2) boundary: double-cancel FAILS ✓

**n=5:** Config {32/63, 2/15, 73/630, 31/315, 17/210, 4/63} (exact fractions):
- a_1 = 32/63 = c(5): B2 boundary ✓
- All gaps = 11/630 > 1/63: hard regime ✓
- a_2+a_3 = 157/630 ≈ 0.249 < 8/21 ≈ 0.381 = true threshold: in true residual ✓
- After double-cancel: active sum = 158/315 ≈ 0.502 >> 5/21 = IH(4) boundary: double-cancel FAILS dramatically ✓

---

## Approach file's stated (wrong) residual: Relation to the true one

The approach file's stated residual (a_2+a_3 ≤ 2^{n-1}/D) is a STRICT SUBSET of the true residual (a_2+a_3 ≤ 3·2^{n-2}/D). As shown above:
- The stated residual is empty for n ≤ 4 (LP infeasibility: for n=4, the residual requires eg_4+2·eg_3+eg_2 ≤ -3/D < 0, impossible).
- The stated residual is nonempty for n ≥ 5 (concrete example found).
- The TRUE residual is nonempty for n ≥ 3.

So the run_state.md description "double-cancel entry works only when a_2+a_3 > 2^{n-1}/D; residual nonempty for n ≥ 5" is PARTIALLY INCORRECT. The true state:
- Double-cancel works iff a_2+a_3 > 3·2^{n-2}/D (correct threshold, larger than stated)
- The true B2 residual is already nonempty for n=3 and n=4
- B2 for n ≥ 3 is genuinely open (the approach file only claims B2 settled for n ≤ 2, which is correct)

---

## What the true B2 residual looks like structurally

Key constraints in the true B2 residual (a_2+a_3 ≤ 3·2^{n-2}/D, hard regime, B2):

1. **Lower pieces are heavy:** a_4+…+a_{n+1} = 1-a_1-(a_2+a_3) ≥ (2^n-1)/D - 3·2^{n-2}/D = (2^{n-1}-1)/D = IH(n-1) boundary. So the lower n-2 pieces carry AT LEAST the IH(n-1) sum.

2. **Upper-middle pieces are light:** a_2 < 3·2^{n-2}/D - a_3 < 3·2^{n-2}/D. Individual bounds: a_3 < 3·2^{n-3}/D (since a_2 > a_3+1/D > a_3, so 2·a_3 < 3·2^{n-2}/D means a_3 < 3·2^{n-3}/D).

3. **a_1 is bounded:** 1/D < a_1 ≤ 2^n/D. The dominant piece is NOT overwhelmingly large.

4. **The sum is at the hard-regime maximum:** sum = 1 = (2^{n+1}-1)/D is fixed. The hard regime with tight gaps means all the "available mass" is tightly constrained.

5. **After halving a_1:** n active pieces {a_2,…,a_{n+1}} with n-1 cuts, sum 1-a_1 ≥ (2^n-1)/D. These pieces all have gaps > 1/D (inherited from hard regime). So IH(n) doesn't apply (sum not strict), Reduction 2 doesn't apply (all gaps > 1/D).

---

## XY strategy candidates for B2 residual

**Double-cancel:** Works only when a_2+a_3 > 3·2^{n-2}/D. For the true residual (a_2+a_3 ≤ 3·2^{n-2}/D), it leaves active sum ≥ (2^{n-1}-1)/D, strictly ABOVE the IH(n-1) boundary. Does NOT give IH(n-1).

**Triple-cancel** (extend cascade to a_4): Cut a_1 at a_2, then at a_3, then at a_4. Active: n-2 pieces {a_1-a_2-a_3-a_4, a_5,…,a_{n+1}}, sum = 1-2(a_2+a_3+a_4). For IH(n-2): sum < (2^{n-2}-1)/D, i.e., a_2+a_3+a_4 > (1-(2^{n-2}-1)/D)/2 = (3·2^{n-2}+2)/D ≈ 3·2^{n-3}/D. In B2 residual, a_2+a_3+a_4 ≥ a_4 > (n-2)/D + a_2+a_3 > (n-2)/D. Whether triple-cancel works depends on whether a_2+a_3+a_4 hits the threshold — this is a sub-sub-case analysis that may give only partial coverage.

**Halve-a_1 then apply Lemma H:** After halving a_1 (1 cut), n active pieces with n-1 cuts. If the smallest of these (a_{n+1}) were ≤ 1/D, Lemma H would give O = 1/2 + a_{n+1}/2 ≤ c(n). But a_{n+1} > 1/D in the hard regime, so Lemma H doesn't directly apply. HOWEVER: one approach is to halve a_{n+1} (1 more cut) to create a_{n+1}/2 pair cancelling, then apply Lemma H to the remaining n-1 pieces. This uses 2 cuts (halve a_1 + halve a_{n+1}) and leaves n-1 pieces with n-2 cuts.

**IH4-flat analog for B2:** The IH4-flat lemma worked by exploiting that S-max(b_1,2b_2) ≥ 7/D gave b_2 < 4/D (a tight upper bound on b_2). In B2 residual, the condition a_2+a_3 ≤ 3·2^{n-2}/D gives a_2 < 3·2^{n-2}/D and a_3 < 3·2^{n-3}/D. These bounds might enable a "B2-flat" leaf argument with 3 specific cuts similar to IH4-flat, exploiting the bounded piece sizes. This is the most promising analog.

**Compactness / geometric extremality:** The approach file notes numeric evidence that A ≤ 1/D is achievable for all B2 tested configs (n=3), but the achieving strategies are adaptive. A global argument that the geometric config (at the threshold boundary) is the unique maximizer of min-A over B2 would close the whole case. The R3 graveyard warns that concavity-of-g fails, so a naive extremality argument is blocked.

---

## What is NOT covered and why

- The **double-cancel (as stated in the file)** covers: B2 with a_2+a_3 > 2^{n-1}/D. In this region the active sum after double-cancel < (2^n-1)/D, NOT < (2^{n-1}-1)/D. So even this is actually wrong — the file only proved entry into an IH(n) upper bound (or maybe IH with weaker bound), not IH(n-1). The proof needs re-examination.

- **Reduction 2** never applies in the hard regime (all gaps > 1/D by assumption). After double-cancel, gaps in the active multiset may be > 1/D or ≤ 1/D — worth checking case-by-case.

- **IH-reducible + IH4-flat** (certified): These apply to B1-large only (after XY halves a_1 with a_1 > c(n), giving active sum strictly inside the IH boundary). B2 (a_1 ≤ c(n)) doesn't reduce to these.

---

## Distinct openings for the outliner

1. **Fix the double-cancel entry theorem:** The correct threshold is 3·2^{n-2}/D, not 2^{n-1}/D. The approach file needs to either prove IH(n-1) using the correct threshold (valid when a_2+a_3 > 3·2^{n-2}/D) OR acknowledge the true residual (a_2+a_3 ≤ 3·2^{n-2}/D, nonempty for n ≥ 3) and separately handle it.

2. **B2-flat leaf argument:** In the true residual, a_2 < 3·2^{n-2}/D gives tight bounds on all pieces (the chain: a_3 < 3·2^{n-3}/D, a_4 < 3·2^{n-4}/D, etc.). This mirrors how IH4-flat exploited b_2 < 4/D. A B2-flat strategy using these bounds with n cuts on n+1 pieces may close it.

3. **Reduction-2 after partial cascade:** After halving a_1 and applying one double-cancel step, the active multiset {a_1-a_2-a_3, a_4,…,a_{n+1}} might have some pair with gap ≤ 1/D (since a_1-a_2-a_3 can be comparable to a_4). If so, Reduction 2 finishes it. Need to check for the true residual.

4. **Cascade from bottom:** Instead of starting with a_1, XY halves a_{n+1} first (removes the smallest piece, uses 1 cut), then applies B1-large or B2 analysis to the n-piece subproblem. This changes the active structure fundamentally.

---

## Candidate techniques from knowledge base

- **Extremal principle / compactness** (KB): For proving "geometric config maximizes min-A over B2," compactness + derivative analysis. Blocked by interior-valley issue (r3 graveyard), but might work with a restricted domain (just the true B2 residual has more structure).
- **LP / simplex bound**: The LP analysis above shows min(a_2+a_3) has a clean extremal structure (all excess in ea). This LP structure might underlie a proof of the B2-flat leaf.

---

## Prior progress on B2

- B2 for n ≤ 2 is settled in direct-constructive §7 (confirmed correct: true residual empty for n ≤ 2).
- B2 for n ≥ 3: OPEN. The approach file has an arithmetic error in the double-cancel threshold that masks the true extent of the residual for n=3,4. The true residual is genuinely open.
- Numeric evidence: min-A search finds A ≤ 1/D achievable for all B2 configs tested (n=3), so XY CAN achieve the bound. The achieving strategy is "adaptive" and not yet in closed form.

---

## Dead ends to avoid

- **IH+(m) dual-bound route:** REFUTED (r6, fixed-point obstruction). Do not retry.
- **Double-cancel as stated with threshold 2^{n-1}/D:** The arithmetic is wrong. The correct threshold is 3·2^{n-2}/D. The proof needs fixing.
- **Concavity-of-g extremality:** REFUTED (r3), blocked for the whole problem.

---

## Small-case / intuition notes

**Conjecture (evidence only):** For every B2 hard-regime config, XY achieves A ≤ 1/D. This is supported by numeric evidence at n=3 (approach file) but not yet proved.

**Key structural observation (verified):** The geometric config a_k = 2^{n+1-k}/D is EXACTLY at the double-cancel boundary (a_2+a_3 = 3·2^{n-2}/D) and after double-cancel has active sum = (2^{n-1}-1)/D = IH(n-1) boundary exactly. This suggests the geometric config is the "hardest" B2 case, and all other B2 configs are "easier." If true, a strategy that works for near-geometric configs would close B2.

**True B2 residual width (asymptotic):** As n grows, the gap between the LP min(a_2+a_3) ≈ (2n-1)/D + O(n/D²) and the true threshold 3·2^{n-2}/D grows exponentially. So the B2 residual becomes a LARGER fraction of the B2 territory as n increases — it's not a thin boundary layer.
