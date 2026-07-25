# Outline review — round 9, imo-2026-03

Source of truth used: the actual files in `results/imo-2026-03/approaches/*.md`
(not just `/tmp/round-9/proof-outliner.md`'s summary), `current.md`, and
`.ranking.json`. All five approaches are continuations (revise/advance), no
new slugs this round, so no `register_approach`/`copy_approach` calls are
needed.

## global-lp-vertex-sufficiency — APPROVE (pivot verified sound)

This is the pivot flagged for scrutiny: concavity of V(p) is abandoned
(correctly — round 8/9's explorer found a genuine sign-alternating
second-difference at n=2, deficit ≈0.01, far outside numerical noise; the
file explicitly forbids re-attempting it) and replaced by a finite
hyperplane-arrangement / cell-wise-affine-vertex target.

**Checked the new target is a real mechanism, not a restated existence
claim.** The plan is: from the already-certified Global Vertex Lemma
(`V(p) = min over valid σ∈Σ of f_σ(p)`, Σ finite and p-independent, each
f_σ affine, validity an affine half-space condition x_σ(p)≥0), build the
finite list L of affine functionals = {every coordinate of every x_σ(p)} ∪
{every pairwise difference f_σ(p)-f_τ(p)} ∪ {the balanced region's own
defining inequalities}. This is standard sign-arrangement machinery: on any
open cell of the arrangement induced by L, every functional in L has
constant sign, hence (a) the set of valid σ is locally constant and (b) the
ordering among valid σ's f_σ values is locally constant, so V restricted to
the cell is a single fixed affine formula — and an affine function's max
over a convex polytope is attained at a vertex. This is a genuine,
checkable mechanism (the same idea underlying parametric-LP / oriented-
matroid sign-vector decompositions), not hand-waving "there exists a finite
reduction." I verified this logic myself independently (not just trusted
the file's prose) and it holds.

**Numerical spot-check (own script, not the file's).** Brute-forced V(p) at
n=2 (k=3) via direct minimization over all cut-allocations and fragment
splits (Nelder-Mead, 25 restarts per allocation) at 6 random balanced-region
points; all gave V(p) ≤ c(2)=4/7 with comfortable margin (worst case
V=0.507 vs c(2)=0.571). This doesn't test the arrangement machinery per se
(that's inherited, correctly, from the already-certified Global Vertex
Lemma) but confirms the Existence Theorem target itself isn't obviously
false at the one n where I could cheaply check it — no red flag.

**Minor gap to flag (not fatal, CHANGES REQUESTED-level care needed during
build, not blocking approval of the outline):** the balanced region is
defined with strict inequalities (p_1<1/2, gaps>γ(n)), so it's open; "max
of affine function over an open cell attained at a vertex" needs the
closure (cell-closure ∩ closed balanced region) argument, consistent with
how Section 3's compactness step already extends to the closed region. The
outline doesn't spell this out explicitly. Flag it for the builder to
handle explicitly (should be routine given Lipschitz continuity is already
certified — V extends continuously to the closure — but must be stated,
not silently assumed).

**Tractability is honestly flagged as open**, not hidden: "the practical
tractability (bounding/classifying |Σ(n,k)|...) is unattempted" is stated
directly under Open gaps, and the file's own "Cases to cover" section says
the reduction to a finite candidate set "must be executed, not just
asserted" — this is exactly the right level of honesty for a target that
is mathematically well-posed but computationally unexplored. The
tractability shortcut (check known survivor configurations first) is a
sensible cheap first move before attempting the full arrangement.

Verdict: **APPROVE**. The pivot is real progress — it replaces a dead
concavity target with a well-posed, mechanistically justified finite-vertex
reduction — not a restatement of the problem.

## self-similar-induction-on-n — APPROVE

Target: close the Branch-I.A-restricted window (now the sole remaining
piece of the sliver, after round 8's Branch II ≡ window equivalence) via
exchange-smoothing modeled on crux aimo-0146, using the certified
Single-Insertion Lemma's exact delta formula as the "unit move" primitive.
The claimed mechanism ("any deviation from the partial-duplicate-the-rest
extremal shape can only add OddSum mass at odd ranks") is stated with an
actual reason (the piece-count budget forces the extremal shape; the
Single-Insertion Lemma gives the exact per-move delta), not a bare label.
Open gaps section is honest that the exchange-smoothing proof itself is
"not yet attempted... only the extremal witness and crux analogy are
established," and correctly flags re-verifying eps/2 at l=7,8 before
trusting the pattern beyond l≤6 — appropriately cautious given round 8's
lesson (idx=1's false extrapolated closed form) about not trusting a
numeric pattern past its checked range. No case-coverage issue (the window
is a continuum, correctly not treated as discrete casework). Approve.

## greedy-reduction-geometric — APPROVE

Target: close Level-Absorption (Subcase (b), the sole remaining piece of
Theorem 7'(m,k;L)'s inductive step) via a quantitative insertion-gain bound,
explicitly NOT via a hypothesis-dropping generalization of Theorem 13
(checked and ruled out this round — stated as a genuine finding, not
assumed). Two concrete routes given (direct chained-gain computation from
Theorem 12's Delta formula, or the same aimo-0146 exchange-smoothing family
used by the sibling gap above) with the tight instance's margin
(2^(m-3)-1/2 > 0) cited as evidence real slack exists once the budget is
correctly enforced. "Watch out for" section explicitly warns against
citing Theorem 13 directly for this (a stated category mismatch — Theorem
13 gives only a zero-gain bound, not the needed positive quantitative one)
— this is exactly the right kind of self-aware guardrail after round 7's
recurring "reduced target loses a hypothesis from the parent" bug pattern.
Approve.

## lp-duality-split-polytope — APPROVE

Multi-Piece Necessity for the triangular family is now fully closed
(certified). This round's target — an explicit closed-form 2-piece
sufficiency response for the triangular family, general n — is a
well-motivated next step built on the just-certified AP-landmark structure
(scaled landmarks are exactly 1,...,n+1, so pairs with i+j=n+3 sum to the
scaled p_1, giving a natural "split p_1 to match two landmarks" candidate).
The outline correctly flags this as a lead (n=3 only hand-verified so far),
not a proof, and explicitly warns against assuming monotonicity in n
(consistent with round 6/7's finding that the necessity floor itself is
non-monotonic for related number-theoretic reasons) and flags parity/range
casework as expected. Sound, appropriately scoped. Approve.

## universal-halving-adversary — hold out of build set (not RETHINK)

No new build target this round — the outline explicitly states "No new
build work is proposed for this approach this round; it stays registered
and its certified tools remain importable." Its full-closure job was
already redirected to `global-lp-vertex-sufficiency` in round 8. Nothing
here is wrong or doomed; there is simply nothing new to build. Per the
per-role rule (round 2's "hold design-stage/no-content approaches out of
build set but keep them ranked"), the symmetric case applies here too: a
mature approach with zero new task this round shouldn't consume a builder
slot. Keep registered/ranked (Theorem 12 stays importable as a candidate
survivor configuration for global-lp-vertex-sufficiency's shortcut check).

## Cross-approach diversity check

The field remains genuinely diverse: two lower-bound-direction approaches
(self-similar-induction-on-n's l-indexed scalar recursion,
greedy-reduction-geometric's dominance-chain/peeling casework) attacking
two different named sub-problems (window closure vs. Level-Absorption) that
are related but distinct (per round 8's diagnosis, not duplicated work);
two upper-bound-direction approaches (lp-duality-split-polytope's
triangular-family-specific vertex enumeration vs. global-lp-vertex-
sufficiency's general balanced-region arrangement argument) that are
explicitly designed to feed into each other (lp-duality's sufficiency
witness as a candidate extremal point for global-lp-vertex's arrangement)
without being the same proof split into pieces — each stands on its own as
a complete-in-principle route to its half of the problem. No single-gap
trap, no shared-wall plateau this round (both directions narrowed to a
single well-diagnosed remaining piece each, with concrete next-step
mechanisms, not vague "then it follows"s).

## Ranking

Ran `update_ranking` with 6 comparisons anchoring the round's 4 real,
verified advances (lp-duality-split-polytope's full necessity closure,
greedy-reduction-geometric's full Insertion-Robustness closure,
self-similar-induction-on-n's Branch II unification, global-lp-vertex-
sufficiency's Lipschitz + honest obstruction diagnosis) against
universal-halving-adversary's stagnant/deprioritized status this round.
Result (best-first): universal-halving-adversary 1601 (still high from
historical accumulation despite no new work — watch this if it persists),
greedy-reduction-geometric 1578, lp-duality-split-polytope 1565,
self-similar-induction-on-n 1519, global-lp-vertex-sufficiency 1471
(newest, lowest expanded count).

## Next-round watch

- If global-lp-vertex-sufficiency's arrangement enumeration turns out
  intractable (Σ(n,k) too large to classify), the fallback should be the
  "survivor configuration" shortcut already flagged in its own file —
  don't let a full enumeration attempt eat a whole round without first
  cheaply checking known candidates.
- self-similar-induction-on-n and greedy-reduction-geometric are both
  attempting a structurally similar exchange-smoothing argument via the
  same crux family (aimo-0146) on two different targets (window vs.
  Level-Absorption) — if BOTH stall on the same obstruction next round,
  that would be a real signal the crux-0146 technique doesn't transfer
  here, worth flagging explicitly rather than treated as two independent
  failures.

build set: global-lp-vertex-sufficiency, self-similar-induction-on-n, greedy-reduction-geometric, lp-duality-split-polytope
