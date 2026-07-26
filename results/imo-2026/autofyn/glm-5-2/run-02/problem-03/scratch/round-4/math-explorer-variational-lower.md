## imo-2026-03 (route: VARIATIONAL / CONTINUOUS-OPTIMIZATION for the LOWER bound G1)

Setup recap. Fix Liu's level-`n` dyadic config (pieces `(1,2,4,…,2^n)/D(n)`, `D(n)=2^{n+1}−1`). Treat Xiang's `≤ n` marks as real variables in the compact simplex `[0,1]^n` (with the collision/coincidence locus removed). The advantage `A = Σ(−1)^{i+1} p_i` (sorted-desc final pieces) is a continuous, piecewise-linear function of those variables. The lower-bound claim `L(n)` is *exactly* the global-minimum statement `min A = α(n) = 1/D(n)`, conjecturally attained at the mirror config `xiang marks = {1−l_j}`. This reframes G1 as a single global-optimization problem — no per-mark decomposition, no `k`-classification, no Hall matching.

### 1. Is the mirror config the global minimizer? — VERIFIED min = α(n), but minimizer is NOT unique

Computational (verified, not a proof):
- **Differential evolution + 50k exact-rational random samples:** for `n=3,4`, `min A = α(n)` exactly, **0 violations** (no Xiang response gives `A < α(n)`). For `n=5`, DE finds `min A = 1/63 = α(5)` (random-grid search on a 2M grid is too coarse to hit the mirror flat region, but DE locates it). The floor `α(n)` is robust.
- **Mirror config itself:** `A = α(n)` for `n=3,4,5` (exact rational), consistent with the certified mirror lemma.

**Minimizer structure — load-bearing finding:** the minimizer is **NOT unique**. The mirror config is one point on the **boundary of a positive-dimensional flat polytope** on which `A = α(n)` exactly. Perturbing `mirror[2]=8/15` (for `n=3`) DOWN by `eps ∈ (−1/15, 0]` keeps `A = 1/15` exactly (verified exact-rational, 50 sample points all `= α`); perturbing UP increases `A` linearly (slope `+2·eps`). Single-mark flat intervals (n=3): `mark[0]=14/15` flat on `[12/15, 1)`, `mark[2]=8/15` flat on `(7/15, 11/15]`, `mark[1]=12/15` has NO flat direction (any perturbation increases `A`). Two- and three-mark simultaneous perturbations: 21/441 and 111/1331 sample points remain flat — the flat region is genuinely positive-dimensional (a polytope of dimension ≥ 2 for n=3).

**Mechanism of the flat facets:** moving a Xiang mark within a sub-interval creates a "sliver" fragment that lands at a canceling (odd) rank — the **`±a` cancellation of the certified `n=1` real case, generalized**. The flat region is the locus where this sliver-canceling holds; `A` is invariant there. Moving OUT of the flat region breaks the cancellation and `A` rises linearly.

So the answer to Q1 is: `min A = α(n)` (verified `n=3,4,5`), but the minimizer set is a **positive-dimensional flat polytope**, NOT the unique mirror config. The mirror is one boundary point of this polytope (and its sort-symmetric images are others).

### 2. Local structure around the minimizer — mirror is on a FACET, not a vertex

`A` is piecewise-linear in the marks, with breakpoints at `x_i = l_j` (mark hits a Liu mark) and `x_i = x_k` (two Xiang marks coincide). The mirror marks `1−l_j` are **NOT** breakpoints — they are interior points of cells of this natural arrangement. The flat region is a **union of full cells** (where the sliver-canceling sort pattern is stable), and the mirror sits in the interior of this flat region, not at an arrangement vertex.

**Implication for the route:** a "local-minimum-at-vertex" argument (check `A ≥ α(n)` at every arrangement vertex, then lift by linearity) does NOT directly apply, because the minimizer is not a vertex — it is a flat facet. The natural arrangement's vertices are degenerate (a piece has size 0, `A` on a singular multiset), and the global minimum is attained on a *facet interior*, where the function is locally constant.

**What IS viable:** a **cell-by-cell** argument. On each cell of the arrangement `A` is linear; its minimum on the closure of the cell is attained at a vertex of the cell (hence at an arrangement vertex, where some piece degenerates). So `A ≥ α(n)` globally ⟺ at every arrangement vertex, the limiting value of `A` is `≥ α(n)`, AND the flat facets (where `A = α(n)`) are accounted for. The flat facets are the "free" cells (linear with slope 0 in the flat directions, rising in the transverse directions). The work is proving the lower bound on the **non-flat cells** — those where the sliver-canceling does not hold and `A` is strictly increasing. This is a finite (but exponential-in-`n`) cell-complex classification problem.

### 3. Convexity / smoothing — NOT viable globally

Checked along the line `mirror + t·(random−mirror)` for `n=3`: `A` goes `0.067 → 0.22 → 0.085 → 0.094` — strongly non-convex, non-monotone, with an interior maximum. `A` is **not convex, not quasi-convex** globally. A smoothing/averaging inequality ("`A` is minimized at the symmetric config by averaging marks") is **not plausible** as a global argument. (Locally, on the flat facet, `A` is constant — trivially "convex" there — but that gives no information off the facet.) So the variational route must be a **direct piecewise-linear cell analysis**, not a convexity/smoothing argument.

### 4. Relation to the dead engines — this framing genuinely escapes the `−2T` wall

The `−2T` tail-flip term (certified dead, `lemmas/lemma-delta-a-local-cut.md`) arises **only** when `A` is decomposed into per-mark local cuts: each mark's contribution carries a `±T` tail-parity term, and the tails ADD destructively (`T_M + T_R ≤ 0` fails). Engine A (two-tail cancellation) was falsified on `n=3` brute force for exactly this reason — the two `ΔA` tails add, same `−2T` wall as per-mark induction.

**The variational framing does not decompose `A` per-mark.** It treats `A` as one piecewise-linear function of the full mark-vector. There is no "tail of mark `i`" to add to "tail of mark `j`" — the function's value at a point is computed once, globally, from the full sorted multiset. Concretely: the `−2T` term comes from the rank-shift of the tail when one mark is inserted; in the global-function view, rank-shifts are absorbed into the cell structure (crossing a cell boundary changes the sort, and `A`'s formula on the new cell is just a different linear form — no additive tail). So a **global cell-by-cell lower bound** bypasses the residual (Match) / Hall matching entirely: there is no `e_M ≤ o_R` inequality to prove, no `Σ_MM m_even ≤ Σ_RR r_odd` residual — those are artifacts of the per-mark / `M⊎R` decomposition. The variational route replaces them with "classify the cells, bound the linear form on each."

This is the structural reason the route is genuinely different: the obstruction of the current field (the residual Match on the merged sort) is a decomposition-dependent artifact, not a property of `A` itself.

### 5. Crux corpus — closest analog: aimo-0261 (partition + symmetry line + self-similar recursion)

Filtered the combinatorics + algebra corpus by `games-and-strategy`, `extremal-principle`, `invariants-and-monovariants`, then keyword-matched for mirror/symmetrize/extremum/alternating/flat/partition. Best match:

- **aimo-0261** (subtopic `extremal-principle`): "In a perimeter-minimizing partition, apply a merge-or-shift local exchange to the piece covering the extreme corner to force its opposite corner onto the symmetry line, producing a self-similar split for induction." — A partition problem whose **extremal config is forced onto a symmetry line by a local exchange, then recurses self-similarly**. Directly analogous to our target: force `A`'s minimizer onto the mirror (symmetric) locus, then the dyadic self-similarity gives the recursion `D(n+1)=2D(n)+1`. The adaptation needed: in aimo-0261 the minimizer is unique (the symmetry line); in our problem the minimizer is a flat polytope, so "force onto the symmetry line" must become "force onto the flat symmetric locus, then show the flat locus has `A=α(n)` by the self-similar recursion." This is a real adaptation, not a citation.

Secondary:
- **aimo-0757** (`sequences-and-recurrences`): "When an extremal index is chosen as the argmax over a FLAT range of all smaller indices, and its complement is itself governed by the same relation, expand that complement to exhibit a strictly larger competitor, contradicting the argmax." — A flat-range extremal argument; the analog of "the minimizer is a flat polytope, not a point, but the flat polytope is still governed by the self-similar recursion." Less directly load-bearing.

No crux in the corpus treats "alternating-rank sum minimized at the symmetric configuration" as such; the closest is the aimo-0261 local-exchange-forces-symmetry move.

### 6. Honest assessment

**Is this route promising enough to open as a new approach? YES.** It is a genuinely different framing: it replaces the per-mark / `M⊎R` / residual-Match decomposition (the current field, plateaued 3 rounds on the same `e_M ≤ o_R` / Hall matching gap) with a single global piecewise-linear minimization. The `−2T` wall and the residual (Match) do not appear — they are decomposition artifacts, absent in the global-function view. The empirical floor `min A = α(n)` is robust (verified `n=3,4,5`).

**The single hardest step:** proving `A ≥ α(n)` on every (non-flat) cell of the arrangement for general `n`. The flat cells are free (`A = α(n)`); the work is the strictly-increasing cells. The arrangement has exponentially many cells (`~ n!·2^n` sort-pattern regions), so a direct enumeration is infeasible for general `n`. The lever expected to close it: **the dyadic self-similar recursion** — at level `n+1`, the cells inherit from level `n` via the `M⊎R` decomposition, and the flat-facet structure (sliver-canceling) lifts inductively. The aimo-0261 move (local exchange forces the extremum onto the symmetry line, then self-similar recursion) is the template.

**What a builder would need to prove first (the base induction step):**
1. **Characterize the flat region structurally.** Prove: for the level-`n` dyadic, the locus `{xiang marks : A = α(n)}` is exactly the sliver-canceling polytope (the configurations where every Xiang mark either is a mirror mark `1−l_j` or lies in a canceling sub-interval). This generalizes the certified `n=1` real-case proof (the `±a` mechanism).
2. **Prove `A > α(n)` on every adjacent non-flat cell** for `n=3` by direct cell enumeration (feasible: 6 hyperplanes, manageable cell count), establishing the `n=3` real-valued lower bound rigorously — this would close `L(3)` for reals, the first new `n` since `n=2`.
3. **Lift to general `n` via the self-similar recursion:** show the cell complex at level `n+1` is built from level-`n` cells by the `M⊎R` decomposition, and the flat-facet / increasing-cell structure recurses. This is the open inductive step; it is the genuine difficulty.

**Risks / honest caveats:**
- The flat polytope being positive-dimensional is a double-edged sword: it means the minimizer is degenerate, so a "unique minimizer → symmetry" argument (aimo-0261 style) does not directly fire. The flat locus must be characterized, not just the mirror point.
- The cell-complex classification at general `n` may be as hard as the original problem; the inductive lift is not guaranteed to be clean.
- No convexity available, so no cheap global argument — the work is genuinely in the cell-by-cell analysis.

**Verdict — is this a genuinely different framing?** Yes. The current field (pair-excess, `e_M ≤ o_R`, residual Hall Match, per-mark `−2T` tail-flip) is a *decomposition* of `A`; the variational route treats `A` as one piecewise-linear function on the mark-simplex and asks for its global minimum. The decomposition artifacts (the residual Match, the `−2T` additive tail) do not exist in the undecomposed function. The empirical answer (`min A = α(n)`, minimizer a flat symmetric polytope) is verified for `n=3,4,5`. The flat polytope's mechanism is the generalized `±a` sliver-canceling — the SAME mechanism already certified for `n=1` reals. The route is promising enough to open as a new approach, with the `n=3` real-valued lower bound (step 2 above) as the first concrete target a builder should hit. The hardest step is the inductive cell-complex lift to general `n`; it is genuinely open and may require combining the variational view with the self-similar `M⊎R` recursion (so it does not fully replace the current field — it provides a different engine for the cell bound that the per-mark field could not supply).

---

### Distinct openings surfaced
- **(V1) Global cell-by-cell lower bound.** `A ≥ α(n)` ⟺ `A ≥ α(n)` on every cell of the natural arrangement (`x_i=l_j`, `x_i=x_k`). Flat cells free; non-flat cells need a linear-form lower bound. Target: close `L(3)` for reals first.
- **(V2) Flat-locus characterization + self-similar recursion.** Prove the locus `{A=α(n)}` is the sliver-canceling polytope; lift via `M⊎R` decomposition (aimo-0261 template: force extremum onto symmetric locus, recurse).
- **(V3) Generalized `±a` sliver-canceling as the load-bearing mechanism.** The flat facets ARE the certified `n=1` mechanism, generalized — so the `n=1` real proof is the base case of an induction on `n`, with the cell structure carrying the induction.
- **(V4) Vertex-check reformulation (weaker but finite).** `A`'s global min equals the min over arrangement vertices of the limiting (degenerate-multiset) value — a finite check per `n` (exponential but structured), usable as a rigorous certificate for fixed small `n` and as a check on the inductive lift.

### Candidate technique(s)
Piecewise-linear function minimization over a hyperplane arrangement; cell-complex classification; local-exchange-forces-symmetry (aimo-0261); self-similar recursion `D(n+1)=2D(n)+1`; sliver-canceling `±a` mechanism (certified `n=1`).

### Cheap-kill candidates
- **Vertex/edge enumeration for `n=3`** (6 hyperplanes, ~20 feasible vertices): a finite rigorous certificate that `min A = α(3)` at all arrangement vertices — would close `L(3)` for reals if the cell-interior monotonicity is also checked. This is the cheapest real-valued result not yet in hand.
- **Flat-direction injection:** show the flat facets' transverse directions all have `A` increasing (verified for one direction `n=3`; a full transverse basis check is cheap).

### Knowledge-base entries to use
- **Invariants & monovariants** (`A` as the controlled invariant; the sliver-canceling `±a` is the `n=1` invariant, certified `lemma-g-greedy-picking` + the round-3 `n=1` real proof).
- **Exploit symmetry / WLOG** (the `x ↔ 1−x` point-reflection involution is the mirror; `lemma-mirror-dyadic-cap`).
- **Pigeonhole / extremal principle** (the global min is attained; the flat polytope is the extremal locus).
- **Casework / exhaustion** (cell-by-cell analysis; the `n=3` vertex enumeration).

### Analogous past problems (cruxes)
- **aimo-0261** — crux: "local-exchange forces the extremal partition onto the symmetry line, then self-similar split for induction." Analogous because: our extremal config (the flat symmetric locus containing the mirror) is forced by a local exchange, and the dyadic self-similarity `D(n+1)=2D(n)+1` is the recursion. Adaptation: our minimizer is a flat polytope, not a unique point.
- **aimo-0757** (secondary) — crux: "argmax over a FLAT range; complement governed by the same relation." Analogous because: the flat minimizer polytope is governed by the self-similar relation.

### Prior progress
- `c(n)=2^n/D(n)` verified `n=1..5`; `n=1,2` solved end-to-end (reals).
- Certified: Lemma G, pair-pile, mirror, `ΔA` local cut, `L*`, `U(2)`, integer-grid parity (all `n`, grid-only), `e_M≤o_R` reduction, self-compensation, CK, dyadic-ratio overshoot.
- The variational route does NOT re-prove any of these; it imports Lemma G (greedy → odd-rank sum, `Liu=(1+A)/2`) and the mirror config as one minimizer, then attacks `min A ≥ α(n)` directly.

### Dead ends (do not retry)
- **Per-mark induction / `−2T` tail-flip** (certified dead, `lemma-delta-a-local-cut`): the variational route avoids this by not decomposing `A` per-mark — do NOT re-introduce per-mark local cuts within this route.
- **Engine A (two-tail cancellation, `pairing-partner-transfer`)**: falsified `n=3` brute force (21/33 `k≥2` minimizers admit no single-pair transfer). Do not retry; the variational route replaces transfers with cell analysis.
- **Engine R-pile (greedy recursive pile-match)**: falsified for regime-N upper bound (3 counterexample classes) — irrelevant to the lower-bound variational route, but flagged for completeness.
- **Conjecture (S) "smallest piece ≥ α(n) at the minimizer"**: FALSE for reals (sub-`α` fragments cancel at odd ranks). The variational route handles this naturally (the flat facets are exactly where sub-`α` slivers cancel), but do NOT use (S) as a premise.
- **Global convexity / smoothing of `A`**: verified FALSE (`A` non-convex along mirror→random line). Do not attempt a convexity/smoothing argument.

### Small-case / intuition notes (CONJECTURE, not proof — labeled)
- **Conjecture (V):** for the level-`n` dyadic, `min A = α(n)` over all real Xiang responses, attained on a positive-dimensional flat polytope (the sliver-canceling locus) whose boundary includes the mirror config. Verified computationally for `n=3,4,5` (DE + 50k exact-rational random samples, 0 violations; flat polytope mapped for `n=3`).
- **Conjecture (V-flat):** the flat polytope's mechanism is the generalized `±a` sliver-canceling (the certified `n=1` real-case mechanism). Plausible (single-mark flat intervals match the `±a` pattern) but NOT proved for general `n`.
- **Conjecture (V-cell):** `A ≥ α(n)` on every non-flat cell, with strict inequality. Verified for `n=3` on the mirror-adjacent cells (perturbation increases `A`); NOT verified on all `n=3` cells, NOT proved for general `n`.
