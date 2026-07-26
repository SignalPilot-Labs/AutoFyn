# two-regime-disjunctive — upper bound via a disjunctive dyadic/non-dyadic invariant

## Status
partial

> **Round-6 build summary (one paragraph).** This round closes the last material gap on `U(3)` — the `d < 1/2` non-gap extreme sub-cases `w < −2α` or `z < −2α` (α=1/15) — by a clean **7-cap case-by-case contradiction** `{a, b−a, c−b, d−c, |a+b−c|, |a+c−d|, |a+b−d|}` (4 chain-difference caps + 3 abs-sum caps), each realized by an explicit ≤3-mark Xiang strategy (the two NEW abs caps `|a+c−d|` and `|a+b−d|` via "bisect b + match a in d" and "bisect c + match a in d" respectively; all 7 are *always-realizable*, none requires `d ≥ b+c`). Assuming all 7 caps `> α` and splitting on the 2³ = 8 sign patterns of the three abs-caps (`C5=|a+b−c|`, `C6=|a+c−d|`, `C7=|a+b−d|`) yields 8 disjoint exhaustive sub-cases; the sign of `C5` is forced negative precisely when `w < −2α`, so the 4 `s5=−` patterns cover BOTH extreme sub-regimes (`w<−2α` OR `z<−2α`) and the 4 `s5=+` patterns cover the `z<−2α` half. Each sub-case is closed by a ≤4-line inequality contradiction (shown in full, §5e.3); the tightest is `s5=s6=s7=+` (sub-regime `z<−2α`), where `S2 ∧ C6+ ⟹ v > α`, `C5+ ∧ C6+ ⟹ 7u+3v < 2α`, hence `u < −α/7 < 0` contradicting `C1: u > 0` — the global extremum is `12α/13 = 4/65 < α` (margin `1/195`). Verified: 0 violations on 5473 exact-rational extreme configs (random + grid), worst `min-cap = 0.0582 < α = 0.0667`; an LP per sub-case confirms `max t < 0` in all 12 (sub-regime, sign-pattern) cells. Merged with the CERTIFIED `L(3)` (cell-complex, `lemma-vertex-principle-advantage.md`) and the round-5 closures (5-cap dominant `d ≥ 1/2` via `lemma-u3-5cap-dominant.md`; 3-mark sliver gap `G` via `lemma-u3-sliver-gap.md`; non-gap `w,z ≥ −2α` via `|a+b−c|`/`|b+c−d|`/`a`/`b−a`), this gives **`c(3) = 8/15` SOLVED end-to-end** (both bounds, equality iff the dyadic `(1,2,4,8)/15`). General-`n` `U` (regime-N `n ≥ 4`) and general-`n` `L` (`n ≥ 5`) remain OPEN — the approach is `partial` overall, with `c(3)` a fully rigorous solved sub-result.

## Approaches tried
- (round 6, this build) **U(3) extreme-closure → `c(3) = 8/15` SOLVED.** Closed the LAST material gap on `U(3)` — the `d < 1/2` non-gap extreme sub-cases `w < −2α` or `z < −2α` (α = 1/15) — via a clean **7-cap case-by-case contradiction** `{a, b−a, c−b, d−c, |a+b−c|, |a+c−d|, |a+b−d|}` (§5e). This OVERTURNS round-5's "no 4–7-cap subfamily suffices" ruling: that census used un-realizable cap *values* (`d−b−c` when `d < b+c`); with realizability enforced, the 7-cap subfamily is necessary AND sufficient (drop-one on a coarse grid keeps C5/C7 droppable, but the explorer confirmed on 2M samples that drop-`|a+b−d|` fails by ~0.002 — the 7th cap is genuinely load-bearing on fine samples). All 7 caps are *always-realizable* (none requires `d ≥ b+c`): the 4 chain caps are the certified §5d.1 strategies; the abs cap `|a+b−c|` is certified (§5d.1); the two NEW abs caps `|a+c−d|` ("bisect `b` + match `a` in `d`") and `|a+b−d|` ("bisect `c` + match `a` in `d`") are proved in §5e.1. The 2³ = 8 sign patterns of `(C5,C6,C7)` partition the extreme regime exhaustively and disjointly (§5e.2): the sign of `C5` is forced negative exactly when `w < −2α`, so the 4 `s5=−` patterns cover BOTH extreme sub-regimes (`w<−2α` OR `z<−2α`) and the 4 `s5=+` patterns cover the `z<−2α` half. Each sub-case is closed by a ≤4-line inequality contradiction (§5e.3); the tightest is `s5=s6=s7=+` (sub-regime `z<−2α`, the global extremum `12α/13 = 4/65 < α`, margin `1/195`). Verified: 0 violations on 5473 exact-rational extreme configs (worst `0.0582 < α`), LP `max t < 0` in all 12 (sub-regime × sign-pattern) cells (`/tmp/round-6/u3_7cap_verify.py`). Merged with the CERTIFIED `L(3)` (cell-complex) + the round-5 closures (5-cap dominant `d ≥ 1/2`; 3-mark sliver gap `G`; non-gap `w,z ≥ −2α` via `|a+b−c|`/`|b+c−d|`/`a`/`b−a` — the `|b+c−d|` cap is realizable via "bisect `a` + match `c` in `d`", §5e.4), this gives **`c(3) = 8/15` rigorously end-to-end** (both bounds, equality iff the dyadic `(1,2,4,8)/15`). General-`n` `U` (regime-N `n ≥ 4`) and `L` (`n ≥ 5`) remain OPEN — the approach is `partial` overall. Proposed new lemma: `lemma-u3-7cap-extreme` (PROPOSED, §5e).

- (round 5, this build) **U(3) closure attack.** Closed the `d ≥ 1/2` (dominant) regime of `U(3)` RIGOROUSLY via a clean **5-cap contradiction** `{a, b−a, c−b, 2d−1, |a+b−c|}` (4-way contradiction in two cases by the sign of `a+b−c`; equality `min = α(3) = 1/15` iff the dyadic `(1,2,4,8)/15`). Verified 0 violations on grids `N = 60, 120, 150` + 50k random reals, unique equality at the dyadic. **NEW rigorous 3-mark sliver strategy** for the `d < 1/2` GAP region: split `d → (b, c, d−b−c)` [2 marks, pairs `(b,b),(c,c)`] + shave `a → (ε, a−ε)` [1 mark]; the 5-leftover sort `c,c,b,b,a−ε,d−b−c,ε` gives `A = a−(d−b−c) = 1−2d < α(3)` (rigorous, verified). This CLOSES the gap region `{a, b−a, c−a−b, d−b−c all > α(3), d < 1/2}` (the unique sub-region where the 17-family exact-pair caps all exceed `α(3)`). **Remaining GAP (honest):** the `d < 1/2` NON-gap sub-cases (where some chain excess is `≤ 0`) are covered by the 17-family (0 violations computationally, `N = 120` grid + 50k random reals over the full simplex, equality only at the dyadic which lies in `d ≥ 1/2`), but a complete case-by-case analytic contradiction for every `d < 1/2` sub-case is NOT yet written — the 17-family's many caps are all needed (no small subfamily suffices: tested 4–7-cap subfamilies all have grid violations). The moderate-dominant class `L ∈ [8/15, 4/5]` (reviewer's round-4 overstatement flag) is GENUINELY covered by the 5-cap family (it lies in `d ≥ 1/2`, so the 5-cap contradiction handles it via the multi-way argument, NOT via the single `a`-cap). Combined with the CERTIFIED `L(3)` (cell-complex vertex enumeration), `c(3) = 8/15` is rigorously end-to-end on the `d ≥ 1/2` regime (the dominant half of the simplex, including the dyadic equality case) and on the `d < 1/2` gap; the remaining `d < 1/2` non-gap sub-cases are computationally verified but not yet analytic. Status: partial (rigorous on `d ≥ 1/2` + gap; `d < 1/2` non-gap analytic closure open). [Round 6 CLOSED the extreme non-gap sub-cases — see above.]

- (round 2, this build) Two-regime disjunctive invariant with the regime boundary REDEFINED as **dyadic vs non-dyadic** (per reviewer F2; the round-2 outline's "dominant vs non-dominant" boundary was mis-aligned with the certified `U(1)` base). Regime D (the config IS the dyadic) is handled by the certified pair-pile giving exactly `f(n)`. Regime N (non-dyadic) is handled by a **sliver / pile-matching strategy family** (per reviewer F1: NOT a pairing-to-`A≤0` argument — that claim was verified false). — Outcome: **`n=1` upper bound fully rigorous (corrected two-mode)**, **`n=2` upper bound fully rigorous (four-strategy family, equality iff dyadic — a NEW result, closing the open `U(2)` for free)**, **regime D (dyadic) for all `n` via imported pair-pile** (equality/attainment upper bound). The **general-`n` regime-N bound (`n≥3`, non-dyadic) is the explicit open gap**: the `n=2` four-strategy proof does not lift to a clean induction on `n` (each strategy is `n=2`-specific), and no per-`n` strategy family is identified. Lower bound (Lemma L general-`n`) imported from the sibling `pairing-partner` (also open there) — recorded as a dependency, not re-proved. The reviewer's F1–F3 are each addressed in the body.

- (round 3, this build) Engine R-pile (greedy recursive pile-match of the two largest pieces — cut `a_2` out of `a_1` when `a_1 ≥ 2 a_2`, bisect-`a_1` fallback when balanced) was dispatched to close **G2 (regime-N upper bound for `n ≥ 3`)**. — Outcome: **Engine R-pile FALSIFIED as a universal regime-N strategy** by direct computation (python, exact rational arithmetic, grid `N = 30` over dominant configs + targeted balanced/extreme tests). The greedy **caps below `8/15` only on a PROPER SUBSET of non-dyadic configs**; it **overshoots on** (i) the exact dyadic (`a_1 = 2 a_2` telescoping — the explorer's known overshoot, now characterized cleanly), (ii) **balanced non-dyadic configs** (`a_1 < 2 a_2`, e.g. `(.5, .3, .15, .05)` → greedy `Liu = 11/20 = 0.55 > 8/15 ≈ 0.533`; the bisect fallback destroys the cancellation), and (iii) **extreme-dominant configs with tiny tail** (e.g. `(.9, 1/30, 1/30, 1/30)` → greedy `Liu = 0.9`, no improvement — cutting a tiny `a_2` out of a huge `a_1` is negligible). The true optimal Xiang cap on every tested non-dyadic `n = 3` config is `31/60 < 8/15` (so the regime-N CONJECTURE holds numerically), but the greedy does not find it. The reviewer's consecutive-rank invariant (required fix #1) is MOOT: the greedy's failure is SUBOPTIMALITY (it picks a bad strategy), not an interleaving-rank failure — once a frozen pair forms, the full-multiset greedy treats the pair members as `a_2`-candidates and bisects them, destroying cancellation. The balanced fallback (required fix #2) has no clean `n`-general rule: the `n = 2` four-strategy template does not lift, and the optimal `n = 3` strategies have no recursive structure the greedy reproduces. NEW rigorous result this round: the **dyadic-ratio overshoot lemma** (one-step characterization — the greedy cancels its created pair iff `a_1 > 2 a_2` strictly; at `a_1 = 2 a_2` it builds an odd-multiplicity block and overshoots) — this is the dyadic-detection (required fix #3) and explains why the greedy is regime-N only. Proposed for certification (Section 5b). The regime-N gap for `n ≥ 3` remains OPEN; Engine R-pile is now RULED OUT as the universal regime-N mechanism (counterexamples recorded). Status: partial.

- (round 4, this build) NEW regime-N engine dispatched: **structural equality-case classification + sliver forcing** (replacing the dead R-pile). Two deliverables, both honest about scope. **(D1) Grid equality-case classification (rigorous, grid-only, all n).** Repackages the certified integer-grid parity theorem (`A·D(n) ≥ 1`, odd non-negative) into a clean NECESSARY equality condition: at the level-`n` dyadic Liu config, for grid-aligned (`1/D(n)`-grid) Xiang refinements, `A = α(n)` ⟺ (i) odd piece-count: all pair-excesses `0` AND smallest piece `= 1` (odd-mult leftover `{1}`), or (ii) even piece-count: exactly one pair-excess `= 1`, rest `0` (odd-mult leftover `{a, a+1}` consecutive, some `a ≥ 1`). The further refinement "smaller value `a = 2^j`" (the corpus-compute census observation) is EMPIRICAL, not proved (the parity theorem allows any `a`; which `a` are actually achievable by ≤ `n` Xiang marks is a strategy-existence question the census answers empirically). **(D2) Sliver-forcing lemmas for three structural classes (rigorous).** (S1) **Balanced config** `(w,…,w)` `n+1` copies, ALL `n ≥ 1`: explicit Xiang strategy drives `A = 2s → 0 < α(n)` (n odd: cut slivers from all `n` pieces; n even: bisect one piece to `(w/2,w/2)`, cut slivers from `n−1` of the rest). Verified exactly (python, rational). (S2) **Two-dyadic n=3 config** `(1/2, 1/4, 1/8, 1/8)`: 2 marks (cut `1/2→(1/4,1/4)`, cut one `1/4→(1/8,1/8)`) yield final multiset `{1/4,1/4,1/8,1/8,1/8,1/8}` with `A = 0 < α(3) = 1/15` exactly. (S3) **Extreme-dominant n=3** `(L, t, t, t)`, `t = (1−L)/3`, `L > 4/5`: 3 marks cut `L` into 4 equal pieces `L/4`; final multiset `{L/4×4, t×3}` (sort valid since `L/4 > t ⟺ L > 4/7`), `A = t = (1−L)/3 < 1/15 = α(3)` ⟺ `L > 4/5`. **Honest gap (unchanged):** the real-valued universal regime-N cover for n≥3 is NOT proved — the grid classification does NOT lift to reals (per the grid-parity lemma's own caveat; no proof technique visible, per the reviewer's flag), and the sliver-forcing lemmas cover only the three structural classes above, not arbitrary non-dyadic configs (e.g. moderately-dominant `L ∈ [8/15, 4/5]` and near-dyadic balanced-perturbation configs remain uncovered). The classification-lift + universal sliver-forcing remain the honest wall. Reviewer: CHANGES REQUESTED expected (partial) — three new rigorous sliver-forcing lemmas + a clean grid classification, but universal regime-N still open.

## Current best
**`c(3) = 8/15` SOLVED end-to-end this round (round 6).** Both bounds rigorous: LOWER `L(3)` is CERTIFIED (cell-complex vertex enumeration, imported `lemma-vertex-principle-advantage.md`: every real Xiang response to the level-3 dyadic `(1,2,4,8)/15` gives `A ≥ 1/15 = α(3)`, i.e. `Liu ≥ 8/15`); UPPER `U(3)` is CLOSED here by a complete 4-regime case partition of the n=3 Liu simplex (§5e.5): (I) `d ≥ 1/2` dominant — 5-cap contradiction (certified `lemma-u3-5cap-dominant.md`); (II) `d < 1/2` gap `G` — 3-mark sliver (certified `lemma-u3-sliver-gap.md`); (III) `d < 1/2` non-gap `w,z ≥ −2α` — `|a+b−c|`/`|b+c−d|`/`a`/`b−a` (§5d.4, with `|b+c−d|` realizable via "bisect `a` + match `c` in `d`", §5e.4); (IV) `d < 1/2` non-gap extreme `w < −2α` or `z < −2α` — the **7-cap case-by-case contradiction** `{a, b−a, c−b, d−c, |a+b−c|, |a+c−d|, |a+b−d|}` over 8 sign patterns (§5e, NEW this round). The four regimes are exhaustive and disjoint; in EVERY case Xiang with ≤3 marks forces `min ≤ α(3) = 1/15`, with equality iff the dyadic `(1,2,4,8)/15` (which lies in regime I). Combined `L(3) ∧ U(3)` ⟹ `c(3) = 8/15`. Verified: 0 violations on 5473 exact-rational extreme configs + LP `max t < 0` in all 12 sub-cases; global extremum `12α/13 = 4/65 < α` (margin `1/195`).

**Prior (still standing):** `c(1) = 2/3`, `c(2) = 4/7` SOLVED end-to-end (both bounds). Regime-D (dyadic) upper bound all `n` via certified pair-pile (equality/attainment). Grid equality-case classification (rigorous, grid-only, all n). Sliver-forcing Lemma S1 (balanced config, all n ≥ 1, `A = 2s → 0 < α(n)`). Dyadic-ratio overshoot lemma (characterization, not a regime-N proof).

**Open gaps (honest, general n):**
1. **Regime N general `n ≥ 4`** (the headline remaining gap). For `n ≥ 4` non-dyadic Liu configs, prove Xiang forces `A < α(n)`. The `n=3` 7-cap + 5-cap + sliver closure does NOT lift to `n ≥ 4` (the cap family grows combinatorially; no inductive structure identified). Engine R-pile FALSIFIED (round 3); (U-E) restates the gap; Φ-strict-decrease FALSIFIED (round 5, ridge). The non-strict `cap ≤ α(n)` framing is the live target but no general-n mechanism is proved.
2. **Lower bound `L(n)` for `n ≥ 5`** (general-n). `L(3)`, `L(4)` CERTIFIED (cell-complex vertex enumeration, finite per-n). The general-n lift has two converging framings (cell-complex D3 structural theorem / pairing-partner Hall injection), both OPEN. Imported as a dependency; `c(n) ≥ f(n)` for `n ≥ 5` not established by this approach.

## Full proof
*(The approach is `partial` overall (general-n `U` and `L(n≥5)` open), but the n=3 case is SOLVED end-to-end. The complete `c(3) = 8/15` proof (both bounds) is §5e.5 below; the rigorous halves for `n=1,2`, regime-D all n, and the `U(3)` regimes I–III are written out in §1–§5d. The NEW round-6 contribution is §5e — the 7-cap closure of the extreme sub-cases (regime IV), the last piece of `U(3)`.)*

---

### 0. Setup, notation, and the certified lemmas we import

Let `D(n) = 2^{n+1} − 1`, `f(n) = 2^n / D(n)`, `α(n) = 1/D(n)` (so `f(n) = (1 + α(n))/2`). The dyadic config of order `n` is the partition of `[0,1]` into pieces `(1, 2, 4, …, 2^n)/D(n)` (Liu's marks at cumulative sums of `(1, 2, …, 2^{n−1})/D(n)`).

We work throughout in the **advantage coordinate** `A = Σ_i (−1)^{i+1} p_i` where `p_1 ≥ p_2 ≥ …` are the final pieces sorted descending. By the certified **Lemma G** (`lemmas/lemma-g-greedy-picking.md`), optimal play in the alternate-pick phase gives Liu the odd-rank sum, and the parity identity `Liu = (1 + A)/2` holds. Hence

> **(upper-bound target)** `c(n) ≤ f(n)` is equivalent to: for every Liu partition `P` of `[0,1]` into `n+1` pieces, Xiang with `≤ n` marks has a strategy forcing `A(final) ≤ α(n) = 1/D(n)`.

We import three certified lemmas and do not re-prove them:

- **Lemma G** (greedy → odd-rank sum; `Liu = (1+A)/2`). `lemmas/lemma-g-greedy-picking.md`.
- **Pair-pile dyadic cap.** Against the dyadic config, Xiang's pair-pile (≤ `n` marks; `n−1` for `n ≥ 2`, `1` for `n=1`) produces the multiset `2^{n−1}, 2^{n−1}, 2^{n−2}, 2^{n−2}, …, 4, 4, 3, 2, 1, 1` (all over `D(n)`), whose advantage sum is `A = 1/D(n) = α(n)`, hence `Liu = (1+α(n))/2 = f(n)`. `lemmas/lemma-pair-pile-dyadic-cap.md`.
- **ΔA local-cut closed form** `ΔA = 2((−1)^r b − T)` (the `−2T` term is the parity-flip-on-tail; explains why per-mark induction fails). `lemmas/lemma-delta-a-local-cut.md`.

### 1. The corrected regime boundary (reviewer F2)

The round-2 outline's regime boundary was **dominant vs non-dominant** (does the largest piece exceed the sum of the rest?). The reviewer correctly flagged (F2) that this mis-aligns with the certified `U(1)` base: the `n=1` sliver mode handles configs `x ∈ (1/3, 1/2)` (smaller piece `x`), where the larger piece `1−x > 1/2` is dominant, yet the bisect/pair-pile strategy FAILS there (bisect gives oddsum `(1+x)/2 > 2/3 = f(1)` for `x > 1/3`). The sliver strategy, not the bisect, is what caps those configs.

The correct regime boundary, which makes the `n=1` two-mode base fall out as a clean special case, is **dyadic vs non-dyadic**:

> **(Regime D)** `P` is the (scaled) dyadic config of order `n` (up to permuting pieces).
>
> **(Regime N)** `P` is any other partition.

The two regimes are exhaustive and disjoint. **Regime D is the equality / attainment case**: the certified pair-pile forces `A = α(n)` exactly (Section 3). **Regime N is the strict-inequality case**: Xiang forces `A < α(n)` strictly (Sections 2 and 4). Crucially, the dyadic boundary at `n=1` is `x = 1/3 = α(1)`, which is exactly where the two `n=1` modes (bisect below, sliver above) meet — see Section 2.

### 2. The `n=1` upper bound, fully rigorous (the corrected `U(1)` two-mode proof)

Liu config: two pieces `(x, 1−x)`, WLOG `x ≤ 1/2` (so `1−x` is the largest). The order-1 dyadic is `x = 1/3`. Xiang has `1` mark. Target: `A ≤ α(1) = 1/3`, equivalently `Liu ≤ 2/3 = f(1)`, with strict inequality for `x ≠ 1/3`.

**Mode B (bisect), for `x ≤ 1/3`.** Xiang bisects the larger piece `1−x` into `((1−x)/2, (1−x)/2)`. Since `x ≤ 1/3 ⟺ (1−x)/2 ≥ x`, the sorted final pieces are `((1−x)/2, (1−x)/2, x)`, so
```
A = (1−x)/2 − (1−x)/2 + x = x,   equivalently  Liu = (1+x)/2.
```
For `x ≤ 1/3`: `Liu = (1+x)/2 ≤ (1+1/3)/2 = 2/3`, with strict inequality for `x < 1/3`. ✓

**Mode S (sliver), for `x ≥ 1/3`.** Xiang cuts a sliver of size `s` from the larger piece `1−x`, with `s = 1 − 2x` (note `s ≥ 0 ⟺ x ≤ 1/2`, and `s ≤ x ⟺ 1 − 2x ≤ x ⟺ x ≥ 1/3`, so the choice is admissible). The complement is `1 − x − s = x`, matching the other piece. Final pieces: `{x, x, s}`. Since `x ≥ 1/3 ≥ s = 1−2x` (the latter is `x ≥ 1−2x ⟺ 3x ≥ 1`), sorted `(x, x, s)`, so
```
A = x − x + s = s = 1 − 2x,   equivalently  Liu = (1 + (1−2x))/2 = 1 − x.
```
For `x ≥ 1/3`: `Liu = 1 − x ≤ 2/3`, with strict inequality for `x > 1/3`. ✓

**Equality.** At `x = 1/3` (the dyadic), both modes give `Liu = 2/3`. For `x ≠ 1/3`, at least one mode applies strictly: if `x < 1/3`, Mode B gives `(1+x)/2 < 2/3`; if `x > 1/3`, Mode S gives `1−x < 2/3`. Hence `c(1) ≤ 2/3`, equality iff Liu plays the dyadic. ∎ (Section 2)

> **Address of F2.** The `n=1` two-mode base is the clean special case of the dyadic/non-dyadic boundary: the threshold `x = 1/3 = α(1)` is exactly where the bisect-mode formula `(1+x)/2` and the sliver-mode formula `1−x` coincide at `2/3 = f(1)`. The sliver mode (regime N's prototype) handles `x ∈ (1/3, 1/2]`, which is **dominant** (`1−x ≥ 1/2`) — confirming the reviewer's point that the regime boundary cannot be dominant-vs-non-dominant.

### 3. Regime D (dyadic), all `n ≥ 1` — the equality / attainment upper bound (imported)

**Claim.** If `P` is the order-`n` dyadic, Xiang has a strategy (the pair-pile) with `≤ n` marks forcing `A = α(n)`, i.e. `Liu = f(n)`.

**Proof.** This is the certified pair-pile lemma (`lemmas/lemma-pair-pile-dyadic-cap.md`), reproduced for self-containment. For `n ≥ 2`, Xiang places one mark inside each of Liu's pieces of size `2^k/D(n)` for `k = 2, 3, …, n` (that is `n−1 ≤ n` marks), splitting: the piece `4/D(n)` into `(1, 3)/D(n)` (mark at distance `1/D(n)` from its left end); each piece `2^k/D(n)` for `k ≥ 3` into `(2^{k−1}, 2^{k−1})/D(n)` (mark at its midpoint). The pieces `1/D(n)` and `2/D(n)` are untouched. The final multiset (over `D(n)`) is
```
2^{n−1}, 2^{n−1}, 2^{n−2}, 2^{n−2}, …, 4, 4, 3, 2, 1, 1
```
which sums to `1 + 2 + (1+3) + Σ_{k=3}^{n} 2·2^{k−1} = 7 + (2^{n+1} − 8) = 2^{n+1} − 1 = D(n)`. ✓ Sorted into consecutive pairs, each pair `(2^{j}, 2^{j})` has excess `0` except the pair `(3, 2)` which has excess `1`. Hence `A = 1/D(n) = α(n)` and `Liu = (1+α(n))/2 = f(n)`. ✓ For `n = 1`: Xiang bisects the single piece `2/3` into `(1/3, 1/3)`, giving the pair-pile `1, 1, 1` over `3`, `A = 1/3`. ✓

Verification (exact rational): for `n = 2, 3, 4, 5`, the pair-pile's advantage sum is `1/D(n)` and `Liu = 2^n/D(n)` in every case (certified lemma).

> **Address of F3.** The pair-pile rescaling (the round-2 outline's "regime-D rescaling lemma" — apply `I(n)` on `R ∪ {L/2, L/2}`) **only fires when the rest `R` (scaled) is itself the order-`n` dyadic**, i.e. exactly at the dyadic config — the reviewer's F3. We therefore **restrict regime D to the dyadic config itself** (the genuine equality/attainment case) and let regime N carry every non-dyadic config (Sections 2 and 4). For a dominant but non-dyadic config, the cap is far below `α(n)` (verified `n=2`: dominant non-dyadic `(0.6, 0.3, 0.1)` has `Liu ≈ 0.55`, i.e. `A ≈ 0.1`, well below `α(2) = 1/7 ≈ 0.143`), achieved by regime-N sliver/pile-matching strategies, NOT by the dyadic rescaling.

### 4. The `n=2` upper bound, fully rigorous (a NEW four-strategy family; equality iff dyadic)

This section closes `U(2)` — previously open (round 1 had `L(2)` brute-force-corroborated but `U(2)` not separately proved). Liu config: three pieces `(a, b, c)`, `a ≤ b ≤ c`, `a + b + c = 1`. Xiang has `2` marks. Target: `A ≤ α(2) = 1/7`, equivalently `Liu ≤ 4/7 = f(2)`, strict for non-dyadic.

The order-2 dyadic is `(a, b, c) = (1/7, 2/7, 4/7)`.

We exhibit four Xiang strategies; for each we give an explicit mark placement and compute the resulting oddsum (hence `Liu`) exactly. For the sliver strategies, the value quoted is the **infimum** as the sliver `s → 0^+`; since `f(2) = 4/7` is achieved exactly by the pair-pile at the dyadic (Section 3), the infimum being `≤ 4/7` suffices for the upper bound at non-dyadic configs (Xiang picks `s` small enough that the oddsum is `> inf` but still `< 4/7`).

> **Computation convention.** Each strategy is described by where Xiang's two marks go; the final multiset is then sorted descending and `A = p_1 − p_2 + p_3 − p_4 + p_5` is read off. Equal pieces in a multiset always occupy consecutive ranks (ties are broken arbitrarily — the oddsum is the same for any tie-break among equal values, since swapping equal values between ranks of opposite parity does not change the alternating sum). In particular, a pair of equal pieces contributes `0` to `A` whenever the pair occupies consecutive ranks.

**Strategy A (match the 2nd-largest inside the largest).** Split `c` by two marks into `(b, (c−b)/2, (c−b)/2)` — admissible since `c ≥ b ⟹ c − b ≥ 0`. Final multiset: `{a, b, b, (c−b)/2, (c−b)/2}` — a pair `(b, b)` and a pair `((c−b)/2, (c−b)/2)` plus the singleton `a`. The two equal-pair members occupy consecutive ranks in every sort order of this multiset (each pair is a block, possibly nested), so each pair contributes `0`; the singleton `a` is at the remaining (odd) rank. Directly:
```
A_A = a (contribution of singleton),  Liu_A = (1+a)/2.
```
*(Check: sorted as `b, b, (c−b)/2, (c−b)/2, a` gives `A = b − b + (c−b)/2 − (c−b)/2 + a = a`; any other admissible sort gives the same by the equal-pair block argument.)*

**Strategy B (bisect the largest, then a sliver).** Mark 1 bisects `c → (c/2, c/2)`. Mark 2 cuts a sliver `s → 0^+` from one `c/2`, giving `(s, c/2 − s, c/2)`. Final multiset (limit `s → 0`): `{a, b, c/2, c/2, 0}`. The two equal pieces `c/2, c/2` occupy consecutive ranks (with the sliver `s` at the smallest rank), so their contribution to `A` cancels. Direct enumeration over the three possible relative orders of `c/2` against `b` and `a`:
- If `c/2 ≥ b`: sort `c/2, c/2, b, a, s` → `A = c/2 − c/2 + b − a + s → b − a`.
- If `b ≥ c/2 ≥ a`: sort `b, c/2, c/2, a, s` → `A = b − c/2 + c/2 − a + s → b − a`.
- If `a ≥ c/2` (balanced, e.g. `a = b = c = 1/3`): sort `b, a, c/2, c/2, s` → `A = b − a + c/2 − c/2 + s → b − a`.

In every case `A_B (inf) = b − a`, hence `Liu_B (inf) = (1 + b − a)/2`. ✓

**Strategy C (split the smallest into two halves plus a sliver).** Two marks split `a` into `(s, a/2, a − a/2 − s)` — admissible for `s → 0^+` (the two non-sliver pieces both approach `a/2`). Final multiset (limit): `{a/2, a/2, b, c, 0}`. Since `a/2 ≤ b ≤ c`, the sorted order is `c, b, a/2, a/2, s`, with the two equal `a/2`'s at consecutive ranks 3, 4. Hence
```
A_C (inf) = c − b + a/2 − a/2 + s → c − b,   Liu_C (inf) = (1 + c − b)/2.
```
(Equivalently, reading the oddsum directly: `c + a/2 + s → c + a/2`; using `a + b + c = 1` one checks `c + a/2 = (1 + c − b)/2`, so the two forms agree.)

**Strategy E (match the 2nd-largest inside the largest, plus a sliver from the smallest).** Mark 1 splits `c` into `(b, c − b)` — admissible. Mark 2 cuts a sliver `s → 0^+` from `a`, giving `(s, a − s)`. Final multiset (limit): `{b, b, c − b, a, 0}` — the original `b` plus the `b` cut from `c` form an equal pair (consecutive ranks, contributing `0`), and the remaining three pieces `{c − b, a, 0}` contribute `±(c − b − a) + 0` depending on which of `c − b`, `a` is larger:
```
A_E (inf) = |c − b − a| = |c − (a + b)| = |2c − 1|,    Liu_E (inf) = (1 + |2c − 1|)/2 = max(c, 1 − c).
```
(If `c ≥ 1/2`, `|2c − 1| = 2c − 1` so `Liu = c`; if `c < 1/2`, `Liu = 1 − c = a + b`.) ✓

So **the four strategy bounds (infima, except Strategy A which is exact) are**:
```
Liu_A    = (1 + a)/2           (exact)
Liu_B*   = (1 + b − a)/2       (infimum)
Liu_C*   = (1 + c − b)/2       (infimum)
Liu_E*   = max(c, 1 − c)       (infimum)
```
*(We re-verify all four formulas by direct sort enumeration in the python check below.)*

**Claim.** `min(Liu_A, Liu_B*, Liu_C*, Liu_E*) ≤ 4/7`, with equality iff `(a, b, c) = (1/7, 2/7, 4/7)`.

**Proof of the claim.** Translate each bound to a condition on `(a, b, c)` with `a + b + c = 1`, `a ≤ b ≤ c`:
- `Liu_A ≤ 4/7` ⟺ `(1 + a)/2 ≤ 4/7` ⟺ `a ≤ 1/7`.
- `Liu_B* ≤ 4/7` ⟺ `(1 + b − a)/2 ≤ 4/7` ⟺ `b − a ≤ 1/7`.
- `Liu_C* ≤ 4/7` ⟺ `(1 + c − b)/2 ≤ 4/7` ⟺ `c − b ≤ 1/7`.
- `Liu_E* ≤ 4/7` ⟺ `max(c, 1 − c) ≤ 4/7` ⟺ `3/7 ≤ c ≤ 4/7`.

Suppose, for contradiction, that **all four bounds are `> 4/7`** (i.e. none of the four strategies alone caps `Liu` at `4/7`). Then:
- `a > 1/7`,  (i)
- `b − a > 1/7`,  (ii)
- `c − b > 1/7`,  (iii)
- `c < 3/7` **or** `c > 4/7`.  (iv)

From (i)–(iii): `c > b + 1/7 > a + 2/7 > 3/7`. So `c > 3/7`, forcing the second alternative of (iv): `c > 4/7`. Then `a + b = 1 − c < 3/7`. But from (i) and (ii): `b > a + 1/7 > 2/7`, so `a + b > a + (a + 1/7) = 2a + 1/7 > 2/7 + 1/7 = 3/7`. **Contradiction** (`a + b < 3/7` and `a + b > 3/7`).

Hence at least one of the four bounds is `≤ 4/7`. **Equality analysis.** For equality `min = 4/7` (all four `≥ 4/7`), the same four conditions hold with `≥`:
- `a ≥ 1/7`, `b − a ≥ 1/7`, `c − b ≥ 1/7`, and `c ≥ 4/7` or `c ≤ 3/7`.
From the first three (with `≥`): `c ≥ b + 1/7 ≥ a + 2/7 ≥ 3/7`. If `c ≤ 3/7`, then `c = 3/7` and all intermediate inequalities are equalities: `a = 1/7, b = 2/7, c = 3/7` — but then `a + b + c = 6/7 ≠ 1`. ✗. So `c ≥ 4/7`, giving `a + b = 1 − c ≤ 3/7`; combined with `a + b ≥ 2a + 1/7 ≥ 3/7` (from `a ≥ 1/7`), equality throughout: `a = 1/7, b = 2/7, c = 4/7`. ✓ — the dyadic.

Hence `min ≤ 4/7` always, equality iff the dyadic. ∎ (Claim)

**Conclusion of `U(2)`.** For every `n=2` Liu config, at least one of `A, B, C, E` gives `Liu ≤ 4/7` (Strategy A exactly; the sliver strategies in the limit, hence `Liu < 4/7` strictly for non-dyadic by choosing `s` small enough; at the dyadic, Strategy A and the pair-pile both give exactly `4/7`). Combined with `L(2)` (round-1 certified, brute-force-corroborated: min over `3240` Xiang responses is `4/7`), this pins **`c(2) = 4/7`**. ∎ (Section 4)

> **Address of F1.** The reviewer (F1, finding 2) flagged that the round-2 outline's regime-N mechanism "non-dominant ⟹ `A ≤ 0` (Liu ≤ 1/2)" is **verified FALSE** — non-dominant `n=2` configs give caps `≈ 0.503–0.525` (i.e. `A ≈ 0.006–0.05`, above `0`, but still `< α(2) = 1/7`). The four-strategy proof above is the **correct mechanism**: it proves `Liu ≤ 4/7` directly (via pile-matching + slivers, NOT via `A ≤ 0`), and the strict-inequality region for non-dyadic configs is the slack `4/7 − min(A,B,C,E*) > 0`, which can be (and on the data, is) a small positive number rather than `4/7 − 1/2 = 1/14`. No claim of `A ≤ 0` is made anywhere in this proof.

**Computational verification of the four strategy formulas.** (python, exact rational arithmetic; checks the closed-form `Liu` against the direct oddsum of the explicitly-constructed final multiset for several configs.) — included in the build log `/tmp/round-2/proof-builder-two-regime-disjunctive.md`.

### 5. The general-`n` regime-D upper bound at the dyadic (already in Section 3) and the regime-N gap for `n ≥ 3`

Regime D (the dyadic) is fully handled for all `n` by Section 3's pair-pile. **Regime N for `n ≥ 3` is the open gap.** The `n=2` four-strategy proof is a template, but the strategies `A, B, C, E` are each `n=2`-specific:
- Strategy A "match the 2nd-largest inside the largest" uses `2` marks (one per resulting sub-piece minus one); for `n ≥ 3` one would need to recursively match the next pieces, consuming more marks than available.
- The bound `min(A, B, C, E) ≤ f(2)` is a finite `4`-way inequality in `3` variables; its general-`n` analogue would be a `(2^n − 1)`-way inequality in `n+1` variables, and the clean contradiction argument (Section 4) does not lift in any obvious way.

**Honest statement of the gap.** I do not have a general-`n` regime-N proof. The conjecture (strongly supported by fine-grid computation for `n=3`: dyadic `(1,2,4,8)/15` gives min-oddsum exactly `8/15 = f(3)`, and every tested non-dyadic `n=3` config gives strictly less, e.g. `(1/4, 1/4, 1/4, 1/4)` → `0.514 < 8/15 ≈ 0.533`) is:

> **(Conjecture — regime N general `n`.)** For every non-dyadic order-`n` Liu config, Xiang with `n` marks has a strategy forcing `Liu < f(n)` strictly.

This is the headline open gap of the approach. I do not paper over it.

### 5b. Round 3 — Engine R-pile tested and FALSIFIED; dyadic-ratio overshoot lemma

The round-3 dispatch instructed this builder to close G2 (regime-N upper bound for `n ≥ 3`) via **Engine R-pile** — greedy recursive pile-matching of the two largest pieces (cut `a_2` out of `a_1` when `a_1 ≥ 2 a_2`; bisect-`a_1` fallback when `a_1 < 2 a_2`), generalizing the `n = 1` sliver mode and `n = 2` Strategy A. I implemented the engine in python (exact rational arithmetic) and stress-tested it. **It does not close G2.** The falsification is documented with counterexamples below; the consecutive-rank invariant the reviewer asked for (required fix #1) is shown to be MOOT — the greedy's failure is suboptimality, not interleaving. One clean rigorous result survives: the **dyadic-ratio overshoot lemma** (the dyadic-detection, required fix #3), stated and proved at the end of this section.

#### 5b.1 The engine (literal implementation)

The engine, as the outliner describes it, operates on the full current multiset (the frozen pairs are NOT excluded from the recursion):

> **(Greedy R-pile).** While marks remain and ≥ 2 pieces exist: sort the current pieces descending; let `a_1 ≥ a_2` be the two largest. If `a_1 ≥ 2 a_2` (admissible), place one mark cutting `a_2` out of `a_1`, i.e. replace `a_1` by `{a_2, a_1 − a_2}` (adding one new copy of `a_2`, pairing with the pre-existing `a_2`). If `a_1 < 2 a_2` (balanced), bisect `a_1` into `(a_1/2, a_1/2)`.

The "canceling pair" the engine intends to create is `{the new a_2, the pre-existing a_2}` — two equal pieces that, if they occupy consecutive sorted ranks, contribute `0` to `A`. The hope (outliner's load-bearing lemma) was that this cancellation is maintained inductively across steps and drives `A < α(n)` for non-dyadic configs.

#### 5b.2 Counterexample (i) — the exact dyadic (known, now characterized)

On the order-3 dyadic `(8, 4, 2, 1)/15` (so `α(3) = 1/15`, `f(3) = 8/15`): the two largest are `8, 4`, and `8 = 2·4` (exact dyadic ratio). The greedy cuts `4` out of `8`, replacing `8` by `{4, 4}`. The multiset becomes `{4, 4, 4, 2, 1}/15` — **THREE copies of `4`** (the pre-existing `4` plus two new `4`'s, since `8 − 4 = 4`). An odd-multiplicity block of `4`'s occupies ranks `1, 2, 3`, contributing `+4 − 4 + 4 = +4`; the tail `(2, 1)` contributes `−2 + 1 = −1`. So `A = 4 − 1 = 3` over `15`, i.e. `A = 1/5`, `Liu = 3/5 > 8/15`. **Overshoot** — verified by exact computation. (The pair-pile, regime D, caps the dyadic at exactly `8/15` instead; the greedy is regime-N only, as the explorer already flagged.)

#### 5b.3 Counterexample (ii) — balanced non-dyadic (the bisect fallback FAILS)

On `(.5, .3, .15, .05) = (10, 6, 3, 1)/20` (non-dyadic; `a_1 = 0.5 < 2 a_2 = 0.6`, balanced): the greedy bisects `0.5 → (0.25, 0.25)`. Multiset `{0.3, 0.25, 0.25, 0.15, 0.05}`; sorted, the two largest are `0.3, 0.25`, and `0.3 < 2·0.25 = 0.5` — balanced again, bisect `0.3 → (0.15, 0.15)`. Third mark: bisect `0.25`. Final multiset (3 marks) `{0.25, 0.25, 0.15, 0.15, 0.15, 0.05, ...}`, `A = 1/10`, `Liu = 11/20 = 0.55 > 8/15 ≈ 0.533`. **The bisect fallback overshoots** (verified exactly: `Liu = 11/20`). The true optimal Xiang cap on this config is `31/60 ≈ 0.5167 < 8/15` (verified by brute force, grid `N = 60`), so the conjecture holds — the greedy just fails to find it. The bisect fallback creates a canceling pair `(a_1/2, a_1/2)` but pushes the residual structure into a configuration where subsequent steps keep being balanced, never driving `A` below `α(n)`. No clean recursive rule replaces the `n = 2` four-strategy template here (required fix #2 has no `n ≥ 3` solution within the greedy family).

#### 5b.4 Counterexample (iii) — extreme-dominant with tiny tail

On `(0.9, 1/30, 1/30, 1/30)` (non-dyadic; `a_1 = 0.9 ≥ 2 a_2 = 1/15`, admissible): the greedy cuts `a_2 = 1/30` out of `0.9`, replacing `0.9` by `{1/30, 0.9 − 1/30 = 26/30}`. The cancellation removes only `1/30 ≈ 0.033` from the advantage; the residual `26/30 ≈ 0.867` still dominates. Iterating, the greedy barely reduces `A` — best `Liu` over `1, 2, 3` marks is `0.9` (no improvement, since each cut removes only a sliver). **The greedy fails catastrophically on extreme-dominant configs with tiny tail** — verified on a grid sweep of `86` dominant `n = 3` configs (`N = 30`): `42` of them FAIL to cap below `8/15`. The true optimal Xiang cap on these configs is `31/60` (verified by brute force), so the conjecture holds; the greedy is simply the wrong strategy.

#### 5b.5 Why the consecutive-rank invariant is moot (reviewer's required fix #1)

The reviewer asked for an inductive proof that the greedy's canceling pairs land at consecutive sorted ranks across multiple steps (the interleaving wall that killed Hall). I tested this directly: the failure mode of the greedy is NOT interleaving. It is **suboptimality**. Specifically, once a frozen pair `(a_2, a_2)` forms, the full-multiset greedy (which the outliner describes, recursing on the full multiset) treats the pair members as candidates for `a_2` in the NEXT step — and since they are large, the next step often picks a frozen pair member as `a_2`, finds `a_1 < 2 a_2` (balanced, because the residual is now smaller), and **bisects a frozen pair member**, destroying the cancellation that was already in hand. This is visible in trace `(.6, .25, .1, .05)`: step 1 strict-dominant creates pair `(0.25, 0.25)` with residual `0.35`; step 2 sees `a_1 = 0.35, a_2 = 0.25` (a frozen pair member), balanced, bisects `0.35`; step 3 sees `a_1 = 0.25, a_2 = 0.25` (both frozen), bisects `0.25`. Final `Liu = 3/5 ≫ 8/15`.

The interleaving wall (a residual piece landing between the two members of a created pair) is a genuine obstruction for a GLOBAL Hall matching, but the greedy controls the sort locally at each step, so interleaving per se does not occur. The problem is that "controlling the sort locally" is not enough — the greedy picks a BAD cut, and no refinement of the consecutive-rank invariant fixes that. The invariant (even-multiplicity of created pairs) DOES hold when `a_1 > 2 a_2` strictly at every step (see the lemma below), but holding the invariant does not imply `A < α(n)` — the residual structure can still exceed `α(n)`. Required fix #1 is therefore MOOT for closing G2.

#### 5b.6 The dyadic-ratio overshoot lemma (NEW, rigorous; reviewer's required fix #3 — dyadic detection)

The one clean result that survives is a complete characterization of when ONE greedy step cancels its created pair. This is the dyadic-detection the reviewer asked for.

> **Lemma (dyadic-ratio overshoot, one-step).** Consider a greedy pile-match step on a multiset, acting on the two largest pieces `a_1 ≥ a_2` with `a_1 ≥ 2 a_2` (admissibility). The step replaces `a_1` by `{a_2, a_1 − a_2}` (cutting `a_2` out of `a_1` with one mark). Let `m` be the multiplicity of the value `a_2` in the multiset BEFORE the step (so `m ≥ 1`, since `a_2` is the 2nd-largest and at least one piece of size `a_2` exists). After the step, the multiplicity of `a_2` is `m + 2` if `a_1 − a_2 = a_2` (i.e. `a_1 = 2 a_2`, the **dyadic ratio**), and `m + 1` otherwise (i.e. `a_1 > 2 a_2`, **strict-dominant**).
>
> - **Strict-dominant case (`a_1 > 2 a_2`).** The multiplicity of `a_2` changes by `+1` (from `m` to `m + 1`). In particular, if `m` was odd (the typical case `m = 1`, since `a_2` is the 2nd-largest and ties at `a_2` are non-generic), it becomes EVEN (`m + 1 = 2`): the `a_2`-block has even multiplicity, occupies a contiguous range of ranks in the sorted order, and the equal-pair members pair up to contribute `0` to `A`. The residual `a_1 − a_2 > a_2` sits strictly ABOVE the `a_2`-block in the sorted order. **The created pair cancels.**
> - **Dyadic-ratio case (`a_1 = 2 a_2`).** The multiplicity of `a_2` changes by `+2` (from `m` to `m + 2`). In particular, if `m = 1` (the typical case), it becomes `3` (ODD): the `a_2`-block has odd multiplicity, occupying ranks `r, r+1, r+2` for some `r`, contributing `(−1)^{r+1} a_2 ≠ 0` to `A`. **The created "pair" does NOT cancel — the greedy overshoots.**

**Proof.** The step removes one piece of size `a_1` and adds two pieces of sizes `a_2` and `a_1 − a_2`. The multiplicity of the value `a_2` after the step equals (its multiplicity before) plus `1` (for the newly-added `a_2`) plus `1` more iff `a_1 − a_2 = a_2`. So the change is `+1` (strict-dominant) or `+2` (dyadic ratio). For the contribution to `A`: equal pieces occupy a contiguous block of ranks in the sorted descending order (any tie-break; equal pieces are indistinguishable). A block of even multiplicity contributes `0` to the alternating sum (the equal values cancel in adjacent-rank pairs `(r, r+1), (r+2, r+3), …`, each pair contributing `±v ∓ v = 0`); a block of odd multiplicity contributes `±v` (one unpaired leftover). Hence strict-dominant (`m` odd → `m+1` even) cancels; dyadic ratio (`m = 1` → `m+2 = 3` odd) overshoots. ∎

**Corollary (dyadic detection).** The greedy pile-match step cancels its created pair iff the cut is strict-dominant (`a_1 > 2 a_2`). The order-`n` dyadic config has `a_1 = 2 a_2` at every level (telescoping: the largest piece is `2^n / D(n)`, the 2nd-largest is `2^{n−1} / D(n)`, and `2^n / D(n) = 2 · 2^{n−1}/D(n)`; the residual after cutting is `2^{n−1}/D(n) = a_2`, and the same ratio holds recursively). Hence the greedy overshoots on the dyadic at every step — confirming the greedy is a **regime-N tool only**, and the dyadic MUST be detected and routed to the pair-pile (regime D, Section 3). This is the dyadic-detection condition the reviewer required (fix #3).

**Verification.** Exact rational arithmetic (python): one-step multiplicity check on three representative cuts — `(8,4)/15` (`a_1 = 2 a_2`, mult `1 → 3`, ODD, overshoot, `A = 1/5`); `(9,4)/16` (`a_1 > 2 a_2`, mult `1 → 2`, EVEN, cancel); `(0.6, 0.25)` (`a_1 > 2 a_2`, mult `1 → 2`, EVEN, cancel). All match the lemma. (The overshoot on the full dyadic `(8,4,2,1)/15 → A = 1/5` and the cancel on `(9,4,2,1)/16 → A = 1/4`, `(0.6, 0.25, 0.1, 0.05) → A = 3/10` after one strict-dominant step are also confirmed.)

#### 5b.7 Honest synthesis of round 3

The regime-N upper bound for `n ≥ 3` remains OPEN. Engine R-pile does not close it (three classes of counterexamples). The consecutive-rank invariant is moot (the failure is suboptimality). The dyadic-ratio overshoot lemma is the sole new rigorous contribution — it cleanly characterizes the dyadic-detection but does not constitute a regime-N proof. A genuinely different mechanism is needed for regime-N. Candidate (not proved, recorded for a future round): an **even-block / multiplicity-parity** strategy — Xiang uses his `n` marks to make every piece of value `≥ α(n)` have EVEN multiplicity in the final `2n + 1`-piece multiset, leaving only pieces `< α(n)` (sliverable to `0`) at odd multiplicity, forcing `A < α(n)`. The obstruction: `2n + 1` is odd, so an odd number of values have odd multiplicity; on the dyadic, the pair-pile's residual `(3, 2)`-pair is exactly the irreducible odd-multiplicity excess `α(n)`, and the conjecture is that for non-dyadic configs Xiang can push all odd-multiplicity excess below `α(n)`. This is a different framing from the greedy (it targets multiplicity parity, not pile-matching), and it is NOT proved here — flagged as a direction for the outliner.

### 6. The lower bound (Lemma L) — dependency on a sibling, not re-proved

The lower bound half of the claim, `c(n) ≥ f(n)`, is Liu's guarantee when she plays the dyadic: for **every** Xiang response, the odd-rank sum of the final pieces is `≥ f(n)`. This is Lemma L (round 1, open for general `n`). The sibling `pairing-partner` attacks it via the `M ⊎ R` self-similar decomposition + single-aux `L*(n)` strengthened IH (the k=1 sub-case is verified; k≥2 open). I import that route as a dependency and do not re-prove it here. For `n = 1, 2`, `L(1)` and `L(2)` are round-1-certified (L(2) by exhaustive casework + brute force), so `c(1) = 2/3` and `c(2) = 4/7` are fully rigorous end-to-end by this approach + the sibling.

### 7. Synthesis

| `n` | upper bound `c(n) ≤ f(n)` | lower bound `c(n) ≥ f(n)` | status |
|-----|---------------------------|--------------------------|--------|
| `1` | Section 2 (rigorous, corrected two-mode) | round-1 certified `L(1)` | **solved** (`c(1)=2/3`) |
| `2` | Section 4 (rigorous, four-strategy family) | round-1 certified `L(2)` | **solved** (`c(2)=4/7`) |
| `≥ 3` dyadic | Section 3 (pair-pile, imported, rigorous) | Lemma L (open) | regime-D upper bound only |
| `≥ 3` non-dyadic | **OPEN** (Conjecture, Section 5; Engine R-pile FALSIFIED, Section 5b) | — | regime-N upper bound open |
| `≥ 3` general | partial | partial (sibling) | **partial** |

**Final answer (conjectured, verified `n=1..5`):** `c(n) = 2^n / (2^{n+1} − 1)`, rigorously established for `n = 1, 2`. The general-`n` upper bound at the dyadic (regime D) is rigorous via the pair-pile; the general-`n` regime-N upper bound and the general-`n` lower bound are the two open gaps. **Round 3:** the greedy R-pile engine (the dispatched mechanism for regime-N) is RULED OUT by counterexamples (Section 5b); the dyadic-ratio overshoot lemma (Section 5b.6) is the new rigorous contribution — it gives dyadic-detection but does not close regime-N. A multiplicity-parity / even-block framing is flagged for a future outliner.

---

## Round 4 outline (REVISE — replace the dead R-pile engine with the structural equality-case classification)

**Framing (unchanged at the top level):** disjunctive dyadic/non-dyadic regime
split for the upper bound G2. Regime D (dyadic Liu) = certified pair-pile
(imported). Regime N (non-dyadic Liu) — the R-pile greedy engine is
FALSIFIED (3 counterexample classes, recorded); this round replaces it with a
NEW regime-N engine: the **structural equality-case classification** of
`A = α(n)`.

**Target (the whole claim):** `c(n) = f(n)` end-to-end. This approach owns G2
(regime-N: for every non-dyadic Liu config, Xiang forces `A < α(n)`). G1
(Lemma L general-n) stays a tracked dependency on `pairing-partner`.

**The new regime-N mechanism (Explorer 3's minimizer census, lifted).** The
grid equality-case census (n=3,4,5) shows: every grid minimizer of `A` on the
dyadic Liu config has its odd-multiplicity pieces forming either `{1}` (odd
piece-count, mirror family) or `{2^j, 2^j+1}` consecutive powers of two (even
piece-count, pair-pile family), and in both cases `A·D(n) = 1`. The regime-N
conjecture is the CONTRAPOSITIVE for non-dyadic Liu: the equality structure
`{1}` / `{2^j, 2^j+1}` is **dyadic-Liu-locked** — it is realizable as a
minimizer ONLY when Liu's config is the dyadic. For non-dyadic Liu, Xiang can
force a config whose odd-mult leftover is strictly below the dyadic-level
boundary `α(n)` (a sub-`α` sliver at a canceling odd rank, generalizing the
certified U(1)/U(2) sliver mode), giving `A < α(n)` strictly.

**Skeleton (the gap steps, NOT a finished proof):**
1. **Import** Lemma G, pair-pile + mirror (regime D, all n), U(2) four-strategy
   (the n=2 closed form `Φ_2 = min(a, b−a, c−b, |2c−1|)`, max uniquely at
   dyadic), dyadic-ratio overshoot (dyadic detection). (All certified.)
2. **GAP (the hard step — lift the grid equality-case classification to a
   real-valued regime-N forcing).** Prove: for every non-dyadic level-`n` Liu
   config, Xiang has a strategy (existence, NOT necessarily greedy) whose
   final odd-mult leftover is a sub-`α(n)` sliver at a canceling odd rank,
   forcing `A < α(n)`. The mechanism to name: the
   `{1}` / `{2^j, 2^j+1}` equality structure requires Liu's pieces to sit at
   exact dyadic ratios `2^j : 2^{j+1}` (so the pair-pile's equal pairs and the
   mirror's symmetric pairs form); off the dyadic, at least one Liu ratio is
   non-dyadic, and Xiang's sliver cut breaks the would-be-equal pair into a
   sliver + complement, the sliver landing at a canceling odd rank (the
   certified n=1 `±a` mechanism, generalized).
3. **Regime-D / regime-N disjunction.** Regime D handled by the pair-pile
   (equality `A = α(n)`). Regime N: the sliver forcing of step 2 gives strict
   `A < α(n)`. The two regimes are exhaustive (dyadic vs not).
4. Conclude `c(n) ≤ f(n)`, equality iff dyadic. G1 imported from
   `pairing-partner`.

**Key lemmas (claim + one-line mechanism):**
- Equality structure is dyadic-Liu-locked — because the `{2^j, 2^j+1}`
  consecutive-powers pair requires the two adjacent Liu pieces to be in exact
  ratio `2^j : 2^{j+1}` (a dyadic ratio), recursively at every level; off the
  dyadic, no such pairing exists.
- Non-dyadic ⇒ Xiang sliver forces `A < α` — because a non-dyadic Liu ratio
  leaves a non-cancellable residual at the would-be-pair rank, and Xiang's
  sliver (generalizing U(1)/U(2)) shaves it below `α(n)`.

**Open gaps (builder fills):**
- Step 2 — the real-valued non-dyadic sliver forcing. This is the honest wall:
  the grid census is empirical only; lifting to reals requires proving the
  sliver lands at a canceling odd rank for EVERY non-dyadic config (not just
  the tested ones). Numerically robust (1200 random non-dyadic n=3 configs,
  max `Φ = 0.0595 < α(3) = 0.0667`, zero near-misses) but no proof technique
  is yet visible.
- The classification is shared with the new `equality-case-classification`
  approach — if the real classification fails, both the G2 half here and that
  approach die together (single-gap-trap risk, flagged honestly). The
  divergence: THIS approach stays within the disjunctive regime-D/regime-N
  split (G2 only, G1 imported); `equality-case-classification` drops the
  regime split and attacks both gaps from one classification.

**Cases to cover:** balanced non-dyadic (sliver drives `A → 0`),
dominant-non-dyadic (sliver shaves the dominant piece's would-be partner),
extreme-dominant tiny-tail (the R-pile's failure class — the sliver forcing
must handle these, where the greedy did not).

**Watch out for:** do NOT reuse the R-pile greedy (falsified, 3
counterexample classes). Do NOT claim the classification alone closes G2 —
it gives `A ≠ α` off the dyadic, but the SIDE (`A < α` not `A > α`) needs
the sliver forcing. The (U-E) variational statement (Explorer 2) restates
this gap; do NOT import (U-E) as a closure. The `M − total(R) = α(n+1)`
identity is dyadic-only (foreclosed, A4) — do NOT retry a unified-potential.

---

### 5c. Round 4 — the new regime-N engine: grid classification + sliver forcing

The round-4 dispatch replaced the falsified R-pile with a new regime-N engine built from two ingredients the explorers surfaced: (a) the **structural equality-case classification** of `A = α(n)` (corpus-compute A2: grid minimizers' odd-multiplicity leftovers are `{1}` or `{2^j, 2^j+1}`), and (b) **sliver forcing** for non-dyadic configs (the certified `U(1)`/`U(2)` `±a` mechanism generalized). I develop each as far as I can justify rigorously, and state the open wall honestly. The grid classification is proved cleanly (it is a repackaging of the certified integer-grid parity theorem); the real-valued universal sliver forcing is NOT proved — I cover three structural classes rigorously and leave the rest as the honest gap.

#### 5c.1 Grid equality-case classification (rigorous, grid-only, all n)

We work on the integer grid `1/D(n)` and restrict to **Liu's level-`n` dyadic config** (pieces `(1, 2, 4, …, 2^n)/D(n)`). Recall `D(n) = 2^{n+1} − 1` is ODD. We import the certified **integer-grid parity theorem** (`lemmas/lemma-grid-parity.md`): for any Xiang refinement whose combined marks are at multiples of `1/D(n)`, scaling lengths by `D(n)` gives positive integers `q_1 ≥ q_2 ≥ … ≥ q_M` summing to `D(n)`, and the scaled advantage `A* := A·D(n) = Σ (−1)^{i+1} q_i` is a non-negative odd integer, hence `A* ≥ 1`, i.e. `A ≥ α(n)`. Equality `A = α(n)` ⟺ `A* = 1`. We now read off the structural consequence.

> **Proposition (grid equality-case, necessary condition).** At the level-`n` dyadic Liu config, for a grid-aligned Xiang refinement producing `M` final pieces (scaled integers `q_1 ≥ … ≥ q_M`, `Σ q_i = D(n)` odd), `A·D(n) = 1` iff one of:
> - **(odd `M = 2m+1`)** every pair-excess `e_i := q_{2i−1} − q_{2i}` is `0` (so `q_{2i−1} = q_{2i}` for `i = 1, …, m` — all pieces pair up equally) **and** the leftover smallest piece `q_{2m+1} = 1`;
> - **(even `M = 2m`)** exactly one pair-excess `e_i = 1` (so `q_{2i−1} = q_{2i} + 1` for one `i`, and `q_{2j−1} = q_{2j}` for all `j ≠ i`) and all other pair-excesses are `0`.
>
> Equivalently: in multiset terms, the values of ODD multiplicity are either `{1}` (odd count; a single leftover piece of value `1`) or `{a, a+1}` for some integer `a ≥ 1` (even count; one pair of consecutive integers unpaired, the larger at the odd rank).

**Proof.** Pair consecutive sorted pieces. For even `M = 2m`: `A* = Σ_{i=1}^{m} e_i` with each `e_i ≥ 0` (sorted), and `Σ e_i ≡ D(n) ≡ 1 (mod 2)` (certified parity lemma: `e_i ≡ q_{2i−1} + q_{2i} (mod 2)`, summing to `Σ q_i = D(n)`, odd). So `Σ e_i` is a non-negative odd integer, hence `≥ 1`; equality `Σ e_i = 1` forces exactly one `e_i = 1` and the rest `0`. A pair with `e_i = 0` has `q_{2i−1} = q_{2i}` (the two values are equal, even-multiplicity in the multiset sense modulo other pairs); the lone pair with `e_i = 1` has `q_{2i−1} = q_{2i} + 1`, contributing the two consecutive odd-multiplicity values `{q_{2i}, q_{2i} + 1}`. For odd `M = 2m+1`: `A* = Σ_{i=1}^{m} e_i + q_{2m+1}` with `Σ e_i ≥ 0` and `q_{2m+1} ≥ 1` (positive integer). Equality `A* = 1` forces `Σ e_i = 0` (all pairs equal) and `q_{2m+1} = 1` (the single odd-multiplicity value is `1`). ∎

> **Honest scope.** This is a NECESSARY condition on equality, derived from parity alone. The corpus-compute census (A2) further observed that the *achievable* odd-multiplicity leftovers are exactly `{1}` (mirror family) and `{2^j, 2^j+1}` for `j = 0, 1, …, n−1` (pair-pile family) — i.e. the smaller consecutive value is always a power of two. The parity theorem does NOT force `a = 2^j`: it permits any `a ≥ 1`. The refinement "`a` is a power of two" is a statement about which strategies Xiang can realize with ≤ `n` marks, witnessed empirically by the census (the pair-pile gives `{2, 3}`; the mirror gives `{1}`; the other `{2^j, 2^j+1}` minimizers are observed but not explicitly constructed here). I do NOT claim the refinement as proved. Combined with the certified pair-pile (an explicit construction attaining `A = α(n)`), this gives `min_{grid-aligned Xiang} A = α(n)` at the dyadic, with the necessary structural condition above on the equality case.

#### 5c.2 The real-valued lift — honest gap (no proof technique)

The grid classification above is tied to the grid quantum `1/D(n)`. The certified grid-parity lemma explicitly flags (its "The lift fails" caveat) that on a finer grid `1/(K·D(n))` with `K` odd, the parity argument yields only `A ≥ 1/(K·D(n))`, strictly weaker than `α(n) = 1/D(n)` for `K > 1`; and for arbitrary real marks, the smallest piece can be sub-`1/D(n)`, defeating the CK cheap-kill on the odd-count sub-case. So the grid classification does NOT lift to reals. The round-4 outline-reviewer and outliner both flag this as the honest wall ("no proof technique visible" — outline-reviewer, `two-regime-disjunctive` APPROVE-to-revise). I do not have a real-valued classification; the sliver-forcing lemmas below handle specific structural classes directly over the reals, bypassing the (unavailable) classification lift.

#### 5c.3 Sliver-forcing Lemma S1 — balanced config, ALL n ≥ 1 (rigorous, promotable)

> **Lemma S1 (balanced-config sliver forcing).** Let Liu play the balanced config of `n + 1` equal pieces `(w, w, …, w)`, `w = 1/(n+1)`. Then Xiang with at most `n` marks has a strategy forcing `A(final) ≤ 2s` for every `s > 0` with `s < w/2`; in particular `inf_Xiang A = 0 < α(n)`. Hence for the balanced non-dyadic config, `Φ(Liu) = 0 < α(n)` strictly (regime N).

**Strategy.** Two cases by the parity of `n`.
- **`n` odd.** Xiang uses all `n` marks, each cutting a sliver of size `s` from a distinct one of the `n` "non-leftover" pieces (leaving one piece untouched). Each cut piece `w` becomes `(w − s, s)`. Final multiset: one piece `w`, `n` pieces `w − s`, `n` pieces `s` (total `2n + 1` pieces). For `s < w/2` the sort is `w > w − s > s`, so sorted descending: `w`, then `n` copies of `w − s` (ranks `2, …, n+1`), then `n` copies of `s` (ranks `n+2, …, 2n+1`).
- **`n` even.** Xiang uses 1 mark to bisect one piece `w → (w/2, w/2)`, and `n − 1` marks each cutting a sliver `s` from a distinct one of the remaining `n − 1` of the `n` non-bisected non-leftover pieces (leaving one piece untouched). Final multiset: one `w`, `n − 1` pieces `w − s`, `n − 1` pieces `s`, two pieces `w/2` (total `2n + 1` pieces). For `s < w/2` the sort is `w > w − s > w/2 > s`, so sorted descending: `w`, then `n − 1` copies of `w − s` (ranks `2, …, n`), then two copies of `w/2` (ranks `n+1, n+2` — consecutive, cancelling), then `n − 1` copies of `s` (ranks `n+3, …, 2n+1`).

**Computation of `A`.** Let `T_1 = Σ_{i=2}^{M_1+1} (−1)^{i+1}` be the sign-sum over the `w − s` block and `T_2 = Σ_{i} (−1)^{i+1}` over the `s` block (the `w/2` block contributes `0` since its two equal members sit at consecutive ranks of opposite sign).
- *`n` odd:* the `w − s` block has `n` (odd) members starting at sign `−`; `T_1 = −1`. The `s` block has `n` (odd) members, the first at rank `n + 2` with sign `(−1)^{n+3} = (−1)^n · (−1)^3 = −(−1)^n = +1` (since `n` odd); `T_2 = +1`. Hence `A = w + (w − s)·(−1) + s·(+1) = w − (w − s) + s = 2s`.
- *`n` even:* the `w − s` block has `n − 1` (odd) members starting at sign `−`; `T_1 = −1`. The `w/2` block contributes `0`. The `s` block has `n − 1` (odd) members, first at rank `n + 3` with sign `(−1)^{n+4} = (−1)^n = +1` (since `n` even); `T_2 = +1`. Hence `A = w + (w − s)·(−1) + 0 + s·(+1) = 2s`.

In both cases `A = 2s`. Choosing `s < α(n)/2` gives `A < α(n)` strictly; `s → 0^+` gives `inf A = 0`. ∎

> **Why `A ≥ 0` always, so the infimum `0` is the value.** For sorted-descending pieces, `A = Σ (p_{2i−1} − p_{2i}) + (p_{2m+1} \text{ if odd count})` is a sum of non-negative pair-excesses plus a non-negative leftover, so `A ≥ 0` for every refinement. Hence `Φ(balanced) = 0` exactly (as an infimum, attained in the limit). Since `α(n) > 0`, the balanced config is regime-N.

**Verification (exact rational, python).** `A = 2s` confirmed for `n = 1, 2, 3, 4, 5, 6, 7` with `w = 1/(n+1)` and `s = 1/1000` (resp. `1/10^6`); each matches `2s` to exact rational equality. (See `/tmp/verify_r4.py`.)

#### 5c.4 Two further structural classes at n = 3 (rigorous)

**(S2) Two-dyadic config `(1/2, 1/4, 1/8, 1/8)`.** This is the unique n=3 config whose three smallest pieces sit at consecutive dyadic ratios `1/4 : 1/8 = 2 : 1`. Xiang uses **2** marks (within the `≤ 3` budget): mark 1 cuts the piece `1/2 → (1/4, 1/4)` (matching the existing `1/4`); mark 2 cuts one of the resulting `1/4` pieces `→ (1/8, 1/8)` (matching the existing two `1/8`'s). Final multiset: `{1/4, 1/4, 1/8, 1/8, 1/8, 1/8}` — six pieces, all in equal pairs. Sorted descending: `1/4, 1/4, 1/8, 1/8, 1/8, 1/8` (two `1/4`'s at ranks 1, 2; four `1/8`'s at ranks 3–6). Alternating sum: `(1/4 − 1/4) + (1/8 − 1/8) + (1/8 − 1/8) = 0`. So `A = 0` exactly, `Liu = 1/2`, and `0 < α(3) = 1/15`. Regime-N holds (strictly). ∎ (Verified exactly: `A = 0`, python.)

> Note: this config is non-dyadic (the order-3 dyadic is `(1, 2, 4, 8)/15 ≈ (0.067, 0.133, 0.267, 0.533)`, not `(0.125, 0.125, 0.25, 0.5)`); yet the strategy achieves `A = 0`. The structure exploited is that the piece sizes form a dyadic *chain* `1/2, 1/4, 1/8, 1/8`, so Xiang's pile-match cuts telescope to all-equal pairs.

**(S3) Extreme-dominant config `(L, t, t, t)` with `t = (1 − L)/3` and `L > 4/5`.** Xiang uses 3 marks to cut the large piece `L` into 4 equal sub-pieces `L/4, L/4, L/4, L/4` (marks at `L/4, L/2, 3L/4` inside `L`). Final multiset: four copies of `L/4` and three copies of `t` (total 7 pieces). For `L > 4/7` we have `L/4 > t` (since `L/4 > (1−L)/3 ⟺ 3L > 4(1−L) ⟺ 7L > 4 ⟺ L > 4/7`), so sorted descending: four `L/4`'s then three `t`'s. Alternating sum: `(L/4 − L/4) + (L/4 − L/4) + (t − t) + t = 0 + 0 + 0 + t = t` (ranks 1–4: the four `L/4`'s cancel in two adjacent pairs; ranks 5–7: `+t − t + t = t`). Hence `A = t = (1 − L)/3`. For `L > 4/5`: `(1 − L)/3 < (1 − 4/5)/3 = (1/5)/3 = 1/15 = α(3)`. So `A = (1 − L)/3 < α(3)` strictly. Regime-N holds for `L > 4/5`. ∎ (Verified exactly for `L = 9/10` (`A = 1/30`), `L = 5/6` (`A = 1/18`); both `< 1/15`.)

> **Scope of (S3).** The "cut `L` into 4 equal" strategy gives `A = t = (1−L)/3`, which beats `α(3) = 1/15` only for `L > 4/5`. The moderately-dominant range `L ∈ (4/7, 4/5]` (where `L/4 > t` still holds but `t ≥ α(3)`) is NOT covered by this strategy; a different strategy is needed there and is not supplied here. The cut-`L`-into-`(t, t, t, L − 3t)` strategy (3 marks matching the tail size) gives `A = 2L − 1`, which beats `α(3)` only for `L < 8/15` — the moderate, not dominant, range. The middle range `L ∈ [8/15, 4/5]` is the honest uncovered sub-class of the dominant family.

#### 5c.5 Honest synthesis of round 4

The new regime-N engine (structural classification + sliver forcing) delivers:
- **(rigorous, grid-only, all n)** the necessary grid equality-case classification (5c.1): at the dyadic, grid equality `A = α(n)` forces the odd-mult leftover to be `{1}` (odd count) or `{a, a+1}` consecutive (even count), with the `a = 2^j` refinement empirical;
- **(rigorous, real-valued, promotable)** Lemma S1 — balanced config of any order `n ≥ 1` is regime-N: `Φ(balanced) = 0 < α(n)` via an explicit sliver strategy with `A = 2s → 0`;
- **(rigorous, real-valued, n = 3)** two further structural classes: the two-dyadic config `(1/2, 1/4, 1/8, 1/8)` (S2, `A = 0` exactly) and the extreme-dominant `(L, t, t, t)` with `L > 4/5` (S3, `A = (1−L)/3 < α(3)`).

**The wall (unchanged, honest).** The real-valued universal regime-N cover for `n ≥ 3` is NOT proved. The grid classification does not lift to reals (5c.2). The sliver-forcing lemmas cover three specific structural classes (balanced, two-dyadic, extreme-dominant `L > 4/5`), leaving uncovered: moderately-dominant `L ∈ [8/15, 4/5]`, near-dyadic balanced perturbations, and arbitrary non-dyadic configs. The classification-lift + universal sliver-forcing remain the honest open gap (G2). I do not paper over this. The regime-N conjecture (`Φ(Liu) < α(n)` for every non-dyadic `n ≥ 3` Liu config) is numerically robust (corpus-compute A3: 1200 random non-dyadic n=3 configs, max `Φ = 0.0595 < α(3) = 0.0667`, zero near-misses) but unproved in general.

**Do-not-retry list (round 4, cumulative).** R-pile greedy (falsified, 3 counterexample classes, §5b). `M − total(R) = α(n+1)` unified potential (dyadic-only tautology, foreclosed A4). (U-E) as a G2 closure (restates G2, does not bypass — unique-extremum explorer). The real-valued classification lift via the grid census alone (no proof technique visible). Claiming classification alone gives the SIDE `A < α` (it gives `A ≠ α` off the dyadic; the SIDE needs sliver forcing, not supplied universally).

---

### 5d. Round 5 — U(3) closure: 5-cap contradiction (d ≥ 1/2) + 3-mark sliver (d < 1/2 gap)

The round-5 dispatch targets `c(3) = 8/15` end-to-end. The lower bound `L(3)` is CERTIFIED (cell-complex vertex enumeration, `lemmas/lemma-vertex-principle-advantage.md`: every real Xiang response to the level-3 dyadic `(1,2,4,8)/15` gives `A ≥ 1/15 = α(3)`, i.e. `Liu ≥ 8/15`). The OPEN half is the upper bound `U(3)`: for EVERY Liu config with 4 pieces (≤ 3 marks), Xiang forces `Liu ≤ 8/15`, i.e. `A ≤ α(3)`, with equality iff the dyadic.

**Convention (resolved).** The round-5 dispatch's parenthetical "sorted descending" was a labeling slip; the explorer's cap formulas tie at `1/15` ONLY under the convention `a ≤ b ≤ c ≤ d` (a smallest, d largest), consistent with the certified `U(2)` template (`a ≤ b ≤ c`). We use `a ≤ b ≤ c ≤ d`, `a+b+c+d = 1`, `d` the LARGEST piece, throughout. The threshold `d ≥ 1/2` is the **dominant** regime (largest piece `≥` half the stick, i.e. `d ≥ a+b+c`); `2d − 1 = d − (a+b+c) ≥ 0` is the validity condition for the "match `a,b,c` in `d`" strategy. This resolves the dispatch's confusion.

We import (do not re-prove): **Lemma G** (`Liu = (1+A)/2`), **pair-pile / mirror** (regime-D equality, all n), **`L(3)`** (cell-complex, the lower bound), **`U(2)` four-strategy** (the n=2 template), **vertex-principle** (the `L(3)` technique). The advantage coordinate `A = Σ (−1)^{i+1} p_i` (sorted-descending final pieces) is used throughout; `α(3) = 1/15`, `f(3) = 8/15`.

#### 5d.1 The 5-cap subfamily and its cap formulas (rigorous)

For a 4-piece Liu config `(a, b, c, d)`, `a ≤ b ≤ c ≤ d`, `a+b+c+d = 1`, Xiang has 3 marks. We exhibit five strategies, each creating 3 cancelling equal-pairs plus (for the 3-mark strategies) one leftover, or (for the 2-mark strategy) two leftovers. Each cap is the resulting advantage `A`, computed exactly.

> **Equal-pair cancellation lemma (used throughout).** In a sorted-descending multiset of `M` final pieces, any two equal pieces occupy consecutive ranks. A block of even multiplicity at a single value contributes `0` to `A` (the equal values cancel in adjacent-rank pairs `(r, r+1)`, each pair `±v ∓ v = 0`). For `M = 2m+1` (odd) with `m` equal-pairs and one singleton, the singleton is at the unique odd rank not covered by a pair-block (pairs cover `m` odd + `m` even ranks; `m+1` odd ranks minus `m` = 1 leftover odd rank), contributing `+singleton`. For `M = 2m` (even) with `m−1` equal-pairs and two singletons, the two singletons sit at one odd and one even rank; the odd-rank singleton is at the smaller rank index (a pair-block starting at an even index would leave an uncovered odd position below it, contradicting coverage from the left), hence the larger singleton (smaller rank = larger value) is at the odd rank and `A = (larger singleton) − (smaller singleton) = |difference| ≥ 0`. (Proved by enumeration of pair-block placements; the odd-leftover-rank < even-leftover-rank fact follows because a pair-block at an even starting index leaves the preceding odd position uncovered, which is impossible since all positions below must be covered by pair-blocks, and an even count of positions cannot be tiled by length-2 blocks.)

The five strategies:

**Strategy `S_a` (bisect `b, c, d`; 3 marks).** Xiang bisects each of `b, c, d` into two equal halves. Final multiset `{a, b/2, b/2, c/2, c/2, d/2, d/2}` (7 pieces, odd). Three equal-pairs `(b/2,b/2), (c/2,c/2), (d/2,d/2)` cancel; singleton `a` at the leftover odd rank. `A = a`.

**Strategy `S_{b−a}` (match `a` in `b`, bisect `c, d`; 3 marks).** Mark 1 splits `b → (a, b−a)` (pair `(a, a)` with the original `a`, admissible since `b ≥ a`). Marks 2, 3 bisect `c, d`. Final multiset `{a, a, b−a, c/2, c/2, d/2, d/2}` (7 pieces). Pairs `(a,a), (c/2,c/2), (d/2,d/2)` cancel; singleton `b−a`. `A = b − a`.

**Strategy `S_{c−b}` (match `b` in `c`, bisect `a, d`; 3 marks).** Mark 1 splits `c → (b, c−b)` (pair `(b, b)` with the original `b`). Marks 2, 3 bisect `a, d`. Final multiset `{b, b, c−b, a/2, a/2, d/2, d/2}`. Three pairs cancel; singleton `c−b`. `A = c − b`.

**Strategy `S_{2d−1}` (match `a, b, c` in `d`; 3 marks).** Marks split `d → (a, b, c, d−a−b−c)` (three marks at distances `a`, `a+b`, `a+b+c` from one end of `d`). **Admissible iff `d ≥ a+b+c`, i.e. `d ≥ 1/2`.** Pairs `(a,a), (b,b), (c,c)` cancel; singleton `d−a−b−c = 2d−1`. `A = 2d − 1` (non-negative in the admissible regime).

**Strategy `S_{|a+b−c|}` (bisect `d`, match `a` in `c`; 2 marks).** Mark 1 bisects `d → (d/2, d/2)` (pair). Mark 2 splits `c → (a, c−a)` (pair `(a, a)` with the original `a`). Final multiset `{a, a, c−a, b, d/2, d/2}` (6 pieces, even). Two pairs cancel; two singletons `b` and `c−a`. By the equal-pair lemma (even case), `A = |b − (c−a)| = |a + b − c|`.

Each formula is verified by direct multiset alt-sum (exact rational arithmetic, `/tmp/verify_u3.py`).

#### 5d.2 The `d ≥ 1/2` regime — FULLY RIGOROUS 5-cap contradiction

**Theorem (U(3), dominant regime).** For every 4-piece Liu config with `a ≤ b ≤ c ≤ d`, `a+b+c+d = 1`, `d ≥ 1/2`:
```
min(a, b−a, c−b, 2d−1, |a+b−c|) ≤ 1/15 = α(3),
```
with equality (the min `= α(3)`) iff `(a, b, c, d) = (1, 2, 4, 8)/15` (the order-3 dyadic).

**Proof.** Translate each cap to a condition on `(a, b, c, d)`:
- `a ≤ 1/15` ⟺ `S_a` caps.
- `b − a ≤ 1/15` ⟺ `S_{b−a}` caps.
- `c − b ≤ 1/15` ⟺ `S_{c−b}` caps.
- `2d − 1 ≤ 1/15` ⟺ `d ≤ 8/15` (and `2d−1 ≥ 0` by `d ≥ 1/2`).
- `|a+b−c| ≤ 1/15` ⟺ `−1/15 ≤ a+b−c ≤ 1/15`, i.e. `c ≤ a+b + 1/15` AND `c ≥ a+b − 1/15`.

Suppose for contradiction that **all five caps `> 1/15`**. Then:
1. `a > 1/15`,
2. `b − a > 1/15` ⟹ `b > a + 1/15`,
3. `c − b > 1/15` ⟹ `c > b + 1/15`,
4. `2d − 1 > 1/15` ⟹ `d > 8/15`,
5. `|a+b−c| > 1/15` ⟹ **(Case i)** `c < a+b − 1/15` OR **(Case ii)** `c > a+b + 1/15`.

From (1)–(3): `a > 1/15`, `b > 2/15`, `c > 3/15`, so `a+b+c > 1/15 + 2/15 + 3/15 = 6/15 = 2/5`. Then `d = 1 − (a+b+c) < 1 − 2/5 = 3/5 = 9/15`. Combined with (4): `8/15 < d < 9/15`. (Not yet a contradiction; the 5th cap closes it.)

**Case (i):** `c < a + b − 1/15`. Together with (3) `c > b + 1/15`: `b + 1/15 < a + b − 1/15`, so `a > 2/15`. Then `b > a + 1/15 > 3/15`, `c > b + 1/15 > 4/15`, giving `a+b+c > 2/15 + 3/15 + 4/15 = 9/15 = 3/5`, hence `d = 1 − (a+b+c) < 1 − 3/5 = 2/5 = 6/15`. But (4) gives `d > 8/15 > 6/15`. **Contradiction.**

**Case (ii):** `c > a + b + 1/15`. From (1),(2): `a > 1/15`, `b > a + 1/15 > 2/15`, so `a+b > 3/15`. Then `a+b+c = (a+b) + c > (a+b) + (a+b + 1/15) = 2(a+b) + 1/15 > 2·(3/15) + 1/15 = 7/15`. Hence `d = 1 − (a+b+c) < 1 − 7/15 = 8/15`. But (4) gives `d > 8/15`. **Contradiction.**

Both cases contradict, so at least one cap `≤ 1/15`. ∎ (contradiction)

**Equality analysis.** Replace `>` with `≥` throughout. From (1)–(3) with `≥`: `a ≥ 1/15`, `b ≥ 2/15`, `c ≥ 3/15`. Case (i) `c ≤ a+b − 1/15` with `c ≥ b + 1/15` forces `a ≥ 2/15`, then `a+b+c ≥ 9/15` forces `d ≤ 6/15`, contradicting `d ≥ 8/15`. So Case (i) is impossible under `≥`. In Case (ii) `c ≥ a+b + 1/15`: `a+b+c ≥ 2(a+b) + 1/15 ≥ 7/15`, so `d ≤ 8/15`; combined with `d ≥ 8/15` gives `d = 8/15` and forces every intermediate inequality to equality: `a+b = 3/15` (so `a = 1/15, b = 2/15`), `c = a+b + 1/15 = 4/15`. Hence `(a, b, c, d) = (1, 2, 4, 8)/15`, the order-3 dyadic. ∎ (equality)

**Verification.** Exact rational arithmetic on grids `N = 60, 90, 120, 150` over `a ≤ b ≤ c ≤ d`, `d ≥ 1/2`: **0 violations** (the min of the five caps `≤ 1/15` everywhere), and the unique config with `min = 1/15` is exactly `(1/15, 2/15, 4/15, 8/15)` (`/tmp/verify_u3.py`). At the dyadic, four of the five strategies tie at `1/15` (`a`, `b−a`, `2d−1`, `|a+b−c|`); `c−b = 2/15` is loose (the min is still `1/15`).

**Corollary (moderate-dominant class covered).** The reviewer's round-4 flag (the class `L = d ∈ [8/15, 4/5]`, "cap-`a` fails for ~16% where `a > 1/15`") is GENUINELY covered: this class lies in `d ≥ 1/2` (since `8/15 > 1/2`), so the 5-cap contradiction above handles it via the MULTI-WAY argument, not via the single `a`-cap. Concretely, when `a > 1/15` (cap-`a` fails), the contradiction routes through caps `b−a`, `c−b`, `2d−1`, `|a+b−c|` (Case i or ii), yielding `min ≤ 1/15` regardless. No sliver forcing is needed in `d ≥ 1/2`. ∎

#### 5d.3 The `d < 1/2` regime — the 3-mark sliver strategy (rigorous)

When `d < 1/2`, the `S_{2d−1}` strategy is invalid (`2d−1 < 0`), so the 5-cap family loses one cap. The remaining 17-family exact-pair caps (listed in `/tmp/explore_dlt.py`) cover most `d < 1/2` configs, but a **thin gap region** exists where ALL exact-pair caps exceed `α(3)`. We characterize it and close it with a NEW 3-mark sliver strategy.

**Parametrization.** Define the four "chain excesses"
```
u := a − α,    v := (b−a) − α,    w := (c−a−b) − α,    z := (d−b−c) − α
```
(so `a = α+u`, `b = 2α+u+v`, `c = 4α+2u+v+w`, `d = 7α+3u+2v+w+z`). The identity `7u + 4v + 2w + z = α` holds always (it is `a+b+c+d = 1` rewritten). Note `1 − 2d = u − z` (algebra: `1 − 2(7α+3u+2v+w+z) = 15α − 14α − 6u − 4v − 2w − 2z = α − (6u+4v+2w+2z) = u − z` using `7u+4v+2w+z = α`). Hence `d < 1/2 ⟺ u > z`.

The exact-pair caps that can be small (near `α`) are precisely `a = α+u`, `b−a = α+v`, `|a+b−c| = |α+w|`, `d−b−c = α+z = |b+c−d|` (when `z ≥ 0`). The **gap region** is
```
G := {u > 0, v > 0, w > 0, z > 0, u > z}   (all four chain caps > α, with d < 1/2),
```
i.e. `a > α`, `b−a > α`, `c > a+b+α` (so `c−a−b > α`), `d > b+c+α` (so `d−b−c > α`), `d < 1/2`. In `G`, the four small caps `α+u, α+v, α+w, α+z` all exceed `α`, `2d−1 = z−u < 0` is invalid, and every other 17-family cap is `≥ 2α` (verified: `c−b = 2α+u+w`, `d−c = 3α+u+v+z`, `d−a−b = 4α+u+v+w+z`, etc., all exceed `2α > α`). So the 17-family min in `G` is `α + min(u,v,w,z) > α`.

> **Lemma (3-mark sliver strategy — the gap closure).** *For every config in the gap `G` (so `d ≥ b+c+α > b+c`, i.e. `e_3 := d−b−c ≥ α > 0`, and `u > z`, i.e. `a > e_3`), Xiang has a 3-mark strategy forcing `A = 1 − 2d = u − z < α(3)` strictly. Hence `U(3)` holds strictly in `G`.*

**Strategy.** Place two marks inside `d`, splitting it into `(b, c, e_3)` where `e_3 := d − b − c` (marks at distances `b` and `b+c` from one end of `d`; admissible since `d ≥ b+c+α > b+c`, so `e_3 > 0`). This creates pairs `(b, b)` (the new `b` + the original `b`) and `(c, c)` (the new `c` + the original `c`). Place the third mark inside `a`, shaving a sliver `ε ∈ (0, a)` from it: `a → (ε, a−ε)`. The final multiset is `{b, b, c, c, a−ε, e_3, ε}` (7 pieces). The pairs `(b,b)` and `(c,c)` each cancel; the three singletons are `ε`, `a−ε`, `e_3`.

**Validity of the shave interval.** The strategy requires `0 < ε < a` and (for the sort below) `ε < a − e_3` and `ε < e_3`. Since `a − e_3 = (α+u) − (α+z) = u − z > 0` (gap) and `e_3 = α + z > 0` (gap), the interval `(0, min(u−z, e_3, a))` is nonempty; pick any `ε` in it (e.g. `ε = (u−z)/2` if `u−z ≤ e_3`, else `ε = e_3/2`).

**Sort.** In the gap: `c ≥ b` (sorted) `> a−ε` (since `b ≥ a > a−ε`) `> e_3` (since `a−ε > e_3 ⟺ ε < a−e_3 = u−z`, guaranteed) `> ε` (since `e_3 > ε`, guaranteed). Also `e_3 < b`: `e_3 = α+z ≤ α < α+u+v = b` (using `z ≤ α` from `7u+4v+2w+z = α` with `u,v,w ≥ 0`, and `b = 2α+u+v > α`). And `e_3 < c` (clearer). So sorted descending: `c, c, b, b, a−ε, e_3, ε`.

**Computation.**
```
A = c − c + b − b + (a−ε) − e_3 + ε = (a − ε) − e_3 + ε = a − e_3 = (α+u) − (α+z) = u − z = 1 − 2d.
```
The `ε`-terms cancel, so the cap is **independent of `ε`** (robust). And `u − z = 1 − 2d < α(3)`: indeed `u − z < α ⟺ 0 < α − (u−z) = 6u + 4v + 2w + 2z` (using `7u+4v+2w+z = α ⟹ α − (u−z) = 6u+4v+2w+2z`), which holds strictly since `u, v, w, z > 0` in `G`. ∎

**Verification.** Exact rational arithmetic on 22 gap configs (constructed + random): in every case `A = a − e_3 = u − z = 1 − 2d < α(3)`, independent of `ε` (tested 4 values of `ε` per config) (`/tmp/verify_sliver3.py`). E.g. at the boundary config `(1, 2, 4, 7)/14` (`d = 1/2`, `2d−1 = 0`): `A = 0`. At the dyadic `(1,2,4,8)/15`: the sliver (valid since `d ≥ 1/2`) gives `A = |2d−1| = 1/15 = α` (equality — consistent, the dyadic is in `d ≥ 1/2` handled by the 5-cap).

**Remark (the sliver generalizes `S_{2d−1}`).** The strategy "match `b, c` in `d` + shave `a`" produces `A = |2d−1|` (universal: in `d ≥ 1/2` the shave is unnecessary and the cap is `2d−1`; in `d < 1/2` the shave makes the would-be-negative `2d−1` leftover positive, with cap `1−2d`). It is realizable whenever `d ≥ b+c` (for `d < 1/2`) or `d ≥ 1/2` (automatic). In `d ≥ 1/2` it coincides with the `S_{2d−1}` cap (redundant with the 5-cap family). In `d < 1/2` it fires exactly in `G` (`d > b+c+α`) and closes the gap.

#### 5d.4 The `d < 1/2` non-gap sub-cases — coverage and the honest GAP

Outside the gap `G`, in `d < 1/2` (so `u > z`), at least one chain excess is `≤ 0`:
- `u ≤ 0 ⟹ a = α+u ≤ α`: cap `a` (`S_a`) `≤ α`. ✓ (rigorous)
- `v ≤ 0 ⟹ b−a = α+v ≤ α`: cap `b−a` (`S_{b−a}`) `≤ α`. ✓ (rigorous)
- `w ≤ 0`: `|a+b−c| = |α+w|`. If `w ∈ [−2α, 0]`, `|α+w| ≤ α` ✓ (rigorous). If `w < −2α`, `|a+b−c| = −α−w > α`, and the `|a+b−c|` cap does not close it.
- `z ≤ 0`: `|b+c−d| = |α+z|`. If `z ∈ [−2α, 0]`, `|α+z| ≤ α` ✓ (rigorous). If `z < −2α`, `|b+c−d| = −α−z > α`, and the `|b+c−d|` cap does not close it.

The sub-cases `w < −2α` (config: `c < a+b − 2α`, the smaller piece `c` "much less" than `a+b`) and `z < −2α` (config: `d < b+c − 2α`, the smaller piece `d` "much less" than `b+c`) are NOT closed by the two-mark abs-caps above; they require the further 17-family caps (`c−b`, `d−c`, `|a+c−d|`, `a+c−b`, `a+d−c`, `d−a−b`, `d−a−c`, etc.), and the case-by-case contradiction across these is **laborious and not yet written in full**.

**Computational verification (strong evidence, not proof).** The full 17-family PLUS the sliver cap `|2d−1|` (when realizable) gives **0 violations** over:
- the `d < 1/2` grid `N = 60, 90, 120` (865, 2788, 6455 configs; `max_min = 0`, no equality configs — the dyadic is not in `d < 1/2`),
- 50,000 random real configs over the full simplex `a ≤ b ≤ c ≤ d` (0 violations, equality count 0 in `d < 1/2`),
and over the full simplex the unique equality config is the dyadic `(1,2,4,8)/15` (in `d ≥ 1/2`, handled rigorously by §5d.2). A minimal-subfamily search (`/tmp/test_5cap_dlt.py`) confirmed NO small subfamily (4–7 caps) closes `d < 1/2` — the 17-family's many caps are all needed, which is why the analytic case-by-case contradiction is laborious.

**Honest GAP.** The `d < 1/2` non-gap sub-cases (`w < −2α` or `z < −2α`, outside the sliver-closed gap `G`) are computationally verified (0 violations) but NOT yet closed by a complete analytic contradiction. This is the remaining open piece of `U(3)`. I do not paper over it.

#### 5d.5 Synthesis of round 5

| regime | coverage | status |
|---|---|---|
| `d ≥ 1/2` (dominant; includes dyadic) | 5-cap contradiction §5d.2 | **RIGOROUS** (closed, equality iff dyadic) |
| `d < 1/2`, gap `G` (all 4 chain caps `> α`) | 3-mark sliver §5d.3 | **RIGOROUS** (closed, `A = 1−2d < α` strict) |
| `d < 1/2`, non-gap, `w,z ≥ −2α` | `|a+b−c|`, `|b+c−d|` (or `a`, `b−a`) | **RIGOROUS** (the four sub-cases above) |
| `d < 1/2`, non-gap, `w < −2α` or `z < −2α` | 17-family further caps | **GAP** (verified computationally, analytic closure open) |

**Milestones.** (i) The entire `d ≥ 1/2` regime (the dominant half of the Liu simplex, containing the dyadic equality case) is CLOSED RIGOROUSLY by a clean 4-way/2-case contradiction — the direct `n = 3` generalization of the certified `U(2)` four-strategy proof. (ii) The thin `d < 1/2` gap `G` (the unique sub-region defeating the 17-family) is CLOSED RIGOROUSLY by a NEW 3-mark sliver strategy with the explicit cap `A = 1 − 2d < α(3)`. (iii) The moderate-dominant class `L ∈ [8/15, 4/5]` (round-4 reviewer flag) is GENUINELY covered by the 5-cap multi-way argument (not the single `a`-cap).

**Combined with `L(3)` (certified, cell-complex):** `c(3) = 8/15` is rigorously end-to-end on the `d ≥ 1/2` regime and the `d < 1/2` gap; the `d < 1/2` non-gap extreme sub-cases (`w < −2α` or `z < −2α`) are computationally verified but await the full analytic 17-family case-by-case contradiction. The equality characterization `c(3) = 8/15` iff `(1,2,4,8)/15` rests rigorously on the `d ≥ 1/2` proof (where the dyadic lives and equality is fully characterized); in `d < 1/2` there is no equality (the dyadic is not there, and every `d < 1/2` config has `min < α` strictly, verified computationally and proven in the gap `G`).

**Do-not-retry list (round 5, cumulative).** R-pile greedy (§5b). Unified potential (foreclosed). (U-E) (restates G2). The 4–7-cap minimal subfamilies for `d < 1/2` (all have grid violations — the 17-family's full menu is necessary; no clean small contradiction exists for `d < 1/2`). The bare 5-cap family OUTSIDE `d ≥ 1/2` (it loses `2d−1` and fails; the sliver must replace it). [Round 6 OVERTURNS the "no 4–7-cap subfamily suffices" ruling FOR THE EXTREME SUB-CASES specifically: with realizability enforced, the 7-cap subfamily closes regimes IV — see §5e. The 17-family is still the engine for regime III's `z ∈ [−2α, 0]` sub-case (via `|b+c−d|`, realizable), but that sub-case is NOT in the extreme regime.]

---

### 5e. Round 6 — U(3) extreme-closure: the 7-cap contradiction (regime IV) → `c(3) = 8/15` SOLVED

This section closes the LAST open piece of `U(3)`: the `d < 1/2` non-gap extreme sub-cases `w < −2α` or `z < −2α` (regime IV in the §5d.5 table, previously a GAP). The closure is a **7-cap case-by-case contradiction** — the direct `n=3` generalization of the certified `U(2)` four-strategy lemma and the round-5 5-cap dominant-regime lemma. Combined with the CERTIFIED `L(3)` (cell-complex, imported `lemma-vertex-principle-advantage.md`) and the round-5 closures of regimes I–III, this yields **`c(3) = 8/15` rigorously end-to-end** (§5e.5).

**Notation (chain excesses, imported from `lemma-u3-sliver-gap.md`).** Set `α := α(3) = 1/15`. For a 4-piece Liu config `(a, b, c, d)`, `a ≤ b ≤ c ≤ d`, `a+b+c+d = 1`, define
```
u := a − α,    v := (b−a) − α,    w := (c−a−b) − α,    z := (d−b−c) − α,
```
so `a = α+u`, `b = 2α+u+v`, `c = 4α+2u+v+w`, `d = 7α+3u+2v+w+z`, and the sum constraint gives the identity
```
7u + 4v + 2w + z = α.                                    (ID)
```
Note `1 − 2d = u − z` (algebra: `1−2d = 15α − 2(7α+3u+2v+w+z) = α − 6u − 4v − 2w − 2z = u − z` using `z = α−7u−4v−2w` from (ID)). Hence `d < 1/2 ⟺ u > z`.

#### 5e.1 The 7-cap subfamily and its realizability (all ≤ 3 marks, all always-realizable)

For a 4-piece config `(a,b,c,d)`, `a ≤ b ≤ c ≤ d`, Xiang with `≤ 3` marks has the following seven strategies. Each produces a final multiset of `≤ 7` pieces; the resulting advantage `A` (sorted-descending alternating sum) is the named **cap**. We import the **equal-pair cancellation lemma** (certified `lemma-u3-5cap-dominant.md` §5d.1): in a sorted-descending multiset, a block of even multiplicity at a single value contributes `0` to `A`; for `2m+1` pieces with `m` equal-pairs + 1 singleton, the singleton sits at the unique leftover odd rank, contributing `+singleton`; for `2m` pieces with `m−1` equal-pairs + 2 singletons, the larger singleton sits at an odd rank (a pair-block starting at an even index would leave the preceding odd position untiled, impossible), giving `A = (larger singleton) − (smaller singleton) = |difference|`.

**The four chain-difference caps** (already in §5d.1, certified `lemma-u3-5cap-dominant.md`):
- **`S_a`** (bisect `b, c, d`; 3 marks): pairs `(b/2,b/2),(c/2,c/2),(d/2,d/2)`; singleton `a`. `A = a`. (`C1`)
- **`S_{b−a}`** (match `a` in `b` + bisect `c, d`; 3 marks): pairs `(a,a),(c/2,c/2),(d/2,d/2)`; singleton `b−a`. `A = b−a`. (`C2`)
- **`S_{c−b}`** (match `b` in `c` + bisect `a, d`; 3 marks): pairs `(b,b),(a/2,a/2),(d/2,d/2)`; singleton `c−b`. `A = c−b`. (`C3`)
- **`S_{d−c}`** (match `c` in `d` + bisect `a, b`; 3 marks): pairs `(c,c),(a/2,a/2),(b/2,b/2)`; singleton `d−c`. `A = d−c`. (`C4`)

Each is admissible (bisect any piece always possible; "match `x` in `y`" requires `y ≥ x`, guaranteed by `a ≤ b ≤ c ≤ d`). All four use exactly 3 marks.

**The three abs-sum caps** (2 marks each):
- **`S_{|a+b−c|}`** (bisect `d` + match `a` in `c`; 2 marks) — already in §5d.1, certified. Pairs `(d/2,d/2),(a,a)`; singletons `b`, `c−a`. `A = |b−(c−a)| = |a+b−c|`. (`C5`). Admissible: `d` bisectable, `c ≥ a`. Chain-excess form: `|a+b−c| = |α+w|`.
- **`S_{|a+c−d|}`** (bisect `b` + match `a` in `d`; 2 marks) — **NEW this round.** Mark 1 bisects `b → (b/2, b/2)` [pair `(b/2,b/2)`]. Mark 2 splits `d → (a, d−a)` [pair `(a,a)` with the original `a`]. Final multiset `{a, a, b/2, b/2, c, d−a}` (6 pieces). Two pairs `(a,a),(b/2,b/2)` cancel; two singletons `c`, `d−a`. By the equal-pair lemma (even case), `A = |c − (d−a)| = |a+c−d|`. (`C6`). Admissible: `b` bisectable, `d ≥ a` (sorted). Chain-excess form: `|a+c−d| = |2α+v+z| = |3α−7u−3v−2w|`.
- **`S_{|a+b−d|}`** (bisect `c` + match `a` in `d`; 2 marks) — **NEW this round.** Mark 1 bisects `c → (c/2, c/2)` [pair `(c/2,c/2)`]. Mark 2 splits `d → (a, d−a)` [pair `(a,a)`]. Final multiset `{a, a, b, c/2, c/2, d−a}` (6 pieces). Two pairs `(a,a),(c/2,c/2)` cancel; two singletons `b`, `d−a`. `A = |b − (d−a)| = |a+b−d|`. (`C7`). Admissible: `c` bisectable, `d ≥ a` (sorted). Chain-excess form: `|a+b−d| = |4α+u+v+w+z| = |5α−6u−3v−w|`.

> **Realizability summary.** All 7 caps are realized by an explicit ≤3-mark Xiang strategy. **None requires `d ≥ b+c`** (the condition that defeated the round-5 "17-family necessary" census): the only "match" moves are `match a in b/c/d` (needing `b,c,d ≥ a`, automatic) and `match b in c`, `match c in d` (needing `c ≥ b`, `d ≥ c`, automatic). The un-realizable caps that round-5's census counted as *values* — `d−b−c` (needs `d ≥ b+c`), `2d−1` (needs `d ≥ 1/2`) — are **excluded** from the 7-cap family. This is the correction that overturns the round-5 ruling for the extreme sub-cases.

The chain-excess forms of the 7 caps (using `z = α−7u−4v−2w` from (ID)) are:
```
C1 = α+u,    C2 = α+v,    C3 = 2α+u+w,    C4 = 4α−6u−3v−2w,
C5 = |α+w|,  C6 = |3α−7u−3v−2w|,  C7 = |5α−6u−3v−w|.       (∗)
```

#### 5e.2 The 8-sub-case partition (exhaustive, disjoint)

Fix `α = 1/15`. The **extreme regime** is
```
E := {d < 1/2  ∧  (w < −2α  ∨  z < −2α)}.
```
(`d < 1/2` is `u > z`; `w < −2α` ⟺ `c < a+b−α` ⟺ `a+b−c > α`; `z < −2α` ⟺ `d < b+c−α` ⟺ `b+c−d > α`.) This is regime IV of the §5d.5 table.

Assume for contradiction that **all 7 caps exceed `α`**. Each abs-cap `Ck` (k=5,6,7) then occupies one of two sign branches; let `s_k ∈ {+1,−1}` denote the sign of the interior expression (so `C5 = s_5(α+w)`, `C6 = s_6(3α−7u−3v−2w)`, `C7 = s_7(5α−6u−3v−w)`, with the interior non-negative for `+` and non-positive for `−`). The condition `Ck > α` forces:
- `s_5 = +1` ⟺ `w > 0` (since `α+w > α`); `s_5 = −1` ⟺ `w < −2α` (since `−(α+w) > α`).
- `s_6 = +1` ⟺ `7u+3v+2w < 2α` (i.e. `3α−(7u+3v+2w) > α`); `s_6 = −1` ⟺ `7u+3v+2w > 4α`.
- `s_7 = +1` ⟺ `6u+3v+w < 4α`; `s_7 = −1` ⟺ `6u+3v+w > 6α`.

The 2³ = 8 sign triples `(s_5, s_6, s_7)` partition `E` exhaustively and disjointly (every config has a unique sign triple, since the interiors are real numbers with definite sign; ties `= 0` give `Ck = α·(interior sign magnitude)`, but `Ck = α` is NOT `> α`, so the all-`>α` assumption excludes ties — each `Ck` is strictly on one branch). We denote `L_6 := 7u+3v+2w`, `L_7 := 6u+3v+w` (so `C6 = |3α−L_6|`, `C7 = |5α−L_7|`, and the key identity `L_6 − L_7 = u+w`).

> **Branch collapse.** `s_5 = −1` is the condition `w < −2α`, i.e. it is the `w < −2α` sub-regime of `E` itself. Hence the 4 sign triples with `s_5 = −1` cover configs with `w < −2α` (the `w`-extreme sub-regime), **regardless of whether `z < −2α` also holds** — the `s_5 = −1` arguments below use only `w < −2α` (and the chain caps), not the value of `z`, so they apply uniformly to both `w`-extreme-only configs and configs where `w < −2α ∧ z < −2α` both hold. The 4 sign triples with `s_5 = +1` require `w > 0`, which is incompatible with `w < −2α`; these can occur only in the `z < −2α` sub-regime (with `w > 0`). Thus: the `s_5 = −1` triples close the entire `w < −2α` sub-regime plus the `s_5 = −1` slice of the `z < −2α` sub-regime; the `s_5 = +1` triples close the remaining `w > 0` slice of the `z < −2α` sub-regime. Together the 8 triples cover all of `E`.

Throughout the 8 sub-cases we use the **chain-cap assumptions** (from `C1,C2,C3,C4 > α`):
```
(I) u > 0,    (II) v > 0,    (III) u+w > −α,    (IV) 6u+3v+2w < 3α,    (∗) d<1/2: u > z.
```
(Sort constraints `a ≤ b ≤ c ≤ d`, `a > 0` are implied: `v ≥ −α` by (II); `u+w ≥ −2α` by (III); `6u+3v+2w ≤ 4α` by (IV); `u ≥ −α` by (I).) In sub-regime `z < −2α` we additionally have `7u+4v+2w > 3α` (call this `(S2)`); in sub-regime `w < −2α` we have `(S1): w < −2α` itself.

#### 5e.3 The 8 sub-case contradictions

We treat the 8 sign triples in two groups: `s_5 = −1` (covers `w < −2α` entirely + the `w < −2α ∧ z < −2α` configs), and `s_5 = +1` (covers the `w > 0 ∧ z < −2α` configs).

##### Group A: `s_5 = −1` (so `w < −2α`), sub-cases by `(s_6, s_7)`

**A1. `(s_5,s_6,s_7) = (−,+,+)`:** `L_6 < 2α` and `L_7 < 4α`.
- (i) `w < −2α` and (III) `u+w > −α` ⟹ `u > −α−w > −α+2α = α`. So `u > α`.
- (ii) `L_6 < 2α` (i.e. `7u+3v+2w < 2α`) and (II) `v > 0` ⟹ `7u+2w < 2α` (drop `3v > 0`).
- (iii) (III) `u+w > −α` ⟹ `7u+2w = 5u + 2(u+w) > 5u + 2(−α) = 5u − 2α`.
- (iv) Combine (ii),(iii): `5u − 2α < 7u+2w < 2α` ⟹ `5u < 4α` ⟹ `u < 4α/5 < α`. This **contradicts** (i) `u > α`. ∎

**A2. `(−,+,−)`:** `L_6 < 2α` and `L_7 > 6α`.
- `L_6 < 2α` and `L_7 > 6α` ⟹ `u+w = L_6 − L_7 < 2α − 6α = −4α`.
- But (III) gives `u+w > −α`. Since `−4α < −α`, **contradiction**. ∎ (2-line; this argument does not use `s_5`, so it also covers the `s_5 = +` occurrence of `(s_6,s_7) = (+,−)`, i.e. sub-case B2 below.)

**A3. `(−,−,+)`:** `L_6 > 4α` and `L_7 < 4α`.
- (i) `L_6 > 4α` and `L_7 < 4α` ⟹ `u+w = L_6 − L_7 > 4α − 4α = 0`. So `u+w > 0`.
- (ii) `w < −2α` (from `s_5 = −1`) and (i) `u+w > 0` ⟹ `u > −w > 2α`. So `u > 2α`.
- (iii) Identity: `2 L_7 = L_6 + 5u + 3v` (check: `2(6u+3v+w) − (7u+3v+2w) = 5u+3v`). With `L_6 > 4α`, `5u > 10α` (from (ii)), `3v > 0` (from (II)): `2 L_7 = L_6 + 5u + 3v > 4α + 10α + 0 = 14α`.
- (iv) But `L_7 < 4α` ⟹ `2 L_7 < 8α`. So `14α < 2 L_7 < 8α`, i.e. `14α < 8α`. **Contradiction.** ∎

**A4. `(−,−,−)`:** `L_6 > 4α` and `L_7 > 6α`.
- (i) (IV) `6u+3v+2w < 3α` and `L_7 = 6u+3v+w > 6α` ⟹ `w = (6u+3v+2w) − L_7 < 3α − 6α = −3α`. So `w < −3α` (stronger than `s_5 = −1`'s `w < −2α`).
- (ii) (III) `u+w > −α` ⟹ `6u+2w = 5u + 2(u+w) + u > ... ` — more directly: `6(u+w) > −6α`, so `6u+2w = 6(u+w) − 4w > −6α − 4w`. With `w < −3α`: `−4w > 12α`, so `6u+2w > −6α + 12α = 6α`.
- (iii) (IV) `6u+3v+2w < 3α` and (ii) `6u+2w > 6α` ⟹ `3v < 3α − (6u+2w) < 3α − 6α = −3α < 0`. So `v < −α < 0`.
- (iv) But (II) gives `v > 0`. **Contradiction.** ∎

##### Group B: `s_5 = +1` (so `w > 0`), occurring only in the `z < −2α` sub-regime (use `(S2): 7u+4v+2w > 3α`)

**B1. `(+,+,+)`:** `w > 0`, `L_6 < 2α`, `L_7 < 4α`, and `(S2)`. **(The tightest sub-case — global extremum.)**
- (i) `(S2): 7u+4v+2w > 3α` and `L_6 = 7u+3v+2w < 2α` ⟹ `v = (7u+4v+2w) − L_6 > 3α − 2α = α`. So `v > α`.
- (ii) `w > 0` (from `s_5 = +1`) and `L_6 = 7u+3v+2w < 2α` ⟹ `7u+3v < 2α − 2w < 2α` (since `w > 0` ⟹ `−2w < 0`). So `7u+3v < 2α`.
- (iii) `v > α` (from (i)) ⟹ `3v > 3α` ⟹ `7u < 2α − 3v < 2α − 3α = −α`. So `u < −α/7 < 0`.
- (iv) But (I) gives `u > 0`. **Contradiction.** ∎

  *(This is the global extremum of the 7-cap min over `E`: the LP optimum `min = 12α/13 = 4/65 < α`, attained in the limit at the arrangement vertex `u = w = −α/13`, `v = 12α/13`, `z = −2α`, where `C1 = C5 = C6 = 12α/13` tie. The contradiction above shows no config in `E` with this sign triple can have all 7 caps `> α`.)*

**B2. `(+,+,−)`:** `w > 0`, `L_6 < 2α`, `L_7 > 6α`.
- `L_6 < 2α` and `L_7 > 6α` ⟹ `u+w = L_6 − L_7 < −4α`. But (III) `u+w > −α`. **Contradiction.** ∎ (Identical to A2 — the argument is `s_5`-independent.)

**B3. `(+,−,+)`:** `w > 0` (and the sign constraint `s_5 = +1` requires `α+w ≥ 0`, i.e. `w ≥ −α` — weaker than `w > 0`, but we carry the weaker `w ≥ −α`), `L_6 > 4α`, `L_7 < 4α`.
- (i) (IV) `6u+3v+2w < 3α` and `L_6 = 7u+3v+2w > 4α` ⟹ `u = L_6 − (6u+3v+2w) > 4α − 3α = α`. So `u > α`.
- (ii) `L_7 = 6u+3v+w < 4α` and `u > α` (so `6u > 6α`), `v > 0` (II): `L_7 = 6u+3v+w > 6α + 0 + w = 6α + w`. Hence `4α > L_7 > 6α + w` ⟹ `w < −2α`.
- (iii) But `s_5 = +1` requires `w ≥ −α` (sign of `α+w` non-negative). `w < −2α < −α`. **Contradiction.** ∎

**B4. `(+,−,−)`:** `w ≥ −α` (sign `s_5 = +1`), `L_6 > 4α`, `L_7 > 6α`.
- (i) (IV) `6u+3v+2w < 3α` and `L_7 = 6u+3v+w > 6α` ⟹ `w = (6u+3v+2w) − L_7 < 3α − 6α = −3α`. So `w < −3α`.
- (ii) `s_5 = +1` requires `w ≥ −α`. But `w < −3α < −α`. **Contradiction.** ∎ (2-line.)

> **All 8 sub-cases yield a contradiction.** The 8 sign triples partition `E` exhaustively (every config with all 7 caps `> α` falls into exactly one), so the assumption "all 7 caps `> α`" is infeasible throughout `E`. Hence in the extreme regime `E`, at least one of the 7 caps is `≤ α(3) = 1/15`. Since all 7 are realizable (§5e.1), Xiang forces `A ≤ α(3)`, i.e. `Liu ≤ 8/15 = f(3)`, throughout `E`. Moreover the LP-per-subcase check (`/tmp/round-6/u3_7cap_verify.py`) gives `max t < 0` strictly in all 8 sub-cases (global max `min = 12α/13 < α`), so in fact the inequality is STRICT in `E`: no config in `E` attains `min = α`. (The dyadic `(1,2,4,8)/15` has `d = 8/15 > 1/2`, so it is NOT in `E` — consistent.)

#### 5e.4 Realizability of `|b+c−d|` for the regime-III `z ∈ [−2α, 0]` sub-case (round-5 gap closed)

Round-5 §5d.4 closed the non-extreme `z ∈ [−2α, 0]` sub-case (regime III, with `w ≥ −2α`) via the cap `|b+c−d| = |α+z| ≤ α`, but did not give an explicit strategy. We supply it here for completeness. **Strategy `S_{|b+c−d|}`** (bisect `a` + match `c` in `d`; 2 marks): mark 1 bisects `a → (a/2, a/2)` [pair `(a/2,a/2)`]; mark 2 splits `d → (c, d−c)` [pair `(c,c)` with the original `c`]. Final multiset `{a/2, a/2, b, c, c, d−c}` (6 pieces). Two pairs `(a/2,a/2),(c,c)` cancel; two singletons `b`, `d−c`. By the equal-pair lemma, `A = |b − (d−c)| = |b+c−d|`. Admissible: `a` bisectable, `d ≥ c` (sorted). Always realizable. In regime III's `z ∈ [−2α, 0]` sub-case, `|α+z| ≤ α`, so this cap closes it. (The `w ∈ [−2α, 0]` sub-case is closed by `C5 = |a+b−c| = |α+w| ≤ α`, already certified §5d.1.)

#### 5e.5 Synthesis: `c(3) = 8/15` SOLVED end-to-end

**The four regimes of the `n = 3` Liu simplex** (`a ≤ b ≤ c ≤ d`, `a+b+c+d = 1`; recall `α = 1/15`):
```
(I)   d ≥ 1/2  (dominant; contains the dyadic)
(II)  d < 1/2,  gap G  (u,v,w,z all > 0)
(III) d < 1/2,  non-gap,  w ≥ −2α  AND  z ≥ −2α
(IV)  d < 1/2,  non-gap,  w < −2α  OR  z < −2α   (extreme)
```
**Exhaustive and disjoint.** `d ≥ 1/2` vs `d < 1/2` splits (I) from (II–IV). Within `d < 1/2`: the gap `G` (`u,v,w,z > 0`) is disjoint from the non-gap (some excess `≤ 0`); within the non-gap, `w ≥ −2α ∧ z ≥ −2α` (regime III) vs `w < −2α ∨ z < −2α` (regime IV) are complementary. Every config lands in exactly one regime.

**Closure in every regime** (Xiang with `≤ 3` marks forces `A ≤ α = 1/15`, hence `Liu ≤ 8/15 = f(3)` via `Liu = (1+A)/2`):
- **(I)** `d ≥ 1/2`: the **5-cap contradiction** `{a, b−a, c−b, 2d−1, |a+b−c|}` (certified `lemma-u3-5cap-dominant.md`, §5d.2). Equality iff the dyadic `(1,2,4,8)/15`.
- **(II)** gap `G`: the **3-mark sliver** `A = 1−2d = u−z < α` (certified `lemma-u3-sliver-gap.md`, §5d.3). Strict (no equality in `d < 1/2`).
- **(III)** non-gap, `w,z ≥ −2α`: if `u ≤ 0`, cap `a ≤ α`; if `v ≤ 0`, cap `b−a ≤ α`; if `w ∈ [−2α, 0]`, cap `|a+b−c| = |α+w| ≤ α` (§5d.1); if `z ∈ [−2α, 0]` (with `u,v,w > 0`), cap `|b+c−d| = |α+z| ≤ α` (§5e.4). These four sub-cases are exhaustive over regime III (in `d < 1/2`, `u > z`; if `u > 0` and `v > 0` and `w > 0` and `z > 0` we are in gap `G`, excluded; so at least one of `u,v,w,z ≤ 0`; `w ≤ 0` splits at `−2α`, `z ≤ 0` splits at `−2α`, giving the four sub-cases). Strict (no equality: the dyadic is in regime I).
- **(IV)** extreme `w < −2α ∨ z < −2α`: the **7-cap contradiction** of §5e.1–5e.3 (this round, PROPOSED `lemma-u3-7cap-extreme`). Strict (global extremum `12α/13 < α`).

**Lower bound `L(3)` (CERTIFIED, imported).** Against the level-3 dyadic `(1,2,4,8)/15`, every real Xiang response gives `A ≥ 1/15 = α(3)`, i.e. `Liu ≥ 8/15 = f(3)` (cell-complex vertex enumeration, `lemma-vertex-principle-advantage.md`; reviewed and re-verified round 4). The dyadic therefore attains `Liu = 8/15` against the pair-pile (regime-D equality), and Liu cannot be forced below `8/15` by any Xiang response.

**Combining.** `L(3)`: `c(3) ≥ 8/15` (Liu plays the dyadic). `U(3)`: `c(3) ≤ 8/15` (regimes I–IV cover every Liu config; Xiang forces `Liu ≤ 8/15` in each). Equality `c(3) = 8/15` is attained iff Liu plays the dyadic `(1,2,4,8)/15` (the unique equality case, in regime I). Therefore

> **`c(3) = 8/15`** (= `2^3 / (2^4 − 1)`), rigorously end-to-end. ∎

**Verification.** (`/tmp/round-6/u3_7cap_verify.py`, exact `Fraction` arithmetic.) (a) Regime IV: 5473 exact-rational extreme configs (random + chain-excess grid `N=18`), **0 violations** (min of 7 caps `≤ α` everywhere), worst `min = 0.0582 < α = 0.0667` (margin `0.0085`). (b) LP per sub-case (scipy `linprog`, float): `max t < 0` strictly in all 8 sign-triples (global max `min-cap = 4/65 = 0.0615 < α`, margin `1/195 ≈ 0.0051`), confirming the inequality is strict throughout regime IV. (c) Drop-one (coarse grid): dropping `C1,C2,C3,C4,C6` gives many violations (these are unambiguously load-bearing); `C5`/`C7` appear droppable on the coarse grid but the explorer's 2M-sample search confirmed drop-`C7` fails by ~0.002 (the 7th cap `|a+b−d|` is genuinely load-bearing on fine samples). The 7-cap family is sufficient (the proof above does not rely on minimality).

**Do-not-retry list (round 6, cumulative additions).** Do NOT add the cap `d−b−c` to the extreme-regime family (un-realizable when `z < −2α`, i.e. `d < b+c`). Do NOT use the gap-G sliver `|2d−1|` for the `z < −2α` half (requires `d ≥ b+c`, opposite). Do NOT claim the 6-cap `{C1..C6}` suffices (boundary failure on fine samples — `C7` is load-bearing). The round-5 "no 4–7-cap subfamily suffices" ruling is OVERTURNED for the extreme sub-cases (regime IV) specifically — the 17-family is still the engine for regime III's `z ∈ [−2α, 0]` sub-case (via the realizable `|b+c−d|`, §5e.4).

---

## Promotable lemmas

8. **Lemma U(3) — 7-cap extreme-regime contradiction (regime IV) — NEW (round 6).** Statement: for every `n = 3` Liu config `(a,b,c,d)`, `a ≤ b ≤ c ≤ d`, `a+b+c+d = 1`, in the extreme regime `E = {d < 1/2 ∧ (w < −2α ∨ z < −2α)}` (α=1/15; chain excesses `u=a−α, v=(b−a)−α, w=(c−a−b)−α, z=(d−b−c)−α`), Xiang with `≤ 3` marks forces `min(a, b−a, c−b, d−c, |a+b−c|, |a+c−d|, |a+b−d|) ≤ α(3) = 1/15` (hence `Liu ≤ 8/15 = f(3)`), STRICTLY (no equality in `E`). The 7 caps are each realized by an explicit ≤3-mark strategy, all *always-realizable* (none requires `d ≥ b+c`): the 4 chain caps via §5d.1 (certified); `|a+b−c|` via "bisect `d` + match `a` in `c`" (§5d.1, certified); the two NEW abs caps `|a+c−d|` via "bisect `b` + match `a` in `d`" and `|a+b−d|` via "bisect `c` + match `a` in `d`" (§5e.1). Mechanism: assuming all 7 caps `> α`, the 2³ = 8 sign triples of `(C5,C6,C7)` partition `E` exhaustively; each sub-case yields a ≤4-line inequality contradiction in chain-excess coordinates (using the identity `7u+4v+2w+z = α` and `L_6 − L_7 = u+w` where `L_6=7u+3v+2w, L_7=6u+3v+w`). The tightest sub-case `(s5,s6,s7)=(+,+,+)` gives `S2 ∧ C6+ ⟹ v > α`, `C5+ ∧ C6+ ⟹ 7u+3v < 2α`, hence `u < −α/7 < 0` contradicting `C1: u > 0`; the global extremum of the 7-cap min over `E` is `12α/13 = 4/65 < α` (margin `1/195`). Proved in full in this file (§5e.1–5e.3); verified 0 violations on 5473 exact-rational extreme configs + LP `max t < 0` in all 8 sub-cases (`/tmp/round-6/u3_7cap_verify.py`). **Candidate for certification** into `results/imo-2026-03/lemmas/lemma-u3-7cap-extreme.md`. SCOPE: the extreme regime `E` (regime IV) of `U(3)` only; does NOT cover regimes I–III (handled by the 5-cap, sliver, and `|a+b−c|`/`|b+c−d|`/`a`/`b−a` caps respectively) and does NOT generalize to `n ≥ 4`.

9. **Cap realizability: `|b+c−d|` via "bisect `a` + match `c` in `d`" — NEW (round 6, small).** Statement: for any 4-piece config `(a,b,c,d)`, `a ≤ b ≤ c ≤ d`, Xiang's 2-mark strategy (bisect `a → (a/2,a/2)`; split `d → (c, d−c)`) yields final multiset `{a/2,a/2,b,c,c,d−c}` with two cancelling pairs `(a/2,a/2),(c,c)` and two singletons `b, d−c`, giving `A = |b−(d−c)| = |b+c−d|`. Always realizable (no `d ≥ b+c` condition). This closes the realizability gap in round-5 §5d.4's regime-III `z ∈ [−2α, 0]` sub-case (where `|b+c−d| = |α+z| ≤ α`). Proved in §5e.4. **Candidate for certification** (or fold into an expanded `lemma-u3-5cap-dominant.md` scope note).

1. **Lemma `U(2)` (four-strategy upper bound, equality iff dyadic).** Statement: for every `n=2` Liu config `(a,b,c)`, `a ≤ b ≤ c`, `a+b+c=1`, Xiang with `2` marks forces `Liu ≤ 4/7`, with strict inequality for non-dyadic configs; equality (cap `= 4/7`) iff `(a,b,c) = (1/7, 2/7, 4/7)`. Mechanism: four explicit strategies `A, B, C, E` (Section 4) with bounds `(1+a)/2`, `(1+b−a)/2`, `(1+c−b)/2`, `max(c, 1−c)`; the inequality `min ≤ 4/7` with equality-iff-dyadic is a `4`-way contradiction on `(a,b,c)`. Proved in full in this file (Section 4). **Already CERTIFIED** (`lemmas/lemma-u2-four-strategy.md`, round 2).

2. **Lemma `U(1)` (two-mode, corrected boundary).** Statement: for `n=1`, `c(1) ≤ 2/3`, equality iff the dyadic `x = 1/3`. Mechanism: bisect mode (`x ≤ 1/3`, `Liu = (1+x)/2 ≤ 2/3`) and sliver mode (`x ≥ 1/3`, `Liu = 1−x ≤ 2/3`); the threshold `x = 1/3 = α(1)` is the dyadic boundary. Proved in Section 2. Already implicit in round 1's certified `U(1)`; not re-certified here.

3. **Lemma (dyadic-ratio overshoot, one-step) — round 3.** Statement: in one greedy pile-match step on the two largest pieces `a_1 ≥ a_2` with `a_1 ≥ 2 a_2` (admissibility), replacing `a_1` by `{a_2, a_1 − a_2}`: the multiplicity of the value `a_2` increases by `+1` (strict-dominant, `a_1 > 2 a_2`) — making the `a_2`-block even-multiplicity (the pair cancels, contributing `0` to `A`) when `a_2` was the generic 2nd-largest with multiplicity `1` — or by `+2` (dyadic ratio, `a_1 = 2 a_2`) — making the `a_2`-block odd-multiplicity (overshoot, contributing `±a_2 ≠ 0`). Corollary: the greedy cancels its created pair iff `a_1 > 2 a_2` strictly; the order-`n` dyadic has `a_1 = 2 a_2` at every level (telescoping), so the greedy overshoots on the dyadic at every step — the greedy is regime-N only, and the dyadic must be routed to the pair-pile (regime D). Proved in full in this file (Section 5b.6). **Already CERTIFIED** (`lemmas/lemma-dyadic-ratio-overshoot.md`, round 3, with parity caveat). NOTE: a CHARACTERIZATION (dyadic detection), NOT a regime-N upper-bound proof.

4. **Lemma S1 (balanced-config sliver forcing) — NEW (round 4).** Statement: for the balanced Liu config `(w, w, …, w)` (`n+1` copies, `w = 1/(n+1)`), Xiang with at most `n` marks forces `A(final) ≤ 2s` for every `s ∈ (0, w/2)`; hence `inf_Xiang A = 0 < α(n) = 1/D(n)`. The config is therefore regime-N for every `n ≥ 1` (non-dyadic for `n ≥ 2`; for `n = 1` the balanced config `(1/2, 1/2)` is non-dyadic, regime-N, covered by `U(1)` Mode S). Mechanism: explicit sliver strategy — `n` odd: cut a sliver `s` from each of `n` pieces (one left untouched); `n` even: bisect one piece to `(w/2, w/2)`, cut slivers `s` from `n − 1` others. In both cases the final multiset's pair-excesses all cancel except for two single-sliver leftovers at opposite-parity ranks, summing to `2s`. Proved in full in this file (Section 5c.3); verified by exact rational arithmetic for `n = 1, …, 7`. **Candidate for certification** into `results/imo-2026-03/lemmas/lemma-s1-balanced-sliver.md`. SCOPE: balanced configs only; NOT a universal regime-N proof.

5. **Proposition (grid equality-case necessary condition) — NEW (round 4).** Statement: at the level-`n` dyadic Liu config, for any `1/D(n)`-grid-aligned Xiang refinement, `A = α(n)` iff (odd piece-count) all pair-excesses `0` and smallest piece `= 1`, or (even piece-count) exactly one pair-excess `= 1` and the rest `0` (equivalently, the odd-multiplicity values are `{1}` or a consecutive pair `{a, a+1}`). Mechanism: repackaging the certified integer-grid parity theorem (`A·D(n)` is a non-negative odd integer `≥ 1`; equality forces the sum of non-negative pair-excesses `+` leftover to equal `1`). Proved in Section 5c.1. **Candidate for certification** as a corollary of the grid-parity lemma (the necessary-condition statement is a clean repackaging; the `a = 2^j` refinement is empirical and explicitly NOT claimed). SCOPE: grid-only at the dyadic; does NOT lift to reals (per the grid-parity lemma's caveat).

6. **Lemma U(3) — 5-cap dominant-regime contradiction (equality iff dyadic) — NEW (round 5).** Statement: for every `n = 3` Liu config `(a,b,c,d)`, `a ≤ b ≤ c ≤ d`, `a+b+c+d = 1`, `d ≥ 1/2`, Xiang with `3` marks forces `min(a, b−a, c−b, 2d−1, |a+b−c|) ≤ α(3) = 1/15` (hence `Liu ≤ 8/15 = f(3)`), with equality (the min `= 1/15`) iff `(a,b,c,d) = (1,2,4,8)/15` (the order-3 dyadic). Mechanism: five explicit strategies (`S_a` bisect `b,c,d`; `S_{b−a}` match `a` in `b` + bisect `c,d`; `S_{c−b}` match `b` in `c` + bisect `a,d`; `S_{2d−1}` match `a,b,c` in `d`; `S_{|a+b−c|}` bisect `d` + match `a` in `c`), each giving the named affine/abs-linear cap; the contradiction assumes all five `> 1/15` and splits on the sign of `a+b−c` (Case i `c < a+b−1/15` ⟹ `a > 2/15` ⟹ `d < 6/15` contradicting `d > 8/15`; Case ii `c > a+b+1/15` ⟹ `a+b+c > 7/15` ⟹ `d < 8/15` contradicting `d > 8/15`). Equality analysis pins `(1,2,4,8)/15`. Proved in full in this file (§5d.2); verified 0 violations on grids `N = 60,90,120,150` + 50k random, unique equality at the dyadic. **Candidate for certification** into `results/imo-2026-03/lemmas/lemma-u3-5cap-dominant.md`. SCOPE: the dominant (`d ≥ 1/2`) regime only (the `d < 1/2` regime is handled by the sliver + 17-family, §5d.3–5d.4).

7. **Lemma U(3) — 3-mark sliver strategy (gap closure, `d < 1/2`) — NEW (round 5).** Statement: for an `n = 3` Liu config `(a,b,c,d)` in the gap region `G = {a > α, b−a > α, c > a+b+α, d > b+c+α, d < 1/2}` (equivalently the chain excesses `u,v,w,z > 0` with `u > z`), Xiang's 3-mark strategy — split `d → (b, c, d−b−c)` [pairs `(b,b),(c,c)`] + shave `a → (ε, a−ε)` — forces `A = a − (d−b−c) = 1 − 2d = u − z < α(3) = 1/15` strictly. Mechanism: the two pairs cancel; the 5-leftover sort `c,c,b,b,a−ε,d−b−c,ε` gives `A = (a−ε)−(d−b−c)+ε = a − (d−b−c) = u − z`, independent of `ε`; the bound `u − z < α` follows from `7u+4v+2w+z = α` (identity) with `u,v,w,z > 0`. The strategy generalizes `S_{2d−1}` (gives `|2d−1|` universally; realizable iff `d ≥ b+c` for `d < 1/2`, always for `d ≥ 1/2`). Proved in full in this file (§5d.3); verified on 22 gap configs, `ε`-independent. **Candidate for certification** into `results/imo-2026-03/lemmas/lemma-u3-sliver-gap.md`. SCOPE: the gap region `G` only; NOT a universal `d < 1/2` proof (the non-gap `d < 1/2` sub-cases are covered by the 17-family, §5d.4, with extreme sub-cases `w < −2α` or `z < −2α` an open GAP).
