# proof-reviewer — round 4 (imo-2026-03)

Reviewed three built approaches adversarially. Each reviewed independently; the verdict on one does not carry to another. Re-derived every load-bearing claim with exact-rational python (`fractions.Fraction`).

---

## 1. `cell-complex-l3` — **L(3) for reals CLOSED** (VERIFIED MILESTONE)

**Status:** `partial` (honestly flagged by the builder). **Verdict: CHANGES REQUESTED.**
**Outcome: `verified-milestone`.**

The headline claim is that `L(3)` over reals is closed: against Liu's level-3 dyadic `(1,2,4,8)/15`, every real Xiang response with ≤ 3 marks gives `A ≥ 1/15 = α(3)`. I verified this independently and rigorously.

### Adversarial checks performed

**(a) Vertex-principle validity.** The proof's Lemma 4: "a continuous piecewise-linear function on a compact polytope attains its min at an arrangement vertex; if `A ≥ 1` at every vertex, `A ≥ 1` everywhere." This is the standard LP/polytope fact (an affine function on a compact polytope attains its min at a vertex; the sub-level set is a face, inductively a vertex). I re-derived the cell-by-cell reduction: for each cell `C`, `min_{cl(C)} A = min_{vertices of cl(C)} A(v)`. Since `[0,1]^3 = ∪ cl(C)` (finite union), the global min is the min over all cell-vertices. **Valid.**

**(b) Flat-facet concern (the dispatch's critical subtlety).** The minimizer is NOT a unique vertex — it is a positive-dimensional flat polytope (verified: shifting all 3 Xiang marks by a common offset preserves `A = 1/15`; single-mark perturbations either increase `A` or stay flat). The dispatch worried: "if the facet contains points with `A <` its vertices' `A`, the claim fails."

I checked this explicitly. For an **affine** function on a polytope, the minimum is **always** attained at a vertex; an affine function cannot have a strict interior minimum. If the function is constant on a facet (flat min region), ALL vertices of that facet attain the min. The facet's interior is a convex combination of the facet's vertices (all with `A = min`). So the flat facet's vertices are arrangement vertices with `A = 1/15`, captured by the enumeration. I confirmed: the 5 min-attaining multisets (boundary vertices of the flat region, including `(4,4,2,2,1,1,1)` = pair-pile / mirror) all give `A = 1/15` exactly. **The vertex check validly covers the flat minimizer.** The flat-facet analysis is needed only for equality characterization, not for the bound. The proof's Remark on the flat-facet concern is correct.

**(c) Continuity (Lemma 1).** The proof argues: a vanishing sub-piece (length → 0) is the smallest (rank `M`), contributes `(−1)^{M+1}·0 = 0`, and removing it decreases `M` by 1 while preserving the signs of all larger sub-pieces. I checked: the vanishing piece has length 0 ≤ any positive length, so it's at rank `M` (or tied). Removing the `M`-th piece leaves ranks 1..`M−1` with the same signs `+,-,+,...,(−1)^{i+1}` in both the `M`- and `(M−1)`-piece alt-sums. **Valid.** I also spot-checked the continuity at `x → 1/15` (both limits agree: `A → 1/3`).

**(d) Piecewise-linearity (Lemma 2).** Within each cell, the sorted order of the 7 sub-pieces is constant (no two equal, none zero), so the sign assignment is fixed, and each sub-piece length is affine in the mark-vector (difference of two cut-points). So `A = Σ ±(sub-piece)` is affine on the cell. **Valid.**

**(e) Arrangement completeness (the dispatch's "missing cell" worry).** The arrangement `H` = piece-equality (`s_a = s_b`, 21 hyperplanes) ∪ piece-zero (`s_a = 0`, 7 hyperplanes), within each of 20 distributions `(k_1,k_2,k_3,k_4)`, `Σ k_j = 3`. I checked:
- **E hyperplanes** capture sort-order changes (interior cell boundaries). ✓
- **Z hyperplanes** capture sub-piece vanishing (mark at Liu mark = distribution boundary; two marks coinciding; mark at stick endpoint). These are the boundary of the feasible region AND distribution changes. ✓
- Marks at stick endpoints (`0` or `1`) create zero sub-pieces → Z hyperplanes. ✓
- Fewer than 3 marks: unused marks placed at an endpoint → Z hyperplanes, continuous extension (Lemma 1). ✓
- Degenerate vertices (≥ 4 active hyperplanes): captured by a rank-3 triple subset. ✓
The arrangement is **correct and complete** over the whole mark-simplex `[0,1]^3` (all real Xiang responses, including degenerate/ coincident marks). No missing cell class.

**(f) Enumeration correctness.** I re-ran `/tmp/round-4/cell_vertex_exhaustive.py` (pure `fractions.Fraction`, no float). Output reproduces exactly:
- 20 distributions, 65520 triples examined (`20 × C(28,3)`), 26940 unique-solved systems, **11523 feasible (nonneg) vertices**, 120 distinct piece-multisets, **0 violations** (`A < 1`), min `A = 1` (= `1/15` real), 5 min-attaining multisets (`(4,4,2,2,1,1,1)`, `(5,4,2,2,1,1,0)`, `(4,4,3,2,1,1,0)`, + 2 more).
- The enumeration solves the `7×7` exact-rational system (4 sum-rows + 3 hyperplane-rows) per distribution × triple, rejecting inconsistent / rank-deficient / negative systems. It accepts only triples where the 3 hyperplanes + 4 sum-constraints give full rank 7 (genuine vertices). **Exhaustive and reproducible.**

**(g) Independent cross-check.** I ran `/tmp/round-4/sanity_check.py`: 226981 grid points (denom 60) + 300000 random exact-rational marks in `[0,1]^3`. **0 violations**, min `A = 1/15` in both. Consistent with Lemma 5, rules out an enumeration bug.

**(h) Does this close L(3) fully?** **YES.** The vertex-principle (valid) + exhaustive enumeration (reproducible, 0 violations) + tightness (certified mirror config `A = 1/15`) constitute a complete, rigorous proof of `L(3)` over reals. By Lemma G (`Liu = (1+A)/2`), `Liu ≥ 8/15 = f(3)`. This is the **first real-`n ≥ 3` lower-bound foothold** — a breakthrough milestone.

**What is NOT closed (honest):**
- `c(3) = f(3)` is NOT solved end-to-end: the upper bound `U(3)` (regime-N for n=3) is owned by `two-regime-disjunctive` and is OPEN.
- General-n lift: the vertex-principle applies for every fixed n (Lemmas 1–4 are general-n), but the arrangement grows exponentially (`~n!·2^n`); direct enumeration is infeasible for large n. The inductive lift (dyadic self-similar recursion via `M⊎R`) is a GAP, not claimed.
- The builder's status `partial` is correct (the approach targets `c(n) = f(n)` end-to-end; `L(3)` is the lower-bound half at n=3 only).

**Score:** Correctness 10/10, Completeness/rigor 9/10 (L(3) airtight; general-n gap honestly flagged), Progress 9/10 (first real-n≥3 lower-bound foothold).

**Promotable lemma certified:** `lemmas/lemma-vertex-principle-advantage.md` — the vertex-principle for the advantage sum (general-n technique, n=3 enumeration certificate). Rigorous, reusable, sorry-free.

---

## 2. `pairing-partner` — L(3) unrefined-R sub-case PROVED; general-n CONJECTURE

**Status:** `partial` (honestly flagged). **Verdict: CHANGES REQUESTED.**
**Outcome: `advanced`.**

### Adversarial checks performed

**(a) L(3) unrefined-R sub-case proof (§B).** I re-derived the closed form `A = 7 − 2(s_3+s_5)` (in `1/15` units) from scratch:
- Setup: `M = 8`, `R = (4,2,1)`, 3 marks in M → `m_1 ≥ m_2 ≥ m_3 ≥ m_4`, `Σ = 8`, `m_1 ≥ 4`. `σ = m_2+m_3+m_4 = 8 − m_1 ≤ 4 = a_1`.
- Merge `{b_1,b_2,b_3} = {m_2,m_3,m_4}` with `R = {4,2,1}` → `s_1 ≥ … ≥ s_6` (6 pieces, total `σ + 7`). `s_1 = 4` (since `b_1 ≤ σ ≤ 4`).
- `A = m_1 − s_1 + s_2 − s_3 + s_4 − s_5 + s_6`. Using `s_2+s_4+s_6 = (σ+7) − s_1 − s_3 − s_5 = σ + 3 − s_3 − s_5` and `m_1 = 8 − σ`:
  `A = (8−σ) − 4 + (σ+3−s_3−s_5) − (s_3+s_5) = 7 − 2(s_3+s_5)`. ✓ (Verified on 100000 random configs, 0 mismatches.)

I re-derived the 3-case casework on `t_2` (the 2nd-largest of `{b_1,b_2,b_3,2,1}`), `A ≥ 1 ⟺ t_2 + t_4 ≤ 3`:
- **Case I** (`t_2 > 2`): ≥ 2 b's exceed 2 → `σ > 4`. Impossible. ✓
- **Case II** (`t_2 = 2`): forces `b_3 ≤ 1` (else `σ > 4`) → `t_4 ≤ 1` → `t_2+t_4 ≤ 3`. ✓
- **Case III** (`t_2 < 2`): `b_1 < 2`, `t_1 = 2`, `t_2 = b_1`. Three sub-cases (IIIa `b_2 ≥ 1 ≥ b_3`: `t_4 = 1`, sum `< 3`; IIIb `b_2 ≥ b_3 ≥ 1`: `t_4 = b_3`, `t_2+t_4 = σ−b_2 ≤ 3` strict; IIIc `b_3 ≤ b_2 ≤ 1`: `t_4 = b_2`, sum `< 3`). ✓

All cases disjoint, exhaustive, each settled. 100000 random configs: 0 violations `A < 1`, min `A = 1`. Equality cases `{2,1,1}` (staircase) and `{2,2,0}` (degenerate) both give `A = 1`. ✓

**(b) Superincreasing-R identity (§A).** `a_j − Σ_{l>j} a_l = 1/D(n+1) = α(n+1)`. For n=3 (level-3, `D=15`): `a_1 − (a_2+a_3) = 4 − 3 = 1`, `a_2 − a_3 = 2 − 1 = 1`. ✓ Corollary `Σ_{MM} m_even ≤ σ ≤ M/2 = a_1 = R_largest`: `m_1 ≥ M/2` (largest of ≥ 2 pieces), so `σ = M − m_1 ≤ M/2 = a_1`. ✓

**(c) General-n conjecture.** The rank-index Hall matching `s_3 + s_5 + … + s_{2n+1} ≤ a_2 + … + a_{n+1}` is verified `n = 1..5` (I re-ran: worst slack 0, −1, −2, −5, −10; all ≤ 0). **HONESTLY flagged as a CONJECTURE, not proved.** The per-position bound `s_{2j} ≤ a_{j+1}` FAILS (counterexample `b=(4/3,4/3,4/3)` at n=2). The layer-cake condition is too strong. The matching is genuinely on the sum over rank indices. ✓ (Correctly not certified.)

**(d) Honest scope.** The build explicitly flags: covers ONLY the `k = n+1` (unrefined-R, all marks in M) sub-case at n=2 (level-3 dyadic). The R-refined sub-cases (`k ≤ n`) are OPEN (refinement breaks superincreasing structure). Full `L(3)` over reals is NOT closed by this approach alone — the cell-complex-l3 sibling closes it via vertex enumeration; this is a parallel, corroborating foothold. The build says so plainly. ✓

**No gap in what's claimed; the open gaps are honestly stated.**

**Score:** Correctness 10/10, Completeness/rigor 9/10 (sub-case airtight; general-n honestly open), Progress 8/10 (first real-valued k≥2 foothold on G1, parallel to cell-complex).

**Promotable lemmas certified:**
- `lemmas/lemma-superincreasing-R.md` — the superincreasing identity + obstruction bound. Rigorous, reusable.
- `lemmas/lemma-L3-unrefined-R-subcase.md` — the L(3) unrefined-R sub-case (closed form + casework). Rigorous, specific milestone.
- General-n Hall matching: REJECTED for certification (honestly flagged as conjecture by the builder; not proved).

---

## 3. `two-regime-disjunctive` — three sliver-forcing lemmas + grid classification; universal regime-N OPEN

**Status:** `partial` (honestly flagged). **Verdict: CHANGES REQUESTED.**
**Outcome: `partial`.**

### Adversarial checks performed

**(a) Sliver-forcing Lemma S1 (balanced config, all n).** I re-derived `A = 2s` for both parities:
- n odd: `w` at rank 1 (+), `n` copies of `w−s` at ranks 2..n+1 (sign-sum `T_1 = −1` for n odd starting at `−`), `n` copies of `s` at ranks n+2..2n+1 (sign-sum `T_2 = +1` since first sign `(−1)^{n+3} = +1` for n odd). `A = w − (w−s) + s = 2s`. ✓
- n even: `w` (+), `n−1` copies `w−s` (`T_1 = −1`, n−1 odd), 2 copies `w/2` (consecutive, contribute 0), `n−1` copies `s` (`T_2 = +1`). `A = w − (w−s) + s = 2s`. ✓
- Verified exactly for n=1..7 (`A = 2s` matches to exact rational equality; `2s < α(n)` in every case). ✓
- `A ≥ 0` always (non-neg pair-excesses + non-neg leftover), so `inf A = 0 < α(n)`. ✓
- Genuinely real-valued (slivers are real cuts, not grid-only). ✓

**(b) S2 (two-dyadic n=3 `(1/2,1/4,1/8,1/8)`).** 2 marks: cut `1/2 → (1/4,1/4)`, cut one `1/4 → (1/8,1/8)`. Final `{1/4,1/4,1/8,1/8,1/8,1/8}`, `A = (1/4−1/4)+(1/8−1/8)+(1/8−1/8) = 0 < α(3)`. ✓ (Verified exactly.)

**(c) S3 (extreme-dominant n=3 `(L,t,t,t)`, `L > 4/5`).** 3 marks cut L into 4 equal `L/4`. Final `{L/4×4, t×3}`. For `L > 4/7`: `L/4 > t`, sort valid. `A = (L/4−L/4)+(L/4−L/4)+(t−t)+t = t = (1−L)/3`. For `L > 4/5`: `(1−L)/3 < (1/5)/3 = 1/15 = α(3)`. ✓ (Verified for `L = 9/10` (`A = 1/30`), `L = 5/6` (`A = 1/18`), `L = 81/100`.) The `(1−L)/3 < 1/15 ⟺ L > 4/5` check: `1−L < 1/5 ⟺ L > 4/5`. ✓

**(d) Grid equality-case classification (5c.1).** I re-derived: at the dyadic, grid-aligned, `A* = A·D(n)` is a non-negative odd integer ≥ 1 (certified grid-parity). Equality `A* = 1`:
- Even M: `Σ e_i = 1` ⟹ exactly one `e_i = 1` (rest 0) ⟹ odd-mult leftover `{a, a+1}` consecutive. ✓
- Odd M: `Σ e_i = 0` and `q_M = 1` ⟹ odd-mult leftover `{1}`. ✓
- The `a = 2^j` refinement is **honestly flagged as empirical** (the parity theorem permits any `a ≥ 1`; which `a` are achievable by ≤ n marks is a strategy-existence question the census answers empirically). NOT claimed as proved. ✓

**(e) Honesty of the universal regime-N gap.** The build explicitly flags: the grid classification does NOT lift to reals (per the grid-parity lemma's caveat). The sliver-forcing lemmas cover only 3 structural classes (balanced all-n, two-dyadic n=3, extreme-dominant n=3 `L > 4/5`); moderately-dominant `L ∈ [8/15, 4/5]` and near-dyadic balanced perturbations are UNCOVERED. The universal regime-N cover for n≥3 is OPEN. ✓

**(f) Avoidance of dead ends.** Does NOT retry R-pile (falsified round 3, 3 counterexample classes). Does NOT retry `M−total(R)=α(n+1)` (dyadic-only, foreclosed). Does NOT import (U-E) as closure. Does NOT claim the classification alone gives the SIDE `A < α` (needs sliver forcing, not supplied universally). ✓

**Score:** Correctness 10/10, Completeness/rigor 8/10 (three lemmas + classification airtight; universal regime-N honestly open), Progress 7/10 (three new real-valued regime-N structural classes + clean grid classification, but universal cover still open).

**Promotable lemmas certified:**
- `lemmas/lemma-s1-balanced-sliver.md` — S1 balanced-config sliver forcing (all n, reals). Rigorous, reusable.
- `lemmas/lemma-grid-equality-case.md` — grid equality-case necessary condition (corollary of grid-parity). Rigorous, grid-only, reusable.

---

## Certification summary

Five new lemmas certified into `results/imo-2026-03/lemmas/`:
1. `lemma-vertex-principle-advantage.md` (cell-complex) — the vertex-principle + n=3 enumeration certificate.
2. `lemma-superincreasing-R.md` (pairing-partner) — superincreasing identity + obstruction bound.
3. `lemma-L3-unrefined-R-subcase.md` (pairing-partner) — L(3) unrefined-R sub-case (closed form + casework).
4. `lemma-s1-balanced-sliver.md` (two-regime) — balanced-config sliver forcing (all n, reals).
5. `lemma-grid-equality-case.md` (two-regime) — grid equality-case necessary condition.

Rejected: the general-n superincreasing-R Hall matching (conjecture, not proved — honestly flagged by the builder).

**Total certified lemmas in cache: 16** (11 prior + 5 new).

---

## Verdicts (per slug, routed independently)

| slug | Status | Verdict | Outcome | Note |
|---|---|---|---|---|
| `cell-complex-l3` | partial | CHANGES REQUESTED | `verified-milestone` | L(3)-reals CERTIFIED via vertex-principle + exhaustive enumeration (11523 vertices, 0 violations, min A=1/15); c(3) needs G2, general-n lift open |
| `pairing-partner` | partial | CHANGES REQUESTED | `advanced` | L(3) unrefined-R sub-case (k=n+1) PROVED over reals (closed form + casework); superincreasing-R lever formalized; general-n conjecture OPEN; R-refined sub-cases OPEN |
| `two-regime-disjunctive` | partial | CHANGES REQUESTED | `partial` | S1 balanced all-n + S2 two-dyadic + S3 extreme-dominant n=3 PROVED; grid classification rigorous (grid-only); universal regime-N n≥3 OPEN |

**`current.md` updated:** Status remains `partial`. The `L(3)`-over-reals milestone (cell-complex) is recorded under Current best + Open gaps (G1 partially closed at n=3, general-n open). The L(3) unrefined-R sub-case (pairing-partner), the superincreasing-R lever, Sliver S1, and the grid equality-case classification are recorded as certified milestones. Full proof still absent (G1 general-n and G2 regime-N n≥3 both open; `c(3) = 8/15` not yet end-to-end — lower bound closed, upper bound open).
