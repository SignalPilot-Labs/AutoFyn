## imo-2026-06

**Problem**: Infinite sequence a_1, a_2, ... of integers > 1; a_{n+1} is the smallest integer > a_n with gcd(a_{n+1}, a_i) > 1 for all i = 1,...,n. Prove there exist positive integers T, L with a_{n+T} = a_n + L for all n ≥ 1.

---

### Distinct openings

**Opening A — Finite S-prime core + CRT residue cycle**

Define S = {primes p : p divides a_n for infinitely many n}. By a pigeonhole argument (every a_n must share a prime with every a_k, so every a_k has some prime dividing infinitely many a_n), S is non-empty. S is finite because: the covering hypergraph H = {P_k ∩ S : k ≥ 1} (where P_k = primes of a_k) lives in 2^S; once H stabilizes, no new S-primes can appear. Set L = ∏_{p ∈ S} p (squarefree product). Define the valid residue set V = {r ∈ Z/LZ : for each k, some p ∈ S with p | a_k also divides r}. Computationally: T = |V|, and the sequence of residues a_n mod L cycles through V in a fixed order, giving a_{n+T} = a_n + L for all n.

The opening move: show S is finite and every term has an S-prime. Then show the greedy sequence always picks elements of V (mod L), establishing a deterministic cycle on a finite set.

**Opening B — The key lemma and inductive quasi-periodicity**

Key Lemma (verified computationally on many examples): For every pair i < j, a_i and a_j share at least one prime in S. Consequence: gcd(a_n + L, a_k) > 1 for every k < n, because a_n and a_k share an S-prime p, and p | L means p | (a_n + L), and p | a_k. This validates a_n + L as a candidate at step n+T. Minimality (a_{n+T} cannot be strictly less than a_n + L) then follows from the residue structure.

If this lemma is established, the proof flows by induction: suppose a_{m+T} = a_m + L for m ≤ n; then a_{n+1} + L is valid at step n+T+1 (by the lemma) and minimal (by residue/gap structure), giving a_{n+T+1} = a_{n+1} + L.

**Opening C — Reversibility of state map → pure periodicity from n = 1**

Analogy: problem aimo-0514 proves pure (not just eventual) periodicity by showing the state map is a bijection on a finite state space, so every orbit is a cycle. Here the "state" is (a_n mod L, S-prime profile of a_n). Since L = ∏ S and the S-profile of a_n+L equals the S-profile of a_n (adding L doesn't change S-residues), the forward and backward maps on (residue, S-profile) are both deterministic. Reversibility would force pure periodicity from n = 1 rather than eventual periodicity.

**Opening D — Stabilization of the covering hypergraph**

As n grows, the covering hypergraph H_n = {P_k ∩ S : 1 ≤ k ≤ n} is non-decreasing (only adds sets). H_n lives in 2^S (finite), so it stabilizes at some step N to H_∞. After step N, the valid residue set V_n = V_∞ is fixed. The greedy sequence from step N onward is periodic with period T = |V_∞| and increment L. The key observation is T = |V_∞| equals the number of S-prime types cycling through the sequence — verified: for L = 30 (S = {2,3,5}), |V| = 8 = φ(30); for L = 154 (S = {2,7,11}), |V| = 18 (not φ(L), but the number of valid residue classes from the specific H_∞). Extending the periodicity back to n = 1 requires showing H_N = H_∞ even from the start (i.e., H does not stabilize "late").

**Opening E — Bertrand/pigeonhole to bound when large primes become irrelevant**

Large primes q ∉ S appear in only finitely many terms. After the last term divisible by q, the constraint from any a_k (k with q | a_k) is satisfied only via other primes of a_k, which are in S. Once all large primes have "appeared for the last time," the sequence becomes purely S-prime-controlled and hence periodic. The Bertrand's postulate entry in knowledge_base.md is relevant: large primes in (a_n, 2a_n) appear at most once (as a factor of a greedy choice) and then fade away.

---

### Candidate technique(s)

- **Finite-state / CRT periodicity**: Define the state as (a_n mod L, S-prime profile), show it lives in a finite set and the dynamics are deterministic. This is the master technique. Combine with the CRT entry in knowledge_base.md to show the valid residue set V is well-defined and has the right size T.
- **Pigeonhole for S ≠ ∅**: Every term must share a prime with every previous term → some prime appears infinitely often → S ≠ ∅.
- **Induction on quasi-period**: Assuming a_{m+T} = a_m + L for m ≤ n, prove for m = n+1 using validity (Key Lemma) and minimality (gap structure of V).

---

### Cheap-kill candidates

- **Every term has an S-prime (elementary)**: If a_n has only primes q_1,...,q_r all outside S, then each q_i appears only finitely often, so only finitely many a_m (m > n) share a prime with a_n. But gcd(a_m, a_n) > 1 for ALL m > n → infinitely many share a prime with a_n. Contradiction. So every a_n has a prime in S.
- **S is non-empty**: Since there are infinitely many a_n, and each must share a prime with a_1 (finitely many primes), some prime of a_1 divides infinitely many a_n. That prime is in S. So S ∩ P_1 ≠ ∅.
- **L is squarefree**: Since adding L to any a_n must preserve S-prime residues, and the S-prime residue of a_n + kL is the same as a_n for all k (because p | L for all p ∈ S), L must be divisible by all S-primes. The smallest such L is ∏_{p ∈ S} p (squarefree). This is confirmed by all computed examples.

---

### Knowledge-base entries to use

From `/home/agentuser/repo/knowledge_base.md`:

- **"Modular arithmetic, CRT"**: the valid residue set V ⊆ Z/LZ is a union of arithmetic progressions determined by which subsets of S-primes cover each constraint; CRT gives the exact count |V| = T.
- **"Order of an element, Fermat/Euler: periodicity of aⁿ mod m; sequences are eventually periodic mod m"**: core analogy — the sequence of residues a_n mod L is periodic by finite-state.
- **"Pigeonhole / extremal principle"**: to show S ≠ ∅ (some prime divides infinitely many terms, by pigeonhole over the finitely many primes of a_1).
- **"Bertrand's postulate"**: large primes (outside S) appear sparsely; their multiples satisfying the full covering constraint are far apart, so the greedy algorithm rarely picks them.
- **"Dirichlet's theorem (primes in AP)"**: may be used to construct terms with specific S-prime profiles in the period, showing V is achieved.
- **"Invariants & monovariants"**: the covering hypergraph H_n is non-decreasing (only grows), giving a monovariant argument for stabilization.

---

### Analogous past problems (cruxes)

**1. aimo-0678** [number_theory / modular-arithmetic-and-CRT] — **Most analogous overall**

Crux: "Once one coordinate of a coupled integer recurrence is bounded, reduce the other coordinate modulo the lcm of the bounded coordinate's attainable values, turning the state pair into a deterministic map on a finite set."

Adaptation: In our problem the "bounded coordinate" is the S-prime profile (finite set 2^S). Once identified, reduce the sequence modulo L = ∏_{p∈S} p. The state (a_n mod L, S-prime profile) is a deterministic map on the finite set (Z/LZ) × 2^S, forcing the state sequence to be eventually periodic. The additional step here (not in aimo-0678) is showing the periodicity holds from n=1 (not just eventually), which requires reversibility or a direct validation of the base period.

**2. aimo-0514** [combinatorics / processes-and-algorithms] — **Key for "pure periodicity from n = 1"**

Crux: "Show a deterministic process is reversible so its state graph is a union of cycles, forcing the orbit to be purely periodic rather than eventually periodic."

Adaptation: If the map on (residue mod L, S-prime profile) is shown to be reversible (given the output state, the input state is uniquely determined), then the orbit is purely periodic from n=1. For our sequence, reversibility would follow from: knowing a_{n+1} mod L and its S-profile, there is a unique a_n mod L and S-profile that could have preceded it under the greedy rule.

**3. aimo-0648** [algebra / sequences-and-recurrences] — **For eventual periodicity as a fallback**

Crux: "Show an order statistic (max/min) of the terms is preserved by the recurrence to confine the sequence to a bounded interval, forcing eventual periodicity of an integer sequence. A bounded integer sequence whose next term is a deterministic function of the last d terms takes finitely many state-vectors, hence is eventually periodic."

Adaptation: In our case the sequence is unbounded but the RESIDUES mod L are bounded. The residue sequence is determined by the current residue (since the greedy rule is translation-invariant mod L once the covering structure is fixed). Hence the residue sequence is eventually periodic, giving eventual quasi-periodicity. Extending to all n is the remaining step.

---

### Prior progress

None (round 1, workspace empty).

---

### Dead ends (do not retry)

None identified yet (round 1).

---

### Small-case / intuition notes

**Computed examples** (all verified a_{n+T} = a_n + L from n=1):
- a_1 = 4: T=1, L=2, S={2}. Sequence = all even numbers ≥ 4. (Conjecture: once a term is a prime power p^k, all subsequent terms divisible by p.)
- a_1 = 6: T=1, L=2, S={2}. Sequence = 6, 8, 10, 12, ... (all evens). Note: 3 only in a_1 itself.
- a_1 = 15 = 3·5: T=8, L=30 = 2·3·5, S={2,3,5}. Residues mod 30 cycle through {15,18,20,24,0,6,10,12} = exactly 8 valid residues = φ(30). Differences cycle: [3,2,4,6,6,4,2,3].
- a_1 = 35 = 5·7: T=34, L=210 = 2·3·5·7, S={2,3,5,7}. Large primes (11,13,17,19,23,...) appear roughly once per period but at SHIFTING positions; the SPECIFIC large prime changes each period while |V|=34 remains constant.
- a_1 = 77 = 7·11: T=18, L=154 = 2·7·11, S={2,7,11}. Valid residue count: type {7,11}: 1 residue; type {2,7}: 10 residues; type {2,11}: 6 residues; type {2,7,11}: 1 residue. Total |V|=18=T. ✓
- a_1 = 210 = 2·3·5·7: T=1, L=2, S={2}. Once a_1=210 forces the constraint to be "divisible by 2" (via a_2=212=4·53), the sequence is all even numbers.

**Key structural facts** (computational evidence, labeled as conjectures until proved):

1. (Conjecture) S is non-empty and finite for every starting a_1. S = {primes dividing infinitely many a_n}. Computationally S contains primes of a_1 OR the primes introduced in the first few steps that appear persistently.

2. (Provable via pigeonhole — not conjecture) Every term a_n has at least one prime in S. Proof: if a_n has only non-S primes (each appearing finitely often), then only finitely many a_m (m>n) share a prime with a_n, contradicting the greedy constraint.

3. (Conjecture, strongly verified) Every pair (a_i, a_j) with i < j shares a prime in S. Verified: 0 counterexamples in 2000 random pairs for a_1 = 15, 35, 77. This is the KEY LEMMA for the proof.

4. (Verified) The sequence of residues a_n mod L is purely periodic from n=1 with period T = |V| = number of valid residues mod L. The large primes appearing in terms (e.g., 11, 13, 17, ... for a_1=35) do not affect the residues or period.

5. (Verified) L = ∏_{p ∈ S} p (squarefree product). This is the natural period for S-prime residues (adding L does not change any S-prime residue).

6. (Verified) The S-prime profile of a_n (which S-primes divide a_n) is periodic with period T. Specifically, a_{n+T} = a_n + L has the SAME S-prime profile as a_n.

**The critical structural picture**: The greedy sequence a_n always picks the minimum element of the "valid residue class" V mod L that exceeds a_{n-1}. The sequence of valid residue classes r_1, r_2, ... (with r_i = a_i mod L) is purely periodic with period T = |V|. The actual values shift by L = ∏_{p∈S} p each period.

**Important subtlety**: The large primes (outside S) appear in DIFFERENT positions each period (their specific values change) but always in combination with at least one S-prime from S. The S-prime "skeleton" is what repeats; large primes are "decoration" on top.
