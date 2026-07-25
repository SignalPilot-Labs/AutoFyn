# Proof-builder report — redundant-constraint-antichain (Round 5, consolidation)

**Status: partial (unchanged, correct — NOT overclaimed).**

## What I did
Consolidation only, per dispatch. No new E5″ lever exists (confirmed by both R5 explorers and the
outline-reviewer, which kept this approach LIVE as certified furthest-forward, not because a lever
was found). Edits to `results/imo-2026-06/approaches/redundant-constraint-antichain.md`:

1. **§13.1 — certified reduction chain in one table.** No-transient ⇒ E1/E2/E3 ⇒ Crux ⇔ E4
   (cardinality) ⇒ R1/R2 ⇒ Prop 12.A (regime `∏G<a₁` fully closed) / Prop 12.B (window (W)) ⇒ single
   open arrow **E5″**. Every link certified in `lemmas/` except `E5″ ⟹ E5`. The whole theorem is
   certified-equivalent to E5″.
2. **§13.2 — two-anchor witness scaffold (NEW, auxiliary).** Cross-references the sibling slug
   `realizer-index-joint-double-count`. If `𝓐_∞` infinite and `a₁` not a prime power: an anchored
   subfamily `G_k∋p*` with `q_k=p_max(G_k)→∞` has E3 private witnesses `H_k` (`G_k∩H_k={q_k}`) forced
   by Anchor+Pigeonhole to carry a SECOND fixed anchor `p**∈P∖{p*}`. Proved in full from certified
   lemmas. Recorded as reusable structure and **promotable**; explicitly NOT a closer of E5″.
3. **Honest guardrail (§13.2/§13.3).** The joint-spread "Lemma J" is illusory:
   `t_k−t'_k = q_k·(A_k−B_k)` with `A_k,B_k` products of DISJOINT prime sets ⇒ `|A_k−B_k|≥1` ⇒ any
   `|t_k−t'_k|≤C(a₁)` gives `q_k≤C(a₁)`. So bounding the witness-pair spread IS the magnitude bound —
   no decoupling. Companion guardrail to the R4 Collapse.
4. **§13.3 — R5 negative findings recorded.** Formation-window route forks to the R4-forbidden
   sub-support-realization move or an unresolved simultaneous-timing claim; density/covering route is
   the certified dead end (obstruction family); joint-spread is illusory. Numeric-only conjecture
   ("at most one prime `>√a₁` per large-regime support") recorded as CONJECTURE, unproved, a sharper
   restatement of the wall not a bypass.
5. Updated `## Approaches tried` (R5 entry) and `## Current best` (R5 status paragraph). Status stays
   `partial`.

## Promotable (for reviewer certification)
- **Two-anchor witness scaffold (S2)** — auxiliary structure lemma (§13.2), from certified E3 +
  Anchor + Pigeonhole; plus the unique-factorization guardrail `t−t'=q(A−B)`.

## Spec concerns
None. The reduction chain is internally consistent; every link but `E5″ ⟹ E5` is certified; the
§4–§5 endgame delivers exactly the problem's periodicity claim (`a_{n+T}=a_n+L` for all `n≥1`,
`T=|ρ(A)|`, `L=∏Π`). E5″ is the single honest open gap.

## Assessment (plain)
Beyond consolidation and the two-anchor scaffold, I have nothing rigorous to ADD to E5″ this round —
and I say so plainly, as instructed. The field is on a hard plateau: the E5″ wall is structural
across all five framings tried. Recommend the orchestrator seed a fundamentally new TOP-LEVEL route
(not another E5″/∏G/|t−t'| lever, all of which share the wall) next round.
