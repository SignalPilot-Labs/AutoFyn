# Build report — ll-inclusion-gap, round 11 (Status: partial)

## Summary
Advanced G-INC-2 (refined-R INC branch of Lemma LL). **CLOSED the `a < 1` top-cut sub-branch of
G-INC-2nt for ALL `n`** — rigorously, not just numerically — plus Opening B (general `h=0` kill) and
Opening D (lower-band cut clean descent, closed for cut value `< 1`). The `a ≥ 1` cut is the honest hard
residual, left explicit and un-closed (not overclaimed). All work in `approaches/ll-inclusion-gap.md`
Step 24; new promotable lemma `lemmas/sigma-family-a-lt-1.md`.

## What was proven (rigorous, all `n`)
1. **The key fix (Step 24.0):** the round-10 obstruction for the `a<1` family was a *bookkeeping* error,
   not a real block. Parametrizing by the sum-excess **relative to `2^k`** loses a factor `a` at the
   entry step (I verified this fails: it yields only `1 − a + 2b`). Parametrizing by
   `σ := ΣQ − ΣX` (excess over the *object's own* sum) makes the top-level cut `R` and the family
   `F_k = {a}∪G_{k−1}` obey the **identical** recursion `σ_lo = σ + a_v − b`, `deficit_top = a_v + b`.
2. **Family Lemma `F_a` (Step 24.1, PROVEN):** `A(F_k) − A(Q) ≥ min(σ, 2−σ)` for `S_Q⊆S_{F_k}`,
   `|Q|≤k`, `σ∈(0,2)`. Strong `k→k−2` induction; same arithmetic as certified `t-ell-mutual-induction`;
   the "tent" peaks at `σ=1` giving the target `≥1`. The family is genuinely descent-closed
   (`F_k → F_{k−2}`, top two pieces `2^{k−1},2^{k−2}` structurally uncut, `h=2` every level), so the R10
   O1 parity break provably cannot fire — this is the specific family the reviewer verified as distinct
   from the refuted abstract `{Claim_R,T_R}` class. Bases `k=1` (vacuous), `k=2` (direct, full casework).
   I hand-traced every case with the extra piece `a` present, as the reviewer demanded.
3. **Top-cut closure (Step 24.2):** one Gen-Decomp step sends `a<1` top-cut `R` into `(Q_lo, F_{n−2})` at
   `σ=1`; `h=0`/`h≥4`/`h=2` (2a/2b-i/2b-ii) all give `A(R)−A(Q) ≥ 1`, all `n≥3`.
4. **Opening B generalized (Step 24.3):** for ANY refined `R`, `h=0` closes when the top band carries
   `S_R`-measure `≥1` (`= 2^{n−2}−a` for the top cut, closed for `a ≤ 2^{n−2}−1`).
5. **Opening D — G-INC-2lb (Step 24.4):** a lower-band cut keeps `R_hi={2^{n−1},2^{n−2}}` uncut (full top
   band, `h_R=2`) and descends `n→n−2` to `G_{n−3}` with the SAME cut. Clean self-similar reduction;
   **fully closed when the cut value `c<1`**; otherwise reduces to a small-level `a≥1` cut.

## Honest residual (OPEN — NOT overclaimed)
- **G-INC-2nt `a ≥ 1`:** the family `{a}∪G_{k−1}` loses descent-closure — once `a ≥ 2^{k−4}` the count
  `#{parts ≥ 2^{k−4}}` can go odd (O1 fires for THIS family too). Needs a direct `A(R)` evaluation
  (`A(R)=A(G_{n−1})` for `n` even, `A(G_{n−1})−2a` for `n` odd); not carried out. This is the genuine
  hard residual singled out by the dispatch/reviewer.
- **G-INC-2lb with terminal cut value `c ≥ 1`:** inherits the same `a≥1` difficulty at the small level.
- **G-INC-2e⁺** (`m≥6`) and **G-GAP** (non-containment): unchanged, open.

## Verification (budget-enforced, all runs <20s, incremental)
- `A == measure(S_odd)` identity: 200 random configs OK.
- Family bound `A(F_k)−A(Q) ≥ min(σ,2−σ)`: 0 violations, 1932 configs (`k=2,3,4`, `a∈{1/4,3/4}`, grid 1/4).
- Top-level `a<1`: 0 violations — `n=3,4` (122 configs, margin ≥5/3) and `n=5, a=1/2` (130 configs,
  margin 3). Joint budget `|Q| ≤ n` enforced; `S_Q ⊆ S_R` enforced.

## Spec / rigor notes
- No re-opening of the refuted abstract `{Claim_R,T_R}` class or generalized-L1 (both dead). The `a<1`
  family is a *specific* descent-closed parametric family; the O1 witness `{1,2,2,2,8,16,32}` and the
  Claim-false witness `{1,3,3}` are NOT in it.
- The proof stands on its own; numerics are only sanity checks, never proof steps.
- Everything invoked is named: Gen-Decomp, Parity-Condition, Forcing Lemma, `set-identity-selfsimilar`
  (`A(G_j)≥1`), `alt-sum-integral` (measure/merge). All certified.

## Files
- `results/imo-2026-03/approaches/ll-inclusion-gap.md` — Step 24 (new), updated Status/Approaches/Current
  best/Promotable lemmas.
- `results/imo-2026-03/lemmas/sigma-family-a-lt-1.md` — NEW promotable Family Lemma `F_a` (for reviewer
  certification).

Recommended verdict: CHANGES REQUESTED (real progress, approach stays live; `a≥1` residual remains).
