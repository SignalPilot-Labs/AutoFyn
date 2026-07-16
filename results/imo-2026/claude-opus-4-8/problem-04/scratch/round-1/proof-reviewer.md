# Proof review — imo-2026-04 (Mulan's triangle game), round 1

Both approaches claim the same answer — **Mulan wins iff θ = 180°/N for integer N ≥ 2 (iff 180/θ ∈ ℤ)** —
and are mathematically identical in content. I re-derived every load-bearing step from scratch and
cross-checked the two critical moves (closure lemma; both-multiples cut) by independent computation.
Both proofs pass.

## Independent verification performed

1. **Cut arithmetic** (both §0). Re-derived Child1=(A₁,B,A+C−A₁), Child2=(A−A₁,C,A₁+B) directly from
   the cevian decomposition. Confirmed: B, C inherited full (cut touches only V_A and P); P-angles
   180−A₁−B = A+C−A₁ and 180−(A−A₁)−C = A₁+B are supplementary; all entries > 0 for A₁∈(0,A); P not a
   vertex. Correct.
2. **Closure Lemma** — the single load-bearing step for impossibility. Re-derived all four cases
   independently: (i) A=(n+m)θ, (ii) B=(m−n)θ with m>n forced by B>0, (iii) C=(n−m)θ with n>m forced
   by C>0, (iv) 180=(n+m)θ. Each contradicts either T∈S or 180/θ∉ℤ. The case split is genuinely
   exhaustive: B, C are inherited-safe so each child's only candidate multiple-angles are its two new
   angles → 2×2 = 4 combinations, all covered. **Brute-force search** over T₀=(36,36,108) with θ=72
   (and permutations) found NO cut making both children non-safe — matches the lemma.
3. **Safe start** T₀=(θ/2,θ/2,180−θ). Verified genuine and safe for 180/θ∉ℤ, including θ>90 (e.g.
   θ=100 → (50,50,80), 80 not a multiple of 100). Covers irrational and rational-non-1/N (72°).
4. **Phase-1 both-multiples cut (G1)**. Verified A>θ for all N≥3 (largest angle ≥60°≥θ, equality only
   in the all-60° = all-θ excluded case). Verified n=⌊C/θ⌋+1 gives C<nθ<A+C strictly (nθ>C by def;
   nθ ≤ C+θ < C+A since θ<A), hence A₁=A+C−nθ ∈(0,A) strictly (P not a vertex). Children carry nθ and
   (N−n)θ, both in {1,…,N−1}·θ, both positive. **Random test over 2000 triangles each for N=3..10**:
   every cut valid, both children carry a multiple, all angles positive.
5. **Descent (G2) and N=2 (G3)**. Descent A₁=θ∈(0,jθ) legal for j≥2; survivor carries (j−1)θ
   regardless of Shan-Yu's choice; j=2 gives both children θ; strictly decreasing bounded monovariant
   ⟹ terminates in ≤N−1 cuts. N=2: cut A₁=A+C−90 on largest vertex gives both children 90°; verified
   A₁∈(0,A) via C<90, B<90.
6. **Full-game simulation.** Winning side (N=2..12): against an adversarial Shan-Yu that avoids θ
   whenever possible, Mulan's stated strategy always reaches an angle θ (no loops). Losing side
   (θ=72, 100, 40 = 180/4.5): Shan-Yu can keep a safe child for 3000 random Mulan cuts each time.
7. **Answer verification.** Stated explicitly; θ=72 correctly excluded (refutes the rival "rational
   ≤90°" hypothesis); N=2..6 spot-checked winning. Correct.

No skipped cases, no hand-waving; monovariant and induction cited to knowledge_base.md; cut mechanics
derived from scratch.

## Verdicts

### safe-set-invariant — Status: **solved** — Verdict: **APPROVE**
- Correctness: 10/10. Completeness/rigor: 10/10. Progress: full solution.
- Builder's recorded Status `solved` is correct. Both directions complete; all four gaps
  (G1 chain entry, G2 descent, G3 N=2, G4 cut symmetry) genuinely closed. No gap found.

### force-2theta-bisect — Status: **solved** — Verdict: **APPROVE**
- Correctness: 10/10. Completeness/rigor: 10/10. Progress: full solution.
- Builder's recorded Status `solved` is correct. Identical mathematical content, cleanly packaged
  (Cut Lemma → Chain-entry I.2 → Descent I.1 → Closure II.1). The exhaustiveness remark in II.1 is
  accurate. No gap found.

## Lemma certification
- `lemmas/closure-lemma.md` — **CERTIFIED**. Statement correct, proof sorry-free, no stronger than
  proved, 4-case split verified exhaustive and confirmed by brute-force search. Marked CERTIFIED.

## Bookkeeping
- Recorded `verified-milestone` for both slugs via record_outcome.
- Wrote `results/imo-2026-04/current.md` with Status `solved` and the Full proof.

Both approaches independently constitute a complete, rigorous solution. The problem is SOLVED.
