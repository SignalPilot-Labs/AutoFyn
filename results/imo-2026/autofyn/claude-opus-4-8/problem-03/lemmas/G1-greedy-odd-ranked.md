# Lemma G1 — greedy = odd-ranked (certified round 2)

**Statement.** Fix a finite multiset of piece-lengths, sorted weakly decreasing
r_1 ≥ r_2 ≥ … ≥ r_m. Two players alternately claim an unclaimed piece, the first player
moving first, each maximising the total length of the pieces they collect. Then, under
optimal play, the first player collects exactly the odd-ranked pieces r_1 + r_3 + …, and
"always take a currently-largest piece" (greedy) is an optimal strategy for **both**
players.

**Proof.** The total T = Σ r_i is constant, so maximising own total is equivalent to
maximising the difference d = (own − opponent): own = (T + d)/2 is increasing in d. This is
a zero-sum game on d, the mover maximising d. For a sorted multiset q let V(q) be the value
of this difference game with the mover to move. Then
  V(q) = max_{1≤j≤k} [ q_j − V(q ∖ q_j) ]        (∗)
(after the mover takes q_j, the opponent becomes mover of the remainder and achieves
V(q ∖ q_j) in their favour = −V(q ∖ q_j) for the original mover).

Let A(q) = Σ_i (−1)^{i+1} q_i (alternating sum of the sorted list). Claim by induction on k:
V(q) = A(q) and the max in (∗) is attained at j = 1 (greedy). Base k = 0,1 immediate.
Step: with V(q ∖ q_j) = A(q ∖ q_j), write f(j) = q_j − A(q ∖ q_j). Removing position j keeps
signs of i < j and flips signs of i > j, and one computes for 1 ≤ j ≤ k−1
  f(j) − f(j+1) = (q_j − q_{j+1})·(1 + (−1)^{j+1}) ≥ 0,
since the factor is 2 (j odd) or 0 (j even) and q_j ≥ q_{j+1}. So f is non-increasing, its
max is at j = 1, and V(q) = f(1) = q_1 − (q_2 − q_3 + …) = A(q). The first player's total is
(T + V)/2 = (Σ q_i + A(q))/2 = Σ_{i odd} q_i. ∎

**Verification.** Checked against exact minimax recursion V(q) for 2000 random multisets
(sizes 0–7): V(q) = A(q) and first-player optimal total = odd-ranked sum, both to 1e-9.

**Certification.** Reviewer-verified round 2. Statement correct, proof sorry-free, no
stronger than proved. Admitted to shared cache.
