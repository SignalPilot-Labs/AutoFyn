## Lemma: Collateral-Safety Theorem (certified)

**Source.** `covering-system-construction`, round 6, Step 8.2. Independently
re-verified by the proof-reviewer (round 6).

**Depends on (certified).** `projection-lemma.md`, `monotonicity-of-resolution.md`.

**Definition (fully safe).** Let A, B ∈ 𝒫 be disjoint persistent base types. Say
(A,B) is **fully safe at S₀** if every pair of S₀-extended-persistent types A', B'
with A' ∩ Q = A, B' ∩ Q = B satisfies A' ∩ B' ≠ ∅ (no rogue extended-persistent
refinement pair at S₀).

**Theorem.** If (A,B) is fully safe at S₀, then (A,B) is fully safe at every
S₁ ⊇ S₀ (S₁ finite, Q ⊆ S₀ ⊆ S₁).

**Proof.** Let A'', B'' be any pair of S₁-extended-persistent types with
A'' ∩ Q = A, B'' ∩ Q = B. By the Projection Lemma, A' := A'' ∩ S₀ is
S₀-extended-persistent with A' ∩ Q = A, and B' := B'' ∩ S₀ is S₀-extended-persistent
with B' ∩ Q = B. Since (A,B) is fully safe at S₀ and A', B' are exactly a pair of
S₀-extended-persistent refinements of A, B, A' ∩ B' ≠ ∅. Applying the Monotonicity of
Resolution Lemma to A', B' (S₀-extended-persistent, A' ∩ B' ≠ ∅) and to A'', B''
(S₁-extended-persistent, with A'' ∩ S₀ = A' and B'' ∩ S₀ = B' by construction)
gives A'' ∩ B'' ≠ ∅. Since A'', B'' were arbitrary, (A,B) is fully safe at S₁. ∎

**Corollary (base-type pairs are fixed forever).** Since Q = P(a_1) never changes
and 𝒫 (the set of persistent base types) is defined purely at the Q-level, 𝒫 and the
finite list of disjoint base-type pairs {(A,B) : A,B ∈ 𝒫, A∩B=∅} (at most
C(|𝒫|,2) ≤ C(2^k−1,2) of them) are fixed once and for all at round 0 of the
recruitment process. Refinement (enlarging S₀) only changes which extended
refinements of a fixed base pair exist and whether they intersect; it never creates
or destroys a base-type pair.

**Consequence (reduction of gap (†), not separately certified as a lemma but
recorded here for context).** Defining open(k) := {(A,B) : not fully safe at
S₀^(k)} for the recruitment process's stage-k core S₀^(k), the Corollary above gives
open(k) ⊆ a FIXED finite set for all k, and the Theorem (contrapositive) gives
open(k+1) ⊆ open(k). Hence (†) holds iff open(k) = ∅ for some finite k — an exact
reduction to base-type-pair-level termination over a fixed finite index set. See
`current.md` for the full statement and its role in the remaining gap.

**Scope.** Closes round 5's "collateral rogue pairs" gap completely and
unconditionally: no dependence on the Universal Singleton Hypothesis, the
Full-Absorption Hypothesis, or any other unproved hypothesis — a structural fact
about the recruitment process itself.

**Status.** Correct, complete, no gaps, unconditional. Certified as a standalone
reusable lemma. Independently re-derived and checked by the reviewer (round 6);
matches the file's proof exactly.
