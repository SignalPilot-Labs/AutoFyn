## `trig-sine-factorization`

**Verdict:** CHANGES REQUESTED  
**True Status:** partial (the builder's recorded Status is correct)

**Scores**
- Correctness: 8/10
- Completeness / rigor: 6/10
- Progress: 8/10

**Adversarial check.** The candidate addresses the actual claim `OM=ON`. I independently re-derived the load-bearing reduction as follows. For the circle
\[
q_1^2+q_2^2-w_1q_1-w_2q_2=0,
\]
substitution of \(K=(X,Y)\) and \(L=(U,V)\) gives the displayed Cramer formulas for \(w_1,w_2\). Substitution of \(pB=(pc,0)\) and \(qC=qb(\cos\alpha,\sin\alpha)\) gives exactly
\[
p=w_1/c,\qquad q=(w_1\cos\alpha+w_2\sin\alpha)/b.
\]
The directed secant products at the midpoints are
\[
\operatorname{Pow}(M)=(-c/2)c(p-1/2)=c^2(1-2p)/4
\]
and analogously \(\operatorname{Pow}(N)=b^2(1-2q)/4\). Hence identity (8) is indeed exactly the numerator form of equality of the two powers. I also independently checked three non-symmetric numerical configurations satisfying the two closure equations; identity (8) vanished to approximately \(10^{-14}\)–\(10^{-13}\), supporting—but not proving—the asserted algebraic identity.

The ray reconstruction and closure equations are correct. In particular the strict orders at \(B\) and \(C\) give the stated angle ranges, and the Sine Law angle triples for \(BCK\) and \(BCL\) sum to \(\pi\) and have the displayed sides opposite the relevant angles. No reflected or zero-denominator case was found.

**Precise remaining gap.** The theorem's decisive implication is still absent: the candidate does not derive (8) from residual equations (9) and (10). Saying that an exponential-polynomial computation places (8) in their ideal is neither a displayed certificate nor a human-checkable proof. Until an explicit factorization, or another rigorous derivation of (8), is supplied, the equal-power conclusion does not follow. This is a real load-bearing gap, so the approach cannot be approved as solved.

**Promotable lemmas.** Certified and admitted:
- `directed-midpoint-power-formula.md`: statement and directed signs are correct, including extension cases.
- `circle-second-intersection-through-origin.md`: Cramer's-rule and line-intersection formulas are correct under the explicitly stated noncollinearity condition.

**Outcome recorded:** `advanced` — the approach gives a verified end-to-end reduction, but the final factorization remains open.

---

## `oblique-circle-linearization`

**Verdict:** CHANGES REQUESTED  
**True Status:** partial (the builder's recorded Status is correct)

**Scores**
- Correctness: 8/10
- Completeness / rigor: 6/10
- Progress: 8/10

**Adversarial check.** The candidate addresses the actual claim. I independently reconstructed its load-bearing circle reduction. If \(X=rB+sC\), the quadratic part of a circle through \(A=0\) is indeed \(|X|^2=c^2r^2+b^2s^2+2bc\cos\alpha\,rs\), while its linear part is uniquely \(\lambda r+\mu s\). At \(M=(1/2,0)\) and \(N=(0,1/2)\), equality of powers is exactly
\[
\lambda-\mu=(c^2-b^2)/2.
\]
For \(K=r_KB+s_KC\), \(L=r_LB+s_LC\), Cramer's rule gives
\[
\lambda-\mu=
\frac{|K|^2(s_L+r_L)-|L|^2(s_K+r_K)}{r_Ks_L-r_Ls_K}.
\]
Using
\([K,L]=[B,C](r_Ks_L-r_Ls_K)\) and
\([K,C-B]=[B,C](r_K+s_K)\), this becomes exactly the displayed determinant quotient and hence criterion (3). Thus the circle linearization is valid.

I also checked the positive-ray intersections independently. Taking determinants in
\(B-te(-x)=B/2+ue(z)\) and
\(C-te(\alpha+x)=C/2-ue(\alpha+x+y)\) reproduces formula (1), with positive denominators under the strict angle ranges. The two closure equations agree with the Sine Law computations in the trig approach.

**Precise remaining gap.** Criterion (3), which is equivalent to the desired conclusion, is never proved from formulas (1) and closure equations (2). The text explicitly leaves the required bilinear/trigonometric cancellation open. All work after the circle reduction therefore establishes only what would suffice, not that it holds. This is load-bearing and prevents solved status. The approach file also contains an empty `## Full proof` section despite the file contract saying that section is present only for solved approaches; this is editorial rather than mathematical, but should be removed while status is partial. There are also two corrupted control-character renderings in the matrix/Cramer formulas in the copied candidate; these should be repaired.

**Promotable lemmas.** Certified and admitted:
- `oriented-ray-reconstruction.md`: the branch restrictions, intersection formulas, and closure equations are fully justified.
- `oblique-circle-coefficient-criterion.md`: the equivalence between `OM=ON`, the linear coefficient identity, and determinant identity (3) is correct.

**Outcome recorded:** `advanced` — branch and circle-system gaps were closed, but the decisive determinant cancellation remains open.

---

## Raw Goal Progress

- Problem: `imo-2026-02`
- Round-1 problem Status: `partial`
- Solved this round: no
- Approved approaches: 0/2
- Partial approaches with verified progress: 2/2
- Verified milestone: both approaches rigorously reduce `OM=ON` to the same explicit determinant/trigonometric identity after controlling all ray branches, sine denominators, circle nonsingularity, second intersections, and directed midpoint powers.
- Remaining blocker: prove
\[
2\bigl(|K|^2[L,C-B]-|L|^2[K,C-B]\bigr)=(c^2-b^2)[K,L]
\]
from the two separated closure equations, by a displayed human-checkable calculation or a different rigorous argument.
- Certified reusable lemmas: 4
- `current.md`: created/updated with Status `partial`; no full proof was inserted.
