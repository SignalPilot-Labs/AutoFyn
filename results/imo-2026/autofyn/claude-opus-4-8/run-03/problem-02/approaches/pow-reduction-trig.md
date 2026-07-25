# Approach: pow-reduction-trig

## Status
partial

## Approaches tried
- (new, round 1) Power-of-a-point reduction to a length/coordinate identity, proved by
  law of sines in the sub-triangles fixed by the angle hypotheses. **Reduction chain
  fully closed and rigorously proved; all sub-triangle length lemmas and the two
  constraint equations (★),(★★) derived from scratch. The single remaining step is one
  trigonometric identity (the "balance identity"), verified numerically to 1e-13 on three
  independent scalene triangles but not yet given a from-scratch derivation.** Round-1
  outcome: substantial progress, one explicit bounded gap remains.
- (advance, round 2) Attacked GAP-2 (the balance identity E(β)≡0) by an EXACT structural
  reduction. Three new exact symbolic facts established (all reproducible in sympy, not
  numeric samples): (i) the constraint (★) is *exactly* `C1 = 2 sinA cosC sin²γ +
  sinC sin(β+γ) sin(γ−A−β)`, which is **affine-linear in (cos2γ, sin2γ)**, and likewise
  (★★) is affine-linear in (cos2δ, sin2δ); (ii) after clearing the two ray denominators,
  `Ẽ := E · sin²(A+β+γ) · sin²(A+β+δ)` is **exactly bilinear** in the pairs
  (cos2γ,sin2γ) × (cos2δ,sin2δ) — every γ- and δ-harmonic above the first vanishes
  identically (verified: the sympy polynomial has degree ≤1 in each of cos2γ,sin2γ,
  cos2δ,sin2δ and no odd-harmonic remainder); (iii) consequently the balance identity is
  equivalent to the *purely linear-algebraic* membership `Ẽ = f·C1 + g·C2` with `f`
  affine in (cos2δ,sin2δ) and `g` affine in (cos2γ,sin2γ). This 6-parameter linear system
  is **consistent** (its coefficient matrix has rank 5 equal to the augmented rank 5 at
  generic A,B,β), and `Ẽ` was confirmed to vanish at **all four** common zeros of
  (C1,C2) on the two unit circles (both branches each). Outcome: the gap is reduced from a
  transcendental identity to an *exact finite linear-algebra identity whose consistency is
  established*; the explicit closed-form cofactors f,g (valid modulo sin²+cos²=1) were not
  extracted symbolically within budget (sympy's solve/linsolve choked on the trig field;
  the rank certificate is currently numeric-at-generic-point). Still `partial`.

## Current best
The problem is reduced, with full rigor, to a single explicit trigonometric identity.

Place `A` at the origin. Then `M = B/2`, `N = C/2` (midpoints). Writing `O` for the
circumcentre of `△AKL` and `P·Q` for the dot product, the following chain is proved
below with no gaps:

```
OM = ON
   ⟺  O·(B−C) = (|B|² − |C|²)/4            (Lemma 1, reduction)
   ⟺  pow(B, ⊙AKL) − pow(C, ⊙AKL) = (c² − b²)/2   (equivalent power form)
```
with `c = AB = |B|`, `b = AC = |C|`. Using the circumcentre relations
`O·K = |K|²/2`, `O·L = |L|²/2` (Lemma 2) and the sub-triangle lengths (Lemma 3),
the target `O·(B−C) = (|B|²−|C|²)/4` becomes a closed trigonometric identity in the
single free parameter `β` once the two constraint equations `(★)`, `(★★)` (which
encode the hypotheses H2, H3) are imposed. **That final identity — call it the balance
identity, stated precisely in "Open gap" below — is verified numerically (E ≤ 1e-13 on
three independent triangles at their admissible β) but is the one step not yet proved
symbolically from scratch.**

Everything up to and including Lemma 3 and the explicit statement of the balance identity
is complete and rigorous.

## Target
The problem's actual claim: `OM = ON` for every admissible configuration.

## Setup and conventions

Triangle `ABC`, non-degenerate. Angles `A = ∠BAC`, `B = ∠ABC`, `C = ∠ACB`
(`A+B+C = π`); sides `a = BC`, `b = CA`, `c = AB`. Let `R₀` be the circumradius of
`ABC`, so by the law of sines `a = 2R₀ sinA`, `b = 2R₀ sinB`, `c = 2R₀ sinC`.

`M, N` are the midpoints of `AB, AC`. The hypotheses (with `K ∈ int△BMC`,
`L ∈ int△BNC`, `K` inside `∠LBA`, `L` inside `∠ACK`):

- **(H1)** `∠KBA = ∠ACL =: β`.
- **(H2)** `∠LBK = ∠LNC`.
- **(H3)** `∠LCK = ∠BMK`.

Define
- `ψ := ∠LCK` (angle at `C` between rays `CL` and `CK`); since `L` is inside `∠ACK`,
  `∠ACK = ∠ACL + ∠LCK = β + ψ`, i.e. ray `CK` makes angle `β+ψ` with ray `CA`.
- `φ := ∠LBK` (angle at `B` between rays `BK` and `BL`); since `K` is inside `∠LBA`,
  `∠LBA = ∠KBA + ∠LBK = β + φ`, i.e. ray `BL` makes angle `β+φ` with ray `BA`.

Thus, as a point set,
- `K = ray_B(β) ∩ ray_C(β+ψ)`, where `ray_B(t)` is the ray from `B` making angle `t`
  with `BA` (turning into the triangle), and `ray_C(t)` is from `C` making angle `t`
  with `CA` (turning into the triangle);
- `L = ray_C(β) ∩ ray_B(β+φ)`.

**Symmetry σ.** Swapping `B↔C`, `K↔L`, `M↔N`, `b↔c`, `B↔C` (angles), `ψ↔φ` maps the
hypotheses to themselves: (H1) is symmetric, and σ exchanges (H2)↔(H3). Hence any
identity we prove for the `B`-side transports to the `C`-side by relabelling; we use
this to halve the length computations.

**Named tools** (all from `knowledge_base.md`, "Geometry (synthetic & analytic)"):
- *Power of a point* and *circle facts* (Synthetic toolkit).
- *Law of sines / law of cosines* in a triangle.
- *Coordinates to exploit symmetry* — we place `A` at the origin, which turns the
  midpoint hypothesis into `M = B/2`, `N = C/2` and makes the reduction one line.

Throughout, `|X|` is the distance from `X` to the origin `A`, so `|B| = AB = c`,
`|C| = AC = b`, `|K| = AK`, `|L| = AL`.

---

## Lemma 1 (Reduction). With `A` at the origin, `OM = ON ⟺ O·(B−C) = (|B|²−|C|²)/4`.

*Proof.* `M = (A+B)/2 = B/2` and `N = C/2` because `A = 0`. Then
```
OM² − ON² = |O − B/2|² − |O − C/2|²
          = (|O|² − O·B + |B|²/4) − (|O|² − O·C + |C|²/4)
          = − O·(B − C) + (|B|² − |C|²)/4.
```
Since `OM, ON ≥ 0`, `OM = ON ⟺ OM² = ON² ⟺ O·(B−C) = (|B|²−|C|²)/4`. ∎

**Power form (equivalent).** For any point `P`, `pow(P, ⊙AKL) = |P−O|² − R²` where
`R = OA = |O|` (as `A = 0` is on the circle). Hence
`pow(B) − pow(C) = |B−O|² − |C−O|² = |B|² − |C|² − 2O·(B−C)`. Substituting the criterion
of Lemma 1, `O·(B−C) = (|B|²−|C|²)/4`, gives
`pow(B) − pow(C) = (|B|²−|C|²) − (|B|²−|C|²)/2 = (|B|²−|C|²)/2 = (c²−b²)/2`.
So equivalently **`OM = ON ⟺ pow(B) − pow(C) = (c²−b²)/2`.** (This is the "power
difference" form; it also follows from the midpoint-power identity
`pow(M) = pow(B)/2 − c²/4`, `pow(N) = pow(C)/2 − b²/4`, since `pow(A)=0`.)

This is the promised power-of-a-point reduction, now with the second circle intersections
`X, Y` eliminated in favour of the cleaner points `B, C`.

---

## Lemma 2 (Circumcentre relations). `O·K = |K|²/2` and `O·L = |L|²/2`.

*Proof.* `O` is equidistant from `A=0`, `K`, `L`: `|O−K|² = |O−A|² = |O|²`. Expanding
`|O−K|² = |O|² − 2O·K + |K|²` gives `−2O·K + |K|² = 0`, i.e. `O·K = |K|²/2`. Likewise
for `L`. ∎

These two linear equations determine `O` (as `K, L` are linearly independent — `A,K,L`
are not collinear, being three points of a genuine circle), so
`O = ( (|K|²/2)·L^⊥·… )`; concretely, solving the 2×2 system,
```
O·(B−C) = [ det(B−C, L)·|K|² + det(K, B−C)·|L|² ] / ( 2·det(K, L) ),   (†)
```
where `det(u,v) = u_x v_y − u_y v_x`. (Derivation: write `B−C = λK + μL`; by Cramer
`λ = det(B−C,L)/det(K,L)`, `μ = det(K,B−C)/det(K,L)`; then
`O·(B−C) = λ(O·K)+μ(O·L) = (λ|K|²+μ|L|²)/2`, which is (†).)

Thus, by Lemmas 1–2, the whole problem is the single scalar identity
```
det(B−C, L)·|K|² + det(K, B−C)·|L|² = ½ (|B|² − |C|²) · det(K, L).   (‡)
```

---

## Lemma 3 (Sub-triangle lengths and the constraint equations).

Set `2R₀ = 1` (a global scaling; all four sides and `O·(B−C)`, `|B|²−|C|²` scale
homogeneously so the identity (‡) is scale-invariant). Then `a = sinA`, `b = sinB`,
`c = sinC`.

**(3a) `BK` from triangle `BMK` (uses H1, H3).** `M` lies on segment `AB`, so ray `BM =`
ray `BA` and `∠MBK = ∠ABK = β`. By H3, `∠BMK = ∠LCK = ψ`. In `△BMK`, `BM = c/2`,
`∠MBK = β`, `∠BMK = ψ`, hence `∠BKM = π−β−ψ`. Law of sines:
```
BK / sin∠BMK = BM / sin∠BKM  ⟹  BK = (c/2)·sinψ / sin(β+ψ).     (3a)
```

**(3b) `BK` from triangle `BKC` (geometry of the two rays).** `∠KBC = ∠ABC − ∠ABK
= B − β`. `∠KCB = ∠ACB − ∠ACK = C − (β+ψ)`. Hence `∠BKC = π − (B−β) − (C−β−ψ)
= π − B − C + 2β + ψ = A + 2β + ψ`. Law of sines in `△BKC` (`BC = a`):
```
BK = a · sin∠KCB / sin∠BKC = a · sin(C−β−ψ) / sin(A+2β+ψ).       (3b)
```

**Constraint (★).** Equating (3a),(3b) and using `c = sinC`, `a = sinA`:
```
sinC · sinψ · sin(A+2β+ψ) = 2 sinA · sin(C−β−ψ) · sin(β+ψ).       (★)
```
This is one transcendental equation for `ψ` given `β` (and `A, C`); it encodes exactly
that the point `K` built from `∠BMK = ψ` also sits on the ray `ray_C(β+ψ)`.

**(3c)–(3d) `CL`, and constraint (★★), by σ-symmetry.** Applying σ (`B↔C`, `b↔c`,
`ψ↔φ`, `M↔N`) to (3a),(3b): `N` on `AC`, `∠NCL = β`, `∠LNC = φ` (H2), `NC = b/2`:
```
CL = (b/2)·sinφ / sin(β+φ)        (3c, from △CNL)
CL = a · sin(B−β−φ) / sin(A+2β+φ)  (3d, from △BLC, ∠BLC = A+2β+φ)
```
and the constraint
```
sinB · sinφ · sin(A+2β+φ) = 2 sinA · sin(B−β−φ) · sin(β+φ).       (★★)
```

These give `K = B + BK·\hat d_{BK}` and `L = C + CL·\hat d_{CL}` explicitly, with
`\hat d_{BK}`, `\hat d_{CL}` the unit ray directions, hence all of `K, L` (and via (‡)
the whole target) as explicit trigonometric functions of `β, ψ, φ` subject to (★),(★★).
Each of (★),(★★) has a unique admissible root (it reduces to `P cos2ψ + Q sin2ψ + S = 0`
after product-to-sum, a single sinusoid), and by (3a),(3b) `ψ` is a real-analytic
function of `β` on the admissible interval; likewise `φ`. ∎

---

## Reduction to the balance identity (numerically verified, symbolic proof is the gap)

Combining Lemmas 1–3: `OM = ON` for the admissible configuration is **equivalent** to
the identity (‡) after substituting the explicit `K(β,ψ)`, `L(β,φ)` from Lemma 3 and the
constraints (★),(★★). Writing the residual
```
E(β) := O·(B−C) − (|B|² − |C|²)/4         (with ψ = ψ(β), φ = φ(β) from (★),(★★)),
```
`OM = ON ⟺ E(β) = 0`.

**Verification.** With `A` at the origin, `B = (c,0)`, `C = (b cosA, b sinA)`, and unit
ray directions
```
\hat d_{BK} = (−cosβ, sinβ),   \hat d_{CK} = (−cos(A+β+ψ), −sin(A+β+ψ)),
\hat d_{BL} = (−cos(β+φ), sin(β+φ)), \hat d_{CL} = (−cos(A+β), −sin(A+β)),
```
(orientations fixed by requiring `K, L` to lie inside the triangle — checked against the
explicit numerics), solving (★),(★★) for `ψ, φ` and evaluating `E(β)` gives
`|E| ≤ 1.4e-13` on three independent scalene triangles
`(A,B,C) = (73.7°,52.8°,53.5°), (80°,60°,40°), (64°,70°,46°)` at their admissible
`β`, while `E` is `O(10⁻²)` off the constraint (so the vanishing genuinely uses
(★),(★★), it is not an unconditional identity). The reduction chain
`OM=ON ⟺ pow(B)−pow(C)=(c²−b²)/2 ⟺ MX/NY = b/c` recorded by the explorers is thereby
confirmed and, up to the balance identity, fully derived.

## Structural reduction of the balance identity (round 2 — exact facts)

Write the two constraints, using product-to-sum on (★),(★★), in the exact forms
```
C1(γ) := 2 sinA cosC sin²γ + sinC sin(β+γ) sin(γ−A−β)      (= (★) exactly)
C2(δ) := 2 sinA cosB sin²δ + sinB sin(β+δ) sin(δ−A−β)      (= (★★) exactly)
```
where `γ := β+ψ = ∠ACK` and `δ := β+φ = ∠ABL`. Both are verified in sympy to equal the
original residuals identically. Using `2sin²γ = 1−cos2γ`, `sin(β+γ)sin(γ−A−β) =
½[cos(A+2β) − cos(A−... )]`, each of `C1, C2` is **affine-linear** in `(cos2γ, sin2γ)`
resp. `(cos2δ, sin2δ)`:
```
C1 = p₀ + p₁ cos2γ + p₂ sin2γ,   C2 = q₀ + q₁ cos2δ + q₂ sin2δ,
```
with `p_i, q_i` explicit in `A,B,β`.

Clearing the two ray denominators, put `Ẽ := E · sin²(A+β+γ) · sin²(A+β+δ)`. Because the
length `BK = a sin(C−γ)/sin(A+β+γ)` always appears multiplied by `sin(A+β+γ)` inside `Ẽ`,
every γ-monomial of `Ẽ` is an even harmonic of degree ≤ 2, i.e. `Ẽ` lies in
`span{1, cos2γ, sin2γ}` (and likewise for δ). Sympy confirms exactly:
`Ẽ` is **bilinear** in `(cos2γ, sin2γ) × (cos2δ, sin2δ)` — degree ≤1 in each of the four,
no odd-harmonic terms. Hence `Ẽ = [1, cos2γ, sin2γ] · M · [1, cos2δ, sin2δ]ᵀ` for a
`3×3` matrix `M(A,B,β)`.

**Reduction achieved.** Since `E = 0 ⟺ Ẽ = 0` (the two sines are nonzero on the
admissible interval), the balance identity is now the *exact* statement:
```
Ẽ  =  f · C1  +  g · C2      with   f affine in (cos2δ, sin2δ),  g affine in (cos2γ, sin2γ).
```
Equivalently `M w_i ∥ (p₀,p₁,p₂)` for each of the two roots `w_i = (1, cos2δ_i, sin2δ_i)`
of `C2` on the unit circle. This 6-parameter linear system was checked **consistent**
(coefficient matrix rank 5 = augmented rank 5 at generic `A,B,β`), and `Ẽ` was verified to
vanish at **all four** common zeros of `(C1, C2)` on the two unit circles.

## Open gap (the one remaining step, now purely linear-algebraic)

**GAP-2′.** Exhibit the explicit cofactors `f, g` above (rational-trigonometric in
`A,B,β`, valid modulo `sin²+cos² = 1`) and verify `Ẽ − f·C1 − g·C2 ≡ 0` as a symbolic
identity. This is a *finite* linear solve over the field `ℚ(sinA,cosA,sinB,cosB,sinβ,cosβ)`
whose consistency (rank 5 = rank 5) is established; the only missing piece is the
from-scratch closed form. (Within this round sympy's `solve`/`linsolve` failed to return
the solution on the trig field, and the rank certificate remains numeric-at-generic-point,
so per the run-state "no numeric-only load-bearing step" rule this is not yet a full solve.)
A subset solve produced candidate cofactors, but their residual is zero only *modulo* the
Pythagorean relations and that final modular reduction did not terminate in budget.

Two clean finishes for next round: (a) compute `M`, `c1=(p_i)`, `c2=(q_i)` explicitly and
verify `M = c1 aᵀ + b c2ᵀ` (rank-≤2 structure) by exhibiting `a, b` — a `3×3` factorisation,
far smaller than the raw trig; (b) prove the four-point vanishing geometrically (each
`M w_i ∥ c1`) via the affine-form proportionality: for fixed admissible δ, `Ẽ` is an affine
form in `(cos2γ,sin2γ)` vanishing at both circle-zeros of `C1`, hence proportional to `C1`,
hence zero at the geometric γ.

## Why this is a strong partial (not a dead end)
- The reduction `OM=ON ⟺ pow(B)−pow(C)=(c²−b²)/2` (Lemmas 1–2) is complete, short, and
  eliminates `O, R, X, Y` entirely — a genuine simplification over the outline's
  `MX/NY = b/c` route.
- All four sub-triangle law-of-sines relations and both constraint equations (★),(★★)
  are derived from scratch (GAP-1 of the outline is **closed**).
- Round 2 replaced the numeric-only balance identity by an **exact structural reduction**:
  the constraints are affine-linear in `(cos2γ,sin2γ)`/`(cos2δ,sin2δ)` and the cleared
  residual `Ẽ` is exactly bilinear in these pairs (proven symbolically). The whole problem
  is thereby reduced to a `3×3` bilinear-form membership `Ẽ = f·C1 + g·C2` — a finite
  linear-algebra fact whose consistency (rank 5 = rank 5) is verified. Only the explicit
  from-scratch cofactor identity (GAP-2′) remains, and two concrete finishes are recorded.

## Promotable lemmas
- **Lemma 1 (origin-at-A reduction):** For `O = circumcentre(AKL)` and `A` at the
  origin, `OM = ON ⟺ O·(B−C) = (|B|²−|C|²)/4 ⟺ pow(B,⊙AKL) − pow(C,⊙AKL) = (c²−b²)/2`.
  Proved in full above; reusable by any approach targeting this problem.
- **Lemma 3 sub-triangle lengths:** `BK = (c/2)sinψ/sin(β+ψ) = a·sin(C−β−ψ)/sin(A+2β+ψ)`
  with `ψ = ∠LCK = ∠BMK`, and the σ-image for `CL`. Proved in full (two independent
  law-of-sines computations, triangles `BMK` and `BKC`).
- **Lemma 4 (constraint normal form, round 2, PROVEN exactly):** With `γ=β+ψ`, `δ=β+φ`,
  constraint (★) equals `2 sinA cosC sin²γ + sinC sin(β+γ) sin(γ−A−β) = 0`, which is
  affine-linear in `(cos2γ, sin2γ)`; the σ-image gives (★★) affine-linear in
  `(cos2δ, sin2δ)`. Verified identically in sympy against the raw law-of-sines residuals.
- **Lemma 5 (bilinearity of the cleared balance residual, round 2, PROVEN exactly):**
  `Ẽ := (O·(B−C) − (|B|²−|C|²)/4)·sin²(A+β+γ)·sin²(A+β+δ)` is bilinear in
  `(cos2γ,sin2γ)×(cos2δ,sin2δ)` (degree ≤1 in each, no odd harmonics). Hence the balance
  identity is the bilinear-form membership `Ẽ = f·C1 + g·C2`, whose consistency (rank 5 =
  augmented rank 5) is verified.
