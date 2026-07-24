## Lemma: Vacuous FAH under 2 | a_1 Corollary (CERTIFIED, round 20)

**Source.** `n1-periodicity-reconciliation`, round 20, §4.1 (content
unchanged since first written round 16, formally certified this round).
Independently re-derived by the round-20 proof-reviewer.

**Depends on (certified).** The Uniform Evenness fact from
`even-seed-literal-periodicity-theorem.md` (`2 | a_1 ⟹ 2 | a_n` for every
`n ≥ 1`, by strong induction: `a_n+1` illegal by consecutive-integer
coprimality, `a_n+2` legal against every even `a_1,…,a_n`, so
`a_{n+1}=a_n+2` exactly).

**Statement.** If `2 | a_1`, then for every finite core `S ⊇ Q`, every two
elements of `𝒫'(S)` intersect (in fact every two `S`-extended types
intersect, whether or not their base types are disjoint) — in particular
(H1)/FAH holds automatically ("vacuously") at every core in the absorption
chain.

**Proof.** By Uniform Evenness, `2 | a_n` for every `n ≥ 1`. Since `2 | a_1`,
`2 ∈ Q ⊆ S` for any core `S ⊇ Q`. So `2 ∈ P(a_n) ∩ S = ρ_S(n)` for every
`n`. Hence for any `A', B' ∈ 𝒫'(S)` (each realized as `ρ_S(n)` for some `n`),
`2 ∈ A' ∩ B'`, so `A' ∩ B' ≠ ∅`. ∎

**Status.** Correct, complete, unconditional given `2 | a_1`. Low practical
priority since the sibling `even-seed-literal-periodicity-theorem.md`
already fully and unconditionally solves this entire subfamily by an
independent, stronger, elementary argument that bypasses the S₀/S*/FAH
machinery altogether — this corollary is recorded as a standing
simplification for any future round that revisits H1 restricted to even
seeds specifically within the general S₀/FAH framework.

**Companion negative finding (documented, not separately certified,
diagnostic only, matches the Lemma F/Lemma I precedent).** The same
mechanism does NOT trivialize (H2): self-absorption requires the ENTIRE
factorization `P(a_j) ⊆ S` for every `j ≤ N(S)`, a categorically stronger
condition than "shares the single prime 2 with `S`" — a generic even `a_j`
acquires odd prime factors outside any fixed finite core, so `2 | a_1` alone
supplies no mechanism forcing chain termination. H2 remains entirely open,
including for even `a_1`.
