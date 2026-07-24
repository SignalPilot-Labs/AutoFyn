# proof-builder report — sunflower-inadmissibility-toolkit, round 12

## Outcome: Status stays `partial` for the whole problem, but a real
previously-open sub-target (Backbone Permanence) is now FULLY CLOSED,
unconditionally — not the round's expected "modulo one open lemma" state.

## What was done
Read the round-12 outline (already at top of
`results/imo-2026-06/approaches/sunflower-inadmissibility-toolkit.md`),
the outline-reviewer's independent verification
(`/tmp/round-12/outline-reviewer.md`, which APPROVEd this outline and
independently reproduced the backbone data to N=60000 on a_1=2747 and
on a_1=21528751), and the jw-rigidity math-explorer's report
(`/tmp/round-12/math-explorer-jw-rigidity.md`, Finding 2, source of the
"Case A" mechanism).

The outline's Step 2 ("Backbone Permanence Lemma") was dispatched as
open, hard content requiring adaptation of the certified single-family
Escape-Confinement/Permanent-Inadmissibility toolkit. On inspection, it
is instead a direct corollary of the outline's own Step 1
finite-descent argument, PROPERLY applied to the entire (infinite)
index class I_{S'} rather than described loosely as "stabilizes in the
tested range": a monotone non-increasing sequence of subsets of a fixed
finite set is eventually constant, full stop, regardless of how many
terms the sequence has — this gives both stabilization AND that the
stabilized value equals the TRUE class-wide intersection, with zero
additional machinery.

Proved this rigorously as **Lemma BS (Backbone Stabilization)** (§6),
combined it via the already-certified Lemma ERD-C into a clean
**Lemma BS-Dichotomy** (§7, "Case A" vs "Case B" now a provable
dichotomy, not an empirical classification), and assembled with the
already-certified Lemma UCR into **Theorem CAC (Case A Closure)** (§8):
a complete, unconditional proof of Conjecture (JW) for every Case A
pair, over the FULL infinite index classes (not a tested prefix — the
overclaim hazard already flagged in `lemmas/lemma-UCR-universal-class-
realization.md`'s scope note was explicitly checked against and avoided,
see §6's dedicated remark).

Independently re-verified 4 of the 5 previously-listed Case A instances
from scratch with a fresh literal-rule generator (own Python + sympy,
not any prior round's script): a_1=2747 (41,67), a_1=4087 (61,67),
a_1=4199 (13,19) and (17,19) (shared witness a_11). Relied on the
outline-reviewer's own this-round independent verification for the 5th,
hardest instance (a_1=21528751), which already constitutes a
from-scratch re-derivation this round.

## Certified this round
- Lemma BS (Backbone Stabilization) — general, unconditional, reusable.
- Lemma BS-Dichotomy — elementary corollary of Lemma ERD-C.
- Theorem CAC (Case A Closure of Conjecture (JW)) — general, unconditional.

All three added to the Promotable lemmas section for reviewer
certification into `results/imo-2026-06/lemmas/`.

## What remains open
Case B pairs (247:(13,19), 4199:(13,17)) — explicitly out of scope for
this approach, ceded to sunflower-bundle-closure / forced-primes-well-
ordering per the outline-reviewer's round-12 scoping. The rest of the
Stabilization Conjecture (whether every doubly-infinite pair of every
a_1 is Case A) remains open — no general criterion for deciding this in
advance was found or claimed.

File updated in place:
results/imo-2026-06/approaches/sunflower-inadmissibility-toolkit.md
(Status: partial)
