# Certified shared lemmas — imo-2026-06 (reviewer-certified, round 1)

Setup: a₁>1 integer; for n≥1, a_{n+1} = min{ m > a_n : gcd(m,a_i)>1 ∀ i≤n }.
Write S_i = supp(a_i) (primes dividing a_i); "m hits S" iff supp(m)∩S ≠ ∅.
A_n = { m≥1 : m hits S_i ∀ i≤n }, so a_{n+1} = min(A_n ∩ (a_n,∞)); A = ⋂_n A_n.
P₁ = largest prime factor of a₁.

## Tool 1 (bounded gaps) — CERTIFIED
Every positive multiple of a₁ lies in every A_n; hence 0 < a_{n+1}−a_n ≤ a₁, the
sequence is well-defined and strictly increasing, a_n → ∞, and every term a_k has a
prime factor ≤ P₁.
Proof: gcd(a_i,a₁)>1 gives a prime p | a₁, p | a_i, so p ≤ P₁; if a₁ | m then p | m so
m hits S_i. Every interval (a_n, a_n+a₁] contains a multiple of a₁ (admissible), giving
the bound. The prime-factor claim is the p above with i=k. ∎

## Tool 2 (pairwise gcd; every term in A) — CERTIFIED
gcd(a_i,a_j)>1 for all i≠j (rule + symmetry of gcd). Hence each a_n hits every clause
S_j, so a_n ∈ A for every n≥1.

## Sub-lemma E (greedy takes all admissibles) — CERTIFIED
If w ∈ A and w > a₁ then w = a_j for some j.
Proof: terms strictly increase to ∞, pick j with a_{j−1} < w ≤ a_j; w ∈ A ⊆ A_{j−1} and
w > a_{j−1}, so by minimality a_j ≤ w, hence a_j = w. ∎
Cor E.1: a nonempty prime-set T that hits every clause is itself a clause (take a number
of support exactly T that is > a₁; it lies in A, so is a term by E).

## Finish package (stabilization ⇒ conclusion, for EVERY n) — CERTIFIED
Suppose A is a union of T := |A mod M| residue classes mod some M ≥ 2 and A_n = A for all
n ≥ N (equivalently: finitely many minimal clauses / A periodic). Then:
- a_{n+1} = min(A ∩ (a_n,∞)) for ALL n≥1. (a_{n+1} ∈ A by Tool 2 and > a_n gives ≥;
  A ⊆ A_n gives ≤.) This uses no finiteness crux.
- Since a₁ ∈ A, the sequence is exactly the increasing enumeration e₁<e₂<… of {x∈A: x≥a₁}
  with e₁=a₁ and a_n=e_n by induction.
- Each window (e_k, e_k+M] contains exactly T elements of A, the largest being e_k+M ∈ A;
  so e_{k+T} = e_k + M, i.e. a_{n+T} = a_n + M for every n≥1.
Hence T,L = M > 0 work. This finish is non-circular (periodicity of A is an input from the
crux, not assumed to prove itself) and off-by-one clean.

## sieve-closure Lemma 1 (vacuous-constraint / fixed-point) — CERTIFIED
If A_n is self-consistent (any two of its elements share a prime), then A_m = A_n for all
m ≥ n. Proof: a_{n+1} ∈ A_n; any m ∈ A_n shares a prime with a_{n+1}, so hits S_{n+1};
thus A_{n+1}=A_n, still self-consistent; induct. ∎

## sieve-closure Lemma 3 (strict density-drop monovariant) — CERTIFIED (but insufficient alone)
Call step n+1 effective if A_{n+1} ⊊ A_n. Then density d_n = |A_n mod M_n|/M_n satisfies
1 ≥ d_1 ≥ d_2 ≥ … ≥ 1/a₁, and each effective step drops d_n − d_{n+1} ≥ 1/M_{n+1} > 0.
(Note: does not bound the number of effective steps, since 1/M_{n+1} → 0.)

NOTE: These certify the FULLY-PROVED supporting steps only. The finiteness crux
(Lemma S / essential primes finite) is NOT certified — it remains an open gap.
