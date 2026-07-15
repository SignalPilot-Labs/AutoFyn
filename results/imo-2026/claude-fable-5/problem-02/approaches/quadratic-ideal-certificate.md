# Approach: quadratic-ideal-certificate

## Status
solved

## Target
The full claim of imo-2026-02: prove OM = ON for the circumcentre O of triangle AKL.

## Route (one paragraph)
Coordinates B = (0,0), C = (a,0), A = (c cos B, c sin B). The six angle hypotheses decouple into: explicit one-parameter forms K = K(τ), L = L(σ) (Lemma 2) and two *independent* quadratic constraints q_K(τ) = 0, q_L(σ) = 0 (Lemma 3). The claim OM = ON is equivalent to O_x = x₀ (the perpendicular bisector of MN is the vertical line x = x₀), which in turn is equivalent to the vanishing of an explicit affine functional F evaluated at one explicit point X on that vertical line (Step 4). Finally F(X), as a polynomial in (τ, σ), is **exhibited** as G(τ,σ)·q_K(τ) + H(τ,σ)·q_L(σ) with explicitly displayed cofactors G, H (the human-checkable ideal-membership certificate, Step 5): the whole certificate reduces to the single identity E(X̂; K̂(τ)) ≡ m₀·q₀(τ) of Lemma 5, proved by three displayed coefficient computations, applied twice (once directly, once through the reflection x ↦ a − x). Hence F(X) = 0 on the constraint set and OM = ON.

The cofactor notation is fixed as the outline-reviewer required: in the final display both cofactors are polynomials in (τ, σ) (here G happens to depend only on σ and H only on τ, each of degree 1 — consistent with the reviewer's remark that a σ-only H is impossible; ours is τ-dependent).

Key simplification found while building (replaces the raw 3×3-determinant division): the certificate point is simply
  X = M + (a/4)·(1, cot(A+α)),
and with this X both required linear conditions become two-line angle-addition computations. The 3×3 determinant Δ of the original outline equals F(X) identically (shown in Step 4, Remark), so this *is* the promised certificate Δ = G·q_K + H·q_L.

## Approaches tried
- (round 1, outline) Ideal-membership verified numerically at 40 digits and by (float-noisy) CAS division — roadmap only.
- (round 1, build) Full proof written. The brute polynomial division was replaced by a structured certificate: Δ collapses to F(x) = E_K(x)(A−L)_y − E_L(x)(A−K)_y, and the explicit point X = M + (a/4)(1, cot(A+α)) satisfies E_K(X;τ) ≡ m_K q_K(τ) and (by the reflection isometry x ↦ a−x) E_L(X;σ) ≡ m_L q_L(σ). All identities proved by hand (product-to-sum / angle addition), each displayed; independently re-verified numerically to 40 digits on 4 triangles (incl. isosceles and obtuse) and exactly in sympy (all six polynomial coefficients of the two certificate identities are identically 0). — worked; proof complete below.

## Current best
Complete proof below (Status: solved). No open gaps.

## Full proof

**Problem.** Let ABC be a triangle, M, N the midpoints of AB, AC. Points K, L are chosen inside triangles BMC, BNC respectively, such that K lies inside angle LBA, L lies inside angle ACK, and
∠KBA = ∠ACL, ∠LBK = ∠LNC, ∠LCK = ∠BMK.
Let O be the circumcentre of triangle AKL. Prove OM = ON.

Throughout, A, B, C denote both the vertices and the angle measures of triangle ABC (all in (0, π), A + B + C = π); a = BC, b = CA, c = AB; d denotes the circumdiameter, so by the **law of sines** (knowledge base: Law of Sines) a = d sin A, b = d sin B, c = d sin C. Write
α := ∠KBA = ∠ACL, β := ∠LBK = ∠LNC, γ := ∠LCK = ∠BMK
(the three hypothesis equalities are exactly the statements that these labels are well defined). "Inside" means strictly inside (interior). The problem posits the triangle AKL and its circumcentre, so A, K, L are not collinear; we use this once, in Step 4.

### Step 0. Coordinates

Place B = (0,0), C = (a, 0), and A in the open upper half-plane. Since ∠ABC = B and BA = c, and the ray BC points in direction (1,0), we get A = (c cos B, c sin B). Then
M = A/2 = ((c cos B)/2, (c sin B)/2),  N = (A + C)/2 = ((c cos B + a)/2, (c sin B)/2).

Two classical one-line identities used repeatedly (both immediate from the law of sines and sin(B+C) = sin(π − A) = sin A):
- **(Projection formula)** b cos C + c cos B = d(sin B cos C + cos B sin C) = d sin(B+C) = d sin A = a.
- **(Height identity)** b sin C = d sin B sin C = c sin B.

For a point P ≠ B in the open upper half-plane write P − B = |BP|·(cos θ, sin θ) with **direction angle** θ ∈ (0, π); similarly for rays from C. The angle between two unit vectors (cos θ₁, sin θ₁), (cos θ₂, sin θ₂) with θ₁, θ₂ ∈ (0, π) is |θ₁ − θ₂| (< π). These conventions make every angle chase below a computation with direction angles.

### Step 1. Position bookkeeping

**Lemma 1.** Under the hypotheses:
(a) α, β, γ > 0;
(b) the direction angle of ray BK is B − α, with 0 < B − α < B; the direction angle of ray CL is π − C + α, with π − C < π − C + α < π;
(c) ∠LBA = α + β < B and ∠ACK = α + γ < C; the direction angle of ray BL is B − α − β and that of ray CK is π − C + α + γ;
(d) ∠KBC = B − α > 0, ∠KCB = C − α − γ > 0, ∠LCB = C − α > 0, ∠LBC = B − α − β > 0;
(e) K lies on none of the lines AB, BC, CA; L lies on none of the lines AC, BC.

*Proof.* First, a containment. The interior of a triangle T is the intersection of the three open half-planes bounded by its side lines and containing the opposite vertices; in particular int(T) meets no line that contains a whole side of T, and more generally int(T) meets no line ℓ such that T lies in one closed half-plane of ℓ (if p ∈ int(T) ∩ ℓ, every neighbourhood of p meets the open side of ℓ not containing T, yet some neighbourhood of p lies in T — contradiction).

Triangle BMC has its vertices in the closed triangle ABC, so BMC ⊆ ABC (convexity). Line AB contains the side BM of BMC; line BC contains the side BC; and ABC (hence BMC) lies in one closed half-plane of line CA. By the previous paragraph, int(BMC) is disjoint from all three lines AB, BC, CA. A point of the closed triangle ABC lying on none of the three side lines is in int(ABC); hence
int(BMC) ⊆ int(ABC),
and int(ABC) is contained in the interior of each of the angles ∠ABC, ∠BCA, ∠BAC (the angle interior at a vertex is the intersection of two of the three defining open half-planes). The same argument gives int(BNC) ⊆ int(ABC) and int(BNC) disjoint from lines AC, BC, AB (line AC ⊇ side NC, line BC ⊇ side BC, and BNC lies in a closed half-plane of AB). This proves (e), and both K and L lie in int(ABC).

(a) K ∉ line AB gives ∠KBA > 0, i.e. α > 0 (and α = ∠ACL is the same number by hypothesis). L ∉ line AC gives ∠LNC ∈ (0, π), and K ∉ line AB gives ∠BMK ∈ (0, π); thus β = ∠LNC > 0 and γ = ∠BMK > 0.

(b) Write K − B = |BK|(cos θ_K, sin θ_K), θ_K ∈ (0, π). K is interior to angle ABC, i.e. strictly on the A-side of line BC (automatic, θ_K ∈ (0,π)) and strictly on the C-side of line BA. The cross-product test against the direction (cos B, sin B) of ray BA: for C = (a,0) we get (cos B, sin B) × (a, 0) = −a sin B < 0; for K we get |BK| sin(θ_K − B). So K on the C-side of BA means sin(θ_K − B) < 0, i.e. θ_K < B (as θ_K − B ∈ (−π, π)). Then ∠KBA = |B − θ_K| = B − θ_K = α, so θ_K = B − α ∈ (0, B). Symmetrically, write L − C = |CL|(cos θ'_L, sin θ'_L), θ'_L ∈ (0, π). Ray CA has direction (A − C)/b; by the projection and height identities A − C = (c cos B − a, c sin B) = (−b cos C, b sin C) = b(cos(π − C), sin(π − C)), so ray CA has direction angle π − C, and ray CB has direction angle π. L interior to angle ACB forces θ'_L ∈ (π − C, π) (cross-product test as before), and ∠LCA = θ'_L − (π − C) = α gives θ'_L = π − C + α.

(c) K lies inside angle LBA (hypothesis). The rays BL and BA have direction angles θ_L, B ∈ (0, π), so the interior of angle LBA consists of the rays with direction angle strictly between θ_L and B. Since θ_K = B − α < B, we must have θ_L < θ_K < B; hence
∠LBK = θ_K − θ_L, ∠KBA = B − θ_K, ∠LBA = B − θ_L = ∠LBK + ∠KBA = β + α,
and θ_L = B − α − β. Since L ∈ int(ABC) is interior to angle ABC, θ_L > 0, i.e. α + β < B. Symmetrically, L lies inside angle ACK (hypothesis), the rays CA, CK have direction angles π − C, θ'_K, and θ'_L = π − C + α lies strictly between them; since θ'_L > π − C this forces θ'_K > θ'_L, so
∠ACK = ∠ACL + ∠LCK = α + γ, θ'_K = π − C + α + γ,
and K interior to angle ACB gives θ'_K < π, i.e. α + γ < C.

(d) ∠KBC = θ_K = B − α > 0; ∠KCB = π − θ'_K = C − α − γ > 0; ∠LCB = π − θ'_L = C − α > 0; ∠LBC = θ_L = B − α − β > 0. ∎

In particular 0 < α < min(B, C), 0 < α + γ < C, 0 < α + β < B, and
**sin(A + α) > 0**, since 0 < A + α < A + C = π − B < π. Define
τ := cot(α + γ), σ := cot(α + β)
(well defined: α + γ, α + β ∈ (0, π)).

### Step 2. Parametrization Lemma

**Lemma 2.** K = K(τ) and L = L(σ), where for real t, s:
K(t) := (c/2)(cos α − t sin α)·(cos(B − α), sin(B − α)),
L(s) := (a, 0) + (b/2)(cos α − s sin α)·(−cos(C − α), sin(C − α)).

*Proof.* Consider triangle BMK (nondegenerate: K ∉ line AB = line BM, by Lemma 1(e)). Since M is on segment BA with M ≠ B, ray BM = ray BA, so the angle at B is ∠KBM = ∠KBA = α; the angle at M is ∠BMK = γ; hence the angle at K is π − α − γ (positive, as α + γ < C < π). By the **law of sines** in BMK, using BM = c/2:
BK = BM·sin(∠BMK)/sin(∠BKM) = (c/2)·sin γ / sin(α + γ).
Now sin γ = sin((α+γ) − α) = sin(α+γ) cos α − cos(α+γ) sin α, so
sin γ / sin(α+γ) = cos α − τ sin α.
Since ray BK has direction angle B − α (Lemma 1(b)), K = B + BK·(cos(B−α), sin(B−α)) = K(τ).

Symmetrically, consider triangle CNL (nondegenerate: L ∉ line AC = line CN). Ray CN = ray CA (N on segment CA, N ≠ C), so the angle at C is ∠LCN = ∠LCA = α; the angle at N is ∠CNL = ∠LNC = β; the angle at L is π − α − β > 0 (α + β < B < π). Law of sines with CN = b/2:
CL = (b/2)·sin β / sin(α + β) = (b/2)(cos α − σ sin α),
by the same expansion with β, σ in place of γ, τ. Ray CL has direction angle π − C + α (Lemma 1(b)), and (cos(π−C+α), sin(π−C+α)) = (−cos(C−α), sin(C−α)); hence L = C + CL·(−cos(C−α), sin(C−α)) = L(σ). ∎

### Step 3. Constraint Lemma (the two decoupled quadratics)

Define, with the angles of ABC and the fixed α:
P := sin A cos C + ½ sin C cos A, Q := ½ sin A sin C, R := sin A cos C + ½ sin C cos(A + 2α),
P′ := sin A cos B + ½ sin B cos A, Q′ := ½ sin A sin B, R′ := sin A cos B + ½ sin B cos(A + 2α),
q_K(t) := (P − R)t² + 2Qt − (P + R),  q_L(s) := (P′ − R′)s² + 2Q′s − (P′ + R′).

Note (difference-to-product, cos X − cos Y = 2 sin((X+Y)/2) sin((Y−X)/2)):
**P − R = ½ sin C·[cos A − cos(A+2α)] = sin C sin α sin(A + α)**, and mirror **P′ − R′ = sin B sin α sin(A + α)**; both are > 0 here.

**Lemma 3 (formal quadratic reduction).** Let A₀, θ, α₀, φ be real numbers with sin(α₀ + φ) ≠ 0, and put t := cot(α₀ + φ). If
2 sin A₀ · sin(α₀+φ) · sin(θ − α₀ − φ) = sin θ · sin φ · sin(A₀ + 2α₀ + φ),  (E)
then (P̃ − R̃)t² + 2Q̃t − (P̃ + R̃) = 0, where
P̃ = sin A₀ cos θ + ½ sin θ cos A₀, Q̃ = ½ sin A₀ sin θ, R̃ = sin A₀ cos θ + ½ sin θ cos(A₀ + 2α₀).

*Proof.* Set u := 2(α₀ + φ). Product-to-sum (2 sin X sin Y = cos(X − Y) − cos(X + Y)):
- LHS of (E): 2 sin(α₀+φ) sin(θ − α₀ − φ) = cos(u − θ) − cos θ, so LHS = sin A₀·[cos(u − θ) − cos θ].
- RHS of (E): 2 sin φ sin(A₀ + 2α₀ + φ) = cos(A₀ + 2α₀) − cos(A₀ + 2α₀ + 2φ) = cos(A₀ + 2α₀) − cos(A₀ + u), so RHS = (sin θ/2)·[cos(A₀ + 2α₀) − cos(A₀ + u)].

Since t = cot(u/2) and sin(u/2) = sin(α₀ + φ) ≠ 0, the half-angle substitution is valid:
cos u = cos²(u/2) − sin²(u/2) = (t² − 1)/(t² + 1),  sin u = 2 sin(u/2)cos(u/2) = 2t/(t² + 1)
(divide the defining identities by sin²(u/2)·(t² + 1)⁻¹; formally, cos u·(t²+1) = t² − 1 and sin u·(t²+1) = 2t follow from t = cos(u/2)/sin(u/2) and (t²+1) sin²(u/2) = 1).

Multiply (E) by (t² + 1) and expand cos(u − θ) = cos u cos θ + sin u sin θ, cos(A₀ + u) = cos A₀ cos u − sin A₀ sin u:
- (t²+1)·LHS = sin A₀·[(t² − 1)cos θ + 2t sin θ − (t² + 1)cos θ] = sin A₀·[2t sin θ − 2 cos θ].
- (t²+1)·RHS = (sin θ/2)·[(t² + 1)cos(A₀+2α₀) − (t² − 1)cos A₀ + 2t sin A₀].

So (E) is equivalent to
2 sin A₀ sin θ·t − 2 sin A₀ cos θ = (sin θ/2)(cos(A₀+2α₀) − cos A₀)·t² + sin θ sin A₀·t + (sin θ/2)(cos(A₀+2α₀) + cos A₀),
i.e. to
0 = (sin θ/2)(cos(A₀+2α₀) − cos A₀)·t² − sin A₀ sin θ·t + [2 sin A₀ cos θ + (sin θ/2)(cos A₀ + cos(A₀+2α₀))]
= −[(P̃ − R̃)t² + 2Q̃t − (P̃ + R̃)],
because P̃ − R̃ = ½ sin θ (cos A₀ − cos(A₀+2α₀)), 2Q̃ = sin A₀ sin θ, and P̃ + R̃ = 2 sin A₀ cos θ + ½ sin θ (cos A₀ + cos(A₀+2α₀)). ∎

**Corollary 3.1.** q_K(τ) = 0.

*Proof.* Consider triangle BKC (nondegenerate: K ∉ line BC by Lemma 1(e)). By Lemma 1(d) its angles at B and C are ∠KBC = B − α and ∠KCB = C − α − γ, hence its angle at K is
∠BKC = π − (B − α) − (C − α − γ) = A + 2α + γ ∈ (0, π).
Law of sines in BKC: BK = a·sin(∠KCB)/sin(∠BKC) = a·sin(C − α − γ)/sin(A + 2α + γ). Equating with BK = (c/2) sin γ / sin(α+γ) from Lemma 2's proof and cross-multiplying (all denominators are positive):
(c/2)·sin γ·sin(A + 2α + γ) = a·sin(α+γ)·sin(C − α − γ).
Substitute a = c sin A / sin C and multiply by 2 sin C / c:
sin C · sin γ · sin(A + 2α + γ) = 2 sin A · sin(α+γ) · sin(C − α − γ).
This is (E) with (A₀, θ, α₀, φ) = (A, C, α, γ), and sin(α + γ) ≠ 0; Lemma 3 gives q_K(τ) = 0. ∎

**Corollary 3.2.** q_L(σ) = 0.

*Proof.* Triangle BLC (nondegenerate: L ∉ line BC) has angles ∠LBC = B − α − β, ∠LCB = C − α (Lemma 1(d)), hence ∠BLC = A + 2α + β ∈ (0, π). Law of sines: CL = a·sin(∠LBC)/sin(∠BLC) = a·sin(B − α − β)/sin(A + 2α + β). Equating with CL = (b/2) sin β / sin(α + β) and substituting a = b sin A / sin B:
sin B · sin β · sin(A + 2α + β) = 2 sin A · sin(α+β) · sin(B − α − β).
This is (E) with (A₀, θ, α₀, φ) = (A, B, α, β); Lemma 3 gives q_L(σ) = 0. ∎

### Step 4. Reduction: OM = ON ⟺ F(X) = 0

Define x₀ := (2A_x + a)/4 = ((2c cos B + a)/4) and, for points x ∈ ℝ² (dot products in ℝ²):
E_K(x) := x·(A − K) − (|A|² − |K|²)/2,  E_L(x) := x·(A − L) − (|A|² − |L|²)/2.
Completing the square shows E_K(x) = ½(|x − K|² − |x − A|²), and likewise for E_L; in particular E_K(x) = 0 iff x is on the perpendicular bisector of AK. The circumcentre O of AKL satisfies
**E_K(O) = 0 and E_L(O) = 0.**

**(4a) OM = ON ⟺ O_x = x₀.** M and N have the same y-coordinate (c sin B)/2, so with p := M_x = (c cos B)/2 and q := N_x = (c cos B + a)/2:
|OM|² − |ON|² = (O_x − p)² − (O_x − q)² = (q − p)(2O_x − p − q) = (a/2)·(2O_x − (2c cos B + a)/2).
Since a > 0, OM = ON ⟺ O_x = (2c cos B + a)/4 = x₀. (Geometrically: MN is horizontal, so the perpendicular bisector of MN is the vertical line x = x₀.)

**(4b) The functional F.** Define
F(x) := E_K(x)·(A − L)_y − E_L(x)·(A − K)_y.
F is an affine function of x with gradient
∇F = (A − K)(A − L)_y − (A − L)(A − K)_y = (D, 0),  D := (A−K)_x(A−L)_y − (A−L)_x(A−K)_y,
(the y-component cancels identically). D is the cross product (A−K) × (A−L), and **D ≠ 0** because A, K, L are not collinear (granted: the problem posits triangle AKL and its circumcentre). Also F(O) = E_K(O)(A−L)_y − E_L(O)(A−K)_y = 0. Hence, for every x,
F(x) = F(O) + ∇F·(x − O) = D·(x_x − O_x).
Consequently, for **any** point X with X_x = x₀:
OM = ON ⟺ O_x = x₀ ⟺ F(X) = 0.

*Remark (link to the outlined determinant).* Expanding along its third row, the 3×3 consistency determinant of the outline,
Δ := det [ (A−K)_x, (A−K)_y, (|A|²−|K|²)/2 ; (A−L)_x, (A−L)_y, (|A|²−|L|²)/2 ; 1, 0, x₀ ],
equals [(A−K)_y(|A|²−|L|²)/2 − (A−L)_y(|A|²−|K|²)/2] + x₀·D = F((x₀, h)) for every h (the h-terms cancel as in ∇F above). So the certificate below is exactly the promised identity Δ = G·q_K + H·q_L.

We now fix the specific point
**X := M + (a/4)·(1, cot(A + α)) = ( (2c cos B + a)/4 , (c sin B)/2 + (a/4)·cot(A + α) )**,
well defined since sin(A + α) > 0 (Step 1). Its first coordinate is x₀ by construction.

### Step 5. The certificate

**Lemma 5 (formal certificate identity).** Let B₀, C₀, α₀ be real numbers and d₀ > 0, with sin C₀ ≠ 0 and sin(A₀ + α₀) ≠ 0, where A₀ := π − B₀ − C₀. Put a₀ := d₀ sin A₀, c₀ := d₀ sin C₀, and in ℝ²:
Â := c₀(cos B₀, sin B₀),  K̂(t) := (c₀/2)(cos α₀ − t sin α₀)·u₁,  u₁ := (cos(B₀ − α₀), sin(B₀ − α₀)),
X̂ := Â/2 + (a₀/4)·(1, cot(A₀ + α₀)),
Ê(x; p) := x·(Â − p) − (|Â|² − |p|²)/2.
Then, **identically in t ∈ ℝ**,
Ê(X̂; K̂(t)) = m₀·q₀(t),
where m₀ := c₀² sin α₀ / (8 sin C₀ sin(A₀ + α₀)) and q₀(t) := (P₀ − R₀)t² + 2Q₀t − (P₀ + R₀) with
P₀ = sin A₀ cos C₀ + ½ sin C₀ cos A₀, Q₀ = ½ sin A₀ sin C₀, R₀ = sin A₀ cos C₀ + ½ sin C₀ cos(A₀ + 2α₀).

*Proof.* Write u₂ := (cos B₀, sin B₀), ρ(t) := ρ₀ + ρ₁ t with ρ₀ := (c₀/2)cos α₀, ρ₁ := −(c₀/2) sin α₀, so K̂(t) = ρ(t)·u₁ and Â = c₀u₂. Then |Â|² = c₀², |K̂(t)|² = ρ(t)², and x·Â = c₀(x·u₂), x·K̂(t) = ρ(t)(x·u₁). Hence
Ê(X̂; K̂(t)) = c₀(X̂·u₂) − ρ(t)(X̂·u₁) − c₀²/2 + ρ(t)²/2,
a quadratic in t with coefficients
[t²]: ρ₁²/2 = c₀² sin²α₀ / 8;
[t¹]: −ρ₁(X̂·u₁) + ρ₀ρ₁ = (c₀/2) sin α₀ (X̂·u₁) − (c₀²/4) sin α₀ cos α₀;
[t⁰]: c₀(X̂·u₂) − ρ₀(X̂·u₁) − c₀²/2 + ρ₀²/2 = c₀(X̂·u₂) − (c₀/2)cos α₀ (X̂·u₁) − c₀²/2 + (c₀²/8)cos²α₀.

*Two dot products.* Since Â/2 = (c₀/2)u₂ and u₂·u₁ = cos B₀ cos(B₀−α₀) + sin B₀ sin(B₀−α₀) = cos α₀:
X̂·u₁ = (c₀/2)cos α₀ + (a₀/4)·[cos(B₀−α₀) + cot(A₀+α₀) sin(B₀−α₀)]
    = (c₀/2)cos α₀ + (a₀/4)·[sin(A₀+α₀)cos(B₀−α₀) + cos(A₀+α₀)sin(B₀−α₀)]/sin(A₀+α₀)
    = (c₀/2)cos α₀ + (a₀/4)·sin(A₀+B₀)/sin(A₀+α₀)
    **= (c₀/2)cos α₀ + (a₀/4)·sin C₀/sin(A₀+α₀)**,  (D1)
using the angle-addition formula and sin(A₀+B₀) = sin(π − C₀) = sin C₀. Likewise, |u₂|² = 1 gives
X̂·u₂ = c₀/2 + (a₀/4)·[cos B₀ + cot(A₀+α₀) sin B₀] = c₀/2 + (a₀/4)·sin(A₀+α₀+B₀)/sin(A₀+α₀)
    **= c₀/2 + (a₀/4)·sin(C₀−α₀)/sin(A₀+α₀)**,  (D2)
using sin(A₀+B₀+α₀) = sin(π − C₀ + α₀) = sin(C₀ − α₀).

*Coefficient [t²].* By the difference-to-product identity, P₀ − R₀ = ½ sin C₀[cos A₀ − cos(A₀+2α₀)] = sin C₀ sin α₀ sin(A₀+α₀), so
m₀(P₀ − R₀) = [c₀² sin α₀/(8 sin C₀ sin(A₀+α₀))]·sin C₀ sin α₀ sin(A₀+α₀) = c₀² sin²α₀/8 = ρ₁²/2. ✓

*Coefficient [t¹].* Using (D1) and a₀ sin C₀ = c₀ sin A₀ (both equal d₀ sin A₀ sin C₀):
(c₀/2) sin α₀ (X̂·u₁) − (c₀²/4) sin α₀ cos α₀ = (c₀ a₀/8)·sin α₀ sin C₀/sin(A₀+α₀) = c₀² sin A₀ sin α₀/(8 sin(A₀+α₀)),
while 2Q₀m₀ = sin A₀ sin C₀ · c₀² sin α₀/(8 sin C₀ sin(A₀+α₀)) = c₀² sin A₀ sin α₀/(8 sin(A₀+α₀)). ✓

*Coefficient [t⁰].* Substituting (D1), (D2) into the [t⁰] expression:
c₀(X̂·u₂) − (c₀/2)cos α₀(X̂·u₁) − c₀²/2 + (c₀²/8)cos²α₀
= [c₀²/2 + (a₀c₀/4)·sin(C₀−α₀)/sin(A₀+α₀)] − [(c₀²/4)cos²α₀ + (a₀c₀/8)·cos α₀ sin C₀/sin(A₀+α₀)] − c₀²/2 + (c₀²/8)cos²α₀
= (a₀c₀/4)·sin(C₀−α₀)/sin(A₀+α₀) − (c₀²/8)cos²α₀ − (a₀c₀/8)·cos α₀ sin C₀/sin(A₀+α₀).
Multiply by 8 sin C₀ sin(A₀+α₀)/c₀² and use a₀ sin C₀ = c₀ sin A₀ twice (so (a₀/c₀)·sin C₀ = sin A₀); the result is
2 sin A₀ sin(C₀−α₀) − cos²α₀ sin C₀ sin(A₀+α₀) − sin A₀ sin C₀ cos α₀.  (♣)
On the other hand, by the sum-to-product identity cos A₀ + cos(A₀+2α₀) = 2 cos(A₀+α₀) cos α₀,
P₀ + R₀ = 2 sin A₀ cos C₀ + sin C₀ cos α₀ cos(A₀+α₀),
so −(P₀+R₀)m₀, multiplied by the same factor 8 sin C₀ sin(A₀+α₀)/c₀², equals
−sin α₀·[2 sin A₀ cos C₀ + sin C₀ cos α₀ cos(A₀+α₀)].  (♠)
It remains to check (♣) = (♠), i.e. that (♣) − (♠) = 0:
(♣) − (♠) = [2 sin A₀ sin(C₀−α₀) + 2 sin A₀ cos C₀ sin α₀] − [cos²α₀ sin C₀ sin(A₀+α₀) − sin C₀ sin α₀ cos α₀ cos(A₀+α₀)] − sin A₀ sin C₀ cos α₀
= 2 sin A₀·[sin(C₀−α₀) + cos C₀ sin α₀] − sin C₀ cos α₀·[cos α₀ sin(A₀+α₀) − sin α₀ cos(A₀+α₀)] − sin A₀ sin C₀ cos α₀
= 2 sin A₀ sin C₀ cos α₀ − sin C₀ cos α₀ sin A₀ − sin A₀ sin C₀ cos α₀ = 0,
using sin(C₀−α₀) + cos C₀ sin α₀ = sin C₀ cos α₀ and cos α₀ sin(A₀+α₀) − sin α₀ cos(A₀+α₀) = sin A₀ (angle subtraction). ✓

All three coefficients of Ê(X̂; K̂(t)) − m₀q₀(t) vanish, proving the identity. ∎

**Application 5.1 (K-side).** Apply Lemma 5 with (B₀, C₀, α₀, d₀) := (B, C, α, d). Then A₀ = A, a₀ = a, c₀ = c, Â = A, K̂(t) = K(t) (the parametrization of Lemma 2), X̂ = A/2 + (a/4)(1, cot(A+α)) = X, q₀ = q_K, and m₀ = m_K := c² sin α/(8 sin C sin(A+α)). The hypotheses sin C ≠ 0, sin(A+α) ≠ 0 hold. Conclusion, identically in t:
**E(X; K(t)) := X·(A − K(t)) − (|A|² − |K(t)|²)/2 = m_K·q_K(t).**  (I-K)

**Application 5.2 (L-side, via reflection).** Apply Lemma 5 with (B₀, C₀, α₀, d₀) := (C, B, α, d) (angles B and C interchanged; note π − C − B = A and the hypotheses sin B ≠ 0, sin(A+α) ≠ 0 hold). Then a₀ = a, c₀ = d sin B = b, and:
Â* = b(cos C, sin C),  K̂*(s) = (b/2)(cos α − s sin α)(cos(C−α), sin(C−α)),
X̂* = Â*/2 + (a/4)(1, cot(A+α)),  m₀ = m_L := b² sin α/(8 sin B sin(A+α)),  q₀ = q_L.
So, identically in s: Ê*(X̂*; K̂*(s)) = m_L·q_L(s), where Ê*(x; p) = x·(Â* − p) − (|Â*|² − |p|²)/2 = ½(|x − p|² − |x − Â*|²).

Now let ψ: ℝ² → ℝ², ψ(x, y) := (a − x, y). ψ is an isometry: |ψ(p) − ψ(q)| = |(q_x − p_x, p_y − q_y)| = |p − q|. We claim
ψ(A) = Â*, ψ(L(s)) = K̂*(s) for all s, ψ(X) = X̂*.
Indeed:
- ψ(A) = (a − c cos B, c sin B) = (b cos C, b sin C) = Â*, by the projection formula (a − c cos B = b cos C) and the height identity (c sin B = b sin C).
- ψ(L(s)): L(s) = (a − (b/2)(cos α − s sin α)cos(C−α), (b/2)(cos α − s sin α)sin(C−α)), so ψ(L(s)) = ((b/2)(cos α − s sin α)cos(C−α), (b/2)(cos α − s sin α)sin(C−α)) = K̂*(s).
- ψ(X) = (a − x₀, X_y). First coordinate: a − x₀ = a − (2c cos B + a)/4 = (3a − 2c cos B)/4, while X̂*_x = (b cos C)/2 + a/4 = (a − c cos B)/2 + a/4 = (3a − 2c cos B)/4 (projection formula again). Second coordinate: X̂*_y = (b sin C)/2 + (a/4)cot(A+α) = (c sin B)/2 + (a/4)cot(A+α) = X_y (height identity). ✓

Since both E-forms are squared-distance differences and ψ is an isometry:
E(X; L(s)) := X·(A − L(s)) − (|A|² − |L(s)|²)/2 = ½(|X − L(s)|² − |X − A|²)
= ½(|ψ(X) − ψ(L(s))|² − |ψ(X) − ψ(A)|²) = Ê*(X̂*; K̂*(s)) = m_L·q_L(s).
So, identically in s:
**E(X; L(s)) = m_L·q_L(s).**  (I-L)

**The certificate, displayed.** Combining (I-K), (I-L) with the definition of F (Step 4b) applied to K = K(t), L = L(s): identically in (t, s) ∈ ℝ²,
**F(X) = E(X; K(t))·(A − L(s))_y − E(X; L(s))·(A − K(t))_y = G(t,s)·q_K(t) + H(t,s)·q_L(s),**
with the explicit cofactors (each of total degree 1, G in s only, H in t only):
**G(t, s) := m_K·(A − L(s))_y = m_K·[ c sin B − (b/2)(cos α − s sin α) sin(C − α) ],**
**H(t, s) := −m_L·(A − K(t))_y = −m_L·[ c sin B − (c/2)(cos α − t sin α) sin(B − α) ].**
(By the Remark in Step 4, the left side equals the 3×3 determinant Δ(t, s) of the original outline; this is the promised human-checkable ideal-membership certificate Δ = G·q_K + H·q_L, every ingredient displayed and every identity above verified by expansion.)

### Step 6. Conclusion

For the actual configuration, K = K(τ) and L = L(σ) (Lemma 2), and q_K(τ) = 0, q_L(σ) = 0 (Corollaries 3.1, 3.2). Evaluating the certificate at (t, s) = (τ, σ):
F(X) = G(τ,σ)·q_K(τ) + H(τ,σ)·q_L(σ) = G(τ,σ)·0 + H(τ,σ)·0 = 0.
By Step 4 (with X_x = x₀ and D ≠ 0), F(X) = D·(x₀ − O_x) = 0 forces O_x = x₀, and therefore OM = ON. ∎

### Verification notes (not part of the proof)
- Every displayed formula was re-verified numerically to 40 significant digits (mpmath, 4 triangles: generic acute, generic with C > B, isosceles B = C, obtuse A) at a root pair (τ, σ) for which **all** original hypotheses (both interiorities and all six angle conditions) were confirmed to hold — such a pair exists in each test, confirming the hypotheses are satisfiable and the bookkeeping of Lemma 1 matches the true configurations.
- The two certificate identities (I-K), (I-L) were additionally verified in exact symbolic arithmetic (sympy): all six polynomial coefficients (t⁰,t¹,t² and s⁰,s¹,s²) of E(X;K(t)) − m_K q_K(t) and E(X;L(s)) − m_L q_L(s) simplify to 0 identically in (α, B, C, d). The written proof stands independently of these checks.

## Promotable lemmas
Reusable, fully proved in this file (statement + proof locations given); candidates for `results/imo-2026-02/lemmas/` certification:
1. **Position bookkeeping (Lemma 1)** — the interiority hypotheses imply: α, β, γ > 0, ray directions BK: B−α, BL: B−α−β, CL: π−C+α, CK: π−C+α+γ, and the strict bounds α+β < B, α+γ < C. Proved in Step 1.
2. **Parametrization Lemma (Lemma 2)** — K = (c/2)(cos α − τ sin α)(cos(B−α), sin(B−α)), L = C + (b/2)(cos α − σ sin α)(−cos(C−α), sin(C−α)), τ = cot(α+γ), σ = cot(α+β). Proved in Step 2. (Shared foundation with fixed-point-t.)
3. **Constraint Lemma (Lemma 3 + Corollaries 3.1–3.2)** — the hypotheses force the decoupled quadratics q_K(τ) = 0, q_L(σ) = 0, coefficients displayed; includes the formal one-variable reduction lemma applied twice. Proved in Step 3. (Shared foundation with fixed-point-t.)
4. **Certificate identity (Lemma 5)** — for X̂ = Â/2 + (a₀/4)(1, cot(A₀+α₀)): Ê(X̂; K̂(t)) ≡ m₀ q₀(t). Proved in Step 5. In particular the point X = M + (a/4)(1, cot(A+α)) lies on the perpendicular bisectors of both AK and AL, so it **is** the circumcentre O of AKL — this closed form (equivalent to fixed-point-t's point T, now with a fully hand-proved identity and the simplification T = M + (a/4)(1, cot(A+α))) is directly importable by fixed-point-t to close its Claims A and B: Claim A is X_x = x₀ by construction, Claim B is the manifest B↔C symmetry of X_y = (c sin B)/2 + (a/4)cot(A+α) via the height identity c sin B = b sin C.
