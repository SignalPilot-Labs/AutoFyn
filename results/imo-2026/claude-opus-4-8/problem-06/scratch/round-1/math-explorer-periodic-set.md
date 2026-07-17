## imo-2026-06 — PERIODIC-SET / SIEVE / MODULAR framing

### Problem recap
Infinite sequence a_1 < a_2 < ... of integers > 1, each a_{n+1} the SMALLEST integer > a_n sharing a prime factor with EVERY previous term. Prove there exist T, L > 0 with a_{n+T} = a_n + L for ALL positive integers n (not just eventually).

---

## Distinct openings surfaced

### Opening A: ADMISSIBLE-SET STABILIZATION + GCD-CLIQUE
Define the admissible set A_n = {m > 1 : gcd(m, a_i) > 1 for all i ≤ n}. This is a decreasing chain of subsets of Z. The greedy rule picks a_{n+1} = min(A_n ∩ (a_n, ∞)). The key sub-claim: A_n eventually stabilizes to a fixed union of residue classes A mod M (for some finite M = product of "core" primes). 

**The GCD-clique criterion (proved empirically):** A_n stabilizes iff A_n is a GCD-clique — i.e., every pair of elements in A_n shares a prime factor. Once A_n is a GCD-clique, any new term a_{n+1} ∈ A_n satisfies gcd(a_{n+1}, m) > 1 for all m ∈ A_n (by the clique property), so the constraint from a_{n+1} is vacuous, and A_{n+1} = A_n.

**Empirically confirmed:** For a1=15 (first 3 effective terms), a1=35 (first 4), a1=77 (first 4), a1=91 (first 3), a1=221 (first several effective terms but a large number of total terms). The admissible set mod M is always a GCD-clique once stable.

**Why A_n eventually becomes a GCD-clique:** If m1, m2 ∈ A_n with gcd(m1,m2)=1, the greedy sequence eventually surpasses max(m1,m2). Once a_k = m1 enters the sequence, the constraint from m1 forces gcd(m, m1) > 1 for ALL future terms. But gcd(m2, m1) = 1, so m2 becomes inadmissible. This reduces the number of coprime pairs in A_n, driving it toward a clique. The hard step: making this quantitative (showing it terminates in finitely many steps).

### Opening B: RESIDUE-CLASS ENUMERATION — "T classes in first T steps"
Once M and A = {admissible residues mod M} are identified, the greedy sequence in the stable phase enumerates elements of A in increasing order. In each M-window there are exactly T = |A| admissible residues. The greedy picks them in sequence, giving a_{n+T} = a_n + M for all n in the stable phase.

**Key structural fact (empirically verified for all tested cases):** The first T terms of the sequence are exactly one representative from each of the T admissible residue classes mod M (all distinct residues mod M). This implies the period T, L = M works from n = 1, not just eventually. No "transient" — the entire sequence, from term 1, satisfies a_{n+T} = a_n + L.

**Evidence:** 
- a1=15: T=8, L=30, first 8 residues mod 30: {0,6,10,12,15,18,20,24} = exactly 8 distinct. ✓
- a1=35: T=34, L=210, first 34 residues mod 210: all 34 distinct. ✓
- a1=77: T=18, L=154, first 18 residues mod 154: all 18 distinct. ✓
- a1=91: T=20, L=182, first 20 residues mod 182: all 20 distinct. ✓

### Opening C: "VACUOUS-CONSTRAINT" CRITERION FOR NEW PRIMES
New primes appear infinitely often in the sequence (7, 11, 13, 17, ... for a1=15; many for a1=221) but are always "harmless." A term a_{n+1} = p * m (p new prime, m composed of old primes) imposes the constraint "div by p or share a prime with m." Once A is a GCD-clique, every element of A shares a prime with m (since m ∈ A), so the constraint reduces to "share prime with m," which is already satisfied by all elements of A. Therefore p's constraint is vacuous. This is the mechanism by which infinitely many primes appear but only finitely many are "core."

**Core prime set:** L = product of "core" primes = primes that appear in the effective (non-vacuous) constraints. Empirically: L = 30 = 2*3*5 for a1=15, L = 210 = 2*3*5*7 for a1=35 and a1=105, L = 154 = 2*7*11 for a1=77, L = 182 = 2*7*13 for a1=91, L = 6630 = 2*3*5*13*17 for a1=221.

### Opening D: "FOR ALL n" VIA FIRST-PERIOD COVERAGE
The theorem demands a_{n+T} = a_n + L for ALL positive integers n (not "for all sufficiently large n"). This is non-trivial: why does the period work from n=1?

**Mechanism (conjecture based on all examples):** The admissible set A_n stabilizes WITHIN the first T steps (N_0 ≤ T where N_0 = stabilization point, T = period). The first T terms of the greedy sequence cover all T residue classes mod M exactly once (one per residue class). After T steps, all residue classes are covered, so:
1. Future constraints from terms with same residue class as earlier terms are equivalent (same prime support mod M), hence vacuous.
2. The greedy in the (T+1)th step picks the same residue class as the 1st step, but M units later: a_{T+1} = a_1 + M.
3. By induction, a_{n+T} = a_n + M for all n ≥ 1.

**Stabilization within T steps:** For all tested a1, the admissible set stabilizes after K ≤ T steps. This is far from obvious and is the main open gap in the proof.

### Opening E: DIRECT GREEDY-ON-PERIODIC-SET ARGUMENT
Once we accept that A is a GCD-clique (self-stabilizing union of residue classes mod M), the subsequent argument is clean:
1. A is periodic with period M: {m : m ∈ A} = {m : m mod M ∈ R} for a fixed residue set R with |R| = T.
2. The greedy sequence on A (enumerating A in increasing order) satisfies a_{n+T} = a_n + M for all n with a_n in the stable regime.
3. The first T terms already lie in A (they satisfy all the constraints of the eventual stable A — this needs proof, but holds empirically).
4. Hence a_{n+T} = a_n + M for ALL n ≥ 1.

---

## Candidate technique(s)
- **Admissible set / sieve framing**: A_n is a union of residue classes mod M_n (product of primes of a_1,...,a_n). The GCD-clique stabilization criterion.
- **Greedy on periodic set**: once A is periodic, the greedy enumeration has period T, shift L=M.
- **Finite-state / decreasing chain argument**: A_n is a decreasing sequence of subsets, must stabilize.
- **Modular arithmetic / CRT**: the admissible set is a union of residue classes; CRT computes the density.

---

## Cheap-kill candidates
- **Parity / mod 2**: If a_1 is even, all terms are even (since gcd(a_{n+1}, a_1) > 1 forces a_{n+1} even). Then T=1, L=2 trivially.
- **Single prime power**: If a_1 = p^k, all terms must be div by p. Sequence = multiples of p. T=1, L=p. Very clean first case.
- **When rad(a_1) is a prime**: T=1, L=p immediately.
- **Two primes p,q with 2 ∈ {p,q}**: if a_1 = 2^k * q^j, effectively all terms are even (since gcd(a_2, a_1) > 1 and a_2 is small, a_2 is likely even). Then all terms even and further GCD structure applies.

The key structural case that requires real work: a_1 = p*q for two ODD primes p, q (the "hardest" case). For example a1=15=3*5 gives L=30=2*3*5, a1=35=5*7 gives L=210=2*3*5*7.

---

## Knowledge-base entries to use
- **Modular arithmetic, CRT** (KB section "Number Theory"): The admissible set A is a union of residue classes mod M; use CRT to compute which residues are admissible.
- **Divisor analysis** (KB "Number Theory"): gcd structure, prime factorizations, coprimality conditions.
- **Invariants & monovariants** (KB "General Proof Methods"): A_n is a monovariant (decreasing), must stabilize.
- **Pigeonhole / extremal principle** (KB "General Proof Methods"): Once T residue classes are covered, the period repeats. The first T terms must hit all T classes.
- **Direct proof** (KB "General Proof Methods"): Chain from definitions.
- **Order of an element, Fermat/Euler** (KB "Number Theory"): eventual periodicity of sequences mod M.

---

## Analogous past problems (cruxes)
1. **aimo-0678** [NT, sequences-and-recurrences] — "Once one coordinate of a coupled integer recurrence is bounded, reduce mod lcm of attainable values to get a finite-state deterministic map." Crux: reduce to a finite modular state space, then periodicity follows. Analogous because: once A_n stabilizes, the greedy sequence is determined by a position within a finite set of residue classes, making it a finite-state deterministic process → periodic.

2. **aimo-0577** [NT, modular-arithmetic-and-CRT] — "Invert a piecewise update map on a finite invariant set to show it is a permutation, then read the desired targets off as the backward iterates." Crux: finite state + bijection → periodicity. Analogous because: the greedy on A (once stable) is a bijection on residue classes (each class advances exactly one slot per step), so the sequence is purely periodic with no transient.

3. **aimo-0514** [combinatorics, processes-and-algorithms + invariants] — "A deterministic process is reversible so its state graph is a union of cycles, forcing the orbit to be PURELY periodic (no transient)." Crux: pure periodicity (not just eventual) by reversibility. Most directly analogous to the "for all n" requirement: if the state map is injective (no two inputs give same output), the orbit is purely periodic. Our problem requires a_{n+T} = a_n + L for ALL n, which is the same as "purely periodic with shift."

---

## Prior progress
None (fresh workspace, first round).

---

## Dead ends (do not retry)
None yet (first round).

---

## Small-case / intuition notes (all labeled conjectural unless stated as proved)

**Empirical pattern:**
- a1=2: T=1, L=2. Sequence = all even integers.
- a1=9: T=1, L=3. Sequence = all multiples of 3 ≥ 9.
- a1=15=3*5: T=8, L=30=2*3*5. Core primes {2,3,5}. Admissible residues mod 30: {6,10,12,15,18,20,24,30} (div by 6, div by 10, or odd mult of 15).
- a1=35=5*7: T=34, L=210=2*3*5*7. Core primes {2,3,5,7}.
- a1=77=7*11: T=18, L=154=2*7*11. Core primes {2,7,11}.
- a1=91=7*13: T=20, L=182=2*7*13. Core primes {2,7,13}.
- a1=221=13*17: T=334, L=6630=2*3*5*13*17. Core primes include {2,3,5} even though they don't divide a_1.

**Key conjecture (empirically verified):** L = product of all core primes; T = number of admissible residue classes mod L (= T elements of Z/LZ satisfying all constraints from the stabilized admissible set).

**Key fact (proved by the GCD-clique argument):** Once A_n is a GCD-clique, all subsequent constraints are vacuous and A_n stabilizes. The clique property means: for any two m1, m2 ∈ A_n, gcd(m1, m2) > 1.

**Key conjectured fact (unproved, hardest step):** A_n becomes a GCD-clique after at most T steps. Equivalently: the first T terms of the sequence cover all T residue classes mod L. (Verified for all tested cases.)

**Mechanism for "infinitely many primes, finitely many core primes":** New primes appear as "riders" on core-prime-containing terms (e.g., 2*3*7 introduces 7 but the constraint "div by 2, 3, or 7" is vacuous since A ⊆ {div by 2 or 3} already). Only primes whose constraint genuinely reduces A are "core."

**The hardest step for the proof:** Showing A_n stabilizes in finite time. Approaches:
(a) Show each "effective" constraint reduces the density of A_n by at least 1/M_n, and since density is bounded below (sequence is infinite), finitely many steps are effective.
(b) Show the number of coprime pairs in A_n strictly decreases with each effective constraint.
(c) Use a finite prime set lemma: the "effective" prime set is bounded by rad(a_1) * (small correction).

**Subtlety for "for ALL n" (not just eventually):** The period holds from n=1 because: the stabilization happens within the first T steps, and the first T terms already cover all T residue classes. The "transient" (before stabilization) is absorbed into the first period. This requires showing: (1) stabilization ≤ T, and (2) the greedy choices during the transient land in the eventual stable A.

---

## Proof of the "for all n" claim — a key reduction

If one can show:
1. A_N stabilizes to A (a GCD-clique, union of T residue classes mod M) after N = N_0 steps.
2. a_1, ..., a_{N_0} all lie in A (i.e., all their residues mod M are in the T admissible residue classes).
3. The first T terms {a_1, ..., a_T} cover all T residue classes (each exactly once).

Then a_{n+T} = a_n + M for all n ≥ 1 follows by induction: a_{T+1} is the smallest element of A > a_T, which is the first element of A in the next M-block after a_T. Since a_1 is the smallest element of A in [a_1, a_1+M), and the period is M, a_{T+1} = a_1 + M. Continuing, a_{n+T} = a_n + M.

This reduction is clean. The key open step is proving (1) + (3), which requires showing "the first T greedy choices exhaust all T residue classes."
