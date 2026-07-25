# Certified lemmas E1, E2(⇒), E3 (round 2)

Source: `redundant-constraint-antichain` §9. Reviewer-verified round 2 (proofs re-derived by
hand + numerically checked for a₁ ∈ {105,375,385,1155}: E1 = A∩[a₁,∞) matches the term set
exactly; E2 = each minimal support is a ⊆-minimal transversal of 𝓐_∞; E3 = private witness
G_p with G∩G_p={p} exists for every (G,p)). All UNCONDITIONAL (do NOT assume the Crux).

Notation: F(x)={primes|x}, F_n=F(a_n), 𝓕={F_n}, 𝓐_∞ = ⊆-minimal elements of 𝓕,
A := {c≥1 : c meets every F∈𝓐_∞}, s(x)=min{c∈A:c>x}. Uses certified L1–L4 and the
no-transient/fixed-successor identity a_{n+1}=s(a_n).

## E1 (Enumeration). {a_n : n≥1} = A ∩ [a₁,∞).
*Proof.* (⊆) Every term a_k∈A (no-transient lemma) and a_k≥a₁ (monotonicity). (⊇) Let c∈A,
c≥a₁. Since a_n→∞, n:=max{n:a_n≤c} exists (a₁≤c) and a_{n+1}>c. If a_n<c then c∈A, c>a_n, so
a_{n+1}=s(a_n)≤c, contradicting a_{n+1}>c. Hence a_n=c, a term. ∎

Corollary: any m≥a₁ with m∈A is a term, and F(m) is a genuine member of 𝓕.

## E2 realization preliminary. If a finite prime-set B meets every G∈𝓐_∞, then every m≥a₁
with F(m)=B lies in A, hence is a term with support B.
*Proof.* For each j, F(a_j) ⊇ some G'∈𝓐_∞ (domination). B meets G'⊆F(a_j), so F(m)=B meets
F(a_j), i.e. gcd(m,a_j)>1. Thus m∈A; E1 makes m a term. (m=(∏B)^k, k large, realizes any B.) ∎

## E2(⇒). Every G∈𝓐_∞ is a ⊆-minimal transversal of 𝓐_∞.
*Proof.* Transversal: G=F(a_i); for G'∈𝓐_∞ take term a_j with F(a_j)=G'; G∩G'≠∅ (L4 if i≠j;
nonempty supports if i=j). Minimality: if B⊊G were a transversal, the preliminary realizes B as
a term's support ⊊ G, contradicting G ⊆-minimal in 𝓕. ∎
(NOT settled / not needed: that every minimal transversal is automatically finite.)

## E3 (Private-witness distance). For G∈𝓐_∞ and p∈G there is G_p∈𝓐_∞ with G∩G_p={p}; hence
two distinct terms t,t' with F(t)=G, F(t')=G_p, gcd(t,t')=p^m, so p | (t−t') and p ≤ |t−t'|.
*Proof.* By E2(⇒) G is a minimal transversal, so G∖{p} is not a transversal: some G_p∈𝓐_∞ has
(G∖{p})∩G_p=∅. G transversal ⇒ G∩G_p≠∅, so G∩G_p={p}. Realize G,G_p as terms t,t' (members of
𝓕); distinct since G≠G_p. F(t)∩F(t')={p} ⇒ gcd=p^m; L3 gives p≤|t−t'|. ∎

## Reduction (immediate). The Crux (𝓐_∞ finite) ⟺ the primes occurring in ⊆-minimal supports
are bounded. (⇐: G⊆{primes≤B} finite; ⇒: Π=⋃𝓐_∞ finite is bounded.) OPEN: the a₁-anchored
bound q≤a₁ on those primes (equivalently on the E3 witness distances) is NOT proved.
