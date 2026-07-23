## imo-2026-06

### Numerical observations (conjecture, not proof)

Starting values and resulting (T, L) pairs:
- a_1 = 2 (prime): sequence = 2,4,6,8,... → T=1, L=2. All even.
- a_1 = p (prime): sequence = p, 2p, 3p, ... → T=1, L=p.
- a_1 = p^k (prime power): same, T=1, L=p.
- a_1 = 6 = 2·3: sequence becomes all even numbers ≥ 6 → T=1, L=2.
- a_1 = 15 = 3·5: sequence has diffs [3,2,4,6,6,4,2,3] repeating from n=1 → T=8, L=30=2·3·5.
- a_1 = 35 = 5·7: diffs with period 34 from n=1 → T=34, L=210=2·3·5·7.
- a_1 = 21 = 3·7: immediately becomes multiples of 3 → T=1, L=3.

Key numerical facts:
1. L is always a product of distinct primes (squarefree).
2. The periodicity a_{n+T} = a_n + L holds from n=1, not just eventually.
3. All pairs (a_i, a_j) with i < j have gcd(a_i, a_j) > 1 (GUARANTEED BY CONSTRUCTION). This is the fundamental constraint.

### Distinct openings

**Opening A (Constraint-antichain stabilization)**:
Define the "constraint antichain" A_n = {minimal sets S of primes : S = primes(a_i) for some i ≤ n, and no proper subset of S is the prime-set of any a_j with j ≤ n}. This antichain is pairwise-intersecting (since gcd(a_i, a_j) > 1 means their prime sets intersect). The main claim is that A_n stabilizes to A_{N_0} for some finite N_0, after which every subsequent constraint is dominated (redundant). Once stable, the valid set V = {x : x satisfies all constraints in A_{N_0}} is a periodic set mod Q = ∏(primes in ∪A_{N_0}), and the greedy sequence cycles through the T valid residues mod Q with shift L = Q. Proof of stability requires showing the antichain eventually has "property (*)": every transversal of the antichain contains some antichain element.

Verified computationally:
- a_1=15: property (*) achieved at step 3 (after visiting 15,18,20); antichain = {{3,5},{2,3},{2,5}}; no new antichain element ever added.
- a_1=35: property (*) achieved at step 4 (after visiting 35,40,42,45); antichain = {{5,7},{2,5},{2,3,7},{3,5}}.

Critical observation (proved computationally): Once the antichain has property (*), NO future term can add a new antichain element. Proof: suppose S = primes(a_{n+1}) would be new (not dominated). S is a transversal (satisfies all current constraints). By property (*), some A_i ⊆ S, so S IS dominated. Contradiction.

**Opening B (Valid-set-is-a-clique route)**:
The valid set V_n = {x > a_n : gcd(x, a_i) > 1 for all i ≤ n} shrinks as n grows (V_n ⊆ V_{n-1}). The sequence is a clique: any two terms share a prime. Claim: Eventually V_n is a "clique" (any two elements share a prime factor). Once V_{N_0} is a clique, the constraint stabilizes: for any future term a_m ∈ V_{N_0} and any valid x ∈ V_{N_0}, gcd(x, a_m) > 1 (they share a prime since V_{N_0} is a clique). So V_m = V_{N_0} for all m > N_0.

Route to clique: The greedy sequence visits coprime pairs. If x, y ∈ V_n with gcd(x,y) = 1 and x < y, then when a_m = x is visited, y must satisfy gcd(y, x) > 1 — contradiction. So y is excluded before x is visited. Each coprime pair resolves in finite time. The gap: why do ALL coprime pairs resolve in finite time?

**Opening C (Reduction to greedy-on-a-sieve)**:
Assuming stabilization (Opening A or B), the proof of periodicity is clean:
1. Let Q = product of primes in the stable antichain. The valid set V is periodic mod Q.
2. The valid residues mod Q form a set R of size T, and R is a clique (any two elements share a prime).
3. The greedy sequence, starting from a_1 (which is in V, proved since a_1 is in the clique by construction), cycles through R in order, gaining L = Q every T steps.
4. Since a_1 ∈ V, the period holds from n=1: a_{n+T} = a_n + L for all n ≥ 1.

Point 4 requires checking: a_i is in the final valid set V_{N_0} for ALL i ≥ 1 (not just i > N_0). True because: for i < j, gcd(a_i, a_j) > 1 (by construction), so a_i satisfies the constraint from a_j, meaning a_i ∈ V_n for all n (regardless of which constraints are active). Specifically a_1 satisfies all constraints since gcd(a_1, a_j) > 1 for all j > 1 (by the symmetry gcd(a_j, a_1) > 1 which is required by definition).

### Main gap: Why does the constraint antichain stabilize?

The antichain grows by adding new minimal elements. For the antichain to have property (*), it must be "complete" (self-covering). The gap is showing this always happens in finite time.

**Candidate argument**: 
- Every antichain element S must contain a prime from B = primes(a_1) (fixed finite set of primes).
- The "projection" T_S = S ∩ B is a nonempty subset of B.
- There are only 2^|B| - 1 possible projections. So the projected antichain stabilizes in at most 2^|B| steps.
- Once the projected antichain has property (*) restricted to B (every B-transversal contains a B-projection), the full antichain has property (*) for the effective constraint.

Why? Because any future term a_{n+1} must share a prime with a_1 → must have a prime in B. The only "useful" part of the constraint from a_m (for satisfying the constraint with a_{n+1}) is the B-primes: if both a_m and a_{n+1} have a common prime in B, they share a factor. If a_m's B-projection is T_m and a_{n+1}'s B-projection is T_{n+1}, and T_m ∩ T_{n+1} ≠ ∅, they share a B-prime.

For a_{n+1} to fail the constraint from a_m: a_{n+1} must have NO prime in primes(a_m) — neither the B-primes of a_m nor its extra primes. But all valid a_{n+1} have some B-prime, and if that B-prime is in primes(a_m), constraint satisfied. So constraint fails only if a_{n+1}'s B-prime(s) are NOT in primes(a_m). This is a condition purely on B-projections!

So: the constraint from a_m on a_{n+1} is effectively: a_{n+1} must have a prime in primes(a_m) = (B-prime of a_m) ∪ (extra primes). Since a_{n+1} already has a B-prime, the constraint is: a_{n+1}'s B-prime(s) must intersect T_m = primes(a_m) ∩ B, OR a_{n+1} must have one of a_m's extra primes.

The "extra primes" condition is an additional requirement. Whether it's binding depends on whether a_{n+1}'s B-primes are all outside T_m.

**Simpler approach to the gap**: Use the following bound. The set of "critical" constraints (those in the stable antichain) has size ≤ the number of maximal cliques in the "prime co-sharing graph" restricted to B-primes. This is at most 2^|B|. Since B = primes(a_1) is finite, the bound is finite.

### Candidate technique(s)

- **Sieve / greedy-on-periodic-set**: The core mechanism once the constraint stabilizes. Valid integers form a periodic set mod Q; greedy selection through them gives shift-periodicity. This is elementary once the valid set is characterized.
- **Antichain / Sperner-type theory**: The pairwise-intersecting antichain of prime sets must eventually have property (*). The Bollobás set-pairs inequality or Helly-type argument for intersecting families may apply.
- **Eventual periodicity of greedy sequences on sieved sets**: The structure is: pick smallest integer not coprime to a fixed squarefree Q. This is periodic with period = number of valid residues mod Q and shift = Q.
- **Pigeonhole on residues**: Once the constraint is mod-Q periodic, the sequence hits each valid residue in cyclic order.

### Cheap-kill candidates

- **If a_1 is a prime power**: immediate. All terms are multiples of the unique prime. T=1, L=p. No work needed for this case, but it illustrates the structure.
- **Parity**: if any term is a power of 2, all subsequent terms are even → T=1, L=2.
- **Pigeonhole**: The projected antichain on B = primes(a_1) has at most 2^|B| - 1 elements; since |B| is finite, stability follows.

### Knowledge-base entries to use

- **Modular arithmetic, CRT** (knowledge_base.md, "Number Theory"): valid set is periodic mod Q; CRT gives independent prime-power conditions.
- **Order of an element, Fermat/Euler / eventual periodicity**: "eventual periodicity of products of a sequence mod m" — the valid residues cycle with period T.
- **Divisor analysis**: "gcd structure, consecutive-integer coprimality" — the gcd conditions defining validity.
- **Pigeonhole / extremal principle**: for bounding the antichain and proving stabilization.
- **Invariants and monovariants**: the antichain as a monovariant (property (*) as the stable state).
- **Bertrand's postulate**: might be used to ensure that the greedy sequence doesn't "skip" valid residues in an unexpected way.

### Analogous past problems (cruxes)

1. **aimo-0079** [number_theory/pigeonhole]: "Among infinitely many length-L windows of a {0,1}-valued (parity) function on the integers, pigeonhole over the finitely many possible window-patterns to find two starting positions whose windows agree termwise." — Analogous because it uses pigeonhole on FINITE WINDOW PATTERNS in an infinite sequence to find periodicity. Crux move: the sequence of (parity) states is eventually periodic because there are finitely many states. Adapt: our "state" is the antichain mod Q; finitely many states → eventual periodicity.

2. **aimo-0231** [number_theory/modular-arithmetic-and-CRT]: "Decompose the first-hitting-time of an iterated map modulo N as the lcm, over the prime-power factors of N, of the first-hitting-times modulo each prime power." — Analogous in that it uses CRT to decompose a periodicity claim into independent prime-power components. Adapt: our period T and shift L might decompose via CRT over the primes in Q.

3. **aimo-0171** [number_theory/modular-arithmetic-and-CRT]: "When a walk returns to its starting residue mod n, equate its telescoped block-sum to the winding count times the full-period sum." — Directly analogous: our sequence returns to the same residue mod Q every T steps, implying a_{n+T} - a_n = L = Q.

### Prior progress

None. First round.

### Dead ends (do not retry)

None yet established. But:
- "All terms eventually share a common prime" is FALSE (e.g., a_1=15 has terms with prime 2 and terms with prime 5 but not both; and terms with prime 3 and 5 but not 2). The correct statement is weaker: the valid set is a clique, not that all terms share a single prime.

### Small-case / intuition notes (all conjectural)

- L = Q = product of distinct primes in the stable antichain. This is always a squarefree number bounded by Q ≤ ∏(primes ≤ a_k) for the first k terms that stabilize the antichain.
- T = number of valid residues mod Q (equivalently: Q minus the number of residues coprime to some antichain element). For a_1=15: T=8, Q=30, so T = 30 - φ(30) + ... (not simply 30-φ(30)=22; the valid set has ONLY 8 elements because of the INTERSECTION constraints, not just "divisible by 2 or 3 or 5").
- The critical terms (those that change the antichain) are all small: a_1, a_2, ..., a_{N_0} where a_{N_0} ≤ Q² (rough bound). So N_0 is explicitly bounded.
- The fact that a_{n+T} = a_n + L holds from n=1 (not just n ≥ N_0) follows from: a_1 itself satisfies all constraints in the stable antichain (since gcd(a_1, a_j) > 1 for all j ≥ 2, by symmetry of the gcd condition).
