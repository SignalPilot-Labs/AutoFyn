## Status
solved

## Approaches tried
- **descent-shared-prime** (round 2): **SOLVED.** Imports the certified reduction and closes the finiteness crux by proving **Lemma S′** ("any two clauses share a prime ≤ a₁") via minimum-height violating-pair descent (companion integer x with supp(x)=σ(S_j) and a₁≤x<a_j, Lemma S4). Prop 1′ then forces every minimal clause ⊆ {primes ≤ a₁}, a finite ground set, so finitely many minimal clauses, and the certified finish gives a_{n+T}=a_n+L for all n. Reviewer re-derived Lemma S4's bound and both descent cases from scratch; verified Lemma S′ has 0 violations for a₁∈{15,35,77,143,210,255,385,1001,2310,4199}. **Complete and correct.**
- **clique-descent** (round 2): partial. Retargeted off the round-1 false Lemma S. Proves self-blocking-clutter Lemma 1, finite-ground-set Prop 2 (Q finite ⇒ 𝓜 finite; correct replacement of false Prop 1), and mutual-witness Lemma 3 (reconciliation map Φ:Q→disjoint shadow-pairs, finite image). Reduces the crux to "Q finite / Φ finite fibers." Honest gap; that gap is closed independently by descent-shared-prime.
- **sieve-closure** (round 1): reduced to "essential primes finite," same crux, different framing. Superseded.
- **finite-state-bijection** (round 1): not built.

## Current best
Complete proof, from descent-shared-prime. The certified reduction (Tools 1–2, Sub-lemma E/Cor E.1, finish package in `lemmas/bounded-gaps-and-clique.md`) turns the problem into the finiteness of minimal clauses; Lemma S′ (`lemmas/shared-small-prime.md`) closes it. See Full proof below.

## Full proof

Throughout, import the reviewer-certified results of `lemmas/bounded-gaps-and-clique.md`.

**Setup.** a₁>1; for n≥1, a_{n+1}=min{ m>a_n : gcd(m,a_i)>1 ∀ i≤n }. For a positive
integer m, supp(m) is its set of prime divisors; "m hits a prime-set S" iff supp(m)∩S≠∅.
S_i=supp(a_i) is the **clause** of a_i. A_n={m≥1 : m hits S_i ∀ i≤n}, so
a_{n+1}=min(A_n∩(a_n,∞)); A=⋂_n A_n. P₁ = largest prime factor of a₁. A prime is **small**
if ≤ a₁ and **big** if > a₁; G={primes ≤ a₁} (finite); σ(S)=S∩G is the **small shadow**.
A clause C is **minimal** if no clause is a proper subset of it.

Certified facts used verbatim:
- **Tool 1.** Every positive multiple of a₁ lies in every A_n; hence 0<a_{n+1}−a_n≤a₁, the
  sequence is strictly increasing with a_n→∞, and every term a_k has a prime factor ≤P₁≤a₁
  (so σ(S_k)≠∅).
- **Tool 2.** gcd(a_i,a_j)>1 for i≠j, so any two clauses intersect; every a_n∈A.
- **Sub-lemma E.** If w∈A and w>a₁ then w=a_j for some j.
- **Cor E.1.** A nonempty prime-set T hitting every clause is itself a clause.
- **Finish package.** If there are finitely many minimal clauses, then A is a union of
  T:=|A mod M| residue classes mod M:=∏_{p∈⋃ minimal clauses}p ≥2, A_n=A for large n, and
  there exist positive integers T,L=M with a_{n+T}=a_n+L for every n≥1.

### Step 1 — Reduction (Prop 1′). Lemma S′ ⇒ theorem.

> **Lemma S′.** Any two clauses share a small prime: for all i,j, S_i∩S_j contains a prime ≤a₁.

**Prop 1′.** *Assuming Lemma S′, every minimal clause C ⊆ G.* Let C=S_i be minimal;
C′:=σ(C)≠∅ by Tool 1. For any clause D, Lemma S′ gives a small prime p∈C∩D, so
p∈C′∩D and C′ hits D. Thus C′ is a nonempty prime-set hitting every clause; by Cor E.1 it is
a clause. As C′⊆C and C is minimal, C′=C, so C⊆G. ∎

Hence every minimal clause is a subset of the finite set G, so there are finitely many minimal
clauses (each nonempty, ≥1 of them since S₁ contains a minimal clause). Since (i) hitting all
minimal clauses is equivalent to hitting all clauses (every clause contains a minimal one, by
finiteness of clauses under ⊊) and (ii) each minimal clause C_t=S_{n_t}, we get A={m : m hits
every minimal clause}, a union of residue classes mod M=∏_{p∈⋃C_t}p; and for N=max n_t, any
m∈A_n with n≥N hits every C_t hence lies in A, so A_n=A for n≥N. The certified finish package
yields positive integers T=|A mod M|, L=M with a_{n+T}=a_n+L for every n≥1. It remains to prove
Lemma S′.

### Step 2 — Lemma S4 (bounded small-only companion).

> **Lemma S4.** If a clause S_j has a big prime factor and σ(S_j)≠∅, put R=∏_{p∈σ(S_j)}p,
> p₀=min σ(S_j), and let n≥0 be least with x:=p₀ⁿR ≥ a₁. Then supp(x)=σ(S_j) and a₁≤x<a_j.

*Proof.* p₀|R ⇒ supp(x)=supp(R)=σ(S_j); x≥a₁ by choice of n. Let q>a₁ be a big prime factor of
a_j. R (a product of distinct small primes of a_j) and q are distinct primes each dividing a_j,
so Rq | a_j and Rq ≤ a_j. (⋆) If n=0: x=R ≤ a_j/q < a_j. If n≥1: minimality gives p₀^{n−1}R<a₁,
so x=p₀·(p₀^{n−1}R) < p₀a₁ ≤ Ra₁ < Rq ≤ a_j (using p₀≤R, then a₁<q, then (⋆)). In both cases
a₁≤x<a_j. ∎

### Step 3 — Lemma S′ by minimum-height descent.

Call an unordered pair of clauses {S_j,S_k}, j<k, **violating** if every prime of S_j∩S_k is
big (S_j∩S_k≠∅ by Tool 2); its **height** is k. Lemma S′ ⟺ no violating pair exists. Suppose one
exists; take a violating pair (S_j,S_k), j<k, of **minimum height** k.

*(2a)* The shared big prime lies in S_j, so S_j has a big prime factor. Since S₁⊆G, no pair with
index 1 is violating, so j≥2. *(2b)* σ(S_j)∩S_k=∅ (a common small prime would violate).

By (2a) and Tool 1, apply Lemma S4 to S_j: obtain x with supp(x)=σ(S_j), a₁≤x<a_j. By (2b),
gcd(x,a_k)=1.

- **Case A: x=a_m is a term.** Then S_m=supp(x)=σ(S_j); and a_m=x<a_j<a_k gives m<k, so by Tool 2
  gcd(a_m,a_k)>1, i.e. S_m∩S_k≠∅ — contradicting σ(S_j)∩S_k=∅. Impossible.
- **Case B: x is not a term.** Since a₁ is a term, x>a₁; by Sub-lemma E, x∉A. As a₁<x<a_j and the
  terms increase, pick s with a_s<x<a_{s+1}, 1≤s≤j−1. If x∈A_s then x∈A_s∩(a_s,∞) with x<a_{s+1}=
  min(A_s∩(a_s,∞)) — contradiction; so x∉A_s. Let t be least with x∉A_t; then supp(x)∩S_t=∅ and
  t≤s≤j−1<k. Now σ(S_j)∩S_t=∅ (since supp(x)=σ(S_j)); by Tool 2, S_t∩S_j≠∅, and any r∈S_t∩S_j is
  big (a small r would lie in σ(S_j)∩S_t=∅). Hence {S_t,S_j} is violating of height j<k,
  contradicting the minimality of k. Impossible.

Both cases are impossible, so no violating pair exists: **Lemma S′ holds.** ∎

### Conclusion.

By Step 1 (Prop 1′ and finiteness) with Lemma S′ from Steps 2–3, there are finitely many minimal
clauses, all ⊆ G, and the certified finish package gives positive integers T=|A mod M| and
L=M=∏_{p∈⋃ minimal clauses}p with

  a_{n+T} = a_n + L  for every positive integer n.  ∎
