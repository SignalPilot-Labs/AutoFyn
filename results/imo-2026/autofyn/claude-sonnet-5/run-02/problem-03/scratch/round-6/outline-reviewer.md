# Outline-reviewer report, round 6 — IMO-2026-03

## Context read
`/tmp/round-6/proof-outliner.md`, `results/imo-2026-03/current.md`, all 14
files under `approaches/` (including the orphan `induction-first-move-
reduction.md`), all 30 files under `lemmas/`, and `.ranking.json`. Also
pulled the precise statement of $(\star\star)$ from
`rank-tie-vertex-reduction.md` §5.1 (Cross-Term Reduction Theorem) to check
whether the round's "new framings" genuinely attack it from a different
angle or are relabelings.

## Verdict on the shared-gap-plateau diagnosis
Confirmed independently: $(\star\star)$ —
$\int_{W\cap[0,r)}v(t)\,dt\le\Delta/2$ (window of length $\Delta$ straddling
$p_1/2$, $v$ the tail's odd-parity indicator) — is derived cleanly in §5.1
as the exact residual of the Cross-Term Reduction Theorem, and §5.2 there
honestly cross-checks it against `greedy-halving-adversary`'s claim (B) and
`rank-pigeonhole-budget`'s band-occupancy minimization, confirming (not
assuming) all three ask for the same fact in different language. This is a
correctly-earned plateau, not premature pattern-matching. Round 6 opening
new framings is warranted.

## Review of the three new approaches

**`lp-duality-certificate` — KEEP, high priority.** Genuinely different
top-level architecture: it drops induction on $n$ altogether and asks for a
single nonnegative-combination (LP-dual) certificate valid on the whole
`vertex-minimum-theorem` polytope at once. This structurally cannot hit the
diagnosed failure mode (an induction needing an unavailable upper bound on
a sub-instance), since there is no sub-instance step. It correctly leans on
already-certified machinery (`vertex-minimum-theorem`, `odd-run-reduction-
lemma`) rather than re-deriving it, and its first deliverable (reverse-
engineer a certificate from the fully-closed $n=2$ case) is concrete and
checkable. Real risk, honestly flagged in the outline itself: LP dual
certificates need not vary recursively with problem size, so a certificate-
recursion (step 4) may simply not exist even if $n=2$'s certificate is
found. That's an acceptable, well-scoped risk for a new-framing approach.
Approved, registered.

**`integer-lattice-reduction` — KEEP, but flag it precisely.** This does
**not** abandon $(\star\star)$; it re-targets the exact same window integral
via a different technique (exact binary-digit/carry computation instead of
a mass/rank/band bound). I checked whether this counts as "a bypass in the
same framing" (which the plateau rule forbids) versus a genuinely different
technique: the five plateaued approaches all tried to *bound* the integral
by some coarsening (mass, rank order, dyadic bands); this one tries to
*compute* it exactly via the ladder's binary structure — a different proof
technique on the same target, which is legitimate (CLAUDE.md's concern is
approaches that are variations of one *framing*, not one that brings an
unrelated toolbox to bear on the known crux). Its step-2 sub-lemma
(minimizing-vertex fragment values are rational with denominator dividing
$D=2^{n+1}-1$) is well-motivated by `vertex-minimum-theorem`'s tie-equalities
being rational, looks tractable, and is reusable by the sibling approaches
regardless of outcome — good low-risk first deliverable. The outline itself
honestly flags that the crux-corpus leads (`aimo-0141`, `aimo-0917`,
`aimo-0764`) concern static sets/monovariants, not a minimax, so the
transplant to step 3 (the actual digit formula) is unconfirmed. Refreshed
its stale round-4 one-liner summary in the ranker to the sharper round-6
plan. Approved, kept live.

**`bijective-mersenne-pairing` — KEEP as a time-boxed scout only.** This one
I scrutinized hardest for being a superficial relabeling, since "pairing
argument" is a common trope that often just re-encodes a mass bound. On
inspection it is a legitimately different top-level architecture (no
top/tail generation split at all — direct rank-based pairing on the final
multiset), but the outline's own honest self-assessment is right: it is
unmotivated by the diagnosed failure mode (unlike `lp-duality-certificate`,
it doesn't structurally avoid needing an upper bound; it just doesn't use
induction either, so it's an open question whether it reproduces or evades
$(\star\star)$-style difficulty at all), and step 1 is a strict go/no-go
gate on the fully-known $n=2$ case. Approved for a single tightly time-boxed
build only — if the $n=2$ pairing isn't found quickly, this should die next
round per its own outline's watch-out clause ("do not accept a pairing rule
that works by construction only for extremal families already known to hit
the target").

## Cut / deprioritized this round
- **`induction-first-move-reduction`** (orphan, round-1, never registered,
  0 builds): agree with the outliner's audit — its own Step 6 records a
  genuine arithmetic contradiction ($2^n+2^{n-1}\ne2^n$) in the naive
  "peel one top piece of size $p$, recurse on the remainder for both
  bounds" recursion, and its top-level architecture is exactly the
  "reduce size $n$ to size $n-1$ via a single peel" pattern already shown
  (by five independent framings) to bottom out on $(\star\star)$ one level
  down. **Not registering, not building.**
- **`dyadic-band-occupancy`**: its own round-5 build already proved its
  assigned coarse technique cannot close claim (A) without at least
  `rank-pigeonhole-budget`'s finer per-band shape data (a certified
  negative result, not a guess) — deprioritized, not rebuilding.
- **`claiming-order-invariant`**: RETHINK/dead-end on record (round 4,
  rigorous structural argument, no repair proposed) — deprioritized, not
  rebuilding.
- **`self-similar-bracketing`**: Prop B2 showed the bracketing-by-endpoints
  premise is false (the $c=n$ endpoint is not free) and zero progress on
  the actual interior target — deprioritized this round; would need a
  genuine re-plan (RETHINK-adjacent) before another build is worth it.

## Numeric/small-case sanity check (per this round's specific caveat)
Round 4 and 5 both caught false small-case claims at this stage, so I
independently re-verified every numeric assertion in the three new outline
files rather than trusting them:
- $D=2^{n+1}-1=\sum_{i=0}^n 2^i$ — correct, direct geometric-sum identity.
- $c(2)=4/7$ used by `bijective-mersenne-pairing`'s $n=2$ test ladder
  $\{4,2,1\}/7$ — matches the already-certified `n2-lower-bound-full-
  closure`/`n2-upper-bound-lp-argument`, and $2^2/(2^3-1)=4/7$. Consistent.
- The $n=3$ tie example $S=\{4,4,3,2,1,1\}$ (units of $1/15$) referenced by
  `lp-duality-certificate` step 5 — re-verified by hand: sorted descending
  alternating sum $4-4+3-2+1-1=1$, odd-rank sum $4+3+1=8$, $\Phi=8/15=c(3)$
  ($2^3/(2^4-1)=8/15$). Matches the on-file computation in
  `rank-tie-vertex-reduction.md` §3 exactly — no discrepancy.
None of the three new outlines assert an unverified numeric claim as
established fact; all numeric material they cite is either already
reviewer-certified on file or elementary algebra I re-checked directly. No
false claims found this round.

## Ranking
Registered the three new approaches (`register_approach`); refreshed
`integer-lattice-reduction`'s stale round-4 summary to the round-6 plan.
Ran `update_ranking` with 15 head-to-head comparisons reflecting: the two
most-targeted new framings (`lp-duality-certificate`, `integer-lattice-
reduction`) beating the confirmed-insufficient/dead approaches
(`dyadic-band-occupancy`, `claiming-order-invariant`, `self-similar-
bracketing`) and drawing with the current co-leaders
(`rank-tie-vertex-reduction`, `rank-pigeonhole-budget`); the time-boxed
scout `bijective-mersenne-pairing` beating only the confirmed dead-end and
drawing with the weakest live approach; and the existing co-leaders
(`greedy-halving-adversary`, `rank-tie-vertex-reduction`,
`smoothing-compactness-certificate`) holding position via mutual draws
since none advanced further this round. Resulting order (best-first, post
update):
1. `greedy-halving-adversary` (1602.5)
2. `rank-tie-vertex-reduction` (1571.5)
3. `smoothing-compactness-certificate` (1566.2)
4. `lp-duality-certificate` (1555.9, new)
5. `rank-pigeonhole-budget` (1535.4)
6. `bijective-mersenne-pairing` (1502.7, new)
7. `dyadic-band-occupancy` (1477.5)
8. `exchange-argument-extremal-response` (1456.0)
9. `self-similar-potential-certificate` (1443.7)
10. `integer-lattice-reduction` (1438.3)
11. `self-similar-bracketing` (1418.9)
12. `claiming-order-invariant` (1404.9, dead-end)

## Build set rationale
Dispatch the two most-targeted new framings in full
(`lp-duality-certificate`, `integer-lattice-reduction`) plus the cheap
time-boxed scout (`bijective-mersenne-pairing`, single tightly-scoped
attempt, drop fast on failure at its own go/no-go gate). Alongside these,
continue exactly the two live approaches with tractable residual gaps that
are *not* $(\star\star)$ itself, per their own round-5 notes: `rank-tie-
vertex-reduction` (§5.3's $n\le7\to$general-$n$ corollary finish, a small
closed-form algebra item) and `rank-pigeonhole-budget` (finish Case II's
remaining sub-range and Case I). Not rebuilding `greedy-halving-adversary`
or `smoothing-compactness-certificate` this round since their open items
are exactly $(\star\star)$-equivalent or the harder untouched general upper
bound respectively — no new angle to give them this round.

build set: lp-duality-certificate, integer-lattice-reduction, bijective-mersenne-pairing, rank-tie-vertex-reduction, rank-pigeonhole-budget
