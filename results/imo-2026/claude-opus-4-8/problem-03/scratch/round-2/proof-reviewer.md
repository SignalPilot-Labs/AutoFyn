# Proof review — imo-2026-03 (IMO 2026 P3), round 2

Two approaches reviewed. Both are honestly marked `partial` and share the same two load-bearing gaps.
Independent verification done via brute-force minimax and grid/random search (all bounded, see log).

## Independent verification performed
- **Lemma G (greedy = odd-index sum)**: brute-force minimax of the claiming game vs Σ_odd on 2000
  random multisets → **0 mismatches**. The lemma's algebra (S(L_j) ≥ S(L_1) via sorted pairing) is
  correct and the value it computes is confirmed.
- **Answer c(n) = 2^n/(2^{n+1}−1)**: full-game optimization. n=1 → 0.668 at a≈1/3 (= 2/3 ✓);
  n=2 → geometric config {1,2,4}/7 gives 0.5714 (= 4/7 ✓), no random config beats it. **Answer correct.**
- **Merge lemma, integral rep A = meas{N(x) odd}, bounds 0≤A≤p_1**: 20000 random trials → **0 violations**.
- **Lower bound true**: min val over random ≤n-cut refinements of the geometric config = 2^n exactly
  for n=1,2,3. Confirms the lower bound holds and the two Case-2 gaps are true-but-unproven.

## Approach 1 — geometric-selfsimilar
**Correctly and completely proven:** Lemma G; measure form of A; merge lemma; answer + n=1,2
verification; lower-bound base n=1 and Case 1 (largest piece uncut ⇒ val ≥ 2^n); the tight value c(n)
attained by XY's replica; the **full n=1 upper bound** (rigorous, both a≤1/3 and 1/3<a≤1/2 cases and the
0-mark case handled). n=2 lower bound closed by exhaustive-style argument.

**Genuine open gaps (load-bearing, correctly surfaced):**
- **Lemma LL** — lower bound Case 2, sub-case A(Q) > 0. The merge sub-case A(Q)=0 is closed correctly;
  the A(Q)>0 sub-case is genuinely open, and the note that a single merge step is provably too weak
  (n=3: 104/398 configs have merge-max < 8) is correct and valuable.
- **Claim U** — general upper bound for arbitrary LB configs. Only n=1 done; the inductive-cap sketch
  (§ "General upper cap") is explicitly labeled OPEN, with the A_1<1/2 sub-step flagged as needing its
  own justification. This is honest, not overclaimed.

No circularity, no hidden hand-waving in the proven parts. Status `partial` is accurate.
**Score:** Correctness 5/5, Rigor 4.5/5 (proven parts airtight; gaps precisely delimited),
Progress 4.5/5 (Lemma G proven from asserted, reduction + Case 1 + n=1 upper bound + tightness all new).
**True status: partial. Verdict: CHANGES REQUESTED.**

## Approach 2 — alternating-sum-value
**Correctly and completely proven:** Lemma G (same, correct); reformulation LB = (1+A)/2; the
**integral representation A = measure{x : N(x) odd}** (distinctive tool, fully rigorous, verified);
A-bounds 0≤A≤p_1 and the removal identity A = q_1 − A(rest); lower-bound Case 1 (via removal identity:
A = 2^n − A(rest) ≥ 2^n − 2^{n−1} ≥ 1); tightness (replica forces A = 1). All correct.

**Genuine open gaps (same two as approach 1):**
- **GAP AL** = LL — lower bound Case 2 when XY cuts the largest piece. Correctly open. The recorded
  dead-end (top/bottom decomposition A = A_top + A_bot − 2B fails because A_top ≥ 2B is false,
  min ≈ −10.5) is a genuine and useful negative result.
- **GAP AU** = U — universal upper bound. Open; only the equalization/pairing intuition is given, no
  proven potential decrease. Correctly not claimed.

The file's `## Full proof` section correctly states "Not present — Status is partial." No overclaiming.
**Score:** Correctness 5/5, Rigor 4.5/5, Progress 4.5/5 (integral rep is a clean reusable tool; same
reduction depth as approach 1, slightly less on the upper bound since no full n=1 upper bound written).
**True status: partial. Verdict: CHANGES REQUESTED.**

## Shared-gap observation (for the orchestrator)
Both approaches, and the extremal-smoothing approach, funnel through the **same two gaps**: (1) lower
bound Case 2 with A(Q) > 0, and (2) the universal upper bound. These have been the sub-target since R1.
The upper bound in particular has no proven strategy beyond n=1. If these stay unchanged another round,
consider tasking an explorer to bypass gap (2) — e.g. an upper bound via smoothing/compactness
(extremal-smoothing) that never names an explicit XY strategy — and the outliner to seat ≥1 approach
that reaches c(n) without the concentrate-and-replicate strategy.

## Lemmas certified
- `lemmas/greedy-odd-index.md` — **certified** (updated Status). Statement matches what is proved,
  sorry-free, tie-robust, confirmed against brute force.
- `lemmas/alt-sum-integral.md` — **created + certified** (measure form of A, A-bounds, merge lemma,
  single-cut effect). All verified numerically, proofs correct.

## Outcomes recorded
- geometric-selfsimilar → `advanced` (Lemma G + merge + reduction + Case 1 + n=1 upper bound + tightness
  proven; LL and U still open).
- alternating-sum-value → `advanced` (Lemma G + integral rep + A-bounds + Case 1 + tightness proven;
  AL and AU open; term-by-term decomposition dead-ended).

`current.md` updated (Status partial; furthest correct progress recorded; no Full proof).

## Verdict lines
- **geometric-selfsimilar: CHANGES REQUESTED — Status partial** (gaps: Lemma LL Case-2 A(Q)>0; Claim U general upper bound).
- **alternating-sum-value: CHANGES REQUESTED — Status partial** (gaps: GAP AL Case-2 lower bound; GAP AU universal upper bound).
