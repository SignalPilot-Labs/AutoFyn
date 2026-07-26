# IMO 2026 Problem 6 — EXPERIMENTAL / COMPUTATIONAL route

## Problem recap
Greedy sequence: a_{n+1} = smallest integer > a_n with gcd(a_{n+1}, a_i)>1 for EVERY i ≤ n. Prove ∃ T,L>0 with a_{n+T}=a_n+L for all n. (Proof-only, no numeric answer.)

## Headline experimental finding (the mechanism, confirmed computationally)

For every start I tested, the sequence obeys **a_{n+1} = (smallest m > a_n with m mod L ∈ V)**, where:
- **L** = product of a finite set S of "essential" primes (always including 2 once 2 has appeared),
- **V ⊆ {0,1,…,L−1}** = a fixed set of "valid residues",
- the residue transition r_n := a_n mod L is a **deterministic function** r ↦ r', and forms a **single cycle** of length T.

Once V is fixed, periodicity is immediate and exact: a_{n+T}=a_n+L from the start (transient length 0 in all cases tested, even a_1=105 where free-rider primes up to 317 appear). Verified directly (see appendix code `verify.py`):

| a_1 | L (factored) | T | transient | primes appearing in 1st 500 terms (free-riders) |
|---|---|---|---|---|
| 2  | 2 | 1 | 0 | — |
| 3  | 3 | 1 | 0 | (2) |
| 5  | 5 | 1 | 0 | (2) |
| 7  | 7 | 1 | 0 | (2) |
| 15 = 3·5 | **30 = 2·3·5** | 8 | 0 | 7, 11 |
| 35 = 5·7 | **210 = 2·3·5·7** | 34 | 0 | 7,31,71,… |
| 77 = 7·11 | **154 = 2·7·11** | 18 | 0 | 3,5,13,17,19,23 |
| 105 = 3·5·7 | **210 = 2·3·5·7** | 58 | 0 | 11,13,17,19,23,29,31,37,… |
| 55 = 5·11 | 5 | 1 | 0 | (locks to mult. of 5) |
| 1001 = 7·11·13 | (no period in 1500 terms) | ? | ? | — (period huge / T large) |

Key points:
- **L = product of essential primes** (a SUBSET of primes ≤ a_1; not all of them). Essential ≠ merely "divides a_1": a_1=105 gives L=2·3·5·7 (note 2 not in a_1; 11 appears but is NOT essential). a_1=77 gives L=2·7·11 (3 is introduced as a free-rider but NOT essential).
- **T = |V|** = number of residues mod L whose "reduced type" (set of essential-prime divisors) is a hitting set of the stabilized family F. E.g. a_1=15: valid residues mod 30 are exactly those divisible by ≥2 of {2,3,5}: {0,6,10,12,15,18,20,24} → T=8. ✓ Matches.
- **Free-rider primes NEVER beat the reduced-type mechanism.** For a_1=105, primes 11,13,…,317 divide various terms, yet a_{n+1} is still the next residue mod 210 in V — a smaller m with an essential-type miss is never rescued by a free-rider prime. (This is the load-bearing conjectural step — see "Crux gap".)

## The cheap structural lemma (the key reduction)

**Lemma (easily provable).** Every a_n is divisible by some prime dividing a_1.
*Proof:* a_n (n≥2) must satisfy gcd(a_n, a_1) > 1, so it shares a prime factor with a_1. ∎

**Corollary (finiteness of the type universe).** Every a_n has a prime factor p ≤ a_1. Restrict to the finite set Q = {primes ≤ a_1}. Define the **reduced type** r_n = (prime divisors of a_n) ∩ Q. Then r_n ≠ ∅ for all n, and r_n ranges over the finite power set P(Q). In particular, only finitely many distinct reduced types ever appear.

**Corollary (stabilization).** The family F = {r_n : n ≥ 1} ⊆ P(Q) is finite. The set of "valid types" H_n = {r ∈ P(Q) : r hits r_1,…,r_n} shrinks monotonically in n (nested) and is bounded below, so H_n stabilizes: H_n = H for all n ≥ N.

**Pairwise-intersecting.** Any two types in F intersect: when r_j appeared (j later), a_j had to hit all earlier terms including the one with type r_i, so r_i ∩ r_j ≠ ∅. Hence F is a pairwise-intersecting family, and F ⊆ H.

This already gives the **finite-state scaffold**: once n ≥ N, a_{n+1} must have reduced type in H (a fixed finite set), so its residue mod L_0 = ∏_{p∈Q} p lies in a fixed set V_0. The only remaining question is whether the greedy actually picks the *next* element of V_0 above a_n, i.e. whether free-rider primes > a_1 ever let a *smaller* m sneak in. Computation says NO (every case tested). Proving this is the crux gap.

## Crux gap (for the outliner)

**Claim to prove:** For n ≥ N (post-stabilization), a_{n+1} = min{m > a_n : (m mod L_0) ∈ V_0}, where V_0 = {residues whose reduced type ∈ H}. Equivalently: if m satisfies a_n < m < m* (m* = next V_0-residue above a_n), then m fails to hit some earlier a_i — i.e. m's reduced type misses some r_i AND no free-rider prime of m rescues it.

Why it is plausible (data): in the test cases the valid-residue cycle starts at n=0 (transient 0), even when many free-rider primes (≤317) are floating around. So the phenomenon is robust.

Possible proof ideas to hand off (NOT a proof — pointers for the outliner):
1. **Density / pigeonhole argument.** Between a_n and a_n + L_0 there is at least one V_0-residue (V_0 contains all of F, and 0 or some essential product is in V_0). A free-rider rescue of m < m* would require m to be divisible by a prime p > a_1 that divides some specific earlier a_i with r_i ∩ type(m) = ∅. Such p are large; m < a_n + L_0. Need a bound: the multiplicity of "rescue primes" in [a_n, a_n+L_0] is too sparse to fill every gap. Delicate.
2. **Monovariant on the essential family.** Show F is closed: every type that can ever appear after stabilization is already in F. (True by definition of stabilization, but the point is: free-rider primes don't create new reduced types.) Then any m whose reduced type is not in H would, if picked, introduce a contradiction with the greedy minimality (a smaller valid residue exists).
3. **Lifting the crude bound Q = {primes ≤ a_1} to the true essential set S.** Once H stabilizes, let S = ∪_{r∈H} (∪r) (primes appearing in some valid type). Take L = ∏_{p∈S} p (the true L). Show the residue dynamics mod L is the deterministic cycle. (Computationally L ≪ L_0; e.g. a_1=105 has L_0 huge but L=210.)

## Distinct openings this route suggests

- **(A) Finite-state-on-residues.** Prove the crude bound (every a_n divisible by a prime of a_1 → reduced types in finite P(Q)), then prove free-riders don't interfere → residue cycle mod L_0 is eventually periodic with T, L. Direct, but the free-rider step is the wall.
- **(B) Monovariant via the type-family.** Track the family F_n of reduced types seen so far as a monotonically growing finite invariant; once it stabilizes, show the next term is forced. Bypasses free-rider issue by proving F's stabilization *forces* the greedy (no smaller m exists). Crux: a "minimality forces type ∈ H" lemma.
- **(C) Restrict to the true essential set S = primes that appear in some *minimal* hitting set of F.** S is finite (⊆ Q). Reduce mod L=∏S. Show the reduced types, restricted to S, are pairwise-intersecting AND form the valid set directly. May give a cleaner free-rider argument: any prime outside S that appears is always accompanied by an S-prime, so it can't be the deciding factor for a *smaller* m. (This matches the data: in a_1=105, every free-rider prime divides a term that is also divisible by ≥2 of {2,3,5,7}.)
- **(D) A "witness" construction.** For each essential prime p, exhibit a specific term a_i whose reduced type is {p}∪(stuff outside S) — i.e. p is the unique S-prime of a_i (a "witness" for p). Then any candidate avoiding p must hit a_i via a prime outside S, which is large; bound the candidate range. This is how a_1=15 locks ≥2 of {2,3,5}: witnesses 15={3,5}, 24={2,3}, 20={2,5} (each pair). Generalize.

## Candidate technique(s)
- **Invariants & monovariants** (the type-family F_n is a monotone-bounded invariant) — the central engine.
- **Finite-state / pigeonhole on residues mod L** — gives periodicity once stabilization + free-rider-irrelevance are established.
- **Hitting-set / set-system duality** — the constraint "non-coprime to all previous" is literally "prime-set is a hitting set of the family of previous prime-sets." The minimal hitting sets form the antichain H.
- **Bertrand / size-bounding** — to bound essential primes ≤ a_1 (the cheap lemma does it via a_1 itself).

## Cheap-kill candidates
- The lemma "every a_n divisible by a prime of a_1" is the one-move structural kill that bounds the universe of essential primes. Use it FIRST.
- The "pairwise-intersecting family F" observation is a second cheap structural fact: any two appearing reduced types intersect. This makes H ⊇ F and gives the valid-residue set nonempty immediately.
- T = |V| can be computed by inclusion-exclusion on the essential primes once S is known — gives a handle on T without running the sequence.

## Knowledge-base entries to use
- **Invariants & monovariants** (Combinatorics section + General Proof Methods) — the type-family F_n is the bounded monotone invariant.
- **Pigeonhole / extremal principle** — finite type universe forces stabilization; finite residue states force periodicity.
- **Divisor analysis** (Number Theory) — consecutive-integer coprimality, gcd structure of the prime-divisor sets.
- **Orders of an element, Fermat/Euler; eventual periodicity of products mod m** (Number Theory) — analogous "finite residues mod m → periodic" engine.
- **Zsigmondy / Bertrand** — potentially to bound which primes can appear as free-riders or to construct witness primes (e.g. pick a prime in a residue class).

## Analogous past problems (cruxes)
- **aimo-0678** [number_theory/size-bounding-and-descent AND /modular-arithmetic-and-CRT] — BEST analogue. A coupled gcd/lcm recurrence a_{n+1}=gcd(a_n,b_n)+1, b_{n+1}=lcm(a_n,b_n)−1. Crux moves: (i) "Construct a min-of-a-set integer monovariant — the least integer ≥ a_n that fails to divide the frozen invariant — and prove it non-decreasing"; (ii) "Once one coordinate of a coupled integer recurrence is bounded, reduce the other coordinate modulo the lcm of the bounded coordinate's attainable values, turning the recurrence into a finite-state map → eventual periodicity." Move (ii) is almost exactly our "reduce a_n mod L_0 once the type family is bounded" engine. Adapt: the "frozen invariant" there is our stabilized family F; "lcm of attainable values" is our L_0.
- **aimo-0477** [number_theory/divisibility-and-gcd] — "Track gcd(fixed term, current term) and show it divides the next one, producing a divisor-chain bounded by the fixed term that must stabilize." d_n = gcd(a_1, a_n) is a non-decreasing divisor of a_1 → stabilizes. Directly adaptable: gcd(a_1, a_n) is monotone and bounded (divides a_1), so v_p(gcd(a_1,a_n)) stabilizes per prime p | a_1. This gives a clean stabilization lemma "for free" on the a_1-side, complementary to the reduced-type stabilization.
- **aimo-0982** [number_theory/modular-arithmetic-and-CRT] — "To prove a subsequence is eventually periodic, track the sampling index modulo the period of the source's eventually-periodic digits; show the residue sequence is eventually periodic." Spirit-parallel: once a_n mod L_0 is governed by a deterministic finite-state map, periodicity follows.
- **aimo-0728** [number_theory/modular-arithmetic-and-CRT] — branching recurrence reduced mod a small prime → finite residues → periodic. Same finite-state engine, weaker analogue.

## Prior progress
None (round 1; `results/imo-2026-06/approaches/` empty, no `.ranking.json`, no lemmas).

## Dead ends (do not retry)
- (none yet — first round.)
- WARNING on a methodological dead end I fell into: a too-short period verification (≤2 periods of evidence) FALSELY reported a_1=35 as T=1, L=5. The true values (with ≥3 periods of evidence) are T=34, L=210. The outliner/builder must require ≥3 full periods of evidence before declaring a period, and ideally cross-check that a_{n+1} equals the next valid residue.

## Small-case / intuition notes (all CONJECTURES from computation, not proofs)
- **Conjecture (strong):** For all a_1, the residue sequence a_n mod L (L = product of essential primes) is purely periodic from n=0 (transient length 0), with period T = |V| and translation L. Verified for a_1 ∈ {15,35,77,105} and trivially for prime-power and even-composite starts.
- **Conjecture:** The essential prime set S is the smallest set such that (i) every term is divisible by some prime in S, (ii) the family of S-reduced types is pairwise-intersecting and "saturated" (closed under the greedy). S always contains 2 (once 2 appears, which happens at a_2 unless a_1 is even and a_1 itself supplies the lock).
- **Conjecture (the lock dichotomy):** EITHER a pure prime power p^k appears at some point → then the sequence locks to multiples of p, giving T=1, L=p (the "Regime A" case, e.g. a_1 even, or a_1=55→mult of 5); OR no pure prime power ever appears → "Regime B", T>1, L=product of ≥2 essential primes. The dichotomy is decided by whether the stabilized valid-type family H contains a singleton {p} (then p^k could appear) — but in Regime B every valid type has ≥2 primes, so no pure power is ever valid, so the lock is permanent.
- **Conjecture:** L is always squarefree (product of distinct essential primes). Matches all data.
- **Intuition for WHY periodic:** The greedy, restricted to residues mod L, is a deterministic map on a finite set; because the valid residues are "upward-closed under the cyclic order" (the next valid residue above any a_n is a function only of a_n mod L), the residue sequence is a single cycle. Translation by L per cycle follows because each cycle step advances the residue and, once the cycle closes, the integer value has advanced by exactly L.

## Watch-fors (pitfalls for the outliner/builder)
- Don't conflate "essential primes" with "primes dividing a_1" — 2 is almost always essential but rarely divides a_1; and free-rider primes (11 for a_1=105) are NOT essential. Define S via the hitting-set family, not via a_1's factorization.
- The free-rider-irrelevance step is the real wall; don't hand-wave it. The data is convincing but a proof must exhibit, for each m in the gap (a_n, m*), a specific earlier a_i that m misses even via free-rider primes.
- The crude bound "every a_n has a prime ≤ a_1" gives finiteness but L_0 = ∏_{p≤a_1} p is astronomically larger than the true L. The proof of periodicity can USE the crude L_0 (finiteness suffices for the finite-state argument) — do not try to pin down the true S unless needed. This is a place where a cruder bound is strictly easier and still sufficient.
- a_1=1001 (=7·11·13) had no period in 1500 terms — likely T or the transient is large; do NOT treat this as a counterexample, it just needs more terms. But it warns that "transient = 0" is not universal for larger a_1.

---

## Appendix: code used

### `greedy.py` / `greedy3.py` — generate sequence, find period (strict, ≥3 periods of evidence)
```python
def factors(x):
    s=set(); d=2
    while d*d<=x:
        while x%d==0: s.add(d); x//=d
        d+=1
    if x>1: s.add(x)
    return s

def gen_sequence(a1, N=2000, cap=10**9):
    a=[a1]; facts=[factors(a1)]
    while len(a)<N:
        m=a[-1]+1; found=None
        while m<cap:
            fm=factors(m); ok=True
            for f in facts:
                if not (fm & f): ok=False; break
            if ok: found=m; break
            m+=1
        if found is None: break
        a.append(found); facts.append(factors(found))
    return a, facts

def find_period_strict(seq, min_evidence_periods=3, maxT=120):
    n=len(seq)
    for T in range(1, maxT):
        for s in range(0, n - min_evidence_periods*T - 1):
            Lc=seq[s+T]-seq[s]
            if all(seq[k+T]-seq[k]==Lc for k in range(s, n-T)) and (n-s)>=(min_evidence_periods+1)*T:
                return T, Lc, s
    return None
```

### `verify.py` — confirm a_{n+1} == next valid residue mod L
```python
# After computing L = product of essential primes (found via find_period_strict),
# build V = set of residues a_n mod L, then check:
residues = set(x % L for x in a)
ok = True
for i in range(len(a)-1):
    m = a[i]+1
    while (m % L) not in residues: m += 1
    if m != a[i+1]: ok = False; break
# ok==True for a_1 in {15,35,77,105}: greedy == next-valid-residue, FREE-RIDERS NEVER BEAT IT.
# Also: residue transition r -> r' is a deterministic FUNCTION and forms a single cycle of length T.
```
