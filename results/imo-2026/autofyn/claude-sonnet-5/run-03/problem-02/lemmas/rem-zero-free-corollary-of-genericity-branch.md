## Lemma (Rem=0 — i.e. cross-ratio realness χ∈ℝ, i.e. A,K,L,Q concyclic — is
a formal, unconditional polynomial consequence of the branch G2a=G3a=0)

In the rotation parametrization (`A=(0,0)`, `B=(a,0)`, `C=(b,cc)`, free
angle `β`, `u=\tan(\beta/2)`, `K=B+t_1(-\cos\beta,\sin\beta)`,
`L=C+s_2R(\beta)(A-C)`, all as in
`lemmas/symbolic-genericity-certificate.md`), let `Q` be the fixed point
`Q=\dfrac{C\bar C-B\bar B}{2(\bar C-\bar B)}` (the reflection of `A` in the
perpendicular bisector of `MN`, `lemmas/amnq-concyclic-and-reduction.md`
Step 1), and let
$$\chi := \frac{L(K-Q)}{Q(K-L)}$$
(viewing `K,L,Q` as complex numbers; the cross ratio criterion for
`A,K,L,Q` concyclic-or-collinear, `A=0`,
`lemmas/cross-ratio-real-concyclic-criterion.md`). Let `T_2` be the
numerator (after clearing an explicitly nonvanishing real denominator) of
`\chi-\bar\chi` (a purely imaginary quantity, since `K,L,Q` have real
coordinates, so `T_2\in\mathbb Q[t_1,s_2,u,a,b,cc]` is a genuine real
polynomial and `\chi\in\mathbb R\iff T_2=0`). Then
$$T_2 \in \langle G_{2a},G_{3a}\rangle \subset \mathbb Q[t_1,s_2,u,a,b,cc]$$
(Gröbner-basis ideal membership, remainder `0`), and `T_2` is in **neither**
`\langle G_{2a}\rangle` nor `\langle G_{3a}\rangle` alone. Consequently: on
the branch `G_{2a}=G_{3a}=0` (the same branch on which
`lemmas/symbolic-genericity-certificate.md`'s central identity `OM=ON`
already holds unconditionally), `\chi` is automatically real — `A,K,L,Q`
are automatically concyclic (or collinear) — for every real, non-degenerate
triangle and every `(t_1,s_2,u)` on that branch, with no further sign,
positivity, or root-counting content needed.

## Proof
Direct Gröbner-basis ideal-membership computation: build `G_{2a},G_{3a}`
from the certified genericity-certificate construction, build `T_2` via
direct symbolic expansion of `\chi-\bar\chi` (real coordinates for `K,L`,
explicit complex `Q`), compute the reduced Gröbner basis of
`\langle G_{2a},G_{3a}\rangle` (grevlex order on `t_1,s_2,u,a,b,cc`), and
reduce `T_2` against it: remainder `0`. By the standard theory of Gröbner
bases as an ideal-membership decision procedure (Cox–Little–O'Shea,
*Ideals, Varieties, and Algorithms*, Ch. 2 — the same citation used for the
genericity certificate itself), this is a genuine polynomial identity
`T_2=q_1G_{2a}+q_2G_{3a}`, valid for every real `(t_1,s_2,u,a,b,cc)`, not
merely at sampled points.

## Independent verification
Independently rebuilt, in full, from scratch by the proof-reviewer (round
8), NOT reusing any polynomial or intermediate formula from the approach
file: (1) built `eq2,eq3` directly from the raw vector definitions and the
`cross_eq`-style squared-cosine construction of hypotheses 2 and 3
(own script, own choice of test vectors `V_1,\ldots,V_4`); (2) confirmed
`eq2` divisible exactly by `t_1^2` and `eq3` by `s_2^2`, with quotients
independent of `t_1`/`s_2` respectively (homogeneity, matching
`lemmas/homogeneity-decoupling-rotation-param.md`); (3) factored the
quotients and independently identified `G_{2a}` (degree 4 in `u`, degree 2
in `s_2`) and `G_{3a}` (degree 4 in `u`, degree 2 in `t_1`); (4) built the
central target `T` (numerator of `O\cdot(C-B)-(|C|^2-|B|^2)/4`) from an
independently-derived circumcenter (own Cramer's-rule computation) and
confirmed `T` reduces to `0` modulo the Gröbner basis of `\langle
G_{2a},G_{3a}\rangle` (18 generators, matching the certified genericity
certificate exactly — this independently re-confirms
`lemmas/symbolic-genericity-certificate.md` as a byproduct, using this
round's own `G_{2a},G_{3a}` rather than copying them); (5) built `\chi` and
`T_2` from scratch, using the own `K,L` and the fixed-point formula for
`Q`, with an independently-chosen denominator-clearing convention (own
`sympy.together`/`fraction`, not matching the file's exact intermediate `T_2`
term-for-term, but a legitimate numerator of the same rational function
`\chi-\bar\chi`); confirmed `T_2/i` is a genuine real polynomial (no
residual `I` dependence); (6) reduced this independently-derived `T_2`
against the (independently-derived) Gröbner basis of `\langle
G_{2a},G_{3a}\rangle`: **remainder `0`**, and confirmed nonzero remainder
modulo `\langle G_{2a}\rangle` alone or `\langle G_{3a}\rangle` alone. This
is a genuinely independent, from-scratch reproduction of the entire chain
(vector definitions → `eq2,eq3` → `G_{2a},G_{3a}` → `T` (re-confirming
genericity) → `\chi,T_2` → ideal membership), not a re-run of the builder's
code, and it confirms the claim exactly. No gap found.

## What this does NOT prove
This does **not** prove `OM=ON` for the actual geometric configuration: it
is conditional on the branch `G_{2a}=G_{3a}=0`, and proving the genuine
geometric solution (satisfying the true unsquared hypotheses and all
containment/betweenness conditions) actually lies on this branch, rather
than the extraneous `G_{2b}=G_{3b}=0` branch, is the population's
separate, still-open "branch selection" gap (see
`lemmas/symbolic-genericity-certificate.md`'s own "What this does NOT
prove", `lemmas/g2b-true-supplementary-parity.md`,
`lemmas/pointwise-branch-selection-criterion.md`). This lemma shows that
`fixed-point-concyclic`'s own remaining algebraic content collapses to
exactly this same shared bottleneck, no more and no less.

## Source
`results/imo-2026-02/approaches/fixed-point-concyclic.md` (round 8, §7).

## Status
Certified.
