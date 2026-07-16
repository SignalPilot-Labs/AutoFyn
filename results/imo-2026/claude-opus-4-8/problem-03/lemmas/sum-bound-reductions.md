# Lemmas R1/R2/R3 (sum-bound reduction moves for the upper bound)

**Status:** CERTIFIED (proof-reviewer, round 6). Proposed by `geometric-selfsimilar`. Reviewer
verified the R2/R3 arithmetic equivalences (0 failures / 20000 random (Σ,b,p₁,q)), equal-pair
invisibility (0/5000), and the R3 leftover identity for `q < p₁` (0/19264; the `q = p₁` case is
excluded, use R1). These are UNCONDITIONAL reduction inequalities; they do NOT by themselves prove the
sum-bound (SB) — a residual "gap case" remains open.

## Setup
`X` a finite multiset of positive lengths, `Σ = Σ(X)`, `b ≥ 0` an integer cut budget,
`D_b := 2^{b+1} − 1`. `μ(X,b) := min over all placements of ≤ b interior cut points of A(result)`,
`A(P) = measure{x : N_P(x) odd}` (Lemma M0). Cutting preserves `Σ`. **Target (SB):**
`μ(X,b) ≤ Σ / D_b`. Key fact: adding an equal pair `{w,w}` to any multiset leaves `A` unchanged
(it changes `N` by an even amount everywhere), so equal pairs are "parity-invisible spectators".

## Lemma R1 (free pair removal)
If `X` contains two equal pieces of value `w`, then `μ(X,b) ≤ μ(X ∖ {w,w}, b)`.
*Proof.* XY leaves the pair uncut and plays optimally on `X' = X ∖ {w,w}`; the pair is
parity-invisible, so the achieved `A` equals that on `X'`. ∎

## Lemma R2 (halving)
Let `b ≥ 1`, `p₁ = max(X)`. Then `μ(X,b) ≤ μ(X ∖ {p₁}, b−1)`. Moreover if
`p₁ ≥ Σ·2^b / D_b` and (SB) holds for `X ∖ {p₁}` at budget `b−1`, then (SB) holds for `X`.
*Proof.* XY cuts `p₁` at its midpoint (1 cut) into two equal halves — parity-invisible — then plays
optimally on `X ∖ {p₁}` with `b−1` cuts, giving the reduction. Then
`μ(X,b) ≤ (Σ − p₁)/(2^b − 1) ≤ Σ/(2^{b+1} − 1) ⟺ Σ·2^b ≤ p₁·D_b`, i.e. `p₁ ≥ Σ·2^b/D_b`. ∎

## Lemma R3 (pairing)
Let `b ≥ 1`, `p₁ = max(X)`, and let `q` be another piece with `q < p₁`. Then
`μ(X,b) ≤ μ((X ∖ {p₁,q}) ∪ {p₁−q}, b−1)`. Moreover if `q ≥ Σ·2^{b−1}/D_b` and (SB) holds for the
reduced instance, then (SB) holds for `X`.
*Proof.* XY cuts `p₁` at offset `q` into `(q, p₁−q)` (1 cut); the new `q` pairs with the spectator
`q`, parity-invisible, leaving `(X ∖ {p₁,q}) ∪ {p₁−q}` (mass `Σ − 2q`). Then
`μ(X,b) ≤ (Σ − 2q)/(2^b − 1) ≤ Σ/(2^{b+1} − 1) ⟺ q ≥ Σ·2^{b−1}/D_b`. (`q = p₁` ⇒ use R1.) ∎

## Base case and induction
`μ(X,0) = A(X) ≤ max(X) ≤ Σ = Σ/D_0`. Strong induction on `(b, |X|)` lexicographically: R1 drops
`|X|`, R2/R3 drop `b`. With `τ := Σ·2^b/D_b`: apply R1 if two pieces are equal, else R2 if
`p₁ ≥ τ`, else R3 if `p₂ ≥ τ/2`.

## Scope
(SB) is proved for every `(X,b)` whose reduction tree never reaches the **gap case** (distinct `X`,
`p₁ < τ`, `p₂ < τ/2`). Consequences: Regime C (`A₁ > c(n)`) gets a rigorous opening cut (R2 fires,
halve `A₁`), and a slice of B2 closes via R3. The **gap case is OPEN** — the partial-shadow move does
NOT preserve the sum invariant (`Σ(R′)/D_{b−j} ≤ Σ/D_b` fails on many instances), so a strictly
stronger potential than the running sum is needed. R1/R2/R3 individually are certified; the full upper
bound (SB) is NOT.
