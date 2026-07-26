# Lemma — dyadic-ratio overshoot (one-step characterization of greedy pile-match)

**Status: CERTIFIED** (round 3, reviewer) — core lemma (multiplicity change `+1` strict-dominant / `+2` dyadic-ratio; even-multiplicity block contributes `0` to `A`, odd-multiplicity block contributes `±a_2`) is unconditionally correct and verified. **Caveat (reviewer):** the corollary "cancels iff `a_1 > 2 a_2` strictly" is valid ONLY when `m` is ODD (the generic case `m = 1`); when `m` is even, the strict-dominant case gives `m+1` odd (overshoot) and the dyadic-ratio case gives `m+2` even (cancel) — counterexample `(6,3,3)`: `a_1 = 2 a_2`, `m = 2 → 4` (even, cancels), contradicting the unconditional "iff". The dyadic-config application (`m = 1` at the top level) is correct. The phrase "overshoots on the dyadic at every step" is loose — the greedy takes ONE admissible step on the dyadic (after it, `a_1 = a_2`, no admissible cut); the overshoot is at that single step. A *characterization* (dyadic detection), NOT a regime-N upper-bound proof — it does not close G2.

**Statement.** Consider a **greedy pile-match step** on a multiset of pieces, acting on
the two largest pieces `a_1 ≥ a_2` with `a_1 ≥ 2 a_2` (admissibility). The step places
one mark cutting `a_2` out of `a_1`, i.e. it replaces `a_1` by the two pieces
`{a_2, a_1 − a_2}`. Let `m` be the multiplicity of the value `a_2` in the multiset
BEFORE the step (`m ≥ 1`, since `a_2` is the 2nd-largest piece and at least one piece of
that size is present). After the step the multiplicity of `a_2` is:

- `m + 1`, if `a_1 > 2 a_2` strictly (**strict-dominant** case; `a_1 − a_2 ≠ a_2`), or
- `m + 2`, if `a_1 = 2 a_2` (**dyadic-ratio** case; `a_1 − a_2 = a_2`).

Consequences for the alternating advantage sum `A = Σ_i (−1)^{i+1} p_i` (sorted
descending):

- **Strict-dominant (`a_1 > 2 a_2`).** If `m` is odd (the generic case `m = 1`, since
  `a_2` is the 2nd-largest and ties at `a_2` are non-generic), the new multiplicity
  `m + 1` is EVEN. Equal pieces occupy a contiguous block of ranks in the sorted order;
  an even-multiplicity block contributes `0` to `A` (its members pair up at adjacent
  ranks `(r, r+1), (r+2, r+3), …`, each pair contributing `±a_2 ∓ a_2 = 0`). The
  residual `a_1 − a_2 > a_2` sits strictly ABOVE the `a_2`-block. **The created pair
  cancels.**
- **Dyadic-ratio (`a_1 = 2 a_2`).** If `m = 1` (generic), the new multiplicity is `3`
  (ODD). An odd-multiplicity block contributes `±a_2 ≠ 0` to `A` (one unpaired
  leftover). **The created "pair" does NOT cancel — the greedy overshoots.**

> **Corollary (dyadic detection).** The greedy pile-match step cancels its created pair
> iff the cut is strict-dominant (`a_1 > 2 a_2`). The order-`n` dyadic config
> `(1, 2, 4, …, 2^n)/D(n)` has `a_1 = 2 a_2` at every level (its two largest pieces are
> `2^n/D(n)` and `2^{n−1}/D(n)`, with `2^n/D(n) = 2 · 2^{n−1}/D(n)`; after cutting, the
> residual `2^{n−1}/D(n) = a_2`, and the same `2 : 1` ratio holds recursively on the
> remaining pieces `(1, 2, …, 2^{n−1})/D(n)`). Hence the greedy overshoots on the dyadic
> at every step — the greedy is a **regime-N tool only**, and the dyadic MUST be detected
> and routed to the certified pair-pile (regime D) instead.

**Proof.** The step removes one piece of size `a_1` and adds two pieces of sizes `a_2`
and `a_1 − a_2`. The new multiplicity of the value `a_2` equals (multiplicity before)
plus `1` (for the newly-added `a_2`) plus `1` more iff `a_1 − a_2 = a_2`. So the change is
`+1` (strict-dominant) or `+2` (dyadic ratio). For the contribution to `A`: equal pieces
occupy a contiguous block of ranks in the sorted descending order (any tie-break; equal
pieces are indistinguishable). A block of even multiplicity `2k` contributes
`0` (the pairs `(r, r+1), …, (r+2k−2, r+2k−1)` each contribute `±a_2 ∓ a_2 = 0`); a
block of odd multiplicity `2k+1` contributes `±a_2` (one unpaired leftover, sign
depending on the block's rank parity). Hence strict-dominant with `m` odd (→ `m+1` even)
cancels; dyadic ratio with `m = 1` (→ `m + 2 = 3` odd) overshoots. ∎

**Verification.** Exact rational arithmetic (python), one-step multiplicity check:
- `(8, 4)/15`: `a_1 = 2 a_2`, mult `1 → 3` (ODD), overshoot, final `A = 1/5` (block
  `4,4,4` at ranks `1,2,3` contributes `+4`, tail `(2,1)` contributes `−2+1 = −1`,
  total `3/15 = 1/5`).
- `(9, 4)/16`: `a_1 > 2 a_2`, mult `1 → 2` (EVEN), cancel, final `A = 1/4`.
- `(0.6, 0.25)`: `a_1 > 2 a_2`, mult `1 → 2` (EVEN), cancel, final `A = 3/10`.

All match the lemma.

**Scope and honest limitation.** This lemma is a ONE-STEP characterization. It explains
WHY the greedy overshoots on the dyadic (so the dyadic must be handled by the pair-pile,
regime D). It does NOT prove that the greedy caps below `f(n)` on non-dyadic configs —
in fact the greedy FAILS on balanced non-dyadic configs (`a_1 < 2 a_2`, where the
admissible cut does not apply and the bisect fallback overshoots, e.g.
`(.5, .3, .15, .05) → Liu = 11/20 > 8/15`) and on extreme-dominant configs with tiny tail
(e.g. `(.9, 1/30, 1/30, 1/30) → Liu = 0.9`). The regime-N upper bound for `n ≥ 3` is
OPEN; the greedy R-pile engine is RULED OUT as the universal regime-N mechanism
(counterexamples in `approaches/two-regime-disjunctive.md`, Section 5b).

**Knowledge-base tools.** **Invariants & monovariants** (the alternating advantage sum
`A` and the multiplicity-parity of equal-piece blocks); **Casework / exhaustion** (the
strict-dominant vs dyadic-ratio dichotomy on `a_1 / a_2`).

**Where proved.** `approaches/two-regime-disjunctive.md`, Section 5b.6 (round 3).
