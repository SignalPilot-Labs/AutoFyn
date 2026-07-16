# Proof-reviewer — imo-2026-03 (IMO 2026 P3), Round 10

Three rival approaches built this round. All three honest `partial`; two delivered
reviewer-certified advances, one delivered a rigorous negative result. No solve.
Overall problem Status: **partial** (headline: **n = 3 upper bound now rigorous**).

---

## 1. geometric-selfsimilar — Lemma T4 = (T) at m = 4

**Verdict: CHANGES REQUESTED. True Status: partial (genuine advance).** Builder-recorded
Status `partial` is correct — no overclaim.

**Load-bearing new claim:** (T) at m=4 — for four distinct pieces `p₁>p₂>p₃>p₄` in the residual
gap region (`p₁ ≤ Σ/2`, `p₂ < 4Σ/15`), Xiang Yu has a legal ≤3-cut strategy forcing
`A ≤ Σ/15`, i.e. `μ(X,3) ≤ Σ/15`.

**Re-derivation (from scratch, reviewer):** I re-derived the entire four-strategy case split
independently and it is **correct**:
- Strategies R/S/P/C each do two Lemma-R1 pairing cuts to two effective pieces `{u,v}` plus
  parity-invisible equal pairs, then a third (halving) cut ⟹ `A ≤ min(u−v, v)`. I verified the
  effective-piece multisets by explicit absolute cut construction and confirmed the R1
  invisibility (equal pairs are adjacent in sorted order, contribute 0, preserve parity).
  Budget = 3, all cuts strictly interior/legal. Bounds R:`d₂`, S:`|d₁−d₃|` and `d₃`, P:`δ/2`,
  C:`δ+d₃−d₁` all confirmed.
- Cases 1–3 (some `d₂`/`d₃`/`|d₁−d₃| ≤ t`) discharged by R/S. Case 4 is the exact complement, so
  1–4 exhaustive. Sub-case B (`d₃>d₁`) vacuous: I reproduced (X) `10t<δ+d₁` from (2′) and (Y)
  `δ+d₁<2t` from (2), chaining to `8t<0`. Sub-case A: `δ<2t` (Z) then P⟹`δ/2<t`, C⟹
  `δ−(d₁−d₃)<2t−t=t`. Every inequality checks. (2′) `7d₂+3d₃<δ+4d₁` re-derived from `p₂<4Σ/15`.

**Independent true-game check:** a richer XY search (all 3-cut sequences with structured
half-integer offsets — a superset of the four strategies) over the integer gap region gives
**0 violations** of `μ(X,3) ≤ Σ/15` (worst ratio 0.88 at {8,4,3,2}). This validates the actual
game quantity, not just the strategy arithmetic.

**Consequence (given prior certified framework R1/R2/R3 + AB.1 + R4.1 + Case A.A):** the whole
**n = 3 upper bound is rigorous** — `val ≤ 8/15 = c(3)`. Previously only n ≤ 2.

**Still open / gap:** (a) `m ≥ 5` general-n upper bound (honestly marked open — the m=4 proof is
algebraic and suggestive but the generalized Sub-case-B impossibility + P/C-chain are unproven;
forbidden dead routes correctly listed); (b) the **n=3 LOWER bound is still gated on the shared LL
t≥2 gap** owned by the LL slugs — so n=3 is NOT fully solved. Correctly stated by the builder.

**Certified:** Lemma T4 → `lemmas/T4-tight-m4.md`.

**Scores:** Correctness 10/10 · Rigor 10/10 · Progress: high (flips n=3 UB partial→rigorous).

---

## 2. ll-dyadic-symdiff — Lemma D1 (small-discrepancy kill)

**Verdict: CHANGES REQUESTED. True Status: partial (genuine advance).** Builder-recorded
Status `partial` correct.

**Load-bearing new claim (Lemma D1):** if `|N_Q(x)−N_R(x)| ≤ 1` for all x, then
`A(Q∪R) ≥ |ΣQ−ΣR|`.

**Re-derivation (reviewer):** correct and clean. `A(Q∪R) = measure{N_Q+N_R odd}` (Lemma M0);
since `N_Q+N_R ≡ N_Q−N_R (mod 2)`, this `= measure{g odd}` with `g=N_Q−N_R`. Under `|g|≤1`,
`g` odd ⟺ `g≠0` and `|g|=𝟙[g≠0]`, so `A = measure{g≠0} = ∫|g| ≥ |∫g| = |ΣQ−ΣR|` (triangle
inequality + `∫N_P = ΣP`). Verified numerically over **47114** configs with `|g|≤1`, 0 failures.

**Still open / gap:** D1 requires the pointwise `|g|≤1` hypothesis; the general **Opening-D
accumulation** `Σδ_k ≥ 1` over even-`|g|` excursions (the real bucket-(iii) GAP crux) and a small
non-tight residual (n=4: 39 configs, all `A≥2`) remain OPEN. INC sub-instances remain conditional
on ll-inclusion-gap's `{Claim_R,T_R}` — which was **refuted this round** (see #3), so that import is
NOT valid support; the INC branch of bucket (iii) is not closed.

**Certified:** Lemma D1 → `lemmas/D1-small-discrepancy-kill.md`.

**Scores:** Correctness 10/10 · Rigor 10/10 · Progress: moderate (reusable general-n GAP tool;
covers most cheap cases, crux still open).

---

## 3. ll-inclusion-gap — refined-R descent obstruction (negative result)

**Verdict: CHANGES REQUESTED. True Status: partial (negative advance + edge closure).**
Builder-recorded Status `partial` correct.

**What was built:** an attempt at the refined-R `{Claim_R, T_R}` mutual induction that the R10
outline asked to revive, which the builder rigorously shows **cannot close G-INC-2**:
- **O1** the refined-R class is not `n→n−2` descent-closed — `h_{R_lo}` parity breaks for lower-band
  cuts (witness `{1,2,2,2,8,16,32}`: `h_R=2` even, `h_{R_lo}=1` odd), refuting the explorers'
  "h_{R_lo}=2 always." **O2/O3** the anchor `h=0` bound and structure-free abstract Claim_R fail.
- Positive: **G-INC-2e** (equal-split thin edge) closed for `n ≤ 6` via a clean vacuousness
  arithmetic `2^{m−2}(9−m) ≥ 2^m ⟺ m ≤ 5` (this final step I verified; the ΣQ_lo→q₁+q₂ bound sits
  inside the deep INC framework and I did not independently re-derive it — I therefore did **not**
  formally certify it as a lemma this round).

**Assessment:** the negative result is the honest core and is valuable — it kills a route every
future round would otherwise retry, and it corrects an overclaim carried in the R10 outline/explorer
reports. But the approach's target **G-INC-2 (refined R) + G-GAP remain OPEN**; the specific
mutual-induction sub-route is dead. This is real progress (search-narrowing + edge closure), not a
solve, and not a fatal break of the whole INC approach (the anchor `R=G_{n−1}` INC branch stays
certified from R8). **Outliner action:** redirect to a direct `A(R)`-per-cut-type attack on
G-INC-2nt; treat `{Claim_R,T_R}` revival as CLOSED-negative (do not re-dispatch).

**Not certified:** #11 (G-INC-2e vacuousness) — final arithmetic sound but the interior ΣQ_lo bound
not independently re-derived in budget; #12 (descent non-closure) — a negative documentation note,
not a reusable positive lemma. Both recorded as partial progress, not lemmas.

**Scores:** Correctness 9/10 (negative result rigorous; interior edge-closure step not
fully re-verified) · Rigor 9/10 · Progress: low-moderate (narrows the search, one edge closed).

---

## Cross-approach dependency note
ll-dyadic-symdiff's INC branch imports `{Claim_R, T_R}` from ll-inclusion-gap. That import was
**refuted this round** (O1). So the INC part of ll-dyadic-symdiff bucket (iii) is NOT supported —
it remains conditional/open, as the dyadic-symdiff builder honestly flagged ("NOT claimed closed").

---

## Goal Progress (for Eval History)
- **Status: partial** (unchanged label; substantive movement).
- **Moved this round:**
  - **n = 3 UPPER bound flipped partial → RIGOROUS** (Lemma T4, geometric-selfsimilar). Answer
    c(3)=8/15 upper half proven. Both-bounds full proof still only n ≤ 2 (lower bound gated on LL).
  - **Lemma D1 certified** — first rigorous general-n GAP cheap-kill (ll-dyadic-symdiff).
  - **Refined-R `{Claim_R,T_R}` route proven DEAD** (ll-inclusion-gap O1–O3) — a shared sub-target
    eliminated; G-INC-2 needs a new direct-A(R) attack.
- **Still open (load-bearing):** (i) general-n upper bound `m ≥ 5` (geometric-selfsimilar);
  (ii) lower-bound LL t≥2 / G-INC-2 refined R + G-GAP non-containment / Opening-D accumulation
  (all three LB slugs). Problem NOT solved.
- **Ranking:** leader geometric-selfsimilar (Elo 1709, advanced), ll-inclusion-gap (1626, partial),
  ll-dyadic-symdiff (1508, advanced).
