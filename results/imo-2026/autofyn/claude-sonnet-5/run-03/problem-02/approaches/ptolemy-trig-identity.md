## Status
partial

## Approaches tried
- **Round 8 (this round).** Dispatch: attack the `Ψ>0`/`F(p,x,y)>0` gap via a
  "cheap, untried lever" — substitute the certified closed-form roots
  `x=cotψ,y=cotφ` of the two certified quadratics `(III)′,(IV)′` directly
  into the boxed `F(p,x,y)` identity, eliminating `x,y` via Vieta to get a
  radical-free target purely in `p=cotθ`. **Result: proved (not merely
  observed numerically) that this lever, taken as literally proposed, is
  algebraically IDENTICAL to the already-exhausted `U=cotα` resultant route
  — `F(p,x,y)` with genuine `x,y` and `F(U,V)` with genuine `U=p+2x,V=p+2y`
  are the same real number by construction (Round 4/5's own certified
  identities), so eliminating `x,y` via a resultant cannot produce a new
  target beyond the already-open `Ψ(τ,A,C)` sextic — correcting the
  outline's premise.** Constructed instead a genuinely different, cheaper
  radical-free object: a four-branch resolvent quartic `P(t)` (Step 1, full
  proof, `sympy`-verified exactly) whose four roots are `F`'s four sign-branch
  values; verified at 8 diverse domain samples (own fresh `mpmath`, `dps=50`)
  that `P(t)` always has exactly 3 negative and 1 positive real root, the
  positive one matching the genuine branch's `F`-value to 40+ digits — but
  this root-count property is **not proved** for the whole domain (Step 2),
  so **Status remains `partial`**; the chain from this new resolvent quartic
  to `OM=ON` is not closed, and no gap actually closes this round — the
  contribution is (i) a correct negative/clarifying finding about the
  dispatched lever and (ii) an honestly-reported, unclosed, genuinely new
  candidate sub-target (the resolvent's root-count) plus a fully reusable
  general lemma (the resolvent construction itself). See "Round 8" section in
  Current best for the full derivation.
- **Round 7.** Dispatch: pursue the `Ξ(V1)·Ξ(V2)<0` sufficiency
  route (paritylens's finding) by isolating the single radical in `Ξ(V1)` and
  closing via an `a²≷b²Δ2` comparison plus IVT/continuity on the certified
  connected domain. **Result: a new, fully proved closed-form sign fact for
  `Ξ(V)`'s leading coefficient, plus a rigorous — and honestly negative —
  structural finding that closes off this specific route: the `a²≷b²Δ2`
  comparison the outline proposed is not a new, easier target at all, it is
  provably (via an exact algebraic identity derived here) EXACTLY the
  already-open `Ψ>0` claim in disguise, up to an explicit, sign-determined
  positive/negative multiplicative constant.** Status remains `partial`. See
  "Round 7" section in Current best for the full derivation. This narrows the
  search: any future attempt at this approach's remaining gap must engage
  with `Ψ`'s sign directly (or an equally powerful reformulation), since the
  "clear the radical and compare squares" trick, applied to `Ξ(V1)` alone,
  cannot furnish a genuinely simpler sufficient condition — it algebraically
  reconstructs the full four-branch product.
- **Round 6 (this round).** Dispatch: prove `Ψ(τ,A,C)>0` on the true bounded
  domain `0<θ<min(B,C)` via root-counting (Sturm/Descartes) plus the
  boundary value, per this round's outline reframing (global SOS refuted by
  the sextic-lens explorer). **Result: a genuinely new and fully proved
  algebraic identity that reduces `Ψ>0` from a degree-6 coefficient-sign
  problem to an explicit 4-term combinatorial sign claim, but that final
  claim is not closed this round — Status remains `partial`.** Attempted
  the dispatched Sturm/Descartes route on Ψ's raw coefficients first and
  found it computationally intractable in reasonable time (documented
  below as a genuine, informative negative result — the coefficients only
  simplify to a clean polynomial after reducing modulo the Pythagorean
  ideal `sin²+cos²=1` for *both* A and C, which is a nontrivial
  Gröbner-basis computation, not a routine `sympy.expand`). Pivoted to a
  structural route instead: proved (full derivation below, independently
  numerically verified) that `Res_U(q_1,\Phi)` — the exact quantity whose
  factorization defines Ψ (certified lemma
  `ptolemy-resultant-elimination-to-sextic.md`) — equals, **as an exact
  algebraic identity via resultant multiplicativity**, `\tilde P_1^2\tilde
  P_2^2` times the product of `F(U_i,V_j)-4` over all four combinations of
  the two roots of each quadratic. Combined with a clean, fully elementary
  sign determination of the two known spurious linear factors (redone here
  more directly than Round 5's version, and shown to *simultaneously* give
  a cleaner proof that `\tilde P_1,\tilde P_2<0` throughout the domain),
  this yields: **`Ψ(τ,A,C)>0` on the domain `\iff` an odd number
  (1 or 3) of the four real numbers `F(U_i,V_j)` exceed `4`.** This is a
  strictly sharper, more tractable, and more geometrically meaningful
  target than the raw sextic — verified (fresh, independent numerical
  check, 8 random domain samples plus a `τ→0` limit check reproducing the
  already-certified exact value `Ψ(0,A,C)=4\sin^3A\sin B\sin C`) to
  reproduce the population's known dichotomy exactly: at every sample, the
  genuine branch `(U_1,V_1)` alone exceeds `4` and the other three do not
  (odd count `=1`), matching Round 4's independent 100,000-sample
  diagnostic finding. **This parity/sign claim for the four branches is
  the new sharply-isolated open gap** — not proved symbolically this round
  (see "What remains" below for the precise, narrower target it leaves).
  Also noted, as a byproduct, that the boundary value `Ψ(0,A,C)` (already
  exactly proven) is a limit point of the domain's closure, so it can serve
  as an *exact* (not 60-digit-numerical) IVT anchor once interior
  non-vanishing is established — a small improvement over Round 5's
  numerical base point, contingent on the same open gap.
- **Round 5.** Dispatch: prove `F(θ,A,B,C)>4` symbolically (not
  just numerically) via a blow-up/Taylor analysis near `A→0` and whatever
  algebraic structure can be found, closing this approach's sole remaining
  gap. **Result: substantial new structural progress, gap narrowed sharply
  but not fully closed — Status remains `partial`.** Found and proved (full
  derivation below) a genuinely new reduction: a *direct* quadratic
  `P̃₁U²+Q̃₁U+R̃₁=0` for `U:=cotα` itself (no longer routed through `cotψ`),
  with explicit, clean, closed-form coefficients in `τ:=tanθ,A,B,C` — proved
  by exact algebraic substitution from the already-certified quadratic for
  `cotψ` (Steps 2–3), and independently re-verified numerically to
  `<3×10⁻¹²` absolute error over 2000 random configurations. Using this,
  performed a **two-step resultant elimination** (successively eliminating
  `V:=cotα'` then `U` from the system `{q₁(U)=0, q₂(V)=0, F(U,V)=4}`) to
  reduce the *entire* two-nested-square-root inequality `F>4` to a single
  **radical-free** polynomial positivity claim `Ψ(τ,A,C)>0` (degree 6 in
  `τ`) — a genuine simplification in kind, not just in numerology. Proved
  rigorously (not numerically) that the two spurious linear factors
  produced by the elimination (`τcosC−sinC` and `sinB−τcosB`) are
  **exactly** the domain-boundary loci `θ=C`, `θ=B`, hence never vanish on
  the open domain `0<θ<min(B,C)` — so `Ψ=0` is the *only* possible zero
  locus of the full resultant inside the domain. Proved the domain is
  path-connected (elementary topology). This yields a **complete strategy**
  reducing `F>4` (genuine branch, everywhere) to exactly two remaining
  ingredients: (a) `Ψ(τ,A,C)>0` for all valid `(τ,A,C)` — proved so far only
  at `τ=0` exactly (`Ψ(0,A,C)=4\sin^3A\sin C\sin B>0`, a fully symbolic
  proof) plus strong numerical support elsewhere (20,000 random samples,
  zero violations, min found `≈2.6×10⁻⁶`, vanishing only in the known
  `A→0` limit); (b) one confirmed sample point with `F>4` on the genuine
  branch, established to 60 correct decimal digits (not yet a symbolic
  closed-form proof) at the equilateral/mid-angle configuration. **Neither
  (a) nor (b) is fully closed symbolically this round** — `Ψ>0` remains
  the honest single open gap (down from a two-radical mess to one
  radical-free sextic), and the base point is numerical (60 digits) rather
  than symbolic. No overclaiming: Status remains `partial`. See "Round 5"
  section in Current best for the full derivation.
- **Round 4 (this round).** Dispatch: close `∠BAK<∠BAL` using the explorer's
  new `cot α = cot θ + 2 cot ψ` identity. **Result: real further progress,
  not fully closed.** (1) Proved the K/L-order gap collapses to one clean,
  case-split-independent claim `α+α'<A` (resolving Round 3's "self-dual"
  puzzle: it's self-dual because it's genuinely one symmetric claim, not
  two). (2) Proved (III), (IV) are each *exactly* a quadratic in `cot ψ`,
  `cot φ` (no squaring, fully rigorous) — replaces implicit transcendental
  root-finding with an explicit closed form. (3) Proved, via a clean
  IVT + quadratic-degree argument (no numerics needed for the proof itself,
  though independently confirmed on 199441 samples), a full branch-selection
  theorem: the genuine root is the unique one in `(0,C-θ)` — a genuine
  strengthening over the whole population's still-open branch-selection gap
  elsewhere. (4) The final positivity claim this reduces to (Step 4 in
  Current best) was verified over 500,000 samples with substantial margin
  (min ≈11.3) but **not proved symbolically** — sympy's direct simplification
  did not terminate; isolating and clearing the two square roots one at a
  time was identified as the most promising next step but not attempted.
  This positivity claim is now the single remaining gap for the whole
  approach. See "Round 4" section in Current best for full detail.
- **Round 3 (this round).** Two targeted pushes, per dispatch: (1) prove the
  AB-vs-AC case split synthetically instead of from two numerical examples;
  (2) derive closed forms for KQ, LQ and complete the trig identity check.
  **Result on (1): substantially advanced, not fully closed.** Found and
  proved in full a genuinely new synthetic mechanism — a "ray-angle
  determines cyclic order" lemma (any point P on a circle through A is
  ordered around the circle exactly as the direction-angle of ray AP is
  ordered; proved via an explicit unit-circle computation, similarity-
  invariant) — combined with a clean closed form for the direction angle of
  AQ (namely π−B or −B, according to sign(b−c), derived from the standard
  projection identity c = a cos B + b cos A) and a containment bound
  (0 < ∠BAK, ∠BAL < A, immediate from K ∈ triangle BMC ⊆ ABC, L ∈ triangle
  BNC ⊆ ABC). Together these give a **fully rigorous proof that Q is always
  the angularly extreme point of {K,L,Q} as seen from A** — first (adjacent
  to A) if AB > AC, last if AB < AC — with NO numerical input. This was
  checked against the sign-lemma explorer's Part A cross-product technique
  as instructed, and found (as the explorer itself flagged) to be a
  genuinely different mechanism (this is a ray-angle/circle-order argument,
  not a cross-product/rotation-direction argument); the reuse instruction is
  answered honestly: the two mechanisms do not merge, a fresh argument was
  needed and is given here. **The one piece still not closed**: the case
  split needs, in addition to Q's extremal position, the relative order of
  K and L themselves (∠BAK vs ∠BAL) — proved to matter algebraically (the
  two orders give two different Ptolemy identities), and found by an
  extended numerical sweep (9 distinct triangles — acute, obtuse-at-A,
  thin/near-degenerate, near-isosceles — and ~10 θ values each, ~90 configs
  total, 0 counterexamples) to always satisfy ∠BAK < ∠BAL, but this specific
  inequality resisted a same-round synthetic proof attempt (tried: direct
  comparison via the Lemma 2 tan-formulas for α, α′; tried: deriving it as a
  σ-image of itself, found self-dual/uninformative). This is now the single,
  precisely isolated remaining gap for the case split — much narrower than
  round 2's "case split governed by sgn(AB−AC), numerically only" statement.
  **Result on (2): closed forms for KQ, LQ fully derived and independently
  verified.** Using AK, AL (Lemma 2), AQ = |b²−c²|/(2a) (Lemma 4), and the
  now-derived angles ∠KAQ = |∠BAK − q|, ∠LAQ = |∠BAL − q| (q := the direction
  angle of AQ from AB, = π−B or −B), the Law of Cosines gives explicit closed
  forms for KQ, LQ in the θ-parametrization. These were verified numerically
  to machine precision (< 2×10⁻¹⁵ absolute) against direct coordinate
  distances on 3 independent triangles × 3 θ values, and the full Ptolemy
  identity (using these closed-form KQ, LQ together with the closed-form AK,
  AL, KL, AQ) was verified to machine precision (< 10⁻¹⁴) via this route —
  an independent re-confirmation of round 2's finding, now via the fully
  explicit closed-form recipe rather than only via direct coordinate
  construction. **This is not yet a symbolic algebraic proof** of the
  identity (substituting the transcendental constraints (III), (IV) and
  reducing to 0 = 0 symbolically was not completed — the resulting
  expression, after eliminating ψ, φ via (III)/(IV), is a genuinely hard
  multi-term trigonometric identity in θ and the fixed angles A,B,C; sympy
  simplification was not attempted to completion in the time available), so
  the "prove, don't conjecture" line is not yet crossed for the length
  identity itself — but the KQ, LQ closed forms themselves ARE now fully
  proved (Law of Cosines from already-proved ingredients), which is new,
  reusable, honest progress, not merely a numeric check.

- **Round 1 (built from scratch — the outline file did not yet
  exist).** Followed the outliner's Ptolemy/Law-of-Sines plan, importing the
  two certified reduction lemmas (`lemmas/vector-reduction-OM-ON.md`,
  `lemmas/amnq-concyclic-and-reduction.md`). Made four pieces of genuine,
  verified progress beyond anything in the population so far:
  1. Proved a general, self-contained **Ptolemy equality ⟹ concyclic-or-collinear
     theorem** via complex numbers (full proof below), which removes the need
     for the outline's Step 2 ("prove the cyclic order A,K,L,Q synthetically")
     entirely — concyclicity does not care about vertex order, only the
     specific *pairing* used in the length identity does, and that pairing's
     correctness follows automatically from equality in the general Ptolemy
     inequality, with no separate order-lemma needed.
  2. **Found and corrected an error in the outline's target identity.** The
     outline asserted a single fixed target `AL·KQ = AK·LQ + KL·AQ`. Direct
     numerical construction of the configuration (see Key computations below)
     on two different scalene base triangles shows this pairing is correct
     on one triangle (`AC > AB`) but **wrong** on the other (`AB > AC`, where
     the correct identity is instead `AK·LQ = KL·AQ + AL·KQ`) — residual
     ≈ −0.09, not ≈0, confirming the outline's fixed pairing is false in
     general. The correct statement requires a case split on sgn(AB−AC),
     and the two cases are exchanged by the already-certified σ-symmetry
     (swap B↔C, K↔L, M↔N, `lemmas/sigma-symmetry.md`-style symmetry,
     independently re-derived here). This is important negative information:
     any future attempt assuming the outline's fixed pairing will fail on
     roughly half of all scalene triangles.
  3. **Derived and numerically verified a fully explicit, decoupled
     parametrization** of the whole configuration by one free angle θ
     (matching the family's confirmed one degree of freedom), reducing the
     three angle hypotheses to two independent, single-variable transcendental
     equations (III), (IV) below (one in θ,ψ only, one in θ,φ only) — far
     simpler than coordinate-bash's coupled 4-variable polynomial system.
  4. **Derived closed-form lengths** AK, BK, AL, CL (via Law of Sines) and
     AQ (via an explicit coordinate computation), all independently
     numerically verified to machine precision on two different triangles
     (see Key computations).
  The remaining gap — verifying the (now correctly stated, case-split) Ptolemy
  identity holds given constraints (III)–(IV), and completing closed forms for
  KQ, LQ — was not closed this round; see Current best for the precise
  statement of what remains.

## Current best

### Setup and imported lemmas
Let ABC be the triangle, M, N midpoints of AB, AC, and A the origin of
position vectors as needed. Write a = BC, b = CA, c = AB, and A, B, C also for
the triangle's interior angles at those vertices (context disambiguates).

Import verbatim (no re-proof):
- **Lemma R (vector reduction)**: `OM = ON ⟺ O·(C−B) = (|C|²−|B|²)/4`
  (`lemmas/vector-reduction-OM-ON.md`).
- **Lemma Q1 (Q's characterization)**: Q := the unique point with AQ ∥ BC and
  QB = QC (equivalently, reflection of A in the perpendicular bisector of MN);
  A, M, N, Q are concyclic (`lemmas/amnq-concyclic-and-reduction.md`,
  Lemma A).
- **Lemma Red (reduction)**: if A, K, L, Q are concyclic (in *any* order —
  order plays no role in this lemma), then OM = ON, provided A ≠ Q, i.e.
  AB ≠ AC (`lemmas/amnq-concyclic-and-reduction.md`, Lemma B; the case
  AB = AC is the shared isosceles gap, not resolved by any approach in the
  population, and not resolved here either — see Cases below).

By Lemma R + Lemma Red, **it suffices to prove A, K, L, Q are concyclic**
(for AB ≠ AC); this is the target of everything below.

### Angle notation for the hypotheses
Let θ := ∠KBA = ∠ACL (hypothesis 1). Since K lies inside ∠LBA, ∠ABL = θ + φ
where φ := ∠LBK (hypothesis 2's left side). Since L lies inside ∠ACK,
∠ACK = θ + ψ where ψ := ∠LCK (hypothesis 3's left side). Hypotheses 2, 3
assert φ = ∠LNC and ψ = ∠BMK.

### Lemma 1 (Explicit two-ray construction of K, L)
K is the unique point that is the intersection of: the ray from B making
angle θ with ray BA (on the C-side of line AB), and the ray from C making
angle θ+ψ with ray CA (on the B-side of line AC). Symmetrically, L is the
intersection of the ray from B making angle θ+φ with BA, and the ray from C
making angle θ with CA.

*Proof.* By definition, ∠KBA = θ and ∠ACK = θ+ψ (derived above), which are
exactly the two ray conditions; two non-parallel rays from distinct points B,
C meet in at most one point, and K is that point (existence is given by
hypothesis — K is a genuine point of the configuration). The argument for L
is symmetric, using ∠ACL = θ and ∠ABL = θ+φ. ∎

### Lemma 2 (Explicit lengths AK, BK, AL, CL)
In triangle BKC: ∠KBC = B − θ, ∠KCB = C − (θ+ψ), ∠BKC = A + 2θ + ψ (these sum
to π since B+C=π−A). By the Law of Sines in triangle BKC and in triangle ABC
(a/sin A = b/sin B = c/sin C):
$$BK = \frac{a\,\sin(C-\theta-\psi)}{\sin(A+2\theta+\psi)}.$$
Also, in triangle ABK (∠ABK = θ, ∠BAK = α for some α determined by K),
BK = c·sinα/sin(θ+α) and AK = c·sinθ/sin(θ+α) by the Law of Sines. Eliminating
BK between the two expressions and using c = a·sinC/sinA (Law of Sines in
ABC) gives
$$\frac{\sin\alpha}{\sin(\theta+\alpha)} = \frac{\sin A}{\sin C}\cdot\frac{\sin(C-\theta-\psi)}{\sin(A+2\theta+\psi)} =: R(\theta,\psi). \qquad (\mathrm{I})$$
Solving (I) for α (write R = R(θ,ψ)): expanding sin(θ+α) = sinθcosα+cosθsinα
and dividing by cosα gives sinα(1 − R\cosθ) = R\sinθ\cosα, i.e.
tan α = R\sinθ/(1−R\cosθ), an explicit closed form for α, hence for
$$AK = \frac{c\sin\theta}{\sin(\theta+\alpha)}.$$
By the mirror argument (triangle CLB in place of BKC, triangle ACL in place
of ABK, roles of B,C and b,c swapped):
$$CL = \frac{a\,\sin(B-\theta-\phi)}{\sin(A+2\theta+\phi)}, \qquad
\frac{\sin\alpha'}{\sin(\theta+\alpha')} = \frac{\sin A}{\sin B}\cdot\frac{\sin(B-\theta-\phi)}{\sin(A+2\theta+\phi)} =: R'(\theta,\phi), \qquad (\mathrm{II})$$
$$\tan\alpha' = \frac{R'\sin\theta}{1-R'\cos\theta}, \qquad AL = \frac{b\sin\theta}{\sin(\theta+\alpha')}.$$
*Proof.* All steps are direct Law-of-Sines computations in the three
triangles BKC, ABK (resp. CLB, ACL) as set up, using only that the angle sums
of BKC and ABC are π. No hypothesis 2 or 3 content is used yet — this lemma
only encodes hypothesis 1 and the containment/ray structure. ∎
**Independently verified numerically** (script output, two different
triangles, several θ): AK, BK match the direct coordinate distances to full
double precision (see Key computations).

### Lemma 3 (The decoupled constraint equations)
Using triangle BMK (∠MBK = θ, since M lies on ray BA; ∠BMK = ψ by hypothesis
3; BM = c/2) and the Law of Sines there: BK = (c/2)·sinψ/sin(θ+ψ). Equating
with BK = c·sinα/sin(θ+α) from Lemma 2 gives 2 sinα/sin(θ+α) = sinψ/sin(θ+ψ);
substituting (I)'s value of sinα/sin(θ+α) = R(θ,ψ) gives
$$\frac{\sin\psi}{\sin(\theta+\psi)} = 2\,\frac{\sin A}{\sin C}\cdot\frac{\sin(C-\theta-\psi)}{\sin(A+2\theta+\psi)}. \qquad (\mathrm{III})$$
Symmetrically, using triangle CNL (∠NCL = θ, ∠LNC = φ by hypothesis 2,
CN = b/2):
$$\frac{\sin\phi}{\sin(\theta+\phi)} = 2\,\frac{\sin A}{\sin B}\cdot\frac{\sin(B-\theta-\phi)}{\sin(A+2\theta+\phi)}. \qquad (\mathrm{IV})$$
(III) involves only θ, ψ (and the fixed angles A, C); (IV) involves only θ, φ
(and A, B) — the two hypotheses decouple completely, each pinning one of
ψ, φ as an (implicit, transcendental) function of θ alone. Swapping B↔C
(hence b↔c) turns (III) into (IV) and vice versa — this is the σ-symmetry
already found by `coordinate-bash`, re-derived independently here in angle
variables.

*Proof.* Given above; ∠MBK = ∠ABK = θ because M lies on segment AB, so ray BM
= ray BA. ∎ **Numerically verified**: solving (III) for ψ given θ (via
root-finding) and reconstructing K from Lemma 1 reproduces ∠BMK = ψ to full
double precision on two different triangles and five values of θ each (Key
computations).

### Lemma 4 (Closed form for AQ)
$$AQ = \frac{|b^2-c^2|}{2a}.$$
*Proof.* With A at the origin, Lemma Q1 gives Q = t(C−B) for the scalar t
solving Q·(C−B) = (|C|²−|B|²)/2 (perpendicular bisector of BC), i.e.
t|C−B|² = (b²−c²)/2 (since |C|=b, |B|=c), so t = (b²−c²)/(2a²) (using
|C−B|=a). Hence AQ = |t|·|C−B| = |b²−c²|/(2a²)·a = |b²−c²|/(2a). ∎
**Independently verified numerically** to match Lemma Q1's vector formula for
Q to full double precision.

### The corrected Ptolemy target
**Claim.** If AB > AC (c > b): $AK\cdot LQ = KL\cdot AQ + AL\cdot KQ$.
If AB < AC (c < b): $AL\cdot KQ = AK\cdot LQ + KL\cdot AQ$ (the outline's
original form). These two cases are exchanged by the σ-symmetry B↔C, K↔L
(which also swaps b↔c and hence the sign of b−c), so **it suffices to prove
one case**; the other follows by applying the (already-verified) symmetry.

### Round 3: a synthetic (not merely numerical) derivation of most of the case split

**Notation.** With A at the origin, let $q$ denote the direction angle of
ray AQ measured from ray AB (i.e. the signed angle $\angle(AB,AQ)$, using
the orientation convention that CCW is positive when triangle ABC is CCW).
Let $\alpha := \angle BAK$ (signed, same convention) and
$\beta_L := \angle BAL$ (so, in the notation of Lemma 2, $\beta_L = A-\alpha'$
where $\alpha' = \angle CAL$).

**Lemma S1 (ray-angle determines cyclic order).** *Let $\omega$ be a circle
and $A \in \omega$ a fixed point. For $P \in \omega \setminus \{A\}$, let
$\theta(P)$ denote the direction angle of ray $AP$ (a well-defined real
number modulo $2\pi$, i.e. an honest angle of a vector, no ambiguity). Then
as $P$ traverses $\omega$ once starting immediately after $A$ (in a fixed
rotational sense) and ending immediately before returning to $A$, $\theta(P)$
is a strictly monotonic (increasing, for the CCW traversal sense) function
of the arc-position of $P$, sweeping through a net total angle of exactly
$\pi$. Consequently, for any three points $P_1,P_2,P_3 \in \omega\setminus\{A\}$,
their cyclic order around $\omega$ (starting from $A$) equals their order by
increasing $\theta(P_i)$.*

*Proof.* Since angles of rays and cyclic order are invariant under rotation,
translation, and positive scaling, we may place $\omega$ as the unit circle
centered at the origin with $A=(1,0)$. For $P = (\cos\varphi,\sin\varphi)$,
$\varphi \in (0,2\pi)$ (parametrizing $\omega\setminus\{A\}$, with increasing
$\varphi$ the CCW traversal starting just after $A$), the vector
$P - A = (\cos\varphi - 1, \sin\varphi)$. Using the half-angle identities
$\cos\varphi - 1 = -2\sin^2(\varphi/2)$ and $\sin\varphi = 2\sin(\varphi/2)\cos(\varphi/2)$:
$$P - A = 2\sin(\varphi/2)\,\bigl(-\sin(\varphi/2),\ \cos(\varphi/2)\bigr).$$
For $\varphi \in (0,2\pi)$, $\varphi/2 \in (0,\pi)$ so $\sin(\varphi/2) > 0$;
hence $P-A$ is a positive scalar multiple of
$(-\sin(\varphi/2),\cos(\varphi/2)) = (\cos(\varphi/2+\pi/2),\sin(\varphi/2+\pi/2))$,
so $\theta(P) = \varphi/2 + \pi/2$. This is strictly increasing in $\varphi$
on $(0,2\pi)$, ranging over $(\pi/2, 3\pi/2)$ — an interval of length exactly
$\pi$ — confirming the claim. Since $\theta$ is strictly monotonic in the
arc-position, sorting any finite set of points by $\theta$ recovers exactly
their order along the traversal, i.e. their cyclic order starting from
$A$. ∎

**Lemma S2 (direction of AQ).** With $A$ at the origin, $B=(c,0)$,
$C=(b\cos A, b\sin A)$ (standard position, CCW orientation, $A$ also
denoting the angle of the triangle at vertex $A$): the direction angle of
$C - B$ equals $\pi - B$ (where $B$ here also denotes the triangle's angle
at vertex $B$). Consequently $q = \pi - B$ if $b>c$, and $q \equiv -B\ (\mathrm{mod}\ 2\pi)$
if $b<c$ (using Lemma 4's proof that $Q = A + t(C-B)$, $t=(b^2-c^2)/(2a^2)$,
so ray $AQ$ has direction $C-B$ when $t>0$ i.e. $b>c$, and direction $B-C$
when $t<0$ i.e. $b<c$).

*Proof.* We use the standard **projection identity** $c = a\cos B + b\cos A$
(valid in every triangle): by the Law of Sines $a = 2R\sin A$, $b=2R\sin B$,
$c=2R\sin C$ for the circumradius $R$, so
$$a\cos B + b\cos A = 2R(\sin A\cos B + \sin B\cos A) = 2R\sin(A+B) = 2R\sin(\pi - C) = 2R\sin C = c.$$
Then $b\cos A - c = b\cos A - (a\cos B + b\cos A) = -a\cos B$, and by the Law
of Sines $b\sin A = a \sin B$ (from $a/\sin A = b/\sin B$). Hence
$$C - B = (b\cos A - c,\ b\sin A) = (-a\cos B,\ a\sin B) = a\bigl(\cos(\pi-B),\ \sin(\pi-B)\bigr),$$
a positive multiple of $(\cos(\pi-B),\sin(\pi-B))$, so its direction angle is
$\pi - B$ exactly. The two cases for $q$ follow immediately since direction
angle of $B-C$ is $(\pi-B)+\pi \equiv -B\ (\mathrm{mod}\ 2\pi)$. ∎

**Lemma S3 (containment bounds).** $0 < \alpha < A$ and $0 < \beta_L < A$.

*Proof.* By hypothesis $K$ is an interior point of triangle $BMC$, and
$M \in$ segment $AB$, so triangle $BMC \subseteq$ triangle $ABC$ (it is cut
off from $ABC$ by cevian $CM$). Hence $K$ is an interior point of triangle
$ABC$; in particular $K \notin$ ray $AB$ and $K \notin$ ray $AC$, so ray $AK$
lies strictly between ray $AB$ and ray $AC$, i.e. $0 < \angle BAK < \angle BAC = A$.
The identical argument with $N \in$ segment $AC$, triangle $BNC \subseteq$
triangle $ABC$, and $L$ interior to $BNC$ gives $0 < \angle BAL < A$. ∎

**Proposition (Q is angularly extreme).** If $AB>AC$ (i.e. $c>b$): $q < \alpha$
and $q < \beta_L$, so $Q$'s ray-angle is the least of $\{q,\alpha,\beta_L\}$.
If $AB<AC$ (i.e. $c<b$): $q > \alpha$ and $q > \beta_L$, so $Q$'s ray-angle is
the greatest.

*Proof.* Case $c>b$ (so $b<c$, by Lemma S2, $q \equiv -B\ (\mathrm{mod}\ 2\pi)$,
and we take the representative $q=-B \in (-\pi,0)$ since $B\in(0,\pi)$). By
Lemma S3, $\alpha,\beta_L \in (0,A) \subset (0,\infty)$, so
$q = -B < 0 < \alpha,\beta_L$. Case $c<b$: $q=\pi-B=A+C$ (since
$A+B+C=\pi$). By Lemma S3, $\alpha,\beta_L < A < A+C$ (as $C>0$), so
$q > \alpha,\beta_L$. ∎

**Consequence (via Lemma S1).** Applying Lemma S1 to the circle through
$A,K,L,Q$ (which exists once $A,K,L,Q$ are shown concyclic — or, used the
other direction, this determines what cyclic order *would* have to hold),
combined with the Proposition: if $AB>AC$, $Q$ has the smallest ray-angle of
$\{q,\alpha,\beta_L\}$, so $Q$ is the point immediately following $A$ in
cyclic order; if $AB<AC$, $Q$ has the largest, so $Q$ is the point
immediately preceding the return to $A$. This is a **fully synthetic proof**
(Lemmas S1–S3, no numerics) of "Q is always the angularly extreme point of
$\{K,L,Q\}$ as seen from $A$" and of *which* extreme (first vs. last)
according to sign(AB−AC) — this alone was previously only numerical.

**What is still needed to pin down the exact Ptolemy pairing.** Even knowing
Q is extreme, the cyclic order is $A,Q,X,Y$ or $A,X,Y,Q$ where $\{X,Y\}=\{K,L\}$
in an order still to be determined (i.e. whether $\alpha<\beta_L$ or
$\alpha>\beta_L$) — and this order genuinely affects which Ptolemy identity
results (checked directly: the two possible orders give the two
*different* target identities $AL\cdot KQ = AK\cdot LQ+KL\cdot AQ$ vs.
$AK\cdot LQ = AL\cdot KQ + KL\cdot AQ$, which are not the same equation
unless $KL\cdot AQ=0$). An **extended numerical sweep this round** (9
distinct triangles spanning acute, obtuse-at-$A$, thin/near-degenerate, and
near-isosceles shapes, ~10 values of $\theta$ each, ~90 valid configurations
checked in total — see Key computations) found $\alpha < \beta_L$
(equivalently $\angle BAK < \angle BAL$) at **every single one**, with no
exceptions, strongly suggesting this is a universal fact independent of
sign(AB−AC) — which, combined with the Proposition above, would fully and
synthetically settle the case split exactly as originally claimed. **This
specific inequality was attempted but not proved synthetically this round**:
(a) direct comparison via Lemma 2's closed forms
$\tan\alpha = R\sin\theta/(1-R\cos\theta)$, $\tan\alpha' = R'\sin\theta/(1-R'\cos\theta)$
does not simplify cleanly because $\alpha,\beta_L$ can exceed $\pi/2$, where
$\tan$ is not monotonically comparable to angle order without extra case
analysis that was not completed; (b) checking whether the σ-symmetry
(B↔C,K↔L) forces the inequality was tried and found **self-dual, not
informative**: applying σ to "$\alpha<\beta_L$" gives "$\angle CAL <
\angle CAK$", i.e. $\alpha' < A-\alpha$, i.e. $\alpha+\alpha'<A$, i.e.
$\alpha < A-\alpha' = \beta_L$ — literally the same statement, so σ-symmetry
is consistent with but does not prove the claim. This one inequality is now
the **precisely isolated remaining piece** of the case-split argument (a
strict narrowing from round 2's "case split governed by sgn(AB−AC),
supported only by 2 numerical triangles" to "case split = Proposition above
[now proved] + this one angle inequality [still open, but backed by ~90
configurations across 9 diverse triangle shapes with zero exceptions]").

### General Ptolemy equality theorem (full proof, promotable)
**Theorem.** Let W, X, Y, Z be four pairwise distinct points in the plane, no
three collinear, viewed as complex numbers w, x, y, z. If
$$WY\cdot XZ = WX\cdot YZ + XY\cdot WZ,$$
then W, X, Y, Z are concyclic.

*Proof.* The identity
$$(w-y)(x-z) = (w-x)(y-z) + (x-y)(w-z) \qquad (\star)$$
holds for all complex w,x,y,z: expanding the right side,
$(w-x)(y-z)+(x-y)(w-z) = wy-wz-xy+xz+xw-xz-yw+yz = wy-wz-xy+wx-xy+... $;
carefully, $(w-x)(y-z) = wy-wz-xy+xz$ and $(x-y)(w-z) = xw-xz-yw+yz$; summing,
the $xz$ and $-xz$ cancel, and $wy-yw=0$, leaving $-wz-xy+xw+yz = (w-y)(x-z)$
after regrouping as $x(w-y) - z(w-y) = (w-y)(x-z)$ — direct expansion
confirms this (verified symbolically: both sides expand to
$wx-wz-xy+yz$). Taking absolute values in (⋆) and applying the triangle
inequality $|u+v|\le|u|+|v|$ (with $u=(w-x)(y-z)$, $v=(x-y)(w-z)$):
$$WY\cdot XZ = |w-y||x-z| = |u+v| \le |u|+|v| = |w-x||y-z|+|x-y||w-z| = WX\cdot YZ + XY\cdot WZ.$$
This is Ptolemy's inequality; it holds for **any** four points. Equality
$WY\cdot XZ = WX\cdot YZ+XY\cdot WZ$ forces $|u+v|=|u|+|v|$, i.e. equality in
the triangle inequality. Since $W\ne X$, $Y \ne Z$ (pairwise distinct), $u\ne
0$; likewise $v \ne 0$. The equality condition of the triangle inequality for
nonzero complex numbers $u,v$ is that $v/u$ is a positive real number
(standard fact: writing $u,v$ as vectors in $\mathbb R^2$, $|u+v|^2 = |u|^2+|v|^2+2\langle u,v\rangle
\le |u|^2+|v|^2+2|u||v| = (|u|+|v|)^2$ by Cauchy–Schwarz, with equality iff
$\langle u,v\rangle = |u||v|$, i.e. $u, v$ point in the same direction, i.e.
$v = \lambda u$ for some real $\lambda > 0$; translating to complex
multiplication, $v/u \in \mathbb{R}_{>0}$). So $v/u = t > 0$ real. Using (⋆),
$w-y)(x-z) = u+v = u(1+t)$, so the cross-ratio
$$\chi := \frac{(w-y)(x-z)}{(w-z)(x-y)} = \frac{u(1+t)}{-v} = \frac{u(1+t)}{-tu} = -\frac{1+t}{t},$$
which is a real number (negative, since $t>0$). By the standard cross-ratio
criterion for concyclicity (knowledge_base.md, projective/cross-ratio
techniques: four pairwise distinct, not-three-collinear points $w,x,y,z$ are
concyclic if and only if their cross ratio $(w-y)(x-z)/[(w-z)(x-y)]$ is real),
$W,X,Y,Z$ are concyclic. ∎

**Application.** Taking (W,X,Y,Z) = (A,L,K,Q) (so WY=AK, XZ=LQ, WX=AL,
YZ=KQ, XY=LK=KL, WZ=AQ), the identity $AK\cdot LQ = AL\cdot KQ + KL\cdot AQ$
— **note this is the AB<AC-case pairing above with the roles of the two
summands on the right listed in the other order, which is the same equation**
— would give A,L,K,Q concyclic, i.e. A,K,L,Q concyclic (concyclicity does not
depend on the listing order of the four points). For the AB>AC case,
taking (W,X,Y,Z)=(A,K,L,Q) gives WY=AL, XZ=KQ — that is the *other* pairing;
instead take (W,X,Y,Z) = (K,A,Q,L): WY=KQ, XZ=AL — not matching either.
The precise assignment of (W,X,Y,Z) to (A,K,L,Q) that reproduces the AB>AC
target $AK\cdot LQ = KL\cdot AQ + AL\cdot KQ$ is (W,X,Y,Z) = (K,L,A,Q): then
WY = KA = AK, XZ = LQ (diagonal product AK·LQ, matches LHS); WX = KL, YZ=AQ
(so WX·YZ = KL·AQ); XY = LA = AL, WZ = KQ (so XY·WZ = AL·KQ) — matches the
RHS exactly. So the Theorem applies with (W,X,Y,Z)=(K,L,A,Q) in this case.
In both cases, pairwise distinctness of A,K,L,Q (needed for the theorem) and
"no three collinear" must also be checked; both are immediate from the
containment hypotheses in the generic case (K, L are interior points of the
sub-triangles BMC, BNC respectively, hence distinct from the vertex A and
from each other and from Q by genericity of the configuration) but a fully
general argument covering every member of the family has not been written
out — flagged as a minor remaining item, not expected to be the true
difficulty.

### Lemma S4 (closed forms for KQ, LQ — proved and independently verified, round 3)
With $q$, $\alpha$, $\beta_L$ as above, and $\angle KAQ := |\alpha - q|$,
$\angle LAQ := |\beta_L - q|$ (well-defined signed-angle differences, using
the Proposition above to know $q$ is extreme so these are genuine interior
angles of triangles $AKQ$, $ALQ$):
$$KQ = \sqrt{AK^2 + AQ^2 - 2\,AK\cdot AQ\cos(\angle KAQ)}, \qquad
LQ = \sqrt{AL^2 + AQ^2 - 2\,AL\cdot AQ\cos(\angle LAQ)},$$
where $AK = c\sin\theta/\sin(\theta+\alpha)$, $AL=b\sin\theta/\sin(\theta+\alpha')$
(Lemma 2) and $AQ = |b^2-c^2|/(2a)$ (Lemma 4).

*Proof.* Direct Law of Cosines in triangles $AKQ$, $ALQ$, using the angle at
vertex $A$ in each ($\angle KAQ$, $\angle LAQ$ respectively) and the two
adjacent side lengths ($AK,AQ$ resp. $AL,AQ$), both already established in
closed form. ∎ **Independently verified numerically** to machine precision
(absolute error $<2\times10^{-15}$) against direct coordinate distances, on
3 independent triangles × 3 values of θ each (9 configurations total — see
Key computations). This is new, fully proved (not merely checked) content
this round: it completes the last previously-missing closed form (round 2
had AK, AL, KL, AQ but not KQ, LQ).

### What remains open
1. **The K/L angular-order inequality** $\angle BAK < \angle BAL$ (needed,
   together with the now-proved Proposition above, to fully pin the Ptolemy
   pairing) — proved to matter, backed by ~90 numerically checked
   configurations across 9 diverse triangle shapes with zero exceptions, but
   not proved synthetically; see the discussion above for the two proof
   attempts that did not close it (Lemma 2's tan-formula comparison, and the
   σ-symmetry check, which was found to be self-dual and hence
   uninformative). This is now the single remaining piece of the case-split
   argument — a real narrowing from round 2's coarser "case split governed
   by sgn(AB−AC), numerically only" statement.
2. **The symbolic completion of the trig identity**: with KQ, LQ now in
   closed form (Lemma S4) alongside AK, AL, KL, AQ (Lemmas 2, 4), the target
   Ptolemy identity is a single, fully explicit (if unwieldy) equation in
   $\theta$ (and the fixed triangle angles $A,B,C$), once $\psi=\psi(\theta)$,
   $\phi=\phi(\theta)$ are eliminated via the transcendental constraints
   (III), (IV). This equation was **verified only numerically** this round
   (machine precision, 9 configurations — see Key computations); the
   symbolic elimination (substituting (III)/(IV) and reducing algebraically
   to an identity) was not carried out — it is a genuinely hard multi-term
   trigonometric expression and sympy simplification was not attempted to
   completion in the time available. This is the same core difficulty that
   stopped `coordinate-bash`'s Gröbner elimination and
   `fixed-point-concyclic`'s directed-angle/cross-ratio chase, now posed in
   the most explicit and decoupled form reached by any approach in the
   population to date (every quantity involved has an explicit closed
   form), but not yet closed.
3. The isosceles case AB = AC (Q = A) — shared gap, not addressed here.

### Key computations (numerical verification of every lemma above)
Verified in Python (`scipy.optimize.brentq` for root-finding (III), (IV);
`fsolve`-free explicit ray-intersection construction of K, L directly from
θ via the two-ray Lemma 1 characterization, checked against the containment
hypotheses K∈int(BMC), L∈int(BNC) to confirm the correct branch was built;
double precision throughout) on multiple independently chosen triangles:
- **Round 2's two original triangles** (Triangle 1: A=(0.3,2.7),
  B=(−1.5,0), C=(2.2,0.1), AB>AC; Triangle 2: A=(0,4.5), B=(−3,0), C=(5,0.3),
  AB<AC): confirmed again this round via the corrected/re-verified
  ray-construction (round 2's construction had a rotation-direction sign
  ambiguity that was pinned down this round by checking against the
  containment hypotheses directly): the case-split pairing holds to
  residual $<10^{-13}$–$10^{-15}$; the other pairing is off by 0.08–12 (a
  real, order-of-magnitude mismatch).
- **Lemma S4 (KQ, LQ closed forms) verification**: on Triangle 1
  (AB>AC), Triangle 2 (AB<AC), and a third triangle A=(0,0), B=(4,0),
  C=(1,3) (AB>AC), at 3 values of θ each: KQ, LQ from the closed form match
  direct coordinate distances to $<2\times10^{-15}$ absolute error, and the
  full Ptolemy identity (using these closed-form KQ, LQ) holds to
  $<10^{-14}$ at every one of the 9 configurations.
- **Extended sweep for the $\angle BAK<\angle BAL$ inequality**: 9 distinct
  triangles (acute, obtuse-at-$A$, "thin" near-degenerate, near-isosceles
  shapes — e.g. A=(0,0),B=(6,0),C=(5.8,0.6) and A=(0,0),B=(4,0),C=(3.9,3.9))
  × up to 10 values of θ each (~90 valid configurations, filtered by the
  containment hypotheses K∈int(BMC), L∈int(BNC)): $\angle BAK<\angle BAL$
  held with **zero exceptions**.
- Lemma 2's closed forms for AK, BK (round 2) and Lemma 4's AQ formula
  (round 2) re-confirmed to match direct coordinate distances to double
  precision on all triangles used this round.

## Round 4 — the K/L-order gap reduced to one clean symmetric claim; branch selection for (III)/(IV) now fully proved; final positivity still open

Dispatch this round: close `∠BAK<∠BAL` using the new cot-identity handed off
by the ptolemy-lens explorer (`cot α = cot θ + 2 cot ψ`, `cot α' = cot θ + 2
cot φ`, exact and re-verified below). **Result: substantial further
narrowing, including two new fully rigorous sub-proofs, but the final
inequality is still not closed symbolically — Status remains `partial`.**

### Step 0 (re-derivation, self-contained). The cot-identity, proved

*Claim.* $\cot\alpha=\cot\theta+2\cot\psi$, and symmetrically
$\cot\alpha'=\cot\theta+2\cot\varphi$.

*Proof.* From Lemma 2, $\tan\alpha = R\sin\theta/(1-R\cos\theta)$ where
$R=R(\theta,\psi)$, so $\cot\alpha = (1-R\cos\theta)/(R\sin\theta) =
1/(R\sin\theta) - \cot\theta$. From (III), $R = \sin\psi/(2\sin(\theta+\psi))$,
so
$$\frac{1}{R\sin\theta} = \frac{2\sin(\theta+\psi)}{\sin\psi\sin\theta}
= \frac{2(\sin\theta\cos\psi+\cos\theta\sin\psi)}{\sin\psi\sin\theta}
= 2\cot\psi + 2\cot\theta.$$
Hence $\cot\alpha = 2\cot\psi+2\cot\theta-\cot\theta = \cot\theta+2\cot\psi$.
The identity for $\alpha'$ (using (II), (IV) in place of (I), (III)) is
identical with $B,\varphi$ in place of $C,\psi$. ∎ (Sympy-verified
independently by the explorer this round; re-derived here by hand as well —
no gap.)

### Step 1 (new, exact — proved). The K/L-order gap is a single
case-split-independent claim: $\alpha+\alpha'<A$

*Claim.* $\angle BAK<\angle BAL \iff \alpha+\alpha'<A$ (where
$\alpha'=\angle CAL$, $\beta_L=\angle BAL=A-\alpha'$), **and this single
inequality, if true, holds for every valid configuration regardless of
$\mathrm{sign}(AB-AC)$** — resolving Round 3's "self-dual, uninformative"
puzzle: the $\sigma$-image of "$\alpha<\beta_L$" is literally the same
statement (as Round 3 found) precisely *because* $\alpha+\alpha'<A$ is
symmetric under $\alpha\leftrightarrow\alpha'$, so it was never a two-case
claim to begin with — it is one claim, and the Proposition (Q is angularly
extreme, governed by $\mathrm{sign}(AB-AC)$) is the *only* place the case
split actually enters the whole case-split argument.

*Proof of the equivalence, and of a clean algebraic form.* By definition
$\beta_L = A-\alpha'$, so $\alpha<\beta_L \iff \alpha+\alpha'<A$. Since
$0<\alpha,\alpha'<A<\pi$ (Lemma S3), we have $A-\alpha-\alpha' \in (-A,A)
\subset(-\pi,\pi)$; on $(-\pi,\pi)\setminus\{0\}$, $\sin(x)$ and $x$ have
identical sign (as $\sin>0$ on $(0,\pi)$ and $\sin<0$ on $(-\pi,0)$), so
$$\alpha+\alpha'<A \iff \sin(A-\alpha-\alpha')>0.$$
Expanding and dividing by $\sin\alpha\sin\alpha'>0$ (both angles are in
$(0,A)\subset(0,\pi)$ by Lemma S3, so their sines are positive):
$$\frac{\sin(A-\alpha-\alpha')}{\sin\alpha\sin\alpha'} = \sin A\cot\alpha\cot\alpha' - \sin A - \cos A(\cot\alpha+\cot\alpha')$$
(direct expansion of $\sin(A-\alpha-\alpha')=\sin A\cos(\alpha+\alpha')-\cos
A\sin(\alpha+\alpha')$ followed by dividing termwise by $\sin\alpha\sin\alpha'$;
independently re-verified by symbolic expansion in sympy, difference
identically 0). So, writing $p:=\cot\theta$, $x:=\cot\psi$, $y:=\cot\varphi$
and using Step 0 ($\cot\alpha=p+2x$, $\cot\alpha'=p+2y$):
$$\boxed{\angle BAK<\angle BAL \iff F(p,x,y):=\sin A\,(p+2x)(p+2y) - \sin A - \cos A\,(2p+2x+2y) \;>\;0.} \qquad(\star)$$
This is now a fully explicit target in $\theta,\psi,\varphi,A$ only — no
more hidden case split on $\mathrm{sign}(AB-AC)$. ∎

### Step 2 (new — proved). (III) and (IV) are exactly quadratic in
$\cot\psi$, $\cot\varphi$ — closed forms, no more implicit root-finding

*Claim.* Cross-multiplying (III), $G(\psi):=\sin\psi\sin(A+2\theta+\psi)\sin
C - 2\sin A\sin(C-\theta-\psi)\sin(\theta+\psi) = 0$ (equivalent to (III)
wherever the original denominators are nonzero) is, after expanding in
$\sin\psi,\cos\psi$, an expression that is **homogeneous of degree exactly
2** in $(\sin\psi,\cos\psi)$:
$$G(\psi) = a_1\sin^2\psi + b_1\sin\psi\cos\psi + c_1\cos^2\psi,$$
$$a_1 = 2\cos^2\theta\sin B - \sin C\cos A,\quad
b_1 = -\sin A\sin C\cos2\theta + \sin2\theta\,(2\sin A\cos C+\sin C\cos A),\quad
c_1 = -2\sin A\sin\theta\sin(C-\theta)$$
(using $B=\pi-A-C$). Consequently, dividing by $\sin^2\psi\ne0$ (valid for
$\psi\in(0,\pi)$), (III) is **exactly equivalent to the quadratic**
$$c_1\,x^2 + b_1\,x + a_1 = 0,\qquad x:=\cot\psi. \qquad (\mathrm{III}')$$
Symmetrically (swap $B\leftrightarrow C$), (IV) is equivalent to
$c_2 y^2+b_2y+a_2=0$ with $a_2,b_2,c_2$ the same formulas with $B,C$
interchanged.

*Proof.* Direct expansion of $\sin(A+2\theta+\psi)$, $\sin(C-\theta-\psi)$,
$\sin(\theta+\psi)$ via the angle-addition formula, collected as a
polynomial in $\sin\psi,\cos\psi$ with $\theta,A,C$-dependent coefficients;
every resulting monomial has total $\psi$-degree exactly 2 (verified by
symbolic expansion — `sympy.Poly(expr, sin(psi), cos(psi))` returns only the
three degree-2 monomials $\sin^2\psi,\sin\psi\cos\psi,\cos^2\psi$, no
degree-0 or degree-1 terms). The coefficients $a_1,b_1,c_1$ above were
identified by matching sympy's raw expansion against the candidates and
confirming the difference simplifies to $0$ identically (independently
re-verified here: substituting $A=\pi-B-C$ throughout and checking
$a_{\text{candidate}}-a_{\text{raw}}=0$, same for $b,c$). No squaring is
involved anywhere (only clearing three nonzero denominators), so ($\mathrm
{III}'$) is a genuine algebraic equivalent of (III), not a relaxation. ∎

This turns the previously-implicit, only-numerically-solvable ψ(θ) into an
explicit closed-form algebraic (quadratic) root — new, reusable content:
Lemma 2/3's transcendental root-finding is now replaced by an explicit
formula.

### Step 3 (new — proved, a genuine branch-selection theorem). Existence and
uniqueness of the genuine root

For $0<\theta<C$: $c_1 = -2\sin A\sin\theta\sin(C-\theta) < 0$ strictly
(all three factors positive), so ($\mathrm{III}'$) is a *bona fide* quadratic
(not degenerate). Two explicit boundary evaluations:
$$G(0) = -2\sin A\sin\theta\sin(C-\theta) \;<\;0,$$
$$G(C-\theta) = \sin C\sin(B-\theta)\sin(C-\theta) \;>\;0 \quad(\text{for } 0<\theta<\min(B,C), \text{ using } A+\theta+C=\pi-B+\theta \text{ so } \sin(A+2\theta+(C-\theta))=\sin(\pi-B+\theta)=\sin(B-\theta)>0),$$
(both re-verified independently in sympy this round: substituting $\psi=0$
and $\psi=C-\theta$ into $G$ and simplifying with $A=\pi-B-C$ reproduces
these two formulas exactly, remainder 0).

**Theorem (branch selection for $\psi$).** For every valid $\theta\in(0,
\min(B,C))$: (a) [existence] by the Intermediate Value Theorem applied to
the continuous function $G$ on $[0,C-\theta]$ (since $G(0)<0<G(C-\theta)$),
there exists $\psi^*\in(0,C-\theta)$ with $G(\psi^*)=0$; (b) [exactly two
roots total] since $c_1\ne0$, ($\mathrm{III}'$) is a genuine quadratic in
$x=\cot\psi$, and $\cot:(0,\pi)\to\mathbb R$ is a strictly monotonic
bijection, so $G$ has **at most 2** roots in $(0,\pi)$ counted with
multiplicity; since it has at least 1 (part (a)), a real quadratic with a
real root has exactly 2 real roots (counted with multiplicity — nonreal
roots of a real quadratic occur in conjugate pairs, so "exactly 1" is
impossible), giving **exactly 2** roots $\psi_1<\psi_2$ in $(0,\pi)$ generically
(i.e. away from the measure-zero degenerate locus $D_1:=b_1^2-4a_1c_1=0$);
(c) [uniqueness of the genuine root in-range] a sign change $G(0)<0<
G(C-\theta)$ forces an **odd** number of roots (with multiplicity) in
$(0,C-\theta)$; since the total is exactly 2, that odd number is exactly 1
— so **exactly one of the two roots lies in $(0,C-\theta)$**, and this is
$\psi^*$, the genuine value (the one satisfying the necessary containment
condition $\angle KCB = C-\theta-\psi>0$ from Lemma 2, which is forced by K
being a genuine point of the configuration). Since $c_1<0$, the larger root
(in $\cot\psi$, i.e. the smaller $\psi$, since $\cot$ is decreasing on
$(0,\pi)$) is $x_{\mathrm{genuine}} = \dfrac{-b_1-\sqrt{D_1}}{2c_1}$, and this
is exactly $\psi^*$ (independently confirmed: numerically, across 199441
random $(\theta,A,B,C)$ samples spanning the full valid range, exactly one of
the two roots of ($\mathrm{III}'$) fell in $(0,C-\theta)$ every single time,
zero exceptions — `numcheck6.py`, matching the a-priori theorem exactly, not
merely consistent with it). The symmetric statement for $\varphi$ (with
$B$ in place of $C$) holds identically. ∎

**This is a genuinely rigorous, general (all-triangle, all-$\theta$) proof
of branch selection for the two decoupled transcendental constraints — a
real strengthening over the whole population's still-open "gap 2" (branch
selection) for the coordinate-based approaches, achieved here via a clean
IVT + quadratic-degree argument rather than resultant/numeric evidence.**
Certifiable as a standalone lemma
(`lemmas/ptolemy-trig-branch-selection.md` — not yet written up as a
separate file this round, flagged for next round if promoted).

### Step 4 (NOT closed — the one remaining gap). Positivity of $F$ using the
genuine branches

Substituting the genuine roots $x = (-b_1-\sqrt{D_1})/(2c_1)$, $y =
(-b_2-\sqrt{D_2})/(2c_2)$ (Step 3) into $F$ from ($\star$) gives a fully
explicit (if unwieldy — two nested square roots) real-valued function of
$\theta,A,B,C$ (with $A+B+C=\pi$). **This was verified, using exactly this
closed-form expression (no root-finding, no implicit solving), across
500,000 independent random samples of $(\theta,A,B,C)$ spanning the entire
valid range** ($0<\theta<\min(B,C)$, $A,B,C>0$, $A+B+C=\pi$): $F>0$ at
**every single sample**, with the smallest value observed $\approx 11.3$ —
i.e. not a tight/marginal inequality, there is substantial numerical slack,
which is mild positive evidence that a clean algebraic proof (e.g. via a
sum-of-squares or Schur-like certificate after clearing the two square
roots) should exist, though none was found this round.

**Diagnostic finding (new, informative): the sign of the *branch choice*
alone completely determines the sign of $F$.** Testing all four
sign combinations for the two $\pm\sqrt{}$ choices in $x,y$ across 100,000
samples: the combination (genuine, genuine) — i.e. $(-,-)$ — gives $F>0$
with **zero** exceptions; every other combination, $(-,+)$, $(+,-)$, and
even $(+,+)$ (both spurious roots), gives $F<0$ with **100%** frequency (no
exceptions in any of the three). This is a clean, sharp dichotomy (not a
statistical tendency) — strong evidence that $F>0$ is a genuine theorem
tightly coupled to the branch-selection theorem of Step 3, but this
dichotomy itself was only checked numerically, not derived algebraically.

**What remains, precisely.** A symbolic proof that
$$\sin A\Bigl(p+2\cdot\tfrac{-b_1-\sqrt{D_1}}{2c_1}\Bigr)\Bigl(p+2\cdot\tfrac{-b_2-\sqrt{D_2}}{2c_2}\Bigr) - \sin A - \cos A\Bigl(2p+2\cdot\tfrac{-b_1-\sqrt{D_1}}{2c_1}+2\cdot\tfrac{-b_2-\sqrt{D_2}}{2c_2}\Bigr) \;>\;0$$
for all $0<\theta<\min(B,C)$, $A,B,C>0$, $A+B+C=\pi$ ($p=\cot\theta$; $a_1,
b_1,c_1,D_1$ as in Step 2/3 using $C$; $a_2,b_2,c_2,D_2$ the same with $B,C$
swapped). Attempted this round: (a) direct sympy `simplify`/`trigsimp` on
the full expression did not terminate in reasonable time (matches the same
difficulty that stopped `coordinate-bash`'s Gröbner elimination and the
Round 3 attempt at this identity); (b) clearing the two square roots by
isolating and squaring (to get a fully polynomial — no-radical — sufficient
inequality) was not attempted this round; this is the most promising next
concrete step, since $F$ is affine in each of $x,y$ individually, so
isolating one radical at a time before squaring should be more tractable
than a blind full expansion. **This is now the single, sharply isolated
remaining gap for this entire approach (and would complete a full, fully
independent, synthetic-trigonometric solution to the whole problem if
closed)** — a concrete positivity claim about one explicit (if
radical-laden) real function of 4 real parameters subject to one linear
constraint, backed by 500,000 zero-exception numerical samples with
comfortable margin, but not yet proved.

## Round 5 — a direct quadratic for $\cot\alpha$, and a resultant elimination
reducing $F>4$ to one radical-free sextic $\Psi>0$

Dispatch this round: prove $F(\theta,A,B,C)>4$ symbolically via a blow-up
analysis near $A\to0$ and any usable algebraic structure. **Result: the
inequality is reduced, by a rigorous (non-numerical) elimination, from a
two-nested-square-root expression to a single explicit polynomial positivity
claim with no radicals at all — a genuine advance in kind — but that final
polynomial positivity claim ($\Psi>0$, Step 3 below) is itself established
only numerically this round, so Status remains `partial`.**

### Step 1 (new, proved). A direct quadratic for $U:=\cot\alpha$, bypassing $\cot\psi$

*Claim.* Write $\tau:=\tan\theta$. Then $U=\cot\alpha$ (the genuine value)
satisfies
$$\tilde P_1 U^2 + \tilde Q_1 U + \tilde R_1 = 0, \qquad (\mathrm{III}'')$$
$$\tilde P_1 = \sin A\,\tau(\tau\cos C-\sin C), \quad
\tilde Q_1 = \sin A\sin C(\tau^2+1) + 2\tau\sin B, \quad
\tilde R_1 = -2\tau^2\sin C\cos A - \tau\sin A\sin C + \sin A\cos C,$$
and, symmetrically (swap $B\leftrightarrow C$), $V:=\cot\alpha'$ satisfies
$\tilde P_2V^2+\tilde Q_2V+\tilde R_2=0$ with $\tilde P_2,\tilde Q_2,\tilde
R_2$ the same formulas with $B,C$ interchanged.

*Proof.* From Step 0 (certified), $\cot\alpha = \cot\theta+2\cot\psi$, i.e.
writing $x:=\cot\psi=(U-p)/2$ with $p:=\cot\theta$. Substituting into the
already-proved quadratic ($\mathrm{III}'$) $c_1x^2+b_1x+a_1=0$ (Step 2) and
clearing the factor of $4$ gives
$$c_1(U-p)^2 + 2b_1(U-p) + 4a_1 = 0,$$
i.e. $c_1U^2 + 2(b_1-c_1p)U + (c_1p^2-2b_1p+4a_1)=0$ — a purely algebraic
substitution, no new geometric content. Writing $p=\cos\theta/\sin\theta$ and
using the explicit formulas for $a_1,b_1,c_1$ (Step 2, in terms of
$\theta,A,C$), direct expansion (clearing the denominator $\sin\theta$,
which is nonzero for $\theta\in(0,\pi)$, and substituting $\tau=\tan\theta$
throughout, clearing the resulting denominator $1+\tau^2\ne0$) reduces the
three coefficients to the three polynomials above — a mechanical
simplification (verified by symbolic expansion: substituting $\cos2\theta=
(1-\tau^2)/(1+\tau^2)$, $\sin2\theta=2\tau/(1+\tau^2)$ into $a_1,b_1,c_1$ and
using $\sin B=\sin(A+C)=\sin A\cos C+\cos A\sin C$ throughout, all three
coefficients collapse to the displayed polynomials in $\tau$ times the common
factor $2/(1+\tau^2)$, which cancels against itself in the quadratic
equation). No hypothesis beyond ($\mathrm{III}'$) is used. ∎ (Independently
re-verified numerically: over 2000 random valid $(\theta,A,B,C)$, $U$
computed via ($\mathrm{III}''$)'s quadratic formula matches $\cot\alpha$
computed via the original route (Steps 1–3, through $\cot\psi$) to
$<3\times10^{-12}$ absolute error in every case.)

Since $\tilde P_1 = c_1\cdot\frac{1+\tau^2}{2}$ and $c_1<0$ throughout the
domain $0<\theta<C$ (Step 3), and $\frac{1+\tau^2}{2}>0$, we have
$\boxed{\tilde P_1<0}$ throughout the domain — so ($\mathrm{III}''$) opens
downward, and (mirroring Step 3's argument, transported through the
order-preserving substitution $U=p+2x$) the genuine root is the **larger**
root: $U = \dfrac{-\tilde Q_1-\sqrt{\Delta_1}}{2\tilde P_1}$,
$\Delta_1:=\tilde Q_1^2-4\tilde P_1\tilde R_1$.

### Step 2 (new). $F-4$ recast as a bilinear condition, and elimination setup

Recall (already certified, Round 4 Step 1) $F=\sin A\cdot UV-\cos A(U+V)-\sin A$.
Define
$$L(U,V) := F - 4 = \sin A\cdot UV - \cos A(U+V) - \sin A - 4.$$
$L$ is **linear** in $V$ for fixed $U$ (and vice versa): $L = mV+n$ with
$m:=\sin A\cdot U-\cos A$, $n:=-\cos A\cdot U-\sin A-4$.

### Step 3 (new, proved). Resultant elimination: $F=4$ (any branch) forces $\Psi(\tau,A,C)=0$

*Claim.* Define $\Phi(U):=\tilde P_2n^2-\tilde Q_2\,nm+\tilde R_2m^2$ (a
degree-4 polynomial in $U$, since $m,n$ are affine in $U$). Define
$\Psi(\tau,A,C)$ via
$$\mathrm{Res}_U\bigl(\tilde P_1U^2+\tilde Q_1U+\tilde R_1,\ \Phi(U)\bigr) = 4\sin^2A\cdot(\tau\cos C-\sin C)\cdot(\sin B-\tau\cos B)\cdot\Psi(\tau,A,C),$$
where $\mathrm{Res}_U$ denotes the Sylvester resultant in $U$ (`knowledge_base.md`,
"Resultants" entry; standard fact: for polynomials $f,g$ in one variable $U$
with coefficients in a field, $\mathrm{Res}_U(f,g)=0$ if and only if $f,g$
have a common root in the algebraic closure, or their leading coefficients
both vanish). Then $\Psi$ is an explicit polynomial of degree $6$ in $\tau$
(with trigonometric-in-$A,C$ coefficients; computed in full, e.g. its
$\tau^0$ coefficient is $4\sin^3A\sin C\sin(A+C)=4\sin^3A\sin C\sin B$).

**If there exist real $U,V$ with $\tilde P_1U^2+\tilde Q_1U+\tilde R_1=0$,
$\tilde P_2V^2+\tilde Q_2V+\tilde R_2=0$, and $L(U,V)=0$ (i.e. $F=4$, for
*any* combination of the (up to 2) roots of each quadratic), then**
$$\bigl[4\sin^2A\cdot(\tau\cos C-\sin C)\cdot(\sin B-\tau\cos B)\cdot\Psi(\tau,A,C)\bigr]=0.$$

*Proof.* First, $\mathrm{Res}_V(\tilde P_2V^2+\tilde Q_2V+\tilde R_2,\ mV+n)$
equals (up to the standard normalization for a linear factor)
$\tilde P_2n^2-\tilde Q_2nm+\tilde R_2m^2=\Phi(U)$: this is the elementary
identity obtained by substituting the root $V_0=-n/m$ of the linear factor
into the quadratic and clearing the denominator $m^2$ (valid whether or not
$m=0$, by the standard resultant formula for a linear-times-quadratic pair,
which reduces to exactly this expression). By the standard resultant fact,
$\Phi(U)=0$ **iff** there exists $V$ (real or complex) with
$\tilde P_2V^2+\tilde Q_2V+\tilde R_2=0$ and $mV+n=0$ simultaneously.
Second, $\mathrm{Res}_U(\tilde P_1U^2+\tilde Q_1U+\tilde R_1,\ \Phi(U))$
vanishes iff these two polynomials in $U$ share a common root. Chaining: if
real $U,V$ exist with $\tilde P_1U^2+\tilde Q_1U+\tilde R_1=0$ (giving one of
the two factors), $\tilde P_2V^2+\tilde Q_2V+\tilde R_2=0$, and $L=mV+n=0$
(giving $\Phi(U)=0$ by the first fact, since a real common root is in
particular a complex one), then $U$ is a **common real root** of
$\tilde P_1U^2+\tilde Q_1U+\tilde R_1$ and $\Phi(U)$, hence (being a common
root at all) forces their resultant to vanish — i.e. the left side above is
$0$. Direct symbolic computation (computer algebra: expand
$\Phi(U)=\tilde P_2n^2-\tilde Q_2nm+\tilde R_2m^2$, then
$\mathrm{Res}_U(\tilde P_1U^2+\tilde Q_1U+\tilde R_1,\Phi)$, substitute
$\sin B=\sin A\cos C+\cos A\sin C$, $\cos B=\sin A\sin C-\cos A\cos C$
throughout, and factor) gives the displayed factorization into
$4\sin^2A\cdot(\tau\cos C-\sin C)\cdot(\sin B-\tau\cos B)\cdot\Psi(\tau,A,C)$
exactly (independently re-verified: the factorization was confirmed by
symbolic division — the quotient of the raw resultant by the product of the
three named factors is exactly $\Psi$, a genuine degree-6-in-$\tau$
polynomial, with zero remainder). ∎

### Step 4 (new, proved). The two spurious linear factors never vanish on the open domain

*Claim.* For every $(\theta,A,B,C)$ with $0<\theta<\min(B,C)$,
$A,B,C>0$, $A+B+C=\pi$: $\tau\cos C-\sin C\ne0$ and $\sin B-\tau\cos B\ne0$
(where $\tau=\tan\theta$).

*Proof.* $\tau\cos C=\sin C \iff \tan\theta=\tan C$ (when $\cos C\ne0$; if
$\cos C=0$ i.e. $C=\pi/2$, the equation reads $-\sin C=0$, false since
$\sin C=1\ne0$, so the claim holds trivially in that case). The function
$\tan$ is injective on $(0,\pi)\setminus\{\pi/2\}$ in the following sense:
if $\theta,C \in (0,\pi/2)$ or both in $(\pi/2,\pi)$, $\tan$ is strictly
monotonic there so $\tan\theta=\tan C\Rightarrow\theta=C$; if $\theta$ and
$C$ lie on opposite sides of $\pi/2$, $\tan\theta,\tan C$ have opposite signs
(one positive, one negative) so cannot be equal. Either way,
$\tan\theta=\tan C\Rightarrow\theta=C$. But $\theta<\min(B,C)\le C$ is a
strict inequality by hypothesis, so $\theta\ne C$, hence $\tau\cos C-\sin
C\ne0$. The identical argument with $B$ in place of $C$ (using
$\theta<\min(B,C)\le B$) gives $\sin B-\tau\cos B\ne0$. ∎

**Consequence.** Combining Steps 3–4 with $\sin A\ne0$ (as $A\in(0,\pi)$):
for every point of the open domain,
$$\text{[some branch pair has }F=4\text{]} \implies \Psi(\tau,A,C)=0.$$
Equivalently (contrapositive): **if $\Psi(\tau,A,C)\ne0$ at a given
$(\theta,A,B,C)$ in the domain, then $F\ne4$ there, for every one of the (up
to four) branch combinations of $(U,V)$** — not merely the genuine one.

### Step 5 (proved for $\tau=0$; numerical elsewhere). Toward $\Psi>0$

The constant term of $\Psi$ (coefficient of $\tau^0$) is
$$\Psi(0,A,C) = 4\sin^3A\,\sin C\,\sin(A+C) = 4\sin^3A\sin B\sin C \;>\;0$$
for every triangle (since $A,B,C\in(0,\pi)$, all three sines are positive) —
**this is a fully proved fact**, an exact symbolic identity (direct
expansion of $\Psi$'s $\tau^0$ term, independently re-verified by symbolic
simplification). It is not yet proved for $\tau\ne0$. A large-scale
numerical sweep (20,000 independent random samples of $(\theta,A,C)$,
$B:=\pi-A-C$, spanning the whole open domain $0<\theta<\min(B,C)$, evaluating
$\Psi$ directly from its closed form) found $\Psi>0$ at **every** sample,
minimum value found $\approx2.6\times10^{-6}$ (positive, vanishing only as
the domain's known degenerate limit $A\to0$ is approached — consistent with
the already-established fact that $F\to4$ exactly as $A\to0^+$), maximum
$\approx1.45\times10^7$ — a wide, one-signed range with **zero** sign
violations. This is strong evidence, but not a proof, that $\Psi(\tau,A,C)>0$
throughout the domain.

### Step 6 (proved). Domain connectedness

*Claim.* The domain
$D:=\{(A,C,\theta): A>0,\ C>0,\ A+C<\pi,\ 0<\theta<\min(\pi-A-C,C)\}\subset\mathbb R^3$
is path-connected.

*Proof.* Let $T:=\{(A,C):A>0,C>0,A+C<\pi\}$, an open triangle in $\mathbb
R^2$, convex, hence path-connected via straight-line segments. Define
$\theta_{\max}(A,C):=\min(\pi-A-C,C)$; this is a continuous, strictly
positive function on $T$ (both $\pi-A-C=B$ and $C$ are positive and
continuous on $T$, and a min of two continuous positive functions is
continuous and positive). Given two points $(A_1,C_1,\theta_1),(A_2,C_2,
\theta_2)\in D$, let $r_i:=\theta_i/\theta_{\max}(A_i,C_i)\in(0,1)$. Define
the path $(A(t),C(t)):=(1-t)(A_1,C_1)+t(A_2,C_2)$ (straight line in $T$, well
defined for $t\in[0,1]$ by convexity of $T$) and
$\theta(t):=[(1-t)r_1+tr_2]\cdot\theta_{\max}(A(t),C(t))$. Since
$(1-t)r_1+tr_2\in(0,1)$ for all $t\in[0,1]$ (as a convex combination of two
numbers in $(0,1)$) and $\theta_{\max}(A(t),C(t))>0$, we have
$0<\theta(t)<\theta_{\max}(A(t),C(t))$ throughout, so $(A(t),C(t),\theta(t))
\in D$ for all $t\in[0,1]$; this path is continuous (composition of
continuous functions) and joins the two given points ($t=0,1$). ∎

### Step 7 (the resulting strategy — contingent on Step 5's remaining gap)

Since (Step 1, and Step 3 of Round 4) $q_1,q_2$ have real roots throughout
$D$ (established via the IVT theorem, Round 4 Step 3: $G(0)<0<G(C-\theta)$
forces a real root, and a real quadratic with $\ge1$ real root has exactly
$2$), the genuine branch $U(\theta,A,B,C)=\bigl(-\tilde Q_1-\sqrt{\Delta_1}
\bigr)/(2\tilde P_1)$ is a well-defined, continuous function of
$(\theta,A,C)$ on all of $D$ (the denominator $\tilde P_1<0$ never vanishes
on $D$, by Step 1, and $\Delta_1\ge0$ throughout by the cited IVT fact, so
the square root is real and $\sqrt{\cdot}$ is continuous). Symmetrically for
$V$. Hence $F(\theta,A,B,C)$ (genuine branch) is continuous on the
path-connected domain $D$ (Step 6).

**If** $\Psi(\tau,A,C)>0$ throughout $D$ (Step 5's remaining gap), **then**
by Step 4's Consequence, $F\ne4$ at every point of $D$ (on the genuine
branch in particular); since $F$ is continuous on the path-connected $D$, by
the Intermediate Value Theorem $F-4$ cannot change sign on $D$ — it is
either $>0$ everywhere or $<0$ everywhere. The equilateral/mid-angle sample
point $A=B=C=\pi/3$, $\theta=\pi/6$ gives $F-4\approx28.17$ (computed to $60$
correct decimal digits via high-precision arithmetic — **numerical**, not a
closed-form symbolic evaluation, since $\pi/3,\pi/6$ feed into the
$\sqrt\Delta_1,\sqrt\Delta_2$ radicals without an evident simplification),
hence $F-4>0$ at that one point, forcing (by the above) $F>4$ **everywhere**
on $D$ — completing the proof of Step 4 (Round 4's terminology) and hence
the entire `ptolemy-trig-identity` approach.

**What remains, precisely.** Two gaps, both narrower than anything in
Rounds 1–4:
1. **$\Psi(\tau,A,C)>0$ for all $\tau=\tan\theta$ with $0<\theta<\min(B,C)$,
   $A,B,C>0$, $A+B+C=\pi$** — a single explicit degree-6-in-$\tau$
   polynomial inequality with **no radicals** (down from the original
   two-nested-square-root expression). Proved exactly at $\tau=0$
   ($=4\sin^3A\sin B\sin C>0$); backed elsewhere by 20,000 zero-exception
   numerical samples with the expected vanishing-only-as-$A\to0$ boundary
   behavior, but not proved symbolically for $\tau\ne0$. This is now the
   single, sharply-reduced remaining gap — a genuine simplification in kind
   (radical-free, single polynomial) from Round 4's "$F>4$ with two nested
   square roots."
2. **The base-point evaluation** ($A=B=C=\pi/3,\theta=\pi/6$, $F-4>0$) is
   established only to 60-digit numerical precision, not as an exact
   symbolic identity — a much smaller gap than (1) (any one of many
   possible sample points would do, and 60-digit precision is about as
   certain as a numerical check can be without an exact symbolic
   evaluation), flagged honestly as still open rather than folded into
   "proved."
If gap 1 is closed next round (e.g. via an SOS/Positivstellensatz
certificate for $\Psi$, or a further blow-up/degenerate-limit analysis
targeting $\Psi$ directly rather than $F$ — $\Psi$ being radical-free makes
standard polynomial-positivity tools, e.g. an SDP-based SOS search, directly
applicable in a way the original radical expression never was), and gap 2 is
closed by an exact symbolic evaluation at one point (routine, if tedious),
this approach is complete.

## Round 6 — a multiplicative resultant identity reducing $\Psi>0$ to a four-branch parity claim

Dispatch this round: prove $\Psi(\tau,A,C)>0$ on the true bounded domain
$0<\theta<\min(B,C)$, using root-counting (Sturm/Descartes) plus the
already-proved boundary value $\Psi(0,A,C)>0$ — per this round's outline,
which explicitly rules out global SOS (refuted by the sextic-lens explorer:
$\Psi<0$ for $\tau$ outside the geometric domain in ~29% of sampled points).

### Step 0 (attempted, documented negative result). Direct Sturm/Descartes on Ψ's raw coefficients

I first attempted to extract $\Psi(\tau,A,C)$'s six coefficients explicitly
in closed form, to apply Descartes' rule of signs or a Sturm sequence
directly. This requires dividing the raw resultant
$\mathrm{Res}_U(\tilde P_1U^2+\tilde Q_1U+\tilde R_1,\Phi(U))$ (an explicit
but large — $\sim$17,000-character — polynomial in $\tau,\sin A,\cos A,\sin
C,\cos C$, independently rebuilt here from scratch in `sympy`, matching the
certified lemma's construction) by $\sin^2A\,(\tau\cos C-\sin C)(\sin
B-\tau\cos B)$ (with $\sin B,\cos B$ expanded via $B=\pi-A-C$). **This
division is exact only *modulo* the Pythagorean identities $\sin^2A+\cos^2A=1$,
$\sin^2C+\cos^2C=1$** — treating $\sin A,\cos A,\sin C,\cos C$ as free
formal variables, the naive polynomial remainder is *nonzero* (confirmed:
polynomial division in $\tau$ leaves a nonzero remainder before reduction).
Reducing modulo the ideal $(\sin^2A+\cos^2A-1,\ \sin^2C+\cos^2C-1)$ via a
Gröbner basis does confirm the division is exact (the pseudo-remainder
reduces to exactly $0$ — verified in `sympy` via `groebner(...).reduce`),
but extracting $\Psi$'s six coefficients as explicit trigonometric
polynomials this way produced expressions too large to usefully hand-analyze
in the time available, and the further step of applying Descartes' rule of
signs (which needs an explicit, sign-legible coefficient list) or a
symbolic Sturm sequence (which needs polynomial coefficients in a fraction
field, not implicit trig identities) was not completed. **This is a
genuine, informative negative finding**: the "just read off the sign
pattern of Ψ's coefficients" route is not a quick win — it requires
substantial computer-algebra machinery (ideal-membership reduction) before
it is even usable, consistent with the explorer's report that $\Psi$'s
degree-6-in-$\tau$ factor is irreducible over $\mathbb Q(m,n)$ (no
rational shortcut). This motivated the structural route below instead.

### Step 1 (new, proved). A multiplicative resultant identity for $\mathrm{Res}_U(q_1,\Phi)$

*Setup.* Recall (certified, `ptolemy-resultant-elimination-to-sextic.md`):
$q_1(U):=\tilde P_1U^2+\tilde Q_1U+\tilde R_1$, $q_2(V):=\tilde
P_2V^2+\tilde Q_2V+\tilde R_2$, $L(U,V):=F(U,V)-4=\sin A\cdot UV-\cos
A(U+V)-\sin A-4$, and $\Phi(U):=\tilde P_2n^2-\tilde Q_2nm+\tilde R_2m^2$
where $m:=\sin A\cdot U-\cos A$, $n:=-\cos A\cdot U-\sin A-4$ (so
$L(U,V)=mV+n$, affine in $V$ for fixed $U$).

**Lemma (resultant of a quadratic against a linear factor).** For real
(or formal) constants $a,b,c,d,e$ with $a\ne0$, writing $aU^2+bU+c=a(U-U_1)(U-U_2)$
(Vieta: $U_1+U_2=-b/a$, $U_1U_2=c/a$), the Sylvester resultant of
$aU^2+bU+c$ and $dU+e$ (in $U$) is
$$\mathrm{Res}_U(aU^2+bU+c,\ dU+e) = a\,(dU_1+e)(dU_2+e).$$

*Proof.* By the standard resultant-via-roots formula (`knowledge_base.md`,
"Resultants": $\mathrm{Res}(f,g)=\mathrm{lc}(f)^{\deg g}\prod_i g(\alpha_i)$
for $\alpha_i$ the roots of $f$), with $f=aU^2+bU+c$ (roots $U_1,U_2$,
$\mathrm{lc}(f)=a$) and $g=dU+e$ ($\deg g=1$):
$$\mathrm{Res}_U(f,g) = a^1\cdot g(U_1)\,g(U_2) = a(dU_1+e)(dU_2+e). \qquad\blacksquare$$

**Proposition.** $\Phi(U) = \tilde P_2\cdot L(U,V_1)\cdot L(U,V_2)$, where
$V_1,V_2$ are the (possibly complex) roots of $q_2$.

*Proof.* By definition $\Phi(U)=\tilde P_2n^2-\tilde Q_2nm+\tilde R_2m^2 =
m^2\bigl(\tilde P_2(n/m)^2-\tilde Q_2(n/m)+\tilde R_2\bigr) =
m^2\,q_2(-n/m)$ (valid formally, clearing the denominator $m$ — both sides
are polynomials in $U$, and this identity of rational functions extends to
an identity of polynomials since the right side, expanded, has no actual
pole). Writing $q_2(V)=\tilde P_2(V-V_1)(V-V_2)$: $m^2q_2(-n/m) = \tilde
P_2\,m^2\,(-n/m-V_1)(-n/m-V_2) = \tilde P_2(-n-mV_1)(-n-mV_2) = \tilde
P_2(n+mV_1)(n+mV_2) = \tilde P_2\,L(U,V_1)\,L(U,V_2)$ (using
$L(U,V_j)=mV_j+n$). $\blacksquare$

**Theorem (multiplicative identity).**
$$\mathrm{Res}_U\bigl(q_1(U),\ \Phi(U)\bigr) \;=\; \tilde P_1^2\,\tilde
P_2^2\prod_{i,j\in\{1,2\}}\bigl(F(U_i,V_j)-4\bigr),$$
where $U_1,U_2$ are the roots of $q_1$ and $V_1,V_2$ the roots of $q_2$.

*Proof.* Resultants are multiplicative in each argument: for polynomials
$g,h$ in $U$, $\mathrm{Res}_U(f,gh)=\mathrm{Res}_U(f,g)\,\mathrm{Res}_U(f,h)$
(standard property, `knowledge_base.md`, "Resultants" — immediate from the
roots-product formula $\mathrm{Res}(f,gh)=\mathrm{lc}(f)^{\deg g+\deg
h}\prod_i(gh)(\alpha_i) = \mathrm{lc}(f)^{\deg g}\prod_ig(\alpha_i)\cdot
\mathrm{lc}(f)^{\deg h}\prod_ih(\alpha_i)=\mathrm{Res}(f,g)\mathrm{Res}(f,h)$).
By the Proposition, $\Phi(U)=\tilde P_2\cdot L(U,V_1)\cdot L(U,V_2)$, a
product of the constant $\tilde P_2$ and two factors linear in $U$ (each
$L(U,V_j)=(\sin A\cdot V_j-\cos A)U + (-\cos A\cdot V_j-\sin A-4)$). Hence
$$\mathrm{Res}_U(q_1,\Phi) = \mathrm{Res}_U(q_1,\tilde P_2)\cdot
\mathrm{Res}_U(q_1,L(\cdot,V_1))\cdot\mathrm{Res}_U(q_1,L(\cdot,V_2)).$$
The first factor: $\mathrm{Res}_U(q_1,\tilde P_2)=\tilde P_2^{\deg
q_1}=\tilde P_2^2$ (resultant against a nonzero constant, degree-2 $f$; a
standard immediate case of the roots-product formula with $g$ the constant
$\tilde P_2$, $\prod_i \tilde P_2 = \tilde P_2^2$, times $\mathrm{lc}(f)^0=1$).
The second and third factors, by the Lemma above (with $a=\tilde P_1$,
$(d,e)$ the coefficients of $L(\cdot,V_j)$, so $dU_i+e=L(U_i,V_j)$):
$$\mathrm{Res}_U(q_1,L(\cdot,V_j)) = \tilde P_1\,L(U_1,V_j)\,L(U_2,V_j),\quad j=1,2.$$
Multiplying all three factors:
$$\mathrm{Res}_U(q_1,\Phi) = \tilde P_2^2\cdot\tilde P_1L(U_1,V_1)L(U_2,V_1)\cdot\tilde P_1L(U_1,V_2)L(U_2,V_2)
= \tilde P_1^2\tilde P_2^2\prod_{i,j}L(U_i,V_j),$$
and $L(U_i,V_j)=F(U_i,V_j)-4$ by definition. $\blacksquare$

**Independent numerical verification (own fresh computation this round).**
Evaluated both sides directly (no symbolic resultant call — computing
$U_{1,2},V_{1,2}$ via the quadratic formula from $\tilde P_1,\tilde
Q_1,\tilde R_1,\tilde P_2,\tilde Q_2,\tilde R_2$, then $F$, then the RHS
product) against the certified constant-term identity
$\Psi(0,A,C)=4\sin^3A\sin B\sin C$ (via the combined formula of Step 2
below, in the limit $\theta\to0^+$) on 5 random triangles: ratio of
computed value to $4\sin^3A\sin B\sin C$ was $1.0000\ldots$ (within
$4\times10^{-5}$, limited only by using $\theta=10^{-6}$ rather than an
exact $\theta=0$ symbolic substitution) in every case — confirming the
Theorem (combined with Step 2's sign facts) reproduces the already-certified
exact value, not merely a proportional or sign-flipped quantity.

### Step 2 (new, proved). Exact sign of the two spurious factors, and a cleaner re-proof that $\tilde P_1,\tilde P_2<0$ on the domain

**Lemma (sign of the spurious factors).** For every $(\theta,A,B,C)$ with
$0<\theta<\min(B,C)$, $A,B,C>0$, $A+B+C=\pi$ (so $\tau=\tan\theta>0$):
$$\tau\cos C-\sin C \;<\;0, \qquad \sin B-\tau\cos B\;>\;0.$$

*Proof.* Since $A,B,C>0$ sum to $\pi$, at most one of them is $\ge\pi/2$
(two angles $\ge\pi/2$ would already sum to $\ge\pi$, leaving no room for
the third positive angle) — so $\min(B,C)<\pi/2$ always (whichever of $B,C$
is not $\ge\pi/2$; if neither is $\ge\pi/2$, trivially $\min(B,C)<\pi/2$;
if exactly one is $\ge\pi/2$, the other, which is the min, is $<\pi/2$
since the third angle $A>0$ forces the two together to be $<\pi$, and if
say $C\ge\pi/2$ then $B=\pi-A-C<\pi/2$). Hence $\theta<\min(B,C)<\pi/2$, so
$\tau=\tan\theta>0$ and $\theta\in(0,\pi/2)$.

*Case $C<\pi/2$:* then $\theta<C<\pi/2$ and $\tan$ is strictly increasing
on $(0,\pi/2)$, so $\tau=\tan\theta<\tan C$, and $\cos C>0$, giving
$\tau\cos C-\sin C = \cos C(\tau-\tan C)<0$.

*Case $C\ge\pi/2$:* then $\cos C\le0$ and (since $\theta>0$) $\tau\cos
C\le0$, while $\sin C>0$ (as $C\in(0,\pi)$); hence $\tau\cos C-\sin C\le
-\sin C<0$.

Either way $\tau\cos C-\sin C<0$. For the second inequality, apply the
identical argument with $B$ in place of $C$ (valid since $\theta<\min(B,C)\le
B$ too): $\tau\cos B-\sin B<0$, i.e. $\sin B-\tau\cos B>0$. $\blacksquare$

**Corollary (re-derivation of $\tilde P_1,\tilde P_2<0$).** On the domain,
$\tilde P_1=\sin A\cdot\tau(\tau\cos C-\sin C)<0$ and $\tilde P_2=\sin
A\cdot\tau(\tau\cos B-\sin B)<0$ (both: product of $\sin A>0$, $\tau>0$,
and a strictly negative factor by the Lemma just proved — for $\tilde P_2$,
using $\tau\cos B-\sin B<0$, the mirror statement proved in the same
paragraph). This reproduces Round 5 Step 1's fact $\tilde P_1<0$ (there
derived via a discriminant-transport argument from the certified
`ptolemy-trig-branch-selection.md` lemma) by a shorter, independent route,
and gives the symmetric fact $\tilde P_2<0$ explicitly for the first time
(previously only asserted "symmetrically" without being spelled out).

### Step 3 (new, proved). The reduction: $\Psi>0 \iff$ an odd number of the four branch values exceed 4

Recall the certified factorization (`ptolemy-resultant-elimination-to-sextic.md`):
$$\mathrm{Res}_U(q_1,\Phi) = \sin^2A\cdot(\tau\cos C-\sin C)\cdot(\sin
B-\tau\cos B)\cdot\Psi(\tau,A,C).$$
Combining with Step 1's Theorem:
$$\Psi(\tau,A,C) = \frac{\tilde P_1^2\tilde P_2^2}{\sin^2A\,(\tau\cos
C-\sin C)(\sin B-\tau\cos B)}\prod_{i,j\in\{1,2\}}\bigl(F(U_i,V_j)-4\bigr).$$
On the open domain $0<\theta<\min(B,C)$: $\sin^2A>0$; by Step 2's Lemma,
$\tau\cos C-\sin C<0$ and $\sin B-\tau\cos B>0$, so their product is
**strictly negative**; and $\tilde P_1^2\tilde P_2^2\ge0$, in fact $>0$
strictly since $\tilde P_1,\tilde P_2<0$ (Step 2's Corollary — in
particular neither vanishes). Hence the prefactor
$\dfrac{\tilde P_1^2\tilde P_2^2}{\sin^2A(\tau\cos C-\sin C)(\sin B-\tau\cos
B)}$ is a well-defined **strictly negative** real number at every point of
the domain (positive numerator, strictly negative nonzero denominator).
Therefore:
$$\boxed{\Psi(\tau,A,C)>0 \iff \prod_{i,j\in\{1,2\}}\bigl(F(U_i,V_j)-4\bigr)<0
\iff \text{an odd number (1 or 3) of the four values } F(U_i,V_j) \text{ exceed } 4.}$$

This is a genuine reduction in kind: the original target was a sign
question about a degree-6-in-$\tau$ polynomial with unwieldy trigonometric
coefficients (Step 0's obstruction); the new target is a sign-parity
question about **four explicit, individually meaningful real numbers**
(the value of the bilinear form $F$ at each of the four combinations of
roots of two already-fully-understood quadratics), each computable in
closed form from $\tilde P_1,\tilde Q_1,\tilde R_1,\tilde P_2,\tilde
Q_2,\tilde R_2$ via the quadratic formula.

### Step 4 (numerical only — the new open gap). The parity claim itself

Verified numerically (fresh computation this round, independent of the
approach file's prior numerics): at 8 random domain points $(A,C,\theta)$
(script below), computing $U_{1,2}=(-\tilde Q_1\mp\sqrt{\Delta_1})/(2\tilde
P_1)$, $V_{1,2}=(-\tilde Q_2\mp\sqrt{\Delta_2})/(2\tilde P_2)$ and all four
values $F(U_i,V_j)$ directly:

| sample | $F(U_1,V_1)-4$ | $F(U_1,V_2)-4$ | $F(U_2,V_1)-4$ | $F(U_2,V_2)-4$ |
|---|---|---|---|---|
| 1 | $+16.79$ | $-7.52$ | $-22.53$ | $-5.29$ |
| 2 | $+16.18$ | $-8.13$ | $-8.08$ | $-5.05$ |
| 3 | $+1005.6$ | $-57.7$ | $-17.2$ | $-4.42$ |
| 4 | $+8.97$ | $-13.80$ | $-31.92$ | $-4.71$ |
| 5 | $+1486.7$ | $-10.10$ | $-80.38$ | $-4.98$ |
| 6 | $+969.1$ | $-7.23$ | $-9.28$ | $-5.14$ |
| 7 | $+5348.5$ | $-29.66$ | $-262.2$ | $-4.71$ |
| 8 | $+608.1$ | $-43.5$ | $-9.58$ | $-4.71$ |

In every sample, $U_1=(-\tilde Q_1-\sqrt{\Delta_1})/(2\tilde P_1)$ (the
**genuine** branch, per the sign convention $\tilde P_1<0$ established in
Step 2 — matches Round 5 Step 1's identification of the genuine root as
the larger one) paired with the genuine $V_1$ is the **unique** one of the
four exceeding $4$; the count of positive entries is exactly $1$ (odd),
matching the required parity and reproducing exactly the pattern Round 4's
independent 100,000-sample diagnostic already found. **This is consistent,
strong, and now doubly-independently-confirmed evidence, but it is not a
proof**: no argument is given here (or previously) for *why* exactly the
genuine-genuine combination is the one that exceeds 4 while the other three
never do, for every triangle and every $\theta$ in range. Two directions
that could plausibly close this, neither attempted to completion this
round for lack of remaining time:
(a) prove directly that $U\ne U_1$ (i.e. $U=U_2$, the spurious root) forces
$F(U,V)<4$ for **either** value of $V$ — this would dispose of two of the
three spurious combinations at once via one lemma, with the symmetric
statement for $V\ne V_1$ disposing of the third; each such lemma is a
single-variable-type inequality (fix the "wrong" root, use its defining
quadratic relation to bound $F$) that might be more tractable than the
raw sextic;
(b) a continuity/IVT argument at the level of each of the four branches
individually (each $F(U_i,V_j)$ is a continuous function of $(\theta,A,C)$
on the domain, since $\Delta_1,\Delta_2\ge0$ throughout by the certified
branch-selection theorem, `ptolemy-trig-branch-selection.md`), reducing
each branch's sign-constancy to one base-point check — but this still
requires ruling out $F(U_i,V_j)=4$ *exactly* somewhere in the domain for
the three spurious branches, which is exactly as hard as the original
per-branch problem, just split into three (unless a slicker joint argument
covering all three at once, e.g. via (a), is found).

### What Step 3's reduction buys, even unfinished
Even without closing Step 4, this round's reduction is a genuine
improvement in the *shape* of the remaining problem: from "a degree-6
polynomial in $\tau$ with coefficients requiring nontrivial ideal-reduction
to even write down (Step 0)" to "an odd number of four explicit real
numbers, each a value of a fixed bilinear form at an explicit
quadratic-formula point, exceeds $4$" — a target for which the population's
already-certified branch-selection machinery
(`ptolemy-trig-branch-selection.md`) and connectedness lemma (Step 6,
Round 5) are more directly applicable, and which does not require ever
extracting Ψ's raw sextic coefficients (avoiding Step 0's computational
obstruction entirely).

### Updated summary of what remains for `ptolemy-trig-identity`
1. **The four-branch parity claim (Round 6 Step 4)** — the single gap
   standing between this approach and a complete, independent solution to
   the whole problem, now reduced (Round 6 Steps 1–3, fully proved) from
   the raw sextic $\Psi(\tau,A,C)>0$ to: *an odd number of the four real
   values $F(U_i,V_j)$, $i,j\in\{1,2\}$ (with $U_{1,2},V_{1,2}$ the roots
   of the two already-certified quadratics), exceeds $4$* — equivalently,
   by Round 6 Step 3's proved identity, exactly $\Psi>0$. Confirmed
   (doubly, across two independent numerical sweeps — Round 4's 100,000
   samples and this round's fresh 8-sample re-check) that the pattern is
   always "genuine branch alone exceeds 4," but this is not proved
   symbolically. Two candidate closing strategies are identified (Round 6
   Step 4(a)-(b)) but not completed. This route (Round 6) also removes the
   need for Round 5's numerical (60-digit) base-point evaluation at the
   equilateral configuration, since $\Psi(0,A,C)=4\sin^3A\sin B\sin C>0$
   is an exact boundary limit already proved — a small additional
   simplification, contingent on the same open gap.
2. The isosceles case $AB=AC$: **resolved this round by the ptolemy-lens
   explorer**, via a free, Q-independent mirror-symmetry argument (`ψ=φ`
   forced when $B=C$, hence $K,L$ are reflections across the triangle's own
   axis of symmetry, hence $O$ lies on that axis, hence $OM=ON$ directly) —
   see the explorer's report; not yet written up as a certified lemma file
   by a builder, recommended for next round (would close the round-1-flagged
   gap for the whole population, not just this approach).
3. The minor pairwise-distinctness/non-collinearity check for the general
   Ptolemy theorem's application (flagged since round 1, still not written
   out in full generality — expected routine, not the true difficulty).

## Round 7 — the `Ξ(V1)`/`Ξ(V2)` radical-isolation route, closed off with an exact equivalence identity to `Ψ`

Dispatch this round: pursue paritylens's `Ξ(V1)·Ξ(V2)<0` sufficiency route
(see `/tmp/round-7/math-explorer-paritylens.md`): isolate the single radical
in `Ξ(V1) := \mathrm{Res}_U(q_1(U), F(U,V_1)-4)` and close via an `a²≷b²Δ2`
comparison plus IVT/continuity on the certified connected domain.

### Step 0 (setup, direct reuse of certified machinery — no new proof needed)

Recall (certified: `ptolemy-resultant-elimination-to-sextic.md`, and Round 6
Step 1's general **Lemma (resultant of a quadratic against a linear
factor)**: for $aU^2+bU+c=a(U-U_1)(U-U_2)$ and $dU+e$,
$\mathrm{Res}_U(aU^2+bU+c,\,dU+e)=a\,(dU_1+e)(dU_2+e)$): define, mirroring
Round 6's $\Phi(U)$ construction but with the roles of $U,V$ exchanged,
$$\Xi(V) := \mathrm{Res}_U\bigl(q_1(U),\ F(U,V)-4\bigr).$$
Writing $F(U,V)-4 = m(V)U+n(V)$ with $m(V)=\sin A\cdot V-\cos A$,
$n(V)=-\cos A\cdot V-\sin A-4$ (i.e. treating $F(U,V)-4$ as linear in $U$ for
fixed $V$ — the mirror decomposition to Round 6's $L(U,V)=mU+n$, linear in
$V$ for fixed $U$), the Lemma above (with $f=q_1(U)$, $a=\tilde P_1$,
roots $U_1,U_2$, $g=m(V)U+n(V)$) gives immediately, **with no new proof
required** (a direct instantiation of the already-certified general Lemma,
roles of $U,V$ swapped — the Lemma's statement and proof do not distinguish
which variable is "the one with the quadratic" beyond notation):
$$\boxed{\Xi(V) = \tilde P_1\cdot\bigl(F(U_1,V)-4\bigr)\bigl(F(U_2,V)-4\bigr).} \qquad (\dagger)$$
Explicitly, expanding via $\Xi(V)=\tilde P_1n(V)^2-\tilde Q_1n(V)m(V)+\tilde
R_1m(V)^2$ (the same formula as Round 6's $\Phi(U)=\tilde P_2n^2-\tilde
Q_2nm+\tilde R_2m^2$, with $1\leftrightarrow2$ and $U\leftrightarrow V$
swapped throughout), $\Xi$ is a polynomial of degree exactly $2$ in $V$:
$$\Xi(V) = c_2V^2+c_1V+c_0.$$
**Independently verified numerically** ($(\dagger)$ checked directly, no
symbolic resultant call, on 5 fresh random domain samples: relative error
$<10^{-13}$ in every case — script `/tmp/round-7/verify_equiv.py`, reproduced
below in Key computations).

### Step 1 (new, proved). The leading coefficient $c_2>0$ throughout the domain — a clean closed form

*Claim.* $c_2 = \dfrac{\sin A\,\sin(A+\theta)\,(\sin B-\tau\cos B)}{\cos\theta}$,
and this is **strictly positive** for every $(\theta,A,B,C)$ in the domain
$0<\theta<\min(B,C)$, $A,B,C>0$, $A+B+C=\pi$.

*Proof.* Direct symbolic expansion of $c_2 = \tilde P_1\,\sin^2A -
\tilde Q_1\sin A\cos A + \tilde R_1\cos^2A$ (the $V^2$-coefficient of
$\tilde P_1n(V)^2-\tilde Q_1n(V)m(V)+\tilde R_1m(V)^2$, using $m(V)=\sin
A\cdot V-\cos A$, $n(V)=-\cos A\cdot V-\sin A-4$, whose $V$-coefficients are
$\sin A$ and $-\cos A$ respectively) in terms of $\tau,\sin A,\cos A,\sin
C,\cos C$ (substituting the closed forms for $\tilde P_1,\tilde Q_1,\tilde
R_1$ from Round 5 Step 1, and $\sin B=\sin A\cos C+\cos A\sin C$, $\cos
B=\sin A\sin C-\cos A\cos C$) gives, after collecting and factoring (verified
by symbolic computation in `sympy`, reproduced below):
$$c_2 = \sin A\cdot(\cos A\cdot\tau+\sin A)\cdot(\cos A\cos C\,\tau+\cos
A\sin C+\cos C\sin A-\sin A\sin C\,\tau).$$
The second factor equals $\sin(A+\theta)/\cos\theta$: writing
$\tau=\sin\theta/\cos\theta$, $\cos A\cdot\tau+\sin A = (\cos A\sin\theta+\sin
A\cos\theta)/\cos\theta = \sin(A+\theta)/\cos\theta$ (angle-addition formula
for sine). The third factor equals $\sin B-\tau\cos B$: grouping,
$\cos A\cos C\,\tau+\cos A\sin C+\cos C\sin A-\sin A\sin C\,\tau =
\tau(\cos A\cos C-\sin A\sin C) + (\cos A\sin C+\cos C\sin A) =
\tau\cos(A+C)+\sin(A+C)$; since $A+C=\pi-B$, $\cos(A+C)=\cos(\pi-B)=-\cos B$
and $\sin(A+C)=\sin(\pi-B)=\sin B$, so this is $-\tau\cos B+\sin B=\sin
B-\tau\cos B$. Hence $c_2 = \sin A\cdot\dfrac{\sin(A+\theta)}{\cos\theta}\cdot
(\sin B-\tau\cos B)$, proving the displayed formula.

For positivity: $\sin A>0$ since $A\in(0,\pi)$. $\theta\in(0,\min(B,C))$
implies (Round 6 Step 2's proof) $\min(B,C)<\pi/2$, so $\theta\in(0,\pi/2)$,
giving $\cos\theta>0$. Also $A+\theta\in(A,\pi)$: since
$\theta<\min(B,C)\le B+C$ trivially and $A+B+C=\pi$, we get
$A+\theta<A+B+C=\pi$; combined with $A+\theta>A>0$, so $A+\theta\in(0,\pi)$
and $\sin(A+\theta)>0$. Finally $\sin B-\tau\cos B>0$ is exactly Round 6
Step 2's certified Lemma. All three factors of the numerator are strictly
positive and the denominator $\cos\theta>0$, so $c_2>0$ throughout the
domain. $\blacksquare$

This is new, reusable, fully closed-form content (a clean structural fact
about $\Xi$ analogous to, but not previously derived for, $\tilde P_1,\tilde
P_2$'s signs), independently confirmed numerically (see Key computations)
via direct evaluation of $c_2$ at 5 random domain points against the boxed
closed form, matching to machine precision.

### Step 2 (new, proved). The single-radical isolation for $\Xi(V_1)$, and its exact meaning

Since $V_1=\dfrac{-\tilde Q_2-\sqrt{\Delta_2}}{2\tilde P_2}$ (the genuine
root, larger since $\tilde P_2<0$ — certified, Round 6 Step 2's Corollary)
and $\Xi(V)=c_2V^2+c_1V+c_0$ is quadratic, substituting and using
$\sqrt{\Delta_2}^2=\Delta_2$ gives, writing $s:=\sqrt{\Delta_2}$:
$$\Xi(V_1) = \frac{a+b\,s}{4\tilde P_2^2}, \qquad
a := c_2(\tilde Q_2^2+\Delta_2)-2\tilde P_2\tilde Q_2\,c_1+4\tilde
P_2^2c_0,\qquad b:=2c_2\tilde Q_2-2\tilde P_2c_1,$$
($a,b$ both radical-free, explicit polynomials in $\tau,A,C$ — this is
exactly the decomposition an elementary substitution of the quadratic
formula into a quadratic function produces; direct algebraic expansion, no
approximation).

**Since $V_2=\dfrac{-\tilde Q_2+\sqrt{\Delta_2}}{2\tilde P_2}$ is obtained
from $V_1$ by the single substitution $s\mapsto -s$, and $\Xi(V)$ is a
polynomial (hence its value at $V_1$, expanded in $s$, is linear in $s$ by
the same computation), the identical substitution applied to the same
expansion gives**
$$\Xi(V_2) = \frac{a-b\,s}{4\tilde P_2^2}$$
**with the *same* $a,b$** — this is not a separate computation, it is the
same algebraic expansion evaluated at $s\to-s$, forced by the fact that
$c_2,c_1,c_0,\tilde Q_2,\tilde P_2$ do not involve $s$ at all (they are
functions of $\tau,A,C$ alone; only $V_1,V_2$ themselves depend on $s$, via
$\mp$). **Independently verified numerically** to $<10^{-12}$ relative error
on 5 fresh random domain samples (`/tmp/round-7/verify_equiv.py`, Key
computations).

**Consequence (the key identity of this round).** Multiplying,
$$a^2-b^2\Delta_2 = (a+bs)(a-bs) = 16\,\tilde P_2^4\,\Xi(V_1)\,\Xi(V_2).$$
By $(\dagger)$ applied to both $V_1$ and $V_2$:
$$\Xi(V_1)\Xi(V_2) = \tilde P_1^2\prod_{i,j\in\{1,2\}}\bigl(F(U_i,V_j)-4\bigr).$$
So
$$a^2-b^2\Delta_2 = 16\,\tilde P_1^2\tilde P_2^4\prod_{i,j}\bigl(F(U_i,V_j)-4\bigr). \qquad (\ddagger)$$

### Step 3 (new, proved — the main finding of this round). The `a²≷b²Δ2` comparison is EXACTLY the `Ψ` question, not a new one

By the already-certified factorization
(`ptolemy-resultant-elimination-to-sextic.md`, restated in the file's Round
6 Step 3):
$$\Psi(\tau,A,C) = \frac{\tilde P_1^2\tilde
P_2^2}{\sin^2A\,(\tau\cos C-\sin C)(\sin B-\tau\cos B)}\prod_{i,j}\bigl(F(U_i,V_j)-4\bigr),$$
so
$$\prod_{i,j}\bigl(F(U_i,V_j)-4\bigr) = \frac{\sin^2A\,(\tau\cos C-\sin
C)(\sin B-\tau\cos B)}{\tilde P_1^2\tilde P_2^2}\,\Psi(\tau,A,C).$$
Substituting into $(\ddagger)$:
$$a^2-b^2\Delta_2 = 16\,\tilde P_1^2\tilde P_2^4\cdot\frac{\sin^2A\,(\tau\cos
C-\sin C)(\sin B-\tau\cos B)}{\tilde P_1^2\tilde P_2^2}\,\Psi(\tau,A,C) =
16\,\tilde P_2^2\sin^2A\,(\tau\cos C-\sin C)(\sin B-\tau\cos
B)\cdot\Psi(\tau,A,C). \qquad (\star\star)$$
**This is an exact algebraic identity** (chain of already-certified facts
plus the elementary radical-isolation algebra of Step 2 — no numerics
needed for its derivation, though independently confirmed to $<10^{-9}$
relative error at 5 domain samples, Key computations).

By the already-certified sign facts (Round 6 Step 2's Lemma: $\tau\cos
C-\sin C<0$, $\sin B-\tau\cos B>0$ throughout the domain) and $\tilde
P_2^2>0$, $\sin^2A>0$: the coefficient $16\,\tilde P_2^2\sin^2A(\tau\cos
C-\sin C)(\sin B-\tau\cos B)$ is **strictly negative** at every point of the
domain (product of a positive quantity and a strictly negative one). Hence
$(\star\star)$ shows:
$$\boxed{a^2-b^2\Delta_2 \text{ and } \Psi(\tau,A,C) \text{ have OPPOSITE sign at every point of the domain } D,}$$
i.e. $\Psi>0\iff a^2<b^2\Delta_2$ pointwise, with the two sides literally
proportional via an explicit, sign-known negative constant.

**Interpretation — an honest negative finding for this specific route, not a
new gap.** The outline's plan was to isolate $\Xi(V_1)$'s single radical and
settle its non-vanishing/sign via the polynomial comparison $a^2\gtrless
b^2\Delta_2$, hoping this would be strictly easier than the raw sextic
$\Psi>0$ (radical-clearing sometimes does simplify a target — e.g. it did in
Round 5, going from two nested radicals in $F$ down to the radical-free
$\Psi$). **Here it provably does not**: $(\star\star)$ shows $a^2-b^2\Delta_2$
is, up to an explicit and already-fully-understood sign-definite constant,
*literally* $\Psi$ again — not a smaller-degree or structurally simpler
object, but the same polynomial reached by a different resultant chain. This
is forced by a structural reason, not a coincidence of this particular
computation: $\Xi(V_1)$'s own definition already sums the effect of *both*
roots $U_1,U_2$ of $q_1$ (via $(\dagger)$), so clearing its remaining radical
(coming from $q_2$'s $\sqrt{\Delta_2}$) necessarily reconstructs $\Xi(V_2)$
as well (Step 2's $s\mapsto-s$ observation) — i.e. any attempt to clear
*all* the radicals in this problem, regardless of the order/route chosen,
must eventually recombine to the full four-term product $\prod_{i,j}(F(U_i,V_j)-4)$,
of which $\Psi$ (up to the same explicit sign-definite prefactor already
used throughout the population) is the unique radical-free avatar. This
matches — and gives an exact algebraic reason for — paritylens's own
independent finding this round that the alternative joint-resultant route
$\Omega:=\mathrm{Res}_V(q_2,\Xi)$ produces a degree-8 polynomial "no simpler
than $\Psi$": both findings are instances of the same underlying fact, that
full radical-clearing in this specific two-quadratic-plus-bilinear-form
system has no route around reconstructing the complete four-branch product.

**What this leaves open.** The core gap is unchanged in substance:
$\Psi(\tau,A,C)>0$ throughout $D$ (equivalently, the four-branch odd-parity
claim) remains unproved. What Step 3 contributes is a *rigorous closure* of
one specific proposed route (radical isolation on $\Xi(V_1)$ alone) as
provably equivalent-in-difficulty rather than a shortcut — valuable
negative information (per CLAUDE.md's rigor rules: an honest, fully-derived
negative result), sparing future rounds from re-attempting this exact plan
expecting a computational win. The one genuinely new positive fact
established this round, Step 1's $c_2>0$, is a clean structural lemma about
$\Xi$'s shape (not by itself sufficient to close the gap, since knowing the
leading coefficient of a quadratic is positive says nothing about its values
at two externally-specified points $V_1,V_2$ without further work — and any
"further work" pursuing this exact axis has now been shown, via
$(\star\star)$, to be exactly as hard as $\Psi>0$ itself).

### Key computations (Round 7)
Verified in Python (`/tmp/round-7/verify_equiv.py`, `/tmp/round-7/ptolemy_calc.py`,
`/tmp/round-7/ptolemy_calc3.py` — fresh scripts this round, double precision
throughout unless noted):
- $(\dagger)$, $\Xi(V)=\tilde P_1(F(U_1,V)-4)(F(U_2,V)-4)$: checked at $V=V_1$
  on 5 random domain samples, relative error $<10^{-13}$ in every case.
- Step 1's closed form for $c_2$ (extracted via `sympy.factor` on the raw
  polynomial in $\tau,\sin A,\cos A,\sin C,\cos C$, then identified in closed
  trigonometric form by hand and re-verified by symbolic re-expansion):
  matches the boxed formula exactly (symbolic, not just numeric — see
  `ptolemy_calc3.py`).
- Step 2/3's identity $(\star\star)$: verified numerically (5 random domain
  samples) by computing $a,b$ via a 3-point linear-system fit to $\Xi$'s
  three coefficients (avoiding a symbolic re-derivation of $c_1,c_0$'s full
  closed form, which — like $\Psi$'s own raw coefficients, Round 6 Step 0 —
  requires Gröbner-ideal reduction to become legible; the *numeric* fit
  suffices to confirm $(\ddagger)$ and, combined with the exact symbolic
  chain from $(\ddagger)$ to $(\star\star)$ via the already-certified
  $\Psi$-factorization, gives full confidence in $(\star\star)$ without
  needing that reduction): $a^2-b^2\Delta_2$ matched $16\tilde P_2^4\Xi(V_1)\Xi(V_2)$
  to $<10^{-9}$ relative error at every sample, and its sign was negative at
  every sample (consistent with $\Psi>0$ there, as required by
  $(\star\star)$'s established negative proportionality).

### Updated summary of what remains for `ptolemy-trig-identity`
1. **`Ψ(τ,A,C)>0` throughout `D`** (equivalently the four-branch odd-parity
   claim) is still the single core open gap, unchanged in substance by this
   round. This round rigorously closes off the specific "isolate $\Xi(V_1)$'s
   radical, compare $a^2\gtrless b^2\Delta_2$" route as provably equivalent
   in difficulty (identity $(\star\star)$), not a shortcut — an honest,
   fully-derived negative result, not a new gap. Any future attempt must
   engage with $\Psi$ (or a genuinely different reformulation not built from
   clearing this problem's own radicals in some order) rather than expect a
   free simplification from radical-clearing here.
2. The isosceles case $AB=AC$: resolved by the ptolemy-lens explorer
   (Round 6 note); not yet written up as a certified lemma file.
3. The minor pairwise-distinctness/non-collinearity check for the general
   Ptolemy theorem's application (flagged since round 1, still not written
   out in full generality — expected routine).

## Round 8 — the "eliminate via x,y directly" lever is algebraically IDENTICAL to the exhausted U=cotα route (proved, not numerical); a new radical-free resolvent quartic constructed instead, verified but not closed

Dispatch this round: attack the `Ψ>0`/`F(p,x,y)>0` gap via a "previously untried, cheap lever" —
substitute the certified closed-form roots `x=cotψ(p)`, `y=cotφ(p)` of the two
certified quadratics `(III)′,(IV)′` directly into the boxed identity
`F(p,x,y):=sinA(p+2x)(p+2y)−sinA−cosA(2p+2x+2y)` to eliminate `x,y` and get a
radical-free target purely in `p=cotθ`.

### Step 0 (new — proved). The proposed lever is NOT independent of the exhausted `U=cotα` route: it is the identical computation in disguise

*Claim.* Let `x,y` denote the genuine roots of `(III)′,(IV)′` (Step 3,
certified), and let `U:=p+2x`, `V:=p+2y` (Step 0 of Round 4, certified:
`cotα=p+2cotψ`, `cotα'=p+2cotφ`). Then, **as an identity of real numbers, not
merely as numerically equal quantities**,
$$F(p,x,y) \;=\; \sin A\cdot(p+2x)(p+2y) - \sin A - \cos A(2p+2x+2y) \;=\; \sin A\cdot UV - \sin A - \cos A(U+V) \;=\; F(U,V),$$
term-for-term, with no approximation — because `(p+2x)(p+2y)` and `UV` are
literally the same product (`U,V` are *defined*, not merely coincidentally
equal, to be `p+2x,p+2y`) and `2p+2x+2y=(p+2x)+(p+2y)=U+V` likewise. Hence
substituting the genuine closed forms for `x,y` (Step 3's quadratic-formula
roots of `(III)′,(IV)′`) into `F(p,x,y)` and substituting the genuine closed
forms for `U,V` (Round 5 Step 1's quadratic-formula roots of the *derived*
quadratics `(III)'',(IV)''` for `cotα,cotα'`) into `F(U,V)` **must produce
the same number at every point of the domain**, since `(III)'',(IV)''` were
*themselves derived* (Round 5 Step 1, certified) by the purely algebraic
substitution `x=(U-p)/2` into `(III)′` (and symmetrically for `y,V`) — so the
discriminants `D_1$ (of `(III)′` in `x`) and `Δ_1` (of `(III)''` in `U`)
satisfy `Δ_1 = D_1\cdot(1+τ^2)^2/4` exactly (both are discriminants of the
*same* quadratic equation, related by the affine substitution `U=p+2x`, which
scales the discriminant by the square of the leading-coefficient ratio — a
standard, elementary fact about discriminants under an affine change of
variable, reused implicitly by Round 5's own "$\tilde P_1=c_1(1+\tau^2)/2$"
identity), hence `√Δ_1` and `√D_1` differ only by the *positive* rational
factor `(1+τ^2)/2`, which is exactly the same factor relating `U0:=p-b_1/c_1`
(the rational part of `U`'s closed form) to `U`'s own closed form via the same
substitution — the two "genuine root" selections (Step 3 here vs. Round 5
Step 1) pick out the *same* branch under this correspondence, since both are
characterized by the same geometric containment condition transported through
the same monotone substitution `U=p+2x`. Independently re-verified
numerically (fresh `mpmath`, `dps=50`, own from-scratch script, not reusing
any prior file's code) at 4 random domain points, `A,C` random,
`θ` random fractions of `min(B,C)`: `F` computed via the `x,y` closed forms
and `F` computed via the `U,V` closed forms agree to at least 49 of 50
digits at every sample (residual `≤2\times10^{-49}`, consistent with pure
floating/precision noise, not a genuine discrepancy). ∎

**Consequence.** This is an important, previously-unstated *negative*
clarification, not merely a redundant numeric check: **the outline's
premise that this lever "bypasses the previously-exhausted `U=cotα` route"
is false.** Eliminating `x,y` via `(III)′,(IV)′` and eliminating `U,V` via
`(III)'',(IV)'')` are the *same* elimination, connected by an exact, already-
certified affine substitution (Round 5 Step 1) — any radical-free polynomial
in `p` (or `τ=1/p`) that results from clearing `x,y`'s radicals must, after
the same affine change of variable, be proportional to (or literally coincide
with, up to the harmless rescaling already accounted for by Round 5's own
derivation) a polynomial already reachable from the `U,V` route — in
particular, the already-attempted-and-still-open `Ψ(\tau,A,C)` sextic (Round
5–6) is exactly this kind of object. So a literal "clear `x,y`'s radicals via
resultants, get a new sextic" repeat of Round 5–6's own construction would
not produce new content — consistent with, and explaining in retrospect,
why Round 4's own Step 4 (attempting exactly this substitution) stalled on
"two nested square roots" without further progress, and why Round 5 pivoted
to `U,V$ instead (not because `x,y` were harder, but because it is the
identical target either way).

### Step 1 (new — proved, a genuinely different construction). A radical-free 4-branch resolvent quartic for `F`

Rather than repeat the resultant-elimination route (Step 0 shows it cannot
give new content), a genuinely different — and cheaper — construction is
available: **directly average `F` over the four sign choices of the two
radicals**, instead of eliminating them via a resultant.

Write `F = R - m_1r_1 - m_2r_2 + \sin A\,r_1r_2` where (all *exactly*,
by direct algebraic expansion of `F(p,x,y)` with `x=(-b_1-\sqrt{D_1})/(2c_1)`,
`y=(-b_2-\sqrt{D_2})/(2c_2)$ substituted in and regrouped into "rational part"
plus "radical part"):
$$U_0:=p-\frac{b_1}{c_1},\quad V_0:=p-\frac{b_2}{c_2},\quad
R:=\sin A\,U_0V_0-\sin A-\cos A(U_0+V_0),$$
$$m_1:=\sin A\,V_0-\cos A,\quad m_2:=\sin A\,U_0-\cos A,\quad
r_1:=\frac{\sqrt{D_1}}{c_1},\quad r_2:=\frac{\sqrt{D_2}}{c_2}$$
(so the genuine `F=R-m_1r_1-m_2r_2+\sin A\,r_1r_2`, matching `x=U_0/2-r_1/2`... — more precisely $U=U_0-r_1$, $V=V_0-r_2$, and expanding $F=\sin A(U_0-r_1)(V_0-r_2)-\sin A-\cos A(U_0-r_1+V_0-r_2)$ directly gives the displayed grouping; **independently verified this grouping is an exact algebraic identity** by symbolic re-expansion, residual 0).

Since `r_1^2=d_1:=D_1/c_1^2` and `r_2^2=d_2:=D_2/c_2^2` are themselves
rational (no radical) once `D_1,c_1,D_2,c_2` are expressed in `\tau=\tan\theta`
(exactly as Round 5 Step 1 did for the affine-transformed quadratics — the
same denominator-clearing argument applies verbatim here, since `D_1/c_1^2`
is invariant under the affine rescaling that turned `c_1,b_1,a_1` into
`\tilde P_1,\tilde Q_1,\tilde R_1`), consider the four numbers
$$F_{s_1,s_2} := R - s_1m_1\sqrt{d_1} - s_2m_2\sqrt{d_2} + s_1s_2\sin A\sqrt{d_1d_2}, \qquad s_1,s_2\in\{+1,-1\},$$
obtained by evaluating the same bilinear expression at all four sign choices
of `(r_1,r_2)` (only one of which, per Round 4's own diagnostic finding, is
the genuine branch). **Claim.** These four numbers are exactly the four roots
of the explicit, fully radical-free quartic
$$P(t) := t^4 - 4R\,t^3 + e_2\,t^2 - e_3\,t + e_4,$$
$$e_2 = 6R^2-2d_1d_2\sin^2A-2d_1m_1^2-2d_2m_2^2,$$
$$e_3 = 4R^3-4Rd_1d_2\sin^2A-4Rd_1m_1^2-4Rd_2m_2^2+8d_1d_2m_1m_2\sin A,$$
$$e_4 = R^4-2R^2d_1d_2\sin^2A-2R^2d_1m_1^2-2R^2d_2m_2^2+8Rd_1d_2m_1m_2\sin A+d_1^2d_2^2\sin^4A-2d_1^2d_2m_1^2\sin^2A+d_1^2m_1^4-2d_1d_2^2m_2^2\sin^2A-2d_1d_2m_1^2m_2^2+d_2^2m_2^4.$$

*Proof.* Direct computation: `P(t):=\prod_{s_1,s_2}(t-F_{s_1,s_2})`; expanding
with `u:=s_1\sqrt{d_1}$, `v:=s_2\sqrt{d_2}` ranging independently over the two
sign choices each, `F_{s_1,s_2}=R-m_1u-m_2v+\sin A\,uv` is *linear* in each of
`u,v` separately, so the elementary symmetric functions of the 4 values (as
`u,v` range over `\{\pm\sqrt{d_1}\}\times\{\pm\sqrt{d_2}\}`) collapse to
polynomials in `R,m_1,m_2,\sin A,d_1,d_2` alone (every odd power of `u` or
`v` that would carry a surviving radical cancels in the sum, since the four
terms pair up under `u\to-u$ and `v\to-v` independently). Computed exactly by
symbolic expansion (own fresh `sympy` session): sum of the 4 values `=4R`
(the `\pm m_1u$, `\pm m_2v$, `\pm\sin A\,uv` cross terms all cancel pairwise
over the 4 sign choices, leaving only the `4R` from the four copies of `R`);
sum of pairwise products `=e_2`; sum of triple products `=e_3`; product of
all 4 `=e_4` — all computed by direct expansion with `sympy`, zero residual
against the displayed closed forms. ∎ (Independently re-verified numerically,
`mpmath`, `dps=50`: at 8 diverse domain samples — see table below — `P(t)`'s
roots computed via `mpmath.polyroots` match the four `F_{s_1,s_2}` values
computed directly from the closed-form radicals, to at least 45 of 50 digits
at every sample and every root.)

### Step 2 (numerical only — the honest open gap). `P(t)` empirically has exactly one positive real root, matching the genuine branch

Evaluated `P(t)`'s roots at 8 diverse domain samples (own fresh `mpmath`
script, `dps=50`, `A,C` random in `(0,\pi)$ with `A+C<\pi`, `\theta$ random
fractions of `\min(B,C)`):

| `A` | `C` | `θ/min(B,C)` | real roots of `P` |
|---|---|---|---|
| 0.7 | 0.9 | 0.3 | −6.969, −5.807, −0.749, **27.123** |
| 0.5 | 1.2 | 0.6 | −5.807, −4.458, −1.474, **12.339** |
| 1.0 | 0.4 | 0.1 | −51.969, −14.123, −0.305, **742.132** |
| 0.3 | 0.3 | 0.8 | −45.575, −4.654, −1.357, **23.045** |
| 0.05 | 0.05 | 0.5 | −155.469, −46.562, −4.169, **207.079** |
| 1.4 | 1.4 | 0.9 | −4.984, −3.795, −0.984, **356.701** |
| 0.2 | 1.0 | 0.95 | −82.523, −5.445, −2.630, **8.237** |
| 1.5 | 0.05 | 0.5 | −379.042, −5.248, −0.765, **6758.040** |

At every single sample: **all four roots of `P` are real**, and **exactly one
is positive** — matching the already-certified genuine branch's `F`-value
(the bold entry, independently cross-checked against the direct closed-form
`F` computation, e.g. `A=0.7,C=0.9`: direct `F=27.123023537659976\ldots`,
`P`'s positive root `=27.123023537659976\ldots$, agreement to 40+ digits) —
and consistent with Round 4's separately-certified diagnostic ("(−,−) gives
`F>0` always; every other sign combination gives `F<0` always").

**This numeric pattern — `P(t)` always has exactly 3 negative and 1 positive
real root — is the precise sub-target this construction reduces the whole
gap to, but it is NOT proved here.** A partial structural observation:
since (by Vieta, forced abstractly *if* the root pattern holds) the product
of the 4 roots would be `(\text{neg})(\text{neg})(\text{neg})(\text{pos})<0`,
the pattern implies `e_4<0` throughout the domain — an explicit, fully
radical-free polynomial inequality in `R,m_1,m_2,d_1,d_2,\sin A` (all
themselves explicit rational functions of `\tau=\tan\theta,A,C`, per Step 1)
which is a *necessary* consequence of, but does not by itself establish, the
"exactly 1 positive root" claim (a quartic can have `e_4<0` with 2 or 4 real
roots too, of either sign split, in general — ruling out the other sign
patterns consistent with `e_4<0` was not attempted this round; it would
require either a full Descartes'-rule-of-signs argument on `(1,-4R,e_2,-e_3,
e_4)$, which needs signs of `R,e_2,e_3` too (not uniformly signed across the
8 samples — `R$ itself is negative at 2 of the 8 sample points above, e.g.
`A=0.3,C=0.3$ and `A=0.2,C=1.0`), or a direct discriminant/root-counting
argument specific to this quartic family). Attempted numerically confirming
`e_4<0` at all 8 sample points (own computation, matches the product of the
4 tabulated real roots at every sample to the displayed precision) — this
part is a fully confirmed *consequence*, not an independent new fact.

### Step 3 — honest assessment: does this close the gap?

**No — Status remains `partial`.** What Round 8 establishes, rigorously:
(a) the outline's proposed lever, taken literally (eliminate `x,y` via a
resultant), is *provably* the same computation as the already-exhausted
`U=cotα` route (Step 0) — a genuine negative clarification correcting the
outline's framing, saving future rounds from re-deriving the same sextic
under a different name; (b) a genuinely different, cheaper construction (the
four-branch-average resolvent quartic `P(t)`, Step 1) is fully derived and
proved as an exact algebraic identity, reducing "genuine branch has `F>0`"
to "`P(t)` has exactly one positive real root" — a well-posed, explicit,
radical-free (once `d_1,d_2,R,m_1,m_2` are expressed via `\tau=\tan\theta`
following Round 5 Step 1's denominator-clearing technique) target, verified
at 8 diverse samples with **zero exceptions** to the claimed root pattern.
**What is not proved**: the root-pattern claim itself (Step 2), for all
`(\theta,A,C)$ in the domain. This is a genuinely new open sub-target — not
identical in form to `\Psi(\tau,A,C)>0$ (it is a statement about a resolvent
quartic's root distribution, built from different intermediate quantities
`R,m_1,m_2,d_1,d_2`, rather than a single sextic's sign) — but it has not
been shown to be *easier* than `\Psi>0` either; only that it is a different,
equally-valid-looking angle of attack, cheaply constructed (no resultant
machinery needed, just Vieta on 4 explicit sign-branch evaluations). **The
whole `OM=ON` proof via this route is NOT completed by this round's work**:
tracing the dependency chain, `F>0` (hence `\Psi>0`, hence `\alpha+\alpha'<A`,
hence the Ptolemy-equality concyclicity, hence `OM=ON` via Lemmas R/Q1/Red)
still rests on the unproved Step 2 claim above (or on the pre-existing,
equally unproved `\Psi>0$) — no new gap-closing content, only a new,
honestly-reported candidate route plus a corrected understanding of why the
originally-dispatched lever cannot itself close anything new.

## Promotable lemmas
- **Round 8: the `x,y`-elimination lever is identical to the `U,V`-elimination
  route** (Step 0 above): `F(p,x,y)` with `x,y` the genuine closed-form roots
  of `(III)′,(IV)′` equals, term-for-term, `F(U,V)` with `U=p+2x,V=p+2y` the
  genuine closed-form roots of the *derived* `(III)'',(IV)''` (Round 5 Step
  1) — because `U,V` are literally defined as `p+2x,p+2y`, and the two
  "genuine root" selections agree under this affine correspondence. Proved
  in full (no gap); reusable as a general caution: whenever a target is first
  derived by substituting one variable's certified root-formula into a second
  variable's derived quadratic (as Round 5 did, `x\to U$), a later attempt to
  "instead eliminate the first variable directly" cannot produce new content
  — it is the same elimination unless a genuinely different combining
  operation (not a resultant) is used.
- **Round 8: four-branch resolvent quartic for `F`** (Step 1 above): the four
  sign-branch values `F_{s_1,s_2}=R-s_1m_1\sqrt{d_1}-s_2m_2\sqrt{d_2}+
  s_1s_2\sin A\sqrt{d_1d_2}` are exactly the four roots of the explicit,
  fully radical-free quartic `P(t)=t^4-4Rt^3+e_2t^2-e_3t+e_4` (closed forms
  for `e_2,e_3,e_4` given above), proved via the elementary-symmetric-function
  expansion of a bilinear form evaluated at the four sign-corners of a
  rectangle. This is a general-purpose construction (not specific to this
  problem's `R,m_1,m_2,d_1,d_2$) — reusable anywhere a bilinear expression in
  two independent `\pm\sqrt{}` radicals needs a radical-free resolvent for
  its four branch values, e.g. the population's other "isolate two radicals"
  obstructions.
- **Round 7: closed form and positivity of $\Xi(V)$'s leading coefficient**
  (Step 1 above): $c_2 = \sin A\sin(A+\theta)(\sin B-\tau\cos B)/\cos\theta
  > 0$ throughout the domain $D$, where $\Xi(V):=\mathrm{Res}_U(q_1(U),
  F(U,V)-4)=c_2V^2+c_1V+c_0$. Proved via direct algebraic factorization of
  the raw coefficient plus the already-certified sign lemma
  (`ptolemy-resultant-elimination-to-sextic.md`, "$\sin B-\tau\cos B>0$").
  Reusable wherever the population needs a clean sign fact about this
  mirror-construction resultant.
- **Round 7: exact equivalence between the single-radical-clearing target
  and $\Psi$** (Step 3 above, identity $(\star\star)$): for $\Xi(V_1)$'s
  radical-isolated form $\Xi(V_1)=(a+b\sqrt{\Delta_2})/(4\tilde P_2^2)$
  (Step 2), $$a^2-b^2\Delta_2 = 16\,\tilde P_2^2\sin^2A\,(\tau\cos C-\sin
  C)(\sin B-\tau\cos B)\cdot\Psi(\tau,A,C),$$ with the prefactor strictly
  negative throughout $D$ by already-certified sign facts — proving
  $a^2\gtrless b^2\Delta_2 \iff \Psi\lessgtr0$ exactly. Proved via the
  general resultant-of-quadratic-vs-linear Lemma (Round 6 Step 1, reused
  verbatim with $U,V$ roles exchanged) plus elementary radical-isolation
  algebra plus the already-certified $\Psi$-factorization. Reusable
  as a template: whenever a target quadratic-system inequality's
  "clear-the-radical-and-compare-squares" reformulation is suspected to be a
  disguised restatement of an already-isolated polynomial (rather than a
  genuine simplification), this identity chain (radical isolation →
  $s\mapsto-s$ symmetry → resultant-of-quadratic-vs-linear → substitution
  into the master factorization) gives a systematic way to check/prove the
  equivalence rigorously instead of guessing from numerics alone.
- **Round 6: multiplicative resultant identity for the sextic Ψ** (Step 1
  above): for the specific bilinear-elimination construction
  $\mathrm{Res}_U(q_1,\Phi)$ used in `ptolemy-resultant-elimination-to-sextic.md`
  (with $\Phi(U)=\mathrm{Res}_V(q_2,L)$ up to the standard linear-resultant
  normalization), the identity $\mathrm{Res}_U(q_1,\Phi)=\tilde P_1^2\tilde
  P_2^2\prod_{i,j}(F(U_i,V_j)-4)$ holds exactly, proved via (i) the general
  fact that $\mathrm{Res}_V(\text{quadratic},\ mV+n)=\text{quadratic's
  leading coeff}\times(\text{quadratic evaluated at each root's
  }L\text{-value})$ and (ii) resultant multiplicativity in the second
  argument. Both ingredients are proved here in general (not just for this
  problem's specific $q_1,q_2,L$), so this is reusable by any approach
  needing to relate a chained-resultant elimination back to explicit
  root-values — in particular directly applicable to the coordinate-based
  approaches' own branch-selection/elimination gaps, which have the same
  "two quadratics + a bilinear target condition" shape.
- **Round 6: sign of the two spurious linear factors, redone directly**
  (Step 2 above): $\tau\cos C-\sin C<0$ and $\sin B-\tau\cos B>0$
  throughout the open domain $0<\theta<\min(B,C)$, proved via the
  elementary fact that at most one triangle angle can be $\ge\pi/2$ (so
  $\min(B,C)<\pi/2$ always) plus a direct case split on $\mathrm{sign}(\cos
  C)$ (resp. $\cos B$) — shorter than Round 5's route (which cited
  `ptolemy-trig-branch-selection.md`'s $\tan$-injectivity argument only for
  *non-vanishing*, not sign). This directly yields $\tilde P_1,\tilde
  P_2<0$ on the domain as an immediate corollary (one line each), giving a
  new, shorter proof of Round 5 Step 1's fact and, for the first time, an
  explicit proof of the symmetric fact $\tilde P_2<0$ (previously only
  asserted "symmetrically").
- **Round 5: direct quadratic for $\cot\alpha$** (Step 1 above): $U=\cot\alpha$
  (the genuine root, bypassing $\cot\psi$ entirely) satisfies the explicit
  quadratic $\tilde P_1U^2+\tilde Q_1U+\tilde R_1=0$ with the closed-form
  coefficients given in Step 1, obtained by a routine but fully proved
  algebraic substitution from the certified $\cot\psi$-quadratic; genuine
  root is the larger one since $\tilde P_1<0$ throughout the domain (proved).
  Reusable wherever the population needs a direct closed form for $\cot\alpha$
  without the intermediate $\psi$ variable.
- **Round 5: resultant-elimination reduction of $F>4$ to a radical-free
  polynomial** (Steps 2–4 above): for a bilinear target condition
  $L(U,V)=0$ where $U,V$ each solve their own quadratic, the successive
  resultant elimination $\mathrm{Res}_U(q_1,\mathrm{Res}_V(q_2,L))$ produces
  a polynomial purely in the remaining parameters whose nonvanishing rules
  out $L=0$ for *any* combination of the roots — proved in general (not
  just for this problem's specific $L$), with the two spurious linear
  factors in this application rigorously identified as exactly the
  domain-boundary loci $\theta=B,\theta=C$ (Step 4, elementary, general
  argument about $\tan$-injectivity on $(0,\pi)\setminus\{\pi/2\}$). This
  elimination technique (reduce a target inequality on the geometric branch
  of a two-quadratic system to a single radical-free polynomial via chained
  resultants, then rule out sign changes via IVT/connectedness) is reusable
  by any approach in this population (or elsewhere) facing a similar
  "prove an inequality on the correct root of a quadratic system" obstacle
  — directly applicable, in particular, to the still-open coordinate-route
  branch-selection gap, which has the same shape (root of a quadratic
  system, need a sign fact on the geometric branch).
- **Round 5: domain path-connectedness** (Step 6 above): the parameter
  domain $\{(A,C,\theta):A,C>0,A+C<\pi,0<\theta<\min(\pi-A-C,C)\}$ is
  path-connected — a short, fully general topological lemma (convexity of
  the base triangle plus a continuous positive fiber function), reusable
  wherever an IVT/no-sign-change argument is needed over this exact
  parameter domain (which recurs throughout this whole population's
  $\theta$-parametrization).
- **Round 4: quadratic reduction + branch-selection theorem for (III)/(IV)**
  (Steps 2–3 above): (III) is exactly equivalent (no squaring) to the
  quadratic $c_1\cot^2\psi+b_1\cot\psi+a_1=0$ with explicit trig coefficients
  $a_1,b_1,c_1$ in $\theta,A,C$; the genuine root is proved (IVT + quadratic-
  degree argument, not numerics) to be the unique root in $(0,C-\theta)$,
  explicitly $\cot\psi = (-b_1-\sqrt{D_1})/(2c_1)$. Symmetric statement for
  (IV)/$\varphi$/$B$. This is a fully general, all-triangle, all-$\theta$
  branch-selection proof — reusable by any future approach needing to pin
  down which root of a "two-branch" trig/algebraic system is geometric
  (the same phenomenon as the coordinate approaches' still-open branch
  selection, resolved here for this parametrization).
- **General Ptolemy equality theorem** (see above): for four pairwise
  distinct, not-three-collinear points, $WY\cdot XZ = WX\cdot YZ + XY\cdot WZ$
  implies W,X,Y,Z concyclic. Proved in full via the complex-number identity
  $(w-y)(x-z)=(w-x)(y-z)+(x-y)(w-z)$, the triangle-inequality equality
  condition, and the real-cross-ratio concyclicity criterion. Fully general,
  reusable in any problem requiring a Ptolemy-equality-based concyclicity
  proof; removes the need for a separate synthetic "cyclic order" lemma.
- **Lemma 1–3 (explicit two-ray construction of K, L; closed forms for AK,
  BK, AL, CL; decoupled constraint equations (III), (IV))**: proved in full
  above, independently numerically verified. Reusable by any future approach
  to this problem (e.g. as an alternative to coordinate-bash's coordinate
  parametrization, in angle variables instead).
- **Lemma 4 (AQ = |b²−c²|/(2a))**: proved in full, reusable closed form for
  the fixed point Q's distance to A.
- **Lemma S1 (ray-angle determines cyclic order)**: for a circle ω and fixed
  point A∈ω, the map from ω∖{A} to the direction-angle of ray AP is strictly
  monotonic with total sweep exactly π, so sorting any finite set of points
  on ω∖{A} by their ray-angle from A recovers their exact cyclic order.
  Proved in full (unit-circle computation + similarity invariance) above.
  Reusable in any problem needing to determine cyclic order on a circle
  through a known point via angles measured from that point — a clean
  general-purpose lemma, not specific to this problem's configuration.
- **Lemma S2 (direction angle of AQ = π−B or −B)**: proved in full via the
  standard projection identity c = a cos B + b cos A (itself proved via Law
  of Sines + sin(A+B)=sin(π−C)=sin C). Reusable wherever this Q-construction
  (reflection of A in the perpendicular bisector of the midpoints) recurs.
- **Lemma S3 (containment bounds 0<∠BAK,∠BAL<A)**: proved in full directly
  from the problem's own hypotheses (K∈int(BMC)⊆ABC, L∈int(BNC)⊆ABC).
  Reusable as a basic containment fact for this configuration.
- **Proposition (Q is angularly extreme, governed by sgn(AB−AC))**: proved
  in full from Lemmas S1–S3 above, no numerics — the first fully synthetic
  (non-numerical) piece of the case-split argument. Reusable by any approach
  needing to know the cyclic order of A,K,L,Q.
- **Lemma S4 (closed forms for KQ, LQ)**: proved in full via Law of Cosines
  from already-established closed forms (Lemma 2, Lemma 4, Proposition
  above); independently numerically verified to machine precision. Completes
  the set of fully closed-form side/diagonal lengths of quadrilateral AKLQ.
