# Outline review — round 16 (imo-2026-03)

Reviewed the outliner's 5-approach field against `current.md`, the live
approach files, `lemmas/`, and all three round-16 explorer reports
(`math-explorer-window.md`, `math-explorer-discharging.md`,
`math-explorer-fresh.md`).

## 1. self-similar-induction-on-n — revise — **APPROVE**

Target: GT(m), m>=4, sub-case (i), now narrowed (round 15) to the width-1
window a_1 in (2^(k-1), 2^(k-1)+1).

The outline's diagnosis matches `math-explorer-window.md` exactly and
line-by-line: the round-15 proof's Step 3 reduces (via Monotonicity
Reduction) to an abstract small-boundary target sum(D)=2^k, but the
explorer found this abstract excess-relaxed statement is **false** for
e>=1 (exact counterexample at k=3: margin -393/800) while the *actually
reachable* embedded instance (sum(D) locked at 2^m throughout a q=0
chain, so R=D\{a_1} really has sum(R)=2^m-a_1, not 2^k-a_1) shows robust
positive margins (~1.5-7.8 growing with m, e=1,2,3, thousands of trials,
zero violations). This is a genuine "wrong reduction, not wrong target"
diagnosis (Rule 94-style), not a hand-wave — the outline correctly
instructs the builder to re-derive Step 3 tracking the real forced value
sum(R)=2^m-a_1, not shrink to the small boundary.

Checked the algebra of the reciprocal identity used elsewhere is unrelated
here — this is a separate lower-bound-direction gap. The proposed
"Large-sum slack lemma" is explicitly and correctly labeled *unproved*
(not yet a lemma), with the open gap honestly stated (Step 2 unclosed) and
the case coverage (e=1,2,...) explicitly flagged as needing either
per-e proof or a uniform-in-e argument via the noted O(log m) feasibility
bound. No circularity: this is a genuinely different statement from the
already-refuted abstract version, targeting the forced-large-sum regime
only. Watch-out section correctly forbids re-attempting the disproven
general form. Step 5 (secondary, absorbing discharging's output) is
appropriately marked optional/unexplored, not load-bearing.

No issues. Sound skeleton, correctly scoped, whole-problem target
(lower-bound direction) preserved.

## 2. discharging-neighbor-transfer — revise (final build, then retire) — **APPROVE**

The outline's plan (relabel the Single-Cut Rank-Shift Identity as AltSum,
state the OddSum corollary via the certified Lemma AS with the 1/2
factor, certify, then retire) is fully pre-validated by
`math-explorer-discharging.md`'s own Tasks 1-4: the corrected identity
holds exactly to 60,000+ trials (30k generic + 10k larger-N + 20k
tie-heavy), and the affine-rescaling argument (OddSum=(sum+AltSum)/2,
sum fixed at 1) is checked directly and shown to preserve every
boundedness/unboundedness property of the connecting-step terms — so
"no independent leverage on either open gap" is now a confirmed finding
(this round), not merely round 15's suspicion. This is a legitimate,
low-risk, cheap terminal task: certify a reusable general-purpose lemma
(a genuine strict generalization of the existing insertion-only
identities — arbitrary split of an existing element, not just inserting
new mass) and correctly stand the approach down as an independent line.
No fatal flaw, nothing hidden — the outline is honest that "open gaps:
none mathematically... this is a closing round."

## 3. reciprocal-potential-induction-on-n — new — **APPROVE**

Genuinely new top-level framing for the upper-bound direction: induction
on n at the value-function level via the reciprocal/renewal recursion
1/c(n) = 1/c(n-1) + 2^{-n}, c(0)=1, structurally disjoint from every live
approach's per-n vertex/tie-topology/Σ-shape classification machinery.
Independently re-verified the closed-form identity by hand:
1/c(n) = 2 - 2^{-n} (from c(n)=2^n/(2^{n+1}-1)), and
1/c(n-1) + 2^{-n} = (2 - 2^{1-n}) + 2^{-n} = 2 - 2^{-n}. Matches exactly —
trivial algebra, correctly not oversold as more than that.

Critically, the outline is disciplined about what's actually established:
the recursion is proved only for the *supremum* c(n), not for V(p)
pointwise, and the outline makes the mandatory cheap-kill (test
1/V(p) >= 1/V(p') + 2^{-n} at the already-catalogued hard n=3,4 points
under >=2 candidate reduction maps) the literal first step before any
proof investment — correctly following the repo's "always stress-test
before building" rule, and correctly requiring two reduction maps be
tried (not one) before concluding the framing dead, learning from this
round's own GT(m) lesson that a wrong reduction can masquerade as a false
target. This is a whole-problem attempt (closes the Existence Theorem's
entire residual at once if it works), not a fragment. Registered as new.

## 4. global-lp-vertex-sufficiency — advance — **APPROVE (light content, correctly scoped)**

Round 15 closed off the last mechanical certificate route (uniform
convexity/concavity, confirmed dead by an exact 4-piece counterexample).
This round's outline is explicitly diagnostic/search-stage — it proposes
two named routes (Zero-Removal-style structural-degeneracy argument on
branch-comparison-boundary points; naming a genuinely new non-constructive
mechanism) plus a narrower n=3,4 classification task to determine which
candidate family (branch-boundary vs within-branch-tie) is actually
realized at the hard points. No lemma is claimed this round (correctly:
"Key lemmas: none yet proposed"). The watch-out list correctly bans
re-attempting all 4 already-refuted bounded tie-topology families and the
dead convexity certificate. This is thin on content but honestly scoped
as diagnostic, not a doomed technique — approve, but flag that if this
produces no new mechanism again next round, it is a 2nd round of
diagnosis-without-lemma on the same gap and should be watched for
plateau.

## 5. lp-duality-split-polytope — advance (light) — **APPROVE**

Correctly scoped as a cheap cross-check, not a new theorem attempt: check
whether the certified Twin-Anchor / Perfect-Tie-Family characterization at
e_0 corresponds to global-lp-vertex-sufficiency's open within-branch-tie
candidate family. Low risk, potentially useful (a genuine cross-approach
data point per the standing "cross-substitute before assuming
independence" rule), explicitly told not to duplicate or force a result.
No fatal issue.

## Diversity check

The field covers both directions of the problem: lower bound (GT(m) width-1
window: self-similar, and discharging in its terminal round, confirmed to
share the identical obstruction — correctly not double-counted as
independent progress) and upper bound (Existence Theorem Σ-shape residual:
global-lp-vertex-sufficiency continuing its vertex/tie framing,
lp-duality-split-polytope's light cross-check, and — genuinely new —
reciprocal-potential-induction-on-n's renewal-equation framing, which
explicitly avoids the vertex/tie/polytope family that 3 of the 5 live
approaches now share). This is real diversity, not a relabeling: no
RETHINK needed, no shared-gap plateau requiring a break this round (the
plateau-break slot is already filled by the new reciprocal approach).

## Ranking

Applied `update_ranking` with 10 comparisons anchoring the cold-start
newcomer (`reciprocal-potential-induction-on-n`) against 3 established,
already-active approaches (loses to self-similar-induction-on-n,
lp-duality-split-polytope, global-lp-vertex-sufficiency — it has no proof
content yet, only an unverified pointwise conjecture) while drawing with
`discharging-neighbor-transfer` (both are exploratory/terminal-scoped this
round). `discharging-neighbor-transfer` loses to the three approaches with
more substantive standing content this round (self-similar's window
narrowing, lp-duality's certified Twin-Anchor extension,
global-lp-vertex's certified Zero-Removal Lemma + 4th refuted topology),
consistent with its own correct self-diagnosis of "no independent
leverage." `self-similar-induction-on-n`, `global-lp-vertex-sufficiency`,
and `lp-duality-split-polytope` are pairwise close (draws / narrow wins)
reflecting genuinely comparable, complementary progress this round.
Post-update Elo: lp-duality-split-polytope 1625, self-similar-induction-on-n
1579, global-lp-vertex-sufficiency 1539, reciprocal-potential-induction-on-n
1459, discharging-neighbor-transfer 1440. All `stale` flags cleared for the
5 touched approaches.

## Build set

All 5 are sound (no RETHINK); none doomed, none a repeated dead end, no
single-gap-trap fragmentation. Dispatch one builder per slug:

build set: self-similar-induction-on-n, discharging-neighbor-transfer, reciprocal-potential-induction-on-n, global-lp-vertex-sufficiency, lp-duality-split-polytope
