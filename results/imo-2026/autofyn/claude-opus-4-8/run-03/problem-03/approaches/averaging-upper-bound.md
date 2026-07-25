## Status
partial

## Approaches tried
- **averaging-upper-bound** (round 4, this file, NEW) — UB via convex combination of the two
  top-part moves, `min(MATCH,BISECT) ≤ p·MATCH+(1−p)·BISECT` (Opening 4 / crux aimo-0198),
  aiming to close `U_k(A) ≤ sum(A)/D_k` without deciding which branch wins.
  **Outcome: the mechanism is REFUTED at the scoped (top-part) level by the mandated fast-fail
  probe.** Even the *min* of the two top-part branches (the best any convex average can be, since
  every average is `≥` the min) already exceeds the target for `k ≥ 2`. Explicit exact
  counterexample: `A = {2,2,1}` (sum 5), `k = 2`, target `s/D_2 = 5/7`, but every strategy whose
  first move is a top-part MATCH or BISECT is stuck at value `1 > 5/7`, while the true value is
  `U_2 = 0` (attained by BISECTing the *small* part `1`, a non-top move the top-part S-effect
  formulas cannot express). Documented in full below as a durable negative lemma so no future
  round retries the top-part averaging. Recommend **RETHINK** of the framing (see Spec concerns).

## Current best
A rigorous **impossibility result** for the outlined mechanism, plus the reduction context and a
positive numerical confirmation that the true (any-part) strategy does reach the target. These
are durable outputs; the upper bound itself remains open (the field-wide crux, 3+ rounds).

### Setup (imported, certified)
Homogeneous value function on integer multisets (L1 reduction, L2/L3 potential):
- `S(A) = Σ_i (−1)^{i+1} a_(i)` (alternating sum of the descending sort); `S = meas{N_A(t) odd}` (L3).
- `U_k(A) := min over ≤k-cut refinements B of S(B)`, with the exact recursion (R)
  `U_0(A) = S(A)`, `U_k(A) = min( S(A), min_{one split A→A'} U_{k−1}(A') )`,
  where a *split* replaces one part `p` by two positive parts summing to `p`.
- `D_k = 2^{k+1} − 1`, `D_k = 2 D_{k−1} + 1`.
- **Lemma B (the whole upper bound):** `U_k(A) ≤ sum(A)/D_k` for every `A`. Applied at `k=n`,
  `sum=1`, this is `max_A min_B S(B) ≤ 1/D_n`; with Lemma A (LB) it pins `c(n) = 2^n/D_n`.

The two canonical **top-part** moves (exact S-effect certified in induction-peel §4): with
`a_1 ≥ a_2 ≥ …`, `s = sum`, `ρ = s − a_1`, `r = a_1/ρ`,
- **BISECT_top:** `a_1 → (a_1/2, a_1/2)` (caps `a_1`'s rank-1 contribution at `a_1/2`; by L3 it
  flips `N`-parity on `(0, a_1/2) ∪ (a_1/2, a_1)`).
- **MATCH_top:** `a_1 → (v, a_1 − v)` for a smaller present value `v` (the twin `v` cancels at
  adjacent rank by L4, carry `a_1 − v` re-enters a smaller subgame).

### The averaging plan and why it cannot close (the refutation)
The outlined plan is: for `|A| ≥ 2`,
```
U_k(A) ≤ min( U_{k−1}(MATCH_top(A)), U_{k−1}(BISECT_top(A)) )
       ≤ p·U_{k−1}(MATCH_top(A)) + (1−p)·U_{k−1}(BISECT_top(A))   for any p ∈ [0,1],
```
and then to pick `p = p(r)` and a profile IH so the two-term average telescopes to `s/D_k`.

**Obstruction 1 (the min–average gap runs the wrong way).** For any reals `X, Y` and `p ∈ [0,1]`,
`p·X + (1−p)·Y ≥ min(X,Y)`. Hence the averaged quantity is *never smaller* than the min of the
two branches. So the averaging bound can only close if the **min itself** already satisfies
`min( U_{k−1}(MATCH_top), U_{k−1}(BISECT_top) ) ≤ s/D_k`. The averaging therefore cannot rescue a
situation where the min of the two top-part branches overshoots — it is strictly weaker than the
min-of-branches step that the exhausted branch-inequality route already tried.

**Obstruction 2 (the min of the two top-part branches overshoots — exact counterexample).**
The first move of an optimal strategy need not be a top-part move. Take
```
A = {2, 2, 1},  sum s = 5,  k = 2,  target s/D_2 = 5/7 ≈ 0.7143.
```
- BISECT_top: `2 → (1,1)` gives `{2,1,1,1}`. MATCH_top with `v = 1`: `2 → (1,1)` gives the same
  `{2,1,1,1}`. (These are the only two top-part first moves, since the top value is `2` and the
  only smaller present value is `1`.)
- With the remaining `k−1 = 1` cut, `U_1(\{2,1,1,1\}) = 1`: the parity-`+`-ranked `2` is
  unmatched; one cut cannot pair it off (bisecting `2→(1,1)` gives `{1,1,1,1,1}`, `S = 1`; any
  other single cut is `≥ 1`). Verified exactly (Fraction arithmetic).
- Hence `min( U_{1}(MATCH_top(A)), U_{1}(BISECT_top(A)) ) = 1 > 5/7`.

By Obstruction 1, every convex average of the two branches is `≥ 1 > 5/7` as well. So **no weight
`p` (whether a function of `r` alone, or of the full profile) makes the averaged bound reach the
target here.** Yet the true value is `U_2(A) = 0`, attained by **BISECTing the small part `1`**
into `(1/2, 1/2)`: `B = {2, 2, 1/2, 1/2}`, `S(B) = 2 − 2 + 1/2 − 1/2 = 0`. This winning move is a
*non-top* split, which the top-part MATCH/BISECT S-effect formulas do not express.

**Refutation Lemma (top-part averaging cannot prove Lemma B).** *For every choice of weights
`p(·)`, the top-part convex-combination bound fails: there exist `A` and `k ≥ 2` with*
`p·U_{k−1}(MATCH_top(A)) + (1−p)·U_{k−1}(BISECT_top(A)) > sum(A)/D_k`, *because already
`min` over the two top-part branches exceeds `sum(A)/D_k` (witness `A={2,2,1}`, `k=2`, value `1`
vs target `5/7`). ∎*

This is rigorous (finite exact computation) and it kills the mechanism as outlined. The
root cause is structural: **which part XY should split is part of the decision**, and on
`{2,2,1}` the correct part is the *smallest*. Restricting the first move to the top part
(the only regime in which the certified S-effect formulas apply) provably forfeits the target.

### Why broadening to any-part moves does not rescue the *averaging* idea
Admitting non-top splits does restore feasibility (see the positive check below), but it destroys
the two-option structure the averaging relied on. The optimal first move's target part depends on
the profile — verified exactly:
- on the dyadic maximizers it is the **top** part (e.g. `G_2=\{4,2,1\}`: bisect `4`; `G_3`: bisect `8`),
- on `\{4,4,2,1\}` it is the **rank-3** part (bisect the `2`),
- on `\{2,2,1\}` it is the **smallest** part (bisect the `1`).
Choosing among "bisect part 1 / bisect part i / match …" is exactly the profile-dependent
case-split (explorer finding F1: no `(a_1, s)`-only closed form). Averaging over a *fixed* pair of
moves cannot absorb this; picking the pair per state *is* the case-split the mechanism was meant to
avoid. So the aimo-0198 "min ≤ average of the two available options" transplant does not apply:
our minimizer has more than two structurally-relevant options, and the two named ones (top
MATCH/BISECT) are not the ones that win in general.

### Positive facts established this round (durable)
1. **Lemma B is achievable and the target is correct.** With the full canonical move set (BISECT
   *any* part, or MATCH *any* part down to any smaller present value), the exact value function
   satisfies `U_k(A)·D_k ≤ 1` on 1500 random `A` each for `k = 1,2,3` (max observed `0.9997`,
   `0.9153`, `0.6492`). This confirms Lemma B numerically and that the crux is the *proof*, not
   the statement.
2. **The winning strategy must split non-top parts.** In particular it bisects *small unmatched*
   parts to cancel them (matching/`β = Σ_even` view, L4: XY maximizes the matched-smaller mass
   `β`, and cancelling an unmatched small part raises `β`). Future UB attempts should model the
   whole-profile split choice, not a top-part rule.

### Explicit remaining gap (unchanged field-wide crux)
> **Open (Lemma B / upper bound).** Prove `U_k(A) ≤ sum(A)/D_k` for all `A`. The top-part
> averaging mechanism is refuted (above). A working proof must either (i) supply a whole-profile
> strategy that legitimately telescopes with `D_k = 2D_{k−1}+1` (matching/`β` view is the most
> promising language), or (ii) a global majorization certificate (explorer Opening 3) — both still
> open. The recursion (R), base case (`U_0 = S ≤ sum`, P2), and the exact top-part S-effect
> formulas remain valid ingredients; they are just insufficient by themselves.

## Full proof
Not present — Status is partial. The upper bound remains open; only the impossibility of the
outlined top-part averaging mechanism is established rigorously this round.

## Promotable lemmas
- **Refutation of top-part UB averaging (negative lemma).** For the value function `U_k` of the
  multiset-refinement game and any weights `p(·)`, the bound
  `min(U_{k−1}(MATCH_top(A)), U_{k−1}(BISECT_top(A))) ≤ sum(A)/D_k` — hence any convex average of
  the two top-part branches — is FALSE for `k ≥ 2`. Exact witness: `A = {2,2,1}`, `k = 2`; both
  top-part first moves lead to `{2,1,1,1}` with `U_1 = 1`, while `sum/D_2 = 5/7` and the true
  `U_2 = 0` (bisect the small part). Proof is a finite exact computation (Section above). Reusable
  to prune the entire "restrict XY's first move to the top part" family of UB attempts. *(Recommend
  the reviewer certify this as a "do-not-retry" negative lemma rather than a positive import.)*

## Spec concerns
- **RETHINK recommended for this slug's framing.** The averaging-of-two-top-moves mechanism is
  refuted, not merely stalled: the min of the two branches — an *upper* bound on how good any
  average can be — already exceeds the target. Any salvage must (a) admit non-top splits (which
  breaks the two-option averaging structure and reintroduces the F1 case-split), or (b) abandon
  averaging for a whole-profile strategy/certificate. The outliner should re-plan the UB attack;
  the most promising untried language is the `β = Σ_even` (min-pairing, L4) "cancel unmatched
  small parts" strategy, or the global majorization certificate (explorer Opening 3), neither of
  which is a top-part rule.
- The answer `c(n) = 2^n/D_n` is unaffected and remains numerically confirmed for `n ≤ 3`.
