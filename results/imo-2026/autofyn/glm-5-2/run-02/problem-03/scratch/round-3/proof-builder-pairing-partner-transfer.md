# Build summary — `pairing-partner-transfer` (round 3, Engine A)

## Outcome: DEAD-END (Engine A falsified), Status = partial

The assigned engine — extremal minimizer + non-improving 2-piece transfer
(crux `aimo-0119`), load-bearing claim "two-tail cancellation
`T_M + T_R ≤ 0`" — is FALSIFIED on n=3 brute force, exactly as the
reviewer warned it might be. Reported honestly; no faking.

## The falsification (exact rational arithmetic)

Level-3 dyadic `(1,2,4,8)/15`, all 232 Xiang responses enumerated on the
integer grid. Global min `A = 1/15 = α(3)` at 40 minimizers; k-distribution
`k=1: 7, k=2: 21, k=3: 12`.

For each of the 33 minimizers with k≥2 marks in `M = [7/15,1]`, I tested the
transfer's load-bearing claim `A(C') ≤ A(C*)` two ways:

| transfer version | `A' ≤ α(3)` | failures | best `A'` on failures |
|---|---|---|---|
| canonical (merge 2 smallest adjacent `M`-sub-pieces + bisect largest unsplit `R`-piece) | 14/33 | 19 | `2/15` |
| most permissive (any `M`-mark removed + new mark anywhere in `R`, 3000-pt grid) | 12/33 | 21 | `2/15` |

For 21/33 minimizers, NO single-pair transfer (one removal from M + one
addition in R) preserves minimality — best achievable `A' = 2/15` (strictly
above `α(3) = 1/15`). Concrete counterexample: `C* = {8/15, 2/3}`, `A = 1/15`;
every transfer gives `A' = 2/15`. The two `ΔA` tails ADD (not cancel) — the
same `−2T` tail-flip wall that killed per-mark induction (certified dead,
`lemma-delta-a-local-cut`). Engine A dies the same death.

## Cheap-kill route (CK + conjecture S) — also tested, partial-only

- **CK** (`A ≥ smallest piece` for odd piece-count): one-line PROVED lemma
  (decomposition into non-negative pair-excesses + last-piece leftover).
  Verified 0 violations on n=2 full grid (1378 odd-count configs) and n=3
  minimizers. Proposed for certification.
- **(S)** (`smallest piece ≥ α(n)` at minimizer): VERIFIED on n=2,3 brute
  force (0 violations, in fact equality `smallest = α(n)` at every minimizer)
  but UNPROVEN — it is itself a variational claim sharing the `−2T` wall.
  Covers only ODD-count minimizers; 18/40 n=3 minimizers are EVEN-count
  (incl. the pair-pile extremal), uncovered by CK + (S). Does not close G1.

## File written

`/home/agentuser/repo/results/imo-2026-03/approaches/pairing-partner-transfer.md`
Status: partial. Inherits pairing-partner's certified partial progress
(Lemma G, pair-pile, mirror, ΔA, L*, k=0, k=1, U(2), n=1,2 end-to-end);
does NOT advance G1 (Engine A dead; CK + (S) covers only odd-count
conditionally). G1 live attempt stays with sibling `pairing-partner`
(Engine C weight-function).

## Promotable lemma proposed

- **CK** (odd-count `A ≥ smallest piece`) — proved one-line; for
  certification at `lemmas/lemma-ck-odd-count.md`.

## Recommendation for next round

Do NOT re-dispatch Engine A / 2-piece transfer / two-tail-cancellation for
G1 — falsified. If pairing-partner's Engine C (weight-function) also hits the
`−2T` wall on the even-count sub-case, the outliner should field a G1
approach from a framing FAR from both (structural/topological on the sorted
multiset, or a probabilistic/averaging bound), as the reviewer's diversity
note already flagged.
