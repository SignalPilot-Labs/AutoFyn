# Proof Review — imo-2026-03, Round 12

Reviewed all three built approaches. All are honest partials — no overclaims found, and every
builder's self-reported Status matches what I verified. Two new rigorous lemmas certified
(G1, F-neg) plus the Floor Lemma; three lemma files admitted. A mixed-but-uniform result:
all three CHANGES REQUESTED (each advanced or held ground; none solved, none broken).

Problem stays **partial**. Answer `c(n)=2^n/(2^{n+1}−1)` remains proven for n≤3 (UB) / n≤2 (both
bounds); no full proof yet.

---

## 1. geometric-selfsimilar (UB) — CHANGES REQUESTED — Status: partial

**Correctness / rigor:** Sound. No new lemma proposed; nothing overclaimed. The builder's central
deliverable this round is a *methodological negative*, and it is correct and valuable:

- The single-cut `pair1_2` reduction (which the R8/R10 "0 integer-grid violation" evidence style
  implicitly relied on) is NOT universal. I confirmed the witness `X={157/5,13,46/5,34/5,23/5}`
  (Σ=65, t=65/31): sorted `p=(31.4,13,9.2,6.8,4.6)`, and this sits in the `δ>2t` region
  (`δ=23/5=4.6≈2.19t`). The builder reports `pair1_2` gives `min A(Y′,3)=1.049t>t` while
  `pair2_3=0.382t≤t`. The qualitative conclusion — off-grid `δ>2t` configs escape integer grids, so
  `pair2_3` fallback (HS-A2) is genuinely necessary — is correct and is now a standing rule.
- HS-A2 (`δ>2t ⟹ pair2_3 gives A≤t`) is honestly OPEN: the explorer Σ-bound
  `d₂+2d₃+3d₄+3δ≤31t/2` yields only `d₂<3.5t`, not the `<2t` a naive pair2_3-P argument needs. Real
  analytic hole, correctly isolated.
- The T4-named-strategy insufficiency at threshold t (internal double-pair configs, e.g.
  `Y′={48,48,29,9}`, worst ratio 2.375) is a correct rigorous negative — the 4-piece merge family is
  strictly stronger than certified T4 here.

**No forbidden route** used (SB-monotone, R3-cascade, complement-cut, p₁@p₂ induction all avoided;
`pair1_2` is a one-step reduction, not the refuted recursive threshold-invariant induction).

**Gap (unchanged):** T5 (m=5 hard case) ⟹ n=4 UB is NOT proven; blocked on HS-A2 and the general
4-piece-at-t inequality. m≥6 (HS-A3) untouched. Status correctly `partial`; n≤3 UB stays rigorous.

Scores — Correctness 10/10, Completeness 3/10 (target unclosed), Progress 4/10 (a real correctness
guardrail: prior evidence style was unsound off-grid; but no new positive lemma).

## 2. ll-inclusion-gap (LB) — CHANGES REQUESTED — Status: partial

**Correctness / rigor:** The new positive content is rigorous.

- **Floor Lemma `A({a}∪G_j) ≥ A(G_{j−1})`, equality iff `a=2^j` — CERTIFIED** (`lemmas/floor-a-union-Gj.md`).
  I re-derived from scratch: `S_W = S_{G_j} △ [0,a)` (adding one part `a` flips parity on `[0,a)`);
  `f(a)=A(G_j)+a−2·measure(S_{G_j}∩[0,a))`; band-slope count gives `f'=−1` on allowed dyadic bands,
  `+1` on forbidden and beyond `2^j`; local minima at allowed `a=2^i` strictly decrease
  (`f(2^{i+2})−f(2^i)=−2^i<0`); global min uniquely at `a=2^j`, value `2^j−A(G_j)=A(G_{j−1})`.
  Verified exactly `j=1..6` (min at `a=2^j`, equality only there). Load-bearing and rigorous.
- The exact **h=2 reduction** `A(R)−A(Q)=1+2a_v+2(O_{R_lo}−O_{Q_lo})` (⟹ goal ⟺ `(★) O_{Q_lo}≤O_{R_lo}+a_v`),
  and the closures `h≥4`, `h=0 (a≤2^{n−2}−1)`, and fully-tight `a=2^{n−3}` (forcing `A(Q_lo)=0`,
  pinch `n∈{4,5}`) are correctly stated. (Builder verified the identity 663 configs 0-mismatch; the
  reduction is an honest reduction, not a closure.)

**No forbidden route:** explicitly avoids the refuted `{Claim_R,T_R}` mutual induction and the false
"INC ⟹ max(Q)≤max(R)". The builder correctly states the family `{a}∪G_{n−3}` is NOT descent-closed
for `a≥1` (O1 fires) and that a DIRECT `A(R_lo)` proof is needed — no revival of the dead route.

**No overclaim:** builder corrected the outline's framing (HS-B2 closes only the *fully-tight* config,
not all `n∈{4,5}`), and correctly names DFB / (★) as the single open crux for general `h=2, a≥1`.

**Gap:** (★) `O_{Q_lo}≤O_{R_lo}+a_v` (= DFB `A(R_lo)−A(Q_lo)≥min(σ_lo,2−σ_lo)`) for general `h=2, a≥1`
is OPEN; a direct (non-recursive) proof is the remaining work. Even closing it leaves multi-cut
refined R and G-GAP for the full LB.

Scores — Correctness 10/10, Completeness 4/10, Progress 6/10 (a certified analytic floor + clean exact
reduction to one scalar inequality; strongest LB advance this round).

## 3. ll-dyadic-symdiff (LB) — CHANGES REQUESTED — Status: partial

**Correctness / rigor:** Two rigorous new lemmas, both certified.

- **Lemma G1 `max g≤1 ⟹ A(Q∪R)≥ΣQ−ΣR=1` — CERTIFIED** (`lemmas/G1-one-sided-kill.md`). Re-derived:
  with `M_k=measure{g=k}` and `max g≤1`, `∫g = M_1 − Σ_{k≤−1}|k|M_k ≤ M_1`, so `M_1≥∫g=1`; since
  `g=1` is odd, `A=measure{g odd}≥M_1≥1`. Verified the measure relation `A≥M_1≥∫g` on 3000 random
  exact-Fraction step functions (0 violations). Strictly generalizes certified D1 on the `g≤1` side
  (D1 needs `|g|≤1`) — a genuine new tool.
- **Foundation F-neg `g(0⁺)=c_Q−c_R−(n−1)≤−1` — CERTIFIED** (`lemmas/F-neg-boundary-parity.md`).
  Re-derived: `|Q|=c_Q+1`, `|R|=n+c_R`, budget `c_Q+c_R≤n`, `c_R≥1` ⟹ `c_Q≤n−1` ⟹ `g(0⁺)≤−1`. Exact.
- **R11 target `B₊≤A₋+B₋` correctly DROPPED as circular** — confirmed `⟺ A≥1` algebraically. The
  Sub-3a dichotomy re-frame is a legitimate non-circular replacement.
- **HS-D3 (max|g|-agnosticism):** confirmed — the route (measure form, F-neg, Sub-3a, G1) uses no
  `max|g|≤2` hypothesis.
- **Obstruction correctly delimits the open gap:** I verified the abstract profile `g=(−1 on [0,ε),
  +2 on [ε,ε+s), 0)` with `∫g=1` (`s=(1+ε)/2`) has `A=measure{g odd}=ε<1` while satisfying F-neg and
  failing Sub-3a — so F-neg + parity alone are provably insufficient; HS-D1 needs the `ΣQ=2^n`
  staircase geometry. Honest and correct.
- **Spec concern validated:** the explorer's budget-parity argument ("each cut lowers the odd-mult
  count by ≤1, so ≥n cuts needed") is NOT rigorous — a cut can drop the count by 3. The builder
  flagged it, uses it only for `A>0` (not the `+1`), and left the general-n proof open. Correct call.

**Gap:** HS-D1 (`Sub-3a fails ∧ max g≥2 ⟹ A≥1`) is OPEN — only a sketch/obstruction, no mechanism
converting the per-level parity switch into ≥1 measure. Numerically true (`min A=9/8,2,3` for n=3,4,5).

Scores — Correctness 10/10, Completeness 3/10, Progress 5/10 (fixed a genuine circularity, added a
D1-generalizing kill lemma + a foundation, and rigorously delimited the residual).

---

## Certifications this round
- `lemmas/floor-a-union-Gj.md` — CERTIFIED (marked certified; reviewer re-derived).
- `lemmas/G1-one-sided-kill.md` — CREATED + CERTIFIED (new).
- `lemmas/F-neg-boundary-parity.md` — CREATED + CERTIFIED (new).
- No lemma rejected. The dyadic budget-parity claim was NOT certified (builder correctly left it open).

## Goal Progress (Elo / status snapshot for run state)
- Status: **partial** (unchanged). Answer confirmed; UB rigorous n≤3, both-bounds n≤2.
- Ranking (Elo, post-round): geometric-selfsimilar **1753.9** (partial) > ll-inclusion-gap **1639.6**
  (advanced) > ll-dyadic-symdiff **1507.0** (advanced) > alternating-sum-value 1374.5 (dormant) >
  extremal-smoothing 1224.9 (dormant, S1 stuck 9 rounds). Order unchanged.
- Net movement: **UB** = still the single pure hard case (T5/HS-A2), plus a hardened rule that all UB
  numeric evidence must be off-grid (prior grid checks were unsound in the `δ>2t` region). **LB** =
  two independent routes each reduced to one sharply-stated open scalar crux: ll-inclusion-gap's
  `(★) O_{Q_lo}≤O_{R_lo}+a_v` (general `h=2, a≥1`), and ll-dyadic's HS-D1 (`Sub-3a fails ∧ max g≥2`).
- Verdicts: **geometric-selfsimilar CHANGES REQUESTED, ll-inclusion-gap CHANGES REQUESTED,
  ll-dyadic-symdiff CHANGES REQUESTED.** All three stay live and advancing; none solved, none broken.
