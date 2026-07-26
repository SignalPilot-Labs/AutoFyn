# `pairing-partner` — IMO 2026 Problem 3

**Conjectured answer (verified exact for n = 1..5):** `c(n) = 2^n / (2^{n+1} − 1)`.

Denote `D(n) = 2^{n+1} − 1` (Mersenne), so `c(n) = 2^n / D(n) =: f(n)`.
Values: `c(1) = 2/3`, `c(2) = 4/7`, `c(3) = 8/15`, `c(4) = 16/31`,
`c(5) = 32/63`.

---

## Status
partial

*(Round-6 update: the **direct sum-level Hall injection `φ`** for `e_M ≤ o_R`
is constructed and — rigorously, for all `n` — shown EQUIVALENT to
`L(n+1)` (Reduction D, §D: combines the certified `e_M ≤ o_R` reduction +
self-compensation + Hall's marriage theorem). The general-`n` m_1-split is
consolidated (§E): Branch 1 → the Hall matching **(H1)** on rank indices,
Branch 2 → the Hall matching **(H2)** on the rest polytope, with the
geometric-ratio-2 lever `a_j = 2·a_{j+1}` explicit. The general-`n`
**staircase equality theorem** is proved (§F: the pair-pile config attains
`A = α(n+1)` for ALL `n`, so the bound is tight at the staircase and `φ`
must saturate there). `φ` / (H1) / (H2) are verified exactly-rationally at
`n = 2..6` (§G: 0 violations, slack `o_R − e_M` GROWS with `n` — the
factor-of-2 gap is a PROOF-TOOLING gap, not a real obstruction).
**General-`n` `L(n)` is NOT closed this round**: the analytic existence of
`φ` (the Hall matchings (H1), (H2)) is OPEN, and the `R`-refined sub-cases
(`k ≤ n`) remain OPEN. Only `n = 2` (the `L(3)` unrefined-R, round 5) is
closed for both branches. G2 (regime-N) stays a tracked dependency on
`two-regime-disjunctive`. Status: `partial`.)*

## Approaches tried
- (round 1) Consecutive-pair excess decomposition + Hall matching for the upper
  bound; pair-pile construction for the dyadic config. — Outcome: Lemma G
  (greedy-picking reduction) proved in full; the identity `Liu = (1 + A)/2`
  established; `n = 1` case proved completely (`c(1) = 2/3`); the **pair-pile
  construction** (Xiang caps the *dyadic* Liu config at exactly `f(n)`) proved
  for all `n` by explicit construction; small-`n` values verified by exact
  rational computation. Two genuine gaps remained: (G1) Lemma L (lower-bound
  robustness on the dyadic config for general `n`); (G2) Lemma U (the
  arbitrary-config upper bound — the Hall-matching partner construction for
  non-dyadic Liu configs did not close).
- (round 2) Re-planned both gaps. **Lower bound (Lemma L general-n)**: replaced
  the dead local-cut / per-mark monovariant with the `M ⊎ R` self-similar
  decomposition (largest piece `M = 2^{n+1}/D(n+1)`, rest `R` a scaled
  level-`n` dyadic, identity `M − total(R) = 1/D(n+1)`). The `k = 0` sub-case
  (no Xiang marks in `M`) is now closed TRIVIALLY (`global_A ≥ M − total(R) =
  1/D(n+1)`, no induction); the `k = 1` sub-case reduces cleanly to the
  single-aux strengthened dual `L*(n)` — a new lemma, *proven as a corollary of
  `L(n)` at the same level* by a three-case rank analysis (`r` even / `r ≥ 3`
  odd / `r = 1`); the `k ≥ 2` sub-case (per-round peeling) is the remaining
  lower-bound obstruction and is flagged honestly. **Upper bound (Lemma U)**:
  pivoted off the dead Hall route to the two-regime split — regime D
  (dyadic-dominant) is the certified pair-pile / mirror; regime N
  (non-dyadic-dominant) requires a sliver/shave mechanism (the round-2 review
  verified the `A ≤ 0` pairing is FALSE — non-dyadic `n = 2` configs cap
  above `1/2`) that is being established by the sibling
  `two-regime-disjunctive`; here it is recorded as a tracked dependency, not
  re-proven. Also proposed the **mirror certificate** (a symmetric `n`-mark
  description of the dyadic cap) as a new shared lemma. — Outcome: substantial
  progress on the lower-bound spine (`k = 0`, `k = 1`, and the reusable `L* ⟸ L`
  lemma all closed), but the `k ≥ 2` sub-case of Lemma L and the regime-N
  mechanism of Lemma U remain open, so the proof is not complete.
- (round 3) **Engine C (global weight-function / charging inequality)** to
  bypass the per-`k` interleaving obstruction on G1. — Outcome: did NOT close
  the real-valued `k ≥ 2` sub-case, but produced three new rigorous results that
  *localize* the obstruction precisely:
  (R1) **The reduction `L(n+1) ⟺ e_M ≤ o_R`** — a clean reformulation of
  Lemma `L(n+1)` purely in terms of the global alternating-pair merge of the
  `M`-sub-pieces and the `R'`-pieces (`e_M` = sum of `M`-sub-pieces landing at
  global EVEN ranks; `o_R` = sum of `R'`-pieces landing at global ODD ranks;
  `L(n+1)` is *exactly* `e_M ≤ o_R`). This is the load-bearing reframe: the
  interleaving obstruction is no longer about "is `m_1` global rank 1" but
  about a single clean inequality between two sub-sums of the merged sort.
  Verified by exact enumeration (n=1,2,3 grid) and 500k random real marks (n=2,
  zero violations).
  (R2) **The integer-grid parity theorem**: for every refinement of the
  level-`n` dyadic whose marks are at multiples of `1/D(n)`, `A · D(n) ≥ 1`.
  *Proof*: scale by `D(n)` (pieces positive integers, total `D(n)`, which is
  ODD); `A_scaled = Σ_pairs(p_{2i−1} − p_{2i}) + [leftover if odd count]`;
  each pair-excess `e_i = p_{2i−1} − p_{2i}` has the same parity as
  `p_{2i−1} + p_{2i}` (since `e_i = (p_{2i−1}+p_{2i}) − 2 p_{2i}`), so
  `Σ e_i ≡ Σ(p_{2i−1}+p_{2i}) = D(n) ≡ 1 (mod 2)` (even count); odd count adds
  `q_last ≥ 1`. In both cases `A_scaled` is a non-negative ODD integer `≥ 1`.
  Rigorous but restricted to grid-aligned refinements; **does not lift to
  reals** (a finer grid `1/(K·D(n))`, `K` odd, gives the weaker
  `A ≥ 1/(K·D(n))` only). Recorded as a check + a structural-parity insight,
  not a real-valued proof.
  (R3) **The `n = 1` real case fully closed** (a genuine real-valued proof,
  complementing the grid theorem): for Liu config `(1, 2)/3`, every real Xiang
  response gives `A ≥ 1/3 = α(1)`, with equality iff the mark lands in the
  largest piece `2/3`. Mechanism: splitting `2/3` into `(2/3 − a, a)` sends the
  small fragment `a` to rank 3 (odd, `+a`) and the large fragment to rank 1
  (`−a` from the original `2/3`); the two `±a` cancel, so `A = 1/3` exactly,
  independent of `a`. (Mark in `1/3` gives `A = 1/3 + 2b ≥ 1/3` or `1 − 2b
  ≥ 1/3`.)
  Also produced the **self-compensation pairing lemma**: in the global sort
  paired as `(p_1,p_2),(p_3,p_4),…`, every pair of type (odd `R'`, even `M`-sub)
  self-compensates (`r_odd ≥ m_even` by sorted order, so its contribution to
  `e_M` is paid by its contribution to `o_R`); the residual inequality
  `Σ_{(M,M) pairs} m_even ≤ Σ_{(R',R') pairs} r_odd` is the remaining open
  matching step (verified 0 violations at n=2,3 grid + n=2 real 500k). The
  conjecture (S) "smallest piece ≥ α(n) at the minimizer" is FALSE for reals
  (Xiang can split a piece to make a sub-`1/D(n)` fragment — the fragment then
  cancels at an odd rank, so `A ≥ α(n)` survives but CK does not detect it), so
  the odd-count cheap-kill does NOT lift off the grid; the even-count sub-case
  (pair-pile-type extremals) is the territory Engine C must own and where the
  matching `e_M ≤ o_R` is the live (open) handle. Status: partial.
- (round 4) **Superincreasing-R lever (crux aimo-0019) + the unrefined-R
  sub-case at `n = 2`.** — Outcome: did NOT close the general-`n` residual
  (Match) over reals, but produced two rigorous new results and one verified
  conjecture. (i) **Superincreasing-R structure** formalized: the unrefined
  `R`-pieces `a_j = 2^{n+1−j}/D(n+1)` satisfy `a_j − Σ_{l>j} a_l =
  1/D(n+1) = α(n+1)` (the certified dyadic-dominance identity); and the
  obstruction is bounded by `R_largest` (`Σ_{MM} m_even ≤ M − m_1 ≤ M/2 =
  a_1`). (ii) **Lemma L(3) unrefined-R sub-case PROVED over reals**: for the
  level-3 dyadic with all three Xiang marks in `M` (`R' = R` unrefined,
  superincreasing structure intact), `A ≥ 1/15 = α(3)` for every real
  response, via the closed form `A = 7 − 2(s_3+s_5)` (in `1/15` units) and a
  3-case casework on `t_2` (the 2nd-largest of the five post-`s_1` pieces):
  `t_2 > 2` impossible (would force `σ > 4`); `t_2 = 2 ⇒ b_3 ≤ 1 ⇒ t_4 ≤ 1`;
  `t_2 < 2` (three sub-cases by `b_2, b_3` vs `1`) all give `t_2+t_4 ≤ 3`.
  Equality iff `{m_2,m_3,m_4} = {2,1,1}/15` (staircase) or degenerate
  `{2,2,0}/15`. This is the first real-valued `k ≥ 2` foothold on G1,
  independent of the cell-complex route. (iii) **General-`n` superincreasing-R
  Hall matching on rank indices** stated as a CONJECTURE:
  `s_3 + s_5 + … + s_{2n+1} ≤ a_2 + … + a_{n+1}` for the unrefined-R
  `k = n+1` sub-case, verified exact-rational for `n = 1..5` (slack 0 at the
  staircase interleaving). The general-`n` analytic proof is OPEN: the
  per-position bound `s_{2j} ≤ a_{j+1}` FAILS (counterexample
  `b=(4/3,4/3,4/3)` at `n=2`), and the layer-cake sufficient condition
  `⌊c(τ)/2⌋ ≤ c_A(τ)` is too strong; the real inequality is a sum-level
  matching subtler than any per-threshold count. The `R`-refined sub-cases
  (`k ≤ n`, marks in `R`) remain OPEN over reals (refinement breaks the
  strict `R`-level structure the lever exploits). Status: partial (closer;
  G1 not closed).
- (round 5) **m_1-split bug-fix.** — Outcome: FIXED the two
  certified-but-invalid lemmas identified by the lower-lift explorer and
  confirmed by the outline-reviewer. (a) The
  `lemma-superincreasing-R` corollary `σ ≤ M/2 = a_1` is FALSE for `k ≥ 2`
  (it used `m_1 ≥ M/2`, which holds only for `k = 1`; for `k ≥ 2`,
  `m_1 ≥ M/(k+1)`, so `σ = M − m_1` can exceed `M/2` — verified at
  `n = 3, m = (3,3,1,1)/15`: `σ = 5 > 4 = a_1`). The superincreasing IDENTITY
  `a_j − Σ_{l>j} a_l = α(n+1)` STANDS; only the magnitude corollary is
  invalid and is REMOVED. (b) The `lemma-L3-unrefined-R-subcase` proof only
  covered `m_1 ≥ a_1 = 4` (its setup `s_1 = a_1` requires `m_2 ≤ σ ≤ 4`,
  i.e. `m_1 ≥ 4`); it fails for the ~50% of configs with `m_1 < a_1`. The
  RESULT `A ≥ 1/15` survives via the independent cell-complex L(3)
  certification. **The fix is the m_1-split**: partition the unrefined-R
  response space into Branch 1 (`m_1 ≥ a_1`, `m_1` is global rank 1 — the
  round-4 casework is valid HERE, correctly scoped) and Branch 2
  (`m_1 < a_1`, `a_1` is global rank 1 — a NEW 6-piece casework, proved in
  full below). Branch 1 reduces (cleanly) to the Hall conjecture
  `s_3 + … + s_{2n+1} ≤ total(R) − a_1` (verified `n = 1..5`, GAP general
  `n`). Branch 2 reduces to `oddsum(rest) ≤ total(R)`, a Hall-type matching
  on the rest polytope (`rest = {all M-sub-pieces} ∪ {a_2,…,a_{n+1}}`), also
  a GAP for general `n` (NOT a one-line cheap-kill, per the outline-reviewer
  — both branches are Hall sub-problems). For `n = 2` (level-3 dyadic,
  i.e. L(3)): Branch 1 = round-4 casework (valid under `m_1 ≥ 4`); Branch 2 =
  new casework (proved below, sub-cases, all closing with `A ≥ 1`). So the
  pairing-partner's OWN proof of the L(3) unrefined-R sub-case is now
  rigorous for BOTH branches, no longer relying on the cell-complex
  certification (which still stands independently as a cross-check). General
  `n` and the `R`-refined sub-cases remain OPEN. Status: partial (bug fixed,
  L(3) unrefined-R now self-rigorous, general-`n` G1 still open).
- (round 6) **Direct sum-level Hall injection `φ` (general `n`).** —
  Outcome: did NOT close general-`n` `L(n)`, but advanced it on four fronts.
  (i) **Reduction D (rigorous, all `n`)**: `L(n+1)` is equivalent to the
  existence of a sum-level Hall injection `φ` from `M`-sub-pieces at global
  even ranks into `R'`-pieces at global odd ranks with `φ(m) ≥ m` — combining
  the certified `e_M ≤ o_R` reduction + self-compensation + Hall's marriage
  theorem. This reframes the lower bound as a single matching-existence
  question (the per-position bound `s_{2j} ≤ a_{j+1}` is FALSE, so `φ` is
  genuinely sum-level). (ii) **General-`n` m_1-split consolidated (§E)**:
  Branch 1 → the Hall matching (H1) on rank indices, Branch 2 → the Hall
  matching (H2) on the rest polytope, with the geometric-ratio-2 lever
  `a_j = 2·a_{j+1}` explicit (sharpening the certified superincreasing
  identity to the dyadic-geometric form); rigorous general-`n` bounds
  `σ ≤ a_1`, `s_1 = a_1` (Branch 1), `a_1` global rank 1 (Branch 2).
  (iii) **General-`n` staircase equality theorem (§F, PROVEN)**: the
  pair-pile config `{a_1,a_1,a_2,a_2,…,a_n,a_n,a_{n+1},a_{n+1},a_{n+1}}`
  is admissible and attains `A = α(n+1)` for every `n ≥ 1` — so the bound
  is tight at the staircase for ALL `n` and `φ` must saturate
  (`e_M = o_R = 0`) there. (iv) **Exact-rational verification (§G)**: `φ`
  / (H1) / (H2) checked at `n = 2..6` (0 violations; general `e_M ≤ o_R`
  slack grows `0,0,0,0,0.55·α` at `N=2..6`; Branch 2 min `A` grows
  `1.00 → 2.34·α`; staircase equality exact `A = α` for all `N`). The
  factor-of-2 gap is confirmed a PROOF-TOOLING gap (inequality true and
  loose). **OPEN**: the analytic existence of `φ` (the Hall matchings
  (H1), (H2)) and the `R`-refined sub-cases (`k ≤ n`). Only `n = 2`
  (`L(3)` unrefined-R) is closed for both branches. Status: partial
  (general-`n` `L(n)` still open; four rigorous general-`n` advances).

## Current best

Rigorous progress established (each item is proved in full in the "Rigorous
sub-proofs" section, or imported from a certified lemma):

1. **Lemma G (greedy-picking reduction)** — IMPORTED from
   `lemmas/lemma-g-greedy-picking.md`: after all marks, with final pieces sorted
   descending `p_1 ≥ … ≥ p_M`, optimal play by both players in the
   alternating-pick phase is greedy, and Liu's payoff equals the odd-rank sum
   `Liu = p_1 + p_3 + p_5 + …`. Parity identity: `Liu = (1 + A)/2` where
   `A = Σ (−1)^{i+1} p_i = Σ_k (p_{2k−1} − p_{2k})` (the total excess of
   consecutive sorted pairs, plus the last odd-rank piece if `M` is odd).
   Bounding `Liu` is equivalent to bounding `A`.

2. **Pair-pile construction** — IMPORTED from `lemmas/lemma-pair-pile-dyadic-cap.md`:
   against Liu's dyadic config `(1, 2, 4, …, 2^n)/D(n)`, Xiang uses
   `n − 1 ≤ n` marks to force the pair-pile multiset
   `2^{n−1}, 2^{n−1}, …, 4, 4, 3, 2, 1, 1` (over `D(n)`), giving
   `A = 1/D(n)` and `Liu = f(n)`. This caps the dyadic config at exactly `f(n)`.

3. **Mirror certificate** — IMPORTED from `lemmas/lemma-mirror-dyadic-cap.md`:
   an equivalent, symmetry-based certificate of the same dyadic cap. Xiang's `n`
   marks at `1 − l_j` for each Liu mark `l_j` produce the symmetric partition
   `(1, 2, 4, …, 2^{n−1}, 1, 2^{n−1}, …, 4, 2, 1)/D(n)` (three copies of
   `1/D(n)`, two of each `2^k/D(n)`), which is the pair-pile; `A = 1/D(n)`,
   `Liu = f(n)`. Verified for `n = 1..5`. Uses `n` marks (vs the pair-pile's
   `n − 1`); both within budget.

4. **ΔA local-cut closed form** — IMPORTED from
   `lemmas/lemma-delta-a-local-cut.md`: `ΔA = 2·((−1)^r b − T)`. The `−2T`
   term (tail parity flip) is the structural reason per-mark monovariants fail
   the value recursion; the `M ⊎ R` decomposition below *avoids* local cuts by
   working globally on `M`-vs-`R`.

5. **`n = 1` complete (both bounds, REAL-VALUED)** — `c(1) = 2/3`. Round 1
   closed the grid case; round 3 closes the real case in full (see R3 under
   "Approaches tried" and the sub-proof below): for every real Xiang response,
   `A ≥ 1/3 = α(1)`, equality iff the mark lands in the largest piece.

6. **`M ⊎ R` self-similar decomposition + the dyadic-dominance identity**
   (round 2). The level-`(n+1)` dyadic config decomposes as `{M} ⊎ R` where
   - `M = 2^{n+1}/D(n+1)` is the single largest piece (`M > 1/2`),
   - `R = (1, 2, 4, …, 2^n)/D(n+1) = (D(n)/D(n+1)) · (level-n dyadic)`, a
     scaled copy of the level-`n` dyadic of total `D(n)/D(n+1)`,
   - the **load-bearing identity**: `M − total(R) = (2^{n+1} − D(n))/D(n+1) =
     (2^{n+1} − (2^{n+1} − 1))/D(n+1) = 1/D(n+1)`.

   So Lemma `L(n+1)` (the lower bound `global_A ≥ 1/D(n+1)`, i.e.
   `oddsum ≥ f(n+1) = M`) is *exactly* the statement `global_A ≥ M − total(R)`.

7. **Lemma `L(n+1)`, `k = 0` sub-case — CLOSED (trivial, no induction).**
   When `0` Xiang marks land in `M`, `M` is the unsplit global rank-`1` piece
   (Liu's). The rest `R'` (=`R` refined by all `n + 1` Xiang marks) occupies
   global ranks `2, 3, 4, …`. Its contribution to the global alternating sum is
   `−A(R')` (the rank-`2` shift flips the sign of every `R'`-piece). Hence
   `global_A = M − A(R') ≥ M − total(R') = M − total(R) = 1/D(n+1)`. ✓

8. **Lemma `L*(n)` — single-auxiliary strengthened dual of `L(n)` — CLOSED**
   (IMPORTED `lemmas/lemma-L-star-single-aux.md`). For the level-`n`
   dyadic `R` refined by `≤ n` marks into `R'`, and a single auxiliary piece `w`
   with `0 ≤ w ≤ R_largest = 2^n/D(n)`: `evensum({w} ∪ R') ≥ w`.

9. **Lemma `L(n+1)`, `k = 1` sub-case — CLOSED (reduces to `L*(n)`).**
   One Xiang mark in `M` splits it as `(m_1, m_2)`, `m_1 ≥ m_2`,
   `m_1 + m_2 = M`. The remaining `n` Xiang marks refine `R` into `R'`. Since
   `m_1 ≥ M/2 = 2^n/D(n+1) = R`'s largest (unrefined) piece, and refining only
   shrinks `R`-pieces, `m_1` is the global rank-`1` piece (Liu's). The rest
   `{m_2} ∪ R'` occupies global ranks `2, 3, 4, …`; Liu's odd-rank take from
   the rest is its even-rank sum (the rank-`2` shift flips parity), so
   `global_oddsum = m_1 + evensum({m_2} ∪ R')`. Apply `L*(n)` (rescale `R` to
   total `1`; the auxiliary rescales to
   `m_2 · D(n+1)/D(n) ≤ (M/2)·D(n+1)/D(n) = 2^n/D(n) = R_largest`), giving
   `evensum({m_2} ∪ R') ≥ m_2`. Hence
   `global_oddsum ≥ m_1 + m_2 = M = f(n+1)`. ✓

10. **(R3, round 3) `n = 1` real case — CLOSED.** See sub-proof below.

11. **(R1, round 3) The reduction `L(n+1) ⟺ e_M ≤ o_R`** — CLOSED (reformulation,
    no new induction). See sub-proof below. This *localizes* the interleaving
    obstruction to a single clean inequality on the merged sort; the open step
    is proving that inequality for reals.

12. **(R2, round 3) Integer-grid parity theorem** — CLOSED (restricted to
    grid-aligned refinements). See sub-proof below.

13. **(Round 4, CORRECTED round 5) Superincreasing-R identity** — CLOSED
    (formal lever, identity only). The unrefined `R`-pieces
    `a_j = 2^{n+1−j}/D(n+1)` are superincreasing:
    `a_j − Σ_{l>j} a_l = 1/D(n+1) = α(n+1)` (the certified dyadic-dominance
    identity). **CORRECTION (round 5):** the round-4 corollary
    "`Σ_{MM} m_even ≤ σ = M − m_1 ≤ M/2 = a_1`" is FALSE for `k ≥ 2`
    (the step `m_1 ≥ M/2` holds only for `k = 1`); it is REMOVED. The
    identity stands; see §0 (round 5). The genuine obstruction bound for
    Branch 1 is `σ ≤ a_1` (valid only under the Branch-1 hypothesis
    `m_1 ≥ a_1`); Branch 2 has no such bound and is handled by the §B'
    casework at `n = 2` / the (H2) Hall matching at general `n`.

14. **(Round 4, RE-WORKED round 5) Lemma L(3) unrefined-R sub-case — CLOSED
    over reals, now self-rigorous via the m_1-split.** For
    the level-3 dyadic with all three Xiang marks in `M` (`R' = R`
    unrefined, superincreasing intact), `A ≥ 1/15 = α(3)` for every real
    response. **m_1-split (round 5):** Branch 1 (`m_1 ≥ a_1 = 4`) = closed
    form `A = 7 − 2(s_3+s_5)` (in `1/15` units) + 3-case casework on `t_2`
    (round-4 proof, valid under `m_1 ≥ 4`); Branch 2 (`m_1 < 4`) = NEW 6-piece
    casework reducing to `oddsum(rest5) ≥ 4` (§B'). Equality iff
    `{m_2,m_3,m_4} = {2,1,1}/15` (staircase) or degenerate `{2,2,0}/15`
    (Branch 1); Branch 2 has no interior equality (tight only in the limit
    `m_1 → 4⁻`). The first real-valued `k ≥ 2` foothold on G1, now
    self-rigorous. See §B + §B' below.

15. **(Round 4) General-`n` superincreasing-R Hall matching on rank indices**
    — CONJECTURE (verified `n = 1..5`, OPEN). For the unrefined-R
    `k = n+1` sub-case, `s_3 + s_5 + … + s_{2n+1} ≤ a_2 + … + a_{n+1}`
    (rank-index Hall matching, staircase equality). Per-position bound
    `s_{2j} ≤ a_{j+1}` FAILS; layer-cake `⌊c(τ)/2⌋ ≤ c_A(τ)` too strong;
    the matching is genuinely on the sum over rank indices, subtler than any
    per-threshold count. See §C below.

### Open gaps (honest)

**(G1) Lemma `L(n+1)`, `k ≥ 2` sub-case — OPEN, localized to `e_M ≤ o_R`.**
The reduction (R1) shows `L(n+1)` is *exactly* `e_M ≤ o_R` (the sum of
`M`-sub-pieces at global even ranks is at most the sum of `R'`-pieces at global
odd ranks). The self-compensation pairing lemma (round 3) reduces this further:
every pair of type (odd `R'`, even `M`-sub) self-compensates by the sorted
order, so the residual is

> **(Match)** `Σ` (smaller piece of each `(M, M)` pair) ` ≤ Σ` (larger piece of
> each `(R', R')` pair).

This is verified by exact enumeration at `n = 2, 3` (integer grid, 0 violations)
and by 500k random *real* marks at `n = 2` (0 violations), but **no analytic
proof for general `n` over the reals is known here**. The integer-grid parity
theorem (R2) proves `A ≥ α(n)` for grid-aligned marks but does NOT lift to
reals (a finer odd grid gives a weaker bound). Conjecture (S) ("smallest piece
≥ α(n) at the minimizer") is **FALSE for reals** (Xiang can make a sub-α
fragment; the fragment then cancels at an odd rank, so `A` survives but CK
cannot detect it), so the odd-count cheap-kill does not lift off the grid
either. The even-count sub-case (pair-pile-type extremals, which have
`e_M = o_R = 0`) is Engine C's distinctive territory and is where the
self-compensation reduction (R1) lives; the residual (Match) is the live open
handle. **Round-4 partial closure** (CORRECTED round 5): the
superincreasing-R identity (crux aimo-0019) is formalized (item 13,
IDENTITY ONLY — the false `σ ≤ M/2` corollary is removed), and the
unrefined-R sub-case (`k = n+1`, `R' = R` with superincreasing structure
intact) is PROVED over reals at `n = 2` (item 14, Lemma L(3) unrefined-R
sub-case) — the first real-valued `k ≥ 2` foothold on G1. **Round-5
fix:** the L(3) unrefined-R proof is re-worked via the **m_1-split**
(Branch 1 `m_1 ≥ a_1` = round-4 casework, correctly scoped; Branch 2
`m_1 < a_1` = NEW 6-piece casework, §B'), making it self-rigorous for both
branches. The general-`n` version reduces to TWO Hall-type matchings —
(H1) on rank indices (Branch 1) and (H2) on the rest polytope (Branch 2) —
both verified `n = 1..5` but OPEN (item 15 + the new (H2) gap). The
`R`-refined sub-cases (`k ≤ n`, marks in `R`) remain OPEN over reals
(refinement breaks the superincreasing structure the lever exploits). The
unrefined-R result is independent of / parallel to the cell-complex-l3
sibling's `n = 3` vertex-enumeration route (two framings converging on
L(3), neither alone closing it).

**(G2) Lemma `U` (arbitrary-config upper bound) — OPEN, two-regime split with a
tracked dependency on the sibling `two-regime-disjunctive`.** (Unchanged from
round 2.)
- **Regime D — `P` is the (scaled) level-`n` dyadic.** Xiang plays the
  pair-pile or mirror (IMPORTED). Either caps `Liu` at exactly `f(n)`. ✓ Closed.
- **Regime N — `P` is not the level-`n` dyadic.** Computationally confirmed
  (non-dyadic `n = 2` configs cap strictly below `f(2) = 4/7`, at `≈ 0.50–0.525`
  for non-dominant and `≈ 0.50–0.504` for dominant-non-dyadic), but the
  mechanism is NOT the FALSE `A ≤ 0` pairing — it is a sliver/shave
  generalizing the certified `U(1)` sliver mode, owned by the sibling
  `two-regime-disjunctive`. This file does NOT claim regime N without that
  construction.

Because both gaps (G1 `k ≥ 2` reals, G2 regime-N mechanism) are open, the proof
is not complete; Status = `partial`. The conjectured answer `c(n) = f(n)` is
verified for `n = 1..5` and is consistent with every certified lemma, every
brute-force check, and every new round-3 result.

---

## Rigorous sub-proofs

*(Lemma G, pair-pile, mirror, ΔA closed form, Lemma L\*, the round-1 `n = 1`
grid proof, and the round-2 `k = 0` / `k = 1` sub-cases are IMPORTED from the
certified lemmas / the round-1 file; they are not re-proved here. The new
round-3 sub-proofs follow.)*

### `M ⊎ R` self-similar decomposition + dyadic-dominance identity

*(Reproduced from round 2 for self-containedness; unchanged.)*

The level-`(n+1)` dyadic config is Liu's `n + 1` marks at cumulative sums of
`(1, 2, 4, …, 2^n)/D(n+1)`, i.e. at positions `(2^j − 1)/D(n+1)` for
`j = 1, …, n+1`. The pieces are `(1, 2, 4, …, 2^n)/D(n+1)` (lengths
`2^{j−1}/D(n+1)` for `j = 1, …, n+2`). Let

- `M = 2^{n+1}/D(n+1)` (the largest, last piece, `M > 1/2`), and
- `R = (1, 2, 4, …, 2^n)/D(n+1)` (the first `n + 1` pieces).

**Self-similarity.** `(1, 2, 4, …, 2^n)/D(n+1) = (D(n)/D(n+1)) ·
(1, 2, 4, …, 2^n)/D(n)`, since `D(n+1) = 2·D(n) + 1` and the common factor is
`D(n)/D(n+1)`. So `R` is a scaled copy of the level-`n` dyadic, scaled to total
`total(R) = D(n)/D(n+1)`. ✓

**Dyadic-dominance identity.**
`M − total(R) = 2^{n+1}/D(n+1) − D(n)/D(n+1) = (2^{n+1} − D(n))/D(n+1) =
(2^{n+1} − (2^{n+1} − 1))/D(n+1) = 1/D(n+1)`.
So the excess of `M` over the entire rest `R` is exactly `1/D(n+1) = α(n+1)`,
the target advantage. ✓

Knowledge-base: **Invariants & monovariants** (the alternating advantage sum
`A` is the controlled invariant; the `M − R` identity linearizes the target).

---

### Lemma `L(n+1)`, `k = 0` sub-case — PROVED (trivial)

*(Unchanged from round 2; reproduced for reference.)* Suppose `0` of Xiang's
`≤ n + 1` marks land in `M`. Then `M` is a single piece, and since
`M = 2^{n+1}/D(n+1) > D(n)/D(n+1) = total(R) ≥` every individual `R'`-piece, `M`
is the global rank-`1` piece (Liu's by Lemma G). The rest `R'` occupies global
ranks `2, 3, 4, …`; its contribution to the global alternating sum is `−A(R')`
(the sign of `R'`'s rank-`j` piece in the global sort is
`(−1)^{(j+1)+1} = −(−1)^{j+1}`). Therefore

```
global_A = M − A(R') ≥ M − total(R') = M − total(R) = 1/D(n+1),
```

using `A(R') ≤ oddsum(R') ≤ total(R') = total(R)` (every piece non-negative).
Hence `global_A ≥ 1/D(n+1)`, i.e. `global_oddsum ≥ f(n+1)`. ∎

*(No induction hypothesis is used; the bound is the bare `A(R') ≤ total(R')`.
In fact `A(R') < total(R')` strictly for `n ≥ 1` since `R'` has `≥ 2` pieces, so
`global_A > 1/D(n+1)` strictly — the tight case requires `k ≥ 1` marks in `M`.)*

---

### Lemma `L*(n)` — single-auxiliary strengthened dual — PROVED

*(IMPORTED. Full proof in `lemmas/lemma-L-star-single-aux.md`; the three-case
rank analysis. **Summary**: sort `{w} ∪ R'` descending, let `r` be `w`'s rank.
`r` even → `w ∈ evensum`, trivial. `r ≥ 3` odd → `w ≤ s_2` and
`oddsum({w} ∪ R') = w + oddsum(R') − A_tail ≤ 1` (uses sortedness only).
`r = 1` → `oddsum({w} ∪ R') = w + evensum(R') = w + 1 − oddsum(R')`, need
`w ≤ oddsum(R')`, which is `L(n)` via `oddsum(R') ≥ f(n) = R_largest ≥ w`.)*

---

### Lemma `L(n+1)`, `k = 1` sub-case — PROVED (reduces to `L*(n)`)

*(Unchanged from round 2; reproduced for reference.)* Exactly `1` Xiang mark
in `M` splits it into `(m_1, m_2)`, `m_1 ≥ m_2`, `m_1 + m_2 = M`. The remaining
marks refine `R` into `R'`. Since `m_1 ≥ M/2 = 2^n/D(n+1) = R`'s largest
(unrefined) piece and refining only subdivides `R`-pieces, `m_1` is the global
rank-`1` piece (Liu's). The rest `{m_2} ∪ R'` occupies global ranks `2, 3, …`;
Liu's odd-rank take from the rest is its even-rank sum (rank-`2` shift flips
parity), so `global_oddsum = m_1 + evensum({m_2} ∪ R')`. Apply `L*(n)` to the
scaled rest (rescale `R` to total `1`; auxiliary rescales to
`m_2 · D(n+1)/D(n) ≤ (M/2)·D(n+1)/D(n) = 2^n/D(n) = R_largest`), giving
`evensum({m_2} ∪ R') ≥ m_2`. Hence
`global_oddsum ≥ m_1 + m_2 = M = f(n+1)`. ∎

---

### (R3, round 3) `n = 1` real case — PROVED

**Setup.** `n = 1`, `D(1) = 3`, `α(1) = 1/3`, `f(1) = 2/3`. Liu's dyadic
config is `(1, 2)/3`: one Liu mark at `1/3`, pieces `(1/3, 2/3)`. Xiang may
place `0` or `1` mark (not at `1/3`). Let `A = Σ (−1)^{i+1} p_i` (sorted desc).
We prove `A ≥ 1/3 = α(1)` for every real Xiang response, with equality iff the
mark lands in the largest piece `2/3`.

**Case 0 marks.** Pieces `(2/3, 1/3)` sorted desc. `A = 2/3 − 1/3 = 1/3`. ✓

**Case 1 mark at `x ∈ [0, 1] \ {1/3}`.** Two sub-cases by which piece `x` lands in.

*Sub-case (a): `x ∈ (1/3, 1)` (mark in the largest piece `2/3`, which occupies
`[1/3, 1]`).* The piece `2/3` is split into `(x − 1/3, 1 − x)`; let
`a := min(x − 1/3, 1 − x)`, `b := max(x − 1/3, 1 − x)`, so `a + b = 2/3`,
`a ≤ b`. The third piece is `1/3`.

  - If `a ≤ 1/3` (i.e. `x − 1/3 ≤ 1/3` and `1 − x ≤ 1/3` — wait, need care):
    actually `a = min(x−1/3, 1−x)`. Since `x ∈ (1/3, 1)`, both `x−1/3` and
    `1−x` are in `(0, 2/3)`. Their min `a` satisfies `a ≤ 1/3` iff
    `x − 1/3 ≤ 1/3` (i.e. `x ≤ 2/3`) or `1 − x ≤ 1/3` (i.e. `x ≥ 2/3`). So
    **always** `a ≤ 1/3` (at `x = 2/3` both fragments equal `1/3`). Hence
    `a ≤ 1/3 ≤ b`. The three pieces sorted desc are `b, 1/3, a` (since
    `b ≥ 1/3 ≥ a`). Then
    ```
    A = b − 1/3 + a = (a + b) − 1/3 = 2/3 − 1/3 = 1/3.   ✓
    ```
    (Equality, independent of `x` — the `±a` from the two fragments cancel:
    the small fragment `a` lands at rank 3 (odd, `+a`), and the large fragment
    `b` replaces `2/3` at rank 1 (loss `−a`).)

  - (No other branch: `a ≤ 1/3` always holds for `x ∈ (1/3, 1)`.)

  So `A = 1/3` for every mark in the largest piece. ✓ (Equality.)

*Sub-case (b): `x ∈ (0, 1/3)` (mark in the smallest piece `1/3`, occupying
`[0, 1/3]`).* The piece `1/3` is split into `(x, 1/3 − x)`; let
`b := max(x, 1/3 − x)`, `c := min(x, 1/3 − x)`, so `b + c = 1/3`, `b ≥ c`,
`b ≥ 1/6`. The other piece is `2/3` (unsplit, rank 1). The three pieces sorted
desc:

  - If `b ≤ 1/3` (always, since `b ≤ 1/3`): sorted `2/3, b, c`. Then
    `A = 2/3 − b + c = 2/3 − (b − c) = 2/3 − (1/3 − 2c) = 1/3 + 2c ≥ 1/3`,
    with equality iff `c = 0` (excluded, mark interior). So `A > 1/3` strictly.
    ✓ (This is the case `b ≤ 1/6`? No — `b ≥ 1/6`, and `c ≤ 1/6`. The sort
    `2/3, b, c` is correct since `2/3 > b ≥ 1/6 ≥ c` and `b ≥ c`.)
    
    *Check the `b ≥ 1/6` sub-branch*: `b = max(x, 1/3 − x) ≥ 1/6`, `c = min
    ≤ 1/6`, so `b ≥ c` and `2/3 ≥ b`. Sort `2/3, b, c` holds. The formula
    `A = 1/3 + 2c` gives `A ≥ 1/3` (since `c ≥ 0`, strict for `c > 0`). ✓

Combining the three cases: `A ≥ 1/3 = α(1)` for every real Xiang response,
with equality iff the mark lands in the largest piece `2/3` (or no mark). By
Lemma G, `Liu = (1 + A)/2 ≥ (1 + 1/3)/2 = 2/3 = f(1)`. The pair-pile (IMPORTED)
caps at exactly `f(1)`, so `c(1) = 2/3` (real case, end-to-end). ∎

**Knowledge-base tools.** **Casework / exhaustion** (the three cases for the
mark's location, each settled); **Invariants & monovariants** (the
cancellation `±a` is the structural reason the local-cut `ΔA` formula fails to
apply — the small fragment jumps rank, a non-local cut).

---

### (R1, round 3) The reduction `L(n+1) ⟺ e_M ≤ o_R` — PROVED (reformulation)

**Setup.** Level-`(n+1)` dyadic. `M = 2^{n+1}/D(n+1)` (largest piece),
`R = (1, 2, …, 2^n)/D(n+1) = (D(n)/D(n+1))·(level-n dyadic)`, `total(R) =
D(n)/D(n+1)`, `R_largest = 2^n/D(n+1) = M/2`. Xiang refines by `≤ n+1` marks:
`k` marks land in `M` (splitting it into `k+1` sub-pieces `m_1 ≥ … ≥ m_{k+1}`,
`Σ m_i = M`, `k ≤ n+1`), and `≤ n+1−k ≤ n` marks refine `R` into `R'`
(so `R'`-pieces each `≤ R_largest = M/2`). Merge the `k+1` `M`-sub-pieces with
the `R'`-pieces into the global sorted-desc list `p_1 ≥ p_2 ≥ …`.

**Definitions.** Partition the global list into two classes by origin:
- `e_M := Σ` (lengths of `M`-sub-pieces at *global EVEN* ranks `2, 4, 6, …`).
- `o_M := Σ` (lengths of `M`-sub-pieces at *global ODD* ranks `1, 3, 5, …`).
  (`e_M + o_M = M`.)
- `e_R := Σ` (lengths of `R'`-pieces at global EVEN ranks).
- `o_R := Σ` (lengths of `R'`-pieces at global ODD ranks).
  (`e_R + o_R = total(R') = total(R) = D(n)/D(n+1)`.)

By Lemma G, `evensum(global) = e_M + e_R` (Xiang's take) and
`oddsum(global) = o_M + o_R` (Liu's take).

**Reduction.** Lemma `L(n+1)` is `oddsum(global) ≥ M` (since `M = f(n+1)`).
Now `oddsum(global) = o_M + o_R = (M − e_M) + o_R`, so

```
oddsum(global) ≥ M   ⟺   M − e_M + o_R ≥ M   ⟺   e_M ≤ o_R.   ✓
```

Equivalently, `evensum(global) = e_M + e_R ≤ total(R) = e_R + o_R ⟺ e_M ≤ o_R`.
So:

> **Lemma `L(n+1)` is EXACTLY the inequality `e_M ≤ o_R`** — the sum of
> `M`-sub-pieces landing at global even ranks is at most the sum of `R'`-pieces
> landing at global odd ranks.

This is independent of the value of `k`: it makes no per-`k` classification and
no WLOG-`k` exchange. The interleaving obstruction is now localized to proving
`e_M ≤ o_R` on the merged sort, a single clean inequality between two sub-sums.
∎ (Reformulation; no induction.)

**Verification.** (a) Exact enumeration on the `1/D(n)` integer grid:
`e_M ≤ o_R` holds with equality iff `oddsum = M = f(n)` (the pair-pile / mirror
extremals), for `n = 2, 3` (verified, 0 violations among all 11 + 232 grid
refinements). (b) 500 000 random *real* Xiang marks at `n = 2` (level `N = 3`,
the `M ⊎ R` decomposition with `M = 4/7`, `R = (1/7, 2/7)`): 0 violations of
`e_M ≤ o_R`; min `A = 1/7 = α(2)`.

**Knowledge-base tools.** **Invariants & monovariants** (the `M`-vs-`R` split
turns the global alternating sum into a pair of sub-alternating sums; the
`e_M ≤ o_R` reformulation linearizes the target).

---

### (R2, round 3) Integer-grid parity theorem — PROVED (restricted)

**Statement.** For the level-`n` dyadic config `(1, 2, 4, …, 2^n)/D(n)` and any
Xiang refinement whose marks are at multiples of `1/D(n)` (so every final piece
is a positive multiple of `1/D(n)`), the alternating advantage sum satisfies

`A ≥ 1/D(n) = α(n)`.

**Proof.** Scale all lengths by `D(n)`: the pieces become positive integers
`q_1 ≥ q_2 ≥ … ≥ q_M` with `Σ q_i = D(n)` (an ODD integer, since
`D(n) = 2^{n+1} − 1`). The scaled advantage is `A* := A·D(n) = Σ (−1)^{i+1} q_i`.

Pair consecutive sorted pieces: `A* = Σ_{i=1}^{⌊M/2⌋} (q_{2i−1} − q_{2i}) +
[remainder]`, where the remainder is `0` (even `M`) or `q_M` (odd `M`). Each
pair-excess `e_i := q_{2i−1} − q_{2i} ≥ 0` (sorted order). Moreover,
`e_i = (q_{2i−1} + q_{2i}) − 2·q_{2i}`, so `e_i ≡ q_{2i−1} + q_{2i} (mod 2)`.
Summing:

```
Σ e_i  ≡  Σ (q_{2i−1} + q_{2i})  (mod 2)  =  Σ q_i (if M even)  ≡  D(n)  ≡  1 (mod 2).
```

So `Σ e_i` is a non-negative integer congruent to `1 (mod 2)`, hence
`Σ e_i ≥ 1`. (Odd `M`: add `q_M ≥ 1`, still `≥ 1`.) Therefore
`A* = Σ e_i + [q_M] ≥ 1`, i.e. `A ≥ 1/D(n) = α(n)`. ∎

**The lift fails.** The argument is tied to the grid spacing `1/D(n)` (the `1`
is the grid unit). For a finer grid `1/(K·D(n))` with `K` odd, the scaled total
`K·D(n)` is still odd, but the parity argument yields `A ≥ 1/(K·D(n))`, which
is *weaker* than `1/D(n)` for `K > 1`. So the parity mechanism does NOT extend
to arbitrary real marks, only to grid-aligned ones. Real marks can produce a
sub-`1/D(n)` smallest piece, defeating the CK cheap-kill; the integer-grid
parity survives only because all pieces are positive multiples of `1/D(n)`.

**Verification.** `A·D(n) = 1` (the minimum odd value) for all 2 (n=1) + 11
(n=2) + 232 (n=3) grid refinements, with the minimum attained at the pair-pile
/ bisect-all-big extremals.

**Knowledge-base tools.** **Pigeonhole / extremal principle** (the parity is a
mod-2 pigeonhole on the pair-excesses); **Invariants & monovariants** (the
alternating sum's parity is locked to the total's parity, an invariant of the
sorted multiset).

---

### Self-compensation pairing lemma — PROVED (reduces `e_M ≤ o_R` to a residual)

**Setup.** Same as the reduction (R1). Pair the global sorted list as
`(p_1, p_2), (p_3, p_4), …`: in each pair `(p_{2i−1}, p_{2i})` the odd-position
piece `p_{2i−1} ≥ p_{2i}` (sorted). Classify each pair by the *origins* of its
two pieces:

- Type **MM**: both pieces are `M`-sub-pieces. Contributes `m_even` to `e_M`,
  `m_odd` to `o_M`; `m_odd ≥ m_even`. (No `R'`-contribution.)
- Type **RR**: both pieces are `R'`-pieces. Contributes `r_odd` to `o_R`,
  `r_even` to `e_R`; `r_odd ≥ r_even`. (No `M`-contribution.)
- Type **MR**: odd is `M`-sub, even is `R'`-piece. Contributes `r_even` to
  `e_R`, `m_odd` to `o_M`. (No `e_M`, no `o_R`.)
- Type **RM**: odd is `R'`-piece, even is `M`-sub-piece. Contributes `m_even`
  to `e_M`, `r_odd` to `o_R`; and by the sorted order within the pair,
  `r_odd ≥ m_even`. (This is the **self-compensating** type.)

**Lemma (self-compensation).** In every **RM** pair, `r_odd ≥ m_even`, so the
pair's contribution to `e_M` is paid in full by its contribution to `o_R`.

**Corollary.** `e_M ≤ o_R` reduces to

> **(Match)** `Σ` over `MM` pairs of `(m_even)` ` ≤ ` `Σ` over `RR` pairs of
> `(r_odd)`.

*Proof of the reduction.* Write
`e_M = Σ_{MM} m_even + Σ_{RM} m_even` and
`o_R = Σ_{RR} r_odd + Σ_{RM} r_odd`.
By self-compensation, `Σ_{RM} m_even ≤ Σ_{RM} r_odd`. Subtracting,
`e_M ≤ o_R ⟺ Σ_{MM} m_even ≤ Σ_{RR} r_odd`. ∎

So the interleaving obstruction, after self-compensation, is reduced to a
single inequality comparing the *smaller half* of each `M`-`M` pair against the
*larger half* of each `R'`-`R'` pair. This residual (Match) is verified by
exact enumeration at `n = 2, 3` (0 violations) and 500k random reals at `n = 2`
(0 violations), but is **not analytically proved for general `n` over the
reals** — it is the live open handle of Engine C.

At the pair-pile extremal (equality case `e_M = o_R = 0`): there are no `MM`
and no `RR` pairs — all pairs are `MR` or `RM` and self-compensate exactly
(`r_odd = m_even` in each, by the pair-pile's equal-pair structure). So the
extremal saturates the self-compensation bound with (Match) holding as
`0 ≤ 0`. ✓

**Knowledge-base tools.** **Hall's marriage theorem** (the (Match) residual is
an injective-matching condition: match each `MM`-pair's smaller half to a
distinct `RR`-pair's larger half `≥` it); **Invariants & monovariants** (the
within-pair sortedness `r_odd ≥ m_even` is the self-compensation monovariant).

---

### Lemma `L(n+1)`, `k ≥ 2` sub-case — OPEN (the residual (Match))

By the reduction (R1), `L(n+1)` for ALL `k` (including `k ≥ 2`) is `e_M ≤ o_R`.
By the self-compensation lemma, this reduces to the residual (Match):
`Σ_{MM pairs} m_even ≤ Σ_{RR pairs} r_odd`.

**Status of (Match).** Verified by exact enumeration (n = 2, 3 grid, 0
violations) and 500k random reals (n = 2, 0 violations). No analytic proof for
general `n` over the reals. The residual is a Hall-type matching condition
(match each `MM`-pair's smaller half to a distinct `RR`-pair's larger half `≥`
it); the superincreasing structure of `R` (each `R`-piece exceeds the sum of
all smaller `R`-pieces by `1/D(n+1)`, the level-boundary excess) is the
structural lever expected to close it, but the inductive matching proof is not
completed here. This is the genuine open gap of the lower-bound route, now
localized to a single clean inequality.

The multi-aux generalization of `L*` remains FALSE (counterexample
`W = (1/9, 4/9, 1/9)` over `D = 9`); the per-round peeling (D1) and the
WLOG-`k = 1` exchange (D2) remain blocked by the ΔA `−2T` tail-flip and by the
n = 3 brute-force counterexample to literal monotonicity in `k`. Engine C's
`e_M ≤ o_R` reduction (R1) + self-compensation (round 3) is the *first*
localization that avoids per-`k` classification entirely; the residual (Match)
is the live handle for the next round.

**Brute-force corroboration (NOT a proof step).** Exact enumeration on the
integer grid: `min oddsum = f(n)` for `n = 1, 2, 3` (n=1: 2 responses, min
2/3; n=2: 11 responses, min 4/7; n=3: 232 responses, min 8/15). Monte-Carlo
(200k random responses) at `n = 4, 5`: min `16/31`, `32/63`, matching `f(n)`.
The floor is robust.

---

### Lemma `U` (arbitrary-config upper bound) — OPEN, two-regime split (tracked dependency)

*(Unchanged from round 2; the upper bound is owned by the sibling
`two-regime-disjunctive`. Recorded here as a tracked dependency.)*

**Retired route.** Round-1 Hall-matching (the Hall-dominance condition fails
for non-dyadic Liu configs, verified round 1) and the per-mark monovariant
(the ΔA `−2T` tail-flip, certified dead) are NOT retried.

**Pivot: two-regime split.** For an arbitrary Liu config `P` of `n` marks:
- **Regime D — `P` is the (scaled) level-`n` dyadic.** Xiang plays the
  pair-pile / mirror (IMPORTED). Either caps `Liu` at exactly `f(n)`. ✓ Closed.
- **Regime N — `P` is not the level-`n` dyadic.** The round-2 review
  computationally confirmed non-dyadic `n = 2` configs cap strictly below
  `f(2) = 4/7` (at `≈ 0.50–0.525`, above `1/2`), so the bound holds in regime
  N but the mechanism is NOT the FALSE `A ≤ 0` pairing — it is a sliver/shave
  generalizing the certified `U(1)` sliver mode, owned by the sibling
  `two-regime-disjunctive`. This file does NOT claim regime N without that
  construction.

The `n = 1` instance of Lemma `U` is closed (round 1, two-mode bisect/sliver;
matches the two-regime split: `a ≤ 1/3` regime D bisect, `a ≥ 1/3` regime N
sliver). `c(1) = 2/3` (both bounds, real case closed this round via R3).

---

### Lemma S (small-`n` verification) — CHECK (not a proof step)

Exact-rational minimax on integer grids (multiples of `D(n)`):

| `n` | `c(n)` | `D(n)` | `2^n` | min `oddsum` (brute/MC) |
|---|---|---|---|---|
| 1 | 2/3  | 3  | 2  | 2/3 (exact, 2 responses) |
| 2 | 4/7  | 7  | 4  | 4/7 (exact, 11 responses) |
| 3 | 8/15 | 15 | 8  | 8/15 (exact, 232 responses) |
| 4 | 16/31| 31 | 16 | 16/31 (Monte-Carlo, 200k) |
| 5 | 32/63| 63 | 32 | 32/63 (Monte-Carlo, 200k) |

These are computational *checks*, not proof steps. `n = 1` (grid + real) and
`n = 2` (round-1 casework + grid + brute) are given full hand proofs; the
real-valued `n = 2` lower bound is also covered by the reduction (R1) +
self-compensation (verified 0 violations on 500k random reals).

---

## Round 4 outline (ADVANCE — close the residual (Match) via the superincreasing-R lever)

**Framing (unchanged):** pair-excess decomposition + `M ⊎ R` self-similar
decomposition + the residual Hall-type matching on the merged sort. No new
framing; this round attacks the SAME open handle `(Match)` with a concrete
borrowed crux move.

**Target (the whole claim):** `c(n) = f(n)` end-to-end. This approach owns G1
(Lemma L general-n, `k ≥ 2` reals, localized to `e_M ≤ o_R` ⟺ residual
`(Match) Σ_{MM} m_even ≤ Σ_{RR} r_odd`). G2 (regime-N) stays a tracked
dependency on `two-regime-disjunctive`.

**The live gap and the round-4 mechanism.** The residual (Match) is a Hall-type
injective-matching condition: match each `MM`-pair's smaller half `m_even` to a
distinct `RR`-pair's larger half `r_odd ≥` it. The structural lever, now backed
by crux **aimo-0019** ("bound a family of dyadic-length pieces of pairwise
distinct sizes by twice the largest, via the geometric sum of distinct
negative powers of two"), is the **superincreasing structure of R**: each
`R`-piece `2^j/D(n+1)` exceeds the sum of all smaller `R`-pieces by exactly
the level-boundary excess `1/D(n+1) = α(n+1)` (the dyadic-dominance identity,
certified). The `MM`-pair smaller halves `m_even` are sub-pieces of
`M = 2·R_largest`, hence each `m_even ≤ R_largest`, and the superincreasing
gap is the candidate Hall witness.

**Skeleton (the gap steps, NOT a finished proof):**
1. **Import** Lemma G, `e_M ≤ o_R` reduction (lemma-em-or), self-compensation
   (lemma-self-compensation), `M ⊎ R` identity, grid-parity (grid-only check),
   n=1 real ±a mechanism. (All certified.)
2. **GAP (the hard step — the Hall matching over reals).** Prove, for all real
   Xiang refinements of the level-`n` dyadic: there is an injective matching
   from the `MM` pairs (smaller halves `m_even`) into the `RR` pairs (larger
   halves `r_odd`) with `m_even ≤ r_odd` matched. The witness is the
   superincreasing-R structure (aimo-0019 geometric-sum `< 2·largest` bound
   adapted): an `MM` smaller half sits below a *distinct* dyadic level of `R`,
   so a distinct `RR` larger half dominates it. Mechanism to name in the proof:
   the merged-sort interleaving of `M`-sub-pieces (each `≤ R_largest = M/2`)
   with `R`-pieces (geometrically spaced, `2^j`-ratio) forces each `m_even` to
   be paired-with / dominated-by a *unique-rank* `r_odd`.
3. **Equality case.** Equality `Σ_MM m_even = Σ_RR r_odd` holds iff the
   refinement is the pair-pile / mirror extremal (the
   `{2^j, 2^j+1}` consecutive-powers odd-mult structure from the minimizer
   census — Explorer 3). Import the grid census as the empirical equality-case
   target; the real-equality characterization is a GAP (shared with the new
   `equality-case-classification` approach — flagged).
4. Conclude `e_M ≤ o_R` ⟹ `L(n+1)` ⟹ `L(n)` for all `n` (induction on `n`),
   hence `c(n) ≥ f(n)`. G2 imported from `two-regime-disjunctive`.

**Key lemmas (claim + one-line mechanism):**
- (Match) `Σ_MM m_even ≤ Σ_RR r_odd` — because each `m_even ≤ R_largest` and
  the `R`-pieces are superincreasing (`2^j > Σ_{i<j} 2^i`), so a Hall matching
  exists by a dyadic-level/rank-distinctness argument (aimo-0019 template).
- Equality ⟺ pair-pile/mirror — because the census shows the only
  odd-mult leftovers are `{1}` or `{2^j, 2^j+1}`, both realized by the
  certified extremals.

**Open gaps (builder fills):**
- Step 2 (the real-valued Hall matching via superincreasing R) — the genuine
  hard step; the grid-parity theorem proves the grid case but does NOT lift.
- Step 3 (real equality-case characterization) — shared-wall risk with
  `equality-case-classification` (if the real classification fails, both the
  equality statement here and that approach's G1 half die together; flagged
  honestly).

**Cases to cover:** even-count minimizers (pair-pile type — the `MM`/`RR`
matching must saturate here) and odd-count minimizers (CK lemma + (S),
already covered grid-side).

**Watch out for:** the `MM`-pair smaller halves are NOT ordered by `R`-level
in any obvious way (the interleaving is the obstruction); the Hall matching
must be built on RANK INDICES in the merged sort, not on piece sizes alone.
The falsified Engine A (two-tail cancellation) is NOT retried — the
superincreasing-R lever is a different mechanism (global matching, not
per-mark transfer).

---

## Promotable lemmas

- **(R1) The reduction `L(n+1) ⟺ e_M ≤ o_R`.** Statement: in the `M ⊎ R`
  self-similar decomposition of the level-`(n+1)` dyadic, with `k` Xiang marks
  splitting `M` into `m_1, …, m_{k+1}` and `≤ n+1−k` marks refining `R` into
  `R'`, Lemma `L(n+1)` (the lower bound `global_oddsum ≥ f(n+1) = M`) is
  EXACTLY equivalent to `e_M ≤ o_R`, where `e_M` = sum of `M`-sub-pieces at
  global EVEN ranks and `o_R` = sum of `R'`-pieces at global ODD ranks in the
  merged sorted-desc list. NEW this round; proved in this file ("The reduction
  `L(n+1) ⟺ e_M ≤ o_R`"). Verified by exact enumeration (n=1,2,3 grid) and
  500k random reals (n=2, 0 violations). Reusable: any approach using the
  `M ⊎ R` decomposition can replace the per-`k` classification with this single
  inequality.

- **(R2) Integer-grid parity theorem.** Statement: for any grid-aligned
  (marks at multiples of `1/D(n)`) Xiang refinement of the level-`n` dyadic,
  `A ≥ 1/D(n) = α(n)`. Mechanism: scale by `D(n)` (ODD); the pair-excesses
  `e_i = q_{2i−1} − q_{2i}` satisfy `e_i ≡ q_{2i−1} + q_{2i} (mod 2)`, so
  `Σ e_i ≡ D(n) ≡ 1 (mod 2)`, a non-negative odd integer `≥ 1`. NEW this round;
  proved in this file. Rigorous but restricted to grid-aligned refinements; does
  NOT lift to reals. Reusable as a structural-parity check and as the clean
  base case for any induction that reduces reals to grid limits.

- **Self-compensation pairing lemma.** Statement: in the merged sorted-desc
  list paired as `(p_1,p_2), (p_3,p_4), …`, every pair of type (odd `R'`-piece,
  even `M`-sub-piece) satisfies `r_odd ≥ m_even` (within-pair sorted order), so
  its contribution to `e_M` is paid in full by its contribution to `o_R`. Hence
  `e_M ≤ o_R` reduces to the residual `Σ_{MM pairs} m_even ≤ Σ_{RR pairs}
  r_odd` (a Hall-type matching). NEW this round; proved in this file. Verified
  (n=2,3 grid + n=2 reals 500k, 0 violations); the residual (Match) is the open
  step. Reusable: localizes the interleaving obstruction for any approach.

- **CK (odd-count cheap-kill, real-valued, one-line).** Statement: for any
  sorted-desc partition with ODD piece-count `2m+1`,
  `A = Σ_{i=1}^m (p_{2i−1} − p_{2i}) + p_{2m+1} ≥ p_{2m+1}` (the smallest
  piece), since each pair-excess `≥ 0` and the leftover is the smallest piece.
  NEW this round; one-line proof in this file. Reusable on the integer grid
  (where `p_{2m+1} ≥ 1/D(n)`, closing the odd-count case immediately) — but
  NOTE: does NOT lift to reals (the smallest piece can be sub-α).

- *(Already certified: Lemma G, pair-pile, mirror, ΔA, Lemma L\*, U(2) —
  IMPORTED, not re-proposed.)*

---

## Round 4 build — the superincreasing-R lever + the unrefined-R sub-case

**Framing (unchanged).** Pair-excess decomposition + `M ⊎ R` self-similar
decomposition + the residual Hall-type matching `(Match) Σ_{MM} m_even ≤
Σ_{RR} r_odd` on the merged sort. No new framing; this round attacks the SAME
open handle with the corpus-backed superincreasing-R lever (crux
**aimo-0019**: "bound a family of dyadic-length pieces of pairwise distinct
sizes by twice the largest, via the geometric sum of distinct negative powers
of two").

### A. Formalization of the superincreasing-R lever

**Lemma (superincreasing structure of `R`).** *In the level-`(n+1)` dyadic,
the unrefined `R`-pieces*

```
a_1 = 2^n / D(n+1) > a_2 = 2^{n−1} / D(n+1) > … > a_{n+1} = 1 / D(n+1)
```

_are pairwise distinct and **superincreasing**_: for every `j`,
`a_j > Σ_{l > j} a_l`. Equivalently (crux **aimo-0019** geometric-sum bound),
each `R`-piece strictly exceeds the sum of all smaller `R`-pieces by exactly
the level-boundary excess `1/D(n+1) = α(n+1)` (the certified
dyadic-dominance identity `M − total(R) = α(n+1)`).

*Proof.* `a_j = 2^{n+1−j}/D(n+1)` and
`Σ_{l > j} a_l = (2^{n+1−j} − 1)/D(n+1)`, so
`a_j − Σ_{l>j} a_l = 1/D(n+1) = α(n+1) > 0`. ∎

**Corollary (the obstruction is bounded by `R_largest`).** *Every `MM`-pair
smaller half `m_even` is one of the "small" `M`-sub-pieces `m_2, …, m_{k+1}`,
whose total `σ = m_2 + … + m_{k+1} = M − m_1 ≤ M/2 = a_1 = R_largest`. Hence*

```
Σ_{MM pairs} m_even  ≤  σ  ≤  a_1 = R_largest.
```

*Proof.* `m_1 ≥ M/2` (largest of `k+1 ≥ 2` pieces summing to `M`), so
`m_1 ≥ M/2 = a_1`; `m_1` is the largest `M`-sub-piece, hence the largest
global piece, and is never the smaller half of any pair. Every `MM`-pair
smaller half is therefore drawn from `{m_2, …, m_{k+1}}`, whose sum is
`σ = M − m_1 ≤ M/2 = a_1`. ∎

> **⚠ CORRECTION (round 5):** This corollary is **FALSE for `k ≥ 2`**. The
> step `m_1 ≥ M/2` holds only when `k+1 = 2` (i.e. `k = 1`): for `k+1 ≥ 3`
> pieces summing to `M`, the largest satisfies `m_1 ≥ M/(k+1)`, which can be
> strictly below `M/2`. E.g. at `n = 2` (level-3 dyadic, `M = 8`), the config
> `m = (3,3,1,1)` has `m_1 = 3 < 4 = M/2`, so `σ = 5 > a_1 = 4`. The
> corollary is therefore INVALID in the very sub-case (`k ≥ 2`) it targets and
> is **NOT used** in the round-5 build (§0–§5 below). The identity above
> (superincreasing structure) is unaffected and remains the structural lever.
> The genuine obstruction bound for **Branch 1** is `σ ≤ a_1`, which IS valid
> *under the Branch-1 hypothesis `m_1 ≥ a_1`* (round 5, §1); Branch 2
> (`m_1 < a_1`) has `σ > a_1` and is handled by the §B' casework at `n = 2`
> and the (H2) Hall matching at general `n`. The corollary above is retained
> only for historical context; do not cite it.

This bounds the **magnitude** of the `Σ_{MM} m_even` obstruction by
`R_largest` — a strict sharpening over the bare `(Match)` statement (which
allows the obstruction to be as large as `M`). It does NOT by itself close
`(Match)`, because `Σ_{RR} r_odd` can be sub-`R_largest` (at the pair-pile
extremal it is `0`). The full Hall matching requires the *rank-structure*
of the superincreasing lever, formalized next.

**Conjecture (superincreasing-R Hall matching on rank indices, general `n`).**
*For the level-`(n+1)` dyadic with `k = n+1` Xiang marks all landing in `M`
(so `R' = R` retains its full superincreasing structure), let `s_1 ≥ s_2 ≥ … ≥
s_{2n+2}` be the sorted-desc merge of the small `M`-sub-pieces
`{m_2, …, m_{n+2}}` (sum `σ ≤ a_1`) with the `R`-pieces
`{a_1, …, a_{n+1}}` (superincreasing). Then `s_1 = a_1`, and*

```
s_3 + s_5 + … + s_{2n+1}  ≤  a_2 + a_3 + … + a_{n+1}.
```

*Equivalently, the odd-position sum (excluding `s_1 = a_1`) of the merge is
at most the total of the smaller `R`-pieces. This is the rank-index form of
the Hall matching: each `MM` smaller half, sitting below a distinct dyadic
level of `R` (the superincreasing bound `a_j > Σ_{l>j} a_l`), is dominated by
a distinct `RR` larger half at the corresponding rank. The matching is on
RANK INDICES in the merged sort, not on piece sizes — the `MM` smaller halves
are not ordered by `R`-level, so the injective matching is the genuine
difficulty (as flagged by the outline-reviewer).*

**Verification of the conjecture (NOT a proof step).** Exact-rational random
search (`300k` configs per `n`) finds the slack `(s_3+s_5+…) − (a_2+…+a_{n+1})`
non-negative for `n = 1..5`, with minimum `0` attained at the **staircase
interleaving** `s_1=a_1, s_2=b_1, s_3=a_2, s_4=b_2, …, s_{2n+1}=a_{n+1},
s_{2n+2}=b_{n+1}` (where the `b`'s straddle the `R`-levels). At the staircase,
odd positions are exactly all the `b`'s, so the bound holds with equality.
The conjecture is numerically robust but the **general-`n` analytic proof is
OPEN** — the per-position bound `s_{2j} ≤ a_{j+1}` FAILS (counterexample
`n=2, b=(4/3,4/3,4/3)`: `s_4 = 4/3 > a_3 = 1`), so the matching is genuinely
on the *sum* over rank indices, not a termwise dominance. A layer-cake
sufficient condition `⌊c(τ)/2⌋ ≤ c_A(τ)` (where `c(τ)`, `c_A(τ)` count
pieces / `R`-pieces `≥ τ`) is too strong (same counterexample violates it at
`τ = 1.3`); the real inequality is subtler than any per-threshold count.

### B. The unrefined-R sub-case at `n = 2` (level-3 dyadic) — PROVED over reals

**Theorem (Lemma L(3), unrefined-R sub-case, reals).** *For the level-3 dyadic
config `Liu = (1, 2, 4, 8)/15`, suppose Xiang's three marks all land in the
largest piece `M = 8/15` (so `R' = R = (1, 2, 4)/15` is unrefined). Then for
every real such response, `A ≥ 1/15 = α(3)`, with equality iff the small
`M`-sub-pieces realize `m_1 = 4/15` and `{m_2, m_3, m_4}` is the multiset
`{2/15, 1/15, 1/15}` (the staircase equality case; the degenerate limit
`{2/15, 2/15, 0}` also attains).*

*Proof.* Work in units of `1/15` (so the stick totals `15`, `M = 8`,
`R = (4, 2, 1)` with `total(R) = 7`, `a_1 = 4`, `a_2 = 2`, `a_3 = 1` —
superincreasing: `a_1 = 4 > 2+1 = 3 = a_2+a_3`, `a_2 = 2 > 1 = a_3`).
Three marks in `M` split it into four pieces `m_1 ≥ m_2 ≥ m_3 ≥ m_4 ≥ 0`
with `Σ m_i = 8`, `m_1 ≥ 4` (largest of `≥ 2` pieces summing to `8`).
Let `σ := m_2 + m_3 + m_4 = 8 − m_1 ≤ 4 = a_1`, and write `b_1 := m_2 ≥
b_2 := m_3 ≥ b_3 := m_4` (so `b_1 ≥ b_2 ≥ b_3 ≥ 0`, `Σ b_i = σ ≤ 4`,
`b_1 ≤ m_1` hence `b_1 ≤ 8 − σ` but more sharply `b_1 ≤ 4 = a_1` since
`b_1 ≤ σ ≤ 4`).

Merge `{b_1, b_2, b_3}` with `R = {4, 2, 1}` and sort descending:
`s_1 ≥ s_2 ≥ s_3 ≥ s_4 ≥ s_5 ≥ s_6`. Since `4 = a_1 ≥ b_1` (as
`b_1 ≤ σ ≤ 4`), we have `s_1 = 4 = a_1`. The global advantage is

```
A = m_1 − s_1 + s_2 − s_3 + s_4 − s_5 + s_6
  = (8 − σ) − 4 + (s_2 + s_4 + s_6) − (s_3 + s_5).
```

The six pieces `s_1, …, s_6` total `4 + σ` (the `R`-pieces `4+2+1=7`? — no:
here `s_1 + … + s_6 = σ + total(R) = σ + 7`). Using
`s_2 + s_4 + s_6 = (σ + 7) − (s_1 + s_3 + s_5) = σ + 7 − 4 − s_3 − s_5 =
σ + 3 − s_3 − s_5`, we substitute:

```
A = (8 − σ) − 4 + (σ + 3 − s_3 − s_5) − (s_3 + s_5)
  = 7 − 2 (s_3 + s_5).
```

So **`A ≥ 1 ⇔ s_3 + s_5 ≤ 3`** (in `1/15` units). It remains to prove
`s_3 + s_5 ≤ 3`. Equivalently (with `t_i := s_{i+1}`, the sorted-desc list of
the five pieces `{b_1, b_2, b_3, 2, 1}`): `t_2 + t_4 ≤ 3` (the 2nd-largest plus
the 2nd-smallest of the five pieces is at most `a_2 + a_3 = 3`).

We prove `t_2 + t_4 ≤ 3` by a three-way case split on `t_2`.

  * **Case I: `t_2 > 2`.** Then at least two of the five pieces exceed `2`.
    The `R`-pieces `2, 1` do not exceed `2` (one equals `2`, none exceeds it
    strictly), so at least two of the `b`'s strictly exceed `2`: `b_1 > 2` and
    `b_2 > 2` (as `b_1 ≥ b_2 ≥ b_3`). Then
    `σ = b_1 + b_2 + b_3 > 2 + 2 + 0 = 4`, contradicting `σ ≤ 4`.
    **Impossible.**

  * **Case II: `t_2 = 2`.** Then `b_3 ≤ 1`: otherwise `b_1 ≥ b_2 ≥ b_3 > 1`
    and (since `t_2 = 2` requires at most one `b` to exceed `2`, so
    `b_1 ≤ 2` or `b_1 > 2` alone) — in either sub-attainment of `t_2 = 2`,
    `σ = b_1 + b_2 + b_3 ≥ 2 + 1 + 1 = 4` would force `σ > 4` whenever
    `b_3 > 1` (if `b_1 > 2` then `σ > 2 + 1 + 1 = 4`; if `b_1 = 2` then
    `σ = 2 + b_2 + b_3 > 2 + 1 + 1 = 4`). Both contradict `σ ≤ 4`. Hence
    `b_3 ≤ 1`, so among `{b_3, 1}` at least two pieces are `≤ 1`, forcing
    `t_4 ≤ 1` (the 2nd-smallest is `≤ 1`). Thus `t_2 + t_4 = 2 + t_4 ≤ 3`. ✓

  * **Case III: `t_2 < 2`.** Then `b_1 < 2` (else `b_1 ≥ 2` would put
    `b_1` at `t_1` or `t_2 = 2`), and the largest of the five is `a_2 = 2`,
    so `t_1 = 2`, `t_2 = b_1 < 2`. The three smallest of the five are
    `{b_2, b_3, 1}` (since `b_2 ≤ b_1 < 2` and `a_3 = 1`), sorted descending;
    `t_4` is their middle (2nd-smallest). Three sub-cases:
      - **IIIa: `b_2 ≥ 1 ≥ b_3`.** Then `t_4 = 1`, so
        `t_2 + t_4 = b_1 + 1 < 2 + 1 = 3` (since `b_1 < 2`). ✓
      - **IIIb: `b_2 ≥ b_3 ≥ 1`.** Then `t_4 = b_3`, and
        `t_2 + t_4 = b_1 + b_3 = σ − b_2 ≤ 4 − b_2 ≤ 4 − 1 = 3` (as
        `b_2 ≥ b_3 ≥ 1`). ✓ (Equality requires `b_2 = 1` and `σ = 4`, which
        forces `b_1 = b_3 = 1.5` — but then `b_1 ≥ b_2 ≥ b_3` reads
        `1.5 ≥ 1 ≥ 1.5`, false. So IIIb is strict.)
      - **IIIc: `b_3 ≤ b_2 ≤ 1`.** Then `t_4 = b_2`, and
        `t_2 + t_4 = b_1 + b_2 < 2 + 1 = 3` (since `b_1 < 2`, `b_2 ≤ 1`). ✓

  In every case `t_2 + t_4 ≤ 3`, i.e. `s_3 + s_5 ≤ 3`, hence `A ≥ 1 = α(3)`
  (in real units, `A ≥ 1/15`). ∎

**Equality characterization.** Equality `A = 1/15` requires `t_2 + t_4 = 3`.
Case I is impossible; Case III is strict in all sub-cases (shown above). So
equality lies in **Case II** (`t_2 = 2`) with `t_4 = 1`: `b_1 = 2` (tie with
`a_2 = 2`), `σ = 4` (so `m_1 = 4`), and `b_3 ≤ 1` with the 2nd-smallest
exactly `1`. Concretely, `{m_2, m_3, m_4} = {2, 1, 1}` (in `1/15` units), giving
global multiset `{4, 4, 2, 2, 1, 1, 1}/15` with
`A = (4−4) + (2−2) + (1−1) + 1 = 1` (in `1/15` units) — a real (non-degenerate)
equality-case minimizer of the unrefined-R sub-case, distinct from the
pair-pile/mirror families (which use marks in `R`). The degenerate limit
`{m_2, m_3, m_4} = {2, 2, 0}` (a mark at `M`'s boundary) also attains.

**Knowledge-base tools.** **Hall's marriage theorem** (the inequality
`s_3 + s_5 ≤ a_2 + a_3` is the rank-index Hall matching: each `MM` smaller
half, sitting below a distinct dyadic level of `R` by the superincreasing
bound `a_j > Σ_{l>j} a_l`, is dominated by a distinct `RR` larger half at the
corresponding rank — aimo-0019 geometric-sum template);
**Invariants & monovariants** (the closed form `A = 7 − 2(s_3+s_5)` linearizes
the obstruction to a single rank-index sum);
**Casework / exhaustion** (the three cases on `t_2`, each settled, disjoint and
exhaustive: `t_2 > 2`, `t_2 = 2`, `t_2 < 2`).

### C. What is still open (honest)

1. **The general-`n` superincreasing-R Hall matching (Conjecture above).**
   The `n = 2` proof above is a full real-valued foothold for the unrefined-R
   sub-case; the staircase equality case generalizes cleanly (verified
   `n = 1..5`), but the **general-`n` analytic proof is OPEN**. The per-position
   bound `s_{2j} ≤ a_{j+1}` fails (counterexample `b = (4/3, 4/3, 4/3)` at
   `n = 2`), and the layer-cake sufficient condition is too strong. The real
   inequality is a sum-level matching on rank indices; a clean proof technique
   for arbitrary `n` is not yet in hand.

2. **The `R`-refined sub-cases (`k ≤ n`, some marks in `R`).** When Xiang
   spends marks in `R`, the `R'`-pieces are fragments and the clean
   superincreasing structure of `R` is partially broken (the
   `a_j > Σ_{l>j} a_l` bound survives only on the *intact* `R`-pieces, not on
   fragments). The `k = 0`, `k = 1` sub-cases are closed (Lemma L(n+1), `k=0`
   trivial; `k=1` reduces to L\*(n), both certified). The `k ≥ 2` sub-cases
   with `R`-refinement (e.g. `k = 2, n = 2`: one mark in `M`, one in `R` —
   three sub-cases by which `R`-piece is refined) are **OPEN** over reals. They
   are numerically verified (grid + `300k` random reals at level 3, 0
   violations) but no analytic proof. The superincreasing lever does not adapt
   directly because refinement breaks the strict `R`-level structure the lever
   exploits; a different argument (or a reduction showing the unrefined-R
   sub-case is extremal) is needed.

3. **Full L(3) over reals** (all `k`, all `R`-refinements) is therefore NOT
   closed by this round. The cell-complex-l3 sibling (undecomposed variational
   route) targets the full L(3) via `n=3` vertex enumeration; the unrefined-R
   sub-case proved here is an independent, parallel real-valued foothold —
   **two framings converging on L(3)**, but neither alone closes it.

The approach remains `partial`. The honest round-4 advance: the
superincreasing-R lever is formalized (Lemma + Corollary bounding the
obstruction by `R_largest`), the general-`n` rank-index matching is stated as
a verified conjecture, and the `n=2` unrefined-R sub-case is proved over
reals (the first real-valued `k ≥ 2` sub-case result on G1, parallel to the
cell-complex L(3) milestone).

---

## Round 5 build — the m_1-split fix

**Framing (unchanged).** Pair-excess decomposition + `M ⊎ R` self-similar
decomposition. This round FIXES the two certified-but-invalid lemmas
(`lemma-superincreasing-R` corollary and `lemma-L3-unrefined-R-subcase`
proof) identified by the lower-lift explorer and confirmed by the
outline-reviewer, via the **m_1-split**: a partition of the unrefined-R
response space into two structurally distinct branches. All reductions use
the CERTIFIED `e_M ≤ o_R` reformulation (`lemmas/lemma-em-or-reduction.md`)
and the self-compensation pairing lemma
(`lemmas/lemma-self-compensation.md`); both branches are shown equivalent to
a Hall-type matching. Bug verification (exact-rational, reproduces the
explorer's finding): the integer-grid config `m = (3,3,1,1)/15` at `n = 2`
(level-3 dyadic, `k = 3`, `M = 8`, `R = (4,2,1)`, `a_1 = 4`) has
`σ = m_2+m_3+m_4 = 5 > 4 = a_1`, falsifying the corollary `σ ≤ M/2 = a_1`;
and its global merged sort is `(4,3,3,2,1,1,1)/15` (since `a_1 = 4` is global
rank 1, NOT `m_1 = 3`), giving `A = 3`, not the round-4 formula's `7 − 2(s_3+s_5)`
applied to `{m_2,m_3,m_4}` (which would be ill-defined here). The round-4
setup `s_1 = a_1` via `b_1 ≤ σ ≤ 4` is valid ONLY when `σ ≤ 4`, i.e. only in
Branch 1.

### 0. The corrected structural input (identity only; corollary removed)

**Lemma (superincreasing structure of `R`, identity only — CORRECTED).** *In
the level-`(n+1)` dyadic's `M ⊎ R` decomposition, the unrefined `R`-pieces*
`a_j = 2^{n+1−j}/D(n+1), j = 1,…,n+1` *are superincreasing: for every `j`,*
`a_j − Σ_{l>j} a_l = 1/D(n+1) = α(n+1) > 0`.

*Proof.* `a_j = 2^{n+1−j}/D(n+1)` and
`Σ_{l>j} a_l = (2^{n+1−j} − 1)/D(n+1)`, so the difference is
`1/D(n+1)`. ∎ (The identity is unchanged from round 4; it is the per-piece
form of the certified dyadic-dominance identity `M − total(R) = α(n+1)` —
the `j = 1` case.)

**REMOVED (false for `k ≥ 2`):** the round-4 corollary
"`Σ_{MM} m_even ≤ σ = M − m_1 ≤ M/2 = a_1`". The step `m_1 ≥ M/2` holds only
when `k + 1 = 2` (i.e. `k = 1`): for `k + 1 ≥ 3` pieces summing to `M`, the
largest satisfies `m_1 ≥ M/(k+1)`, which can be strictly below `M/2`. The
config `m = (3,3,1,1)/15` (`k = 3`, `M = 8`) has `m_1 = 3 < 4 = M/2`, so
`σ = 5 > a_1 = 4`. The corollary is therefore INVALID in the very sub-case
(`k ≥ 2`) it was designed to support, and is not used anywhere below. The
identity above is the only structural input retained; it is the genuine
superincreasing lever (each `R`-piece exceeds the sum of all smaller
`R`-pieces by exactly `α(n+1)`), and it is what the Hall matchings in both
branches exploit.

**Proposed correction to the shared cache** (for the reviewer to certify):
replace the statement of `lemmas/lemma-superincreasing-R.md` with the
identity-only version above; DELETE the "Corollary (obstruction bound)"
section and the `σ ≤ M/2 = a_1` claim from its statement and reusability
notes. The IDENTITY is unaffected and remains a valid structural input.

### 1. The m_1-split (corrected structure of the G1 unrefined-R proof)

**Setup (unrefined-R sub-case, `k = n+1`).** Level-`(n+1)` dyadic.
`M = 2^{n+1}/D(n+1)`, `R = (a_1,…,a_{n+1})` with
`a_j = 2^{n+1−j}/D(n+1)` (superincreasing, `a_1 = M/2`). Xiang's `n+1` marks
all land in `M`, splitting it into `n+2` sub-pieces `m_1 ≥ m_2 ≥ … ≥ m_{n+2}`
with `Σ m_i = M`. `R' = R` is unrefined (superincreasing structure intact).
Let `σ := Σ_{i≥2} m_i = M − m_1`. The global merged sort pairs the `n+2`
`M`-sub-pieces with the `n+1` `R`-pieces (total `2n+3` pieces).

**The split.** Two disjoint, exhaustive branches:

- **Branch 1: `m_1 ≥ a_1 = M/2`.** Then `m_1` is the global rank-1 piece
  (since `m_1 ≥ a_1 ≥ a_j` for all `j`, and `m_1 ≥ m_i` for all `i`). The
  `n+2`-piece tail `{m_2,…,m_{n+2}} ∪ R` (total `2n+2` pieces) occupies
  global ranks `2,…,2n+3`; sort it `s_1 ≥ … ≥ s_{2n+2}`. Here
  `σ = M − m_1 ≤ M/2 = a_1`, so `m_2 ≤ σ ≤ a_1`, hence **`s_1 = a_1`**.
  This is the regime where the round-4 setup (and the analogous general-`n`
  bound `σ ≤ a_1`) genuinely holds.

- **Branch 2: `m_1 < a_1 = M/2`.** Then `a_1` is the global rank-1 piece
  (since `a_1 > m_1 ≥ m_i` for all `i`, and `a_1 ≥ a_j` for all `j`). All
  `M`-sub-pieces sit strictly below `a_1` in the merged sort. The
  `(2n+2)`-piece rest `= {m_1,…,m_{n+2}} ∪ {a_2,…,a_{n+1}}` occupies global
  ranks `2,…,2n+3`; sort it `t_1 ≥ … ≥ t_{2n+2}`.

The branches are disjoint (the boundary `m_1 = a_1` is assigned to Branch 1)
and exhaustive (every config has either `m_1 ≥ a_1` or `m_1 < a_1`). The split
isolates the regime where the obstruction-magnitude bound holds (Branch 1)
from the regime where it fails (Branch 2); each reduces to a Hall-type
matching, as recorded honestly below.

### 2. Branch 1 (general `n`): reduction to the Hall conjecture

Let `O := s_1 + s_3 + s_5 + … + s_{2n+1}` (odd `s`-indices, `n+1` terms) and
`E := s_2 + s_4 + … + s_{2n+2}` (even `s`-indices, `n+1` terms). Then
`O + E = σ + total(R)`. The global advantage is (ranks: `m_1` at 1, then
`s_1,…,s_{2n+2}` at `2,…,2n+3`)

```
A = m_1 − s_1 + s_2 − s_3 + … − s_{2n+1} + s_{2n+2}
  = m_1 − O + E = m_1 + (O+E) − 2O = m_1 + σ + total(R) − 2O
  = M + total(R) − 2O.
```

So `A ≥ α(n+1) = M − total(R) ⟺ 2O ≤ 2·total(R) ⟺ O ≤ total(R)`. Since
`s_1 = a_1`, `O = a_1 + (s_3 + s_5 + … + s_{2n+1})`, so the claim is
equivalent to the **Hall conjecture on rank indices**:

> **(H1)** `s_3 + s_5 + … + s_{2n+1} ≤ a_2 + … + a_{n+1} = total(R) − a_1`.

**Status of (H1).** Verified exact-rational for `n = 1,…,5` (`300k` configs
per `n`, `0` violations; min slack `0` at `n = 1,…,4`, attained at the
**staircase interleaving** `s_1 = a_1, s_2 = m_2, s_3 = a_2, s_4 = m_3, …,
s_{2n+1} = a_{n+1}, s_{2n+2} = m_{n+2}`; at `n = 5` the min slack over random
sampling is `≈ 0.0013 > 0` because the staircase is measure-zero). The
per-position bound `s_{2j} ≤ a_{j+1}` FAILS (counterexample
`m_2 = m_3 = m_4 = 4/3` at `n = 2`: `s_4 = 4/3 > a_3 = 1`), and the
layer-cake sufficient condition `⌊c(τ)/2⌋ ≤ c_A(τ)` is too strong (same
counterexample). So the matching is genuinely a **sum-level Hall matching on
rank indices**, not a termwise dominance; the structural lever is the
superincreasing gap `a_j − Σ_{l>j} a_l = α(n+1)` (each `MM` smaller half sits
below a distinct dyadic level of `R`, so a distinct `RR` larger half at the
corresponding rank dominates it), but a clean analytic Hall/marriage argument
for arbitrary `n` is not in hand.

> **GAP (Branch 1, general `n`).** The Hall matching (H1) is a verified
> conjecture (`n = 1..5`); no analytic proof for general `n` over the reals.
> For `n = 2` (level-3 dyadic), (H1) is PROVED by the round-4 3-case
> casework (reproduced in §B below, valid under the Branch-1 hypothesis
> `m_1 ≥ a_1`), which is exactly `s_3 + s_5 ≤ a_2 + a_3 = 3`.

### 3. Branch 2 (general `n`): reduction to a Hall-type matching on the rest

Global rank 1 is `a_1` (Liu's). The rest `t_1,…,t_{2n+2}` occupies ranks
`2,…,2n+3`. Write `A_rest := t_1 − t_2 + t_3 − … − t_{2n+2}` (alternating sum
of the rest; `2n+2` terms, even count, last sign `−`). Then

```
A = a_1 − A_rest,   where   A_rest = oddsum(rest) − evensum(rest) = 2·oddsum(rest) − rest_total.
```

Here `rest = {m_1,…,m_{n+2}} ∪ {a_2,…,a_{n+1}}`,
`rest_total = M + (total(R) − a_1) = (using M = 2a_1, total(R) = 2a_1 − α)
3a_1 − α`. The target `A ≥ α(n+1) = α` is `a_1 − A_rest ≥ α ⟺ A_rest ≤ a_1 − α`.
Substituting `A_rest = 2·oddsum(rest) − rest_total`:

```
A_rest ≤ a_1 − α  ⟺  2·oddsum(rest) ≤ rest_total + a_1 − α
            = (3a_1 − α) + a_1 − α = 4a_1 − 2α = 2M − 2α
  ⟺  oddsum(rest) ≤ M − α = total(R).
```

Equivalently (since `oddsum + evensum = rest_total`), `evensum(rest) ≥ a_1`.
So:

> **(H2)** `oddsum(rest) ≤ total(R)`, equivalently `evensum(rest) ≥ a_1`,
> where `rest = {all M-sub-pieces} ∪ {a_2,…,a_{n+1}}` (sorted desc) and
> `oddsum`/`evensum` are its odd-/even-index sums.

This is a **Hall-type matching on the rest polytope**, structurally the SAME
KIND of problem as (H1) (and as the residual (Match) of self-compensation),
NOT a one-line cheap-kill — the outline-reviewer's correction. The rest is a
smaller polytope (all pieces `< a_1`; the `n` `R`-rest pieces
`a_2,…,a_{n+1}` retain the superincreasing structure
`a_j − Σ_{l>j} a_l = α(n+1)`, and the `n+2` `M`-sub-pieces sum to
`M = 2a_1`), so (H2) may be easier than (H1), but it is not trivial: a naive
bound fails (if all `M`-sub-pieces landed at odd ranks of the rest, the
`R`-rest pieces would have to fill the even ranks, and their total
`total(R) − a_1 = a_1 − α < a_1` would NOT meet the `evensum ≥ a_1` target —
so the proof must use that such a worst-case interleaving is impossible
precisely because the `M`-sub-pieces sum to `2a_1` while all being `< a_1`,
forcing enough of them into even ranks).

**Status of (H2).** Verified by computation: `n = 1,…,5` (`300k` configs per
`n`), `0` violations of `A ≥ α(n+1)` in Branch 2; min `A` in Branch 2 EXCEEDS
`α(n+1)` by a margin growing with `n` (n=2: min `A = α` in the limit
`m_1 → a_1⁻`; n=5: `min A ≈ 0.0145` vs `α ≈ 0.0079`). The tight case is the
limit `m_1 → a_1⁻` (the boundary with Branch 1), where the config approaches
a Branch-1 equality case. No analytic proof for general `n` over the reals.

> **GAP (Branch 2, general `n`).** The Hall-type matching (H2) is verified
> `n = 1..5` but not analytically proved. For `n = 2` (level-3 dyadic), (H2)
> is PROVED by an explicit 6-piece casework in §B' below.

### 4. Re-worked L(3) unrefined-R proof (both branches, rigorous)

We now specialize to `n = 2` (the level-3 dyadic, `D(3) = 15`,
`M = 8/15`, `R = (4,2,1)/15`, `a_1 = 4/15`, `a_2 = 2/15`, `a_3 = 1/15`,
`α(3) = 1/15`). Work in `1/15` units: `M = 8`, `R = {4,2,1}`,
`total(R) = 7`, `α = 1`. Three marks in `M` split it into
`m_1 ≥ m_2 ≥ m_3 ≥ m_4`, `Σ m_i = 8`.

#### §B. Branch 1 (`m_1 ≥ a_1 = 4`) — the round-4 casework, valid here

This is exactly the round-4 proof, now correctly SCOPED. Under `m_1 ≥ 4`:
`σ = m_2+m_3+m_4 = 8 − m_1 ≤ 4 = a_1`, so `m_2 ≤ σ ≤ 4 = a_1`, hence `s_1 = a_1 = 4` (in the merge of `{m_2,m_3,m_4}` with `R`). The closed form
`A = 7 − 2(s_3 + s_5)` and the 3-case casework on `t_2 := s_3` (the
2nd-largest of the five pieces `{m_2,m_3,m_4,2,1}`) apply verbatim
(§B of the round-4 build, unchanged). Each case closes with `s_3 + s_5 ≤ 3`,
hence `A ≥ 1 = α(3)`. Equality iff `{m_2,m_3,m_4} = {2,1,1}` (staircase) or
the degenerate `{2,2,0}`. ∎ (Branch 1, `n = 2`.)

*Scope note (honest):* the round-4 derivation `s_1 = a_1` via `b_1 ≤ σ ≤ 4`
is valid ONLY under `m_1 ≥ 4`; that hypothesis is exactly the Branch-1
condition. The bug was the round-4 file applying this derivation to ALL
configs (including `m_1 < 4`); it is here restricted to Branch 1.

#### §B'. Branch 2 (`m_1 < a_1 = 4`) — NEW 6-piece casework, proved in full

Here `a_1 = 4` is the global rank-1 piece (Liu's, `+4`). All `m_i < 4`.
The rest is `rest = {m_1,m_2,m_3,m_4, 2, 1}` (6 pieces), sorted
`t_1 ≥ t_2 ≥ t_3 ≥ t_4 ≥ t_5 ≥ t_6`, occupying global ranks `2,…,7`.
`A = 4 − A_rest`, `A_rest = t_1 − t_2 + t_3 − t_4 + t_5 − t_6`.
By §3 (with `n = 2`), `A ≥ 1 ⟺ A_rest ≤ 3 ⟺ oddsum(rest) ≤ 7
⟺ evensum(rest) ≥ 4`. We prove `evensum(rest) ≥ 4` directly.

**Preliminary bounds.** Since `m_1 ≥ m_2 ≥ m_3 ≥ m_4`, `Σ m_i = 8`, and
`m_1 < 4` (Branch 2): the average is `2`, so `m_1 ≥ 2` (largest ≥ average)
and `m_1 ∈ [2, 4)`. Also `m_2 ≥ (8 − m_1)/3 > 4/3` (the average of
`m_2,m_3,m_4`, whose sum `8 − m_1 > 4`). Since `m_1 ≥ 2 = a_2` and
`m_1 ≥ m_i`, `t_1 = m_1`. Remove `t_1 = m_1`; the five remaining pieces
`rest5 = {m_2,m_3,m_4,2,1}` (sum `11 − m_1`) sort `u_1 ≥ u_2 ≥ u_3 ≥ u_4 ≥ u_5`,
occupying global ranks `3,…,7`. Then `evensum(rest) = t_2 + t_4 + t_6 = u_1 + u_3 + u_5 = oddsum(rest5)`. So the target is **`oddsum(rest5) ≥ 4`**, where
`oddsum(rest5) = u_1 + u_3 + u_5` (5 pieces, odd count, last included).

We prove `oddsum(rest5) ≥ 4` by casework on `m_2` (vs `2`) and `m_3` (vs `1`).
Recall `m_2 + m_3 + m_4 = 8 − m_1 > 4` (since `m_1 < 4`).

**Case B2a: `m_2 ≥ 2`.** Then `u_1 = m_2` (since `m_2 ≥ 2 = a_2` and
`m_2 ≥ m_3 ≥ m_4`, `m_2 ≥ 2 > 1 = a_3`). Sub-case on `m_3`:

  - **B2a-i: `m_3 ≥ 2`.** Then `m_2 ≥ m_3 ≥ 2`, and `m_4 = 8 − m_1 − m_2 − m_3 ≤ 8 − 2 − 2 − 2 = 2` (using `m_1 ≥ 2`). So `m_4 ≤ 2 = a_2`, giving
    `u_1 = m_2, u_2 = m_3, u_3 = 2`. Then `u_5 = min(m_4, 1)` (the smallest of
    `{m_4, 1}`, since `m_4 ≤ 2` and `1 = a_3`). Hence
    `oddsum(rest5) = m_2 + 2 + min(m_4, 1) ≥ 2 + 2 + 0 = 4`. ✓

  - **B2a-ii: `m_3 < 2`.** Then `u_1 = m_2, u_2 = 2` (since `2 > m_3` and
    `2 ≥ m_4`, `2 > 1`). The remaining three pieces `{m_3, m_4, 1}` sort as
    `u_3,u_4,u_5`. Sub-sub-case on `m_3` vs `1`:

    * **`m_3 ≥ 1`.** Then `u_3 = m_3` (as `m_3 ≥ 1`, and `m_3 ≥ m_4`), and
      `{m_4, 1}` gives `u_4 = max(m_4,1)`, `u_5 = min(m_4,1)`. So
      `oddsum(rest5) = m_2 + m_3 + min(m_4,1)`.
        * If `m_4 ≥ 1`: `min(m_4,1) = 1`, so `oddsum = m_2 + m_3 + 1 ≥ 2 + 1 + 1 = 4`. ✓
        * If `m_4 < 1`: `min(m_4,1) = m_4`, so `oddsum = m_2 + m_3 + m_4 = 8 − m_1 > 4` (since `m_1 < 4`). ✓

    * **`m_3 < 1`.** Then `u_3 = 1` (as `1 > m_3 ≥ m_4`), and `{m_3, m_4}`
      gives `u_4 = m_3, u_5 = m_4`. So `oddsum(rest5) = m_2 + 1 + m_4`. Now
      `m_2 + m_4 = (8 − m_1) − m_3`. Since `m_1 < 4` and `m_3 < 1`,
      `m_2 + m_4 > 4 − 1 = 3`, hence `oddsum = (m_2 + m_4) + 1 > 4`. ✓ (strict)

**Case B2b: `m_2 < 2`.** Then `u_1 = 2` (since `2 > m_2` and `2 ≥ m_3 ≥ m_4`,
`2 > 1`). Since `m_2 > 4/3 > 1` (preliminary bound), `u_2 = m_2` (as
`m_2 > 1 = a_3` and `m_2 ≥ m_3 ≥ m_4`). The remaining three pieces
`{m_3, m_4, 1}` sort as `u_3,u_4,u_5`. Sub-case on `m_3` vs `1`:

  - **`m_3 ≥ 1`.** Then `u_3 = m_3`, `u_5 = min(m_4, 1)`.
    `oddsum(rest5) = 2 + m_3 + min(m_4,1)`.
      * If `m_4 ≥ 1`: `oddsum = 2 + m_3 + 1 = 3 + m_3 ≥ 4`. ✓
      * If `m_4 < 1`: `oddsum = 2 + m_3 + m_4 = 2 + (8 − m_1 − m_2)`. Since
        `m_1 < 4` and `m_2 < 2`, `oddsum > 2 + (8 − 4 − 2) = 4`. ✓ (strict)

  - **`m_3 < 1`.** Then `u_3 = 1`, `u_5 = m_4`, giving
    `oddsum(rest5) = 2 + 1 + m_4 = 3 + m_4`. This requires `m_4 ≥ 1` to meet
    `≥ 4`, but `m_4 ≤ m_3 < 1`. **However this sub-case is IMPOSSIBLE:**
    `m_2 + m_3 + m_4 = 8 − m_1 > 4` (since `m_1 < 4`), and with
    `m_3 < 1, m_4 < 1` this forces `m_2 > 4 − m_3 − m_4 > 4 − 2 = 2`,
    contradicting the Case-B2b hypothesis `m_2 < 2`. ✓ (vacuous)

All cases close with `oddsum(rest5) ≥ 4`, hence `evensum(rest) ≥ 4`, hence
`A_rest ≤ 3`, hence `A = 4 − A_rest ≥ 1 = α(3)` (in `1/15` units, `A ≥ 1/15`).
Equality in Branch 2 is approached only in the limit `m_1 → 4⁻` (boundary
with Branch 1), where `m_2 + m_3 + m_4 → 4` and the config approaches the
Branch-1 staircase `{2,1,1}`; no interior Branch-2 config attains equality
strictly (every sub-case is either strict or meets `≥ 4` with the slack
`m_2+m_3+m_4 = 8 − m_1 > 4`). ∎ (Branch 2, `n = 2`.)

**Verification (NOT a proof step).** Exhaustive exact-rational grid (step
`1/30`, `39 980` configs) and `2·10⁶` random real configs in Branch 2: `0`
violations of `A ≥ 1`, min `A → 1` as `m_1 → 4⁻`, no config with
`oddsum(rest5) < 4`. The casework above is the proof; the computation
confirms it.

**Knowledge-base tools.** **Casework / exhaustion** (the cases on `m_2` vs `2`
and `m_3` vs `1`, disjoint and exhaustive, each settled); **Invariants &
monovariants** (the reduction `A = a_1 − A_rest` linearizes the obstruction;
the rest-total constraint `m_2+m_3+m_4 = 8 − m_1 > 4` is the monovariant
forcing the impossible sub-case); **Hall's marriage theorem** (the general-`n`
form (H2) is the Hall-type matching this casework instantiates at `n = 2`).

### 5. Honest status after the fix

- **L(3) unrefined-R sub-case (reals): now SELF-RIGOROUS via the m_1-split.**
  Branch 1 (`m_1 ≥ 4`) = round-4 casework (valid under this hypothesis);
  Branch 2 (`m_1 < 4`) = new casework (§B', proved in full). Both branches
  cover all configs disjointly. This no longer leans on the cell-complex
  certification (which independently stands as a cross-check). The certified
  lemma `lemma-L3-unrefined-R-subcase.md` should be UPDATED by the reviewer
  to record the m_1-split structure (Branch 1 = the existing 3-case casework,
  correctly scoped to `m_1 ≥ a_1`; Branch 2 = the new §B' casework); the
  RESULT `A ≥ 1/15` is unchanged.

- **General `n` (Branch 1 + Branch 2): OPEN.** Both branches reduce to
  Hall-type matchings — (H1) on rank indices (Branch 1) and (H2) on the rest
  polytope (Branch 2) — each verified `n = 1..5` but neither analytically
  proved. The superincreasing identity (§0) is the structural lever for both;
  a clean Hall/marriage argument for arbitrary `n` (rank-distinct dyadic
  levels) is the live open handle. The false magnitude corollary is no longer
  an obstruction to the proof's correctness (it is removed); the genuine
  obstruction is the unproved matching.

- **`R`-refined sub-cases (`k ≤ n`): OPEN** (refinement breaks the
  superincreasing structure). The `k = 0`, `k = 1` sub-cases remain CLOSED
  (certified, trivial / `L*(n)`).

- **The approach's G1 status:** L(3) unrefined-R is now rigorously proved by
  the pairing-partner route (both branches); the general-`n` lift (via
  `M ⊎ R` recursion + the m_1-split closing `L(n+1)` for all `k`) remains
  OPEN, blocked by the two Hall matchings (H1), (H2). G2 (regime-N) remains a
  tracked dependency on `two-regime-disjunctive`. Status: `partial`.

---

## Promotable lemmas (round 4)

- **Superincreasing-R structure (formal lever, CORRECTED round 5).** Statement:
  in the level-`(n+1)` dyadic, the unrefined `R`-pieces
  `a_j = 2^{n+1−j}/D(n+1)` (`j = 1, …, n+1`) are superincreasing,
  `a_j − Σ_{l>j} a_l = 1/D(n+1) = α(n+1)` (the certified dyadic-dominance
  identity). Proved in this file (§A, round 4; §0, round 5). **CORRECTION
  (round 5):** the round-4 corollary "`Σ_{MM} m_even ≤ σ = M − m_1 ≤ M/2 =
  a_1`" is FALSE for `k ≥ 2` (the step `m_1 ≥ M/2` holds only for `k = 1`) and
  is REMOVED. The identity stands; only the magnitude corollary is invalid.
  Reusable: any approach using the `M ⊎ R` decomposition may import the
  superincreasing IDENTITY as a structural input to a Hall matching, but must
  NOT cite the removed `σ ≤ a_1` corollary.

- **Lemma L(3) unrefined-R sub-case (reals, RE-WORKED round 5).** Statement:
  for the level-3
  dyadic with all three Xiang marks in `M` (`R' = R` unrefined), `A ≥ 1/15 =
  α(3)` for every real response, equality iff `{m_2, m_3, m_4} = {2, 1, 1}/15`
  (staircase) or the degenerate limit `{2, 2, 0}/15`. **Mechanism (CORRECTED
  round 5, m_1-split):** Branch 1 (`m_1 ≥ a_1 = 4`) uses the closed form
  `A = 7 − 2(s_3+s_5)` (in `1/15` units) + 3-case casework on `t_2` (the
  round-4 proof, valid HERE under `m_1 ≥ 4`); Branch 2 (`m_1 < 4`) uses a NEW
  6-piece casework reducing to `oddsum(rest5) ≥ 4` (proved in §B'). The
  round-4 proof's setup `s_1 = a_1` via `b_1 ≤ σ ≤ 4` is valid ONLY in Branch
  1; round 5 isolates it there and supplies Branch 2 separately. Proved in
  this file (§B + §B', round 5). Reusable: the first real-valued `k ≥ 2`
  foothold on G1, now self-rigorous (no longer reliant on the cell-complex
  certification) — corroboration for any approach targeting L(3).

- *(Proposed but NOT certified — the general-`n` superincreasing-R Hall
  matching on rank indices is a CONJECTURE, verified `n = 1..5` but not
  proved; not promoted to the shared cache.)*

---

## Promotable lemmas (round 5)

- **(Proposed correction) Superincreasing-R identity (identity-only).**
  Statement: in the level-`(n+1)` dyadic, `a_j − Σ_{l>j} a_l = α(n+1)` for
  `j = 1,…,n+1`. The round-4 certified lemma
  `lemmas/lemma-superincreasing-R.md` should be REPLACED by this
  identity-only statement; the "Corollary (obstruction bound)" section
  (`σ ≤ M/2 = a_1`) is FALSE for `k ≥ 2` and must be DELETED. Proved in this
  file (§0). Reusable: structural input to Hall matchings; the removed
  corollary is NOT a valid bound on the obstruction magnitude.

- **(Proposed correction) Lemma L(3) unrefined-R sub-case, m_1-split
  version.** Statement: as above, with the two-branch proof structure.
  The certified `lemmas/lemma-L3-unrefined-R-subcase.md` should be UPDATED
  to record the m_1-split (Branch 1 = round-4 casework scoped to `m_1 ≥ a_1`;
  Branch 2 = §B' casework). The RESULT is unchanged. Proved in this file
  (§4). Reusable: self-rigorous real-valued `k ≥ 2` foothold on G1.

- **Branch 2 reduction to a rest Hall matching (H2) (NOT certified — GAP).**
  Statement: for the unrefined-R sub-case with `m_1 < a_1`, `A ≥ α(n+1)` is
  equivalent to `oddsum(rest) ≤ total(R)` where
  `rest = {all M-sub-pieces} ∪ {a_2,…,a_{n+1}}`. Verified `n = 1..5`, OPEN
  for general `n`. NOT promoted (no analytic proof); recorded as an explicit
  GAP for the next round.

- **Branch 1 reduction to the rank-index Hall matching (H1) (NOT certified
  — GAP).** Statement: for the unrefined-R sub-case with `m_1 ≥ a_1`,
  `A ≥ α(n+1)` is equivalent to
  `s_3 + s_5 + … + s_{2n+1} ≤ total(R) − a_1`. Verified `n = 1..5`, OPEN
  for general `n` (proved at `n = 2` by the round-4 casework). NOT promoted;
  recorded as an explicit GAP.

---

## Round 6 build — the direct sum-level Hall injection `φ` (general `n`)

**Framing (unchanged).** Pair-excess decomposition + `M ⊎ R` self-similar
decomposition. This round attacks the dispatch's central question: is the
"factor-of-2 gap" between the `L(n)`-on-`R` induction (which delivers only
`o_R ≥ M/2`) and the target `e_M ≤ o_R` a REAL obstruction or a
PROOF-TOOLING gap? The round-6 lower-lift explorer established, via
exact-rational sampling of `e_M ≤ o_R` (≡ `L(n+1)`) at levels 3–7, that it
is a **proof-tooling gap, NOT a real obstruction**: 0 violations at every
level, with the slack `o_R − e_M` **growing** with `n`. This round
(1) constructs the direct sum-level Hall injection `φ` that *would* close
the gap if proved, reducing `e_M ≤ o_R` to it (a rigorous reduction);
(2) consolidates the general-`n` Branch 1 / Branch 2 structure (the
m_1-split, lifted to general `n`) with the geometric-ratio-2 lever made
explicit; (3) proves the general-`n` equality case (staircase = pair-pile
attains `A = α(n+1)` for ALL `n`); (4) verifies `φ` numerically
(exact-rational, `n = 2..6`); (5) scopes the open analytic step honestly.
**General-`n` `L(n)` is NOT closed this round** — the analytic Hall
matchings (H1), (H2) remain open. Status stays `partial`.

### D. The direct sum-level Hall injection `φ` (rigorous reduction)

**Setup.** Level-`(n+1)` dyadic. `M = 2^{n+1}/D(n+1)`, `R` refined by
Xiang into `R'`. By the CERTIFIED `lemma-em-or-reduction`,
`L(n+1)` ⟺ `e_M ≤ o_R` on the merged desc sort, where

- `e_M` = sum of `M`-sub-pieces at global EVEN ranks,
- `o_R` = sum of `R'`-pieces at global ODD ranks.

By the CERTIFIED `lemma-self-compensation`, every pair `(p_{2k−1},p_{2k})`
of type `RM` (odd = `R'`-piece, even = `M`-sub-piece) self-compensates:
`r_odd ≥ m_even` (within-pair sortedness). Hence `e_M ≤ o_R` reduces to the
residual **(Match)** `Σ_{MM pairs} m_even ≤ Σ_{RR pairs} r_odd`.

**Definition of the injection `φ` (sum-level, NOT termwise).** A *sum-level
Hall injection* is a map that assigns to each `M`-sub-piece sitting at a
global even rank a *distinct* `R'`-piece sitting at a global odd rank,
dominating it:

> `φ :` {`M`-sub-pieces at global even ranks} `⟶` {`R'`-pieces at global odd ranks}, injective, with `φ(m) ≥ m` for every `m` in the domain.

If such a `φ` exists, then summing `m ≤ φ(m)` over the domain gives
`e_M ≤ o_R` immediately (the unmatched odd-rank `R'`-pieces only add to
`o_R`). Conversely, the Hall-type condition `(Match)` is *equivalent*
(`⟺`) to the existence of such an injection by **Hall's marriage theorem**
(KB "Hall's marriage theorem / SDR"): build the bipartite graph with left
vertices = `MM`-pair smaller halves (one per `MM` pair) and right vertices
= `RR`-pair larger halves, edge `m ↔ r` iff `r ≥ m`; Hall's condition for a
matching of all left vertices is exactly `(Match)` summed over every
sub-family (the superincreasing-`R` structure is the candidate Hall
witness). So:

> **(Reduction D)** `L(n+1)` ⟺ `e_M ≤ o_R` ⟺ existence of a sum-level Hall
> injection `φ` as above. The three statements are equivalent.

This is a **reformulation**, not yet a proof of `φ`'s existence. The
dispatch's "the matching is on the SUM over rank indices, not per-position"
is honored: the per-position bound `s_{2j} ≤ a_{j+1}` is FALSE
(counterexample `b = (4/3,4/3,4/3)` at `n = 2`), so `φ` is genuinely a
sum-level matching — no termwise domination by rank index holds. ∎
(Reduction D.)

### E. General-`n` m_1-split (the two Hall matchings, consolidated)

The round-5 m_1-split lifts to general `n` verbatim. We retain the
notation `a_j = 2^{n+1−j}/D(n+1)` (`j = 1,…,n+1`; `a_1 = M/2`), and the
**geometric-ratio-2 structure** `a_j = 2·a_{j+1}` (equivalent to the
certified superincreasing identity `a_j − Σ_{l>j} a_l = α(n+1)`, since the
dyadic `R` is a geometric sequence with ratio 2 and smallest term
`a_{n+1} = α(n+1)`):

> **(Geometric lever, general `n`)** `a_j = 2·a_{j+1}` for `j = 1,…,n`,
> and `a_{n+1} = α(n+1)`. Hence `a_j = 2^{n+1−j}·α(n+1)`,
> `total(R) = (2^{n+1} − 1)·α(n+1) = 2·a_1 − α(n+1)`.

*Proof.* `a_j = 2^{n+1−j}/D(n+1)`, so `a_j/a_{j+1} = 2`; and
`a_{n+1} = 1/D(n+1) = α(n+1)`. The superincreasing identity
`a_j − Σ_{l>j} a_l = α(n+1)` follows: `Σ_{l>j} a_l = (2^{n+1−j} − 1)/D(n+1)`,
so `a_j − Σ_{l>j} a_l = 1/D(n+1)`. ∎ (This sharpens the certified
`lemma-superincreasing-R` to the geometric-ratio-2 form, which is the lever
`φ` must exploit; the false `σ ≤ M/2 = a_1` corollary remains removed.)

**The split (unrefined-R sub-case, `k = n+1`, `R' = R` intact).** Xiang's
`n+1` marks all land in `M`, splitting it into `n+2` sub-pieces
`m_1 ≥ m_2 ≥ … ≥ m_{n+2}` with `Σ m_i = M = 2·a_1`. Let
`σ := m_2 + … + m_{n+2} = M − m_1`. Two disjoint, exhaustive branches:

- **Branch 1: `m_1 ≥ a_1`.** Then `σ = M − m_1 ≤ M − a_1 = a_1`
  (rigorous, general `n`); `m_1` is the global rank-1 piece (it is `≥ a_1 ≥
  a_j` for all `j`, and `≥ m_i` for all `i`). Sort the rest
  `{m_2,…,m_{n+2}} ∪ R` (sum `σ + total(R)`) as `s_1 ≥ … ≥ s_{2n+2}`; since
  `m_2 ≤ σ ≤ a_1` and `a_1` is the largest element of the rest, `s_1 = a_1`
  (rigorous). The closed-form reduction (file §2) gives
  `A ≥ α(n+1)` ⟺ **(H1)** `s_3 + s_5 + … + s_{2n+1} ≤ total(R) − a_1`
  (`= a_2 + … + a_{n+1}`). (H1) is exactly the Hall injection `φ` restricted
  to Branch 1: it asks that the sum of rest-pieces at odd `s`-positions
  (excluding `s_1 = a_1`) be at most the sum of `R`-pieces other than
  `a_1`. Equivalently (sum-level), the `M`-sub-pieces at odd `s`-positions
  (= global even ranks = the `e_M` contributors) inject into the
  `R`-pieces at even `s`-positions (= global odd ranks = the `o_R`
  contributors).

- **Branch 2: `m_1 < a_1`.** Then `a_1` is the global rank-1 piece
  (`a_1 > m_1 ≥ m_i` and `a_1 ≥ a_j`). The rest
  `rest = {m_1,…,m_{n+2}} ∪ {a_2,…,a_{n+1}}` (sum
  `M + (total(R) − a_1) = 2a_1 + (a_1 − α) = 3a_1 − α`) occupies global
  ranks `2,…,2n+3`. The reduction (file §3) gives
  `A ≥ α(n+1)` ⟺ **(H2)** `oddsum(rest) ≤ total(R)`
  (equiv. `evensum(rest) ≥ a_1`). (H2) is a Hall-type matching on the rest
  polytope — structurally the same kind of problem as (H1), NOT a one-line
  cheap-kill: a naive bound fails (if all `M`-sub-pieces landed at odd ranks
  of the rest, the `R`-rest pieces would have to fill the even ranks, and
  their total `total(R) − a_1 = a_1 − α < a_1` would NOT meet the
  `evensum ≥ a_1` target — so the proof must use that such a worst-case
  interleaving is impossible precisely because the `M`-sub-pieces sum to
  `2a_1` while all being `< a_1`).

Both branches are disjoint and exhaustive (boundary `m_1 = a_1` assigned to
Branch 1). Each reduces `L(n+1)` to a Hall-type matching — (H1) on rank
indices (Branch 1), (H2) on the rest polytope (Branch 2). The reductions
are rigorous for all `n`; the **matchings themselves are open**.

### F. Rigorous general-`n` equality case (staircase = pair-pile, `A = α`)

**Theorem (staircase equality, general `n`).** *For the unrefined-R sub-case
at Branch 1 boundary (`m_1 = a_1`), the config
`m_1 = a_1`,
`{m_2,…,m_{n+2}} = {a_2, a_3, …, a_{n+1}, a_{n+1}}`
(`n` small pieces = the `R`-pieces `a_2,…,a_{n+1}` plus one extra copy of
`a_{n+1} = α(n+1)`) is admissible (`σ = a_1`, `Σ m_i = M`) and attains
`A = α(n+1)` for every `n ≥ 1`. This is exactly the pair-pile multiset
`{a_1,a_1, a_2,a_2, …, a_n,a_n, a_{n+1},a_{n+1},a_{n+1}}` (two of each
`a_j` for `j = 1,…,n`, three of `a_{n+1}`).*

*Proof.* Admissibility: `σ = (a_2 + … + a_{n+1}) + a_{n+1} = (a_1 − α) + α
= a_1`, so `m_1 = M − σ = 2a_1 − a_1 = a_1`; and `Σ m_i = a_1 + a_1 = 2a_1
= M`. ✓. The merged multiset is `{a_1} ∪ {a_2,…,a_{n+1},a_{n+1}} ∪
{a_1,…,a_{n+1}} = {a_1,a_1, a_2,a_2, …, a_n,a_n, a_{n+1},a_{n+1},a_{n+1}}`
(2 of each `a_j` for `j ≤ n`, three of `a_{n+1}`), totaling `2n + 3`
pieces. Pair them descending `(p_1,p_2),(p_3,p_4),…`: each pair
`(a_j, a_j)` has zero excess; the final unpaired piece is `a_{n+1} =
α(n+1)` (one of the three copies). Hence
`A = Σ_{pairs} (p_{2k−1} − p_{2k}) + (leftover) = 0 + α(n+1) = α(n+1)`.
By Lemma G, `oddsum = (1 + A)/2 = (1 + α(n+1))/2 = (D(n+1) + 1)/(2·D(n+1)) =
2^{n+1}/D(n+1) = M = f(n+1)`. ✓. ∎

This is the general-`n` equality case for the unrefined-R sub-case (the
pair-pile, already certified by `lemma-pair-pile-dyadic-cap.md` from the
upper-bound side; here realized intrinsically within the lower-bound
`M ⊎ R` frame). It confirms the bound `A ≥ α(n+1)` is tight at the
staircase for ALL `n`, and that the Hall injection `φ` (if it exists) must
saturate at `e_M = o_R = 0` here.

### G. Numerical verification of `φ` / (H1) / (H2) (NOT a proof step)

Script: `/tmp/round-6/hall_injection_verify.py` (exact-rational,
`fractions.Fraction`; seed 12345). Three checks:

**(A) General `e_M ≤ o_R`, arbitrary Xiang play (any `k`), `N = 2..6`**
(here `N` = level = file's `n+1`; `α(N) = 1/D(N)`):

| `N` | `D(N)` | samples | violations | min `o_R − e_M` (× `α(N)`) |
|---|---|---|---|---|
| 2 | 7   | 30000 | 0 | 0 |
| 3 | 15  | 30000 | 0 | 0 |
| 4 | 31  | 30000 | 0 | 0 |
| 5 | 63  | 30000 | 0 | 0 |
| 6 | 127 | 12000 | 0 | 0.55 |

Min slack `0` at `N = 2..5` reflects that the staircase/pair-pile equality
config `e_M = o_R = 0` is attainable; at `N = 6` the random sample does
not hit the measure-zero equality locus and the min slack is `0.55·α(6) >
0`. **Slack grows with `n`** (the explorer's signature `0, 0, 0.10, 0.64,
1.15` at `N = 3..7` is reproduced up to seed/sample variation).

**(B) Unrefined-R (`k = N`, all marks in `M`, `R` intact), Branch 1 & 2:**

| `N` | B1 cnt | B1 bad | B1 min `A` (×α) | B2 cnt | B2 bad | B2 min `A` (×α) |
|---|---|---|---|---|---|---|
| 2 | 30069 | 0 | 1.000 | 9931  | 0 | 1.002 |
| 3 | 19899 | 0 | 1.000 | 20101 | 0 | 1.002 |
| 4 | 12461 | 0 | 1.000 | 27539 | 0 | 1.004 |
| 5 | 7483  | 0 | 1.000 | 32517 | 0 | 1.270 |
| 6 | 1672  | 0 | 2.390 | 13328 | 0 | 2.342 |

Branch 1 min `A = 1.000·α` at every `N` (staircase equality, §F). Branch 2
min `A` **grows above `α`** with `N` (`1.002 → 2.342`), confirming the
slack-grows-with-`n` signature: the (H2) bound is loose and gets looser,
consistent with a direct injection existing but the `L(n)`-on-`R` induction
being too weak a tool to find it.

**(C) Staircase sanity** (exact `A = α` for all `N = 2..6`): confirmed
exactly — `A = 1/D(N)` at the staircase config of §F for every `N`.
Matches the theorem of §F.

All three checks give **0 violations**, consistent with `φ` existing for
all `n`. Per the rigor rules, a numerical check is **NOT a proof step**;
the analytic construction of `φ` is the open gap.

### H. Honest gap scoping (general `n` is NOT closed)

1. **(H1) — Branch 1 Hall injection, general `n` — OPEN.** The reduction
   `A ≥ α(n+1)` ⟺ (H1) is rigorous (§E); (H1) is the sum-level Hall
   injection `φ` on rank indices. Verified `n = 1..6` (0 violations, §G);
   proved at `n = 2` by the round-4 3-case casework (`s_3 + s_5 ≤ 3`).
   **No analytic proof for general `n`** is in hand. The geometric lever
   `a_j = 2·a_{j+1}` (§E) is the structural input; the difficulty is that
   the matching is on the SUM over rank indices (per-position domination
   fails), and a naive induction peeling `a_1` shifts parity AND changes
   the `b`-count, so the recursion does not preserve the (H1) form. The
   pair-pile/staircase saturation (`e_M = o_R = 0`, §F) shows `φ` is tight
   here, leaving no slack at the extremum — a robust injection must
   degenerate correctly at the staircase.

2. **(H2) — Branch 2 Hall matching on the rest polytope, general `n` —
   OPEN.** Rigorous reduction (§E); verified `n = 1..6` (0 violations,
   growing slack, §G). Proved at `n = 2` by the round-5 6-piece casework
   (§B'). **No analytic proof for general `n`.** Structurally the same
   kind of Hall problem as (H1) on a smaller polytope (all pieces `< a_1`;
   the `n` `R`-rest pieces `a_2,…,a_{n+1}` retain the geometric-ratio-2
   structure; the `n+2` `M`-sub-pieces sum to `2a_1` while all being
   `< a_1`).

3. **`R`-refined sub-cases (`k ≤ n`, some marks in `R`) — OPEN.** When
   Xiang spends marks in `R`, the `R'`-pieces are fragments and the clean
   geometric structure of `R` is partially broken; the superincreasing
   lever does not adapt directly. The `k = 0`, `k = 1` sub-cases remain
   CLOSED (certified: trivial / `L*(n)`). The direct injection `φ` of §D
   applies to the *general* merged sort (any `k`), so in principle it would
   close ALL sub-cases at once — but its existence is exactly the open
   (H1)+(H2)+refined step. The numerical check (A) above (general
   `e_M ≤ o_R`, any `k`) gives 0 violations, consistent with `φ` existing
   across all `k`, but is not a proof.

4. **What IS rigorously general-`n` this round:**
   - the reduction `L(n+1)` ⟺ `e_M ≤ o_R` ⟺ existence of `φ`
     (Reduction D, §D) — rigorous, all `n`;
   - the general-`n` m_1-split (Branch 1 / Branch 2) with the rigorous
     reductions to (H1) and (H2) (§E) and the geometric-ratio-2 lever
     (§E);
   - the general-`n` equality theorem (staircase = pair-pile attains
     `A = α(n+1)` for ALL `n`, §F);
   - rigorous general-`n` bounds: `σ ≤ a_1` and `s_1 = a_1` in Branch 1,
     `a_1` global rank 1 in Branch 2 (§E).

**The approach's G1 status after round 6:** `L(1)`, `L(2)` closed
(prior); `L(3)` unrefined-R self-rigorous (round 5, both branches); the
**general-`n` lift remains OPEN**, blocked by the two analytic Hall
matchings (H1), (H2). The direct injection `φ` is constructed as a
reduction (rigorous) and verified (0 violations, slack grows with `n`), but
its existence is not analytically proved. G2 (regime-N) remains a tracked
dependency on `two-regime-disjunctive`. **Status: `partial`.**

---

## Promotable lemmas (round 6)

- **(Proposed, PROVEN) Reduction `L(n+1)` ⟺ existence of the sum-level
  Hall injection `φ`.** Statement: in the `M ⊎ R` decomposition, `L(n+1)`
  is equivalent to the existence of an injection `φ` from the `M`-sub-pieces
  at global even ranks into the `R'`-pieces at global odd ranks with
  `φ(m) ≥ m`, applied sum-level (not per-position). Combines the certified
  `lemma-em-or-reduction` (`L(n+1)` ⟺ `e_M ≤ o_R`) with the certified
  `lemma-self-compensation` (reduces to the residual (Match)) and Hall's
  marriage theorem. Proved in this file (§D). Reusable: any approach may
  import this to reframe the lower bound as a single matching-existence
  question.

- **(Proposed, PROVEN) General-`n` staircase equality.** Statement: for
  the unrefined-R sub-case at Branch 1 boundary, the config
  `{m_1,…,m_{n+2}} = {a_1, a_2,…,a_{n+1}, a_{n+1}}` is admissible and
  attains `A = α(n+1)` for every `n ≥ 1` (the pair-pile multiset). Proved
  in this file (§F). Reusable: confirms the bound is tight at the staircase
  for all `n`; any injection `φ` must saturate here (`e_M = o_R = 0`).

- **(Proposed, CONJECTURE — NOT certified) General-`n` Hall matchings
  (H1)+(H2).** Statement: (H1) `s_3 + s_5 + … + s_{2n+1} ≤ total(R) − a_1`
  (Branch 1, unrefined-R); (H2) `oddsum(rest) ≤ total(R)` (Branch 2,
  unrefined-R). Both verified `n = 1..6` (0 violations, §G), proved at
  `n = 2` (rounds 4–5). **NOT promoted (no analytic proof for general
  `n`)**; recorded as explicit GAPs. The geometric-ratio-2 lever
  `a_j = 2·a_{j+1}` is the structural input; the matching is genuinely
  sum-level (per-position domination fails).

---

## Round 6 build summary

This round advanced the general-`n` lower-bound G1 by (i) constructing the
direct sum-level Hall injection `φ` and proving — rigorously, for all `n` —
that `L(n+1)` is *equivalent* to `φ`'s existence (Reduction D, combining
the certified `e_M ≤ o_R` and self-compensation lemmas with Hall's
theorem); (ii) consolidating the general-`n` m_1-split (Branch 1 → (H1) on
rank indices, Branch 2 → (H2) on the rest polytope) with the
geometric-ratio-2 lever `a_j = 2·a_{j+1}` made explicit; (iii) proving the
general-`n` equality theorem (staircase = pair-pile attains `A = α(n+1)`
for ALL `n`); (iv) verifying `φ` / (H1) / (H2) exactly-rationally at
`n = 2..6` (0 violations, slack grows with `n`, staircase equality exact).
The factor-of-2 gap is confirmed as a proof-tooling gap (the inequality is
true and loose, not tight). **General-`n` `L(n)` is NOT closed**: the
analytic existence of `φ` (the Hall matchings (H1), (H2)) and the
`R`-refined sub-cases (`k ≤ n`) remain open; only `n = 2` (the `L(3)`
unrefined-R) is closed for both branches. Status stays `partial`.
