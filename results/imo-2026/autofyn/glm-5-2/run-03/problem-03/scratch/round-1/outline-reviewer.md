# Outline-reviewer report — imo-2026-03 (Chu-Han war, IMO 2026 P3)

Round 1. Four new approaches, all targeting the whole problem end-to-end (greedy lemma + lower bound + upper bound, answer `c(n)=2^n/(2^{n+1}−1)`). I verified the answer `2/3, 4/7, 8/15` independently by brute-force minimax (n=2 worst random Liu held to 0.5702 < 4/7; dyadic config held to exactly 4/7). The greedy-alternating lemma is sound (proven airtight by the explorer). The lower-bound crux (G1, splits-inequality) is shared and tractable. **The bottleneck is the upper bound — and I ran numerics that materially change how the four upper-bound mechanisms should be ranked.**

## Numeric findings that drove this review

I tested the two restricted Xiang strategies that `surrogate-adversary` names, against 20–30k random Liu configs:

| strategy | n=1 | n=2 | n=3 | n=4 |
|---|---|---|---|---|
| `R_n` (always equal-split largest, n marks) | ratio 1.13 | 1.31 | 1.24 | 1.20 |
| `R_n` adaptive (try k=0..n, take min)        | 1.00 | 1.05 | 1.12 | 1.10 |
| `R_n'` (threshold-gated: equal-split unless largest < `2^n/D_n`, then barely-split+stop) | 1.00 | 1.37 | 1.43 | 1.46 |

(ratio = worst Liu odd-sum / target `2^n/D_n`; > 1 means the restricted strategy FAILS to cap.)

**Both `R_n` and `R_n'` are falsified for n ≥ 2.** The plain equal-split-largest is the wrong restricted strategy; the threshold variant is worse (the "barely-split and stop" rule ignores the *other* pieces still contributing to `S_odd`, so Liu gets `a + (other odd pieces)` ≫ target).

### What the TRUE optimal Xiang actually does (and why it matters)

On the hardest random config I found (Liu pieces desc `[0.798, 0.2007, 0.0013]`), the optimal Xiang uses marks `{0.4, 0.7}`, producing final pieces desc `[0.3, 0.3, 0.2007, 0.198, 0.0013]`. **This is a pairing strategy** — Xiang creates two near-equal pairs (0.3+0.3, 0.2007+0.198) that cancel in `D = S_odd − S_even`, leaving only the tiny 0.0013 as the odd surplus. On the dyadic n=2 config `{1/7,2/7,4/7}`, the optimal Xiang mark `{0.575}` barely-splits the 4/7 piece into 0.425 + 0.146, again forcing a cancellation structure, NOT equal-splitting the largest.

So the empirically-correct upper-bound mechanism is **pairing**, which is `pairing-charging`'s framing — and the empirical evidence *against* `surrogate-adversary`'s named engine.

## Per-approach verdicts

### dyadic-induction — APPROVE
- Spine is sound: the recursion `1/c(n) = 1/c(n−1) + 1/2^n` is exact (I checked: `2 − 1/2^n = (2 − 1/2^{n−1}) + 1/2^n`), so an inductive peeling that realizes it would prove the upper bound. The n=1 base (proven by explorer, two-regime split) is correct.
- Lower-bound half is the shared G1 crux; the "largest exceeds sum of rest" (`2^n > 2^n−1`) forcing is one-line and load-bearing.
- **Gap G2 (peeling step) is the live risk but attackable**: the builder must (a) pin the threshold separating Regime A (equal-split) from Regime B (barely-split) and show it falls out of the recursion exactly, and (b) prove the "at most n marks" accounting (n=2 worst case uses 1 mark — the approach correctly flags this).
- **Concern to flag for the builder:** my numerics show the optimal split on the dyadic config is *unequal* (4/7 → 0.425 + 0.146, not 2/7 + 2/7). The peeling split is NOT always an equal split — the builder must derive the actual split point from the recursion, not assume equal-splitting.
- No dead-end repeat. Whole attempt, distinct route. Registered.

### pairing-charging — APPROVE (strongest)
- **Strongest numeric support of the four.** The optimal Xiang response literally creates near-equal pairs (0.3+0.3, 0.2007+0.198) — the domino/antipodal-response mechanism the approach describes is exactly what the game's true minimizer does.
- The `D ≤ 1/D_n` target is derived cleanly inside the skeleton (`S_odd ≤ 2^n/D_n ⟺ D ≤ 1/D_n`).
- **Gap G2 (domino partition for ARBITRARY Liu marks) is the real crux and the approach correctly self-flags the circularity risk** (a partition that only works for the dyadic config is dead). The builder must define the partition constructively for any Liu marks and prove the deficit telescope sums to *exactly* `1/D_n` (slack ⇒ loose bound).
- The surplus telescope hitting `1/D_n` *exactly* is genuinely tight — lower bound numerics say equality is attained, so the telescope must be sharp, not just an inequality.
- Whole attempt, distinct route (one-shot charging, no induction). Registered. Highest Elo.

### surrogate-adversary — CHANGES REQUESTED
- The surrogate-adversary *framing* (design a restricted Xiang strategy that caps; cap transfers up to real Xiang via aimo-0560 weaker-minimizer direction) is a valid technique. The direction is right (weaker minimizer hits target ⇒ real does too).
- **But the specific restricted strategy `R_n` (equal-split largest) is NUMERICALLY FALSIFIED for n ≥ 2** (ratio 1.05–1.31 above target even with adaptive mark count). The monovariant gap "prove `Σ a_{1,k} ≥ 2(Φ_0 − 1/D_n)`" is therefore **structurally empty as written** — the premise "`R_n` caps" is false, so no monovariant proof of `R_n`'s cap can exist.
- **Required fix for the builder:** replace `R_n` with a restricted strategy that actually caps Liu at `2^n/D_n` (run the same falsification sweep — a working restricted strategy must score ratio ≈ 1.0). The empirically-correct restricted strategy looks pairing-based, so the builder must either (a) find a non-pairing restricted strategy that caps (keeping this approach distinct from `pairing-charging`), or (b) concede the surrogate collapses into pairing and recommend RETHINK next round. Do not pursue `R_n` further — it is dead.
- Not RETHINK because the surrogate *technique* is sound; only the named instance is wrong, and the approach's own "what would kill this" section anticipated exactly this falsification. Registered at the lowest Elo.

### alternating-potential — APPROVE
- The `D`-reformulation (`S_odd = (1+D)/2`) is clean and unifies both bounds through one lens — genuinely distinct framing.
- Lower-bound half (G1, `D ≥ 1/D_n` via self-reproducing invariant) is the shared tractable crux; the "equal-split-preserves-`D`" sub-lemma is subtle (the two equal halves are equal-valued hence adjacent in sorted order, so they occupy consecutive odd-even ranks and cancel — the rank-shift of intervening pieces is the part to verify) but numerics confirm `D ≥ 1/D_n`.
- **Upper-bound crux (G2) has a REAL factor-of-2 obstacle** — the approach honestly flags it and I confirm it is not a missing label:
  - Naive dyadic-decrement telescope: `Σ_{k=1}^n 1/2^k = 1 − 1/2^n`, so `D ≤ D_0 − (1 − 1/2^n)`. With `D_0 ≤ 1`, this gives `D ≤ 1/2^n`.
  - Target is `1/D_n = 1/(2^{n+1}−1) ≈ 1/2^{n+1}`, which is **half** of `1/2^n`. So the naive telescope is **insufficient** by a factor of 2 — it does NOT prove `D ≤ 1/D_n`.
  - The proposed resolutions are weak: (a) "`D_0 < 1` for worst Liu" is false (a single dominant piece gives `D_0 → 1`); (b) "decrements `1/2^{k+1}`" sums to `1/2`, giving `D ≤ 1/2`, still far above `1/D_n` for n≥2 (for n=1 alone, the needed decrement is 2/3, not dyadic).
  - The three-gap/Kronecker fallback is heavy and speculative.
- **This is the hardest upper-bound gap of the four** — a genuine mathematical obstacle, not an under-specification. The builder must either find a non-dyadic decrement schedule that reaches `1/D_n` exactly, or report the gap as unbridgeable (which would downgrade the approach). Registered at below-1500 because the upper-bound mechanism is the least credible.

## COPY request — REJECTED

The outliner asked to branch `surrogate-adversary` into `surrogate-adversary-thresholded` (the `R_n'` threshold-gated twin). **I reject the copy.** My numerics falsify `R_n'` for n ≥ 2 (ratio 1.37–1.46, *worse* than plain `R_n`) — the "barely-split and stop" rule ignores the other pieces still contributing to `S_odd`, so Liu gets `a + (other odd pieces)` ≫ target. Branching a falsified mechanism into a falsified twin doubles a dead line and wastes a builder. **If surrogate-adversary is to branch later, the twin should explore a *working* restricted strategy** (e.g. a mirroring/dyadic-offset surrogate), not a threshold variant of the dead `R_n`. No `copy_approach` call made; no twin skeleton seeded.

## Diversity check (framing, not technique)

The four upper-bound routes are nominally distinct (recursion / charging / restricted-strategy-monovariant / D-cap), and the lower bound is shared (G1, tractable, not a wall). **However, two diversity risks to flag for the orchestrator:**

1. **`surrogate-adversary` and `alternating-potential` both use the `Φ = D = S_odd − S_even` potential as their upper-bound engine.** They are partially overlapping in framing (monovariant on `D`), differing only in *how* `D` is driven down (restricted strategy vs direct cap). If surrogate-adversary is reworked, the builder should diversify its potential away from `D`-only.
2. **My numerics show the true optimal Xiang mechanism is pairing.** This is strong evidence for `pairing-charging` and a warning that the other three upper-bound routes (`dyadic-induction`'s peeling, `surrogate-adversary`'s restricted strategy, `alternating-potential`'s D-cap) may each have to *reproduce* the pairing structure to succeed — risking convergence of the field onto one framing next round. The orchestrator should watch for this: if 2+ of these three stall and resort to pairing, the field has collapsed and a genuinely different framing (e.g. LP/minimax-duality, or a measure-concentration argument) should be seeded.

## Shared-gap leverage (for the builder work allocation)

- **G1 (splits-inequality lemma `D ≥ 1/D_n`)** is shared by all four and tractable. Highest leverage: whoever proves it first certifies it as `lemmas/splits-inequality.md` and all four import it.
- **Greedy-alternating lemma** already proven airtight by the explorer — certify as `lemmas/greedy-alternating.md` immediately so no approach re-proves it.

## Ranking (all cold-start 1500; ranked by intrinsic promise of the upper-bound mechanism, anchored to my numeric evidence)

`update_ranking` applied with 6 pairwise comparisons:
- pairing-charging > surrogate-adversary (PC mechanism empirically confirmed as the true minimizer; SA's `R_n` falsified)
- pairing-charging > alternating-potential (PC mechanism supported; AP has a confirmed factor-of-2 obstacle)
- pairing-charging > dyadic-induction (PC mechanism empirically confirmed; DI's peeling split is unverified and likely non-equal)
- dyadic-induction > surrogate-adversary (DI has a sound recursion spine with attackable gap; SA's named engine is falsified)
- dyadic-induction > alternating-potential (DI's gap is attackable via a real recursion; AP's upper gap is a confirmed factor-of-2 wall)
- alternating-potential > surrogate-adversary (AP has a real non-empty gap; SA's specific mechanism is falsified)

Result:
1. pairing-charging — 1546
2. dyadic-induction — 1517
3. alternating-potential — 1485
4. surrogate-adversary — 1452

## Build set

Round 1 — broad population, parallel progress on every framing. All four registered approaches get a builder this round. The `surrogate-adversary` builder is dispatched with the CHANGES-REQUESTED note: do not pursue `R_n`/`R_n'` (falsified); find a restricted strategy that actually caps (run a falsification sweep, target ratio ≈ 1.0), or recommend RETHINK if none distinct from pairing exists.

build set: pairing-charging, dyadic-induction, alternating-potential, surrogate-adversary
