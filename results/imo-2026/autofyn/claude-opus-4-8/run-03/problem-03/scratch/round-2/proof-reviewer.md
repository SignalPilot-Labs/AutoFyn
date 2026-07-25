# Proof review — imo-2026-03 (IMO 2026 P3), Round 2

Reviewed three built approaches. Claimed answer **c(n) = 2^n/(2^{n+1}−1)** — numerically
consistent for n=1,2,3; not fully proven (both global bounds remain the field crux).

## Foundational lemmas — verified independently and CERTIFIED

I re-derived and numerically checked the shared foundation. All pass; certified into
`results/imo-2026-03/lemmas/`.

- **L0 (claiming lemma).** LB value = odd-rank sum, greedy optimal. Proof via constant-sum
  recursion V(P)=T−min_i V(P∖{p_i}) + order-statistic monotonicity (raising one element
  weakly increases every order statistic ⇒ removing the larger of two adjacent ranks
  minimizes the opponent's odd-rank sum). Rigorous. Numeric: 0/300 mismatches vs brute-force
  minimax. Both approach writeups (induction-peel's and smoothing-extremal's) are correct;
  I certified the cleanest form.
- **L1 (order irrelevance).** c(n)=max_A min_B Σ_odd(B). Correct; reachable B = ≤n-split
  refinements of A, value depends only on the multiset. Rigorous.
- **L2 (potential identity).** Σ_odd=(1+S)/2; target ⟺ max_A min_B S = 1/D_n. Trivial, correct.
- **L3 (layer-cake).** S(B)=meas{t:#parts>t odd}, plus XOR decomposition S(Q⊔C)=S(Q)+S(C)−2W,
  W=meas{both odd}, giving S≥|S(Q)−S(C)|. Rigorous. Numeric: 0/400 mismatches.
- **L4 (min-pairing / balanced-mass).** S = min-pairing cost = 1−2β. The writeup's uncrossing
  proof is standard but sketched; I certified an airtight proof via L3-parity (c(t)≡N(t) mod 2
  ⇒ any pairing cost ≥ S). Numeric: 0/400 mismatches. Yields the witness principle for the
  upper bound.

The maximizer-existence reformulation (S* continuous on the simplex via Berge's Maximum
Theorem → EVT) in smoothing-extremal is also correct and durable.

These four+ lemmas are the round's genuine, reusable value and the reductions are watertight.

## Per-slug verdicts

### induction-peel — CHANGES REQUESTED (Status: partial) — builder's status is HONEST
Complete & rigorous: L0/L1/L2/L3, base case n=1 (both bounds), and lower-bound **Case 1**
(top dyadic piece uncut ⇒ S(B)=2^n−S(C) ≥ 1 via S(C)≤sum(C)). The two gaps are honestly
marked and are real:
- **Sub-claim A2** (lower Case 2, XY cuts the top piece): S(Q⊔C)≥1. The abstract bound
  S≥|S(Q)−S(C)| is genuinely too weak (correctly acknowledged); needs the dyadic structure
  of C and the "+1" superincreasing margin. Unproven — correctly left as a gap.
- **Sub-claim B** (upper bound): MATCH/BISECT value-function induction. Left as a gap; the
  claimed target inequality 2^{k−1}/D_{k−1} > 2^k/D_k is correct, showing the generic IH is
  insufficient — an honest statement of why the crux is hard, not a hidden leap.
No overclaim: no gap is presented as proven. Good progress. Re-dispatch to close A2 and B.

### alternating-sum-potential — CHANGES REQUESTED (Status: partial) — builder's status is HONEST
Complete & rigorous: L0/L1/L2/L3/L4 (adds the certified min-pairing/witness principle L4),
full n=1, lower-bound case (i), and the exact XOR decomposition (†). Gaps honestly marked:
- **G1** (binding lower-bound case): overlap term W uncontrolled; (†) alone insufficient
  (correctly stated). Unproven.
- **G2** (general upper bound / Lemma D): witness pairing with β≥(2^n−1)/D_n for arbitrary A.
  Only the dyadic illustration is done; the general construction is explicitly open (F1: no
  one-pass rule). No overclaim. This slug's distinct durable asset over induction-peel is L4.
Re-dispatch to attack G1 (overlap W) / G2 (witness pairing).

### smoothing-extremal — RETHINK (Status: unsolved as a route) — builder's self-assessment CONFIRMED
The approach's crux mechanism, **Lemma G** (a single sum-preserving consecutive-pair move
toward ratio 2:1 does not decrease S*), is refuted, and I judge the refutation sound and
decisive — not premature. The structural obstruction is a proof, not just numerics: a
sum-preserving consecutive-pair move fixes that pair's sum, so no sequence of such moves can
even connect a generic A to the dyadic G_n (whose pair-sums are specific). The surviving
weaker claim ("some improving 2-part transfer exists at every non-dyadic A") requires the
directional derivative of a min-over-XY-responses, i.e. it re-imports XY's optimal-response
structure — the very crux the framing was meant to bypass. So the framing cannot deliver a
crux-avoiding upper bound. Route back to the outliner for a different strategy. Its durable
output (L0/L1/L2 + maximizer-existence reformulation) is retained and certified.

## Recorded outcomes (ranker)
- induction-peel: **advanced** (Elo ~1572, field leader) — Case 1 + reductions rigorous.
- alternating-sum-potential: **advanced** (Elo ~1516) — L4 witness principle + XOR decomp.
- smoothing-extremal: **dead-end** (Elo ~1454) — Lemma G refuted; RETHINK.

## Goal Progress (for Eval History)
Status of population: **partial** (no solve). Answer c(n)=2^n/D_n established as target and
numerically consistent (n=1,2,3). Reductions L0–L4 now fully proven and certified — durable
foundation locked. Two live approaches (induction-peel #1, alternating-sum-potential #2) share
the same two open crux gaps: the **general upper bound** (witness/value-function for arbitrary A)
and the **binding lower-bound case** (XY cuts the top piece). smoothing-extremal dead-ended
(RETHINK). Shared-gap watch: both live approaches now bottom on the same upper-bound crux —
if unclosed next round, the field is one framing away from a plateau; a genuinely different
upper-bound framing should be opened. n=1 fully solved as a proof-of-concept for both bounds.
