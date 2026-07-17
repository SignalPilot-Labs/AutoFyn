ALWAYS: When exploring greedy sequences defined by gcd/divisibility conditions, compute the sequence numerically for several starting values (a_1=2,3,7,15,35,77) and check differences for periodicity — the period and gap emerge directly from computation. (Because the greedy dynamics evidence is the primary guide, round 1)

ALWAYS: For problems about sequences with pairwise gcd > 1, the "intersecting antichain H" (irredundant prime-set constraints) is the key structural object — define it early and track how it evolves. (Because this gives both the period T and the gap L = lcm(∪H), round 1)

ALWAYS: Compute not just the differences but also the residues mod L to confirm the valid-set structure: check that {a_n mod L : n large} = {residue classes divisible by ≥2 primes from some set S}. (Because this confirmed the K_k^2 structure in every tested case, round 1)

NEVER: Assume that large primes entering the sequence prevent H from stabilizing — in practice they appear alongside small primes and their constraints are dominated by the small-prime constraints. (Because in a_1=15 case, every term like 42=2*3*7 had its constraint dominated by {2,3}, round 1)

ALWAYS: Verify computationally that future backbone types are supersets of startup backbone types (the "constraint subsumption" property) — this is the KEY structural fact enabling periodicity. Confirmed for a_1=35 and a_1=143 in round 1.

ALWAYS: Check that the period T holds from n=1 (not just eventually) — this was true for ALL tested cases in round 1, suggesting the proof should establish pure periodicity (no transient), not just eventual periodicity.

NEVER: Assume a single prime divides all sufficiently large terms — this fails for a_1=15 where no single prime divides all large terms (45=3^2*5 not divisible by 2, 20=4*5 not divisible by 3). The correct unit is the "backbone set" S'. (round 1)

ALWAYS: For the antichain stabilization proof, check "property (*)" = every transversal of the antichain contains some antichain element. Once this holds, the antichain is stable forever. Verified: achieved at step 3 for a_1=15 and step 4 for a_1=35. (round 1)

ALWAYS: The valid residue set mod Q is always a "clique" (any two elements share a prime) once the antichain stabilizes. This is the key reason new constraints don't add anything: both the new term and any old valid element share a prime (both are in the clique). Verify this computationally by checking all pairs in the valid residue set. (round 1)

ALWAYS: The periodicity holds from n=1 (not just for n > N_0) because a_1 itself satisfies all constraints in the stable antichain — by symmetry gcd(a_1, a_j) = gcd(a_j, a_1) > 1 for all j > 1, so a_1 is in the final clique. (round 1)

ALWAYS: For backward-extension questions in greedy gcd-sequences, the right reformulation is "the sequence IS the greedy on V*" rather than "extend periodicity backward." Prove two lemmas: (a) every a_j ∈ V* (pairwise non-coprime + H* consists of actual prime sets), (b) V* ⊆ V_{H_n} for all n (antichain refinement: each Q ∈ H_n has some Q* ∈ H* with Q* ⊆ Q). Together: a_{n+1} = min V* ∩ (a_n, ∞). No startup phase, no transient. (round 2)

NEVER: Say "all a_n ∈ V by definition of valid" to justify the backward extension — 'valid at step n' (transversal of H_n) and 'in V*' (transversal of H*) are DIFFERENT conditions. The correct argument uses pairwise non-coprimality and the fact that H* elements ARE prime sets of actual terms. (round 2)

ALWAYS: For the saturation condition (H_n stable), verify that the antichain is "self-saturating": every transversal of H_n contains some element of H_n as a subset. Verified computationally for a_1=15 (saturated at n=3 = H_3={{2,3},{2,5},{3,5}}) and a_1=35 (saturated at n=4). Once saturated, H_n never changes. (round 2)

ALWAYS: If H_stable might be infinite, use the backbone argument: if infinitely many 2-element sets {p, r_i} ∈ H_stable share a backbone prime p, then ALL valid elements are multiples of p, reducing to Case 2a (T=1, L=p). So either H_stable is finite or we're in Case 2a. (round 2)

ALWAYS: The monovariant f(H) = sum_{Q in H} 2^{-|Q|} is NON-DECREASING as H evolves (replacing Q by subset P increases f, adding incomparable P increases f). f is bounded above (≤1 for self-blocking antichains). This is the right monovariant for proving H stabilizes. (round 2)

ALWAYS: support(H) can SHRINK as H evolves (e.g. a1=105: primes 11,13 enter support when {2,5,11},{2,5,13} join H, then leave when {2,5} replaces both). The final L = product(support(H_stable)) may be SMALLER than product of all primes ever seen. (round 2)

NEVER: Assume support(H) is monotone increasing — it is not. Only S_n = all primes ever seen in sequence terms is monotone. support(H_n) is the union of elements currently in H and can decrease. (round 2)
