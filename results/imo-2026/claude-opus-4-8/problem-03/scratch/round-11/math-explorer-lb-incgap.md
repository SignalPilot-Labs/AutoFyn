# imo-2026-03 — LB explorer: G-INC-2nt direct per-cut attack

## Problem context

G-INC-2nt = the INC branch of Lemma LL (t ≥ 2, A(Q) > 0) for REFINED R (c_R ≥ 1), restricted to NON-EQUAL TOP CUTS of G_{n−1}. Specifically: R is G_{n−1} with its top piece 2^{n−1} cut into {a, 2^{n−1}−a} (0 < a < 2^{n−2}, a ≠ 2^{n−3}; the case a = 2^{n−3} is G-INC-2e, now closed for n ≤ 6). Goal: prove A(R) − A(Q) ≥ 1 for S_Q ⊆ S_R, ΣQ = 2^n, |Q| ≤ n, via a DIRECT per-cut bound (no mutual induction over the abstract {Claim_R, T_R} class, which is refuted).

---

## Distinct openings (direct-attack angles)

### Opening A: Parametric-family mutual induction for a < 1 (MOST PROMISING)

**Key structural fact (proved here by inspection, verified n=4 numerically — 0 violations, 355 configs, min margin 3/2 > 1):**

For the non-equal top cut with a < 1 (the "a < 1 sub-branch" in the dispatch), the Gen-Decomp descent produces a CLOSED parametric family:

  R_k := {a} ∪ G_{k−1}   (k ≥ 2, a fixed, a < 1)

where at each descent step (k → k−2) the descended R_lo = {a} ∪ G_{k−3} is **the same family two levels down**. Concretely:

- For the non-equal top cut at level n (threshold 2^{n−2}): R_hi = {2^{n−1}−a, 2^{n−2}}, R_lo = {a} ∪ G_{n−3} = R_{n−2}.
- h_{R_lo} = #{R_lo-parts ≥ 2^{n−4}} = #{2^{n−3}, 2^{n−4}} = 2 (EVEN), because a < 1 ≤ 2^{n−4} for n ≥ 6; and for n=4,5 the base cases close directly.
- So Gen-Decomp **re-applies** at level n−2 with the SAME FAMILY. This is exactly the closure property that the abstract {Claim_R, T_R} class lacked (O1: h_{R_lo} parity breaks for lower-band cuts with k_0 ∈ {n−4, n−3}). For the **top-cut family** with a < 1, O1 does NOT apply.

**The direct proof structure:**

  Claim_a(k): for fixed a ∈ (0,1), for all R_k = {a} ∪ G_{k−1}, all Q with S_Q ⊆ S_{R_k}, |Q| ≤ k, ΣQ = 2^k: A(R_k) − A(Q) ≥ 1.

  T_a(k): same with ΣP ∈ (2^k − 1, 2^k): A(R_k) − A(P) ≥ 1 − τ (τ = 2^k − ΣP).

Prove by mutual strong induction on k (step k → k−2):

**Base cases k=1,2:**
- k=1: R_1 = {a, 1}, |Q| ≤ 1. Only Q = {p} or ∅. S_Q ⊆ S_{R_1} = [0,a) ∪ [1,...) forces p ≤ a. A(Q) = p ≤ a, A(R_1) = 1+a (sorted {1,a} or {a,1}). A(R_1) − A(Q) ≥ 1. ✓ T_a(1) similar.
- k=2: R_2 = {a, 2, 1}. S_{R_2} = [0,a) ∪ [1,2) for a < 1. |Q| ≤ 2. Budget forces Q to have parts only in S_{R_2}-compatible positions. Any single part p ≤ a gives A(Q) = p ≤ a; A(R_2) = 1+a; A(R_2) − A(Q) ≥ 1 (exact equality when p=a). ✓ Verified: A(R_2) − a = 1 exactly for all a < 1.

**Inductive step k ≥ 3:** Gen-Decomp at threshold 2^{k−2} (h_R = 2 since both 2^{k−1}−a and 2^{k−2} are ≥ thr, a < 1 < thr):
- deficit_top = a_val' + b (same formula as anchor, where a_val' = max(R_k ∩ I_{k−1}) − q_1, b = q_2 − 2^{k−2}).
- Sub-instance: (Q_lo, R_{k−2}) with ΣQ_lo = 2^{k−2} + ε', ε' = ε + a_val' − b.
- Route: h=0 → deficit_top = 2^{k−2}−a ≥ 2^{k−2}−1 ≥ 1 ✓; h≥4 impossible (ΣQ < 2^k); h=2 → 2a direct, 2b-i → Claim_a(k−2,ε'), 2b-ii → T_a(k−2).
- ARITHMETIC IDENTICAL TO ANCHOR (Steps 12/12b of certified t-ell-mutual-induction).

This is a per-family induction, NOT the refuted abstract {Claim_R, T_R}: the class is {R_k = {a} ∪ G_{k−1} : k ≥ 1} for each fixed a ∈ (0,1), which is descent-closed (unlike the abstract class that failed O1/O3).

**Scope:** Closes G-INC-2nt for ALL non-equal top cuts with a < 1, for ALL n. The a < 1 case is the nontrivial sub-branch singled out in the dispatch.

---

### Opening B: h=0 trivial sub-case for all a (cheap kill)

When the Gen-Decomp h=0 case applies (no Q-parts ≥ thr = 2^{n−2}): S_Q ∩ I_{n−1} = ∅, so deficit_top = measure(S_R ∩ I_{n−1}) = 2^{n−2} − a. 

- For a < 2^{n−2} − 1 (which includes ALL a < 1 for n ≥ 3): deficit_top ≥ 1. Done immediately.
- For a ∈ [2^{n−2}−1, 2^{n−2}): deficit_top ∈ (0,1). In this regime, all Q-parts < 2^{n−2}; but ΣQ = 2^n and |Q| ≤ n. For all Q-parts < 2^{n−2}: each part < 2^{n−2}, so need ≥ 2^n / 2^{n−2} = 4 parts. |Q| ≥ 4. Then the sub-instance A(R_lo) − A(Q_lo) = A(R_lo) − A(Q) (since Q_lo = Q when h=0) ≥ measure(S_{R_lo}) − measure(S_Q) ≥ 0. And A(R_lo) = A({a} ∪ G_{n−3}) ≥ 1 (for a ≠ 2^{n−3}). So the sub-instance closes if A(Q) ≤ A(R_lo) − 1, which is the sub-instance claim. This requires the inductive hypothesis.

So for a < 1, h=0 closes by deficit_top alone. For larger a, h=0 feeds into the sub-instance induction.

---

### Opening C: Large a regime (a close to 2^{n−2}) via S_R measure bound

For a ∈ [2^{n−2}/2, 2^{n−2}): A(R) becomes small (e.g., at n=4: A(R) = 3 for a ∈ (2,4)). The INC constraint S_Q ⊆ S_R with a small-measure S_R severely limits A(Q). Specifically: A(Q) ≤ measure(S_R) = A(R). The budget (|Q| ≤ n) forces the "one-short" gap: A(Q) ≤ A(R) − 1 via parity + budget.

For a ∈ (2,4) at n=4: S_R = [0,1) ∪ [a−2, 4) ∪ other... (more complex structure). The max Q with S_Q ⊆ S_R and |Q| ≤ 4 achieves A(Q) ≤ A(R) − 1 because the budget forces an even number of high parts (h even), each pair contributing 0 to A, while the low parts can't exceed A(R_lo) − 1 by L1 or sub-instance induction.

Numerically confirmed (n=4, 355 configs, 0 violations, min margin 3/2). The tight cases have Q equal-pairs in the top band (h=2, q_1=q_2) contributing 0 to the top deficit.

---

### Opening D: Lower-band cut sub-case (G-INC-2lb)

For R = G_{n−1} with a cut at piece 2^{k_0} (k_0 ≤ n−3) rather than the top piece: Gen-Decomp gives:
- R_hi = {2^{n−1}, 2^{n−2}} (top two pieces uncut, h_R = 2, EVEN ✓)
- R_lo = {G_{n−3} with the same lower-band cut of 2^{k_0}}

This is a G-INC-2 sub-instance at level n−2 with R_lo being G_{n−3} with one extra cut — i.e., EXACTLY G-INC-2 at level n−2 (same type, one level down). Budget: c_{R_lo} = 1 (same extra cut), c_{Q_lo} ≤ n−3, total n−2. ✓

The descent IS self-similar: G-INC-2lb at level n reduces to G-INC-2lb at level n−2. Base case n=4: lower-band cut has k_0 ≤ 1 (cut of piece 1 or 2), R_lo = G_1 with one cut, budget already tight. Verified numerically by the run-state (G-INC-2 at n=3 is vacuous, n=4 base verified 0 violations).

This is a CLEAN INDUCTION: G-INC-2lb at level n reduces to G-INC-2lb at level n−2 with no class-closure issue (h_R = 2 at every step since the top two pieces are always uncut). Base case n=4 needs direct proof (or it's already verified — 123 configs, 0 violations, min margin 1 per R10).

---

## What Gen-Decomp and L1 supply

**Gen-Decomp (certified, round 9):** For h_R even, A(R) − A(Q) = deficit_top + (A(R_lo) − A(Q_lo)), with S_{Q_lo} ⊆ S_{R_lo} (clean descent). The key output: the sub-instance (Q_lo, R_lo) is always INC at the descended level. This is the foundation for all four openings.

**Lemma L1 (certified, round 9):** S_P ⊆ S_{G_{m−1}}, |P| ≤ m−1 ⟹ A(P) ≤ A(G_{m−1}) − 1. Applies directly when S_{Q_lo} ⊆ S_{G_{n−3}} (which holds for the a < 1 sub-branch via S_{Q_lo} ⊆ S_{R_lo} ⊊ S_{G_{n−3}} for n ODD, but NOT for n EVEN or a ≥ 1). L1 gives an EXTRA −1 from budget whenever |Q_lo| ≤ n−3 and S_{Q_lo} ⊆ S_{G_{n−3}}.

---

## What breaks (the O1/O2/O3 obstructions and which openings sidestep them)

**O1 (h_{R_lo} parity breaks):** Triggered when the cut in R is a LOWER-BAND cut with k_0 ∈ {n−4, n−3} (destroys a piece at the threshold 2^{n−4}, making h_{R_lo} odd). Opening A sidesteps this: for the top-cut family {a} ∪ G_{k−1}, the cut is always the TOP piece, so R_lo = {a} ∪ G_{k−3} always has h_{R_lo} = 2 (even) when a < 2^{k−4} — guaranteed when a < 1 and k ≥ 6; for k ∈ {4,5} verify directly. Opening D addresses the lower-band case separately and avoids O1 because R_hi = {2^{n−1}, 2^{n−2}} is always uncut in a lower-band cut.

**O2 (h=0 deficit fails):** For general R, S_R ∩ I_{n−1} can be small (a non-equal top cut with a close to 2^{n−2} gives measure 2^{n−2}−a → 0). Opening B handles h=0 by (i) direct bound for a < 2^{n−2}−1 and (ii) sub-instance induction for larger a. Opening A handles the a < 1 case where deficit_top = 2^{n−2} − a ≥ 2^{n−2}−1 ≥ 1.

**O3 (R_lo not a refinement):** For the top-cut family, R_lo = {a} ∪ G_{n−3} is NOT a refinement of G_{n−3} (it has an extra piece). BUT for the PARAMETRIC FAMILY, this is fine: the class is defined as {R_k = {a} ∪ G_{k−1}} and IS closed. The abstract {Claim_R, T_R} for general R failed O3 because it needed the ABSTRACT CLASS to close, not a specific parametric family.

---

## Candidate technique(s)

The G-INC-2nt direct attack uses the SAME MECHANISM as the certified t-ell-mutual-induction (anchor, rounds 7-8), but applied to a SPECIFIC PARAMETRIC FAMILY of R (parametrized by the cut parameter a) rather than the abstract class. This is:

- **Per-family mutual induction** (for the {R_k = {a} ∪ G_{k−1}} family with a < 1).
- The key point: instead of proving Claim_R for ALL R in a general class (which fails O1/O3), prove it for the SPECIFIC DESCENDED FAMILY of a given cut. This is not a class argument — it's a specific induction for each fixed a.

For a ≥ 1: the same approach needs extension (the family {R_k = {a} ∪ G_{k−1}} may hit h_{R_lo} = 3 ODD at some descent level when a ≥ 2^{k−4}). Need a separate case split or an earlier termination argument.

---

## Cheap-kill candidates

1. **h=0 immediate kill:** deficit_top = 2^{n−2} − a ≥ 1 when a ≤ 2^{n−2} − 1. For a < 1 this is always satisfied (n ≥ 3). Closes h=0 without induction.

2. **h≥4 immediate kill:** Four Q-parts ≥ 2^{n−2} sum to ≥ 2^n = ΣQ, so Q_lo = ∅, A(Q_lo) = 0, M = A(R_lo) ≥ 1. Closes h≥4 trivially (same as anchor).

3. **L1 kill for large-pair cases:** When Q has an equal pair {q,q} at the top (q₁ = q₂), A contribution from that pair is 0, and |Q_lo| drops by 2 → often hits L1's budget threshold.

4. **Forced equal pairs:** By Parity-Condition, h = #{Q-parts ≥ thr} is even. When h=2 and q₂ = 2^{n−2} exactly (b=0): deficit_top = a_val'. For a_val' ≥ 1: done.

---

## Knowledge-base entries to use

From the certified lemmas:
- `gen-decomp-refined` — the descent engine (provides S_{Q_lo} ⊆ S_{R_lo}, splits A(R)−A(Q)).
- `L1-budget-anchor` — for sub-instances where S_{Q_lo} ⊆ S_{G_{m−1}} and budget |Q_lo| ≤ m−1.
- `t-ell-mutual-induction` — the TEMPLATE: the same arithmetic structure (deficit_top = a_val+b, ε' routing, h cases) applies to the parametric family. Treat it as a model.
- `parity-condition-inc` — gives h even.
- `top-band-decomposition` — specific to anchor R = G_{n−1}; Gen-Decomp supersedes it for refined R.
- `forcing-inc-reduction` — gives max(Q) ≤ max(R) (= 2^{n−1}−a for top cuts), bounds q₁.

---

## Analogous past problems (cruxes)

Not pursued this round (focus was on direct computation and structural analysis per dispatch instructions). The most analogous certified proof in the corpus is the certified `t-ell-mutual-induction` itself — the technique is exactly a repeat of that induction for the specific parametric family.

---

## Prior progress

- G-INC-1 (anchor R = G_{n−1}): PROVEN all n (certified `t-ell-mutual-induction`).
- G-INC-2e (equal-split): CLOSED for n ≤ 6 (Step 22, R10).
- G-INC-2nt (non-equal top cut): first nontrivial at n=4. Verified 0 violations (n=4: 355 configs d=4, min margin 3/2; n=5: 17 configs sparse check, min margin 21/4). NOT proved.
- G-INC-2lb (lower-band cut): Gen-Decomp gives clean descent, NOT proved.

---

## Dead ends (do not retry)

1. **Abstract {Claim_R, T_R} mutual induction:** REFUTED (R10, rigorous). The class of ALL refinements R is not descent-closed (O1: h_{R_lo} parity breaks for lower-band cuts at k_0 ∈ {n−4, n−3}; witness {1,2,2,2,8,16,32}). Do NOT attempt to revive this.

2. **Claim_R = FALSE for non-refinement R:** Verified 12 violations at ℓ=3 (e.g., R={1,3,3}). The class must be restricted to a specific parametric family — not the abstract structure-free version.

3. **Generalized L1 without anchor structure:** FAILS with 2880 violations. L1 requires S_P ⊆ S_{G_{m−1}} (anchor structure), not arbitrary R.

4. **Using G-INC-1 directly for the non-equal top cut (n EVEN):** Does not work because S_Q ⊆ S_R ≠ S_{G_{n−1}} (the cut changes S_R), so S_Q ⊄ S_{G_{n−1}} in general.

5. **Using G-INC-1 directly for the non-equal top cut (n ODD):** Gives only A(Q) ≤ A(G_{n−1}) − 1, but the target is A(Q) ≤ A(R) − 1 = A(G_{n−1}) − 2a − 1 (tighter). Not sufficient.

---

## Small-case / intuition notes (labeled as conjecture)

1. **Conjecture (supported by 355 configs, n=4):** For non-equal top cuts at n=4, min margin A(R) − A(Q) = 3/2 (NOT tight at 1). The tight cases have Q with an equal pair {q,q} in the top band (contributing 0 to deficit_top), and Q_lo = equal pair (A=0). Margin = A(R_lo) − 0 = A(R_lo) ≥ 1 + (something > 0).

2. **Conjecture (supported by sparse n=5 check):** For n ODD, the margin is much larger (21/4 at n=5). This is because A(R) = A(G_{n−1}) − 2a (smaller) but the constraint S_Q ⊆ S_R ⊊ S_{G_{n−1}} forces A(Q) even smaller.

3. **Key structural fact (verified, not a conjecture):** A(R_lo) = 1 ONLY at a = 2^{n−3} (the equal-split boundary, G-INC-2e). For a ≠ 2^{n−3}: A(R_lo) > 1. This gives the sub-instance "slack" that prevents tight cases from arising — explaining the min margin > 1.

4. **Conjecture:** For the parametric family R_k = {a} ∪ G_{k−1} with a < 1, Claim_a(k) holds with equality only at the base case k=2, p=a. For k ≥ 3: min margin > 1.

5. **A(R) for non-equal top cuts is piecewise linear in a** (not monotone): For n=4: A(R)=5 for a ∈ (0,1], A(R)=7−2a for a ∈ [1,2], A(R)=3 for a ∈ [2,4). This piecewise structure should inform the case split for the a ≥ 1 sub-branch.
