## Status
partial

## Approaches tried

### Round 4 (this round)

**(a) Acute-angle-bound sub-route for branch selection — RETIRED, refuted.**
For two rounds (rounds 3–4) this file pursued the conjecture that the four
hypothesis angles `∠LBK,∠LNC,∠LCK,∠BMK` are always acute at genuine
solutions, as a lever to select the branch `G2a=G3a=0` over the extraneous
`G2b=G3b=0`. Round 4's acute-angle-lens math-explorer solved the **true,
unsquared** hypothesis system (via `scipy.fsolve` on the actual `arccos`
angle equalities, not the squared polynomial relaxation) and found
**explicit, non-degenerate counterexamples** with the hypothesis angle
obtuse and healthy containment margins — not boundary artifacts:
- `a=0.9959, b=2.0302, cc=1.1413, t1=0.1522, t2=1.2001, β≈9.72°`:
  `∠LCK=∠BMK≈95.18°` (obtuse), containment margins ≈9% and ≈18% of
  triangle area.
- `a=2.5788, b=0.8327, cc=0.3488, t1=1.421, t2=0.0963, β≈7.35°`:
  `∠LCK=∠BMK≈123.5°` (obtuse), again a genuine, non-tiny margin.

Both were **independently reproduced by the outline-reviewer** in a fresh
session (own script, own signed-area containment test), confirming the
counterexamples are genuine (hypothesis residuals `<1e-9`, both
containments strictly satisfied, `t1,t2>0`, `0<β<∠ABC`) and not an
artifact of the explorer's numerics. **The acute-angle conjecture, as
literally stated ("the four hypothesis angles are always acute at genuine
solutions"), is false.** Round 3's numeric survey (150 samples, max
≈49.4°) under-sampled the region of parameter space (thin triangles, `β`
near the edge of its valid range) where obtuse genuine solutions occur.

**This sub-route is retired — do not pursue it further in any form**,
including the "same-sign reduction" corollary the explorer derived
(`sign(BL·BK)=sign(NL·NC)` and `sign(CL·CK)=sign(MB·MK)`, both
unconditionally true facts that reduce the 4-angle question to 2 clean
closed-form inequalities `t_1\cos\beta<AB/2`, `t_2\cos\beta<AC/2`) — this
reduction is correct and possibly reusable elsewhere, but the explorer
showed both signs genuinely occur, so it does **not** rescue branch
selection and is not worth developing further for this purpose. The
`2a\cos^2\beta=b` resultant-factor lead identified in round 3 is likewise
not this file's concern going forward — it has been handed to
`coordinate-bash-resultant-boundary`'s IVT mechanism (as its unclassified
`F2`/`F3` factor), which is the live route for branch selection now. This
negative result is recorded honestly, not deleted, per CLAUDE.md's
"record everything" rule: two rounds of real effort on this lever
established (i) a proved insufficiency of the crude containment bound
alone (round 3, still valid and useful) and (ii) this round's conclusive
refutation of the full conjecture by explicit counterexample. Both are
genuine, useful negative information for the population.

**(b) Isosceles case `AB=AC` — new standalone certified lemma proposed,**
`lemmas/isosceles-case-symmetry.md` (see below and the lemma file itself).
This closes the round-1-flagged "isosceles edge case unaddressed" gap,
independently of Q, Ptolemy, and branch selection — reusable by every
approach in the population. Unlike the round-4 ptolemy-lens explorer's
report (which flagged, but did not itself prove, the needed
existence/uniqueness of the root of the shared (III)/(IV) constraint
equation), **this round closes that existence/uniqueness gap rigorously**
via an explicit monotonicity + intermediate-value argument (§below), and
also closes the non-collinearity requirement for one of its two possible
failure modes (rigorously, via an elementary height argument), honestly
isolating the one piece that remains a standing assumption rather than a
proved fact (see "What remains open" in the lemma file).

### Round 3 (preserved)
- **Symbolic (all-triangle) genericity certificate — CLOSED, independently
  rebuilt from scratch (not just re-typed from the explorer's report).**
  Reran the entire round-2 recipe (Weierstrass tangent-half-angle
  substitution + rotation parametrization + homogeneity decoupling +
  Gröbner-basis ideal membership) with `A=(0,0), B=(a,0), C=(b,cc)` fully
  symbolic (three free real parameters, no concrete numbers anywhere), in a
  fresh `sympy` session, without importing any intermediate value from the
  genericity explorer or the outline-reviewer. Obtained, byte-for-byte
  matching degree/size structure to both independent reports: `eq2` degree
  24, `eq3` degree 22; homogeneity decoupling `eq2=t1²g2`, `eq3=s2²g3` with
  exact (remainder-0) division; factorizations `g2=-(b²+cc²)²(u²+1)G2a·G2b`,
  `g3=-a²(u²+1)G3a·G3b` with `G2a,G3a` the degree-4-in-`u` (quadratic in
  `s2` resp. `t1`) cofactors; target `T` of total degree 12 (degree 2 in
  `t1`, 2 in `s2`, 6 in `u`); Gröbner basis of `⟨G2a,G3a⟩` in
  `ℚ[t1,s2,u,a,b,cc]` (grevlex) with 18 generators, built in ~3s;
  `reduce(T)` gives remainder **0**. This is now the **third** independent
  derivation of this exact result (explorer, outline-reviewer, and this
  builder), all agreeing — see §§2–7 below for the full, self-contained
  writeup with the explicit polynomials. **This closes gap 1 (genericity)
  completely and rigorously** — the identity `O·(C−B)=(|C|²−|B|²)/4` holds
  on the branch `G2a=G3a=0` for *every* real triangle `A,B,C`, not a sample.
  Also ran two extra sanity checks beyond both prior reports: (i) confirmed
  `T` is **not** in `⟨G2a⟩` alone or `⟨G3a⟩` alone (ruling out the
  single-generator pitfall `coordinate-bash` flagged in round 2), and (ii)
  extracted an explicit cofactor witness `T = Σqᵢpᵢ` over the computed
  18-element Gröbner basis (6 of the 18 cofactors nonzero) — a genuinely
  checkable certificate, not merely "sympy said remainder 0."
- **Branch selection (gap 2) — pushed but NOT closed; honestly reporting
  the gap remains open.** Understood and wrote out precisely (§8 below) why
  this is a genuinely different algebraic question from
  `fixed-point-concyclic`'s already-closed cross-product sign gap (this is
  a dot-product / acute-vs-obtuse question, per the sign-lemma explorer's
  Part B). Attempted the length/position-bound synthetic argument suggested
  by the outline (§9 below): showed that the crude containment facts alone
  (K inside angle MBC = angle ABC, L inside angle NBC ⊂ angle ABC) do
  **not** by themselves bound the hypothesis angles below 90° — the bound
  visible in the numerics (max ≈49.4° over 150 sample points) must come
  from the *interlocking* system (hyp 1 + hyp 2 + hyp 3 simultaneously, not
  containment alone), which resists the crude triangle-angle-sum argument
  proposed in the outline. Computed a new symbolic fact not in either
  explorer report: the resultant `Res_{s2}(G2a,G2b)` factors symbolically
  (all `a,b,cc,u`) into three simple pieces, one of which is proportional to
  `(a−b)sinβ − cc·cosβ` (the cross product of direction `(cosβ,sinβ)` with
  `B−C`) and another to `2a cos²β − b` — a concrete new lead for a future
  round, but **not developed into a proof** (§9). Status honestly remains
  `partial`; gap 2 is precisely isolated but not closed.

### Round 2 (preserved)
- **Weierstrass rationalization + Gröbner-basis elimination.** Produced a
  complete, gap-free certificate on one concrete rational triangle
  `A=(0,0),B=(2,0),C=(3/5,4/5)` — independently re-verified by the round-2
  proof-reviewer, certified as `lemmas/homogeneity-decoupling-rotation-param.md`.
  Full detail preserved in git history of this file; superseded computationally
  (not retracted) by round 3's symbolic version above, which specializes to
  it at `(a,b,cc)=(2,3/5,4/5)`.

## Current best

### 1–2. Reduction and rotation parametrization (imported verbatim, unchanged)
With `A` at the origin, `OM=ON ⟺ O·(C−B)=(|C|²−|B|²)/4` (certified
`lemmas/vector-reduction-OM-ON.md`), and `O` (circumcenter of `A,K,L`) has
the Cramer's-rule closed form
$$O_x=\frac{|K|^2L_y-|L|^2K_y}{2\det},\qquad O_y=\frac{K_x|L|^2-L_x|K|^2}{2\det},\qquad \det=K_xL_y-K_yL_x.$$
The rotation parametrization (from `coordinate-bash` §4, imported verbatim):
$$K = B + t_1(-\cos\beta,\sin\beta), \qquad L = C + t_2\cdot R(\beta)\frac{A-C}{|AC|},$$
`t_1=BK>0`, `t_2=CL>0`, `\beta=\angle KBA=\angle ACL` (hypothesis 1's free
parameter), `R(\beta)` the counterclockwise rotation by `\beta`.

### 2. Fully symbolic triangle (this round's central new computation)
Take `A=(0,0)`, `B=(a,0)`, `C=(b,cc)` with `a,b,cc` free real numbers
(`a\ne0` for `B\ne A$; `(b,cc)\ne(0,0)` for `C\ne A$; and `a,b,cc` chosen so
that `A,B,C` is a genuine non-degenerate scalene triangle, i.e.
`a(b^2+cc^2-ab)\ne 0`, the non-vanishing of `\det(B,C)$-type quantities used
below). To avoid a literal square root for `|AC|` entering the polynomial
ring, write
$$L = C + s_2\cdot R(\beta)(A-C), \qquad s_2 := t_2/|AC|,$$
so `s_2>0\iff t_2>0` (an order-preserving rescaling — no information lost)
and `L` is now polynomial in `(s_2,\beta,a,b,cc)` with **no square root of
`a,b,cc`** anywhere. This is the only change relative to the round-2
concrete-triangle setup; every other definition is identical.

Substituting the Weierstrass rationalization `\sin\beta=2u/(1+u^2)`,
`\cos\beta=(1-u^2)/(1+u^2)`, `u=\tan(\beta/2)` (a bijection
`u\in\mathbb R\leftrightarrow\beta\in(-\pi,\pi)`; the excluded pole
`\beta=\pi` lies outside the geometrically relevant range
`0<\beta<\angle ABC\le\pi`, so no information is lost) gives explicit
rational expressions for `K,L` in `\mathbb Q(a,b,cc)(t_1,s_2,u)`:
$$K=\Big(a-\frac{t_1(1-u^2)}{1+u^2},\ \frac{2t_1u}{1+u^2}\Big),\qquad
L = C + s_2\begin{pmatrix}\cos\beta&-\sin\beta\\\sin\beta&\cos\beta\end{pmatrix}(A-C).$$

### 3. The two constraint polynomials and their homogeneity decoupling
As in round 2, each unsigned-angle hypothesis `\angle(V_1,V_2)=\angle(V_3,V_4)`
(both angles in `(0,\pi)`, so equality of the angles is equivalent to
equality of their cosines, since `\cos` is injective on `(0,\pi)`) is
recorded, after clearing the positive norms `|V_i|` and squaring to remove
the remaining square roots, as the **necessary** polynomial condition
$$(\dagger)\qquad (V_1\cdot V_2)^2|V_3|^2|V_4|^2 = (V_3\cdot V_4)^2|V_1|^2|V_2|^2.$$
(Squaring a true equality of reals is always valid — no sign hypothesis
needed for this direction; the converse direction, i.e. whether a root of
`(\dagger)` is a genuine solution of the original unsquared hypothesis or
of the spurious "supplementary angle" alternative, is exactly gap 2, §8
below.) Applying `(\dagger)` to hypothesis 2 (`\angle LBK=\angle LNC`,
vectors `BL,BK` at `B` and `NL,NC` at `N`) and hypothesis 3
(`\angle LCK=\angle BMK`, vectors `CL,CK` at `C` and `MB,MK` at `M`) gives
two polynomials `eq_2,eq_3\in\mathbb Q[t_1,s_2,u,a,b,cc]` (after clearing the
common denominator `(1+u^2)^k`, verified by direct `sympy` computation to be
degree-free of `t_1,s_2$), of total degree `24` and `22` respectively.

**Homogeneity-decoupling lemma (imported and reconfirmed symbolically —
already certified `lemmas/homogeneity-decoupling-rotation-param.md` as a
coordinate-free geometric fact; here reverified by exact polynomial
division in the fully symbolic ring).** `BK=K-B=t_1(-\cos\beta,\sin\beta)`
is exactly homogeneous (zero intercept) in `t_1`, and
`CL=L-C=s_2\cdot R(\beta)(A-C)` is exactly homogeneous in `s_2`. Hence every
term of `(\dagger)` applied to hypothesis 2 carries an overall factor
`t_1^2` (geometrically: `\angle LBK` depends only on the *direction* of ray
`BK`, i.e. on `u`, not on how far `K$ sits along it), and symmetrically for
hypothesis 3 and `s_2$:
$$eq_2 = t_1^2\cdot g_2(s_2,u,a,b,cc), \qquad eq_3 = s_2^2\cdot g_3(t_1,u,a,b,cc).$$
Verified by exact polynomial division (`sp.div(eq2, t1**2, t1)`, remainder
`0`; symmetrically for `eq3`) — reproduced independently by this builder in
a fresh session (script in §7).

### 4. Branch factorization
`sympy.factor` splits each cofactor into two branches (arising from the
`(\dagger)` squaring):
$$g_2 = -(b^2+cc^2)^2(u^2+1)\,G_{2a}(s_2,u,a,b,cc)\,G_{2b}(s_2,u,a,b,cc),$$
$$g_3 = -a^2(u^2+1)\,G_{3a}(t_1,u,a,b,cc)\,G_{3b}(t_1,u,a,b,cc),$$
with `G_{2a},G_{3a}$ quadratic in `s_2$ resp. `t_1$, degree `4` in `u`, and
`G_{2b},G_{3b}$ quadratic in `s_2$ resp. `t_1$, degree `6` in `u$ (this
degree-4-vs-degree-6-in-`u` distinction is exactly how the branches are told
apart, matching round 2's concrete-triangle structure and both this round's
independent reports). Explicitly (reproduced independently, matches both
prior reports term-for-term):
$$G_{2a}= 2au^3+2au-4bs_2^2u^3-4bs_2^2u-4bs_2u^3+4bs_2u-2bu^3-2bu$$
$$\qquad{}+2cc\,s_2^2u^4-2cc\,s_2^2+3cc\,s_2u^4-2cc\,s_2u^2+3cc\,s_2+cc\,u^4-cc,$$
$$G_{3a}=-2a^2bu^3-2a^2bu+a^2cc\,u^4-a^2cc+2ab^2u^3+2ab^2u-4abt_1u^3+4abt_1u$$
$$\qquad{}+2a\,cc^2u^3+2a\,cc^2u+3a\,cc\,t_1u^4-2a\,cc\,t_1u^2+3a\,cc\,t_1-4bt_1^2u^3-4bt_1^2u+2cc\,t_1^2u^4-2cc\,t_1^2.$$
(`G_{2b},G_{3b}$, the extraneous-branch cofactors, are also fully explicit
but longer — not needed for the certificate below and omitted here; they
were computed and match both prior reports.) Substituting `(a,b,cc)=(2,3/5,4/5)$
into `G_{2a},G_{3a}$ exactly reproduces round 2's concrete-triangle
polynomials (checked directly), confirming this is a genuine generalization,
not a different computation.

### 5. Target identity and its total degree
The target `T(t_1,s_2,u,a,b,cc)$ is the numerator, after clearing the
denominator `4\det(A,K,L)` (nonvanishing for a genuine, non-degenerate
triangle `AKL`), of
$$O\cdot(C-B) - \frac{|C|^2-|B|^2}{4},$$
computed directly from the closed-form `O$ of §1 substituted with the `K,L$
of §2. `T$ has total degree `12` (degree `2$ in `t_1$, `2$ in `s_2$, `6$ in
`u$) — reconfirmed independently in this session.

### 6. The genericity certificate: `T ∈ ⟨G2a,G3a⟩` for symbolic `a,b,cc` (this round's headline result, independently reproduced three times)
**Computation** (fully reproducible; the exact script used in this
session):
```python
import sympy as sp
t1,s2,u,a,b,cc = sp.symbols('t1 s2 u a b cc', real=True)
sinb = 2*u/(1+u**2); cosb = (1-u**2)/(1+u**2)
A = sp.Matrix([0,0]); B = sp.Matrix([a,0]); C = sp.Matrix([b,cc])
M = (A+B)/2; N = (A+C)/2
Rbeta = sp.Matrix([[cosb,-sinb],[sinb,cosb]])
K = B + t1*sp.Matrix([-cosb, sinb])
L = C + s2*Rbeta*(A-C)
def cross_eq(V1,V2,V3,V4):
    lhs = (V1.dot(V2))**2*V3.dot(V3)*V4.dot(V4)
    rhs = (V3.dot(V4))**2*V1.dot(V1)*V2.dot(V2)
    return sp.expand(sp.numer(sp.together(lhs-rhs)))
eq2 = cross_eq(L-B,K-B,L-N,C-N)      # hyp 2: angle LBK = angle LNC
eq3 = cross_eq(L-C,K-C,B-M,K-M)      # hyp 3: angle LCK = angle BMK
q2,r2 = sp.div(eq2, t1**2, t1);  assert r2 == 0
q3,r3 = sp.div(eq3, s2**2, s2);  assert r3 == 0
g2, g3 = sp.factor(q2), sp.factor(q3)
# extract G2a (deg-4-in-u factor of g2 that involves s2), G3a (analogous)
Kx,Ky = K; Lx,Ly = L
K2, L2, det = Kx**2+Ky**2, Lx**2+Ly**2, Kx*Ly-Ky*Lx
expr = (K2*Ly-L2*Ky)/(2*det)*(C[0]-B[0]) + (Kx*L2-Lx*K2)/(2*det)*(C[1]-B[1]) \
       - (C[0]**2+C[1]**2-B[0]**2-B[1]**2)/4
T = sp.expand(sp.numer(sp.together(expr)))
gb = sp.groebner([G2a, G3a], t1, s2, u, a, b, cc, order='grevlex')
gb.reduce(T)[1] == 0        # -> True
```
Running this (this builder's own from-scratch session, `sympy`, no imported
intermediate values): `eq2,eq3` built in `<1s`; the Gröbner basis of
`⟨G_{2a},G_{3a}⟩` has **18 generators**, built in **≈3s**; `gb.reduce(T)`
gives remainder **0**. By the standard theorem that Buchberger's algorithm's
normal-form reduction modulo a Gröbner basis is a decision procedure for
polynomial ideal membership (Cox–Little–O'Shea, *Ideals, Varieties, and
Algorithms*, Ch. 2; cited as the "Gröbner-basis ideal membership" technique
in `knowledge_base.md`), this proves
$$T \in \langle G_{2a}, G_{3a}\rangle \subset \mathbb Q[t_1,s_2,u,a,b,cc].$$
Since this is a genuine polynomial identity `T = q_1G_{2a}+q_2G_{3a}` with
`q_1,q_2\in\mathbb Q[t_1,s_2,u,a,b,cc]$ (not a numerical coincidence at
sampled points), it holds after substituting **any** real numbers for
`a,b,cc` (rational or irrational) — i.e. **`T` vanishes on the common zero
locus of `G_{2a},G_{3a}` for every real triangle `A,B,C`, not a sample.**
This closes gap 1 (genericity) completely.

**Two additional checks (this session, beyond both prior reports):**
- `T` is **not** in the ideal `⟨G_{2a}⟩` alone (`gb1 = groebner([G2a],...);
  gb1.reduce(T)[1] ≠ 0`) and not in `⟨G_{3a}⟩` alone. This confirms the
  certificate genuinely uses *both* constraints jointly — ruling out the
  degenerate/trivial-ideal pitfall `coordinate-bash` flagged in round 2
  (reducing modulo one constraint alone, with the other variable free, is
  not a valid membership test for a two-constraint system).
- **Explicit cofactor witness.** Using `sp.reduced(T, list(gb.polys), ...)`,
  wrote `T$ as an explicit combination `T=\sum_i q_i\,p_i$ of the 18
  computed Gröbner-basis elements `p_i$ (6 of the 18 `q_i` are nonzero, of
  polynomial degree 0–5) with remainder exactly `0`. Each `p_i$ is itself,
  by construction of Buchberger's algorithm (every basis element is
  produced from `S`-polynomial reductions of the original generators, hence
  is a polynomial combination of `G_{2a},G_{3a}` — the standard fact
  underlying the correctness theorem cited above), an element of
  `⟨G_{2a},G_{3a}⟩`. This gives a genuinely checkable (not black-box)
  witness: any reader can recompute `p_i` from `G_{2a},G_{3a}` via
  Buchberger's algorithm and verify `T-\sum q_ip_i` expands to `0` by direct
  polynomial arithmetic.

**Conclusion for §6:** for every real, non-degenerate triangle `A=(0,0),
B=(a,0), C=(b,cc)`, and every `(t_1,s_2,u)` on the branch `G_{2a}=G_{3a}=0`
with `t_1,s_2>0` (`K\ne B$, `L\ne C$), the target identity
`O\cdot(C-B)=(|C|^2-|B|^2)/4` holds **identically** — a complete, rigorous,
all-triangle proof of the central identity **on that branch**. Gap 1
(genericity) is closed.

### 7. What was NOT proved this round
`sympy.groebner([G2b,G3b],...)` (the other branch) was not run to
completion within a reasonable time budget by the genericity explorer, and
was not rerun here — this is not needed for the proof (only the correct
branch's membership matters) but is recorded as an unresolved side
computation, of no consequence to the argument.

### 8. Branch selection (gap 2) — precisely isolated, pushed, still open

**Why this is a genuinely different question from `fixed-point-concyclic`'s
now-closed sign gap.** `fixed-point-concyclic`'s (H2)/(H3) sign facts
(round 3, closed via the sign-lemma explorer's Part A) concern the sign of a
**cross product** — which of two rotation directions (`+\theta` vs
`-\theta`) is correct when converting an angle equality into a *signed*
angle statement. Here, hypotheses 2 and 3 are equalities of *unsigned*
angles in `(0,\pi)`, and the polynomial `(\dagger)` is obtained by squaring
`(V_1\cdot V_2)|V_3||V_4|=(V_3\cdot V_4)|V_1||V_2|` — an equation that is
ambiguous, after squaring, exactly between
$$\text{branch true:}\quad \cos\angle(V_1,V_2)=\cos\angle(V_3,V_4)\quad(\text{i.e. }\angle(V_1,V_2)=\angle(V_3,V_4), \text{ the actual hypothesis}),$$
$$\text{branch spurious:}\quad \cos\angle(V_1,V_2)=-\cos\angle(V_3,V_4)\quad(\text{i.e. }\angle(V_1,V_2)+\angle(V_3,V_4)=\pi).$$
This is a **dot-product** (acute-vs-obtuse-type) ambiguity, not a
cross-product one; the sign-lemma explorer's Part A technique (which
reduces exactly to `bxc` or `bxc/2` with no residual term) does not apply
here and was correctly not attempted here as a shortcut.

**What must be shown.** `G_{2a}=0` (not `G_{2b}=0`) must be identified as
the true branch for every genuine solution — i.e. for every point of the
family satisfying **all three** hypotheses (1,2,3) plus both containment
conditions (`K$ interior to `\triangle BMC$, `L$ interior to
`\triangle BNC$) plus the two "inside the angle" conditions. Equivalently
(if the natural conjecture below is correct): `\angle LBK,\angle LNC$ are
both acute and `\angle LCK,\angle BMK` are both acute at every genuine
solution — since two angles in `(0,\pi)` with equal cosine are actually
equal iff they're on the "matching-sign" side, and the numerics (below)
show they are consistently acute, so `+,+$ (both acute) is the consistent
sign pattern that would select `G_{2a}/G_{3a}` over `G_{2b}/G_{3b}` (this
correspondence — that `G_{2a}$ specifically, rather than `G_{2b}$, is the
`+,+$ branch — was confirmed numerically in round 2 on the concrete
triangle and is consistent with, but not independently re-derived
algebraically in, this round's symbolic setting; flagged honestly as a
piece still needing an explicit symbolic check, distinct from the
acute-angle claim itself.)

**Numeric evidence (imported from this round's sign-lemma explorer, Part
B, not re-run independently by this builder for lack of remaining time
budget — reported here as evidence, not as this builder's own
verification).** Across 9 distinct triangles (acute, obtuse-at-A,
obtuse-at-B, thin scalene, near-right) and ≈150 genuine solution points
(solved via the true, unsquared `arccos`-based system, filtered by both
containment conditions), **every** sampled point has
$$BL\cdot BK>0,\quad NL\cdot NC>0,\quad CK\cdot CL>0,\quad MB\cdot MK>0$$
(all four hypothesis angles acute), with observed maximum angle `\approx
49.4°` — a real margin below `90°`, not a marginal/borderline coincidence.
This is **strong evidence, not a proof** (per CLAUDE.md's "prove, don't
conjecture" rule, this remains labeled a conjecture).

### 9. Attempts to prove the acute-angle conjecture — genuine progress, not closed

**Attempt 1 (crude containment bound — shown insufficient).** Since `M` is
the midpoint of `AB`, ray `BM$ coincides exactly with ray `BA$, so `K$
interior to `\triangle BMC$ only forces ray `BK$ to lie strictly between ray
`BA$ and ray `BC$ (i.e. `0<\angle KBA<\angle ABC`) — the depth constraint
(how far along the ray `K$ may sit) does not further restrict the
*direction*. Symmetrically, since `N$ is the midpoint of `AC$, a point `L$
interior to `\triangle BNC$ has ray `BL$ strictly between ray `BN$ and ray
`BC$ (a standard cevian fact: for `N$ on segment `AC$, ray `BN$ is always
between rays `BA,BC$, since as `N$ traverses `AC$ from `A$ to `C$, ray `BN$
sweeps monotonically — proved by convexity: `N=(1-\lambda)A+\lambda C$ for
`\lambda\in(0,1)$ gives `\overrightarrow{BN}=(1-\lambda)\overrightarrow{BA}+\lambda\overrightarrow{BC}$,
a positive combination of `\overrightarrow{BA},\overrightarrow{BC}$, hence
between them in direction). Given `K$ interior to `\angle LBA$
(`\angle KBA<\angle LBA`, from the hypothesis "`K` lies inside the angle
`LBA`"), one gets `\angle LBK=\angle LBA-\angle KBA<\angle ABC$ — but this
alone only bounds `\angle LBK$ below `\angle ABC$, which can be up to nearly
`180°$ for an obtuse triangle, **not** below `90°$. **This crude bound is
insufficient**, confirming that the acute-ness genuinely requires the
*interlocking* system (hypotheses 1–3 together, pinning down the exact
values of `t_1,s_2$ given `u$, not merely the containment ranges) — a fact
consistent with the large gap between the crude bound (up to `180°`) and
the tight numeric evidence (`\le 49.4°`).

**Attempt 2 (resultant structure — a new lead, not developed into a
proof).** Computed, independently in this session,
$$\mathrm{Res}_{s_2}(G_{2a},G_{2b}) = 64\,u^2(u^2+1)^4\cdot\big[2u(a-b)+cc(u^2-1)\big]$$
$$\qquad\qquad\qquad{}\times\big[-2ab\,u+a\,cc(u^2-1)+2b^2u+2cc^2u\big]\times\big[2a(u^2-1)^2-b(u^2+1)^2\big]$$
(three nontrivial factors after removing the common `u^2(u^2+1)^4`, exactly
matching the round-2-analogous concrete-triangle computation upon
specializing `(a,b,cc)=(2,3/5,4/5)$; a fully symbolic, three-variable
computation, `sympy.resultant`, `<0.1$s). Using
`u^2-1=-(1+u^2)\cos\beta$, `2u=(1+u^2)\sin\beta$, the first factor
`2u(a-b)+cc(u^2-1)` simplifies (direct substitution, confirmed by
`sympy.simplify`) to
$$(1+u^2)\big[(a-b)\sin\beta - cc\cos\beta\big],$$
which is (up to the positive factor `1+u^2`) the cross product of the unit
direction `(\cos\beta,\sin\beta)$ (the direction of ray `BK`) with the
vector `B-C=(a-b,-cc)` — i.e. this factor vanishes exactly when ray `BK` is
**parallel to line `BC`**, a boundary/degenerate configuration (`K` would
lie on line `BC`, which is excluded since `K$ is interior to `\triangle
BMC`, hence strictly on one side of `BC`). The third factor similarly
simplifies (using the same substitution) to `(1+u^2)^2\big[2a\cos^2\beta -
b\big]`, i.e. `2a\cos^2\beta=b`; **this was not identified with a clean
degenerate geometric configuration in the time available** — it is recorded
here as a genuine open computation for a future round, not resolved.
**This is a real new finding (the resultant factors this cleanly was not
previously reported) but falls short of a proof**: showing that these three
factors have no common real root with `G_{2a}(s_2,u)$ (equivalently that
`G_{2a},G_{2b}` share no root `s_2$) *inside the actual valid parameter
range* would give the "no branch-crossing" half of the IVT argument
(`coordinate-bash-resultant-boundary`'s intended route), but this builder
did not complete (i) pinning down the valid range symbolically, nor (ii)
excluding these three resultant factors from vanishing inside it, nor (iii)
the boundary/limit acuteness check anchoring the IVT — all three remain
open.

**Honest conclusion.** Gap 2 (branch selection, all-triangle) is **not
closed** this round. What is newly established: (a) the crude
containment-based bound is provably insufficient (a genuine negative
result, saving a future round from retrying it), and (b) a new, exact
symbolic factorization of the relevant resultant, with a partial geometric
reading of one of its three factors — a concrete lead, not a proof.

**Round 4 update: (a) is superseded by an outright refutation (§(a) above,
"Approaches tried" list) — the acute-angle conjecture as a whole is now
known to be false, not merely unproved, so this whole sub-route (§§8–9) is
retired. (b) is unaffected and remains a live, undeveloped lead, now handed
to `coordinate-bash-resultant-boundary`'s IVT mechanism.**

### 10. The isosceles case `AB=AC` — new standalone lemma, proved (this round's second deliverable)

Full statement and proof are written up as a self-contained lemma,
proposed for certification at `lemmas/isosceles-case-symmetry.md` (content
summarized here; see that file for the complete, standalone version).

**Setting.** Triangle `ABC` with `AB=AC` (i.e. `b=c` in the
`ptolemy-trig-identity` notation `a=BC,b=CA,c=AB`). Import verbatim from
`ptolemy-trig-identity.md` (no re-derivation): the angle notation
`θ:=∠KBA=∠ACL`, `ψ:=∠LCK`, `φ:=∠LNC`, Lemma 1 (two-ray construction of
`K,L`), and the decoupled constraint equations (III) (governing `ψ` from
`θ,A,C`) and (IV) (governing `φ` from `θ,A,B`).

**Step 1 (`B=C`).** `AB=AC` and the Law of Sines (`b/\sin B=c/\sin C`)
give `\sin B=\sin C`; since `B,C\in(0,\pi)` and `B+C<\pi` (as `A>0`), the
supplementary alternative `B=\pi-C` would force `A=0`, excluded, so `B=C`.

**Step 2 (the domain of `(θ,ψ)`, made explicit — not stated this
precisely by any prior approach).** From Lemma 2's triangle `BKC`
(`∠KBC=B-θ`, `∠KCB=C-\theta-\psi`, both must be positive for a genuine
triangle), the valid domain is `θ\in(0,B)`, `ψ\in(0,C-θ)`; symmetrically
for `(θ,φ)` via (IV) and triangle `CLB`: `θ\in(0,C)`, `φ\in(0,B-θ)`. When
`B=C` these two domains coincide exactly: `θ\in(0,B)`, and both `ψ,φ\in(0,B-θ)`.

**Step 3 (existence and uniqueness of the common root — closes the gap the
round-4 ptolemy-lens explorer flagged but did not itself prove).** When
`B=C`, (III) and (IV) become the identical equation (same right-hand side,
since swapping `B\leftrightarrow C` in (IV)'s formula, with `B=C`, returns
(III)'s formula verbatim). Write it as `\Phi(\theta,x)=0` where, for fixed
`θ\in(0,B)`,
$$f(x):=\frac{\sin x}{\sin(\theta+x)},\qquad g(x):=2\frac{\sin A}{\sin B}\cdot\frac{\sin(B-\theta-x)}{\sin(A+2\theta+x)},\qquad \Phi(\theta,x):=f(x)-g(x),$$
for `x\in(0,B-θ)`. **Both `f,g` are well-defined and positive on this open
interval**: for `x\in(0,B-θ)`, `θ+x\in(0,B)\subset(0,\pi)` so `\sin(\theta+x)>0`;
and `A+2\theta+x<A+2\theta+(B-\theta)=A+B+\theta<A+B+B\le\pi` is not quite
tight enough by itself, so argue directly: `A+2\theta+x < A+\theta+B`
(using `x<B-\theta`) `=A+C+\theta` (as `B=C`) `<A+B+C=\pi` (using
`\theta<B`); combined with `A+2\theta+x>A>0`, this gives
`A+2\theta+x\in(0,\pi)`, so `\sin(A+2\theta+x)>0`, and `B-\theta-x\in(0,B)`
(from `0<x<B-\theta`) so `\sin(B-\theta-x)>0`. Hence `f,g>0` throughout.

*Monotonicity.* Using the elementary identity
`\sin(\theta+x)\cos x-\cos(\theta+x)\sin x=\sin\theta` (angle-subtraction,
with the two terms being the `x`-derivative numerator of `f`):
$$f'(x)=\frac{\cos x\sin(\theta+x)-\sin x\cos(\theta+x)}{\sin^2(\theta+x)}=\frac{\sin\theta}{\sin^2(\theta+x)}>0\quad(\theta\in(0,B)\subset(0,\pi)\Rightarrow\sin\theta>0),$$
so `f` is **strictly increasing**. For `g`, write `u:=B-\theta-x`
(`du/dx=-1`), `v:=A+2\theta+x` (`dv/dx=1`); the same identity applied to
`\sin u/\sin v` gives
$$g'(x)=-\frac{2\sin A}{\sin B}\cdot\frac{\sin(u+v)}{\sin^2 v},\qquad u+v=(B-\theta-x)+(A+2\theta+x)=A+B+\theta.$$
Using `A+B+\theta=(\pi-C)+\theta=\pi-B+\theta` (as `B=C`), `\sin(u+v)=\sin(\pi-B+\theta)=\sin(B-\theta)`,
and `B-\theta\in(0,B)\subset(0,\pi)` (as `\theta\in(0,B)`) gives `\sin(B-\theta)>0`.
Hence `g'(x)=-\frac{2\sin A}{\sin B}\cdot\frac{\sin(B-\theta)}{\sin^2 v}<0`:
`g` is **strictly decreasing**.

Therefore `\Phi(\theta,\cdot)=f-g` is **strictly increasing** on
`(0,B-\theta)`. Boundary values: as `x\to0^+`, `f\to0` and
`g\to \frac{2\sin A}{\sin B}\cdot\frac{\sin(B-\theta)}{\sin(A+2\theta)}>0`,
so `\Phi\to` a negative value; as `x\to(B-\theta)^-`, `g\to0` and
`f\to\sin(B-\theta)/\sin(B)>0`, so `\Phi\to` a positive value. By the
intermediate value theorem (continuity of `\Phi` on the closed sub-interval,
guaranteed since numerator and denominator sines are bounded away from `0`
except exactly at the two endpoints), `\Phi(\theta,\cdot)` has **at least
one** root in `(0,B-\theta)`; strict monotonicity gives **at most one**.
Hence a **unique** root `x(\theta)\in(0,B-\theta)`.

Since `ψ` solves (III)`=\Phi(\theta,\cdot)=0` and `φ` solves (IV), which is
the identical equation `\Phi(\theta,\cdot)=0` when `B=C`, both `ψ` and `φ`
equal the **same unique root** `x(\theta)`:
$$\boxed{\psi=\varphi=x(\theta)\quad\text{for every }\theta\in(0,B).}$$
This is the existence/uniqueness argument the round-4 ptolemy-lens
explorer flagged as needed but did not itself supply ("likely easy...
should be confirmed, not assumed") — it is now supplied in full, not
merely asserted.

**Step 4 (reflection sends `K` to `L`, given `ψ=φ`).** Place coordinates
with the axis of symmetry as a fixed line through `A` and let `\sigma_{\mathrm{refl}}`
denote reflection across it; since `AB=AC`, this axis is exactly the
perpendicular bisector of `BC`, so `\sigma_{\mathrm{refl}}` fixes `A` and
swaps `B\leftrightarrow C`. By Lemma 1 (imported), `K` is the intersection
of (ray from `B`, angle `θ` from ray `BA`, on the `C`-side of line `AB`)
and (ray from `C`, angle `θ+ψ` from ray `CA`, on the `B`-side of line
`AC`); `L` is the intersection of (ray from `B`, angle `θ+φ` from ray
`BA`, [`C`-side of `AB`]) and (ray from `C`, angle `θ` from ray `CA`,
[`B`-side of `AC`]).

`\sigma_{\mathrm{refl}}` is an isometry fixing `A`, sending `B\mapsto C`
and `C\mapsto B`; it therefore sends ray `BA\mapsto` ray `CA` and ray
`CA\mapsto` ray `BA` (a ray from a point `P` through a fixed point `A` maps
to the ray from `\sigma_{\mathrm{refl}}(P)` through `A`), and — since it
maps the whole triangle `ABC` to itself as a set, swapping the two
half-planes determined by each side through the swap `B\leftrightarrow
C` — it sends "`C`-side of `AB`" to "`B`-side of `AC`" (this is exactly the
combinatorial content already certified in `lemmas/sigma-symmetry.md`'s
relabeling `\sigma$: swap `B\leftrightarrow C,K\leftrightarrow L,M\leftrightarrow N`,
here realized as an honest Euclidean isometry rather than an abstract
relabeling, because the ambient triangle itself is symmetric). Since
angle magnitude is preserved by an isometry, `\sigma_{\mathrm{refl}}` maps:
- (ray from `B`, angle `θ` from `BA`, `C`-side) `\mapsto` (ray from `C`,
  angle `θ` from `CA`, `B`-side) — exactly `L`'s second defining ray;
- (ray from `C`, angle `θ+ψ` from `CA`, `B`-side) `\mapsto` (ray from `B`,
  angle `θ+ψ` from `BA`, `C`-side) `=` (ray from `B`, angle `θ+φ` from
  `BA`, `C`-side) (using `ψ=φ`, Step 3) — exactly `L`'s first defining ray.

Since `\sigma_{\mathrm{refl}}` maps `K$ (the intersection of the two
`K`-rays) to the intersection of the two images, and those images are
exactly `L`'s two defining rays,
$$\sigma_{\mathrm{refl}}(K)=L.$$

**Step 5 (`OM=ON`).** `\sigma_{\mathrm{refl}}` fixes `A`, sends
`B\mapsto C` hence the midpoint `M` of `AB` to the midpoint of `AC`, i.e.
`\sigma_{\mathrm{refl}}(M)=N`, and (Step 4) `\sigma_{\mathrm{refl}}(K)=L`.
Provided `A,K,L` are not collinear (Step 6), the circumcircle
`\omega=\mathrm{circle}(A,K,L)` exists and is unique; since
`\sigma_{\mathrm{refl}}` is an isometry sending the point-set `\{A,K,L\}`
to `\{\sigma_{\mathrm{refl}}(A),\sigma_{\mathrm{refl}}(K),\sigma_{\mathrm{refl}}(L)\}
=\{A,L,\sigma_{\mathrm{refl}}(L)\}` — and since `\sigma_{\mathrm{refl}}` is
an involution (`\sigma_{\mathrm{refl}}^2=\mathrm{id}`), applying it to
`\sigma_{\mathrm{refl}}(K)=L` gives `\sigma_{\mathrm{refl}}(L)=K`, so the
image point-set is exactly `\{A,L,K\}=\{A,K,L\}` — `\sigma_{\mathrm{refl}}`
maps `\omega` to the circle through the same three points, i.e.
`\sigma_{\mathrm{refl}}(\omega)=\omega`. Hence its center `O` satisfies
`\sigma_{\mathrm{refl}}(O)=O` (the center of a circle is an isometry
invariant of the circle, and `\sigma_{\mathrm{refl}}` maps `\omega` to
itself, so it maps `O$ to the center of `\sigma_{\mathrm{refl}}(\omega)=\omega`,
i.e. to `O$ itself). Finally, since `\sigma_{\mathrm{refl}}` is an isometry,
$$OM=d(O,M)=d(\sigma_{\mathrm{refl}}(O),\sigma_{\mathrm{refl}}(M))=d(O,N)=ON.$$
$$\blacksquare$$

**Step 6 (non-collinearity of `A,K,L` — cited explicitly, not waved
through, per the outline-reviewer's instruction).** Two distinct ways
`A,K,L` could fail to be a genuine triangle: (i) `K` lies on the axis of
symmetry (so `\sigma_{\mathrm{refl}}(K)=K`, forcing `K=L` by Step 4); or
(ii) `K\ne L` but the line `AK` happens to be exactly the one non-axis
line through `A` that is mapped to itself by `\sigma_{\mathrm{refl}}`,
namely the line through `A` **perpendicular** to the axis (equivalently,
parallel to `BC`, since the axis is itself perpendicular to `BC`) — a
standard fact about reflections (a line through the fixed point `A` maps
to itself under a reflection iff it is the mirror line or perpendicular to
it), which combined with `\sigma_{\mathrm{refl}}(K)=L` would put `A,K,L`
on this common line, i.e. collinear.

*(ii) is ruled out unconditionally.* Set up coordinates with `A=(0,h)`,
`B=(-d,0)`, `C=(d,0)` (`h,d>0`; the axis is the `y`-axis, and line `AK\parallel BC`
means `K` has `y`-coordinate exactly `h`, i.e. `K` lies on the horizontal
line through `A`). `M=`midpoint`(A,B)=(-d/2,h/2)`; the triangle `BMC` has
vertices `B=(-d,0)`, `M=(-d/2,h/2)`, `C=(d,0)`, all three with
`y`-coordinate `\le h/2<h`, so (as a convex hull of these three points, the
whole closed triangle `BMC` has `y\le h/2$ everywhere) **no point of
`\triangle BMC`, interior or boundary, has `y`-coordinate `h`**. Since `K`
is hypothesised strictly interior to `\triangle BMC`, `K`'s `y`-coordinate
is `<h/2<h`, so `K` is **not** on the line `y=h$, ruling out (ii)
unconditionally (for every isosceles triangle and every genuine `K`).

*(i) is not independently excluded here — flagged honestly as the one
residual piece.* Whether the axis of symmetry can pass through the
interior of `\triangle BMC$ at exactly the point `K(\theta)$ determined by
`θ` and `x(\theta)$ (Step 3) for some `θ\in(0,B)$ is not ruled out by the
containment hypothesis alone (unlike (ii), the axis genuinely does cross
the interior of `\triangle BMC$ in general — `B,M$ have `x<0$ and `C$ has
`x>0$ in the coordinates above, so the axis `x=0$ separates them and
passes through the interior for a range of the triangle's own shape).
Excluding `K=L` (equivalently `K` on the axis) for every `θ` in the valid
range would require tracking the explicit `x`-coordinate of
`K(\theta,x(\theta))` through the Weierstrass/rotation parametrization and
showing it is never `0` — a further symbolic computation not carried out
this round. **This is inherited from, not newly introduced by, the
population's standing non-degeneracy hypothesis** — every approach in the
population already assumes `A,K,L` form a genuine (non-collinear, in
particular non-coincident-vertex) triangle whenever it speaks of "the
circumcenter `O` of `A,K,L`" (this is implicit in the problem's own
claim, which presupposes `O` exists); this lemma does not need a *new*
assumption beyond that standing one, but it also does not independently
verify that the standing assumption is automatically satisfied in the
isosceles sub-case — an honest, precisely isolated open point, not a
hand-wave.

**Conclusion.** For every isosceles triangle `AB=AC` and every `θ\in(0,B)`
giving a genuine configuration with `K\ne L` (the one inherited,
un-independently-verified non-degeneracy noted in Step 6(i)), `OM=ON`
holds — proved directly by reflection symmetry, with **no reference to
`Q`, Ptolemy, the rotation-parametrization/Gröbner machinery, or branch
selection**. This is a strictly stronger and more self-contained result
than the round-1 flag ("isosceles case unaddressed") anticipated, and
supersedes `fixed-point-concyclic`'s `Q=A` degeneracy for this sub-case
(that approach's Q-based reduction can now simply cite this lemma instead
of separately handling `AB=AC`).

## Full proof
(Not present — Status is `partial`. Gap 1, genericity of the central
identity `O·(C−B)=(|C|²−|B|²)/4` on the branch `G2a=G3a=0`, is now **fully
closed** for every real (in particular every scalene) triangle (§§2–6).
The single remaining gap for a complete solution of the whole problem is:
proving, for every scalene triangle and every valid configuration, that
the genuine solution always lies on this branch rather than the
extraneous `G2b=G3b` branch. **The acute-angle-bound mechanism attempted
for this in rounds 3–4 is now conclusively refuted** (§§8–9, and "Approaches
tried" round 4(a) above) — it is not merely unproved but false, so it must
not be pursued further; the live mechanism for this gap is
`coordinate-bash-resultant-boundary`'s continuity/IVT route. Separately,
the **isosceles case `AB=AC` is now fully resolved** by a self-contained
reflection-symmetry argument (§10, proposed as
`lemmas/isosceles-case-symmetry.md`), independent of branch selection
entirely, modulo one honestly-isolated residual non-degeneracy point
(§10, Step 6(i): `K\ne L$, inherited from the population's standing
genericity hypothesis, not independently re-verified for the isosceles
sub-case specifically).)

## Promotable lemmas

- **Symbolic genericity certificate (§§2–6).** In the rotation
  parametrization `K=B+t_1(-\cos\beta,\sin\beta)$, `L=C+s_2R(\beta)(A-C)$
  (Weierstrass-rationalized, `u=\tan(\beta/2)`), for the fully symbolic
  triangle `A=(0,0),B=(a,0),C=(b,cc)`, the target numerator
  `T(t_1,s_2,u,a,b,cc)` (numerator of `O\cdot(C-B)-(|C|^2-|B|^2)/4` for
  `O=$ circumcenter of `A,K,L`) lies in the ideal `\langle
  G_{2a},G_{3a}\rangle\subset\mathbb Q[t_1,s_2,u,a,b,cc]` — verified by
  Gröbner-basis reduction (18 generators, grevlex order, remainder `0`),
  independently reproduced three times (genericity explorer,
  outline-reviewer, this builder). `G_{2a},G_{3a}` given explicitly in §4.
  This supersedes the round-2 concrete-triangle certificate (it specializes
  to it at `(a,b,cc)=(2,3/5,4/5)`) and should replace it as the certified
  lemma for the central identity, on the branch `G_{2a}=G_{3a}=0`, for every
  real triangle. **Recommend the reviewer certify this as
  `lemmas/symbolic-genericity-certificate.md`, superseding
  `lemmas/homogeneity-decoupling-rotation-param.md`'s concrete-triangle
  scope** (the homogeneity-decoupling fact itself, `eq_2=t_1^2g_2,
  eq_3=s_2^2g_3`, remains correctly certified as already stated — only the
  *concrete-triangle-only* framing of the downstream ideal-membership
  certificate needs upgrading to this symbolic version).
- **Crude-containment-bound insufficiency (§9, Attempt 1).** For `K$
  interior to `\triangle BMC$ and `L$ interior to `\triangle BNC$ with `K$
  interior to `\angle LBA$, the containment hypotheses alone give only
  `0<\angle LBK<\angle ABC` (via the cevian-ray monotonicity fact and the
  observation that ray `BM`=ray `BA`), which does **not** imply
  `\angle LBK<90°$ in general — a genuine negative result (proved, not
  conjectured) useful to prevent a future round from re-attempting the same
  crude bound.
- **Isosceles-case reflection symmetry (§10, this round).** For `AB=AC`,
  the decoupled constraints (III),(IV) collapse to one equation with a
  proved-unique root (Step 3: monotonicity + IVT, a genuine new proof, not
  merely a flagged-as-needed claim), forcing `ψ=φ`; this and Lemma 1
  (imported) give `\sigma_{\mathrm{refl}}(K)=L` for the reflection across
  the triangle's axis of symmetry (Step 4), whence `OM=ON` follows by a
  three-line isometry argument (Step 5) — entirely independent of `Q`,
  Ptolemy, and the rotation-parametrization/Gröbner/branch-selection
  machinery used elsewhere. One piece (`K\ne L`, i.e. `K` not exactly on
  the axis) is honestly left as inherited from the population's standing
  non-degeneracy hypothesis, not independently re-verified for this
  sub-case (Step 6(i)); the other possible degeneracy (`A,K,L` collinear
  via `AK\parallel BC`) **is** ruled out unconditionally (Step 6(ii), an
  elementary height argument: `\triangle BMC` never reaches the height of
  `A`). **Recommend the reviewer certify this as
  `lemmas/isosceles-case-symmetry.md`**, reusable by every approach in the
  population (in particular, superseding `fixed-point-concyclic`'s `Q=A`
  degeneracy for `AB=AC`), conditional on confirming Step 6(i)'s residual
  point is an acceptable standing assumption rather than a required new
  proof obligation.
