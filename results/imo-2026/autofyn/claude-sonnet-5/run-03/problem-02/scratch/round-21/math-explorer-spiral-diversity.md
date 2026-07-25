## imo-2026-02 (lens: inversion / new synthetic bridge for spiral-similarity-bootstrap)

### Setup used for all numerics
Built a robust from-scratch numeric solver for genuine H1-H3 instances (the
prior round's fsolve attempt failed to converge; fixed here). Method: fix
triangle $A,B,C$, parametrize $K=B+t_K\,d_K(\varphi)$, $L=C+t_L\,d_L(\varphi)$
where $d_K,d_L$ are unit directions making angle $\varphi$ with $BA$, $CA$
respectively (this encodes H1, $\angle KBA=\angle ACL=\varphi$, by
construction), then solve the 2x2 system H2 ($\angle LBK=\angle LNC$), H3
($\angle LCK=\angle BMK$) for $(t_K,t_L)$ via grid-search + `scipy.optimize.
least_squares` (residuals driven to $<10^{-7}$, typically $10^{-11}$–$10^{-14}$
after refinement). Verified containment (K inside $\triangle BMC$ inside
$\angle LBA$; L inside $\triangle BNC$ inside $\angle ACK$). On triangle
$A=(0.3,1.1),B=(-1,0),C=(1.3,-0.1)$ this found 11 genuine solutions across
$\varphi\in[0.1,0.6]$ (all with $\mathrm{sign}=-1$ branch), and reconfirmed
$OM=ON$ to $\sim10^{-8}$ or better on each, and $A,K,L,Q$ concyclic to
$\sim10^{-9}$–$10^{-16}$ on each (both already-certified facts, used as a
correctness check on the solver — passed).

### (1)+(2) Inversion centered at A, and centered at Q: negative
Inverted $K,L,Q$ (and $B,C,M,N$) at center $A$ with radius$^2=1$. Confirmed
(as expected, since $A,K,L,Q$ are concyclic through $A$) that $K^*,L^*,Q^*$
are exactly collinear (cross product $\sim10^{-9}$–$10^{-14}$) — this is not
new information, just a restatement of the concyclicity already proved.
Checked whether the image line $K^*L^*Q^*$ is parallel to $BC$: **no**
(cross product of direction vectors $\approx0.17$–$0.25$, clearly nonzero and
drifting with $\varphi$). Checked whether $K^*$ lies on line $M^*N^*$: **no**
(cross $\approx0.13$–$0.29$, drifting). So inversion at $A$ does not send the
target line to any of the other natural fixed lines in the configuration —
no clean picture found.

Inverted at $Q$ instead: as expected $A^*,K^*,L^*$ are collinear (circle
$AKLQ$ passes through the center $Q$). Checked if this image line is
parallel to $BC$: **no** (cross $\approx1.5$–$1.7$, large and drifting).
Checked if $B^*$ or $C^*$ lies on it: **no** (distances $\approx0.29$–$0.39$,
not shrinking, no sign of coincidence). So inversion at $Q$ also gives no
recognizable simplification with the tools/points available.

### (3) Wider point-assignment sweep for the general lemma vs H1: essentially exhausted, negative
Worked out explicitly which assignments $(P,Q',X,Y,Z)$ can even *literally*
encode H1 ($\angle(BK,BA)=\angle(CA,CL)$) in the lemma's required form
$\angle(PX,PY)=\angle(QX,QZ)$ (note: the lemma needs the **same** point $X$
to appear as the second point of both $P$'s and $Q'$'s expressions). Since
H1's two clauses share only the point $A$ (as $BA$ on the left, $CA$ on the
right), the *only* literal encoding (up to the trivial swap that negates
both sides) is $P=B,Q'=C,X=A,Y=K,Z=L$ — exactly the assignment already
tried and refuted (drifts by $2\varphi$, per current.md). Every other
assignment considered (and the two more tried in round 20,
$(B,C,K,A,L)$ and $(K,L,B,A,C)$) requires silently changing what H1 says
(e.g. forcing $CA=CK$ as lines), so they are not valid encodings of the
actual hypothesis. **Conclusion: the general lemma applied to H1 alone has
no further content beyond the one assignment already on record as refuted.**
Any real progress on H1 needs either both hypotheses combined differently
(as the existing Corollary already does) or a different lemma shape
entirely — not more relabelings of this one lemma against H1 in isolation.

Also tried the lemma against H2/H3 using $Q$'s two known facts ($QB=QC$,
$AQ\parallel BC$) as auxiliary hypotheses, to see if a shared point could be
engineered. Confirmed numerically and by direct computation the clean fact
$$\angle(AQ,AB) = \angle B \pmod\pi$$
(measured: $0.74571$ vs $\angle B=-0.74571$ i.e. equal in magnitude, sign
consistent with the directed-angle convention) — this **is** new,
usable content (a fixed, explicit direction for line $AQ$ relative to $AB$,
not previously stated this precisely in current.md, though it follows
immediately from $AQ\parallel BC$ + alternate angles — a one-line fact).
However, no combination of this with Lemma A/B (which pin angles *at* $K,L$
against $BK,AC,CL,AB$) into a valid application of the general lemma that
produces a $Q$-involving equality was found in the time available — flagging
this as a concrete, well-defined next thing to try (see below), not
completed.

### (4) Wider circle-membership sweep for Q: all negative, cleanly ruled out numerically
Systematically tested (numeric, 6-11 sample $\varphi$ values per test,
residual $|{\rm dist}(Q,\text{circle})|$ reported):
- circle$(B,K,C)$ through $Q$: **no** (residual $0.6$–$0.9$, growing with $\varphi$).
- circle$(B,L,C)$ through $Q$: **no** (residual $0.55$–$0.82$).
- circle$(K,L,B)$, circle$(K,L,C)$ through $Q$: **no** (residual $0.6$–$0.9$).
- circle$(K,L,M)$, circle$(K,L,N)$ through $Q$: **no** (residual $0.22$–$0.32$,
  smaller but clearly nonzero and drifting — not a coincidence).
- circle$(B,N,K)$, circle$(C,M,L)$ through $Q$: **no** (residual $0.5$–$0.55$).
- circle$(B,N,L)$, circle$(C,M,K)$ through $Q$: **no**, but noticeably
  *smaller* residual than most others ($0.04$–$0.26$, growing with
  $\varphi$) — still clearly nonzero and drifting, not a hidden identity,
  but flagged since it's the closest near-miss found.
- **Lemma A/B's own circles**, $(B,L,N)$ and $(C,K,M)$, through $Q$:
  **no** (residual $0.04$–$0.30$ for $(B,L,N)$, $0.10$–$0.30$ for
  $(C,K,M)$, both growing with $\varphi$ — the most natural candidate circles
  given the population's existing lemmas, cleanly ruled out).
- circumcircle of $ABC$ through $Q$: **no**, but with a striking
  **constant** residual $4.34\times10^{-3}$ across every $\varphi$ tested
  (makes sense — $Q$'s distance-from-circumcircle-power doesn't depend on
  $K,L$ at all, it's a fixed fact about $Q,A,B,C$ alone; not useful for
  bridging to $K,L$).
- Power of $Q$ w.r.t. circle$(BLN)$ vs. circle$(CKM)$ (radical-axis test,
  i.e. is $Q$ on the radical axis of Lemma A/B's two circles?): **no**,
  powers differ by $-0.10$ to $-0.07$, shrinking slowly but clearly nonzero
  and not extrapolating to $0$ in the tested range.
- Line $BQ$ through $K$? Line $CQ$ through $L$? **no** (distances
  $0.10$–$0.18$ and $0.03$–$0.12$ respectively, both growing with
  $\varphi$, not vanishing).
- Spiral similarity at $Q$ sending $B\mapsto C$: does it (approximately) send
  $K\mapsto L$? Checked ratio $QL/QK$ vs. $QC/QB\,(=1$ since $QB=QC)$ and
  angle $\angle KQL$ vs $\angle BQC$: **no**, $QL/QK$ drifts
  $1.074\to1.054$ (not $\equiv1$), $\angle KQL$ drifts $1.42\to1.32$
  rad while $\angle BQC=1.567$ rad is fixed — not a spiral similarity center
  for $(B,K)\to(C,L)$.

None of the ~15 circle/line/similarity candidates tested gave a clean
(constant-zero, or extrapolating-to-zero) residual. This strengthens the
existing diagnosis in current.md ("no certified relation ties $Q$ to $K$ or
$L$") to: no *simple* natural circle/line/similarity construction involving
$Q$ and any 2-3 of $\{B,C,K,L,M,N\}$ found by this sweep works either — the
needed bridge, if it exists via one of these primitive constructions, is not
among the ones tried here.

### Distinct openings
- **Opening 1 (negative, rules out a whole family):** inversion at $A$ or at
  $Q$ does not obviously simplify — confirmed numerically, don't spend
  further rounds trying "does inversion make it a line/circle with
  recognizable center" without a much more specific target line/circle in
  mind first.
- **Opening 2 (the one concretely promising unexplored thread):** the fact
  $\angle(AQ,AB)=\angle B\pmod\pi$ (equivalently $\angle(AQ,AC)=-\angle C$)
  is clean, provable in one line from $AQ\parallel BC$, and is new relative
  to what's in current.md (which states $AQ\parallel BC$ but not this
  angle-at-$A$ consequence explicitly). This gives $AQ$'s direction in terms
  of the *base angles* $B,C$ — the same currency Lemma A/B and the Corollary
  already use ($\angle BLN=\angle(BK,AC)$, $\angle CKM=\angle(CL,AB)$, and
  the $\varphi$-elimination). A concyclicity proof via
  $\angle(AK,AL)=\angle(QK,QL)\pmod\pi$ (an equivalent restatement of
  "A,K,L,Q concyclic" using the inscribed-angle criterion from a different
  pair of vertices than the file's $(\ast)$) might be more tractable than
  $(\ast)$ itself, since it only needs the angle *at $A$* between $AK,AL$ —
  and $AQ$'s fixed direction is now pinned relative to $AB,AC$. This was not
  attempted numerically or synthetically this round (ran out of scope/time
  budget for this lens) — flagged as the most promising concrete next step.
- **Opening 3 (near-miss worth one more careful look):** circle$(B,N,L)$
  and circle$(C,M,K)$ had the smallest (though still clearly nonzero and
  growing) residual to $Q$ among all circles tested — these already appear
  refuted per current.md's "5 prior guesses" list, so this is *not* a new
  lead, just confirms that refutation independently with the new solver.

### Candidate technique(s)
Directed-angle chase using the inscribed-angle criterion at $A$ (not $K,L$)
combined with the new $\angle(AQ,AB)=\angle B$ fact (Opening 2); no
inversion-based simplification found.

### Cheap-kill candidates
None beyond what's already been ruled out this round (the ~15 circle/line
tests above are the cheap kills for this route; all done).

### Knowledge-base entries to use
Directed-angle / spiral-similarity general lemma (already in use in the
approach file); inscribed-angle / concyclic-criterion entries in
`knowledge_base.md` (same family already cited by the approach for
criterion $(\ast)$) — the same entries apply to the alternative
$\angle(AK,AL)=\angle(QK,QL)$ restatement in Opening 2.

### Analogous past problems (cruxes)
Did not run a fresh corpus query this round (lens was numeric/computational,
per dispatch); the approach file and prior rounds' explorers have already
surveyed the corpus for this problem (see current.md's history) — no new
crux search performed here. If needed next round, filter
`crux_moves_documentation.md` corpus by `domain=geometry`,
`subtopic` matching "concyclic points" / "spiral similarity" / "fixed
point under inversion" and look specifically for a "fixed point lies on
circle through two moving points determined by an angle condition" pattern,
which is the real shape of this problem's residual gap.

### Prior progress
As recorded in current.md / spiral-similarity-bootstrap.md: problem fully
reduced (unconditional vector-algebra proof, certified) to proving
$A,K,L,Q$ concyclic, $Q=(\text{line through }A\parallel BC)\cap
(\text{perp. bisector of }BC)$ — certified lemmas
`q-as-two-line-intersection.md`, `q-as-foot-of-perpendicular-from-
circumcenter.md`, `amnq-concyclic-and-reduction.md`,
`vector-reduction-OM-ON.md`. Lemma A ($\angle BLN=\angle(BK,AC)$), Lemma B
($\angle CKM=\angle(CL,AB)$), and the Corollary
($\angle BLN+\angle CKM\equiv0\pmod\pi$) are all proved and certified-grade
(hand-derived, not just numeric).

### Dead ends (do not retry)
- Naive spiral similarity at $A$ sending $B\mapsto C,K\mapsto L$: refuted
  (unequal ratios/angles at a genuine instance).
- Full triangle similarities $\triangle LBK\sim\triangle LNC$,
  $\triangle KCL\sim\triangle KMB$ from single hypotheses alone: refuted.
- $O$ = a fixed point (circumcenter/nine-point center of $ABC$): refuted, $O$
  moves along a line.
- 5 prior concyclicity guesses (B,N,Q,L; C,M,Q,K; B,N,L,K; circle(BMC)
  through Q; nine-point circle through Q): refuted in earlier rounds;
  **independently reconfirmed this round** for $(B,N,L,Q)$ and $(C,M,K,Q)$
  specifically (residuals $0.04$–$0.30$, clearly nonzero, growing with
  $\varphi$).
- New this round, also refuted: circle$(B,K,C,Q)$, circle$(B,L,C,Q)$,
  circle$(K,L,B,Q)$, circle$(K,L,C,Q)$, circle$(K,L,M,Q)$, circle$(K,L,N,Q)$,
  circle$(B,N,K,Q)$, circle$(C,M,L,Q)$, circle$(B,L,N,Q)$, circle$(C,K,M,Q)$
  (Lemma A/B's own circles), radical axis of circle$(BLN)$/circle$(CKM)$,
  line $BQ$ through $K$, line $CQ$ through $L$, spiral similarity at $Q$
  sending $B\mapsto C,K\mapsto L$. Inversion centered at $A$ (image line
  $K^*L^*Q^*$ not parallel to $BC$, not through $M^*N^*$) and centered at
  $Q$ (image line $A^*K^*L^*$ not parallel to $BC$, not through $B^*/C^*$):
  both refuted as simplification mechanisms.
- Systematic point-assignment sweep of the general lemma vs H1 alone: now
  **exhausted, not just incomplete** — shown analytically that the lemma's
  required shared-point structure forces the assignment to be (up to a
  trivial sign swap) exactly the one already tried and refuted; no further
  relabeling can encode H1 correctly. (This corrects current.md's Open gap
  4, which described this sweep as merely "incomplete" — it is now known to
  be complete and exhausted for H1 in isolation.)

### Small-case / intuition notes
All conjectural / numeric-only (not proofs): (i) $A,K,L,Q$ concyclic
reconfirmed to $10^{-9}$–$10^{-16}$ on 11 fresh solutions of the actual
H1-H3 system (a working solver, since the previous round's did not
converge); (ii) $\angle(AQ,AB)=\angle B$ exactly matches to 5+ decimals
(this one is provable exactly from $AQ\parallel BC$, not merely numeric —
worth writing up as a one-line certified fact next round); (iii) no natural
circle/line/spiral-similarity construction tried this round involving $Q$
and $K$ or $L$ shows even approximate (let alone exact) coincidence — the
residuals for all ~15 candidates grow (not shrink) as $\varphi$ moves away
from the tested range's low end, consistent with genuine non-coincidence
rather than a numerical-precision artifact.
