# Lemma (Parity-Condition, INC branch)

**Status:** CERTIFIED (proof-reviewer, round 6). Proposed by `ll-inclusion-gap` as the corrected
replacement for the R5-decertified FALSE "Structural Lemma" part (a). Reviewer verified the parity
claim (h even; `N_Q` even on every forbidden band) over all 52 n=3 INC configs (0 failures) and
confirmed it is satisfied by the R5 counterexample `Q={3/2,3/2,2,3}` (a genuine INC config).

## Statement
Let `S_P := {x ≥ 0 : N_P(x) odd}`, `N_P(x) = #{parts of P exceeding x}`. Suppose `S_Q ⊆ S_R`. Then at
every point `x` with `N_R(x)` even, `N_Q(x)` is even.

Specialization to `R = G_{n−1} = {2^0,…,2^{n−1}}`: the dyadic bands `I_0 = [0,1)`,
`I_k = [2^{k−1}, 2^k)` (`1 ≤ k ≤ n−1`) carry `N_{G_{n−1}} = n` on `I_0` and `N_{G_{n−1}} = n−k` on
`I_k`. Call a band **forbidden** when `N_{G_{n−1}}` is even there. Then:
- **(P1)** `N_Q(x)` is even for every `x` in a forbidden band;
- **(P2)** for every dyadic point `2^j` that is the top of a forbidden band, `#{parts ≥ 2^j}` is even;
- **(P3)** inside a forbidden band, Q-parts occur with parities keeping `N_Q` even — an equal interior
  pair `{s, s}` is admissible; two distinct interior values are not.

## Proof
If `N_Q(x)` were odd then `x ∈ S_Q ⊆ S_R`, so `N_R(x)` is odd; the contrapositive is the main claim.
(P1) is the specialization to forbidden bands, where `N_{G_{n−1}}` is even. (P2): `x = 2^j − 0` lies
in the forbidden band, `N_Q(2^j−0) = #{parts ≥ 2^j}`, even by (P1). (P3): `N_Q` is even throughout the
band; as `x` decreases across an interior value of multiplicity `μ`, `N_Q` jumps by `μ`, so to remain
even each interior value must have even multiplicity. ∎

## Scope
This is the TRUE parity mechanism replacing the false "no Q-part in a forbidden-band interior". It
permits even-multiplicity interior pairs (the {3/2,3/2} pair that broke the old lemma). Used to prove
`h = #{parts ≥ 2^{n−2}}` even in the top-band decomposition (`lemmas/top-band-decomposition.md`) and
in the complete n=3 INC base case. Reviewer-verified: 0 failures over all 52 n=3 INC configs.
