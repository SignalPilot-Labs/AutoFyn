# Build report — geometric-selfsimilar (R6)

Status: **partial** (unchanged flip; real new rigorous progress on the upper bound).

## What I did
Attacked the assigned upper-bound targets (B2 general n; push C). Found a **unifying reformulation**
that collapses Regimes A/B/C into one statement and proved the load-bearing reduction lemmas.

### Unified target (SB)
μ(X, b) := min over ≤ b cuts of A(result). The whole upper bound is
  **μ(X, b) ≤ Σ(X)/(2^{b+1}−1)** — for LB (Σ=1, b=n) this is μ ≤ 1/D ⟺ val ≤ c(n), all regimes at once.
Tight exactly on the geometric config. Verified: strategy search gives μ ≤ 1/D with 0 violations,
n=1..6 (exact Fractions).

### Rigorous new lemmas (fully proved, arithmetic double-checked symbolically)
- **R1 free pair removal:** equal pair ⇒ μ(X,b) ≤ μ(X∖pair, b). Parity-invisible spectators.
- **R2 halving (Case I):** p_1 ≥ Σ·2^b/D_b ⇒ halve p_1, μ(X,b) ≤ μ(X∖{p_1}, b−1) ≤ Σ/D_b.
- **R3 pairing:** some q ≥ Σ·2^{b−1}/D_b ⇒ pair p_1 with q, μ(X,b) ≤ Σ/D_b.
Each reduces to a lex-smaller instance; base b=0 is A ≤ p_1 ≤ Σ. Both D_b-equivalences derived line by
line and re-verified over 20000 random (Σ,b,p_1,q).

### Payoff
- **Regime C gets a rigorous opening cut:** A_1 > c(n) = τ ⇒ R2 fires (halve A_1), reducing C to (SB)
  for {A_2,…,A_m} at budget n−1. Supersedes the previously-unproven "dominant-chop". C now funnels into
  the single residual gap.
- A slice of B2 (A_2 ≥ 2^{n−1}/D) closed by R3.
- R1/R2/R3 alone close 100/99.3/96.7/93.8/89.9/85.6 % of sampled LB configs (n=1..6), 0 bound violations
  among closed configs.

### The single residual gap (honest)
Distinct X with p_1 < τ and p_2 < τ/2 ("spread/small-max"). This **subsumes both** old open gaps
(B2-general and C). Recorded dead-end: the partial-shadow (greedy-prefix) move does NOT preserve the
(SB) invariant — Σ(R′)/D_{b−j} ≤ Σ/D_b is violated 18/123/315/678 times at n=3/4/5/6 — so the naive sum
induction cannot pass through it, even though the final A stays ≤ 1/D by slack. Closing the gap needs a
potential stronger than the running sum. That is the honest frontier.

## Files
- Wrote: `results/imo-2026-03/approaches/geometric-selfsimilar.md` (new "Unified sum-bound framework"
  section with full proofs of R1/R2/R3, base case, induction structure, regime consequences, gap +
  dead-end; updated Approaches tried / Current best / Open gaps / Verification log / Promotable lemmas).
- Proposed for certification: `lemmas/sum-bound-reductions.md` (R1/R2/R3).

## Spec concerns
None. Answer c(n)=2^n/(2^{n+1}−1) unchanged. Lower bound (Lemma LL t≥2) untouched — owned by the LL
slugs. Enforced the joint cut budget (≤ n total) in every numeric check.

## Note for the reviewer
The R6 lemmas are conditional-reduction statements (bound μ(X,b) by μ of a smaller instance); combined
with the base case they *prove* (SB) unconditionally for every branch that avoids the gap. They do NOT
close B2 general n or C on their own. Status stays partial, honestly. The value is: (i) unification of
the upper bound into one clean target, (ii) three certifiable reduction lemmas, (iii) a rigorous first
step for Regime C, (iv) one precisely-delimited residual gap with the partial-shadow dead-end recorded.
