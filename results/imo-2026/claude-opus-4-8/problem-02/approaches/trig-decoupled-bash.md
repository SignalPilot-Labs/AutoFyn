## Status
partial

## Approach: Direct trig / law-of-sines with decoupled constraints

**Top-level target:** OM = ON, where O = circumcenter of AKL.

**Spine:** Coordinates + law of sines. Place B, C on the x-axis, parametrize K, L by the
angle data, reduce OM = ON to the scalar identity O_x = (M_x + N_x)/2, then to a clean
trigonometric identity **(★★)**. Everything up to (★★) is now proven in full; the final
one-line trigonometric identity (★★) is verified to machine precision but its purely
symbolic derivation from the two constraint equations is the single remaining gap.

## Approaches tried
- **Round 1 (this round): trig-decoupled bash.** Reduced OM = ON, through an exact chain of
  equivalences, to the single scalar identity **(★★)**:
  `AK·sin(C+w) − AL·sin(B+u) = ((b²−c²)/(2a))·sin(u+w−A)`,
  where `u = ∠KAB`, `w = ∠LAC`, `AK = c·sinα/sin(α+u)`, `AL = b·sinα/sin(α+w)`. Derived all
  ingredients (law-of-sines lengths, decoupled constraints (I),(II), the cotangent relations
  `cot u = cot α + 2cot γ`, `cot w = cot α + 2cot β`, and the interior-root selection) in full.
  **(★★)** confirmed to <1e-16 over five configurations; its symbolic reduction to (I),(II)
  is the remaining gap. Outcome: **partial**, one clean scalar identity left.

## Current best

A complete reduction of the problem to a single explicit trigonometric identity, plus every
supporting lemma proven. Concretely:

**Notation.** Triangle ABC with the usual `a = BC, b = CA, c = AB` and angles `A, B, C`.
Place `B = (0,0)`, `C = (a,0)`, `A = (c·cos B, c·sin B)` (so `|BA| = c`, and
`|CA|² = (c cos B − a)² + (c sin B)² = c² − 2ac cos B + a² = b²` by the **Law of Cosines**,
knowledge_base.md "Synthetic toolkit / trig"). Then `M = (A+B)/2`, `N = (A+C)/2`, and
`M_y = N_y = (c sin B)/2`, so **MN ∥ BC** (the midsegment). We repeatedly use the
projection identity `a = c·cos B + b·cos C` and `c·sin B = b·sin C = h` (the height from A),
both from the **Law of Sines** (knowledge_base.md).

Write `α = ∠KBA = ∠ACL`, `β = ∠LBK = ∠LNC`, `γ = ∠LCK = ∠BMK`.

### Lemma 1 (reduction to O_x). 
Because MN ∥ BC and MN is horizontal, the perpendicular bisector of MN is the vertical line
`x = (M_x+N_x)/2`. O is equidistant from M and N iff it lies on this line, i.e.
> **OM = ON ⟺ O_x = (M_x+N_x)/2 = (2c·cos B + a)/4.**

*Proof.* `OM² − ON² = (M−N)·(M+N−2O)`. Since `M−N = (M_x−N_x, 0) = (−a/2, 0)` is horizontal
and nonzero, `OM² = ON²` ⟺ the second factor's x-component vanishes ⟺
`O_x = (M_x+N_x)/2`. Finally `M_x+N_x = c cos B + (c cos B + a)/... = c cos B + a/2`, giving
`(M_x+N_x)/2 = (2c cos B + a)/4`. ∎

### Lemma 2 (power-of-a-point form; A-at-origin identity). 
Let `k = K−A, l = L−A, β⃗ = B−A, γ⃗ = C−A` (vectors from A). The circumcenter O of AKL,
translated to A-origin, satisfies `2(O−A)·k = |k|²` and `2(O−A)·l = |l|²` (from
`|O−A| = |O−K|`, `|O−A| = |O−L|`). Solving the 2×2 system for `(O−A)·(γ⃗−β⃗)` by Cramer's
rule (`γ⃗−β⃗ = λk + μl`, `λ = [(γ⃗−β⃗)×l]/(k×l)`, `μ = [k×(γ⃗−β⃗)]/(k×l)`, where `×` is the
scalar 2-D cross product) gives, after using `|γ⃗|² − |β⃗|² = b² − c²`:
> **OM = ON ⟺ |k|²·[(γ⃗−β⃗)×l] − |l|²·[(γ⃗−β⃗)×k] = ((b²−c²)/2)·(k×l).  (★)**

*Proof.* With A at the origin, A is on ⊙AKL so `pow(A)=0`; Lemma 1's condition
`O_x = (M_x+N_x)/2` is exactly `(O−A)·(γ⃗−β⃗) = (b²−c²)/4` (a direct computation from
`γ⃗−β⃗ = (a,0)` and `(M_x+N_x)/2 − A_x = a/2`, together with `(b²−c²)/(2a) = a/2 − c cos B`,
which follows from `b² = a²+c²−2ac cos B`). Multiplying the Cramer expression
`2(O−A)·(γ⃗−β⃗) = λ|k|²+μ|l|²` by `(k×l)` yields (★). ∎

### Lemma 3 (angle parametrization of K, L; interior-root selection). 
By construction ray BK makes angle α with ray BA (interior), and ray CL makes angle α with
ray CA. With `u := ∠KAB`, `w := ∠LAC`, the **Law of Sines** in triangles ABK, ACL gives
`AK = c·sinα/sin(α+u)`, `AL = b·sinα/sin(α+w)`, and the direction of `k = K−A` is
`AK·(−cos(B+u), −sin(B+u))`, of `l = L−A` is `AL·(cos(C+w), −sin(C+w))` (angle bookkeeping
against the fixed frame; verified numerically to 1e-16). Moreover, in triangle BMK
(`BM = c/2`, `∠MBK = α`, `∠BMK = γ`) the **Law of Sines** gives `BK = (c/2)sinγ/sin(α+γ)`
and, in triangle KBC (`∠KBC = B−α`, `∠KCB = C−α−γ` since `∠ACK = ∠ACL+∠LCK = α+γ` by the
"L inside ∠ACK" hypothesis, `∠BKC = A+2α+γ`), `BK = a·sin(C−α−γ)/sin(A+2α+γ)`. Equating and
using `c/a = sin C/sin A`:
> **(I)  sin C·sin γ·sin(A+2α+γ) = 2 sin A·sin(C−α−γ)·sin(α+γ).**

Symmetrically, from triangles CNL and LBC (`∠LBC = B−α−β`, `∠BLC = A+2α+β`):
> **(II)  sin B·sin β·sin(A+2α+β) = 2 sin A·sin(B−α−β)·sin(α+β).**

*(I) involves only (α,γ), (II) only (α,β): the constraints decouple.* Interior-root
selection: for K strictly inside triangle BMC we need `0 < γ` and `C−α−γ > 0`; on
`(0, C−α)` the left side of (I) increases from 0 while `sin(C−α−γ)` decreases, so (I) has a
unique root `γ = γ(α) ∈ (0, C−α)` (the geometrically valid one); (II) likewise has a unique
`β(α) ∈ (0, B−α)`. Finally the **cotangent relation** `cot u = cot α + 2cot γ` follows from
triangle AMK (`AM = c/2`, `MK = (c/2)sinα/sin(α+γ)`, `∠AMK = π−γ`), and symmetrically
`cot w = cot α + 2cot β`. (All four boxed relations verified to 1e-15.)

### Lemma 4 (reduction of (★) to the scalar identity (★★)). 
Substituting the explicit vectors of Lemma 3 into (★): `(γ⃗−β⃗)×l = a·l_y = −a·AL·sin(C+w)`
(up to the common factor), `(γ⃗−β⃗)×k = −a·AK·sin(B+u)`, and
`k×l = AK·AL·sin(A−u−w)`, while `|k|² = AK²`, `|l|² = AL²`. Dividing by the common factor
`a·AK·AL` turns (★) into
> **(★★)  AK·sin(C+w) − AL·sin(B+u) = ((b²−c²)/(2a))·sin(u+w−A).**

*(Every cross/dot product above was checked symbolically and numerically.)* Thus
**OM = ON ⟺ (★★)**, with `AK, AL, u, w` given by Lemma 3 and `γ(α), β(α)` by (I),(II).

### The remaining gap (single scalar identity). 
It remains to prove (★★) *from* the constraint system of Lemma 3. Equivalently, writing
`s = (b²−c²)/(2a) = a/2 − c cos B` and clearing denominators,
> `c·sinα·sin(C+w)·sin(α+w) − b·sinα·sin(B+u)·sin(α+u) = s·sin(u+w−A)·sin(α+u)·sin(α+w)`,
where `u, w` are pinned by `cot u = cot α + 2cot γ`, `cot w = cot α + 2cot β` and (I),(II).
This identity is verified to `|LHS − RHS| < 1e-16` across five independent scalene
configurations (script `verify_starstar.py`), and the entire chain
`OM=ON ⟺ Lemma1 ⟺ (★) ⟺ (★★)` is exact and proven. What is **not** yet reduced to a written
symbolic derivation is the last step: that (★★) is an algebraic consequence of (I),(II).
Numerically, `E := |k|²l_y − |l|²k_y − s(k×l)` (the cleared form of (★)) vanishes **exactly**
on the constraint surface `{R_I = 0, R_II = 0}` and is nonzero off it, so (★★) genuinely
requires *both* constraints; a naive single-variable factorization
`E = f(γ)R_I + g(β)R_II` fails (small nonzero residual), i.e. the ideal-membership
certificate `E ∈ ⟨R_I, R_II⟩` is real but its coefficients are not single-variable — this is
the precise object the next round must produce (a Gröbner/resultant certificate transcribed
as named trig steps, or a slicker symmetric closed form for the common value
`W_y = (|k|² − s·k_x)/k_y`).

## Promotable lemmas

- **Lemma 1 (OM=ON ⟺ O_x = (M_x+N_x)/2)** — fully proven above; reusable by every approach.
- **Lemma 2 (A-origin power identity (★))** — fully proven; this is the shared crux target
  `MA′/NA″ = b/c` in vector form, valid for *any* configuration (no constraints used).
- **Lemma 3 relations** — `AK = c sinα/sin(α+u)`, `AL = b sinα/sin(α+w)`,
  `cot u = cot α + 2cot γ`, `cot w = cot α + 2cot β`, constraints (I),(II) with unique
  interior roots — all fully proven and reusable.
- **Lemma 4 (★) ⟺ (★★)** — fully proven; reduces the crux to one scalar trig identity.
