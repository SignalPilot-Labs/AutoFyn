# imo-2026-03 — tracking (reviewer-owned)

## Status
partial

## Answer (conjectured; UPPER bound proven n ≤ 3, full both-bounds proof n ≤ 2)
c(n) = 2^n / (2^{n+1} − 1). Verified correct: n=1 → 2/3 (grid optimum 0.668 at a≈1/3), n=2 → 4/7
(grid optimum 0.5714 at geometric config {1,2,4}/7, no config beats it). Independently re-derived by
the reviewer.

## Approaches tried
- **geometric-selfsimilar** (partial, advanced R3) — Lemma G reduction + geometric config +
  self-similar induction. Proven through R3: Lemma G, measure form of A, merge lemma, lower-bound base
  n=1 and Case 1, the tight value c(n), the full n=1 upper bound. **NEW R3 (reviewer-verified):**
  (i) **Lemma LL sub-case t=1** (single cut of 2^n) — interval-overlap bound B ≤ (max(R)−q)^+ cancels
  A(Q) down to A(R) ≥ 1; certified `lemmas/ll-t1-single-cut.md`. (ii) **Upper bound Regime A**
  (1/2 ≤ A_1 ≤ c(n)): shadow strategy forces val = A_1 ≤ c(n); certified `lemmas/shadow-regime-A.md`.
  (iii) **n=2 lower bound now rigorous** (t=2 casework s_0+s_2 ≥ s_1 verified). Remaining gaps:
  **Lemma LL t ≥ 2, A(Q) > 0** and upper-bound **Regimes B (A_1 < 1/2) and C (A_1 > c(n))**.
- **alternating-sum-value** (partial, advanced R3) — same reduction via LB = (1+A)/2, integral rep
  A = measure{x : N(x) odd}. Proven through R3: Lemma G, reformulation, integral rep, A-bounds,
  lower-bound Case 1, tightness. **NEW R3 (reviewer-verified):** Lemma LL-1 (= LL t=1, same as above),
  and **Lemma P** (odd piece count + all pieces ≥ 1 ⇒ A ≥ 1; certified `lemmas/parity-piece-count.md`,
  restricted family). Recorded dead-end: potential-decrease greedy XY does not reach A ≤ 1/D (stalls;
  needs lookahead). Remaining gaps: **GAP AL** (= LL t ≥ 2 residual) and **GAP AU** (universal upper).
- **extremal-smoothing** (partial, built R3) — maximin/extremal route to the UPPER bound, bypassing any
  per-config XY strategy. **NEW R3 (reviewer-verified):** Props 1–2 (V continuous on compact Δ, max
  attained by Weierstrass) and Prop 4 (replica bound V(G_n) ≤ c(n)) rigorous; Prop 3 reduction
  **upper bound ⟸ S1 + replica, independent of LL** is a valid logical implication. Certified
  `lemmas/extremal-framework.md`. Remaining gaps: **S1** (G_n is the unique maximizer / smoothing
  monotonicity — the load-bearing open bet) and **LL** (imported lower-bound gap).
- **ll-dyadic-symdiff** (partial, NEW R5; advanced R6) — rival lower-bound attempt on LL t≥2 via a
  three-way split on `measure(S_Q △ S_R)`, avoiding the merge a/b and peel-one-cut dead-ends. **R5:**
  Case 1 (`max(Q) ≥ 2^{n−1}+1`) closed (certified `lemmas/ll-case1-high-interval.md`); Case 2 (odd count,
  all pieces ≥ 1) closed via Lemma P; Sub-3a (some full dyadic level fully odd) closed (certified
  `lemmas/dyadic-level-parity.md`). **NEW R6 (reviewer-verified):** proved the **General reflection
  identity (Lemma REFL)** `A(Q∪R) = max(Q) − A(Q'∪R)` for `max(Q) ≥ 2^{n−1}` (rigorous set-theory proof,
  reviewer re-derived + verified 2282/2282 0 mismatches; certified `lemmas/ll-reflection-identity.md`).
  This collapses branches B1 (`2^{n−1}<max(Q)<2^{n−1}+1`) and B2 (`max(Q)=2^{n−1}`) of Sub-3b to the
  single upper-bound inequality **GAP-A** `A(Q'∪R) ≤ max(Q)−1`. **Deleted the FALSE R5 outline step**
  "`max(Q)<2^{n−1} ⟹ A ≥ 2`" (reviewer counterexample `Q={15/4,13/4,1}` gives A=3/2; sharper witness
  `Q={3,3,2}`, `R={2,2,2,1}` gives A=1 exactly — B3 is tight, no slack). Open: **GAP-A** (=G-INC-1) and
  **GAP-B** (`max(Q)<2^{n−1}`, tight). Honest partial.
- **ll-inclusion-gap** (partial, NEW R5; revised R6) — rival lower-bound attempt on LL t≥2 via the
  inclusion split `S_Q ⊆ S_R`. **R5:** Forcing Lemma + INC reduction (`A(Q∪R)=A(R)−A(Q)`), certified
  `lemmas/forcing-inc-reduction.md`; INC sub-case `max(Q)≤2^{n−2}`; GAP-branch Case-1. R5 flaw: the
  "Structural Lemma" part (a) was FALSE (counterexample `Q={3/2,3/2,2,3}`), leaving the n=3 base case
  incomplete. **NEW R6 (reviewer-verified), both outline corrections obeyed:** (i) replaced the false
  Structural Lemma with the **Parity-Condition Lemma** (`S_Q⊆S_R ⟹ N_Q even wherever N_R even`; general n,
  rigorous; certified `lemmas/parity-condition-inc.md`) — TRUE, admits even-multiplicity interior pairs.
  (ii) **Complete, correct n=3 INC base case for R=G_2** (all sub-cases incl. the even-multiplicity
  interior pair `{s,s}⊂(1,2)`): `A(Q) ≤ 2 = A(G_2)−1`, reviewer re-verified the casework + 0 violations
  over 52 INC configs. (iii) **Top-band decomposition identity** (general n, R=G_{n−1}): with `h` even,
  `A(G_{n−1})−A(Q) = deficit_top + M`, both ≥0 (certified `lemmas/top-band-decomposition.md`), reducing
  the general "+1" to the scalar inequality **G-INC-1** `deficit_top+M ≥ 1`. Open: **G-INC-1** (=GAP-A),
  **G-INC-2** (refined R general n — the n=3 INC branch is proven ONLY for R=G_2; refined R at n=3 is
  only numerically checked, NOT proven), **G-GAP** (non-containment alignment cost). Honest partial.
- **geometric-selfsimilar** (partial, advanced R6) — leader; upper-bound route. **NEW R6
  (reviewer-verified):** a **unified sum-bound reframe** `μ(X,b) ≤ Σ/(2^{b+1}−1)` (SB) folding Regimes
  A/B/C into one target, plus three rigorous **reduction lemmas R1/R2/R3** (free-pair removal, halving,
  pairing; certified `lemmas/sum-bound-reductions.md`; reviewer verified equal-pair invisibility, R3
  leftover identity for q<p₁, and R2/R3 arithmetic, all 0 failures). Regime C now has a **rigorous
  opening cut** (R2 halves A₁), superseding the unproven "dominant-chop". Collapses old gaps
  B2-general + C into a SINGLE residual **gap case** (distinct X, `p₁<τ`, `p₂<τ/2`). Recorded dead-end:
  partial-shadow does NOT preserve the sum invariant (`Σ(R′)/D_{b−j} ≤ Σ/D_b` fails 18/123/315/678 at
  n=3..6), so the naive sum induction cannot pass the gap — a stronger potential is needed. Open: the
  gap case (the full upper bound). Honest partial.

## Current best
The whole game is **rigorously reduced** (Lemma G, certified) to a one-parameter quantity: with the
final sorted pieces p_1 ≥ … ≥ p_k, Liu Bang's optimal share is exactly Σ_odd = val(P) = (1 + A(P))/2,
A the alternating sum. So c(n) = max_{LB} min_{XY} val, in unnormalized units (×D, D = 2^{n+1}−1) the
target is val ≥ 2^n on the lower side and ≤ 2^n on the upper side.

Established and reviewer-verified:
- **Lemma G** (greedy/odd-index) — certified in `lemmas/greedy-odd-index.md`.
- **Integral rep of A, A-bounds, merge lemma, single-cut effect** — certified in
  `lemmas/alt-sum-integral.md`.
- **Answer c(n)** — correct (verified n=1, n=2 by full-game optimization).
- **Lower bound Case 1** (XY spares the largest geometric piece 2^n): val ≥ 2^n. Complete.
- **Tightness / replica bound** V(G_n) ≤ c(n): XY's midpoint-halving forces val = exactly 2^n. Complete
  (certified `lemmas/extremal-framework.md`).
- **Full n=1 upper bound** (geometric-selfsimilar): XY holds every LB config to ≤ 2/3. Complete.
- **n=1 and n=2 lower bounds fully rigorous** (R3): c(1) ≥ 2/3, c(2) ≥ 4/7 both proven (all cases).
- **Lower bound Lemma LL sub-case t=1** (single cut of 2^n): A(Q ∪ R) ≥ 1. Complete, certified
  `lemmas/ll-t1-single-cut.md`. Reviewer-verified (0 violations, 5000 configs).
- **Upper bound Regime A** (1/2 ≤ A_1 ≤ c(n)): shadow strategy ⇒ val = A_1 ≤ c(n). Complete, certified
  `lemmas/shadow-regime-A.md`. Reviewer-verified (val = A_1 exactly, 301 configs).
- **Upper bound Regime B sub-case B1** (1 − c(n) ≤ A_1 < 1/2), **general n**: partial-shadow prefix ⇒
  val ≤ 1 − A_1 ≤ c(n). Complete, certified `lemmas/partial-shadow-B1.md`. Reviewer re-derived the chain
  and re-verified (0 violations / 17961 flat configs). **Regime B fully closed at n = 2** (B1 + B2a + B2b,
  exhaustive; reviewer-checked the ε-cancellation identity val = A_1 + A_3/2 and the case split).
- **Extremal framework**: V continuous on compact Δ, max attained; upper bound reduced to S1 alone,
  LL-independent. Complete, certified `lemmas/extremal-framework.md`.

## R13 progress (reviewer-verified)
- **geometric-selfsimilar — Lemma HS-A2 CERTIFIED** (`lemmas/HS-A2.md`): in the m=5 pure hard case with
  `δ>2t`, the **Sub-A-P** branch closes — `pair2_3` (cut `p₂@p₃`, R1) leaves `Y″={p₁,d₂,p₄,δ}` at budget 3
  with `min A(Y″,3) ≤ t`. Reviewer re-derived the Σ-P bound [*] `2d₂≤31t−7δ−6d₄−4d₃` and all 6 case
  bounds (A/B1/B2/C1/C2/C3) by hand, and independently confirmed the CONCLUSION `min A(Y″,3)≤t` via an
  achievable-strategy (matching/halving) search over off-grid Fractions covering every live case (A, B1,
  B2, C1, C2; worst achievable = 1.0·t, 0 violations; C3 vacuous). The builder's **C2 CORRECTION is
  verified**: the outline's "P fires, `A_P≤d₂/2`" is FALSE; the correct closure is the custom halve-`p₁`
  strategy giving `A≤|d₄−d₂|<t` (both `d₂,d₄∈(t,2t)`). **NO OVERCLAIM:** T5 (m=5 UB) and the n=4 UB are
  NOT proven — the pair1_2 success region (Sub-A-C, Sub-B, all `δ≤2t`; gap G1, ~40k configs, numerics
  only) is OPEN, and m≥6 (G3/HS-A3) is untouched. The step tree is NOT uniform in m.
- **ll-inclusion-gap — Lemma size2-Qlo-closure CERTIFIED** (`lemmas/size2-Qlo-closure.md`): for the `a≥1`
  `h=2` top cut, the **size-2 `Q_lo`** case closes for EVERY `n` and every `a∈[1,2^{n−2})` (upgrading the
  R12 pinch `n∈{4,5}`): `A(R_lo)−A(Q_lo)≥A(G_{j−1})≥1` (`j=n−3`), via Regime A (`a<2^j`: `p₁=p₂` forced,
  Floor Lemma) and Regime B (`a≥2^j`: `p₂≥2^j` parity forcing + `p₁≤a` ⟹ `A(Q_lo)≤a−2^j`). Reviewer
  re-derived both regimes by hand + verified 0 violations over 18386 off-grid configs (`a≥1`, dens 8).
  **KEY NEGATIVE FINDING verified**: the "large slack for size≥3" premise is FALSE — the size-4 witness
  `n=6, a=2, R={1,2,4,8,16,2,30}, Q={30,16,8,4,3,3}` gives `A(R)−A(Q)=1` EXACTLY (reviewer reproduced:
  A(R)=19, A(Q)=18, INC holds), so the distinct-top `|Q_lo|≥3` crux is genuinely tight (same tier as the
  anchor's mutual induction). Corrected target `DFB≥1−deficit_top`. No revival of the refuted
  `T'(j)`/`{Claim_R,T_R}` mutual induction. Open: distinct-top `|Q_lo|≥3`, refined multi-cut R, G-GAP.
- **ll-dyadic-symdiff — Lemma BR CERTIFIED** (`lemmas/BR-bottom-restriction.md`): a genuine
  `max|g|`-agnostic BYPASS. `A(Q∪R) ≥ measure{x∈[0,τ):g odd}` (one-line measure monotonicity); with
  `τ=min(Q)`, `A(Q∪R) ≥ B=measure{x∈[0,min(Q)):N_R(x)≢|Q| mod 2}`. Reviewer confirms it routes through
  neither the alternating-tail crux nor Sub-3a nor any `max|g|` bound — a real bypass. For the **Q-top**
  slice (`min(Q)≥2^{n−2}`), reviewer verified the reduction: `|Q|∈{3,4}`, and the within-bottom parity
  identity eliminates `Q`, reducing `A(Q∪R)≥1` to the R-only inequality (★R) `|Q|=4⟹A_R^{bot}≥1`,
  `|Q|=3⟹A_R^{bot}≤2^{n−2}−1` (verified tight, 0 violations n=3,4,5, but **NOT proved** — honest open).
  The builder correctly notes the n=3 sub-case was closed in R9 and is NOT presented as new progress; the
  non-Q-top residual (`min(Q)<2^{n−2}`) is NOT covered. No overclaim.

## R12 progress (reviewer-verified)
- **geometric-selfsimilar — no new lemma; rigorous methodological negative.** T5 (m=5 hard case) still
  OPEN; HS-A2 (`δ>2t ⟹ pair2_3 gives A≤t`) unproven — the explorer Σ-bound only yields `d₂<3.5t`, not
  `<2t`. KEY FINDING (reviewer-endorsed): the R8/R10-style "0 integer-grid violations" evidence is a GRID
  ARTIFACT — the single-cut `pair1_2` reduction FAILS off-grid (witness `X={157/5,13,46/5,34/5,23/5}`,
  `δ>2t` region, `min A(Y′,3)=1.049t>t`), so `pair2_3` fallback is genuinely required. **New standing rule:
  all UB numeric checks must use off-grid exact-Fraction configs.** Status unchanged (n≤3 UB rigorous).
- **ll-inclusion-gap — Floor Lemma CERTIFIED** (`lemmas/floor-a-union-Gj.md`): `A({a}∪G_j) ≥ A(G_{j−1})`,
  equality iff `a=2^j` (measure form `S_W=S_{G_j}△[0,a)`, band-slope count; reviewer re-derived + verified
  `j=1..6`). NEW exact **h=2 reduction** `A(R)−A(Q)=1+2a_v+2(O_{R_lo}−O_{Q_lo})` collapses the `a≥1` top-cut
  goal to the single odd-position inequality **(★) `O_{Q_lo}≤O_{R_lo}+a_v`**. CLOSED: `h≥4`, `h=0`
  (`a≤2^{n−2}−1`), fully-tight config `a=2^{n−3}` (forcing `A(Q_lo)=0`, pinch `n∈{4,5}`). **HONEST OPEN
  crux (DFB / (★)) for general `h=2, a≥1`** — the family `{a}∪G_{n−3}` is NOT descent-closed for `a≥1` (O1
  fires), so a DIRECT `A(R_lo)` proof is needed; the refuted `{Claim_R,T_R}` mutual induction is not revived.
- **ll-dyadic-symdiff — Lemma G1 + Foundation F-neg CERTIFIED** (`lemmas/G1-one-sided-kill.md`,
  `lemmas/F-neg-boundary-parity.md`). Dropped the R11 target `B₊≤A₋+B₋` (confirmed circular, `⟺ A≥1`).
  Re-framed crux as the **Sub-3a dichotomy**; `Sub-3a` fires `⟹ A≥1` (certified). **G1** (`max g≤1 ⟹
  A≥ΣQ−ΣR=1`, strictly stronger than D1 on the `g≤1` side) closes the whole `max g≤1` slice, all `n`.
  **F-neg** (`g(0⁺)=c_Q−c_R−(n−1)≤−1`) established. **HS-D3 agnosticism** confirmed (route uses no
  `max|g|≤2`). **HONEST OPEN crux HS-D1** (`Sub-3a fails ∧ max g≥2`): reviewer-verified OBSTRUCTION shows
  F-neg+parity alone insufficient (profile `g=(−1,+2,0)`, `∫g=1`, `A=ε<1`) — needs the `ΣQ=2^n` staircase
  geometry, honestly open. The explorer's budget-parity (`R` has an odd-mult piece) is flagged non-rigorous
  (a cut can change the odd-mult count by −3), used only for `A>0`, not load-bearing.

## R11 progress (reviewer-verified)
- **geometric-selfsimilar — Lemma MK CERTIFIED** (`lemmas/MK.md`): `μ(X,|X|−1) ≤ min(X)` (midpoint-halve
  the largest into an invisible pair, recurse; bases k=1,2). Corollary MK.1 (`δ≤t` or some `d_j≤t` ⟹
  `μ(X,m−1)≤t`, tight budget, uniform in m) is the uniform easy-case tool T4 lacked. This yields a
  **complete exhaustive reduction of the ENTIRE remaining upper bound to ONE pure hard case (c)** for all
  m: `(a) p₁>Σ/2` [Case A.A at threshold, CLOSED], `(b) p₁≤Σ/2 & (δ≤t or ∃d_j≤t)` [MK.1, CLOSED],
  `(c) p₁≤Σ/2, all d_j>t, δ>t` [hard; closed m≤4, open m≥5]. Reviewer re-derived MK, MK.1, Case A.A-at-t
  (`A=2q₁−Σ<t`) and re-verified 0 violations. **NEGATIVE result (correct, not a builder error):** the
  outliner's threshold-invariant induction is REFUTED — after the universal `p₁@p₂` move the subproblem
  `Y'={d₁,p₃,…,p_m}` does NOT inherit gap condition `(2')` (`{(I'),(II'),(III')}` is the wrong invariant;
  (II') inheritance is the false step). Explicit witness `X={8,4,3,2,1}, t=18/31, Y'={4,3,2,1}`: no
  inheritance/easy-escape yet `μ({4,3,2,1},3)=0≤t` (reviewer verified `A({2,2,2,2,1,1})=0`, 2 cuts). So
  m≥5 needs a weaker-recursable invariant or a direct hard-case strategy — the naive route is certified-dead.
- **ll-inclusion-gap — Family Lemma F_a CERTIFIED** (`lemmas/sigma-family-a-lt-1.md`): closes the
  **`a<1` top-cut sub-branch of G-INC-2nt for ALL `n`**, rigorously. The fix is the σ-reference: parametrize
  by `σ:=ΣQ−ΣX` (excess over the object's OWN sum), making top cut `R` and family `F_k={a}∪G_{k−1}` obey the
  identical recursion. `F_a`: `A(F_k)−A(Q)≥min(σ,2−σ)` for `S_Q⊆S_{F_k}, |Q|≤k, σ∈(0,2)`, via strong
  `k→k−2` induction (same arithmetic as certified `t-ell-mutual-induction`, tent peaks `≥1` at `σ=1`).
  Reviewer re-derived `A(F_k)=A(G_{k−1})+(−1)^k a`, every induction case (h=0/h≥4/h=2 2a/2b-i/2b-ii; 2a uses
  `A(Q_lo)≤A(F_{k−2})` from S-containment), confirmed **genuine descent-closedness** (parts ≥2^{k−2} are
  exactly `{2^{k−1},2^{k−2}}`, `h=2` every level — the R10 O1 break provably cannot fire; the O1 witness
  `{1,2,2,2,8,16,32}` and Claim-false `{1,3,3}` are NOT in this family). Verified 0 violations on the family
  bound and the top-level closure (124 configs, n=3,4). Opening B (h=0) and Opening D (cut value `<1`) also
  closed. **Honest residual OPEN:** G-INC-2nt `a≥1` (family loses descent-closure — once `a≥2^{k−4}` the count
  goes odd; needs a direct `A(R)` evaluation), G-INC-2lb terminal cut `≥1`, G-INC-2e⁺ (m≥6), G-GAP.
- **ll-dyadic-symdiff — rigorous NEGATIVE correction + level-charge reduction** (promotable lemmas in the
  approach file, both reviewer-verified): the outline's "INC forces `max(Q)≤max(R)`" is **FALSE**
  (machine + reviewer-checked counterexample `Q={15/2,15/2,1}, R={7,4,2,1,1}` at n=4: `S_Q=[0,1)⊆[0,2)∪[4,7)=S_R`
  INC holds, yet `max(Q)=15/2>7=max(R)` — `max(Q)` has even multiplicity; **within joint budget**
  `c_Q+c_R=2+1=3≤4`, R being G₃ with `8→7+1`). Corrected lemma **PROVED**: INC ⟹ `max(Q)≤max(R)` OR
  `max(Q)` even multiplicity (clean point-parity argument). So the intended non-inductive INC closure and
  the `(r−q)`-slack identity collapse. Kept: **D1-direct** (ordering-free, `max|g|≤1` slice, all n) and the
  **level-charge reduction** `A(Q∪R)=1+2(A₋+B₋−B₊)` (`A_±=measure{g=±1}, B_±=measure{g=±2}`), hence
  `A≥1 ⟺ B₊≤A₋+B₋` for `max|g|≤2`. Reviewer re-derived the algebra + verified on the counterexample
  (`A₋=1,B₋=1,B₊=1/2 ⟹ A=4` ✓). **Honest OPEN crux:** `B₊≤A₋+B₋` (g=+2 excess dominated by g<0 mass; needs a
  wide-support argument from `ΣQ=2^n`, not implied by `∫g=1` alone) + the `max|g|≥3` extension.

## R10 progress (reviewer-verified)
- **geometric-selfsimilar — Lemma T4 = (T) at m=4 CERTIFIED** (`lemmas/T4-tight-m4.md`): the tight-case
  inequality `μ(X,3) ≤ Σ/15` for every four-distinct-piece residual gap case, via a direct four-strategy
  (R/S/P/C) actual-A case split. Reviewer re-derived the whole split from scratch (Cases 1–3 by R/S,
  Case-4 Sub-case B vacuous via (X)&(Y) collision, Sub-case A by δ<2t + P/C) and confirmed with an
  independent true-game half-integer 3-cut search (0 violations, worst ratio 0.88). With the certified
  R1/R2/R3 reduction + Cor R4.1 (m≤3) + Cor AB.1 (m=4,b≥4⟹μ=0) + Case A.A (p₁>Σ/2), **the entire n=3
  UPPER bound is now rigorous: `val ≤ 8/15 = c(3)`.** (Previously only n≤2.) `m ≥ 5` (general-n UB) OPEN.
  The n=3 LOWER bound is still gated on the shared LL gap — n=3 is NOT fully solved.
- **ll-dyadic-symdiff — Lemma D1 CERTIFIED** (`lemmas/D1-small-discrepancy-kill.md`): general-`n`
  small-discrepancy kill — `|N_Q−N_R| ≤ 1` pointwise ⟹ `A(Q∪R) ≥ |ΣQ−ΣR|` (=1 in bucket (iii)). Clean
  measure proof (g odd ⟺ g≠0 ⟹ A = ∫|g| ≥ |∫g|); reviewer re-derived + verified 47114 configs. First
  rigorous general-`n` GAP tool beating the `∫g=1` obstruction. K1/K2/D1 cover most GAP; the general
  Opening-D accumulation `Σδ_k ≥ 1` over even-`|g|` excursions + a small non-tight residual (n=4: 39
  configs, all A≥2) remain OPEN.
- **ll-inclusion-gap — rigorous NEGATIVE result** (not certified as a lemma): the refined-R
  `{Claim_R, T_R}` mutual induction is **obstructed** — the class is not `n→n−2` descent-closed
  (O1: `h_{R_lo}` parity breaks for lower-band cuts, witness `{1,2,2,2,8,16,32}`; O2/O3). Also **G-INC-2e**
  (equal-split thin edge) closed for `n ≤ 6` (vacuousness: `2^{m−2}(9−m) ≥ 2^m ⟺ m ≤ 5`). The clean
  mutual-induction sub-route for refined R is DEAD; G-INC-2 needs a direct `A(R)`-per-cut-type attack.
  No solve; approach stays partial.

## Remaining gaps (load-bearing, still open after R9)

**R9 progress (reviewer-verified, 0 violations, budget-enforced; all 3 approaches honest partial → CHANGES REQUESTED):**
- **geometric-selfsimilar — Lemma AB CERTIFIED** (`lemmas/abundant-budget.md`): `μ(X,b)=0` whenever
  `b ≥ |X|`, via a constructive pairing-reduction (invisible pairs + one midpoint cut). Corollary narrows
  the R8 `m ≥ 4` frontier ("all `b ≥ 3`") to the **single tight budget `b = m−1`**. The tight case reduces
  to a finite merge-family inequality (T), **verified 0/9646 exact m=4 gap configs but NOT analytically
  proven** — the whole remaining upper bound, honestly open (no overclaim). Reviewer confirmed the two
  spec concerns: the outline's single-cut "complement" parity distinction is illusory (Lemma R3), and its
  one-cut m=4→3 mechanism is refuted (R4-on-sub value exceeds target 141/367).
- **ll-inclusion-gap — Gen-Decomp + Lemma L1 CERTIFIED** (`lemmas/gen-decomp-refined.md`,
  `lemmas/L1-budget-anchor.md`): the refined-R top-band engine `A(R)−A(Q)=deficit_top+(A(R_lo)−A(Q_lo))`
  (no SET IDENTITY) and the budget anchor bound `S_P⊆S_{G_{m−1}}, |P|≤m−1 ⟹ A(P)≤A(G_{m−1})−1` (strict
  `−1` from the budget deficit, `m→m−2` induction). Equal-split top cut closed for all `n ≥ 4` except the
  non-near-tight edge `g=0, h̄≥2, q₁>q₂` (G-INC-2e). Open: G-INC-2lb (lower-band cross-position recursion,
  unpinned `ΣQ_lo`), G-INC-2nt (non-equal top cut, `a<1`).
- **ll-dyadic-symdiff — K1/K2/REFL-telescope CERTIFIED** (`lemmas/dyadic-cheap-kills.md`) + **n=3 bucket
  (iii) COMPLETELY CLOSED** (whole `max(Q),max(R)<2^{n−1}` top-cut regime; budget forces `R={4−a,2,a,1}`,
  `|Q|=3`; Lemma Q3 + regime split; min A(Q∪R)=1, 0 violations over 10912 configs, reviewer re-ran).
  REFL-telescope termination proven (well-founded piece-count descent) but honestly only recomputes A —
  the general-n bucket (iii) bottom object is the refined-R alternating-tail crux, open for `n ≥ 4`.

**R8 progress (reviewer-verified):**
- **ll-inclusion-gap — T(ℓ) CLOSED for ALL ℓ, hence G-INC-1 = Claim(n,0) for ALL n** (certified
  `lemmas/t-ell-mutual-induction.md`). The round-7 single-claim induction was upgraded to a **mutual
  strong induction on `{Claim(n,ε), T(n)}`** (Step 12b + 13). Reviewer re-derived the h=2 arithmetic
  (`deficit_top=a+b`, `ε'=ε+a−b` / `a−b−τ`, targets `1+2b+τ≥1−τ`, `1+2a−τ≥1−τ`), verified the 4 bases
  by hand, confirmed NO same-level circularity (each of Claim(n),T(n) uses only level n−2) and NO
  negative-ε Claim call, and checked the STATEMENTS 0-violation (budget enforced) at n=3 (grid 1/8),
  n=4, n=5. The flagged trivially-true `h=0` sub-case of Claim's Step 12 is now written. **This closes
  the INC branch of LL for the anchor `R = G_{n−1}`, every n** (the shared crux `T(ℓ)=GAP-A=B2*`, open
  3+ rounds). Still open for the full lower bound: **G-INC-2** (refined R) and **G-GAP** (non-containment).
- **geometric-selfsimilar — Lemma R4 (gap-case m=3) CLOSED**, so the **n=2 upper bound is now fully
  rigorous** (certified `lemmas/gap-case-m3-closure.md`). XY's single R3 cut of p₁ at p₂ gives
  `A(final)=Σ−2p₁ < Σ/D_b` via `p₁≤Σ/2` and the exact identity `D_b−2(2^b−1)=1`; reviewer re-derived
  and verified 0-violation over 60000 gap configs. With Case A.A (m=2 / p₁>Σ/2), the gap case is closed
  for **all m ≤ 3**. The **m ≥ 4** cascade was REFUTED (the potential Σ−2p₁ ≈ Σ/2 ≫ Σ/D_b; every simple
  deterministic strategy fails) — honestly open, needs lookahead / a genuinely new potential.
- **ll-dyadic-symdiff — refined-R core advanced** (certified `lemmas/ll-general-R-core.md`): Cases
  1/2/Sub-3a proven R-agnostic (any `max(R)≤2^{n−1}`, `A(R)≥1`); budget-reduction lemma (`c_R≥1 ⟹
  |Q|≤n`); double-REFL for refined R with top piece `2^{n−1}` uncut closes B3a-ref/B3b-ref all n. The
  crux residual `(B2*)-ref` (refined-R alternating-tail) and the top-cut bucket remain open (= refined-R
  analogue of the shared crux). No false `max(Q)<2^{n−1}⟹A≥2` re-imported. Honest partial.

**Net: the LB anchor INC branch (R=G_{n−1}) and the n=2 upper bound are both now rigorous for all/at
n. The problem is NOT solved** — the full lower bound still needs G-INC-2 (refined R) + G-GAP
(non-containment), and the upper bound still needs the m≥4 gap case (n≥3). Answer c(n)=2^n/(2^{n+1}−1)
remains conjectured-and-verified-small-n, not fully proven.

### Detailed residual (carried from R7)
1. **Lower bound Lemma LL, t ≥ 2, A(Q) > 0 — shared residual narrowed further (R7).**
   Both LL routes reduce to the SAME alternating-tail crux; R7 PROVED it for small n and isolated a
   cleaner residual.
   - `ll-inclusion-gap` (R7, reviewer-verified): a **two-step strong induction n→n−2** on
     `Claim(n,ε) ⟺ O_Q ≤ O_{G_{n−1}}+ε`, built on the certified generalized (ΣQ-free) top-band
     decomposition + the **SET IDENTITY** `S_{G_{n−1}}∩[0,2^{n−2})=S_{G_{n−3}}` (certified
     `lemmas/set-identity-selfsimilar.md`), PROVES **G-INC-1 = Claim(n,0) unconditionally for
     n ∈ {1,2,3,4}** (reviewer re-verified base cases Claim(1,·),Claim(2,·),T(1),T(2), both identities,
     and the conclusion 0-violation n=3,4). For general n it holds **conditional on the single residual
     lemma T(ℓ), ℓ≥3** (`O_P ≤ O_{G_{ℓ−1}}` for INC P, |P|≤ℓ+1, ΣP∈(2^ℓ−1,2^ℓ); verified 0-viol
     ℓ=3,4). MINOR remaining gap in the general-n step: the case split lists only `h≥4` and `h=2`; the
     `h=0` case IS reachable for n≥5 (reviewer found instances, e.g. n=5 Q={13/2,13/2,6,6,4,3}) — it is
     trivially true (h=0 ⟹ deficit_top=2^{n−2}≥1) but must be written. Does NOT affect n=3,4 (h≥2 there).
   - `ll-dyadic-symdiff` (R7, reviewer-verified): **REFL-gen** (relaxed hyp `max(R)≤μ`, certified
     `lemmas/ll-reflection-identity-gen.md`) + **double-REFL formula** `A(Q∪G_{n−1})=2^{n−1}−q₁+A(Q'∪G_{n−2})`
     close branches **B3a, B3b for all n** and reduce B3c to the single tight residual **(B2*)**
     `A(Q'∪G_{n−2})≥1`, **PROVED at n=3** (exhaustive |Q'|∈{2,3}, reviewer min=1, 0 viol on 1/8 grid).
     General-n B2* = GAP-A = the shared alternating-tail crux, open. Scope: anchor R=G_{n−1} only; refined
     R (min A=3/2) open.
   Remaining shared pieces: **T(ℓ)/GAP-A/(B2*) general n** (the alternating-tail `+1`), **G-INC-2**
   (refined R general n), **G-GAP / GAP-B refined R** (alignment branch). The naive integral bound
   `∫(N_Q−N_R)=1` is provably insufficient.
2. **Upper bound — unified sum-bound gap, R7 shrinks it further (geometric-selfsimilar).** The whole
   upper bound is the single sum-bound `μ(X,b) ≤ Σ/(2^{b+1}−1)` (SB). Regime A (shadow), B1
   (partial-shadow), B fully at n=2 closed; R1/R2/R3 (certified `lemmas/sum-bound-reductions.md`) give
   Regime C a rigorous opening cut and collapse B2-general+C into the **gap case** (distinct X, `p₁<τ`,
   `p₂<τ/2`). **R7 (reviewer-verified):** **Case A.A** (`p₁>Σ/2`) CLOSED via subtract-all chain
   (`A(final)=2p₁−Σ<Σ/D_b`, certified `lemmas/gap-caseAA-subtract-chain.md`); and the **SB-obstruction
   theorem** (`Σ'/D_{b−1}≤Σ/D_b ⟺ q≥τ/2`, certified `lemmas/sb-obstruction.md`) — a correctly-scoped
   NEGATIVE result proving no SB-monotone reduction reaches the residual `p₁≤Σ/2`, so an actual-A
   potential is required. Residual `p₁≤Σ/2` honestly open (numerically μ·D_b≤1/2 throughout, so SB true).
   The extremal-smoothing route reduces the WHOLE upper bound to S1 (G_n unique maximizer),
   LL-independent but stuck 4+ rounds.

(No `## Full proof` — the problem is not solved; both the lower-bound residual (G-INC-1 = GAP-A) and the
upper-bound gap case are load-bearing and open.)
