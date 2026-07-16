# Outline Review — imo-2026-03, Round 12

Field: advance the 3 leaders (geometric-selfsimilar UB, ll-inclusion-gap LB, ll-dyadic-symdiff LB),
each re-planned around this round's explorer findings. No new slug proposed; one contingency copy
flagged. I verified the load-bearing claims numerically (exact Fraction) and checked every plan
against the forbidden/refuted-route list in run_state.md.

---

## geometric-selfsimilar (UB) — APPROVE (advance)

Target: whole UB via the single pure hard case (c), immediate deliverable T5 (m=5) ⟹ n=4 UB rigorous.

Route check — no forbidden route smuggled in. The four refuted UB routes are SB-monotone (R7),
R3-cascade (R8), complement-cut m=4→3→R4 (R9), and the **p₁@p₂ threshold-invariant induction {(I'),(II'),(III')}** (R11). The T5 plan cuts pair1_2 (p₁@p₂) as a FIRST cut and then applies the certified T4
*strategy bounds* (A_R≤d₂, A_S≤d₃, A_P≤δ/2, A_C≤δ+d₄−|d₁−p₃|) compared against the ORIGINAL threshold t.
This is a one-step reduction to a concrete 4-piece analysis, NOT the recursive induction that required
the subproblem to inherit gap condition (2') — that inheritance (II') is the exact false step, and this
plan never invokes it. Distinction confirmed sound; the refuted route is not revived.

The double-invisible-pair reduction (Step 1) → Lemma AB/MK is a genuine one-cut m→m−2 drop, mechanism
stated (p_i−p_j=p_k cancels three pieces). Sound.

Load-bearing gaps, honestly flagged:
- **HS-A2 (the single blocking lemma for T5):** δ>2t ∧ Sub-A P fires ⟹ pair2_3 gives A≤t. The explorer's
  own bound d₂+2d₃+3d₄+3δ≤31t/2 yields only d₂<3.5t, NOT d₂<2t — so the naive pair2_3 P argument is
  INSUFFICIENT, and the config (d₁=8.6t, d₂=d₃=d₄=1.1t, δ=2.5t) is off the integer grid so "0 grid
  violations" does not cover it. This is a real analytic hole; the builder must either sharpen the Σ-bound
  or add a non-P pair2_3 sub-case for d₂∈(2t,3.5t). Expect T5 to remain a partial until HS-A2 is closed.
- **HS-A3 (general m≥6):** completely unmapped; Sub-B non-vacuous, double-pair coverage untested. Builder
  must state explicitly whether the Step1–5 tree is uniform in m or only closes m=5.

Verdict: sound direction, correct existence-of-witness UB ("min over strategy-family ≤ t"), no forbidden
route. Build to advance; target T5 first, mark HS-A2 and general-m honestly open. Do not let the write-up
present HS-A2 as closed by the grid checks.

## ll-inclusion-gap (LB) — APPROVE (advance)

Target: close G-INC-2nt a≥1 branch via Opening C (analytic floor + static tight-case forcing).

Route check — deliberately avoids both refuted routes: the {Claim_R,T_R} mutual induction (NOT
descent-closed, R10) and "INC forces max(Q)≤max(R)" (FALSE, R11). Opening C uses a STATIC analytic floor,
no induction on R's structure, so the a≥1 descent-closure break (O1 fires) that killed the F_a family route
does not apply here. This is a genuinely distinct, non-forbidden line.

Load-bearing claim VERIFIED (exact Fraction, j=1..5): **A({a}∪G_j) ≥ A(G_{j−1}), with the unique
minimum = A(G_{j−1}) attained exactly at a=2^j** (HS-B1). 0 violations below target; equality only at
a=2^j. The tight pinch is confirmed to be only n∈{4,5} (A(G_{n−4})=1); n≥6 has A(R_lo)≥3 auto-slack.
The mechanism (the pair {2^j,2^j} cancels the top term, piecewise-linear in a) is correct.

Gaps, honestly flagged:
- **HS-B2 (tight forcing A(Q_lo)=0):** the load-bearing static step — ΣQ_lo=3·2^{n−3}, S_{Q_lo}⊆[1,2),
  |Q_lo|≤budget ⟹ Q_lo is equal pairs. Only the unique witness (n=5: Q_lo={6,6}, A=0) is checked; the
  general argument is unwritten. Mind the parity subtlety (S_{Q_lo}⊆[1,2) constrains the odd-count region,
  not part magnitudes). This is the real crux — build it, don't hand-wave it.
- **HS-B3 (non-tight slack absorption):** A(Q_lo)≤A(R_lo)−1 for the REFINED R_lo. The certified L1 was proved
  for containment in the GEOMETRIC S_{G_{m−1}}, not the refined S_{R_lo}={a}∪G_{n−3}; confirm the −1 budget
  deficit transfers, or supply it directly. Honestly flagged.

Verdict: clean, non-circular, non-forbidden route with the floor claim machine-confirmed. Build to advance;
HS-B2 is the load-bearing target.

## ll-dyadic-symdiff (LB) — CHANGES REQUESTED (advance)

Target: bucket (iii) via the Sub-3a dichotomy (HS-D1), REPLACING the R11 level-charge target.

**The outliner's central re-frame is CORRECT and I confirmed it.** The old target B₊≤A₋+B₋ IS algebraically
equivalent to the goal A(Q∪R)≥1 for max|g|≤2: with ∫g=1, A₊=1+A₋−2B₊+2B₋ ⟹ A=1+2(A₋+B₋−B₊), so
A≥1 ⟺ B₊≤A₋+B₋. Verified numerically on the tight config Q={3,3,2},R={2,2,2,1}: A=1, and
1+2(A₋+B₋−B₊)=1+2(1+0−1)=1. It is a restatement, not a reduction — correctly dropped. Do NOT let the
build re-present it as a reduction (recorded dead-end).

The replacement (Sub-3a dichotomy) is a genuine, non-circular route: Sub-3a fires ⟹ A≥1 (certified), else
prove A>1 strictly. The foundations g(0+)≤−1 and the budget-parity odd-mult-piece lemma are PROVED by the
explorer (1548/1548) and sound.

CHANGES REQUESTED because the crux mechanism is only a SKETCH:
- **HS-D1 (Sub-3a-fails ⟹ A>1):** numerics min A = 9/8 (n=3), 2 (n=4), 3 (n=5), all >1 — but there is NO
  proof mechanism yet, only "each failing level has an internal parity switch creating paired odd-g
  sub-intervals." The builder MUST turn the per-level parity switch into a fixed positive measure and sum
  over levels; a bare "then it accumulates to ≥1" is not acceptable.
- **HS-D2 (g(0+) even, doubly-negative):** getting exactly ≥1 (not merely >0) from the forced ±1 crossings
  is the gap — the ≥0-vs-≥1 distinction is precisely what the whole LB turns on.
- **HS-D3 (max|g|≥3 agnosticism):** confirm the parity route does NOT secretly assume max|g|≤2 (unlike the
  discarded algebra). For general n max|g|≤n+1.

Verdict: the re-frame fixes a genuine circularity; the new route is legitimate but HS-D1 is the least-baked
of the three lines. Build it to advance and pin down the per-level measure lower bound; keep the write-up
honest (partial) — do not overclaim HS-D1.

## Contingency copy (max(P)-induction via double-REFL) — DECLINE

Not registered/copied this round. It is not clearly a distinct viable route with a concrete gap-fill: the
double-REFL cancellation A(Q∪R)=max(Q)−max(R)+A(Q'∪R'') requires the max(Q)=max(R) precondition (memory
rule 15: the 2nd peel breaks otherwise, INC does not force it), so it handles only part of bucket (iii); and
its base cases are claimed "closed by K1/K2/D1/Sub-3a on the reduced object" — but the residual is EXACTLY
where those cheap-kills fail, so the induction reduces to the same open crux at its base. The dead-end note
"REFL-telescope alone only recomputes A" applies. This matches the caution against approving a hedge slug
whose central descent bottoms out on the very obstruction it is meant to bypass. Keep 3 focused builds; if
HS-D1 proves too speculative next round, revisit with a concretely different base-case argument.

## Ranking (updated, stale flags cleared)

geometric-selfsimilar 1753.9 > ll-inclusion-gap 1639.6 > ll-dyadic-symdiff 1507.0 > alternating-sum-value
1374.5 > extremal-smoothing 1224.9. Evidence anchoring: geometric's UB is nearly complete (single hard case,
everything else closed all m) — clear leader; ll-inclusion closed the a<1 branch R11 and this round has a
machine-verified analytic floor for the a≥1 route — ahead of ll-dyadic, whose R11 target was just exposed as
circular and whose new HS-D1 is only a sketch (a setback, but still live and advancing vs the two dormant
lines); alt-sum and extremal remain unbuilt since R3 (extremal's S1 stuck 9 rounds) — trailing.

build set: geometric-selfsimilar, ll-inclusion-gap, ll-dyadic-symdiff
