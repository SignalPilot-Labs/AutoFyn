# Lemma H — halve-the-(p−1)-largest formula (certified round 3)

**Setup.** In the odd-sum marking game (Lemma G1), once cuts are fixed and pieces are sorted
weakly decreasing, LB's guaranteed take equals the odd-sum O, and with A = O − E the sorted
alternating sum one has O = (1 + A)/2 (since O + E = 1). Let LB's pieces be a_1 ≥ … ≥ a_p
(Σ = 1, p ≤ n+1).

**Statement.** Suppose XY cuts each of the p−1 largest LB pieces a_1,…,a_{p−1} at its midpoint
(p−1 ≤ n cuts, within budget) and leaves a_p intact. Then the resulting odd-sum is
    **O = 1/2 + a_p/2.**
Consequently, if a_p ≤ 1/D (D = 2^{n+1}−1) then O ≤ 1/2 + 1/(2D) = 2^n/D = c(n), so this XY
strategy holds LB to ≤ c(n) (Case A of the upper bound).

**Proof.** The 2p−1 resulting pieces are the p−1 equal pairs {a_i/2, a_i/2} (i = 1,…,p−1) and
the singleton a_p. The map from the LB piece vector (a_1,…,a_p) to the resulting odd-sum O is
continuous (sorting is continuous and A is a continuous function of the sorted list, so
O = (1+A)/2 is continuous). It therefore suffices to prove O = 1/2 + a_p/2 on the dense set G
of vectors (a_i) with the a_i mutually distinct and a_i/2 ≠ a_p for all i; both sides are
continuous in (a_i), so equality on the dense set G forces equality everywhere. (Note the
pairs are exact by construction — a_i/2 twice — for every (a_i); the genericity is only on the
values a_i, so G is dense in a-space and O and 1/2 + a_p/2 are continuous coordinates.)

Assume (a_i) ∈ G. Then all half-values a_i/2 are mutually distinct and distinct from a_p.
- Each pair {a_i/2, a_i/2} consists of two equal values, and since no other piece equals
  a_i/2, the two copies occupy two CONSECUTIVE ranks r, r+1 in the sorted list. In the sorted
  alternating sum A = Σ_ρ (−1)^{ρ+1} r_ρ, consecutive ranks carry opposite signs, so the pair
  contributes (−1)^{r+1}·a_i/2 + (−1)^{r+2}·a_i/2 = 0 to A — regardless of where it sits.
- Locate a_p. Let k = #{i : a_i/2 > a_p}. Each such pair puts 2 pieces above a_p and each
  pair with a_i/2 < a_p puts none above (both copies equal, hence on the same side of a_p as
  a_i/2 ≠ a_p). So exactly 2k pieces exceed a_p, placing a_p at rank 2k+1, which is ODD; it
  contributes (−1)^{2k+2}·a_p = +a_p to A.

Summing, A = a_p (all pairs contribute 0), so O = (1 + A)/2 = 1/2 + a_p/2. ∎

**Machine check.** 2·10^5 random configs (p ≤ 6), |O − (1/2 + a_p/2)| ≤ 1.1·10^{-16}.

**Scope.** Closes Case A (a_p ≤ 1/D) of the XY upper bound for all n. Case B (a_p > 1/D,
i.e. all pieces > 1/D) is NOT covered by this lemma and remains open (GAP U1).
