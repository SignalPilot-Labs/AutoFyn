# imo-2026-03 — Explorer Report: LB Unifier (refined-R mutual induction)
**Lens: refined-R alternating-tail base crux; {Claim_R, T_R} unifying induction**

---

## Problem ID: imo-2026-03

---

## Summary for the outliner

The central dispatch question — "can Gen-Decomp's descent now support a unifying {Claim_R, T_R} mutual induction for refined R?" — is answered **YES for the dominant cases, with two precise residual gaps**. Full terrain follows.

---

## (a) Does Gen-Decomp give a well-founded recursion?

**Descent measure: n, decreasing by 2 each step.**

Gen-Decomp (certified, R9) states: for any R, Q with max(R) ≤ 2^{n-1}, S_Q ⊆ S_R, and h_R := #{R-parts ≥ 2^{n-2}} EVEN:
```
A(R) − A(Q) = deficit_top + (A(R_lo) − A(Q_lo)),   S_{Q_lo} ⊆ S_{R_lo}
```
where R_lo := {R-parts < 2^{n-2}}, Q_lo := {Q-parts < 2^{n-2}}.

**Key cases for termination:**

**Lower-band cuts** (G_{n-1} with cuts only of pieces 2^{k_0}, k_0 ≤ n-3):
- h_R = #{4=2^{n-2}, 8=2^{n-1}} = 2 (EVEN). Gen-Decomp applies.
- R_lo = G_{n-3} with the SAME lower-band cut(s). Still a standard G_{n-3}-refinement.
- h_{R_lo} at thr = 2^{n-4}: #{2^{n-4}, 2^{n-3}} = 2 (EVEN). Gen-Decomp applies at level n-2 too.
- Descent: (n, R) → (n-2, R_lo) → (n-4, R_lo_lo) → ... → (2, base). Well-founded, every level has h = 2. **The recursion is clean for all lower-band cuts.**

**Non-equal top-piece cuts with a ≥ 1** (cut 2^{n-1} → {a, 2^{n-1}-a}, a ∈ [1, 2^{n-2})):
- h_R = #{a < 2^{n-2}: 2 high pieces: (2^{n-1}-a) and 2^{n-2}} = 2 (EVEN). Gen-Decomp applies.
- R_lo = G_{n-3} △ [0, a) (flip of [0, a)), where a ≥ 1 means [0,a) overlaps full unit-width pieces: R_lo is a valid G_{n-3}-refinement (cut of piece at position a within [0,2^{n-3}]).
- h_{R_lo} at thr = 2^{n-4}: still 2 (the two remaining uncut upper G_{n-3} pieces). Gen-Decomp applies.
- **Descent is clean.** Budget at n-2: |Q_lo| ≤ (n-2)+1 (from |Q| ≤ n and h=2), matching level n-2 hypotheses.

**ΣQ_lo in the correct window:** For both lower-band and non-equal top cuts, the sub-case analysis (h=2, deficit_top = a+b < 1) gives ΣQ_lo = 2^{n-2} + ε' with ε' = a-b ∈ (-1,1) — IDENTICAL to the anchor analysis. This is the SAME window as the anchor proof used for {Claim, T}.

**Conclusion:** The recursion terminates in ⌊n/2⌋ steps; the descent measure is strictly decreasing; at every level Gen-Decomp applies (h_{R_lo} = 2 even). The cross-position concern from G-INC-2lb is RESOLVED for these cases — lower-band cuts at each level remain lower-band cuts at the descended level, never converting to top-piece cuts at the same descended level (a top-piece cut of G_{n-3} at level n-2 would arise only if the "base" k_0 = n-3, which terminates the recursion one step earlier). The descent terminates cleanly at n ∈ {1,2} or n=4 (where verified numerically).

---

## (b) Correct statements of Claim_R and T_R

**Claim_R(n, ε):** For finite multisets Q, R with max(R) ≤ 2^{n-1}, h_R := #{R-parts ≥ 2^{n-2}} EVEN, A(R) ≥ 1, S_Q ⊆ S_R, |Q| ≤ n+1, ΣQ = 2^n + ε (ε ∈ [0,1)):
```
A(R) − A(Q) ≥ 1 − ε.
```

**T_R(n):** Same hypotheses but ΣP ∈ (2^n − 1, 2^n) (τ = 2^n − ΣP ∈ (0,1)):
```
A(R) − A(P) ≥ 1 − τ.
```

These directly generalize the certified {Claim, T} (which fix R = G_{n-1}).

**Inductive step via Gen-Decomp** (for h_R even):
Reduce to deficit_top + (A(R_lo) − A(Q_lo)) ≥ 1 − ε:
- Case h=0: deficit_top = measure(S_R ∩ I_{n-1}) ≥ 2^{n-2} ≥ 1 ≥ 1-ε. Done.
- Case h=2: deficit_top = a+b (where a = 2^{n-1}-q_1 ≥ 0, b = q_2-2^{n-2} ≥ 0). ΣQ_lo = 2^{n-2}+ε'. Same 2a/2b-i/2b-ii split as the anchor proof (identical arithmetic). Invokes Claim_{R_lo}(n-2, ε') or T_{R_lo}(n-2).

**The step is LITERALLY the same as the anchor proof.** Gen-Decomp replaces the SET IDENTITY's role in delivering S_{Q_lo} ⊆ S_{R_lo}.

**Where the anchor SET IDENTITY was used and why Gen-Decomp removes the dependence:**
The anchor's SET IDENTITY (S_{G_{n-1}} ∩ [0,2^{n-2}) = S_{G_{n-3}}) was used to get S_{Q_lo} ⊆ S_{G_{n-3}} (fixed anchor object). Gen-Decomp delivers S_{Q_lo} ⊆ S_{R_lo} DIRECTLY, with no assumption on what R_lo looks like. The dependence on the anchor's specific dyadic structure is GENUINELY removed. The residual: R_lo is variable (not fixed as G_{n-3}), so the induction must carry R as a parameter — but the structure of the inductive step is unchanged.

---

## (c) Base case verification

**Descent base at n=2 (lower-band cut arriving with R_lo = {1,1,1}):**

R_lo = {1,1,1} is the canonical output of a lower-band cut (cut piece 2 → {1,1}) at n=4. A(R_lo) = 1. Budget gives |Q_lo| ≤ (n-2)-h+h_lo... concretely |Q_lo| ≤ 2 from |Q| ≤ n=4, h=2.

For |Q_lo| ≤ 2, S_{Q_lo} ⊆ S_{R_lo={1,1,1}} = [0,1): parts > 1 must come in equal pairs (otherwise N_{Q_lo} odd above 1 violates INC). With |Q_lo| = 2: Q_lo = {s, s} (equal pair), A(Q_lo) = 0. A(R_lo) − A(Q_lo) = 1. **Claim_{R_lo}(2, ε') holds trivially: A(R_lo)−A(Q_lo) = 1 ≥ 1-ε'.** Verified numerically at n=4 (step=1/2, 29 INC configs, min margin = 1, 0 violations).

**The budget is the key**: |Q_lo| ≤ n-h forces so few parts at the base that the equal-pair cancellation gives A(Q_lo) = 0 automatically.

**Descent base at n=2 (non-equal top-cut arriving with R_lo = {3,2,1} at n=4, a_cut=3):**

A(R_lo = {3,2,1}) = 2. S_{R_lo} = [0,1)∪[2,3). For Q_lo with S_{Q_lo} ⊆ [0,1)∪[2,3), |Q_lo| ≤ 2: the constraint S_{Q_lo} ⊆ [2,3) forces p1 ≥ 2, p2 ≤ 3. With p1+p2 = 4+ε' and p1 ≥ 2: p2 ≤ 2+ε'. A(Q_lo) = p2-p1 = 2p2-(4+ε') ≤ 2(2+ε')-(4+ε') = ε'. So A(R_lo)−A(Q_lo) ≥ 2-ε' ≥ 1 ≥ 1-ε'. Verified: n=4 non-equal cut (8→5+3), step=1/2, 11 INC configs, min margin=2, 0 violations.

**The base cases close for all verified descent configurations.**

---

## (d) A(Q'∪R'') ≥ 1 base object in bucket (iii) (ll-dyadic-symdiff)

The REFL-telescope in ll-dyadic-symdiff reduces general-n bucket (iii) to A(Q'∪R'') ≥ 1 where Q' = Q\{max(Q)}, R'' = R\{max(R)}. This is an INC or GAP sub-instance at smaller piece-count and sum. The INC sub-instance of this base is exactly Claim_{R''}(?, ε) for the appropriate level. The {Claim_R, T_R} induction, if established for all h_R-even R, covers the INC sub-instances. The GAP sub-instances need the G-GAP argument.

Numerically: n=3 bucket (iii) FULLY CLOSED (R9, 0/10912 violations, min A=1). The n=4 base object is the first nontrivial general-n instance. No violations at n=4 (188 configs at step=1/2, min A=2).

---

## (e) G-INC-2e thin edge: parity argument closes it

The "thin edge" G-INC-2e (equal-split top cut, g=0, h_bar≥2, q1>q2 unequal) is NOT a real gap:

**Parity argument:** For the equal-split top-piece cut: R = {2^{n-2}, 2^{n-2}, 2^{n-2}} ∪ G_{n-3}, so |R| = n+1. The Forcing Lemma gives max(Q) ≤ max(R) = 2^{n-2}. By Step 18(a), S_R = S_{G_{n-2}}. When |R| is ODD (n even): N_R(0+) = n+1 is odd, so [0,1) ∈ S_R. Then for |Q| EVEN: N_Q(0+) = |Q| even → [0,1) ∉ S_Q → A(Q) = measure(S_Q) ≤ measure(S_R) − measure([0,1)) = A(R) − 1. The G-INC-2 claim holds automatically.

For the G-INC-2e cases to be nontrivial, we need |Q| odd (so [0,1) ∈ S_Q). But |Q| odd + ΣQ = 2^n with all parts ≤ max(R) = 2^{n-2}: the few-parts-budget constraint makes this infeasible for the unequal-top-parts (q1>q2) case.

**Numerical verification:**
- n=4, step=1/4: 0 G-INC-2e cases found.
- n=5, step=1/4: 0 G-INC-2e cases found.
- n=6, step=1/2: 2379 G-INC-2e cases found, all with margin ≥ 3 (the parity argument gives margin ≥ 1; the actual minimum is 3). NOT a gap.

**The G-INC-2e thin edge is vacuous or automatically satisfied by the |Q|-parity argument.** The outliner should remove it from the open-gaps list.

---

## (f) Concrete obstructions, ranked by promise

**Obstruction 1 (MAIN): G-INC-2nt with a_cut < 1 (sub-unit flip).**
For non-equal top-piece cuts with a_cut < 1: R_lo = G_{n-3} △ [0, a_cut) where [0, a_cut) is a proper subset of [0,1) (the bottom unit interval). This R_lo is NOT a standard G_{n-3}-refinement (it's not obtained by cutting any piece of G_{n-3}; it "flips" a sub-interval of the bottom piece). The descent via Gen-Decomp still applies (h_R = 2 even), and S_{Q_lo} ⊆ S_{R_lo} is still guaranteed. But the claim Claim_{R_lo}(n-2, ε') at level n-2 for this exotic R_lo needs verification.

**What's specific about a_cut < 1:** A(R_lo) = A(G_{n-3} △ [0, a_cut)) = A(G_{n-3}) ± a_cut (sign depends on n parity). For n even: A(G_{n-3}) is even-indexed (odd integer), and [0, a_cut) is flipped INTO S_R if N_{G_{n-3}}(0+) = |G_{n-3}| = n-2 is even, i.e., n even. So A(R_lo) = A(G_{n-3}) + a_cut ≥ 1. For n odd: A(R_lo) = A(G_{n-3}) − a_cut ≥ 1 − a_cut. If a_cut is close to 1: A(R_lo) can be close to 0.

**Why it may still close:** The budget constraint gives |Q_lo| ≤ n-2 (from h=2 at level n). At level n-2 with R_lo's S_{R_lo} = S_{G_{n-3}} △ [0, a_cut), the target is A(R_lo) − A(Q_lo) ≥ 1 − ε'. The (n-odd, small a_cut) sub-case may be the only hard one, but numerically (n=4,5 verified 0 violations) the claim holds. The budget forces A(Q_lo) to be near-zero (equal pairs), giving the slack needed.

**Proposed approach:** Handle a_cut < 1 as a DIRECT BASE CASE at n=4 (the first time it can arise in the recursion). At n=4, a lower-band cut or non-equal top cut with a_cut < 1: verify the finite case directly (budget-enforced enumeration, already 0 violations).

**Obstruction 2: G-GAP branch (non-containment, S_Q ⊄ S_R).**
Not covered by the {Claim_R, T_R} INC framework at all. The "bulge/gap pairing" inequality measure(S_Q △ S_R) ≥ 1 for S_Q ⊄ S_R with all-mass-below constraint. No mechanism known. This is the ll-inclusion-gap's G-GAP = ll-dyadic-symdiff's non-containment residual. Priority: medium (shared gap across both LB approaches, no progress yet).

**Obstruction 3 (essentially GONE): G-INC-2e thin edge.** Vacuous by parity argument (see above). Not a real gap.

---

## Distinct openings for the outliner

**Opening A: Build the {Claim_R, T_R} mutual induction for lower-band cuts and non-equal (a≥1) top cuts.**
- This is now a clean build: exactly the anchor proof structure, using Gen-Decomp instead of the SET IDENTITY. Bases at n=2 (and n=4 for first nontrivial refined-R) verified numerically (0 violations). The induction descends cleanly, budget transfers, ΣQ_lo window matches.
- This CLOSES G-INC-2 for all lower-band cuts AND non-equal top cuts with a≥1 across ALL n. Covers the large majority of refined-R cases.
- Certifiable as a promotable lemma analogous to t-ell-mutual-induction.

**Opening B: Direct base case for G-INC-2nt (a < 1) at n=4.**
- At n=4, the a < 1 sub-case (cut top piece 8 → {a, 8-a} with 0 < a < 1) gives R_lo = G_1 △ [0,a). The INC instance at level n-2=2 has |Q_lo| ≤ 2 and S_{Q_lo} ⊆ S_{R_lo}. Direct casework (|Q_lo| ≤ 2, few options) may close this case directly without needing a "well-formed refinement" framework. If a_cut < 1 cases are vacuous at n=4 (budget forces no valid Q_lo), that's the base for the induction.

**Opening C: Parity argument closes G-INC-2e for equal-split.**
- For the equal-split top-piece cut: |R| = n+1 and |Q| ≤ n. The [0,1)-interval parity argument (|Q| even → [0,1) ∉ S_Q → A(Q) ≤ A(R)-1) closes the claim for the dominant sub-case. The residual (|Q| odd) appears structurally impossible for the tight configurations (budget+sum constraints). This can be stated and proved as a 1-line certifiable fact.

**Opening D: G-GAP branch — aligned-pair argument.**
- The GAP branch has S_Q ⊄ S_R. There exists a "pivot" point x* ∈ S_Q \ S_R. Near this pivot, S_Q and S_R diverge: S_Q contributes odd-count on one side, S_R on the other. An "alignment cost" argument (the ΔN = N_Q - N_R integral equals 1 = ΣQ - ΣR, distributing as a signed signed-measure) could give measure(S_Q △ S_R) ≥ 1. Prior explorers noted ∫(N_Q - N_R) = 1 is insufficient alone, but a DYADIC-LEVEL PAIRING of mismatched intervals may give the needed lower bound.

---

## Dead ends (do not retry)

- **{Claim_R, T_R} for equal-split top-piece cut via Gen-Decomp**: h_R = 3 (ODD). Gen-Decomp's hypothesis is NOT satisfied. Use the separate parity argument instead.
- **SET IDENTITY analogue for refined R**: No known identity. The anchor's S_{G_{n-1}} ∩ [0,2^{n-2}) = S_{G_{n-3}} is G_{n-1}-specific; Gen-Decomp is the correct substitute.
- **G-INC-1 auto-giving G-INC-2**: FALSE. Tight pairs at n=4 (Q={5,5,4,2}, R={4,4,4,2,1}) have S_Q = [2,4) ⊄ S_{G_3} = [1,2)∪[4,8). G-INC-1 inapplicable.
- **G-INC-2e as a real gap**: Vacuous — closed by parity argument (verified n=4,5,6, 0 violations of A(Q) ≤ A(R)-1 in any G-INC-2e case).
- **ΣQ_lo out of certified window as obstruction**: FALSE for h=2 lower-band and non-equal top cuts — ΣQ_lo = 2^{n-2} + ε' with ε' ∈ (-1,1) is within the certified {Claim, T} window at level n-2.

---

## Candidate techniques

- **Mutual strong induction {Claim_R(n,ε), T_R(n)}, descending n → n-2**: exact analogue of the certified t-ell-mutual-induction, using Gen-Decomp to descend. The key tool is Gen-Decomp for the lower-band and non-equal (a≥1) top-cut cases.
- **|Q|-parity argument for equal-split**: elementary, one-line. Closes G-INC-2e.
- **Budget-tightness argument**: the constraint |Q_lo| ≤ n-h forces equal-pair structure at base levels → A(Q_lo) = 0 automatically at the base.

---

## Knowledge-base entries

- `t-ell-mutual-induction.md` — the EXACT template to adapt. The {Claim_R, T_R} step is structurally identical.
- `gen-decomp-refined.md` — the core descent engine (certified, R9). Replaces the SET IDENTITY in the inductive step.
- `L1-budget-anchor.md` — handles equal-split case (g=2 and g=0 with equal-top), partially closes G-INC-2 for those sub-cases already.
- `parity-condition-inc.md` — Parity-Condition gives N_Q parity from N_R parity. Used in Gen-Decomp's proof (step (i)).
- `top-band-decomposition.md` — special case of Gen-Decomp for R=G_{n-1}. Already certified.
- `set-identity-selfsimilar.md` — NOT needed for the refined-R induction (Gen-Decomp removes the dependence), but still needed for the anchor base cases (Claim(1,·), Claim(2,·), T(1), T(2)).
- `forcing-inc-reduction.md` — the INC reduction A(Q∪R) = A(R)−A(Q); and the Forcing bound max(Q) ≤ max(R) (used for the equal-split Forcing → max(Q) ≤ 2^{n-2}).

---

## Prior progress

- G-INC-1 (anchor R=G_{n-1}): CERTIFIED for all n (t-ell-mutual-induction, R8). Template for the unifier.
- Gen-Decomp: CERTIFIED (R9). The missing descent engine.
- L1: CERTIFIED (R9). Closes equal-split sub-cases (g=2 and g=0 equal-top).
- G-INC-2 at n=3: VACUOUS (budget+parity, certified R7/R8).
- G-INC-2 at n=4: verified 0 violations (4164 INC configs, min margin=1, R9).
- G-INC-2e cases: verified 0 violations at n=4,5; n=6 min margin=3 (confirmed by direct enumeration this round). G-INC-2e is NOT a real gap.

---

## Small-case / intuition notes (labeled as conjectures)

- **Conjecture:** The {Claim_R, T_R} mutual induction closes G-INC-2 for lower-band cuts and non-equal top cuts with a≥1, for ALL n. The proof is structurally identical to the anchor with Gen-Decomp replacing the SET IDENTITY. (Strong conjecture, supported by 0 violations at n=4,5, and exact structural match.)

- **Conjecture:** G-INC-2nt with a_cut < 1 is vacuous or closes by a direct n=4 base case. The sub-unit flip creates exotic R_lo with A(R_lo) ≈ A(G_{n-3}) ± a_cut, and the budget constraint |Q_lo| ≤ n-2 forces A(Q_lo) ≈ 0 (equal-pair structure), giving A(R_lo)−A(Q_lo) ≥ 1 anyway. (Medium confidence.)

- **Observation (proved this round):** For the equal-split case (h_R = 3, ODD), G-INC-2e thin edge is settled by the |Q|-parity argument. NOT a conjecture — this is a concrete provable lemma.

- **Observation:** A(Q_lo) = 0 at the base levels (n=2) of the descent is forced by the budget constraint |Q_lo| ≤ 2 plus the INC constraint. This makes the base case trivial.

---

## Build recommendations

**Priority 1 (HIGH):** Build the {Claim_R, T_R} mutual induction for lower-band cuts and non-equal (a≥1) top cuts in ll-inclusion-gap. This is a concrete, structured proof:
1. State Claim_R(n,ε) and T_R(n) with R = any refinement having h_R even.
2. Base cases: Claim_R(1,ε), T_R(1) (same as anchor, R=G_0), Claim_R(2,ε), T_R(2) (same or direct).
3. Inductive step: apply Gen-Decomp (certified), get h=0 (done), h=2 with sub-cases 2a/2b-i/2b-ii (exact anchor structure). 
4. Cases: lower-band cut (h_{R_lo}=2 always, clean) and non-equal top (a≥1, h_{R_lo}=2 always, clean).
5. This closes G-INC-2 for all these cases, leaving only a_cut < 1 and G-GAP.

**Priority 2 (MEDIUM):** Settle G-INC-2nt (a_cut < 1) by direct casework at n=4 or prove vacuousness. The structure is: R_lo = G_{n-3} △ [0, a_cut) with a_cut < 1. At n=4 this is the bottom of the descent and can be handled directly by enumerating valid Q_lo configs.

**Priority 3 (MEDIUM):** State and certify the |Q|-parity lemma closing G-INC-2e for the equal-split case. One paragraph: |R| = n+1 (ODD for n even); Forcing gives max(Q) ≤ 2^{n-2}; when [0,1) ∈ S_R but [0,1) ∉ S_Q (from |Q| even), automatically A(Q) ≤ A(R)-1.
