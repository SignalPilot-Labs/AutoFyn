## imo-2026-02

### Scope of this report
Lens: symbolic root-counting (Sturm/discriminant/resultant sign-determination)
applied specifically to closing `coordinate-bash-resultant-boundary.md` §13's
open gap — full 3-way exclusion of `G_{2b}`'s roots (positivity `s_2>0` +
true-root status `W>0` + containment/sign `L_1<0 ∧ \tilde N_2>0`). All claims
below are my own from-scratch `sympy`/numpy computations this round (not
copied from any file), explicitly labeled proved-symbolically vs. numeric.

### Exact target objects, independently re-derived
Working directly from the coordinate definitions `A=(0,0),B=(a,0),C=(b,cc)`,
`K=B+t_1(-\cosβ,\sinβ)`, `L=C+s_2R(β)(A-C)` (Weierstrass `u=\tanβ/2`), I
rebuilt `eq2` from the raw dot-product/cos-equality construction, divided by
`t_1^2`, and factored: this reproduces `G_{2a}` **exactly** (term-for-term
match with the certified formula) and gives the **first time `G_{2b}` has
been displayed explicitly in this population's records**:
```
G_2b = 8a s2 u^5 - 8a s2 u + 2a u^5 + 4a u^3 + 2a u
     - 12b s2^2 u^5 + 40b s2^2 u^3 - 12b s2^2 u - 12b s2 u^5 + 12b s2 u
     - 2b u^5 - 4b u^3 - 2b u
     + 2cc s2^2 u^6 - 30cc s2^2 u^4 + 30cc s2^2 u^2 - 2cc s2^2
     + 3cc s2 u^6 - 15cc s2 u^4 - 15cc s2 u^2 + 3cc s2
     + cc u^6 + cc u^4 - cc u^2 - cc
```
Leading coeff `B_2 = 2(-6bu^5+20bu^3-6bu+cc u^6-15cc u^4+15cc u^2-cc)` matches
the file's reported value exactly. Also independently re-derived, and
confirmed exact term-for-term matches with, `D_K(s_2)`, `D_N(s_2)` (the
true/supplementary test's affine numerators), `L_1(s_2)=P+s_2Q` (the
K-inside-angle-LBA test), and `\tilde N_2(s_2)` (the L-inside-triangle-BNC
containment test):
```
tildeN2(s2) = [-8ab u + 4a cc u^2 - 4a cc + 4b^2 u + 4cc^2 u] s2 + [2a cc u^2 + 2a cc]
```

### New symbolic findings this round (all fresh `sympy.resultant` computations)
Computed all four pairwise resultants `Res_{s2}(G_2b, D_K)`, `Res(G_2b,D_N)`,
`Res(G_2b,L_1)` (already known), `Res(G_2b,\tilde N_2)` — all four factor
cleanly and **share recurring factors with the already-certified sign facts
`F_1<0`, `F_2<0`** (Lemma 11.6) and with `Y:=2a(u^2-1)^2-b(u^2+1)^2` (the
"perfect square" factor from the certified `g2b-true-supplementary-parity`
theorem):
```
Res(G2b, D_K)      = (u^2+1)^4 · F2 · Y
Res(G2b, D_N)      = -4u(b^2+cc^2)^2(u^2+1)^2 · Y
Res(G2b, L_1)       = -4u(u^2+1)^4 · F1 · F2          [independently reproduces the file's §11 formula]
Res(G2b, tildeN2)  = -8u(u^2+1)^2 · F2 · Z
```
where `Z` is an explicit cubic-degree (in `u`, with `a,b,cc` coefficients)
polynomial (given in my scratch code, reportable to the outliner on request).

**New lemma-candidate (proved, not numeric): `D_K` and `D_N` always agree in
"both-roots-product" sign, independent of the unknown signs of `B_2` and
`Y`.** Taking the ratio `Res(G2b,D_K)/Res(G2b,D_N)` the unknown factor `Y`
cancels exactly (verified symbolically, zero remainder):
$$\frac{D_K(r_1)D_K(r_2)}{D_N(r_1)D_N(r_2)} = \frac{\mathrm{Res}(G_{2b},D_K)}{\mathrm{Res}(G_{2b},D_N)} = \frac{-(u^2+1)^2F_2}{4u(b^2+cc^2)^2} > 0$$
(using `F_2<0`, `u>0`, already-certified). So `\mathrm{sign}(D_K(r_1)D_K(r_2)) = \mathrm{sign}(D_N(r_1)D_N(r_2))` **always**, throughout the valid range,
for every triangle — a clean, `B_2`/`Y`-independent fact, and (as a sanity
check) multiplying the two ratios reproduces exactly the already-certified
`W(r_1)W(r_2)\ge0` theorem, confirming consistency with the existing
certified lemma rather than contradicting it.

**Threshold-ordering ("fixed Sturm interval chart") approach: tested and
REFUTED as a route.** I tried the natural Sturm-style idea: if the zero
locations of `D_K,D_N,L_1,\tilde N_2` (each affine in `s_2`) had a FIXED
order relative to each other and to `s_2=0` across the whole triangle
family, the joint 3-way exclusion would reduce to a finite interval sign
chart (classical Sturm-sequence-style root isolation). **This is false**:
sweeping 3000 random valid `(a,b,cc,β)` samples and sorting the five
threshold values `{0, \mathrm{zero}(D_K), \mathrm{zero}(D_N),
\mathrm{zero}(L_1), \mathrm{zero}(\tilde N_2)}`, I found **17 distinct
orderings** realized (out of 120 possible permutations) — no universal
order exists. This rules out the simplest fixed-interval-chart proof
strategy; any Sturm-based argument must itself case-split on which ordering
holds (effectively a small CAD/cylindrical-algebraic-decomposition problem
in `(a,b,cc,u)`), which is a real obstacle, not a shortcut.

**Sign-pattern census of the three residual unknowns `(Y,B_2,Z)`.** The
above resultant factorizations show the ENTIRE joint-exclusion question
depends only on the (already known `F_1,F_2<0`) plus the signs of exactly
three explicit polynomials `Y(a,b,cc,u)`, `B_2(a,b,cc,u)`, `Z(a,b,cc,u)` —
a genuine reduction from "root-by-root case analysis" to "sign of finitely
many explicit polynomials," which is the right shape for a Sturm/discriminant
finite case split. However, an 8000-sample numeric census of
`(\mathrm{sign}(Y),\mathrm{sign}(B_2),\mathrm{sign}(Z))` found **7 of the 8
combinatorially possible sign patterns actually occur** (only
`(+,+,+)` was absent in this sample) — so this reduction, while real
progress in *kind*, does **not** collapse to a small number of cases; a full
proof via this route would need up to ~7 separate sub-case
verifications, each re-deriving the fine root-position facts (which root of
`G_2b` is which, its relation to the `s_2>0`/`L_1<0`/`\tilde N_2>0`
thresholds) within that sign regime. This is a large but *finite and
concrete* target — a legitimate next-round build item, not a dead end, but
should be scoped honestly as heavy (not a one-lemma closer).

### Cheap-kill candidates
None found this round beyond what's already certified (`F_1,F_2<0`,
`D_K(r_1)D_K(r_2)` same-sign-as-`D_N(r_1)D_N(r_2)`). No parity/pigeonhole
shortcut discovered that bypasses the `(Y,B_2,Z)` sign classification.

### Candidate technique(s)
- The genuine Sturm/root-isolation technique (interval sign charts) does
  **not** directly apply because there is no fixed threshold ordering (see
  above) — ruling this out as a "quick win," confirming the population's
  round-6 suspicion that this shared gap is structurally hard, not just
  under-explored.
- What DOES work, and is new this round: resultant-ratio cancellation
  (computing `Res(G_2b,f)/Res(G_2b,g)` for pairs of affine test functions
  `f,g` and checking whether the unknown leading-coefficient/`Y` factors
  cancel) — a genuinely different, more surgical use of resultants than
  the population's prior "compute one resultant, read its sign" pattern.
  This produced one new proved lemma (`D_K`/`D_N` both-roots-sign
  coincidence) with zero extra numerics, and cleanly isolates the exact
  three unknowns (`Y,B_2,Z`) blocking full closure.
- A full closure via this route would need either (a) a genuine sign
  classification of `Y,B_2,Z` as functions of `(a,b,cc,u)` on the valid
  domain (possibly via the same "single-crossing sinusoid" endpoint-value
  technique already used for `F_1,F_2` in §12, since `Y,B_2` are also
  expressible in Weierstrass form as trig-polynomial-like expressions after
  back-substitution), combined with (b) a genuine finite case-split (up to
  ~7 cases) tracking each case's actual `s_2>0`/`W>0`/containment
  conclusion — a real but bounded amount of remaining work.

### Knowledge-base entries to use
- Resultant theory / Cox–Little–O'Shea ideal-membership and resultant-value
  formulas (`Res(f,g)=\mathrm{lc}(f)^{\deg g}\prod g(r_i)`), already the
  population's main tool — reused here in ratio form.
- No new KB entry (Sturm sequences specifically) proved necessary; sympy's
  `sturm`/`count_roots` were not needed since `G_2b` is only degree 2 in
  `s_2` — all root-interval information is obtainable directly from
  resultants/Vieta, which is what the population has been doing all along.
  (I did not find a case where genuine Sturm-sequence machinery, as opposed
  to elementary quadratic-root algebra, would add power here — degree 2 in
  `s_2` is too low for Sturm sequences to be doing real work beyond IVT.)

### Analogous past problems (cruxes)
Per prior rounds' note (`crux_moves_documentation.md` — geometry cruxes not
yet extracted for this corpus), I did not find a genuinely analogous crux
for this specific "exclude the extraneous branch of a squared-cosine
elimination via joint sign/positivity conditions" sub-problem; it is a
purely algebraic byproduct of this problem's own coordinate setup, not a
recognizable olympiad crux pattern. None to report.

### Prior progress
See `results/imo-2026-02/current.md` round 6 summary: §12 (magnitude bound)
fully closed; §13 (G2b exclusion) has the true/supplementary-parity theorem
proved but the full 3-way exclusion open, backed only by 17,800+ samples
(0 counterexamples). This round's work sits entirely inside §13's open gap
and produces a strictly finer decomposition of it (see above), not a
closure.

### Dead ends (do not retry)
- **Fixed threshold-ordering / simple interval sign chart** (this round):
  refuted by direct sampling (17 distinct orderings among 5 thresholds over
  3000 samples) — do not attempt a "assume WLOG the thresholds are ordered
  as X<Y<Z<W" style argument without first proving the ordering is fixed,
  which it is not.
- (Inherited from round 6, still valid) single-lever `B_2`-sign alone
  cannot close the gap (confirmed structurally here too: `B_2`'s sign is
  one of three still-undetermined quantities, not decisive alone).

### Small-case / intuition notes
- Confirmed (numeric, 8000 samples) that `(sign Y, sign B_2, sign Z) =
  (+,+,+)` never occurred — worth checking in a future round whether this
  is a genuine forbidden pattern (would shave the case count from 8 to 7,
  or possibly indicate an algebraic dependency among `Y,B_2,Z` worth
  deriving symbolically, e.g. a resultant or discriminant relation between
  them) — flagged as a concrete, cheap next check (a `sympy.resultant` or
  `sympy.groebner` run on `{Y,B_2,Z}` as polynomials in `u` for fixed
  generic `a,b,cc}` to see if `(+,+,+)` is algebraically excluded).
- `(True,False,False)` [i.e. `Y>0,B_2<0,Z<0`] was by far the dominant
  pattern (6047/7983 ≈ 76%) — this is conjecture-level evidence (not
  proved) that this is the "generic" regime and might be worth proving
  first/separately as the majority case, leaving the other 6 rarer regimes
  as a secondary case-split.
