## imo-2026-03

Answer already PINNED & verified: c(n) = 2^n/(2^{n+1}−1). Shared certified backbone (all approaches import,
do NOT re-prove): Lemma G (greedy = odd-index, LB = val = (1+A)/2), alt-sum-integral (A = measure{N odd}),
tightness V(G_n) ≤ c(n), Lower-bound Case 1, LL t=1 single-cut, Regime A shadow, Regime B1 partial-shadow,
R1/R2/R3 sum-bound reductions, Parity-Condition, Top-band decomposition, Lemma REFL, ll-case1-high-interval,
dyadic-level-parity. Each slug below is a FULL rival attempt at the whole c(n) claim (upper + lower), differing
only in the mechanism for its still-open hard step. Field this round: three advances (both LB routes + the UB
leader), each converting the fresh explorer machinery into rigor and isolating a precise residual.

---

ll-inclusion-gap: advance
Target: c(n) = 2^n/(2^{n+1}−1) — full LB+UB determination; this slug's distinctive open step is the
  lower-bound crux G-INC-1 (`deficit_top + M ≥ 1` for S_Q ⊆ S_{G_{n−1}}, ΣQ = 2^n, |Q| ≤ n+1), reached via
  the inclusion split S_Q ⊆ S_R.
Technique: TWO-STEP STRONG INDUCTION n → n−2, driven by the SET IDENTITY, with a strengthened IH Claim(n,ε).
Skeleton:
  1. Reduce whole LB to LL t≥2, then (certified forcing-inc-reduction + Parity-Condition + top-band-decomposition)
     to G-INC-1, equivalently O_Q ≤ O_{G_{n−1}} — by certified lemmas.
  2. Certify SET IDENTITY `S_{G_{n−1}} ∩ [0,2^{n−2}) = S_{G_{n−3}}` — by the algebraic count identity
     N_{G_{n−1}}(x) = N_{G_{n−3}}(x) + 2 for x < 2^{n−2} (both 2^{n−2}, 2^{n−1} exceed x), same parity. (Verified
     n=3..7 this round, 0 mismatch.) Corollary: S_{Q_lo} ⊆ S_{G_{n−3}} where Q_lo = parts of Q below 2^{n−2}.
  3. Certify self-similar identity `M = A(G_{n−3}) − A(Q_lo)` — from A(G_{n−3}) = 2^{n−2} − A(G_{n−2}) and the
     certified top-band decomposition M = 2^{n−2} − A(G_{n−2}) − A(Q_lo).
  4. Budget propagation: h = |Q_hi| even ≥ 2 ⇒ |Q_lo| ≤ n−1 = (n−2)+1 — EXACT match to the level n−2 IH budget.
  5. Two-step induction with strengthened IH Claim(n,ε): A(Q) ≤ A(G_{n−1}) − 1 + ε for ΣQ = 2^n+ε, ε∈[0,1).
     Cases (with a = 2^{n−1}−q_1 ≥ 0, b = q_2−2^{n−2} ≥ 0, deficit_top = a+b, ΣQ_lo = 2^{n−2}+(a−b)):
       Case 1 (h ≥ 4): ΣQ_lo ≤ 2^n − 4·2^{n−2} = 0 ⇒ Q_lo = ∅, M = A(G_{n−3}) ≥ 1 (A(G_k) always odd ≥ 1). ✓
       Case 2a (h=2, deficit_top ≥ 1): direct. ✓
       Case 2b-i (h=2, a ≥ b): IH Claim(n−2, a−b) ⇒ A(Q_lo) ≤ A(G_{n−3})−1+(a−b) ⇒ M ≥ 1−(a−b);
         deficit_top + M ≥ (a+b)+(1−(a−b)) = 1+2b ≥ 1. ✓
  6. Base cases Claim(2,ε) (vacuous, no valid Q), Claim(3,ε) (Step-7 casework + ε∈(0,1) perturbation).
Key lemmas (claim + mechanism):
  - SET IDENTITY (step 2) — because N_{G_{n−1}}(x) − N_{G_{n−3}}(x) = 2 on [0,2^{n−2}), so parity is preserved.
  - A(G_k) odd, hence ≥ 1 — because A(G_k) = 2^k − A(G_{k−1}) = even − odd = odd, base A(G_0)=1.
  - Strengthened IH Claim(n,ε) — because sub-case 2b-i feeds ε' = a−b ≥ 0 ∈[0,1) back at level n−2, cycling
    cleanly (do NOT extend to ε<0 — FALSE: Q_lo={1.9,1.5} at n−2=2 gives A=0.4 > 0).
Open gaps:
  - Sub-case 2b-ii (h=2, a < b, ΣQ_lo ∈ (2^{n−2}−1, 2^{n−2})): need A(Q_lo) ≤ deficit_top (= a+b). PROVED at n=4
    for 2-part Q_lo via sup(S_{G_1})=2 ⇒ p_1 ≤ 2 ⇒ A(Q_lo) ≤ 4−ΣQ_lo = b−a ≤ a+b. General n: recurse
    top-band decomp on Q_lo one more level → telescoping sum of deficit terms bottoming on A(G_base) ≥ 1.
    The builder must formalize: for S_{Q_lo} ⊆ S_{G_{n−3}}, ΣQ_lo ∈ (2^{n−2}−1,2^{n−2}), |Q_lo| ≤ n−1,
    the top parts of Q_lo are bounded by sup(S_{G_{n−3}}) = 2^{n−3}, and the same sum+part-bound argument
    forces A(Q_lo) ≤ deficit_top.
  - G-INC-2 (refined R, general n): VACUOUS at n=3 (budget+parity kills all instances: |Q|≡|R| mod 2 forces
    c_Q+c_R > n). First nontrivial at n=4 (|Q|=3, c_R=1). Separate residual — the INC branch is proven only
    for R = G_{n−1}; refined R lacks the clean dyadic band structure. Builder: settle n=4 refined base explicitly.
Cases to cover: h≥4; h=2 with deficit_top≥1 / a≥b / a<b; Claim base cases n=2,3; G-INC-2 refined R at n=4.
Watch out for: (a) do NOT reinstate the false Structural Lemma — bound A(Q) by arithmetic on part values only;
  (b) even-multiplicity interior pairs {s,s} are admissible (Parity-Condition), must be handled; (c) ε<0 IH is
  FALSE; (d) the INC-parity shortcut (h even, h=2 forced, A(Q) ≤ (q_1−q_2)+q_3 < 3 at n=3) is a clean n=3
  cross-check but is just the n=3 special case of the top-band decomposition — do not present it as a general proof.

---

ll-dyadic-symdiff: advance
Target: c(n) = 2^n/(2^{n+1}−1) — full determination; this slug's distinctive open steps are GAP-B
  (A(Q∪G_{n−1}) ≥ 1 for max(Q) < 2^{n−1}) and GAP-A (A(Q'∪R) ≤ max(Q)−1 for max(Q) ≥ 2^{n−1}), reached via
  the measure(S_Q △ S_R) ≥ 1 split and Lemma REFL.
Technique: DOUBLE-REFL TELESCOPING (apply the certified reflection identity twice).
Skeleton:
  1. Reduce whole LB to measure(S_Q △ S_R) ≥ 1 (certified Lemma M framing); Cases 1/2/Sub-3a already closed
     (certified ll-case1-high-interval, dyadic-level-parity, Lemma P).
  2. GAP-B, R = G_{n−1} unrefined. First REFL on the global max 2^{n−1} (from G_{n−1}):
     A(Q∪G_{n−1}) = 2^{n−1} − A(Q∪G_{n−2}), where G_{n−2} = {1,…,2^{n−2}}.
  3. Split on q_1 = max(Q):
       Case A (q_1 ≤ 2^{n−2}): max(Q∪G_{n−2}) = 2^{n−2}, so A(Q∪G_{n−2}) ≤ 2^{n−2} ≤ 2^{n−1}−1 (by A(P) ≤ max P)
         ⇒ A(Q∪G_{n−1}) ≥ 2^{n−2} ≥ 1. ✓
       Case B1 (2^{n−2} < q_1 ≤ 2^{n−1}−1): second REFL on q_1 gives
         A(Q∪G_{n−1}) = 2^{n−1} − q_1 + A(Q'∪G_{n−2}) ≥ 2^{n−1} − q_1 ≥ 1 (by A ≥ 0). ✓
  4. Cover both LB regimes: also state GAP-A (max(Q) ≥ 2^{n−1}) as the alternating-tail bound
     (p_2−p_3)+(p_4−p_5)+⋯ ≥ 1 — this is the same crux as ll-inclusion-gap's G-INC-1; import whichever route closes.
Key lemmas (claim + mechanism):
  - Double-REFL telescoping A(Q∪G_{n−1}) = 2^{n−1} − q_1 + A(Q'∪G_{n−2}) — because REFL removes the global max,
    applied to 2^{n−1} then to q_1 (valid since q_1 = max after removing 2^{n−1} when q_1 > 2^{n−2}).
  - A(P) ≤ max(P) and A(P) ≥ 0 — because A = p_1 − (p_2−p_3) − (p_4−p_5) − ⋯ with each pair ≥ 0.
Open gaps:
  - GAP-B Case B2 (q_1 ∈ (2^{n−1}−1, 2^{n−1})): need A(Q'∪G_{n−2}) > q_1 − (2^{n−1}−1) ∈ (0,1). PROVED at n=3
    (3-piece Q: analytic case on q_3's dyadic level gives A(Q'∪G_1) > 1 ≥ q_1−3; 4-piece numerically 0 failures,
    min margin 1/2). General n: recurse — Q'∪G_{n−2} is itself a valid B-type problem one level down, so
    A(Q'∪G_{n−2}) ≥ 1 by the same REFL chain (induction on n). Builder: formalize this descent.
  - GAP-A general n (= G-INC-1 crux): the alternating-tail bound for max(Q) ≥ 2^{n−1}. Shared with ll-inclusion-gap;
    if that slug closes it, import; otherwise attack via REFL reducing to the max(Q) < 2^{n−1} problem.
Cases to cover: q_1 ≤ 2^{n−2}; q_1 ∈ (2^{n−2}, 2^{n−1}−1]; q_1 ∈ (2^{n−1}−1, 2^{n−1}); q_3 in level I_0 vs I_1 (B2, n=3).
Watch out for: (a) the tight A=1 witness Q={3,3,2},R={2,2,2,1} is Sub-3a (I_0 fully odd), NOT GAP-B/Sub-3b —
  Sub-3b B3 has min A = 3/2, do NOT chase a phantom tight-at-1 case there; (b) do NOT revive "max(Q)<2^{n−1} ⇒ A≥2"
  (FALSE, min is 3/2); (c) the second REFL needs q_1 > 2^{n−2} to be the max after removing 2^{n−1}.

---

geometric-selfsimilar: advance
Target: c(n) = 2^n/(2^{n+1}−1) — full determination; this slug OWNS the upper bound (XY holds every LB config
  to val ≤ c(n)), now reduced to the single sum-bound μ(X,b) ≤ Σ/(2^{b+1}−1) residual "gap case"
  (distinct X, p_1 < τ, p_2 < τ/2).
Technique: SUM-BOUND reductions R1/R2/R3 + a direct Case-A.A closure + a gap-step-then-R3 two-level argument.
Skeleton:
  1. Whole UB reframed to μ(X,b) ≤ Σ/(2^{b+1}−1) (certified SB + R1/R2/R3 sum-bound-reductions). Regimes A, B1,
     B(n=2), and the R2/R3 boundaries are closed. Residual = gap case only.
  2. CHEAP KILL — Case A.A (p_1 − p_2 > p_3 AND p_1−p_2−p_3 > p_4): the 3-cut "subtract-all" chain (pair p_1 at
     p_2, leftover at p_3, leftover at p_4) gives A = (p_1−p_2−p_3)−p_4 = 2p_1 − 1. Since p_1 < τ and
     2τ − 1 = 1/D_b (identity: 2·Σ·2^b/D_b − 1 = 1/D_b for Σ=1), A = 2p_1−1 < 1/D_b STRICT. Closes the
     "dominant p_1" part of the gap case with NO induction. PROVE THIS FIRST.
  3. Remaining gap case (p_1 ≤ p_2 + p_3): gap-step-then-R3 two-level argument. Pair p_1 at p_2 (Σ' = Σ − 2p_2,
     b' = b−1); the invisible pair {p_2,p_2} drops out and the reduced threshold τ' = Σ'·2^{b−1}/D_{b−1} shrinks,
     so the UNCHANGED p_3 can satisfy the new R3 condition p_3 ≥ τ'/2. Show: for every gap case there exists a
     pairing j s.t. the reduced (X', b−1) is handled by R1/R2/R3 OR is a gap case at b−1 (strict descent in b,
     terminating). If p_3 < τ'/2 after one step, a second gap-step precedes R3.
Key lemmas (claim + mechanism):
  - Case A.A identity A = 2p_1 − 1 — because the subtract-all chain leaves the single alternating tail 2p_1−ΣX,
    and ΣX = 1 (the leftover p_1−p_2−p_3−p_4 = p_1−(1−p_1)); strict from p_1 < τ and 2τ−1 = 1/D_b.
  - Gap-step reduces Σ so p_3 crosses the R3 threshold — because τ' = (Σ−2p_2)·2^{b−1}/D_{b−1} < τ/2·(scaling),
    and the gap-case hypothesis p_2 < τ/2 leaves p_3 relatively large vs τ'.
Open gaps:
  - The gap case with p_1 ≤ p_2 + p_3: prove the algebraic R3-firing condition p_3 ≥ τ'/2 after one gap-step
    (or that two gap-steps suffice). This is the last upper-bound gap. Do NOT attempt to preserve the SB invariant
    step-by-step — PROVED FALSE (Σ'/D_{b−1} ≤ Σ/D_b fails 18/123/315/678 at n=3..6); the descent is in b, not in SB.
Cases to cover: m=2 (halve p_1), m=3 (n=2 B2a/b prototype val = p_1 + p_3/2), Case A.A (p_1 > p_2+p_3),
  gap case p_1 ≤ p_2+p_3 with one vs two gap-steps.
Watch out for: (a) fixed "always-pair-at-p_2" fails 44/222 and "always-pair-at-smallest" fails 95/222 — the
  pairing j must be CHOSEN adaptively, not fixed; (b) partial-shadow does NOT preserve SB — do not reuse it here;
  (c) the strict interior of the gap case is strictly below 1/D_b (tightness only at the R2/R3 boundary p_1=τ or
  p_2=τ/2), so the bound is not tight inside — exploit strictness.

---

NOT built this round (kept live, low Elo, no new machinery): alternating-sum-value (1447 — greedy-XY dead-end
  recorded, its GAP AL = the same LL crux the two LL slugs now push), extremal-smoothing (1362 — S1 "G_n unique
  maximizer" stuck 4+ rounds, no mechanism). No new approach opened: G-INC-1/GAP-A moved materially this round
  (SET IDENTITY two-step induction + double-REFL both close large sub-cases), so the anti-plateau reframe rule
  does NOT trigger; concentrating builder effort on converting the fresh machinery to rigor is the higher-value move.

STRICT anti-stuck rules for every builder: any numeric sanity check must be tiny bounded (<20s) python with
incremental prints; ALWAYS enforce the JOINT CUT BUDGET (#Q-cuts + #R-cuts ≤ n) — unbudgeted grids fabricate
spurious violations; no long silent computation; emit steadily; time-box.

build set: ll-inclusion-gap, ll-dyadic-symdiff, geometric-selfsimilar
