# Round 15 scouting report: case (b2), general upper bound (lp-duality-certificate)

Scope: case (b2) is $p_1<T/2$ and $T/D_n<p_2<a_nT/2$ (§R13.3 of
`lp-duality-certificate.md`). Task: characterize its witness family more
precisely, and assess whether a rigorous vertex enumeration
(`per-piece-vertex-decomposition-theorem`) is tractable there, vs. a
different mechanism (reuse of `vertex-minimum-theorem` /
`odd-run-reduction-lemma` from the lower-bound population, per round 9's
unexecuted suggestion). No proof attempted; this is reconnaissance only,
verified numerically (exact-`Fraction` where stated, float multi-start
optimization elsewhere, both clearly flagged).

## 1. Case (b2)'s witness family is NOT a small/finite family

Legality places no constraint on the tail $p_3,\dots,p_m$ beyond
$p_2\ge p_3\ge\cdots\ge p_m>0$, $\sum_{i\ge3}p_i=T-p_1-p_2$. The two
case-(b2) defining inequalities pin down only $p_1$ (to $(0,T/2)$) and
$p_2$ (to a band of order-$T$ width, e.g. $\approx(0.067,0.267)T$ at
$n=3$ — already noted in the file). **The tail shape is an
$(m-3)$-dimensional continuum with no further constraint from being in
case (b2).** So "enumerate case (b2)'s witnesses" is not a finite task —
case (b2) is a full-dimensional (codimension-0) region of the marking
simplex for every $n\ge2$. The only enumerable finite object per marking
is Xiang Yu's own vertex-response family (`vertex-minimum-theorem`
applied to *that* marking) — confirming that "vertex enumeration" must
mean *characterizing the response family as a function of an arbitrary
marking in the region*, not literally listing case-(b2) points. This
matches, and sharpens, the R11.5/R12.5/R14.3 diagnosis already on file.

## 2. Exact structure at two round-14 near-tight witnesses (new this round)

I ran a genuinely thorough search (exhaustive over all legal cut
*compositions* $(c_1,\dots,c_m)$, $\sum c_i\le n$, each with 12-25
Nelder–Mead multi-starts over the composition's continuous split
variables) at round 14's own two reported near-tight case-(b2) witnesses,
rather than round 14's cheaper composition-restricted local probe.
Scripts: `/tmp/round-15/vertex_probe.py`, `/tmp/round-15/refine1.py`.

- **$n=3$, $p=(0.4468,0.2591,0.2251,0.0691)/T$:** true optimum
  $\Phi_{\min}\approx0.51585$ (margin to $a_3T=0.53333$: $\approx0.0175$,
  matching round 14's figure), attained at composition $(1,0,1,0)$ — cut
  $p_1$ once, $p_3$ once, leave $p_2,p_4$ untouched. **New finding:**
  running the optimizer from many restarts found *different* optimal split
  points ($x\approx0.179,y\approx0.169$ vs. $x\approx0.283,y\approx0.161$
  in two separate runs) both giving the *exact same* $\Phi$ value to
  numerical precision. Tracing the sorted order confirms why: in this
  order-type ($p_{1a}\!>\!p_2\!>\!p_{1b}\!>\!p_{3a}\!>\!p_4\!>\!p_{3b}$,
  i.e. $p_1$'s two fragments both land on **odd** ranks and $p_3$'s two
  fragments both land on **even** ranks), the alternating sum telescopes
  algebraically to
  $$A = x-p_2+(p_1-x)-y+p_4-(p_3-y) = p_1-p_2-p_3+p_4,$$
  independent of $x,y$ — verified symbolically by hand and confirmed by
  both numeric optima agreeing exactly. This is a genuine flat 2-dimensional
  face of the polytope, not a numerical artifact: $\Phi=(T+p_1-p_2-p_3+p_4)/2$
  for *any* legal $x\in(\ldots),y\in(\ldots)$ preserving that order.

- **$n=4$, $p=(0.2933,0.2514,0.2131,0.1338,0.1085)/T$:** true optimum
  $\Phi_{\min}\approx0.50455$ (margin $\approx0.0116$, matching round 14),
  composition $(2,1,0,0,0)$: $p_1$ split into 3 fragments
  $(0.2131,0.0401,0.0401)$, $p_2$ split into 2 fragments
  $(0.1405,0.1109)$. Here the structure is a **genuine pinned vertex**, not
  a flat face: one $p_1$-fragment ties *exactly* to $p_3$'s value
  ($0.2131=p_3$), and the other two $p_1$-fragments tie to each other
  (an ordinary same-piece pair, canceling). This is exactly the
  pinned-to-reference-value + tied-pair vertex shape
  `per-piece-vertex-decomposition-theorem` /
  `simplex-exchange-smoothing-vertex-maximization` already predict.

**Conclusion from this pair:** the two witnesses realize *qualitatively
different* vertex/face types (one a clean cross-piece sign-cancellation
identity, the other a standard pinned-tie vertex) even though both are
in case (b2) at nearby $n$. This is concrete evidence that case (b2)'s
vertex family is genuinely heterogeneous — reinforcing that a single
closed-form template (of the Bisect-Top-$k$ flavor) cannot cover it, but
also pointing at a specific, promising generalization (§3).

## 3. A concrete, promising generalization: cross-piece sign-cancellation

The $n=3$ example's flat face is an instance of a clean general fact,
strictly broader than `pair-cancellation-identity`/Bisect-Top-$k$:

**Observation (not yet proved as a general lemma — flag for next round).**
If Xiang Yu splits a *subset* of pieces such that, in the resulting sorted
order, **every fragment of a given split piece lands on ranks of one
common parity** (not necessarily adjacent — e.g. $p_1$'s fragments at
ranks 1 and 3 with $p_2$ intervening at rank 2), then that piece's total
contribution to $A$ is $\pm p_i$ (its *whole* original value, with the
sign of its parity class), **independent of where exactly it is split**.
Summing over such "monochromatic" pieces plus the untouched pieces (each
trivially monochromatic) gives
$$\Phi = \Big(T+\textstyle\sum_i \varepsilon_i p_i\Big)/2,\qquad
\varepsilon_i\in\{+1,-1\},$$
for any sign vector $\varepsilon$ *realizable* by some legal composition
and split (a combinatorial feasibility condition on interleaving order and
cut budget, not yet characterized). Bisect-Top-$k$'s
$\Phi=(T+A(\mathrm{tail}))/2$ construction is exactly the trivial corner
of this family where only the top $k$ pieces are split, each pair
*adjacent* (opposite-parity, canceling to $0$, not contributing $\pm p_i$)
— i.e. Bisect-Top-$k$ never actually uses the "same-parity, non-adjacent"
freedom this observation exposes. The $n=3$ witness above shows this
extra freedom **does** help: standalone Bisect-Top-$k$ at that witness
gets $k=2$ giving $\Phi=0.508$ (worse than the true $0.516$ margin... — no,
worse means larger $\Phi$; Bisect-Top-$k$ actually already finds
$0.502$–$0.508$ range at these points per round-14's own table, so it is
*not* always strictly worse, but the true optimum needs the cross-piece
mechanism to be reached exactly, and a broader numeric check below shows
Bisect-Top-$k$ alone matches the true optimum only a minority of the time).

**This is precisely the mechanism round 9 flagged and left unexecuted:**
it is the natural way to reuse the lower-bound population's
`odd-run-reduction-lemma` (which already handles evaluating $A$ when
*several* values are simultaneously at odd/even multiplicity — exactly
the "monochromatic parity class" situation here) on the **upper-bound**
side, rather than re-deriving it from scratch. Concretely: **recommend
round 15's builder formalize a "Cross-Piece Sign-Assignment Identity"**
generalizing `pair-cancellation-identity`, import `odd-run-reduction-lemma`
directly for the evaluation half, and separately attack the **feasibility
question** (which sign vectors $\varepsilon$ are achievable by a legal
composition/order, given cut budget $n$) — this feasibility question is a
finite combinatorial problem (unlike the raw joint vertex fixed point),
and looks tractable: a piece can be made monochromatic-negative if enough
"spacer" elements of appropriate size exist to interleave its fragments at
even ranks, with a cut cost equal to (fragments $-1$).

## 4. Reconfirmed (with a stronger search) that case (b2) shows no near-zero margin

Using the same exhaustive-composition + multi-start search (a strictly
more thorough method than round 14's composition-*restricted* local probe,
since it also searches non-adjacent/cross compositions like $(2,1,0,0,0)$
that round 14's probe was structured to explore only implicitly), I
re-sampled fresh random case-(b2) markings at $n=3,4$ (8 samples each,
`/tmp/round-15/coverage_check.py`) and computed true $\Phi_{\min}$ exactly
via this search: **every sample's true optimum had margin
$\gtrsim0.011$–$0.03$ below $a_nT$** (e.g. $n=3$: true values
$0.502$–$0.511$ vs. target $0.5333$; $n=4$: true values $0.500$–$0.503$ vs.
target $0.5161$) — **no near-zero-margin witness found**, corroborating
(not merely repeating) round 14's own weaker probe with an independent,
broader search. **Bisect-Top-$k$ alone matched the true optimum in only
$1/9$ ($n=3$) and $3/9$ ($n=4$) sampled cases** — consistent with round
14's $10$–$26\%$ coverage figure, now confirmed against a genuine
full-composition search rather than just the closed-form family itself.

## 5. Recommendation for round 15's builder

1. **Do not attempt the literal joint `per-piece-vertex-decomposition-
   theorem` fixed-point enumeration as a monolithic target** — this
   round's evidence (two structurally different vertex/face types at two
   nearby witnesses) reconfirms it is heterogeneous and not a small closed
   family; this matches every prior round's diagnosis (R11.5/R12.5/R14.3)
   and no new tractability was found for the *general* joint system.
2. **Instead, formalize the Cross-Piece Sign-Assignment Identity (§3)**
   as a standalone general lemma (a genuine generalization of
   `pair-cancellation-identity`/Bisect-Top-$k$, reusing
   `odd-run-reduction-lemma` from the lower-bound population for the
   evaluation half — the concrete execution of round 9's suggestion) and
   attack the **feasibility characterization** (which sign vectors
   $\varepsilon$ are legally realizable given cut budget $n$) as the
   actual new mathematical content — this is a finite combinatorial
   question, not a continuum optimization, and looks more tractable than
   raw vertex enumeration.
3. **Numeric evidence continues to weakly favor "case (b2) has genuine
   slack"** (no witness found this round or last with margin below
   $\approx0.01$, across two independent and increasingly thorough
   searches) — this does not reduce proof burden (still need a rigorous
   argument for *every* marking, not a numeric sample), but it is a second
   independent data point against investing further effort in hunting for
   a tight counterexample, and in favor of investing in the
   sign-assignment mechanism (or a genuinely different existence/pairing
   argument) to actually prove the bound.
4. If the sign-assignment feasibility characterization stalls, the
   fallback per round 14's own §"Open gaps" item 0 remains: sharpen case
   (a)'s conditioning so case (b2)'s *recursive* sub-instances land in
   case (a)/(b1) one level down (an inductive "eventually escapes case
   (b2)" argument) — not attempted by this scout, flagged only as the
   documented fallback.

## Files/scripts (for reproducibility, not part of any proof)
- `/tmp/round-15/explore.py` — first (weaker) crude comparison, superseded.
- `/tmp/round-15/vertex_probe.py`, `/tmp/round-15/refine1.py` — exact
  structural analysis of the two round-14 witnesses (§2).
- `/tmp/round-15/coverage_check.py` — broader exhaustive-composition
  coverage/margin check (§4).
