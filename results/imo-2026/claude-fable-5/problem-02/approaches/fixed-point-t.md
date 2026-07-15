# Approach: fixed-point-t

## Status
solved

## Target
The full claim of imo-2026-02: with M, N midpoints of AB, AC, K, L as in the statement, and O the circumcentre of AKL, prove OM = ON.

## Approaches tried
- (round 1, outline) Outlined; all steps verified numerically, Claims A/B certified by CAS. Not yet built.
- (round 1, build) Built in full. Restructured the outline's Steps 4–6: instead of defining T by two linear equations and proving the trig Claims A/B afterwards, T is **defined by its closed form** and four dot-product identities are verified directly — identities (i), (ii) collapse to the sine addition formula, and (iii), (iv) are short product-to-sum computations. This removes the mirror/reflection step and the CAS-only Claims A/B entirely. Every formula was independently re-verified numerically to ≤ 5e-15 during the build (5 triangles × several α, plus a spurious-root configuration). Result: complete proof below. — worked.

## Current best
Complete rigorous proof (below). No open gaps.

## Route (one paragraph)
Place B = (0,0), C = (a,0), A in the upper half-plane. The interiority hypotheses pin down the direction angles of the rays BK, BL, CK, CL (Lemma 1). The sine rule in triangles BMK and CNL gives one-parameter forms K = (c/2)(cos α − τ sin α)e^{i(B−α)}, τ = cot(α+γ), and the analogous form for L with σ = cot(α+β); the remaining constraints (sine rule in BKC, BLC) become two decoupled quadratics q_K(τ) = 0, q_L(σ) = 0 (Lemma 3). An explicit point T is then written down in closed form; four short trigonometric identities (Lemma 4) show that the power-type expression E(T; t) is *identically* proportional to q_K(t) (and, on the other side, to q_L(t)) as a polynomial in t — hence T is equidistant from A and K, and from A and L (Lemma 5). Since the perpendicular bisectors of AK and AL are distinct lines through both T and the circumcentre O, we get O = T; and T_x is visibly the abscissa of the midpoint of MN, giving OM = ON.

## Full proof

### 0. Statement, conventions, and named tools

**Problem.** Let ABC be a triangle, M, N the midpoints of AB, AC. Points K, L are chosen inside triangles BMC, BNC respectively, such that K lies inside the angle LBA, L lies inside the angle ACK, and
∠KBA = ∠ACL, ∠LBK = ∠LNC, ∠LCK = ∠BMK.
Let O be the circumcentre of triangle AKL. Prove OM = ON.

**Named tools used** (cf. `knowledge_base.md`, Geometry: synthetic toolkit and coordinates):
- **Law of Sines**: in any nondegenerate triangle XYZ with angles x, y, z at X, Y, Z and opposite sides of lengths |YZ|, |ZX|, |XY|, one has |YZ|/sin x = |ZX|/sin y = |XY|/sin z.
- **Angle sum of a triangle**: x + y + z = π.
- **Addition formulas**: sin(X±Y) = sin X cos Y ± cos X sin Y, cos(X±Y) = cos X cos Y ∓ sin X sin Y. All product-to-sum and sum-to-product identities used below are derived from these on the spot:
  - (PS1) 2 sin X sin Y = cos(X−Y) − cos(X+Y) (subtract the two cos formulas);
  - (PS2) 2 sin X cos Y = sin(X+Y) + sin(X−Y) (add the two sin formulas);
  - (PS3) 2 cos X cos Y = cos(X−Y) + cos(X+Y) (add the two cos formulas);
  - (SP1) cos X − cos(X+2δ) = 2 sin(X+δ) sin δ (apply PS1 with X+δ, δ);
  - (SP2) cos X + cos(X+2δ) = 2 cos(X+δ) cos δ (apply PS3 with X+δ, δ).
- Elementary vector algebra in ℝ²: dot product x·y, and the identity |x−z|² = |x|² − 2x·z + |z|².

**Coordinates and notation.** Write e^{iθ} := (cos θ, sin θ) ∈ ℝ². Denote by A, B, C both the vertices and the interior angles of the triangle (context disambiguates), and let a = |BC|, b = |CA|, c = |AB|. Place
  B = (0, 0), C = (a, 0), A in the open upper half-plane {y > 0}.
(Reflecting in the x-axis if necessary, this is no loss of generality; a reflection is an isometry, so it preserves all hypotheses and the conclusion OM = ON.)

The angle at B is the angle between rays BC and BA. Ray BC is the positive x-axis (direction angle 0). Since A_y > 0, the direction angle θ_A of ray BA lies in (0, π); the angle between the unit vectors e^{i·0} and e^{iθ_A} is θ_A (see the Angle Fact below), so θ_A = B. Hence

  A = c·e^{iB},  and likewise A − C = b·e^{i(π−C)},

the latter because ray CB has direction angle π, A lies above the x-axis, so ray CA has direction angle in (0, π), and the angle at C between rays CB and CA is C: the direction angle θ of ray CA satisfies |π − θ| = C with θ ∈ (0,π), i.e. θ = π − C.

In particular, reading off the x-coordinate of A = c·e^{iB} = C + b·e^{i(π−C)}:

  (Proj) c cos B = a − b cos C, i.e. a = b cos C + c cos B  (projection formula, proved by this coordinate computation).

Since B, C ∈ (0, π) and A = π − B − C ∈ (0, π), we have sin A, sin B, sin C > 0.

**Angle Fact.** For unit vectors e^{iθ₁}, e^{iθ₂} with |θ₁ − θ₂| ≤ π, the (unsigned) angle between them is |θ₁ − θ₂|. *Proof.* The angle is arccos(e^{iθ₁}·e^{iθ₂}) = arccos(cos θ₁ cos θ₂ + sin θ₁ sin θ₂) = arccos(cos(θ₁ − θ₂)), and arccos(cos φ) = |φ| for |φ| ≤ π. ∎

**Interiors.** For a nondegenerate triangle XYZ, "P lies (strictly) inside triangle XYZ" means P = λX + μY + νZ with λ, μ, ν > 0, λ + μ + ν = 1; this is the standard interior of the convex hull. Because X − Z and Y − Z are linearly independent, the coefficients (λ, μ, ν) of any such affine combination are unique: if λ₁X+μ₁Y+ν₁Z = λ₂X+μ₂Y+ν₂Z with λᵢ+μᵢ+νᵢ = 1, subtracting gives (λ₁−λ₂)(X−Z) + (μ₁−μ₂)(Y−Z) = 0, forcing λ₁ = λ₂, μ₁ = μ₂ and then ν₁ = ν₂. In particular a point inside triangle XYZ lies on none of the lines XY, YZ, ZX (points of line XY are exactly the affine combinations with ν = 0, by uniqueness), and is distinct from the vertices.

### 1. Sector Lemma and angle bookkeeping

**Lemma 0 (Sector Lemma).** Let X be a point and θ′ < θ″ with θ″ − θ′ < π. The interior of the (convex) angle bounded by the rays from X with direction angles θ′ and θ″ is
  S = { X + r e^{iθ} : r > 0, θ ∈ (θ′, θ″) }.
Moreover, for rays from X with direction angles θ₁, θ₂ ∈ [θ′, θ″], the angle between them is |θ₁ − θ₂|.

*Proof.* The interior of a convex angle of opening < π is the intersection of two open half-planes: the side of the line through X with direction e^{iθ′} containing the ray of direction θ″, and the side of the line through X with direction e^{iθ″} containing the ray of direction θ′. For a point X + r e^{iθ} (r > 0), its side of the line through X with direction e^{iθ′} is the sign of the cross product e^{iθ′} × e^{iθ} = cos θ′ sin θ − sin θ′ cos θ = sin(θ − θ′); for the reference point X + e^{iθ″} this sign is sin(θ″ − θ′) > 0. Normalizing θ ∈ [θ′ − π, θ′ + π), the condition sin(θ − θ′) > 0 reads θ ∈ (θ′, θ′ + π). The second half-plane condition is sin(θ − θ″) < 0; in the normalized range, θ − θ″ ∈ [θ′ − π − θ″, θ′ + π − θ″) ⊂ (−2π, π) (using 0 < θ″ − θ′ < π), and on (−2π, π) the sine is negative exactly on (−π, 0) (on (−2π, −π) it equals sin(x + 2π) with x + 2π ∈ (0, π), hence is positive), so the condition reads θ ∈ (θ″ − π, θ″). Since θ″ < θ′ + π, the intersection of the two conditions is θ ∈ (θ′, θ″). The angle statement is the Angle Fact (|θ₁ − θ₂| ≤ θ″ − θ′ < π). ∎

**Lemma 1 (Position and angle bookkeeping).** Define
  α := ∠KBA = ∠ACL, β := ∠LBK = ∠LNC, γ := ∠LCK = ∠BMK
(the equalities are the hypotheses). Then:
1. K and L lie strictly inside triangle ABC; in particular neither lies on any of the lines AB, BC, CA.
2. The direction angles of the relevant rays are:
   ray BA: B;  ray BK: B − α;  ray BL: B − α − β;
   ray CA: π − C;  ray CL: π − C + α;  ray CK: π − C + α + γ.
3. α > 0, β > 0, γ > 0, α + β < B, α + γ < C. Consequently 0 < A + α < π and sin(A + α) > 0.

*Proof.*
**(1)** Let P be inside triangle BMC: P = λB + μM + νC with λ, μ, ν > 0 summing to 1. Since M = (A+B)/2,
  P = (μ/2)A + (λ + μ/2)B + νC,
an affine combination with all three coefficients positive and total (μ/2) + (λ + μ/2) + ν = λ + μ + ν = 1. Hence P is inside triangle ABC. (Triangle BMC is nondegenerate: if B, M, C were collinear then A = 2M − B would lie on line BC, contradicting nondegeneracy of ABC.) The same computation with N = (A+C)/2 shows that any point inside triangle BNC is inside triangle ABC. So K, L are inside ABC, and by §0 they avoid the lines AB, BC, CA and the vertices.

**(2) and (3).** First, a point P = λA + μB + νC inside ABC (λ, μ, ν > 0) lies in the open sector at B between rays BC and BA: indeed P − B = λ(A − B) + ν(C − B) = λc·e^{iB} + νa·e^{i·0}, so writing P − B = r e^{iθ} (r > 0), the cross products give
  e^{i·0} × (P − B) = λc sin B > 0 and (P − B) × e^{iB} = (λc cos B + νa) sin B − (λc sin B) cos B = νa sin B > 0,
i.e. sin θ > 0 and sin(B − θ) > 0; with θ normalized to (−π, π] the first gives θ ∈ (0, π), and then B − θ ∈ (B − π, B) ⊂ (−π, π), so the second gives B − θ ∈ (0, π), i.e. θ ∈ (0, B). By Lemma 0 (applied with θ′ = 0, θ″ = B < π) this is exactly the interior of the angle ABC. Likewise at C: P − C = λ(A − C) + μ(B − C) = λb·e^{i(π−C)} + μa·e^{iπ}, so writing P − C = r e^{iθ} (r > 0, θ normalized to [0, 2π)), the cross products give
  e^{i(π−C)} × (P − C) = μa·(e^{i(π−C)} × e^{iπ}) = μa sin C > 0 and (P − C) × e^{iπ} = λb·(e^{i(π−C)} × e^{iπ}) = λb sin C > 0,
i.e. r sin(θ − (π−C)) > 0 and r sin(π − θ) > 0. The second gives θ ∈ (0, π); then θ − (π−C) ∈ (C − π, C) ⊂ (−π, π), so the first gives θ − (π−C) ∈ (0, π), i.e. θ ∈ (π − C, π): by Lemma 0 (θ′ = π − C, θ″ = π), P lies in the open sector at C between rays CA and CB.

Now:
- **Ray BK.** K is inside ABC, so the direction angle θ_K of ray BK lies in (0, B). By Lemma 0, ∠KBA = B − θ_K, so θ_K = B − α; and θ_K ∈ (0, B) gives 0 < α < B.
- **Ray CL.** L is inside ABC, so the direction angle θ′_L of ray CL lies in (π − C, π). By Lemma 0, ∠ACL = θ′_L − (π − C), so θ′_L = π − C + α; and θ′_L < π gives α < C.
- **Ray BL.** The direction angle θ_L of ray BL lies in (0, B) (L inside ABC). The hypothesis "K lies inside the angle LBA" says K is in the interior of the convex angle bounded by rays BL and BA; by Lemma 0 (with θ′ = θ_L, θ″ = B; opening B − θ_L < π) this means θ_K ∈ (θ_L, B), strictly. (Here we use that direction angles are unique modulo 2π: K = B + r e^{iθ} with θ ∈ (θ_L, B) forces θ ≡ θ_K (mod 2π), and both θ, θ_K lie in (0, B), an interval of length < 2π, so θ = θ_K. The same remark applies at C below.) Hence θ_L < θ_K and, by Lemma 0, β = ∠LBK = θ_K − θ_L > 0, so
  θ_L = θ_K − β = B − α − β, and θ_L > 0 gives α + β < B.
- **Ray CK.** The direction angle θ′_K of ray CK lies in (π − C, π) (K inside ABC). The hypothesis "L lies inside the angle ACK" (bounded by rays CA and CK, direction angles π − C and θ′_K, opening θ′_K − (π − C) < π) means θ′_L ∈ (π − C, θ′_K) strictly. Hence γ = ∠LCK = θ′_K − θ′_L > 0 and
  θ′_K = θ′_L + γ = π − C + α + γ, and θ′_K < π gives α + γ < C.

Finally α > 0, α + γ < C < π and A + α < A + C = π − B < π, A + α > A > 0, so sin(A + α) > 0. ∎

### 2. Parametrization Lemma

**Lemma 2 (Parametrization).** Set τ := cot(α + γ) and σ := cot(α + β) (well-defined: α + γ ∈ (0, C) ⊂ (0, π) and α + β ∈ (0, B) ⊂ (0, π), so the sines are positive). Then
  K = (c/2)(cos α − τ sin α)·e^{i(B−α)},
  L = C + (b/2)(cos α − σ sin α)·e^{i(π−C+α)}.

*Proof.* **K.** M = (A+B)/2, so M − B = (A − B)/2: M lies on ray BA with |BM| = c/2, and ray BM = ray BA. K does not lie on line AB (Lemma 1.1), so BMK is a nondegenerate triangle. Its angle at B is the angle between rays BM = BA and BK, namely ∠KBA = α; its angle at M is ∠BMK = γ (the hypothesis names this angle γ). By the angle sum, its angle at K is π − α − γ, which is positive, so α + γ < π and sin(π − α − γ) = sin(α + γ) > 0. The Law of Sines in triangle BMK gives
  |BK| / sin γ = |BM| / sin(∠BKM) ⟹ |BK| = (c/2)·sin γ / sin(α + γ).
Expanding sin γ = sin((α+γ) − α) = sin(α+γ) cos α − cos(α+γ) sin α and dividing by sin(α+γ) > 0:
  |BK| = (c/2)(cos α − τ sin α).
Since ray BK has direction angle B − α (Lemma 1.2), K = B + |BK| e^{i(B−α)}, which is the displayed formula (B is the origin).

**L.** N = (A+C)/2, so N − C = (A − C)/2: N lies on ray CA with |CN| = b/2, and ray CN = ray CA. L is not on line AC (Lemma 1.1), so CNL is a nondegenerate triangle; its angle at C is ∠LCN = ∠LCA = ∠ACL = α, its angle at N is ∠CNL = ∠LNC = β (hypothesis ∠LBK = ∠LNC and the definition β = ∠LBK). Its angle at L is π − α − β > 0. Law of Sines in CNL:
  |CL| = (b/2)·sin β / sin(α + β) = (b/2)(cos α − σ sin α),
by the same expansion. Since ray CL has direction angle π − C + α (Lemma 1.2), L = C + |CL| e^{i(π−C+α)}. ∎

### 3. Constraint Lemma: the two decoupled quadratics

For θ ∈ (0, π) define
  P(θ) := sin A cos θ + ½ sin θ cos A,  Q(θ) := ½ sin A sin θ,  R(θ) := sin A cos θ + ½ sin θ cos(A + 2α).

**Lemma 3a (closed forms of P ± R).** For every θ:
  P(θ) − R(θ) = sin θ sin α sin(A + α),  P(θ) + R(θ) = 2 sin A cos θ + sin θ cos α cos(A + α).

*Proof.* P − R = ½ sin θ·[cos A − cos(A + 2α)] = ½ sin θ · 2 sin(A + α) sin α by (SP1) with X = A, δ = α. P + R = 2 sin A cos θ + ½ sin θ [cos A + cos(A+2α)] = 2 sin A cos θ + ½ sin θ · 2 cos(A+α) cos α by (SP2). ∎

In particular, by Lemma 1.3 and sin B, sin C > 0:
  (†) P(C) − R(C) = sin C sin α sin(A+α) > 0 and P(B) − R(B) = sin B sin α sin(A+α) > 0.

**Lemma 3b (trig-to-quadratic conversion).** Let θ ∈ (0, π) and φ be angles with α + φ ∈ (0, π), and set t := cot(α + φ). If
  (E) sin θ sin φ sin(A + 2α + φ) = 2 sin A sin(α + φ) sin(θ − α − φ),
then
  (P(θ) − R(θ))·t² + 2Q(θ)·t − (P(θ) + R(θ)) = 0.

*Proof.* Put u := 2(α + φ), so u ∈ (0, 2π) and u/2 = α + φ ∈ (0, π).

*Step 1: product-to-sum.* By (PS1) with X = α+φ, Y = θ−α−φ (so X − Y = u − θ, X + Y = θ):
  2 sin(α+φ) sin(θ−α−φ) = cos(u − θ) − cos θ.
By (PS1) with X = φ, Y = A + 2α + φ (so Y − X = A + 2α, X + Y = A + u; PS1 is symmetric and cos is even):
  2 sin φ sin(A + 2α + φ) = cos(A + 2α) − cos(A + u).
Hence (E) is equivalent to
  (sin θ/2)[cos(A + 2α) − cos(A + u)] = sin A [cos(u − θ) − cos θ].

*Step 2: expand in cos u, sin u.* Using cos(u − θ) = cos u cos θ + sin u sin θ and cos(A + u) = cos A cos u − sin A sin u, the last display rearranges to
  cos u·[sin A cos θ + (sin θ/2) cos A] + sin u·[sin A sin θ − (sin θ/2) sin A] − [sin A cos θ + (sin θ/2) cos(A + 2α)] = 0,
i.e. (since sin A sin θ − ½ sin θ sin A = ½ sin A sin θ)
  (E′) P(θ) cos u + Q(θ) sin u − R(θ) = 0.

*Step 3: cotangent substitution.* Let h := u/2 ∈ (0, π), so sin h > 0 and t = cot h = cos h / sin h. Then t² + 1 = 1/sin² h, so sin² h = 1/(t²+1), and
  cos u = 1 − 2 sin² h = (t² − 1)/(t² + 1),  sin u = 2 sin h cos h = 2 sin² h · cot h = 2t/(t² + 1).
Substituting into (E′) and multiplying by t² + 1 > 0:
  P(θ)(t² − 1) + 2Q(θ) t − R(θ)(t² + 1) = 0, i.e. (P(θ) − R(θ)) t² + 2Q(θ) t − (P(θ) + R(θ)) = 0. ∎

**Lemma 3 (Constraint Lemma).** With τ, σ as in Lemma 2, and writing
  q_K(t) := (P(C) − R(C)) t² + 2Q(C) t − (P(C) + R(C)),  q_L(t) := (P(B) − R(B)) t² + 2Q(B) t − (P(B) + R(B)),
we have q_K(τ) = 0 and q_L(σ) = 0.

*Proof.* **K-side.** K does not lie on line BC (Lemma 1.1), so BKC is a nondegenerate triangle. Its angle at B is between rays BK (direction B − α) and BC (direction 0); both direction angles lie in [0, B] ⊂ [0, π), so by Lemma 0 the angle is B − α, which is positive by Lemma 1.3. Its angle at C is between rays CK (direction π − C + α + γ) and CB (direction π); both lie in [π − C, π], so the angle is π − (π − C + α + γ) = C − α − γ > 0 (Lemma 1.3). By the angle sum, the angle at K is π − (B − α) − (C − α − γ) = A + 2α + γ (using A = π − B − C). Law of Sines in BKC:
  |BK| = a·sin(C − α − γ)/sin(A + 2α + γ).
Equating with |BK| = (c/2) sin γ / sin(α+γ) from Lemma 2 and cross-multiplying (all denominators are sines of angles of a nondegenerate triangle, hence nonzero):
  c·sin γ·sin(A + 2α + γ) = 2a·sin(α + γ)·sin(C − α − γ).
By the Law of Sines in ABC, a = c sin A / sin C; substituting and multiplying by sin C / c > 0:
  sin C sin γ sin(A + 2α + γ) = 2 sin A sin(α + γ) sin(C − α − γ),
which is (E) with (θ, φ) = (C, γ). Lemma 3b gives q_K(τ) = 0.

**L-side.** L is not on line BC, so BLC is a nondegenerate triangle. Its angle at B is between rays BL (direction B − α − β) and BC (direction 0); both directions lie in [0, B], so by Lemma 0 it equals B − α − β, which is > 0 by Lemma 1.3. Its angle at C is between rays CL (direction π − C + α) and CB (direction π); both directions lie in [π − C, π], so by Lemma 0 it equals π − (π − C + α) = C − α > 0. Its angle at L is A + 2α + β. Law of Sines in BLC:
  |CL| = a·sin(B − α − β)/sin(A + 2α + β).
Equating with |CL| = (b/2) sin β / sin(α + β) from Lemma 2, cross-multiplying, and using a = b sin A / sin B:
  sin B sin β sin(A + 2α + β) = 2 sin A sin(α + β) sin(B − α − β),
which is (E) with (θ, φ) = (B, β). Lemma 3b gives q_L(σ) = 0. ∎

### 4. The point T and four dot-product identities

**Definition.** Let
  T := ( (c cos B)/2 + a/4 , (c sin B)/2 + (c sin A cos(A + α))/(4 sin C sin(A + α)) ).
This is well-defined since sin C > 0 and sin(A + α) > 0 (Lemma 1.3). Set the unit vectors
  u₁ := e^{i(B−α)}, u₂ := e^{iB}, v₁ := e^{i(π−C+α)} = (−cos(C−α), sin(C−α)), v₂ := e^{i(π−C)} = (−cos C, sin C),
so that (Lemma 2 and §0): K = (c/2)(cos α − τ sin α)u₁, A = c·u₂, L = C + (b/2)(cos α − σ sin α)v₁, A − C = b·v₂.

**Lemma 4.** The point T satisfies:
  (i) T·u₁ = d₁ := (c/2) cos α + (c/4)·sin A / sin(A+α);
  (ii) T·u₂ = d₂ := c/2 + (c/4)·sin A sin(C−α) / (sin C sin(A+α));
  (iii) (T − C)·v₁ = d₁′ := (b/2) cos α + (b/4)·sin A / sin(A+α);
  (iv) (T − C)·v₂ = d₂′ := b/2 + (b/4)·sin A sin(B−α) / (sin B sin(A+α)).

*Proof.* Throughout we use the Law of Sines in ABC in the form a sin C = c sin A, b sin C = c sin B, a sin B = b sin A, and sin(A + B) = sin(π − C) = sin C, cos(B + C) = cos(π − A) = −cos A, and the addition formulas.

**(i).** T·u₁ = T_x cos(B−α) + T_y sin(B−α). The two "c/2-terms" combine by the cosine subtraction formula:
  (c/2)[cos B cos(B−α) + sin B sin(B−α)] = (c/2) cos(B − (B−α)) = (c/2) cos α.
The remaining terms are
  (a/4) cos(B−α) + (c/4)·sin(B−α) sin A cos(A+α)/(sin C sin(A+α)).
Multiply this quantity by 4 sin C sin(A+α)/c > 0 and use a sin C = c sin A:
  sin A cos(B−α) sin(A+α) + sin A sin(B−α) cos(A+α) = sin A·sin((A+α) + (B−α)) = sin A sin(A+B) = sin A sin C,
by the sine addition formula. Dividing back by 4 sin C sin(A+α)/c, the remaining terms equal (c/4) sin A / sin(A+α). Adding the (c/2)cos α part gives T·u₁ = d₁.

**(ii).** T·u₂ = T_x cos B + T_y sin B. The c/2-terms give (c/2)(cos²B + sin²B) = c/2. The remaining terms are
  (a/4) cos B + (c/4)·sin B sin A cos(A+α)/(sin C sin(A+α)).
Multiply by 4 sin C sin(A+α)/c and use a sin C = c sin A:
  sin A cos B sin(A+α) + sin A sin B cos(A+α) = sin A sin(A + α + B) = sin A sin(π − C + α) = sin A sin(C − α),
since sin(π − x) = sin x with x = C − α. Dividing back, the remaining terms equal (c/4) sin A sin(C−α)/(sin C sin(A+α)), so T·u₂ = d₂.

**(iii).** T − C = ( (c cos B)/2 − 3a/4 , T_y ). Then
  (T−C)·v₁ = −cos(C−α)[(c cos B)/2 − 3a/4] + sin(C−α)·T_y
  = (c/2)[−cos B cos(C−α) + sin B sin(C−α)] + (3a/4) cos(C−α) + (c/4)·sin(C−α) sin A cos(A+α)/(sin C sin(A+α)).
The first bracket is −cos(B + C − α) = −cos(π − A − α) = cos(A + α). So
  (T−C)·v₁ = (c/2) cos(A+α) + (3a/4) cos(C−α) + (c/4)·sin(C−α) sin A cos(A+α)/(sin C sin(A+α)).
We must show this equals d₁′ = (b/2) cos α + (b/4) sin A/sin(A+α). Multiply both sides by 4 sin C sin(A+α)/c > 0, using a sin C = c sin A and b sin C = c sin B; the claim becomes the identity
  (I₃) 2 sin C cos(A+α) sin(A+α) + 3 sin A cos(C−α) sin(A+α) + sin(C−α) sin A cos(A+α) = 2 sin B cos α sin(A+α) + sin B sin A.
*Proof of (I₃).* Left side. First term: 2 cos(A+α) sin(A+α) = sin(2A+2α) (PS2 with X = Y = A+α), so it is sin C sin(2A+2α) = ½[cos(2A+2α−C) − cos(2A+2α+C)] by (PS1). For the second and third terms, factor sin A and expand by (PS2):
  2 cos(C−α) sin(A+α) = sin(A+C) + sin(A+2α−C), hence 3 cos(C−α) sin(A+α) = (3/2)[sin(A+C) + sin(A+2α−C)];
  2 sin(C−α) cos(A+α) = sin(A+C) − sin(A+2α−C), hence sin(C−α) cos(A+α) = ½[sin(A+C) − sin(A+2α−C)].
Their sum is 2 sin(A+C) + sin(A+2α−C), so the second-plus-third terms equal
  2 sin A sin(A+C) + sin A sin(A+2α−C) = [cos C − cos(2A+C)] + ½[cos(2α−C) − cos(2A+2α−C)]
by (PS1) twice. Altogether the left side is
  ½cos(2A+2α−C) − ½cos(2A+2α+C) + cos C − cos(2A+C) + ½cos(C−2α) − ½cos(2A+2α−C)
  = −½cos(2A+2α+C) + cos C − cos(2A+C) + ½cos(C−2α),
using cos(2α−C) = cos(C−2α).
Right side. sin B = sin(A+C). By (PS2), 2 cos α sin(A+α) = sin(A+2α) + sin A, so
  2 sin B cos α sin(A+α) = sin(A+C)[sin(A+2α) + sin A] = ½[cos(C−2α) − cos(2A+2α+C)] + ½[cos C − cos(2A+C)]
by (PS1) twice, and sin B sin A = sin(A+C) sin A = ½[cos C − cos(2A+C)]. Summing:
  right side = ½cos(C−2α) − ½cos(2A+2α+C) + cos C − cos(2A+C),
which matches the left side. This proves (I₃), hence (iii).

**(iv).** Similarly,
  (T−C)·v₂ = −cos C[(c cos B)/2 − 3a/4] + sin C·T_y
  = (c/2)[−cos B cos C + sin B sin C] + (3a/4) cos C + (c/4)·sin A cos(A+α)/sin(A+α)
  = (c/2) cos A + (3a/4) cos C + (c/4)·sin A cos(A+α)/sin(A+α),
since −cos B cos C + sin B sin C = −cos(B+C) = cos A, and the sin C in T_y's second term cancelled against the sin C denominator. We must show this equals d₂′ = b/2 + (b/4) sin A sin(B−α)/(sin B sin(A+α)). Multiply both sides by 4 sin C sin(A+α)/c, using a sin C = c sin A and b sin C = c sin B; the claim becomes
  (I₄) 2 sin C cos A sin(A+α) + 3 sin A cos C sin(A+α) + sin C sin A cos(A+α) = 2 sin B sin(A+α) + sin A sin(B−α).
[On the right: (b/2)·(4 sin C sin(A+α)/c) = 2 sin B sin(A+α), and (b/4)(sin A sin(B−α)/(sin B sin(A+α)))·(4 sin C sin(A+α)/c) = sin A sin(B−α).]
*Proof of (I₄).* Left side. Group the first and third terms as sin C·[2 cos A sin(A+α) + sin A cos(A+α)]. By (PS2), 2 cos A sin(A+α) = sin(2A+α) + sin α and 2 sin A cos(A+α) = sin(2A+α) − sin α, so
  2 cos A sin(A+α) + sin A cos(A+α) = sin(2A+α) + sin α + ½ sin(2A+α) − ½ sin α = (3/2) sin(2A+α) + ½ sin α.
Also, by (PS1), 2 sin A sin(A+α) = cos α − cos(2A+α), so the middle term is
  3 sin A cos C sin(A+α) = (3/2) cos C [cos α − cos(2A+α)].
Hence, expanding everything by (PS1) and (PS3):
  (3/2) sin C sin(2A+α) = (3/4)[cos(2A+α−C) − cos(2A+α+C)];
  ½ sin C sin α = ¼[cos(C−α) − cos(C+α)];
  (3/2) cos C cos α = (3/4)[cos(C−α) + cos(C+α)];
  −(3/2) cos C cos(2A+α) = −(3/4)[cos(2A+α−C) + cos(2A+α+C)].
Summing, the cos(2A+α−C) terms cancel (¾ − ¾), and
  left side = −(3/2) cos(2A+α+C) + (¼ + ¾) cos(C−α) + (−¼ + ¾) cos(C+α) = cos(C−α) + ½cos(C+α) − (3/2) cos(2A+α+C).
Right side. sin B = sin(A+C) and sin(B−α) = sin(π − A − C − α) = sin(A+C+α). By (PS1):
  2 sin(A+C) sin(A+α) = cos(C−α) − cos(2A+C+α), sin A sin(A+C+α) = ½[cos(C+α) − cos(2A+C+α)].
Summing: right side = cos(C−α) + ½cos(C+α) − (3/2)cos(2A+C+α), matching the left side. This proves (I₄), hence (iv). ∎

### 5. Fixed Point Lemma: TA = TK and TA = TL

**Lemma 5a (perpendicular-bisector criterion and coefficients).** Let X, Z be points and w a unit vector; let s := |Z − X| > 0, and with our fixed α set ρ₀ := (s/2) cos α, ρ₁ := −(s/2) sin α. For t ∈ ℝ define Y(t) := X + (ρ₀ + ρ₁ t)·w and, for a point x,
  F(x; t) := (x − X)·(Z − Y(t)) − ( |Z − X|² − |Y(t) − X|² )/2.
Then:
(a) |x − Z| = |x − Y(t)| if and only if F(x; t) = 0.
(b) As a polynomial in t,
  F(x; t) = (ρ₁²/2)·t² + f₁(x)·t + f₀(x),
  with f₁(x) = −ρ₁[(x−X)·w − ρ₀] and f₀(x) = (x−X)·(Z−X) − s²/2 − ρ₀·(x−X)·w + ρ₀²/2.

*Proof.* (a) Expanding |x−Z|² − |x−Y|² = 2x·(Y−Z) + |Z|² − |Y|², and |Z|² − |Y|² = (|Z−X|² + 2X·Z − |X|²) − (|Y−X|² + 2X·Y − |X|²) = |Z−X|² − |Y−X|² + 2X·(Z−Y), we get
  |x−Z|² − |x−Y|² = −2(x−X)·(Z−Y) + |Z−X|² − |Y−X|² = −2F(x; t).
So the two distances are equal iff F(x;t) = 0 (distances are nonnegative, so equality of squares is equivalent).
(b) Z − Y(t) = (Z−X) − (ρ₀ + ρ₁ t)w and |Y(t) − X|² = (ρ₀ + ρ₁ t)² since w is a unit vector. Hence
  F(x;t) = (x−X)·(Z−X) − (ρ₀+ρ₁t)·(x−X)·w − s²/2 + (ρ₀+ρ₁t)²/2.
Collecting powers of t: the t²-coefficient is ρ₁²/2; the t-coefficient is −ρ₁(x−X)·w + ρ₀ρ₁ = −ρ₁[(x−X)·w − ρ₀]; the constant term is as displayed. ∎

**Identity (⋆).** For every θ:
  cos²α sin θ sin(A+α) + cos α sin A sin θ − sin α cos α cos(A+α) sin θ − 2 sin A cos θ sin α = 2 sin A sin(θ − α).
*Proof.* The first and third terms combine:
  cos α sin θ [cos α sin(A+α) − sin α cos(A+α)] = cos α sin θ sin((A+α) − α) = cos α sin θ sin A,
by the sine subtraction formula. Adding the second term gives 2 sin A sin θ cos α, and then
  2 sin A sin θ cos α − 2 sin A cos θ sin α = 2 sin A (sin θ cos α − cos θ sin α) = 2 sin A sin(θ − α). ∎

**Lemma 5 (Fixed Point Lemma).** TA = TK and TA = TL.

*Proof.* **K-side.** Apply Lemma 5a with X = B = (0,0), Z = A, w = u₁, s = |A − B| = c. Then Y(t) = (c/2)(cos α − t sin α)u₁, and by Lemma 2, K = Y(τ). Also Z − X = A = c·u₂. Define
  m := c² sin α / (8 sin C sin(A+α)) > 0.
We claim the polynomial identity in t:
  (♣) F(T; t) = m·q_K(t).
Both sides are quadratic in t; we match the three coefficients, using Lemma 4 (i), (ii) for the values (T−X)·w = T·u₁ = d₁ and (T−X)·(Z−X) = c·(T·u₂) = c·d₂.

- *t² coefficient.* Left: ρ₁²/2 = c² sin²α/8. Right: m·(P(C) − R(C)) = [c² sin α/(8 sin C sin(A+α))]·sin C sin α sin(A+α) = c² sin²α/8, by (†). Equal.
- *t coefficient.* Left: f₁(T) = −ρ₁[d₁ − ρ₀] = (c/2) sin α·[d₁ − (c/2)cos α] = (c/2) sin α·(c/4) sin A/sin(A+α) = c² sin α sin A/(8 sin(A+α)). Right: m·2Q(C) = m·sin A sin C = c² sin α sin A/(8 sin(A+α)). Equal.
- *constant coefficient.* Left:
  f₀(T) = c·d₂ − c²/2 − ρ₀·d₁ + ρ₀²/2
  = [c²/2 + (c²/4) sin A sin(C−α)/(sin C sin(A+α))] − c²/2 − (c/2)cos α·[(c/2)cos α + (c/4) sin A/sin(A+α)] + (c²/8)cos²α
  = (c²/4)·sin A sin(C−α)/(sin C sin(A+α)) − (c²/8)cos²α − (c²/8)·cos α sin A/sin(A+α).
  Over the common denominator 8 sin C sin(A+α):
  f₀(T) = c²·[ 2 sin A sin(C−α) − cos²α sin C sin(A+α) − cos α sin A sin C ] / (8 sin C sin(A+α)).
  Right: −m·(P(C)+R(C)) = −c² sin α·[2 sin A cos C + sin C cos α cos(A+α)]/(8 sin C sin(A+α)) by Lemma 3a. Equality of the two numerators is exactly
  2 sin A sin(C−α) − cos²α sin C sin(A+α) − cos α sin A sin C = −2 sin A cos C sin α − sin C sin α cos α cos(A+α),
  i.e., after moving all terms to the right-hand arrangement,
  cos²α sin C sin(A+α) + cos α sin A sin C − sin α cos α cos(A+α) sin C − 2 sin A cos C sin α = 2 sin A sin(C−α),
  which is Identity (⋆) with θ = C. Equal.

So (♣) holds. Evaluating at t = τ and using q_K(τ) = 0 (Lemma 3): F(T; τ) = 0, hence |T − A| = |T − K| by Lemma 5a(a).

**L-side.** Apply Lemma 5a with X = C, Z = A, w = v₁, s = |A − C| = b. Then Y(t) = C + (b/2)(cos α − t sin α)v₁, and by Lemma 2, L = Y(σ). Also Z − X = A − C = b·v₂. Define
  m′ := b² sin α / (8 sin B sin(A+α)) > 0.
We claim F(T; t) = m′·q_L(t) identically in t, now using Lemma 4 (iii), (iv) for (T−X)·w = (T−C)·v₁ = d₁′ and (T−X)·(Z−X) = b·(T−C)·v₂ = b·d₂′. The three coefficient checks are word-for-word those of the K-side with (c, C, d₁, d₂, m) replaced by (b, B, d₁′, d₂′, m′); we display them:

- *t².* Left: ρ₁²/2 = b² sin²α/8. Right: m′(P(B) − R(B)) = [b² sin α/(8 sin B sin(A+α))]·sin B sin α sin(A+α) = b² sin²α/8, by (†). Equal.
- *t.* Left: f₁(T) = (b/2) sin α·[d₁′ − (b/2)cos α] = (b/2) sin α·(b/4) sin A/sin(A+α) = b² sin α sin A/(8 sin(A+α)). Right: m′·2Q(B) = m′ sin A sin B = b² sin α sin A/(8 sin(A+α)). Equal.
- *constant.* Left:
  f₀(T) = b·d₂′ − b²/2 − (b/2)cos α·d₁′ + (b²/8)cos²α = (b²/4)·sin A sin(B−α)/(sin B sin(A+α)) − (b²/8)cos²α − (b²/8)·cos α sin A/sin(A+α)
  = b²·[2 sin A sin(B−α) − cos²α sin B sin(A+α) − cos α sin A sin B]/(8 sin B sin(A+α)).
  Right: −m′(P(B)+R(B)) = −b² sin α[2 sin A cos B + sin B cos α cos(A+α)]/(8 sin B sin(A+α)).
  Equality of numerators is Identity (⋆) with θ = B. Equal.

Evaluating at t = σ and using q_L(σ) = 0 (Lemma 3): F(T; σ) = 0, hence |T − A| = |T − L|. ∎

### 6. Conclusion: O = T and OM = ON

**Nondegeneracies.**
- A ≠ K and A ≠ L: K, L are inside triangle ABC (Lemma 1.1), and interior points are distinct from vertices (§0).
- K ≠ L: K lies on the ray from B with direction angle B − α, and K ≠ B (K is not a vertex); L lies on the ray from B with direction angle B − α − β, and L ≠ B. These two direction angles both lie in (0, B) ⊂ (0, π) and differ by β > 0 (Lemma 1), so they are distinct as directions: if K = L, the vector K − B ≠ 0 would be a positive multiple of both e^{i(B−α)} and e^{i(B−α−β)}, forcing e^{i(B−α)} = e^{i(B−α−β)}, i.e. β ∈ 2πℤ, contradicting 0 < β < B < π. Hence K ≠ L.
- The perpendicular bisectors ℓ_{AK} of segment AK and ℓ_{AL} of segment AL are therefore well-defined lines, and ℓ_{AK} ≠ ℓ_{AL}: if they were the same line ℓ, then the reflection across ℓ would map A to K (ℓ is the perpendicular bisector of AK) and also A to L (ℓ is the perpendicular bisector of AL); since a reflection is a map, K = L — contradiction.

**O = T.** By Lemma 5, T ∈ ℓ_{AK} (as TA = TK, A ≠ K) and T ∈ ℓ_{AL}. The circumcentre O of triangle AKL satisfies OA = OK and OA = OL, so also O ∈ ℓ_{AK} ∩ ℓ_{AL}. If O ≠ T, then the two distinct points O and T would both lie on each of the lines ℓ_{AK} and ℓ_{AL}; but two distinct points lie on a unique line, so ℓ_{AK} = ℓ_{AL} — contradicting the previous paragraph. Hence
  O = T.

**OM = ON.** We have M = (A + B)/2 = ((c cos B)/2, (c sin B)/2) and N = (A + C)/2 = ((c cos B + a)/2, (c sin B)/2). In particular M and N have the same ordinate M_y = N_y = (c sin B)/2, and
  O_x = T_x = (c cos B)/2 + a/4, so O_x − M_x = a/4 and O_x − N_x = (c cos B)/2 + a/4 − (c cos B)/2 − a/2 = −a/4.
Therefore
  OM² = (O_x − M_x)² + (O_y − M_y)² = (a/4)² + (O_y − M_y)² = (−a/4)² + (O_y − N_y)² = ON²,
and OM = ON. ∎

### Remarks (not part of the proof)
- The point T = O admits the symmetric description T = ((2A_x + B_x + C_x)/4, ·): indeed (2A_x + B_x + C_x)/4 = (2c cos B + a)/4 = (c cos B)/2 + a/4 = T_x by the projection formula (Proj); i.e., O lies on the perpendicular bisector of MN, which is the geometric content of OM = ON.
- The B↔C symmetry of T is visible in its coordinates: T_x = (2A_x+B_x+C_x)/4 is symmetric, and T_y = A_y/2 + (ϱ/2)·sin A cos(A+α)/sin(A+α) with ϱ := c/(2 sin C) = b/(2 sin B) the circumradius of ABC — both symmetric under swapping (B, b) ↔ (C, c). This is why one fixed point serves both sides.
- All displayed formulas were re-verified numerically during the build (5 triangles × several α; errors ≤ 5·10⁻¹⁵), including at a spurious root pair of (q_K, q_L), where F(T;·) ≡ m·q_K(·) continues to hold — the proof never selects roots.

## Promotable lemmas
- **Sector & Bookkeeping Lemma** (Lemmas 0–1 above): interiority of K, L in ABC; exact direction angles of rays BK, BL, CK, CL; positivity α, β, γ > 0 and bounds α+β < B, α+γ < C. Proved in full in §1. Proposed as `lemmas/setup-bookkeeping.md`.
- **Parametrization Lemma** (Lemma 2): K = (c/2)(cos α − τ sin α)e^{i(B−α)}, τ = cot(α+γ); L = C + (b/2)(cos α − σ sin α)e^{i(π−C+α)}, σ = cot(α+β). Proved in full in §2. Proposed as `lemmas/parametrization.md`.
- **Constraint Lemma** (Lemmas 3a, 3b, 3): q_K(τ) = 0 and q_L(σ) = 0 with the explicit coefficients P(θ) ± R(θ), Q(θ); includes the reusable trig-to-quadratic conversion (Lemma 3b). Proved in full in §3. Proposed as `lemmas/constraint-quadratics.md`.
