## Status
partial

## Approaches tried
- Round 2: outline-reviewer flagged a logical error in the round's proposed
  "step 2" (claiming BK is computable from θ,β by law of sines alone — false,
  since BK=r1 is exactly the free parameter conditions (2),(3) exist to pin
  down; confirmed and NOT used below). Redirected to two untried levers per
  the synthetic-gap explorer: (a) radical axis of Γ=circumcircle(AKL) and
  Ω=circumcircle(ABC); (b) secant-line identification of the second
  intersection of Γ with lines through B or C. Result: (a) gives a fully
  rigorous ALTERNATIVE derivation of the equivalence target — cleaner, and
  frame-free — but proved (by direct computation) to be *informationally
  equivalent* to the existing (TI)/O_x=p/2 criterion, not a new reduction:
  it still requires computing the projection of O onto line BC, which is
  exactly what's unknown. (b) tested numerically on three independent
  triangles: the second intersection of line BK (or CL, or BA, or CA) with Γ
  does not coincide with any hypothesis point (M, N, A, C, L, etc.) in any
  instance — ruled out as a shortcut. Net outcome: genuine but negative
  progress — two additional plausible synthetic shortcuts are now shown NOT
  to bypass the core difficulty; this approach's gap is reconfirmed to be the
  same underlying difficulty flagged in coordinate-trig-bash (computing the
  BC-projection, equivalently pow_Γ(B)−pow_Γ(C), from the raw angle system).
  See "Current best" and new subsection below for full derivations.
- Round 1 (outline): symmetric-function/duality argument on OM²−ON² using the
  σ: B↔C, K↔L, M↔N relabeling symmetry of the hypothesis system, working
  directly with the Cramer's-rule vector formula for O(A,K,L). Outline flagged
  steps 3–4 (finding and cancelling the σ-antisymmetric residual) as an
  unproven "named-without-mechanism" gap — confirmed accurate by this build
  pass; see below.
- Round 1 (this build): (1) verified the σ-invariance of the hypothesis system
  rigorously (not just asserted); (2) derived a NEW, cleaner reduction of the
  whole target OM=ON to a single power-of-a-point identity via the classical
  median-length (Apollonius) theorem, sidestepping the messier Cramer's-rule
  cross-product expansion the outline proposed; (3) verified this reduction
  numerically to machine precision on the explorer's example; (4) attempted to
  close the remaining identity synthetically via secant lines through B, C to
  the circumcircle of AKL — did not find a complete synthetic closure in the
  time available; this final identity is the honest, explicit open gap.
  Outcome: genuine progress (a sharper, fully-proven equivalent target), but
  the approach does not yet close the problem.

## Current best

**Step 0 — the σ-invariance of the hypothesis system (fully verified).**

Since `M` is the midpoint of `AB`, `M` lies on segment `AB`, so ray `BM` = ray
`BA`; hence `∠KBA = ∠KBM` as literal ray-equality (not just numerically equal
angles — the two angles are the same angle, sharing both rays). Likewise `N`
on segment `AC` gives ray `CN` = ray `CA`, so `∠ACL = ∠NCL`. Hence hypothesis
(1), `∠KBA = ∠ACL`, is verbatim the same statement as

  (1′) `∠KBM = ∠LCN`.

The full hypothesis list, rewritten, is:
  (1′) `∠KBM = ∠LCN`
  (2)  `∠LBK = ∠LNC`
  (3)  `∠LCK = ∠BMK`

Apply the relabeling σ that swaps `B↔C`, `K↔L`, `M↔N` and fixes `A` (a purely
syntactic substitution into the *symbols*, not a claim about a geometric map
of the actual figure):
  - (1′) `∠KBM = ∠LCN` ↦ `∠LCN = ∠KBM`, i.e. the same equation (condition (1′)
    is self-dual).
  - (2) `∠LBK = ∠LNC` ↦ `∠KCL = ∠KMB`. This is exactly condition (3),
    `∠LCK = ∠BMK`, since `∠KCL=∠LCK` and `∠KMB=∠BMK` (angle notation is
    symmetric in its two rays). So σ sends (2) to (3).
  - (3) `∠LCK = ∠BMK` ↦ `∠KBL = ∠CNL`. This is exactly condition (2),
    `∠LBK=∠LNC`, again by symmetry of angle notation (`∠KBL=∠LBK`,
    `∠CNL=∠LNC`). So σ sends (3) to (2).

Hence σ maps the set `{(1′),(2),(3)}` bijectively to itself: (1′) is fixed,
(2) and (3) are swapped. This proves the hypothesis *system* (as a set of
equations) is σ-invariant. (The containment/interiority hypotheses — K inside
∠LBA, L inside ∠ACK, K interior to △BMC, L interior to △BNC — are also
syntactically self-dual under σ in the same sense: "K inside ∠LBA" $\leftrightarrow$
"L inside ∠KCA" = "L inside ∠ACK", and "K ∈ int(△BMC)" $\leftrightarrow$ "L ∈
int(△CNB)" = "L ∈ int(△BNC)". So the full hypothesis package, as a set of
syntactic conditions on the labels, is σ-invariant.)

**Caveat (carried over from the outline, confirmed, and to be respected by
any future work on this approach):** σ is a symmetry of the *equation set*,
not of the geometric figure. For a fixed triangle `ABC` (B, C not
interchangeable in general) there is no rigid map of the plane realizing σ,
and indeed the round-1 explorer's numeric example already refutes any naive
metric transfer: `BM=1.803` vs `CN=2.121`, `BK=0.728` vs `CL=1.181`,
`∠BMK=15.06°` vs `∠CNL=25.39°` — all unequal. So σ cannot be used to assert
`BK=CL`, `MK=NL`, or any other length/angle transfer between the "B-side" and
"C-side" data of one single solution `(K,L)`. Its only legitimate use is:
*if `(K,L)` satisfies the hypothesis system for triangle `(A,B,C)`, and
`(K*,L*):=(L,K)` is defined for the "mirror" triangle-instance with `B,C`
swapped, then `(K*,L*)` satisfies the (swapped) hypothesis system for that
mirror instance.* This is a fact about two different problem instances, not
an equality within one figure — exactly the caveat the outline-reviewer
required be respected, and it is respected here: no metric identity between
the B-side and C-side of a *single* configuration is asserted anywhere below.

**Step 1 — reduce OM=ON to a power-of-a-point identity via Apollonius
(fully proved, not conjectural).**

*Lemma A (median-length / Apollonius theorem).* For any point `O` and any
segment `XY` with midpoint `Z`,
$$OZ^2 = \frac{OX^2+OY^2}{2} - \frac{XY^2}{4}.$$

*Proof.* Place vectors with origin at `O`; write `x = X-O`, `y=Y-O`,
`z = Z-O = (x+y)/2`. Then
$$2\,OZ^2 + \tfrac12 XY^2 = 2\left|\tfrac{x+y}2\right|^2+\tfrac12|x-y|^2
=\tfrac12|x+y|^2+\tfrac12|x-y|^2=\tfrac12\big(|x|^2+2x\cdot y+|y|^2\big)+\tfrac12\big(|x|^2-2x\cdot y+|y|^2\big)
=|x|^2+|y|^2=OX^2+OY^2,$$
using the parallelogram identity `|x+y|^2+|x-y|^2=2|x|^2+2|y|^2`. Rearranging
gives the claim. ∎ (This is the standard median-length / Apollonius theorem;
knowledge_base.md's synthetic toolkit lists power-of-a-point and standard
circle/triangle metric identities as the relevant technique family.)

Apply Lemma A twice, with `M` the midpoint of `AB` and `N` the midpoint of
`AC`:
$$OM^2=\frac{OA^2+OB^2}2-\frac{AB^2}4, \qquad ON^2=\frac{OA^2+OC^2}2-\frac{AC^2}4.$$
Subtracting,
$$OM^2-ON^2=\frac{OB^2-OC^2}2+\frac{AC^2-AB^2}4. \tag{$\ast$}$$
This identity holds for **any** point `O` — it does not yet use that `O` is
the circumcenter of `AKL`. In particular `OM=ON \iff OM^2=ON^2 \iff`
$$OB^2-OC^2=\frac{AB^2-AC^2}2. \tag{$\ast\ast$}$$

Now use that `O` is specifically the circumcenter of `AKL`, so `OA=OK=OL=:R`.
Let `Γ` denote the circumcircle of `AKL` (center `O`, radius `R`); since `A`
lies on `Γ`, `R = OA`. The power of a point `X` with respect to `Γ` is by
definition `\mathrm{pow}_\Gamma(X) = OX^2-R^2 = OX^2-OA^2`. Hence
$$OB^2-OC^2 = (OB^2-OA^2)-(OC^2-OA^2) = \mathrm{pow}_\Gamma(B)-\mathrm{pow}_\Gamma(C),$$
so `(∗∗)` is exactly equivalent to

$$\boxed{\ \mathrm{pow}_\Gamma(B)-\mathrm{pow}_\Gamma(C) = \frac{AB^2-AC^2}{2}\ }\tag{TI}$$

where `Γ` is the circumcircle of `AKL`. **This target (TI) is a strictly
sharper, single scalar identity equivalent to the original OM=ON claim**, and
its proof would complete the problem. This equivalence is a complete,
gap-free chain: Lemma A is proved from scratch above, the passage `(∗)→(∗∗)`
and `(∗∗)→(TI)` are direct algebra using only the definitions of midpoint,
power of a point, and `OA=OK=OL`.

**Numerical confirmation of the reduction (sanity check, not a proof step).**
Using the round-1 explorer's example `A=(0,3), B=(-2,0), C=(3,0)` with `θ =
∠KBA = 25°` solved numerically (via the same `fsolve` setup the synthetic
explorer used) to get a concrete valid `(K,L)`:
`K≈(-1.378,0.378), L≈(1.891,0.404)`, circumcenter `O≈(0.25, 1.1955)`,
`R≈1.8217`. Then:
`OM = 1.2865506964..., ON = 1.2865506964...` (agree to 1e-10, confirming
`OM=ON` for this instance, as expected),
`OB^2-OC^2 = -2.500000000002`, `(AB^2-AC^2)/2 = -2.499999999999...` (agree to
1e-10), and `pow_Γ(B)-pow_Γ(C) = -2.500000000002` also agreeing — confirming
`(TI)` holds numerically on this instance, consistent with the algebra above
(this is a consistency check of the derivation, not a substitute for it — the
derivation of `(∗),(∗∗),(TI)` above is a self-contained algebraic proof valid
for every configuration, independent of this numeric instance).

**Open gap: proving (TI) from the three angle hypotheses.**

This is now the entire remaining content of the problem. It has not been
closed by this build pass. What has been tried and where it stalls:

- *Attempt via σ-consistency.* Under the σ-relabeling of Step 0 (swap
  `B↔C, K↔L`, hence `Γ` becomes the circumcircle of the *mirror* configuration
  `A,L,K` — the same circle, since `{A,K,L}` is an unordered point set), (TI)
  becomes `pow_Γ(C)-pow_Γ(B) = (AC^2-AB^2)/2`, which is exactly the negation
  of (TI) — i.e. (TI) is anti-symmetric under σ, consistently with the
  hypothesis system being σ-invariant. This is a necessary consistency check
  that (TI) passes, but (as flagged in the outline and reconfirmed above) σ
  relates *two different configurations* (the given one, and the mirror one
  with `B,C` swapped), not two quantities within the same figure, so
  self-consistency under σ cannot by itself force (TI) to hold — it only
  shows (TI) is not obviously false by symmetry. The σ argument alone cannot
  close this gap; an independent computation using the actual angle
  hypotheses is required.
- *Attempt via secant lines.* The natural way to compute `pow_Γ(B)` is via a
  secant of `Γ` through `B`. Two candidate secants: (a) line `BK` (since `K∈Γ`)
  meets `Γ` again at some second point `K₂`, giving
  `pow_Γ(B) = \overline{BK}\cdot\overline{BK_2}` (signed lengths); (b) line
  `BA` (since `A∈Γ`) meets `Γ` again at some second point `A'`, giving
  `pow_Γ(B)=\overline{BA}\cdot\overline{BA'}`. Either route requires locating
  the second intersection point (`K_2` or `A'`) using the inscribed-angle
  theorem in `Γ` (relating angles subtended by chords `AK`, `AL`, `KL` as seen
  from different points of `Γ`), and there is no hypothesis directly pinning
  down `∠AKL`, `∠ALK`, or `∠KAL` — these would have to be derived from
  conditions (1′), (2), (3), which involve `M`, `N`, `B`, `C`, not points of
  `Γ` itself. This is genuinely the hard remaining step, and closing it
  appears to require essentially reconstructing (a version of) the angle-chase
  that would pin down `K, L` — i.e., there is no shortcut found that avoids
  substantial further computation. Flagged honestly as unresolved within this
  build's time budget.
- The Cramer's-rule vector route proposed in the original outline (steps 2–4)
  was checked as an alternative and shown (by hand, cross-checked with the
  above) to reduce to an *equivalent* but algebraically messier version of the
  same identity (TI) — expanding `O` via `2O\cdot K=|K|^2`, `2O\cdot L=|L|^2`
  and substituting into `OM^2-ON^2` reproduces `(TI)` after using the standard
  circumcenter-of-`(0,K,L)` formula `O=(|L|^2\,\mathrm{rot}_{90}(K)-|K|^2\,
  \mathrm{rot}_{90}(L))/(2\,K\times L)` (with `A` at the origin); this is
  consistent with, but strictly harder to use than, the power-of-a-point form
  (TI) obtained via Lemma A, since (TI) isolates a single circle-invariant
  quantity (`\mathrm{pow}_\Gamma`) rather than an explicit coordinate
  expression for `O`. **Recommendation for the next round:** work directly
  with target (TI) (drop the Cramer's-rule/cross-product route entirely — it
  is redundant with (TI) and strictly more cluttered), and focus all effort
  on expressing `\mathrm{pow}_\Gamma(B)` and `\mathrm{pow}_\Gamma(C)` via the
  three angle hypotheses, most promisingly via secant line `BA`/`CA` through
  the already-known point `A\in\Gamma`, using the inscribed angle theorem
  together with conditions (1′)–(3) to pin the second intersection points.

**Step 2 (this round) — the radical-axis reframing of (TI), and why it does
not shortcut the gap.**

Let `Ω` denote the circumcircle of `ABC` (center `O_Ω`, radius `R_Ω`), and
recall `Γ` denotes the circumcircle of `AKL` (center `O`, radius `R`); both
pass through `A`. For any point `X` in the plane, expanding the definition of
power of a point in coordinates (origin arbitrary):
$$\mathrm{pow}_\Gamma(X)=|X|^2-2X\cdot O+|O|^2-R^2,\qquad
\mathrm{pow}_\Omega(X)=|X|^2-2X\cdot O_\Omega+|O_\Omega|^2-R_\Omega^2.$$
Subtracting, the `|X|^2` terms cancel and
$$\mathrm{pow}_\Gamma(X)-\mathrm{pow}_\Omega(X) = 2X\cdot(O_\Omega-O) + \big(|O|^2-R^2\big)-\big(|O_\Omega|^2-R_\Omega^2\big),$$
an **affine-linear function of `X`** with linear part `2X\cdot(O_\Omega-O)`
(its zero set is, by definition, the radical axis of `Γ,Ω`; this is standard
but re-derived from scratch here, not merely cited). Evaluate at `X=B` and
`X=C` and subtract: the constant term cancels identically, giving
$$\big(\mathrm{pow}_\Gamma(B)-\mathrm{pow}_\Omega(B)\big)-\big(\mathrm{pow}_\Gamma(C)-\mathrm{pow}_\Omega(C)\big)
= 2(B-C)\cdot(O_\Omega-O). \tag{R1}$$
Since `B,C\in\Omega`, `\mathrm{pow}_\Omega(B)=\mathrm{pow}_\Omega(C)=0` by
definition of power of a point on its own circle. So (R1) simplifies to
$$\mathrm{pow}_\Gamma(B)-\mathrm{pow}_\Gamma(C) = 2(B-C)\cdot(O_\Omega-O). \tag{R2}$$
Substituting into target (TI) (already proved equivalent to `OM=ON` in Step
1), we get the **equivalent restatement**:
$$2(B-C)\cdot(O_\Omega-O) = \frac{AB^2-AC^2}{2}. \tag{TI′}$$
Note `O_\Omega` is a completely FIXED point (the circumcenter of the given
triangle `ABC`, independent of `K,L,θ`), so (TI′) says: *the scalar projection
of `O` (circumcenter of `AKL`) onto the fixed direction `B-C` is pinned to one
specific fixed value*, namely
$$(B-C)\cdot O = (B-C)\cdot O_\Omega - \frac{AB^2-AC^2}{4}.\tag{TI″}$$

*Cross-check this is a genuine re-derivation, not circular.* (TI″) is
literally the frame-free version of coordinate-trig-bash's certified target
`O_x=p/2` (in their frame `B=(-1,0),C=(1,0),A=(p,q)`, direction `B-C` is the
`x`-axis, so `(B-C)\cdot O \propto O_x`, and one checks directly that the
right-hand side of (TI″) reduces exactly to `p/2` after substituting
`O_\Omega,AB,AC` in that frame — confirmed both algebraically, by direct
substitution `B=(-1,0),C=(1,0),A=(p,q)`: `AB^2-AC^2=(p+1)^2+q^2-(p-1)^2-q^2=4p`,
and `O_\Omega=(0,(p^2+q^2-1)/(2q))` [standard circumcenter formula for this
frame], so `(B-C)\cdot O_\Omega = (-2,0)\cdot(0,\cdot)=0`, giving RHS of
(TI″) `=0-4p/4=-p`; and `(B-C)\cdot O=(-2,0)\cdot(O_x,O_y)=-2O_x`, so (TI″)
reads `-2O_x=-p`, i.e. `O_x=p/2` exactly — and numerically, on the three
fresh triangles tested below, to machine precision.)

This confirms (TI′)/(TI″) is a **correct, fully rigorous alternative form**
of the SAME target as `O_x=p/2` — genuinely equivalent, not merely
consistent. It is arguably cleaner (frame-free, and isolates "projection of
`O` onto `BC`" as the single unknown, with a fully explicit target value in
terms of `O_\Omega` and side lengths). **But it supplies no new information**:
proving (TI″) still requires computing where the circumcenter `O` of `AKL`
projects onto line `BC`, and that still requires locating `K,L` (or at least
`O`) using the raw angle hypotheses — exactly the same open computation
flagged by coordinate-trig-bash's Gröbner-basis negative result. The radical
axis route was a legitimate thing to try (per the synthetic-gap explorer's
suggestion) and is now confirmed, by this direct computation, to be
information-equivalent to the existing gap rather than a bypass of it.

*(Aside, not load-bearing: an even more elementary route to the same
equivalence, bypassing both Apollonius and the radical axis, is to note
`OM=ON \iff O` lies on the perpendicular bisector of segment `MN`, and
`M-N=(B-C)/2` — i.e. segment `MN` is parallel to `BC` with half its length
(the midline of `ABC`), a standard fact re-derivable in one line from
`M=(A+B)/2,N=(A+C)/2`. Hence the perpendicular bisector of `MN` is the line
through `\mathrm{mid}(M,N)=\tfrac14(2A+B+C)` perpendicular to `BC` — i.e. `OM=ON
\iff O` and `\tfrac14(2A+B+C)` have the same projection onto line `BC`. This is
again exactly the same "projection of `O` onto `BC`" statement as (TI″); it is
recorded here only because it is a strictly simpler proof of the equivalence
than either Step 1 (Apollonius) or Step 2 (radical axis) above, and could
replace both in a final writeup, but it does not close the open gap either.)*

**Step 3 (this round) — secant-line attempts to compute `pow_Γ(B)`
individually: tested and ruled out as a shortcut.**

The natural way to compute `pow_Γ(B)` directly is via a secant of `Γ`
through `B`. Two candidate secants were tested numerically (via `fsolve` on
the exact hypothesis system, using the same rig as prior rounds) on three
independent triangles (`A=(0.3,1.7)`, `A=(0.9,1.3)`, `A=(-0.2,2.1)`, each with
`B=(-1,0),C=(1,0)` and a solved value of `θ`):

- *Secant `B,K`* (since `K\in\Gamma`): computed the second intersection point
  `K'` of line `BK` with `Γ` explicitly (solving the quadratic
  `|B+td-O|^2=R^2` for `t`, `d` the unit direction `B\to K`) on all three
  triangles. In every instance, `K'` does not coincide with any hypothesis
  point: measured distances from `K'` to `M,N,A,C,L` are all bounded well
  away from zero (e.g. on triangle `A=(0.3,1.7)`: distances `1.30, 0.37, 0.87,
  1.10, 0.82` respectively — none near `0`; similarly on the other two
  triangles, no near-zero distance to any named point). So `K'` is not
  identifiable with a named point of the configuration by inspection, and
  `pow_\Gamma(B)=\overline{BK}\cdot\overline{BK'}` cannot be evaluated without
  first locating `K'` by some other means (e.g. the inscribed-angle theorem
  on `Γ`, which would require angles `\angle AKL,\angle ALK` — themselves not
  directly given by the hypotheses, which only constrain angles at `B,C,M,N`).
  **Ruled out** as a shortcut (matches, and independently reconfirms on fresh
  triangles, the synthetic-gap explorer's finding on this route).
- *Secant `B,A`*: same conclusion by the symmetric computation — the second
  intersection of line `BA` with `Γ` does not coincide with any named point
  either (this matches the explorer's report: `A′` at distance `1.25` from
  `N`, `1.67` from `C`, i.e. no match).

Both secant routes require, in effect, first solving for the shape of
triangle `AKL` inside `Γ` (its inscribed angles), which is not shortcut-able
from the given hypotheses (they constrain `\angle KBA,\angle LBK,\angle LCK`
— angles at `B` and `C`, not the internal angles of `AKL` itself) without
essentially redoing the full nonlinear system.

**Honest conclusion for this round.** Both untried directions flagged by the
synthetic-gap explorer have now been carried out to completion: the radical
axis reframing is fully proved (a legitimate new equivalent form of (TI)) but
shown to be informationally equivalent to the existing gap, and the
secant-line identification is numerically tested and ruled out as a
shortcut. No new route out of the gap was found this round. This approach's
open gap — deriving (TI)/(TI″)/`O_x=p/2` from the raw angle hypotheses — is
the SAME gap coordinate-trig-bash's Gröbner-basis computation showed cannot
be reached by algebra on the raw angle-equality polynomials alone (the
containment/orientation branch must be used); this round's negative results
reinforce that no simple synthetic identity (single secant, single spiral
similarity, single concyclicity, or a change of target via radical axis)
bypasses this. The most promising untried lever, per the synthetic-gap
explorer and not attempted in the time available this round, is the direct
law-of-sines chase using the *decoupled* structure already certified by
coordinate-trig-bash's Lemma 3 (condition (2) alone determines `r2=CL` as a
function of `θ` only, and condition (3) alone determines `r1=BK` as a
function of `θ` only, since each angle in each condition is shown to be
independent of the "other" free radius by the ray-direction-cancellation
argument) — i.e., solving each of the two single-unknown transcendental
equations `F_1(\theta,r_2)=0` and `F_2(\theta,r_1)=0` in closed form via the
law of sines in the moving triangles, rather than treating them as an
implicit coupled pair. This was not attempted here for lack of remaining
time and is flagged for the next round.

## Full proof
(Not present — Status is `partial`; see Current best for the exact point
the proof stops, honestly marked.)

## Promotable lemmas

- **Lemma A (median-length / Apollonius identity for an arbitrary point):**
  For any point `O` and segment `XY` with midpoint `Z`,
  `OZ^2 = (OX^2+OY^2)/2 - XY^2/4`. Proved in full above via the
  parallelogram law `|x+y|^2+|x-y|^2 = 2|x|^2+2|y|^2` applied to
  `x=X-O, y=Y-O`. This is a fully general, standalone, reusable fact
  (independent of the rest of the problem) and should be certified as a
  shared lemma.
- **Reduction lemma (specific to this problem, but fully proved and
  reusable across any approach attacking OM=ON directly):** For `O` the
  circumcenter of `AKL`, `OM=ON \iff \mathrm{pow}_\Gamma(B)=\mathrm{pow}_\Gamma(C)+(AB^2-AC^2)/2`,
  where `Γ=`circumcircle(`AKL`). Proved in full in Step 1 above (combines
  Lemma A with the definition of power of a point and `OA=OK=OL`). This
  converts the entire remaining problem into proving identity (TI); any
  future approach (coordinate, synthetic, or complex-number) should target
  (TI) directly rather than `OM=ON` itself, since (TI) is a strictly
  simpler, single scalar target.
- **σ-invariance of the hypothesis system** (Step 0 above): fully verified,
  reusable observation, with the caveat about it being a labeling symmetry
  of equations (not the figure) made explicit and precise.
- **Radical-axis form of (TI)** (Step 2 above, round 2): for `Ω`=
  circumcircle(`ABC`), `Γ`=circumcircle(`AKL`), `\mathrm{pow}_\Gamma(X)-\mathrm{pow}_\Omega(X)`
  is affine-linear in `X` with linear part `2X\cdot(O_\Omega-O)`; combined
  with `\mathrm{pow}_\Omega(B)=\mathrm{pow}_\Omega(C)=0`, this gives
  `\mathrm{pow}_\Gamma(B)-\mathrm{pow}_\Gamma(C)=2(B-C)\cdot(O_\Omega-O)`, an
  equivalent, frame-free restatement of (TI) as a statement about the
  projection of `O` onto line `BC`. Fully proved; reusable by any future
  approach as an alternative (not strictly more powerful) form of the target.
  Confirmed information-equivalent to coordinate-trig-bash's `O_x=p/2`
  criterion, not a new reduction — see Step 2 discussion for why this does
  not close the gap.
