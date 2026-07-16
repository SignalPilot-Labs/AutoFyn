## imo-2026-03 — dyadic-topcut / G-GAP / Sub-3b-refined-R bucket (iii) lens

### Background (what's already closed)

After R8, the ll-dyadic-symdiff approach covers Lemma LL (t ≥ 2) as follows:
- **Cases 1/2/Sub-3a (R-agnostic core):** 91.6% of n=3 refined configs. CLOSED for ANY R with max(R) ≤ 2^{n-1}, A(R) ≥ 1.
- **Anchor R=G_{n-1}, B3a/B3b:** CLOSED for all n (double-REFL).
- **Anchor R=G_{n-1}, B3c → (B2*):** closed at n=3; general n = shared crux GAP-A/G-INC-1. NOW PROVEN for all n (T(ℓ) mutual induction, certified t-ell-mutual-induction.md).
- **Anchor R=G_{n-1}, B1/B2 → GAP-A:** reduces to A(Q'∪G_{n-1}) ≤ max(Q)-1. NOW PROVEN for all n via same T(ℓ).
- **Refined R, top-uncut (bucket ii), B3a-ref/B3b-ref:** CLOSED all n. Residual: (B2*)-ref.
- **Refined R, top-CUT (bucket iii):** the residual this lens scouted.

So: the ONLY remaining lower-bound gap in ll-dyadic-symdiff after R8+R9 is
**bucket (iii) = the top-cut refined-R residual** (plus the related G-INC-2 and the (B2*)-ref from bucket ii).

---

### (a) Structural characterization of bucket (iii)

**Definition:** max(Q) < 2^{n-1} AND max(R) < 2^{n-1} (the top piece 2^{n-1} of G_{n-1} was CUT in R), after removing Cases 1/2/Sub-3a.

**Key forced constraints:**
- ΣQ = 2^n with all parts of Q strictly below 2^{n-1}. With two parts < 2^{n-1} summing to < 2^n, a third part must compensate; in fact **|Q| ≥ 3 is NECESSARY** (if |Q|=2: Q={a,2^n-a} with a < 2^{n-1} forces max(Q)=2^n-a > 2^{n-1}, contradiction). So c_Q ≥ 2.
- c_R ≥ 1 (top piece cut). Combined with budget c_Q + c_R ≤ n: c_Q + c_R ≥ 3, so **n ≥ 3** (bucket (iii) is vacuously empty for n ≤ 2).
- For **n=3**: budget forces c_Q=2, c_R=1 EXACTLY (tight, no slack). |Q|=3, |R|=|G_2|+1=4, |P|=7.
- For **n=4**: three sub-cases: (c_Q,c_R) ∈ {(2,1),(2,2),(3,1)}; |Q| ∈ {3,4}, |R| ∈ {5,6}.

**Numerics (verified, budget enforced):**
- n=3, step=1/2: 20 configs (before Case1/2/Sub3a exclusion; corrected 42 after proper exclusion at step=1/4). Min A = 3/2.
- n=3, step=1/4: 42 configs. A-values in {3/2, 2, 5/2}. Min A = 3/2. Zero violations of A ≥ 1.
- n=3, step=1/8: 476 configs (partial). Min A = 5/4. Zero violations of A ≥ 1.
- n=4, step=1/2: 188 configs. A-values in {2, 3, 4, 5, 6}. Min A = 2. Zero violations.

**The infimum of A in bucket (iii) is 1, NOT ACHIEVED in-bucket (only in the limit).** Near-tight family: Q = {2^{n-1}-ε, 2^{n-1}-ε, 2ε}, R = some top-cut refinement with A(R) = 1+O(ε). S_Q = [0, 2ε) (tiny), S_R = [L, L+1) for some integer L ≥ 1 (away from 0). S_Q ∩ S_R = ∅ → A = 2ε + A(R) → 1 from above. The A=1 limit corresponds to max(Q)→2^{n-1} which lands in **bucket (i)** (B2 case, handled by Lemma REFL + T(ℓ) → CLOSED). So bucket (iii) is an open set bounded away from A=1 only infinitesimally.

---

### (b) What's special/harder about top-CUT vs top-uncut

**Bucket (ii) — top-uncut** (the "good" case): max(R) = 2^{n-1} is the UNIQUE global maximum of P = Q∪R (since max(Q) < 2^{n-1}). Certified Lemma REFL (R-agnostic) immediately applies:

    A(Q∪R) = 2^{n-1} − A(Q∪R'),   R' = R\{2^{n-1}}.

This removes the top piece and leaves R' refining G_{n-2} — a clean level-down structure. The second REFL (REFL-gen on max(Q)) telescopes to the closed formula. The anchor G_{n-1} was never used explicitly.

**Bucket (iii) — top-CUT** (the hard case): max(P) = max(max(Q), max(R)) < 2^{n-1}. There is NO piece at 2^{n-1}. Applying REFL-gen to max(P) = M < 2^{n-1} removes M, but:
- The remainder (Q∪R)\{M} has max < 2^{n-1} still — no level-down collapse occurs.
- The identity A(Q∪R) = M − A(remainder) requires the upper bound A(remainder) ≤ M−1. This is the **GAP-A crux for refined R** — the alternating-tail +1 inequality in a setting where M is not an integer (on a rational grid, A(remainder) ≤ M − step < M − 1 may fail for step < 1).
- No "first reflection at 2^{n-1}" is available to create the clean level-down structure of bucket (ii).
- The SET IDENTITY (S_{G_{n-1}} ∩ [0, 2^{n-2}) = S_{G_{n-3}}) used in the anchor T(ℓ) induction is G_{n-1}-SPECIFIC and has no known analogue for a refined R with top piece cut.

The obstruction: **the first REFL step in the double-REFL telescoping requires an anchor piece at 2^{n-1}, which bucket (iii) destroys by cutting it.**

---

### (c) Does REFL or REFL-gen give leverage?

**REFL-gen applies** (it only requires max(R) ≤ max(Q), and in bucket (iii) we can always take the global max of Q∪R as the reflection anchor). Specifically:

If max(Q) ≥ max(R): A(Q∪R) = max(Q) − A(Q'∪R), need A(Q'∪R) ≤ max(Q)−1.
If max(R) > max(Q): A(Q∪R) = max(R) − A(Q∪R'), need A(Q∪R') ≤ max(R)−1.

In both cases: **this reduces to the GAP-A upper-bound crux for a refined R** (the same alternating-tail +1 inequality that was the bottleneck before T(ℓ) closed it for the anchor). The difference: here max(P) < 2^{n-1} (not at 2^{n-1}), so the "tight window" is different.

**The double-REFL can be applied in two steps:** Let M_Q = max(Q), M_R = max(R). If M_Q ≥ M_R: first remove M_Q (REFL-gen), giving A(Q∪R) = M_Q − A(Q'∪R). If then M_R ≥ max(Q'): second remove M_R (REFL-gen again), giving A(Q∪R) = M_Q − M_R + A(Q'∪R''). This is the double-REFL formula for bucket (iii):

    A(Q∪R) = M_Q − M_R + A(Q'∪R''),

valid when M_Q ≥ M_R ≥ max(Q') (second condition depends on Q'). This telescoping gives:
- A(Q∪R) ≥ 1 iff A(Q'∪R'') ≥ 1 − (M_Q − M_R).

If M_Q ≈ M_R (close maxima): RHS ≈ 1, recovering the same tight target. If M_Q ≫ M_R: RHS < 1, giving slack. The bucket (iii) difficulty is precisely when M_Q ≈ M_R (both close to 2^{n-1}).

**Conclusion: REFL-gen gives a useful reduction in the easy sub-case (M_Q ≫ M_R) but in the tight sub-case (M_Q ≈ M_R ≈ 2^{n-1}-ε) it reduces to A(Q'∪R'') ≈ 1 — still requiring a proof of the alternating-tail bound for a "smaller" refined system. The iterative multi-step telescoping is viable but needs a termination argument.**

Concrete example (verified): Q=[15/4, 13/4, 1], R=[15/4, 2, 1, 1/4] (n=3, bucket iii):
- First REFL (max Q = max R = 15/4, remove from Q): A(Q∪R) = 15/4 − A(Q'∪R), Q'={13/4,1}.
- A(Q'∪R) = 9/4 (computed directly). Need ≤ 15/4 − 1 = 11/4. YES: 9/4 ≤ 11/4. ✓
- Second REFL (max R=15/4 > max Q'=13/4, remove from R): A(Q'∪R) = 15/4 − A(Q'∪R''), R''={2,1,1/4}.
- A(Q'∪R'') = 3/2. So A(Q∪R) = 15/4 − (15/4 − 3/2) = 3/2 ≥ 1. ✓
- The chain: A(Q∪R) = 15/4 − 15/4 + A(Q'∪R'') = A(Q'∪R'') = 3/2. (Both maxima canceled!)
- Need A(Q'∪R'') ≥ 1: YES, 3/2 ≥ 1. This is a (B2*)-ref type sub-target.

---

### (d) Unifying refined-R lemma shared with G-INC-2

**G-INC-2 (ll-inclusion-gap):** S_Q ⊆ S_R for refined R. Need A(G_{n-1}) − A(Q) ≥ 1, i.e., the alternating-tail bound O_Q ≤ O_{G_{n-1}} for INC configs with refined R. Currently OPEN.

**G-GAP (ll-inclusion-gap) / bucket (iii) (ll-dyadic):** S_Q ⊄ S_R. Need measure(S_Q △ S_R) ≥ 1.

**Parity structure determines which applies:**

For bucket (iii) at n=3: |Q|=3 (ODD), |R|=4 (EVEN). N_Q(0+)=3 odd → S_Q contains [0, min_Q_piece). N_R(0+)=4 even → S_R does NOT contain [0, ε). Therefore **S_Q ⊄ S_R for ALL n=3 bucket (iii) configs** (structural, not just numeric). Verified: 0 containment cases out of 42 bucket (iii) configs at 1/4-grid.

For n=4 with (c_Q=2, c_R=1): |Q|=3 (ODD), |R|=5 (ODD). Both |Q| and |R| are odd → both S_Q and S_R contain [0, ε) → containment (S_Q ⊆ S_R) is POSSIBLE. So **G-INC-2 and bucket (iii) overlap at n=4 for the (c_Q=2,c_R=1) sub-case**. This is where a unifying lemma matters.

For n=4 with (c_Q=2, c_R=2) and (c_Q=3, c_R=1): |Q|=3(ODD)/|R|=6(EVEN) and |Q|=4(EVEN)/|R|=5(ODD) — different parities, so S_Q ⊄ S_R and S_R ⊄ S_Q structurally (same argument as n=3). Only the GAP branch.

**Potential unifying lemma:** A(Q∪R) ≥ 1 for any Q (partitioning 2^n with all parts < 2^{n-1}), any R (refining G_{n-1} with max(R) < 2^{n-1}, A(R) ≥ 1), budget ≤ n. This would close ALL of: bucket (iii), G-INC-2 (INC branch within bucket iii), and G-GAP (non-containment branch). The T(ℓ) mutual induction structure from t-ell-mutual-induction.md is the natural template: adapt Claim(n,ε)/T(n) to handle refined R by replacing "S_P ⊆ S_{G_{n-1}}" with structural constraints on Q and R separately.

**No known SET IDENTITY or top-band decomposition for refined R.** The anchor's key tool was S_{G_{n-1}} ∩ [0,2^{n-2}) = S_{G_{n-3}}, which is G_{n-1}-specific. For a refined R with top piece cut, the analogous identity would relate the "lower part" of S_R to a G_{n-3}-refinement — this doesn't obviously hold. The builder should NOT assume this identity transfers.

---

### (e) Concrete n=4 verifiable sub-target for bucket (iii)

**Sub-target:** For all Q (partitioning 16 into parts each < 8), all R (refining G_3={1,2,4,8} with top piece 8 CUT, max(R) < 8), with joint budget c_Q + c_R ≤ 4 and A(R) ≥ 1:
    A(Q∪R) ≥ 1.

**Verified:** 188 configs at step=1/2, min A=2. Zero violations. A strict A ≥ 2 > 1 at coarse grid.

**First nontrivial test:** run step=1/4 for n=4 (sub-unit pieces will appear, tighter configs will emerge). Expect min A ≈ 5/4 or 3/2 (by analogy with n=3 pattern).

**The (c_Q=2,c_R=1) sub-case** (|Q|=3 odd, |R|=5 odd) is the first to have possible S_Q ⊆ S_R configurations (parity match at 0). A builder should check this sub-case specifically at step=1/4 for n=4 to see whether INC (containment) configs appear and what A looks like.

**Pattern of infimum A in bucket (iii) by step (n=3):**
- step=1/2: min A = 2
- step=1/4: min A = 3/2
- step=1/8: min A = 5/4

Conjecture: min A ≈ 1 + step (infimum = 1, achieved in limit only). Specifically the near-tight family Q={4-ε, 4-ε, 2ε}, R={top-cut refinement with sub-piece ε near 0} gives A = 1 + O(ε).

---

### Key openings for the outliner

**Opening A: Disjoint sub-case (immediately provable)**
If S_Q ∩ S_R = ∅: A = A(Q) + A(R) − 0 = A(Q) + A(R) ≥ A(R) ≥ 1. Done. This covers the near-tight limit. At n=3 step=1/4: 9/42 bucket (iii) configs are disjoint. This sub-case can be stated as a certifiable lemma immediately.

**Opening B: Parity argument (n=3 non-containment)**
For n=3 bucket (iii): |Q|=3(ODD) → S_Q always contains [0,ε). |R|=4(EVEN) → S_R never contains [0,ε). So S_Q ⊄ S_R structurally. This means A(Q∪R) ≠ A(R)−A(Q) (INC formula inapplicable). Instead A = A(Q)+A(R)−2B with B < A(Q). Now: A ≥ A(R) − A(Q) + 2(A(Q)−B) ≥ A(R) − A(Q) since A(Q) ≥ B. Need A(R) ≥ A(Q) + 1... but we only know A(R) ≥ 1. This suggests a structural bound A(Q) ≤ A(R) − 1 for all n=3 bucket (iii) configs.

**Opening C: Multi-step REFL telescoping (promising for overlap case)**
As shown in the concrete example: applying REFL-gen alternately on max(Q) and max(R), the two maxima cancel and we reduce to A(Q'∪R'') ≥ 1, where Q'=Q\{max(Q)}, R''=R\{max(R)}. This is a sub-instance of the SAME type (smaller multisets, still partitioning 2^n−M_Q and 2^n−1−M_R respectively). If the telescoping TERMINATES (e.g., after finitely many alternating reflections when pieces become integers or exhaust), a clean inductive proof is possible. The key: does Q'∪R'' always satisfy A ≥ 1 by a simpler argument (e.g., (B2*)-ref or Sub-3a at a smaller scale)?

**Opening D: Induction reducing bucket (iii) to (B2*)-ref / Sub-3c-ref**
The concrete n=3 example showed: double-REFL gives A(Q∪R) = A(Q'∪R'') = 3/2 ≥ 1 where Q'∪R'' is a (B2*)-ref-type object (Q'={13/4,1}, R''={2,1,1/4} with ΣQ' < 2^{n-1}+1). This IS the (B2*)-ref target from bucket (ii)! So bucket (iii) after double-REFL may REDUCE TO bucket (ii)'s (B2*)-ref. This is a concrete, verifiable reduction worth formalizing.

---

### Dead ends (do not retry)

- The integral bound ∫(N_Q−N_R)dx = 1 does NOT force A ≥ 1 (integral is about sum, not parity; well-known failure certified R5/R6).
- "max(Q) < 2^{n-1} ⟹ A ≥ 2" is FALSE (tight case A=3/2 at n=3 for bucket iii anchor). Permanently deleted.
- Direct REFL-gen without follow-up: reduces to GAP-A crux, which is OPEN (does not close by itself).
- Trying to use the SET IDENTITY S_{G_{n-1}} ∩ [0,2^{n-2}) = S_{G_{n-3}} for refined R: NOT APPLICABLE (identity is G_{n-1}-specific; no refined-R analogue known).
- Containment (INC) argument for n=3 bucket (iii): S_Q ⊄ S_R structurally (parity of |Q|=3 vs |R|=4), so no INC formula applies.

---

### Knowledge-base entries

- **Measure / area argument** (K-base: "A(P) = measure(S_P) = measure(S_Q △ S_R)" — integral rep from alt-sum-integral.md, applies here).
- **Invariants & monovariants** (K-base Combinatorics: the invariant ΣQ=2^n, ΣR=2^n−1, hence ΣP=2^{n+1}−1 is constant in all bucket (iii) configs — constrain the A value).
- **Pigeonhole / extremal principle** (K-base Combinatorics: used for parity argument at x=0).
- **Constructive / incremental** (K-base Combinatorics: the sub-case disjoint/overlap split is constructive).
- No direct analogy in algebra/NT/geometry entries.

---

### Analogous past problems (cruxes)

Not scouted (this lens focused on terrain, not crux corpus). The alternating-sum / dyadic-level structure is quite specific to this problem's reformulation. The general REFL-telescoping pattern (remove max, reduce to level-down target) resembles Hall's marriage theorem (reduce by matching) but I did not verify a direct crux match.

---

### Prior progress and current gap summary

**G-INC-1/GAP-A (anchor R=G_{n-1}): NOW CLOSED for all n** (t-ell-mutual-induction, R8). This resolves the shared 3+-round crux.

**Remaining lower-bound gap in ll-dyadic-symdiff:**
1. Bucket (iii) top-cut refined R: A(Q∪R) ≥ 1 for max(Q), max(R) < 2^{n-1}. n=3 zero violations (42 configs, min A=3/2); n=4 zero violations (188 configs, min A=2). Not proved.
2. Bucket (ii) (B2*)-ref: A(Q'∪R') ≥ 1 for R' refining G_{n-2}, top piece uncut. Not proved for general n (closed only via GAP-A = T(ℓ) for anchor; refined R is separate).
3. Bucket (i) GAP-A refined-R: A(Q'∪R) ≤ max(Q)−1. Not proved for general refined R.

Items 1, 2, 3 all ultimately reduce (via REFL-gen) to: "alternating-tail +1 inequality for refined R." The unresolved core is: **for any refined R with A(R) ≥ 1 and max(R) ≤ 2^{n-1}, the certified T(ℓ) induction with anchor G_{n-1} does NOT transfer without a refined-R analogue of the SET IDENTITY and top-band decomposition.**

**Suggested sub-target for R9 builder:** Prove bucket (iii) for n=3 by direct casework (|Q|=3, |R|=4, one cut on top piece of R), using the structural properties:
- S_Q ⊄ S_R (parity argument: |Q|=3 odd, |R|=4 even)
- A = A(Q)+A(R)−2B with B < A(Q) (non-containment)
- max(Q) < 4, max(R) < 4, ΣP = 15

This would be a fully verifiable partial step (n=3 bucket iii closed) before tackling general n.
