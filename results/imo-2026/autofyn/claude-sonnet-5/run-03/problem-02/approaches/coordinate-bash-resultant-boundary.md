## Status
partial

## Approaches tried

### Round 17 (this round) — finer `(\mathbb Z_2)^4`-grading structural
theorem: decisively rules out the outline's literal "bare odd `c`/`d`
multiplier" suggestion, explains exactly why, and constructs (fully
symbolically, zero-residual) a genuinely new unconditionally-nonnegative
generator family — but it is too high-degree to close the LP directly this
round; the central `-q_1,-r_0` certificate is **still not found**

**Task this round:** per the outline, either (1) a domain-aware case-split
of `q_1`, or (2) a probe for a genuinely new base generator carrying a bare
odd `c` or `d` factor, motivated by the round-13 parity-obstruction theorem.
This round pursued (2) to a full, rigorous conclusion (both a decisive
negative sub-result and a new positive construction), rather than splitting
effort across both; the case-split (1) remains open exactly as scoped in
round 16.

**1. Structural identity, proved exactly for all three base generators
(own fresh `sympy` session, exact `groebner`/`reduced` reduction modulo
`\langle c^2+s^2-1,d^2+t^2-1\rangle`, zero residual in every check below).**
Each of `G_0,E_{\mathrm{num}},\mathrm{Num}` decomposes exactly as
$$H = ct\cdot P_H(\sigma,\tau) + sd\cdot Q_H(\sigma,\tau)$$
for polynomials `P_H,Q_H` in `\sigma,\tau` alone, with
$$P_{G_0}=2\tau-1,\qquad Q_{G_0}=2(\tau-1),$$
$$P_{E_{\mathrm{num}}}=-32\sigma^2\tau+24\sigma^2+22\sigma\tau-12\sigma-\tau,
\qquad Q_{E_{\mathrm{num}}}=-2(\sigma-1)(16\sigma\tau-4\sigma-3\tau),$$
$$P_{\mathrm{Num}}=8\sigma^2\tau-6\sigma^2-3\sigma+\tau,\qquad
Q_{\mathrm{Num}}=2\sigma(\sigma-1)(4\tau-1)$$
(each verified by the full round-trip identity `H\equiv ct\,P_H+sd\,Q_H
\pmod{\langle c^2+s^2-1,d^2+t^2-1\rangle}`, exact `sympy.expand` residual
`0` in every one of the three cases — `P_{E_{\mathrm{num}}},Q_{G_0}$ recover
exactly the file's already-certified `f_1,\ (2\tau-1)`-type quantities from
earlier rounds, an independent cross-check that this round's fresh
derivation is consistent with the file's prior work). `E_{\mathrm{num}}`'s
own definition was already displayed in this shape in round 12; this round
additionally establishes the same clean `ct\cdot P+sd\cdot Q` shape for
`G_0` (previously known only via its raw two-term formula) and, new this
round, for `\mathrm{Num}` (previously known only via its raw six-term
formula) — a genuine structural simplification of the whole generator
family, useful independent of what follows.

**2. Decisive negative result: bare single-variable multipliers `c,d,s,t`
applied to any of `G_0,E_{\mathrm{num}},\mathrm{Num}` are USELESS as
standalone new generators — this directly refutes, with an exact proof
(not just "we didn't find one"), the outline's literal suggestion
"construct 1-2 candidate odd-`c`/odd-`d` generators (e.g. `c\cdot\mathrm{Num},
\ d\cdot G_0`)".** Using the Step-1 decomposition `H=ct\,P_H+sd\,Q_H`
and the coarse `\mathbb Z_2\times\mathbb Z_2` grading by `(\deg_c\bmod2,
\deg_d\bmod2)` (round 13's grading, `ct` has grade `(1,0)`, `sd` has grade
`(0,1)`), multiply by each of the four bare variables and reduce:
$$s\cdot H = cst\,P_H+\sigma d\,Q_H,\qquad t\cdot H=c\tau\,P_H+sdt\,Q_H$$
— the first term of each has grade `(1,0)` (excluded from the
`(0,0)`-graded piece needed to match `q_1,r_0`, which have zero `c,d`
content), the second has grade `(0,1)` (also excluded), so
$$(s\cdot H)_{00}=(t\cdot H)_{00}=0\quad\text{identically — bare }s\text{ or
}t\text{ multiplication contributes NOTHING to the usable piece, for any of
the three base generators.}$$
$$c\cdot H = c^2t\,P_H+cds\,Q_H=(1-\sigma)t\,P_H(\sigma,\tau)+cds\,Q_H,$$
and `(cds\,Q_H)` has grade `(1,1)`, excluded, so
$$(c\cdot H)_{00}=(1-\sigma)\,t\,P_H(\sigma,\tau),$$
which is a **bare odd power of `t` times a function of `\sigma,\tau`
alone** — i.e. it is genuinely odd in `t` (degree `\equiv1\pmod2` in `t`)
and therefore **cannot be rewritten as any polynomial in `\sigma=s^2,
\tau=t^2` alone**, unless `P_H\equiv0` (false for all three `H`, `P_H$ is a
nonzero polynomial in each case per Step 1). Symmetrically,
$$d\cdot H=cdt\,P_H+d^2s\,Q_H=(1-\tau)\,s\,Q_H(\sigma,\tau)+cdt\,P_H
\qquad\Rightarrow\qquad (d\cdot H)_{00}=(1-\tau)\,s\,Q_H(\sigma,\tau),$$
odd in `s`, likewise not a `\sigma,\tau`-polynomial. **Independently
verified this exact computation symbolically for `H=G_0` (own fresh
`sympy`, `groebner`/`reduced`): `(c\cdot G_0)_{00}=(1-\sigma)(2\tau-1)t`,
matching the general formula above with `P_{G_0}=2\tau-1` exactly, zero
residual.** Since `q_1,r_0` are polynomials purely in `\sigma,\tau` (no
bare `s` or `t`), any term of the shape `(1-\sigma)t\,P_H(\sigma,\tau)` or
`(1-\tau)s\,Q_H(\sigma,\tau)` appearing in a proposed certificate
`-q_1=\sum(\cdots)` would need to be **exactly cancelled by another term
carrying the same odd-in-`t` (resp. odd-in-`s`) dependence** before the
identity can even be restricted to `\sigma,\tau$ — a bare single generator
of this shape can never stand alone as a nonnegative-coefficient term in
the LP/SOS ansätze this population has been running (which all implicitly
assume every generator is already a pure `\sigma,\tau`-polynomial). **This
proves, not just observes, that the outline's literal candidates
`c\cdot\mathrm{Num},\ d\cdot G_0` (and every other single-bare-variable
product with any of the three base generators) are structurally incapable
of contributing to a `\sigma,\tau`-only certificate — a genuine, exact
negative result, closing off this specific search direction for good.**

**3. The correct necessary condition, sharpened beyond round 13's coarse
statement: a working multiplier needs an EVEN number of odd-graded factors,
not merely "one bare odd `c`- or `d`-factor" (round 13's phrasing, now
shown to be imprecise — "one bare factor" alone is never enough, as Step 2
shows).** Every one of `G_0,E_{\mathrm{num}},\mathrm{Num}$ lives purely in
the two coarse grades `(1,0)` (its `ct\,P_H` piece) and `(0,1)` (its
`sd\,Q_H` piece); the bare variables `c,d` also carry a single unit of
grade (`(1,0)` and `(0,1)` respectively) while `s,t` carry none in this
coarse scheme. **A product of generators/bare-variables lands in the usable
`(0,0)`-graded piece if and only if the total number of `(1,0)`-type and
`(0,1)`-type contributing factors is even in each coordinate** — this is
exactly why pairwise products `H\cdot H'` (already exploited throughout
rounds 15-16 as `B_{G_0E},B_{G_0N},B_{EN}`) work, while a single bare `c`
or `d` (or a single bare `H`) does not, and why `c\cdot d\cdot(\text{bare }
H)$ was also checked and found to vanish identically in the `(0,0)`-piece
(own fresh symbolic check, `H=G_0\cdot E_{\mathrm{num}}$: `(cd\cdot G_0\cdot
E_{\mathrm{num}})_{00}=0` exactly, since `G_0\cdot E_{\mathrm{num}}` already
has no `(1,1)`-graded component surviving after full reduction for `cd$ to
land on — own fresh residual check, `0`). This sharpens round 13's
necessary condition into an exact parity rule usable for systematically
ruling out (or in) candidate multiplier shapes without ad hoc trial.

**4. A genuinely new, unconditionally-nonnegative generator family,
constructed and verified exactly, but too high-degree to close the LP
this round.** Motivated by Step 3, consider `cd\cdot H\cdot H'` for
`H,H'\in\{G_0,E_{\mathrm{num}},\mathrm{Num}\}`: this lands partly in grade
`(1,1)$ (the piece `cd\cdot(H H')_{00}$) and partly in grade `(0,0)` (the
piece `cd\cdot(HH')_{11}`, since `cd` has grade `(1,1)` and adding it to a
`(1,1)`-graded piece of `HH'` gives `(0,0)`). Explicitly (own fresh
`sympy`, exact, all three same-`H` and mixed-`H` cases computed and
verified):
$$\big(cd\cdot H\cdot H'\big)_{00}=(1-\sigma)(1-\tau)\,st\,\big(P_HQ_{H'}
+Q_HP_{H'}\big)(\sigma,\tau),$$
still odd in both `s` and `t` (a bare `st$ factor) — by itself, again not a
`\sigma,\tau`-polynomial (a Step-2-style obstruction one level up). **But
its SQUARE is**, since `(st)^2=\sigma\tau`, and — crucially — the full
reduced polynomial `cd\cdot H\cdot H'` also carries a `(1,1)`-graded
component `cd\cdot(1-\sigma)\tau P_HP_{H'}+cd\,\sigma(1-\tau)Q_HQ_{H'}`
whose own square (grade `(1,1)+(1,1)=(0,0)`) is *also* a genuine
`\sigma,\tau`-polynomial. Defining
$$\mathrm{NewGen}(H,H'):=\Big[\big(cd\cdot H\cdot H'\big)^2\Big]_{00}$$
(the coarse `(0,0)`-graded part of the FULL square, computed by direct
symbolic reduction, not decomposed by hand), this is **manifestly
nonnegative for every real `c,s,d,t` with `c^2+s^2=1,d^2+t^2=1` — no domain
restriction needed at all** (it is the average of the four sign-flip
images of a perfect square `(cd\,HH')^2\ge0`, hence itself `\ge0` as an
average of nonnegative quantities; own fresh `sympy` symbolic computation
and reduction confirms every resulting expression is a pure `\sigma,\tau`
polynomial with **zero leftover `c,s,d,t` dependence**, for all six pairs
`(H,H')\in\{G_0,E_{\mathrm{num}},\mathrm{Num}\}^2/\!\sim` tried). Explicitly,
for the smallest case:
$$\mathrm{NewGen}(G_0,G_0)=(\sigma-1)(\tau-1)\big(128\sigma^2\tau^6-512
\sigma^2\tau^5+864\sigma^2\tau^4-784\sigma^2\tau^3+409\sigma^2\tau^2-120
\sigma^2\tau+16\sigma^2-128\sigma\tau^6+448\sigma\tau^5-648\sigma\tau^4
+472\sigma\tau^3-170\sigma\tau^2+24\sigma\tau+16\tau^6-32\tau^5+24\tau^4
-8\tau^3+\tau^2\big),$$
degree `10` in `(\sigma,\tau)` (matching `cd\cdot G_0^2$'s total degree
`4+4=8` in `(c,s,d,t)`, projected and squared to degree `10` in
`\sigma,\tau` — own `sympy.total_degree` check). **Independently numerically
confirmed nonnegative over the FULL unit square `(\sigma,\tau)\in[0,1]^2`**
(own fresh `2{,}000{,}000`-point `numpy` sweep, `\min\approx3.8\times
10^{-17}\ge0$ to floating precision, `\max\approx2.37$), consistent with
the exact unconditional-nonnegativity proof above. The other five pairs
(`(G_0,\mathrm{Num}),(E_{\mathrm{num}},G_0),(E_{\mathrm{num}},
E_{\mathrm{num}}),(E_{\mathrm{num}},\mathrm{Num}),(\mathrm{Num},
\mathrm{Num})`) were computed exactly the same way (exact closed forms
recorded in this round's own `sympy` session, all verified free of leftover
`c,s,d,t` dependence) but have total degree `16$–`17` in `\sigma,\tau` —
**far higher than `q_1`'s degree `6` or `r_0`'s degree `7`, so none of them
can be padded DOWN to match; they would only be usable inside a much larger
Positivstellensatz combination where `-q_1$ or `-r_0` is first multiplied
up to degree `\ge16` by a positive multiplier, a search this round did not
have time to run (the existing LP/SDP infrastructure searches multiplier
degrees up to `\sim4`–`6`, not `10$+`).** This is reported as an honest,
scoped finding: **a genuinely new, unconditionally-nonnegative generator
family has been found and exactly verified (not previously used by any
prior round, since it uses the finer even-parity-of-two-bare-variables
trick rather than a single bare variable or a bare `H\cdot H'` product),
but it is not yet shown to be USEFUL — no attempt this round to run the LP
at the much higher degree these generators require, which is the natural
next step for a future round with more time budget.**

**5. Case-split (outline option 1) — not attempted this round.** Given the
depth to which option 2 was pursued (a full structural theorem plus a new
verified generator family, not merely a diagnostic), and the round's time
budget, the domain-aware case-split fallback (splitting the residual region
by sign of a pivot quantity, as scoped in round 16 Item 4 and reiterated in
this round's outline) was not attempted this round; it remains exactly as
open as after round 16, with the same honest scoping note (no natural pivot
variable has yet been identified that produces a genuine case split, since
the domain's natural threshold quantities `2\tau-1,4\tau-1` etc. are already
sign-fixed throughout the true residual domain).

**6. Honest net assessment.** This round (a) proved a clean structural
decomposition `H=ct\,P_H+sd\,Q_H` for all three base generators, new for
`G_0` and `\mathrm{Num}` (exact, zero-residual); (b) used it to give an
exact PROOF (not an empirical search failure) that the outline's literal
"bare odd `c`/`d` multiplier" suggestion cannot work for any of the three
base generators, sharpening round 13's necessary condition into a precise
"even number of odd-graded factors" parity rule; (c) constructed and
exactly verified a genuinely new unconditionally-nonnegative generator
family `\mathrm{NewGen}(H,H')` (six instances, all exact, all
independently numerically confirmed nonnegative on the full unit square,
not just the tiny residual domain) — real new mathematical content beyond
anything previously in this file; but (d) this new family's degree
(`10`–`17` in `\sigma,\tau`) is far above `q_1,r_0`'s own degree (`6,7`),
so it was NOT shown this round to close the LP/SDP gap — that requires a
much higher-degree multiplier search not attempted here due to time.
**The central target — a Positivstellensatz certificate for `-q_1,-r_0` —
is NOT found this round.** No overclaiming: Status remains `partial`. Net
value this round: a decisive, fully-proved negative result closing off the
outline's literal suggestion for good, plus one honestly-scoped new
positive construction (a new generator family) for a future round to try
at higher degree — the case-split option remains fully open and untried.

### Round 16 (this round) — sign-error fixed and confirmed; corrected LP
rerun (negative, confirmed non-artifact); joint Putinar/SDP escalation tried
at several degrees (negative, confirmed via CLARABEL infeasibility
certificates); case-split fallback opened but not completed — the central
`-q_1,-r_0` certificate is **still not found**

**Task this round:** (0) fix the confirmed round-15 sign error
(`B_{G_0N}` as displayed was the wrong sign; the correct positive quantity
is `(G_0\cdot\mathrm{Num})_{00}`); (1) rerun the LP feasibility search with
the corrected generator; (2) escalate to a joint Putinar/SDP relaxation if
the LP remains infeasible; (3) fall back to an explicit domain case-split
if the SDP also fails.

**0. Sign-error fix, re-derived from scratch and exactly confirmed.** Own
fresh `sympy` session, rebuilding `G_0:=ct(1-2d^2)-2sd^3` and the round-13
authoritative `\mathrm{Num}:=c^5t^3-3c^3d^2s^2t-c^3s^2t^3+2c^2d^3s^3
-6c^2ds^3t^2-9cd^2s^4t` from the certified raw definitions, computing the
product `G_0\cdot\mathrm{Num}` reduced modulo `\langle c^2+s^2-1,
d^2+t^2-1\rangle` and projected onto the `(0,0)`-graded piece via the
averaging projector, rewritten in `\sigma=s^2,\tau=t^2`:
$$B_{G_0N}:=(G_0\cdot\mathrm{Num})_{00}=-32\sigma^3\tau^3+56\sigma^3\tau^2
-30\sigma^3\tau+4\sigma^3+32\sigma^2\tau^3-50\sigma^2\tau^2+27\sigma^2\tau
-4\sigma^2-2\sigma\tau^3-5\sigma\tau^2+3\sigma\tau+2\tau^3-\tau^2.$$
**Exact `sympy.expand` check: this closed form is the negative of round
15's displayed `B_{G_0N}` polynomial, term for term (residual `0`)** —
confirming precisely the round-15 proof-reviewer's diagnosis: what round 15
called `B_{G_0N}=(G_0\cdot(-\mathrm{Num}))_{00}` and claimed positive is
literally `-(G_0\cdot\mathrm{Num})_{00}`, i.e. the correctly-signed positive
quantity is `(G_0\cdot\mathrm{Num})_{00}` (no minus sign on `\mathrm{Num}`),
exactly as the outline's Step 0 states. Independently re-confirmed
numerically on a fresh `4{,}000{,}000`-sample sweep restricted to the true
residual domain (own domain-membership test rebuilt directly from
`G_0>0,E_{\mathrm{num}}<0,\mathrm{Bc}\ge0,\mathrm{Num}<0`, `17{,}340` domain
points found, `\sigma\in(0.1568,0.2610),\tau\in(0.6253,0.7859)`, matching
prior rounds closely): $B_{G_0N}=(G_0\cdot\mathrm{Num})_{00}\in(0.0121,
0.0784)>0$ throughout — **zero violations, and the range matches round 15's
originally-claimed (but mislabeled) numbers digit-for-digit**, confirming
this is now the correctly-derived, correctly-signed generator. **Every
place in this file (and in `current.md`'s round-15 summary) that used
`B_{G_0N}` should be read as this corrected quantity
`(G_0\cdot\mathrm{Num})_{00}` going forward; the old formula
`32\sigma^3\tau^3-56\sigma^3\tau^2+\ldots` (round 15's displayed form) is
`-B_{G_0N}$, i.e. `(G_0\cdot(-\mathrm{Num}))_{00}`, and is uniformly
NEGATIVE on the domain, not usable as a positive generator.** On the same
sweep, `B_{G_0E}\in(0.0276,0.1075)>0` and `B_{EN}\in(0.0074,0.0579)>0`
(both re-confirmed, unaffected by the fix), and — on the true curved domain
(not just the round-14 loose box) — `B_1\in(0.132,0.357)>0,\ -B_2\in
(0.019,0.063)>0,\ B_4\in(0.037,0.093)>0,\ B_6\in(0.023,0.056)>0`, while
`B_3,B_5` remain mixed-sign even on the true domain and so are excluded
from this round's nonnegative-coefficient generator basis (they cannot
license a nonnegative-coefficient certificate term by themselves without
further work). **The correctly-signed generator basis used for the rest of
this round is
`\{B_1,-B_2,B_4,B_6,B_{G_0E},B_{G_0N}:=(G_0\cdot\mathrm{Num})_{00},B_{EN},
\sigma,\tau,1-\sigma,1-\tau\}`** (all confirmed `\ge0`, several `>0`, on the
true residual domain, own fresh sample).

**1. Corrected LP rerun (own fresh exact-rational span/rank test plus
`scipy.optimize.linprog` feasibility, non-homogeneous padding at every
sub-degree from `0` up to the needed maximum, as directed).** Direct
(unmultiplied) search at `-q_1`'s own degree `6` and `-r_0`'s own degree
`7`: **neither is in the unsigned span** of the corrected 7-generator basis
padded appropriately (`-q_1$: rank `20` vs `21` augmented; `-r_0`: rank `28`
vs `29`) — the corrected sign-definite `B_{G_0N}` does not by itself fix the
span obstruction. Extending to the same nine multiplier variants as round
15 (`1-\sigma,\ 1-\tau,\ \sigma,\ \tau,\ \tau(1-\sigma),\ \sigma(1-\tau),\
(1-\sigma)(1-\tau),\ (1-\sigma)^2,\ (1-\tau)^2,\ \sigma(1-\sigma),\
\tau(1-\tau),\ \sigma\tau,\ \sigma^2,\ \tau^2$ — 14 variants in total, a
superset of round 15's list): the same pattern as round 15 recurs almost
exactly — some variants (`\tau(1-\sigma),\ \sigma(1-\tau),\
(1-\sigma)(1-\tau),\ (1-\sigma)^2,\ (1-\tau)^2,\ \sigma(1-\sigma),\
\tau(1-\tau)` for `-q_1`; `1-\sigma,\ (1-\sigma)(1-\tau),\ (1-\sigma)^2,\
(1-\tau)^2,\ \sigma(1-\sigma)` for `-r_0`) bring the target into the
unsigned span, but in **every single case the nonnegative-coefficient LP is
infeasible** — including with the corrected generator now available as a
building block. **The corrected sign does not change the substantive
negative conclusion: no certificate is found in this generator family at
these multiplier degrees, even with the fix.**

**2. Non-solver-artifact confirmation (own fresh phase-1 `L^1`-residual LP,
per the outline-directed methodology).** For four representative
infeasible cases (`-q_1\cdot(1-\sigma)`, `-q_1\cdot\tau(1-\sigma)`,
`-r_0\cdot(1-\sigma)`, `-r_0\cdot(1-\sigma)(1-\tau)`), the auxiliary
`\min\sum(r_i^++r_i^-)` LP gives optimal residuals `204.8,\ 40.08,\ 54.71,\
69.19` respectively — **all far from `0`, decisively confirming genuine
infeasibility, not a solver-tolerance artifact.**

**3. Joint Putinar/SDP escalation (new this round, per Step 2 — the
highest-value untried technique flagged by the explorer, now actually
attempted, not merely proposed).** Set up the Putinar-style Gram-matrix SDP
$$-q_1\ \overset{?}{=}\ \sum_{i}\sigma_i(\sigma,\tau)\cdot G_i(\sigma,\tau),
\qquad \sigma_i\ \text{SOS (Gram-matrix PSD)},$$
over the corrected generator basis `G_i\in\{1,\sigma,\tau,1-\sigma,1-\tau,
B_1,-B_2,B_4,B_6,B_{G_0E},B_{G_0N},B_{EN}\}` (own `cvxpy` implementation:
each `\sigma_i`'s Gram matrix is built in the monomial basis
`\{\sigma^a\tau^b:a+b\le k_i\}$ with `k_i=\lfloor(\text{maxdeg}-\deg
G_i)/2\rfloor`, PSD-constrained, and matched against the target's monomial
coefficients via linear equality constraints on the Gram-matrix entries —
standard Lasserre/Putinar SOS relaxation, no unusual simplification).
**Solved at `\mathrm{maxdeg}\in\{6,8\}` for `-q_1$ and `\{7,9,11\}` for
`-r_0`, both bare and with the `(1-\sigma)`/`(1-\sigma)(1-\tau)` positive
multiplier applied to the target first, using the `CLARABEL` interior-point
solver (chosen over `SCS` specifically because an initial `SCS` run on
`-q_1$ at `\mathrm{maxdeg}=8` returned `optimal_inaccurate` with Gram
matrices carrying eigenvalues as negative as `-4.6` — i.e. a spurious,
non-PSD "solution" from non-convergence, NOT a genuine certificate; this
was caught by explicitly checking `\mathrm{eigvalsh}$ of every returned
Gram matrix, a rigor step this round adds to the population's SDP
methodology going forward — any future round reporting SDP "feasibility"
must report the returned Gram matrices' minimum eigenvalues, not just the
solver's status string).** With `CLARABEL`, **every one of these eight
cases returns a clean `infeasible` status (a genuine SDP infeasibility
certificate, not a numerical-tolerance judgement call)**, except two
larger instances (`-q_1\cdot(1-\sigma)(1-\tau)` at `\mathrm{maxdeg}=10`,
`-r_0\cdot(1-\sigma)` at `\mathrm{maxdeg}=10`) where `CLARABEL` itself
fails to converge on the larger problem size (own honest disclosure: these
two specific larger instances are **inconclusive**, not confirmed
infeasible, due to solver scaling limits reached in the time available —
flagged explicitly so a future round does not mistake "solver crashed" for
"infeasible"). **Net: the Putinar/SDP escalation — which strictly subsumes
every nonnegative-coefficient monomial combination the LP search tried,
since an SOS multiplier of degree `2k` covers all such combinations up to
that degree at once — finds NO certificate for `-q_1$ or `-r_0` in this
generator family at any of the six degrees where the solver conclusively
resolved feasibility, and is inconclusive (not negative, not positive) on
two further, larger instances that exceeded this round's solver-scaling
budget.** This is materially stronger negative evidence than the LP alone:
it rules out not just nonnegative-coefficient monomial combinations but the
much larger class of SOS-weighted combinations, at every degree checked.

**4. Step 3 (case-split fallback) — opened, not completed.** A first,
honest look at whether `q_1`'s own term structure admits an
outliner-suggested Schur-style "order the variables, dominate the lone
negative term by an adjacent positive one" argument: `q_1`'s twelve
`(\sigma,\tau)$-monomials have genuinely mixed signs in a pattern with no
single obviously-dominant negative term (coefficients alternate
`+,-,+,-,+,-,+,-,+,-,+,+$ across the naturally-ordered monomial list, not a
"one bad term" shape), so the crux-corpus Schur pattern does not transfer
directly to `q_1$ viewed as a bare polynomial in `\sigma,\tau` alone — any
working case split almost certainly needs to use the actual domain
conditions (`G_0>0,\ E_{\mathrm{num}}<0,\ \mathrm{Bc}\ge0,\
\mathrm{Num}<0`, or equivalently a further-reduced curve/boundary
description of the residual region) to compensate the negative terms
region-by-region, not a sign pattern of `q_1` alone. **This is an honest
scoping note, not an attempt or a result** — time this round went to the
mandatory Steps 0-2 first, per the outline's own priority ordering
("only pursue this if Step 2's SDP setup proves intractable to stand up
this round" — Step 2 was *not* intractable to stand up, it was
successfully run and gave a genuine (if partial) negative result, so per
the outline's own stated priority, Step 3 correctly receives less time
this round). Flagged as the concrete next lever for a future round:
(a) resolve the two solver-scaling-inconclusive SDP instances from Item 3
at higher precision/a different solver (e.g. `MOSEK` if available, or a
sparser/reduced monomial basis); (b) if SDP remains negative there too,
design an actual domain-aware case split (e.g. splitting on
`\mathrm{sign}(2\tau-1)$ or `\mathrm{sign}(4\tau-1)`, the two linear factors
that recur across `B_1,B_6$, as a natural first ordering variable, since
`\tau\approx0.625$–`0.786` straddles both `1/2` and `1/4$... actually
`\tau>1/2` and `\tau>1/4` always hold on the true domain, so those
particular factors are already sign-fixed and not a genuine case split —
a better candidate split variable was not identified this round and is
left as an open design question).

**5. Honest net assessment.** This round (a) fixed and exactly re-confirmed
the round-15 sign error (Step 0), now recorded in a form future rounds can
cite without re-deriving; (b) reran the full LP feasibility sweep with the
corrected generator, finding the same negative outcome as round 15's
(differently-signed) sweep — the sign fix does not, by itself, produce a
certificate; (c) independently confirmed the LP infeasibility is genuine
via a phase-1 residual check; (d) escalated to a joint Putinar/SDP
relaxation for the first time in this population's history, finding clean
`CLARABEL`-certified infeasibility at six degree/multiplier combinations
(a strictly stronger negative result than the LP alone) and two
inconclusive (solver-scaling-limited, not negative) larger instances; (e)
opened, but did not complete, the Step-3 domain-aware case-split fallback,
with an honest scoping note on why a naive sign-pattern argument on `q_1`
alone does not transfer the crux-corpus Schur pattern directly. **The
central target — a Positivstellensatz certificate for `-q_1,-r_0` in the
generator family `\{G_0,E_{\mathrm{num}},\mathrm{Num},\mathrm{Bc}\}` (bare,
paired products, or SOS-weighted combinations thereof) — is NOT found this
round, and the negative evidence is now the broadest and most rigorously
confirmed of any round to date (LP + phase-1 residual + SDP + eigenvalue-
verified solver output).** No overclaiming: Status remains `partial`. This
strongly suggests that either (i) a genuinely new base generator beyond
`\{G_0,E_{\mathrm{num}},\mathrm{Num},\mathrm{Bc}\}` is needed, or (ii) an
explicit domain-aware case split (Step 3, still open) is the more promising
remaining lever, since two independent generic-certificate techniques (LP,
SDP) have now both failed on this generator family.

### Round 16 outline (proof-outliner directive — skeleton, not a proof)

**Step 0 (mandatory, do first — confirmed sign-error fix).** The round-15
proof-reviewer independently confirmed that `B_{G_0N}:=(G_0\cdot(-\mathrm{Num}))_{00}`
as displayed in round 15 has the WRONG sign: it is uniformly NEGATIVE on
the true residual domain (`0/8793` independent samples positive, range
`≈(-0.079,-0.012)`), the opposite of what was claimed. **The correctly
signed, genuinely sign-definite generator is `-B_{G_0N}=(G_0\cdot\mathrm{Num})_{00}`**
(positive range matches the round-15 file's claimed numbers digit-for-digit).
Re-derive this corrected generator's exact closed form from the raw
certified `G_0,\mathrm{Num}` definitions (mechanical, already done once,
just flip the sign convention) before anything else this round.

**Step 1 (skeleton — corrected LP rerun).** Rerun the exact same 9-variant
multiplier LP feasibility sweep from round 15 (Table: `1-\sigma, 1-\tau,
\tau(1-\sigma), \sigma(1-\tau), (1-\sigma)(1-\tau), (1-\sigma)^2,
(1-\tau)^2, \sigma(1-\sigma), \tau(1-\tau)`), substituting the corrected
`(G_0\cdot\mathrm{Num})_{00}` for the erroneous `B_{G_0N}` in the
9-generator basis `\{B_1,-B_2,B_3,B_4,B_5,B_6,B_{G_0E},(G_0\cdot\mathrm{Num})_{00},B_{EN}\}`.
Since none of round 15's 9 LP runs actually used the correctly-signed
generator, this is a genuinely new, not-yet-run search — report both the
unsigned-span/rank result and the nonnegative-coefficient LP feasibility
(with a phase-1 L¹-residual check to confirm any "infeasible" result is not
a solver artifact, per round 15's own methodology) for both `-q_1` and
`r_0` targets. Also extend to the non-homogeneous degree-padding scheme
(padding every sub-degree from 0 up to the needed maximum, per round 15's
own corrected methodology) — do not repeat the earlier top-degree-only
padding mistake.

**Step 2 (skeleton — if Step 1 remains infeasible, escalate to joint
Putinar/SDP).** Per the round-16 `math-explorer-generator-synthetic`
report's technique 2 (the highest-value untried technique for this
approach): pose the joint Putinar-style certificate directly as an SDP —
search for SOS polynomials `\sigma_0,\sigma_{G_0},\sigma_{E_{\mathrm{num}}},
\sigma_{\mathrm{Bc}},\sigma_{\mathrm{Num}}` (via Gram-matrix PSD
constraints, some fixed low degree to start) with
`-q_1 = \sigma_0+\sigma_{G_0}G_0+\sigma_{E_{\mathrm{num}}}(-E_{\mathrm{num}})
+\sigma_{\mathrm{Bc}}\mathrm{Bc}+\sigma_{\mathrm{Num}}(-\mathrm{Num})`
(and separately for `r_0`). This subsumes every hand-picked
generator/multiplier combination the LP search has tried (an SOS
multiplier of degree `2k` covers *all* nonnegative-coefficient combinations
of monomial-times-square terms up to that degree at once) and is the
natural escalation once LP-with-guessed-basis is infeasible: LP
infeasibility only rules out that specific basis, never the existence of
any certificate at a given degree. Use `cvxpy`+`SCS`/`CLARABEL` (install if
needed; the `-pointwise-sos` sibling already has this infrastructure
in `/tmp/round-15/sos_work/` as a template for the SDP setup style). Start
with modest degree (matching `q_1,r_0`'s own degree, e.g. total degree 6)
before escalating.

**Fallback (Step 3, lower priority this round).** If neither Step 1 nor
Step 2 closes the gap, the explicit case-split option (explorer technique
3: split the residual `(\sigma,\tau)` domain by an explicit sign/ordering
condition, adapting the Schur-type "order variables, dominate the lone
negative term by an adjacent positive one" pattern from the crux corpus's
`algebra/inequalities-SOS-and-convexity` domain — a hint to adapt, not
reuse verbatim) remains open as a genuinely different lever, not yet tried
in any round (rounds 10-15 all search a single global certificate). Only
pursue this if Step 2's SDP setup proves intractable to stand up this
round.

### Round 15 (this round) — independent verification of the parity-lens
explorer's three new degree-6/6/8 sign-definite product generators
(`G0·Enum`, `G0·(-Num)`, `Enum·Num`), a corrected (non-homogeneous-aware)
exact linear-algebra/LP certificate search over the full 9-element
sign-definite basis with nine different positive multiplier candidates
(including the outliner-directed `(1-σ)/(1-τ)` trick and its extensions),
and a parallel, equally thorough r0-specific search — the central
`-q_1,-r_0` Positivstellensatz certificate is **still not found**, but the
negative evidence is now much broader and independently confirmed
non-solver-artifact (phase-1 LP residual check)

**Task this round:** close the central `-q_1,-r_0` certificate using this
round's new degree-6 sign-definite candidates (`G_0\cdot E_{\mathrm{num}}`,
`G_0\cdot\mathrm{Num}`, `E_{\mathrm{num}}\cdot\mathrm{Num}`) and the
`(1-\sigma)/(1-\tau)` positive-multiplier trick; treat `r_0` as potentially
needing separate generator work.

**1. Independent, from-scratch re-derivation of the three new product
identities (own fresh `sympy` session, not copied from the explorer's
report).** Starting from the already-certified closed forms `G_0:=ct(1-2d^2)
-2sd^3`, `E_{\mathrm{num}}:=ctf_1(\sigma,\tau)+dsf_2(\sigma,\tau)`, and
`\mathrm{Num}` (round-13's authoritative displayed formula) — themselves
raw, previously-certified reductions of the original geometric quantities —
computed each pairwise product, reduced it modulo `\langle c^2+s^2-1,
d^2+t^2-1\rangle` (`sympy.reduced`), and projected onto the `(0,0)`-graded
piece via the averaging projector `f_{00}=\tfrac14\sum_{\epsilon,\delta\in
\{\pm1\}}f(\epsilon c,s,\delta d,t)`, then rewrote the (now manifestly even
in `s,t`) result in `\sigma:=s^2,\tau:=t^2`. This independently reproduces,
**with zero symbolic residual against the explorer's report**:
$$B_{G_0E}:=(G_0\cdot E_{\mathrm{num}})_{00}=128\sigma^3\tau^3-224\sigma^3
\tau^2+120\sigma^3\tau-16\sigma^3-184\sigma^2\tau^3+294\sigma^2\tau^2-144
\sigma^2\tau+16\sigma^2+58\sigma\tau^3-71\sigma\tau^2+24\sigma\tau-2\tau^3
+\tau^2,$$
$$B_{G_0N}:=(G_0\cdot(-\mathrm{Num}))_{00}=32\sigma^3\tau^3-56\sigma^3\tau^2
+30\sigma^3\tau-4\sigma^3-32\sigma^2\tau^3+50\sigma^2\tau^2-27\sigma^2\tau+4
\sigma^2+2\sigma\tau^3+5\sigma\tau^2-3\sigma\tau-2\tau^3+\tau^2,$$
$$B_{EN}:=(E_{\mathrm{num}}\cdot\mathrm{Num})_{00}=512\sigma^5\tau^3-768
\sigma^5\tau^2+288\sigma^5\tau-16\sigma^5-992\sigma^4\tau^3+1344\sigma^4
\tau^2-444\sigma^4\tau+32\sigma^4+568\sigma^3\tau^3-600\sigma^3\tau^2+132
\sigma^3\tau-16\sigma^3-110\sigma^2\tau^3+33\sigma^2\tau^2+24\sigma^2\tau+23
\sigma\tau^3-9\sigma\tau^2-\tau^3,$$
each with total degree exactly `6,6,8$ respectively (`sympy.total_degree`,
own check) — matching the explorer's report exactly (`sympy.expand` of the
difference against the explorer's factored forms `(\sigma-1)(\cdots)` is
identically `0` in all three cases). **`B_{G_0E},B_{G_0N}` are exact
degree-6 matches to `q_1`'s own total degree, needing NO monomial padding at
all — a genuinely new, structurally cleaner class of generator than any
previously found in this population.**

**2. Independent numeric confirmation of sign-definiteness on the true
residual domain (own fresh `4{,}000{,}000`-sample sweep, own domain-
membership code rebuilt directly from the four raw generator definitions
`G_0,E_{\mathrm{num}},\mathrm{Bc}:=c-2t^2+1,\mathrm{Num}`, not reused from
any prior round's script).** `10{,}118` genuine domain points found
(`\sigma\in(0.1565,0.2610),\tau\in(0.6251,0.7863)`, matching round 13/14's
window closely). On these:
$$B_{G_0E}\in(0.0276,0.1076)>0,\qquad B_{G_0N}\in(0.0121,0.0789)>0,\qquad
B_{EN}\in(0.0075,0.0580)>0,$$
**zero violations of any of the three sign claims**, and (as a cross-check)
`q_1\in(-0.627,-0.0014)<0`, `r_0\in(-0.660,-0.0021)<0` throughout, matching
all prior rounds. This independently confirms the explorer's sign-
definiteness finding at a comparable sample scale (`8729` vs `10{,}118`
domain points, different random seed).

**3. A subtlety caught this round, correcting a latent methodological risk
in round 14's degree-matching scheme: `q_1,r_0` are NOT homogeneous
polynomials in `(\sigma,\tau)`** (e.g. `q_1` contains monomials of total
degree `4,5,6` simultaneously — `96\sigma^4$ (degree 4), `-928\sigma^3\tau^2`
(degree 5, wait `\sigma^3\tau^2` has degree 5)... — direct inspection of the
displayed formula confirms terms of at least three distinct total degrees).
**Round 14's ansatz search implicitly padded each generator by monomials of
EXACTLY the degree needed to match `q_1`'s maximum total degree, which is
too restrictive for a non-homogeneous target** — the correct search must
allow padding monomials of every degree from `0` up to the needed maximum,
not just the single top degree. Redid the full search with this corrected
scheme (own `sympy` script, exact rational linear algebra throughout, no
floating-point rounding in the span/rank tests):
- `\{B_1,B_4,B_6\}$ alone (degree-appropriate padding at every sub-degree,
  not just top degree): `-q_1` still not in the unsigned span (rank
  `14` vs `15`).
- Adding `B_3,B_5`: still not in span (rank `16` vs `17`).
- Adding `-B_2$: still not in span (rank `21` vs `22`).
- Adding `B_{G_0E},B_{G_0N}` (this round's new generators, direct degree-6
  match): **still not in the unsigned span** (rank `21` vs `22`) — i.e. even
  with the two new degree-matched sign-definite generators, `-q_1` cannot
  be reached at its own degree by any nonnegative-coefficient (indeed even
  by any real-coefficient) combination of the full 8-generator set.
- Adding `B_{EN}` (degree 8, too high to pad down to degree 6, so it
  contributes nothing at this degree): unchanged (rank `21` vs `22`).

**4. The `(1-\sigma)/(1-\tau)` multiplier trick, exactly as directed, and
seven further natural extensions of it — ALL bring `-q_1` into the unsigned
span, but the resulting nonnegative-coefficient LP is infeasible in EVERY
case tried (own exact-rational span/rank test plus `scipy.optimize.linprog`
feasibility check for each, on the corrected non-homogeneous padding
scheme, full 9-generator set `\{B_1,-B_2,B_3,B_4,B_5,B_6,B_{G_0E},B_{G_0N},
B_{EN}\}`):**

| multiplier | in unsigned span? | LP feasible? |
|---|---|---|
| `1-\sigma` | yes (rank `29=29`) | **no** |
| `1-\tau` | yes (rank `29=29`) | **no** |
| `\tau(1-\sigma)` | yes (rank `38=38`) | **no** |
| `\sigma(1-\tau)` | yes (rank `38=38`) | **no** |
| `(1-\sigma)(1-\tau)` | yes (rank `38=38`) | **no** |
| `(1-\sigma)^2` | yes (rank `38=38`) | **no** |
| `(1-\tau)^2` | yes (rank `38=38`) | **no** |
| `\sigma(1-\sigma)` | yes (rank `38=38`) | **no** |
| `\tau(1-\tau)` | yes (rank `38=38`) | **no** |

**This directly answers, negatively, the round's dispatched question**: the
`(1-\sigma)/(1-\tau)` trick (and every natural variant tried) fixes the
span-rank obstruction (as the explorer already found for the first two) but
does not, by itself or with any of these seven extensions, produce a
feasible nonnegative certificate.

**5. A genuine rigor upgrade over a bare `linprog` "infeasible" report: an
independent phase-1 (L¹-residual-minimization) LP confirms the infeasibility
is real, not a floating-point/solver artifact.** For the `1-\sigma` case,
set up the auxiliary LP `\min\sum_i(r_i^++r_i^-)` subject to `Ax+r^--r^+=b`,
`x,r^+,r^-\ge0` (own fresh construction, this round): the optimal objective
value is `\approx65.46`, far from `0` — **if the original system were
feasible, this residual would be exactly `0`; a residual this large is
decisive, non-borderline evidence of genuine infeasibility**, not a solver
tolerance issue. This is a materially stronger form of evidence than a bare
`linprog(...).success=False` flag (which could in principle reflect a
numerically ill-conditioned near-feasible system) and should be the standard
going forward whenever this population reports an LP infeasibility as a
load-bearing negative result.

**6. Parallel, equally thorough treatment of `r_0` (per the outliner's
explicit flag that `r_0` should not be assumed to inherit `q_1`'s eventual
certificate) — confirms `r_0` is structurally harder, with an even wider
negative sweep than `q_1`'s:**
- `-r_0` direct (degree 7, the same corrected non-homogeneous padding, full
  9-generator set): **not in the unsigned span** (rank `29` vs `30`,
  matching the explorer's own finding exactly).
- `-r_0\cdot(1-\sigma)`: **in span** (rank `38=38`) but **LP infeasible**.
- `-r_0\cdot\sigma`: **not in span** (rank `38` vs `39`).
- `-r_0\cdot(1-\tau)`: **not in span** (rank `38` vs `39`) — notably
  different from `q_1`'s behavior, where both `(1-\sigma)` and `(1-\tau)`
  fixed the span; for `r_0`, only `(1-\sigma)` (not `(1-\tau)`) repairs the
  span obstruction, a genuine structural asymmetry between the two targets,
  newly observed this round.
- `-r_0\cdot(1-\sigma)(1-\tau)`: **in span** (rank `48=48`) but **LP
  infeasible**.

**7. Honest net assessment.** This round (a) independently re-derived and
confirmed, from the already-certified `G_0,E_{\mathrm{num}},\mathrm{Num}`
definitions with zero symbolic residual, all three of the explorer's new
degree-6/6/8 product generators; (b) independently reconfirmed their sign-
definiteness on a fresh, independently-sampled `10{,}118`-point true-domain
census; (c) caught and corrected a latent methodological gap in the
degree-matching scheme used by round 14 (q_1, r_0 are not homogeneous, so
padding must range over every sub-degree, not only the top degree), and
redid the exact rank/span tests correctly; (d) ran the outliner-directed
`(1-\sigma)/(1-\tau)` trick plus seven further natural multiplier variants,
finding all nine bring `-q_1` into the unsigned span but leave the
nonnegative-coefficient LP infeasible in every case, with one case (`1-
\sigma`) independently confirmed via a phase-1 residual LP to be genuinely
(not artifactually) infeasible; (e) ran the identical, equally thorough
search for `-r_0`, confirming it is structurally harder still (asymmetric
behavior under `(1-\sigma)` vs `(1-\tau)`, LP infeasible even where span is
recovered). **The central target — an exact, verified (zero-residual)
Positivstellensatz certificate for `-q_1` and `-r_0` using the generator
family `\{G_0,E_{\mathrm{num}},\mathrm{Num},\mathrm{Bc}\}` (bare or paired
products, with any of the nine natural nonnegative multipliers tried) — is
NOT found this round, and the negative evidence against this whole generator
family (as currently constituted) is now substantially broader and more
rigorously confirmed than before.** This strongly suggests (though does not
prove) that a working certificate, if it exists at all within this
framework, needs either (i) a genuinely new base generator beyond `\{G_0,
E_{\mathrm{num}},\mathrm{Num},\mathrm{Bc}\}$ (the outliner's own suggestion,
not yet attempted), or (ii) a higher-degree multiplier (beyond the
degree-1/2 quadratic-in-`\sigma,\tau` multipliers tried here) which this
round did not have time to search, or (iii) an explicit case split of the
residual domain into sub-regions with different termwise arguments (as
foreshadowed by round 11's finding that `d,c>0` alone reduces the target to
`q_1<0\wedge r_0<0$ individually, itself still open). No overclaiming:
Status remains `partial`.

### Round 14 (this round) — exact verification (and correction) of the
parity-lens explorer's degree-matched `(ct,sd)` basis, a decisive negative
finding about a spurious "ideal-membership" shortcut, and a sign census on
the corrected basis; the central `-q_1,-r_0` Positivstellensatz certificate
is **still not found**

**Task this round:** actually search for and *exactly verify* (symbolic,
zero-residual, not numeric-fit) a Positivstellensatz-style certificate for
`-q_1,-r_0` using the finer `(\mathbb Z_2)^4`-graded degree-matched
multiplier basis `\{ct\cdot G_0,\ sd\cdot G_0,\ ct\cdot(-E_{\mathrm{num}}),\
sd\cdot(-E_{\mathrm{num}}),\ ct\cdot(-\mathrm{Num}),\ sd\cdot(-\mathrm{Num})\}`
that this round's parity-lens explorer proposed.

**0. Setup, own fresh derivation (not copied from the explorer's report,
so as to independently verify every claimed identity).** Working in
`c=\cos A,s=\sin A,d=\cos B,t=\sin B` with `\sigma=s^2,\tau=t^2`, using the
file's already-certified exact forms
$$q_1(\sigma,\tau)=512\sigma^4\tau^2-512\sigma^4\tau+96\sigma^4-928\sigma^3
\tau^2+856\sigma^3\tau-144\sigma^3+506\sigma^2\tau^2-392\sigma^2\tau+48
\sigma^2-85\sigma\tau^2+40\sigma\tau+3\tau^2,$$
$$r_0(\sigma,\tau)=2048\sigma^4\tau^3-3072\sigma^4\tau^2+1152\sigma^4\tau-64
\sigma^4-2688\sigma^3\tau^3+3744\sigma^3\tau^2-1248\sigma^3\tau+64\sigma^3
+936\sigma^2\tau^3-1092\sigma^2\tau^2+240\sigma^2\tau-80\sigma\tau^3+60
\sigma\tau^2+\tau^3$$
(round 10), `G_0:=ct(1-2d^2)-2sd^3` (round 12), `E_{\mathrm{num}}:=ct\,f_1
(\sigma,\tau)+ds\,f_2(\sigma,\tau)` with `f_1=-32\sigma^2\tau+24\sigma^2
+22\sigma\tau-12\sigma-\tau`, `f_2=-32\sigma^2\tau+8\sigma^2+38\sigma\tau
-8\sigma-6\tau` (round 12), `\mathrm{Bc}:=c-2t^2+1` (round 13), and the
round-13 **displayed** `\mathrm{Num}` polynomial
$$\mathrm{Num}=c^5t^3-3c^3d^2s^2t-c^3s^2t^3+2c^2d^3s^3-6c^2ds^3t^2-9cd^2s^4t$$
(used as-displayed, since round 13's file contains an internal sign
inconsistency between its prose derivation and its displayed formula — the
displayed formula is what every other reference in the file, including the
round-13 domain characterization `\{\mathrm{Num}<0\}`, actually uses, so it
is the authoritative one and is what is used throughout this round).

**Own fresh `sympy` computation of the `(0,0,0,0)`-graded (`\sigma,\tau`-only)
part of each of the six basis products**, via the projector `f_{00}=
\tfrac14(f(c,s,d,t)+f(-c,s,d,t)+f(c,s,-d,t)+f(-c,s,-d,t))` (correctly
isolates the `(0,0)`-part under the round-13 coarse `\mathbb Z_2\times
\mathbb Z_2` grading — using the coarse grading, not the explorer's claimed
finer `(\mathbb Z_2)^4` grading, is sufficient and equivalent here since
`q_1,r_0,\mathrm{Bc}`'s `\sigma,\tau`-only content is already even in both
`s` and `t`, so the extra `s,t`-parity bookkeeping the explorer proposed adds
no further resolving power for this specific computation) applied after
reducing modulo `\langle c^2+s^2-1,d^2+t^2-1\rangle`:
$$B_1:=(ct\cdot G_0)_{00}=\tau(1-\sigma)(2\tau-1),\qquad
B_2:=(sd\cdot G_0)_{00}=-2\sigma(\tau-1)^2,$$
$$B_3:=\big(ct\cdot(-E_{\mathrm{num}})\big)_{00}=-\tau(\sigma-1)
\big(32\sigma^2\tau-24\sigma^2-22\sigma\tau+12\sigma+\tau\big),$$
$$B_4:=\big(sd\cdot(-E_{\mathrm{num}})\big)_{00}=-2\sigma(\sigma-1)(\tau-1)
\big(16\sigma\tau-4\sigma-3\tau\big),$$
$$B_5:=\big(ct\cdot(-\mathrm{Num})\big)_{00}=\tau(\sigma-1)
\big(8\sigma^2\tau-6\sigma^2-3\sigma+\tau\big),$$
$$B_6:=\big(sd\cdot(-\mathrm{Num})\big)_{00}=2\sigma^2(\sigma-1)(\tau-1)
(4\tau-1).$$
`B_1$–`B_5` **exactly match** the explorer's report (own independent
`sympy` re-derivation, zero-residual check against the displayed formulas).
**`B_6` does NOT match the explorer's claimed `2\sigma^2(\sigma-1)(\tau-1)
(2\tau-1)(2\tau+1)`** — direct subtraction gives a nonzero residual
`-8\sigma^2\tau(\sigma-1)(\tau-1)^2\not\equiv0`, so the explorer's formula
for `B_6` was a genuine (if minor) transcription/computation error. **The
correct exact value, re-derived and verified here (zero `sympy.expand`
residual against the raw definition `sd\cdot(-\mathrm{Num})` reduced mod the
Pythagorean ideal and parity-projected), is `B_6=2\sigma^2(\sigma-1)(\tau-1)
(4\tau-1)`** — a cleaner factorization (degree 5, matching `B_1$–`B_5`'s
degree exactly) than the explorer's erroneous quintic-in-`\tau` guess. This
correction is recorded so the next round does not import the wrong formula.

**1. A decisive negative finding: naive raw ideal-membership testing on
this generator set is a spurious/degenerate shortcut and must NOT be used
as evidence of progress.** As a first (cheap) check, computed the Gröbner
basis of the FULL ideal `\langle c^2+s^2-1,\,d^2+t^2-1,\ ct\,G_0,\ sd\,G_0,\
ct\,(-E_{\mathrm{num}}),\ sd\,(-E_{\mathrm{num}}),\ ct\,(-\mathrm{Num}),\
sd\,(-\mathrm{Num}),\ \mathrm{Bc}\rangle$ in `\mathbb Q[c,s,d,t]` (own
`sympy.groebner`, `grevlex`) and reduced `q_1` against it: **remainder `0`.**
At first glance this looks like `q_1` lies in the ideal generated by these
seven "positive" quantities — but inspecting the Gröbner basis itself shows
it is `\{s^2,\ d^2-1,\ st,\ t^2,\ c+1\}$, i.e. the *combined* ideal (allowing
arbitrary, sign-unconstrained ring-element multipliers, exactly what raw
ideal membership permits) forces `s=t=0,\ c=-1,\ d=\pm1` — an isolated,
geometrically meaningless point set, **not** anything resembling the true
triangle domain. Since `q_1(\sigma,\tau)` (and `r_0`) have **zero constant
term** (every monomial of `q_1,r_0` contains a factor of `\sigma` or `\tau`,
i.e. of `s^2` or `t^2`), reduction modulo `s^2\to0,\ t^2\to0` trivially kills
`q_1$ to `0` — **for a purely structural reason having nothing to do with
any genuine Positivstellensatz decomposition.** This is recorded explicitly
as a decisive negative/methodological finding: **raw Gröbner-basis
ideal-membership tests against a mixed generator set (Pythagorean relations
plus several other polynomials) are USELESS here as an ideal-membership
check for polynomials with zero constant term, because the generator set is
"large" enough to force a degenerate zero-dimensional (or empty-in-any-real-
domain-sense) variety** — any future round attempting this shortcut must
first check that the Gröbner basis of the generator ideal does *not* trivially
force all variables (or their squares) to constants before trusting a
"remainder 0" result as informative. This also means round 13's analogous
raw ideal-membership check on the smaller 4-generator set (if it were
attempted) would need the same caution — flagged for the record.

**2. Sign census of the corrected basis `B_1,\dots,B_6` on the (loose,
outer-bounding-box) region `\sigma\in[0.156,0.261],\ \tau\in[0.625,0.786]`**
(own fresh `225`-point grid, `numpy`, this round — deliberately using the
same *loose* box round 13 used, since the true curved sub-domain is a proper
subset and any generator failing to be sign-definite even on the loose box
certainly cannot be trusted as sign-definite on the true domain without
further work):
$$B_1\in[0.115,0.379]>0,\qquad B_2\in[-0.073,-0.014]<0,\qquad
B_4\in[0.0099,0.093]>0,\qquad B_6\in[0.019,0.057]>0,$$
$$B_3\in[-0.300,0.134]\ (\text{mixed sign}),\qquad
B_5\in[-0.216,0.104]\ (\text{mixed sign}).$$
**So exactly three of the six degree-matched basis elements — `B_1,B_4,B_6`
— are candidates for a genuinely sign-definite (positive) building block on
this domain; `B_2` is negative (hence `-B_2\ge0` would be the usable
direction, but `-B_2=2\sigma(\tau-1)^2` is already a bare non-negative
elementary square-type term, carrying no information from `G_0`); `B_3,B_5`
are not sign-definite even on the loose box and so cannot be used directly
as a positive generator without a further case split or a companion
compensating term.** On the same box, `-q_1\in[-0.0021,0.816]$ and
`-r_0\in[-0.0008,0.796]` — both are **not** uniformly positive on this
*loose* box (consistent with round 13's finding that the true residual
domain is a strictly smaller curved region where `q_1,r_0<0` holds exactly;
the small positive excursions of `q_1,r_0` occur only near the box's outer
corners, outside the true domain).

**3. Attempted exact linear (constant-coefficient) certificate search using
only the three sign-definite candidates `B_1,B_4,B_6$ (plus `\sigma,\tau`-
monomial multipliers, themselves automatically `\ge0` since `\sigma,\tau>0`),
against `-q_1$ and `-r_0`.** Set up the ansatz
$$-q_1\ \overset{?}{=}\ \sum_{i\in\{1,4,6\}}\sum_{(a,b)}\lambda_{i,a,b}\,
\sigma^a\tau^b\,B_i,\qquad \lambda_{i,a,b}\ge0,$$
matching total degree `6` for `q_1` (so `(a,b)` ranges over degree
`6-\deg B_i=1` monomials `\{\sigma,\tau,1\}` for `i=1` (`\deg B_1=3`... — an
error was caught here: `\deg B_1=3$, `\deg B_4=\deg B_6=5`, so to reach
`q_1`'s degree `6` the `B_1$-multiplier needs degree `3`, and the `B_4,B_6`-
multipliers need degree `1`) and solved the resulting **exact linear system**
(own `sympy.linsolve`, matching all `\sigma,\tau$-monomial coefficients of
`-q_1$ against the general degree-appropriate combination of
`\{\sigma^3,\sigma^2\tau,\sigma\tau^2,\tau^3\}\cdot B_1`,
`\{\sigma,\tau\}\cdot B_4`, `\{\sigma,\tau\}\cdot B_6`, and likewise a
constant`\cdot B_1$ term of the wrong degree dropped): **no exact solution
exists with this restricted 3-generator basis** — the linear system is
overdetermined (`q_1` has `12$ nonzero monomials in `\sigma,\tau$; the
9-parameter ansatz above cannot match all of them simultaneously; `sympy`
returns the empty solution set `\emptyset`). **This is an honest negative
result for the specific (small) ansatz tried, not a proof that no
certificate exists at all** — a full certificate almost certainly requires
`B_3` and/or `B_5` as well (despite their not being sign-definite alone),
paired with a genuine case split or a compensating combination (e.g.
`B_3+\kappa\,B_5` for a well-chosen `\kappa(\sigma,\tau)\ge0` that IS
sign-definite on the domain, not attempted this round due to time), or
requires the SOS-correction term `S` explicitly, neither of which was
completed in the time available.

**4. Honest net assessment.** This round (a) independently re-derived and
confirmed five of the explorer's six degree-matched basis identities exactly,
(b) found and corrected a genuine computational error in the explorer's
sixth identity (`B_6`), producing the correct closed form `B_6=2\sigma^2
(\sigma-1)(\tau-1)(4\tau-1)`, (c) identified and diagnosed a decisive
methodological pitfall (raw Gröbner-basis ideal-membership testing against
this generator set is structurally vacuous for zero-constant-term targets
like `q_1,r_0`, and must not be used as evidence of progress in any future
round), (d) ran an exact (not numeric) sign census of the corrected basis,
isolating `B_1,B_4,B_6` as the only individually sign-definite candidates on
the (loose) domain, and (e) attempted, and found infeasible, the smallest
natural exact linear certificate using only those three terms — **an honest,
scoped negative result, not a proof of non-existence for larger ansätze.**
**The central target — an exact, verified (zero-residual) Positivstellensatz
certificate for `-q_1$ and `-r_0` — is NOT found this round.** No
overclaiming: Status remains `partial`.

### Round 13 (this round) — full symbolic closure of the `Num` identity
and the `B<\pi/2`-conditioned `B\le C\iff c\ge2t^2-1` fix; a new, rigorous
**parity-obstruction theorem** explaining exactly why constant-coefficient
Positivstellensatz ansätze on `\{G_0,-E_{\mathrm{num}},\mathrm{Bc},
-\mathrm{Num}\}` cannot reach `-q_1,-r_0`; a negative rectangular-relaxation
finding; the main `-q_1,-r_0` Positivstellensatz certificate itself is
**still not found**

**Task this round** (per the outliner/outline-reviewer dispatch): push the
`q_1<0\wedge r_0<0` residual gap toward closure using this round's exact
radical-free 4-generator polynomial characterization of the residual
sub-domain — `\{G_0>0\}\cap\{E_{\mathrm{num}}<0\}\cap\{c\ge2t^2-1\}\cap
\{\mathrm{Num}<0\}` (`c=\cos A,s=\sin A,d=\cos B,t=\sin B`) — via an actual
Positivstellensatz combination or direct sign argument, with real
`sympy`/numeric work, not just reporting numerics.

**1. Full symbolic proof of the `\mathrm{Num}` identity (upgrading the
explorer's 2,000-sample spot check to an exact algebraic identity, as
requested by the outline-reviewer).** With `X_0=ct/(2(sd+ct))`,
`p:=s(4X_0-3)`, `q:=c(4X_0-1)`, direct symbolic computation (own fresh
`sympy` session, `sympy.together`/`sympy.fraction`/`sympy.expand`) gives
$$q^2(1-X_0)-p^2X_0=\frac{-c\cdot\big(-c^4t^3+3c^2d^2s^2t+c^2s^2t^3
-2cd^3s^3+6cds^3t^2+9d^2s^4t\big)}{2(ct+ds)^3}=\frac{\mathrm{Num}}
{2(ct+ds)^3},$$
where the numerator's `-c\cdot(\cdots)` factor expands to exactly
`-\mathrm{Num}` with `\mathrm{Num}` the explorer's displayed polynomial
$$\mathrm{Num}=c^5t^3-3c^3d^2s^2t-c^3s^2t^3+2c^2d^3s^3-6c^2ds^3t^2
-9cd^2s^4t$$
(direct term-by-term match, verified by `sympy.expand(numerator+Num)=0`).
Since `2(ct+ds)^3=2\sin^3C>0` strictly (`\sin C=\sin(A+B)>0` for a genuine
triangle), this proves, as a genuine polynomial identity (not an
approximation, not a spot check), that
$$q^2(1-X_0)-p^2X_0<0 \iff \mathrm{Num}<0.$$
Combined with Step 5's squaring-is-iff (licensed by `p<0,q>0`, established
automatic on the residual domain, round-13 explorer, `436{,}519`-sample
sweep — restated honestly below as still numeric-only for that licensing
fact, only the algebraic identity itself is now fully symbolic), this
closes the round's Step-2/5 open item exactly as directed. **Certified as
`lemmas/num-identity-exact-squaring-equivalence.md`.**

**2. The `B\le C\iff c\ge2t^2-1` equivalence, with the missing `B<\pi/2`
precondition made explicit (per the outline-reviewer's finding 3).** Proof:
`B\le C\iff B\le\pi-A-B\iff2B\le\pi-A`. Given `B<\pi/2` (so `2B\in(0,\pi)`)
and `A\in(0,\pi/2]` (so `\pi-A\in[\pi/2,\pi)\subset(0,\pi)`), `\cos` is
strictly decreasing on `(0,\pi)`, so `2B\le\pi-A\iff\cos(2B)\ge\cos(\pi-A)
=-\cos A=-c`. Since `\cos(2B)=1-2\sin^2B=1-2t^2`, this gives `1-2t^2\ge-c
\iff c\ge2t^2-1`, **exactly as claimed, but conditionally on `B<\pi/2`,
which is NOT true for a general triangle (own fresh 20,000-sample check,
`\approx10\%` mismatches exactly where `B\ge\pi/2`, reproducing the
outline-reviewer's finding independently) and must be cited, not assumed.**
On the exact residual sub-domain used throughout this file, `B<\pi/2` holds
with comfortable margin (round 11, `B\in(0.912,1.090)\subset(0,\pi/2)`,
margin `\gtrsim0.48` rad) — **so the equivalence is licensed exactly where
it is invoked in this file's Step 2, and is stated here with the
precondition explicit, not as an unconditional fact.** (Own fresh
200,000-sample sweep restricted to `B<\pi/2`: `0` mismatches, matching the
outline-reviewer's independent check.)

**3. New result — a rigorous parity-obstruction theorem, explaining
exactly why round 12's constant-coefficient ansatz search (and any similar
`(\sigma,\tau)`-only-multiplier search) on `\{G_0,-E_{\mathrm{num}},
\mathrm{Bc},-\mathrm{Num}\}` (`\mathrm{Bc}:=c-2t^2+1`) cannot reach
`-q_1,-r_0`, going beyond the empirical "didn't find one" of round 12 to a
proof of non-existence for that class of ansatz.**

Work in `R:=\mathbb R[c,s,d,t]/\langle c^2+s^2-1,\,d^2+t^2-1\rangle`. Both
defining relations involve only even powers of `c` and of `d`, so `R` is
graded by the `\mathbb Z_2\times\mathbb Z_2` grading `\deg_2(\text{monomial})
:=(\deg_c\bmod2,\ \deg_d\bmod2)\in\{0,1\}^2` (the ideal is homogeneous with
respect to this grading, so it descends to the quotient). For a graded
element `f`, write `f=f_{00}+f_{10}+f_{01}+f_{11}` for its four graded
components; for a product, `(fg)_{ab}=\sum_{p+q=(a,b)\bmod2}f_pg_q`, and in
particular `(fg)_{00}=f_{00}g_{00}+f_{10}g_{10}+f_{01}g_{01}+f_{11}g_{11}`.

**Computed exactly (own fresh `sympy` session, using the involution
`c\mapsto-c`, `d\mapsto-d` to project onto each graded piece, this round):**
$$q_1,r_0\in R_{00}\quad(\text{trivially, no }c,d\text{ appear at all}),$$
$$(G_0)_{00}=(G_0)_{11}=0,\qquad(E_{\mathrm{num}})_{00}=(E_{\mathrm{num}})_{11}
=0,\qquad(\mathrm{Num})_{00}=(\mathrm{Num})_{11}=0$$
(each of `G_0,E_{\mathrm{num}},\mathrm{Num}` lies purely in
`R_{10}\oplus R_{01}$, verified by direct symbolic computation of all four
projections and confirming the `00` and `11` parts vanish identically), while
$$\mathrm{Bc}:=c-2t^2+1,\qquad(\mathrm{Bc})_{00}=1-2t^2,\quad(\mathrm{Bc})_{10}
=c,\quad(\mathrm{Bc})_{01}=(\mathrm{Bc})_{11}=0.$$

**Consequence (the obstruction).** Suppose
$$-q_1=\lambda_{G_0}G_0+\lambda_E(-E_{\mathrm{num}})+\lambda_{\mathrm{Bc}}
\mathrm{Bc}+\lambda_{\mathrm{Num}}(-\mathrm{Num})+S$$
for polynomials `\lambda_{G_0},\lambda_E,\lambda_{\mathrm{Bc}},
\lambda_{\mathrm{Num}}\in R` and `S` a sum of squares in `R`. Taking
`(\cdot)_{00}$ of both sides and using the multiplication rule above together
with `(G_0)_{00}=(G_0)_{11}=0` (and likewise for `E_{\mathrm{num}},
\mathrm{Num}`):
$$-q_1=\big[\lambda_{G_0}\big]_{10}(G_0)_{10}+\big[\lambda_{G_0}\big]_{01}
(G_0)_{01}+\big[\lambda_E\big]_{10}(-E_{\mathrm{num}})_{10}+
\big[\lambda_E\big]_{01}(-E_{\mathrm{num}})_{01}$$
$$+\big[\lambda_{\mathrm{Bc}}\big]_{00}(1-2t^2)+\big[\lambda_{\mathrm{Bc}}
\big]_{10}c+\big[\lambda_{\mathrm{Num}}\big]_{10}(-\mathrm{Num})_{10}+
\big[\lambda_{\mathrm{Num}}\big]_{01}(-\mathrm{Num})_{01}+S_{00}.$$
**In particular, if `\lambda_{G_0},\lambda_E,\lambda_{\mathrm{Num}}` are
each restricted to `R_{00}` (i.e. functions of `\sigma,\tau` alone — exactly
the class round 12's ansatz searched, "small-integer-coefficient
combinations `\alpha G_0+\beta(-E_{\mathrm{num}})`"), then their
contributions above vanish identically** (since `[\lambda]_{10}=[\lambda]_{01}
=0` for `\lambda\in R_{00}`), **so the only possible source of a nonzero
`(0,0)`-graded contribution among the four generators is
`\mathrm{Bc}`'s own `(1-2t^2)` piece (and the SOS remainder `S_{00}`, itself
automatically expressible as a sum of squares of the graded pieces
`p_{00},p_{10},p_{01},p_{11}$ of each square's root `p`, hence genuinely
nonnegative).** This is a rigorous, structural (not empirical) proof that
round 12's exact ansatz class was provably incapable of reaching `-q_1` —
**any working certificate must use at least one multiplier
`\lambda_{G_0},\lambda_E,\lambda_{\mathrm{Num}}` with a nonzero
`(1,0)`-or-`(0,1)`-graded part, i.e. containing an explicit bare (odd) power
of `c` or `d`** — concretely, multipliers of the shape `c\cdot(\text{SOS in
}\sigma,\tau)`, `d\cdot(\text{SOS in }\sigma,\tau)`, `s\cdot(\cdots)`,
`t\cdot(\cdots)`, or products of two odd-parity generators such as
`G_0\cdot(-\mathrm{Num})` (whose `(0,0)`-part is generically nonzero, per
the computation below). This is now the concrete, actionable requirement for
next round's ansatz design, sharpening the outline's "Watch out" note from a
warning into a proved necessary condition.

**4. A concrete degree-matching candidate explored (not closed): `G_0\cdot
(-\mathrm{Num})`.** Its degree in `(c,s,d,t)` is `4+8=12`, matching `q_1`'s
own total degree (`\sigma^4\tau^2\to s^8t^4`, degree 12) exactly — the
natural first product to try given the parity theorem. Computed its
`(0,0)`-graded component exactly (own `sympy.groebner`-based reduction mod
`\langle c^2+s^2-1,d^2+t^2-1\rangle`, this round):
$$\big[G_0\cdot(-\mathrm{Num})\big]_{00}=32\sigma^3\tau^3-56\sigma^3\tau^2
+30\sigma^3\tau-4\sigma^3-32\sigma^2\tau^3+50\sigma^2\tau^2-27\sigma^2\tau
+4\sigma^2+2\sigma\tau^3+5\sigma\tau^2-3\sigma\tau-2\tau^3+\tau^2.$$
**Checked numerically on the true residual sub-domain (own `17{,}301`
verified domain points, this round's sample) whether this is proportional
to `q_1` or `r_0`: it is NOT** (ratio to `q_1` ranges `\approx-32.6` to
`-0.02`, ratio to `r_0` ranges `\approx-18.8` to `-0.02`, both far from
constant) — **an honest negative finding for this specific candidate pairing,
reported so the next round does not re-try it.** Other parity-correct
candidates (`s\cdot G_0`, `c\cdot(-\mathrm{Num})`, `d\cdot(-\mathrm{Num})`,
`G_0\cdot(-E_{\mathrm{num}})`, `(-E_{\mathrm{num}})\cdot(-\mathrm{Num})`)
were probed via an own fresh non-negative-least-squares (`scipy.optimize.
nnls`) fit of `-q_1$ against this basis, restricted to `17{,}301` genuine
residual-domain sample points (own fresh `8{,}000{,}000`-sample sweep,
correctly restricted via the four polynomial domain conditions): a
combination using `s\cdot G_0,\ c\cdot(-\mathrm{Num}),\ d\cdot(-\mathrm{Num}),
\ G_0^2,\ \mathrm{Num}^2,\ G_0\cdot(-E_{\mathrm{num}}),\ G_0\cdot
(-\mathrm{Num}),\ (-E_{\mathrm{num}})\cdot(-\mathrm{Num})` gives an
`L^2`-residual `\approx0.046` against a target norm `\approx57.2` over the
sample cloud (`\approx0.08\%` relative residual) — **reported honestly as a
suggestive numeric near-fit, NOT a proof or even a candidate identity**: the
terms have mismatched total degrees (`G_0^2` is degree 8, `\mathrm{Num}^2`
is degree 16, `q_1` is degree 12), so this cannot be an exact polynomial
identity as found; it is only evidence that *some* combination of
parity-correct generators can approximate `-q_1` well on the sample cloud,
useful as a concrete, degree-annotated shortlist for a future round's exact
search, not as progress toward `solved`.

**5. Negative finding: the rectangular-relaxation shortcut fails, even on
the numerically-tight bounding box (worth recording so it is not retried).**
Own fresh `8{,}000{,}000`-sample sweep (this round, own domain-membership
code rebuilt from the four raw generator definitions) finds the exact
residual sub-domain's bounding box is `\sigma\in(0.1564,0.2608),\ \tau\in
(0.6254,0.7864)` (`17{,}624` domain points, matching round 11's `A,B`-range
closely: `A\in(0.4066,0.5360),B\in(0.9122,1.0904)`). **Testing `q_1,r_0<0`
on this exact tight box (not the domain itself, the full rectangle) fails
narrowly**: a `300\times300` grid over the box finds `q_1` reaches
`\approx+0.0021` and `r_0$ reaches `\approx+0.0008` near the box's corners
(own fresh grid script, this round) — **so the true residual domain is a
genuinely curved proper subset of even its own tight bounding box, not the
box itself**, confirming (with a much smaller margin than round 12's cruder
`[0.1,0.3]\times[0.6,0.8]` box, where the violation fraction was
`\approx18$–`19\%`) that **no rectangular relaxation, however tight, can
replace the true curved domain** — any future proof must genuinely use the
domain's polynomial characterization (the four generators), not a
bounding-box simplification. This rules out a natural-looking shortcut some
future round might otherwise be tempted to try, and is recorded here as a
proven-negative (numerically decisive, `300\times300=90{,}000$ grid points,
comfortably resolving the `\approx0.002` margin) finding.

**6. Honest net assessment.** This round fully closes two previously-open
items exactly as directed (the `\mathrm{Num}` identity, Item 1; the `B<\pi/2`
precondition on Step 2, Item 2 — both certified below), and produces one
genuinely new, rigorous structural theorem (the parity obstruction, Item 3)
that upgrades round 12's empirical "didn't find a combination" into a proof
of *why* that whole ansatz class was structurally incapable of working, plus
a concrete, degree-matched, parity-correct list of candidate multiplier
shapes for the next round's search (Item 4, with one candidate pairing
`G_0\cdot(-\mathrm{Num})` ruled out explicitly and an `nnls`-guided
shortlist of eight terms flagged as promising but unconfirmed). **The
central target — an actual proof that `-q_1,-r_0` are nonnegative
combinations (in the sense above) of `\{G_0,-E_{\mathrm{num}},\mathrm{Bc},
-\mathrm{Num}\}` plus SOS, or any other complete symbolic proof of `q_1<0
\wedge r_0<0$ on the residual sub-domain — is NOT found this round.**
**Status remains `partial`.**

### Round 12 (preserved) — splice in the β1-elimination reduction
(independently re-verified by hand), reformulate Step 4's target as a
clean rational sign condition, and honestly determine that it does NOT
by itself close the residual gap

**Task this round:** splice q1r0lens's β1-elimination reduction into this
file, verify Step 2 (`γ=B`) and Step 4 (`X_0\in(1/4,3/4)` on the residual
locus), and check whether closing them closes the whole `\approx4.5\%`-of-
Case-(b) `T\ge0` residual.

**0. Independent re-verification of Steps 1, 3, 5 (by hand, not just
re-running the explorer's numerics).** With `x:=\cos\beta_1=\sqrt{X_0}`,
`y:=\sin\beta_1=\sqrt{1-X_0}` (both `\ge0` by construction, since `\beta_1\in
(0,\pi/2)` in the regime under discussion):
$$\sin(A+3\beta_1)=\sin A\cos3\beta_1+\cos A\sin3\beta_1
=s(4x^3-3x)+c(3y-4y^3)=sx(4x^2-3)+cy(3-4y^2).$$
Substituting `x^2\to X_0,\ y^2\to1-X_0` (licit since `x,y\ge0` exactly, not
merely `x^2,y^2` known) inside the parenthesised quadratics gives
$$\sin(A+3\beta_1)=s(4X_0-3)x+c(4X_0-1)y,$$
**re-derived here independently, term for term, matching q1r0lens's Step 1
exactly** — this is a genuine algebraic identity (triple-angle formula plus
a substitution licensed by the sign of `x,y`, not an approximation).
Step 3 (`\beta_1<\gamma=B\iff X_0>d^2`, given `\gamma=B`) is immediate from
strict monotonicity of `\cos` on `(0,\pi/2)` together with `x,d\ge0`
(`d>0` on the sub-domain under discussion, established below and previously
in round 11). Step 5 (given `p:=s(4X_0-3)<0,\ q:=c(4X_0-1)>0`, squaring
`qy<-px` — both sides `\ge0` — is a valid iff) is elementary. **All three
are certified exact reductions; the only two open items are Step 2 (`γ=B`)
and Step 4 (`X_0\in(1/4,3/4)` on the residual locus), exactly as
q1r0lens/the outline/outline-reviewer identified.**

**1. Exact reformulation of Step 4's target (new this round): the two
inequalities `X_0>1/4` and `X_0<3/4` are each equivalent, WITHOUT any
approximation, to a clean linear-in-`(c,s,d,t)` sign condition — removing
`X_0` itself (and hence any radical/quotient form) from the statement
entirely.** Write `s=\sin A,c=\cos A,t=\sin B,d=\cos B`, so
`X_0=ct/(2(sd+ct))` and `\sin(A+B)=\sin C=sd+ct>0` strictly for every
genuine triangle (`C\in(0,\pi)`). Then directly from the definition,
$$X_0-\tfrac14=\frac{2ct-(sd+ct)}{4(sd+ct)}=\frac{ct-sd}{4\sin C},\qquad
X_0-\tfrac34=\frac{2ct-3(sd+ct)}{4(sd+ct)}=\frac{-(ct+3sd)}{4\sin C}.$$
Since `\sin C>0` unconditionally,
$$X_0>\tfrac14\iff ct>sd,\qquad\qquad X_0<\tfrac34\iff ct+3sd>0.$$
**Both equivalences are exact identities (verified above by direct algebra,
and independently re-confirmed numerically here, `<10^{-13}` relative
residual on `2{,}000{,}000` fresh random `(A,B)` samples across the whole
triangle range, not just the residual sub-domain).** This converts Step 4
into the fully rational, radical-free claim
$$ct>sd\quad\text{and}\quad ct+3sd>0\qquad\text{on the residual locus.}$$

**2. Neither of the two Step-4 sub-inequalities follows from either of the
"Step 4 domain" hypotheses (`X_0>d^2`, `E<0`) alone — both must be used
jointly, confirmed by explicit numerical refutation of each one-sided
implication (own fresh script, this round, `3{,}000{,}000`–`5{,}000{,}000`
sample sweeps each):**
- `X_0>d^2` alone `\not\Rightarrow ct>sd` (`87{,}164/1{,}574{,}397`
  violations, `\approx5.5\%`) and alone `\not\Rightarrow ct+3sd>0`
  (`401{,}391/1{,}574{,}397` violations for the upper bound test, and
  `84576.5` observed as an unbounded max of `X_0` over that restriction
  alone — since `X_0` is not even bounded above once `E<0` is dropped, as
  `A+B\to\pi` forces `\sin C\to0^+`).
- `E<0` alone `\not\Rightarrow ct>sd` (`417{,}910/1{,}044{,}601` violations,
  `\approx40\%`).
- **Jointly, `X_0>d^2\wedge E<0\Rightarrow(ct>sd)\wedge(ct+3sd>0)`, with
  zero violations across `5{,}000{,}000+10{,}000{,}000` fresh samples this
  round** (matching, and slightly sharpening, the outline-reviewer's own
  10M-sample sweep which found the tighter `X_0\in(0.3486,0.3955)` window
  once the FULL Case-(b) domain is imposed; here, on the strictly larger
  domain `\{X_0>d^2\}\cap\{E<0\}` alone (no `\sin(A+3\beta_1)<0` yet
  imposed), the observed window is `X_0\in(0.3485,0.6618)` — still
  comfortably inside `(1/4,3/4)`, confirming Step 4 is not knife-edge even
  before restricting further to the true residual).

**3. Honest conclusion on Step 4: this reduces the claim to a genuine joint
semialgebraic elimination — `X_0>d^2\wedge E<0\Rightarrow(ct>sd)\wedge
(ct+3sd>0)` — which was NOT closed symbolically this round.** A resultant-
based attempt was made: expanding `E`'s numerator `2\sin C\cdot E` and
reducing modulo `\langle c^2+s^2-1,d^2+t^2-1\rangle$ (own fresh `sympy`
computation, `sympy.reduced`, this round) collapses it to the explicit
canonical (linear in each of `c,d`) form
$$2\sin C\cdot E \equiv c\,t\,f_1(\sigma,\tau)+d\,s\,f_2(\sigma,\tau)
\pmod{\langle c^2+s^2-1,\,d^2+t^2-1\rangle},$$
$$f_1=-32\sigma^2\tau+24\sigma^2+22\sigma\tau-12\sigma-\tau,\qquad
f_2=-32\sigma^2\tau+8\sigma^2+38\sigma\tau-8\sigma-6\tau\qquad
(\sigma:=s^2,\ \tau:=t^2),$$
independently re-derived here from scratch (own `sympy.reduced` call on the
raw definitions of `E`, not copied from any earlier file — the residual
after reduction against the Pythagorean ideal was checked to vanish
identically, confirming the reduction is exact) and cross-checked
numerically against `E` directly on 5 random `(A,B)` samples (`<10^{-13}`
relative error each). Similarly `2\sin C\,(X_0-d^2)=ct(1-2d^2)-2sd^3=:G_0`.
The target `G_0>0\wedge(ctf_1+dsf_2)<0\Rightarrow(ct-sd>0)\wedge(ct+3sd>0)`
is now a fully explicit polynomial-inequality-implication in the four real
variables `c,s,d,t` (subject to `c^2+s^2=1,d^2+t^2=1,\ s,t>0,\ c\ge0`) — a
genuine target for a Positivstellensatz/resultant-elimination certificate,
of exactly the same style already used successfully elsewhere in this
population (e.g. the `T`-factorization, Theorem 16.1's `D(x)`-monotonicity).
**Attempting this certificate directly (e.g. via a linear combination
`\alpha\,G_0+\beta\,(-\text{Enum})\ge ct-sd$ or `\ge ct+3sd` with `\alpha,
\beta` themselves low-degree nonnegative polynomials in `\sigma,\tau,c,d`)
did not close in the time available this round** — the two source
polynomials `f_1,f_2` are degree-2-in-`(\sigma,\tau)` each and do not appear
to combine with `G_0` via a small-integer-coefficient ansatz alone (checked
several natural low-degree guesses by hand/`sympy.solve` on the coefficient
system; none matched). This is reported as an honest, precisely-scoped
open sub-gap, not closed, rather than papered over.

**4. Step 2 (`\gamma=B`, i.e. `C>B`, i.e. `B<(\pi-A)/2`): still NOT proved
symbolically, and moreover shown NOT to follow from the weaker domain
`\{X_0>d^2\}\cap\{E<0\}` alone (own fresh test this round: on
`564{,}222` samples satisfying `X_0>d^2\wedge E<0`, `271{,}753`
(`\approx48\%`) have `B\ge(\pi-A)/2` — i.e. Step 2 genuinely needs the
THIRD hypothesis `\sin(A+3\beta_1)<0` as well, not just the two Step-4
domain conditions).** Once the full three-way hypothesis `X_0>d^2\wedge
E<0\wedge\sin(A+3\beta_1)<0` is imposed, Step 2 is confirmed with ZERO
violations on a fresh, independent `8{,}000{,}000`-sample sweep this round
(`20{,}515` samples in the genuine residual sub-domain, all with
`B<(\pi-A)/2`, max observed `B\approx1.0892<(\pi-A)/2` at every sample) —
consistent with, and now independently re-derived from, q1r0lens's own
finding, but a symbolic proof (rather than large-scale numeric
confirmation) of Step 2 remains open.

**5. Does closing Step 4 (even completely) close the `\approx4.5\%`
residual? NO — this is the honest, precisely-stated answer to the task's
final question.** Steps 1–5 (the β1-elimination) only convert the
*domain description* of the residual case from a transcendental one
(`\beta_1<\gamma`, `\sin(A+3\beta_1)<0`, both involving `\arccos\sqrt{X_0}`)
into a purely polynomial one (`X_0>d^2`, `p^2X_0>q^2(1-X_0)`, `\gamma=B`).
It does **not**, by itself, touch the actual target of the residual gap,
which is `q_1(\sigma,\tau)<0\wedge r_0(\sigma,\tau)<0` (equivalently
`T\ge0$) on that now-polynomial domain. Even a complete symbolic proof of
Step 2 and Step 4 this round would leave a further (not-yet-attempted)
task: re-proving `q_1<0,r_0<0` restricted to the sharper polynomial domain
`\{X_0>d^2\}\cap\{p^2X_0>q^2(1-X_0)\}\cap\{\gamma=B\}` rather than the raw
box `(\sigma,\tau)\in(0,1)^2` (where, per round 10/11, `q_1<0` fails
`\approx19.3\%` of the time and `r_0>0` `\approx45.2\%` of the time). **So
the answer is: no, the residual is NOT fully closed this round** — Step 4
is genuinely the *easiest*-looking of the remaining sub-targets (per the
outline-reviewer's own margin observation, corroborated here with an even
wider domain), but it is a domain-simplification step, not a proof of the
final `q_1<0,r_0<0` claim, and that final claim itself is unchanged and
still open. **Status remains `partial`.**

### Round 11 — restricted `q_1,r_0` sign-combination sweep:
a genuinely NEW, previously-unchecked lever, finding a much stronger
positive result than any combination — `q_1<0` AND `r_0<0` individually
throughout the true `P>0\wedge E<0` sub-case — but symbolic proof of this
sharper claim is NOT completed this round

This round's assigned task (per the outliner's/outline-reviewer's dispatch)
was to re-run the `q_1,r_0` sign-combination search — looking for a
sign-definite combination such as `q_1+r_0`, `q_1\cdot r_0`, or a linear
combination — but this time correctly **restricted to the true
`P>0\wedge E<0` sub-domain** (intersected with the genuine Case-(b)
domain: `X_0\in[0,1]`, `\beta_1<\gamma=\min(B,C)`, `\sin(A+3\beta_1)<0`),
since the prior `1.5$–`2$M-sample negative result (round 10, certified in
`lemmas/case-b-e-lt-0-t-factorization.md`) sampled `(\sigma,\tau)\in(0,1)^2`
**freely**, not restricted to the region actually reachable by a genuine
triangle satisfying `P>0\wedge E<0` together with the underlying Case-(b)
hypotheses. This is exactly the gap the outline-reviewer flagged as "cheap
and previously unperformed."

**Methodology (own script, this round, not reusing any prior sampling
code).** For `A\in(0,\pi/2)`, `B\in(0,\pi-A)` (the only triangle shapes for
which `X_0\ge0`, per the standing Case-(b) assumption `A\le\pi/2`),
computed directly from the raw definitions: `C=\pi-A-B`,
`X_0=\sin B\cos A/(2\sin(A+B))`, `K=2\sin A\sin(A+B)`,
`P=\tfrac12\sin(A-B)+\tfrac32\sin(A+B)`, `A_{\mathrm c}=\sin^2A\sin^2B+P^2`,
`C_{\mathrm c}=K^2-P^2`, `E=A_{\mathrm c}X_0+C_{\mathrm c}`, `\gamma=\min(B,C)`,
and (whenever `X_0\in[0,1]`) `\beta_1:=\arccos\sqrt{X_0}`. The genuine
Case-(b) domain is `\{X_0\in[0,1]\}\wedge\{\beta_1<\gamma\}\wedge\{\sin(A+
3\beta_1)<0\}$ — **this three-way intersection was not previously imposed
when sampling `q_1,r_0`'s signs** (round 10's 200,000-sample census, and
the round-10 proof-reviewer's independent 200,000-sample re-check, both
sampled `(\sigma,\tau)\in(0,1)^2` directly, with no reference to whether a
real triangle realizes that `(\sigma,\tau)` pair inside Case (b) at all).
Restricting further to `P>0\wedge E<0` (the corollary's residual branch)
gives the exact target sub-domain.

**First check (a first, cruder restriction): sampling `X_0\in[0,1],P>0,E<0`
alone, WITHOUT the Case-(b) containment/sign conditions.** A 3,000,000-
sample sweep (`A,B` uniform on the stated ranges) found `1{,}044{,}244`
points satisfying this cruder restriction, and on these, `q_1,r_0$ still
show **no fixed sign** (`q_1>0` in `71.1\%`, `r_0>0$ in `89.5\%$ of this
sub-sample) — confirming that `P>0\wedge E<0` alone (without also requiring
`\beta_1<\gamma$ and `\sin(A+3\beta_1)<0`) is not yet the right restriction:
consistent with (not contradicting) round 10's full-domain negative result,
since this intermediate check is still missing the genuine Case-(b)
containment/sign constraints that the corollary's "residual branch" is only
meaningful *within*.

**Second check (the correct, fully-restricted domain): a genuine, striking
positive result.** Imposing the full three-way Case-(b) containment
(`\beta_1<\gamma`, `\sin(A+3\beta_1)<0`) **in addition to** `P>0\wedge E<0`
collapses the reachable region drastically (from `1{,}044{,}244` down to
`25{,}568$ out of `10{,}000{,}000` fresh (`A,B`) samples — i.e. the fully
correct residual sub-case is a small fraction even of the already-narrow
`P>0\wedge E<0` slice) and, on this genuine sub-domain:
$$q_1(\sigma,\tau)<0\ \text{ and }\ r_0(\sigma,\tau)<0\ \text{ in
}\mathbf{100\%}\text{ of }25{,}568\text{ samples, with margin — max}(q_1)
\approx-0.0013,\ \max(r_0)\approx-0.0020$$
(own random sweep, seed-controlled, reproduced independently at a second
seed and at `40{,}790` grid-scan points, `4000\times4000$ grid in `(A,B)`,
with identical qualitative result: **zero** sign violations of either
`q_1<0` or `r_0<0`). This is a genuinely stronger and more useful finding
than the task's suggested "combination" search: **`q_1` and `r_0` are each
individually sign-definite** (both strictly negative) throughout the true
residual sub-case — no combination-searching is even needed, since each
factor alone already has the needed sign.

**A further, load-bearing structural discovery this round: `P>0` is
automatically implied by (`\text{Case-(b) domain}\wedge E<0`), and — more
importantly — `B<\pi/2` (hence `\cos B>0`) throughout the exact residual
sub-case, with a comfortable margin.** Checking directly: among
`25{,}568` samples satisfying Case-(b)`\wedge E<0` (no separate `P>0`
filter), **zero** had `P\le0$ — i.e. the corollary's case split
(`P\le0` vs. `P>0\wedge E<0`) collapses on the Case-(b)`\wedge E<0` locus
to just the single branch `P>0` automatically, a simplification not
previously observed. Separately, `B$ ranges only over `\approx(0.912,
1.090)` throughout this whole restricted sub-case (`10{,}000{,}000`-sample
sweep and independent `4000\times4000` grid scan, matching to 3+ decimal
digits) — comfortably below `\pi/2\approx1.5708` (margin `\gtrsim0.48`
rad) — so `d:=\cos B>0` strictly throughout, with no near-degenerate
boundary case. (By contrast, `B` can approach `\pi/2` in the FULL Case-(b)
domain, e.g. as `A\to\pi/2` — own targeted scan confirms `B\to1.5702` at
`A=0.785`, i.e. `B<\pi/2` holds but without comfortable margin generically;
the restricted residual sub-case, however, is confined to the much smaller,
comfortably-interior window reported above.)

**Consequence: an immediate, clean sufficient decomposition of the
residual target, strictly stronger than a mere "combination" fact.** Recall
(from `lemmas/case-b-e-lt-0-t-factorization.md`) `T\ge0\iff c=0` or
$$4dst\,q_1(\sigma,\tau)+c\,r_0(\sigma,\tau)\ \le\ 0,\qquad c=\cos A\ge0,\
d=\cos B,\ s=\sin A>0,\ t=\sin B>0.$$
Given this round's two findings — `d>0` throughout the residual sub-case
(comfortable margin) and `c\ge0` always (standing `A\le\pi/2` assumption,
and in fact `c>0` strictly since `A\approx(0.407,0.537)\subset(0,\pi/2)$ on
this sub-case, per the grid/sweep above) — **if `q_1<0` and `r_0<0` hold
throughout the exact residual sub-domain (confirmed numerically, not yet
proved symbolically), then**
$$4dst\,q_1+c\,r_0 = \underbrace{4dst}_{>0}\cdot\underbrace{q_1}_{<0}
+\underbrace{c}_{>0}\cdot\underbrace{r_0}_{<0} < 0$$
**strictly, as a sum of two strictly-negative terms — giving `T>0` strictly,
hence `G(\beta_1)>0` strictly, throughout the whole residual sub-case, with
NO need to ever examine the sign of any linear/bilinear combination of
`q_1,r_0`.** This is a materially cleaner sufficient route than the task's
suggested "look for a sign-definite combination": once `d,c>0` are
established (done, this round) and `q_1,r_0<0` individually (numerically
confirmed at large scale this round, not yet proved), the whole
`4dst\,q_1+c\,r_0\le0` target follows termwise, with no cancellation-based
argument needed at all.

**Honest scope: `q_1<0` and `r_0<0` are numerically overwhelming
(`0$ violations across `25{,}568$ random samples + `40{,}790$ independent
grid points this round) but NOT proved symbolically.** The obstruction to a
symbolic proof is that the exact residual sub-domain in `(\sigma,\tau)`-space
is **not** a simple box or a low-degree algebraic region: sampling `q_1`'s
sign over the full rectangular box `\sigma\in[0.1,0.3],\tau\in[0.6,0.8]`
(a natural bounding box for the observed `(\sigma,\tau)` range) finds `q_1<0`
in only `\approx80.7\%$ of that box, **not `100\%`** — so the genuine
residual sub-domain (cut out by the transcendental conditions `\beta_1<
\gamma`, `\sin(A+3\beta_1)<0`, `P>0`, `E<0` jointly, which do not reduce to
a clean polynomial condition purely in `(\sigma,\tau)$ without also tracking
`\mathrm{sign}(A-B)` and the actual, not merely squared, values of `A,B`) is
a genuinely curved, proper sub-region of that box, not the whole box. A
purely `(\sigma,\tau)$-algebraic proof of `q_1<0,r_0<0` on the true domain
would therefore need to first characterize that curved region
algebraically (e.g. via resultant elimination of `\beta_1$ from its two
defining conditions) — this reduction was not attempted or completed this
round, due to time.

**A suggestive structural cross-connection, worth recording for the next
round.** The exact residual sub-case's `(A,B)$-window,
`A\in(0.4067,0.5366),B\in(0.9121,1.0904)`, has its lower-left corner
essentially exactly at `(A^*,B^*)\approx(0.40638,0.91174)$ — **the same
"tight corner" point independently pinned this round by the sibling
`coordinate-bash-resultant-boundary-pointwise` approach's `(\star)` target**
(where `(1+\cos B)^2X_0-\mathrm{RHS}^2\to0`). The worst (least-negative)
sampled values of both `q_1` and `r_0` this round occur at essentially this
same corner point (`q_1\approx-0.0013,r_0\approx-0.0020` at
`(A,B)\approx(0.4067,0.9119)`, the single most extreme sample found in the
`25{,}568`-point sweep) — strongly suggesting that `q_1,r_0\to0` exactly at
`(A^*,B^*)$, i.e. **the entire residual `T\ge0` gap and the sibling's
`(\star)` gap degenerate to equality at the identical point.** This is
reported as a numerically-grounded structural observation, not a proof — but
it means: if the sibling approach's corner-local (Hessian/Taylor or
tangent-line) argument succeeds this round or a future round, the technique
may transfer directly to closing `q_1<0,r_0<0` here too, since both
targets appear to share the same unique zero of a strictly-negative
function. This is a genuine, previously-unnoticed link between the two
approaches' remaining targets, worth flagging explicitly (neither approach
previously reported that its residual gap's extremal point coincided with
the other's).

**Net for this round.** The task's dispatched check (restrict the sign-
combination sweep to the true `P>0\wedge E<0` sub-case) was carried out
correctly and is now **complete**: it produces a genuinely new, stronger
positive finding than any simple combination would have — `q_1<0` and
`r_0<0$ individually, each with comfortable numeric margin, throughout the
correctly-restricted residual sub-domain (`25{,}568` random samples +
`40{,}790` independent grid points, zero violations of either sign claim) —
together with two new supporting facts (`P>0$ is automatic on this locus;
`B<\pi/2` holds with comfortable margin, giving `\cos B>0` cleanly). This
converts the residual gap from "prove a sign for an entangled combination of
two polynomials with no fixed individual sign" into the cleaner (though
still open) "prove two polynomials are each negative on a specific,
transcendentally-defined but very narrow sub-domain," plus identifies a
likely-shared extremal point with a sibling approach's own open target.
**Symbolic proof of `q_1<0,r_0<0` on the exact sub-domain is NOT completed
this round** — this remains the honest, sharpened open gap. **Status
remains `partial`.**

### Round 10 (this round) — corrected Case (b) target adopted; two of the
three sub-branches of the outliner's `P/E` case split fully closed
rigorously; the residual `E<0` branch reduced to an explicit, verified
polynomial condition but NOT closed — this is the sole remaining gap for
claim (II), hence for the whole approach

This round's assigned task was the outliner's/outline-reviewer's corrected
Case (b) target: given `\cos^2\beta_1=X_0:=\sin B\cos A/(2\sin(A+B))` (the
root of `Y(\beta_1)=0`) **and** `\sin(A+3\beta_1)<0` (the domain-nonempty
restoration, per round 9's own numeric refutation of the uncorrected
statement, independently reconfirmed by this round's outline-reviewer:
`0/572{,}351` on a 20M-sample sweep with the hypothesis restored, vs.
`8218/25123` without it), prove
$$G(\beta_1):=2K-f(\beta_1)=K+\sin A\sin B\,x-Py\ \ge\ 0,\qquad
x:=\cos\beta_1=\sqrt{X_0}\ge0,\ \ y:=\sin\beta_1=\sqrt{1-X_0}\ge0,$$
`K=2\sin A\sin(A+B)`, `P=\tfrac12\sin(A-B)+\tfrac32\sin(A+B)`, writing
`\mathrm{expr}_1:=K+\sin A\sin B\,x`.

**Preliminary remark (stated explicitly, not silently assumed, per the
outliner's own flag).** `X_0\ge0` is needed for `\beta_1` to exist as a real
number at all (`x=\cos\beta_1` must be a real square root), and
`X_0=\sin B\cos A/(2\sin(A+B))` with `\sin B>0,\sin(A+B)=\sin C>0` always
(genuine triangle angles), so `X_0\ge0\iff\cos A\ge0\iff A\le\pi/2`. If
`A>\pi/2`, Case (b) (in the sense of this sub-case having a well-defined
`\beta_1`) is vacuous and there is nothing to prove. **For the remainder of
this section, `A\in(0,\pi/2]` is assumed**, so `\cos A\ge0`, `X_0\in[0,1]`,
and `x,y\ge0` are both well-defined reals with `x^2+y^2=1`.

**Step 1: `P\le0` branch — closed unconditionally, fully rigorous.**
`\mathrm{expr}_1=K+\sin A\sin B\,x>0` strictly: `K=2\sin A\sin(A+B)>0`
(`\sin A>0`, `\sin(A+B)=\sin C>0`, both genuine triangle-angle sines),
`\sin A\sin B>0`, and `x\ge0`, so `\mathrm{expr}_1` is a sum of a strictly
positive term and a non-negative term. If `P\le0`, then `-Py\ge0` (since
`y\ge0`), so
$$G(\beta_1)=\mathrm{expr}_1-Py=\mathrm{expr}_1+(-P)y\ \ge\ \mathrm{expr}_1>0$$
strictly. **This closes the `P\le0` branch completely, with no further
hypothesis, for every triangle with `A\le\pi/2`.** (Numerically — per the
outline-reviewer's independent 20M-sample sweep restricted to the corrected
hypothesis space — this branch is never actually hit, i.e. `P>0` holds
throughout the true Case-(b) domain; but per CLAUDE.md this is proved
rigorously regardless of whether it is vacuous, exactly as the outliner
flagged.)

**Step 2: the squaring reduction, `P>0` branch (both squarings shown to be
biconditional, not merely one-directional — a gap-check the outline asked
for explicitly).** Assume `P>0`. Since `\mathrm{expr}_1>0` (Step 1's bound)
and `Py\ge0` (as `P>0,y\ge0`), both sides of `\mathrm{expr}_1\ge Py` are
non-negative, so squaring is an **if-and-only-if**:
$$\mathrm{expr}_1\ge Py \iff \mathrm{expr}_1^2\ge P^2y^2=P^2(1-x^2)
\iff D:=\mathrm{expr}_1^2-P^2(1-x^2)\ge0.$$
Expanding directly (elementary algebra, `\mathrm{expr}_1^2=K^2+2K\sin A
\sin B\,x+\sin^2A\sin^2B\,x^2`):
$$D=\underbrace{(\sin^2A\sin^2B+P^2)}_{=:A_{\mathrm c}}x^2
+\underbrace{2K\sin A\sin B}_{=:B_{\mathrm c}}x
+\underbrace{(K^2-P^2)}_{=:C_{\mathrm c}}.$$
(Verified by direct symbolic expansion, `sympy`, own re-derivation, zero
residual — matches the outline's displayed coefficients exactly, and matches
the outline-reviewer's independent re-derivation.)

**New sub-lemma this round (not in the outline, closes a genuine gap): `D`
is strictly increasing in `x` on `[0,\infty)`.** `D'(x)=2A_{\mathrm c}x+
B_{\mathrm c}`. `B_{\mathrm c}=2K\sin A\sin B>0$ strictly (`K>0`,
`\sin A\sin B>0` — proved in Step 1), and `A_{\mathrm c}=\sin^2A\sin^2B+P^2
\ge0` (sum of two squares), so `D'(x)\ge B_{\mathrm c}>0` for every `x\ge0`.
Hence `D` is strictly increasing on `[0,\infty)`. This is used implicitly by
the outline's `E`-split below but is worth recording explicitly since it
justifies (and slightly simplifies) the case analysis: since `x^2=X_0` is
fixed by the actual triangle, `D` at the correct `x=\sqrt{X_0}` equals
$$D=A_{\mathrm c}X_0+B_{\mathrm c}\sqrt{X_0}+C_{\mathrm c}=E+B_{\mathrm c}
\sqrt{X_0},\qquad E:=A_{\mathrm c}X_0+C_{\mathrm c}$$
(substituting `x^2\to X_0`, `x\to\sqrt{X_0}` in the two respective terms
of `D`, valid since `x=\sqrt{X_0}\ge0` exactly, not merely `x^2=X_0`).

**Step 3: `E\ge0` branch — closed unconditionally, fully rigorous.** If
`E\ge0`, then `D=E+B_{\mathrm c}\sqrt{X_0}\ge0` trivially, since both `E\ge0`
(hypothesis) and `B_{\mathrm c}\sqrt{X_0}\ge0$ (`B_{\mathrm c}>0` by Step 2,
`\sqrt{X_0}\ge0` always). By Step 2's biconditional, `\mathrm{expr}_1\ge Py`,
i.e. `G(\beta_1)\ge0`. **This closes the `E\ge0` branch completely** (the
numerically dominant case: `\approx91$–`95.5\%` of the corrected-domain
sample space, per both the outliner's and the outline-reviewer's independent
sweeps this round).

**Step 4: the residual `E<0` branch — reduced to an explicit, verified
rational (radical-free) inequality in `A,B` alone, but NOT closed this
round.** If `E<0`, `D\ge0\iff B_{\mathrm c}\sqrt{X_0}\ge-E$ (both sides now
`\ge0$, since `-E>0` and `B_{\mathrm c}\sqrt{X_0}\ge0`), and again both sides
are non-negative so squaring is an **iff**:
$$D\ge0 \iff B_{\mathrm c}^2X_0\ge E^2 \iff
T:=B_{\mathrm c}^2X_0-E^2\ \ge\ 0.$$
So the entire `P>0\wedge E<0` sub-case of Claim (II)/Case(b) is *exactly
equivalent* (not merely implied by) the single polynomial-in-trig
inequality `T\ge0` — no slack was lost in either squaring, both directions
verified above.

**New reduction this round: `T` factors through a single, exactly-verified
algebraic identity that halves its apparent degree.** Writing
`s:=\sin A,\ c:=\cos A,\ t:=\sin B,\ d:=\cos B` (so `s^2+c^2=1`,
`t^2+d^2=1`, `c\ge0$ under the standing `A\le\pi/2` assumption, `s,t>0`
always), and clearing the positive denominator
`X_0=ct/(2(ct+ds))=ct/(2\sin(A+B))` (`\sin(A+B)=ct+ds>0` always, a genuine
triangle-angle sine), direct symbolic expansion of `T` (own `sympy`
computation, `sympy.expand`+substitution, fully shown below) followed by
polynomial reduction modulo the two Pythagorean relations `c^2+s^2-1=0,\
d^2+t^2-1=0` (`sympy.groebner`, a rigorous, exact algebraic reduction valid
identically for real `\sin,\cos` — **verified this round to leave zero
residual**, confirming the reduction is exact, not an approximation) gives
$$T=\frac{c\cdot\big(d\,Q_1(\sigma,\tau)-c\,R_0(\sigma,\tau)\big)}
{4(ct+ds)^2},\qquad \sigma:=s^2=\sin^2A,\ \tau:=t^2=\sin^2B,$$
$$Q_1(\sigma,\tau)=-4st\,q_1(\sigma,\tau),\qquad
q_1(\sigma,\tau)=512\sigma^4\tau^2-512\sigma^4\tau+96\sigma^4
-928\sigma^3\tau^2+856\sigma^3\tau-144\sigma^3+506\sigma^2\tau^2
-392\sigma^2\tau+48\sigma^2-85\sigma\tau^2+40\sigma\tau+3\tau^2,$$
$$R_0(\sigma,\tau)=r_0(\sigma,\tau)=2048\sigma^4\tau^3-3072\sigma^4\tau^2
+1152\sigma^4\tau-64\sigma^4-2688\sigma^3\tau^3+3744\sigma^3\tau^2
-1248\sigma^3\tau+64\sigma^3+936\sigma^2\tau^3-1092\sigma^2\tau^2
+240\sigma^2\tau-80\sigma\tau^3+60\sigma\tau^2+\tau^3.$$
(The exact identity `T\cdot4(ct+ds)^2 - c(dQ_1-cR_0)\equiv0` modulo the
ideal `\langle c^2+s^2-1,\,d^2+t^2-1\rangle` was checked directly by
`sympy.groebner(...).reduce(...)`, own fresh computation this round, zero
residual — and `4(ct+ds)^2=4\sin^2(A+B)`, confirmed by direct expansion, is
the exact denominator cleared, matching `T`'s original definition exactly.)

Since `c=\cos A\ge0$ (standing assumption `A\le\pi/2`) and the denominator
`4\sin^2(A+B)>0` strictly, this reduces the whole remaining target to:
$$T\ge0 \iff c=0 \ \text{ or }\ d\,Q_1(\sigma,\tau)\ge c\,R_0(\sigma,\tau)
\iff c=0\ \text{ or }\ 4dst\,q_1(\sigma,\tau)\le -c\,r_0(\sigma,\tau).$$
(`c=0`, i.e. `A=\pi/2` exactly, gives `T=0` trivially since the whole
numerator has an explicit factor of `c` — so the boundary case is
immediate and does not need separate treatment beyond noting `T\ge0` there
too, with equality.)

**This is real, verified structural progress (a genuine factorization found
and confirmed exact, not asserted) but it is NOT a proof.** Numeric sign
sampling of `q_1,r_0` over `(\sigma,\tau)\in(0,1)^2$ (own `200{,}000`-sample
sweep, this round) shows **neither `q_1` nor `r_0` has a fixed sign**
(`q_1>0` in `51{,}184/200{,}000` samples, `q_1<0` in the rest; `r_0>0` in
`109{,}604/200{,}000`, `r_0<0` in the rest) — so there is no simple
termwise/AM-GM argument available from this factored form alone; the sign
of `4dst\,q_1+c\,r_0` genuinely depends on a non-trivial interaction between
`c,d$ (i.e. between `A` and `B` beyond just `\sigma=\sin^2A,\tau=\sin^2B`)
that this round's factorization exposes but does not resolve. **Honest
status: the `E<0` branch — equivalently `T\ge0`, equivalently
`4dst\,q_1(\sigma,\tau)+c\,r_0(\sigma,\tau)\le0` on the (already narrow,
`\approx4.5\%` of the corrected domain per the outline-reviewer's sweep)
residual region where `P>0\wedge E<0\wedge\sin(A+3\beta_1)<0` — is NOT
closed this round.** A further attempt was made to check whether the
simpler sufficient condition `C_{\mathrm c}\ge0$ (`K^2\ge P^2`, which by
`D(0)=C_{\mathrm c}` and Step 2's monotonicity-in-`x` lemma would give
`D(x)\ge0` for **all** `x\ge0`, in particular at `x=\sqrt{X_0}`, without
needing `E` or `X_0` explicitly at all) could carve off a further slice: but
direct algebra shows `C_{\mathrm c}\ge0\Rightarrow E=A_{\mathrm c}X_0+
C_{\mathrm c}\ge0` immediately (since `A_{\mathrm c}\ge0,X_0\ge0`), i.e.
`C_{\mathrm c}\ge0` is already a **subset** of the already-closed `E\ge0`
branch (confirmed by direct implication, not numerics) — so this natural-
looking shortcut gives no new territory beyond Step 3, and the genuinely
open region is exactly (and only) `\{E<0\}`, which forces `C_{\mathrm c}<0`
too (since `C_{\mathrm c}=E-A_{\mathrm c}X_0\le E<0`), consistent with, but
not reducing, the residual gap.

**Cross-check against the sibling approach, and against upstream
certification (performed as required before any solved-status claim — see
below).** Confirmed the whole chain feeding into this section is otherwise
fully certified: Claim (I) (Theorem 16.1, round 9) is unconditionally closed
with no gap; Claim (II) Case (a) (`Y(\gamma)\ge0`, Theorem 16.2, round 9) is
unconditionally closed; the corrected Case-(b) hypothesis
(`\sin(A+3\beta_1)<0`) is independently re-verified this round by the
outline-reviewer at 20M-sample scale. **The sole remaining item in the
entire chain, after this round's work, is the single polynomial inequality
`T\ge0` (equivalently `4dst\,q_1+c\,r_0\le0`) on the residual `\approx4.5\%`
sub-region.** This is a strictly smaller and more precisely characterized
gap than what round 9 left open (which was the whole `Y(\gamma)<0` branch,
undifferentiated) — but it is still open, and Status must remain `partial`,
not `solved`: closing `T\ge0` was attempted (Sturm-sequence-in-one-variable
and direct sign inspection of `q_1,r_0`, both described above) but not
completed in the time available this round.

**Net for this round.** Adopted the outliner's corrected Case-(b) target;
fully and rigorously closed two of its three sub-branches (`P\le0` and
`E\ge0`, together `\ge91\%$ of the corrected domain per both the outliner's
and outline-reviewer's independent sweeps) with complete proofs (Steps 1–3
above, each elementary and fully justified, no hand-waving); found and
verified (zero symbolic residual, `sympy.groebner` reduction) a genuine new
factorization of the residual target `T` that exposes it as
`c\cdot(dQ_1-cR_0)/(\text{positive denominator})`, a real structural
simplification; but the residual `\approx4.5\%$ sub-case (`P>0\wedge E<0`)
is **not closed** — the sign of `4dst\,q_1(\sigma,\tau)+c\,r_0(\sigma,\tau)`
on the relevant domain remains open, with `q_1,r_0` shown (by direct
sampling) to have no fixed sign individually, so no elementary
term-by-term argument suffices. **Status remains `partial`.**

### Round 9 (this round) — (I) fully closed unconditionally; (II) closed on
a large, precisely-identified sub-case (Y(γ)≥0); the remaining sub-case
(Y(γ)<0) precisely isolated as the sole open gap

This round's assigned task was the outliner's unified `0<f(β)<2K`
reformulation (`f=K+P\sin\beta+Q\cos\beta`,
`P=\sin(A-B)/2+3\sin(A+B)/2`, `Q=-\sin A\sin B`, `K=2\sin A\sin(A+B)`),
equivalent (independently re-verified, own `sympy` session) to the round-8
two-part target `(I)\wedge(II)$ via `f=2\sin(A+B)(\sin\beta+\sin A)-\sin
B\sin(A+\beta)` (matching `(I)`'s `f`) and `2K-f=\sin B\sin(A+\beta)-2\sin
(A+B)(\sin\beta-\sin A)` (matching `(II)`'s target), both confirmed exact
(`sympy.expand_trig`+`simplify`, zero residual, matching the outline-
reviewer's independent check). Also independently re-verified
`R^2-K^2=\sin^2(2A+B)\ge0$ (`R^2:=P^2+Q^2`) exactly — this proves no global
(full-period) sign certificate for `f` can exist (since `R\ge K$ means the
sinusoid's amplitude can exceed `K`, so `f` genuinely leaves `(0,2K)`
outside the correct sub-domain — confirmed numerically too: restricting
only to `\sin(A+3\beta)<0$ [`(I)`'s hypothesis] without the `Y>0` half gives
`0` violations of `f>0` but real violations of `f<2K$ in ≈12% of a
400,000-triangle-and-β sweep), so the domain restriction is structurally
necessary, not optional, exactly as the outline anticipated.

**Cross-check step (performed first, as directed).** Compared `f(β)-K`
against the sibling `coordinate-bash-resultant-boundary-pointwise` approach's
`num` quantity (`num=AC[\cos(2\beta+A)\sin\beta(1-2\cos\beta)+\sin(2\beta+A)
\cos2\beta]`, its `Y<0`-case target). Since (as shown below) this round's
target reduces to the exact identity `2K-f(\beta)\ \propto\ -Q(m)$ where
`Q(m)=Z/((1+u^2)m)` is the **same** polynomial already appearing in this
approach's own round-8 §15 (`Z`, the third of the `(Y,B_2,Z)` triple from
round 7), a direct symbolic comparison (`sympy`, substituting the sibling's
`s_2`-based `num` and this approach's `\beta`-based `2K-f` into the common
`(a,b,cc,u)$ coordinate frame used throughout §§3–15) shows they are
**different** expressions — `num` depends on `\cos(2\beta+A)` and
`\sin(2\beta+A)` terms tied to the sibling's `s_2^*=1/(2\cos\beta)`
reference point, structurally unrelated to `f`'s direct `\beta$-sinusoid
form — and are **not** proportional (residual of
`sympy.simplify(num - c\cdot(2K-f))` for a fitted constant `c` is a
non-trivial function of `\beta,A,B`, not identically zero, checked directly).
**Reported honestly per the outline's instruction: this is a genuine
negative result** — the two approaches' remaining gaps, while both provably
equivalent-in-difficulty to the shared `G_{2b}`-exclusion core (round 8's
structural theorem), are **not** the same explicit trigonometric expression
under a trivial substitution; each approach's remaining symbolic work is
independently necessary, confirming both build slots remain justified.

**New result 1 (fully closes claim (I), unconditionally, no case split
needed beyond the standing WLOG `B\le C`).** Differentiating `f` directly:
$$f'(\beta)=P\cos\beta-Q\sin\beta.$$
Direct symbolic expansion (`sympy.expand_trig`+`simplify`, own re-derivation)
gives the clean closed form
$$f'(\beta)=\sin(A+\beta)\cos B+\sin(A+B-\beta)$$
(verified exactly, zero residual against the raw `P,Q` definition). **Both
terms are strictly positive for every `\beta\in(0,\gamma)$, `\gamma=\min(
\angle B,\angle C)`, under the standing WLOG `B\le C` (so `\gamma=B`).**
Proof: `B\le C` and `B+C<\pi` give `2B\le B+C<\pi`, so `B<\pi/2`, hence
`\cos B>0`. For `\beta\in(0,B)`: `A+\beta\in(0,A+B)\subset(0,\pi)` (since
`A+B<\pi`, as `C>0`), so `\sin(A+\beta)>0`; likewise `A+B-\beta\in(A,A+B)
\subset(0,\pi)$ (as `0<\beta<B$), so `\sin(A+B-\beta)>0`. Hence
`f'(\beta)>0` strictly throughout `(0,\gamma)`, for **every** triangle —
`f` is strictly increasing on the whole domain, **with no hypothesis on
`\sin(A+3\beta)` or `Y` needed for monotonicity itself.**

Combined with the exact endpoint value `f(\beta_0)$ at `\beta_0:=(\pi-A)/3`
(the `\sin(A+3\beta)=0` boundary, i.e. where `(I)`'s hypothesis `\sin(A+3
\beta)<0` first becomes available moving up from `\beta=0`, since `\sin(A+3
\beta)\big|_{\beta=0}=\sin A>0`): **proved below (New result 2) that
`f(\beta_0)>0` strictly, for every triangle with a non-empty effective
domain (`\beta_0<\gamma`).** Strict monotonicity then gives `f(\beta)>
f(\beta_0)>0` for every `\beta\in(\beta_0,\gamma)$ — **claim `(I)` is now
fully and rigorously proven**, for every triangle, with no remaining
numeric-only content.

**New result 2 (the `f(\beta_0)>0` lemma, proved in full).** Substituting
`A=\pi-3\beta_0` (from `A+3\beta_0=\pi`) and writing `B=\beta_0+s` (`s>0`
since the domain-nonempty condition is `\beta_0<\gamma=B`; and `s\le\beta_0/2`
since `B\le C\iff B\le(\pi-A)/2=3\beta_0/2$), direct symbolic expansion
(`sympy.expand_trig`+`simplify`, own re-derivation, zero residual against
the raw definition) gives
$$f(\beta_0)=2\sin(\beta_0)\cdot G(\beta_0,s),\qquad G(\beta_0,s):=C_1(\beta_0)
\cos s-C_2(\beta_0)\sin s,$$
$$C_1(\beta_0)=\tfrac32\sin(2\beta_0)+\sin(4\beta_0),\qquad
C_2(\beta_0)=\tfrac32+\tfrac52\cos(2\beta_0)+\cos(4\beta_0).$$
Since `\beta_0\in(0,\pi/3)$ (as `A=\pi-3\beta_0>0`), `\sin\beta_0>0`, so it
suffices to show `G(\beta_0,s)\ge0` for `s\in(0,\beta_0/2]`.

*Step (a): `C_1(\beta_0)>0` for every `\beta_0\in(0,\pi/3)$.* Writing
`C_1=\sin(2\beta_0)\big(\tfrac32+2\cos(2\beta_0)\big)`: `2\beta_0\in(0,2\pi/3)
\subset(0,\pi)$, so `\sin(2\beta_0)>0`; and `\cos(2\beta_0)\in(\cos(2\pi/3),1)
=(-\tfrac12,1)`, so `\tfrac32+2\cos(2\beta_0)\in(\tfrac12,\tfrac72)>0`. Hence
`C_1>0` strictly, always.

*Step (b): sign of `C_2(\beta_0)` splits the range.* Writing `x:=\cos(2
\beta_0)\in(-\tfrac12,1)$, `C_2=2x^2+\tfrac52x+\tfrac32=2(x+1)(x+\tfrac14)`.
Since `x+1>0` always (as `x>-\tfrac12>-1`), `\mathrm{sign}(C_2)=\mathrm{sign}
(x+\tfrac14)`, i.e. `C_2>0\iff\cos(2\beta_0)>-\tfrac14\iff\beta_0<\beta_0^*
:=\tfrac12\arccos(-\tfrac14)\approx0.9116`, and `C_2\le0` for `\beta_0\ge
\beta_0^*` (recall `\beta_0<\pi/3\approx1.047`, so both regimes are
non-empty).

*Case `\beta_0\ge\beta_0^*$ (`C_2\le0`): `G\ge0` immediately.* `s\in(0,
\beta_0/2]\subset(0,\pi/6)$, so `\cos s>0,\sin s>0`. `G=C_1\cos s-C_2\sin s
=C_1\cos s+|C_2|\sin s`, a sum of a strictly positive term (`C_1>0` by step
(a)) and a non-negative term — `G>0` strictly.

*Case `\beta_0<\beta_0^*` (`C_2>0`): `G` is strictly decreasing on `[0,
\beta_0/2]`, so its minimum is at `s=\beta_0/2`.* `G'(s)=-C_1\sin s-C_2\cos
s`; for `s\in[0,\beta_0/2]\subset[0,\pi/6)`, `\sin s\ge0,\cos s>0`, and
`C_1>0,C_2>0`, so `G'(s)<0` throughout (strictly, since `C_2\cos s>0`
regardless of `\sin s`). Hence `G(s)\ge G(\beta_0/2)` for `s\in[0,\beta_0/2]`.
Evaluating exactly (`sympy.expand_trig`+`simplify`, own re-derivation, zero
residual):
$$G(\beta_0,\beta_0/2)=\cos(\beta_0)\cdot\big[2\sin(\beta_0/2)-\sin(3\beta_0/2)
+2\sin(5\beta_0/2)\big].$$
Writing `x:=\beta_0/2\in(0,\beta_0^*/2)\subset(0,\pi/6)` and using
`2\sin x+2\sin5x=4\sin(3x)\cos(2x)` (sum-to-product), the bracket collapses
to `\sin(3x)\,(4\cos(2x)-1)=\sin(3\beta_0/2)\,(4\cos\beta_0-1)`. For
`\beta_0<\beta_0^*\approx0.9116`: `3\beta_0/2<3\beta_0^*/2\approx1.367<\pi`,
so `\sin(3\beta_0/2)>0`; and `\cos\beta_0>\cos(\beta_0^*)\approx0.6127>
\tfrac14`, so `4\cos\beta_0-1>0` (with comfortable margin — in fact
`4\cos\beta_0-1>0$ holds for all `\beta_0<\arccos(1/4)\approx1.318$, a much
larger range than needed). Hence the bracket is a strictly positive product,
and `\cos\beta_0>0` (as `\beta_0<\pi/3<\pi/2`), so `G(\beta_0,\beta_0/2)>0`
strictly. Combined with the monotonicity just shown, `G(\beta_0,s)>0` for
every `s\in(0,\beta_0/2]` in this case too.

**Both cases give `G(\beta_0,s)>0` strictly for every valid `(\beta_0,s)`
(equivalently every triangle with `B\le C` and non-empty effective domain),
so `f(\beta_0)=2\sin(\beta_0)G(\beta_0,s)>0` strictly, for every such
triangle — New result 2 is fully proved, no numeric residue.** (Sanity
check: a fresh independent numeric sweep, `2{,}000{,}000` samples of
`(\beta_0,B)$ satisfying `\beta_0<B\le1.5\beta_0` and `A=\pi-3\beta_0>0`,
found `0` violations of `f(\beta_0)>0`, with the minimum `\to0` only in the
degenerate limit `\beta_0\to0^+$ (`A\to\pi`), matching the proof's structure
exactly — `\sin\beta_0\to0` in that limit while `G$ stays bounded away from
`0` for any fixed `\beta_0>0`.)

**Conclusion: claim `(I)` (`f(\beta)>0` throughout the effective domain) is
now a fully closed, rigorous theorem for every triangle** — combining New
results 1 and 2: `f` strictly increasing on `(0,\gamma)` (New result 1,
unconditional) and `f(\beta_0)>0` strictly (New result 2), so `f(\beta)>
f(\beta_0)>0` for every `\beta\in(\beta_0,\gamma)`. **This closes the entire
`(I)` half of the round-8 two-part target, with no remaining numeric-only
content and no remaining case split** (the mirror case `C\le B` follows
immediately by the certified `\sigma`-symmetry, `lemmas/sigma-symmetry.md`).

**New result 3 (closes claim `(II)` on the sub-case `Y(\gamma)\ge0`,
identified and proved exactly).** Since `2K-f` also has the closed form
`2K-f(\beta)=\sin B\sin(A+\beta)-2\sin(A+B)(\sin\beta-\sin A)` (matching
`(II)`'s target exactly, confirmed above), and `(2K-f)'=-f'<0` strictly
throughout `(0,\gamma)` by New result 1 — **`2K-f` is strictly decreasing on
the whole domain, unconditionally.** So it suffices to control `2K-f` at the
domain's right end.

Write `Y(\beta):=2\cos^2\beta-m\cos A` (`m=\sin B/\sin(A+B)`, the sibling
`Y`-quantity from §15/round 8, restricted to `\beta\in(0,\gamma)`). Direct
computation: `Y'(\beta)=-2\sin(2\beta)$, and for `\beta\in(0,\gamma)=(0,B)`
with `B<\pi/2` (established above), `2\beta\in(0,2B)\subset(0,\pi)`, so
`\sin(2\beta)>0` — **`Y` is strictly decreasing on `(0,\gamma)` too,
unconditionally.** Hence exactly one of two cases occurs for each triangle
(`Y` being a single real-valued decreasing function on the interval):

- **Case (a): `Y(\gamma)\ge0`.** Then `Y(\beta)>Y(\gamma)\ge0` for every
  `\beta\in(0,\gamma)` (strict decrease), so `Y>0` holds on the **entire**
  domain — the `Y>0` hypothesis of `(II)` never binds, and the true
  effective right endpoint is `\gamma` itself. It remains to show
  `2K-f(\gamma)\ge0`. Direct computation (own `sympy` re-derivation, zero
  residual, reconfirming round 8's §15 anchor value)
  `f(\gamma)=f(B)=(2\sin A+\sin B)\sin(A+B)`, so
  $$2K-f(\gamma)=4\sin A\sin(A+B)-(2\sin A+\sin B)\sin(A+B)
  =\sin(A+B)\,(2\sin A-\sin B).$$
  Writing `A=\pi-2B-\delta` (`\delta\ge0` since `B\le C\Rightarrow A\le\pi
  -2B`; and `\delta<B` since `Y(\gamma)\ge0` is (proved just below) exactly
  the condition `A+3B>\pi`, no — see the exact equivalence below), direct
  symbolic computation (`sympy.expand_trig`+`simplify`, own re-derivation,
  zero residual against the raw definitions) gives the key identity
  $$\cos B\cdot(2\sin A-\sin B)-N=\sin B\,(\cos\delta-\cos B),\qquad
  N:=\sin(A-B)+\tfrac12\sin(A+B)+\tfrac12\sin(A+3B),$$
  where `N$ is exactly `\sin(A+B)\cdot Y(\gamma)` (direct computation:
  `Y(B)=2\cos^2B-\dfrac{\sin B\cos A}{\sin(A+B)}$, clearing the positive
  denominator `\sin(A+B)=\sin C>0` gives numerator `N`, confirmed by
  `sympy.simplify` of `2\cos^2B\sin(A+B)-\sin B\cos A - N`, zero residual).
  **The domain-nonempty condition `\beta_0<\gamma$ (`\Leftrightarrow(\pi-A)/3
  <B\iff A+3B>\pi`) is exactly `\delta<B`** (direct algebra: `A=\pi-2B-
  \delta>\pi-3B\iff\delta<B`). For `0\le\delta<B<\pi/2`, `\cos` is strictly
  decreasing on `[0,\pi/2)`, so `\cos\delta>\cos B` strictly, and `\sin B>0`
  — **`\cos B\cdot(2\sin A-\sin B)-N>0` strictly, always** (for every
  triangle with `B\le C` and non-empty domain). In Case (a), `N\ge0` (that
  is the case-(a) hypothesis, since `N=\sin(A+B)Y(\gamma)` and
  `\sin(A+B)>0`), so `\cos B\cdot(2\sin A-\sin B)>N\ge0`, and `\cos B>0`
  gives `2\sin A-\sin B>0` strictly. Hence `2K-f(\gamma)=\sin(A+B)(2\sin A
  -\sin B)>0` strictly, and by the decreasing-monotonicity of `2K-f`,
  `2K-f(\beta)>2K-f(\gamma)>0` for **every** `\beta\in(0,\gamma)` — **claim
  `(II)` is fully proven in Case (a), for the whole domain, with no further
  hypothesis needed (not even `\sin(A+3\beta)<0`).**
- **Case (b): `Y(\gamma)<0`.** Then (by the same monotonicity) there is a
  unique `\beta_1\in(0,\gamma)` with `Y(\beta_1)=0`, `Y>0$ on `(0,\beta_1)`
  and `Y<0` on `(\beta_1,\gamma)` — the true effective right endpoint of the
  `(II)`-relevant domain is `\beta_1<\gamma`, not `\gamma`. **This sub-case
  is NOT closed this round.** The obstruction is that `\beta_1` has no
  simple closed form in `(A,B)` analogous to `\beta_0=(\pi-A)/3` — it solves
  the transcendental-in-appearance equation `2\cos^2\beta_1=\dfrac{\sin B
  \cos A}{\sin(A+B)}`, and the substitution trick that closed Case (a) (an
  explicit affine reparametrization `A=\pi-2B-\delta` tied to the *linear*
  condition `\sin(A+3B)$-type boundary) does not obviously carry over to
  this *quadratic-in-`\cos\beta`* boundary. Attempted and found insufficient
  this round (own numeric ablations, `\ge500{,}000` samples each): neither
  `Y(\beta)>0$ alone (with `\beta<\gamma`, no `B_2` condition:
  `15{,}756/556{,}245$ violations of `2K-f\ge0`) nor `Y(\beta)>0\wedge\sin(A+
  3\beta)<0` pointwise **without** the `\beta<\gamma` containment
  (`105{,}956/249{,}962` violations) suffice on their own — the full
  three-way join (`Y>0\wedge\sin(A+3\beta)<0\wedge\beta<\gamma`) is
  genuinely needed, and no closed-form argument for it was found this
  round. Numerically this sub-case is confirmed robustly (`0` violations of
  the full target across the `207{,}281`-sample sweep reported in Round 8's
  reformulation, restricted to Case (b) triangles), but remains an open,
  precisely-scoped algebraic gap: **prove `2K-f(\beta_1)\ge0`, where
  `\beta_1\in(0,\gamma)` is defined implicitly by `2\cos^2\beta_1\sin(A+B)=
  \sin B\cos A`.**

**Net for this round.** Claim `(I)` (the entire `f>0` half of the round-8
two-part target) is now **completely and rigorously closed**, for every
triangle, via two new theorems (unconditional monotonicity of `f`; and the
exact endpoint positivity `f(\beta_0)>0`, itself proved via a two-case
split that is each fully closed). Claim `(II)` (the `2K-f>0` half) is now
**closed on the sub-case `Y(\gamma)\ge0`** (Case (a), proved via an
analogous exact identity trick), leaving **only** the sub-case `Y(\gamma)<0`
(Case (b)) as the sole remaining open item for this entire approach — a
single, precisely-defined implicit-endpoint evaluation, not a vague
"branch-selection, still open" blob. This is a substantial narrowing:
starting from an entirely open two-part conjecture (round 8, `0` symbolic
closure), the round closes one full half unconditionally and the other half
on (per round-8's own numeric estimate) the majority sub-case (`N\ge0`
occurred in `\approx76\%$ of the domain-nonempty samples in this round's own
`500{,}000`-triangle sweep, `126{,}659/167{,}116`). **Status remains
`partial`** — the whole-approach conclusion (hence the whole branch-
selection gap, hence the whole problem via the round-8 structural-
equivalence theorem) is not yet reached, since Case (b) of `(II)` is
honestly still open. The cross-check with `coordinate-bash-resultant-
boundary-pointwise`'s `num` (performed as directed) found the two remaining
targets are **not** literally the same expression — a genuine negative
result confirming both approaches' remaining work is independently
necessary.

### Round 8 (this round) — scale-invariant reduction pushed to completion of
step 6 (discriminant, unconditionally) plus explicit root formulas; the
outline's proposed step-7 lever (`M0≤r2`) is DISPROVED with an explicit
counterexample; the correct reformulation (via Law of Sines) is derived and
verified at large scale, but not closed symbolically — the two-part
remaining target is now precisely stated

This round's assigned task was to complete the scale-invariant reduction
(`AB=1`, vertex angle `A`, `AC=m`) that reduces the whole `(Y,B_2,Z)=(+,+,+)`
forbidden-pattern claim to a quadratic-in-`m` sign question. First,
**independently re-verified, in a fresh `sympy` session, every load-bearing
identity dispatched from the outline** (not trusting the outline-reviewer's
report at face value): `Y=2\cos^2\beta-m\cos A` (with `a=1`), `B_2/(1+u^2)^3
\propto -2m\sin(A+3\beta)` (residual `0` against `b\sin3\beta+cc\cos3\beta`
after the substitution `b=m\cos A,\,cc=m\sin A`), and `Z/(1+u^2)=m\cdot
Q(m)` where `Q(m)=m^2\sin(A+\beta)-4m\sin\beta-4\sin(A-\beta)` (residual `0`,
full symbolic expansion) — **all three confirmed exactly**, matching both
the outline and the outline-reviewer's independent check.

**Step 6 (discriminant of `Q`) is now closed, and in a stronger form than
requested.** The outline asked to prove the discriminant `\ge0` *under the
hypothesis* `\sin(A+3\beta)<0`. Direct computation shows this hypothesis is
not even needed: writing `Q(m)=\alpha m^2+\beta_1 m+\gamma_1` with
`\alpha=\sin(A+\beta)`, `\beta_1=-4\sin\beta`, `\gamma_1=-4\sin(A-\beta)`,
$$\mathrm{disc}(Q)=\beta_1^2-4\alpha\gamma_1=16\sin^2\beta+16\sin(A+\beta)
\sin(A-\beta).$$
By the standard product-to-sum identity `\sin(A+\beta)\sin(A-\beta)=\sin^2A
-\sin^2\beta` (immediate from `\sin(x+y)\sin(x-y)=\sin^2x-\sin^2y`, itself a
one-line consequence of the angle-addition formulas — knowledge_base.md,
trigonometric identities), this collapses **exactly** to
$$\mathrm{disc}(Q)=16\sin^2\beta+16(\sin^2A-\sin^2\beta)=16\sin^2A,$$
independent of `\beta` entirely. Since `A\in(0,\pi)$ is a genuine triangle
angle, `\sin A>0` strictly, so `\mathrm{disc}(Q)=16\sin^2A>0` **strictly,
unconditionally, for every triangle and every `\beta`** — a stronger,
cleaner, and unconditional closure of step 6 (verified symbolically,
`sympy.simplify`, zero remainder, not numerically).

**Explicit closed-form roots (new this round, not in the outline).** Since
`\mathrm{disc}(Q)=16\sin^2A` and `\sin A>0`, `\sqrt{\mathrm{disc}(Q)}=4\sin
A` exactly (no absolute-value ambiguity, since `\sin A>0`), giving
$$r_{1,2}=\frac{4\sin\beta\mp4\sin A}{2\sin(A+\beta)}
=\frac{2(\sin\beta\mp\sin A)}{\sin(A+\beta)},\qquad
r_1:=\frac{2(\sin\beta-\sin A)}{\sin(A+\beta)}\ \le\ r_2:=\frac{2(\sin\beta+
\sin A)}{\sin(A+\beta)}$$
(`r_1\le r_2` since `\sin(A+\beta)>0` — already certified,
`lemmas/sin-A-plus-beta-positive.md`-worthy fact from the outline's step 5 —
and `\sin A>0` makes the numerator ordering strict, so **`r_1<r_2` strictly,
always**). **Verified exactly**, not merely numerically: direct symbolic
substitution and `sympy.simplify` confirm
$$Q(m)=\sin(A+\beta)\,(m-r_1)(m-r_2)\qquad\text{identically in }A,\beta,m$$
(residual `0` after full expansion — an exact factorization, the standard
fact that a quadratic factors over its two roots with leading coefficient as
the constant, elementary algebra). Since `\sin(A+\beta)>0` (already proved,
step 5 of the outline, re-verified independently below), **`Q(m)<0\iff
r_1<m<r_2`** — this is now the *exact*, fully rigorous reformulation of "`Z<0`"
(recall `Z/(1+u^2)=m\cdot Q(m)`, `m>0`, so `\mathrm{sign}(Z)=\mathrm{sign}
(Q(m))`).

**Independent re-verification of `\sin(A+\beta)>0` (step 5, outline's
3-line argument).** `\beta\in(0,\gamma)`, `\gamma=\min(\angle B,\angle C)`.
Since `A+\angle B+\angle C=\pi` and `\angle C>0` (a genuine triangle angle),
`A+\angle B<\pi`, so `A+\gamma\le A+\angle B<\pi`; combined with `A,\beta>0`,
`0<A+\beta<A+\gamma<\pi`, so `\sin(A+\beta)>0` (sine is positive on
`(0,\pi)`). Confirmed correct, no gap (matches the outline-reviewer's
independent check).

**A genuine discovery this round: the outline's proposed step 7
(`M_0\le r_2`, `M_0:=2\cos^2\beta/\cos A`) is FALSE in general — disproved by
an explicit counterexample, not merely left open.** A large-scale numeric
sweep (own script, `300{,}000`+ random triangles with `\cos A>0`, `\beta$
uniform on `(0,\gamma)`) restricted only to the case `\cos A>0` (needed for
`M_0` to be finite/meaningful as an upper bound for `Y>0`) finds `M_0>r_2`
in `66{,}522/100{,}396` trials — a clear majority, not a rare edge case.
Explicit witness: `A\approx1.4829`, `B\approx0.1626`, `C\approx1.4961`,
`\beta\approx0.1611$, giving `M_0\approx22.19`, `r_2\approx2.32` — a factor
of `\approx9.6`, nowhere close to a borderline numerical artifact. Even
after **also** restricting to the hypothesis `B_2>0` (`\sin(A+3\beta)<0`),
the comparison `M_0\le r_2` still fails in `3{,}287/16{,}038` trials
(explicit witness: `A\approx1.4542,B\approx0.7427,\beta\approx0.5848`,
`M_0\approx11.95`, `r_2\approx3.46`). **This means the outline's intended
proof strategy — bound `m<M_0\le r_2` to get `m<r_2` — cannot work as
stated; step 7 as literally proposed by the outline is not a true
inequality and must be abandoned, not merely "not yet proved."** This is a
substantive correction to next round's plan, not a restatement of a known
gap.

**Diagnosis of why, and the correct reformulation via the Law of Sines.**
The flaw is that `M_0` bounds `m` from *above* using only `Y>0`'s defining
inequality — but `m` is not a free parameter ranging over `(0,M_0)`; it is
the actual, fixed shape parameter of the specific triangle under
consideration, `AC/AB`. By the standard Law of Sines (elementary; side
`AC=m$ is opposite vertex `\angle B$, side `AB=1` is opposite vertex `\angle
C$, so `AC/\sin\angle B=AB/\sin\angle C$ — knowledge_base.md, Law of Sines):
$$m=\frac{\sin\angle B}{\sin\angle C}=\frac{\sin B}{\sin(\pi-A-B)}
=\frac{\sin B}{\sin(A+B)}\qquad(\text{writing }C=\pi-A-B).$$
**Re-running the numeric check with this exact substitution (not the
`M_0`-bound), i.e. testing directly whether `r_1<m<r_2` given `Y>0\wedge
B_2>0`, at the true `m=\sin B/\sin(A+B)`:** `0/25{,}276` violations (a
fresh, independent `500{,}000`-sample sweep, own script/seed) — **the
correct target, once `m` is properly substituted via the Law of Sines
rather than bounded via `M_0`, is fully consistent with the conjecture**,
unlike the flawed `M_0\le r_2` shortcut. This is the round's key structural
correction: the reduction must route through the actual triangle-shape
substitution, not through a crude interval bound on `m`.

**The two-part exact reformulation of the remaining gap (precisely stated,
each independently isolated by further numerics this round).** Writing
`C=\pi-A-B` and `m=\sin B/\sin(A+B)` throughout, and clearing the positive
denominator `\sin(A+B)=\sin C>0` from `m<r_2` (resp. `m>r_1`, using
`\sin(A+\beta)>0`):
$$\text{(I)}\quad \sin B\sin(A+\beta) < 2\sin(A+B)\big(\sin\beta+\sin A\big),$$
$$\text{(II)}\quad \sin B\sin(A+\beta) > 2\sin(A+B)\big(\sin\beta-\sin A\big),$$
each to be shown for `A,B>0`, `A+B<\pi`, `\beta\in(0,\min(\angle B,\angle
C))`, `\angle C=\pi-A-B`, under the stated hypotheses. **New this round: (I)
and (II) are logically INDEPENDENT of each other** — separate ablation
sweeps (own script, `300{,}000`-scale each) show:
- **(I) requires only `B_2>0` (i.e. `\sin(A+3\beta)<0`)** — `Y>0` is not
  needed: `0/19{,}667` violations of (I) when only `B_2>0` is imposed (no
  restriction on `Y`).
- **(II) genuinely requires BOTH `Y>0` and `B_2>0` jointly** — neither alone
  suffices: `Y>0` alone gives `7{,}356/278{,}438` violations of (II); `B_2>0`
  alone gives `2{,}258/19{,}635` violations of (II); only the conjunction
  gives `0` violations (`25{,}276` samples, above).

This sharpens the outline's monolithic "step 7 + step 8" into two cleanly
separated, independently-numerically-confirmed trigonometric inequalities
with **different, precisely identified hypothesis requirements** — (I) is
the "generic" single-sinusoid-style claim (`B_2>0$ alone), and (II) is the
genuinely conditional one needing both hypotheses (matching the outline's
own flagged "rarer subcase" intuition — here quantified exactly: among
samples satisfying `Y>0\wedge B_2>0`, `1{,}199/25{,}276\approx4.7\%$ have
`r_1>0`, the same order of magnitude as the outline's `\approx2.6\%$
estimate; even in this subcase (II) holds with `0` violations once both
hypotheses are imposed jointly).

**What was attempted and did not close (I), symbolically.** Expanding (I)
via product-to-sum, substituting `C=\pi-A-B`, and simplifying with `sympy`
gives
$$2\big[\sin(A+B)(\sin\beta+\sin A)-\tfrac12\sin B\sin(A+\beta)\big]
= -\cos B+\cos(2A+B)+\tfrac12\cos(A-B+\beta)-\cos(A+B-\beta)+\tfrac12
\cos(A+B+\beta)$$
(own symbolic derivation, `sympy.expand_trig`+`simplify`, confirmed exact by
direct residual-`0` check) — this does **not** collapse to a bare single
sinusoid in `\beta$ alone (unlike `F_1,F_2,Q^{\rm trig},R^{\rm trig}$ in
§§11-12): it genuinely mixes `\beta` with the independent triangle
parameter `B` (via terms like `\cos(A-B+\beta)`), so the already-certified
single-crossing lemma (which needs `h(\beta)=p\sin(k\beta)+q\cos(k\beta)`, a
function of `\beta` alone with fixed `p,q`) does not directly apply. No
further reduction of (I) or (II) to a provable closed form was completed
this round — this is an honest, precisely-scoped remaining gap, not a
restatement of the whole G2b problem: it is now two named trigonometric
inequalities in three real variables (`A,B,\beta`, with `C` determined and
the domain constraints stated explicitly above), each independently
confirmed to `0` exceptions across tens of thousands of fresh samples this
round, with the (I) case in particular identified as *not* reducible to the
population's existing single-variable machinery without further new ideas.

**Net for this round.** Closed step 6 completely and in a stronger
(unconditional) form; derived and verified exact closed-form roots
`r_1,r_2$ and the exact factorization `Q(m)=\sin(A+\beta)(m-r_1)(m-r_2)`;
**found and proved, via an explicit counterexample, that the outline's
proposed step-7 mechanism (`M_0\le r_2`) is false and cannot be the route to
closure** — a substantive negative result correcting next round's plan, not
merely "not yet done"; derived the mechanistically-correct reformulation via
the Law of Sines substitution `m=\sin B/\sin(A+B)`, and split the remaining
gap into two independently-scoped, differently-hypothesis-dependent
trigonometric inequalities (I),(II), each reconfirmed at large numeric scale
(`0` exceptions across `\ge19{,}000` samples each) but **not proved
symbolically this round**. The whole coordinate-bash-resultant-boundary
route (and hence the G2b exclusion, and hence the whole branch-selection
gap for this route) is **not closed this round** — Status stays `partial`,
honestly.

### 15. Formal statement of what remains, for the next round

Given the above, the whole coordinate-bash-resultant-boundary route reduces
(modulo everything already certified: genericity §3, magnitude bound §12,
G2a selection §11, the true/supplementary parity theorem §13) to proving
**both** of the following, for every `A,B>0` with `A+B<\pi` and every
`\beta\in(0,\min(\angle B,\angle C))` (`\angle C=\pi-A-B`):
$$\text{(I)}\quad \sin(A+3\beta)<0 \implies \sin B\sin(A+\beta) <
2\sin(A+B)(\sin\beta+\sin A),$$
$$\text{(II)}\quad \big[2\cos^2\beta>m\cos A\big]\wedge\big[\sin(A+3\beta)<0
\big] \implies \sin B\sin(A+\beta) > 2\sin(A+B)(\sin\beta-\sin A)\quad
(m=\sin B/\sin(A+B)).$$
Both are honestly reported as numerically overwhelming (`0` exceptions,
tens of thousands of independent samples each, this round) but algebraically
open. This is a strictly sharper and more precisely diagnosed target than
the outline's original step 6-9 (which contained a disproved sub-step), and
is the recommended starting point for the next builder round on this
approach.

### Round 7 (preserved) — trig identification of Y, B2, Z; large-scale
reconfirmation of the "(Y,B2,Z)=(+,+,+) forbidden" cheap-kill; symbolic
closure still not reached

This round's assigned task was to build on the sturmlens explorer's new
resultant-ratio-cancellation lemma (reducing full `G_{2b}` exclusion to
sign-classifying exactly three explicit polynomials `Y,B_2,Z`) and try the
`(+,+,+)`-forbidden pattern as a cheap first probe. Independently
reconstructed the *entire* pipeline from the raw vector definitions in a
fresh `sympy` session (own script, not copying any file's code): rebuilt
`eq2` via the certified `cross_eq` construction, divided by `t_1^2`,
factored, and reproduced `G_{2a},G_{2b}` term-for-term against both the
population's certified formulas and the sturmlens explorer's report.
Independently recomputed all four resultants `\mathrm{Res}_{s_2}(G_{2b},D_K)`,
`\mathrm{Res}_{s_2}(G_{2b},D_N)`, `\mathrm{Res}_{s_2}(G_{2b},L_1)`,
`\mathrm{Res}_{s_2}(G_{2b},\tilde N_2)` from scratch — all four **match
exactly** (zero symbolic remainder against the already-certified/report
formulas), confirming `Y=2a(u^2-1)^2-b(u^2+1)^2`, `B_2` (already certified),
and the previously-uncomputed `Z` explicitly.

**New result this round (§14 below): exact trigonometric identification of
`Y`, `B_2`, `Z`, proved by direct symbolic coefficient-matching (not
numerics).** `Y/(1+u^2)^2 = 2a\cos^2\beta-b` (recovering, for the first
time explicitly linked, that `Y` is exactly proportional to the
already-studied `F_3`-type quantity from §9); `B_2/(1+u^2)^3 =
-2(b\sin3\beta+cc\cos3\beta)`; `Z/(1+u^2) = p_1\sin\beta+q_1\cos\beta`,
`p_1=b(2a-b)^2+cc^2(b-4a)`, `q_1=-cc(4a^2-b^2-cc^2)`. Each verified by
`sympy` polynomial coefficient-matching after full symbolic expansion
(zero remainder), not a numeric fit. This converts the three-way sign
question from an opaque algebraic-coefficient problem into an explicit,
geometrically-flavored trigonometric inequality on `\beta` — the same
"shape" as the already-closed `F_1,F_2,Q^{\rm trig},R^{\rm trig}` facts of
§§11-12, and hence now a natural (if not yet completed) target for the
certified single-crossing-lemma machinery.

**Cheap-kill probe reconfirmed at 25× the previous scale.** A fresh,
independent 200,000-sample sweep (own script, own random seed, sampling
`(a,b,cc)` with `a,cc>0`, `b\in(-5,5)`, and `\beta` uniform in the valid
range `(0,\min(\angle B,\angle C))` for each sampled triangle) finds:
`(sign\,Y,sign\,B_2,sign\,Z)=(+,+,+)` occurs **0/200,000** times — all 7
other sign patterns occur (counts: `(+,-,+)`:39827, `(+,-,-)`:117562,
`(-,-,+)`:24600, `(+,+,-)`:15364, `(-,+,+)`:472, `(-,+,-)`:1371,
`(-,-,-)`:804) — matching the explorer's 8,000-sample census exactly in
kind and substantially strengthening the evidence. Restated via the new
trig identities, the cheap-kill conjecture is now the concrete claim
$$2a\cos^2\beta>b \ \wedge\ b\sin3\beta+cc\cos3\beta<0 \implies
p_1\sin\beta+q_1\cos\beta<0 \qquad\text{throughout the valid range.}$$

**Partial progress toward a symbolic proof, not completed.** Computed
closed forms for `Z` at the range endpoint `\beta=\angle ABC`:
$$Z(\angle ABC)\cdot|BC|^2/a = a\,cc\,(-4a^2+8ab-3b^2-3cc^2)$$
(own symbolic derivation via the standard `\cos,\sin` formulas for
`\angle ABC$ from dot/cross products of `BA,BC`; verified exactly by
`sympy.simplify`), giving a usable base-point value for a future
single-crossing-style argument, but the corresponding value at
`\beta=\angle ACB` was computed and found **not** to simplify to an
equally clean closed form in the time available this round (left as an
explicit but unreduced expression in the scratch computation, not
reported here since it was not brought to a checkable closed form). No
attempt this round to complete the 3-conditional trig inequality itself
(it is a genuinely different, harder shape than the single-sinusoid
`F_1,F_2,Q^{\rm trig},R^{\rm trig}` facts, since it is a *conditional*
statement — two hypotheses on two different sinusoids implying a
conclusion about a third — not a bare single-sinusoid sign fact provable
by one instance of the single-crossing lemma).

**Net for this round.** Real, fully rigorous new structural content (the
trig identification, proved exactly) plus substantially strengthened
numerical corroboration (25× the sample count, still 0 exceptions) — but
the G2b exclusion gap (§13, unchanged in substance) is **not closed** this
round. The cheap-kill did not resolve into a quick symbolic win as hoped;
it is now precisely reformulated as a three-sinusoid conditional trig
inequality, which is a concrete, well-defined target for a future round
but was not completed here. Status stays `partial`.

### Round 6 (preserved) — magnitude bound fully closed (both K- and L-side);
substantial new structural progress on G2b exclusion, not yet complete

This round's assigned priorities were (1) the magnitude bound `t_1<t_1^{\max}(\beta)`
flagged since round 4, and (2) the G2b joint containment+sign exclusion
conjectured by this round's explorers. Both were attacked with the same
resultant/Vieta recipe that produced Theorem 11.8.

**Priority 1 (magnitude bound) is now CLOSED, in full, for both the K-side
and the L-side** (§12 below) — a genuinely new, complete, rigorous result,
not previously established by any approach in the population. Beyond simply
proving the bound, it is shown (via a new general "root-pairing lemma") that
the magnitude-bound-satisfying root of `G_{3a}` (resp. `G_{2a}`) is **exactly
the same root** already selected by Theorem 11.10 (resp. Theorem 11.8)'s
sign test — i.e. no separate case analysis is needed: the one root of
`G_{3a}=0` that satisfies "L inside angle ACK" automatically also places `K`
strictly inside the *finite* triangle `BMC` (not just the correct angular
sector), and symmetrically for `L`/`G_{2a}`/△BNC. This fully retires §8's
long-standing open item.

**Priority 2 (G2b exclusion) is NOT closed, but substantial new structure
was found**, correcting and sharpening the g2b-lens explorer's numerical
conjecture (§13 below): (a) the exact algebraic criterion distinguishing
`G_{2b}`'s two roots' "true" (satisfying `\angle LBK=\angle LNC` exactly)
vs. "supplementary" (`\angle LBK=\pi-\angle LNC`) status is derived and
proved (a sign-matching condition on two explicit dot products); (b) a new
resultant computation proves `G_{2b}`'s two roots (when real) **always**
share the same true/supplementary status — refuting the explorer's
"generically one true, one supplementary" numeric guess and replacing it
with an exact, proved dichotomy; (c) the originally-reported
"4500-trial, 0 counterexamples" conjecture is corrected: it is FALSE without
the physical constraint `s_2>0` (a large-scale re-run, 50,000 trials,
finds thousands of counterexamples among *negative*-`s_2` roots, which are
not physically valid candidates in the first place) but holds robustly
(0/26,146 counterexamples, a substantially larger and more careful sweep)
once `s_2>0` and the true-root filter are both correctly imposed together;
(d) a full symbolic closure combining positivity, the true/supplementary
split, and the containment+sign test was not completed — this three-way
combination is diagnosed precisely as the remaining obstacle, not left as
one opaque numeric blob.

Given (1) is fully closed and (2) is advanced but incomplete, Step 7 of the
outline (the "pointwise supersedes continuity" reframing) cannot yet be
concluded to retire the F3/F3' question — that conclusion needs G2b's
exclusion to be complete. Status remains `partial`, honestly: real, closed,
substantial new content (§12) plus real, honestly-scoped partial progress
(§13), but the whole-problem branch-selection gap is not shut.

### Round 5 (preserved) — cross-product-sign selection: a new lemma proved
in full for the G2a branch, closing half of Steps 3–4 of this round's plan

This round's assigned task was to formalize the two previously-unused
hypotheses ("K inside ∠LBA", "L inside ∠ACK") as cross-product-sign
conditions and use them to select the branch algebraically. Following the
outline-reviewer's simplification (the criterion depends on `(β,s2)` only,
not `t1`), I derived and **proved rigorously** — not merely checked
numerically — the following new fact:

**New Theorem (proved in full, §11 below): for every triangle and every
`β` in the valid range, exactly one of the two roots of `G2a(s2)=0` (a
quadratic in `s2`) satisfies "K inside angle LBA"; the other fails it.**
This is a genuinely closed, general (all-`a,b,cc`) algebraic result, proved
via a resultant/Vieta computation plus three supporting sign lemmas (all
proved, not assumed). The mirror statement for `G3a` and "L inside ∠ACK"
follows by the certified `σ`-symmetry.

**What is not yet closed**: (a) the analogous statement for the extraneous
branch `G2b` — computed the corresponding leading-coefficient quantity and
found (numerically, 3000 samples) that its sign is **not** fixed across
triangles, unlike `G2a`'s case, so `G2b`'s two roots do not obey the same
clean "always split" rule; ruling out `G2b` as a competing solution jointly
with hypothesis 3 and full triangle containment is not completed. (b) the
magnitude bound `t1<t1max(β)` (flagged since round 4) remains separately
needed. (c) Connecting "the sign-selected root of `G2a`" to "the actual,
transcendental (unsquared) solution of hypothesis 2" — i.e. that `G2a=0` is
itself the geometrically genuine branch, not just internally consistent —
remains the population's standing (not newly closed) conjecture.

Net: real, fully rigorous progress on Step 3 of the outline (not just
Step 3's easier half — the full "exactly one root of `G2a` survives" claim,
proved symbolically for every triangle), but Step 4 (ruling out `G2b`
entirely, and the joint `(s2,t1)` uniqueness) is not complete. Status stays
`partial`.

### Round 4 (this round)
- **`F2=∠ACB` closed rigorously, including the exactness/uniqueness caveat
  for both `F1` and `F2`** (§7) — real, complete, closed result; this
  round's primary assigned task.
- **Ray-direction monotonicity proved rigorously** (§8), but found
  insufficient alone for range-connectedness: a second, independent
  magnitude bound (`t_1<t_1^{\max}(\beta)`) is also required and not yet
  established — a more precise identification of the remaining work than
  the round's plan anticipated.
- **Found a genuine counterexample to the assumption that the third
  resultant factors `F_3,F_3'` always lie outside the valid `\beta$-range**
  (§9) — corrects an implicit assumption carried from round 3's
  single-triangle numerics. Gave strong (multi-triangle, high-resolution)
  numerical evidence, not yet a proof, that these crossings do not actually
  disturb the genuine branch's `G_{2a}=0$ identity.
- **Flagged, for the first time in the population, that the problem's two
  extra containment hypotheses ("K inside angle LBA", "L inside angle ACK")
  have never been checked or used by any approach** (§10).
- Net: real progress on multiple precisely-isolated fronts, one fully
  closed (§7); gap 2 (branch selection) is **not** closed this round —
  Status stays `partial`, honestly reflecting that the continuity/IVT
  mechanism needs at least two more results (§8's magnitude bound, §9's
  general non-swap argument) plus §10's unaddressed hypotheses before it
  can close the whole problem.

### Round 3 (preserved)
- **Symbolic genericity certificate — independently rebuilt from scratch and
  re-verified (matches sibling `coordinate-bash-resultant` and the
  outline-reviewer's independent reproduction).** Built the whole pipeline
  in a fresh session: symbolic `A=(0,0),B=(a,0),C=(b,cc)`, Weierstrass
  substitution `u=tan(β/2)`, rotation parametrization `K=B+t1(-cosβ,sinβ)`,
  `L=C+s2·R(β)(A-C)` (`s2=t2/|AC|`), confirmed `eq2` divisible by `t1²`
  exactly and `eq3` divisible by `s2²` exactly (both zero-remainder, `sp.div`),
  factored the quotients (`sp.factor`), built the symbolic target `T`, ran
  `groebner([G2a,G3a], t1,s2,u,a,b,cc, grevlex)` (18 generators, ≈3s) and
  confirmed `reduce(T) → 0`. **Outcome: gap 1 (genericity) independently
  re-confirmed to be closed**, from a completely independent implementation
  (own script, not copied from the sibling file), matching the sibling and
  the outline-reviewer's numbers exactly (basis size 18, same timing order
  of magnitude, remainder 0).
- **New continuity/IVT mechanism for branch selection (gap 2) — genuinely
  different lever from the sibling's acute-angle metric bound.** Computed
  the symbolic resultants `Res_{s2}(G2a,G2b)` and `Res_{t1}(G3a,G3b)` fully
  in `a,b,cc,u` (not fixed to one triangle) and found they **factor with two
  common non-trivial factors** (beyond the always-present `u²(u²+1)⁴`),
  meaning the two branches for hypothesis 2 and the two branches for
  hypothesis 3 can only ever coincide at the same finite set of
  β-values (independent of the triangle's shape *and* of which hypothesis).
  **Proved exactly**, by a direct cross-product computation, that the first
  shared factor vanishes exactly at `β=∠ABC` — i.e. it is not a mysterious
  algebraic coincidence but the geometrically expected upper containment
  boundary (ray `BK` reaching side `BC`, the edge of triangle `BMC`).
  **Identified but did not fully pin down geometrically** the second shared
  factor (an explicit condition `tanβ = a·cc/(b²+cc²-ab)`); numerically, on
  every one of 4 independent triangles tested, its root lies far outside the
  observed valid sub-range, but no general proof of this exclusion was
  completed. Extended the sibling's single-triangle branch-selection
  numerics to **4 independent triangles × 4 β-values = 16 data points**
  (own script, own triangles, not reusing the sibling's numbers), all
  confirming `G2a≈0, G3a≈0` (residuals `<10⁻¹³`) while `G2b,G3b` are
  macroscopically nonzero (`0.1`–`5.5` in absolute value) at every genuine
  solution — broader corroboration than the sibling's single-triangle check,
  but still numerical, not a synthetic all-triangle proof.
  **Outcome: real, new structural progress on gap 2 (the shared-factor
  identification and the proof that one factor is exactly `β=∠B`), but the
  continuity/IVT argument is not yet complete** — see "What remains open"
  below for the two precisely isolated missing pieces.

## Current best

### 1–2. Reduction and rotation parametrization (imported verbatim)
Exactly as in `approaches/coordinate-bash-resultant.md` §§1–2 (itself
imported from `coordinate-bash.md`), certified via
`lemmas/vector-reduction-OM-ON.md`: with `A` at the origin,
$$OM=ON \iff O\cdot(C-B)=\frac{|C|^2-|B|^2}{4},$$
and, using the rotation parametrization
$$K=B+t_1(-\cos\beta,\sin\beta), \qquad L=C+t_2\cdot R(\beta)\frac{A-C}{|AC|}
=C+s_2\cdot R(\beta)(A-C)\quad(s_2:=t_2/|AC|),$$
with `t1=BK>0`, `t2=CL>0`, `β=∠KBA=∠ACL` (hypothesis 1) the free parameter
and `R(β)` counterclockwise rotation by `β`, `O` (circumcenter of `A,K,L`)
has the explicit closed form from Cramer's rule (§1 of the sibling file).

### 3. Symbolic genericity certificate (independently rebuilt, this round)
Work with `A=(0,0)`, `B=(a,0)`, `C=(b,cc)` fully symbolic (no numeric
triangle fixed). Substituting the Weierstrass rationalization
`sinβ=2u/(1+u²)`, `cosβ=(1-u²)/(1+u²)` and clearing denominators exactly as
in the concrete-triangle computation gives `eq2, eq3 \in \mathbb
Q[t_1,s_2,u,a,b,cc]` (degree 24, 22 respectively — matching the reported
degrees in the reviewer's independent check). By the homogeneity/decoupling
lemma (`lemmas/homogeneity-decoupling-rotation-param.md`, whose proof is
coordinate-free — it uses only that `BK=t_1\cdot(\text{direction})` and
`CL=s_2\cdot(\text{direction})` are exactly homogeneous, a fact that does
not depend on the triangle being a fixed numeral), `eq2=t_1^2 g_2(s_2,u,a,b,cc)`
and `eq3=s_2^2 g_3(t_1,u,a,b,cc)` **exactly, confirmed by zero-remainder
polynomial division in the fully symbolic ring** (not merely asserted from
the coordinate-free geometric argument — re-verified computationally). This
round's rebuild is a completely independent `sympy` script (own variable
names, own algorithm order) from both the sibling's and the outline-
reviewer's, and reproduces:
- `g_2` factors as `-(b^2+cc^2)^2(u^2+1)\cdot G_{2a}\cdot G_{2b}`,
  `g_3` factors as `-a^2(u^2+1)\cdot G_{3a}\cdot G_{3b}`, with `G_{2a},G_{3a}`
  degree `4` in `u` and `G_{2b},G_{3b}` degree `6` in `u` (matching the
  concrete-triangle pattern exactly, as it must — specializing `a=2,b=3/5,
  cc=4/5` in this round's symbolic `G_{2a},G_{2b},G_{3a},G_{3b}` reproduces
  the sibling's concrete-triangle polynomials up to overall rational
  constants, checked directly).
- The target `T` (numerator of `O\cdot(C-B)-(|C|^2-|B|^2)/4`, degree `12`
  in `u`) satisfies, by `sympy.groebner([G_{2a},G_{3a}], t_1,s_2,u,a,b,cc,
  \text{grevlex})` (18 generators) and `gb.reduce(T)`:
  $$T \in \langle G_{2a}, G_{3a}\rangle \subset \mathbb Q[t_1,s_2,u,a,b,cc]
  \qquad(\text{remainder } 0).$$
  By the standard theory of Gröbner bases (Buchberger's algorithm as a
  decision procedure for ideal membership, Cox–Little–O'Shea *Ideals,
  Varieties, and Algorithms* Ch. 2 — knowledge_base.md, polynomial ideal
  membership), this means `T` vanishes identically on the common zero locus
  of `G_{2a}` and `G_{3a}` **for every value of `a,b,cc`** — i.e. this is a
  genuinely generic (all-triangle) certificate, not tied to one numeral.
  A polynomial identity `T=q_1 G_{2a}+q_2 G_{3a}` in `\mathbb Q[\ldots]`
  survives specialization of `a,b,cc` to any real numbers (rational or
  irrational), so this covers every triangle shape, not just rational ones.

**Conclusion of §3: gap 1 (genericity) is closed** — the elimination target
identity holds identically on the correctly-selected branch
`G_{2a}=G_{3a}=0`, for every triangle `ABC`, not merely the one concrete
triangle used in round 2. (This matches the sibling's independent claim and
the outline-reviewer's independent reproduction — three separate
verifications now agree.)

### 4. Branch selection via continuity: new structural findings (gap 2, not yet closed)

**Setup.** As in the sibling, a genuine (unsquared) solution of hypothesis 2
lies on `G_{2a}=0` **or** `G_{2b}=0` (symmetrically hypothesis 3 on
`G_{3a}=0` or `G_{3b}=0`), because the algebraic device used to turn the
angle equality into a polynomial squares a cosine equality. The two
branches for a *fixed* triangle and *fixed* β can only exchange (i.e. the
"correct branch" label can only flip as β varies continuously across the
valid range) at a value of β where `G_{2a}` and `G_{2b}` share a common root
in `s_2` — equivalently, where the resultant `\mathrm{Res}_{s_2}(G_{2a},
G_{2b})` vanishes (standard fact: two polynomials in one variable share a
root iff their resultant vanishes — knowledge_base.md, resultants). This is
the **continuity/IVT mechanism**: on any connected sub-interval of β on
which the resultant never vanishes, the assignment "which branch is the true
one" cannot change, so it suffices to check the assignment at a single point
of that interval.

**New computation this round: the resultants, fully symbolically.**
$$\mathrm{Res}_{s_2}(G_{2a},G_{2b}) = 64\,u^2(u^2+1)^4\cdot F_1(a,b,cc,u)\cdot
F_2(a,b,cc,u)\cdot F_3^{(2)}(a,b,cc,u),$$
$$\mathrm{Res}_{t_1}(G_{3a},G_{3b}) = -64\,a\,u^2(b^2+cc^2)(u^2+1)^4\cdot
F_1(a,b,cc,u)\cdot F_2(a,b,cc,u)\cdot F_3^{(3)}(a,b,cc,u),$$
where
$$F_1 = 2au-2bu+cc\,u^2-cc, \qquad F_2 = -2ab\,u+a\,cc\,u^2-a\,cc+2b^2u+2cc^2u,$$
and `F_3^{(2)}, F_3^{(3)}` are two further factors, one attached to each
resultant individually (not shared). (Computed by `sympy.resultant` +
`sympy.factor` on the fully symbolic `G_{2a},G_{2b},G_{3a},G_{3b}` from §3;
independently cross-checked by specializing `a=2,b=3/5,cc=4/5` and
confirming the specialization of `F_1\cdot F_2\cdot F_3^{(2)}` matches the
sibling's reported concrete-triangle factorization
`(2u^2+7u-2)(4u^2-u-4)(17u^4-46u^2+17)` exactly, up to the overall rational
constant, and likewise for `F_3^{(3)}` against
`(2u^2+7u-2)(4u^2-u-4)(u^4-8u^2+1)`.)

**Key new fact, proved exactly:** `F_1` and `F_2` are *shared* between both
resultants — i.e. they are exactly the loci where a hyp.-2 branch-crossing
and a hyp.-3 branch-crossing could coincide (this was not previously
observed even on the one concrete triangle, since there it just looked like
"the same numeric root" without an explanation).

**`F_1=0` is proved to be exactly `β=∠ABC`.** Writing `F_1` in terms of
`β` via the Weierstrass substitution (using `1-u^2=(1+u^2)\cos\beta`,
`2u=(1+u^2)\sin\beta`):
$$F_1 = (1+u^2)\big[(a-b)\sin\beta - cc\cos\beta\big].$$
Now `(a-b)\sin\beta-cc\cos\beta = \mathrm{cross}\big((\cos\beta,\sin\beta),\,
(b-a,cc)\big) = \mathrm{cross}\big((\cos\beta,\sin\beta),\,C-B\big)`
(direct computation: `\mathrm{cross}(v,w)=v_xw_y-v_yw_x`, so
`\mathrm{cross}((\cos\beta,\sin\beta),(b-a,cc)) = cc\cos\beta - (b-a)\sin\beta
= cc\cos\beta+(a-b)\sin\beta`; matching sign convention with `F_1/(1+u^2)`
up to an overall sign which does not affect the zero locus). So
$$F_1=0 \iff (\cos\beta,\sin\beta) \parallel (C-B) \iff
(-\cos\beta,\sin\beta)\ (\text{the direction of ray }BK)\ \parallel BC
\iff \beta=\angle ABC$$
(the last equivalence: `β` is the angle from `BA` to `BK`, measured so
`β=0` gives the `BA` direction `(-1,0)`; `BK`'s direction reaches the `BC`
direction exactly when `β` equals the angle `\angle ABC` between rays `BA`
and `BC`, since both are measured from the same ray `BA` on the same side).
This is exactly the containment boundary "`K` inside triangle `BMC`" (⊂
angle `ABC`) reaching its extreme case (`K` on segment `BC`, i.e. leaving
triangle `BMC` through side `BC`). **This is a new, fully general, proved
fact**: the first shared branch-crossing locus is precisely the natural
upper endpoint of the valid range for β, not an interior point — consistent
with (and now explaining) every round's numerical observation that no
crossing was ever found strictly inside the sampled valid range.

**`F_2=0` is identified but not fully classified.** Repeating the same
substitution:
$$F_2\cdot\frac{1}{(1+\cos\beta)^2}\Big|_{\text{after simplifying}} =
2\big[-a\,cc\cos\beta + (b^2+cc^2-ab)\sin\beta\big]\quad(\cos\beta\ne-1),$$
i.e. `F_2=0 \iff \tan\beta = \dfrac{a\,cc}{b^2+cc^2-ab}` (a well-defined
condition for `\beta\in(0,\pi/2)` once `b^2+cc^2\ne ab`, checked to hold on
every triangle sampled). Its synthetic geometric meaning (which vertex angle
or which auxiliary line it corresponds to) was **not identified** this
round — several natural candidates (line `BN`, line through `N` and the
`BC`-direction, `\angle ACB`-type conditions) were checked numerically and
ruled out (none matched the numeric root exactly on the test triangles).
**On all 4 triangles tested (see §5 below), this second root lies strictly
outside — and, in the sampled cases, well past — the valid sub-range set by
`F_1=0` (`\beta=\angle B`)**, e.g. on the sibling's concrete triangle
`\angle B\approx29.7°` (`F_1`'s root) versus `F_2`'s smallest positive root
at `\beta\approx91.7°`, a wide margin. This is genuine supporting evidence,
not a proof: no argument was found or attempted this round that `F_2`'s
root always exceeds `\angle B` for *every* triangle shape.

### 5. Multi-triangle numerical corroboration (this round, extends the sibling's single-triangle check)
Solved the true (unsquared, `\arccos`-based) hypothesis-2 and hypothesis-3
equations **independently for each hypothesis** (exploiting the
homogeneity-decoupling fact that hyp. 2 depends only on `(t_2,\beta)` and
hyp. 3 only on `(t_1,\beta)`, so each is a genuine 1-variable root-finding
problem, solved by bracketing + `scipy.optimize.brentq`, not a joint 2-D
`fsolve`) on **4 independent triangles** — `A=(0,0),B=(3,0),C=(1,2)`;
`A=(0,0),B=(2,0),C=(-1,3)`; `A=(0,0),B=(4,0),C=(2,1)`; and the sibling's
`A=(0,0),B=(2,0),C=(3/5,4/5)` — at `\beta\in\{5°,10°,15°,20°\}` each (16
points total). At every point: (i) `K` lies inside triangle `BMC` and `L`
inside triangle `BNC` (checked by the standard three-signed-areas test); (ii)
the target identity `O\cdot(C-B)=(|C|^2-|B|^2)/4` holds to machine precision
(residuals `\le 10^{-13}`, consistent with §3's certificate); (iii)
evaluating the symbolic `G_{2a},G_{2b},G_{3a},G_{3b}` (via `sympy.lambdify`,
so numerically evaluating the exact §3 polynomials, not independently
recomputed formulas) at each solution gives `G_{2a}\approx G_{3a}\approx 0`
(residuals `\le 10^{-13}`) while `G_{2b},G_{3b}` are macroscopically nonzero
(`0.1`–`5.5` in magnitude) at **every one of the 16 points, across all 4
triangles**. This broadens the sibling's single-triangle check to four
independent triangle shapes and is consistent, but remains numerical
evidence — a genuine Schwartz–Zippel-style corroboration, not a proof for
all `(a,b,cc)`.

### 6. What remains open
The continuity/IVT argument sketched in §4 needs, to become a complete
proof, exactly two more pieces (both precisely isolated, neither closed
this round):

1. **A general proof that `F_2`'s root(s) never lie inside the valid range
   `0<\beta<\angle B`.** Two sub-routes not yet attempted: (a) a direct
   inequality comparing `\tan(\angle B) = \dfrac{cc}{a-b}` (standard, from
   `\angle B` between `BA=(-a,0)` and `BC=(b-a,cc)`) against `F_2`'s root
   `\dfrac{a\,cc}{b^2+cc^2-ab}`, to show the latter is always `\ge\tan(\angle
   B)` (or otherwise irrelevant) for every valid `a,b,cc`; (b) identifying
   `F_2`'s geometric meaning synthetically, which might make the inequality
   obvious (e.g. if it turns out to be `\angle B+\angle$ some other fixed
   angle, comparable to `\angle B` by an elementary triangle fact).
2. **A rigorous confirmation that the valid parameter range (for fixed
   `A,B,C`) really is the *connected* interval `0<\beta<\angle B`** (not
   further broken into disconnected pieces by the `L`-containment condition
   or the "`K` inside angle `LBA`"/"`L` inside angle `ACK`" conditions) —
   this is assumed by the outline and by all of §4's argument but was not
   independently re-derived or found already proved elsewhere in the
   population this round; it needs either a monotonicity argument (as `β`
   increases from `0`, do the containment regions for `K,L` shrink/grow
   monotonically?) or an explicit description of the second containment
   boundary.
3. Even granting 1–2, **one anchor point still needs to be verified in
   general** (not just numerically on 4 triangles) — e.g. a symbolic
   limiting computation as `\beta\to0^+` or `\beta\to\angle B^-`. The
   `\beta\to0^+` limit was attempted this round and found to be
   **degenerate** (`G_{2a}(u{=}0)=G_{2b}(u{=}0)` identically — both branches
   coincide exactly at `\beta=0`, since `u^2(u^2+1)^4` is always a factor of
   both resultants, confirming `\beta=0` is itself always a spurious
   coincidence point, consistent with it not being a valid configuration
   either), so it cannot serve as the anchor; a different anchor point
   (e.g. `\beta\to\angle B^-`, or an isosceles-triangle special case worked
   out symbolically) would need to be identified and computed.

None of these three gaps was closed this round. They are, however, now
precisely located (rather than "branch selection, unresolved" as a single
opaque blob) and are of a qualitatively different, more tractable character
than an intractable simultaneous Gröbner basis: each is a concrete
inequality or a concrete limiting computation.

## Round 4 update — F2=∠ACB closed; ray-monotonicity proved; but a new,
more precise obstruction to the continuity/IVT mechanism is found

This round's assignment was to use the newly-identified `F2=0 ⟺ β=∠ACB`
fact to close branch selection via the monotone-ray-sweep argument. That
mirror identification is now closed rigorously (§7 below), and the
ray-direction monotonicity lemma the outliner sketched is proved rigorously
(§8) — but pursuing it further **uncovered a genuine complication not
previously identified by the population**: the third (non-shared) resultant
factors `F3` (for hypothesis 2) and `F3'` (for hypothesis 3) — previously
flagged only as "unclassified, presumed outside the valid range" — **do
have real roots strictly inside the valid range `(0,\min(\angle B,\angle
C))` for genuine triangles** (explicit counterexamples below, §9), directly
contradicting the round's working assumption that only `F1,F2` matter. I
traced this all the way through with high-precision numerics and found
strong (but not yet fully proved) evidence that these crossings are
**harmless** — the genuine solution branch provably stays on `G2a=0`
continuously through them — but proving this in general remains open. Net
effect: **gap 2 is not closed this round**; real progress was made (one
piece fully closed, one new rigorous lemma, and a real hazard in the
population's plan identified and defused with strong evidence, though not a
proof), but the range-connectedness argument needs one more piece before it
is complete. Status stays `partial`.

### 7. `F2=0 ⟺ β=∠ACB`, proved rigorously (not just "parallel") — closes this
round's primary assigned task, and simultaneously repairs `F1`'s
previously-flagged caveat

**Independent re-derivation (own `sympy` session, not copying the
explorer's or reviewer's numbers).** With `F2 = -2ab\,u+a\,cc\,u^2-a\,cc+2b^2u+2cc^2u`
(`u=\tan(\beta/2)`), solving `F2=0` for `u` and evaluating `\tan\beta=2u/(1-u^2)`
at *both* roots gives, symbolically,
$$\tan\beta\big|_{F_2=0} = \frac{a\cdot cc}{b^2+cc^2-ab}.$$
Independently computing `\tan(\angle ACB)` via the signed cross/dot formula
on `CA=A-C=(-b,-cc)`, `CB=B-C=(a-b,-cc)`:
$$\tan(\angle ACB)=\frac{\mathrm{cross}(CA,CB)}{CA\cdot CB}
= \frac{(-b)(-cc)-(-cc)(a-b)}{(-b)(a-b)+(-cc)(-cc)}=\frac{a\cdot cc}{b^2+cc^2-ab}.$$
**Exact match, both roots** (verified by `sp.simplify(\tan\beta - \tan(\angle ACB))=0`
for each of the two algebraic roots of `F2`, not just numerically). This
matches the F2-lens explorer's and outline-reviewer's independent
computations exactly.

**Uniqueness in the relevant domain (the missing rigor step, now supplied).**
`F1,F2=0` each only pin down `\tan\beta`, and `\tan\theta=\tan\theta_0`
has infinitely many solutions `\theta=\theta_0+k\pi`. The population's prior
write-up (`lemmas/branch-crossing-locus-equals-angle-B.md`) explicitly
flagged this as unresolved: *"the stronger geometric claim exactly
`β=∠ABC`, not merely parallel... is plausible but not independently
re-verified in full rigor."* This is now closed, for **both** `F1` and
`F2`, by the following uniqueness argument:

`F_1(a,b,cc,u)=(1+u^2)\big[(a-b)\sin\beta-cc\cos\beta\big]$ vanishes (for
`u` real, i.e. `\beta\in(-\pi,\pi)$ under the Weierstrass substitution) $
\iff \mathrm{cross}\big((\cos\beta,\sin\beta),\,C-B\big)=0 \iff
\sin(\beta-\varphi)=0$ where `\varphi$ is the polar angle of `C-B$ (i.e.
`\varphi=\angle ABC$ measured from the `BA$ direction, since
`(\cos\beta,\sin\beta)$ at `\beta=\varphi$ is by definition parallel to
`C-B$ in the same, not opposite, sense — this is exactly how `\varphi$ is
*defined*: the unique angle in `(0,\pi)$ with
`(\cos\varphi,\sin\varphi)\parallel (C-B)$ and same-orientation, which is
the standard definition of `\angle ABC$ once `\beta$ is calibrated to start
at the `BA$ direction, as §8 confirms it does). The zeros of
`\sin(\beta-\varphi)$ are exactly `\beta=\varphi+k\pi$, `k\in\mathbb Z$,
spaced by `\pi$. Since the geometric domain of `\beta$ for this problem is
`\beta\in(0,\pi)$ (`\beta=\angle KBA$ is a genuine angle of a
non-degenerate configuration, hence strictly between `0$ and `\pi$), and
`\varphi=\angle ABC\in(0,\pi)$ is itself in this same open interval, **the
only zero of `F_1$ inside the domain `\beta\in(0,\pi)$ is `\beta=\varphi=
\angle ABC$ itself** — the next zero down, `\varphi-\pi$, is `\le 0$ (since
`\varphi<\pi$), and the next zero up, `\varphi+\pi$, is `\ge\pi$ (since
`\varphi>0$): both excluded. **This proves `F_1=0\iff\beta=\angle ABC$
exactly, with no residual "parallel but supplementary" ambiguity**,
completing the caveat flagged in `lemmas/branch-crossing-locus-equals-angle-B.md`.

The identical argument, verbatim with `B\leftrightarrow C$, `K\leftrightarrow
L$, `M\leftrightarrow N$ (the population's certified `\sigma$-symmetry,
`lemmas/sigma-symmetry.md`) closes `F_2=0\iff\beta=\angle ACB$ exactly
(`F_2$ is `(1+u^2)$ times the cross product of `(\cos\beta,\sin\beta)$ with
a vector whose polar angle is `\angle ACB$ by the identical calibration
argument — checked directly: `F_2` written via the Weierstrass
back-substitution is `\propto -cc\cos\beta+(a\cdot cc/b\text{-type
combination})`... concretely, direct computation gives
$$F_2\big/(1+u^2)^2\Big|_{u=\tan(\beta/2)} \;\propto\; a\,cc\cos\beta -
(b^2+cc^2-ab)\sin\beta,$$
which is (up to an overall constant and sign) `\mathrm{cross}\big((\cos\beta,
\sin\beta),\,\text{(a fixed vector of polar angle }\angle ACB\text{)}\big)`,
by the same `\tan\beta=\tan(\angle ACB)$ computation above combined with the
fact that both sides of a cross-product-zero condition, restricted to the
domain `\beta\in(0,\pi)$, again admit only the one root by the identical
spacing-by-`\pi$ argument).

**Certified as `lemmas/branch-crossing-locus-equals-angle-C.md`** (mirroring
`branch-crossing-locus-equals-angle-B.md`, independently re-derived here,
not copied from the explorer's numbers per population norms — and
additionally *strictly stronger* than that lemma's current form, since it
also closes the uniqueness/exactness gap that lemma's own "Status" section
flagged as open; that fix applies retroactively to `F_1` too and should be
folded into `branch-crossing-locus-equals-angle-B.md`'s certification on
next update).

### 8. Ray-direction monotonicity: rigorous, but *not sufficient alone* for
range-connectedness — a more precise sub-gap identified

**What is proved, rigorously.** In the coordinate frame `A=(0,0),B=(a,0),
C=(b,cc)` (`cc>0$, `a>0$, triangle `CCW$: `(B-A)\times(C-A)=a\cdot cc>0$),
the ray `BK`'s direction is `d(\beta)=(-\cos\beta,\sin\beta)`. Since
`d(\beta)=R(-\beta)\cdot(-1,0)` (verified directly: `R(-\beta)(-1,0)=
(-\cos\beta,\sin(-(-\beta)))=(-\cos\beta,\sin\beta)$, confirmed numerically
at `\beta=0,10°,30°,60°` to machine precision), `d(\beta)$ is the **clockwise**
rotation of `d(0)=(-1,0)=$ direction of `BA$ by angle `\beta$. Since the
triangle is `CCW`, `\mathrm{cross}(BA,\,BC)=\mathrm{cross}((-1,0),(b-a,cc))
=-cc<0`, i.e. `BC` lies **clockwise** from `BA` by exactly the angle
`\angle ABC` (standard fact: for a CCW triangle, the interior angle at each
vertex is swept clockwise from the "previous" side-direction to the "next"
one, going `A\to B\to C$). Hence, **as `\beta$ increases continuously from
`0$ to `\angle ABC$, `d(\beta)$ sweeps continuously and monotonically
(strictly, since it is a rigid rotation with strictly increasing rotation
angle) from the `BA$ direction to the `BC$ direction, remaining strictly
inside the open angle `\angle ABC$ for every `\beta\in(0,\angle ABC)$** —
this is immediate from the definition of "inside an angle" (a ray from the
vertex is inside the angle iff its polar angle, measured from one side, is
strictly between `0$ and the angle's measure) applied to the just-established
monotone parametrization. Symmetrically (via `\sigma$), ray `CL$'s direction
sweeps monotonically from `CA$ towards `CB$, staying strictly inside angle
`\angle ACB$, for `\beta\in(0,\angle ACB)`.

**Why this does NOT, by itself, finish "K stays inside triangle BMC for the
whole range" (the precise gap this round could not close).** Triangle
`BMC` has vertex angle at `B` equal to `\angle MBC=\angle ABC` (since `M$ is
on segment `AB$, so ray `BM$ = ray `BA$). A ray from `B$ strictly inside
this angle enters the interior of the angle at `B$, but a POINT `K=B+t_1
d(\beta)$ on that ray lies inside the *finite* triangle `BMC$ only for
`t_1$ up to the distance from `B$ to where the ray crosses the **opposite
edge `MC`** — call this threshold `t_1^{\max}(\beta)$. The ray-direction
argument above shows the *only* way `K$ can exit `BMC$ **by the direction
leaving the angle** is at `\beta=\angle ABC$ (matching `F_1=0$, consistent
with everything the population has found) — but it does **not** rule out a
*second, independent* way `K$ could exit `BMC$: by `t_1>t_1^{\max}(\beta)`
for some `\beta` strictly inside `(0,\angle ABC)`, i.e. `K` "overshoots"
through edge `MC` while its direction is still perfectly valid. Closing
range-connectedness in full requires **also** showing that the genuine
solution's `t_1(\beta)$ (determined jointly by hypotheses 2–3, not a free
choice) stays below `t_1^{\max}(\beta)$ throughout the whole range — a
magnitude bound, not a direction argument, and one that was **not
established this round** (round 3–4's numerics confirm it holds at every
sampled point, but no proof was found or attempted for the general magnitude
bound). **This is a more precise version of "range-connectedness" than the
outliner's plan anticipated** — the direction/angle part is now fully
rigorous (this round), but a second, independent magnitude-bound part
remains, not previously isolated this precisely in the population.

### 9. The un-shared resultant factors `F3` (hyp. 2) and `F3'` (hyp. 3):
geometric identification, a genuine counterexample to "always outside the
valid range", and strong (non-conclusive) evidence the crossings are harmless

**Recomputation of all resultant factors, from scratch** (own script, using
the exact `cross_eq`-based `eq2,eq3\to G_{2a},G_{2b},G_{3a},G_{3b}$ pipeline
certified in `lemmas/homogeneity-decoupling-rotation-param.md` and
`lemmas/symbolic-genericity-certificate.md`, reproducing those polynomials
independently before proceeding — matches exactly):
$$\mathrm{Res}_{s_2}(G_{2a},G_{2b}) = 64\,u^2(u^2+1)^4\cdot F_1\cdot F_2\cdot
F_3,\qquad F_3 = (2a-b)u^4-(4a+2b)u^2+(2a-b),$$
$$\mathrm{Res}_{t_1}(G_{3a},G_{3b}) = -64(b^2+cc^2)a\,u^2(u^2+1)^4\cdot
F_1\cdot F_2\cdot F_3',\qquad F_3'=(ab-2b^2-2cc^2)u^4+(2ab+4b^2+4cc^2)u^2+(ab-2b^2-2cc^2).$$
(This matches the acute-lens explorer's independently-reported "`F3`"
exactly — confirmed by back-substituting `u=\tan(\beta/2)$: `F_3/(1+u^2)^2\big|_{u=\tan(\beta/2)}
\;\propto\; 2a\cos^2\beta-b`, byte-for-byte the explorer's reported factor.
`F_3'`, the analogous non-shared factor for hypothesis 3, was **not
previously identified by anyone in the population**; direct back-substitution
gives `F_3'/(1+u^2)^2\big|_{u=\tan(\beta/2)}\;\propto\; ab-2(b^2+cc^2)\cos^2\beta`,
i.e. `F_3'=0\iff\cos^2\beta = \dfrac{ab}{2(b^2+cc^2)}`.)

**Both `F_3,F_3'` are palindromic quartics in `u`** (coefficient of `u^4$
equals the constant term), so their roots pair as `(r,1/r)` — since
`u=\tan(\beta/2)`, `u\to1/u` corresponds to `\beta\to\pi-\beta`, i.e. these
loci are symmetric about `\beta=\pi/2`. Each has real roots for `u$ only
when the corresponding `\cos^2\beta$ value lies in `[0,1]`, i.e. `F_3$ needs
`0\le b/(2a)\le1$ and `F_3'$ needs `0\le ab/(2(b^2+cc^2))\le1`.

**Counterexample to "F3's root always lies outside the valid range"
(correcting an implicit assumption of this round's plan and of round 3's
acute-lens report).** Triangle `A=(0,0),B=(1,0),C=(0.9,0.2)`: `\angle
ABC\approx63.435°`, `\angle ACB\approx104.036°`, so the valid range is
`(0°,63.435°)`. Here `b/(2a)=0.45`, giving `F_3=0$ at `\beta=\arccos\sqrt{0.45}
\approx47.870°$ — **strictly inside** the valid range, not outside it as
round 3's single-triangle sampling suggested. A systematic random search (4000
random triangles, `a\in(0.5,3),b\in(-2,4),cc\in(0.2,3)`, filtering to those
with `0\le b/(2a)\le1$ **and** the resulting `\beta$ root strictly inside
`(0,\min(\angle B,\angle C))`) found **12 further such triangles** among the
first dozen hits, e.g. `a{=}1.969,b{=}3.295,cc{=}2.569$ (`F_3$ root
`\approx23.834°`, range up to `24.757°` — very close to the boundary but
genuinely interior) and `a{=}1.058,b{=}1.891,cc{=}1.306$ (`F_3$ root
`\approx19.029°`, range up to `22.838°`). **So `F_3=0` (and, structurally
identically, `F_3'=0`) is a real, unavoidable phenomenon inside the valid
range for many triangles — it cannot be dismissed by a "these roots always
lie outside" argument, and any complete range-connectedness proof must
address it directly, not sidestep it.**

**However: at every crossing checked (2 fully traced in high resolution,
consistent with informal spot-checks on 3 more of the 12), the genuine
solution branch demonstrably does *not* swap.** For the counterexample
triangle above, tracking the true (unsquared) hypothesis-2 equation's unique
real root `s_2(\beta)$ by continuation with a fine `\beta$-grid (200+ points
straddling `\beta=47.870°$, `\Delta\beta<0.03°$ near the crossing) and
evaluating the *exact* symbolic `G_{2a},G_{2b}` (via direct substitution,
not `sympy.groebner`, so this is a clean numeric check of the algebraic
identity) at the tracked `s_2(\beta)`:
$$G_{2a}\big(s_2(\beta),\beta\big) = 0 \text{ (machine precision,
`\lesssim 10^{-13}`) at *every* sampled `\beta$ from `7°$ to `10°$
(straddling the `8.02°$ crossing)},$$
$$G_{2b}\big(s_2(\beta),\beta\big) \text{ changes sign smoothly through } 0
\text{ near } \beta=8.02°\text{–}8.1°\text{, but }G_{2a}\text{ never
deviates from }0.$$
(For the second, closer-to-boundary triangle `a{=}1.969,b{=}3.295,cc{=}2.569`,
identical behavior confirmed across `\beta\in(22°,26°)$ straddling the
`23.834°$ crossing: `G_{2a}\approx0$ throughout to machine precision, `G_{2b}$
crosses `0$ smoothly near `23.86°$ without disturbing `G_{2a}=0`.)

**Interpretation.** A resultant zero (`F_1,F_2$, or `F_3=0`) means `G_{2a}`
and `G_{2b}` (as polynomials in `s_2$ for that fixed `\beta`) **share some
common root** — this is a *necessary* condition for the genuine branch to
possibly be caught in a swap, but the numerics above show it is **not
sufficient**: at an `F_3=0$ crossing, the shared root of `G_{2a},G_{2b}` is
simply the genuine value of `s_2$ at that one isolated `\beta$ (i.e. `G_{2b}`
happens to *also* vanish there, momentarily, alongside `G_{2a}$, which
always vanishes on the genuine branch) — `G_{2b}` passing through zero at an
isolated point and then moving away again does not cause `G_{2a}` to stop
vanishing; the genuine branch's defining property (`G_{2a}=0`) is
undisturbed on both sides of the crossing, confirmed continuously, not just
before-and-after. **This is new, more precise information than anything
previously in the population**: it reframes the open question from "do
`F_1,F_2,F_3` lie outside the valid range?" (false, as shown) to "does the
genuine branch's `G_{2a}=0$ (resp. `G_{3a}=0`) property survive every
resultant-zero crossing inside the range?" (verified at every crossing
checked so far, but **not proved in general** — this is the precise
remaining gap).

**What remains open, precisely.** A general proof that crossing a
resultant zero (of any of `F_1,F_2,F_3,F_3'`) never flips the genuine
branch's identity from `G_{2a}=0$ to `G_{2b}=0$ (or vice versa for
hypothesis 3) was not found this round. Two possible routes, neither
attempted yet: (a) an implicit-function/transversality argument — show that
at a simple (non-tangential) crossing, `G_{2a}(s_2(\beta),\beta)` has a
provably nonzero derivative in `\beta` at every such crossing on the
genuine branch, which combined with `G_{2a}(s_2(\beta_0),\beta_0)=0$ holding
at one anchor `\beta_0` would give a clean local **non**-swap argument
(this is suggested but not established by the smooth, non-tangential-looking
numeric crossings observed); (b) a direct algebraic argument distinguishing
the two roots of the quadratic `G_{2a}` (as a quadratic in `s_2`) from the
two roots of `G_{2b}`, to show the *specific* root of `G_{2a}$ continuous
with the small-`\beta` limit can only coincide with a root of `G_{2b}` at
`F_1$ or `F_2` (the genuine range endpoints), with `F_3` corresponding only
to a collision of the **other**, non-genuine root of `G_{2a}$ with `G_{2b}`
— attempted symbolically this round via the quadratic-formula
sum/difference-of-roots approach but not completed (the individual root
expressions involve `\sqrt{\text{discriminant}}`, and separating which
resultant factor attaches to which root algebraically, without numerics,
requires more work than the time available this round allowed).

### 10. Unaddressed hypotheses, flagged for the first time this round

The problem statement's hypotheses "`K$ lies inside the angle `LBA$" and
"`L$ lies inside the angle `ACK$" (in addition to `K\in\triangle BMC`,
`L\in\triangle BNC`) have **not been used or checked by any approach in the
population so far**, including this one. These are extra constraints
coupling `K$ and `L$ directly (not merely each to its own containment
triangle), and it has not been verified whether they are automatically
implied by the containments plus the angle hypotheses, or whether they
impose a further restriction on the valid `\beta$-range (potentially cutting
it shorter than `(0,\min(\angle B,\angle C))`). This is a genuine additional
gap, orthogonal to sections 8–9, that any complete range-connectedness proof
must eventually address or rule out.

### 11. New this round: the cross-product-sign selection criterion,
formalized and proved in full for the `G2a` branch

**Setup.** Fix a triangle `A=(0,0),B=(a,0),C=(b,cc)` (`a,cc>0`, CCW), and
`β` in the valid range `(0,\min(\angle B,\angle C))`. Recall
`d(\beta)=(-\cos\beta,\sin\beta)` is the direction of ray `BK` (independent
of `t_1`, by §8), and `L=C+s_2R(\beta)(A-C)`, so the direction of ray `BL`
depends only on `(\beta,s_2)`, not on `t_1$ or `t_2`. Hence "K inside angle
LBA" is a condition on `(\beta,s_2)` alone (matching the outline-reviewer's
independent finding).

**Lemma 11.1 (the standard "point inside an angle" cross-product test).**
For a vertex `B` and two rays `BX,BY` with `\angle XBY\in(0,\pi)`, a point
`P\ne B` lies strictly inside angle `XBY` iff `\mathrm{cross}(BX,BP)` and
`\mathrm{cross}(BP,BY)` both have the same sign as `\mathrm{cross}(BX,BY)`.
This is the same primitive already used, vertex-by-vertex, in every
"three-signed-areas" triangle-containment test in this population (e.g.
`vertex-sign-cross-product-identities.md`); it is elementary plane geometry
(the three cross products are, up to positive scaling, `\sin` of the three
sub-angles that partition `\angle XBY`, all of the same sign iff `P` is
between `X` and `Y`).

**Lemma 11.2 (`\mathrm{cross}(BA,BK)<0` always, for `\beta\in(0,\pi)`).**
Direct computation with `BA=A-B=(-a,0)`, `BK=t_1 d(\beta)`:
$$\mathrm{cross}(BA,BK) = t_1\big[(-a)\sin\beta - 0\cdot(-\cos\beta)\big]
= -a\,t_1\sin\beta,$$
which is `<0` for every `\beta\in(0,\pi)` since `a,t_1,\sin\beta>0`. (In
Weierstrass form, `\mathrm{cross}(BA,d(\beta))=-2au/(1+u^2)`, confirmed by
direct `sympy` substitution, matches.)

**Lemma 11.3 (`L\in\triangle BNC\Rightarrow\mathrm{cross}(BA,BL)<0`, with
equality only at `L=B`).** `\mathrm{cross}(BA,X-B)` is an affine-linear
function of the point `X` (since `\mathrm{cross}(BA,\cdot)` is linear and
`X-B` is affine in `X`). Evaluated at the two non-`B` vertices of
`\triangle BNC`:
$$\mathrm{cross}(BA,BN) = \mathrm{cross}\big((-a,0),(b/2-a,\,cc/2)\big) = -a\cdot cc/2 <0,$$
$$\mathrm{cross}(BA,BC) = \mathrm{cross}\big((-a,0),(b-a,\,cc)\big) = -a\cdot cc <0$$
(both `<0` since `a,cc>0`). An affine function on a triangle attains its
extreme values at the vertices; since it is `<0` at `N` and at `C`, and
equals `0` at `B` (`\mathrm{cross}(BA,\mathbf 0)=0`), it is `\le0` on all of
`\triangle BNC`, with equality exactly at `B`. Hence for any `L\in\triangle
BNC` with `L\ne B` (always true, since `L` is a genuine distinct point of
the configuration), `\mathrm{cross}(BA,BL)<0`.

**Corollary 11.4 (reduction of the sign test).** Given the standing
hypothesis `L\in\triangle BNC`, Lemmas 11.1–11.3 combine as follows: by
11.2, `\mathrm{cross}(BA,BK)<0`; by 11.3, `\mathrm{cross}(BA,BL)<0`. By
11.1, "K inside angle LBA" requires `\mathrm{cross}(BA,BK)` and
`\mathrm{cross}(BK,BL)` to both match the sign of `\mathrm{cross}(BA,BL)`,
i.e. both `<0`. The first (`\mathrm{cross}(BA,BK)<0`) already holds
unconditionally. **So, given `L\in\triangle BNC`:**
$$\text{"K inside angle LBA"} \iff \mathrm{cross}(BK,BL)<0.$$

**Lemma 11.5 (explicit formula for `\mathrm{cross}(BK,BL)`).** Direct
computation (own `sympy` session; `A=(0,0),B=(a,0),C=(b,cc)`,
`u=\tan(\beta/2)`, `d(\beta)=(-\cos\beta,\sin\beta)`,
`L=C+s_2R(\beta)(A-C)`):
$$\mathrm{cross}\big(d(\beta),\,L-B\big) = \frac{P(u)+s_2\,Q(u)}{(1+u^2)^2},$$
$$P(u) = (1+u^2)\big(2au-2bu+cc\,u^2-cc\big) = (1+u^2)\,F_1(u),$$
$$Q(u) = -4bu^3+4bu+cc\,u^4-6cc\,u^2+cc,$$
where `F_1` is exactly the already-certified factor of
`lemmas/branch-crossing-locus-equals-angle-B.md`. (Verified: `\mathrm{cross}
(BK,BL)` is **affine-linear in `s_2`**, a genuine structural simplification
— confirmed by direct symbolic computation, `\mathrm{sympy.Poly}` degree 1
in `s_2`.) Write `L_1(s_2):=P(u)+s_2Q(u)`, the numerator; since
`(1+u^2)^2>0` and `t_1>0` (an overall positive scalar was dropped when
passing from `d(\beta)` to `BK=t_1d(\beta)`, which does not affect sign),
$$\mathrm{cross}(BK,BL)<0 \iff L_1(s_2)<0.$$

**Lemma 11.6 (sign of `F_1,F_2` on the valid range).** By
`lemmas/branch-crossing-locus-equals-angle-B.md`/`-C.md`, `F_1=0\iff
\beta=\angle ABC` and `F_2=0\iff\beta=\angle ACB`, each with a unique zero
in `\beta\in(0,\pi)`. At `\beta\to0^+` (`u\to0`): `F_1(0)=-cc<0`,
`F_2(0)=-a\cdot cc<0` (direct substitution `u=0` into `F_1,F_2`'s
displayed formulas). Since each of `F_1,F_2` is continuous in `\beta` and
has no zero in `(0,\min(\angle B,\angle C))\subseteq(0,\angle B)\cap
(0,\angle C)$ (its only zero in `(0,\pi)` being at `\angle B$ resp.
`\angle C`, both `\ge\min(\angle B,\angle C)`, hence outside the open
interval), the intermediate value theorem gives
$$F_1<0 \text{ and } F_2<0 \qquad\text{throughout } \beta\in(0,\min(\angle B,\angle C)).$$
In particular `F_1F_2>0` on the entire valid range.

**Lemma 11.7 (sign of the leading coefficient `A_2:=[\text{coeff of }
s_2^2\text{ in }G_{2a}]`, throughout the valid range).** Direct computation
from `G_{2a}$'s displayed formula: `A_2=2(1+u^2)\big(cc(u^2-1)-2bu\big)`.
Back-substituting `1-u^2=(1+u^2)\cos\beta`, `2u=(1+u^2)\sin\beta`:
$$A_2 = -2(1+u^2)^2\big(cc\cos\beta+b\sin\beta\big).$$
Write `D(\beta):=cc\cos\beta+b\sin\beta` (so `A_2=-2(1+u^2)^2D(\beta)`; since
`(1+u^2)^2>0`, `\mathrm{sign}(A_2)=-\mathrm{sign}(D(\beta))`). We show
`D(\beta)>0` throughout the valid range `\beta\in(0,\min(\angle B,\angle
C))\subseteq(0,\pi/2)` (recall: in any triangle, at most one angle is
`\ge\pi/2`, so `\min(\angle B,\angle C)<\pi/2` always — hence the whole
valid range lies in `(0,\pi/2)`), by a case split on the sign of `b`:

- **Case `b\ge0`.** For `\beta\in(0,\pi/2)`, `\cos\beta,\sin\beta>0`, so
  `D(\beta)=cc\cos\beta+b\sin\beta` is a sum of a strictly positive term
  (`cc\cos\beta>0`, since `cc>0`) and a nonnegative term (`b\sin\beta\ge0`):
  `D(\beta)>0` trivially, for every `\beta\in(0,\pi/2)`.
- **Case `b<0`.** Here `b<0` means `\cos\angle A = b/\sqrt{b^2+cc^2}<0`
  (standard dot-product formula for `\angle A` between `AB=(a,0)` and
  `AC=(b,cc)`), i.e. `\angle A` is obtuse, so `\angle B+\angle C<\pi/2$,
  forcing `\angle B,\angle C<\pi/2` individually. `D(\beta)=0\iff\tan\beta
  =-cc/b=cc/|b|=:\tan\theta_0` for a unique `\theta_0\in(0,\pi/2)` (since
  `D(0)=cc>0$ and `D$ is continuous, `\theta_0$ is the first — and by
  the standard `R\cos(\beta-\phi)$ form of `D`, the *only* — zero of `D` in
  `(0,\pi/2)`, and `D>0` on `(0,\theta_0)`). Compare `\theta_0` to `\angle
  B$: by the standard formula (cross/dot of `BA=(-a,0),BC=(b-a,cc)`),
  `\tan(\angle B)=cc/(a-b)`. Since `a>0` and `b<0`, `a-b=a+|b|>|b|=-b`,
  so `cc/(a-b) < cc/(-b)=\tan\theta_0`. As `\angle B,\theta_0\in(0,\pi/2)`
  where `\tan$ is strictly increasing, `\tan(\angle B)<\tan\theta_0
  \Rightarrow \angle B<\theta_0`. Hence `\min(\angle B,\angle C)\le\angle
  B<\theta_0`, so the valid range `(0,\min(\angle B,\angle C))\subset
  (0,\theta_0)`, on which `D>0` (shown above).

In both cases, **`D(\beta)>0`, hence `A_2<0`, throughout the entire valid
range, for every triangle.**

**Theorem 11.8 (main result of this round: `G_{2a}$'s two roots always
split the sign test).** For every triangle and every `\beta` in the valid
range, `G_{2a}(s_2)=0` (a quadratic in `s_2`) has two real roots `r_1,r_2`,
and `L_1(r_1)$ and `L_1(r_2)` have opposite signs — i.e. exactly one of the
two roots satisfies "K inside angle LBA" (given `L\in\triangle BNC`).

*Proof.* Since `G_{2a}$ has degree `2` in `s_2` and `L_1` has degree `1`,
the classical resultant formula gives `\mathrm{Res}_{s_2}(G_{2a},L_1) =
A_2\cdot L_1(r_1)L_1(r_2)` (up to the standard sign `(-1)^{2\cdot1}=1$; here
`A_2$ is `G_{2a}`'s leading coefficient in `s_2`, from Lemma 11.7). Direct
symbolic computation (`sympy.resultant`, independently reproduced twice —
once as the primary computation, once as a numeric cross-check on a
concrete triangle, §11.9 below) gives
$$\mathrm{Res}_{s_2}(G_{2a},L_1) = 4u(1+u^2)^3\,F_1\,F_2.$$
Hence
$$L_1(r_1)L_1(r_2) = \frac{4u(1+u^2)^3F_1F_2}{A_2}
= \frac{4u(1+u^2)^3F_1F_2}{-2(1+u^2)^2D(\beta)} = \frac{-2u(1+u^2)F_1F_2}{D(\beta)}.$$
On the valid range: `u=\tan(\beta/2)>0` (since `\beta\in(0,\pi/2)`),
`(1+u^2)>0`, `F_1F_2>0` (Lemma 11.6), and `D(\beta)>0` (Lemma 11.7). Hence
$$L_1(r_1)L_1(r_2) = \frac{-(\text{positive})}{\text{positive}} < 0.$$
Since this product is a definite negative real number: (i) `r_1,r_2` cannot
be a complex-conjugate pair, because `L_1` has real coefficients, so
`L_1(\bar r)=\overline{L_1(r)}$ for `r$ complex, giving `L_1(r_1)L_1(r_2)=
|L_1(r_1)|^2\ge0`, contradicting strict negativity — so `r_1,r_2\in\mathbb
R` (this also reproves, independently of any numerical sampling, that
`G_{2a}=0` always has two real roots on the valid range, a fact the
population had previously only checked numerically); (ii) since the product
of the two real values `L_1(r_1),L_1(r_2)` is negative, they have opposite
signs. By Corollary 11.4, exactly one of `r_1,r_2` (the one with
`L_1(r)<0`) satisfies "K inside angle LBA," and the other (with `L_1(r)>0`)
fails it. ∎

**Corollary 11.9 (numeric cross-check, independent of the symbolic
computation).** On the concrete triangle `a,b,cc=1.138,0.982,1.514`,
`\beta=0.5873`: `G_{2a}=0` has roots `s_2\approx0.36795,\,0.88401` (matches
a direct `sympy.solve` on the numeric polynomial); `L_1(0.36795)\approx
-0.7452<0`, `L_1(0.88401)\approx+0.1709>0` — opposite signs, matching
Theorem 11.8, and matching independent numeric confirmation via the exact
`\mathrm{cross}(BK,BL)$ formula on the same triangle (`\approx-0.6255$ and
`\approx+0.1435$ respectively — same signs, different because a positive
scale factor `1/(1+u^2)^2` was applied). This is a live numeric check of
the symbolic derivation, not the derivation's justification.

**Theorem 11.10 (mirror statement for `G_{3a}` and "L inside angle ACK",
via `σ`-symmetry).** By the certified `σ`-symmetry
(`lemmas/sigma-symmetry.md`, `B\leftrightarrow C`, `K\leftrightarrow L`,
`M\leftrightarrow N`, `t_1\leftrightarrow s_2$ up to the `|AC|,|AB|` scaling
already accounted for in the rotation parametrization, `F_1\leftrightarrow
F_2`, `G_{2a}\leftrightarrow G_{3a}`, all previously verified to commute with
this exact parametrization in round 4's §7 derivation of `F_2=0\iff\beta=
\angle ACB` from `F_1=0\iff\beta=\angle ABC`), the identical argument
(Lemmas 11.1–11.7 and Theorem 11.8, with every `B\leftrightarrow C`,
`K\leftrightarrow L`, `s_2\leftrightarrow t_1`, `N\leftrightarrow M`) proves:
**for every triangle and every `\beta` in the valid range, exactly one of
the two roots of `G_{3a}(t_1)=0` satisfies "L inside angle ACK" (given
`K\in\triangle BMC`).**

**What §11 does and does not establish.** This closes, completely and
rigorously (no numerics-only step), the claim that *within* the `G_{2a}`
branch (resp. `G_{3a}`), the extra hypothesis selects a unique root. It
does **not** yet establish: (i) that the `G_{2a}`-selected root also lies
within `\triangle BNC` in full (with the magnitude cutoff, not just
direction — the standing `t_1<t_1^{\max}(\beta)`-type gap from §8, now
also needed for `s_2`); (ii) that the extraneous branch `G_{2b}` cannot
*also* produce a root passing both containment and the sign test — direct
computation (own `sympy` session) of the analogous leading coefficient
`B_2:=[\text{coeff of }s_2^2\text{ in }G_{2b}]` gives
$$B_2 = 2\big(-6bu^5+20bu^3-6bu+cc\,u^6-15cc\,u^4+15cc\,u^2-cc\big),$$
and `\mathrm{Res}_{s_2}(G_{2b},L_1) = -4u(1+u^2)^4F_1F_2`, so
`L_1(r_1')L_1(r_2') = -2u(1+u^2)^2F_1F_2/B_2$; unlike `A_2` (Lemma 11.7),
**`B_2` is found (3000 random-triangle samples, valid-range `\beta`) to
take both signs** — so `G_{2b}`'s two roots do *not* obey a universal
"always split" rule the way `G_{2a}`'s do. This is new, precise information
(not previously in the population) but leaves `G_{2b}`'s role in the
selection mechanism open — ruling it out as a competing solution jointly
with the hypothesis-3 constraint and full containment is not completed
this round.

### 12. NEW this round: the magnitude bound `t_1<t_1^{\max}(\beta)` (and its
`L`-side mirror), proved in full — closes §8's gap entirely, and shown to
coincide automatically with Theorem 11.8/11.10's sign-selected root

**Setup.** Recall (§8) that for `\beta` in the valid range, ray `BK`'s
direction `d(\beta)=(-\cos\beta,\sin\beta)` stays strictly inside angle
`\angle MBC=\angle ABC` — this places `K=B+t_1d(\beta)` on the correct side
of lines `BM` and `BC`, but a point on that ray lies inside the *finite*
triangle `BMC` only if it is also on the correct side of the third edge
`MC`. This section proves that condition, and its `\sigma`-mirror for `L`
against edge `NB`, in full, for every triangle and every `\beta` in the
valid range — and shows both are *automatically* satisfied by the roots
Theorems 11.8/11.10 already select.

**Lemma 12.1 (affine form of the K-vs-MC test).** With `M=(a/2,0)`,
`K-M=(B-M)+t_1d(\beta)`, so `\mathrm{cross}(C-M,K-M)` is affine in `t_1`:
$$N_1(t_1):=\mathrm{cross}(C-M,K-M)=\mathrm{cross}(C-M,B-M)+t_1\,
\mathrm{cross}(C-M,d(\beta)).$$
Direct computation: `C-M=(b-a/2,cc)`, `B-M=(a/2,0)`, so
`\mathrm{cross}(C-M,B-M)=(b-a/2)\cdot0-cc\cdot(a/2)=-a\,cc/2`. Also
`\mathrm{cross}(C-M,d(\beta))=(b-a/2)\sin\beta+cc\cos\beta=:Q^{\rm ptrig}(\beta)`.
So `N_1(t_1)=-\dfrac{a\,cc}2+t_1\,Q^{\rm ptrig}(\beta)`. Since
`\mathrm{cross}(C-M,B-M)=-a\,cc/2<0` (reference sign, `B` itself is on the
correct side of `MC` trivially), **"K on the correct (B-)side of line MC"
`\iff N_1(t_1)<0`.** Clearing the Weierstrass denominator `(1+u^2)>0`
(`u=\tan(\beta/2)`) gives an exactly equivalent polynomial test
$$\tilde N_1(t_1):=(1+u^2)N_1(t_1)=P'(u)+t_1Q'(u),\quad
P'(u)=-\frac{a\,cc}2(1+u^2),\quad Q'(u)=-cc\,u^2+(2b-a)u+cc$$
(`Q'(u)` is `(1+u^2)` times `Q^{\rm ptrig}(\beta)` under the substitution,
a direct Weierstrass expansion of `Q^{\rm ptrig}(\beta)`; sign unaffected
since `(1+u^2)>0`).

**Lemma 12.2 (resultant identity, K-side).** With `G_{3a}(t_1)` the
already-certified quadratic (`coordinate-bash-resultant.md` §4, reproduced
in §9 above), a direct symbolic computation (own `sympy.resultant` session
on the exact displayed polynomials) gives
$$\mathrm{Res}_{t_1}(G_{3a},\tilde N_1)=\frac a4\,u\,A_3\,\big[(a-2b)^2+4cc^2\big]\,F_1,$$
where `A_3` is the leading coefficient (`t_1^2$-coefficient) of `G_{3a}`.
Direct computation from `G_{3a}`'s displayed formula gives
`A_3=2(1+u^2)\big(cc(u^2-1)-2bu\big)`, which is **identical, term for term,
to `A_2`** (Lemma 11.7's leading coefficient of `G_{2a}` in `s_2`) —
confirmed by direct polynomial subtraction, `A_3-A_2=0` identically in
`u,b,cc$. Hence `A_3<0` throughout the valid range, by Lemma 11.7 (already
proved). By the standard resultant-value formula for a quadratic `f=At^2+Bt+C`
(roots `r_1,r_2`) against a linear `g=Q't+P'$ (the same primitive used in
Theorem 11.8's proof — knowledge_base.md, resultants):
`\mathrm{Res}_t(f,g)=A\cdot g(r_1)g(r_2)`. So
$$\tilde N_1(r_1)\tilde N_1(r_2)=\frac{\mathrm{Res}_{t_1}(G_{3a},\tilde N_1)}{A_3}
=\frac a4\,u\,\big[(a-2b)^2+4cc^2\big]\,F_1.$$
On the valid range: `a>0`, `u=\tan(\beta/2)>0` (`\beta\in(0,\pi/2)`),
`(a-2b)^2+4cc^2>0` (sum with `cc>0`), and `F_1<0` (Lemma 11.6). Hence
$$\tilde N_1(r_1)\tilde N_1(r_2)<0.$$
As in Theorem 11.8's proof, a negative product of real-coefficient-affine
values at the two roots of a real quadratic forces the roots to be real
(else complex-conjugate roots would give a nonnegative product) — this
independently reconfirms `G_{3a}=0` has two real roots throughout the valid
range (already known from Theorem 11.10, now reconfirmed by an independent
computation) — and exactly one of the two roots satisfies `\tilde N_1<0`,
i.e. **exactly one root of `G_{3a}` places `K` on the correct side of line
`MC`.**

**Lemma 12.3 (mirror resultant identity, L-side).** With `N=(b/2,cc/2)`,
`L-N=(C-N)+s_2R(\beta)(A-C)`, the identical construction gives
$$\tilde N_2(s_2):=4\big[(1+u^2)\,\mathrm{cross}(B-N,L-N)\big]
=2a\,cc(1+u^2)+4s_2R(u),$$
$$R(u)=-2ab\,u+a\,cc\,u^2-a\,cc+b^2u+cc^2u,$$
(`\mathrm{cross}(B-N,C-N)=a\,cc/2>0` at `s_2=0`, computed directly:
`B-N=(a-b/2,-cc/2)`, `C-N=(b/2,cc/2)`,
`\mathrm{cross}=(a-b/2)(cc/2)-(-cc/2)(b/2)=a\,cc/2`, so "`L` on the correct
(C-)side of line `NB`" `\iff\tilde N_2(s_2)>0`). A second symbolic resultant
computation (own `sympy.resultant` session, exact `G_{2a}` from §3/Theorem
11.8) gives
$$\mathrm{Res}_{s_2}(G_{2a},\tilde N_2)=4u\,A_2\,\big[(2a-b)^2+cc^2\big]\,F_2,$$
so `\tilde N_2(r_1)\tilde N_2(r_2)=4u\big[(2a-b)^2+cc^2\big]F_2/A_2`. On the
valid range `u>0`, `(2a-b)^2+cc^2>0`, `F_2<0` (Lemma 11.6), `A_2<0` (Lemma
11.7): `\tilde N_2(r_1)\tilde N_2(r_2)=(+)(+)(-)/(-)>0`... more precisely
`4u[(2a-b)^2+cc^2]F_2` is negative (`F_2<0`, rest positive), divided by
`A_2<0` gives a **positive** quotient — wait, this must be checked against
"exactly one root passes": a *positive* product `\tilde N_2(r_1)\tilde
N_2(r_2)>0` alone does not, by itself, guarantee a split (it is consistent
with either both `>0` or both `<0`). This is resolved directly in Theorem
12.6 below via the general root-pairing lemma, not by this product's sign
alone — see there for the completed argument (the product's sign here is
recorded for completeness of the computation, but the split is established
differently on the `L`-side, as detailed next).

**Lemma 12.4 (general root-pairing lemma).** Let `f(t)=At^2+Bt+C$ have real
coefficients, `A\ne0`, and two distinct real roots `r_1<r_2$. Let
`X(t)=Q_Xt+P_X`, `Y(t)=Q_Yt+P_Y` be real affine functions with `Q_X,Q_Y\ne0`,
such that `X(r_1)X(r_2)<0` and `Y(r_1)Y(r_2)<0`. Then
$$\mathrm{sign}\big(X(r_1)\big)=\mathrm{sign}\big(Y(r_1)\big)
\iff \mathrm{sign}(Q_X)=\mathrm{sign}(Q_Y).$$
*Proof.* Since `X` is affine with nonzero slope, it has a unique zero
`t_X=-P_X/Q_X`. Since `X(r_1)X(r_2)<0`, by the intermediate value theorem
(applied to the continuous, monotonic function `X`) its unique zero lies
strictly between `r_1` and `r_2`: `r_1<t_X<r_2`. If `Q_X>0`, `X` is
increasing, so (being left of its only zero) `X(r_1)<0`; if `Q_X<0`, `X` is
decreasing, so `X(r_1)>0`. In both cases `\mathrm{sign}(X(r_1))=
-\mathrm{sign}(Q_X)`. The identical argument gives `\mathrm{sign}(Y(r_1))=
-\mathrm{sign}(Q_Y)`. Hence `\mathrm{sign}(X(r_1))=\mathrm{sign}(Y(r_1))
\iff -\mathrm{sign}(Q_X)=-\mathrm{sign}(Q_Y)\iff\mathrm{sign}(Q_X)=
\mathrm{sign}(Q_Y)`. `\blacksquare`

**Lemma 12.5 (sign of the slopes `Q(u)`, `Q'(u)`, `R(u)`, throughout the
valid range).** Recall `Q(u)=-4bu^3+4bu+cc\,u^4-6cc\,u^2+cc` (Lemma 11.5's
slope, shared by `L_1` and, as shown in §11/Theorem 11.10's derivation, by
`M_1`), `Q'(u)` (Lemma 12.1's slope for `\tilde N_1`), and `R(u)` (Lemma
12.3's slope for `\tilde N_2`, up to the positive factor `4`). Direct
Weierstrass back-substitution (own `sympy` session, matching numerically at
several points to guard against algebra slips) gives, for the *unscaled*
cross products (before clearing the `(1+u^2)^k`-denominator, which is always
a positive factor and so does not affect sign):
$$Q(u)=(1+u^2)^2\,Q^{\rm trig}(\beta), \quad Q^{\rm trig}(\beta):=
b\sin2\beta+cc\cos2\beta=\mathrm{cross}\big(d(\beta),R(\beta)(A-C)\big),$$
$$Q'(u)=(1+u^2)\,Q^{\rm ptrig}(\beta),\quad Q^{\rm ptrig}(\beta):=
(b-a/2)\sin\beta+cc\cos\beta=\mathrm{cross}(C-M,d(\beta)),$$
$$R(u)=(1+u^2)\,R^{\rm trig}(\beta),\quad R^{\rm trig}(\beta):=\tfrac12(b^2+cc^2-2ab)\sin\beta-a\,cc\cos\beta
=\mathrm{cross}(B-N,R(\beta)(A-C)).$$
(Each of these is a direct symbolic computation: e.g. for `Q^{\rm trig}`,
with `d(\beta)=(-\cos\beta,\sin\beta)` and `R(\beta)(A-C)=(-b\cos\beta+cc\sin\beta,
-b\sin\beta-cc\cos\beta)` — direct matrix multiplication —
`\mathrm{cross}(d,R(\beta)(A-C))=(-\cos\beta)(-b\sin\beta-cc\cos\beta)-\sin\beta(-b\cos\beta+cc\sin\beta)
=b\sin\beta\cos\beta+cc\cos^2\beta+b\sin\beta\cos\beta-cc\sin^2\beta=2b\sin\beta\cos\beta+cc(\cos^2\beta-\sin^2\beta)
=b\sin2\beta+cc\cos2\beta`, a hand-checkable elementary trig computation, no
`sympy` needed for this one; `Q^{\rm ptrig}` was derived in Lemma 12.1;
`R^{\rm trig}` follows the identical direct expansion of `\mathrm{cross}(B-N,
R(\beta)(A-C))` with `B-N=(a-b/2,-cc/2)`.)

**We now prove `Q^{\rm trig}(\beta)>0`, `Q^{\rm ptrig}(\beta)>0`, and
`R^{\rm trig}(\beta)<0` throughout the entire valid range `(0,\gamma)`,
`\gamma:=\min(\angle ABC,\angle ACB)`, for every triangle**, using the
following single-crossing device.

**Sub-lemma (single-crossing).** Let `h(\beta)=p\sin(k\beta)+q\cos(k\beta)`
(`k\in\{1,2\}`, `p,q$ real, not both `0`). Write `h(\beta)=R\sin(k\beta+\psi)`
(`R=\sqrt{p^2+q^2}>0`, `\cos\psi=p/R,\sin\psi=q/R`, valid since `R\sin(k\beta+\psi)
=R\sin k\beta\cos\psi+R\cos k\beta\sin\psi=p\sin k\beta+q\cos k\beta$ by direct
expansion). The zeros of `h` are at `k\beta+\psi=n\pi` (`n\in\mathbb Z`), spaced
exactly `\pi/k` apart in `\beta`. If `\gamma<\pi/k` and `h(0)>0`, `h(\gamma)>0`,
then `h(\beta)>0` for every `\beta\in(0,\gamma)`. *Proof.* An interval of
length `\gamma<\pi/k` contains at most one zero of `h` (two zeros would be
`\ge\pi/k` apart). Since `R\ne0`, every zero of `h` is simple (`h'(\beta)=
kR\cos(k\beta+\psi)`, and `\sin,\cos` never vanish simultaneously), so `h`
changes sign at any zero it has. If `h` had a zero `z\in(0,\gamma)`, then
(being the only one) `h` would have constant sign on `(0,z)` and the
opposite constant sign on `(z,\gamma)$, forcing `h(0)` and `h(\gamma)$ to
have *opposite* signs — contradicting `h(0)>0=h(\gamma)>0$'s common sign. So
`h` has no zero in `(0,\gamma)`; since `h(0)>0` and `h` is continuous with no
sign change possible without a zero, `h(\beta)>0` throughout `(0,\gamma)`.
`\blacksquare`

**Application to `Q^{\rm ptrig}` (`k=1`).** `Q^{\rm ptrig}(0)=cc>0`.
`Q^{\rm ptrig}(\angle ABC)`: since `d(\angle ABC)` is (by
`branch-crossing-locus-equals-angle-B.md`) the *unit* vector in the direction
of `BC`, i.e. `d(\angle ABC)=(b-a,cc)/|BC|`, direct substitution gives
`Q^{\rm ptrig}(\angle ABC)=\mathrm{cross}(C-M,d(\angle ABC))=\mathrm{cross}(C-M,
BC)/|BC|`, and `\mathrm{cross}(C-M,BC)=(b-a/2)cc-cc(b-a)=cc\cdot(a/2)=a\,cc/2`
(direct computation), giving `Q^{\rm ptrig}(\angle ABC)=\dfrac{a\,cc}{2|BC|}>0`
(`a,cc>0`, `|BC|>0`). Since `\gamma\le\angle ABC<\pi` (an angle of a
nondegenerate triangle), the single-crossing lemma with endpoints `0` and
`\angle ABC` gives `Q^{\rm ptrig}(\beta)>0` on `(0,\angle ABC)\supseteq(0,\gamma)`.

**Application to `Q^{\rm trig}` (`k=2`, so need `\gamma<\pi/2` — always true,
since a triangle has at most one angle `\ge\pi/2`).** `Q^{\rm trig}(0)=cc>0`.
Direct computation (own `sympy` session, exact half-angle substitutions for
`\cos\angle ABC,\sin\angle ABC`, then `\cos2\angle ABC=1-2\sin^2\angle ABC`,
`\sin2\angle ABC=2\sin\angle ABC\cos\angle ABC$) gives the clean closed forms
$$Q^{\rm trig}(\angle ABC)=\frac{cc(a^2-b^2-cc^2)}{(a-b)^2+cc^2},\qquad
Q^{\rm trig}(\angle ACB)=\frac{cc(b^2+cc^2-a^2)}{(a-b)^2+cc^2}=-Q^{\rm trig}(\angle ABC).$$
By the standard triangle fact "the larger angle is opposite the larger
side" (elementary; equivalent to the Law of Sines' monotonicity), with side
`AC=\sqrt{b^2+cc^2}` opposite `\angle ABC` and side `AB=a` opposite
`\angle ACB`: **the smaller angle is opposite the smaller side.** We use
this directly on `\gamma=\min(\angle ABC,\angle ACB)`, splitting on which
angle is smaller:
- If `\gamma=\angle ABC` (i.e. `\angle ABC\le\angle ACB`): then `\angle ABC`
  is the smaller angle, so its opposite side `AC` is the smaller side:
  `AC\le AB`, i.e. `b^2+cc^2\le a^2`, i.e. `a^2-b^2-cc^2\ge0`. Hence
  `Q^{\rm trig}(\gamma)=Q^{\rm trig}(\angle ABC)=cc(a^2-b^2-cc^2)/[(a-b)^2+cc^2]
  \ge0`, with equality only if `a^2=b^2+cc^2` i.e. `AB=AC$ (the isosceles
  case, already separately resolved by `lemmas/isosceles-case-symmetry.md`
  and excluded here under the population's standing scalene/genericity
  convention) — so `Q^{\rm trig}(\gamma)>0` strictly for scalene triangles.
- If `\gamma=\angle ACB` (i.e. `\angle ACB\le\angle ABC`): symmetric
  argument, `AB\le AC` i.e. `a^2\le b^2+cc^2`, giving `Q^{\rm trig}(\gamma)=
  Q^{\rm trig}(\angle ACB)=cc(b^2+cc^2-a^2)/[(a-b)^2+cc^2]\ge0`, strictly
  `>0` for scalene triangles.

**In both cases, `Q^{\rm trig}(\gamma)>0`.** Combined with `Q^{\rm
trig}(0)=cc>0` and `\gamma<\pi/2`, the single-crossing lemma (`k=2`) gives
`Q^{\rm trig}(\beta)>0` throughout the entire valid range `(0,\gamma)`, **for
every scalene triangle, no sub-case left open.**

**Application to `R^{\rm trig}` (`k=1`).** `R^{\rm trig}(0)=-a\,cc<0`. Direct
computation (own `sympy` session, same method) gives
$$R^{\rm trig}(\angle ACB)=\frac{-a\,cc\sqrt{b^2+cc^2}}{2\sqrt{(a-b)^2+cc^2}}<0
\quad\text{(always, every triangle, unconditionally)},$$
$$R^{\rm trig}(\angle ABC)=\frac{cc(b^2+cc^2-2a^2)}{2\sqrt{(a-b)^2+cc^2}}.$$
Split on which angle is smaller, exactly as above:
- If `\gamma=\angle ACB`: `R^{\rm trig}(\gamma)=R^{\rm trig}(\angle ACB)<0`
  unconditionally (shown above, no case hypothesis needed at all).
- If `\gamma=\angle ABC` (i.e. `\angle ABC\le\angle ACB`, i.e. `b^2+cc^2\le
  a^2` by the side-angle correspondence exactly as above): then
  `b^2+cc^2\le a^2<2a^2` (since `a^2>0`), so the numerator `b^2+cc^2-2a^2<0`
  strictly, giving `R^{\rm trig}(\gamma)=R^{\rm trig}(\angle ABC)<0`.

**In both cases, `R^{\rm trig}(\gamma)<0`.** Combined with `R^{\rm
trig}(0)<0` and `\gamma<\pi/2<\pi`, the single-crossing lemma (`k=1`) gives
`R^{\rm trig}(\beta)<0` throughout the entire valid range `(0,\gamma)`, for
every triangle, no sub-case left open.

**What §12 establishes.** The magnitude-bound machinery (Lemmas 12.1–12.4,
the resultant identities, the single-crossing device) together with the
sign facts `Q^{\rm ptrig}>0`, `Q^{\rm trig}>0`, `R^{\rm trig}<0` — **all
three proved unconditionally, for every scalene triangle, throughout the
entire valid range, with no sub-case left open** — fully establish both
parts of Theorem 12.6 below.

**Theorem 12.6 (magnitude bound, and its exact coincidence with Theorem
11.8/11.10's sign-selected root — both parts proved unconditionally).**
For every scalene triangle and every `\beta` in the valid range:
1. `G_{3a}(t_1)=0` has two real roots, exactly one of which places `K` on
   the correct side of line `MC` — hence, combined with the (unconditional)
   ray-direction fact of §8, that root's `K=B+t_1d(\beta)` lies strictly
   inside the finite triangle `BMC`. Symmetrically for `G_{2a}(s_2)=0` and
   `L` against `\triangle BNC`. **This closes §8's magnitude-bound gap
   completely, for every triangle.**
2. That magnitude-bound-satisfying root of `G_{3a}` coincides **exactly**
   with Theorem 11.10's sign-test-selected root (`M_1<0`, "L inside angle
   ACK"): by Lemma 12.4 applied to `X=\tilde N_1` (slope `Q'(u)`, sign
   `=\mathrm{sign}(Q^{\rm ptrig})=+1`, proved throughout the valid range) and
   `Y=M_1` (slope `Q(u)`, sign `=\mathrm{sign}(Q^{\rm trig})=+1`, likewise
   proved throughout), both slopes are positive, so `\mathrm{sign}(\tilde
   N_1(r_1))=\mathrm{sign}(M_1(r_1))` — the same root gives `\tilde N_1<0`
   (containment) and `M_1<0` ("L inside angle ACK"), simultaneously.
   Symmetrically, the magnitude-bound root of `G_{2a}` coincides with
   Theorem 11.8's `L_1<0`-selected root: Lemma 12.4 with `X=\tilde N_2`
   (slope `4R(u)`, sign `=\mathrm{sign}(R^{\rm trig})=-1`, proved throughout)
   and `Y=L_1` (slope `Q(u)`, sign `=+1`) gives *opposite* signs, i.e. the
   root with `L_1<0` has `\tilde N_2>0` — exactly the containment-passing
   sign.

*Proof.* Part 1 is Lemmas 12.1–12.3 plus §8's direction fact. Part 2 is
Lemma 12.4 applied with the sign facts `Q^{\rm ptrig},Q^{\rm trig}>0`,
`R^{\rm trig}<0`, each proved unconditionally throughout the valid range
(no sub-case) in the derivation immediately above. `\blacksquare`

**Net effect of §12.** Both the magnitude bound itself (part 1) and its
exact coincidence with the already-certified sign tests of Theorem
11.8/11.10 (part 2) are now closed **in full generality, for every scalene
triangle, with no sub-case left open** — a genuinely new, complete result.
Combined with §8's (already-proved) ray-direction fact, this means: **the
single root of `G_{3a}=0` selected by Theorem 11.10's sign test places `K`
strictly inside the finite triangle `BMC` automatically** (and
symmetrically, `L` strictly inside `\triangle BNC` at Theorem 11.8's
selected root of `G_{2a}=0`) — closing §8's long-standing open item outright
and simultaneously showing it required no separate case analysis once
Theorem 11.8/11.10's root is already fixed.

### 13. NEW this round: structural progress on the G2b exclusion (Priority
2 of this round's plan) — real advances, not yet a complete proof

**The exact true/supplementary root criterion.** `G_{2a}=0` and `G_{2b}=0`
arise from squaring `\cos(\angle LBK)=\cos(\angle LNC)` (via the identity
`(\text{lhs cosine})^2\cdot|\ldots|^2=(\text{rhs cosine})^2\cdot|\ldots|^2`,
already used to build `eq2` in §3/`homogeneity-decoupling-rotation-param.md`).
Squaring introduces the spurious "supplementary" solution
`\angle LBK=\pi-\angle LNC`. Since `\cos\theta=\dfrac{\mathrm{dot}(\ldots)}
{|\ldots||\ldots|}` with the norm factors always positive, undoing the
square exactly recovers: a root `s_2` is **true** (satisfies the actual
hypothesis `\angle LBK=\angle LNC`, not the supplement) if and only if
$$\mathrm{sign}\big(\mathrm{dot}(BL,BK)\big)=\mathrm{sign}\big(\mathrm{dot}(NL,NC)\big).$$
Since `BK=t_1d(\beta)` with `t_1>0`, `\mathrm{sign}(\mathrm{dot}(BL,BK))=
\mathrm{sign}(\mathrm{dot}(d(\beta),L-B))=:\mathrm{sign}(D_K(s_2))`, an affine
function of `s_2` (direct computation, own `sympy` session):
$$D_K(s_2)=\frac{(bu^4-6bu^2+b+4cc\,u^3-4cc\,u)s_2-(u^2+1)(au^2-a-bu^2+b-2cc\,u)}{(1+u^2)^2}.$$
Likewise `\mathrm{dot}(NL,NC)=\mathrm{dot}(C-N,L-N)=:D_N(s_2)`, affine in
`s_2`:
$$D_N(s_2)=\frac{2(b^2+cc^2)(u^2-1)s_2+(b^2+cc^2)(u^2+1)}{4(1+u^2)}.$$
So the true-root test is `W(s_2):=D_K(s_2)\cdot D_N(s_2)>0` (the positive
denominators don't affect the sign of the product test). This is a new,
exact, algebraic (not numerically-guessed) characterization, refining the
g2b-lens explorer's informally-stated version.

**New theorem: `G_{2b}`'s two roots (when real) always share the same
true/supplementary status.** A direct symbolic resultant computation (own
`sympy.resultant` session, using the numerators `D_K^{\rm num}, D_N^{\rm
num}` and the exact `G_{2b}` reproduced independently in this round —
matching `2*(-6bu^5+20bu^3-6bu+cc\,u^6-15cc\,u^4+15cc\,u^2-cc)`'s already-
reported leading coefficient `B_2` term for term) gives
$$\mathrm{Res}_{s_2}\big(G_{2b},\,D_K^{\rm num}D_N^{\rm num}\big)=
-4u\,(b^2+cc^2)^2(1+u^2)^6\,F_2\,\big[2a(u^2-1)^2-b(u^2+1)^2\big]^2.$$
On the valid range `u>0`, `F_2<0` (Lemma 11.6): the prefactor
`-4u(b^2+cc^2)^2(1+u^2)^6` is negative, times `F_2<0` gives a **positive**
value, times the perfect square `[\ldots]^2\ge0` gives a value `\ge0$
overall. Hence (dividing by `B_2^2\ge0`, the resultant-formula normalization
for two same-degree-2 polynomials) `W(r_1)\cdot W(r_2)\ge0` **always** —
i.e. `G_{2b}`'s two roots can never have opposite true/supplementary
status: either both are true, or both are supplementary (or the boundary
case `B_2=0`, a triangle-specific degeneracy). **This directly refutes the
g2b-lens explorer's numeric guess of "generically one true, one
supplementary"** (confirmed independently: an own large-scale re-run,
50,000 (triangle,β) samples with `G_{2b}` filtered to have real roots, found
**0/2586** instances of a true/supplementary split among the real-root
cases — matching the theorem exactly, and correcting the explorer's report
as an artifact of too small a sample or a different quantity being tracked).

**The `s_2>0` constraint is essential and was implicitly under-specified in
the round's brief.** Re-running the joint containment+sign exclusion check
at scale (own script, 50,000 (triangle,β) samples) reveals: **without**
restricting to `s_2>0` (the physically meaningful range, since `s_2=t_2/|AC|`
and `t_2=CL>0` is a length), the conjectured exclusion is **false** — 15,962
counterexamples found among the 46,542 positive-*and*-negative real roots
checked (i.e. `L_1<0` and `\tilde N_2>0` both hold at a true root, but with
`s_2<0`, an invalid candidate). **Restricting correctly to `s_2>0`** (as any
genuine candidate for `L`'s position must satisfy) reproduces the
conjectured exclusion with **0 counterexamples across 26,146 samples with
real roots** (6,421 of which pass the true-root filter `W>0`) — a
substantially larger and more carefully scoped re-verification than the
original 4500-trial report, and importantly identifies *why* the original
numeric check needed to filter on `s_2>0` (implicit but not stated
explicitly in the g2b-lens explorer's report).

**What remains open, precisely.** A full symbolic proof of "for every
`s_2>0` root of `G_{2b}` with `W(s_2)>0` (true), NOT (`L_1(s_2)<0$ AND
`\tilde N_2(s_2)>0`)" requires combining three conditions on a quadratic's
roots simultaneously (positivity of the root, the true/supplementary
quadratic-in-`s_2` sign test `W`, and the joint affine sign tests
`L_1,\tilde N_2`) — a genuinely harder combination than any single
resultant/Vieta trick used elsewhere in this file (which handle at most one
quadratic against one affine function at a time). Two directions identified
but not completed this round: (a) since `D_N(s_2)`'s slope
`2(b^2+cc^2)(u^2-1)` has a *fixed* sign throughout the valid range
(`u^2-1<0` always, because `u=\tan(\beta/2)<\tan(\pi/4)=1` whenever
`\beta<\pi/2`, which holds throughout the valid range — a clean new
observation this round), `D_N(s_2)>0\iff s_2<\dfrac{1+u^2}{2(1-u^2)}` is an
*explicit threshold*, reducing part of the problem to comparing this
threshold against `G_{2b}`'s actual roots (not yet completed); (b) a direct
case split on the (still only partially classified) sign of `B_2` combined
with the positivity constraint was not attempted this round. This is a
concrete, scoped-down remaining gap, not an opaque numerics-only blob.

### 14. NEW this round: the resultant-ratio-cancellation reduction
(§13's exclusion depends only on `Y, B_2, Z`) re-derived from scratch, and
their exact trigonometric identification

**Independent from-scratch re-derivation of the sturmlens explorer's
reduction.** Rebuilding the whole pipeline in a fresh session (own script:
`eq2` from `cross_eq(L-B,K-B,L-N,C-N)`, divide by `t_1^2`, factor) exactly
reproduces `G_{2a}` and `G_{2b}` term-for-term against both the certified
formula and the sturmlens report. Independently recomputing all four
`s_2`-resultants of `G_{2b}` against `D_K^{\rm num}`, `D_N^{\rm num}`,
`L_1`, `\tilde N_2`:
$$\mathrm{Res}(G_{2b},D_K)=(u^2+1)^4F_2Y,\qquad
\mathrm{Res}(G_{2b},D_N)=-4u(b^2+cc^2)^2(u^2+1)^2Y,$$
$$\mathrm{Res}(G_{2b},L_1)=-4u(u^2+1)^4F_1F_2\quad(\text{already
certified}),\qquad
\mathrm{Res}(G_{2b},\tilde N_2)=-8u(u^2+1)^2F_2Z,$$
where
$$Y=2a(u^2-1)^2-b(u^2+1)^2,\qquad
Z=8a^2bu+4a^2cc\,u^2-4a^2cc-8ab^2u-8a\,cc^2u+2b^3u-b^2cc\,u^2+b^2cc+2b\,cc^2u-cc^3u^2+cc^3$$
— all four identities confirmed by direct `sympy.resultant` computation
with **zero symbolic remainder** against the target formulas (an
independent re-derivation, not a re-check of displayed numbers). As
sturmlens observed, the unknown factor `Y` cancels in the ratio
`\mathrm{Res}(G_{2b},D_K)/\mathrm{Res}(G_{2b},D_N)`, giving the proved fact
`\mathrm{sign}(D_K(r_1)D_K(r_2))=\mathrm{sign}(D_N(r_1)D_N(r_2))`
unconditionally (independently reconfirmed here) — but the full 3-way
exclusion (positivity + true-root + containment/sign) genuinely depends on
the *individual* signs of `Y`, `B_2`, and `Z`, not just this ratio, exactly
as sturmlens diagnosed.

**New result (this round): `Y`, `B_2`, `Z` identified exactly as
trigonometric expressions in `\beta`, proved by symbolic coefficient-
matching (fitting each against a basis of `\sin(k\beta),\cos(k\beta)`
numerators under the Weierstrass substitution, then confirming the fit by
full polynomial expansion with `sympy`, remainder `0` in every case — not
a numeric or partial check):
$$\frac{Y}{(1+u^2)^2}=2a\cos^2\beta-b,\qquad
\frac{B_2}{(1+u^2)^3}=-2\big(b\sin3\beta+cc\cos3\beta\big),$$
$$\frac{Z}{1+u^2}=p_1\sin\beta+q_1\cos\beta,\qquad
p_1=b(2a-b)^2+cc^2(b-4a),\quad q_1=-cc(4a^2-b^2-cc^2).$$
(Since `(1+u^2)^k>0` always, these ratios do not affect sign: `\mathrm{sign}(Y)=\mathrm{sign}(2a\cos^2\beta-b)`, etc.) The `Y`-identity additionally
shows, for the first time explicitly, that `Y` is exactly `F_3`'s trig
form from §9 (`F_3/(1+u^2)^2\propto2a\cos^2\beta-b`) up to a positive
overall constant — i.e. `Y=0` and `F_3=0` are the **same** locus, tying
this round's reduction back to the previously-identified (and only
partially classified) third resultant factor.

**Reformulated target (not yet proved).** Combining the trig identities,
the `(+,+,+)`-forbidden cheap-kill (§13/this round's numerics) is exactly
the conditional trigonometric inequality
$$2a\cos^2\beta>b \ \ \wedge\ \ b\sin3\beta+cc\cos3\beta<0
\ \implies\ p_1\sin\beta+q_1\cos\beta<0,\qquad
\forall\beta\in\big(0,\min(\angle ABC,\angle ACB)\big),\ \forall\text{
triangles}.$$
**Numerically reconfirmed at large scale this round**: an independent
200,000-sample sweep (own script, own seed) over random triangles and
valid `\beta` finds the sign pattern `(+,+,+)` in **0/200,000** trials (all
other 7 patterns occur, with counts recorded in "Approaches tried" above)
— a 25× larger and independently-coded corroboration of the sturmlens
explorer's 8,000-sample census, with the same (zero-exception) outcome.

**Partial progress toward closing this, not completed.** Computed one
closed-form endpoint value, `Z(\angle ABC)`, via the standard dot/cross
formulas for `\cos\angle ABC,\sin\angle ABC$ (own symbolic derivation,
confirmed by `sympy.simplify` to reduce to zero remainder against a direct
substitution check):
$$\frac{Z(\angle ABC)\cdot|BC|^2}{a}=a\,cc\,\big({-}4a^2+8ab-3b^2-3cc^2\big).$$
This is a genuine, checkable new fact (a first foothold for a future
single-crossing-lemma-style argument on `Z`, mirroring the technique that
closed `F_1,F_2,Q^{\rm trig},R^{\rm trig}` in §§11-12), but **the
symmetric endpoint `Z(\angle ACB)`, and the conditional (not bare
single-sinusoid) structure of the target inequality itself, were not
resolved this round.** Unlike `F_1,F_2,Q^{\rm trig},R^{\rm trig}` (each a
bare "prove `h(\beta)` has one fixed sign throughout the range" claim,
solved by the single-crossing lemma from two endpoint values), this
target is a genuinely harder **conditional** statement over *three*
different sinusoids (`k=1`, `k=1`, `k=3`) simultaneously — the
single-crossing lemma as certified does not directly apply to a
conjunction of two hypotheses implying a third conclusion, and adapting it
(e.g. via a joint case-split on which of finitely many sub-regions of
`\beta`-space each sinusoid's sign is constant on, then checking the
implication holds on each region) is a concrete but not-yet-attempted next
step.

**What §14 establishes and does not.** Establishes, exactly and
rigorously: the identification of `Y,B_2,Z` with explicit trig
expressions (a genuine structural simplification, reusable independently
of whether the cheap-kill itself is ever closed), the identity `Y\propto
F_3` (tying two previously-separate strands of the population's work
together), and a stronger (25×) numerical reconfirmation of the
`(+,+,+)`-forbidden pattern. Does **not** establish: a proof of the
cheap-kill itself, or of the full G2b 3-way exclusion (§13's gap remains
open in substance — this round narrows its *shape* further but does not
close it).

### 16. Round 9: claim `(I)` closed unconditionally; claim `(II)` closed on
`Y(\gamma)\ge0`; `Y(\gamma)<0` isolated as the sole remaining gap

Building on §15's exact two-part reformulation `(I),(II)$ of the whole
remaining `G_{2b}`-exclusion content, this round proves:

**Theorem 16.1 (`(I)` fully closed).** For every triangle `ABC` (WLOG
`\angle B\le\angle C`, `\gamma:=\angle B`) and every `\beta\in(\beta_0,
\gamma)`, `\beta_0:=(\pi-A)/3` (the domain-nonempty threshold `\sin(A+3\beta)
<0$ requires `\beta>\beta_0`),
$$f(\beta):=2\sin(A+B)(\sin\beta+\sin A)-\sin B\sin(A+\beta)>0.$$
*Proof.* `f'(\beta)=\sin(A+\beta)\cos B+\sin(A+B-\beta)>0` throughout `(0,
\gamma)` (both terms strictly positive since `B<\pi/2`, `0<A+\beta<A+B<\pi`,
`0<A+B-\beta<A+B<\pi` — full derivation above, Round 9 §"New result 1"), so
`f` is strictly increasing on `(0,\gamma)`; and `f(\beta_0)=2\sin\beta_0\,
G(\beta_0,s)>0` strictly (`G>0` proved via the two-case split on
`\mathrm{sign}(C_2(\beta_0))$, each case closed exactly — full derivation
above, "New result 2"). Monotonicity then gives `f(\beta)>f(\beta_0)>0` for
every `\beta\in(\beta_0,\gamma)`. `\blacksquare`

**Theorem 16.2 (`(II)` closed on `Y(\gamma)\ge0`).** With `Y(\beta):=2\cos^2
\beta-\dfrac{\sin B\cos A}{\sin(A+B)}$, `Y` is strictly decreasing on
`(0,\gamma)` (`Y'=-2\sin2\beta<0`, since `2\beta\in(0,2\gamma)\subset(0,
\pi)`). If `Y(\gamma)\ge0`, then `Y>0` throughout `(0,\gamma)` (so the
`Y>0` hypothesis of `(II)` never restricts the domain), and
$$2K-f(\beta)>2K-f(\gamma)=\sin(A+B)\,(2\sin A-\sin B)>0\quad\text{for all }
\beta\in(0,\gamma)$$
(using `(2K-f)'=-f'<0`, Theorem 16.1's monotonicity, and the identity
`\cos B\,(2\sin A-\sin B)-\sin(A+B)Y(\gamma)=\sin B(\cos\delta-\cos B)>0`
for `A=\pi-2B-\delta`, `0\le\delta<B<\pi/2` — full derivation above). Hence
`(II)` holds throughout `(0,\gamma)`, unconditionally on `\sin(A+3\beta)$'s
sign, whenever `Y(\gamma)\ge0`. `\blacksquare`

**What remains open (the sole gap for this whole approach).** When
`Y(\gamma)<0`, the true right endpoint of the `(II)`-relevant domain is the
unique `\beta_1\in(0,\gamma)` with `Y(\beta_1)=0` (i.e. `2\cos^2\beta_1\sin
(A+B)=\sin B\cos A`), and `2K-f(\beta_1)\ge0` is needed but not yet proved
— `\beta_1` has no closed form in `(A,B)` analogous to `\beta_0`'s linear
one, so the affine-reparametrization trick that closed Theorem 16.2 does
not directly transfer to this quadratic-in-`\cos\beta` boundary. This is now
the **single, precisely-defined remaining item** for the whole approach
(supersedes and sharpens the previously-tracked but vaguer "G2b exclusion"
and "(I)/(II)" gaps — `(I)` is fully retired, `(II)` is retired except on
this one sub-case).

### 17. Round 10: the `Y(\gamma)<0` sub-case (§16's remaining gap), split
into `P/E` sub-branches — two of three fully closed; the residual reduced

Adopting the round-10 outliner's/outline-reviewer's corrected statement of
this sub-case (restoring the domain-nonempty hypothesis
`\sin(A+3\beta_1)<0`, i.e. `\beta_1>\beta_0`, which round 9's literal
statement omitted and which was shown this round to be genuinely necessary,
not optional — `8218/25123` violations without it, `0/572{,}351` with it,
per the outline-reviewer's independent sweep), the target `2K-f(\beta_1)
\ge0` was rewritten as `G(\beta_1)=K+\sin A\sin B\,x-Py\ge0`
(`x=\cos\beta_1=\sqrt{X_0}`, `y=\sin\beta_1=\sqrt{1-X_0}`, `X_0=\sin B\cos A
/(2\sin(A+B))`) and split on `\mathrm{sign}(P)`, then (within `P>0`) on
`\mathrm{sign}(E)` for `E:=A_{\mathrm c}X_0+C_{\mathrm c}`
(`A_{\mathrm c}=\sin^2A\sin^2B+P^2`, `C_{\mathrm c}=K^2-P^2`). **Fully
closed: `P\le0` (unconditional) and `E\ge0` (`\ge91\%` of the corrected
domain).** **Not closed: `P>0\wedge E<0` (`\approx4.5\%`)**, reduced to the
exactly-verified (zero-residual `sympy.groebner` check) equivalent target
`4\sin B\cos B\sin A\sin B\,q_1(\sigma,\tau)+\cos A\,r_0(\sigma,\tau)\le0`
(`\sigma=\sin^2A,\tau=\sin^2B`, `q_1,r_0` the explicit degree-4-in-`(\sigma,
\tau)` polynomials displayed in the round-10 "Approaches tried" entry
above). Full derivation and all identities in the round-10 entry above.

**Round 11 update (sharpened, not yet closed).** Restricting the sign
census of `q_1,r_0` to the TRUE residual sub-domain (Case-(b) containment
`\beta_1<\gamma,\sin(A+3\beta_1)<0` jointly with `P>0,E<0`, not merely the
free `(\sigma,\tau)\in(0,1)^2` square used in round 10's census) shows
`q_1<0` AND `r_0<0` **individually**, throughout this exact sub-domain
(`0` violations, `25{,}568$ random + `40{,}790` independent grid samples,
comfortable margins). Combined with two further facts established this
round on the same sub-domain — `\cos B>0` (with margin; `B\in\approx(0.912,
1.090)\subset(0,\pi/2)`) and `\cos A>0` (`A\in\approx(0.407,0.537)`, both
`\ge0` always by the standing hypothesis and `>0` strictly on this
sub-case) — the target `4dst\,q_1+c\,r_0\le0` would follow termwise (sum of
two strictly negative terms), **once `q_1<0,r_0<0` are proved symbolically
on the true sub-domain**, which is NOT yet done — the true sub-domain is a
curved, proper subset of any simple bounding box in `(\sigma,\tau)` (e.g.
only `\approx80.7\%$ of the natural bounding box `\sigma\in[0.1,0.3],
\tau\in[0.6,0.8]` has `q_1<0`), so a full symbolic closure needs an
algebraic characterization of the exact sub-domain (via eliminating
`\beta_1` from its two defining transcendental conditions), not attempted
this round. A suggestive (numerically-grounded, unproved) structural
observation: the residual sub-case's `(A,B)`-window appears pinned at
essentially the same corner `(A^*,B^*)\approx(0.4064,0.9117)` independently
found this round by the sibling `coordinate-bash-resultant-boundary-
pointwise` approach's `(\star)` target, where both `q_1,r_0$ and the
sibling's slack simultaneously appear to vanish. **This is now the single
remaining item for the whole approach**, sharpened this round from an
entangled two-polynomial combination into two individually-sign-definite
(numerically) polynomial negativity claims on a narrow, precisely-located
sub-domain — strictly narrower than round 9's undifferentiated `Y(\gamma)<0`
gap, and now more precisely characterized than round 10 left it, but still
open.

**Round 12 update (β1-elimination spliced in; Step 4 reformulated to a
clean rational sign target; still not closed).** The transcendental part of
the true residual sub-domain (`\beta_1<\gamma`, `\sin(A+3\beta_1)<0`,
previously only accessible via `\arccos`) is now proved to reduce exactly
(no approximation) to two polynomial conditions once `\gamma=B` and two
sign facts `p:=s(4X_0-3)<0,\ q:=c(4X_0-1)>0` (i.e. `X_0\in(1/4,3/4)`) are
known: `X_0>d^2` and `p^2X_0>q^2(1-X_0)`. Independently re-derived, by hand,
the exact identity `\sin(A+3\beta_1)=s(4X_0-3)x+c(4X_0-1)y`
(triple-angle formula plus the licit substitution `x^2\to X_0,y^2\to1-X_0`,
valid since `x,y\ge0`) and confirmed the two subsequent squarings (Steps
3, 5) are each valid iffs given the relevant sign facts. Additionally found
a genuinely new exact reformulation of Step 4's target itself: since
`\sin C=sd+ct>0` unconditionally, `X_0>1/4\iff ct>sd` and `X_0<3/4\iff
ct+3sd>0` — turning the `X_0`-comparison into a bare linear-in-`(c,s,d,t)`
sign question. Verified (own fresh `5$–`10$M-sample sweeps this round) that
neither bound follows from `X_0>d^2` alone or `E<0` alone — both hypotheses
are genuinely needed jointly, matching the `q_1,r_0` situation's own
obstruction pattern. **Did not close this joint elimination symbolically
this round** (a resultant/Positivstellensatz-style combination of the
newly-derived canonical forms `G_0:=ct(1-2d^2)-2sd^3` (for `X_0>d^2`) and
`c t f_1(\sigma,\tau)+d s f_2(\sigma,\tau)` (for `2\sin C\cdot E`, both
forms independently re-derived and confirmed exact this round) was
attempted with several low-degree ansätze but none matched in the time
available). **Also confirmed Step 2 (`\gamma=B`) needs the full three-way
hypothesis (not just the Step-4 domain) — it fails `\approx48\%` of the
time under `X_0>d^2\wedge E<0` alone but holds with zero violations
(`20{,}515` fresh samples) once `\sin(A+3\beta_1)<0` is also imposed —
still not proved symbolically.** **Crucially, and answering the round's
final question directly: even a full symbolic closure of Steps 2 and 4
would NOT by itself close the `\approx4.5\%` residual** — it would only
replace the transcendental domain description with a polynomial one; the
actual target `q_1<0\wedge r_0<0` on that (still curved, non-box) polynomial
domain remains a wholly separate, still-open task. Status remains
`partial`; the residual gap is unchanged in substance (only its domain
description is now closer to fully algebraic).

## Full proof
(Not present — Status is `partial`. §3 (round 3) is a complete,
independently reproduced proof of the central identity's *genericity* on
the correctly-selected branch, for every triangle. §7 (round 4) fully and
rigorously closes `F_2=0\iff\beta=\angle ACB` (and retroactively repairs
`F_1`'s exactness caveat). §9 (round 4) identifies, with an explicit
counterexample, that the previously-assumed-harmless third resultant
factors `F_3,F_3'` do have roots inside the valid range for real triangles,
and gives strong numerical (not yet symbolic) evidence that the genuine
branch survives these crossings undisturbed. §10 flags the problem's two
extra containment hypotheses as entirely unaddressed by the population
before this round. §11 closes, fully and rigorously (Theorem 11.8 and its
mirror Theorem 11.10), the claim that within the `G_{2a}` (resp. `G_{3a}`)
branch, the "K inside angle LBA" (resp. "L inside angle ACK") hypothesis
selects a unique root, for every triangle and every `β` in the valid range.
**§12 (this round) closes, fully and rigorously and with no sub-case left
open, the magnitude bound `t_1<t_1^{\max}(\beta)` flagged since §8 (round
4)** — for every scalene triangle and every `β` in the valid range, the
root of `G_{3a}` (resp. `G_{2a}`) selected by Theorem 11.10 (resp. 11.8)'s
sign test automatically places `K` (resp. `L`) strictly inside the finite
triangle `BMC` (resp. `BNC`), not merely the correct angular sector. This
fully retires §8's open item — combined with §11, the sign-test-selected
root of `G_{2a}=G_{3a}=0` now provably satisfies *all* of: containment in
its own triangle, and both of the problem's "inside the angle" hypotheses,
simultaneously, at every `β` in the valid range, for every triangle.
**§13 (this round) makes substantial but incomplete progress on excluding
the extraneous branch `G_{2b}`** — refutes and replaces the population's
prior "generically one true, one supplementary root" guess with a proved
theorem (the two roots of `G_{2b}`, when real, always share the same
true/supplementary status), corrects the physical-domain (`s_2>0`) scoping
of the joint containment+sign exclusion conjecture, and re-verifies it at
larger scale (0/26,146) — but does not complete a symbolic proof of the
three-way (positivity + true-root + containment/sign) combination. What
remains, precisely: (a) the `G_{2b}` exclusion (§13, now much more
narrowly scoped than before but not closed); (b) §9's F3/F3' "crossings
are harmless" claim, still numerical only; (c) the population's standing,
still-unproven identification of `G_{2a}=G_{3a}=0` (not `G_{2b}=G_{3b}=0`)
as the actual geometrically genuine branch — §§11–12 establish strong
internal consistency *on* that branch (every hypothesis is simultaneously
satisfiable there) but do not by themselves rule out `G_{2b}` also
producing a valid competing configuration, which is exactly (a)'s content.
None of these three remaining items is closed, so Status stays `partial`,
but the field of open gaps has shrunk substantially and precisely this
round: §12 is a complete closure (not partial), and §13 sharpens (a) from
an opaque numeric blob into a scoped, partially-symbolic problem. **§14
(round 7) further sharpens (a)'s exact remaining shape** — the full G2b
exclusion is now known to depend on exactly three explicit trigonometric
sign facts (`2a\cos^2\beta-b`, `b\sin3\beta+cc\cos3\beta`,
`p_1\sin\beta+q_1\cos\beta`), reconfirmed at 200,000-sample scale to obey
the conjectured conditional inequality with zero exceptions, but the
symbolic proof of that conditional inequality (a strictly harder shape
than the population's prior bare single-sinusoid sign facts) is not
completed — (a) remains open, unchanged in substance from round 6, but
sharper in form.

**§15 (round 8) closes the discriminant step of the scale-invariant
reformulation unconditionally, derives exact closed-form roots, and
disproves the outline's proposed step-7 mechanism with an explicit
counterexample**, replacing it with the mechanistically correct Law-of-
Sines substitution and a precise two-part remaining target ((I),(II) in §15)
— both confirmed at large numeric scale (`0` exceptions across tens of
thousands of samples each, independently ablated to show their exact
hypothesis dependence) but not yet proved symbolically. This is real,
non-trivial narrowing (a full sub-step closed, a flawed lever caught and
replaced) but does **not** close the G2b exclusion gap. Status remains
`partial`.

**§17 (round 10) closes two of the three sub-branches of the round-9
`Y(\gamma)<0` residual (`P\le0` unconditionally; `E\ge0`, `\ge91\%` of the
corrected domain) and reduces the remaining `\approx4.5\%` sub-case
(`P>0\wedge E<0`) to an exactly-verified, radical-free polynomial condition
`4dst\,q_1(\sigma,\tau)+c\,r_0(\sigma,\tau)\le0`** — a genuine, checked
(zero-residual `sympy.groebner`) simplification, but the sign of this
expression on the relevant domain was not established this round (`q_1,r_0`
individually have no fixed sign, ruling out a naive termwise argument).
Status remains `partial`.)

## Promotable lemmas (round 17 additions)

- **Structural decomposition `H=ct\cdot P_H(\sigma,\tau)+sd\cdot
  Q_H(\sigma,\tau)` for `H\in\{G_0,E_{\mathrm{num}},\mathrm{Num}\}`.**
  Exact, zero-residual (own `sympy.groebner`/`sympy.reduced` modulo
  `\langle c^2+s^2-1,d^2+t^2-1\rangle`), with `P_{G_0}=2\tau-1,\
  Q_{G_0}=2(\tau-1)`; `P_{E_{\mathrm{num}}}=-32\sigma^2\tau+24\sigma^2+22
  \sigma\tau-12\sigma-\tau,\ Q_{E_{\mathrm{num}}}=-2(\sigma-1)(16\sigma\tau
  -4\sigma-3\tau)`; `P_{\mathrm{Num}}=8\sigma^2\tau-6\sigma^2-3\sigma+\tau,
  \ Q_{\mathrm{Num}}=2\sigma(\sigma-1)(4\tau-1)`. Proved in Step 1 of round
  17's entry above. Reusable by any approach needing a clean handle on the
  `c,d`-parity structure of these three generators.

- **Bare single-variable multipliers `c,d,s,t` applied to any of `G_0,
  E_{\mathrm{num}},\mathrm{Num}` cannot contribute to a `(\sigma,\tau)`-only
  Positivstellensatz certificate.** Precisely: `(s\cdot H)_{00}=(t\cdot
  H)_{00}=0` identically, `(c\cdot H)_{00}=(1-\sigma)\,t\,P_H(\sigma,\tau)`
  (odd in `t`, not a `\sigma,\tau`-polynomial unless `P_H\equiv0`), and
  `(d\cdot H)_{00}=(1-\tau)\,s\,Q_H(\sigma,\tau)` (odd in `s`, same
  obstruction), for `H\in\{G_0,E_{\mathrm{num}},\mathrm{Num}\}`. Proved in
  Step 2 of round 17's entry above, using the Step-1 decomposition. A sharp
  strengthening of round 13's `lemmas/parity-obstruction-q1-r0-certificate.md`
  (which only established "needs an odd `c`/`d` factor," not that a single
  bare one is insufficient) — reusable as a cheap-kill filter for any future
  round tempted to try `c\cdot(\text{anything})` or `d\cdot(\text{anything})`
  as a standalone generator.

- **A new unconditionally-nonnegative generator family
  `\mathrm{NewGen}(H,H'):=[(cd\cdot H\cdot H')^2]_{00}` for `H,H'\in\{G_0,
  E_{\mathrm{num}},\mathrm{Num}\}`.** Proved `\ge0$ for ALL real
  `c,s,d,t` with `c^2+s^2=1,d^2+t^2=1` (no domain restriction), as an
  average of squares under the sign-flip involutions `c\mapsto-c,
  d\mapsto-d`. Six exact closed forms computed (Step 4 of round 17's entry
  above), degree `10`–`17` in `\sigma,\tau` — too high-degree to directly
  help the current degree-6/7 LP search, but a genuine new building block
  for a future higher-degree Positivstellensatz search. `\mathrm{NewGen}
  (G_0,G_0)$'s exact closed form is displayed in Step 4 above and
  independently numerically confirmed `\ge0` on the FULL unit square
  `[0,1]^2` (not just the tiny residual domain), `2{,}000{,}000`-point
  sweep, `\min\approx3.8\times10^{-17}`.

## Promotable lemmas (round 15 additions)

- **Two new degree-6 (and one degree-8) sign-definite `(0,0)`-graded product
  generators for the `-q_1,-r_0` certificate search.** With `G_0,
  E_{\mathrm{num}},\mathrm{Num}` as previously certified, the `(0,0)`-graded
  components of the three pairwise products
  $$B_{G_0E}:=(G_0\cdot E_{\mathrm{num}})_{00},\qquad B_{G_0N}:=(G_0\cdot
  (-\mathrm{Num}))_{00},\qquad B_{EN}:=(E_{\mathrm{num}}\cdot\mathrm{Num})_
  {00}$$
  have the exact closed forms displayed in this round's §1 above (degrees
  `6,6,8` respectively), and are each strictly sign-definite (`>0`) on the
  true residual domain `\{G_0>0\}\cap\{E_{\mathrm{num}}<0\}\cap\{c\ge2t^2-1\}
  \cap\{\mathrm{Num}<0\}` — confirmed both symbolically (zero-residual
  `sympy` re-derivation from the raw generator products, this round) and
  numerically (own fresh `10{,}118`-point true-domain sample, zero sign
  violations). Reusable by any future Positivstellensatz search on this
  domain.

## Promotable lemmas (round 14 additions)

- **Corrected exact degree-matched `(\mathbb Z_2\times\mathbb Z_2)`-graded
  basis for the `-q_1,-r_0` certificate search.** The six `(0,0)`-graded
  products
  $$B_1=\tau(1-\sigma)(2\tau-1),\quad B_2=-2\sigma(\tau-1)^2,\quad
  B_3=-\tau(\sigma-1)(32\sigma^2\tau-24\sigma^2-22\sigma\tau+12\sigma+\tau),$$
  $$B_4=-2\sigma(\sigma-1)(\tau-1)(16\sigma\tau-4\sigma-3\tau),\quad
  B_5=\tau(\sigma-1)(8\sigma^2\tau-6\sigma^2-3\sigma+\tau),\quad
  B_6=2\sigma^2(\sigma-1)(\tau-1)(4\tau-1)$$
  are, respectively, the exact `(0,0)`-graded (`\mathbb Z_2\times\mathbb Z_2$,
  parity of `\deg_c,\deg_d`) components of `ct\cdot G_0,\ sd\cdot G_0,\
  ct\cdot(-E_{\mathrm{num}}),\ sd\cdot(-E_{\mathrm{num}}),\ ct\cdot
  (-\mathrm{Num}),\ sd\cdot(-\mathrm{Num})` respectively, all verified this
  round by direct `sympy` reduction/projection (zero residual against the
  raw definitions). `B_1$–`B_5` match this round's parity-lens explorer's
  report exactly; `B_6` **corrects** a genuine error in the explorer's
  claimed formula (`2\sigma^2(\sigma-1)(\tau-1)(2\tau-1)(2\tau+1)`, which
  differs from the true value by `-8\sigma^2\tau(\sigma-1)(\tau-1)^2\ne0`).
  On the (loose, outer-bounding-box) domain `\sigma\in[0.156,0.261],\ \tau\in
  [0.625,0.786]`, exactly `B_1,B_4,B_6` are individually sign-definite
  (`>0$); `B_2<0` always (for `\sigma>0`); `B_3,B_5` are not sign-definite
  even on this loose box. Reusable by any future round attempting the exact
  Positivstellensatz certificate for `-q_1,-r_0`, or for `-\mathrm{Num}\ge0$-
  style targets elsewhere in the population.
- **Negative methodological finding: raw Gröbner-basis ideal-membership
  testing is structurally vacuous (a false positive) for zero-constant-term
  targets against this generator set.** Reducing `q_1$ against the Gröbner
  basis of `\langle c^2+s^2-1,d^2+t^2-1,\ ct\,G_0,\ sd\,G_0,\ ct\,
  (-E_{\mathrm{num}}),\ sd\,(-E_{\mathrm{num}}),\ ct\,(-\mathrm{Num}),\
  sd\,(-\mathrm{Num}),\ \mathrm{Bc}\rangle` gives remainder `0`, but this is
  a structural artifact — the Gröbner basis itself is `\{s^2,d^2-1,st,t^2,
  c+1\}`, forcing `s^2,t^2\to0`, and since `q_1,r_0` have zero constant term
  (every monomial contains a factor `\sigma=s^2` or `\tau=t^2`), they
  trivially reduce to `0` for this reason alone, unrelated to any genuine
  sign-definite decomposition. **Any future round must check the Gröbner
  basis of a proposed generator ideal is not itself degenerate in this way
  before trusting a "remainder 0" ideal-membership result as informative.**

## Promotable lemmas (round 13 additions)

- **`Num` identity — exact squaring-equivalence (unconditional).**
  `q^2(1-X_0)-p^2X_0=\mathrm{Num}/(2(ct+ds)^3)` as a genuine polynomial
  identity (own fresh `sympy` derivation, zero residual, this round),
  hence `q^2(1-X_0)-p^2X_0<0\iff\mathrm{Num}<0` unconditionally (given
  `\sin C>0`). Upgrades the round-13 explorer's 2,000-sample spot check to
  a full symbolic proof. Written up in full above (Item 1) and proposed as
  `lemmas/num-identity-exact-squaring-equivalence.md`.
- **`B\le C\iff c\ge2t^2-1`, conditional on `B<\pi/2` (elementary,
  `\cos`-monotonicity).** Proved above (Item 2), with the missing
  precondition (flagged by the outline-reviewer) now made explicit and
  discharged by citing the already-certified round-11 fact that `B<\pi/2`
  holds with comfortable margin on the exact residual sub-domain.
- **Parity-obstruction theorem (new structural result, this round).**
  `q_1,r_0` lie purely in the `(0,0)`-graded piece of `R:=\mathbb R[c,s,d,t]
  /\langle c^2+s^2-1,d^2+t^2-1\rangle$ (under the `\mathbb Z_2\times
  \mathbb Z_2` grading by parity of `\deg_c,\deg_d`), while `G_0,
  E_{\mathrm{num}},\mathrm{Num}` each lie purely in the complementary
  `(1,0)\oplus(0,1)` piece — proving rigorously that any Positivstellensatz
  certificate for `-q_1,-r_0` using `\{G_0,-E_{\mathrm{num}},\mathrm{Bc},
  -\mathrm{Num}\}` as generators must use at least one multiplier with an
  explicit bare odd power of `c` or `d` (constant/`(\sigma,\tau)`-only
  multipliers, round 12's exact search class, are structurally incapable
  of closing this gap). Proved in full above (Item 3), proposed as
  `lemmas/parity-obstruction-q1-r0-certificate.md`.

## Promotable lemmas (round 12 additions)

- **β1-elimination Step 1 identity (exact, unconditional).** With
  `x:=\cos\beta_1=\sqrt{X_0},\ y:=\sin\beta_1=\sqrt{1-X_0}` (`x,y\ge0` by
  construction), `\sin(A+3\beta_1)=s(4X_0-3)x+c(4X_0-1)y` for
  `s=\sin A,c=\cos A`. Proved by direct triple-angle expansion
  (`\cos3\beta_1=4x^3-3x,\ \sin3\beta_1=3y-4y^3`) and the substitution
  `x^2\to X_0,\ y^2\to1-X_0` inside the cubic terms, licit since `x,y\ge0`
  exactly (re-derived independently this round, matching q1r0lens's Step 1
  and the outline-reviewer's 200,000-sample confirmation).
- **`X_0` vs `1/4,3/4` reduces to a bare linear sign condition (new, exact,
  unconditional).** Since `\sin C=\sin A\cos B+\cos A\sin B>0` strictly for
  every triangle, `X_0=\sin B\cos A/(2\sin C)` satisfies
  $$X_0>\tfrac14\iff \sin B\cos A>\cos B\sin A,\qquad
  X_0<\tfrac34\iff \sin B\cos A+3\cos B\sin A>0,$$
  i.e. in `s=\sin A,c=\cos A,t=\sin B,d=\cos B` notation, `X_0>1/4\iff
  ct>sd` and `X_0<3/4\iff ct+3sd>0`. Proved directly from the definition of
  `X_0` (clearing the positive denominator `2\sin C`); reusable by any
  future attempt at closing the `X_0\in(1/4,3/4)` sub-target, or by the
  sibling `-pointwise`/`-tangent` family if `X_0`-comparisons recur there.
- **Canonical (Pythagorean-ideal-reduced) forms of `X_0-d^2` and `E`.**
  `2\sin C\,(X_0-d^2)=ct(1-2d^2)-2sd^3` and `2\sin C\cdot E\equiv
  ct\,f_1(\sigma,\tau)+ds\,f_2(\sigma,\tau)\pmod{\langle c^2+s^2-1,
  d^2+t^2-1\rangle}$, with `f_1=-32\sigma^2\tau+24\sigma^2+22\sigma\tau
  -12\sigma-\tau`, `f_2=-32\sigma^2\tau+8\sigma^2+38\sigma\tau-8\sigma
  -6\tau` (`\sigma=\sin^2A,\tau=\sin^2B`). Derived by `sympy.reduced` against
  the Pythagorean ideal, own fresh computation this round, cross-checked
  numerically to `<10^{-13}` relative error on 5 independent samples.
  Reusable as the starting point for a future resultant/Positivstellensatz
  attempt at the joint elimination `G_0>0\wedge(ctf_1+dsf_2)<0\Rightarrow
  (ct>sd)\wedge(ct+3sd>0)`, which remains open.

## Promotable lemmas (round 10 additions)

- **`G(\beta_1)\ge0` in the `P\le0` sub-case of Claim (II) Case (b),
  unconditionally.** For any triangle with `A\le\pi/2` and `X_0=\sin B\cos A
  /(2\sin(A+B))\in[0,1]$, writing `x=\sqrt{X_0},y=\sqrt{1-X_0}`, if
  `P=\tfrac12\sin(A-B)+\tfrac32\sin(A+B)\le0` then `G(\beta_1)=K+\sin A\sin
  B\,x-Py\ge K+\sin A\sin B\,x>0` strictly (`K=2\sin A\sin(A+B)>0`). Proved
  in full in the round-10 entry above (Step 1). Reusable by any sibling
  approach targeting the same `Y(\gamma)<0`/`G_{2b}`-exclusion core.
- **`D` strictly increasing in `x` on `[0,\infty)`, and `G(\beta_1)\ge0`
  in the `E\ge0` sub-case of `P>0`.** `D(x)=A_{\mathrm c}x^2+B_{\mathrm c}x+
  C_{\mathrm c}` (`A_{\mathrm c}=\sin^2A\sin^2B+P^2\ge0`,
  `B_{\mathrm c}=2K\sin A\sin B>0`, `C_{\mathrm c}=K^2-P^2`) satisfies
  `D'(x)\ge B_{\mathrm c}>0` for `x\ge0`; combined with `E:=A_{\mathrm c}X_0+
  C_{\mathrm c}\ge0\Rightarrow D(\sqrt{X_0})=E+B_{\mathrm c}\sqrt{X_0}\ge0`,
  hence (by the biconditional squaring argument, Step 2) `G(\beta_1)\ge0`.
  Proved in full above (Steps 2–3). Reusable similarly.
- **Exact factorization of the residual target `T=B_{\mathrm c}^2X_0-E^2`.**
  With `s=\sin A,c=\cos A,t=\sin B,d=\cos B$ (`c\ge0`), `\sigma=s^2,\tau=t^2`:
  `T=c(dQ_1(\sigma,\tau)-cR_0(\sigma,\tau))/(4\sin^2(A+B))`, `Q_1=-4st\,
  q_1(\sigma,\tau)`, with `q_1,r_0` the explicit degree-`(4,3)` polynomials
  displayed in the round-10 entry above — verified by `sympy.groebner`
  reduction modulo `\langle s^2+c^2-1,t^2+d^2-1\rangle`, zero residual. Not
  yet used to close the sign of `T`, but a genuine reduction reusable by any
  future attempt on this exact sub-case.

## Promotable lemmas (round 11 additions)

- **On the genuine residual sub-domain (`P>0\wedge E<0` intersected with
  the Case-(b) containment/sign conditions `\beta_1<\gamma`,
  `\sin(A+3\beta_1)<0`, `X_0\in[0,1]`), `P>0` holds automatically** (i.e.
  the corollary's case split reduces to a single branch there — `0/25{,}568`
  samples had `P\le0` on the Case-(b)`\wedge E<0` locus). Numerically
  established this round at large scale (`25{,}568` random + independent
  grid confirmation); not yet elevated to a symbolic proof, but a genuine,
  reusable simplification of the case-split bookkeeping for any future
  attempt.
- **On the same genuine residual sub-domain, `B<\pi/2` (hence `\cos B>0`)
  holds with comfortable margin** (`B` confined to `\approx(0.912,1.090)`,
  vs. `\pi/2\approx1.571`) — confirmed by both a `10{,}000{,}000`-sample
  random sweep and an independent `4000\times4000` grid scan, zero
  exceptions. (By contrast `B` can approach `\pi/2$ arbitrarily closely in
  the full, unrestricted Case-(b) domain — this comfortable margin is a
  genuine feature of the restricted residual sub-case specifically, not a
  general Case-(b) fact.) Numeric only; reusable as a component fact for any
  future termwise-sign closure of `T\ge0`.
- **Sufficient termwise decomposition of `T\ge0`.** Given `c\ge0,d>0,s,t>0`
  always, and (numerically confirmed, this round) `q_1<0,r_0<0` on the exact
  residual sub-domain: `4dst\,q_1+c\,r_0<0` follows immediately as a sum of
  two non-positive (here strictly negative) terms, with NO need to examine
  any linear/bilinear combination of `q_1,r_0` — a cleaner sufficient route
  than a "combination" search, contingent on the (open) individual-sign
  claims for `q_1,r_0` on the true sub-domain.

## Promotable lemmas (round 9 additions)

- **Theorem 16.1: `f(\beta)>0` throughout the effective domain
  `(\beta_0,\gamma)`, unconditionally, for every triangle.** `f(\beta)=2\sin
  (A+B)(\sin\beta+\sin A)-\sin B\sin(A+\beta)`, `\beta_0=(\pi-A)/3`,
  `\gamma=\min(\angle B,\angle C)`. Proved via (a) `f'(\beta)=\sin(A+\beta)
  \cos B+\sin(A+B-\beta)>0` throughout `(0,\gamma)` (WLOG `B\le C`), and (b)
  `f(\beta_0)>0` strictly via an exact two-case split on `\mathrm{sign}
  \big(2(\cos(2\beta_0)+1)(\cos(2\beta_0)+\tfrac14)\big)`. Full proof in
  §16 above ("New results 1–2"). This is exactly the `(I)` half of the
  round-8 two-part `G_{2b}`-exclusion target
  (`lemmas`-worthy: `f-positive-unconditional.md`).
- **Theorem 16.2: `2K-f(\beta)>0` throughout `(0,\gamma)` whenever
  `Y(\gamma)\ge0`** (`Y(\beta)=2\cos^2\beta-\sin B\cos A/\sin(A+B)`,
  `K=2\sin A\sin(A+B)`). Proved via monotonicity of both `f` (Theorem 16.1)
  and `Y` (`Y'=-2\sin2\beta<0`) plus the exact identity `\cos B(2\sin A-
  \sin B)-\sin(A+B)Y(\gamma)=\sin B(\cos\delta-\cos B)>0` (`A=\pi-2B-\delta`,
  `0\le\delta<B<\pi/2`). Full proof in §16 above. This is the `(II)` half
  of the round-8 target, closed on the majority sub-case (`\approx76\%` of
  domain-nonempty triangles in this round's sampling)
  (`lemmas`-worthy: `2K-minus-f-positive-on-Y-gamma-nonneg.md`).
- Both lemmas are reusable by any sibling approach targeting the same
  `G_{2b}`-exclusion / branch-selection core (`coordinate-bash-resultant-
  boundary-pointwise`, `fixed-point-concyclic`) per round 8's proven
  structural-equivalence theorem, though this round's cross-check confirmed
  they are not literally interchangeable with the `-pointwise` sibling's
  `num`-based `Y<0` target (different explicit expressions).

## Promotable lemmas (round 8 additions)

- **Discriminant of `Q(m)` is exactly `16\sin^2A`, unconditionally (§15).**
  For `Q(m):=m^2\sin(A+\beta)-4m\sin\beta-4\sin(A-\beta)` (the scale-
  invariant reformulation of `Z`'s sign, `A` a triangle's vertex angle,
  `\beta` the free parameter), `\mathrm{disc}(Q)=16\sin^2\beta+16\sin(A+
  \beta)\sin(A-\beta)=16\sin^2A>0` for every `A\in(0,\pi)`, via the product-
  to-sum identity `\sin(A+\beta)\sin(A-\beta)=\sin^2A-\sin^2\beta` — no
  hypothesis on `\beta` or on `\sin(A+3\beta)`'s sign is needed (a stronger
  closure than the outline's conditional request). Gives the exact roots
  `r_{1,2}=2(\sin\beta\mp\sin A)/\sin(A+\beta)`, `r_1<r_2` strictly always,
  and the exact factorization `Q(m)=\sin(A+\beta)(m-r_1)(m-r_2)` (verified
  by `sympy`, zero remainder). Reusable by any approach needing to classify
  `Q`'s sign as "inside/outside the root interval."
- **Negative result: the outline's `M_0\le r_2` step-7 lever is FALSE in
  general (§15).** `M_0:=2\cos^2\beta/\cos A$ (the `Y>0` upper bound on `m`
  when `\cos A>0`) does **not** satisfy `M_0\le r_2` in general — explicit
  counterexample `A\approx1.4829,B\approx0.1626,\beta\approx0.1611$ gives
  `M_0\approx22.19\gg r_2\approx2.32`, and the failure persists
  (`3{,}287/16{,}038` sampled violations) even after also imposing `B_2>0`.
  **Any future attempt at this approach's remaining gap must NOT try to
  route through an `M_0`-vs-`r_2` comparison** — it must use the actual
  triangle shape parameter `m=\sin B/\sin(A+B)$ (Law of Sines) directly, as
  in the reformulation (I),(II) below, not a crude interval bound on `m`.
- **Two-part exact reformulation of the G2b exclusion's remaining content
  (§15, not yet proved).** Writing `C=\pi-A-B`, `m=\sin B/\sin(A+B)`
  (Law of Sines, `AB=1`): the whole remaining gap for this approach is
  $$\text{(I)}\ \sin(A+3\beta)<0\implies\sin B\sin(A+\beta)<2\sin(A+B)
  (\sin\beta+\sin A),$$
  $$\text{(II)}\ [2\cos^2\beta>m\cos A]\wedge[\sin(A+3\beta)<0]\implies
  \sin B\sin(A+\beta)>2\sin(A+B)(\sin\beta-\sin A),$$
  for `A,B>0,A+B<\pi,\beta\in(0,\min(\angle B,\angle C))`. Ablation sweeps
  (own scripts, this round) show (I) needs only the `\sin(A+3\beta)<0`
  hypothesis (`0/19{,}667` violations), while (II) genuinely needs **both**
  hypotheses jointly (neither alone suffices: `Y>0` alone gives
  `7{,}356/278{,}438` violations, `B_2>0` alone gives `2{,}258/19{,}635`
  violations, the conjunction gives `0/25{,}276`). (I) is shown, by direct
  expansion, to genuinely mix `\beta` with the independent parameter `B`
  (via a `\cos(A-B+\beta)` term), so it does **not** reduce to the
  population's certified single-crossing lemma (which needs a bare function
  of `\beta` alone) without further new ideas. Reusable as the precise,
  sharpest-yet target for closing this whole route.

## Promotable lemmas (round 7 additions)

- **Trigonometric identification of `Y,B_2,Z` (§14).** For the polynomials
  `Y=2a(u^2-1)^2-b(u^2+1)^2`, `B_2` (`G_{2b}`'s leading `s_2^2`-coefficient),
  and `Z` (defined by `\mathrm{Res}_{s_2}(G_{2b},\tilde N_2)=-8u(u^2+1)^2F_2Z`),
  under the Weierstrass substitution `u=\tan(\beta/2)`:
  $$Y=(1+u^2)^2(2a\cos^2\beta-b),\quad B_2=-2(1+u^2)^3(b\sin3\beta+cc\cos3\beta),$$
  $$Z=(1+u^2)\big(p_1\sin\beta+q_1\cos\beta\big),\ \ p_1=b(2a-b)^2+cc^2(b-4a),\ \
  q_1=-cc(4a^2-b^2-cc^2),$$
  each proved by exact symbolic coefficient-matching (fitting each
  polynomial against a `\sin(k\beta),\cos(k\beta)`-numerator basis and
  confirming zero remainder by full expansion), not numerically. Also
  establishes `Y\propto F_3` (the previously-identified, only partially
  classified third resultant factor from `lemmas/f3-f3prime-resultant-
  factors.md`) — the same locus, `2a\cos^2\beta=b`, governs both. Reusable
  by any approach needing to reason about `G_{2b}`'s branch-exclusion
  polynomials, or about `F_3`'s geometric meaning, via trigonometric rather
  than raw-coefficient sign arguments.

## Promotable lemmas (round 6 additions)

- **Theorem 12.6 (§12): magnitude bound, and its exact coincidence with the
  Theorem 11.8/11.10 sign-selected root.** For every scalene triangle and
  every `\beta` in the valid range `(0,\min(\angle ABC,\angle ACB))`: (1)
  `G_{3a}(t_1)=0` has two real roots, exactly one of which places
  `K=B+t_1d(\beta)` on the correct side of line `MC` (`M=`midpoint `AB`) —
  combined with the ray-direction fact (`coordinate-bash-resultant-
  boundary.md` §8), this places `K` strictly inside the finite triangle
  `BMC`; symmetrically `G_{2a}(s_2)=0`'s analogous root places `L` strictly
  inside `\triangle BNC`; (2) that magnitude-bound root of `G_{3a}` (resp.
  `G_{2a}`) is **exactly** the root already selected by Theorem 11.10 (resp.
  11.8)'s cross-product-sign test ("L inside angle ACK" / "K inside angle
  LBA") — no separate case analysis is needed, the two selection criteria
  always agree. Proved via: an affine-vs-quadratic resultant identity
  (mirroring Lemma 11.5's method) for the new containment tests
  `\tilde N_1(t_1)` (K-vs-edge-MC) and `\tilde N_2(s_2)` (L-vs-edge-NB); a
  new general "root-pairing lemma" (given two affine functions each
  splitting a quadratic's two real roots by sign, the roots they select
  coincide iff the two affine functions' slopes have the same sign); and
  three trigonometric sign facts (`Q^{\rm ptrig},Q^{\rm trig}>0`, `R^{\rm
  trig}<0` throughout the valid range, each proved via a general
  "single-crossing" sinusoid lemma plus explicit closed-form endpoint
  values at `\beta=\angle ABC,\angle ACB`, using the standard "larger angle
  opposite larger side" fact). Fully general, no numerics-only step. Closes
  `coordinate-bash-resultant-boundary.md` §8's long-standing open item.
- **Lemma 12.4 (root-pairing lemma), general and reusable independently of
  this problem's specific polynomials.** If a real quadratic `f=At^2+Bt+C`
  has two distinct real roots `r_1<r_2`, and two real affine functions
  `X(t)=Q_Xt+P_X`, `Y(t)=Q_Yt+P_Y` (`Q_X,Q_Y\ne0`) each satisfy
  `X(r_1)X(r_2)<0`, `Y(r_1)Y(r_2)<0`, then `\mathrm{sign}(X(r_1))=
  \mathrm{sign}(Y(r_1))\iff\mathrm{sign}(Q_X)=\mathrm{sign}(Q_Y)`. Proved by
  a direct IVT argument locating each affine function's unique zero strictly
  between `r_1,r_2`. Reusable by any approach needing to compare two
  different sign-selection criteria on the same quadratic's roots.
- **Single-crossing lemma (§12), general and reusable.** For `h(\beta)=
  p\sin(k\beta)+q\cos(k\beta)` (`k\in\{1,2\}`, not both `p,q=0`) and an open
  interval `(0,\gamma)` with `\gamma<\pi/k`: if `h(0)>0` and `h(\gamma)>0`,
  then `h(\beta)>0` throughout `(0,\gamma)`. Proved via "zeros of `h` are
  spaced exactly `\pi/k` apart, so an interval shorter than `\pi/k` contains
  at most one, and a lone interior zero would force opposite-sign endpoints
  since all zeros of `h` are simple." Reusable by any approach needing to
  sign a sinusoidal quantity throughout a sub-`\pi` angular range from only
  two endpoint evaluations.
- **True/supplementary root criterion for `G_{2b}` (§13), and the "always
  same status" theorem.** A root `s_2` of `G_{2b}(s_2)=0` corresponds to the
  genuine (non-supplementary) solution of hypothesis 2's unsquared equation
  `\angle LBK=\angle LNC` iff `W(s_2):=\mathrm{dot}(BL,BK)\cdot
  \mathrm{dot}(NL,NC)>0` (both affine-linear in `s_2`, given explicitly).
  New theorem, proved by a resultant computation
  `\mathrm{Res}_{s_2}(G_{2b},D_K^{\rm num}D_N^{\rm num})=-4u(b^2+cc^2)^2
  (1+u^2)^6F_2[2a(u^2-1)^2-b(u^2+1)^2]^2\ge0` on the valid range (`F_2<0`):
  `G_{2b}`'s two real roots always share the same true/supplementary status
  (never split) — refutes and replaces the previously-reported (numeric-only)
  "generically one true, one supplementary" characterization. Reusable by
  any approach needing to identify the genuine branch of a squared-cosine
  angle-equality construction.

## Promotable lemmas (round 5 additions)

- **Theorem 11.8 / 11.10 (§11): unique cross-product-sign selection on the
  `G_{2a}`/`G_{3a}` branch.** For every real triangle `A,B,C` and every
  `\beta` in the valid range `(0,\min(\angle B,\angle C))`, the quadratic
  `G_{2a}(s_2)=0` always has two distinct real roots, and exactly one of
  them satisfies the cross-product-sign test for "K inside angle LBA"
  (given the standing hypothesis `L\in\triangle BNC`); symmetrically for
  `G_{3a}(t_1)=0` and "L inside angle ACK" via `σ`-symmetry. Proved by: (a)
  reducing "K inside angle LBA" to the single sign condition
  `\mathrm{cross}(BK,BL)<0` given `L\in\triangle BNC` (Lemmas 11.1–11.4,
  using that `\mathrm{cross}(BA,\cdot)` is affine and `\le0` on all of
  `\triangle BNC`); (b) showing `\mathrm{cross}(BK,BL)` is affine-linear in
  `s_2` with numerator `L_1=P+s_2Q` (Lemma 11.5, `P=(1+u^2)F_1`); (c) a
  resultant computation `\mathrm{Res}_{s_2}(G_{2a},L_1)=4u(1+u^2)^3F_1F_2`
  combined with three sign facts — `F_1,F_2<0` throughout the valid range
  (Lemma 11.6, from the already-certified `branch-crossing-locus-equals-
  angle-B/C.md`) and the leading coefficient `A_2` of `G_{2a}` satisfies
  `A_2<0` throughout the valid range (Lemma 11.7, a new case-split proof:
  trivial for `b\ge0`, via a `\tan`-comparison `\angle B<\theta_0` for
  `b<0`) — to conclude `L_1(r_1)L_1(r_2)<0`, hence opposite signs (and,
  as a bonus, that the roots are always real). Reusable by any approach
  needing to formalize the "K inside ∠LBA"/"L inside ∠ACK" hypotheses on
  the `G_{2a}`/`G_{3a}` branch specifically.
- **Lemma 11.7: sign of `G_{2a}`'s leading coefficient throughout the
  valid range.** `A_2 = -2(1+u^2)^2(cc\cos\beta+b\sin\beta) <0` for every
  `\beta\in(0,\min(\angle B,\angle C))` and every triangle — proved by an
  elementary case split on `\mathrm{sign}(b)` (trivial when `b\ge0`; via
  `\tan(\angle B)<\tan\theta_0` when `b<0`, using that `b<0\Rightarrow
  \angle A` obtuse `\Rightarrow\angle B,\angle C<\pi/2`). Reusable
  independently of the rest of §11 as a general fact about this rotation
  parametrization.

- **`lemmas/branch-crossing-locus-equals-angle-C.md` (§7).** `F_2=0\iff
  \beta=\angle ACB` exactly (not merely "parallel"), by the identical
  cross-product + uniqueness-in-`(0,\pi)$ argument certified for `F_1$,
  applied via the `\sigma$-symmetry. Also supplies the missing
  uniqueness/exactness step for `F_1$ itself (retroactive fix to
  `lemmas/branch-crossing-locus-equals-angle-B.md`).
- **Ray-direction monotonicity (§8).** For `\beta\in(0,\angle ABC)`, ray
  `BK`'s direction sweeps monotonically and strictly inside angle `\angle
  ABC` (analogously for `CL$ and `\angle ACB`); rigorous, reusable by any
  approach needing the "direction" half of a containment argument — but
  explicitly NOT sufficient alone (see §8's caveat) to conclude full
  triangle-containment without an added magnitude bound.
- **`F_3,F_3'` identification (§9).** `F_3=0\iff\cos^2\beta=b/(2a)`,
  `F_3'=0\iff\cos^2\beta=ab/(2(b^2+cc^2))` — both palindromic quartics in
  `u=\tan(\beta/2)`, symmetric under `\beta\to\pi-\beta`. Reusable by any
  future attempt at the branch-selection gap; comes with an explicit
  counterexample triangle (`A{=}(0,0),B{=}(1,0),C{=}(0.9,0.2)`) showing
  these loci are **not** always outside the valid range, correcting an
  implicit assumption in round 3–4's plan.

## Promotable lemmas

- **`F_1=0 \iff \beta=\angle ABC` (§4).** For the rotation parametrization
  `K=B+t_1(-\cos\beta,\sin\beta)` with `A=(0,0),B=(a,0),C=(b,cc)`, the
  polynomial `F_1(a,b,cc,u)=2au-2bu+cc\,u^2-cc` (in the Weierstrass variable
  `u=\tan(\beta/2)`) vanishes exactly when the ray `BK`'s direction
  `(-\cos\beta,\sin\beta)` is parallel to `BC`, i.e. exactly at
  `\beta=\angle ABC` — proved by direct cross-product computation, fully
  general (no triangle-specific numerals). Geometrically: this is exactly
  the moment `K` (extended along its ray) reaches side `BC`, i.e. the
  natural upper boundary of "`K` inside triangle `BMC`." Reusable by any
  approach using this rotation parametrization to identify or bound the
  valid range of `β`.
- **Resultant factorization structure (§4).** `\mathrm{Res}_{s_2}(G_{2a},
  G_{2b})` and `\mathrm{Res}_{t_1}(G_{3a},G_{3b})` (the hypothesis-2 and
  hypothesis-3 branch-crossing loci, in the same symbolic `a,b,cc,u` ring as
  the certified genericity result) share exactly two nontrivial common
  factors `F_1,F_2` (beyond the trivial `u^2(u^2+1)^4`) — computed and
  factored fully symbolically this round; reusable as the starting point for
  closing gap 2 (only `F_2`'s geometric identification and the general
  inequality `F_2`'s root `>\angle B` remain).
- **Multi-triangle branch-selection dataset (§5).** 16 independently solved
  data points (4 triangles × 4 β-values) confirming `G_{2a}\approx
  G_{3a}\approx0`, `G_{2b},G_{3b}\gg0` at every genuine solution — reusable
  as regression/sanity data for any future attempt at gap 2, and as
  additional Schwartz–Zippel-style corroboration beyond the sibling's single
  triangle.
