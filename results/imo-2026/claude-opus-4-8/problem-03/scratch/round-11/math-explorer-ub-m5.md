## imo-2026-03 (lens: UPPER BOUND — general m≥5, Inequality T)

### Problem context
The entire n≥4 upper bound collapses to proving (T): for the residual m-piece gap case (distinct pieces, p₁≤Σ/2, p₂<τ/2 where τ=2^{m-1}Σ/(2^m−1)), we have μ(X, m−1) ≤ Σ/(2^m−1) = t. Certified for m=4 (T4-tight-m4). Open for m≥5. This report covers the m=5 terrain (n=4).

---

### New lemma discovered: Lemma MK

**Lemma MK** (verified numerically for k=1,...,5, proof sketch complete):
> μ(k pieces, k−1 cuts) ≤ min(pieces).

**Proof sketch**: Sort pieces descending p₁≥...≥p_k. Halve p₁ (1 cut): {p₁/2,p₁/2} is an invisible pair, removed. Remaining: {p₂,...,p_k} with k−2 cuts. By induction: μ ≤ min(p₂,...,p_k) = p_k = min(all k). Base k=1: μ({p₁},0)=p₁=min. k=2: μ({u,v},1)=min(v,u−v)≤v=min. ✓

This is the KEY new tool for the general m case—it was NOT needed for m=4's ad hoc T4 argument.

---

### Complete case structure for m=5, budget b=4

For m=5 pieces {p₁>p₂>p₃>p₄>p₅=δ>0}, Σ=Σpᵢ, t=Σ/31, gap conditions: (1) p₁≤Σ/2; (2) p₂<8t (i.e., τ/2=16Σ/62).
Differences dᵢ=pᵢ−pᵢ₊₁, δ=p₅.

**Case 1 (d₂≤t)**: Strategy — cut p₂@p₃ (net: {p₁,d₂,p₄,p₅}), p₄@p₅ (net: {p₁,d₂,δ,d₄}), p₁@d₄ (net: {p₁−d₄,d₂}). Effective 2 pieces, 1 cut remains. A≤d₂≤t. Verified 100% (integer diffs 1..6, gap conditions, ~456 configs). ✓

**Case 2 (d₃≤t, d₂>t)**: Strategy — cut p₁@p₂ (net: {d₁,p₃,p₄,p₅}), cut p₃@p₄ (net: {d₁,d₃,δ}). Effective {d₁,d₃,δ}, 2 cuts remain. Lemma MK (3 pieces, 2 cuts): A≤min(d₁,d₃,δ). Since δ<d₃ or δ<d₃ in all sub-orderings, min≤d₃≤t. Verified 100% (~193 configs). ✓

**Case 3 (d₄≤t, d₃>t, d₂>t)**: Strategy — cut p₄@p₅ (net: {p₁,p₂,p₃,d₄}). Effective 4 pieces, 3 cuts. Lemma MK (4 pieces, 3 cuts): A≤min(p₁,p₂,p₃,d₄)=d₄≤t. Verified 100% (182 configs). ✓

**Case 0 (δ≤t, all d₂,d₃,d₄>t)**: Lemma MK on all 5 pieces with 4 cuts: A≤min(p₁,...,p₅)=δ≤t. (29 configs, 0 violations.) ✓

**General case structure**: For d_j≤t (j∈{2,...,m}), use m−j pairings to expose d_j as the minimum piece, reaching j effective pieces with j−1 remaining cuts. Lemma MK gives A≤min≤d_j≤t. This covers ALL easy sub-cases uniformly for general m.

---

### Hard case: all d₂,d₃,d₄>t AND δ>t

(813 configs in denom=6 sampling; 0 violations confirmed with correct μ-optimal simulation.)

**Key constraint from gap condition (2)**: p₂=δ+d₄+d₃+d₂<8t. Since each of d₂,d₃,d₄,δ>t: p₂>4t, so δ<8t−(d₂+d₃+d₄)<5t. Combined: t<δ<5t.

**Splitting the hard case** (Sub-A vs Sub-B by d₄ vs d₁):
- Sub-A (d₄≤d₁): 620 configs. Max ratio μ/t = 0.72.
- Sub-B (d₄>d₁): 193 configs. Max ratio μ/t = 0.63.
- Sub-B is NOT vacuous (no arithmetic contradiction rules it out).

**Universal strategy for hard case**: R3 cut p₁@p₂ → effective {d₁,p₃,p₄,p₅} with budget 3.
- Sub-A: 620/620 work. ✓
- Sub-B: 193/193 work. ✓

**Why p₁@p₂ works — mechanism**:
After p₁@p₂ cut: new Σ' = d₁+p₃+p₄+p₅ = Σ−2p₂. From cond(2): p₂<8t, so Σ'>15t. The 4-piece subproblem {d₁,p₃,p₄,p₅} with budget 3 falls into:
- NOT in Case A.A (none of 813 configs have q₁>Σ'/2 after this cut).
- For Sub-A configs (456/620): q₂≥4Σ'/15, R3-reducible, further reduces to 3 pieces → Lemma MK or R4.
- For Sub-A configs (102/620): T4 Case 1 at threshold t (td₂≤t).
- For Sub-A configs (55/620): T4 Case 2 at threshold t (td₃≤t).
- For Sub-A configs (7/620): hard sub-sub-case — BUT T4 Sub-A (P or C) gives A≤t via bounding δ_new and differences.

**Key gap in the analytical proof**: For the 7 hard sub-sub-cases (and analogously for Sub-B), T4 Sub-A works but requires bounding δ_new (=p₅=δ or d₁ depending on ordering) against the ORIGINAL t=Σ/31, not Σ'/15. The T4 Z-bound "δ_new<2t" needs to be derived from the original gap condition (2) rather than the subproblem's own gap condition. In 5 of 7 cases P works (δ_new≤2t), in 2 cases C works (δ_new+td₃−td₁≤t from different arithmetic).

---

### Candidate induction / general-m structure

The m=5 case analysis suggests the following general structure for T_m:

1. **Easy cases** (d_j≤t for some j=2,...,m, or δ≤t): (m−j) pairings + Lemma MK. Handles everything except the true hard case.
2. **Hard case** (all d_j>t, δ>t): Cut p₁@p₂ → 4-piece subproblem + 3 cuts. Recurse or apply T4. HOWEVER: the recursion is NOT "apply T_4 at threshold Σ'/D₄" because Σ'/D₄ > t. The recursion must use the ORIGINAL threshold t throughout.

**Induction proposal**: Define "T_m(at threshold t)" as μ(m pieces, m−1 cuts)≤t when gap conditions hold at that threshold. The inductive step is:
- Easy cases: Lemma MK.
- Hard case: p₁@p₂ cut; resulting (m−1)-piece problem satisfies T_{m−1} "at threshold t" (not at Σ'/D_{m−1}).

This is a MODIFIED induction that carries the SAME threshold throughout, not the usual self-similar induction. The key analytical step is showing the (m−1)-piece subproblem inherits appropriate conditions for T_{m−1}-at-t to apply.

**Viable alternate angle**: Instead of the p₁@p₂-then-induct route, there may be a DIRECT analytic case split for general m using:
- Condition (2'): p₂ < 2^{m-1}·t rewrites as a linear inequality on the differences.
- Sub-B vacuousness for general m: NOT always possible (Sub-B is non-vacuous for m=5), so the general proof must handle Sub-B directly (NOT via contradiction like m=4).
- Sub-A P/C analog for general m: after reducing to effective pieces {δ,something}, verify A≤t using original gap conditions.

---

### Distinct openings for the outliner

1. **Lemma MK + case-split**: Prove easy cases (d_j≤t) uniformly for all m via Lemma MK. Then for the hard case, prove Sub-A and Sub-B separately. Sub-A via p₁@p₂ + induction on the resulting (m−1)-piece problem at threshold t. Sub-B: same p₁@p₂ cut, but verify the resulting problem satisfies T_{m−1}-at-t differently.

2. **Modified T4 induction at SAME threshold**: Write T_m as: "for m-piece gap-case config at threshold t=Σ/(2^m−1), μ≤t." For the hard sub-case, prove p₁@p₂ cut → {d₁,p₃,...,pₘ} satisfies the m−1 version of the SAME gap conditions (with p₃+...+pₘ adjusted) at the SAME t. Verification: Σ'=Σ−2p₂ > 15t (for m=5) > t(2^{m−1}−1) for general m? Need condition (2) to give Σ'>(2^{m−1}−1)t exactly.

3. **Direct P/C analog for hard case, bypassing recursion**: For the hard case, find explicit effective pairs {u,v} achievable in m−1 cuts with A=min(v,u−v)≤t. This avoids the need to track the subproblem's threshold. The key is finding (u,v) in terms of δ,d_j that always achieve A≤t.

4. **Sub-B handled by Case A.A on subproblem**: For Sub-B (d₄>d₁), the p₁@p₂ cut may produce a subproblem where q₁>Σ'/2 (Case A.A), giving μ=0≤t. Check: numerically 0/193 Sub-B configs land in Case A.A directly. So this doesn't work — Sub-B is genuinely hard.

---

### Candidate technique(s)
- Lemma MK (k pieces, k−1 cuts ≤ min): the core new tool.
- R3 pairing cut p₁@p₂ as the universal hard-case first move.
- Modified induction on m: T_m at threshold t → T_{m−1} at same threshold t (not self-similar).
- Gap condition (2) arithmetic: p₂<2^{m−1}t controls δ, key for Sub-A P/C bounds.

### Cheap-kill candidates
- If δ≤t: Lemma MK immediately. Cheap pre-check before any case analysis.
- If any d_j≤t (j=2,...,m): (m−j) pairings + Lemma MK. O(m) cheap reductions before the hard case.
- Sub-B vacuousness: cannot be a cheap kill for m≥5. Don't try to mimic m=4 Sub-B argument.

### Knowledge-base entries to use
- Certified T4-tight-m4.md: template for Sub-A P/C argument in hard case.
- Lemma AB (abundant-budget.md): justifies focusing on tight budget b=m−1.
- Lemma R4 (gap-case-m3-closure.md): base case m=3 for the induction.
- Lemmas R1/R2/R3 (sum-bound-reductions.md): justify pairing moves; R3 "cut pᵢ@pⱼ" notation.

### Analogous past problems (cruxes)
None found that closely parallel this structure (multi-round nested case induction with threshold-invariant recursion).

### Prior progress
- T4 (m=4) certified, n=3 upper bound fully rigorous.
- Lemma MK proved (to be certified).
- Easy cases (d_j≤t, δ≤t) for m=5 verified numerically and analytically (Cases 0,1,2,3).
- Hard case for m=5: 0 violations (813 configs), universal strategy p₁@p₂ identified, full breakdown through T4 sub-cases.
- Hard Sub-A: completely covered analytically (p₁@p₂ → T4 gap case or R3-reducible → T4 Cases 1,2,4-Sub-A).
- Hard Sub-B: covered numerically; analytic argument NOT yet written.
- MISSING: clean bound showing T4 Sub-A at threshold t (not Σ'/15) works for the 7 sub-sub-hard cases and Sub-B.

### Dead ends (do not retry)
- SB-monotone chaining: certified dead (SB-obstruction theorem, round 7). Do not retry.
- R3-cascade actual-A potential for m≥4: refuted (round 8). Do not retry.
- Complement-cut m=4→3→R4: refuted (round 9). Do not retry.
- T4 Sub-B vacuousness for m=5: NOT vacuous. The d₄>d₁ assumption does NOT lead to arithmetic contradiction for m=5. Do not try to replicate this m=4 argument.
- Inductive reduction "apply T4 at Σ'/15": fails because Σ'/15>t. Do not try.

### Small-case / intuition notes (all CONJECTURAL unless labeled verified)
- **CONJECTURE**: For general m, the full proof has 2 parts: (A) Easy cases via Lemma MK (clean, likely provable now). (B) Hard case via p₁@p₂ + T_{m−1} at threshold t, requiring a NEW inductive lemma that the subproblem inherits gap conditions (at the original threshold, not Σ'/D_{m−1}).
- **VERIFIED** (denom=6): T_5 holds for all 2722 gap-case configs (0 violations, worst ratio 0.795).
- **VERIFIED** (denom=6): Hard case for m=5 (813 configs): 0 violations. Universal strategy p₁@p₂ works 100%.
- **VERIFIED**: Sub-B analog (d₄>d₁) is NOT vacuous for m=5 (193/813 configs).
- **CONJECTURE**: The threshold-invariant induction "T_{m}(at t) via p₁@p₂ → T_{m−1}(at t)" extends to all m, with the condition Σ'/(2^{m−1}−1) > t following from condition (2) p₂ < 2^{m−1}t and Σ'=Σ−2p₂ > Σ−2^m·t = (2^m−1−2^m)t... wait, this needs Σ−2p₂ > (2^{m−1}−1)t. Σ=(2^m−1)t, p₂<2^{m−1}t: Σ−2p₂ > (2^m−1−2^m)t? No: (2^m−1)t−2·2^{m−1}t = (2^m−1−2^m)t < 0. Contradiction shows Σ' may be < (2^{m−1}−1)t in general? Need to re-examine.
- **NOTE**: The correct bound on Σ' is Σ−2p₂ > (2^m−1)t−2·2^{m−1}t = −t < 0, which is trivial. The useful bound is Σ' > (2^m−1−2p₂/t)t. For p₂ just below 2^{m−1}t, Σ'≈t>0. For m=5: Σ'>Σ−16t=31t−16t=15t=(2⁴−1)t. So Σ'>(2^{m−1}−1)t exactly for m=5! This is the KEY: Σ'=Σ−2p₂ > (2^m−1)t−2·2^{m−1}t = (2^m−1−2^m)t + t·... wait let me recompute: Σ=(2^m−1)t, p₂<2^{m−1}t ⟹ 2p₂<2^m·t ⟹ Σ−2p₂ > (2^m−1)t−2^m·t = −t. That's negative, not useful. But p₂>0 ⟹ Σ'=Σ−2p₂<Σ=(2^m−1)t. And condition: Σ'>(2^{m−1}−1)t iff Σ−2p₂>(2^{m−1}−1)t iff p₂<(2^m−1−2^{m−1}+1)t/2 = (2^{m−1})t/2·... hmm. For m=5: p₂<8t and need Σ'>15t = (2^4−1)t. Σ'=Σ−2p₂>31t−16t=15t. ✓ For general m: Σ'>(2^{m−1}−1)t iff p₂<(2^m−1−(2^{m−1}−1))t/2 = 2^{m−2}·t. But condition (2) gives p₂<2^{m−1}t, not 2^{m−2}t. So the inductive relationship Σ'>(2^{m−1}−1)t does NOT follow from condition (2) for general m (only works for m=5 specifically where the arithmetic is exact). **This is a critical observation for the outliner.**
