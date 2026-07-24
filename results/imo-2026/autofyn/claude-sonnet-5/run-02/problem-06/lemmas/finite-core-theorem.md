## Theorem: Finite Core Theorem (certified)

**Source.** `covering-system-construction`, Step 3. Depends only on
`bounded-witness-lemma.md` and `persistent-type-pigeonhole.md`.

**Statement.** Let 𝒫 be the (finite, nonempty) set of persistent types and N_0 the
threshold of `persistent-type-pigeonhole.md`. For each B ∈ 𝒫, fix the witness index
m_B := the smallest index n > N_0 with τ(n) = B (exists since B is persistent). Define

  S := ⋃_{B ∈ 𝒫} (P(a_{m_B}) \ Q),

a finite union of finite sets, hence finite, and N_1 := max(N_0, max_{B∈𝒫} m_B). Then
for every n > N_1 and every B ∈ 𝒫 with B ∩ τ(n) = ∅, a_n is divisible by some prime of
S.

**Proof.** Apply the Bounded Witness Lemma with A = τ(n) (persistent since n > N_0)
and witness m = m_B (valid since τ(m_B) = B by construction, and m_B ≤ N_1 < n). It
gives a_n divisible by some prime of F_{τ(n),B} = P(a_{m_B}) \ Q ⊆ S. ∎

**Status.** Correct, complete, no gaps. Gives an explicit finite bound on the core
prime pool, |S| ≤ Σ_{B∈𝒫} ω(a_{m_B}), with no growth-rate or density argument needed.

**Caveat for downstream use.** This theorem shows that for each n > N_1 and each
disjoint persistent type B, *some* prime of S links a_n to type B — but it does NOT
show that the same S-prime (or the same subset of S) works simultaneously across all
such B for a fixed n, nor that the "extended type" ρ(n) := P(a_n) ∩ (Q ∪ S) is
eventually confined to a small, pairwise-intersecting family. That further claim
(labelled (†) in `covering-system-construction`) is the open gap; it is NOT established
by this theorem and must not be assumed by any approach importing this lemma.
