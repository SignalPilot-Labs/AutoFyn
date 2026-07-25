## imo-2026-02

**Context recap.** The whole problem has, since round 8, been proved to collapse
(across every live "route" — coordinate-bash, fixed-point-concyclic, Ptolemy,
inversion, spiral-similarity) onto ONE shared residual gap: Case (b)'s
positivity target, expressed equivalently as `(\star)`:
`(1+\cos B)^2X_0(A,B)\ge\mathrm{RHS}(A,B)^2` on the exact domain
`\mathcal D`, or as `q_1<0\wedge r_0<0` on the narrower `P>0\wedge E<0`
sub-case, or as `\mathrm{Num}\ge0` in the Weierstrass `u=\tan(A/6)` frame.
Denominator positivity (`\mathrm{Den},\mathrm{den}_1,\mathrm{den}_2>0`) is
now **fully, unconditionally proved** (Theorem 1, round 12). All four
approaches below attack this ONE shared target via four genuinely different
mechanisms; none is a re-decomposition of another into sub-pieces.

---

coordinate-bash-resultant-boundary: advance
Target: the whole problem — prove `q_1<0\wedge r_0<0` on the residual
sub-case `P>0\wedge E<0` (equivalently, via round-8's certified structural
equivalence, this closes the shared gap for every live route).
Technique: Positivstellensatz / explicit nonnegative-combination search on
a now-fully-polynomial (radical-free) domain, in `(c,s,d,t)=(\cos A,\sin
A,\cos B,\sin B)` with `c^2+s^2=1,\ d^2+t^2=1,\ s,t>0,\ c\ge0`.
Skeleton:
  1. Recall the certified reduction chain (rounds 9-12): the whole problem
     reduces to `q_1<0\wedge r_0<0` on `\{P>0\wedge E<0\}`. — already
     certified, reuse verbatim.
  2. **New this round** (per `math-explorer-q1r0.md`): the exact
     4-inequality polynomial characterization of that residual domain:
     `\{G_0>0\}\cap\{E_{\text{num}}<0\}\cap\{c\ge2t^2-1\}\cap\{\mathrm{Num}<0\}`,
     where `G_0=ct(1-2d^2)-2sd^3` (`\iff X_0>d^2`), `c\ge2t^2-1` (`\iff
     B\le C`, an elementary `\cos`-monotonicity identity), and `\mathrm{Num}`
     is the explicit degree-8 polynomial in `(c,s,d,t)` from the explorer's
     report — **write this out as a formal theorem with a full symbolic
     derivation** (the explorer only spot-checked the `\mathrm{Num}<0}`
     equivalence at 2,000 samples plus an "exact array match" on 436,519
     domain-restricted points; the builder must upgrade this to an actual
     `sympy` symbolic identity — clear the denominator `2\sin^3C=2(sd+ct)^3`
     of `q^2(1-X_0)-p^2X_0$ and show the result equals `\mathrm{Num}` up to
     a manifestly-positive factor).
  3. **Main new task**: find an explicit nonnegative combination
     `-q_1=\lambda_1G_0+\lambda_2(-E_{\text{num}})+\lambda_3(c-2t^2+1)+
     \lambda_4(-\mathrm{Num})+\sigma`, `\lambda_i\ge0` polynomials (or SOS),
     `\sigma` SOS — and the analogous combination for `-r_0`. **Must include
     `\mathrm{Num}` as a generator with a nontrivial coefficient** — round
     12's small-integer-coefficient ansatz on `G_0,-E_{\text{num}}` alone
     failed precisely because `\mathrm{Num}<0` is NOT redundant (it alone
     shrinks the domain by `\approx25\times`, from `\approx18\%\to100\%`
     hit rate for `q_1,r_0<0`) — this is the explorer's key new insight and
     must drive the ansatz design, not be treated as optional bookkeeping.
  4. Exploit the shared-corner structure: `G_0`, `-E_{\text{num}}`,
     `\mathrm{Num}`, `q_1`, `r_0` are all numerically observed to vanish
     simultaneously at the same corner `(A^*,B^*)` (round 11's already-
     certified corner) — first check this symbolically (does the certified
     `G_{\mathrm{curve}}(A^*)=0` equation divide each of `G_0,-E_{\text{num}
     },\mathrm{Num},q_1,r_0` evaluated along some natural 1-parameter
     restriction?). If so, this pins the ansatz's multiplier degrees/
     structure (each `\lambda_i` should also vanish there), sharply cutting
     the search space versus a blind degree-8 Positivstellensatz search.
  5. Fallback if step 3/4 fails directly: restrict to a numeric SDP search
     (small integer-coefficient hand ansatz first per round-12's lesson
     that `cvxpy` has no MOSEK and is unreliable above minimal degree —
     see the sibling `-sos` explorer's report this round) on this smaller,
     now fully-explicit 4-generator system, which is a strictly easier SDP
     than the `-sos` route's degree-34 `\mathrm{Num}` target.
Key lemmas (claim + mechanism):
  - The domain characterization (Step 2) — because the transcendental
    conditions `\beta_1<\gamma`, `\gamma=B`, `\sin(A+3\beta_1)<0` each admit
    an exact polynomial equivalent via `\cos`-monotonicity (`\gamma=B` case)
    or squaring-is-iff given a proven sign precondition (`\mathrm{Num}<0`
    case, licensed because `p<0,q>0` is proven automatic on the domain).
  - `p<0,q>0` automatic on `\{G_0>0\}\cap\{E<0\}\cap\{B\le C\}` — because
    (per the explorer's 436,519-sample sweep, zero violations) the sign
    preconditions needed to license Step 4's squaring are implied by the
    other three domain conditions; this removes a layer of casework the
    outline previously worried about. **Not yet symbolically proved** —
    flag for the builder to attempt a direct algebraic implication, or
    accept as a large numeric sweep if a symbolic proof is out of reach in
    one round (state honestly which).
Open gaps: the domain-characterization equivalence (Step 2) needs upgrading
from spot-check to a full symbolic identity; the main Positivstellensatz
combination (Step 3) is entirely unproved — the round's central task.
Cases to cover: none beyond the domain's own case split (already reduced to
one unified 4-inequality system, no further casework needed if Step 2-3
succeed).
Watch out for: do not repeat round 12's mistake of searching a
`G_0,-E_{\text{num}}`-only ansatz — `\mathrm{Num}` must appear nontrivially.
Also do not conflate this residual sub-case's domain with the FULL Case (b)
domain used by the `-tangent`/`-tangent-twopoint`/`-sos` siblings — it is
the strictly narrower `P>0\wedge E<0` slice.

---

coordinate-bash-resultant-boundary-pointwise-tangent: revise
Target: the whole problem — prove `(\star)`:
`(1+\cos B)^2X_0(A,B)\ge\mathrm{RHS}(A,B)^2` on the full Case-(b) domain
`\mathcal D` (a strictly larger target than the sibling above's, and per
round-10's cross-pollination note, proving it alone finishes the whole
problem via this route without needing the `T\ge0`/`q_1,r_0` factorization
at all).
Technique: abandon the stuck `T_1+T_2` termwise split (`T_1` consistently
negative, no viable bound found in 3 rounds). **Reformulate `S=f^2-g^2` as
a genuine difference `f-g`**, `f:=(1+\cos B)\sqrt{X_0}\ge0`,
`g:=\mathrm{RHS}$, and prove `f\ge g` directly via monotonicity of `f-g` in
`B`, reducing to a boundary-curve evaluation that reconnects with the
`-tangent-twopoint` sibling's own partial result.
Skeleton:
  1. `X_0\ge0` and `\mathrm{RHS}>0` on `\mathcal D` — the first is already
     established (Case-(b) domain facts); the second remains numeric-only
     (margin `\approx0.315` per round 12) and **must be proved
     symbolically this round** (it licenses `f-g\ge0\iff S\ge0`, and is a
     precondition of the whole reformulation, not optional).
  2. Compute `\partial f/\partial B=-\sin B\sqrt{X_0}+\dfrac{(1+\cos B)}
     {2\sqrt{X_0}}\dfrac{\partial X_0}{\partial B}` (elementary, reuses the
     already-certified `\partial X_0/\partial B$ closed form,
     `lemmas/x0-partial-b-derivative.md`) and `\partial g/\partial B` (D2,
     already certified, `lemmas/rhs-partial-b-derivative-and-decomposition.md`).
  3. **New key step**: both `\partial f/\partial B<0` and `\partial g/
     \partial B<0` throughout `\mathcal D` (numerically confirmed this
     round, `0/129{,}609` violations) — so `\partial(f-g)/\partial B>0
     \iff|\partial g/\partial B|>|\partial f/\partial B|\iff(\partial g/
     \partial B)^2>(\partial f/\partial B)^2`, which is **radical-free**
     (unlike a direct symbolic simplification of `\partial f/\partial B-
     \partial g/\partial B$, confirmed by the explorer NOT to collapse
     under `sympy.trigsimp`) since `(\partial f/\partial B)^2` only involves
     `X_0` (polynomial/trig, no `\sqrt{\cdot}`), not `\sqrt{X_0}` itself.
     This squaring is licensed safely because both quantities are already
     known same-signed (negative) — it is a magnitude comparison, not a
     sign-recovery squaring, so it does not reintroduce the `T_1`-style
     cancellation problem. **This is the round's primary open computation**
     — attempt it in `sympy` directly.
  4. Given Step 3 closes: `f-g` is strictly increasing in `B` on `\mathcal
     D$ for each fixed `A`, so its minimum over the domain's `B`-range
     (fixed `A`) occurs at the domain's lower `B`-boundary, which is the
     **implicit curve** `\mathcal C=\{X_0(A,B)=\cos^2B\}` (established in
     round 12 — NOT the naive `B=\beta_0(A)` curve; watch out for this
     exact pitfall, per memory rule 25).
  5. On `\mathcal C`, `f-g` coincides (numerically confirmed exactly this
     round, matching to 4 significant figures at all sampled points) with
     the `-tangent-twopoint` sibling's already-partially-proved `D_1$ (from
     `lemmas/star-factorization-on-boundary-curve.md`). **Formally prove
     this coincidence symbolically** (substitute `X_0=\cos^2B` into
     `f-g=(1+\cos B)\sqrt{X_0}-\mathrm{RHS}` and into `D_1=(1+\cos B)\cos B
     -\mathrm{RHS}` — since `\sqrt{\cos^2B}=\cos B` on the relevant range
     where `\cos B>0`, this should be a one-line identity, not merely a
     numeric coincidence — do this exactly, not by sampling).
  6. Conclude `(\star)` on all of `\mathcal D`, contingent on `D_1\ge0` on
     `\mathcal C` (the sibling's own still-open concavity/unimodality
     sub-gap, `\approx90\%` numerically confirmed, not fully proved).
Key lemmas (claim + mechanism):
  - `(\partial g/\partial B)^2>(\partial f/\partial B)^2` on `\mathcal D` —
    because `\mathrm{RHS}` (via `X_0`'s certified derivative formula)
    decreases in `B` strictly faster in magnitude than `(1+\cos B)\sqrt{X_0}`
    does; the mechanism is a direct algebraic comparison of two closed-form
    polynomial/trig expressions, both already certified as building blocks.
  - `f-g|_{\mathcal C}=D_1` exactly — because `\sqrt{X_0}=\cos B` exactly
    on `\mathcal C` (given `\cos B>0`, true throughout `\mathcal D` since
    `B<\pi/2$, round 11), collapsing the definitions to the identical
    expression.
Open gaps: `\mathrm{RHS}>0` symbolic proof (Step 1); the magnitude
inequality (Step 3, the round's central new computation); the `f-g=D_1`
identity's formal symbolic confirmation (Step 5, currently numeric-only);
`D_1\ge0` on `\mathcal C` (inherited unproved gap from the sibling
`-tangent-twopoint`, unimodality/concavity).
Cases to cover: none beyond the domain's existing structure.
Watch out for: the lower `B`-boundary of `\mathcal D` is the *implicit*
curve `X_0=\cos^2B`, not `\beta_0(A)` (memory rule 25) — do not evaluate
the boundary case at the wrong curve. Also: `T_1$ alone is a confirmed dead
end (memory/round-12 finding) — do not have the builder retry bounding it
in isolation; this reformulation exists specifically to bypass that.

---

coordinate-bash-resultant-boundary-pointwise-sos: advance (lower priority
this round)
Target: the whole problem — prove `\mathrm{Num}\ge0` (equivalently
`(\star)`) in the Weierstrass `u=\tan(A/6)` frame, given Theorem 1's fully
proved denominator positivity.
Technique: Positivstellensatz/SOS on the semialgebraic domain
`\{u\in(0,2-\sqrt3),\ n_1>0,\ n_2>0,\ (\angle B\le\angle C)\}`.
Skeleton:
  1. Theorem 1 (denominators unconditionally positive) — already fully
     proved, reuse verbatim (`lemmas/star-weierstrass-denominators-
     positive.md`).
  2. **New this round (required before any further SDP attempt)**: encode
     `\angle B\le\angle C$ (i.e. `B\le(\pi-A)/2`) polynomially. Per this
     round's explorer, this needs `w:=\sqrt{1+u^2}` as an extra algebraic
     generator (since `\cos(A/2)$ is irrational in `u=\tan(A/6)` alone, `A/2
     =3\cdot(A/6)`, and `\cos t,\sin t=\pm1/w,\pm u/w`) — add the relation
     `w^2=1+u^2,\ w>0` to the polynomial system and re-derive the `B\le
     (\pi-A)/2` condition as a polynomial inequality in `(u,w,\cos B,\sin
     B)`.
  3. **Do NOT re-attempt the confirmed-infeasible 2-multiplier ansatz**
     `\mathrm{Num}=\sigma_0+\lambda_1n_1+\lambda_2n_2$ at minimal degree —
     this round's SDP explorer confirmed, via two independently-agreeing
     solvers (CLARABEL, SCS) with clean convergence (`t^*\approx-1.548$,
     well-conditioned after rescaling), that this exact ansatz is
     genuinely infeasible. Any further attempt must add at least the
     `u`-domain-bound multiplier `n_3=u(2-\sqrt3-u)` (`\iff\cos A\ge0`) and
     ideally the new `\angle B\le\angle C` generator from Step 2.
  4. **Fix the numerical-conditioning wall before re-attempting SDP**: the
     raw monomial basis on `u\in(0,0.268)` gives a `\sim10^8`-`10^9`
     coefficient dynamic range even after linear rescaling, which broke
     both solvers at the 3-multiplier / higher-degree attempts this round.
     Switch to a basis adapted to the true bounded interval — e.g.
     Chebyshev polynomials on `[0,2-\sqrt3]`, or a further rational
     re-parametrization `u=(2-\sqrt3)w/(1+w)`, `w\in(0,1)` — before
     re-running the SDP with 3 multipliers.
  5. If SDP tooling remains inadequate (no MOSEK in this sandbox, per two
     rounds' confirmation), fall back to a smaller-scale hand
     coefficient-matching ansatz on a *reduced-degree* sub-target first
     (e.g. verify the 3-multiplier Positivstellensatz form exists at all
     via a much lower-degree relaxation / restriction to one boundary
     slice of `A`, as a cheaper feasibility probe before committing to the
     full degree-34 search).
Key lemmas (claim + mechanism): none new proved this round; Step 2's
`w=\sqrt{1+u^2}` encoding is the one concrete new piece of machinery to
attempt, because it is the standard fix for "triple-angle rational in
tangent, but half-angle isn't" — a one-dimension-larger but still fully
algebraic extension.
Open gaps: `\mathrm{Num}\ge0` itself (unchanged, the central target); the
`\angle B\le\angle C` polynomial encoding (newly identified, not yet done);
whether a 3-multiplier certificate exists at all (currently unknown —
SDP attempts this round were inconclusive due to tooling, not refuted).
Cases to cover: none beyond the domain's existing structure.
Watch out for: the 2-multiplier ansatz is a **confirmed dead end** (two
solvers, clean convergence, `t^*<0`) — do not re-dispatch a builder to
search it again in any form (raw or hand ansatz) at these degrees. Given
this route has now spent 3+ rounds on the same gap with a fresh negative
result this round, weigh giving it a smaller build budget than the two
approaches above unless Step 2 (the `\angle B\le\angle C` encoding) shows
quick, concrete progress.

---

coordinate-bash-resultant-boundary-pointwise-tangent-twopoint: advance
(no build slot this round — deprioritized per explorer recommendation)
Target: unchanged — `(\star)` restricted to the boundary curve
`\mathcal C=\{X_0=\cos^2B\}$ via `S=D_1D_2`.
Rationale for no build slot: its own remaining gaps (`D_2>0`, `D_1`
concavity/unimodality) are real and well-scoped, but even fully closing
them only proves `(\star)` ON `\mathcal C` (measure zero), not on the full
domain `\mathcal D` — extending off the curve needs the sibling
`-tangent`'s monotonicity lever (Step 3/4 above), which is this round's
priority build target. If `-tangent`'s Step 5 (the `f-g|_{\mathcal C}=D_1`
identity) is confirmed this round, `-tangent-twopoint`'s open `D_1\ge0`
gap becomes IMMEDIATELY load-bearing for the whole problem (not just its
own file) — at that point it should be given a build slot next round
without further deliberation. Its certified lemma
(`lemmas/star-factorization-on-boundary-curve.md`) remains available for
`-tangent` to cite directly (Step 5 above), so no work is lost by skipping
a build this round.
Open gaps (unchanged): `D_2>0` on `\mathcal C` (unproved, numeric only);
`D_1$'s concavity/unimodality on `\mathcal C` (unproved, `\approx90\%`
numeric); the domain-extension dependency on the sibling (structural, not
this file's own gap).
Cases to cover: none new.
Watch out for: do not let this approach silently rot past next round if
`-tangent`'s Step 5 closes — revive immediately per memory rule 18's
precedent (a named, unexplored-this-round lever should not sit idle once
it becomes load-bearing elsewhere).

build set: coordinate-bash-resultant-boundary, coordinate-bash-resultant-boundary-pointwise-tangent, coordinate-bash-resultant-boundary-pointwise-sos
