## oblique-circle-linearization

**Verdict:** APPROVE  
**True Status:** solved (the builder's recorded Status is correct)  
**Scores:** Correctness 10/10; Completeness / rigor 10/10; Progress 10/10.

### Adversarial checks

- The proof answers the actual problem: for the given interior configuration it proves that the circumcentre of `AKL` is equidistant from the midpoints `M,N`.
- The imported oriented-ray reconstruction is reviewer-certified. It supplies the strict orders and ranges
  \(0<x<\min(\beta,\gamma)\), \(0<y<\beta-x\), \(0<z<\gamma-x\), so every ray branch used in (2)--(5) is the positive one. In particular \(t,s,\sin x,\sin y,\sin z,\sin(x+y),\sin(x+z)>0\). The closure denominators are sines of interior angles of the nondegenerate triangles `BKC` and `BLC`, so they are also positive.
- I independently re-derived both load-bearing quadratic eliminations. Substitution of
  \(\cot z=(c-2t\cos x)/(2t\sin x)\) into the expanded `BKC` closure gives (8), and the Sine Law plus the cosine-law projection gives exactly `Q_t=0`. The parallel `y,s` calculation gives exactly `Q_s=0`. No division by a possibly zero quantity occurs.
- I independently reconstructed `K,L,d=C-B` in Cartesian coordinates and expanded the determinant target `F`. Every coefficient in table (17), including the signs of the `t`, `s`, `t²s`, and `ts²` terms and the simplification of the `ts` coefficient to `(c²-b²)h`, agrees exactly. No monomials besides the eight listed occur.
- I independently expanded the right side of certificate (18). Its difference from `2pF` simplifies identically to zero. The only non-immediate coefficient comparisons reduce to `hr-q²=p²+2pu`; the displayed product-to-sum evaluation proves that identity correctly.
- The final implication is sound: `Q_t=Q_s=0` makes the certificate yield `2pF=0`, while `x<β` and `α+β<π` imply `0<α+x<π`, hence `p>0` and `F=0`.
- The circle criterion is applied in its valid nonsingular branch. The problem's circumcentre of triangle `AKL` entails that `A,K,L` form a nondegenerate triangle, so `[K,L]≠0`. The criterion correctly translates `F=0` to equality of the midpoint powers, equivalently `OM=ON` for the same circle centre and radius.
- Reflection is harmless because it preserves the hypotheses, circumcentres, midpoints, and distances; choosing `[B,C]>0` loses no case.
- The promoted **Quadratic ray-length certificate** is accepted and certified at `results/imo-2026-02/lemmas/quadratic-ray-length-certificate.md`; its statement is no stronger than the audited derivation.

`results/imo-2026-02/current.md` has been updated to Status `solved` with the complete proof.

### Raw Goal Progress

Problem `imo-2026-02`; Status `solved`; solved: yes; approved approaches: 1/1 built this round; verified milestone: the round-1 determinant gap is closed by two explicitly derived quadratics and a fully audited polynomial certificate; promotable lemmas accepted this round: 1; final theorem verified with all angle branches, denominators, coefficient signs, nonsingularity, and geometric implication checked.
