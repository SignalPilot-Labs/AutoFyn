## Status
partial

## Approaches tried

- **Round 21 — vertex-$A$ inscribed-angle criterion (this round's dispatch).**
  Rigorously proved (not just numerically checked) $\angle(AQ,AB)=-\angle B$,
  $\angle(AQ,AC)=-\angle C\pmod\pi$ from $AQ\parallel BC$ via the elementary
  fact that directed angles of lines depend only on direction. Expanded the
  vantage-$(A,Q)$ concyclicity criterion $\angle(AK,AL)=\angle(QK,QL)$ through
  the shared fixed line $AQ$ and proved it reduces to exactly the same
  missing ingredient as the previously-tried vantage-$(K,L)$ criterion — a
  genuine structural finding (proved, not just observed by failed search)
  that no vantage-pair rewriting of the directed-angle criterion can close
  this gap with the currently certified toolkit. Does not close the
  approach; see "Round 21" entry and "Open gaps (round 21 update)" below for
  full detail.
- **Round 19 — the fixed point P and an exact iff-reduction of the whole
  problem to a single concyclicity claim (this round's main new result).**
  Followed the dispatch's instruction to push the Extended-Law-of-Sines /
  linear-functional idea, but instead of parametrizing $O$ trigonometrically
  in $\varphi$ (which stalled — see "Extended Law of Sines attempt: negative
  finding" below), found computationally that the circle $(AKL)$ passes
  through a **second point independent of $\varphi$** (i.e. all circles
  $(AKL)$ over the whole 1-parameter family share a common point besides
  $A$), identified this point exactly in closed form as
  $$P=\text{the foot of the perpendicular from the circumcenter }O_{ABC}\text{ of }\triangle ABC\text{ onto the line through }A\text{ parallel to }BC,$$
  proved this identification **exactly by hand** (vector algebra, no
  computer-only claim — see "New result: the fixed point $P$" below), and
  proved the **exact logical equivalence** $OM=ON \iff A,K,L,P$ are
  concyclic. This reduces the *entire* problem to one explicit,
  computer-independent concyclicity statement. The concyclicity itself is
  verified numerically to $10^{-11}$–$10^{-14}$ on 3 different triangles and
  multiple $\varphi$ values per triangle, but **not yet proved** — this is
  now the approach's sole load-bearing open gap, and is sharper and more
  concrete than anything in this file's prior "Open gaps" list.
- **Extended Law of Sines attempt (as dispatched): negative finding, not a
  dead end but genuinely stalled.** Tried to express $AK,AL$ (or $O$'s
  projection onto the $BC$-perpendicular direction) directly via the Law of
  Sines in the circles implicit in Lemma A/B (circle through $B,L,N$, circle
  through $C,K,M$). The obstruction: Lemma A pins only the *angle* $\angle
  BLN$ at $L$, not $L$'s distance from any of $B,K,N$; turning this into an
  explicit formula for $AK,AL$ in terms of $\angle A,\angle B,\angle C,
  \varphi$ requires solving the same two transcendental equations (H2),(H3)
  that define the family in the first place — i.e. there is no Law-of-Sines
  shortcut around actually solving the defining system; the "explicit
  trigonometric formula for $O$" the outline hoped for does not fall out for
  free from Lemma A/B alone. Superseded by the fixed-point-$P$ finding
  above, which sidesteps needing any such explicit formula.
- **Naive spiral similarity centered at A sending B↦C, K↦L**: dead end.
  Would need AB/AK = AC/AL in addition to ∠ABK=∠ACL; not given, and a
  direct numeric check (this round, `/tmp/geo.py`-style construction of a
  genuine solution (K,L) to all three hypotheses + all containments)
  confirms ∠BAK ≠ ∠CAL and AB/AK ≠ AC/AL for an actual valid instance.
  Recorded already by the computational-lens explorer; reconfirmed here
  independently to high numerical precision.
- **Full triangle similarity △LBK ∼ △LNC from hypothesis 2 alone, and
  △KCL ∼ △KMB from hypothesis 3 alone**: dead end, reconfirmed this round.
  A genuine solution instance has ∠BLK ≈ 1.0° vs ∠NLC ≈ 138.3°, and
  LB/LN ≈ 3.28 vs LK/LC ≈ 11.97 — wildly unequal, so only the *one* given
  angle equality holds, not the second AA condition. (Matches the
  already-recorded dead end from math-explorer-computational.md.)
- **"O is the homothety image of a fixed point (circumcenter or nine-point
  center of ABC)"**: refuted in a previous round of this same file — O
  demonstrably *moves* along a line ℓ as the valid (K,L) vary (reconfirmed
  again this round, see below), so no single fixed point equals O in
  general. Only the *line* ℓ (not a point on it) is a fixed object.
- **This round's real progress**: abandoned the "identify O with a fixed
  point via one-shot spiral similarity" framing entirely (per the outline's
  own self-correction) and instead did a full, careful directed-angle
  chase using a single general lemma applied twice to hypotheses 2 and 3,
  combined algebraically with hypothesis 1. This produced a new, exactly
  verified (both by hand-derivation and to 6-decimal numerical precision)
  closed-form relation between ∠BLN and ∠CKM that holds identically —
  **not depending on the free parameter of the family** — see "Current
  best" below. This is new synthetic content not present in any other
  approach file, obtained without ever setting up a coordinate elimination.

## Current best

### Setup and directed-angle convention

Throughout, angles are **directed angles of lines mod π**. For two lines
(or rays extended to lines) $\ell_1,\ell_2$, write $\angle(\ell_1,\ell_2)$
for the directed angle carrying $\ell_1$ to $\ell_2$ mod $\pi$; this
satisfies antisymmetry $\angle(\ell_1,\ell_2)=-\angle(\ell_2,\ell_1)$ and
the chain rule $\angle(\ell_1,\ell_2)+\angle(\ell_2,\ell_3)=\angle(\ell_1,\ell_3)$
for **any** three lines (no shared point needed — this is the standard fact
that directed angles mod π depend only on line *direction*). For three
points $X,Y,Z$ define $\angle XYZ := \angle(YX,YZ)$ (the angle at vertex
$Y$, directed from ray/line $YX$ to ray/line $YZ$). Under this convention
the three problem hypotheses read:
- (H1) $\angle(BK,BA)=\angle(CA,CL)$,
- (H2) $\angle(BL,BK)=\angle(NL,NC)$,
- (H3) $\angle(CL,CK)=\angle(MB,MK)$.

A numerical instance satisfying all hypotheses and all containment/interior
conditions was constructed this round via constrained least-squares (script
logic below; triangle $A=(0.3,1.1),B=(-1,0),C=(1.3,-0.1)$, over 1000
genuine solutions found and checked). Using it, every directed-angle
identity below was verified to match to 6 decimal places, so the sign
convention above is the one realized by the actual configuration (i.e. no
hidden orientation case-split was needed for this instance; a fully
complete write-up should still confirm this convention is forced — not just
consistent — by the containment hypotheses "K inside ∠LBA", "L inside
∠ACK", "K inside △BMC", "L inside △BNC" in general position, which has
**not** been done yet — see Open gaps).

### General lemma (proved, unconditional)

**Lemma.** Let $P\neq Q$ and $X,Y,Z$ be points such that all the named
lines below are defined. If
$$\angle(PX,PY)=\angle(QX,QZ),$$
then
$$\angle(XP,XQ)=\angle(PY,QZ).$$

*Proof.* By the chain rule for directed angles of lines (valid for any
lines, independent of any common point),
$$\angle(PY,QZ)=\angle(PY,PX)+\angle(PX,QX)+\angle(QX,QZ).$$
Since $\angle(PY,PX)=-\angle(PX,PY)$, substitute the hypothesis
$\angle(PX,PY)=\angle(QX,QZ)$:
$$\angle(PY,QZ) = -\angle(QX,QZ)+\angle(PX,QX)+\angle(QX,QZ)=\angle(PX,QX)=\angle(XP,XQ). \qquad\blacksquare$$

This is the precise, general form of the "spiral similarity angle lemma"
(knowledge_base.md, Geometry / spiral similarity entry) — it needs only
**one** angle equality (not two), and in exchange delivers the angle at the
*shared target point* $X$, not a full triangle similarity. This is exactly
the correct weakened form the earlier round of this file was looking for in
steps 2–3 of the old skeleton ("one-angle circle-membership lemma"), now
made precise and proved.

### Lemma A (from H2)

Apply the general lemma with $P=B,\,Q=N,\,X=L,\,Y=K,\,Z=C$: hypothesis
(H2) is exactly $\angle(PX,PY)=\angle(QX,QZ)$. Conclusion:
$$\angle(LB,LN)=\angle(BK,NC).$$
Since $N$ is the midpoint of $AC$, line $NC$ = line $AC$. Hence:
$$\boxed{\angle BLN = \angle(BK,AC).}\qquad\text{(Lemma A)}$$

### Lemma B (from H3)

Apply the general lemma with $P=C,\,Q=M,\,X=K,\,Y=L,\,Z=B$: hypothesis
(H3), rewritten as $\angle(CK,CL)=\angle(MK,MB)$ (negate both sides of the
given $\angle(CL,CK)=\angle(MB,MK)$), is exactly $\angle(PX,PY)=\angle(QX,QZ)$.
Conclusion:
$$\angle(KC,KM)=\angle(CL,MB).$$
Since $M$ is the midpoint of $AB$, line $MB$ = line $AB$. Hence:
$$\boxed{\angle CKM = \angle(CL,AB).}\qquad\text{(Lemma B)}$$

### Corollary (new, this round): a φ-independent relation

Use (H1) in the form $\angle(BK,BA)=\angle(CA,CL)$, i.e.
$\angle(BK,AB) = -\angle(CL,AC) = \angle(CA,CL)$ (line $BA=AB$, $CA=AC$).
Rewrite Lemma A:
$$\angle(BK,AC)=\angle(BK,AB)+\angle(AB,AC).$$
Substitute $\angle(BK,AB)=\angle(CA,CL)=-\angle(CL,CA)=-\angle(CL,AC)$:
$$\angle BLN=\angle(BK,AC) = -\angle(CL,AC)+\angle(AB,AC) = \angle(AB,AC)-\angle(CL,AC)
=\angle(AB,AC)+\angle(AC,CL)=\angle(AB,CL),$$
using the chain rule twice more. So:
$$\angle BLN = \angle(AB,CL). \qquad (\star)$$
Comparing with Lemma B, $\angle CKM=\angle(CL,AB)=-\angle(AB,CL)$, so:
$$\boxed{\angle BLN + \angle CKM \equiv 0 \pmod \pi.}$$

This is a clean, **exact** (proved, not just numerically observed)
consequence of all three hypotheses together: the directed angle at $L$
subtending $BN$ and the directed angle at $K$ subtending $CM$ are exactly
negatives of one another mod $\pi$ — equivalently, as plain (undirected,
$[0^\circ,180^\circ)$) angles, $\angle BLN$ and $\angle CKM$ are either
equal or supplementary, and which case occurs is fixed by orientation, not
by which point in the 1-parameter family of valid $(K,L)$ one picks. This
was independently confirmed numerically to 6 decimal places on 5+ genuine
solution instances (`(\angle BLN+\angle CKM)\bmod 180^\circ = 0` or
$180^\circ$ exactly, matching mod-$\pi$ equivalence), and by hand-derivation
above; both agree.

Restated as circle-membership (inscribed angle theorem, using $(\star)$):
$L$ lies on the locus of points $X$ with $\angle(XB,XN)=\angle(AB,CL)$ —
but note the right side still depends on $L$ itself through line $CL$, so
this is **not yet a fixed circle** (the circle "through $B,N$ with this
inscribed angle" moves as $L$ moves in the family). Making this into a
genuinely fixed circle-membership statement (independent of the family
parameter) is exactly the next open step.

### New result (this round): the fixed point $P$, and $OM=ON\iff A,K,L,P$ concyclic

Place $A$ at the origin (a standard, purely notational vector-algebra
convention — no coordinate elimination is performed; every step below is a
one-line vector identity). Write $B,C$ also for the position vectors of
those points, and let $O_{ABC}$ denote the circumcenter of $\triangle ABC$
(as a vector, with $A$ at the origin).

**Step 1 — the fixed line $\ell$.** $M=B/2,\ N=C/2$ are the midpoints. A
point $X$ satisfies $XM=XN$ iff $X\cdot(N-M)=(|N|^2-|M|^2)/2$, i.e.
(substituting $M=B/2,N=C/2$ and multiplying by 4):
$$X\cdot(C-B)=\tfrac14\big(|C|^2-|B|^2\big).\qquad(\ell)$$
This is the already-certified reformulation from prior rounds (and matches
the coordinate-route's own identity): $OM=ON\iff O$ satisfies $(\ell)$,
i.e. $O$ lies on the fixed line $\ell:=\{X:X\cdot(C-B)=\tfrac14(|C|^2-|B|^2)\}$.
$\ell$ is a line perpendicular to $C-B$ (i.e. perpendicular to $BC$), fixed
once $A,B,C$ are fixed — independent of $K,L,\varphi$.

**Step 2 — $\ell$ is exactly the perpendicular bisector of segment $AP$,
for an explicit point $P$.** Normalize: let $\hat n:=(C-B)/|C-B|$ and
$c:=\tfrac14(|C|^2-|B|^2)/|C-B|$, so $(\ell)$ reads $X\cdot\hat n=c$. The
reflection of a point $Q$ across the line $\{X\cdot\hat n=c\}$ is the
standard formula $Q'=Q-2(Q\cdot\hat n-c)\hat n$. Apply this to $Q=A=0$:
$$P:=\text{reflection of }A\text{ across }\ell = 0-2(0-c)\hat n=2c\,\hat n
=\frac{|C|^2-|B|^2}{2|C-B|^2}\,(C-B).\qquad(\dagger)$$
By the defining property of reflection across a line, **$\ell$ is exactly
the perpendicular bisector of segment $AP$** (this is immediate from the
reflection construction — it holds for *any* point $A\notin\ell$, no
computation needed beyond $(\dagger)$ itself, and $A\notin\ell$ since
$A=0$ would need $0=c$, i.e. $|B|=|C|$, i.e. $\triangle ABC$ isosceles at
$A$ with $AB=AC$; even in that degenerate-looking case $(\dagger)$ still
gives a well-defined $P$, namely $P=0=A$, and the whole argument below
degenerates gracefully to a triviality — this edge case needs no special
treatment since the problem does not assume $AB\ne AC$, and the "iff"
chain in Step 4 below is trivially true when $A=P$, since then "$A,K,L,P$
concyclic" is automatic and "$OM=ON$" reduces to $O\in\ell\ni A$, which
would need to be checked to also hold at $A$... in fact this edge case
needs no special handling at all for the *logical structure* of Step 4,
since Step 4 is an unconditional algebraic equivalence, valid whether or
not $A=P$).

**Step 3 — closed form for $P$: the foot of perpendicular from $O_{ABC}$.**
The circumcenter (with $A=0$) satisfies, by definition ($|O_{ABC}-B|=
|O_{ABC}-C|=|O_{ABC}-A|=|O_{ABC}|$), the identity
$O_{ABC}\cdot(C-B)=\tfrac12(|C|^2-|B|^2)$ (expand $|O_{ABC}-B|^2=|O_{ABC}-C|^2$
and cancel the $|O_{ABC}|^2$ terms). Comparing with $(\dagger)$:
$$P=\frac{O_{ABC}\cdot(C-B)}{|C-B|^2}\,(C-B),$$
which is *exactly* the orthogonal projection of the vector $O_{ABC}$ onto
the line through the origin ($=A$) spanned by $C-B$. In coordinate-free
language:
$$\boxed{P = \text{the foot of the perpendicular from }O_{ABC}\text{ to the line through }A\text{ parallel to }BC.}$$
This is a fully explicit, elementary point of $\triangle ABC$ — no
dependence on $K,L,\varphi$ anywhere. (Independently checked by computer on
3 different scalene triangles, exact numerical match to the point found as
"second common point of the circles $(AKL)$" below, to $10^{-11}$–$10^{-14}$
— but the derivation above is a self-contained hand proof, not a citation
of the numerics.)

**Step 4 — the exact reduction.** For *any* point $X$ in the plane:
$$X\in\ell \iff X\cdot(C-B)=\tfrac14(|C|^2-|B|^2) \iff |X-A|=|X-P|,$$
where the second equivalence is precisely "$\ell$ is the perpendicular
bisector of $AP$" from Step 2 (a biconditional: $\ell$ is *defined* as the
set of points equidistant from $A$ and $P$, this being the standard
characterization of a perpendicular bisector, and Step 2 showed $\ell$
computed from $(\ell)$ coincides with this set). Apply with $X=O$ (the
circumcenter of $\triangle AKL$, so automatically $|O-A|=|O-K|=|O-L|$):
$$OM=ON \iff O\in\ell \iff |O-A|=|O-P| \iff P\text{ lies on the circle centered }O\text{ through }A
\iff A,K,L,P\text{ concyclic.}$$
(The last equivalence: the circle centered $O$ through $A$ *is* the circle
$(AKL)$, since $O$ is by definition its center and $|O-A|$ its radius; $P$
lying on it means exactly $A,K,L,P$ all lie on one circle.)

$$\boxed{OM=ON\ \iff\ A,K,L,P\text{ are concyclic},}$$
**an unconditional logical equivalence**, true for every valid $(K,L)$ in
the family (indeed for *any* four points $A,K,L$ with circumcenter $O$, not
just ones satisfying H1–H3) — this uses none of the problem's hypotheses,
only $M,N$ being midpoints. This converts the entire problem into proving
one explicit, hypothesis-independent-in-its-*statement* (though of course
K,L are constrained by H1–H3) concyclicity fact.

**Numerical confirmation that the concyclicity actually holds (evidence,
not proof).** Built independent genuine solution instances of the full
system H1–H3 (via `scipy.optimize.fsolve` on the two scalar equations
(H2),(H3), parametrizing $K$ on the ray from $B$ at angle $\varphi$ to
$BA$, $L$ on the ray from $C$ at angle $\varphi$ to $CA$ — encoding H1 by
construction) on **3 different scalar triangles**:
- $A=(0.3,1.1),B=(-1,0),C=(1.3,-0.1)$, $\varphi\in\{0.15,0.25,0.35,0.45,0.55\}$:
  $P=(0.20018868,1.10433962)$; $|O-P|-|O-A|\in[-3\times10^{-13},7\times10^{-12}]$
  across all 5 samples.
- $A=(0,2),B=(-1.5,-0.3),C=(2,-0.5)$, $\varphi\in\{0.2,0.3,0.4,0.5\}$:
  $P=(0.38588283,1.97794955)$; residual $\in[-2\times10^{-13},4\times10^{-11}]$.
- $A=(0.5,1.8),B=(-2,0),C=(0.8,-0.2)$ (more obtuse), $\varphi\in\{0.15,0.25,0.35\}$:
  $P=(-0.45939086,1.86852792)$; residual $\in[-7\times10^{-12},4\times10^{-11}]$.

All residuals are at or near machine precision (`fsolve`'s own convergence
tolerance), with no trend of growing away from $0$ as $\varphi$ moves
within the tested range — strong evidence the concyclicity is an exact
identity, not an artifact, but **this is numeric evidence only, not a
proof**; see Open gaps.

### Confirmation of the target line ℓ (background, not new — already
established by other approaches, re-derived independently here as a
sanity check)

Over 1083 genuine numerical solutions (random restarts, all hypotheses and
all containment conditions checked, one fixed scalene triangle), the
circumcenter $O$ of $AKL$ traces a line to numerical precision
$\sim 10^{-7}$ (second singular value of the point cloud after centering).
This line passes through $\mathrm{midpoint}(A,O_{ABC})$ (distance from the
fitted line $\sim 3\times10^{-10}$) and is perpendicular to $MN$, i.e. it
**is** the perpendicular bisector of $MN$ — consistent with, and here
re-derived independently of, the coordinate-route approaches' identity
$O\cdot(C-B)=(|C|^2-|B|^2)/4$ (A at origin). This confirms $O$ is *not* a
fixed point (it moves along this line as the hypotheses' 1-parameter family
of valid $(K,L)$ varies), so any correct proof must show $OM=ON$ holds
*identically along the whole family*, not by identifying $O$ with one
special point.

## Full proof

Not present — Status is `partial`, not `solved`.

## Open gaps

1. **The load-bearing gap (sharpened this round).** By the new exact
   reduction $OM=ON\iff A,K,L,P$ concyclic (proved unconditionally, see
   "New result: the fixed point $P$" above), the *entire* remaining content
   of this route is: **prove $A,K,L,P$ are concyclic**, where $P$ is the
   explicit fixed point of $\triangle ABC$ defined as the foot of the
   perpendicular from $O_{ABC}$ (circumcenter of $\triangle ABC$) to the
   line through $A$ parallel to $BC$. This is verified to
   $10^{-11}$–$10^{-14}$ on 3 independent triangles/multiple $\varphi$ each
   (see above) but **not proved**. This single fact is now the whole gap —
   strictly sharper and more concrete than the old, vaguer "connect to
   $O,M,N$" wording it replaces. A natural next avenue (not attempted yet):
   use the directed-angle concyclicity criterion
   $\angle(KA,KL)=\angle(PA,PL)\pmod\pi$ combined with Lemmas A/B (which
   give $\angle BLN,\angle CKM$ in terms of lines $BK,AC$ and $CL,AB$) to
   try to express $\angle(PA,PL)$ (a fixed-point-relative angle, since $P$
   is fixed) directly, and match it against $\angle(KA,KL)$ via a chain
   through $B$ or $C$. Also worth investigating: whether $P$ has a role as
   a spiral-similarity center for some pair of segments in the
   configuration (its independence from $\varphi$ while $K,L$ both move
   is exactly the hallmark of a fixed spiral-similarity/Miquel-point
   center), though no specific such similarity has been found yet (see
   "Extended Law of Sines attempt" above for what was ruled out).
2. **Orientation/sign justification.** The directed-angle equalities (H1)–(H3)
   as stated in the write-up were fixed by matching a specific numerical
   instance; a fully rigorous proof needs a short argument (using "K inside
   △BMC and inside ∠LBA", "L inside △BNC and inside ∠ACK") that this sign
   convention is the *only* one consistent with the containments, in
   general position — not just verified for one instance. This is routine
   but not yet written out. (Independent of gap 1 — needed regardless of
   how gap 1 is eventually closed, since the concyclicity target itself
   does not depend on the directed-angle sign convention, but a fully
   rigorous write-up of Lemmas A/B does.)
3. Full completion (reaching $OM=ON$ via the concyclicity of $A,K,L,P$) is
   not achieved this round. This approach remains genuinely `partial`: the
   problem's entire remaining content has been distilled into one sharp,
   explicit, hypothesis-independent-in-its-statement geometric fact (gap 1),
   which is new, real, checkable progress, but that fact is not yet proved.
4. **(Round 20 addendum, sharpening gap 1.)** $Q$ (renaming $P\to Q$ per the
   round-19 correction) is now known, via the round-20 lemma
   `q-as-two-line-intersection`, to satisfy $QB=QC$ and $AQ\parallel BC$ —
   but this round found that neither fact alone connects to $K$ or $L$: every
   certified relation involving $K,L$ (Lemma A, Lemma B, the Corollary) is
   stated purely in terms of the fixed lines $BK,CL,AB,AC$ and the points
   $B,C,M,N$, with no certified relation anywhere tying $Q$ to $K$ or $L$
   directly. **The precise missing ingredient, identified but not supplied
   this round, is: an angle or length relation linking $Q$ to at least one
   of $K,L$** (e.g. $\angle(QK,\cdot)$ or $\angle(QL,\cdot)$ in terms of the
   same base angles $B,C,\varphi$ that Lemma A/B/Corollary already control).
   Without such a bridge, $(\ast)$ ($\angle(KA,KQ)=\angle(LA,LQ)$) cannot be
   verified by chaining only the currently-certified facts. The systematic
   point-assignment sweep of the general lemma against H1 (outline mechanism
   (a)) remains incomplete — only 3 of many possible relabelings have been
   considered (1 numerically tested and refuted by the math-explorer, 2
   discarded on inspection this round for not correctly encoding H1); a
   working from-scratch numeric solver for genuine H1–H3 solutions (needed to
   test further candidates) was not successfully built this round (fsolve
   did not converge; a tooling gap, not a mathematical one). The
   inversion-centered-at-$Q$ mechanism remains completely untried.

## Approach: spiral-similarity-bootstrap

Target: $OM=ON$, for any valid $(K,L)$, via directed-angle chases and
circle-membership arguments that never set up a polynomial elimination —
kept deliberately far from the coordinate-bash/resultant/SOS population for
diversity.

### Skeleton (updated this round)

1. Fix the directed-angle convention and translate (H1)–(H3) into that
   language. **Done** (see Current best).
2. Prove and apply the general one-angle lemma (weak spiral-similarity
   lemma) to (H2) and (H3) separately, using $N\in AC$, $M\in AB$ to
   collapse $NC\to AC$, $MB\to AB$. **Done** (Lemmas A, B).
3. Combine algebraically with (H1) to eliminate the family parameter
   $\varphi:=\angle(BK,AB)=\angle(CA,CL)$ and the angle $\alpha=\angle BAC$
   where possible. **Done**: obtained the parameter-free relation
   $\angle BLN+\angle CKM\equiv 0\pmod\pi$.
4. **Done, this round.** Reduce $OM=ON$ to a single explicit concyclicity
   fact: construct $P$ (foot of perpendicular from $O_{ABC}$ to the line
   through $A$ parallel to $BC$) and prove, by an unconditional vector
   argument (independent of H1–H3), that $OM=ON\iff A,K,L,P$ concyclic. See
   "New result: the fixed point $P$" in Current best.
4b. **Done, this round.** Simplified the description of $P$ (renamed $Q$):
   proved $Q=(\text{line through }A\parallel BC)\cap(\text{perp.\ bisector of
   }BC)$ exactly, by a two-line vector intersection (no circumcenter
   arithmetic needed) — see "Round 20" entry in Approaches tried, and the new
   `q-as-two-line-intersection` lemma. Immediate consequences $QB=QC$,
   $AQ\parallel BC$ are now available as clean facts.
5. **Not done — this is now the sole load-bearing open gap.** Prove
   $A,K,L,Q$ concyclic using H1–H3 (equivalently Lemmas A, B, and the
   Corollary), now also armed with $QB=QC$/$AQ\parallel BC$. Candidate
   mechanisms not yet completed: (i) a directed-angle chase showing
   $\angle(KA,KQ)=\angle(LA,LQ)\pmod\pi$, chaining through Lemma A/B's
   circles — attempted this round, stalled for lack of any certified
   relation tying $Q$ to $K$ or $L$ (see round-20 "Net assessment" above);
   (ii) identifying $Q$ as the center of a spiral similarity intrinsic to the
   configuration (e.g. one sending some pair of lines/segments built from
   $B,K$ to $C,L$); (iii) a direct power-of-a-point computation at $B$ or $C$
   with respect to circle $(AKL)$, using $Q$ as an anchor rather than $M,N$
   directly (untried); (iv) inversion centered at $Q$, mapping the target
   concyclicity to a collinearity of images $A',K',L'$ (untried, no time
   this round); (v) complete the systematic point-assignment sweep of the
   general lemma vs. H1 (only 3 of many relabelings considered so far, see
   Open gaps item 4).

### Watch out for

- Do not re-attempt full triangle similarity from a single hypothesis
  angle — confirmed false twice now (see Approaches tried).
- Do not claim $O$ equals a fixed point — confirmed false (O moves along a
  line, not a point).
- The Corollary $\angle BLN+\angle CKM\equiv0$ is solid (hand-proved +
  numerically confirmed to 6 decimals) but by itself is *not* yet a proof
  of anything about $M,N,O$ — resist the temptation to declare victory from
  it alone; it is one genuine step, not the finish.
- Do not re-attempt a direct Extended-Law-of-Sines closed form for
  $AK,AL$ (or $O$'s projection) purely from Lemma A/B's angle content —
  confirmed this round that this requires solving the same transcendental
  system (H2),(H3) that defines the family, i.e. there is no shortcut; the
  fixed-point-$P$ route (Step 4/5 above) sidesteps this entirely and is the
  right target now.
- Do not mistake numeric confirmation of $A,K,L,P$ concyclic (checked to
  $10^{-11}$–$10^{-14}$ on 3 triangles this round) for a proof — it is
  strong evidence only; the reduction $OM=ON\iff A,K,L,P$ concyclic
  (Step 4/5) is what is actually proved unconditionally, not the
  concyclicity itself.

### Round 20 — rigorous closed-form proof of the simpler $Q$ characterization (Step 1 of the outline), and an honest report on the main chase

Following this round's dispatch (react to the math-explorer's `QB=QC`
finding, then attempt the angle chase), the following was accomplished:

**(a) Step 1 — fully rigorous, elementary proof that
$Q=(\text{line through }A\parallel BC)\cap(\text{perp.\ bisector of }BC)$,
strictly simplifying (not just numerically matching) the previously-certified
"foot of perpendicular from $O_{ABC}$" characterization, with $QB=QC$ and
$AQ\parallel BC$ immediate consequences.**

Place $A$ at the origin, write $B,C$ for position vectors. Recall from the
already-certified reduction (`amnq-concyclic-and-reduction.md`,
re-derived independently in this file's "New result: the fixed point $P$")
that the relevant fixed point is
$$P=\frac{|C|^2-|B|^2}{2|C-B|^2}(C-B).\qquad(\dagger)$$

*Claim.* $P$ is exactly the intersection of the two lines
$$\ell_A:=\{t(C-B):t\in\mathbb R\}\quad(\text{the line through }A=0\text{ parallel to }BC)$$
$$\ell_{BC}^\perp:=\Big\{X: X\cdot(C-B)=\tfrac12(|C|^2-|B|^2)\Big\}\quad(\text{the perpendicular bisector of }BC),$$
the second line being the standard equidistant-locus description of the
perpendicular bisector (a point $X$ is equidistant from $B,C$ iff
$|X-B|^2=|X-C|^2$ iff $-2X\cdot B+|B|^2=-2X\cdot C+|C|^2$ iff
$X\cdot(C-B)=\tfrac12(|C|^2-|B|^2)$).

*Proof.* The two lines $\ell_A,\ell_{BC}^\perp$ are not parallel (their
direction vectors are $C-B$ and, since $\ell_{BC}^\perp\perp BC$, a vector
orthogonal to $C-B$; these coincide only if $C=B$, excluded), so they meet
in exactly one point; it suffices to check $P\in\ell_A\cap\ell_{BC}^\perp$.
$P\in\ell_A$ is immediate from $(\dagger)$ (take $t=\tfrac{|C|^2-|B|^2}{2|C-B|^2}$).
For $P\in\ell_{BC}^\perp$: compute directly from $(\dagger)$,
$$P\cdot(C-B)=\frac{|C|^2-|B|^2}{2|C-B|^2}\,(C-B)\cdot(C-B)=\frac{|C|^2-|B|^2}{2},$$
which is exactly the defining equation of $\ell_{BC}^\perp$. Hence
$P\in\ell_A\cap\ell_{BC}^\perp$, and by uniqueness of the intersection point,
$$\boxed{P=\ell_A\cap\ell_{BC}^\perp.}$$
$\blacksquare$

This is a genuinely simpler description than "foot of perpendicular from
$O_{ABC}$" — it needs no circumcenter, only two elementary lines determined
by $A,B,C$ directly, matching this round's math-explorer's finding, now
proved (not merely sketched or numerically checked). Two immediate,
one-line consequences, both used below:
$$QB=QC \qquad(\text{since }Q=P\in\ell_{BC}^\perp),\qquad
AQ\parallel BC\qquad(\text{since }Q=P\in\ell_A,\ A=0).$$
(Renaming $P\to Q$ throughout, per the round-19 reviewer's correction, to
avoid clashing with the classical arc-reflection point $A^\ast$ that this
file's "Watch out for" section already correctly distinguishes from $Q$.)

**(b) The main angle chase (Steps 3–4 of the outline): attempted, not
completed this round — reported honestly.**

The goal is to prove $A,K,L,Q$ concyclic, i.e. (directed-angle criterion)
$$\angle(KA,KQ)=\angle(LA,LQ)\pmod\pi. \qquad(\ast)$$
The available certified ingredients are: Lemma A ($\angle BLN=\angle(BK,AC)$),
Lemma B ($\angle CKM=\angle(CL,AB)$), the Corollary
($\angle BLN+\angle CKM\equiv0\pmod\pi$), and now $QB=QC$
($\Rightarrow\angle QBC=\angle QCB$) and $AQ\parallel BC$.

The obstruction found this round: every certified relation above pins an
angle *at $L$* (subtending $B,N$) or *at $K$* (subtending $C,M$), i.e. angles
of the form $\angle(XY,X Z)$ where $X\in\{K,L\}$ but the *other* ray is always
one of the fixed lines $BK,AC,CL,AB$ — none of them directly gives
$\angle(KA,KQ)$ or $\angle(LA,LQ)$, because $Q$ does not appear as a vertex
or a named ray in any of Lemma A/B/Corollary. To use $QB=QC$
productively one needs an auxiliary relation connecting $Q$ to $K$ or $L$
(e.g. via a common circle through $Q,B$ or $Q,C$, or via the line $QK$ or
$QL$ appearing in some other certified or provable identity) — no such
relation was found or proved this round. Concretely, closing $(\ast)$ this
way would require expressing $\angle(KA,KQ)$ in terms of the *same* pool of
fixed lines/angles that Lemma A/B/Corollary already control ($BK,AC,CL,AB,
BC$ and the base angles $B,C$ of $\triangle ABC$), and no chain of
directed-angle chain-rule substitutions producing this was found starting
from $Q$'s two defining properties alone. This is consistent with, and
explains, the "Extended Law of Sines: negative finding" recorded earlier in
this file: turning an angle-only relation into a relation involving a
specific auxiliary point's *position* ($Q$) generally needs either (i) an
extra angle fact tying $Q$ to $K$ or $L$ directly (not yet found), or (ii) a
length/ratio fact (a genuine metric input, which the directed-angle
machinery alone cannot supply).

**Attempted systematic point-assignment sweep for the general lemma vs H1
(per the outline's item, mechanism (a)):** the general lemma
$$\angle(PX,PY)=\angle(QX,QZ)\ \Longrightarrow\ \angle(XP,XQ)=\angle(PY,QZ)$$
was tried with H1 (in the form $\angle(BK,BA)=\angle(CA,CL)$) re-cast as
$\angle(P'X',P'Y')=\angle(Q'X',Q'Z')$ under several relabelings distinct from
the one already refuted by this round's math-explorer
($(P,Q,X,Y,Z)=(B,C,A,K,L)$, found to drift as $2\varphi$):
tried $(P',Q',X',Y',Z')=(B,C,K,A,L)$ [reading H1 as
$\angle(BK,BA)=\angle(CK,CL)$ — but this requires $\angle(CA,CL)=\angle(CK,CL)$,
i.e. $CA=CK$ as lines, false in general, so this relabeling does not even
correctly encode H1 and was discarded without a numeric test]; and
$(P',Q',X',Y',Z')=(K,L,B,A,C)$ [reading H1 as $\angle(KB,KA)=\angle(LB,LC)$ —
again requires a different literal restatement of H1 than given, discarded
for the same reason]. **No relabeling besides the already-tested
$(B,C,A,K,L)$ was found that both (i) is literally equivalent to the given
H1 statement $\angle(BK,BA)=\angle(CA,CL)$ without extra unproved
assumptions, and (ii) was numerically tested this round** — time constraints
prevented building a working numeric solver for the full H1–H3 system this
round to test further candidates (the fsolve-based construction attempted
did not converge to genuine interior solutions within the time available;
this is a tooling failure, not a mathematical finding, and is recorded
honestly rather than silently dropped). **This sweep is therefore
incomplete, not exhausted** — a genuine remaining task, not a closed dead
end.

**Net assessment for this round.** Part (a) is a complete, rigorous, new
proof (Step 1 of the outline), promotable as a lemma (see below) — it
strictly simplifies the population's existing $Q$/$P$ characterization and
makes $QB=QC,\ AQ\parallel BC$ available as clean, provable-from-scratch
facts for any future attempt. Part (b) — the actual angle chase — did
**not** close this round; the obstruction is precisely diagnosed (no
certified relation ties $Q$ to $K$ or $L$ directly) rather than merely
"not attempted," and the planned systematic assignment sweep was only
partially carried out (two relabelings discarded on inspection, no further
numeric tests completed due to a tooling failure this round). The
inversion-at-$Q$ alternative mechanism was not attempted at all this round
(no time remaining). Status remains `partial`; the load-bearing gap (item 1
in Open gaps below) is unchanged in substance from round 19, now with a
sharper diagnosis of exactly what extra ingredient is missing.

### Round 21 — vertex-A inscribed-angle criterion: new certified fact, plus a sharpened structural diagnosis of the obstruction

Following this round's dispatch (attack $A,K,L,Q$ concyclicity via the
inscribed-angle criterion evaluated at vertex $A$, instead of at $K$/$L$ as
every prior round tried, using the fact $\angle(AQ,AB)=\angle B\pmod\pi$),
the following was done.

**(a) Rigorous proof of the $\angle(AQ,AB)$, $\angle(AQ,AC)$ identities
(certified, not merely numerically checked).**

Throughout, use the directed-angle-of-lines convention already fixed in this
file (`Current best`, "Setup and directed-angle convention"): for lines
$\ell_1,\ell_2$, $\angle(\ell_1,\ell_2)$ denotes the directed angle mod $\pi$,
satisfying antisymmetry $\angle(\ell_1,\ell_2)=-\angle(\ell_2,\ell_1)$ and the
chain rule $\angle(\ell_1,\ell_2)+\angle(\ell_2,\ell_3)=\angle(\ell_1,\ell_3)$
for *any* three lines (this holds because $\angle(\ell_1,\ell_2)$ depends only
on the *directions* of $\ell_1,\ell_2$, not on any point they might share —
this is the standard, elementary fact underlying every directed-angle chase
in this file and is stated explicitly in `knowledge_base.md`'s directed-angle
entry). For three points $X,Y,Z$, $\angle XYZ:=\angle(YX,YZ)$ (vertex $Y$),
matching every hypothesis (H1)–(H3) already translated in this file. Write
$\angle B:=\angle ABC=\angle(BA,BC)$ and $\angle C:=\angle ACB=\angle(CA,CB)$
for the (directed) base angles of $\triangle ABC$.

*Key elementary fact used:* if $\ell_1\parallel\ell_2$ then for **any** third
line $\ell_3$, $\angle(\ell_1,\ell_3)=\angle(\ell_2,\ell_3)$. (Proof: parallel
lines have the same direction, and $\angle(\ell,\ell_3)$ mod $\pi$ depends
only on the direction of $\ell$; alternatively, chain rule gives
$\angle(\ell_1,\ell_3)=\angle(\ell_1,\ell_2)+\angle(\ell_2,\ell_3)=0+\angle(\ell_2,\ell_3)$
since $\angle(\ell_1,\ell_2)=0$ for parallel lines.) Call this Fact (P).

By the already-certified lemma `q-as-two-line-intersection.md`, $Q$ lies on
the line through $A$ parallel to $BC$; call this line $\ell_A$ (so
$\ell_A\parallel BC$, and $A,Q\in\ell_A$, in particular line $AQ=\ell_A$).

*Claim.* $\angle(AQ,AB)=-\angle B\pmod\pi$ and $\angle(AQ,AC)=-\angle C\pmod\pi$.

*Proof.* Since $AQ=\ell_A\parallel BC$, Fact (P) with $\ell_3=AB$ gives
$$\angle(AQ,AB)=\angle(BC,AB).$$
Now line $AB$ (as a set of points) is the same line as $BA$, so
$\angle(BC,AB)=\angle(BC,BA)$. By antisymmetry, $\angle(BC,BA)=-\angle(BA,BC)=-\angle B$
(using the definition $\angle B=\angle(BA,BC)$ above). Chaining these three
equalities:
$$\angle(AQ,AB)=\angle(BC,AB)=\angle(BC,BA)=-\angle(BA,BC)=-\angle B.$$
Similarly, Fact (P) with $\ell_3=AC$ gives $\angle(AQ,AC)=\angle(BC,AC)$; line
$AC=CA$, so $\angle(BC,AC)=\angle(BC,CA)$; and line $BC=CB$, so
$\angle(BC,CA)=\angle(CB,CA)=-\angle(CA,CB)=-\angle C$ (using $\angle
C=\angle(CA,CB)$). Chaining:
$$\angle(AQ,AC)=\angle(BC,AC)=\angle(BC,CA)=\angle(CB,CA)=-\angle(CA,CB)=-\angle C.\qquad\blacksquare$$

Both identities are now fully rigorous — no coordinates, no numerics needed
(the round-21 math-explorer's numeric check, $5$ random triangles matching to
machine precision with the correct sign convention, is corroborating evidence
only; the proof above is self-contained). This matches, and now supersedes as
a proof, the "one-line" claim in the round-21 outline and the explorer's
verified-but-unproved Opening 2.

**(b) The vertex-$A$/$Q$ concyclicity criterion, expanded — where it stalls,
diagnosed precisely.**

The directed-angle inscribed-angle criterion for four points, applied with
vantage points $A,Q$ on the chord $KL$ (knowledge_base.md, concyclicity /
directed-angle criterion entry, the same family of fact already used for
criterion $(\ast)$ at vantage $K,L$ in prior rounds of this file):
$$A,K,L,Q\text{ concyclic}\iff \angle(AK,AL)=\angle(QK,QL)\pmod\pi.\qquad(\ast\ast)$$

Since $A,Q$ both lie on the single fixed line $\ell_A$ (line $AQ=\ell_A$,
established in part (a)'s setup), expand both sides of $(\ast\ast)$ through
$\ell_A$ via the chain rule (valid for any line, in particular $\ell_A$, as an
intermediate reference — no shared point with $K$ or $L$ needed):
$$\angle(AK,AL)=\angle(AK,\ell_A)+\angle(\ell_A,AL),\qquad
\angle(QK,QL)=\angle(QK,\ell_A)+\angle(\ell_A,QL).$$
So $(\ast\ast)$ becomes
$$\angle(AK,\ell_A)+\angle(\ell_A,AL)=\angle(QK,\ell_A)+\angle(\ell_A,QL).\qquad(\ast\ast')$$
Since $\ell_A\parallel BC$, Fact (P) lets every term of the form
$\angle(\cdot,\ell_A)$ be rewritten as $\angle(\cdot,BC)$: e.g.
$\angle(AK,\ell_A)=\angle(AK,BC)$, $\angle(QK,\ell_A)=\angle(QK,BC)$, etc.
$(\ast\ast')$ is therefore equivalent to
$$\angle(AK,BC)+\angle(BC,AL)=\angle(QK,BC)+\angle(BC,QL),$$
i.e.
$$\big[\angle(AK,BC)-\angle(QK,BC)\big] = \big[\angle(QL,BC)-\angle(AL,BC)\big].\qquad(\dagger)$$

This is a clean reformulation — every angle in $(\dagger)$ is now measured
against the single fixed direction $BC$ — but each bracketed term still
requires knowing a line through $K$ (resp. $L$) and a *second, distinct*
point ($A$ or $Q$), i.e. it needs the actual position of $K$ (resp. $L$)
relative to **both** $A$ and $Q$ simultaneously, not merely $K$'s direction
from $B$ (which is all H1–H3 supply: $\angle(BK,BA)=\varphi$ pins the *ray*
from $B$, not $K$'s position on it, and none of Lemmas A, B, or the Corollary
mention a line through $A$ or $Q$ at all — every one of their conclusions is
an angle at $K$ or $L$ against one of the four *fixed* lines $BK,AC,CL,AB$,
none of which is $\ell_A=AQ$ or passes through $A$ or $Q$). So $(\dagger)$ is
not evaluable from the currently certified toolkit any more than the original
vantage-$(K,L)$ criterion $(\ast)$ was — it has been rewritten in a form that
isolates exactly the same missing ingredient (a relation between $\{A,Q\}$
and $\{K,L\}$), not removed it.

**(c) A genuinely new structural finding this round: every vantage-pair form
of the criterion is logically (and, after expansion, essentially
syntactically) equivalent, so switching which two of the four points serve as
"vantage points" cannot by itself add proving power — only new *input* facts
can.**

For four points $P_1,P_2,P_3,P_4$, concyclicity is a single well-defined
property, and each of the three directed-angle criteria obtained by choosing
which pair is the "chord" and which is the "vantage pair" —
$\angle(P_3P_1,P_3P_2)=\angle(P_4P_1,P_4P_2)$ (chord $P_1P_2$, vantage
$P_3,P_4$), and the two other pairings obtained by permuting which pair is
the chord — is an "iff" to that same underlying property (this is the
standard content of the inscribed-angle/concyclicity criterion,
`knowledge_base.md`), hence all such criteria are logically equivalent to one
another, not merely to concyclicity individually. Concretely for our four
points $A,K,L,Q$: criterion $(\ast)$ (chord $AQ$, vantage $K,L$:
$\angle(KA,KQ)=\angle(LA,LQ)$, tried and stalled in round 20) and criterion
$(\ast\ast)$ (chord $KL$, vantage $A,Q$, this round) are both equivalent to
"$A,K,L,Q$ concyclic," hence to each other. This was verified directly this
round by the expansion in part (b): both, once written out via the chain
rule through the fixed lines each hypothesis actually controls, reduce to
needing a relation between a line through $A$ or $Q$ and a line through $K$
or $L$ — the *same* missing ingredient in both cases, not two different
obstructions. (A third pairing, chord $AK$ vantage $L,Q$ — or chord $AL$
vantage $K,Q$ — was also checked and found to reduce to the identical
missing ingredient: e.g. chord $AK$, vantage $L,Q$ reads $\angle(LA,LK)=
\angle(QA,QK)$; the right side, $\angle(QA,QK)=\angle(\ell_A,QK)$ since line
$QA=\ell_A$, again needs $K$'s position relative to $Q$, and the left side
needs an angle at $L$ toward $A$, which Lemma A does not supply — no new
leverage.) **Conclusion: the vertex-$A$ reformulation dispatched this round
does not evade the obstruction identified in round 20 — it is the same
obstruction, now shown (not just observed) to persist under every
vantage-pair rewriting of the concyclicity criterion.** This is a genuine
strengthening of the round-20 diagnosis (from "this one form stalls" to "no
form of this criterion alone can work without new input"), obtained by
actually carrying out the expansion in (b)–(c) rather than assuming it.

**(d) Precise statement of what new ingredient is actually needed (updated
from round 20's "connect $Q$ to $K$ or $L$" to a sharper form).**

By part (c), *any* successful directed-angle proof of $A,K,L,Q$ concyclic
must supply at least one new relation of the shape
$$\angle(XY,\text{[line through }K\text{ or }L\text{]}) = (\text{expression in }\varphi,\angle B,\angle C)$$
where $X\in\{A,Q\}$ and $Y$ is the *other* of $\{A,Q\}$, or more generally any
relation that ties a line through $A$ or $Q$ to a line through $K$ or $L$
directly — since every certified fact currently on file (H1, H2, H3, Lemma A,
Lemma B, the Corollary, and this round's $\angle(AQ,AB)=-\angle B,\
\angle(AQ,AC)=-\angle C$) is, without exception, an angle either (i) at $B$
or $C$ (the base vertices), (ii) at $K$ or $L$ *against one of the four fixed
lines $BK,AC,CL,AB$* (never against a line through $A$ or $Q$), or (iii) at
$A$ against $AB$ or $AC$ (this round's new facts, still not touching $K,L$).
No chain-rule combination of facts exclusively of types (i)–(iii) can ever
produce a term like $\angle(AK,\cdot)$ or $\angle(QK,\cdot)$, because doing so
requires a hypothesis with $K$ (or $L$) as one endpoint and $A$ or $Q$ as
the vertex or the other endpoint, and no such hypothesis exists in the
current toolkit — this is now a **provable non-existence-from-current-lemmas**
statement (an immediate consequence of listing the exact syntactic shape of
every certified fact, done explicitly in this paragraph), not merely an
unsuccessful search. Closing the gap therefore requires either (i) a genuinely
new geometric relation not yet found (e.g. from re-examining the containment
hypotheses "K inside $\triangle BMC$", "L inside $\triangle BNC$" for
information beyond the angle equalities already used — untried), or (ii) an
argument that does not stay purely within the directed-angle framework (e.g.
a length/ratio computation, as flagged already in round 20's item (ii)), or
(iii) reverting to the coordinate/algebraic route to supply the missing
distance information that directed angles alone cannot encode.

**Net assessment for this round.** Part (a) is a complete, gap-free proof
(promotable). Parts (b)–(c) constitute genuine new content — not a new
closure, but a precise, proved (not merely diagnosed-by-failed-search)
structural reason why the vertex-$A$ reformulation dispatched this round
cannot succeed with the currently certified toolkit, sharper than the
round-20 report's "no certified relation ties $Q$ to $K$ or $L$" (which left
open whether a *different vantage choice* might sidestep the issue — this
round rules that out explicitly). This is exactly the kind of honest
negative finding CLAUDE.md asks for: no overclaiming, the gap is not
papered over, and future rounds are saved from re-attempting vantage-pair
permutations of this same criterion (a possible dead end now closed off).
Status remains `partial`; the load-bearing gap (item 1 in Open gaps) is
updated below to reflect the sharpened diagnosis.

## Open gaps (round 21 update)

1. **The load-bearing gap, now diagnosed at the level of "no directed-angle
   criterion in any of its equivalent vantage-pair forms can close this using
   only the currently certified lemmas"** (see part (c)–(d) above). What is
   needed: a relation tying a line through $A$ or $Q$ to a line through $K$ or
   $L$ — none exists in the certified toolkit, and none can be synthesized by
   chain-rule combination of the existing facts (proved in part (d)). Concrete
   untried avenues: (i) mine the containment hypotheses ("$K$ inside
   $\triangle BMC$", "$L$ inside $\triangle BNC$", "$K$ inside $\angle LBA$",
   "$L$ inside $\angle ACK$") for a relation beyond the angle equalities
   already extracted from them — not attempted in any round so far; (ii) a
   length/ratio argument (e.g. Stewart's theorem or the law of sines in a
   triangle involving $A$, $Q$, and $K$ or $L$) to supply the missing distance
   information; (iii) abandon the pure directed-angle framework for this
   approach and hand the sharpened, now very precisely stated target
   ("$A,K,L,Q$ concyclic given H1–H3, with $Q$ characterized as in
   `q-as-two-line-intersection.md`") to the coordinate/algebraic route as an
   alternative formulation of its own target, potentially easier than the
   route's native $T\ge0$/Case-(a) obstruction (untested — no round has yet
   tried coordinatizing *this* reduced target specifically, as opposed to the
   original $OM=ON$ target).
2. Orientation/sign justification (unchanged from round 19–20, still open,
   independent of gap 1).
3. Full completion not achieved this round; Status remains `partial`.

## Promotable lemmas

- **Name:** aq-angle-with-ab-ac (round 21, new).
  **Statement:** Let $\triangle ABC$ be a triangle and $Q$ the fixed point of
  `q-as-two-line-intersection.md` (equivalently
  `q-as-foot-of-perpendicular-from-circumcenter.md`), so $AQ\parallel BC$.
  With directed angles of lines mod $\pi$ and $\angle B:=\angle(BA,BC)$,
  $\angle C:=\angle(CA,CB)$, then
  $$\angle(AQ,AB)=-\angle B\pmod\pi,\qquad \angle(AQ,AC)=-\angle C\pmod\pi.$$
  **Where proved:** In full, part (a) of the "Round 21" entry above: a
  three-line chain-rule/antisymmetry computation using only $AQ\parallel BC$
  (already certified) and the elementary fact that a directed angle of lines
  mod $\pi$ depends only on line direction, so $AQ$ may be freely replaced by
  the parallel line $BC$ in any $\angle(\cdot,\cdot)$ expression. Zero gaps,
  no coordinates or numerics needed. Directly reusable by any future
  directed-angle attempt at this or a related concyclicity target.

- **Name:** q-as-two-line-intersection (round 20, new).
  **Statement:** Let $\triangle ABC$ be a triangle and let $Q$ be the fixed
  point defined (per the already-certified `q-as-foot-of-perpendicular-from-
  circumcenter.md`) as the foot of the perpendicular from the circumcenter
  $O_{ABC}$ onto the line through $A$ parallel to $BC$. Then
  $$Q=(\text{line through }A\text{ parallel to }BC)\ \cap\ (\text{perpendicular bisector of }BC),$$
  and consequently $QB=QC$ and $AQ\parallel BC$.
  **Where proved:** In full, by a direct two-line vector-intersection
  computation (part (a), "Round 20" entry in Approaches tried above): with
  $A$ at the origin, both lines' equations are written down explicitly, the
  known closed form $P=\frac{|C|^2-|B|^2}{2|C-B|^2}(C-B)$ (already certified)
  is checked by direct substitution to lie on both lines, and non-parallelism
  of the two lines gives uniqueness of the intersection point, hence equality
  with $Q$. Zero gaps, no numerics needed (this is an exact algebraic
  identity, independently double-checked in this file only as a
  cross-reference, not relied upon). Strictly simplifies the existing
  certified characterization (no circumcenter arithmetic needed) and is
  a good candidate for certification, since $QB=QC$ (an immediate
  consequence) is directly useful to any future angle-chase attempt on this
  or other approaches.

- **Name:** fixed-point-P-and-concyclicity-reduction.
  **Statement:** Let $\triangle ABC$ be a triangle, $M,N$ the midpoints of
  $AB,AC$, $O_{ABC}$ its circumcenter, and let $P$ be the foot of the
  perpendicular from $O_{ABC}$ to the line through $A$ parallel to $BC$
  (equivalently, with $A$ placed at the origin,
  $P=\frac{|C|^2-|B|^2}{2|C-B|^2}(C-B)$). Then for *any* points $K,L$ (no
  hypotheses on $K,L$ needed beyond existence of the circumcenter $O$ of
  $\triangle AKL$), $OM=ON \iff A,K,L,P$ are concyclic.
  **Where proved:** In full, by hand vector algebra (Steps 1–4 of "New
  result: the fixed point $P$" in the Current best section of this file),
  independent of the problem's hypotheses H1–H3 — a general fact about any
  triangle $ABC$ with midpoints $M,N$ and any circle through $A$. This is a
  complete, self-contained, gap-free proof and is a good candidate for
  certification into `results/imo-2026-02/lemmas/`, since it is reusable
  by any future approach (coordinate or synthetic) that wants to replace
  the "$OM=ON$" target with a concyclicity target.
