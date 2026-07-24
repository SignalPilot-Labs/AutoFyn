## Lemma: Persistent-Type Pigeonhole (certified)

**Source.** Independently derived in both `amortized-charging-budget` (Lemma 3,
"recurrent pattern") and `covering-system-construction` (Step 1, "persistent types").
Certified as a single shared lemma; use whichever name fits the importing approach.

**Statement.** Let Q := P(a_1) (finite, since a_1 is a fixed positive integer), and for
n ≥ 1 define τ(n) := P(a_n) ∩ Q, a nonempty subset of Q (nonempty by the Free Facts
lemma). Then:
(a) There is a nonempty A ⊆ Q such that {n : τ(n) = A} is infinite (call such A
*persistent*; let 𝒫 be the finite, nonempty set of all persistent types).
(b) There is an index N_0 such that τ(n) ∈ 𝒫 for every n > N_0.

**Proof.** (a) τ maps the infinite index set into the finite set 2^Q \ {∅} of size
2^{|Q|} − 1; by the infinite pigeonhole principle (`knowledge_base.md`, "Pigeonhole /
extremal principle"), some value is attained infinitely often. (b) Every type in
𝒯 \ 𝒫 (𝒯 := 2^Q \ {∅}) occurs, by definition of "not persistent," only finitely often;
𝒯 \ 𝒫 is a finite set of types, so the total number of indices n with τ(n) ∉ 𝒫 is a
finite sum of finitely many finite quantities, hence finite; let N_0 be the largest
such index (or 0 if none). ∎

**Status.** Correct, complete, no gaps. Elementary pigeonhole; reusable.
