# imo-2026-03 — measure-theoretic / analytic characterization of the D-extremizer

Lens: calculus of variations / KKT / measure characterization of the D-minimizing Xiang reply and the worst Liu config. Scout only.

## Setup recap (units: dyadic config `{1,2,…,2^n}`, total `D_n = 2^{n+1}−1`, target `D ≥ 1`)

`D = ∫_0^∞ [j(t) odd] dt` (parity-integral, CERTIFIED). For the multi-split G1-i sub-case (piece `2^n` split into `M, g_2,…,g_r`, `M ≥ 2^{n−1}` unique largest; dyadic rest `R_0 = {1,2,…,2^{n−1}}` with piece `2^{n−1}` UNSPLIT; Lemma 5 applies):

```
D = M − D_{R_0} − D_F + 2C        (Lemma 5, verified EXACT: 0 error over 8k trials, correct dyadic config)
```

where `D_{R_0} = |O_{R_0}|`, `D_F = |O_F|` are measures of the odd-parity regions, and `C = |O_{R_0} ∩ O_F|` is their overlap (all within `[0, 2^{n−1}]`).

## 1. Terrain through this lens

### The D-minimizing Xiang reply is NON-SMOOTH / piecewise (KKT stalls)
- The n=1 upper bound (PROVED) already exhibits the structure: Xiang's minimizer is `equal-split A` (regime `A ≥ 2/3`, gives `D = 1−A`) vs `barely-split A` (regime `A < 2/3`, gives `D = 2A−1`). Crossover at `A = 2/3` is a **kink**, not a critical point. The minimizer is a *combinatorial* choice (which pieces to split, in what ratio), sitting on **flat regions** between kinks.
- Consequence: pure variational / KKT methods (Lagrange multipliers on a continuous relaxation) **stall** — there is no smooth critical point to characterize. The extremal *value* `min_Xiang D` as a function of Liu's config is a piecewise-linear (in fact min-of-finitely-many-linear) function; it is continuous but non-differentiable. This is the **honest verdict**: variational characterization of the minimizer is dead; the live object is the extremal *value* and the *rigid structure of the dyadic rest's odd region*.

### The dyadic rest's odd-parity region is a rigid union of alternating dyadic intervals
- For the unsplit dyadic rest `R_0 = {1,2,4,…,2^{n−1}}` (superincreasing: each `2^k > Σ_{j<k} 2^j`), the `j`-function is a step function: `j(t) = n − 1 − k` on `[2^k, 2^{k+1})`. Hence `O_{R_0}` = union of `[2^k, 2^{k+1})` over `k` with `(n−1−k)` odd, i.e. **alternating dyadic intervals tiling `[1, 2^{n−1})`** (plus a constant-parity segment `[0,1)`).
- `D_{R_0}` (unsplit) `= (2^n + (−1)^{n−1})/3`: n=3→3, n=4→5, n=5→11, n=6→21. (Confirmed.)
- This rigidity is the analytic asset: `O_{R_0}` is not an arbitrary measurable set but a **fixed dyadic-tiling parity pattern**. `F`'s odd region `O_F ⊆ [0, W]` (`W = 2^n − M ≤ 2^{n−1}`) is constrained by `F` being a partition of `W`.

### Worst Liu config (max over Liu of min over Xiang of D) — numerically dyadic
- n=2: dyadic `(4/7,2/7,1/7)` gives `min_Xiang D = 1/7`; PROVED worst (the n=2 upper bound is tight only at dyadic, and the bound holds for all Liu).
- n=3: dyadic `(8/15,4/15,2/15,1/15)` gives `min_Xiang D = 1/15 = 0.0667`; coarse grid-Xiang search over 400 random Liu configs found worst `min_Xiang D = 0.0587 < 1/15`. Dyadic is the maximizer (numerical, conjecture).
- The dyadic config is the **most superincreasing** Liu config (`largest > sum of rest`, by exactly `1/D_n`). Flat configs (e.g. all-equal) allow Xiang to drive `D ≪ 1/D_n` (Lemma 4: `D = p_{n+1}`, small for spiky; and pair-cancellation for flat). So the conjecture "worst Liu = most superincreasing = dyadic" is robust.

## 2. Distinct openings

### Opening A — Union-measure reformulation of the overlap bound (G1-i, live)
Via inclusion–exclusion (`|O_{R_0} ∪ O_F| = D_{R_0} + D_F − C`) and the Lemma-5 identity:
```
D = M + D_{R_0} + D_F − 2|O_{R_0} ∪ O_F|     (verified EXACT, 0 error)
```
So `D ≥ 1 ⟺ |O_{R_0} ∪ O_F| ≤ (M + D_{R_0} + D_F − 1)/2`. **The overlap bound IS this union bound** — no easier rewrite exists via inclusion–exclusion alone; the slack is exactly the gap-to-trivial.
- The trivial bound `|union| ≤ 2^{n−1}` is **off by 1** from the target: it suffices iff `D_{R_0} + D_F ≥ 2^n − M + 1 = W + 1`, but `D_{R_0} + D_F` can be `≤ W` (e.g. `D_F` small). So the wall is exactly **"shave 1 unit off the trivial union bound."**
- The slack is **large in the easy regime** (clean single-split, 2^n→M+g2, rest unsplit: gap `(D−1)/2` = 1.0, 2.0, 5.0, 10.0 for n=3,4,5,6 — `D` is 3, 5, 11, 21 there, far above 1) and **shrinks to exactly 0** at the Lemma-6 tight family (multi-split barely-larger, `D = 1`).
- The "shave 1" is forced by the **dyadic-tiling rigidity of `O_{R_0}`**: `F`'s odd region (constrained to be the odd-parity set of a partition of `W` into ≤ `n` real pieces) cannot perfectly tile the complement of `O_{R_0}` in `[0, 2^{n−1}]`, because the complement is a union of superincreasing dyadic blocks whose lengths `1, 4, 16, …` do not match any achievable `O_F` profile at the boundary. **PROMISING but the tight case is measure-zero** — the proof must be exact (interleaving bookkeeping), not approximate.

### Opening B — "Worst Liu config = dyadic" collapse theorem (G2 → G1, bigger prize, higher risk)
If provable, `max_Liu min_Xiang D = min_Xiang D|_{dyadic} = 1/D_n` (G1), so G2 = G1 and the upper bound follows from the lower bound. Numerically robust (n=2 PROVED, n=3 numerical). The natural analytic handle is a **flattening / Robin-Hood lemma**: a transfer of mass from Liu's largest piece to his smallest (making the config less superincreasing) does NOT increase `min_Xiang D`. If true, iterating flattens to the all-equal config where `min_Xiang D = 0`, and the maximizer is at the opposite (most-superincreasing = dyadic) extreme.
- **HIGH RISK**: this is a minimax theorem (max of a min of a non-smooth piecewise function). Such theorems are often HARDER than the underlying inequality. The smoothing lemma is plausible (superincreasing = hard for Xiang) but I could not verify it numerically in a clean monotone form within budget. If the flattening lemma fails, the route dies with no partial credit.
- This is **genuinely orthogonal** to pairing (it attacks G2 via a minimax/convexity argument on Liu's side, not via constructing a Xiang partition).

### Opening C — Closed form of `min_Xiang D` as a function of Liu's sorted CDF
Sought a cleaner closed form for `D` (and `min_Xiang D`) in terms of the sorted piece CDF that would make both extrema obvious. **Did not find one** beyond the parity-integral itself. The reverse-CDF `j(t) = #{pieces ≥ t}` is the cleanest handle, and the dyadic config makes `j(t)` a specific step function, but `min_Xiang D` over the (combinatorial) split choices does not simplify to a closed form in Liu's CDF. Dead end for a cheap closed form.

## 3. Promising vs dead (honest)

- **Dead: smooth/KKT characterization of the minimizer.** The minimizer is piecewise, flat between kinks, non-differentiable (n=1 already shows the kink at `A = 2/3`). No critical-point equation to solve.
- **Live but tight-only-at-measure-zero: the union-measure bound (Opening A).** The analytic structure (dyadic alternating-interval `O_{R_0}`) is real and rigid, but the bound is slack everywhere except the Lemma-6 family, so an argument that is "almost tight" is not enough — the proof must achieve the exact deficit-≥1 at the tight config. This is the same wall as G1-i, just reframed in measure language. It is a **reframing of the existing overlap bound, not a bypass**.
- **Live, orthogonal, high-risk: the "worst Liu = dyadic" collapse (Opening B).** This is the only opening that attacks G2 by a genuinely different mechanism (minimax/convexity on Liu's side rather than constructing a Xiang partition). If the flattening lemma holds, it collapses G2 into G1 and is the single biggest structural payoff available. If it fails, nothing salvageable.

## 4. Convergence risk

- Opening A **converges toward the existing G1 overlap bound** — it is the same inequality in measure-theoretic clothing. It does NOT escape the wall; it re-states it. The outliner should NOT frame this as a new rival approach to G1; it is a re-derivation of the same gap. Useful only if the dyadic-tiling rigidity makes the "deficit ≥ 1" bookkeeping cleaner than the current XOR-overlap form (plausible for the unsplit-rest sub-case, unclear for the split-rest sub-case G1-ii).
- Opening B is **genuinely orthogonal** to the pairing-charging / dyadic-induction field (which all construct explicit Xiang replies). It is the only route that attacks G2 without building a partition. Risk: it may be strictly harder than G2 itself (minimax theorems usually are). Do NOT present as a cheap kill.
- Neither opening converges to the pairing mechanism. The union-measure route stays in the parity-integral frame; the collapse route stays on the Liu-side minimax.

## 5. Concrete slugged approach skeleton

**Slug: `measure-extremizer`**

Outline (for the outliner; hard steps flagged):
1. Import `lemmas/parity-integral.md`, `lemmas/splits-inequality.md` Lemma 5 identity (`D = M − D_{R_0} − D_F + 2C`, proven), and the union reformulation `D = M + D_{R_0} + D_F − 2|O_{R_0} ∪ O_F|` (verified exact here).
2. **Hard step 1 (G1-i, unsplit rest):** prove `|O_{R_0} ∪ O_F| ≤ (M + D_{R_0} + D_F − 1)/2` by exploiting that `O_{R_0}` is a union of alternating dyadic intervals `[2^k, 2^{k+1})` (superincreasing rest) and `O_F ⊆ [0, W]`. The complement of `O_{R_0}` in `[0, 2^{n−1}]` is a superincreasing-block pattern that `O_F` (the odd region of a partition of `W`) cannot tile perfectly — formalize the "deficit ≥ 1" via the superincreasing gap structure (each complement block `> sum of smaller complement blocks`).
3. **Hard step 2 (tight case):** at the Lemma-6 family (`2^n → {2^{n−1}+ε_1, …, 1+ε_n}`, rest unsplit), verify the bound is saturated and the deficit is exactly 1 — needs exact interleaving bookkeeping (the `ε_i` align `O_F`'s breakpoints with `O_{R_0}`'s dyadic edges).
4. **Hard step 3 (G1-ii, split rest — OPTIONAL):** when the rest's `2^{n−1}` is itself split, the Lemma-5 top band changes (`max(R) < 2^{n−1}`); re-derive the union bound. This is the hardest sub-case and may not yield to the same tiling argument.
5. **G2 collapse (SEPARATE, flag as high-risk):** prove the flattening lemma "Robin-Hood on Liu decreases `min_Xiang D`" ⟹ worst Liu = dyadic ⟹ G2 = G1. Flag as the riskier half; if the flattening lemma is not provable, this half dies and the approach survives only on the G1-i union bound (which is a reframing, not a new result).

**Hard steps:** (1) the exact "deficit ≥ 1" bookkeeping against the superincreasing complement blocks; (2) the tight Lemma-6 saturation arithmetic; (3) the G1-ii split-rest sub-case (top band shifts); (4) the flattening lemma for G2 collapse (may not exist — minimax theorems are hard).

## 6. Numerics summary (all CONJECTURE unless labelled PROVED)

- **G1 (D ≥ 1) on correct dyadic config: PROVED-numerically** — airtight step-by-step generator, 30k trials n=3,4,5, min `D = 1.000000` at n=3 k=3 (Lemma-6 family). No counterexample. (Confirms prior rounds' brute-force.)
- **G1-i targeted (2^n barely-split, rest dyadic unsplit + splits): min D = 1.000000** — no counterexample in 24k trials.
- **Union formula `D = M + D_{R_0} + D_F − 2|union|`: EXACT** (0 error, 8k trials, correct dyadic rest).
- **1-unit miss is large in easy regime**: clean single-split gives `D = 3, 5, 11, 21` for n=3,4,5,6 (gap `(D−1)/2` = 1, 2, 5, 10); the bound is tight (`D=1`) only at the multi-split Lemma-6 family. (CONJECTURE: the union bound's slack is non-negative everywhere, zero only at Lemma-6.)
- **Worst Liu = dyadic: PROVED n=2, CONJECTURE n=3** (coarse grid: dyadic `1/15 = 0.0667`, worst random `0.0587`).
- **D_R0 of unsplit dyadic rest = `(2^n + (−1)^{n−1})/3`** (CONJECTURE-as-formula, verified n=3..6).

## 7. Prior progress (this lens confirms)

- G1 Cases A/B/C PROVED (all n) — confirmed sound; the union-measure frame reproduces them.
- Lemma 5 identity PROVED exact — re-verified here.
- The overlap bound `2C ≥ D_{R_0} + D_F + 1 − M` is the live G1 gap; this lens finds it is **equivalent** to `|O_{R_0} ∪ O_F| ≤ (M + D_{R_0} + D_F − 1)/2` (union form), with the trivial bound off by exactly 1 — the wall is a "shave 1 unit" problem forced by dyadic-tiling rigidity. No easier reformulation found.

## 8. Dead ends (do not retry through this lens)

- **KKT / variational critical-point characterization of the Xiang minimizer** — non-smooth, piecewise, kinks at regime boundaries (n=1 crossover at `A = 2/3`). Dead.
- **Closed-form `min_Xiang D` in Liu's sorted CDF** — does not simplify beyond the parity-integral. Dead.
- **Trivial union bound `|O_{R_0} ∪ O_F| ≤ 2^{n−1}`** — off by exactly 1 from the target; insufficient (noted in splits-inequality.md as the "naive `C ≤ D_F`" failure, here re-derived as the union-side failure). Do not retry.
- **Earlier "violations" of G1 in this probe** — were a generator budget bug (contiguous-rest + over-budget splits); with the correct dyadic config and airtight split budget, no violations. The overlap bound holds.
