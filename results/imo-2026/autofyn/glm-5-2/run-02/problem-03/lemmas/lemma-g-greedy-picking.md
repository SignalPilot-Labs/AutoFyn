# Lemma G — greedy-picking → odd-rank sum

**Statement.** After all marks are placed, sort the final pieces descending
`p_1 ≥ p_2 ≥ … ≥ p_M` (M ≤ 2n+1). In the alternating-pick phase (Liu first,
each player maximizes their own total, both optimal), Liu's payoff equals the
**odd-rank sum** `p_1 + p_3 + p_5 + …`, and Xiang's payoff equals the
**even-rank sum** `p_2 + p_4 + …`. Greedy play (always take the largest
unclaimed piece) is optimal for BOTH players.

**Equivalently.** `Liu = (1 + A)/2` where `A = Σ_i (−1)^{i+1} p_i` is the
alternating (advantage) sum. Bounding Liu's payoff is equivalent to bounding
`A`.

**Proof (strong induction on M, both move-orders loaded into one induction).**
Define (A): with Liu to move on sorted `p_1 ≥ … ≥ p_M`, the value to Liu is
`oddsum = p_1 + p_3 + p_5 + …`. (B): with Xiang to move on sorted
`p_1 ≥ … ≥ p_M`, the value to Liu is `evensum = p_2 + p_4 + …`. (If M is odd,
"oddsum" includes the last piece; "evensum" stops at p_{M−1}. If M is even,
vice versa. The player to move gets the odd-indexed pieces of the sorted
remaining multiset.)

**Base cases.** M=1: Liu-to-move takes `p_1`, value `= p_1 = oddsum` ✓;
Xiang-to-move takes `p_1`, value to Liu `= 0 = evensum` ✓. M=2: Liu-to-move
takes `p_1` (taking `p_2` leaves `p_1` for Xiang, strictly worse since
`p_1 ≥ p_2`), then Xiang-to-move on `{p_2}` gives Liu 0; value `= p_1 = oddsum` ✓.
Xiang-to-move takes `p_1` (taking `p_2` leaves `p_1` for Liu, strictly worse for
Xiang), then Liu-to-move on `{p_2}` gives Liu `p_2`; value to Liu `= p_2 = evensum` ✓.

**Inductive step** (assume (A),(B) for all multisets of size < M; prove M ≥ 3).

*Proof of (A).* Liu chooses piece `p_k`; by IH (B) the residual value is
`evensum(R_k)`. Removing `p_k` from the sorted list shifts positions `> k` left
by one (flipping even↔odd), so `evensum(R_k) = Σ_{j<k, j even} p_j + Σ_{j>k, j odd} p_j`.
For `k = 1`: `evensum(R_1) = Σ_{j>1, j even}... ` — careful: `R_1`'s position 1
= `p_2`, position 2 = `p_3`, …, so even-indexed in `R_1` = `p_3, p_5, …`, hence
`evensum(R_1) = p_3 + p_5 + …` and `p_1 + evensum(R_1) = oddsum`. For `k ≥ 2`,
`Δ_k = (p_k + evensum(R_k)) − oddsum`:
- k odd, k=2m+1: `Δ_k = Σ_{j<2m+1, j even} p_j − Σ_{j<2m+1, j odd} p_j = (p_2−p_1) + (p_4−p_3) + … + (p_{2m}−p_{2m−1}) ≤ 0`.
- k even, k=2m: `Δ_k = p_{2m} + Σ_{j<2m, j even} p_j − Σ_{j<2m, j odd} p_j = (p_2−p_1) + … + (p_{2m}−p_{2m−1}) ≤ 0`.
Each term `≤ 0` by the sorted order. So `k = 1` is a maximizer, value = oddsum;
greedy (take `p_1`) is optimal for Liu. ∎ (A)

*Proof of (B).* Symmetric. Xiang chooses `p_k` to MINIMIZE Liu's value, which by
IH (A) is `oddsum(R_k)`. Removing `p_k`: `oddsum(R_k) = Σ_{j<k, j odd} p_j + Σ_{j>k, j even} p_j`.
For `k = 1`: `oddsum(R_1) = Σ_{j even} p_j = evensum`. For `k ≥ 2`,
`oddsum(R_k) − oddsum(R_1) = (p_1−p_2) + (p_3−p_4) + … ≥ 0` (each term ≥ 0 by
sorted order), for both k odd and k even. So `k = 1` is a minimizer, value to
Liu = evensum; greedy (take `p_1`) is optimal for Xiang. ∎ (B)

By (A) with M = number of final pieces, Liu's payoff under optimal play is the
odd-rank sum. ∎

**Verification.** Brute-force minimax vs `oddsum` on 5000 random multisets of
size 1–7, values in {1..20}: 0 mismatches.

**Knowledge-base tools.** Invariants & monovariants (the alternating sum is the
game's natural monovariant); Induction (strong, on M, loading both move-orders
into one induction — Pólya "a stronger statement is sometimes easier to prove by
induction").

**Where proved.** `approaches/pairing-partner.md` (the rigorous version).
`approaches/induct-one-mark.md` also states Lemma G but its upper-bound half is
flawed (the per-piece claim is false under Liu deviation) — use this certified
version instead.
