## imo-2026-03 (lens: new mechanism for Case (b) "v>=a", sub-case "T' cuts p4")

### Context recap (verified against the files, not just trusted)
Case (b)'s residual target: for $R'=\{a,b\}\cup T'$ ($a\ge b>0$, $a+b=p_3$, so
$a\ge p_4\ge b$), need $A(B)\ge f(n)$ for $B=\{b\}\cup T'$, $T'$ a legal
refinement of $\{p_4,\dots,p_{n+1}\}$ using $\le n-4$ cuts, jointly over all
$(b,T')$. Theorem 37 (round 23, `greedy-halving-adversary.md` lines
4936-4987) closes exactly the vertex $a=b=p_4$, $T'=\{p_4\}\cup T''$ ($T'$
leaves $p_4$ itself untouched) — via odd-run cancellation
$A(B)=A(T'')$ then the certified Cross-Level Rescaling Lemma, conditional on
$(\star_{n-4})$ (unconditional $n\le6$). The round-23 diagnostic (lines
4988-5047) found that when $T'$ *does* cut $p_4$, the natural next vertex
candidate ($b$ tied to $T'$'s own top fragment $=\max(T')$) reduces via the
same odd-run cancellation to $A(\{c_2\}\cup(\text{rest of }T'))$ where $c_2$
is an *arbitrary* residual fragment of $p_4$ (not a ladder value) — and this
residual object is **not** a rescaled ladder (Cross-Level Rescaling Lemma's
hypothesis fails), so the mechanism does not terminate in one step. I
independently re-derived this diagnosis by hand from the Insert-Element
Identity's slope argument (§ "Diagnostic finding") and confirm it is
correct: the failure is genuinely about the *shape* of the residual
($\{$arbitrary point$\}\cup\{$smaller legal ladder response$\}$), not an
artifact of any specific algebraic route.

### Numeric exploration (this round, exact `Fraction`, scripts below)

**Experiment 1** (`/tmp/explore_tcuts4.py`): grid search over $b\in(0,p_4]$
and $T'$ (all legal cut placements up to budget) at $n=5,6$. Found the
global minimum found equals $f(n)$ exactly both times (as expected). At
$n=6$ the argmin found by the grid included a **"T' cuts $p_4$" vertex** —
$p_4$ bisected exactly into two copies of $p_5$ (using the ladder identity
$p_4=2p_5$), with $b$ also tied to $p_5$: four total copies of $p_5$ (even
multiplicity) cancel to $0$ under odd-run reduction, leaving the residual
$\{p_6,p_7\}$ untouched. **I checked this by hand and confirmed it is
isomorphic to Theorem 37's own mechanism, not a new route**: at $n=6$ the
residual $\{p_6,p_7\}$ happens to be the trivial "last two elements" case
($p_n-p_{n+1}=p_{n+1}=a_n$, an elementary identity, always true, no
induction needed) — but for $n=7$ the same construction's residual
$\{p_6,p_7,p_8\}$ has $A=3/255\ne f(7)=1/255$, i.e. this exact vertex is
**not** tight at $n=7$; it needs the same $(\star_{n-4})$-conditional
Cross-Level Rescaling step Theorem 37 already uses. **Conclusion: the
bisect-$p_4$-into-two-copies-of-$p_5$ vertex is not a new unconditional
result — it collapses to a residual that is again a genuine sub-ladder, so
it is really the *same* Theorem 37 vertex reached by a different route, not
progress on the open "$T'$ cuts $p_4$ into a non-ladder-native fragment"
branch.**

**Experiment 2** (`/tmp/explore_n7.py`): randomized exact-`Fraction` search
(tens of thousands of trials per $n$, forcing at least one cut specifically
on $p_4$, i.e. deliberately restricted to the *open* branch) for
$n=6,7,8$. In every case the minimum found stays $\ge f(n)$ with the gap
shrinking toward $0$ as the search refines (consistent with $f(n)$ being
the true infimum, never crossed) — **no counterexample found in the open
branch** at $n=6,7,8$. This is corroborating numeric evidence only (a random
search over a high-dimensional simplex is not exhaustive and cannot
substitute for a vertex enumeration), but it is a genuine, independently
run stress test of exactly the branch that's open, and it found nothing
that contradicts the standing conjecture.

### Distinct openings (new mechanisms to try, not yet attempted on file)

1. **Reframe the residual shape as its own standalone lemma, induct
   directly on IT instead of trying to force it through Cross-Level
   Rescaling.** Define $h(m):=\inf\{A(\{c\}\cup S)\}$ over all $c\in(0,q_1]$
   ($q_1$ the top value of an $m$-length ratio-2 tail $q$) and all legal
   refinements $S$ of $q$ using $\le m-1$ cuts, where **crucially $c$ is
   totally unconstrained relative to $q$'s own values** (this is exactly
   the shape both Theorem 37's diagnostic and this round's Experiment 1
   independently landed on). This is a *new* target, structurally identical
   to Case (b)'s "$v\ge a$" branch one level down but stated abstractly and
   divorced from the specific $p_3/p_4$ labels — try strong induction on
   $m$ directly using the certified `vertex-minimum-theorem` +
   `odd-run-reduction-lemma` machinery (the same tools Theorem 37 already
   uses), rather than trying to route through the ladder-specific
   rescaling lemma that provably doesn't apply here. This turns "does not
   reduce to a smaller self-similar instance" from a dead end into "reduces
   to a smaller instance of a *genuinely new* self-referential family" —
   which is exactly the kind of induction target this problem has
   repeatedly needed (cf. the certified `case-i-closure-theorem`'s own
   exchange-smoothing-vertex-maximization, which succeeded on a
   structurally similar "arbitrary point + fixed reference set" problem in
   Claim (A)).
2. **Exploit that the open sub-case has TWO free continuum parameters
   coupled by one budget** ($c_2\in(0,p_4/2]$ and $T'''$'s own legal
   refinement of $\{p_5,\dots\}$ with $\le n-5$ cuts) — apply the
   Vertex-Minimum Theorem to *this whole two-parameter object jointly*
   (as Theorem 37's authors did for $(b,T')$), rather than fixing $c_2$
   first. This is a direct continuation of the round-23 mechanism, one
   level further in, not a new tool — but it's the most mechanical next
   step and hasn't been executed yet (round 23 only diagnosed the
   obstruction, did not attempt the joint vertex analysis on the new
   two-parameter object).
3. **Try to prove the WEAKER but sufficient bound directly**: since (per
   round 22's negative finding) any bound built from a one-sided *lower*
   bound on $A(T')$-type quantities is structurally insufficient, and this
   sub-case is exactly where that finding bites hardest, look for a genuine
   *upper* bound on $A(T'')$ or the smaller-instance analogue instead (dual
   direction) — i.e. bound $A(\{c_2\}\cup T''')$ from *above* by something
   independent of $c_2$'s precise value using Fact 2 (`A <= Total`, already
   certified, general) plus the certified `exchange-smoothing-vertex-
   maximization` (which the project has already proved handles exactly this
   "maximize over an arbitrary free coordinate plus a fixed reference set"
   shape in Claim (A)'s Case I). This reuses machinery already proved
   sufficient for a structurally analogous problem (Case I) rather than
   inventing new tools.

### Cheap-kill candidates
- None found. Every "obvious" collapse (bisect $p_4$ exactly, tie $b$ to
  $\max(T')$) checked out numerically consistent with the standing
  conjecture (no violation), so there is no quick refutation available —
  the branch appears genuinely hard, not a bug or oversight.

### Knowledge-base entries to use
- `exchange-smoothing-vertex-maximization` (already certified,
  `lemmas/case-i-closure-theorem.md`'s engine) — most promising reusable
  tool for opening (3) above; it was built for exactly "maximize an
  alternating-sum-type functional over an arbitrary free coordinate merged
  with a fixed reference multiset," the same shape as $\{c_2\}\cup T'''$.
- `vertex-minimum-theorem`, `odd-run-reduction-lemma` — already the engine
  for Theorem 37; needed again for opening (1)/(2).
- `half-bound-lemma` ($A\ge0$) and Fact 2 ($A\le\mathrm{Total}$, proved
  inline in `rank-pigeonhole-budget.md` §5.2) — cheap general bounds that
  closed several branches of Case I and may again bound the residual
  without needing its exact value.
- General Cross-Level Rescaling Lemma (certified, round 22) — confirmed
  again this round (Experiment 1) to be the *wrong* tool for the open
  branch (its hypothesis genuinely fails on a non-ladder-native residual);
  do not re-attempt forcing it here.

### Analogous past problems (cruxes)
Searched `crux_moves_documentation.md`'s subtopics (`games-and-strategy`,
`extremal-principle`, `induction-and-construction`,
`size-bounding-and-descent`) and grepped `technique`/`how_used` for
superincreasing/geometric/alternating-sum/peel/vertex/exchange/dyadic
keywords (441 combinatorics entries in those four subtopics). Found:
- `aimo-0146` (`extremal-principle`/`induction-and-construction`) — "Maximize
  a fixed weighted sum of a sorted nonnegative integer sequence under a sum
  constraint by exchange-smoothing weight toward the higher-coefficient
  positions," and "delete a globally minimum-degree vertex... universal
  vertex" reductions — this is the crux already cited (round 8) as the
  inspiration for `exchange-smoothing-vertex-maximization`; already
  absorbed into the project's own machinery, no new content to extract.
- `aimo-0117` — dyadic/geometric-sequence defer-commitment strategy —
  **already confirmed a dead end for this project** (per `run_state.md`'s
  round-4/5 finding: no multi-round structure for it to exploit); do not
  reconsider.
- `aimo-0019` — "Bound a family of dyadic-length pieces of pairwise distinct
  sizes by twice the largest, via the geometric sum of distinct negative
  powers of two" — same flavor as the already-certified `ratio-2-spacing-
  lemma`/Spacing Corollary; no new content beyond what's already certified.
- No genuinely new analogous crux found for the specific "arbitrary foreign
  point merged with a smaller self-similar family, prove an alternating-sum
  floor" shape — this appears to be a problem-specific structure without a
  close corpus match; say so honestly rather than force a weak analogy.

### Prior progress
Theorem 37 (conditional on $(\star_{n-4})$, unconditional $n\le6$) closes
exactly the symmetric-split/$p_4$-untouched vertex. The "$T'$ cuts $p_4$"
sub-case (this round's assigned target) has **zero closed content** as of
round 23 — only the diagnostic finding that the natural next vertex
candidate does not terminate in one step.

### Dead ends (do not retry)
- Cross-Level Rescaling Lemma applied directly to the "$T'$ cuts $p_4$"
  residual $\{c_2\}\cup(\text{rest})$ — confirmed again this round (not
  just round 23) that its hypothesis (whole tail = rescaled ladder) fails
  when $c_2$ is an arbitrary fragment, including via the "exact bisection"
  special case I explored (Experiment 1), which merely reproduces Theorem
  37's own conditional closure via a longer path, not new unconditional
  ground.
- `aimo-0117`-style defer-commitment (already recorded dead, round 4/5).

### Small-case / intuition notes (conjectural, from numerics only)
- At $n=6,7,8$, forced-cut-on-$p_4$ random search (tens of thousands of
  trials, exact `Fraction`) never found $A(B)<f(n)$; margins shrink toward
  $0$ as search resolution increases, consistent with $f(n)$ remaining the
  true infimum even in the open branch, and with the *same* extremal shape
  (near-total cancellation via even multiplicities, leaving a genuine
  residual sub-ladder or single small leftover) recurring at every level —
  i.e. the true minimizer in the "$T'$ cuts $p_4$" branch is conjectured
  (not proved) to *still* be achieved at a configuration that, after
  cancellation, reduces to a smaller legal ladder instance — just not via
  the single-step Cross-Level Rescaling Lemma; it looks like it needs one
  more layer of the same vertex-cancellation argument applied recursively
  (opening 1/2 above), which is exactly the induction the file has not yet
  set up.
