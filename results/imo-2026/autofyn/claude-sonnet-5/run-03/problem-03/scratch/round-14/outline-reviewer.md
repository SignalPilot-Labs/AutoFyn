# Outline review — round 14 (imo-2026-03)

## self-similar-induction-on-n (revise) — CHANGES REQUESTED (build, but fix a false numeric claim first)

The revised target (variable-$V$ generalization of the Unified Threshold-Pair-Peeling
Lemma, closing sub-cases (i) $q=1,e\ge1$ and (ii) small-sum mirror as one corollary) is
the right next step and is not a doomed leap:

- The claim "$q\ge2$ closes for any target $V\le2^k$, unconditionally, with no change to
  the proof" is **independently re-verified and correct**: the certified proof's bound
  ($\mathrm{OddSum}(M)>2^k$ via $\sigma_q+2^{k-1}(q/2)$, or via $\sigma_q$ alone for odd
  $q$) never uses $V=2^k$ specifically, and $2^k\ge V$ trivially propagates the strict
  inequality to any smaller target. No new work is owed there — correctly scoped.
- The filler-insertion argument for the not-full-count instance of (ii) is not
  circular: it depends on the boundary case at the *same* $m$ (established for
  $m\le3$ now, and prospectively for general $m$ once step 5 is closed independently of
  step 3) — step 5 does not depend on step 3's output, so the dependency order is
  sound, not a hidden circularity.
- The elementary corollary $0\le\mathrm{AltSum}(N)\le\max(N)$ is a genuine one-line
  induction from the certified Peeling identity; fine to certify as stated.

**Found and independently re-verified a real numeric error underlying this round's
central motivating claim** (mandatory-numerical-stress-test rule): the explorer's
reported "full-count ($|D|=m+1$) instance of (ii) has genuine, non-tight slack
(margins $\approx1.04,2.58,5.66$ at $m=3,4,5$, at $\mathrm{sum}(D)/2^m=0.99$)" **does
not reproduce**. I independently reimplemented the exact object (own Nelder–Mead
optimizer, multiple restarts, cross-checked against 4000-trial exact-`Fraction` random
search, both from scratch) and find the worst-case margin at $\mathrm{sum}(D)/2^m=0.99$
is $\approx0$ (numerically $-10^{-14}$, i.e. tight) for $m=3,4,5$ — **not** $1$–$5.7$.
Sweeping $\mathrm{sum}(D)/2^m\in\{0.1,\dots,0.99\}$ at $m=4$ confirms the margin
decreases smoothly from $\approx9.2$ down through $0$ exactly as $\mathrm{sum}(D)/2^m$
approaches $0.95$–$0.99$ (the minimizer found is essentially $D\approx\Gamma_{m-1}$
plus one small extra element, i.e. the classic near-duplicate-of-$\Gamma$ tight
configuration) — the full-count instance is **just as knife-edge as the not-full-count
case**, not a distinct "genuine slack" regime. (My first attempt at this check also
got a spurious negative margin from an off-by-one $\Gamma$-index bug of my own,
caught and fixed by cross-referencing the certified index convention
$\Gamma_{m-1}:=\{2^{m-1},\dots,2^0\}$, $m$ elements — worth flagging in case the
explorer's script has the same class of bug.)

This does **not** invalidate the plan — the variable-$V$ generalization of Result 2's
$q=0,1$ branches is still the correct, only concrete route to close both sub-cases, and
it must work at the tight boundary regardless. What must change: **drop the "full-count
has real slack, supports an easier direct argument" framing** from the outline before
the builder spends effort assuming a shortcut that isn't there — the full-count
sub-sub-case is exactly as hard as the general boundary case, so budget the builder's
effort accordingly (expect to need the `aimo-0377`-style companion-bound fallback, not
treat it as a fallback-of-last-resort for a supposedly-easy case). Ask the builder to
re-run its own numeric check with the corrected framing before writing up "genuine
slack" as evidence for anything.

## global-lp-vertex-sufficiency (revise) — APPROVE

The reframe is well-justified, not an unjustified leap. Read the certified
Mass-Constraint Theorem directly (`lemmas/rank-pinning-lemma-and-mass-constraint-
theorem.md`): its hypothesis is explicitly "tie each split fragment to the value of a
whole untouched piece," and its own file states in "What this does and does not
resolve" that fragment-vs-fragment tying is untouched. The revision targets exactly
that untouched mechanism — the outliner's claim that the growing-$s^*$ finding rules
out only a *fixed* $s_0$, not an $n$-dependent construction, is correct on its face:
$s^*\sim n/2$ is comfortably inside the $n$-cut budget, so this is a real re-scoping,
not wishful reframing of a refuted result. The mandatory cheap-kill (step 2, testing
the chain-tie construction numerically before any proof effort) is correctly placed
first and is the load-bearing gate — good process. No issue found; proceed to build.

## lp-duality-split-polytope (advance) — APPROVE

Genuinely complementary exact-arithmetic angle (general nonzero-residual
fragment-vs-fragment family at $e_0$), disjoint technique from the LP-vertex builder's
numeric search, using its own certified toolkit (Integer-AltSum Lower Bound Lemma).
Reasonable stepping stone; no soundness issue.

## greedy-reduction-geometric — correctly held out of the build set

Verified via `current.md`'s round-11 record and `lemmas/wlog-b2-and-case-b-topOnly-
equivalence.md`-adjacent history: Theorem N gives a literal (reviewer-independently-
checked, symbol-for-symbol) equivalence between this approach's residual gap and
self-similar-induction-on-n's GT($m$), $m\ge4$ gap. Dispatching a second builder on the
identical open sub-case this round would be duplicated effort, not genuine diversity —
correctly excluded. Re-dispatch only if self-similar-induction-on-n's builder stalls and
a genuinely independent greedy-side angle is worth trying.

## Decision not to open a discharging/charge-conservation approach — sound, with one caveat

The reasoning (both remaining gaps saw concrete new mechanisms this round, not just
narrower framings of the same wall) is a fair read of the LP-vertex side (the
mis-scoped-target correction is real and independently checked above). It is *weaker*
than stated on the GT($m$) side, since the "full-count has real slack" finding —
one of the two cited pieces of evidence for "not part of the unbounded case-growth
pattern" — is independently found to be a numeric error (see above): the full-count
case is tight, not slack. The architecture simplification (one variable-$V$
generalization instead of two separate sub-cases) still stands as genuine progress
independent of the slack claim, so the overall call to hold discharging in reserve
this round remains reasonable, but the bar for opening it next round should be treated
as effectively "one gap (LP-vertex) has a corrected genuine new mechanism; the other
(GT(m)) is down to an architecture simplification with a fallback technique, not a
demonstrated easier sub-case" — closer to a 3rd-round plateau than the outline's
framing suggests. If the variable-$V$ generalization (including the full-count instance,
now correctly understood as equally hard) stalls again next round, open the
discharging/charge-conservation approach then, no further deferral.

## Ranking

Applied via `update_ranking` (Elo updates recorded): `greedy-reduction-geometric`
(1677, top — its own gap fully closed, standing by) > `lp-duality-split-polytope`
(1594) ≈ `global-lp-vertex-sufficiency` (1535, draw vs. lp-duality and vs.
self-similar) > `self-similar-induction-on-n` (1513, real certified progress but this
round's numeric motivation was found flawed) > `structured-randomization-upper-bound`
(1485, dead-end, correctly recorded) > `universal-halving-adversary` (1483, stale
since round 8) > `layer-cake-parity-reframing` (1387, stalled since round 4) >
`dyadic-potential-invariant` (1327, dead-end).

## Build set

Dispatch builders for the three approaches in the outliner's build set, with the
correction above passed to `self-similar-induction-on-n`'s builder (drop the "full-count
has genuine slack" framing; treat it as equally tight, budget for the companion-bound
fallback from the start rather than as a last resort).

build set: self-similar-induction-on-n, global-lp-vertex-sufficiency, lp-duality-split-polytope
