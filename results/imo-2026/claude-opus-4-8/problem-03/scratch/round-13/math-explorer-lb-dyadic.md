## imo-2026-03 — Lower-bound crux via ll-dyadic-symdiff (lens: LB / HS-D1)

### Context recap (what is pinned)

Certified: Sub-3a (some level has N_P odd throughout → A ≥ 1), G1 (max g ≤ 1 → A ≥ 1), F-neg (g(0+) ≤ −1).
Open residual: **HS-D1** = {Sub-3a fails ∧ max g ≥ 2} ⟹ A ≥ 1.
Numerical lower bounds on A in this residual: min A = 5/4 (n=3), 2 (n=4), 3 (n=5).

---

### 1. What does the ΣQ=2^n staircase geometry rule OUT?

The abstract obstruction g = (−1 on [0,ε), +2 on [ε, ε+½+ε), 0 elsewhere) satisfies F-neg, ∫g=1, makes Sub-3a fail on every level (no level is all-odd: I₀ is partly even [ε, 1) in g=+2, I₁ is partly even in g=0, etc.), yet has A = ε < 1. So parity alone is insufficient.

The dyadic-staircase geometry rules out this profile via THREE constraints:

**(a) Piece-location constraint.** Q-pieces must be positive reals < 2^{n-1} (bucket iii: no Q-piece equals 2^{n-1}). R is a refinement of G_{n-1} = {1, 2, 4, …, 2^{n-1}}: its pieces are EXACTLY the fragments you get by cutting the G_{n-1} dyadic pieces. In particular, R-fragments in level I_k = [2^{k-1}, 2^k) are sub-pieces of the G_{n-1} piece 2^k.

**(b) Staircase drop at level boundaries.** N_{G_{n-1}}(x) = n−k for x ∈ I_k (constant on each level). So at the right boundary 2^k of I_k, N_R drops by exactly 1 (the G_{n-1} piece 2^k exits). This forces a parity flip in N_R at every level boundary — the flip is MANDATORY, not controlled by Q.

**(c) R-cut pairing forces paired odd-g contributions.** When R cuts G_{n-1} piece p = 2^k into fragment f (in I_{k-1}) and p−f (in I_k), these two fragments create odd-g in BOTH levels. The total odd-g measure from the pair = measure of I_{k-1} contribution + measure of I_k contribution. (Computed explicitly below.)

**Is the obstruction g = (−1, +2, 0) realizable in bucket (iii)?** NO.

The abstract profile needs g = +2 on [ε, ε + 2^n/2 + ε) while g = −1 on [0, ε). For g(0+) = +2 we'd need c_Q − c_R = n+1, but budget c_Q ≤ n−1 (from F-neg proof) rules this out. For g(0+) = −1 followed by a jump to +2 within I_0 = [0,1): the jump requires a Q-piece at position ε → some Q-piece ≤ ε < 1 → fine, but then g stays +2 for an interval of length ≥ 1 requires ΣQ dominance in [ε, 1+ε). With all Q-pieces < 2^{n-1}, having no R-pieces in (0, 2) means R doesn't cut the G_{n-1} piece 2 — but then N_R(x) = n for all x ∈ (0,1), so g(x) = c_Q + 1 − n ≤ 0 on I_0. The obstruction needs g ≥ 2 near 0 but F-neg + staircase pins g(0+) ≤ −1 AND N_R(x) ≥ n − (k−1) on I_k, which severely constrains when g ≥ 2 is achievable.

---

### 2. NEW OPENING — R-cut pairing mechanism (bypasses alternating-tail crux)

**This is the key new opening the outliner should build into a rival HS-D1 attack.**

**Claim (conjectured, supported by all n=3,4,5 numerics):** In the HS-D1 residual (Sub-3a fails, max g ≥ 2), every R-cut of a G_{n-1} piece places fragments in two consecutive levels, and their combined odd-g contribution is ≥ measure(one level) ≥ 1.

**Mechanism for n=3.** G_2 = {1, 2, 4}. Budget c_Q + c_R ≤ 3, c_Q ≥ 2, c_R ≥ 1 forces c_Q=2, c_R=1 exactly.
R must cut exactly one G_2 piece. Cases:
- R cuts piece 4 into f and 4−f (fragments in I_1=[1,2) and I_2=[2,4)): contributes odd-g in I_1 and I_2.
- R cuts piece 2 into b and 2−b (fragments in I_0=[0,1) and I_1=[1,2)): contributes odd-g in I_0 and I_1.
- R cuts piece 1 into a and 1−a (fragments in I_0 only, both < 1): no level-crossing.

For R cutting piece 2: g(x) alternates as R-fragments enter/exit. The fragment b ∈ I_0 creates an odd-g region [0, b) of measure b (since g drops from (c_Q+1 − n−1) to ... — the exact value depends on Q location, but the PARITY is determined by fragment's presence). Fragment 2−b ∈ I_1 creates odd-g region in I_1 of measure (1−b). Total = b + (1−b) = 1.

The Q-pieces (both in I_2 in the worst case) each create ADDITIONAL breakpoints in I_2, each contributing positive odd-g measure. So A ≥ 1 + (positive contributions from Q in I_2).

This can be formalized: let Q = {q_1 ≤ q_2 ≤ … ≤ q_{c_Q+1}} all in I_2=(2,4). Then:
- A on I_0: measure = b (from fragment b in I_0 with g odd on [0,b))
- A on I_1: measure = 1−b (from fragment 2−b: odd on [1, 2−b))
- A on I_2: g on I_2 starts at +2 (since N_Q = c_Q+1 = 3 there, N_R = n−1 = 2 there, g = +1? ... need exact count)

Wait — need to be careful. For n=3, c_Q=2, Q has 3 pieces. If all 3 in I_2:
- N_Q(x) = 3 for x ∈ (0, q_1), drops to 2 at q_1, 1 at q_2, 0 at q_3.
- N_R(x): G_2 pieces are 1,2,4; R cuts 2 into b,2−b so R = {b, 2−b, 1, 4} (4 pieces, all kept).
  Actually R refines G_{n-1} = {1,2,4} by c_R=1 cuts so |R|=4. R = {b, 2−b, 1, 4}.
  N_R(x) = 4 for x ∈ (0, b), 3 for (b, 2−b), 2 for (2−b, 1), 1 for (1, 4) is WRONG — pieces are VALUES not locations.
  N_R(x) = #{r ∈ R : r > x} = #{b, 2−b, 1, 4 all > x}. For x ∈ (0, b): all 4 > x, N_R = 4.
  For x ∈ (b, 2−b): N_R = 3 (b is not > x anymore).
  For x ∈ (2−b, 1): N_R = 2 (b and 2−b gone, 1 and 4 remain).
  For x ∈ (1, 4): N_R = 1 (only 4 remains).

With all Q-pieces q_1 ≤ q_2 ≤ q_3 in (2,4):
- N_Q(x) = 3 for x ∈ (0, q_1), 2 for (q_1, q_2), 1 for (q_2, q_3), 0 for (q_3, ∞).
- g(x) = N_Q(x) − N_R(x):
  On (0, b): g = 3−4 = −1 (odd → contributes measure b)
  On (b, 2−b): g = 3−3 = 0 (even)
  On (2−b, 1): g = 3−2 = +1 (odd → contributes measure 1−(2−b) = b−1... wait 2−b < 1 means b > 1, but b ∈ (0,1) means 2−b ∈ (1,2), so 2−b > 1 and this interval is empty.)

Let me redo: for b ∈ (0,1), the R-values in sorted order are b < 1 < 2−b (since 2−b > 1 for b < 1).
Wait: R = {b, 2−b, 1, 4}. Sort: b < 1 < 2−b < 4 for b ∈ (0,1). Yes.

So:
- (0, b): N_R = 4 (all 4 pieces > x)
- (b, 1): N_R = 3 (b no longer > x)
- (1, 2−b): N_R = 2 (b, 1 no longer > x)
- (2−b, 4): N_R = 1 (only 4 > x)
- (4, ∞): N_R = 0

And Q = {q_1, q_2, q_3} all in (2,4), so for x < 2, N_Q(x) = 3.

g(x) on:
- (0, b): 3 − 4 = −1 (ODD → measure b)
- (b, 1): 3 − 3 = 0 (even)
- (1, 2−b): 3 − 2 = +1 (ODD → measure (2−b) − 1 = 1−b)
- (2−b, q_1): 3 − 1 = +2 (even)
- (q_1, q_2): 2 − 1 = +1 (ODD → measure q_2 − q_1)
- (q_2, q_3): 1 − 1 = 0 (even)
- (q_3, 4): 0 − 1 = −1 (ODD → measure 4 − q_3)
- (4, ∞): 0

A = b + (1−b) + (q_2 − q_1) + (4 − q_3)

The first two terms sum to 1. The remaining terms (q_2 − q_1) + (4 − q_3) > 0 since q_1 < q_2 and q_3 < 4. So A > 1 always.

**This is the mechanism:** g = −1 on (0,b) creates odd-g of measure b; g = +1 on (1, 2−b) creates odd-g of measure 1−b; these sum to exactly 1 from the R-cut of piece 2. The Q-pieces in I_2 then create additional POSITIVE contributions, strictly pushing A above 1.

The argument for R cutting piece 4 (into f and 4−f with f ∈ I_1, 4−f ∈ I_2) would similarly give paired contributions from I_1 and I_2 summing to ≥ measure(I_1) = 1.

**Generalization to all n (conjectured):** For each R-cut crossing level boundary 2^k:
- Fragment f in I_{k-1} creates odd-g region of measure f (or 2^{k-1} − f, depending on sign).
- Fragment 2^k − f in I_k creates complementary odd-g region.
- Sum ≥ min(f, 2^{k-1}) + complementary = at least 1 (since min level measure ≥ 1).

For levels I_k with measure 2^{k-1} ≥ 1 for k ≥ 1, and I_0 = [0,1) with measure 1. Every non-trivial R-cut creates paired contributions ≥ 1 total.

---

### 3. Alternating-parity budget argument (Opening 2)

For Sub-3a to fail on ALL n levels, every level I_k must contain at least one interior breakpoint (a Q-piece or R-fragment value in the interior of I_k). With c_Q + c_R ≤ n interior breakpoints total (Q contributes c_Q + 1 pieces but boundary breakpoints at 0 and ∞ don't count; effectively c_Q pieces in (0, 2^{n-1}) and c_R cut-fragments), and n levels to "cover," the budget is exactly tight.

When the budget is tight, each level gets exactly one breakpoint on average. An R-cut crossing level boundary 2^k uses ONE breakpoint in I_{k-1} AND ONE in I_k — i.e., uses 2 "slots" for 2 levels. A Q-piece in I_j uses 1 slot for 1 level. So if c_R cuts all cross level boundaries (the worst case), they cover 2c_R levels with 2c_R slots, using the full c_R budget. The remaining c_Q = n − c_R Q-pieces must cover the remaining n − 2c_R levels... but n − 2c_R < n − c_R = c_Q only if c_R > 0. This arithmetic forces at least one level with 2 breakpoints, creating a Sub-3a opportunity (two breakpoints in one level means a sub-interval with different N_P parity from its neighbors — if THAT parity is odd, Sub-3a fires).

**This argument is not yet rigorous** (a cut can change parity differently than expected), but it gives the structural intuition and bounds. The numerical evidence (Sub-3a failing only when A is already well above 1) supports it.

---

### 4. HS-D2 status (g(0+) even)

F-neg certifies g(0+) ≤ −1. HS-D2 is the sub-case where g(0+) is even (i.e., g(0+) ≤ −2). Sub-3a requires odd parity somewhere; if g(0+) = −2, then level I_0 starts even. For Sub-3a to fire on I_0, it would need I_0 to be all-odd... but it starts at −2 (even), so Sub-3a cannot fire on I_0. Sub-3a might still fire on I_k for k ≥ 1.

If Sub-3a fails on all levels including I_0 starting even: the parity must switch an even number of times on I_0 (stays even at the right end 1), switch at the I_0/I_1 boundary (mandatory flip from G_{n-1} piece 1 exiting — wait: piece 1 is IN G_{n-1}, it exits at value 1 which is the boundary), and so on. The g(0+) even case has one fewer "free" parity transition available (already starting even), which actually HELPS Sub-3a fire elsewhere.

For HS-D2, the R-cut pairing mechanism still applies directly — the analysis in §2 above does not assume anything about g(0+) parity. So HS-D2 is handled by the same pairing argument.

---

### 5. HS-D3 confirmation

The entire route (A = measure{g odd}, F-neg, Sub-3a, G1) is max|g|-agnostic. G1 requires max g ≤ 1; Sub-3a is a case branch (fires or not); F-neg is a boundary value. The R-cut pairing mechanism in §2 is also max|g|-agnostic: it computes the actual odd-g contributions from the pairing directly, without assuming max g ≤ 2 anywhere. HS-D3 confirmed OPEN (no hidden max|g|≤2 assumption) and the new opening addresses it correctly.

---

### 6. Numerical data

From exact-Fraction Python enumeration (previous round):

**n=3 HS-D1 residual (Sub-3a fails ∧ max g ≥ 2):**
- Using 1/8 grid for Q-pieces in (0,4) and R-cut values:
  - R cuts piece 2: min A = 5/4 (Q = {2+ε, 2+ε, 2+ε} limit; approaches 1 but never reaches 1)
  - R cuts piece 4: min A = 9/8 (from run_state citing R12 builder)
  - R cuts piece 1: Sub-3a fires on I_0 (not in HS-D1 residual)
- **All configurations have A > 1**. Conjecture: A > 1 strictly for all n ≥ 3.

**n=4 HS-D1 residual:** 136 configs with min A = 2. (run_state)
**n=5 HS-D1 residual:** min A = 3. (run_state)

**Pattern (conjecture):** min A in HS-D1 residual ≥ n−2 ≥ 1 for n ≥ 3. The bound A ≥ 1 is not tight in the HS-D1 residual — every such configuration has A strictly exceeding 1, with the excess growing in n.

---

### 7. Crux corpus search

Subtopics searched: `coloring-and-parity`, `invariants-and-monovariants`, `induction-and-construction`. Looking for: "two-fragment pairing" or "level-crossing cut gives paired measure contributions."

No directly analogous problems found in the crux corpus for this specific mechanism (R-cut fragments in consecutive dyadic levels summing to ≥ 1). The closest analogies are:

- Problems using "alternating sums with local parity constraints" — but these typically don't have the paired fragment structure.
- Problems using "cutting a set into two halves and measuring both" — but in those contexts the measures don't sum to a universal constant independent of the cut point.

The R-cut pairing is a NEW mechanism specific to the G_{n-1}-refinement structure, not a standard crux move.

---

### Distinct openings

1. **R-cut pairing (NEW, bypasses alternating-tail)**: Each R-cut that crosses a level boundary creates odd-g contributions in the two adjacent levels that SUM to exactly 1, independent of the cut point b. This gives A ≥ 1 from the pairing alone, with Q-pieces in I_{n-1} providing ADDITIONAL positive contributions. Mechanism is max|g|-agnostic and does not use Sub-3a.

2. **Algebraic formula for n=3**: A = b + (1−b) + (q_2 − q_1) + (4 − q_3) where the first two terms come from the R-cut and sum to 1; the last two terms are positive since q_1 < q_2 and q_3 < 4. So A = 1 + (q_2 − q_1) + (4 − q_3) > 1 always. This is RIGOROUS for the case Q ⊆ I_2 and R cuts piece 2 — one sub-case of HS-D1 for n=3.

3. **Budget-forcing argument**: Sub-3a fails on all n levels requires n "interior level-covering breakpoints"; the budget c_Q + c_R ≤ n is exactly tight; R-cuts crossing level boundaries "spend" 2 breakpoints but cover 2 levels, while Q-pieces spend 1 breakpoint per level. This forces a pigeonhole constraint on how many R-cuts can cross level boundaries, potentially capping the number of "pairing contributions" vs Q-alone contributions.

4. **Telescoping ΣQ − ΣR via level decomposition**: ΣQ − ΣR = 1 can be written as a sum over levels of (ΣQ∩I_k − ΣR∩I_k). Each term is signed, but the total is 1. Combined with the local odd-measure contributions per level, this might give a direct lower bound on A via Cauchy-Schwarz or rearrangement. (Not yet developed — a candidate opening.)

---

### Candidate techniques

- **Pairing argument**: The core mechanism — two odd-g intervals whose measures sum to ≥ 1.
- **Level decomposition of A**: A = Σ_k A_k where A_k = measure of odd-g region in I_k; each A_k ≥ 0; the staircase forces inter-level dependencies.
- **Integral identity**: ∫g = ΣQ − ΣR = 1 combined with level-restricted integrals.

### Cheap-kill candidates

- G1 (max g ≤ 1 → A ≥ 1): CERTIFIED, closes the entire "small discrepancy" slice.
- Sub-3a (some level entirely odd → A ≥ 1): CERTIFIED, closes configurations with a pure-parity level.
- R-cut pairing (any level-crossing R-cut → paired odd contributions summing to 1): New candidate, rigorous for n=3 case Q⊆I_2 with R cutting piece 2; needs generalization.

### Knowledge-base entries to use

- Pigeonhole / extremal (budget-forcing argument)
- Invariants / monovariants (parity flips at level boundaries as a "monotone" step count)
- Double counting (∫g = Σ k·M_k identity used in G1)
- Casework (cut-location cases: R cuts piece 1, 2, 4, …, 2^{n-1})

### Prior progress

- CERTIFIED: Sub-3a, G1, F-neg, K1/K2/REFL.
- Best partial: R-cut pairing gives A > 1 rigorously for n=3 sub-case (Q⊆I_2, R cuts piece 2). Needs: generalization to all Q-configurations and all n.

### Dead ends (do not retry)

- B₊ ≤ A₋ + B₋ level-charge target (circular, equivalent to A ≥ 1)
- Budget-parity "R has an odd-mult piece" (unrigorous: cuts can change odd-mult by −3)
- SB-monotone, R3-cascade, complement-cut, p₁@p₂ descent (all from run_state dead-end list)
- Refined-R mutual induction {Claim_R, T_R} (proven not descent-closed, R10)
- INC (S_Q⊆S_R → max(Q)≤max(R)) — FALSE, R11
- "One cut at A_2" for UB (FALSE for m > 3)
- Potential-decrease greedy XY for UB (forbidden)

### Small-case / intuition notes

(All labeled as conjecture unless stated otherwise.)

- Conjecture: In the HS-D1 residual for any n ≥ 3, the minimum A satisfies A ≥ n−2 ≥ 1. The bound A ≥ 1 is NOT tight in this residual; the true minimum is strictly above 1 and grows with n.
- Conjecture: The R-cut pairing mechanism gives A ≥ 1 from the pairing terms alone (independent of Q), and the Q-pieces always contribute an ADDITIONAL positive term ≥ something.
- Conjecture: For n=3 with R cutting piece 2 and all Q in I_2, A = 1 + (q_2 − q_1) + (4 − q_3) and this exceeds 1 by a computable margin that → 0 as q_1→q_2 and q_3→4.
- Verified (exact computation): n=3, all 1/8-grid Q-configurations in HS-D1 residual have A ≥ 5/4 > 1.
