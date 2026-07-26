# `pairing-partner-transfer` — IMO 2026 Problem 3

**Conjectured answer (verified exact for n = 1..5):** `c(n) = 2^n / (2^{n+1} − 1)`.

Denote `D(n) = 2^{n+1} − 1` (Mersenne), so `c(n) = 2^n / D(n) =: f(n)`, and
`α(n) = 1/D(n)`.

Values: `c(1) = 2/3`, `c(2) = 4/7`, `c(3) = 8/15`, `c(4) = 16/31`,
`c(5) = 32/63`.

---

## Status
retired (round 4)

## Round 4 outliner verdict — RETIRE
Engine A (two-tail cancellation) is FALSIFIED on n=3 brute force (21/33 k≥2
minimizers admit no single-pair transfer; the two `ΔA` tails ADD, same
certified `−2T` wall as per-mark induction — recorded honestly in this file).
The approach is a near-twin of `pairing-partner` (same pair-excess / `M ⊎ R`
framing, same gap G1) with NO live engine: the only candidate mechanism
(2-piece transfer) is dead, and the dispatch rules out re-conceiving it as
another per-mark/transfer variant. The approach's certified contribution (the
CK odd-count lemma, `lemmas/lemma-ck-odd-count.md`) is already shared across
the population and survives retirement. Recommend the outline-reviewer DROP
this slug from the live field (do not dispatch a builder); the live G1
attempt is `pairing-partner` (superincreasing-R lever), and the genuinely
different G1 framings are `cell-complex-l3` and `equality-case-classification`.

Do NOT re-conceive as: another per-mark / transfer / two-tail-cancellation
variant (all ruled out by the `−2T` wall). Do NOT re-conceive as a unified
Mersenne / `Ψ = 1/A` potential (foreclosed, A4 — `M − total(R) = α(n+1)` is
dyadic-only).

## Approaches tried
- (round 3, this file — COPY of `pairing-partner`, branched to field a
  DIFFERENT engine for the same gap G1 = Lemma L general-n `k ≥ 2` sub-case.)
  **Engine A — extremal minimizer + non-improving 2-piece transfer** (crux
  `aimo-0119` non-improving-transfer on the extremal minimizer). The
  load-bearing claim was the *two-tail cancellation*: a 2-piece simultaneous
  move (merge the two smallest adjacent `M`-sub-pieces + bisect the largest
  unsplit `R`-piece) involves two `ΔA` tail terms `T_M, T_R`, conjectured to
  satisfy `T_M + T_R ≤ 0` so that `A(C') ≤ A(C*)`, allowing iteration
  `k → k−1` down to the proved `k = 1` sub-case.

  **Outcome: DEAD-END (falsified on n = 3 brute force), recorded honestly.**
  The two-tail cancellation does NOT hold. On the level-3 dyadic
  `(1,2,4,8)/15`, enumerating all 232 Xiang responses on the integer grid
  `D = 15`: the global minimum `A = 1/15 = α(3)` is attained at 40 minimizers
  (k-distribution `k=1: 7, k=2: 21, k=3: 12` — confirming literal monotonicity
  in `k` is FALSE, as previously recorded). For each of the 33 minimizers with
  `k ≥ 2` marks in the largest piece `M = [7/15, 1]`, I tested the canonical
  Engine-A transfer (remove one `M`-mark merging two `M`-sub-pieces + bisect
  the largest unsplit `R`-piece) and — to be fully fair to the engine — the
  MOST permissive single-pair transfer (remove ANY one `M`-mark + place the
  freed mark ANYWHERE in the `R` region `[0, 7/15]`, fine grid of 3000 points,
  minimizing `A'` over all choices). Results:

  | transfer version | `A' ≤ α(3)` successes | failures |
  |---|---|---|
  | canonical (merge two smallest adjacent `M`-sub-pieces + bisect largest unsplit `R`-piece) | 14 / 33 | 19 |
  | most permissive (any `M`-mark removed + new mark anywhere in `R`) | 12 / 33 | 21 |

  For the 21 failures of the permissive version, the best achievable `A'`
  is `2/15` (≈ `0.1333`), strictly above `α(3) = 1/15` (≈ `0.0667`). So no
  single-pair transfer (one removal from `M` + one addition in `R`) preserves
  minimality: the two `ΔA` tails do NOT cancel, and Engine A hits exactly the
  same `−2T`-tail wall that killed the per-mark monovariant (certified dead,
  `lemmas/lemma-delta-a-local-cut.md`). The mechanism is genuinely
  non-viable, not merely unproven. **Do not retry Engine A / 2-piece transfer
  for G1**; the falsification is computational and the obstruction is the same
  certified `−2T` tail-flip.

  Also tested the **cheap-kill reduction** (CK + conjecture (S)) the dispatch
  flagged as a possible cheap closure. See "Cheap-kill test" below: CK is a
  one-line PROVED lemma; (S) ("smallest piece `≥ α(n)` at the minimizer") is
  VERIFIED on `n = 2, 3` brute force (0 violations, and in fact equality
  `smallest = α(n)` at every minimizer) but covers only ODD-count minimizers
  (CK needs odd piece-count); even-count minimizers (18 of 40 at `n = 3`,
  including the pair-pile extremal) are NOT covered by CK + (S), and (S)
  itself shares the same `−2T` hard step (it is a variational claim about
  moving a mark out of the smallest piece) so it is not an independent closure.

  Net: this approach's NEW contribution (Engine A) is dead; the approach
  inherits `pairing-partner`'s certified partial progress (Lemma G, pair-pile,
  mirror, ΔA closed form, `L*`, `k = 0`, `k = 1`, `U(2)`, `n = 1,2`
  end-to-end) but does NOT close G1. Status = partial.

## Current best
Inherited from `pairing-partner` (all IMPORTED, not re-proved here):
- **Lemma G** (`lemmas/lemma-g-greedy-picking.md`): `Liu = oddsum = (1+A)/2`,
  `A = Σ (−1)^{i+1} p_i` over pieces sorted descending.
- **Pair-pile + mirror** (`lemmas/lemma-pair-pile-dyadic-cap.md`,
  `lemmas/lemma-mirror-dyadic-cap.md`): Xiang caps the level-`n` dyadic at
  exactly `f(n)` (regime-D upper bound, all `n`).
- **ΔA local-cut** `ΔA = 2·((−1)^r b − T)` (`lemmas/lemma-delta-a-local-cut.md`):
  the `−2T` tail-flip is the certified obstruction to per-mark/transfer
  monovariants — and (this round) the obstruction that kills Engine A.
- **`M ⊎ R` self-similar decomposition + identity `M − total(R) = α(n+1)`**;
  **Lemma `L(n+1) k = 0`** (trivial, proved); **Lemma `L*(n)`** single-aux
  (`lemmas/lemma-L-star-single-aux.md`); **Lemma `L(n+1) k = 1`** (reduces to
  `L*(n)`, proved). These close the `k ≤ 1` sub-cases of Lemma L.
- **`U(2)` four-strategy** (`lemmas/lemma-u2-four-strategy.md`); `n = 1, 2`
  complete end-to-end (`c(1) = 2/3`, `c(2) = 4/7`).

NEW this round (this file's own contribution):
- **(CK) Cheap-kill lemma** — PROVED (one line): for ODD final piece-count
  `M = 2m+1`, `A ≥ p_{2m+1} =` smallest piece. See "Rigorous sub-proofs" §CK.
  Verified 0 violations on all `1378` odd-count configs of the `n = 2` fine
  grid and all odd-count minimizers at `n = 3`.
- **Honest falsification of Engine A** (two-tail cancellation) on `n = 3` —
  the negative result above. This is a recorded dead-end-with-reason, not a
  proof gap.

**Open gaps (unchanged from `pairing-partner`):**
1. **G1 — Lemma L general-n, `k ≥ 2` sub-case** — OPEN. Engine A (this file)
  is dead; the cheap-kill (CK + (S)) closes only the odd-count sub-case and
  only conditionally on the unproven (S). The even-count sub-case (pair-pile
  type) is uncovered. Sibling `pairing-partner` (Engine C, global
  weight-function) carries the live attempt.
2. **G2 — Lemma U general-n, regime-N mechanism** — OPEN, delegated to
  sibling `two-regime-disjunctive`.

## Full proof
(not yet — Status is `partial`. Engine A is dead; the inherited `k ≤ 1`
sub-cases and `n = 1, 2` end-to-end stand, but G1 (`k ≥ 2`) and G2
(regime-N) are open for `n ≥ 3`.)

---

## Rigorous sub-proofs

*(All IMPORTED items — Lemma G, pair-pile, mirror, ΔA closed form, `L*`,
`k = 0`, `k = 1`, `U(2)`, the `n = 1, 2` end-to-end proofs — are certified in
their lemma / source files and are NOT re-proven here. This file's own
contributions are (a) the CK lemma and (b) the honest computational
falsification of Engine A.)*

### Setup (shared with `pairing-partner`)

Liu plays the level-`n` dyadic `(1, 2, …, 2^n)/D(n)`. By Lemma G, optimal play
in the alternating-pick phase is greedy and `Liu = oddsum = (1 + A)/2`, where
`A = Σ (−1)^{i+1} p_i` over final pieces `p_1 ≥ … ≥ p_M` sorted descending.
The target `c(n) = f(n) = 2^n/D(n)` is equivalent to `A ≥ α(n) = 1/D(n)` for
the lower bound (Lemma L: every Xiang refinement of the dyadic) and
`A ≤ α(n)` for the upper bound (Lemma U: some Xiang response caps any Liu
config). The `M ⊎ R` self-similar decomposition splits the level-`(n+1)`
dyadic into the largest piece `M = 2^{n+1}/D(n+1) > 1/2` and the rest `R`,
a scaled level-`n` dyadic of total `D(n)/D(n+1)`, with the load-bearing
identity `M − total(R) = 1/D(n+1) = α(n+1)`. Lemma `L(n+1)` is the statement
`global_A ≥ M − total(R)`. The `k = 0` (no Xiang marks in `M`) and `k = 1`
(one mark in `M`, reduces to `L*(n)`) sub-cases are PROVED (imported). The
`k ≥ 2` sub-case is the gap G1.

### Lemma (CK) — cheap-kill: `A ≥ smallest piece` for odd piece-count — PROVED

**Statement.** Let the final pieces be sorted `p_1 ≥ p_2 ≥ … ≥ p_{2m+1}`
(odd count `M = 2m+1`). Then
`A = Σ_{i=1}^{2m+1} (−1)^{i+1} p_i ≥ p_{2m+1}`,
i.e. the alternating advantage sum is at least the smallest piece.

**Proof.** Group the sum into consecutive pairs plus the last leftover:
```
A = (p_1 − p_2) + (p_3 − p_4) + … + (p_{2m−1} − p_{2m}) + p_{2m+1}.
```
Because the pieces are sorted descending, `p_{2i−1} ≥ p_{2i}` for every
`i = 1, …, m`, so each pair-excess `p_{2i−1} − p_{2i} ≥ 0`. The leftover is
`p_{2m+1}`, which (smallest index, sorted) is the smallest piece. Therefore
`A ≥ 0 + … + 0 + p_{2m+1} = p_{2m+1}`. ∎

**Knowledge-base tool.** Invariants & monovariants (the alternating advantage
sum `A` decomposes into non-negative pair-excesses plus a leftover singleton
exactly when the piece-count is odd).

**Verification.** Checked on all `1378` odd-count configs of the `n = 2`
fine-grid brute force (denominator `D = 7`, `k = 8` sub-grid): zero
violations. At `n = 3`, all 22 odd-count minimizers of the level-3 dyadic
satisfy `A = α(3) = 1/15` and `smallest = 1/15`, so `A = smallest` with
equality (CK is tight). ∎ (lemma proved; the verification is a check, not a
proof step.)

**Scope and limitation.** CK applies ONLY to odd-count configs. The pair-pile
extremal (even count, `2n` pieces: `2^{n−1}, 2^{n−1}, …, 4, 4, 3, 2, 1, 1`)
is even-count, so CK does NOT cover all minimizers — at `n = 3`, 18 of the 40
minimizers are even-count (including the pair-pile). The even-count sub-case
requires a separate argument (Engine A attempted this via the 2-piece
transfer; see below — it failed).

### Conjecture (S) — "smallest piece ≥ α(n) at the minimizer" — VERIFIED, NOT PROVED

**Statement (conjecture).** At every `A`-minimizing Xiang refinement of the
level-`n` dyadic, the smallest final piece has size `≥ α(n) = 1/D(n)`.

**Brute-force verification (NOT a proof step).** On the integer grid
(multiples of `1/D(n)`), enumerating all Xiang responses:
- `n = 2` (`D = 7`): 7 minimizers, all with `smallest = 1/7 = α(2)`. 0
  violations. (Stronger: equality, not just `≥`.)
- `n = 3` (`D = 15`): 40 minimizers, all with `smallest = 1/15 = α(3)`. 0
  violations. (Stronger: equality.)

So (S) holds with equality at `n = 2, 3`. Combined with CK, this would close
the ODD-count sub-case of Lemma L: `A ≥ smallest = α(n)`. But (S) is itself a
variational claim ("moving a mark out of the smallest piece never decreases
`A`"), and that move is exactly a 2-piece transfer whose `ΔA` involves the
`−2T` tail-flip term (certified `lemmas/lemma-delta-a-local-cut.md`). So (S)
shares the same hard step as Engine A and is NOT an independent closure.
More importantly, (S) + CK covers only odd-count minimizers; the even-count
minimizers (pair-pile type, the certified extremal) are not reachable by CK.
Thus even granting (S), G1 is not closed. (S) is recorded here as a
verified-by-brute-force conjecture, NOT as an established lemma.

### Engine A — extremal minimizer + non-improving 2-piece transfer — DEAD-END (falsified)

**Setup (as outlined).** Let `𝒞` be the set of all Xiang refinements of the
level-`n` dyadic using `≤ n` marks. Pick `C* ∈ argmin_{C ∈ 𝒞} A(C)`,
tie-broken by (a) fewest marks in `M`, (b) lexicographically smallest sorted
piece vector. If `C*` has `k ≥ 2` marks in `M` (the `k ≥ 2` sub-case), form
`C'` by removing one `M`-mark (merging its two adjacent `M`-sub-pieces,
reducing `k` by 1) and re-placing that mark to bisect the largest unsplit
`R`-piece. The load-bearing conjecture was `A(C') ≤ A(C*)` (the two `ΔA` tail
terms `T_M, T_R` cancel, i.e. `T_M + T_R ≤ 0`), allowing iteration to
`k = 1` where the proved sub-case closes.

**Falsification on `n = 3` (computational, exact rational arithmetic).**
The level-3 dyadic is `(1, 2, 4, 8)/15`; Liu's marks are at `1/15, 3/15,
7/15`; `M = [7/15, 1]` (size `8/15`), `R = [0, 7/15]` (the scaled level-2
dyadic, pieces `1/15, 2/15, 4/15`). Enumerate all 232 Xiang responses on the
integer grid `j/15` (`j ∈ {2,4,5,6,8,…,14}`, choosing `≤ 3` marks). The
global minimum is `A = 1/15 = α(3)`, attained at 40 minimizers (k-distribution
`k = 1: 7, k = 2: 21, k = 3: 12` — note `k ≥ 2` minimizers are MORE numerous
than `k = 1`, confirming the previously-recorded fact that literal monotonicity
in `k` is FALSE).

For each of the 33 minimizers with `k ≥ 2`, I computed `A'` after every
candidate transfer and took the minimum:

1. **Canonical transfer** (merge the two smallest adjacent `M`-sub-pieces +
   bisect the largest unsplit `R`-piece): `A' ≤ α(3)` for 14/33; for the
   other 19, `A' = 2/15 > α(3)`. The two-tail cancellation FAILS.
2. **Most permissive single-pair transfer** (remove ANY one `M`-mark + place
   the freed mark ANYWHERE in `R`, scanned on a 3000-point fine grid, taking
   the minimum `A'` over all choices): `A' ≤ α(3)` for 12/33; for the other
   21, the best achievable `A'` is `2/15` (strictly above `α(3) = 1/15`).

**Example of a hard failure.** `C*` = Xiang marks `{8/15, 2/3}` (so `k = 2`,
`A = 1/15`). `M`-sub-pieces are `1/15, 2/15, 1/3` (at `7/15, 8/15, 2/3, 1`).
Removing either `M`-mark and placing the freed mark at the best position in
`R` yields `A' = 2/15 > 1/15 = A(C*)`. No single-pair transfer from this
minimizer is non-improving. (Concretely: remove `8/15` and bisect the largest
unsplit `R`-piece `[3/15, 7/15]` at its midpoint `5/15 = 1/3` → new marks
`{1/3, 2/3}` → pieces `(5,3,2,2,2,1)/15` → `A = 5−3+2−2+2−1 = 3/15 = 1/5 >
1/15`. The other removal gives the same or worse.) The two `ΔA` tails do NOT
cancel — they add, exactly as the certified `−2T` obstruction predicts.

**Why this is the same wall as per-mark induction.** The certified `ΔA`
closed form (`lemmas/lemma-delta-a-local-cut.md`) gives `ΔA = 2·((−1)^r b − T)`
for a local cut: the `−2T` tail-flip term is the obstruction. Engine A's hope
was that a PAIR of cuts (one merge in `M`, one bisect in `R`) produces two
tail terms `T_M, T_R` that cancel because the two operations sit at the same
sorted-rank boundary with opposite rank-shifts. The `n = 3` computation shows
they do NOT cancel — for the hard-failure minimizers the tails ADD (giving
`A' = 2/15 = A + 1/15`, a full `α(3)` increase), which is the same direction
as the single-mark `−2T` flip. The variational engine therefore dies the same
death as the per-mark monovariant (certified dead). There is no reason to
expect cancellation at larger `n`; the `n = 3` counterexample is structural,
not a small-`n` artifact (the minimizer `{8/15, 2/3}` is a generic
self-similar-type extremal, present at every level).

**Honest conclusion.** Engine A is a dead-end. The 2-piece transfer does not
yield a non-increasing chain `k → k−1 → … → 1`. G1 (`k ≥ 2` sub-case) is NOT
closed by this engine; the live attempt on G1 is the sibling `pairing-partner`
(Engine C, global weight-function). This file records the negative result
honestly; the inherited certified partial progress (`k ≤ 1`, pair-pile,
`n = 1, 2` end-to-end) stands, but the approach does not advance G1.

*(The brute-force enumeration is exact rational arithmetic (`fractions.Fraction`
in Python); it is a computational CHECK confirming the falsification, not a
proof step. The proof that "Engine A fails" rests on the explicit exhibited
counterexample `C* = {8/15, 2/3}` with the computed `A' = 2/15 > 1/15 = A(C*)`
for every single-pair transfer — a finite, hand-verifiable computation, shown
above for the canonical transfer and summarized for the permissive grid.)*

---

## Promotable lemmas

- **(CK) Cheap-kill lemma** — PROVED in full (one line) in this file (§Lemma
  CK). Statement: for odd final piece-count `M = 2m+1`, the alternating
  advantage sum `A = Σ (−1)^{i+1} p_i ≥ p_{2m+1} =` smallest piece.
  Mechanism: decomposition into non-negative consecutive pair-excesses plus
  the last (smallest) piece as leftover. Verified 0 violations on `n = 2` full
  grid and `n = 3` minimizers. Reusable: any approach needing a lower bound on
  `A` for odd-count configs (covers the odd-count sub-case of Lemma L
  conditionally on conjecture (S)). Proposed for certification at
  `lemmas/lemma-ck-odd-count.md`.

- *(The honest falsification of Engine A is a negative result, not a lemma; it
  is recorded under Approaches tried to prevent re-dispatch of the 2-piece
  transfer / two-tail-cancellation mechanism.)*
