## Status
certified (round 6)

## Statement (Lemma P1/P2, `coordinate-bash-resultant-boundary-pointwise.md` §6)
With the setup of `symbolic-genericity-certificate.md` (`A=(0,0),B=(a,0),
C=(b,cc)`, rotation parametrization of `K,L`), fix `β` in the valid range.
Let `V_1=L-B`, `V_2=d(\beta)`, `V_3=L-N`, `V_4=C-N`. A value `s_2>0` is the
value making `K,L` satisfy hypothesis 2 (`\angle LBK=\angle LNC`) **and**
`L\in\triangle BNC` **and** "`K` inside angle `LBA`" simultaneously if and
only if all of:
1. `(V_1\cdot V_2)^2|V_3|^2|V_4|^2=(V_3\cdot V_4)^2|V_1|^2|V_2|^2` (degree-4
   polynomial in `s_2`, the squared form of the unsquared hypothesis);
2. `\mathrm{sign}(V_1\cdot V_2)=\mathrm{sign}(V_3\cdot V_4)` (both nonzero;
   distinguishes the genuine angle equality from the spurious supplementary
   alternative introduced by squaring);
3. `L=C+s_2R(\beta)(A-C)\in\triangle BNC` (strictly);
4. `\mathrm{cross}(d(\beta),L-B)<0` (equivalent, given (3), to "K inside
   angle LBA" — by the already-certified reduction of
   `cross-product-sign-selection-G2a.md`).

A `σ`-mirror statement (Lemma P2) holds for `t_1`, hypothesis 3, `K\in
\triangle BMC`, and "L inside angle ACK", with the cross-product sign
convention in (4') flipped to `>0` (a genuine consequence of `σ` reversing
orientation at the level of this specific cross product, not an error).

## Proof
Condition (1) is exactly `\cos^2\angle(V_1,V_2)=\cos^2\angle(V_3,V_4)` after
clearing the positive norm-product denominators (each `V_i\ne0`: `V_2=d(
\beta)\ne0` always, `V_4=C-N=C/2\ne0` since `C\ne A`, `V_1,V_3\ne0` since
`L\ne B,N`, a standing non-degeneracy assumption). Since both angles lie in
`(0,\pi)` where `\cos` is injective up to sign, this is equivalent to
"`\angle(V_1,V_2)=\angle(V_3,V_4)`" (the genuine hypothesis) **or**
"`\angle(V_1,V_2)=\pi-\angle(V_3,V_4)`" (spurious), distinguished exactly by
whether `\mathrm{sign}(V_1\cdot V_2)=\mathrm{sign}(V_3\cdot V_4)` — condition
(2). Conditions (3),(4) are literally/by-certified-reduction the remaining
two hypotheses. `\blacksquare`

## Independent verification (proof-reviewer, round 6)
Reimplemented conditions (1)-(4) from scratch (own Python/numpy script, no
code reuse from the builder — built the degree-4 polynomial in `s_2`
directly from the affine-in-`s_2` vector definitions, extracted real roots
via `numpy.polynomial.polynomial.polyroots`, tested (2)-(4) via direct
coordinate computation, not via any resultant shortcut) on 277 independent
random (triangle, `β`) samples: **277/277 had exactly one root satisfying
all four conditions**, corroborating the population's central open
conjecture at a scale independent of and consistent with the builder's own
552-sample report. The logical proof of the equivalence itself (Lemma
P1/P2) is elementary and complete — no gap found.

## Reuse
An exact (non-numerical) translation of "genuine geometric solution" into a
single real variable, avoiding any reference to the `G_{2a}/G_{2b}`
polynomial factorization. Reusable by any future branch-selection attempt
wanting a factorization-free formulation. **Does NOT itself close branch
selection**: the claim "exactly one candidate survives (1)-(4), for every
triangle and every `β`" remains unproved symbolically (552+277 independent
numeric samples, 0 counterexamples, but no proof).
