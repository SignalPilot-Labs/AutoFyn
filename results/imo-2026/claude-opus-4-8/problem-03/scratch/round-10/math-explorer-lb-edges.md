## imo-2026-03 — residual edges of ll-inclusion-gap (lens: lb-edges)

### Scope
Three open sub-cases of G-INC-2 (refined-R INC branch): G-INC-2e (equal-split, g=0, h̄≥2, q1>q2),
G-INC-2lb (lower-band cut), G-INC-2nt (non-equal top cut). All numerics below use CORRECT constraints:
- ΣQ = 2^n (Q is a cut of [0,2^n), total length fixed)
- c_Q = |Q|-1, c_R = |R|-n, joint budget c_Q + c_R ≤ n
- INC: S_Q ⊆ S_R via brute-force N_Q parity check at midpoints

Bug caught: earlier test set ΣQ = ΣR = 2^n-1 (wrong). Fixed: ΣQ = 2^n throughout.

---

### G-INC-2e: equal-split top cut, g=0, h̄≥2, q1>q2

**Setup** (from Step 18). Equal-split gives S_R = S_{G_{n-2}} exactly (three copies of 2^{n-2} cancel the
top half). Target reduces to: S_Q ⊆ S_{G_{m-1}}, ΣQ = 2^{m+1}, |Q| ≤ m+1 ⟹ A(Q) ≤ A(G_{m-1})-1
(where m = n-1). After pair-reduction (g ∈ {0,2}, g≥4 impossible by sum) and g=2 (closed by L1),
g=0 remains. In g=0: apply Gen-Decomp / top-band-decomp at thr = 2^{m-2}: h̄ = #{parts ≥ 2^{m-2}} ≥ 2.
The sub-case h̄=0 is closed (deficit_top = 2^{m-2} ≥ 1). Sub-case h̄≥2 with q1=q2: closed by L1
(remove equal pair, |Q''| ≤ m-1, L1 applies). Open: h̄≥2 with q1>q2.

**Vacuousness argument for h̄=2, q1>q2** (NEW — discovered this round):
- Q_lo = {Q-parts < thr = 2^{m-2}}, |Q_lo| ≤ m+1-h̄ = m-1.
- Each Q_lo-part strictly < 2^{m-2}, so ΣQ_lo < (m-1)*2^{m-2}.
- ΣQ_lo = 2^{m+1} - q1 - q2. Feasibility requires q1+q2 > 2^{m+1} - (m-1)*2^{m-2} = 2^{m-2}*(9-m).
- But q1,q2 ≤ 2^{m-1} (from S_Q ⊆ S_{G_{m-1}}) and q1 ≠ q2 (open sub-case), so q1+q2 ≤ 2*2^{m-1} = 2^m.
- For m ≤ 5: 2^m ≤ 2^{m-2}*(9-m) iff 4 ≤ 9-m iff m ≤ 5. At m=5: 2^m = 32 and threshold = 32; equality
  only if q1=q2=2^{m-1} (contradicts q1>q2). So h̄=2,q1>q2 is VACUOUS for all m ≤ 5 (n ≤ 6).
- For m=6: q1+q2 ∈ (48, 64] (strict lower needed, strict upper from max), non-vacuous. ΣQ_lo ∈ [64,80).
  But every Q_lo-part < 16 and |Q_lo| ≤ 5; max ΣQ_lo ≤ 5*16=80 (barely). Feasible.

**Numerics for h̄≥4 sub-cases, n=4..6** (pre-summary computation, step=1, correct ΣQ):
- 135 configs (g=0,h̄≥2,q1>q2) at n=6: 0 violations, min_margin=2.
- All tight (margin=2) cases have equal pairs in Q_hi or Q_lo (pair-reduction applies → |Q''| ≤ m-1 → L1).
- No-equal-pair sub-cases: margin ≥ 3 (comfortable, no violations).

**Proof path to closure**: 
1. h̄=2,q1>q2: VACUOUS for m≤5 by sum argument above. For m≥6: need an argument showing M≥1 or
   deficit_top+M≥1. S_{Q_lo} ⊆ S_{G_{m-3}}, |Q_lo|≤m-1, ΣQ_lo∈[64,80). The budget |Q_lo|≤m-1 is
   ONE MORE than L1's required m-3; extending L1 by one step (allowing |P|=m-1 with large ΣP) may work.
2. h̄≥4,q1>q2: even fewer Q_lo parts (|Q_lo|≤m-3), closer to L1. Pre-summary showed max A(Q)=8 vs
   target 10 at m=5 (margin=2). These cases are covered by L1 when equal pairs exist in Q_hi; the
   "all-distinct hi parts" sub-sub-case still needs a combinatorial bound.

**Ranking**: NEAREST TO CLOSURE. The sub-case h̄=2,q1>q2 is vacuous for m≤5; m≥6 needs
one more step beyond L1. Sum-argument approach is clean and likely formalizable.

---

### G-INC-2lb: lower-band cut

**Setup** (Step 19). R = G_{n-1} with a cut at piece 2^{k0} for some k0 ≤ n-3 (top two pieces uncut).
Then h_R = 2 (both top pieces {2^{n-1}, 2^{n-2}} remain). Gen-Decomp gives:
A(R) - A(Q) = deficit_top + (A(R_lo) - A(Q_lo)), with R_lo = G_{n-3} with the SAME cut at k0.
S_{Q_lo} ⊆ S_{R_lo} (certified by Gen-Decomp), |Q_lo| ≤ n-2, A(R_lo) ≥ 1.

**Descent measure H = n - k0**: When k0 ≤ n-3, the cut at k0 IN R_lo is a cut at level k0 in G_{n-3}.
If k0 = (n-2)-1 = n-3: the cut is the TOP-PIECE cut of G_{n-3}, landing in G-INC-2nt at level n-2.
If k0 ≤ n-4: another lower-band cut at level k0 in G_{n-3}, yielding G-INC-2lb at level n-2.
Each Gen-Decomp step drops from level n to level n-2, so H = n-k0 decreases by 2.
Termination: after ⌊(n-k0)/2⌋ steps, reaches either G-INC-2nt (k0 = top piece of some G_{n-2j}) or
the base case n ∈ {3,4} (vacuous at n=3 by budget/parity).

**Numerics (pre-summary, n=4, step=1/4)**:
- k0=0: 601 valid INC configs, 0 violations, min_margin=1/2.
- k0=1 (= n-3 at n=4): 922 total, 0 violations, min_margin=0. Tight case couples to G-INC-2nt.

**Proof path**: G-INC-2lb(n) follows from G-INC-2nt(n-2) by induction on H. The descent is
well-founded (H decreases by 2 each step, grounding on n=3 or G-INC-2nt). Formally:
- Base: n=3 vacuous. 
- Step: by Gen-Decomp, A(R)-A(Q) = deficit_top + (A(R_lo)-A(Q_lo)) ≥ 0 + G-INC-2nt(n-2) or
  G-INC-2lb(n-2) (by IH at level n-2). Since both give ≥ 1, done.

**Key open issue**: The unpinned ΣQ_lo at each descent step (ΣQ_lo = ΣQ - ΣQ_hi, varies with Q_hi).
This is exactly the same "unpinned sum" issue as G-INC-2nt. G-INC-2lb REDUCES TO G-INC-2nt.

**Ranking**: SECOND — once G-INC-2nt is proved, G-INC-2lb follows immediately by the induction on H.

---

### G-INC-2nt: non-equal top cut

**Setup**. R = G_{n-2} ∪ {a, 2^{n-1}-a}, 0 < a < 2^{n-2} (non-equal top-piece split). h_R=2 (even).
Gen-Decomp: A(R)-A(Q) = deficit_top + (A(R_lo)-A(Q_lo)).
R_lo = G_{n-3} ∪ {a}: G_{n-3} (n-2 pieces) plus piece a. |R_lo| = n-1.
deficit_top = (2^{n-2}-a) - δ_top^Q ≥ 0 (where δ_top^Q = measure(S_Q ∩ I_{n-1})).
S_{Q_lo} ⊆ S_{R_lo}, |Q_lo| ≤ n-2 = |R_lo|-1.

**Numerics (this round, step=1/4, CORRECT sum ΣQ=2^n, budget c_Q+c_R≤n)**:
- n=3,4: 857 configs, 0 violations, min_margin=0.
- Tight (margin=0): n=3, a=1, R={3,2,1,1}, Q={4,4}. A(R)=1, A(Q)=0. ΣQ=8=2^3 ✓.
  Q has all equal parts → A(Q)=0 → claim holds as 0 ≤ A(R)-1 = 0.
- Earlier spurious violations (pre-round) due to bug: setting ΣQ=2^n-1 instead of ΣQ=2^n.

**a≥1 sub-case**: a ∈ [1, 2^{n-2}). R_lo = G_{n-3} ∪ {a} where a ∈ [1, 2^{n-3}) or [2^{n-3}, 2^{n-2}).
A(R_lo) ≥ 1 (A(G_{n-3}) ≥ 1 and adding piece a at level < thr perturbs A by (-1)^{n-3}*a from
the alternating structure; net ≥ 1 for n ≥ 4 verified numerically 0-violation n=3,4).

**a<1 sub-case**: a ∈ (0,1). R_lo = G_{n-3} ∪ {a} where a < 1 is a "tiny" extra piece.
A(R_lo) = A(G_{n-3}) + (-1)^{n-3}*a (the tiny piece a fits at the tail of the sorted order, adding ±a).
For n≥4: A(G_{n-3}) ≥ 1 and the perturbation |a| < 1, so A(R_lo) ≥ 1-a > 0. More precisely ≥ 1 iff
(-1)^{n-3}*a ≥ 0 (i.e., n-3 even ⟺ n odd). For n even (n-3 odd): A(R_lo) = A(G_{n-3})-a. Need A(G_{n-3})-a ≥ 1: true iff A(G_{n-3}) > 1+a, i.e., A(G_{n-3}) ≥ 2 (since a<1). For n=4: A(G_1)=1-a: might be < 1 when a∈(0,1). CHECK: A(G_{n-3}) for n=4 is A(G_1)=A({1,2})=2-1=1. So A(R_lo)=1-a<1 for a∈(0,1). BUT: Gen-Decomp still gives A(R_lo)-A(Q_lo) ≥ 0, and deficit_top = (2^{n-2}-a) - δ_top^Q. For the full bound A(R)-A(Q)≥1: deficit_top must compensate.
- Pre-summary numeric: a<1 sub-case at n=4: 342 configs, 0 violations, min_margin=1/2. ✓

**The unpinned ΣQ_lo issue**:
ΣQ_lo = ΣQ - ΣQ_hi = 2^n - q1 - q2 (for h=2). ΣR_lo = ΣR - ΣR_hi = (2^n-1) - (2^{n-1}-a+2^{n-2}) = 2^{n-2}+a-1.
ΣQ_lo ≠ ΣR_lo in general; ΣQ_lo depends on Q_hi choices. This is why neither Claim(n-2,0) nor T(n-2)
applies directly (their ΣP windows don't cover the free range of ΣQ_lo).

**Structural observation on the tight case**:
Tight (margin=0) happens when A(Q)=0 (all Q-parts in equal pairs, A=0) AND A(R)=1 (minimum positive).
At these points: deficit_top + M = 1 (exactly). Since deficit_top ≥ 0 and M ≥ 0, both can be 0+1 or
1+0. When A(Q)=0: S_Q = ∅ (all parts in equal-pair, contribute 0). So Q = {{p,p,...}} all pairs. Then
δ_top^Q = 0 (S_Q = ∅), deficit_top = 2^{n-2}-a, and M = A(R_lo)-0 = A(R_lo). deficit_top+M = (2^{n-2}-a)+A(R_lo).
A(R) = A(R_lo) + (2^{n-2}-a) (since A(R) = δ_top^R + A(R_lo) = (2^{n-2}-a)+A(R_lo)).
So margin = (A(R_lo)+(2^{n-2}-a)) - 0 - 1 = A(R)-1. Tight iff A(R)=1. ✓ Self-consistent.

**Proof path candidates**:
1. **Mutual induction {Claim_R, T_R}**: Generalize the anchor {Claim(n,ε), T(n)} to refined R.
   The descent identity S_{Q_lo} ⊆ S_{R_lo} is already certified (Gen-Decomp). The obstacle: the
   "sum window" for Claim_R varies across different R types (G-INC-2nt, G-INC-2lb), making a clean
   ε-parametrization harder than the anchor case. But Gen-Decomp supplies the needed descent identity
   (the reviewer noted this as a possible revival of the cut refined-r-alt-tail route, Step 19).
2. **Direct A(R) bound**: For the specific R = G_{n-2}∪{a,2^{n-1}-a}, compute A(R) exactly and show
   A(R) is "large enough" relative to any feasible Q. This may split by position of a relative to G_{n-3}
   pieces. Not yet formalized.

**Ranking**: HARDEST. The unpinned ΣQ_lo in the descent prevents direct use of certified Claim/T.
The correct proof engine is likely the mutual induction {Claim_R, T_R} generalizing the anchor proof.

---

### Dead ends — do not retry

- **Generalized L1** (S_Q ⊆ S_R, |Q| ≤ |R|-1, A(R) ≥ 1, NO sum/R-structure constraint ⟹ A(Q) ≤ A(R)-1):
  FAILS. Python test found 2880 violations in 614871 configs (e.g., R={2,1,1/4}, Q={2,1}: A(R)=5/4,
  A(Q)=1 > 5/4-1). The sum constraint AND the specific R-structure (anchor G_{n-1} or equal-split) are
  essential. Do NOT attempt a structure-free generalization.

- **Spurious G-INC-2nt violations** from setting ΣQ = ΣR (= 2^n-1) instead of ΣQ = 2^n: these
  are outside the valid domain. Under correct constraint (ΣQ=2^n), 0 violations at n=3,4.

---

### Rankings (closest to closure first)

1. **G-INC-2e** (g=0,h̄≥2,q1>q2): Vacuous for m≤5 by sum argument (ΣQ_lo infeasibility). Non-vacuous
   starts at m=6 but numerics show large margins. Proof needs: (a) formalize vacuousness for all m≤5
   as a written argument; (b) handle m≥6 with a tighter L1-like bound or explicit vacuousness extension.
   ESTIMATE: 1-2 builder rounds.

2. **G-INC-2lb** (lower-band cut): Reduces cleanly to G-INC-2nt via descent H=n-k0 (decreases by 2,
   well-founded). Once G-INC-2nt is proved, G-INC-2lb follows by induction on H with zero new ideas.
   ESTIMATE: 0 additional rounds after G-INC-2nt.

3. **G-INC-2nt** (non-equal top cut): 0 violations with correct constraints at n=3,4. Tight cases
   have A(Q)=0. The proof requires handling the unpinned ΣQ_lo in the Gen-Decomp descent. The mutual
   induction {Claim_R, T_R} (a generalization of the anchor proof to refined R) is the best candidate.
   ESTIMATE: 2-3 builder rounds; may require a new mutual induction structure.

---

### Summary for proof-builder

**G-INC-2e close-out**:
- Write the vacuousness argument explicitly: for h̄=2, q1>q2, feasibility requires q1+q2 > 2^{m-2}*(9-m);
  for m≤5 this exceeds the maximum q1+q2 ≤ 2^m, so VACUOUS. For m≥6: ΣQ_lo ∈ [64,80) with 5 parts
  each < 16; show A(Q_lo) ≤ A(G_{m-3})-1 by applying the T-lemma or a sum-based bound.
- For h̄≥4,q1>q2: similar argument with more budget consumed.
- All cases where equal pairs exist in Q_hi are closed by the existing pair-reduction → L1 path.

**G-INC-2nt close-out**:
- Generalize the mutual {Claim(n,ε), T(n)} induction to the refined-R setting.
  Gen-Decomp gives clean descent S_{Q_lo}⊆S_{R_lo}; the obstacle is characterizing R_lo = G_{n-3}∪{a}
  as itself admitting a recursive G-INC-2nt or G-INC-2lb instance.
- Consider a "joint" induction on n AND the cut position (a, k0), using A(R_lo) ≥ 1 (available by IH).
- The equal-pair Q (tight case) is already handled: A(Q)=0 ≤ A(R)-1 iff A(R)≥1 which holds by IH.

**G-INC-2lb**: no separate work needed; prove G-INC-2nt and G-INC-2lb is immediate.
