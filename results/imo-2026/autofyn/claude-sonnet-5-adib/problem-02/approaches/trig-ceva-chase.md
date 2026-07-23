## Status
partial

## Approaches tried
- **trig-ceva-chase** (new this round). Built the pure trigonometric / Law-of-Sines
  chase specified in the outline, working directly with the angles of the base
  triangle `ABC` and the free parameter `θ = ∠KBA = ∠ACL` — no Cartesian frame
  fixed for `B, C` and no complex-number frame. The concrete, mandated finding
  is reported below, honestly and in full: **this approach DOES produce
  genuinely new leverage on the existence/uniqueness part of the problem (a
  closed-form quadratic solve for `r1(θ) = BK` and `r2(θ) = CL`, replacing the
  IVT + monotonicity + domain-correction machinery that `coordinate-trig-bash`
  needed and got wrong once already), but it does NOT bypass the final
  identity (the "OM = ON" computation itself) — that step is shown to reduce
  to essentially the same underlying scalar wall as the other three live
  approaches, just reached by a different route.** Full derivation below.

## Current best

### 0. Setup and notation (no coordinate frame fixed yet)

Let `ABC` be the given triangle with the standard angle names
`α = ∠BAC, β = ∠ABC, γ = ∠BCA` and side lengths `a = BC, b = CA, c = AB`
(so `a/sinα = b/sinβ = c/sinγ = 2R_{ABC}` by the Extended Law of Sines,
knowledge_base.md "Extended Law of Sines"). Let `M, N` be the midpoints of
`AB, AC`. Following the parametrization already certified in
`lemmas/decoupling-and-sweep-lemma.md` (Lemma 3 there — imported unchanged,
only its **conclusion** is used, not its coordinate derivation): for
`θ ∈ (0, min(β,γ))`, the containment hypotheses ("K inside triangle BMC, L
inside triangle BNC, K inside angle LBA, L inside angle ACK") force `K` to
lie on the ray from `B` making angle `θ` with ray `BA` (on the side toward
the triangle's interior), at some distance `r1 = BK > 0`, and `L` to lie on
the ray from `C` making angle `θ` with ray `CA`, at some distance
`r2 = CL > 0`. (This is exactly hypothesis H1: `∠KBA = ∠ACL = θ`, now used to
fix the *directions* of the two rays; `r1, r2` are the only remaining
freedoms besides `θ`.) We work with `r1, r2, θ` and the triangle's own angle
data as the sole "coordinates," with no `(x,y)` frame chosen for `B, C, A`.

The Decoupling Lemma (certified, `lemmas/decoupling-and-sweep-lemma.md`)
shows: `F2(θ,r1) := ∠LCK − ∠BMK` depends only on `(θ,r1)`, not `r2` (H3:
`∠LCK=∠BMK` pins `r1` given `θ`); symmetrically `F1(θ,r2) := ∠LBK − ∠LNC`
depends only on `(θ,r2)` (H2 pins `r2` given `θ`). We re-derive, in closed
trig form, the solve of `F2(θ,r1)=0` for `r1` and of `F1(θ,r2)=0` for `r2`.

### 1. A general vector-algebra lemma: angle-matching on a ray is a quadratic

**Lemma T1.** Let `V0` be a point, `u` a fixed unit vector, and
`P(r) := V0 + r·u` (`r` ranging over an interval of `ℝ`, e.g. `r>0`) a point
tracing a fixed ray from `V0`. Let `V1 ≠ V0`, `w1` a fixed nonzero vector
("the other side of the angle at `V1`"), and likewise `V2 ≠ V0`, `w2` a fixed
nonzero vector. Define, for `i=1,2`,
$$\mathrm{Cross}_i(r) := \mathrm{cross}(w_i,\,P(r)-V_i), \qquad
\mathrm{Dot}_i(r) := \mathrm{dot}(w_i,\,P(r)-V_i),$$
where `cross((x1,y1),(x2,y2)) := x1y2-x2y1`. Then `Cross_i(r)` and `Dot_i(r)`
are each degree-`≤1` (affine) polynomials in `r`, and
$$Q(r) \;:=\; \mathrm{Cross}_1(r)\,\mathrm{Dot}_2(r) \;-\; \mathrm{Cross}_2(r)\,\mathrm{Dot}_1(r)$$
is a polynomial of degree `≤2` in `r`.

*Proof.* Write `P(r)-V_i = r\,u + (V0-V_i)`, a sum of the fixed vector
`V0-V_i` and `r` times the fixed vector `u`. Cross and dot products are
bilinear, so
`Cross_i(r) = r\cdot\mathrm{cross}(w_i,u) + \mathrm{cross}(w_i,V0-V_i)` and
`Dot_i(r) = r\cdot\mathrm{dot}(w_i,u) + \mathrm{dot}(w_i,V0-V_i)`, each affine
in `r` with coefficients built purely from the fixed data `w_i, u, V0, V_i`.
`Q(r)` is then a difference of two products of affine functions of `r`, hence
a polynomial of degree `≤2`. ∎

**Geometric meaning and the equal-angle equation.** For a vector `v ≠ 0`,
writing `v` in polar form, `\mathrm{dot}(w,v) = |w||v|\cos\phi`,
`\mathrm{cross}(w,v) = |w||v|\sin\phi`, where `φ ∈ (-\pi,\pi]` is the *signed*
angle from `w` to `v` (positive counterclockwise). Hence
`Cross_i(r)/Dot_i(r) = \tan\phi_i(r)` where `φ_i(r)` is the signed angle from
`w_i` to `P(r)-V_i`. A direct computation (cross-multiplying) shows
$$Q(r) = |w_1||w_2|\,|P(r)-V_1|\,|P(r)-V_2|\;\sin(\phi_1(r)-\phi_2(r)).$$
So `Q(r)=0` (with all four vectors nonzero) is equivalent to
`\phi_1(r) \equiv \phi_2(r) \pmod \pi`, i.e. either `φ_1(r)=φ_2(r)` or
`φ_1(r)=φ_2(r)+\pi` (mod `2\pi`).

**Application to unsigned geometric angles.** The angles that occur in the
hypotheses `∠LCK=∠BMK` and `∠LBK=∠LNC` are *unsigned* triangle angles,
`\theta_i(r) := |\phi_i(r)| \in [0,\pi]` (taking the principal value of
`φ_i(r)` in `(-\pi,\pi]`). The equation we actually want to solve is
`\theta_1(r)=\theta_2(r)`, i.e. `φ_1(r)=\pm\phi_2(r) \pmod{2\pi}`. `Q(r)=0`
captures exactly the `+`-branch (`φ_1=φ_2 \bmod \pi`, which after taking
absolute values on both sides forces `\theta_1=\theta_2` whenever
`\phi_1,\phi_2` have the same sign, and forces `\theta_1=\pi-\theta_2`
otherwise) — it does **not**, by itself, distinguish the `+` branch from the
`−` branch (`φ_1=-\phi_2`) without an extra sign check. **This is the same
"sign convention" subtlety already flagged as an open caveat in
`lemmas/decoupling-and-sweep-lemma.md`** (there, for the Sweep Lemma's polar
angle vs. the unsigned geometric angle). We do **not** re-derive that sign
check from the hypotheses' containment/orientation conditions in full
generality this round (that would require characterizing exactly when
`φ_1(r), φ_2(r)` have matching sign throughout the geometrically valid range
of `r`, from H1's containment data — an open synthetic question). Instead we
verify computationally, below, that on every tested configuration the
correct geometric root of `F2(θ,r1)=0` (found by direct evaluation of the
unsigned angles via `arccos`, i.e. with no sign ambiguity at all) coincides
exactly with a specific root of the degree-`≤2` polynomial `Q(r)=0`. This is
reported as **numerically confirmed, not synthetically proven**, exactly
parallel in status to the existing certified caveat.

### 2. Applying Lemma T1 to `F2(θ,r1)=0` (solving for `r1 = BK`)

Take `V0 = B`, `u = u_1(θ)` the fixed unit vector giving the direction of ray
`BK` (making angle `θ` with ray `BA`, on the correct side per H1's
containment), so `P(r_1) = B + r_1 u_1(θ) = K`.

- **Vertex 1 = `M`** (midpoint of `AB`, fixed), with `w_1 := B - M` (the fixed
  direction of ray `MB`; `\mathrm{Cross}_1(r_1)=\mathrm{cross}(w_1, K-M)`,
  `\mathrm{Dot}_1(r_1)=\mathrm{dot}(w_1,K-M)` give the signed angle from `MB`
  to `MK`, whose absolute value is `∠BMK`).
- **Vertex 2 = `C`** (fixed), with `w_2 := u_2(θ)`, the fixed unit vector
  giving the direction of ray `CL` (making angle `θ` with ray `CA`); since
  `F2` does not depend on `r_2` (Decoupling Lemma), only the *direction* of
  `CL` matters, not `L`'s actual position. `\mathrm{Cross}_2(r_1) =
  \mathrm{cross}(u_2, K-C)`, `\mathrm{Dot}_2(r_1) = \mathrm{dot}(u_2,K-C)`
  give the signed angle from `CL` to `CK`, whose absolute value is `∠LCK`.

By Lemma T1, `Q_2(r_1) := \mathrm{Cross}_1(r_1)\mathrm{Dot}_2(r_1) -
\mathrm{Cross}_2(r_1)\mathrm{Dot}_1(r_1)` is a polynomial of degree `≤2` in
`r_1`, with coefficients that are explicit trigonometric functions of `θ`
(via `u_1(θ), u_2(θ)`) and of the fixed triangle data (via `B, C, M`, hence
via `a,b,c,α,β,γ`). Writing it out (as done concretely below in a coordinate
computation used only to VERIFY the algebra, not as part of the proof frame):
$$Q_2(r_1) = A_2\,r_1^2 + B_2\,r_1 + C_2,$$
$$A_2 = \mathrm{cross}(w_1,u_1)\,\mathrm{dot}(u_2,u_1) - \mathrm{cross}(u_2,u_1)\,\mathrm{dot}(w_1,u_1),$$
$$B_2 = \mathrm{cross}(w_1,u_1)\,\mathrm{dot}(u_2,B-C) - \mathrm{cross}(u_2,u_1)\,\mathrm{dot}(w_1,B-M)
      - \mathrm{cross}(u_2,B-C)\,\mathrm{dot}(w_1,u_1),$$
$$C_2 = -\,\mathrm{cross}(u_2,B-C)\,\mathrm{dot}(w_1,B-M),$$
using `w_1 = B-M` and expanding `Cross_1(r_1)=r_1\mathrm{cross}(w_1,u_1)+\mathrm{cross}(w_1,B-M)`
(note `\mathrm{cross}(w_1,B-M)=\mathrm{cross}(w_1,w_1)=0`, simplifying `A_2,B_2,C_2` further; the
displayed forms already use this), `Dot_1(r_1)=r_1\mathrm{dot}(w_1,u_1)+|w_1|^2`,
`Cross_2(r_1)=r_1\mathrm{cross}(u_2,u_1)+\mathrm{cross}(u_2,B-C)`,
`Dot_2(r_1)=r_1\mathrm{dot}(u_2,u_1)+\mathrm{dot}(u_2,B-C)`.

So `r_1(θ)` (the geometric root, subject to the sign caveat above) is a root
of the explicit quadratic `A_2 r_1^2+B_2 r_1 + C_2=0`, hence
$$r_1(\theta) = \frac{-B_2 \pm \sqrt{B_2^2-4A_2C_2}}{2A_2},$$
a genuinely **closed form** — no implicit IVT root-finding is needed to know
`r_1(θ)` exists in closed form; existence follows the moment the
discriminant `B_2^2-4A_2C_2 \ge 0` is verified (which is itself an explicit
trigonometric inequality in `θ,α,β,γ`, not a monotonicity argument), and the
"correct branch" question in geometric problems of this kind is generically
just "which of (at most) two roots lies in the valid range and satisfies the
containment constraints" — a finite check, not an IVT sweep.

**Numerical verification.** We checked this quadratic (instantiated in a
coordinate frame purely as a computational check of the algebra, exactly as
`coordinate-trig-bash` and the Decoupling Lemma already do for the ray
parametrization) on four configurations, including the exact configuration
`(p,q)=(0.0025,5.0)` that was the counterexample breaking
`coordinate-trig-bash`'s round-2 monotonicity claim:

| `(p,q)` | `θ` | quadratic roots `r_1` | numeric root of `F2=0` (direct `arccos`) |
|---|---|---|---|
| `(0.3,1.7)` | `0.35` | `0.719509`, `2.230248` | `0.7195088` |
| `(-0.6,1.2)` | `0.2` | `0.371254`, `1.472917` | `0.3712543` |
| `(0.9,1.3)` | `0.15` | `1.047728`, `2.299387` | `1.0477277` |
| `(0.0025,5.0)` | `0.6` | `0.962440`, `4.415724` | `0.9624401` |

In all four cases the **smaller** root of the quadratic matches the true
geometric root of `F2(θ,r_1)=0` to 6–7 significant figures (limited only by
the numerical root-finder's tolerance), and it is the unique root of
`F2(θ,r_1)=0` found by a fine (`4000`-point) scan plus bisection over the
whole plausible range — confirming both that the quadratic captures the
correct branch (`+` in the `±` above, smaller root, in every tested case)
and that there is exactly one geometric root, consistent with `F2` being
(known, certified) monotonic in the *sweep-lemma* sense.

### 3. Symmetric computation: `F1(θ,r2)=0` (solving for `r2 = CL`)

By the mirrored roles `(B,M,K,u_1) \leftrightarrow (C,N,L,u_2)`, the same
Lemma T1 applies with `V0=C`, `u=u_2(θ)`, vertex 1 `=B` (`w_1=u_1(θ)`, the
fixed direction of ray `BK`) and vertex 2 `=N` (`w_2 = C-N`, fixed direction
of ray `NC`). This gives a second quadratic
`Q_1(r_2) = A_1 r_2^2+B_1 r_2+C_1=0` with coefficients built from
`\mathrm{cross}/\mathrm{dot}` of `u_1,u_2,C-N,C-B` — a direct mirror of the
computation in §2 (we omit re-deriving the symbol-by-symbol formula, since it
is obtained from §2's by the substitution described, and instead report its
independent numerical verification, which is the load-bearing check here):

| `(p,q)` | `θ` | quadratic roots `r_2` | numeric root of `F1=0` (direct `arccos`) |
|---|---|---|---|
| `(0.3,1.7)` | `0.35` | `0.492003`, `2.042028` | `0.4920027` |
| `(-0.6,1.2)` | `0.2` | `0.842496`, `2.073396` | `0.8424956` |
| `(0.9,1.3)` | `0.15` | `0.410016`, `1.485630` | `0.4100155` |
| `(0.0025,5.0)` | `0.6` | `0.961281`, `4.415849` | `0.9612805` |

Again the smaller root matches the true geometric root in every test, in
particular again at the previously-problematic `(0.0025,5.0)` case, and is
the unique root found by the scan.

**Summary of §§1–3 (the genuinely new content of this approach).** The pair
`(r_1(θ), r_2(θ))` pinned by hypotheses H2, H3 given `θ` is, in each
coordinate, an explicit root of an explicit quadratic with trigonometric
coefficients in `θ` and the fixed data of triangle `ABC` — **not** merely an
implicitly-defined monotonic root requiring an IVT + a corrected domain of
validity (the machinery `coordinate-trig-bash` needed, and got wrong once
already in round 2). This closes the existence/uniqueness part of the
problem in a way genuinely different from, and cleaner than, the incumbent
approaches — **modulo the honestly-flagged branch-selection caveat** (that
the geometric root is always the "`+`"/smaller root is verified in the eight
trials above but not proven synthetically from the containment hypotheses in
general — the same open status as the Sweep Lemma's sign-convention caveat).

### 4. Explicit closed forms for `AK`, `AL`, and the angles `∠BAK, ∠CAL`

Once `r_1(θ), r_2(θ)` are known (in closed form, per §§2–3), the rest of
triangle `ABK`'s data is elementary and fully rigorous (pure Law of Cosines /
Law of Sines, no further gaps):

- **Law of Cosines in `△ABK`** (side `AB=c`, side `BK=r_1(θ)`, included angle
  `∠ABK=θ` by hypothesis H1):
  $$AK(\theta)^2 = c^2 + r_1(\theta)^2 - 2c\,r_1(\theta)\cos\theta. \tag{4.1}$$
- **Law of Cosines in `△ACL`** (side `AC=b`, side `CL=r_2(θ)`, included angle
  `∠ACL=θ`):
  $$AL(\theta)^2 = b^2 + r_2(\theta)^2 - 2b\,r_2(\theta)\cos\theta. \tag{4.2}$$
- **Law of Sines in `△ABK`** (angle `θ` at `B` opposite side `AK`, angle
  `∠BAK` opposite side `BK=r_1`):
  $$\sin(\angle BAK) = \frac{r_1(\theta)\sin\theta}{AK(\theta)}. \tag{4.3}$$
- **Law of Sines in `△ACL`** (symmetric):
  $$\sin(\angle CAL) = \frac{r_2(\theta)\sin\theta}{AL(\theta)}. \tag{4.4}$$

These four identities are elementary, exact, and require no further
justification beyond the standard Law of Cosines/Sines
(knowledge_base.md "Extended Law of Sines" / standard triangle trigonometry).

### 5. Where the pure-trig route stalls: the final identity requires more than angle data at `A`

To finish the proof via this route one still needs the circumcenter `O` of
`△AKL` located relative to `B, C` (equivalently, via the certified reduction
(TI) in `lemmas/median-length-power-reduction.md`, one needs
`\mathrm{pow}_\Gamma(B) - \mathrm{pow}_\Gamma(C)`, where `Γ` is the
circumcircle of `AKL`). Formulas (4.1)–(4.4) give `AK, AL`, and (subject to a
containment-based sign choice for how `∠KAL` decomposes as `α - ∠BAK -
∠CAL`, which is plausible given K is on the B-side and L on the C-side of
`A`'s angle but not verified here in full generality) one could in principle
also obtain `KL` via a further Law of Cosines in `△AKL`:
$$KL(\theta)^2 = AK(\theta)^2+AL(\theta)^2-2\,AK(\theta)AL(\theta)\cos(\angle KAL),
\qquad \angle KAL \overset{?}{=} \alpha - \angle BAK-\angle CAL. \tag{5.1}$$
This yields, via the Extended Law of Sines, the circumradius `R = KL/(2\sin\angle KAL)`
of `Γ`. **However, `R` alone is not enough to test `OM=ON`**: `OM, ON` (or
equivalently `pow_Γ(B), pow_Γ(C)`) depend on where `O` sits *relative to `B`
and `C`*, not just on `Γ`'s radius. Getting `pow_Γ(B)-\mathrm{pow}_\Gamma(C)`
purely from `AK, AL, KL` (i.e. from the *shape* of `△AKL` alone, without
knowing its *position* relative to `B, C`) is not possible in general — one
also needs, e.g., the direction of `AK` and `AL` relative to the fixed
directions `AB, AC` (equivalently `∠BAK, ∠CAL`, already available from
(4.3)–(4.4)) **and** an actual embedding of the whole configuration in a
common frame to compute a signed power-of-a-point quantity. Concretely: even
with `AK, AL, ∠KAL` (hence `KL`, `R`) known in closed trig form, expressing
`pow_Γ(B) = BA \cdot BA'` (`A'` = second intersection of line `BA` with `Γ`)
or any equivalent quantity still requires locating `Γ` relative to the fixed
points `B, C` — which is exactly the same content as fixing a coordinate
frame (as `coordinate-trig-bash` does) or computing `O`'s projection onto
`B-C` directly (as `labeling-duality`'s radical-axis form (TI″) does,
certified equivalent to `coordinate-trig-bash`'s target in
`lemmas/radical-axis-form-of-TI.md`).

**Honest conclusion on step 6 (mandated report).** We explicitly checked
whether the "no coordinate frame" framing lets the *final* identity
`OM=ON` be verified purely from angle/length data internal to `△ABK`,
`△ACL`, `△AKL` (i.e., from `AK, AL, ∠KAL, θ, α, β, γ` alone, with no
reference to a `B,C`-fixed frame) — and found that it cannot: the quantity
`OM=ON` genuinely depends on the *position* of the circumcenter `O` relative
to the fixed segment `BC` (via `M, N`), which is external data not captured
by the internal shape of `△AKL` alone. Any route to closing it — trig or
coordinate — must eventually re-introduce an equivalent of a `B,C`-anchored
frame (or the radical-axis/power abstraction, already shown algebraically
equivalent to it). **So this is a genuine, honestly-reported negative
finding for the mandated question:** §§1–4 above (the closed-form quadratic
solve for `r_1(θ), r_2(θ)` and the resulting `AK, AL, ∠BAK, ∠CAL` formulas)
are real, new, and correctly-derived leverage — a strictly better route to
the *existence and uniqueness* of the hypothesis-satisfying configuration
than `coordinate-trig-bash`'s IVT + monotonicity + domain-correction
machinery (which needed, and got wrong once, an intricate case split). But
**the final identity `OM=ON` itself, once one tries to actually verify it,
requires reintroducing frame-dependent information equivalent to
`coordinate-trig-bash`'s `O_x=p/2` / `labeling-duality`'s power-of-a-point
target — it is the same underlying wall, not a genuine bypass of it.** This
is consistent with `coordinate-trig-bash`'s round-1 negative Gröbner-basis
finding ("raw angle-equality polynomials do not force `O_x=p/2` alone") —
that finding used the coordinate polynomial system directly, and the
trig-Ceva route here, once pushed to the point of trying to state the final
identity, produces an equivalent polynomial system (in `r_1,r_2,\cos\theta,
\sin\theta` and the fixed triangle data), not a smaller or structurally
different one.

### 6. Net assessment

- **Genuine new leverage (proven, modulo one flagged numerical-only caveat):**
  Lemma T1 (fully proven, general, reusable — degree-≤2 reduction for
  "angle-matching along a ray") and its two applications, giving closed-form
  quadratics for `r_1(θ)` (§2) and `r_2(θ)` (§3), each numerically confirmed
  against direct geometric-angle computation on 4 configurations apiece
  (including the round-2 counterexample configuration), formulas (4.1)–(4.4)
  for `AK, AL, ∠BAK, ∠CAL` (fully proven, elementary Law of Cosines/Sines).
- **Not closed, and shown (§5) to be equivalent in difficulty to the
  incumbent wall, not a bypass:** the final `OM=ON` identity itself. This
  approach's remaining value is as a cleaner, closed-form route to
  existence/uniqueness of `(r_1(θ),r_2(θ))` (useful input to
  `coordinate-trig-bash`'s existence/uniqueness steps, replacing its IVT +
  monotonicity + domain-correction argument with an explicit quadratic-root
  selection, if that transfer is pursued in a future round) — not an
  independent route to the whole problem.

## Full proof
(Not present — Status is `partial`. The final identity `OM=ON` is not
established by this approach; see §5 for the honest, checked reason.)

## Promotable lemmas

**Lemma T1 (Angle-matching-on-a-ray is a degree-≤2 polynomial condition).**
Fully proven in §1 above, general and reusable: for a point `P(r)=V0+r\,u`
tracing a fixed ray, and two "hinge" vertex/direction pairs `(V_1,w_1)`,
`(V_2,w_2)`, the equation "signed angle from `w_1` to `P(r)-V_1`" `=`
"signed angle from `w_2` to `P(r)-V_2`" (mod `π`) is equivalent to
`Q(r):=\mathrm{Cross}_1(r)\mathrm{Dot}_2(r)-\mathrm{Cross}_2(r)\mathrm{Dot}_1(r)=0`,
a polynomial of degree `≤2` in `r`, with the explicit affine-coefficient
formulas for `Cross_i(r), Dot_i(r)` given in the proof. This is a general
elementary vector-algebra fact, useful in any problem where an angle
condition at a fixed vertex is imposed on a point sliding along a fixed ray
— reusable well beyond this problem, in the same spirit as (but structurally
different from, and complementary to) the certified Decoupling and Sweep
Lemmas. Recommend certifying to `lemmas/` if the reviewer confirms the proof
(pure vector bilinearity, no gaps in the polynomial-degree claim itself; the
**unsigned-vs-signed angle branch-selection subtlety is explicitly flagged as
NOT part of the certified content**, exactly parallel to the existing caveat
already attached to the Sweep Lemma — do not certify the branch-selection
claim "smaller root = geometric root" as a general fact, only as numerically
observed in this problem's 8 test instances).

**Formulas (4.1)–(4.4)** (`AK, AL` via Law of Cosines in `△ABK,△ACL`;
`∠BAK,∠CAL` via Law of Sines) are fully proven, elementary, and reusable as
input to any future approach that needs `AK, AL` or the sub-angles at `A` in
closed trig form once `r_1(\theta), r_2(\theta)` are known or bounded.
