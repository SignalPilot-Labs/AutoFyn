## Lemma: Single-Witness-Prime Pigeonhole Refinement (certified)

**Source.** `greedy-exchange-cost-potential`, round 2 ("Lemma B"). Sharpens the
certified `bounded-witness-lemma.md`: instead of "some prime of the fixed finite set
F_{A,B} divides a_n" (possibly a different prime for each n), it isolates ONE specific
prime that recurs infinitely often. Strictly more informative than the Bounded Witness
Lemma alone, though — as documented in both `covering-system-construction` and
`greedy-exchange-cost-potential` — it is NOT by itself strong enough to close gap (†),
because the argument does not extend to arbitrary (non-canonical) witnesses without
risking "junk" primes outside the fixed core S₀.

**Statement.** Let A, B ∈ 𝒫 (persistent Q-types, see `persistent-type-pigeonhole.md`)
be disjoint. Let m_B be any fixed witness index with τ(m_B) = B, and
F_{A,B} := P(a_{m_B}) \ Q. Then there is a single prime p*(A,B) ∈ F_{A,B} such that the
set {n > m_B : τ(n) = A and p*(A,B) | a_n} is infinite.

**Proof.** Let N_A := {n > m_B : τ(n) = A}, infinite since A is persistent (only
finitely many n ≤ m_B are excluded). By the Bounded Witness Lemma (witness m = m_B),
every n ∈ N_A has a_n divisible by some prime of the finite set F_{A,B}. Define
g : N_A → F_{A,B} by choosing, for each n, one such prime g(n). Since F_{A,B} is finite
and N_A infinite, by the infinite pigeonhole principle (`knowledge_base.md`,
"Pigeonhole / extremal principle") some p* ∈ F_{A,B} is attained by g on an infinite
subset of N_A. ∎

**Status.** Correct, complete, no gaps. Self-contained (uses only the certified
Bounded Witness Lemma and the infinite pigeonhole principle); does not depend on any
open gap. Does NOT close (†) — see the honest discussion in
`greedy-exchange-cost-potential.md` ("Where this leaves gap (†)") for exactly where
the natural attempt to extend it to extended types stalls.
