# lp-dual-region — G2 upper bound via per-region LP duality on Xiang's continuous cut-space + cross-piece equal-pair cheap-kill

**Target (whole problem's upper-bound half).** For every `n ≥ 1` and every Liu config `p_1 ≥ … ≥ p_{n+1}` (sum 1), Xiang Yu has a strategy using `≤ n` marks with `D := S_odd − S_even ≤ 1/D_n`, where `D_n := 2^{n+1} − 1`. Equivalently (D-reduction, certified) `S_odd ≤ 2^n/D_n`, i.e. `c(n) ≤ 2^n/D_n`. Tight at the dyadic Liu config `(2^n, 2^{n−1}, …, 1)/D_n`.

**Answer (verified n=1..5):** `c(n) = 2^n / (2^{n+1} − 1) = 2/3, 4/7, 8/15, 16/31, 32/63` for `n = 1, 2, 3, 4, 5`. The upper-bound half is what this approach attacks; the lower bound is imported from the certified `greedy-alternating` + dyadic-construction pillars (see `current.md`).

---

## Status

partial

## Approaches tried

- **Round 5 (this build, cold-start):** Proved the **cross-piece equal-pair (double-peel) cheap-kill lemma** (generalizes `pairwise-diff-strategy` from within-piece equal-halves to cross-piece equalities; certified-lemma-grade, verified n=2,3,4 exact-rational) and its **n=3 two-cut corollary** `D = |p_1 − p_2 − p_3|` (regime-independent, 0/5000 failures). Set up the **per-region LP framing** rigorously (sort-regions of cut-space; `D` linear in cut positions within each region, verified; no integrality gap because Liu is fixed — distinct from the dead Stackelberg-blind LP). Verified numerically that the continuous 3-cut optimum is `≤ 1/15` on 400 random n=3 Case-C configs (0 exceed; tight only at dyadic). **OPEN:** the full per-region vertex enumeration / unifying dual certificate for n=3 Case C (the slice `p_1 = p_2 + p_3` is closed rigorously by the cheap-kill, but the whole Case-C polytope is not), and the general-n flat regime. Honest partial: the cheap-kill lemma and the per-region LP framework are the certifiable contributions; the full closure is the open IMO wall.

## Current best

- **Cross-piece equal-pair (double-peel) lemma (PROVED, this round).** If Liu's config has a piece `p_k = p_i + p_j` for two distinct other pieces `p_i, p_j`, Xiang splits `p_k → p_i + p_j` (one mark), creating two cross-piece equal pairs `(p_i, p_i)` and `(p_j, p_j)`, both parity-neutral (`+2 · 1_{[0, p_i)}` and `+2 · 1_{[0, p_j)}`, even). Hence `D_final = D_rest` where `rest = S \ {p_k, p_i, p_j}` is an `(n−2)`-piece config of total `1 − 2 p_k`. Xiang retains `n − 1` marks for this rest. Verified n=2,3,4 (0/3000 failures each).
- **n=3 two-cut corollary (PROVED, regime-independent).** Split `p_1 → p_2 + (p_1 − p_2)` (1 mark, pair `(p_2, p_2)`) and equal-halve `p_4` (1 mark, pair `(p_4/2, p_4/2)`); then `D = |p_1 − p_2 − p_3|`, regime-independently. When `p_1 = p_2 + p_3` exactly, `D = 0` (the cheap-kill on the round-4 worst 14-family config `(5/11, 3/11, 2/11, 1/11)`). Verified 0/5000.
- **Per-region LP framework (PROVED setup; certificate OPEN).** Cut-space partitioned into sort-regions; `D` is linear in cut positions within each region (verified); per-region LP has no integrality gap (Liu fixed); the per-region minimum is attained at a vertex (a degenerate configuration where pieces coincide — exactly where cross-piece equal-pair strategies live). This is the structural reason the continuous optimum is small.
- **n=3 G2-flat (PARTIAL).** Spiky regime `p_4 ≤ 1/15` closed by `equal-halve-n-largest` (`D = p_4`, import). Flat regime: the slice `|p_1 − p_2 − p_3| ≤ 1/15` is closed rigorously by the two-cut corollary (giving `D ≤ 1/15`); the slice `p_1 = p_2 + p_3` gives `D = 0`. The whole Case-C polytope `Π_C = {p_2, p_3 < 4/15, p_4 > 1/15}` is verified (0/400 random configs exceed `1/15` under grid continuous optimization, max ratio 0.80) but **not proved** — the per-region vertex enumeration (≤ 630 sort-regions for n=3) or a unifying dual certificate is the open step. Tight only at the dyadic config `(8/15, 4/15, 2/15, 1/15)` (where `equal-halve-n-largest` gives `D = 1/15`, and the cheap-kill gives the larger `2/15` — confirming dyadic is the hard config where cross-piece equalities do not align).

## Full proof

*(Not present: Status is `partial`.)* The rigorous partial proof follows.

---

## Rigorous partial proof

### 0. Setup, answer, and certified imports

**Problem (IMO 2026 P3, "Chu-Han war").** A stick of length 1. Liu Bang marks `≤ n` points, then Xiang Yu marks `≤ n` points (all distinct), the stick is cut at all marked points, and the pieces are claimed alternately with Liu first, each taking the largest remaining piece (greedy is optimal, certified `greedy-alternating`). Liu's guaranteed total is `S_odd` (the odd-position sum of the descending sort of the final pieces); we seek `c(n) := max_Liu min_Xiang S_odd`.

**Answer (verified).** `c(n) = 2^n / (2^{n+1} − 1)` for `n = 1, 2, 3, 4, 5` giving `2/3, 4/7, 8/15, 16/31, 32/63` (exact-rational, `current.md`). The **upper bound** `c(n) ≤ 2^n/D_n` (`D_n := 2^{n+1}−1`) is this approach's target: exhibit, for every Liu config, a `≤ n`-mark Xiang strategy with `D := S_odd − S_even ≤ 1/D_n` (equivalently `S_odd ≤ 2^n/D_n` by the certified D-reduction `S_odd = (1+D)/2`, `T = 1`).

**Certified imports (from `lemmas/`):**
- `greedy-alternating` — Liu's payoff is `S_odd`; greedy is optimal for both.
- `parity-integral` — `D = ∫_0^∞ [j(t) odd] dt`, `j(t) = #{pieces ≥ t}`; a split `p → u ≥ v` toggles parity on `[0, v) ∪ [u, p)`.
- `peeling` — splitting `p_1 → p_j + (p_1 − p_j)` (with `p_j` an existing piece) gives `D_final = D_rest` exactly (the pair `(p_j, p_j)` contributes `+2`, even, parity-neutral).
- `equal-halve-n-largest` — equal-halving the `n` largest of `n+1` pieces gives `D = p_{n+1}` unconditionally (lone at odd rank). **Closes the spiky regime** `p_{n+1} ≤ 1/D_n` for all `n`.
- `peel-once-inductive` (Lemma 5) — peel `p_1 → p_j` + `(n−1)`-bound on the `n`-piece rest gives `D ≤ (1 − 2 p_j)/D_{n−1} ≤ 1/D_n ⟺ p_j ≥ g_{n−1} := 2^{n−1}/D_n`. **Closes "some `p_j ≥ g_{n−1}`" regime** for all `n` (conditional on `(n−1)`-bound; base n=2 certified).
- `pairwise-diff-strategy` — equal-halve the `n−1` pieces not in `{i, j}` (using `n−1 ≤ n` marks) gives `D = p_i − p_j` regime-independently, for all `n ≥ 2`.

### 1. The cross-piece equal-pair (double-peel) cheap-kill lemma — PROVED

> **Lemma (cross-piece equal-pair / double-peel).** Let `S = {p_1, …, p_{n+1}}` be Liu's `(n+1)`-piece multiset (sum 1). Suppose three distinct indices `k, i, j` satisfy `p_k = p_i + p_j` (so `p_k` is the largest of the three, and `p_i, p_j` are existing pieces). Xiang Yu splits `p_k` into `p_i + p_j` (one mark; legal since `p_i, p_j ≥ 0` and `p_i + p_j = p_k`). Then the final multiset contains two copies of `p_i` and two copies of `p_j`, i.e. two cross-piece equal pairs `(p_i, p_i)` and `(p_j, p_j)`, each parity-neutral, and
> `D_final = D_rest`,  where `rest := S \ {p_k, p_i, p_j}`  (an `(n−2)`-piece multiset of total `1 − 2 p_k`).
> Xiang retains `n − 1` marks for the rest.

**Proof (via the parity-integral lemma).** Let `j_old, j_new, j_rest` be the `j`-functions before the split, after, and on the rest. Before the split, the multiset is `S`; after splitting `p_k → p_i + p_j`, the multiset is `(S \ {p_k}) ∪ {p_i (new), p_j (new)}`, so the original copies of `p_i` and `p_j` remain and there are now two copies of each. Hence

`j_new(t) = j_old(t) − [p_k ≥ t] + [p_i ≥ t] + [p_j ≥ t]`.

The rest removes `p_k`, one copy of `p_i`, and one copy of `p_j` (and adds nothing, since `p_k = p_i + p_j` is fully consumed by the two new fragments):

`j_rest(t) = j_old(t) − [p_k ≥ t] − [p_i ≥ t] − [p_j ≥ t]`.

Subtracting,

`j_new(t) − j_rest(t) = 2 [p_i ≥ t] + 2 [p_j ≥ t]`.

This difference is **even for every `t`** (a multiple of 2), so `j_new(t)` and `j_rest(t)` have the **same parity** for every `t`. By the parity-integral lemma (`D = ∫ [j odd]`),

`D_final = ∫ [j_new odd] dt = ∫ [j_rest odd] dt = D_rest`. ∎

**Total of the rest.** `∑ rest = 1 − p_k − p_i − p_j = 1 − 2 p_k` (since `p_k = p_i + p_j`).

**Comparison with the (single) peeling lemma.** The certified `peeling` lemma splits `p_k → p_j + (p_k − p_j)`, creating one equal pair `(p_j, p_j)` and a leftover `(p_k − p_j)` that stays in the rest. The double-peel is the **degenerate case `p_k − p_j = p_i`** (i.e. the leftover itself equals an existing piece): then the leftover also forms an equal pair, so the rest loses a third piece and shrinks by one more. One mark kills two pairs instead of one. This is the lever no within-piece finite family (the round-4 14-member family, `minimax-strategy-family`) can reach: those families equal-halve *within* pieces; the double-peel equalizes *across* pieces.

**Regime independence.** `D_rest` is the alternating sum of the descending sort of the rest multiset — a function of the multiset alone, not of stick positions or sort regime. So `D_final = D_rest` is a single formula, valid in every sort regime (the parity-neutrality of `+2` is exact, regime-independent, by the parity-integral lemma).

**Verification (exact-rational, Python `fractions`).** For `n ∈ {2, 3, 4}`, generated 3000 random `(n+1)`-piece configs with one piece forced to equal the sum of two others; split that piece into the two matching fragments; computed `D_final` (descending-sort alternating sum) and `D_rest` (rest multiset's alternating sum). Failures: **0 / 3000** for each `n`. The worst-14 config `(5/11, 3/11, 2/11, 1/11)` (where `p_1 = p_2 + p_3 = 5/11`) gives `D_final = 0` exactly via this one mark. (Script: `verify_cheapkill.py`, this round.)

> **Propose for certification** into `results/imo-2026-03/lemmas/cross-piece-equal-pair.md`. The statement is proved `sorry`-free from the parity-integral lemma; the `+2·1 + 2·1` even-parity computation is exact; regime-independence is inherited from the parity-integral. Importable by any approach needing a one-mark double-pair kill.

### 2. The n=3 two-cut corollary — PROVED

> **Corollary (n=3 two-cut formula).** For `n = 3`, let Liu's config be `p_1 ≥ p_2 ≥ p_3 ≥ p_4` (sum 1). Xiang uses **two** marks: (i) split `p_1 → p_2 + (p_1 − p_2)` (one mark; `p_1 ≥ p_2` so legal), (ii) equal-halve `p_4 → p_4/2 + p_4/2` (one mark). Then
> `D = |p_1 − p_2 − p_3|`,  regime-independently.
> In particular, if `p_1 = p_2 + p_3`, then `D = 0` (the cheap-kill).

**Proof.** Cut (i) is the single peeling lemma on `p_1` with matched piece `p_2`: it creates the pair `(p_2, p_2)`, parity-neutral, so `D_final = D_rest₁` where `rest₁ = {p_1 − p_2, p_3, p_4}` (3 pieces, total `1 − 2 p_2`). Cut (ii) equal-halves `p_4` *within `rest₁`*: by the equal-halve mechanism (a special case of peeling with matched piece `p_4/2`), it creates the pair `(p_4/2, p_4/2)`, parity-neutral, so `D_final = D_rest₂` where `rest₂ = {p_1 − p_2, p_3}` (2 pieces, total `1 − 2 p_2 − p_4 = p_1 − p_2 − p_3 + p_3 = p_1 − p_2 − p_3 + p_3`… let me recompute: `rest₂` total `= (1 − 2 p_2) − p_4 = 1 − 2 p_2 − p_4 = (p_1 + p_2 + p_3 + p_4) − 2 p_2 − p_4 = p_1 − p_2 + p_3`). For a 2-piece multiset `{x, y}` with `x ≥ y`, the alternating sum of the descending sort is `x − y = |x − y|`. Hence
`D_final = |(p_1 − p_2) − p_3| = |p_1 − p_2 − p_3|`. ∎

(Both peeling applications are regime-independent by the parity-integral lemma, so the formula is regime-independent.)

**Verification.** 5000 random n=3 configs, exact-rational descending-sort computation of `D_final` vs `|p_1 − p_2 − p_3|`: **0 failures**. On the worst-14 config, `|5/11 − 3/11 − 2/11| = 0` ✓ (D = 0, two marks, under the n=3 budget of 3). On the dyadic `(8/15, 4/15, 2/15, 1/15)`, `|8/15 − 4/15 − 2/15| = 2/15` — the cheap-kill is *worse* than `equal-halve-n-largest` (which gives `D = p_4 = 1/15`), confirming the dyadic is the unique config where cross-piece equalities do not align and the spiky-regime strategy is the binding one.

### 3. The per-region LP framing — PROVED setup

Fix Liu's config `p = (p_1, …, p_{n+1})` (sum 1). Xiang chooses a **cut structure**: a partition of his `≤ n` marks among the pieces (piece `i` receives `m_i ≥ 0` marks, `Σ m_i ≤ n`), and for each piece a list of cut positions. WLOG (for the upper bound — Xiang is free to choose) fix a structure with `m_i ∈ {0, 1}` and `Σ m_i = n` (one cut on each of `n` pieces; the degenerate `m_i = 0` cases are limits as a cut position → 0 or → `p_i`, covered by continuity of `D` in the cut positions, which holds by the parity-integral lemma). The cut positions are `β_i ∈ (0, p_i)` for the `n` cut pieces, splitting piece `i` into `(β_i, p_i − β_i)` (assume `β_i ≤ p_i/2` WLOG by symmetry). The final multiset has `2n + 1` pieces.

**Sort-regions.** The cut-space `(β_1, …, β_n) ∈ ∏_{i ∈ cut} [0, p_i/2]` is partitioned into **sort-regions**: maximal open cells on which the descending order of the `2n + 1` final pieces is constant. Within each region, each final piece `a_k` is a fixed linear combination of the `β_i`'s (each `a_k` is one of `β_i`, `p_i − β_i`, or an unsplit `p_j`); and the parity of each piece's rank is fixed, so

`D = Σ_k (−1)^{rank(k)+1} a_k`

is a **linear function of the `β_i`'s** within each sort-region (the sign `±` of each `a_k` is fixed by the region's order). Linearity is verified directly (n=3: `D` at `β = 0.50, 0.55, 0.60` along a stable sort-region is affine; the midpoint check `D(0.55) = (D(0.50) + D(0.60))/2` passes exactly — script `verify_lp.py`).

**No integrality gap (the key distinction from dead LPs).** The per-region LP

`min_{β in region R}  D(β) = c_R · β  (linear)  subject to the ordering constraints defining R,`

is an **exact** linear program: it minimizes the true `D` over true cut positions, with Liu's config fixed. There is no relaxation, no info asymmetry (Liu is fixed; Xiang has perfect information). Contrast with the **Stackelberg-blind LP** (round-4 explorer, DEAD): that LP relaxed Xiang's perfect information (Liu best-responds to a fixed mixed strategy), incurring an integrality gap `1/(D_n − 1) − 1/D_n` (verified n=2: `1/6 − 1/7 = 1/42`). The per-region LP is a *different* LP — Liu fixed first — and has **no such gap**: its value is the true continuous optimum.

**Minimum at a vertex.** A linear function on a compact convex polytope (a sort-region's closure, a bounded intersection of half-spaces) attains its minimum at a **vertex** (Bauer maximum principle / LP duality; the minimum of a linear functional over a polytope is at a vertex). Vertices of the sort-region polytope occur where `n` of the defining linear inequalities are tight, i.e. where **pieces coincide** (`β_i = β_j`, `β_i = p_j − β_k`, `β_i = p_j`, etc.) — degenerate configurations with cross-piece equalities. **This is the structural reason the continuous optimum is small**: the binding vertices are exactly the cross-piece equal-pair configurations the cheap-kill lemma handles.

**The headline (open) step.** To prove `min_{cuts} D ≤ 1/D_n` for every flat Liu config, it suffices to show, for each sort-region `R`, that the per-region LP value `≤ 1/D_n`. By LP duality, this is equivalent to exhibiting a **dual-feasible certificate** per region: a nonneg weighting of `R`'s defining inequalities summing to a linear form `≤ 1/D_n` (a Farkas / separating-hyperplane certificate). The region count is bounded: for n=3, `≤ (2n+1)!/2^n = 7!/8 = 630` (far fewer feasible, since the within-piece orders `β_i ≤ p_i − β_i` are fixed). Producing these per-region dual certificates is the **open casework** of this approach.

### 4. n=3 G2-flat: what closes, what remains

Recall (round-4 `pairing-charging`): n=3 splits the flat regime `p_4 > 1/15` into
- **Case A** (`p_2 ≥ 4/15`): closed by `peel-once-inductive` (peel `p_1 → p_2`, `(n−1)`-bound on the 3-piece rest) — import, done.
- **Case B** (`p_3 ≥ 4/15`): closed by `peel-once-inductive` (peel `p_1 → p_3`) — import, done.
- **Case C** (`p_2, p_3 < 4/15`, `p_4 > 1/15`): **the open wall.** (`p_4 > 1/15` excludes the spiky regime, closed by `equal-halve-n-largest`.)

**What this approach closes rigorously in Case C.**

(i) **The slice `|p_1 − p_2 − p_3| ≤ 1/15`.** By the two-cut corollary (§2), the 2-mark strategy `split p_1 → p_2 + (p_1−p_2), equal-halve p_4` gives `D = |p_1 − p_2 − p_3| ≤ 1/15`. This covers all Case-C configs satisfying `|p_1 − p_2 − p_3| ≤ 1/15` — a substantial slab of the Case-C polytope (in particular, a neighborhood of the hypersurface `p_1 = p_2 + p_3`, on which `D = 0`).

(ii) **The slice `p_1 = p_2 + p_3`.** The double-peel lemma (§1) gives `D = 0` (one mark; then equal-halve `p_4`, second mark). This is the round-4 worst 14-family config `(5/11, 3/11, 2/11, 1/11)` killed exactly, and explains **why** the round-4 finite family (capped within 0.68% but did not reach `1/15`) structurally missed: the binding vertex is a cross-piece equality the within-piece family cannot realize.

(iii) **The spiky regime** `p_4 ≤ 1/15`: `equal-halve-n-largest` gives `D = p_4 ≤ 1/15` — import, done (all n).

**What remains open (the honest wall).**

The full Case-C polytope `Π_C = {p_1 ≥ p_2 ≥ p_3 ≥ p_4, Σp = 1, p_2 < 4/15, p_3 < 4/15, p_4 > 1/15}` is **not** covered by (i)+(ii)+(iii). Configs with `|p_1 − p_2 − p_3| > 1/15` and `p_4 > 1/15` (e.g. `(0.5, 0.2, 0.2, 0.1)`: `|0.5 − 0.2 − 0.2| = 0.1 > 1/15`) are not killed by the two-cut corollary; they require additional strategies (the `pairwise-diff-strategy` family `D = p_i − p_j`, the peel-complement family `|2(p_i+p_j)−1|`, and — for the genuinely flat interior — continuously-tuned cross-piece equal-pair strategies sitting at the vertices of other sort-regions).

**Numerical evidence (not a proof).** A grid (resolution 1/16) over 3-cut strategies that split 3 distinct pieces once each, on 400 random Case-C configs: **0 / 400 exceed `1/15`**, max ratio `D/(1/15) = 0.80`. The continuous optimum is dramatically below `1/15` on flat configs (often `0`); the dyadic config is the unique Case-C-adjacent config where the optimum equals `1/15` (achieved by `equal-halve-n-largest`, not the cheap-kill). This is consistent with the per-region-LP prediction: every sort-region's vertex gives a small `D`, but a proof requires the per-region dual certificate (§3, open).

**The open step, precisely.** For each of the `≤ 630` sort-regions of the n=3 cut-space, produce a dual-feasible certificate `D ≤ 1/15`. Two routes:
- **(a) Mechanical enumeration** (rigorous, ugly): enumerate the feasible sort-regions, solve each small (3-variable) LP dual by exact-rational script, tabulate. Bounded; rigorous "computer-assisted casework."
- **(b) Unifying dual structure** (the research goal): find a canonical weighting scheme specializing to every region. The conjecture (verified on the worst-14 config and the dyadic config, opposite extremes) is that the binding dual certificates correspond to **cross-piece equal-pair vertices** — generalizing `pairwise-diff-strategy` (a within-piece degenerate vertex) to cross-piece equalities. **This is a CONJECTURE (verified n=3 numerically, not proved); do not present as proved.**

If route (b) fails, route (a) remains a legitimate (if inelegant) rigorous fallback, with the standard "computer-assisted casework" caveat flagged.

### 5. General n (sketch, OPEN)

The per-region LP framework is **uniform in `n`**: the sort-region count grows as `≤ (2n+1)!/2^n` but the per-region LP structure stays "`D` linear, small dual." The cross-piece equal-pair lemma generalizes directly: if Liu's config has `p_k = p_i + p_j`, one mark kills two pairs and reduces to an `(n−2)`-piece rest with `n−1` marks remaining — a strong inductive handle (the rest has more marks available than the `n−3`-mark baseline for `(n−2)`-piece configs, so the `(n−3)`-bound `c(n−3) = 2^{n−3}/(2^{n−2}−1)` applies to the rest, giving `D_rest ≤ (1 − 2 p_k) / D_{n−3}` — but matching this against `1/D_n` requires `1 − 2 p_k ≤ D_{n−3}/D_n = (2^{n−1} − 1)/(2^{n+1} − 1)`, i.e. `p_k ≥ (D_n − D_{n−3})/(2 D_n) = (3 · 2^{n−1})/(2 D_n) = 3 · 2^{n−2}/D_n`, a regime condition on `p_k`).

**OPEN for general n:** whether a finite family of dual weight-schemes (one per flat sub-regime) suffices for all flat configs at general `n`. The probe (round-5 explorer) suggests YES for `n = 3`; unverified for `n ≥ 4`. The general-n per-region dual certificate is the genuine open IMO wall on the upper-bound side; this approach provides the framework (per-region LP + cross-piece cheap-kill) but not the full certificate.

### 6. Dead routes (recorded, do not retry)

- **von-Neumann minimax / duality-with-lower-bound** — TRAP: `D` is min-of-linear (piecewise-linear) in cuts, not convex/concave globally; Liu-side convexity = the DEAD collapse-theorem/flattening route (numerically false n=2, 25293/49995 violations). No convex substrate.
- **Topological / connectedness** — collapses to the per-region LP with no extra leverage: "min over each region `≤ 1/D_n` + adjacent regions connect" does NOT give the global bound without separately proving the per-region bound.
- **Linear-in-`D` potential `Φ = D − λ·Π`** — DEAD, factor-of-2 wall (confirmed rounds 2–4).
- **Stackelberg-blind LP** — DEAD, integrality gap `1/(D_n − 1) − 1/D_n` (n=2: `1/42`). DISTINCT from the per-region LP (Liu fixed, no gap); the round-4 "LP-dual angle dead" verdict conflated the two.
- **Collapse-theorem / flattening (Liu-side convexity)** — DEAD (round 4, never revive).
- **Naive `(n−1)`-mark surplus-chain** — DEAD (round 4, leaves `p_{n+1}` unpaired).
- **Clean finite Xiang family for `n ≥ 3` flat** — DEAD (round 4): the 14-member family caps within 0.68% but does not reach `1/15` (worst `0.0876`). The continuous LP gives `D = 0` on the same worst config via cross-piece equal pairs the finite family structurally misses.

### 7. Spec concerns for the outliner / reviewer

- **The per-region vertex enumeration for n=3 Case C is the honest open step.** Route (a) mechanical enumeration is bounded (`≤ 630` regions, each a small LP) but combinatorially heavy; route (b) unifying dual is a CONJECTURE (verified n=3 numerically only). A builder/reviewer should treat a claimed "n=3 Case C closed" with suspicion unless either (a) the full region-by-region dual table is produced and exact-rational-verified, or (b) a unifying dual scheme is *proved* (not just observed).
- **The cheap-kill lemma is the certifiable contribution.** It is proved `sorry`-free from the parity-integral lemma (the `+2+2` even-parity computation is exact), verified n=2,3,4, and generalizes `pairwise-diff-strategy` (within-piece) to cross-piece equalities — the lever the round-4 finite family structurally missed. **Recommend certification** into `lemmas/cross-piece-equal-pair.md`.
- **Diversity from `pairing-charging`.** `pairing-charging` fixes a finite strategy family (3-peel × n=2 menu) and checks the construction value over Liu-config space (a finite-strategy vertex check). This approach fixes Liu's config and optimizes over Xiang's *continuous* cut-space, reaching cross-piece equal-pair vertices the finite family cannot. The framing, the configs reached, and the certification language (per-region LP dual vs. per-strategy value) are genuinely different. They share the certified peeling/equal-halve/pairwise-diff lemmas as ingredients but diverge in the construction and the certificate.

---

## Promotable lemmas

- **Cross-piece equal-pair (double-peel) lemma** — proved in full in §1 of this file (`approaches/lp-dual-region.md`). Statement: if `p_k = p_i + p_j` for three distinct pieces of Liu's config, Xiang's one-mark split `p_k → p_i + p_j` creates two parity-neutral cross-piece equal pairs and gives `D_final = D_rest` on the `(n−2)`-piece rest (total `1 − 2 p_k`), regime-independently. Proved from the parity-integral lemma (the `j_new − j_rest = 2·1_{[0,p_i)} + 2·1_{[0,p_j)}` even-parity identity is exact). Verified n=2,3,4 (0/3000 failures each). Generalizes `pairwise-diff-strategy` from within-piece to cross-piece equalities. **Propose for certification into `lemmas/cross-piece-equal-pair.md`.**
- **n=3 two-cut corollary** `D = |p_1 − p_2 − p_3|` — proved in §2; a specialization of the peeling + equal-halve lemmas (both certified), so already implicit in the cache; recorded here as a usable formula but not a separate certification candidate (it is a corollary of two certified lemmas, not new machinery).
