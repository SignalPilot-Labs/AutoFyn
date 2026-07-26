## imo-2026-03

**`pairing-partner`**: advance
Target: `c(n) = f(n)` end-to-end; owns G1 (Lemma L general-n, `k ≥ 2` reals),
localized to `e_M ≤ o_R` ⟺ residual Hall-type `(Match) Σ_MM m_even ≤ Σ_RR r_odd`. G2 imported.
Technique: pair-excess decomposition + `M ⊎ R` self-similar decomposition +
Hall matching on the merged sort (framing UNCHANGED — the live handle).
Skeleton:
  1. Import Lemma G, `e_M ≤ o_R` reduction, self-compensation, `M ⊎ R` identity, grid-parity (grid-only), n=1 `±a` — all certified.
  2. GAP: prove the residual (Match) over reals via the superincreasing-R lever (crux aimo-0019, "bound dyadic-length distinct-size pieces by twice the largest via geometric sum"). Each `MM` smaller half `m_even ≤ R_largest = M/2`; `R`-pieces superincreasing (`2^j > Σ_{i<j} 2^i`); build an injective Hall matching on RANK INDICES in the merged sort.
  3. Equality case `Σ_MM m_even = Σ_RR r_odd` ⟺ pair-pile/mirror (odd-mult `{1}` / `{2^j, 2^j+1}` census).
  4. Conclude `L(n+1) ⟹ L(n)` all `n` (induction); `c(n) ≥ f(n)`. G2 from sibling.
Key lemmas:
  - (Match) holds — because each `m_even` sits below a distinct dyadic level of R, so a distinct `r_odd` dominates it (aimo-0019 geometric-sum `< 2·largest` template).
  - Equality ⟺ pair-pile/mirror — the census's odd-mult `{1}` / `{2^j, 2^j+1}` invariant.
Open gaps: step 2 (real-valued Hall matching via superincreasing R — the hard step; grid-parity proves grid only, does NOT lift); step 3 (real equality-case characterization — shared-wall with `equality-case-classification`).
Cases: even-count minimizers (pair-pile type — (Match) saturates), odd-count (CK + (S)).
Watch out for: the `MM` smaller halves are NOT ordered by R-level in any obvious way — the Hall matching is on RANK INDICES, not piece sizes. Do NOT retry Engine A (two-tail cancellation, falsified).

**`two-regime-disjunctive`**: revise
Target: `c(n) = f(n)` end-to-end; owns G2 (regime-N: every non-dyadic Liu config, Xiang forces `A < α(n)`). G1 imported.
Technique: disjunctive dyadic/non-dyadic regime split (regime D = pair-pile, certified; regime N — REPLACE the FALSIFIED R-pile greedy with the structural equality-case classification as the new regime-N engine).
Skeleton:
  1. Import Lemma G, pair-pile + mirror (regime D, all n), U(2) four-strategy (`Φ_2 = min(a, b−a, c−b, |2c−1|)`, max uniquely at dyadic), dyadic-ratio overshoot (dyadic detection).
  2. GAP: lift the grid equality-case classification (odd-mult `{1}` / `{2^j, 2^j+1}`, `A·D(n)=1`) to a real-valued regime-N forcing. Prove the equality structure is dyadic-Liu-locked (realizable as `A=α` only when Liu is dyadic — adjacent Liu pieces must be in exact ratio `2^j:2^{j+1}`, recursively). For non-dyadic Liu, Xiang's sliver (generalizing U(1)/U(2)) shaves the would-be-equal pair into a sliver + complement, sliver landing at a canceling odd rank ⇒ `A < α(n)`.
  3. Regime-D/regime-N disjunction exhaustive (dyadic vs not); regime D = pair-pile (equality), regime N = strict `< α`.
  4. Conclude `c(n) ≤ f(n)`, equality iff dyadic. G1 from sibling.
Key lemmas:
  - Equality structure is dyadic-Liu-locked — the `{2^j, 2^j+1}` consecutive-powers pair requires exact dyadic ratios at every level.
  - Non-dyadic ⇒ sliver forces `A < α` — a non-dyadic Liu ratio leaves a non-cancellable residual at the would-be-pair rank; Xiang's sliver shaves it below `α(n)` (certified n=1 `±a` mechanism generalized).
Open gaps: step 2 (real-valued non-dyadic sliver forcing — the honest wall; grid census empirical only; numerically robust 1200-config n=3 scan, max `Φ=0.0595 < α(3)`, but no proof technique visible).
Cases: balanced non-dyadic (`A→0`), dominant-non-dyadic (sliver shaves dominant piece's partner), extreme-dominant tiny-tail (R-pile's failure class — sliver forcing must handle these).
Watch out for: do NOT reuse R-pile greedy (falsified, 3 counterexample classes). Do NOT claim classification alone closes G2 (gives `A ≠ α`, but SIDE `A < α` needs sliver forcing). (U-E) restates this gap — do NOT import as closure. `M − total(R) = α(n+1)` is dyadic-only (foreclosed).

**`cell-complex-l3`**: new
Target: `c(n) = f(n)` end-to-end; owns G1 via the variational cell-complex route. FIRST milestone: `L(3)` for reals (the first real-`n≥3` lower-bound foothold). G2 imported. General-`n` inductive lift is a DISTANT goal.
Technique: treat `A` as ONE piecewise-linear function of the Xiang mark-vector on the simplex; cell-by-cell lower bound on the natural hyperplane arrangement `H = {x_i = l_j} ∪ {x_i = x_k}`. NO per-mark decomposition, NO `e_M ≤ o_R`, NO Hall matching (decomposition artifacts absent in the undecomposed function). Escapes the certified `−2T` tail-flip wall.
Skeleton:
  1. Import Lemma G, mirror cap (one minimizer), n=1 real `±a` (base case for flat-cell characterization).
  2. Set up arrangement H for n=3 (Liu marks at `(1,3,7)/15`; ~6 hyperplanes). Enumerate feasible cells/vertices.
  3. GAP (cheap finite certificate — the n=3 milestone): at every feasible arrangement vertex, compute limiting (degenerate-multiset) `A`, verify `≥ α(3)=1/15`. Finite (~20 feasible vertices).
  4. GAP (flat-cell monotonicity): characterize flat cells = sliver-canceling locus (generalized `±a`); prove `A=α(3)` on them, `A` strictly increasing transversally off them (n=3 verified 20/20). Then `A ≥ α(3)` on every cell by linearity + vertex check + flat-cell accounting.
  5. Conclude `L(3)` for reals: `min_x A = α(3)`, `c(3) ≥ f(3)`.
  6. (DISTANT) GAP: inductive cell-complex lift to general `n` via `M ⊎ R` self-similarity + aimo-0261 (local exchange forces extremum onto symmetric locus, then recurse `D(n+1)=2D(n)+1`).
Key lemmas:
  - `A` piecewise-linear in mark-vector — sorted-order sign assignment constant per cell.
  - Global `min A = min over arrangement vertices` — linear form on a polytope attains min at a vertex; flat cells contribute `A=α`.
  - Flat facets = sliver-canceling locus — the certified n=1 `±a` mechanism generalized.
Open gaps: step 3 (n=3 vertex enumeration — cheap finite certificate, the concrete milestone); step 4 (flat-cell characterization + transverse monotonicity at n=3 — needed because minimizer is a FACET not a vertex); step 6 (inductive lift to general n — distant hard wall).
Cases: flat cells (`A=α(3)`), non-flat adjacent cells (transverse increase), degenerate vertex cells (piece=0).
Watch out for: minimizer is a positive-dimensional flat polytope, NOT a unique vertex — "unique minimizer ⇒ symmetry" does NOT fire. `A` NOT globally convex (no smoothing). Arrangement exponential in `n` (n=3 finite; general-n lift is the wall). Shared-wall with `equality-case-classification` (both lean on the sliver-canceling flat polytope) — divergence: this bounds a linear form per polytope (finite cert per n); equality-case aims for a structural theorem at all n directly.

**`equality-case-classification`**: new
Target: `c(n) = f(n)` end-to-end, via ONE structural classification theorem attacking BOTH gaps.
Technique: classify over REALS exactly when `A = α(n)` (the equality-case invariant: odd-mult pieces form `{1}` (mirror family) or `{2^j, 2^j+1}` (pair-pile family), `A·D(n)=1`); read off G1 (`A ≥ α` for every Xiang refinement of the dyadic) and G2 (equality is dyadic-Liu-locked ⇒ non-dyadic forces `A < α`) from the classification. Genuinely far from pair-excess/Hall and from regime/pile.
Skeleton:
  1. Import Lemma G, pair-pile + mirror (the two certified equality realizations), n=1 `±a`, minimizer census (grid-empirical, n=3,4,5).
  2. GAP (load-bearing): prove the REAL-VALUED equality-case classification — `A = α(n)` iff odd-mult leftover is `{1}` or `{2^j, 2^j+1}`. Mechanism: the sliver-canceling `±a` flat polytope IS the real form of the odd-mult leftover = dyadic-unit (so the classification = the flat-polytope characterization, shared with `cell-complex-l3`).
  3. G1 closure: every real Xiang refinement of the dyadic has `A ≥ α(n)`; equality iff it realizes the classified structure; off the flat polytope `A` strictly increasing transversally (dyadic's superincreasing R forces non-canceling leftovers to exceed the dyadic-unit).
  4. GAP (the G2 wall, honest): prove equality is dyadic-Liu-locked (`A = α` realizable only when Liu is dyadic — adjacent pieces in exact ratio `2^j:2^{j+1}` recursively). Then for non-dyadic Liu, Xiang's sliver forces `A < α`. HONEST CAVEAT: this G2 half is (U-E)'s global statement restated (Explorer 2 confirmed (U-E)'s global half IS G2 verbatim); the classification gives `A ≠ α` off the dyadic but the SIDE (`A < α` not `A > α`) needs the sliver forcing, NOT supplied by classification alone — does NOT trivialize G2.
  5. Conclude `c(n) = f(n)`: G1 from step 3, G2 from step 4 (sliver forcing as open sub-step).
Key lemmas:
  - Real equality-case classification — `A = α` iff odd-mult leftover is `{1}`/`{2^j,2^j+1}`, because the sliver-canceling flat polytope is the real form of the odd-mult leftover = dyadic-unit.
  - G1: non-equality ⇒ `A > α` — off the flat polytope `A` strictly increasing transversally (superincreasing R).
  - G2 (hard wall): equality is dyadic-Liu-locked — the `{2^j, 2^j+1}` pair requires exact dyadic Liu ratios recursively.
Open gaps: step 2 (real equality-case classification — load-bearing, grid-empirical only); step 4 (G2 sliver forcing from the classification's converse — the honest wall, (U-E) restated); the SIDE argument (why `A < α` not `A > α` off the dyadic — shared with `two-regime-disjunctive`).
Cases: odd-count minimizers (`{1}`) and even-count minimizers (`{2^j, 2^j+1}`) both must fall out of the real classification; non-dyadic Liu of every structural class (balanced, dominant, extreme-dominant).
Watch out for: shared-wall with `cell-complex-l3` (both lean on the sliver-canceling flat polytope as equality locus — if real characterization fails, both die together; divergence: structural theorem at all n vs finite cert per n). shared-wall with `two-regime-disjunctive` (both use the equality-case classification for G2 — if real classification fails to lift, the G2 half here AND `two-regime-disjunctive`'s regime-N engine die together; divergence: this drops the regime split and attacks both gaps from one classification, `two-regime-disjunctive` stays within the disjunctive split, G2 only). Do NOT claim classification alone closes G2 (SIDE needs sliver forcing). `M − total(R) = α(n+1)` dyadic-only (foreclosed).

**`pairing-partner-transfer`**: retire
Verdict: RETIRE (do NOT dispatch a builder). Engine A (two-tail cancellation) FALSIFIED on n=3 brute force (21/33 k≥2 minimizers admit no single-pair transfer; the two `ΔA` tails ADD — same certified `−2T` wall as per-mark induction). The approach is a near-twin of `pairing-partner` (same pair-excess/`M⊎R` framing, same gap G1) with NO live engine. Its certified contribution (CK odd-count lemma) is already shared across the population and survives retirement. Do NOT re-conceive as another per-mark/transfer variant (ruled out) or as a unified Mersenne/`Ψ=1/A` potential (foreclosed, A4). Flagged for the outline-reviewer to DROP from the live field.

---

### field:
- `pairing-partner` — advance — close the residual Hall (Match) `Σ_MM m_even ≤ Σ_RR r_odd` over reals via the superincreasing-R lever (crux aimo-0019). Hard step: the injective Hall matching on RANK INDICES in the merged sort (grid-parity proves grid only, does NOT lift).
- `two-regime-disjunctive` — revise — replace the falsified R-pile with the structural equality-case classification as the new regime-N engine; prove equality structure is dyadic-Liu-locked ⇒ non-dyadic forces `A < α` via sliver. Hard step: real-valued non-dyadic sliver forcing (grid census empirical only; (U-E) restates the gap, does NOT bypass).
- `cell-complex-l3` — new — close `L(3)` for reals by n=3 cell/vertex enumeration of `A` as one piecewise-linear function on the mark-simplex (no decomposition, escapes `−2T`). Hard step: flat-cell characterization + transverse monotonicity at n=3 (minimizer is a FACET, not a vertex); general-n inductive lift is the distant wall.
- `equality-case-classification` — new — attack BOTH gaps via the real-valued equality-case classification (odd-mult `{1}` / `{2^j, 2^j+1}` invariant). Hard step: real equality-case classification (= flat-polytope characterization); G2 half is the (U-E) wall restated, does NOT trivialize.
- `pairing-partner-transfer` — retire — Engine A falsified (same `−2T` wall), near-twin of `pairing-partner` with no live engine; CK lemma already shared. Drop from the live field.

### Diversity / single-gap-trap check (honest)
- `pairing-partner` (pair-excess + Hall) and `cell-complex-l3` (undecomposed variational) are GENUINELY different framings of G1 (one decomposes `A` into per-mark pair-excesses and chases the residual Match; the other treats `A` as one piecewise-linear function with no decomposition). They do NOT share a wall — the `−2T`/Hall obstruction is a decomposition artifact absent in the variational view.
- `cell-complex-l3` and `equality-case-classification` SHARE the sliver-canceling flat polytope as the equality locus — a genuine single-gap-trap risk, flagged in both skeletons. Divergence: cell-complex bounds a linear form per polytope (finite cert per n); equality-case aims for a structural theorem at all n. If the real flat-polytope characterization fails, both die together; the outline-reviewer should rank them with this in mind.
- `equality-case-classification` and `two-regime-disjunctive` SHARE the equality-case classification as a load-bearing fact for G2 — a second single-gap-trap risk, flagged. Divergence: equality-case drops the regime split (attacks both gaps from one classification); two-regime-disjunctive stays within the disjunctive split (G2 only, G1 imported). If the real classification fails to lift, the G2 half of equality-case AND two-regime-disjunctive's regime-N engine die together.
- Net: the field has one genuinely-independent G1 framing pair (pairing-partner vs cell-complex) and one genuinely-independent G2 framing pair (two-regime-disjunctive's disjunctive split vs equality-case's unified classification), with two shared-wall risks explicitly flagged for the reviewer. This is the honest terrain; the cell-complex n=3 milestone is the cheapest new foothold, and the superincreasing-R lever on pairing-partner is the cheapest G1 advance.
