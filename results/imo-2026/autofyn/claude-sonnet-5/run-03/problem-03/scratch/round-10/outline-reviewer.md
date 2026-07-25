# Outline review — imo-2026-03, round 10

Reviewed `/tmp/round-10/proof-outliner.md` against `results/imo-2026-03/current.md`,
the four revised approach files, `.ranking.json`, and the three explorer reports.
Independent sanity checks were run (Python/sympy) rather than just reading the
outline's claims at face value.

## global-lp-vertex-sufficiency — CHANGES REQUESTED (advance)

The round-9 gap (candidate functional list $L$ omits $p_k\ge0$, making the cut
region unbounded and admitting $p_k<0$) is correctly diagnosed and the fix
("add $p_k$ to $L$, redo vertex extraction; Lemmas 4.1/4.2 unchanged since they
only use finiteness/affineness of $L$") is the right, narrow fix — Lemma 4.1's
proof only uses that each $\ell\in L$ is affine and finite-in-number, so adding
one more functional to $L$ leaves its proof mechanism untouched. Good.

I independently re-derived the outline's headline numeric claim (region-only
vertex count = 2 genuine + 2(n-1) degenerate for $n\ge4$, with $n=2,3$ as
boundary exceptions) from scratch, by brute-force intersecting all
$(n)$-subsets of the $n+2$ functionals $\{p_1-\tfrac12,\ p_i-p_{i+1}-\gamma(n)\
(i=1..n),\ p_k\}$ with the simplex hyperplane and filtering for feasibility
(fresh sympy script, independent of the builder's/explorer's):

```
n=2: total=3  (matches the outline's stated boundary exception)
n=3: total=5  (matches the outline's stated boundary exception)
n=4: total=8  = 2*4,   genuine=2, degen=6=2*3   ✓ matches "2 + 2(n-1)"
n=5: total=10 = 2*5,   genuine=2, degen=8=2*4   ✓ matches "2 + 2(n-1)"
```

This is a real, independently-verified confirmation of step 2's claimed
enumeration — the outline is not overclaiming here, and correctly flags
$n=2,3$ as needing separate handling (which my check also confirms diverge
from the $2n$ pattern). Step 3 (continuity reduction for the $p_k=0$
degenerate vertices) and step 4 (exact-arithmetic closure of the 2 genuine
vertices, currently only numeric $V\approx1/2$) are honestly still open —
the outline does not claim them closed. Step 5's honesty about the
untouched $|\Sigma(n,k)|$-unboundedness obstruction is correct and
important — this is the harder, unaddressed part; the outline does not
bury it. **No fatal flaw. Approve to build**, with the reminder (already
in the outline's "watch out for") that step 4's numeric $V\approx1/2$ must
not be treated as proved without the exact derivation.

## greedy-reduction-geometric — CHANGES REQUESTED (advance)

The new asymmetric decomposition (step 2: bank $\mathrm{sum}(B'')$ for free
via Theorem 7a one level down, applied to $B''\cup S'''$) is a legitimate
reuse of an already-certified theorem at a smaller parameter — Theorem 7a's
hypothesis (Dominance-Chain structure) is exactly what $B''$ has by
construction one level down, so this is not a fresh unverified leap.
Confirmed Theorem 13 (General Insertion Monotonicity) is indeed certified
and already reused multiple times in this file's own text (grep confirms
its use in Lemma L's own proof and elsewhere), so step 4's reuse is sound
in principle.

The genuinely open piece — step 5's flagged additivity concern (OddSum is
not simply additive across an arbitrary split of the merged sorted
multiset) — is correctly identified as the crux difficulty, not glossed
over with "it follows." The outline explicitly names two fallback routes
(rank-band separation vs. Lemma S/Theorem 13 direct application) rather
than hand-waving a way through. This is exactly the kind of honest,
mechanism-stated lemma flagging the process wants. **No fatal flaw. Approve
to build.**

## self-similar-induction-on-n — CHANGES REQUESTED (revise)

Step 3(i)'s "new tiny piece below the current minimum changes at most one
rank" claim was checked directly: inserting a value smaller than every
existing element in a descending sort pushes it to the very last rank
without disturbing any other element's relative rank, so OddSum either
stays the same (new element lands at an even rank) or increases by exactly
that element's value (odd rank) — never decreases. This matches the
outline's stated mechanism exactly and is correctly attributed to the
certified rank-counting/Peeling-Lemma. Step 3(ii) (piece-cap-saturated
sub-case) is honestly flagged as the one genuinely open sub-case, not
silently assumed via Schur/majorization (which the file's own "watch out
for" correctly bars, since that mechanism is a certified dead end here).
Step 5's LP cross-connection to global-lp-vertex-sufficiency is correctly
labeled speculative/untested, not claimed as a working route. **No fatal
flaw. Approve to build.**

## lp-duality-split-polytope — CHANGES REQUESTED (advance)

Dual role is properly kept separate: (i) tool-supply to
global-lp-vertex-sufficiency step 4 (already-certified formulas, no new
proof) and (ii) its own remaining gap (idx=1 case of Multi-Piece
Necessity). The file's own "watch out for" explicitly warns builders not
to conflate the two, which is the right discipline given this file plays
two roles. Step 2 (excess-parametrized induction) and step 3 (m≥4
domination, fallback) are both correctly labeled unproved, with a stated
mechanism for each (bounded excess vs. consecutive-run merging argument)
rather than a bare "then it follows." Neither route is chosen as
mandatory; the outline explicitly says "pick whichever closes first,"
which is fine for an outline stage. **No fatal flaw. Approve to build.**

## universal-halving-adversary — correctly deprioritized

Not part of this round's outline; its last note (plateaued survivor-rate
finding, scope redirected to global-lp-vertex-sufficiency) still stands.
No new content to review this round; staying out of the build set is
correct — it would compete for builder time on a route already reported
as not shrinking toward a proof.

## Diversity check

The four approaches still cleanly split into two independent framings for
the two open directions (LB: self-similar-induction-on-n +
greedy-reduction-geometric, both peel/insertion-style but attacking
disjoint sub-cases — window vs. Level-Absorption — not the same wall; UB:
global-lp-vertex-sufficiency's LP/finite-cell route vs.
lp-duality-split-polytope's shadow-price/negative-construction route, a
genuinely different technique, not a variation of the same one). No
collapse to a single framing this round. layer-cake-parity-reframing
remains a third, distinct LB/parity framing not sampled this round — fine
to leave out given it has been stalled since round 4, but worth a look in
a future round if the top four plateau simultaneously.

## Ranking

Ran `update_ranking` anchoring this round's four candidates against each
other and against the deprioritized `universal-halving-adversary`
(comparisons based on: certified content this round — Lemma L, Theorem W,
the two AltSum/Bottom-Block-Doubling formulas — vs. `global-lp-vertex-
sufficiency`'s still-open found gap, and all four beating the plateaued
`universal-halving-adversary`). Resulting order (best first):
`greedy-reduction-geometric` (1630) > `lp-duality-split-polytope` (1589) >
`universal-halving-adversary` (1530) > `self-similar-induction-on-n`
(1525) > `global-lp-vertex-sufficiency` (1458). No new approaches to
register this round (all four are already-registered slugs being
revised/advanced); no branching requested by the outliner this round.

## Verdict

All four proposed approaches are technically sound at the outline level —
no wrong technique, no circular step, no unjustified leap, no repeat of a
recorded dead end (Schur/majorization and the abstract Split-Degradation
bound are both correctly avoided per their own "watch out for" sections).
Confirming the outliner's proposed build set unchanged.

build set: global-lp-vertex-sufficiency, greedy-reduction-geometric, self-similar-induction-on-n, lp-duality-split-polytope
