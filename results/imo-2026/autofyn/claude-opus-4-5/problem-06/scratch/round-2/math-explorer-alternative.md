## imo-2026-06

- **Distinct openings:**

  **Opening A — "All terms enumerate V_stable from n=1" (direct enumeration, no startup phase).**
  Define H_stable = antichain of {P(a_i) : all i ≥ 1} and V_stable = {m : P(m) transverses H_stable}. Two lemmas:
  (i) All pairs a_j, a_k share a prime. Proof: the later term was chosen to share a prime with all earlier terms, so P(a_k) ∩ P(a_j) ≠ ∅ for k > j, and symmetrically for j > k. Hence the full family is intersecting.
  (ii) Every a_j ∈ V_stable. Proof: each Q ∈ H_stable is P(a_k) for some k; by (i), P(a_j) ∩ P(a_k) ≠ ∅, hence P(a_j) ∩ Q ≠ ∅ for all Q ∈ H_stable, so a_j ∈ V_stable.
  (iii) Greedy = min V_stable from n=1. Proof: H_stable is more refined than H_n (each Q ∈ H_stable is a subset of some element of H_n), so V_stable ⊆ V_n. Hence min V_n ≤ min V_stable. But a_{n+1} = min V_n ∈ V_stable (by ii), so a_{n+1} ≥ min V_stable. Combining: a_{n+1} = min V_stable > a_n.
  This collapses the "backward extension problem" completely: the sequence IS the ordered enumeration of V_stable starting from a_1, so if V_stable is L-periodic (with valid residues S ⊆ [0,L)), then a_{n+T} = a_n + L for ALL n ≥ 1 (T = |S|). The backward extension, which was the unresolved gap in two-of-k-structure, is now handled by this opening.
  Remaining: prove V_stable is L-periodic (i.e., H_stable is a finite antichain with finitely many primes in union(H_stable)).

  **Opening B — "H stabilizes via saturation" (monovariant on the valid set).**
  Call H saturated if every m ∈ V(H) has P(m) ⊇ some Q ∈ H (every valid element is "dominated"). If H_n is saturated, then H_m = H_n for all m ≥ n (any new a_{n+1} ∈ V(H_n) is dominated, hence doesn't change H). Computational evidence: H_n saturates after at most 4 steps for tested cases. The proof strategy: show that after finitely many steps, the greedy generates a term forcing every subsequent valid element to be dominated. This is a pure combinatorial argument about intersecting antichains of prime sets.
  Saturation of H = {{2,3},{2,5},{3,5}}: Case 2|m needs 3|m or 5|m → P(m) ⊇ {2,3} or {2,5}. Case 2∤m: need 3|m AND 5|m → P(m) ⊇ {3,5}. EVERY valid element dominated. Verified for other cases too.

  **Opening C — "Infinite H_stable forces all-multiples-of-p structure" (reduction to Case 2a).**
  Suppose H_stable is an infinite antichain. Since every Q ∈ H_stable has Q ∩ B ≠ ∅ (backbone), by pigeonhole some backbone prime p appears in infinitely many Q_1, Q_2, ... ∈ H_stable. If p ∉ Q_i for all but finitely many i, contradiction. So {Q_i} with p ∈ Q_i is infinite, meaning H_stable contains {p, r_1}, {p, r_2}, ... for infinitely many distinct primes r_i (the sets are pairwise incomparable so r_i are all distinct). Now any m ∈ V_stable must hit {p, r_i} for all i; if p ∤ m then r_i | m for all i (impossible). So p | m for all m ∈ V_stable. Hence the sequence is entirely multiples of p, effectively reducing to Case 2a (T=1, L=p). This case is solvable: all multiples of p are valid once all terms are multiples of p (they pairwise share p), so a_{n+1} = a_n + p.

  **Opening D — "State machine on a_n mod L" (automaton framing).**
  The next term a_{n+1} depends only on a_n mod L and the current constraints H_n. If H_n stabilizes, a_{n+1} mod L is determined by a_n mod L alone (deterministic finite automaton on |valid residues| states). Since the state space is finite, the sequence of states is periodic. The forward direction (after stabilization) is clear. The backward direction is handled by Opening A: the greedy always picks min V_stable, so a_n mod L cycles through valid residues from n=1. The state machine analogy provides an alternative language for the same argument.

  **Opening E — "2-element stability in Sub-case 2b" (no prime power).**
  In Sub-case 2b (no prime power ever enters): every Q ∈ H_n has |Q| ≥ 2. A 2-element set {p,q} ∈ H_n NEVER leaves (it can only be replaced by a proper subset with ≥ 2 elements, which doesn't exist for a 2-element set). So 2-element sets in H_n are non-decreasing. This means the "2-skeleton" of H_n is non-decreasing. Once all the necessary 2-element sets {p_i, p_j} are in H_n (for the essential primes {p_1,...,p_k}), H_n is saturated (every valid element contains some pair). The key: the 2-skeleton stabilizes to a finite set of pairs, because each new pair requires a term whose MINIMAL prime set is exactly that pair — and once enough pairs are in H_n, no new minimal pairs arise. This gives a K_k^2 structure only for the 2-element part, but NOT claiming H is exactly K_k^2 (which was the false claim). H might also have larger elements {p,q,r} initially, but those are eventually replaced or dominated.

- **Candidate technique(s):**
  - Intersecting family / antichain theory: H is an intersecting antichain, giving structural constraints on V.
  - Invariants / monovariants: V_n is non-increasing. The "saturation" event is a one-way transition.
  - Chinese Remainder Theorem / sieve: V_stable is L-periodic for L = product of primes in union(H_stable).
  - Finite state machine: sequence mod L is eventually periodic (from Opening D).
  - Case analysis: Sub-case 2a (prime power enters) vs 2b (no prime power), already verified computationally.

- **Cheap-kill candidates:**
  - Case 2a (prime power enters): once p^e appears, all terms are multiples of p (gcd with p^e forces it), hence T=1, L=p. This case is essentially solved already.
  - The backward extension: All terms in V_stable (proven via intersecting family). Eliminates the need for a separate backward argument.
  - "Infinite H_stable forces Case 2a" (Opening C): If H_stable is infinite, reduce to all-multiples-of-p. So either H_stable is finite (Case 2b) or we're in Case 2a. Both cases give periodicity.

- **Knowledge-base entries to use:**
  - "Divisor analysis / gcd structure": core of the problem.
  - "Invariants & monovariants": V_n non-increasing, saturation as a termination criterion.
  - "Pigeonhole / extremal principle": backbone prime pigeonhole for finiteness of H_stable.
  - "Modular arithmetic, CRT": V_stable is L-periodic once H_stable is finite.
  - "Direct proof / casework": Case 2a vs 2b analysis.

- **Analogous past problems (cruxes):**
  1. **aimo-0678** (modular-arithmetic-and-CRT): "Once one coordinate of a coupled integer recurrence is bounded, reduce the other coordinate modulo the lcm of the bounded coordinate's attainable values, turning the state pair into a deterministic map on a finite set." Analogy: In our problem, once H_n stabilizes (bounding the constraint structure), a_n mod L is the state, giving a deterministic finite map and hence periodicity.
  2. **aimo-0477** (divisibility-and-gcd): "Track gcd(fixed term, current term) and show it divides the next one, producing a divisor-chain bounded by the fixed term that must stabilize." Analogy: The "saturation" of H_n can be tracked via the divisors of the backbone a_1 = p_1^e1 ... p_k^ek; the constraints involving backbone primes form a non-decreasing divisor chain.
  3. **aimo-0514** (processes-and-algorithms): "Show a deterministic process is reversible so its state graph is a union of cycles, forcing the orbit to be purely periodic." Analogy: The greedy sequence, viewed as picking the next element of V_stable, is deterministic given a_n mod L. The state graph on finite states is a union of cycles (since V_stable has no "transient" states), giving a_{n+T} = a_n + L from the start.

- **Prior progress:**
  - two-of-k-structure approach (CHANGES REQUESTED): Main structure correct (antichain stabilizes, V_stable is L-periodic), but contains a false K_k^2 claim (not needed) and an unrigorous backward extension.
  - Backward extension is now RESOLVED by Opening A: all terms are in V_stable (intersecting pair lemma), and greedy = min V_stable from n=1 (since a_{n+1} ∈ V_stable and V_stable ⊆ V_n).
  - The remaining gap: H_stable is a FINITE antichain (finitely many primes in union(H_stable)).
  - Computational verification: H_n stabilizes within 3-4 steps for all tested cases (a1 = 6, 10, 14, 15, 21, 30, 35, 42, 70, 77, 91, 105, 143, 210).

- **Dead ends (do not retry):**
  - K_k^2 claim: PROVEN FALSE. For a_1 = 35, H_stable = {{5,7},{2,5},{3,5},{2,3,7}} which has a 3-element set.
  - backbone-periodicity approach: RETHINK verdict. The approach restricts to backbone primes, but non-backbone primes (like 2 for a_1=15) enter the constraints.
  - clique-valid-set: DEAD-END. Fatal gap in coprime-pair resolution.

- **Small-case / intuition notes:**
  - For a_1 = 15: H stabilizes at n=3 to {{2,3},{2,5},{3,5}}. L=30, T=8. Valid residues mod 30: {6,10,12,15,18,20,24,30} (8 residues). All terms divisible by ≥2 of {2,3,5}. New primes (7,11,13,...) enter as passengers but don't affect H. (VERIFIED, conjecture confirmed.)
  - For a_1 = 35: H stabilizes at n=4 to {{5,7},{2,5},{3,5},{2,3,7}}. L=210, T=34. (VERIFIED.)
  - For a_1 = 105: H stabilizes quickly. L=210, T=58. (VERIFIED.)
  - New primes keep entering the sequence indefinitely (11, 13, 17, ... appear for a_1=15), but their prime sets are always dominated by existing elements of H_stable. (VERIFIED, CONJECTURE: this is always the case.)
  - H_n stabilizes fast (within O(1) steps in all tested cases) because saturation happens quickly. (VERIFIED empirically, proof gap remains.)
  - In Sub-case 2b (no prime power): 2-element sets in H_n never leave H_n, so the "2-skeleton" is non-decreasing. This is a useful structural observation. (PROVEN.)
  - For Case 2a (prime power enters): T=1, L=p. This is completely proven. All terms are multiples of p because a_j shares a prime with the prime power p^e, so p | a_j for all j. (PROVEN.)
  - KEY NEW INSIGHT (CONJECTURE labeled): The greedy sequence a_{n+1} = min V_stable > a_n for ALL n ≥ 1, without any "startup phase" correction. This is equivalent to the backward extension and is now proven as a corollary of "all terms in V_stable" plus "V_stable ⊆ V_n."
