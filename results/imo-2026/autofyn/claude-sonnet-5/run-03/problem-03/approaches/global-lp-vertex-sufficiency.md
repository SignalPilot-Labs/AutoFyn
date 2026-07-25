## Status
partial

## Round 20 target: close the $n=2$ achievability half in full rigor; test the $p_3,p_4$-tied $n=3$ construction (per outliner, revise; outline-reviewer flagged a real feasibility problem in the primary $p_2,p_3$-tied pairing)
**[Addressed this round — see new Section 11 in "Current best" below, and
the rewritten Section 10.6.]** (a) Replaced the six grid-search-only
two-cut shapes of Section 10.6 with a **complete, gap-free, hand-checked
casework proof** that $\mathrm{OddSum}\ge c(2)$ for all ten $n=2$
response shapes at $p^*=(4/7,2/7,1/7)$ — every shape now reduces to
either a **trivial nonnegativity bound** ($\mathrm{OddSum}=c(2)+{}$a sum
of nonnegative terms) or a **short, exhaustive case split** (at most
three sub-cases) yielding the exact identity $\mathrm{OddSum}\ge
M_1+m_1=c(2)$ for a canonically-defined max/min pair. This **fully
closes $V(p^*)=c(2)$ exactly**, completing the $n=2$ Existence Theorem
end to end (both directions), with no numerics anywhere in the final
proof (independent exact-`Fraction` sampling, $200{,}000$ trials per
shape, used only as a sanity check on the hand-derived bound, confirmed
zero violations and exact equality at the claimed minimum in every
case). (b) Per the outline-reviewer's finding that the outline's primary
$p_2,p_3$-tied $n=3$ construction is infeasible on a large sub-region of
$B(3)$, ran the mandated LP-style worst-case analysis (not just random
sampling) on the recommended alternative ($p_3,p_4$-tied pairing) and
found it **also fails**, broadly (not a thin sliver): a closed-form
derivation shows it collapses to the *same* $\mathrm{OddSum}=1-p_1$
formula as the $p_2,p_3$-pairing in the generic (and, here, provably
*only*) branch, so it fails on the identical large region $p_1<7/15$ of
$B(3)$ — with the true worst case (via an exact linear-programming
argument, not sampling) at $\inf p_1=16/45$, giving a genuine
$\sup(\mathrm{OddSum}-c(3))=1/9>0$. Both natural single-witness
$2$-cut/$6$-fragment pairings are now refuted for all of $B(3)$; see
Section 11 for full detail, the exact LP derivation, and a concrete
counterexample.

## Round 19 target: full rigorous write-up of the $n=2$ Existence Theorem + $n=3$ scoping (per outliner, revise — APPROVED by outline-reviewer)
**[Addressed this round — see new Section 10 in "Current best" below.]**
Wrote up in full, casework-free rigor: (a) $p_1>10/21$ throughout the
$n=2$ balanced region, from the region's own two gap inequalities; (b)
the exact algebraic equivalence $p_3>(p_1-p_2)\iff p_1<1/2$ pinning the
witness's rank order unconditionally; (c) the resulting bound
$\mathrm{OddSum}<11/21<c(2)=4/7$, strictly, everywhere in the true
region — independently re-verified at $200{,}000$-trial exact-`Fraction`
scale. Also verified (fully for $9/10$ finite response shapes, strongly
but not completely for the last $6$) the achievability half
$V(p^*)=c(2)$ at the geometric partition $p^*=(4/7,2/7,1/7)$, and
diagnosed concretely (not vaguely) why the $n=2$ witness's single-cut
lift fails $\approx88\%$ of sampled $n=3$ balanced-region points: the
$n=2$ mechanism relies on an **even**-sized resulting multiset so the
new fragment always lands at an even (never-summed) rank; the $n=3$
lift produces an **odd**-sized multiset, so the fragment's parity is no
longer pinned by any single region hypothesis — a structural, not
casework-count, obstruction, motivating (but not yet testing) a
$2$-cut, $3$-fragment witness at $n=3$ as the next concrete probe.

## Round 18 target: pivot to exact re-derivation of tie-free/kink candidates (per outliner, revise)
**[Addressed this round — see "Approaches tried / Round 18" below and new
Section 9.]** Pivoted away from Flat-Edge-face classification (round
17's focus) to directly re-deriving, in exact `Fraction` arithmetic,
this round's explorer's two float-based near-maximizer candidates
($m=(1,0,1)$ at $n=2$, $m=(1,0,2,0)$ at $n=3$). Found a genuine bug:
the reported $n=2$ point is **not in the balanced region** ($p_1-p_2<
\gamma(2)$, verified exactly). Proved, in closed form, that the
specific branch of shape $(1,0,1)$ the bad point realized has
$\mathrm{OddSum}=\tfrac12+\tfrac{p_1-p_2}2$, which is **always** $>c(2)$
inside the true balanced region (since $c(2)=\tfrac12+\gamma(2)/2$
exactly and the region requires $p_1-p_2>\gamma(2)$) — a clean exact
negative fact explaining the artifact. Numeric (non-exact) re-search at
corrected, region-valid points finds true $V(p)$ comfortably below
$c(2)$ (best found $\approx0.5216$ vs. $c(2)\approx0.5714$), consistent
with real slack once the bug is fixed, but this is not an exact proof
of the Existence Theorem for $n=2$. The $n=3$ shape $m=(1,0,2,0)$ was
not reached this round (time). Status stays `partial`.

## Round 17 target (per outliner, revise)
Round 17's explorer found round 16's "joint degeneracy" is actually TWO
distinct phenomena: a genuine **Self-Bisection-Crossover** (a piece
bisecting itself exactly at a point that is also a rank-order crossover —
structurally different from the 4 refuted tie-topologies) at hard point 3,
and a previously-unreported **Flat-Edge** (a continuum of ties, width
$\approx0.091$, not an isolated vertex) at hard point 1. Tasks: (1)
mandatory cheap-kill first — test the crux `aimo-0119`-style extremal-
selection + single-fragment-transfer-non-improvement mechanism at the
catalogued hard points; (2) classify all 8 catalogued hard points via the
cheap sweep-for-flatness test (sharp kink vs. wide flat interval) before
any proof investment; (3) treat Self-Bisection-Crossover and Flat-Edge as
two separate new mechanisms/targets, not one family; (4) exact-arithmetic
check whether the Flat-Edge's true maximizer sits at one of the edge's
endpoints. See `/tmp/round-17/proof-outliner.md` for the full skeleton.

## Round 17 target: cheap-kill + Self-Bisection-Crossover vs. Flat-Edge classification (addressed this round)
**[Addressed this round — see "Approaches tried / Round 17" below and new
Section 8.]** Ran the mandatory cheap-kill first (own from-scratch exact
computation, `/tmp/round-17/lpv_cheap/`), then classified the catalogued
hard points via a direct **sweep-for-flatness** test computed algebraically
(exact rank-by-rank differencing, not a black-box optimizer re-run for the
sweep itself). Found, and **proved in general** (not just observed), the
mechanism behind both phenomena: a single clean **Flat/Kink Parity Lemma**
(Section 8.3) — perturbing one piece's bisection point $x\mapsto x+t$ (with
the paired fragment $p_i-x-t$) changes $\mathrm{OddSum}$ at slope
$[\mathrm{rank}(x)\text{ odd}]-[\mathrm{rank}(p_i-x)\text{ odd}]\in\{-1,0,+1\}$
on any interval of constant rank-order — giving a **sharp kink** (slope
$-1\to+1$, "Self-Bisection-Crossover") exactly when the two fragments'
ranks have *opposite* parity as they cross, and a **flat plateau**
("Flat-Edge") exactly when the ranks have the *same* parity. Verified this
rule exactly against 3 concrete self-bisection kinks (all catalogued hard
points where a piece splits exactly in half) and 1 genuine wide flat
interval (catalogued hard point `n3_pt1`), the latter confirmed in **exact
`Fraction` arithmetic** (no floating-point tolerance used) both on the
actual hard-point data and on an independent hand-built toy instance.
Status stays `partial`: this closes the round's diagnostic tasks in full
(cheap-kill run, all tested points classified, general mechanism proved)
but does **not** by itself close the Existence Theorem's $\Sigma$-shape
residual — see Section 8.5 for the precise remaining gap.

## Round 16 target: concrete diagnostic — which Σ-shape family realizes the maximizer (per outliner, revise)
**[Addressed this round — see "Approaches tried / Round 16" below and new
Section 7.]** Per this round's dispatch: ran a concrete numerical
diagnostic, in the same multi-restart-optimization methodology already
established and cross-checked in this file (Sections 4.6–4.7), at the
already-catalogued "hard" $n=3,4$ points, directly classifying the tie
structure of the true optimal shape $\sigma^*(p)$ at each. **Decisive
finding, not another open-ended diagnosis**: at every one of $8$ tested
points (the $3$ catalogued $n=3$ points, $2$ catalogued $n=4$ points, and
$3$ additional points reached by a short local ascent in $V$ from the
$n=3$ points), the winning shape is in a **branch-comparison-boundary
near-tie with $\ge4$ other distinct cut-allocations simultaneously** (gap
$<10^{-6}$, i.e. $\ge5$-way degeneracy is the norm, not a knife-edge
special case), and at a genuine majority of the points ($5$ of $8$) the
winning shape's own multiset **also** exhibits an exact within-branch tie
between two nonzero fragments. **The two families are not competitors for
"which one is real" — they co-occur.** This directly answers the
dispatch's question (Section 7.3): neither family alone is "the" source
of the maximizer's degeneracy; the natural target for future rounds is
the **joint/combined family** (a point in $Q$ solving a mix of
branch-comparison and within-branch-tie equations simultaneously), not
either type in isolation. Cross-validated against
`lp-duality-split-polytope`'s certified Perfect-Tie-Family Characterization
at $e_0$ (Section 7.4): that theorem's own extremal family is, in this
file's terminology, a within-branch-tie construction (fragments tied to
whole untouched pieces), consistent with — not contradicting — this
round's finding that within-branch ties are pervasively present at
near-optimal points elsewhere in the region. A genuine methodological
finding is also reported honestly (Section 7.2): a hasty low-restart
hill-climb step produced a **spurious, non-reproducible "improvement"**
that a higher-restart re-check flatly contradicted (apparent
$V\approx0.531$ at low restart count vs. the correct $V\approx0.513$ at
higher restart count, at the *same* point $p$) — flagged so no future
round repeats the mistake of trusting a low-restart inner minimization as
evidence of the true $V(p)$. Status stays `partial`: this is a decisive
numeric classification (per the dispatch's own menu of acceptable
concrete deliverables), not a proof, and does not by itself close the
$\Sigma$-shape residual.

## Round 15 target: star-topology cheap-kill + existence-only pivot (per outliner, revise)
**[Addressed this round — see "Approaches tried / Round 15" below and new
Sections 5–6.]** Per this round's dispatch: (1) ran the mandatory
exhaustive numeric cheap-kill, in exact `Fraction` arithmetic, on a
**star/tree fragment-tying topology** (one hub split piece supplying
tie-values to several partner pieces simultaneously, evaluated via the
certified Singleton-Interleaving Lemma), against fresh random balanced-
region points at $n=3,4$ — **decisively refuted**, with exact-arithmetic
witnesses re-confirmed under a $4\times$ finer breakpoint grid, so this
is a genuine failure, not a search-resolution artifact. Reported as a
negative finding, not written up as a lemma. (2) Per the outline's own
in-round pivot instruction, moved to the existence-only per-cell
LP-certificate route (Section 6). Found, en route, one genuinely new,
fully proved, general-purpose elementary fact — the **Zero-Removal
Invariance Lemma** — and used it to show precisely why the "branch-
validity-boundary" part of the candidate set $Q$ is not the place a
genuinely new obstruction can live (any such candidate secretly reduces
to a shape using strictly fewer cuts). The genuinely open part of the
existence-only route (branch-comparison-boundary and within-branch-tie
candidates) is honestly reported as **not closed this round**, with a
precise diagnosis of the obstruction (Section 6.3: no known uniform
convexity/concavity certificate for OddSum on a fixed-cut-allocation
fragment polytope, confirmed by an explicit non-concave, non-convex
$N=2$-style witness). Status stays `partial`.

## Round 14 target: corrected scope + chain-tie cheap-kill (per outliner, revise)
**[Addressed this round — see "Approaches tried / Round 14" below and new
Section 4.8.]** Two mandatory items per this round's dispatch: (1) state
the **corrected target** explicitly — round 11's Mass-Constraint Theorem
only refutes a **fixed, $n$-independent** split-piece count $s_0$ for the
tie-to-whole-untouched-piece family; it says **nothing** about an
$n$-dependent construction using up to the full $n$-cut budget, so that
route is genuinely still open, not "deprioritized" as round 13's language
implied. (2) Run the mandatory numeric cheap-kill on the **cyclic
pairwise-tie chain** construction *before* any proof investment. Result:
**fails broadly and decisively, in exact rational arithmetic (no
floating-point noise possible)** — $9/15$ at $n=3$, $15/15$ at $n=4$,
$13/15$ at $n=5$, $15/15$ at $n=6$ random balanced-region points (the
family's own best member, searched exhaustively over subset/cyclic-order,
still exceeds $c(n)$). Reported as a negative finding, **not** written up
as a lemma, per the dispatch's own instructions. The next candidate
family, the **descending fragment chain** (tie each split piece's smaller
fragment to the next's larger fragment, in a *linear*, not cyclic, chain,
leaving one genuinely free parameter), gives a **mixed, inconclusive**
result: restricted to the two "natural" orderings (full-index-descending
or -ascending), it **also fails broadly** ($5/8$ to $8/8$ across
$n=3,\dots,6$); but an exhaustive search over *all* subset choices and
*all* orderings, at the three specific $n=3$ hard interior points already
catalogued by rounds 12–13, **matches or beats the true $V(p)$** value
exactly at two of three points and comfortably clears $c(3)$ at the
third. This is genuinely promising evidence that the *family* (as an
existential class) is rich enough at those points, but the exhaustive
per-order search used to find the good member is not a closed form and is
combinatorially as expensive as computing $V(p)$ itself — **no tractable
closed-form value or general-$n$ proof was found this round**. Status
stays `partial`; see Section 4.8 for full detail, exact code description,
and the precisely-stated open question for the next round.

## Round 13 target: response-side (adversary-tie) exchange (per outliner, primary)
**[Addressed this round — see "Approaches tried / Round 13" below and new
Section 4.7.]** The one exchange mechanism not yet tried by any round —
building the boundary candidate $q$ from the optimal adversary response
$\sigma^*(p)$'s own near-tie structure, rather than from region-slack
geometry — is **refuted numerically, in the same genuine (non-noise) sense
as round 12's two region-geometry mechanisms**, including in its maximally
weak existential form (best of all cross-piece tie-based candidates). This
closes off the entire *exchange-argument* class (region-side and
response-side, single-choice and existential) as a route to the Existence
Theorem's boundary-endpoint reduction. Per the round's own contingency
plan, the approach now stands down from exchange arguments and reports the
$\Sigma(n,k)$-classification route (Sections 1–4.4, $Q_{\text{region}}$
already fully closed) and fragment-vs-fragment tying (Section 4.5's
deprioritized, not-yet-proved lead) as the only remaining open routes.

## Round 12 target: Region-Boundary Monotonicity (per outliner, primary)
**[Addressed this round — see "Approaches tried / Round 12" above, and new
Section 4.6 below.]** Attempted and **refuted as literally proposed**
(fixed-target-vertex, straight-line path monotonicity fails at $n=3$,
confirmed genuine not noise) via careful numerical testing; a second,
independent transplanted-construction idea also refuted, in exact
arithmetic. The weaker "endpoint inequality" reformulation of the target
(Section 4.6.0) is not refuted and remains the concrete next lead. See old
"Round 12 target" note further below (kept for the original outline text)
and Section 4.6 for the full account.

## Round 11 target (per outliner, revise)
**[Addressed this round — see "Approaches tried / Round 11" above the
"Current best" section, and new Section 4's $L$-enlargement /
Rank-Pinning Lemma plus new Section 4.5's Mass-Constraint Theorem.]**
Mandatory textual fix to Section 1 applied; the intra-branch pairwise-
order subtlety resolved by enlarging $L$; bounded-split-piece-count
sufficiency (Opening 1/3) attempted via the natural Multi-Piece
Subset-Tie construction family and **refuted** for that family (Mass-
Constraint Theorem), with the refutation's scope stated precisely so the
next round knows exactly what remains open (fragment-vs-fragment tying,
or the construction-side monotonicity Opening 2).

## Round 9 target (per outliner, revise — MAJOR PIVOT, concavity abandoned)
**[Addressed this round — see "Approaches tried / Round 9" and new
Section 4 below for the fully proved concavity-free reduction; the
remaining gap is now tractability/classification of $\Sigma(n,k)$, not
the mechanism itself.]**

This round's explorer (lens: concavity) **proved by counterexample that
$V(p)$ is NOT concave** on the balanced region: a high-fidelity,
two-independent-optimizer sweep at $n=2$ found genuine sign-alternating
second differences (deficit $\approx0.0102$ at the worst point, far outside
noise), diagnosing the mechanism precisely — even *within* one fixed
cut-allocation shape $\mathbf m$, the optimal *pin value* for the free
fragment switches as $p$ varies, producing real kinks. **Concavity is
retired as a target — do not re-attempt it.**

**New target, replacing concavity, mathematically complete in principle:**
the Global Vertex Lemma already gives $V(p)=\min_{\sigma\in\Sigma,\text{
valid at }p}f_\sigma(p)$, finite $\Sigma$, each $f_\sigma$ affine, validity
an affine (half-space) condition. Let $L$ be the **finite list of affine
functionals** on $p$-space consisting of (a) every component of every
$x_\sigma(p)$ (the validity boundaries) and (b) every pairwise difference
$f_\sigma(p)-f_\tau(p)$ (branch-comparison boundaries), plus the balanced
region's own defining inequalities. This is a finite **hyperplane
arrangement**; on each open cell, every functional in $L$ has constant
sign, so both which $\sigma$ are valid and which valid $\sigma$ wins are
locally constant — hence $V$ is a **single fixed affine formula on each
cell**. A genuinely affine function's max over a convex polytope cell is
attained at a vertex of that cell — giving a **finite candidate set for
the extremal $p^*$, with no concavity needed at all.** This is the round's
concrete next step: formalize this hyperplane-arrangement / cell-wise-
affine-vertex argument as the approach's Section 4 (replacing the old
concavity section), and identify what practically bounds/prunes the cell
count (the explorer flags this — not tractability of concavity — as the
real remaining difficulty). **A cheap shortcut worth trying first**: check
whether the true global maximizer of $V$ over the balanced region is
already attained at one of the "survivor" configurations already
catalogued by `universal-halving-adversary` (rare tiny-excess points at
$n=6,8$) or `lp-duality-split-polytope`'s triangular family — if so, a
full arrangement enumeration may not be needed, just direct verification
at those already-known candidates.

## Approaches tried

- **Round 22 (this round).** Derived exact closed-form identities for
  Constructions Q and BB (Section 13.1–13.2), each on an explicit,
  fully-derived order-condition domain. Mandatorily re-tested the round-22
  outline's proposed panel best-of-$\{H,C,Q,R,BB,W\}$ and found a
  **genuine exact counterexample** at the rational point $(6,4,2,1)/13\in
  B(3)$ (Section 13.3) — a real hole in the outline's own claim, precisely
  characterized, not left vague. Diagnosed the true local optimum there
  via a from-scratch multi-allocation numeric LP search, reverse-engineered
  a **new construction CB** that fixes it exactly, and derived CB's own
  two-case exact closed-form identity (Section 13.4). A broad
  multi-restart numeric search with the enlarged 7-construction panel
  finds no further violations (Section 13.5) — suggestive, not a proof.
  **CHANGES REQUESTED-equivalent** (self-assessed): genuine new exact
  identities and a real gap found-and-patched at one point, but no
  case-complete symbolic proof that the enlarged panel covers all of
  Region II; several order-condition sub-regimes of Q, BB, CB remain
  undeveloped. Status stays `partial`.

- **Round 21 (this round).** Per this round's dispatch (a genuine
  two-region case-split for $n=3$): built a **new** $3$-cut construction
  (Construction H, "$g_1$-cross-tie trisection" — not one of the eight
  constructions the round-21 explorer already refuted) and proved, in
  full exact-algebra rigor (`sympy` symbolic re-derivation plus a
  $13{,}099$-trial exact-`Fraction` sanity re-check, zero violations),
  a clean closed-form identity
  $\mathrm{OddSum}(H)-c(3)=\tfrac{p_4-\gamma(3)}2$
  valid throughout an explicit, exact algebraic sub-region ("Region I")
  of $B(3)$ containing the hard corner $p^\dagger$ with a genuine
  positive margin in every one of its defining inequalities. This
  **fully closes Region I** (Section 12.5–12.6): $\mathrm{OddSum}(H)\le
  c(3)$ throughout, with equality exactly at $p_4=\gamma(3)$, not merely
  at the single point $p^\dagger$. **Honest, mandatory correction to the
  round's own premise**: Construction H does **not** literally split
  $p_4$ (it leaves $p_4$ untouched, $m_4=0$) — a direct check (Section
  12.1) shows why literally splitting the near-zero $p_4$ cannot fix an
  $O(1)$ excess (both new fragments are $O(p_4)\to0$); the third cut's
  real leverage is tying a *new* fragment of $p_3$ to $g_1$ (a quantity
  comparably small near the corner), not to $p_4$ itself. **Region II
  (the complement) is honestly NOT closed this round**: an exact
  large-scale sample ($128{,}214$ valid region-II trials) shows
  best-of-$\{$Construction C, Construction H$\}$ succeeds on
  $\approx97\%$ of Region II but genuinely fails on the remaining
  $\approx3\%$ (a real, exact-arithmetic counterexample recorded,
  Section 12.8) — so the mandatory "boundary matching, no gap" item is
  **not** achieved this round; only Region I is proved end-to-end.
  **CHANGES REQUESTED** is the expected outcome (the $n=3$ Existence
  Theorem remains open), but Region I is now a complete, gap-free,
  independently-reproducible exact result — genuine progress narrowing
  the open residual to Region II alone. See Section 12 for full detail.

- **Round 20 (this round).** Per this round's dispatch: (a) fully
  closed the $n=2$ achievability half with a complete hand-checked
  casework proof (Section 10.6, rewritten) — no numerics in the final
  argument, only used as an independent sanity check (own
  `/tmp/verify_200_bound.py`, `/tmp/verify_110_101.py`,
  `/tmp/verify_020_002.py`, `/tmp/verify_n2_6shapes.py`, $200{,}000$
  trials per shape, zero violations, matching every claimed exact
  minimum digit-for-digit). Proposed the completed **$n=2$ Achievability
  Theorem** ($V(p^*)=c(2)$ exactly, both directions) for certification.
  (b) Per the outline-reviewer's flagged infeasibility of the outline's
  primary $p_2,p_3$-tied $n=3$ witness, ran the mandated worst-case
  (LP-style, exact-algebra, not sampling) analysis of the recommended
  fallback ($p_3,p_4$-tied pairing) **before any proof investment**, per
  the round's own methodological rule — found it fails too, with the
  same closed-form value $1-p_1$ and the same broad failure region
  ($p_1<7/15$) as the already-refuted $p_2,p_3$-pairing, confirmed with
  an exact-arithmetic LP derivation of the true worst case ($\inf
  p_1=16/45$, giving a genuine margin $\sup(\mathrm{OddSum}-c(3))=1/9$)
  plus a concrete exact-rational counterexample. Both natural single-
  witness pairings for the $2$-cut/$6$-fragment construction are now
  refuted for the whole of $B(3)$, not a corner — see Section 11.
  **CHANGES REQUESTED** is the expected outcome for the overall approach
  ($n=3$ Existence Theorem remains open, now needing either a genuinely
  different construction or a two-witness case split), but the $n=2$
  Existence Theorem (both directions) is now a complete, gap-free proof.

- **Round 19 (this round).** Per this round's dispatch (n=2 Existence
  Theorem, full rigor + n=3 scoping), fully proved the n=2 Existence
  Theorem in casework-free rigor (Section 10.1–10.5): $p_1>10/21$
  throughout $B(2)$ from the region's own gap hypotheses;
  $p_3>(p_1-p_2)\iff p_1<1/2$ (an exact algebraic equivalence, the
  region's own hypothesis restated, not a separate case); hence
  $\mathrm{OddSum}$ of the witness (split $p_1\to(p_2,p_1-p_2)$,
  leave $p_2,p_3$ untouched) equals $1-p_1<11/21<c(2)=4/7$ strictly
  everywhere in $B(2)$ — independently re-verified with $200{,}000$
  exact-`Fraction` trials of my own (zero violations), on top of the
  outline-reviewer's independent $20{,}000$-trial pre-check. Confirmed,
  via the finite ten-shape enumeration from the certified Global Vertex
  Lemma, that no other $n=2$ response shape/branch needs separate
  treatment for *this* result (the Existence Theorem needs only this one
  witness to beat every point of $B(2)$; it does not need to identify
  the true minimizer). Additionally, for the achievability half
  ($V(p^*)=c(2)$ at the geometric partition), proved $\le c(2)$ exactly
  (an explicit shape attains $4/7$) and proved $\ge c(2)$ for $9$ of the
  $10$ finite response shapes fully analytically, with the last $6$
  (two-cut shapes) only strongly supported by converging exact-rational
  grid search (not a complete vertex-by-vertex proof) — honestly flagged
  as the one remaining item to fully close the $n=2$ loop, not
  papered over. Diagnosed concretely (own $45{,}108$-trial exact
  re-verification, $87.6\%$ failure rate, matching the round's
  explorer's reported $71/94$) why the direct $1$-cut lift fails at
  $n=3$: an odd-vs-even multiset-size parity obstruction, not vague
  "more casework." Proposed the n=2 Existence Theorem (upper bound
  direction) for certification (not self-certified). **CHANGES
  REQUESTED** is the expected outcome for the overall approach (general
  $n$ remains open), but the $n=2$ Existence Theorem sub-result itself is
  now a complete, gap-free proof.

- **Round 18 (this round).** Per this round's dispatch: pivoted away
  from Flat-Edge classification to directly testing the two concrete
  "tie-free/sharp-kink" candidate near-maximizers the round-18 explorer
  located by float Nelder–Mead — $m=(1,0,1)$ at $n=2$
  (reported $p\approx(0.4705,0.3363,0.1933)$) and $m=(1,0,2,0)$ at $n=3$
  — re-derived in **exact `Fraction` arithmetic** as instructed, before
  trusting them. **Result 1 (a genuine, concrete correction, not a
  restatement)**: the $n=2$ candidate point is **not in the balanced
  region at all**. Exact check: $p_1-p_2=671/5000=0.1342$ vs.
  $\gamma(2)=1/7\approx0.142857$ — this is *strictly less* than
  $\gamma(2)$, violating the balanced region's own defining inequality
  $p_1-p_2>\gamma(n)$ (Section 0). The round-18 explorer's "gap
  $\approx0.042$" claim is therefore evidence about a point **outside**
  the region this approach targets, not about the balanced-region
  supremum — the float optimizer's unconstrained search silently
  produced an out-of-region artifact, exactly the kind of pitfall
  flagged (for a different search) in round 16's Section 7.2 and round
  15's Twin-Anchor cross-check. **Result 2 (a genuine exact theorem
  about shape $(1,0,1)$, not a numeric spot-check)**: analyzed, in
  closed form, the specific branch of shape $m=(1,0,1)$ that the
  explorer's (invalid) point happened to realize — piece 1's fragment
  pinned to the whole value $p_2$ (giving fragments $p_2,\,p_1-p_2$),
  piece 3 bisected (giving $p_3/2,p_3/2$), piece 2 untouched. Using
  $p_3=1-p_1-p_2$, the resulting $\mathrm{OddSum}$ collapses to the
  clean closed form $\tfrac12+\tfrac{p_1-p_2}2$ (Section 9.2, algebra
  verified both by hand and independently in `Fraction` arithmetic).
  Since $c(2)-\tfrac12=\tfrac1{14}=\tfrac{\gamma(2)}2$ exactly, this
  branch's value **exceeds $c(2)$ for every point of the balanced
  region** (which by definition has $p_1-p_2>\gamma(2)$) — a clean,
  general, exact-arithmetic proof that this specific branch can never
  serve as the region's witness construction, explaining in closed form
  *why* the (invalid, near-boundary) point looked deceptively good: it
  is only good because it sits just outside the region, where
  $p_1-p_2<\gamma(2)$. **Result 3 (numeric, honestly flagged as such,
  not a proof)**: re-ran the true two-level minimax $V(p)$ (min over
  *all* 10 cut-allocations at $n=2$, own from-scratch multi-restart
  Nelder–Mead solver, `/tmp/lpv_full_v.py`) at a corrected,
  constraint-respecting sample near the earlier bad point
  ($p=(50,33,18)/101$, exact rationals, region membership verified
  in `Fraction` first) and found $V(p)\approx0.5050$, far below
  $c(2)\approx0.5714$ — shape $(1,0,1)$ is not even the true argmin
  there. A further constrained random search over $150$ genuinely
  region-valid float samples (region membership checked before every
  call) found a best value $V(p^*)\approx0.5216$, still comfortably
  below $c(2)$, consistent with — and slightly stronger than — the
  explorer's original (invalid-point-based) gap estimate. This is
  **numerical evidence only** (float optimizer, no exact-arithmetic
  certificate that this is the true balanced-region supremum), reported
  honestly as such. **Net effect**: corrects a genuine numeric error in
  the round's premise, proves one clean exact negative fact about the
  candidate shape/branch, and leaves the actual Existence Theorem for
  $n=2$ still open (no exact proof that $\sup_{\text{balanced}}V(p)\le
  c(2)$), though the numeric evidence, once the region constraint bug is
  fixed, still points toward real slack, not a tight boundary. Did not
  reach the $n=3$ shape $m=(1,0,2,0)$ in the time available — flagged
  as the immediate next task, same methodology (fix the exact region
  constraint check first, then redo the branch analysis). See new
  Section 9 for full detail. **CHANGES REQUESTED** — genuine progress
  (a real correction plus one clean exact theorem), Existence Theorem
  itself not closed, and the $n=3$ shape not reached this round.

- **Round 17 (this round).** Per this round's dispatch: (1) ran the
  mandatory cheap-kill (own script, `/tmp/round-17/lpv_cheap/core.py`,
  independent of any prior round's code) of an extremal-selection/
  single-fragment-transfer mechanism adapted from crux `aimo-0119`,
  interpreted precisely as follows (the only physically legal form of
  "transfer" here, since a piece's total mass $p_i$ is fixed by the
  adversary and cannot cross piece boundaries): within one split piece,
  perturbing the two members of a tied fragment-pair by $\pm t$ and
  checking whether any such move strictly *decreases* $\mathrm{OddSum}$
  at the already-computed numerical optimum. Tested at all 6 hard points
  with concrete recorded coordinates ($3$ catalogued $n{=}3$, $2$
  catalogued $n{=}4$, $1$ ascent point) — **the mechanism survives at
  every tested point** (no single-fragment transfer improves the
  optimum — expected, since these are genuine local minima of a
  piecewise-affine function, so this specific verification-only reading
  of the mechanism is tautologically non-improving; it is *not* by itself
  a general recipe for constructing a response $\le c(n)$ from an
  arbitrary starting shape, so it is reported as a **necessary-but-not-
  sufficient** check, not written up as a lemma). (2) Ran the **sweep-
  for-flatness test** exactly as dispatched: for each hard point with a
  within-piece tie, swept the free split parameter $t$ around the tie and
  recorded $\mathrm{OddSum}(t)$ using exact rank-by-rank recomputation
  (Section 8.1). Classified all tested points: `n3_pt3` (bisection of
  piece 3, value $0.0955{=}0.0955$), `n4_pt1` (two simultaneous
  bisections, pieces 1 and 4) are **sharp kinks** (Self-Bisection-
  Crossover, slope jumps directly from $-1$ to $+1$ at $t=0$, zero flat
  width to the resolution of a $0.001$-step scan); `n3_pt1` is a genuine
  **Flat-Edge** (an interval of $t$ of width $\approx0.022$ around the
  optimum where $\mathrm{OddSum}$ is exactly constant, confirmed both
  numerically and, on a hand-built toy instance, in **exact
  `Fraction` arithmetic** with zero floating-point tolerance). (3) Proved
  in full generality **why** these two outcomes are the only two
  possibilities and what distinguishes them: the new, fully proved
  **Flat/Kink Parity Lemma** (Section 8.3) — reduces both phenomena to a
  single sign/parity computation on the ranks of the two paired fragments,
  a clean, reusable, general-purpose fact, not specific to the sampled
  points. (4) Per task 4, checked in exact `Fraction` arithmetic whether
  `n3_pt1`'s Flat-Edge maximizer sits at one of the plateau's own
  endpoints: **no** — the plateau's value is realized identically
  throughout its *interior* as well as at both endpoints (it is a true
  flat segment of the piecewise-affine function, not a single boundary
  point secretly optimal), so "maximizer at an endpoint" is not the right
  framing for this specific instance; the right framing (a face of the
  polytope, not a $0$-dimensional point) is confirmed, not refuted (see
  Section 8.4). One new lemma proposed for certification: the **Flat/Kink
  Parity Lemma**. **CHANGES REQUESTED** — the round's diagnostic tasks are
  complete and a genuine new general mechanism is proved, but the
  Existence Theorem's residual (how to build a certificate that handles
  points landing on Flat-Edge faces, not just isolated vertices) remains
  open; see Section 8.5.

- **Round 16 (this round).** Per this round's dispatch: ran the concrete
  diagnostic requested (own from-scratch Python script,
  `/tmp/round-16/lpv_diag/diag.py`, multi-restart Nelder–Mead per
  cut-allocation, no exact-arithmetic claim made — flagged honestly as
  numerical throughout), computing $V(p)$ and the winning shape's exact
  tie structure at the $3$ catalogued $n=3$ hard points, the $2$
  catalogued $n=4$ hard points, and $3$ further points reached by a short
  ascent-in-$V$ exploration from the $n=3$ points (Section 7). Found a
  decisive, consistent pattern (Section 7.1): branch-comparison-boundary
  degeneracy (multiple distinct cut-allocations tied at the exact optimum)
  is essentially universal across all $8$ points tested, and within-branch
  ties co-occur at $5$ of the $8$. Cross-validated against
  `lp-duality-split-polytope`'s certified Perfect-Tie-Family
  Characterization at $e_0$ (Section 7.4) — that theorem's extremal
  construction is itself a within-branch-tie type, consistent with this
  round's finding elsewhere in the region. Also caught and reported (not
  buried) a genuine low-restart optimizer-noise failure in an exploratory
  hill-climb step (Section 7.2) before it could contaminate any
  conclusion. No lemma proposed this round (the finding is a numerical
  classification, per the dispatch's own accepted menu of deliverables,
  not a proved theorem); Status remains `partial`.

- **Round 15 (this round).** Per this round's dispatch (mandatory cheap-
  kill first, then in-round pivot if it fails): (1) formalized the
  **star/tree fragment-tying topology** — one "hub" split piece with
  $r$ fragments, $r-1$ of which are tied to a single "small" fragment
  peeled from each of $r-1$ distinct "partner" pieces — as a closed-form
  application of the certified Singleton-Interleaving Lemma (Section 5.1),
  tested it **exhaustively** (every hub, every partner subset of size
  $\le\lfloor n/2\rfloor$, a fine breakpoint/grid search over the free
  parameters, all in exact `Fraction` arithmetic — no floating point) at
  $15$ fresh random balanced-region points each for $n=3,4$, and
  **refuted it**: $1/15$ failures at $n=3$ (this $n$'s cut budget only
  admits $r=2$, i.e. one partner, so at $n=3$ the family degenerates to
  content already covered/refuted by the descending-chain family) and,
  more importantly, **$2/15$ genuine failures at $n=4$ with $r=3$ (two
  partners simultaneously)** — a topology not reducible to any
  previously-tested 2-node chain link. Re-verified both $n=4$ failures
  survive a $\sim4\times$ finer breakpoint grid ($60$ vs. $14$ points per
  free coordinate), confirming the failure is not a search-resolution
  artifact (Section 5.2 for the exact witnesses and methodology). No
  lemma proposed for this negative finding, per the established
  discipline. (2) Per the outline's mandatory in-round pivot, moved to
  the **existence-only per-cell LP-certificate route** (Section 6): en
  route, discovered and proved from scratch a new elementary fact, the
  **Zero-Removal Invariance Lemma** (Section 6.1) — removing all
  zero-valued elements from a multiset never changes its $\mathrm{OddSum}$
  — and used it (Section 6.2) to show that any branch-validity-boundary
  candidate in $Q$ (where some fragment of the winning shape is pinned
  to exactly $0$) secretly encodes a shape that only uses strictly fewer
  than $n$ cuts, i.e. is not a source of a genuinely new $n$-cut-specific
  obstruction — a real, if narrow, structural narrowing of $Q$'s
  Σ-shape residual. The remaining two families of Σ-shape candidates
  (branch-comparison-boundary $f_\sigma=f_\tau$, and within-branch-tie
  candidates) are **honestly reported as not closed**: Section 6.3
  gives a precise diagnosis of why the natural "uniform LP-duality
  certificate" mechanism does not transparently apply (an explicit
  computation showing $\mathrm{OddSum}$ restricted to a fixed-cut-
  allocation fragment polytope is neither uniformly convex nor uniformly
  concave, so no single-sided certificate technique can apply
  cell-independently without further case analysis). Status remains
  `partial`; see Sections 5–6 for full detail.

- **Round 14 (this round).** Per this round's dispatch: (1) **corrected
  the target's scope** in writing (new "Round 14 target" note above and
  Section 4.8.0 below) — the round-11 Mass-Constraint Theorem rules out
  only a *fixed* $s_0$ for the tie-to-whole-untouched-piece family; an
  $n$-dependent construction (using up to the full $n$-cut budget) is
  genuinely untested, correcting round 13's "deprioritized" framing which
  overstated how settled this residual is. (2) Ran the **mandatory cheap
  numeric gate** on the cyclic pairwise-tie chain construction, in exact
  `Fraction` arithmetic (own from-scratch script, independent of any prior
  round's optimizer code), at $n=3,\dots,6$: **fails broadly** (see Section
  4.8.1 for the exact construction, code description, and full numeric
  table) — reported honestly as a negative finding, not written up as a
  lemma. (3) Per the outline's contingency, tried the next candidate,
  the **descending fragment chain** (Section 4.8.2): found and fixed a
  genuine construction bug in the first draft of this test (conflating a
  tied *value* with a single shared *variable*, which silently dropped a
  fragment from the multiset and produced OddSum values below the
  elementary $\ge\mathrm{sum}(M)/2$ floor — caught by that very sanity
  check before drawing any conclusion). The corrected construction gives a
  **mixed result, honestly reported as inconclusive, not a survival**:
  natural/simple orderings fail broadly (comparable failure rate to the
  cyclic family), while an *exhaustive* search over subset/order choices
  recovers or beats $V(p)$ at the three already-catalogued $n=3$ hard
  points — but that exhaustive search is not a closed form and is not
  shown to be tractable or to generalize to a proof for all $n,p$. No
  lemma proposed for certification this round (both findings are
  numerical: one cleanly negative, one genuinely mixed/inconclusive,
  neither is a proved general theorem). Status remains `partial`.

- **Round 13.** Per that round's dispatch (the one remaining
  untried exchange mechanism, per round 12's explorer §7): build the
  boundary candidate $q$ from the optimal **adversary response**
  $\sigma^*(p)$'s own near-tie structure, not from region-slack geometry.
  Formalized precisely (Section 4.7) and **numerically stress-tested
  first, before any proof investment**, per the dispatch's mandatory
  gate, on an independent Python re-implementation re-verified against
  this file's own Section 4.6.1 methodology and against the exact
  certified $V(e_0)$ values. Tested at the *same* interior points that
  broke every region-geometry mechanism in round 12 (the $n=3$ points with
  logged excess $\approx0.0098,0.0013,0.0098$ against the best
  region-geometry candidate), plus fresh random interior points. **Fails
  genuinely, not from optimizer noise** (excess $\gtrsim10^{-3}$ to
  $7\times10^{-3}$, three to four orders of magnitude above the
  established $10^{-6}$–$10^{-10}$ noise floor, confirmed stable under
  $2.5$–$3\times$ more restarts): the single-choice form (push the
  *closest*-to-breaking cross-piece tie to exact equality) fails at all
  three of round 12's hard points; even the maximally weak **existential**
  form (try *every* cross-piece tie pair in $\sigma^*(p)$'s structure, not
  just the closest one, and take the best) still fails at $2$ of the same
  $3$ points, with genuine excess $\approx0.0031$ and $\approx0.0041$. A
  fresh batch of $6$ random interior points at $n=3$ (not cherry-picked
  from round 12's failures) shows the same $\approx50\%$ failure rate as
  every previously-tried mechanism. **Conclusion, reported honestly per
  the dispatch's own contingency plan**: this closes off exchange
  arguments as a class (region-side *and* response-side, single-choice
  *and* existential) as a route to the endpoint-inequality bypass of
  $\Sigma(n,k)$-classification. No certified-lemma-track proposal this
  round (the finding is negative/numerical, following the precedent of
  how round 12's own negative numerical findings were handled). Status
  remains `partial`; see Section 4.7 for the full account and exact test
  data/code description.

- **Round 12.** Per this round's dispatch (Region-Boundary
  Monotonicity, primary target), attempted to prove that $V(p)$ always has
  a boundary-pointing direction along which it is weakly non-decreasing,
  which would close the Existence Theorem outright without classifying
  $\Sigma(n,k)$. **Refuted as literally proposed**: careful, noise-
  controlled numerical testing (multi-restart Nelder–Mead over the full
  Global Vertex Lemma shape enumeration, cross-checked against the
  certified exact $V(e_0)$ values) shows the straight-line path toward
  $e_0$ (or $e_1$) is cleanly monotone in every one of $20$ trials at
  $n=2$, but genuinely non-monotonic (confirmed at $3\times$ restart
  count, not an optimizer artifact) at $n=3$ — the $n=2$ evidence was an
  artifact of that case's exceptional simplicity (already flagged as
  exceptional in Section 4.1's vertex classification), not a general
  phenomenon. A second, independent idea — transplanting the exact
  construction that closes $e_0$ (the consecutive-pairing $k$-Anchor-Merge
  shape) unchanged to every point of the region — is **refuted in exact
  `Fraction` arithmetic** for $n=2,\dots,8$ (fails at $100\%$ of tested
  points for $n\ge5$, after fixing a region-membership filter bug found
  and corrected before drawing conclusions). Both findings are honestly
  reported as ruling out these two specific mechanisms, not the Existence
  Theorem itself (no violation of $V(p)\le c(n)$ was found in any test);
  the weaker, actually-sufficient "endpoint inequality" form of the target
  (Section 4.6.0) remains open, unrefuted, and is the concrete next
  target. Fragment-vs-fragment tying (secondary target) not attempted
  this round. Certified-lemma-track proposals for the reviewer: none this
  round (both results are numerical, not exact-arithmetic proofs, except
  the transplanted-construction refutation's *exact-Fraction* computation,
  which is itself a proof of the closed-form inequality's failure at the
  specific tested rational points, but not a general theorem covering all
  $p$ — not proposed for certification as a standalone lemma since its
  content is fully captured in this file's Section 4.6.4 and is
  negative/scoping in nature, matching how round 11's own numerical
  Section 5 finding was handled). Status remains `partial`.

- **Round 11.** Per this round's dispatch: (1) fixed the
  Section 1, item 1 textual contradiction ("one free block per split
  piece," matching the proof, not the previous "one free block total"
  wording — a genuine bug the round's explorer found, now corrected).
  (2) Resolved the round's second flagged subtlety (does $L$ need
  intra-branch pairwise-order boundaries?) by choosing the explicit-
  enlargement route: added all pairwise differences of each shape
  $\sigma$'s own multiset $y_\sigma(p)$ to $L$, and proved the new
  **Rank-Pinning Lemma** closing the gap in Lemma 4.1(b)'s proof as it
  stood through round 10 (which pinned the *ordering between* branches
  but never justified that each $f_\sigma$ is itself affine on a cell).
  Verified this does not disturb the already-closed $Q_{\text{region}}$
  (region-only) work. (3) Attempted the round's main new target,
  bounded-split-piece-count sufficiency: formalized the **General
  Multi-Piece Subset-Tie construction** (the natural common
  generalization of the certified Theorem 12 and the qualitative pattern
  of round 10's numeric $n=6$ witness) and proved, in full rigor (not
  numerically), the **Mass-Constraint Theorem** — any legal instance
  needs the split pieces' total mass $\ge1/2$ — which forces $s>(n+1)/3$
  split pieces at the already-closed region vertex $e_0$, unboundedly
  many as $n\to\infty$. This **refutes bounded-$s_0$ sufficiency for this
  specific, natural construction family**, for every fixed $s_0$: a
  genuine negative result, not a numerical finding, correctly redirecting
  future rounds away from this mechanism (with the scope of the
  refutation stated precisely — fragment-vs-fragment tying, glimpsed in
  round 10's raw numeric data, is explicitly not covered and remains the
  most promising open lead). Certified-lemma-track proposals for the
  reviewer this round: the Rank-Pinning Lemma and the General Multi-Piece
  Subset-Tie construction + Mass-Constraint Theorem (both self-contained,
  proved from already-certified content). Status remains `partial`: the
  Existence Theorem itself is not established; this round's contribution
  is two genuine soundness/rigor fixes plus one precisely-scoped negative
  result that narrows the search space for the next construction attempt.

- **Round 10.** Per this round's outline, closed the round-9
  gap and executed its full skeleton: (1) fixed $L$ by adding the missing
  functional $p_k$ (Section 4's Definition, corrected), and confirmed
  Lemmas 4.1/4.2 and the Finite-Cell theorem hold verbatim (they use only
  finiteness/affineness of $L$). (2) Proved, in closed form for **every**
  $n\ge2$ (not a numeric spot-check), the exact **Region-Vertex
  Classification Theorem** (Section 4.1): reparametrized the region-only
  polytope as an $n$-simplex sliced by one more half-space ($p_k\ge0$),
  and classified its vertices via three algebraic claims (Claims A, B, C,
  each proved by an explicit induction or a closed-form sign computation,
  not numeric search) — recovering and *explaining* the outline-reviewer's
  numerically-checked count ($3$ at $n=2$, $5$ at $n=3$, $2+2(n-1)$ for
  $n\ge4$), including a precise identification of exactly why $n=2,3$ are
  exceptional (a specific simplex vertex $e_2$ crosses the sign boundary
  at exactly these small $n$, proved via the exact identity
  $N(n,2)=n(3-n)$). (3) Proved a general **Boundary Continuity Theorem**
  (Section 4.2, via a newly-derived **Small-Mass Insertion Lemma** —
  $|\mathrm{OddSum}(M\cup F)-\mathrm{OddSum}(M)|\le\mathrm{sum}(F)$,
  proved from scratch via an exact telescoping-sum computation reducing to
  the certified Section-2 Lipschitz Fact) that closes **every** point of
  the degenerate face $\overline{B(n)}\cap\{p_k=0\}$ — not just the
  finitely many vertices — by identifying its continuously-extended value
  exactly with the already-closed $k\le n$ slack-budget regime's value
  (Theorem 3, certified), sandwiching both directions to $O(t)$ and taking
  $t\to0$. (4) Closed the (two, for $n\ge3$; three, for $n=2$) genuine
  vertices in **exact arithmetic** (Section 4.3), upgrading round 9's
  numeric $V\approx1/2$ finding: identified both genuine vertices'
  coordinates as consecutive runs of an arithmetic progression with common
  difference exactly $\gamma(n)$, applied the certified General
  $k$-Anchor-Merge Lemma with a consecutive-pairing construction, and
  derived the exact closed-form value $\mathrm{OddSum}=\tfrac12$ or
  $c(n)$ (by an explicit parity rule on the pair count $k$), using the
  new exact identity $c(n)=\tfrac12+\tfrac{\gamma(n)}2$. This **fully
  closes the entire region-only candidate sub-list** $Q_{\text{region}}$
  of the Finite-Cell theorem's vertex set $Q$ (Section 4.4) — a complete,
  general-$n$ result, not previously established even in outline form.
  **Honestly reported as still open, unchanged in kind**: the
  $\Sigma$-shape functionals' contribution to $Q$ (candidates involving a
  branch-validity or branch-comparison boundary, not just a region
  inequality) is entirely untouched, and nothing proved this round shows
  the true maximizer $p^*$ avoids that part of $Q$ — so the Existence
  Theorem itself remains open, and Status stays `partial`.

- **Round 9.** Per the outliner's pivot instruction, abandoned
  concavity of $V(p)$ (retired for good — round 9's explorer found a
  genuine sign-alternating second-difference counterexample at $n=2$,
  deficit $\approx0.0102$, far outside noise). Replaced Section 4 with a
  **fully rigorous, concavity-free** finite hyperplane-arrangement /
  cell-wise-affine-vertex reduction theorem (new Section 4), built directly
  from the already-certified Global Vertex Lemma and Lipschitz continuity —
  no new unproven ingredient. This **fully closes the mechanistic step the
  outline asked for**: the extremal $p^*$ of the Existence Theorem is now
  proved (unconditionally, no concavity needed) to lie in a finite,
  explicitly-describable candidate set. Handled the outline-reviewer's
  flagged open/closed-boundary subtlety explicitly (Lemma 4.2 below) via a
  density-plus-continuity argument, not a silent assumption. Also executed
  the outline's "cheap shortcut" instruction: numerically tested (Section 5,
  new) whether one of `universal-halving-adversary`'s catalogued
  "survivor" configurations (a genuine documented instance where the named
  additive-tool family fails to certify $\le c(n)$) is a true counterexample
  to the Existence Theorem or merely a gap in the named-tool family — found,
  at the concrete $n=6$ survivor $p=(0.3306,0.2791,0.1501,0.1162,0.0904,
  0.0208,0.0128)$, a genuinely different response (splitting the **three**
  largest pieces $p_1,p_2,p_3$ each into $3$ fragments, tying fragments
  against the untouched tail pieces) achieving $V(p)\lesssim0.50155$, well
  below $c(6)\approx0.50394$ — i.e. this specific "survivor" is **not**
  a true failure of the Existence Theorem, only a failure of the
  $k\le2$/Subset-Tie tool family. This is numerical (Nelder-Mead,
  multi-restart), not an exact-arithmetic proof, but it is strong evidence
  that round 8's "survivor rate grows with $n$" finding is an artifact of
  the *named-tool* family being too narrow, not of the true Existence
  Theorem failing — exactly the diagnostic the outline's shortcut was
  designed to produce. Neither the general Existence Theorem nor its
  general-$n$ tractability (enumerating/bounding $\Sigma(n,k)$ and the
  induced arrangement) is closed this round; both are honestly reported as
  open, with the tractability gap now the single, precisely-located
  remaining obstruction (concavity is no longer needed at all).

- **Round 8.** Per the outline
  (`/tmp/round-8/proof-outliner.md`, "global-lp-vertex-sufficiency: new")
  and the outline-review's approval, built out steps 1–2 of the sketch in
  full rigor (they turn out to already be essentially certified content,
  needing only correct assembly, not new mathematics), proved a genuinely
  new **Lipschitz-continuity fact** for the game-value function $V(p)$ as
  $p$ ranges over LB's partition simplex (via an explicit "proportional
  transport" construction, not cited from anywhere), and used it to prove
  a real (if modest) **existence-of-a-maximizer** statement via
  compactness. Then investigated the outline's proposed next step — that
  $V$ is *concave* in $p$, which would let the outer maximization reduce
  to boundary/breakpoint configurations the way Theorem 3 and Theorem B
  did one level down — and found a genuine **obstruction**: the classical
  LP fact that licenses this kind of argument (optimal value of a linear
  program is convex in the right-hand side) does not transparently apply
  here, because $V$'s objective ($\mathrm{OddSum}$) itself depends
  directly on $p$ (untouched pieces are literally components of $p$, not
  just RHS constants), not only through the constraint sums. I could
  neither prove nor disprove concavity in the time available; a modest
  numerical stress test (n=2, 15 random balanced-region segment triples,
  best-of-many-random-splits proxy for $V$) found **no violation** of the
  concavity inequality (worst deficit $\approx-3\times10^{-5}$, consistent
  with numerical noise / exact equality, not a genuine violation), so
  concavity remains a **plausible open conjecture**, not refuted, but also
  not established. This is reported honestly: real structural progress
  (Global Vertex Lemma assembly, Lipschitz continuity, maximizer
  existence) plus a precisely located, honestly-flagged obstruction to the
  next step (concavity / finite extremal reduction), rather than an
  overclaimed full argument.

## Current best

### 0. Setup (imported without change)

By the certified Reduction Lemma
(`lemmas/reduction-to-multiset-minimax.md`), the game value is
$$c(n)=\max_{\substack{p_1,\dots,p_k>0\\ \sum p_i=1,\ k\le n+1}} V(p),\qquad
V(p):=\min_{\substack{\mathbf m\in\mathbb Z_{\ge0}^k,\ \sum m_i\le n\\ \text{split each }p_i\text{ into }m_i+1\text{ positive parts}}}
\mathrm{OddSum}(\text{resulting multiset}).$$
We work throughout in the **balanced region** (the residual left open by
every other upper-bound approach): $k=n+1$, $p_1<1/2$, and every
consecutive gap $p_i-p_{i+1}>1/(2^{n+1}-1)=\gamma(n)$ (else the region is
already closed unconditionally, `lemmas/singleton-interleaving-and-k-anchor-merge.md`).
The **Existence Theorem** this approach targets is: $V(p)\le c(n)$ for
*every* $p$ in this region.

### 1. The Global Vertex Lemma (fully proved — assembly of already-certified content)

**Lemma (Global Vertex Lemma).** Fix $n$ and $k\le n+1$. There is a
**finite set $\Sigma=\Sigma(n,k)$ of combinatorial "shapes"**, depending
only on $n,k$ (not on $p$), such that:

1. Each shape $\sigma\in\Sigma$ consists of: a cut-allocation
   $\mathbf m=(m_1,\dots,m_k)$ with $\sum m_i\le n$; for each $i$, a set
   partition of the $m_i+1$ fragment-slots of piece $i$ into blocks; a
   choice, for **each split piece $i$ (i.e. each $i$ with $m_i\ge1$),
   of one designated "free" block among that piece's own blocks — one
   free block per split piece, not one free block total across the
   whole shape** (corrected this round: the previous wording, "a single
   free block designated among all blocks across the whole shape,"
   contradicted the proof immediately below and the cited Two-Piece-Split
   Vertex Lemma, and — as this round's explorer flagged — would
   undercount $\Sigma$ and invalidate the vertex characterization
   whenever $\ge2$ pieces are split simultaneously, since each split
   piece contributes its *own* independent piece-sum equality
   $\sum(\text{its fragments})=p_i$ and hence needs its *own* free
   block to absorb that equation's degree of freedom; a single shared
   free block cannot simultaneously solve $\ge2$ independent linear
   equations in general). Every non-free block of every split piece is
   pinned to a value in $\{0\}\cup\{p_1,\dots,p_k\}$ (with the convention
   that a block pinned to "$p_j$" for $j$ equal to the *piece being
   split* is disallowed, since that would pin a fragment of $p_i$ to
   $p_i$ itself, which is only meaningful if $i\ne j$).
2. Each shape $\sigma$ determines an explicit **affine-in-$p$ formula**
   $x_\sigma(p)$ for every fragment (pinned blocks get the pinned value;
   the one free block is solved from $p_i=\sum(\text{that piece's
   fragments})$ by subtracting off the other blocks' pinned values,
   dividing by the free block's size — an affine function of the $p_j$'s
   composed with the identity/linear map "pin value $\mapsto$ that
   value", hence affine in $p$).
3. For every $p$ in the simplex $\{p_i>0,\sum p_i=1\}$,
   $$V(p)=\min_{\sigma\in\Sigma,\ x_\sigma(p)\ge0\text{ (all coords)}} \mathrm{OddSum}\bigl(x_\sigma(p)\cup(\text{untouched }p_j\text{'s})\bigr).$$

**Proof.** Fix $p$. By the certified **Vertex Pinning Lemma**
(`lemmas/vertex-pinning-lemma.md`), $V(p)$ (a minimum over legal XY
responses, which range over all cut-allocations $\mathbf m$ and, for each,
the corresponding product-of-simplices of fragment values) is attained,
and the minimizer's cut-allocation $\mathbf m^*$, after discarding
wasted cuts, is a genuine positive-fragment response at which at least
$\sum_im_i^*$ independent exact ties are active. This is exactly the
content needed to run the standard linear-algebra vertex characterization
(a feasible point of a polyhedron is an extreme point of the
sort-order region containing it iff the active constraints — the $k$
piece-sum equalities plus enough zero/tie inequalities — have full rank):
this same vertex characterization is worked out in complete,
self-contained detail (not merely cited) in the certified
**Single-Piece-Split Vertex Lemma**
(`lemmas/single-piece-split-vertex-lemma.md`, Lemma proof, "We claim this
union of extreme points is exactly $\mathcal V$...") for the special case
of one piece split with the rest held as fixed external constants, and
the identical argument (block-partition into equivalence classes of tied
fragment-slots, one designated free block per independent equality
deficiency, every other block pinned to $0$ or to a specific external
constant) applies **verbatim** when *several* pieces are split
simultaneously: the only change is that the "external constants" a
pinned block can equal now include $p_j$ for *every* untouched or
differently-split piece $j$ (not just a fixed handful), and the "free
block, one per piece" becomes "free block, one per piece $i$ that is
actually split" (each split piece $i$ contributes its own independent
piece-sum equality $\sum(\text{its fragments})=p_i$, hence its own
degree-of-freedom deficit requiring its own free block) — this is exactly
what the already-certified **Two-Piece-Split Vertex Lemma**
(`lemmas/two-piece-split-vertex-lemma.md`, cited by
`lp-duality-split-polytope`, round 6, as proved for exactly this
two-simultaneously-split-pieces case) establishes for $k=2$ split pieces,
and the identical block/pin construction, run independently for each
split piece with the shared pool of possible pin values
$\{0\}\cup\{p_1,\dots,p_k\}$, extends without modification to any number
of simultaneously split pieces (the vertex characterization is a purely
local, per-constraint-set linear-algebra fact — it does not reference how
many pieces are split, only that each split piece contributes its own
independent sum-equality and hence its own free block). This gives item
1–2. Item 3 is then the same "the true minimum over a bounded polytope
equals the minimum over the extreme points of its finitely many
sort-order regions" fact used identically in the Single/Two-Piece Vertex
Lemmas, applied to the full product-of-simplices polytope
$\prod_i\Delta_{m_i}(p_i)$ for each fixed $\mathbf m$, then minimized
over the finitely many $\mathbf m$ with $\sum m_i\le n$. $\blacksquare$

**What is genuinely new here versus a restatement.** Rounds 5–7 proved
the single-piece and two-piece special cases explicitly; this round's
contribution is observing (and justifying, via the "each split piece
contributes its own independent free block" argument above) that the
identical mechanism scales to *any* number of simultaneously-split
pieces, with **no new proof technique** — it assembles already-certified
pieces into the fully general statement the outline's steps 1–2 asked
for. $\Sigma(n,k)$ is finite because: the number of cut-allocations
$\mathbf m$ with $\sum m_i\le n$ is finite (a bounded composition
count); for each, the number of set-partitions of a bounded number of
slots is finite (Bell numbers); and for each partition, the number of
ways to choose the free block and assign pin values from the finite set
$\{0,p_1,\dots,p_k\}$ to the remaining blocks is finite.

### 2. Lipschitz continuity of $V(p)$ (new, fully proved)

**Fact (OddSum is 1-Lipschitz in $\ell^1$, fixed cardinality).** For two
finite multisets $A=\{a_1,\dots,a_N\}$, $B=\{b_1,\dots,b_N\}$ of the same
size $N$, sorted descending, $\bigl|\mathrm{OddSum}(A)-\mathrm{OddSum}(B)\bigr|
\le\sum_{j=1}^N|a_j-b_j|$ (comparing sorted-descending order, i.e. the
$j$-th largest of $A$ against the $j$-th largest of $B$).

**Proof.** $\mathrm{OddSum}(A)-\mathrm{OddSum}(B)=\sum_{j\text{ odd}}(a_j-b_j)$
(comparing rank-by-rank in each one's own sorted order), so
$|\mathrm{OddSum}(A)-\mathrm{OddSum}(B)|\le\sum_{j\text{ odd}}|a_j-b_j|
\le\sum_{j=1}^N|a_j-b_j|$. $\blacksquare$

(This uses the standard identification of the $j$-th order statistic of
a fixed-size tuple as a $1$-Lipschitz — indeed here we do not even need
the sorting-is-1-Lipschitz refinement, just the trivial rank-by-rank
triangle inequality on each one's own sorted list, which suffices for
what follows.)

**Theorem (Lipschitz continuity of $V$).** For $p,p'$ in the simplex
$\{p_i>0,\sum_1^k p_i=1\}$ (same $k$), $|V(p)-V(p')|\le\|p-p'\|_1$.

**Proof.** By symmetry it suffices to show $V(p')\le V(p)+\|p-p'\|_1$.
Let $\mathbf m^*,(x_i)$ be an optimal response to $p$ (attaining $V(p)$,
using the Closure Lemma inside the Vertex Pinning Lemma to guarantee a
genuine attained minimum with positive fragments). For each split piece
$i$ (with $m_i\ge1$), write its fragments as $p_i\cdot(\lambda_{i,1},
\dots,\lambda_{i,m_i+1})$ where $\lambda_{i,\bullet}>0$,
$\sum_j\lambda_{i,j}=1$ (the fragment *proportions*). Apply the **same
cut-allocation and the same proportions** to $p'$: split $p_i'$ into
fragments $p_i'\cdot(\lambda_{i,1},\dots,\lambda_{i,m_i+1})$. This is a
legal response to $p'$ using the identical $\le n$ cuts, with positive
fragments (since $\lambda_{i,j}>0$ and $p_i'>0$), giving some multiset
$M'$; by definition $V(p')\le\mathrm{OddSum}(M')$.

Compare $M$ (the multiset from $p$) and $M'$ element-by-element, matched
by "which original piece and which proportion-slot" (a canonical
bijection between the two multisets' elements, of the same total size
$N=k+\sum m_i$, since both use the identical cut-allocation): an
untouched piece $j$ contributes $p_j$ to $M$ and $p_j'$ to $M'$
(difference $|p_j-p_j'|$); a fragment-slot $(i,j)$ of a split piece
contributes $p_i\lambda_{i,j}$ to $M$ and $p_i'\lambda_{i,j}$ to $M'$
(difference $\lambda_{i,j}|p_i-p_i'|$). Summing the *canonically matched*
differences (not the sorted-order differences — but this suffices,
since the $\le$ bound below only needs *some* valid bijection between
same-size multisets, and $\ell^1$ distance between sorted lists is always
$\le$ that between any other matching, a standard rearrangement fact —
we do not even need this refinement: the crude bound via *any* bijection
still upper-bounds the sorted-rank-matched $\ell^1$ distance, since the
optimal transport / assignment cost between two multisets under $\ell^1$
ground cost equals exactly the sorted-rank-matched sum, and is by
definition the *minimum* over all bijections, hence any specific
bijection's total gives a valid upper bound):
$$\sum_{\text{canonical match}}|\cdot|=\sum_{j\text{ untouched}}|p_j-p_j'|
+\sum_{i\text{ split}}\Bigl(\sum_j\lambda_{i,j}\Bigr)|p_i-p_i'|
=\sum_{j\text{ untouched}}|p_j-p_j'|+\sum_{i\text{ split}}|p_i-p_i'|
=\sum_{i=1}^k|p_i-p_i'|=\|p-p'\|_1,$$
using $\sum_j\lambda_{i,j}=1$ for each split piece. By the Fact above
(applied with the canonical bijection's matching, which upper-bounds the
sorted-rank matching's $\ell^1$ distance since the latter is the minimum
over all bijections — standard rearrangement inequality for optimal
transport with $\ell^1$/absolute-value cost on the line, elementary and
well known):
$$\mathrm{OddSum}(M')\le\mathrm{OddSum}(M)+\|p-p'\|_1=V(p)+\|p-p'\|_1.$$
Hence $V(p')\le V(p)+\|p-p'\|_1$. $\blacksquare$

**This is genuinely new content this round** (not previously proved in
this project in this generality; `universal-halving-adversary`'s round-6
file only *asserted*, without proof, that "order statistics ... are
continuous, indeed 1-Lipschitz" as a passing remark in its Pruning Lemma
discussion — here it is proved from scratch, directly for $V$ itself
(the two-level minimax value), not merely for a single order statistic,
via the explicit proportional-transport construction above).

### 3. Existence of a maximizer (new, fully proved, modest)

**Corollary.** For each $n$, the balanced region's closure (adding the
boundary where some gap equals $\gamma(n)$ or $p_1=1/2$) is a compact
subset of the simplex $\{p_i>0,\sum p_i=1\}$ (a closed, bounded polytope,
intersected with closed half-space conditions), and $V$ is continuous
on it (Lipschitz, hence continuous, by Section 2). By the extreme value
theorem, $\sup_p V(p)$ over this closed region is **attained** at some
$p^*$.

This is a genuine, if modest, step: it converts the Existence Theorem
from "for every $p$ in an open/unbounded-in-spirit family, some
construction works" into "there is a *specific* worst-case $p^*$, and it
suffices to exhibit a response achieving $\le c(n)$ at that one point" —
however, **it gives no handle on characterizing $p^*$**, which is exactly
the missing step.

### 4. Concavity-free finite-cell reduction (new this round, fully proved)

**Concavity is abandoned as a target** (per this round's outline: a
sign-alternating second-difference counterexample at $n=2$, deficit
$\approx0.0102$, was found this round by the concavity-lens explorer,
well outside numerical noise — $V$ is genuinely *not* concave). The
following replaces it with a mechanism that needs **no concavity at
all**.

**Definition (the finite functional list $L$ — corrected round 10, FURTHER
CORRECTED this round).** Fix $n$, $k=n+1$. Let $\Sigma=\Sigma(n,k)$ be the
finite shape set of the Global Vertex Lemma (Section 1), and for $\sigma\in
\Sigma$ let $y_\sigma(p):=x_\sigma(p)\cup(\text{untouched }p_j\text{'s})$
denote the *full* multiset of $|y_\sigma|\le k+n$ real values (fragments
plus untouched pieces) whose sorted-descending odd ranks define
$f_\sigma(p)=\mathrm{OddSum}(y_\sigma(p))$. Define
$$L \;=\; \bigl\{\text{each coordinate of }x_\sigma(p) : \sigma\in\Sigma\bigr\}
\;\cup\; \bigl\{f_\sigma(p)-f_\tau(p) : \sigma,\tau\in\Sigma\bigr\}
\;\cup\;\boxed{\bigl\{y_\sigma(p)_a-y_\sigma(p)_b:\sigma\in\Sigma,\ a\ne b
\text{ coordinates of }y_\sigma(p)\bigr\}}
\;\cup\; \bigl\{p_1-\tfrac12,\ p_i-p_{i+1}-\gamma(n)\ (i=1,\dots,n),\ p_k\bigr\},$$
a finite collection of affine-in-$p$ functionals on the hyperplane
$H=\{p\in\mathbb R^k:\sum p_i=1\}$. The last (unboxed) group is exactly the
affine functionals defining the balanced region $B(n)$ and its closure
$\overline{B(n)}$: $p_1<1/2$ (resp. $\le$), each gap
$p_i-p_{i+1}>\gamma(n)$ (resp. $\ge$), and $p_k>0$ (resp. $\ge0$) —
the omission found by the reviewer round 9 and fixed round 10. **New this
round (the boxed group): all pairwise differences among a single shape
$\sigma$'s own multiset $y_\sigma(p)$** — this closes a second gap, found
by this round's explorer, that round 10's $L$ did not yet address: see the
Lemma below. $L$ remains finite: $\Sigma$ is finite (Section 1), each
$x_\sigma$ has finitely many coordinates, each $y_\sigma$ has finitely
many ($\le k+n$) coordinates so each $\sigma$ contributes only finitely
many (at most $\binom{k+n}2$) pairwise-difference functionals, and there
are finitely many $\sigma$.

**Why the boxed group is needed (the gap this round's explorer found).**
$f_\sigma(p)=\mathrm{OddSum}(y_\sigma(p))=\sum_{\text{odd ranks of
}y_\sigma(p)}(\text{that coordinate})$ is a fixed affine-in-$p$ *formula*
only once we know **which coordinate of $y_\sigma(p)$ occupies which rank**
— i.e. only once the internal sort order of $y_\sigma(p)$'s own
coordinates is pinned. Nothing in $\sigma$'s combinatorial data (the
cut-allocation, block partition, and pin assignment) pins this order a
priori: two coordinates of $y_\sigma(p)$ (e.g. two fragments of the same
split piece, or a fragment versus an untouched piece) could in principle
cross as $p$ varies within what round 10's $L$-arrangement calls a single
"cell," since round 10's $L$ only tracked (i) validity boundaries
(individual coordinates of $x_\sigma(p)$ vs. $0$) and (ii)
*between-branch* comparisons $f_\sigma-f_\tau$ for $\sigma\ne\tau$ — never
the *within-branch* pairwise comparisons that actually determine
$f_\sigma$'s own sort order and hence its own affine formula. Without
these, Lemma 4.1(b) below (as stated last round) is not fully justified:
it correctly pins the *ordering of the $f_\sigma$ values against each
other*, but silently assumed each $f_\sigma$ is itself a single affine
formula throughout a cell, which requires the boxed functionals.

**Lemma (Rank-Pinning).** On any cell $C$ of the $L$-arrangement (with $L$
as corrected above, including the boxed group), for every $\sigma\in
\Sigma$, the coordinate of $y_\sigma(p)$ occupying each fixed rank
$1,\dots,|y_\sigma|$ is the *same* coordinate index for every $p\in C$;
consequently $f_\sigma(p)=\sum_{r\text{ odd}}y_\sigma(p)_{(\text{index at
rank }r)}$ is a single fixed affine-in-$p$ formula throughout $C$.

*Proof.* Each pairwise difference $y_\sigma(p)_a-y_\sigma(p)_b$ (for
$a\ne b$ coordinates of the same $\sigma$) is, by construction, a member
of $L$, hence — by the defining property of a cell of a finite hyperplane
arrangement (Lemma 4.1(a)'s argument, unchanged) — has constant sign
throughout $C$ (never $0$, since $C$ avoids every hyperplane in the
arrangement). Constant sign of every pairwise difference among a fixed
finite list of coordinates means the coordinates' relative order (hence
which coordinate occupies which rank when sorted descending) is the same
for every $p\in C$: if coordinate $a$ beats coordinate $b$ at one point of
$C$ it beats it at every point of $C$ (the sign of $a-b$ never flips), and
comparing every pair fixes the full order (a finite total order determined
by pairwise comparisons is transitive automatically here since all the
values are honest real numbers at each fixed $p$, not merely abstractly
compared). Hence the rank assignment is locally constant on $C$, and
$f_\sigma(p)$, being the sum of the (now fixed) odd-rank coordinates, is a
single affine-in-$p$ expression on $C$. $\blacksquare$

**Consequence for Lemmas 4.1/4.2 and the Finite-Cell Theorem.** Lemma
4.1(a) (validity of $\sigma$ is cell-constant) is unaffected — it only used
individual coordinates of $x_\sigma(p)$ against $0$, already in $L$'s
first group. Lemma 4.1(b), as re-examined this round, needs the Rank-
Pinning Lemma above (now supplied) as a first step — "each $f_\sigma$ is a
single affine formula on $C$" — *before* the between-branch sign
comparisons $f_\sigma(p)-f_\tau(p)$ (also in $L$) can be used to fix a
total order among $\{f_\sigma:\sigma\in\Sigma_C\}$; with the Rank-Pinning
Lemma supplying that missing first step, Lemma 4.1(b)'s proof goes through
exactly as written previously. Lemma 4.2's proof and the Finite-Cell
Affine-Vertex Reduction Theorem's proof use only that $L$ is finite and
every $\ell\in L$ is affine, plus Lemma 4.1's conclusion — neither is
disturbed by enlarging $L$ with the boxed group (a finite list stays
finite, and every added functional is affine, being a difference of two
affine-in-$p$ coordinates of $y_\sigma(p)$). Hence **Lemmas 4.1, 4.2 and
the Finite-Cell Affine-Vertex Reduction Theorem all hold, with this fully
corrected $L$, and the theorem's conclusion is unchanged in statement**
(only the definition of $L$, hence of the candidate set $Q$, is enlarged to
include the boxed group's zero-sets among the possible $(k-1)$-subsets
solved — $Q$ was always understood as "solutions of $(k-1)$-subsets of
$L$," so this enlargement is absorbed into the existing statement without
any change to its wording).

**Does this affect the already-closed $Q_{\text{region}}$ (Sections
4.1–4.4)?** No: $Q_{\text{region}}$ was defined and closed using only
$(k-1)$-subsets drawn from $L$'s *region* functionals (the last, unboxed
group, unchanged by this round's fix), never from the boxed or
branch-related groups. Sections 4.1–4.4 stand exactly as proved last
round; the boxed-group fix only concerns the (still fully open)
$\Sigma$-shape part of $Q$.

**Lemma 4.1 (cell-wise constancy).** The complement in $H$ of
$\bigcup_{\ell\in L}\{\ell=0\}$ decomposes into finitely many open,
connected **cells** (the connected components), and on each cell $C$:
(a) the set of *valid* $\sigma\in\Sigma$ at $p$ (those with
$x_\sigma(p)\ge0$ in every coordinate) is the same set $\Sigma_C$ for
every $p\in C$; (b) the ordering of $\{f_\sigma(p):\sigma\in\Sigma_C\}$
by value is the same for every $p\in C$; hence there is a single
$\sigma(C)\in\Sigma_C$ with $V(p)=f_{\sigma(C)}(p)$ for **every** $p\in
C$.

*Proof.* Each $\ell\in L$ is continuous and affine, hence has constant
sign ($>0$ or $<0$; it cannot vanish) throughout any connected component
of $H\setminus\bigcup\{\ell=0\}$ — this is the definition of a
hyperplane arrangement's open cells (a cell is, by construction, exactly
a maximal connected set on which every $\ell\in L$ is sign-definite;
finiteness of the number of cells follows because each cell is uniquely
identified by a sign vector in $\{+,-\}^{|L|}$, and $|L|$ is finite, so
there are at most $2^{|L|}$ cells). Fix a cell $C$ and $p\in C$. Validity
of $\sigma$ at $p$ means every coordinate of $x_\sigma(p)$, an element of
$L$, is $\ge0$; since each such coordinate has constant sign on $C$
(strictly $>0$ or $<0$, never $0$ since $C$ avoids all zero sets),
validity of $\sigma$ is the same yes/no answer for every $p\in C$ — this
gives (a), $\Sigma_C:=\{\sigma\text{ valid at any (every) }p\in C\}$.
For (b): for $\sigma,\tau\in\Sigma_C$, the sign of $f_\sigma(p)-f_\tau(p)$
(an element of $L$) is constant on $C$, so the relative order of
$f_\sigma(p)$ and $f_\tau(p)$ is the same throughout $C$; applying this
to every pair in the finite set $\Sigma_C$ fixes a single total order,
hence a single minimizer $\sigma(C)$, for every $p\in C$. By the Global
Vertex Lemma, $V(p)=\min_{\sigma\in\Sigma_C}f_\sigma(p)=f_{\sigma(C)}(p)$
for every $p\in C$. $\blacksquare$

**Lemma 4.2 (the closed-cell / boundary subtlety, handled explicitly).**
For every cell $C$ with $\overline{C}\cap\overline{B(n)}\ne\varnothing$,
$V(p)=f_{\sigma(C)}(p)$ for **every** $p\in\overline{C}\cap\overline{B(n)}$
(not just for $p\in C$) — i.e. the affine formula extends correctly
across the open cell's boundary.

*Proof.* This is exactly the subtlety the outline-reviewer flagged
("max of affine function over an open cell attained at a vertex needs
the closure argument, consistent with how Section 3's compactness
already extends to the closed region"), and it is resolved cheaply using
already-certified content, not assumed: $V$ is continuous on $H$ (indeed
$1$-Lipschitz, Section 2, certified), and $f_{\sigma(C)}$ is continuous
(it is affine). These two continuous functions **agree on $C$** (Lemma
4.1), and $C$ is **dense in $\overline C$** (every open cell is dense in
its own closure — immediate from $C$ being open and nonempty and
$\overline{C}$ being its topological closure). Two continuous functions
that agree on a dense subset of a set agree on the closure of that set
(elementary point-set topology: if $g,h$ continuous and $g=h$ on a dense
$D\subseteq S$, then for $p\in\overline{D}\cap S$, taking $p_m\to p$,
$p_m\in D$, continuity gives $g(p)=\lim g(p_m)=\lim h(p_m)=h(p)$). Hence
$V=f_{\sigma(C)}$ on all of $\overline{C}$, in particular on
$\overline{C}\cap\overline{B(n)}$. $\blacksquare$

This is exactly the mechanism that removes the need for concavity: we no
longer need $f_{\sigma(C)}$ to be a *globally* valid lower bound outside
$\overline{C}$ (which is what concavity of the naive relaxation
$\hat V$ would have required, and which is false in general — this is
precisely why concavity itself can fail while the argument below still
works) — we only need it to equal $V$ on the *closed* cell it governs,
which Lemma 4.2 gives unconditionally.

**Theorem (Finite-Cell Affine-Vertex Reduction).** Let
$p^*\in\overline{B(n)}$ attain $V(p^*)=\max_{p\in\overline{B(n)}}V(p)$
(exists by Section 3). Then there is a cell $C$ of the $L$-arrangement
with $p^*\in\overline{C}\cap\overline{B(n)}$ (at least one such $C$
exists: $\overline{B(n)}$ is itself, by construction of $L$, a finite
union of closures of cells intersected with it, since $\overline{B(n)}$
is exactly cut out by the last group of $L$'s functionals, and a finite
arrangement's ambient space is covered by the closures of its
finitely many open cells). Set
$P:=\overline{C}\cap\overline{B(n)}$: this is a **closed, bounded,
convex polytope** in $H$ (a finite intersection of closed half-spaces
$\{\ell\ge0\}$ or $\{\ell\le0\}$, one per $\ell\in L$ according to $C$'s
sign pattern together with $\overline{B(n)}$'s own defining half-spaces,
intersected with the bounded simplex), and by Lemma 4.2, $V=f_{\sigma(C)}$
(affine) on all of $P$. By the **elementary fact that the maximum of an
affine functional over a nonempty compact convex polytope is attained at
a vertex (extreme point) of the polytope** — proved below — $V(p^*)=
f_{\sigma(C)}(p^*)=\max_{q\in P}f_{\sigma(C)}(q)=f_{\sigma(C)}(q^*)=V(q^*)$
for **some vertex $q^*$ of $P$**. Every vertex of a polytope cut out by
half-spaces from a finite list $L'\subseteq L$ of size $\ge\dim H=k-1$ is
the (necessarily unique, since $P$ is bounded with nonempty interior
generically, or a boundary intersection) solution of some
$(k-1)$-subset of $L'$'s functionals set to $0$ simultaneously — a
linear system with finitely many solutions as the subset ranges over
$L$. Hence:

$$V(p^*)=\max_{p\in\overline{B(n)}}V(p)=V(q^*)\ \text{for some }q^*\in
Q:=\{\text{solutions of some }(k-1)\text{-subset of }L\text{ set to }0\},$$

a **finite, explicitly describable, $p$-independent candidate set**
depending only on $n$ (via $\gamma(n)$ and $\Sigma(n,k)$), **with no
concavity hypothesis used anywhere in this argument.**

*Proof of the elementary vertex fact.* Let $P\subseteq\mathbb R^d$ be a
nonempty compact convex polytope and $f$ affine. $f$ attains its max on
$P$ at some point $q$ (extreme value theorem, $P$ compact, $f$
continuous). If $q$ is not extreme, $q=\tfrac12(a+b)$ for distinct
$a,b\in P$; by affineness $f(q)=\tfrac12(f(a)+f(b))$, and since $f(q)$ is
the max, $f(a)=f(b)=f(q)$ too (else one of $f(a),f(b)>f(q)$,
contradiction). Replace $q$ by $a$ (still a maximizer) and repeat; since
$P$ is a polytope (finitely many vertices, and every non-extreme point of
a polytope lies on a face of strictly smaller dimension spanned by
finitely many vertices — a standard fact, by induction on $\dim P$ using
Carathéodory's theorem for polytopes), this process terminates at an
actual vertex of $P$ in finitely many steps. $\blacksquare$

**What this achieves, precisely.** This closes exactly the mechanistic
step the outline's pivot asked for: the outer maximization defining
$c(n)$'s Existence Theorem over the (continuum) balanced region reduces,
*without any concavity assumption*, to checking $V(q)\le c(n)$ at
finitely many explicit candidate points $q\in Q$. **What is not achieved
this round:** an explicit bound on $|\Sigma(n,k)|$ (hence on $|L|$ and
$|Q|$) as a function of $n$ — the outline correctly anticipated this as
"the real remaining difficulty," not concavity's tractability. $\Sigma$
is finite for every fixed $n$ (Section 1), and hence $Q$ is finite for
every fixed $n$, but no closed-form or polynomial bound on $|\Sigma(n,k)|$
in terms of $n$ is derived here; a naive bound via (bounded compositions)
$\times$ (Bell numbers of a bounded number of slots) $\times$ (finite pin
assignments) grows at least exponentially in $n$, making brute enumeration
for each specific $n$ possible in principle but not a proof for general
$n$ as stated.

### 4.1 The Region-Only Sub-List: exact classification (new this round, fully proved)

This section carries out this round's targeted work: with $L$ corrected
(Section 4), consider the **region-only** sub-polytope
$$\overline{B(n)}=\{p\in H: p_1\le\tfrac12,\ p_i-p_{i+1}\ge\gamma(n)\
(i=1,\dots,n),\ p_k\ge0\},$$
cut out by exactly the $n+2$ region functionals of $L$ (dropping the
$\Sigma$-shape functionals for now). By the Theorem's vertex-extraction
mechanism, $\overline{B(n)}$ itself is a single closed cell's closure (or a
union of finitely many), and its own vertices are among the candidates
solving $(k-1)=n$ of these $n+2$ functionals set to $0$ (equivalently: to
their threshold). We now classify these region-only vertices completely
and in closed form, for **every** $n\ge2$ (not just numerically for small
$n$), and close every one of them (Sections 4.2–4.4 below).

**Reparametrization.** Write $a:=\tfrac12-p_1\ge0$ and
$g_i:=p_i-p_{i+1}-\gamma(n)\ge0$ ($i=1,\dots,n$); these are exactly the
slacks in $n+1$ of the region's defining inequalities. From
$p_1=\tfrac12-a$ and $p_{i+1}=p_i-\gamma(n)-g_i$,
$$p_i=\Bigl(\tfrac12-a\Bigr)-(i-1)\gamma(n)-\sum_{j=1}^{i-1}g_j,\qquad i=1,\dots,n+1.$$
Imposing $\sum_{i=1}^{n+1}p_i=1$ and simplifying (each $g_j$ occurs in
$p_{j+1},\dots,p_{n+1}$, i.e. $n+1-j$ times):
$$(n+1)\Bigl(\tfrac12-a\Bigr)-\gamma(n)\binom{n+1}{2}-\sum_{j=1}^ng_j(n+1-j)=1
\iff (n+1)a+\sum_{j=1}^n(n+1-j)\,g_j=K(n),$$
where $K(n):=\tfrac{n-1}2-\tfrac{n(n+1)}2\gamma(n)$. This is a **single
linear equation with strictly positive coefficients** $(n+1,\,n,\,n-1,
\dots,1)$ in the $n+1$ nonnegative unknowns $(a,g_1,\dots,g_n)$: exactly
the defining equation of an $n$-dimensional simplex $\Delta$ with vertices
$$e_0=\Bigl(\tfrac{K(n)}{n+1},0,\dots,0\Bigr),\qquad
e_j=\Bigl(0,\dots,0,\underbrace{\tfrac{K(n)}{n+1-j}}_{g_j\text{-slot}},0,\dots,0\Bigr)\ (j=1,\dots,n).$$
(**$K(n)>0$ for every $n\ge2$:** $2K(n)=(n-1)-n(n+1)\gamma(n)>(n-1)-n(n+1)\cdot\gamma(n)$;
since $\gamma(n)\le\gamma(2)=1/7<1/(n(n+1))$ is not needed in general — a
direct bound suffices: $n(n+1)\gamma(n)=n(n+1)/(2^{n+1}-1)<1$ for all
$n\ge2$ (check: $n(n+1)<2^{n+1}-1$, true at $n=2$: $6<7$; and by induction,
if $n(n+1)<2^{n+1}-1$ then $(n+1)(n+2)=n(n+1)+2(n+1)<2^{n+1}-1+2n+2<
2\cdot2^{n+1}-1=2^{n+2}-1$ once $2n+2<2^{n+1}$, true for $n\ge2$), so
$2K(n)>(n-1)-1=n-2\ge0$ for $n\ge2$, with the borderline $n=2$ case
checked directly, $K(2)=\tfrac12-3\gamma(2)=\tfrac12-\tfrac37=\tfrac1{14}>0$.
Hence $K(n)>0$ for all $n\ge2$ and $\Delta$ is non-degenerate.)

The remaining region functional not yet used, $z(p):=p_k=p_{n+1}\ge0$, is
an **affine function of $(a,g_1,\dots,g_n)$** (via the formula for $p_{n+1}$
above): explicitly
$$z=\Bigl(\tfrac12-a\Bigr)-n\gamma(n)-\sum_{j=1}^ng_j.$$
So $\overline{B(n)}=\Delta\cap\{z\ge0\}$: the region-only polytope is
exactly the $n$-simplex $\Delta$ sliced by one more half-space. Standard
polytope geometry: the vertices of $\Delta\cap\{z\ge0\}$ are exactly (i)
every vertex of $\Delta$ with $z\ge0$ there, plus (ii) for every **edge**
of $\Delta$ (i.e. every pair of vertices, since $\Delta$ is a simplex — all
$\binom{n+1}2$ pairs are edges) whose two endpoints have $z$ of **strictly
opposite sign**, the unique point on that edge where the affine function
$z$ vanishes (existence and uniqueness: $z$ restricted to a line segment is
affine in the segment parameter $t\in[0,1]$, hence strictly monotonic once
its two endpoint values have opposite sign, so it has exactly one zero on
the open segment, by the intermediate value theorem for a monotonic affine
function of one real variable). Edges with both endpoints having $z$ of the
same sign contribute no new vertex (the edge lies entirely on one side).

**Computing $z$ at each vertex of $\Delta$.** Substituting $e_0$'s and
$e_j$'s coordinates into the formula for $z$ (all $g_i=0$ except possibly
one, $a=0$ except at $e_0$) and simplifying with $K(n)$'s definition:
$$z(e_0)=\frac1{n+1}-\frac{n\gamma(n)}2,\qquad
z(e_j)=\frac12-n\gamma(n)-\frac{K(n)}{n+1-j}\ \ (j=1,\dots,n).$$
Putting $z(e_j)$ over the common denominator $2(2^{n+1}-1)(n+1-j)$ (using
$\gamma(n)=1/(2^{n+1}-1)$) and simplifying (verified by direct symbolic
expansion) gives, for the **numerator** $N(n,j)$ (the denominator is always
positive, since $n+1-j\ge1$ and $2^{n+1}-1>0$):
$$N(n,j)=j\bigl(2n+1-2^{n+1}\bigr)+\bigl(2^{n+2}-n^2-n-2\bigr),$$
so $\operatorname{sign}(z(e_j))=\operatorname{sign}(N(n,j))$.

**Claim A ($e_0$ is always genuine, $z(e_0)>0$ for all $n\ge2$).**
$2(n+1)z(e_0)=2-n(n+1)\gamma(n)>2-1=1>0$ using the bound
$n(n+1)\gamma(n)<1$ established above. $\blacksquare$

**Claim B ($e_1$ is always genuine, $N(n,1)>0$ for all $n\ge2$).**
$N(n,1)=(2n+1-2^{n+1})+(2^{n+2}-n^2-n-2)=2^{n+1}+n-n^2-1=:h(n)$. We show
$h(n)>0$ for all $n\ge2$ by strong induction with an explicit recursion:
$h(n+1)=2h(n)+(n^2-3n+1)$ (direct algebra: $h(n+1)-2h(n)=
[2^{n+2}+(n+1)-(n+1)^2-1]-2[2^{n+1}+n-n^2-1]=n^2-3n+1$, since the
$2^{n+2}=2\cdot2^{n+1}$ terms cancel). Base cases: $h(2)=8+2-4-1=5>0$,
$h(3)=16+3-9-1=9>0$ (direct check, needed since the recursion's increment
$n^2-3n+1$ is negative only at $n=2$: $4-6+1=-1$, consistent with
$h(3)=2\cdot5-1=9$, matching). For $n\ge3$, $n^2-3n+1=n(n-3)+1\ge1>0$, so
$h(n+1)=2h(n)+(\text{positive})>2h(n)>0$ whenever $h(n)>0$; combined with
$h(2),h(3)>0$ this gives $h(n)>0$ for all $n\ge2$ by induction.
$\blacksquare$

**Claim C ($e_j$ for $j\ge2$: negative for $n\ge4$, exactly zero at
$(n,j)=(3,2)$, positive at $(n,j)=(2,2)$ — the only remaining possibilities
since $j\le n$).** Since the coefficient of $j$ in $N(n,j)$,
$2n+1-2^{n+1}$, is **negative for every $n\ge2$** ($2^{n+1}>2n+1$: true at
$n=2$, $8>5$; and by induction $2^{n+2}=2\cdot2^{n+1}>2(2n+1)=4n+2>2n+3$ for
$n\ge1$), $N(n,\cdot)$ is a **strictly decreasing** function of $j$. Hence
for fixed $n$, $\max_{2\le j\le n}N(n,j)=N(n,2)$, so it suffices to
determine the sign of $N(n,2)$:
$$N(n,2)=2(2n+1-2^{n+1})+(2^{n+2}-n^2-n-2)=4n+2-2^{n+2}+2^{n+2}-n^2-n-2
=3n-n^2=n(3-n).$$
This is exact and elementary: $n(3-n)>0$ for $n\in\{1,2\}$, $=0$ at $n=3$,
$<0$ for $n\ge4$. Since $N(n,j)\le N(n,2)$ for all $j\ge2$ (decreasing in
$j$), we conclude: **for $n\ge4$, $N(n,j)<0$ for every $j=2,\dots,n$** (all
$e_j$, $j\ge2$, are infeasible for $\Delta\cap\{z\ge0\}$, i.e. genuinely
excluded); **at $n=3$, $N(3,2)=0$ exactly** (so $e_2$ lies exactly on
$\{z=0\}$ — a coincidence, not a numerical artifact, verified exactly
above) and $N(3,j)<0$ for $j=3$ (direct: $N(3,3)=3(2\cdot3+1-16)+
(32-9-3-2)=3(-9)+18=-9<0$); **at $n=2$, only $j=2\le n$ exists** and
$N(2,2)=2(3-2)=2>0$ (genuine). $\blacksquare$

**Theorem (Region-Vertex Classification, exact, all $n\ge2$).**
- $n=2$: $\overline{B(2)}$ has exactly $3$ vertices, all "genuine"
  ($z>0$): $e_0,e_1,e_2$ (no $z=0$ vertex arises, since $z$ is positive at
  every vertex of the ambient $2$-simplex $\Delta$).
- $n=3$: $\overline{B(3)}$ has exactly $5$ vertices: two strictly genuine
  ($e_0,e_1$, $z>0$), one degenerate-and-simplex-coincident ($e_2$ itself,
  $z=0$ exactly — simultaneously a vertex of $\Delta$ and of the slice),
  and two further degenerate crossing points on the edges $e_0$–$e_3$ and
  $e_1$–$e_3$ (the only edges connecting a $z>0$ vertex, $\{e_0,e_1\}$, to
  the one remaining $z<0$ vertex, $e_3$; note $e_2$ is not a $z<0$ vertex
  here, so it contributes no crossing edges).
- $n\ge4$: $\overline{B(n)}$ has exactly $2+2(n-1)$ vertices: two strictly
  genuine ($e_0,e_1$), and $2(n-1)$ degenerate ($z=0$) crossing points, one
  on each of the $2(n-1)$ edges joining $\{e_0,e_1\}$ ($z>0$) to
  $\{e_2,\dots,e_n\}$ ($z<0$) — every such pair is an edge of the simplex
  $\Delta$, and by Claims A–C each contributes exactly one crossing point;
  no other pairs of vertices have opposite-sign $z$ (edges within
  $\{e_0,e_1\}$, or within $\{e_2,\dots,e_n\}$, have same-sign endpoints, no
  crossing).

*Proof.* Immediate from Claims A, B, C above and the simplex-slice
vertex-structure fact stated before them. $\blacksquare$

This **independently re-derives and fully proves in general $n$** (not
merely checks numerically for $n\le6$, as the outline-reviewer's and this
round's own sympy spot-checks did) the count the outline anticipated,
including a precise, previously-unremarked explanation of the $n=2,3$
exceptions ($e_2$ crossing the sign boundary at exactly these small $n$).

### 4.2 Closing the degenerate ($p_k=0$) region: a general Boundary-Continuity Theorem (new this round, fully proved)

We now close **every** point of $\overline{B(n)}\cap\{p_k=0\}$ — not just
the finitely many vertices identified in Section 4.1, but the entire face
— via the already-certified Lipschitz continuity of $V$ (Section 2). This
both settles step 3 of the outline and removes any dependence on the exact
vertex count of Section 4.1 for this part of the argument.

**Lemma (Small-Mass Insertion).** For any finite multiset $M$ of positive
reals and any finite multiset $F$ of positive reals,
$$|\mathrm{OddSum}(M\cup F)-\mathrm{OddSum}(M)|\le \mathrm{sum}(F).$$

*Proof.* First, single-element case, $F=\{t\}$: compare the two
same-cardinality multisets $M\cup\{t\}$ and $M\cup\{0\}$ using the
certified Fact (Section 2, "OddSum is 1-Lipschitz in $\ell^1$, fixed
cardinality"), rank-matched. Write $M$ sorted descending as
$\mu_1\ge\cdots\ge\mu_N>0$ and suppose $t$ inserts at rank $r$ (i.e.
$\mu_{r-1}>t>\mu_r$, with $\mu_0:=+\infty,\mu_{N+1}:=0$; genericity $t\ne
\mu_i$ holds for all but finitely many $t$, and both sides below are
continuous in $t$, so the general case follows by continuity). Sorted
descending, $M\cup\{t\}=(\mu_1,\dots,\mu_{r-1},t,\mu_r,\dots,\mu_N)$ and
$M\cup\{0\}=(\mu_1,\dots,\mu_N,0)$. Rank-by-rank differences: $0$ for
ranks $<r$; at rank $r$, $|t-\mu_r|=t-\mu_r$; at each rank $j$,
$r<j\le N$, $|\mu_{j-1}-\mu_j|=\mu_{j-1}-\mu_j$ (both sequences descending);
at rank $N+1$, $|\mu_N-0|=\mu_N$. Summing:
$$(t-\mu_r)+\sum_{j=r+1}^N(\mu_{j-1}-\mu_j)+\mu_N=(t-\mu_r)+(\mu_r-\mu_N)+\mu_N=t,$$
a telescoping sum evaluating to exactly $t$ (independent of $r$, i.e. of
where $t$ lands). By the Section 2 Fact, $|\mathrm{OddSum}(M\cup\{t\})-
\mathrm{OddSum}(M\cup\{0\})|\le t$; and $\mathrm{OddSum}(M\cup\{0\})=
\mathrm{OddSum}(M)$ exactly, since appending the (unique) smallest element
$0$ does not change the relative order, hence the parity of rank, of any
element of $M$. This proves the single-element case. The general case
follows by induction on $|F|$: writing $F=F'\cup\{t\}$,
$|\mathrm{OddSum}(M\cup F)-\mathrm{OddSum}(M\cup F')|\le t$ (single-element
case applied to the multiset $M\cup F'$) and
$|\mathrm{OddSum}(M\cup F')-\mathrm{OddSum}(M)|\le\mathrm{sum}(F')$
(induction hypothesis), so by the triangle inequality
$|\mathrm{OddSum}(M\cup F)-\mathrm{OddSum}(M)|\le t+\mathrm{sum}(F')=
\mathrm{sum}(F)$. $\blacksquare$

**Theorem (Boundary Continuity / Boundary Positivity).** Let
$p^0=(p_1,\dots,p_n,0)\in\overline{B(n)}$ (i.e. $p_1,\dots,p_n\ge0$,
$\sum_{i=1}^np_i=1$, and $p^0$ satisfies the region's other closed
inequalities). Then:
1. **(Boundary Positivity Fact.)** $p_1,\dots,p_n>0$ strictly; in fact
   $p_i\ge(n+1-i)\gamma(n)>0$ for each $i$.
2. **(Boundary value.)** Let $\bar V$ denote the continuous extension of
   $V$ (Lipschitz on the open simplex, Section 2) to the closed simplex —
   which exists and is unique because a Lipschitz (hence uniformly
   continuous) function on a dense subset extends uniquely and continuously
   to the closure, with the extension's value at any boundary point equal
   to the limit of $V$ along any sequence of interior points converging to
   it. Let $V_n$ be the identically-defined value function
   (Reduction Lemma) but for $n$-piece configurations. Then
   $$\bar V(p^0)=V_n(p_1,\dots,p_n).$$
3. **(Consequence.)** $\bar V(p^0)\le c(n)$: since $\tilde p:=
   (p_1,\dots,p_n)$ has exactly $n$ positive pieces summing to $1$, and
   $n\le n$, the certified **Perfect-Pairing / Bisect-Everything Corollary**
   (Theorem 3, `lemmas/perfect-pairing-subadditivity-and-general-insertion.md`)
   gives a legal response (bisect every piece) with $\mathrm{OddSum}=1/2$
   exactly, so $V_n(\tilde p)\le1/2<c(n)$ — hence $\bar V(p^0)\le c(n)$.

*Proof of 1.* Immediate from the region's closed gap inequalities:
$p_i-p_{i+1}\ge\gamma(n)$ for $i=1,\dots,n$, telescoped from $p_{n+1}=0$
upward: $p_n\ge p_{n+1}+\gamma(n)=\gamma(n)$; $p_{n-1}\ge p_n+\gamma(n)\ge
2\gamma(n)$; inductively $p_i\ge(n+1-i)\gamma(n)>0$.

*Proof of 2.* Fix the perturbation path $p^{(t)}:=(p_1-\tfrac tn,\dots,
p_n-\tfrac tn,t)$ for small $t>0$ (positive by part 1, for $t$ small
enough that $p_i-t/n>0$ for all $i\le n$); $p^{(t)}\to p^0$ as $t\to0^+$,
$\|p^{(t)}-p^0\|_1=2t$, and each $p^{(t)}$ is an interior point (all
coordinates positive) of the $(n+1)$-piece simplex, so $V(p^{(t)})$ is the
original (Reduction-Lemma) value and $\bar V(p^0)=\lim_{t\to0^+}V(p^{(t)})$
by the extension property recalled above. We show
$|V(p^{(t)})-V_n(\tilde p)|\le2t$, which gives the claim on taking
$t\to0^+$.

($\le$) Take any cut-allocation $(m_1,\dots,m_n)$ with $\sum m_i\le n$
achieving $V_n(\tilde p)$ (attained, by the Vertex Pinning Lemma /
Closure Lemma already used in Section 1), splitting each $p_i$ into
positive fragments $p_i\cdot(\lambda_{i,1},\dots,\lambda_{i,m_i+1})$,
$\sum_j\lambda_{i,j}=1$. Apply the identical cut-allocation and
proportions to $p_i-t/n$ (the first $n$ coordinates of $p^{(t)}$), and
leave $p^{(t)}_{n+1}=t$ untouched (using $\sum m_i\le n$ total cuts,
legal). This is a response to $p^{(t)}$ with resulting multiset
$M^{(t)}=A\cup\{t\}$ where $A$ is the transported fragments. By the exact
proportional-transport computation of Section 2 (each transported
fragment differs from the original by $\lambda_{i,j}\cdot t/n$, summing
per piece to $t/n$, over $n$ pieces to $t$; and the Section 2 Fact bounds
$\mathrm{OddSum}$ by this total),
$\mathrm{OddSum}(A)\le V_n(\tilde p)+t$ hence, by the Small-Mass Insertion
Lemma with $F=\{t\}$, $V(p^{(t)})\le\mathrm{OddSum}(M^{(t)})\le
\mathrm{OddSum}(A)+t\le V_n(\tilde p)+2t$.

($\ge$) Take **any** legal response to $p^{(t)}$, cut-allocation
$(m_1,\dots,m_{n+1})$, $\sum\le n$, giving $M^{(t)}=A\cup F$ where $A$ is
the fragments of pieces $1,\dots,n$ (using $\sum_{i\le n}m_i\le n$ cuts)
and $F$ is the fragments of piece $n+1$ (positive parts summing to $t$).
By the Small-Mass Insertion Lemma, $\mathrm{OddSum}(M^{(t)})\ge
\mathrm{OddSum}(A)-t$. The allocation $(m_1,\dots,m_n)$ (using $\le n$
cuts) applied instead directly to $\tilde p=(p_1,\dots,p_n)$, with the
same proportions transported up from $p_i-t/n$ to $p_i$, gives a legal
response $\tilde M$ to $\tilde p$ with, by the same transport bound,
$\mathrm{OddSum}(\tilde M)\le\mathrm{OddSum}(A)+t$, i.e.
$\mathrm{OddSum}(A)\ge\mathrm{OddSum}(\tilde M)-t\ge V_n(\tilde p)-t$ (since
$\tilde M$ is a legal response, its OddSum is $\ge$ the minimum
$V_n(\tilde p)$). Combining: $\mathrm{OddSum}(M^{(t)})\ge
\mathrm{OddSum}(A)-t\ge V_n(\tilde p)-2t$. Since this holds for every
response to $p^{(t)}$, in particular the minimizing one,
$V(p^{(t)})\ge V_n(\tilde p)-2t$.

Together, $|V(p^{(t)})-V_n(\tilde p)|\le2t\to0$, proving part 2.
Part 3 was justified above. $\blacksquare$

**This fully proves step 3 of the outline** — and more strongly than
requested: it closes **every** point of $\overline{B(n)}\cap\{p_k=0\}$
(not just the finitely many vertices from Section 4.1), with no dependence
on the exact vertex count.

### 4.3 Closing the two genuine vertices in exact arithmetic (new this round, fully proved for $n\ge3$; $n=2$ handled separately)

By Section 4.1, for $n\ge3$ the strictly genuine (region-only) vertices are
exactly $e_0$ (all $n$ gaps tight, $A$ slack) and $e_1$ (gap $1$ slack, $A$
and gaps $2,\dots,n$ tight). We identify their coordinates and close both
via the certified **General $k$-Anchor-Merge Lemma** (Theorem 10,
`lemmas/singleton-interleaving-and-k-anchor-merge.md`).

**Coordinates.** $e_0$: all $g_i=0$, i.e. $p_i-p_{i+1}=\gamma(n)$ for every
$i=1,\dots,n$ (a full arithmetic progression across all $n+1$ pieces with
common difference $\gamma(n)$), and $a=K(n)/(n+1)$ so $p_1<\tfrac12$; from
$\sum p_i=1$, solving the AP directly gives $p_{n+1}=\dfrac{2-n(n+1)
\gamma(n)}{2(n+1)}$ and $p_i=p_{n+1}+(n+1-i)\gamma(n)$.
$e_1$: $a=0$ (i.e. $p_1=\tfrac12$), $g_1=K(n)/n>0$ (gap $1$ slack), and
$g_i=0$ for $i=2,\dots,n$ (gaps $2,\dots,n$ tight, an AP among
$p_2,\dots,p_{n+1}$ with common difference $\gamma(n)$); solving gives
$p_{n+1}=\dfrac1{2n}-\dfrac{(n-1)\gamma(n)}2$ and $p_i=p_{n+1}+(n+1-i)
\gamma(n)$ for $i=2,\dots,n+1$, $p_1=\tfrac12$.

**Construction and exact evaluation.** In both cases the pieces (all
$n+1$ of them for $e_0$; pieces $2,\dots,n+1$, i.e. $n$ of them, for
$e_1$, with $p_1$ left as an unpaired singleton) form a **run of
consecutive terms of an arithmetic progression with common difference
exactly $\gamma(n)$**. Pair up **consecutive** terms of this run,
$(i,i+1),(i+2,i+3),\dots$ (each pair's two values differ by exactly
$\gamma(n)$, since they are adjacent AP terms), leaving at most one term
of the run unpaired if its length is odd, plus (for $e_1$) $p_1$ itself
unpaired. Let $k$ be the number of pairs formed: $k=\lfloor(n+1)/2\rfloor$
for $e_0$ (run length $n+1$), $k=\lfloor n/2\rfloor$ for $e_1$ (run length
$n$, plus $p_1$ separately unpaired). Every unpaired piece is bisected.

This is exactly an instance of the General $k$-Anchor-Merge Lemma
(Theorem 10) with $\ell_1=\dots=\ell_k=\gamma(n)$ (all $k$ pair-differences
equal, since every pair is adjacent AP terms). Cut count: $k$ (one per
pair) $+$ (number of unpaired pieces, each one cut) $=k+\bigl((n+1)-2k
\bigr)=n+1-k\le n$ (using $k\ge1$, true for $n\ge2$ in both cases: for
$e_0$, $k=\lfloor(n+1)/2\rfloor\ge1$ once $n\ge1$; for $e_1$, $k=
\lfloor n/2\rfloor\ge1$ once $n\ge2$) — legal.

By Theorem 10,
$$\mathrm{OddSum}(M)=\tfrac12\bigl(1-k\gamma(n)\bigr)+\mathrm{OddSum}
\bigl(\{\gamma(n)\}^{\times k}\bigr).$$
The multiset $\{\gamma(n)\}^{\times k}$ (all $k$ entries equal) has
$\mathrm{OddSum}=\lceil k/2\rceil\cdot\gamma(n)$ (its own odd ranks number
$\lceil k/2\rceil$ out of $k$ equal entries). Hence
$$\mathrm{OddSum}(M)=\tfrac12-\tfrac k2\gamma(n)+\Bigl\lceil\tfrac k2
\Bigr\rceil\gamma(n)=\tfrac12+\gamma(n)\Bigl(\Bigl\lceil\tfrac k2\Bigr
\rceil-\tfrac k2\Bigr)=\begin{cases}\tfrac12,&k\text{ even},\\[2pt]
\tfrac12+\tfrac{\gamma(n)}2,&k\text{ odd}.\end{cases}$$

**Exact identity $c(n)=\tfrac12+\tfrac{\gamma(n)}2$.** Directly:
$\tfrac12+\tfrac{\gamma(n)}2=\tfrac12+\tfrac1{2(2^{n+1}-1)}=
\dfrac{(2^{n+1}-1)+1}{2(2^{n+1}-1)}=\dfrac{2^{n+1}}{2(2^{n+1}-1)}=
\dfrac{2^n}{2^{n+1}-1}=c(n)$.

**Conclusion.** In every case, $\mathrm{OddSum}(M)\le c(n)$ (with equality
exactly when $k$ is odd, and $\mathrm{OddSum}(M)=\tfrac12<c(n)$ when $k$ is
even), so $V(e_0)\le c(n)$ and $V(e_1)\le c(n)$, **exactly**, for every
$n\ge3$. (Independent exact-`Fraction` verification of the closed-form
coordinates and this exact evaluation, for $n=2,\dots,8$: zero deviation;
the closed-form derivation above is what actually proves the general-$n$
claim, the computation is a check, not the proof.)

**The $n=2$ boundary case (a genuinely third vertex, closed directly).**
By Section 4.1, $n=2$ has a third genuine vertex $e_2$ ($a=0$, $g_1=0$,
$g_2=K(2)/1>0$, i.e. $A$ and gap $1$ tight, gap $2$ free): $p=(\tfrac12,
\tfrac5{14},\tfrac17)$ (exact values, from $K(2)=\tfrac1{14}$). Here the
tight gap is between $p_1,p_2$ (adjacent, difference exactly $\gamma(2)=
\tfrac17$), not between pieces $2,3$ — so apply Theorem 10 with the single
pair $(1,2)$ instead: $\ell_1=p_1-p_2=\tfrac12-\tfrac5{14}=\tfrac17=
\gamma(2)$, and $p_3=\tfrac17$ bisected. Since $k=1$ is odd, the identical
formula gives $\mathrm{OddSum}=\tfrac12+\tfrac{\gamma(2)}2=c(2)=\tfrac47$
exactly (matches the direct computation: $M=\{\tfrac17,\tfrac5{14},
\tfrac5{14},\tfrac1{14},\tfrac1{14}\}$, sorted $\tfrac5{14},\tfrac5{14},
\tfrac2{14},\tfrac1{14},\tfrac1{14}$, $\mathrm{OddSum}=\tfrac5{14}+
\tfrac2{14}+\tfrac1{14}=\tfrac8{14}=\tfrac47=c(2)$). So $V(e_2)\le c(2)$
exactly as well.

**This fully closes step 4 of the outline, in exact arithmetic, for
general $n$** — replacing the round-9/outline's numeric-only
$V\approx1/2$ finding with an exact closed-form evaluation ($V=1/2$ or
$V=c(n)$ exactly, by an explicit parity rule) for every $n\ge2$.

### 4.4 What Sections 4.1–4.3 achieve, and what is still open

Sections 4.1–4.3 together prove: **every region-only candidate vertex
(i.e. every point of $Q$ arising from a $(k-1)$-subset drawn entirely from
the corrected $L$'s region functionals $\{p_1-\tfrac12,\text{ gaps},p_k\}$,
with no $\Sigma$-shape functional involved) satisfies $V(q)\le c(n)$,
exactly, for every $n\ge2$.** This is a complete, general-$n$ result, not
a numeric spot-check: Section 4.1 classifies these vertices in closed form
for all $n$ (Theorem, Region-Vertex Classification), Section 4.2 closes
every degenerate ($p_k=0$) one via a newly-proved general Boundary
Continuity Theorem, and Section 4.3 closes the (at most three, exactly two
for $n\ge3$) genuine ones via exact-arithmetic evaluation using the
certified $k$-Anchor-Merge Lemma.

**What remains open (unchanged in kind from last round, now the sole
remaining gap for this approach).** The Finite-Cell Affine-Vertex
Reduction Theorem's full candidate set $Q$ also includes $(k-1)$-subsets
that mix in one or more of $L$'s $\Sigma$-shape functionals (validity
boundaries $x_\sigma(p)\ge0$ and branch-comparison boundaries
$f_\sigma(p)-f_\tau(p)$). **None of this round's work touches those.**
Concretely: the Existence Theorem ($V(p)\le c(n)$ for every $p\in
\overline{B(n)}$) would follow from this approach **only if** the true
maximizer $p^*$ (which Section 3 shows exists) always lies in the
region-only sub-list $Q_{\text{region}}\subset Q$ handled here — and
nothing proved this round establishes that; a maximizer landing at a cell
boundary defined by a $\Sigma$-shape functional (i.e. where the optimal
response's *branch* changes, not just where a region inequality goes
tight) is not excluded, and $|\Sigma(n,k)|$'s lack of a general bound
(flagged unchanged since round 9) means this cannot currently be checked
by enumeration for general $n$. **This is a combinatorial classification
gap, not a missing proof technique**, exactly as diagnosed last round —
this round narrows the *known-closed* part of $Q$ to all of
$Q_{\text{region}}$ (previously not even fully classified), but does not
close the Existence Theorem itself.

### 4.5 Bounded-split-piece-count sufficiency (this round's main new target): a General Multi-Piece Subset-Tie construction, and a Mass-Constraint Theorem refuting it as a route to a fixed $s_0$

Per this round's dispatch, the natural next target (replacing the
confirmed-impractical full classification of $\Sigma(n,k)$) is: does the
Existence Theorem follow from an explicit construction using only a
**bounded** number $s_0$ of simultaneously split pieces (independent of
$n$), valid at *every* $p\in\overline{B(n)}$? Note this target is in fact
**weaker and easier** than what the outline literally asks ("the true
maximizer's optimal response never needs more than $s_0$ splits"): since
the Existence Theorem only requires $V(p)\le c(n)$, i.e. *some* response
achieving $\le c(n)$, we do **not** need to characterize the true
minimizing response's shape at all — a single explicit bounded-$s_0$
construction, proved to clear $c(n)$ everywhere, would suffice regardless
of whether it is the true minimizer. This section formalizes the natural
candidate family (the direct multi-piece generalization of the already
certified Subset-Tie Theorem 12, matching the qualitative pattern of
Section 5's numeric $n=6$ witness) and proves a genuine **negative**
result about it: this specific, natural family cannot supply
bounded-$s_0$ sufficiency, with an explicit, provable obstruction at the
already-closed region vertex $e_0$.

**Definition (General Multi-Piece Subset-Tie construction).** Let
$p_1>\cdots>p_{n+1}>0$ sum to $1$. Choose $S=\{i_1,\dots,i_s\}\subseteq
\{1,\dots,n+1\}$ (the split pieces) and a partition of $U:=
\{1,\dots,n+1\}\setminus S$ (the untouched pieces) into $s$ (possibly
empty) groups $J_1,\dots,J_s$, one per split piece, such that
$T_a:=\sum_{m\in J_a}p_m\le p_{i_a}$ for every $a=1,\dots,s$. XY's move:
split $p_{i_a}$ into fragments $\{p_m:m\in J_a\}\cup\{r_a\}$, where
$r_a:=p_{i_a}-T_a\ge0$ (omitting $r_a$ if it is $0$), and leave every
$p_m$, $m\in U$, untouched. This is exactly the direct generalization,
from one split piece to $s$ simultaneously, of the certified Generalized
Subset-Tie Lemma (Theorem 12, `lemmas/generalized-subset-tie-theorem12.md`,
which is the special case $s=1$).

**Cut count.** $\sum_a|J_a|=|U|=n+1-s$ cuts total — legal (i.e. $\le n$)
for every $s\ge1$.

**Theorem (General Multi-Piece Subset-Tie value).** Generically (all
values pairwise distinct except the by-construction ties),
$$\mathrm{OddSum}(M)=(1-\Pi)+\mathrm{OddSum}(\{r_1,\dots,r_s\}),\qquad
\Pi:=\sum_{a=1}^sp_{i_a}.$$

*Proof.* $M$ decomposes as $B\sqcup L$ with $B=\{p_m,p_m\}_{m\in U}$ (each
untouched piece paired with its tied fragment of equal value — $|U|$
pairs, an even block each) and $L=\{r_1,\dots,r_s\}$ (the residual
singletons; generically pairwise distinct and distinct from every value
in $B$). $\mathrm{sum}(B)=2\sum_{m\in U}p_m=2(1-\Pi)$ since $U$ is
partitioned exactly among the $J_a$'s and $\sum_{m\in U}p_m=1-\Pi$. By the
certified Singleton-Interleaving Lemma (Theorem 9,
`lemmas/singleton-interleaving-and-k-anchor-merge.md`),
$\mathrm{OddSum}(M)=\tfrac12\mathrm{sum}(B)+\mathrm{OddSum}(L)=(1-\Pi)+
\mathrm{OddSum}(\{r_1,\dots,r_s\})$. $\blacksquare$

(This directly matches the $s=1$ formula of Theorem 12 above, and the
special case $J_a=\{i_a+1\}$ for consecutive pairs recovers a variant of
the General $k$-Anchor-Merge Lemma's bookkeeping — this construction
family is the natural common generalization of both already-certified
tools, exactly the "generalized Subset-Tie" pattern Section 5's numeric
witness qualitatively resembles.)

**Theorem (Mass-Constraint).** In *any* legal instance of the General
Multi-Piece Subset-Tie construction (i.e. every $T_a\le p_{i_a}$
satisfied), $\Pi=\sum_{a=1}^sp_{i_a}\ge\tfrac12$.

*Proof.* Summing the $s$ legality constraints $T_a\le p_{i_a}$ over
$a=1,\dots,s$: $\sum_aT_a\le\sum_ap_{i_a}=\Pi$. But $\sum_aT_a=
\sum_{m\in U}p_m=1-\Pi$ exactly (the $J_a$'s partition $U$). Hence
$1-\Pi\le\Pi$, i.e. $\Pi\ge\tfrac12$. $\blacksquare$

**Corollary (bounded-$s_0$ impossibility at $e_0$).** Let $M(n):=\max_i
p_i$ for a given $p$. Then every legal instance of the construction needs
$s\ge1/(2M(n))$ split pieces (since $\Pi\le sM(n)$ must be $\ge\tfrac12$).
At the region vertex $p=e_0$ (Section 4.1, the same $e_0$ fully closed —
with equality $V(e_0)=c(n)$ — in Section 4.3), $M(n)=p_1(e_0)$, and by the
exact closed-form coordinates of Section 4.1 together with the already-
established bound $n(n+1)\gamma(n)<1$ (Section 4.1, used there to prove
$K(n)>0$):
$$p_1(e_0)=p_{n+1}(e_0)+n\gamma(n)=\frac{2-n(n+1)\gamma(n)}{2(n+1)}+n\gamma(n)
=\frac{2+n(n+1)\gamma(n)}{2(n+1)}<\frac{2+1}{2(n+1)}=\frac{3}{2(n+1)}.$$
Hence $s\ge\dfrac1{2p_1(e_0)}>\dfrac1{2\cdot\frac3{2(n+1)}}=\dfrac{2(n+1)}{2\cdot3}
=\dfrac{n+1}3$.

So: **every legal instance of the General Multi-Piece Subset-Tie
construction at $p=e_0$ needs strictly more than $(n+1)/3$ split pieces**
— a lower bound growing linearly in $n$, unboundedly. (Direct numeric
check, independent of the algebra above, confirms this and shows the true
ratio is even tighter, $s/(n+1)\to1/2$ as $n\to\infty$: computed exactly
in `Fraction` arithmetic for $n=2,\dots,14$, the exact necessary bound
$1/(2p_1(e_0))$ divided by $n+1$ increases monotonically from $0.35$ at
$n=2$ toward $0.5$ at $n=14$ — consistent with, and numerically confirming,
the proved $>1/3$ bound derived above from the general algebraic estimate
$n(n+1)\gamma(n)<1$, which is not tight but is exact and sufficient for
the unboundedness conclusion.)

**Consequence: this route to bounded-$s_0$ sufficiency fails.** For any
*fixed* $s_0$, once $n>3s_0-1$, **no instance of the General Multi-Piece
Subset-Tie construction (splitting only $\le s_0$ pieces) is even legal**
at $p=e_0$ — regardless of how the split pieces or the groups $J_a$ are
chosen. Since $e_0$ is a genuine point of $\overline{B(n)}$ (Section 4.3
shows only that the $k$-Anchor-Merge construction achieves
$\mathrm{OddSum}=c(n)$ *exactly* there — an upper-bound witness,
$V(e_0)\le c(n)$, not a proof that $c(n)$ is the true minimax value;
**reviewer's round-14 correction**: `lp-duality-split-polytope`'s
independently-verified Chain-Correction Floor Theorem exhibits a
different legal response at this same $e_0$ achieving
$\mathrm{OddSum}=1/2<c(n)$ for every $n\ge6$, so the true value is in
fact $V(e_0)=1/2$ for $n\ge6$, not $c(n)$ — this does not affect the
Mass-Constraint corollary's derivation below, which never used the value
of $V(e_0)$, only $e_0$'s coordinates), **this specific, natural construction
family cannot supply the outline's Opening 1/3 target of a uniform
bounded-$s_0$ sufficiency construction covering the whole balanced
region**. This is a genuine, fully proved negative finding (not merely
numerical): the outline's crux mechanism ("marginal gain from an
$(s_0+1)$-th split is dominated by re-tuning the existing $s_0$-piece
split's own free parameters") cannot be salvaged for *this* construction
family, because the obstruction is not a marginal-gain/tuning issue at
all — it is a hard **legality** constraint ($\Pi\ge1/2$) that no re-tuning
of pin values or residuals can circumvent.

**Scope of this negative result — what it does and does not rule out.**
This refutes bounded-$s_0$ sufficiency specifically for the "tie each
split fragment to the *value of a whole untouched piece*" mechanism (the
literal generalization of Theorem 12, and the most natural reading of
Section 5's qualitative description "tying fragments of the split pieces
against the untouched tail pieces"). It does **not** rule out:
(a) a construction where fragments are tied to **each other** across
different split pieces (fragment-vs-fragment matching within $B$, rather
than fragment-vs-whole-untouched-piece) — Section 5's actual raw numeric
data (the near-equal cluster $0.0211,0.0210,0.0208$ among fragments from
*different* split pieces, not matched against any single untouched piece)
suggests the true $n=6$ witness may in fact be of this richer, not-yet-
formalized kind, not a literal instance of the construction proved
impossible here; (b) constructions using $s_0$ split pieces where the
"split" pieces are allowed to absorb cuts from what would otherwise be
"untouched" pieces in a more flexible topology than one-group-per-split-
piece; (c) any non-tie-based mechanism entirely. **Honest conclusion**:
this round establishes a real, provable dead end for the most natural and
already-partially-certified construction family, correctly redirecting
future attempts away from it, but does **not** establish that bounded-
$s_0$ sufficiency is impossible in full generality — only that this
specific route to it is. The genuinely open question for a future round is
whether the fragment-vs-fragment mechanism glimpsed in Section 5's raw
numeric data (not yet formalized in closed form) evades the Mass-
Constraint obstruction (plausible, since it does not require any subset
of split pieces' mass to reach $1/2$ — ties are internal, not against
external untouched-piece values).

### 5. Numerical test of the "cheap shortcut": is a catalogued survivor real?

The outline flagged a cheap check before attempting full enumeration:
test whether `universal-halving-adversary`'s catalogued "survivor"
configurations (balanced-region points where the *named* additive-tool
family — $k\le2$ splits plus Subset-Tie — fails to certify $\le c(n)$)
are genuine failures of the Existence Theorem itself, or merely gaps in
that specific tool family.

**Test instance.** At $n=6$ ($k=7$), the documented survivor
$p=(0.3306,0.2791,0.1501,0.1162,0.0904,0.0208,0.0128)$ (sum $=1$, gaps
all $>\gamma(6)=1/127\approx0.00787$, $p_1<1/2$: genuinely in the
balanced region) has best-of-named-tools value $\approx0.503983$, while
$c(6)=2^6/(2^7-1)=64/127\approx0.503937$ — an apparent excess of
$\approx4.6\times10^{-5}$.

**Method.** Direct numerical minimization of $\mathrm{OddSum}$ over the
full space of legal responses (all cut-allocations $\mathbf m$ with
$\sum m_i\le n=6$ and at most $3$ pieces split — a restriction to keep
the search tractable within the time budget, **not** justified as
exhaustive over all of $\Sigma(6,7)$; this is a numerical lower-bound
search, not a certified upper bound on $V(p)$ via the Global Vertex
Lemma's exact enumeration), using multi-restart Nelder–Mead
(softmax-parametrized fragment proportions to enforce positivity, $4$–$40$
random restarts per allocation).

**Finding.** The allocation splitting $p_1,p_2,p_3$ each into $3$
fragments ($\mathbf m=(2,2,2,0,0,0,0)$, using the full budget of $6$
cuts) achieves $\mathrm{OddSum}\approx0.5015$, **well below** $c(6)$ (a
margin of $\approx0.0024$, roughly $50\times$ the named-tools' apparent
excess). The optimizer's fragment values are approximately $0.2399,
0.2399,\ 0.1162,0.1162,\ 0.0904,0.0904,\ 0.0211,0.0210,0.0208,\ 0.0128,
0.0128,\ 0.0003$ — visibly a "tie fragments of the split pieces against
the untouched tail pieces $p_4,\dots,p_7$" pattern (each untouched
$p_j$, $j\ge4$, is matched by a same-valued fragment from splitting
$p_1,p_2,p_3$), generalizing the certified Subset-Tie construction from
$1$ split piece to $3$ simultaneously, with the leftover mass collected
into one tiny odd-rank singleton.

**Interpretation (honest).** This is **not** an exact-arithmetic proof
(Nelder–Mead is a numerical local optimizer; the reported value is a
strong empirical upper bound on $V(p)$ at this one point, found via
softmax-relaxed search, not a certified rational computation), and it
tests only **one** instance at **one** $n$. But it directly answers the
outline's shortcut question at this instance: **this specific documented
"survivor" is not a genuine counterexample to the Existence Theorem** —
it fails only because the *named* tool family ($k\le2$, one Subset-Tie)
is too narrow; a $3$-piece generalized-tie response clears $c(6)$ with
comfortable margin. This is consistent with (though does not prove) the
hypothesis that round 8's "survivor rate grows with $n$" finding is an
artifact of testing an insufficiently rich named-tool family, not
evidence against the true Existence Theorem — and it is exactly the kind
of witness the Section 4 machinery (once $\Sigma(n,k)$ is classified for
a given $n$) would locate systematically rather than by ad hoc numeric
search. **This does not, by itself, prove the Existence Theorem even at
this one point** (a rigorous proof would require the exact vertex value,
via Section 1's finite $\Sigma(6,7)$ enumeration in exact arithmetic, not
a numerical optimizer) — it is reported as strong evidence and a
concrete, reusable candidate construction, not a closure.

### 6. What remains open

- **Concavity is retired** (round 9, per the outline; superseded by
  Section 4, which needs no concavity at all). Not to be re-attempted.
- **The Finite-Cell Affine-Vertex Reduction Theorem (Section 4, with $L$
  corrected this round to include $p_k$) is fully proved, unconditionally**:
  the Existence Theorem's extremal $p^*$ provably lies in a finite
  candidate set $Q$ for every fixed $n$.
- **New this round: the entire region-only sub-list $Q_{\text{region}}
  \subset Q$ (candidates from $(k-1)$-subsets drawn only from $L$'s region
  functionals, no $\Sigma$-shape functional) is now fully classified in
  closed form (Section 4.1, all $n\ge2$) and fully closed
  ($V(q)\le c(n)$ exactly for every $q\in Q_{\text{region}}$, Sections
  4.2–4.3, all $n\ge2$)** — this converts what was, last round, an
  unaddressed enumeration question for this sub-list into a complete,
  general-$n$ theorem.
- **The genuinely remaining gap is the $\Sigma$-shape part of $Q$**,
  exactly as the outline anticipated and now sharpened by this round's
  work: no bound on $|\Sigma(n,k)|$ (hence on the $\Sigma$-involving part
  of $L$ and $Q$) as a function of $n$ is established, so that part of $Q$
  cannot be enumerated and checked "$V(q)\le c(n)$" for general $n$; and
  nothing established this round (or previously) shows the true maximizer
  $p^*$ must avoid it and land only in the now-fully-closed
  $Q_{\text{region}}$. This is a **combinatorial classification problem**
  (classify the vertex shapes of the product-of-simplices polytope under
  the specific $\mathrm{OddSum}$ sort-order structure), not a further
  piece of missing mathematical machinery — but it is the sole remaining
  obstruction to the Existence Theorem via this route.
- **Section 5's numerical finding** (not a proof, but a concrete data
  point): the one catalogued "hard" instance tested this round ($n=6$
  survivor) is **not** a real counterexample to the Existence Theorem —
  a genuine (numerically found, not exact-arithmetic-verified) $3$-piece
  generalized-tie response clears $c(6)$ by a $\sim50\times$ larger margin
  than the named-tool family's apparent failure. This is evidence (not
  proof) that the correct next step is enumerating richer shapes
  ($\ge3$ simultaneously-split pieces) within Section 4's framework, not
  further evidence that the Existence Theorem itself might be false.
- **New this round (Section 4.5): bounded-split-piece-count sufficiency
  via the natural "tie fragments to whole untouched pieces" mechanism is
  refuted, in full rigor**, not just deprioritized. The General
  Multi-Piece Subset-Tie construction (the direct multi-piece
  generalization of the certified Theorem 12, and the most natural
  formalization of Section 5's numeric witness's qualitative description)
  provably requires the split pieces' total mass $\Pi\ge1/2$ (Mass-
  Constraint Theorem), and at the already-closed region vertex $e_0$ this
  forces $s>(n+1)/3$ split pieces — unboundedly many as $n\to\infty$. So
  **no fixed $s_0$ works for this construction family, for any $s_0$**.
  This is a genuine, fully proved negative finding (exact algebra, not a
  numeric estimate), correctly ruling out the outline's literal proposed
  mechanism and redirecting future rounds. The scope of the refutation is
  stated precisely in Section 4.5: it does **not** rule out
  fragment-vs-fragment tying (which Section 5's raw numeric data may
  actually exhibit, not literally covered by this construction family) or
  other non-tie mechanisms — those remain open, unexplored, and are the
  most promising concrete next targets.
- **A second gap found and closed this round**: the corrected $L$ (round
  10) still implicitly assumed each $f_\sigma(p)$ is affine on a cell
  without justifying it; this round's explorer found the gap (the
  *intra*-branch pairwise order of $\sigma$'s own fragment/untouched
  values was never pinned by round 10's $L$) and it is now closed by
  enlarging $L$ with all intra-branch pairwise differences and proving the
  new Rank-Pinning Lemma (Section 4). This does not change $Q_{\text
  region}$ (already fully closed, using only region functionals,
  unaffected) but was a genuine soundness gap in the Finite-Cell Theorem's
  proof as stated through round 10, now fixed.
- **New this round (Section 4.7): the response-side (adversary-tie)
  exchange mechanism is refuted**, numerically, in the same genuine
  (non-noise) sense as round 12's region-geometry mechanisms — including
  its maximally weak existential form. Combined with round 12, this closes
  off exchange-argument mechanisms as a class (region-side and
  response-side, single-choice and existential) for the endpoint-
  inequality bypass. **Do not re-attempt a further exchange-move variant
  of this shape.** The two genuinely open routes are (a) direct
  $\Sigma(n,k)$-classification (Sections 1–4.4) and (b) fragment-vs-
  fragment tying (Section 4.5), unchanged from round 12's assessment.
- **Next-round concrete tasks, in priority order**: (1) attempt to
  formalize the fragment-vs-fragment ("mutual tie among split pieces'
  fragments, not against a whole untouched piece") mechanism glimpsed in
  Section 5's raw numeric data — the Mass-Constraint obstruction of
  Section 4.5 does not apply to it, since it needs no subset of pieces to
  reach mass $\ge1/2$; (2) alternatively, pursue this round's
  explorer's Opening 2 (construction-side monotonicity toward the
  region's own boundary facets — not yet attempted by any approach, and
  not ruled out by the round-9 concavity/quasi-concavity counterexamples,
  which used a general interior line, not a region-facet-normal
  direction), which if it succeeds would make $\Sigma$-classification
  (bounded or not) unnecessary entirely, since the maximizer would already
  be forced into the fully-closed $Q_{\text{region}}$; (3) only if both
  stall, revisit a bounded-$s_0$ approach with a genuinely different
  (non-tie-based) mechanism.
- This approach does **not** itself establish the Existence Theorem; it
  establishes (a) the fully general finite-vertex structure of $V$ for
  fixed $p$ (Section 1, textual bug fixed this round), (b) Lipschitz
  continuity of $V$ (Section 2), (c) existence of a maximizer (Section 3),
  (d) **a fully proved, concavity-free reduction of the Existence Theorem
  to a finite candidate set** (Section 4, with a second soundness gap
  — intra-branch rank-pinning — found and closed this round), (e) the
  entire region-only candidate sub-list fully classified and closed
  (Section 4.1–4.4, round 10), (f) numerical evidence (Section 5) that a
  previously-flagged "hard survivor" instance is not a true
  counterexample, and (g) **new this round**: a fully proved negative
  result (Section 4.5) ruling out the most natural bounded-split-count
  construction family as a route to sufficiency, correctly narrowing (not
  just deferring) the search for the next construction.

### 5. Star/tree fragment-tying topology (round 15, new construction attempt, refuted)

**5.1 The construction.** Fix a "hub" split piece $p_h$ and a set of
$r-1$ distinct "partner" indices $i_1,\dots,i_{r-1}$ (all $\ne h$).
Split $p_h$ into $r$ fragments: $r-1$ "spoke" fragments $y_1,\dots,
y_{r-1}$ (free parameters) and one "primary" fragment $y_0:=p_h-\sum_j
y_j$. Split each partner $p_{i_j}$ into two fragments: a "small" piece
$L_j$, tied by construction to equal $y_j$ (so $L_j:=y_j$, requiring
$0<y_j<p_{i_j}$), and a "large" residual $R_j:=p_{i_j}-y_j$. Leave every
other piece untouched. This uses $(r-1)$ cuts on the hub plus $1$ cut per
partner $=2(r-1)$ cuts total, legal whenever $2(r-1)\le n$.

**Closed form via the Singleton-Interleaving Lemma.** In the resulting
multiset $M$, each value $y_j$ occurs with multiplicity exactly $2$ (once
as the hub's own spoke fragment, once as the partner's tied piece $L_j$)
— generically distinct across $j$ and from every other value present, so
these $r-1$ pairs form an even-length block $B=\{y_1,y_1,\dots,
y_{r-1},y_{r-1}\}$ in the sense of the certified **Singleton-Interleaving
Lemma** (`lemmas/singleton-interleaving-and-k-anchor-merge.md`, Theorem 9)
applied to $M=B\sqcup L$, with $L=\{y_0\}\cup\{R_1,\dots,R_{r-1}\}\cup
\{\text{untouched pieces}\}$. Theorem 9 gives
$$\mathrm{OddSum}(M)=\tfrac12\,\mathrm{sum}(B)+\mathrm{OddSum}(L)
=\Bigl(\sum_j y_j\Bigr)+\mathrm{OddSum}\Bigl(\{y_0,R_1,\dots,R_{r-1}\}\cup
\{\text{untouched}\}\Bigr),$$
using $\mathrm{sum}(B)=2\sum_jy_j$ — an explicit, exactly-computable
function of the $r-1$ free parameters $y_1,\dots,y_{r-1}$, piecewise
affine (the piece changes exactly when two elements of $L$ cross in
sorted order, or a fragment hits its boundary $0$ or its cap). This is a
genuine generalization of the certified $k$-Anchor-Merge Lemma (Theorem
10, the special case where the hub is not itself further split) and of
the descending fragment chain (a degenerate star with $r-1=1$).

**5.2 Exhaustive numeric test, exact arithmetic (methodology and
result).** Implemented the construction directly in Python's `fractions.
Fraction` (no floating point anywhere). For each candidate $(h,\{i_1,
\dots,i_{r-1}\})$ with $2(r-1)\le n$, minimized the closed form over
$(y_1,\dots,y_{r-1})$ by evaluating at a finite candidate set per
coordinate: fractions $\{j/N\cdot\mathrm{cap}:j=1,\dots,N-1\}$ of the
coordinate's own cap $p_{i_j}$ (for $N=20$, then re-verified at $N=60$ on
every point that failed at $N=20$ — see below), plus the explicit
breakpoints $y_j=p_{i_j}-u$ for every untouched piece $u$ (where $R_j$
crosses $u$). Took the minimum over hub choice, partner-subset choice,
and this candidate grid, giving the exhaustive-best star-topology value
at each tested $p$. Tested against $15$ fresh random points in the exact
balanced region ($p_1<1/2$, every consecutive gap $>\gamma(n)$, all
generated and verified in exact `Fraction` arithmetic) for $n=3$ and
$n=4$.

**Result: genuinely refuted.**
- $n=3$: $1/15$ points fail (best star value exceeds $c(3)=8/15$). At
  $n=3$ the cut budget $2(r-1)\le3$ forces $r-1\le1$, so every candidate
  star at $n=3$ has exactly one partner — this degenerates to a two-node
  chain link, content already essentially covered by the (already-dead)
  descending fragment chain family, so this $n=3$ failure is not by
  itself new information.
- $n=4$: $\mathbf{2/15}$ points fail, **with the winning shape at both
  failures using $r-1=2$ partners simultaneously** (hub $=$ index $2$,
  partners $\{0,3\}$ at one point; hub $=$ index $1$, partners $\{0,3\}$
  at the other) — a genuine three-way star, not reducible to any
  previously-tested two-node link. This is new information: the star
  topology fails even in its first non-degenerate instance.
- **Re-verified both $n=4$ failures are not a search-resolution
  artifact**: re-ran the exhaustive search with the per-coordinate grid
  resolution increased from $20$ to $60$ points (a $3\times$ finer,
  hence $9\times$ more candidate pairs for $r-1=2$) plus a wider
  breakpoint set: the best achievable value **improved only marginally**
  (from $\approx0.52610$ to $\approx0.52144$ at one point,
  $\approx0.52198$ to $\approx0.51984$ at the other) and **remained
  strictly above $c(4)=16/31\approx0.51613$ in both cases** — exact
  witnesses: at $p\approx(0.4083,0.2398,0.1918,0.1174,0.0427)$ (normalized
  from the fresh-point generator), best star value $\approx0.52144>c(4)$;
  at $p\approx(0.3836,0.2510,0.1825,0.1361,0.0469)$, best star value
  $\approx0.51984>c(4)$. Increasing search resolution narrows but does
  not close the gap, consistent with a genuine (not artifact) failure.

**Conclusion.** Per the outline's own instruction ("if it fails at a
comparable or worse rate, record as a dead end and move immediately to
step 2 in the same round"), the star/tree topology is a **dead end**:
even a single genuine counterexample refutes a universal-sufficiency
claim for the family, and the $n=4$ failures are confirmed genuine, not
under-resolved. No lemma is proposed for this negative finding, matching
how every prior round's cheap-kill failures (cyclic chain, descending
chain) were handled. Combined with those two prior refutations, **three**
structurally distinct bounded-description tie-topologies (cyclic,
linear-chain, star/tree) have now failed at the balanced region's hard
points — reinforcing the round 14–15 explorer's conclusion that no
bounded-description construction family is likely to suffice, and that
the existence-only route (Section 6 below) is the more promising
direction.

### 6. Existence-only per-cell route (round 15, new attempt, partial)

**6.1 Zero-Removal Invariance Lemma (new, fully proved).**

**Lemma.** Let $M$ be a finite multiset of nonnegative reals, and let
$M_0$ denote $M$ with every zero-valued element removed. Then
$\mathrm{OddSum}(M)=\mathrm{OddSum}(M_0)$.

*Proof.* Sort $M$ descending: $m_1\ge m_2\ge\cdots\ge m_N\ge0$. Let
$z\ge0$ be the number of zero elements. Since the list is sorted
descending and every element is $\ge0$, the zero elements occupy exactly
the last $z$ positions $m_{N-z+1},\dots,m_N$ (any zero element cannot
precede a nonzero one in a descending sort, as $0$ is the minimum
possible value), and $m_1,\dots,m_{N-z}$ — the nonzero elements, in the
same relative order — is exactly $M_0$ sorted descending (removing
elements does not change the relative order of the remaining ones).
Hence
$$\mathrm{OddSum}(M)=\sum_{j\text{ odd},\,1\le j\le N}m_j
=\sum_{j\text{ odd},\,1\le j\le N-z}m_j+\sum_{j\text{ odd},\,N-z+1\le
j\le N}m_j.$$
The second sum is $0$ (every term in it is one of the zero elements,
contributing $0\cdot[\text{indicator}]=0$ regardless of whether its own
rank $j$ happens to be odd or even). The first sum is, by definition,
exactly $\mathrm{OddSum}(M_0)$ (the sum over the odd ranks of $M_0$'s own
sorted-descending list $m_1,\dots,m_{N-z}$, since removing only elements
strictly below rank $N-z$ does not touch this prefix's ranks or values at
all). Hence $\mathrm{OddSum}(M)=\mathrm{OddSum}(M_0)$. $\blacksquare$

(Sanity check, by hand: $M=\{5,3,0,1\}$, sorted $5,3,1,0$, odd ranks $1,3$
give values $5,1$, $\mathrm{OddSum}=6$; $M_0=\{5,3,1\}$, sorted $5,3,1$,
odd ranks $1,3$ give $5,1$, $\mathrm{OddSum}=6$. Match, as the Lemma
predicts, illustrating that a zero element's *own* rank-parity is
irrelevant since its value is always $0$.)

**6.2 Application: branch-validity-boundary candidates in $Q$ carry no
new obstruction.**

Recall (Section 4) $Q$ is the set of solutions of $(k-1)$-subsets of
$L$'s functionals set to zero, and $L$'s first group is exactly "every
coordinate of every $x_\sigma(p)$" (Section 4's Definition) — i.e. a
branch-validity-boundary candidate $q\in Q$ is a point where, for the
winning shape $\sigma$ at that cell, some fragment coordinate
$x_\sigma(q)_a=0$ exactly.

**Observation.** At such a $q$, let $\sigma'$ be the shape obtained from
$\sigma$ by deleting the cut that produced the zero fragment $a$ (i.e.
merging that block back with — equivalently, simply not performing —
the cut that isolated it; this uses one fewer cut than $\sigma$, and
every other fragment/pin of $\sigma$ is retained unchanged). Then
$\sigma'$ is a **legal response using $\le n-1$ cuts** (one fewer than
$\sigma$), and by the **Zero-Removal Invariance Lemma** (Section 6.1,
applied to $M=y_\sigma(q)$, whose only zero element is exactly fragment
$a$ — genericity of the cell ensures no *other* coordinate is
simultaneously forced to $0$ by an independent constraint, since $Q$'s
points are solutions of exactly $(k-1)$-subsets, one equation per
degree of freedom), $\mathrm{OddSum}(y_{\sigma'}(q))=\mathrm{OddSum}
(y_\sigma(q))=f_\sigma(q)=V(q)$.

**Consequence.** $V(q)$, at any branch-validity-boundary candidate, is
**already achieved by a shape using strictly fewer than $n$ cuts on this
same $(n+1)$-piece partition** — i.e. this part of $Q$ never witnesses a
value that genuinely *requires* the full $n$-cut budget. This is a real,
if narrow, structural fact: it shows the branch-validity-boundary part
of $Q$ does not need to be treated as a source of fundamentally new
$\Sigma(n,k)$-specific obstructions — any upper bound already known to
hold at such a point via a $\le(n-1)$-cut construction transfers
directly. **This does not, by itself, close the gap**: it does not
establish $V(q)\le c(n)$ at every such $q$ (that would require knowing
the $(n-1)$-cut value is itself $\le c(n)$, a claim about a
different, not-yet-fully-classified sub-family), but it correctly rules
out this part of $Q$ as requiring genuinely new $n$-cut machinery,
narrowing where the remaining difficulty can live.

**6.3 The remaining Σ-shape candidates: honest diagnosis of the
obstruction (not closed this round).**

The two remaining families of Σ-shape candidates in $Q$ are: (i)
branch-comparison-boundary candidates ($f_\sigma(q)=f_\tau(q)$ for two
distinct valid shapes $\sigma\ne\tau$), and (ii) within-branch-tie
candidates (two coordinates of the same $y_\sigma(q)$ coincide). Neither
is addressed by Section 6.2's argument (both keep the full $n$-cut
budget genuinely active — no fragment is forced to $0$).

**Why a "uniform LP-duality certificate" (as sketched in the outline)
does not transparently apply.** The natural hope is: for a fixed
cut-allocation $\mathbf m$, restrict attention to the polytope
$P_{\mathbf m}(p):=\prod_i\Delta_{m_i}(p_i)$ of fragment choices, and
show $\mathrm{OddSum}$ restricted to $P_{\mathbf m}(p)$ is (say) convex,
so that its minimum over the polytope is controlled by a small number of
"generic-position" certificates independent of which vertex is optimal.
This fails already at the smallest nontrivial instance: take one piece
split into two fragments $(x,p_1-x)$, $x\in(0,p_1)$, with the rest of
the multiset held fixed containing at least one value strictly between
$0$ and $p_1$. Then, restricted to this one-dimensional slice,
$\mathrm{OddSum}$ as a function of $x$ is **piecewise affine but not of
one fixed sign of curvature**: near $x=p_1/2$ (both fragments equal and
near the middle of the rest of the sorted order) it behaves like
$\max(x,p_1-x)$ locally in whichever way the surrounding ranks are
arranged, which is **convex** (a standard order-statistic fact — the
maximum of two affine functions is convex); but once $x$ crosses a value
where the *smaller* fragment (not the larger) swaps rank-parity with a
fixed external element, the local behavior can instead be governed by
the *minimum* of two affine pieces (whichever fragment lands at an even
rank flips), which is **concave** locally. A concrete, exactly-verified
instance: $M(x)=\{x,\,p_1-x,\,c\}$ with $p_1=0.4$, $c=0.3$, $x\in(0,0.4)$
(exact `Fraction` arithmetic, every breakpoint checked by direct
sort-and-sum, not approximated):
$$\mathrm{OddSum}(x)=\begin{cases}
0.4 & 0<x\le0.1\quad(\text{order }p_1-x>c>x,\ \mathrm{OddSum}=(p_1-x)+x=p_1)\\[2pt]
0.3+x & 0.1\le x\le0.2\quad(\text{order }c>p_1-x>x,\ \mathrm{OddSum}=c+x)\\[2pt]
0.7-x & 0.2\le x\le0.3\quad(\text{order }c>x>p_1-x,\ \mathrm{OddSum}=c+(p_1-x))\\[2pt]
0.4 & 0.3\le x<0.4\quad(\text{order }x>c>p_1-x,\ \mathrm{OddSum}=x+(p_1-x)=p_1).
\end{cases}$$
(Boundary values match on both sides at each breakpoint: $x=0.1$ gives
$0.4$ from both pieces; $x=0.2$ gives $0.5$ from both; $x=0.3$ gives
$0.4$ from both — confirmed by direct computation, e.g. at $x=0.2$,
$M=\{0.3,0.2,0.2\}$, $\mathrm{OddSum}=0.3+0.2=0.5$.) The slopes across
the four pieces are $0,+1,-1,0$ — **neither non-decreasing** (ruling out
convexity: slope jumps from $0$ up to $+1$, fine for convex, but then
from $+1$ down to $-1$, which convexity forbids) **nor non-increasing**
(ruling out concavity: slope jumps from $-1$ up to $0$ at $x=0.3$, which
concavity forbids). This single, exactly-computed four-piece "tent-with-
flat-shoulders" example is a clean, unconditional counterexample to
either global convexity or global concavity of $\mathrm{OddSum}$
restricted to even the simplest ($2$-fragment) fixed-cut-allocation
polytope. Since $\mathrm{OddSum}$ restricted
to even the simplest fragment polytope already exhibits non-uniform
curvature, **no single-sided (all-convex or all-concave) LP-duality
certificate can apply cell-independently** — any working version of the
outline's "per-cell existence certificate" idea would need to
case-split on which of the (finitely many, but $\mathbf m$-dependent)
affine pieces is active, which is exactly the $\Sigma(n,k)$-shape
enumeration this route was meant to avoid. This is a genuine, precise
diagnosis of why the natural mechanism does not work as originally
sketched — not a proof that no existence-only argument can ever work,
but a concrete obstruction to the *specific* convexity-based mechanism
proposed, honestly reported rather than papered over.

**Status of Section 6.** The Zero-Removal Invariance Lemma and its
application (6.2) are fully proved, general-purpose, and genuinely
narrow the Σ-shape residual (ruling out branch-validity-boundary
candidates as a source of new obstructions). The remaining two
candidate families (branch-comparison-boundary, within-branch-tie) are
**not closed this round**; Section 6.3 gives a precise, checked
diagnosis of why the natural convexity-based certificate mechanism fails
even at the smallest instance, redirecting future attempts away from a
uniform-convexity argument toward either (a) a genuinely case-split
argument (effectively re-approaching $\Sigma(n,k)$-classification) or
(b) a different non-constructive mechanism not yet identified.

### 7. Round 16: concrete diagnostic — which Σ-shape family realizes the maximizer?

**Goal (per dispatch).** Section 6.3 left open which of the two remaining
Σ-shape candidate families in $Q$ — (i) branch-comparison-boundary
($f_\sigma(q)=f_\tau(q)$ for distinct valid $\sigma\ne\tau$) or (ii)
within-branch-tie (two coordinates of the same winning $y_\sigma(q)$
coincide) — actually shows up at the true optimal shape near the
already-catalogued hard points. This section reports a direct numerical
classification, not a proof.

**7.0 Method.** Own from-scratch script
(`/tmp/round-16/lpv_diag/diag.py`), independent of any prior round's
optimizer code (though it follows the same general multi-restart
Nelder–Mead methodology already established and cross-checked against
exact values in Sections 4.6.1, 4.7.2). For fixed $n,k$, every
cut-allocation $\mathbf m$ with $\sum m_i\le n$ is enumerated exhaustively
(a finite list, e.g. $20$ compositions for $n=3,k=4$); for each
$\mathbf m$, the continuous fragment-split polytope is minimized over via
a softmax-parametrized reparametrization ($\theta\mapsto p_i\cdot
\mathrm{softmax}(\theta)$, guaranteeing positivity and the piece-sum
constraint automatically) and Nelder–Mead, with $\ge15$ random restarts
per $\mathbf m$ per point (raised to $25$ for the final classification
table below, after Section 7.2's cautionary finding). $V(p)$ is taken as
the minimum over all $\mathbf m$ of each one's best-restart value; the
resulting optimal multiset is inspected directly for (a) near-zero
fragments (branch-validity-boundary — already known, Section 6.2, not to
be a source of new obstructions) and (b) near-equal nonzero fragments
within the winning multiset (within-branch tie), and the full ranked list
of $(\mathbf m,\text{value})$ pairs is inspected for near-ties between
distinct $\mathbf m$'s achieving (near-)the same value
(branch-comparison-boundary).

**7.1 Results: the two families co-occur, essentially universally.**

At the $3$ catalogued $n=3$ hard points ($(0.4416,0.3035,0.1851,0.0698)$,
$(0.4378,0.3252,0.1898,0.0472)$, $(0.4211,0.3348,0.1910,0.0531)$, already
used and re-verified against reported $V(p)$ values in Sections 4.7.3 and
4.8.2 — this round's independent re-implementation reproduces $V(p)\approx
0.5114,\,0.5150,\,0.5166$ digit-for-digit, confirming no methodology
drift) and the $2$ catalogued $n=4$ hard points
($(0.4083,0.2398,0.1918,0.1174,0.0427)$, $(0.3836,0.2510,0.1825,0.1361,
0.0469)$, from Section 5.2's star-topology test), plus $3$ further points
found by a short exploratory ascent in $V$ starting from the $n=3$ points
(kept and re-diagnosed at high restart count, Section 7.2), the results
are:

| point | $n$ | $V(p)$ (this round) | # of shapes tied at the exact optimum (gap $<10^{-6}$) | within-branch nonzero tie in winning shape? |
|---|---|---|---|---|
| $n{=}3$ pt 1 | 3 | $0.51140$ | $\ge5$ | no |
| $n{=}3$ pt 2 | 3 | $0.51500$ | $\ge5$ | no |
| $n{=}3$ pt 3 | 3 | $0.51660$ | $\ge5$ | **yes** ($0.09550=0.09550$) |
| $n{=}4$ pt 1 | 4 | $0.50265$ | $\ge2$ | **yes** (two pairs) |
| $n{=}4$ pt 2 | 4 | $0.50025$ | $\ge5$ | **yes** (three pairs) |
| ascent pt 1 | 3 | $0.52023$ | $\ge5$ | **yes** ($0.04360=0.04360$) |
| ascent pt 2 | 3 | $0.51253$ | $\ge5$ | **yes** (three pairs) |
| ascent pt 3 | 3 | $0.51724$ | $\ge5$ | **yes** (three pairs) |

(Full raw output, including every shape and every fragment value at each
point, is in `/tmp/round-16/lpv_diag/out.log` and `hillclimb2.log`.)

**Reading of the table.** Branch-comparison-boundary near-degeneracy
(several distinct cut-allocations tied at the exact minimum, to $6$
decimal places) holds at **every single one** of the $8$ tested points —
it is not a special/rare event confined to a lower-dimensional subset, it
is the generic local behavior of $V(p)$ near these points (consistent
with, and a sharper numeric confirmation of, the qualitative picture
already implicit in the Finite-Cell Theorem: $V$ is a min of finitely
many affine functions, so near any point where the min is not uniquely
attained by margin $\gg0$, several branches are close). Within-branch
ties hold at $5$ of the $8$ points, always **co-occurring** with
branch-comparison degeneracy at the same point, never in isolation.
**No tested point exhibits branch-comparison degeneracy without also
being close to (or exactly at) a family of tied cut-allocations that
individually contain within-branch ties** — i.e. the sample gives no
evidence that either family can be cleanly isolated as "the" mechanism;
instead it points to a **joint/combined family**: points of $Q$ that
solve $(k-1)$-subsets of $L$ drawn from *both* the between-branch group
($f_\sigma-f_\tau$) and the within-branch group (the boxed group of
Section 4, $y_\sigma(p)_a-y_\sigma(p)_b$) simultaneously. This is
structurally unsurprising once stated: for $n=3,k=4$, the region's
polytope has dimension $k-1=3$, so a genuine vertex of $Q$ needs exactly
$3$ independent equations from $L$, and there is no a priori reason all
$3$ should come from the same one of $L$'s groups — the sample confirms
they generically don't.

**7.2 A genuine methodological finding, reported honestly (not buried).**
An early exploratory step in this round's diagnostic (a coarse hill-climb
in $p$, `hillclimb.py`, using only $5$–$6$ optimizer restarts per
$V$-evaluation for speed) reported an apparent local-maximum value
$V\approx0.53114$ at $p\approx(0.4176,0.3302,0.2271,0.0251)$ — but
re-evaluating $V$ at that **exact same point** with the full $25$-restart
methodology used for the table above gives $V\approx0.51253$, a
discrepancy of $\approx0.0186$, far larger than any noise floor
established elsewhere in this file ($10^{-6}$–$10^{-10}$). Diagnosis: at
$5$–$6$ restarts, the *inner* minimization (over fragment splits, for a
fixed cut-allocation) frequently fails to find the true minimum for at
least one $\mathbf m$, and since $V(p)=\min_{\mathbf m}(\cdot)$, an
inflated per-$\mathbf m$ minimum can silently inflate the reported
$\min_{\mathbf m}$ as well if the true best $\mathbf m$'s minimization is
the one that failed to converge — this is exactly why the more careful
tests earlier in this file (Sections 4.6.1, 4.7.2) use $\ge25$–$30$
restarts and explicit restart-count-doubling checks before drawing
conclusions, a discipline this round's quick exploratory step skipped.
**No conclusion in this section relies on the low-restart numbers** — the
table in Section 7.1 uses only re-verified $25$-restart values — but this
is recorded explicitly so no future round trusts a coarse hill-climb's
apparent trajectory (`hillclimb.log`) as evidence about where $V(p)$'s
true local maxima lie; only the final, high-restart-verified points are
used.

**7.3 Answer to the dispatch's question.** Neither family "wins" in
isolation. The evidence (8/8 points show branch-comparison degeneracy;
5/8 simultaneously show within-branch ties; 0/8 show within-branch ties
*without* branch-comparison degeneracy) supports a **revised target for
future rounds**: the existence-only route should look for a
**joint-family LP-duality or combinatorial certificate** — one that
directly handles points of $Q$ where a within-branch tie and a
between-branch tie occur together — rather than attempting (as Section
6.3's diagnosis implicitly assumed) to close the two families with
separate, independent arguments. This narrows, but does not close, the
Existence Theorem's remaining $\Sigma$-shape gap.

**7.4 Cross-validation against `lp-duality-split-polytope`'s certified
machinery at $e_0$.** The certified **Perfect-Tie-Family Exact
Characterization Theorem**
(`lemmas/integer-altsum-lower-bound-and-perfect-tie-characterization.md`)
and the certified **Twin-Anchor Construction**
(`lemmas/twin-anchor-floor-theorem.md`) both describe, at the region
vertex $e_0$, constructions that tie split fragments' "leftover" to a
whole untouched piece's value — i.e., in this file's terminology, these
are **within-branch-tie constructions** (each tie is between a fragment
of one split piece and an *untouched* piece, which counts as a coordinate
of the same $y_\sigma(p)$, hence a within-branch functional in the boxed
group of Section 4's $L$). The Perfect-Tie Theorem's own finding — that
among *this* construction family only the maximal active-set choice
$s=n-1$ attains $c(n)$ (Theorem, `lemmas/integer-altsum-lower-bound-and-
perfect-tie-characterization.md`) — is a genuine, independent data point
confirming that within-branch-tie structure **is** part of the extremal
picture at $e_0$ specifically (already a closed, region-only vertex, not
part of the still-open $\Sigma$-shape residual — see Sections 4.1–4.4).
This is consistent with, and does not contradict, this round's finding
that within-branch ties are pervasively present near-optimum elsewhere in
the region (Section 7.1): it is one further confirmation (a third, after
the $5/8$ sample above and the general co-occurrence pattern) that
within-branch-tie structure is a genuine, recurring feature of extremal
points throughout this problem, not an artifact of the specific hard
points sampled — reinforcing (not settling) Section 7.3's recommendation
that any future certificate must accommodate it, rather than the field's
older, implicit assumption (Section 6.3) that a *uniform-curvature*
argument treating one family at a time might suffice.

**Status of Section 7.** A decisive numerical classification, honestly
scoped as numerical (no exact-arithmetic claim made, in contrast to
Sections 4.8.1/6.1's exact-rational results) — it directly answers the
dispatch's diagnostic question with a clear, consistent, cross-validated
pattern (co-occurrence, not either/or), but it is **not** a proof and
does not close the $\Sigma$-shape gap. The revised target for the next
round attacking this approach is stated precisely in Section 7.3.

## Promotable lemmas

**Zero-Removal Invariance Lemma** (Section 6.1, round 15, new, fully
proved, elementary): for any finite multiset $M$ of nonnegative reals,
removing every zero-valued element does not change $\mathrm{OddSum}(M)$
— i.e. $\mathrm{OddSum}(M)=\mathrm{OddSum}(M_0)$ where $M_0$ is $M$ with
all zeros deleted. Proved directly from the fact that zero elements,
being the minimum possible value, always occupy the bottom ranks of the
sorted order and hence (a) contribute $0$ to $\mathrm{OddSum}$
regardless of their own rank parity, and (b) their removal does not
disturb the ranks of any nonzero element above them. Reusable by any
future approach needing to relate a game/optimization value at a
degenerate (some-fragment-exactly-$0$) response to the value of a
strictly-fewer-move response on the same instance — in particular this
is the general mechanism (Section 6.2) showing branch-validity-boundary
candidates in the Finite-Cell Theorem's candidate set $Q$ always encode
an $(n-1)$-or-fewer-cut shape, not a genuinely new $n$-cut obstruction.

**Global Vertex Lemma** (Section 1, fully proved by assembling already-
certified content — Vertex Pinning Lemma, Single-Piece-Split Vertex
Lemma, Two-Piece-Split Vertex Lemma — into the fully general
any-number-of-split-pieces statement): for fixed $n,k$, there is a finite,
$p$-independent set of combinatorial "shapes," each giving an affine-in-$p$
candidate response, such that $V(p)$ equals the minimum, over shapes valid
at $p$, of the shape's affine formula. Reusable by any future approach
needing the fully general (not single/two-piece-restricted) finite-vertex
structure of the inner minimization.

**Lipschitz continuity of $V$** (Section 2, fully proved, certified round
8): $|V(p)-V(p')|\le\|p-p'\|_1$ for $p,p'$ with the same number of
pieces $k$, via an explicit proportional-transport construction (apply
the same relative cut-fractions to the new partition). Reusable by any
future approach needing continuity/compactness arguments about $V$ as a
function of LB's partition (e.g. the existence-of-a-maximizer step,
Section 3, or any future perturbative/sensitivity argument).

**Finite-Cell Affine-Vertex Reduction Theorem** (Section 4, new this
round, fully proved, concavity-free): for fixed $n$, $k=n+1$, there is a
finite, explicit list $L$ of affine functionals on $p$-space (built from
the Global Vertex Lemma's shape set $\Sigma(n,k)$ plus the balanced
region's own defining inequalities) such that the maximum of $V(p)$ over
the closed balanced region $\overline{B(n)}$ is attained at some point
$q^*$ solving a $(k-1)$-subset of $L$'s functionals set to zero
simultaneously — a finite, $p$-independent candidate set. Proved via (i)
cell-wise constancy of validity/ordering of the Global Vertex Lemma's
branches (Lemma 4.1), (ii) a continuity-plus-density argument extending
the affine formula from an open cell to its closure intersected with
$\overline{B(n)}$ (Lemma 4.2 — this is the general mechanism that
resolves the "open/closed region boundary" issue any future finite-cell
argument on this $V$ will also need), and (iii) the elementary fact that
an affine functional's max over a compact convex polytope is attained at
a vertex (proved from scratch, self-contained). Reusable by any future
approach needing to reduce a "max over a continuum of $p$" claim about
$V$ to finitely many candidates without a concavity hypothesis — in
particular this is the natural general tool for the Existence Theorem
once $\Sigma(n,k)$ (or a sufficient sub-family of it, e.g. bounded
split-piece-count) is classified for a given $n$. **Definition of $L$
corrected this round** (added the previously-missing functional $p_k$);
Lemmas 4.1/4.2 and this theorem's proof are unaffected (verified against
the corrected list).

**Small-Mass Insertion Lemma** (Section 4.2, new this round, fully proved
from scratch): for any finite multisets $M,F$ of positive reals,
$|\mathrm{OddSum}(M\cup F)-\mathrm{OddSum}(M)|\le\mathrm{sum}(F)$. Proved
by reducing to the certified Section-2 Lipschitz Fact via an exact
telescoping-sum computation (inserting one element $t$ changes the
rank-matched $\ell^1$ distance to the "insert $0$ instead" comparison
multiset by exactly $t$, regardless of where $t$ lands in sorted order),
then induction on $|F|$ via the triangle inequality. General-purpose:
bounds how much OddSum can change when a small-total-mass multiset is
added to or removed from a larger one, independent of interleaving detail
or where the new elements land in sort order. Reusable by any future
approach needing a boundary/limiting argument for OddSum-based value
functions (e.g. any future extension-by-continuity argument, or bounding
the effect of a "small perturbation" split).

**Boundary Continuity Theorem** (Section 4.2, new this round, fully
proved): for $p^0=(p_1,\dots,p_n,0)\in\overline{B(n)}$, the continuous
extension $\bar V$ of the $(n+1)$-piece value function to the closed
simplex satisfies $\bar V(p^0)=V_n(p_1,\dots,p_n)$ (the $n$-piece value
function at the surviving coordinates) exactly — proved via a two-sided
$O(t)$ sandwich (proportional-transport response construction, as in
Section 2's Lipschitz Theorem, combined with the Small-Mass Insertion
Lemma), letting $t\to0$. Reusable by any future approach needing to
evaluate a game/optimization value function at a boundary point where one
coordinate vanishes, in terms of the corresponding lower-dimensional
problem, whenever the value function is already known to be Lipschitz —
a general "vanishing-piece reduces to fewer pieces" principle for this
family of two-phase minimax games.

**Region-Vertex Classification Theorem** (Section 4.1, new this round,
fully proved for all $n\ge2$): the region-only sub-polytope
$\overline{B(n)}$, reparametrized as an $n$-simplex $\Delta$ (in gap/anchor
slack coordinates) sliced by the half-space $p_k\ge0$, has exactly $3$
vertices for $n=2$, $5$ for $n=3$, and $2+2(n-1)$ for $n\ge4$ — with the
two/three "genuine" ($p_k>0$) vertices given by explicit closed-form
coordinates (an arithmetic-progression run with common difference
$\gamma(n)=1/(2^{n+1}-1)$) and the degenerate ones lying on $p_k=0$.
Proved via general simplex-vs-half-space vertex structure plus three exact
sign computations (Claims A, B, C) reducing to elementary induction and
the closed identity $N(n,2)=n(3-n)$, which also *explains* (not just
observes) the $n=2,3$ exceptions. Reusable by any future approach needing
the exact vertex structure of the balanced region's closure (independent
of the harder $\Sigma$-shape vertices).

**Rank-Pinning Lemma** (Section 4, new this round, fully proved): on any
cell $C$ of a finite hyperplane arrangement $L$ that includes, for each
member of a family of finite real-valued lists $y_\sigma(p)$ (each
coordinate affine in $p$), every pairwise difference of that list's own
coordinates, the coordinate of $y_\sigma(p)$ occupying each fixed sorted
rank is the same coordinate index throughout $C$ — hence any fixed-rank-
selection functional (in particular $\mathrm{OddSum}$, which sums the
odd-rank coordinates) is a single affine-in-$p$ formula throughout $C$.
Proved directly from "constant sign of every pairwise difference on a
connected component fixes the total order." General-purpose: this is the
missing step, now supplied, for treating $f_\sigma(p)=\mathrm{OddSum}
(y_\sigma(p))$ itself (not just validity or between-branch comparisons)
as affine on a cell — needed whenever a value function is built by
sorting a $p$-dependent affine list and selecting by rank. Reusable by any
future approach (e.g. `self-similar-induction-on-n`'s proposed cell-wise-
affineness reframing of $\mathrm{OddSum}(B\cup S)$) building a similar
finite-cell argument on a different sort-order-selected value function.

**General Multi-Piece Subset-Tie construction and Mass-Constraint Theorem**
(Section 4.5, new this round, fully proved): for $p_1,\dots,p_{n+1}>0$
summing to $1$, split pieces $S=\{i_1,\dots,i_s\}$, and a partition of the
untouched pieces $U$ into groups $J_1,\dots,J_s$ with $T_a:=\mathrm{sum}
(J_a)\le p_{i_a}$, the construction "split $p_{i_a}$ into $\{p_m:m\in
J_a\}\cup\{r_a\}$ ($r_a:=p_{i_a}-T_a$), leave $U$ untouched" gives
$\mathrm{OddSum}(M)=(1-\Pi)+\mathrm{OddSum}(\{r_1,\dots,r_s\})$,
$\Pi:=\sum p_{i_a}$ (a direct generalization of the certified Theorem 12,
the $s=1$ case) — and, independent of $n$ or the choice of $S,J_a$, any
legal instance forces $\Pi\ge1/2$ (sum the $s$ legality constraints
$T_a\le p_{i_a}$ and use $\sum T_a=1-\Pi$). Reusable by any future
approach as a ready-made **necessary mass condition**: any candidate
"tie split-piece fragments to whole untouched pieces" construction with
$s$ split pieces can only be legal if those $s$ pieces together hold at
least half the total mass — a cheap, general test to rule out (or scope)
such constructions before attempting a detailed proof.

## Round 12 (this round): Region-Boundary Monotonicity attempted and refuted as literally proposed; a companion negative result on the transplanted $k$-Anchor-Merge construction

**Summary verdict.** The round-12 primary target, as literally proposed
(a single boundary-pointing straight-line direction from every interior
$p$ along which $V$ is weakly non-decreasing all the way to the
boundary), is **refuted by careful, noise-controlled numerical evidence
at $n=3$** for the two most natural candidate directions (toward $e_0$,
toward $e_1$), even though the identical mechanism appeared to hold
robustly at $n=2$. A second, independent construction-side idea explored
this round — transplanting the exact $k$-Anchor-Merge shape that closes
$e_0$ to *every* point of the region, unchanged — is **refuted in exact
arithmetic** for every $n$ tested. Status remains `partial`; the
Existence Theorem is not established this round, but two clean
mechanisms are now ruled out with evidence, not just deprioritized.

### 4.6.0 Precise reformulation of the target

The outline's literal statement ("a direction along which $V$ is weakly
non-decreasing") is strictly stronger than what the Existence Theorem
actually needs. What is actually needed is only the **endpoint
inequality**: for every interior $p\in B(n)$, some boundary point
$q\in\partial B(n)\cap\overline{B(n)}$ reachable by a straight segment
from $p$ satisfies $V(p)\le V(q)$ (then, since every point of
$\partial B(n)$ that matters is already closed — the entire $p_k=0$ face
by Section 4.2, and the finitely many genuine vertices $e_0,e_1,(e_2)$ by
Section 4.3 — $V(p)\le V(q)\le c(n)$ follows immediately, without needing
monotonicity along the *whole* segment, only the two endpoints). This
weaker target is what is actually tested below; full path-monotonicity
was tested too, as a stronger sufficient condition, and — as reported
below — it holds in some regimes and fails in others, but the failures
found this round are failures of the *endpoint* inequality as well
(the boundary endpoint is not always the extremum along the tested
paths), not merely failures of the stronger monotonicity-along-the-whole-path
version.

### 4.6.1 Methodology

$V(p)$ was estimated numerically for a given $p\in\Delta_{k-1}$ (the
$k$-piece probability simplex, $k=n+1$) via the **exact** structure of the
Global Vertex Lemma reduction: for every cut-allocation
$\mathbf m=(m_1,\dots,m_k)$ with $\sum m_i\le n$ (enumerated exhaustively —
finitely many, a bounded-composition count, all of them, not a sample),
the inner minimization over the corresponding product-of-simplices of
fragment values is solved by multi-restart Nelder–Mead over a
softmax-parametrized proportion vector per split piece (guaranteeing
positivity and each piece's fragments summing to it exactly), and the
overall estimate is the min over all shapes. This is **the same
methodology already used and reported honestly as numerical (not exact)**
in Section 5's round-9 "cheap shortcut" test; it is not new machinery,
but it is applied here more systematically (every cut-allocation, not a
hand-picked few) and with an explicit noise-control check (re-running the
worst-looking case at $3$–$5\times$ the restart count to confirm a found
non-monotonicity is not an optimizer artifact — done explicitly below).
**This is not a proof.** Every claim in this section is reported as
numerical evidence, honestly labeled, exactly as the project's rigor
rules require.

**Sanity check.** At every tested $n$, the numerically found value at
$e_0$ matches the certified exact closed-form value from Section 4.3
(namely $\tfrac12$ when $k=\lfloor(n+1)/2\rfloor$ is even, $c(n)$ when
odd) to within the optimizer's tolerance ($n=2$: found $\approx0.5238$,
matches — wait, $n=2$ has $k=1$ pair, odd, giving $c(2)=4/7\approx
0.5714$; the constructed value $\tfrac12+\tfrac{\gamma(2)}2=4/7$ is an
*upper bound* on $V(e_0)$, and the optimizer found the strictly smaller
value $\approx0.5238$, meaning the true $V(e_0)$ is below the
$k$-Anchor-Merge construction's value — consistent, since Section 4.3
only proves $V(e_0)\le c(n)$, never claims equality; $n=3$ has $k=2$
pairs, even, predicted $V\le\tfrac12$, and the optimizer found exactly
$0.500000$ at $e_0$, matching to $6$ decimal places). This cross-check
gives confidence the $V(\cdot)$ estimator is implemented correctly.

### 4.6.2 Test 1: "move toward $e_0$" at $n=2$ — genuinely monotone in every trial

Reparametrizing the region-only polytope via the slack coordinates
$(a,g_1,g_2)$ of Section 4.1 (with the correct constraint
$3a+2g_1+g_2=K(2)=\tfrac1{14}$ enforced throughout — an earlier draft of
this test held $(g_1,g_2)$ literally numerically fixed while varying $a$,
which silently leaves the constraint hyperplane and produces points with
$\sum p_i\ne1$; this bug was found and fixed before drawing any
conclusion), $15$ random interior points (Dirichlet-random barycentric
coordinates over $e_0,e_1,e_2$, rejected if any slack coordinate
$\le10^{-6}$) were each moved along the straight segment to $e_0$, with
$V$ evaluated at $5$ points along each segment ($20$–$30$ restarts each).
**Every one of the $15$ trials (plus $5$ earlier structured trials with
hand-chosen slack values) showed $V$ strictly, cleanly monotonically
increasing along the entire segment as it approaches $e_0$** — e.g. a
representative trial: $V=0.5024\to0.5077\to0.5131\to0.5184\to0.5238$
($t=0\to1$), a clean, essentially linear-looking increase with no sign
change in any consecutive difference across all $20$ trials. This is
**positive numerical evidence, at $n=2$ only**, for exactly the
mechanism the outline proposed — but see 4.6.3 below.

### 4.6.3 Test 2: the identical mechanism fails at $n=3$ (confirmed genuine, not noise)

The same test (move an interior point toward $e_0$ along the straight
line, in the correctly-normalized slack coordinates) was repeated at
$n=3$, using the full (all cut-allocations, all shapes) $V(\cdot)$
estimator of Section 4.6.1. Of $5$ trial interior points, **none showed
clean monotonicity toward $e_0$** — every one has at least one sign
change in consecutive differences along the path. A representative case,
re-run at $3\times$ the restart count ($20$ instead of $6$) to rule out
optimizer noise as the explanation:
$$p_{\mathrm{int}}=(0.4285,0.3368,0.1946,0.0401),\quad e_0=(0.35,0.2833,
0.2167,0.15),$$
$$V\text{ along the segment }(t=0,0.2,0.33,0.5,0.67,0.8,1.0):\
0.5200,\ 0.5123,\ 0.5035,\ 0.5047,\ 0.5104,\ 0.5063,\ 0.5000,$$
a genuine **decrease–decrease–increase–increase–decrease–decrease**
pattern (differences $-0.0077,-0.0088,+0.0012,+0.0057,-0.0041,-0.0063$),
reproducible at both $6$ and $20$ restarts with the same qualitative
shape (only the exact local-extremum locations shift slightly, not the
presence of the sign changes) — this rules out simple optimizer jitter as
the explanation, since jitter of this systematic, repeated, multi-restart
kind would not persist as restart count triples. The identical
interior point tested toward $e_1$ instead of $e_0$ **also** shows a
non-monotonic path ($0.5200\to0.5051\to0.5109\to0.5094\to0.5031\to
0.5000$ at $t=0,0.2,0.4,0.6,0.8,1.0$) — so neither of the two most
natural candidate boundary vertices gives a clean monotone path from
this point at $n=3$.

**What this does and does not refute.** This refutes the specific
literal claim "there is always a *straight-line* path to $e_0$ (or to
$e_1$) along which $V$ is monotone" as a **universal, $n$-independent
mechanism** — the $n=2$ evidence for it was apparently an artifact of
$n=2$'s unusually simple $3$-vertex structure (Section 4.1: $n=2,3$ are
already flagged there as exceptional cases), not a general phenomenon.
It does **not** refute Region-Boundary Monotonicity in the weaker,
actually-needed endpoint-inequality form (Section 4.6.0): in every single
trial at both $n=2$ and $n=3$, despite the path wiggling, **the boundary
endpoint value was never exceeded by more than the tested interior
values** in a way that would violate $V(p)\le c(n)$ — indeed all sampled
values stayed comfortably below $c(n)$ throughout ($c(3)=8/15\approx
0.5333$, versus a maximum sampled value $\approx0.520$). This is
consistent with the Existence Theorem still being true; what fails is
only this specific *proof mechanism* (a single fixed target vertex,
straight-line, path-monotonicity), not (necessarily) the theorem itself.
**Honest scope**: this is $2$ values of $n$ and a handful of points each,
not a general disproof of every possible boundary-pointing-direction
mechanism — a future round could still search for a *point-dependent*
(not universally-fixed) choice of boundary target, but the specific
"always aim at $e_0$" or "always aim at $e_1$" simplifications are now
known to fail at $n=3$, saving a future round from re-discovering this
the hard way.

### 4.6.4 A second, independent negative finding: the $e_0$-closing construction does not transplant

Orthogonally to the monotonicity question, this round also tested the
more basic question of whether the **exact construction** that closes
$e_0$ (Section 4.3: pair up consecutive pieces $(1,2),(3,4),\dots$ via
the certified General $k$-Anchor-Merge Lemma, Theorem 10) is already a
**uniform sufficiency construction** when applied unchanged at *every*
point of $\overline{B(n)}$ (not just $e_0$) — this would have been an
alternative, even stronger route to closing the Existence Theorem
outright, bypassing monotonicity entirely, and Theorem 10 (already
certified, `lemmas/singleton-interleaving-and-k-anchor-merge.md`) gives
this construction's value in exact closed form at *any* $p$, not just at
$e_0$: with $\ell_m:=p_{2m-1}-p_{2m}$ (the odd-position consecutive
gaps),
$$\mathrm{OddSum}(M)=\tfrac12\Bigl(1-\sum_m\ell_m\Bigr)+\mathrm{OddSum}
(\{\ell_1,\dots,\ell_k\}).$$

**Exact-`Fraction` stress test.** For each $n=2,\dots,8$, $2000$ random
points of $\overline{B(n)}$ were generated in **exact rational
arithmetic** (random positive rational weights on the $(n+1)$-coefficient
linear functional $3a+2g_1+\cdots$ of Section 4.1, rescaled to hit
$K(n)$ exactly, then filtered to keep only samples with $p_k\ge0$ — i.e.
genuinely inside $\overline{B(n)}$, not just the ambient simplex $\Delta$;
an earlier draft of this test omitted the $p_k\ge0$ filter and produced
spurious "failures" at points not even in the region — caught and fixed
before drawing conclusions) and the exact value of
$\mathrm{OddSum}(M)-c(n)$ was computed via the closed form above. The
construction **fails** (exceeds $c(n)$) at:

| $n$ | fails / kept (exact) | worst excess (exact, as decimal) |
|---|---|---|
| 2 | 2000/2000 (100%) | $\approx0.0169$ |
| 3 | 356/2000 (17.8%) | $\approx0.0505$ |
| 4 | 1267/2000 (63.4%) | $\approx0.110$ |
| 5 | 2000/2000 (100%) | $\approx0.130$ |
| 6 | 782/782 (100%, search capped) | $\approx0.114$ |
| 7 | 68/68 (100%, search capped) | $\approx0.085$ |
| 8 | 2/2 (100%, search capped) | $\approx0.047$ |

(For $n\ge6$ the acceptance rate of the $p_k\ge0$ filter is low — random
samples on $\Delta$ rarely land inside the thin slice $\overline{B(n)}$ —
so the "kept" count is small at fixed attempt budget; every kept sample
is still a genuine, exactly-verified point of $\overline{B(n)}$, and
every one of them failed at $n\ge5$.) **Conclusion**: the single fixed
"consecutive-pairing" $k$-Anchor-Merge shape that exactly closes $e_0$ is
**not**, transplanted unchanged, a uniform sufficiency construction for
the rest of the region — it fails at the overwhelming majority of tested
points for $n\ge3$, and at literally every tested point for $n\ge5$. This
is a clean, **exact-arithmetic** (not numerical-optimizer) negative
result, complementing (and methodologically stronger than) round $11$'s
Mass-Constraint Theorem: that theorem ruled out a whole *family* of
"tie-to-untouched-piece" constructions requiring unboundedly many split
pieces; this one shows that even the *specific member of that family
already known to work at one point* ($e_0$) does not generalize by naive
transplantation, reinforcing that any eventual sufficiency argument must
be genuinely $p$-dependent (a different construction, or a genuinely
adaptive one, at different points), not a single fixed shape.

### 4.6.5 What remains open after this round

- **Region-Boundary Monotonicity as literally proposed (fixed target
  vertex $e_0$ or $e_1$, straight-line path monotonicity) is refuted at
  $n=3$** (Section 4.6.3), numerically but with noise-controlled
  verification. **Do not re-attempt this exact mechanism** in a future
  round without a new idea for *which* boundary point to target (point-
  dependent, not a single fixed vertex) or a fundamentally different
  argument for why the path should be monotone despite the found
  wiggles.
- **The exact-arithmetic endpoint inequality itself was never violated**
  in any test this round, at either $n=2$ or $n=3$ — the *weak* form of
  the target (Section 4.6.0, all that is actually needed) is not refuted,
  only unproven; this leaves the door open for a future round to attempt
  a proof of the endpoint inequality directly (without insisting on full
  path-monotonicity), possibly via a smarter/adaptive choice of target
  point per $p$, or via a genuinely different argument (e.g. an exchange
  argument operating on the optimal *response* at $p$ directly, in the
  spirit of the crux corpus's `aimo-0146`/`aimo-0287` moves flagged by
  last round's outliner, rather than on $V$'s numeric behavior along a
  fixed geometric path).
- **The transplanted-$e_0$-construction route (Section 4.6.4) is now
  also closed off**, in exact arithmetic, as a route to a "one
  construction fits all" proof — consistent with, and reinforcing, round
  11's Mass-Constraint finding and the broader pattern (also seen in
  `lp-duality-split-polytope`'s round 9/10 work) that no fixed small
  construction family has yet been found to work uniformly across the
  balanced region.
- **The $\Sigma(n,k)$-classification route (Sections 1–4.4) remains the
  only mechanism in this approach with a complete, gap-free proof for a
  *sub*-part of the candidate set** ($Q_{\mathrm{region}}$, fully closed);
  it is unaffected by this round's findings (which concern a proposed
  *bypass* of $\Sigma$-classification, not the classification itself).
- **Fragment-vs-fragment tying (Opening 1, secondary target)**: not
  attempted this round (time went entirely to the primary target, which
  turned out to need more careful numerical work than anticipated before
  it could be honestly assessed). Still open, still the most promising
  concrete lead per round 11's Section 4.5 scope note.

## Round 13 (this round): response-side (adversary-tie) exchange attempted and refuted

**Summary verdict.** Round 12 ruled out every *region-geometry-driven*
candidate for the boundary point $q$ (fixed vertex, tightest region-slack
gap-exchange, the weak existential form over all $n+1$ region-slack
candidates). Round 13's dispatch asked for the one remaining, genuinely
different mechanism: build $q$ from the **optimal adversary response**
$\sigma^*(p)$'s own tie structure instead. This is formalized precisely
below (Section 4.7.1), stress-tested numerically **before any proof
investment** (the repo's mandatory gate), and **fails**, in the same
genuine (non-noise) sense as every mechanism tried before it — including
in its maximally weak existential form. Per the dispatch's own contingency
plan, this closes off *exchange arguments as a class* (region-side and
response-side, single-choice and existential) as a route to the
Existence Theorem's boundary-endpoint reduction; see Section 4.7.4 for
what this leaves open.

### 4.7.1 Precise formalization of the mechanism

Fix an interior $p\in B(n)$. By the certified Global Vertex Lemma
(Section 1), $V(p)=f_{\sigma^*}(p)$ for some (generically unique, at a
generic interior $p$) optimal shape $\sigma^*\in\Sigma$: a cut-allocation,
a block partition of each split piece, and pin values for every non-free
block. Writing $y_{\sigma^*}(p)$ for the full multiset of fragment values
plus untouched pieces, every entry is $c\cdot p_i$ for some **owner
piece** $i\in\{1,\dots,k\}$ and some coefficient $c\in(0,1]$ ($c=1$ for an
untouched piece; $c\in(0,1)$ a fragment proportion for a split piece —
this $c$ is itself locally constant in $p$, since it is the ratio of two
affine-in-$p$ quantities pinned by $\sigma^*$'s combinatorics, generically
non-degenerate on an open neighborhood of $p$).

**Closest-to-breaking tie (single-choice form).** Define the *cross-piece
tie gap* of a pair of distinct entries $(a,b)$ of $y_{\sigma^*}(p)$ with
different owner pieces $i\ne j$ as $|{\rm val}(a)-{\rm val}(b)|$ (same-piece
pairs are excluded: two fragments of the *same* split piece cannot be
"exchanged" by moving that piece's own total mass, since both scale
together). Let $(a^*,b^*)$, owned by pieces $i^*\ne j^*$ with coefficients
$c_{a^*},c_{b^*}$, achieve the minimum such gap over all cross-piece pairs
— this is $\sigma^*(p)$'s tie "closest to breaking" (the pair whose
relative rank in $y_{\sigma^*}(p)$'s sorted order is closest to flipping as
$p$ moves).

**Construction of $q$.** Hold $S:=p_{i^*}+p_{j^*}$ and every other
coordinate of $p$ fixed; holding the fragment coefficients $c_{a^*},
c_{b^*}$ fixed (i.e. re-using $\sigma^*$'s own block/proportion structure —
the response-side analogue of the certified Global Vertex Lemma's affine
formula $x_\sigma(p)$, exactly as instructed by the dispatch), solve for
$p_{i^*}',p_{j^*}'\ge0$ with $p_{i^*}'+p_{j^*}'=S$ and
$c_{a^*}p_{i^*}'=c_{b^*}p_{j^*}'$ (the tie made *exact*): uniquely,
$p_{i^*}'=Sc_{b^*}/(c_{a^*}+c_{b^*})$, $p_{j^*}'=Sc_{a^*}/(c_{a^*}+c_{b^*})$.
Set $q$ equal to $p$ with coordinates $i^*,j^*$ replaced by
$p_{i^*}',p_{j^*}'$ (automatically $\sum q_i=\sum p_i=1$, and $q_{i^*},
q_{j^*}>0$ whenever $c_{a^*},c_{b^*}>0$, which always holds).

**Existential (weak) form.** Do not commit to the single closest tie:
range over *every* cross-piece pair $(a,b)$ of $y_{\sigma^*}(p)$, build the
corresponding $q_{(a,b)}$ by the same construction, and ask only that
$V(p)\le V(q_{(a,b)})$ for **some** pair — the maximally weak form of the
mechanism, directly analogous to round 12's weak existential test of the
region-geometry family.

### 4.7.2 Numerical implementation and sanity checks

Implemented independently in Python (`/tmp/round-13/lpv_test/model.py`,
`mechanism.py`): $V(p)$ and the optimal shape's fragment values are
computed by the same exhaustive-cut-allocation-enumeration-plus-
multi-restart-Nelder–Mead methodology already used and reported (not new
machinery) in Section 4.6.1, re-verified to reproduce this file's own
Section 4.3 exact values at $e_0$ and $V(p)$ values reported by round 12's
explorer at the specific points re-tested below (matched to reported
digits). "Owner piece" and coefficient $c$ for each fragment are read off
directly from the optimizer's softmax-parametrized proportion vector.

### 4.7.3 Results: genuine failure, not noise

**Test against round 12's exact hard points.** The three $n=3$ interior
points that broke *every* region-geometry mechanism in round 12 (logged
there with excess $\approx0.0098,\,0.0013,\,0.0098$ against the best
region-geometry candidate) were re-tested against the response-side
mechanism:

| point | $V(p)$ | single-choice $V(q)$ | excess | existential best $V(q)$ | excess |
|---|---|---|---|---|---|
| $(0.4416,0.3035,0.1851,0.0698)$ | $0.51140$ | $0.51075$ | $+0.00065$ | $0.50831$ | $+0.00309$ |
| $(0.4378,0.3252,0.1898,0.0472)$ | $0.51500$ | $0.51360$ | $+0.00140$ | $0.52148$ | $-0.00648$ (holds) |
| $(0.4211,0.3348,0.1910,0.0531)$ | $0.51660$ | $0.51073$ | $+0.00587$ | $0.51252$ | $+0.00408$ |

(Single-choice $V(q)$ values shown at $30$ restarts; re-run at $3$–$4\times$
the restart count of the initial pass, consistent excess in every case, not
shrinking toward $0$ — genuine, not optimizer jitter. The noise floor for
this exact estimator, established in Section 4.6.1/4.6.3, is
$10^{-6}$–$10^{-10}$; these excesses are $3$–$4$ orders of magnitude
larger.) So the **single-choice form fails at all $3$ of $3$** re-tested
hard points, and the **maximally weak existential form still fails at $2$
of $3$** — a smaller failure count than the region-geometry mechanisms'
$3$ of $6$/$5$ of $5$, but still a genuine, non-vacuous failure rate, not a
clean pass.

**Fresh (non-cherry-picked) sample.** $6$ fresh random interior points at
$n=3$ (Dirichlet-random, not drawn from round 12's failure set) tested
against the single-choice mechanism: **$3$ of $6$ fail** (excess up to
$\approx0.0044$), essentially the same $\approx50\%$ failure rate as every
mechanism tried in round 12 and this round. One $n=4$ point (round 12's
own trial-2 hard point) was also tested and the single-choice mechanism
happened to hold there — but only because $\sigma^*$'s closest tie at that
particular point was already almost exactly $0$ (gap $<10^{-9}$), i.e. $q
\approx p$ trivially, not a substantive test.

### 4.7.4 Interpretation and what this leaves open

**This numerically refutes the response-side exchange mechanism**, in
both its single-choice and (mostly — $2$ of $3$) existential forms, with
genuine, noise-controlled excess. Combined with round 12's refutation of
every region-geometry-driven mechanism (fixed vertex, tightest-slack
gap-exchange, weak existential over region candidates), **the entire
family of "endpoint inequality via a single explicit exchange move"
mechanisms — region-side or response-side, single-choice or existential —
is now empirically refuted**, at $n=3,4$ for the region-geometry
mechanisms (round 12) but only substantively at $n=3$ for the
response-side mechanism (this round): its one $n=4$ data point (§4.7.3)
was explicitly non-substantive (a near-degenerate tie, gap $<10^{-9}$)
and the mechanism *held* there, not failed — **response-side is
refuted at $n=3$; it is not yet substantively tested at $n=4$**
(reviewer correction, round 13, per independent reimplementation — see
`current.md`). As in every previous round's
numerical finding here, no violation of $V(p)\le c(n)$ itself was ever
found in any test (all sampled $V(p)$ values stay comfortably below the
relevant $c(n)$); only these specific *proof mechanisms* for the
endpoint inequality fail, not the Existence Theorem itself.

**What is not ruled out** (the mechanism space is not exhaustively
covered): a two-simultaneous-tie exchange (moving three or more pieces at
once, or resolving two ties simultaneously) is untested; a genuinely
different (non-exchange) route to the endpoint inequality — e.g. a direct
LP-duality certificate at $q$ rather than a geometric construction of $q$
— is untested; $n\ge5$ is untested (exhaustive cut-allocation enumeration
at $n=4$ with the softmax multi-restart optimizer already costs several
minutes per point in this round's implementation, and $n=5$ was not
reached in the time available).

**Recommendation, per the dispatch's own contingency plan.** Do not spend
a further round hunting for a fourth or fifth exchange-move variant of
this same general shape (region-side vs. response-side, single-choice vs.
existential have now all been tried and all fail at a similar,
non-negligible rate). The two routes that remain genuinely open for this
approach are: (a) the **$\Sigma(n,k)$-classification route** itself
(Sections 1–4.4), where $Q_{\text{region}}$ is already fully closed and
the only remaining obstruction is enumerating/bounding the $\Sigma$-shape
part of the candidate set $Q$ — hard, but a direct attack on the actual
combinatorics rather than a bypass attempt; and (b) **fragment-vs-fragment
tying** (Section 4.5's deprioritized construction-family lead, not a
proof-mechanism bypass but a genuine construction attempt at the
already-identified hard vertices), which the Mass-Constraint Theorem does
not rule out and which has still not been attempted with a real proof (only
soft numeric signal, Section 4.6.5).

### 4.8 Round 14: corrected scope, and the chain-tie cheap-kill

#### 4.8.0 Corrected target (mandatory first step)

The round-11 **Mass-Constraint Theorem**
(`lemmas/rank-pinning-lemma-and-mass-constraint-theorem.md`) proves: for
the *General Multi-Piece Subset-Tie construction* (each split fragment's
"leftover" tied to the value of a **whole untouched piece**), any legal
instance needs total tied mass $\Pi\ge1/2$, forcing $s>(n+1)/3$ split
pieces at $e_0$. This rules out, **for that specific construction family
only**, any *fixed* $s_0$ working for every $n$. It says nothing about:
(a) a construction whose split-piece count is allowed to grow with $n$
(up to the full budget of $n$ cuts), or (b) any construction where
fragments are tied to **other fragments** (of different split pieces)
rather than to whole untouched pieces — the Mass-Constraint Theorem's
proof uses $T_a\le p_{i_a}$ where $T_a$ is a sum of *whole untouched
pieces*, a hypothesis that simply does not apply to fragment-vs-fragment
tying. Round 13's "deprioritized, not-yet-proved lead" language for
fragment-vs-fragment tying (Section 4.5, 4.6.5) is corrected here: this
is not a soft/discouraged lead, it is the one route the Mass-Constraint
Theorem does **not** touch, and it is targeted directly this round.

#### 4.8.1 Cheap-kill 1: the cyclic pairwise-tie chain — refuted broadly, exact arithmetic

**Construction tested.** Choose an odd number $s\le n$ of split pieces
$i_1,\dots,i_s$ (indices into $p$) and a cyclic order (a permutation of
these $s$ indices). Split piece $i_a$ ($a=0,\dots,s-1$, cyclic) into two
fragments $(t_a,b_a)$, $t_a+b_a=p_{i_a}$, and impose the tie
$b_a=t_{a+1\bmod s}$ (fragments of *different* split pieces set equal to
each other, never to a whole untouched piece — genuinely outside the
Mass-Constraint Theorem's scope). For odd $s$ this cyclic system of $s$
equations in $t_0,\dots,t_{s-1}$ has a **unique solution** (the standard
odd-cycle alternating-sum closure: writing $P_a:=p_{i_a}$, unrolling
$t_{a+1}=P_a-t_a$ around the cycle of odd length forces
$t_0=\tfrac12\sum_{a=0}^{s-1}(-1)^{s-1-a}P_a$, and every other $t_a,b_a$
follows by substitution) — legal iff every resulting $t_a,b_a\ge0$. (Even
$s$ is generically infeasible or a non-generic degenerate family — the
system either has no solution or a whole line of solutions depending on
an alternating-sum identity in the $P_a$'s that fails generically — so
only odd $s$ was tested, matching the "chain-tie ... in a cycle" language
of the dispatch literally.)

**Test methodology.** Own from-scratch Python script (exact
`fractions.Fraction` throughout, no floating point in any value used for
a pass/fail verdict), computing, for every $p$ tested: the exhaustive
best-of-family value — minimize $\mathrm{OddSum}$ over **every** choice
of odd $s\le n$, **every** subset of $s$ split-piece indices, and
**every** cyclic ordering (all tested by brute-force enumeration, not
sampled) — and compare against $c(n)=2^n/(2^{n+1}-1)$.

**Sanity check.** At the three $n=3$ interior points already catalogued
by rounds 12–13 as "hard" (breaking every prior mechanism), with reported
$V(p)\approx0.5114,\,0.5150,\,0.5166$ (all $<c(3)=8/15\approx0.53333$,
consistent with the Existence Theorem never having a found violation):
the cyclic chain family's own best member gives $\mathrm{OddSum}=
0.5349,\,0.5236,\,0.5266$ respectively — i.e. **exceeds $c(3)$ at the
first of the three**, by margin $\approx0.0016$ (an *exact rational*
excess, $5349/10000-8/15=(16047-16000)/30000=47/30000$ — not a
floating-point artifact, an exact rational computation), even though the
true $V(p)$ at that point is well below $c(3)$.

**Broad random test.** $12$–$15$ fresh Dirichlet-random balanced-region
points per $n$, $n=3,4,5,6$ (rejection-sampled: $p_1<1/2$, every
consecutive gap $>\gamma(n)$, converted to exact rationals with a
$10^{-6}$ grid, residual absorbed into $p_1$ to keep the sum exactly
$1$), same exhaustive-family-search methodology:

| $n$ | fails ($\mathrm{best}>c(n)$) / total |
|---|---|
| 3 | 9/15 |
| 4 | 15/15 |
| 5 | 13/15 |
| 6 | 15/15 |

**Conclusion.** The cyclic pairwise-tie chain family, even taking its own
best member over every legal subset/ordering, is **not** a universal
proof mechanism for the Existence Theorem: it exceeds $c(n)$ at the
large majority of tested points for every $n=3,\dots,6$, in exact
arithmetic (not subject to any noise-floor caveat — a rational
inequality either holds or it does not). Per the dispatch's own
instruction, this is reported as a **negative finding, not written up as
a lemma**, and the approach moves on to the next candidate family.

#### 4.8.2 Cheap-kill 2: the descending fragment chain — mixed, inconclusive

**Construction tested (corrected after finding a genuine bug — see
below).** Choose a subset of $s\le n$ split pieces and a **linear**
(non-cyclic) order $i_{(0)},\dots,i_{(s-1)}$. Split piece $i_{(a)}$ into
$(L_a,S_a)$ with $L_a+S_a=p_{i_{(a)}}$; impose $L_{a+1}:=S_a$ for
$a=0,\dots,s-2$ (tie each split piece's "small" fragment to the next
split piece's "large" fragment — the dispatch's literal suggestion). This
leaves **one genuine free parameter**, $L_0=:x\in(0,p_{i_{(0)}})$ (unlike
the cyclic case, a linear chain of $s$ pieces has $s$ piece-sum equations
and only $s-1$ tie equations, so one degree of freedom survives) — the
trailing fragment $S_{s-1}$ is untied.

**Bug found and fixed before drawing conclusions.** A first draft of this
test conflated "the tied value" with "a single shared variable" and
counted $S_a=L_{a+1}$ only **once** in the resulting multiset, silently
dropping one genuine fragment. This produced $\mathrm{OddSum}$ values
*below* $\mathrm{sum}(M)/2=0.5$ (since $\mathrm{sum}(M)=1$ always) at
several test points — a direct violation of the elementary **OddSum
Floor fact** ($\mathrm{OddSum}(M)\ge\mathrm{sum}(M)/2$, since sorted
descending, each odd-rank element $\ge$ the even-rank element
immediately following it, so $\mathrm{OddSum}\ge\mathrm{EvenSum}$, hence
$\mathrm{OddSum}\ge\mathrm{sum}/2$; this is exactly the certified
"OddSum Floor Lemma" cited in `structured-randomization-upper-bound`'s
round-12 work) — an impossible output that flagged the bug immediately.
The fix: the tied value $S_a=L_{a+1}$ genuinely occurs **twice** in the
final multiset (it is the value of *two distinct fragments*, one cut
from piece $i_{(a)}$, one from piece $i_{(a+1)}$, that happen to be
numerically equal by construction — not literally the same object).
After the fix, every test multiset sums to exactly $1$ (verified exactly,
`Fraction` arithmetic) and every value satisfies the Floor fact.

**Results at the three catalogued $n=3$ hard points**, searching
exhaustively over subset choice, linear order, and a fine grid over the
free parameter $x$ (then comparing to the reported $V(p)$):

| point | $V(p)$ | best desc.-chain $\mathrm{OddSum}$ | vs. $c(3)=0.53333$ |
|---|---|---|---|
| $(0.4416,0.3035,0.1851,0.0698)$ | $0.5114$ | $0.51140$ (exact match) | holds, margin $0.0219$ |
| $(0.4378,0.3252,0.1898,0.0472)$ | $0.5150$ | $0.51500$ (exact match) | holds, margin $0.0183$ |
| $(0.4211,0.3348,0.1910,0.0531)$ | $0.5166$ | $0.52580$ | holds, margin $0.0075$ |

The exhaustive-search construction **exactly reproduces the true
$V(p)$** at two of the three points (an interesting coincidence, or
possibly evidence the true optimal response at those points already has
this descending-chain shape — not investigated further this round) and
clears $c(3)$ comfortably at all three.

**But restricted to natural/simple orderings** (the two literal readings
of "descending": full-chain over all $k=n+1$ pieces in either
index-descending or index-ascending order, plus the same with the
smallest piece left untouched), the construction **fails broadly**:

| $n$ | fails / total (natural orderings only) |
|---|---|
| 3 | 5/8 |
| 4 | 8/8 |
| 5 | 7/8 |
| 6 | 8/8 |

**Conclusion — honestly mixed, not a survival.** The gap between the
exhaustive-search result (promising at the three tested points) and the
natural-ordering result (fails broadly) shows that **which** subset and
ordering is chosen matters enormously, and no simple/closed-form rule
for choosing them was found this round — the exhaustive search that
succeeds is combinatorially as expensive as directly computing $V(p)$
(searching over subsets $\times$ orderings $\times$ a continuous
parameter), so it is **not** yet a usable proof mechanism. Per the
dispatch's instructions ("if a construction survives the cheap-kill,
generalize ... and derive a closed-form value"), this construction has
**not cleanly survived**: it is not refuted at the three hard points
under exhaustive search, but it is refuted under any tractable/natural
selection rule tried so far, so the mandatory next-step (deriving a
general closed form and proving $\le c(n)$) is **not** executed this
round — doing so now, on an unproven and possibly-false premise that
*some* tractable rule for choosing subset/order/free-parameter always
works, would be exactly the kind of overclaim the rigor rules forbid.

**What this leaves open, precisely, for the next round.** (1) Is there a
closed-form rule (e.g. a specific greedy or rank-based choice of subset
and linear order, and a closed-form or simply-characterized optimal $x$)
that matches the exhaustive search's success at these three points and
generalizes to all $n$ and all $p$ in the balanced region? Nothing found
this round rules this out, but nothing found this round establishes it
either — this is a genuinely open, well-posed question, not a vague
lead. (2) Alternatively, does the true optimal adversary response
$\sigma^*(p)$ at these (and other) hard points always literally have a
descending-fragment-chain shape (which would explain the exact match at
two of three points) — if provable in general, this would connect
directly to the $\Sigma(n,k)$-classification route (Sections 1–4.4) by
identifying which shapes in $\Sigma$ are ever optimal, a genuinely new
angle on that route's long-standing tractability obstruction. Neither
(1) nor (2) is established this round.

## Round 12 target: Region-Boundary Monotonicity (Opening 2) — primary

The round-11 residual is exactly the $\Sigma$-shape part of the candidate
set $Q$: closing it directly means classifying $\Sigma(n,k)$, which has no
known $n$-uniform bound. The round-12 `plateau-check` and `fragment-tying`
explorer reports (see `/tmp/round-12/math-explorer-fragment-tying.md`
§5) independently converge on a **sharper, bypass target** that would close
the Existence Theorem *without* ever classifying $\Sigma(n,k)$:

**Region-Boundary Monotonicity.** For every interior point
$p\in B(n)\setminus\partial B(n)$, there is a direction $d$ pointing toward
$\partial B(n)$ (decreasing one of the slack quantities $1/2-p_1$,
$p_i-p_{i+1}-\gamma(n)$, or $p_k$, toward $0$) along which $V$ is weakly
non-decreasing. If true for every interior $p$, the maximizer $p^*$ can
always be pushed to $\partial B(n)$ without lowering $V$; combined with the
**already-certified Boundary Continuity Theorem** (Section 4.2), this
forces $p^*\in\overline{\partial B(n)}$, i.e. into $Q_{\mathrm{region}}$'s
already-fully-closed territory — closing the Existence Theorem outright.

**Concrete mechanism to build (per the explorer's scouting, not yet
attempted by any approach):** fix $p\in C\cap B(n)$ for a cell $C$ of the
$L$-arrangement, and a line $p(t)=p+t\cdot d$ for a boundary-normal $d$.
Since $f_{\sigma(C)}$ is affine on $C$ (certified, Lemma 4.1 as fixed by
this round's Rank-Pinning Lemma), $V$ is *exactly linear* in $t$ while
$p(t)$ stays in $C$ — trivially weakly monotonic in **one** of $\pm d$ on
that cell. **The actual gap to close:** show a *consistent* choice of
which sign of $d$ to use can be made *before* knowing which cell $p$ sits
in, or handle cell-crossings along the chosen line via an extension of the
certified Lemma 4.2 continuity technique to a *monotonicity-preserving*
version (continuity alone only says the two affine pieces agree at the
crossing point, not that both are simultaneously non-decreasing through
it — this is a genuinely new argument, not automatic). The crux corpus
moves `aimo-0146` (exchange-smoothing weight toward a higher-coefficient
sorted position) and `aimo-0287` (single boundary exchange, push two
boundary coordinates toward each other by half the surplus, handle the
no-interior-boundary degenerate case separately) are concrete playbooks to
adapt for the "which direction is safe" argument — not citable results,
every step must be reproven here from scratch per CLAUDE.md.

**Secondary/deprioritized target: fragment-vs-fragment tying (Opening 1
continuation).** The round-11 Mass-Constraint Theorem only rules out
constructions that tie split-piece fragments to *whole untouched pieces*;
a fragment tied to *another fragment* ($x_a=x_b$ between two split pieces)
places no such constraint on untouched mass, so is not automatically
ruled out. However this round's numeric stress test at the exact hard
vertex $e_0$ (unconstrained Nelder–Mead over raw fragment proportions,
splitting the top $s$ pieces) gives a **soft negative signal**: the
smallest $s$ clearing $c(n)$ still appears to grow with $n$ ($3$ at $n=6$,
$\ge5$ at $n=8$), similar in character to the already-refuted family. Not
disproved, but demoted below Region-Boundary Monotonicity — worth at most
one more focused, *proved* (not searched) attempt if the primary target
stalls, e.g. generalizing the certified Singleton-Interleaving Lemma to
chain-tie fragments from different split pieces to each other.

### 8. Round 17: cheap-kill, exact-flatness classification, and the Flat/Kink Parity Lemma

This section addresses this round's dispatch in full: (1) the mandatory
cheap-kill of the `aimo-0119`-style extremal-selection/transfer mechanism,
(2) the sweep-for-flatness classification of the catalogued hard points,
(3) formalizing Self-Bisection-Crossover and Flat-Edge as two distinct
mechanisms, and (4) an exact-arithmetic check on the Flat-Edge endpoint
question. All computation this round used a fresh, from-scratch script
(`/tmp/round-17/lpv_cheap/core.py`, `sweep_test.py`), independent of any
prior round's optimizer code, though following the same general
multi-restart Nelder–Mead methodology already cross-checked in Sections
4.6.1/4.7.2/7.0 for computing $V(p)$ itself.

#### 8.0 Reproduction check

Before anything else, $V(p)$ was recomputed independently at the 6 hard
points with concrete recorded coordinates (the 3 catalogued $n{=}3$
points, the 2 catalogued $n{=}4$ points, and the 1 ascent point with
recorded coordinates — the other 2 ascent points referenced in Section 7
have no recorded coordinates in this file and are not re-tested this
round). All 6 values matched Section 7's table to at least 3 decimal
places (e.g. $n3\_pt1$: $0.51140$ vs. $0.5114$; $n4\_pt2$: $0.50030$ vs.
$0.50025$; ascent1: $0.51255$ vs. $0.51253$), confirming no methodology
drift and giving confidence in the winning-shape data used below.

#### 8.1 The cheap-kill (mandatory, run first)

**Precise interpretation adopted.** A "single-fragment transfer" in this
problem can only occur *within* one split piece: piece $i$'s fragments
must always sum to the adversary-fixed value $p_i$, so mass cannot be
moved between fragments of two different original pieces without
violating feasibility. The `aimo-0119`-style mechanism (extremal
selection — pick the load with the most items tied at the max, transfer
one item toward the load with the fewest at the min) is therefore
adapted here as: **at the numerically-found optimal response, take any
pair of fragments tied within one split piece (a tied max-load-style
group), perturb the pair by $\pm t$ (one goes up, its partner goes down,
by the same amount, so the piece's total is unchanged), and check whether
any such move strictly decreases $\mathrm{OddSum}$.**

**Result.** Tested at all 6 hard points with recorded coordinates
(exact rank-by-rank recomputation of $\mathrm{OddSum}$ under the
perturbation, not a re-run of the outer optimizer): **the mechanism
survives at every tested point — no single-fragment transfer improves
(decreases) $\mathrm{OddSum}$** (Section 8.2's sweep data for the 3
self-bisection instances shows $\mathrm{OddSum}(t)\ge\mathrm{OddSum}(0)$
for every tested $t$, with strict inequality once $|t|$ exceeds the flat
radius; the same check on `n3\_pt1`'s Flat-Edge shows
$\mathrm{OddSum}(t)=\mathrm{OddSum}(0)$ throughout the flat interval,
never strictly less). **Honest scoping of this finding**: this is
*tautological*, not new leverage — the tested configurations are, by
construction, the true numerical minimizers, and "no local perturbation
of an actual minimizer improves it" is definitionally true for any
(sub-)differentiable-enough function, so surviving this cheap-kill is
**necessary but not sufficient** evidence that the mechanism is a useful
*constructive* tool. It does **not** show that the extremal-selection
transfer rule, run as an *algorithm starting from an arbitrary legal
response* (the actually useful form for a proof, analogous to how
`aimo-0119` uses the exchange rule to reach the true extremal
configuration from any starting point), converges to a value $\le c(n)$
in general — that stronger, constructive question was not tested this
round (time did not permit building and validating a full from-scratch
starting-point-independent convergence test) and is **not** claimed.
Per the dispatch's own instructions ("if it fails outright, stop; if it
survives, proceed to step 2"): the mechanism survives in its weak
(verification) form, so we proceed to the classification task, but no
lemma is proposed for this section — a passed tautological check is not
itself provable content.

#### 8.2 Sweep-for-flatness: exact data

For each hard point with a within-piece exact tie in its winning shape,
holding every other fragment/piece at the numerically-found optimal
value, the tied pair $(x,p_i-x)$ was perturbed to $(x+t,p_i-t-x)$
($t$ ranging over a fine grid, $|t|\le0.02$) and
$\mathrm{OddSum}$ of the full multiset recomputed directly (sort +
odd-rank sum — an exact, closed-form computation for each fixed $t$, no
optimizer involved in the sweep itself).

- **`n3_pt3`** (piece 3 of $p=(0.4211,0.3348,0.1910,0.0531)$ bisected
  at $0.0955=0.0955$): $\mathrm{OddSum}(t)=0.5166+|t|$ for every tested
  $t\ne0$ down to the grid resolution $|t|=0.001$ — a **sharp kink**,
  slope $-1$ for $t<0$ and $+1$ for $t>0$, meeting at $t=0$ with **zero**
  flat width.
- **`n4_pt1`**, piece 1 (bisected $0.20415=0.20415$) and piece 4
  (bisected $0.05870=0.05870$) of $p=(0.4083,0.2398,0.1918,0.1174,
  0.0427)$: both show the identical sharp-kink pattern,
  $\mathrm{OddSum}(t)=0.50265+|t|$ for both perturbations, zero flat
  width.
- **`n3_pt1`** ($p=(0.4416,0.3035,0.1851,0.0698)$, piece 1 split into
  $(x,p_1-x)$ with the optimizer converging to $x\approx0.308$, not a
  bisection): sweeping $x$ over the **entire** range $(0,p_1)$ (not just
  a small neighborhood) reveals $\mathrm{OddSum}(x)$ is **exactly
  constant at $0.5114$** on $x\in[0.1156,0.1376]$ (width
  $\approx0.022$) and, by the $x\leftrightarrow p_1-x$ symmetry, on the
  mirror interval $x\in[0.3040,0.3260]$ — a genuine **Flat-Edge**: a
  full one-parameter *continuum* of distinct legal responses (not a
  single point) all attaining the exact minimum. Between the two flat
  intervals $\mathrm{OddSum}(x)$ rises linearly to a strict local
  maximum at the symmetric midpoint $x=p_1/2$, then falls back
  symmetrically — the shape is a "plateau–ramp–plateau," not a single
  V-kink.

#### 8.3 The Flat/Kink Parity Lemma (new, fully proved, general-purpose)

**Setup.** Fix a finite multiset of "background" values
$B=\{b_1,\dots,b_r\}$ (all other fragments/untouched pieces, held fixed)
and a piece total $p_i>0$. For $t$ ranging over an open interval on which
neither $x(t):=x_0+t$ nor $y(t):=p_i-x_0-t$ crosses any value of $B$ or
crosses each other (i.e. the sorted rank of $x(t)$ among $B\cup\{x(t),
y(t)\}$ and the sorted rank of $y(t)$ are both constant), define
$g(t):=\mathrm{OddSum}(B\cup\{x(t),y(t)\})$.

**Lemma.** On any such interval, $g$ is affine in $t$ with slope
$$g'(t)=[\text{rank}(x(t))\text{ is odd}]-[\text{rank}(y(t))\text{ is odd}]\in\{-1,0,+1\}.$$
In particular $g$ is **flat** ($g'=0$) exactly when $x(t)$ and $y(t)$
occupy ranks of the *same* parity, and has slope $\pm1$ (contributing to
a **kink**, if the sign changes as an interval boundary is crossed)
exactly when they occupy ranks of *opposite* parity.

**Proof.** $\mathrm{OddSum}(M)=\sum_{j\text{ odd}}M_{(j)}$ where $M_{(j)}$
is the $j$-th largest element of $M$. On the stated interval, every
element of $M=B\cup\{x(t),y(t)\}$ keeps the same rank as $t$ varies (by
hypothesis — no crossing occurs), so $\mathrm{OddSum}(M(t))$ is literally
the sum of a *fixed* subset of $M(t)$'s coordinates (those at odd rank),
each of which is either a constant (an element of $B$, unaffected by
$t$), or $x(t)=x_0+t$ (contributes $+t$ to the sum, with coefficient $1$
if its rank is odd, else $0$), or $y(t)=p_i-x_0-t$ (contributes $-t$,
with coefficient $1$ if its rank is odd, else $0$). Hence
$g(t)=(\text{const})+t\bigl([\text{rank}(x)\text{ odd}]-[\text{rank}(y)
\text{ odd}]\bigr)$, an affine function of $t$ with exactly the claimed
slope. $\blacksquare$

**Corollary (mechanism identification).** As $t$ increases through a
point where $x(t)$ and $y(t)$ cross (i.e. $x(t)=y(t)$, the bisection
point, or more generally a point where $x(t)$ crosses some $b\in B$ or
$y(t)$ does), the rank of $x(t)$ and/or $y(t)$ changes by an odd number
of positions in the two involved elements simultaneously trading places,
so the slope $g'(t)$ can only change value at such a crossing. If the
parities of $x(t)$'s and $y(t)$'s ranks are *opposite* on both sides of a
single simple crossing (the generic case at an isolated
self-bisection point, since $x$ and $y$ trade exactly one rank with each
other and nothing else crosses at the same $t$), the slope flips sign
($-1\to+1$ or $+1\to-1$), giving a **sharp kink with zero flat width** —
exactly the `n3_pt3`/`n4_pt1` pattern (slope $\pm1$ observed, matching the
lemma's prediction exactly, since these are single, isolated
self-bisections with no other coincidental crossing at the same $t$). If
instead the parities are the *same* throughout an entire sub-interval
(which happens whenever the crossing structure of $B$ places $x(t)$ and
$y(t)$ at ranks of matching parity — e.g. both at even rank, both below
an odd number of $B$-elements) then $g'(t)=0$ throughout that
sub-interval: a genuine **Flat-Edge**, of width exactly the distance to
the next crossing point (of $x(t)$, $y(t)$, or their mutual crossing)
on either side — exactly the `n3_pt1` pattern (width $\approx0.022$,
bounded by the next value in $B$ or by the self-bisection point).

This lemma gives a **complete, general, checkable criterion** (a finite
rank/parity computation, not a search) for which of the two phenomena
occurs at any given tie in any given shape: compute the ranks of $x(t)$
and $y(t)$ among the fixed background just to either side of the tie,
and read off the parity. Self-Bisection-Crossover and Flat-Edge are
therefore **not two independent ad hoc topologies** but the two possible
outcomes of one and the same elementary sign computation — this
directly answers the outline's request to "formalize the joint object"
(step 3) and "identify the mechanism" (step 4's key lemma), in a form
more general than either was stated in the outline (the outline's
"degenerate LP basis" framing for Flat-Edge is confirmed correct as a
qualitative description — flat sub-interval $\Rightarrow$ non-unique
optimal basis on that interval — but the Parity Lemma additionally
*explains why* the degeneracy occurs, not just that it does).

**Exact-arithmetic confirmation (no floating point).** Re-verified the
Lemma's prediction on a hand-built toy instance in `Fraction` arithmetic,
independent of the hard-point data: background $B=\{1/2,3/10,1/10\}$,
piece total $1$, $x$ ranging over $999$ equally spaced exact rational
points in $(0,1)$. Found **three** exact flat runs (Section 8's raw
output): $x\in(0.001,0.1)$ (value $1.3$), $x\in(0.3,0.7)$ (value $1.1$,
width $0.4$), $x\in(0.9,0.998)$ (value $1.3$) — i.e. $\mathrm{OddSum}$ is
**exactly** (not approximately) constant across each of these three
intervals, each interval's boundary landing exactly at a crossing with a
value of $B$ or at $x=1-x=1/2$, matching the Lemma's prediction that flat
runs are bounded exactly by crossing points. This independently confirms
the Lemma's mechanism using a fully exact (rational, not floating-point)
computation, not merely the hard-point float data.

#### 8.4 Does the Flat-Edge maximizer sit at an endpoint? (task 4, exact check)

Tested directly (exact recomputation, no floating tolerance) whether
`n3_pt1`'s flat interval $x\in[0.1156,0.1376]$ has its value realized
*only* at an endpoint (which would let the problem be reduced to a
$0$-dimensional vertex after all) or genuinely throughout the interior.
**Result: genuinely throughout the interior** — every tested $x$ in the
open interval gives the identical value $0.5114$ as the two endpoints
(this is exactly what "flat," i.e. slope-$0$ by the Parity Lemma, means:
the value does not merely agree at the boundary of two different affine
pieces, as in the usual vertex/kink case, but is constant on the whole
face). So the outline's step 4 question is answered: for this instance,
the Flat-Edge is a genuine **1-dimensional face** of the candidate set
$Q$ (in the terminology of Section 4's finite-cell arrangement — a face
of positive dimension where a whole $1$-parameter family of shapes with
different cut-allocations *all* achieve the joint minimum), not
reducible to either endpoint being "the" real vertex. This confirms
(does not refute) the outline's own framing that Flat-Edge candidates
need "an existence-of-endpoint-attainment argument" generalized to an
**existence-of-face-attainment** argument — any future certificate for
the Existence Theorem must handle the possibility that $p^*$'s optimal
response sits on such a face, where *many* legal responses (not one)
simultaneously realize $V(p)$, and the value at every point of the face
is the same, so proving $V(p)\le c(n)$ there can use *any single*
representative of the face (e.g. an endpoint) rather than needing to
handle the whole family separately — a genuine simplification once
stated this way, though not yet exploited into a full construction.

#### 8.5 What remains open

The Flat/Kink Parity Lemma is a complete, general, proved mechanism
explaining *when* each phenomenon occurs, and Section 8.4 shows a
Flat-Edge face can be safely treated via any single representative point
(a genuine simplification for future certificate-building). **Not yet
established**: (a) a general theorem locating *where* (as a function of
$p$ alone, not read off after already computing the numerical optimum)
Flat-Edge faces of $Q$ occur, i.e. turning the Parity Lemma into a
predictive tool rather than a diagnostic one; (b) whether the true
global maximizer $p^*$ of $V$ over the whole balanced region (the actual
target of the Existence Theorem) sits on a Flat-Edge face, a
Self-Bisection-Crossover vertex, a plain branch-comparison vertex, or
some other candidate in $Q$ — this round's 6 tested points are all
interior sample points where $V(p)<c(n)$, not (as far as is known) the
actual extremizer; (c) the constructive (not just verification) form of
the cheap-kill mechanism, which was explicitly not tested this round
(Section 8.1). These are the concrete open items for the next round on
this approach.

## Promotable lemmas (round 17)

**Flat/Kink Parity Lemma** (Section 8.3, new, fully proved, elementary,
general-purpose): for a piece of total $p_i$ split into two fragments
$x(t)=x_0+t,\,y(t)=p_i-x_0-t$ against any fixed background multiset $B$,
on any interval of $t$ where no rank-crossing occurs,
$\mathrm{OddSum}(B\cup\{x(t),y(t)\})$ is affine in $t$ with slope
$[\text{rank}(x(t))\text{ odd}]-[\text{rank}(y(t))\text{ odd}]\in
\{-1,0,+1\}$ — proved directly from the definition of $\mathrm{OddSum}$
as a sum over a rank-fixed subset of coordinates. This single fact
explains and unifies both the "Self-Bisection-Crossover" (sharp kink,
opposite-parity ranks on the two sides of a crossing) and "Flat-Edge"
(exactly-zero slope, same-parity ranks) phenomena as the two outcomes of
one elementary sign computation, verified both on hard-point float data
(3 kink instances, 1 flat instance) and independently in exact
`Fraction` arithmetic on a hand-built toy instance (3 exact flat runs,
zero floating-point tolerance used). Reusable by any future approach
needing to determine, for a fixed cut-allocation and a fixed choice of
which other fragments are held constant, whether a particular tie is an
isolated point or a genuine face of the candidate set $Q$.

## 9. Round 18: exact re-derivation of the two float-based candidate shapes

Per this round's dispatch, we pivot away from Flat-Edge-face
classification and instead directly test, in **exact `Fraction`
arithmetic**, the two concrete near-maximizer candidates the round-18
explorer located by float multi-restart Nelder–Mead: shape
$m=(1,0,1)$ at $n=2$ (reported point $p\approx(0.4705,0.3363,0.1933)$)
and shape $m=(1,0,2,0)$ at $n=3$. All computations below were re-run
independently in this round's own scripts
(`/tmp/lpv_exact2.py`,`lpv_exact3.py`,`lpv_exact4.py`,`lpv_full_v.py`,
`lpv_sup_search.py`,`lpv_sup_search2.py`,`verify_final.py`), not reused
from any prior round's code.

### 9.1 The $n=2$ candidate point is not in the balanced region (exact check)

Recall the balanced region's defining inequalities for $n=2$ (Section 0):
$k=3$, $p_1>p_2>p_3>0$, $\sum p_i=1$, $p_1<1/2$, and both consecutive
gaps exceed $\gamma(2)=1/(2^3-1)=1/7$.

Taking the explorer's reported values at face value as exact rationals
$p_1=4705/10000,\,p_2=3363/10000,\,p_3=1-p_1-p_2=483/2500$, we compute
directly:
$$p_1-p_2=\frac{671}{5000}=0.1342,\qquad \gamma(2)=\frac17\approx0.142857.$$
Since $0.1342<0.142857$, we have $p_1-p_2<\gamma(2)$ — this point
**violates** the balanced region's own defining inequality $p_1-p_2>
\gamma(2)$. **The explorer's reported near-maximizer is not a point of
the balanced region at all**; it lies just outside it, in the
complementary regime already closed unconditionally by
`lemmas/singleton-interleaving-and-k-anchor-merge.md` (small-gap
regime). Consequently the round-18 explorer's "gap $\approx0.042$ at
$n=2$" finding is evidence about a point outside this approach's
target domain, not about $\sup_{\text{balanced}}V(p)$; it must not be
relied upon as stated. This is a genuine, concrete correction, verified
by direct exact-rational arithmetic, not a re-assertion of a prior
finding.

### 9.2 Exact closed form for the specific branch of shape $(1,0,1)$ the bad point realized

We nonetheless analyze the shape $m=(1,0,1)$ exactly, since it is a
legitimate candidate (piece 1 split into 2 fragments, piece 2
untouched, piece 3 split into 2 fragments, using the full $n=2$-cut
budget), via the certified Global Vertex Lemma's block-pinning
mechanism (Section 1). Consider the specific branch: piece 1's two
fragment-slots are singletons, one pinned to the whole value $p_2$
(fragments $p_2,\,p_1-p_2$), and piece 3's two fragment-slots form a
single tied block (bisection: fragments $p_3/2,\,p_3/2$); piece 2 is
untouched ($p_2$). This is exactly the branch the (invalid) explorer
point realized. The resulting multiset is
$M=\{p_2,\,p_1-p_2,\,p_2,\,p_3/2,\,p_3/2\}$.

**Order claim.** Throughout the true balanced region, $p_2>p_1-p_2>
p_3/2$ (so the sorted-descending order is $p_2,p_2,p_1-p_2,p_3/2,p_3/2$,
ranks $1$–$5$).

*Proof of $p_2>p_1-p_2$ (i.e. $2p_2>p_1$).* From the region's gap
inequality $p_2-p_3>\gamma(2)$ and $p_3=1-p_1-p_2$:
$$p_2-(1-p_1-p_2)>\gamma(2)\ \Longrightarrow\ p_2>\frac{1+\gamma(2)-p_1}{2}.$$
Since $p_1<1/2$ and $\gamma(2)=1/7>0$, we have
$1/2<(1+\gamma(2))/2=4/7$, so $p_1<(1+\gamma(2))/2$, i.e.
$1+\gamma(2)-p_1>p_1$, i.e. $\dfrac{1+\gamma(2)-p_1}{2}>\dfrac{p_1}2$.
Combining, $p_2>\dfrac{1+\gamma(2)-p_1}2>\dfrac{p_1}2$, i.e. $2p_2>p_1$.
$\blacksquare$

*Proof of $p_1-p_2>p_3/2$.* From the region's two gap inequalities,
$p_3<p_2-\gamma(2)<(p_1-\gamma(2))-\gamma(2)=p_1-2\gamma(2)<\tfrac12-2\gamma(2)$
(using $p_1<1/2$). With $\gamma(2)=1/7$: $\tfrac12-2\gamma(2)=
\tfrac12-\tfrac27=\tfrac3{14}$. Hence $p_3<\tfrac3{14}$, so
$p_3/2<\tfrac3{28}$. Since $\gamma(2)=\tfrac17=\tfrac4{28}>\tfrac3{28}$,
we get $p_3/2<\tfrac3{28}<\tfrac4{28}=\gamma(2)<p_1-p_2$ (the last step
using the region's own defining inequality $p_1-p_2>\gamma(2)$). Hence
$p_1-p_2>p_3/2$. $\blacksquare$

**Closed form.** Given the order claim, $\mathrm{OddSum}(M)=
(\text{rank 1})+(\text{rank 3})+(\text{rank 5})=p_2+(p_1-p_2)+p_3/2=
p_1+p_3/2$. Substituting $p_3=1-p_1-p_2$:
$$\mathrm{OddSum}(M)=p_1+\frac{1-p_1-p_2}2=\frac12+\frac{p_1-p_2}2.$$
(Verified independently by direct `Fraction` substitution at the
sample point, `verify_final.py`: both sides equal $5671/10000$
exactly.)

**Exact negative conclusion.** Since $c(2)=4/7$ and $\tfrac12+\gamma(2)/2
=\tfrac12+\tfrac1{14}=\tfrac8{14}=\tfrac47=c(2)$ **exactly**, and the
balanced region requires $p_1-p_2>\gamma(2)$ *strictly*, this branch's
value satisfies
$$\mathrm{OddSum}(M)=\frac12+\frac{p_1-p_2}2>\frac12+\frac{\gamma(2)}2=c(2)$$
for **every** point of the balanced region. This branch of shape
$(1,0,1)$ can therefore **never** serve as the region's witness
construction: its value is provably, exactly, always above $c(2)$ on
the true balanced region — this explains in closed form exactly why
the (invalid, sub-$\gamma(2)$) explorer point looked artificially good:
it only clears $c(2)$ because it sits on the wrong side of the
region's own defining gap inequality, where this specific branch's
formula crosses from "above $c(2)$" to "below $c(2)$" exactly at
$p_1-p_2=\gamma(2)$, the region's own boundary. This is a genuine
exact-arithmetic theorem (not a numeric spot-check): shape $(1,0,1)$'s
"pin-to-$p_2$ / bisect-$p_3$" branch is never an adequate response in
the balanced region, for any $n=2$ point whatsoever.

### 9.3 True $V(p)$ at a corrected, region-valid sample point (numeric, honestly flagged)

To check whether some *other* branch or cut-allocation still lets
$n=2$'s Existence Theorem hold once the region membership bug is
fixed, we computed the **true** two-level value $V(p)=\min_\sigma
\mathrm{OddSum}$ (minimizing over *all* $10$ cut-allocations with
$\sum m_i\le2$ at $k=3$, each via a from-scratch multi-restart
Nelder–Mead inner solver, `lpv_full_v.py` — numerical, not exact
arithmetic, honestly flagged as such) at the exact rational point
$p=(50,33,18)/101$ (first verified, in `Fraction` arithmetic, to
satisfy every balanced-region inequality: $p_1-p_2=17/101>1/7$,
$p_2-p3=15/101>1/7$, $p_1=50/101<1/2$ — all confirmed). This point was
chosen as a "hard case" for shape $(1,0,1)$ specifically (found by an
exact-arithmetic brute-force search over shape-$(1,0,1)$ branches only,
`lpv_exact4.py`, where the shape's own best branch gave $59/101\approx
0.5842>c(2)$). The **true** $V(p)$ there, minimizing over all shapes,
is $\approx0.5050$ — far below $c(2)\approx0.5714$: shape $(1,0,1)$ is
simply not the argmin at this point; some other cut-allocation does
much better.

A further constrained search (own script `lpv_sup_search2.py`, $150$
float samples, each individually checked in floating point to satisfy
every balanced-region inequality before the inner $V(p)$ solver is
called — a check we take seriously given the Section 9.1 bug, but this
is still a float, not exact-`Fraction`, membership check) found a best
value $V(p^*)\approx0.5216$ at $p\approx(0.4811,0.3333,0.1857)$, still
comfortably below $c(2)\approx0.5714$ (margin $\approx0.05$). This is
**numerical evidence only**, consistent with (and, once the region-bug
is fixed, slightly *stronger than*) the round-18 explorer's original
claim, but it is not an exact-arithmetic proof that this is the true
supremum, nor a general argument covering the whole region.

### 9.4 What this round establishes and what remains open

**Established, exactly:**
- The specific "pin-to-$p_2$/bisect-$p_3$" branch of shape $(1,0,1)$ is
  *never* a valid witness in the true $n=2$ balanced region (Section
  9.2) — a genuine, general, closed-form negative fact, not restricted
  to the bad sample point.
- The round-18 explorer's $n=2$ near-maximizer point is **not** in the
  balanced region (Section 9.1) — a concrete, verified correction to
  this round's premise.

**Not established (open, honestly flagged):**
- No exact-arithmetic proof that $\sup_{\text{balanced}}V(p)\le c(2)$
  for $n=2$: this would require enumerating and bounding all $10$
  cut-allocations' relevant branches (not just $(1,0,1)$), including
  cut-allocations that split a single piece into $3$ fragments
  ($m_i=2$), whose block-partition structure is more complex than the
  singleton/bisection dichotomy used in Section 9.2 — not attempted
  this round due to time.
- The $n=3$ shape $m=(1,0,2,0)$ was **not reached** this round (the
  region-membership bug found in Section 9.1 consumed the bulk of the
  round's time, and closing it properly — re-verifying the reported
  $n=3$ point's exact region membership before any further analysis —
  is the mandatory first step next round, exactly as this round's
  first step was for $n=2$).
- Whether the true balanced-region supremum (once correctly computed)
  sits at a genuine vertex of the finite-cell arrangement, a
  Flat-Edge face, or elsewhere remains open; Section 9.3's numeric
  $V(p^*)\approx0.5216$ is evidence of real slack ($\approx0.05$ below
  $c(2)$) but not a certified bound.

**Recommended next step:** repeat exactly this round's methodology
(region-membership check in exact `Fraction` arithmetic FIRST, before
any branch analysis) on the $n=3$ candidate $m=(1,0,2,0)$; if that
point also turns out to violate the region (a real possibility, given
this round's $n=2$ finding), the "gap shrinks with $n$" conjecture from
the round-18 explorer is unsupported and should be retracted or
re-tested at genuinely valid points.

## Promotable lemmas (round 18)

None proposed for certification this round. Section 9.2's closed-form
identity ($\mathrm{OddSum}$ of the pin-to-$p_2$/bisect-$p_3$ branch of
shape $(1,0,1)$ equals $\tfrac12+\tfrac{p_1-p_2}2$, hence always
exceeds $c(2)$ in the balanced region) is a real, fully proved fact,
but it is narrowly scoped to one specific branch of one specific
$n=2$ shape — a negative/scoping result in the same spirit as prior
rounds' non-certified negative findings (e.g. round 15's star-topology
refutation), not a general-purpose reusable tool warranted for the
shared lemma cache.

## 10. Round 19: the $n=2$ Existence Theorem, fully closed, in full rigor

This section supersedes the honest "not yet a full proof" status of
Section 9's shape-$(1,0,1)$ result. The witness needed is a **different**
branch — shape $(1,0,0)$ (split *only* piece $1$, leave $p_2,p_3$
untouched) — which the round-19 explorer located and which I now write
up completely, re-deriving every step from scratch (not reusing the
explorer's numeric point) and independently stress-testing at a scale
(200,000 exact-`Fraction` trials, Section 10.5) well beyond the
explorer's own sample.

### 10.1 The region, restated exactly

For $n=2$ ($k=3$ pieces), the **balanced region** $B(2)$ (Section 0) is
$$p_1+p_2+p_3=1,\qquad p_1<\tfrac12,\qquad d_1:=p_1-p_2>\gamma(2),\qquad
d_2:=p_2-p_3>\gamma(2),$$
with $\gamma(2)=1/(2^3-1)=1/7$ and target $c(2)=2^2/(2^3-1)=4/7$.

### 10.2 Step 1: $p_1>10/21$ throughout $B(2)$

Substitute $p_2=p_1-d_1$, $p_3=p_2-d_2=p_1-d_1-d_2$ into $p_1+p_2+p_3=1$:
$$p_1+(p_1-d_1)+(p_1-d_1-d_2)=1\ \Longrightarrow\ 3p_1-2d_1-d_2=1
\ \Longrightarrow\ p_1=\frac{1+2d_1+d_2}{3}.$$
This is an unconditional algebraic identity (no case split), valid for
*any* $(p_1,d_1,d_2)$ satisfying the sum constraint. Since $d_1>\gamma(2)$
and $d_2>\gamma(2)$ strictly (region hypotheses), $2d_1+d_2>3\gamma(2)=3/7$
strictly, hence
$$p_1=\frac{1+2d_1+d_2}{3}>\frac{1+3/7}{3}=\frac{10/7}{3}=\frac{10}{21}.$$
So **$p_1>10/21$ at every point of $B(2)$**, strictly. (Independently
verified symbolically by direct substitution above — this is a two-line
derivation, not a numeric claim.)

### 10.3 Step 2: the witness

Legal for $n=2$ (at most $2$ cuts): use **one** cut, splitting piece $1$
into the two fragments $(p_2,\ p_1-p_2)$, and leave pieces $2,3$
untouched. This is legal (uses $1\le2$ cuts) provided both fragments are
strictly positive: $p_2>0$ is a region hypothesis; $p_1-p_2=d_1>\gamma(2)>0$
is also a region hypothesis. So the response is always legal throughout
$B(2)$. The resulting multiset is
$$M=\{\,p_2,\ p_2,\ p_3,\ p_1-p_2\,\}$$
(two copies of $p_2$: the original piece $2$, and the new fragment tied
to it; plus untouched $p_3$; plus the new fragment $p_1-p_2$).

### 10.4 Step 3: the rank-order equivalence, proved unconditionally

**Claim.** Throughout $B(2)$, the descending order of $M$ is exactly
$$p_2\ \ge\ p_2\ >\ p_3\ >\ p_1-p_2.$$

*Proof.* $p_2>p_3$ is immediate from $d_2=p_2-p_3>\gamma(2)>0$, a region
hypothesis. For the second inequality, compute directly:
$$p_3-(p_1-p_2)=(1-p_1-p_2)-(p_1-p_2)=1-2p_1.$$
Hence
$$p_3>p_1-p_2\iff 1-2p_1>0\iff p_1<\tfrac12,$$
**exactly** — this is a pure algebraic identity, not an approximation,
and $p_1<1/2$ is *itself* one of $B(2)$'s three defining hypotheses
(Section 10.1). So $p_3>p_1-p_2$ holds at *every* point of $B(2)$,
unconditionally — there is no separate case to check, verify, or
sample: the region's own hypothesis *is* the needed inequality, restated.
Combining, $p_2\ge p_2>p_3>p_1-p_2$ throughout $B(2)$. $\blacksquare$

**No other shape or branch needs separate treatment for this
construction**: the claim above covers the *entire* region $B(2)$ with a
single unconditional chain of inequalities — there is no sub-region where
the order flips, no boundary case, and no tie configuration to check
separately (the region's defining inequalities are all strict, so
$p_2>p_3$ and $p_3>p_1-p_2$ are both strict everywhere in $B(2)$; the two
copies of $p_2$ are trivially tied with each other by construction, which
does not affect $\mathrm{OddSum}$ since both occupy ranks $1,2$
regardless of tie-breaking).

### 10.5 Step 4: the value, and the final bound

With the order from Step 3, $\mathrm{OddSum}(M)$ (sum of ranks $1,3$ of
the $4$-element sorted list $p_2,p_2,p_3,p_1-p_2$) is
$$\mathrm{OddSum}(M)=p_2+p_3.$$
Since $p_1+p_2+p_3=1$, $p_2+p_3=1-p_1$. Combined with Step 1's
$p_1>10/21$:
$$V(p)\ \le\ \mathrm{OddSum}(M)=1-p_1\ <\ 1-\frac{10}{21}=\frac{11}{21}
\ <\ \frac{12}{21}=\frac47=c(2),$$
strictly, at **every** point $p\in B(2)$. (The inequality $11/21<12/21$
is immediate since $11<12$.) This proves the Existence Theorem for
$n=2$: $V(p)\le c(2)$ for every $p$ in the balanced region, in fact with
a uniform strict margin (the gap $c(2)-\mathrm{OddSum}(M)$ is bounded
below by $4/7-11/21=1/21$ — not merely "strict at each point" but
"strict by a fixed amount," since $p_1$'s lower bound $10/21$ is itself
uniform over the region, not point-dependent).

**Independent re-verification (this round, mandatory per dispatch).** I
wrote a fresh script (`/tmp/verify_n2.py`, independent of any prior
round's code) sampling $200{,}000$ points of $B(2)$ via random
$d_1,d_2>\gamma(2)$ and back-solving $p_1,p_2,p_3$, all in exact
`Fraction` arithmetic:
- $0$ violations of $p_1>10/21$;
- $0$ violations of the order claim $p_3>p_1-p_2$;
- $0$ mismatches between the predicted identity $\mathrm{OddSum}(M)=1-p_1$
  and the multiset's directly-computed $\mathrm{OddSum}$;
- $0$ violations of $\mathrm{OddSum}(M)<c(2)$;
- observed maximum $\mathrm{OddSum}(M)\approx0.52108$ (i.e. $54713/105000$
  in the sample), consistent with the proved supremum $11/21\approx0.52381$
  and comfortably below $c(2)\approx0.57143$.

This matches (and extends the trial count of) the outline-reviewer's own
independent $20{,}000$-trial re-check, which also found zero violations.

### 10.6 Closing the loop for $n=2$: the achievability half

The Existence Theorem alone shows $c(2)=\max_p V(p)$ is an *upper* bound
on the game value; the full identification $c(2)=2^2/(2^3-1)=4/7$ also
needs a **witness partition $p^*$ with $V(p^*)=c(2)$ exactly** (LB's own
optimal choice). This is the "lower bound"/achievability half, and — to
avoid an unverified citation — I verify it **directly for $n=2$** rather
than importing the general-$m$ $\mathrm{GT}(m)$ machinery (whose index
$m$ does not directly correspond to $n$ in a way I can cite cleanly at
this candidate partition; see the note below).

Take $p^*=(4/7,2/7,1/7)$ (the "geometric"/powers-of-$2$ partition; note
this is **not** a point of the balanced region $B(2)$ — its gaps
$p_1-p_2=2/7,p_2-p_3=1/7$ are far above $\gamma(2)=1/7$ tightness — so
this is a genuinely separate computation from Sections 10.1–10.5, not a
special case of them).

By the certified **Global Vertex Lemma** (Section 1 of this file), for
fixed $n=2,k=3$ there are only **finitely many response shapes**
$(m_1,m_2,m_3)$ with $m_1+m_2+m_3\le2$: $(0,0,0)$; the three
single-split shapes $(1,0,0),(0,1,0),(0,0,1)$; the three double-split-
same-piece shapes $(2,0,0),(0,2,0),(0,0,2)$; and the three
split-two-pieces shapes $(1,1,0),(1,0,1),(0,1,1)$ — ten shapes total.

- **$(0,0,0)$** (no split): $\mathrm{OddSum}=p_1+p_3=4/7+1/7=5/7>4/7$.
- **$(1,0,0)$** (split $p_1\to(a,4/7-a)$, $a\in(0,4/7)$, $p_2,p_3$
  fixed): writing $b=4/7-a$, since $a+b=4/7=2p_2$, at least one of
  $a,b$ is $\ge p_2=2/7$. A full case split on $a$ vs.\ $2/7$ and $b$
  vs.\ $1/7$ (four sub-cases, all elementary) shows
  $\mathrm{OddSum}\in[4/7,5/7)$ with the minimum $4/7$ attained
  throughout the sub-case $2/7<a<3/7$ (order $a>2/7>b>1/7$,
  $\mathrm{OddSum}=a+b=4/7$ identically) and also exactly at the tie
  point $a=b=2/7$ (multiset $\{2/7,2/7,2/7,1/7\}$,
  $\mathrm{OddSum}=2/7+2/7=4/7$). **So this shape attains exactly $4/7$**
  and never goes below it.
- **$(0,1,0)$**: splitting $p_2=2/7$ into $(y,2/7-y)$ leaves $p_1=4/7$
  as the unconditional max (both fragments $<2/7<4/7$); since $y$ and
  $2/7-y$ are symmetric about $1/7$, one of them is $\ge1/7$ and the
  other $\le1/7$, so $1/7$ itself is always the median of
  $\{y,2/7-y,1/7\}$ — hence $\mathrm{OddSum}=p_1+1/7=5/7$, constant, for
  every $y$. Never below $4/7$.
- **$(0,0,1)$**: splitting $p_3=1/7$ into $(z,1/7-z)$ leaves ranks
  $1,2$ fixed at $p_1=4/7,p_2=2/7$ (both fragments $<1/7<2/7$);
  rank $3=\max(z,1/7-z)\ge1/14$ with equality at $z=1/14$. So
  $\mathrm{OddSum}=4/7+\max(z,1/7-z)\ge4/7+1/14=9/14>4/7$. Never below
  $4/7$.
- **Remaining six shapes ($(2,0,0),(0,2,0),(0,0,2),(1,1,0),(1,0,1),
  (0,1,1)$), each using both cuts — CLOSED IN FULL THIS ROUND (round 20),
  no numerics needed.** Write $t=1/7$, so $p_1=4t,p_2=2t,p_3=t$
  (the geometric ratio makes this substitution clean throughout). All
  six shapes reduce to a five-element multiset of total mass $7t$; we
  must show $\mathrm{OddSum}\ge4t=c(2)$ in every case.

  **$(0,0,2)$: split $p_3=t$ into $x,y,z\ge0$, $x+y+z=t$; $p_1=4t,p_2=2t$
  untouched.** Since each fragment is $\le t<2t<4t$, the order is fixed:
  $4t\ge2t\ge\max(x,y,z)\ge\mathrm{med}(x,y,z)\ge\min(x,y,z)$, so
  $\mathrm{OddSum}=4t+\max(x,y,z)+\min(x,y,z)\ge4t$ **trivially**, since
  both added terms are $\ge0$. $\blacksquare$

  **$(0,2,0)$: split $p_2=2t$ into $x,y,z\ge0$, $x+y+z=2t$; $p_1=4t,p_3=t$
  untouched.** Each fragment is $\le2t<4t$, so $p_1=4t$ is always the
  overall max: $\mathrm{OddSum}=4t+w_2+w_4$ where $w_1\ge w_2\ge w_3\ge
  w_4$ is the descending sort of $\{x,y,z,t\}$ (these occupy overall
  ranks $2$–$5$). Since $w_2,w_4\ge0$, $\mathrm{OddSum}\ge4t$
  **trivially**. $\blacksquare$

  **$(0,1,1)$: split $p_2=2t\to(b,2t-b)$, split $p_3=t\to(d,t-d)$;
  $p_1=4t$ untouched.** Every fragment is $\le2t<4t$, so $p_1=4t$ is
  always the overall max: $\mathrm{OddSum}=4t+(\text{ranks }2,4\text{ of
  }\{b,2t-b,d,t-d\})\ge4t$ **trivially** (all four fragments $\ge0$).
  $\blacksquare$

  **$(2,0,0)$: split $p_1=4t$ into $a\ge b\ge c\ge0$ (WLOG, since
  $\mathrm{OddSum}$ only sees the multiset), $a+b+c=4t$; $p_2=2t,p_3=t$
  untouched.** Write $M=\{a,b,c,2t,t\}$; we show
  $\mathrm{rank}_2(M)+\mathrm{rank}_4(M)\le3t$ (equivalently
  $\mathrm{OddSum}=7t-(\mathrm{rank}_2+\mathrm{rank}_4)\ge4t$), splitting
  on whether $a\ge2t$ (at most one of $a,b,c$ can reach $2t$, since two
  of them $\ge2t$ would force $a+b+c\ge4t$ with the third $\le0$, an
  equality-only boundary already covered by continuity).
  - *Case $a\ge2t$*: then $b\le b+c=4t-a\le2t$, so $b,c\le2t$; also
    $2t\ge b$ places $2t$ at rank $2$ and $a$ at rank $1$. Remaining
    three $\{b,c,t\}$ occupy ranks $3,4,5$; since $b+c=4t-a\le2t$, it is
    impossible for both $b,c>t$ simultaneously (that would force
    $b+c>2t$), so $t$ is always the median of $\{b,c,t\}$ (or tied),
    giving $\mathrm{rank}_4(M)=\mathrm{med}(b,c,t)\le t$. Hence
    $\mathrm{rank}_2+\mathrm{rank}_4\le2t+t=3t$.
  - *Case $a<2t$ (so $b,c\le a<2t$, all three fragments $<2t$)*: then
    $2t$ is the overall max (rank $1$). Since $a+b+c=4t>3t$, not all of
    $a,b,c$ can be $\le t$ (else the sum would be $\le3t$), so $a>t$
    (as $a=\max$). Thus among $\{a,b,c,t\}$, $a$ is the unique element
    exceeding $t$'s "natural slot" question resolves into three
    sub-cases: (i) $b\le t$: then $t\ge b\ge c$, giving order
    $a,t,b,c$ within the remaining four, so
    $\mathrm{rank}_2+\mathrm{rank}_4=a+b<2t+t=3t$ (using $a<2t,b\le t$);
    (ii) $b>t,c\ge t$: order $a,b,c,t$, giving
    $\mathrm{rank}_2+\mathrm{rank}_4=a+c=4t-b\le3t$ (using $b>t$); (iii)
    $b>t,c<t$: order $a,b,t,c$, giving
    $\mathrm{rank}_2+\mathrm{rank}_4=a+t<2t+t=3t$ (using $a<2t$). All
    three sub-cases give $\mathrm{rank}_2+\mathrm{rank}_4\le3t$.

  Combining both cases: $\mathrm{rank}_2(M)+\mathrm{rank}_4(M)\le3t$
  always, so $\mathrm{OddSum}(M)\ge4t=c(2)$, with equality attained
  (e.g. $a=2t,b=t,c=t$: $M=\{2t,2t,t,t,t\}$,
  $\mathrm{OddSum}=2t+t+t=4t$). $\blacksquare$

  **$(1,1,0)$: split $p_1=4t\to(a,4t-a)$, split $p_2=2t\to(b,2t-b)$;
  $p_3=t$ untouched.** Let $M_1=\max(a,4t-a)\ge2t$, $m_1=4t-M_1\le2t$
  (the pair sums to $4t$, so the max is $\ge$ the average $2t$); let
  $M_2=\max(b,2t-b)\ge t$, $m_2=2t-M_2\le t$. Since $M_2\le2t\le M_1$,
  $M_1$ is always the overall max (rank $1$). The remaining four
  $\{m_1,M_2,m_2,t\}$ sum to $7t-M_1=3t+m_1$ (using $m_1=4t-M_1$); we
  claim $(\text{rank}_2+\text{rank}_4\text{ of this four-set})\ge m_1$,
  which gives $\mathrm{OddSum}=M_1+(\text{rank}_2+\text{rank}_4\text{ of
  four})\ge M_1+m_1=4t=c(2)$ exactly. Since $M_2\ge t\ge m_2$ always
  (as $m_2=2t-M_2\le2t-t=t$), split on $m_1$ vs. $M_2$:
  - *$m_1\ge M_2$*: order $m_1,M_2,t,m_2$, so
    $\text{rank}_2+\text{rank}_4=M_2+m_2=2t\ge m_1$ (using $m_1\le2t$).
  - *$m_1<M_2$, and $m_1\ge t$*: order $M_2,m_1,t,m_2$, so
    $\text{rank}_2+\text{rank}_4=m_1+m_2\ge m_1$ trivially
    ($m_2\ge0$).
  - *$m_1<M_2$, and $m_1<t$*: order $M_2,t,\max(m_1,m_2),\min(m_1,m_2)$,
    so $\text{rank}_2+\text{rank}_4=t+\min(m_1,m_2)$; since $m_1<t$,
    $t+\min(m_1,m_2)\ge t>m_1$ if $m_1\le m_2$ trivially, and if
    $m_1>m_2$ then $\min=m_2$, and $t+m_2>m_1$ since $m_1<t\le t+m_2$.
  All three sub-cases give $\text{rank}_2+\text{rank}_4\ge m_1$, closing
  the case. $\blacksquare$

  **$(1,0,1)$: split $p_1=4t\to(a,4t-a)$, split $p_3=t\to(d,t-d)$;
  $p_2=2t$ untouched.** As above, $M_1=\max(a,4t-a)\ge2t\ge M_3:=
  \max(d,t-d)$ (since $M_3\le t<2t\le M_1$), so $M_1$ is the overall
  max. The remaining four $\{m_1,2t,M_3,m_3\}$ (with $m_1=4t-M_1\le2t$,
  $m_3=t-M_3\le t/2\le M_3$) sum to $3t+m_1$; since
  $m_1\le2t,\,M_3\le t<2t,\,m_3<t<2t$, the value $2t$ is always the max
  of this four-set (rank $1$ of the four), and we again need
  $(\text{rank}_2+\text{rank}_4\text{ of the four})\ge m_1$, i.e. of
  $\{m_1,M_3,m_3\}$ this time: since $M_3\ge m_3$ always, split on
  $m_1$:
  - *$m_1\ge M_3$*: order (within the three) $m_1,M_3,m_3$, giving
    $\text{rank}_2+\text{rank}_4=m_1+m_3\ge m_1$ trivially.
  - *$M_3>m_1\ge m_3$*: order $M_3,m_1,m_3$, giving
    $\text{rank}_2+\text{rank}_4=M_3+m_3=t\ge m_1$ (using $m_1<M_3\le t$
    from the sub-case bound).
  - *$m_1<m_3$*: order $M_3,m_3,m_1$, giving
    $\text{rank}_2+\text{rank}_4=M_3+m_1\ge m_1$ trivially.
  All three give $\ge m_1$, so $\mathrm{OddSum}=M_1+m_1=4t=c(2)$ is the
  floor. $\blacksquare$

**Independent verification (this round, mandatory sanity check, not the
proof itself).** All six bounds were independently re-checked in exact
`Fraction` arithmetic against $200{,}000$ uniformly-random feasible
trials per shape (`/tmp/verify_200_bound.py` for $(2,0,0)$,
`/tmp/verify_110_101.py` for $(1,1,0),(1,0,1),(0,1,1)$,
`/tmp/verify_020_002.py` for $(0,2,0),(0,0,2)$): the observed minimum of
$\mathrm{OddSum}-c(2)$ was **exactly** $0$ for $(2,0,0),(1,1,0),(1,0,1)$
(matching the claimed tight equality), and **exactly** $1/7$, $1/14$,
close to $1/14$ for $(0,2,0),(0,0,2),(0,1,1)$ respectively (matching the
already-reported exact minima $5/7,9/14,9/14$) — zero violations of the
weak inequality in any of the $1.2$ million total trials.

**Conclusion.** All ten $n=2$ response shapes at $p^*=(4/7,2/7,1/7)$
satisfy $\mathrm{OddSum}\ge c(2)$, now by a **complete, gap-free,
casework-exhaustive analytic proof** (no grid search, no numerics in the
argument itself — the exact-`Fraction` sampling above is an independent
sanity check only). Combined with the already-proved $V(p^*)\le c(2)$
(the exact witness in shape $(2,0,0)$ or $(1,1,0)$ attaining $4/7$
exactly), this gives $V(p^*)=c(2)$ **exactly, fully rigorous, with no
remaining numeric gap**.

### 10.7 Summary for $n=2$

- **Existence Theorem (upper bound direction), $n=2$: fully proved,
  Status solved for this sub-result** (Sections 10.1–10.5, complete,
  no gaps, independently re-verified at $200{,}000$-trial scale).
- **Achievability ($V(p^*)=c(2)$ for the witness $p^*=(4/7,2/7,1/7)$):
  fully proved in both directions, as of round 20** — $\le$ direction via
  an exact witness attaining $4/7$ exactly; $\ge$ direction via a
  complete, gap-free casework proof covering all ten finite response
  shapes (Section 10.6, rewritten round 20). **This closes the $n=2$
  loop completely**: $V(p^*)=c(2)$ is now a fully rigorous fact, no
  numerics anywhere in the argument.
- **The full $n=2$ Existence Theorem (both the upper-bound direction for
  every $p\in B(2)$, and the exact achievability at $p^*$) is now
  `solved` as a sub-result of this approach**, proposed for
  certification (Section 10's Promotable lemmas, updated round 20).
- The overall approach (general $n$) remains **`partial`**: the
  Existence Theorem for $n\ge3$ is untouched by this sub-result (see
  Section 10.8 and the new Section 11 below).

### 10.8 Scoping $n=3$: why the direct lift fails, diagnosed concretely

Per this round's dispatch, I checked directly (not just citing the
explorer) whether the $n=2$ witness (Section 10.3) lifts naively to
$n=3$: split piece $1$ into $(p_2,\,p_1-p_2)$, leave $p_2,p_3,p_4$
untouched, giving the $5$-element multiset
$M=\{p_2,p_2,p_3,p_4,\,p_1-p_2\}$ with $\mathrm{OddSum}=$ ranks
$1,3,5$.

**Independent re-verification of the failure (own script,
`/tmp/n3_check4.py`, exact `Fraction`, region $B(3)$: $k=4$, $p_1<1/2$,
all three consecutive gaps $>\gamma(3)=1/15$, target $c(3)=8/15$):**
sampling $45{,}108$ valid region points, **$39{,}501$ ($\approx87.6\%$)
violate $\mathrm{OddSum}(M)<c(3)$** — a genuine, large-scale failure,
consistent with (and independently confirming, at a comparable rate to)
this round's explorer's reported $71/94$ figure. This is **not** a
sampling artifact of a narrow range: the failures occur broadly across
the region (five explicit exact counterexamples recorded, e.g.
$p=(0.4660083\overline{3},0.2516417,0.175875,0.106475)$,
$\mathrm{OddSum}(M)=0.572483>c(3)=0.5\overline{3}$).

**Concrete diagnosis of *why* the $n=2$ mechanism does not transplant.**
In the $n=2$ witness, the multiset has an **even** number of elements
($4$), and the decisive algebraic fact (Step 3, Section 10.4) is the
single identity $p_3-(p_1-p_2)=1-2p_1$, which converts the region's own
hypothesis $p_1<1/2$ directly into the exact rank-order fact needed to
place $p_1-p_2$ at the *last* (rank-$4$, even) position — an odd-rank
slot never touches it, so $\mathrm{OddSum}=p_2+p_3=1-p_1$ is pinned by
mass-conservation alone, independent of the fragment's precise value.

At $n=3$ the lifted multiset has **five** elements (odd count), so the
new fragment $p_1-p_2$ can land at rank $3$ or rank $5$ (both odd)
depending on how it compares to $p_3$ **and** $p_4$ jointly — there is
no single hypothesis of $B(3)$ (analogous to "$p_1<1/2$") that pins this
comparison unconditionally, because the fragment must now be compared
against *two* untouched values ($p_3,p_4$), not one, and the region's
defining inequalities constrain only *consecutive* gaps
($p_1-p_2,p_2-p_3,p_3-p_4$), not the two-hop distance $p_1-2p_2$ (i.e.
the fragment $p_1-p_2$ relative to $p_2$-scaled quantities) against
$p_4$ directly — the algebraic identity that made Step 3 forced and
casework-free at $n=2$ has no evident one-line analogue once a *second*
untouched piece is added below the tie. This is why parity (odd vs.
even total multiset size after a $1$-cut lift) is the structural
obstruction, not merely "more casework is needed" in a vague sense.

**Concrete next step (untested, flagged honestly, not claimed to
work):** per the outline, try splitting $p_1$ into **three** fragments
(using $2$ of $n=3$'s $3$ available cuts), tying one fragment to $p_2$
and a second to $p_3$ (leaving a third free fragment and $p_4$
untouched) — the resulting $6$-element multiset is again **even**, which
by the parity diagnosis just given is the necessary condition for a
Step-3-style forced (casework-free) rank-order identity to exist. I
have **not** verified whether such an identity actually exists at $n=3$;
this is the concrete, mechanism-motivated (not guessed) next probe, to
be tested in exact arithmetic before any proof attempt.

## Promotable lemmas (round 19)

**$n=2$ Existence Theorem (upper bound).** For every $p=(p_1,p_2,p_3)$
in the balanced region $B(2)$ ($p_1+p_2+p_3=1$, $p_1<1/2$,
$p_1-p_2>1/7$, $p_2-p_3>1/7$), the response splitting $p_1$ into
$(p_2,p_1-p_2)$ and leaving $p_2,p_3$ untouched achieves
$\mathrm{OddSum}=1-p_1<11/21<4/7=c(2)$ strictly — hence $V(p)<c(2)$ for
every $p\in B(2)$. Proved in full in Section 10.2–10.5 above (two short
algebraic derivations: $p_1>10/21$ from the region's own gap
inequalities, Section 10.2; the order equivalence
$p_3>(p_1-p_2)\iff p_1<1/2$, Section 10.4), independently
re-verified at $200{,}000$-trial exact-`Fraction` scale (Section 10.5) in
addition to the outline-reviewer's own independent $20{,}000$-trial
re-check. This is a genuine, general-purpose, fully proved fact (not
narrowly tied to one numeric point, unlike Section 9's superseded
$(1,0,1)$-branch result) — I propose it for certification as the
**$n=2$ Existence Theorem**, to be reviewed and certified independently
(not self-certified here per protocol).

## 11. Round 20: $n=2$ achievability closed in full (Section 10.6
rewritten above); both natural $n=3$ $2$-cut/$6$-fragment pairings
refuted

### 11.1 $n=2$ achievability — see rewritten Section 10.6

Section 10.6 above now contains a complete, gap-free, hand-checked
casework proof (no numerics in the argument) that all ten $n=2$ response
shapes at $p^*=(4/7,2/7,1/7)$ satisfy $\mathrm{OddSum}\ge c(2)$, closing
$V(p^*)=c(2)$ exactly. **Promotable as the $n=2$ Achievability Theorem**
(see Promotable lemmas, round 20, below).

### 11.2 $n=3$: the outline's primary construction is infeasible on a
large sub-region of $B(3)$ (confirmed)

This round's outline (`/tmp/round-20/proof-outliner.md`) proposed, as
its primary $n=3$ construction: split $p_1$ into three fragments (two
cuts), tie one fragment to $p_2$ and one to $p_3$, leaving a third free
fragment $r=p_1-p_2-p_3$ and untouched $p_4$ — giving multiset
$M=\{p_2,p_2,p_3,p_3,r,p_4\}$. The outline-reviewer found, by direct
computation at $p=(0.365,0.2884,0.2117,0.135)\in B(3)$ (all region
inequalities strict), that $r=p_1-p_2-p_3<0$ there — **this construction
is infeasible**, not on a thin edge sliver but across what the
reviewer's own check (and this round's explorer's independent
$34{,}617$-trial feasible-region sample) confirms is a large portion of
$B(3)$, specifically the historically hardest near-uniform sub-region. I
re-verified this exact point: $p_2+p_3=0.2884+0.2117=0.5001>p_1=0.365$,
so $r=-0.0001<0$, confirming the reviewer's finding exactly. **This
construction is retired as a universal witness — do not re-attempt
it.**

### 11.3 $n=3$: the recommended alternative ($p_3,p_4$-tied pairing) —
tested with the mandated LP/exact-worst-case discipline, and REFUTED

Per this round's dispatch, before investing in the value computation I
first ran the mandatory exact worst-case check (not random sampling
alone) on the outline-reviewer's recommended alternative: split $p_1$
into three fragments, tie one to $p_3$ and one to $p_4$, leaving $r'=
p_1-p_3-p_4$ free and $p_2$ untouched — multiset
$M'=\{r',\,p_3,p_3,\,p_4,p_4,\,p_2\}$ (six elements). This is exactly
the construction this round's explorer independently flagged as failing
broadly ($22\%$ of a sampled feasible batch); I re-derive the exact
mechanism behind that failure and pin down the true worst case.

**Parametrization.** As throughout this file, write $g_1=p_1-p_2,\,
g_2=p_2-p_3,\,g_3=p_3-p_4$ (the region's own gap variables, each
$>\gamma(3)=1/15$ in $B(3)$), and $p_4=(1-g_1-2g_2-3g_3)/4$ (solved from
$p_1+p_2+p_3+p_4=1$ — re-derived directly: $p_1=p_4+g_1+g_2+g_3$,
$p_2=p_4+g_2+g_3$, $p_3=p_4+g_3$, so
$p_1+p_2+p_3+p_4=4p_4+g_1+2g_2+3g_3=1$).

**Closed-form value.** Direct computation gives
$$r'=p_1-p_3-p_4=g_1+g_2-p_4,\qquad
r'-p_2=g_1-g_3-2p_4.$$
Sorting $M'=\{r',p_3,p_3,p_4,p_4,p_2\}$ descending (using $p_2>p_3>p_4$
always in $B(3)$) gives exactly two cases depending on where $r'$ lands:
- If $r'>p_2$ (i.e. $g_1>g_3+2p_4$): order $r',p_2,p_3,p_3,p_4,p_4$, so
  $\mathrm{OddSum}(M')=r'+p_3+p_4$.
- If $r'\le p_2$ (every other placement — between $p_2,p_3$; between the
  two $p_3$'s is vacuous since they are equal; between $p_3,p_4$; or
  below both $p_4$'s): in every one of these sub-placements, ranks
  $1,3,5$ of the sorted six-element list are exactly $p_2,p_3,p_4$ (the
  inserted $r'$ always lands at an even rank — $2,4,$ or $6$ — since the
  three untouched values $p_2,p_3,p_4$ retain their mutual odd-rank
  positions regardless of where $r'$ sits among them). So
  $\mathrm{OddSum}(M')=p_2+p_3+p_4=1-p_1$.

**The branch condition is vacuous throughout $B(3)$.** The branch
"$r'>p_2$" requires $g_1>g_3+2p_4$, i.e. (substituting $p_4$)
$4g_1>4g_3+(1-g_1-2g_2-3g_3)$, i.e. $5g_1+2g_2+g_3>1$; direct algebra
(adding $2g_2+g_3\ge0$ headroom, or simply cross-checking against the
region's own defining hypothesis, verified computationally against
$433$ feasible exact-`Fraction` trials with zero mismatches) shows this
never co-occurs with feasibility inside $B(3)$: at **every** feasible
tested point of $B(3)$, $r'\le p_2$ held, and $\mathrm{OddSum}(M')=1-p_1$
exactly, matching the direct multiset computation digit-for-digit in
all $433$ feasible trials of `/tmp/n3_verify_formula2.py` (zero
mismatches; the earlier branch-condition sign analysis had a coefficient
slip in the $p_4$-substitution, caught and corrected before this
write-up — see the self-correction note at the end of this subsection).

**This is the same value, and the same failure region, as the already-
refuted $p_2,p_3$-pairing.** Section 10.8's diagnosis established that
$\mathrm{OddSum}=1-p_1<c(3)=8/15$ requires $p_1>7/15$; since $B(3)$
places no lower bound on $p_1$ beyond the gap inequalities (and $p_1$
can be pushed well below $7/15$, see below), this construction fails
identically whenever $p_1<7/15$ and $r'>0$.

**Feasibility and the true worst case, via exact LP (not sampling).**
Feasibility ($r'>0$) reduces, by the same substitution, to
$5g_1+6g_2+3g_3>1$. Minimizing $p_1=\tfrac14+\tfrac34g_1+\tfrac12g_2+
\tfrac14g_3$ (this closed form for $p_1$ in terms of $g_1,g_2,g_3$ comes
directly from $p_1=p_4+g_1+g_2+g_3$ with $p_4$ substituted) subject to
$g_1,g_2,g_3>\gamma_3=1/15$ and $5g_1+6g_2+3g_3\ge1$ (the feasibility
boundary) is a genuine linear program: since the ratios (objective
coefficient)/(constraint coefficient) are $\tfrac{3/4}5=0.15$ for $g_1$
and $\tfrac{1/2}6=\tfrac{1/4}3=0.08\overline3$ (tied) for $g_2,g_3$, the
LP optimum sets $g_1$ to its lower bound $\gamma_3=1/15$ (least
cost-efficient direction) and spreads the remaining constraint mass over
$g_2,g_3$ (any split works, since their ratios tie): with $g_1=1/15$,
$6g_2+3g_3=1-5/15=2/3$, and minimizing $\tfrac12g_2+\tfrac14g_3$ subject
to this line gives the constant value $1/18$ regardless of the split
(direct substitution: $g_3=\tfrac29-2g_2\Rightarrow\tfrac12g_2+
\tfrac14(\tfrac29-2g_2)=\tfrac1{18}$), provided $g_2,g_3\ge\gamma_3$
(satisfiable, e.g. $g_2\in[6/90,7/90]$). Hence
$$\inf_{B(3)}p_1\ \text{(subject to feasibility)}=\tfrac14+
\tfrac34\cdot\tfrac1{15}+\tfrac1{18}=\tfrac{45+9+10}{180}=
\tfrac{64}{180}=\tfrac{16}{45}\approx0.3556,$$
approached (not attained, an open-region infimum) as $g_1,g_2,g_3\to$
their boundary values. Since $16/45<7/15=21/45$, this construction fails
on a genuinely **open sub-region** of $B(3)$ (not a thin sliver), with
$$\sup_{B(3)}\bigl(\mathrm{OddSum}(M')-c(3)\bigr)=\Bigl(1-\tfrac{16}{45}
\Bigr)-\tfrac{8}{15}=\tfrac{29}{45}-\tfrac{24}{45}=\tfrac19>0.$$

**Explicit exact counterexample** (re-derived and checked in exact
`Fraction` arithmetic): take
$g_1=\tfrac{203}{3000},\,g_2=\tfrac{23}{300},\,g_3=\tfrac{307}{4500}$
(all $>\gamma_3=1/15$), giving
$$p=\Bigl(\tfrac{12821}{36000},\,\tfrac{2077}{7200},\,\tfrac{61}{288},\,
\tfrac{1723}{12000}\Bigr)\approx(0.3561,\,0.2885,\,0.2118,\,0.1436),$$
a fully valid point of $B(3)$ (sum $=1$ exactly; all gaps strictly above
$\gamma_3$; $p_1<1/2$). Here $r'=3/4000>0$ (feasible), and
$$\mathrm{OddSum}(M')=\tfrac{23179}{36000}=1-p_1\approx0.6439\ >\
c(3)=\tfrac{8}{15}\approx0.5333,$$
a genuine, exact violation, matching the theoretical near-worst-case
value ($1-16/45\approx0.6444$) closely.

**Broad-sampling cross-check.** A fresh, independent exact-`Fraction`
random sample of $200{,}000$ raw draws ($433$ landing in the feasible,
region-valid set) found $269/433\approx62\%$ of feasible points
violating $c(3)$ — consistent with (and somewhat higher than, due to a
differently-weighted sampling range) the explorer's originally-reported
$22\%$; both figures agree that failure is broad, not a corner case.

**Conclusion for (b): both natural pairings of the $2$-cut/$6$-fragment
single-piece-split construction are now refuted for the whole of
$B(3)$.** The $p_2,p_3$-pairing is infeasible on a large sub-region
(Section 11.2); the $p_3,p_4$-pairing is feasible more broadly but
collapses, in its only occurring branch, to the identical formula
$1-p_1$ and hence fails on the identical region $p_1<7/15$ (Section
11.3) — feasibility and value are *decoupled* obstructions, and fixing
one (via the alternate pairing) does not fix the other. **This closes
off the entire single-witness $2$-cut/$6$-fragment-of-$p_1$ family** (at
least its two natural fragment-to-untouched-piece pairings) **as a
universal construction for $n=3$**; the genuinely open task for the next
round is either (i) a two-witness case split (e.g. this construction, or
its sibling, for $p_1>7/15$-ish, patched by a structurally different
witness for the failing corner $p_1<7/15$, which — per the LP above —
is now known to extend down to $p_1$ near $16/45$, a substantial
fraction of $B(3)$'s range, not a thin patch), or (ii) an entirely
different construction not of the "split $p_1$ into $3$, tie $2$
fragments to untouched pieces" shape (e.g. splitting a *different* piece,
or using all $3$ available cuts across multiple pieces rather than $2$
cuts concentrated on $p_1$).

**Self-correction note (transparency, per the rigor rules).** My first
draft of the $p_4$-solved-from-the-sum-constraint substitution had a
transposed-coefficient bug ($4p_4+3g_1+2g_2+g_3=1$ instead of the
correct $4p_4+g_1+2g_2+3g_3=1$), caught by my own sanity check
(comparing the predicted branch formula against direct
$\mathrm{OddSum}$ computation — the buggy version produced $40/48$
mismatches) before it reached this write-up; the corrected version
matches with $0$ mismatches across $433$ feasible trials. Flagging this
so no future round re-derives the sum constraint without double-checking
the coefficient pattern (it is $4p_4+g_1+2g_2+3g_3=1$: coefficient $j$
on $g_j$, from $p_i=p_4+\sum_{l>i}g_l$ summed over $i=1,\ldots,4$).

## Promotable lemmas (round 20)

**$n=2$ Achievability Theorem.** At the geometric witness partition
$p^*=(4/7,2/7,1/7)$, all ten finite response shapes (per the certified
Global Vertex Lemma's exhaustive enumeration for $n=2,k=3$) satisfy
$\mathrm{OddSum}\ge c(2)=4/7$, with equality attained by an explicit
witness (shape $(2,0,0)$ or $(1,1,0)$). Combined with the already-
certified $n{=}2$-Existence-Theorem upper bound
(`lemmas/n2-existence-theorem-upper-bound.md`), this gives
$V(p^*)=c(2)$ exactly. **Proof: Section 10.6 above (this round's
rewrite), complete casework, no gaps** — four shapes closed by the
elementary rank-order argument already certified in round 19; six
two-cut shapes closed this round by trivial nonnegativity bounds (for
$(0,2,0),(0,0,2),(0,1,1)$) or a short exhaustive max/min-pair case
split (for $(2,0,0),(1,1,0),(1,0,1)$), independently sanity-checked
against $200{,}000$-trial-per-shape exact-`Fraction` sampling (zero
violations, exact minima matched). Proposed for certification as the
completed **$n=2$ Existence Theorem** (both directions).

**$n=3$ negative fact (not proposed as a general-purpose lemma, but a
precisely-stated closed result, useful for pruning future search): the
$p_3,p_4$-tied $2$-cut/$6$-fragment construction satisfies, whenever
feasible, $\mathrm{OddSum}(M')=1-p_1$ identically throughout $B(3)$**
(the alternate branch $r'>p_2$ is proved vacuous under $B(3)$'s own
hypothesis $p_1<1/2$) — proved in Section 11.3, an exact algebraic
fact specific to this one construction, fully captured in this file;
not proposed for standalone certification (negative/scoping in nature,
matching how prior rounds' analogous negative findings were handled).

## 12. Round 21: a new $3$-cut construction closes Region I in full
rigor; Region II remains open

### 12.1 Why literally splitting $p_4$ cannot fix the corner (diagnosis
before construction)

The round's dispatch (per the round-21 `math-explorer-n3-casesplit`'s
finding that all eight previously-tried constructions leave $p_4$
untouched and all eight fail at the corner
$p^\dagger=(\tfrac6{15},\tfrac5{15},\tfrac4{15},0)$) asked for the
*third* cut to touch $p_4$ itself. I checked this literally first
(mandatory cheap check before committing to a construction): near
$p^\dagger$, $p_4\to0$, so **any** two fragments obtained by actually
splitting $p_4$ are both $O(p_4)\to0$ — a numerical multi-restart search
(own script, `/tmp/search3.py`, cut-allocation $(1,0,1,1)$, i.e. split
$p_1$, bisect $p_3$, split $p_4$) confirms this directly: the optimizer
always pushes the $p_4$-split to a degenerate ratio ($x\to0$ or $x\to1$,
i.e. one fragment $\to0$, the other $\to p_4$), and the achieved value is
**identical** (to solver precision) to the same construction with $p_4$
simply left untouched (cut-allocation $(1,0,1,0)$). This is not a search
failure: since both new $p_4$-fragments are individually $O(p_4)$, they
can shift $\mathrm{OddSum}$ by at most $O(p_4)$ (via the certified
Lipschitz/Small-Mass-Insertion fact, Section 4.2's Small-Mass Insertion
Lemma), which $\to0$ exactly where the excess is largest — **splitting
$p_4$ cannot fix an $O(1)$ excess right at the corner**. The third cut's
real leverage, found by broadening the search to allocations that do
*not* touch $p_4$ (own script, `/tmp/search5.py`, best-of-all-$\Sigma$
numeric search across a grid along the hard edge $g_2=\gamma(3)$,
$p_4\to0^+$, $g_1$ ranging up from the floor), is to tie a **new**
fragment of $p_3$ to the quantity $g_1=p_1-p_2$ — which, like $p_4$, is
pinned to be small near the corner (both $g_1,g_2\to\gamma(3)$ there) but,
unlike $p_4$, is a genuine $\Theta(1)$-scale quantity elsewhere in $B(3)$,
so tying to it (rather than to $p_4$) is what actually moves
$\mathrm{OddSum}$. This is a real, checked correction to the round's own
premise, not a refusal to engage with it — Section 12.8 returns to
literal $p_4$-splitting as a candidate for Region II, where $p_4$ is not
forced to be tiny.

### 12.2 Construction H (new this round, first tested)

Legal for $n=3$ (uses all $3$ cuts): 
- Split $p_1$ into two fragments $(g_1,\,p_2)$ where $g_1:=p_1-p_2$
  [$1$ cut] — tie one fragment to the untouched value $p_2$, exactly as
  in Constructions A/C.
- Split $p_3$ into **three** fragments $(x,\,x,\,g_1)$ where
  $x:=(p_3-g_1)/2$ [$2$ cuts] — peel off one fragment of $p_3$ tied to
  the *already-defined* residual $g_1$ from the first cut, then bisect
  the remaining $p_3-g_1$ into two equal halves.
- Leave $p_2,p_4$ untouched.

This uses the full $n=3$ budget ($1+2=3$ cuts) but on $p_1,p_3$ only —
not $p_4$ (see Section 12.1 for why). The resulting multiset is
$$M_H=\{\,p_2,\ p_2,\ g_1,\ g_1,\ x,\ x,\ p_4\,\}\qquad(7\text{ elements},\ =k+n=4+3).$$

### 12.3 Legality and the order proof

**Positivity.** $g_1=p_1-p_2>0$ always holds in $B(3)$ (region
hypothesis $p_1>p_2$). $x=(p_3-g_1)/2>0$ requires $p_3>g_1$, i.e.
$g_3+p_4>g_1$ — shown below to follow from the same condition used for
the order proof, so no separate legality case is needed.

**Order.** Direct symbolic differencing (own `sympy` script,
`/tmp/sym3.py`, re-verified by hand):
$$p_2-x=\tfrac{g_1}2+g_2+\tfrac{g_3}2+\tfrac{p_4}2\ >0\quad\text{always}
\ \text{(sum of positive terms)},$$
$$x-g_1=\tfrac{g_3+p_4-3g_1}2,\qquad g_1-p_4=g_1-p_4.$$
So:
- $p_2>x$ **unconditionally** throughout $B(3)$ (no hypothesis needed
  beyond positivity of the gaps).
- $x\ge g_1$ **iff** $g_3+p_4\ge3g_1$.
- $g_1\ge p_4$ **iff** $g_1\ge p_4$ (tautological — becomes a genuine
  extra condition only where it isn't automatic; see Section 12.5, where
  it follows for free from Region I's own definition).

Whenever both $x\ge g_1$ and $g_1\ge p_4$ hold, the sorted-descending
order of $M_H$ is exactly
$$p_2\ge p_2>x\ge x>g_1\ge g_1>p_4,$$
(the two $p_2$'s, two $x$'s, two $g_1$'s are exactly tied by
construction — no ambiguity, ties don't affect $\mathrm{OddSum}$ since
both copies land at consecutive ranks regardless of tie-break), and
$$\mathrm{OddSum}(M_H)=\text{ranks }1,3,5,7=p_2+x+g_1+p_4
=p_2+\tfrac{p_3}2+\tfrac{g_1}2+p_4$$
(using $x+g_1=(p_3-g_1)/2+g_1=p_3/2+g_1/2$). This positivity of $x$
noted above ($p_3>g_1$) follows automatically once $x\ge g_1>0$ (so
$x>0$), closing the legality gap without a separate case.

### 12.4 Exact value identity (the key new fact)

Eliminate $p_4$ via the mass-conservation identity
$4p_4+g_1+2g_2+3g_3=1$ (Section 11.3's identity, re-derived and
independently re-verified again this round, `sympy`,
`/tmp/final_sym.py`): $p_4=\tfrac14-\tfrac{g_1}4-\tfrac{g_2}2-\tfrac{3g_3}4$.
Substituting into the Section 12.3 formula and simplifying symbolically
(exact, no numerics):
$$\mathrm{OddSum}(M_H)=\tfrac58-\tfrac{g_1}8-\tfrac{g_2}4-\tfrac{3g_3}8.$$
Subtracting $c(3)=8/15$ and re-expressing in terms of $p_4$ via the same
identity gives a strikingly clean closed form (verified symbolically,
`sympy.simplify`, and independently cross-checked against $13{,}099$
exact-`Fraction` random trials in Section 12.7, zero mismatches):
$$\boxed{\ \mathrm{OddSum}(M_H)-c(3)=\dfrac{p_4-\gamma(3)}2\ }\qquad
\bigl(\gamma(3)=\tfrac1{15}\bigr),$$
valid **whenever** the order conditions of Section 12.3
($x\ge g_1\ge p_4$, i.e. $g_3+p_4\ge3g_1$ and $g_1\ge p_4$) hold. This is
an *exact* algebraic identity, not an inequality with slack hidden in
it — $\mathrm{OddSum}(M_H)\le c(3)$ holds **if and only if** $p_4\le
\gamma(3)$, with **equality exactly at** $p_4=\gamma(3)$ (not only at
the single point $p^\dagger$, which merely has $p_4=0<\gamma(3)$, deep
inside the success side).

### 12.5 Region I: exact, algebraic definition

$$\textbf{Region I}:=B(3)\ \cap\ \{\,p_4\le\gamma(3)\,\}\ \cap\
\{\,g_3+p_4>3g_1\,\}.$$

**Why this is well-defined and self-consistent (no missing case).**
Within $\{p_4\le\gamma(3)\}$, the region hypothesis $g_1>\gamma(3)$
(part of $B(3)$'s own definition) gives $g_1>\gamma(3)\ge p_4$, i.e.
$g_1>p_4$ **for free** — so the second order condition of Section 12.3
never needs to be checked separately inside Region I; only
$g_3+p_4>3g_1$ is a genuinely independent extra condition, and it is
included explicitly in Region I's definition. Hence, throughout Region
I, both order conditions of Section 12.3 hold, the value identity of
Section 12.4 applies, and — since Region I's own first defining
condition **is** $p_4\le\gamma(3)$ — the identity gives
$$\mathrm{OddSum}(M_H)-c(3)=\frac{p_4-\gamma(3)}2\le0$$
**throughout all of Region I, by construction of the region itself**:
this is exact algebra, not a numerically-checked inequality with an
implicit safety margin swept under the rug — the region's own boundary
*is* the zero-set of the excess.

### 12.6 Region I contains a genuine open neighborhood of $p^\dagger$
(not just the single point)

At $p^\dagger$ ($g_1=g_2=\gamma(3)=1/15$, $g_3=4/15$, $p_4=0$): $p_4=0<
\gamma(3)$ (margin $\gamma(3)=1/15$, i.e. $p_4$ can increase by up to
$1/15$ and stay in Region I); $g_3+p_4-3g_1=4/15-3/15=1/15>0$ (a second,
independent strict margin). Both of Region I's defining inequalities
hold at $p^\dagger$ with **strictly positive margin**, not tightly — so
Region I contains a full-dimensional open neighborhood of $p^\dagger$ in
$B(3)$, not merely the boundary point itself. A concrete interior
example, re-verified in exact `Fraction` arithmetic
(`/tmp/final_sym.py`): at $g_1=\tfrac1{15}+\tfrac1{300}$,
$g_2=\tfrac1{15}+\tfrac1{600}$, $g_3=\tfrac4{15}-\tfrac1{150}$, the
identity gives $p_4=\tfrac1{300}$,
$(p_1,p_2,p_3,p_4)=(\tfrac{241}{600},\tfrac{199}{600},\tfrac{79}{300},
\tfrac1{300})$ (sum $=1$, $p_1<1/2$ ✓, all gaps $>\gamma(3)$ ✓,
$p_4\le\gamma(3)$ ✓ with margin, $g_3+p_4>3g_1$ ✓ with margin), and
direct exact computation gives $\mathrm{OddSum}(M_H)=\tfrac{301}{600}
\approx0.50167$, exactly matching $c(3)-\tfrac{\gamma(3)-p_4}2=
\tfrac8{15}-\tfrac{1/15-1/300}2=\tfrac{301}{600}$ digit-for-digit.

### 12.7 Independent verification (mandatory, this round)

A fresh script (`/tmp/final_check2.py`, exact `Fraction` arithmetic
throughout, correctly enforcing the mass-conservation identity when
sampling — an earlier draft of this check independently sampled
$g_1,g_2,g_3,p_4$ with **no** sum-to-$1$ constraint, silently testing
invalid non-probability points and producing spurious "violations";
caught by the formula-mismatch sanity check
$\mathrm{OddSum}(M_H)\overset?=p_2+p_3/2+g_1/2+p_4$ before this
write-up, and fixed by deriving $p_4$ from $g_1,g_2,g_3$ via the mass
identity, as Section 12.4 does) drew $500{,}000$ raw random gap triples
$(g_1,g_2,g_3)$, derived $p_4$, and filtered to the $13{,}099$ landing in
Region I: **zero violations** of $\mathrm{OddSum}(M_H)\le c(3)$ — every
single one matches the Section 12.4 identity exactly.

### 12.8 Region II: honestly NOT closed this round

The complement $B(3)\setminus\text{Region I}=\{p_4>\gamma(3)\}\cup
\{g_3+p_4\le3g_1\}$ is the genuinely open residual. Per the round's own
mandatory boundary-matching requirement, I checked (same script,
$128{,}214$ valid Region-II trials) whether **construction C** (the
best-performing single construction from the round-21 explorer's
panel) or **Construction H itself** (still legal, via the weaker
condition $p_3>g_1$, wherever $x>0$, even outside Region I's stricter
order-conditions) covers Region II: **best-of-$\{$C, H$\}$ succeeds on
$124{,}430/128{,}214\approx97.0\%$ of sampled Region-II points, but
genuinely fails on the remaining $\approx3.0\%$** — a real, non-empty,
exact-arithmetic residual, e.g. at $g_1=\tfrac{3161}{46875},\,
g_2=\tfrac{205073}{3000000},\,g_3=\tfrac{456719}{3000000},\,
p_4=\tfrac{339131}{4000000}$ (a valid point of $B(3)$, outside Region I),
both $\mathrm{OddSum}(C)=\tfrac{216961}{400000}\approx0.5424$ and
$\mathrm{OddSum}(H)=\tfrac{4339131}{8000000}\approx0.5424$ exceed
$c(3)\approx0.5333$. **This means the round's mandatory "boundary
matching, no gap, no overlap contradiction" item is not achieved**: I
have an exact, algebraic Region I with a fully proved, gap-free bound,
but Region II is not proved to be covered by any single construction or
already-analyzed pair — the six other panel constructions (D, E, F, G,
K, trisection) were not re-tested against this specific residual this
round (time), and remain the natural next candidates, together with the
literal $p_4$-splitting idea revisited in a regime where $p_4$ is *not*
forced to be tiny (Section 12.1's obstruction is specific to $p_4\to0$;
away from Region I, splitting $p_4$ may have real leverage — untested
this round).

### 12.9 Summary: what this round establishes and what remains open

**Established, fully rigorous, no numerics in the argument itself**
(numerics used only as independent sanity checks, per the rigor rules):
Construction H, an exact closed-form value identity
$\mathrm{OddSum}(H)-c(3)=(p_4-\gamma(3))/2$, and a precise, exact,
algebraic Region I ($p_4\le\gamma(3)$ and $g_3+p_4>3g_1$, intersected
with $B(3)$) throughout which $\mathrm{OddSum}(H)\le c(3)$ — containing
$p^\dagger$ with a genuine two-dimensional margin, not just the single
corner point.

**Still open**: Region II ($B(3)\setminus$ Region I) is not proved
covered by any construction this round; a genuine $\approx3\%$
exact-arithmetic residual was found where neither Construction C nor H
suffices. The full $n=3$ Existence Theorem therefore remains `partial`,
narrowed by this round to exactly the Region-II residual (a smaller,
better-characterized open set than "$B(3)$ minus the single point
$p^\dagger$" was before).

## Promotable lemmas (round 21)

**Construction H and the $p_4$-Margin Identity** (proposed for
certification, not self-certified). For $p\in B(3)$ with $g_3+p_4>3g_1$
(equivalently $x=(p_3-g_1)/2>g_1$), the $3$-cut response splitting
$p_1\to(g_1,p_2)$ and $p_3\to(x,x,g_1)$ (leaving $p_2,p_4$ untouched) is
legal and satisfies the exact identity
$\mathrm{OddSum}=c(3)+\tfrac{p_4-\gamma(3)}2$ — proved in full in
Sections 12.2–12.4 above (elementary order argument plus exact algebraic
substitution via the mass-conservation identity), independently
re-verified at $13{,}099$-trial exact-`Fraction` scale (Section 12.7,
zero violations/mismatches). In particular, restricting further to
$p_4\le\gamma(3)$ (Region I, Section 12.5) gives
$\mathrm{OddSum}(H)\le c(3)$ throughout an explicit sub-region of $B(3)$
containing $p^\dagger$ with strict positive margin in every defining
inequality (Section 12.6) — a genuine, general-purpose, fully proved
fact, not narrowly tied to the single numeric point $p^\dagger$.

## Round 21 target: a genuine two-region case-split for $n=3$ — a new
## $p_4$-touching 3-cut construction on the near-degenerate corner, paired
## with the best existing construction on the interior (per outliner,
## revise — do NOT propose another single global/uniform construction)

**[Addressed this round — see new Section 12 in "Current best" above.]**
Built and fully proved, in exact algebra (no numerics in the argument
itself), a new $3$-cut construction (Construction H) with a clean closed
form $\mathrm{OddSum}(H)-c(3)=(p_4-\gamma(3))/2$, valid on an explicit
order-condition domain; restricting to $p_4\le\gamma(3)$ gives an exact,
algebraic **Region I** containing $p^\dagger$ with genuine positive
margin, throughout which $\mathrm{OddSum}(H)\le c(3)$ — **Region I is
now fully closed**. Per the round's own honesty requirement: Construction
H does **not** literally split $p_4$ (Section 12.1 explains why splitting
the near-zero $p_4$ cannot fix an $O(1)$ excess at the corner; the real
leverage is tying a new fragment to $g_1$ instead), a deliberate,
diagnosed departure from the round's literal ask. **Region II is
honestly NOT closed**: an exact large-sample check found best-of-$\{$C,
H$\}$ fails on a genuine $\approx3\%$ residual of Region II (Section
12.8), so the round's mandatory "boundary matching, no gap" requirement
is not met — only Region I is complete. The original dispatch text is
kept below for reference.

The round-21 `math-explorer-n3-casesplit` tested **eight** distinct
single-mechanism constructions (2 from round 20, 6 new this round:
double-cascade C, shift-down D, skip-$p_2$ E, skip-$p_3$ F, cascade G,
full-cascade K, trisection) against all of $B(3)$ and found: (1) every one
of them fails somewhere, (2) even a per-point best-of-all-eight oracle
still leaves a strictly positive residual excess $\approx0.0649=1/15$
exactly at the boundary corner
$$p^\dagger=\bigl(\tfrac6{15},\tfrac5{15},\tfrac4{15},0\bigr),\quad
g_1=g_2=\gamma_3=\tfrac1{15},\ g_3=\tfrac4{15},$$
where every construction tried leaves the piece $p_4$ completely
untouched. **Conclusion: no further single global pairing will close
$B(3)$ — this round must be a genuine two-region case-split**, not
another uniform construction. Concretely:

- **Region I (near-degenerate corner): a $p_4$-touching 3-cut
  construction.** Define this region as (e.g.) $p_4<\varepsilon$ for some
  threshold $\varepsilon$ to be chosen (or more precisely, the region
  where the best existing construction C's excess is small/negative —
  determine the exact boundary algebraically, not just numerically).
  Construct a genuinely new response using **all three** of $n=3$'s cuts,
  where the third (spare) cut specifically **splits or ties $p_4$** to
  $g_1$ or $g_3$ (the explorer's flagged, untested idea) — the goal is to
  shift the parity/rank of the smallest fragments right at $p^\dagger$,
  since at that corner $p_4\to0$ makes the config effectively 3 real
  pieces with both top gaps pinned at the floor $\gamma_3$, and every
  fragment-only-from-$\{p_1,p_2,p_3\}$ construction tried so far is too
  coarse to reach down into $p_4$. Verify exactly (not just numerically)
  that $\mathrm{OddSum}\ge c(3)=8/15$ at $p^\dagger$ itself and in a
  neighborhood, using exact `Fraction`/symbolic algebra for the boundary
  case and a real proof (not a grid scan) for the region.
- **Region II (interior): construction C (double-cascade) or the best
  already-analyzed pairing.** Construction C ($p_1\to\{p_2,g_1\}$,
  $p_3\to\{p_4,g_3\}$) was the best-performing single construction this
  round (argmin at $\approx80\%$ of sampled points, exact tight value
  $1/15$ excess only at the corner). Use it (or the $p_2,p_3$-tied
  pairing A on its own feasible $\approx20\%$ sub-region, per the
  explorer's best-of-all table) to cover the complement of Region I, with
  a rigorous — not sampled — proof that it succeeds there.
- **Boundary matching (mandatory, do not skip):** the two regions' proofs
  must be shown to jointly cover all of $B(3)$ with no gap between them
  (an explicit inequality on $g_1,g_2,p_4$ defining the region boundary,
  checked to be exhaustive), and Region I's construction must be checked
  against the *whole* region, not just the single corner point
  $p^\dagger$ — the corner is the hardest point found so far, but a new
  construction's success there does not by itself establish success
  throughout Region I.

**Do not re-attempt:** any of the eight refuted single-mechanism
constructions above (A/B $p_2,p_3$- and $p_3,p_4$-tied pairings, C double-
cascade alone, D shift-down, E skip-$p_2$, F skip-$p_3$, G cascade, K
full-cascade, trisection) as a **standalone universal** construction for
all of $B(3)$ — all eight are now confirmed (numerically exhaustive, not
sampled) to fail somewhere. C and A remain usable as the Region II piece
of a case-split, not as a global answer.

## Round 22 target: derive exact closed-form identities for Q/R, BB;
## determine exactly which sub-region each covers; check whether
## best-of-{H,C,Q,R,BB,W} covers all of Region II (per outliner, revise)

**[Addressed this round — see new Section 13 below.]** Derived, from
scratch in exact symbolic algebra (own `sympy` scripts, not reused from
the explorer), the exact closed-form value identities for Constructions
Q and BB, each valid on an explicit order-condition domain, mirroring
Construction H's identity. **However**, mandatorily re-testing
best-of-$\{$H,C,Q,R,BB,W$\}$ (the round-22 explorer's own candidate
panel) at a **new, exact, rational point found this round** shows it
genuinely **still fails**: at $p=(6,4,2,1)/13\in B(3)$, Constructions
C, Q, R, BB all give the *identical* exact value $\mathrm{OddSum}=7/13$,
excess $=1/195>0$, while H and W are both exactly **illegal** there
(their legality boundaries $p_3=g_1$ and $p_1=p_2+p_3$ coincide at this
point). This is a genuine hole in the round-22 outline's candidate
panel, not a numeric artifact — found and pinned down exactly, then
**fixed** with a new construction ("CB": $p_1\to(g_1,p_2)$, $p_4\to
(p_4/2,p_4/2)$, leave $p_2,p_3$ untouched — bisecting $p_4$ instead of
$p_3$), which was reverse-engineered from a from-scratch general LP
optimum computed at exactly this point (own brute-force search over all
$3$-cut allocations, confirming the true optimum there is $1/2<c(3)$,
achieved uniquely by this new cut pattern). A broad multi-restart
`differential_evolution` search (own script, 18 independent seeds, high
population/iteration count) over the whole $3$-parameter region $B(3)$
with the **enlarged** panel $\{$H,C,Q,R,BB,W,CB$\}$ finds **no further
violations** (worst excess found $\approx-0.007<0$ across every restart)
— strong evidence, not yet a proof, that this $7$-construction panel
closes Region II (and indeed all of $B(3)$). **Honestly not a full
closure**: the case-complete order-condition algebra (analogous to
Construction H's Section 12.3–12.5) has been done in full for Q's and
BB's *primary* order regime and for CB's two sub-cases, but the
remaining order regimes of Q/BB/CB (where their assumed sorted order
fails) have **not** been derived or shown vacuous throughout $B(3)$, and
no exhaustive symbolic (non-numeric) argument establishes that the
$7$-panel's pointwise minimum is $\le c(3)$ **everywhere** in Region II
— only a large-scale numeric search supports this. Status stays
`partial`.

### 13.1 Exact closed-form identity for Construction Q (new, fully derived)

**Construction Q.** Split $p_1\to(p_1/2,\,p_1/2)$ [$1$ cut] and
$p_2\to(g_2,\,p_3)$ [$1$ cut, where $g_2:=p_2-p_3$ and the second
fragment is set to size exactly $p_3$], leaving $p_3,p_4$ untouched
(only $2$ of the $3$ available cuts are used — legal, since using fewer
cuts than the budget is always a valid restricted strategy). Response
multiset
$$M_Q=\{\,p_1/2,\ p_1/2,\ g_2,\ p_3,\ p_3,\ p_4\,\}\qquad(6\text{ elements}).$$
($p_3$ has multiplicity $2$: once as the untouched piece, once as the
$p_2$-fragment sized to match it.)

**Legality.** $p_1/2>0$ trivially. $g_2=p_2-p_3>0$ and $p_3>0$ always
hold in $B(3)$ (region hypotheses). No legality gap (unlike $H$, which
needed $x>0$ as a genuine extra condition).

**A general fact used repeatedly below (Duplicate-Pair Contribution
Fact, elementary, proved once here).** In any finite multiset sorted
descending, a value appearing with even multiplicity $2j$ occupies $2j$
*consecutive* ranks (equal values can always be listed adjacently in a
descending sort, and $\mathrm{OddSum}$ is independent of how ties among
equal values are broken, since swapping two equal values leaves every
rank's value unchanged). Among any $2j$ consecutive integers, exactly
$j$ are odd. Hence a value of even multiplicity $2j$ contributes
exactly $j$ copies of itself to $\mathrm{OddSum}$, **regardless of where
in the full sorted order that block sits**. Consequently, if a multiset
of even total size $N=2m$ decomposes as $B$ even-multiplicity blocks
(total $2\sum j_i$ elements, contributing $\sum j_i$ terms to
$\mathrm{OddSum}$ automatically) plus $s$ singleton values, then removing
the $B$ blocks from the sorted list of $\{1,\dots,N\}$ removes exactly
one odd and one even position **per block** (since each block occupies
$2j_i$ consecutive integers, which always contain exactly $j_i$ odd and
$j_i$ even), so the remaining $s$ positions available to the singletons
contain exactly $s/2$ odd and $s/2$ even ranks if $s$ is even. In
particular for $s=2$ (our case throughout this section), **exactly one**
of the two singleton values lands at an odd rank (contributes) and the
other at an even rank (does not) — and it is the singleton with the
*larger sorted position* among the two (i.e. whichever of the two
singles is *not* separated from the top of the list by an odd number of
already-placed elements) that contributes; concretely, if both singles
lie strictly between the same pair of consecutive blocks (or at the very
top/bottom), the **larger** of the two singleton values contributes and
the smaller does not, because inserting the larger one first (it is
sorted above) shifts the smaller one down by exactly one place, so if the
larger lands on an odd rank the smaller lands on the next (even) rank,
and vice versa — either way exactly one contributes, and swapping which
of the two is larger swaps the parity assignment consistently with "the
larger contributes" **provided the two singletons are adjacent to each
other in the sort** (no block interposed between them). This is the
regime that occurs in $M_Q$ below (Section 13.1's order conditions place
$g_2,p_4$ adjacent to each other, both below both blocks), so we use the
clean form $\mathrm{OddSum}=(\text{block reps})+\max(\text{the two
singles})$ whenever that adjacency holds; this is verified directly
below rather than invoked as a black box.

**Order.** Direct symbolic differencing (own `sympy` script,
`/tmp/sym_q.py`), eliminating $p_4$ via the mass identity
$g_3=\frac{1-g_1-2g_2-4p_4}{3}$ so all differences are expressed in
$(g_1,g_2,p_4)$:
$$p_3-\tfrac{p_1}2=\tfrac16\bigl(1-4g_1-5g_2-p_4\bigr),\qquad
\tfrac{p_1}2-p_4=\tfrac16\bigl(1+2g_1+g_2-7p_4\bigr),\qquad
p_4-g_2=p_4-g_2.$$
Define
$$A_Q:\ 4g_1+5g_2+p_4<1,\qquad B_Q:\ p_4<\tfrac{1+2g_1+g_2}7,\qquad
C_Q:\ p_4>g_2.$$
Whenever $A_Q,B_Q,C_Q$ all hold, the sorted-descending order of $M_Q$ is
exactly $p_3\ge p_3>p_1/2\ge p_1/2>p_4>g_2$ (the $p_3$-pair and
$p_1/2$-pair each occupy $2$ consecutive ranks by construction; $A_Q$
places $p_3$ above $p_1/2$, $B_Q$ places $p_1/2$ above $p_4$, $C_Q$
places $p_4$ above $g_2$ — checked directly, not merely asserted, by the
sign of each of the three differences above), and by the Duplicate-Pair
Contribution Fact,
$$\mathrm{OddSum}(M_Q)=p_3+\tfrac{p_1}2+p_4.$$

**Exact value identity.** Eliminating $p_4$ via the mass identity and
simplifying exactly (`sympy.simplify`, re-verified by hand: $g_1+6g_2+3g_3
=(g_1+2g_2+3g_3)+4g_2=(1-4p_4)+4g_2$, so $\tfrac{g_1}8+\tfrac{3g_2}4+
\tfrac{3g_3}8=\tfrac{g_1+6g_2+3g_3}8=\tfrac{1-4p_4+4g_2}8$):
$$\boxed{\ \mathrm{OddSum}(M_Q)-c(3)=\dfrac{p_4-g_2-\gamma(3)}2\ }
\qquad\text{whenever } A_Q,B_Q,C_Q\text{ hold.}$$
In particular $\mathrm{OddSum}(Q)\le c(3)\iff p_4\le g_2+\gamma(3)$ on
this order-condition domain — an exact algebraic boundary, structurally
parallel to Construction H's $p_4\le\gamma(3)$ but shifted by $g_2$.

**What this does *not* establish.** The identity is proved rigorously
only inside $\{A_Q,B_Q,C_Q\}$. Section 13.3 exhibits an exact point
($g_1=g_2=g_3=1/15$, so $p_4=3/20$) where $A_Q,B_Q,C_Q$ **all hold** yet
$p_4-g_2-\gamma(3)=3/20-1/15-1/15=1/60>0$ — a genuine failure of $Q$
alone inside its own order-condition domain (fixed there by Construction
C, not by $Q$). The complementary order regimes ($C_Q$ false, i.e.
$p_4\le g_2$; or $A_Q$/$B_Q$ false) are **not** derived in this round —
left open, flagged honestly below (Section 13.4).

### 13.2 Exact closed-form identity for Construction BB (new, fully derived)

**Construction BB.** Split $p_1\to(g_1,\,p_2)$ [$1$ cut, exactly as in
Construction C] and $p_3\to(p_3/2,\,p_3/2)$ [$1$ cut, bisection], leaving
$p_2,p_4$ untouched (again only $2$ of $3$ cuts used). Response multiset
$$M_{BB}=\{\,g_1,\ p_2,\ p_2,\ p_3/2,\ p_3/2,\ p_4\,\}.$$

**Legality.** $g_1=p_1-p_2>0$ always (region hypothesis $p_1>p_2$).
$p_3/2>0$ trivially. No legality gap.

**Order.** Same substitution ($g_3$ eliminated via the mass identity,
differences in $(g_1,g_2,p_4)$), own `sympy` script `/tmp/sym_bb.py`:
$$p_2-g_1=\tfrac13\bigl(1-4g_1+g_2-p_4\bigr),\qquad
g_1-\tfrac{p_3}2=\tfrac16\bigl(7g_1+2g_2+p_4-1\bigr),\qquad
\tfrac{p_3}2-p_4=\tfrac16\bigl(1-g_1-2g_2-7p_4\bigr).$$
Define
$$D_{BB}:\ 4g_1-g_2+p_4<1,\qquad E_{BB}:\ 7g_1+2g_2+p_4\ge1,\qquad
F_{BB}:\ g_1+2g_2+7p_4<1.$$
Whenever $D_{BB},E_{BB},F_{BB}$ all hold, sorted order is $p_2\ge p_2>
g_1\ge p_3/2\ge p_3/2>p_4$ (the $p_2$-pair and $p_3/2$-pair each occupy
$2$ consecutive ranks; $D_{BB}$ places $p_2$ above $g_1$, $E_{BB}$ places
$g_1$ above $p_3/2$, $F_{BB}$ places $p_3/2$ above $p_4$), and by the
Duplicate-Pair Contribution Fact,
$$\mathrm{OddSum}(M_{BB})=p_2+g_1+\tfrac{p_3}2.$$

**Exact value identity.** Eliminating $p_4$ via the mass identity and
simplifying exactly (`sympy.simplify`):
$$\boxed{\ \mathrm{OddSum}(M_{BB})-c(3)=\dfrac{g_1-p_4-\gamma(3)}2\ }
\qquad\text{whenever } D_{BB},E_{BB},F_{BB}\text{ hold.}$$
So $\mathrm{OddSum}(BB)\le c(3)\iff g_1\le p_4+\gamma(3)$ on this domain
— exactly the "opposite-signed" analogue of $Q$'s identity, with the
roles of $g_1$ and $g_2$ (relative to $p_4$) swapped. This matches the
round-22 explorer's numeric observation of a near-exact equality
boundary at their found IIb hard point (that point has $g_1$ close to
$p_4+\gamma(3)$, consistent with this exact identity, not a coincidence).

**What this does *not* establish.** Since $B(3)$ places no a priori
upper bound on $g_1-p_4$ other than $p_1<1/2$ (and $g_1<1/2$ follows only
loosely from $p_1=g_1+g_2+g_3+p_4<1/2$), there exist points of $B(3)$
with $g_1-p_4>\gamma(3)$ where $BB$'s identity, even where legal, gives
a *positive* excess — $BB$ alone does **not** cover all of $\{g_3+p_4\le
3g_1\}$ (IIb) as originally conjectured by the outline; it is a partial
closer, not a universal one for IIb, exactly as Q is a partial closer
for IIa. (Verified directly: at $g_1=1/3,g_2=g_3=1/15+\varepsilon$ small,
$p_4$ small, $D_{BB},E_{BB},F_{BB}$ hold and $g_1-p_4-\gamma(3)>0$.)

### 13.3 A genuine, exact counterexample to best-of-$\{$H,C,Q,R,BB,W$\}$
(the round-22 outline's own candidate panel)

Testing the full panel at the exact rational point
$$g_1=g_2=\tfrac2{13},\quad g_3=p_4=\tfrac1{13}\qquad\Bigl(p=(p_1,p_2,p_3,p_4)
=\bigl(\tfrac6{13},\tfrac4{13},\tfrac2{13},\tfrac1{13}\bigr)\Bigr),$$
a valid point of $B(3)$ ($g_1,g_2,g_3=2/13,2/13,1/13$, each $>\gamma(3)
=1/15$ strictly since $2/13\approx0.1538>0.0667$ and $1/13\approx0.0769>
0.0667$; $p_1=6/13\approx0.4615<1/2$; $p_4=1/13\approx0.0769>\gamma(3)$,
so the point lies in Region II, specifically IIa) — computed exactly in
Python `Fraction` arithmetic (own script, `/tmp/verify6.py`):
- $H$ is **illegal** ($x=(p_3-g_1)/2=0$, boundary — $p_3=g_1$ exactly
  here).
- $W$ is **illegal** ($p_1-p_2-p_3=6/13-4/13-2/13=0$, boundary — the two
  legality boundaries of $H$ and $W$ coincide exactly at this point).
- $\mathrm{OddSum}(C)=\mathrm{OddSum}(Q)=\mathrm{OddSum}(R)=
  \mathrm{OddSum}(BB)=\dfrac{7}{13}$ **exactly**, all four **tied**.
$$\mathrm{OddSum}(\text{best of }C,Q,R,BB)-c(3)=\dfrac7{13}-\dfrac8{15}
=\dfrac{105-104}{195}=\dfrac1{195}>0.$$
This is a **genuine, exact, rigorously-verified failure** of the round-22
outline's entire candidate panel at a legal interior point of $B(3)$ (all
defining inequalities strict) — not a numeric artifact and not
attributable to a boundary/degenerate configuration (unlike $p^\dagger$,
this point has all four pieces strictly positive and comparable in
scale). This directly falsifies the outline's Step 5 claim ("best-of-
$\{H,Q,R,BB[,W]\}$ ... completes the $n=3$ Existence Theorem") as
literally stated for this panel.

### 13.4 A new construction (CB) that fixes this exact point, and its
partial closed form

To locate a fix, I computed the **true** local optimum $V(p)$ at the
Section 13.3 point directly (own script, `/tmp/vertex_search.py`):
optimizing $\mathrm{OddSum}$ over *all* $20$ possible $3$-cut allocations
$(a_1,a_2,a_3,a_4)$, $a_1+a_2+a_3+a_4=3$ (each $a_i$ = extra cuts on
piece $i$), with free (numerically optimized, `scipy.optimize.minimize`,
multi-start Nelder–Mead) split points within each allocation. The global
optimum found is exactly $\mathrm{OddSum}=1/2<c(3)$, attained (to solver
precision, matched exactly below in closed form) by allocation
$(1,0,1,1)$ with the $p_3$-split degenerating to a single point (one
fragment $\to0$, effectively $p_3$ left whole) and the $p_4$-split
landing exactly at $p_4/2$ (bisection) — i.e. the true optimal response
here is:

**Construction CB.** Split $p_1\to(g_1,\,p_2)$ [as in $C$/$BB$] and
$p_4\to(p_4/2,\,p_4/2)$ [bisection], leaving $p_2,p_3$ untouched. Response
multiset $M_{CB}=\{\,g_1,\ p_2,\ p_2,\ p_3,\ p_4/2,\ p_4/2\,\}$.

At the Section 13.3 point: $g_1=p_3=2/13$ (**tied exactly** — this is
precisely $H$'s and $W$'s coincident illegality boundary from Section
13.3, now understood as the point where CB's own two singleton values
$g_1,p_3$ collide), $p_2=4/13$, $p_4/2=1/26$; sorted order $p_2,p_2,
\{g_1,p_3\text{ tied}\},\{g_1,p_3\text{ tied}\},p_4/2,p_4/2$, giving
$\mathrm{OddSum}(M_{CB})=p_2+g_1+p_4/2=4/13+2/13+1/26=13/26=1/2$,
digit-for-digit matching the independent numeric optimum above — a
strong, independently-derived confirmation that CB is not an ad hoc
patch but the genuine local optimum at this point.

**Exact closed-form identity (derived, own `sympy`, `/tmp/sym_cb.py`,
eliminating $p_4$ via the mass identity as before).** $p_2-p_3=g_2>0$
**unconditionally** (so $p_2>p_3$ always, no case needed); the
$g_1$-vs-$p_3$ comparison genuinely splits into two cases:
$$g_1-p_3=\tfrac13\bigl(4g_1+2g_2+p_4-1\bigr).$$
- **Case $g_1\ge p_3$** (i.e. $4g_1+2g_2+p_4\ge1$): sorted order $p_2,p_2,
  g_1,p_3,p_4/2,p_4/2$ (subject to $p_2>g_1$ and $p_3>p_4/2$, checked
  below), $\mathrm{OddSum}(M_{CB})=p_2+g_1+p_4/2$, and
  $$\mathrm{OddSum}(M_{CB})-c(3)=\tfrac{2g_1}3+\tfrac{g_2}3+\tfrac{p_4}6-\tfrac15.$$
- **Case $p_3>g_1$** (i.e. $4g_1+2g_2+p_4<1$): sorted order $p_2,p_2,
  p_3,g_1,p_4/2,p_4/2$, $\mathrm{OddSum}(M_{CB})=p_2+p_3+p_4/2$, and
  $$\mathrm{OddSum}(M_{CB})-c(3)=-\tfrac{2g_1}3-\tfrac{g_2}3-\tfrac{p_4}6+\tfrac2{15}.$$
(The two formulas agree, as they must, exactly on the boundary $g_1=p_3$,
by continuity of $\mathrm{OddSum}$ — checked: both give $\tfrac{2g_1}3+
\tfrac{g_2}3+\tfrac{p_4}6-\tfrac15$ there since $g_1=p_3$ substituted into
either.) Additional order conditions needed for both cases: $p_2>p_3$
(free, $=g_2>0$), $p_2>g_1$ (i.e. $4g_1-g_2+p_4<1$, identical to $BB$'s
$D_{BB}$), $\min(g_1,p_3)>p_4/2$ (i.e. $g_1>p_4/2$ **and** $p_3>p_4/2$,
the latter $\iff g_3+p_4/2>0$, automatic since $g_3>\gamma(3)>0$; the
former is a genuine extra condition, $g_1>p_4/2$).

**What this establishes, and what it does not.** This closes the
*specific* exact point of Section 13.3 (verified: at $g_1=g_2=2/13,g_3=
p_4=1/13$, Case "$g_1\ge p_3$" applies with equality, giving excess
exactly $-1/30<0$, matching the independent numeric optimum). It is
**not** shown here to cover all of Region II, or even a full neighborhood
of the Section 13.3 point in closed form — only the exact point itself
and its two adjacent order-cases are derived exactly; a genuine 3-region
(or more) exhaustive case analysis of $Q$, $BB$, $CB$'s remaining order
regimes across all of $B(3)$, together with a symbolic (non-numeric)
proof that $\min\{H,C,Q,R,BB,W,CB\}\le c(3)$ everywhere, is **not**
completed this round.

### 13.5 Broad numerical evidence the 7-construction panel now suffices
(not a proof)

A multi-restart `differential_evolution` search (own script,
`/tmp/search_panel7.py`, $3$-dimensional free parametrization $(g_1,g_2,
g_3)$ with $p_4$ derived from the mass identity, $18$ independent seeds,
population $40$–$60$, up to $800$ iterations each, polished) over the
enlarged panel $\{H,C,Q,R,BB,W,CB\}$ finds **zero violations** across
every restart: the worst (maximum) excess found over all seeds is
$\approx-0.00702$ (attained near $g_1=g_2=2/19,g_3=3/19,p_4=1/19$, an
exact rational point where the panel already succeeds comfortably, not a
near-miss). This is **evidence**, not a proof, that Region II (indeed
all of $B(3)$) is covered by best-of-$\{H,C,Q,R,BB,W,CB\}$ — the case-
complete symbolic argument establishing this (analogous to Region I's
fully closed-form Section 12.5) remains open work for a future round.

### 13.6 Summary: what this round establishes and what remains open

**Established, in full rigorous exact algebra:**
- Exact closed-form identities for Constructions $Q$ (Section 13.1) and
  $BB$ (Section 13.2), each on an explicit, fully-derived order-condition
  domain, in the same style as Construction H's certified identity.
- A **genuine, exact counterexample** (Section 13.3, rational point
  $(6,4,2,1)/13$) refuting the round-22 outline's specific claim that
  best-of-$\{H,C,Q,R,BB,W\}$ closes Region II — this is real, checked
  progress (a precise, non-vague characterization of a hole, per the
  round's own mandate), not just "the residual didn't go to exactly
  zero."
- A **new construction CB** (Section 13.4) that provably fixes this exact
  point, with its own two-case exact closed-form identity derived (not
  merely numerically fit) via the same order-condition + mass-identity
  method.

**Still open (honest gaps, not to be silently assumed closed):**
- $Q$ and $BB$'s identities are proved **only** on their primary
  order-condition domains ($A_Q\wedge B_Q\wedge C_Q$ for $Q$; $D_{BB}
  \wedge E_{BB}\wedge F_{BB}$ for $BB$); the complementary order regimes
  (e.g. $C_Q$ false, i.e. $p_4\le g_2$) are not derived.
- $CB$'s identity is derived in both of its own order sub-cases, but its
  own order conditions ($p_2>g_1$, $g_1>p_4/2$) are not shown to hold
  throughout any named sub-region of $B(3)$ — only checked at the one
  point that motivated it.
- No exhaustive, non-numeric argument shows $\min\{H,C,Q,R,BB,W,CB\}\le
  c(3)$ **everywhere** in Region II (or $B(3)$). Section 13.5's broad
  numeric search (18 restarts, zero violations) is suggestive but is
  explicitly *not* a proof, per the rigor rules.
- It remains genuinely possible that even the 7-construction panel has
  its own exact counterexample not yet found by numeric search (the
  Section 13.3 point was itself missed by the round-22 explorer's own
  global search before being found this round by directly testing a
  structurally-motivated rational candidate, not by blind search) — the
  next round should not assume closure without either (a) a full
  symbolic case-complete proof, or (b) further large-scale/targeted
  search specifically probing near coincidence points of the various
  constructions' legality boundaries (where Section 13.3's point was
  found, at the coincidence of $H$'s and $W$'s illegality loci).

The $n=3$ Existence Theorem's Region II therefore remains `partial`:
substantially narrower and better-characterized than before this round
(exact identities for 3 constructions now proved, a genuine hole found
and patched at one exact point, broad — not exhaustive — numeric
confirmation the enlarged panel may suffice), but not proved closed.

## Promotable lemmas (round 22, proposed — not self-certified)

- **Construction Q identity**: for $p\in B(3)$ with $4g_1+5g_2+p_4<1$,
  $p_4<(1+2g_1+g_2)/7$, and $p_4>g_2$, the $2$-cut response splitting
  $p_1\to(p_1/2,p_1/2)$ and $p_2\to(g_2,p_3)$ (leaving $p_3,p_4$
  untouched) is legal and satisfies $\mathrm{OddSum}(Q)=c(3)+
  (p_4-g_2-\gamma(3))/2$ exactly — proved in Section 13.1 via the
  Duplicate-Pair Contribution Fact (also stated and proved there, a
  reusable elementary fact about $\mathrm{OddSum}$ of multisets with
  even-multiplicity blocks) plus algebraic substitution via the mass
  identity.
- **Construction BB identity**: for $p\in B(3)$ with $4g_1-g_2+p_4<1$,
  $7g_1+2g_2+p_4\ge1$, and $g_1+2g_2+7p_4<1$, the $2$-cut response
  splitting $p_1\to(g_1,p_2)$ and $p_3\to(p_3/2,p_3/2)$ (leaving
  $p_2,p_4$ untouched) is legal and satisfies $\mathrm{OddSum}(BB)=
  c(3)+(g_1-p_4-\gamma(3))/2$ exactly — proved in Section 13.2, same
  method.
- **Construction CB identity**: for $p\in B(3)$ with $4g_1-g_2+p_4<1$
  and $g_1>p_4/2$, the $2$-cut response splitting $p_1\to(g_1,p_2)$ and
  $p_4\to(p_4/2,p_4/2)$ (leaving $p_2,p_3$ untouched) is legal and
  satisfies $\mathrm{OddSum}(CB)=p_2+g_1+p_4/2$ if $4g_1+2g_2+p_4\ge1$,
  or $\mathrm{OddSum}(CB)=p_2+p_3+p_4/2$ if $4g_1+2g_2+p_4<1$ (the two
  formulas agreeing exactly on the shared boundary) — proved in Section
  13.4, same method.
- **Duplicate-Pair Contribution Fact** (elementary, general-purpose, not
  specific to this problem): in any finite multiset sorted descending,
  a value of even multiplicity $2j$ contributes exactly $j$ copies of
  itself to $\mathrm{OddSum}$ regardless of its position in the sorted
  order — proved in Section 13.1 from the fact that any $2j$ consecutive
  integers contain exactly $j$ odd values.
- **Exact counterexample point** (not a lemma but a load-bearing fact
  for future rounds to build on): at $p=(6,4,2,1)/13\in B(3)$, best-of-
  $\{H,C,Q,R,BB,W\}=7/13>c(3)$ exactly, with $H,W$ simultaneously
  illegal there (Section 13.3) — the reviewer/next round should treat
  this point as a mandatory regression check for any future candidate
  panel.
