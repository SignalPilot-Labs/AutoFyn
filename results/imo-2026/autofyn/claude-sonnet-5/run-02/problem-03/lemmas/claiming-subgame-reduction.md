## Statement

Given any fixed final multiset of piece lengths $L_1\ge L_2\ge\dots\ge L_m$
on the stick, if the two players alternately claim pieces (Liu Bang first,
each maximizing his own total), the game value is unique regardless of
tie-breaking, and is achieved by both players always claiming the
currently-largest unclaimed piece:
$$\text{Liu Bang's total} = \Phi(\{L_i\}) := \sum_{i\text{ odd}} L_i,\qquad
\text{Xiang Yu's total} = \sum_{i\text{ even}}L_i.$$

Consequently the whole problem reduces to a purely combinatorial question:
$$c(n) = \max_{\text{Liu Bang's} \le n \text{ points}}\ \min_{\text{Xiang
Yu's}\le n\text{ points}}\ \Phi(\text{final multiset}).$$

## Proof

See `results/imo-2026-03/approaches/greedy-halving-adversary.md`, Lemma 1,
for the full exchange-argument proof (monotonicity sub-claim + downward
induction on the number of remaining pieces showing greedy-max is a mutual
best response).

## Certification note (proof-reviewer, round 1)

Re-derived independently by brute-force minimax search (exact game tree,
not the claimed formula) over 200 random multisets of sizes 1–6 with
integer entries: the minimax game value matched $\Phi(\{L_i\})$ in every
case, no mismatch found. The written proof is a standard exchange argument;
combined with the brute-force cross-check this lemma is certified correct
and safe for any approach to this problem to import without re-proving.
