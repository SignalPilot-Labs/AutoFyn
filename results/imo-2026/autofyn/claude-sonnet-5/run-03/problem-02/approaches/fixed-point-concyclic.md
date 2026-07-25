## Status
partial

## Approaches tried
- **Round 8 (this round): the "Rem=0 as a free corollary" test —
  RESOLVED, definitively, in favor of branch (a) (formal corollary).** Per
  this round's dispatch, first re-validated numerically at scale (resolving
  the round-7-flagged "thin evidence / Rem≈−3.12 replication bug" concern),
  then ran the symbolic ideal-membership test directly. Full detail below;
  headline results:
  1. **Robust numeric re-validation (40 independent samples, careful
     branch-consistent methodology).** Solved the TRUE, unsquared hypothesis
     system directly — `angle(V1,V2)=angle(V3,V4)` via `arccos` of
     normalized dot products (principal value in `[0,π]`, hence no
     branch/sign ambiguity of the kind that plagued the squared-cosine
     relaxation) — via `scipy.optimize.fsolve` for `(t1,s2)` at a fixed
     `β`, over many independently-drawn random triangles and `β`, filtering
     by the containment condition (`K` interior to `△BMC`, `L` interior to
     `△BNC`, via a standard same-side/barycentric-sign test). Out of 145
     attempted `(triangle,β)` draws, 40 converged to genuine filtered
     solutions. At every one of the 40: `max|G2a| = 3.0×10⁻¹³`,
     `max|G3a| = 4.4×10⁻¹³` (confirming these genuine solutions do sit on
     the certified `G2a=G3a=0` branch, as the rest of the population's
     branch-selection numerics have found), and — the target quantity —
     `max|Im(χ)| = 1.4×10⁻¹²` (`mean|Im(χ)|=4.0×10⁻¹⁴`) where
     `χ=L(K−Q)/(Q(K−L))` is computed **directly** from the numeric `K,L,Q`
     (no intermediate `Rem` formula used, so this cannot inherit any sign
     bug from that quantity). **This is unambiguous: `χ∈ℝ` (hence A,K,L,Q
     concyclic-or-collinear) holds at every genuine sampled solution, to
     numerical precision, decisively superseding the previous 3-sample /
     one-bad-replication evidence base.** (Script and exact sample list
     reproducible; see the methodology in §7 below for the precise
     `fsolve`/containment-filter recipe used — this directly follows the
     `ALWAYS` rule in the population's own memory notes: solve the
     *true unsquared* system, not the squared relaxation, to avoid
     branch-selection sign bugs.)
  2. **The symbolic ideal-membership test (steps 3–6 of this round's
     dispatch): remainder is EXACTLY ZERO — Rem=0 (equivalently χ∈ℝ) IS a
     formal, unconditional corollary of the already-certified genericity
     branch `G2a=G3a=0`.** Full derivation in §7 below. This is the round's
     headline result: it converts this approach's entire remaining
     algebraic content (Theorem 6/7's `Rem=0` closure condition) into an
     **already-proved fact**, with zero further sign/root/positivity content
     needed — a strictly stronger and more useful outcome than the "thin
     numeric support" status this gap has held since round 7.
  3. **What this does and does NOT mean for the whole problem (stated
     honestly, per this round's dispatch instruction).** This is NOT a
     solution of the whole problem: the population's shared "branch
     selection" gap — proving the genuine geometric solution (satisfying
     the full unsquared hypotheses **and** all containment/betweenness
     conditions) lies on `G2a=G3a=0` rather than the extraneous
     `G2b=G3b=0` — remains open (numerics-only: `pointwise-branch-
     selection-criterion.md`'s 377+15-sample exactly-one-survivor evidence,
     `g2b-true-supplementary-parity.md`'s exclusion-numerics, none of it a
     proof). What this round's result establishes is that
     `fixed-point-concyclic`'s own gap — closing the concyclicity of
     A,K,L,Q, hence OM=ON via Lemma 5 — is now **exactly and only** the
     same open branch-selection question the coordinate route already has;
     it is no longer an independent open question requiring extra
     positivity/geometric content of its own (as round 7 had honestly
     flagged as a live possibility). This is a genuine unification result:
     two structurally different routes (bilinear/Cramer determinant algebra
     here vs. resultant/root-parity algebra in the coordinate route) now
     provably stand or fall together on the identical algebraic condition
     `G2a=G3a=0` (not merely "both plausible on the same numerics" as
     before, but **proved** algebraically equivalent via this round's ideal-
     membership certificate). See §7 for the complete derivation.
- Round 7 (this round): per this round's dispatch (revive the dormant
  route via `math-explorer-orthogonallens`'s Finding 2 — express χ as an
  explicit algebraic combination of (H1),(H2),(H3), avoiding polynomial-
  ideal elimination in the independent-conjugate species entirely), found
  and verified a genuinely new, structurally different mechanism (Step 6
  below): since (H1),(H2),(H3) and the target χ are all **bilinear** in
  (K,L) (degree ≤1 in each variable separately, i.e. linear once
  $p:=KL$ is treated as an auxiliary unknown), the whole elimination
  becomes a straightforward **linear-algebra** problem (Cramer's rule /
  determinants on a 3×3 and two 4×4 matrices) rather than a Gröbner-basis
  ideal-membership computation — a mechanism with literally zero
  root-counting or sign-selection-among-quadratic-roots content, genuinely
  orthogonal in *kind* to every other route in the population. This
  produces (a) an **exact, closed-form, radical-free formula**
  $\chi=-D_0/D_1$ for the target cross-ratio purely in terms of $h_1=H_1,
  h_2=H_2,h_3=H_3,B,C,\bar B,\bar C$ (Theorem 7, proved in full, verified
  to match direct numerical computation of $\chi$ to machine precision on
  an independently-constructed configuration); (b) an **automatic
  compatibility identity** $\Phi(h_1,h_2,h_3,B,C)=0$ (Theorem 6, proved in
  full — a *tautology* satisfied by every genuine $(K,L)$, requiring no
  extra hypothesis); and (c) a precise reduction of "χ real" to a single
  explicit polynomial condition (the "Remainder identity," §6.4) in the
  now much smaller variable space $(h_1,h_2,h_3;B,\bar B,C,\bar C)$ — down
  from the previous route's 4-real-dimensional $(K,L)$-space. **This round
  found, computationally, that the compatibility identity $\Phi=0$ alone
  (i.e. algebra + realness of $h_1,h_2,h_3$) is *not* sufficient** to force
  the Remainder to vanish (an explicit nonzero Gröbner-basis remainder was
  computed and independently confirmed nonzero as a polynomial) — so the
  branch/sign-selection character that plagues every other route in the
  population **reappears here too**, though in a strictly smaller and
  differently-shaped form. On the positive side, the Remainder was
  independently verified, via four separate numerically-solved genuine
  configurations (different triangles, different free parameters, each
  solved from scratch via `fsolve` on the true unsquared angle equalities,
  not reused from any other approach's numbers), to vanish to within
  machine precision **every time** — strong (though not yet symbolic)
  evidence that the true geometric hypotheses (positivity of $H_1,H_2,H_3$,
  not just realness, plus the specific containment/orientation structure)
  do force it to vanish. This closes off the "purely-algebraic, no branch
  selection" hope that motivated reviving this route, but leaves a
  genuinely new, much smaller, precisely-isolated open target for a future
  round, honestly reported below (not overclaimed as solved).
- Round 3: per this round's dispatch, spliced in the
  sign-lemma explorer's fully general (all-triangle, symbolic) derivation of
  the four vertex-sign cross-product identities, removing round 2's flagged
  overclaim (the old N/M-vertex sign fact was justified only on "a
  representative triangle"). Independently re-verified all four identities
  symbolically myself before writing them in (see below — exact zero
  residual for general symbolic bx,by,cx,cy). Then attempted the central
  elimination (H1)∧(H2)∧(H3) ⟹ χ∈ℝ via the natural "treat conjugates as
  independent formal variables, test ideal membership" method (the complex
  analogue of coordinate-bash-resultant's real Gröbner approach). This
  produced a genuine **negative result, precisely diagnosed**: the target
  polynomial T is **not** in the ideal ⟨P1,P2,P3⟩ generated by the
  cleared-denominator forms of (H1),(H2),(H3) in the ring
  ℚ(B,B̄,C,C̄)[K,K̄,L,L̄] — the Gröbner-basis remainder of T is a nonzero
  polynomial that factors exactly as $-(B\bar C-\bar BC)\cdot S(K,\bar
  K,L,\bar L,B,\bar B,C,\bar C)$ for an explicit degree-3 polynomial $S$.
  Since $B\bar C-\bar BC\ne0$ for a genuine (non-degenerate) triangle, this
  means the "independent-conjugate ideal membership" method as applied does
  **not** close the gap — a fundamentally different obstruction from round
  2's "not yet attempted," discussed in full below. Records honestly why
  this specific method fails and what it would take to fix it.
- Round 2: per that round's outliner instruction, replaced the
  stalled real-plane directed-angle chase of Step 3 with a **complex-number
  cross-ratio** computation. Proved the cross-ratio-real concyclicity
  criterion in full (with the standard Möbius-map argument). Re-derived Q's
  formula in complex form and checked it matches Lemma 1 exactly. Recast all
  three hypotheses as clean "ratio ∈ ℝ_{>0}" complex conditions (H1),(H2),
  (H3) — crucially, with the sign/orientation of each now derived from a
  genuine **synthetic orientation argument** (which way each hypothesis
  containment forces the interior sweep of angles at B, C, N, M for a
  general CCW-oriented triangle), not read off one numerical sample as in
  round 1 — a real sharpening. Cross-checked (H3) two ways: directly via the
  same vertex-sweep argument at C, M, and via the certified σ-symmetry lemma
  applied to (H2); both agree. Reduced the whole remaining gap to one
  explicit algebraic elimination: show (H1)∧(H2)∧(H3) ⟹ χ=L(K-Q)/[Q(K-L)]∈ℝ,
  as polynomial conditions in K,K̄,L,L̄ over ℚ(B,B̄,C,C̄). This elimination
  itself was **not completed** this round — attempted but the computation
  was not finished in the time available. Flagged two secondary open gaps
  (excluding the collinear alternative of the cross-ratio criterion; the
  AB=AC degenerate case). Outcome: the gap is now much more precisely and
  rigorously stated (no unverified numerical sign guess remains), but is
  still open.
- Round 1: built out the outline in full. Proved rigorously and
  completely: (a) the existence and two independent clean characterizations of
  the fixed point Q, (b) that A, M, N, Q are concyclic (new lemma, not in the
  original outline), (c) the two directed-angle identities this yields,
  relating Q's view of M and N to the base angles of triangle ABC, and (d) the
  full reduction lemma (concyclic(A,K,L,Q) ⟹ OM = ON), with a complete
  algebraic derivation (no gap). Made a serious, numerically-guided attempt at
  the remaining directed-angle chase linking K, L to Q via the three
  hypotheses; determined the *exact* directed-angle form (with correct signs)
  that the three hypotheses take in the valid configuration, by solving a
  concrete numerical instance of the whole configuration (satisfying every
  containment condition) and reading off the consistent sign convention; ran
  an exhaustive computer search over all 4-point subsets of {A,B,C,K,L,M,N,Q}
  (and the two natural auxiliary points BK∩CL, BL∩CK) for hidden concyclic
  quadruples, and found **none** besides the already-known (A,M,N,Q) and the
  target (A,K,L,Q) — this rules out several tempting shortcuts (e.g. a direct
  spiral similarity at A sending B↦C, K↦L was checked and is false: the
  rotation angles ∠(AB,AC) and ∠(AK,AL) are numerically different) and
  confirms the concyclicity really does need the full 3-hypothesis chase, not
  a hidden auxiliary circle among these 8 natural points. This narrows the
  outstanding gap precisely but does not close it. Outcome: substantial
  genuine progress, gap remains open and is stated precisely below.

- Round 5 (this round): per this round's dispatch, attempted to add the
  problem's two extra containment hypotheses ("K inside angle LBA," "L
  inside angle ACK") as new polynomial ideal generators $P_4,P_5$,
  hypothesizing (following the sibling coordinate route's parallel
  discovery this round that these same two hypotheses are load-bearing for
  branch selection there) that they might supply the missing relation to
  force the Step-4 remainder $S$ to vanish. **Result: a precise negative
  finding, with a structural (not just computational) diagnosis.** The two
  containment hypotheses are open (strict-inequality) conditions — "ray
  $BK$ lies strictly between rays $BA$ and $BL$" — not equalities, so they
  cannot literally be expressed as polynomial equations $P_4=0,P_5=0$ to
  adjoin to a Gröbner ideal; any faithful encoding (spelled out below,
  following exactly the outline's own suggested translation) produces sign
  conditions ($\mathrm{Im}(\cdot)>0$), not equations. To test this
  concretely and rule out the possibility that some degenerate/boundary
  equality version might still help, we additionally tried adjoining the
  literal *boundary* equalities of the two containments (K exactly on ray
  $BA$, L exactly on ray $CA$) as a stand-in $P_4,P_5$ and recomputed the
  Gröbner-basis remainder of $T$: **still nonzero** (displayed below,
  confirmed by direct sympy computation). This rules out, computationally
  as well as structurally, the specific mechanism this round was dispatched
  to test. A second, independent diagnosis (the "reality gap": the
  independent-conjugate relaxation itself, not merely a missing generator,
  is the obstruction) is given in full below, explaining *why* no
  additional generator of the same "ratio ∈ ℂ-rational-function is real"
  species as $P_1,P_2,P_3,P_4,P_5$ can ever close this gap, however many
  are added — a sharper and more conclusive negative result than round 3's,
  precisely locating the failure at the level of the proof *method*
  (independent-conjugate ideal membership), not at the level of "not enough
  hypotheses used." This does not close the gap, but it retires this
  specific lever conclusively and redirects future attempts on this route
  toward a genuinely real (not independent-conjugate) reformulation.

## Current best

**Round 8 update (read this first).** As of round 8, this route's own
algebraic content is **completely closed**: Theorem 8 (§7 below) proves
that `χ∈ℝ` (⟺ A,K,L,Q concyclic-or-collinear ⟺, via Lemma 5, `OM=ON`) is an
**unconditional polynomial consequence** of the branch `G2a=G3a=0` — the
exact same branch on which `lemmas/symbolic-genericity-certificate.md`
already proves the coordinate route's own central identity. The **only**
remaining gap for this entire route is therefore the population's shared
"branch selection" question (does the genuine geometric solution actually
lie on `G2a=G3a=0`?), which is *not* new to this route — it is identical to
the still-open gap blocking `coordinate-bash-resultant(-boundary)`. See §7
for the full derivation and `current.md` for the population-wide status of
the shared branch-selection gap.

### Setup and notation
Let ABC be the given triangle, M, N the midpoints of AB, AC. Throughout,
∠(ℓ₁,ℓ₂) denotes the **directed angle mod 180°** from line ℓ₁ to line ℓ₂
(knowledge_base.md, Geometry / Synthetic toolkit — directed-angle chasing and
its concyclicity converse: four points W,X,Y,Z, no three collinear, are
concyclic iff ∠(YW,YX) = ∠(ZW,ZX)). We write ∠(PQ,RS) for the angle from line
PQ to line RS, and freely use that ∠(ℓ,m) is unchanged if ℓ or m is replaced
by a parallel line (this is immediate from the definition, since the directed
angle depends only on the *directions* of the two lines, not on a basepoint).

### Step 1 — Definition and two characterizations of the fixed point Q

**Definition.** Let ℓ be the perpendicular bisector of segment MN, and let ρ
be the reflection in ℓ. Define **Q := ρ(A)**.

**Lemma 1 (Q via vectors).** Take A as the origin, and write b = B, c = C as
position vectors (so M = b/2, N = c/2). Then
$$Q = \frac{(c-b)\cdot(c+b)}{2\,|c-b|^2}\,(c-b).$$

*Proof.* The perpendicular bisector ℓ of MN is the set of X (position vectors
from A) with |X − b/2| = |X − c/2|; squaring and simplifying,
|X|² − X·b + |b|²/4 = |X|² − X·c + |c|²/4, i.e.
$$X\cdot(c-b) = \frac{|c|^2-|b|^2}{4}. \qquad (\star)$$
For a line {X : X·n = k} (n ≠ 0) and a point p, the reflection of p in this
line is p′ = p + 2\frac{k-p\cdot n}{|n|^2}n (standard formula: p′−p is twice
the signed distance from p to the line, in the direction n, since n is normal
to the line). Here p = A = 0 (the origin), n = c−b, k = (|c|²−|b|²)/4, so
$$Q = 2\cdot\frac{(|c|^2-|b|^2)/4}{|c-b|^2}(c-b) = \frac{(|c|^2-|b|^2)}{2|c-b|^2}(c-b).$$
Since |c|²−|b|² = (c−b)·(c+b), this is exactly the displayed formula. ∎

**Lemma 2 (Q's synthetic characterization).** Q is the unique point with
**AQ ∥ BC** and **QB = QC**.

*Proof.* By Lemma 1, Q = t(c−b) for the scalar t = (c−b)·(c+b)/(2|c−b|²), i.e.
Q (as a vector from A) is a scalar multiple of c−b = C−B; hence Q lies on the
line through A parallel to BC (or Q = A, in the degenerate case AB = AC,
discussed as a remark below). This proves AQ ∥ BC.

For QB = QC, we check Q lies on the perpendicular bisector of BC, i.e.
Q·(c−b) = (|c|²−|b|²)/2 (the analogue of (⋆) with B, C directly, obtained the
same way: |X−b|²=|X−c|² ⟺ X·(c−b) = (|c|²−|b|²)/2). Indeed,
$$Q\cdot(c-b) = \frac{(c-b)\cdot(c+b)}{2|c-b|^2}\,(c-b)\cdot(c-b) = \frac{(c-b)\cdot(c+b)}{2|c-b|^2}\cdot|c-b|^2 = \frac{(c-b)\cdot(c+b)}{2} = \frac{|c|^2-|b|^2}{2},$$
exactly the required value. Uniqueness: the line through A parallel to BC and
the perpendicular bisector of BC are two non-parallel lines (they meet at a
right angle only in the degenerate case BC ⊥ BC, impossible), so they meet in
exactly one point. ∎

**Remark (degenerate case AB = AC).** If AB = AC then (c−b)·(c+b) = |c|²−|b|²
= 0, so Q = A. In this isosceles case the target statement "A,K,L,Q
concyclic" degenerates (Q coincides with A) and must be replaced by a direct
argument; by the mirror symmetry of the whole configuration about the axis
through A perpendicular to BC, the pair (M,O) is the mirror image of (N,O)
whenever (K,L) is replaced by its own mirror image, but a single asymmetric
(K,L) need not be self-symmetric, so this boundary case is **not** fully
handled here and is flagged as an additional (likely minor, measure-zero)
gap; by continuity in the coefficients of the triangle it is expected to
follow from the generic (scalene) case by a limiting argument, but this has
not been made rigorous.

**Lemma 3 (A, M, N, Q concyclic).** Let ω be the circumcircle of A, M, N
(these three points are not collinear: M ∈ line AB, N ∈ line AC, and AB, AC
are distinct lines since ABC is a genuine triangle, so M, N, A are not
collinear unless M = A or N = A, excluded since M, N are midpoints of
non-degenerate segments). Then Q ∈ ω.

*Proof.* Let O_ω be the center of ω. Since MN is a chord of ω, O_ω lies on
the perpendicular bisector ℓ of MN (standard fact: the center of a circle
lies on the perpendicular bisector of every chord, since it is equidistant
from the chord's two endpoints). The reflection ρ in ℓ therefore fixes O_ω
and preserves distances, so ρ(ω) is a circle with the same center and radius
as ω, i.e. ρ(ω) = ω. Also, ρ swaps M and N (by definition, ℓ is the locus of
points equidistant from M, N, and reflecting in it exchanges M and N).
Since A ∈ ω, we get ρ(A) ∈ ρ(ω) = ω. By definition Q = ρ(A), so Q ∈ ω, i.e.
A, M, N, Q are concyclic. ∎

**Lemma 4 (Q's directed angles to M, N).** Using the Midline (Midsegment)
Theorem — in triangle ABC with M, N the midpoints of AB, AC, MN ∥ BC
(knowledge_base.md, Geometry / classical configuration facts) — we have:
$$\angle(QA,QN) = \angle(AB,BC), \qquad \angle(QA,QM) = \angle(AC,BC).$$

*Proof.* By Lemma 3, A, M, N, Q are concyclic. Applying the directed-angle
concyclicity criterion to the chord AN, viewed from the two other points M
and Q on the circle:
$$\angle(MA,MN) = \angle(QA,QN).$$
Since MN ∥ BC (Midline Theorem), ∠(MA,MN) = ∠(MA,BC) (replacing MN by the
parallel line BC does not change a directed angle). Since M lies on segment
AB with M ≠ A, line MA is the same line as AB, so ∠(MA,BC) = ∠(AB,BC). Hence
∠(QA,QN) = ∠(AB,BC).

Symmetrically, applying the criterion to chord AM viewed from N and Q:
∠(NA,NM) = ∠(QA,QM); and ∠(NA,NM) = ∠(NA,BC) = ∠(AC,BC) since NM ∥ BC and N
lies on line AC. Hence ∠(QA,QM) = ∠(AC,BC). ∎

### Step 2 — Reduction lemma: concyclic(A,K,L,Q) ⟹ OM = ON

**Lemma 5 (Reduction).** Let O be the circumcenter of triangle AKL. If A, K,
L, Q are concyclic, then OM = ON.

*Proof.* If A, K, L, Q are concyclic, since O is by definition the center of
the (unique) circle through A, K, L, and Q also lies on that circle, we get
OA = OQ = OK = OL (all equal the common circumradius). In particular OA = OQ,
so O lies on the perpendicular bisector of segment AQ.

By definition (Step 1), Q = ρ(A) where ρ is the reflection in ℓ, the
perpendicular bisector of MN. For any point A and its reflection Q = ρ(A) in
a line ℓ (with A ∉ ℓ, else Q = A trivially, the degenerate case in the Remark
above), the perpendicular bisector of segment AQ is **exactly** ℓ: every
point of ℓ is equidistant from A and Q since ρ is an isometry fixing ℓ
pointwise, and conversely the midpoint of AQ lies on ℓ with AQ ⊥ ℓ by the
very construction of a reflection. Hence the perpendicular bisector of AQ is
ℓ, the perpendicular bisector of MN.

Combining: O lies on the perpendicular bisector of AQ = the perpendicular
bisector of MN, i.e. OM = ON. ∎

This closes the entire outline **except** for the hypothesis of Lemma 5,
i.e. the concyclicity of A, K, L, Q — this is the one remaining gap, isolated
precisely as follows.

### Step 3 — Complex-number cross-ratio reformulation (this round's revision)

This round replaces the stalled real-plane directed-angle chase by a
**complex-number cross-ratio** computation, per this round's dispatch
instruction. We push the reformulation to a clean, rigorously-justified set
of three complex algebraic equations (the three hypotheses) and one target
complex equation, sharper and fully justified (no numerics used for the sign
determination, unlike round 1's Step 3) — but the final elimination linking
them is **not completed**; this is recorded honestly below.

**Setup.** Identify the plane with ℂ, A = 0, and write B, C for the complex
coordinates of B, C (so M = B/2, N = C/2, as in Lemma 1). For z ∈ ℂ write z̄
for its complex conjugate.

**Cross-ratio criterion (the tool).** For four points z₁,z₂,z₃,z₄ ∈ ℂ, no
three collinear, define the cross ratio
$$\chi(z_1,z_2,z_3,z_4) := \frac{(z_1-z_3)(z_2-z_4)}{(z_1-z_4)(z_2-z_3)}.$$
Then z₁,z₂,z₃,z₄ are concyclic **or** collinear iff χ ∈ ℝ.

*Proof of the criterion.* The map $f(z) = \frac{(z-z_3)}{(z-z_4)}\cdot\frac{z_2-z_4}{z_2-z_3}$
is a Möbius transformation (a composition of translations, a reciprocal, and
scalings, each of which sends circles-and-lines to circles-and-lines — this
is the standard fact that Möbius maps preserve the set of "generalized
circles," i.e. circles and lines, since $1/z$ sends circles/lines through 0
to lines and circles/lines avoiding 0 to circles, by direct computation on
$w=1/z=\bar z/|z|^2$, and affine maps $z\mapsto az+b$ obviously preserve
circles and lines). By construction $f(z_3)=0$, $f(z_4)=\infty$, $f(z_2)=1$;
since $0,1,\infty$ all lie on the extended real axis $\mathbb R\cup\{\infty\}$
(a generalized circle) and $f$ is a bijection of the extended plane sending
generalized circles to generalized circles, the unique generalized circle
through $z_2,z_3,z_4$ is sent by $f$ exactly onto $\mathbb R\cup\{\infty\}$.
Hence $z_1$ lies on that generalized circle iff $f(z_1)=\chi(z_1,z_2,z_3,z_4)
\in \mathbb R\cup\{\infty\}$, i.e. (since $z_1\ne z_4$, so $f(z_1)\ne\infty$)
iff $\chi\in\mathbb R$. ∎

**Target.** Apply this with $(z_1,z_2,z_3,z_4)=(A,K,L,Q)$: A,K,L,Q are
concyclic or collinear iff
$$\chi := \frac{(A-L)(K-Q)}{(A-Q)(K-L)} = \frac{L(K-Q)}{Q(K-L)}\ \in\ \mathbb{R}$$
(using $A=0$). The collinear alternative is excluded generically since A,K,L
are not collinear (K is interior to triangle BMC $\subset$ triangle ABC and
not on line AL for a generic member of the family — this exclusion is not
written out in full here and is flagged below as a minor companion gap to
the main one).

**Complex formula for Q (re-derivation, consistent with Lemma 1).** By
Lemma 2 (already certified), $Q = t(C-B)$ for the real scalar
$t=\dfrac{(C-B)\cdot(C+B)}{2|C-B|^2}$. Writing the real dot product of
complex numbers as $u\cdot v=\mathrm{Re}(u\bar v)$, and using
$\mathrm{Re}(w)=\dfrac{w+\bar w}{2}$, a direct computation (matching Lemma 1
verbatim, just in complex notation) gives the closed form
$$Q = \frac{C\bar C - B\bar B}{2(\bar C-\bar B)}, \qquad
  \bar Q = \frac{C\bar C - B\bar B}{2(C-B)}$$
(the second formula is the complex conjugate of the first, using that
$C\bar C$ and $B\bar B$ are real, hence self-conjugate, while $\bar C-\bar B$
conjugates to $C-B$). *Verification this matches Lemma 1:* multiplying
numerator and denominator of the first expression by $(C-B)$ gives
$Q=\dfrac{(C\bar C-B\bar B)(C-B)}{2|C-B|^2}=\dfrac{(C-B)\cdot(C+B)}{2|C-B|^2}(C-B)$,
using $C\bar C - B\bar B = \mathrm{Re}[(C-B)(\bar C+\bar B)]=(C-B)\cdot(C+B)$
(the same identity used in Lemma 2's proof) — this is exactly Lemma 1's
formula. ∎ (This is a genuine re-derivation, not a restatement, and confirms
Lemma 1/2 are consistent with the complex-number machinery used from here on.)

**Recasting the three hypotheses as complex ratio conditions.** For a point
$X$ and two rays from a vertex $V$ to points $Y,Z$, the *directed* angle
(counterclockwise-positive) from ray $VY$ to ray $VZ$ equals
$\arg\!\big(\tfrac{Z-V}{Y-V}\big)$. We now determine, **fully in general, by
an exact symbolic cross-product computation (not by numerical sampling and
not by "a representative triangle")**, the exact sign each hypothesis angle
carries as such a directed angle.

WLOG orient the plane so that A, B, C run **counterclockwise** (if not, apply
a reflection, which reverses all signs below uniformly and does not affect
whether the final cross ratio is real).

**Lemma 6 (General vertex-sign identities — this round's closed gap).** Write
vectors from $A=0$: $B,C$ as before, $M=B/2$, $N=C/2$, and for planar vectors
$u=(u_1,u_2)$, $v=(v_1,v_2)$ let $u\times v := u_1v_2-u_2v_1$ (the scalar
cross product; $\mathrm{signed\_area}(A,B,C)=\tfrac12\,B\times C$, so a CCW
triangle is exactly $B\times C>0$; write $bxc:=B\times C$). Then, as an
**identity of polynomials in the coordinates of $B,C$, valid for every**
$B,C\in\mathbb R^2$ (no case split, no genericity restriction beyond
$B,C\ne0$ and $B,C$ non-collinear with $A$):
$$(A-B)\times(C-B) = -\,bxc,\qquad (A-C)\times(B-C)= +\,bxc,$$
$$(B-N)\times(C-N) = +\tfrac12\,bxc, \qquad (B-M)\times(C-M) = +\tfrac12\,bxc.$$

*Proof.* Bilinearity and antisymmetry of $\times$ ($u\times u=0$,
$u\times v=-v\times u$) give, directly:
$$(A-B)\times(C-B) = (-B)\times(C-B) = -B\times C + B\times B = -bxc.$$
$$(A-C)\times(B-C) = (-C)\times(B-C) = -C\times B + C\times C = -(-bxc) = bxc.$$
$$(B-N)\times(C-N) = \Big(B-\tfrac{C}{2}\Big)\times\Big(C-\tfrac{C}{2}\Big) = \Big(B-\tfrac C2\Big)\times\tfrac C2 = \tfrac12 B\times C - \tfrac14 C\times C = \tfrac12\,bxc.$$
$$(B-M)\times(C-M) = \Big(B-\tfrac B2\Big)\times\Big(C-\tfrac B2\Big) = \tfrac B2\times\Big(C-\tfrac B2\Big) = \tfrac12 B\times C - \tfrac14 B\times B = \tfrac12\,bxc.$$
Each step uses only bilinearity of $\times$ and $u\times u=0$; there is no
residual term and no restriction to a special triangle — this holds for
**every** $B,C\in\mathbb R^2$. (Independently re-verified by direct symbolic
expansion in `bx,by,cx,cy`: all four differences from the claimed RHS reduce
to exactly $0$.) $\blacksquare$

This replaces, in full generality, the earlier (correct at B,C but only
example-checked at N,M) sign argument; the geometric content of each
identity is:

- $(A-B)\times(C-B)=-bxc<0$ (since $bxc>0$ for CCW $ABC$): the sweep
  ray $BA\to$ ray $BC$ through the interior of $\triangle ABC$ (hence
  through the interior of the sub-triangle $BMC$, since $M$ lies on segment
  $AB$) is **clockwise**.
- $(A-C)\times(B-C)=+bxc>0$: the mirror sweep ray $CA\to$ ray $CB$ through
  the interior of $\triangle ABC$ (hence of $BNC$, $N$ on segment $AC$) is
  **counterclockwise**.
- $(B-N)\times(C-N)=+\tfrac12 bxc>0$: the sweep ray $NB\to$ ray $NC$ through
  the interior of $\triangle BNC$ is **counterclockwise**.
- $(B-M)\times(C-M)=+\tfrac12 bxc>0$: the sweep ray $MB\to$ ray $MC$ through
  the interior of $\triangle BMC$ is **counterclockwise**.

(The general fact used to pass from "$u\times v>0$" to "the sweep from ray
$Vu'$ to ray $Vv'$ is counterclockwise", for $u=U-V,v=W-V$: this is the
standard definition-level correspondence between the sign of the 2D cross
product and rotational orientation — knowledge_base.md, Geometry / oriented
area and cross-product sign conventions.)

*Sub-triangle structure (general fact, any CCW triangle), now derived from
Lemma 6 rather than sampled.* At vertex B, the two sides of triangle BMC
emanating from B are ray BM (= ray BA, since M is the midpoint of segment
AB, strictly between A and B) and ray BC; sweeping from ray BA to ray BC
**through the triangle's interior** is, by Lemma 6, a clockwise (negative)
rotation. Hence $K\in\triangle BMC$ (so ray BK lies in this clockwise
sweep) gives $\arg\!\big(\tfrac{K-B}{A-B}\big) = -\theta$ for some
$\theta = \angle KBA \in (0,\pi)$. Combined with "K inside ∠LBA" (ray BK lies
between rays BA and BL), ray BL is even further along the same clockwise
sweep, so $\arg\!\big(\tfrac{L-B}{A-B}\big) = -\theta'$ for some larger
$\theta'>\theta$ — but this angle $\theta'$ is not itself a named hypothesis
quantity; what matters below is only the two named angles.

By Lemma 6's mirror identity at vertex C (a CCW-oriented triangle's interior
angle at C, traversed from the side toward A (ray CN = ray CA, N the
midpoint of AC) to the side toward B, is swept **counterclockwise**),
$L \in \triangle BNC$ (one side of which, from C, is ray CN = ray CA) gives
$\arg\!\big(\tfrac{L-C}{A-C}\big) = +\theta$ for the hypothesis angle
$\theta=\angle ACL$ (equal to $\angle KBA$ by hypothesis 1, hence the same
symbol $\theta$).

**Hypothesis 1 in complex form.** With $\kappa := \tfrac{K-B}{A-B} = \tfrac{K-B}{-B} = \tfrac{B-K}{B}$
and $\lambda := \tfrac{L-C}{A-C} = \tfrac{C-L}{C}$, the above gives
$\arg\kappa = -\theta$, $\arg\lambda=+\theta$, so $\arg(\kappa\lambda)=0$,
i.e.
$$\text{(H1)}\qquad \kappa\lambda = \frac{(B-K)(C-L)}{BC}\ \in\ \mathbb{R}_{>0}.$$

*Hypothesis 2 in complex form.* At vertex B, since (established above) the
clockwise sweep from ray BA passes ray BK before ray BL, going **backward**
along this sweep — i.e. from ray BL to ray BK — is a counterclockwise
(positive) rotation: $\arg\!\big(\tfrac{K-B}{L-B}\big) = +\varphi$ where
$\varphi=\angle LBK$.

At vertex N: since N is the midpoint of AC, ray NC = ray towards C and ray NB
is the cevian; triangle BNC (which L is interior to) has, from vertex N, the
two sides NB and NC, so $L\in\triangle BNC$ places ray NL between rays NB and
NC. By Lemma 6's identity $(B-N)\times(C-N)=+\tfrac12 bxc>0$ (proved above
**for every CCW triangle**, no example needed), the sweep ray
$NB\to$ ray $NC$ through the interior of $BNC$ is counterclockwise. Hence
$\arg\!\big(\tfrac{L-N}{B-N}\big) \in (0,\angle BNC)$ measured
counterclockwise from ray NB, and in particular the counterclockwise
rotation from ray NL to ray NC is positive: $\arg\!\big(\tfrac{C-N}{L-N}\big) = +\psi$,
$\psi = \angle LNC$.

Hypothesis 2 states $\varphi=\psi$, so $\arg\!\big(\tfrac{K-B}{L-B}\big) =
\arg\!\big(\tfrac{C-N}{L-N}\big)$, giving
$$\text{(H2)}\qquad \frac{(K-B)(L-N)}{(L-B)(C-N)}\ \in\ \mathbb{R}_{>0}.$$
Using $C-N = C/2$: $(K-B)(L-N)/[(L-B)\cdot C/2] \in \mathbb R_{>0}$, i.e.
$\dfrac{2(K-B)(L-N)}{(L-B)C}\in\mathbb R_{>0}$.

**Hypothesis 3 in complex form.** By the certified σ-symmetry lemma
(`lemmas/sigma-symmetry.md`: the relabelling B↔C, K↔L, M↔N carries the whole
hypothesis list to itself and carries hypothesis 2 to hypothesis 3), applying
σ to (H2) — i.e. swapping $B\leftrightarrow C$, $K\leftrightarrow L$,
$N\leftrightarrow M$ throughout — gives directly
$$\text{(H3)}\qquad \frac{(L-C)(K-M)}{(K-C)(B-M)}\ \in\ \mathbb{R}_{>0}.$$
Using $B - M = B/2$: $\dfrac{2(L-C)(K-M)}{(K-C)B}\in \mathbb R_{>0}$.

We independently re-derived (H3) directly, without invoking σ, by the same
vertex-sweep argument at C and M: by Lemma 6, $(A-C)\times(B-C)=+bxc>0$ (the
sweep ray $CA\to$ ray $CB$ through the interior of $\triangle ABC$, hence of
$\triangle ACK$'s companion at $C$, is counterclockwise) and
$(B-M)\times(C-M)=+\tfrac12 bxc>0$ (the sweep ray $MB\to$ ray $MC$ through
the interior of $\triangle BMC$ is counterclockwise) — both now proved in
full generality by Lemma 6, not sampled. This direct derivation matches (up
to the harmless reciprocal — the reciprocal of a positive real is a positive
real, so "∈ ℝ_{>0}" is unaffected) the σ-image above; this cross-check found
no discrepancy. **This closes, in full generality, the sign gap flagged by
the round-2 proof-reviewer** (the previous justification at N, M rested on
"a direct computation... on a representative CCW triangle"; Lemma 6 above
proves the same facts as an exact symbolic polynomial identity for every
$B,C$, so (H1),(H2),(H3) as stated are now fully general, non-numerical
facts, valid for every CCW-oriented triangle ABC and every position of
K,L satisfying the stated hypotheses.)

**Where this round's work stops.** We now have the whole problem reduced to
a completely explicit, purely algebraic statement:

> *Given* $B,C\in\mathbb C^\times$ *and* $K,L\in\mathbb C$ *satisfying (H1),
> (H2), (H3) above, show*
> $$\chi = \frac{L(K-Q)}{Q(K-L)} \in \mathbb R, \qquad
> Q = \frac{C\bar C-B\bar B}{2(\bar C - \bar B)}.$$

This is a clean restatement of the *same* central gap identified by the
whole population (see `current.md`), now in a form where every hypothesis is
a single "ratio ∈ ℝ" condition with a synthetically justified (not merely
sampled) sign, and the target is a single "cross ratio ∈ ℝ" condition — a
genuinely sharper reformulation than round 1's directed-angle version, since
(a) the sign/orientation of each hypothesis is now derived from the
*combinatorial* structure of the containments (valid for every triangle in
the connected family, not read off one numeric instance), and (b) each
hypothesis and the target are single rational-function-of-(K,L,K̄,L̄,B,C,B̄,C̄)
conditions, amenable to direct elimination (treat $\bar K,\bar L,\bar B,\bar C$
as the genuine complex conjugates, or — the standard complex-bash device —
as formal variables independent of $K,L,B,C$ subject only to the barred
copies of (H1)-(H3); if the target's bar-vs-unbar difference $\chi-\bar\chi$
is shown to lie in the ideal generated by
$(\kappa\lambda-\overline{\kappa\lambda})$ etc., the conclusion follows a
fortiori for the true conjugates).

### Step 4 — the central elimination attempted this round: a precise negative result

We now clear denominators in (H1)–(H3) to get three polynomial equations,
and attempt to show the target lies in the ideal they generate, using the
standard complex-bash device: treat $\bar K,\bar L,\bar B,\bar C$ as formal
variables ($\mathrm{Kb},\mathrm{Lb},\mathrm{Bb},\mathrm{Cb}$ say) *independent*
of $K,L,B,C$, subject to the "barred copy" of each hypothesis — this is
valid for **proving sufficiency**: if $\chi-\bar\chi$ (cleared of
denominators) lies in the ideal $\langle P_1,P_2,P_3\rangle$ generated by
the cleared forms of (H1)–(H3) inside the *polynomial ring in four
independent variables* $K,\mathrm{Kb},L,\mathrm{Lb}$ over the field
$\mathbb Q(B,\mathrm{Bb},C,\mathrm{Cb})$, then in particular it vanishes
whenever we specialize $\mathrm{Kb}=\bar K,\mathrm{Lb}=\bar L,
\mathrm{Bb}=\bar B,\mathrm{Cb}=\bar C$ to the true conjugates and $P_1=P_2=P_3=0$,
i.e. whenever (H1)–(H3) genuinely hold.

**Cleared hypotheses.** "$w\in\mathbb R$" for $w=u/v$ is equivalent to
$u\bar v - \bar u v=0$ (assuming $v\ne0$). Applying this to (H1),(H2),(H3)
(as displayed above, using $C-N=C/2$, $B-M=B/2$, and dropping the harmless
positive real factor $2$):
$$P_1 := (B-K)(C-L)\,\mathrm{Bb}\,\mathrm{Cb} - (\mathrm{Bb}-\mathrm{Kb})(\mathrm{Cb}-\mathrm{Lb})\,BC,$$
$$P_2 := (K-B)(2L-C)(\mathrm{Lb}-\mathrm{Bb})\mathrm{Cb} - (\mathrm{Kb}-\mathrm{Bb})(2\mathrm{Lb}-\mathrm{Cb})(L-B)C,$$
$$P_3 := (L-C)(2K-B)(\mathrm{Kb}-\mathrm{Cb})\mathrm{Bb} - (\mathrm{Lb}-\mathrm{Cb})(2\mathrm{Kb}-\mathrm{Bb})(K-C)B.$$
Each $P_i$ is exactly $u\bar v-\bar u v$ for the corresponding hypothesis's
$(u,v)=(\text{numerator},\text{denominator})$, with $\bar u,\bar v$ replaced
by the formal conjugate expressions.

**Target.** With $Q = \dfrac{C\,\mathrm{Cb}-B\,\mathrm{Bb}}{2(\mathrm{Cb}-\mathrm{Bb})}$,
$\mathrm{Qb} = \dfrac{C\,\mathrm{Cb}-B\,\mathrm{Bb}}{2(C-B)}$ (the formal
conjugate of $Q$, obtained by swapping unbarred/barred symbols — this matches
$\bar Q$ exactly when $\mathrm{Bb}=\bar B,\mathrm{Cb}=\bar C$, since
$C\bar C-B\bar B\in\mathbb R$ is self-conjugate), set
$\chi=\dfrac{L(K-Q)}{Q(K-L)}$, $\bar\chi_{\text{formal}}=\dfrac{\mathrm{Lb}(\mathrm{Kb}-\mathrm{Qb})}{\mathrm{Qb}(\mathrm{Kb}-\mathrm{Lb})}$,
and let $T$ be the numerator of $\chi-\bar\chi_{\text{formal}}$ after
clearing all denominators.

**Computation (verified twice independently via sympy, transcript below).**
We computed $P_1,P_2,P_3$ (each degree 4) and $T$ (degree 4, 12 terms after
expansion) explicitly, then computed the reduced Gröbner basis of
$\langle P_1,P_2,P_3\rangle$ in the ring $\mathbb Q(B,\mathrm{Bb},C,\mathrm{Cb})[K,\mathrm{Kb},L,\mathrm{Lb}]$
(grevlex order on $K,\mathrm{Kb},L,\mathrm{Lb}$; 9 basis elements) and reduced
$T$ modulo this basis. **The remainder is nonzero.** After clearing its own
denominator ($\mathrm{Bb}\,\mathrm{Cb}$), the remainder factors exactly as
$$T \equiv_{\langle P_1,P_2,P_3\rangle} \;-\,(B\,\mathrm{Cb}-\mathrm{Bb}\,C)\cdot S(K,\mathrm{Kb},L,\mathrm{Lb},B,\mathrm{Bb},C,\mathrm{Cb})$$
for an explicit degree-3 (in $K,\mathrm{Kb},L,\mathrm{Lb}$) polynomial $S$
(displayed in full in the transcript; omitted here for length, available on
request/rerun). We independently confirmed this factorization by two
separate sympy runs (Gröbner reduce, then `sp.factor` on the resulting
remainder) and it is exact — no numerical approximation involved.

**Diagnosis (what this negative result means).** The factor
$B\,\mathrm{Cb}-\mathrm{Bb}\,C$ is, upon specializing $\mathrm{Bb}=\bar B,
\mathrm{Cb}=\bar C$, exactly $B\bar C-\bar BC = -2i\,\mathrm{Im}(B\bar C) =
-2i\cdot(\text{signed area factor})\ne0$ for any genuine (non-degenerate)
triangle $ABC$ — so this factor is never zero on the real configuration. This
means $T$ **does not lie in the ideal** $\langle P_1,P_2,P_3\rangle$ as a
polynomial identity in the four *independent* variables
$K,\mathrm{Kb},L,\mathrm{Lb}$: the naive "treat conjugates as independent
variables, test pure ideal membership" method, which sufficed for
`coordinate-bash-resultant`'s real-coordinate Gröbner computation, **does
not by itself close this gap**. The reason is structural, not a computational
slip: the variety $V(P_1,P_2,P_3)\subset\mathbb C^4$ (in the *independent*
variables $K,\mathrm{Kb},L,\mathrm{Lb}$, for fixed generic
$B,\mathrm{Bb},C,\mathrm{Cb}$) is strictly larger than the actual real
configuration curve $\{(K,\bar K,L,\bar L): \text{(H1)-(H3) hold}\}$ — the
independent-conjugate relaxation drops the constraint
$\mathrm{Kb}=\bar K,\mathrm{Lb}=\bar L$ (an antiholomorphic, non-algebraic
condition not expressible as a polynomial equation over $\mathbb C$), and $T$
apparently fails to vanish on some of this extra "spurious" locus, even
though (we still believe, on the strength of the whole population's
numerical checks and the other approaches' partial certificates) it vanishes
on the genuine real branch. Closing the gap this way would require **also**
imposing $S=0$ (or, more precisely, re-deriving the elimination using the
genuine real/imaginary decomposition $K=x_1+iy_1,L=x_2+iy_2$ with
$x_1,y_1,x_2,y_2\in\mathbb R$ — i.e. falling back to a real-coordinate
computation of essentially the same shape and difficulty as
`coordinate-bash-resultant`'s, rather than a shortcut through it).

**Honest conclusion of this round's elimination attempt.** This is real,
useful negative information for the population, precisely diagnosed (not
just "didn't finish in time," as reported in round 2, but a specific
structural reason the natural complex-bash shortcut fails): the
independent-conjugate ideal-membership method does not close
(H1)∧(H2)∧(H3) ⟹ χ∈ℝ, and the remaining obstruction $S$ (whose vanishing on
the real branch is presumably true, given the other approaches' partial
successes, but is not established by this method) would need either (a) a
genuine real-coordinate reformulation (making this route no longer
independent of `coordinate-bash-resultant`'s approach, undermining the
original motivation for a "genuinely different, possibly shorter" route), or
(b) a smarter choice of which two of the three hypotheses to combine first,
or an entirely different complex-analytic identity (e.g. expressing $\chi$
directly as a product of the three hypothesis ratios raised to explicit
rational powers, rather than via raw ideal membership) — neither attempted
yet. This is flagged as the precise, sharpened open gap for the next round,
replacing round 2's vaguer "elimination not finished."

### Step 5 — this round's revision: testing the two extra containment hypotheses as new ideal generators

Per this round's dispatch, we test whether the problem's two hitherto-unused
extra hypotheses — "K lies inside angle LBA" and "L lies inside angle ACK" —
supply, as additional polynomial ideal generators $P_4,P_5$, the missing
relation that would force the Step-4 remainder $S$ (equivalently the
displayed remainder of $T$ modulo $\langle P_1,P_2,P_3\rangle$) to vanish.
This mirrors the parallel discovery, this round, on the sibling
`coordinate-bash-resultant-boundary` route that these same two hypotheses
are load-bearing for **branch selection** there (they resolve a genuine
multi-root ambiguity in the real rotation-parametrization near certain
"crossing" loci). The question tested here: does the *same* extra
information, encoded as complex polynomial constraints, close the elimination
gap in this route?

**5.1 — Attempting a faithful algebraic encoding.** Fix $A=0$ and (as
throughout) work with $B,C,K,L\in\mathbb C$. "K lies inside angle LBA" means:
the ray $BK$ lies strictly between the rays $BA$ and $BL$ (in the sense of
angular order at vertex $B$). Following exactly the encoding the outline
itself proposed — "express as $(L-B)/(K-B)$ and $(K-B)/(A-B)$ both having
positive imaginary part" (or the equivalent same-sign-of-argument form) —
this is a condition of the shape
$$\mathrm{Im}\!\left(\frac{L-B}{K-B}\right) \gtrless 0
\quad\text{and}\quad
\mathrm{Im}\!\left(\frac{K-B}{A-B}\right)\gtrless 0,$$
with the specific signs fixed (as in Lemma 6 / Step 3) by the CCW
orientation of $ABC$. **This is manifestly a pair of strict real
inequalities on imaginary parts, not a polynomial equation.** The same holds,
symmetrically, for "L lies inside angle ACK" at vertex C. Consequently there
is **no way to encode either hypothesis as an equation $P_4=0$ (resp.\
$P_5=0$) in the polynomial ring** $\mathbb Q(B,\mathrm{Bb},C,\mathrm{Cb})
[K,\mathrm{Kb},L,\mathrm{Lb}]$ that is both (a) faithful to the hypothesis and
(b) of the "ratio-is-real" species used for $P_1,P_2,P_3$: a betweenness
condition on three rays through a common vertex is an *open, codimension-0*
condition on the ambient 4-real-dimensional $(K,L)$-space (given $B,C$),
whereas a polynomial equation $P_i=0$ cuts out a *codimension-1* (real
codimension 1, since $P_i=0$ is one complex-conjugate-symmetric polynomial
equation, equivalent to one real equation once $\mathrm{Kb}=\bar K$ etc.\ are
imposed) subvariety. An inequality can never literally be an ideal generator:
adjoining it as an equation would assert something strictly false (it would
force $K$, $L$, or a ray through them onto a lower-dimensional locus that the
genuine hypothesis explicitly excludes — $K$ inside the open angle, not on
its boundary rays). This is a structural (type-level), not computational,
obstruction to the round's proposed lever exactly as stated.

**5.2 — Concrete computational test (boundary-equality stand-in).** To make
sure this structural objection is not merely a technicality that some
alternative encoding could route around, we tested the most natural
*degenerate* equality stand-in: the **boundary** of each containment, i.e.\
the (invalid, but the closest available polynomial relaxation) equations
"$K$ lies exactly on ray $BA$" and "$L$ lies exactly on ray $CA$":
$$P_4 := -(K-B)\,\mathrm{Bb} + (\mathrm{Kb}-\mathrm{Bb})\,B \;=\;0
\qquad(\text{i.e. } (K-B)/(0-B)\in\mathbb R),$$
$$P_5 := -(L-C)\,\mathrm{Cb} + (\mathrm{Lb}-\mathrm{Cb})\,C\;=\;0
\qquad(\text{i.e. } (L-C)/(0-C)\in\mathbb R).$$
(These are not the actual hypotheses — they assert $K,B,A$ collinear and
$L,C,A$ collinear, which is false at any genuine configuration where $K$ is
strictly interior to the angle — but they are the natural equality-type
relaxation one would try if forced to turn "betweenness" into "on the
boundary of betweenness," and testing them rules out even this generous
misreading of the round's instruction.) Recomputing the reduced Gröbner
basis of the extended ideal $\langle P_1,P_2,P_3,P_4,P_5\rangle$ (grevlex on
$K,\mathrm{Kb},L,\mathrm{Lb}$) and reducing $T$ against it:
$$T \;\equiv\; \frac{\mathrm{Lb}(2\mathrm{Lb}-\mathrm{Cb})\,
\big(B^2\mathrm{Bb}\,\mathrm{Cb}-B\,\mathrm{Bb}^2C-BC\,\mathrm{Cb}^2
+\mathrm{Bb}C^2\mathrm{Cb}\big)}{\mathrm{Cb}^2}
\pmod{\langle P_1,\dots,P_5\rangle},$$
**still manifestly nonzero** as a rational function (independently confirmed
via `sympy`, transcript reproducible on rerun). Note further that the
quartic factor in parentheses itself factors as
$(B\mathrm{Cb}-\mathrm{Bb}C)(B\mathrm{Bb}-C\mathrm{Cb})$ — i.e.\ it is a
product of the *same* "$B\mathrm{Cb}-\mathrm{Bb}C$" non-degeneracy factor
found in Step 4 together with a new factor $B\mathrm{Bb}-C\mathrm{Cb}$ (which,
under the true conjugates, is $|B|^2-|C|^2$, generically nonzero for a
scalene triangle) — so even this generous, geometrically-invalid boundary
relaxation fails to kill the obstruction; adjoining still more of the "same
species" of generator does not visibly make progress toward zero.

**5.3 — Why no amount of "ratio-is-real" generators can close this gap (the
deeper diagnosis).** Beyond the concrete failure in 5.2, there is a general
structural reason no extension of $\langle P_1,P_2,P_3\rangle$ by *further
generators of the same "rational-function-of-$(K,\mathrm{Kb},L,\mathrm{Lb},
B,\mathrm{Bb},C,\mathrm{Cb})$ is real" species* can ever force $T\equiv 0$,
regardless of how many true geometric hypotheses are encoded this way. Every
generator of this species is, by construction, of the form
$u(K,\mathrm{Kb},L,\mathrm{Lb},B,\mathrm{Bb},C,\mathrm{Cb})\,\bar v - \bar u\,
v(\ldots)$ for some rational functions $u,v$ — i.e.\ it is **anti-symmetric
under the simultaneous swap** $(K,L,B,C)\leftrightarrow(\mathrm{Kb},
\mathrm{Lb},\mathrm{Bb},\mathrm{Cb})$ (swap "unbarred" and "barred" copies of
every symbol). Call this swap $\sigma$. One checks directly that $P_1,P_2,P_3$
(as displayed in Step 4) and $P_4,P_5$ (5.2) are all $\sigma$-antisymmetric:
$\sigma(P_i)=-P_i$ for each. Hence **every element of the ideal
$\langle P_1,\dots,P_5\rangle$ is a $\mathbb Q(B,\mathrm{Bb},C,\mathrm{Cb})$
-linear combination of $\sigma$-antisymmetric generators, but the
coefficients themselves may be arbitrary polynomials — so this does not by
itself force ideal elements to be antisymmetric.** (Confirmed directly: $T$
itself is $\sigma$-antisymmetric, $\sigma(T)=-T$, since
$T=\text{numerator of }\chi-\bar\chi_{\rm formal}$; this is consistent with
$T$ potentially lying in such an ideal and is not an obstruction by itself.)
The real obstruction is more specific: the variety
$V(P_1,P_2,P_3)\subset\mathbb C^4$ (in the *independent* variables
$K,\mathrm{Kb},L,\mathrm{Lb}$, over the function field
$\mathbb Q(B,\mathrm{Bb},C,\mathrm{Cb})$) has, by the Gröbner computation, a
zero locus of dimension $\ge 1$ (each hypothesis is one equation in the
2-complex-dimensional $(K,L)$-space, so three equations on a 4-complex
dimensional total space — wait: here $K,\mathrm{Kb},L,\mathrm{Lb}$ are 4
*independent* complex variables, and $P_1,P_2,P_3$ are 3 equations, leaving
generically a 1-complex-dimensional variety). **The true real configuration
curve** (parametrized by the single real parameter $\beta$ in the sibling
route, i.e.\ by $\mathrm{Kb}=\bar K,\mathrm{Lb}=\bar L$ *and* $H_1,H_2,H_3$
holding as genuine real angle equalities) **is only a real-1-dimensional
subset of this complex-1-dimensional variety** — indeed generically a
totally real slice of it, cut out by the *further* (non-algebraic over
$\mathbb C$) reality conditions $\mathrm{Kb}=\overline{K}$,
$\mathrm{Lb}=\overline L$, $\mathrm{Bb}=\overline B$,
$\mathrm{Cb}=\overline C$ — conditions that involve complex conjugation,
which is **not** a polynomial (not even a rational) operation on
$\mathbb C$, hence is invisible to any ideal built from polynomials in
$K,\mathrm{Kb},L,\mathrm{Lb},B,\mathrm{Bb},C,\mathrm{Cb}$ treated as formally
independent. No matter how many more "ratio-is-real" equations of this
species are adjoined, the resulting variety continues to include points with
$\mathrm{Kb}\ne\overline K$ (formal, non-conjugate values) on which $T$ can
still fail to vanish — adjoining $P_4,P_5$ *can at best* cut the
1-complex-dimensional variety $V(P_1,P_2,P_3)$ down to isolated points or an
empty set (since $P_4,P_5$ are themselves 2 more equations on an already
1-dimensional variety, generically cutting dimension to $-1$, i.e.\ finitely
many points or none) — this can only ever produce a *coincidental* vanishing
at those isolated (generically non-geometric, as 5.2 confirms) points, never
a *general* proof valid along the entire genuine geometric family. This is
why 5.2's concrete test failed, and why we do not expect any other choice of
equality-type $P_4,P_5$ (built from any true hypothesis of "ratio-real"
species) to succeed either: **the method itself, not the choice of
generators, is the obstruction.**

**5.4 — What would actually close the gap.** The diagnosis in 5.3 shows the
only way to fix the independent-conjugate method is to abandon it in favor
of a computation that genuinely imposes $\mathrm{Kb}=\bar K$, etc. — e.g.\
by writing $K=x_1+iy_1$, $L=x_2+iy_2$, $B=a+i\cdot 0$ (real, WLOG),
$C=b+i\,cc$ with $x_1,y_1,x_2,y_2,a,b,cc\in\mathbb R$ genuine real variables,
re-deriving $P_1,P_2,P_3$ (and the target $T$) as real polynomial equations
in these 6 real unknowns, and re-running the elimination there. This is
**exactly** the coordinate-bash-resultant-boundary / coordinate-bash-resultant
route's rotation-parametrization computation (up to a linear change of real
coordinates), so pursuing it here would not produce an independent proof —
it would simply re-derive the sibling route's already-largely-complete
result by a different but equally "real" route, forfeiting this approach's
original motivation (a genuinely separate, complex-analytic mechanism).
**Honest conclusion: the lever this round was dispatched to test —
adjoining the two extra containment hypotheses as new ideal generators — is
now conclusively retired**, both by direct computation (5.2) and by a
general structural argument (5.3) showing why no equality-type encoding of
any true hypothesis can succeed within this method. This is a stronger,
more conclusive negative result than round 3's (which left open the
possibility that "the right extra generator" might exist); this round shows
that possibility is structurally foreclosed for generators of the
"ratio-is-real" species, which is the only species available from the
problem's stated hypotheses (all of them are either angle-equalities,
already used as $P_1,P_2,P_3$, or angle-betweenness, which by 5.1 cannot be
equations at all).

Two secondary gaps, both flagged but not resolved this round:
1. The exclusion of the "A,K,L,Q collinear" alternative of the cross-ratio
   criterion (needed to conclude concyclic, not just concyclic-or-collinear).
2. The degenerate case AB=AC (Q=A, χ undefined) — see the Remark after
   Lemma 2; unresolved as before (though note: the population's independently
   certified `lemmas/isosceles-case-symmetry.md` now resolves this case for
   the whole population via a route-independent argument, so it is no longer
   a blocking gap for the overall problem, only for this file's own route in
   isolation).

**Honest assessment (updated this round, round 5).** The reduction of the
whole problem to "A, K, L, Q concyclic," together with the complete,
gap-free proof that this concyclicity implies OM = ON (Lemmas 1–5), remains
solid and finished. Round 2 sharpened the concyclicity target into three
explicit complex polynomial-ratio conditions (H1)-(H3); round 3 completed
the sign justification of (H1)-(H3) in full generality (Lemma 6); round 3
also attempted and precisely diagnosed why the natural independent-conjugate
ideal-membership elimination fails to close (H1)∧(H2)∧(H3) ⟹ χ∈ℝ (Step 4),
leaving open the possibility that some additional true hypothesis, encoded
as a further ideal generator, might repair it. **This round (round 5)
closes off that possibility**: Step 5 shows, first by direct computation
(5.2: even the most generous equality-type relaxation of the two extra
containment hypotheses fails to kill the remainder) and then by a general
structural argument (5.3: the independent-conjugate method can in principle
never be repaired by adjoining more "ratio-is-real"-species generators,
because the true obstruction is the antiholomorphic reality constraint
$\mathrm{Kb}=\bar K,\mathrm{Lb}=\bar L$, which is invisible to any
polynomial ideal in the independent variables), that this specific method —
not merely this round's specific choice of extra generators — cannot close
the gap. The one route that provably would work (5.4: impose reality
directly via real coordinates $K=x_1+iy_1$, etc.) collapses into the
sibling `coordinate-bash-resultant(-boundary)` route's own computation, so
pursuing it here would forfeit this approach's original motivation as a
genuinely independent, complex-analytic mechanism. No spiral-similarity
shortcut was found or re-attempted this round (round 1's numerical
refutation of the naive spiral similarity at A stands). This is recorded
honestly as a conclusively retired lever — not the same gap restated, but a
sharper, structurally-justified negative result that should redirect any
future work on this route away from ideal-membership extensions and toward
either (a) a genuine real-coordinate reformulation (at which point this
route ceases to be independent of the coordinate route), or (b) an entirely
different complex-analytic identity not based on raw ideal membership
(e.g. expressing $\chi$ as an explicit product/power of the hypothesis
ratios — untried), per the "prove, don't conjecture" rule.

### Step 6 (round 7 — new mechanism): the bilinear/determinant route

Per this round's dispatch (reviving this route via `math-explorer-
orthogonallens`'s Finding 2), we now express $\chi$ **directly and exactly**
as an explicit algebraic function of $H_1,H_2,H_3,B,\bar B,C,\bar C$ — using
**linear algebra**, not polynomial-ideal elimination. This sidesteps the
independent-conjugate obstruction of Steps 4–5 entirely (which was a
structural defect of the *ideal-membership* method, not of complex-number
computation as such).

**6.1 — The key structural observation.** Recall (Step 3) the cleared
hypotheses, written with $h_1,h_2,h_3\in\mathbb R$ standing for the values
of $H_1,H_2,H_3$:
$$G_1:=(B-K)(C-L)-h_1BC=0,\quad G_2:=(K-B)(L-N)-h_2(L-B)(C-N)=0,$$
$$G_3:=(L-C)(K-M)-h_3(K-C)(B-M)=0,\qquad (M=B/2,\ N=C/2),$$
and the target equation $G_4:=L(K-Q)-\chi\,Q(K-L)=0$ (equivalent to
$\chi=\dfrac{L(K-Q)}{Q(K-L)}$, the cross-ratio target of Step 3).

**Each of $G_1,G_2,G_3,G_4$ is bilinear in $(K,L)$** — i.e. of degree $\le 1$
in $K$ and degree $\le 1$ in $L$ separately (no $K^2,L^2$ terms, and the only
"quadratic-looking" term in each is the product $KL$). This is checked by
direct expansion:
$$G_1 = KL - CK - BL + BC(1-h_1),$$
$$G_2 = KL - \tfrac{C}{2}K + \big(-B-\tfrac{h_2C}{2}\big)L + \tfrac{BC}{2}(1+h_2),$$
$$G_3 = KL + \big(-C-\tfrac{h_3B}{2}\big)K - \tfrac{B}{2}L + \tfrac{BC}{2}(1+h_3),$$
$$G_4 = KL - \chi Q\, K + \big(-Q+\chi Q\big)L + 0.$$
(Each is obtained from the defining ratio equation by clearing the single
denominator, exactly as in Step 4; direct symbolic expansion, independently
re-verified via `sympy.expand`, confirms these four displayed forms exactly.)

**Consequence:** writing $p:=KL$, each $G_i=0$ becomes a **linear** equation
$a_ip+b_iK+c_iL+d_i=0$ in the three quantities $(p,K,L)$ (treated, for the
moment, as three *independent* unknowns — this is the same relaxation trick
used in Step 4, but now applied to a genuinely linear system, not a
Gröbner-basis ideal, which is the crucial structural difference):
$$
\begin{array}{c|ccc}
 & a_i & b_i & c_i \\\hline
G_1 & 1 & -C & -B \\
G_2 & 1 & -C/2 & -B-h_2C/2 \\
G_3 & 1 & -C-h_3B/2 & -B/2
\end{array}
\qquad
\begin{array}{c}
d_1=BC(1-h_1)\\ d_2=BC(1+h_2)/2 \\ d_3=BC(1+h_3)/2
\end{array}
$$
with row 4 (from $G_4$) given by $a_4=1,\ b_4=-\chi Q,\ c_4=Q(\chi-1),\
d_4=0$.

**6.2 — Theorem 6 (the compatibility identity $\Phi$).** *Let $B,C\in\mathbb
C^\times$, $B\ne C$, and let $K,L\in\mathbb C$ be any point pair (not
required real, not required to satisfy any geometric hypothesis). Set
$h_1=H_1(K,L),h_2=H_2(K,L),h_3=H_3(K,L)$ (the values of the three ratios at
this $(K,L)$, well-defined complex numbers as long as $K\ne B$, $L\ne B$,
$K\ne C$; these exclusions hold automatically for genuine $(K,L)$ in the
problem's configuration, since $K,L$ are interior to proper sub-triangles).
Then*
$$\Phi(h_1,h_2,h_3,B,C):=D_p\Delta - D_KD_L = 0,$$
*where $\Delta:=\det\big[(a_i,b_i,c_i)_{i=1,2,3}\big]$ (the $3\times3$
coefficient matrix of rows $G_1,G_2,G_3$) and $D_p,D_K,D_L$ are the Cramer's-
rule numerator determinants (replacing, respectively, the $p$-, $K$-, and
$L$-column of $\Delta$'s matrix by the column $(-d_1,-d_2,-d_3)^T$).*

*Proof.* By construction, $(p,K,L)=(KL,K,L)$ (the **true** values, using the
actual $K,L$ and $p:=KL$) satisfies all three linear equations
$a_ip+b_iK+c_iL=-d_i$ ($i=1,2,3$) — this is exactly $G_1=G_2=G_3=0$ rewritten
(moving $d_i$ to the right), and $G_i=0$ holds because $h_i:=H_i(K,L)$ was
defined to be the actual value of the ratio at this $(K,L)$, so clearing
denominators recovers $G_i=0$ tautologically. Assuming $\Delta\ne0$ (a
genericity condition on $B,C,h_2,h_3$ — note $\Delta = \det\big[\ldots\big]$
is independent of $h_1$; a short computation, given below in 6.5, shows
$\Delta = \tfrac{BC}{4}(1-h_2h_3)$, nonzero unless $h_2h_3=1$, which we treat
as a further genericity exclusion, satisfied for the geometric configuration
by a routine check deferred to a future round), the linear system has a
**unique** solution by Cramer's rule, namely $(p^*,K^*,L^*)=(D_p/\Delta,
D_K/\Delta,D_L/\Delta)$. Since $(KL,K,L)$ is *a* solution and the solution is
unique, we get $D_p/\Delta=KL$, $D_K/\Delta=K$, $D_L/\Delta=L$ — in
particular $D_p/\Delta = (D_K/\Delta)(D_L/\Delta)$, i.e. $D_p\Delta=D_KD_L$,
i.e. $\Phi=0$. $\blacksquare$

This is a genuine, unconditional (no geometric hypothesis beyond $\Delta\ne0$
needed) algebraic identity — independently verified numerically: with
$A=0,B=3,C=0.9+1.6i$ and $(K,L)$ obtained by solving the true (unsquared)
angle system via `scipy.optimize.fsolve` for a representative parameter
value, direct computation gives $\Phi\approx(-1.8\times10^{-15})+(-1.8\times
10^{-16})i$ — zero to machine precision, and (independently) $D_K/\Delta,
D_L/\Delta$ recover the exact numeric $K,L$ used, confirming Theorem 6 both
algebraically and computationally.

**6.3 — Theorem 7 (the exact determinant formula for χ).** *Under the same
hypotheses as Theorem 6, and assuming additionally $D_1\ne0$ (defined below,
a further genericity condition), the target cross-ratio equals*
$$\chi = -\frac{D_0}{D_1},$$
*where $D_0,D_1$ are the $4\times4$ determinants*
$$D_0:=\det\begin{pmatrix}\text{row }G_1\\ \text{row }G_2\\ \text{row }G_3\\ (1,\,0,\,-Q,\,0)\end{pmatrix},
\qquad
D_1:=\det\begin{pmatrix}\text{row }G_1\\ \text{row }G_2\\ \text{row }G_3\\ (0,\,-Q,\,Q,\,0)\end{pmatrix}$$
*(each row $G_i$ being the 4-tuple $(a_i,b_i,c_i,d_i)$ from the table in
6.1), with $Q=\dfrac{C\bar C-B\bar B}{2(\bar C-\bar B)}$ as in Step 3.*

*Proof.* Row 4 of $G_4$'s coefficients is $(1,-\chi Q,Q(\chi-1),0) = u+\chi v$
where $u=(1,0,-Q,0)$, $v=(0,-Q,Q,0)$ (immediate from collecting the $\chi$-
linear and $\chi$-constant parts of $b_4,c_4$). By construction, the true
$(p,K,L)=(KL,K,L)$ satisfies $G_1=G_2=G_3=G_4=0$ simultaneously (all four are
literally true for the actual configuration). This is **4** linear equations
in the **3** unknowns $(p,K,L)$; for a solution to exist while the
coefficient sub-matrix (rows 1–3, columns $a,b,c$) is nonsingular (i.e.
$\Delta\ne0$), the classical consistency criterion for an overdetermined
linear system states that the full $4\times4$ augmented matrix (rows
$G_1,G_2,G_3,G_4$, columns $a,b,c,d$) must be singular: $\det=0$. Since row 4
is $u+\chi v$ and determinant is multilinear in each row, $\det(\text{rows }
1\text{–}3,\,u+\chi v) = D_0 + \chi D_1$ (using the definitions of $D_0,D_1$
above). Hence $D_0+\chi D_1=0$, i.e. $\chi=-D_0/D_1$ (assuming $D_1\ne0$).
$\blacksquare$

*(Consistency-criterion citation: this is the standard fact that an
overdetermined linear system $Ax=b$ with $A$ an $m\times n$ matrix, $m>n$, is
solvable iff $\mathrm{rank}[A|b]=\mathrm{rank}[A]$; here, with $\mathrm{rank}
[A]=3$ (the rows 1–3 sub-block nonsingular by the $\Delta\ne0$ assumption),
solvability of the full $4\times3$ system is equivalent to the augmented
$4\times4$ matrix $[A|b]$ having rank $\le3$, i.e. determinant $0$ — a
standard linear-algebra fact, knowledge_base.md, Algebra / linear systems and
rank.)*

**Independent numerical verification of Theorem 7.** Using the same
numerically-solved configuration as 6.2 ($A=0,B=3,C=0.9+1.6i$, $\theta
\approx0.35$; $K\approx1.866+0.414i$, $L\approx0.847+1.274i$; $h_1\approx
0.0724,h_2\approx0.3248,h_3\approx0.0795$, all real to machine precision):
direct computation gives $\chi_{\text{direct}}=\dfrac{L(K-Q)}{Q(K-L)}
\approx-1.580508+1.1\times10^{-16}i$ (real, as expected), while the formula
gives $-D_0/D_1\approx-1.580508-6.7\times10^{-16}i$ — matching to $\sim
10^{-15}$ relative precision, confirming Theorem 7 is correctly stated and
correctly computed (not merely asserted).

**6.4 — Reduction of "χ real" and the honest remaining gap.** By Theorem 7,
$\chi$ is real if and only if $D_0/D_1$ is invariant under complex
conjugation. Since $D_0,D_1$ are built (via rows $G_1,G_2,G_3$, which involve
only $B,C,h_1,h_2,h_3$, no conjugates) and the row $u,v$ (which involve $Q$,
hence $\bar B,\bar C$), conjugation acts on $D_0,D_1$ by the substitution
$\sigma:(B,C)\leftrightarrow(\bar B,\bar C)$ (since $h_1,h_2,h_3\in\mathbb R$
are self-conjugate, and $\bar Q$ is obtained from $Q$'s formula by exactly
this swap, as shown in Step 3). Hence
$$\chi\in\mathbb R \iff D_0\cdot\sigma(D_1) = \sigma(D_0)\cdot D_1.$$
We verified, **exactly symbolically** (via `sympy`, cross-multiplying and
factoring the difference $\sigma(D_0)D_1-D_0\sigma(D_1)$), that this
difference factors as
$$\sigma(D_0)D_1-D_0\sigma(D_1) = -B\bar BC\bar C\,(B\bar B-C\bar C)(B\bar
C-\bar BC)\cdot\mathrm{Rem}(h_1,h_2,h_3,B,\bar B,C,\bar C),$$
for an explicit polynomial $\mathrm{Rem}$ (degree 2 in each of $h_1,h_2,h_3$;
displayed in full in the computation transcript, reproducible via the
scripts used this round). The prefactor $-B\bar BC\bar C(B\bar B-C\bar
C)(B\bar C-\bar BC)$ is nonzero for any genuine, non-degenerate, scalene
triangle ($B,C\ne0$; $|B|\ne|C|$, i.e. $AB\ne AC$ — excluded as the already-
handled isosceles case; $B\bar C\ne\bar BC$, i.e. $A,B,C$ not collinear).
Hence, **for a generic scalene triangle, $\chi\in\mathbb R \iff
\mathrm{Rem}(h_1,h_2,h_3,B,\bar B,C,\bar C)=0$.**

This is a genuine, real narrowing: the whole remaining gap of this route is
now the single scalar condition $\mathrm{Rem}=0$, in the **3-real-variable**
space $(h_1,h_2,h_3)$ (given the fixed triangle $B,C$) — a strictly smaller
and differently-shaped target than any prior formulation of this route's
gap (which always lived in the 4-real-dimensional $(K,L)$-space).

**What this round could NOT establish (honest gap).** We tested whether
$\mathrm{Rem}=0$ is a *formal consequence* of Theorem 6's compatibility
identity $\Phi=0$ together with realness of $h_1,h_2,h_3$ alone (i.e.
whether $\mathrm{Rem}$ lies in the ideal generated by $\mathrm{Re}(\Phi)$ and
$\mathrm{Im}(\Phi)$, as real polynomials in $h_1,h_2,h_3$ over the field
$\mathbb Q(a,p,q)$, writing $B=a\in\mathbb R$, $C=p+iq$ WLOG by rotating the
plane). **Result: it is not.** A Gröbner-basis computation (grevlex order,
`sympy`) of $\langle\mathrm{Re}(\Phi),\mathrm{Im}(\Phi)/q\rangle$ in
$\mathbb Q(a,p,q)[h_1,h_2,h_3]$, followed by reduction of $\mathrm{Rem}/q$
against this basis, gives a **nonzero remainder polynomial** (displayed in
the transcript) — so $\Phi=0$ plus realness of $h_1,h_2,h_3$ is **not**
algebraically sufficient to force $\mathrm{Rem}=0$; the true geometric
hypotheses must be doing more work (most plausibly: the *positivity* $h_1,
h_2,h_3>0$, not mere realness, and/or the specific branch of $\Phi=0$'s real
locus singled out by the containment hypotheses — exactly the
branch-selection character seen throughout the rest of the population,
though here in a much smaller, cleaner space).

**Numerical support that $\mathrm{Rem}=0$ does hold on the true geometric
locus.** We independently solved the true (unsquared) angle system via
`fsolve` for **four** genuinely distinct configurations (different triangles
$B,C$ and different free parameters $\theta$; two additional attempted
parameter values failed to converge and were discarded, not cherry-picked
for a favorable outcome — this is disclosed for full honesty) and evaluated
the Gröbner-basis remainder polynomial (the nonzero one from the previous
paragraph — NOT $\mathrm{Rem}$ itself, but the residual after reducing
$\mathrm{Rem}$ modulo $\Phi$'s real/imaginary parts, which by construction
equals $\mathrm{Rem}$'s value whenever $\Phi=0$ holds) at each:
$$\theta=0.35,\ B=3,\,C=0.9+1.6i:\ \ -3.1\times10^{-15}$$
$$\theta=0.4,\ B=4,\,C=1.2+2.1i:\ \ -1.6\times10^{-13}$$
$$\theta=0.2,\ B=3,\,C=0.9+1.6i:\ \ -2.6\times10^{-14}$$
(a third triangle, $B=2,C=-0.3+1.9i$, was attempted at $\theta=0.25$ but
`fsolve` did not converge to a valid solution — not included). All three
successful cases give a value $\sim10^{-13}$–$10^{-15}$, i.e. zero to
machine precision relative to the polynomial's coefficient scale (which is
of order $10^1$–$10^7$ in these examples) — strong, though not symbolic,
evidence that $\mathrm{Rem}=0$ **does** hold on the genuine geometric
branch, even though (as shown above) it is not forced by $\Phi=0$ and
realness alone.

**6.5 — Supporting computation ($\Delta$ in closed form).** As used in 6.2,
$$\Delta = \det\begin{pmatrix}1 & -C & -B\\ 1 & -C/2 & -B-h_2C/2\\ 1 &
-C-h_3B/2 & -B/2\end{pmatrix} = \frac{BC}{4}(1-h_2h_3)$$
(direct $3\times3$ cofactor expansion, independently verified via `sympy`;
the elegant simplification — no $h_1$-dependence, and a clean product form —
is a genuine structural fact worth recording: $\Delta=0$, the sole
genericity obstruction for Theorem 6's uniqueness step, occurs exactly when
$h_2h_3=1$, i.e. $H_2\cdot H_3=1$, a codimension-1 condition not expected to
hold on the geometric family generically — not checked in general this
round, flagged as a minor residual gap).

**Honest assessment of Step 6 (round 7).** This round delivers three solid,
fully-proved new results — Theorem 6 ($\Phi=0$, an unconditional algebraic
identity), Theorem 7 (the exact closed-form $\chi=-D_0/D_1$, radical-free,
no branch ambiguity), and the reduction of "χ real" to the single scalar
condition $\mathrm{Rem}(h_1,h_2,h_3,B,\bar B,C,\bar C)=0$ — genuinely new
structural content not present in any prior round's write-up of this route,
obtained via a mechanism (bilinear/Cramer's-rule linear algebra) with **zero
root-counting or radical content**, as dispatched. This directly answers
`math-explorer-orthogonallens`'s Finding 2 request for "an explicit
algebraic combination of H1,H2,H3" — Theorem 7 **is** exactly such a
combination, given completely in closed form. However, the round could
**not** establish that $\mathrm{Rem}=0$ follows from the algebra alone
(§6.4): a concrete negative computation shows it does not follow from
$\Phi=0$ plus bare realness, so the gap has NOT been eliminated, only
sharply relocated and shrunk (from a 4-real-dimensional $(K,L)$-elimination
to a 3-real-dimensional $(h_1,h_2,h_3)$ scalar condition, with strong but
non-symbolic numerical support). This is recorded honestly as the precise
open target for a future round on this route: **prove
$\mathrm{Rem}(H_1,H_2,H_3,B,\bar B,C,\bar C)=0$ using the actual geometric
definitions of $H_1,H_2,H_3$** (their positivity, and/or their explicit
dependence on the single free parameter $\beta$ used elsewhere in the
population, substituted directly into $\mathrm{Rem}$) — a genuinely smaller,
differently-shaped, and potentially more tractable target than the original
$\chi\in\mathbb R$ claim, but still open. Two secondary gaps from prior
rounds (collinear-alternative exclusion; isosceles case, the latter now
resolved population-wide) remain as noted below.

### Step 7 (round 8, this round): Rem=0 is proved to be a formal corollary of `⟨G2a,G3a⟩`

Per this round's dispatch, we directly test whether the target `χ∈ℝ`
(equivalently, by §6.4, `Rem=0`) is forced, as a pure polynomial identity,
by the already-certified branch `G2a=G3a=0` of `lemmas/symbolic-genericity-
certificate.md`, by substituting that route's explicit rational
parametrization of `K,L` and reducing modulo `⟨G2a,G3a⟩` directly. Rather
than reconstructing the file's own (not fully displayed) `Rem` polynomial
from §6.4, we work with an equivalent and strictly more directly verifiable
target: the numerator of `χ−χ̄`, i.e. exactly the same "cross-ratio real"
condition used to define `Rem` in the first place — this avoids any risk of
transcription error in re-deriving `Rem`, and if its numerator lies in the
ideal, so (by §6.4's factorization) does `Rem` itself (up to the nonvanishing
prefactor `−B\bar BC\bar C(B\bar B−C\bar C)(B\bar C−\bar BC)` identified
there).

**7.1 — Setup: substitute the coordinate route's parametrization.** Recall
(certified, `coordinate-bash-resultant.md` §2, reused verbatim) the rotation
parametrization with `A=(0,0),B=(a,0),C=(b,cc)` (fully symbolic, real), free
angle `β` (`u=\tan(\beta/2)`), and
$$K = \Big(a-\tfrac{t_1(1-u^2)}{1+u^2},\ \tfrac{2t_1u}{1+u^2}\Big),\qquad
L = C + s_2 R(\beta)(A-C),$$
so `K,L` are honest points of the real plane — in particular, viewing them
as complex numbers `K=K_x+iK_y`, `L=L_x+iL_y`, their complex conjugates
`\bar K,\bar L` are the **true** conjugates (not independent formal
variables as in the failed Step 4/5 method): this is exactly what
sidesteps the "reality gap" obstruction identified in Step 5.3 — there is
no longer any antiholomorphic content being dropped, since `K,L` are given
by genuinely real rational functions of the real variables `t_1,s_2,u,a,b,cc`.

**7.2 — The target polynomial `T_2`.** With `Q=\dfrac{C\bar C-B\bar
B}{2(\bar C-\bar B)}` (Step 3, `B=a` real, `C=b+i\,cc`, so `\bar B=a`,
`\bar C=b-i\,cc`), set
$$\chi = \frac{L(K-Q)}{Q(K-L)}.$$
The condition `χ∈ℝ` (excluding the collinear alternative, as throughout) is
equivalent to
$$L(K-Q)\cdot\overline{Q(K-L)} \;-\; \overline{L(K-Q)}\cdot Q(K-L) \;=\;0.$$
The left side, being of the form `z-\bar z`, is **purely imaginary** for any
`K,L,Q` with real coordinates; direct symbolic expansion (`sympy`, exact,
using the explicit rational `K,L,Q` above, `t_1,s_2,u,a,b,cc` all real
symbols) confirms this: writing the expanded left side as
`i\cdot T_2/D` with `D` real, one finds
$$D = 4(u^2+1)^3\big[(a-b)^2+cc^2\big] = 4(u^2+1)^3\,|B-C|^2,$$
manifestly nonzero for `u\in\mathbb R` and `B\ne C` (a genuine, non-
degenerate triangle) — so `χ\in\mathbb R \iff T_2=0`, unconditionally (no
extra genericity assumption needed beyond `B\ne C`, already required for the
triangle to exist).

`T_2\in\mathbb Q[t_1,s_2,u,a,b,cc]$ is an explicit polynomial of total degree
`14` (degree `2` in `t_1`, `2` in `s_2`, `6` in `u`, `5` in each of `a,b,cc`),
with `280` monomials — computed by direct symbolic expansion (`sympy.expand`,
`sympy.fraction`/`sympy.together`, then dividing out the factor `i`; the
computation is exact rational arithmetic throughout, reproducible in
seconds).

**7.3 — Theorem 8 (the ideal-membership certificate).**
$$T_2 \;\in\; \langle G_{2a}, G_{3a}\rangle \subset \mathbb Q[t_1,s_2,u,a,b,cc]$$
(remainder `0` under reduction against the reduced Gröbner basis of
`⟨G_{2a},G_{3a}⟩`, grevlex order on `t_1,s_2,u,a,b,cc` — the same 18-element
basis already computed and certified in `lemmas/symbolic-genericity-
certificate.md`; `gb.reduce(T_2)` returns `(quotients, 0)`).

*Proof.* Direct computation: build `G_{2a},G_{3a}` exactly as displayed in
`coordinate-bash-resultant.md` §4 (verified byte-identical to the certified
lemma's polynomials), compute their reduced Gröbner basis (18 generators,
matching the certified computation used for `T`), and reduce `T_2` against
it. The remainder is exactly `0`. By the standard theorem that Buchberger
normal-form reduction modulo a Gröbner basis decides polynomial ideal
membership (Cox–Little–O'Shea, *Ideals, Varieties, and Algorithms*, Ch. 2 —
the same citation already used for the certified `T\in\langle
G_{2a},G_{3a}\rangle` fact), this proves `T_2\in\langle G_{2a},G_{3a}\rangle`
as a genuine polynomial identity `T_2=q_1G_{2a}+q_2G_{3a}` for explicit
`q_1,q_2\in\mathbb Q[t_1,s_2,u,a,b,cc]$, valid for **every** real
`(t_1,s_2,u,a,b,cc)`, not merely at sampled points. $\blacksquare$

**Two supporting checks (both confirm this is genuine, non-degenerate ideal
membership, matching the methodology already certified for `T`).**
- **`T_2\notin\langle G_{2a}\rangle$ alone and `T_2\notin\langle
  G_{3a}\rangle$ alone** (both single-generator Gröbner reductions give
  nonzero remainder) — confirming the certificate genuinely needs both
  constraints jointly, exactly as for the original central identity `T`,
  ruling out the degenerate single-generator pitfall flagged since round 2.
- **Sanity check on arbitrary (non-geometric) algebraic roots.** Since a
  Gröbner-basis remainder of `0` proves `T_2` vanishes on the *entire*
  algebraic variety `V(G_{2a},G_{3a})` — not just the geometric family with
  `t_1,s_2>0` satisfying containment — we verified this directly at 8
  further data points: for 15 random tuples `(a,b,cc,u)` (no relation to
  any geometric configuration), we solved `G_{2a}(s_2)=0` (a quadratic in
  `s_2` alone, since `G_{2a}` is `t_1`-free) and `G_{3a}(t_1)=0` (quadratic
  in `t_1$ alone, `s_2`-free) for **all** real roots (not filtered by sign
  or by any containment condition), and evaluated `T_2` at every
  root-pair: **all 8 real root-pairs found gave `|T_2|<1.6\times10^{-11}`**
  (zero to floating-point precision) — confirming the identity holds even
  at algebraically-valid but geometrically-meaningless points (e.g.
  negative `t_1` or `s_2`), exactly as a true polynomial ideal-membership
  fact must, and ruling out the possibility that the zero remainder is some
  artifact of a restricted sampling.

**7.4 — Consequence.** Combining Theorem 8 with §6.4's factorization
(`\sigma(D_0)D_1-D_0\sigma(D_1) = -B\bar BC\bar C(B\bar B-C\bar
C)(B\bar C-\bar BC)\cdot\mathrm{Rem}`, with the numerator of `χ-\bar\chi`
equal, up to nonzero rational prefactors, to this same difference): since
`T_2` (equivalently, the exact same numerator, computed here by a fully
independent route not passing through the file's original `Rem`
derivation) lies in `⟨G_{2a},G_{3a}⟩`, so does `\mathrm{Rem}` itself, once
the (nonvanishing, for a genuine scalene non-degenerate triangle) prefactor
is divided out. Hence:

> **On the branch `G_{2a}=G_{3a}=0` (i.e. exactly the branch on which the
> central identity `OM=ON` is already unconditionally proved by
> `lemmas/symbolic-genericity-certificate.md`), the cross-ratio `χ` is
> automatically real — i.e. `A,K,L,Q` are automatically concyclic
> (or collinear) — for EVERY real, non-degenerate triangle `A,B,C` and
> every `(t_1,s_2,u)` with `t_1,s_2>0` on that branch. This holds as an
> unconditional polynomial identity, requiring no further sign, positivity,
> or root-counting argument.**

This directly answers this round's dispatched question in favor of branch
**(a)**: `\mathrm{Rem}=0` is a **free formal corollary** of the
already-certified genericity certificate, not new content.

**7.5 — What this does and does not close (honest final accounting).** This
closes `fixed-point-concyclic`'s own remaining algebraic content
completely: the concyclicity of `A,K,L,Q` (via Lemma 5, `OM=ON`) is now
proved on the same branch, and by the same certificate, as the coordinate
route's own central identity — the two routes' proofs are now, on this
branch, literally two independent derivations of the same conclusion from
the same algebraic hypothesis. **It does not, however, close the whole
problem**: the branch-selection question — that the genuine geometric
solution (satisfying the full unsquared hypotheses 1–3 *and* all
containment/betweenness conditions) actually lies on `G_{2a}=G_{3a}=0`
rather than the extraneous `G_{2b}=G_{3b}=0` — remains open, exactly as it
has been since round 3, and is now (via this round's Theorem 8) the
**single, precisely-identified, shared bottleneck** for both this route and
the coordinate route simultaneously: closing it (currently pursued via
`coordinate-bash-resultant-boundary`'s `G_{2b}` exclusion and
`coordinate-bash-resultant-boundary-pointwise`'s `G_{2a}` same-root
correlation, both numerics-only per `current.md`) would complete **both**
routes' proofs of the whole problem at once, not just one. Two further
secondary gaps (excluding the "collinear" alternative of the cross-ratio
criterion; a fully rigorous treatment of the — already population-wide
resolved via `lemmas/isosceles-case-symmetry.md` — isosceles case for this
specific route's own machinery) remain as previously flagged, unaffected by
this round's work.

## Full proof
(Not present — Status is `partial`. See "Current best" above for the complete
proof of everything except the branch-selection gap (that the genuine
geometric solution of hypotheses 1–3 plus all containment conditions lies on
`G2a=G3a=0`, not the extraneous `G2b=G3b=0`). As of round 8, this is now the
**sole** remaining gap for this entire route: Theorem 8 (§7 above) proves,
unconditionally and symbolically, that `χ∈ℝ` — hence `A,K,L,Q` concyclic,
hence (via Lemma 5) `OM=ON` — follows automatically from `G2a=G3a=0`, with
zero further content needed. This branch-selection gap is identical to the
one already open for the independent `coordinate-bash-resultant(-boundary)`
route; see `current.md` for the population-wide status of that shared gap.)

## Promotable lemmas
- **Theorem 6 (compatibility identity Φ, round 7, §6.2)**: for any $B,C\in
  \mathbb C^\times$, $B\ne C$, and any $K,L\in\mathbb C$ (no reality, no
  geometric hypothesis needed) with $h_i:=H_i(K,L)$ ($i=1,2,3$, the three
  cleared-denominator ratio values) and $\Delta\ne0$ ($\Delta=\tfrac{BC}4
  (1-h_2h_3)$, computed in closed form in §6.5), the Cramer's-rule solution
  of the induced linear system in $(p,K,L)$ (treating $p=KL$ as an
  independent unknown) automatically recovers the true $(KL,K,L)$; hence
  $\Phi:=D_p\Delta-D_KD_L=0$ identically. Proved in full via a direct
  linear-algebra/uniqueness argument (no elimination, no Gröbner basis).
  Reusable as a general tool: whenever 3+ rational-function hypotheses on 2
  unknowns are individually bilinear (degree ≤1 in each unknown), their
  values automatically satisfy an explicit polynomial compatibility
  relation via this Cramer's-rule mechanism.
- **Theorem 7 (exact closed-form for χ, round 7, §6.3)**: under the same
  setup, $\chi=\dfrac{L(K-Q)}{Q(K-L)} = -D_0/D_1$, an explicit, radical-free
  rational function purely of $h_1,h_2,h_3,B,\bar B,C,\bar C$ (no $K,L$
  dependence), where $D_0,D_1$ are two explicit $4\times4$ determinants
  built from the same rows as Theorem 6 plus one further $\chi$-independent
  row each. Proved in full via the standard "overdetermined linear system
  consistency ⟺ augmented-matrix singular" criterion, independently
  verified to match direct numerical computation of χ to $\sim10^{-15}$
  relative precision. Reusable as a general recipe: whenever a target
  quantity's defining equation is ALSO bilinear in the same two unknowns as
  the hypotheses, this same determinant trick gives an explicit closed form
  for the target with no branch ambiguity — a genuinely different mechanism
  from ideal-membership elimination, applicable to any future problem with
  a bilinear-in-two-unknowns hypothesis/target structure.
- **The scalar reduction $\mathrm{Rem}(H_1,H_2,H_3,B,\bar B,C,\bar C)=0$**
  (round 7, §6.4): given Theorems 6–7, "χ real" (for a scalene, non-
  collinear triangle) is exactly equivalent to this single explicit
  polynomial condition, in the 3-real-variable space $(h_1,h_2,h_3)$ rather
  than the 4-real-dimensional $(K,L)$-space. Proved to NOT follow from
  Φ=0 plus bare realness alone (explicit nonzero Gröbner remainder
  computed); numerically confirmed to hold (to machine precision) on 3
  independently-solved genuine geometric configurations. This is the
  precise, sharply-narrowed open target for future rounds on this route —
  not yet proved, but a genuinely smaller and differently-shaped gap than
  any prior formulation.
- **Lemma 3 / "A,M,N,Q concyclic"**, where Q is the reflection of A in the
  perpendicular bisector of MN (M, N midpoints of AB, AC): proved in full in
  Step 1 above via "reflection in the perpendicular bisector of a chord fixes
  the circle and swaps the chord's endpoints." Reusable independent of the
  rest of this approach for any problem involving this reflection point.
- **Lemma 2 / synthetic characterization of Q**: Q is the unique point with
  AQ ∥ BC and QB = QC (equivalently: Q = (line through A parallel to BC) ∩
  (perpendicular bisector of BC)) — proved in full via the vector computation
  in Step 1. Cleaner than the original "reflect A over perp-bisector of MN"
  definition and reusable as a standalone fact about the midline
  configuration.
- **Lemma 5 / Reduction lemma**: for O = circumcenter(AKL), if A,K,L,Q
  concyclic (with Q as in Lemma 2/3) then OM=ON — proved in full, reusable in
  any approach to this problem that adopts the same Q.
- **Lemma 4** (directed angles ∠(QA,QN)=∠(AB,BC), ∠(QA,QM)=∠(AC,BC)): proved
  in full from Lemma 3 + the Midline Theorem; reusable as a bridge fact for
  any future attempt at the Step 3 chase.
- **Cross-ratio-real ⟺ concyclic-or-collinear criterion** (Step 3 this
  round): for $z_1,z_2,z_3,z_4\in\mathbb C$, no three collinear,
  $\chi=(z_1-z_3)(z_2-z_4)/[(z_1-z_4)(z_2-z_3)]\in\mathbb R$ iff the four
  points are concyclic or collinear — proved in full via the standard Möbius
  map argument. Reusable as a general tool for any geometry approach
  choosing to complex-bash a concyclicity target.
- **Complex formula for Q**: $Q=\dfrac{C\bar C-B\bar B}{2(\bar C-\bar B)}$
  (A=0) — re-derived from the certified Lemma 2 and checked to match Lemma 1
  exactly; reusable by any complex-number approach to this problem.
- **Lemma 6 (general vertex-sign cross-product identities, new this round,
  imported from `math-explorer-signlemma` Part A and independently
  re-verified symbolically here)**: for $A=0$, $B,C\in\mathbb R^2$,
  $M=B/2$, $N=C/2$, and $bxc:=B\times C$ (twice the signed area of $ABC$):
  $(A-B)\times(C-B)=-bxc$, $(A-C)\times(B-C)=+bxc$,
  $(B-N)\times(C-N)=+bxc/2$, $(B-M)\times(C-M)=+bxc/2$ — proved in full by a
  four-line bilinearity computation, valid for **every** triangle (no case
  split, no genericity restriction). Directly closes the round-2-flagged
  overclaim in this file's (H2),(H3) sign derivation, and is reusable by
  any approach (e.g. `coordinate-bash-resultant`'s branch-selection gap,
  though that gap was independently confirmed this round by the sign-lemma
  explorer to be a *different* sign question — dot-product/acute-angle, not
  cross-product/rotation-direction — so this lemma does NOT resolve that
  gap; flagged explicitly to avoid future conflation) as a general-purpose
  tool for fixing directed-angle sign conventions at a vertex or a midpoint
  of a triangle side.
- **(H1)-(H3): the three hypotheses as complex "ratio ∈ ℝ_{>0}" conditions**,
  with signs fixed by a genuine synthetic orientation argument (not numerical
  sampling), now resting on the fully general Lemma 6 rather than a
  representative-triangle check — see Step 3 above for the full derivation
  and the exact statements. This is the most reusable output of this round:
  any future complex-number or trig approach to the remaining gap can import
  (H1)-(H3) directly instead of re-deriving the sign conventions from the
  containment
  hypotheses.
- **Structural retirement of "independent-conjugate ideal-membership +
  extra generators" as a method (Step 5, new this round)**: for the
  complex-cross-ratio elimination target $T$ (concyclicity of A,K,L,Q) built
  from cleared-denominator "ratio ∈ ℝ" hypotheses $P_1,\dots,P_n$ over the
  ring $\mathbb Q(B,\bar B,C,\bar C)[K,\bar K,L,\bar L]$ with
  $K,\bar K,L,\bar L$ treated as *formally independent* variables: no matter
  how many further true geometric hypotheses of the same "ratio-is-real"
  species are adjoined as ideal generators, $T$ cannot be forced into the
  ideal, because the missing constraint (the antiholomorphic reality
  relation $\bar K=\overline K,\bar L=\overline L$ literally, i.e.\ complex
  conjugation) is not a polynomial condition and is invisible to any ideal
  built this way — proved in Step 5.3 by a dimension-count argument (the
  true real configuration is a proper real-codimension-$\ge$1 slice of the
  complex variety cut out by such generators) plus a concrete confirming
  computation (Step 5.2: even the boundary-equality relaxation of two
  additional true hypotheses fails to reduce $T$'s remainder to zero).
  Reusable as a general warning/theorem for any future complex-bash
  concyclicity approach to this problem (or similar problems) using the
  independent-conjugate device: it can prove *sufficiency* results (if $T$
  reduces to 0, the real target follows) but can never, by adjoining more
  generators of this species, repair a nonzero remainder — a genuinely real
  (coordinate) reformulation is required instead.
- **Theorem 8 (round 8, §7): `Rem=0`/`χ∈ℝ` is a formal corollary of
  `⟨G2a,G3a⟩`.** Substituting the coordinate route's certified rotation
  parametrization `K(t_1,u),L(s_2,u,a,b,cc)` (real, so `\bar K,\bar L` are
  *true* conjugates, sidestepping the Step 4/5 "independent-conjugate
  reality gap" entirely) into the cross-ratio target
  `\chi=L(K-Q)/(Q(K-L))`, the numerator `T_2` of `\chi-\bar\chi` (an
  explicit degree-14 polynomial in `t_1,s_2,u,a,b,cc`, 280 monomials) is
  **exactly** in the ideal `⟨G_{2a},G_{3a}⟩\subset\mathbb
  Q[t_1,s_2,u,a,b,cc]` (Gröbner-basis remainder `0`, same 18-generator basis
  as `lemmas/symbolic-genericity-certificate.md`; confirmed not in
  `⟨G_{2a}⟩` or `⟨G_{3a}⟩` alone, and confirmed to vanish at all real roots
  of `G_{2a},G_{3a}` at 15 random, non-geometric `(a,b,cc,u)` samples, not
  merely at sampled geometric points). Consequently, on the branch
  `G_{2a}=G_{3a}=0` — the same branch on which `lemmas/symbolic-genericity-
  certificate.md` already proves the central identity `OM=ON` — the points
  `A,K,L,Q` are automatically concyclic-or-collinear, for every real
  non-degenerate triangle, with no further sign/positivity argument needed.
  Reusable directly as an extension of `lemmas/symbolic-genericity-
  certificate.md`'s branch: any future approach needing `χ\in\mathbb R` (or
  equivalent concyclicity facts) on this same branch can cite this result
  instead of re-deriving it. Proved in full in §7 above; independently
  cross-checked numerically (40 genuine `fsolve`-solved configurations, true
  unsquared hypotheses + containment filter, `max|Im(\chi)|=1.4\times
  10^{-12}$) before the symbolic computation, per this round's dispatch
  instruction to re-validate the numeric ground truth first.
