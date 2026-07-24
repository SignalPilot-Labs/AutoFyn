## Lemma: Double-Witness Nested Pigeonhole Lemma (CERTIFIED, round 19 — content from round 18)

**Source.** `triangle-consistency-pigeonhole`, round 18, §1. Independently
re-verified by the round-19 proof-reviewer (re-derived from scratch).

**Depends on (certified).** `confined-gcd-lemma.md` (applied twice, with the
two occurrences of type `A` exchanged in the roles of "witness" and
"variable index"); `persistent-type-pigeonhole.md` /
`extended-persistent-type-pigeonhole.md` (for infiniteness of the type index
sets); `free-facts-gcd.md`.

**Setup.** Fix a rogue pair `(A,B)` at core `S_0` (disjoint `S_0`-persistent
extended types), and fix two distinct indices `m_A, m_A' ∈ X_A` (exist since
`X_A` is infinite).

**Statement.** There exist an integer `d_1 | a_{m_A}` and an infinite set
`X_B^{(1)} ⊆ X_B` with `gcd(a_{m_A}, a_x) = d_1` for every `x ∈ X_B^{(1)}`;
and, restricting to `X_B^{(1)}`, an integer `d_2 | a_{m_A'}` and an infinite
set `X_B^{(2)} ⊆ X_B^{(1)}` with `gcd(a_{m_A'}, a_x) = d_2` for every
`x ∈ X_B^{(2)}`. Moreover `d_1, d_2 > 1`, and every prime factor of `d_1`
lies in `F'_{m_A} := P(a_{m_A}) \ S_0`, while every prime factor of `d_2`
lies in `F'_{m_A'} := P(a_{m_A'}) \ S_0` — both fixed finite sets independent
of `x`.

**Proof.** For each `x ∈ X_B`, `gcd(a_{m_A},a_x)` is a positive divisor of
the fixed integer `a_{m_A}`, hence takes finitely many values; since `X_B` is
infinite, pigeonhole gives an infinite `X_B^{(1)} ⊆ X_B` on which this gcd is
constant, `= d_1`. Repeating with `a_{m_A'}` in place of `a_{m_A}` and
`X_B^{(1)}` in place of `X_B` (still infinite) gives `d_2, X_B^{(2)}`.
Positivity `d_1, d_2 > 1` follows from Free Facts (any `x ∈ X_B^{(1)}` has
`x ≠ m_A` since `ρ(x)=B ≠ A=ρ(m_A)`, disjoint hence distinct types).
Confinement: if a prime `p | d_1` lay in `S_0`, then `p ∈ ρ(m_A) ∩ ρ(x) =
A ∩ B = ∅` for `x ∈ X_B^{(1)}`, contradiction; so `p ∈ F'_{m_A}`. Identically
for `d_2`. ∎

**Status.** Correct, complete, unconditional. A direct two-fold application
of the certified Confined-GCD Lemma composed with elementary infinite
pigeonhole; no open hypothesis used. Genuinely new bookkeeping (nests two
pigeonhole passes on two *different, fixed* witnesses of one type against a
shrinking shared subset of the disjoint type's occurrence set) not previously
stated in the workspace. Reusable building block for any future multi-witness
FAH attack.
