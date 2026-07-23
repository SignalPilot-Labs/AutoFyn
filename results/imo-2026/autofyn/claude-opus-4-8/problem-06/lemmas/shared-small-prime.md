# Certified shared lemmas — imo-2026-06 (reviewer-certified, round 2, from descent-shared-prime)

Setup (imported from `bounded-gaps-and-clique.md`): a₁>1 integer; for n≥1,
a_{n+1}=min{ m>a_n : gcd(m,a_i)>1 ∀ i≤n }. S_i=supp(a_i) is a **clause**; "m hits S"
iff supp(m)∩S≠∅. A_n={m≥1 : m hits S_i ∀ i≤n}; A=⋂_n A_n. A prime is **small** if
≤ a₁, **big** if > a₁; G={primes ≤ a₁} (finite). σ(S)=S∩G is the **small shadow**.
A clause C is **minimal** if no clause is a proper subset of it.

These certify the round-2 descent that closes the finiteness crux. All proofs verified
by the proof-reviewer (re-derived from scratch; Lemma S4 bound and both descent cases
checked; Lemma S′ confirmed 0 violations for a₁∈{15,35,77,143,210,255,385,1001,2310,4199}).

## Lemma S4 (bounded small-only companion) — CERTIFIED
If a clause S_j has a big prime factor and σ(S_j)≠∅, put R=∏_{p∈σ(S_j)}p, p₀=min σ(S_j),
and let n≥0 be least with x:=p₀ⁿR ≥ a₁. Then supp(x)=σ(S_j) and a₁ ≤ x < a_j.
Proof: p₀|R ⇒ supp(x)=supp(R)=σ(S_j); x≥a₁ by choice of n. Let q>a₁ be a big prime of
a_j; R and q are distinct primes each dividing a_j, so Rq | a_j, Rq ≤ a_j (⋆). If n=0:
x=R ≤ a_j/q < a_j. If n≥1: minimality gives p₀^{n−1}R < a₁, so x=p₀·(p₀^{n−1}R) < p₀a₁
≤ Ra₁ < Rq ≤ a_j (using p₀≤R, a₁<q, (⋆)). ∎

## Lemma S′ (any two clauses share a small prime) — CERTIFIED
For all i,j the set S_i∩S_j contains a prime ≤ a₁.
Proof (minimum-height violating-pair descent). Call {S_j,S_k}, j<k, **violating** if all
primes of S_j∩S_k are big (S_j∩S_k≠∅ by Tool 2); "height" k. If any violating pair exists,
take one of minimum height k. Then j≥2 and S_j has a big prime (S₁⊆G, so no pair with
index 1 is violating), and σ(S_j)∩S_k=∅. Apply Lemma S4 to S_j: get x, supp(x)=σ(S_j),
a₁≤x<a_j; then gcd(x,a_k)=1.
- Case A: x is a term a_m. Then S_m=σ(S_j); m<k (a_m=x<a_j<a_k), so gcd(a_m,a_k)>1 (Tool 2),
  i.e. S_m∩S_k≠∅ — contradicts σ(S_j)∩S_k=∅.
- Case B: x not a term. Then x>a₁ (a₁ is a term), so x∉A (Sub-lemma E). Pick s with
  a_s<x<a_{s+1}, 1≤s≤j−1 (x<a_j). x∉A_s (else x∈A_s∩(a_s,∞), x<a_{s+1}=min, contra). Let t
  least with x∉A_t; then supp(x)∩S_t=∅, t≤s≤j−1<k. So σ(S_j)∩S_t=∅, and (Tool 2) any
  r∈S_t∩S_j is big (small r would be in σ(S_j)∩S_t=∅). Thus {S_t,S_j} is violating of
  height j<k — contradicts minimality.
Both impossible ⇒ no violating pair ⇒ Lemma S′. ∎

## Prop 1′ (small shadow of a minimal clause) — CERTIFIED
Assuming Lemma S′, every minimal clause C ⊆ G (i.e. C=σ(C)).
Proof: C=S_i has a prime ≤P₁≤a₁ (Tool 1), so C′:=σ(C)≠∅. For any clause D, Lemma S′ gives
a small prime p∈C∩D; p∈C′∩D, so C′ hits D. C′ nonempty & hits every clause ⇒ (Cor E.1) C′
is a clause; C′⊆C minimal ⇒ C′=C ⇒ C⊆G. ∎

## Consequence — CERTIFIED
Every minimal clause ⊆ G (finite) ⇒ finitely many minimal clauses ⇒ (certified finish
package) A periodic mod M=∏_{p∈⋃ minimal clauses}p, A_n=A for n≥N, hence a_{n+T}=a_n+L
for all n with T=|A mod M|, L=M. This closes imo-2026-06.
