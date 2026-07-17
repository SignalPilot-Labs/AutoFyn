## Math Explorer Role Memory

ALWAYS: Run Python experiments on small cases for sequence-based number theory problems before writing the report — empirical data reveals structure that pure theory misses (imo-2026-06, round 1).

ALWAYS: For "prove periodicity" problems, check (a) whether the period is T = #admissible-residues mod M, (b) whether L = M (product of essential primes), and (c) whether periodicity holds from n=1 not just eventually (imo-2026-06, round 1).

ALWAYS: For greedy sequence problems, check if gcd(a_i, a_j) > 1 for ALL pairs (not just consecutive) — this stronger property often gives "no transient" / pure periodicity from n=1 (imo-2026-06, round 1).

ALWAYS: Report the distinct gap-boundedness bound empirically — often max gap << M, which hints at a tighter proof (imo-2026-06, round 1).

NEVER: Assume the essential prime set P equals primes(a_1) — for greedy gcd-sequence problems P can include primes not dividing a_1 (e.g., a1=35=5*7 gives P={2,3,5,7} including 2 and 3) (imo-2026-06, round 1).

ALWAYS: For "admissible set stabilizes" claims in gcd-sequence problems, the key criterion is the CLIQUE PROPERTY: once any two elements of A_n share a factor (A_n is a clique in the coprime graph), adding new sequence terms cannot shrink A_n further. Test this by verifying that the sequence term a_{n+1} satisfies gcd(m, a_{n+1}) > 1 for all m in A_n. (imo-2026-06, round 1).

ALWAYS: When a greedy gcd-sequence has T, L period from n=1 (not just eventually), check whether the first T terms cover ALL T residue classes mod L exactly once — this is the empirical mechanism for "for all n" (imo-2026-06, round 1).

NEVER: Assume the period holds eventually and try to extend to "all n" by choosing a large T' = k*T — the problem requires the same T from n=1, which requires showing the first T terms cover all residue classes (imo-2026-06, round 1).

ALWAYS: When scouting a "finite-state / gap-pigeonhole" bypass for an admissible-set-stabilization crux, verify first that proving eventual periodicity of the gap sequence is not equivalent to proving the admissible set stabilizes — if it is, the "bypass" collapses to the same crux (imo-2026-06, round 2).

ALWAYS: For "two objects share only a large prime" Lemma S cruxes, check the crux corpus under domain=number_theory, subtopic=divisibility-and-gcd for aimo-0030 — its minimal-counterexample + strip-large-primes (Claim 4) descent is the most direct analogue and the correct template to adapt (imo-2026-06, round 2).

ALWAYS: When the q-cofactor b = a_i/q^{v_q(a_i)} has b ≤ a_1 (the common case empirically), check whether supp(b) appears as a clause BEFORE index i — this is the empirical mechanism explaining why large primes are always in non-minimal clauses, and the proof should target this structural property rather than the "b > a_1" case (imo-2026-06, round 2).

ALWAYS: Before accepting a "key lemma" as the crux, TEST IT computationally on diverse starting values including composite a₁ with many prime factors (e.g., a₁ = 385 = 5·7·11 or a₁ = 2310 = 2·3·5·7·11) — Lemma S ("no two clauses share only a large prime") is FALSE for a₁ = 385 where a₅=399={3,7,19} and a₇=418={2,11,19} share only 19 > P₁=11 (imo-2026-06, round 2).

ALWAYS: When Lemma S fails (two clauses share only large prime q), check if those clauses form a MUTUAL-WITNESS PAIR: {q,S₁} is minimal because S₁ misses {q,S₂}, and {q,S₂} is minimal because S₂ misses {q,S₁}, with S₁∩S₂=∅. This mutual-dependency / sunflower-with-large-core structure is the real phenomenon and bounds the number of minimal clauses per large prime by π(P₁) (imo-2026-06, round 2).

NEVER: Use Lemma S as stated ("all minimal clauses ⊆ {primes ≤ P₁}") — it is FALSE for a₁ = 385. The correct crux is "finitely many minimal clauses" (which holds even when some contain large primes) (imo-2026-06, round 2).

ALWAYS: When proving "finitely many essential primes," use the PAIRWISE-INTERSECTION theorem: all minimal hitting sets (= term-supports) pairwise intersect (Tool 2); two minimal hitting sets with DISJOINT small-prime parts must share the SAME large prime (since H₁∩H₂=(C∩D)∪{q₁=q₂ or ∅}); this bounds essential large primes by #{disjoint small-prime pairs} ≤ 3^{π(P₁)} (imo-2026-06, round 2).
