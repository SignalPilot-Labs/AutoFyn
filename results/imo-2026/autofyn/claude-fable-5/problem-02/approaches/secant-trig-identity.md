# Approach: secant-trig-identity

## Status
solved

## Approaches tried
- (round 1, outline) Verified reduction chain OM = ON ⟺ linear condition on the circumcentre; trig system E1–E6; tangent–chord parametrization — all numerically exact. Left one load-bearing gap (the elimination identity).
- (round 1, build) Closed the gap completely. Replaced the tangent–chord/power step by a branch-free linear-algebra formulation (chord equations `X cosθ + Y sinθ = chord length` for the circle through the origin), eliminated the auxiliary angles χ, ψ by a 2×2 homogeneous-system determinant, and reduced the whole problem to one four-variable trigonometric identity (KI). Proved KI rigorously by an interpolation argument: both sides are trig polynomials in s with frequencies in {±1, ±3}; equality is checked at the four points s ∈ {t, 0, φ, μ−φ} by short product-to-sum computations, and a cubic polynomial vanishing at four distinct points is zero. Every displayed equation was independently machine-checked (`/tmp/round-1/scratch/builder_endtoend.py`, 33 checks × 3 configurations, plus exact sympy verification of KI in `builder_identity4.py`); the written proof below stands on its own. — **worked**.
- Refuted shortcuts (do not retry): △LBK ~ △LNC ratio similarity; identifying the second intersections P, Q of AB, AC with ⊙(AKL) as named points; P ∈ ⊙(BMK); the identity does NOT hold as an unconditional identity in (φ,A,α,β) — it holds exactly modulo the two constraints (K), (L), with the discrepancy factoring as sin(α−β)[N(s)N(t) − sin²s sin²t] (this factorization is the key discovery of the build).

## Current best
Complete proof below. No gaps.

## Full proof

**Problem.** Let ABC be a triangle, M and N the midpoints of AB and AC. Points K and L
are chosen inside triangles BMC and BNC respectively, such that K lies inside angle LBA,
L lies inside angle ACK, and ∠KBA = ∠ACL, ∠LBK = ∠LNC, ∠LCK = ∠BMK. Let O be the
circumcentre of triangle AKL. Prove that OM = ON.

Throughout, all angles are ordinary (unsigned) angles in (0, π); b := CA, c := AB;
A also denotes the angle ∠BAC ∈ (0, π). We write

φ := ∠KBA = ∠ACL,  χ := ∠LCK = ∠BMK,  ψ := ∠LBK = ∠LNC.

Since O is defined as the circumcentre of **triangle** AKL, the points A, K, L are not
collinear; we use this once (Step 5).

All named tools are elementary: the Law of Sines, the product-to-sum formulas
2 sin X sin Y = cos(X−Y) − cos(X+Y) and sin X cos Y = ½[sin(X+Y) + sin(X−Y)], the
addition formulas, and the fact that a polynomial of degree ≤ 3 with four distinct
roots is identically zero (Factor Theorem). (These are all standard; the knowledge
base's "Law of Sines"/"trig identities" entries apply.)

---

### Step 0. Coordinates, position of K and L, and angle bookkeeping

Place A at the origin, B = (c, 0), and C = (b cos A, b sin A), with sin A > 0.
For θ ∈ ℝ write u(θ) := (cos θ, sin θ), so ray AB = {ρ u(0) : ρ ≥ 0} and
ray AC = {ρ u(A) : ρ ≥ 0}. M = B/2 = (c/2, 0), N = C/2.

**Lemma 0.1 (open sector at A).** The interior of the angle BAC — that is, the
intersection of the open half-plane bounded by line AB containing C with the open
half-plane bounded by line AC containing B — equals
S := { ρ u(θ) : ρ > 0, 0 < θ < A }. Moreover for P = ρ u(θ) ∈ S one has
∠BAP = θ and ∠PAC = A − θ, hence ∠BAP + ∠PAC = A.

*Proof.* Line AB is the x-axis and C has y-coordinate b sin A > 0, so the first
half-plane is {y > 0}. Line AC has direction u(A); the vector n := (sin A, −cos A) is
normal to it, and ⟨n, B⟩ = c sin A > 0, so the second half-plane is
{x sin A − y cos A > 0}. For P = ρ u(θ) (ρ > 0, θ taken in (−π, π]):
y > 0 ⟺ sin θ > 0 ⟺ θ ∈ (0, π); and x sin A − y cos A = ρ sin(A − θ), with
A − θ ∈ (A − π, A) ⊆ (−π, π), so it is positive iff A − θ ∈ (0, π) iff θ < A.
Thus P ∈ S ⟺ θ ∈ (0, A). Finally ∠BAP is the angle between the unit vectors u(0)
and u(θ): cos ∠BAP = cos θ with both angles in [0, π], so ∠BAP = θ; likewise
cos ∠PAC = ⟨u(θ), u(A)⟩ = cos(A − θ) gives ∠PAC = A − θ. ∎

**Lemma 0.2 (interiority).** int(△BMC) ⊆ int(△ABC), and int(△BNC) ⊆ int(△ABC).

*Proof.* Since M lies on segment AB, the vertices B, M, C lie in the closed triangle
ABC, so △BMC ⊆ △ABC by convexity. Suppose a point P ∈ int(△BMC) lay on ∂(△ABC).
∂(△ABC) consists of the segments AB, BC, CA. (a) If P ∈ AB: let ℓ be an affine
functional vanishing on line AB with ℓ(C) ≠ 0. Writing P = λB + νM + γC with
λ, ν, γ ≥ 0, λ+ν+γ = 1, we get 0 = ℓ(P) = γ ℓ(C), so γ = 0 and P ∈ segment BM ⊆
∂(△BMC), contradicting P ∈ int(△BMC). (b) If P ∈ BC: BC is a side of △BMC, so
P ∈ ∂(△BMC), contradiction. (c) If P ∈ CA: let ℓ′ vanish on line CA; ℓ′(B) ≠ 0, and
ℓ′(M) = ½(ℓ′(A) + ℓ′(B)) = ½ℓ′(B) ≠ 0 with the same sign. Then
0 = ℓ′(P) = λℓ′(B) + νℓ′(M) forces λ = ν = 0, so P = C ∈ ∂(△BMC), contradiction.
Hence int(△BMC) ∩ ∂(△ABC) = ∅, and since int(△BMC) ⊆ △ABC we conclude
int(△BMC) ⊆ int(△ABC). The proof for △BNC is identical with the roles of the sides
AB and AC exchanged. ∎

By hypothesis K ∈ int(△BMC) and L ∈ int(△BNC), so by Lemma 0.2 both lie in
int(△ABC), which is contained in the open sector S of Lemma 0.1 (the interior of a
triangle is contained in the interior of each of its vertex angles, being the
intersection of three of the relevant open half-planes). Therefore, by Lemma 0.1:

- K = AK · u(α) with AK := |AK| > 0 and α := ∠BAK ∈ (0, A), and ∠KAC = A − α;
- L = AL · u(A − β) with AL := |AL| > 0 and β := ∠CAL ∈ (0, A), and ∠LAB = A − β.

Also K, L lie on none of the lines AB, AC, BC (interior points of △ABC), so all the
triangles used below (ABK, MBK, ACK, ACL, NCL, ABL) are nondegenerate.

**Lemma 0.3 (angle addition).** If a ray r from a vertex Q lies in the interior of an
angle ∠PQS ∈ (0, π), then ∠PQS = ∠PQr + ∠rQS.

*Proof.* Identical computation to Lemma 0.1 after an isometry taking Q to the origin
and ray QP to {ρ u(0)}: the interior of the angle is {ρ u(θ) : ρ > 0, 0 < θ < γ}
where γ = ∠PQS, and a ray u(θ₀) with θ₀ ∈ (0, γ) satisfies ∠PQr = θ₀ and
∠rQS = γ − θ₀, which sum to γ. ∎

**Consequences of the hypotheses (all interiority is consumed here).**

(a) *Rays through midpoints.* M is the midpoint of AB, so M lies strictly between B
and A; hence ray BM = ray BA and **∠KBM = ∠KBA = φ**. Likewise ray CN = ray CA and
**∠LCN = ∠LCA = φ**.

(b) *Angle splitting at C.* K ∈ int(△ABC) is not on line CA, so ∠ACK ∈ (0, π) is a
genuine angle; L lies inside angle ACK (hypothesis), so by Lemma 0.3
**∠ACK = ∠ACL + ∠LCK = φ + χ**.

(c) *Angle splitting at B.* Similarly, K lies inside angle LBA, so
**∠ABL = ∠LBK + ∠KBA = ψ + φ**.

(d) *Angle ranges.* In triangle ABK the angles are α (at A), φ (at B), π − α − φ
(at K); all lie in (0, π), so **0 < φ + α < π**. In triangle MBK the angles are
χ (at M), φ (at B, by (a)), π − φ − χ (at K), so **0 < φ + χ < π**. Symmetrically
(triangles ACL and NCL): **0 < φ + β < π** and **0 < φ + ψ < π**. In particular all
of sin(φ+α), sin(φ+β), sin(φ+χ), sin(φ+ψ), sin φ, sin α, sin β are > 0.

---

### Step 1. Reduction of OM = ON to a linear condition on O

Since all quantities are nonnegative, OM = ON ⟺ OM² = ON². With A at the origin:

OM² = |O − B/2|² = |O|² − ⟨O, B⟩ + |B|²/4,  ON² = |O|² − ⟨O, C⟩ + |C|²/4.

Hence

**OM = ON ⟺ ⟨O, B − C⟩ = (|B|² − |C|²)/4 = (c² − b²)/4.**  (1)

Write (X, Y) := 2O. Since B − C = (c − b cos A, −b sin A), condition (1) reads

**(c − b cos A)·X − b sin A·Y = (c² − b²)/2.**  (GOAL)

---

### Step 2. Chord equations for the circumcircle

Let ω be the circumcircle of AKL, with centre O and radius R. Since A = 0 ∈ ω,
|O|² = R². For K ∈ ω: |K − O|² = R² = |O|², i.e. |K|² = 2⟨K, O⟩. With
K = AK·u(α) and AK > 0, this gives AK² = AK·(X cos α + Y sin α), hence

**X cos α + Y sin α = AK.**  (2K)

Identically, from L = AL·u(A−β) ∈ ω:

**X cos(A−β) + Y sin(A−β) = AL.**  (2L)

---

### Step 3. The Law-of-Sines system and elimination of χ, ψ

All six relations below are the Law of Sines in a nondegenerate triangle, using
sin(π − x) = sin x for the third angle, and the angle values established in Step 0.

- Triangle ABK (angles α at A, φ at B):
  **E1: AK = c sin φ / sin(φ+α)** and **BK = c sin α / sin(φ+α)**.
- Triangle MBK (angles χ at M, φ at B; BM = c/2):
  **BK = (c/2) sin χ / sin(φ+χ)**.
- Triangle ACK (angles A−α at A, φ+χ at C, by Step 0(b)):
  **E5: AK = b sin(φ+χ) / sin(φ+χ+A−α)**.
- Triangle ACL (angles β at A, φ at C):
  **E2: AL = b sin φ / sin(φ+β)** and **CL = b sin β / sin(φ+β)**.
- Triangle NCL (angles ψ at N, φ at C, by Step 0(a); CN = b/2):
  **CL = (b/2) sin ψ / sin(φ+ψ)**.
- Triangle ABL (angles A−β at A, φ+ψ at B, by Step 0(c)):
  **E6: AL = c sin(φ+ψ) / sin(φ+ψ+A−β)**.

(The sine of the angle at K in triangle ACK is sin(π−(A−α)−(φ+χ)) = sin(φ+χ+A−α),
which is > 0 since it is the sine of an angle of a triangle; similarly in ABL. The
midpoint hypothesis enters *only* through BM = c/2 and CN = b/2.)

Equating the two expressions for BK, and multiplying by 2 sin(φ+α) sin(φ+χ)/c > 0:

**E3: 2 sin α sin(φ+χ) = sin χ sin(φ+α)**,

and symmetrically for CL:

**E4: 2 sin β sin(φ+ψ) = sin ψ sin(φ+β)**.

**Elimination of χ (K-side).** Set u := φ + χ ∈ (0, π). Equating E1 and E5 and
clearing the (positive) denominators:

c sin φ · sin(u + A − α) = b sin u · sin(φ+α).

Expanding sin(u+A−α) = sin u cos(A−α) + cos u sin(A−α) and collecting:

sin u · [c sin φ cos(A−α) − b sin(φ+α)] + cos u · [c sin φ sin(A−α)] = 0.  (★1)

Rewriting E3 with χ = u − φ, i.e. sin χ = sin u cos φ − cos u sin φ:

sin u · [2 sin α − cos φ sin(φ+α)] + cos u · [sin φ sin(φ+α)] = 0.  (★2)

(★1) and (★2) form a homogeneous linear system in the vector (sin u, cos u), which is
nonzero (sin²u + cos²u = 1). Hence the determinant vanishes:

[c sin φ cos(A−α) − b sin(φ+α)]·sin φ sin(φ+α) − c sin φ sin(A−α)·[2 sin α − cos φ sin(φ+α)] = 0.

Dividing by sin φ > 0 and regrouping the two terms containing sin(φ+α) via the
addition formula sin φ cos(A−α) + cos φ sin(A−α) = sin(φ+A−α):

**(K): c · [ sin(φ+α) sin(φ+A−α) − 2 sin α sin(A−α) ] = b sin²(φ+α).**

**Elimination of ψ (L-side).** The L-side system (E2, E6, E4) is obtained from the
K-side system (E1, E5, E3) by the substitution (b, c, α, χ) → (c, b, β, ψ): indeed E2,
E6, E4 are exactly E1, E5, E3 under this substitution. Hence the same computation gives

**(L): b · [ sin(φ+β) sin(φ+A−β) − 2 sin β sin(A−β) ] = c sin²(φ+β).**

---

### Step 4. Unified notation

Set

**s := φ + α, t := φ + β, μ := 2φ + A,**
**N(w) := sin w sin(μ−w) − 2 sin(w−φ) sin(μ−φ−w).**

Then s − φ = α, μ − φ − s = A − α, μ − s = φ + A − α, and likewise with (t, β);
also μ − s − t = A − α − β. So (K) and (L) read

**(K): c·N(s) = b sin²s,  (L): b·N(t) = c sin²t,**

and multiplying them: **N(s) N(t) = sin²s sin²t.**  (3)

**Lemma 4.1 (N-form).** With σ := 2 sin φ sin(μ−φ): N(w) = σ − sin w sin(μ−w) for all w.

*Proof.* By product-to-sum, 2 sin(w−φ) sin(μ−φ−w) = cos((w−φ)−(μ−φ−w)) −
cos((w−φ)+(μ−φ−w)) = cos(2w−μ) − cos(μ−2φ), and 2 sin w sin(μ−w) = cos(2w−μ) − cos μ,
and σ = cos(μ−2φ) − cos μ. Hence
N(w) = ½[cos(2w−μ) − cos μ] − [cos(2w−μ) − cos(μ−2φ)]
      = cos(μ−2φ) − cos μ − ½[cos(2w−μ) − cos μ] = σ − sin w sin(μ−w). ∎

Two more one-line identities (product-to-sum) used in Step 6:

**Lemma 4.2 (B1).** sin φ sin(μ−φ−t) − sin(φ−t) sin(μ−φ) = sin(μ−2φ) sin t.

*Proof.* 2 sin φ sin(μ−φ−t) = cos(2φ+t−μ) − cos(μ−t) and
2 sin(φ−t) sin(μ−φ) = cos(2φ−t−μ) − cos(μ−t). Subtracting:
cos(2φ+t−μ) − cos(2φ−t−μ) = cos(t−(μ−2φ)) − cos(t+(μ−2φ)) = 2 sin t sin(μ−2φ). ∎

**Lemma 4.3 (B3).** sin(μ−φ) sin(μ−φ−t) + sin φ sin(t−φ) = sin(μ−2φ) sin(μ−t).

*Proof.* 2 sin(μ−φ) sin(μ−φ−t) = cos t − cos(2μ−2φ−t);
2 sin φ sin(t−φ) = cos(t−2φ) − cos t; summing: cos(t−2φ) − cos(2μ−2φ−t).
Also 2 sin(μ−2φ) sin(μ−t) = cos((μ−2φ)−(μ−t)) − cos(2μ−2φ−t) = cos(t−2φ) − cos(2μ−2φ−t). ∎

**Lemma 4.4.** N(t) − σ = −sin t sin(μ−t) (immediate from Lemma 4.1), and
N(φ) = N(μ−φ) = σ/2 (from Lemma 4.1, since sin φ sin(μ−φ) = σ/2), and N(0) = σ.

---

### Step 5. Reduction of (GOAL) to one identity

**Non-collinearity.** The lines AK and AL are the lines through the origin with
directions u(α) and u(A−β). Since α, β ∈ (0, A) and A ∈ (0, π), we have
A − α − β ∈ (−A, A) ⊆ (−π, π), so

Δ := cos α sin(A−β) − sin α cos(A−β) = sin(A−α−β) = 0 ⟺ α + β = A ⟺ u(α) = u(A−β),

which would put A, K, L on one line — contradicting that AKL is a triangle. Hence
**Δ = sin(A−α−β) ≠ 0**, and the system (2K), (2L) determines (X, Y):

X = [AK sin(A−β) − AL sin α]/Δ,  Y = [AL cos α − AK cos(A−β)]/Δ.

Substituting into the left side of (GOAL):

(c − b cos A) X − b sin A · Y
= { AK·[(c − b cos A) sin(A−β) + b sin A cos(A−β)] − AL·[(c − b cos A) sin α + b sin A cos α] } / Δ.

The two brackets simplify by the addition formula:

(c − b cos A) sin(A−β) + b sin A cos(A−β) = c sin(A−β) + b[sin A cos(A−β) − cos A sin(A−β)]
 = c sin(A−β) + b sin β;
(c − b cos A) sin α + b sin A cos α = c sin α + b[sin A cos α − cos A sin α] = c sin α + b sin(A−α).

Therefore, multiplying by Δ ≠ 0, (GOAL) is equivalent to

**AK·[c sin(A−β) + b sin β] − AL·[c sin α + b sin(A−α)] = ½(c² − b²)·sin(A−α−β).**  (GOAL′)

Now substitute E1: AK = c sin φ/sin s and E2: AL = b sin φ/sin t, and multiply by
2 sin s sin t > 0 (Step 0(d)). Using the unified notation of Step 4
(sin α = sin(s−φ), sin(A−α) = sin(μ−φ−s), sin β = sin(t−φ), sin(A−β) = sin(μ−φ−t),
sin(A−α−β) = sin(μ−s−t)), (GOAL′) is equivalent to G = 0, where

**G := 2c sin φ sin t·[c sin(μ−φ−t) + b sin(t−φ)] − 2b sin φ sin s·[c sin(s−φ) + b sin(μ−φ−s)] − (c² − b²) sin(μ−s−t) sin s sin t.**

Collect G by the coefficients c², bc, b², and introduce

**U := sin t·[ sin(μ−s−t) sin t − 2 sin φ sin(μ−φ−s) ],**
**V := sin s·[ 2 sin φ sin(μ−φ−t) − sin(μ−s−t) sin s ],**
**W := 2 sin φ·[ sin t sin(t−φ) − sin s sin(s−φ) ]·sin s sin t.**

Then, expanding both expressions and comparing term by term:

- coefficient of c² in G: 2 sin φ sin t sin(μ−φ−t) − sin(μ−s−t) sin s sin t = (sin t/sin s)·V;
- coefficient of b² in G: −2 sin φ sin s sin(μ−φ−s) + sin(μ−s−t) sin s sin t = (sin s/sin t)·U;
- coefficient of bc in G: 2 sin φ[sin t sin(t−φ) − sin s sin(s−φ)] = W/(sin s sin t).

Hence, multiplying by sin s sin t (> 0):

**G · sin s sin t = c² sin²t · V + b² sin²s · U + bc · W.**  (4)

By the constraints (L) and (K): c² sin²t = bc·N(t) and b² sin²s = bc·N(s). So

**G · sin s sin t = bc·[ N(s)·U + N(t)·V + W ].**  (5)

Everything now rests on the following identity.

---

### Step 6. The Key Identity

**Theorem (KI).** For all real s, t, φ, μ, with N, U, V, W as defined in Steps 4–5:

**N(s)·U + N(t)·V + W = sin(s−t)·[ N(s) N(t) − sin²s sin²t ].**

Granting KI for a moment, we finish: by (3), N(s)N(t) − sin²s sin²t = 0 on our
configuration, so by (5), G·sin s sin t = bc·sin(s−t)·0 = 0; since sin s sin t > 0,
G = 0; by Step 5 this is (GOAL′), hence (GOAL), hence OM = ON by Step 1. ∎ (mod KI)

**Proof of KI.** Write D(s) := [N(s)U + N(t)V + W] − sin(s−t)[N(s)N(t) − sin²s sin²t],
viewed as a function of s with parameters (t, φ, μ).

**(6a) Frequency structure.** Every sine factor above has argument of the form
εs + (terms free of s) with ε ∈ {0, ±1}. Using sin x = (e^{ix} − e^{−ix})/(2i), a
product of sines in which exactly d factors contain s (each with coefficient ±1)
expands as a finite linear combination (coefficients depending on t, φ, μ only) of
exponentials e^{iks} with k ∈ {−d, −d+2, …, d}. Now count the s-carrying factors in
each summand of D:

- N(s)·U: by Lemma 4.1, N(s) = σ − sin s sin(μ−s) has summands with d = 0 and d = 2;
  each of the two summands of U has exactly one s-factor (namely sin(μ−s−t) or
  sin(μ−φ−s)), i.e. d = 1. Products: d ∈ {1, 3}.
- N(t)·V: N(t) is s-free; V = 2 sin φ sin(μ−φ−t)·sin s − sin(μ−s−t)·sin²s has
  summands with d = 1 and d = 3.
- W: expanding the bracket, its two summands have d = 1 and d = 3.
- sin(s−t)·N(s)N(t): d = 1 (from σN(t) sin(s−t)) and d = 3 (from
  sin s sin(μ−s) N(t) sin(s−t)); sin(s−t) sin²s sin²t: d = 3.

Hence **D(s) = h₃e^{3is} + h₁e^{is} + h₋₁e^{−is} + h₋₃e^{−3is}** for some
h₃, h₁, h₋₁, h₋₃ depending only on (t, φ, μ): only odd frequencies of size ≤ 3 occur.
Equivalently, D(s) = e^{−3is}·Q(e^{2is}) where Q(x) = h₃x³ + h₁x² + h₋₁x + h₋₃ is a
polynomial of degree ≤ 3.

**(6b) Four evaluations.** We show D(s) = 0 at s ∈ {t, 0, φ, μ−φ}.

*Evaluation at s = t.* U|_{s=t} = sin t[sin(μ−2t) sin t − 2 sin φ sin(μ−φ−t)] and
V|_{s=t} = sin t[2 sin φ sin(μ−φ−t) − sin(μ−2t) sin t] = −U|_{s=t}; since N(s)|_{s=t}
= N(t), the first two terms cancel: N(t)U|_{s=t} + N(t)V|_{s=t} = 0. The bracket in W
vanishes at s = t, so W|_{s=t} = 0. On the right, sin(s−t) = 0. Hence D(t) = 0.

*Evaluation at s = 0.* sin s = 0 kills V and W. By Lemma 4.4, N(0) = σ. And
U|_{s=0} = sin t[sin(μ−t) sin t − 2 sin φ sin(μ−φ)] = sin t[sin(μ−t) sin t − σ]
= −sin t·N(t) by Lemma 4.1. So the left side is −σ sin t N(t). The right side is
sin(0−t)[N(0)N(t) − 0] = −sin t·σ·N(t). Equal; D(0) = 0.

*Evaluation at s = φ.* Here sin(s−φ) = 0 and, by Lemma 4.4, N(φ) = σ/2 = sin φ sin(μ−φ).
The pieces become:

U|_{s=φ} = sin t[sin(μ−φ−t) sin t − 2 sin φ sin(μ−2φ)],
V|_{s=φ} = sin φ[2 sin φ sin(μ−φ−t) − sin(μ−φ−t) sin φ] = sin²φ sin(μ−φ−t),
W|_{s=φ} = 2 sin φ·sin t sin(t−φ)·sin φ sin t = 2 sin²φ sin²t sin(t−φ),
RHS|_{s=φ} = sin(φ−t)[ sin φ sin(μ−φ)·N(t) − sin²φ sin²t ].

Therefore

D(φ) = sin φ sin(μ−φ)·sin t[sin(μ−φ−t) sin t − 2 sin φ sin(μ−2φ)]
     + N(t)·sin²φ sin(μ−φ−t) + 2 sin²φ sin²t sin(t−φ)
     − sin(φ−t) sin φ sin(μ−φ) N(t) + sin(φ−t) sin²φ sin²t.

Factor out sin φ and group the N(t)-terms:

D(φ)/sin φ = N(t)·[ sin φ sin(μ−φ−t) − sin(φ−t) sin(μ−φ) ]
           + sin(μ−φ) sin²t sin(μ−φ−t) − 2 sin φ sin(μ−φ) sin(μ−2φ) sin t
           + 2 sin φ sin²t sin(t−φ) + sin φ sin²t sin(φ−t).

The last two terms combine to + sin φ sin²t sin(t−φ). By Lemma 4.2 (B1) the bracket
equals sin(μ−2φ) sin t, so the first and third terms combine to

sin(μ−2φ) sin t·[ N(t) − 2 sin φ sin(μ−φ) ] = sin(μ−2φ) sin t·[N(t) − σ]
= −sin(μ−2φ) sin²t sin(μ−t)  (Lemma 4.4).

Hence

D(φ)/sin φ = sin²t·[ sin(μ−φ) sin(μ−φ−t) + sin φ sin(t−φ) − sin(μ−2φ) sin(μ−t) ] = 0

by Lemma 4.3 (B3). Since this computation is an identity of trig polynomials in
(t, φ, μ) after multiplying back by sin φ, we conclude D(φ) = 0 for **all** (t, φ, μ)
with sin φ ≠ 0, and by continuity of D in its four variables, for all (t, φ, μ).

*Evaluation at s = μ−φ.* Here sin(μ−φ−s) = 0, sin s = sin(μ−φ), sin(s−φ) = sin(μ−2φ),
sin(μ−s−t) = sin(φ−t), and N(μ−φ) = σ/2 (Lemma 4.4). The pieces become:

U|_{s=μ−φ} = sin²t sin(φ−t),
V|_{s=μ−φ} = sin(μ−φ)[ 2 sin φ sin(μ−φ−t) − sin(φ−t) sin(μ−φ) ],
W|_{s=μ−φ} = 2 sin φ[ sin t sin(t−φ) − sin(μ−φ) sin(μ−2φ) ]·sin(μ−φ) sin t,
RHS|_{s=μ−φ} = sin(μ−φ−t)[ (σ/2) N(t) − sin²(μ−φ) sin²t ].

Expanding W|_{s=μ−φ} and using σ = 2 sin φ sin(μ−φ):

W|_{s=μ−φ} = σ sin²t sin(t−φ) − σ sin(μ−φ) sin(μ−2φ) sin t.

So, using σ/2 = sin φ sin(μ−φ):

D(μ−φ) = (σ/2) sin²t sin(φ−t)
       + N(t) sin(μ−φ)[2 sin φ sin(μ−φ−t) − sin(φ−t) sin(μ−φ)]
       + σ sin²t sin(t−φ) − σ sin(μ−φ) sin(μ−2φ) sin t
       − sin(μ−φ−t) sin φ sin(μ−φ) N(t) + sin(μ−φ−t) sin²(μ−φ) sin²t.

The first and third terms combine (sin(φ−t) = −sin(t−φ)):
(σ/2) sin²t sin(φ−t) + σ sin²t sin(t−φ) = (σ/2) sin²t sin(t−φ) = sin φ sin(μ−φ) sin²t sin(t−φ).
Group the N(t)-terms:

N(t)·sin(μ−φ)·[ 2 sin φ sin(μ−φ−t) − sin(φ−t) sin(μ−φ) − sin φ sin(μ−φ−t) ]
= N(t)·sin(μ−φ)·[ sin φ sin(μ−φ−t) − sin(φ−t) sin(μ−φ) ]
= N(t)·sin(μ−φ)·sin(μ−2φ) sin t  (Lemma 4.2).

Hence, factoring out sin(μ−φ):

D(μ−φ)/sin(μ−φ) = sin(μ−2φ) sin t·[N(t) − 2 sin φ sin(μ−φ)]
                + sin²t·[ sin φ sin(t−φ) + sin(μ−φ) sin(μ−φ−t) ]
                = −sin(μ−2φ) sin²t sin(μ−t) + sin²t·sin(μ−2φ) sin(μ−t)  (Lemmas 4.4, 4.3)
                = 0.

As before, multiplying back by sin(μ−φ) and using continuity, D(μ−φ) = 0 for all
(t, φ, μ).

**(6c) Interpolation.** Fix (t, φ, μ) such that the four numbers
x₁ = e^{2it}, x₂ = 1, x₃ = e^{2iφ}, x₄ = e^{2i(μ−φ)} are pairwise distinct. By (6b),
the polynomial Q of (6a) (degree ≤ 3) vanishes at the four distinct points
x₁, x₂, x₃, x₄ (since D(s_j) = e^{−3is_j}Q(e^{2is_j}) = 0 for s_j ∈ {t, 0, φ, μ−φ}).
By the Factor Theorem, Q ≡ 0, hence D(s) = 0 for **every** s ∈ ℝ, for this (t, φ, μ).

The set of (t, φ, μ) ∈ ℝ³ for which x₁, x₂, x₃, x₄ are pairwise distinct is the
complement of the union of the six families of hyperplanes
{t ∈ πℤ}, {φ ∈ πℤ}, {μ−φ ∈ πℤ}, {t−φ ∈ πℤ}, {μ−φ−t ∈ πℤ}, {μ−2φ ∈ πℤ},
which is a dense open subset of ℝ³. Thus D(s, t, φ, μ) = 0 on a dense subset of ℝ⁴;
D is continuous on ℝ⁴; hence D ≡ 0 on ℝ⁴. This proves KI. ∎

---

### Step 7. Conclusion

On the given configuration, Steps 0–3 established the constraints (K) and (L), whence
N(s)N(t) = sin²s sin²t (equation (3)). By Step 5 and KI (Step 6),

G·sin s sin t = bc·[N(s)U + N(t)V + W] = bc·sin(s−t)·[N(s)N(t) − sin²s sin²t] = 0,

and sin s sin t > 0, so G = 0, which by Step 5 is equivalent to (GOAL′), which (using
Δ ≠ 0 and the chord equations (2K), (2L)) is equivalent to (GOAL):

⟨O, B−C⟩ = (c² − b²)/4,

which by Step 1 is equivalent to OM = ON. **∎**

---

### Remarks on rigor coverage

- *Cases.* The argument is configuration-free past Step 0: Steps 1–2 are unconditional
  algebra for any point O and any circle through A, K, L; Step 3's eliminations use
  determinants (no division by possibly-zero quantities except sin φ > 0, justified);
  KI is a global identity on ℝ⁴. The only configuration inputs are the interiority
  facts of Step 0, each proven (Lemmas 0.1–0.3 and consequences (a)–(d)), and the
  non-collinearity of A, K, L, which is part of the problem statement ("triangle AKL").
- *No unproven steps.* Every trigonometric identity invoked (Lemmas 4.1–4.4, the
  bracket simplifications in Step 5, the four evaluations in Step 6b) is proven by
  explicit product-to-sum/addition-formula computation reproduced above.
- *Machine checks (not proof steps).* Exact symbolic verification of KI:
  `/tmp/round-1/scratch/builder_identity4.py` (sympy, LHS−RHS ≡ 0); end-to-end
  numeric verification of all 33 displayed equations on 3 triangles:
  `/tmp/round-1/scratch/builder_endtoend.py`.

## Promotable lemmas

- **KI (Key Identity)** — *statement:* For all real s, t, φ, μ, with
  N(w) = sin w sin(μ−w) − 2 sin(w−φ) sin(μ−φ−w),
  U = sin t[sin(μ−s−t) sin t − 2 sin φ sin(μ−φ−s)],
  V = sin s[2 sin φ sin(μ−φ−t) − sin(μ−s−t) sin s],
  W = 2 sin φ[sin t sin(t−φ) − sin s sin(s−φ)] sin s sin t:
  N(s)U + N(t)V + W = sin(s−t)[N(s)N(t) − sin²s sin²t].
  *Proved in full* in Step 6 above (interpolation at s ∈ {t, 0, φ, μ−φ}).
  Reusable by the complex-certificate approach: it is exactly the polynomial
  certificate that approach seeks, in trig-resolved coordinates.
- **Constraint pair (K)/(L)** — *statement:* Under the problem's hypotheses, with
  s = φ+∠BAK, t = φ+∠CAL, μ = 2φ+∠A: c·N(s) = b sin²s and b·N(t) = c sin²t.
  *Proved in full* in Steps 0 & 3 above (interiority lemmas + Law of Sines +
  determinant elimination). This is the complete trig-resolved encoding of all five
  hypothesis conditions.
- **Interiority package (Lemmas 0.1–0.3)** — sector description of angle interiors,
  int(△BMC) ⊆ int(△ABC), and the angle-addition lemma; proved in Step 0; reusable by
  any approach needing the additive splittings ∠ACK = φ+χ, ∠ABL = φ+ψ.
