## imo-2026-03

dyadic-cascade-induction: revise
Target: the whole theorem `c(n)=2^n/(2^{n+1}-1)`, both directions, every `n` (this approach's
existing scope: full physical-cut lower-bound casework for every `m` against `D_m`, plus the
`n=1,2` upper bound and `n=3` Case (i) upper bound already proved).
Technique: for the revised gap specifically — a self-contained, D_m-only resolution of the
"all-cycles" D/M-completeness caveat, via (i) a cheap pigeonhole/counting fact, (ii) a
joint piecewise-linear extreme-value argument (Vertex-Lemma-style) for the minimal cycle, and
(iii) a crux-inspired (`aimo-0003`) adjacent-transposition/confluence induction on cycle length
— bypassing the general `lemmas/dm-completeness-partial.md` lemma entirely rather than
extending it, since that lemma's own general form has been stuck since round 4.
Skeleton (new §5.4, written into the approach file):
  1. Guaranteed-Untouched-Original Lemma: for `A=D_m`, `k=m+1` pieces, any `\le m`-cut strategy
     touches at most `m` distinct root originals (each cut traces to a unique root via forest
     parentage) — by pigeonhole, `\ge1` original of `D_m` is always left completely untouched.
  2. Base-case Cycle-Breaking Lemma (length-2 cross-tie cycles): with the guaranteed untouched
     third piece present, the pure-cross-tie sub-family's value is piecewise-linear in the
     shared tie parameter `t` (Lemma P collapses the duplicate pair, Vertex Lemma gives
     piecewise-linearity), and its minimum is always at a breakpoint tying the untouched piece
     (cycle-breaking) or a degenerate boundary — never a genuinely inescapable interior optimum.
  3. Cycle-Shortening induction (open): generalize step 2 to cross-tie cycles of length `\ge3`
     via a local re-target move (crux `aimo-0003`'s adjacent-transposition-generates-the-group
     idea) against the guaranteed-untouched piece, inducting down to the length-2 base case.
  4. Conclude: no all-cycles obstruction can occur for `A=D_m` at any `m`, promoting the already
     -proved D/M-sequence bound (Superincreasing No-Early-Zero Lemma, §5.3, certified) to the
     true physical lower bound `g(D_m,m)\ge e_m\cdot S(D_m)`, for every `m`.
Key lemmas (claim + mechanism):
  - Guaranteed-Untouched-Original Lemma — because cut-forest roots injectively bound touched
    originals by `\le m < k`.
  - Base-case Cycle-Breaking Lemma — because Lemma P + Vertex Lemma reduce the 2-cycle family
    to an ordinary 1-parameter piecewise-linear extremal problem whose minimum is always at a
    tie/boundary, never purely interior-cyclic.
  - Cycle-Shortening/Local-Re-Target Lemma (OPEN) — conjectured mechanism only: an
    adjacent-transposition-style exchange targeting the guaranteed-untouched piece.
Open gaps: Step 3 (cycles of length `\ge3`) is the sole remaining piece; steps 1-2 are cheap
and unconditional, should be written up and verified first.
Cases to cover: cycle lengths `L=2,\dots,\lfloor(m+1)/2\rfloor` in Step 3's induction.
Watch out for: (a) whether the `L` tying equations of a length-`L` cycle collapse to fewer than
`L` free parameters (verify, don't assume, before attempting the induction); (b) do not conflate
the "escape to an untouched piece" move with the already-refuted "re-pair a fixed support" dead
end from `potential-weighting-upper-bound` — confirm the distinction explicitly, since this
targets a genuinely new resource (the untouched piece), not a re-pairing of already-cut pieces.

potential-weighting-upper-bound: revise
Target: the whole theorem's upper-bound direction, general `m` (this approach's existing scope:
D/M operation reformulation, certified Slack Collapse Lemma reducing the whole induction to the
tight case `k=m+1`, non-crossing matching+deletion conjecture for that tight case).
Technique: for the revised gap (proving the non-crossing matching+deletion conjecture) — retire
the now-confirmed-dead local pairwise uncrossing-exchange technique in favor of (i) a new
"layer-cake" threshold-counting reformulation of `e`, and (ii) a top-down peel-the-extreme-
element DP/induction (the standard non-crossing-partition recursion, using Fact 3's own
`(-1)^{|X|}` sign flip as a genuine running rank/sign-offset invariant carried through every
level — not a bounded lookahead, and not a local exchange).
Skeleton (new §8, written into the approach file):
  1. Layer-cake identity (new, general, easy): `e(\text{sorted }x_1\ge\dots\ge x_n) =
     \int_0^\infty \mathbf{1}[N(t)\text{ odd}]\,dt`, `N(t):=\#\{i:x_i>t\}` — proved by an
     elementary induction matching the telescoping alternating sum term-by-term.
  2. Define `NC(Y,b)` (the best non-crossing selection's value) via the classical
     non-crossing-partition recursion on the extreme element `y_1` (keep / delete / match to
     each `y_j`, recursing on inside/outside sub-lists with split budgets), scored exactly via
     the certified Fact 3 block-extraction identity at every level — a well-defined, fully
     computable quantity, no conjecture needed for this step.
  3. Prove `OPT(Y,b)=NC(Y,b)$ by strong induction on `p`: given any optimal (possibly crossing)
     selection, case on `y_1`'s fate and replace the ENTIRE residual selection (not one arc) by
     an equal-or-better non-crossing one via the IH — a global replacement, structurally
     different from local exchange (which only ever perturbs one arc within a frozen support).
  4. Conclude: `OPT=NC` closes the non-crossing conjecture, giving (via Fact 3) a closed-form
     expression for the one-shot tail, completing the chain-prefix+tail family's proof.
Key lemmas (claim + mechanism):
  - Layer-cake identity — because odd/even nested-threshold coverage exactly reproduces the
    alternating-sum telescoping.
  - `NC(Y,b)` closed form — because the inside/outside split is Fact 3 applied recursively to
    itself, no new machinery.
  - `OPT=NC` induction (OPEN) — the genuine content is whether an arc from outside a matched
    pair `(1,j)` that crosses it can always be rerouted around the split without loss; this is
    a different, larger move than the already-refuted local arc-swap.
Open gaps: Step 3's induction, specifically the outside-crossing-arc interaction.
Cases to cover: the three-way `y_1` fate split (kept/deleted/matched-to-every-`j`) is exhaustive
by construction; inside/outside budget splits are standard non-crossing DP bookkeeping.
Watch out for: (a) apply the layer-cake identity to the FINAL multiset (kept elements plus
match-difference values), not to `Y` itself — the interaction between kept-element thresholds
and match-difference thresholds is exactly where the difficulty lives; (b) reject any builder
write-up that only ever perturbs one arc at a time while freezing the rest — that has silently
regressed to the confirmed-dead local-exchange mechanism.
Secondary/fallback (not built this round): LP-relaxation of the cut-allocation problem + an
integrality-gap bound, flagged by this round's new-framing explorer as an alternative technique
for the same `k=m+1` gap if the DP/induction route stalls for several more rounds.

concavity-minimax-duality: advance
Target: the whole theorem's lower-bound direction, via a closed-form 1-Lipschitz certificate
`g_m` (an independent route to the lower bound not needing D/M-completeness at all).
Technique: extend the already-certified Cascade Reachability Lemma + Forced-Value Lemmas A/B
(`g(1)=1,g(2)=2` forced, round 5) to check whether `g(j)=j` is forced for every reachable `j`,
rather than proposing a new scalar candidate from scratch (that line — `\Phi_1,\Phi_2`,
`\min(t,1),\min(t,2)` — has been tried and refuted twice already).
Skeleton:
  1. Reuse the Cascade Reachability Lemma (already proved: `D_j\to D_{j-1}` reachable in exactly
     one D/M op, for every `j`) to construct, for each `j=3,4,\dots`, an explicit reachable
     witness state analogous to the round-5 `g(1),g(2)` witnesses.
  2. Check whether the same forced-value argument (1-Lipschitz + the witness's own structure)
     pins down `g(j)=j` exactly, or whether it stops being forced at some `j_0`.
  3a. If forced for all `j`: conclude no nontrivial 1-Lipschitz certificate can differ from the
      identity on any reachable value — a clean, general, decisive negative result retiring
      this whole certificate line.
  3b. If forcing stops at some `j_0`: identify precisely why (which reachable witness fails to
      constrain `g(j_0)`), turning the informal "slack at `g(4)\in[3,4]`" observation into a
      structural fact usable to construct an actual candidate `g_m` differing from identity.
Key lemmas (claim + mechanism):
  - Generalized Forced-Value Lemma (claim: `g(j)=j` forced for every `j` up to some threshold,
    or all `j`) — because the same reachable-cascade-witness + 1-Lipschitz argument that forced
    `g(1),g(2)` in round 5 is, by construction, not obviously specific to `j\le2`; whether it
    generalizes is a concrete, cheaply checkable question, not yet asked.
Open gaps: whether the generalized forcing argument holds is untested; this is this round's
one concrete task.
Cases to cover: none beyond checking increasing `j`.
Watch out for: do not force a brand-new scalar potential candidate this round if the forcing
check is negative — report precisely where/why it fails (the structural information itself,
per outcome 3b above, is the valuable output, not a hastily-guessed replacement candidate).

Notes for the outline-reviewer / build-set choice: no new slug is proposed this round. The
new-framing explorer's search (self-similar recursion, majorization/Schur-convexity, the
"leave-alone-or-subdivide" framing, Sion's minimax, entropy bounds) was exhaustive and
conclusively negative — every candidate either collapses into an already-recorded dead end or
is isomorphic to the existing non-crossing-matching-conjecture gap. Forcing a nominally-"new"
slug here would just be a relabeled restatement of one of the two approaches above (the
single-gap trap CLAUDE.md warns against), so the field stays at 3 live slugs this round, each
attacking a genuinely different mechanism for its respective open gap.
`elementary-exchange-smoothing` remains formally retired (round 4) — do not dispatch a builder
to it; no new target was found for it this round either.

build set: dyadic-cascade-induction, potential-weighting-upper-bound, concavity-minimax-duality
