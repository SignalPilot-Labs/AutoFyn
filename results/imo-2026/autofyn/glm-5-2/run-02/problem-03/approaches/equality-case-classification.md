# `equality-case-classification` — IMO 2026 Problem 3

**Conjectured answer (verified exact for n = 1..5):** `c(n) = 2^n / (2^{n+1} − 1)`.
Denote `D(n) = 2^{n+1} − 1`, `f(n) = 2^n/D(n)`, `α(n) = 1/D(n)`.

---

## Status
partial

## Framing (unifying structural classification — far from pair-excess/Hall and from regime/pile)

Classify, over REALS, exactly when `A = α(n)` (the equality case), then read
off BOTH bounds from the classification. The grid census (Explorer 3, n=3,4,5)
discovered the unifying invariant: every grid minimizer of `A` on Liu's
dyadic has its odd-multiplicity pieces forming either

- `{1}` (odd piece-count, mirror family — the dominant extremal), or
- `{2^j, 2^j+1}` consecutive powers of two (even piece-count, pair-pile
  family — the thin extremal),

and in both cases the scaled excess `A·D(n) = 1`. The minimizers are NOT
unique (46 distinct multisets at n=5) but share this single odd-mult
leftover = 1 (or `{a, a+1}` consecutive-powers) structure.

This approach attacks the problem by proving the REAL-VALUED classification
theorem and deriving both gaps:

- **G1 (Liu dyadic, every Xiang response):** every real Xiang refinement has
  `A ≥ α(n)`, with equality iff the refinement realizes the
  `{1}` / `{2^j, 2^j+1}` odd-mult structure. Non-equality configs have
  `A > α(n)` strictly.
- **G2 (Liu arbitrary, Xiang's best):** the equality structure is
  dyadic-Liu-locked — realizable as `A = α(n)` ONLY when Liu's config is the
  dyadic. For non-dyadic Liu, Xiang forces `A < α(n)` strictly (the sliver
  mechanism of `two-regime-disjunctive`, derived here from the
  classification's converse).

This is genuinely different from pair-excess/Hall (no merged-sort matching)
and from the regime/pile greedy (no constructed Xiang strategy per regime);
it is a structural-classification route.

## Target (the whole claim)
`c(n) = f(n)` end-to-end, via one classification theorem.

## Skeleton (gap steps, NOT a finished proof)

1. **Import** Lemma G, pair-pile + mirror (the two certified equality
   realizations — `{1}` via mirror, `{2^j, 2^j+1}` via pair-pile), the
   `±a` n=1 real proof, the minimizer census (grid-empirical, n=3,4,5).
2. **GAP (the hard step — real-valued equality-case classification).** Prove
   over REALS: for Liu's level-`n` dyadic, `A = α(n)` iff the final multiset's
   odd-multiplicity pieces form `{1}` (one unpaired dyadic-unit) or
   `{2^j, 2^j+1}` (a consecutive-powers pair at the dyadic level boundary).
   Mechanism to name: the sliver-canceling `±a` flat polytope (Explorer 1) IS
   the real incarnation of this odd-mult structure — a sub-`α` fragment at a
   canceling odd rank is exactly the "leftover = 1" (in scaled units) of the
   odd-mult census. So the classification theorem = the flat-polytope
   characterization (shared with `cell-complex-l3`, flagged below).
3. **G1 closure.** For every real Xiang refinement of the dyadic, `A ≥ α(n)`
   (the classification gives `A = α` at the equality structure, and `A > α`
   off it — every non-equality config has its odd-mult leftover strictly
   larger than the dyadic-unit, by the superincreasing-R structure of the
   dyadic pieces). Mechanism: off the flat polytope, `A` is strictly
   increasing in every transverse direction (Explorer 1, n=3 verified 20/20).
4. **GAP (the G2 half — the honest wall).** Prove the equality structure is
   dyadic-Liu-locked: `A = α(n)` realizable ONLY when Liu's config is the
   dyadic. Then for non-dyadic Liu, Xiang forces `A < α(n)` (the sliver
   forcing of `two-regime-disjunctive`, derived here as the contrapositive of
   the equality classification). HONEST CAVEAT: this G2 half is the
   unique-extremum (U-E) global statement restated (Explorer 2 confirmed
   (U-E)'s global half IS G2 verbatim); the classification gives `A ≠ α` off
   the dyadic but the SIDE (`A < α` not `A > α`) needs the sliver forcing,
   which is not supplied by the classification alone. So the G2 half does
   NOT trivialize; it restates the gap with a cleaner target.
5. Conclude `c(n) = f(n)`: G1 from step 3, G2 from step 4 (with the sliver
   forcing as the open sub-step).

## Key lemmas (claim + one-line mechanism)
- Real equality-case classification — `A = α(n)` iff odd-mult leftover is
  `{1}` or `{2^j, 2^j+1}`, because the sliver-canceling `±a` flat polytope
  is exactly the real form of the odd-mult leftover = dyadic-unit.
- G1: non-equality ⇒ `A > α` — because off the flat polytope `A` is strictly
  increasing transversally (the dyadic's superincreasing R forces every
  non-canceling leftover to exceed the dyadic-unit).
- G2 (hard wall): equality is dyadic-Lui-locked — because the
  `{2^j, 2^j+1}` pair requires adjacent Liu pieces in exact ratio
  `2^j : 2^{j+1}` (dyadic), recursively at every level.

## Open gaps (builder fills)
- Step 2 (real-valued equality-case classification) — the load-bearing hard
  step; the grid census is empirical only.
- Step 4 (G2 sliver forcing from the classification's converse) — the honest
  wall; (U-E)'s global half restated, does NOT bypass G2.
- The SIDE argument for G2 (why `A < α` not `A > α` off the dyadic) — not
  supplied by the classification; needs the sliver mechanism (shared with
  `two-regime-disjunctive`).

## Cases to cover
- Odd-count minimizers (mirror family, `{1}`) and even-count minimizers
  (pair-pile family, `{2^j, 2^j+1}`) — both must fall out of the real
  classification.
- Non-dyadic Liu configs of every structural class (balanced, dominant,
  extreme-dominant) — the sliver forcing must handle all.

## Watch out for
- Shared-wall risk with `cell-complex-l3`: both lean on the sliver-canceling
  flat polytope as the equality locus. If the real characterization fails,
  both die together. Divergence: THIS approach aims for a structural theorem
  at all `n` directly (no cell enumeration); `cell-complex-l3` bounds a linear
  form per polytope (finite certificate per `n`). Flagged honestly.
- Shared-wall risk with `two-regime-disjunctive`: both use the equality-case
  classification as a load-bearing fact for G2. Divergence: THIS approach
  drops the regime-D/regime-N disjunctive split and attacks both gaps from
  one classification; `two-regime-disjunctive` stays within the disjunctive
  split (G2 only, G1 imported). If the real classification fails to lift,
  the G2 half of this approach AND `two-regime-disjunctive`'s regime-N engine
  die together — a genuine single-gap-trap risk, flagged.
- Do NOT claim the classification alone closes G2 — it gives `A ≠ α` off the
  dyadic, but the SIDE (`A < α`) needs the sliver forcing (the (U-E) global
  wall).
- The `M − total(R) = α(n+1)` identity is dyadic-only (foreclosed, A4) — do
  NOT retry a unified-potential.

## Prior progress imported
- Lemma G, pair-pile, mirror, ΔA, L*, U(2), grid-parity, `e_M ≤ o_R`
  reduction, self-compensation, CK, dyadic-ratio overshoot — all certified.
- The minimizer census (Explorer 3) — empirical equality-case target.
- The n=1 real `±a` proof — the base case for the flat-polytope
  characterization (step 2).
