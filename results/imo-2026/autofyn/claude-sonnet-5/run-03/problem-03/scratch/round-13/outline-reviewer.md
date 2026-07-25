# Round 13 outline review — IMO-2026-03

## Verdict: outline approved as proposed, no cuts, no new approaches

Read `current.md`, all 8 approach files' current heads/tails, `.ranking.json`,
and this round's three explorer reports (`math-explorer-plateau-check.md`,
`math-explorer-general-l.md`, `math-explorer-lp-vertex.md`) against the
outliner's `/tmp/round-13/proof-outliner.md`. Every claim the outline makes
about round-12/round-13 state checks out against the underlying files —
nothing fabricated, nothing overclaimed, no step silently promoted from
"conjectured" to "proved."

## Checks performed

**1. Plateau-check claim (the two open gaps are not the same obstruction).**
Verified directly against the explorer report: GT($m$)'s obstruction (a
1-D dyadic threshold descent, depth provably $O(\log m)$ via an explicit
Feasibility Lemma) and the Σ-shape Existence-Theorem gap (an unbounded
combinatorial classification $|\Sigma(n,k)|$ with no known formula) are
shown structurally distinct, with an honest concession that both share only
a rhetorical pattern. This correctly blocks a `self-similar-induction-
on-n` ⟺ `global-lp-vertex-sufficiency` merge and correctly still allows
each to be pushed independently this round. No leap here.

**2. `self-similar-induction-on-n` Routes A–D.** All four routes are
extensions of already-certified machinery (the peeling-identity chain, the
Feasibility Lemma, the certified vertex/affine-cell lemmas from the sibling
approaches) — none invokes a new unproven axiom. Route B (exchange-
smoothing) is flagged with its real, non-trivial gap named explicitly (rank/
parity sensitivity of OddSum under a coordinate swap, unlike a smooth
functional) rather than assumed away by analogy to the crux transplant —
correct per CLAUDE.md's "hint to adapt, never a citation" rule. The
explorer's own numerics (tight margins through $m=6$, extremizer always
tied-pair-shaped, the literal feasibility-witnessing configurations
comfortably safe) support Route B/C as the live priority without claiming
them proved. Route A/D is flagged as the direct-but-fiddly fallback with an
honest "not completed this round" pedigree, and the outline correctly bans
re-attempting the literal hand-extension (round 12 already showed it doesn't
terminate — depth grows like $\log_2 m$). Sound, no doomed leap.

**3. `global-lp-vertex-sufficiency` response-side exchange target.**
Cross-checked against the round-13 lp-vertex explorer: region-geometry-
driven mechanisms (fixed-vertex path monotonicity, both new exchange
families this round, even the maximally weak existential form) are now
refuted with genuine (non-noise, $10^3$–$10^4\times$ margin) numeric
counterexamples — correctly not re-proposed. The response-side exchange
(build $q$ from the adversary's optimal shape $\sigma^*(p)$'s tie structure,
not from $p$'s own region-slack coordinates) is the one mechanism flagged as
untested by any round to date, and the outline correctly gates it behind a
numeric sanity check *before* any proof investment (step 2 of its plan),
with an explicit honest fallback ("report that honestly rather than
searching for a fourth exchange variant") if it also fails. This is the
right discipline — no premature proof commitment on an unverified mechanism.

**4. Standby-only roles for `lp-duality-split-polytope` and
`greedy-reduction-geometric`.** Confirmed both approaches' own round-12
content is exhausted for their currently-assigned scope (Perfect-Tie-Family
characterization complete for its subfamily; Window Reduction Theorem
closes gap (b) in full) and that `greedy-reduction-geometric`'s only
remaining open item is *literally* GT($m$) at general $m$ (confirmed twice
in-file, independently restated by this round's plateau-check explorer) —
so assigning it no independent build and flagging its Elementwise
Monotonicity Lemma as reusable inside `self-similar-induction-on-n`'s Route
B is correct, not a demotion without cause.

**5. Untouched approaches.** `universal-halving-adversary`,
`dyadic-potential-invariant`, `layer-cake-parity-reframing` correctly left
alone (no explorer surfaced anything new for them this round).
`structured-randomization-upper-bound` correctly stays RETHINK — the
plateau-check explorer's independent consideration of a probabilistic
lower-bound angle found nothing to revive it.

## Ranking

No new approach opened this round, so no `register_approach`/
`copy_approach` calls. Four approaches carried `stale: true` from round 12
(their outcomes recorded but not yet folded into head-to-head Elo); folded
them in via `update_ranking` per this round's relative read of round-12
outcomes (`greedy-reduction-geometric`'s full gap-(b) closure > `self-
similar-induction-on-n`'s positive partial closure (gap (a), $\ell\le4$,
plus a caught-and-fixed scope error) > `global-lp-vertex-sufficiency`'s
negative-only bypass-mechanism results ≈ `lp-duality-split-polytope`'s
negative-only characterization result, scored as a draw). Updated Elo
(stale cleared on all four):

- `greedy-reduction-geometric`: 1657.54
- `lp-duality-split-polytope`: 1584.76
- `global-lp-vertex-sufficiency`: 1525.59
- `self-similar-induction-on-n`: 1501.25

This leaves `greedy-reduction-geometric` and `lp-duality-split-polytope`
top-ranked by Elo (reflecting their strong, complete round-12 results) even
though neither gets an independent build this round — correct, since Elo
tracks approach quality/progress, not this round's dispatch priority, and
the orchestrator's build set is chosen by "which approach has a genuine,
well-scoped open target this round," not raw Elo rank.

## Build set confirmation

Both proposed targets have well-scoped, honestly-gapped, non-doomed round-13
plans, backed by this round's explorer numerics, and are the two approaches
carrying the problem's only two live top-level gaps. No changes to the
outliner's proposed build set.

build set: self-similar-induction-on-n, global-lp-vertex-sufficiency
