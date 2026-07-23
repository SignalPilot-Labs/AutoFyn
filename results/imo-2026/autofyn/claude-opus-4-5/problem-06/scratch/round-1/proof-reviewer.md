# Proof Review: IMO 2026 P6

## Approach 1: two-of-k-structure

### Summary
The proof divides into cases based on whether a prime power enters the sequence. If a prime power p^e enters, all terms are multiples of p, giving T=1, L=p. If no prime power enters, the proof claims the constraint antichain H stabilizes to K_k^2 (all 2-element subsets of some prime set S), and the valid set becomes L-periodic where L = product(S).

### Issues Found

1. **Incorrect claim about K_k^2 structure (Line 226):** The proof claims "The antichain H_n for n >= N equals K_|S|^2, the set of all 2-element subsets of S." This is FALSE. Computational verification shows:
   - For a1 = 35, H stabilizes to {{5,7}, {2,5}, {2,3,7}, {3,5}} which is NOT K_k^2 (the element {2,3,7} has size 3).
   - For a1 = 105, H stabilizes to {{3,5,7}, {2,3}, {2,7}, {2,5}}, also not K_k^2.
   
   The proof says "Let me prove this directly" (line 217-218) but never actually provides the proof.

2. **Incomplete proof of K_k^2 claim:** Lines 219-265 meander through various lemmas and observations without ever completing the claimed proof of the K_k^2 structure.

3. **However, the main result is still correct:** The K_k^2 claim is not actually needed for the periodicity result. The proof's key steps are:
   - H stabilizes to some finite intersecting antichain (TRUE)
   - L = product of union(H) is finite (TRUE)
   - The valid set is L-periodic (TRUE)
   - The greedy cycles through valid residues with period T = |valid residues mod L| (TRUE)
   - a_{n+T} = a_n + L holds for all n >= 1 (TRUE)

4. **Backward extension argument (lines 290-296):** The proof asserts "all a_n for n >= 1 are in V (by definition of valid)" without carefully verifying this for n < N (during the startup phase). This is a gap, though the claim is in fact true.

### Computational Verification
Tested a_{n+T} = a_n + L from n=1 for: a1 = 6, 10, 14, 15, 21, 30, 35, 42, 70, 77, 91, 105, 143, 210, 1001. All verified correct.

### Verdict: CHANGES REQUESTED (Status: partial)

The proof contains a significant false claim (K_k^2 structure) and an incomplete sub-proof. However, the main argument structure is sound - the false claim happens not to be necessary. The proof needs to:
1. Remove or correct the K_k^2 claim
2. Explicitly prove that H stabilizes without relying on K_k^2
3. Rigorously prove the backward extension (a_{n+T} = a_n + L for n < N)

---

## Approach 2: backbone-periodicity

### Summary
The proof defines backbone types T(a_n) = P(a_n) intersect B where B = primes(a_1). It claims the valid set is determined by backbone-type constraints, and uses this to establish periodicity with L = product(B).

### Issues Found

1. **CRITICAL FLAW: Wrong characterization of valid set (Lines 106-107):** The proof claims "the valid set V_n is determined by the constraints 'T(m) intersects every Q in H.'" This is FALSE. 

   The constraint gcd(m, a_i) > 1 means m shares SOME prime with a_i - this could be a prime IN the backbone or OUTSIDE the backbone. The proof only considers backbone primes.

2. **Wrong period L (Lines 113-120):** The proof claims L = lcm(B) = product of backbone primes. But:
   - For a1 = 15, B = {3, 5}, so the proof gives L = 15
   - The ACTUAL period is L = 30 (as 2 enters the constraint structure via a2 = 18, a3 = 20)
   
   Computational verification: The correct valid residues mod 30 are {6, 10, 12, 15, 18, 20, 24, 30}, not residues mod 15.

3. **The remark at line 47-48 acknowledges but doesn't fix the issue:** "The converse is not quite true: m and a_i might share a prime outside B." The proof proceeds as if this doesn't matter, but it fundamentally breaks the argument.

4. **False claim about self-blocking over backbone (Lines 53-93):** The self-blocking analysis only considers subsets of B, but the actual constraints involve primes outside B too.

### Computational Counter-Example
For a1 = 15 = 3*5:
- Proof claims: L = 15, valid set determined by T(m) intersecting T(a_i)
- Reality: L = 30, valid set = {m : divisible by at least 2 of {2, 3, 5}}

The constraint antichain is H = {{3,5}, {2,3}, {2,5}}, which includes the prime 2 NOT in B.

### Verdict: RETHINK (Status: unsolved)

The backbone-periodicity proof has a fundamental flaw: it restricts attention to backbone primes but the actual constraints involve primes outside the backbone. The proof would need to be completely restructured to use P(a_i) (all primes) instead of T(a_i) (backbone types).

---

## Summary

| Approach | Builder Status | True Status | Verdict | Gap |
|----------|---------------|-------------|---------|-----|
| two-of-k-structure | solved | partial | CHANGES REQUESTED | K_k^2 claim is false (not needed), backward extension needs rigor |
| backbone-periodicity | solved | unsolved | RETHINK | Wrong constraint characterization (backbone vs full primes) |

---

## Promotable Lemmas

### From two-of-k-structure:

1. **Backbone Constraint Lemma:** 
   - Statement: Every term a_n shares a prime with a_1.
   - Status: CERTIFIED. The proof is correct: gcd(a_n, a_1) > 1 implies P(a_n) intersect P(a_1) != empty.

2. **Intersecting Antichain Lemma:**
   - Statement: The prime sets P(a_i) form an intersecting family (any two share a prime).
   - Status: CERTIFIED. Follows from the gcd > 1 condition.

### From backbone-periodicity:
No promotable lemmas - the proof is fundamentally flawed.
