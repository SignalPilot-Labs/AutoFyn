## imo-2026-06

### Route: WQO-repair / Small-Common-Prime Lemma — attacking the shared crux directly

---

## Strategy A: Small Common Prime Lemma (SCL) — critical correction

**The claim as stated in `small-prime-core` is FALSE.** The natural threshold Q = P(a_1) does not work.

Computational counterexamples:
- a_1 = 15, P(a_1) = {3,5}: terms 18 = 2·3² and 20 = 2²·5 share gcd = 2, but 2 ∉ {3,5}.
- a_1 = 35, P(a_1) = {5,7}: terms 42 = 2·3·7 and 45 = 3²·5 share gcd = 3, but 3 ∉ {5,7}.
- Violations occur for a_1 ∈ {15, 35, 77, 91, 105, 143, 221}.

**Correct threshold (CONJECTURE, strongly supported):** Let p_max = max prime factor of a_1.  
Then for any two terms a_j, a_k, gcd(a_j, a_k) has a prime factor ≤ p_max.

Verified computationally with 150+ terms for a_1 ∈ {15, 35, 77, 91, 105, 143, 221, 10403} — zero violations in every case.

Examples of what this means:
- a_1 = 15 = 3·5, p_max = 5: every pair shares gcd with prime ≤ 5. ✓ (2 ≤ 5)
- a_1 = 77 = 7·11, p_max = 11: every pair shares gcd with prime ≤ 11. ✓
- a_1 = 10403 = 101·103, p_max = 103: every pair shares prime ≤ 103. ✓ (pairs involving 2·101 and 3·103 etc. share 2 ≤ 103)

---

## Strategy A: Proof path for SCL with Q = {primes ≤ p_max}

**Key structural facts** (all proved or immediate from definitions):

1. Every term a_k has P(a_k) ∩ P(a_1) ≠ ∅ (clique with a_1). So every term contains a prime ≤ p_max.

2. Any multiple of rad(a_1) ≥ a_1 is in A (it shares each prime of a_j via the prime a_j shares with a_1). These multiples have prime sets ⊆ P(a_1) ⊆ {primes ≤ p_max}.

3. For any term a_k with prime factor r > p_max: since r > all primes of a_1, the next multiple of r exceeds a_k by r > B = rad(a_1). So a_{k+1} ≤ a_k + B < a_k + r, meaning a_{k+1} is NOT divisible by r. Therefore a_{k+1} shares some prime < r (in fact ≤ p_max) with a_k.

**The proof attempt** (by strong induction on k, to show SCL for all pairs (j,k)):

Suppose SCL holds for all pairs with second index < k. Consider the term a_k and any a_j with j < k.

Since a_k ∈ V_∞: a_k shares some prime with a_j. Let p be a shared prime. 

Case 1: p ≤ p_max. Done. ✓

Case 2: p > p_max. Both a_j and a_k contain p, and p > all primes of a_1. But:
- a_j has some prime q_j ∈ P(a_j) ∩ P(a_1) ≤ p_max (clique with a_1).
- a_k has some prime q_k ∈ P(a_k) ∩ P(a_1) ≤ p_max (clique with a_1).

If q_j = q_k (same small prime): then q_j | a_j and q_j | a_k, so they share q_j ≤ p_max. ✓

If q_j ≠ q_k: We need to find a shared prime ≤ p_max between a_j and a_k. This requires using the clique constraint more carefully — specifically that a_j and a_k both intersect ALL earlier terms via small primes. The greedy minimality of a_k provides the remaining constraint. [This is the sub-gap in the proof; see opening below.]

**OPENING A** — Induction route using greedy minimality:
When a_k was chosen, the number a_k - q_j (if divisible by q_j) was either already a term or invalid. If it's a term a_l = a_k - q_j ∈ A, then a_l < a_k and shares q_j with a_j. By SCL (induction for pair (j,l) if l > j): P(a_j) ∩ P(a_l) has a prime ≤ p_max... this chain is complex but may close.

**OPENING B** — Direct domination route:
The core mechanism is that for any term a_k with prime r > p_max in P(a_k): the "small part" a_k^{small} = a_k / (product of prime powers > p_max) satisfies gcd(a_k^{small}, a_j) > 1 for EVERY other term a_j. If true, this means a_k^{small} ∈ V_∞, so P(a_k^{small}) ⊊ P(a_k) is a realized prime set strictly contained in P(a_k), dominating it. Hence P(a_k) ∉ E_∞ (not minimal). Proving this claim IS the SCL proof.

---

## Strategy B: WQO Descent — evaluation

**The descent argument as described has a recoverable gap.** Here is the precise analysis:

**What works:** 
- Every F ∈ E_∞ satisfies F ∩ P(a_1) ≠ ∅ (clique with a_1).  
- So if E_∞ is infinite, pigeonhole over P(a_1) = {q_1,...,q_r} gives infinitely many F all containing some fixed q_i.  
- The sub-family E_i = {F ∈ E_∞ : q_i ∈ F} is infinite and all contain q_i.

**The gap in the descent as described:**
After removing q_i, the sets F \ {q_i} form a family in P_fin(primes \ {q_i}). The dispatch says these must form a "bad sequence" in P_fin(primes \ {q_i}), then recurse. But:
- F \ {q_i} might not be pairwise intersecting after removing q_i (two sets sharing ONLY q_i become disjoint, breaking the clique structure).
- P_fin(primes \ {q_i}) under ⊆ is still NOT WQO (infinitely many incomparable finite sets).

So the descent as described does NOT terminate cleanly. The recursion breaks because the bad-sequence property in P_fin(primes \ P(a_1)) is not contradicted.

**The correct fix:** Use SCL instead.

**WQO argument with SCL (COMPLETE once SCL is proved):**  
If SCL holds (all primes in ∪E_∞ are ≤ p_max), then:
- E_∞ ⊆ 2^Q where Q = {primes ≤ p_max}.
- Q is a finite set (bounded by π(p_max), the number of primes up to p_max).
- P_fin(Q) under ⊆ IS WQO by Dickson's Lemma (identify each subset with its {0,1}-indicator vector in {0,1}^{|Q|}; the coordinate-wise ≤ is Dickson which is WQO on N^k for finite k; ⊆ is exactly this).
- E_∞ is an antichain in P_fin(Q). Any antichain in a WQO is finite. So E_∞ is finite. ∎

So the WQO argument works perfectly — but requires SCL as input. The descent (peeling P(a_1) primes) was an attempt to avoid SCL and fails. The right path is: prove SCL directly, then invoke WQO/Dickson on the finite prime universe.

---

## Computational data on E_∞

E_∞ stabilizes quickly (within the first 10–20 terms) and has the following structure:

| a_1 | P(a_1) | E_∞ | Primes in E_∞ | p_max |
|---|---|---|---|---|
| 15 | {3,5} | {{2,3},{2,5},{3,5}} | {2,3,5} | 5 |
| 35 | {5,7} | {{2,3,7},{2,5},{3,5},{5,7}} | {2,3,5,7} | 7 |
| 77 | {7,11} | {{2,7},{2,11},{7,11}} | {2,7,11} | 11 |
| 91 | {7,13} | {{2,7},{2,13},{7,13}} | {2,7,13} | 13 |
| 105 | {3,5,7} | {{2,3},{2,5},{2,7},{3,5,7}} | {2,3,5,7} | 7 |
| 10403 | {101,103} | {{2,3,103},{2,101},{3,101},{101,103}} | {2,3,101,103} | 103 |

**Key pattern (conjecture):** Every prime in ∪_{F∈E_∞} F is ≤ p_max = max prime of a_1. No prime > p_max ever appears in E_∞, even though terms contain primes > p_max as "bonus factors" that get dominated.

**Why large primes get dominated (mechanism):** A term a_k = q · r (q ≤ p_max, r > p_max) would need to share a prime with EVERY term. But there exist terms (multiples of rad(a_1) or early terms with mixed small primes) that contain some prime of P(a_1) ≠ q and DON'T contain r. For such a term a_j: gcd(a_j, q·r) = gcd(a_j, q) (since r ∤ a_j). If also q ∤ a_j, then gcd = 1 and a_k ∉ V_∞. Specifically for a_1 = 101·103: the term 10506 = 2·3·17·103 shares NO prime with 101·107 = 10807 (since gcd(10807, 10506) = gcd(101·107, 2·3·17·103) = 1), so 10807 ∉ V_∞.

---

## Distinct openings surfaced

1. **SCL via greedy minimality + induction on k (OPENING A):** Strong induction on the term index k. When a_k is chosen as the greedy minimum, analyze the number a_k - q_j (where q_j ∈ P(a_j) ∩ P(a_1)) and whether it was a term or invalid, building a chain that forces a shared small prime.

2. **SCL via domination of large-prime terms (OPENING B):** Show directly that for any term a_k with prime r > p_max, the "de-r-ified" version a_k / r^{v_r(a_k)} is itself in V_∞ (hence is a term that dominates a_k). The proof requires: the small-prime part of a_k shares a prime with every other term. This is equivalent to SCL.

3. **WQO + SCL:** GIVEN SCL, the WQO argument closes immediately via Dickson's Lemma on the finite set Q = {primes ≤ p_max}. This requires zero additional creativity once SCL is established.

4. **Direct finite-stabilization via bounded-time argument:** The antichain E_n stabilizes within the first ~20 terms (computationally). Try to prove: after at most B = rad(a_1) terms, E_n = E_∞. Mechanism: within the first B terms, the greedy sequence hits all "necessary constraint types" modulo rad(a_1). After that, new terms are periodic mod L and add no new minimal constraints.

5. **Early-segment determines everything:** E_∞ is determined by the first N_0 terms (N_0 ≤ B), and all primes of these terms are ≤ a_{N_0} ≤ a_1 + B · N_0 ≤ a_1(1 + rad(a_1)). This gives a specific but large upper bound. This bound is not tight (the real bound is p_max, not a_1 · rad(a_1)), but any finite bound suffices for the WQO argument.

---

## Candidate technique(s)

- **SCL proof**: greedy minimality + induction + clique structure. The pivot is the relation between a term and the terms before/after it in the window of size B.
- **Dickson's Lemma** (WQO for P_fin(S), finite S): closes the argument given SCL.
- **Density/sieve** (Mertens-type): secondary backup for bounding E_∞ size, but unnecessary once SCL+WQO works.

## Cheap-kill candidates

- **Large-prime blocking**: For any prime r > p_max and candidate m = q·r (q ≤ p_max): the number r·⌊a_1/r⌋ or nearest multiple is likely blocked by a term with P ∩ {q,r} = ∅ from early in the sequence. Check if a_1 having ≥ 2 distinct prime factors always creates such a blocking term.
- **Singleton check**: P(a_k) = {p} (pure prime power) requires p | all a_j, so p ∈ P(a_1). Singletons in E_∞ are subsets of P(a_1). Quick verification.

## Knowledge-base entries to use

- **Pigeonhole / extremal principle**: for the WQO argument (pigeonhole over the finite prime set Q).
- **Dickson's Lemma / WQO**: not listed by name in knowledge_base.md but is the correct tool: P_fin(S) under ⊆ for finite S is WQO. Available from general "invariants & monovariants" or combinatorics techniques.
- **Divisor analysis** (from knowledge_base.md): "gcd structure, consecutive-integer coprimality" — relevant for the gap structure.
- **Induction** (general proof methods): the base case/inductive step for SCL.
- **Direct proof + contradiction** (general): assume SCL fails, derive that some term is not in V_∞.

## Analogous past problems (cruxes)

None directly analogous found. The problem structure (greedy sequence on gcd constraints leading to periodicity via a "stable prime universe") is specific to IMO 2026 P6 and does not match standard crux-corpus patterns.

## Prior progress

- Steps 1 (Clique), 2 (Bounded gaps), 3 (Reduction: A = V_∞ ∩ [a_1,∞)), 5 (Periodicity given finiteness), 6 (Greedy on periodic set) all complete in greedy-clique-closure.
- Small-prime-core: Steps 1-2 (shared), 4-5 (complete given SCL). 
- **Single remaining gap**: Prove E_∞ is finite, equivalently prove SCL (primes in E_∞ ≤ p_max).

## Dead ends (do not retry)

- **SCL with Q = P(a_1)**: FALSE. Counterexample: a_1=15, (18,20) share prime 2 ∉ {3,5}.
- **WQO descent (peeling P(a_1) primes)**: The descent from E_∞ into P_fin(primes \ P(a_1)) does not terminate cleanly because P_fin(primes \ P(a_1)) is NOT WQO and the pairwise intersection property breaks after removing a common prime.
- **Small-prime-core with Q = P(a*)** (minimum radical term's prime set): also FAILS. Pairs like (20,45) for a_1=15 share prime 5 ∉ P(a*)={2,3}.
- **Claiming prime set of sequence stabilizes**: FALSE. New primes keep appearing as bonus factors in later terms (e.g., 107, 109, 113, ... for a_1=10403). Only the MINIMAL antichain E_∞ stabilizes.

## Small-case / intuition notes

- (CONJECTURE) Every prime p ∈ ∪_{F∈E_∞} F satisfies p ≤ p_max. Verified for a_1 up to 10403 with 150-500 terms. No counterexample found.
- (CONJECTURE) E_∞ stabilizes after at most ~20 terms (much less than B = rad(a_1) in all tested cases). The stabilization happens when the greedy sequence first "fills in" all constraint types needed.
- (CONJECTURE) The number |E_∞| is roughly φ(L)/L * constant, where L is the period. For a_1=15: T=8, L=30. For a_1=35: T=34, L=210.
- (FACT) period L = product of all primes in ∪_{F∈E_∞} F. Verified: a_1=15 gives L=2·3·5=30; a_1=35 gives L=2·3·5·7=210; a_1=77 gives L=2·7·11=154; a_1=91 gives L=2·7·13=182.
- (FACT) The monovariant B*_n = min_{i≤n} rad(a_i) stabilizes after 1-4 terms. B* is typically much smaller than rad(a_1). But B* alone doesn't determine E_∞ or L.
