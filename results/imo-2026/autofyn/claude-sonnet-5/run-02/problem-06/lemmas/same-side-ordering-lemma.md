## Lemma: Same-Side Ordering (certified)

**Source.** `witness-index-descent`, round 5. Independently re-verified by the
proof-reviewer (round 5) — a short, direct, self-contained proof.

**Depends on (certified).** Only the definitions of base type τ(n) := P(a_n) ∩ Q,
extended type ρ(n) := P(a_n) ∩ S₀, and the literal-minimal-witness convention
(m_B := min{n ≥ 1 : τ(n) = B}, the GLOBAL earliest occurrence, consistent with the
convention already used throughout the Finite Core Theorem / Generalized Bounded
Witness Lemma / Lemma G proofs).

**Statement.** Let A' be any S₀-extended-persistent type refining base type A
(A' ∩ Q = A), and let n_{A'} := min{n : ρ(n) = A'}. Let m_A := min{n : τ(n) = A} (the
global earliest occurrence of base type A). Then n_{A'} ≥ m_A.

**Proof.** Every n with ρ(n) = A' satisfies τ(n) = ρ(n) ∩ Q = A' ∩ Q = A, so
n ∈ {n : τ(n) = A}. Since m_A is the minimum of this same set and n_{A'} is a
particular element of it, n_{A'} ≥ m_A. ∎

**Scope.** Gives the "same-side" half of a natural ordering comparison between
canonical (base-type) witnesses and extended-type witnesses. Does **not** give the
"cross" inequalities (n_{A'} ≥ m_B, n_{B'} ≥ m_A for a disjoint partner B), which
remain open and are, per the source file's own analysis, not actually needed by the
certified Lemma G (whose shared-prime conclusion via Free Facts holds for every pair of
indices regardless of relative order).

**Status.** Correct, complete, no gaps, unconditional. Certified as a standalone
reusable lemma for any approach doing witness-index bookkeeping between base and
extended types. Independently re-derived and checked by the reviewer (round 5); matches
the file's proof exactly.
