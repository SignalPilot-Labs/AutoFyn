## Lemma: Extended Persistent-Type Pigeonhole (certified)

**Source.** Independently derived (identical statement and proof mechanism) in both
`covering-system-construction` (round 1/2, Step 4, the "𝒫' " construction) and
`greedy-exchange-cost-potential` (round 2, "Lemma C"). A verbatim upgrade of the
certified `persistent-type-pigeonhole.md` from the base set Q to any fixed finite
superset S₀ ⊇ Q. Certified once here as the canonical shared statement so future
approaches can cite one lemma instead of re-deriving it.

**Statement.** Let S₀ ⊇ Q = P(a_1) be a fixed finite set of primes (e.g. S₀ = Q ∪ S
from the Finite Core Theorem), and define ρ(n) := P(a_n) ∩ S₀ for n ≥ 1 (nonempty since
τ(n) ⊆ ρ(n) and τ(n) ≠ ∅ by the Free Facts lemma). Then there is a finite, nonempty set
𝒫' ⊆ 2^{S₀} \ {∅} of "extended-persistent" types (occurring infinitely often) and a
threshold N₂ such that ρ(n) ∈ 𝒫' for every n > N₂.

**Proof.** Identical to the certified Persistent-Type Pigeonhole's proof with Q
replaced by S₀: ρ maps the infinite index set into the finite set 2^{S₀} \ {∅} (size
2^{|S₀|} − 1), so by the infinite pigeonhole principle (`knowledge_base.md`,
"Pigeonhole / extremal principle") some value is attained infinitely often, giving 𝒫'
nonempty; every type not in 𝒫' occurs only finitely often, and 2^{S₀} \ {∅} is finite,
so the total number of indices with ρ(n) ∉ 𝒫' is a finite sum of finitely many finite
quantities, hence finite; let N₂ be the largest such index (0 if none). ∎

**Status.** Correct, complete, no gaps. Self-contained; does not depend on any open
gap. Sets up the correct finite state space 2^{S₀} for the eventual CRT + cyclic
pigeonhole finish, but does NOT by itself determine which subsets of S₀ the
extended-persistent types 𝒫' actually are, nor whether disjoint-base-type pairs among
them intersect in S₀ — that is exactly gap (†), which remains open.
