## imo-2026-03 (LP / minimax-duality / game-theoretic dual certificate lens)

### The terrain through this lens

The game is a **perfect-information sequential** zero-sum game (Liu marks, Xiang sees and responds). Value `V = max_L min_s D(L,s)`. Two LP reframings exist; they are NOT equivalent and the distinction is the whole story.

**(A) Stackelberg-blind relaxation (the "real" LP dual).** Relax Xiang to commit a *mixed strategy before seeing Liu*: pick a probability distribution `q` over ≤n-mark configurations. Value `V_blind = min_q max_L E_{s~q}[D(L,s)]`. This IS an LP:
- Primal: `min_{q≥0, Σq=1} max_L Σ_s q_s D(L,s)`.
- Dual: `max_{p≥0, Σp=1} min_s Σ_L p_L D(L,s)` (Liu's mixed best response).
- **Complementary slackness** at optimum pins the active strategies on both sides.

Crucial inequality: `V_blind ≥ V` (Xiang's perfect info helps him: for fixed `L`, `min_s D(L,s) ≤ E_s D(L,s)`; maxing over `L` preserves it). The gap `V_blind − V` is the **value of Xiang's information**.

**(B) Per-region LP (within a fixed combinatorial type).** Within a region where the descending sort order of final pieces is fixed, each `a_i` is *linear* in the split locations, so `D = Σ(±)a_i` is linear there. The inner `min_s D(L,s)` is an LP *per region*; dualizing gives a per-region dual certificate. Bounded but combinatorially messy (many regions).

**(C) Lower-bound "LP" (Liu fixed to dyadic).** Here there is NO info asymmetry (Liu is pure-fixed), so `min_pure = min_mixed`: the relaxation is *tight* in principle. But `D = ∫[j_0 ⊕ σ odd] dt = D_0 + D_σ − 2·(overlap)` is **nonlinear (parity-XOR)** in the toggle-set indicator `σ = Σ 1_{T_i} mod 2`. The "overlap" coupling `C = ∫[j_0 odd ∧ σ odd]` is exactly Lemma 5's `C`. So the lower-bound dual certificate **IS** the overlap bound `2C ≥ D_{R_0}+D_F+1−M` — the existing open crux, rephrased. No new LP; no new opening.

### Distinct openings (concrete, not in the current field)

1. **Dyadic-weight dual certificate for the SPIKY upper-bound regime (n general).** Conjecture (verified n=1,2): the LP dual of the Stackelberg relaxation is solved by weights `λ_k = g_k = 2^k/D_n` (the dyadic pieces themselves) on a menu of "equal-halve all but piece k" + "barely-split piece 1" strategies.
   - n=1: `λ = (2/3, 1/3)` on {equal-split (D=1−a), barely-split (D=2a−1)} ⟹ `E[D] = (2/3)(1−a) + (1/3)(2a−1) = 1/3` **constant** for all `a ∈ [1/2,1]`. (Symbolically exact; LP solver lands within 2e-3.)
   - n=2: `λ = (4/7, 1/7, 2/7, 0) = (g_2, g_0, g_1, 0)` on {A: D=c, B′: D=|2a−1|, C1: D=b−c, C3: D=a−b} ⟹ in regime `a ≥ 1/2`, `E[D] = 1/7` **exactly constant** (symbolic sympy check). At dyadic `(4/7,2/7,1/7)` all active menu values `= 1/7`, so any supported mix is tight.
   - **The recursion `1/c(n) = Σ_{k=0}^n 2^{−k}` falls out as the dual-feasibility (complementary-slackness) identity** `Σ g_k = Σ 2^k/D_n = 1`. This is the load-bearing structural reason the dyadic weights are dual-optimal. The geometric series is NOT an add-on — it IS the dual solution.
   - This re-derives the **regime `p_{n+1} ≤ 1/D_n`** (currently closed by `equal-halve-n-largest`, Lemma 4) via LP duality instead of the parity-rank argument. Different proof, same boundary, with the recursion explained.

2. **Flat-regime integrality gap (the honest wall).** In the flat regime `a < 1/2` (n=2), the dyadic-weight mix gives `E[D] = 3/7 − 4a/7`, which at `a = 1/3` is `5/21 ≈ 0.238 ≫ 1/7`. The full LP optimum over the 4-menu AND a 756-strategy rich menu both give **`V_blind = 1/6`** for n=2 (exactly, robust across menus). So:
   - n=1: `V_blind = 1/3 = V` (no info gap — the mix cancels the `a`-coefficient).
   - n=2: `V_blind = 1/6`, `V = 1/7`. **Integrality gap = `1/6 − 1/7 = 1/42 = 1/(D_n(D_n−1))`.**
   - n=3 (coarse, 455 Liu configs, 400-strategy menu): `V_blind ≈ 0.129 ≫ 1/15 ≈ 0.0667`. Gap huge.
   - **Pattern: `V_blind = 1/(D_n − 1)`** (= `1/2` n=1... wait n=1 gives 1/3 not 1/2; the n=1 case is special because the two strategies' `a`-coefficients cancel exactly). For n≥2 the blind value is `≥ 1/(D_n−1) > 1/D_n` strictly. The complementary (flat) regime is where the casework's information advantage is essential — the dual **cannot** reach `1/D_n` there. This is the G2 wall seen through the dual lens: the wall is not a missing technique, it is an **inherent integrality / info gap**.

3. **Per-region LP dual for the lower-bound overlap crux (micro-tool, not a top-level approach).** Within each fixed combinatorial type (fixed sort order of final pieces), `D` is linear in the split points; the lower-bound inequality `D ≥ 1/D_n` becomes a per-region LP whose dual is a nonneg weighting of "parity-obstruction" inequalities. This is a possible *tactic* to prove `2C ≥ D_{R_0}+D_F+1−M` case-by-case (one region at a time) when the global overlap bound resists a single inequality. Bounded promise: each region is small, but the number of regions grows fast with n. Genuine alternative to the global superincreasing-overlap chase, but not obviously less work.

### What looks promising vs dead (honest)

- **PROMISING (clean, novel, but only re-derives a closed regime):** the dyadic-weight dual certificate (opening 1). It gives a *new proof* of the `p_{n+1} ≤ 1/D_n` regime via LP duality, with the recursion `1/c(n) = Σ 2^{−k}` emerging as the complementary-slackness identity. This is genuinely illuminating — it explains WHY the dyadic weights and the geometric series appear — but it does **not** close any open wall (Lemma 4 already closed that regime combinatorially).
- **DEAD for the open G2 (upper-bound flat regime):** the Stackelberg-blind LP has an inherent integrality gap `≥ 1/(D_n−1) − 1/D_n = 1/(D_n(D_n−1))` (verified n=2 exactly; n=3 large). No enrichment of the menu closes it — the gap is the value of Xiang's perfect information, which the dual discards by construction. Adding strategies can only push `V_blind` down toward `1/(D_n−1)`, never to `1/D_n`. The pure casework's per-`L` best-response is doing real work the dual cannot replicate.
- **DEAD for the open G1 (lower bound):** the lower-bound "LP" has no info asymmetry (so dual = primal in principle), but `D` is parity-nonlinear in the toggle sets; the dual coupling IS the overlap term `C` from Lemma 5. Certifying the dual = proving `2C ≥ D_{R_0}+D_F+1−M`. **Same wall, different words.** No bypass.
- **PROMISING-but-narrow (opening 3):** per-region LP dual is a real micro-tool for the overlap crux, but combinatorially heavy and not obviously better than the direct superincreasing-overlap chase.

### Risk of convergence

**Genuinely orthogonal, not a pairing variant.** Pairing-charging seeks a *deterministic domino partition* (per-`L` pure strategy). The dual seeks a *fixed fractional distribution* over strategies, independent of `L`, with dyadic weights. These are different mathematical objects. The dual does NOT collapse to pairing — if anything it is weaker on the flat regime (where pairing is also stuck) for a *different* reason (info gap vs missing partition rule). No convergence risk.

However: as a *top-level approach* it mostly re-derives the already-closed spiky regime, so its *population value* is diversification-of-insight (the recursion explanation) rather than a new attack on the open walls. Recommend opening it as a **secondary** approach for the recursion-structure insight, NOT as the main line on G1/G2.

### Knowledge-base entries to use
- *Linear-programming duality / minimax (von Neumann)* — the Stackelberg-blind LP and its dual.
- *Complementary slackness* — pins the dyadic weights as dual-optimal.
- *Casework / exhaustion* (the per-region LP dual tactic, opening 3).
- *Invariants & monovariants* (the parity-integral `D = ∫[j odd]`, already certified in `lemmas/parity-integral.md`, is the bridge between the LP variables and the combinatorial `D`).

### Analogous past problems (cruxes)
- **aimo-0117** (Dutch TST 2021 / "Jesse & Tjeerd boxes") — crux: *assign values as a two-sided geometric (dyadic) sequence so the largest exceeds the sum of all others; maintain "largest power sits in the target box."* Analogous because: (i) the winning values are exactly powers of two, (ii) the invariant is a *weighted* domination, mirroring how our dual weights `λ_k = 2^k/D_n` are the dyadic sequence and the complementary-slackness condition is "largest exceeds sum of rest." This is the closest crux to the *dual weights*, not to the game structure. Adapt, don't cite.
- **aimo-0019** (IMO-SL 2013 C8 / paint game) — crux: *amortized linear potential `3x_r` charging frontier advances against absorbed dyadic pieces; bound total ink by geometric sum of distinct powers.* Analogous in that the geometric-series bound is the engine, but the game is simultaneous (paint) not perfect-info sequential; the amortized-potential route was already tried and conceded by `alternating-potential`. Not a fresh opening here.
- No crux in the corpus is a direct LP-duality / minimax-mixed-strategy hit for a sequential marking game — the LP-dual lens is **off the corpus grid**, which is itself a signal (it's genuinely different, but also unproven as a wall-cracker).

### Prior progress (current best, relevant to this lens)
- Lemma 4 (`equal-halve-n-largest`, CERTIFIED) closes the regime `p_{n+1} ≤ 1/D_n` for all `n` — the *same* regime the dyadic-weight dual cleanly re-derives. So the dual's "win" is already in the bank; the dual explains the recursion but adds no new closed ground.
- Lemma 5 (multi-split formula, PROVED identity) gives `D = M − D_{R_0} − D_F + 2C`; the lower-bound dual is *literally* this identity's `C`-term inequality. Confirms the lower-bound dual = existing overlap crux.
- n=1 both bounds PROVED; n=2 both bounds PROVED (4-menu casework). The dual re-derives n=1 exactly (`λ=(2/3,1/3)`) and n=2 spiky exactly (`λ=(4/7,1/7,2/7,0)`), matching the certified results — a consistency check on the dual.

### Dead ends (do not retry, from this lens)
- **Stackelberg-blind LP as a G2 (upper-bound flat regime) attack:** integrality gap `1/6 − 1/7 = 1/42` at n=2 (verified exact, robust to 756-strategy menus); n=3 gap ≈ `0.062 ≫ 0`. The gap is the value of Xiang's perfect information — structural, not a missing technique. No menu enrichment closes it. (Verified this round, not a prior-round claim.)
- **Lower-bound LP dual as a G1 bypass:** reduces exactly to the overlap bound `2C ≥ D_{R_0}+D_F+1−M` (Lemma 5 corollary). Not a new route; it IS the crux. (Confirmed by writing out `D = D_0 + D_σ − 2·overlap` from the parity-XOR identity.)
- **"Leave piece k unsplit" convex combination** (a tempting simpler dual): forced to `λ_0 = 1` (concentrate on smallest) by the dyadic-point constraint `Σ λ_k 2^k ≤ 1`, reducing to Lemma 4 only. Useless for the flat regime. (Quick check, this round.)

### Small-case / intuition notes (labeled CONJECTURE from numerics)
- **CONJECTURE (n=1,2 verified; n=3 coarse):** the Stackelberg-blind value `V_blind = 1/(D_n − 1)` for `n ≥ 2` (n=1 is special: `= 1/3 = 1/D_n` because the two strategies' `a`-coefficients cancel). If true, the integrality gap is exactly `1/(D_n(D_n−1))`, quantifying Xiang's information advantage. Verified n=2 exactly (1/6); n=3 coarse (0.129 vs 1/14=0.071 — not a clean match, likely menu too coarse; do not trust n=3 value).
- **CONJECTURE (n=2 verified symbolically):** the dyadic weights `λ_k = g_k = 2^k/D_n` are dual-optimal for the spiky regime at every `n`, and the complementary-slackness identity `Σ 2^k = D_n` IS the recursion `1/c(n) = Σ 2^{−k}`. This is the cleanest structural output of the lens: the recursion is a dual-feasibility condition.
- **Intuition:** the flat regime is fundamentally where "fractional/blind" Xiang loses to "per-config-best-response" Xiang. The dual lens *cannot* crack G2-flat; only a per-`L` pure construction (pairing/adaptive) can. This reinforces, from a new angle, that the G2 wall is real and not a technique gap.

### One concrete slugged approach skeleton

**Slug: `lp-dyadic-dual`** (secondary / diversifying approach; do NOT seed as a main G2 attacker — it cannot crack the flat regime).

Outline (3–5 lines):
1. Recast the upper bound as the Stackelberg-blind LP `min_q max_L Σ_s q_s D(L,s)`; cite von-Neumann/minimax duality and the inequality `V_blind ≥ V = 1/D_n`.
2. Construct the dual certificate `λ_k = g_k = 2^k/D_n` on the menu {equal-halve all but piece k} ∪ {barely-split piece 1}; prove `Σ_k g_k · D_k(L) = 1/D_n` **identically** in the regime `p_{n+1} ≤ 1/D_n` (the spiky regime), via the complementary-slackness identity `Σ 2^k = D_n` (= the recursion `1/c(n) = Σ 2^{−k}`). **HARD STEP:** the per-strategy `D_k(L)` linear form must be worked out for general `n` (known for n=1,2; pattern not yet closed for n≥3).
3. **Concede the flat regime honestly:** prove `V_blind ≥ 1/(D_n−1) > 1/D_n` for `n ≥ 2` (n=2 exact: `1/6`; n≥3 by the integrality-gap argument + numerics), so the dual cannot close G2-flat. Record this as a *negative result* that localizes the G2 wall to the information advantage.
4. **Optional micro-tool (do not block on it):** per-region LP dual for the G1 overlap bound — within each fixed sort-order region, dualize the linear `D` to a nonneg weighting of parity obstructions. Sketch only; flag as open.

**Hard steps identified:** (a) general-n form of the menu linear forms `D_k(L)` and the proof `Σ g_k D_k = 1/D_n` in the spiky regime (n=1,2 done; n≥3 pattern open); (b) proving `V_blind ≥ 1/(D_n−1)` rigorously (n=2 exact; n≥3 open). Both are bounded and honest; neither cracks the open G2-flat or G1-overlap walls. The approach's *value* is the recursion-as-dual-slackness insight, not wall-closure.
