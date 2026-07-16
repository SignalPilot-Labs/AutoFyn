## imo-2026-03 — Upper-bound finite inequality (T) — lens: algebraic/computational

### 1. Precise restatement of (T)

**Setting** (tight budget, residual gap case): X = {p₁ > p₂ > p₃ > p₄} four distinct positive reals, Σ = Σpᵢ, b = 3 = m−1 (m = |X| = 4), D₃ = 15 = 2⁴−1, τ = 8Σ/15.

**Gap conditions**: p₁ ≤ Σ/2 (residual, already closed for p₁ > Σ/2 by Case A.A) and p₂ < τ/2 = 4Σ/15. Note p₁ ≤ Σ/2 implies p₁ < τ automatically (since τ = 8Σ/15 > Σ/2), so the two gap conditions reduce to just these two.

**Merge-family**: XY performs exactly 2 "pairing steps" (each cuts the larger of two chosen pieces at the offset equal to the smaller piece, creating an invisible pair, budget cost = 1 cut) to reach a 2-piece effective instance {u, v} with u ≥ v > 0, then applies one final cut (either cut u at v for leftover u−v, or halve u for effective piece v). Equal-pair collapses at any step cost 0 cuts (free).

**Inequality (T)**: min over the merge-family of A ≤ Σ/(2⁴−1) = Σ/15.

**Status before this round**: Verified with 0 violations over 9646 budget-enforced exact-Fraction m=4 gap integer configs (Σ ≤ 90), worst ratio 0.882 at {8,4,3,2}. NOT analytically proven. The "worst ratio 0.9494 at {37,21,16,5}" cited in the approach file refers to a restricted 5-strategy sub-family, NOT the full merge-family (which achieves A=0 at {37,21,16,5}).

---

### 2. The mechanism: which strategy achieves the minimum

**Computational findings** (verified 0/10052 violations, Σ ≤ 90):

Define d₁ = p₁−p₂, d₂ = p₂−p₃, d₃ = p₃−p₄, δ = p₄. The gap conditions become:
- (1) d₁ ≤ 2δ+d₃ (from p₁ ≤ Σ/2)
- (2) δ+d₂+d₃ < 4Σ/15 (from p₂ < 4Σ/15 = τ/2)

Write t = Σ/15 (the target). Only 4 strategies suffice (covering all 10052 integer gap configs):

**Strategy R** (perfect matching: pair (p₁,p₄) and (p₂,p₃)): effective {p₁−p₄, p₂−p₃} = {d₁+d₂+d₃+δ, d₂} ... A_R = min(d₁+d₃, d₂) ≤ d₂.

**Strategy S** (perfect matching: pair (p₁,p₂) and (p₃,p₄)): effective {d₁, d₃}; A_S = min(|d₁−d₃|, min(d₁,d₃)) ≤ d₃.

**Strategy P** (applicable when d₁ ≥ δ+d₃, i.e., p₁ ≥ p₂+p₃): pair p₂ into p₁ then p₃ into p₁; effective {Σ−2p₁, p₁−p₂−p₃}; A_P = min(2δ+d₃−d₁, d₁−δ−d₃). **Key**: sum = δ so A_P ≤ δ/2.

**Strategy C** (applicable when d₁ ≤ δ+d₃, i.e., p₁ ≤ p₂+p₃): pair p₂ into p₁ (leftover L=d₁), then pair L into p₃ (L ≤ p₃); effective {p₄, p₃−L} = {δ, δ+d₃−d₁}; A_C = min(d₁−d₃, δ+d₃−d₁) (when d₁ ≥ d₃). **Key**: sum = δ so A_C ≤ δ/2.

P and C are COMPLEMENTARY (d₁ ≥ δ+d₃ vs d₁ ≤ δ+d₃); when they're equal (d₁ = δ+d₃), both give A = 0.

---

### 3. THE COMPLETE PROOF OF (T) FOR m = 4

**Proof** (set t = Σ/15):

**Case 1** (d₂ ≤ t): Strategy R gives A_R ≤ d₂ ≤ t. ✓

**Case 2** (d₃ ≤ t): Strategy S gives A_S ≤ d₃ ≤ t. ✓

**Case 3** (|d₁−d₃| ≤ t): Strategy S gives A_S ≤ |d₁−d₃| ≤ t. ✓

**Case 4** (d₂ > t, d₃ > t, |d₁−d₃| > t): We claim d₁ ≥ d₃ (Sub-case A) must hold.

*Sub-case B impossible*: Suppose d₃ > d₁, so d₃−d₁ > t. With d₂ > t and d₃ > d₁+t, condition (2) gives δ+d₂+d₃ > δ+t+(d₁+t) = δ+d₁+2t. But (2) also says δ+d₂+d₃ < 4t. So δ+d₁ < 2t. Now from gap condition (2) rewritten: 7d₂+3d₃ < δ+4d₁ (derived from p₂ < 4Σ/15 and Σ expressed in d_i, δ). With d₂ > t and d₃ > d₁+t: 7t+3(d₁+t) = 10t+3d₁ < 7d₂+3d₃ < δ+4d₁. Hence 10t < δ+d₁ < 2t, giving 10 < 2 — contradiction.

So Sub-case B cannot occur: when d₂ > t, d₃ > t, and |d₁−d₃| > t, necessarily d₁ > d₃.

*Sub-case A* (d₁ > d₃, d₁−d₃ > t): From (2) with d₂ > t and d₃ > t:
- **δ < 2t**: δ < (4t−d₂−d₃) < 4t−2t = 2t. [From condition (2).]

Exactly one of P or C applies (they partition d₁ ≷ δ+d₃):
- **P applies** (d₁ ≥ δ+d₃): A_P = min(2δ+d₃−d₁, d₁−δ−d₃). The two terms sum to **δ < 2t**, so A_P ≤ δ/2 < t.
- **C applies** (d₁ < δ+d₃): A_C = min(d₁−d₃, δ+d₃−d₁). The two terms sum to **δ < 2t**, so A_C ≤ δ/2 < t. Moreover since d₁−d₃ > t: the second term δ+d₃−d₁ = δ−(d₁−d₃) < 2t−t = t, giving A_C = δ+d₃−d₁ < t directly.

In both sub-cases A_P, A_C < t = Σ/15. ∎

**This is a complete, elementary, rigorous proof of (T) for m=4** — no gaps, no unverified lemmas. It uses only:
- The four strategies R, S, P, C (all directly constructive, no search).
- The gap conditions (1) and (2) (both already established in the approach file).
- Arithmetic (averaging bound and contradiction via summing conditions).

---

### 4. The gap condition reformulation needed for the proof

The critical computation: from p₂ < 4Σ/15 and Σ = p₁+p₂+p₃+p₄:
**p₂ = δ+d₂+d₃ < 4Σ/15 = 4t** (condition (2)).

The inequality **7d₂+3d₃ < δ+4d₁** (used for the Sub-case B contradiction) follows from:
- Σ = 4δ+3d₃+2d₂+d₁, so t = Σ/15.
- p₂ = δ+d₂+d₃ < 4t = 4Σ/15 = (16δ+12d₃+8d₂+4d₁)/15.
- 15(δ+d₂+d₃) < 16δ+12d₃+8d₂+4d₁.
- 7d₂+3d₃ < δ+4d₁. ✓

This needs to be stated explicitly in the proof.

---

### 5. The minimizing strategy and its mechanism

**Worst case** (smallest margin): {8,4,3,2}, Σ=17, t=17/15≈1.133. 
Here d₁=4, d₂=1, d₃=1, δ=2. Case 1 applies (d₂=1 < 17/15). Strategy R gives A_R = min(d₁+d₃, d₂) = min(5,1) = 1 ≤ 17/15. ✓

**The "hard" case structure** (Cases 3+4 dominate): Occurs when the consecutive differences d₁,d₂,d₃ are all comparable to Σ/15 and nearly equal, e.g. {18,11,8,5} (d₁=7,d₂=3,d₃=3,δ=5, t=2.8). Here Case 4 applies: δ=5 < 2t=5.6 (barely), C gives A_C=min(4,1)=1<2.8. ✓

**The "P/C" mechanism** (the central insight): In the hard case, strategies P and C BOTH encode the algebraic identity A_P + other_term = δ and A_C + other_term = δ. Since δ < 2t (forced by the gap condition when both d₂>t and d₃>t), the minimum of the two terms is < t. This is the "smooth" algebraic machinery behind (T).

---

### 6. Extension to general m

The m=4 proof structure points to the following inductive approach for m≥5:

**Base**: m=4 proved above (and m=3 proved as Lemma R4, m=2 as Case A.A).

**Inductive step** (candidate, not proved here): For m≥5, either:
(a) One of the "matching" strategies (generalizations of R, S) gives A ≤ Σ/(2^m−1), OR
(b) The "chain P/C" strategies give A ≤ p_m/2 where p_m < 2Σ/(2^m−1) (forced by the gap condition when m−1 differences are all > Σ/(2^m−1)).

The key gap condition for tight budget b=m−1: p₂ < Σ·2^{m-2}/(2^m−1). When all inner differences exceed Σ/(2^m−1), this forces p_m < 2Σ/(2^m−1), making the P/C bound A ≤ p_m/2 < Σ/(2^m−1).

This generalizes the m=4 argument but requires careful verification that Sub-case B analogues are impossible for m≥5 (numerically confirmed, 0 violations at m=5 in bounded search).

---

### 7. Candidate proof strategies, ranked by promise

1. **[STRONGLY RECOMMENDED, m=4 DONE]** Direct case-split (4 cases R/S/P/C) via the above proof — complete and elementary for m=4. **This should be written up immediately as the proof of (T) for m=4.**

2. **[PROMISING, needs verification]** Induction on m via the P/C chain mechanism: reduce m pieces to (m−1) pieces via one pairing step, showing the reduced instance satisfies the (m−1) induction hypothesis or exits the gap case. The bound p_m < 2Σ/(2^m−1) plays the key role.

3. **[LOWER PRIORITY]** General m by "matching" averaging: the sum of all 3 perfect-matching A-values ≤ 2p₂ < 8Σ/(2^m−1), hence min ≤ 2p₂/3. This gives Σ/(2^m−1) if p₂ ≤ 3Σ/(2·(2^m−1)), which is NOT always true from the gap condition alone. So averaging alone is insufficient.

4. **[DEAD END]** SB-monotone reduction (already ruled out by the SB-obstruction theorem).

---

### Distinct openings

1. **[IMMEDIATE]** The m=4 proof above is COMPLETE — write it up. Cases 1−3 use strategies R or S (matching). Case 4: Sub-case B impossible (10t < δ+d₁ < 2t contradiction), Sub-case A uses P or C giving A ≤ δ/2 < t since δ < 2t by gap condition.

2. **Induction for m≥5**: After the m=4 proof, set up an induction on m where one "chain" pairing step reduces m pieces to m−1 effective pieces and the induction hypothesis (T for m−1) closes it. The tight-budget structure (b=m−1 → b'=(m−1)−1 = (m−1)−1) propagates. The residual to check is whether the reduced instance stays in gap-case form.

3. **Continuous case verification**: The proof above works for ALL positive real pieces (not just integers), since it is purely algebraic. No integrality used anywhere.

- **Candidate technique(s)**: Finite case-split (4 cases), averaging bound (min ≤ sum/2 = δ/2), gap condition arithmetic. All elementary.
- **Cheap-kill candidates**: The Sub-case B impossibility is the key "cheap kill" — one algebraic contradiction (10t < 2t) eliminates half the case space. After that, the P/C complementary covering is immediate.
- **Knowledge-base entries to use**: None specifically needed; the proof is self-contained from the existing certified lemmas (gap conditions from sum-bound framework, R1/R2/R3 certified in sum-bound-reductions.md).
- **Analogous past problems**: None identified.
- **Prior progress**: m≤3 fully proved. m=4 now has a complete proof (above). m≥5 is the remaining frontier.
- **Dead ends (do not retry)**: SB-monotone reductions (sb-obstruction.md), the 5-strategy sub-family as the FULL merge family (it's not — it misses free equal-pair collapses).
- **Small-case / intuition notes**: The worst ratio for the FULL merge family (including free equal-pair collapses) is 0.882 at {8,4,3,2} (A=1, t=17/15). NOT 0.9494 — that ratio was for the restricted 5-strategy sub-family. The proof for m=4 requires only 4 strategies: R, S, P, C.
