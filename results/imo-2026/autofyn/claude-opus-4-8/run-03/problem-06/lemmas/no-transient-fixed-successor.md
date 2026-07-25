# Lemma: No-transient / fixed-successor identity (CERTIFIED, round 1)

Source approach: `redundant-constraint-antichain` (§1 L4, §2 L5–L8).
Reviewer-verified round 1 (proof + numerical check on a_1=105: every term in A,
a_{n+1}=s(a_n) with no A-element skipped, |ρ(A)|=58).

## Setup
Greedy sequence a_1,a_2,… (positive ints >1), a_{n+1}=min{c>a_n : gcd(c,a_i)>1 ∀ i≤n}.
F(x)={primes | x}, F_n=F(a_n), 𝓕={F_n : n≥1}. Note gcd(x,y)>1 ⟺ F(x)∩F(y)≠∅.
"c meets F" means F(c)∩F≠∅.

## Prerequisite: Pairwise-intersecting (Lemma 4)
For all i≠j, gcd(a_i,a_j)>1 (i.e. F_i∩F_j≠∅).
*Proof.* For i<j, the defining property of a_j=a_{(j-1)+1} includes the clause i≤j−1
requiring gcd(a_j,a_i)>1. Symmetry gives all i≠j. ∎

## Statement
Let 𝓐_∞ = {⊆-minimal elements of 𝓕}, and A := {c≥1 : c meets every F∈𝓐_∞},
s(x):=min{c∈A : c>x}. Then:
1. (Domination) Every F_i contains some F∈𝓐_∞, hence A ⊆ A_n := {c : c admissible at stage n} for every n.
2. (Every term in A) a_k ∈ A for every k≥1.
3. (Fixed successor) a_{n+1}=s(a_n) for every n≥1.

## Proof
**(1)** For fixed i, {G∈𝓕 : G⊆F_i} is finite and nonempty, so has a ⊆-minimal element G;
G is minimal in all 𝓕 (any G'⊊G⊆F_i would lie in the set, contradicting minimality), so G∈𝓐_∞.
Redundancy: if c meets G⊆F_i then c meets F_i. Hence any c∈A meets every F_i (i≤n), so c∈A_n. Thus A⊆A_n.

**(2)** Fix F∈𝓐_∞; F=F_j for some j (elements of 𝓐_∞ are members of 𝓕). If j=k, a_k meets F_k
trivially (F_k≠∅). If j≠k, Lemma 4 gives F_k∩F_j≠∅. So a_k meets F. As F arbitrary, a_k∈A.

**(3)** A is unbounded (contains every a_k→∞), so s(a_n) exists.
(≤): s(a_n)∈A⊆A_n and s(a_n)>a_n, so s(a_n) is admissible >a_n, giving a_{n+1}≤s(a_n).
(≥): a_{n+1}∈A (by 2) and a_{n+1}>a_n; s(a_n) is the least A-element >a_n, so a_{n+1}≥s(a_n).
Hence a_{n+1}=s(a_n) for all n≥1. ∎

## Consequence (endgame, needs an external finiteness input)
If Π:=⋃_{F∈𝓐_∞}F is finite, put L₀=∏_{p∈Π}p. Then A is a union of residue classes mod L₀
(membership depends only on which p∈Π divide c), every multiple of L₀ is in A, and the sequence
enumerates {c∈A : c≥a_1} in increasing order. With T=|ρ(A)| (=#residues of A mod L₀) and L=L₀,
a_{n+T}=a_n+L for ALL n≥1. **This removes the usual "eventual periodicity ⇒ all n" step entirely.**

The finiteness of Π (the "Finite Alphabet" crux) is NOT proved here.
