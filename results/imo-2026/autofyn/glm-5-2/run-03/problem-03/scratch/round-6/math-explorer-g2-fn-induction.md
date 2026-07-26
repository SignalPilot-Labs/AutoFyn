# imo-2026-03 — G2 general-n upper bound, `f_n` recursive-functional induction lens

Scout route: does the Theorem-6 (n=3 Case-C) template generalize to n=4's very-flat regime? Reports terrain for the outliner; no proof attempted.

## (a) n=4 very-flat characterization + gap parametrization + box bounds

**Constants.** `D_4 = 2^5 − 1 = 31`, target `D ≤ 1/31` (`S_odd ≤ 16/31`). Lemma-5 threshold `g_3 = 2^3/D_4 = 8/31`. Spiky threshold `g_0 = 1/31`. Dyadic vertex `p* = (16/31, 8/31, 4/31, 2/31, 1/31)`.

**Very-flat polytope `Π_4`** (open interior, the regime NOT closed by Lemma 4 spiky or Lemma 5 peel-once):
`Π_4 = {p_1 ≥ p_2 ≥ p_3 ≥ p_4 ≥ p_5 ≥ 0, Σ=1, p_2,p_3,p_4 < 8/31 (=g_3), p_5 > 1/31}`.
(p_5 < 8/31 is automatic from p_5 ≤ p_4 < 8/31. p_1 is the largest, unconstrained above except by sum: p_1 = 1 − (p_2+p_3+p_4+p_5) > 1 − 3·(8/31) − 1 = 1 − 25/31 = 6/31; in fact p_1 ≥ p_2 so p_1 ≥ ~8/31-ish on the interior, growing toward 16/31 at the dyadic corner.)

**Gap parametrization** (generalizes n=3's `w,z,y,x` to 5 pieces → 5 gaps; n=3 had 4 gaps `w=p_4, z=p_3−p_4, y=p_2−p_3, x=p_1−p_2`; n=4 adds one more interior gap):
```
w := p_5,  z := p_4 − p_5,  y := p_3 − p_4,  x := p_2 − p_3,  u := p_1 − p_2,  all ≥ 0
p_5=w, p_4=w+z, p_3=w+z+y, p_2=w+z+y+x, p_1=w+z+y+x+u
sum constraint:  5w + 4z + 3y + 2x + u = 1.
```
**Dyadic gap values at `p*`:** `w = 1/31, z = 1/31, y = 2/31, x = 4/31, u = 8/31` (dyadic doubling of the upper gaps; the two SMALLEST gaps `w,z` hit `1/D_4` exactly, the larger gaps double). This generalizes n=3, where dyadic gave `w = 1/15, z = 1/15, y = 2/15, x = 4/15`. (So at every level, the dyadic vertex is the corner where `w = z = 1/D_n` simultaneously, with the upper gaps `2/D_n, 4/D_n, …, 2^{n−1}/D_n`.)

**Box bounds on `w` in the "all lower gaps `z,y,x ≥ 1/31`" sub-case** (the n=4 analog of n=3 Theorem-6 sub-case 3, where `z,y ≥ 1/15`): from `p_2 = w+z+y+x < 8/31` with `z,y,x ≥ 1/31` we get the loose bound `w < 5/31`; but the SUM constraint `5w + 4z + 3y + 2x + u = 1` with `z,y,x ≥ 1/31, u ≥ 0` gives `5w + 9/31 + u = 1` i.e. `5w + u = 22/31`, hence `u ≥ 0` tightens to `w ≤ 22/155 ≈ 0.142` (strictly below the loose `5/31 ≈ 0.161`). So **`w ∈ (1/31, 22/155)`** in this sub-case (vs n=3's clean `p_4 ∈ (1/15, 2/15)`). The sum-constraint coupling is the new wrinkle: at n=4 the box-bound arithmetic involves 5 gap variables linked by a weighted sum, not the 3 effectively-independent variables of n=3. The dyadic vertex `w = 1/31` is the spiky-facet corner of this box (on the already-proved Lemma-4 side), and `z = 1/31` is the sub-case-3 boundary — exactly mirroring n=3's closure geometry, but with a heavier bookkeeping surface.

## (b) Exact-rational sweep result (CONJECTURE-LEVEL evidence, NOT a proof)

Defined the recursive construction value `f_2 = min(c, |2a−T|, a−b, b−c)` (certified n=2 menu, `T`=rest total), `f_3 = min` over all 6 peels `(i,j)` (i≠j, p_i ≥ p_j) of `f_2(rest_3pc)`, `f_4 = min` over all 10 peels of `f_3(rest_4pc)`. Each level uses `n` marks (peel 1 + `(n−1)`-menu): f_2 ≤ 2 marks, f_3 ≤ 3, f_4 ≤ 4 — exact budget. Rest = `{p_i − p_j} ∪ {p_k : k≠i,j}` (Lemma 3 / `lemmas/peeling.md` makes the equal pair parity-neutral, so `D_final = D_rest` exactly).

**Findings (exact rational, `fractions`):**
- `f_4(p*) = 1/31` EXACTLY (asserted). The dyadic vertex is tight, no slack — consistent with the conjecture (any upper-bound construction loose at dyadic is dead).
- **0 escapes** of `f_4 > 1/31` over: 64 near-dyadic corner configs (perturb `p_2 = 8/31−ε, p_5 = 1/31+ε` with dyadic middle, ε ∈ {1,…,8}/248), 8000 random very-flat interior configs (denominators 31·8, 31·12, 31·16, 31·24), and a fine grid (the first run reached 228k configs before timeout, 0 escapes throughout).
- **Worst interior value found: `3/124 ≈ 0.0242`** (well below `1/31 ≈ 0.0323`); the random sweep's worst interior configs sit far from dyadic. The near-dyadic ray confirms `f_4 → 1/31` STRICTLY FROM BELOW: at ε = 1/248, 1/496, 1/992, 1/1984, 1/3968, 1/7936 the gap `1/31 − f_4 = ε/2` exactly (1/124, 1/248, 1/496, 1/992, 1/1984, 1/3968). So slack grows `≈ ε/2` along the dyadic ray — same order as n=3's `≈ 2ε`.
- One-sided perturbation (only `p_2 = 8/31 − ε`, `p_5` pinned just above `1/31`) also approaches `1/31` from below: at ε = 1/63488, `f_4 ≈ 0.03223` (gap `≈ 2.7e-5`).

**Conclusion (conjecture-level):** the uniform-in-n `f_n` conjecture **HOLDS at n=4 numerically**: `f_4 ≤ 1/31` on `Π_4^{cl}` with equality ONLY at the dyadic vertex `p*` (on the Lemma-5 / Lemma-4 facets); on the open interior `f_4 < 1/31` strictly, supremum `1/31` approached only at `p*`. Labeled CONJECTURE — a sweep is evidence, never a proof.

## (c) Does the Theorem-6 3-subcase template propagate? — NO, not as a clean human-readable proof

I classified, over 3000 random very-flat configs, which top-level peel `(i,j)` and which sub-peel (within `f_3`) ACHIEVE the min (i.e. is the binding strategy). Distribution:

**Top-level binding peel (10 candidates):** `p_1→p_2` 60.0%, `p_1→p_4` 15.3%, `p_1→p_3` 12.5%, `p_2→p_3` 8.5%, `p_1→p_5` 3.7% (the other 5 peels: ~0%). **Sub-peel within `f_3` (6 candidates):** `(0,1)` 44.1%, `(1,2)` 32.3%, `(0,3)` 18.5%, `(0,2)` 5.2%.

**Contrast with n=3.** The n=3 Theorem-6 proof worked because each of the 3 sub-cases had a SINGLE binding peel (peel A / peel B / peel C), and sub-case 3's peel C had a SORT-INDEPENDENT member (`p_1` always largest in the rest ⇒ `b−c = |y−p_4|` regardless of regime). That "one sort-independent member per sub-case" is what collapsed the ~20-expression arrangement into 3 lines.

**At n=4 this breaks.** The binding peel is NOT a function of a single gap threshold; it spreads across 5 peels (60/15/12/8/4%). No single peel's rest has an always-largest piece that covers the whole "all gaps ≥ 1/31" residual the way n=3's peel C did. (Peel `p_2→p_3` — the literal n=3-peel-C analog — does have `p_1` always-largest in its rest, giving a sort-independent `f_3` sub-structure, but it binds only 8.5% of the time; it does NOT dominate the "all gaps ≥ 1/31" residual at n=4 the way it did at n=3.) The construction value is still PWL and still maximized at dyadic (per (b)), but the human-readable packaging is genuinely heavier.

**Verdict:** the Theorem-6 template (3-subcase + sort-independent member + `min(a−b,b−c)≤(a−c)/2` absorption) does **NOT** propagate as a 3–4-line proof to n=4. n=4 needs one of: (i) a **fresh, larger sub-case table** (~5 sub-cases, one per binding peel, each still possibly absorbable by `min(a−b,b−c)≤(a−c)/2`-style identities but with 5-gap box arithmetic — heavier, maybe still hand-checkable), or (ii) a **mechanical vertex enumeration** (the KB *Piecewise-concavity smoothing* entry certifies the max of a PWL function on a compact polytope is at an arrangement vertex; enumerate the finitely many vertices of the n=4 sort-regime arrangement, evaluate `f_4` at each exactly, confirm `≤ 1/31` with equality only at `p*` — rigorous but ugly, ~10²–10³ vertices for n=4), or (iii) a **uniform-induction shortcut** that bypasses per-level casework entirely (see (d)/(e)).

## (d) Obstruction to a uniform induction

1. **Single-sort-independent-member property breaks.** The n=3 collapse relied on sub-case 3's peel C giving ONE sort-independent menu member covering the entire "all gaps ≥ 1/D_n" residual. At n=4, the residual's binding peel varies (5 peels needed); there is no single sort-independent member per residual. So the inductive step "the residual is closed by one sort-independent member" does NOT lift.

2. **Sub-case count grows.** n=3 had 2 interior gaps `(z,y)` ⇒ `2²−1 = 3` sub-cases (one gap small / the other / both large). n=4 has 3 interior gaps `(z,y,x)` ⇒ the naive generalization is `2³−1 = 7` sub-cases (or a 4-way "which gap is small" partition + the all-large residual). The approach file's `~4·5^{n−2}` arrangement-expression estimate gives ~100 expressions at n=4 (vs ~20 at n=3) — still mechanically tractable but no longer hand-elegant; at n=5 it reaches ~500 and the human-readable route is dead.

3. **Box-bound coupling.** At n=3, the box bounds (`y∈[1/15,2/15), p_4∈(1/15,2/15)`) were 3 effectively-independent variables. At n=4 the sum constraint `5w+4z+3y+2x+u=1` couples 5 gap variables with distinct weights, so each sub-case's box bounds are more intricate (e.g. the all-gaps-≥1/31 sub-case gives `w ∈ (1/31, 22/155)` only after combining the sum constraint with `u ≥ 0`, not the naive `w < 5/31` from `p_2<8/31` alone). The arithmetic is still finite and exact, but the per-sub-case bookkeeping surface grows.

4. **The `min(a−b,b−c)≤(a−c)/2` identity still absorbs sort-regimes WITHIN a sub-case** (verified: the identity is arity-2 and applies wherever a 3-piece rest has its middle piece straddling the two boundary pieces). It does NOT reduce the NUMBER of sub-cases (the cross-gap partition), only the sort-regime fan-out inside each. So the absorption lever survives but does not tame the cross-gap growth.

**Net.** A uniform induction `f_n` PWL/max-at-dyadic is **numerically true at n=4** but does NOT admit the n=3-style 3-line human-readable step. The honest paths are: mechanical vertex enumeration per level (rigorous, exponential, script-verified — viable for n=4,5 then dead), OR a genuinely different framing that bypasses the recursive peel-then-menu cascade (see (e)).

## (e) Genuinely-different G2 framing (far from peel-then-menu AND from per-region LP)

**Direct parity-coverage / measure-extremal bound on `D = ∫[j(t) odd] dt`.**

The certified parity-integral lemma (`lemmas/parity-integral.md`) gives `D = ∫_0^∞ [j(t) odd] dt`, and the parity-XOR toggle (Cor 2.1) says each Xiang split `p → u+v` toggles parity on `[0,v) ∪ [u,p)` — two intervals, total measure `2v` (v = smaller fragment). So Xiang's `≤ n` cuts are `≤ n` parity-toggle operators, each painting a two-interval (total `2v`) region of the `t`-axis; `D` is the residual ODD-measure after all toggles.

**The framing.** Instead of constructing an explicit Xiang strategy (peel-then-menu) or solving a per-region LP (fix Liu, optimize cuts in each sort-region), ask directly: *given Liu's `(n+1)`-piece partition (which fixes the initial `j_0(t)` and hence the initial odd-measure `D_0`), what is the MINIMUM residual odd-measure achievable by `≤ n` parity-toggles each covering a two-interval total-`2v` set (with `v` chosen by Xiang)?* This is a global measure-covering / amortized-coverage extremal problem on the `t`-axis, NOT a constructed-strategy bound. The target `1/D_n = 1/(2^{n+1}−1)` is the residue of the geometric series `Σ_{k=0}^n 2^{−k} = 2 − 2^{−n}` — strongly suggesting a dyadic-coverage bound: each toggle covers `2v`, the maximal dyadic tiling of the odd-region leaves an uncovered sliver of measure exactly `1/D_n`, attained when Liu's config is dyadic (the fixed point of dyadic self-similarity, where every toggle exactly tiles).

**Why this is far from both existing G2 routes:**
- *Not peel-then-menu (pairing-charging):* that route CONSTRUCTS a specific adaptive strategy (peel `p_1→p_j` + certified `(n−1)`-menu) and bounds its `D`. The parity-coverage route bounds the OPTIMAL toggle coverage directly — no strategy constructed, no peel cascade, no per-level menu. The dyadic-config tightness is explained structurally (dyadic = self-similar fixed point of the toggle tiling), not by exhibiting an equal-halving reply.
- *Not per-region LP (lp-dual-region):* that route FIXES Liu's config and optimizes Xiang's continuous cut-positions WITHIN each sort-region of the final 2n+1 pieces (a partition of cut-space by sort-order hyperplanes). The parity-coverage route does NOT fix Liu's sort regime — it works on the `t`-axis measure directly, agnostic to the final piece sort. It is a global amortized-cover bound, not a per-region LP.

**Crux-move analog (crux corpus).** `aimo-0019` (paintful game on the real line, combinatorics/games-and-strategy + invariants-and-monovariants) is the closest corpus crux: a two-player covering game on the real line with dyadic-length pieces, won by B via a **look-ahead dyadic-frontier strategy** ("respond by painting the cell beyond the frontier, not the gap at the frontier, so no cell-size is painted twice ahead") plus a **linear-potential amortized bound** ("ink spent on `[0,x_r]` ≤ `3x_r`", proved by amortized induction charging each frontier advance against the dyadic pieces it absorbs). The crux move — amortized dyadic-frontier potential bounding cumulative coverage by a constant times progress — is the analog to adapt here: a potential `Φ(toggle-set) = (covered odd-measure) − λ·(progress)` that is monovariant, with the residue `1/D_n` emerging as the dyadic-amortization slack. (Caveat: run-state records that aimo-0019's structural-inventory invariant "has no analog" for the LOWER bound / linear-in-D potential, which is DEAD by a factor of 2 — but that ruling was about a `Φ = D − λΠ` potential on the lower-bound side; the UPPER-bound parity-coverage amortization is a different object, on the toggle-covering side, and is not pre-falsified. Flag as risky-but-novel.)

**Candidate cheap-kills before committing to the heavy route:**
- Parity/counting: each toggle flips parity on a set of measure `2v`; `n` toggles flip total measure `≤ 2·Σ v_i`. Bound the residual odd-measure by inclusion-exclusion on the toggle sets (a Bonferroni/union-bound first pass). Likely too loose (gives `O(1/2^n)`, the factor-of-2 wall) but cheap to check.
- Dyadic-pigeonhole: the largest uncovered odd-interval after `n` dyadic toggles has measure `≥ 1/2^{n+1}`; refine to `1/(2^{n+1}−1)` by the geometric-series residue (the toggles can't all be dyadic-aligned unless Liu is dyadic). This is the lever to make rigorous.

## Summary for the outliner

- **Distinct openings surfaced:**
  1. **Mechanical vertex enumeration at n=4** (rigorous, ~10²–10³ vertices, KB *Piecewise-concavity smoothing*; closes n=4 G2 as a verified milestone, doesn't generalize to general n but proves the `f_n` conjecture's n=4 instance).
  2. **Fresh 5-subcase gap table at n=4** (heavier n=3-Theorem-6 analog: one sub-case per binding peel, `min(a−b,b−c)≤(a−c)/2` absorbs intra-sub-case sort-regimes, 5-gap box arithmetic; maybe hand-checkable, generalizes messily).
  3. **Direct parity-coverage / amortized dyadic-frontier bound** (the genuinely-different framing in (e); bypasses the peel-then-menu cascade and the per-region LP; aimo-0019 crux; risky-but-novel, not pre-falsified for the upper bound).
  4. **Uniform-induction shortcut on the recursive `f_n`** (prove PWL + max-at-dyadic as a structural theorem, not per-level casework — the conjecture's intended vehicle; the obstruction in (d) is the missing "sort-independent member" lift, so this needs a NEW invariant beyond `min(a−b,b−c)≤(a−c)/2`, e.g. a dyadic-self-similarity-fixed-point argument).

- **Candidate technique(s):** Piecewise-concavity smoothing (KB) for the vertex-enumeration route; amortized-potential / monovariant (KB *Invariants & monovariants*) for the parity-coverage route; the certified `peeling` + `peel-once-inductive` + `parity-integral` lemmas are the existing machinery.

- **Cheap-kill candidates:** (1) inclusion-exclusion / Bonferroni union bound on `n` toggle-sets (likely too loose, factor-2 wall — record to avoid); (2) dyadic-pigeonhole on the largest uncovered odd-interval (the lever to make rigorous, gives `1/2^{n+1}` naively, needs the geometric-residue refinement to reach `1/D_n`); (3) the existing `cross-piece-equal-pair` cheap-kill (`lemmas/cross-piece-equal-pair.md`) already kills `p_k = p_i+p_j` configs — check whether the n=4 very-flat worst configs satisfy any cross-piece sum equality (if so, the cheap-kill closes them with `D=0`, far below `1/31`).

- **Knowledge-base entries to use:** *Piecewise-concavity smoothing* (vertex-enumeration route, the max-at-vertex principle); *Invariants & monovariants* + *Induction* (parity-coverage amortized potential); *Pigeonhole / extremal principle* (dyadic-pigeonhole cheap-kill).

- **Analogous past problems (cruxes):** `aimo-0019` (paintful line game) — crux = amortized dyadic-frontier linear potential `ink ≤ 3·progress`, look-ahead "paint beyond the frontier so no cell is painted twice" strategy; analogous because it is a two-player covering game on the real line with dyadic-length pieces won by an amortized dyadic-coverage bound with a geometric-series residue — the same shape as the parity-coverage upper bound proposed in (e). No other corpus crux resembles the problem (the other games-and-strategy cruxes are board/grid placement games, not real-line measure games).

- **Prior progress:** n=3 G2 upper bound CLOSED & certified (`lemmas/case-c-n3.md`, Theorem 6 + Corollary 6.1). The `f_n` recursive-functional conjecture (PWL, max-at-dyadic, uniform-in-n) is verified n=3 (proved) + n=4 (this report, conjecture-level sweep, 0 escapes, tight at dyadic, slack `≈ ε/2` on the dyadic ray). n≥4 unverified-by-proof.

- **Dead ends (do not retry):** (1) naive `(n−1)`-mark surplus-chain telescope (leaves `p_{n+1}` unpaired, `D=|2p_1−1|`, 18050/30000 fail n=3 — `pairing-charging` §6.4'); (2) fixed finite Xiang family for n≥3 (insufficient, worst `0.097 > 1/15` — minimax round 4); (3) collapse-theorem / flattening-lemma route (monotonicity numerically FALSE n=2, 25293/49995 violations — outline-reviewer round 4); (4) Stackelberg-blind LP (integrality gap); (5) von-Neumann minimax (D not convex in cuts); (6) linear-in-D potential (factor-of-2 wall); (7) treating the n=3 Theorem-6 3-subcase as a uniform-in-n template — this report shows the single-sort-independent-member lift FAILS at n=4 (5 binding peels), so do NOT present `f_n`-induction as proved by "the same 3-subcase at every level."

- **Small-case / intuition notes (CONJECTURE):** `f_4 ≤ 1/31` on `Π_4^{cl}` with equality ONLY at `p* = (16/31,8/31,4/31,2/31,1/31)`, open interior strict, slack `≈ ε/2` on the dyadic ray — VERIFIED by exact-rational sweep (8000+ random + 64 near-dyadic corner + 228k-grid-prefix, 0 escapes), but NOT PROVED. The dyadic vertex is the self-similar fixed point of the peel-then-menu operator (every peel of a dyadic config yields a dyadic rest, so every menu expression is simultaneously tight); away from dyadic at least one peel breaks self-similarity and gives slack. The `f_n` conjecture's structure (PWL, unique max at dyadic) is numerically robust at n=4; the obstacle is purely proof-theoretic (no clean human-readable inductive step; the n=3 sort-independent-member lift breaks).
