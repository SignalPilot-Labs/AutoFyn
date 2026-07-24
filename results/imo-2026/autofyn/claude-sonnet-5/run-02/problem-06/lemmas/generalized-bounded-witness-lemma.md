## Lemma: Generalized Bounded Witness Lemma (S₀-level) (certified)

**Source.** `covering-system-construction`, round 2, Step 4c. A strict generalization of
the certified `bounded-witness-lemma.md`: identical proof, but the argument never
actually used any special property of Q beyond it being a fixed finite set, so it
upgrades verbatim to any fixed finite superset S₀ ⊇ Q and the induced "extended type"
ρ(n) := P(a_n) ∩ S₀. Recommended as the default tool for any future approach reasoning
about extended/refined types (not just base Q-types).

**Statement.** Let S₀ ⊇ Q = P(a_1) be *any* fixed finite set of primes (S₀ need not be
built from any particular construction), and define ρ(n) := P(a_n) ∩ S₀ for n ≥ 1. Let
A', B' ⊆ S₀ be two ρ-types (each occurring for at least one index; in practice applied
to ρ-types occurring infinitely often) with A' ∩ B' = ∅ (disjoint as subsets of S₀ — a
strictly stronger hypothesis than Q-level disjointness of the base types A'∩Q, B'∩Q).
Fix any single index m with ρ(m) = B'. Then for every n > m with ρ(n) = A', a_n is
divisible by some prime of the fixed finite set F'_{A',B'} := P(a_m) \ S₀; in
particular a_n has a prime factor outside S₀.

**Proof.** Fix n > m with ρ(n) = A'. By the Free Facts lemma (`free-facts-gcd.md`),
gcd(a_n, a_m) > 1, so there is a prime p dividing both a_n and a_m. Suppose p ∈ S₀.
Then p ∈ P(a_n) ∩ S₀ = ρ(n) = A' and p ∈ P(a_m) ∩ S₀ = ρ(m) = B', so p ∈ A' ∩ B' = ∅,
contradiction. Hence p ∉ S₀, so p ∈ P(a_m) \ S₀ = F'_{A',B'}, and p | a_n. ∎

**Corollary (Recruitment step, also certified).** With S₀ and ρ as above and 𝒫' the set
of ρ-types occurring infinitely often, suppose A', B' ∈ 𝒫' have disjoint base types
(A'∩Q, B'∩Q disjoint) but A' ∩ B' = ∅ as subsets of S₀ (i.e. the pairwise-intersection
claim (†) fails for this pair). Then there is a specific prime q ∉ S₀ such that q | a_n
for infinitely many n with ρ(n) = A'.

*Proof.* Fix any witness index m with ρ(m) = B' (exists since B' ∈ 𝒫'). By the Lemma,
every n > m with ρ(n) = A' has a_n divisible by some prime of the finite set
F'_{A',B'} = P(a_m) \ S₀. Since A' ∈ 𝒫', infinitely many such n exist (n > m still
leaves infinitely many after discarding the finitely many n ≤ m). Assigning to each such
n some responsible prime in the finite set F'_{A',B'} and applying the infinite
pigeonhole principle (`knowledge_base.md`, "Pigeonhole / extremal principle"), some
single q ∈ F'_{A',B'} ⊆ (primes) \ S₀ is responsible for infinitely many n. ∎

**Status.** Correct, complete, no gaps. Self-contained (uses only the Free Facts
lemma and the infinite pigeonhole principle for the Corollary); does not depend on any
open gap. **Does NOT by itself close gap (†)** — it only shows that IF (†) fails for a
pair, a specific new prime is recruitable; whether the resulting recruitment process
(iteratively enlarging S₀) terminates after finitely many rounds is exactly the open
content of (†) and is NOT established by this lemma.
