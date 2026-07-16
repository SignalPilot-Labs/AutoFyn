## imo-2026-02

### Lens: Bypass via Direct OM=ON from Angle Conditions

---

## NEGATIVE RESULT: There is NO bypass to the Key Lemma

After systematic investigation of three proposed "direct" routes, I can confirm:

**OM = ON is provably equivalent to A' on circumcircle(AKL).**

The chain of equivalences is tight:
```
OM = ON
↔ O on perp-bisector of MN (= axis of reflection ρ swapping M↔N, A↔A')
↔ |OA| = |OA'| (since perp-bisector of MN = perp-bisector of AA')
↔ A' on circumcircle(AKL)
↔ pow(B,ω) - pow(C,ω) = (AB²-AC²)/2  [Claim 1 of power-of-point, PROVED]
```

Every "direct" route (radical axis, reflection, locus) collapses to one of these equivalent forms. There is no mathematical shortcut: any proof of OM=ON must prove A' on circumcircle(AKL).

---

## What was DEAD on Arrival

- **B,N,K,L concyclic from C2**: False. Numerically disproved (Im(CR) = 0.44, not 0).
- **C,M,K,L concyclic from C3**: False. Numerically disproved (Im(CR) = 1.39, not 0).
- **Any four-point concyclicity involving {B,C,M,N,K,L}**: All tested (8 combinations) are false.
- **Radical axis of circumcircles of BNK, CMK, etc. having O on perp-bisector of MN**: False numerically.
- **Miquel point of BK/CL transversals = A'**: False. The Miquel point is at ~(0.13, 1.97), not A' = (0.5, 2.0).

---

## POSITIVE FINDS (genuinely new)

### 1. THE MIDPOINT IS ESSENTIAL — numerically confirmed

Tested M = A + r(B-A), N = A + r(C-A) for r ∈ {0.3, 0.4, 0.5, 0.6, 0.7} with the SAME angle conditions C1, C2, C3:
- r = 0.5 (midpoints): OM - ON = 1.40e-12 ✓
- r = 0.3: OM - ON = 2.44e-02 ✗
- r = 0.4: OM - ON = 1.32e-02 ✗
- r = 0.6: OM - ON = 4.32e-03 ✗
- r = 0.7: OM - ON = 4.36e-03 ✗

**Implication**: Any proof MUST use BM = AB/2 and CN = AC/2 crucially. The "2" in the denominator is load-bearing.

### 2. EXPLICIT TRIGONOMETRIC FORMS OF C2 AND C3 (new, never derived before)

Setting BC = 1, with α = ∠BAC, β = ∠ABC, γ = ∠BCA, φ = ∠KBA = ∠ACL:

**From C3 (∠LCK = ∠BMK = ν) + law of sines in triangle BCK:**
```
2·sin(α)·sin(γ-φ-ν)·sin(φ+ν) = sin(γ)·sin(ν)·sin(α+2φ+ν)   ... (*)
```
This uniquely determines ν given α, β, γ, φ (numerically verified to < 1e-7).

**Geometric content of (*)**: The triangle BCK has ∠KBC = β-φ and ∠BCK = γ-φ-ν, and the law of sines in BCK gives BK = sin(γ-φ-ν)/sin(α+2φ+ν). The midpoint condition BM = AB/2 forces the "2sin(α)" on the left, which is why r = 1/2 is special.

**From C2 (∠LBK = ∠LNC = μ) + law of sines in triangle BCL:**
```
2·sin(α)·sin(β-φ-μ)·sin(φ+μ) = sin(β)·sin(μ)·sin(α+2φ+μ)   ... (**)
```
This uniquely determines μ given α, β, γ, φ, ν (the coupling between ν and μ is through K's position).

**Concrete consequence**: With BC = 1:
- BK = sin(γ-φ-ν)/sin(α+2φ+ν)
- CL = sin(β-φ-μ)/sin(α+2φ+μ)
- The directions: K is on the ray from B at angle (β-φ) from positive x-axis; L on the ray from C at angle (π-γ+φ) from positive x-axis.

These four quantities (two positions on rays, two distances along rays) fully determine (K, L) in pure trig terms.

### 3. THE POWER IDENTITY VIA INSCRIBED ANGLES (new approach ingredient)

Using the inscribed angle theorem in ω = circumcircle(AKL):

Since B, K, K'' are on line BK (K'' = second intersection with ω), and A, L are on ω:
- ∠BK''A = ∠KLA (inscribed angles for chord KA at K'' and L)
- ∠ABK'' = ∠ABK = φ (since K'' is on ray BK from B)

By law of sines in triangle ABK'':
```
BK'' = AB · sin(φ + ∠ALK) / sin(∠ALK)
```

Similarly: CL'' = AC · sin(φ + ∠AKL) / sin(∠AKL).

So the power identity pow(B,ω) - pow(C,ω) = (AB²-AC²)/2 becomes:
```
BK · AB · sin(φ+∠ALK)/sin(∠ALK) - CL · AC · sin(φ+∠AKL)/sin(∠AKL) = (AB²-AC²)/2
```

Substituting BK = sin(γ-φ-ν)/sin(α+2φ+ν), CL = sin(β-φ-μ)/sin(α+2φ+μ), AB = sin(γ)/sin(α), AC = sin(β)/sin(α), this becomes a pure trig identity in α, β, γ, φ, ν, μ, ∠AKL, ∠ALK.

**The gap in all approaches** = proving this identity after expressing ∠AKL and ∠ALK in terms of the other angles.

### 4. SYMMETRIC "ANGULAR SHIFT" REFORMULATION (new)

Key Lemma (A' on circumcircle of AKL) is equivalent to:
```
angle(BAL) - angle(BA'L) = angle(BAK) - angle(BA'K)
```
(The "angular shift" from A to A' in viewing K from the B-reference equals the shift in viewing L.)

Numerically: both differences ≈ 1.861°. 

This is yet another equivalent form (it reduces to cross-ratio (K,L;A,A') being real), but it suggests an approach: prove the angular shift is equal via the symmetry of the conditions.

---

## Most Promising Route for the Outliner

**Pure trigonometric identity proof via explicit trig forms:**

The Key Lemma reduces to showing that the point A' = (1/2, b) [intersection of perpendicular bisector of BC with horizontal through A] lies on the circle through A, K, L where K and L are EXPLICITLY GIVEN by:
- K = (sin(γ-φ-ν)/sin(α+2φ+ν)) · (cos(β-φ), sin(β-φ))  [from B = origin]
- L = (1,0) + (sin(β-φ-μ)/sin(α+2φ+μ)) · (-cos(γ-φ), sin(γ-φ))  [from C = (1,0)]
- A = (cos α_x, b) for the specific triangle
- A' = (1/2, b)

with ν and μ satisfying the trig conditions (*) and (**).

The concyclicity of A, K, L, A' reduces to Im[(A-K)(A'-L)/((A-L)(A'-K))] = 0, which with A-A' = a - 1/2 (real in these coordinates) simplifies to Im[(A-L)(A'-K)/(A'-L)] = 0 ... or the equivalent cross-ratio condition.

**This is a purely algebraic identity in the five quantities α, β, γ, φ, ν (with μ determined via (**) from them)**. Since both (*) and (**) are known, the "two-variable" system is closed, and the identity should be provable by polynomial manipulation or product-to-sum trig identities.

---

## Candidate Techniques

- **Law of sines trigonometric identity**: the explicit form of K and L gives a direct trig identity to verify (substitute into cross-ratio condition, use (*) and (**) to simplify)
- **Spiral similarity at L or K** (still unresolved from round 1; the specific conditions might define such a transformation more carefully than previously tried)
- **Power-of-point + inscribed angle theorem** (the BK'' formula above gives a new ingredient)
- **Directed angles mod π** (standard)

## Knowledge-Base Entries to Use

- **Geometry > synthetic toolkit**: power of a point, inscribed angles, spiral similarity
- **Geometry > Circle/triangle configuration facts**: inscribed angle theorem (used extensively)
- **Geometry > Coordinates / complex / barycentric**: trig form of concyclicity
- **Problem-Solving Heuristics > Introduce substitution**: the explicit trig forms (*) and (**) are the right substitution
- **Direct proof**: chain of trig identities from the explicit formulas

## Analogous Past Problems (cruxes)

None from the corpus (geometry not extracted). No analogues found.

## Prior Progress

Key Reduction PROVED (A' on circumcircle → OM = ON). Key Lemma UNPROVEN but numerically verified to 10^{-14}. Three approaches all blocked at the same gap.

## Dead Ends (do not retry)

- B,N,K,L concyclic: DISPROVED numerically.
- C,M,K,L concyclic: DISPROVED numerically.
- Any Miquel-point approach using standard transversals: Miquel point ≠ A'.
- "Locus" argument (K,L vary with conditions): The system is RIGID (0-parameter family for fixed φ, α, β, γ). No locus to take.
- Finding a bypass to Key Lemma: IMPOSSIBLE (OM=ON ↔ A' on circumcircle, full equivalence).

## Small-Case / Intuition Notes

- Midpoint essential: CONFIRMED. r = 1/2 is the unique ratio making OM=ON.
- The factor "2" in trig identities (*) and (**) [i.e., "2·sin(α)" on LHS] comes DIRECTLY from BM = AB/2, CN = AC/2. Without midpoints, this factor changes to "r/(1-r)·sin(α)" and OM ≠ ON.
- The "cross-pairing" (B↔N, C↔M) manifests as: condition (*) uses sin(γ) [from angle at C], and condition (**) uses sin(β) [from angle at B], with the factors SWITCHED from what one might naively expect. This switchover is the geometric content of the cross-pairing.
- CONJECTURE (strong numerical evidence, not proved): The Key Lemma A' on circumcircle(AKL) holds for all valid configurations. The proof is a trig identity in α, β, γ, φ, ν, μ satisfying (*) and (**).
