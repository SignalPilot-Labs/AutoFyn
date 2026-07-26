# fixpoint-attractor — least-fixpoint / co-inductive winning region

## Status
partial

## Approaches tried
- Least-fixpoint characterization of the winning region W (this file) — framing the game as an AND-OR fixpoint; both directions re-proved via fixpoint identity. Same core facts as mod-theta-descent, different proof structure.

## Current best
A fixpoint identity: W = {triples with a θ-multiple} when θ = 180/N is a unit fraction (and this set = all triples under the create-move); and the complement C = {no θ-multiple} is a greatest-fixpoint (Shan-Yu trap) when θ is not a unit fraction.

## Target (whole problem)
Same full characterization: Mulan wins ⇔ θ = 180°/N, N ∈ ℤ_{≥2}.

## Technique
Co-induction / greatest-fixpoint (dual of the AND-OR game recursion). Invariant/monovariant KB; the AND-OR game fixpoint is the formal workhorse (matches the BFS that produced the conjecture).

## Skeleton

Define W ⊆ 𝒯 (the set of all valid triangles) as the LEAST fixpoint of the operator
  F(S) = {T ∈ 𝒯 : T has an angle = θ} ∪ {T ∈ 𝒯 : ∃ a move (vertex, γ) such that BOTH children ∈ S}.
T ∈ W ⇔ Mulan has a finite forced win from T (standard AND-OR game semantics: she needs a move where Shan-Yu cannot escape). Mulan guarantees victory from every start ⇔ W = 𝒯.

Dually, the LOSING region L = 𝒯 \ W is the GREATEST fixpoint of
  G(Q) = {T ∈ 𝒯 : T has no angle = θ AND ∀ moves (vertex, γ), ∃ a child ∈ Q}.
T ∈ L ⇔ Shan-Yu can keep T away from θ forever (co-inductive: T is losing if even after Mulan's best move, some child remains losing).

### IF direction (θ = 180/N): W = 𝒯.

Prove by showing M := {triples with a θ-multiple} ⊆ W, then M = 𝒯 (create-move makes every triple land in M).

- **Base.** Any T with an angle = θ is in F(∅) ⊆ W.
- **Induction on k.** Any T with an angle = kθ (k ≥ 2) is in W: Mulan splits that angle with γ = θ; child1 has θ (∈ W by base), child2 has (k−1)θ. By (strong) induction on k, child2 ∈ W. So T ∈ F(W) = W.
- **Create-move lifts.** Any T with NO θ-multiple is in W: Mulan plays γ = θ − (Y mod θ) at the max-angle vertex (validity as in mod-theta-descent); both children acquire a θ-multiple at P, so both children ∈ M ⊆ W by the previous bullet. Hence T ∈ F(W) = W.
- Since every T is either θ-multiple-free (in W by create-move) or has a θ-multiple (in W by induction), W = 𝒯.

### ONLY direction (θ not a unit fraction): L ⊋ ∅, in fact C := {no θ-multiple} ⊆ L.

Show C is a G-fixpoint: T ∈ C (no θ-multiple, in particular no angle = θ) AND for every Mulan move, some child stays in C. The latter is exactly the mod-θ four-case obstruction (no γ makes BOTH children acquire a θ-multiple, so at least one child ∈ C). Hence C ⊆ G(C); by coinduction C ⊆ L = greatest fixpoint. So W ⊆ 𝒯 \ C ⊊ 𝒯. Mulan does not win from any start in C.

Since C ≠ ∅ (generic initial triangle, as in mod-theta-descent), Mulan cannot guarantee victory.

### Conclusion
W = 𝒯 ⇔ θ is a unit fraction of 180° (θ = 180/N). Both directions reduce to the two load-bearing facts: the create-multiple move (IF) and the four-case obstruction (ONLY).

## Key lemmas (claim + mechanism)
- **W-fixpoint identity:** W = 𝒯 when θ = 180/N — because the create-move sends every θ-multiple-free triple into two θ-multiple children (membership in W by the k-induction).
- **C-greatest-fixpoint:** C = {no θ-multiple} is G-closed when 180 mod θ ≠ 0 — because the four-case residue chase shows every Mulan move leaves some child θ-multiple-free.
- **AND-OR semantics:** T ∈ W ⇔ finite forced win — standard combinatorial-game theory (recursion on the game tree with bounded depth here, since the k-descent terminates in ≤ N−1).

## Open gaps (builder fills)
1. **Justify the fixpoint recursion terminates / is well-founded** in the IF direction: the k-induction is on k ∈ {1,…,N−1}, finite; but the create-move could in principle be re-invoked after a descent (it is not — once a multiple is created we only descend — write this explicitly).
2. **Co-induction soundness in the ONLY direction:** the "greatest fixpoint = losing region" is a coinductive principle; state the (standard) justification that membership in G-fixpoint ⟹ Shan-Yu strategy, i.e. extract Shan-Yu's choice function "keep the C-child" explicitly.
3. The create-move validity and four-case obstruction are imported from mod-theta-descent (same gaps).

## Cases to cover
Same casework as mod-theta-descent (θ > 90, θ = 90, θ < 60 unit fraction vs not).

## Watch out for
- This framing is the SAME core proof as mod-theta-descent, re-skinned in fixpoint language. It is diversity insurance: if the reviewer finds a flaw in the direct prose of mod-theta-descent, the fixpoint formalization may surface it differently. But they share the create-move + four-case load-bearing facts — a shared wall. If that wall breaks, both die.
- Do NOT over-claim the BFS computation as proof; the fixpoint identity above replaces it.
