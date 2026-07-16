## imo-2026-06

### Computational Findings (Lens: Simulation and Empirical Structure)

---

#### 1. Data Tables: Sequences for Many Starting Values

All sequences computed with Python/sympy; period detection by matching repeated difference-blocks over 200–400 terms.

| a_1 | prime factors of a_1 | T | L | prime factors of L |
|-----|----------------------|---|---|--------------------|
| 2   | {2}       | 1  | 2   | {2}         |
| 3   | {3}       | 1  | 3   | {3}         |
| 4   | {2}       | 1  | 2   | {2}         |
| 5   | {5}       | 1  | 5   | {5}         |
| 6   | {2,3}     | 1  | 2   | {2}         |
| 9   | {3}       | 1  | 3   | {3}         |
| 10  | {2,5}     | 1  | 2   | {2}         |
| 15  | {3,5}     | 8  | 30  | {2,3,5}     |
| 21  | {3,7}     | 1  | 3   | {3}         |
| 33  | {3,11}    | 1  | 3   | {3}         |
| 35  | {5,7}     | 34 | 210 | {2,3,5,7}   |
| 45  | {3,5}     | 8  | 30  | {2,3,5}     |
| 55  | {5,11}    | 1  | 5   | {5}         |
| 65  | {5,13}    | 58 | 390 | {2,3,5,13}  |
| 77  | {7,11}    | 18 | 154 | {2,7,11}    |
| 85  | {5,17}    | 1  | 5   | {5}         |
| 91  | {7,13}    | 20 | 182 | {2,7,13}    |
| 105 | {3,5,7}   | 58 | 210 | {2,3,5,7}   |
| 997 | {997}     | 1  | 997 | {997}       |

**Key fact**: The period holds from n=1 (not just eventually). For a1=35, the difference block [5,2,3,5,10,10,5,5,4,6,10,5,5,10,6,4,5,5,10,10,5,3,2,5,5,10,5,5,10,10,5,5,10,5] repeats exactly from position 0 onward (verified at positions 0,34,68,102).

---

#### 2. The Eventual Prime Structure ("Core Primes")

For each starting value, the sequence is eventually (in fact, immediately) supported on a fixed finite set of "core primes" P_core. Every term in the sequence is divisible by at least one prime in P_core.

The core prime set is determined by early dynamics:
- a1 = p (prime): P_core = {p}. Sequence = all multiples of p.
- a1 = 2*q: P_core = {2}. (2 dominates immediately: a2 = first even > a1.)
- a1 = 3*q (q > 5): P_core = {3}. (27 = 3^3 enters early, forcing all future terms divisible by 3.)
- a1 = 3*5 = 15: P_core = {2,3,5}. (2 enters via 18=2*3, then 20=2*5 enters before 27 can "lock in" 3.)
- a1 = 5*7 = 35: P_core = {2,3,5,7}. (42=2*3*7 enters after 40=2^3*5, before 5-multiples can dominate.)
- a1 = 5*11 = 55: P_core = {5}. (65=5*13 enters before 66=2*3*11 can; then 65 blocks 11-multiples.)
- a1 = 7*11 = 77: P_core = {2,7,11}. (84=2^2*3*7, 88=2^3*11, 98=2*7^2 establish the constraint.)

---

#### 3. The "Constraint Antichain" and Its Stabilization

**Central empirical observation**: After a small number of terms (3–5 in all tested cases), the sequence's "essential constraint set" A stabilizes to a fixed antichain of prime sets. After stabilization:

- Any valid next term t must have its prime set hit each element of A.
- Every valid prime set automatically CONTAINS some element of A as a subset.
- Therefore: no new essential constraints are ever added after stabilization.

**Explicit examples**:

For a1=15: After seeing {15=3*5, 18=2*3, 20=2*5}, the antichain is A = {{3,5}, {2,3}, {2,5}}.
- Any prime set that hits {3,5}, {2,3}, {2,5} simultaneously must contain {3,5} or {2,3} or {2,5}.
- Proof: if not containing {3,5} → missing 3 or 5. If missing 3: hits {2,3} only via 2, hits {2,5} only via 2 or 5 — but must hit {3,5} via 5. OK if has 5 and 2, which is {2,5} ⊂ prime set. If missing 5: hits {2,5} only via 2 or (missing 5 means...), hits {3,5} only via 3, hits {2,3} via 2 or 3. If has 3 and 2: {2,3} ⊂ prime set. So always contains some element of A.
- Self-covering property: A is "self-covering" — every set hitting all elements of A contains some element of A.

For a1=77: After {77=7*11, 84=2^2*3*7, 88=2^3*11, 98=2*7^2}: antichain A = {{7,11}, {2,11}, {2,7}}.
- Any prime set hitting all three must contain {7,11} or {2,11} or {2,7}. (Same argument as above with 3 two-element sets.)
- Self-covering property holds.

---

#### 4. The Eventual Periodic Set V

After the antichain A = {P_1, ..., P_k} stabilizes, the valid set is:
  V = {m ∈ Z_{>0} : prime_set(m) ∩ P_i ≠ ∅ for all i}

This set V is determined by congruence conditions modulo L = product of all primes appearing in A's elements, and is periodic with period L.

**Verified cases**:
- a1=15, A={{3,5},{2,3},{2,5}}: V = {n : n divisible by ≥2 of {2,3,5}}. L=30, T=8.
  VERIFIED: seq15 == [n ≥ 15 : n divisible by ≥2 of {2,3,5}] for all 200 terms.

- a1=35, A={{5,7},{2,5},{2,3,7},{3,5}}: V = {n : (5|n and (2|n or 3|n or 7|n)) or 42|n}.
  VERIFIED: seq35 == expected for all 300 terms.

- a1=77, A={{7,11},{2,11},{2,7}}: V = {n : n divisible by ≥2 of {2,7,11}}. L=154, T=18.

In EVERY tested case, the sequence = all elements of V starting from a1, in increasing order.

---

#### 5. Why the Sequence = V in Order (After Stabilization)

Key: a_{n+1} = smallest integer > a_n sharing a factor with EVERY previous a_i.

After A stabilizes: "sharing a factor with every previous a_i" ≡ "having prime set hitting each P_i in A" ≡ "being in V".

So a_{n+1} = smallest element of V exceeding a_n. The sequence is the sorted enumeration of V. Since V is periodic with period L and has T elements per period, a_{n+T} = a_n + L. ✓

---

#### 6. Why the Antichain Must Stabilize (Mechanism)

The self-covering property of A is the key: once A has this property, no new essential constraints can ever be added (all future terms' prime sets contain some element of A). The proof needs to show A eventually reaches this state.

Empirically, this happens quickly (within 3–5 terms). The mechanism:
- The "small" primes enter early (the sequence's second term is small: just slightly > a1, sharing a prime factor with a1).
- Once a "covering configuration" of small primes is established, large primes can only enter paired with small ones (hence subsumed).
- The competition between primes is decided in the first few steps by which bridge terms (like 42=2*3*7) enter before alternatives (like 5^2=25 for a1=35).

**The only delicate case**: When the starting value a1 = p*q (two large primes, p < q), and neither p nor q is small enough to become the sole hub, the sequence establishes a more complex 3-prime antichain involving 2, p, q (like {2,p,q} style). This always happens within 4 terms.

---

#### 7. Distinct Proof Openings

**Opening A: Constraint stabilization via self-covering antichains.**
Define the antichain A of essential prime constraints. Show A becomes self-covering in finitely many steps (either directly or by showing the "free" structure shrinks monotonically). Then V is periodic. Then sequence = sorted V.

**Opening B: Direct "eventual all-multiples" reduction.**
Show that for every a1, there exists a prime p | a1 such that all but finitely many terms are divisible by p (single-prime domination). Then show the sequence is eventually all multiples of p (if p dominates), which is arithmetic with T=1, L=p. Handle the non-dominating cases (a1=15, 35, etc.) separately. [Note: this fails for a1=15 where no single prime divides all terms.]

**Opening C: Product moduli / CRT.**
Let L = product of all primes dividing any of a_1,...,a_N for a large N. Consider the sequence modulo L. The valid set modulo L is finite (determined by congruences). By pigeonhole, the sequence of residues mod L is eventually periodic. Then lift to get a_{n+T} = a_n + L.

**Opening D: Greedy "covers the valid set" argument.**
Show V is non-empty and periodic (directly). Then argue the greedy sequence walks through ALL of V: at each step, the minimum of V \ {a_1,...,a_n} that exceeds a_n is chosen. Since V ∩ [a_n+1, a_n+L] is non-empty (V has bounded gaps), the sequence hits every element of V in order.

---

#### Candidate Techniques from Knowledge Base

- **Modular arithmetic and CRT**: The valid set V is defined by congruences; periodicity follows from CRT once the essential constraints are identified.
- **Invariants/monovariants**: The constraint antichain A is a monovariant (only grows) and is bounded above (by the self-covering property), so it stabilizes.
- **Pigeonhole**: The sequence of residues mod L is eventually periodic (finitely many residues).
- **Divisor analysis / gcd structure**: The essential tool throughout; the "self-covering" property of antichains of prime sets is the key combinatorial-number-theoretic fact.

---

#### Analogous Past Problems (Cruxes)

- **aimo-0030** (divisibility-and-gcd): Deals with sequences where terms must share "allowed primes" with each other. The crux move "produce a number with the same allowed-prime signature but no forbidden large prime factors" is adjacent to our problem's structure (the large primes are always "subsumed" by small primes in our sequence). Not a perfect match but most analogous.

- **aimo-0678** (sequences with gcd/lcm recurrence): The approach of tracking a monovariant (the sum a_n + b_n) and showing eventual constancy is analogous to tracking the valid set V_n and showing eventual stability.

- No exact analogues found in the corpus; this problem's structure (self-covering antichains of prime sets) appears novel.

---

#### Prior Progress

None (round 1, no prior approaches).

#### Dead Ends

None yet.

---

#### Small-Case / Intuition Notes (All Conjectural)

1. **Conjecture (verified to 400 terms for a1=35)**: The sequence from a_1 = 35 is exactly all n ≥ 35 satisfying "(5|n and (2|n or 3|n or 7|n)) or 42|n", with T=34, L=210 from n=1.

2. **Conjecture**: For a1 = p*q where p < q are odd primes with q ≡ 1 (mod p) [so the "bridging" term 2*q shares factors easily]: the sequence collapses to all multiples of p. This is not the right criterion — the actual criterion is whether a "non-p-multiple" term can enter before p^2 locks in.

3. **Conjecture**: For ALL starting values a1, the period T and period-sum L are:
   L = product of all "essential primes" (those in the eventual antichain A).
   T = |{r ∈ [1..L] : r satisfies all constraints in A}|.

4. **The critical structural fact (verified, not yet proved)**: The antichain A satisfies the "self-covering property" — every valid prime set contains some element of A as a subset. This is the mechanism preventing unbounded growth of A.

5. **The sequence is globally (not just eventually) periodic**: a_{n+T} = a_n + L holds for ALL n ≥ 1, with T and L as above. No transient phase in the examples tested.
