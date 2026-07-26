# Approach: covering-system-redundancy

## Status
unsolved

## Framing
Reframe the allowed set A_n = ∩_{i≤n} ∪_{p|a_i} pZ as the COMPLEMENT OF A COVERING SYSTEM (the forbidden set is a union of residue classes "non-coprime to a_i"). Prove that beyond a finite essential set of primes, every late prime's forbidden-class is REDUNDANT mod a fixed L (its residue classes are already covered by the essential primes). Then A_n mod L stabilizes and the residue walk is eventually periodic.

## Target
Prove ∃ T,L>0 with a_{n+T}=a_n+L for all n.

## Technique
Covering systems / complement-of-cover + redundancy argument; finite-state pigeonhole mod L. Per knowledge_base "Modular arithmetic/CRT", "Pigeonhole/extremal". (Mirsky–Newman is NOT in knowledge_base — cannot cite; re-prove any covering-system step.)

## Skeleton
1. **Sieve reformulation.** A_n = ∩_{i≤n} ∪_{p|a_i} pZ = {m : ∀ i≤n, ∃ p|a_i with p|m} = integers non-coprime to every prior term. a_{n+1} = min(A_n ∩ (a_n, ∞)). A_n is periodic mod R_n = rad(∏_{i≤n} a_i) = product of all distinct primes seen so far. — by definition (each ∪_{p|a_i}pZ is periodic mod rad(a_i); intersection periodic mod lcm = R_n).
2. **R_n → ∞ (the obstacle).** The set of all primes appearing is INFINITE (proven for a_1=15 via a_{8k+6}=6(6+5k)). So R_n grows without bound; A_n's period grows. Cannot directly fix L. — known dead fact.
3. **Essential prime set (covering-theoretic).** A prime q appearing at stage n is REDUNDANT if removing the constraint ∪_{qZ} (when q is the only prime of some a_i NOT already covered) leaves A_n mod (current candidate L) unchanged. The NON-redundant primes are the essential set E. E ⊆ primes ≤ (max of frozen prefix). — mechanism: a prime is essential only if it is the unique shared prime with some earlier term (same as essential-monovariant's dichotomy).
4. **Redundancy of late primes (the crux).** Prove: there exists a finite E and a stage N such that for all n ≥ N, every prime q appearing at stage n with q ∉ E is redundant — its forbidden class ∪_{qZ} (restricted to mod L = ∏_{p∈E} p) is already contained in ∪_{p∈E,f∈F} (pZ) mod L. Mechanism: a late prime q divides a_n; a_n's REDUCED type (P(a_n)∩E) is already a transversal of the stabilized family (it hits every earlier a_i via an E-prime); so q is only ever a co-factor alongside an E-prime, never the unique shared prime. Hence q's constraint adds nothing.
5. **A_n mod L stabilizes.** Once all late primes are redundant, A_n mod L = A_N mod L =: A_∞ for all n ≥ N. A_∞ is a fixed finite union of residue classes mod L. — by step 4 + definition.
6. **Deterministic residue walk.** a_{n+1} = min{m > a_n : m mod L ∈ A_∞} for n ≥ N. The map φ: A_∞ → A_∞ (next residue in A_∞ above current) is well-defined and deterministic. — by step 5 + translation-equivariance of "next residue above".
7. **Eventual periodicity.** r_n = a_n mod L follows φ on finite A_∞ ⇒ eventually periodic, period T. — pigeonhole.
8. **Lift.** Sum of gaps over period T = L ⇒ a_{n+T} = a_n + L for n ≥ N. — telescoping.
9. **Transient / "for all n".** Same load-bearing ambiguity: if the problem requires "for all n ≥ 1" literally, absorb the transient by re-indexing or enlarging T,L. Builder must resolve.

## Key lemmas (claim + one-line mechanism)
- **Lemma A (A_n is periodic mod R_n):** the intersection of finite unions of APs is periodic mod their lcm — by CRT / lcm structure of residue-class unions.
- **Lemma B (late primes redundant) — the crux:** every prime q appearing after stage N with q∉E has its constraint already implied mod L — because q always co-occurs with an E-prime (q is never the unique shared prime with an earlier term, by the free-rider dichotomy: a newly introduced prime divides no earlier term). This is the covering-theoretic form of the free-rider dichotomy.
- **Lemma C (E is finite):** E ⊆ primes ≤ (max of the frozen prefix) — because an essential prime must be the unique shared prime with an earlier term a_i, and that a_i is a concrete finite integer, so p ≤ a_i ≤ (frozen prefix max). The frozen prefix is finite, so E is finite.

## Open gaps
- Step 4 / Lemma B: the redundancy claim must be written rigorously. The subtle point: a late prime q divides a_n (late), and a_n's reduced type (P(a_n)∩E) hits every earlier a_i via an E-prime — but does this mean q's CONSTRAINT (∪qZ) is redundant mod L? The constraint from a_n is ∪_{p|a_n} pZ ⊇ ∪_{p∈P(a_n)∩E} pZ, so the E-part already covers a_n's contribution. Yes — q only ever appears alongside E-primes in the same term, so removing q from that term's constraint loses nothing. Make this airtight.
- Step 3: E is defined via "unique shared prime" — must match the transversal framing. Verify consistency with the crude-reduced-type and essential-monovariant definitions of "essential."
- Step 9: transient resolution.

## Cases to cover
- Even a_1, prime-power a_1: E={2} resp. E={p}, A_∞ = {0} mod L, T=1. Machine handles.

## Watch out for
- Do NOT cite Mirsky–Newman or any covering-system theorem not in knowledge_base.md — re-prove.
- Distinguish THIS approach's contribution from crude-reduced-type: both end in finite-state mod L, but THIS approach proves the stabilization via covering-system REDUNDANCY (a late prime's forbidden class is already covered), whereas crude-reduced-type uses the transversal-family lattice stabilization. The redundancy argument is the distinct mechanism — keep it load-bearing.
- The "E finite" bound (Lemma C) uses "essential prime ≤ max of frozen prefix" — this is the SAME bound as essential-monovariant's step 3; verify it (the witness a_i is bounded by the frozen prefix, so p ≤ a_i). This is cleaner here because the frozen prefix is explicitly the stage-N segment.
