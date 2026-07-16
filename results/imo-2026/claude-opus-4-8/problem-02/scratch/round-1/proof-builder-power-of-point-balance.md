# Build report — power-of-point-balance (imo-2026-02, Prove OM=ON)

**Status: partial (strong).** Complete rigorous reduction of OM=ON to one explicit
coupled trig identity; that identity is the sole remaining gap.

## What I proved (fully rigorous, no gaps)
1. **Power reduction (Step 1):** OM=ON ⟺ pow(M,⊙AKL)=pow(N,⊙AKL) (pow(X)=|XO|²−ρ²).
2. **Secants through A (Step 2):** with d=signed AA′, e=signed AA″ (A′,A″ = second
   intersections of lines AB,AC with ⊙AKL), pow(M)=c²/4−(c/2)d, pow(N)=b²/4−(b/2)e, so
   OM=ON ⟺ **cd−be=(c²−b²)/2** (T). Signs handled uniformly by arc-length param; no case split.
3. **Chord/circumcenter computation (Steps 3–4):** d=2u·O, e=2v·O, and via O·K=k²/2,
   O·L=l²/2 plus B−C=μK+νL (Cramer) I derived
   cd−be = (2R sinA/sin(A−φ−ψ))·[k sin(C+ψ) − l sin(B+φ)].
   Key simplification is **Lemma S**: c sin(A−θ)+b sinθ = 2R sinA sin(C+θ) (proved).
4. **Step 5:** OM=ON ⟺ **(★★)  k sin(C+ψ) − l sin(B+φ) = R sin(C−B) sin(A−φ−ψ).**
5. **Trig-cevian data:** derived k=AK=c sinα/sin(α+φ), l=AL=b sinα/sin(α+ψ),
   cotφ=cotα+2cotγ, cotψ=cotα+2cotβ, and the two constraints
   (I) sinC sinγ sin(A+2α+γ)=2 sinA sin(C−α−γ) sin(α+γ), (II) its B↔C mirror,
   all from Law of Sines in triangles BMK,BKC,ABK / CNL,BLC,ACL.
6. Reduced (★★) to a polynomial identity **(♦5)** in sin/cos of α,β,γ,B,C.

All of the above are verified numerically to 1e-14 across three scalene triangles and all
α (scripts: scratch_pop.py, scratch_id.py; sanity in-repo).

## Remaining gap
Prove **(♦5)** (equivalently (★★)) from constraints (I),(II). It is:
- numerically exact (1e-14) on the solution variety, and
- provably a polynomial consequence of (I),(II)+Pythagorean relations — I obtained a
  multivariate-division cofactor certificate in sympy, but the cofactors are enormous
  (hundreds of terms) and NOT a human-presentable proof.
The identity is genuinely COUPLED (term P_C·N_C² mixes β-data with γ-data; W mixes both),
so simple decoupling fails. A Gröbner-basis membership check timed out (10 vars).

## Spec concerns
None. Problem statement is consistent; the three angle conditions yield a 1-parameter
family per triangle (parametrized by α), and OM=ON holds throughout (independently
re-confirmed).

## Note for the orchestrator
This approach shares its crux (★★)/(♦5) with trig-decoupled-bash (both funnel into the
same coupled trig identity forced by (I),(II)). The identity is TRUE and is a polynomial
consequence — the obstacle is presentation, not correctness. If neither trig route closes
(♦5) by hand next round, consider: (a) the complex-reality-conditions route, which bypasses
this identity entirely, or (b) tasking an outliner to find the correct cofactor split of
(♦5)=f·(I)+g·(II) (the sin²γ-leading-coefficient method is the natural attack but the
Pythagorean reduction entangles leading coefficients — needs care).
