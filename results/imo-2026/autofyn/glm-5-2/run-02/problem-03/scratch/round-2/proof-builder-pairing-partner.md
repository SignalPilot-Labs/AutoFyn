# Build report — `pairing-partner` (round 2, imo-2026-03)

## What I proved this round

### Lower-bound spine (Lemma L general-n) — partial close

1. **`M ⊎ R` self-similar decomposition + dyadic-dominance identity** (full proof).
   The level-`(n+1)` dyadic decomposes as `{M} ⊎ R` with
   `M = 2^{n+1}/D(n+1)`, `R = (D(n)/D(n+1))·(level-n dyadic)`, and the
   load-bearing identity `M − total(R) = 1/D(n+1)`. This makes Lemma `L(n+1)`
   exactly the statement `global_A ≥ M − total(R)`, sidestepping the per-mark
   local-cut / `−2T` tail-flip obstruction by working globally on `M`-vs-`R`.

2. **Lemma `L(n+1)`, `k = 0` sub-case — CLOSED (trivial, no induction).**
   When `0` Xiang marks land in `M`, `M` is global rank `1`; the rest `R'`
   contributes `−A(R') ≥ −total(R')`; `global_A ≥ M − total(R) = 1/D(n+1)`. ✓
   (Strict inequality in fact — verified at `n = 2, 3`: `k = 0` min oddsum is
   `5/7`, `2/3`, both `> f(n)`.)

3. **Lemma `L*(n)` — single-aux strengthened dual — CLOSED, as a corollary of
   `L(n)` at the same level.** Written to
   `results/imo-2026-03/lemmas/lemma-L-star-single-aux.md` (proposed for
   certification). Mechanism: three-case rank analysis of where `w` lands in
   the merged sort `{w} ∪ R'`. `r` even: trivial. `r ≥ 3` odd: free from
   sortedness (`w ≤ s_2 ≤ evensum(R') + A_tail`, no induction). `r = 1`: uses
   `oddsum(R') ≥ R_largest ≥ w` from `L(n)`. Verified: min gap `0` for
   `n = 1..3` (exact) and `n = 4` (Monte-Carlo, 30k trials), equality at the
   self-similar extremal (`R'` = pair-pile, `w = R_largest`) for `n = 2..5`.

4. **Lemma `L(n+1)`, `k = 1` sub-case — CLOSED (reduces to `L*(n)`).**
   `M → (m_1, m_2)`, `m_1 ≥ M/2 = R`'s largest (unrefined) piece, so `m_1` is
   global rank `1`; `global_oddsum = m_1 + evensum({m_2} ∪ R') ≥ m_1 + m_2 = M`
   by `L*(n)` applied to the scaled rest. ✓ Verified at `n = 2, 3`: `k = 1`
   min oddsum `4/7`, `8/15`, matching `f(n+1)`.

### Upper bound (Lemma U) — pivot, dependency tracked

5. **Retired the dead Hall route** (round-1 Hall-dominance failure for
   non-dyadic configs) and the per-mark monovariant (certified dead end via
   `ΔA` `−2T`). Pivoted to the **two-regime split**:
   - **Regime D** (dyadic): pair-pile / mirror (IMPORTED) caps at `f(n)`. ✓
   - **Regime N** (non-dyadic): the round-2 review computationally confirmed
     the cap is `< f(n)` (non-dominant `n = 2` configs cap `≈ 0.50–0.525`
     below `f(2) = 4/7`; dominant non-dyadic cap `≈ 0.50–0.504`), BUT the
     `A ≤ 0` pairing mechanism is FALSE (verified). The correct mechanism is
     a sliver/shave generalizing the certified `U(1)` sliver mode; this is
     the sibling `two-regime-disjunctive`'s task (dispatch: fix F1, F2). I do
     NOT claim regime N without it; the dependency is recorded in the approach
     file, the proof is kept self-contained on what it does claim (regime D).

### Mirror certificate — new shared lemma

6. **Mirror certificate** written to
   `results/imo-2026-03/lemmas/lemma-mirror-dyadic-cap.md` (proposed for
   certification). Xiang's `n` mirror marks `1 − l_j` produce the symmetric
   pair-pile, `A = 1/D(n)`, `Liu = f(n)`. Verified `n = 1..5`. Salvaged from
   the cut `mirror-dyadic-saddle` per the review. Full proof of distinctness,
   symmetry, the central piece, the symmetric pairs, and the excess.

## Remaining gaps (honest)

- **(G1) Lemma `L(n+1)`, `k ≥ 2` sub-case — OPEN.** Per-round peeling (D1)
  requires a monotonicity ("merging two `M`-sub-pieces and re-placing a mark
  in `R` does not increase oddsum") that the `ΔA` `−2T` tail-flip blocks
  locally; not closed. The multi-aux `L*` is FALSE (explorer counterexample
  `W = (1/9, 4/9, 1/9)` over `D = 9`). The D2 exchange ("a `k = 1` response
  at least as good for Xiang as any `k ≥ 2` response") is conjectural; the
  `n = 3` brute force (7 extremals at `k = 1`, 21 at `k = 2`, 12 at `k = 3`)
  shows the literal monotonicity is FALSE. Brute-force min `= f(n)` for
  `n = 1..5` is robust but is a CHECK, not a proof. This blocks `L(n)` for
  `n ≥ 3` and hence the full lower bound.

- **(G2) Lemma `U` regime-N mechanism — OPEN, dependency on sibling.** The
  sliver/shave general-`n` construction is the sibling
  `two-regime-disjunctive`'s task. Until it is supplied, the upper bound is
  closed only at the dyadic config (regime D) and at `n = 1` (round 1).

Both gaps are exactly the two halves (lower, upper) of general `n`. Status
remains `partial`.

## Spec concerns

- The dispatch's `L*(n−1)` notation (used in the outline for the `k = 1`
  reduction) is one level down from `L(n+1)`, i.e. `L*(n)` in my notation. I
  reconciled this: `L*(n)` is applied to the *scaled level-`n` rest* `R` of
  the level-`(n+1)` config. The scaling factor `D(n)/D(n+1)` is handled
  explicitly (the auxiliary `w = m_2` rescales to `m_2·D(n+1)/D(n) ≤
  R_largest = 2^n/D(n)`). No off-by-one.
- The outline's claim "k=1 reduces to `L*(n−1)` (verified n=1..5)" — I verified
  `L*(n)` for `n = 1..4` and the `k = 1` reduction for `N = 2, 3` (=`n+1` for
  `n = 1, 2`); the chain is `L(n) ⟹ L*(n) ⟹ L(n+1)[k ≤ 1]`, sound.
- The reviewer's F1 (regime-N `A ≤ 0` is FALSE) is respected: I do NOT assert
  `A ≤ 0` anywhere; the regime-N mechanism is explicitly recorded as
  sliver/shave, delegated to the sibling, NOT claimed here.
- The reviewer's F3 (regime-D rescaling is circular for arbitrary dominant
  non-dyadic configs) is respected: my regime D is restricted to "the Liu
  config IS the (scaled) level-`n` dyadic" — the only case the pair-pile /
  mirror certificate directly certifies. All other configs go to regime N.
  I do NOT claim a rescaling for dominant non-dyadic configs.

## New lemmas proposed (for reviewer certification)

1. `results/imo-2026-03/lemmas/lemma-L-star-single-aux.md` — Lemma `L*(n)`:
   single-aux strengthened dual of `L(n)`. Full proof + verification.
2. `results/imo-2026-03/lemmas/lemma-mirror-dyadic-cap.md` — Mirror
   certificate: symmetric `n`-mark dyadic cap. Full proof + verification.

Both are reusable across approaches (any `M ⊎ R` lower-bound route imports
`L*`; any dyadic-cap route can use the mirror in place of the pair-pile).

## Status

`partial`. The lower-bound spine is closed for `k ≤ 1` plus a clean reusable
`L* ⟸ L` lemma; the `k ≥ 2` sub-case and the regime-N mechanism of Lemma `U`
remain open. `c(n) = f(n)` is verified for `n = 1..5` but not proved for
general `n`.
