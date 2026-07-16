# Outline Review: IMO 2026 P1

## Problem Summary
2026 integers > 1 on a blackboard. Move: (m, n) -> (gcd(m,n), lcm(m,n)/gcd(m,n)). Prove (a) finitely many moves lead to exactly one M > 1 remaining; (b) M does not depend on choices.

---

## Approach 1: p-adic-gcd-invariant

**Verdict: APPROVE**

**Assessment:**
- **Right technique?** Yes. The lexicographic monovariant (P, k) where P = product and k = count of entries > 1 is a valid termination argument. The p-adic invariant G_p = gcd(v_p(a_i)) for uniqueness is the correct tool.
- **Sound skeleton?** Yes. The three-case analysis (A: m=n, B: m!=n with gcd=1, C: m!=n with gcd>1) is exhaustive and correct. Each case correctly tracks (P, k).
- **Load-bearing lemmas identified with mechanism?**
  - Euclidean identity: gcd(min(a,b), |a-b|) = gcd(a,b) -- mechanism is subtraction step of Euclid. Verified by test.
  - G_p invariant via the Euclidean identity on valuations -- correct.
  - gcd(k,0) = k -- standard convention, correct.
  - k >= 1 at termination via G_p >= 1 for some prime p -- correct.
- **Complete case coverage?** Yes. Cases A, B, C are disjoint and exhaustive.
- **Open gaps:** The three gaps identified (verify casework exhaustion, prove Euclidean identity, verify lcm/gcd > 1 in Case C) are all routine and closable.

**Small-case verification:** Tested with Python; all claims confirmed. The operation on valuations is (a,b) -> (min(a,b), |a-b|), the Euclidean identity holds, and M = prod p^{G_p} matches simulation.

**Issues to address during build:**
1. Gap 3 (lcm(m,n)/gcd(m,n) > 1 in Case C when m != n): Need to show that if m = ga, n = gb with gcd(a,b) = 1, then ab >= 2 when m != n. This follows because a != b (else m = n), and a,b >= 1 coprime implies ab >= 2.

---

## Approach 2: omega-monovariant

**Verdict: APPROVE**

**Assessment:**
- **Right technique?** Yes. Using Omega(n) = sum of v_p(n) as the primary monovariant is cleaner than the product monovariant because the decrease formula is explicit: S_after = S_before - Omega(g).
- **Sound skeleton?** Yes. The formula Omega(g) + Omega(mn/g^2) = Omega(m) + Omega(n) - Omega(g) is correct. The lexicographic (S, k) monovariant works.
- **Load-bearing lemmas identified with mechanism?**
  - Omega subadditivity: correct formula with mechanism (multiplicativity of Omega over coprime factors).
  - k drops when gcd=1: outputs are (1, mn), so exactly one entry > 1 -- correct.
  - G_p invariant: same as approach 1, correct.

**Issues to address during build:**
1. Gap 1: Prove Omega(mn/g^2) = Omega(m) + Omega(n) - 2*Omega(g) explicitly. This follows from Omega(mn) = Omega(m) + Omega(n) (true when factorizations don't overlap in the count, but actually Omega IS additive on products: Omega(xy) = Omega(x) + Omega(y) for all x,y). Then Omega(mn/g^2) = Omega(mn) - Omega(g^2) = Omega(m) + Omega(n) - 2*Omega(g).

**Small-case verification:** Confirmed by Python test.

---

## Approach 3: euclidean-reduction

**Verdict: APPROVE**

**Assessment:**
- **Right technique?** Yes. The structural insight that the operation IS the subtractive Euclidean algorithm on valuation coordinates is correct and illuminating.
- **Sound skeleton?** Yes, but slightly less direct than the other two. The per-prime analysis (sum of v_p decreases by min(a,b) each move) is correct. The global termination argument via total Omega is the same as approach 2.
- **Load-bearing lemmas identified with mechanism?**
  - Operation on valuations = Euclidean step: (a,b) -> (min(a,b), |a-b|) -- correct.
  - Sum decreases: min(a,b) + |a-b| = max(a,b) < a+b when a != b, a,b > 0 -- correct.
  - Multi-number Euclidean terminates with one nonzero entry -- this is the key claim that needs proof.

**Issues to address during build:**
1. Gap 1: The claim that iterated Euclidean steps on a multiset eventually reduce all but one entry to 0 needs justification. The standard Euclidean algorithm on two numbers terminates because gcd(a,0) = a. For a multiset, we need to argue that the sum strictly decreases until all pairs have at least one 0, at which point the gcd is concentrated in one entry.
2. Gap 3: Connection between per-prime termination and global termination needs the lexicographic (S, k) argument.

**Small-case verification:** Confirmed by Python test.

---

## Ranking

All three approaches are sound and target the complete problem (both parts a and b). They share the same core insight: the p-adic invariant G_p = gcd(v_p(a_i)) determines M = prod p^{G_p}.

**Head-to-head comparisons:**
1. **p-adic-gcd-invariant vs omega-monovariant**: Draw. Both are complete; omega has a cleaner monovariant formula, p-adic has clearer case exposition.
2. **p-adic-gcd-invariant vs euclidean-reduction**: p-adic wins. More direct casework, fewer gaps.
3. **omega-monovariant vs euclidean-reduction**: omega wins. More direct, same termination argument but cleaner presentation.

**Final Elo:**
- p-adic-gcd-invariant: 1516.0
- omega-monovariant: 1515.3
- euclidean-reduction: 1468.7

---

## Build Set Decision

For Round 1, I recommend building **two** approaches to establish a baseline and test both monovariant styles:

1. **p-adic-gcd-invariant** (Elo 1516.0): Clearest case analysis, most pedagogical.
2. **omega-monovariant** (Elo 1515.3): Cleaner monovariant formula, may yield a shorter proof.

The euclidean-reduction approach, while sound, is more conceptual and the gaps are slightly harder to close. It can be built in a later round if the other two stall.

---

build set: p-adic-gcd-invariant, omega-monovariant
