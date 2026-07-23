## imo-2026-03

All three build-set approach files were revised **in place** this round (edits applied directly
to `results/imo-2026-03/approaches/*.md`); no new slug opened. Rationale for each decision below,
then the field for the outline-reviewer.

### Why no 5th slug (dispatch item 4)

The `math-explorer-gstar-framing.md` report's "genuinely new candidate" — a probabilistic/
averaging existence argument (`E[e]\le` target over a random response distribution) for the
upper-bound Case (ii) gap — was evaluated against CLAUDE.md's single-gap-trap and plateau-break
rules and **not** opened as a new slug. Reasoning: it targets exactly the same sub-gap
(`potential-weighting-upper-bound`'s open MATCH-branch/crossing obstruction) using the same
overall framing (D/M formalism, one-shot allocation, Lemma D/M, Lemma P) — it swaps a
deterministic-construction technique for an expectation-based existence technique on the *same*
open step of the *same* overall route, not a genuinely different whole-problem route (different
top-level target, reduction, or angle). Per memory rule 16 and the CLAUDE.md warning against
fragmenting one proof's sub-tasks across slugs, this belongs as a flagged alternative mechanism
*inside* `potential-weighting-upper-bound`'s own open-gap description (added, see below), not a
new Elo-bearing population member. If a future round wants to test it concretely and it produces
a genuinely different overall proof skeleton (e.g. it turns out the randomized argument gives an
entirely different induction structure, not just a different way to fill the MATCH branch), it
can be promoted to its own slug then — not preemptively.

The other three "new framing" candidates the explorer checked (generating-function, entropy,
outer-recursion-in-n) were independently re-confirmed isomorphic to existing machinery/dead ends
— no action needed, already correctly not proposed by the explorer itself.

---

dyadic-cascade-induction: revise
Target: `c(n)=2^n/(2^{n+1}-1)`, full theorem — this slug's role is the lower-bound direction
(XY cannot beat `e_m\cdot S(D_m)` against the dyadic opening, for every `m`), via the D/M-sequence
formalism promoted to a true physical bound.
Technique: strong induction / direct physical-cut casework, now supplemented by the "all-cycles"
tie-dependency-graph cycle-elimination machinery (`lemmas/dm-completeness-partial.md`,
`lemmas/shallow-cycle-resolution.md`).
Skeleton (new §5.5 added this round, appended before "## Promotable lemmas" in the file):
  1. Classify every possible tie-dependency cycle by the integer invariant `\#X` := number of
     cross-type edges (cheap structural pruning, composing the `L` affine cyclic relations into
     one scalar closing equation with coefficient `(-1)^{\#X}$ and a signed `\pm1` subset-sum
     offset over `X`-successor pieces) — by KB "invariants and monovariants" heuristic
     (classify-by-one-integer before casework).
  2. `\#X=0`: already resolved (existing Shared-Value Cycle-Breaking Lemma, any `L\ge2`).
  3. `\#X=1`: new short Lemma — forces a common value `t` plus a self-bisection identity,
     reduces to the certified Vertex Lemma's other breakpoint type (out-degree 0, peelable).
  4. `\#X\ge2` even: new Lemma — closing equation is `0=(\text{nonempty signed subset sum})`,
     infeasible by the certified exact no-vanishing-signed-subset-sum fact (no dominance/
     magnitude argument needed — this is the key reason it also covers derived participants,
     unlike the round-7 crude extension attempt).
  5. `\#X\ge3` odd: **the single remaining open gap**, given a precise two-sub-case mechanism
     (self-bisection-only vs. genuine-signed-difference-derived participants) and a named crux
     analog (`aimo-0440`) to adapt for the sign-level argument the second sub-case needs.
Key lemmas (claim + mechanism):
  - Lone-`X`-Edge Reduction Lemma — because a single cross-tie forces every node to one value
    plus a self-bisection identity, which is exactly the Vertex Lemma's other breakpoint type.
  - Even-`\#X` Infeasibility Lemma — because pairwise-disjoint token supports make the combined
    closing-equation offset a genuine signed subset sum over ORIGINAL indices, and such a sum is
    provably never zero for a superincreasing sequence (exact fact, no magnitude bound needed).
  - Odd-`\#X\ge3` Domain-Violation Lemma (open) — because the closing equation gives a unique
    solution whose domain-violation, for derived participants, needs sign-level (not
    absolute-value) information about the token expansion, per the `aimo-0440` analog.
Open gaps: the Odd-`\#X\ge3` Domain-Violation Lemma (both all-original-mixed and any-derived
sub-cases) — this is now the single, precisely-isolated residual of the entire all-cycles gap.
Cases to cover: `\#X\in\{0,1\}$ (closed), `\#X\ge2` even (closed this round), `\#X\ge3` odd
(open); multiple simultaneous disjoint cycles need no separate handling (Opening 3,
re-confirmed exhaustive).
Watch out for: the general mixed-edge-pattern closing equation must be explicitly re-derived by
the builder (not assumed to extend automatically from the uniform-edge-type case that was
symbolically checked); the "shared-value edge" formalization is a slightly looser notion than
the strict tie-dependency-graph edge definition and is inherited, not re-derived, from round 7.

potential-weighting-upper-bound: revise
Target: `c(n)=2^n/(2^{n+1}-1)`, full theorem — this slug's role is the upper-bound direction
(Case (ii), Xiang Yu has a response achieving `e\le e_n\cdot S(a)` for any Liu Bang opening `a`),
now reduced by Slack Collapse to the single tight sub-case `k=m+1`, and by the chain-prefix
construction to proving `OPT(Y,p-1)=NC(Y,p-1)`.
Technique: strong induction on list size `p`, peeling the global max, via the telescoping
identity `e(y_1,\dots,y_p)=y_1-e(y_2,\dots,y_p)`; new this round, an explicit **mutual induction**
between the MIN-problem at gap 1 and a MAX-companion problem at gap 0.
Skeleton (new §10 added this round, appended at the end of the file):
  1. DELETE `y_1` branch: self-similar reduction, same gap, smaller `p` — proved, elementary.
  2. MATCH `y_1,y_j` branch: reduces to a same-gap `(p-1)`-instance, but NOT a fresh
     unconstrained one — the certified non-crossing inside/outside independence lemma forces
     `NC`'s recursive value to decompose independently, while `OPT`'s need not — **the open gap**.
  3. KEEP `y_1` branch: reduces exactly (via the same telescoping identity) to MAXIMIZING `e` on
     the residual at gap 0 — define `MAXOPT`/`MAXNC` companions and recurse the identical 3-way
     split on them.
  4. MAX-DELETE and MAX-KEEP branches close trivially (self-similar; Slack-Collapse-style
     gap`\le-1` triviality respectively) — leaving MAX-MATCH with the *same* obstruction as
     step 2, one gap level lower.
  5. State the Small-Gap Crossing-Domination Lemma as the single shared open lemma needed at
     both gap 0 and gap 1 — by KB extremal-principle + budget/pigeonhole-counting heuristic.
Key lemmas (claim + mechanism):
  - Telescoping Identity — because the peeled max stays the max of any final combined multiset
    from a selection on the rest (every matched difference `\le` the max).
  - MAX-companion's KEEP-branch triviality — because it reduces via the same telescoping trick to
    a gap`\le-1` MIN-problem, trivially `0` by the certified Slack Collapse mechanism.
  - Small-Gap Crossing-Domination Lemma (open) — because a crossing-improving configuration
    needs a chain of `\ge3` pairwise-crossing arcs whose minimal-improving-`p` threshold
    empirically grows as gap shrinks (gap 4→p=7, gap 3→p=8, gap 2/1→none found through p=9/10),
    conjecturally placing gap `\in\{0,1\}$ below every threshold the induction ever encounters.
Open gaps: the Small-Gap Crossing-Domination Lemma (the single item both the MIN-gap-1 and
MAX-gap-0 instances need) — with a concrete first step (hand-verify the smallest `p` where a
crossing configuration is combinatorially possible at gap 1) and a fallback induction order
(innermost-chord peeling, crux `aimo-0003`, with an explicit caution against regressing to the
dead "sorted-adjacency" conjecture).
Cases to cover: 6 branches (MIN-side DELETE/MATCH/KEEP at gap 1; MAX-side DELETE/MATCH/KEEP at
gap 0) — 4 closed, 2 (both MATCH branches) sharing the one open lemma.
Watch out for: do not silently treat the reduced MATCH-branch list as "just another same-gap
instance, apply IH" — this is the exact unsound step that reintroduces the already-refuted
general `OPT=NC` conjecture (round 7 dead end). The probabilistic/averaging idea is noted as an
alternative *sub-mechanism* for this same open lemma, not a separate route (see rationale above).

concavity-minimax-duality: revise
Target: `c(n)=2^n/(2^{n+1}-1)`, full theorem — this slug's role is an independent, alternative
route to the lower bound via a closed-form 1-Lipschitz certificate `g` (would not need
D/M-completeness at all if it worked).
Technique: weak-duality certificate method; new this round, a pairing/telescoping induction
attempt (primary) plus a Kraft-budget reformulation attempt (fallback) to prove the candidate
certificate `g^*`'s minimum-is-1 property for general `m`.
Skeleton (new §13 added this round, appended at the end of the file):
  1. Recap: `g^*` survived exhaustive BFS through `m=7` this round (new, one level beyond the
     file's own `m\le6`), minimum always exactly 1, achieved by a rich minimizer family.
  2. Structural lead: at exact minimizers, sorted `g^*`-values decompose into exactly-cancelling
     adjacent pairs plus one residual `=1` — the mechanistic explanation for why `g^*` works.
  3. Technique 1 (primary): induct on D/M-operation count, tracking how each `D`/`M` operation
     moves elements between `g^*`-dyadic-brackets, to show the "pairs-plus-residual-`\ge1`"
     structure is preserved throughout — generalizes the certified Superincreasing No-Early-Zero
     Lemma's token/parity mechanism from raw magnitudes to `g^*`-coarsened values.
  4. Technique 2 (fallback, independent): translate the Kraft-inequality weighted-decomposition
     mechanism of crux `aimo-0790` (bounding a subadditive sequence via its behavior at powers of
     2, extended via binary expansion) into this game's terms — genuinely different mechanism,
     not a rephrasing of technique 1.
Key lemmas (claim + mechanism):
  - Coarsened Alternating-Cancellation Lemma (open) — because dyadic-bracket coarsening produces
    adjacent-equal-`g^*`-value pairs that cancel exactly like raw duplicate pairs (Lemma P
    mechanism), and every D/M operation should preserve a "rich cancellation plus residual `\ge1`"
    invariant.
  - Kraft-Budget Reformulation Lemma (open, fallback) — because `g^*`'s pinning at powers of 2
    (certified Combined Theorem) has the same shape as a Kraft-style weighted decomposition of a
    subadditive sequence.
Open gaps: both lemmas above are unproved; technique 1's own case split (how a `D(x)` operation
that breaks one member of an already-cancelling pair should be handled; how an `M(x,y)`
operation's effect on brackets depends on where `x,y,x-y` land) is not yet enumerated — the
concrete next task.
Cases to cover: none additional beyond the D/M-operation case split above.
Watch out for: do not count another brute-force BFS extension (e.g. `m=8`) as progress on its
own — the concrete next step is the inductive argument, not more exhaustive numerics.

---

Nominate all three for the build set (advance/revise, no new slug): `dyadic-cascade-induction`,
`potential-weighting-upper-bound`, `concavity-minimax-duality`. `elementary-exchange-smoothing`
remains retired (no action, per standing memory rule).

build set: dyadic-cascade-induction, potential-weighting-upper-bound, concavity-minimax-duality
