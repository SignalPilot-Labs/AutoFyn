## imo-2026-03

self-similar-induction-on-n: revise
Target: the whole problem — c(n)=2^n/(2^{n+1}-1), via the certified
reduction to max_p min_refinement OddSum. This approach owns the
lower-bound direction (LB's geometric construction achieves ≥c(n)); its
sole remaining gap is General Theorem GT(m) for m≥4 (equivalently the
Branch-I.A-restricted window at ℓ≥5), which round 14 reduced to exactly
two named sub-objects: `Case-B(m,k)` (open since round 4) and sub-case
(i) (q=1, e≥1, target OddSum(R∪Γ_{k-2})≥2^k-a_1).
Technique: peel-and-recurse induction on the dyadic level m, now
augmented with (a) the abandoned variable-target generalization
G(m,k;V), and (b) a continuity/limiting transfer across the excluded
boundary of Case-B(m,k)'s sliver.
Skeleton:
  1. **Index-match sub-case (i) to G(m,k;V).** Re-derive, symbol for
     symbol, whether sub-case (i)'s target — OddSum(R∪Γ_{k-2})≥2^k−a_1,
     with R the residual multiset after peeling and a_1∈(2^{k-1},2^k)
     the excess element — is literally an instance of the round-3/4
     definition G(m,k;V): "for every partition B of V into j+1 parts and
     every c-cut refinement S of Γ_{m-1} with j+c≤k, OddSum(B∪S)≥V,"
     taking m=k-1, V=2^k-a_1, B={the elements of R besides Γ_{k-2}'s own
     contribution}. This is a cheap, mechanical check (no new math) —
     do it FIRST, before any proof effort, because if the index match is
     inexact the whole plan below is void. (Explorer's opening (A).)
  2. **If the match holds:** revive the Lemma AS (AltSum reformulation)
     and Single-Insertion Lemma machinery that was built for G(m,k;V) in
     rounds 3-4 but abandoned mid-way (not because it failed — because
     the file pivoted framings). Attempt to close G(m,k;V) for general
     V∈[2^{m-1},2^m] (previously only Monte-Carlo-confirmed, m≤5, never
     proved for j≥1, V<2^m) using this machinery plus the now-certified
     Growth Lemma / Monotonicity Reduction Lemma (round 13-14) as
     additional tools not available when G(m,k;V) was first shelved.
  3. **In parallel, attempt the continuity/limiting transfer for
     Case-B(m,k)'s excluded boundary.** The interior of the sliver
     2^{m-2}≤b_1≤2^{m-1}-1 is closed (round 5); the excluded boundary is
     max(D)→2^{m-1}⁻, exactly where the explorer's own Nelder-Mead sweep
     (m=3..7) finds margin→0⁺ monotonically. Since OddSum is continuous
     in its arguments even through rank ties (this is explicit in the
     already-certified Tie-Neutrality Lemma's proof — ties do not
     require special-casing, unlike the Growth Lemma's own honestly-
     flagged tie-boundary gap from round 14), attempt: fix the already-
     proved interior inequality OddSum(D∪Γ_{m-2})≤2^m-1 for
     max(D)<2^{m-1}-δ for every δ>0, and take δ→0 using the
     Tie-Neutrality Lemma to control what happens exactly at the limit
     point max(D)=2^{m-1} (where D∪Γ_{m-1} then has a genuine tie
     between D's largest coordinate and Γ_{m-1}'s next level down) —
     this is a genuinely different mechanism from every prior attempt
     (all induction/peel-based), worth a dedicated try since the margin
     data is consistent with a clean limiting identity, not with a
     nonzero floor that a soft inequality could catch with room to
     spare.
  4. If both (2) and (3) stall, fall back to reporting the sharpened
     diagnosis only (as round 14 did) — do not force an invalid proof.
Key lemmas (claim + mechanism):
  - G(m,k;V) closes for general V, j≥1 — because the AltSum
    reformulation converts OddSum(B∪S)≥V into a peeling identity whose
    residual term is controlled by the certified Growth Lemma (mono-
    tonicity in the increasing direction, unavailable when G(m,k;V) was
    first attempted in round 3-4).
  - Case-B(m,k)'s boundary case follows from the interior case by a
    continuity/limiting argument — because OddSum is provably continuous
    through rank ties (Tie-Neutrality Lemma), so a family of strict
    inequalities holding on (2^{m-2}, 2^{m-1}-δ) for all δ>0 extends to
    the closed endpoint by taking the limit, PROVIDED the bound itself
    (not just each instance) is uniform in δ — this uniformity is the
    actual content to check, not assume.
Open gaps: whether the index match in step 1 is exact (must be checked
before anything else); whether G(m,k;V) actually closes with the revived
machinery; whether the continuity argument's uniformity-in-δ holds (a
genuine possible failure point — a margin sequence →0 does not
automatically mean the *bounding technique* is uniform, only that the
*true* margin is).
Cases to cover: sub-case (i) is only reached once e grows past
log_2(m+1) (round 14's feasibility diagnosis) — the closing argument
must actually apply in that regime, not just in the abstract.
Watch out for: do NOT re-attempt the naive "piece-cap-relaxed
generalization of GT(k-1)" (refuted, D={0.4,0.4} counterexample) — the
G(m,k;V) route is a DIFFERENT, more general statement (varying V, not a
fixed cap), not a relabeling of the refuted one; verify this distinction
explicitly in step 1's index-matching check.

global-lp-vertex-sufficiency: revise
Target: the whole problem — same reduction, this approach owns the
upper-bound direction (no p beats c(n)). Q_region is fully closed
(round 10); the sole remaining obstruction is the Σ-shape part of the
candidate set Q / equivalently a construction closing the balanced-
region residual at the hard vertices. The descending fragment chain
family (round 14-15) is now DECISIVELY DEAD as a general mechanism: this
round's explorer found, via the exact (not grid-approximated) Singleton-
Interleaving-Lemma closed form, that the FULL exhaustive descending-chain
family fails at fresh random points, 2/20 at n=3 and 4/12 at n=4 — do
NOT re-attempt searching harder within this family (round 14's 2/3-match
"promising" reading is now superseded).
Technique: LP/compactness-vertex classification (Sections 1-4, already
certified) combined with a new construction-family attempt using the
Singleton-Interleaving Lemma as an evaluation tool, cheap-killed before
any proof investment; if that also dies, pivot within the same round to
the existence-only Σ(n,k) route.
Skeleton:
  1. **Cheap-kill: tree/star fragment-tying topology.** Instead of a
     linear or cyclic chain (both now dead), test a STAR topology: pick
     one "hub" split piece with fragments {h_1,...,h_r} (r-way split, not
     just 2-way) and tie each of r-1 other split pieces' single "small"
     fragment to one of the hub's r-1 non-primary fragments — i.e. one
     central piece supplies r-1 tie-values simultaneously instead of a
     chain propagating one tie-value forward. Evaluate via the certified
     Singleton-Interleaving Lemma exactly as the explorer did for the
     chain (closed-form affine function of the remaining free
     parameters, exact breakpoint optimization, not a grid) — this reuses
     verified machinery, no new tooling needed. Test EXHAUSTIVELY (every
     hub choice, every partner subset, exact optimum over free
     parameters) against the SAME fresh random balanced-region points
     that killed the descending chain (n=3,4, ≥15 points each, exact
     rational arithmetic) BEFORE writing any lemma. If it fails at a
     comparable or worse rate, record as a dead end and move immediately
     to step 2 in the SAME round — do not spend further build time on
     topology variants.
  2. **If step 1 also dies (expected, given 3 chain/cycle/star variants
     failing for structurally similar reasons — no bounded-description
     tie-construction has ever survived at Q's hard vertices): pivot to
     the existence-only route.** Target a genuinely weaker, non-
     constructive claim: for every cell C of the L-arrangement (already
     proved finite, Lemma 4.1), there EXISTS some member of Σ(n,k)
     (not necessarily from any named construction family) attaining
     V(p) on C and satisfying V(p)≤c(n) — proved via a case-independent
     argument on the cell's defining inequalities (e.g. an LP-duality
     certificate specific to each cell's affine functional, using the
     already-certified affineness of f_σ on C) rather than by
     exhibiting the winning σ explicitly. This does not require bounding
     |Σ(n,k)|, only that SOME bound argument applies uniformly across
     cells — a different kind of argument than enumeration.
Key lemmas (claim + mechanism):
  - Star-topology closed form — because the Singleton-Interleaving Lemma
    (Theorem 9) applies to any tie structure that is a bijection between
    a "tied" set and its images, and a star (one hub with r-1 spokes) is
    such a structure exactly as much as a chain is; only the resulting
    affine-coefficient pattern differs.
  - Per-cell existence bound (if step 2 is reached) — because affineness
    of f_σ on each cell C (already certified) means the constraint
    "some σ achieves ≤c(n) on C" is itself an LP feasibility question
    over C's vertices, reducible to checking the (already fully closed)
    genuine vertices of C plus a certificate that non-vertex interior
    points are dominated by a convex combination — this is a genuinely
    different mechanism from constructing an explicit winning σ.
Open gaps: step 1's star-topology numeric outcome (unknown until run);
step 2's LP-certificate argument is only sketched, not yet attempted by
any approach.
Cases to cover: none beyond n=3,4 cheap-kill coverage for step 1.
Watch out for: do not let step 1 consume more than the cheap-kill budget
— per the population's now-3-times-repeated pattern (cyclic chain,
descending chain, and now expected star), a fourth bounded-construction
family surviving would be surprising; the mandated exhaustive test at
fresh points (not just the 3 catalogued hard points) is what makes this
a real kill, not a cherry-picked pass.

discharging-neighbor-transfer: new
Target: the whole problem — attempt an independent, from-scratch
argument for V(p)≤c(n) (upper bound) via a genuine charge-transfer/
discharging invariant maintained across the whole two-phase cutting
game, distinct in kind from every framing tried so far (peeling/
induction, layer-cake, LP-duality/split-polytope, self-similar
recursion, global-LP-vertex/compactness, structured-randomization — all
of which the plateau-check explorer confirms are either dead-ended or
share the same "no per-cut/per-piece additive decomposition survives"
wall). If it succeeds it directly closes global-lp-vertex-sufficiency's
Σ-shape gap; framed as a standalone whole-problem attempt (not a patch)
because a genuine discharging invariant, if it exists, proves the bound
for every p uniformly, not just at the hard vertices.
Technique: charge-transfer discharging (Four-Color-Theorem style: define
transfer RULES between neighboring objects, prove conservation by
summing transfers — not a single closed-form potential evaluated per
object, since three such fixed-formula attempts have now failed:
Cut-Reallocation Exchange Lemma, per-cut-additive layer-cake, and this
round's own falsified w(v,s)=v·2^{-|log2 v-s|}).
Skeleton:
  1. **MANDATORY FIRST STEP (per dispatch, cheap-kill before any proof
     investment): hand-check the neighbor-transfer-rule variant.** On
     the explorer's own worked example — the geometric partition
     (8,4,2,1)/15 (n=3), splitting the top piece 8→4.8+3.2 — the
     fixed-formula `s=-i` convention gave residual Δ=+0.03125 (small
     but nonzero). Attempt, by direct algebra (not a script), a
     transfer rule that moves exactly this residual charge between the
     split piece and the pieces whose RANK shifted as a result of the
     split (ranks 2,3,4 in the post-split ordering — the diagnosed
     mechanism: rank-shift-blind formulas cannot capture this, per the
     plateau-check explorer's finding that the sign of Δ flips between
     top-split and middle-split under the s=i convention specifically
     because of uncaptured rank shifts). Check whether SOME local
     transfer amount (not a formula guess — solve for it exactly from
     the algebra of the single example) zeroes the residual. Repeat on
     a SECOND, structurally different example (a middle-piece split,
     e.g. 2→1+1 in the same partition) to check whether the same rule
     (not a different one per example) works both times — a rule that
     only works on one hand-picked example is not a real cheap-kill
     pass.
  2. If step 1 finds a consistent local rule: generalize to an explicit
     transfer function T(piece, split-details, rank-shift) and prove
     conservation in general (sum of all transfers over any legal
     single cut = 0) as a genuine algebraic identity, then extend by
     induction over the sequence of n cuts to a global conservation
     statement, then relate the conserved total charge to OddSum(M)
     directly (this last connecting step — charge total ↔ OddSum — is
     itself unproven and must be established, not assumed, since the
     whole point of the invariant is to bound OddSum via a quantity
     that IS provably conserved/bounded).
  3. If step 1 fails on even the second example (a real possibility,
     given the failure mode diagnosed by the plateau-check explorer is
     structural — a cut changes ALL lower ranks' positions, not just a
     local neighborhood, so no genuinely "local" transfer rule may
     exist at all): report a clean negative result (this is a real,
     certifiable finding — "no local single-cut charge-transfer rule
     restricted to rank-adjacent pieces can conserve charge" — ruling
     out the whole neighbor-transfer family, not just the fixed-formula
     subfamily) and issue RETHINK, per the population's established
     discipline of not forcing an invalid proof onto a dead mechanism.
Key lemmas (claim + mechanism):
  - Local transfer rule exists and conserves charge on a single cut —
    because [to be determined by step 1's algebra; this is exactly the
    open question the cheap-kill answers, not assumed true].
  - Global conservation ⟹ OddSum bound — because [the connecting
    argument itself, once a conserved quantity is found, must show that
    quantity dominates or equals AltSum/OddSum up to a controlled slack
    — this is a second, currently entirely unaddressed gap even if step
    1-2 succeed].
Open gaps: everything downstream of step 1's outcome — this approach is
maximally honest that it may die in the first 30 minutes of its build,
per the mandatory-cheap-kill discipline established over three prior
falsified single-formula attempts in this exact family.
Cases to cover: at minimum the top-split and middle-split example types
(both already numerically diagnosed as behaving differently under fixed
formulas) must both be checked before generalizing.
Watch out for: do NOT let the builder skip straight to "define some
transfer rule and hope" — the whole point of the cheap-kill is to derive
the rule's existence (or non-existence) from the algebra of 1-2 concrete
examples FIRST; do not reuse or lightly modify the already-falsified
w(v,s) formula as a starting point (its failure mode — sign flip between
top- and middle-split under one convention — is diagnostic evidence
against any rank-local-only formula, whether transfer-based patches to
it are tried first, this wastes the round).

lp-duality-split-polytope: advance
Target: the whole problem — same reduction, upper-bound direction. The
Chain-Correction Floor Theorem (V(e_0)=1/2 exactly, n≥6) is certified;
the Perfect-Tie-Family Exact Characterization (round 12) shows no fixed
s_0 "perfect" self-tie suffices. Genuinely open: the general nonzero-
residual fragment-vs-fragment family, and n<6 for the Chain-Correction
construction.
Technique: same as before (explicit closed-form constructions at the
region vertex e_0, generalized via the certified AltSum/Singleton-
Interleaving machinery).
Skeleton:
  1. Extend the Chain-Correction Floor Theorem's construction to n<6
     (currently only proved n≥6) — check whether the same hybrid
     mixing (tie-to-untouched, fragment-vs-fragment chain, plain
     bisection) admits a variant hitting the floor for n=3,4,5, or
     whether small n is genuinely different (finitely many cases,
     checkable exactly).
  2. Cross-feed this round's fragment-tying negative results (from
     global-lp-vertex-sufficiency's revised work above): if the star-
     topology cheap-kill in that approach produces a numeric near-miss
     or exact match at any hard vertex, attempt to explain it via this
     approach's own exact-characterization machinery (Perfect-Tie-
     Family style), converting a numeric coincidence into a proved
     closed form if one exists — this is the kind of cross-approach
     synthesis that has paid off before (rounds 12, 14).
Key lemmas: none new proposed; this is incremental extension of already-
certified machinery to uncovered n-ranges and cross-validation duty.
Open gaps: n<6 case of Chain-Correction; general nonzero-residual
fragment-vs-fragment family (numeric hint only, not proved).
Cases to cover: n=3,4,5 individually for step 1.
Watch out for: do not duplicate global-lp-vertex-sufficiency's star-
topology cheap-kill work — this approach's role is extension/synthesis,
not re-running the same numeric test independently.
