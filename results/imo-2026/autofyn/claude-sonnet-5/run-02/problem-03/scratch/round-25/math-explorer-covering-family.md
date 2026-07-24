## imo-2026-03 — lens: lp-duality-certificate's case (b2) upper bound, turning the round-24 20-member covering family into a genuine coverage proof

### Setup / parameter count (answers task item 1)

At $n=3$, case (b2)'s box lives on $p=(p_1,p_2,p_3,p_4)$ with $p_1\ge p_2\ge
p_3\ge p_4>0$. Everything in this problem (both $\Phi$-values and
feasibility walls) is **homogeneous of degree 1** in $p$, so WLOG normalize
$T=p_1+p_2+p_3+p_4=1$. This leaves exactly **3 free continuous parameters**
(say $p_1,p_2,p_3$, with $p_4=1-p_1-p_2-p_3$ determined), subject to:
- the sort order $p_1\ge p_2\ge p_3\ge p_4>0$ (3 linear inequalities + positivity),
- case (b2)'s box: $p_1<1/2$, $1/15<p_2<4/15$ (3 more linear inequalities).

So case (b2)'s box is a **bounded convex polytope in $\mathbb R^3$** (a
"3-dimensional" case split), not a higher-dimensional or curved region.
This is genuinely low enough for exhaustive symbolic/computational
case-splitting to be tractable — see below.

### Crucially: this is a *linear*, not a curved/CAD, problem (answers task item 2)

Every one of the 20 chambers' formulas $\Phi_\tau(p)$ on file (Bisect-Subset,
Double-Sandwich-Below/Above, Triple-Pin, Chamber A/A2/B1/B2, R22.1.1,
P1P2-tied-to-$p_3$) is an **affine** function of $(p_1,p_2,p_3,p_4)$, and
every feasibility wall on file is a **linear** inequality in $p$ (e.g.
$p_1<p_2+p_3$, $p_1\ge 2p_3$, $p_2\le p_3+p_4$, $p_2\ge 2p_3$, etc. — no
products, no square roots, nothing polynomial of degree $\ge2$ appears
anywhere in the chamber definitions). So the "covering family fully covers
the box" question is a **pure linear/polyhedral covering problem**: does
the union of $\le20$ convex polyhedra $R_\tau:=\mathrm{Feas}_\tau\cap\{g_\tau
\ge0\}$ (each cut out by finitely many half-spaces, since $g_\tau=a_3T-\Phi_\tau$
is itself affine) cover the box polytope? This is **strictly easier than
general CAD** — no algebraic-number/root-isolation machinery is needed, only
linear algebra + LP. The rigorous route is: form the hyperplane arrangement
of (a) the box's own $\sim7$ boundary hyperplanes, (b) each chamber's feasibility-wall
hyperplanes, (c) each chamber's success-boundary hyperplane $g_\tau=0$; this
arrangement partitions the box into finitely many convex cells on which every
predicate (feasible/infeasible, $g_\tau\ge0$/$<0$) is constant; checking one
representative point per cell (via LP, exact rationals) certifies the whole
cell. With the full 20-chamber family this could run to $\sim30$–$40$
hyperplanes (worst-case $O(h^3)$ cells, tens of thousands) — heavy but not
absurd for a dedicated computational round. **However §"Redundancy" below
shows this full-scale arrangement is very likely unnecessary.**

### Redundancy: a 5-chamber sub-family appears to already suffice (answers task item 3 — the most important finding this round)

I ran a greedy set-cover probe (Python, `/tmp/round-25/probe_greedy2.py`) on
$\sim3500$ random box points and found that a tiny sub-family already
achieves zero uncovered points:
$$\{\text{Bisect}\{1,4\},\ \text{Bisect}\{1,2\},\ \text{DS-Above},\
\text{Triple-Pin},\ \text{R22.1.1}\}.$$
I then **stress-tested this 5-chamber family alone** with $10^6$ fresh random
trials (`/tmp/round-25/probe_test5.py`): **zero uncovered points.** (An
initial cruder 4-chamber greedy family, dropping Triple-Pin, *does* fail —
found 11/200000 violations — so Triple-Pin is load-bearing; this is a useful
negative data point too.)

I then went further and **attempted an exact LP-based proof, not just
sampling**, for this 5-chamber family (`/tmp/round-25/lp_check5b.py`):
the "bad" region (all 5 chambers simultaneously fail) splits into exactly
6 branches by case-splitting on (a) whether $p_1>p_2+p_3$ (the shared
feasibility wall of DS-Above/Triple-Pin) and (b) which of R22.1.1's two
feasibility inequalities fails (or both hold and its own $g<0$). Each branch
is a single LP feasibility query in 3 free variables. **Result: at any
genuine open-box margin $\varepsilon\ge10^{-7}$ from the box's boundary, all
6 branches are LP-infeasible** — i.e. the bad region is empty in the box's
interior away from its own walls. At $\varepsilon\to0$ exactly, I found (and
verified by hand with exact `Fraction` arithmetic,
`/tmp/round-25/exact_vertex_check.py`) a **single degenerate vertex**
$$p=(p_1,p_2,p_3,p_4)=\Big(\tfrac25,\ \tfrac4{15},\ \tfrac15,\
\tfrac2{15}\Big)$$
where $g_{\text{Bisect}\{1,4\}}=g_{\text{Bisect}\{1,2\}}=g_{\text{R22.1.1}}=0$
**simultaneously** (a genuine triple tie), while DS-Above/Triple-Pin are
infeasible there ($p_1<p_2+p_3$ exactly fails to hold at this point... check
sign: $p_1=2/5$, $p_2+p_3=7/15>2/5$, so indeed infeasible). This point lies
**exactly on the box's own boundary wall** $p_2=4/15$ (which the box excludes
by strict inequality), so it is not itself a counterexample — but it is the
limiting worst case, and (per the already-certified
`p-space-chamber-vertex-theorem` item 3 boundary-sharing corollary cited
repeatedly in the approach file) points exactly on the box's own walls are
already handled by separate, previously-closed machinery (Theorem C$'$/
Theorem B at $n\le3$, `unconditional-p2-threshold-closure`).

**This is a strong, concrete, and highly promising finding for the next
round**: instead of an intractable 20-chamber, ~30–40-hyperplane arrangement,
the *actual* covering-family target may collapse to as few as **5 chambers**
with a **6-branch case split**, each branch a linear-inequality system in 3
variables that a careful hand (or `sympy`/exact-Fraction LP) argument can
almost certainly close outright — this is a dramatically smaller and more
tractable target than round 24 left it. I did **not** complete a rigorous
proof (this is exploration, not proof-outlining) — the LP infeasibility
findings above are floating-point `scipy.optimize.linprog` results with a
numerical margin, corroborating but not yet a certified exact-arithmetic
proof; the next round should redo the 6-branch check in exact `Fraction`/
`sympy.Rational` LP (or by hand, since 3-variable LPs are humanly
checkable) and handle the boundary vertex found above by explicitly
invoking the box-wall machinery. **Caveat**: I only searched greedily on
random samples for the minimal family; it is possible a slightly different
5–8 chamber combination is needed once boundary cases are treated exactly —
treat the specific 5-chamber list above as a strong lead, not a certified
final answer.

### Cheap-kill / structural notes

- The homogeneity-degree-1 normalization ($T=1$) that collapses the problem
  to 3 free parameters is itself a "cheap" structural simplification worth
  stating explicitly in the outline — it seems to already be used implicitly
  throughout the approach file's derivations but should be named as the
  reason the covering-family target is tractable at all.
- The Bisect-Subset family (`bisect-subset-lemma`, certified) is
  **unconditionally feasible everywhere** — no feasibility wall at all, only
  a success-boundary hyperplane $g_S=0$. This is why 2 of the 5
  survivor-chambers (Bisect$\{1,4\}$, Bisect$\{1,2\}$) contribute no
  feasibility branching at all — a real simplification of the arrangement.
- Every "hard" vertex found this round (like the boundary triple-tie above)
  and every hard vertex found in round 24 (§R24.5) sits either exactly on a
  box wall (already separately closed) or is resolved by a different
  chamber — this is a recurring pattern worth the outliner exploiting
  directly: a proof strategy of "case-split on box walls first (already
  closed), then show the 5–6 chamber family suffices strictly inside" may
  be the cleanest route.

### Knowledge-base entries

No entry in `knowledge_base.md` addresses polyhedral/LP covering-family
proofs or CAD directly — the relevant "Casework/exhaustion" generic entry
(General Proof Methods section) is the only on-point generic guidance
("split into finitely many cases... keep cases disjoint and exhaustive").
The actual applicable machinery here is standard LP duality/Farkas-style
infeasibility certificates, which the approach's own name
(`lp-duality-certificate`) already signals but which the project has so far
used only for per-chamber $\Phi$ derivations, not yet for the covering
step itself — this round's LP-branch check is the first time an LP
infeasibility certificate was aimed at the *covering* claim itself rather
than at a single chamber's value.

### Crux corpus

Searched `combinatorics`/`algebra` domains, subtopics `extremal-principle`
and `inequalities-SOS-and-convexity`, filtering for cruxes mentioning
piecewise/vertex/polytope/case/linear-program/covering/affine language.
Found ~77 candidates; none are a genuine structural analogue of "cover a
bounded polytope by finitely many affine-inequality regions via LP
branch-and-bound" — the closest in flavor (`aimo-0048`'s "index the domain
by a rectangle and bound in each cell" and `aimo-0146`'s smoothing/re-imposition
pattern) are case-exhaustion-flavored but solve different problems (integer
functional inequalities, graph degree sequences) with no reusable geometric
technique. **Conclusion: no directly analogous crux found**; this is a
genuinely bespoke computational-geometry sub-target, not one with a known
crux template to borrow.

### Prior progress / dead ends

- Prior progress: the 20-member covering family (round 24, this file) with
  zero uncovered points on 1577+3351 exact-`Fraction` sampled points — sampling
  evidence only, explicitly not a proof (per the approach file's own honest
  scoping, confirmed by the reviewer).
- Round 24's own §R24.6 partial attempt (Triple-Pin + DS-Above margin-sum
  bound, sufficient only when $p_4\le 2T/15$) is **not** superseded by this
  round's finding — it's a different sub-claim (about the $p_1>p_2+p_3$
  region specifically) and remains a valid, narrower, already-proved
  fragment; the 5-chamber LP-branch finding above is a more promising
  full-target route but is not yet a proof.
- No dead end to report this round — the redundancy findings are new,
  positive information, not a refutation of anything on file.

### Small-case / intuition notes (all labeled conjecture/numeric)

- **Conjecture (strong numeric support, $10^6$ trials + exact-vertex check):**
  the 5-chamber family {Bisect$\{1,4\}$, Bisect$\{1,2\}$, DS-Above,
  Triple-Pin, R22.1.1} covers case (b2)'s open box at $n=3$ with zero
  failures away from the box's own boundary walls, and the sole
  boundary-limit failure point is the exact vertex $p=(2/5,4/15,1/5,2/15)$,
  which is excluded by the box's strict $p_2<4/15$ inequality and is
  independently already covered by boundary-wall machinery.
- This suggests the true "hard part" of case (b2) is concentrated almost
  entirely on/near the box's own boundary (already largely closed by other
  certified theorems), with the box's interior being comparatively easy —
  consistent with round 24's own §R24.5 observation that every chamber's
  own individual failure vertex sits on a box wall or is rescued elsewhere.
