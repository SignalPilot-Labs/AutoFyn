## imo-2026-06 — Lens: Eventual Periodicity and Stabilization

### Distinct openings

**Opening A — Clique + Periodic Valid Set**

Every two terms of the sequence share a common prime factor (the sequence is a "clique" in the gcd-graph). Proof: by definition, a_{n+1} must satisfy gcd(a_{n+1}, a_i) > 1 for ALL i ≤ n, so gcd(a_m, a_n) > 1 whenever m > n. By symmetry, gcd(a_m, a_n) > 1 for all distinct m, n.

This clique property means: every term lies in V = {m : gcd(m, a_n) > 1 for all n ≥ 1} (the "full valid set"). Since a_n ∈ V and V is a clique (any two members share a prime), the constraint "gcd(·, a_n) > 1" is automatically satisfied by all members of V. So V ⊆ {m : gcd(m, a_n) > 1} for every n. The greedy sequence is therefore the greedy increasing sequence on V: a_{n+1} = min(V ∩ (a_n, ∞)). If V is periodic (V + M = V), then the greedy sequence on V satisfies a_{n+T} = a_n + M with T = |V mod M|. This is global (holds for all n), not just eventual.

The hard subproblem: show V is periodic. This requires showing the prime constraints stabilize mod some finite M.

**Opening B — Essential Antichain Stabilizes (finite binding constraints)**

The constraint from term a_n is "hit P(a_n)" (be divisible by some prime in the prime set of a_n). A constraint is redundant if P(a_j) ⊆ P(a_n) for some earlier j (then "hit P(a_j)" implies "hit P(a_n)"). The non-redundant constraints form an antichain in the "prime-set inclusion" poset.

Computational evidence: for a1=105, the antichain stabilizes after 4 terms (a_1=105, a_2=108, a_3=110, a_4=112). After that, V mod 210 = {58 residues} and never changes despite new primes 11,13,17,... appearing in later terms. The valid set mod M (M = product of binding primes) is fixed at N=4 and T = |V mod M| = 58 = the period.

Proof sketch for antichain stabilization: after enough terms, any new a_n ∈ V (greedy), and since V-mod-M is fixed, the constraint from a_n reduces to a constraint mod M, which is already in the antichain.

**Opening C — State-Machine: Sequence determined by (a_n mod M, M)**

The greedy rule depends only on which residues mod M = rad(binding terms) are "valid." Once the binding terms are established (finite, determined by first few terms), the valid residue set is fixed. The state (a_n mod M) cycles through valid residues deterministically. By pigeonhole on the finite state space ℤ/Mℤ, the sequence is globally periodic (the greedy map σ : valid_residue → next_valid_residue is a bijection on a finite set → purely periodic, no transient needed). This gives global (not just eventual) periodicity.

**Opening D — Reduction to Greedy on a Union of APs**

V = {m : for each binding term a_j, gcd(m, a_j) > 1} = union of APs. Specifically, V is defined by a finite system of "hit hyperedge E_j" conditions (each E_j = prime set of a binding term). By inclusion-exclusion, V is a union of APs with period M = product of primes in ∪E_j. The greedy increasing sequence on such a union of APs is clearly arithmetic-periodic: period T = |V ∩ [1,M]| and increment L = M. The hard part: show the binding set is finite.

**Opening E — No new prime can escape the coverage**

Key structural fact: for any new prime p appearing in a_n (say a_n = p^k · (2-3-5-...-smooth part)), the term a_n has prime factors from both p and the established binding prime set. The constraint "gcd(m, a_n) > 1" is then already implied by older binding constraints (since a_n's established-prime factors already cover V). More precisely: since a_n ∈ V and V is periodic mod M (the binding-prime product), a_n has at least one prime factor q ∈ M (the binding primes); the constraint from a_n (hit {q, p, ...}) is weaker than the existing constraint (hit {q, ...} or whatever subset-set contains {q}).

### Candidate technique(s)

1. **CRT / Sieve periodicity**: V is a periodic subset of ℤ (intersection of "not coprime to a_j" sets, each periodic mod rad(a_j)). Once finite binding prime set established, period is M = product. From knowledge_base.md: "Modular arithmetic, CRT: solve/count solutions mod n by factoring and combining residues."

2. **Invariants and monovariant — density of V_n**: d(V_n) = |V_n ∩ [0,M)|/M is a decreasing rational. Each essential new constraint strictly decreases it. Since d(V_n) > 0 always (sequence is infinite), the density stabilizes in finite steps → finite essential constraints.

3. **State machine / finite-state pigeonhole**: The greedy map on ℤ/Mℤ is a deterministic map on a finite set → periodic orbit → global periodicity. From knowledge_base.md: "Order of an element, Fermat/Euler: periodicity of a^n mod m; eventual periodicity of products of a sequence mod m."

4. **Greedy on periodic set**: standard fact that the greedy increasing sequence on a periodic subset S + M = S satisfies a_{n+T} = a_n + M for all n (globally, not eventually) with T = density × M.

### Cheap-kill candidates

- **Clique check**: The clique property (any two terms share a prime) is immediate from the definition and is the organizing lemma. It reduces "global periodicity" to "V is periodic" — a much cleaner target.

- **V mod M stabilizes after finitely many essential terms**: Each essential term strictly reduces |V mod M|. Since |V mod M| ≥ 1 always (V nonempty), there are at most |V_1 mod M_1| essential terms → finite.

- **Parity / density bound**: If 2 | a_1, then all terms are even (since gcd(a_2, a_1) > 1 forces some prime | a_1 to | a_2; if a_1 is even, a_2 could be even with gcd=2, and then constraint from a_2 forces all future terms even). Reduces to T=1, L=2 immediately. This is the "cheap kill" for even a_1.

### Knowledge-base entries to use

- **Modular arithmetic, CRT** (NT section): V is a periodic subset of ℤ mod M = product of binding primes. CRT combines residue conditions.
- **Order of an element, Fermat/Euler** (NT section): eventual periodicity of sequences mod m; the greedy sequence mod M is periodic.
- **Invariants & monovariants** (Combinatorics): density d(V_n) is a decreasing monovariant bounded below by 0, so it stabilizes.
- **Pigeonhole / extremal** (Combinatorics): finite state space (residues mod M) → periodic orbit of the greedy map.
- **Linear recurrences** (NT section): "sequences are eventually periodic mod m" — exactly our setting once M is fixed.
- **Divisor analysis** (NT section): "gcd structure, bounding a finite search by size."

### Analogous past problems (cruxes)

1. **aimo-0678** [number_theory, modular-arithmetic-and-CRT]: "Once one coordinate of a coupled integer recurrence is bounded, reduce the other coordinate modulo the lcm of the bounded coordinate's attainable values, turning the state pair into a deterministic map on a finite set." Crux: bounded quantity → finite state → eventual periodicity. Analogous: our V_n stabilizes mod M (bounded/finite state mod M) → greedy map is finite-state → periodic.

2. **aimo-0514** [combinatorics, invariants-and-monovariants]: "When each state deterministically forces both its successor and predecessor, the map on the finite state set is a bijection, so every orbit is purely periodic." Crux: finite state + deterministic bijective map → purely periodic (global, no transient). Analogous: the greedy map on valid residues mod M is a bijection on T elements → orbit is purely periodic → a_{n+T} = a_n + M for ALL n (not just eventually).

3. **aimo-0077** [combinatorics, processes-and-algorithms]: "Finite state space (≤ 2^2008 configurations) means a non-ending process repeats a state, giving a periodic cycle." Crux: finite state + infinite process → periodic. Analogous: residues mod M form a finite state space; the greedy sequence is an infinite deterministic process → periodic.

### Prior progress

None (first round, status = unsolved, no existing approaches).

### Dead ends (do not retry)

- **"Prime set of the sequence stabilizes"**: FALSE. New primes 11, 13, 17, 19, 23, ... keep appearing as factors of later terms (verified for a1=15, a1=105). Any approach assuming the prime set is finite will fail.

- **"V is a clique iff V is eventually the valid set"**: The clique property of V (any two elements of V share gcd > 1) is TRUE and useful, but the argument "V is a clique → greedy on V agrees with original sequence" needs care. The key: the greedy sequence elements are ALL in V (by the clique property of the sequence itself), so the greedy sequence IS the greedy sequence on V.

- **"V_{n+1} = V_n iff V_n is a clique"**: Partially wrong. V_n (valid candidates > a_n) is NOT always a clique for small n. For a1=105, V_4 (m>112) is NOT a clique: gcd(130, 231) = 1. The clique that matters is the SEQUENCE ITSELF (as a set of terms), not the valid candidate set. Do not conflate these.

### Small-case / intuition notes

**Conjecture (supported by computation, not proved):**
- a1=6 (2·3): T=1, L=2. Binds immediately to "must be even."
- a1=15 (3·5): T=8, L=30=2·3·5. Essential constraints from terms a_1=15, a_2=18, a_3=20 (3 terms). V mod 30 stabilizes at N=3, |V mod 30|=8 residues.
- a1=105 (3·5·7): T=58, L=210=2·3·5·7. Essential constraints from terms a_1,...,a_4 (4 terms). V mod 210 stabilizes at N=4, |V mod 210|=58 residues.

Pattern: L = product of "binding primes" (always includes 2). Essential constraints come from first ~k terms where k is small. After N essential terms, V mod L is fixed with |V mod L| residues = period T.

The fact that a_{n+T} = a_n + L holds for ALL n (globally, not just eventually — VERIFIED computationally) suggests the proof should yield a GLOBAL period via the state-machine / bijective map argument, not an eventual-periodicity argument.

**Key structural facts established (conjectural from data, candidates for lemmas):**

1. (CLIQUE LEMMA — PROVABLE) Any two terms of the sequence share gcd > 1. Proof: immediate from the definition (a_n must share a prime with all a_i, i < n).

2. (REDUCTION LEMMA — CONJECTURAL) The greedy sequence equals the greedy increasing sequence on V = {m : gcd(m, a_n) > 1 for all n ≥ 1}.

3. (PERIODICITY OF V — MAIN CLAIM) V is periodic: V + M = V for some finite M (the product of "binding primes"). The binding primes are those p such that the constraint "hit some prime-set containing p" cannot be removed from the essential antichain.

4. (PERIOD FORMULA — CONJECTURAL) T = number of residues of V in [0,M), L = M.
