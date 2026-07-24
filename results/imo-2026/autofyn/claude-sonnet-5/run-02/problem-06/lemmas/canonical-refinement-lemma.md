## Lemma: Canonical-Refinement Lemma (certified)

**Source.** Independently proved in both `covering-system-construction` (Step 4d,
"General Reconciliation Lemma" + "canonical refinement equals base ∪ extra-primes,
exactly" + "Theorem (Canonical-Refinement Lemma)") and `greedy-exchange-cost-potential`
(Step "ROUND 3: importing...", restated as "Lemma D"). The two proofs are the same
mathematical content in different notation; certified once here as the canonical
statement, crediting both approach files.

**Depends on (certified).** `free-facts-gcd.md`, `bounded-witness-lemma.md`,
`finite-core-theorem.md`, `persistent-type-pigeonhole.md`.

**Setup.** Q = P(a_1), τ(n) = P(a_n) ∩ Q, 𝒫 the finite set of persistent (Q-level)
types. S := ⋃_{B∈𝒫}(P(a_{m_B})\Q) (Finite Core Theorem, one canonical witness m_B per
B ∈ 𝒫), S₀ := Q ∪ S, ρ(n) := P(a_n) ∩ S₀, 𝒫' the finite set of extended-persistent
(S₀-level) types. For B ∈ 𝒫 write F_B := P(a_{m_B}) \ Q (⊆ S) and B_can := ρ(m_B) (the
canonical witness's own extended type).

**Statement.**
(0) B_can = B ∪ F_B exactly (not merely ⊇).
(i) For disjoint persistent base types A, B ∈ 𝒫, every extended-persistent A' ∈ 𝒫'
    refining A (A' ∩ Q = A) satisfies A' ∩ F_B ≠ ∅, hence A' ∩ B_can ≠ ∅.
(ii) Symmetrically, every extended-persistent B' ∈ 𝒫' refining B satisfies
    B' ∩ A_can ≠ ∅.

**Proof.**
(0) ρ(m_B) = P(a_{m_B}) ∩ S₀ = (P(a_{m_B})∩Q) ∪ (P(a_{m_B})∩(S₀\Q)) = τ(m_B) ∪
(P(a_{m_B})\Q ∩ S₀) = B ∪ (F_B ∩ S₀). Since F_B ⊆ S ⊆ S₀ by definition of S as a union
including the B-term F_B, F_B ∩ S₀ = F_B. So ρ(m_B) = B ∪ F_B, and this union is disjoint
(B ⊆ Q, F_B ∩ Q = ∅ by definition), giving equality with no cancellation.

(i) Fix n > N_1 (Finite Core Theorem's threshold, enlarged if needed so it also exceeds
the Persistent-Type/Extended-Type pigeonhole thresholds — only finitely many indices are
excluded, harmless since A' ∈ 𝒫' still occurs infinitely often) with ρ(n) = A' (exists
since A' is extended-persistent). Then τ(n) = ρ(n) ∩ Q = A' ∩ Q = A. By the Bounded
Witness Lemma applied with witness m = m_B (valid: τ(m_B) = B, and A, B disjoint,
m_B ≤ N_1 < n), a_n is divisible by some prime p ∈ F_{A,B} = P(a_{m_B}) \ Q = F_B (this
set depends only on the witness m_B, i.e. only on B, not on A — established already in
`bounded-witness-lemma.md`). Since p | a_n and p ∈ F_B ⊆ S ⊆ S₀, p ∈ P(a_n) ∩ S₀ = ρ(n) =
A'. So p ∈ A' ∩ F_B, proving A' ∩ F_B ≠ ∅; since F_B ⊆ B_can (part 0), A' ∩ B_can ≠ ∅.

(ii) Identical with the roles of A, B exchanged. ∎

**Scope (must be stated explicitly).** This Lemma closes the pairwise-intersection
requirement (†) ONLY for pairs (A', B') ∈ 𝒫' × 𝒫' with disjoint base types where **at
least one side equals its own base type's canonical refinement** (A' = A_can or
B' = B_can). It says NOTHING about pairs where BOTH sides are non-canonical refinements
("rogue pairs") — for such pairs (†) remains open. A concrete example (a_1 = 175, base
types {5} vs {7}, non-canonical refinements {3,5} and {2,7}) shows the residual rogue
case is not vacuous in general (see `current.md`, "Independent verification, round 3").

**Status.** Correct, complete, no gaps, unconditional. Does NOT resolve gap (†) in
general; strictly narrows it.
