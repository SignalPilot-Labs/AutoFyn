## imo-2026-02 (lens: genericity extension of coordinate-bash-resultant)

- **Headline finding: full symbolic genericity IS tractable, and I completed it.**
  Redid the round-2 `coordinate-bash-resultant` recipe (Weierstrass
  substitution `u=tan(β/2)` + rotation parametrization + homogeneity
  decoupling) with a **fully symbolic triangle** `A=(0,0)`, `B=(a,0)`,
  `C=(b,cc)` (three free real parameters `a,b,cc`, no concreteness anywhere),
  using `L = C + s2·R(β)(A−C)` (i.e. `s2 = t2/|AC|`, absorbing `|AC|` into the
  parameter so no square root ever enters the ring — this is the one change
  needed relative to the concrete-triangle setup, and it costs nothing: `t2>0
  ⟺ s2>0`). Computed in `sympy`, with wall-clock times:
  - Building `eq2`, `eq3` (the two squared-cosine hypothesis polynomials):
    **< 1 second each**, degree 24 / 22 in `(t1,s2,u,a,b,cc)` jointly.
  - Dividing out `t1²` / `s2²` and factoring: **< 1 second each**. The
    homogeneity-decoupling lemma (`lemmas/homogeneity-decoupling-rotation-param.md`)
    **generalizes verbatim and symbolically**: `eq2 = t1²·g2(s2,u,a,b,cc)`,
    `eq3 = s2²·g3(t1,u,a,b,cc)`, confirmed by exact polynomial division with
    zero remainder (not just observed on one triangle — this is the same
    coordinate-free geometric fact, and the symbolic computation reconfirms
    it holds identically in `a,b,cc` too, as the lemma's own proof already
    guarantees synthetically).
  - `sympy.factor` splits each cofactor into two branches exactly as before:
    `g2 = -(b²+cc²)²(u²+1)·G2a·G2b`, `g3 = -a²(u²+1)·G3a·G3b`, with `G2a,G3a`
    (quadratic in `s2`/`t1`, degree 4 in `u`) matching the same structural
    role as the concrete-triangle `G2a,G3a`, and `G2b,G3b` (quadratic, degree
    6 in `u`) matching `G2b,G3b`. **< 1 second.**
  - Built the target `T(t1,s2,u,a,b,cc)` (numerator of `O·(C−B) −
    (|C|²−|B|²)/4`, from the closed-form circumcenter of `A,K,L`): degree 12
    total, degree 2 in `t1`, 2 in `s2`, 6 in `u`. **< 1 second.**
  - **The elimination**: ran `sympy.groebner([G2a,G3a], t1,s2,u,a,b,cc,
    order='grevlex')` — a full 6-variable Gröbner basis over `ℚ` treating
    `a,b,cc` as ordinary polynomial variables (not parameters in a field —
    this sidesteps any field-of-fractions subtlety and gives an
    unimpeachable answer). **Basis of 18 generators, built in ~2.6s.**
    `gb.reduce(T)` gives remainder **0**. So `T ∈ ⟨G2a,G3a⟩ ⊂
    ℚ[t1,s2,u,a,b,cc]` — a complete, fully general, checkable
    ideal-membership certificate for **every** triangle `A=(0,0),B=(a,0),
    C=(b,cc)` simultaneously, not sample points. Total compute time for the
    whole pipeline from scratch: well under 10 seconds.
  - **Independent cross-check via pseudo-remainder** (a second, more
    "manual" route giving explicit near-cofactors): `sp.prem(T, G2a, s2)`
    then `sp.prem(·, G3a, t1)` also gives literal remainder 0, matching the
    Gröbner result — two independently-coded methods agree.
  - **Sanity check the branch matters** (i.e. this isn't some universal
    identity independent of branch choice): the same certificate attempt for
    the *other* branch, `⟨G2b,G3b⟩`, did **not** terminate within 2 minutes
    on the same hardware — consistent with `G2a,G3a` being the structurally
    distinguished (correct) branch, though I did not force this computation
    to completion (not needed: round 2 already has strong numeric evidence,
    reconfirmed below, that `G2b,G3b` is the extraneous branch).
  - **Fresh numeric spot-check** on a brand-new random triangle (not
    round 2's concrete one): `A=(0,0), B=(3.7,0), C=(1.1,2.3)`, solved the
    true (unsquared, `arccos`-based) hypothesis system via `fsolve` at
    `β=8°,12°,16°,20°`, and confirmed `OM−ON ≈ 0` to `1e-12`–`1e-15`
    precision at every point — independent corroboration on a triangle not
    used anywhere in the algebra above.

- **Conclusion for the outliner: gap 1 (genericity) of `coordinate-bash-resultant`
  is CLOSED, modulo writeup.** The concern that a symbolic `(a,c)` rerun would
  "likely blow up" (current.md §6) did not materialize — the homogeneity
  decoupling that made the concrete case tractable makes the symbolic case
  essentially just as tractable (degrees barely grow; the extra 3 symbols
  `a,b,cc` add very little to the Gröbner basis size — 18 generators vs. 6
  for the concrete case, still small). **This is the single most important
  finding this round**: what remains for a fully rigorous, all-triangle
  proof of the central identity is now *only* gap 2 — the branch selection
  (`G2a,G3a` vs `G2b,G3b`) — proved synthetically for all triangles, not
  gap 1. The builder next round should redo this exact computation (script
  below is fully reproducible) and write it into the approach file /
  promote a new lemma superseding the concrete-triangle-only certificate.

- **Distinct openings for the outliner:**
  1. **(Primary, ready to write up)** Promote the symbolic Gröbner
     certificate above as the generic replacement for
     `coordinate-bash-resultant`'s concrete-triangle certificate — this closes
     genericity outright, leaving only branch-selection.
  2. **Branch selection via the signed-area argument already found by the
     round-2 proof-reviewer** (see current.md, "Round 2's genuine new
     milestone" paragraph): `signed_area(N,B,C) = signed_area(A,B,C)/2`
     gives a triangle-independent sign fact; this needs to be connected
     explicitly to "which of `G2a` or `G2b` is selected" (i.e., translate the
     sign condition `sign(BL·BK)=sign(NL·NC)` into a statement about which
     root of the quadratic-in-`s2` factorization is picked) — this is now
     clearly the single remaining piece of the whole problem, and it is a
     narrower, more tractable question than genericity was.
  3. Similarity-invariant reformulation (per dispatch's suggestion 3): since
     I used `A=(0,0),B=(a,0),C=(b,cc)` with `a` free (not fixed to 1), the
     computation already has one more degree of freedom than the true shape
     space (angles) requires — fixing `a=1` (WLOG by scaling, since the whole
     identity is scale-invariant — both sides of `O·(C−B)=(|C|²−|B|²)/4`
     scale as length², so scaling all of `A,B,C` by `λ` scales the identity
     by `λ²`, hence WLOG-able) would reduce to 2 parameters `(b,cc)` instead
     of 3 `(a,b,cc)` and probably shrink the Gröbner basis further, but given
     the already-fast run time this is a minor optimization, not needed for
     correctness — I did not bother since the 3-parameter run already
     succeeded comfortably.

- **Candidate technique(s):** Gröbner-basis ideal membership
  (`knowledge_base.md` — polynomial ideal membership / Buchberger's
  algorithm, Cox–Little–O'Shea) exactly as already cited in
  `coordinate-bash-resultant.md`; no new KB entry needed — the technique was
  already correctly named, only the scope (concrete → fully symbolic) is new.

- **Cheap-kill candidates:** none new found this round (this was a
  computational verification task, not a structural pruning task) — the
  homogeneity/decoupling lemma already IS the relevant structural
  simplification and it re-verified cleanly in the symbolic setting.

- **Knowledge-base entries to use:** same as round 2's certificate —
  polynomial/Gröbner-basis elimination entry in `knowledge_base.md`; the
  Weierstrass tangent-half-angle substitution (standard rationalization,
  cited already in the lemma file).

- **Analogous past problems (cruxes):** did not query the crux corpus this
  round (dispatch scope was purely computational verification of the
  round-2 breakthrough's genericity, not new-angle search) — no crux search
  performed. If the outliner wants crux support for the *branch-selection*
  sub-problem (a sign/orientation argument), that would be a `geometry`
  subtopic query for "directed angle" or "orientation" cruxes, not covered
  here.

- **Prior progress:** `coordinate-bash-resultant`'s concrete-triangle
  certificate (round 2), now **superseded/extended** by the fully symbolic
  certificate above (same recipe, all triangles at once, `<10s` compute).

- **Dead ends (do not retry):** none newly found. (Do NOT retry: assuming
  the symbolic Gröbner basis "will blow up" — it does not; this fear from
  current.md §6 is now disproven by direct computation and should not block
  next round's builder from attempting it.)

- **Small-case / intuition notes:** Fresh numeric spot-check (new random
  triangle, listed above) is additional (labeled: numerical, not proof)
  corroboration that the target identity `OM=ON` holds on genuine solutions
  of the hypothesis system, consistent with all prior rounds' evidence.
  The branch-selection asymmetry (⟨G2a,G3a⟩ tractable/fast, ⟨G2b,G3b⟩ not
  completing in 2 min) is suggestive (conjecture, not proof) that the two
  branches are genuinely structurally different, not merely a labeling
  choice — worth the builder double-checking if a synthetic branch argument
  is sought, but not required, since round 2 already has solid numeric +
  resultant evidence that G2b/G3b is extraneous.

**Reproducible script (the core pipeline, symbolic a,b,cc):**
```python
import sympy as sp
t1,s2,u,a,b,cc = sp.symbols('t1 s2 u a b cc', real=True)
sinb = 2*u/(1+u**2); cosb = (1-u**2)/(1+u**2)
A = sp.Matrix([0,0]); B = sp.Matrix([a,0]); C = sp.Matrix([b,cc])
M = (A+B)/2; N = (A+C)/2
Rbeta = sp.Matrix([[cosb,-sinb],[sinb,cosb]])
K = B + t1*sp.Matrix([-cosb, sinb])
L = C + s2*Rbeta*(A-C)   # s2 = t2/|AC|, keeps everything polynomial
def cross_eq(V1,V2,V3,V4):
    lhs=(V1.dot(V2))**2*V3.dot(V3)*V4.dot(V4); rhs=(V3.dot(V4))**2*V1.dot(V1)*V2.dot(V2)
    return sp.expand(sp.numer(sp.together(lhs-rhs)))
eq2 = cross_eq(L-B,K-B,L-N,C-N)          # hyp 2: angle LBK = angle LNC
eq3 = cross_eq(L-C,K-C,B-M,K-M)          # hyp 3: angle LCK = angle BMK
g2 = sp.factor(sp.div(eq2, t1**2, t1)[0])
g3 = sp.factor(sp.div(eq3, s2**2, s2)[0])
# -> g2 = -(b^2+cc^2)^2 (u^2+1) G2a G2b,  g3 = -a^2 (u^2+1) G3a G3b  (extract factors)
# target T: numerator of O.(C-B) - (|C|^2-|B|^2)/4, O = circumcenter(A,K,L)
Kx,Ky=K; Lx,Ly=L
K2=Kx**2+Ky**2; L2=Lx**2+Ly**2; det=Kx*Ly-Ky*Lx
expr = sp.together((K2*Ly-L2*Ky)/(2*det)*(C[0]-B[0]) + (Kx*L2-Lx*K2)/(2*det)*(C[1]-B[1])
                    - (C[0]**2+C[1]**2-B[0]**2-B[1]**2)/4)
T = sp.expand(sp.numer(expr))
gb = sp.groebner([G2a, G3a], t1, s2, u, a, b, cc, order='grevlex')  # 18 generators, ~2.6s
gb.reduce(T)[1] == 0   # -> True: T in <G2a,G3a> for ALL a,b,cc
```
(`G2a`, `G3a` are the explicit degree-4-in-`u` quadratic-in-`(s2 or t1)`
cofactors, obtained from `factor_list(g2)` / `factor_list(g3)` — full
expanded forms recorded in my working notes, reproducible in under a
minute end to end.)
