## imo-2026-03 — UB hard case (c) for m≥5 [lens: UPPER-BOUND PURE HARD CASE]

### Problem recap
Inequality (T): For m distinct pieces p₁>p₂>…>p_m, Σ=(2^m−1)t, budget b=m−1, gap-case conditions
(1) p₁≤Σ/2, (2) p₂<2^{m−2}t, all dⱼ=pⱼ−pⱼ₊₁>t, δ=p_m>t: prove μ(X,m−1)≤t.
T4 (m=4) is certified. Open: m≥5 (a single self-contained finite inequality).

---

### Distinct openings for case (c)

**Opening A — Double invisible pair (NEW, not in any prior approach).**
A "double invisible pair" occurs when some cut p_i@p_j creates fragment v=p_i−p_j that equals another existing piece p_k.
One physical cut eliminates THREE effective pieces (p_i, p_j, p_k all cancelled in pairs), reducing to an m−2-piece subproblem with budget m−2 remaining: Lemma AB closes it (μ=0) or Lemma MK/R4 does.

Numerical finding (denom=4, 1551 hard configs for m=5): **67.4% of hard configs (1046/1551) have at least one such triple (i,j,k)**.
These are covered in one step without any T4 machinery.

The remaining 32.6% (505 configs) have all differences p_i−p_j distinct from all pieces (generic case). This is the real frontier.

**Opening B — Pair1_2 + T4-at-t for the generic (no-double-pair) case.**
After cutting p₁ at offset p₂ (pair1_2), the 4-piece subproblem Y'={d₁,p₃,p₄,p₅} has Σ'=Σ−2p₂>(2^{m−1}−1)t (from condition (2): Σ−2·2^{m−2}t=(2^m−1)t−2^{m−1}t=(2^{m−1}−1)t). Apply T4's R/S/P/C strategies at threshold t (not Σ'/15).

Numerical finding (denom=4, no-DP configs): **96.8% (489/505) of no-DP hard configs are closed by pair1_2 + T4-at-t**.

The failures of pair1_2+T4 are always one of: T4 Sub-B C fires with A_C>t, or T4 Sub-A C fires with A_C>t (never R, S_e3, S_sym, or P fail).

**Opening C — Fallback non-adjacent cuts for pair1_2-fail region.**
The remaining 3.2% (16/505 no-DP configs, ~1% total) all yield to some other first cut + T4-at-t:
- Sub-B C_SubB_FAIL (e₃>e₁ in Y', A_C=δ+d₄−|d₁−p₃|>t): cut_1@3 (p₁@p₃) works for 13/20 Sub-B cases; cut_2@3, cut_2@4, cut_2@5 cover the rest. Most common T4 sub-cases after these cuts: S_sym, S_e3, R.
- Sub-A C fail (d₁>p₃ but eps+e₃−e₁>t): cut_2@3 (pair2_3) works via T4 P strategy, giving A=d₂/2.
Together: **0 failures across 1551 denom=4 hard configs** (and confirmed 0 for denom=5, 70,722 fractional configs in prior session).

**Opening D — Direct extended case split for m=5 (analogue of T4).**
T4's proof: 4 strategies + case split (Cases 1/2/3 easy, Sub-B vacuous, Sub-A P/C). For m=5: Sub-B is NOT vacuous (see below), requiring 2−3 first-cut options. The proof structure:
- Step 1 (double pair): if some (i,j,k) triple exists, one cut + AB/MK closes.
- Step 2 (pair1_2 → easy T4 sub-cases): R, S_e3, S_sym close via MK.
- Step 3 (pair1_2 → Sub-A): P works when δ≤2t (analytic bound needed); C works when d₁−p₃≥δ+d₄−t.
- Step 4 (pair1_2 Sub-B): try cut_1@3 → S_sym (analytic bound: |d₁+d₂−p₃|≤t or similar).
- Step 5 (both fail): cut_2@3 P with A=d₂/2≤t (need d₂≤2t from some condition).

**Opening E — Induction bypassing threshold-invariant. (CAUTION: prior induction refuted.)**
The threshold-invariant induction (subproblem inherits (2'): 2nd piece <2^{m−3}t) was rigorously refuted in R11. Do NOT revive. However, a WEAKER induction might work: after pair1_2, the subproblem inherits condition (1) (max≤Σ'/2, certified) and Σ'>(2^{m−1}−1)t (certified). If a T_{m−1} lemma for NON-GAP-CASE or WEAKER conditions can be proven, induction goes through. Untested territory — risky.

---

### Where T4's Sub-B vacuousness breaks for m=5

T4 Sub-B vacuousness used: from condition (2') for m=4: "7d₂+3d₃<δ+4d₁", combined with d₂,d₃>t, to derive δ+d₁<2t, giving contradiction with 10t<δ+d₁.

For m=5: condition (2) gives p₂<8t, translating to a WEAKER constraint on the subproblem after pair1_2. Specifically: δ=p₅<p₂<8t and d₁+d₂+d₃+d₄<p₂<8t. No analogue of "δ+d₁<2t" is provable. Sub-B DOES fire (confirmed: configs p=[8,7,6,5,4] and family with large δ).

The Sub-B C_SubB_FAIL pattern: e₃=d₄>e₁=|d₁−p₃| and A_C=δ+d₄−|d₁−p₃|>t. This occurs precisely when d₁ is "near" p₃ (within δ+d₄−t of p₃). The typical fix: cut_1@3 creates S_sym (|d₁+d₂−p₃|≤t for balanced configs) or S_e3.

---

### Key analytical gap needing a lemma

**Sub-A P failure**: In Sub-A P (d₁>p₃, d₁−p₃≥p₄, P gives A=δ/2), δ≤2t is NOT automatically guaranteed by the m=5 hard case conditions alone. Example: d₁=8.6t, d₂=d₃=d₄=1.1t, δ=2.5t satisfies all hard case conditions, yields Sub-A P with A_P=1.25t>t. This config is NOT caught in the integer grid (denom=4 requires integer multiples of 0.25 with t=Σ/31 rational), explaining the 0 failures in the grid — but continuous real-valued inputs ARE the actual problem.

**Fix for this case**: pair2_3 gives A=d₂/2=0.55t<t in the example. But pair2_3 P gives A=min_piece/2, and min_piece might be δ or d₂ depending on the sorted order. Need: when δ>2t AND pair1_2 Sub-A P fires (d₁≥p₃+p₄), prove pair2_3 gives A≤t. This is the most important UNPROVEN analytical sub-lemma.

**Claim (unproved, strongly supported numerically)**: In the m=5 hard case, if pair1_2's T4 Sub-A P fails (δ>2t), then pair2_3 gives a subproblem where T4's minimum-piece (in pair2_3 subproblem) ≤2t.

Partial evidence: From inequality (*): d₂+2d₃+3d₄+3δ≤31t/2. With δ>2t and d₂+d₃+d₄ taking their minimum values (slightly above 3t): d₂≈31t/2−2d₃−3d₄−3δ. For δ=2.5t and d₃=d₄=t+ε: d₂≈31t/2−5t−7.5t−εs=3.5t−εs<3.5t. So d₂<3.5t. For d₂<2t to hold: need either a tighter bound or pair2_3 to fire some non-P sub-case when d₂>2t.

---

### Candidate techniques

- **Double invisible pair mechanism**: A single cut can eliminate 3 effective pieces when p_i−p_j=p_k. Covers 67% of hard cases. Needs to be characterized: which arithmetic conditions on the gaps guarantee a triple exists?
- **Multi-first-cut strategy**: T4 used a fixed set of strategies; T5 needs a case-split based on WHICH first cut is available. This is analogous to T4 but with one more dimension.
- **T4 R/S strategies as "gap detectors"**: R and S fire when some gap ≤t in the subproblem. The S_sym strategy (|e₁−e₃|≤t) is particularly versatile and fires after cut_1@3 in many Sub-B fail cases.
- **Pair2_3 as fallback for large-δ Sub-A P fails**: When δ>2t causes Sub-A P to fail, cut p₂@p₃ creates a subproblem with new minimum piece d₂=p₂−p₃, and P gives A=d₂/2.

---

### Cheap-kill candidates

- **Double pair pre-check**: Before any case split, check if any (i,j,k) triple exists with p_i−p_j=p_k. This is a cheap Θ(m³) check and closes 67% of hard cases immediately.
- **Gap ≤ t in the pair1_2 subproblem**: After pair1_2, if any gap in {d₁,p₃,p₄,p₅} is ≤t, MK (Corollary MK.1) closes immediately. Fires for ~65% of hard cases (including double-pair and easy T4 sub-cases).
- **Condition-dependent bound on δ**: From the P condition d₁≥d₃+2d₄+2δ and condition (1), one can bound δ. Find the exact constraint: when d₁≥d₃+2d₄+2δ is compatible with cond(1) and δ>2t.

---

### Knowledge-base entries to use

From `knowledge_base.md`:
- **Parity-invisibility / Pairing cuts (Lemma R1)**: The fundamental tool for all strategies.
- **Certified Lemma MK**: μ(k,k−1)≤min(pieces). Handles all easy sub-cases after a first cut.
- **Certified Lemma T4**: R/S/P/C strategies for 4-piece subproblem. Applied at original threshold t (not subproblem's own t') — this is the key non-obvious application.
- **Certified Lemma AB**: μ(X,b)=0 for b≥|X|. Handles double-pair reduced subproblems.
- **Certified Lemma R4 (gap-case-m3-closure)**: Closes m=3 after double-pair reduction.
- **Case A.A**: p₁>Σ'/2 in subproblem closes by subtract-all chain. May fire after non-adjacent cuts.

---

### Analogous past problems (cruxes)

None found precisely analogous to the "m≥5 multi-strategy game theory" structure. The T4 proof itself (certified) is the closest template — the extension challenge is whether T5 can be proven by adding cases rather than by induction.

---

### Prior progress

- **m≤3**: Closed by certified Lemma R4 (gap-case m=3) + MK/AB.
- **m=4**: Closed by certified T4 (strategies R/S/P/C, Sub-B vacuous).
- **m≥5 easy sub-cases**: Closed by certified MK.1 (any gap dⱼ≤t or δ≤t), Lemma AB (budget≥pieces), Case A.A (p₁>Σ/2).
- **Pure hard case m≥5**: OPEN. Numerically verified (0 violations, 70,722 fractional configs for m=5). Two-cut strategies (pair1_2 OR fallback) always work. No clean analytic proof.

---

### Dead ends (do not retry)

- **SB-monotone reduction**: rigorously refuted, R7 (sb-obstruction theorem). Never revisit.
- **R3-cascade actual-A potential**: refuted R8.
- **Complement-cut m=4→3→R4**: refuted R9.
- **Threshold-invariant induction {(I'),(II'),(III')}**: rigorously refuted R11. Subproblem after pair1_2 does NOT inherit condition (2') p₂'<2^{m−3}t. Witness: X={8,4,3,2,1}.

---

### Small-case / intuition notes (all labeled conjecture unless certified)

1. **[Conjecture, strongly supported]** For m=5 hard case with real-valued gaps satisfying all conditions, either (a) a double invisible pair exists, or (b) pair1_2+T4-at-t works, or (c) pair2_3+T4-at-t works. This covers all cases with at most 2 first-cut choices.

2. **[Conjecture, supported by denom=4,5 grids]** The critical Sub-A P failure (δ>2t) only occurs when pair2_3 gives A≤t via P with min_piece=d₂<2t. Equivalently: δ>2t forces d₂<2t in the hard case. This would be the KEY MISSING LEMMA.

3. **[Observed]** The Sub-B fail region (pair1_2 C_SubB_FAIL) is characterized by d₁ being within distance δ+d₄−t of p₃. In this region, cut_1@3 (creating new piece d₁+d₂) tends to give S_sym (|d₁+d₂−p₃|≤t for balanced gaps) or S_e3. The arithmetic reason: d₁+d₂=p₁−p₃ and p₃ in the new subproblem, so |p₁−p₃−p₂|=|p₁−p₂−p₃|=|d₁−p₃|<t (if d₁≈p₃). This means S_sym fires when d₁≈p₃ (the exact Sub-B fail condition!). So Sub-B fail → cut_1@3 S_sym has a natural duality.

4. **[Observed]** For the 16 no-DP pair1_2-fail configs in the integer grid: ALL have working cuts with A=exactly 1 (not a fraction). This suggests the "tight" configs in the residual hard case may have integer structure that simplifies the proof.

5. **[Analytical note]** For general m, the double-pair mechanism gives a DIRECT reduction to m−2 pieces with 1 cut. If ALWAYS applicable, this would prove T_m by induction from T_{m−2} with no new strategy needed. The question: does every m-piece hard case have a double-pair cut? Numerical answer for m=5: NO (32.6% lack one). For m=6,7: untested.

6. **[Analytical note, Sub-A C bound]** In Sub-A with d₁>p₃ and d₁−p₃∈(d₄, d₄+p₅) (C applies, not P): A_C=p₅+d₄−(d₁−p₃). For A_C≤t: d₁≥p₃+d₄+p₅−t. Since d₁>p₃+d₄ (Sub-A with P not applying means... wait P is d₁≥p₃+p₄=p₃+d₄+p₅, so C means d₁<p₃+p₄=p₃+d₄+p₅). So A_C=p₃+p₄−d₁=p₃+d₄+p₅−d₁∈(0,p₅). For A_C≤t: d₁≥p₃+d₄+p₅−t. This is NOT guaranteed from the hard case conditions alone. From condition (1): d₁≤31t/2−p₂. For d₁≥p₃+d₄+p₅−t to follow from condition (1): would need 31t/2−p₂≥p₃+d₄+p₅−t, i.e., 31t/2+t≥p₂+p₃+p₄=Σ−p₁−p₅. With p₁≤Σ/2=31t/2 and p₅=δ: Σ−p₁−p₅≥31t−31t/2−p₅=31t/2−p₅. So condition gives 33t/2≥31t/2−p₅... this doesn't help directly. The Sub-A C case needs a separate argument.
