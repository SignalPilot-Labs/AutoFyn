# Outline-reviewer report — round 3, imo-2026-03

## Summary

Read `current.md`, all 6 approach files (+ the 2 orphan/ghost files) in
`approaches/`, and `/tmp/round-3/proof-outliner.md`. Adversarially checked
the outliner's field before any build effort, per the round's assignment.
No approach was cut as doomed — see per-approach verdicts below — but one
registered slug with no file and no viable premise (`integer-lattice-
reduction`) is formally deprioritized rather than built. Registered the 3
new approaches, ranked the whole field head-to-head (12 comparisons folding
in round 2's outcomes plus the new field), and emit a build set of the 3
new approaches, per CLAUDE.md's shared-gap-plateau rule (none of the 3 live
approaches had genuine new proof content to build this round; re-building
them would repeat round 2's stall).

## Adversarial check of each approach

**Live approaches (3) — no revision needed, nothing to cut.**
- `greedy-halving-adversary`: Lemmas 1–9 and the Key Lemma are sound
  (spot-checked the Key Lemma's $p_1\le 2r$ algebra and Lemma 7/8's
  threshold-splitting derivations — no error found). Its Open gap 0 (the
  cross-term inequality) is honestly stated as unproved, not smuggled in.
  Not doomed — the machinery is correct and reusable even though the round's
  own crux is unresolved.
- `smoothing-compactness-certificate`: spot-checked the `(1,0,1)` and
  `(0,1,1)` median identities ($\Phi=5-\text{median}$,
  $\Phi=5+q_2-\text{median}$) by re-deriving the max+min=total-median fact
  for 3 elements and confirming the case splits are exhaustive (3
  mutually-exclusive median cases each time) — correct. This is the
  strongest fully-closed result in the workspace (n=2, both directions,
  zero numerics); genuinely not doomed, its general-n gap is honestly
  scoped as unattempted.
- `self-similar-potential-certificate`: verified Lemma A's algebra
  ($f(n)=p_1-r$ and $f(n)=r\cdot f(n-1)$ both check out by direct
  substitution) and Lemma B's case split (at most one fragment of $p_1$
  exceeds $r$, using $p_1\le 2r$ — matches the sibling Key Lemma exactly).
  The reported negative result (mass-based insertion bound degrades to
  $f(n)-p_1<0$, vacuous) is correct and valuable — not doomed, converges
  honestly onto the same obstruction rather than hiding it.

**New approaches (3) — checked for unjustified leaps before registering.**
- `self-similar-bracketing`: independently re-verified the load-bearing
  new claim (the $c=n$ alternation) by direct algebra: $q_i>p_{i+1}
  \iff 2^{n+1}>2^{n+1}-1$ (always true) and $p_{i+1}>q_{i+1}\iff
  2^{n+1}-1>2^n$ (true $n\ge1$); with $q_i=p_1\cdot p_i(n)$, all $n+1$
  fragments of $p_1$ land on odd ranks and all $n$ tail pieces on even
  ranks (piece count $2n+1$ checks out), giving $\Phi=p_1\sum p_i(n)=p_1$
  exactly. This is genuinely new, genuinely correct, and not previously
  found by any approach — the strongest-grounded new entry. Its Step 3
  induction invariant is honestly flagged as unstated, not smuggled in as
  proved. Not doomed; register and prioritize.
- `rank-tie-vertex-reduction`: the core mechanism (fixed sorted-order
  region $\Rightarrow$ $\Phi$ affine in the free cut coordinates $\Rightarrow$
  affine function on a polytope extremizes at a boundary/tie) is sound
  reasoning, not a leap — each piece length is affine in adjacent cut
  positions, so a sum of a fixed rank-subset is affine on each fixed-order
  region. Grounded in a concrete, reproducible $n=3$ tie example, not just
  a plausible-sounding claim. The outline is honest that Step 2 (ruling out
  exotic non-two-way-tie minima) and Step 3 (the tie-enumeration) are
  unproved and may be as hard as the original gap — flagged, not hidden.
  Not doomed; register.
- `exchange-argument-extremal-response`: the weakest-grounded of the three
  (Step 3's "rigid pairing shape" is explicitly conjectural, and the
  crux-of-the-whole-approach two-cut exchange condition is "not yet even
  stated precisely" per its own outline) — but this is normal for a
  round-0 outline, not a logical error, and existence-of-minimizer +
  single-cut stationarity (Step 1, 2a) are genuinely easy and correct
  (compactness of a finite union of closed simplices, continuity of a
  piecewise-linear function). It is the most structurally different
  mechanism from the other two new approaches (variational/local-swap vs.
  vertex-geometry vs. induction-on-budget-split) — worth testing for
  diversity even though it is currently the least concrete. Not doomed;
  register, ranked lowest of the three new entries pending real content.

No approach is cut this round. The three new approaches are genuinely
different mechanisms from each other and from the three live ones (per
CLAUDE.md's instruction on breaking a shared-gap plateau, confirmed by
re-deriving/spot-checking their core claims above rather than taking the
outliner's word for it).

## Workspace inconsistencies resolved

- **`integer-lattice-reduction`** (elo 1454, expanded 0, no approach file):
  confirmed via the ranker script (`.autofyn/approach_ranker.py`) that there
  is **no hard-retire tool** — Elo is designed to be "never hard-retired,"
  only naturally down-sampled by P-UCB. Since a formal deregister isn't
  available, I did the next best thing: included it in this round's
  head-to-head comparisons as the loser against every other approach
  (reflecting the round-3 integer-lattice explorer's finding that the
  framing is not viable as scoped — the LP-vertex reduction buys no
  leverage, the resulting finite search is exactly as hard as the
  continuous problem). Its Elo dropped from 1454.0 to **1380.9**, now the
  clear bottom of the field, and it is excluded from the build set. Per the
  outliner's recommendation, **no stub file was created for it** — do not
  dispatch a builder to it; it remains a ghost ranker entry by design
  constraint, but effectively retired via Elo and by never being sampled
  into a build set.
- **`induction-first-move-reduction.md`**: confirmed this file has no
  ranker entry (never registered) and should stay that way — it is a
  round-1 dead end with an unrepaired fatal arithmetic error
  ($2^n+2^{n-1}\ne2^n$) in its core recursion. Left untouched, excluded
  from ranking, as the outliner recommended. Not re-registered.

## Ranking (post round-3 update_ranking, 12 comparisons)

Best-first by Elo after folding round 2's outcomes (verified-milestone >
advanced > partial) and seeding the new field by outline strength:

1. `greedy-halving-adversary` — 1564.8 (↑ from 1559.1)
2. `smoothing-compactness-certificate` — 1545.7 (↑ from 1502.2)
3. `self-similar-bracketing` — 1541.4 (new, seeded high: concrete verified
   new endpoint result)
4. `rank-tie-vertex-reduction` — 1512.4 (new, seeded mid: sound mechanism,
   concrete n=3 example, but core lemma unproved)
5. `exchange-argument-extremal-response` — 1481.4 (new, seeded low: crux
   condition not yet even stated)
6. `self-similar-potential-certificate` — 1473.4 (↓ from 1484.7: genuine
   partial progress and a valuable negative result, but weakest outcome of
   the 3 live approaches this round)
7. `integer-lattice-reduction` — 1380.9 (↓ from 1454.0: confirmed
   non-viable as scoped, sunk to bottom, effectively retired)

## Build set rationale

None of the 3 live approaches has a genuine new proof step to build this
round (per the outliner's own assessment, confirmed above) — building them
again would very likely just restate round 2's stall. Per CLAUDE.md's
explicit plateau-break instruction ("put ≥1 approach on the table that
attacks the problem from a genuinely different framing... Don't just route
around that gap"), and since this round opened 3 such approaches
specifically to test different mechanisms against the located obstruction,
the build set is all 3 new approaches — this is the round to actually find
out whether any of them gains real traction, rather than spend builder
effort re-deriving already-recorded stalls.

build set: self-similar-bracketing, rank-tie-vertex-reduction, exchange-argument-extremal-response
