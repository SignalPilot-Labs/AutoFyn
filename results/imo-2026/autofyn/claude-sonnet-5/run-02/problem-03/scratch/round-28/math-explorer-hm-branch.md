## imo-2026-03 (lens: h(m) / "T'-cuts-p4" branch, m>=3)

### What h(m) precisely is

`greedy-halving-adversary`, round 24 (§"Definition (Standalone induction
target h(m))"), `results/imo-2026-03/approaches/greedy-halving-adversary.md`
line ~5280:

$$h(m):=\inf\{A(\{c\}\cup S): c\in(0,q_1],\ S\text{ a legal }(\le m-1)\text{-cut
refinement of the unit }m\text{-ladder }q=(q_1,\dots,q_{m+1})\}.$$

Well-posed (compact feasible region, Vertex-Minimum-Theorem applies to the
joint object $\{c\}\cup S$; certified). The reduction of the original
problem's "$T'$-cuts-$p_4$" sub-case of Case (b)'s "$v\ge a$" branch to
$h(m)$, $m=n-4$, via `general-cross-level-rescaling-lemma` ($k=4$) plus
Lemma 9 scaling, is unconditional pure algebra (round 24, certified, not at
issue). **$n$-to-$m$ map: $m=n-4$.** So $h(1)\leftrightarrow n=5$,
$h(2)\leftrightarrow n=6$, and the next open case **$h(3)\leftrightarrow
n=7$**.

### How h(1), h(2) were closed (mechanism)

Not full induction on $m$ — direct **exhaustive per-shape hand
casework**, using the general **Vertex-Minimum Theorem** (every
minimizer of $A$ over a fixed composition is at a vertex: $c=0$, $c=q_1$,
or $c$ tied to some element of $S$) plus `odd-run-reduction-lemma` /
`pair-cancellation-identity` to collapse ties, plus a piecewise-linear
sweep of $A(\{c\}\cup S)$ across every breakpoint of $S$ (`Insert-Element
Identity`, slope $\pm1$).

- **$h(1)$ (Theorem 38, round 24):** at $m=1$, $S$'s budget is $m-1=0$
  cuts, so $S$ is *forced* to be the entire untouched $1$-ladder — only
  two vertex types exist at all (Claim I: $c=0\Rightarrow A(S)\ge f(1)$
  via $(\star_1)$; Claim II: $c=q_1$, cancels with $q_1$'s own copy,
  reduces to $(\star_0)$ trivially) and they are **exhaustive by
  construction** — no casework needed beyond the two claims. Fully
  unconditional, certified `theorem-38-h1-exhaustive-closure`.
- **$h(2)$ (Theorem 39, round 25, extending round 24's partial):** at
  $m=2$, budget $=1$ cut, so exactly **4 exhaustive branches** (untouched;
  $q_1$-split; $q_2$-split; $q_3$-split) — each branch has exactly one
  free parameter, and each is closed by a direct 1-D piecewise-linear
  sweep of $A(\{c\}\cup S)$ over $c$'s breakpoints, by hand, in closed
  form. All four give $A\ge f(2)$, tight only at the two Theorem-38-style
  vertices. Certified `theorem-39-h2-closure`.

**Important, already-recorded caveat (round 24, not yet resolved for any
$m$):** the shortcut "the worst $c$, for fixed $S$, is always the
top-tie $c=\max(S)$ (or the boundary $c\in\{0,q_1\}$)" is **false** in
general — a deep interior tie ($c$ tied to the 3rd-, 5th-, ... largest
element of $S$) can be a *local* minimum not dominated by the "base
trio." A 20,000-trial exact-`Fraction` search over legal ladder
refinements at $m=2,\dots,5$ found such deep ties beating the base-trio
comparison in $\approx3.7\%$ of trials — **but never below $f(m)$
itself** (a separate 60,000-trials-per-$m$ search checking *every*
candidate vertex type found zero violations of $h(m)\ge f(m)$, equality
only at the two known vertices). So a *rigorous* proof cannot skip
deep-tie candidates even though they empirically never win.

### Is h(3) tractable by direct extension of the same technique?

**Shape/branch count explosion, confirmed by direct counting (new this
round).** At $m$, the branch count (distinct "how many cuts landed on
each of the $m+1$ pieces" patterns, summed over budgets $0,\dots,m-1$) is
$\sum_{b=0}^{m-1}\binom{b+m}{m}$ (stars-and-bars over $m+1$ pieces). This
gives:
- $m=2$: $1+3=4$ shapes — matches Theorem 39's 4 branches exactly.
- $m=3$: $1+4+10=15$ shapes (0 cuts: 1; 1 cut over 4 pieces: 4; 2 cuts
  over 4 pieces: 10 — includes both "one piece split into 3" [4 shapes]
  and "two different pieces each split once" [$\binom42=6$ shapes]).
- $m=4$: $1+5+15+35=56$ shapes.

So going from $m=2\to m=3$ is a $4\times$ jump in shape count (4→15), and
**each multi-cut shape now has $\ge2$ free continuous split parameters**
(vs. exactly 1 at $m=2$), so the piecewise-linear sweep needed to find
every breakpoint/tie candidate is a genuine 2-D (or higher) case split,
not a 1-D sweep — this is a real jump in algebraic complexity per branch,
not just "more of the same casework." This matches, both qualitatively
and in spirit, round 27's independent finding for the sibling MaxCeil
front ($C(2m-3,m)$ shape blow-up) — **the same combinatorial-explosion
pattern the dispatch flagged is confirmed here too, by direct counting,
for h(m) specifically.**

**Verdict: $h(3)$ is almost certainly still tractable by brute exhaustive
casework in a single dedicated round (15 shapes, each closable by
piecewise-linear sweep as at $m=2$, just with more sub-cases and
higher-dimensional sweeps per multi-cut branch) — but $m=4,5,\dots$ will
not be, and there is no sign the per-$m$ technique terminates in a
closed form as $m\to\infty$.** Continuing to grind $m=3,4,5,\dots$
one round at a time is exactly the trap the dispatch is asking to avoid.

### Is h(3) even true? (computational check, this round, independent of round-24's own script)

Fresh exact-`Fraction` script (`/tmp/hm_check2.py`, written from scratch
this round, not reusing the builders' own): for $m=3,4,5$, generated
20,000 random legal $(\le m-1)$-cut refinements $S$ of the unit
$m$-ladder, evaluated $A(\{c\}\cup S)$ at the candidate set
$\{0,q_1\}\cup S$ (a strict subset of all true vertex candidates — does
not include cross-pairwise-tie candidates within $S$ beyond the elements
themselves, so this is a lighter/faster check than round 24's full
60k-per-$m$ sweep, run here purely as an independent corroboration, not a
new proof):

- $m=3$: global min found over 20,000 trials $=1/15=f(3)$ **exactly**,
  no violation.
- $m=4$: global min found $=1/31=f(4)$ **exactly**, no violation.
- $m=5$: global min found $=112/5625\approx0.0199>f(5)=1/63\approx0.0159$
  (did not land on the exact tight witness with only 20,000 random
  continuous-cut trials — expected, since hitting an exact rational tie
  point by uniform random sampling has probability $0$; this is a
  sampling-density artifact, not evidence against $h(5)=f(5)$, and is
  consistent with round 24's own finding using a larger/targeted search).

**Conclusion: $h(3)=f(3)$ is true with strong (fresh, independently
re-derived) numeric support, margin is exactly $0$ at the known tight
vertices (same as $h(1),h(2)$) and strictly positive everywhere else
tested — no sign the true bound is anything other than exactly $f(m)$ at
every $m$, consistent with all prior rounds' findings. This is
corroborating evidence, not a proof.**

### Is a general-m mechanism findable (recommended next step)?

Two structural observations point toward a promising general-$m$
mechanism, **not yet attempted by any approach on file for $h(m)$
specifically**:

1. **Self-similar recursive structure already visible inside Theorem
   38/39's own case analysis.** The "$q_1$-split" branch's worst vertex
   ($c=\max(S)$, cancelling the split-off top fragment) reduces exactly
   to $A(\{x,q_2,\dots,q_{m+1}\})$ — i.e., inserting the *smaller*
   fragment $x$ of $q_1$'s split into the untouched remainder, which is
   structurally the **same kind of object one level down** (an inserted
   free value merged with a $(m-1)$-ladder-shaped tail). Separately,
   `rank-pigeonhole-budget`'s §7.9.4 (breakpoint $b=c_1$ of a *different*
   but closely related residual) explicitly notes its own reduced object
   "is precisely the sibling's $h(m)$-shaped object one level further
   down" (line ~1609 of `rank-pigeonhole-budget.md`) — i.e. **two
   independent approaches have already, separately, noticed $h(m)$-type
   objects recursing into smaller $h(m')$-type objects.** No approach has
   yet tried to formalize this into an actual induction on $m$ (as
   opposed to per-$m$ exhaustive casework).

2. **Non-$q_1$-split branches never win, only approach the bound.**
   At $m=2$: the $q_2$-split branch gives $A=1=f(2)$ *identically*, no
   matter the split point $y$ (an exact algebraic coincidence, not
   curve-fit), and the $q_3$-split branch gives $A=3-2z>f(2)$ **strictly**
   for every legal split, approaching $f(2)$ only in the degenerate limit
   (coinciding with the untouched branch). This is a clean, verified
   ($m=2$) instance of a plausible **general claim**: "splitting a piece
   $q_i$, $i\ge2$, of the $m$-ladder never produces a value below $f(m)$,
   and strictly-lower-index splits ($i$ small) are the tightest" — if
   provable in general (not per-shape), this would collapse the
   branch-explosion problem to just the two vertex types Theorem 38
   already handles, **plus** a genuine induction "if $S$ splits $q_1$,
   the worst case reduces to $h(m-1)$ (or a bound derivable from it)" —
   exactly mirroring the successful pattern of Theorem 40/41 on the
   sibling "$T'$-untouched" branch (a general deep-tie-closure theorem
   via rank-split + insert-element-identity + per-piece trivial bounds,
   proved once, for **every** $n\ge5$, no per-$n$ casework).

**Concrete most-promising next step:** attempt to adapt the **Theorem
40/41 technique** (rank-split at the tie point via `insert-element-
identity`, then bound the two resulting halves $H,L$ *separately* by
trivial per-piece bounds, rather than lump-bounding the whole tail) to
$h(m)$'s deep-tie residual directly — i.e., prove a general "$h(m)$'s
non-$q_1$/non-boundary vertex candidates are all dominated" theorem for
every $m$ at once, the same shape of result that already worked on the
structurally analogous "$T'$-untouched" branch. This is a genuinely
different target than re-running Theorem 39's exhaustive-shape technique
at $m=3$ (which would only buy one more level, $n=7$, at high cost and
with no path to general $m$).

### Cheap-kill / pruning before heavy casework

- Do **not** re-attempt the "$h(m)$ as a disguised corollary of
  $(\star_{n-4})$ via literal substitution" shortcut — **provably false**
  (`Proposition 39`, mass-conservation injectivity argument, round 25,
  certified dead end). This rules out one whole class of shortcuts before
  spending time on it again.
- Do **not** re-attempt reducing "$T'$-cuts-$p_4$" to a smaller
  self-similar $(\star_m)$ instance via a *single* rescaling step (round
  23, proven twice independently that this sub-case is not a rescaled
  ladder in that naive sense) — this is a different (and already-refuted)
  idea from the "recursive vertex structure" observation above; the
  latter is about the *behavior at specific vertices* inside $h(m)$'s own
  case analysis, not a global rescaling of the whole target, so it is not
  barred by this dead end.
- If pursuing brute-force $h(3)$ anyway: prune using the already-proven
  fact that the "$q_1$-untouched, $S$ entirely leaves $q_1$" and
  "$q_1$-split" branches are the *only* ones that have ever attained
  equality with $f(m)$ at $m\le2$ — prioritize fully closing those two
  families first (they subsume the two Theorem-38 vertex types plus
  their $m=3$-level generalizations) and treat the other $\sim13$ shapes
  at $m=3$ as "only need a strict-inequality margin," which is usually an
  easier (non-tight) bound to establish than an exact equality case.

### Knowledge-base / lemma entries relevant to this branch

- `lemmas/theorem-38-h1-exhaustive-closure.md` (certified: $h(1)=f(1)$)
- `lemmas/theorem-39-h2-closure.md` (certified: $h(2)\ge f(2)$)
- `lemmas/proposition-39-mass-conservation-obstruction.md` (certified
  dead-end record: no literal $(\star_k)$-substitution shortcut exists)
- `vertex-minimum-theorem`, `odd-run-reduction-lemma`,
  `pair-cancellation-identity`, `insert-element-identity`,
  `general-cross-level-rescaling-lemma`, `alternating-sum-scaling`
  (all certified, all directly load-bearing for any $h(m)$ work)
- `even-multiplicity-non-maximal-tie-closure` / Theorem 40 (odd case) —
  the technique to adapt (rank-split + per-piece trivial bounds), proved
  on the sibling "$T'$-untouched" branch, not yet tried on $h(m)$.
- `sigma2-untouched-closure-theorem` (§7.14, `rank-pigeonhole-budget`) —
  another example, on the separate MaxCeil front, of a general-$m$
  (budget-free, no shape enumeration) theorem replacing per-shape
  casework — the template this branch should aim to replicate.

### Analogous past problems (crux corpus)

Not separately queried this round (dispatch is narrowly scoped to
understanding $h(m)$'s internal structure and tractability, which is
better served by the on-file combinatorial/algebraic analysis above than
by an external crux search); the general shape — "prove a piecewise-affine
functional is minimized at a small finite family of tie-vertices,
uniformly in a size parameter $m$, rather than by per-$m$ vertex
enumeration" — is the same shape of difficulty already explored via the
existing sibling fronts (`rank-pigeonhole-budget`'s §7.11 Index-Chain
Identity, §7.14 σ2-Untouched Closure Theorem) rather than via the crux
corpus; no new crux match found beyond what prior rounds already used.

### Prior progress summary

$h(1)$ (n=5) and $h(2)$ (n=6) fully, unconditionally closed. $h(3)$
(n=7) open; almost certainly true (fresh numeric corroboration this
round, zero violations, exact equality at $m=3,4$); tractable by direct
per-shape extension of Theorem 38/39's technique (15 shapes at $m=3$,
confirmed by direct stars-and-bars count) but this does **not** scale to
general $m$ (56 shapes at $m=4$, growing combinatorially, each with more
free parameters and deeper-tie sub-cases per branch). The single most
promising concrete next step is **not** "grind $m=3$" but **attempt a
general-$m$ deep-tie-domination theorem for $h(m)$** modeled directly on
Theorem 40/41's successful rank-split mechanism (already proved to work
on the structurally analogous "$T'$-untouched" branch's own deep-tie
residual) — a genuinely different, likely-more-productive target than
continuing the per-$m$ exhaustive casework the project has used for
$m=1,2$.

### Dead ends (do not retry)

- "$h(m)$ as a disguised corollary of $(\star_{n-4})$ via literal
  substitution" — proven false (`Proposition 39`, round 25).
- Reducing the whole "$T'$-cuts-$p_4$" sub-case to a single rescaled
  $(\star_m)$ instance via one global rescaling step — proven not a
  rescaled ladder in that sense (round 23, two independent derivations).
- The naive "worst $c$ is always $c=\max(S)$ (or $c\in\{0,q_1\}$)"
  shortcut — proven false for generic $S$ ($\approx46\%$ of arbitrary-$S$
  trials) and even for legal ladder-refinement $S$ ($\approx3.7\%$ of
  trials, $m=2,\dots,5$) — any future proof must handle deep-tie
  candidates explicitly, it cannot assert top-tie dominance as a
  shortcut.
