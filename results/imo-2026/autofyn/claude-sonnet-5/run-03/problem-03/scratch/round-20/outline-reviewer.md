# Outline review — round 20, imo-2026-03

Reviewed `/tmp/round-20/proof-outliner.md` against
`results/imo-2026-03/approaches/self-similar-induction-on-n.md` and
`.../global-lp-vertex-sufficiency.md`, `current.md`, and
`knowledge_base.md`. Both are `revise` of live, registered approaches —
no new slug proposed this round, nothing to newly register.

## `self-similar-induction-on-n`: CHANGES REQUESTED

**Target**: general-$k$ matching lower bound for GCH($k$)
($\mathrm{AltSum}(R\cup\Gamma_{k-1})\ge1$), the last gap before GT($m$)
sub-case (i) closes completely.

**Verified correct / sound so far:**
- The certified lemmas this outline builds on (Lemma TPC, Lemma BCF +
  Corollary, Lemma LNI) are exactly as stated in the approach file and
  match the certified cache; re-derived TPC/BCF by hand (rank-parity
  argument is elementary and correct) and independently re-ran a
  multi-restart SLSQP sweep ($k=3,4,5$, ~40 trials × several $n$,
  fresh script, not reusing the builder's) — **zero violations of
  AltSum ≥ 1**, corroborating the theorem's truth (not its proof).
- Step 2's *literal* claim — "among any set of $\ge2$ **distinct**
  values occupying a single contiguous rank-block (no $\Gamma$-element
  interleaved among them), some adjacent pair has opposite rank parity"
  — is true and in fact trivial: ranks alternate parity by
  construction, so any two rank-adjacent free coordinates automatically
  have opposite parity, and LNI kills that pair immediately. This part
  of step 2, as scoped to a single Γ-gap, is fine and should be quick
  to formalize.

**Real gap found, not currently flagged by the outline:** the outline's
step 1 restates, as already established, that "a minimizer's free
coordinates are... at most one additional free block... of a single new
value." This is **not** yet proved by LNI+TPC as stated. LNI only rules
out **pairs of free coordinates with opposite overall rank parity** — it
says nothing about two free coordinates sitting in **different**
Γ-gaps (i.e., with a Γ-tied element wedged between them) that happen to
land on the **same** rank parity. Such a configuration is not touched by
LNI at all (rate is 0 for same-parity pairs) and is not addressed by
step 2 either (step 2 only treats $\ge3$ distinct values *within one
block*). I hand-built a same-parity, two-different-gap scenario
structurally consistent with this gap (e.g. one free element in gap
$(2^{k-2},2^{k-1})$ and one in gap $(2^{k-4},2^{k-3})$, separated by an
odd number of intervening odd-multiplicity Γ-ties) and confirmed the
outline's own text nowhere rules this shape out. My own numerical sweep
found no violation from this shape either (consistent with the theorem
being true), but that does **not** establish the *proof strategy*
("finite reduction to a single free block") is complete — it only shows
the counterexample I looked for isn't a counterexample to the theorem,
which is a weaker fact than "the reduction captures every candidate
minimizer."

**What to change:** step 2 must be broadened (or a new step 2.5 added)
to also prove that a minimizer cannot have free elements split across
**two or more distinct Γ-gaps simultaneously** — not just that a single
gap can't hold $\ge3$ distinct values. This is likely provable by a
similar-in-spirit argument (e.g. show any two same-parity free
coordinates in different gaps admit *some* joint perturbation — not a
simple pairwise transfer, since that changes AltSum at rate 0, but
possibly a coordinated 3-way transfer bringing in a third element, or an
argument that a same-parity multi-gap configuration is dominated by a
single-gap one via a different mechanism) but as of this outline it is
an unaddressed hole in the "Finite Reduction Theorem," not merely an
open sub-case of an already-complete reduction. Flag this explicitly to
the builder as a second load-bearing item alongside the outline's own
step 2, before trusting steps 3–5's finite-candidate enumeration.

Everything else (the coupled two-parameter GCH($j$,cap,$b$;$S$) induction
template, the "do not re-attempt the refuted single-parameter induction"
warning, the base-case-matches-Lemma-2 sanity check) is sound guidance,
consistent with the certified record and this round's own
cheap-kill-first discipline.

Also note (housekeeping, not fatal): the approach file's own body text
(the "Exact achievability" theorem, lines ~90–127 and its "Promotable
lemmas (round 19)" restatement) still literally states "for every
$k\ge2$," which the round-19 proof-reviewer found **false** and
certified only in corrected split-by-$k$ form
(`lemmas/gch-achievability-witness-k-geq-3.md`, $k\ge2$ via a
*different* certified witness $\{2,b,b\}$). The approach file itself was
never edited in place to reflect the correction. This round's outline
correctly cites the corrected combined fact ("Achievability is fully
closed for all k>=2 (certified)") and doesn't re-import the bug, but the
builder should be told explicitly to cite the certified lemma cache, not
re-derive or re-cite the stale "for every $k\ge2$" sentence still sitting
in the approach file body.

## `global-lp-vertex-sufficiency`: CHANGES REQUESTED

**Target (a)**: write up the exact vertex-enumeration closure of the 6
remaining $n=2$ two-cut shapes — this is essentially bookkeeping on
already-certified machinery (Global Vertex Lemma), low risk, approve as
is.

**Target (b)**: the untested $n=3$ 2-cut/6-fragment construction
(split $p_1$ into 3 fragments via 2 cuts, tie one fragment to $p_2$ and
one to $p_3$, leaving a free fragment $r=p_1-p_2-p_3$, untouched $p_4$).

**Real feasibility problem found by direct computation, not caught by
the outline:** this construction requires $r=p_1-p_2-p_3>0$, i.e.
$p_1>p_2+p_3$. I checked this against the actual balanced region
$B(3)$ ($p_1<1/2$, every consecutive gap $>\gamma(3)=1/15$) with an
explicit near-uniform (small-gap) point:
$p=(0.365,0.2884,0.2117,0.135)$ (gaps $\approx0.0767>1/15$ each,
$p_1<1/2$, sum $=1$) — a completely generic, non-edge point of $B(3)$.
Here $p_2+p_3=0.5001>p_1=0.365$, so $r<0$: **the construction is
infeasible**, not just on a "thin sliver" the way the previously-refuted
single-piece-split witness was, but across what looks like a large
(possibly majority) portion of $B(3)$ — specifically the near-uniform
sub-region that has historically been the *hardest* part of the balanced
region across many prior rounds. I also confirmed $p_1>p_2+p_3$ **is**
achievable in $B(3)$ but only in a "front-loaded" corner (large first
gap, small later gaps, e.g. $p=(0.48,0.23,0.08,0.01)$ gives $r=0.17>0$)
— the opposite corner from where the difficulty has concentrated.

By contrast, pairing the two tied fragments to $p_3,p_4$ instead of
$p_2,p_3$ (mentioned only as a *fallback* "patch witness" in the
outline's step 5) is feasible at exactly the near-uniform point above
($p_3+p_4=0.3467<p_1=0.365$, $r=0.0183>0$).

**What to change:** the outline's mandatory cheap-kill (step 2) will
almost certainly reveal near-total infeasibility of the $p_2,p_3$-tied
pairing across the hard (near-uniform) sub-region — this is not a
surprise the builder needs to discover from scratch; flag it now so the
round isn't spent re-deriving what a 2-minute hand computation already
shows. Recommend either (i) swap the primary construction to the
$p_3,p_4$-tied pairing (checked feasible at the near-uniform test point
above — test its feasibility and worst-case value first, before the
$p_2,p_3$ version), or (ii) keep both as literally two feasibility-gated
branches and let the cheap-kill itself decide which region each pairing
covers, then look for a natural case split (e.g. by sign of
$p_1-p_2-p_3$) from the start rather than treating $p_2,p_3$-tied as the
sole primary attempt. Either way, do not spend proof effort on the
$p_2,p_3$-tied shape's value *before* confirming on which sub-region of
$B(3)$ it is even feasible.

## Diversity / plateau check

No shared-gap plateau this round: `self-similar-induction-on-n`'s open
item is a finite integer-vector combinatorial lower bound inside a fixed
$\Gamma$-recursion; `global-lp-vertex-sufficiency`'s open item is an
$n=3$ construction/feasibility question on a different polytope. These
remain two structurally distinct obstructions (consistent with round
13–19's repeated plateau-checks), so no fresh top-level framing is
required this round. `lp-duality-split-polytope` stays dormant
(no revival lead since round 18's dead-end); other approaches
(`greedy-reduction-geometric`, `universal-halving-adversary`,
`discharging-neighbor-transfer`, `layer-cake-parity-reframing`,
`dyadic-potential-invariant`, `structured-randomization-upper-bound`,
`reciprocal-potential-induction-on-n`) remain correctly deprioritized/
dead/retired, no reason to revive any this round.

## Ranking

Cleared staleness on both build-set approaches by anchoring against the
population (`update_ranking` already called): treated
`self-similar-induction-on-n` vs `global-lp-vertex-sufficiency` as a draw
(both made genuine certified progress in round 19, comparably far from
closing their respective gaps), and both as beating the dormant
`dead-end`-outcome `lp-duality-split-polytope`. No new slugs to register
or copy this round.

## Build set

Both outlines are technically sound in direction and both have a real,
previously-unflagged load-bearing gap that must be addressed as part of
this round's build (not treated as a rubber-stamped continuation):
`self-similar-induction-on-n` needs the multi-gap same-parity case
covered before trusting its finite reduction; `global-lp-vertex-
sufficiency` needs the $p_2,p_3$-tied construction's feasibility region
checked (and likely the $p_3,p_4$-tied pairing promoted to primary)
before investing in its value computation. Both are worth building this
round with these corrections passed along.

build set: self-similar-induction-on-n, global-lp-vertex-sufficiency
