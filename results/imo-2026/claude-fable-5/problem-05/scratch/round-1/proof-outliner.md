## imo-2026-05

Consensus facts (all three explorers, verified): sufficiency of f(x)=x+c (c≥0) is a one-line perfect-square identity (both squared inequalities reduce to (x−y−c)² ≥ 0); x=f(y) collapses QM=GM giving f(f(y)) = 2f(y) − y; orbits are APs, so d := f − id ≥ 0 and d(f(y)) = d(y). Open crux: d globally constant. Answer to prove: exactly {f(x)=x+c : c≥0} — "f=id only" is a recorded FALSE target.

New round-1 finding (mine, symbolically verified with sympy this round): substituting x = f(y') into the ORIGINAL right inequality and using f(f(y')) = 2f(y')−y' yields the exact identity
  (y+y'+2d(y'))² − 4(y'+d(y'))(y+d(y)) = (y−y')² + 4·f(y')·(d(y')−d(y)) ≥ 0,
i.e. d(y) − d(y') ≤ (y−y')²/(4f(y')) ≤ (y−y')²/(4y') for ALL unrelated pairs. Swapping roles gives |d(a)−d(b)| ≤ (a−b)²/(4·min(a,b)); telescoping over a k-fold subdivision of [a,b] bounds |d(a)−d(b)| ≤ (b−a)²/(4ak) → 0. This closes the global-constancy gap without orbits-at-infinity or any regularity. That is approach 1.

---

two-point-pinch: new
Target: All f: R_{>0}→R_{>0} satisfying the chain are exactly f(x)=x+c, c≥0 (verification + full uniqueness).
Technique: Squeeze-to-equality substitution (x=f(y) ⟹ f∘f = 2f−id), then a second substitution x=f(y') into the original right inequality giving a two-point quadratic pinch on d, closed by subdivision/telescoping.
Skeleton:
  1. f(x)=x+c (c≥0) works — both squared inequalities equal (x−y−c)² ≥ 0.
  2. f(f(y)) = 2f(y) − y — QM/GM equality collapse at x=f(y).
  3. d ≥ 0 — orbit is AP y+n·d(y), positivity of codomain for all n.
  4. |d(a)−d(b)| ≤ (a−b)²/(4·min(a,b)) — x=f(y') substitution identity above (right inequality alone suffices; left gives a cross-check bound).
  5. d constant — telescope step 4 over k equal subdivisions of [a,b]: total ≤ (b−a)²/(4ak) → 0.
Key lemmas (claim + mechanism):
  - f(f(y)) = 2f(y)−y — because x=f(y) makes QM(x,f(y)) = GM(x,f(y)) = f(y), squeezing the middle term to equality on both sides.
  - d(y) − d(y') ≤ (y−y')²/(4f(y')) — because at x=f(y') the right inequality's slack is exactly (y−y')² + 4f(y')(d(y')−d(y)) (verified identity).
  - d(a)=d(b) — because the quadratic per-step error beats the 1/k mesh linearly in the telescoping sum.
Open gaps: rigorous write-up only (hand derivation of the step-4 identity, explicit induction in step 3, positivity justifications for squaring). No structural gap identified.
Cases to cover: none — argument is case-free.
Watch out for: squaring legality (all sides positive — state it); step 3 induction needs the identity applied at each orbit point (each is a positive real); c<0 excluded by domain, not by the inequality.
File: results/imo-2026-05/approaches/two-point-pinch.md

marching-orbits: new
Target: same full characterization {x+c : c≥0}.
Technique: Orbit matching / asymptotic squeeze — place points of two orbits with different d-values at bounded offset arbitrarily far out; the right inequality's slack there is 4·(position)·(p−q)+O(1), forcing all positive d-values equal; fixed-point case killed by exclusion-interval vs. propagating fixed points.
Skeleton:
  1. Sufficiency — perfect square (x−y−c)².
  2. f∘f = 2f−id, d ≥ 0, d constant on orbits — as above.
  3. Marching lemma: d(x)=p>0, d(y)=q>0 ⟹ p=q — choose m=⌈(y_n−x)/p⌉ so x_m−y_n ∈ [0,p); right inequality at (x_m,y_n) has slack 4y_n(p−q)+O(1) → −∞ if p<q; swap for the other direction.
  4. Dichotomy d ∈ {0,c}; mixed case contradiction:
     4a. Right ineq at (a,s), f(a)=a, d(s)=c ⟹ (s−a)² ≥ 4ac: d=c points avoid a length-4√(ac) interval around each fixed point.
     4b. Left ineq at (x,a) ⟹ d(x) < c, hence d(x)=0, for all x ∈ [a, a+c+√(4ac+2c²)): fixed points propagate to +∞ in steps > c.
     4c. The AP b+nc (all d=c) tends to +∞ with gap c, so it must hit the excluded interval around a large fixed point a' (length 4√(a'c) > c once a' > c/16) — pigeonhole contradiction.
  5. Conclude d ≡ c ≥ 0.
Key lemmas: marching lemma (AP placement makes mismatch-slack linear in position while squares stay bounded); fixed-point propagation (solving the quadratic √(2(x²+a²)) < x+a+c); AP-hits-interval (gap c vs. interval length > c).
Open gaps: full rigor in 3 (m(n) choice, limits), 4b induction, 4c explicit constants.
Cases to cover: d≡0; d≡c>0; mixed {0,c}.
Watch out for: forward orbits only (no f⁻¹); 4a needs f(a)=a exactly (legal only after the dichotomy).
File: results/imo-2026-05/approaches/marching-orbits.md

tangent-envelope: new
Target: same full characterization.
Technique: Supporting-curve geometry (aimo-0089 pattern adapted): for each y the chain traps the graph of f between explicit curves L_y(x)=2√(x f(y))−y and U_y(x)=√(2(x²+f(y)²))−y that TOUCH the graph at x₀=f(y) with common slope 1 ⟹ quadratic pinch |d(x)−d(x₀)| ≤ C(x−x₀)²/x₀ anchored at range points; chain anchors to force d constant.
Skeleton: 1. sufficiency; 2. f∘f identity + d≥0; 3. envelope with tangency at every range point; 4. slope-1 + curvature O(1/x₀) ⟹ quadratic pinch at anchors (via exact algebraic second-order inequalities, no calculus); 5. GAP — density/syndeticity of range(f) to let the telescoping run; 6. chain to d constant.
Key lemmas: L_y'(f(y)) = U_y'(f(y)) = 1 — because √(B/x₀)=1 and 2x₀/√(2(x₀²+B²))=1 at x₀=B=f(y) (both computed).
Open gaps: step 5 (anchor density) is a real structural gap; step 4 exact constants.
Cases to cover: none unless step 5 routes through the {0,c} dichotomy.
Watch out for: no continuity assumed — replace derivative language with exact inequalities. This approach is the geometric cousin of two-point-pinch (which achieves an anchor-FREE pinch); it is a reserve in case the algebraic route has a hidden flaw, not a build priority.
File: results/imo-2026-05/approaches/tangent-envelope.md

---

Recorded dead ends respected (do not build on): x=y substitution (tautology); adding right ineq at (x,y)+(y,x) (trivial SOS); y=f(x) after knowing the identity (reduces to (f(x)−x)²≥0); scaling family f=kx (only k=1, subsumed); target "f=id only" (false).

Priority for the reviewer: two-point-pinch is a candidate COMPLETE solution — every step has a verified mechanism and no structural gap; it should headline the build set. marching-orbits is the strongest independent rival (fully different constancy mechanism — orbit asymptotics vs. two-point algebra) and near-complete itself; build it in parallel as insurance. tangent-envelope is a reserve (shares the pinch idea with the leader; genuine open gap) — rank it but building it this round is optional.

Suggested build set: two-point-pinch, marching-orbits.
