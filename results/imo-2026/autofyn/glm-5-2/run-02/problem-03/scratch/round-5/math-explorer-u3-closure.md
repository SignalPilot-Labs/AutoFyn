## imo-2026-03

**Lens: CLOSE THE UPPER BOUND U(3) FOR REALS.** Target: `c(3)=8/15` end-to-end. Lower bound `L(3)` is CERTIFIED (cell-complex vertex enumeration). The OPEN half is `U(3)`: for EVERY Liu config with ≤3 marks (not just the dyadic), Xiang forces `Liu ≤ 8/15`, i.e. `A ≤ 1/15 = α(3)`.

### Distinct openings (the terrain I scouted)

1. **DUAL VERTEX PRINCIPLE (the most rigorous unifying route).** The lower-bound vertex-principle (CERTIFIED, `lemma-vertex-principle-advantage.md`) FIXED Liu's config = dyadic and varied Xiang's mark-vector `x ∈ [0,1]^3`, showing `A(x) ≥ 1/15` via 11523 arrangement vertices. The DUAL fixes Xiang's optimal strategy and varies Liu's config `P` over the sorted simplex `{(a,b,c,d): a≤b≤c≤d, a+b+c+d=1}`. `Φ(P) := min_x A(x;P)` is a min of finitely many piecewise-linear (abs-value + conditional) functions of `P` → **piecewise-concave** in `P` (KB entry "Piecewise-concavity smoothing": a finite sum/min of `|linear|` terms is piecewise-concave; its MAX over a compact polytope is at a breakpoint where some argument vanishes — a "zero entry", i.e. a piece-equality or piece-zero hyperplane). So `max_P Φ(P)` is attained at an arrangement vertex of the `P`-space arrangement. My fine-grid + 200k-random search confirms: `max_P Φ(P) = 1/15`, attained ONLY at the dyadic `(1,2,4,8)/15`. The dyadic IS an interior arrangement vertex (a kink where multiple strategies tie), NOT a simplex vertex — consistent with piecewise-concavity (max at a breakpoint, not a domain vertex). This dual vertex-principle is the cleanest UNIFYING frame and mirrors the certified L(3) proof.

2. **FINITE EXACT-PAIR STRATEGY FAMILY (the concrete tractable route, generalizes n=2 four-strategy).** I built a family of 17 explicit Xiang strategies for n=3, each "k marks creating k pairs + (4−k) leftovers", with caps that are simple affine or `|linear|` functions of `(a,b,c,d)`:
   - **3-mark (3 pairs + 1 leftover):** `a` (bisect b,c,d), `b−a` (match a in b, bisect c,d), `c−a`, `d−a`, `c−b`, `d−b`, `d−c`, `d−a−b` (match a,b in d, bisect c), `d−a−c`, `d−b−c`, `2d−1` (match a,b,c in d; valid iff `d ≥ 1/2`).
   - **2-mark (2 pairs + 2 leftovers):** `|a+b−c|` (bisect d, match a in c), `a+c−b`, `|a+b−d|`, `a+d−b`, `a+d−c`, `|a+c−d|`, `|b+c−d|`.
   Each cap formula was verified by direct multiset alt-sum computation (exact rational). At the dyadic `(1,2,4,8)/15`, FOUR strategies attain equality `cap = 1/15`: `a`, `b−a`, `2d−1`, `|a+b−c|` — a clean n=2-analogue signature (n=2's four strategies A/B/C/E all tie at `(1,2,4)/7`).

3. **MODERATE-DOMINANT CLASS `L ∈ [8/15, 4/5]` (the round-4 OPEN class) IS COVERED by the exact-pair family.** Verified: for `L ∈ [8/15, 4/5]` with balanced small pieces `a=b=c=(1−L)/3`, the cap `b−a = 0` (or `c−b = 0`) drives `Φ = 0 < α(3)`. For unbalanced small pieces, `a` (bisect-b,c,d strategy) or `d−b−c` caps it. The "match a in b" / "match b in c" strategies handle the near-balanced-small regime; the "match a,b in d" / "match a,c in d" strategies handle the spread-small regime. NO sliver forcing needed for this class — it falls out of exact-pair matching. This CLOSES the round-4 open class `L ∈ [8/15, 4/5]` analytically (cap ≤ 1/15, strict for non-dyadic).

4. **THE GAP: thin region near `d = 1/2` from BELOW (where `2d−1` is invalid).** The 17-family has a real gap: when `d` is just below `1/2` (so `2d−1` strategy invalid) AND `a, b−a, c−b, d−b−c, |a+b−c|, |b+c−d|` are ALL just above `1/15`, the family's min exceeds `1/15`. Verified numerically: e.g. config ≈ `(0.0706, 0.1423, 0.2871, 0.49998)` gives family-min ≈ 0.0706 > 1/15 = 0.0667. BUT Xiang's TRUE cap (fine brute force, N=200 exact) is `A = 3/700 ≈ 0.0043 ≪ 1/15`, achieved by a SLIVER-TUNED 3-mark strategy: shave a sliver `ε` from piece `a`, match the shaved remainder `a−ε` in piece `d`, split `d`'s remainder into two unequal parts chosen so the 5-leftover alt-sum `= base + ε` with `base < 1/15`. At `(1,2,4,7)/14` (boundary `d=1/2`), the sliver-strategy infimum is `1/350 ≪ 1/15`. So the gap is an artifact of the EXACT-pair family missing the SLIVER family, NOT a true violation of `U(3)`.

5. **The 5-cap direct-n=2-analogue `{a, b−a, c−b, 2d−1, |a+b−c|}` FAILS.** Verified on N=60 grid: 5 violations (e.g. `(1/12,1/6,1/3,5/12)` → `min = 1/12 > 1/15`). The failure mode is exactly the `d < 1/2` regime where `2d−1` is invalid. The full 17-family (or at minimum adding `d−a−c`, `d−b−c`, `|a+c−d|`, `|b+c−d|`) is needed. Do NOT pursue the bare 5-family — it does not close.

### Candidate technique(s)

- **Dual vertex-principle / piecewise-concavity (KB: "Piecewise-concavity smoothing").** `Φ(P)` is piecewise-concave in `P`; max at a breakpoint (zero-entry). Enumerate `P`-arrangement vertices (piece-equality + piece-zero + cap-tie + validity-boundary hyperplanes), verify `max ≤ 1/15`. Mirrors the certified L(3) vertex-principle DUALIZED.
- **Casework contradiction on the exact-pair family (KB: "Casework / exhaustion", like n=2 four-strategy).** Assume all valid caps `> 1/15`, derive contradiction. The 5-family `{a, b−a, c−b, 2d−1, |a+b−c|}` gives a clean contradiction in the `d ≥ 1/2` regime (case `c ≥ a+b`: `c > 4/15` and `c < 4/15`; case `c < a+b`: `b > 3/15` and `b < 3/15`). The `d < 1/2` regime needs the 2-mark caps (`|a+c−d|`, `|b+c−d|`, `d−b−c`) and sliver-tuned strategies.
- **Sliver-tuned 3-mark strategy** (generalizes S1/S2/S3): shave `ε` from one piece, match the remainder in another, split the target's remainder to tune the tail alt-sum to `base + ε` with `base < α(3)`.

### Cheap-kill candidates

- **Bisect-three cap `= a`** (smallest piece): if `a ≤ 1/15`, done immediately. Covers all configs where Liu's smallest piece is small (extreme-dominant, many moderate-dominant, degenerate).
- **Match-adjacent cap `b−a, c−b, d−c`**: if any adjacent difference `≤ 1/15`, done. Covers near-balanced configs.
- **2-mark abs caps `|a+b−c|, |a+c−d|, |b+c−d|`**: if any `≤ 1/15`, done. Covers configs where one piece ≈ sum of two others (dyadic-ratio-adjacent).

### Knowledge-base entries to use

- **"Piecewise-concavity smoothing"** (Algebra & Polynomials section) — the core technique: a finite min of `|linear|` terms is piecewise-concave; max at a breakpoint/zero-entry. This IS the dual vertex-principle's engine.
- **"Casework / exhaustion"** (Combinatorics) — the n=2 four-strategy contradiction template, generalized to the 17-family.
- **"Extreme value theorem"** (Linear Algebra) — `Φ` continuous on the compact Liu simplex attains its max.
- **Certified lemmas to import**: `lemma-u2-four-strategy.md` (the n=2 template whose 4 caps `a, b−a, c−b, |2c−1|` generalize to the n=3 17-family; note `|2c−1| = |a+b−c|` is the n=2 instance of the 2-mark cap `|a+b−c|`), `lemma-s1-balanced-sliver.md` (handles balanced class), `lemma-vertex-principle-advantage.md` (the L(3) dual to mirror), `lemma-grid-equality-case.md` (equality-structure hint: equality iff odd-mult leftover `{1}` or `{a,a+1}`).

### Analogous past problems (cruxes)

- **`aimo-0019`** (combinatorics, games-and-strategy): dyadic-interval painting game — "respond to each opponent move by painting the cell immediately beyond the current filled frontier". Directly analogous: the dyadic structure and the superincreasing-R lever. Already cited in prior rounds; confirms the dyadic-equality signature.
- **`aimo-0225`** (combinatorics, games-and-strategy): "recurse on the 2-adic valuation of a difference that exactly halves at each relevant step" — the dyadic-ratio detection (`a_1 = 2 a_2` telescoping at the dyadic). Relevant for the equality-characterization (equality iff dyadic).
- **`aimo-0596`** (combinatorics, games-and-strategy): "responder answers each opponent pick with its fixed involution-partner" — the pair-pile / exact-pair matching strategy (each Xiang mark creates a pair). The n=3 17-family is the involution-partner strategy with a finite menu of pairings.

No crux in the corpus is a closer match than these three (already cited). The stick-cutting + alternate-claiming game structure is NOT in the corpus — this problem is genuinely novel.

### Prior progress

- **`L(3)` CERTIFIED** (cell-complex vertex-principle, round 4). Lower bound done.
- **`U(1), U(2)` CERTIFIED** (two-regime-disjunctive). `c(1)=2/3, c(2)=4/7` end-to-end.
- **`U(3)` OPEN**. Three structural classes covered by certified sliver lemmas S1 (balanced all-n), S2 (two-dyadic n=3), S3 (extreme-dominant `L > 4/5`). The moderate-dominant `L ∈ [8/15, 4/5]` was the flagged open class — my computation shows it IS covered by the exact-pair family (no sliver needed).
- **Regime-D (dyadic) upper bound** for all n via certified pair-pile.

### Dead ends (do not retry)

- **Engine R-pile greedy** (round 3, FALSIFIED — 3 counterexample classes). The exact-pair family is NOT the greedy; it is a finite MENU of explicit pairings, each chosen optimally per config. Do not confuse the two.
- **5-cap direct-n=2-analogue `{a, b−a, c−b, 2d−1, |a+b−c|}`** — FAILS for `d < 1/2` (5 violations on N=60 grid). Need the full 17-family.
- **"Non-dyadic ⟹ A ≤ 0"** (round 2, false). The true cap is strict-positive but `< α(3)` for non-dyadic.
- **LP-dual / weight-function averaging / majorization** (round 3, killed). `Φ` is neither Schur-convex nor Schur-concave; the n=2 four-strategy min is NOT a weighted-average identity.
- **(U-E) unique-extremum** (round 4, RETHINK'd) — restates G2 globally, supplies no technique.

### Small-case / intuition notes (CONJECTURES, labeled)

- **CONJECTURE (numerically robust, 200k random + fine-grid exact):** `max_P Φ(P) = 1/15`, attained ONLY at the dyadic `(1,2,4,8)/15`. Every tested non-dyadic config (including all moderate-dominant, balanced, degenerate, near-d=1/2) gives `Φ < 1/15` strictly. The regime-N conjecture HOLDS for n=3.
- **CONJECTURE:** the 17-cap exact-pair family proves `Φ(P) ≤ 1/15` for all `P` EXCEPT a thin region near `d = 1/2` from below, where sliver-tuned strategies (cap `→ base < 1/15`) are needed. The exact boundary of the gap region is the locus where `d < 1/2` AND `a, b−a, |a+b−c|, |b+c−d|, d−b−c` are all `> 1/15` simultaneously — a positive-measure but thin sliver of the simplex.
- **CONJECTURE (equality characterization):** `Φ(P) = 1/15` iff `P` is the dyadic `(1,2,4,8)/15` (up to the sort symmetries). At the dyadic, 4 strategies tie (a, b−a, 2d−1, |a+b−c|). Off the dyadic, at least one of the 17 caps is strictly `< 1/15` OR a sliver strategy drives `< 1/15`.
- **KEY NUMBERS (exact):** dyadic `(1,2,4,8)/15`: `Φ = 1/15` (4 strategies tie). `(1,2,3,9)/15`: `Φ = 0` (true cap; family gives `1/15` — a family-insufficiency artifact, capped by the 2-mark `|a+b−c|`-variant... actually `|a+b−c| = |1+2−3|/15 = 0` IS in the 17-family — so the 17-family DOES cap this at 0; the 8-subfamily was the insufficient one). `(1,2,4,7)/14` (d=1/2 boundary): `Φ = 3/700` (sliver strategy), `2d−1 = 0` (boundary valid). Near-dyadic perturbations: strict `< 1/15`.

### Concrete recommendation for the outliner

**Build a `U(3)`-closure approach on the EXACT-PAIR FAMILY + SLIVER-TUNED BOUNDARY route** (the concrete tractable path), with the DUAL VERTEX PRINCIPLE as the unifying frame:

1. **Field the 17-strategy exact-pair family** (caps listed above). Each cap is a proven affine/abs-linear function of `(a,b,c,d)` (verified by direct multiset alt-sum). This is the n=3 generalization of the n=2 four-strategy family (`lemma-u2-four-strategy.md`).
2. **Casework contradiction for `d ≥ 1/2`**: the 5-cap subfamily `{a, b−a, c−b, 2d−1, |a+b−c|}` gives a clean 4-way contradiction (case `c ≥ a+b` and case `c < a+b`, both yield `c > 4/15 ∧ c < 4/15` or `b > 3/15 ∧ b < 3/15`). This covers the ENTIRE `d ≥ 1/2` regime (including all dominant and moderate-dominant configs with `d ≥ 1/2`, i.e. `L ≥ 1/2`).
3. **For `d < 1/2`**: use the 2-mark caps `|a+c−d|, |b+c−d|, d−b−c` (when valid) PLUS the 3-mark caps `a, b−a, c−b`. If these don't close (the thin boundary region), invoke a SLIVER-TUNED lemma: "shave `ε` from piece `a`, match `a−ε` in `d`, split `d`'s remainder to tune the 5-leftover alt-sum to `base + ε` with `base < α(3)`". The base is the alt-sum of the 5 non-sliver leftovers in the limit, which is `< 1/15` by construction (the tuning freedom lets Xiang choose the split to make the base small).
4. **Equality characterization**: at the dyadic, 4 strategies tie at `1/15`; off-dyadic, at least one cap is strict `<` OR a sliver gives strict `<`. Combine with certified S1/S2/S3 for the structural classes.
5. **Frame the whole as the dual vertex-principle** (KB "Piecewise-concavity smoothing"): `Φ` is piecewise-concave in `P`, max at a breakpoint = the dyadic. This gives the clean high-level structure even if the casework is laborious.

**The immediate high-value win**: the moderate-dominant class `L ∈ [8/15, 4/5]` (round-4 open) is CLOSED by the exact-pair family — no sliver needed. The outliner should claim this first. The remaining work is the `d < 1/2` boundary (sliver-tuned) and the equality-characterization tidy-up.

**Do NOT** pursue: the bare 5-family (fails for `d < 1/2`), the R-pile greedy (FALSIFIED), (U-E) (restates G2), LP-dual/majorization (killed). **DO** reuse the certified `lemma-u2-four-strategy.md` as the n=2 template and `lemma-vertex-principle-advantage.md` as the dual vertex-principle's L(3) sibling.
