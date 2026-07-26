# Proof-reviewer — Round 6 — imo-2026-03

Four built slugs reviewed independently and adversarially. **HEADLINE: `c(3)=8/15` IS SOLVED end-to-end** (two-regime-disjunctive APPROVED; lower bound L(3) certified via cell-complex, upper bound U(3) now closed by a complete 4-regime partition with the new 7-cap extreme closure). This is the third solved value alongside c(1)=2/3, c(2)=4/7.

---

## 1. `two-regime-disjunctive` — APPROVE — Status `solved` (for n=3)

**Claim:** `c(3)=8/15` solved end-to-end via a 7-cap case-by-case contradiction closing the U(3) `d<1/2` non-gap extreme sub-cases (regime IV), merged with the certified L(3) and the round-5 closures of regimes I–III.

**Adversarial re-derivation of the load-bearing step (the 7-cap contradiction, §5e.3).** I re-derived every one of the 8 sign-triple sub-cases from scratch in chain-excess coordinates `(u,v,w,z)` with the identity `7u+4v+2w+z=α`, `z=α−7u−4v−2w`. The chain-excess forms of the 7 caps (C1=α+u, C2=α+v, C3=2α+u+w, C4=4α−6u−3v−2w, C5=|α+w|, C6=|3α−L_6|, C7=|5α−L_7| with L_6=7u+3v+2w, L_7=6u+3v+w, L_6−L_7=u+w) all check out. Under the contradiction assumption all 7 > α, the chain caps give (I) u>0, (II) v>0, (III) u+w>−α, (IV) 6u+3v+2w<3α, (∗) d<1/2 ⟺ u>z. The sign branches s_5/s_6/s_7 are correctly derived. Each of the 8 sub-cases yields a clean ≤4-line inequality contradiction:
- A1 (−,+,+): u>α from (III)∧w<−2α, then 5u−2α<2α ⟹ u<4α/5<α. Contradiction. ✓
- A2 (−,+,−): u+w<−4α vs (III) u+w>−α. ✓
- A3 (−,−,+): 2L_7=L_6+5u+3v (identity verified) >14α vs L_7<4α ⟹ 2L_7<8α. ✓
- A4 (−,−,−): w<−3α from (IV)∧L_7>6α; then 6u+2w>6α ⟹ 3v<−3α<0 contradicting (II). ✓
- B1 (+,+,+) [tightest]: (S2)∧L_6<2α ⟹ v>α; w>0∧L_6<2α ⟹ 7u+3v<2α; v>α ⟹ u<−α/7<0 contradicting (I). Global extremum 12α/13=4/65<α, margin 1/195. ✓
- B2/B3/B4: each a 2-line contradiction (u+w<−4α vs III; w<−2α vs s_5=+1's w≥−α; w<−3α vs w≥−α). ✓

**Realizability of all 7 caps (§5e.1).** I verified the equal-pair cancellation lemma (even case: the two odd-multiplicity blocks contribute +larger, −smaller = |difference|, because the earlier block starts at an odd rank; proven via the tileability-by-length-2-blocks argument). The two NEW abs caps are sound and always-realizable: C6=|a+c−d| via "bisect b + match a in d" (multiset {a,a,b/2,b/2,c,d−a}, pairs (a,a),(b/2,b/2), singletons c,d−a); C7=|a+b−d| via "bisect c + match a in d". None requires d≥b+c or d≥1/2 — the round-5 "no 4–7-cap subfamily suffices" ruling is correctly overturned (it counted un-realizable cap *values* like d−b−c). The §5e.4 realizability of |b+c−d| (bisect a + match c in d) for regime III's z∈[−2α,0] sub-case is also sound.

**Exhaustiveness/disjointness of the 4 regimes.** (I) d≥1/2 / (II) gap G (u,v,w,z>0) / (III) non-gap w,z≥−2α / (IV) extreme w<−2α∨z<−2α. Exhaustive and disjoint; every config in exactly one. Regime III's four sub-cases (u≤0→cap a; v≤0→cap b−a; w∈[−2α,0]→cap |a+b−c|; z∈[−2α,0]→cap |b+c−d|) are exhaustive (in d<1/2 non-gap, at least one excess ≤0, split at −2α). Regime IV partition: under all-7>α, C5>α forces w>0 or w<−2α (w∈(−2α,0) gives C5<α), so the 8 sign triples are exhaustive over E under the contradiction assumption. Each sub-case contradicts, so min≤α throughout E (strict — LP max t<0 in all 12 cells).

**Verification.** `/tmp/round-6/u3_7cap_verify.py` confirms: 0 violations on 5473 exact-rational extreme configs (worst min=0.0582<α=0.0667), LP max t<0 in all 12 (sub-regime×sign-triple) cells. Reproduced.

**Lower bound L(3).** Certified (cell-complex, `lemma-vertex-principle-advantage.md`): every real Xiang response to (1,2,4,8)/15 gives A≥1/15, Liu≥8/15.

**Final answer.** f(3)=2³/(2⁴−1)=8/15. ✓ Verified by substitution. Equality iff the dyadic (1,2,4,8)/15 (in regime I).

**Minor caveats (non-blocking).** Drop-one on the coarse grid shows C5 and C7 appear droppable (0 violations), but the proof uses all 7 and does NOT rely on minimality — sound regardless. The builder's note that C7 is "genuinely load-bearing on fine samples" is about minimality, not correctness.

**Status:** the approach is `partial` overall (general-n U and L(n≥5) open), but **`c(3)=8/15` is SOLVED end-to-end**. Verdict: **APPROVE** (for the n=3 sub-claim). Proposed lemma `lemma-u3-7cap-extreme` **CERTIFIED** (sound, correct scope, proved).

---

## 2. `pairing-partner` — CHANGES REQUESTED — Status `partial`

**Claim:** general-n L via sum-level Hall injection φ (Reduction D: L(n+1) ⟺ φ-existence); m_1-split consolidated; staircase equality theorem PROVEN for all n; H1/H2 OPEN.

**Flaw in Reduction D (load-bearing).** The claimed equivalence `L(n+1) ⟺ existence of φ` is FALSE in the direction `e_M ≤ o_R ⟹ φ-existence`. The chain is: L(n+1) ⟺ e_M ≤ o_R (certified) ⟺ (Match) Σ_MM m_even ≤ Σ_RR r_odd (certified self-compensation). The builder then claims (Match) ⟺ φ-existence "by Hall's marriage theorem". This conflates the TOTAL sum inequality (Match) with Hall's per-subset condition. Hall's theorem requires: for EVERY subset S of left vertices, |N(S)| ≥ |S| (a per-threshold count condition for the r≥m graph), NOT just the single total Σ m ≤ Σ r. Counterexample: L={3,3}, R={5,1}: Σ m=6≤6=Σ r, but no injective matching with r≥m exists (only one right vertex ≥3). So (Match) is necessary but NOT sufficient for φ. The correct statement is φ-existence ⟹ L(n+1) (one direction); the reverse is unestablished. The proposed lemma `lemma-hall-injection-reduction` as stated (an equivalence) is **INCORRECT — REJECTED**. It should be downgraded to "φ-existence ⟹ L(n+1)" (sufficient condition, not equivalence).

**Sound parts.** (a) The staircase equality theorem (§F: pair-pile config attains A=α(n+1) for all n) is correctly proved — verified independently; it is the certified pair-pile re-derived within the M⊎R frame. (b) The general-n m_1-split consolidation (§E) with the geometric-ratio-2 lever a_j=2·a_{j+1} is sound. (c) The Branch-1/Branch-2 reductions to (H1)/(H2) are rigorous reductions (the matchings themselves OPEN, honestly scoped). (d) L(3) unrefined-R self-rigorous (round-5, both branches) stands.

**Overclaim:** Status and approach are honestly `partial` (general-n H1/H2 open), but the Reduction D "⟺" and the proposed lemma overclaim an equivalence. The gap: prove φ-existence (the per-subset Hall condition), not just the total (Match).

**Verdict:** CHANGES REQUESTED (partial). Outcome: advanced (staircase theorem + consolidation sound) but the headline Reduction D equivalence is wrong and the lemma is rejected.

---

## 3. `cell-complex-l3` — CHANGES REQUESTED — Status `partial` (verified-milestone / dead-engine)

**Claim:** D3 structural theorem attacked via 2-adic-valuation lever; lever FALSIFIED; verified data (min fractional A=5/3 at n=3,4) stands; conditional L(n)-for-all-n corollary; gaps honestly scoped.

**Soundness of the falsification.** The valuation-reduction lemma `v_2(num)−v_2(L)=v_2(A)` is a correct one-line identity (num=A_num·k, L=A_den·k after reducing A=num/L; v_2(xy)=v_2(x)+v_2(y)). The explorer's `v_2(num)<v_2(L)` is indeed equivalent to v_2(A)<0. The census (27/2019 at n=3, 135/5148 at n=4 have v_2(A)<0; min fractional A=5/3 has v_2(5/3)=0, odd denominator 3) is decisive: the 2-adic mechanism is NOT the obstruction. Falsification is sound.

**Verified data.** L(4) CERTIFIED (prior round, reproduced). Min fractional A=5/3 at n=3,4 stands. The structural pattern (4/3-triple extremal: bisect top n−1 Liu pieces + split piece 4 into three 4/3's + leftover 1) is a genuine general-n candidate family (A=5/3 for all n≥3), but NOT proved to be the global min — honestly scoped.

**Conditional corollary (§D3.3).** Correctly stated: IF D3 (fractional vertices have A>1) AND certified lemma-parity-integer-vertices (integer vertices A≥1) AND vertex-principle, THEN L(n) for all n. Sound conditional; D3 is the sole open step in this route.

**Induction gap (§E).** L(n) on R gives o_R≥M/2, but L(n+1) needs e_M≤o_R; factor-of-2 gap honestly scoped (same wall as pairing-partner).

**Proposed lemma `lemma-d3-fractional-vertices`.** Honestly labeled PROPOSED (unproven conjecture). It is a tracked OPEN conjecture (verified n=3,4, 2-adic mechanism falsified), NOT a proved lemma. **REJECTED for certification** (it is a conjecture, not a lemma); left in lemmas/ as a record of the open problem.

**Verdict:** CHANGES REQUESTED (partial, verified-milestone + dead-engine). Outcome: verified-milestone (L(4) certified) with the 2-adic engine dead (a real negative result); D3 open; conditional corollary sound.

---

## 4. `self-reproducing-invariant` — CHANGES REQUESTED — Status `partial` (new)

**Claim:** G2 framing via self-reproducing invariant (crux aimo-0262); pair-pile as recursive invariant; ridge reproduces all n≥2; 2-strategy family for near-dyadic active+below; far-from-dyadic OPEN (single-gap-trap risk noted).

**Sound parts.** (a) Self-reproduction (§1.3): pair-pile(n+1)=bisect(M)++pair-pile(n), A=α(n+1). Correct (verified n=2..5); essentially the certified pair-pile in recursive form. (b) Ridge reproduction all n≥2 (§2.1): pair-pile on R_e=(2^n,...,4,2+e,1−e)/D(n) gives A=α(n) via compensating excesses (1−e)+e=1. I verified the algebra for n=3,4 and several e — sound. This generalizes the certified n=3 ridge-falsification to a POSITIVE all-n result. (c) 2-strategy bound (§3.2): dist-2 gives A=1 always; dist-1 gives A=1+2a (a>−1/2) or A=−1−2a (a<−1/2, changed sort). I verified min(A1,A2)≤1 for all a∈(−1,1) — the bound holds.

**Overclaim / proof gap.** The theorem 3.2 CONCLUSION is stated for a∈(−1/2,1) (matching the proof's explicit sort), but the PROMOTABLE LEMMA 3 claims a∈(−1,1). The claim is actually true for a∈(−1,−1/2] (dist-1's sort changes to A=−1−2a≤1, which I verified), but the proof TEXT does not derive this changed-sort case. So the promotable lemma is stronger than the proof-as-written. Reject lemma 3 (fillable gap).

**Honest scoping (no overclaim).** The builder explicitly scopes to near-dyadic + E_n, and explicitly notes the single-gap-trap risk for far-from-dyadic (would share two-regime's S1/S3 sliver wall). Gap 1 ("active grows from above", both strategies overshoot, n≥4) and Gap 2 (far-from-dyadic) are honestly OPEN. The aimo-0262 disjoint-pair averaging is correctly noted as NOT translating (A is a sum, not a max). This is genuinely-different from the dead 2-adic strict-decrease and two-regime 17-family casework.

**Verdict:** CHANGES REQUESTED (partial, new approach with real progress). Outcome: partial (self-reproduction + ridge + 2-strategy rigorous; two open gaps).

**Lemma certifications for this approach:**
- Lemma 1 (self-reproduction, §1.3): **CERTIFIED** — correct, proved; structural recursion framing of the pair-pile. Will create `lemmas/lemma-pair-pile-self-reproduction.md`.
- Lemma 2 (ridge reproduction all n≥2, §2.1): **CERTIFIED** — correct, proved, verified; genuinely new (positive all-n generalization of the n=3 ridge). Will create `lemmas/lemma-ridge-reproduction-all-n.md`.
- Lemma 3 (2-strategy bound, §3.2): **REJECTED** — promotable statement (a∈(−1,1)) is stronger than the proof-as-written (a∈(−1/2,1)); the changed-sort case for a∈(−1,−1/2] must be filled in (it is true but unproved in the text).

---

## Summary

| Slug | Verdict | Status | Outcome | Lemma |
|---|---|---|---|---|
| two-regime-disjunctive | APPROVE (n=3) | solved (n=3; partial overall) | verified-milestone | u3-7cap-extreme CERTIFIED |
| pairing-partner | CHANGES REQUESTED | partial | advanced (Reduction D ⟺ false) | hall-injection-reduction REJECTED |
| cell-complex-l3 | CHANGES REQUESTED | partial | verified-milestone (2-adic dead) | d3-fractional-vertices REJECTED (conjecture) |
| self-reproducing-invariant | CHANGES REQUESTED | partial | partial (new) | self-reproduction + ridge-reproduction CERTIFIED; 2-strategy REJECTED |

**HEADLINE: `c(3)=8/15` IS SOLVED end-to-end.** Lower bound L(3) certified (cell-complex); upper bound U(3) closed by a complete 4-regime partition (I: 5-cap dominant; II: 3-mark sliver gap; III: |a+b−c|/|b+c−d|/a/b−a; IV: 7-cap extreme — all rigorous, equality iff the dyadic (1,2,4,8)/15). Third solved value after c(1)=2/3, c(2)=4/7. General-n L and U remain open.
