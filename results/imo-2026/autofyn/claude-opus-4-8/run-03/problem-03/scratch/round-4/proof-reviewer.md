# Proof-reviewer report — imo-2026-03, round 4

Reviewed 3 builds. All recorded Statuses (2× partial, 1× partial-recommending-RETHINK) are
HONEST — no overclaiming. Every load-bearing new claim re-derived independently and checked
numerically (exact Fraction arithmetic). Answer c(n)=2^n/(2^{n+1}−1) unchanged, consistent n≤3.

---

## 1. induction-peel.md — Verdict: CHANGES REQUESTED (Status: partial)

Scores: Correctness 10/10 (on the parts claimed rigorous) · Rigor 9/10 · Progress 8/10.

Load-bearing new claims, all independently verified:
- **L9 (self-pairing ⟹ W=0).** Trivially rigorous: the overlap set {N_Q odd ∧ N_C odd} ⊆
  {N_Q odd}, so W ≤ meas{N_Q odd} = S(Q_low) (L3) = 0. Correct. CERTIFIED → lemmas/L9-selfpairing.md.
- **(PM) reformulation.** S(B_low)=∫[D odd] since N_{B_low}=N_Q+N_C ≡ N_Q−N_C=D (mod 2), odd-sets
  coincide (L3). ∫D = sum(Q_low)−sum(C) = (2^n−e)−(2^n−1) = 1−e. The >H part is necessarily a
  shard of 2^n (shards of 2^j, j≤n−1 are ≤2^{n-1}=H), so it lies in Q and capping removes exactly
  e — the sum accounting is correct. So (A-res) ⟺ (PM) ∫[D odd] ≥ ∫D. Verified. CERTIFIED → L11.
- **R2 (D≤1 a.e. ⟹ (PM)).** f(d)=[d odd]−d ≥ 0 for integer d≤1 (d≤0: both terms ≥0; d=1: 0).
  Correct. Extremal Q_low=C⊔{1} gives D=[t<1]∈{0,1}, (PM) tight. Verified.
- Truncation identity, Case 1, e≥1 regime: unchanged from certified L6, still rigorous.

**Honest remaining gap (Open gap 1'):** prove (PM) ∫[D odd] ≥ ∫D when D reaches ≥2 in the
interior, using the single-block part budget |Q_low|+|C| ≤ 2n+1. The builder correctly fences off
refuted directions (arbitrary-X invariant P*, cuts-on-C cap on W). Upper bound (Open gap 2, branch
inequalities) still open — the field's second wall. Gap honestly flagged, not overclaimed.
Re-dispatch this builder to attack (PM)'s interior compensation.

## 2. alternating-sum-potential.md — Verdict: CHANGES REQUESTED (Status: partial)

Scores: Correctness 10/10 · Rigor 9/10 · Progress 7/10.

Load-bearing claims, all independently verified (0 mismatches over thousands of random cases):
- **β = matching = even-rank sum = ∫⌊N/2⌋.** Consecutive pairing (L4) has pair-minima = even
  ranks; layer-cake gives ∫⌊N/2⌋. Verified. CERTIFIED → lemmas/L10-beta-matching.md.
- **β-split β(Q⊔C)=β(Q)+β(C)+W** via floor identity ⌊(a+b)/2⌋−⌊a/2⌋−⌊b/2⌋=[a odd ∧ b odd].
  Verified. Included in L10.
- **Case 1 (top uncut) in β-language:** 2^n is the strict max (2^n > 2^n−1 = sum of rest), removing
  it shifts every even rank of B to an odd rank of B∖{2^n}, so β = odd-rank sum(B') ≤ sum(B') =
  2^n−1. Algebraically rigorous. Verified.
- **Obstruction map O1–O4:** all counterexamples reproduce exactly — O1 six 2.5's β=7.5>7 (cut
  budget essential); O2 B={4,2,2,2,2,2,1} (valid ≤3-cut refinement of P_3, sum 15) β=6, both
  pointwise strengthenings fail (⌊N/2⌋=3>N_R=2 on (1,2]; y_(6)=2>1); O4 six 2.5's majorized by P_3,
  ≤7 parts, yet fails (Tβ). Correct rigorous negative results.

**Important non-overclaim (builder is honest about this):** (Tβ) β(B)≤2^n−1 is EXACTLY equivalent
to the layer-cake residual S(B)≥1 (both via L4). The reforge is a reframing + obstruction map, not
a closure. Gaps Gβ (e<1 global matching cap) and G2 (general UB) honestly open. Re-dispatch.

## 3. averaging-upper-bound.md — Verdict: RETHINK (Status: unsolved)

Scores: Correctness 10/10 (the negative result is correct) · Rigor 10/10 · Progress: negative
(closes off a mechanism).

The top-part convex-averaging mechanism is GENUINELY REFUTED, verified exactly:
- U_2({2,2,1}) = 0 (attained by BISECTing the small part 1 → {2,2,½,½}, S=0), target 5/7.
- Both top-part first moves (BISECT_top and MATCH_top with v=1) yield {2,1,1,1}, and U_1({2,1,1,1})
  = 1 > 5/7. Since every convex average ≥ min of the two branches (Obstruction 1), no weight p(·)
  can reach 5/7. The winning move is a non-top split, outside the top-part S-effect formulas.

The mechanism is dead, not merely stalled: the min of the branches — the best any average can be —
already overshoots. Correctly recommends RETHINK. Recorded as a do-not-retry finding (record_outcome
dead-end). The outliner must re-plan the UB from a framing that admits whole-profile split choice
(β=Σ_even "cancel unmatched small parts", or a global majorization/LP certificate) — NOT a top-part
rule and NOT a match/bisect-DP variant (both walls exhausted).

---

## Lemmas certified this round
- **lemmas/L9-selfpairing.md** — S(Q_low)=0 ⟹ W=0 ⟹ S(B_low)=S(C). (from induction-peel)
- **lemmas/L10-beta-matching.md** — β=even-rank sum=∫⌊N/2⌋; β-split. (from alternating-sum)
- **lemmas/L11-parity-vs-mean.md** — R1 reformulation + R2 pointwise condition (general PM stays
  OPEN, explicitly marked non-certified). (from induction-peel)

No lemma was rejected. current.md updated (Status stays partial; approaches-tried and certified-
lemma list refreshed; averaging-upper-bound RETHINK + do-not-retry recorded).

## Field state
Both walls persist: (1) LB residual = (PM)/Gβ interior-compensation in the e<1 sub-case (same
statement in both live approaches, plateaued 4 rounds); (2) general UB, with the top-part averaging
route now also refuted. Per CLAUDE.md plateau rule, next round's outliner MUST open ≥1 UB approach
on a framing far from top-part / match-bisect-DP / min-pairing-witness.
