## imo-2026-03 (lens: greedy-halving-adversary Vertex 5 / h(m) q1-cut obstruction)

### Setup recap (verified against the approach file, round 29 section)
Vertex 5 (the honest residual) asks: for $S=\{x,q_1-x\}\cup\mathrm{tail}$
($\mathrm{tail}=\{q_2,\dots,q_{m+1}\}$ fully untouched, $x\in(0,q_1/2)$),
and $c=t$ a *genuine* tail element ($t\ne q_1-x$), prove
$$A(\{c\}\cup S)=A(\{x,q_1-x\}\cup(\mathrm{tail}\setminus\{t\}))\ \ge\ f(m),\qquad m\ge3.$$
The file's own attempted route (peel the dominant fragment $q_1-x$ exactly,
then bound the remainder $A(\{x\}\cup(\mathrm{tail}\setminus\{t\}))$ via the
generic `Insert-Bound Corollary` $A(T)-x\le A(\{x\}\cup T)\le A(T)+x$) is
confirmed dead as diagnosed: the corollary is a *slack* bound (loses up to
$2x$ of margin against a gain of only $t$), and I reproduced the exact
numeric failure of that particular bound (e.g. $m=5$, $t=1$, $x\to q_1/2$:
insert-bound requires $A(\mathrm{rest})\le \mathrm{Total}(\mathrm{rest})-t-2x$,
which is false there, even though the true value is comfortably positive).
**This is a genuinely lossy step, not a tight obstruction** — the true
quantity is much larger than the bound suggests, so the fix is to stop
bounding and start computing exactly.

### Distinct openings

**Opening 1 (recommended primary route) — Exact Piecewise-Affine
Monotonicity, NOT peeling.** Fix $t$ (hence fix the explicit multiset
$T:=\mathrm{tail}\setminus\{t\}$, zero free parameters). Peel the dominant
fragment $q_1-x$ exactly via `sharp-dominant-removal-identity` (valid for
$x\in(0,q_1/2)$ since $q_1-x>q_2\ge\max(T)$ and $q_1-x>x$):
$$A(\{x,q_1-x\}\cup T)=(q_1-x)-A(\{x\}\cup T)=:F(x).$$
Now invoke the certified `single-insert-point-vertex-lemma` **for its slope
fact, not its vertex-enumeration fact**: $g(x):=A(\{x\}\cup T)$ is
piecewise affine of slope *exactly* $\pm1$ a.e. on $(0,q_1/2)$ (since $T$
is fixed). Hence $F'(x)=-1-g'(x)\in\{-2,0\}$ **always** — $F$ is
*monotonically non-increasing* on the whole interval, for *every* choice
of $t$. This collapses the continuum-in-$x$ universal quantifier to a
single boundary check at $x\to q_1/2^-$ — **exactly**, not approximately,
and I verified this monotonicity numerically (exact `Fraction`, not
float) for every $t\in\mathrm{tail}$ at $m=5,6$: zero non-monotone steps
in 60-80 point grids per $(m,t)$ pair (script below). At the boundary
$x=q_1/2=q_2$, $\{x,q_1-x\}=\{q_2,q_2\}$, so the full multiset becomes
$\{q_2,q_2,q_2\}\cup T$ (three copies of $q_2$, since $T$ still contains
$q_2$ unless $t=q_2$). Pair-cancel two copies of $q_2$ (elementary,
already used in Vertices 3/4): if $t=q_2$, this reduces to exactly the
untouched-tail value $A(\mathrm{tail})=f(m)$ (equality, matching the file's
own observed tightness at $t=q_2,x\to q_1/2$); if $t\ne q_2$, it reduces
to $\{q_2\}\cup T$ which still has $q_2$ appearing twice (once as the
surviving copy, once already in $T$) — pair-cancel again to get the
*explicit* tail with **both** $q_2$ and $t$ removed, a finite closed-form
alternating sum with two "gaps," directly computable by the same
telescoping/geometric-series technique already used for Vertex 4's
$A(\mathrm{tail})$ evaluation (just with one extra removed rank). Numerics
(below) show this two-gap value is comfortably $\ge f(m)$ with wide margin
for every $t\ne q_2$, consistent with $t=q_2$ being the unique tight case —
so this route reduces Vertex 5 to (a) the already-rigorous monotonicity
argument (real proof, not numeric) plus (b) one finite family of exact
double-removal alternating-sum computations (an induction/telescoping
exercise in the same style as Vertex 4, not a new proof technique).
**This is a genuinely different mechanism from peeling-then-bounding**: it
uses the *exact* slope characterization of an already-certified lemma to
prove a global monotonicity fact, not a local per-cut bound, so it does
not inherit the "$2x$-vs-$t$" lossiness at all.

**Opening 2 — reduce "worst $t$" via a second monotonicity-in-$t$
argument.** Numerics strongly and uniformly suggest $t=q_2$ (the tail's
own largest element) is the unique worst choice of $t$ across every $m$
tested (3–7): the boundary value at $t=q_2$ is always exactly $f(m)$ while
every other $t$ gives a strictly larger value, with growing margin as $m$
grows. A clean way to prove this without hand-checking $m-1$ separate
$t$'s: express the two-gap alternating sum as a function of *which rank*
$t$ occupies in the tail and show it is monotonic in that rank (removing a
*smaller*-valued/ deeper element costs less than removing $q_2$ itself) —
likely another slope/perturbation argument analogous to Opening 1, applied
to a discrete "swap which rank is removed" argument, or directly via the
Insert-Bound Corollary applied the OTHER way (bounding the *effect of
removing* $t$ rather than the effect of inserting $x$).

**Opening 3 — LP/vertex-domination read of the whole Vertex-5 sub-problem
at once.** Since $x$ ranges over a box and $t$ ranges over a finite set,
the entire Vertex-5 claim is literally "min over a finite union of
line-segments (one per $t$) of a piecewise-affine function $\ge f(m)$" —
exactly the shape the project's `vertex-minimum-theorem` /
`single-insert-point-vertex-lemma` machinery was built for. Opening 1 is
already this LP/vertex argument specialized to one coordinate; a fully
general treatment (skip fixing $t$ first, treat $(x,t)$ jointly as a
2-dimensional — one continuous, one discrete — optimization) would give
the same conclusion with less bookkeeping, but Opening 1 as scoped above
is already concrete and buildable, so I do not see this as a materially
different mechanism, just a reframing of Opening 1 at a higher level of
generality — flag it as available but redundant with Opening 1.

**Opening 4 (exchange argument) — swap $x$ against a tail element
directly.** An alternative to peeling $q_1-x$ first: apply a direct
"exchange smoothing" (as used by `exchange-smoothing-vertex-maximization`)
treating $x$ as one coordinate of a larger vertex-maximization problem
over the *whole* multiset (not decomposed via peeling at all). This is
mechanically close to Opening 1/3 in spirit (same underlying LP-vertex
toolkit) but attacks the joint $(x,t)$-domain without first isolating
$q_1-x$ — worth trying only if Opening 1's two-gap sum proves
unexpectedly hard to close in closed form; not otherwise a distinct
mechanism.

### Cheap-kill candidates
- The monotonicity fact in Opening 1 ($F'\in\{-2,0\}$, hence non-increasing)
  is itself a cheap structural kill of the "need to check all $x$" part of
  the problem — reduces a continuum to one boundary point, essentially for
  free once you cite the slope fact of the already-certified
  `single-insert-point-vertex-lemma` correctly (this is the fix: use the
  lemma's *slope*, not just its *breakpoint enumeration*).
- Parity: the boundary reduction ($3$ copies of $q_2$ → pair-cancel to $1$
  or after a second cancellation to $0$ copies) is a two-line parity
  argument, already the exact mechanism Vertices 3/4 used — no new tool
  needed for that step.

### Knowledge-base entries to use
- `single-insert-point-vertex-lemma` (cite for its **slope** property, a
  genuinely different use than its existing citations in this file, which
  only use it for breakpoint enumeration).
- `sharp-dominant-removal-identity` (peel $q_1-x$).
- `odd-run-reduction-lemma` / the pair-cancellation fact (used repeatedly
  in Vertices 3/4, reused for the boundary reduction).
- Lemma A / general-anchored-tie-bound, Theorem 42, insert-bound-corollary
  — per dispatch, cite these rather than re-deriving; Theorem 42 is what
  gives $A(\{x\}\cup\mathrm{tail})\ge f(m)$ one level down (used in
  Vertices 2/3, not directly needed for the new Opening-1 route but stays
  available as a cross-check).

### Analogous past problems (cruxes)
Searched `combinatorics` / `games-and-strategy`, `extremal-principle`,
`inequalities-SOS-and-convexity` in the crux corpus specifically for
"tie-breaking against a fixed anchor" style moves. Found no genuine
analog: the closest-sounding entries (`aimo-0119`, `aimo-0146`'s
exchange-smoothing, `aimo-0594`'s "domination-monotone rank sweep") are
about discrete/integer exchange arguments over *unconstrained* orderings,
not about a continuous single-free-coordinate insertion into an already-
fixed superincreasing multiset with a linked partner coordinate ($x$ and
$q_1-x$ moving together). This reconfirms the round-1 finding recorded in
`run_state.md`: **no strong direct crux analog for this problem's specific
mechanism** — do not force a transplant here; Opening 1 above is a
from-scratch (but cheap) use of already-certified in-house lemmas, which
is the right register for this gap.

### Prior progress
Per `approaches/greedy-halving-adversary.md` round 29: Vertices 1–4 of the
single-cut-on-$q_1$, tail-untouched piece of $h(m)$'s $q_1$-cut sub-case
are closed for $m\ge3$ (citing `sharp-dominant-removal-identity`,
`Theorem 42`, pair-cancellation). Vertex 5 is the sole open item in this
piece; the wider "$q_1$-cut-and-tail-refined" piece (S spends its
remaining $\le m-2$ cuts refining the tail too, not just splitting $q_1$)
is separately and entirely untouched (see below).

### Dead ends (do not retry)
- The two-step "peel $q_1-x$ exactly, then bound the remainder via
  Insert-Bound Corollary" is confirmed lossy (reproduced the exact
  shortfall numerically) — do **not** retry patching this specific bound
  with a slightly sharper constant; the fix is to replace the *bound* with
  an *exact* computation (Opening 1), not to sharpen it.
- General anchor-switching / looking for a fixed-ratio domination fact for
  $q_1$'s own split fragment (round 28's "why we did not pursue option
  (B)" discussion) is already diagnosed dead — the largest fragment of a
  split $q_1$ can approach $q_2$ in the limit with no fixed dominance
  ratio. Opening 1 above sidesteps this entirely by never needing $q_1-x$
  to dominate anything beyond the already-legal comparison to $\max(T)\le
  q_2<q_1-x$ (strict, for $x<q_1/2$), which **is** available — this is not
  the same obstruction as the "$c_2$-anchor"/round-26 dead end (that one
  needed $q_1$'s split fragment to dominate the *whole remaining
  multiset* at a much larger scale; here we only need it to dominate $T$,
  which is exactly the tail, always true for $x<q_1/2$ by the ladder's own
  doubling).

### Untouched second piece (per dispatch, scouted separately)
The "simultaneous $q_1$-and-tail cuts" piece — $S$ spends $\ge1$ cut
splitting $q_1$ **and** $\ge1$ further cut refining the tail with its
remaining $\le m-2$ budget — is completely unattempted by any approach on
file (confirmed by grep: no proposition or theorem in the file addresses
it; round 28/29's own "Open gaps" sections both flag it as fully open and
distinct from Vertex 5). It first becomes possible at $m\ge3$ (needs
budget $\ge2$: one cut on $q_1$, one on the tail). No existing lemma
directly targets it. A first cheap probe: since the tail refinement now
has $\le m-2$ of its own cuts, by the certified `vertex-minimum-theorem`
the tail's own minimizer (for *any* fixed split of $q_1$) is itself at a
tie-vertex — so this piece should decompose as "outer" min over $q_1$'s
split composed with "inner" tail-vertex minimization, i.e. it is
structurally the *same* two-level vertex problem as the untouched-$q_1$
case (Theorem 42) but with the anchor ($q_1$'s largest fragment) no
longer automatically dominant — likely the natural next target once
Vertex 5 itself is closed, but genuinely unexplored; I did not find a
reason to expect it easier or harder than Vertex 5, only that it shares
the same underlying vertex-machinery and should probably be attacked with
the Opening-1-style exact-slope-monotonicity method rather than any
peeling/bounding shortcut, given peeling's demonstrated fragility
throughout this file.

### Small-case / intuition notes (labeled conjecture where not proved)
- **Proved (not conjectured):** for every $t\in\mathrm{tail}$ and every
  fixed $t$, $F(x):=A(\{x,q_1-x\}\cup(\mathrm{tail}\setminus\{t\}))$ is
  monotonically non-increasing in $x$ on $(0,q_1/2)$ — this follows
  directly from the certified slope fact of
  `single-insert-point-vertex-lemma` plus elementary calculus
  ($F'\in\{-2,0\}$), not merely observed numerically (though also
  confirmed numerically for $m=3,\dots,7$, all $t$, zero non-monotone
  steps — script `/tmp/vertex5_check.py`-equivalent commands run inline
  above).
- **Conjectured (numeric only, not yet proved):** $t=q_2$ is the unique
  worst-case choice of $t$ for every $m$; the boundary value at $t=q_2$
  equals $f(m)$ exactly (matches the file's own claimed tightness), and
  every other $t$ gives a value strictly larger, with the margin
  apparently growing as $t$'s tail-rank gets deeper (checked exactly,
  `Fraction` arithmetic, $m=3,\dots,7$).
- Combining the proved monotonicity-in-$x$ fact with the conjectured (but
  strongly evidenced) worst-$t$-is-$q_2$ fact would fully close Vertex 5:
  the global minimum over both $x$ and $t$ is then exactly the already-
  known equality case ($t=q_2$, $x\to q_1/2$, value $=f(m)$ via the untouched
  tail identity), matching $f(m)$ with no shortfall.
