# math-explorer (HIGH-n COMPUTATION + CRUX-CORPUS MINING) — `imo-2026-03`, round 4

Conjecture: `c(n) = 2^n/D(n)`, `D(n) = 2^{n+1}−1` (Mersenne), `α(n) = 1/D(n)`. Liu plays the level-`n` dyadic `(2^n, 2^{n−1}, …, 1)/D(n)`. `Liu = (1+A)/2`, `A = Σ(−1)^{i+1} p_i`. The two open gaps: **G1** (Liu's lower bound `A ≥ α(n)` over reals, only n=1,2 proven) and **G2** (Xiang's upper bound `A < α(n)` for non-dyadic Liu configs, only n=1,2 proven). This report is the empirical + corpus backbone for the field.

---

## A1. High-n verification table

Exact grid enumeration (`fractions.Fraction`, marks at multiples of `1/D(n)`) — this is the regime where the **integer-grid parity theorem (Lemma R2)** ALREADY PROVES `A ≥ α(n)` for all `n`; the computation confirms the bound is *tight* and extracts minimizers. For n=6,7,8 the grid is too large to enumerate exactly (`C(120,6) ≈ 3.7e10` for n=6), so the grid case is covered by the theorem and I use **random-real search + Nelder-Mead local optimization + the proven pair-pile/mirror constructions** instead.

| n | D(n) | α(n) | grid min A (exact) | # grid minimizer configs | # distinct minimizer multisets | random-real min A (150k–300k) | local-opt min A (Nelder-Mead, 40 starts) | pair-pile A (proven) | mirror A | conjecture `min A = α(n)` over reals |
|---|---|---|---|---|---|---|---|---|---|---|
| 3 | 15 | 1/15 | **1/15** (exact, 165 configs) | 22 | 2 (≤n marks: 46) | 0.066667 | 0.066667 | 1/15 | 1/15 | holds (n=1 real PROVEN) |
| 4 | 31 | 1/31 | **1/31** (exact, 14950 configs) | 184 | 7 (≤n: many) | 0.032258 | 0.032258 | 1/31 | 1/31 | holds (conjectural) |
| 5 | 63 | 1/63 | **1/63** (exact, 4.2M configs, 5.8s) | 2218 | 34 (≤n: 46) | 0.015873 | 0.015873 | 1/63 | 1/63 | holds (conjectural) |
| 6 | 127 | 1/127 | (grid proven by R2; too large to enumerate) | — | — | 0.017998 | **0.00787406** (≈ α) | 1/127 | 1/127 | holds (conjectural) |
| 7 | 255 | 1/255 | (grid proven by R2) | — | — | 0.015386 | 0.004049 | 1/255 | 1/255 | holds (conjectural) |
| 8 | 511 | 1/511 | (grid proven by R2) | — | — | 0.015805 | 0.003260 | 1/511 | 1/511 | holds (conjectural) |

**Verified:** (a) grid `min A = α(n)` exactly for n=3,4,5 (matches the R2 theorem's equality case); (b) the **pair-pile** (uses n−1 marks for n≥2) and the **mirror config** (uses n marks, Xiang at `1−l_j`) both give `A = α(n)` EXACTLY for all n=3..8 (rational-exact + float-confirmed) — these are the proven upper-bound constructions; (c) random-real + local-optimization search found **NO sub-`α(n)` config** for any n=3..8 over ~150k–300k samples each (the n=6 local-opt converged to ≈α(6), essentially re-finding the pair-pile). The random mins for n=6,7,8 sit well above α(n) simply because random marks almost never hit the dyadic-positioned pair-pile/mirror — they are upper bounds on the random-search min, NOT evidence against the conjecture.

**Verdict (verified vs plausible):** the upper bound `min_Xiang A ≤ α(n)` is PROVEN for all n (pair-pile + mirror, certified lemmas, re-confirmed here for n=3..8). The lower bound `min_Xiang A ≥ α(n)` over reals is PROVEN for n=1, CONJECTURAL for n≥2 (grid-only for all n via R2; real case open). The high-n random search is consistent with the conjecture but is NOT a proof — a sub-α real config could exist between sample points. Label the n≥2 real lower bound **CONJECTURAL**.

---

## A2. Extremal-config structure (the critical structural finding)

This is the most important new structural result. I extracted every minimizer piece-multiset for n=3,4,5 (with ≤n marks allowed, since Xiang may use fewer).

**For n=5 (clearest, 46 distinct minimizer multisets over 3046 configs):** the minimizers split cleanly into two structural families:

**Family 1 — odd piece-count (`2n+1` pieces, all `n` marks used):** ALL members have **exactly one odd-multiplicity value, and that value is `1`** (= `α(n)` in scaled units). The mirror config `{16,16,8,8,4,4,2,2,1,1,1}` is the most numerous (628 configs), but there are 33 other distinct multisets in this family — e.g. `{16,16,6,6,4,4,3,3,2,2,1}`, `{14,14,8,8,4,4,3,3,2,2,1}`, etc. — all sharing the invariant: pair up every piece except a single leftover of value 1. This is exactly the **grid-parity theorem's equality case**: `A·D(n)` is a non-negative odd integer ≥ 1, and the minimum `1` is attained iff the lone unpaired piece has value exactly 1.

**Family 2 — even piece-count (`2n` pieces, `n−1` marks used):** ALL members have **exactly two odd-multiplicity values, and they are CONSECUTIVE integers `{a, a+1}` with `a = 2^j`** for some `j ∈ {0,1,…,n−1}`. The pair-pile `{16,16,8,8,4,4,3,2,1,1}` (odd-mult `{2,3}`) is the canonical `a=2` case; the other even-count minimizers use `{1,2}`, `{4,5}`, `{8,9}`, `{16,17}` (a `2^j` and its successor). The excess `A·D(n) = (a+1) − a = 1` always: the two unpaired values sit at adjacent ranks of opposite parity, the larger at the odd rank, net `+1`.

**Unification (the load-bearing structural lemma for the field):** *Every grid minimizer has its odd-multiplicity pieces forming either `{1}` (one piece, odd count) or `{2^j, 2^j+1}` (two pieces, even count), and in both cases the scaled excess `A·D(n) = 1`.* The minimizers are **NOT unique** — they form a rich family — but they all share this single odd-mult-leftover = 1 (or {a,a+1} consecutive-powers-of-two) structure. The mirror is the *generic* equality case (dominant count: 628/3046 for n=5, 103/184 for n=4, 19/22 for n=3); the pair-pile is a *thin special case*.

**Implication for the two routes:**
- **For the variational / Hall-Match route (G1, `pairing-partner`):** a proof of `e_M ≤ o_R` / the residual Match need NOT pin a unique minimizer — it must show the residual is `≥ 0` with equality iff the odd-mult structure above holds. The "superincreasing R" lever flagged in round 3 is the right target: R's pieces grow geometrically (`2^j`), so any even-count minimizer's `{2^j, 2^j+1}` pair is exactly an (R-piece, R-piece+1) pair, and the +1 is the level-boundary excess `α(n)`. The structure says: the irreducible residual is ONE unit (in scaled grid), and it sits at the dyadic level boundary.
- **For the unique-extremum route (G2, regime-N):** the minimizer is FAR from unique on the grid (46 distinct multisets for n=5). So any "unique extremum ⇒ dyadic" argument for the upper bound must be reformulated as a *structural-classification* argument (classify which odd-mult patterns are achievable) rather than a unique-minimizer argument. This rules out a naive "extremal minimizer is unique ⇒ must be dyadic" route — the field has many extremals.

**Pair-pile vs mirror:** the pair-pile (n−1 marks, even count, `{2,3}` odd-mult) and the mirror (n marks, odd count, `{1}` odd-mult) are *different* extremals giving the same `A = α(n)`. The mirror is the maximally-refined extremal (all n marks spent); the pair-pile is the minimally-refined one (n−1 marks). Both certified.

---

## A3. Regime-N probe (n=3, non-dyadic Liu configs) — the empirical heart of G2

For each non-dyadic level-3 Liu config I computed `Φ(Liu) = min_Xiang A` by (a) grid-50 enumeration and (b) 80k random-real samples. `α(3) = 1/15 ≈ 0.066667`. `Φ < α(3)` strictly is the regime-N conjecture.

| Liu config (pieces, sorted desc) | grid-50 min A | random min A (80k) | `Φ < α(3)`? | `Φ → 0`? (sliverable) |
|---|---|---|---|---|
| dyadic `(8,4,2,1)/15` | 0.066667 | 0.066667 | **NO** (saturates α, as required) | no |
| balanced `(1/4,1/4,1/4,1/4)` | 0.020000 | **0.000781** | YES | yes (bisect+sliver drives `A→0`, Liu→1/2) |
| dominant-0.6 `(.6,.2,.1,.1)` | 0.040000 | 0.006495 | YES | near-0 |
| extreme-dom `(.9,.0333,.0333,.0333)` | 0.013333 | 0.004743 | YES | near-0 |
| tiny-tail `(.8,.1,.05,.05)` | 0.020000 | 0.007249 | YES | near-0 |
| near-dyadic `(.55,.25,.1,.1)` | 0.020000 | 0.007588 | YES | near-0 |
| two-dyadic `(.5,.25,.125,.125)` | 0.020000 | 0.006107 | YES | near-0 |

**Verified:** `Φ(Liu) < α(3)` strictly for EVERY tested non-dyadic n=3 config; the dyadic config saturates `α(3)` exactly. The random min is much smaller than the grid min (slivers), and for balanced configs `Φ → 0` (Xiang bisects + cuts slivers to make all pairs cancel, `Liu → 1/2`). This matches the round-3 finding (true cap `31/60 < 8/15` on all tested non-dyadic n=3) and **CONFIRMS the regime-N conjecture numerically** for n=3.

**Conjecture (labeled as such):** for every non-dyadic n≥3 Liu config, `Φ(Liu) < α(n)` strictly, and often `Φ(Liu) ≈ 0` (balanced) or a small positive value (dominant). The mechanism is the sliver/shave generalizing U(1)/U(2) — NOT the falsified `A ≤ 0` pairing (round 2) and NOT the falsified R-pile greedy (round 3). The n=2 four-strategy proof is the template; the even-block / multiplicity-parity framing (round-3 flag) is the candidate lift.

---

## A4. The "+1 boundary quantity" check (preventing a repeat of the round-3 unified-Mersenne death)

Round-3 `unified-mersenne-charging` died on the claim `M − total(R) = α(n+1)` for arbitrary partitions. I re-verified the failure precisely.

**The tautology.** For ANY partition of `[0,1]` with largest piece `M` and rest `R = 1 − M`: `M − total(R) = M − (1 − M) = 2M − 1`. Equality `2M − 1 = α(n+1) = 1/D(n+1)` holds **iff** `M = (1 + 1/D(n+1))/2 = 2^{n+1}/D(n+1) = f(n+1)`, i.e. iff the largest piece IS the level-`(n+1)` dyadic largest. So `M − total(R) = α(n+1)` is a **dyadic-only identity**, NOT a general partition identity.

| partition (n+1=3, `α(3)=1/15`) | M | total(R) | M−total(R) | = α(3)? |
|---|---|---|---|---|
| dyadic `(.5333,.2667,.1333,.0667)` | 0.5333 | 0.4667 | **0.066667** | YES |
| non-dyadic `(.6,.2,.1,.1)` | 0.6 | 0.4 | 0.2 = 1/5 | **NO** (round-3 counterexample, re-confirmed) |
| non-dyadic `(.5,.25,.125,.125)` | 0.5 | 0.5 | 0.0 | NO |
| non-dyadic `(.9,.0333×3)` | 0.9 | 0.1 | 0.8 | NO |
| balanced `(.25×4)` | 0.25 | 0.75 | −0.5 | NO (even negative!) |

**Verdict (verified):** any approach that charges the Mersenne "+1" to the boundary `M − total(R)` fails off the dyadic — it is a tautological consequence of the dyadic self-similarity (`M = f(n+1)`, `R` a scaled level-`n` dyadic), not a partition-wide invariant. Do NOT retry a unified amortized-potential `Ψ = 1/A` charging the `+1` to `M − total(R)`. The same death as the retired `induct-one-mark` value-recursion. (Round-3 rule stands; this is the empirical re-confirmation the dispatch asked for.)

---

## B. Crux-corpus mining (Job B)

I queried the crux corpus (`past_crux_moves_database.json`, 2434 cruxes; `past_problems_database.json`). Filtered by `domain ∈ {combinatorics, number_theory}` and the subtopics `games-and-strategy`, `invariants-and-monovariants`, `extremal-principle`, `coloring-and-parity`, `p-adic-valuation`; then keyword-searched `technique`+`how_used` for `mirror`, `involution`, `partner`, `dyadic`, `geometric sequence`, `halving`, `alternating`. Top 6 cruxes that adapt to this problem, ranked by relevance:

### B1. **aimo-0019** (IMO-SL 2013, "paintful game" on the real line) — STRONGEST MATCH
*Problem:* Player A has 4 units of ink, each round picks `m`, supplies `1/2^m` units; Player B paints a real interval of length `1/2^m` at integer-grid dyadic position. A tries to deplete the pot to cover the line; B tries to conserve.
**Two cruxes that map directly:**
- *"Bound a family of dyadic-length pieces of pairwise distinct sizes by twice the largest, via the geometric sum of distinct negative powers of two."* — This is EXACTLY the **superincreasing structure of R** that round-3 flagged as the lever for the residual Hall Match (G1). R's pieces are `2^j/D(n)`; "at most one interval of each length" ⇒ "the pre-painted pieces swallowed total < 2/2^m" is the geometric-sum `< 2·(largest)` bound. **Adapt:** prove `Σ_MM m_even ≤ Σ_RR r_odd` by showing the `MM`-pair smaller-halves are distinct dyadic sizes bounded by a geometric sum dominated by the `RR`-pair larger-halves (the superincreasing R-pieces). This is the cleanest known analogue for closing G1.
- *"Maintain a linear potential bounding cumulative resource by a constant times progress, proved by amortized induction that charges each frontier advance against the pieces it absorbs."* — A **charging-scheme template** (NOT the falsified `Ψ=1/A` unified potential — this is a *linear* potential `3·x_r`, charged per frontier advance). **Adapt:** a linear charging inequality `e_M ≤ c·o_R` with the right constant, proved by amortized induction over the merged sort. This is far from the dead per-mark `−2T` wall and far from the falsified `Ψ=1/A` (which was nonlinear/circular).

### B2. **aimo-0117** (Dutch TST 2021, Jesse-Tjeerd stones) — STRONG
*Problem:* Jesse writes positive reals on stones split between two boxes (half each); Tjeerd moves stones between boxes; Jesse wants the two box-sums to differ maximally at the end.
**Two cruxes:**
- *"Assign the played values as a two-sided geometric (dyadic) sequence so that the single largest value strictly exceeds the sum of all the others."* — This IS the dyadic config: Liu's `(2^n, 2^{n−1}, …, 1)/D(n)` has `2^n > 2^{n−1}+…+1 = D(n)−2^n`. **Adapt:** the dyadic dominant-piece property is the *attainment* half of `c(n)` — the largest piece `M > 1/2` pins Liu's rank-1 take. (Caveat from round-1 rules: the bare dominant-piece claim is FALSE for the lower bound; the correct lever is the dyadic self-similarity `M = 2·R_largest`. Use the crux as the *construction* intuition, not the proof.)
- *"Defer committing the extreme value until the opponent's move vacates its target cell, playing a non-committal value elsewhere, to hold an invariant."* — A per-ROUND invariant strategy (Jesse waits for Tjeerd's move, then commits). **Adapt:** this is the structural reason the per-Xiang-mark induction fails but a per-ROUND (both players add a mark) Mersenne recursion `B(n+1)=2B(n)+1` is the right object (round-1/2 rule). The "defer commitment" mirrors the `±a` cancellation in the n=1 real proof (the small fragment jumps rank, cancelling the large-fragment loss).

### B3. **aimo-0779** (IMO-SL 2017, Eduardo-Fernando digit game) — STRONG
*Problem:* Players alternate choosing digits at indices `0..p−1`; Eduardo (first) wants the final number divisible by `p`.
**Key crux:** *"Reply to the opponent's move on element i by immediately playing the image of i under a fixed involution of the index set"* + *"Choose the response value on the paired index so the pair's combined contribution becomes independent of the opponent's chosen value, summed over all pairs to a quantity that vanishes mod p."*
**Adapt:** this is the **mirror certificate** (Xiang at `1−l_j`, a fixed-point-free involution on the stick). The "pair sums to zero mod p" is the pair-cancellation `A = 0` per pair (the pair-pile's equal pairs). The involution `l ↦ 1−l` is the exact analogue of `i ↦ i+(p−1)/2`. The crux gives the *strategy-stealing* framing: Eduardo's opening move fixes the unpaired index (the "floating" piece) — in our problem the unpaired piece is the single value-`1` leftover (Family 1) or the `{2^j, 2^j+1}` pair (Family 2). This is the cleanest known mirror-strategy template.

### B4. **aimo-0225** (RMM 2015, n-gon area-increase game) — MODERATE
*Problem:* Players slide counters on an n-gon; a move is legal iff the triangle's area strictly increases; first player unable to move loses.
**Key crux:** *"Determine the game value by recursing on the 2-adic valuation of a difference that exactly halves at each relevant step, so the P/N status flips with each halving and depends only on the valuation's parity."*
**Adapt:** the Mersenne recursion `D(n+1) = 2·D(n)+1` is a "halving + 1" step; the `−2T` tail-flip in `ΔA = 2((−1)^r b − T)` is the parity flip. The game value `c(n) = (1 + 1/D(n))/2` depends on `D(n) mod 2` (= 1, odd) — a parity-locked value. This is the structural reason the integer-grid parity theorem (R2) works: `A·D(n)` is odd ≥ 1. The crux suggests a **2-adic-valuation framing** of `A`'s parity could close G1 on the grid and lift partially.

### B5. **aimo-0093** (Dutch TST 2011, `v_2(5^n − 3^n) ≤ v_2(n) + 3`) — MODERATE
**Key crux:** *"Show the difference of two integer-valued functions is invariant under a halving step by proving each side increases by exactly one, reducing the inequality to base cases via induction on `v_2(n)`."*
**Adapt:** `a(2k) = a(k) + 1` and `b(2k) = b(k) + 1` ⇒ `a − b` invariant under doubling. The Mersenne `D(n+1) = 2D(n) + 1` has the same "each side increases by exactly one under the halving step" structure: `A_scaled·D(n+1)` and `D(n+1)` both increment by the level-boundary `+1`. This is the induction-on-`v_2` template that could make the grid-parity theorem (R2) lift toward reals — the parity of `A·D(n)` is locked to the parity of `D(n)`, and `D(n)` is always odd.

### B6. **aimo-0596** (IMO-SL 2014 C8, 1024-card deck) — MODERATE
**Key crux:** *"Pair the ground set by a fixed nonzero translation and show any transversal's XOR lands in the two-element coset"* + *"partner-mirroring strategy: responder answers each opponent pick with its fixed involution-partner, seeded with one full pair up front so the final invariant lands on a card the responder holds."*
**Adapt:** the fixed-point-free involution `X ↦ X△B` is the mirror `l ↦ 1−l`; the "transversal's XOR lands in `{0, B}`" is the pair-pile's `A ∈ {0, α(n)}` (either all pairs cancel, or one unpaired leftover `= α(n)`). The "seeded with one full pair up front" is the pair-pile's `(3,2)` residual pair. This gives the **algebraic (F_2/coset) framing** of the mirror certificate — a different lens than the geometric one, possibly lifting to reals via a measure-theoretic / coset argument.

**No other crux in the corpus is a closer match** — I checked all 40 `games-and-strategy` cruxes and all `mirror`/`involution`/`dyadic` keyword hits. The closest is aimo-0019 (paintful game), which is a near-twin in setup (dyadic lengths on the real line, adversarial). The corpus has NO crux about alternating-sum minimax over interval cuts specifically — our problem's exact mechanism is not directly in the corpus, so the borrow is at the *crux-move* level (the superincreasing bound, the involution-mirror, the 2-adic parity), not a citation.

---

## Verdict: what structure does the field now have that it didn't last round?

Three new structural assets. **(1) The minimizer census (A2):** grid minimizers are NOT unique — they form a rich family (46 distinct multisets for n=5) unified by a single clean invariant: the odd-multiplicity pieces are either `{1}` (odd count, mirror family, dominant) or `{2^j, 2^j+1}` (even count, pair-pile family, thin). This tells G1's route the target is a *classification* (`A·D(n) = 1` iff this odd-mult structure), not a unique-extremum pin; and tells G2's route the "extremal is unique ⇒ dyadic" naive argument is dead (many extremals). **(2) The regime-N empirical confirmation extends to n=3 reals (A3):** `Φ < α(3)` strictly for every tested non-dyadic config, with `Φ → 0` for balanced (sliver-driven) — the conjecture is numerically solid and the sliver mechanism is the right target. **(3) The boundary-quantity death is now precisely characterized (A4):** `M − total(R) = α(n+1)` iff `M = f(n+1)` (dyadic-only tautology), foreclosing any unified-potential retry. The corpus adds the strongest analogue found in 4 rounds — **aimo-0019 (paintful game)**, whose "bound dyadic-length distinct-size pieces by twice the largest via geometric sum" crux is the exact superincreasing-R lever round 3 flagged for the Hall Match, giving G1 a concrete borrowed move to try.
