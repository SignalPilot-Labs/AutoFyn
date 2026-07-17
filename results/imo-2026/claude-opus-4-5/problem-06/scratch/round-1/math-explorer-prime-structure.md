# imo-2026-06 — Prime Structure Lens

## Problem
Greedy sequence: a_{n+1} = smallest integer > a_n with gcd(a_{n+1}, a_i) > 1 for all i ≤ n.
Prove: there exist T, L > 0 with a_{n+T} = a_n + L for ALL positive integers n.

---

## Small-case / intuition notes (all labeled as conjecture/verified)

**Computations** (verified, not conjectured):

| a_1 | T | L | L factored | Notes |
|-----|---|---|-----------|-------|
| 4 | 1 | 2 | 2 | All even numbers from a_1 |
| 9 | 1 | 3 | 3 | All multiples of 3 |
| 25 | 1 | 5 | 5 | All multiples of 5 |
| 15 | 8 | 30 | 2·3·5 | Period from n=1 |
| 35 | 34 | 210 | 2·3·5·7 | Period from n=1 |
| 77 | 18 | 154 | 2·7·11 | Period from n=1 |
| 91 | 20 | 182 | 2·7·13 | Period from n=1 |
| 143 | 64 | 858 | 2·3·11·13 | Period from n=1 |

Key observations (verified):
1. **L = lcm of the "backbone" primes** — the primes from the first K terms of the sequence.
2. **Period holds from n=1** (not just eventually) in all computed cases.
3. **The backbone set S' stabilizes after K startup terms**. For a_1=35, K=4; for a_1=143, K~4.
4. **Every a_n (n≥2) is divisible by some prime factor of a_1** (since gcd(a_n, a_1) > 1 forces this).
5. **No term in the sequence can be a new prime**: if a_n = q (prime, new), then gcd(a_n, a_{n-1}) = 1, contradiction.
6. **New primes appear only as extra factors alongside backbone primes**: e.g., a_14 = 66 = 2·3·11 for a_1=15 has extra prime 11 but backbone primes 2,3.

---

## Key structural discovery: Backbone types and minimal transversals

Define **backbone set** S' = prime factors of L. For a_1=35: S' = {2,3,5,7}.

Define the **backbone type** T_i of a_i as {prime factors of a_i} ∩ S'.

**Critical computation** (verified for a_1=35, a_1=143, a_1=15):
- The startup backbone types T_1,...,T_K are pairwise intersecting: T_i ∩ T_j ≠ ∅ for all i,j ≤ K.
  (This follows directly from gcd(a_i, a_j) > 1.)
- The startup backbone types T_1,...,T_K are EXACTLY the minimal transversals of the
  hypergraph {T_1,...,T_K}. (Verified computationally for K=4 in a_1=35 example.)
- **EVERY future term a_j (j > K) has backbone type ⊇ T_i for some i ≤ K**:
  i.e., the backbone type of a_j contains a startup backbone type as a subset.
  (Verified for all j up to 100 in a_1=35 and a_1=143 cases.)

**Why this matters**: Since every transversal of {T_1,...,T_K} contains a minimal transversal as a subset, and minimal transversals are pairwise intersecting, ANY TWO VALID BACKBONE TYPES intersect. Hence any two terms (both with valid backbone types) share a backbone prime, giving gcd > 1.

**Consequence**: After the startup phase, constraint C_j (from a_j, j > K) is subsumed by constraint C_{i_0} (from some startup term a_{i_0} with T_{i_0} ⊆ T_j). The gcd condition gcd(m, a_j) > 1 is automatic for any m satisfying C_1,...,C_K (since m and a_j have backbone types, both transversals, which intersect at some backbone prime).

---

## The core proof mechanism (unproved but strongly supported)

**After K startup terms, the valid set V for future terms is:**
V = {m : m has backbone type = transversal of {T_1,...,T_K}}
  = {m : for each i ≤ K, some prime from T_i divides m}

This set V is PERIODIC mod L = lcm(S').

The valid residues mod L are exactly those r with T_r = transversal of {T_1,...,T_K}. There are T = |{r ∈ {0,...,L-1} : r ∈ V}| valid residues per period.

The greedy on V gives: a_{n+T} = a_n + L for all n ≥ 1.

**For a_1=15**: S'={2,3,5}, L=30, T=8.
Valid residues mod 30 = {r : r divisible by ≥2 of {2,3,5}} = {0,6,10,12,15,18,20,24}. T=8. ✓

**For a_1=35**: S'={2,3,5,7}, L=210, T=34. Verified. ✓

---

## Key structural claim to prove

**CLAIM (Constraint Stabilization)**: For all j > K: the constraint from a_j is subsumed by C_1,...,C_K.

**CLAIM (Minimal Transversal = Startup)**: The startup backbone types T_1,...,T_K are exactly the minimal transversals of the hypergraph {T_1,...,T_K}.

**Why the startup = minimal transversals**: (Heuristic, needs proof.) The greedy picks a_i = smallest valid integer at step i. If T' ⊂ T_i (strict subset) were also a valid backbone type, then the greedy would prefer a number with backbone type T' (smaller backbone = earlier appearance in the sequence). Since a_i is the greedy pick, T_i is "forced" (minimal).

**Key gap**: The formal proof that T_i is a minimal transversal requires showing: for each prime p ∈ T_i, there exists j < i with T_j ∩ T_i = {p} (i.e., p is the UNIQUE shared backbone prime between a_i and a_j). This requires the greedy mechanism creates such "uniqueness."

---

## Distinct openings

**Opening A (Backbone + Minimal Transversal)**: 
Show T_1,...,T_K are minimal transversals of {T_1,...,T_K} → any two transversals intersect → constraints stabilize → valid set periodic mod L → greedy periodic.

**Opening B (Direct Constraint Subsumption)**:
Show directly: for each j > K, the backbone prime type of a_j contains T_i as subset for some i ≤ K (by induction on j using that a_j must hit each T_i). Then subsumed immediately.

**Opening C (Stable valid set V_∞ = V_K)**:
Show V_∞ = {m : gcd(m, a_i) > 1 for ALL i} = V_K (the startup valid set). Since V_∞ ⊆ V_K trivially, need V_K ⊆ V_∞. This requires: every m ∈ V_K has gcd(m, a_j) > 1 for all j. This is exactly constraint stabilization.

**Opening D (Finite State Machine argument)**:
After startup, the "state" determining a_{n+1} is (a_n mod L, the last T backbone types). Show this state space is finite and the map is deterministic, hence eventually periodic. Then extend to purely periodic from n=1 since a_1 ∈ V_K.

**Opening E (Direct L = lcm(S') periodicity)**:
Note that L = lcm(prime factors of a_1 · a_2 · ... · a_K) for some K. Show that m ∈ V_K iff m + L ∈ V_K (the valid set is L-periodic). Prove: adding L to m doesn't change which backbone primes divide it (since L is divisible by all backbone primes, so adding L preserves residues mod each backbone prime). Hence m and m+L have the same backbone type. Then V_K is L-periodic, and the greedy gives periodicity.

---

## Candidate techniques

- **Covering sets / transversal hypergraph theory**: The backbone types form a hypergraph; valid terms are transversals; minimal transversals are pairwise intersecting; constraint stabilizes.
- **Greedy algorithm on periodic set**: Once valid set V is periodic mod L, greedy gives purely periodic sequence with T = |V ∩ {0,...,L-1}|.
- **Divisibility analysis**: Backbone primes determined by a_1,...,a_K; prime factorization structure.
- **CRT / periodic conditions**: The valid set V = ∩_i {m : p | m for some p ∈ T_i} is periodic mod L = lcm(T_1 ∪ ... ∪ T_K).

---

## Cheap-kill candidates

- **Single backbone prime**: If a_1 is a prime power p^k, every future a_n is divisible by p (since gcd(a_n, a_1) > 1 forces p | a_n), and the sequence is all multiples of p. T=1, L=p. (Trivial case.)
- **Prime power rule**: No a_n can equal a new prime (q prime, q ∤ a_i for all i < n), since gcd(q, a_{n-1}) would be 1. This limits the set of possible prime factors strongly.
- **New primes always co-packaged**: Any new prime q appearing in a_n must co-appear with a backbone prime (since otherwise some a_i with only backbone prime p would have gcd(a_n, a_i) = 1). This shows new primes are "extras" that don't affect the backbone.

---

## Knowledge-base entries to use

- **Divisor analysis**: gcd structure, the key starting fact that every a_n shares a prime with a_1.
- **Order of an element / eventual periodicity**: The greedy on a periodic set eventually produces a periodic sequence.
- **CRT**: The valid set V_K = ∩_i (multiples of some prime in T_i) is periodic mod L = lcm(T_i).
- **Pigeonhole**: With |S'| backbone primes and each term having ≥ d of them (2d > |S'|), any two terms share a backbone prime.

---

## Analogous past problems (cruxes)

**aimo-0514** (most analogous): "Show a deterministic process is reversible so its state graph is a union of cycles, forcing the orbit to be PURELY periodic (not just eventually)." The analogy: once we identify the finite "state" (residue mod L), the greedy is a deterministic map on a finite state space, giving pure periodicity from n=1. Crux move: finite-state determinism → pure periodicity.

**aimo-0678**: "Once one coordinate of a coupled recurrence is bounded, reduce modulo the lcm of bounded values → eventually periodic." Analogous: once backbone is bounded (finite S'), reduce mod L = lcm(S') → periodic.

**aimo-0477**: (less direct) "p-adic valuation tracking in a sequence: exponents eventually constant." Technique of tracking prime factors of sequence terms and showing they stabilize. Related to backbone stabilization.

---

## Prior progress

None (Status: unsolved, no approaches yet).

## Dead ends (do not retry)

None yet (first round).

## Critical open gap

The hardest step is **proving the startup backbone types T_1,...,T_K are exactly the minimal transversals of the hypergraph {T_1,...,T_K}**. This is equivalent to: for each prime p ∈ T_i, there exists j ≤ K with T_j ∩ T_i = {p}. The greedy mechanism (a_i = smallest valid integer) likely forces this, but the argument is subtle.

Alternative route around this gap (Opening B): Show by induction that a_j's backbone type ⊇ T_i for some startup T_i. This gives constraint subsumption without going through minimal transversal theory.

The cleanest route (Opening E): Show V_K is L-periodic directly from the fact that backbone prime divisibility is preserved under +L (since L = lcm(backbone primes)). Then the greedy on the L-periodic set V_K is purely periodic from n=1.
