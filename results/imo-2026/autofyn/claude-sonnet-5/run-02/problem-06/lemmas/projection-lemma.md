## Lemma: Projection Lemma (certified)

**Source.** `covering-system-construction`, round 6, Step 8.1. Independently
re-verified by the proof-reviewer (round 6) — pure set-theoretic identity, no
computational content to check.

**Depends on (certified).** Nothing beyond the definitions of extended type
ρ(n) := P(a_n) ∩ S₀ for a fixed finite S₀ ⊇ Q.

**Statement.** Let S₀ ⊆ S₁ be finite sets of primes with Q ⊆ S₀, and let
ρ(n) := P(a_n) ∩ S₀, ρ₁(n) := P(a_n) ∩ S₁. Suppose A'' ⊆ S₁ is S₁-extended-persistent
(ρ₁(n) = A'' for infinitely many n). Then:
  (i) A' := A'' ∩ S₀ is S₀-extended-persistent;
  (ii) A' ∩ Q = A'' ∩ Q (the base type is unchanged by projection).

**Proof.** Since S₀ ⊆ S₁, for every n, ρ(n) = P(a_n) ∩ S₀ = (P(a_n) ∩ S₁) ∩ S₀ =
ρ₁(n) ∩ S₀ (pure set identity: X ∩ S₀ = (X ∩ S₁) ∩ S₀ whenever S₀ ⊆ S₁). Fix any n
with ρ₁(n) = A''; then ρ(n) = A'' ∩ S₀ = A' — the same fixed set for every such n.
Since infinitely many such n exist, ρ(n) = A' for infinitely many n, proving (i). For
(ii): A' ∩ Q = (A'' ∩ S₀) ∩ Q = A'' ∩ (S₀ ∩ Q) = A'' ∩ Q, using Q ⊆ S₀. ∎

**Scope.** The "downward" counterpart of the identity already used inside the
certified Monotonicity of Resolution Lemma's proof; isolated here because the
Collateral-Safety Theorem needs it in the opposite direction (S₁-persistent implies
S₀-persistent parent, rather than S₀-persistent implies some S₁-refinement
persistent). Logically independent of Monotonicity — neither subsumes the other.

**Status.** Correct, complete, no gaps, unconditional. Certified as a standalone
reusable lemma. Independently re-derived and checked by the reviewer (round 6);
matches the file's proof exactly.
