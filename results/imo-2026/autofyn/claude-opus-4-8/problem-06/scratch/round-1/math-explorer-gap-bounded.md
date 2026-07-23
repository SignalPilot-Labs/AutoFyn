## imo-2026-06 — Gap-Boundedness / Growth-Control / Finite-State-Machine framing

### Empirical findings

Ran experiments for a1 ∈ {2, 4, 6, 10, 15, 21, 35, 77, 91, 143, 221}. All sequences are purely periodic from n=1.

| a1 | T | L | L factors |
|----|---|---|-----------|
| 2, 4, 6 | 1 | 2 | {2} |
| 10 | 1 | 2 | {2} |
| 15 | 8 | 30 | {2,3,5} |
| 21 | 1 | 3 | {3} |
| 35 | 34 | 210 | {2,3,5,7} |
| 77 | 18 | 154 | {2,7,11} |
| 91 | 20 | 182 | {2,7,13} |
| 143 | 64 | 858 | {2,3,11,13} |
| 221 | 334 | 6630 | {2,3,5,13,17} |

**Key empirical observations** (labeled as conjectured):
1. L is always the product of a finite set P of primes = the "essential prime set". T = number of admissible residues mod L.
2. New large primes (e.g., 7, 11, 17, ...) continually enter the sequence as factors of terms, but do NOT change L or T after L is established.
3. The period holds from n=1, not just eventually.
4. ALL terms of the sequence are admissible in the sense that a_i mod M ∈ A for every i ≥ 1, where A is the eventual admissible set mod M=L.
5. For a1=15: admissible set A = {0, 6, 10, 12, 15, 18, 20, 24} mod 30 (T=8 elements, sum of gaps = 30 = L).
6. Max gap bounded empirically by max-element-of-A - second-to-last-element-of-A ≤ M. For a1=35: max gap = 10; for a1=143: max gap = 22; for a1=221: max gap = 34.

### Distinct openings (each a different route)

**Opening A — The Constraint Hypergraph Stabilizes**  
Define the constraint hypergraph H_n = {{p prime : p | a_i} : i ≤ n} (multiset of prime-signature sets). H_n is non-decreasing in the sense that new terms add new hyperedges. The minimal hyperedges of H_n (those not containing a proper sub-hyperedge already in H_n) form the "active constraint set." These minimal hyperedges live in 2^P for P = set of primes appearing in any minimal hyperedge. The claim: minimal hyperedges eventually stabilize. Once they stabilize, the admissibility condition for a_{n+1} is:

  a_{n+1} ≡ r (mod M) for some r in A ⊆ Z/MZ, where M = product(P).

The finite-state argument then gives: the successor function f: A → A (the greedy "next admissible residue mod M") is a cyclic bijection on A. So the orbit is purely periodic with T = |A| and L = M.

**Opening B — Mutual Coprimeness Forces Finiteness of Essential Primes**  
Every pair a_i, a_j (i < j) satisfies gcd(a_i, a_j) > 1. This means every pair shares a prime. The "essential primes" (those that are the sole-prime-in-a-constraint) must divide gcd(a_1, a_2, ..., a_k) for all k, which is controlled by a_1. New primes enter only as co-factors, never as sole constraints. This gives the finite P directly from the prime factorization of a_1 (or the first few terms).

Wait — this is NOT quite right for a1=35. The prime 2 enters via a_2=40, which is NOT a factor of a_1=35. So P is not just primes(a_1). But: any new prime q can only become an essential prime (sole constraint) if q | a_i for ALL i (since the term q^k would need gcd(q^k, a_i) > 1 for all i, requiring q | a_i). But that means q | a_1. So singleton constraints are bounded by primes(a_1). More generally, the "minimal constraint sets" are bounded by the prime signatures of the FIRST FEW TERMS, not just a_1. But these are still finite.

**Opening C — All Terms in A; Successor on A Is a Bijection**  
The key observation: for any i < j, gcd(a_i, a_j) > 1 (by the sequence definition). So EVERY term a_i satisfies the constraint from every OTHER term a_j. In particular, once A (the admissible residue class mod M) is defined, EVERY term a_i has a_i mod M ∈ A. There is no "transient phase" — the sequence visits elements of A from n=1.

Once A is established, the successor function f on A (cyclic successor in the sorted order of A mod M) is a bijection (cyclic rotation), giving PURE periodicity T = |A|, L = M from the very first term.

This is analogous to **aimo-0514**: the deterministic process is reversible (or more precisely, the state transition is a bijection on the finite state space), giving purely periodic orbits rather than eventually periodic ones.

**Opening D — Bounded Gaps via Product Admissibility**  
After the essential prime set P = {p_1, ..., p_k} is identified, note that M = p_1 * ... * p_k is itself admissible (it shares factor p_i with any term divisible by p_i, and every term is divisible by some p_i since every term must share a factor with a_1, ..., which collectively cover P). So multiples of M are "universal admissibles." Within any window of length M after a_n, a multiple of p_i (for at least one i) exists. This gives gap ≤ M. More precisely: the gaps g_n are bounded by the maximum gap in the cyclic order of A mod M, which is at most M.

**Opening E — Finite-State Machine via Residues mod M**  
After H stabilizes, define state = (a_n mod M). The transition (a_n mod M) ↦ (a_{n+1} mod M) is a deterministic function on the finite set A ⊆ Z/MZ. Since f: A → A is a bijection (injective since f is a cyclic-order successor function), the orbit is finite and purely periodic. All terms have residue in A. Therefore, the period of the sequence (a_n mod M) equals |A|, and the actual gaps g_n = a_{n+1} - a_n are determined by (a_n mod M). So the gap sequence is periodic with period T = |A|, and L = M (the total increase per full cycle of A).

### Load-bearing steps and hardest foreseen step

**Step 1 (easiest):** Show gcd(a_i, a_j) > 1 for all pairs i ≠ j. This is trivial from the definition (the sequence rule requires gcd > 1 with all previous terms, so by transitivity of the binary gcd relation... wait, NOT by transitivity but directly from the definition: a_j requires gcd(a_j, a_i) > 1 for all i < j).

**Step 2 (key — HARDEST):** Show the constraint hypergraph H_n stabilizes to H_∞ after finitely many steps, with H_∞'s minimal hyperedges involving only finitely many primes (giving a finite M). 

The argument: 
- At any step, a new term t = a_{n+1} must share a factor with a_n (in particular). So primes(t) ∩ primes(a_n) ≠ ∅.
- Let p ∈ primes(t) ∩ primes(a_n). Then the constraint from t is {p, ...} which contains p.
- For this NOT to add a new minimal constraint, we need some existing minimal constraint S ⊆ {p, other primes of t} (S must be a subset of primes(t)).
- The existing minimal constraints include the constraint from a_n itself (which contains p). If {p} alone is a minimal constraint, done. Otherwise, the constraint from a_n is {p, q_1, ...} for some other primes q_i. For {p, q_1, ...} ⊆ primes(t), we need a_n's primes ⊆ primes(t). This is not guaranteed.

This step is the genuinely hard part. The key insight (which the problem likely requires) is:

**Sub-claim**: The set of primes appearing in any MINIMAL constraint hyperedge is the same as the set of primes appearing in the "closed" prime system determined by the sequence. Once the sequence reaches a "balanced" state where every prime in P is covered by every minimal constraint set, no new minimal constraints can appear.

Alternatively, use the following: the set A (admissible residues mod M) is a SELF-CONSISTENT set. This means: if r ∈ A, then r satisfies gcd(r, s) > 1 for every s ∈ A. This self-consistency means that once the sequence reaches residues in A, all subsequent terms also have residues in A, and the constraints don't grow further.

The proof that A is self-consistent: by induction, every term a_i has a_i mod M ∈ A, and the constraint from a_i (for future terms) is "share a factor with a_i mod M", which is already guaranteed by the property that A is self-consistent.

**Step 3 (medium):** Prove that the successor function on A is a bijection (cyclic shift). This follows immediately: f: A → A sends r to the next element of A in sorted cyclic order mod M. This is clearly a bijection (it's a cyclic permutation of A).

**Step 4 (easy given Step 3):** The sequence (a_n mod M) is purely periodic with period |A| = T, and L = M. Therefore a_{n+T} = a_n + L for all n.

### The hardest foreseen step (elaborated)

The crux is **showing that H_∞ (the eventual constraint hypergraph) has finitely many minimal edges and involves only finitely many primes**.

One approach: Show that P (the set of primes in any minimal constraint) is contained in the set of primes ≤ max(a_1, ..., a_k) for some fixed k. Since a_1, ..., a_k are finite, there are finitely many primes to worry about.

Actually: here's a cleaner argument. Consider the first time a prime q appears in the sequence (as a factor of some term a_k). This term a_k is admissible, so gcd(a_k, a_1) > 1, meaning a_k shares a prime with a_1. If q is new (not in primes(a_1)), then a_k must share another prime p ∈ primes(a_1) with a_1. So a_k = q * r where p | r. The constraint from a_k is "divisible by q or some prime of r". The prime p ∈ primes(a_1) is in r, so the constraint from a_k is "divisible by q or p or ...". Since the constraint from a_1 is "divisible by some prime of a_1" (which includes p), the constraint from a_k is dominated by: if the constraint from some earlier term is {p}, that dominates {p, q}. But the constraint from a_1 is {primes of a_1}, not {p} alone...

I think the cleanest route is:

**Finiteness of P via the greedy bound**: There exists a constant C (depending only on a_1) such that a_{n+1} ≤ a_n + C for all n. Given this, the sequence a_n ≤ a_1 + C*n. Any new prime q first appears in some term a_k ≤ a_1 + C*k. But also q > (term before it in the sequence), so q can be arbitrarily large... This doesn't immediately bound P.

Alternatively (and this seems correct from experiments): The number of primes p that ever enter ANY minimal constraint is bounded by the count of primes needed to "witness" constraints from a_1, a_2, .... For a1 = p*q (product of two primes), the primes P grows to include 2, 3, ..., but only up to a specific finite bound determined by the first few terms' interaction.

The cleanest argument I can see: 

A prime q enters the "essential set" P iff there exists a term a_k in the sequence with gcd(a_k, M_prev) = 1 (coprime to all previous essential primes) where M_prev is the product of primes already in P. But a_k must share a factor with a_{k-1}, and a_{k-1} has a prime from P_prev (by induction). So a_k shares a prime p_prev with a_{k-1}, meaning p_prev | a_k. Thus a_k is NOT coprime to M_prev (it has factor p_prev). So q cannot be a "pure" new prime in the minimal constraint from a_k — the constraint contains p_prev. But p_prev ∈ P_prev, so the constraint from a_k is not minimal (it's dominated by any constraint that contains only p_prev).

WAIT. This IS the key argument! Let me state it precisely:

**Claim**: No new prime ever becomes part of P (the essential prime set) after the initial primes of a_1 are in P.

**Proof**: Suppose q is a prime not in P (where P = primes(a_1) initially). For q to enter P, there must be a term a_k that is a power of q (so that the constraint from a_k is {q} alone — a singleton). For a_k = q^m to be in the sequence:
- gcd(q^m, a_1) > 1, requiring q | a_1. But q ∉ primes(a_1) by assumption. Contradiction.

So singleton constraints {q} for q ∉ primes(a_1) never appear. ✓

But P is NOT just primes(a_1)! For a1=35, P includes {2,3,5,7} but 2 and 3 are not primes of a_1=35. So the above argument only handles SINGLETON constraints, not non-singleton ones.

The full argument needs more care. Let me think about what "essential" means more carefully.

Actually, the above argument shows: primes appearing as SINGLETONS in minimal constraints ⊆ primes(a_1). But minimal constraints can be non-singletons (like {2,5} or {3,5}). The primes in non-singleton minimal constraints can be primes NOT in a_1.

For the full argument: Consider the smallest admissible number greater than 0 (or greater than any fixed value). This is determined by the system of constraints. The "essential primes" are those that appear in the support of this minimum-cost admissibility structure. They're bounded because the first few terms determine the structure, and the structure only involves primes ≤ max(a_1, ..., a_k) for small k (roughly 2-5 terms).

Actually, let me just accept the empirical fact and note that the key lemma (stabilization of H) is the crux that needs a careful proof, and state the approach clearly.

### Approach for "all n" periodicity (not just eventual)

The crucial structural fact: gcd(a_i, a_j) > 1 for ALL i ≠ j. Therefore every a_i is "admissible" with respect to every other a_j. This means:
- For all i, a_i satisfies the constraint imposed by a_j for every j ≠ i.
- In particular, if H_∞ is the eventual constraint hypergraph and A is the admissible residue class mod M_∞, then a_i mod M_∞ ∈ A for ALL i ≥ 1 (since a_i satisfies all constraints from all other terms).

Therefore the sequence (a_n mod M_∞) has ALL terms in A from the very start (n=1). The successor function f: A → A is a cyclic bijection, and the sequence visits each element of A exactly once per period. Hence the period starts at n=1.

This is analogous to **aimo-0016** (crux: upgrade from "eventually holds" to "holds for all n" using the structure of the rule).

### Candidate technique

**Finite-state machine / pigeonhole on modular residues**: identify M = product of essential primes, define A = admissible residues mod M, observe (a_n mod M) ∈ A for all n and evolves as a bijection on A (cyclic successor). Pure periodicity with T = |A|, L = M.

**Cheap-kill candidates**: 
- Parity: if a_1 is even, all terms are even (gcd(a_n, a_1) > 1 and a_1 even → a_n even), giving T=1, L=2 trivially.
- If a_1 = p (prime), all terms must be divisible by p, giving T=1, L=p trivially.
- If a_1 = p*q (semiprime), the structure becomes non-trivial (the interesting case).

### Knowledge-base entries to use

- **Pigeonhole / extremal principle** (Combinatorics section): the finite-state argument uses pigeonhole over the finite set A.
- **Order of an element / eventual periodicity** (Number Theory section): sequences are eventually periodic mod m — this is the direct analogue.
- **Divisor analysis / gcd structure** (Number Theory): the core property gcd(a_i, a_j) > 1 for all pairs.
- **Modular arithmetic, CRT** (Number Theory): the admissibility condition mod M.
- **Bertrand's postulate** (Number Theory): useful for bounding where new primes can first appear.
- **Invariants & monovariants** (General Proof Methods): H_n is a monotone non-decreasing hypergraph.

### Analogous past problems (cruxes)

1. **aimo-0514** [combinatorics/processes-and-algorithms]: "Show a deterministic process is reversible so its state graph is a union of cycles, forcing the orbit to be purely periodic rather than eventually periodic." How used: the state-to-state map (successor function on A) is a bijection on a finite set, giving pure (not eventual) periodicity. This is the MOST ANALOGOUS crux.

2. **aimo-0016** [combinatorics/induction-and-construction]: "Upgrade an 'equal infinitely often' shift relation on state-tuples to 'holds for all indices' by a one-step downward induction." How used: extends eventual periodicity to all n by using the structural property that the sequence is deterministic and the state already lies in A from n=1.

3. **aimo-0678** [number_theory/modular-arithmetic-and-CRT]: "Once one coordinate of a coupled integer recurrence is bounded, reduce the other coordinate modulo the lcm of the bounded coordinate's attainable values, turning the state pair into a deterministic map on a finite set." How used: the "bounded coordinate" is the constraint hypergraph H (eventually stable), and the other coordinate is a_n mod M, which lives in the finite set A.

### Prior progress

None (fresh workspace).

### Dead ends (do not retry)

None yet (first round).

### Small-case / intuition notes (conjectured)

1. **Conjecture**: L = M = product of primes in the essential prime set P. T = number of admissible residues mod M. The sequence visits each element of A exactly once per period.

2. **Conjecture**: The essential prime set P is finite and determined by the "constraint closure" of the first few terms. For a1=p*q (semiprime), P can include primes 2 and 3 (which appear early in the sequence to satisfy gcd conditions), so P ⊄ primes(a_1).

3. **Empirical gap bound**: max(g_n) ≤ M. Tightest bound observed: for a1=221, max gap = 34 = 2*17 (which is a factor of M=6630 but not M itself). So the bound is tighter than M in practice.

4. **Pure periodicity from n=1** (strongly supported by all experiments): the sequence (a_n mod M) is purely periodic from n=1 because every term satisfies gcd(a_i, a_j) > 1 for all j, placing every term in A from the start.

5. **Surprise**: The prime 5 appears in P for a1=221=13*17 (L includes 5), but NOT for a1=143=11*13 (L excludes 5). Why? For a1=221, the greedy rule forces a term like 255=3*5*17 early on, making {3,5,17} a minimal constraint and 5 essential. For a1=143, the sequence avoids terms with 5 as an essential prime. This shows P is NOT determined by a_1 alone — it depends on the first few greedy choices.

6. **Hardest gap in the proof**: showing that the constraint hypergraph H eventually stabilizes to H_∞ with finitely many minimal edges, all involving primes in a fixed finite set P. This requires showing new terms either (a) have constraints dominated by existing ones, or (b) the process of "discovering" new constraints terminates. The failure mode: new minimal constraints keep appearing forever, making P infinite. But empirically this never happens, and the structural reason is that new large primes always enter via terms that have existing essential-prime co-factors, making their constraints subsumed.
