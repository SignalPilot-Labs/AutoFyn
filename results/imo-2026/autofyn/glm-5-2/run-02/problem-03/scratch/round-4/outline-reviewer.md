## imo-2026-03 — outline-reviewer report (round 4)

Re-derived the two load-bearing claims from the explorer reports before gating.

### Claim re-check 1: Is the cell-complex route really free of the `−2T` wall?

YES (re-derived from `math-explorer-variational-lower.md` §4). The `−2T` tail-flip term (`lemmas/lemma-delta-a-local-cut.md`) arises ONLY when `A` is decomposed into per-mark local cuts — each mark's contribution carries a `±T` tail-parity term, and the tails ADD destructively across marks. The cell-complex route treats `A` as ONE piecewise-linear function of the full mark-vector; there is no "tail of mark i" to add to "tail of mark j." Rank-shifts are absorbed into the cell structure (crossing a cell boundary changes the sort, and `A`'s formula on the new cell is a different linear form — no additive tail). So the residual Hall Match / `e_M ≤ o_R` inequality is a decomposition artifact, absent in the undecomposed function. The escape is structural, not verbal.

### Claim re-check 2: Are `equality-case-classification` and `two-regime-disjunctive` the same wall?

YES on G2 — they share the load-bearing fact. Both need the real-valued equality-case classification (`A = α(n)` iff odd-mult leftover is `{1}` or `{2^j, 2^j+1}`) lifted from grid-empirical to reals, AND both need the same sliver-forcing converse (`A < α` not `A > α` for non-dyadic Liu). The outliner's own honest caveat confirms: equality-case's G2 half "is (U-E)'s global statement restated" — i.e., the same wall two-regime faces. The divergence the outliner names ("drops the regime split, attacks both gaps") is a difference in SCOPE, not in the load-bearing mechanism: the hard step is the identical classification-lift + sliver-forcing. If that wall fails, both die on G2 together. Additionally, equality-case's G1 half (the flat-polytope equality locus) is the SAME mechanism cell-complex-l3 leans on — so equality-case is the *union* of two existing walls (two-regime's G2 + cell-complex's G1 equality locus), not an independent route. Per CLAUDE.md's strict single-gap-trap rule, keep the sharper owner of each wall and RETHINK the union.

---

### `pairing-partner` — APPROVE (advance)

The live leader (Elo 1544, `advanced` last round). Framing UNCHANGED — pair-excess + `M⊎R` + Hall matching on the merged sort. The hard step is honest: the residual (Match) `Σ_MM m_even ≤ Σ_RR r_odd` over reals, via the superincreasing-R lever (crux `aimo-0019`: "bound dyadic-length distinct-size pieces by twice the largest via geometric sum"). The outline correctly flags that the Hall matching is on RANK INDICES, not piece sizes (the `MM` smaller halves are not ordered by R-level) — this is the genuine difficulty, and it is not hidden.

- Sound skeleton? Yes — Lemma G, `e_M ≤ o_R` reduction, self-compensation, `M⊎R` identity all certified; the open gap (residual Match over reals) is the explicit, localized target.
- Load-bearing lemma WITH mechanism? Yes — "each `m_even` sits below a distinct dyadic level of R, so a distinct `r_odd` dominates it" (aimo-0019 geometric-sum `< 2·largest`). Mechanism named; the hard step is proving the injective matching on rank indices actually realizes this. Honest.
- Avoids dead ends? Yes — explicitly does NOT retry Engine A (two-tail cancellation, falsified) or per-mark induction (`−2T`).
- Whole attempt? Yes — targets `c(n)=f(n)` end-to-end (G1 owned, G2 imported from sibling).
- Cases? even-count minimizers (pair-pile, (Match) saturates), odd-count (CK + (S)). The (S) conjecture is correctly flagged as FALSE for reals.

APPROVE to advance. Build target: close the residual (Match) via the superincreasing-R lever, OR honestly bound the obstruction tighter if the lever doesn't adapt.

### `two-regime-disjunctive` — APPROVE (revise)

The new regime-N engine (structural equality-case classification) is genuinely different from the dead R-pile: R-pile was a CONSTRUCTIVE greedy strategy (cut `a_2` out of `a_1` recursively); the new engine is a CLASSIFICATION + CONTRAPOSITIVE argument (equality structure is dyadic-Liu-locked ⇒ non-dyadic forces `A < α`). Not a rename — a different mechanism class.

- Sound skeleton? Yes — regime D (pair-pile, certified all n), regime N (classification + sliver forcing, open). U(1)/U(2)/dyadic-ratio all certified.
- Load-bearing lemma WITH mechanism? Yes — "the `{2^j,2^j+1}` consecutive-powers pair requires adjacent Liu pieces in exact ratio `2^j:2^{j+1}`, recursively" (dyadic-Liu-locked); "non-dyadic ⇒ sliver forces `A < α`" (generalized U(1)/U(2) sliver). Mechanisms named; the hard step (real-valued sliver landing at a canceling odd rank for EVERY non-dyadic config) is the honest wall.
- Honest about the wall? Yes — "grid census empirical only; no proof technique visible." Does NOT claim classification alone closes G2 (the SIDE argument `A < α` not `A > α` needs sliver forcing, flagged). Does NOT import (U-E) as closure.
- Avoids dead ends? Yes — explicitly does NOT reuse R-pile (falsified, 3 counterexample classes), does NOT retry `M−total(R)=α(n+1)` (dyadic-only, foreclosed A4).
- Whole attempt? Yes — targets `c(n)=f(n)` end-to-end (G2 owned, G1 imported).

APPROVE to revise. Build target: develop the classification-lift + sliver-forcing engine; the G2 wall is honest but the framing is sound.

### `cell-complex-l3` — APPROVE (new, register)

Genuinely far from the pair-excess/Hall field (Claim re-check 1 above). Treats `A` as one piecewise-linear function on the mark-simplex; the `−2T`/Hall obstruction is a decomposition artifact, absent here. The n=3 milestone is concrete and finite: ~6 hyperplanes, ~20 feasible arrangement vertices, exact-rational vertex check. This is the cheapest real-valued `n≥3` lower-bound foothold not yet in hand.

- Sound skeleton? Yes — piecewise-linearity per cell (mechanism: sorted-order sign assignment constant per cell); global min = min over arrangement vertices + flat-cell accounting (mechanism: linear form on a polytope attains min at a vertex); flat facets = sliver-canceling locus (mechanism: certified n=1 `±a` generalized).
- Honest about the FACET issue? Yes — the minimizer is a positive-dimensional flat polytope, NOT a unique vertex (Explorer 1, verified n=3,4,5). The outline correctly flags that the vertex check alone does NOT close L(3); the flat-cell characterization + transverse monotonicity (step 4) is needed. This is the honest hard step at n=3; it is finite and cheap (20/20 directions verified numerically).
- Avoids dead ends? Yes — no per-mark decomposition, no `−2T`, no Hall. The "unique minimizer ⇒ symmetry" argument is correctly flagged as NOT firing (minimizer is degenerate).
- Whole attempt? Yes — top-level target is `c(n)=f(n)` end-to-end (G1 owned via cell-complex, G2 imported); the n=3 milestone is the first concrete foothold, with the general-n inductive lift honestly flagged as a distant wall.
- Cases? flat cells (`A=α(3)`), non-flat adjacent cells (transverse increase), degenerate vertex cells (piece=0). Disjoint and exhaustive at n=3.
- Shared-wall risk with equality-case-classification? Flagged honestly. But cell-complex's n=3 milestone is a FINITE certificate per n, independent of whether the all-n structural theorem (equality-case's target) lifts. So the divergence is real: cell-complex could succeed at n=3 while equality-case fails at general n. (See RETHINK of equality-case below.)

APPROVE and register. Build target: the n=3 vertex enumeration + flat-cell characterization (the cheap finite milestone). The general-n lift is a distant goal — do not block the n=3 foothold on it.

### `equality-case-classification` — RETHINK

The single-gap-trap risk the dispatch flagged is REAL. This approach is the *union* of two existing walls, not an independent route:

1. **G2 wall shared with `two-regime-disjunctive`**: both need the real-valued equality-case classification lifted from grid-empirical to reals, AND the same sliver-forcing converse. The outliner's own caveat confirms the G2 half "is (U-E)'s global statement restated" — identical to two-regime's hard step. If the classification fails to lift, the G2 half here AND two-regime's regime-N engine die together.
2. **G1 wall shared with `cell-complex-l3`**: both lean on the sliver-canceling flat polytope as the equality locus. The outliner flags this honestly.

The divergences the outliner names are differences in SCOPE (attacks both gaps vs G2-only; all-n structural theorem vs finite cert per n), not differences in the load-bearing mechanism. The hard step is the same classification-lift + sliver-forcing on both sides. CLAUDE.md's rule is strict here: "Approaches that only differ in technique hit the same wall and fail together." equality-case-classification shares the G2 wall with two-regime AND the G1 flat-polytope wall with cell-complex — it is the most-overlapping approach in the field.

**Why not keep it as the "ambitious unifier"?** If the classification theorem is the real heart of the problem, it should be developed AS a shared lemma within the G2-owner (`two-regime-disjunctive`, where it's the regime-N engine) and/or the G1-owner (`cell-complex-l3`, where it's the flat-polytope characterization) — NOT as a standalone approach that dies if either of two walls fails. A standalone approach must own an independent route; this one owns the union of two shared walls.

**Direction for the outliner:** re-plan `equality-case-classification` to either (a) become a genuinely independent route (e.g., attack G2 via a mechanism NOT based on the equality-case classification — a different framing of the non-dyadic upper bound), or (b) dissolve into the shared lemma cache (the classification theorem becomes a `lemmas/` entry certified by whichever approach proves it first, imported by the others). Do NOT re-propose it as a standalone unifier that shares both walls.

Not registered. Not in the build set.

### `pairing-partner-transfer` — RETIRE (confirmed)

Engine A (two-tail cancellation) FALSIFIED on n=3 brute force (21/33 k≥2 minimizers admit no single-pair transfer; the two `ΔA` tails ADD, same `−2T` wall as per-mark induction). The approach is a near-twin of `pairing-partner` (same pair-excess/`M⊎R` framing, same gap G1) with NO live engine. Its certified contribution (CK odd-count lemma) is already in the shared lemma cache (`lemmas/lemma-ck-odd-count.md`) and survives retirement.

- Not registered (already in population).
- Not advanced, not in the build set. Let it sink in the ranking — it has no live engine.
- Do NOT re-conceive as another per-mark/transfer variant (ruled out) or as a unified Mersenne/`Ψ=1/A` potential (foreclosed, A4).

Retired. Recorded.

---

### Diversity / single-gap-trap assessment of the surviving field

- **G1 has two genuinely independent framings**: `pairing-partner` (per-mark pair-excess decomposition + Hall matching on merged sort) and `cell-complex-l3` (undecomposed variational cell enumeration). They do NOT share a wall — the `−2T`/Hall obstruction is a decomposition artifact absent in the variational view (Claim re-check 1). This is the honest terrain.
- **G2 has one owner**: `two-regime-disjunctive` (disjunctive regime split + classification/sliver engine). The G2 wall (real-valued sliver forcing) is honest and no proof technique is visible; this is the field's hardest open wall. The RETHINK of equality-case-classification leaves G2 with a single owner — but that one owner is the only approach NOT sharing the G2 wall, so this is the correct concentration. The outliner should be told: if G2 stalls next round, open a G2 approach with a DIFFERENT framing of the non-dyadic upper bound (NOT the equality-case classification — that's the shared wall), e.g. a direct sliver-construction family per non-dyadic structural class, or a 2-adic-valuation framing (crux `aimo-0225`/`aimo-0093`).
- **The retired `pairing-partner-transfer` and the dead `induct-one-mark`** are not in the build set; they sink in the ranking.

---

### Ranking (head-to-head, anchored to last outcomes)

- `pairing-partner` (advanced, partial, leader) — most certified progress, sound framing, concrete borrowed crux (aimo-0019) for the gap. Leader.
- `cell-complex-l3` (new, cold-start 1500) — sharp new framing, genuinely escapes `−2T`, concrete finite n=3 milestone. Ranked ABOVE the stuck `two-regime-disjunctive` per the dispatch's "rank a sharp new framing above a stuck old one" guidance, but BELOW `pairing-partner` (which has more certified territory and isn't stuck).
- `two-regime-disjunctive` (partial, engine replaced) — re-planned (R-pile dead, new engine unproven), G2 wall has no visible proof technique. Below cell-complex (closer to a concrete foothold) but above the dead approaches (still owns G2 with certified U(1)/U(2)/dyadic-ratio).
- `pairing-partner-transfer` (dead-end, retired) — below all live approaches.
- `induct-one-mark` (partial, dead central route) — below all live approaches.

Comparisons issued: pairing-partner > cell-complex; cell-complex > two-regime-disjunctive; pairing-partner > two-regime-disjunctive; two-regime-disjunctive > pairing-partner-transfer; two-regime-disjunctive > induct-one-mark; cell-complex > pairing-partner-transfer; cell-complex > induct-one-mark; pairing-partner > pairing-partner-transfer; pairing-partner > induct-one-mark; pairing-partner-transfer > induct-one-mark (inherited-twin with certified CK contribution vs dead central route).

---

build set: pairing-partner, cell-complex-l3, two-regime-disjunctive
