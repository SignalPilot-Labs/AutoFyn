## imo-2026-03 (lens: nonlinear telescoping potential / supermartingale unifying BOTH bounds)

### Terrain through this lens

**The load-bearing identity is arithmetic, not structural — and that is the crux of the wall.** Verified exactly for n=1..5:
```
1 / g_n  =  1 / c(n)  =  Σ_{k=0}^{n} 2^{-k}  =  2 − 2^{-n},
```
where `g_n = 2^n / D_n` is Liu's largest dyadic piece. Liu's largest piece IS `c(n)`; its reciprocal IS the telescoping sum. So the "level-k contribution to 1/c" is `2^{-k}`, and the recursion `1/c(n) = 1/c(n−1) + 1/2^n` is literally the statement "going from level n−1 to level n adds `1/2^n` to the reciprocal of Liu's largest piece."

This is the natural level object the dispatch asked for. But note carefully: the sum `Σ 2^{-k}` lives on `1/c(n)` (the reciprocal of Liu's guarantee), NOT on `D` directly. The target `D = 1/D_n` is related by `c(n) = 2^n · D_target`, i.e. `D_target = c(n)/2^n`. So a single unified Ψ must reconcile `Σ 2^{-k}` (on `1/c`) with `1/D_n` (on `D`) — they differ by the factor `2^n`. Any unified potential must carry that factor `2^n` explicitly.

**The factor-of-2 wall, restated sharply.** A linear potential `Φ = α·D + β·(leftover)` changes by `O(piece/2)` per equal-split (both `D` and the leftover couple linearly to a piece that halves geometrically under equal-halving). The schedule `Σ piece_k/2` is a geometric series with ratio 1/2, summing to `≈ 2 × (first term)`. With `first term ≈ 1/2` (Liu's largest piece at unit scale), this lands at `Φ ≤ O(1/2^n) = 2/2^{n+1} ≈ 2·(1/D_n)`. **The factor of 2 is the geometric-series tail `Σ 2^{-k} = 2 − 2^{-n} ≈ 2`**, not a coincidence: the geometric decrement ratio 1/2 sums to 2, which is precisely twice the target `1/D_n ≈ 1/2^{n+1}`. So linear telescoping is doomed by the geometric-ratio arithmetic itself, not by a bad ansatz.

**The factor of 2 must come out NONLINEARLY.** To halve the linear bound `2·(1/D_n)` down to `1·(1/D_n)` requires exploiting a binary relation that linear functionals cannot see: that the equal-halving reply produces PAIRS that cancel in D (the peeling lemma / equal-halve-n-largest lemma). Each pair-cancellation removes TWO pieces from D's contribution, but a linear Φ charges each piece once. The factor of 2 lives in the pair structure.

### Distinct openings (each a different attack the outliner could build)

**Opening A — Pair-count-exponential potential.** Define `Φ(config) = (lone piece) · 2^{#(equal-pair cancellations)}`. At equal-halving on dyadic: lone = `g_0 = 1/D_n`, #pairs = n, so `Φ = (1/D_n)·2^n = c(n)`. The bound `Φ ≤ c(n)` would be the upper bound (Xiang's reply), and `Φ ≥ c(n)` for Liu's dyadic strategy would be the lower bound — both via the SAME invariant. The decrement per equal-split: lone is unchanged (small piece untouched), #pairs goes up by 1 ⇒ `Φ` doubles. To keep `Φ ≤ c(n)` we'd need the lone to halve when a pair forms, which is exactly the dyadic-tower coupling `g_{k-1} = g_k/2`. **Hard step:** generalizing "equal-pair cancellations" to non-equal splits (config-dependent, not robust); the natural generalization `(lone)·2^{floor(m/2)}` fails at Liu's unsplit dyadic (no pairs, lone = 0 when m = n+1 even). Risk: collapses to pairing-charging.

**Opening B — Reciprocal-largest-piece martingale / optional stopping.** `Ψ = 1/M` (M = current largest piece). At Liu's dyadic config, `Ψ = 1/g_n = 1/c(n) = Σ 2^{-k}` ✓. Under Xiang's equal-halving, M halves ⇒ `Ψ` doubles (multiplicative, not additive). Treat Xiang's split choice as a stochastic process: if Xiang random-equal-halves the largest piece at each step, `log Ψ` does a random walk with +log 2 drift; optional stopping pins `E[Ψ]`. But the worst-case (adversarial Xiang) is what we need for the upper bound, so optional stopping gives the WRONG direction (it averages, not extremizes). This opening is likely a dead end for the upper bound but **could certify the lower bound** if the martingale is a SUBmartingale under Liu's strategy (Liu forces Ψ to stay ≥ 1/c(n)). The parity-process `j(t)` under random Xiang play is the natural substrate. **Hard step:** proving a submartingale inequality for `1/M` against adversarial splits; the worst case (equal-halving) drives Ψ up, which is the right direction for the LOWER bound but the wrong direction for the upper.

**Opening C — Band-decomposition of the parity integral.** Decompose `D = ∫[j(t) odd] dt` into bands `(g_{k-1}, g_k]` (in `1/D_n` units). At Liu's unsplit dyadic, band `k` has length `2^{k-1}/D_n` and `j = k`, contributing `2^{k-1}/D_n · [k odd]`. So `D_init = (1/D_n)·Σ_{k odd} 2^{k-1}`. Xiang's equal-halving kills all odd-band contributions except the bottom band `(0, g_0]` (= `1/D_n`). The "telescoping" here is `Σ_{k odd} 2^{k-1} → 1` — a down-telescope killing levels top-down. The UPPER-bound target `D ≤ 1/D_n` becomes "Xiang kills all odd bands above the bottom"; the LOWER bound becomes "Liu's dyadic forces at least one odd band to survive at level 1." This is structurally orthogonal to the pairing framing (it lives on the t-axis, not the piece-axis) and unifies both bounds through band-parity. **Hard step:** for non-equal Xiang splits, the bands fragment and the clean `[k odd]` parity becomes a coupled XOR profile (exactly the overlap `C` of Lemma 5 in `dyadic-induction`); closing the multi-split gap is equivalent to showing the band-parity telescope survives fragmentation. This is the SAME gap as the shared G1, restated in band language — so it's not a bypass, just a different lens on the same wall.

### Promising vs dead (honest)

- **Linear potentials: DEAD** (alternating-potential round 2, confirmed). The wall is arithmetic (geometric ratio 1/2 sums to 2), not fixable by tuning weights.
- **Opening A (pair-count-exponential):** the ONLY opening I can see that has a clean factor-of-2 escape mechanism (the exponential in #pairs generates the missing factor 2). But it is config-fragile — "equal pairs" don't exist in arbitrary configs. Generalizing to "virtual pairs" (a sorted-pair-deficit schedule) lands back in linear territory. **Plausible but high-risk; may collapse to pairing-charging.**
- **Opening B (reciprocal martingale):** multiplicative increment escapes the linear wall in FORM, but optional stopping gives an average, not an extremum — wrong direction for adversarial bounds. Likely only useful for the LOWER bound, and the lower bound is the shared gap G1 already attacked elsewhere. **Likely dead for the upper bound.**
- **Opening C (band-parity):** structurally clean and orthogonal to pairing, but the multi-split fragmentation reduces EXACTLY to the shared overlap-bound gap `2C ≥ D_{R_0}+D_F+1−M` (Lemma 5 of dyadic-induction). It is a re-lensing, not a bypass. **Not a new route; a unifying language for the existing wall.**

**Bottom line:** I could not find a concrete nonlinear invariant that escapes the factor-of-2 wall AND does not collapse into the pairing framework. The wall is deep (arithmetic from the geometric ratio), and the only structural fact that supplies the missing factor 2 — pair-cancellation — is already the load-bearing machinery of `pairing-charging` and the certified `equal-halve-n-largest` / `peeling` lemmas. A "nonlinear telescoping potential" approach is therefore best understood NOT as a genuinely new route, but as a UNIFYING LANGUAGE that reframes the two bounds through one identity (the dyadic tower `1/g_n = Σ 2^{-k}`), with the actual proof still riding on pair-cancellation.

### Convergence risk

**HIGH.** Any successful nonlinear invariant here must exploit pair-cancellation to get the factor-of-2 saving (arithmetic necessity). Pair-cancellation is the defining bet of `pairing-charging` and the certified content of the `peeling` + `equal-halve-n-largest` lemmas. So a built "telescoping-potential" approach will, at the moment its gap closes, have re-derived the pairing construction under a potential-function hat. The dispatch explicitly warned about this collapse. The honest evaluation: this lens UNIFIES the two bounds conceptually (via `1/g_n = Σ 2^{-k}`) but does NOT supply a proof route orthogonal to pairing.

### Cheap-kill candidates

- The identity `1/g_n = Σ 2^{-k}` is a free cheap fact (verified n=1..5, arithmetic) — usable as the "telescoping increment" hook in any approach's writeup, no proof needed.
- Band-parity decomposition of `D_init = (1/D_n)·Σ_{k odd} 2^{k-1}` (verified n=1..5 via the parity integral) — gives a clean structural reason why `D_init ≥ 1/D_n` (at least one odd band survives). Could short-circuit the Case-A sub-lemma.
- No genuine cheap kill for the open gaps (the multi-split overlap bound and the complementary upper regime both require real work).

### Knowledge-base entries to use

- **Invariants & monovariants** (combinatorics) — the natural home for a potential function.
- **Double counting** (the parity-integral `D = ∫[j odd]` is already a double-count identity; band decomposition double-counts band-by-band).
- **Constructive vs existence** — the unified-Ψ framing is a "find a single functional" existence claim, which the rigour rules require to be backed by a concrete construction (Opening A's `Φ = lone·2^{#pairs}` is the candidate, but config-fragile).
- **Induction** (the recursion `1/c(n) = 1/c(n−1) + 1/2^n` invites strong induction on n; the inductive step would need the band-parity telescope to survive one more level — equivalent to the G1 multi-split gap).

### Analogous past problems (cruxes)

- **aimo-0019** (games-and-strategy + invariants-and-monovariants) — the Austria paint-pot game. Crux: "maintain a linear potential `ink ≤ 3·x_r` via amortized induction, exploiting the dyadic-distinctness invariant (at most one interval of each length beyond the frontier)." This is the SAME amortized-linear-potential template that `alternating-potential` round 2 already tried to transfer and CONCEDED (the dyadic-distinctness invariant has no analog in our toggle-sets `[0,v)∪[u,p)` which nest at the bottom and overlap arbitrarily at the top). **The concession is sound; do not retry aimo-0019's template directly.** But the dispatch's question — "does a nonlinear invariant avoid the wall?" — is answered by aimo-0019 negatively for the LINEAR template; the nonlinear question is genuinely open.
- **aimo-0117** (games-and-strategy) — the dyadic-sequence "largest strictly exceeds sum of all others" (`2^j > 2^{j-1}+...+2^{-i}`). Crux: assign played values as a two-sided geometric (dyadic) sequence so the largest dominates. This is EXACTLY Liu's dyadic construction (`g_n = 2^n/D_n > (2^n−1)/D_n = sum of rest`). The crux is already load-bearing in our lower-bound construction; no new lift here, but confirms the dyadic tower is the right level structure.
- **aimo-0043** (invariants-and-monovariants) — "repeatedly place obstacle on the larger of two competing options, at-most-halving the surviving count; compare total obstacles to threshold." Crux: halving count gives geometric decay. **This is the structural cousin of the factor-of-2 wall** (halving ⇒ geometric ⇒ Σ = 2× first term). Suggests the wall is fundamental to any halving-based schedule; a nonlinear escape must NOT be a halving schedule (it must be pair-cancellation, which is quadratic/categorical, not geometric).

No crux in the corpus resembles a "nonlinear telescoping potential unifying two bounds through one identity" — the closest is aimo-0019's amortized potential, which is linear and has been ruled out. **No genuinely analogous past problem found for this specific lens.**

### Prior progress (current best, round 3)

- Answer `c(n) = 2^n/(2^{n+1}−1)` verified n=1..5; both bounds proved for n=1,2; lower bound proved for Cases A/B/C (all n) plus n=2 two-mark; upper bound closed for regime `p_{n+1} ≤ 1/D_n` (all n, via equal-halve-n-largest lemma, CERTIFIED).
- Shared gap: G1 multi-split non-tie (overlap bound `2C ≥ D_{R_0}+D_F+1−M`), open for n ≥ 3.
- Approach-specific gap: G2-general complementary regime `p_{n+1} > 1/D_n` (flat Liu configs), open for n ≥ 3.
- **Linear potentials CONFIRMED DEAD** (factor-of-2 wall, alternating-potential round 2).

### Dead ends (do not retry)

- **Linear amortized potentials `Φ = α·D + β·(leftover)` or `Φ = D − λ·Π` (Π = pair-deficit sum):** confirmed dead (alternating-potential round 2). Both `D` and `leftover` change by `O(piece/2)` per equal-split; geometric decrement sums to `2 × target`; factor of 2 short. The wall is arithmetic (geometric ratio 1/2 sums to 2), not fixable by weight tuning.
- **aimo-0019 amortized-linear-potential template direct transfer:** the dyadic-distinctness invariant (at most one interval of each length beyond the frontier) has no analog in our toggle-sets `[0,v) ∪ [u,p)` (they nest at the bottom, overlap arbitrarily at the top). Already conceded in alternating-potential round 2; do not retry without first specifying a concrete substitute invariant.
- **Opening B (reciprocal martingale) for the UPPER bound:** optional stopping averages; adversarial Xiang needs extremum. Likely only useful for the lower bound (submartingale direction). Do not pursue for upper bound.

### Small-case / intuition notes (CONJECTURE, not proved)

- `1/g_n = Σ 2^{-k}` is arithmetic (n=1..5 verified, exact). The recursion `1/c(n) = 1/c(n−1) + 1/2^n` is the level-n increment to the reciprocal of Liu's largest piece.
- `D_init = (1/D_n)·Σ_{k odd} 2^{k-1}` (band-parity decomposition, verified via the parity integral for n=1..5). Conjecture: the lower bound `D ≥ 1/D_n` is equivalent to "at least one odd band above the bottom survives Xiang's splits" — equivalent to the G1 overlap bound, restated. NOT a bypass.
- The factor-of-2 wall is the geometric-sum identity `Σ 2^{-k} ≈ 2` manifesting as the gap between linear Φ's `O(1/2^n) = 2·(1/D_n)` and the target `1/D_n`. Conjecture: ANY telescoping potential whose per-level decrement is `O(piece/2)` (geometric ratio 1/2) hits this wall; only a potential whose per-level decrement is `O(piece)` (ratio 1, NOT halving) or that exploits pair-cancellation (categorical, not geometric) can escape. This is the rigorous reason nonlinear is necessary but does not by itself prove an escape exists.
- `Φ = lone·2^{#pairs}` equals `c(n)` at the equal-halving extremum (verified n=1..5 by arithmetic). Conjecture: a config-robust generalization of "#pairs" could give a unified invariant at `c(n)`. The generalization is the hard step; the obvious one (`floor(m/2)`) fails at Liu's unsplit dyadic (no pairs). This is the most promising single lead but is explicitly flagged as config-fragile.

### One concrete slugged approach skeleton for the outliner

**Slug: `nonlinear-tower-potential`**

1. Define `Ψ(config) := (lone piece in sorted-desc, i.e. `a_m` if `m` odd else `0`) · 2^{N(config)}` where `N(config)` is a config-robust "pair-cancellation count" generalizing "number of equal pairs" to arbitrary configs (e.g. `Σ_j 1_{a_{2j-1} = a_{2j}}`, or a continuous relaxation `Σ_j exp(−(a_{2j-1}−a_{2j})/ε)` taking `ε→0`).
2. **Lower bound:** show Liu's dyadic config forces `Ψ ≥ c(n)` after any ≤ n Xiang splits, by proving `N(config)·(dyadic-tower structure) ≥ n` (each Xiang split can destroy at most one level of the dyadic tower, and the lone piece compensates). This is the band-parity survival conjecture, restated.
3. **Upper bound:** show Xiang's equal-halving reply achieves `Ψ = c(n)` (lone = `g_0 = 1/D_n`, `N = n` pairs cancelled ⇒ `Ψ = (1/D_n)·2^n = c(n)`); and that any Xiang reply has `Ψ ≤ c(n)` (the lone cannot grow beyond `g_0` without destroying pairs proportionally). **Hard step:** the trade-off inequality `lone · 2^N ≤ c(n)` for non-equal splits — this is where the approach either succeeds (genuine nonlinear escape) or collapses into pairing-charging (if the proof reduces to "exhibit a pairing partition").
4. **Unification:** `Ψ = c(n)` iff `D = 1/D_n`, via the arithmetic `c(n) = 2^n·(1/D_n)`. Both bounds are the single statement `Ψ = c(n)` at the extremum.
5. **Hard steps identified:** (a) defining `N` config-robustly without collapsing to pairing; (b) proving the `lone · 2^N ≤ c(n)` trade-off for arbitrary splits (this IS the open upper-bound gap G2-general, restated); (c) proving the lower-bound side `Ψ ≥ c(n)` (this IS the open overlap-bound gap G1, restated in band-parity language). The approach UNIFIES the language but does NOT bypass either gap — it re-frames them through one identity.
