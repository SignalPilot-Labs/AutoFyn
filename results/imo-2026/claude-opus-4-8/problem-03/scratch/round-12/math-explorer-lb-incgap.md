## imo-2026-03 (lens: G-INC-2nt a≥1 branch — direct A(R) evaluation)

- **Distinct openings:**

  **Opening A — Extended Family Lemma (σ-arithmetic for F_{n-2} with a≥1).**
  After ONE Gen-Decomp step at the top level (always valid: h_R=2 for any a∈(0,2^{n-2})), the bound
  A(R)−A(Q) = deficit_top + (A(F_{n-2})−A(Q_lo)) ≥ 1 follows from the SAME 2b-i/2b-ii σ-arithmetic
  as the certified a<1 proof, IF A(F_{n-2})−A(Q_lo) ≥ min(σ_lo, 2−σ_lo) holds at the sub-level
  (σ_lo = 1+a_v−b, same formula as before). The arithmetic: 2b-i gives (a_v+b)+(2−σ_lo) = 1+2b ≥ 1; 2b-ii
  gives (a_v+b)+σ_lo = 1+2a_v ≥ 1. Both hold. The GAP is proving the sub-level sigma-bound for
  F_{n-2} = {a}∪G_{n-3} with a≥1 (not just a<1). The inductive descent a<2^{k-2} still works for
  large n (handle a ∈ [1, 2^{n-4}) by Gen-Decomp descent); the terminal sub-cases a ∈ [2^{n-4}, 2^{n-2})
  at small k need direct argument (see Opening B).

  **Opening B — Direct base-case closure at small k.**
  For k=2 (n=4): F_2 = {a,1,2} with a∈[1,4). |Q_lo|≤2 and ΣQ_lo ∈ [11/2, 8]. The containment
  S_{Q_lo}⊆S_{F_2} = [0,1)∪[a,2) combined with ΣQ_lo≥5.5 forces Q_lo to have large parts; with two parts
  each <thr=4 summing to ≥5.5, the only sub-structures compatible with S-containment give A(Q_lo)≤A(F_2)−1.
  VERIFIED numerically: 496 configs, 0 violations, minimum deficit_top+(A(F_2)−A(Q_lo))=1 at a=2,
  Q=[6,4,3,3]. For k=3 (n=5): same direct argument; 662 configs (half-integer grid), 0 violations,
  minimum=1 at a=4, Q=[12,8,6,6]. These BASE CASES close the residual after the descent in Opening A hits
  k=2 or k=3.

  **Opening C — Minimum-A(R_lo) + tight-case forcing.**
  ANALYTIC CLAIM (numerically confirmed for j=1,...,6):
    A({a}∪G_j) ≥ A(G_{j-1}) for all a∈(0,2^{j+1}), with equality exactly at a=2^j.
  Proof: A({2^j}∪G_j) = A(G_{j-1}) (the pair {2^j,2^j} cancels the 2^j term, leaving A(G_{j-1}));
  for all other a the piecewise formula gives A>A(G_{j-1}). And A(G_{j-1}) = (2^j+(-1)^{j-1})/3 ≥ 1 for
  j≥1 (certified set-identity-selfsimilar). In the top-level problem: R_lo = {a}∪G_{n-3}, j=n-3,
  A(R_lo) ≥ A(G_{n-4}) ≥ 1.

  TIGHT CASE: a=2^{n-3} gives A(R_lo)=A(G_{n-4})=1 (for n=4,5) or 3+ (for n≥6). At n=4: a=2,
  A(R_lo)=1; at n=5: a=4, A(R_lo)=1. For n≥6 min A(R_lo)=3. When A(R_lo)=1 (n∈{4,5}): S_{R_lo}=[1,2)
  (a single band), and the sum constraint ΣQ_lo = 2^{n-2}+a = 3·2^{n-3} forces parts > 2 (above the band
  support), so S_{Q_lo}⊆[1,2) forces Q_lo to be equal pairs with A(Q_lo)=0. VERIFIED: the UNIQUE valid
  Q_lo with ΣQ_lo=12, |Q_lo|≤3, S_{Q_lo}⊆S_{R_lo}=[1,2) for n=5,a=4 is Q_lo={6,6}, A(Q_lo)=0.
  Thus deficit_top+(A(R_lo)−A(Q_lo))=0+1−0=1. ✓

  Opening C combines these two facts:
  (i) A(R_lo)≥1 always.
  (ii) When A(R_lo)=1 (tight), the sum+S-containment forces A(Q_lo)=0.
  Together: A(R_lo)−A(Q_lo)≥1 in the tight sub-case; for all other a, A(R_lo)>1 and the slack absorbs
  any A(Q_lo)>0.

  **Opening D — Iterative descent halting at critical a level.**
  Apply Gen-Decomp at the top level. If a<2^{n-4}: the sub-level R_lo=F_{n-2} also has h=2 (Gen-Decomp
  applies again). Descend until a≥2^{k-2} at some level k; at that point, use Opening B (direct base)
  or Opening C (A(R_lo)≥A(G_{k-3})≥1 plus tight-case forcing). This FINITE DESCENT eventually terminates
  at level k∈{2,3}, which is directly closed by Opening B numerics. The descent depth is at most ⌊log_2(a)⌋+2.

- **Candidate technique(s):**
  Piecewise linear analysis of A({a}∪G_j) combined with the σ-parametrized descent (same as certified
  sigma-family-a-lt-1, extended base). The formula A({2^j}∪G_j)=A(G_{j-1}) and the parity-kill
  (equal-pair forcing from large ΣQ_lo + small S_{R_lo}) are the two structural levers.

- **Cheap-kill candidates:**
  Parity: A(R_lo)=A(G_{n-4})=1 iff a=2^{n-3}; for n≥6 the minimum is 3, and deficit_top+(A(R_lo)−A(Q_lo))≥3
  with room to absorb A(Q_lo). The ONLY case needing tight argument is n∈{4,5}; n≥6 is automatically slack.

- **Knowledge-base entries to use:**
  - gen-decomp-refined: A(R)−A(Q) = deficit_top + (A(R_lo)−A(Q_lo)) with even h_R and S_{Q_lo}⊆S_{R_lo}.
  - sigma-family-a-lt-1 (certified): extends to the sub-level once base cases are closed.
  - set-identity-selfsimilar: A(G_j) = (2^{j+1}+(-1)^j)/3 ≥ 1; use A(G_{j-1}) formula.
  - parity-condition-inc: h (count of Q-parts ≥ thr) must be even; eliminates h-odd configs.
  - forcing-inc-reduction: q_1 ≤ 2^{n-1}−a (Forcing Lemma); constrains ΣQ_lo from below.
  - alt-sum-integral: A(P) = measure(S_P); used in piecewise analysis of A({a}∪G_j).

- **Analogous past problems (cruxes):** Not consulted this round (prior rounds established no close analogs in corpus).

- **Prior progress:**
  G-INC-1 (anchor R=G_{n-1}): PROVEN all n (certified t-ell-mutual-induction).
  G-INC-2nt a<1: PROVEN all n (certified sigma-family-a-lt-1, Step 24).
  UB: PROVEN all n except pure hard case (c) m≥5 (Lemma MK certified).
  OPEN: G-INC-2nt a≥1 (this round's target); UB hard case (c).

- **Dead ends (do not retry):**
  - {Claim_R,T_R} simultaneous mutual induction: NOT descent-closed (O1/O2/O3), abstract Claim_R FALSE.
    Witnesses: R={1,2,2,2,8,16,32} (h odd), R={1,3,3} (Claim_R false). REFUTED R10.
  - Generalized-L1 without fixed R structure: 2880 violations, R9.
  - "INC forces max(Q)≤max(R)": FALSE (counterexample {15/2,15/2,1}/{7,4,2,1,1}), R11.
  - a≥1 Family Lemma F_a via direct descent (F_k→F_{k-2}): breaks at k=2 for a≥1 (h_{F_2}=3, odd).
    The CERTIFIED sigma-family-a-lt-1 lemma already records this scope limitation.
  - Claiming A(F_k)≥1 is sufficient alone: it is, but only when A(Q_lo)=0 is also established;
    need the sum+S-containment forcing argument to bound A(Q_lo).

- **Small-case / intuition notes (all labeled conjecture unless stated):**
  FACT (numeric, 0-violation, n=4, 496 configs, quarter-int grid, a≥1):
    min deficit_top+(A(R_lo)−A(Q_lo)) = 1, at a=2, Q=[6,4,3,3].
  FACT (numeric, 0-violation, n=5, 662 configs, half-int grid, a≥1):
    min deficit_top+(A(R_lo)−A(Q_lo)) = 1, at a=4, Q=[12,8,6,6].
  FACT (analytic, confirmed for j=1,...,6):
    A({2^j}∪G_j) = A(G_{j-1}) and this equals the global minimum of A({a}∪G_j) over a∈(0,2^{j+1}).
  CONJECTURE: The extended Family Lemma A(F_k)−A(Q)≥min(σ,2−σ) holds for all a∈[0,2^{k-1}), k≥2.
    The a<1 case is certified; the a≥1 extension requires proving the direct base at k=2 and k=3,
    then the same inductive descent closes for a<2^{k-2} at each level. Terminal sub-cases with
    a≥2^{k-2} bottom out at k∈{2,3} which are directly closed.
  CONJECTURE: The tight case (A(R_lo)=1) always forces A(Q_lo)=0 via the product of:
    (a) Large ΣQ_lo (≈2^{n-2}+2^{n-3}) forces Q_lo parts above S_{R_lo} support.
    (b) Small S_{R_lo} = [1,2) (single band, measure 1) means Q_lo parts in the support form
        sub-threshold pairs with high sum, and only equal-pair solutions (A=0) achieve the sum target.
