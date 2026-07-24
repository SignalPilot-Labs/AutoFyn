## imo-2026-03 (lens: h(m) q1-cut sub-case, m>=3)

### Setup recap (for the outliner, not re-derived)
$h(m):=\inf\{A(\{c\}\cup S): c\in(0,q_1],\ S$ legal $(\le m-1)$-cut refinement
of the unit $m$-ladder $q_1>\dots>q_{m+1}\}$. Theorem 42 (round 28, built on
new Lemma A = General Anchored-Tie Bound, certified as
`lemmas/general-anchored-tie-bound.md`) closes the **q1-untouched** sub-case
for every $m\ge1$ at once. The **q1-cut** sub-case ($S$ spends some of its
budget splitting $q_1$ itself into $\ge2$ fragments) is open for $m\ge3$
(closed by hand only at $m\le2$). The file's own diagnosis: no fixed anchor
$w$ was found with $w>\max(\text{everything else})$ unconditionally, because
the larger fragment of $q_1$'s split can approach $q_2$ in the limit, at
which point it no longer strictly dominates the (still-present) original
tail.

### Distinct openings

**1. (Strongest, concrete, worth trying first) "Switch-the-anchor" case
split on $c$ vs. $q_1{-}x$, single-cut-on-$q_1$ sub-branch.** Consider the
narrowest piece of the q1-cut territory first: $S$ spends exactly one cut on
$q_1\to(x,q_1-x)$, $x\le q_1-x$, and leaves the rest of the tail
$\{q_2,\dots,q_{m+1}\}$ **untouched** (this is presumably the base case any
general argument must handle first, and is exactly the situation Theorem 38
hand-checked at $m=2$). The reported "degeneracy" is about a *single fixed*
anchor $w=q_1-x$ losing dominance as $x\to q_1/2^-$ — but note $q_1-x>q_2=
\max(\text{tail})$ **strictly** for every $x<q_1/2$ (only exactly at
$x=q_1/2$ does $q_1-x=q_2$, the already-closed symmetric-split vertex). So
for $x<q_1/2$, the *only* way domination by $w=q_1-x$ can fail is if $c$
itself exceeds $q_1-x$. But if $c>q_1-x$, then since $c\le q_1$ and
$q_1-x>q_2\ge\max(\text{tail})$, $c$ **itself** dominates
$\{x,q_1-x\}\cup\text{tail}$ (as $c>q_1-x>q_2=\max(\text{tail})$, and
trivially $c>x$). So the two candidate anchors $w=q_1-x$ (when $c\le q_1-x$)
and $w=c$ (when $c>q_1-x$) jointly and exhaustively cover the whole range of
$c$ for this sub-branch — the degeneracy the file reports is really only at
the single boundary point $x=q_1/2$, already handled, not a genuine
obstruction across the interior. **This has not been checked/written up by
any approach on file** (Theorem 38 handled $m=2$ by direct hand algebra, not
via this anchor-switching principle) — it looks like a clean, general-$m$
closure of the "single cut spent entirely on $q_1$, tail else untouched"
piece of the q1-cut sub-case, reusing Lemma A twice (once per anchor choice)
rather than needing a new lemma. Flag as an opening, not a proof — the
multiplicity bookkeeping when $c$ ties exactly to $x$, $q_1-x$, or a tail
element still needs the same odd/even-parity care Lemma A already handles,
and this only resolves the *single-cut-on-$q_1$* piece, not simultaneous
cuts on $q_1$ and the tail.

**2. Import the Case-I-closure mechanism (exchange-smoothing-vertex-
maximization) instead of a fixed-anchor domination lemma.** Claim (A)'s own
Case I (round 8) was closed *not* by finding one dominant anchor but by a
genuinely different mechanism: dualize `vertex-minimum-theorem`'s exchange
argument to a **maximum**, reducing the continuum to a small "pinned + one
tied group" family (Ratio-2 Spacing Lemma, Last-Element Bound), then
evaluate each surviving profile via `odd-run-reduction-lemma`. $h(m)$'s
q1-cut sub-case has the same shape (a free coordinate $c$ plus a
budget-constrained multiset built from splitting ladder pieces) — the
domination-anchor approach is not the only tool in the population that
handles "no single element dominates" configurations. This is a genuinely
different top-level mechanism from Lemma A/Theorem 40-42's peel-and-anchor
recipe, worth assigning to a separate approach rather than iterating on
anchor search.

**3. Pair/mass-conservation anchor instead of single-element anchor.** Since
$x+(q_1-x)=q_1$ exactly regardless of how $q_1$ is split, an alternative
mechanism treats the **pair** $\{x,q_1-x\}$ jointly (via
`peel-decomposition-identity`/`cross-term-reduction-theorem`, both already
certified) rather than requiring one of the two fragments alone to dominate
everything else. This could recover an *exact identity* for $A(\{c\}\cup
\{x,q_1-x\}\cup S'')$ in terms of $A(S'')$ and the fixed mass $q_1$, sidestepping
the single-anchor-domination requirement altogether — genuinely different
from Lemma A's "find $w$" recipe, in the spirit of `case-ii-exact-peel-
identity`'s mechanism (peel by a value, not by domination margin).

**4. Bracket the split point directly (revive `self-similar-bracketing`'s
idea, but on this narrower target).** The file's own diagnosis pins the
danger zone to $x$ near $q_1/2$. A genuinely different route: treat $h(m)$
restricted to the single-cut-on-$q_1$ branch as a function of $x\in(0,q_1/2]$
and show it is monotonic (or convex, attaining its minimum only at the two
endpoints $x\to0$ and $x=q_1/2$, both already closed by Theorem 38/42) —
i.e. prove a **monotonicity-in-$x$** lemma for this one-parameter family
directly, rather than hunting for a domination anchor. This is weaker in
scope than opening 1 (only covers the single-cut branch) but is a genuinely
different *proof technique* (calculus/slope argument on a 1-parameter
family, akin to the already-certified `insert-element-identity`'s slope
formula) that could be pushed further once established.

**5. Small-case exhaustive closure of $h(3)$ specifically.** The round-28
explorer counted ~15 candidate shapes at $m=3$ (several cutting $q_1$). Given
how much machinery already exists (Lemma A, odd-run-reduction, vertex-
minimum-theorem), a direct by-hand (or careful symbolic) closure of $h(3)$
alone — mirroring the $h(1)$, $h(2)$ pattern — would not resolve general
$m$ but would supply a third data point and might reveal the actual
worst-vertex pattern needed to design the real general-$m$ induction. Lowest
risk, lowest reward; good "insurance" approach if 1-4 stall.

### Candidate technique(s)
Anchor-switching case split (opening 1) is the most immediately checkable;
exchange-smoothing-vertex-maximization (opening 2, already certified
elsewhere in this project) is the most structurally different mechanism on
offer; pair-anchor/mass-conservation peel (opening 3) reuses certified
identities in a new combination.

### Cheap-kill candidates
- Check opening 1's anchor-switching argument numerically first (cheap,
  `python3`/`Fraction`, single-cut-on-$q_1$ branch only, $m=3,4,5$) before
  committing an approach to writing it up — if it holds it is a genuine
  general-$m$ closure of a real slice of the open territory with almost no
  new machinery.
- Parity/multiplicity check: at the conjectured worst vertex for each $m$,
  does $q_1$'s fragment always end up tied (even multiplicity) with an
  existing tail value? If so the already-certified even-$\mu$ half of Lemma
  A may already cover it once the right anchor is identified — worth a
  quick numeric scan across the ~15 $m=3$ shapes before inventing a new
  lemma.

### Knowledge-base entries to use
`knowledge_base.md`'s General Proof Methods (exchange/smoothing arguments)
and Problem-Solving Heuristics (specialize/generalize, work backwards) are
the generic entries; the load-bearing project-specific machinery is all in
`results/imo-2026-03/lemmas/` (`general-anchored-tie-bound`,
`odd-run-reduction-lemma`, `vertex-minimum-theorem`,
`cross-term-reduction-theorem`, `case-ii-exact-peel-identity`,
`exchange-smoothing-vertex-maximization` / `case-i-closure-theorem` from
Claim (A)'s own closure — the last is the specific reusable mechanism behind
opening 2).

### Analogous past problems (cruxes)
Queried `past_crux_moves_database.json` (`domain=combinatorics`,
subtopics `extremal-principle`/`games-and-strategy`/
`invariants-and-monovariants`) for ladder/doubling/exchange/adversary
keywords.
- **aimo-0146** — crux: "Maximize a fixed weighted sum of a sorted
  nonnegative integer sequence under a sum constraint by exchange-smoothing
  weight toward the higher-coefficient positions until the free coordinates
  equalize and the tail drains, then enumerate the few surviving profiles."
  This is structurally the closest analog on file to opening 2: an
  exchange-smoothing argument that collapses a continuum/integer optimum to
  a handful of extremal profiles without needing a single dominant anchor —
  exactly the mechanism that already worked for Claim A's Case I in this
  project. Worth re-reading `past_problems_database.json`'s solution for
  aimo-0146 if opening 2 is pursued, for the exact "few surviving profiles"
  bookkeeping pattern.
- **aimo-0117** — crux: dyadic/geometric sequence where the single largest
  value strictly exceeds the sum of all others (an "anchor dominates
  everything" construction). This is the *same flavor* as the Lemma A
  domination recipe already tried and diagnosed as degenerating for the
  q1-cut case — **already flagged as a dead end for a different part of
  this project** (`claiming-order-invariant`, round 4, RETHINK) for an
  unrelated reason (no strategic freedom in the marking stage), but worth
  noting here too: it does not obviously suggest a fix for the q1-cut
  degeneracy since that degeneracy is precisely the "anchor no longer
  strictly exceeds the rest" failure this crux's mechanism assumes away.
  Not a match to build on for this sub-target — noted to prevent
  re-attempting it as if it were new.
- No crux found that treats a "pair of a split object" as a joint anchor
  (opening 3) — nothing genuinely analogous located; do not force a match.

### Prior progress
Theorem 42 + Lemma A (certified `general-anchored-tie-bound`) fully close
$h(m)$'s q1-untouched sub-case, every $m\ge1$. $h(1)$, $h(2)$ fully closed
(both sub-cases). $h(m)$, $m\ge3$, q1-cut sub-case: open. No domination
lemma found on file for it; the search for one was reported honestly as
unattempted-to-completion, not as a proven negative result — i.e. it is not
established that no domination-based fix exists, only that the *first*
natural candidate (a single fixed-ratio anchor) fails at the boundary.

### Dead ends (do not retry)
- A single fixed-ratio domination anchor (analogous to $q_1=2q_2$) for
  $q_1$'s own split fragment: confirmed (not just suspected) to degenerate
  as the split approaches $q_1/2$, per the file's own round-26 "$c_2$-anchor"
  diagnosis and round-28's explicit restatement. Opening 1 above is *not*
  a retry of this — it resolves the degeneracy by switching which quantity
  serves as anchor ($c$ vs. $q_1-x$) rather than insisting on one fixed
  choice.
- "$h(m)$ as a literal corollary of $(\star_{n-4})$ via substitution":
  rigorously refuted, round 25, Proposition 39 (Mass-Conservation
  Obstruction) — $\{c\}\cup S$ is provably not a legal response to any fixed
  ladder for a whole interval of $c$. Do not re-attempt any rescaling that
  treats $\{c\}\cup S$ as itself a legal ladder response.
- "The worst $c$ for fixed $S$ is always the top-tie": refuted numerically
  and by exact computation, round 24 (deeper odd-rank ties beat the top tie
  in ~3.7% of legal-ladder trials) — any argument for the q1-cut case must
  independently justify which tie-vertex is worst, not assume it is the top
  one.

### Small-case / intuition notes (conjecture, not proof)
- Numerics (round 24/25, 60,000 trials per $m=2,\dots,5$, joint search over
  $c$ and legal $S$) found $h(m)=f(m)$ exactly at every $m$ tested, never
  below — strong evidence the conjecture $h(m)\ge f(m)$ is simply true for
  all $m$, consistent with every other sub-case closed so far. No evidence
  the q1-cut branch behaves differently in value, only that its *proof
  mechanism* is harder to find.
- Opening 1's anchor-switching argument, if it checks out numerically, would
  suggest the "hard part" of the q1-cut sub-case is not the single-cut-on-
  $q_1$ branch at all, but branches where $S$ splits $q_1$ **and**
  simultaneously refines the tail with its remaining budget (only relevant
  for $m\ge3$, since $m=2$'s single cut is entirely spent on one piece) —
  narrowing the true open territory further than the current "all of q1-cut,
  $m\ge3$" framing suggests.
