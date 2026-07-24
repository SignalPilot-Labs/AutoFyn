## Lemma: Monotonicity of Resolution (certified)

**Source.** `covering-system-construction`, round 5, Step 7. Independently re-verified
by the proof-reviewer (round 5) — a short, direct, self-contained proof.

**Depends on (certified).** Nothing beyond the definitions of extended type
ρ(n) := P(a_n) ∩ S for a fixed finite S ⊇ Q.

**Statement.** Let S₀ ⊆ S₁ be finite sets of primes with Q ⊆ S₀, and let ρ, ρ₁ be the
corresponding extended-type maps (ρ(n) := P(a_n) ∩ S₀, ρ₁(n) := P(a_n) ∩ S₁). If
A', B' are S₀-extended-persistent types with A' ∩ B' ≠ ∅, then every pair of
S₁-extended-persistent types A'', B'' with A'' ∩ S₀ = A' and B'' ∩ S₀ = B' also
satisfies A'' ∩ B'' ≠ ∅.

**Proof.** Since S₀ ⊆ S₁, for every n, ρ(n) = P(a_n) ∩ S₀ = (P(a_n) ∩ S₁) ∩ S₀ =
ρ₁(n) ∩ S₀. Fix p ∈ A' ∩ B' (exists by hypothesis; p ∈ S₀ since A', B' ⊆ S₀). Since
A' = A'' ∩ S₀, p ∈ A' ⊆ A''; since B' = B'' ∩ S₀, p ∈ B' ⊆ B''. So p ∈ A'' ∩ B'' ≠ ∅. ∎

**Scope.** Shows resolution of a pair, once achieved at any stage of the recruitment
process (enlarging the core prime set S₀ → S₁ → ...), is permanent — it cannot be
undone by any later recruitment round. Used as the closing step of `covering-system-
construction`'s Conditional Single-Pair / Simultaneous Resolution Theorems (both still
conditional on the unproved "Universal Singleton Hypothesis" — NOT certified as
unconditional lemmas; see current.md).

**Status.** Correct, complete, no gaps, unconditional. Certified as a standalone
reusable lemma. Independently re-derived and checked by the reviewer (round 5);
matches the file's proof exactly.
