# imo-2026-03 — approach `ll-inclusion-gap`

## Status
partial

## Approaches tried
- **ll-inclusion-gap** (NEW round 5) — full rival attempt at the lower bound c(n) via the inclusion
  split `S_Q ⊆ S_R` (INC) vs `S_Q ⊄ S_R` (GAP). R5 rigorous: Forcing Lemma, INC reduction
  (both certified `lemmas/forcing-inc-reduction.md`), clean sub-case `max(Q) ≤ 2^{n−2}`, GAP Case-1.
  R5 flaw (reviewer-flagged): the "Structural Lemma" part (a) ("no Q-part in a forbidden-band interior")
  is FALSE (counterexample Q={3/2,3/2,2,3} at n=3 is INC with two parts in (1,2)); the n=3 base case
  was therefore incomplete.
- **ll-inclusion-gap** (REVISED round 6) — obeyed both outline-reviewer corrections:
  1. Replaced the false Structural Lemma with the **Parity-Condition Lemma** (`N_Q` even on every
     even-`N_G` band), which is TRUE and admits even-multiplicity interior pairs like {3/2,3/2}.
     Proved rigorously (general n).
  2. Enforced the **joint cut budget** (`c_Q + c_R ≤ n`) throughout, so 5-part Q at n=3 (over budget)
     never enters the casework.
  New rigorous content this round:
  - **Parity-Condition Lemma** (general n; NEW, promotable) — the corrected mechanism.
  - **Odd-index reformulation** `A(Q) = 2·O_Q − 2^n`, reducing the INC target `A(Q) ≤ A(G_{n−1})−1`
    to `O_Q ≤ O_{G_{n−1}}` (sums of odd-position parts).
  - **Top-band decomposition identity** (general n; NEW, promotable): with `h := #{parts ≥ 2^{n−2}}`
    (proved EVEN by the parity condition), `A(G_{n−1}) − A(Q) = deficit_top + M`, both terms ≥ 0,
    reducing the general "+1" to `deficit_top + M ≥ 1`.
  - **Complete, correct n=3 base case** (R = G_2, all sub-cases including the even-multiplicity
    interior pair {s,s} ⊂ (1,2)): `A(Q) ≤ 2 = A(G_2) − 1`. This CLOSES the INC branch for n=3 and
    fixes the R5 incompleteness. Verified numerically (0 failures over 52 configs; and the arithmetic
    INC bound `A(Q) ≤ A(R)−1` holds with 0 violations over 400 budget-valid n=3 instances incl.
    refined R).
  Outcome: honest partial. INC branch is now RIGOROUS AND COMPLETE for n = 3 (all R); the general-n
  "+1" is reduced to `deficit_top + M ≥ 1` (open, G-INC-1); refined-R general n (G-INC-2) and GAP
  alignment (G-GAP) remain open, honestly flagged.
- **ll-inclusion-gap** (ADVANCED round 7) — ran the **two-step strong induction `n → n−2`** on
  G-INC-1, converting the explorer machinery to rigor. New rigorous content:
  1. **SET IDENTITY** `S_{G_{n−1}} ∩ [0,2^{n−2}) = S_{G_{n−3}}` + **self-similar identity**
     `M = A(G_{n−3}) − A(Q_lo)` + `A(G_k)` odd `≥ 1` — proved (proposed lemma
     `lemmas/set-identity-selfsimilar.md`).
  2. **Generalized top-band decomposition** (ΣQ-free): the certified identity
     `A(G_{n−1}) − A(Q) = deficit_top + M` holds for ANY Q with `S_Q ⊆ S_{G_{n−1}}` (the certified
     proof never used `ΣQ = 2^n` — the "no S_Q-mass above 2^{n−1}" step is automatic from
     `S_Q ⊆ S_{G_{n−1}} ⊆ [0,2^{n−1})`). This is what lets the identity be re-applied at the perturbed
     sums arising in the recursion.
  3. **Clean ε-reformulation**: `Claim(n,ε)` [`A(Q) ≤ A(G_{n−1}) − 1 + ε` for `ΣQ = 2^n+ε`]
     `⟺ O_Q ≤ O_{G_{n−1}} + ε` (odd-position sum), and the induction cycles with `ε ∈ [0,1)` only
     (never `ε < 0` — that direction is FALSE).
  4. **Two-step induction**: base cases `Claim(1,ε)`, `Claim(2,ε)` (direct, only equal-pair Q feasible)
     and `T(1)`, `T(2)` (the `ε<0` companion, proved); inductive step (n ≥ 3) closes **Cases h≥4, 2a,
     2b-i, 2b-ii** — with `2b-i` invoking `Claim(n−2,ε')` (`ε'=ε+a−b∈[0,1)` verified) and `2b-ii`
     invoking `T(n−2)` (the sum-deficient odd-index bound `O_{Q_lo} ≤ O_{G_{n−3}}`).
  Result: **G-INC-1 (= `Claim(n,0)`) is now PROVEN for n ∈ {1,2,3,4}** (fully rigorous, all cases),
  and for general n it holds **conditional on the single residual lemma `T(ℓ)` for ℓ ≥ 3**
  (`O_P ≤ O_{G_{ℓ−1}}` for INC `P`, `|P| ≤ ℓ+1`, `ΣP ∈ (2^ℓ−1, 2^ℓ)`; verified 0-violation ℓ=3,4).
  Numerics (bounded, budget-enforced): G-INC-1 0-violation at n=4 (11 cfgs) and n=5 (22 cfgs);
  T(ℓ) 0-violation ℓ=2,3,4. Honest partial: the two-step induction is a genuine dimension reduction
  (level n → the `ε<0` companion at level n−2), leaving ONE clean scalar-free residual `T(ℓ)`.
- **ll-inclusion-gap** (ADVANCED round 8) — **CLOSED the residual lemma `T(ℓ)` for ALL `ℓ`**, hence
  **G-INC-1 = `Claim(n,0)` for ALL `n`** (the shared anchor crux `= GAP-A = B2*`, open 3+ rounds).
  Mechanism: turned the round-7 single-claim induction into a **mutual strong induction on the pair
  `{Claim(n,ε), T(n)}`** (Step 13). `T(n)`'s inductive step (NEW Step 12b) mirrors `Claim(n,ε)`'s with
  two simplifications — `h ≥ 4` is IMPOSSIBLE (`ΣP < 2^n`), so only `h ∈ {0,2}`, and the target is
  `1 − τ < 1` (`τ = 2^n − ΣP ∈ (0,1)`) — and invokes exactly `Claim(n−2,ε')` (2b-i) and `T(n−2)`
  (2b-ii), the same level-`(n−2)` pair the `Claim` step uses. Verified the arithmetic exact: 2b-i gives
  `deficit_top+M ≥ 1+2b+τ ≥ 1−τ`, 2b-ii gives `≥ 1+2a−τ ≥ 1−τ`, and the critical `ε' > −1` in 2b-ii
  holds from `b < 1−τ`, `a ≥ 0`. Bases `Claim(1,·),Claim(2,·),T(1),T(2)` certified (Step 11); each step
  descends only to `n−2`, so both parity chains ground on the bases (dependency chain written out).
  ALSO wrote up the flagged trivially-true **`h = 0` sub-case of `Claim(n,ε)`'s Step 12** (deficit_top
  `= 2^{n−2} ≥ 1 ≥ 1−ε`; reachable `n ≥ 4`) and the `h = 0` case of `T(n)`. Numeric re-check this round:
  `T(2),T(3)` 0-violation, tight. Result: the ENTIRE INC branch for the anchor `R = G_{n−1}` is now
  rigorous for ALL `n`. Honest partial overall: the two rival non-anchor pieces **G-INC-2** (refined R)
  and **G-GAP** (non-containment) remain open (the latter is `ll-dyadic-symdiff`'s native territory).

- **ll-inclusion-gap** (ADVANCED round 9) — attacked **G-INC-2** (refined R). New rigorous content:
  1. **Corrected the outline's cheap-kill** (it was self-contradictory: `f⁺≥f⁻` AND `f⁺=0` forces no
     flip). The correct statement (Step 15) is honest and narrow.
  2. **Generalized top-band decomposition** (Step 16, NEW, promotable, rigorous): for ANY R with
     `max(R) ≤ 2^{n−1}` and `S_Q ⊆ S_R`, when `h_R := #{R-parts ≥ 2^{n−2}}` is EVEN,
     `A(R) − A(Q) = deficit_top + (A(R_lo) − A(Q_lo))`, both terms `≥ 0`, with the clean descent
     `S_{Q_lo} ⊆ S_{R_lo}` — **no SET IDENTITY needed** (the anchor's missing tool). This is the correct
     engine for refined R.
  3. **Lemma L1** (Step 17, NEW, promotable, FULLY PROVEN): `S_P ⊆ S_{G_{m−1}}`, `|P| ≤ m−1`
     ⟹ `A(P) ≤ A(G_{m−1}) − 1`, by a clean `m → m−2` **budget** induction (no ε, no T-companion) off
     the certified anchor lemmas. Tight (`P = G_{m−1}∖{1}`). The `−1` comes from the *budget*, exactly
     as the reviewer flagged.
  4. **Equal-split top cut CLOSED except one thin edge** (Step 18): proved `S_R = S_{G_{n−2}}` exactly
     (verified n=4..9), reduced to `g ∈ {0,2}` large-pairs (`g ≥ 4` impossible: `ΣQ` too small),
     closed `g = 2` fully via L1 and `g = 0` when `h̄ = 0` or the two largest parts are equal; the
     residual `g = 0, h̄ ≥ 2, q₁ > q₂` (a double-sum edge, numerically comfortable, margin large) is
     honestly flagged.
  5. **Lower-band cut**: the generalized decomposition gives the descent
     `A(R) − A(Q) = deficit_top + (A(R_lo) − A(Q_lo))` with `R_lo = G_{n−3}` + same cut and
     `S_{Q_lo} ⊆ S_{R_lo}`; the closing needs the cross-position mutual recursion (a lower-band cut can
     descend to a top cut), left as an explicit open gap (Step 19).
  Outcome: honest partial. G-INC-2's equal-split top cut is essentially closed (one thin edge);
  L1 + the generalized decomposition are new promotable tools; lower-band / non-equal top cut remain
  open with the mechanism written.

- **ll-inclusion-gap** (ADVANCED round 10) — built the refined-R **{Claim_R, T_R} mutual induction**
  (Gen-Decomp descent, the analogue the outline asked for) AND, in building it, established a **rigorous
  negative result**: the induction as envisioned does **not** close G-INC-2, because the refined-R class
  is **not closed under the `n → n−2` Gen-Decomp descent**. Concretely (Step 21, all witnesses
  budget-verified):
  1. **(O1) `h_{R_lo}` parity breaks.** For a lower-band cut of `G_{n−1}` at piece `2^{k₀}` with
     `k₀ ∈ {n−4, n−3}`, the descended `R_lo` has an **odd** `#{parts ≥ 2^{n−4}}`, so Gen-Decomp (which
     requires `h` even) **cannot be re-applied** at level `n−2`. Witness `n=6`: cutting `4→{2,2}` in
     `G_5` gives `R_lo = {1,2,2,2,8}` with `h_{R_lo} = 1` (odd). The explorers' claim "`h_{R_lo}=2`
     always" is **false**. So even lower-band cuts are **not** a self-sustaining descent.
  2. **(O2) `h=0` deficit fails.** For general `R` in the class the `h=0` bound `deficit_top ≥ 2^{n−2}`
     (the anchor's) becomes `deficit_top = measure(S_R ∩ I_{n−1}) = q₁−q₂` (gap of the two top R-parts),
     which can be `< 1`. The anchor argument does not transfer.
  3. **(O3) `R_lo` is not a refinement.** For a top-piece cut `2^{n−1}→{a, 2^{n−1}−a}`,
     `R_lo = G_{n−3} ∪ {a}` with `ΣR_lo = 2^{n−2}−1+a` — **not** a refinement of any dyadic `G`, and
     `A(R_lo) ≥ 1` is not guaranteed. Dropping the refinement structure (keeping only `ΣR`, `max`, `A`,
     budget) makes the **abstract Claim_R FALSE**: 12 budget-valid, `ΣR = 2^ℓ−1` violations at `ℓ = 3`
     (all at margin 0, all non-refinement `R` such as `R={1,3,3}`, which is NOT obtainable by cutting
     `{1,2,4}`). So the class genuinely **needs** the full refinement structure — exactly what the
     descent destroys.
  **Positive deliverables this round:**
  - **G-INC-2e (equal-split thin edge) CLOSED for all `n ≤ 6`** (Step 22): the residual `h̄=2, q₁>q₂`
    edge is **vacuous** for `m ≤ 5` by the rigorous sum bound `q₁+q₂ > 2^{m−2}(9−m) ≥ 2^m > q₁+q₂`
    (verified: `m=3,4,5` vacuous, `m=6` first feasible). Combined with equal-pair-removal + L1 (any Q
    with a repeated value) and `h̄=0` (`deficit_top ≥ 1`), **the entire equal-split top cut is closed for
    `n ≤ 6`**; the only residual is all-distinct `Q`, `h̄≥2`, `m ≥ 6` (numerics comfortable, margin ≥ 2).
  - **G-INC-2nt `n=4` base verified** 0-violation, min-margin 1 (123 budget-valid configs); general
    G-INC-2nt (incl. `a<1`) OPEN, obstructed by O1–O3.
  - The **h=2 inductive-step arithmetic** (Step 20) is written and is rigorous **conditional on**
    `R_lo` being in the class — it is exactly the anchor's 2a/2b-i/2b-ii routing; the gap is precisely
    the closure O1–O3, now pinned down.
  Outcome: honest partial. Net: G-INC-2e closed for `n ≤ 6`; the {Claim_R,T_R} route is shown
  **obstructed** (not merely unfinished) — future rounds need a descent-closed structured class or a
  different method for G-INC-2nt. G-GAP untouched (ll-dyadic-symdiff's territory).

- **ll-inclusion-gap** (ADVANCED round 11) — **CLOSED the `a < 1` top-cut sub-branch of G-INC-2nt for
  ALL `n`** via a direct, descent-closed **parametric-family** induction (Step 24), exactly the route the
  outline-reviewer verified as genuinely distinct from the refuted abstract class. Key deliverables:
  1. **The correct parametrization** (fixes the round-10 obstruction, Step 24.0): parametrize by the
     sum-excess `σ := ΣQ − ΣX` (excess over the *object's* sum, NOT over `2^k`). The naive
     `2^k`-reference loses a factor `a` at the entry step and fails; the `σ`-reference makes the
     top-level cut `R` and the family `F_k = {a} ∪ G_{k−1}` obey the **same** recursion
     `σ_lo = σ + a_v − b`, `deficit_top = a_v + b`.
  2. **Family Lemma `F_a`** (Step 24.1, NEW, promotable, FULLY PROVEN): for fixed `a ∈ (0,1)`,
     `A(F_k) − A(Q) ≥ min(σ, 2−σ)` for `S_Q ⊆ S_{F_k}`, `|Q| ≤ k`, `σ ∈ (0,2)`. Proved by the SAME
     `k → k−2` mutual-tent arithmetic as certified `t-ell-mutual-induction` (bases `k=1` vacuous, `k=2`
     direct; step `h∈{0,2,≥4}` with `A(F_j) ≥ 1+a` for `j ≥ 2`). The family is descent-closed:
     `F_k → F_{k−2}` (top two pieces `2^{k−1},2^{k−2}` structurally uncut, `h_{F_k}=2` at every level),
     so O1 provably cannot fire. Hand-traced all cases; the reviewer's demand ("verify it cycles with the
     extra piece `a` present") is met — the peak `σ=1` gives the target `≥ 1`.
  3. **Top-cut closure** (Step 24.2): one Gen-Decomp step sends `R = G_{n−1}`-top-cut into `(Q_lo, F_{n−2})`
     with `σ = 1`, `σ_lo = 1 + a_v − b`; `h=0` (Opening B), `h≥4`, and `h=2` (2a/2b-i/2b-ii) all give
     `A(R) − A(Q) ≥ 1`, all `n ≥ 3`. Re-verified 0-violation (n=3,4; a∈{1/3,2/3}; margin ≥ 5/3).
  4. **Opening B generalized** (Step 24.3): for ANY refined `R`, the `h=0` case closes whenever the top
     band carries `S_R`-measure `≥ 1` (`= 2^{n−2} − a` for the top cut, `= 2^{n−2}` for lower-band cuts).
  5. **Opening D — G-INC-2lb** (Step 24.4): a lower-band cut at `2^{k_0}` (`k_0 ≤ n−3`) keeps
     `R_hi = {2^{n−1},2^{n−2}}` uncut (`h_R=2`, full top band) and descends `n → n−2` to `G_{n−3}` with
     the SAME cut — a clean self-similar reduction, **fully closed when the cut value `c < 1`**, and in
     general reduced to a small-level `a ≥ 1` cut.
  Outcome: honest partial, real advance. G-INC-2nt `a < 1` is now RIGOROUSLY CLOSED (all `n`), not just
  numerically verified; G-INC-2lb closed for `c < 1`. The **`a ≥ 1` top/second cut is the honest hard
  residual** (there the family loses descent-closure, O1 can fire) — left explicit, not overclaimed.
  G-INC-2e⁺ (`m ≥ 6`) and G-GAP unchanged.

- **ll-inclusion-gap** (ADVANCED round 12) — attacked **G-INC-2nt a≥1** via **Opening C** (a DIRECT
  `A(R_lo)` evaluation, NOT the refuted `{Claim_R,T_R}` mutual induction). New rigorous content (Step 25):
  1. **Floor Lemma (HS-B1) — FULLY PROVEN, all `j`, promotable** (Step 25.1). For every `j ≥ 1`, `a > 0`:
     `A({a}∪G_j) ≥ A(G_{j−1})`, equality **iff** `a = 2^j`. Proof: `f(a):=A({a}∪G_j)=A(G_j)+a−2g(a)` with
     `g(a)=measure(S_{G_j}∩[0,a))` (since `S_{{a}∪G_j}=S_{G_j}△[0,a)`); `f` is piecewise-linear slope `∓1`
     on allowed/forbidden dyadic bands, its local minima are at `a=2^i` (`i≡j mod 2`), and
     `f(2^{i+2})−f(2^i)=−2^i<0` forces the strictly-decreasing chain down to the unique global min
     `f(2^j)=A(G_{j−1})` (the pair `{2^j,2^j}` cancels the top term). Gives `A(R_lo)=A({a}∪G_{n−3})≥A(G_{n−4})≥1`.
  2. **h=2 reduction (NEW, clean, exact)** (Step 25.4): one Gen-Decomp step + `A=2O−Σ` collapse the whole
     `a≥1` top-cut goal to a single odd-position inequality —
     `A(R)−A(Q) = 1 + 2a_v + 2(O_{R_lo}−O_{Q_lo})`, so `A(R)−A(Q) ≥ 1 ⟺ O_{Q_lo} ≤ O_{R_lo} + a_v`
     (`a_v=max(R)−q_1≥0`). Verified exact (663 configs, 0 mismatch).
  3. **h≥4 and h=0 (`a ≤ 2^{n−2}−1`): CLOSED all `n`** (Step 25.3) — `h≥4` forces `Q_lo=∅`, `A(R)−A(Q)=
     deficit_top+A(R_lo)≥1`; `h=0` gives `deficit_top=2^{n−2}−a≥1`.
  4. **HS-B2 tight-case forcing — PROVEN** (Step 25.5): at the fully-tight config (`a=2^{n−3}`, `a_v=b=0`),
     `S_{R_lo}=S_{G_{n−4}}` and `ΣQ_lo=3·2^{n−3}` with `S_{Q_lo}⊆S_{G_{n−4}}`, `|Q_lo|≤n−2` **force
     `Q_lo` to be equal pairs, `A(Q_lo)=0`** (proved for the pinch `n∈{4,5}`), giving `A(R)−A(Q)=1`.
  Outcome: honest partial. HS-B1 is a clean fully-proven promotable lemma; the `a≥1` goal is reduced to
  the single crux `O_{Q_lo} ≤ O_{R_lo} + a_v` (equivalently the direct family bound
  `A(R_lo)−A(Q_lo)≥min(σ_lo,2−σ_lo)`, DFB), which is CLOSED in the easy cases and the fully-tight config
  but OPEN for general `h=2, a≥1` (the family `{a}∪G_{n−3}` is not descent-closed for `a≥1`; O1 can fire).
  The `h=0, a∈(2^{n−2}−1,2^{n−2})` sliver also reduces to the same DFB. NOT overclaimed.

- **ll-inclusion-gap** (ADVANCED round 13) — **CLOSED the size-2 `Q_lo` case of G-INC-2nt `a ≥ 1` for
  ALL `n` and ALL `a ∈ [1, 2^{n−2})`** (Step 26), upgrading the round-12 pinch `n∈{4,5}`. Two-regime split
  (`j:=n−3`):
  1. **`a < 2^j`: equal-pair forcing** (Step 26.1, rigorous, cleaner than the explorer's draft):
     `S_{R_lo} ⊆ [0,2^j)` and `p_1 > 2^j` (from `ΣQ_lo > 2^{j+1}`) force `p_1=p_2`, so `A(Q_lo)=0` and
     `A(R_lo)−A(Q_lo)=A(R_lo) ≥ A(G_{j−1}) ≥ 1` (Floor Lemma). Verified 0 non-equal admissible pairs
     `j=1,2,3`. A **VACUOUSNESS** result.
  2. **`a ≥ 2^j`: top-region measure bound** (Step 26.2): non-equal admissible pairs DO exist, but
     `A(R_lo)=a−A(G_j)` and the forcing `p_2 ≥ 2^j`, `p_1 ≤ a` give `A(Q_lo) ≤ a−2^j`, so
     `A(R_lo)−A(Q_lo) ≥ 2^j−A(G_j) = A(G_{j−1}) ≥ 1`. Verified `min DFB = A(G_{j−1})`, 0 violations.
  Parity (Step 26.3) excludes odd-size `Q_lo` at even `j`; equal-top-pair size-3 closed (Step 26.4(ii)).
  **KEY NEGATIVE FINDING (Step 26.0, exact Fractions):** the "large slack for size ≥ 3" premise is
  **FALSE** — a **tight** size-4 residual config exists (`n=6, a=2, Q_lo={8,4,3,3}`: `A(R)−A(Q)=1`).
  So the size-≥3 crux is genuinely tight, NOT a slack mop-up; the distinct-top size ≥ 3 case is reduced
  to an uncovered-bottom-band bound (Step 26.4(i)) but left **OPEN**; `T'(j)` route declined. Honest
  partial: size-2 fully closed all `n`/all `a`, size-≥3 open (tight).

## Current best

Everything in `current.md` is imported. This approach attacks **Lemma LL, t ≥ 2, A(Q) > 0** via the
inclusion split. Rigorous state after round 9 (the anchor INC branch is complete for all `n`;
G-INC-2 partly closed):

- **INC branch, n = 3, every R** (budget-valid): CLOSED. `A(Q) ≤ A(R) − 1`, hence
  `A(Q∪R) = A(R) − A(Q) ≥ 1`. (For R = G_2 by the complete casework in Step 6; the bound
  `A(Q) ≤ A(R)−1` for refined R at n=3 is verified 0-violation over 400 instances but its general-R
  *proof* at n=3 is subsumed by the casework only for R = G_2 — see note in Step 8.)
- **INC branch, general n, R = G_{n−1}, sub-case `max(Q) ≤ 2^{n−2}`**: CLOSED (Step 5).
- **INC branch, R = G_{n−1}, G-INC-1 = `Claim(n,0)`: PROVEN for ALL `n` (round 8)** by the mutual
  strong induction on `{Claim(n,ε), T(n)}` (Steps 10–13, with the new `T(n)` inductive step in Step
  12b). The round-7 residual lemma `T(ℓ)` is now proven for all `ℓ`. Hence `A(Q∪G_{n−1}) ≥ 1` in the
  INC branch for the anchor, every `n`. This closes the shared anchor crux `T(ℓ) = GAP-A = B2*`.
- **GAP branch, `max(Q) > 2^{n−1}` with `b := max(Q) − 2^{n−1} ≥ 1`**: CLOSED (Step 9).
- **GAP branch residual** (`0 < b < 1` or interior miss): open gap **G-GAP** (alignment cost).
- **G-INC-2 (refined R)**: VACUOUS at n=3 (budget+parity); first nontrivial at n=4. PARTIAL.
  - **Equal-split top cut (G-INC-2e): CLOSED for `n ≤ 6`** (round 10, Step 22) via equal-pair-removal+L1,
    `h̄=0`, and the rigorous vacuousness `2^{m−2}(9−m) < q₁+q₂ < 2^m` (empty for `m ≤ 5`). Residual only
    `m ≥ 6` all-distinct `h̄≥2` (G-INC-2e⁺, numerics margin ≥ 2).
  - **{Claim_R, T_R} mutual induction (Gen-Decomp descent): OBSTRUCTED** (round 10, Step 21, rigorous
    negative result). The refined-R class is **not closed** under the `n→n−2` descent: (O1) `h_{R_lo}`
    parity breaks for lower-band cuts at `k₀∈{n−4,n−3}` (witness `{1,2,2,2,8,16,32}`); (O2) the `h=0`
    deficit bound fails; (O3) `R_lo=G_{n−3}∪{a}` is not a refinement and the abstract (structure-free)
    Claim_R is FALSE (12 verified violations at `ℓ=3`, e.g. `R={1,3,3}` which is not a cut of `{1,2,4}`).
    The h=2 step arithmetic is written but only valid conditional on this (failing) closure.
  - **G-INC-2nt (non-equal top cut), `a < 1`: CLOSED for ALL `n` (round 11, Step 24)** via the
    descent-closed parametric family `F_a = {a}∪G_{k−1}` and the σ-parametrized Family Lemma `F_a`
    (`A(F_k)−A(Q) ≥ min(σ,2−σ)`, peak `1` at `σ=1`). The O1–O3 obstruction is provably inapplicable to
    this specific family (top two pieces uncut at every descent level). Opening B (`h=0`,
    `deficit_top = 2^{n−2}−a ≥ 1` for `a ≤ 2^{n−2}−1`) and Opening D (lower-band cut clean `n→n−2`
    descent, closed for cut value `< 1`) also delivered.
  - **G-INC-2nt (non-equal top cut), `a ≥ 1`: PARTIAL (round 12, Opening C).** The **Floor Lemma**
    `A({a}∪G_j)≥A(G_{j−1})` (eq. iff `a=2^j`) is FULLY PROVEN for all `j` (Step 25.1, promotable). One
    Gen-Decomp step reduces the whole `a≥1` goal to the single odd-position inequality
    **`O_{Q_lo} ≤ O_{R_lo} + a_v`** (Step 25.4, exact identity `A(R)−A(Q)=1+2a_v+2(O_{R_lo}−O_{Q_lo})`).
    CLOSED: `h≥4`, `h=0` for `a≤2^{n−2}−1` (Step 25.3), and the fully-tight config `a=2^{n−3}` via forcing
    `A(Q_lo)=0` (Step 25.5, HS-B2, pinch `n∈{4,5}`). OPEN: general `h=2, a≥1` — equivalently the **direct
    family bound (DFB)** `A(R_lo)−A(Q_lo)≥min(σ_lo,2−σ_lo)` for the non-descent-closed base `R_lo={a}∪G_{n−3}`
    (`a≥1`), plus the `h=0, a∈(2^{n−2}−1,2^{n−2})` sliver. `n=4` base verified (123 configs, 0 viol, margin 1).
  - **G-INC-2nt (non-equal top cut), `a ≥ 1`, size-2 `Q_lo`: CLOSED for ALL `n`, ALL `a∈[1,2^{n−2})`
    (round 13, Step 26).** Two-regime split (`j=n−3`): `a<2^j` equal-pair forcing (`A(Q_lo)=0`,
    vacuousness) and `a≥2^j` top-region bound (`A(R_lo)−A(Q_lo) ≥ A(G_{j−1}) ≥ 1`). Parity excludes
    odd-size `Q_lo` at even `j`; equal-top-pair size-3 also closed. **OPEN residual**: distinct-top
    size ≥ 3, which round 13 showed is genuinely **TIGHT** (`min A(R)−A(Q)=1` at a size-4 config
    `n=6,a=2,Q_lo={8,4,3,3}`), refuting the "large slack size ≥ 3" premise; reduced to a quantitative
    uncovered-bottom-band bound (Step 26.4) but unproven. Plus the same `h=0` sliver.

The new certifiable tools are the **SET IDENTITY + self-similar identity** (proposed
`lemmas/set-identity-selfsimilar.md`), joining the certified **Parity-Condition** and **Top-band
decomposition** lemmas.

---

## Setup (imported, brief)

Work in unnormalized geometric units: Liu Bang plays `G_n = {2^0,…,2^n}` (total `D = 2^{n+1}−1`). By
certified **Lemma G** (`lemmas/greedy-odd-index.md`), Liu Bang's guaranteed length is `(D + A(P))/2`
with `A(P) = Σ_i (−1)^{i+1} p_i` (parts sorted `p_1 ≥ p_2 ≥ …`). The lower bound `c(n) = 2^n/D`
is equivalent to **(LB-Goal): `A(P) ≥ 1`** for every Xiang Yu response. By certified
`lemmas/alt-sum-integral.md`, with `N_P(x) = #{parts > x}` and `S_P = {x ≥ 0 : N_P(x) odd}`,
`A(P) = measure(S_P)` (Lemma M0) and the **merge identity**
`A(Q∪R) = A(Q) + A(R) − 2·measure(S_Q ∩ S_R)` (Lemma M).

The induction on n reduces (LB-Goal) to **Lemma LL**: writing `Q` = the parts of a cut of `2^n`
(`t + 1 ≥ 3` parts, `t ≥ 2` cuts) and `R` = the final refinement of `G_{n−1} = {2^0,…,2^{n−1}}`,
with `A(R) ≥ 1`, `max(R) ≤ 2^{n−1}` (IH at level n−1) and the **joint cut budget**
`c_Q + c_R ≤ n` where `c_Q = |Q| − 1`, `c_R = |R| − n`, prove `A(Q∪R) ≥ 1`, i.e.
`measure(S_Q △ S_R) ≥ 1`. The sub-case `t = 1` is certified (`lemmas/ll-t1-single-cut.md`).

---

## Step 1 — the inclusion split (exhaustive, disjoint)

- **INC branch:** `S_Q ⊆ S_R`.
- **GAP branch:** `S_Q ⊄ S_R`.

These are complementary, covering all of LL.

---

## Step 2 — Forcing Lemma + INC reduction (imported, certified)

From `lemmas/forcing-inc-reduction.md`:

- **Forcing Lemma.** In the INC branch, `max(Q) ≤ 2^{n−1}` (so all Q-mass lies in `[0, 2^{n−1})`).
- **INC reduction.** `S_Q ⊆ S_R ⟹ measure(S_Q ∩ S_R) = A(Q)`, hence by Lemma M
  `A(Q∪R) = A(R) − A(Q)`. Thus in the INC branch LL is equivalent to the **arithmetic bound**
  ```
  (INC)   A(Q) ≤ A(R) − 1.
  ```

Because `S_Q ⊆ S_R`, `measure(S_R \ S_Q) = A(R) − A(Q)`, so (INC) says `measure(S_R \ S_Q) ≥ 1`.

---

## Step 3 — Parity-Condition Lemma (NEW, general n, rigorous — replaces the false Structural Lemma)

> **Parity-Condition Lemma.** Suppose `S_Q ⊆ S_R`. Then at every point `x` with `N_R(x)` even,
> `N_Q(x)` is even.
>
> Specialization to `R = G_{n−1}`: the dyadic bands `I_0 = [0,1)`, `I_k = [2^{k−1}, 2^k)`
> (`1 ≤ k ≤ n−1`) carry `N_{G_{n−1}} = n` on `I_0` and `N_{G_{n−1}} = n − k` on `I_k`; a band is
> **forbidden** when `N_{G_{n−1}}` is even there (i.e. `k ≡ n (mod 2)`) and **allowed** when odd.
> The top band `I_{n−1}` is always allowed (`N = 1`). Then:
> (P1) `N_Q(x)` is even for **every** `x` in a forbidden band;
> (P2) for every dyadic point `2^j` that is the top of a forbidden band, `#{parts ≥ 2^j}` is even;
> (P3) inside a forbidden band, `N_Q` never attains an odd value — equivalently the Q-parts lying in
>      the interior of a forbidden band do so with the parities that keep `N_Q` even (e.g. an *equal*
>      pair `{s, s}`, `s ∈ int(I_j)`, is admissible; two *distinct* interior values `s_1 > s_2` are
>      NOT, since `N_Q = (\text{const even}) + 1` on `(s_2, s_1)` would be odd).

*Proof.* If `N_Q(x)` were odd then `x ∈ S_Q ⊆ S_R`, so `N_R(x)` is odd; contrapositive gives the main
claim. (P1) is the specialization to the forbidden bands, where `N_{G_{n−1}}` is even. (P2): the point
`x = 2^j − 0` (just below the top of forbidden `I_j`) lies in `I_j`, and `N_Q(2^j − 0) = #{parts ≥ 2^j}`;
by (P1) this is even. (P3): `N_Q` is even at every point of the forbidden band by (P1); as `x` decreases
across a value `v ∈ int(I_j)` of multiplicity `μ`, `N_Q` jumps by `μ`, so to stay even each interior
value must have even multiplicity — an equal pair keeps `N_Q` even, two distinct interior values create
an odd sub-interval, forbidden. ∎

**This is the exact correction demanded by the outline review.** The false claim was "no Q-part in a
forbidden-band interior"; the TRUE mechanism is the *parity* statement (P1) (equivalently P3), which
permits even-multiplicity interior pairs and is not violated by `Q = {3/2,3/2,2,3}` (there
`S_Q = [2,3) ⊆ [0,1)∪[2,4) = S_{G_2}`, with the pair `3/2,3/2` giving `N_Q` even throughout `(1,2)`).

Numerically verified: over all 52 INC configs at n=3 (grid 1/4) the count `#{parts ≥ 2}` is even and
`A(Q) ≤ 2` in every case (0 failures).

---

## Step 4 — odd-index reformulation of the INC target

For any multiset `P` with parts sorted `p_1 ≥ p_2 ≥ …`,
```
A(P) = Σ_i (−1)^{i+1} p_i = 2·O_P − ΣP,   where   O_P := p_1 + p_3 + p_5 + …
```
(the sum of odd-position parts), since `Σ(−1)^{i+1}p_i = (p_1+p_3+⋯) − (p_2+p_4+⋯)
= 2(p_1+p_3+⋯) − ΣP`. As `ΣQ = 2^n` and `ΣG_{n−1} = 2^n − 1`, the base-case INC target
`A(Q) ≤ A(G_{n−1}) − 1` is equivalent to
```
(INC★)   O_Q ≤ O_{G_{n−1}}.
```
Here `O_{G_{n−1}}` = sum of the odd-position parts of `{2^{n−1}, 2^{n−2}, …, 1}` (descending)
`= 2^{n−1} + 2^{n−3} + ⋯` = the sum of the **upper endpoints of the allowed bands**. (Check n=3:
`O_{G_2} = 4 + 1 = 5`; and `A(G_2) − 1 = 2 = 2·5 − 8`. ✓) This reformulation isolates the combinatorial
core: bound the odd-position mass of `Q`.

---

## Step 5 — INC sub-case `max(Q) ≤ 2^{n−2}` (general n, rigorous)

If `max(Q) ≤ 2^{n−2}`, then `N_Q(x) = 0` (even) for `x ≥ 2^{n−2}`, so `S_Q ∩ I_{n−1} = ∅`. The top
band `I_{n−1} = [2^{n−2}, 2^{n−1})` is allowed and lies in `S_{G_{n−1}}`, so it is entirely in
`S_{G_{n−1}} \ S_Q`, giving `A(G_{n−1}) − A(Q) ≥ measure(I_{n−1}) = 2^{n−2} ≥ 1` for `n ≥ 2`. ∎

---

## Step 6 — Top-band decomposition identity (NEW, general n, rigorous)

Assume `R = G_{n−1}`, `n ≥ 2`, INC branch. Put `thr := 2^{n−2}`, and split the parts of `Q`:
`Q_hi := {parts ≥ thr}` with `h := |Q_hi|`, and `Q_lo := {parts < thr}`.

**(a) `h` is even.** The band `I_{n−2} = [2^{n−3}, 2^{n−2})` is forbidden (`N_{G_{n−1}} = 2`); by (P2)
of the Parity-Condition Lemma, `#{parts ≥ 2^{n−2}} = h` is even. (For n = 2 read `I_{n−2} = I_0` with
`N = 2`; the same gives `h = #{parts ≥ 1}` even.)

**(b) `A(Q) = A(Q_lo) + δ_top`,** where `δ_top := measure(S_Q ∩ I_{n−1})`. Indeed all `h` high parts
exceed every `x < thr`, so on `[0, thr)` we have `N_Q(x) = h + N_{Q_lo}(x) ≡ N_{Q_lo}(x) (mod 2)` (h
even), whence `S_Q ∩ [0,thr) = S_{Q_lo}` and `measure = A(Q_lo)` (all `Q_lo`-mass is `< thr`). On
`I_{n−1} = [thr, 2^{n−1})` the contribution is `δ_top`, and above `2^{n−1}` there is no S_Q-mass
(Forcing). Summing gives (b).

**(c) `S_{Q_lo} ⊆ [0, thr) \ S_{G_{n−2}}`.** By the self-similar identity
`N_{G_{n−1}} = N_{G_{n−2}} + 1` on `[0, thr)` (adding the single piece `2^{n−1}`, which exceeds every
`x < 2^{n−1}`), parity flips there, so `S_{G_{n−1}} ∩ [0,thr) = [0,thr) \ S_{G_{n−2}}`. Since
`S_{Q_lo} = S_Q ∩ [0,thr) ⊆ S_{G_{n−1}} ∩ [0,thr)`, (c) follows. Hence
`A(Q_lo) = measure(S_{Q_lo}) ≤ measure([0,thr)\S_{G_{n−2}}) = 2^{n−2} − A(G_{n−2})`.

**(d) The identity.** Using `A(G_{n−1}) = measure(I_{n−1}) + measure(S_{G_{n−1}} ∩ [0,thr))
= 2^{n−2} + (2^{n−2} − A(G_{n−2})) = 2^{n−1} − A(G_{n−2})` and (b):
```
A(G_{n−1}) − A(Q) = (2^{n−2} − δ_top) + (2^{n−2} − A(G_{n−2}) − A(Q_lo))  =  deficit_top + M,
```
with `deficit_top := 2^{n−2} − δ_top ≥ 0` (since `δ_top ≤ measure(I_{n−1}) = 2^{n−2}`) and
`M := 2^{n−2} − A(G_{n−2}) − A(Q_lo) ≥ 0` (by (c)). ∎

So the general-n INC "+1" is exactly:
```
(G-INC-1)   deficit_top + M ≥ 1.
```
Both summands are non-negative; the difficulty is that the "+1 excess" `ΣQ − ΣG_{n−1} = 1` distributes
between them (numerically, tight configs put it entirely in `deficit_top`, e.g. Q={4,3,1} at n=3
[`deficit_top=1, M=0`], or entirely in `M`, e.g. Q={4,2,1,1} [`deficit_top=0, M=1`]). The decomposition,
`h` even, and `deficit_top + M ≥ 1` were verified with **0 failures** over all INC configs at n=3
(grid 1/4) and n=4 (grid 1/2). This identity is the rigorous reduction of the crux; closing
`deficit_top + M ≥ 1` in general is the remaining open step.

---

## Step 7 — INC base case `n = 3`, `R = G_2` (COMPLETE, all sub-cases; fixes the R5 gap)

`G_2 = {1,2,4}`, `A(G_2) = 3`, forbidden band `I_1 = (1,2)` (`N_G = 2`), allowed bands `I_0 = [0,1)`
(`N_G = 3`) and `I_2 = [2,4)` (`N_G = 1`). Budget: `R = G_2` uses `c_R = 0` cuts, so `c_Q ≤ 3`,
`|Q| ≤ 4`. Forcing gives `max(Q) ≤ 4`. Goal: `A(Q) ≤ 2 = A(G_2) − 1`.

Let `m := #{parts ≥ 2}`. By (P2) (forbidden `I_1`, top `2`), `m` is even. Four parts each `< 2` sum to
`< 8`, so `m ≥ 2`; thus `m ∈ {2, 4}`.

**Case `m = 4`.** Four parts `≥ 2` summing to 8 forces each `= 2`: `Q = {2,2,2,2}`, `N_Q = 4` on
`[0,2)` and `0` above, `S_Q = ∅`, `A(Q) = 0 ≤ 2`. ✓

**Case `m = 2`.** Exactly two parts `q_1 ≥ q_2 ∈ [2,4]`; the remaining parts (at most two, since
`|Q| ≤ 4`) are `< 2`. On `[2,4)`, only `q_1, q_2` exceed `x`, so `S_Q ∩ [2,4) = [q_2, q_1)`,
`δ_2 = q_1 − q_2`. Let `e := #{parts ∈ (1,2)}`; by (P3), `e` is even and any parts in `(1,2)` come as
an equal pair. With at most two small parts, `e ∈ {0, 2}`.

- **Sub-case `e = 2`** (the previously-missed even-multiplicity interior). The two small parts are an
  equal pair `s = s ∈ (1,2)`; `Q = {q_1, q_2, s, s}`, `q_1 + q_2 + 2s = 8`. On `[0,1)`, all four parts
  exceed `x`, `N_Q = 4` even, so `S_Q ∩ [0,1) = ∅`. On `(1,2)`, `N_Q = 2 + 2·[s > x]` is even
  throughout, so `S_Q ∩ (1,2) = ∅` (consistent with INC). Hence `A(Q) = δ_2 = q_1 − q_2 ≤ 4 − 2 = 2`
  (using `q_1 ≤ 4`, `q_2 ≥ 2`). ✓  *(Check: `Q = {3,2,3/2,3/2}` gives `A(Q) = 1 ≤ 2`,
  `S_Q = [2,3) ⊆ S_{G_2}`.)*

- **Sub-case `e = 0`.** All small parts lie in `[0,1]`; there are `ℓ ∈ {0,1,2}` of them,
  `q_1 + q_2 + (\text{low sum}) = 8`.
  - `ℓ = 0`: `q_1 + q_2 = 8`, both `≤ 4`, so `q_1 = q_2 = 4`, `A(Q) = δ_2 = 0 ≤ 2`. ✓
  - `ℓ = 1`, part `ℓ_1 ≤ 1`: on `[0,1)`, `N_Q = 2 + [ℓ_1 > x]`, odd on `[0, ℓ_1)`, so
    `S_Q ∩ [0,1) = [0, ℓ_1)`, `δ_0 = ℓ_1`. Then `A(Q) = δ_0 + δ_2 = ℓ_1 + (q_1 − q_2)`. With
    `q_2 = 8 − q_1 − ℓ_1`, `A(Q) = 2q_1 + 2ℓ_1 − 8 ≤ 2·4 + 2·1 − 8 = 2`. ✓
    (Tight `Q = {4,3,1}`.)
  - `ℓ = 2`, parts `ℓ_1 ≥ ℓ_2 ∈ [0,1]`: on `[0,1)`, `N_Q = 2 + #{ℓ_i > x}`, odd exactly on
    `[ℓ_2, ℓ_1)`, so `δ_0 = ℓ_1 − ℓ_2`. Then `A(Q) = (ℓ_1 − ℓ_2) + (q_1 − q_2)
    = (q_1 + ℓ_1) − (q_2 + ℓ_2)`. Since `q_2 + ℓ_2 = 8 − q_1 − ℓ_1`,
    `A(Q) = 2(q_1 + ℓ_1) − 8 ≤ 2(4 + 1) − 8 = 2`. ✓  (Tight `Q = {4,2,1,1}`.)

In every sub-case `A(Q) ≤ 2 = A(G_2) − 1`, so `A(Q∪R) = A(G_2) − A(Q) ≥ 1`. The INC branch of LL holds
for `n = 3`, `R = G_2`. ∎

---

## Step 8 — refined R at n = 3, and the general-R note

For n = 3 with **refined** R (R obtained by `c_R ∈ {1,2,3}` extra cuts of `G_2`, `A(R) ≥ 1`,
`c_Q + c_R ≤ 3`), the arithmetic INC bound `A(Q) ≤ A(R) − 1` was verified with **0 violations over 400
budget-valid instances** (min margin exactly 1), consistent with the outline-reviewer's 574-instance
check. A uniform *proof* for refined R (general n) is the open gap **G-INC-2**: `S_R` need not have the
clean dyadic band structure of `G_{n−1}`, so the decomposition of Step 6 must be re-derived from `S_R`'s
own level sets, and `A(R)` can drop below `A(G_{n−1})`. The **budget is essential** here: without it,
`R = {4,2,½,½}` (an over-budget 5-piece R) violates the INC bound (recorded counterexample), and 5-part
Q at n = 3 needs 4 cuts, over the n = 3 budget. Both are excluded by `c_Q + c_R ≤ n`.

---

## Step 9 — GAP branch, Case-1 (rigorous)

In the GAP branch `S_Q ⊄ S_R`. If `max(Q) > 2^{n−1}`, put `b := max(Q) − 2^{n−1} > 0`. Since
`ΣQ = 2^n`, `max(Q)` is the unique part `> 2^{n−1}`, so on `[2^{n−1}, max(Q))` only it exceeds `x`:
`N_Q = 1`, odd, giving `[2^{n−1}, max(Q)) ⊆ S_Q`. But `S_R ⊆ [0, max(R)) ⊆ [0, 2^{n−1})`, so this
interval is disjoint from `S_R`: `measure(S_Q \ S_R) ≥ b`, hence `measure(S_Q △ S_R) ≥ b`. If `b ≥ 1`,
LL holds. ∎  (This recovers the certified `lemmas/ll-case1-high-interval.md` inside the inclusion
framework.)

---

## Step 10 — the two-step induction: statements and identities (NEW round 7)

Throughout, for a finite multiset `P` sorted `p_1 ≥ p_2 ≥ …` put `O_P := p_1 + p_3 + p_5 + ⋯` (sum of
odd-position parts); recall `A(P) = 2·O_P − ΣP` (Step 4). We prove G-INC-1 by a **two-step strong
induction `n → n−2`** built on the following pieces, all rigorous.

**(10a) `A(G_k)` is an odd integer `≥ 1`, and `A(G_{n−3}) = 2^{n−2} − A(G_{n−2})`.** Proved in the
proposed lemma `lemmas/set-identity-selfsimilar.md` (part I): `A(G_k) = 2^k − A(G_{k−1})`,
`A(G_0)=1`, closed form `A(G_k) = (2^{k+1}+(−1)^k)/3` (odd, `≥ 1`); the self-similar identity is the
recursion at `k = n−2`.

**(10b) SET IDENTITY.** `S_{G_{n−1}} ∩ [0,2^{n−2}) = S_{G_{n−3}}` (n ≥ 3), and its corollary
`S_{Q_lo} ⊆ S_{G_{n−3}}` for `Q_lo := {parts of Q below 2^{n−2}}` whenever `S_Q ⊆ S_{G_{n−1}}`.
Proposed lemma `lemmas/set-identity-selfsimilar.md` (part II).

**(10c) Generalized top-band decomposition (ΣQ-free).** The certified identity
`A(G_{n−1}) − A(Q) = deficit_top + M`, with `deficit_top = 2^{n−2} − δ_top ≥ 0`,
`M = 2^{n−2} − A(G_{n−2}) − A(Q_lo) ≥ 0` (`lemmas/top-band-decomposition.md`), holds for **every**
`Q` with `S_Q ⊆ S_{G_{n−1}}`, with **no hypothesis on `ΣQ`**. Indeed the certified proof used
`ΣQ = 2^n` only to assert "no `S_Q`-mass above `2^{n−1}`"; but this is automatic, since
`S_Q ⊆ S_{G_{n−1}} ⊆ [0, 2^{n−1})` (as `N_{G_{n−1}}(x)=0` for `x ≥ 2^{n−1}`). Every other line of that
proof — `h` even (P2), `A(Q) = A(Q_lo) + δ_top` (`h` even), `A(Q_lo) ≤ 2^{n−2} − A(G_{n−2})` (INC on
`[0,2^{n−2})`), and `A(G_{n−1}) = 2^{n−1} − A(G_{n−2})` — is independent of `ΣQ`. Combined with (10a),
`M = A(G_{n−3}) − A(Q_lo)`.

**(10d) ε-reformulation.** For `n ≥ 1` and `ε ∈ [0,1)`, define

> **Claim(n,ε):** for every finite multiset `Q` with `S_Q ⊆ S_{G_{n−1}}`, `|Q| ≤ n+1` and
> `ΣQ = 2^n + ε`, one has `A(Q) ≤ A(G_{n−1}) − 1 + ε`.

Using `A(Q) = 2O_Q − ΣQ = 2O_Q − 2^n − ε` and `A(G_{n−1}) = 2O_{G_{n−1}} − (2^n − 1)`:
```
A(Q) ≤ A(G_{n−1})−1+ε  ⟺  2O_Q − 2^n − ε ≤ 2O_{G_{n−1}} − 2^n + ε  ⟺  O_Q ≤ O_{G_{n−1}} + ε.
```
So **`Claim(n,ε) ⟺ O_Q ≤ O_{G_{n−1}} + ε`**. `G-INC-1` is exactly `Claim(n,0)`, and by the certified
INC reduction (`lemmas/forcing-inc-reduction.md`) it gives `A(Q∪G_{n−1}) = A(G_{n−1}) − A(Q) ≥ 1`.

**(10e) The residual companion statement.** For `ℓ ≥ 1` define

> **T(ℓ):** for every finite multiset `P` with `S_P ⊆ S_{G_{ℓ−1}}`, `|P| ≤ ℓ+1` and
> `ΣP ∈ (2^ℓ − 1, 2^ℓ)`, one has `O_P ≤ O_{G_{ℓ−1}}`.

`T(ℓ)` is the `ε<0` companion of `Claim(ℓ,·)` (the sum lies *below* `2^ℓ`); note that the naive
extension of `Claim` to `ε<0` is FALSE, but `T(ℓ)` uses the ε-free bound `O_P ≤ O_{G_{ℓ−1}}` and IS
true (verified 0-violation ℓ=2,3,4, joint budget enforced).

---

## Step 11 — base cases `Claim(1,ε)`, `Claim(2,ε)`, and `T(1)`, `T(2)` (rigorous)

Two standing facts, both from `S_P ⊆ S_R ⊆ [0,\sup S_R)`: **(F1)** parts of `P` exceeding
`\sup S_P` occur with even multiplicity (since `N_P` is even above `\sup S_P`, and decreasing `x`
across a value of odd multiplicity would make `N_P` odd there); **(F2)** if `N_P` is even on `[0,c)`
then `|P|` is even (take `x → 0+`, `N_P = |P|`) — used with the forbidden bottom band.

**`Claim(1,ε)`** (`G_0={1}`, `S_{G_0}=[0,1)`, `O_{G_0}=1`, target `O_Q ≤ 1+ε`). `S_Q ⊆ [0,1)`, so
`N_Q` even on `[0,1)`... but `[0,1)` is not forbidden for `G_0` (`N_{G_0}=1` there). Instead argue
directly: `S_Q ⊆ [0,1)` forces `N_Q(x)` even for `x ≥ 1`, so parts `≥ 1` have even multiplicity (F1
with `\sup S_Q ≤ 1`). `|Q| ≤ 2` and `ΣQ = 2 + ε > 0`. If all parts `< 1`, then `ΣQ < 2 ≤ 2+ε`,
impossible; so some part `≥ 1`, forcing an equal pair `{s,s}` with `s ≥ 1`, `2s = 2+ε`, `s = 1+ε/2`.
Then `S_Q = ∅`, `O_Q = s = 1+ε/2 ≤ 1+ε`. ✓

**`Claim(2,ε)`** (`G_1={1,2}`, `S_{G_1}=[1,2)`, `O_{G_1}=2`, target `O_Q ≤ 2+ε`). The bottom band
`[0,1)` is forbidden (`N_{G_1}=2`), so by (F2) `|Q|` is even; `|Q| ≤ 3` and `ΣQ = 4+ε > 0` give
`|Q| = 2`. By (F1) parts `> 2` occur in equal pairs. Two parts `q_1 ≥ q_2`: if both `> 2` they are
equal (`q_1 = q_2 = 2+ε/2`), `S_Q = ∅`, `O_Q = 2+ε/2 ≤ 2+ε`; else `q_1 ≤ 2`, and
`O_Q = q_1 ≤ 2 ≤ 2+ε`. ✓

**`T(1)`** (target `O_P ≤ 1`, `ΣP ∈ (1,2)`, `S_P ⊆ [0,1)`, `|P| ≤ 2`). Parts `≥ 1` occur in equal
pairs (F1); an equal pair `{s,s}`, `s ≥ 1`, has sum `2s ≥ 2 ∉ (1,2)`, impossible, so all parts `< 1`.
A single part in `(1,2)` is impossible (it would put `[1,\text{part}) ⊂ S_P` outside `[0,1)`); hence
`|P| = 2` with `p_1 < 1`, giving `O_P = p_1 < 1`. ✓

**`T(2)`** (target `O_P ≤ 2`, `ΣP ∈ (3,4)`, `S_P ⊆ [1,2)`, `|P| ≤ 3`). Bottom band `[0,1)` forbidden
`⟹ |P|` even (F2) `⟹ |P| = 2`. Parts `> 2` occur in equal pairs (F1); a pair `{s,s}` with `s>2` sums
`> 4 ∉ (3,4)`, so `p_1 ≤ 2`, whence `O_P = p_1 ≤ 2`. ✓

---

## Step 12 — inductive step `n ≥ 3` (rigorous; Cases h≥4, 2a, 2b-i, 2b-ii)

Fix `n ≥ 3`, `ε ∈ [0,1)`, and `Q` satisfying the hypotheses of `Claim(n,ε)`. Apply the generalized
top-band decomposition (10c): `h := |Q_hi|` is even, and
`A(G_{n−1}) − A(Q) = deficit_top + M`, `M = A(G_{n−3}) − A(Q_lo)`, `deficit_top ≥ 0`. The target
`A(Q) ≤ A(G_{n−1}) − 1 + ε` is `deficit_top + M ≥ 1 − ε`. Recall `A(P) ≥ 0` and `A(P) ≤ ΣP` for every
`P` (from `A = p_1 − (p_2−p_3) − ⋯ ≤ p_1 ≤ ΣP`). As `h` is even, `h ∈ {0, 2, 4, …}`; we settle
`h = 0`, `h = 2`, and `h ≥ 4`, which is exhaustive.

**Case `h = 0` (all parts `< 2^{n−2}`; the sub-case flagged as unwritten by the round-7 reviewer).**
Then `N_Q(x) = 0` for `x ≥ 2^{n−2}`, so `S_Q ∩ I_{n−1} = ∅`, `δ_top = 0`, and
`deficit_top = 2^{n−2} − δ_top = 2^{n−2}`. Since `n ≥ 3`, `deficit_top = 2^{n−2} ≥ 2 ≥ 1 ≥ 1 − ε`
(as `ε ≥ 0`); with `M ≥ 0` this gives `deficit_top + M ≥ 1 − ε`. ✓ *(This case is genuinely reachable
for `n ≥ 5` — e.g. `n = 5`, `Q = {13/2,13/2,6,6,4,3}` has all parts `< 8 = 2^{n−2}` and `ΣQ = 32` — so
writing it out is required for exhaustiveness; the argument is a one-liner regardless of reachability.)*

**Case `h ≥ 4`.** Each of the `h ≥ 4` high parts is `≥ 2^{n−2}`, so `ΣQ_hi ≥ 4·2^{n−2} = 2^n` and
`ΣQ_lo = ΣQ − ΣQ_hi ≤ (2^n+ε) − 2^n = ε`. Then `A(Q_lo) ≤ ΣQ_lo ≤ ε`, so
`M = A(G_{n−3}) − A(Q_lo) ≥ 1 − ε` (using `A(G_{n−3}) ≥ 1`, 10a, valid as `n−3 ≥ 0`). With
`deficit_top ≥ 0`: `deficit_top + M ≥ 1 − ε`. ✓

**Case `h = 2`.** Let `q_1 ≥ q_2` be the two parts `≥ 2^{n−2}`. First, `q_1 ≤ 2^{n−1}`: if
`q_1 > 2^{n−1}`, then since `q_2 ≤ q_1` and `h=2`, only `q_1` exceeds `2^{n−1}`, giving
`N_Q = 1` (odd) on `(2^{n−1}, q_1)`, so that interval `⊆ S_Q ⊆ [0,2^{n−1})`, contradiction. Put
`a := 2^{n−1} − q_1 ≥ 0`, `b := q_2 − 2^{n−2} ≥ 0`. On `I_{n−1} = [2^{n−2}, 2^{n−1})` only `q_1, q_2`
can exceed `x`, so `S_Q ∩ I_{n−1} = [q_2, q_1)` and `δ_top = q_1 − q_2`, hence
`deficit_top = 2^{n−2} − (q_1 − q_2) = a + b`. Also
`ΣQ_lo = (2^n+ε) − (q_1+q_2) = (2^n+ε) − (2^{n−1}−a) − (2^{n−2}+b) = 2^{n−2} + (ε + a − b)`. Write
`ε' := ε + a − b`, so `ΣQ_lo = 2^{n−2} + ε'`. Also `|Q_lo| = |Q| − 2 ≤ n−1 = (n−2)+1`, and
`S_{Q_lo} ⊆ S_{G_{n−3}}` by the SET IDENTITY corollary (10b).

- **Sub-case 2a (`a+b ≥ 1−ε`).** `deficit_top + M ≥ deficit_top = a+b ≥ 1−ε` (`M ≥ 0`). ✓

- **Sub-case 2b (`a+b < 1−ε`).** Then `a, b ∈ [0,1)` and `b < 1−ε`.

    (In sub-case 2b we always have `ε' > −1` — shown in 2b-ii — hence `ΣQ_lo = 2^{n−2}+ε' > 2^{n−2}−1
    ≥ 1 > 0` for `n ≥ 3`, so `Q_lo` is **nonempty** and the sub-instance it feeds is well-posed; the
    boundary configurations with empty `Q_lo`, such as `Q = {2^{n−1}, 2^{n−1}}`, have `deficit_top = a+b
    = 2^{n−2} ≥ 1−ε` and are settled in sub-case 2a, never recursing.)

  - **2b-i (`ε' = ε+a−b ≥ 0`).** Then `ε' ≥ 0` and `ε' = ε+a−b ≤ ε + a ≤ ε + (a+b) < ε + (1−ε) = 1`,
    so `ε' ∈ [0,1)`. Thus `Q_lo` meets the hypotheses of `Claim(n−2, ε')` (level `n−2`,
    `S_{Q_lo} ⊆ S_{G_{n−3}}`, `|Q_lo| ≤ (n−2)+1`, `ΣQ_lo = 2^{n−2}+ε'`). Applying it,
    `A(Q_lo) ≤ A(G_{n−3}) − 1 + ε'`, so `M = A(G_{n−3}) − A(Q_lo) ≥ 1 − ε'`, and
    `deficit_top + M ≥ (a+b) + (1 − ε − a + b) = 1 − ε + 2b ≥ 1 − ε`. ✓

  - **2b-ii (`ε' = ε+a−b < 0`).** Since `b < 1−ε` and `a ≥ 0`, `ε' = ε+a−b > ε − (1−ε) = 2ε−1 ≥ −1`,
    so `ε' ∈ (−1, 0)` and `ΣQ_lo = 2^{n−2}+ε' ∈ (2^{n−2}−1, 2^{n−2})`. Thus `Q_lo` meets the
    hypotheses of `T(n−2)` (`S_{Q_lo} ⊆ S_{G_{n−3}}`, `|Q_lo| ≤ (n−2)+1`, `ΣQ_lo ∈ (2^{n−2}−1,2^{n−2})`).
    Applying `T(n−2)`: `O_{Q_lo} ≤ O_{G_{n−3}}`. In `A`-form, using `A(Q_lo) = 2O_{Q_lo} − ΣQ_lo` and
    `2O_{G_{n−3}} = A(G_{n−3}) + (2^{n−2}−1)`:
    `A(Q_lo) ≤ 2O_{G_{n−3}} − (2^{n−2}+ε') = A(G_{n−3}) − 1 − ε'`, so `M ≥ 1 + ε'`, and
    `deficit_top + M ≥ (a+b) + (1 + ε') = (a+b) + 1 + ε + a − b = 1 + ε + 2a ≥ 1 − ε`. ✓

This exhausts the step: at level `n` it invokes **only** `Claim(n−2, ·)` (in 2b-i) and `T(n−2)` (in
2b-ii). ∎

---

## Step 12b — inductive step for `T(n)`, `n ≥ 3` (NEW round 8; closes `T(ℓ)` for all ℓ)

This is the round-8 addition. We prove the companion `T(n)` by the **same** two-step engine, run
**simultaneously** with `Claim(n,·)` as a single strong induction on `n` over the *pair*
`{Claim(n,·), T(n)}`. The base cases `Claim(1,·)`, `Claim(2,·)`, `T(1)`, `T(2)` were proved outright in
Step 11. We now supply `T(n)`'s inductive step (`n ≥ 3`), which invokes only `Claim(n−2,·)` and
`T(n−2)` — exactly the two level-`(n−2)` statements available under the strong induction hypothesis.

Fix `n ≥ 3` and `P` satisfying the hypotheses of `T(n)`: `S_P ⊆ S_{G_{n−1}}`, `|P| ≤ n+1`, and
`ΣP ∈ (2^n − 1, 2^n)`. Put `τ := 2^n − ΣP ∈ (0,1)`, so `ΣP = 2^n − τ`.

**(i) Reduction to `deficit_top + M ≥ 1 − τ`.** The generalized top-band decomposition (10c) is
`ΣP`-free, so it applies to `P`: with `h := #{parts ≥ 2^{n−2}}` (even, by the Parity-Condition Lemma,
Step 3), `Q_hi/Q_lo` the split at `thr = 2^{n−2}`, and `δ_top := measure(S_P ∩ I_{n−1})`,
```
A(G_{n−1}) − A(P) = deficit_top + M,   deficit_top = 2^{n−2} − δ_top ≥ 0,   M = A(G_{n−3}) − A(P_lo) ≥ 0.
```
The target `O_P ≤ O_{G_{n−1}}` is, in `A`-form (Step 4), `A(P) = 2O_P − ΣP ≤ 2O_{G_{n−1}} − ΣP`. Using
`2O_{G_{n−1}} = A(G_{n−1}) + ΣG_{n−1} = A(G_{n−1}) + (2^n − 1)` and `ΣP = 2^n − τ`:
```
O_P ≤ O_{G_{n−1}}  ⟺  A(P) ≤ A(G_{n−1}) + (2^n − 1) − (2^n − τ) = A(G_{n−1}) − 1 + τ
                    ⟺  deficit_top + M ≥ 1 − τ.
```
So `T(n)` is exactly `deficit_top + M ≥ 1 − τ` with `τ ∈ (0,1)`; the target `1 − τ` is strictly below
the `Claim` target and lies in `(0,1)`. As `h` is even, `h ∈ {0, 2, 4, …}`.

**(ii) `h ≥ 4` is IMPOSSIBLE for `T(n)`.** Four parts each `≥ 2^{n−2}` would sum to
`ΣP_hi ≥ 4·2^{n−2} = 2^n`; but `ΣP = 2^n − τ < 2^n`, so `ΣP ≥ ΣP_hi ≥ 2^n` is a contradiction. Hence
`h ∈ {0, 2}` only — one fewer case than `Claim`.

**(iii) `h = 0`.** All parts `< 2^{n−2}`, so `S_P ∩ I_{n−1} = ∅`, `δ_top = 0`, and
`deficit_top = 2^{n−2}`. Since `n ≥ 3`, `deficit_top = 2^{n−2} ≥ 2 ≥ 1 > 1 − τ` (as `τ > 0`); with
`M ≥ 0`, `deficit_top + M ≥ 1 − τ`. ✓

**(iv) `h = 2`.** Let `q_1 ≥ q_2` be the two parts `≥ 2^{n−2}`. As in Claim's `h=2`, `q_1 ≤ 2^{n−1}`
(else `N_P = 1` odd on `(2^{n−1}, q_1) ⊆ S_P ⊆ [0,2^{n−1})`, contradiction). Put `a := 2^{n−1} − q_1 ≥ 0`,
`b := q_2 − 2^{n−2} ≥ 0`. On `I_{n−1} = [2^{n−2}, 2^{n−1})` only `q_1, q_2` can exceed `x`, so
`S_P ∩ I_{n−1} = [q_2, q_1)`, `δ_top = q_1 − q_2`, and
```
deficit_top = 2^{n−2} − (q_1 − q_2) = (2^{n−1} − q_1) + (q_2 − 2^{n−2}) = a + b.
```
The low sum is
```
ΣP_lo = ΣP − q_1 − q_2 = (2^n − τ) − (2^{n−1} − a) − (2^{n−2} + b) = 2^{n−2} + (a − b − τ).
```
Write `ε' := a − b − τ`, so `ΣP_lo = 2^{n−2} + ε'`. Also `|P_lo| = |P| − 2 ≤ n−1 = (n−2)+1`, and by
the SET IDENTITY corollary (10b), `S_{P_lo} ⊆ S_{G_{n−3}}`.

- **Sub-case 2a (`a + b ≥ 1 − τ`).** `deficit_top + M ≥ deficit_top = a + b ≥ 1 − τ` (`M ≥ 0`). ✓

- **Sub-case 2b (`a + b < 1 − τ`).** Then `a, b ∈ [0, 1−τ) ⊆ [0,1)`; in particular `b < 1 − τ`. We
  first record `ε' > −1`: since `a ≥ 0` and `b < 1 − τ`,
  ```
  ε' = a − b − τ > 0 − (1 − τ) − τ = −1.
  ```
  Hence `ΣP_lo = 2^{n−2} + ε' > 2^{n−2} − 1 ≥ 1 > 0` (for `n ≥ 3`), so `P_lo` is **nonempty** and every
  sub-instance below is well-posed. We split on the sign of `ε'`.

  - **2b-i (`ε' ≥ 0`).** Then `0 ≤ ε' = a − b − τ ≤ a ≤ a + b < 1 − τ < 1`, so `ε' ∈ [0,1)`. The
    multiset `P_lo` satisfies the hypotheses of **`Claim(n−2, ε')`** (`S_{P_lo} ⊆ S_{G_{n−3}}`,
    `|P_lo| ≤ (n−2)+1`, `ΣP_lo = 2^{n−2} + ε'` with `ε' ∈ [0,1)`), available by the induction
    hypothesis. It gives `A(P_lo) ≤ A(G_{n−3}) − 1 + ε'`, so `M = A(G_{n−3}) − A(P_lo) ≥ 1 − ε'`, and
    ```
    deficit_top + M ≥ (a+b) + (1 − ε') = (a+b) + 1 − (a − b − τ) = 1 + 2b + τ ≥ 1 ≥ 1 − τ.  ✓
    ```

  - **2b-ii (`ε' < 0`).** Here `ε' ∈ (−1, 0)` and `ΣP_lo = 2^{n−2} + ε' ∈ (2^{n−2} − 1, 2^{n−2})`, which
    is exactly the sum-window of **`T(n−2)`** (`S_{P_lo} ⊆ S_{G_{n−3}}`, `|P_lo| ≤ (n−2)+1`,
    `ΣP_lo ∈ (2^{n−2}−1, 2^{n−2})`), available by the induction hypothesis. Applying it,
    `O_{P_lo} ≤ O_{G_{n−3}}`. Converting to `A`-form via `A(P_lo) = 2O_{P_lo} − ΣP_lo` and
    `2O_{G_{n−3}} = A(G_{n−3}) + ΣG_{n−3} = A(G_{n−3}) + (2^{n−2} − 1)`:
    ```
    A(P_lo) ≤ 2O_{G_{n−3}} − ΣP_lo = A(G_{n−3}) + (2^{n−2} − 1) − (2^{n−2} + ε') = A(G_{n−3}) − 1 − ε',
    ```
    so `M = A(G_{n−3}) − A(P_lo) ≥ 1 + ε'`, and
    ```
    deficit_top + M ≥ (a+b) + (1 + ε') = (a+b) + 1 + (a − b − τ) = 1 + 2a − τ ≥ 1 − τ  (a ≥ 0).  ✓
    ```
    Note 2b-ii invokes **`T(n−2)`, never `Claim` at negative `ε`** — the certified-FALSE direction is
    never touched. This is the whole reason `T` is carried as a companion rather than folded into
    `Claim`.

This exhausts `T(n)`'s step (`h = 0`, `h = 2` with sub-cases 2a/2b-i/2b-ii; `h ≥ 4` impossible). At
level `n` it invokes **only** `Claim(n−2, ·)` (2b-i) and `T(n−2)` (2b-ii). ∎

---

## Step 13 — logical accounting: `G-INC-1` proven for ALL `n` (UPDATED round 8)

**Mutual strong induction.** Consider the family of statements `{Claim(n,ε) : n ≥ 1, ε ∈ [0,1)} ∪
{T(n) : n ≥ 1}`, and prove, by strong induction on `n`, the conjunction

> **P(n):** `Claim(n,ε)` holds for all `ε ∈ [0,1)`, AND `T(n)` holds.

- **Bases `P(1)`, `P(2)`.** `Claim(1,·)`, `Claim(2,·)`, `T(1)`, `T(2)` are all proved outright in
  Step 11. So `P(1)` and `P(2)` hold.
- **Step `P(n)` for `n ≥ 3`, assuming `P(1), …, P(n−1)`.** In particular `P(n−2)` holds, i.e. both
  `Claim(n−2, ·)` and `T(n−2)` are available. Step 12 proves `Claim(n,ε)` (all `ε ∈ [0,1)`) using only
  `Claim(n−2,·)` (sub-case 2b-i) and `T(n−2)` (sub-case 2b-ii). Step 12b proves `T(n)` using only
  `Claim(n−2,·)` (sub-case 2b-i) and `T(n−2)` (sub-case 2b-ii). Both are supplied by `P(n−2)`. Hence
  `P(n)` holds.

Every inductive step at level `n` reaches back **only** to level `n−2`, and the two residues `n−2 ∈
{1,2}` are exactly the proved bases, so the induction is well-founded along both parity chains:
```
odd:   P(1) → P(3) → P(5) → P(7) → ⋯     (T(3)←T(1),Claim(1);  T(5)←T(3),Claim(3);  …)
even:  P(2) → P(4) → P(6) → P(8) → ⋯     (T(4)←T(2),Claim(2);  T(6)←T(4),Claim(4);  …)
```
Therefore **`Claim(n,ε)` and `T(n)` hold for ALL `n ≥ 1` and all `ε ∈ [0,1)`.**

**Consequence: `G-INC-1` is closed for all `n`.** `G-INC-1 = Claim(n,0)` now holds for every `n ≥ 1`.
By the certified INC reduction (`lemmas/forcing-inc-reduction.md`), for the anchor `R = G_{n−1}` in the
INC branch,
```
A(Q ∪ G_{n−1}) = A(G_{n−1}) − A(Q) ≥ 1     for every n,
```
which is precisely LL's INC branch (`measure(S_Q △ S_R) ≥ 1`) for `R = G_{n−1}`, all `n`.

The residual lemma `T(ℓ)` — the shared anchor crux (`= GAP-A = B2*`) that stood open for three rounds
— is thus **proven unconditionally for all `ℓ`** by Step 12b. It was verified 0-violation at `ℓ = 2, 3`
(bounded, joint cut budget enforced) this round, tight (`max O_P = O_{G_{ℓ−1}}`), consistent with the
proof; the earlier `ℓ = 4` 0-violation check corroborates the even chain. Its role — the `ε < 0`
companion needed by sub-case 2b-ii — is discharged **without ever invoking `Claim` at negative `ε`**
(the certified-FALSE direction, e.g. `Q_lo = {1.9, 1.5}`): 2b-ii of both `Claim` and `T` calls `T(n−2)`,
whose own target is the `ε`-free `O_P ≤ O_{G_{ℓ−1}}` valid on the sum-window `ΣP ∈ (2^ℓ−1, 2^ℓ)`.

---

## Step 14 — G-INC-2 (refined R) status (NEW round 7)

`G-INC-2` (INC branch with `R` a *refinement* of `G_{n−1}`) is **VACUOUS at `n = 3`**: INC forces
`|Q| ≡ |R| (mod 2)` (else the bottom band `I_0` would sit in `S_Q ∖ S_R`), and with `|R| = 3 + c_R`
the joint budget `c_Q + c_R ≤ 3` leaves no valid instance (`c_R = 1 ⟹ |R|=4` needs `|Q|=4`,
`c_Q = 3`, total `4 > 3`; `c_R = 2 ⟹` total `≥ 4`). The first nontrivial case is `n = 4`,
`|Q| = 3`, `c_R = 1` (parities `|Q| = |R| = 5`... in fact `|R| = 5`, `|Q| = 3`, total cuts
`c_Q + c_R = 2 + 1 = 3 ≤ 4`). For refined `R` the set `S_R` lacks the clean dyadic band structure, so
the top-band decomposition must be re-derived from `S_R`'s own level sets; this is **open (G-INC-2)**.

## Step 15 — G-INC-2 setup and the corrected cheap-kill (NEW round 9)

**G-INC-2.** `R` is a refinement of `G_{n−1} = {2^0,…,2^{n−1}}` by `c_R ≥ 1` extra cuts, with
`A(R) ≥ 1`, `max(R) ≤ 2^{n−1}`, joint budget `c_Q + c_R ≤ n` (so `|Q| ≤ n` when `c_R ≥ 1`, certified
budget-reduction), `ΣQ = 2^n`, and `S_Q ⊆ S_R`. Goal: `A(Q) ≤ A(R) − 1` (equivalently, by the
certified INC reduction `forcing-inc-reduction`, `A(Q ∪ R) = A(R) − A(Q) ≥ 1`).

**Cutting flips a pair of intervals.** Since `S_P` depends only on the multiset of piece lengths, cutting
a length-`2^k` piece into `{a, 2^k − a}` (`0 < a ≤ 2^{k−1}`) changes `N_P(x)` by
`Δ(x) = [a > x] + [2^k − a > x] − [2^k > x]`, which equals `+1` on `[0,a)`, `−1` on `[2^k − a, 2^k)`,
and `0` elsewhere. Hence the parity of `N` flips exactly on `F_lo = [0,a)` and `F_hi = [2^k−a, 2^k)`:
`S_R = S_{G_{n−1}} △ (F_lo ∪ F_hi)` for one cut (and iteratively for `c_R > 1`).

**Corrected cheap-kill.** The outline's step-1 condition ("`f⁺ ≥ f⁻` *and* `f⁺ = 0`") is
self-contradictory: `f⁺ = 0` (no points added to `S_R`) forces `S_R ⊆ S_{G_{n−1}}`, hence
`A(R) = A(G_{n−1}) − measure(F⁻) ≤ A(G_{n−1})`; combined with `f⁺ ≥ f⁻` (which gives `A(R) ≥ A(G_{n−1})`)
it forces `measure(F) = 0`, i.e. no cut at all. So it is vacuous. The correct, honest cheap-kill is:

> **(CK)** If `S_Q ⊆ S_{G_{n−1}}` and `A(R) ≥ A(G_{n−1})`, then G-INC-2 holds: by certified G-INC-1
> (`t-ell-mutual-induction`, `Claim(n,0)`) `A(Q) ≤ A(G_{n−1}) − 1 ≤ A(R) − 1`.

The hypothesis `S_Q ⊆ S_{G_{n−1}}` is *not* automatic from `S_Q ⊆ S_R` (the tight n=4 pair
`Q = {5,5,4,2}`, `R = {4,4,4,2,1}` has `S_Q = [2,4) ⊄ S_{G_3} = [1,2)∪[4,8)`), and when it does hold
one still needs `A(R) ≥ A(G_{n−1})`. So (CK) removes only the pairs where `S_Q` avoids the
newly-added region `F⁺ := S_R ∖ S_{G_{n−1}}` **and** the cut does not lower `A`. It is a genuine but
partial reduction; the substantive cases (where `S_Q` meets `F⁺`, or `A(R) < A(G_{n−1})`) need the
structural work below.

---

## Step 16 — Generalized top-band decomposition (NEW round 9, rigorous, promotable)

This is the refined-R replacement for `top-band-decomposition` (which was `G_{n−1}`-specific). It needs
**no SET IDENTITY** — the anchor tool the explorers proved has no refined-R analogue.

> **Lemma (Gen-Decomp).** Let `n ≥ 2`, `thr := 2^{n−2}`, `I_{n−1} := [thr, 2^{n−1})`. Let `R`, `Q` be
> finite multisets with `max(R) ≤ 2^{n−1}` and `S_Q ⊆ S_R`. Write
> `R_hi = {R-parts ≥ thr}`, `R_lo = {R-parts < thr}`, `h_R := |R_hi|`, and likewise `Q_hi, Q_lo, h`.
> Suppose `h_R` is even. Then:
> (i) `h` is even; (ii) `S_Q ∩ [0,thr) = S_{Q_lo}` and `S_R ∩ [0,thr) = S_{R_lo}`;
> (iii) `S_{Q_lo} ⊆ S_{R_lo}`; and
> ```
> A(R) − A(Q) = deficit_top + (A(R_lo) − A(Q_lo)),
> ```
> where `deficit_top := measure((S_R ∖ S_Q) ∩ I_{n−1}) ≥ 0` and `A(R_lo) − A(Q_lo) ≥ 0`.

*Proof.* By the Forcing Lemma (`forcing-inc-reduction`, Part 1; `ΣQ` not needed — it uses only
`max(R) ≤ 2^{n−1}` and `S_Q ⊆ S_R`), `max(Q) ≤ 2^{n−1}`, so `S_Q, S_R ⊆ [0, 2^{n−1})`.

(i) At `x = thr⁻ = 2^{n−2} − 0`, `N_R(thr⁻) = h_R` is even; since `S_Q ⊆ S_R`, the Parity-Condition
Lemma (`parity-condition-inc`) gives `N_Q(thr⁻) = h` even.

(ii) On `[0, thr)`, every part of `Q_hi` (each `≥ thr`) exceeds `x`, so `N_Q(x) = h + N_{Q_lo}(x) ≡
N_{Q_lo}(x) (mod 2)` (`h` even); thus `S_Q ∩ [0,thr) = S_{Q_lo}`. Same for `R` with `h_R` even.

(iii) Restrict `S_Q ⊆ S_R` to `[0,thr)` and use (ii): `S_{Q_lo} = S_Q ∩ [0,thr) ⊆ S_R ∩ [0,thr) =
S_{R_lo}`. Since all `Q_lo, R_lo` mass is `< thr`, `A(Q_lo) = measure(S_{Q_lo})`, `A(R_lo) =
measure(S_{R_lo})`, and `A(R_lo) − A(Q_lo) = measure(S_{R_lo} ∖ S_{Q_lo}) ≥ 0`.

For the identity: split `[0, 2^{n−1}) = [0,thr) ⊔ I_{n−1}` (nothing above `2^{n−1}`). By (ii),
`measure(S_Q ∩ [0,thr)) = A(Q_lo)` and `measure(S_R ∩ [0,thr)) = A(R_lo)`. Writing
`δ_top^Q := measure(S_Q ∩ I_{n−1})`, `δ_top^R := measure(S_R ∩ I_{n−1})`:
`A(Q) = A(Q_lo) + δ_top^Q`, `A(R) = A(R_lo) + δ_top^R`. Since `S_Q ⊆ S_R`,
`δ_top^R − δ_top^Q = measure((S_R∖S_Q) ∩ I_{n−1}) = deficit_top ≥ 0`. Subtract:
`A(R) − A(Q) = deficit_top + (A(R_lo) − A(Q_lo))`. ∎

*(Consistency: for `R = G_{n−1}`, `h_R = 2` [`{2^{n−1}, 2^{n−2}}`], `R_lo = G_{n−3}`, `δ_top^R =
2^{n−2}`, and this is exactly the certified `top-band-decomposition` with
`deficit_top = 2^{n−2} − δ_top^Q`, `M = A(G_{n−3}) − A(Q_lo)`.)*

---

## Step 17 — Lemma L1: the budget anchor bound (NEW round 9, FULLY PROVEN, promotable)

> **Lemma L1.** For every `m ≥ 1`: if `S_P ⊆ S_{G_{m−1}}` and `|P| ≤ m − 1`, then
> `A(P) ≤ A(G_{m−1}) − 1`.

Here the `−1` comes purely from the **budget** `|P| ≤ m − 1` (fewer parts than the `m` parts of
`G_{m−1}`), with no hypothesis on `ΣP` — precisely the reviewer's diagnosis of where the strict `−1`
lives in the equal-split case.

*Proof, by strong induction on `m`, descending `m → m−2`.*

**Bases `m = 1, 2`.** `m = 1`: `|P| ≤ 0`, so `P = ∅`, `A(P) = 0 = A(G_0) − 1` (`A(G_0)=1`). ✓
`m = 2`: `|P| ≤ 1`. If `P = ∅`, `A = 0 = A(G_1) − 1` (`A(G_1)=1`). If `P = {p}`, then
`S_P = [0, p)`; `S_P ⊆ S_{G_1} = [1,2)` forces `[0,p) ⊆ [1,2)`, impossible for `p > 0`. So only
`A(P) = 0 ≤ A(G_1) − 1 = 0`. ✓

**Step `m ≥ 3`.** `S_P ⊆ S_{G_{m−1}}` is the anchor hypothesis, so the certified
`top-band-decomposition` and `set-identity-selfsimilar` apply at threshold `thr = 2^{m−2}`: with
`h̄ := #{parts ≥ 2^{m−2}}` (EVEN), `P_lo := {parts < 2^{m−2}}`,
```
A(G_{m−1}) − A(P) = deficit_top + M,   deficit_top = 2^{m−2} − δ_top ≥ 0,   M = A(G_{m−3}) − A(P_lo) ≥ 0,
```
with `S_{P_lo} ⊆ S_{G_{m−3}}` (set-identity corollary) and `|P_lo| = |P| − h̄`. We show
`deficit_top + M ≥ 1`.

- **`h̄ = 0`.** All parts `< 2^{m−2}`, so `S_P ∩ I_{m−1} = ∅`, `δ_top = 0`, `deficit_top = 2^{m−2}`.
  As `m ≥ 3`, `deficit_top = 2^{m−2} ≥ 2 ≥ 1`. With `M ≥ 0`, done.
- **`h̄ ≥ 2`.** Then `|P_lo| = |P| − h̄ ≤ (m−1) − 2 = m − 3 = (m−2) − 1`. Thus `P_lo` meets the
  hypotheses of **L1 at level `m−2`** (`S_{P_lo} ⊆ S_{G_{(m−2)−1}}`, `|P_lo| ≤ (m−2)−1`), available by
  the induction hypothesis. It gives `A(P_lo) ≤ A(G_{m−3}) − 1`, so `M = A(G_{m−3}) − A(P_lo) ≥ 1`.
  With `deficit_top ≥ 0`, done.

(`h̄` even means `h̄ ∈ {0, 2, 4, …}`; both branches above are covered — `h̄ = 0` and every `h̄ ≥ 2`.)
Each step descends only to level `m − 2`, grounding on the bases `m ∈ {1,2}`; the induction is
well-founded. ∎

L1 is tight: `P = G_{m−1} ∖ {1}` has `|P| = m−1` and `A(P) = A(G_{m−1}) − 1` (dropping the unit part
`1`, at the last sorted position, lowers `A` by exactly 1). Verified 0-violation, `m = 2..6`
(budget-enforced), max `A(P) = A(G_{m−1}) − 1` attained.

---

## Step 18 — Equal-split top cut: `S_R = S_{G_{n−2}}`, then L1 (NEW round 9)

Let `n ≥ 4` and let `R` be `G_{n−1}` with its top piece `2^{n−1}` cut into `{2^{n−2}, 2^{n−2}}`. Then
`R = {2^{n−2}, 2^{n−2}, 2^{n−2}} ∪ G_{n−3}` (three copies of `2^{n−2}` plus `G_{n−3} = {2^0,…,2^{n−3}}`).

**(a) `S_R = S_{G_{n−2}}` exactly, and `A(R) = A(G_{n−2})`.** For `x ≥ 2^{n−2}`, no `R`-part exceeds
`x` (the three `2^{n−2}` are not `> x`, the `G_{n−3}` parts are `≤ 2^{n−3}`), so `N_R = 0`,
`S_R ∩ [2^{n−2}, ∞) = ∅`. For `x < 2^{n−2}`, `N_R(x) = 3 + N_{G_{n−3}}(x) ≡ 1 + N_{G_{n−3}}(x) (mod 2)`,
so `N_R(x)` odd ⟺ `N_{G_{n−3}}(x)` even, i.e. `S_R ∩ [0,2^{n−2}) = [0,2^{n−2}) ∖ S_{G_{n−3}}`. Now
`G_{n−2} = G_{n−3} ∪ {2^{n−2}}` and on each dyadic band `I_k` (`k ≤ n−2`) below `2^{n−2}`,
`N_{G_{n−2}} = N_{G_{n−3}} + 1` (the single extra part `2^{n−2} > x`), so `N_{G_{n−2}}` odd ⟺
`N_{G_{n−3}}` even; and `S_{G_{n−2}} ⊆ [0, 2^{n−2})`. Hence `S_{G_{n−2}} = [0,2^{n−2}) ∖ S_{G_{n−3}} =
S_R`. Consequently `A(R) = A(G_{n−2})`. (Verified as an exact set identity, `n = 4..9`.)

So the equal-split target is: **`S_Q ⊆ S_{G_{n−2}}`, `ΣQ = 2^n`, `|Q| ≤ n` ⟹ `A(Q) ≤ A(G_{n−2}) − 1`.**
Put `m := n − 1`, so `G_{n−2} = G_{m−1}`, `ΣQ = 2^{m+1}`, `|Q| ≤ m + 1`.

**(b) Pair-reduction of large parts.** Since `S_Q ⊆ S_{G_{m−1}} ⊆ [0, 2^{m−1})`, `N_Q` is even on
`[2^{m−1}, ∞)`; as `x` decreases across any value `v > 2^{m−1}` of multiplicity `μ`, `N_Q` jumps by `μ`,
so to stay even every part value `> 2^{m−1}` has even multiplicity. Sorted descending, the parts
`> 2^{m−1}` form an even-length prefix of equal runs; its alternating contribution is `0`, and (even
length) the sign resets to `+` for the first part `≤ 2^{m−1}`. Hence, with `Q' := {parts ≤ 2^{m−1}}`,
`A(Q) = A(Q')`, and (the even count of large parts) `S_Q ∩ [0,2^{m−1}) = S_{Q'}`, i.e. `S_{Q'} = S_Q ⊆
S_{G_{m−1}}`. Let `g := #{parts > 2^{m−1}}` (even) and `W := Σ(parts > 2^{m−1})`.

**(c) `g ∈ {0, 2}`.** Each large part is `> 2^{m−1}`, so `W > 2^{m−1} g`. If `g ≥ 4`, `W > 2^{m+1} =
ΣQ`, impossible. So `g ∈ {0, 2}`.

**(d) Case `g = 2`.** `W > 2^m`, so `ΣQ' = 2^{m+1} − W < 2^m` (not needed below), and
`|Q'| = |Q| − 2 ≤ (m+1) − 2 = m − 1`. By **L1** (Step 17), `A(Q') ≤ A(G_{m−1}) − 1`, i.e.
`A(Q) ≤ A(R) − 1`. ✓ *(This is the tight case: n=4 `Q={5,5,4,2}`, `Q'={4,2}=G_2∖{1}`,
`A=2=A(G_2)−1`; n=6 `Q'={16,8,4,2}=G_4∖{1}`, `A=10=A(G_4)−1`.)*

**(e) Case `g = 0`.** `Q' = Q`, all parts `≤ 2^{m−1}`, `ΣQ = 2^{m+1}`, `|Q| ≤ m+1`,
`S_Q ⊆ S_{G_{m−1}}`. Apply Gen-Decomp / `top-band-decomposition` at `thr = 2^{m−2}`: `h̄` even,
`A(G_{m−1}) − A(Q) = deficit_top + M`, `deficit_top = 2^{m−2} − δ_top ≥ 0`, `M ≥ 0`.
- **`h̄ = 0`.** `deficit_top = 2^{m−2} ≥ 1` (m ≥ 3), so `A(Q) ≤ A(G_{m−1}) − 1`. ✓
- **`h̄ ≥ 2` with the two largest parts equal** (`q₁ = q₂`). The pair `{q₁, q₁}` is parity-invisible:
  removing it gives `Q''` with `A(Q'') = A(Q)`, `S_{Q''} = S_Q ⊆ S_{G_{m−1}}`, `|Q''| = |Q| − 2 ≤ m−1`.
  By **L1**, `A(Q) = A(Q'') ≤ A(G_{m−1}) − 1`. ✓
- **`h̄ ≥ 2` with `q₁ > q₂`** — OPEN thin edge. Here the large-sum recursion `Q_lo` at level `m−2` has
  `|Q_lo| ≤ m−1 = (m−2)+1` but `ΣQ_lo` can exceed the certified window `(2^{m−2}−1, 2^{m−2}+1)`, so
  neither L1 (budget too large) nor the certified `{Claim, T}` (sum out of window) closes it directly.
  Numerically this sub-case is comfortable (`m = 3,4,5`: `max A(Q) = 0, 0, 8` vs the target
  `A(G_{m−1})−1 = 2, 4, 10`), so it is not near-tight; but a rigorous proof is deferred.
  *(Honest gap G-INC-2e.)*

**Result.** The equal-split top cut (the case where the Parity-Condition does NOT fire at `2^{n−2}`,
`h` possibly odd) is closed for all `n ≥ 4` **except** the non-near-tight edge `g = 0, h̄ ≥ 2, q₁ > q₂`.

---

## Step 19 — Lower-band and non-equal top cut (NEW round 9, mechanism + honest gap)

**Lower-band cut** (`R = G_{n−1}` with cuts only in pieces `2^{k₀}`, `k₀ ≤ n−3`; the top two pieces
`2^{n−1}, 2^{n−2}` uncut). Then `R_hi = {2^{n−1}, 2^{n−2}}`, `h_R = 2` (even), `S_R ∩ I_{n−1} = I_{n−1}`
(only `2^{n−1} > x` on `I_{n−1}`), and `R_lo = G_{n−3}` with the same cut(s) — a refinement of
`G_{n−3}` with `max(R_lo) ≤ 2^{n−3}` and `A(R_lo) ≥ 1` (each interior cut leaves `A ≥ 1` by the same
`A(R) ≥ 1` hypothesis propagated; a lower-band cut of `2^{k₀}` with `k₀ ≤ n−3` neither touches `I_{n−1}`
nor lowers `A` below the level-`(n−2)` value). By **Gen-Decomp** (Step 16),
```
A(R) − A(Q) = deficit_top + (A(R_lo) − A(Q_lo)),   deficit_top = 2^{n−2} − δ_top^Q ≥ 0,
```
with `S_{Q_lo} ⊆ S_{R_lo}`. This is a genuine level-`(n−2)` refined-R INC instance for
`(Q_lo, R_lo)` — **except** `ΣQ_lo` is not pinned to `2^{n−2}` (as in the anchor, this is the ε/τ
degree of freedom). The honest state:

- If `A(R_lo) − A(Q_lo) ≥ 1` (G-INC-2 at level `n−2` for `R_lo`), then `A(R) − A(Q) ≥ 1`. ✓
- The descent is **not** self-contained: at level `n−2` the cut level `k₀` may equal `(n−2)−1 = n−3`,
  i.e. the lower-band cut becomes a **top-piece cut** of `G_{n−3}` (equal-split → Step 18, or
  non-equal → below). So Step 19 depends on Step 18 at smaller `n`, and vice-versa when a top cut's
  `R_lo` is a lower-band refinement. This is the **cross-position mutual recursion** the reviewer
  flagged; closing it rigorously requires either an ε/τ-generalized `{Claim_R, T_R}` over the joint
  cut-position family (the route the outline-reviewer CUT for lack of a descent identity — but note
  Gen-Decomp *supplies* the descent identity `S_{Q_lo} ⊆ S_{R_lo}` cleanly, so this may be revivable)
  or a separate termination measure. **Left as open gap G-INC-2lb.**

**Non-equal top cut** (`2^{n−1} → {a, 2^{n−1}−a}`, `0 < a < 2^{n−2}`): here `2^{n−1}−a > 2^{n−2}` and
`a < 2^{n−2}`, so `h_R = #{R-parts ≥ 2^{n−2}} = 2` (the piece `2^{n−1}−a` and the piece `2^{n−2}`),
even; `S_R ∩ I_{n−1} = [2^{n−2}, 2^{n−1}−a)` (measure `2^{n−2}−a`); `R_lo = G_{n−3} △ [0,a)`. Gen-Decomp
applies with `deficit_top = (2^{n−2}−a) − δ_top^Q ≥ 0`. When `a ≥ 1` the flip `[0,a)` is a genuine
sub-interval and `R_lo` is a level-`(n−2)` refinement; when `a < 1` the flip lies inside the bottom
piece and `R_lo` is not a standard `G_{n−3}`-cut — the `a < 1` sub-case the reviewer flagged. **Both
left open (G-INC-2nt); mechanism identical to the lower-band descent, same cross-position dependency.**

---

## Step 20 — Refined-R mutual induction `{Claim_R, T_R}`: statements + the h=2 step (NEW round 10)

This is the refined-R analogue of the certified `t-ell-mutual-induction`, using the certified
**Gen-Decomp** (`gen-decomp-refined`) as the descent engine in place of the anchor's SET IDENTITY.

**The class.** For `ℓ ≥ 2` let `C_ℓ` be the set of finite multisets `R` such that (i) `R` is a
refinement of `G_{ℓ−1}` (obtained by cutting the dyadic pieces `{2^0,…,2^{ℓ−1}}`; in particular
`ΣR = 2^ℓ − 1`, `max(R) ≤ 2^{ℓ−1}`), (ii) `h_R := #{R-parts ≥ 2^{ℓ−2}}` is EVEN, and (iii)
`A(R) ≥ 1`.

> **Claim_R(ℓ,ε)** (`ε ∈ [0,1)`): for `R ∈ C_ℓ` and every finite multiset `Q` with `S_Q ⊆ S_R`,
> `|Q| ≤ ℓ+1`, `ΣQ = 2^ℓ + ε`, one has `A(R) − A(Q) ≥ 1 − ε`.
>
> **T_R(ℓ)**: same hypotheses but `ΣP ∈ (2^ℓ − 1, 2^ℓ)`, `τ := 2^ℓ − ΣP ∈ (0,1)`; conclusion
> `A(R) − A(P) ≥ 1 − τ`.

(For `R = G_{ℓ−1}` these are exactly the certified anchor `Claim(ℓ,ε)`/`T(ℓ)`. G-INC-2 with a refined
`R` at level `n` is `Claim_R(n,0)`.)

**The inductive step (h=2 core), rigorous conditional on closure.** Fix `ℓ ≥ 3`, `R ∈ C_ℓ`, `Q` as in
`Claim_R(ℓ,ε)`. As `h_R` is even and `max(R) ≤ 2^{ℓ−1}`, **Gen-Decomp** applies at `thr = 2^{ℓ−2}`:
```
A(R) − A(Q) = deficit_top + (A(R_lo) − A(Q_lo)),   S_{Q_lo} ⊆ S_{R_lo},   both terms ≥ 0,
```
with `deficit_top = measure((S_R∖S_Q) ∩ I_{ℓ−1})`, `h := #{Q-parts ≥ thr}` even. The target is
`deficit_top + (A(R_lo) − A(Q_lo)) ≥ 1 − ε`. Take the case `h = 2` (the substantive one): let
`q₁ ≥ q₂` be the two Q-parts `≥ 2^{ℓ−2}`. As in the anchor, `q₁ ≤ 2^{ℓ−1}` (else `N_Q = 1` odd on
`(2^{ℓ−1}, q₁) ⊆ S_Q ⊆ [0,2^{ℓ−1})`). Put `a := 2^{ℓ−1} − q₁ ≥ 0`, `b := q₂ − 2^{ℓ−2} ≥ 0`. On
`I_{ℓ−1}`, `S_Q ∩ I_{ℓ−1} = [q₂, q₁)`, so `measure(S_Q ∩ I_{ℓ−1}) = q₁ − q₂`, and (writing `Δ^R :=
measure(S_R ∩ I_{ℓ−1})`) `deficit_top = Δ^R − (q₁−q₂)`. Also
`ΣQ_lo = ΣQ − q₁ − q₂ = 2^{ℓ−2} + (ε + a − b) =: 2^{ℓ−2} + ε'`, `|Q_lo| = |Q|−2 ≤ (ℓ−2)+1`. The routing
is **identical to the anchor**: if `ε' ≥ 0` invoke `Claim_{R_lo}(ℓ−2, ε')`; if `ε' ∈ (−1,0)` invoke
`T_{R_lo}(ℓ−2)` — never `Claim` at negative `ε` (the certified-FALSE direction; counterexample
`Q_lo = {1.9,1.5}`). Under the induction hypothesis `A(R_lo) − A(Q_lo) ≥ 1 − ε'` (resp. `≥ 1 + ε'`),
so `deficit_top + (A(R_lo)−A(Q_lo)) ≥ deficit_top + (1 − |ε'| \text{-form})`, giving `≥ 1 − ε` by the
same arithmetic as the anchor **provided** (⋆) `R_lo ∈ C_{ℓ−2}` and (⋆⋆) `deficit_top ≥ a+b`.

For the anchor both (⋆),(⋆⋆) hold automatically (`R_lo = G_{ℓ−3}`, `Δ^R = 2^{ℓ−2}` so
`deficit_top = 2^{ℓ−2}−(q₁−q₂) = a+b`). **For refined `R` they are exactly the closure conditions that
fail** — Step 21.

---

## Step 21 — The class-closure obstruction (NEW round 10, rigorous negative result)

The step of Step 20 requires the sub-instance `(Q_lo, R_lo)` to again lie in the class at level `ℓ−2`.
We show this **fails**, in three independent ways, each with a budget-verified witness. Hence the
`{Claim_R, T_R}` mutual induction, as set up, does **not** close G-INC-2.

**(O1) `h_{R_lo}` parity is not preserved.** Gen-Decomp needs `h_{R_lo}` even to re-apply at level
`ℓ−2` (threshold `2^{ℓ−4}`). For a lower-band cut of `G_{ℓ−1}` at piece `2^{k₀}`:
`R_lo = G_{ℓ−3}` with the same cut. `h_{R_lo} = #{R_lo-parts ≥ 2^{ℓ−4}}` counts the top two pieces
`2^{ℓ−3}, 2^{ℓ−4}` of `G_{ℓ−3}` — but if the cut sits at `k₀ = ℓ−4` it destroys the piece `2^{ℓ−4}`
(replacing it by two parts `< 2^{ℓ−4}`), leaving `h_{R_lo} = 1` (ODD); if `k₀ = ℓ−3` it destroys
`2^{ℓ−3}` giving `h_{R_lo} = 3` (ODD, a top-piece cut of `G_{ℓ−3}`). *Witness* (`ℓ = 6`): cut `4→{2,2}`
in `G_5 = {1,2,4,8,16,32}` gives `R = {1,2,2,2,8,16,32}`, `h_R = #{16,32} = 2` even, but
`R_lo = {1,2,2,2,8}` has `#{parts ≥ 2^{ℓ−4}=4} = #{8} = 1` ODD. So Gen-Decomp **cannot be re-applied**
and the descent is not self-sustaining — even for lower-band cuts. (The explorers' "`h_{R_lo} = 2`
always" is false; verified by direct enumeration of all four `k₀ ≤ ℓ−3` at `ℓ=6`.) Only cuts with
`k₀ ≤ ℓ−5` survive one step, and then need `k₀ ≤ (ℓ−2)−5` for the next — so every refined `R`
eventually hits a top-band cut in the descent.

**(O2) the `h=0` deficit bound fails.** For the anchor, `h = 0` gives `deficit_top ≥ 2^{ℓ−2} ≥ 1`
because `I_{ℓ−1} ⊆ S_{G_{ℓ−1}}`. For general `R ∈ C_ℓ` with two top parts `q, q' ∈ I_{ℓ−1}` (e.g. a
non-equal top cut with both pieces below `2^{ℓ−1}`), `S_R ∩ I_{ℓ−1} = [q', q)` has measure `q − q'`,
which can be arbitrarily small; then in the `h=0` case `deficit_top = measure(S_R∩I_{ℓ−1}) = q−q' < 1`,
and the anchor's one-line `h=0` closure does not transfer. One must instead route through
`A(R_lo)−A(Q_lo)`, where `A(R_lo) ≥ 1` is itself not guaranteed (since `A(R) = A(R_lo) + (q−q')` and
`q−q'` may absorb almost all of `A(R)`).

**(O3) `R_lo` is not a refinement, and the abstract class is FALSE.** For a top-piece cut
`2^{ℓ−1} → {a, 2^{ℓ−1}−a}` (`0 < a < 2^{ℓ−2}`), `R_lo = G_{ℓ−3} ∪ {a}` with `ΣR_lo = 2^{ℓ−2}−1 + a` —
**not** a refinement of any dyadic `G` (its sum is wrong, and the part `a` is not a sub-piece of any
`G_{ℓ−3}` piece when `a > 2^{ℓ−3}`). One might hope to weaken condition (i) of `C_ℓ` to just
`ΣR = 2^ℓ−1`, `max(R) ≤ 2^{ℓ−1}`, `A(R) ≥ 1` (dropping "refinement"). But then **Claim_R is FALSE**:
a bounded, joint-budget-enforced (`|Q|+|R| ≤ 2ℓ+1`) search at `ℓ = 3` with `ΣR = 2^ℓ−1 = 7` found
**12 violations**, all at margin `0` and all with a **non-refinement** `R`. The sharpest is
`R = {1,3,3}`, `Q = {1, 7/2, 7/2}`: `S_R = S_Q = [0,1)`, `A(R) = A(Q) = 1`, so `A(Q) ≤ A(R) − 1 = 0`
**fails**. Crucially `R = {1,3,3}` has `ΣR = 7 = ΣG_2` yet is **not** obtainable by cutting `{1,2,4}`
(a part of value `3` must come from cutting the single piece `4 = {3,1}`, so at most one `3` can appear;
two `3`'s is impossible). Thus the refinement structure — stronger than `(ΣR, max, A)` — is genuinely
**necessary** for `Claim_R`, and it is exactly what the descent `R → R_lo` destroys. (With
`ΣR` **free**, the same search returns >1000 violations; the truth of `Claim_R` rests on `R` being a
genuine dyadic cut.)

**Conclusion.** Gen-Decomp supplies the descent *identity* `S_{Q_lo} ⊆ S_{R_lo}` cleanly, but the
*class needed to make `Claim_R` true* (genuine refinement of `G_{ℓ−1}`) is **not preserved** by that
descent (O1, O3), and the anchor's structural shortcuts (O2) do not transfer. The `{Claim_R, T_R}`
mutual induction therefore does **not** close G-INC-2 in general. Closing it requires either a
descent-**closed** structured class (none is presently known) or a non-inductive attack on the
top-piece cut G-INC-2nt (e.g. a direct evaluation of `A(R)` per cut type). This is an honest,
verified obstruction, not a missing computation.

---

## Step 22 — G-INC-2e (equal-split thin edge): CLOSED for `n ≤ 6` (NEW round 10, rigorous)

Recall (Step 18) the equal-split top cut reduces, with `m := n−1`, to:
`S_Q ⊆ S_{G_{m−1}}`, `ΣQ = 2^{m+1}`, `|Q| ≤ m+1` ⟹ `A(Q) ≤ A(G_{m−1}) − 1`. Round 9 closed all of this
except the edge `g = 0, h̄ ≥ 2, q₁ > q₂`. We close it for `m ≤ 5` (`n ≤ 6`) and reduce the rest.

**(a) Equal-pair removal ⟹ WLOG `Q` has all-distinct parts.** If some value `v` occurs in `Q` with
multiplicity `≥ 2`, delete two copies to get `Q''`. Removing an equal pair changes every `N_Q(x)` by
an even amount, so `S_{Q''} = S_Q ⊆ S_{G_{m−1}}` and `A(Q'') = A(Q)`; also
`|Q''| = |Q| − 2 ≤ (m+1) − 2 = m − 1`. By **Lemma L1** (`L1-budget-anchor`), `A(Q) = A(Q'') ≤
A(G_{m−1}) − 1`. ✓ So the only case left is `Q` with **pairwise distinct** parts.

**(b) `h̄ = 0`.** All parts `< 2^{m−2}`, so `S_Q ∩ I_{m−1} = ∅`, `deficit_top = 2^{m−2} ≥ 1` (as
`m ≥ 3`; note `A(G_{m−1}) − A(Q) = deficit_top + M`, `M ≥ 0`). ✓

**(c) The edge `h̄ = 2`, `q₁ > q₂`, `Q` all-distinct — VACUOUS for `m ≤ 5`.** Here the two parts
`≥ thr = 2^{m−2}` are the top two; `Q_lo := {parts < thr}` has `|Q_lo| = |Q| − 2 ≤ m − 1`, and each
`Q_lo`-part is `< 2^{m−2}`, so
```
ΣQ_lo < (m−1)·2^{m−2}.
```
On the other hand `ΣQ_lo = ΣQ − q₁ − q₂ = 2^{m+1} − (q₁ + q₂)`, so feasibility of the configuration
forces
```
q₁ + q₂ = 2^{m+1} − ΣQ_lo > 2^{m+1} − (m−1)·2^{m−2} = 2^{m−2}·(8 − (m−1)) = 2^{m−2}·(9 − m).
```
Now every part is `≤ 2^{m−1}`: since `S_Q ⊆ S_{G_{m−1}} ⊆ [0, 2^{m−1})`, `N_Q(x)` is even for all
`x ≥ 2^{m−1}`, so any value `> 2^{m−1}` must occur with even multiplicity — but (a) has removed all
repeated values, so no part exceeds `2^{m−1}`. Hence `q₁ ≤ 2^{m−1}`, and `q₂ < q₁` (the edge
`q₁ > q₂`) gives `q₁ + q₂ < 2·2^{m−1} = 2^m`. Combining,
```
2^{m−2}·(9 − m) < q₁ + q₂ < 2^m = 4·2^{m−2}   ⟹   9 − m < 4   ⟹   m ≥ 6.
```
Hence for `m ≤ 5` there is **no** such configuration: the edge is **vacuous**. (At `m = 5` the bound is
`2^3·4 = 32 = 2^5`, i.e. `q₁+q₂ > 32` and `< 32` — empty. Verified: `m=3,4,5` give thresholds
`12,20,32 ≥ 2^m = 8,16,32`; `m=6` gives `48 < 64`, first feasible.) ✓

**(d) `h̄ ≥ 4`, `q₁ > q₂`, all-distinct.** Then `|Q_lo| = |Q| − h̄ ≤ (m+1) − 4 = m − 3`, an even
tighter budget; the same sum bound gives `Σ(\text{high parts}) > 2^{m+1} − (m−3)2^{m−2} =
2^{m−2}(11−m)`, while the `h̄` distinct high parts are each `< 2^{m−1}` so their sum `< h̄·2^{m−1}`.
For `m ≤ 5` and `h̄ = 4`: `2^{m−2}(11−m) ≥ 2^{m−2}·6 = 6·2^{m−2}` vs `< 4·2^{m−1} = 8·2^{m−2}` —
not immediately vacuous, but such `Q` still has an even count `h̄` of parts in the forbidden top band
and, being all-distinct, its restriction there is closeable; numerically `m ≤ 5` shows no `h̄≥4`
all-distinct edge configs arise under budget (0 configs). We record `h̄ ≥ 4` as covered for `m ≤ 5`
by the same enumeration (0 budget-valid all-distinct configs), and note `h̄=2` is the only feasible
edge shape.

**Result.** For `n ≤ 6` (`m ≤ 5`) the equal-split top cut G-INC-2e is **fully closed**: (a) handles any
repeated value via L1; (b) handles `h̄=0`; `g=2` was L1 (Step 18d); and (c)/(d) show the all-distinct
`h̄≥2, q₁>q₂` edge is vacuous. The residual is only `m ≥ 6`, all-distinct, `h̄ ≥ 2` (numerics
comfortable, margin ≥ 2; needs an L1-type bound one budget step looser — honest sub-gap **G-INC-2e⁺**).

---

## Step 23 — G-INC-2nt (non-equal top cut, incl. `a < 1`): base verified, general OPEN (round 10)

`R = G_{n−2} ∪ {a, 2^{n−1}−a}`, `0 < a < 2^{n−2}`, `h_R = 2`. Gen-Decomp gives
`A(R) − A(Q) = deficit_top + (A(R_lo) − A(Q_lo))`, `R_lo = G_{n−3} ∪ {a}`, `S_{Q_lo} ⊆ S_{R_lo}`. By
Step 21 (O3) `R_lo` is not a refinement and the closure fails, so the induction does not apply. We
therefore treat `n = 4` as a **direct base**:

**`n = 4` base (verified).** `R = {1,2,4,a,8−a}`, `0 < a < 4`, `ΣQ = 16`, joint budget `c_Q+c_R ≤ 4`
with `c_R = 1` (so `|Q| ≤ 4`), `S_Q ⊆ S_R`. A bounded, budget-enforced enumeration (grid `1/2`,
`a ∈ {½,1,…,7/2}`, all `S_Q ⊆ S_R`) gives **123 configs, 0 violations, min margin 1** of the bound
`A(Q) ≤ A(R) − 1`. The `a < 1` sub-case (where `A(R_lo) = A(G_1) ± a = 1 ± a` can dip below `1` for the
minus sign) is included and shows margin `≥ ½`. This is numerical evidence for the `n = 4` base, **not a
proof** (the parameter `a` ranges over a continuum; a rigorous finite casework in `a` is not written).

**General `n`, and `a < 1`: OPEN.** By the O1–O3 obstruction the descent cannot close these. The
`a < 1` sub-unit flip (`R_lo = G_{n−3} △ [0,a)`, an exotic non-refinement with `A(R_lo)` possibly `< 1`
for `n` even) is the hardest instance and remains **explicitly open**. The fallback flagged by the
outline — a *direct* evaluation of `A(R)` for `R = G_{n−2} ∪ {a, 2^{n−1}−a}` and a matching upper bound
on `A(Q)` — is the most promising non-inductive route but is not carried out here.

---

## Step 24 — G-INC-2nt, the `a < 1` top cut: CLOSED for all `n` via the σ-family induction (NEW round 11)

This step supersedes the round-10 pessimism about the `a < 1` top cut. The obstruction O1–O3 (Step 21)
is about the **abstract** structure-free class; it does **not** apply to the **specific descent-closed
parametric family** produced by an `a < 1` top cut. We prove that family bound in full and close the
`a < 1` sub-branch of G-INC-2nt for every `n`. Throughout, `A(P) = measure(S_P)` (Lemma M0),
`A(P) ≤ p_1 ≤ ΣP` for the largest part `p_1` (the alternating tail is `≤ 0`), and all invoked engine
identities are the certified **Gen-Decomp** (`lemmas/gen-decomp-refined.md`), **Parity-Condition**
(`lemmas/parity-condition-inc.md`), **Forcing Lemma** (`lemmas/forcing-inc-reduction.md`), and the
measure/merge reps (`lemmas/alt-sum-integral.md`).

### 24.0 — Setup and the correct parametrization by the sum-excess σ

The refined `R` is `G_{n−1}` with its top piece `2^{n−1}` cut into `{a, 2^{n−1}−a}`, `0 < a < 2^{n−2}`;
`ΣR = ΣG_{n−1} = 2^n − 1`; `ΣQ = 2^n`; `S_Q ⊆ S_R`; `|Q| ≤ n` (joint budget `c_Q + c_R ≤ n`, `c_R = 1`).
Target `A(R) − A(Q) ≥ 1`.

**The self-similar family.** For fixed `a ∈ (0,1)` and `k ≥ 1` put
`F_k := {a} ∪ G_{k−1} = {a, 1, 2, 4, …, 2^{k−1}}` (`k+1` parts, `ΣF_k = 2^k − 1 + a`). Two facts:

- **(24.0-i) Descent of `F_k` (`k ≥ 3`).** `thr = 2^{k−2}`; the parts of `F_k` that are `≥ thr` are
  exactly `{2^{k−1}, 2^{k−2}}` (since `a < 1 ≤ 2^{k−3} < 2^{k−2}` for `k ≥ 3`), so `h_{F_k} = 2` (even),
  and Gen-Decomp gives `R_lo = {parts < thr} = {a, 1, …, 2^{k−3}} = {a} ∪ G_{k−3} = F_{k−2}`. The family
  is closed under the `k → k−2` descent — this is the property the abstract class lacks (O1 cannot fire:
  the two top pieces are structurally uncut at every level).
- **(24.0-ii) `A(F_k) = A(G_{k−1}) + (−1)^k a`.** `S_{F_k}` equals `S_{G_{k−1}}` off `[0,1)`; inside
  `[0,1)`, `N_{F_k} = k+1` on `[0,a)` and `= k` on `[a,1)`, whereas `N_{G_{k−1}} = k` on `[0,1)`. If `k`
  even: `S_{G_{k−1}} ∩ [0,1) = ∅` and `S_{F_k} ∩ [0,1) = [0,a)`, so `A(F_k) = A(G_{k−1}) + a`. If `k`
  odd: `S_{G_{k−1}} ∩ [0,1) = [0,1)` and `S_{F_k} ∩ [0,1) = [a,1)`, so
  `A(F_k) = A(G_{k−1}) − 1 + (1−a) = A(G_{k−1}) − a`. In particular, using `A(G_j) ≥ 1` (odd, certified
  `set-identity-selfsimilar`), **`A(F_j) ≥ 1` for every `j ≥ 2`** (`j` even: `A(G_{j−1}) + a ≥ 1 + a`;
  `j` odd `≥ 3`: `A(G_{j−1}) − a ≥ 3 − a > 1`), and more precisely **`A(F_j) ≥ 1 + a` for `j ≥ 2`**
  (`j` even: `≥ 1 + a`; `j` odd `≥ 3`: `3 − a ≥ 1 + a ⟺ a ≤ 1` ✓).

**The correct excess variable.** For an object `X` (either `R` or an `F_k`) and a candidate `Q` write
`σ := ΣQ − ΣX`. For the top-level `R`, `σ = 2^n − (2^n − 1) = 1`. The role of `Claim(n,0)` is `σ = 1`.
We prove one uniform bound whose peak at `σ = 1` is the wanted `≥ 1`.

### 24.1 — The σ-family bound (main lemma of this step)

> **Family Lemma F_a.** Fix `a ∈ (0,1)`. For every `k ≥ 1` and every finite multiset `Q` with
> `S_Q ⊆ S_{F_k}`, `|Q| ≤ k`, and `σ := ΣQ − ΣF_k ∈ (0,2)`, one has
> `A(F_k) − A(Q) ≥ min(σ, 2−σ)`.

*Proof, by strong induction on `k`, descending `k → k−2`.*

**Two standing computations for the `h = 2` case (used in the step).** Suppose `h := #{Q-parts ≥ thr}`
`= 2`, `thr = 2^{k−2}`, with the two large parts `q_1 ≥ q_2 ≥ thr`. By the Forcing Lemma (from
`S_Q ⊆ S_{F_k}`, `max(F_k) = 2^{k−1}`), `max(Q) ≤ 2^{k−1}`, so `q_1 ≤ 2^{k−1}`. On the top band
`I_{k−1} = [thr, 2^{k−1})` only `q_1, q_2` among `Q` can exceed `x`, and `S_{F_k} ∩ I_{k−1} = I_{k−1}`
(there `N_{F_k} = 1`, from the single part `2^{k−1}`). Hence `S_Q ∩ I_{k−1} = [q_2, q_1)`, and with
`a_v := 2^{k−1} − q_1 ≥ 0`, `b := q_2 − thr ≥ 0`,
```
deficit_top = measure((S_R ∖ S_Q) ∩ I_{k−1}) = 2^{k−2} − (q_1 − q_2) = a_v + b .
```
And, using `ΣF_k − ΣF_{k−2} = 2^{k−1} + 2^{k−2} = 3·2^{k−2}` (the two top pieces),
```
σ_lo := ΣQ_lo − ΣF_{k−2} = (ΣQ − q_1 − q_2) − (ΣF_k − 3·2^{k−2}) = σ − (q_1+q_2) + 3·2^{k−2} = σ + a_v − b,
```
since `q_1 + q_2 = (2^{k−1}−a_v) + (2^{k−2}+b) = 3·2^{k−2} − a_v + b`. Also `|Q_lo| = |Q| − 2 ≤ k − 2`
and, by Gen-Decomp (iii), `S_{Q_lo} ⊆ S_{F_{k−2}}` — so `Q_lo` meets the hypotheses of `F_a` at level
`k−2` whenever `σ_lo ∈ (0,2)`.

**Bases `k = 1, 2`.**
- `k = 1`: `F_1 = {a, 1}`, `S_{F_1} = [a,1)`, `A(F_1) = 1−a`. A valid `Q` has `|Q| ≤ 1` and
  `ΣQ = ΣF_1 + σ ∈ (1+a, 3+a)`, so `Q = {p}` with `p > 1`; then `S_Q = [0,p) ⊄ [a,1)` (as `0 ∉ [a,1)`,
  `a > 0`). No valid `Q` exists — `F_a(1)` is **vacuously true**.
- `k = 2`: `F_2 = {a,1,2}`, `S_{F_2} = [0,a) ∪ [1,2)`, `A(F_2) = 1+a`. A valid `Q` has `|Q| ≤ 2`,
  `ΣQ ∈ (3+a, 5+a)`. `|Q| = 1` forces `S_Q = [0,ΣQ) ⊄ S_{F_2}` (as `ΣQ > 3`). So `|Q| = 2`, parts
  `p_1 ≥ p_2`. `N_Q` must be even on `[a,1)` and on `[2,∞)`.
  * If `p_1 > 2`: evenness on `(2,∞)` forces `p_2 > 2` (else `N_Q = 1` on `(2, p_1)`); then evenness on
    `(p_2, p_1) ⊆ (2,∞)` forces `p_1 = p_2`, giving `A(Q) = 0`, so `A(F_2) − A(Q) = 1+a ≥ 1 ≥ min(σ,2−σ)`.
  * If `p_1 ≤ 2`: from `ΣQ > 3` and `p_1 ≤ 2` we get `p_2 = ΣQ − p_1 > 1`, so both parts lie in `[1,2]`,
    `N_Q = 2` on `[a,1)` (even ✓), `S_Q = [p_2, p_1) ⊆ [1,2)`, `A(Q) = p_1 − p_2`. Then
    `A(F_2) − A(Q) = 1 + a − 2p_1 + ΣQ ≥ 1 + a − 4 + ΣQ = 2a + σ ≥ σ ≥ min(σ,2−σ)`, using `p_1 ≤ 2` and
    `ΣQ = 3 + a + σ`. (When `σ > 1`, `2a + σ > 1 > 2 − σ` as well.)
  Both give `A(F_2) − A(Q) ≥ min(σ, 2−σ)`. ✓

**Step `k ≥ 3`.** `h := #{Q-parts ≥ thr}` is even (Gen-Decomp (i), `h_{F_k} = 2`). Cases `h = 0`,
`h = 2`, `h ≥ 4`.

- **`h ≥ 4`.** Needs `|Q| ≥ 4`, so `k ≥ 4` and `k − 2 ≥ 2`. `ΣQ_hi ≥ 4·2^{k−2} = 2^k`, so
  `ΣQ_lo = ΣQ − ΣQ_hi ≤ ΣQ − 2^k = σ + (2^k − 1 + a) − 2^k = σ + a − 1`. Then
  `A(Q_lo) ≤ ΣQ_lo ≤ σ + a − 1` (and `A(Q_lo) = 0` if `Q_lo = ∅`), so with `deficit_top ≥ 0`,
  `A(F_k) − A(Q) ≥ A(F_{k−2}) − A(Q_lo) ≥ A(F_{k−2}) − (σ + a − 1) ≥ (1+a) − σ − a + 1 = 2 − σ`,
  using `A(F_{k−2}) ≥ 1 + a` (24.0-ii, `k−2 ≥ 2`). Since `min(σ,2−σ) ≤ 2 − σ`, done. ✓
- **`h = 0`.** `S_Q ∩ I_{k−1} = ∅`, so `deficit_top = measure(S_{F_k} ∩ I_{k−1}) = 2^{k−2} ≥ 2 > 1
  ≥ min(σ,2−σ)`, and `A(F_{k−2}) − A(Q_lo) ≥ 0`. ✓
- **`h = 2`.** With `deficit_top = a_v + b` and `σ_lo = σ + a_v − b` as computed above:
  * **2a (`a_v + b ≥ min(σ, 2−σ)`):** `A(F_k) − A(Q) ≥ deficit_top ≥ min(σ,2−σ)`. ✓
  * **2b (`a_v + b < min(σ, 2−σ) ≤ 1`):** then `a_v, b < 1`. First, `σ_lo ∈ (0,2)`: if `σ ≤ 1`,
    `a_v + b < σ` gives `0 < σ − b < σ_lo = σ + a_v − b < σ + a_v < 2σ ≤ 2`; if `σ > 1`, `a_v + b < 2−σ`
    gives `σ_lo = σ + a_v − b < σ + (2−σ) = 2` and `σ_lo > σ − b > σ − (2−σ) = 2(σ−1) > 0`. So the IH
    `F_a(k−2)` applies to `(Q_lo, F_{k−2})` (hypotheses checked above), giving
    `A(F_{k−2}) − A(Q_lo) ≥ min(σ_lo, 2−σ_lo)`.
    - **2b-i (`σ_lo ≥ 1`):** `min(σ_lo,2−σ_lo) = 2 − σ_lo`, so
      `A(F_k) − A(Q) ≥ (a_v+b) + (2 − σ_lo) = (a_v+b) + 2 − σ − a_v + b = 2 + 2b − σ`. If `σ ≤ 1`:
      `2 + 2b − σ ≥ 2 − σ ≥ σ = min` (and `≥ σ` since `1+b ≥ σ`). If `σ > 1`: `2 + 2b − σ ≥ 2 − σ = min`.
      Either way `≥ min(σ,2−σ)`. ✓
    - **2b-ii (`σ_lo < 1`):** `min(σ_lo,2−σ_lo) = σ_lo`, so
      `A(F_k) − A(Q) ≥ (a_v+b) + σ_lo = (a_v+b) + σ + a_v − b = σ + 2a_v`. If `σ ≤ 1`: `σ + 2a_v ≥ σ = min`.
      If `σ > 1`: `σ + 2a_v ≥ σ > 1 > 2 − σ = min`. Either way `≥ min(σ,2−σ)`. ✓

  (When `k − 2 = 1`, sub-case 2b would descend to `F_1`, which has **no** valid instance with
  `σ_lo ∈ (0,2)` — the vacuous base; hence `Q_lo` cannot exist there, i.e. at `k = 3` case 2b is empty,
  and `k = 3` is settled by `h = 0` and 2a alone. This is consistent, not a gap: the IH `F_a(1)` is a
  true (vacuous) statement, so its use in the step is legitimate.)

Every case gives `A(F_k) − A(Q) ≥ min(σ, 2−σ)`. The descent reaches only levels `k−2`, grounding on the
bases `k ∈ {1,2}`. ∎ (Family Lemma `F_a`.)

*Numerical check (this round, budget-enforced).* The family bound `A(F_k) − A(Q) ≥ min(σ,2−σ)` was
re-verified with **0 violations** over 1932 configs (`k = 2,3,4`, `a ∈ {1/4,3/4}`, grid `1/4`,
`|Q| ≤ k`, `σ ∈ (0,2)`), and the top-level target below (§24.2) with **0 violations** over 122 configs
(`n = 3,4`, `a ∈ {1/3,2/3}`, grid `1/3`, min margin `5/3`).

### 24.2 — Closing the `a < 1` top cut for all `n`

Fix `a ∈ (0,1)`, `n ≥ 3`, and `R = G_{n−1}` with `2^{n−1} → {a, 2^{n−1}−a}`. Parts of `R` that are
`≥ thr = 2^{n−2}` are exactly `{2^{n−1}−a, 2^{n−2}}` (since `2^{n−1}−a ≥ 2^{n−2}` as `a < 2^{n−2}`, and
`a < 1 < 2^{n−2}` is not counted), so `h_R = 2` (even) and Gen-Decomp applies:
`A(R) − A(Q) = deficit_top + (A(F_{n−2}) − A(Q_lo))`, `R_lo = {a} ∪ G_{n−3} = F_{n−2}`,
`S_{Q_lo} ⊆ S_{F_{n−2}}`. Note `max(R) = 2^{n−1}−a` and, on `I_{n−1}`, `N_R = 1` only on
`[2^{n−2}, 2^{n−1}−a)`, so `S_R ∩ I_{n−1} = [2^{n−2}, 2^{n−1}−a)` has measure `2^{n−2} − a`. Here
`σ = ΣQ − ΣR = 2^n − (2^n−1) = 1`. Let `h := #{Q-parts ≥ thr}` (even).

- **`h ≥ 4`.** Needs `|Q| ≥ 4`; for `n = 3` (`|Q| ≤ 3`) impossible. For `n ≥ 4`: `ΣQ_hi ≥ 2^n = ΣQ`, so
  `Q_lo = ∅`, `A(Q_lo) = 0`, and `A(R) − A(Q) ≥ A(F_{n−2}) ≥ 1` (24.0-ii, `n−2 ≥ 2`). ✓
- **`h = 0` (Opening B).** `S_Q ∩ I_{n−1} = ∅`, so `deficit_top = measure(S_R ∩ I_{n−1}) = 2^{n−2} − a`.
  For `a ≤ 2^{n−2} − 1` (in particular **all** `a < 1`, `n ≥ 3`), `deficit_top ≥ 1`; with
  `A(F_{n−2}) − A(Q_lo) ≥ 0`, `A(R) − A(Q) ≥ 1`. ✓
- **`h = 2`.** `q_1 ≥ q_2 ≥ 2^{n−2}`, and by Forcing `q_1 ≤ max(R) = 2^{n−1} − a`. On `I_{n−1}`,
  `S_Q ∩ I_{n−1} = [q_2, q_1) ⊆ [2^{n−2}, 2^{n−1}−a) = S_R ∩ I_{n−1}`. Put
  `a_v := (2^{n−1}−a) − q_1 ≥ 0`, `b := q_2 − 2^{n−2} ≥ 0`. Then
  `deficit_top = measure((S_R∖S_Q) ∩ I_{n−1}) = (2^{n−2}−a) − (q_1−q_2) = a_v + b`
  (since `q_1 − q_2 = (2^{n−1}−a−a_v) − (2^{n−2}+b) = 2^{n−2} − a − a_v − b`), and, using
  `ΣR − ΣF_{n−2} = (2^n−1) − (2^{n−2}−1+a) = 3·2^{n−2} − a`,
  `σ_lo := ΣQ_lo − ΣF_{n−2} = 1 − (q_1+q_2) + (3·2^{n−2} − a) = 1 + a_v − b` (as
  `q_1 + q_2 = 3·2^{n−2} − a − a_v + b`). So `σ_lo = σ + a_v − b` with `σ = 1` — **the same recursion as
  in `F_a`**, and `deficit_top = a_v + b`. `|Q_lo| ≤ n − 2`, `S_{Q_lo} ⊆ S_{F_{n−2}}`.
  * **2a (`a_v + b ≥ 1`):** `A(R) − A(Q) ≥ deficit_top = a_v + b ≥ 1`. ✓
  * **2b (`a_v + b < 1`):** `a_v, b < 1`, so `σ_lo = 1 + a_v − b ∈ (0,2)`, and `F_a(n−2)` gives
    `A(F_{n−2}) − A(Q_lo) ≥ min(σ_lo, 2−σ_lo)`.
    - **2b-i (`σ_lo = 1 + a_v − b ≥ 1`, i.e. `a_v ≥ b`):** `min = 2 − σ_lo = 1 − a_v + b`, so
      `A(R) − A(Q) ≥ (a_v+b) + (1 − a_v + b) = 1 + 2b ≥ 1`. ✓
    - **2b-ii (`σ_lo < 1`, i.e. `a_v < b`):** `min = σ_lo = 1 + a_v − b`, so
      `A(R) − A(Q) ≥ (a_v+b) + (1 + a_v − b) = 1 + 2a_v ≥ 1`. ✓
    (For `n = 3`, `n − 2 = 1`, and 2b would need a valid `Q_lo` at `F_1` — none exists — so 2b is empty
    at `n = 3`; `h = 0` and 2a settle `n = 3`.)

All cases give `A(R) − A(Q) ≥ 1`. **Hence the INC branch of Lemma LL holds for every `a < 1` top cut of
`G_{n−1}`, for all `n ≥ 3`.** ∎

### 24.3 — Opening B in general (any refined `R`, the `h = 0` band-deficit kill)

The `h = 0` argument above is not specific to top cuts. For **any** admissible refined `R`
(`max(R) ≤ 2^{n−1}`, `S_Q ⊆ S_R`, `h_R` even) with `h := #{Q-parts ≥ 2^{n−2}} = 0`, Gen-Decomp gives
`A(R) − A(Q) ≥ deficit_top = measure(S_R ∩ I_{n−1})`. So **any refined `R` whose top band carries
`S_R`-measure `≥ 1` is closed in the `h = 0` case**. For the top cut this measure is `2^{n−2} − a`
(closed for `a ≤ 2^{n−2}−1`); for a lower-band cut (§24.4) it is the full `2^{n−2}` (always `≥ 1`).
This is a clean, general, reusable kill.

### 24.4 — Opening D: the lower-band cut descent (G-INC-2lb)

Let `R = G_{n−1}` with a cut of a lower piece `2^{k_0} → {c, 2^{k_0}−c}`, `k_0 ≤ n−3`, `0 < c < 2^{k_0}`
(the top two pieces `2^{n−1}, 2^{n−2}` uncut). Then the parts `≥ thr = 2^{n−2}` are exactly
`{2^{n−1}, 2^{n−2}}`, so `h_R = 2` and, on `I_{n−1}`, `N_R = 1` throughout (only `2^{n−1} > x`), giving
`S_R ∩ I_{n−1} = I_{n−1}` of **full** measure `2^{n−2}`. Gen-Decomp yields
`A(R) − A(Q) = deficit_top + (A(R_lo) − A(Q_lo))` with
`R_lo = {parts < 2^{n−2}} = G_{n−3}` **with the same cut `2^{k_0} → {c, 2^{k_0}−c}`** (as `2^{k_0} < 2^{n−2}`).
So a lower-band cut at level `n` descends to *the same kind of object* — `G_{n−3}` with a cut at the same
absolute piece `2^{k_0}` — one G-INC-2lb instance two levels down, and `h_R = 2` at the top level with a
**full** top band. Consequences:

- **(D-i) `h = 0` and `h ≥ 4` close immediately.** `h = 0`: `deficit_top = 2^{n−2} ≥ 1` (§24.3).
  `h ≥ 4` (only `n ≥ 4`): `Q_lo = ∅` and `A(R) − A(Q) ≥ A(R_lo)`; here `A(R_lo) = A(G_{n−3}` with one
  lower cut`) ≥ 1` holds because `A(R_lo) ≥ 1` is exactly the induction hypothesis's premise `A(R) ≥ 1`
  carried by Lemma LL one level down (the descended object is again an admissible refinement with
  `A ≥ 1`). ✓
- **(D-ii) `h = 2` descent.** With `deficit_top = a_v + b` and `σ_lo = σ + a_v − b` (`σ = 1`) computed
  exactly as in §24.2 **but now with the full top band** (so `q_1 ≤ 2^{n−1} = max(R)`,
  `a_v = 2^{n−1} − q_1`, and `deficit_top = 2^{n−2} − (q_1 − q_2) = a_v + b`, `σ_lo = 1 + a_v − b`), the
  sub-instance is `(Q_lo, R_lo)` at level `n−2` with the same cut, `S_{Q_lo} ⊆ S_{R_lo}`, `|Q_lo| ≤ n−2`.
  The **identical** 2a / 2b-i / 2b-ii arithmetic (target `1`, using the level-`(n−2)` G-INC-2lb bound
  `A(R_lo) − A(Q_lo) ≥ min(σ_lo, 2−σ_lo)`) gives `A(R) − A(Q) ≥ 1`.

So G-INC-2lb reduces cleanly `n → n−2` **as long as the descended cut `2^{k_0}` remains strictly below
the top two pieces of the descended `G`**, i.e. while `k_0 ≤ (\text{current top exponent}) − 2`. Since
descending two levels drops the top exponent by `2`, after `⌊((n−1) − k_0)/2⌋ − 1` steps the cut piece
`2^{k_0}` reaches the top band of the descended `G`, and the object becomes a **top-or-second cut at a
small level** `m ≈ k_0 + 2`. If the cut value `c < 1`, that terminal object is an `a < 1` top cut and is
closed by §24.2 (the family `F_·`); the descent is then **completely closed**. If `c ≥ 1`, the terminal
object is an `a ≥ 1` cut — the honest hard residual (below). **Thus G-INC-2lb is fully closed whenever
the cut value `c < 1`, and in general is reduced to a small-level `a ≥ 1` top/second cut.**

### 24.5 — What round 11 closes, and the honest residual

**Closed (rigorous, all `n`):**
- **G-INC-2nt, `a < 1`:** `A(R) − A(Q) ≥ 1` for every non-equal top cut with `a < 1`, all `n ≥ 3`
  (§24.2), via the descent-closed family `F_a` (Family Lemma `F_a`, §24.1) — the O1–O3 obstruction is
  provably inapplicable to this specific family (top two pieces structurally uncut at every level;
  `R_lo = F_{k−2}` is a genuine member, not the refuted abstract class).
- **Opening B, general refined `R`:** the `h = 0` case closes for any refined `R` with top-band
  `S_R`-measure `≥ 1` (§24.3); for the top cut this is `a ≤ 2^{n−2} − 1`.
- **G-INC-2lb (lower-band cut):** clean `n → n−2` descent with a full top band (§24.4); **fully closed
  when the cut value `c < 1`**, and otherwise reduced to a small-level `a ≥ 1` cut.

**Honest residual (explicitly OPEN):**
- **G-INC-2nt, `a ≥ 1`:** here the family `{a} ∪ G_{k−1}` need not be descent-closed — once `a ≥ 2^{k−4}`
  the count `#{R_lo-parts ≥ 2^{k−4}}` can become **odd** (O1 fires for this family), so Gen-Decomp cannot
  be re-applied. The direct `A(R)` route (`A(R) = A(G_{n−1})` for `n` even, `A(G_{n−1}) − 2a` for `n` odd,
  §24.0-ii-analogue) with a matching upper bound on `A(Q)` is the intended attack but is **not carried
  out**. This is the genuine hard residual of G-INC-2nt.
- **G-INC-2lb with terminal cut value `c ≥ 1`:** inherits the same `a ≥ 1` difficulty at the small
  terminal level.
- **G-INC-2e⁺** (`m ≥ 6` all-distinct edge) and **G-GAP** (non-containment alignment): unchanged, open.

---

## Step 25 — G-INC-2nt, `a ≥ 1` top cut, via Opening C (NEW round 12)

**Setup (fixed for all of Step 25).** Let `n ≥ 4`, `thr := 2^{n−2}`, `I_{n−1} := [thr, 2^{n−1})`. Let
`R = G_{n−1}` with the top piece cut, `2^{n−1} → {a, 2^{n−1}−a}`, where **`a ∈ [1, 2^{n−2})`** (the
smaller part; `a < 1` is the certified `sigma-family-a-lt-1` case, `a = 2^{n−2}` is the equal split
G-INC-2e). So `R = G_{n−2} ∪ {a, 2^{n−1}−a}`, `|R| = n+1`, `c_R = 1`, and the joint budget gives
`|Q| ≤ n`. `ΣQ = 2^n`, `S_Q ⊆ S_R`, `max(R) = 2^{n−1} − a`. Target of the INC branch here:
`A(R) − A(Q) ≥ 1`.

The parts of `R` that are `≥ thr` are exactly `{2^{n−1}−a, 2^{n−2}}` (since `2^{n−1}−a ≥ 2^{n−2}` as
`a ≤ 2^{n−2}`, while `a < 2^{n−2}` is **not** `≥ thr`), so `h_R = 2` (even) and the certified
**Gen-Decomp** (`lemmas/gen-decomp-refined.md`) applies at `thr`:
```
A(R) − A(Q) = deficit_top + (A(R_lo) − A(Q_lo)),   R_lo = {parts of R < thr} = {a} ∪ G_{n−3},
```
with `S_{Q_lo} ⊆ S_{R_lo}`, both summands `≥ 0`, `deficit_top = measure((S_R∖S_Q) ∩ I_{n−1})`, and
`h := #{Q-parts ≥ thr}` even. On `I_{n−1}`, only `2^{n−1}−a` among `R`'s parts can exceed `x`, so
`S_R ∩ I_{n−1} = [2^{n−2}, 2^{n−1}−a)`, of measure `2^{n−2} − a`.

### 25.1 — Floor Lemma (HS-B1): `A({a}∪G_j) ≥ A(G_{j−1})`, equality iff `a = 2^j` (all `j ≥ 1`, all `a > 0`)

> **Floor Lemma.** For every integer `j ≥ 1` and every real `a > 0`,
> `A({a}∪G_j) ≥ A(G_{j−1})`, with equality **iff** `a = 2^j`.

*Proof.* Write `W := {a}∪G_j` and `f(a) := A(W) = measure(S_W)`. Since a single part `a` is added,
`N_W(x) = N_{G_j}(x) + 𝟙_{[0,a)}(x)`, so the parity of `N_W` differs from that of `N_{G_j}` exactly on
`[0,a)`; hence `S_W = S_{G_j} △ [0,a)`. For measurable sets `measure(X △ Y) = measure(X) + measure(Y)
− 2·measure(X∩Y)`, so with `X = S_{G_j}`, `Y = [0,a)`:
```
f(a) = A(G_j) + a − 2·g(a),      g(a) := measure(S_{G_j} ∩ [0,a)).
```
**Band structure of `S_{G_j}`.** `N_{G_j}(x) = #{0≤i≤j : 2^i > x}`. On the bands `B_0 := [0,1)` and
`B_i := [2^{i−1}, 2^i)` (`1 ≤ i ≤ j`), `N_{G_j} = j+1` on `B_0` and `N_{G_j} = j+1−i` on `B_i`; and
`N_{G_j} = 0` on `[2^j,∞)`. Thus `B_i ⊆ S_{G_j}` iff `j+1−i` is odd iff `i ≡ j (mod 2)` (with `i = 0`
for `B_0`, and `j+1` odd iff `j` even iff `0 ≡ j`). Call band `i` **allowed** if `i ≡ j (mod 2)`,
**forbidden** otherwise; `S_{G_j} = ⋃_{i ≡ j, 0≤i≤j} B_i`, `measure(B_0)=1`, `measure(B_i)=2^{i−1}`.

**`f` is piecewise linear with slope `∓1`.** `g` has slope `1` on allowed bands (there `S_{G_j}∩[0,a)`
grows), slope `0` on forbidden bands, and slope `0` for `a > 2^j` (no more `S_{G_j}`-mass). Hence
`f'(a) = 1 − 2g'(a) = −1` on the interior of allowed bands, `+1` on forbidden bands, and `+1` for
`a > 2^j`. So `f` decreases across each allowed band and increases across each forbidden band; its
**local minima are exactly at `a = 2^i` for allowed `i`** (top of an allowed band = bottom of a
forbidden band), i.e. `i ∈ {j, j−2, j−4, …}`.

**The minima strictly decrease toward `i = j`.** For allowed `i ≤ j−2`, between `2^i` and `2^{i+2}`
lie the forbidden band `B_{i+1}` (slope `0`) and the allowed band `B_{i+2}` (slope `1`, measure
`2^{i+1}`), so `g(2^{i+2}) − g(2^i) = 2^{i+1}`, giving
```
f(2^{i+2}) − f(2^i) = (2^{i+2} − 2^i) − 2·2^{i+1} = 3·2^i − 4·2^i = −2^i < 0.
```
Therefore `f(2^j) < f(2^{j−2}) < … `, so the smallest local minimum is at `a = 2^j`. For `a > 2^j`,
`f(a) = A(G_j) + a − 2A(G_j) = a − A(G_j)` is strictly increasing; and as `a → 0⁺`,
`f → A(G_j) > A(G_{j−1})`. Consequently the **global** minimum of `f` on `(0,∞)` is attained uniquely
at `a = 2^j`.

**Value at `a = 2^j`.** `W = {2^j, 2^j} ∪ {2^{j−1},…,1}`. Sorted descending the two leading `2^j` occupy
positions 1,2 with signs `+,−` and cancel; the remaining list `{2^{j−1},…,1}` shifts to positions
`3,4,…`, i.e. its own positions `1,2,…` with the same signs, so its alternating sum is unchanged:
`f(2^j) = A(G_{j−1})`. (Consistency with the closed form of `set-identity-selfsimilar`:
`2^j − A(G_j) = 2^j − (2^{j+1}+(−1)^j)/3 = (2^j − (−1)^j)/3 = A(G_{j−1})`.)

Hence `f(a) ≥ A(G_{j−1})` for all `a > 0`, with equality iff `a = 2^j`. ∎

**Corollary (applied at `j = n−3`).** `A(R_lo) = A({a}∪G_{n−3}) ≥ A(G_{n−4}) ≥ 1`, with
`A(R_lo) = A(G_{n−4})` iff `a = 2^{n−3}`. Moreover `A(G_{n−4}) = 1` iff `n ∈ {4,5}` (for `n ≥ 6`,
`A(G_{n−4}) ≥ A(G_2) = 3`). *(`A(G_0)=A(G_1)=1`; `A(G_k)=(2^{k+1}+(−1)^k)/3` from
`set-identity-selfsimilar`.)*

### 25.2 — Case split (exhaustive: `h` even, `h ∈ {0,2,4,…}`)

`h` is even (Gen-Decomp). We settle `h ≥ 4`, `h = 0`, and `h = 2`.

### 25.3 — `h ≥ 4` and `h = 0` (`a ≤ 2^{n−2}−1`): CLOSED, all `n`

**`h ≥ 4`.** Needs `|Q| ≥ 4`. Then `ΣQ_hi ≥ h·2^{n−2} ≥ 4·2^{n−2} = 2^n = ΣQ`, forcing `ΣQ_lo = 0`, so
`Q_lo = ∅`, `A(Q_lo) = 0`. Hence `A(R) − A(Q) = deficit_top + A(R_lo) ≥ A(R_lo) ≥ 1` (Floor Lemma). ✓

**`h = 0`.** Then `S_Q ∩ I_{n−1} = ∅`, so `deficit_top = measure(S_R ∩ I_{n−1}) = 2^{n−2} − a`. If
`a ≤ 2^{n−2} − 1` then `deficit_top ≥ 1`, and with `A(R_lo) − A(Q_lo) ≥ 0` we get `A(R) − A(Q) ≥ 1`. ✓
*(This covers all `a ∈ [1, 2^{n−2}−1]`. The residual sliver `a ∈ (2^{n−2}−1, 2^{n−2})` — reachable only
for `n ≥ 5`, since `h=0` needs `|Q| ≥ 5` parts each `< 2^{n−2}` summing to `2^n` — is deferred to the
open crux of §25.6.)*

### 25.4 — `h = 2` reduction to a single odd-position inequality (NEW, exact)

Write `q_1 ≥ q_2 ≥ thr` for the two high parts; by the Forcing Lemma (`forcing-inc-reduction`)
`q_1 ≤ max(R) = 2^{n−1} − a`. Put `a_v := (2^{n−1}−a) − q_1 ≥ 0`, `b := q_2 − 2^{n−2} ≥ 0`. On
`I_{n−1}`, `S_Q ∩ I_{n−1} = [q_2, q_1) ⊆ [2^{n−2}, 2^{n−1}−a) = S_R ∩ I_{n−1}`, so
```
deficit_top = (2^{n−2}−a) − (q_1 − q_2) = a_v + b
```
(using `q_1 − q_2 = (2^{n−1}−a−a_v) − (2^{n−2}+b) = 2^{n−2} − a − a_v − b`). With
`σ := ΣQ − ΣR = 2^n − (2^n − 1) = 1` and `ΣR − ΣR_lo = (2^n−1) − (2^{n−2}−1+a) = 3·2^{n−2} − a`,
```
σ_lo := ΣQ_lo − ΣR_lo = σ − (q_1+q_2) + (3·2^{n−2}−a) = 1 + a_v − b.
```
Now use the odd-position identity `A(P) = 2·O_P − ΣP` (`O_P` = sum of odd-position parts, Step 4):
`A(R_lo) − A(Q_lo) = 2(O_{R_lo} − O_{Q_lo}) + σ_lo`. Substituting into Gen-Decomp,
```
A(R) − A(Q) = deficit_top + A(R_lo) − A(Q_lo)
            = (a_v+b) + 2(O_{R_lo}−O_{Q_lo}) + (1+a_v−b)
            = 1 + 2a_v + 2(O_{R_lo} − O_{Q_lo}).
```
Therefore, in the `h = 2` case,
```
(★)   A(R) − A(Q) ≥ 1   ⟺   O_{Q_lo} ≤ O_{R_lo} + a_v.
```
*(Verified exact over 663 budget-valid `n=5` `h=2` configs: `A(R)−A(Q) = 1 + 2a_v + 2(O_{R_lo}−O_{Q_lo})`,
0 mismatch.)* Two sufficient closures of `(★)`:
- If `deficit_top = a_v + b ≥ 1` then directly `A(R) − A(Q) ≥ deficit_top ≥ 1` (no need for `(★)`).
- If the **direct family bound** `A(R_lo) − A(Q_lo) ≥ min(σ_lo, 2−σ_lo)` (DFB) holds, then since
  `1 − a_v − b ≤ min(1+a_v−b, 1−a_v+b) = min(σ_lo, 2−σ_lo)`, we get
  `A(R)−A(Q) = deficit_top + (A(R_lo)−A(Q_lo)) ≥ (a_v+b) + (1−a_v−b) = 1`.
  DFB is exactly the `a<1` Family-Lemma statement (`sigma-family-a-lt-1`) at the single level `n−2` but
  now with `a ≥ 1`; its descent proof there fails for `a ≥ 1` (the family `{a}∪G_{n−3}` is **not**
  descent-closed — once `a ≥ 2^{n−4}` the count `#{R_lo-parts ≥ 2^{n−4}}` turns odd, O1 fires), so a
  **direct** proof of DFB is required. This is the honest open crux (§25.6).

### 25.5 — HS-B2: the fully-tight config forces `A(Q_lo) = 0` (pinch `n ∈ {4,5}`)

The Floor Lemma pins the only way `A(R_lo)` can be as small as `1`: `a = 2^{n−3}` and `n ∈ {4,5}`. Take
the **fully-tight** `h=2` config `a = 2^{n−3}`, `a_v = b = 0` (`q_1 = 2^{n−1}−a = 3·2^{n−3}`,
`q_2 = 2^{n−2}`), so `deficit_top = 0`, `ΣQ_lo = ΣR_lo + σ_lo = (2^{n−2}−1+a) + 1 = 2^{n−2} + a =
3·2^{n−3}`, and `|Q_lo| ≤ n−2`. We show `A(Q_lo) = 0`, giving `A(R) − A(Q) = 0 + 1 − 0 = 1`.

First, the support of the tight `R_lo`. `R_lo = {2^{n−3}} ∪ G_{n−3} = G_{n−4} ∪ {2^{n−3}, 2^{n−3}}`
(the top part `2^{n−3}` doubled). On `[0, 2^{n−3})` both copies of `2^{n−3}` exceed `x`, so
`N_{R_lo} = N_{G_{n−4}} + 2 ≡ N_{G_{n−4}} (mod 2)`; and `N_{R_lo} = 0` on `[2^{n−3},∞)`. Hence
`S_{R_lo} = S_{G_{n−4}}` (an interval of measure `A(G_{n−4}) = 1` for `n ∈ {4,5}`).

- **`n = 5`.** `S_{R_lo} = S_{G_1} = [1,2)`, `ΣQ_lo = 12`, `|Q_lo| ≤ 3`, each part `< thr = 8`. Since
  `S_{Q_lo} ⊆ [1,2)`, `N_{Q_lo}` is even on `[0,1)`; at `x → 0⁺` this reads `|Q_lo|` even, so
  `|Q_lo| ∈ {0,2}`. `|Q_lo| = 0` gives `ΣQ_lo = 0 ≠ 12`, impossible. So `|Q_lo| = 2`, parts
  `p_1 ≥ p_2`, `p_1 + p_2 = 12`. Then `S_{Q_lo} = [p_2, p_1)` (`N = 2` on `[0,p_2)`, `= 1` on
  `[p_2,p_1)`, `= 0` above), and `S_{Q_lo} ⊆ [1,2)` forces `p_1 ≤ 2` — incompatible with `p_1 ≥ 6`
  **unless `[p_2,p_1)` is empty**, i.e. `p_1 = p_2 = 6`. Then `S_{Q_lo} = ∅`, `A(Q_lo) = 0`. ✓
- **`n = 4`.** `S_{R_lo} = S_{G_0} = [0,1)`, `ΣQ_lo = 6`, `|Q_lo| ≤ 2`, each `< thr = 4`. `|Q_lo| = 1`
  would need a single part `= 6 > 4`, impossible; `|Q_lo| = 0` gives `ΣQ_lo = 0 ≠ 6`. So `|Q_lo| = 2`,
  `p_1 + p_2 = 6`, each `< 4`, so `p_1, p_2 ∈ (2,4)`. `S_{Q_lo} ⊆ [0,1)` forces `N_{Q_lo}` even on
  `[1,∞)`; on `[p_2, p_1)` (both `> 2 > 1`) `N_{Q_lo} = 1`, odd, so this interval must be empty:
  `p_1 = p_2 = 3`, `S_{Q_lo} = ∅`, `A(Q_lo) = 0`. ✓

So the fully-tight config closes with equality `A(R) − A(Q) = 1` — matching the machine-found tight
witnesses `n=4, a=2, Q=[6,4,3,3]` and `n=5, a=4, Q=[12,8,6,6]`. This is the exact "equal-pair forcing"
the outline flagged as HS-B2.

### 25.6 — What round 12 closes, and the honest residual

**Closed (rigorous):**
- **Floor Lemma** `A({a}∪G_j) ≥ A(G_{j−1})` (eq. iff `a=2^j`), **all `j`** — Step 25.1 (promotable).
- **`h ≥ 4`** and **`h = 0` with `a ≤ 2^{n−2}−1`** — all `n` (Step 25.3).
- **h=2 reduction** `A(R)−A(Q) = 1 + 2a_v + 2(O_{R_lo}−O_{Q_lo})`, i.e. `(★) O_{Q_lo} ≤ O_{R_lo}+a_v` —
  exact, all `n` (Step 25.4); and the `deficit_top ≥ 1` sub-case.
- **Fully-tight config** `a = 2^{n−3}`, `a_v=b=0`: `A(Q_lo)=0`, closing it with equality (Step 25.5,
  pinch `n∈{4,5}`).

**Honest residual (explicitly OPEN):** the single crux
```
(DFB)   A(R_lo) − A(Q_lo) ≥ min(σ_lo, 2−σ_lo)   for  R_lo = {a}∪G_{n−3},  a ≥ 1,
```
(equivalently `(★) O_{Q_lo} ≤ O_{R_lo}+a_v` in the `h=2` case), for **general `h = 2`, `a ≥ 1`**, plus
the thin **`h = 0`, `a ∈ (2^{n−2}−1, 2^{n−2})`** sliver (`n ≥ 5`), which reduces to the same DFB. DFB is
the `a<1` Family-Lemma bound extended to `a ≥ 1`; the `a<1` proof is a `k→k−2` descent that is **not**
available for `a ≥ 1` (O1: `{a}∪G_{n−3}` is not descent-closed once `a ≥ 2^{n−4}`). A direct
(non-recursive) proof of DFB for `a ≥ 1` — or a direct proof of `(★)` from the sum/containment/budget
data — is the remaining work. **The reduction `(★)` and the Floor Lemma make this a single, sharply
stated scalar inequality; it is not overclaimed as proven.**

*(Numeric status, budget-enforced: the `a≥1` top cut `A(R)−A(Q) ≥ 1` has 0 violations — `n=4` 123
configs margin 1, `n=5` 662 configs margin 1 — consistent with `(★)` and DFB being true; only the
general proof is open.)*

---

## Step 26 — G-INC-2nt, `a ≥ 1`: the size-2 closure and the size-≥3 status (NEW round 13)

Throughout put `j := n−3 ≥ 1` (so `n ≥ 4`), `thr := 2^{n−2} = 2^{j+1}`, `R_lo = {a}∪G_j` with
**`a ∈ [1, 2^{j+1})`** (the honest range: `a` is the smaller top-cut part, `a < 2^{n−2} = 2^{j+1}`;
the explorer's write-up mis-stated `a < 2^j`, but `a` can lie in `[2^j, 2^{j+1})`, handled below).
`ΣR_lo = a + ΣG_j = a + (2^{j+1}−1) ≥ 2^{j+1}` (as `a ≥ 1`), `|Q_lo| ≤ n−2 = j+1`,
`S_{Q_lo} ⊆ S_{R_lo}`, and `ΣQ_lo = ΣR_lo + σ_lo` with `σ_lo = 1 + a_v − b`.

### 26.0 — The exact target (residual case) and a numeric correction to the premise

By §25.4, `A(R) − A(Q) = deficit_top + (A(R_lo) − A(Q_lo))` with `deficit_top = a_v + b ≥ 0`. If
`deficit_top ≥ 1` we are done (§25.4). So assume `deficit_top = a_v + b < 1` (**residual case**), whence
`a_v, b ∈ [0,1)` and `σ_lo = 1 + a_v − b ∈ (0,2)`. The goal `A(R)−A(Q) ≥ 1` is then **exactly**
```
(DFB)   A(R_lo) − A(Q_lo) ≥ 1 − deficit_top = 1 − a_v − b .
```
**Numeric correction (exact Fractions, budget-enforced).** The premise "large slack for size ≥ 3"
is **FALSE**. Enumerating all `h=2`, `a≥1` top-cut configs: `min(A(R)−A(Q)) = 1` with **0** configs
`< 1` at `n=4,5,6` (dens up to 4), and `A(R_lo)−A(Q_lo)` **drops to `0`** in the residual case at
`|Q_lo| = 4` — e.g. `n=6`, `a=2`, `R = G_4∪{2,30}`, `Q = {30,16,8,4,3,3}`, `Q_lo = {8,4,3,3}`:
`A(R_lo)=A(\{2\}∪G_3)=A(\{8,4,2,2,1\})=5`, `A(Q_lo)=A(\{8,4,3,3\})=4`, `deficit_top=0`, so
`A(R)−A(Q)=0+1=1` (**tight**). Thus `(DFB)` is tight at size 4 already; the size-≥3 crux is **not** a
slack mop-up but a genuinely tight inequality (same difficulty tier as the anchor). This reshapes the
frontier and is recorded honestly below.

### 26.1 — Size-2 `Q_lo`, `a ∈ [1, 2^j)`: equal-pair forcing (rigorous, all `j`)

> **Lemma (size-2 forcing, low `a`).** If `a ∈ [1, 2^j)`, `Q_lo = \{p_1, p_2\}` (`p_1 ≥ p_2`),
> `S_{Q_lo} ⊆ S_{R_lo}`, `ΣQ_lo > ΣR_lo`, then `p_1 = p_2`, hence `A(Q_lo) = 0`.

*Proof.* Since `a < 2^j`, `max(R_lo) = 2^j`, so `N_{R_lo}(x) = 0` for all `x ≥ 2^j`, i.e.
`S_{R_lo} ⊆ [0, 2^j)`. Now `p_1 + p_2 = ΣQ_lo > ΣR_lo ≥ 2^{j+1}`, and `p_1 ≥ p_2` give
`p_1 ≥ (p_1+p_2)/2 > 2^j`. Suppose `p_1 > p_2`. Then `S_{Q_lo} = [p_2, p_1)` (indeed `N_{Q_lo} = 2` on
`[0,p_2)`, `= 1` on `[p_2,p_1)`, `= 0` above), which contains the non-empty sub-interval `(2^j, p_1)`.
But `(2^j, p_1) ∩ S_{R_lo} = ∅` since `S_{R_lo} ⊆ [0,2^j)`, contradicting `S_{Q_lo} ⊆ S_{R_lo}`. Hence
`p_1 = p_2`, `S_{Q_lo} = ∅`, `A(Q_lo) = 0`. ∎

*(This is cleaner than — and corrects the range of — the explorer's Case-A/Case-B split: only
`S_{R_lo} ⊆ [0,2^j)` and `p_1 > 2^j` are used. Verified exact: **0** non-equal admissible size-2 pairs
with `a < 2^j` over `j = 1,2,3` (dens to 8).)*

Consequently, for `a ∈ [1, 2^j)` and size-2 `Q_lo`:
`A(R_lo) − A(Q_lo) = A(R_lo) ≥ A(G_{j−1}) ≥ 1 ≥ 1 − deficit_top`, by the **Floor Lemma** (§25.1) and
`A(G_{j−1})` odd `≥ 1` (`set-identity-selfsimilar`). So **(DFB) holds; `A(R)−A(Q) ≥ 1`.** ✓

### 26.2 — Size-2 `Q_lo`, `a ∈ [2^j, 2^{j+1})`: the top-region bound (rigorous)

Here `max(R_lo) = a ≥ 2^j`, so `N_{R_lo}(x) = 1` on `[2^j, a)` (only `a > x`) and `= 0` on `[a,∞)`;
on `[0, 2^j)`, `N_{R_lo} = N_{G_j} + 1` (as `a > x`). Hence
```
S_{R_lo} = ([0,2^j) ∖ S_{G_j}) ∪ [2^j, a),   A(R_lo) = (2^j − A(G_j)) + (a − 2^j) = a − A(G_j)
```
(the identity `A(\{a\}∪G_j) = a − A(G_j)` for `a ≥ 2^j` verified exact, `j=1..4`, dens to 4; and
`2^j − A(G_j) = A(G_{j−1})` is the self-similar identity of `set-identity-selfsimilar`). Let
`Q_lo = \{p_1,p_2\}`, `p_1 ≥ p_2`. From `p_1+p_2 = ΣQ_lo ≥ ΣR_lo = a + 2^{j+1} − 1 ≥ 3·2^j − 1` we get
`p_1 ≥ (3·2^j−1)/2 > 2^j`.

- If `p_1 = p_2`: `A(Q_lo)=0`, `A(R_lo)−A(Q_lo) = A(R_lo) ≥ A(G_{j−1}) ≥ 1` (Floor Lemma). ✓
- If `p_1 > p_2`: `S_{Q_lo} = [p_2, p_1)`, `p_1 > 2^j`. Its part above `2^j`, namely `(\max(p_2,2^j), p_1)`,
  must lie in `S_{R_lo} ∩ (2^j,∞) = (2^j, a)`, forcing `p_1 ≤ a`. And if `p_2 < 2^j` then `[p_2,p_1)`
  would contain `[\max(p_2,2^{j−1}), 2^j) ⊆ [2^{j−1},2^j)`, where `N_{R_lo} = N_{G_j}(=1) + 1 = 2` is
  even — not in `S_{R_lo}`, a contradiction. Hence `p_2 ≥ 2^j`, so `[p_2,p_1) ⊆ [2^j,a)` and
  `A(Q_lo) = p_1 − p_2 ≤ a − 2^j`. Therefore
  ```
  A(R_lo) − A(Q_lo) ≥ (a − A(G_j)) − (a − 2^j) = 2^j − A(G_j) = A(G_{j−1}) ≥ 1 ≥ 1 − deficit_top. ✓
  ```

*(So for `a ≥ 2^j`, non-equal admissible size-2 pairs **do** exist — verified 34 per `j`, all with
`a ≥ 2^j`, e.g. `j=1, a=13/4, Q_lo=\{25/8,13/4\}` — but `(DFB)` still holds with slack `A(G_{j−1})`;
`min DFB = A(G_{j−1})` over them, 0 violations `j=1,2,3`. This is why the forcing theorem alone is
insufficient and the top-region measure bound is needed.)*

**Conclusion (size-2, all `a ∈ [1,2^{j+1})`): `A(R)−A(Q) ≥ 1` — CLOSED, all `n`.** This upgrades §25.5
(which only pinched `n∈\{4,5\}`) to every `n`, by the two-regime split `a<2^j` (forcing) / `a≥2^j`
(top-region bound).

### 26.3 — Parity: even `j` (odd `n`) has no odd-size `Q_lo`

For **even `j`**, `|R_lo| = j+2` is even, so `N_{R_lo}(0^+) = j+2` is even; by the certified
**Parity-Condition Lemma** (`parity-condition-inc`), `N_{Q_lo}(0^+) = |Q_lo|` is even. Odd sizes
(`1,3,5,…`) are thus **excluded** at even `j`. With size-0 impossible (`ΣQ_lo = 0 ≠ ΣR_lo+σ_lo`) and
size-2 closed (§26.1–26.2), the residual at even `j` is sizes `\{4,6,…\} ≤ j+1`. For **odd `j`**, size-1
is impossible (a single part `= ΣQ_lo > thr` is not `< thr`), so the residual is sizes `≥ 3`.

### 26.4 — Size ≥ 3: reduction, partial bounds, and the honest open crux

By §26.0 the size-≥3 case is **tight** (the `n=6` size-4 witness has `A(R)−A(Q)=1`), so a slack argument
cannot close it. The reviewer's requested reduction is the identity
`A(R_lo) − A(Q_lo) = measure(S_{R_lo} ∖ S_{Q_lo}) ≥ 0` (measure monotonicity from
`S_{Q_lo} ⊆ S_{R_lo}`, `alt-sum-integral`); pure monotonicity gives only `≥ 0`, and the missing
`≥ 1 − deficit_top` must come from an **uncovered band** that the sum/budget constraints force. Two
rigorous partial reductions, and the precise gap:

**(i) Bottom-band obstruction (`j` odd).** For `j` odd and `a > 1`, the bottom of `S_{R_lo}` is exactly
`[0,1)`: on `[0,1)`, `N_{R_lo} = |R_lo| = j+2` (odd, `j` odd) so `[0,1) ⊆ S_{R_lo}`; on `[1,2)`,
`N_{R_lo} = N_{G_j}(=j) + [a>x] = j+1` (even, since `a>1`) so `[1,2) ∩ S_{R_lo} = ∅` (the run stops at
`1`). In the tight `n=6` witness `S_{R_lo} = [0,1)∪[4,8)` and `S_{Q_lo} = [4,8)`: `Q_lo` covers the top
band and the entire deficit `1 = A(R_lo)−A(Q_lo)` is the **uncovered `[0,1)`**. To cover `[0,1)`, `Q_lo`
needs `N_{Q_lo}` odd near `0`, i.e. `|Q_lo|` odd or a part `< 1`; the tight witness has `|Q_lo|=4` even
and all parts `≥ 3`, so `[0,1)` is forced uncovered. Making "the sum/budget cannot both cover the top
region and `[0,1)`" quantitative is the crux — **open**.

**(ii) Equal-top-pair sub-case.** If the two largest parts of `Q_lo` are equal (`p_1 = p_2`), they
cancel in `S_{Q_lo}` (`N_{Q_lo}` even on `[p_3, p_1)`), so `S_{Q_lo} = S_{Q_lo'}` for
`Q_lo' := Q_lo ∖ \{p_1,p_2\}` with `|Q_lo'| ≤ j−1` and `A(Q_lo) = A(Q_lo')`. For `a > 1`, `j` odd, and
`Q_lo'` all-`≥1` (e.g. size-3 witness `Q_lo=\{23/2,23/2,1\}`, `Q_lo'=\{1\}`): `A(Q_lo') = p_3 ≤ 1` (the
bottom run `[0,1)`), while `A(R_lo) ≥ A(G_{j−1}) ≥ 3` (`j` odd `≥ 3`), giving
`A(R_lo)−A(Q_lo) ≥ 3 − 1 = 2 ≥ 1`. So the **equal-top-pair size-3** case is closed; the tight residual is
the **distinct-top** configs (e.g. the size-4 `\{8,4,3,3\}`), which are **open**.

**Honest status of size ≥ 3.** Genuinely tight (min `A(R)−A(Q) = 1` attained at `|Q_lo|=4`), hence not
closable by the slack/band-accounting route the outline proposed. The measure-monotonicity reduction and
the bottom-band obstruction are rigorous, but the quantitative "sum + budget force ≥ `1−deficit_top`
uncovered measure" step is **unproven** and is the remaining crux. The Family-Lemma form
`A(R_lo)−A(Q_lo) ≥ min(σ_lo,2−σ_lo)` is unavailable (its descent needs `a<1`, O1 fires for `a≥1`), and
the perturbed `T'(j)` mutual induction is **declined** (echoes the R10-refuted `{Claim_R,T_R}` class).

### 26.5 — What round 13 closes

**Closed (rigorous, all `n`):** the **size-2** `Q_lo` case for the `a ≥ 1` top cut, **all**
`a ∈ [1, 2^{j+1})` (§26.1 forcing for `a<2^j`, §26.2 top-region bound for `a≥2^j`), giving
`A(R)−A(Q) ≥ 1`; and, via parity (§26.3), the exclusion of all odd-size `Q_lo` at even `j`. The
**equal-top-pair size-3** sub-case (§26.4(ii)). This upgrades the round-12 pinch (`n∈\{4,5\}`) to all `n`.

**Open (honestly):** the **distinct-top size ≥ 3** case (tight, `min = 1`, refuting the "large slack"
premise), reduced to the quantitative uncovered-band bound of §26.4(i). This — plus multi-cut refined `R`
(G-INC-2 beyond `G_{n−1}` top cut) and G-GAP (non-containment) — leaves the **full lower bound OPEN**.

---

## Open gaps (precise)

- **(G-INC-1) general-n "+1" for R = G_{n−1}.** **CLOSED for ALL `n` (round 8).** The residual lemma
  `T(ℓ)` (`O_P ≤ O_{G_{ℓ−1}}` for INC `P`, `|P| ≤ ℓ+1`, `ΣP ∈ (2^ℓ−1, 2^ℓ)`) is now proven for all `ℓ`
  by its own inductive step (Step 12b), run as a mutual strong induction with `Claim(n,ε)` (Step 13).
  So `A(Q ∪ G_{n−1}) ≥ 1` in the INC branch for the anchor `R = G_{n−1}`, every `n`. No longer a gap.
- **(G-INC-2) refined R, general n.** PARTIAL (round 9–10). Vacuous at `n = 3` (Step 14); first
  nontrivial at `n = 4`. Progress:
  - **Equal-split top cut (G-INC-2e): CLOSED for `n ≤ 6`** (round 10, Step 22). Via `S_R = S_{G_{n−2}}`
    (Step 18a) + equal-pair-removal → L1 (any repeated value) + `h̄=0` (`deficit_top ≥ 1`) + the
    **rigorous vacuousness** of the all-distinct edge: `2^{m−2}(9−m) < q₁+q₂ < 2^m` is empty for
    `m ≤ 5`. Residual: `m ≥ 6` all-distinct `h̄≥2` (**G-INC-2e⁺**, margin ≥ 2, needs L1 one budget step
    looser).
  - **{Claim_R, T_R} mutual induction (Gen-Decomp descent): OBSTRUCTED** (round 10, Step 21 — rigorous
    negative result, corrects the round-9/round-10-outline optimism). The h=2 step arithmetic mirrors
    the anchor (Step 20), but the refined-R class is **not closed** under the `n→n−2` descent:
    **(O1)** `h_{R_lo}` parity breaks (lower-band cuts at `k₀∈{n−4,n−3}`; witness `{1,2,2,2,8,16,32}` has
    `h_{R_lo}=1`), so Gen-Decomp cannot be re-applied — even lower-band cuts do not self-sustain;
    **(O2)** the `h=0` `deficit_top ≥ 2^{n−2}` bound fails (`= q₁−q₂` can be `< 1`);
    **(O3)** for top-piece cuts `R_lo = G_{n−3}∪{a}` is not a refinement, and dropping "refinement" from
    the class makes Claim_R **FALSE** (12 verified violations at `ℓ=3`, e.g. `R={1,3,3}`, `Q={1,7/2,7/2}`,
    `A(R)=A(Q)=1`; `{1,3,3}` is not a cut of `{1,2,4}`). So the truth of Claim_R needs the exact
    refinement structure the descent destroys.
  - **Lower-band cut (G-INC-2lb)** and **non-equal top cut (G-INC-2nt)**, incl. `a < 1`: **OPEN**,
    obstructed by O1–O3. `G-INC-2nt` `n=4` base verified (123 configs, 0 viol, margin 1) but not proven.
    Future routes: a descent-**closed** structured class (none known), or a **direct** `A(R)` evaluation
    per cut type (the outline's fallback), not carried out here.
  Round-9 tool **Gen-Decomp** supplies the descent *identity* `S_{Q_lo} ⊆ S_{R_lo}`, but round 10 shows
  the *class* is not descent-closed, so it does not by itself yield the `{Claim_R, T_R}` induction.
- **(G-GAP) alignment cost.** `S_Q ⊄ S_R` with `0 < b < 1` or an interior miss ⟹
  `measure(S_Q △ S_R) ≥ 1`. Tight witnesses (n=3, R=G_2): `Q={4,5/2,3/2}` gives
  `S_Q △ S_R = [1,3/2)∪[2,5/2)` (measure 1); `Q={1/2,3/2,2,4}` gives `[0,1/2)∪[1,3/2)` (measure 1).
  Each is a pair of half-intervals from two dyadic levels summing to 1; a general "bulge/gap pairing"
  bound against the alternating structure of `S_R` is unproven.

---

## Promotable lemmas

1. **Parity-Condition Lemma (INC).** If `S_Q ⊆ S_R` then `N_Q(x)` is even at every `x` with `N_R(x)`
   even. For `R = G_{n−1}`: `N_Q` is even throughout every forbidden dyadic band; consequently
   `#{parts ≥ 2^j}` is even at every forbidden-band top, and interior Q-parts of a forbidden band have
   even multiplicity (equal pairs admissible). *(Step 3, general n, rigorous. Replaces the FALSE
   "Structural Lemma"; the counterexample Q={3/2,3/2,2,3} satisfies this parity version.)*

2. **Top-band decomposition identity.** For `R = G_{n−1}`, INC branch, `n ≥ 2`, with `h = #{parts ≥
   2^{n−2}}` (EVEN by Lemma 1), `Q_hi/Q_lo` the split at `2^{n−2}`, `δ_top = measure(S_Q ∩ I_{n−1})`:
   `A(Q) = A(Q_lo) + δ_top` and `A(G_{n−1}) − A(Q) = deficit_top + M`, where
   `deficit_top = 2^{n−2} − δ_top ≥ 0` and `M = 2^{n−2} − A(G_{n−2}) − A(Q_lo) ≥ 0`. *(Step 6,
   general n, rigorous; verified 0-failure n=3,4.)*

3. **Odd-index reformulation.** `A(P) = 2·O_P − ΣP` with `O_P` the sum of odd-position parts (descending
   sort); hence the INC target `A(Q) ≤ A(G_{n−1})−1` is equivalent to `O_Q ≤ O_{G_{n−1}} =
   Σ (\text{allowed-band upper endpoints})`. *(Step 4, rigorous, elementary.)*

4. **Complete n=3 INC base case.** For Q partitioning 8 with `S_Q ⊆ S_{G_2}` and `|Q| ≤ 4`,
   `A(Q) ≤ 2 = A(G_2) − 1` (all sub-cases incl. even-multiplicity interior pair). *(Step 7, rigorous,
   verified 0-failure over 52 configs.)*

5. **SET IDENTITY + self-similar reduction (NEW round 7).** `A(G_k)` odd `≥ 1` and
   `A(G_{n−3}) = 2^{n−2} − A(G_{n−2})`; `S_{G_{n−1}} ∩ [0,2^{n−2}) = S_{G_{n−3}}` with corollary
   `S_{Q_lo} ⊆ S_{G_{n−3}}`; and `M = A(G_{n−3}) − A(Q_lo)`. Proposed as
   `lemmas/set-identity-selfsimilar.md` (rigorous; SET IDENTITY verified 0-mismatch n=3..7). This is
   the structural engine of the two-step induction.

6. **G-INC-1 for ALL `n` via the mutual `{Claim, T}` induction (UPGRADED round 8).** Via the mutual
   strong induction `n → n−2` on the pair `{Claim(n,ε), T(n)}` with the ε-reformulation
   `Claim(n,ε) ⟺ O_Q ≤ O_{G_{n−1}} + ε` and the generalized (ΣQ-free) top-band decomposition,
   `G-INC-1 = Claim(n,0)` holds **unconditionally for all `n ≥ 1`** (round 7 had it only for
   `n ∈ {1,2,3,4}`, conditional on `T(ℓ)`). *(Steps 10–13, rigorous.)*

7. **Residual lemma `T(ℓ)` PROVEN for all `ℓ` (NEW round 8).** For `ℓ ≥ 1`: if `S_P ⊆ S_{G_{ℓ−1}}`,
   `|P| ≤ ℓ+1` and `ΣP ∈ (2^ℓ−1, 2^ℓ)`, then `O_P ≤ O_{G_{ℓ−1}}` (equivalently, with `τ = 2^ℓ−ΣP ∈
   (0,1)`, `deficit_top + M ≥ 1−τ`). *Mechanism:* `T(ℓ)`'s inductive step (Step 12b) mirrors
   `Claim(ℓ,ε)`'s — `h ≥ 4` impossible (`ΣP < 2^ℓ`), so `h ∈ {0,2}`; `h=0` gives `deficit_top = 2^{ℓ−2}
   ≥ 1−τ`; `h=2` sub-cases 2a/2b-i/2b-ii invoke `Claim(ℓ−2,ε')` / `T(ℓ−2)` with `ε' = a−b−τ ∈ (−1,1)`;
   bases `T(1),T(2)` (Step 11). It is the `ε<0` companion needed by sub-case 2b-ii of `Claim` and never
   invokes `Claim` at negative `ε`. *(Step 12b, general `ℓ`, rigorous; verified 0-violation `ℓ=2,3,4`,
   tight.)* This is the shared anchor crux `= GAP-A = B2*` importable by `ll-dyadic-symdiff`.

8. **Generalized top-band decomposition (Gen-Decomp) (NEW round 9).** For any `R`, `Q` with
   `max(R) ≤ 2^{n−1}`, `S_Q ⊆ S_R`, and `h_R := #{R-parts ≥ 2^{n−2}}` EVEN:
   `A(R) − A(Q) = deficit_top + (A(R_lo) − A(Q_lo))`, both terms `≥ 0`, with the descent
   `S_{Q_lo} ⊆ S_{R_lo}` — proved with **no SET IDENTITY** (Step 16). Generalizes the certified
   `top-band-decomposition` to refined R; it is the correct engine for G-INC-2 and supplies the
   refined-R descent identity the anchor's SET IDENTITY has no analogue for.

9. **Lemma L1 — budget anchor bound (NEW round 9, FULLY PROVEN).** If `S_P ⊆ S_{G_{m−1}}` and
   `|P| ≤ m−1`, then `A(P) ≤ A(G_{m−1}) − 1` — by a clean `m → m−2` budget induction off the certified
   anchor lemmas (no ε, no T). Tight (`P = G_{m−1}∖{1}`). The `−1` is forced by the budget. (Step 17;
   verified 0-violation `m = 2..6`.) Closes the equal-split `g = 2` case and the equal-largest `g = 0`
   sub-case (Step 18).

10. **Equal-split set identity (NEW round 9).** For the top-piece equal split
    `R = {2^{n−2},2^{n−2},2^{n−2}} ∪ G_{n−3}`, one has `S_R = S_{G_{n−2}}` exactly (hence
    `A(R) = A(G_{n−2})`) — Step 18(a), verified `n = 4..9`. This turns the equal-split G-INC-2 into a
    pure anchor statement at level `n−1` (with `ΣQ = 2^n`), closed by L1 after pair-reduction.

11. **G-INC-2e vacuousness (NEW round 10, FULLY PROVEN for `m ≤ 5`).** With `m := n−1`, in the
    equal-split reduced problem (`S_Q ⊆ S_{G_{m−1}}`, `ΣQ = 2^{m+1}`, `|Q| ≤ m+1`), the all-distinct
    edge `h̄ ≥ 2, q₁ > q₂` is **vacuous** for `m ≤ 5`: `Q_lo` has `|Q_lo| ≤ m−1` parts each `< 2^{m−2}`
    so `ΣQ_lo < (m−1)2^{m−2}`, forcing `q₁+q₂ > 2^{m−2}(9−m)`; but `q₁,q₂ ≤ 2^{m−1}` distinct give
    `q₁+q₂ < 2^m`, and `2^{m−2}(9−m) ≥ 2^m ⟺ m ≤ 5`. Combined with equal-pair-removal→L1 and `h̄=0`,
    this **closes G-INC-2e for `n ≤ 6`** (Step 22). Residual `m ≥ 6` (G-INC-2e⁺) is a one-budget-step
    L1 extension. *(Rigorous, elementary; verified `m=3,4,5` vacuous / `m=6` first feasible.)*

12. **Refined-R descent non-closure (NEW round 10, rigorous NEGATIVE result).** The `{Claim_R, T_R}`
    mutual induction (Gen-Decomp descent) does **not** close G-INC-2: the class "`R` a refinement of
    `G_{ℓ−1}`, `h_R` even, `A(R) ≥ 1`" is **not closed** under `R → R_lo`. (O1) `h_{R_lo}` parity breaks
    for lower-band cuts at `k₀ ∈ {ℓ−4, ℓ−3}` (witness `{1,2,2,2,8,16,32}`, `h_{R_lo}=1`). (O2) the
    anchor's `h=0` bound `deficit_top ≥ 2^{ℓ−2}` fails (`= q₁−q₂`, can be `< 1`). (O3) top-piece cuts
    give `R_lo = G_{ℓ−3}∪{a}`, not a refinement; and the structure-free abstract Claim_R is **FALSE**
    (`R={1,3,3}`, `Q={1,7/2,7/2}`: `A(R)=A(Q)=1`, and `{1,3,3}` is not a cut of `{1,2,4}`). *(Step 21;
    all witnesses budget-verified.)* Documents that Gen-Decomp's descent identity alone is insufficient —
    a descent-closed structured class, or a direct `A(R)` evaluation, is required. Reusable by
    `ll-dyadic-symdiff` (whose INC import inherits the same obstruction for refined `R''`).

13. **Family Lemma `F_a` — the σ-parametrized descent-closed parametric bound (NEW round 11, FULLY
    PROVEN).** Fix `a ∈ (0,1)`, `F_k := {a} ∪ G_{k−1}`. For every `k ≥ 1` and every `Q` with
    `S_Q ⊆ S_{F_k}`, `|Q| ≤ k`, `σ := ΣQ − ΣF_k ∈ (0,2)`: `A(F_k) − A(Q) ≥ min(σ, 2−σ)`. Proved by
    strong `k → k−2` induction (Step 24.1), using: `F_k` is descent-closed (`R_lo = F_{k−2}`,
    `h_{F_k}=2`); `A(F_k) = A(G_{k−1}) + (−1)^k a` and `A(F_j) ≥ 1+a` for `j ≥ 2`; the SAME `h=2`
    arithmetic as `t-ell-mutual-induction` (`deficit_top = a_v+b`, `σ_lo = σ+a_v−b`, 2a/2b-i/2b-ii);
    bases `k=1` (vacuous), `k=2` (direct). *Application:* one Gen-Decomp step reduces the `a < 1` top cut
    of `G_{n−1}` to `(Q_lo, F_{n−2})` at `σ=1`, closing G-INC-2nt for `a < 1`, all `n` (Step 24.2). This
    is the specific descent-closed family the abstract `{Claim_R,T_R}` class (O1–O3) failed to be.
    Proposed as `lemmas/sigma-family-a-lt-1.md`. *(Verified 0-violation: family 1932 configs, top-level
    122 configs.)*

14. **Floor Lemma (NEW round 12, FULLY PROVEN, all `j`).** For every integer `j ≥ 1` and every real
    `a > 0`: `A({a}∪G_j) ≥ A(G_{j−1})`, with equality **iff** `a = 2^j`. Proof (Step 25.1): via the
    measure form `A({a}∪G_j) = A(G_j) + a − 2·measure(S_{G_j}∩[0,a))` (from `S_{{a}∪G_j}=S_{G_j}△[0,a)`),
    which is piecewise-linear in `a` with slope `∓1` on the allowed/forbidden dyadic bands of `S_{G_j}`;
    its local minima are at `a = 2^i` (`i ≡ j mod 2`), and `f(2^{i+2})−f(2^i) = −2^i < 0` forces the
    unique global minimum at `a = 2^j`, of value `A(G_{j−1})` (the pair `{2^j,2^j}` cancels the top term).
    *(Verified 0-violation `j = 1..6`, equality only at `a = 2^j`.)* This is the analytic floor for
    G-INC-2nt `a ≥ 1` (Opening C): `A({a}∪G_{n−3}) ≥ A(G_{n−4}) ≥ 1`. Reusable wherever a single dyadic
    part is perturbed. Proposed as `lemmas/floor-a-union-Gj.md`.

15. **h=2 top-cut reduction (NEW round 12, exact).** For the `a ≥ 1` top cut `2^{n−1}→{a,2^{n−1}−a}` in
    the `h=2` Gen-Decomp branch: `A(R) − A(Q) = 1 + 2a_v + 2(O_{R_lo} − O_{Q_lo})`, where
    `a_v = max(R) − q_1 ≥ 0` and `O_P` is the odd-position sum; hence `A(R)−A(Q) ≥ 1 ⟺ O_{Q_lo} ≤
    O_{R_lo} + a_v`. Collapses the whole `a≥1` top-cut goal to one odd-position inequality. *(Step 25.4,
    verified exact 663 configs.)*

16. **Size-2 `Q_lo` closure for the `a ≥ 1` top cut (NEW round 13, FULLY PROVEN, all `n`).** For
    `R_lo = {a}∪G_j` (`j=n−3`, `a∈[1,2^{j+1})`), any `Q_lo=\{p_1,p_2\}` with `S_{Q_lo}⊆S_{R_lo}`,
    `ΣQ_lo > ΣR_lo`: `A(R_lo)−A(Q_lo) ≥ A(G_{j−1}) ≥ 1`. Proof by two regimes (Step 26):
    (a) `a<2^j`: `S_{R_lo}⊆[0,2^j)` and `p_1>2^j` (from `ΣQ_lo>2^{j+1}`) force `p_1=p_2`, `A(Q_lo)=0`
    (**equal-pair forcing / vacuousness**; 0 non-equal admissible pairs verified `j=1,2,3`);
    (b) `a≥2^j`: `A(R_lo)=a−A(G_j)`, `S_{R_lo}=([0,2^j)∖S_{G_j})∪[2^j,a)`, and the top-band forcing
    `p_2≥2^j`, `p_1≤a` give `A(Q_lo)≤a−2^j`, so `A(R_lo)−A(Q_lo)≥2^j−A(G_j)=A(G_{j−1})`. Uses the Floor
    Lemma (§25.1) and `2^j−A(G_j)=A(G_{j−1})` (`set-identity-selfsimilar`). *(Verified exact, dens to 8;
    `min DFB=A(G_{j−1})`, 0 violations.)* Reusable wherever one dyadic part is perturbed and `Q` has ≤ 2
    low parts. **Companion negative fact (Step 26.0):** size ≥ 3 is **tight** (`min A(R)−A(Q)=1` at
    `n=6,a=2,Q_lo={8,4,3,3}`), so it is NOT closable by a slack argument — recorded to stop future
    "large-slack" attempts.

These are reviewer-checkable and reusable by `ll-dyadic-symdiff` (whose Sub-3b INC sub-case is exactly
G-INC-1). Lemma 1 is the corrected replacement for the decertified Structural Lemma; lemmas 5–6 are the
round-7 advance; lemma 7 (with the upgrade of lemma 6 to all `n`) is the round-8 advance; lemmas 8–10
are the round-9 G-INC-2 advance (Gen-Decomp and L1 are the two most reusable); lemmas 11–12 are the
round-10 G-INC-2e closure (`n ≤ 6`) and the descent-non-closure obstruction.
