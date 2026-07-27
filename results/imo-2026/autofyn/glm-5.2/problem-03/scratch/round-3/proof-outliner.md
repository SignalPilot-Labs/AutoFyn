## imo-2026-03
Spec review: required
Technique: Parity-integral (rank function) for the lower bound; Schur-majorisation/smoothing for the upper bound. Spine = the identity D = ∫ 1_{r(t) odd} dt, with cuts as parity toggle-pairs, plus its "even-sum" reformulation that makes Case A trivial and pins Case B.

### Reformulations to reuse (all rigorous, build on Lemma A)
- D = a_1 − a_2 + a_3 − … ; LB gets (1+D)/2, XY gets (1−D)/2. Units: total S_n = 2^{n+1}−1; LB plays G_n=(1,2,…,2^n); target D* = 1.
- **EVEN-SUM REFORMULATION (new, clean):** D ≥ 1 ⟺ XY's even-position sum ≤ 2^n−1 (= tail total) ⟺ LB's odd-position sum ≥ 2^n. Proof: Σ_odd − Σ_even = D and Σ_odd + Σ_even = S_n. This makes Case A one line (see below) and gives the exact target for Case B: "the second picker's take cannot exceed the mass of everything below the former largest piece."
- **CORRECTED rank/parity integral.** D = ∫_0^{∞} 1_{r(t) odd} dt, r(t)=#{pieces ≥ t}. A cut splitting a piece of size s into (m, M) (m ≤ M, m+M=s) toggles the parity of r(t) on the two intervals (0, m] and (M, s] (each of length m); it leaves parity unchanged on (m, M]. [Verification on n=1 halving 2→1+1: r_0 parity odd on (0,1], even on (1,2]; toggles on (0,1] and (1,2]; result odd on (0,1] only → D=1. ✓]
  - **WARNING (verify, do NOT assume Lead 1):** the formula "r_final = r_0 + R(t), R = #{cuts with smaller fragment ≥ t}" stated in Lead 1 is FALSE — it omits the −1 toggle on (M, s]. On n=1 halving it predicts D=2 instead of the true D=1. The correct object is the *toggle-pair* description above. Treat Lead 1's R as a non-rigorous mnemonic only.

Skeleton (LOWER bound — primary target this round):
  1. State L(n): every refinement of G_n by ≤ n cuts has D ≥ 1 (units). — by definition + Lemma A.
  2. Reduce to even-sum form: L(n) ⟺ "XY's even-position sum ≤ 2^n−1". — by the even-sum identity.
  3. **Case A (re-prove, one line):** 2^n intact ⟹ it sits at position 1 (odd) ⟹ every even-position piece lies in the tail ⟹ XY's even sum ≤ |tail| = 2^n−1. ✓ (This replaces the longer Case A computation; reuse the already-proved Case A if preferred.)
  4. **Case B (the gap):** 2^n is cut into fragments F (using k≥1 cuts), tail refined by ≤ n−k cuts into T. Use the toggle-pair picture: starting from the geometric parity staircase r_0 (r_0(t) = n+1−j on (2^{j-1}, 2^j], j=0..n, so parity alternates block-to-block), XY applies ≤ n toggle-pairs; prove ∫1_{r odd} ≥ 1 survives.
  5. Equality case = full halving (each 2^j → 2^{j-1}+2^{j-1}), giving 2n+1 pieces 2^{n-1}(×2),…,1(×3) with D=1; certify it attains the bound.

Skeleton (UPPER bound — secondary, harder; aim for n=2 case proof as concrete advance):
  1. Dual target U(n): for EVERY ≤ n+1-piece partition of [0,1] (total 1), XY with ≤ n cuts forces D ≤ 1/S_n.
  2. Reuse U(1) (proved, all three L-regimes incl. boundary).
  3. **Halving recurrence (Lead 2, verified):** when a_1 ≥ 2a_2, halving a_1 gives D_new = a_1 − D_old. Use it to handle the "top-heavy" regime a_1 ≥ 2a_2 by induction.
  4. **Flat regime (a_1 < 2a_2) — the precise failure point.** Here the recurrence condition breaks; identify the smallest n and a concrete config where the hybrid leaves a leftover > 1/S_n, and design a compensating multi-cut strategy for that regime. (Round 2 showed the scale-invariant induction V(C,m) ≤ T/S_m fails exactly here for m ≥ 2.)
  5. Conjectured clean route (state, do not claim proved): f(C) := min_XY D(C) is Schur-maximised uniquely at G_n; a smoothing lemma "deforming C toward G_n only increases f" would close U(n) from the lower bound. Flag the smoothing monotonicity as the open hard lemma.

Key lemmas (claim + mechanism):
  - **Lemma (Even-sum equivalence).** D ≥ 1 ⟺ Σ_even ≤ 2^n−1 ⟺ Σ_odd ≥ 2^n. — because Σ_odd − Σ_even = D and totals match; makes the lower-bound target combinatorial ("2nd picker's take ≤ tail mass").
  - **Lemma (Toggle-pair structure, CORRECTED).** A cut on s→(m,M) toggles r-parity on (0,m] and (M,s] (equal lengths m); cuts compose as toggle-pairs on the geometric staircase. — direct from r(t) = #{pieces ≥ t} and m+M=s. [This is the replacement for Lead 1's broken r_0+R formula.]
  - **HARD Lemma (Lower-bound Case B — the open crux).** On the geometric staircase r_0 of G_n, no sequence of ≤ n toggle-pairs (each pair = one bottom interval (0,m_i] + one "top stub" interval (M_i, s_i] ⊂ (2^{j-1}, 2^j] of equal length m_i, with s_i a piece currently present) reduces ∫ 1_{r odd} below 1. — mechanism to prove: induction on n exploiting staircase self-similarity (the G_n staircase = G_{n-1} staircase + the single top block (2^{n-1}, 2^n] of length 2^{n-1}); the "+1 gap" 2^j = (Σ_{i<j} 2^i) + 1 forces an unmatched unit of parity mass to survive. This carries the dyadic STRUCTURE of the tail (satisfying the round-2 lesson that "D(T) ≥ 1 alone" is insufficient). Equality iff full halving. **This is the load-bearing step; flag for the builder.**
  - Lemma (Halving recurrence). When a_1 ≥ 2a_2, halving a_1 ⟹ D_new = a_1 − D_old. — after halving, sorted order is a_1/2, a_1/2, a_2, … so the new alternating sum is a_2−a_3+… = a_1 − D_old. (Verified; gives the equality trajectory on G_n.)
  - Lemma (Staircase self-similarity). r_0(G_n) restricted to (0, 2^{n-1}] is r_0(G_{n-1}) scaled; only the top block (2^{n-1}, 2^n] is new. — because G_n = G_{n-1} ∪ {2^n} and 2^n is the unique piece ≥ 2^{n-1}.

Cases to cover:
  - Lower bound: Case A (2^n uncut) — done/trivial. Case B (2^n cut) — open; sub-cases by #cuts k on 2^n (1 ≤ k ≤ n) and whether fragments of 2^n interleave into the top of the tail.
  - Upper bound: top-heavy regime (a_1 ≥ 2a_2, halving applies) vs flat regime (a_1 < 2a_2, recurrence fails) — flat is open. Suggest settling U(2) exhaustively (piecewise-linear in 2 cut positions, breakpoints at coincident-sorted-order) as a concrete partial advance.

Watch out for:
  - Lead 1's "r_final = r_0 + R" is WRONG (verified n=1: predicts D=2, true D=1). Use the toggle-pair version; do not let the builder build on the broken formula.
  - The merge inequality "D(F∪T) ≥ |F|−|T| = 1" is FALSE for general tails (round-2 counterexample); the induction MUST carry the dyadic structure of T, not merely D(T) ≥ 1.
  - Cut budget is essential: with > n cuts on G_n, XY can drive D to 0 (e.g. 2 cuts on G_1). Any toggle-pair counting argument must use "≤ n pairs" crucially.
  - Upper bound: myopic greedy fails (36/400 n=2); naive Hall-pairing leaves leftover > 1/S_n (n≥3). Don't reuse these as strategies.
  - For the upper bound, equality (D = 1/S_n) occurs iff LB = geometric AND XY = full halving; this pins the extremal config for both directions and is the equality case to verify in any final answer.

Existing rigorous pieces to reuse (do not re-derive):
  - Lemma A (greedy-pick reduction to D) — fully proved.
  - Lower bound L(1) and Case A (general n) — fully proved; Case A re-derivable in one line via even-sum.
  - Upper bound U(1) (all three L-regimes incl. L=1/2 boundary) — fully proved.
  - Difference-game f(G_n)=1 certifies min_XY D(G_n) ≤ 1 (XY upper bound on the geometric config only); does NOT prove the general lower bound and is NOT a general lower bound (counterexample {0.7,0.3}: min D=0.3 < f=0.4). Use only as a certificate that 1 is attainable.

Priority: CLOSE the lower-bound Case B via the corrected toggle-pair lemma (primary). If the builder cannot close the general toggle lemma, fall back to proving L(2), L(3) rigorously by exhaustive breakpoint casework (the staircase has finitely many breakpoints; this is a legitimate rigorous proof for fixed n) — this advances the result from "n=1 only" to "n≤3" even if the general induction is not found. Upper bound: attempt U(2) by the same exhaustive breakpoint method as a concrete partial advance; leave the general U(n) as a clearly-flagged conjecture with the smoothing lemma stated.
