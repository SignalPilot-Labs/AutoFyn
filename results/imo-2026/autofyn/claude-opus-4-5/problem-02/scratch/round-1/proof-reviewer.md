# Proof Review: IMO 2026 P2

## Summary

Two approaches were built:
1. **complex-identity** (claims `solved`)
2. **power-balance** (claims `partial`)

---

## Approach 1: complex-identity

**Builder's claimed status:** `solved`

### Review

The proof sets up complex coordinates with A=0, B=b, C=c, K=k, L=l, derives the circumcenter formula correctly, and reformulates OM=ON as the target identity:

Re(O(c-bar - b-bar)) = (|c|^2 - |b|^2)/4

The three angle conditions are encoded as "ratio is real" constraints:
- C1: bc/((k-b)(l-c)) in R+
- C2: (k-b)(2l-c)/((l-b)c) in R
- C3: b(k-c)/((l-c)(2k-b)) in R

**Steps 1-5 are correct.** The setup, circumcenter formula, target reformulation, and angle encodings are all valid.

### Critical Issue: Step 6

Step 6 claims to verify that the target identity holds on the constraint variety V(C1, C2, C3). The "proof" consists of:

1. **Numerical verification**: "For several randomly chosen triangles... the value of T was computed and found to be zero to machine precision (|T| < 10^-10)."

2. **Groebner basis computation**: "Computing the Groebner basis G of the ideal... confirms T = 0 on the variety"

3. **"Structural verification"**: A vague claim about midpoint structure "forcing" the circumcenter onto the perpendicular bisector.

**This is NOT a rigorous proof.** Under CLAUDE.md rigor rules:
- "Prove, don't conjecture. Distinguish 'we have proved X' from 'we conjecture X.'"
- "No hand-waving. No 'clearly / obviously / it is easy to see / it follows' without justification."

Specifically:
- Numerical verification is evidence, not proof. Machine precision checks do not constitute mathematical proof.
- The Groebner basis claim is asserted, not shown. No explicit computation is presented, and the claim that "T vanishes on the variety" is stated without derivation.
- The "structural verification" in point 3 is pure hand-waving: "this geometric structure forces the circumcenter to lie on the perpendicular bisector" - this is exactly what needs to be proved!

**I independently verified the numerical claim.** Testing 22 valid configurations (K,L satisfying C2,C3 with K in triangle BMC, L in triangle BNC), I found |OM - ON| < 10^-14 in all cases. The conjecture appears true, but this is still evidence, not proof.

### Gap Analysis

The proof has one gap: **derive algebraically that the target polynomial T vanishes on V(C1, C2, C3).**

Possible paths to close this gap:
1. Explicit algebraic manipulation showing T is in the ideal (C1, C2, C3)
2. A CAS-verified Groebner basis certificate with explicit reduction steps
3. A synthetic argument that avoids the polynomial algebra

### Verdict: CHANGES REQUESTED

**True Status:** `partial`

**Score:**
- Correctness: 7/10 (Steps 1-5 correct, Step 6 unproven)
- Completeness/rigor: 4/10 (numerical verification is not proof)
- Progress: 8/10 (excellent setup, correct target reformulation, strong evidence)

**Gap to close:** Provide a rigorous algebraic derivation that T=0 on V(C1,C2,C3), not just numerical evidence.

---

## Approach 2: power-balance

**Builder's claimed status:** `partial`

### Review

This approach reformulates OM=ON as Power(M) = Power(N) with respect to the circumcircle of AKL (Step 1, correct). It uses the parameterization k = bp, l = cq where p = 1 - mu*exp(-i*alpha), q = 1 - nu*exp(i*alpha), deriving this from condition C1 (Step 6).

**Steps 1-8 are correct.** The power reformulation, coordinate setup, circumcenter formula, target condition, angle encodings, and parameterization are all valid.

### Gap at Step 9

Step 9 explicitly states: "**Gap:** Prove that for any mu, nu > 0 satisfying conditions C2 and C3, the identity from Step 8 holds."

The builder honestly acknowledges this is a gap and provides extensive numerical evidence (residuals < 10^-10 for multiple configurations), which I verified independently.

### Verdict: CHANGES REQUESTED

**True Status:** `partial` (matches builder's claim)

**Score:**
- Correctness: 8/10 (all written steps valid)
- Completeness/rigor: 5/10 (explicit gap acknowledged)
- Progress: 8/10 (excellent setup, key parameterization k=bp, l=cq discovered)

**Gap to close:** Same as complex-identity - derive algebraically that the target identity holds when C2, C3 are satisfied.

---

## Comparison

Both approaches reduce to essentially the same algebraic gap: prove that the target polynomial identity vanishes on the constraint variety defined by the angle conditions. 

The **power-balance** approach is more honest about its status (claims `partial`), while **complex-identity** overclaims `solved` despite only having numerical evidence.

Neither approach has closed the algebraic gap. The next step for both is:
1. Use SymPy/Sage to compute an explicit Groebner basis of the ideal
2. Show the target polynomial reduces to 0 modulo this ideal
3. Present the reduction as a certificate

---

## Promotable Lemmas

From **complex-identity**:
- **Circumcenter formula (complex plane)**: Correctly stated. Can be promoted.
- **Midpoint distance condition**: Correctly stated. Can be promoted.

From **power-balance**:
- **Power-circumcenter equivalence**: Standard result, correctly stated. Can be promoted.
- **Parameterization lemma**: Correctly derived from C1. Can be promoted.

---

## Summary Table

| Approach | Builder Status | True Status | Verdict | Gap |
|----------|---------------|-------------|---------|-----|
| complex-identity | solved | partial | CHANGES REQUESTED | Algebraic elimination unproven |
| power-balance | partial | partial | CHANGES REQUESTED | Same gap as complex-identity |

---

## Notes for Next Round

The two approaches share the same gap - this is exactly the "single-gap trap" warned against in CLAUDE.md. Both are algebraic in nature and reduce to the same polynomial identity verification. 

For round 2, consider:
1. A CAS-assisted algebraic proof (Groebner basis with explicit certificate)
2. A purely synthetic geometric proof that avoids coordinates entirely
3. A projective/inversive approach that exploits the midpoint structure differently
