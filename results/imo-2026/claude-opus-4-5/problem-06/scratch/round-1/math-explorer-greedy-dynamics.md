## imo-2026-06

### Greedy-Dynamics Lens

---

**Distinct openings:**

**Opening 1 — Irredundant Constraint Hypergraph (H) + Periodicity.**
Define H as the "irredundant constraint antichain": the antichain of minimal prime-sets P(a_i) such that the constraint "share a prime with a_i" is not implied by any earlier constraint. Once H stabilizes (i.e., every future term's prime-set contains some element of H as a subset), the valid set V = {m : P(m) intersects every Q ∈ H} is periodic mod L = lcm(∪H), and the greedy sequence moves through V in increasing order giving a_{n+T} = a_n + L. The key lemma is that H always stabilizes in finitely many steps. Proof idea: H is an intersecting antichain (any two terms of the sequence share a prime, so any two elements of H share a prime); once H becomes self-blocking (b(H) = H, where b is the blocker/dual), no future term can add a new irredundant constraint. Self-blocking is reached because each change to H adds a minimal transversal of H that uses only primes from ∪H, forcing H to eventually close under this operation.

**Opening 2 — Residue Stabilization Without Hypergraph Language.**
For each pair of primes (p, q) in some finite set S, show that eventually every term is divisible by p OR q (by the gcd-sharing constraint), and that the set of residues mod L = lcm(S) that satisfy all such binary conditions is finite and exactly T elements. The greedy sequence cycles through these T residue classes repeatedly, advancing L each cycle. This avoids hypergraph language: the proof reduces to (a) identifying S, (b) showing the "divisible by at least one of each pair" condition is periodic mod L, (c) showing the greedy search respects this periodicity.

**Opening 3 — Direct Monovariant on the Constraint System.**
Show that the constraint system C_n = {m : gcd(m, a_i) > 1 for all i ≤ n} satisfies C_{n+1} ⊆ C_n (constraints only get tighter), but that C_n stabilizes: C_n = C_{N} for all n ≥ N (some N). Key: when a new term a_{n+1} is added, C_{n+1} = C_n ∩ D(a_{n+1}) where D(k) = "numbers sharing a prime with k". If D(a_{n+1}) ⊇ D(Q) for some constraint Q already in C_n (i.e., a_{n+1}'s prime-set contains Q as a superset, making its constraint weaker), then C_{n+1} = C_n. Stabilization follows when all future terms satisfy this dominance condition — which is equivalent to H stabilizing.

**Opening 4 — "All two-of-three" Structure.**
In all computed examples, H ends up being the set of ALL 2-element subsets of some set S = {p_1,...,p_k} of primes. This is the "triangle/clique hypergraph" K_k^2. The valid set V then = {m : m divisible by at least 2 elements of S}, which has exactly T = (sum of phi-type counts) residue classes mod lcm(S). Proving the sequence always produces this K_k^2 structure for some k and S would immediately give the result. Evidence: a_1=2 → K_1^1 on {2} (T=1,L=2); a_1=15 → K_3^2 on {2,3,5} (T=8,L=30); a_1=77 → K_3^2 on {2,7,11} (T=18,L=154); a_1=35 → K_4^2 on {2,3,5,7} (T=34,L=210).

**Opening 5 — Induction on the Sequence's "Prime Signature".**
Show that after exactly one "fundamental period" (a block of T consecutive terms covering each of the T residue classes once), the next T terms are identical to the previous T terms shifted by L. Prove this by showing the constraint system at step T is "isomorphic" to the constraint system at step 0 (modulo L): the prime factorizations of terms in period 2 are related to those of period 1 by replacing "large primes" (which contribute dominated constraints) by other large primes that don't affect the constraint structure.

---

**Candidate technique(s):**
- Chinese Remainder Theorem / modular arithmetic: the valid set mod L is described by a finite system of congruence conditions (divisibility by primes in each Q ∈ H), and CRT shows this is periodic mod L.
- Hypergraph blocking / self-complementary clutters: H stabilizes at a self-blocking antichain.
- Invariant / monovariant: H is a decreasing (in some measure) function of the sequence that eventually stabilizes.

---

**Cheap-kill candidates:**
- Any two terms of the sequence share a prime (verified: for all computed examples, gcd(a_i, a_j) > 1 for all i ≠ j). This "pairwise non-coprime" property means H is an INTERSECTING FAMILY — and intersecting antichains have bounded size for fixed support.
- The valid set for a_1=p (prime) is trivially all multiples of p, giving T=1, L=p immediately. This handles the "degenerate" case.
- Parity observation: if 2 | a_1 or 2 ever appears in a term, all subsequent terms are even (eventually), collapsing L to 2. So the "hardest" case is when a_1 is a product of odd primes.

---

**Knowledge-base entries to use:**
- "Modular arithmetic, CRT": the periodicity of the valid set mod L.
- "Divisor analysis: gcd structure, bounding a finite search by size": the irredundant constraint analysis.
- "Invariants & monovariants": H is a monovariant.
- "Pigeonhole / extremal principle": the sequence mod L is eventually periodic (finitely many residue classes).
- "Order of an element, Fermat/Euler: eventual periodicity of ... a sequence mod m": the sequence a_n mod L is eventually periodic.
- "Dirichlet's theorem (primes in AP)": possibly used to show certain prime-combinations can be realized by sequence terms (to force H to the self-blocking state).

---

**Analogous past problems (cruxes):**
- **aimo-0030** (divisibility-gcd game): The problem involves "good numbers" whose prime-sharing structure creates a non-adjacency class — any two good numbers must share a prime. Crux: "to produce a number with the same allowed-prime signature but no forbidden (large) prime factors, take the product of allowed primes." This is directly analogous to our observation that large prime factors in sequence terms are "replaceable" — the constraint from a term with a large prime is dominated by the constraint from its small-prime factors. The crux of aimo-0030 (showing you can always find a "small" representative with the same prime signature) mirrors our argument that H stabilizes over S_0 = small primes.
- **aimo-0231** (iterated map periodicity): Crux: "decompose the first-hitting-time of an iterated map modulo N as the lcm over prime-power factors of N of the first-hitting-times modulo each prime power." The eventual-periodicity-via-lcm structure is analogous. The same CRT-based lcm decomposition applies here.
- None of the crux moves is directly about "greedy sequences with pairwise gcd > 1" becoming periodic — this combination appears to be novel.

---

**Prior progress:** None — this is round 1.

**Dead ends (do not retry):** None identified yet.

---

**Small-case / intuition notes (all conjectural from computation):**

1. **a_1 = 2**: Sequence = 2, 4, 6, 8, 10, ... All even. T=1, L=2. H = {{2}}.
2. **a_1 = 3**: Sequence = 3, 6, 9, 12, ... All multiples of 3. T=1, L=3. H = {{3}}.
3. **a_1 = 7**: Sequence = 7, 14, 21, 28, ... All multiples of 7. T=1, L=7. H = {{7}}.
4. **a_1 = 15 = 3·5**: Sequence eventually periodic with T=8, L=30. Valid residues mod 30 = {0,6,10,12,15,18,20,24} = numbers divisible by ≥2 of {2,3,5}. H stabilizes as {{2,3},{2,5},{3,5}}. VERIFIED: a_{n+8} = a_n + 30 for ALL n ≥ 1 (period starts immediately!).
5. **a_1 = 77 = 7·11**: T=18, L=154=2·7·11. Valid residues mod 154 = numbers divisible by ≥2 of {2,7,11}. H stabilizes as {{2,7},{2,11},{7,11}} (= K_3^2 on {2,7,11}). VERIFIED: a_{n+18} = a_n + 154 for ALL n ≥ 1.
6. **a_1 = 35 = 5·7**: T=34, L=210=2·3·5·7. Valid residues mod 210 = numbers divisible by ≥2 of {2,3,5,7}. H stabilizes as K_4^2 = all pairs from {2,3,5,7}.
7. **a_1 = 30 = 2·3·5**: T=1, L=2. The sequence is all even numbers. (Since a_2=212 is even and all subsequent terms must share a prime with 212=2^2·53, forced to be even.)

**Key structural observation (conjecture):** In all cases, H stabilizes as "all 2-element subsets of some finite set S of primes." The valid set is then "divisible by ≥2 elements of S," which is periodic mod lcm(S). The exception is a_1 = prime power (H = 1-element subset {{p}}, valid set = all multiples of p).

**Why H is an intersecting family (PROVED from the problem statement):** Any two terms a_i, a_j (i < j) satisfy gcd(a_j, a_i) > 1 by definition (a_j must share a prime with EVERY previous term). So any two prime-set constraints P(a_i) and P(a_j) must intersect: P(a_i) ∩ P(a_j) ≠ ∅. Hence H (a subantchain of {P(a_i)}) is an intersecting antichain.

**Key bottleneck:** Proving H stabilizes after finitely many steps is THE main challenge. The argument is: (a) any new irredundant constraint added to H must be a subset of ∪H_old (because it must hit each Q ∈ H_old using only primes from ∪H_old — but this is false when H is not self-blocking, since new primes CAN enter). A cleaner argument: the sequence of antichains H_0 ⊂ H_1 ⊂ ... (in the sense of the antichain order) is bounded, because H is always an intersecting antichain, and intersecting antichains over a finite prime set are finite. But the prime set ∪H can itself grow. The correct bound comes from: each new prime entering ∪H appeared in a term a_k that created a genuinely new irredundant constraint, and this can happen at most finitely many times because eventually the self-blocking condition H = b(H) is reached and makes all future constraints redundant.

**Fastest answer guess:** T and L depend on a_1. L = lcm(S) where S is the set of "essential" primes (those in ∪H after stabilization). T = |{r ∈ [0,L) : r divisible by ≥ 2 elements of S}| (when H is K_k^2). The problem only asks to prove T and L EXIST, not to compute them explicitly.
