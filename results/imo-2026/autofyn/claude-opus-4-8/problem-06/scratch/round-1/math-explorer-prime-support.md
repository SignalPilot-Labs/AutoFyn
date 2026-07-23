## imo-2026-06 (Prime-Support / Finite-Prime-Set lens)

### Empirical findings (run Python experiments, labeled as conjecture where unproved)

**Starting values tested:** a_1 ∈ {2, 3, 4, 6, 10, 15, 30, 35, 77, 91, 105, 143, 210, 323}.

**Observed periods (T, L) and essential primes:**
- a_1 = 6 = 2·3: all-even sequence. T=1, L=2. Essential primes: {2}.
- a_1 = 15 = 3·5: period T=8, L=30=2·3·5. Diffs repeat: [3,2,4,6,6,4,2,3].
- a_1 = 30 = 2·3·5: all-even. T=1, L=2.
- a_1 = 35 = 5·7: T=34, L=210=2·3·5·7. Stabilizes at step n=5.
- a_1 = 77 = 7·11: T=18, L=154=2·7·11. Stabilizes at step n=5.
- a_1 = 91 = 7·13: T=20, L=182=2·7·13.
- a_1 = 143 = 11·13: T=64, L=858=2·3·11·13.
- a_1 = 323 = 17·19: T=94, L=1938=2·3·17·19.

**Conjecture:** The period L is always the product of a finite set of "essential primes" containing primes(a_1), always including 2 (when a_1 is odd), and sometimes 3.

**The admissible set A_n:** At step n, the admissible set is A_n = {m > a_n : gcd(m, a_i) > 1 for all i ≤ n}. Experiments verify:
- For a_1=15: A_∞ = {m : 6|m or 10|m or 15|m}, period 30, with 8 elements per period. ✓
- For a_1=77: A_∞ = {m : 14|m or 22|m or 77|m}, period 154, with 18 elements per period. ✓
- For a_1=35: A_∞ = {m : 10|m or 15|m or 35|m or 42|m}, period 210, with 34 elements per period. ✓

Verified by checking all terms in 100-term sequences lie in the stated A_∞.

**Stabilization:** For a_1=77 and a_1=35, A_n stabilizes to A_∞ at step n=5 (verified computationally). After step 5, new terms add NO new constraints to the admissible set.

---

### Distinct sub-openings inside the Prime-Support framing

**Opening A — The "every term has a P_1-prime" anchor.**
Set P_1 = primes(a_1). Since a_n must share a factor with a_1 (by the greedy condition applied inductively), gcd(a_n, a_1) > 1 for ALL n ≥ 2. Hence every term a_n is divisible by at least one prime p ∈ P_1. This is the universal anchor: A_n ⊆ {m : ∃p ∈ P_1, p|m} for all n.

**Opening B — Finite-lattice stabilization of the constraint formula.**
The admissible set A_n is defined by the monotone Boolean formula:
  φ_n(m) = ∧_{i=1}^{n} (∨_{p|a_i} p|m).
The P_1-RESTRICTED formula ψ_n(m) = ∧_{i=1}^{n} (∨_{p ∈ P_1, p|a_i} p|m) uses only the |P_1| atoms {p|m : p ∈ P_1}. Since the lattice of monotone Boolean functions on P_1 is FINITE (Dedekind number, finite), ψ_n stabilizes after finitely many steps. The key claim is that the full formula φ_n also stabilizes — because once A_n achieves the "clique property" (see below), new terms add only redundant constraints.

**Opening C — The Clique Property as the stabilization criterion.**
Key structural observation: any two TERMS of the sequence share a common factor (since a_n is defined to share a factor with every a_i for i < n). So the sequence is a clique in the "shares-a-factor" graph. The admissible set A_n is NOT always a clique (initially A_1 = {m : some p ∈ P_1 divides m} contains coprime pairs like 7^2 and 11^2 for a_1=77). But as terms are added, coprime pairs get eliminated:

  - When a_k is added, all m ∈ A_{k-1} with gcd(m, a_k) = 1 are REMOVED from A_k.
  - Once A_n has the clique property (any two elements share a factor), the next term a_{n+1} ∈ A_n satisfies gcd(m, a_{n+1}) > 1 for ALL m ∈ A_n (since a_{n+1} ∈ A_n and A_n is a clique). So A_{n+1} = A_n — no shrinkage.
  - Therefore: once A_n achieves the clique property, it stabilizes forever.

This reduces the problem to: **prove A_n achieves the clique property after finitely many steps.**

**Opening D — Density argument for clique achievement.**
The admissible set A_n is a union of arithmetic progressions. Its density (number of elements per unit interval) is bounded below by δ > 0 (since the sequence is infinite). As new terms are added, the density can decrease but only by removing "bad pairs" (coprime elements). Since the AP-structure constrains how many coprime pairs can exist (bounded by the number of distinct prime-support types), after finitely many steps all coprime pairs are eliminated.

**Opening E — CRT / modular characterization of A_∞.**
A_∞ is characterized by a finite set of conditions each of the form "m is divisible by at least one prime in S_j" for various prime sets S_j. The period L = lcm(∏S_j for all j) = product of essential primes (observed to be squarefree in all experiments). The number of admissible residues per period is T. The greedy sequence on A_∞ picks the next element of A_∞ above a_n, producing differences that cycle through T values with sum L. So a_{n+T} = a_n + L.

---

### What is load-bearing (hardest steps)

**Step 1 (HARD): Prove A_n eventually stabilizes (achieves the clique property).**

The critical gap: showing that after finitely many steps, any two elements of A_n share a common factor. 

Best argument I see: 
- P_1 is finite, so there are finitely many "types" of elements in A_n (classified by which P_1-primes they are divisible by). 
- Initially, there may be coprime elements of different types (e.g., divisible by 7 only vs. divisible by 11 only, for P_1={7,11}).
- Each new term from one type forces elements of the other type to acquire a shared factor (e.g., a term divisible by 7 but not 11 forces future elements divisible only by 11 to ALSO be divisible by 2, since gcd(m, 7k)>1 requires 2|m or 3|m or 7|m when 11|m only).
- There are only finitely many (at most 2^|P_1|-1) types. The "conflict graph" between types must eventually be resolved. 

**Step 2 (MEDIUM): Prove A_∞ is a union of APs (periodic).**

Once stabilization is established (A_n = A_∞ for n ≥ N), A_∞ = {m : φ_N(m)} where φ_N is a finite conjunction of "divisibility by some prime" conditions. This is a finite Boolean formula over atomic APs {p|m}, hence A_∞ is a finite union/intersection of APs — so it's periodic with period L = product of the relevant primes.

**Step 3 (EASY): Prove greedy on periodic A_∞ gives a_{n+T}=a_n+L.**

If A_∞ is periodic with period L and has T elements per period, then the greedy sequence on A_∞ has exactly T gaps per period of L. So a_{n+T} = a_n + L for all n ≥ N. This is elementary once A_∞ is periodic.

---

### Key structural facts (proved or easily provable)

1. Every term a_n (n≥2) is divisible by some prime in P_1 = primes(a_1). [Proof: gcd(a_n, a_1)>1.]

2. The sequence (a_n) is a "clique": any two terms share a factor. [Proof: by definition, a_n shares a factor with a_m for all m<n.]

3. The admissible set A_n is eventually BOUNDED BELOW by a fixed positive density (since the sequence is infinite, A_n is never empty, and the gap between consecutive admissible elements is bounded). [This follows from existence of a_{n+1}.]

4. A_∞ is periodic: every m ∈ A_∞ can be characterized by its prime-support, and the set of "valid prime-supports" is a finite combinatorial object. [Empirically verified; needs rigorous proof.]

---

### Candidate techniques (pointers, not plans)

- **Monotone Boolean lattice / finite constraint**: The formula for A_n lives in a finite lattice; stabilization follows from finiteness once the right atoms are identified.
- **Sieve / union of APs**: A_∞ as union of APs (inclusion-exclusion over prime products). Period L = product of essential primes.
- **Greedy on periodic sets**: Completely standard once periodicity is established.
- **Pigeonhole on prime-support types**: Force clique property by pigeonhole over the 2^|P_1| type partition.

---

### Cheap-kill candidates

- **Parity**: When a_1 is even (2 ∈ P_1), then 2 | a_n for all n (since a_2 is even: smallest even integer >a_1 shares factor 2). The sequence is all-even, L=2, T=1. This handles the case 2|a_1 immediately.
- **When a_1 is a prime power p^k**: Then P_1 = {p}, and every term must be divisible by p. The sequence is all multiples of p: a_n = a_1 + (n-1)p for n≥1. L=p, T=1. This is trivial.
- **Size bound on L**: L ≤ ∏_{p ∈ essential primes} p. Since the essential primes are bounded by the first few terms of the sequence (which are bounded by a_1 + some small multiple), L is bounded in terms of a_1.

---

### Knowledge-base entries to use

- **Modular arithmetic, CRT**: The admissible set A_∞ is described by congruence conditions, and its period L = lcm of relevant prime products is computable via CRT.
- **Divisor analysis**: gcd structure and the "shares a factor" relation — core to the entire analysis.
- **Pigeonhole**: For the clique property argument: finitely many prime-support types, infinitely many terms, so some type repeats and forces structure.
- **Order of an element, Fermat/Euler**: Periodicity of sequences mod m — used in Step 3.
- **Invariants and monovariants**: The density of A_n is a monovariant (non-increasing), bounded below; used to argue the clique property is reached.

---

### Analogous past problems (cruxes)

**Best match: aimo-0030** (Banana game with coprime moves, subtopic divisibility-and-gcd)
- Crux move: "Two good numbers (P-positions) share a SMALL prime. Proof by minimal counterexample descent: take the smallest pair sharing only big primes and manufacture a smaller violation."
- Why analogous: Our problem also requires showing that elements of a special set (admissible integers) share a common factor, with "big primes" being redundant and "small primes" (from P_1 and the early sequence) being the essential glue. The descent argument for small primes mirrors our "clique property via P_1-anchor" approach.
- The crux move "strip big primes and replace by a small-prime equivalent" is directly applicable to showing that large primes in later terms are always redundant.

**Second match: aimo-0079** (Omega-parity, subtopic sequences-and-recurrences)
- Crux move: "Among infinitely many length-L windows of a {0,1}-valued (parity) function, pigeonhole to find two starting positions whose windows agree termwise."
- Why analogous: A version of this pigeonhole is what forces the "greedy on periodic set → eventually periodic" conclusion once A_∞ is established. The residue sequence mod L is finite-state and periodic.

**Third match: aimo-0144** (coprime-to-n integers, divisibility-and-gcd)
- Crux move: "In each block of length d (a divisor of n), count integers coprime to n using phi(d) — any window of d consecutive integers contains exactly phi(d) integers coprime to d."
- Why analogous: Our T = |A_∞ ∩ [1, L]| is exactly this type of count (elements per period), computed via inclusion-exclusion on the prime structure.

---

### Prior progress

None — this is the first round.

---

### Dead ends (do not retry)

None established yet (first round).

---

### Small-case / intuition notes (labeled as conjecture)

**Conjecture 1:** The period L is always a squarefree integer equal to the product of the "essential primes." The essential primes are always primes(a_1), plus 2 (when 2 ∉ primes(a_1)), plus possibly 3 (in some cases where primes(a_1) are both > 3 and "far apart"). The set of essential primes is always the set of primes dividing the FIRST FEW terms of the sequence.

**Conjecture 2:** The admissible set A_n stabilizes (achieves the clique property) after at most N steps, where N ≤ C * |P_1| * max(P_1) for some absolute constant C. Empirically N ≤ 5 in all tested cases.

**Conjecture 3:** The eventual admissible set A_∞ = {m : (m,a_1,...,a_{N-1} form a clique)}. It has a "covering" structure: m ∈ A_∞ iff m's prime support intersects every "critical clause" derived from the first N terms.

**Conjecture 4 (key structural):** The admissible set A_n, as a set of residue classes mod L, is eventually CONSTANT (does not depend on n for n ≥ N). This is the content of "stabilization."

**Key warning for proof-builder:** The admissible set A_n is NOT simply {m : some p ∈ P_1 divides m}. It is more refined. The admissible set for a1=35 is {10|m or 15|m or 35|m or 42|m}, which excludes many multiples of 5 (e.g., 5 itself) and many multiples of 7 (e.g., 7 itself). The "clique" structure enforces pairwise divisibility, not individual divisibility by P_1 primes.
