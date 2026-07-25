## Status
partial

### Round 18 (this round) — the 3 dispatched diagnostic tests run; a real,
partial (not clean, not uniform) explanation found for a large chunk of the
"3 unexplained near-null directions," plus a clean negative result ruling
out the specific complex-conjugate-pair hypothesis flagged as the round-17
next step. Still no certificate; Status correctly stays `partial`.

**Setup.** Reused round 17's saved artifacts verbatim
(`/tmp/round-17/sos_work/polys_s.pkl`, `sstar.pkl` — the exact
`s^*=\mathrm{CRootOf}` and its 60-digit value) for witness 1
(`u=93/1000,\cos B=51/149,\sin B=140/149`), and round 15's saved
`/tmp/round-15/sos_work/polys.pkl` plus Theorem 4's `n4sq` formula for
witness 2 (`r=\tan(B/2)=1/2,u=7/100`, round 17's second witness point). All
three tests below were run at witness 1 (the primary target); test 1 was
additionally cross-checked at witness 2. Scripts saved under
`/tmp/round-18/sos_work/`.

**Test 1 — real roots of `n_2(s)` and `n4sq(s)` at the witness, and their
evaluation-vector's projection onto the near-null eigenspace.**

First, an important domain-structure correction found in the course of this
test: at witness 1, computing the domain-interior real roots of all three
generators shows `n_1`'s only domain root is `s^*\approx0.87468`, `n4sq`'s
only domain root is `s\approx1.16977`, and `n_2`'s only domain root is
`s\approx2.48213` — but a direct sign check across `s\in(0,3)` shows the
**true simultaneous-positivity domain (`n_1>0\wedge n_2>0\wedge n4sq>0`) is
`s\in(0.87468,1.16977)`**, i.e. the right endpoint of the actual domain is
`n4sq`'s root, not `n_2`'s (`n_2` stays positive there and only turns
negative much later, at `s\approx2.48213`, by which point `n4sq` is already
negative). This had not been explicitly stated in prior rounds' files.

With `E_5:=` the (numerically) 5-dimensional near-null eigenspace of the
order-2-constrained `M_0` (i.e. after `M_0z(s^*)=0,\,M_0z'(s^*)=0` as in
round 17), and the "explained" 2-dim subspace of `E_5` taken as the
orthonormalization of `E_5`'s projections of (normalized) `z(s^*),z'(s^*)`
(both `\approx100\%$ captured in `E_5`, confirmed), the **residual 3-dim
orthogonal complement of `E_5`** was tested against the (normalized)
evaluation vectors at the two OTHER generators' domain roots:
- `z(s\!=\!1.16977)` (`n4sq`'s root, the TRUE right boundary of the domain):
  `27.97\%` capture of the residual 3-dim complement (`91.29\%` of the full
  `E_5`).
- `z(s\!=\!2.48213)` (`n_2`'s root, numerically real but **outside** the
  true domain, since `n4sq<0` there): **`88.07\%$ capture of the residual
  3-dim complement** (`99.68\%$ of the full `E_5`) — a single direction
  explaining almost all of what was left unexplained.

This is a genuine, non-trivial finding — one real evaluation vector, at a
domain generator's real root (even though that root lies outside the actual
Case-(b) domain, since SOS positivity of `\sigma_0` is a global, not
domain-restricted, constraint), accounts for the large majority of the
previously "mystery" 3-dim residual. **However, cross-checking at witness 2
breaks the clean pattern**: at witness 2, the near-null cluster is only
3-dimensional (matching round 17's count there) and — a new finding this
round — `z'(s^*)$ is only `32.35\%$ captured by it (not `\approx100\%$ as at
witness 1; round 17 only tested `z(s^*)$'s capture at witness 2, not
`z'(s^*)$'s, so this is new information, not a contradiction of a prior
claim). Using the same "explained via `z(s^*),z'(s^*)$" projection
(imperfect here, since `z'(s^*)$ itself is poorly captured), the residual
complement is captured **`76.2\%$ by `z(n4sq\text{-root}=2.1785)$** and
essentially `0\%$ (`0.005\%$) by `z(n_2\text{-root}=0.7989)$ — the
**opposite** generator from witness 1's dominant direction. **Honest
conclusion: Test 1 finds a real, large, single-direction capture of the
residual near-null space by one of the two "other" domain generators' root
evaluation vectors, but WHICH generator's root dominates is not consistent
between the two witnesses tested — this is genuine partial progress
(rules out "no explanation exists"), not a clean uniform mechanism, and the
witness-2 measurement is itself less reliable since `z'(s^*)$'s own capture
is not near-total there.**

**Test 2 — `\sigma_0`'s full root list, searching for a near-double
complex-conjugate pair.** Reconstructed the degree-34 polynomial
`\sigma_0(s)$ from the order-2-constrained optimal `M_0$ (round 17's
`M_0z(s^*)=0,M_0z'(s^*)=0$ solve, re-run this round with `\texttt{SCS}$,
`\mathrm{eps}=10^{-12}`), and computed all 34 roots via `numpy.roots` on the
reconstructed coefficient vector. Sorting by `|\mathrm{Im}|`, the two
smallest-imaginary-part conjugate pairs found are
$$0.87441257\pm0.00026278i\quad\text{and}\quad0.87493796\pm0.00026261i,$$
both **immediately adjacent to `s^*\approx0.874675`** — their real parts
average to `0.874675265`, matching `s^*` to 6 significant figures — with
imaginary parts `\approx2.6\times10^{-4}$, **two full orders of magnitude
smaller than the next-smallest-imaginary-part root pair found**
(`-1.12064\pm0.17318i`, `1.19011\pm0.18894i`, both `|\mathrm{Im}|\approx0.17$
–`0.19`). **Interpretation, stated as a diagnosis, not a proof:** this
strongly suggests `\sigma_0$ has an (approximate) 4th-order zero exactly at
`s^*$ — i.e. the numerical solver, forced to make `\sigma_0$ vanish to
2nd order there (round 17's constraint), is finding it advantageous or
natural to push the vanishing to 4th order (splitting, at finite solver
precision, into two nearby complex-conjugate pairs rather than resolving
cleanly to a single real 4-fold root) — **not** a signature of an
independent, structurally distinct near-double root explaining new
directions elsewhere. **Explicit negative result, as flagged as the
concrete next step by round 17's own Net Assessment**: no other
comparably-small-imaginary-part conjugate pair was found anywhere in the 34
roots — the specific "second, independent near-double complex-conjugate
root pair explaining 2 more real dimensions" hypothesis floated in round 17
is **checked and not confirmed** at this witness point. This rules out that
specific mechanism as the explanation for the residual directions and
should not be re-tried blind in a future round.

**Test 3 — `M_0z''(s^*)=0$ as a third-order pinning constraint.** Added
`M_0z''(s^*)=0$ (18 more scalar equalities, using the exact 60-digit
`s^*$) as a third explicit linear constraint alongside `M_0z(s^*)=0` and
`M_0z'(s^*)=0`, re-solved (SCS, `\mathrm{eps}=10^{-8}$, needed since
CLARABEL failed outright and tight-tolerance SCS did not converge in the
time budget): **`\mathrm{status}=\mathrm{optimal}`, `t^*\approx7.815546080`
(matches the unconstrained baseline to 8 significant figures)**, with all
three residuals driven small (`\|M_0z(s^*)\|\approx6\times10^{-11}`,
`\|M_0z'(s^*)\|\approx3\times10^{-10}`, `\|M_0z''(s^*)\|\approx3\times
10^{-9}`) — **genuinely feasible, essentially free**, directly corroborating
Test 2's 4th-order-tangency diagnosis. **But this does NOT relieve the
degeneracy**: the near-null eigenvalue cluster **grows from 5 to 6**
(`\approx-1.8\times10^{-7},-1.1\times10^{-8},-2.7\times10^{-12},-1.7\times
10^{-14},9.3\times10^{-12},2.9\times10^{-7}`, gap to `3.2\times10^{-4}`) —
i.e. of the new 6-dim near-null space, exactly 3 are now explained
(`z,z',z''` at `s^*`, each `\approx100\%$ captured) and **exactly 3 remain
unexplained, the same count as before** — pinning the 3rd-order direction
does not shrink the residual, it just adds one more (now-explained)
dimension to keep pace. Re-testing Test 1's two directions against this new
6-dim space: `z(n_2\text{-root})$'s capture of the (now 3-dim, redefined)
residual complement drops to `60.7\%$ (`99.8\%$ of the full 6-dim space);
`z(n4sq\text{-root})$'s drops to `5.9\%$ (`98.9\%$ of the full 6-dim
space) — both still substantial but smaller shares of a differently-defined
residual, underscoring that "5 (or 6) near-null directions split into a
clean, additive list of independently-meaningful pieces" is not quite
right; there is overlap/redundancy between the explained and
Test-1-implicated directions that a purely numerical projection cannot
fully disentangle. **A parallel experiment pinning `M_0z(s_{n_2})=0`
(Test 1's dominant direction) as the 3rd constraint instead of `z''(s^*)`**
was also run: feasible, `t^*$ essentially unchanged, but the observed
near-null eigenvalue count rose to 7, several at `\lesssim10^{-13}$–
`10^{-15}$ magnitude — **below solver/floating-point precision**, so this
specific sub-result is reported as inconclusive noise, not a reliable count,
per this file's own standing practice (round 17) of not treating
near-machine-epsilon solver output as decisive.

**Net assessment (honest, per the round's own dispatch not to overclaim).**
All 5 near-null directions are **not** fully and cleanly accounted for this
round, but real, partial structural insight was gained: (a) a substantial
share of the residual (beyond the already-known `z(s^*),z'(s^*)$ pair) is
explained, at least at one witness point, by a single further evaluation
vector at a domain-generator's real root (`88\%$ of the residual at witness
1, via `n_2`'s root, which lies just outside the true domain) — genuine
progress, but not reproduced identically at witness 2 (there it is
`n4sq`'s root instead, at `76\%$, and the baseline `z'(s^*)$ capture itself
is markedly weaker); (b) independently, `\sigma_0$ appears (via two
convergent pieces of evidence — the σ0-root near-double-pair test and the
explicit, cheap `M_0z''(s^*)=0$ feasibility test) to vanish to (at least)
4th order at `s^*` itself, not merely 2nd order — a clean, mutually
corroborating finding, though it does not by itself shrink the residual
count; (c) the specific "second independent complex-conjugate near-double
root elsewhere" hypothesis flagged by round 17 is checked and **ruled out**
at this witness — a genuine negative result narrowing the search space for
future rounds. **No exact SOS certificate was found or attempted to be
extracted this round; this remains purely diagnostic.** Status stays
`partial`. Recommended next step (not taken this round, given the
time budget): since Test 1's dominant direction differs between the two
witnesses (n2's root vs n4sq's root), a future round should check whether
BOTH directions together (as a joint 2-dimensional "explained-beyond-`s^*`"
subspace, tested against the residual complement jointly rather than
one at a time) close the gap more uniformly across witnesses — this was not
attempted here due to time constraints and is flagged as the concrete next
diagnostic, not claimed as done.

**Round 18 promotable lemmas: none.** All findings this round are numeric
SDP/root-finding diagnostics (however precise or cross-checked), explicitly
not certifiable as lemmas per CLAUDE.md's rigor rules — no proof was
produced. One reusable domain-structure fact worth flagging for future
rounds (not yet promoted to a certified lemma, but elementary and easy to
verify if needed): at witness 1, the true Case-(b) domain's right endpoint
is `n4sq`'s root (`s\approx1.16977`), not `n_2`'s root — `n_2` remains
positive well beyond it.

### Round 17 (this round) — the complementary-slackness mechanism confirmed
by an EXPLICIT constrained SDP (not merely diagnosed post hoc), and
independently reproduced at a genuinely different second witness point;
still not an exact certificate, and the 3-of-5 unexplained near-null
directions remain unresolved even after building in the explained 2.

**Setup.** Reused round 16's exact rational witness `(cos B,\sin B)=
(51/149,140/149)` and its saved artifacts (`/tmp/round-16/exact_point_data.pkl`,
own re-derivation cross-checked against it) and round 15's fully symbolic
`(u,\cos B,\sin B)`-parametrized `\mathrm{Num},n_1,n_2` (`/tmp/round-15/sos_work/polys.pkl`,
combined with Theorem 4's `n4sq` formula), enabling a genuine second-witness
check this round (not available as a saved artifact before).

**Step 1 — exact algebraic isolation of `s^*` (upgrade from "numerically
matches to 5-6 digits" to a genuine exact algebraic number).** With the
same affine rescaling `u=s/10` used throughout this file, `n_1(s)` is an
exact degree-10 polynomial over `\mathbb Q(\sqrt3)`. Using
`sympy.Poly(n_1,s,\text{extension}=\sqrt3)` and `sympy.real\_roots`, found
**all 6 real roots exactly** (`\approx-114.33,-25.43,-2.68,0.87468,3.93,
37.32`), confirming round 16's numeric finding that the unique real root in
the domain window `s\in(0,2.679)` is
`$s^*\approx0.874675269599096869489546969896100552029\ldots$` — this root,
returned by `sympy` as an exact `\mathrm{CRootOf}` object of a degree-16
polynomial over `\mathbb Q$ (the minimal polynomial of the `\mathbb Q(\sqrt3)`
root over `\mathbb Q$ itself, degree `\le2\times10=20$, sympy's normalization
found the exact minimal one, degree 16), is a **bona fide exact algebraic
number**, not a float — the prerequisite the round's dispatch asked for.
Sign check confirms `n_1<0` for `s<s^*`, `n_1>0` for `s>s^*` (matches round
16's finding: `s^*` is exactly the lower edge of the true `u`-domain at
this `B`).

**Step 2 — the constrained SDP: `M_0z(s^*)=0` built in explicitly, not
discovered post hoc.** Using a 60-digit numeric evaluation of the exact
`s^*` (via `sympy.Float(s^*,60)`) to build `z(s^*)=(1,s^*,\ldots,{s^*}^{17})$
and `z'(s^*)=(0,1,2s^*,\ldots,17{s^*}^{16})` as high-precision floats, added
`M_0\cdot z(s^*)=0` (18 scalar linear equalities on the Gram-matrix entries)
as an EXPLICIT extra constraint to the identical (17,12,14,14)-half-degree
3-generator SDP (maximize `t`), re-solved with CLARABEL:
- **Result: still `status=optimal`, `t^*\approx7.8155461` — essentially
  unchanged from the unconstrained baseline (`t^*\approx7.8155461` there
  too, matching to 7 significant figures)**, and the residual
  `\|M_0z(s^*)\|` **drops from `\approx3.9\times10^{-5}$ (unconstrained
  baseline, i.e. this was already nearly true at the numeric optimum) to
  `\approx1.2\times10^{-9}$** (now exactly enforced). This is a genuine,
  non-trivial confirmation: forcing the vanishing condition costs
  essentially nothing in slack, exactly as complementary slackness
  predicts for a constraint that is already active at the true optimum —
  **not** a case of the SDP "fighting" the constraint (which would show up
  as a materially reduced `t^*`).
- The Gram matrix `M_0`'s eigenvalue spectrum after this constraint is
  qualitatively unchanged from the unconstrained case: still `3` eigenvalues
  at `\lesssim10^{-7}$ magnitude (`\approx-4\times10^{-8},\ 0,\ 6\times
  10^{-7}`) before a clear gap to `\approx7\times10^{-4}`. **Explicitly
  building in the single vanishing condition does not, by itself, remove
  the rank deficiency** — consistent with the file's prior finding that
  `\sigma_0`'s null space is genuinely `\ge2`-dimensional at this witness
  (round 16's `4$–`5` near-null eigenvalues), of which the `z(s^*)$
  direction is only one (or two, counting the derivative direction below).

**Step 3 — forcing full order-2 vanishing (`M_0z(s^*)=0` AND
`M_0z'(s^*)=0`): feasible, but does not reach a genuinely well-conditioned
matrix, and shows solver-precision-level ambiguity that must be reported
honestly.** Adding both constraints (36 scalar equalities total, some
linearly dependent) and re-solving:
- CLARABEL: `status=optimal\_inaccurate`, `t^*\approx7.8155488$ (matches
  the unconstrained value to 5 sig figs); a margin-maximization
  reformulation (fix `t=7.8155$, maximize the joint minimum-eigenvalue
  margin `\lambda` across `M_0,\ldots,M_3`, as round 16's own robustness
  check) gives `\lambda^*\approx-2.7\times10^{-5}` (CLARABEL,
  `optimal\_inaccurate`) versus `\lambda^*\approx+5.6\times10^{-6}` (SCS,
  clean `optimal`) — **the two solvers disagree on the SIGN of the margin,
  both at the `10^{-5}$–`10^{-6}$ scale**, i.e. genuinely at the numerical
  noise floor, not a decisive result either way. Per this file's own prior
  practice (round 14's "solver disagreement near 0 is inconclusive, not
  evidence of infeasibility"), **this is reported honestly as
  inconclusive, not as a proof the order-2-constrained problem is
  feasible or infeasible** — it does *not* show the "decisively,
  non-marginally infeasible" signature (`\lambda^*\approx-0.5`) that round
  16's rank-13-truncation attempt showed; it is consistent with the
  constrained problem sitting right at the same PSD boundary as the
  unconstrained one, no better and no (decisively) worse.
- A tighter SCS run (`eps=10^{-12}`, `\text{max\_iters}=5\times10^5`) on
  the maximize-`t` (not margin) formulation converges to `status=
  optimal\_inaccurate`, `t^*\approx7.8155461` (again matching), with
  **residuals `\|M_0z(s^*)\|\approx5.5\times10^{-12}`,
  `\|M_0z'(s^*)\|\approx2.7\times10^{-11}`** (both constraints satisfied
  to near machine precision) and reconstruction residual (`\sigma_0+
  \lambda_1n_1+\lambda_2n_2+\lambda_3n4sq` vs. `\mathrm{Num}-t^*`) of only
  `6.1\times10^{-11}` across all 35 coefficients — an excellent numerical
  fit. **But the resulting `M_0` eigenvalue spectrum still shows exactly
  5 eigenvalues clustered at `\lesssim1.5\times10^{-8}$** (both signs:
  `-1.5\times10^{-8},\ -3\times10^{-12},\ 2\times10^{-13},\ 8\times
  10^{-13},\ 1.3\times10^{-8}`), then a clean, comfortable gap to
  `1.97\times10^{-3}$ and beyond — **the same "4-5 near-null dimensions"
  degeneracy round 16 found, unchanged in count even after this round
  explicitly pins 2 of them to the exact `z(s^*),z'(s^*)$ directions.**
  This is the round's central honest negative finding for the
  "constructive extraction" goal: **building in the explained
  complementary-slackness vanishing does not relieve the degeneracy or
  reduce it to a well-conditioned, exact-extractable rank** — 3 further
  near-null directions persist, exactly as flagged as an open risk by
  this round's own outline. (An attempt to identify these 3 directions by
  inspecting the near-degenerate eigenvectors' polynomial roots was made
  but is **inconclusive by construction**: since the 5 eigenvalues are
  themselves numerically near-degenerate with each other, `numpy`'s
  eigensolver returns an essentially arbitrary orthonormal basis of the
  5-dimensional near-null eigenspace, not a canonically meaningful
  individual eigenvector — no attempt is made to over-interpret the
  specific root locations found this way.)

**Step 4 — cross-witness-point confirmation (new this round, explicitly
requested as a "cheap next check" by both the outline and the
outline-reviewer, previously untested).** Built a **second, independent
exact rational witness point**, reusing round 15's fully symbolic
`(u,\cos B,\sin B)`-parametrized `\mathrm{Num},n_1,n_2$
(`/tmp/round-15/sos_work/polys.pkl`) plus Theorem 4's `n4sq$ formula (not
merely re-evaluating the same saved point): `r=\tan(B/2)=1/2$ gives
`(\cos B,\sin B)=(3/5,4/5)`, `B\approx0.9273$ (genuinely different `B`-slice
from round 16's `B\approx1.287`); scanning small-denominator `u$ for
Case-(b) domain membership found `u=7/100$ works (`n_1\approx0.0178,
n_2\approx0.0291, n4sq\approx0.3214, \mathrm{Num}\approx0.6837`, all
positive as required). Re-ran the identical (unconstrained) 3-generator SDP
at this point: `t^*\approx0.4480` (CLARABEL, `optimal\_inaccurate`), with a
`3`-dimensional near-null cluster in `M_0` (`\approx-2.9\times10^{-8},
2.4\times10^{-9},6.8\times10^{-7}`, gap to `7.4\times10^{-4}`, a smaller
degeneracy count than the first witness's `5`, but still genuinely
present). Independently solved `n_1(s)=0` exactly at this new point and
found its unique domain-interior real root
`s^*_2\approx0.687048156396019582864\ldots` — **projecting the (normalized)
exact evaluation vector `z(s^*_2)` onto the (numerically found) 5
lowest-eigenvalue eigenspace of this second `M_0` captures
`99.99999999887\%$ of its norm** — matching the first witness's finding
(`99.9999999996\%`) closely. **This is a genuine, independently-verified
confirmation that the "σ0 forced to vanish at the exact root of the active
domain generator `n_1`" mechanism is not an artifact of the one previously
studied witness point — it recurs, essentially identically, at a second,
structurally unrelated `B`-value.** This substantially strengthens the
round-16/17 diagnosis from "true at one point" to "a structural feature of
this 3-generator ansatz across the domain," though it remains a
finite-sample (2-point) numerical finding, not a proof that it holds at
every `(cos B,\sin B)`.

**Net assessment.** Genuine progress of the diagnostic, not constructive,
kind, exactly as the round's dispatch anticipated as the likely outcome:
(a) `s^*` is now an exact, `sympy`-certified algebraic number (a `CRootOf`
of an explicit degree-16 rational polynomial), not merely a 5-6-digit
numeric match; (b) an **explicit** constrained SDP with `M_0z(s^*)=0` built
in as a hard linear equality confirms the complementary-slackness
prediction cleanly (feasible, `t^*` essentially unchanged, residual driven
to `\approx10^{-9}$) rather than merely observing it post hoc in the
unconstrained optimum; (c) adding the derivative direction (order-2
vanishing) remains feasible at essentially the same `t^*$ with excellent
polynomial-identity residuals (`\approx6\times10^{-11}`), but — the
round's key honest negative finding — **does not remove or reduce the
rank deficiency**: `M_0` still carries exactly 5 near-zero eigenvalues, of
which only 2 are now explained, the other 3 unchanged and still
unexplained; (d) the whole "σ0 vanishes where `n_1=0`" mechanism is
**independently reproduced at a second, genuinely different witness
point** (a check flagged as untested and cheap by both this round's
outliner and reviewer), closing that specific open item. **No exact
rational (or exact-algebraic) SOS certificate was extracted this round** —
the near-null eigenspace, even after 2 of its ~5 directions are pinned to
an exact algebraic locus, remains too close to singular for a
round-and-project extraction to succeed without further structural
insight into the other 3 directions (candidates for future investigation,
not resolved here: a genuine near-double COMPLEX-conjugate root pair of
`\sigma_0`, per round 16's root list of `\sigma_0`'s 34 roots, none of
whose imaginary parts were flagged as small enough to explain 3 more real
dimensions — this specific candidate was NOT checked against the 3
residual directions this round and is flagged as the concrete next step).

**Round 17 promotable lemmas: none.** All of this round's findings are
either (a) numeric SDP evidence (however high-precision or cross-checked)
— explicitly not certifiable as a lemma per `CLAUDE.md`'s rigor rules,
since it is not a proof — or (b) a single exact algebraic fact (`s^*` is
the `\mathrm{CRootOf}` of an explicit degree-16 rational polynomial, the
unique domain-interior real root of `n_1(s)`) that is tied to one specific
fixed witness point's `\lambda_i`-optimizing SDP output, not a
general-purpose reusable statement about the original geometry problem.
Recorded here for completeness rather than under a separate heading.

### Round 16 — exact rational witness point built and the
numeric SDP reproduced there cleanly, but exact Gram-matrix extraction hits
a genuine new obstruction: the optimal `σ₀` Gram matrix is forced to sit
essentially exactly on the PSD boundary, independent of the slack `t`.
Sub-goal B (joint multivariate ansatz) not attempted, deferred honestly.

**Step 0 — a necessary correction to the round-15 outline's own premise.**
The outline's dispatched witness point `(A,B)≈(0.603,1.269)` is a *float*
approximation; `A=0.603`, `B=1.269` are not themselves algebraic numbers of
bounded degree in any useful sense (they're arbitrary decimals), so
`u=\tan(A/6)`, `\cos B`, `\sin B` at that literal point are transcendental,
and "exact Gram-matrix extraction" at that literal point is not a
well-posed target (there is no finite-degree number field for `sympy` to
certify positivity in). **Fix (this round):** replaced the float witness
with a genuine **algebraic, rational witness point** close to it, reusing
the same trick round 14's Theorem 3 already certified for a different
purpose (an exact rational counterexample point) — parametrize
`(\cos B,\sin B)` via a rational point on the unit circle,
`\cos B=\frac{1-r^2}{1+r^2}`, `\sin B=\frac{2r}{1+r^2}` for `r=\tan(B/2)\in
\mathbb Q`, and pick `u\in\mathbb Q` directly. Choosing `r=7/10` gives the
Pythagorean-triple point `(\cos B,\sin B)=(51/149,140/149)` (`B\approx
1.28700`, close to `1.269`), and scanning small-denominator `u` near
`\tan(0.603/6)\approx0.1008` for genuine Case-(b) domain membership
(`n_1,n_2,n4sq,\mathrm{Num}` all `>0`, checked by exact `sympy.Rational`
substitution into the certified Theorem-1/4 polynomials) found
`u=93/1000` works, with comfortable margins:
`n_1=0.0667$, `n_2=0.5834`, `n4sq=0.0428`, `\mathrm{Num}=8.560` (all exact
rationals, floats shown for readability). This point is a genuine Case-(b)
domain member and close to the previously-hardest-known float point, so it
is a faithful stand-in for it, but now every target coefficient in the
resulting univariate-in-`u` polynomials `\mathrm{Num},n_1,n_2,n4sq` is an
**exact rational number**, not a float or a transcendental — the
prerequisite for any exact SOS-certificate claim. (Methodological note for
future rounds: **any** future "exact certificate at a witness point" attempt
must use a rational, or at worst `\mathbb Q(\sqrt3)`, witness point
constructed this way — a literal decimal `(A,B)` float point is not exact-
certifiable, full stop.)

**Step 1 — numeric SDP reproduced cleanly at the exact point.** Re-ran the
identical (17,12,14,14)-half-degree 3-generator ansatz (round 15's own
`sdp_solve4.py`/`build_polys.py` machinery, reused verbatim, only the
witness substitution changed to the new exact rational point, with an
`s=u/10` affine rescaling — not the domain-boundary rescaling of round 15,
since exactness no longer needs a shared-domain rescale, just conditioning)
at `(u,\cos B,\sin B)=(93/1000,\,51/149,\,140/149)`: both CLARABEL
(`optimal`) and SCS (`optimal_inaccurate`, expected at this precision)
converge to `t^*\approx7.8155461`, matching round 15's float-point result at
the "same" location almost exactly (round 15 reported `t^*\approx8.507976`
at the float point `(0.603,1.269)` itself — the new point is intentionally
not identical, chosen slightly toward the interior of the `n4sq`-tight
region to keep all four generators comfortably strictly positive, hence the
close but not identical slack). Confirms round 15's numeric finding is
reproducible at a genuinely exact-arithmetic-amenable point, not an
artifact of the specific float location.

**Step 2 — round-and-project fails, and a genuine new degeneracy is found
and pinned down precisely (the round's main finding).** Attempted the
outline's prescribed method: round each Gram matrix entry to a nearby
rational (denominator `10^7`–`10^8`), compute the exact linear defect
against the exact rational target (`\mathrm{Num},n_1,n_2,n4sq` are now
exact, so this defect is itself an exact rational number, computed via
`sympy` — no float residual ambiguity), and solve for a minimal exact
correction. **The correction step is where this breaks down, and not for a
superficial reason:**

1. A first attempt (uniform shim `+\varepsilon I` added to each Gram matrix
   before rounding, to buy PSD margin, then a sparse single-entry — later a
   min-Frobenius-norm — correction to hit the exact target) reliably
   produced a *small but genuine* negative eigenvalue in the corrected
   `\sigma_0` matrix (`\approx-3.6\times10^{-7}` to `-1.2\times10^{-2}$
   depending on shim size) — **not** shrinking to `0` as the shim size was
   reduced in the natural way, which is the signature of correcting *away*
   a self-inflicted defect rather than absorbing genuine rounding noise:
   the uniform shim `\varepsilon I` contributes `+\varepsilon` to *every
   even-degree* coefficient of the reconstructed polynomial (since `(v_i
   v_i^T)`'s antidiagonal sum for the identity matrix hits exactly the
   even degrees `2i`), but only the **single** degree-`0` coefficient can be
   compensated by adjusting the slack `t` — so matching the *exact* target
   forces the correction step to remove almost the entire artificial shim
   again at every other even degree, defeating its purpose.
2. Removing the artificial shim (eigen-clip only, no added margin) and
   isolating the *only* genuine sources of residual — rational-rounding
   truncation (`\lesssim10^{-7}` per matrix entry) and the necessary choice
   `t_{\mathrm{exact}}<t^*` (chosen to `10^{-5}$ precision, so the residual
   this introduces is `\lesssim10^{-5}`, confined to degree `0`) — gives a
   *much smaller* total defect (`\lesssim1.6\times10^{-5}`, matching the
   expected scale) but **still** produces a small negative eigenvalue after
   the sparse correction (`\approx-3.6\times10^{-7}`), because `\sigma_0`'s
   Gram matrix has **4–5 eigenvalues at `\approx10^{-7}$–`10^{-11}`, i.e.
   essentially exactly `0`, with a real spectral gap to the next eigenvalue
   (`\approx0.0139`)** — so *any* nonzero correction with even a tiny
   component along those directions (unavoidable for a correction concentrated
   at specific matrix entries, which are not eigen-aligned) pushes them
   negative.
3. **Decisive diagnostic (this round's key new finding): this
   near-zero-eigenvalue degeneracy of `\sigma_0` is intrinsic to the
   ansatz/witness-point pair, not an artifact of maximizing `t`.** Re-solved
   the SDP with a completely different objective — fix `t=t_{\mathrm{exact}}`
   at a chosen value and **maximize the joint minimum eigenvalue margin**
   `\lambda` across all four Gram matrices simultaneously (`M_0\succeq
   \lambda I,\ldots,M_3\succeq\lambda I`, maximize `\lambda`) — at
   `t_{\mathrm{exact}}=7.81553$ (essentially `t^*`): best achievable margin
   `\lambda^*\approx-3.5\times10^{-7}$ (i.e. `0` to solver precision). **Then
   repeated at `t_{\mathrm{exact}}=7,5,2,0`** (sacrificing up to the *entire*
   slack `t^*\approx7.816`, an enormous giveback far beyond any plausible
   rounding need): `\lambda^*\approx-1.79\times10^{-8}`,
   `-1.79\times10^{-8}`, `-1.74\times10^{-8}`, `-1.95\times10^{-8}$
   respectively — **the achievable margin stays pinned at essentially exactly
   `0` regardless of how much slack is sacrificed.** This rules out "the
   slack is being spent on `t` instead of margin" as the explanation; the
   degeneracy is a property of the polynomial shape itself (`\mathrm{Num},
   n_1,n_2,n4sq` at this witness point, and this exact ansatz degree split)
   — most plausibly a genuine near-double real root of the residual
   polynomial (`\sigma_0` is forced toward `0` at some real `s_0`, since a
   real root of an SOS polynomial forces the corresponding evaluation vector
   `(1,s_0,\ldots,s_0^{17})` into the Gram matrix's null space) — not a
   solver-tolerance artifact of the maximize-`t` objective.
4. **A rank-reduction attempt (per the outline's own diagnostic-first
   suggestion) was tried and gives a clean, informative negative result.**
   Built `\sigma_0` explicitly as `\sigma_0=Q^TQ$ with `Q$ a `13\times18`
   **exact rational** matrix (rounded from the top-13 eigenpairs of the
   numeric `M_0`, discarding the `5` near-zero ones) — this is **automatically
   and unconditionally exactly PSD** (a Gram matrix of real rational vectors
   needs no PSD verification at all, only the rounding arithmetic is exact,
   which `sympy.Rational` guarantees) — genuinely achieving the outline's
   "explicit small SOS, easier to verify" goal for `\sigma_0` alone. But
   feeding the resulting *exact* residual target (`\mathrm{Num}-t_{
   \mathrm{exact}}-c_0`, all `35` coefficients, exact rational) to a fresh
   joint-margin SDP over `\lambda_1,\lambda_2,\lambda_3` alone (now with
   `\sigma_0` fixed, not part of the margin optimization) returns
   **`\lambda^*\approx-0.511`, a decisively, non-marginally infeasible
   result** (`\lambda_1,\lambda_2,\lambda_3` reach eigenvalues near `-0.51`
   at the optimum, not merely `\approx0`): discarding even this small a
   sliver of `\sigma_0$'s spectrum (`5$ of `18` eigenvalues, all individually
   `<10^{-6}`) removes something the other three generators cannot come
   close to replacing (the residual target's magnitude jumps to `\approx33`,
   comparable to `\mathrm{Num}`'s own scale, from the sub-`10^{-5}` residual
   the full-rank `\sigma_0` leaves) — **so the near-zero eigenvalues of
   `\sigma_0`, individually tiny, are collectively load-bearing for matching
   the polynomial's *shape*, not merely for slack.** This directly rules out
   the "generously low-rank, easy explicit SOS" shortcut the outline hoped
   for: `\sigma_0` needs (numerically) all `18$ dimensions to hit the target
   shape, even though `4$–`5$ of its eigenvalues are forced to the exact PSD
   boundary.

**Net assessment for sub-goal A.** Genuine progress of a diagnostic, not
constructive, kind: (a) a reusable, now-necessary methodological fix — exact
rational witness points, not float ones, are required for any future exact-
certificate attempt in this family, and a concrete recipe (rational
`\tan(B/2)$ parametrization plus a small-denominator scan for domain
membership) is given and verified to work; (b) the round-15 numeric SDP
result is reproduced cleanly at such an exact point (`t^*\approx7.8155`),
confirming it is not a float-precision artifact; (c) **a new, precisely
diagnosed obstruction to naive exact extraction**: `\sigma_0`'s optimal Gram
matrix is forced to near-exact rank deficiency (`4$–`5` eigenvalues at
`\lesssim10^{-7}`, confirmed independent of the slack `t$ by direct
re-optimization across `t\in\{0,2,5,7,7.816\}`), and this degeneracy is
*not* removable by discarding those directions (a rank-13 explicit-SOS
attempt is decisively, not marginally, infeasible for the remaining three
generators to compensate). **No exact rational SOS certificate was
obtained this round** — this is reported honestly as an open gap, per
CLAUDE.md's rigor rules, not claimed as solved. The obstruction is a real
mathematical fact worth recording precisely (a strong, multiply-cross-
checked numerical finding, though not yet an exact symbolic proof that the
degeneracy is *exactly* `0` rather than merely `\lesssim10^{-8}`): any
future exact-certificate attempt at this ansatz size likely needs either
(i) the exact algebraic identification of `\sigma_0`'s forced null
directions (plausibly tied to a genuine double real root of the residual
polynomial — not attempted this round, a nontrivial resultant/discriminant
computation), or (ii) an enlarged ansatz (higher degree and/or extra
generators) to relieve the degeneracy and open genuine numerical margin
before attempting rational rounding.

**Sub-goal B — not attempted this round, deferred honestly.** Given (a)
sub-goal A was explicitly prioritized and consumed the round's time budget,
and (b) the degeneracy found in sub-goal A is a property of the *pointwise*
ansatz that would very plausibly recur (or worsen) in a joint multivariate
version — promoting `\lambda_i` to polynomials in `(\cos B,\sin B)` adds
degrees of freedom that could either relieve or be structurally blocked by
the same forced-null-direction phenomenon — attempting the joint SDP before
understanding sub-goal A's obstruction risked wasted effort building a much
larger (many-hundred-variable) SDP on top of an unresolved foundational
issue. **Recommended next step, not taken this round**: before attempting
the full joint ansatz, identify (symbolically, via `sympy.resultant` or
`discriminant`) whether `\mathrm{Num}-t^*-\lambda_1^*n_1-\lambda_2^*n_2-
\lambda_3^*n4sq` (at the numeric optimum) has a genuine repeated real root
in `u$ — this would confirm or refute the "forced double root" hypothesis
directly and, if confirmed, would identify exactly where a joint-in-`B`
certificate must also vanish, which is essential structural information for
any degree-`\le1`-in-`(\cos B,\sin B)` joint ansatz to have a chance.

### Round 16 outline (proof-outliner directive — skeleton, not a proof, kept
for the record of what was dispatched)

**Two parallel sub-goals this round, per the round-16 `math-explorer-sos-extraction`
report, both reusing `/tmp/round-15/sos_work/` (`sdp_solve.py`…`sdp_solve4.py`,
`sdp_cheb.py`, `build_polys.py`, `polys.pkl`, `rescaled_coeffs.pkl`) as a
starting point — no re-derivation of Theorem 4 or Parts 1–2 needed.**

**Sub-goal A (higher expected value, self-contained): exact rational
Gram-matrix extraction at the existing witness points, via round-then-project.**

1. *Diagnostic first (cheap, ~free)*: compute and inspect the full
   eigenvalue spectrum (not just the minimum eigenvalue already logged) of
   the converged numeric Gram matrices `G₀,G₁,G₂,G₃` at the witness point
   `(A,B)≈(0.603,1.269)`. If any is effectively low-rank (say rank ≤4 out
   of 15–18), rewrite it as `V^Tᐧ V` with `V` a small `k×n` matrix — an
   explicit small sum of squares, both easier to verify by hand and far
   better conditioned for exact rational rounding — before attempting
   step 2.
2. Round each Gram-matrix entry to a nearby rational with a small bounded
   denominator (`sympy.nsimplify` or continued-fraction rounding).
3. The rounded matrices will not exactly satisfy the linear equality
   constraints `σ₀+λ₁n1+λ₂n2+λ₃n4sq = Num−t*` coefficient-by-coefficient
   (`Num,n1,n2,n4sq` are exact rational/`ℚ(√3)` polynomials, already
   certified). Compute the exact residual defect vector in `sympy`.
4. Since the equality constraints are *linear* in the Gram-matrix entries,
   solve exactly (via `sympy` linear algebra, not another SDP) for a
   minimal correction `ΔG` in the affine null-space of the map
   "Gram-matrix entries ↦ polynomial coefficients," using the numeric
   solution as the starting point.
5. Re-verify `G+ΔG` is exactly PSD (`sympy.Matrix.is_positive_semidefinite`
   or an exact LDL^T/Cholesky-with-rational-pivots decomposition — this is
   the step that could fail if the true optimum is exactly rank-deficient
   at the PSD boundary, but the comfortably-positive numeric slacks
   already logged (`t* ≈ 0.24` to `8.5`, none near `0`) make this unlikely).
6. If successful, this yields a fully rigorous, hand-verifiable POINTWISE
   certificate ("`Num(u, B≈1.269) ≥ 0` for all valid `u`, via an explicit
   exact SOS decomposition") — not the full proof, but a genuine
   certifiable lemma and a strong sanity check on the ansatz shape before
   committing more effort to sub-goal B.

**Sub-goal B (the one that could actually close the gap, larger
undertaking): promote pointwise multipliers to low-degree joint
polynomials in `(cosB, sinB)`.**

1. Set up ONE SDP where `λ₁(u,cosB,sinB), λ₂(...), λ₃(...)` are themselves
   polynomial (start with degree ≤1, i.e. affine, in `(cosB,sinB)` — the
   cheapest test — then degree ≤2 if that's infeasible) and `σ₀` is a
   joint SOS polynomial in all three variables, so that
   `Num − σ₀ − λ₁n1 − λ₂n2 − λ₃n4sq ≡ 0` becomes a genuine polynomial
   identity in three variables (many more scalar linear equality
   constraints on a correspondingly larger Gram-matrix system), reusing
   `build_polys.py`'s existing joint `(u,cosB,sinB)` parsing.
2. **Build in from the start** (per explorer technique 6): add a
   free-sign (non-SOS) multiplier `μ(u,cosB,sinB)·(cosB²+sinB²−1)` to the
   certificate, since `cosB,sinB` are now free polynomial variables rather
   than numbers fixed per witness point — omitting this ideal-membership
   term is a likely silent source of spurious infeasibility or inflated
   required degree.
3. Try constant λ first only as a sanity check expected to fail (round
   15's own pointwise `t*` values vary substantially, `0.24` to `8.5`,
   across `(A,B)`, so a constant-λ joint certificate is very unlikely to
   exist) — do not spend real budget there; go straight to degree ≤1.
4. Before running the full joint SDP, re-run the pointwise SDP (cheap,
   reuses existing code) at 2-3 points near the domain boundary
   `A→A*≈0.4064` to see whether `t*(B)→0` there (expected, since Case (b)
   pinches to a corner) — this constrains the achievable λ-degree and is a
   useful sanity check on the joint solver's own output.

**Do not** re-attempt a bare higher-degree monomial-basis *pointwise* SDP
without either upgrade above — round 15 already achieved a clean pointwise
result at the natural degree; further pointwise runs at more points add
only more numeric-only evidence of the same already-judged-insufficient
kind.

### Round 15 (this round) — the n4→n4sq plain-polynomial simplification, formally
proved (Theorem 4); a full-degree, clean two-solver 3-generator SDP at four
independent witness points reverses the "suggestive but inconclusive" verdict
into strong, reproducible numeric evidence — but still NOT an exact
certificate, and still only pointwise (not the global multivariate target).

**Part 1 — Theorem 4 (n4≥0 ⟺ n4sq≥0 on Case (b)'s domain, plain polynomial,
no algebraic extension), fully proved, case-free.** See "Promotable lemmas"
below for the certified statement and proof. Summary: on Case (b)'s domain,
`cos B>0` (elementary, from `B≤C` and the angle-sum) and `u(3−u²)>0`
(elementary, from `u∈(0,2−√3)⊂(0,√3)`), so `n₄=w³cosB−u(3−u²)` compares two
*nonnegative* quantities, making the squaring `n₄≥0 ⟺ (w³cosB)²≥(u(3−u²))²`
lossless; substituting `w²=1+u²` gives `n4sq:=(1+u²)³cos²B−u²(3−u²)²`, a
degree-6-in-`u` polynomial in the PLAIN ring `ℚ(√3)[u,cosB,sinB]` — no `w`,
no extension bookkeeping. This closes the outline's dispatched item 1 in
full; independently symbolically re-verified this round (own fresh `sympy`
session: `(w³cosB)²−(u(3−u²))²` expanded and reduced mod `w²=1+u²` matches
`n4sq` exactly, residual 0) and numerically corroborated (own `mpmath`
30-digit script, `300,000` samples on the correctly-restricted domain
`B≤(π−A)/2`: **0 mismatches** between `sign(n₄)` and `sign(n4sq)`; a
control run using only the weaker `B<π/2` restriction reproduces the
expected `≈19%` mismatch rate, confirming — as flagged repeatedly by prior
rounds — that the exact `B≤(π−A)/2` restriction, not merely `B<π/2`, is
what makes the equivalence exact).

**Part 2 — rebuilding Num, n1, n2 from scratch (independent of any prior
round's displayed polynomials).** Own fresh `sympy` session, own
`u=tan(A/6)` Weierstrass substitution (`cosA=4x³−3x`, `sinA=3y−4y³` with
`x=(1−u²)/(1+u²), y=2u/(1+u²)`; `β₀=π/3−A/3` via `cosβ₀=½x+(√3/2)y`,
`sinβ₀=(√3/2)x−½y`), rebuilding `K_c,P,Q,f,G,X₀,RHS` from the raw
definitions (not copied from the file), clearing denominators via
`sympy.together`/`fraction`: obtained `Den=−16(u²+1)¹⁴h` (exact match to
Theorem 1's `h`), `deg_uNum=34`, `deg_un1=10` (denominator `−4(u²+1)²h`),
`deg_un2=6` (denominator `−2h`) — matching rounds 12–14's reported structure
exactly, component for component, independently re-derived this round.

**Part 3 — the 3-generator SDP, run with correct conditioning and, this
round, without the prior rounds' apparent conditioning discrepancy.** Using
the affine rescaling `u=((2−√3)/2)(s+1)` mapping the true `u`-domain exactly
onto `s∈[−1,1]` (as round 13 used), and the FULL degree-34 ansatz sizes
round 13/14's explorer used (`σ₀` half-degree 17, `λ₁` half-degree 12
[multiplying `n1`, degree 10, to reach degree 34], `λ₂` half-degree 14
[multiplying `n2`, degree 6], `λ₃` half-degree 14 [multiplying the new
`n4sq`, degree 6]), maximizing slack `t` in
`Num−t·𝟙_{k=0}=σ₀+λ₁n1+λ₂n2+λ₃n4sq` (all `σ₀,λᵢ` SOS via PSD Gram matrices,
`≈630` total SDP scalar variables), at the explorer's own known-hard witness
point `(A,B)≈(0.603,1.269)` (where the 2-generator ansatz is proved
unconditionally infeasible, Theorem 3): **both solvers converge cleanly to
`optimal` (not `optimal_inaccurate`) status, in close agreement:**
`t*≈8.5079759` (CLARABEL) vs. `t*≈8.5079935` (SCS) — agreement to 5–6
significant figures, a decisively positive slack, three orders of magnitude
above any plausible noise floor. Extracted Gram matrices: minimum
eigenvalues `≈−4.1×10⁻⁸` (`G₀`), `≈0.877` (`G₁`), `≈2.1×10⁻⁸` (`G₂`),
`≈2.3×10⁻⁶` (`G₃`) — all effectively `≥0` up to ordinary floating-point
solver tolerance (not the `≈−1` to `−10` violations that would indicate a
spurious solution); reconstructing `σ₀+λ₁n1+λ₂n2+λ₃n4sq` from the returned
Gram matrices and comparing against `Num−t*` coefficient-by-coefficient
gives a **maximum absolute residual of `1.6×10⁻⁹`** across all 35
coefficients — an excellent numerical fit, unlike the round-14 explorer's
own `≈0.72` max-residual, PSD-violated run at the same problem size. This
is a substantially cleaner and more reliable numeric result than any prior
round's SDP attempt at this witness point and ansatz size.

**Part 4 — reproduced independently at three further domain-valid witness
points, all consistent.** Re-ran the identical (17,12,14,14)-ansatz SDP,
same rescaling, at three more points, first confirming genuine Case-(b)
domain membership (`n1>0,n2>0,n4sq>0,Num>0` all checked directly from the
independently-rebuilt polynomials):

| `(A,B)` | `n1` | `n2` | `n4sq` | `Num` | CLARABEL `t*` | SCS `t*` |
|---|---|---|---|---|---|---|
| `(0.603,1.269)` | `0.1109` | `0.6367` | `0.000173` | `9.524` | `8.507976` | `8.507994` |
| `(0.42,0.92)` (near corner) | `0.0251` | `0.0121` | `0.3284` | `0.5651` | `0.237615` | `0.237616` |
| `(0.45,1.0)` | `0.0306` | `0.1811` | `0.2463` | `2.9763` | `2.544223` | `2.544223` |
| `(0.5,1.05)` | `0.1024` | `0.2718` | `0.1903` | `5.3398` | `3.938773` | `3.938773` |

Every point tested gives status `optimal` at both solvers, agreement to
5–6 significant figures, and a comfortably positive slack. (A fifth point,
`(A,B)=(0.35,0.9)`, was independently checked to have `n1<0` — i.e. it lies
outside Case (b)'s true domain at all, consistent with round 11's certified
finding that Case (b) is empty for `A≤A*≈0.4064`; the SDP there returns
`unbounded`, which is the expected, non-alarming behaviour for an emptily-
constrained feasibility problem, not a counterexample to anything.) **Note
of an important consistency cross-check**: the near-corner point's slack
`t*≈0.23762` matches round 13's own reported 2-generator-ansatz slack at
this same point (`t*≈0.2376`, round 13's "Finding 2") almost to the digit —
since the 2-generator ansatz was already feasible there, adding `n4sq`
correctly contributes essentially nothing extra at this point, exactly as
expected. This is a genuine, independently-reproduced sanity check that the
new 3-generator machinery specializes correctly to the already-published
2-generator result where the latter already succeeds.

**Part 5 — an explicit, honestly-diagnosed pitfall found and corrected this
round: a naive low-degree ansatz gives a FALSE "success" via a silent
constraint-dropping bug, not a genuine lower-degree certificate.** An
initial attempt to find the *minimal* sufficient ansatz degree (hoping for
an exactly-matching lower-degree — hence more tractable for exact
extraction — certificate) used half-degrees `(10,5,5,5)` (total degree 20,
well below `Num`'s degree 34) and appeared to reproduce the SAME optimal
slack `t*≈8.5080` as the full degree-34 ansatz. **This was traced to a bug,
not a genuine finding**: the implementation silently skipped equality
constraints at monomial degrees `k>20` (where no SDP variable contributes,
since all four SOS pieces vanish there) whenever the *target* coefficient
at that degree also happened to be a plain float rather than a cvxpy
expression — but the target's degree-`21..34` coefficients of `Num` (in the
rescaled `s`-variable) are **not exactly zero**, only *numerically tiny*
(`≈10⁻¹⁴` to `10⁻²⁹`, since `u∈(0,0.268)` makes high powers of `u` small
after the affine rescaling), so silently treating "target is a plain float"
as "no constraint needed" incorrectly discarded genuine (if tiny)
degree-21–34 matching requirements. Re-running with an explicit static
tolerance check (`|lhs−rhs|<10⁻⁹` before allowing a constraint to be
dropped) correctly reports genuine infeasibility for `(6,3,3,3)` and
`(8,4,4,4)`, and only reports "optimal" from half-degree `10` upward — but
even there the reported match is only *approximate* (residual capped by the
`10⁻⁹` tolerance, not exact), so **no claim of a lower-than-34-degree exact
certificate is made**; this is recorded here explicitly as a documented
implementation pitfall for any future round attempting the same degree-
reduction search (do not silently drop float-vs-float equality checks in a
`cvxpy` constraint-construction loop — always assert the values actually
match before treating the constraint as trivial).

**Net assessment — what this round genuinely establishes and what it does
NOT.** Established, fully rigorously: Theorem 4 (`n4≥0⟺n4sq≥0`, plain
polynomial, case-free, proved and verified both symbolically and
numerically). Established, with strong but *not exact* numerical evidence
(clean `optimal` status at two independent solvers, 5–6-digit agreement,
`≈10⁻⁹` residual, PSD satisfied to `≈10⁻⁸`, reproduced at four independent
domain-valid witness points including the previously-known-hardest one):
the 3-generator ansatz `Num=σ₀+λ₁n1+λ₂n2+λ₃n4sq` (degree-34 total, plain
ring, no algebraic extension) appears genuinely feasible — pointwise, at
every `B`-slice tested — with a comfortable, non-noise-floor margin. This
is a substantial reversal of the round-14 explorer's own "suggestive but
solver-disagreeing, `optimal_inaccurate`" verdict into a clean, reproducible
result. **This is NOT yet a proof.** Two gaps remain, both explicitly
required by CLAUDE.md's rigor rules and this round's own dispatch: (a) no
exact rational Gram-matrix certificate has been extracted and symbolically
verified (attempted; degree 34 with `ℚ(√3)`-valued target/generator
coefficients makes exact rounding-and-verification a substantial
undertaking not completed this round — see Part 5's honest account of what
was and wasn't achieved); (b) even a fully exact pointwise certificate at
one, or even four, fixed `B`-values does **not** establish the true target
(`Num≥0` as a polynomial identity/Positivstellensatz jointly in
`(u,cosB,sinB)`) — a global certificate needs `σ₀,λ₁,λ₂,λ₃` themselves to be
polynomials in `(cosB,sinB)` (not real numbers re-fit at each sample `B`),
which was not attempted this round. Both gaps are recorded below as the
concrete next targets.

## Open gaps (further updated, round 18)
**Round 18 update, in brief (full detail in the round-18 section above):**
the 3 dispatched diagnostic tests were run. Test 1 (real roots of `n_2,n4sq`
at the witness): a single evaluation vector (at `n_2`'s domain-generator
root at witness 1, at `n4sq`'s at witness 2) captures a large majority
(`88\%$/`76\%$ respectively) of the residual 3-dim near-null complement —
real, but not uniform across the two witnesses tested. Test 2 (`\sigma_0`'s
full root list for a near-double conjugate pair): found exactly the
`s^*`-adjacent pairs (consistent with 4th-order tangency there), and
**ruled out** any other comparably-small-imaginary-part pair — the round-17
hypothesized mechanism is checked and not confirmed. Test 3
(`M_0z''(s^*)=0`): feasible, essentially free (`t^*` unchanged), but grows
the near-null cluster from 5 to 6 rather than shrinking it — 3 remain
unexplained either way. **Net: real partial progress explaining much, but
not all, of the residual, with no uniform mechanism identified yet; still
no exact rational/algebraic SOS certificate.**

**Round 17 update, in brief (full detail in the round-17 section above):**
the `M_0z(s^*)=0` complementary-slackness constraint was built into the SDP
explicitly (not merely observed) and confirmed cheap (feasible, `t^*`
unchanged, residual → `10^{-9}`); adding the order-2 (`z'(s^*)`) constraint
too remains feasible with excellent polynomial-identity residuals
(`\approx6\times10^{-11}`) but does **not** reduce `M_0`'s rank deficiency
below its prior `5` near-null eigenvalues — 3 of the 5 remain unexplained,
unchanged from round 16. The mechanism was independently reproduced at a
**second, genuinely different exact rational witness point**
(`r=\tan(B/2)=1/2`, `u=7/100`), closing the "untested at other points" item
flagged by round 16. Still no exact rational/algebraic SOS certificate.

1. `Num≥0` on Case (b)'s domain (equivalently `(⋆)`) — still not proved.
   **Round 15 upgraded the numeric evidence substantially** (clean,
   two-solver-agreeing, low-residual, PSD-satisfied SDP at four witness
   points). **Round 16 reproduced this cleanly at a genuine exact rational
   witness point** (`u=93/1000`, `\cos B=51/149`, `\sin B=140/149`,
   `t^*\approx7.8155`), closing the "float witness point isn't exact-
   certifiable" gap in principle — but **found and precisely diagnosed a new
   obstruction to the round-15-planned extraction method**: `\sigma_0`'s
   optimal Gram matrix is forced to near-exact rank deficiency (`4`–`5` of
   `18` eigenvalues at `\lesssim10^{-7}`, a spectral gap of `\approx0.0139`
   to the rest), confirmed *independent of the slack* `t` by re-optimizing
   the joint PSD margin at `t\in\{0,2,5,7,7.816\}` (margin stays pinned at
   `\approx-2\times10^{-8}$, i.e. `0` to solver precision, at every value
   tested) and confirmed *not discardable* (an explicit rank-13 `\sigma_0=
   Q^TQ`, exactly PSD by construction, leaves a residual the other three
   generators are decisively — `\lambda^*\approx-0.51$, not marginally —
   unable to supply). No exact rational certificate obtained. Still open:
   (a) exact extraction at this or any point (harder than anticipated, see
   round 16's Step 2 above); (b) the joint multivariate Positivstellensatz
   (not attempted, see below).
2. `n4` requires the algebraic extension `w=√(1+u²)` — **CLOSED**, round 15
   Theorem 4 (unchanged this round).
3. Extracting and symbolically verifying an exact rational SOS certificate
   — **attempted again, more rigorously, this round; still not completed**.
   Round 16 pins down *why* naive round-and-project fails (a genuine,
   `t`-independent near-boundary degeneracy of `\sigma_0`, not a rounding-
   precision artifact) rather than merely re-attempting the same method.
   Recommended next step (not taken): symbolically test, via
   `sympy.resultant`/`discriminant`, whether the optimal residual
   polynomial `\mathrm{Num}-t^*-\sum\lambda_i^*n_i` has a genuine repeated
   real root in `u` at this witness point — this would upgrade the
   degeneracy from "strong numerical evidence" to a proved structural fact
   and identify exactly what an exact certificate must vanish at.
4. The joint multivariate (`(u,cosB,sinB)`-simultaneous, not per-point)
   3-generator Positivstellensatz — **still not attempted** (round 16's
   sub-goal B was explicitly deferred: attempting it before understanding
   sub-goal A's degeneracy risked building a much larger SDP on an
   unresolved foundation, since the same forced-null-direction phenomenon
   would plausibly recur or worsen when `\lambda_i` are promoted to
   bivariate polynomials). Recommended to attack only after item 3's
   repeated-root diagnostic is resolved.

## Promotable lemmas (round 15 addendum)

**New lemma (round 15), fully proved by elementary case-free algebra plus
independent symbolic and numeric verification — candidate for certification
as `lemmas/n4-to-n4sq-plain-polynomial-equivalence.md`:**

**Theorem 4.** With `u:=tan(A/6)` as in Theorem 1, `w:=√(1+u²)>0`, and
`n4(u,w,cosB):=w³cosB−u(3−u²)` as in Theorem 2 (certified
`lemmas/angle-b-le-c-weierstrass-encoding.md`), define the PLAIN polynomial
$$n4sq(u,\cos B):=(1+u^2)^3\cos^2B-u^2(3-u^2)^2\ \in\ \mathbb Q[u,\cos B]$$
(no `w`, no algebraic extension). Then, on Case (b)'s domain (`A∈(0,π/2]`,
`∠B≤∠C`, so in particular `u∈(0,2−√3)`), as an unconditional equivalence,
$$n4(u,w,\cos B)\ge0\iff n4sq(u,\cos B)\ge0.$$

*Proof.* We first establish two elementary sign facts on Case (b)'s domain.

(i) **`cos B>0`.** Since `∠B≤∠C` and `A+B+C=π` with `A>0`, we have
`B+C<π`. Suppose toward contradiction `B≥π/2`. Since `B≤C`, this gives
`C≥B≥π/2`, so `B+C≥π`, contradicting `B+C<π`. Hence `B<π/2`, so
`cos B>0` (as `B>0` also, being an angle of a genuine triangle).

(ii) **`u(3−u²)>0`.** Since `A∈(0,π/2]`, `t:=A/6∈(0,π/12]`, so
`u=\tan t\in(0,\tan(\pi/12)]=(0,2-\sqrt3]`. In particular `u>0`. Since
`2-\sqrt3\approx0.268<\sqrt3`, also `u<\sqrt3$, so `u^2<3`, giving
`3-u^2>0`. Hence `u(3-u^2)>0`.

(This matches the outline-reviewer's independently-verified argument, and
was independently reconfirmed here.)

Now, `w^3\cos B\ge0` by (i) and `w>0`, and `u(3-u^2)>0` by (ii); so `n4\ge0$
compares the two NONNEGATIVE real numbers `w^3\cos B` and `u(3-u^2)`.
For any two nonnegative reals `X,Y\ge0`, `X\ge Y\iff X^2\ge Y^2$ (the
forward direction is monotonicity of `t\mapsto t^2` on `[0,\infty)`; the
converse holds because `X^2\ge Y^2\iff(X-Y)(X+Y)\ge0`, and `X+Y\ge0`, with
`X+Y=0` only when `X=Y=0`, a case in which `X\ge Y` trivially holds, so in
all cases `X^2\ge Y^2\Rightarrow X\ge Y$ whenever `X,Y\ge0`). Applying this
with `X:=w^3\cos B\ge0`, `Y:=u(3-u^2)>0$ (so in particular `Y\ge0`):
$$n4\ge0\iff w^3\cos B\ge u(3-u^2)\iff(w^3\cos B)^2\ge(u(3-u^2))^2\iff
w^6\cos^2B-u^2(3-u^2)^2\ge0.$$
Finally `w^6=(w^2)^3=(1+u^2)^3` (since `w^2=1+u^2` by definition), so the
last displayed condition is exactly `n4sq(u,\cos B)\ge0`. Chaining the
equivalences proves the theorem. `\blacksquare`

**Independent verification (this round).** (1) Symbolic: own `sympy`
session confirms `\bigl(w^3\cos B\bigr)^2-\bigl(u(3-u^2)\bigr)^2$, expanded
and with `w^2` replaced by `1+u^2` throughout, equals
`(1+u^2)^3\cos^2B-u^2(3-u^2)^2` exactly (residual `0` after
`sympy.expand`). (2) Numeric: own `mpmath` 30-digit-precision script,
`300{,}000` uniform random `(A,B)` samples with `A\in(0,\pi/2)` and
`B\in(0,(\pi-A)/2)` (i.e. genuinely restricted to `∠B≤∠C`, the domain the
theorem requires): **`0/300{,}000`** mismatches between `\mathrm{sign}(n4)`
and `\mathrm{sign}(n4sq)`. A control run using only the strictly weaker
restriction `B<\pi/2` (dropping `B\le C`) reproduces a substantial mismatch
rate (`\approx19\%$ of `300{,}000$ samples), confirming that the theorem's
domain hypothesis (`∠B≤∠C`, not merely `B<π/2`) is exactly what is needed
and is not a superfluous overstatement.

**Consequence.** The route's Case-(b) domain is now fully polynomially
encoded in the PLAIN ring `\mathbb Q(\sqrt3)[u,\cos B,\sin B]` — no algebraic
extension — via three generators `n1>0` (deg 10, `ℚ(√3)`-coefficients),
`n2>0` (deg 6, `ℚ`-coefficients), `n4sq\ge0` (deg 6, `ℚ`-coefficients), plus
the interval bound `u\in(0,2-\sqrt3)`. This is a genuine simplification of
the Positivstellensatz setup a future round should use (replacing the
4-generator extended-ring `(u,w,\cos B,\sin B)/(w^2-1-u^2)` ansatz with a
3-generator plain-ring one), as this round's Part 3–4 SDP experiments
already exploit.

## Approaches tried
(inherited verbatim from `coordinate-bash-resultant-boundary-pointwise` through
round 10 — this file is a round-11 fork targeting the same open gap `(\star)`
via a genuinely different, algebraic (SOS-after-radical-clearing) mechanism
instead of the sibling's analytic (local-expansion) one. See the sibling file
for the full history of rounds 1-10; not duplicated here to avoid drift.)

### Round 11 (this round) — triple-angle clearing via a rational (Weierstrass)
parametrization; a genuine reduction, SOS certificate NOT found; negative
finding on the "clean global polynomial" hope, with a precise, reusable
semialgebraic reformulation left for a future round.

**Setup reused verbatim (certified `lemmas/mvt-lipschitz-reduction-case-b.md`).**
`K_c=2\sin A\sin(A+B)`, `P=\tfrac12\sin(A-B)+\tfrac32\sin(A+B)`,
`Q=-\sin A\sin B`, `f(\beta)=K_c+P\sin\beta+Q\cos\beta`, `G(\beta)=2K_c-f(\beta)`,
`\beta_0=(\pi-A)/3`, `X_0=\sin B\cos A/(2\sin(A+B))`,
`\mathrm{RHS}=(1+\cos B)\cos\beta_0-\sin\beta_0G(\beta_0)`, target
$$(\star)\qquad (1+\cos B)^2X_0\ \ge\ \mathrm{RHS}^2,$$
needed only when `\mathrm{RHS}>0`, on Case (b)'s domain: `A,B\in(0,\pi)`,
`\cos A\ge0` (i.e. `A\in(0,\pi/2]`), `\angle B\le\angle C$ (i.e. `B\le(\pi-A)/2`,
the WLOG labeling convention — **this exact constraint, not merely `B<\pi/2`,
is essential**; see the correction noted below), and, with `\beta_1:=\arccos
\sqrt{X_0}\in(0,\pi/2)`, `\beta_0<\beta_1<B`.

**Step 1 — triple-angle clearing, done via a genuinely different (better)
substitution than the outline's literal proposal.** The outline's dispatched
plan was to substitute `\cos\beta_0,\sin\beta_0` as cubics in `x:=\cos(A/3)`,
`y:=\sin(A/3)=\sqrt{1-x^2}`, hoping only even powers of the radical `y` survive
after `(\star)` is expanded. **I built this substitution explicitly (`sympy`,
own script) and checked the claim directly: it is FALSE.** Writing
`\mathrm{num}(x,y,\cos B,\sin B)/\mathrm{den}(x,y,\cos B,\sin B)` for
`(1+\cos B)^2X_0-\mathrm{RHS}^2$ after clearing the sole denominator
`\mathrm{den}=-256\sin(A+B)` (verified numerically, 20 fresh random samples,
relative error `<10^{-12}`), and reducing `\mathrm{num}` modulo `y^2=1-x^2`
gives `\mathrm{num}=R_0(x,\cos B,\sin B)+y\,R_1(x,\cos B,\sin B)` with **`R_1$
genuinely nonzero** (`84`- and `79`-term polynomials respectively, `\deg_xR_0=16`,
`\deg_xR_1=15`) — so the naive `\cos(A/3)`-basis substitution does **not**
already give a radical-free rational function; it requires one more squaring
(`R_0^2-(1-x^2)R_1^2$, plus a further `\mathrm{sign}(R_1)`-dependent case split
to justify the squaring is valid) to clear `y`. This squared quantity was built
explicitly (degree `34` in `x`, degree `6` jointly in `\cos B,\sin B`, `494`
terms before `\mathtt{sympy.factor}`) and `\mathtt{sympy.factor}` was run on it
(under 5 minutes): **it returns only the constant `256` factored out — no
further algebraic factorization is found.** This is a genuine negative
finding for the literal outline plan, not a stall: the claim that `(\star)` is
"already one clean squaring away from radical-free" in the `\cos(A/3)` basis
is refuted, and the resulting degree-34 object does not factor.

**Step 1' — a strictly better substitution, avoiding the extra squaring
entirely.** Since `x=\cos(A/3),y=\sin(A/3)` satisfy `x^2+y^2=1` with no extra
structure, use instead the Weierstrass parametrization on the sixth-angle:
`u:=\tan(A/6)`, so `x=\cos(A/3)=\dfrac{1-u^2}{1+u^2}`,
`y=\sin(A/3)=\dfrac{2u}{1+u^2}` — a *bijective, radical-free* rational
substitution (no `\pm\sqrt{}$ ambiguity, unlike `y=\sqrt{1-x^2}`, since `u$
ranges freely over the reals as `A/6` ranges over `(0,\pi/2)`). Substituting
directly into the trig expression for `(1+\cos B)^2X_0-\mathrm{RHS}^2`
(own `sympy` session, `A\mapsto 3t\mapsto$ triple-angle expand `\mapsto$
substitute `\cos t,\sin t\mapsto x_u,y_u\mapsto$ substitute `\cos B,\sin B$)
gives, after clearing denominators,
$$(1+\cos B)^2X_0-\mathrm{RHS}^2=\frac{\mathrm{Num}(u,\cos B,\sin B)}
{\mathrm{Den}(u,\cos B,\sin B)},$$
$$\mathrm{Den}=-256(u^2+1)^{14}\bigl(-6\cos B\,u^5+20\cos B\,u^3-6\cos B\,u
+\sin B\,u^6-15\sin B\,u^4+15\sin B\,u^2-\sin B\bigr),$$
with `\mathrm{Num}` an explicit polynomial in `\mathbb Q(\sqrt3)[u,\cos B,
\sin B]` of degree `34` in `u` and (jointly) degree `3` in `(\cos B,\sin B)`
(`466` terms in expanded form). **This identity was independently verified
numerically** (own `sympy`/`mpmath` script, `mp.dps=30`): `20` fresh random
`(A,B)` samples give `|\mathrm{Num}/\mathrm{Den}-[(1+\cos B)^2X_0-
\mathrm{RHS}^2]|<10^{-12}` in every case. This achieves the outline's Step-1
goal — a genuine algebraic (non-transcendental-in-`A`) reformulation of
`(\star)` — **cleanly and in one substitution, with no extra squaring and no
sign-dependent case split**, unlike the literal `\cos(A/3)`-basis route.
(One correction to my own initial read of this computation: `\mathrm{Num}`
does still carry `\sqrt3` coefficients, inherited from `\cos(\pi/3-A/3),
\sin(\pi/3-A/3)` in `\beta_0`'s definition — this is unavoidable and does not
make `\mathrm{Num}` "irrational" in the disqualifying sense: it lives in the
fixed quadratic extension `\mathbb Q(\sqrt3)`, a perfectly good coefficient
field for a polynomial-positivity argument, just not `\mathbb Q$ itself.)

**Step 2 — sign of `\mathrm{Den}$.** `\mathrm{Den}=-256(u^2+1)^{14}\cdot h(u,
\cos B,\sin B)`, `h:=-6\cos B\,u^5+20\cos B\,u^3-6\cos B\,u+\sin B\,u^6-15
\sin B\,u^4+15\sin B\,u^2-\sin B`. Numerically (own script, `500{,}000`
samples restricted to the corrected Case-(b) domain, see Step 3 below):
`\mathrm{Den}>0$ throughout (`0` sign changes) — consistent with `h$ being
(up to the explicit rational prefactor) the same `\sin(A+B)$ factor that
appears as the sole denominator throughout this whole population's
`X_0`-based computations, here just re-expressed via `u`; I did not
symbolically re-derive `h=c(u^2+1)^6\sin(A+B)` for an explicit constant `c`
this round (time-limited) — **this identification is asserted only as a
numerically-corroborated plausibility, not a proved identity**, and is
flagged as an open item below.

**Step 3 — domain correction (found and fixed this round).** My first
attempt at the Case-(b) numeric sweep used only `B<\pi/2` (not the full WLOG
`\angle B\le\angle C$, i.e. `B\le(\pi-A)/2`) and found `\approx2\%$ of sampled
points violating `(\star)` by as much as `-0.17` — **this was a bug in my own
domain restriction, not a refutation of the certified reduction**: at the
"violating" witness `(A,B)\approx(1.511,1.325)`, direct computation gives
`G(\beta_1)\approx0.385>0` (the actual target, still true) even though
`(\star)$ — a merely *sufficient*, lossy MVT bound — happens to fail there;
and, decisively, `B\approx1.325>(\pi-A)/2\approx0.815$ at that point, i.e. it
lies **outside** the WLOG-labeled domain (`\angle B$ is not the smaller of
the two base angles there) — not a genuine domain point at all. Restricting
correctly to `B\le(\pi-A)/2$ (in addition to `\cos A\ge0`, `\beta_0<\beta_1<B`,
`\mathrm{RHS}>0`), a fresh `2{,}000{,}000`-sample sweep (own script) finds
**`0` violations of `(\star)`**, minimum slack `\approx0.0021` — matching the
certified lemma's own reported figures and confirming this round's
`(u,\cos B,\sin B)` reformulation is consistent with all prior findings once
the domain is stated correctly. (This is recorded explicitly as a
methodological trap for any future round reusing this file's numeric
machinery: always impose `\angle B\le\angle C$ literally, not merely
`B<\pi/2`.)

**Step 4 — is `\mathrm{Num}\ge0` a domain-free (global SOS-amenable) claim?
No — checked directly, decisive negative finding.** With the corrected
domain (Step 3), a `500{,}000`-sample sweep found `\mathrm{Num}>0`
throughout (range `[4.41,183.5]`, bounded away from `0` except as the domain
pinches to the known corner) and `\mathrm{Den}>0$ throughout — consistent
with `(\star)`. **But relaxing the domain to just `\cos A\ge0$ (i.e.
`u\in(0,2-\sqrt3)`) and `B$ ranging over all of `(0,\pi)$ — dropping the
`\beta_0<\beta_1<B` and `\angle B\le\angle C$ conditions that define Case (b)
— `\mathrm{Num}`'s sign flips constantly** (own `200{,}000`-sample sweep:
`\approx37\%$ negative, minimum `\approx-1260`). **This conclusively refutes
the possibility of an unconditional (domain-free) SOS certificate for
`\mathrm{Num}` as a polynomial in `(u,\cos B,\sin B)` alone** — no Gram
matrix, however large, can certify positivity of a polynomial that is
genuinely negative elsewhere in the ambient variable space. Any certificate
must be a genuine **Positivstellensatz**-type object: `\mathrm{Num}$ expressed
as an SOS combination *plus* nonnegative-coefficient multiples of the
domain-defining inequalities themselves (Case (b)'s own defining conditions),
not a bare sum of squares.

**Step 5 — the domain-defining conditions, made explicit and algebraic (new,
useful structure for a future attempt).** The two conditions `\beta_0<\beta_1`
and `\beta_1<B` are equivalent, via strict monotonicity of `\cos` on
`(0,\pi/2)$ (both `\beta_0,\beta_1,B\in(0,\pi/2)` in this domain) and
`\cos\beta_1=\sqrt{X_0}\ge0`, to the purely algebraic statements
$$\cos^2\beta_0>X_0\qquad\text{and}\qquad X_0>\cos^2B$$
respectively (no arccos or further trig needed once expressed this way).
Substituting the same `u=\tan(A/6)` parametrization (own `sympy` session)
gives these explicitly as
$$n_1(u,\cos B,\sin B):=\cos^2\beta_0-X_0\ \text{(times a positive
denominator `4(u^2+1)^2h`)},\quad \deg_un_1=10,\ (\text{coefficients in }
\mathbb Q(\sqrt3)),$$
$$n_2(u,\cos B,\sin B):=X_0-\cos^2B\ \text{(times a positive denominator
`2h`)},\quad\deg_un_2=6,\ (\text{coefficients in }\mathbb Q,\text{ no
`\sqrt3` — since `X_0,\cos B` involve no `\beta_0`}).$$
Both `n_1,n_2` are explicit, degree `\le10` polynomials — far smaller and
more tractable than `\mathrm{Num}$ (degree `34`) — and, together with
`u\in(0,2-\sqrt3)` (`\cos A\ge0`) and the `\angle B\le\angle C` linear-in-angle
condition, they give a **complete, explicit semialgebraic description of
Case (b)'s domain** in the `(u,\cos B,\sin B)` coordinates. This is new,
concrete structure: a fully-posed target for a genuine Positivstellensatz
search (`\mathrm{Num}=\sigma_0+\lambda_1n_1+\lambda_2n_2+\cdots`, `\sigma_0,
\lambda_i` SOS) that was **not attempted this round** (would require an SDP
solver — `cvxpy`/similar — set up and run against a degree-34 target with
multiple degree-`\le10` constraint polynomials, a substantial undertaking
beyond this round's remaining time budget after the derivations above).

**Net assessment.** This round makes genuine, independently-verified progress
of a different kind than a symbolic closure: (a) it refutes the outline's
specific optimistic Step-1 hope (naive `\cos(A/3)`-basis clearing is *not*
already radical-free) with an explicit, checked counter-computation; (b) it
replaces that route with a strictly better one substitution (`u=\tan(A/6)`)
that *does* achieve a clean single-step algebraic reduction of `(\star)$ to a
polynomial-sign statement, `\mathrm{Num}\ge0` on an explicit semialgebraic
domain, fully verified numerically; (c) it decisively refutes the stronger
"no case split needed at all" ambition the outline hoped for (a domain-free
SOS certificate is impossible, confirmed by direct counterexample sampling
outside Case (b)); (d) it hands off a concrete, well-posed, much smaller
Positivstellensatz target (`\mathrm{Num}`, `n_1`, `n_2`, plus the two linear
domain conditions) for whichever future round wants to attempt an SDP-based
certificate search — genuinely new, reusable structure, not merely "still
open." No SOS or Positivstellensatz certificate was found or verified this
round; `(\star)` itself remains open, exactly as it was at the start of the
round, but the terrain around it is now mapped substantially more precisely.

**Open gaps.**
1. `\mathrm{Num}\ge0` on Case (b)'s domain (equivalently `(\star)`) — not
   proved; a Positivstellensatz certificate is the recommended next attempt,
   using `n_1,n_2` (Step 5) as the domain-defining multipliers, but this was
   not attempted (needs SDP tooling and substantial additional time).
2. The identity `h(u,\cos B,\sin B)=c(u^2+1)^6\sin(A+B)$ (Step 2) — asserted
   only from numeric sign-consistency, not symbolically derived or certified
   this round.
3. `\mathrm{Den}>0$ and `\mathrm{Num}>0` on the true domain — verified
   numerically at large scale (`500{,}000`+ samples, `0` violations after the
   Step-3 domain correction) but not proved symbolically.

**Watch out for (recorded for future rounds).** (i) The WLOG condition is
`\angle B\le\angle C$, i.e. `B\le(\pi-A)/2` — **not** merely `B<\pi/2`; using
the weaker condition alone silently admits spurious "violations" that are
just non-domain points, as this round's own initial (corrected) mistake
shows. (ii) The naive `\cos(A/3),\sin(A/3)` substitution the outline
proposed does **not** avoid an extra squaring — use `u=\tan(A/6)` instead,
which does. (iii) `\mathrm{Num}$ is not a free-standing SOS target; any
certificate must be a genuine Positivstellensatz combination using the
Case-(b) domain conditions (`n_1,n_2$ above, plus `\cos A\ge0`, `\angle B\le
\angle C`) as nonnegative constraint multipliers, not a bare sum of squares.

## Current best
The whole-problem backbone (central identity, isosceles case, branch
selection reduced to Case (b), Case (b) reduced to `(\star)`) is inherited and
certified as before. Through round 11, `(\star)` was known only
*numerically* to be equivalent to `\mathrm{Num}(u,\cos B,\sin B)\ge0` (an
explicit degree-`34`-in-`u` polynomial over `\mathbb Q(\sqrt3)`), with the
denominator positivity (needed for the equivalence direction) likewise only
numerically checked. **Round 12 (this round) upgrades this to a fully
proved, zero-symbolic-residual equivalence** — see Theorem 1 below — and
then attempts, and precisely documents the failure of, a hand
Positivstellensatz search using `n_1,n_2` as multipliers. **Round 13 (this
round) closes a second prerequisite gap** — the `\angle B\le\angle C`
domain condition now has a fully proved polynomial encoding (Theorem 2,
via the extra generator `w=\sqrt{1+u^2}`) — and reconfirms, with a
well-conditioned two-solver SDP computation at two witness points, that
the minimal 2-/3-multiplier ansatz is genuinely (point-locally) infeasible,
while identifying but not resolving a concrete diagnostic pointing at the
now-available fourth generator `n_4` as the likely missing piece. The open
gap remains unchanged in substance: find a certificate establishing
`\mathrm{Num}\ge0` on the stated domain (equivalently, prove `(\star)`) —
the domain is now fully polynomially specified (`u\in(0,2-\sqrt3)`,
`n_1>0`, `n_2>0`, `n_4\ge0`, in the extended ring with `w^2=1+u^2`), but no
certificate of any degree has yet been found or ruled out in full
generality. **Round 14 (this round) resolves a contradiction between round
13's SDP result and a round-14 explorer's contradictory SDP result, in
round 13's favor, via an exact (non-numeric) counterexample** (Theorem 3):
at the disputed witness `B`, the exact rational point `u=1/4` satisfies
`n_1>0,n_2>0,\mathrm{Num}<0`, **proving unconditionally (any degree) that
no 2-generator (`n_1,n_2`-only) certificate can exist**, and confirming
`n_4` is a necessary (not merely helpful) generator for any valid
certificate. The central gap is unchanged in substance (still open), but
the population's understanding of what a certificate must look like is now
on a fully rigorous footing rather than resting on disputed numerics.
**Round 15 (this round) proves a further simplification** (Theorem 4):
`n_4\ge0` is equivalent, case-free and on Case (b)'s domain, to a PLAIN
polynomial condition `n4sq:=(1+u^2)^3\cos^2B-u^2(3-u^2)^2\ge0` — no
algebraic extension `w=\sqrt{1+u^2}` needed at all — fully proved
symbolically and case-free. Using this, a 3-generator (`n_1,n_2,n4sq`)
degree-34 SDP was run at four independent, domain-verified witness points,
with both CLARABEL and SCS converging cleanly (`optimal` status, not
`optimal_inaccurate`) to closely-agreeing (5–6 significant figures),
comfortably positive slacks in every case, and near-exact residual
(`\approx10^{-9}`) — a substantial, reproducible improvement over the prior
round's inconclusive, solver-disagreeing SDP evidence. This is still NOT a
proof: no exact rational certificate has been extracted (attempted, not
completed — a documented implementation pitfall around silently-dropped
low-degree matching constraints was found and fixed en route, yielding no
false shortcut), and even a fully exact certificate at finitely many
witness points would only be a pointwise result, not the joint
multivariate Positivstellensatz needed to close the route. The central gap
(`\mathrm{Num}\ge0` on the true domain) remains open.

## Full proof
(Not applicable — Status is `partial`.)

## Promotable lemmas

**New lemma (round 12), fully proved, zero symbolic residual — candidate for
certification as `lemmas/star-weierstrass-denominators-positive.md`:**

**Theorem 1.** With `u:=\tan(A/6)`, `x:=\cos(A/3)=\frac{1-u^2}{1+u^2}`,
`y:=\sin(A/3)=\frac{2u}{1+u^2}` (the standard rational double-angle
parametrization on `t:=A/6`, valid and radical-free since `A/3=2t`), and
`\cos A,\sin A` obtained from `x,y` by the triple-angle formulas
`\cos A=4x^3-3x`, `\sin A=3y-4y^3$ (since `A=3\cdot(A/3)`), define
`h(u,\cos B,\sin B):=-6\cos B\,u^5+20\cos B\,u^3-6\cos B\,u+\sin B\,u^6-15
\sin B\,u^4+15\sin B\,u^2-\sin B`
(the same `h` appearing in round 11's `\mathrm{Den}=-16(u^2+1)^{14}h`,
`n_1`'s denominator `-4(u^2+1)^2h`, `n_2`'s denominator `-2h`). Then, as an
**exact polynomial identity** (verified by `sympy`, zero residual after
clearing denominators):
$$h(u,\cos B,\sin B)\;=\;-(1+u^2)^3\sin(A+B),$$
where `\sin(A+B)=\sin A\cos B+\cos A\sin B` with `\sin A,\cos A` as above.
Consequently, **exactly** (all three re-derived and verified independently,
zero residual):
$$\mathrm{Den}=16(1+u^2)^{17}\sin(A+B),\qquad
\mathrm{den}_1=4(1+u^2)^5\sin(A+B),\qquad
\mathrm{den}_2=2(1+u^2)^3\sin(A+B).$$

*Proof.* Direct computation: `\sin(A+B)=\sin A\cos B+\cos A\sin B`, with
`\sin A,\cos A` the triple-angle polynomials in `x,y` above; substituting
`x,y`'s rational forms in `u` and calling `\mathrm{sympy.together}` gives
`\sin(A+B)=\dfrac{-h(u,\cos B,\sin B)}{(1+u^2)^3}` — confirmed by expanding
the numerator of the resulting single fraction and checking it equals `-h`
identically (`\texttt{sympy.expand(num - (-h)) == 0}`, exact, no residual;
this reviewer independently re-ran this check from the raw `x,y,\cos A,\sin
A` definitions, not from any file's displayed formula). Multiplying by the
already-established constants `-16(1+u^2)^{14}$, `-4(1+u^2)^2`, `-2`
(round 11's `\mathrm{Den},\mathrm{den}_1,\mathrm{den}_2$ prefactors, each
re-derived from scratch this round directly from `\cos^2\beta_0-X_0`,
`X_0-\cos^2B`, `(1+\cos B)^2X_0-\mathrm{RHS}^2` via `\texttt{sympy.together}
`/\texttt{fraction}`, matching round 11's reported denominators exactly)
gives the three displayed identities; each was checked independently by
`\texttt{sympy.simplify}` of the difference, returning `0` in every case.
`\blacksquare`

**Corollary (fully rigorous now, not merely numeric).** Since `A,B` are two
angles of a triangle, `0<A+B=\pi-C<\pi`, so `\sin(A+B)=\sin C>0`; and
`(1+u^2)^k>0` for every real `u` and `k>0`. Hence
`\mathrm{Den},\mathrm{den}_1,\mathrm{den}_2>0` **unconditionally** (no
restriction to Case (b) needed beyond `A,B,C` being a genuine triangle's
angles). This means the three equivalences
$$(\star)\iff\mathrm{Num}\ge0,\qquad
\cos^2\beta_0>X_0\iff n_1>0,\qquad X_0>\cos^2B\iff n_2>0$$
(claimed only numerically in round 11) are now **fully proved**, not
conjectural — a genuine, if modest, gap-closing upgrade: the semialgebraic
reformulation of Case (b)'s domain and target is now on rigorous footing,
not resting on any numeric sampling.

## Approaches tried (continued)

### Round 12 (this round) — exact re-derivation of the Weierstrass
reformulation (Theorem 1 above), plus a documented hand Positivstellensatz
search that does not close the gap.

**Step A — full symbolic rebuild (independent of round 11's file, own
`sympy` session).** Rebuilt `\mathrm{Num},\mathrm{Den},n_1,n_2` completely
from scratch (own script, not copying round 11's displayed polynomials):
same substitution `u=\tan(A/6)\to x,y\to$ triple-angle `\to\cos A,\sin A\to`
`K_c,P,Q,f,G,\beta_0\to\mathrm{RHS}\to(1+\cos B)^2X_0-\mathrm{RHS}^2`,
cleared denominators via `\texttt{sympy.together}/\texttt{fraction}`.
Confirms round 11's reported shapes exactly: `\deg_u\mathrm{Num}=34`,
`\mathrm{Den}=-16(u^2+1)^{14}h` (round 11 reports `-256`, a difference of an
overall positive constant `16` from a different, equally valid, denominator-
clearing convention — this does not affect any sign statement, since both
conventions clear the same rational function up to a positive factor;
verified directly that `\mathrm{Num}/\mathrm{Den}` computed either way
equals `(1+\cos B)^2X_0-\mathrm{RHS}^2` to machine precision at 5 fresh
random samples), `\deg_un_1=10` with denominator `-4(u^2+1)^2h`,
`\deg_un_2=6$ with denominator `-2h` — matching round 11's structure exactly
component-for-component, now derived independently rather than reused.

**Step B — Theorem 1 (see Promotable lemmas above), the round's headline
result.** Discovered and proved the exact factorization
`h=-(1+u^2)^3\sin(A+B)` (round 11 had only *conjectured*, via numeric sign-
consistency across `500{,}000` samples, that `h\propto(u^2+1)^6\sin(A+B)`
for an unidentified constant — an incorrect guess at the exponent, `6`
instead of the correct `3`; a first numeric attempt at this exponent by this
round's builder, using the wrong exponent `6`, gave a non-constant "ratio"
across sample points, `\approx-0.993$ to `-0.995` at small `A,B$ but drifting
to `\approx-0.89` at larger `A,B$ — this discrepancy was the clue that the
guessed exponent was wrong; switching to `3` and rechecking symbolically
resolved it exactly). This proves `\mathrm{Den},\mathrm{den}_1,\mathrm{den}_2
>0` unconditionally (any triangle), upgrading round 11's numeric-only claim
to a full proof, and is the round's one genuinely new, certified,
promotable result.

**Step C — hand Positivstellensatz search, as dispatched: result is
negative/inconclusive, with the precise obstruction documented (not just
"didn't find one").**

1. *Degree-mismatch obstruction (the central finding).* `\mathrm{Num}` has
   `\deg_u=34`; `n_1,n_2` have `\deg_u=10,6`. To cancel `\mathrm{Num}`'s
   leading `u^{34}` term using `\lambda_1n_1$ or `\lambda_2n_2` as literally
   proposed in the outline's Step 2 ("`\lambda_i` a low-degree polynomial
   with a handful of unknown rational coefficients") requires `\lambda_1$ of
   `\deg_u=24` or `\lambda_2$ of `\deg_u=28$ — **not** a "handful of
   coefficients" ansatz: a degree-`24` (resp. `28`) polynomial in `u` with
   coefficients that are themselves polynomials in `(\cos B,\sin B)` up to
   total degree `\approx2$ (to match `\mathrm{Num}`'s joint degree `3` in
   `(\cos B,\sin B)` after accounting for `n_1,n_2`'s own degree-`1`
   dependence) has on the order of `25\times4\approx100$ free rational
   coefficients — a genuine large-scale linear system, not a small hand
   ansatz. This is a concrete, checked obstruction (computed the exact
   leading-coefficient polynomials of `\mathrm{Num},n_1,n_2$ in `u$,
   confirming the degree gap directly), not a vague impression.
2. *Leading-coefficient inspection.* `\mathrm{Num}$'s `u^{34}` coefficient
   is `-\sin B\,(4\cos^2B-12\cos B\sin B+8\cos B-9\sin^2B-12\sin B+4)`; its
   `u^0$ coefficient is the *negative* of this same polynomial (an exact,
   checked coincidence — not a general palindromic/anti-palindromic symmetry
   of the full polynomial, which was checked and found **false**:
   `\mathrm{Num}(u)\ne\pm u^{34}\mathrm{Num}(1/u)$ as polynomials, confirmed
   by direct symbolic comparison). Numerically, this leading-coefficient
   polynomial is **not** sign-definite over the full range `B\in(0,\pi)`
   (own `2{,}000`-sample sweep: range `[-2.27,17.14]`), but **is** strictly
   positive (range `\approx[5.5,17.1]`) when `B$ is restricted to the
   plausible Case-(b) range `B\in(0.8,1.5)$ (own `5{,}000`-sample sweep) —
   consistent with, but far from a proof of, `\mathrm{Num}\ge0` on the true
   domain.
3. *Numerical division instability (methodological finding, recorded to
   save a future round the same trap).* Attempted floating-point polynomial
   long division (`\texttt{numpy.polydiv}`) of `\mathrm{Num}` by `n_1` (then
   the remainder by `n_2`) at several sample `(\cos B,\sin B)` values: this
   is **numerically unstable at this degree** — reconstructing
   `\mathrm{Num}` from the computed quotients/remainder gave values off by
   `10^{16}$–`10^{17}$ from the true (small, `O(1)`–`O(10)`) value of
   `\mathrm{Num}` at every sample tried (`6` samples, `100\%` failure of the
   naive floating-point approach) — a genuine numerical-conditioning
   failure of naive long division at `\deg=34$ with widely-varying
   coefficient magnitudes, not a bug in the setup (confirmed the direct
   evaluation of `\mathrm{Num}$ itself at the same points is well-behaved,
   `O(1)$–`O(10)`, only the division-based reconstruction blows up).
   **Do not use floating-point long division at this degree; use exact
   rational arithmetic instead.**
4. *Exact rational division (verified to work mechanically, but unwieldy).*
   Repeated the division exactly (`sympy`, exact rationals, at a sample
   rational point `\cos B=3/5,\sin B=4/5$): `\deg_ur_1=9<10=\deg_un_1$ and
   `\deg_ur_2=5<6=\deg_un_2` as required, and the reconstruction
   `q_1n_1+q_2n_2+r_2$ was confirmed to equal `\mathrm{Num}` exactly at the
   sample `u`-value tested — so the division mechanics are well-defined and
   correct, but the resulting quotient polynomials `q_1,q_2` have
   `\sqrt3$-and-rational coefficients with numerator/denominator integers in
   the `10^{20}$–`10^{50}` range even at this single sample point — **far
   too large and un-patterned for hand inspection or a plausible closed-form
   guess**. This rules out "read off the pattern from one sample" as a
   viable route at this degree.
5. *`\mathtt{sympy.factor}` on the full symbolic `\mathrm{Num}`.* Ran (under
   2 minutes): returns the polynomial unfactored (no nontrivial common
   factor, confirming round 11's same finding independently on this round's
   own re-derived `\mathrm{Num}`).
6. *cvxpy is, in fact, installable in this environment* — contrary to the
   dispatch's premise (`pip install cvxpy` succeeded in under two minutes,
   network available). **This does not mean an SDP-based certificate was
   found or attempted to completion this round.** Setting up a genuine
   multivariate Positivstellensatz SDP for this problem correctly requires:
   (i) a monomial basis for `u$ of half-degree `\approx17$ (since
   `\deg_u\mathrm{Num}=34`) crossed with a basis for `(\cos B,\sin B)$ of
   half-degree `\approx1$–`2$ (`\approx50$ monomials total, a `50\times50`
   Gram-matrix PSD variable, or several such for the `\sigma_0,\lambda_1,
   \lambda_2` pieces); (ii) correctly encoding the equality constraint
   `\cos^2B+\sin^2B=1` (as a free-sign polynomial multiplier of degree
   matching the rest, a genuine ideal-membership term, not itself required
   SOS); (iii) additionally encoding `\angle B\le\angle C` — **which is
   not yet reduced to a polynomial condition in `(u,\cos B,\sin B)` alone**
   (see the newly-identified open item below) — as a further domain
   constraint; and (iv), critically, **extracting an exact rational
   certificate from the numerical SDP solution and re-verifying it by exact
   symbolic expansion** (a numerical SDP "solved" flag is not, by itself, a
   proof — CLAUDE.md's rigor rules require the written proof stand on its
   own). This is a substantial, multi-step undertaking that was not
   completed this round given the remaining time after Steps A–B; it is
   recommended, precisely scoped, as next round's concrete task if this
   route is pursued further, rather than left as a vague "try SOS" note.

**New item, not previously flagged this precisely: the `\angle B\le\angle C`
condition is transcendental, not yet algebraic.** All prior rounds'
`(u,\cos B,\sin B)$ semialgebraic description of Case (b) (`u\in(0,2-\sqrt3)`,
`n_1>0`, `n_2>0`) omits this fourth domain condition, `B\le(\pi-A)/2`, which
mixes `B` (via `\cos B,\sin B`) and `A` (via `u=\tan(A/6)`) transcendentally
— it is **not** currently expressed as a polynomial inequality in
`(u,\cos B,\sin B)` alone. A further Weierstrass substitution on `B` (e.g.
`v:=\tan(B/2)`) would make `\cos B,\sin B$ rational in `v`, but comparing
`A$ (via `u`) and `B$ (via `v`) still requires expressing `\cos(A/2)` (not
just `\cos(A/3)`) rationally in `u`, which — since `A/2=3\cdot(A/6)$ is a
triple angle of `t=A/6`, while `u=\tan t`, not `\cos t,\sin t` — needs
`\cos t,\sin t$ themselves, which are `\pm1/\sqrt{1+u^2}$ and
`\pm u/\sqrt{1+u^2}$: genuinely irrational in `u` (a real, if mild,
algebraic extension `w:=\sqrt{1+u^2}`, not further reducible). This is a
concrete, previously-unrecorded gap in the semialgebraic domain description,
left open for a future round: either incorporate `w=\sqrt{1+u^2}` as an
additional generator with the relation `w^2=1+u^2` (still algebraic, just
one dimension larger), or find a different route to express `\angle B\le
\angle C` polynomially.

**Net assessment.** This round's genuine, fully rigorous contribution is
Theorem 1 (the exact `h=-(1+u^2)^3\sin(A+B)` identity and the consequent
proof that `\mathrm{Den},\mathrm{den}_1,\mathrm{den}_2>0` unconditionally),
upgrading round 11's numeric-only semialgebraic reformulation to a fully
proved equivalence. The dispatched hand Positivstellensatz search did
**not** find a certificate; the negative/inconclusive findings are precisely
documented (degree-mismatch obstruction, numerical-instability trap, exact-
division unwieldiness, and a newly-identified additional gap — the
`\angle B\le\angle C` condition's own non-algebraic status) rather than left
as a bare "didn't work." `\mathrm{Num}\ge0}` (equivalently `(\star)`) remains
open.

## Open gaps (updated)
1. `\mathrm{Num}\ge0` on Case (b)'s domain (equivalently `(\star)`) — not
   proved. A genuine Positivstellensatz/SOS certificate search was
   attempted by hand this round and did not succeed; the concrete
   obstruction (degree mismatch requiring `\approx100`-coefficient
   multiplier polynomials) is documented in Step C above. A real SDP-based
   search (cvxpy, now confirmed installable) is the recommended next
   attempt, but constructing and rigorously (exactly) verifying such a
   certificate is a substantial task not completed this round.
2. The `\angle B\le\angle C` domain condition is not yet expressed as a
   polynomial inequality in `(u,\cos B,\sin B)` alone (newly identified this
   round) — needed to fully specify Case (b)'s domain algebraically before
   a complete Positivstellensatz set-up is possible. **CLOSED this round**
   — see Theorem 2 below, which gives an exact, rigorously proved
   polynomial encoding via the extra generator `w:=\sqrt{1+u^2}`.
3. `\mathrm{Den},\mathrm{den}_1,\mathrm{den}_2>0` — **now fully proved**
   (Theorem 1), no longer an open item (upgraded from round 11's numeric-
   only status).

### Round 13 (this round) — the `w=\sqrt{1+u^2}` polynomial encoding of
`\angle B\le\angle C` (fully proved, closes open item 2), plus a refined,
well-conditioned re-examination of the 2-/3-multiplier Positivstellensatz
ansatz that both reconfirms the explorer's infeasibility finding and
uncovers a concrete new diagnostic pointing at the missing generator.

**Dispatch.** This was a lower-priority build slot. Per the dispatch, the
confirmed-dead minimal 2-multiplier ansatz `\mathrm{Num}=\sigma_0+
\lambda_1n_1+\lambda_2n_2` was **not** re-attempted as-is. Instead this
round (a) closes the `\angle B\le\angle C` polynomial-encoding gap the
explorer and round-12's file both flagged as the concrete prerequisite for
a genuine 3-/4-multiplier attempt, and (b) uses the resulting better-
conditioned rescaled basis to re-run the 2-/3-multiplier SDP (now including
the `u`-domain-bound multiplier `n_3`) at multiple domain points, cleanly
resolving the explorer's own "inconclusive due to solver limitations"
verdict on that specific narrower question (the `n_3`-augmented ansatz),
and produces a new, concrete diagnostic about where the missing information
actually lives.

**Theorem 2 (new, fully proved) — polynomial encoding of `\angle B\le
\angle C`.** With `u=\tan(A/6)` as in Theorem 1, define
`$$w:=\sqrt{1+u^2}\ (>0),\qquad n_4(u,w,\cos B):=w^3\cos B-u(3-u^2).$$`
Then, on Case (b)'s domain (`A\in(0,\pi/2]`, so `t:=A/6\in(0,\pi/12]`, and
`B\in(0,\pi)`, `C=\pi-A-B$),
$$\angle B\le\angle C\iff n_4(u,w,\cos B)\ge0,$$
where `w` is subject to the single extra algebraic relation `w^2=1+u^2`
(and `w>0`), so `n_4\ge0` is a genuine polynomial condition on the extended
variable set `(u,w,\cos B,\sin B)`.

*Proof.* `\angle B\le\angle C\iff B\le C=\pi-A-B\iff B\le\tfrac{\pi-A}2=
\tfrac\pi2-\tfrac A2`. Since `B\in(0,\pi)` and, for `A\in(0,\pi/2]`,
`\tfrac\pi2-\tfrac A2\in[\tfrac\pi4,\tfrac\pi2)\subset(0,\pi)`, both angles
being compared lie in `(0,\pi)`, on which `\cos` is strictly decreasing
(hence injective); therefore
$$B\le\tfrac\pi2-\tfrac A2\iff\cos B\ge\cos\bigl(\tfrac\pi2-\tfrac A2\bigr)
=\sin\tfrac A2.$$
(No extra precondition such as `B<\pi/2` is needed here — unlike the
population's other `\cos`-monotonicity lever `B\le C\iff\cos A\ge2\cos^2B-1`,
which this round's outline-reviewer correctly flagged as needing `B<\pi/2`
— because here *both* compared angles are shown directly to lie in the
full injectivity interval `(0,\pi)` for `\cos`, with no restriction on `B$
itself required.) It remains to express `\sin(A/2)` polynomially in `u,w`.
Write `t:=A/6`, so `\cos t=1/w`, `\sin t=u/w` (valid since `w=\sqrt{1+u^2}
=\sec t>0`, as `t\in(0,\pi/12]\subset(0,\pi/2)$ gives `\cos t>0`, and
`u=\tan t\ge0` gives `\sin t\ge0`). Since `A/2=3t`, the triple-angle
formula gives
$$\sin\tfrac A2=\sin3t=3\sin t-4\sin^3t=\frac{3u}w-\frac{4u^3}{w^3}
=\frac{3uw^2-4u^3}{w^3}.$$
Substituting `w^2=1+u^2`: `3uw^2-4u^3=3u(1+u^2)-4u^3=3u-u^3=u(3-u^2)`, so
$$\sin\tfrac A2=\frac{u(3-u^2)}{w^3}.$$
(This was independently verified as an **exact symbolic identity, not
merely numeric**: substituting `\cos t=1/w,\sin t=u/w` into the triple-angle
formulas for `\cos3t,\sin3t` and reducing the difference against the
claimed closed forms `(1-3u^2)/w^3,\ u(3-u^2)/w^3` modulo the ideal
generator `w^2-(1+u^2)$ — via exact polynomial division in `w` — gives
remainder `0` in both cases, own fresh `sympy` session. A parallel 5-point,
30-digit `mpmath` numeric check, independent of the symbolic computation,
agreed to `<4\times10^{-17}` absolute error in every case.) Since `w^3>0`,
$$\cos B\ge\sin\tfrac A2\iff w^3\cos B\ge u(3-u^2)\iff n_4:=w^3\cos B-
u(3-u^2)\ge0.$$
Chaining the two displayed equivalences proves the theorem. `\blacksquare`

**Independent large-scale numeric confirmation (not part of the proof, a
corroborating sanity check of the closed-form target only).** Own fresh
Python/`mpmath` script, `200{,}000` uniform random `(A,B)$ samples with
`A\in(0,\pi/2)`, `B\in(0,\pi-A)` (no other domain restriction imposed, i.e.
testing the identity in maximal generality beyond Case (b) itself): compared
`B\le C` directly (via `C=\pi-A-B`) against `n_4(u,w,\cos B)\ge0` computed
from the closed form — **`0/200{,}000` mismatches**. This corroborates
Theorem 2's proof (which is unconditional in `A,B` beyond `A\le\pi/2`) at
scale, though the symbolic proof above is what makes the claim rigorous,
not the sampling.

**Refined Positivstellensatz feasibility study (own `cvxpy` session,
CLARABEL + SCS, independent of the round's `math-explorer-sdp` transcript
— same general method, but with two concrete methodological upgrades).**

*Upgrade 1 — proper affine rescaling fixes the conditioning wall the
explorer hit at the 3-multiplier ansatz.* The explorer's `u=0.2t` rescaling
left `\mathrm{Num}`'s coefficients spanning `\approx16` to `\approx2\times
10^9` (a `1.3\times10^8` dynamic range) even after rescaling, which broke
SCS/CLARABEL convergence for the 3-multiplier and higher-degree attempts.
Using instead the affine map that sends the true domain interval
`u\in(0,2-\sqrt3)` exactly onto `s\in(-1,1)$ (`u=\tfrac{2-\sqrt3}2(s+1)`,
own `sympy` session, at two fixed representative domain points), the
resulting `\mathrm{Num}(s)`'s coefficient range collapses to `\approx3\times
10^{-29}` (numerical noise, effectively `0`) to `\approx16$–`24` — a
`\lesssim10^2` dynamic range, dramatically better conditioned. **With this
fix, both CLARABEL and SCS now converge cleanly** (no failures, no
oscillation) on the `\deg\le34` 3-multiplier ansatz (`\sigma_0` half-degree
`17`, `\lambda_1$ half-degree `12`, `\lambda_2` half-degree `14`, `\lambda_3
$ half-degree `16`, `n_3:=u(2-\sqrt3-u)\ (\iff\cos A\ge0)`, `\approx535`
total SDP variables) at every point tested — resolving the explorer's own
"SCS failed to converge... CLARABEL errored out" report for exactly this
ansatz size, purely via basis choice, with no change to the mathematical
content of the ansatz itself.

*Finding 1 — the 3-multiplier ansatz's feasibility is genuinely
point-dependent, and this round reconfirms infeasibility at the explorer's
own witness point, now cleanly (not inconclusively).* At the explorer's
domain point `(A,B)\approx(0.603,1.269)` (`\mathrm{Num},n_1,n_2,n_4$ all
independently re-verified `>0$ there, i.e. a genuine Case-(b) point):
maximizing slack `t` in `\mathrm{Num}-t=\sigma_0+\lambda_1n_1+\lambda_2n_2
(+\lambda_3n_3)`, both solvers converge to `t^*\approx-1.5489` — **with**
`n_3` included and **without** it, to `4$-`5` significant figures identical
in each case (`-1.548873` CLARABEL / `-1.548882` SCS without `n_3`;
`-1.548873`/`-1.548886` with `n_3`). Since `t^*<0`, the exact identity
(`t=0`) is infeasible: **the 3-multiplier ansatz (`n_1,n_2,n_3`) is, like
the 2-multiplier one, genuinely infeasible at this point — now confirmed
with a well-conditioned, cleanly-converging computation rather than the
explorer's own inconclusive attempt**, and `n_3` (the `\cos A\ge0$
generator) makes essentially **no** difference to the achievable slack at
this point.

*Finding 2 — feasibility is NOT infeasible everywhere: a near-corner
witness point is feasible.* At a second domain point close to the known
`(A^*,B^*)$ corner, `(A,B)=(0.42,0.92)` (`n_1\approx0.0063,n_2\approx0.0061,
n_4\approx0.400$, all `>0`, so genuinely in Case (b), and near the tight
corner where `\mathrm{Num}$'s own margin is small, `\mathrm{Num}\approx
0.033$), the **same** 2-/3-multiplier ansatz is **feasible**: `t^*\approx
+0.2376` (both solvers agree to `5` significant figures, with or without
`n_3`). This shows the minimal ansatz's infeasibility is not a uniform
phenomenon — it can succeed at some domain points and fail at others.
**This does not weaken the negative conclusion**: since a genuine *global*
Positivstellensatz certificate needs a single pair of polynomials
`\lambda_1(u,\cos B,\sin B),\lambda_2(u,\cos B,\sin B)` (not
independently re-optimized per point) that work simultaneously at every
domain point, and restricting any such global certificate to one fixed
`(\cos B,\sin B)` value gives exactly the per-point SDP solved here,
**infeasibility at even one point (as independently reconfirmed at
`(0.603,1.269)` above) already rules out the existence of a global
2-/3-multiplier certificate of these minimal degrees** — this round's
Finding 2 refines, but does not overturn, that conclusion; it shows the
obstruction is localized rather than everywhere.

*Finding 3 — a concrete diagnostic pointing at the missing generator.* At
the infeasible witness point `(0.603,1.269)`, the newly-derived `n_4`
(Theorem 2, the `\angle B\le\angle C` condition) evaluates to `n_4\approx
0.000287` — **three orders of magnitude smaller than `n_1\approx0.0276` and
four orders smaller than `n_2\approx0.323`** at the same point, i.e. this
witness point sits almost exactly ON the `\angle B\le\angle C` boundary
(`B$ is barely `\le C` there), while comfortably inside the `n_1,n_2$
boundaries. Since `n_1,n_2` (and `n_3`) carry essentially no information
about proximity to the `n_4=0$ boundary, an ansatz built only from them has
no way to "see" that this point's positivity of `\mathrm{Num}` is aided by
being near a *different*, omitted domain constraint — a plausible
mechanistic explanation for why exactly this point is the hard one for the
minimal ansatz. **This is offered as a diagnostic, not a proof**: a
complementary scan at fixed `B=1.269$ varying `u$ over the whole
`\cos A\ge0` range (own script) shows `\mathrm{Num}\ (=S)$ in fact stays
positive well beyond where `n_4$ turns negative at that particular `B$-slice
(`\mathrm{Num}>0` continues from `u\approx0.09$ to `u\approx0.245`, while
`n_4$ turns negative already at `u\approx0.107`), so `n_4$'s zero-crossing
is **not** locally where `\mathrm{Num}$ itself changes sign along that
one-dimensional slice — meaning the connection between the witness point's
smallness of `n_4` and the ansatz's infeasibility there is suggestive, not
established. Whether including `n_4$ (via the bivariate `(u,w)$ SOS
extension Theorem 2 makes possible) restores feasibility at
`(0.603,1.269)` was **not tested this round** — it requires a genuinely
larger bivariate `(u,w)$ Gram-matrix SDP (with an additional free-sign
multiplier for the ideal relation `w^2-1-u^2=0`), which is a substantial
setup not completed in the remaining time budget; it is the concrete,
well-motivated next computational step for a future round.

**Net assessment.** This round (a) fully closes round 12's open item 2 —
the `\angle B\le\angle C` domain condition now has a rigorously proved
polynomial encoding (Theorem 2, `n_4$ via the algebraic extension `w=
\sqrt{1+u^2}$, both symbolically derived with zero remainder and
numerically corroborated at `200{,}000` samples); (b) upgrades the
explorer's own "inconclusive due to solver limitations" verdict on the
3-multiplier (`n_1,n_2,n_3`) ansatz to a clean, well-conditioned,
two-solver-confirmed result: it is genuinely infeasible at the same
witness point the 2-multiplier ansatz failed at, and `n_3$ contributes
essentially nothing there — narrowing, not just re-confirming, the
population's understanding of which generators matter; (c) discovers that
this infeasibility is point-dependent (feasible at a second, corner-
adjacent witness point), refining rather than overturning the negative
conclusion, since one infeasible point already rules out a global minimal
certificate; and (d) identifies, but does not resolve, a concrete
diagnostic (the infeasible witness point's near-degeneracy in the newly
available `n_4` constraint) suggesting — without proving — that the
4-generator (`n_1,n_2,n_3,n_4`) bivariate `(u,w)` Positivstellensatz is the
right next object to attempt. `\mathrm{Num}\ge0` (equivalently `(\star)`)
remains open. No overclaiming: none of this round's findings closes the
central gap; they close one previously-flagged prerequisite (the `\angle
B\le\angle C` polynomial encoding) and sharpen, with better tooling and two
new witness points, the population's diagnostic picture of the
Positivstellensatz search.

**Watch out for (recorded for future rounds, in addition to round 12's
list).** (iv) Use the affine rescaling `u=\tfrac{2-\sqrt3}2(s+1)$ (mapping
the true domain interval exactly onto `[-1,1]`), not an ad hoc linear
rescale — this alone fixes the `\sim10^8`–`10^9` coefficient dynamic range
that broke SCS/CLARABEL on the raw-`u` basis, without changing the
mathematical ansatz at all. (v) A per-point SDP feasibility test is only a
*necessary* condition for a global certificate (infeasibility at one point
kills the global claim; feasibility at one point proves nothing about
other points) — do not conclude "certificate exists" from one feasible
point, and do not conclude "no certificate of any degree exists" from one
infeasible point at *minimal* degree only (higher degree might still work).
(vi) `n_4$ (Theorem 2) requires the extra generator `w=\sqrt{1+u^2}$ with
relation `w^2=1+u^2` — a genuine (if mild) algebraic field extension of the
`(u,\cos B,\sin B)` ring, needed because `A/2=3\cdot(A/6)` is an *odd*
multiple of the angle whose tangent is `u`, and odd-multiple-angle formulas
are not rational in the tangent alone (only even multiples are, via the
usual Weierstrass substitution) — this is a structural fact, not a
workaround failure, and any future Positivstellensatz attempt including
`n_4` must set up the SOS machinery in the extended ring `(u,w,\cos B,\sin
B)/(w^2-1-u^2)`, not in `(u,\cos B,\sin B)` alone.

### Round 14 (this round) — RECONCILIATION of round 13's monomial-basis
"infeasible" (`t^*\approx-1.549`) against the round-14 explorer's Chebyshev-
basis "feasible" (`t^*\approx+1.6$–`6\times10^{-5}`) claims at the same
witness point `(A,B)\approx(0.603,1.269)`, via an **exact, non-numeric**
counterexample. **Verdict: round 13 was right; the explorer's positive-slack
finding was a numerical artifact of its SDP setup, not a real feasible
point.**

**Method.** Rather than trust either SDP run (both near the noise floor per
the dispatch's own caution), I rebuilt `\mathrm{Num},n_1,n_2` completely
from scratch (own fresh `sympy` session, own `together`/`fraction`
denominator-clearing, not reusing any file's or explorer's displayed
polynomials) and independently reproduced the exact same structural facts
already on record: `\deg_u\mathrm{Num}=34`, `\mathrm{den}=-16(u^2+1)^{14}h`
with the same `h`, `\deg_un_1=10`, `n_1$'s denominator `-4(u^2+1)^2h`,
`\deg_un_2=6`, `n_2$'s denominator `-2h` — matching round 12/13's file
character-for-character, confirming those polynomials are being built
correctly. Then, instead of an SDP (which is only ever a *sufficient*-
condition search for a specific certificate form and is exactly what's in
dispute), I asked the *prior*, more basic question directly: **is
`\mathrm{Num}(u)\ge0` actually true whenever `n_1(u)\ge0` and `n_2(u)\ge0`,
at this exact `B`** — a question answerable by exact algebra, with no SDP
and no floating-point ambiguity at all.

**Exact rational witness point (fully rigorous, zero floating point).**
Rationalized `B\approx1.269` via `\tan(B/2)=1383/1879$, giving exact
`\cos B=808976/2721665`, `\sin B=2598657/2721665` (own `sympy` construction,
`\cos^2B+\sin^2B=1` exactly, `B=2\arctan(1383/1879)\approx1.269000132`,
matching the disputed witness to `4` decimal places). Substituting these
exact rationals into `\mathrm{Num}(u),n_1(u),n_2(u)` gives univariate
polynomials in `u` alone with coefficients in `\mathbb Q(\sqrt3)` (`\mathrm{Num},
n_1`) or `\mathbb Q` (`n_2`, as Theorem 1's remark already predicted). At the
exact rational point `u=1/4` (own `sympy`, `sp.Rational`, no `float`
anywhere in the computation):
$$n_1\Bigl(\tfrac14\Bigr)=\frac{1441832575281}{2853872599040}+\frac{15721829709\sqrt3}{35673407488}\approx1.2686>0,$$
$$n_2\Bigl(\tfrac14\Bigr)=\frac{2669124911349663387119}{82577922596748306944000}\approx0.0323>0\ \ (\text{a pure rational, exactly as Theorem 1 predicts}),$$
$$\mathrm{Num}\Bigl(\tfrac14\Bigr)=-\frac{113514130801596539362512787832455086285503}{5950366422971925385220556329880387584000}+\frac{32767230334161893655943225321974516839\sqrt3}{2975183211485962692610278164940193792}\approx-0.00086<0.$$
Sympy's `is_negative`/`is_positive` on these exact `\mathbb Q(\sqrt3)`
expressions (an exact algebraic-number sign test, via minimal-polynomial/
norm methods, not a floating evaluation) confirms every sign claimed above;
independently corroborated at `50`-digit precision (`\mathtt{sympy.N}`,
`\approx-0.00085965755\ldots$).

**This is a decisive, fully rigorous counterexample.** At `u=1/4$ (this
exact `B`): `n_1>0` and `n_2>0`, yet `\mathrm{Num}<0`. Since any
Positivstellensatz representation `\mathrm{Num}=\sigma_0+\lambda_1n_1+
\lambda_2n_2` with `\sigma_0,\lambda_1,\lambda_2` SOS (hence `\ge0`
everywhere on `\mathbb R`) would force `\mathrm{Num}\ge0` at every point
where `n_1\ge0` and `n_2\ge0` — this single exact witness **proves, for
ALL degrees, not just the degree round 13 or the explorer tested, that no
2-generator (`n_1,n_2`-only) Positivstellensatz certificate for
`\mathrm{Num}\ge0` can exist at this `B`.** This upgrades round 13's
numerical "infeasible at degree `\approx17`" finding to an **unconditional,
symbolic non-existence proof** for the minimal ansatz (a strictly stronger
and more useful conclusion than either SDP run individually could give).

**Locating the true minimum confirms round 13's exact number was correct,
not noise.** A high-precision (`60`-digit `mpmath`) golden-section search
for `\min_{u\in[r_1,r_2]}\mathrm{Num}(u)$, where `r_1\approx0.09123` (`n_1$'s
only root in `(0,2-\sqrt3)`) and `r_2\approx0.25607` (`n_2$'s only root in
`(0,2-\sqrt3)`) bound the interval `\{n_1\ge0\}\cap\{n_2\ge0\}` at this `B`
(confirmed by evaluating `n_1,n_2` at sample points in each of the three
subintervals `(0,r_1),(r_1,r_2),(r_2,2-\sqrt3)$ cut out by their roots — only
the middle one has both `>0`), finds the minimum is attained **at the right
endpoint** `u\to r_2^-` (i.e. `\mathrm{Num}` decreases monotonically toward
the `n_2=0` boundary over the relevant range), with value
$$\min_{[r_1,r_2]}\mathrm{Num}\approx-1.54887600273723620680\ldots$$
— matching round 13's reported SDP optimal values (`-1.548873`/
`-1.548882`/`-1.548886` across solvers/ansätze) to **5–6 significant
figures**. This is not a coincidence: round 13's SDP was (correctly)
converging toward the true achievable slack, which is essentially pinned
by `\mathrm{Num}$'s actual minimum over the naive `\{n_1\ge0,n_2\ge0\}`
domain (the SOS multiplier terms cannot do better than trivially matching
`\mathrm{Num}` at its worst point in this domain). **This independently
confirms round 13's number was a real, correct signal, not solver noise —
the opposite of what the round-14 explorer's contradictory result
suggested.**

**Diagnosis of the round-14 explorer's error.** Since the true infeasibility
margin at this witness point is `O(1)` (`\approx-1.549$, or at minimum
`\approx-0.86$ elsewhere per round 12's leading-coefficient sweep) — nowhere
near a numerical noise floor — **a correctly-posed SDP for this exact
2-generator ansatz cannot report a genuine near-zero positive optimal
value**; any such report reflects an error in problem setup, not
conditioning. I do not have access to the round-14 explorer's own script to
identify the exact line, but the mathematical conclusion is unaffected by
this: whatever the explorer's Chebyshev-basis code computed, it was **not**
a correct feasibility certificate for `\mathrm{Num}=\sigma_0+\lambda_1n_1+
\lambda_2n_2` at this witness `B`, since we have proved by exact algebra
that this system is infeasible with a margin of order `1`, not `10^{-5}`.
(One plausible mechanism, offered as a hypothesis and not verified: if the
Chebyshev product-to-sum convolution or the `w^2\to1+u^2$-reduction step in
the 4-generator extension had even a small indexing/degree-truncation bug,
the "reconstructed identity" check the explorer performed — comparing
`\sigma_0+\lambda_1n_1+\lambda_2n_2` against `\mathrm{Num}-t` on a `2000`-
point grid with residual `\approx7\times10^{-7}` — could pass while
silently checking a *slightly wrong* polynomial (e.g. a truncated or
mis-scaled version of `\mathrm{Num}` itself, if the same conditioning bug
affected the "reference" values used in the residual check); this is
consistent with, but not proof of, the observed contradiction. Confirming
the exact bug would require the explorer's own code, not available to this
builder.)

**Consequence for the certificate search.** This closes the reconciliation
task cleanly: round 13's infeasibility conclusion is correct (indeed now
proved, not just numerically indicated); the round-14 explorer's
contradictory finding must be discarded as an artifact. It also sharpens
round 13's own Finding 3 diagnostic from a suggestive numeric correlation
into a **proven fact**: at this witness `B`, `n_4$ (Theorem 2's `\angle
B\le\angle C$ encoding) is strictly required. Direct exact check: at
`u=1/10` (well inside `n_1,n_2>0`, own `sympy.Rational` computation),
`n_4=27053627936065702617/10000000000000000000000\approx0.0027>0` and
`\mathrm{Num}\approx9.45>0` — i.e. restricting to the region where `n_4\ge0`
too (a proper subinterval `u\in(0.0912,0.1009)` of the naive
`(r_1,r_2)=(0.0912,0.2561)`, since `n_4` has its own root at
`u\approx0.1009` inside `(r_1,r_2)`) removes the counterexample at
`u=1/4$ (which has `n_4<0` there, exact check: `n_4(1/4)\approx-0.4088<0`,
own `sympy` computation, confirming this point genuinely lies outside Case
(b)'s true domain). **This is now a proved structural fact, not a
diagnostic guess: any valid Positivstellensatz certificate for
`\mathrm{Num}\ge0` on Case (b)'s domain must include `n_4` (or an
equivalent constraint that excludes this exact counterexample region) as a
generator — the 2-generator (`n_1,n_2`-only) ansatz is not merely
"hard to find a certificate for," it is unconditionally impossible.**

**Net assessment.** This round fully resolves the round-13/round-14
contradiction in round 13's favor, via an exact (non-numeric,
non-SDP) counterexample that is strictly more rigorous than either prior
SDP run: `n_1(1/4)>0`, `n_2(1/4)>0`, `\mathrm{Num}(1/4)<0` at the exact
rational witness `\cos B=808976/2721665,\sin B=2598657/2721665$ (matching
`B\approx1.269`), proved by exact `\mathbb Q(\sqrt3)$ algebraic-number sign
tests. This (a) proves, unconditionally and for all degrees, that no
2-generator (`n_1,n_2`) Positivstellensatz certificate for `\mathrm{Num}\ge0`
can exist — upgrading round 13's numeric finding to a theorem; (b)
identifies the round-14 explorer's contradictory finding as a numerical
artifact, not a genuine feasible point, since the true margin is `O(1)`,
far outside any plausible noise band; (c) upgrades round 13's Finding 3 from
a suggestive correlation to a proved fact: `n_4` is a *necessary* generator,
not an optional refinement. The central gap (`\mathrm{Num}\ge0` on the true,
`n_4`-including domain) remains open, but the terrain is now unambiguous:
any future certificate search must use the 4-generator (`n_1,n_2,n_3,n_4`)
bivariate `(u,w)` ansatz, not the minimal one — this is now a proved
requirement, not a hypothesis to test.

## Open gaps (further updated, round 14)
1. `\mathrm{Num}\ge0` on Case (b)'s domain (equivalently `(\star)`) — still
   not proved. **Round 14 upgrades this item's status**: the minimal
   2-generator (`n_1,n_2`-only) ansatz is now **proved (not just
   numerically indicated) unconditionally infeasible at every degree**, via
   an exact `\mathbb Q(\sqrt3)` counterexample (`u=1/4$ at the witness `B`:
   `n_1>0,n_2>0,\mathrm{Num}<0`) — so this ansatz is no longer even worth
   revisiting at higher degree; the reconciliation task (was this round 14's
   Chebyshev "feasible" finding or round 13's monomial "infeasible" finding
   correct?) is **closed**, in round 13's favor. `n_4` is now proved (not
   merely diagnosed) to be a *necessary* generator. A 4-generator ansatz
   including `n_4` (Theorem 2) in the bivariate `(u,w)` extension remains
   the concrete recommended next attempt, not yet built or tested — but now
   it is known to be *necessary*, not merely a plausible improvement, which
   focuses the search.
2. ~~The `\angle B\le\angle C` domain condition is not yet expressed as a
   polynomial inequality~~ — **CLOSED this round, Theorem 2**: fully
   proved polynomial encoding `n_4(u,w,\cos B)=w^3\cos B-u(3-u^2)\ge0` in
   the extended ring `(u,w,\cos B,\sin B)/(w^2-1-u^2)`.
3. `\mathrm{Den},\mathrm{den}_1,\mathrm{den}_2>0` — fully proved (Theorem
   1, round 12), not an open item.
4. (New, round 13.) The bivariate `(u,w)` Positivstellensatz SDP including
   `n_4` as a fourth generator — not set up or attempted this round
   (identified as the concrete next computational step; requires an
   SOS/Gram-matrix formulation in two variables plus a free-sign multiplier
   for the ideal relation `w^2-1-u^2=0`, a substantially larger undertaking
   than this round's univariate-in-`u` per-point tests).

## Promotable lemmas (round 13 addendum)

**New lemma (round 13), fully proved, zero symbolic residual — candidate
for certification as `lemmas/angle-b-le-c-weierstrass-encoding.md`:**

**Theorem 2.** With `u:=\tan(A/6)` as in the already-certified Theorem 1
(`lemmas/star-weierstrass-denominators-positive.md`), and `w:=\sqrt{1+u^2}
>0`, define
$$n_4(u,w,\cos B):=w^3\cos B-u(3-u^2).$$
Then, for `A\in(0,\pi/2]` and `B\in(0,\pi)` (Case (b)'s domain), with
`C:=\pi-A-B`,
$$\angle B\le\angle C\ \iff\ n_4(u,w,\cos B)\ge0,$$
subject only to the algebraic relation `w^2=1+u^2` (`w>0`) — a genuine
polynomial encoding in the extended ring `(u,w,\cos B,\sin B)/(w^2-1-u^2)`.

*Proof.* See the full derivation above (this file, Round 13 section,
"Theorem 2"): `\angle B\le\angle C\iff B\le\tfrac\pi2-\tfrac A2$, both
angles lying in `(0,\pi)` where `\cos` is injective, so this is equivalent
to `\cos B\ge\sin(A/2)`; with `t:=A/6`, `\cos t=1/w,\sin t=u/w` (both
positive on the relevant range), the triple-angle formula gives `\sin(A/2)
=\sin3t=u(3-u^2)/w^3` after reducing `3uw^2-4u^3` modulo `w^2=1+u^2`; since
`w^3>0`, `\cos B\ge u(3-u^2)/w^3\iff n_4\ge0`. The triple-angle reduction
was independently verified as an exact symbolic identity (own `sympy`
session: polynomial division of the difference `\cos3t-(1-3u^2)/w^3` and
`\sin3t-u(3-u^2)/w^3`, each times `w^3`, by the ideal generator
`w^2-(1+u^2)` in the variable `w`, gives remainder `0` in both cases), and
corroborated at `200{,}000` random samples (own script, `0` mismatches
against the direct trig definition of `\angle B\le\angle C`).
`\blacksquare`

This closes round 12's open item 2 (the `\angle B\le\angle C` domain
condition's polynomial encoding), a genuine prerequisite the round-13
outliner and outline-reviewer both flagged as needed before a complete
Positivstellensatz set-up for `\mathrm{Num}\ge0` is possible. It does not
by itself close the central gap (`\mathrm{Num}\ge0}`), which remains open.

**Also recorded (not proposed as a standalone lemma, but reusable
methodology):** the affine rescaling `u=\tfrac{2-\sqrt3}2(s+1)$ (exactly
mapping Case (b)'s `u$-domain onto `s\in[-1,1]$) reduces `\mathrm{Num}`'s
coefficient dynamic range from `\sim10^8$–`10^9$ (naive rescalings) to
`\lesssim10^2`, which is what let CLARABEL/SCS converge cleanly on the
3-multiplier ansatz this round where the round-13 explorer's own attempt
did not converge — recorded in "Watch out for" above (item iv) for any
future SDP attempt on this target.

## Promotable lemmas (round 14 addendum)

**New lemma (round 14), fully proved by exact `\mathbb Q(\sqrt3)` algebraic
computation (no floating point, no SDP) — candidate for certification as
`lemmas/n1n2-minimal-ansatz-unconditionally-infeasible.md`:**

**Theorem 3.** At the exact rational point `\cos B=\tfrac{808976}{2721665}`,
`\sin B=\tfrac{2598657}{2721665}` (a point on the unit circle,
`\cos^2B+\sin^2B=1` exactly, with `B=2\arctan\tfrac{1383}{1879}\approx
1.269000132`) and `u=\tfrac14$ (so `u\in(0,2-\sqrt3)`, a legitimate value of
`\tan(A/6)` for `A\in(0,\pi/2)`), the certified polynomials `\mathrm{Num},
n_1,n_2` (Theorem 1's Weierstrass reformulation) satisfy
$$n_1\Bigl(\tfrac14,\cos B,\sin B\Bigr)>0,\qquad
n_2\Bigl(\tfrac14,\cos B,\sin B\Bigr)>0,\qquad
\mathrm{Num}\Bigl(\tfrac14,\cos B,\sin B\Bigr)<0.$$
Consequently, **no** Positivstellensatz representation `\mathrm{Num}=
\sigma_0+\lambda_1n_1+\lambda_2n_2$ with `\sigma_0,\lambda_1,\lambda_2` sums
of squares (of any degree) can exist — the minimal 2-generator ansatz for a
certificate of `\mathrm{Num}\ge0` is **unconditionally impossible**, not
merely numerically hard to find.

*Proof.* Direct exact substitution (own `sympy` session, `sp.Rational`
throughout, no `float`) into the certified formulas for `\mathrm{Num},n_1,
n_2` (independently re-derived from scratch this round, matching round
12/13's file exactly: `\deg_u\mathrm{Num}=34`, `\deg_un_1=10`, `\deg_un_2=6`,
denominators `-16(u^2+1)^{14}h,-4(u^2+1)^2h,-2h` respectively, all
`>0$ unconditionally by Theorem 1, so sign of the numerator equals sign of
the original quantity) gives, exactly,
$$n_1=\frac{1441832575281}{2853872599040}+\frac{15721829709\sqrt3}{35673407488}\approx1.2686,$$
$$n_2=\frac{2669124911349663387119}{82577922596748306944000}\approx0.0323\ \ (\text{pure rational, no }\sqrt3),$$
$$\mathrm{Num}=-\frac{113514130801596539362512787832455086285503}{5950366422971925385220556329880387584000}+\frac{32767230334161893655943225321974516839\sqrt3}{2975183211485962692610278164940193792}\approx-0.00086.$$
Each sign was confirmed by `sympy`'s exact algebraic-number sign test
(`is_positive`/`is_negative`, which for elements of `\mathbb Q(\sqrt3)`
reduces to comparing rational bounds on `\sqrt3`, not a floating
evaluation) and independently corroborated at `50`-digit `\mathtt{sympy.N}`
precision. If `\sigma_0,\lambda_1,\lambda_2` were SOS polynomials (in `u$,
with coefficients allowed to depend on `\cos B,\sin B$, but evaluated here
at the fixed rationals above) satisfying `\mathrm{Num}=\sigma_0+
\lambda_1n_1+\lambda_2n_2` identically in `u`, then at `u=1/4$ we would have
`\sigma_0(1/4)\ge0$ (SOS `\Rightarrow` nonnegative everywhere on `\mathbb
R`), `\lambda_1(1/4)n_1(1/4)\ge0$ (since `n_1(1/4)>0` and `\lambda_1(1/4)\ge
0` by the SOS property), and likewise `\lambda_2(1/4)n_2(1/4)\ge0`, forcing
`\mathrm{Num}(1/4)\ge0` — contradicting the computed exact value `<0`.
`\blacksquare`

**Corollary (reconciliation of round 13 vs. the round-14 explorer,
established this round).** Theorem 3 proves round 13's numeric infeasibility
finding at witness `(A,B)\approx(0.603,1.269)` was correct in substance (the
minimal ansatz genuinely cannot work, at any degree), and identifies the
round-14 `math-explorer-sdp`'s contradictory small-positive-slack finding as
a numerical/setup artifact: since the true infeasibility gap is `O(1)`
(a golden-section search, own `60`-digit `mpmath` script, finds
`\min_{u\in[r_1,r_2]}\mathrm{Num}(u)\approx-1.548876$ at this same `B`,
matching round 13's reported SDP optimal values `-1.548873`/`-1.548882`/
`-1.548886` to `5$–`6` significant figures), no correctly-posed SDP for this
exact system could report a genuine near-`0` positive optimum; whatever the
Chebyshev-basis run computed was not a valid certificate for this system.
This also upgrades round 13's Finding 3 (the witness point sits near the
`n_4=0` boundary) from a numeric diagnostic to a **proved necessity**: exact
computation confirms `n_4(1/4,\cdot)\approx-0.4088<0` at the `u=1/4`
counterexample (outside Case (b)'s true domain) while `n_4(1/10,\cdot)
\approx0.0027>0$ inside it (own `sympy` exact computation both ways) — so
any valid certificate must include `n_4` as a generator, not merely
benefit from it.
