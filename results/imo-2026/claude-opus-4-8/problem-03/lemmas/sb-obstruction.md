# Lemma (SB-obstruction theorem — negative result, upper bound)

**Status:** CERTIFIED (proof-reviewer, round 7). Proposed by `geometric-selfsimilar`. Reviewer verified
the equivalence exactly (0 anomalies / 21000 random `(b, Σ, q)`). This is a NEGATIVE result: it rules out
one *family* of proof strategies (SB-monotone reductions) for the residual gap case; it does not preclude
other approaches (an actual-A potential remains viable).

## Statement
Consider a parity-invisible pairing step at a piece `q`: cut `p₁` at offset `q`, delete the invisible
pair `{q,q}`, pass to `X' = (X∖{p₁,q})∪{p₁−q}` with `Σ' = Σ − 2q` at budget `b − 1`. Then (with
`D_b = 2^{b+1}−1`, `τ = Σ·2^b/D_b`)
```
Σ'/D_{b−1} ≤ Σ/D_b   ⟺   q ≥ τ/2 = Σ·2^{b−1}/D_b.
```
**Corollary.** In a gap case (`X` distinct, `p₁ < τ`, `p₂ < τ/2`, so every piece `q ≤ p₂ < τ/2`), every
parity-invisible pairing step gives `Σ'/D_{b−1} > Σ/D_b` (strict). Hence no SB-monotone reduction — one
whose only guarantee is the sum-bound `μ(X',b−1) ≤ Σ'/D_{b−1}` for the smaller instance — can certify the
target `μ(X,b) ≤ Σ/D_b`: the reduced instance's own sum-bound already exceeds the target.

## Proof
`Σ' = Σ − 2q` and `D_b − D_{b−1} = (2^{b+1}−1) − (2^b−1) = 2^b`. Hence
`(Σ − 2q)/D_{b−1} ≤ Σ/D_b ⟺ (Σ − 2q)D_b ≤ Σ D_{b−1} ⟺ Σ(D_b − D_{b−1}) ≤ 2q D_b ⟺ Σ·2^b ≤ 2q D_b ⟺
q ≥ Σ·2^{b−1}/D_b = τ/2`. The corollary is immediate from `q ≤ p₂ < τ/2`. ∎

## Scope
Rigorously establishes the round-6 recorded dead-end (partial-shadow does not preserve the sum-bound
invariant) and sharpens it: it is not partial-shadow specifically, but EVERY invisible-pair step in a
gap case. Consequently the residual `p₁ ≤ Σ/2` requires a potential strictly stronger than the running
sum (tracking the actual alternating sum `A` through the recursion). Correctly scoped: it forbids
SB-chaining, not all proofs.
