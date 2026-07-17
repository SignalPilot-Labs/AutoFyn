# Lemma TwoLevelCascade — two dominant-top-piece flat-residual closures (certified round 8)

**Setup.** Odd-sum marking game (Lemma G1); A = μ(⊕_i [0,ℓ_i]) (Lemma X); D = 2^{n+1}−1. Flat residual
on the σ-face: b_1 ≥ … ≥ b_q, Σ b_i = S = (2^q−1)/D, b_1 ≤ 2^{q-1}/D, b_2 ≤ 2^{q-2}/D, gaps ≥ 1/D,
b_q ≥ 1/D. Threshold identity: (S + 1/D)/2 = 2^{q-1}/D (verified).

**Statement.**
- **(c1)** If b_1 ≥ S/2, XY forces A = 2b_1 − S ≤ 1/D with q−1 cuts.
- **(c2a)** If b_1 < S/2 and b_2 ≥ (S−b_1)/2, XY forces A = 2b_2 − (S−b_1) ≤ 1/D with q−1 cuts.

**Proof (c1).** Generalized GreedyCascade with total mass S (the certified GreedyCascade proof uses the
total only via r_p = 2b_1 − Σ and legality b_1 ≥ Σ/2, both stated in the actual total). Set r_1 = b_1;
for j = 1,…,q−1 cut leftover r_j at b_{j+1}, giving fragment b_{j+1} and r_{j+1} = r_j − b_{j+1}. Then
r_j = b_1 − (b_2+…+b_j). Legality b_{j+1} ≤ r_j ⟺ b_2+…+b_{j+1} ≤ b_1, which holds since
b_1 ≥ S/2 ≥ S − b_1 = b_2+…+b_q. Each of b_2,…,b_q appears twice (intact + as a fragment of b_1) and
XOR-cancels (Lemma X); the sole survivor is r_q = 2b_1 − S, so A = μ([0, 2b_1−S]) = 2b_1 − S ≥ 0.
Using b_1 ≤ 2^{q-1}/D = (S+1/D)/2: A ≤ 2·2^{q-1}/D − S = 2^q/D − (2^q−1)/D = 1/D. ∎

**Proof (c2a).** Cuts: (1) halve b_1 into (b_1/2, b_1/2) — these XOR-cancel (Lemma X). (2) Greedy-cascade
b_2 over {b_3,…,b_q}, total mass s' = S − b_1, using q−2 cuts: r_1 = b_2, cut at b_3,…,b_q successively.
Legality b_2 ≥ b_3+…+b_{j+1} holds since b_2 ≥ (S−b_1)/2 = s'/2 ≥ b_3+…+b_q. Survivors: two halves of
b_1 (cancel), b_3..b_q twice each (cancel), and final leftover r = 2b_2 − s' = 2b_2 − (S−b_1) ≥ 0. So
A = 2b_2 − (S−b_1). Total cuts 1 + (q−2) = q−1. Bound: A = 2b_2 − S + b_1 ≤ 2·2^{q-2}/D − (2^q−1)/D + b_1
= b_1 − (2^{q-1}−1)/D ≤ 2^{q-1}/D − (2^{q-1}−1)/D = 1/D, using b_2 ≤ 2^{q-2}/D and b_1 ≤ 2^{q-1}/D. ∎

**Scope.** Closes the two dominant-top-piece slivers of the flat residual for all q. The complementary
slice **c2b = {b_1 < S/2 AND b_2 < (S−b_1)/2}, q ≥ 5** is NOT covered (open; the bulk of the flat
residual). Generalizes certified GreedyCascade to arbitrary total mass S; c2a is new (round 8).
