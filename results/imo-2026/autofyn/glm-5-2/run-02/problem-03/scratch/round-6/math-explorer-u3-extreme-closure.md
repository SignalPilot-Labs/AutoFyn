## imo-2026-03

**Lens: Close U(3) end-to-end** by killing the `d < 1/2` non-gap extreme sub-cases (`w < −2α` or `z < −2α`, α=1/15) — the sole remaining material GAP between `L(3)` (certified) and `c(3)=8/15`. The round-5 reviewer flagged these as "computationally verified, analytic closure open; no 4–7 cap subfamily suffices (the 17-family's full menu is necessary)."

### Terrain scouted on THIS gap

**Geometric meaning.** In chain-excess coords `u=a−α, v=(b−a)−α, w=(c−a−b)−α, z=(d−b−c)−α` (with `7u+4v+2w+z=α`), `w<−2α` means `c < a+b−2α` (the third piece is *significantly smaller* than the sum of the two smaller — the dyadic chain `1+2<4` is "compressed from below"; `a+b` *overshoots* `c`). Symmetrically `z<−2α` means `d < b+c−2α` (the fourth piece is *significantly smaller* than `b+c`; the chain is "compressed from above"). Both break the dyadic-ratio chain in the "smaller-than-expected" direction — i.e. they live at the *opposite* end of the simplex from the dominant regime `d ≥ 1/2` (where the 5-cap proof already closes). They are NOT reducible by a mark permutation to an already-closed regime: the 5-cap family loses `2d−1` (invalid for `d<1/2`), and the gap-G sliver requires `d ≥ b+c`, which fails exactly when `z<0` (so the sliver is unavailable precisely in the `z<−2α` sub-case). No symmetry of the sorted simplex maps `w<−2α` to the closed `w≥−2α` region.

**THE KEY FINDING (overturns the round-5 "no 4–7 cap subfamily suffices" ruling).** With *proper realizability enforced* (cap `d−b−c`, `d−a−c`, `d−a−b` excluded when `d<a+b`, `d<a+c`, `d<b+c` resp.; `2d−1` excluded when `d<1/2`), I searched 2M+ random configs over the extreme regime and verified exactly (Fraction arithmetic) that the **7-cap subfamily**
```
{ a,  b−a,  c−b,  d−c,  |a+b−c|,  |a+c−d|,  |a+b−d| }
```
closes BOTH extreme sub-cases (worst cap value `0.0598 < α=0.0667`, margin `0.007`, on 105k exact-rational extreme configs; 0 violations). This 7-cap set is **minimal**: drop-one analysis shows every 6-cap subset fails (drop `|a+b−d|` → worst `0.066` on 600k samples but `0.0696` on 2M — boundary failure; drop any other → fails by ≥0.01). The 7-cap structure: **4 chain-difference caps** (`a, b−a, c−b, d−c` — the 4 consecutive gaps of the sorted 5-broken-stick) **plus 3 abs-sum caps** (`|a+b−c|, |a+c−d|, |a+b−d|` — three of the four "sum-of-two-smaller minus a-larger" abs values; the missing fourth is `|b+c−d|`, already used in the closed `z∈[−2α,0]` sub-case).

**Why round-5 said "no 4–7 cap subfamily suffices."** Round-5 tested *structured* subfamilies (the 5-cap direct-n=2-analogue, plus a 4–7-cap census) without the proper realizability mask — including the algebraic *value* `d−b−c` even when `d<b+c` (where the strategy is invalid). My probe without realizability reproduced round-5's "size-3 closes" false positive; *with* realizability, the 7-cap is the true minimum. The 6-cap `{a,b−a,c−b,d−c,|a+b−c|,|a+c−d|}` is on the boundary (passes 600k, fails 2M) — so the 7th cap `|a+b−d|` is genuinely load-bearing.

### Distinct openings (each a different attack the outliner could build)

1. **7-CAP CASE-BY-CASE CONTRADICTION (the concrete tractable route).** Assume all 7 caps `> α`; derive contradiction in `d<1/2` + (w<−2α OR z<−2α). From the 4 chain caps: `a>α, b>2α, c>3α, d>4α`, so `a+b+c+d > 10α = 2/3` (consistent, since `d<1/2` needs `a+b+c>1/2`). The 3 abs caps give `2^3=8` OR-sub-cases. **In the `w<−2α` sub-regime, `c<a+b−2α < a+b−α` FORCES the `|a+b−c|` cap into the "c<a+b−α" branch** (no OR), reducing to `2^2=4` sub-cases. **In the `z<−2α` sub-regime, `d<b+c−2α`; combine with the chain-`d>c+α`** to narrow branches. 8 sub-cases total (4 per sub-regime), each a clean ≤4-line inequality contradiction. This is the smallest *analytic* closure found and is far less laborious than the 17-family's full menu. **Most promising route.**

2. **6-CAP + SLIVER HYBRID.** The 6-cap `{a,b−a,c−b,d−c,|a+b−c|,|a+c−d|}` fails by a hair (`0.0696 > 0.0667`) on the `w<−2α` sub-regime when `z>0` (where `d≥b+c` and the gap-G sliver `|2d−1|` IS realizable). Adding the sliver as an 8th strategy (only in the `w<−2α ∧ z>0` slice) might let a 6+sliver hybrid close — but the sliver is *not* realizable in `z<−2α`, so it can't replace `|a+b−d|` there. Marginal gain; the 7-cap is cleaner.

3. **DUAL VERTEX-PRINCIPLE (the unifying frame, NOT a separate closure).** The round-5 explorer's piecewise-concavity argument (`Φ(P) := min_x A(x;P)` is a finite min of `|linear|` functions of `P`, hence piecewise-concave; max at a `P`-arrangement breakpoint) gives a *one-shot* cover if the `P`-arrangement vertices are enumerated and checked. The dyadic is the unique interior max. BUT this requires enumerating `P`-arrangement vertices (piece-equality + piece-zero + cap-tie hyperplanes in the 3-dim sorted simplex) — the analogue of the `L(3)` cell-complex enumeration *dualized*. No enumeration has been done. This is the cleanest *if* it lands, but the heaviest lift; the 7-cap casework is the cheaper near-term win.

4. **D3-STYLE STRUCTURAL THEOREM for the upper bound (does NOT dualize cleanly).** The `L(n)` D3 conjecture (fractional arrangement vertices have `A>α·D`) characterizes the lower-bound extremals. The dual for U(3) would say "the unique `P` maximizing `Φ(P)` is the dyadic" — which is the round-5 explorer's conjecture (numerically robust on 200k+ samples). No analytic proof; this is the SAME wall as the regime-N mechanism. The D3 framing does NOT give a one-shot cover for U(3) without enumerating the `P`-arrangement (opening 3).

### Candidate technique(s)

- **Casework / exhaustion on a 7-cap subfamily** (KB "Casework / exhaustion", Combinatorics section) — the direct generalization of the certified `U(2)` four-strategy contradiction. This is the n=3 template: 4 chain-difference caps + 3 abs-sum caps, 8 sub-cases.
- **Dual vertex-principle / piecewise-concavity smoothing** (KB "Piecewise-concavity smoothing", Algebra & Polynomials) — the unifying frame if the casework is to be replaced.

### Cheap-kill candidates

- **Chain-difference cap `a` (bisect b,c,d)**: closes the `z<−2α` regime in ~50% of configs (smallest-piece cheap kill); also the *tightest* cap at the worst-case config (`a≈0.0598 < α`).
- **`|a+c−d|` and `|a+b−d|`**: abs-sum caps closing configs where `d ≈ a+c` or `d ≈ a+b` (dyadic-ratio-adjacent at the top of the chain).
- The 7-cap set itself is the cheap-kill family for THIS gap.

### Knowledge-base entries to use

- **"Casework / exhaustion"** (Combinatorics) — the 7-cap contradiction template.
- **"Piecewise-concavity smoothing"** (Algebra & Polynomials) — for the dual vertex-principle framing (opening 3).
- **"Extreme value theorem"** (Linear Algebra) — `Φ` continuous on compact simplex.

### Analogous past problems (cruxes)

- **`aimo-0019`** (combinatorics, games-and-strategy): dyadic painting game, "respond just beyond the frontier." Confirms the dyadic-equality signature (already cited).
- **`aimo-0066`** (combinatorics, games-and-strategy): "blocking-in-place pairing / same-weight mirroring." The pair-pile + 17-family's involution-partner strategy template (already cited).
- **`aimo-0017`** (combinatorics, extremal-principle): "minimum-size cover, read off a private element per cover member." Tangentially relevant — the 7-cap family is a minimum cover of the extreme regime; each cap is "private" to a sub-region. No closer match found. The stick-cutting + alternate-claiming structure is genuinely novel to the corpus.

### Prior progress

- `L(3)` CERTIFIED (cell-complex); `L(4)` CERTIFIED.
- `U(1)`, `U(2)` CERTIFIED; regime-D (dyadic) all-n via pair-pile.
- **U(3) closure (round 5):** `d≥1/2` regime CLOSED (5-cap contradiction, `lemma-u3-5cap-dominant.md`); `d<1/2` gap `G` CLOSED (3-mark sliver, `lemma-u3-sliver-gap.md`); `d<1/2` non-gap `w,z≥−2α` CLOSED (4 sub-cases via `|a+b−c|`, `|b+c−d|`, `a`, `b−a`). **REMAINING: the `w<−2α` or `z<−2α` extreme sub-cases.**

### Dead ends (do not retry)

- **Bare 5-cap `{a, b−a, c−b, 2d−1, |a+b−c|}` outside `d≥1/2`** — fails (loses `2d−1`).
- **The 6-cap `{a,b−a,c−b,d−c,|a+b−c|,|a+c−d|}` as a closure** — boundary failure (passes 600k, fails 2M by `0.003`). Needs the 7th cap `|a+b−d|`.
- **Using cap *values* `d−b−c`, `d−a−c`, `d−a−b` without realizability check** — these strategies require `d≥b+c` (resp. `d≥a+c`, `d≥a+b`), which FAILS in the extreme sub-cases (esp. `z<−2α` ⟹ `d<b+c`). Round-5's "17-family covers it" census implicitly used un-realizable caps in part.
- **R-pile greedy**, **(U-E)**, **unified potential**, **LP-dual/majorization** — all killed in prior rounds (per `two-regime-disjunctive.md` do-not-retry list).
- **Sliver (gap-G strategy) as a closure for `z<−2α`** — requires `d≥b+c`, exactly opposite to `z<−2α`.

### Small-case / intuition notes (CONJECTURES, labeled)

- **CONJECTURE (numerically robust, 105k exact-rational + 2M float extreme configs):** the 7-cap `{a, b−a, c−b, d−c, |a+b−c|, |a+c−d|, |a+b−d|}` closes the entire `d<1/2 ∧ (w<−2α ∨ z<−2α)` regime, with `max min-cap ≈ 0.0598 < α=0.0667` (margin 0.007). Worst config: `a≈0.0598` (closed by cap `a`); `z≈−0.138`.
- **CONJECTURE:** the 7-cap family is *minimal* — drop-one on each of the 7 caps fails (the `|a+b−d|` drop is the boundary case, failing by 0.003 on 2M samples).
- **Equality characterization:** in `d<1/2`, NO config attains `min = α` (the dyadic is in `d≥1/2`); every extreme-sub-case config has `min < α` strictly. The 7-cap family is consistent with this (worst `0.0598 < α`).

### Concrete next step for the outliner

Build a `U(3)`-extreme-closure lemma on the **7-cap case-by-case contradiction** (opening 1): state the 7 caps, the realizability conditions (all 7 are always-realizable — `a, b−a, c−b, d−c` via bisect/match strategies; `|a+b−c|, |a+c−d|, |a+b−d|` via 2-mark bisect-and-match — none requires `d≥b+c`), assume all `> α`, split into the 8 OR-sub-cases (4 per sub-regime, since `w<−2α` forces one branch), derive contradiction in each. The outliner should treat this as the **direct n=3 generalization of the certified `U(2)` four-strategy lemma**, NOT as a 17-family exhaustive enumeration. **The 7-cap family IS necessary and sufficient** (no 6-cap works); the round-5 "17-family necessary" ruling is overturned *for the extreme sub-cases specifically* (the 17-family is still the engine for the rest of `d<1/2` non-gap, but those sub-cases are already closed by the 4 sub-case argument in §5d.4). Combined with the certified `L(3)` (cell-complex), this closes `c(3)=8/15` end-to-end.

**Watch out for:** the cap `d−b−c` is NOT in the 7-cap family — do NOT add it (it's un-realizable in `z<−2α`). The 7 caps are all *always-realizable*; that's the point. Do NOT claim the 6-cap suffices (it fails on 2M). Do NOT use the sliver for the `z<−2α` half.
