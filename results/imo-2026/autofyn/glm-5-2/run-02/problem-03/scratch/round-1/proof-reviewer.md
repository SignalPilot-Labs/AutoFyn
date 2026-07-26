# Proof-reviewer — IMO 2026 Problem 3, round 1

Conjectured answer `c(n) = 2^n/(2^{n+1}−1)` (verified exact for n=1..5 by the
explorers). The problem is `compute_and_prove` / `answer_type: expression`, so
`solved` needs BOTH a Liu lower-bound strategy (≥ f(n) for all Xiang) AND a
Xiang upper-bound forcing strategy (≤ f(n) for all Liu configs), each rigorous
for general n. Neither approach closes both halves this round; both are honestly
marked `partial`. I verified every claimed lemma independently (sympy/Fraction
brute force + algebra re-derivation); findings below.

## Ground-truth checks I ran

- **Lemma G (greedy → odd-rank sum).** Brute-force minimax vs `oddsum` on 5000
  random multisets of size 1–7, values in {1..20}: **0 mismatches**. The lemma is
  true. The pairing-partner strong-induction proof of it is algebraically valid
  (I re-derived both Δ_k ≤ 0 for (A) and oddsum(R_k) ≥ oddsum(R_1) for (B), 1-indexed,
  and they reproduce). The induct-one-mark invariant proof of the upper-bound
  half is NOT valid (see below).
- **L(2).** Exhaustive exact-rational grid (3240 Xiang 2-mark responses on the
  dyadic config 1/7,2/7,4/7): min `oddsum = 4/7`, matching the casework.
- **L(n) Monte Carlo** (200k random Xiang responses per n): min ≥ f(n) for
  n=1..5 (n=1..4 hit the exact extremum f(n); n=5 sample-min 0.5099 ≥ 32/63).
- **U(1) brute.** Max over a grid of `a ∈ (0,1/2]` of (Xiang's best cap) = 0.665
  ≤ 2/3. The bound holds.
- **Pair-pile construction.** Exact arithmetic for n=2,3,4,5: `Σ pieces = D(n)`,
  `A = 1` (over D), `oddsum = 2^n`. The construction is correct and uses ≤ n
  marks (n−1 for n≥2, 1 for n=1).
- **ΔA closed form** (induct-one-mark). Re-derived and stress-tested on 4954
  local-cut trials: **0 mismatches**. The formula `ΔA = 2·((−1)^r b − T)` (T =
  old tail alt-sum with *global* rank signs) is correct for the adjacent-rank
  (local) case. (My first test had a sign-convention bug on the tail; the
  formula itself reproduces once T uses global-rank signs.)

---

## `induct-one-mark` — verdict: CHANGES REQUESTED (Status: partial)

**Status honestly marked `partial`.** Real, correct progress:

- **Lemma G — lower-bound half (Liu greedy ≥ oddsum) is correct.** The invariant
  "before Liu's j-th turn, ≥1 piece of size ≥ p_{2j−1} survives" is justified
  (2j−2 pieces removed in 2j−2 turns ⇒ at least one of p_1..p_{2j−1} remains).
- **Lemma S (small-n).** Verified computational certificate; correctly labeled a
  check, not a proof step.
- **L(1), L(2).** Both rigorous; L(2) corroborated by my brute force
  (min = 4/7 over all 3240 Xiang 2-mark responses).
- **U(1).** The two-mode (bisect/sliver) case split is rigorous and the bound
  reproduces (max cap 0.665 ≤ 2/3 on a grid).
- **ΔA closed form.** Correct (verified).
- The two main gaps (Lemma L general-n interleaving; Lemma U inductive step) are
  **honestly flagged**, not papered over, and the obstruction analysis (R is a
  value-recursion not a per-mark monovariant; parity-flip-on-tail via the −2T
  term in ΔA) is correct and load-bearing for the next round.

**Flaws found (adversarial):**

1. **Lemma G upper-bound half is NOT rigorously proved — overclaim.** The file
   marks Lemma G "fully proved", but the Xiang-upper-bounds-`S_odd` half rests on
   the per-piece claim *"Liu's j-th piece ≤ p_{2j−1}"* justified by *"exactly
   the top 2j−2 pieces p_1,…,p_{2j−2} are gone"* before Liu's j-th turn. **This
   per-piece claim is FALSE under Liu deviation.** Concrete counterexample
   (verified): pieces `5,4,3,2,1`, `oddsum = 9`. Liu deviates on turn 1 (takes
   `p_3 = 3`); Xiang greedy takes `p_1 = 5`; remaining `{4,2,1}`; Liu's 2nd
   piece (greedy) = `p_2 = 4`, but the claimed bound is `≤ p_3 = 3`. `4 > 3`,
   contradiction. The "exactly the top 2j−2 are gone" assertion fails because
   Xiang's greedy removes the then-largest, not the rank-next, so when Liu
   deviates downward the surviving rank-next (`p_2` here) is NOT removed. The
   **total** bound `Liu ≤ oddsum` (8 ≤ 9 here) is still TRUE — but it is NOT
   proved by this per-piece argument; it requires the exchange/strong-induction
   argument that the sibling `pairing-partner` gives correctly. **Downgrade:
   induct-one-mark's own Lemma G proof has a real gap in its upper-bound half.**
   The lemma itself is true and importable; the approach's claim that it is
   "fully proved" here is an overclaim (rigor rule: prove, don't conjecture;
   overclaiming is worse than admitting a gap).

2. **U(1) sliver mode has an edge-case hole at `a = 1/2`.** The sliver requires
   `0 < ε < 1 − 2a`, claimed "positive since a ≤ 1/2". But at `a = 1/2`,
   `1 − 2a = 0`, so NO valid ε exists; the sliver mode does not cover `a = 1/2`.
   The bound still holds at `a = 1/2` (Xiang picks `ε ≤ 1/6`, giving sorted
   `(1/2, 1/2−ε, ε)` and `oddsum = 1/2 + ε ≤ 2/3`) — but this uses a DIFFERENT
   sorted order than the sliver formula `(1−a−ε, a, ε)` (which needs
   `1−a−ε ≥ a`, i.e. `ε ≤ 1−2a = 0`). So the n=1 upper-bound proof has a one-point
   gap at `a = 1/2`; trivially patched (one line: handle `a = 1/2` via the
   alternate sort), but as written it is a rigor hole. (Same hole in
   `pairing-partner`.)

**Progress assessment.** Beyond the honest gaps the builder flagged, Lemma G's
upper-bound half is an overclaim — the approach should either import the
certified Lemma G from `pairing-partner` (where it is rigorous) or re-prove the
upper bound via the exchange argument. The ΔA identity, L(1), L(2), U(1) (modulo
the `a=1/2` patch), and the obstruction analysis are all correct and reusable.

**Verdict: CHANGES REQUESTED.** Real progress (L(1), L(2), U(1) modulo patch,
ΔA identity, correct obstruction analysis), but Lemma G's upper-bound proof is
flawed (overclaim) and both main gaps (Lemma L general-n, Lemma U inductive
step) remain open. Route the builder next round to (a) fix Lemma G by importing
the certified strong-induction proof, (b) patch U(1) at `a=1/2`, (c) attack
Lemma L general-n via the dyadic self-similarity (the pair-pile construction
from the sibling shows the dyadic value is *tight* at f(n), so Lemma L only
needs the ≥ direction).

---

## `pairing-partner` — verdict: CHANGES REQUESTED (Status: partial)

**Status honestly marked `partial`.** Stronger progress than `induct-one-mark`:

- **Lemma G — FULLY and rigorously proved** by strong induction on M with both
  move-orders (A: Liu-to-move → oddsum; B: Xiang-to-move → evensum) loaded into
  one induction. I re-derived both delta computations:
  - (A) `Δ_k = (p_2−p_1)+…+(p_{2m}−p_{2m−1}) ≤ 0` for k odd OR even (k≥2), so
    Liu's best first move is `p_1` (greedy), value = oddsum. ✓
  - (B) `oddsum(R_k) − oddsum(R_1) = (p_1−p_2)+…+(p_{2m−1}−p_{2m}) ≥ 0` for all
    k, so Xiang's best first move is `p_1` (greedy), value to Liu = evensum. ✓
  The proof text has several honest "careful / wait / let me redo" self-corrections
  (the initial `evensum(R_1) = Σ_{j>1,j even}` is corrected to
  `= p_3+p_5+…`); the FINAL conclusions are correct. This is the version of
  Lemma G that I certify (see lemmas/).
- **Parity identity** `Liu = (1+A)/2`. Correct, a direct corollary.
- **n=1 complete** (L(1) + U(1)). Rigorous, modulo the same `a=1/2` sliver edge
  case (one-line patch).
- **Pair-pile construction (Xiang caps the dyadic config at f(n), ALL n).**
  Fully proved by explicit construction + exact arithmetic; I verified
  `Σ = D(n)`, `A = 1`, `oddsum = 2^n` for n=2..5. The construction uses ≤ n
  marks (n−1 for n≥2 — splitting pieces of size 2^k for k=2..n — and 1 mark
  for n=1). This is **real, general-n forward progress**: it shows the dyadic
  config's value is **at most** f(n) for every n (not just n=1,2). Once Lemma L
  (the matching ≥ f(n) lower bound on the same config) is closed, the dyadic
  value is pinned to exactly f(n) and `c(n) ≥ f(n)` follows. This is the
  strongest single result of the round.

**Flaws / gaps found (adversarial):**

1. **U(1) sliver edge case at `a = 1/2`.** Same as induct-one-mark: the sliver
   needs `ε ≤ 1−2a = 0` at `a=1/2`; the alternate sort gives the bound but the
   sliver formula as written does not cover `a=1/2`. Trivial patch.
2. **Lemma L general-n (gap G1).** Honestly open. The builder correctly notes
   the naive "largest piece dominates" argument is INSUFFICIENT (their
   counterexample `M=0.6 → (0.3,0.3)`, `R=0.4 → (0.2,0.2)`, final
   `0.3,0.3,0.2,0.2`, `oddsum = 0.5 < 0.6` is valid). The real engine is the
   recursive self-similarity of the dyadic config (R's largest = M/2), which
   the builder identifies but does not turn into an induction. Honest gap.
3. **Lemma U / G2 (arbitrary-config upper bound).** Honestly open. The Hall-
   matching partner-construction does not close for non-dyadic Liu configs; the
   builder honestly reports the Hall dominance test fails in simple examples.
   This is the problem's main open gap.

**Progress assessment.** Lemma G fully rigorous, pair-pile construction for all n
(the tightness/upper half of the dyadic saddle), n=1 complete, obstruction
analysis correct. The two open gaps (Lemma L general-n, Lemma U arbitrary-config)
are honest.

**Verdict: CHANGES REQUESTED.** Best progress of the round (Lemma G rigorous,
pair-pile general-n). Stays live; route the builder next round to attack Lemma L
general-n (the dyadic self-similarity + the now-proved tightness from the
pair-pile give a clear target: only the ≥ direction is needed) and to attack
Lemma U via a genuinely different route (see shared-wall note below).

---

## Do both upper-bound routes share a wall? (single-gap-trap assessment)

Partially. The two approaches attack the arbitrary-config upper bound (Lemma U)
via genuinely DIFFERENT mechanisms:
- `induct-one-mark`: one-mark value-recursion induction, blocked because (R) is
  a per-ROUND (both players add a mark) recursion, not a per-Xiang-mark
  monovariant, and the parity-flip-on-tail (the `−2T` term in ΔA) scrambles the
  residual game.
- `pairing-partner`: Hall matching on consecutive pair-excesses, blocked because
  the partner-construction for non-dyadic configs fails the dominance test.

The MECHANISMS and the OBSTRUCTIONS differ, so they are NOT the single-gap trap
in the strict sense (the outline-reviewer's "genuinely far apart" verdict is
defensible). HOWEVER, both target the SAME gap (arbitrary-config Xiang upper
bound) and neither has picked up the explorers' strongest structural insight
(computation report + upperbound explorer): **the cap is tight ONLY at the dyadic
config; for every non-dyadic config Xiang typically forces Liu down to exactly
1/2 < f(n).** This suggests a genuinely DIFFERENT framing neither builder took
up: a **two-regime proof** — separate the "dyadic-tight" regime (cap = f(n),
handled by the pair-pile construction + Lemma L) from the "everything else"
regime (cap ≤ 1/2 < f(n), where Xiang has slack). This would bypass both current
obstructions (no per-mark monovariant needed; no Hall matching on non-dyadic
configs needed). The field would benefit from a third approach opening this
two-regime / structural-invariant framing next round — it is far from both
current framings.

---

## Recorded outcomes (mcp__approach-ranker__record_outcome)

- `induct-one-mark` — round 1, outcome `partial`. Note: "Lemma G upper-bound half flawed (per-piece claim false under deviation: pieces 5,4,3,2,1, Liu deviates → 2nd piece p_2=4 > p_3=3); L(1),L(2),U(1) mod a=1/2 patch, ΔA identity all correct; Lemma L general-n + Lemma U inductive step open; shared wall with sibling on parity-flip."
- `pairing-partner` — round 1, outcome `advanced`. Note: "Lemma G fully rigorous (strong induction, verified); pair-pile construction proves Xiang caps dyadic config at f(n) for ALL n (verified n=2..5); n=1 complete; Lemma L general-n + Lemma U arbitrary-config open; strongest progress of round."

## Certified promotable lemmas (admitted to results/imo-2026-03/lemmas/)

1. **Lemma G (greedy-picking → odd-rank sum)** — certified from `pairing-partner`
   (the rigorous version). `lemmas/lemma-g-greedy-picking.md`.
2. **Pair-pile construction (dyadic-config cap, all n)** — certified from
   `pairing-partner`. `lemmas/lemma-pair-pile-dyadic-cap.md`.
3. **ΔA closed form for a local cut** — certified from `induct-one-mark`
   (correct derivation, verified). `lemmas/lemma-delta-a-local-cut.md`.

Rejected: none (all three pass the bar). Lemma S is a computational check, not a
reusable theorem — not promoted as a lemma (it stays as verified ground-truth in
the approach files).

## current.md status

`## Status` = `partial`. Correct pieces established (Lemma G, pair-pile
construction, n=1 complete, L(1), L(2), U(1) mod patch, ΔA identity); upper bound
for general n (Lemma U) and lower bound for general n (Lemma L) both open. No
`## Full proof` (not solved).
