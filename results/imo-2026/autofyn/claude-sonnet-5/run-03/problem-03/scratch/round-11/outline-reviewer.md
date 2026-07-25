# Outline review — round 11, imo-2026-03

Checked `/tmp/round-11/proof-outliner.md` against the live approach files in
`results/imo-2026-03/approaches/`, `current.md`, and this round's three
explorer reports (`math-explorer-sigma-shape.md`, `math-explorer-trichotomy.md`,
`math-explorer-level-absorption.md`). All four outlined approaches target the
problem's actual claim end-to-end (upper- or lower-bound half of
`c(n)=2^n/(2^{n+1}-1)`), not a fragment — no single-gap-trap violation.
Diversity is healthy: four genuinely different framings remain live
(LP-vertex/finite-cell, self-similar strategy-stealing induction, greedy
peel-and-insert, LP-duality/split-polytope), each currently blocked on its
own distinct obstruction, not a shared wall.

## global-lp-vertex-sufficiency — APPROVE

Verified against the live file (`global-lp-vertex-sufficiency.md` lines
171–255): Section 1 item 1 literally reads "...a choice ... **across the
whole shape** (not per-piece — a single 'free' block is designated among
all ... blocks)", while the proof paragraph (lines 218–235) explicitly
establishes "free block, one per piece $i$ that is actually split." This is
a genuine internal contradiction between the stated lemma and its own proof
— the outliner's step 1 correction is real and load-bearing, not a nitpick.
Good catch by the explorer/outliner; a builder who trusted the stated
wording literally would undercount $\Sigma$.

Section 5's numeric $n=6$ finding (3-piece generalized-tie clearing $c(6)$
by $50\times$ the named-tools' margin) is accurately summarized, and is
honestly flagged in the file itself as numerical (Nelder–Mead), not exact.
The outline correctly treats it as evidence for Opening 1 (bounded
split-count sufficiency), not as a closure.

Cross-checked the "super-exponential" claim about full $\Sigma(n,k)$
classification against `math-explorer-sigma-shape.md` line 119 — confirmed,
this round's explorer independently established it, so restricting to
$\Sigma_{\le s_0}$ (step 3–4) is the right pivot away from a dead-end
direct-classification route, not a downgrade.

The crux lemma (bounded split-count sufficiency, $s_0=3$) is correctly
labeled unproved/conjectured, with a stated mechanism (exchange argument:
marginal gain from an $(s_0{+}1)$-th split is dominated by re-tuning the
existing $s_0$-piece split) — this is a real mechanism sketch, not a bare
label, though genuinely unproved. Fine for a revise-stage outline; the
builder must not overclaim it.

One thing to watch: step 2 (intra-branch pairwise-difference subtlety) is
correctly flagged as unresolved and given two honest disjunctive resolution
paths (prove pinned by existing $L$, or enlarge $L$) rather than silently
assumed — good practice, no change needed.

## self-similar-induction-on-n — APPROVE

Checked the trichotomy structure against `math-explorer-trichotomy.md`:
Case A circular/dead, Case B reduced-but-open, middle regime with zero
reduction — matches lines 13–38 and 216–219 of that report exactly. The
outline correctly does NOT re-attempt Case A (explicitly excluded in "Cases
to cover"), avoiding a recorded dead end.

The cell-wise-affineness reframing is explicitly marked "genuine
reframing, not a bypass" and the outline itself flags the key risk: the
correspondence with `global-lp-vertex-sufficiency`'s machinery is
*conjectured* by the explorer, not verified, and the outline instructs the
builder to check this explicitly early rather than assume it (step 1
skeleton note, "Watch out for" section) — correct, appropriately cautious.
The claimed advantage (no free-block-solving step needed here since $B$'s
coordinates are already free) is a plausible, checkable simplification, not
an assumed shortcut.

Step 5 (tractability pre-check before full vertex classification) is a
sound sanity gate given `global-lp-vertex-sufficiency`'s own
just-discovered $\Sigma(n,k)$ blowup — good transfer of a lesson across
approaches without conflating the two polytopes.

## greedy-reduction-geometric — APPROVE

The WLOG $b_2=2^{m-1}$ reduction (step 1) is justified as "monotone
favorable to shrink" and is corroborated by the file's own numeric finding
(section 14.3): the exact worst-margin-0 tight instance found across 27,430
trials is *at* $b_2=2^{m-1}$ exactly — consistent with the claim that this
is the hardest sub-case, not an unearned simplification.

Case B's proposed quick-win mechanism (dominant-element insertion via
Theorem 13, twice) is plausible given the explorer's 23,905-trial finding
of substantial slack (worst margin ≈0.34, zero near-ties) — the outline
correctly treats this evidence as motivating an attempt, not as a proof,
and explicitly instructs (per the standing rule from `/tmp/memory`) to
stress-test any specific mechanism before write-up. Case A is correctly
scoped to general $|P|\ge3$ from the start (not extrapolated from $|P|=2$),
matching the explorer's numeric localization to near-geometric
$1{:}2{:}4{:}8$-ratio configurations — avoids a base-case-only trap.
Step 4 correctly forbids re-litigating the refuted Split-Degradation bound
and Candidate Swap Lemma, both already recorded dead in `current.md`.

## lp-duality-split-polytope — APPROVE (tool-supplier framing, correctly scoped)

The outline is honest that this approach's own upper-bound target
(triangular family) is complete, and correctly reframes its round-11 role
as investigating generalization / tool supply rather than re-deriving
already-closed content. Step 2 is explicitly flagged "long shot... treat as
secondary" given the round's own negative numeric finding (ratio ≈1.0 at
LB's geometric partition) — no overclaim risk. This avoids status inflation
while keeping the approach active and useful (its certified
Consecutive-Block AltSum / Bottom-Block-Doubling / Even-Block-Neutrality
lemmas remain citable). Good discipline: explicitly reasserts the round
9/10 scope note that the triangular family is not shown to be (and is
likely not) LB's true extremal partition.

## Untouched approaches this round

`layer-cake-parity-reframing`, `universal-halving-adversary`,
`dyadic-potential-invariant` were not revised this round; no action needed
— they remain in the population at their current Elo/records.
`dyadic-potential-invariant`'s core mechanism is dead (round 6,
Schur-monotonicity refutation) and stays deprioritized;
`universal-halving-adversary` stays deprioritized per its own round-8
redirect to `global-lp-vertex-sufficiency`.

## Ranking

All four outlined slugs plus the three untouched slugs are already
registered (no new slugs this round — all revise/advance on existing
approaches, no copy requested). Ranked the whole field head-to-head via
`update_ranking`, anchoring to `current.md`'s round-10 outcomes: the two
`advanced` approaches with concrete reviewer-certified new theorems this
cycle (`greedy-reduction-geometric` — Lemma M + Swap-Lemma refutation +
clean base-case reduction; `lp-duality-split-polytope` — full
Necessity+Sufficiency for the triangular family) rank above the more
open-ended `self-similar-induction-on-n` and `global-lp-vertex-sufficiency`
(both real progress but with the harder remaining obstruction — full
trichotomy / $\Sigma$-classification respectively), which in turn rank
above the deprioritized `universal-halving-adversary` and the
exploratory-but-real `layer-cake-parity-reframing`, with the dead-ended
`dyadic-potential-invariant` last. This clears `stale` on all seven.

## Diversity note for the orchestrator

Field remains genuinely diverse across four active framings; no shared-gap
plateau this round — each of the four live approaches closed distinct,
independently-verified content in round 10 (Q_region, Lemma M + Swap
refutation, Lemma TPI + endpoint reduction, Multi-Piece Sufficiency for the
triangular family) and each now has its own distinct, named next
obstruction. No RETHINK needed. Continue the current four in parallel.

build set: global-lp-vertex-sufficiency, greedy-reduction-geometric, lp-duality-split-polytope, self-similar-induction-on-n
