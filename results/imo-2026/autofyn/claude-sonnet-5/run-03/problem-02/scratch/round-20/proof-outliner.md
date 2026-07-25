## imo-2026-02

### Cross-cutting note for the outline-reviewer (read before ranking)
This round's `T-positivstellensatz` explorer gives a structural explanation
for the 10-round-old SOS/SDP degeneracy on `-q1,-r0`/`T≥0`: `T` is not just
numerically tight but **exactly 0** at the corner `(A*,β0(A*))`,
`A*=3·arcsin(√6/4)−π/2` — the SAME corner already used to close
`D1≥0` (rounds 17-18, `lemmas/d1-nonnegative-on-boundary-curve.md`) and
`Tgt>0` (round 16, `lemmas/tgt-strictly-positive-throughout-D-full.md`) —
and `T` vanishes to first order (linearly, not quadratically) along the
domain's own active boundary there. This is a forced complementary-slackness
rank deficiency: **no further SOS/SDP search on `T`, `q1`, `r0`, or the
`-sos` route's `Num/n1/n2/n4` encoding should be dispatched this round** —
it will keep reproducing the same degeneracy at any degree (memory rule,
rounds 16-18, now explained rather than merely observed). The one proven
technique that has twice already defeated an identical local degeneracy at
this exact corner (Taylor expansion + certified Lagrange remainder, glued to
an away-from-corner interval sweep) is the right tool, applied directly —
not routed through another SDP attempt. `coordinate-bash-resultant-
boundary-pointwise-sos` is therefore **not** fielded for a build slot this
round (recommend "advance (dormant, no build slot)" per the round-9 memory
rule, unless the reviewer wants a diagnostic-only pass); its diagnosed
degeneracy is now explained by item (1) below, not left as an open mystery.

---

coordinate-bash-resultant-boundary-pointwise-tangent: advance
Target: `OM=ON` (the whole problem, via this route's certified Reduction
Lemma: hypothesis (A) `Tgt>0` [closed, round 16] + hypothesis (B) `D1≥0` on
the boundary curve [closed, rounds 17-18] + Case (a)/(b) case-tree closure
of the underlying `G(β1)≥0` fact [Case (b) closed except the residual
`P>0∧E<0` sub-case; Case (a) reduced by round 19 to the SAME residual
sub-case] `⟹ f≥g ⟹ OM=ON`).
Technique: local Taylor expansion + certified Lagrange-remainder bound near
the corner `(A*,β0(A*))`, glued to a coarse `mpmath.iv` interval-arithmetic
sweep away from the corner — the exact two-part method already certified
twice on this same corner (`d1-nonnegative-on-boundary-curve.md`,
`tgt-strictly-positive-throughout-D-full.md`), applied here to close the
route's one remaining open gap: `G(β1)≥0` on the residual sub-case
`P>0∧E<0` of the true domain `D={0<A≤π/2, 0<B≤C, B>β0(A),
cos²B<X0(A,B)<cos²β0(A)}` (this domain restriction, with BOTH bounds, is
essential — dropping the upper bound manufactures spurious violations, per
this round's explorer; use the file's own "Exact Case-(b) domain" verbatim).
Skeleton:
  1. Restate the target exactly: `G(β1)≥0` for all `(A,B)∈D∩{P>0,E<0}` —
     by the certified equivalence chain in `case-b-e-lt-0-t-factorization.md`
     and `case-b-p-le-0-and-e-ge-0-closed.md` this is equivalent to
     `T:=Bc²X0−E²≥0`.
  2. Away from the corner (`|A−A*|>δ` for a fixed small `δ`, say `10⁻²`):
     dense `mpmath.iv` directed-rounding sweep of `T` (or `G`) over
     `D∩{P>0,E<0}∩{|A−A*|>δ}` — by the same interval-arithmetic machinery
     already certified for `Tgt`/`D1`. This round's explorer's own coarse
     sweep already shows `T_min≈0.0187` at `ε=δ=10⁻²`, giving real margin
     to certify.
  3. Near the corner (`|A−A*|≤δ`): Taylor-expand `T` (or, to avoid the
     extra algebraic complexity of the two squarings in the `T`-reduction,
     `G(β1)` directly) in `(A−A*, B−β0(A))` along the domain's own active
     boundary curve `B=β0(A)`, to FIRST order (the vanishing here is
     linear, confirmed this round via `T_min(ε)/ε≈1.87–2.14` roughly
     constant for `ε∈{10⁻²,…,10⁻⁵}` — not the quadratic/tangential case
     round 16's `Tgt` argument handled, so the Lagrange-remainder bound
     must be built around a nonzero first derivative along the active
     constraint direction, mirroring round 17-18's `D1` corner argument
     (which also had a nonzero one-sided derivative, not a cusp — per the
     memory rule from round 17, do NOT plan a concavity/unimodality proof;
     a directional-derivative-lower-bound + remainder split suffices).
  4. Glue Steps 2–3 via the standard "value at corner is 0, sign of nearby
     values controlled either by direct sweep or by MVT off a certified
     nonzero directional derivative" argument (exact template of
     `d1-nonnegative-on-boundary-curve.md`'s Steps 1-4).
  5. Conclude `T≥0` (hence `G(β1)≥0`) throughout `D∩{P>0,E<0}`, closing
     Case (b)'s residual sub-case, and — per round 19's finding that the
     same sub-case is the one remaining piece of Case (a) too — closing
     Open gap 7 for BOTH cases simultaneously.
  6. Combine with the already-certified Reduction Lemma to conclude
     `OM=ON` unconditionally (modulo the separately-handled isosceles case,
     already closed per `isosceles-case-symmetry.md`).
Key lemmas (claim + mechanism):
  - `T(A*,β0(A*))=0` exactly — because this is the same corner where
    `D1` and the `Tgt` boundary curve both vanish (numerically confirmed to
    50-166 digits this round; a short symbolic proof that
    `X0(A*,β0(A*))=cos²β0(A*)=3/8` exactly is a concrete, well-scoped
    sub-lemma, analogous in style to round 17-18's `D1` corner-value proof).
  - `T` vanishes to exactly first order along `B=β0(A)` as `A→A*⁺` — because
    the domain itself has width 0 at the corner (a genuine boundary-active
    constraint, not an interior critical point) — this determines the shape
    of the required Lagrange-remainder argument (directional derivative
    bound, not a second-order/concavity argument).
Open gaps: the symbolic proof of `X0(A*,β0(A*))=3/8` (numerically certain,
not yet proved); the Taylor+Lagrange-remainder argument itself (Step 3) —
not yet built for `T`/`G` (only diagnosed this round); the final gluing
(Step 4) and margin arithmetic.
Cases to cover: none beyond the existing Case (a)/(b) split, already fully
enumerated by prior rounds — this closes the single remaining residual
sub-case shared by both.
Watch out for: (i) always use the FULL three-part domain restriction
(`B>β0(A)` AND `cos²B<X0` AND `X0<cos²β0(A)`) in every sweep — dropping the
upper bound manufactures large spurious violations (this round's explorer's
own finding); (ii) the vanishing is LINEAR not quadratic — do not reuse the
`Tgt` corner's tangent-cone/second-derivative template verbatim, adapt it to
a first-order directional-derivative bound instead (per the round-17 memory
rule on cusp-vs-nonzero-derivative gaps).

coordinate-bash-resultant-boundary-pointwise-tangent-via-T: copy-of coordinate-bash-resultant-boundary-pointwise-tangent
Target: identical (`OM=ON`, same Reduction Lemma).
Technique: identical two-part local-Taylor/interval-sweep method, but Step 3
is built on the EXPLICIT RATIONAL polynomial form
`T=c(dQ1−cR0)/(4sin²(A+B))`, `Q1=−4st·q1(σ,τ)`, `R0=r0(σ,τ)` (certified,
`case-b-e-lt-0-t-factorization.md`), Taylor-expanding the polynomials
`q1,r0` directly in `(σ,τ)=(sin²A,sin²B)` near the corner's `(σ*,τ*)` value,
rather than expanding the trigonometric `G(β1)` directly. This is a genuine
alternative mechanism for the SAME gap (algebraic-polynomial Taylor
expansion vs. trigonometric-function Taylor expansion) — worth running in
parallel per the round-12 "two distinct untried levers, field as a copy"
rule, since it is not obvious in advance which expansion is more tractable
for producing a clean, certifiable Lagrange-remainder bound (the polynomial
route avoids trig identities but the degree-(4,3) polynomials are messier;
the direct-`G` route is lower-degree but retains trig structure).
Skeleton: same as above, Step 3 replaced by an all-polynomial multivariate
Taylor expansion of `q1(σ,τ),r0(σ,τ)` around `(σ*,τ*):=(sin²A*,sin²β0(A*))`,
with the Lagrange remainder bounded via an explicit `mpmath.iv` box on the
second partials over `|σ−σ*|,|τ−τ*|≤δ'`.
Key lemmas: same corner-vanishing fact as above, restated in `(σ,τ)`
coordinates.
Open gaps: same as above, via the alternate polynomial route.
Cases to cover: none (same as sibling).
Watch out for: the `(A,B)↔(σ,τ)` domain-boundary translation must use the
SAME correct three-part domain (watch for a translation error introducing
spurious boundary artifacts, an easy way to accidentally reintroduce the
"drop the upper bound" bug from a different angle).

ptolemy-trig-identity: advance
Target: `OM=ON` via the entire ptolemy-trig-identity route — reduces (fully
certified, rounds 1-16) to the single remaining fact `Ψ(τ,A,C)>0` for all
`0<θ<min(B,C)` (`τ=tanθ`), equivalently `α+α'<A`, equivalently (certified
boxed identity, round 4) `F(p,x,y):=sinA(p+2x)(p+2y)−sinA−cosA(2p+2x+2y)>0`
where `p=cotθ,x=cotψ,y=cotφ`, with `x,y` each roots of explicit certified
quadratics (Step 2: `(III)′` `c1x²+b1x+a1=0`, `(IV)′` `c2y²+b2y+a2=0`, both
in terms of `p` and the fixed angles).
Technique: symmetric-function (Vieta) elimination — an untried, cheap lever
this round's explorer surfaced: substitute Vieta's formulas
`x+y=−b1/c1−b2/c2`-type... (more precisely, since `x,y` come from two
DIFFERENT quadratics, not one shared quadratic, the elimination is: treat
`F` as linear in each of `x,y` separately via its bilinear `(p+2x)(p+2y)`
structure, expand `F` fully in `x,y`, then substitute `x²=−(b1x+a1)/c1` (from
`(III)′`) and `y²=−(b2y+a2)/c2` (from `(IV)′`) to eliminate the SQUARE
terms, leaving a form linear in each of `x,y` — then use the two linear
relations plus known sign facts on `x,y`'s valid root (Step 3's already-
certified "exactly one of the two roots is valid" selection) to reduce to a
single inequality purely in `p` and the fixed angles A,B,C. This directly
extends the population's own memory-rule-8/9/13-style technique
(radical/root elimination via a certified quadratic), previously applied
via `U=cotα` to produce the transcendental `Ψ(τ,A,C)`; this is the first
attempt to eliminate through `x,y` directly instead.
Skeleton:
  1. Expand `F(p,x,y)=sinA(p²+2p(x+y)+4xy)−sinA−cosA(2p+2x+2y)` fully —
     by direct algebra (already boxed, round-4 identity).
  2. Use `(III)′,(IV)′` to write `x²`-degree terms... note `F` itself has no
     `x²,y²` term (only `xy`, linear `x`, linear `y`) — so no direct
     substitution of the quadratics' `x²/y²` terms is needed for `F` itself;
     the real lever is: **the valid root selection** (round 5/6's certified
     "which of the two roots is the genuine `cotψ`/`cotφ`" fact) pins `x,y`
     to explicit closed-form expressions `x=x(p;A,B,C)`, `y=y(p;A,B,C)` via
     the quadratic formula — substitute THESE closed forms (not a Vieta
     symmetric-function shortcut, since `F` is bilinear in `x,y`, not
     symmetric) directly into `F`, producing a single explicit function of
     `p` and the fixed angles A,B,C, radical-free after the standard
     "isolate one radical, square" step (already the population's certified
     technique, `radical-isolation-equals-psi.md`).
  3. Determine the resulting 1-variable-in-`p` target's sign on the correct
     domain (`p=cotθ` ranges over `cot(min(B,C))<p<+∞`, per the certified
     domain facts) — by an IVT + degree-counting or direct sign-of-leading-
     coefficient argument (reuse the population's certified
     `pointwise-branch-selection-criterion.md`/`ray-angle-determines-cyclic-
     order.md` style tools if the resulting polynomial is low-degree enough).
  4. Conclude `F>0` hence `Ψ>0` hence `α+α'<A` hence (already certified,
     round 1-4's general-Ptolemy-equality theorem) `OM=ON`.
Key lemmas (claim + mechanism):
  - The valid-root closed form for `x,y` in terms of `p` (already certified,
     Steps 2-3, "exactly one of the two roots is genuine") is directly
     substitutable into `F` — because `F` was constructed (round 4) exactly
     as a function of `x,y` alone (no other free variables), so no new
     elimination machinery is needed beyond the ALREADY-certified quadratic
     roots — this is why the lever is cheap: it reuses existing certified
     content, it does not require re-deriving anything.
  - The resulting 1-variable target is lower-effective-dimension than the
     existing `Ψ(τ,A,C)` (degree-6-in-τ, transcendental coefficients in
     A,C) — because it comes from a DIFFERENT elimination path (`x,y`
     directly, not through `U=cotα`), so it may have a genuinely different,
     more tractable algebraic shape even though it targets the same fact.
Open gaps: Step 2's substitution has not been carried out symbolically by
any file yet (the whole point of this lever); Step 3's sign determination on
whatever polynomial results.
Cases to cover: none beyond the existing branch-selection case split
(already certified, Steps 2-3).
Watch out for: `F` is NOT symmetric in `x,y` in general (check this
explicitly before assuming a symmetric-function shortcut works) — the
correct substitution is via each variable's own explicit closed form from
its OWN quadratic, not a shared Vieta symmetric-function trick across two
different quadratics; verify the closed forms for `x` and `y` use the
CORRECT valid root (not just any root) per the already-certified selection
criterion, or the resulting inequality will be for the wrong geometric
configuration.

spiral-similarity-bootstrap: revise
Target: `OM=ON` via the certified reduction `OM=ON ⟺ A,K,L,Q` concyclic,
where `Q` = reflection of `A` in the perpendicular bisector of `MN`
(certified, `amnq-concyclic-and-reduction.md`) = foot of perpendicular from
`O_{ABC}` onto the line through `A` parallel to `BC` (certified, `q-as-foot-
of-perpendicular-from-circumcenter.md`) = **NEW, simpler characterization
found this round**: the intersection of (line through `A` parallel to `BC`)
with (perpendicular bisector of `BC`) — equivalently, `Q` lies on the
perpendicular bisector of `BC`, giving `QB=QC` as a directly usable
elementary fact with no circumcenter arithmetic required. Re-plan the
concyclicity gap (dead-ended on 5 tested radical-axis/Miquel guesses and one
tested general-lemma point-assignment, all this round) using this new
lever.
Technique: directed-angle chase anchored at `Q`, using the inscribed-angle
criterion `∠(QK,QA)=∠(LK,LA)` (equivalently Ptolemy/cyclic-quadrilateral
criterion), now armed with the isosceles fact `QB=QC` (⟹ `∠QBC=∠QCB`) as an
additional equal-angle pair to feed into the chase alongside the two
already-certified lemmas (Lemma A: `∠BLN=∠(BK,AC)` from H2; Lemma B:
`∠CKM=∠(CL,AB)` from H3) and their Corollary (`∠BLN+∠CKM≡0 mod π` from H1).
Skeleton:
  1. Adopt the simpler definition: `Q:=`(line through `A`∥`BC`)∩(perp.
     bisector of `BC`) — by the elementary two-line argument this round's
     explorer sketched (the perpendicular from `O_{ABC}` to the parallel
     line through `A` has direction ⟂ `BC`, i.e. is exactly the `BC`-
     perpendicular-bisector direction through `O_{ABC}`, so the foot lies on
     both lines at once). Prove this rigorously (currently a sketch, not a
     full write-up) — cheap, short, elementary.
  2. Establish `∠QBC=∠QCB` from `QB=QC` — trivial isosceles-triangle fact.
  3. Chase: express `∠(QK,QA)` and `∠(LK,LA)` each in terms of the base
     angles B,C, the free parameter `φ`, and the H1-H2-H3-derived relations
     (Lemma A, Lemma B, Corollary), using `∠QBC=∠QCB` to relate `Q`'s
     position angularly to `B,C` without needing `O_{ABC}` or any
     circumradius computation.
  4. Show the two expressions are equal for every valid `φ` — by direct
     angle arithmetic using only the certified relations plus `∠QBC=∠QCB`
     — concluding `A,K,L,Q` concyclic via the inscribed-angle criterion.
  5. Combine with the certified reduction to conclude `OM=ON`.
  Alternative mechanism for Step 3-4 (untried lever, from this round's
  synthetic explorer): **inversion centered at `Q`** — maps the target
  concyclicity of `A,K,L,Q` to collinearity of the images `A',K',L'` (since
  a circle through the center of inversion maps to a line) — potentially
  turning an angle-chase into a simpler collinearity/cross-ratio check using
  the already-certified `H1-H3` relations transported through the inversion.
  Also untried: a systematic (not single-guess) sweep of point assignments
  `(P,Q,X,Y,Z)` in the certified general one-angle lemma applied to H1 (only
  one assignment, `(B,C,A,K,L)`, was tested this round and found false,
  giving a `φ`-dependent `2φ` gap, not a fixed relation) — several other
  assignments remain untried and should be swept cheaply (numerically first,
  per the round-9 memory rule: check `φ`-independence before investing in a
  hand proof) before the angle-chase-at-`Q` route is attempted in full.
Key lemmas (claim + mechanism):
  - `QB=QC` — because `Q`, defined via the perpendicular from `O_{ABC}`,
     lies on the line through `O_{ABC}` perpendicular to `BC` (a diameter
     line of the circumcircle, hence exactly the perpendicular bisector of
     `BC`) by construction, not merely numerically — this round's explorer
     verified it to machine precision but the short synthetic argument (the
     perpendicular-direction coincidence) has not yet been written up
     rigorously; that write-up is Step 1's open gap.
  - The general one-angle lemma, correctly re-assigned (an untried
     assignment), may give a direct fixed-angle relation from H1 the way
     Lemmas A/B already do from H2/H3 — because the lemma's mechanism (an
     algebraic chain-rule argument on directed angles, already certified in
     general form) does not depend on which of the 3 hypotheses it is fed,
     only on correctly matching the lemma's abstract points to H1's concrete
     ones; the one assignment tried failed, but the lemma itself is generic.
Open gaps: Step 1 (rigorous proof of the simpler `Q` characterization, cheap
but not yet written); the whole angle chase Steps 3-4 (not yet attempted
with `QB=QC` as an ingredient); the inversion-at-`Q` alternative (wholly
untried); the systematic point-assignment sweep for the general lemma vs H1
(only 1 of many assignments tested).
Cases to cover: none additional — this is a single synthetic fact, no
casework, though the chase must be verified for the whole 1-parameter family
of valid `(K,L,φ)`, not just one instance (per the round-1 memory rule on
underdetermined systems).
Watch out for: (i) do not conflate `Q` with `A*` (the classical arc-
reflection point on the circumcircle) — confirmed this round to be a
DIFFERENT point despite both lying on the line through `A` parallel to
`BC`; (ii) before investing in a hand proof of any new angle relation
(inversion images, a new lemma assignment), first check numerically that it
is `φ`-independent (vary `φ` holding the triangle fixed) — a cheap filter
that already caught one false lead this round (the `2φ`-drifting
assignment).

coordinate-bash-resultant-boundary-pointwise-sos: advance (dormant, no build slot)
Target: unchanged (`Num≥0`/4-generator Positivstellensatz for the
`u=tan(A/6)`-encoded route). Not fielded for a build slot this round: this
round's `T-positivstellensatz` explorer's structural finding (`T=0` exactly
attained at a genuine domain corner, forcing a linear-vanishing
complementary-slackness rank deficiency in ANY Gram-matrix decomposition,
reproducible at any degree) explains this route's own repeatedly-observed
SDP degeneracy too (both are Positivstellensatz searches on closely-related
trigonometric domain targets hitting the same phenomenon). Recommend no
further SDP/SOS search dispatched on this route this round; if revived,
it should adopt the SAME local-Taylor-near-corner reframing as the
`-pointwise-tangent` route above, not another solver attempt.
