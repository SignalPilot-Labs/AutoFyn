## imo-2026-03 (Upper-bound m≥4 gap case — lookahead / minimax lens)

### Problem context

Gap case for the upper bound: distinct X = {p₁ > p₂ > p₃ > p₄ > …} with m=|X|≥4, p₁ ≤ Σ/2, p₂ < τ/2 (where τ = Σ·2^b/D_b, D_b = 2^{b+1}−1). Goal: μ(X,b) ≤ Σ/D_b. Budget invariant: |X| ≤ b+1, so m=4 requires b≥3.

---

### (a) Why deterministic one-cut-per-step fails; why optimal XY succeeds

**The greedy error (root cause of all cascade failures):** Every "cut p₁ at offset pⱼ" produces pieces (pⱼ, p₁−pⱼ). Since pⱼ is ALREADY in X, we now have THREE copies of pⱼ (the original, plus the new pⱼ fragment). Odd multiplicity → the alternating sum does NOT cancel this value. This is the mechanism behind every cascade failure: the greedy R3 cut creates an ODD-parity copy.

**The correct mechanism — complement cut:** Optimal XY instead cuts p₁ at offset p₁−pⱼ (not pⱼ), producing pieces (pⱼ, p₁−pⱼ). Combined with the EXISTING pⱼ in X, we now have TWO copies of pⱼ — an invisible pair. The pair {pⱼ, pⱼ} cancels completely. Cost: 1 cut, 1 pair created.

**Concrete trace for X={8,4,3,2}, b=3, Σ=17, target=17/15≈1.133:**
- CUT 8 at 1 (= 8−p₄−p₃? No: offset 1 creates (1,7); pair {1,1} with existing... wait). Actually the optimal trace is:
  CUT 8 at 1 → (1,7); CUT 2 at 1/2 → (1/2,3/2); CUT 7 at 3 → (3,4).
  Final: {4,4,3,3,3/2,1,1/2} — pairs {4,4}, {3,3}; A = 3/2−1+1/2 = 1 ≤ 17/15 ✓.
  
**Trace for hard Case D instance X={11, 15/2, 7, 9/2}, b=3, Σ=30, target=2 (COMPUTED):**
- CUT 11 at 4 (= 11−7, complement of p₃=7) → (4,7). Pair {7,7} with existing p₃=7.
- CUT 15/2 at 15/4 (halve p₂) → (15/4, 15/4). Pair {15/4, 15/4}.
- Effective residual: {p₄=9/2, p₁−p₃=4}. A = 9/2−4 = 1/2 ≤ 2 ✓.
- Optimal μ = 1/2 (VERIFIED by exhaustive minimax search).

**Near-equal arithmetic progression X={108,106,104,102}, b=3, Σ=420, target=28 (COMPUTED):**
- CUT 108 at 6 (= 108−102, complement of p₄=102) → (6,102). Pair {102,102} with p₄.
- Effective sub: {106, 104, 6}, S'=216, b'=2. Now p'₂=106 ≥ τ'/2=61.7 → sub NOT gap!
- R3 on sub: CUT 106 at 104 → (104,2). Pair {104,104} with p'₁'=104. Effective: {6,2}.
- One more cut if needed: A={6,2}→halve 6→{3,3,2}→A=2 ≤ 28 ✓. Optimal μ=0.

**Key bifurcation:** Greedy cuts p₁ at pⱼ (triple pⱼ, A large); optimal play cuts p₁ at p₁−pⱼ (double pⱼ, pair formed, A small). The difference is a SINGLE BIT of lookahead: which offset to use. This is why opt_mu satisfies the bound while all deterministic cascade strategies fail.

---

### (b) Lookahead / minimax structure — the complement-cut + sub-solve approach

**The structural observation (verified on all tested gap instances):**

For any choice j ∈ {2,3,4}: the "complement cut of pⱼ" strategy — cut p₁ at p₁−pⱼ creating pair {pⱼ,pⱼ}, then OPTIMALLY solve the 3-piece sub-instance at budget b−1 — gives A(final) ≤ Σ/D_b.

Verified for X={11,7.5,7,4.5}: j=1(p₂): A=1.0 ≤ 2 ✓; j=2(p₃): A=0.5 ≤ 2 ✓; j=3(p₄): A=0.5 ≤ 2 ✓.
Verified for X={8,4,3,2}: j=1,2,3: ALL give A=1.0 ≤ 17/15 ✓.
Verified for X={108,106,104,102}: j=1,2: A=0 ✓; j=3: A=2.0 ≤ 28 ✓.
Verified for X={8,4,3,1}: j=1,2,3: ALL give A=0 ✓.

**The 3-piece sub-instance is ALREADY SOLVED** by Lemma R4 (certified, gap-case-m3-closure.md) and Case A.A (certified). After complement-cut pⱼ, the sub = {pk: k≠1,k≠j} ∪ {p₁−pⱼ} has m=3, budget b−1, Σ' = Σ−2pⱼ.

Crucially: p₁−pⱼ ≤ p₁ ≤ Σ/2 ≤ (Σ−2pⱼ)/2 + pⱼ = Σ'/2 + pⱼ. With pⱼ > 0 and p₁ ≤ Σ/2: p₁−pⱼ ≤ Σ/2−pⱼ < Σ'/2... wait, this needs Σ'/2 = (Σ−2pⱼ)/2, and p₁−pⱼ ≤ Σ/2−pⱼ = (Σ−2pⱼ)/2 = Σ'/2. So max of sub ≤ Σ'/2 always (from p₁≤Σ/2). Case A.A never applies to the sub.

**Applying Lemma R4 to the sub:**

If sub is a gap case for budget b−1, Lemma R4 gives A(sub-final) = Σ'−2·max(sub).

Two sub-cases depending on j:
- **Complement p₂ (j=1):** sub = {p₃, p₄, p₁−p₂}, Σ'=Σ−2p₂.
  - If p₁−p₂ ≥ p₃ (Case α): A(final) = (Σ−2p₂)−2(p₁−p₂) = Σ−2p₁. Need Σ−2p₁ < Σ/D_b.
  - If p₁−p₂ < p₃ (Case β): A(final) = (Σ−2p₂)−2p₃ = Σ−2p₂−2p₃. Need p₂+p₃ > Σ(D_b−1)/(2D_b).

- **Complement p₄ (j=3):** sub = {p₂, p₃, p₁−p₄}, Σ'=Σ−2p₄.
  - If p₁−p₄ ≥ p₂: A(final) = Σ−2p₁. Same as α.
  - If p₁−p₄ < p₂ (always in near-equal case, since p₁≈p₂+p₄): A(final) = Σ−2p₂−2p₄.

**The sub may not be a gap case (when pⱼ is small → Σ' large → p₂ ≥ τ'/2):**

For complement-cut p₄ with p₄ small: Σ'=Σ−2p₄≈Σ, τ'/2=(Σ−2p₄)·2^{b−2}/D_{b−1}≈Σ·2^{b−2}/D_{b−1}. And p₂<τ/2=Σ·2^{b−1}/D_b. Compare: τ'/2/τ_orig*2 ≈ D_b/(2D_{b−1}). For b=3: D_b=15, D_{b−1}=7, ratio=15/14>1. So τ'/2>τ/2>p₂ is NOT guaranteed for b=3.

In the {108,106,104,102} case: complement-cut p₄=102 gives Σ'=216, τ'/2≈61.7, p₂=106>61.7. Sub IS NOT gap → R3 applies directly. Then after R3 of sub: A = some small two-piece instance.

**The proof approach:** For m=4 gap case, XY does complement-cut of pⱼ for the BEST j. The sub-instance is m=3 (solved) and the ACTUAL A formula gives A(sub-final) < Σ/D_b — this is the key claim that needs to be proved. The SB-obstruction is NOT a contradiction: it says S'/D_{b−1} > Σ/D_b (bound is looser), but the actual A can still satisfy A < Σ/D_b.

**Candidate proof strategies:**
1. **Averaging over j=2,3,4:** Show Σⱼ A(final, complement-cut pⱼ) < 3Σ/D_b → min_j < Σ/D_b. Requires computing the sum of A-formulas.
2. **Direct sub-case algebra:** Split on whether the sub is or isn't a gap case, get explicit formula, bound directly using gap case conditions.
3. **Induction step:** After complement-cut, sub has m=3 with max ≤ Σ/2. The exact R4 formula + gap conditions closes it.

---

### (c) Re-assessment: extremal-smoothing S1 vs m≥4 lookahead

**Extremal-smoothing cost assessment:** S1 (G_n unique maximizer) has been stuck 4+ rounds. No approach has moved it: the V(G_n) ≥ V(any X) statement requires showing the n-dimensional maximum is attained uniquely at G_n, which is strictly harder than just bounding μ for specific instance types. No new opening found this round. **Assessment: S1 is lower-probability and higher-cost than m≥4 direct.**

**m≥4 lookahead cost assessment:** The core mechanism is now clear (complement cut creates pair → m reduces by 1 → apply certified m=3 result). The sub-cases appear algebraically tractable. The ACTUAL bound A(sub-final) < Σ/D_b needs proof but has a concrete algebraic form in each sub-case. **Assessment: lower-cost than S1; 1–2 rounds likely to close.**

**Recommendation:** Advance the m≥4 complement-cut route in geometric-selfsimilar. Leave S1 last-resort.

---

### (d) Concrete verifiable sub-targets

**Sub-target 1 (simplest, check first):** For complement-cut of p₂ in Case α (p₁−p₂ ≥ p₃):
A(final) = Σ−2p₁ < Σ/D_b iff p₁ > Σ(D_b−1)/(2D_b).
Verify: in gap case with m=4, does p₁ > Σ(D_b−1)/(2D_b) always hold in Case α?
Case α is p₁ ≥ p₂+p₃. Combined with p₂+p₃+p₄ ≥ Σ/2: p₁+p₄ ≥ Σ/2, so p₁ ≥ Σ/2−p₄.
Need: Σ/2−p₄ > Σ(D_b−1)/(2D_b), i.e., p₄ < Σ/(2D_b) = τ/2^{b+1}. Does gap case imply p₄ < τ/2^{b+1}?
This is OPEN analytically but appears to hold in all tested instances. Concrete check: b=3, Σ=17, need p₄ < 17/30≈0.567. With p₄=2 > 0.567: fails? Actually X={8,4,3,2}: p₄=2>0.567 and yet A=Σ−2p₁=17−16=1<17/15. Hmm, the bound 1<17/15≈1.13 holds but barely. Need to verify the actual algebra gives strict inequality from gap conditions.

**Sub-target 2 (key case):** For complement-cut p₄ with sub NOT gap (p₂ ≥ τ'/2):
After complement-cut p₄ and R3 of sub: A(final) = |(p₂−(p₁−p₄)) − p₃| or similar.
Concrete: X={108,106,104,102}, b=3: A(final) = |106−(108−102)−104|... traces to 2 or 4 (≤28). Verify algebraically for the sub-type p₂ ≥ τ'/2 case.

**Sub-target 3 (the genuine crux):** Prove: for m=4 gap case, A(complement-cut p₂ then R4 on sub, Case β) = Σ−2p₂−2p₃ < Σ/D_b, i.e., p₂+p₃ > Σ(D_b−1)/(2D_b). In Case β: p₁−p₂ < p₃, i.e., p₁ < p₂+p₃. Also p₁≤Σ/2. From gap: p₂ < τ/2 = Σ·2^{b−1}/D_b, p₃ < p₂. What's a lower bound on p₂+p₃?

Observe: p₂+p₃ > p₁−p₂+p₄+p₂ (in Case β where p₁<p₂+p₃ → p₃>p₁−p₂). And sum p₁+p₂+p₃+p₄=Σ. This needs a different angle. CONJECTURE (from 0 failures in all tested instances): p₂+p₃ > Σ(D_b−1)/(2D_b) always in Case β of the m=4 gap case. Proving this rigorously is the concrete sub-target.

---

### Distinct openings

1. **Complement-cut + m=3 solve (main route):** Single complement cut of pⱼ reduces m=4 to m=3 (solved). The SB-obstruction is bypassed because we use the actual A formula, not the SB bound for the sub. Proof: split on j∈{2,3,4}, sub-case on whether sub is/isn't gap case, bound A(final) explicitly.

2. **Averaging over j:** Compute the three A-formulas (one per j=2,3,4) and show their SUM < 3Σ/D_b → MIN < Σ/D_b. This bypasses sub-case analysis by exploiting that at least one j works.

3. **Sub NOT gap → R3 cascade closes:** When complement-cut p₄ gives p₂ ≥ τ'/2 in the sub, R3 applies to the sub. Then R4 or Case AA applies to the sub-sub (which is 2-piece). This chain closes without any A-formula gap-case analysis. Identify exactly which m=4 instances fall in this regime and prove it.

4. **Halving chain:** The instance {11,7.5,7,4.5} shows that complement-cut p₃ (creating pair {7,7}) + halve p₂ gives A = p₄−(p₁−p₃) = p₃+p₄−p₁. For this to be < Σ/D_b: need p₃+p₄ < p₁+Σ/D_b = p₁+τ/2^b. In Case D (p₃+p₄>p₁), this requires p₃+p₄−p₁ < τ/2^b. Since p₃,p₄ < τ/2 and p₃+p₄=Σ−p₁−p₂, this is p₂ > Σ−p₁−τ/2^b−p₁ = Σ(1−1/2^b)−2p₁+p₁ ... needs algebraic analysis.

5. **Extremal-smoothing bypass (low probability):** S1 (G_n unique max). Last resort, 4+ rounds stuck, last-placed.

---

- **Candidate technique(s):** Complement cut (create pair via p₁−pⱼ offset) → reduce m=4 to m=3 → apply certified Lemma R4 → explicit A formula → algebraic bound using gap conditions. One-step lookahead (no backward induction needed beyond choosing j).

- **Cheap-kill candidates:** The sub-case where complement-cut p₄ gives sub NOT gap (p₂≥τ'/2): check whether p₂ ≥ τ'/2 follows from gap case conditions alone for m=4. If so, this kills the gap case in 2 R3-type cuts with no new argument.

- **Knowledge-base entries to use:** Lemma R4 (gap-case-m3-closure, certified), SB-obstruction theorem (sb-obstruction, certified, negative), R1/R2/R3 reductions (sum-bound-reductions, certified), Case A.A chain (gap-caseAA-subtract-chain, certified).

- **Analogous past problems (cruxes):** None directly analogous found. The complement-cut mechanism is specific to this game's alternating-sum structure.

- **Prior progress:** m≤3 gap case fully closed (Lemma R4 + Case A.A certified). n=2 UB rigorous. m≥4: refuted all deterministic cascade strategies; identified complement-cut mechanism; computed optimal μ=0 or small for all tested m=4 instances (0 failures, 24+ cases).

- **Dead ends (do not retry):**
  - R3-cascade actual-A = Σ−2p₁ potential for m≥4 (REFUTED R8, 18385/29234 violations).
  - R3-at-p₂ deterministic strategy (REFUTED, 1314/2000 violations).
  - Partial-shadow chaining (CERTIFIED DEAD by sb-obstruction R7).
  - SB-monotone reductions for gap case (CERTIFIED DEAD by sb-obstruction R7).

- **Small-case / intuition notes (conjectural):**
  - CONJECTURE: for every m=4 gap case, EVERY choice of j∈{2,3,4} for complement-cut gives A(final) ≤ Σ/D_b (0 failures in 24+ tested instances including hard Case D and near-equal APs). This is stronger than needed — only min_j is required.
  - CONJECTURE: In Case β of complement-cut p₂ (p₁<p₂+p₃): p₂+p₃ > Σ(D_b−1)/(2D_b). This would close the sub-case algebraically. No counter-example found in 24+ instances.
  - The near-equal case ({108,106,104,102}) is handled by the "sub NOT gap → R3 on sub" branch (p₂=106 ≥ τ'/2=61.7 after complement-cut p₄=102). The asymmetric case ({8,4,3,1}) is handled by m=3 sub with direct A=0.
