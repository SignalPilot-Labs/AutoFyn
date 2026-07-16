## imo-2026-06 (Structure Lens)

### Problem recap
Infinite sequence a_1 < a_2 < ... of integers > 1 where a_{n+1} is the SMALLEST integer > a_n sharing a common factor > 1 with EVERY previous term. Prove there exist T, L > 0 (positive integers) with a_{n+T} = a_n + L for ALL positive integers n.

---

### Computational evidence (reliable, labeled as conjecture unless noted)

| a_1 | T | L | Factorization of L | Stable antichain M* | Verified |
|-----|---|---|---------------------|----------------------|---------|
| 2 | 1 | 2 | 2 | {{2}} | ✓ for 40 terms |
| 3 | 1 | 3 | 3 | {{3}} | ✓ for 40 terms |
| 15 = 3·5 | 8 | 30 = 2·3·5 | primes {2,3,5} | {{2,3},{2,5},{3,5}} | ✓ for 80 terms |
| 21 = 3·7 | 1 | 3 | 3 | {{3}} (27=3^3 appears at n=3) | ✓ for 40 terms |
| 35 = 5·7 | 34 | 210 = 2·3·5·7 | primes {2,3,5,7} | {{5,7},{2,5},{3,5},{2,3,7}} | ✓ for 60 terms |
| 77 = 7·11 | 18 | 154 = 2·7·11 | primes {2,7,11} | {{7,11},{2,7},{2,11}} | ✓ for 50 terms |
| 210 = 2·3·5·7 | 1 | 2 | 2 | {{2}} (via a_1 even, all terms even) | ✓ for 30 terms |

**The period T equals the number of valid residue classes mod L.** For example, for a_1=77: T=18, and exactly 18 residue classes mod 154 satisfy the stable antichain constraint. For a_1=15: T=8, and exactly 8 residue classes mod 30 satisfy it.

**Crucially, the claim a_{n+T} = a_n + L holds for ALL n starting from n=1**, not just eventually. The first term a_1 is always in the correct residue class for the stable antichain.

---

### Key structural objects

**Prime-set antichain (M_n):** For each term a_i, let P_i = set of prime factors. The *minimal antichain* M_n is the antichain of inclusion-minimal sets among {P_1,...,P_n}. The effective constraint on a_{n+1} is: a_{n+1} must be a *hitting set* of M_n (share at least one prime with each element of M_n).

**Valid set (V_n):** V_n = {m : gcd(m, a_i) > 1 for all i ≤ n}. This is non-increasing: V_0 ⊇ V_1 ⊇ V_2 ⊇ ....

**Infinite-divisibility set (P*):** P* = {primes p : p | a_n for infinitely many n}. Computationally: P* = {2,3,5} for a_1=15; P* = {2} for a_1=210; P* = {2,7,11} for a_1=77; P* = {2,3,5,7} for a_1=35.

---

### The critical structural lemma (proved)

**Lemma 1 (P*-intersection):** For every i, P* ∩ P_i ≠ ∅. Equivalently, every term has at least one prime factor that divides infinitely many terms.

*Proof:* If all prime factors of a_i divided only finitely many terms, there would be a last term a_M containing any prime of a_i. For all n > M, gcd(a_n, a_i) = 1, contradicting that a_n must share a prime with a_i. ∎

**Corollary:** P* ≠ ∅.

---

### The self-reinforcing antichain phenomenon

**Definition:** Call M* *self-reinforcing* (stable) if every hitting set of M* contains some element of M* as a subset.

**Key computational finding:** The stable antichains M* in all examples have this property. For example:
- M* = {{2,3},{2,5},{3,5}} (a_1=15): I verified algebraically that every hitting set contains {2,3}, {2,5}, or {3,5}. Case analysis: if 5∈P, then P hits {2,3} via some prime, forcing {2,3}⊆P or {3,5}⊆P; if 5∉P, then 3∈P (to hit {3,5}) and 2∈P (to hit {2,5}), giving {2,3}⊆P. In all cases P is dominated.
- M* = {{5,7},{2,5},{3,5},{2,3,7}} (a_1=35): Verified: ZERO valid hitting sets exist that are not dominated by an element of M*. (Exhaustive check over all subsets of {2,3,5,7,11,13}.)

**Consequence:** Once the antichain reaches a self-reinforcing state M*, it never changes. Every future valid term has prime set dominated by some Q ∈ M*, so no new minimal element enters M*.

---

### How the antichain evolves and stabilizes

For a_1=15:
- After term 1 (a_1=15): M = {{3,5}}
- After term 2 (a_2=18): M = {{3,5},{2,3}}
- After term 3 (a_3=20): M = {{3,5},{2,3},{2,5}} — **self-reinforcing! Stable from here.**

For a_1=35:
- Terms 1-4 grow M: {{5,7}} → {{5,7},{2,5}} → {{5,7},{2,5},{2,3,7}} → {{5,7},{2,5},{2,3,7},{3,5}}
- After term 4: self-reinforcing. **Stable from here.**

For a_1=210: The antichain M_n KEEPS GROWING (terms 2,3,4,... introduce {2,53},{2,107},{2,3},{2,109},...) but the EFFECTIVE VALID SET is already {even numbers} from term 1. The growing antichain is irrelevant because all elements contain {2}, and any even number hits all of them simultaneously.

**This shows: the right object to track is not the antichain itself but the EFFECTIVE VALID SET V_L** (the set of integers satisfying the stable constraint mod L = lcm of primes in the stable constraint).

---

### Why L = product of primes in P* works (or lcm thereof)

Once M* is stable and every element of M* has primes only from P*:

For any integer m and any a_i: gcd(m, a_i) > 1 via some prime p ∈ P* ∩ P_i (by Lemma 1 and the self-reinforcing property, which ensures the shared prime in the stable constraint is in P*).

Since p ∈ P* ⊆ primes(L): p | L, so p | m ↔ p | (m + L). Therefore gcd(m, a_i) > 1 ↔ gcd(m+L, a_i) > 1.

**Conclusion:** The valid set is periodic mod L = lcm of primes in P*.

---

### The periodicity mechanism (once L is established)

**Step 1:** The valid residue classes mod L form a finite set R ⊂ {0,1,...,L-1} of size T.
- R consists of those residues r such that for each Q ∈ M*, some prime in Q divides r.
- In example a_1=15: R = {0,6,10,12,15,18,20,24} (mod 30), exactly 8 elements.
- In example a_1=77: R is exactly 18 residues mod 154.

**Step 2:** The greedy "next valid integer > a_n" function is periodic mod L: if m ≡ r (mod L), the gap to the next valid integer is the gap from r to the next element of R mod L.

**Step 3:** The sequence a_1, a_2, ..., a_T, a_{T+1}, ... cycles through the residues of R: a_n ≡ r_n (mod L) where r_1, r_2, ..., r_T, r_1, r_2, ... cycles with period T and each a_{n+T} = a_n + L.

**Why this holds for ALL n (not just eventually):** Every a_i has a prime in P* (Lemma 1). For a_n sharing a prime with a_i, the self-reinforcing property of M* guarantees the shared prime is in P* (or rather, a_n's prime set already "covers" all elements of M*, so a_n hits M* via primes in P*). Since p ∈ P* and p | L, the shift by L is transparent.

---

### What lemmas the proof needs

**Lemma 1 (proved above):** P* ∩ P_i ≠ ∅ for all i.

**Lemma 2 (KEY, needs proof):** P* is finite.
- *Why believed:* In all examples P* is finite. A heuristic: if infinitely many primes were in P*, the density of valid integers would go to 0 (they'd need to hit infinitely many independent prime constraints), but the sequence is always defined.
- *Hard to prove rigorously.* Possible angle: by Bertrand's postulate, any interval (a_n, 2a_n) contains a prime q. If q were in P* (dividing infinitely many terms), those terms would all be multiples of q spaced q apart. But these multiples must also satisfy other constraints, leading to a sieving argument. Still unclear how to bound |P*|.

**Lemma 3 (KEY, needs proof):** The minimal antichain M* (over all terms) is self-reinforcing (stable). Equivalently, every integer sharing a prime with each a_i has prime set dominated by some element of M*.
- *This is the hardest step.* It's equivalent to saying: the sequence eventually "fills in" all the prime constraints so the stable state is reached.

**Lemma 4:** Once M* is stable and L = lcm(P*), the greedy sequence is periodic with T = |valid residues mod L|, shift L, from the beginning (n = 1).

---

### Distinct proof openings (rival approaches for outliner)

**Opening A (Prime power route):**
If any term a_k is a prime power p^m, then all subsequent terms are divisible by p (since gcd(a_n, p^m) > 1 forces p | a_n). So p ∈ P* and the constraint "p | a_n" dominates. Show the constraint system then simplifies: if P* has a "universal" prime p (dividing all terms from some point), the valid set becomes {m : gcd(m, a_i) > 1 for all i, and p | m} which is periodic mod (p * other primes). Induct on the structure.
- *Hard step:* What if no term is a prime power? (This happens for a_1=15, a_1=35, etc.)

**Opening B (Antichain stabilization via descent):**
Track the multiset of sizes in the minimal antichain M_n. Show it eventually reaches a fixed multiset (self-reinforcing state). The key monovariant: each time a strictly smaller prime set enters the antichain (replacing a larger one), some total "weight" decreases. But the antichain can also GROW (new elements added), so the weight is not simply monotone. A more subtle argument is needed, perhaps tracking the number of "non-redundant" elements.
- *Hard step:* Identifying the correct monovariant.

**Opening C (Density argument, bypassing antichain):**
Show directly that for all sufficiently large n, a_{n+1} depends only on a_n mod L. Key: show that the "next valid" function f(m) = min{m' > m : m' ∈ V_n} stabilizes as n → ∞. This requires showing that adding more terms eventually does NOT increase the constraint (no new primes become "effective"). The effective primes stabilize because each new term's prime set is dominated by existing constraints. Hard to make rigorous without first proving Lemma 3.

**Opening D (Structural sieving with Bertrand/Dirichlet):**
Use Dirichlet's theorem (primes in AP) or Bertrand's postulate to show that the sequence eventually lives in a specific union of arithmetic progressions. Argument: the "forbidden" patterns (numbers coprime to some a_i) form a finite union of arithmetic progressions mod L, and by Dirichlet, infinitely many valid numbers exist in each AP mod L. The greedy picks the smallest valid number, which cycles through the APs.

**Opening E (Shift-invariance via explicit construction):**
Show directly that a_n + L satisfies the recurrence starting from a_{n-T+1} + L, a_{n-T+2} + L, ..., a_n + L. For this, verify: (i) each a_k + L shares a prime with each a_j + L for j < k (same indices), AND (ii) a_k + L shares a prime with each a_j (for j much earlier). Part (i) is straightforward if L = lcm of primes of all {a_k}. Part (ii) is the crux: requires every a_j to have a prime in P* (Lemma 1) and L to be divisible by all primes in P*. If (i) and (ii) are proved, then by uniqueness of the greedy, a_{n+T} = a_n + L.

---

### Hard steps (what every approach must face)

1. **Proving P* is finite** — needed for L to be well-defined and finite.
2. **Proving the stable antichain is reached** — equivalently, that every future term eventually is "dominated" by M* in the sense that removing primes ∉ P* still satisfies all constraints.
3. **Handling the case where NO term is a prime power** — the examples a_1=15, a_1=35, a_1=77 show this is a real case, and it's harder than the prime power case.
4. **Proving the periodicity holds from n=1 (not just n ≥ N)** — this seems automatic from the structure once L is established, but needs careful verification.

---

### The key subtlety about "for ALL n"

The problem claims periodicity for ALL n ≥ 1. Computationally verified: for a_1=77, T=18, L=154 works from n=1 (a_{1+18} = a_1 + 154 = 77 + 154 = 231 ✓). This seems automatic because:
- a_1 itself is in the stable antichain M* as an element with P_1 ∈ M* (or P_1 dominated by M*).
- The greedy respects the stable pattern from the very first step.

A valid proof approach: show a_{n+T} = a_n + L by induction on n, using that gcd(a_n + L, a_i) > 1 for ALL i ≤ n+T-1. The key tool: p | a_n and p | L implies p | (a_n + L), and every sharing uses primes p ∈ P*.

---

### Dead ends

None yet (first round, no prior approaches).

---

### Knowledge-base entries to use

- **Divisor analysis / gcd structure:** The problem is fundamentally about gcd conditions; Euclidean-style gcd arguments.
- **Order of an element, Fermat/Euler (eventually periodic):** The eventual periodicity of sequences mod m is a general number-theory principle.
- **Dirichlet's theorem (primes in AP):** May be needed to show valid numbers are dense in each residue class.
- **Bertrand's postulate:** To bound prime gaps and prevent certain "isolating" configurations.
- **Invariants and monovariants:** For proving antichain stabilization.
- **Pigeonhole:** For showing some prime divides infinitely many terms.

---

### Analogous past problems (cruxes)

- **aimo-0916** (Stabilize a descending chain by taking a power that restricts to identity): Technique = stabilizing a self-map's iterates. Crux = show the image stabilizes. Analogous because M_n is the image of a self-map (add new minimal elements), and we need the iterate to stabilize. Moderately analogous.
- **aimo-0514** (Reversible process forces purely periodic orbit, not eventually periodic): Crux = deterministic reversibility implies purely cyclic state graph. Potentially analogous if the sequence-defining rule is "reversible" in some sense, forcing periodicity from the start. Worth exploring.
- **aimo-0964** (Choose size one larger than self-terminating to force periodic orbit via reflecting boundary): Shows how a size choice can force cyclicity. Less directly analogous.

**Best analogy: none exactly matches.** The problem is uniquely about a greedy gcd-based sequence construction, which doesn't have a close crux match in the corpus.

---

### Small-case / intuition notes (labeled conjecture)

**Conjecture 1:** P* = {primes p : p divides a_n for all n ≥ N for some N} ∪ {other primes appearing infinitely often}. In practice, P* seems to be exactly the set of primes of the "stable" antichain M*.

**Conjecture 2:** L = product of distinct primes in P* (not lcm of prime powers). Verified for all examples: L = 2 (P*={2}), L=30=2·3·5 (P*={2,3,5}), L=154=2·7·11 (P*={2,7,11}), L=210=2·3·5·7 (P*={2,3,5,7}).

**Conjecture 3:** T = number of valid residue classes mod L under M*. Verified numerically in all cases.

**Conjecture 4:** The stable antichain M* is always the antichain of prime sets of a_1,...,a_T (just the first period). After T terms, no new minimal sets appear.

**Conjecture 5:** When a_1 = p·q (product of two primes with p < q), and neither p nor q is 2:
- If there exists a prime r with p < r < q appearing in a_2 (which goes to the smallest multiple of p or q that is > a_1), then the structure is more complex.
- When p=3, q=5 (a_1=15): a_2=18=2·3, so r=2 < p=3. The "triangle" antichain {{2,3},{2,5},{3,5}} forms quickly.
- When p=7, q=11 (a_1=77): a_2=84=2^2·3·7, so 2 enters; antichain is {{7,11},{2,7},{2,11}}.

**Observation (not conjecture):** The antichain can grow while the effective valid set stays constant (a_1=210 case). The correct object for the proof is the *effective valid set* (periodic mod L), not the antichain.
