# Outline Review: IMO 2026 P6 (Round 2)

## Summary of Approaches Proposed

The outliner proposes:
1. **greedy-on-vstable** (REVISE of two-of-k-structure): Eliminate K_k^2 claim, use pairwise gcd argument for backward extension
2. **antichain-monovariant** (REVISE of antichain-stabilization): Use f(H) = sum 2^{-|Q|} monovariant to prove stabilization
3. **saturation-route** (NEW): Prove H becomes "saturated" (every valid m dominated by some Q in H)
4. Dead-ends: backbone-periodicity (wrong constraint model), clique-valid-set (fatal gap in coprime-pair)

---

## Approach 1: greedy-on-vstable

**Verdict: APPROVE**

### Soundness Analysis

**Step 1 (Define H_stable, V_stable):** Correct by definition.

**Step 2 (All pairs share a prime):** SOUND. The later term a_k (k > j) was chosen with gcd(a_k, a_j) > 1, so P(a_k) intersect P(a_j) != empty. This is symmetric by construction.

**Step 3 (Every a_n in V_stable):** SOUND. Each Q in H_stable equals P(a_j) for some j. By Step 2, P(a_n) intersect P(a_j) != empty, so a_n transverses H_stable.

**Step 4 (V_stable subset V_{H_n}):** SOUND with correct mechanism. The claim requires: for each Q' in H_n, there exists Q in H_stable with Q subset Q'. This follows because H_n = antichain of {P(a_1),...,P(a_n)} while H_stable = antichain of all {P(a_i) : i >= 1}. Each element of H_n either is minimal globally (so is in H_stable) or contains a smaller element that is (which is in H_stable). Verified computationally for a1=35.

**Step 5 (Squeeze argument):** SOUND. a_{n+1} = min V_{H_n}(>a_n) and V_stable subset V_{H_n} gives a_{n+1} >= min V_stable(>a_n). Since a_{n+1} in V_stable (Step 3), equality holds. The sequence is greedy on V_stable from n=1.

**Step 6 (Dichotomy: H_stable finite or all-multiples-of-p):** This is the MAIN GAP. The outline states "by pigeonhole on backbone primes: infinite H_stable forces common prime p | all terms." The mechanism from explorer Opening C is: if H_stable is infinite, by pigeonhole some backbone prime p appears in infinitely many Q_i in H_stable. These must be {p, r_1}, {p, r_2}, ... for distinct r_i (pairwise incomparability). Any m in V_stable must hit each {p, r_i}; if p nmid m then all r_i | m, impossible. So p | m for all m in V_stable, reducing to Case 2a.

The logic is valid but needs to be written out explicitly. This is a MANAGEABLE gap - the mechanism is stated.

**Steps 7-8 (CRT periodicity, greedy cycles):** Standard. Once H_stable is finite with support S, L = prod(S) gives V_stable as union of residue classes mod L. Greedy on L-periodic set cycles with period T = |residues|.

### Case Coverage

- Case 1 (a_1 prime power): T=1, L=p. Already proved.
- Case 2a (prime power enters later): All terms multiples of p, T=1, L=p. Already proved.
- Case 2b (no prime power ever): H_stable finite by dichotomy, use main argument.

All cases covered.

### Issues

1. **Step 6 gap** needs explicit proof in the build. The mechanism is stated but not yet rigorous.

### Computational Verification

Verified for a1=35:
- H_stable = {{5,7}, {2,5}, {3,5}, {2,3,7}} (has 3-element set, not K_k^2 - correct)
- L=210, T=34
- a_{n+T} = a_n + L verified for n=1..59
- V_stable subset V_{H_n} verified for n=1..4
- All pairs share a prime: verified

The outline is sound. Proceed to build.

---

## Approach 2: antichain-monovariant

**Verdict: CHANGES REQUESTED**

### Soundness Analysis

**Steps 1-2 (Define H_n, intersecting antichain):** Correct.

**Step 3 (f non-decreasing):** SOUND. When element Q replaced by P subsetneq Q, delta f = 2^{-|P|} - 2^{-|Q|} > 0. When new incomparable P added, delta f = 2^{-|P|} > 0.

Verified computationally: f(H_n) non-decreasing for a1=35, starting at 0.25 and stabilizing at 0.875.

**Step 4 (f < 1 for intersecting antichains):** GAP. The outline claims "Bollobas-type bound" but does not prove it. This is the KEY LEMMA.

The claim f(H) <= 1 with equality iff H = {{p}} for intersecting antichains is NOT obvious. Empirically f(H_stable) <= 0.875 for all tested cases. But this needs proof.

Actually, for an intersecting antichain H, consider any two elements Q, Q' with |Q| <= |Q'|. They share a prime, so if Q = {p}, then p in Q' for all Q', meaning all elements share p. This limits the structure. The bound f < 1 needs a formal argument - likely via the fact that an intersecting antichain on primes {p_1,...,p_k} has limited size.

**Step 5 (Discrete jump >= 2^{-k}):** Depends on max element size k being bounded. If no bound on k, jumps can be arbitrarily small and infinitely many steps possible.

**Step 6 (k bounded once 2-element set enters):** The logic that once a 2-element set enters, k is bounded by the largest existing element size. This is handwavy - need to show 2-element sets actually enter and that they bound future growth.

**Steps 7-8:** Import from greedy-on-vstable. Sound once H stabilization proved.

### Issues

1. **f <= 1 bound for intersecting antichains:** Needs proof. The statement is true but not obvious.
2. **2-element sets enter quickly:** Need to show greedy produces terms with exactly 2 prime factors.
3. **k bounded:** Even if a 2-element set enters, need to show max|Q| doesn't grow unboundedly afterward.

These gaps are FIXABLE but represent substantial work beyond greedy-on-vstable.

### Recommendation

The monovariant approach is a valid alternative mechanism but has MORE gaps than greedy-on-vstable. Build greedy-on-vstable as primary; this can be a backup if the dichotomy argument fails.

---

## Approach 3: saturation-route

**Verdict: CHANGES REQUESTED**

### Soundness Analysis

**Step 1-2 (Saturated => frozen):** SOUND. If H is saturated (every transversal P contains some Q in H), then any new term's prime set is dominated, so H doesn't change.

**Step 3 (2-element sets permanent):** SOUND for Sub-case 2b. A 2-element set {p,q} can only be replaced by a 1-element set {p} or {q}, which would be a prime power = Case 2a.

**Step 4 (Greedy generates all essential pairs):** GAP. The claim "Dirichlet: products of 2 primes appear with positive density" is true but doesn't guarantee the greedy sequence visits them. The greedy picks the SMALLEST valid element, which might always be a product of 3+ primes.

**Step 5 (Saturation via pairs):** Depends on Step 4.

**Step 6:** Import from greedy-on-vstable.

### Issues

1. **"Essential primes" must be shown finite:** The claim is that backbone primes suffice. But non-backbone primes do enter (e.g., 2 for a1=15). Need to show the essential set is exactly support(H_stable).
2. **Step 4 is the hard part:** Showing greedy must eventually pick a 2-prime-factor term is non-trivial. The greedy might avoid them if larger products are always smaller.

### Computational Check

For a1=35, the sequence is 35, 40, 42, 45, 50, 60, 70...
- 35 = 5*7 (2 primes)
- 40 = 2^3*5 (2 primes by prime set)
- 42 = 2*3*7 (3 primes)
- 45 = 3^2*5 (2 primes)

So 2-prime-factor terms do appear, but proving this always happens requires an argument about density vs. greedy selection.

### Recommendation

Saturation-route has potential but Step 4 is a hard gap. Not clearly better than greedy-on-vstable.

---

## Dead-End Verdicts

**backbone-periodicity:** Confirmed DEAD-END. Uses T(a_i) = P(a_i) intersect B but constraints involve all primes. For a1=15, gives L=15 vs correct L=30.

**clique-valid-set:** Confirmed DEAD-END. Round 1 reviewer cut it for fatal gap.

---

## Diversity Assessment

All three approaches share:
- The pairwise gcd argument (Step 2 of greedy-on-vstable)
- The V_stable enumeration argument (Steps 7-8 of greedy-on-vstable)
- The CRT periodicity conclusion

They differ in HOW they prove H stabilizes:
- greedy-on-vstable: dichotomy (infinite => all-multiples-of-p)
- antichain-monovariant: monovariant f(H) bounded + discrete jumps
- saturation-route: 2-element permanence + saturation via pairs

This is GOOD DIVERSITY within a common framework. If one mechanism fails, the others provide fallback routes. The approaches are not trivially variations of each other - they genuinely attack the stabilization gap differently.

However, if the CORE framework (V_stable = greedy enumeration) were wrong, all three would fail. The framework itself is computationally verified and structurally sound.

---

## Rankings

### Registrations

- greedy-on-vstable: REVISE of two-of-k-structure. Already registered as two-of-k-structure; this is a revision, not a new slug.
- antichain-monovariant: REVISE of antichain-stabilization. Already registered.
- saturation-route: NEW. Should be registered.

### Comparisons

Based on:
- greedy-on-vstable has one manageable gap (dichotomy argument) with clear mechanism stated
- antichain-monovariant has multiple gaps (f<=1 bound, k bounded, 2-element entry)
- saturation-route has one hard gap (Step 4: greedy visits 2-prime terms)
- two-of-k-structure (round 1) had false K_k^2 claim but main structure sound
- backbone-periodicity is dead-end
- clique-valid-set is dead-end
- antichain-stabilization was never built, unknown outcome

Pairwise:
1. greedy-on-vstable > antichain-monovariant (fewer gaps)
2. greedy-on-vstable > saturation-route (clearer mechanism for main gap)
3. antichain-monovariant ~ saturation-route (different gaps, similar difficulty)
4. two-of-k-structure > backbone-periodicity (partial vs dead-end)
5. two-of-k-structure > clique-valid-set (partial vs dead-end)
6. antichain-stabilization < greedy-on-vstable (greedy-on-vstable is the evolved form)

---

## Final Verdicts

| Slug | Verdict | Note |
|------|---------|------|
| greedy-on-vstable | APPROVE | Main gap (dichotomy) has stated mechanism; build it |
| antichain-monovariant | CHANGES REQUESTED | f<=1 bound and k bounded need proofs; secondary priority |
| saturation-route | CHANGES REQUESTED | Step 4 (greedy visits 2-prime terms) needs proof; viable backup |
| backbone-periodicity | DEAD-END | Wrong constraint model |
| clique-valid-set | DEAD-END | Fatal gap |

---

build set: two-of-k-structure, saturation-route

Note: "greedy-on-vstable" is a REVISION of two-of-k-structure. The builder should update results/imo-2026-06/approaches/two-of-k-structure.md with the new approach (remove K_k^2 claim, add dichotomy argument for finiteness, use pairwise gcd for backward extension). The saturation-route builder should create results/imo-2026-06/approaches/saturation-route.md.
