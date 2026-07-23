# Outline review — round 7 (reviewing round 6's proof-outliner output, which was orphaned by a hung outline-reviewer)

Scope note: per dispatch, I am reviewing `/tmp/round-6/proof-outliner.md`'s three revised/advanced
skeletons against the round-6 explorer reports and the actual (already-edited) approach files.
The explorers and outliner are NOT re-run. This is exactly the review/ranking/build-set step that
round 6 failed to complete.

## 1. `dyadic-cascade-induction` — new §5.4 ("all-cycles" D_m-only resolution)

**Verdict: APPROVE**

Read the actual skeleton at `results/imo-2026-03/approaches/dyadic-cascade-induction.md` lines
1953-2041.

- **Step 1 (Guaranteed-Untouched-Original Lemma).** Pigeonhole: each of XY's ≤m cuts traces to a
  unique root original of `D_m` via cut-forest parentage, contributing at most 1 new root per cut,
  so ≤m distinct originals are ever touched; since `D_m` has `k=m+1>m` original pieces, ≥1 is
  always completely untouched. This is airtight — logically checked by hand, no gap. It is a
  genuinely NEW resource not previously stated anywhere in `dm-completeness-partial.md` or the
  approach files (confirmed by grep — the phrase "guaranteed untouched" and this exact pigeonhole
  count do not appear before this round's explorer report).
- **Step 2 (Base-case Cycle-Breaking Lemma, length-2).** I independently re-derived this with a
  fresh script (`/tmp/round-7/verify_step2.py`), NOT reusing the explorer's own code, on `D_2=(4,2,1)`,
  `D_3=(8,4,2,1)`, and `D_4=(16,8,4,2,1)` — every pair `(a_i,a_j)` tied at `t`, checked the
  resulting piecewise-linear `e(t)` (via Lemma P collapsing the duplicate `t`, then ordinary
  alternating sum) against ALL of its own breakpoints (ties to any untouched rest-piece) and domain
  boundaries. In every one of the 3+6+10=19 pair-instances tested, the minimum over `t` occurred
  exactly at a breakpoint (tie to an untouched original) or a domain boundary (`t=0` or a piece
  hitting 0) — several cases were flat/degenerate segments (slope 0), which trivially still contain
  their own boundary/breakpoints as minimizers, consistent with the claim. This is in fact close to
  a tautology given piecewise-linearity is already established (min of a piecewise-linear function
  on a closed interval is always at a kink or an endpoint) — so Step 2's real content is just
  establishing piecewise-linearity via the already-certified Vertex Lemma + Lemma P, which is sound.
  No counterexample found; claim independently corroborated.
- **Step 3 (Cycle-Shortening, length≥3) is explicitly left OPEN**, not disguised as solved. The
  outline correctly flags the open degrees-of-freedom question ("do the `L` tying equations collapse
  to fewer than `L` free parameters — check, don't assume") and explicitly distinguishes this
  "escape to guaranteed-untouched-piece" move from the already-refuted "re-pair a fixed support"
  dead end from `potential-weighting-upper-bound` §7.3. I checked this distinction myself: the dead
  end there specifically froze the *complement* of two re-paired arcs; here the untouched piece is
  a genuinely new target never available to that argument (by Step 1's guarantee it always exists
  and was never a candidate participant in the frozen dead-end argument, which only ever compared
  re-pairings *within* an already-cut support). The distinction is real, not a rebrand.

No overclaim: the file explicitly keeps this section's status as an open skeleton (Step 3 marked
OPEN in both the "Key lemmas" and "Open gaps" blocks), does not claim §5.4 is complete anywhere I
could find (grepped for "certified" near line 1953-2041 — none found). This is a genuinely new
mechanism (pigeonhole + joint extreme-value + crux-adapted local re-target), distinct from
`concavity-minimax-duality`'s `dm-completeness-partial.md` (topological/DAG peeling on the general
tie-dependency graph) — a second, independent, complementary attack on the same underlying gap,
not a duplicate.

## 2. `potential-weighting-upper-bound` — new §8 (layer-cake + non-crossing DP)

**Verdict: APPROVE, with an explicit gap for the builder to attack (Step 3 outside-crossing-arc case)**

Read `results/imo-2026-03/approaches/potential-weighting-upper-bound.md` lines 942-1042.

- **Step 1 (layer-cake identity)** is elementary and correct: `e = ∫ 1[N(t) odd] dt` reproduces the
  alternating sum by construction (each interval between consecutive sorted values contributes its
  length iff its rank is odd) — this is a standard, easy identity, no red flags.
- **Step 2 (NC(Y,b) via the classical non-crossing/Dyck-path DP recursion)** is well-defined: the
  "inside"/"outside" split at a matched pair `(1,j)` exactly encodes non-crossing-ness (an
  inside-outside match would satisfy `1<a<j<b`, precisely the crossing condition the file's own
  §7.3 definition uses) — I confirmed this correspondence explicitly, it is not asserted loosely.
- **Step 3 is the crux of my check, per the dispatch instruction to verify this ISN'T the
  frozen-support dead end restated.** I traced the counterexample `Y=(43,33,20,16,11,8,2)`, `b=2`
  from the explorer's report by hand: witness 2 (`kept={33,8,2}`, matched `(43,11)→32,(20,16)→4`)
  IS expressible in the DP (inside={33,20,16} gets budget 1 via the (20,16) match, outside={8,2}
  gets budget 0, kept). Witness 1 (`kept={33,16,2}`, matched `(43,11)→32,(20,8)→12`) is NOT
  expressible in the split-at-j=4 DP, because the `(20,8)` match pairs an inside element (index 2)
  with an outside element (index 5) — exactly a crossing arc relative to `(0,4)`. This is precisely
  the scenario Step 3 flags as unproved: "what is NOT yet proved: that this residual replacement,
  when y_1 was matched to y_j in σ* with OTHER selections crossing that arc, can be carried out
  without those other crossing arcs increasing the value." **This is genuinely the induction
  replacing the ENTIRE residual selection** (via the strong IH on `Y\{y_1}` or the inside/outside
  split), not a frozen-support arc-swap — the move class differs qualitatively from the dead
  local-uncrossing-exchange (which held "the rest" literally fixed and compared only 2-3
  alternative pairings on one frozen 4-point support). I confirm this is NOT a relabeled dead end.
  However, I want to flag precisely for the builder: the induction as sketched has a real,
  currently-unaddressed subtlety even beyond what "Step 3" states — when the IH is invoked on the
  residual `Y\{y_1,y_j}`, it must produce a non-crossing selection **with respect to the full index
  order of `Y`** (i.e., respecting the `(1,j)` split boundary), not merely "non-crossing among
  itself" as an abstract (p-2)-element list. The IH's own inductive statement (`OPT=NC` for smaller
  `p`) is naturally phrased for a bare list without an externally imposed split, so applying it to
  "inside" and "outside" *separately* (rather than to the combined residual as one list) is the
  step that actually needs justifying — and this is exactly why an inside-outside crossing arc
  (like `(20,8)` in witness 1) is troublesome: the IH, invoked separately on inside and outside,
  cannot by itself rule out that some optimal configuration NEEDS an inside-outside link. The file's
  own Step 3 language gestures at this ("the interaction between a matched arc (1,j) and crossing
  arcs from outside (1,j)") but does not make explicit that the induction hypothesis must be applied
  to two SEPARATE sub-lists (not one combined list) for the recursion to even be well-formed, and
  that this separate-application step is unjustified. I recommend the builder state this precisely
  as the formal induction gap rather than leaving it as prose.

No overclaim found: Step 3 is explicitly marked OPEN, and the "Key lemmas" block honestly says
"whether it closes is the precise open question." The "Watch out for" section correctly instructs
rejecting any write-up that reverts to one-arc-at-a-time perturbation.

## 3. `concavity-minimax-duality` — advance (Generalized Forced-Value check)

**Verdict: APPROVE**

This is a narrow, well-scoped, decisive-either-way task: extend the certified Cascade
Reachability + Forced-Value machinery from `g(1)=1,g(2)=2` to `g(j)=j` for larger `j`. I
independently ran the argument one step further by hand/script to sanity-check feasibility before
approving (not reusing any outline code):

- From `D_2=(4,2,1)` (reachable from `D_m` for `m≥2`), applying `M(4,1)` gives `{3,2}`, reachable
  within `m-1` ops. Hypothesis `e_g({3,2})=g(3)-g(2)≥1` plus Lemma B (`g(2)=2`) forces `g(3)≥3`;
  1-Lipschitz plus `g(2)=2` forces `g(3)≤3`. **Hence `g(3)=3` is forced** — the pattern extends
  cleanly one more step past Lemmas A/B, exactly the kind of result outcome (a)/(b) is asking the
  builder to chase systematically.
- Testing `g(4)`: the reachable witness `D_2=(4,2,1)` itself gives only `g(4)-g(2)+g(1)≥1`, i.e.
  `g(4)≥2`, while 1-Lipschitz from `g(3)=3` gives `g(4)≤4` — **not pinned to a single value**,
  consistent with the file's own round-5 "informal" observation that slack appears around `g(4)`.
  This independently corroborates that outcome (b) (forcing stops at a specific `j_0`, here
  plausibly `j_0=4`) is the likely real answer, giving the builder a concrete, already-partially-
  verified target rather than an unexplored guess.

This task is low-risk (reuses certified lemmas, no new machinery, decisive), correctly declines to
invent a new scalar candidate this round (avoiding a third guess-and-refute cycle), and is
distinct in mechanism from both siblings (certificate/duality framing vs. physical case-split vs.
non-crossing DP) — good diversity, not a re-hash.

## Cross-cutting checks

- **Whole-attempt vs. fragment:** `dyadic-cascade-induction` targets the full theorem (both
  directions, general `n`). `potential-weighting-upper-bound` and `concavity-minimax-duality` each
  own one direction (upper / lower respectively) via genuinely different techniques — this is the
  same upper/lower split flagged as an acceptable (not ideal) pattern in rounds 4-5 (memory rule,
  round 5 entry); no NEW slug joined this split this round, and no import pointer to an unproven
  sibling result was introduced this round (each of the three sections stands on its own certified
  lemmas or clearly-marked-open work). Continuing to treat as acceptable, watched.
- **Shared-gap / single-framing risk:** the three approaches attack three distinct mechanisms
  (pigeonhole+extreme-value for all-cycles; non-crossing DP for Case ii; Lipschitz certificate for
  the lower bound) — genuinely diversified, not the same wall from three angles. `dyadic-cascade-
  induction` and `concavity-minimax-duality` do both ultimately serve the lower-bound direction, but
  via fully independent techniques (as in round 4's two independent D/M-completeness closures) —
  this is healthy redundancy, not a shared-gap trap.
- **Dead-end reuse check:** grepped all three files for the three known-dead mechanisms (local
  pairwise uncrossing-exchange with frozen rest; bounded/fixed-depth lookahead; global concavity of
  `g`) — none are silently reintroduced. `potential-weighting-upper-bound` explicitly restates why
  its old mechanism is dead before presenting the new one (good practice). `concavity-minimax-
  duality`'s own history of two dead scalar-candidate attempts is correctly not repeated (this
  round explicitly declines a third guess).
- **Dangling references:** every `lemmas/*.md` filename referenced across all three approach files
  exists on disk (cross-checked via `grep -oh 'lemmas/[a-zA-Z0-9_.-]*\.md'` against `ls lemmas/`) —
  no stale/leftover filenames found this round.
- **Crux usage:** `aimo-0003` is cited only as an adapted proof *shape* ("reduce invariance-under-
  all-orderings to a single adjacent transposition") for the still-open Step 3, not as a citation
  substituting for an actual proof — correctly scoped per CLAUDE.md's crux-corpus rule.
- **No hangs risk this round:** none of the three skeletons requires unbounded search; the explorer
  reports already ran their exhaustive checks up to `p≈6-7` and explicitly flagged not to push
  further. My own verification scripts this round were bounded (`p≤5` piecewise-linear checks,
  closed-form Lipschitz-bound arithmetic) — no long-running or exponential scripts were invoked.

## Ranking

All three approaches made real, well-scoped progress last round (certified lemmas: Superincreasing
No-Early-Zero, Slack Collapse, Lipschitz-certificate-and-forced-values) and enter this round with
sound, non-overclaiming, genuinely novel-mechanism skeletons for their next gap. `dyadic-cascade-
induction` remains the most advanced (whole-theorem scope, most certified content, and this round's
§5.4 Steps 1-2 are close to fully rigorous already — likely to close further this round).
`potential-weighting-upper-bound`'s §8 is a substantive upgrade from a stuck local-exchange dead end
to a well-posed (if still incomplete) global DP induction. `concavity-minimax-duality`'s task is the
narrowest/cheapest but still genuinely decisive either way (a clean negative result or a structural
fact), and it is the lowest-Elo of the three (historically the most exploratory), so I rank it
third but do not drop it.

Comparisons submitted to `update_ranking` (anchoring the newly-advanced work against each other,
using round 5's ranking as the base since all three are established, not cold-start newcomers):
- dyadic-cascade-induction beats potential-weighting-upper-bound (more advanced overall scope +
  its §5.4 Steps 1-2 are independently verified essentially complete this round, vs.
  potential-weighting-upper-bound's §8 Step 3 still has an unaddressed formal subtlety I found).
- dyadic-cascade-induction beats concavity-minimax-duality (broader scope, more total certified
  content).
- potential-weighting-upper-bound beats concavity-minimax-duality (its new mechanism, while
  incomplete, replaces a fully-dead technique with a substantive DP structure closer to a working
  proof than concavity-minimax-duality's still-exploratory certificate search).

No RETHINK verdicts this round — all three skeletons are sound and should be built.

## Build set

build set: dyadic-cascade-induction, potential-weighting-upper-bound, concavity-minimax-duality
