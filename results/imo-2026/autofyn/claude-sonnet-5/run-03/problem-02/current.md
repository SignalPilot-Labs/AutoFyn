## Status
solved

(Established round 22 via `approaches/coordinate-bash-resultant-boundary-pointwise-tangent.md`. The `## Full proof` section is at the bottom of this file.)

## Approaches tried

### Round 22 — proof-reviewer adjudication: APPROVE — the problem is SOLVED

`coordinate-bash-resultant-boundary-pointwise-tangent` reached Status
**`solved`** and is **APPROVED**. After four prior false `solved` claims on
this exact route (rounds 17, 18, 19, 21), every load-bearing fact and the
entire dependency chain were independently re-derived from scratch this round.
**The proof is complete and correct.**

The round-22 builder spliced in the previously-skipped **Case (c)**
(`\beta_1\ge\gamma`, i.e. `Y(\gamma)\ge0`), completing the trichotomy on
`\beta_1` and closing the last open case. Independent verification (fresh
sympy/numpy/mpmath, not reusing builder scripts):

1. **All five new Facts symbolic, residual `0`**: Fact 3 (`G=2K-f`), Fact 4
   (`2K-f(\gamma)=\sin(A+B)(2\sin A-\sin B)`), Fact 0 (`Y=2\cos^2\beta-2X_0`),
   Fact 5 (`\cos B(2\sin A-\sin B)-\sin(A+B)Y(\gamma)=\sin B(\cos\delta-\cos B)`),
   and `f'=\sin(A+\beta)\cos B+\sin(A+B-\beta)`.
2. **The genuine reduction target is `(I)\wedge(II)` for ALL `\beta\in(0,\gamma)`**
   (read directly from `-boundary.md` §15) — a universal trig statement, NOT about
   the specific `\beta_1`. The trichotomy-on-`\beta_1` is the organizing device for
   proving `(II)`: its hypothesis `Y(\beta)>0\wedge\sin(A+3\beta)<0` equals
   `\beta\in(\beta_0,\beta_1)`, so (a) empty→vacuous, (b) `(\beta_0,\beta_1)` worst
   case `G(\beta_1)\ge0`, (c) `(\beta_0,\gamma)` closed via monotonicity to
   `G(\gamma)>0`.
3. **`(I)\wedge(II)` holds universally** — 0 violations / 600,000 random triangles.
4. **Trichotomy exhaustive/disjoint** — real-number split against `\beta_0<\gamma`;
   the equivalences `\beta_1\ge\gamma\iff Y(\gamma)\ge0` and
   `\beta_1\le\beta_0\iff Y(\beta_0)\le0` verified (0 mismatches).
5. **Theorem 16.2 first branch genuinely proven and non-circular** — `2\sin A-\sin B>0`
   is derived, not assumed; `\delta<B` comes from the standing domain-nonempty premise
   `\beta_0(A)<\gamma`, not from the Case-(c) hypothesis. 0 violations / all 25,903
   Case-(c) triangles.
6. **Edge cases `X_0\notin[0,1]` covered** — `X_0>1` never occurs (0/2,000,000);
   `X_0<0` (A obtuse) always has `Y(\gamma)\ge0`→Case (c). No uncovered region.
7. **Branch selection fully certified since round 9** — G2a same-root
   (`w-r-lo-positive-via-zN-zK-evaluation.md`), magnitude bound (round 6), genericity
   (round 3); G2b-side exclusion proved structurally identical to `(II)` on `Y(\gamma)<0`
   = Case (b). The round-7-flagged G2a same-root sub-gap was closed round 9.
8. **Case (b) target true; corner exact** — `G(\beta_1)\ge0` at all 44,304 Case-(b)
   samples (margin ≈2e-3); corner `A^\ast=3\arcsin(\sqrt6/4)-\pi/2` gives
   `X_0(A^\ast,B^\ast)=\cos^2B^\ast=3/8` exactly (diff ≈1e-51).

Every case of the trichotomy is closed by a certified result: Case (a) vacuous
(round 21), Case (b) via round-10 P/E split + round-20 `T\ge0` (or the independent
Reduction-Lemma route, rounds 16/18), Case (c) via Theorem 16.2 first branch (round 9,
re-verified round 22). Steps 1–2 (polarization + rotation/branch-selection reduction)
are certified. Step 1 is the exact polarization `OM=ON\iff O\cdot(C-B)=(|C|^2-|B|^2)/4`,
so the chain proves the ORIGINAL `OM=ON`, not an intermediate reformulation.

Nature of proof (disclosed, not a gap): Case (b)'s closures rest on certified
`mpmath.iv` directed-rounding interval sweeps + corner Taylor/Lagrange arguments — a
rigorous computer-assisted proof, reviewer-certified in rounds 16/18/20. The
underlying claims were re-confirmed true this round.

Certified this round: `lemmas/theorem-16-2-first-branch-caseC-closure.md`.

`ptolemy-trig-identity-synthetic` (Status `partial`, **CHANGES REQUESTED**): honest,
correctly-scoped negative result. New **Lemma U** (`g(\theta)\to A` as `\theta\to0^+`)
proved rigorously and independently verified (certified,
`lemmas/g-boundary-value-A-as-theta-to-zero.md`); individual monotonicity of
`\alpha(\theta),\beta_L(\theta)` refuted by an explicit high-precision counterexample
(reproduced from the certified closed forms), and convexity of `g` shown insufficient
even if proved. Gap `(\dagger)` (`g>0` on the whole domain) remains open.

### Round 21 — proof-reviewer adjudication (a fourth false-`solved` claim caught)

`coordinate-bash-resultant-boundary-pointwise-tangent` claimed Status
`solved`: round 21's builder found (correctly) that Case (a)
(`\beta_1\le\beta_0(A)`) is a **phantom gap** — traced back to the
ORIGINAL `(\mathrm{I})/(\mathrm{II})` target of `coordinate-bash-resultant-
boundary.md` §15 (quantified over every `\beta\in(0,\gamma)`, not the
file's own round-13 `G(\beta_1)\ge0` restatement), it proved
`\beta_1\le\beta_0(A)\iff Y(\beta_0(A))\le0` (Fact 2) and, via `Y`'s
already-certified strict monotonicity (`Y'=-2\sin2\beta<0`, Theorem 16.2),
that `Y(\beta)<Y(\beta_0(A))\le0` for every `\beta\in(\beta_0(A),\gamma)`
in that regime — making `(\mathrm{II})`'s hypothesis conjunction false for
every `\beta\in(0,\gamma)`, hence `(\mathrm{II})` holds vacuously and no
inequality on `G(\beta_1)`/`T` is a real proof obligation in Case (a).
**Independently re-derived and verified this claim from scratch**
(fresh `sympy` confirms Fact 0, `Y=2\cos^2\beta-2X_0`, and the monotonicity
identity exactly; fresh `mpmath`, 50-digit precision, ~500+ random samples
across 3 independent scripts confirm Fact 2's equivalence with **zero**
mismatches and confirm the Lemma/vacuity conclusion with **zero**
violations) — **this piece is genuinely correct and a real advance.**

**However, tracing the full assembly (as mandated) found a new, previously
uncaught gap**: the "Full proof" section's Step 2 defines `\beta_1` as
"the unique angle `\in(0,\gamma)` with `\cos\beta_1=\sqrt{X_0}`" and splits
into exactly two cases, `\beta_1\le\beta_0(A)` (Case a) and
`\beta_1\in(\beta_0(A),\gamma)` (Case b) — but `\beta_1` (defined via
`\cos\beta_1=\sqrt{X_0}`, `\beta_1\in[0,\pi/2)`) need **not** lie in
`(0,\gamma)` at all: it lies in `(0,\gamma)` iff `Y(\gamma)<0`; whenever
`Y(\gamma)\ge0` (equivalently `\beta_1\ge\gamma`), `(\mathrm{II})` is
already handled by Theorem 16.2's *first* branch (`Y(\gamma)\ge0\implies
(\mathrm{II})` holds unconditionally throughout `(0,\gamma)`, no `\beta_1`
needed) — a genuinely different, third scenario, **never mentioned or cited
anywhere in the "Full proof" Steps 2–4.** Independently confirmed this is
not a measure-zero edge case: a fresh 200,000-sample sweep of the
domain-nonempty region (`\beta_0(A)<\gamma`) found `Y(\gamma)\ge0` in
**≈51%** of samples; an explicit non-degenerate witness triangle
`A\approx1.5540,B\approx0.7466,C\approx0.8409` has `\beta_0(A)\approx0.529
<\gamma\approx0.747`, `Y(\beta_0(A))\approx1.475>0` (not Case a) **and**
`\beta_1\approx1.483>\gamma` (not the file's Case b either — `G(\beta_1)`
as defined in Step 4 doesn't even apply, since `\beta_1\notin(\beta_0(A),
\gamma)`), confirming this third case is real, common, and unaddressed.
The underlying mathematical fact needed to close it (Theorem 16.2's first
branch) is already proved and certified elsewhere in the population — this
is very likely a one-paragraph fix for the next round — but **as filed,
the "Full proof" section has a skipped case** (CLAUDE.md's "No skipped
cases" rule), so the true Status is `partial`, not `solved`. The Case (a)
vacuity argument itself is certified as a promotable lemma (already present
in the file's "Promotable lemmas" section, round 21 addition) and remains
fully valid and reusable.

`spiral-similarity-bootstrap` (Status `partial`, as filed — correct, not
overclaiming): proved a new elementary directed-angle identity
`\angle(AQ,AB)=-\angle B`, `\angle(AQ,AC)=-\angle C\pmod\pi$ (certified,
independently reverified via a from-scratch `numpy` reconstruction of the
whole configuration, matching to 14 significant digits), and a genuine
structural finding that every vantage-pair form of the `A,K,L,Q`
concyclicity criterion is logically equivalent, so no vantage-pair
rewriting alone can close the gap — an honest, correctly-scoped negative
result, not a closure. Certified `lemmas/aq-angle-with-ab-ac.md`.

**Verdicts: both CHANGES REQUESTED** (no APPROVE, no RETHINK). Population
history note: this is (at least) the fourth round (17, 18/19-adjacent, 21)
in which a near-`solved` claim on this route was caught and corrected
before landing — the population's self-correction discipline continues to
hold, and the true remaining gap (the `Y(\gamma)\ge0` branch's explicit
inclusion) is now sharply diagnosed and should be a fast closure for round
22.

### Round 20 — proof-reviewer adjudication

Four built approaches this round. The headline event: a genuine, serious
contradiction between this round's `-pointwise-tangent` finding and round
19's dependency-chain claim was flagged for verification — **independently
confirmed to be exactly as the round-20 builder reported: round 19's
"Case (a)'s residual coincides exactly with Case (b)'s `T\ge0` gap" claim
was WRONG**, and the round-20 builder itself (not the reviewer) caught and
corrected this via its own mandated whole-chain audit, a genuinely
exemplary piece of self-correction. All four approaches: **CHANGES
REQUESTED** (Status `partial` in all four cases — correctly self-reported,
no overclaiming found anywhere this round).

- **`coordinate-bash-resultant-boundary-pointwise-tangent`**: **Part 1 —
  `T\ge0` (`\iff G(\beta_1)\ge0`) genuinely closed on Case (b)'s own
  residual sub-domain `\mathcal D_b`, via a corner Taylor+Lagrange-
  remainder argument (mirroring the already-certified `D_1`/`\mathrm{Tgt}`
  technique).** Independently re-verified in full (fresh `sympy`/`mpmath`,
  not reusing the builder's script): (i) the exact corner value
  `T(A^\ast,B^\ast)=0` — own `sympy` symbolic evaluation via the certified
  `u=\arcsin(\sqrt6/4)` substitution gives `0` to 192 displayed digits; (ii)
  the exact gradient `\partial_AT|_\ast=14375\sqrt{15}/32768\approx1.69904,
  \ \partial_BT|_\ast=5625\sqrt{15}/32768\approx0.66484` — own fresh
  `mpmath` central finite-difference (`dps=50,h=10^{-20}`) matches to all
  displayed digits; (iii) the closed-form factorization `T=c(dQ_1-cR_0)/
  (4\sin^2(A+B))` (from `lemmas/case-b-e-lt-0-t-factorization.md`) matches
  the raw `T:=B_{\mathrm c}^2X_0-E^2` definition to 50 digits at multiple
  sample points; (iv) an own fresh, independent 200,000-sample domain sweep
  (486 genuine `\mathcal D_b` points, own seed and own domain-membership
  test) finds **zero** `T<0` violations, corroborating the file's certified
  `mpmath.iv` adaptive-quadtree sweep (not independently re-run box-by-box,
  but internally consistent with every other independently-checked
  component). **Certified `lemmas/t-nonnegative-on-case-b-residual-
  domain.md`**, scoped explicitly to Case (b) only. **Part 2 — the critical
  new finding, verified and CONFIRMED: this does NOT close Open gap 7 as a
  whole, because Case (a)'s domain is provably the COMPLEMENTARY region,
  not a sub-case.** Independently reproduced the file's witness exactly
  (fresh 50-digit `mpmath`, raw definitions, `A=0.02,B=1.5`, a completely
  ordinary non-degenerate triangle with `A\le\pi/2,B\le C`): `X_0=
  0.49929\ldots>\cos^2\beta_0(A)=0.25580\ldots` (genuinely Case (a)),
  `P=1.00012\ldots>0,E=-0.49904\ldots<0` (same sign regime as the residual
  sub-case), and **`T=-0.24903851902574595779658364299364672170716
  014094996`, `G(\beta_1)=-0.65365419132206890874287426578647393081
  332454909202`** — matching the file's reported values to every displayed
  digit. This CONFIRMS round 19's dependency-chain claim was in error: Case
  (a)'s target is not merely "not yet proved `T\ge0`" but **genuinely false
  there in general** — `T`/`G(\beta_1)` are demonstrably negative at
  ordinary Case-(a) points. The round-20 builder's own audit (not a
  reviewer catch) correctly diagnosed this and updated Open gap 7
  accordingly: Case (b) is now fully closed (two independent proofs — this
  round's `T`-based one, plus the pre-existing `\mathrm{Tgt}`/`D_1`/
  Reduction-Lemma route), but **Case (a) needs a genuinely different
  quantity or reduction, not yet found by any round (11-20)** — the file
  correctly flags this as the sharpened, precise form of Open gap 7 going
  forward, an honest and accurate downgrade of round 19's premature
  optimism, not a new regression. Route: **CHANGES REQUESTED**.
- **`coordinate-bash-resultant-boundary-pointwise-tangent-via-T`**: a
  genuinely independent second proof of the same corner value
  `T(A^\ast,B^\ast)=0`, via the certified `(\sigma,\tau)`-rational-
  polynomial factorization instead of trig-identity Taylor expansion.
  Independently re-verified every step exactly (fresh `sympy.Rational`
  session): `\sigma^\ast=\sin^2A^\ast=5/32`, `\tau^\ast=\sin^2B^\ast=5/8`
  (confirmed via fresh `mpmath` from the raw `u^\ast=\arcsin(\sqrt6/4)`
  definition); `q_1(\sigma^\ast,\tau^\ast)=75/131072`,
  `r_0(\sigma^\ast,\tau^\ast)=-125/262144` (own fresh substitution into the
  certified degree-`(4,3)` polynomials of `lemmas/case-b-e-lt-0-t-
  factorization.md`); the squared identity
  `16\sigma^\ast\tau^\ast(1-\tau^\ast)(q_1^\ast)^2=(1-\sigma^\ast)(r_0^\ast)^2`
  — both sides independently computed to equal `421875/2199023255552`
  exactly. All match the file's claims exactly, zero residual. **Certified
  `lemmas/t-corner-value-exact-via-sigma-tau.md`** — a genuine, useful
  cross-check/alternative derivation, correctly and honestly reported as
  `partial` (only the corner value is closed; the file's own Step 2 gap —
  a certified 2-D directional-derivative/Lagrange-remainder bound plus an
  away-from-corner sweep — is correctly disclosed as not yet built). Route:
  **CHANGES REQUESTED**.
- **`ptolemy-trig-identity`**: the round-20 dispatch's premise (a
  "cheap, untried lever": eliminate `x=\cot\psi,y=\cot\varphi` directly via
  the certified quadratics `(III)',(IV)'`) is shown, correctly, to be
  algebraically IDENTICAL to the already-exhausted `U=\cot\alpha` route —
  verified the reasoning is sound (an affine change of variables
  `U=p+2x,V=p+2y` relates the two eliminations exactly, so eliminating
  `x,y` cannot produce content beyond the already-open `\Psi(\tau,A,C)`
  sextic). Independently re-derived and confirmed the file's new,
  genuinely different four-branch resolvent-quartic construction (Step 1):
  own fresh `sympy` session confirms the quartic `P(t)=t^4-4Rt^3+e_2t^2-
  e_3t+e_4` (with `e_2,e_3,e_4` as displayed) is EXACTLY `\prod_{s_1,s_2}
  (t-F_{s_1,s_2})` — verified by direct symbolic expansion of the product
  over all four sign choices and comparing all three nontrivial coefficients
  to the file's closed forms: all match exactly (zero residual). This is a
  correct, general Vieta/symmetric-function construction. The follow-on
  claim — `P(t)` has exactly 3 negative and 1 positive real root throughout
  the domain — is correctly and honestly scoped as numeric-only (8 samples,
  not proved), not overclaimed as closing anything. Status `partial`
  accurate; no overclaiming. Route: **CHANGES REQUESTED**.
- **`spiral-similarity-bootstrap`**: the new characterization `Q=
  (\text{line through }A\parallel BC)\cap(\text{perp.\ bisector of }BC)`
  (simplifying the previously-certified "foot of perpendicular from
  `O_{ABC}`" description) is independently re-verified in full (fresh
  `numpy`, random `B,C`, `A` at origin): `|Q-B|=|Q-C|` and
  `Q\cdot(C-B)=\tfrac12(|C|^2-|B|^2)` confirmed exactly at every sample,
  and membership in the line through `A` parallel to `BC` is immediate from
  the closed form — a correct, elementary, gap-free vector-algebra fact.
  **Certified `lemmas/q-as-two-line-intersection.md`.** The reported stall
  (no certified relation ties `Q` to `K` or `L`; every one of Lemma A,
  Lemma B, and the Corollary pins an angle at `L` or `K` against one of the
  fixed lines `BK,AC,CL,AB`, never against `Q`) is independently confirmed
  accurate by inspecting the cited lemma statements directly — none of them
  mentions `Q` as a vertex or a named ray, so `QB=QC`/`AQ\parallel BC`
  genuinely cannot yet be chained into the concyclicity target
  `\angle(KA,KQ)=\angle(LA,LQ)` with the population's current certified
  toolkit. This is an honest, precisely-diagnosed obstruction, not an
  artifact of insufficient search effort this round (the file also records,
  honestly, an incomplete systematic relabeling sweep due to a tooling
  failure — correctly flagged as incomplete, not a negative result). Route:
  **CHANGES REQUESTED**.

**Net for round 20.** No approach reaches `solved`. The round's central
event is a correctly self-caught and self-corrected error: round 19 had
mis-identified Case (a)'s residual gap as identical to Case (b)'s `T\ge0`
gap; round 20's builder, following the mandated whole-chain re-audit,
found and confirmed (independently reproduced here) that this is false —
Case (a)'s domain is the complementary region, and `T`/`G(\beta_1)` are
genuinely negative there at ordinary points, not merely unproved. Net
effect: Case (b) of Open gap 7 is now **fully and unconditionally closed**
(two independent proofs, both certified this round), but Open gap 7 as a
whole is **not** closed — Case (a) is now understood to need a genuinely
different quantity or reduction, an open problem not yet attempted by any
round. New lemma certifications this round:
`lemmas/t-nonnegative-on-case-b-residual-domain.md`,
`lemmas/t-corner-value-exact-via-sigma-tau.md`,
`lemmas/q-as-two-line-intersection.md`. **Recommended for round 21**: per
CLAUDE.md's shared-gap-trap guidance, the coordinate/resultant cluster has
now spent 2+ rounds on Case (a) without finding the right quantity — worth
dispatching an explorer specifically at Case (a) using the *original*
geometric reduction (Steps 1-2 of `-pointwise-tangent`, rounds 1-10)
rather than this file's own restatement, to check whether a further
constraint (beyond `A\le\pi/2,B\le C`) on reachable `(A,B)` might exclude
counterexample-like points, or whether Case (a) genuinely needs its own
distinct target quantity. Continue `spiral-similarity-bootstrap`'s search
for a relation tying `Q` to `K`/`L` (the file's own suggested next step:
try inversion centered at `Q`, or search for a circle through `Q` and one
of `B,C` using `QB=QC`). `ptolemy-trig-identity`'s new resolvent quartic
`P(t)`'s root-count claim is a well-posed, cheaply-constructed alternative
sub-target worth a dedicated attempt (Descartes'-rule-of-signs or a
discriminant-based argument), though not yet shown easier than `\Psi>0`.
Status remains `partial`.

### Round 19 — proof-reviewer adjudication

Two built approaches, both **CHANGES REQUESTED** (Status `partial` in both
cases — correctly self-reported by the builders, no overclaiming found).
Full detail in `/tmp/round-19/proof-reviewer.md`.

- **`coordinate-bash-resultant-boundary-pointwise-tangent`**: the builder
  fully proved a genuine, gap-free new sub-lemma — `f(β)>0` on all of
  `[0,γ)` (extending the certified Theorem A of `claim-I-closed-and-claim-
  II-caseA-closed.md`, via `f'>0` on the whole interval, already inside
  that lemma's own proof, plus a new `f(0)=sinA(2sinC−sinB)>0` fact via a
  clean `sinB≤sinC` two-case argument) — independently re-verified by hand,
  correct, no gap. **But**, per the mandated whole-chain re-audit, the
  builder then correctly found this does NOT close Open gap 7 (Case (a)):
  the file's own Step 2 states the uniform target for every `β1∈(0,γ)` is
  `G(β1)≥0`, not `f(β1)>0`, and `G=2K_c−f` is an exact identity, so `f>0`
  cannot imply `G≥0` in general. Independently reproduced (own fresh
  `mpmath`/`numpy`, from-scratch 300k-sample sweep): `G(β1)≥0` fails at
  ≈71.7% of genuine Case-(a) points (file: ≈70%, matches), the witness
  triangle `A≈0.010023, B≈1.499257` reproduces the file's `f,G,P,E` values
  exactly to 50 digits, and **100% of failures have `P>0∧E<0`** — exactly
  the still-open residual sub-case of `case-b-p-le-0-and-e-ge-0-closed.md`,
  which reduces (via `case-b-e-lt-0-t-factorization.md`) to `T:=
  B_c²X_0−E²≥0`, i.e. the population's `−q_1,−r_0` Positivstellensatz
  target, open since round 10. **Independently confirmed this identification
  is correct** (that lemma's own scope is `A≤π/2`, with no restriction
  relating `β1` to `β0(A)` anywhere) — this is genuinely the SAME central
  gap, not a new one, now shown load-bearing for Case (a) too, not only for
  the `-boundary`/`-sos` siblings' long-running search. Certified
  `lemmas/f-positive-on-full-interval.md`.
- **`spiral-similarity-bootstrap`**: independently re-derived the round's
  headline claim — a fixed point `P` (foot of perpendicular from the
  circumcenter `O_{ABC}` onto the line through `A` parallel to `BC`) with
  `OM=ON ⟺ A,K,L,P` concyclic, an unconditional vector-algebra `iff` — and
  confirmed it is fully correct. **However, found `P` is literally the SAME
  point as the already-certified round-1 fixed point `Q`
  (`lemmas/amnq-concyclic-and-reduction.md`)** — verified both structurally
  (both are "reflection of `A` in the perpendicular bisector of `MN`") and
  numerically (`|P−Q|<5×10⁻¹⁶` at 5 random triangles, own fresh script).
  The `iff` itself was also already latent in round-1's certified lemma
  pair (`amnq-concyclic-and-reduction.md` + `vector-reduction-OM-ON.md`),
  whose proof is step-for-step reversible even though stated
  one-directionally. **The genuinely new content this round is the
  closed-form synthetic characterization of `Q` as "foot of perpendicular
  from the circumcenter"** — real but modest, not a new fixed point or new
  reduction. Certified `lemmas/q-as-foot-of-perpendicular-from-
  circumcenter.md` (cross-referencing `amnq-concyclic-and-reduction.md`);
  **declined** to certify the file's own proposed
  `fixed-point-P-and-concyclicity-reduction` lemma as a separate entry
  (redundant with the already-certified `amnq` pair). Recommended
  correction for next round: rename `P→Q` and cite `amnq-concyclic-and-
  reduction.md` explicitly in the file. Concyclicity of `A,K,L,Q` (open
  since round 1) remains the load-bearing gap for this route.

**Net for round 19.** No approach reaches `solved`. The population's
closest-to-completion route (`-pointwise-tangent`) made genuine progress
(a new certified sub-lemma) but its remaining gap is now understood to be
identical to — not distinct from — the population's oldest, most
persistent open target (`−q1,−r0`/`T≥0`), now confirmed load-bearing for
*two* independent routes simultaneously. `spiral-similarity-bootstrap`
produced a correct and useful (if more modest than initially framed) new
synthetic fact, with a rediscovery flagged and corrected for accurate
attribution going forward. New lemma certifications this round:
`lemmas/f-positive-on-full-interval.md`,
`lemmas/q-as-foot-of-perpendicular-from-circumcenter.md`. Status remains
`partial`. **Recommended for round 20**: prioritize the `T≥0`/`−q1,−r0`
Positivstellensatz certificate as the single highest-value shared target
(closing it would complete `-pointwise-tangent`'s entire route); for
`spiral-similarity-bootstrap`, fix the `P→Q` attribution and continue
attacking concyclicity of `A,K,L,Q` using the new closed-form
characterization.

### Round 18 — proof-reviewer adjudication

Three built approaches this round. The headline event, again: the builder
of `coordinate-bash-resultant-boundary-pointwise-tangent` marked Status
`solved`, claiming to close **Open gap 6** (`D_1(A)\ge0` on the boundary
curve, the route's sole remaining obstruction per round 17's adjudication)
via a hand-derived exact identity and closed form for `A^\ast`, and
thereby complete the whole `OM=ON` proof. **The Gap-6 closure itself is
genuine and is CERTIFIED** — but the "solved" claim is again **rejected**,
this time for a *different*, previously-unflagged reason found only by
tracing the full dependency chain as the round-18 dispatch explicitly
instructed.

- **`coordinate-bash-resultant-boundary-pointwise-tangent`**: Route
  **CHANGES REQUESTED**, not APPROVE; Status reverts to **`partial`**.
  **Part 1 — Gap 6 is genuinely closed (certified).** Independently
  re-derived, from the raw definitions (`X_0,\beta_0,K_c,P,Q,G`) in a fresh
  `sympy` session (not reusing the builder's script), the identity
  `G_{\mathrm{curve}}(u)=-8\sin u\cos^2u\cdot h(u)$ (`u=A/3+\pi/6`) —
  confirmed exact, zero residual, matching the file's hand-derivation
  term-for-term. Independently re-derived the closed form
  `A^\ast=3\arcsin(\sqrt6/4)-\pi/2` (own fresh `mpmath`, `dps=50`): matches
  the population's standing 40-digit numeric `A^\ast` to all 40 digits;
  confirmed `u^\ast=A^\ast/3+\pi/6\in(\pi/6,\pi/3)` by the same rational
  comparison the file uses, so the cofactor `-8\sin u^\ast\cos^2u^\ast\ne0`
  and `G_{\mathrm{curve}}(A^\ast)=0\Rightarrow h(A^\ast)=0` (fact (ii),
  round 17's missing piece) is a genuine algebraic consequence, not a
  citation to an unproved coincidence. Independently confirmed
  `D_1(A^\ast,B^\ast)=0` to `\approx10^{-42}` from the raw `D_1,\mathrm{RHS}`
  definitions, and spot-checked Steps 1-4's certified `mpmath.iv` sweeps
  (own finite-difference derivative check near `B^\ast$: `\approx4.626`,
  matching the file's certified `\ge4.625`; own dense value sweep on
  `[B^\ast,\pi/3]`: no violation). **Certified
  `lemmas/d1-nonnegative-on-boundary-curve.md` in full** — Open gap 6 is
  closed, a genuine strengthening over round 17's rejected version. **Part
  2 — a new, independent gap found in "Full proof" Step 3.** Per the
  round-18 dispatch's item (f) (trace the entire dependency chain for any
  other silent gap or scope mismatch), the proof-reviewer found that "Full
  proof" Step 3 ("Case (a)", `\beta_1\in(0,\beta_0(A)]`) cites Theorem A of
  `lemmas/claim-I-closed-and-claim-II-caseA-closed.md` (`f(\beta)>0` for
  `\beta\in(\beta_0,\gamma)`) to close a case whose `\beta_1` actually lies
  in the **complementary** interval `(0,\beta_0]` — Theorem A does not
  cover this range. The file's own text flags the mismatch inline ("`G(\beta_1)
  \ge G(\beta_0)` for `\beta_1\le\beta_0` is not directly what's needed")
  and then asserts a reduction to Theorem A without ever justifying it — an
  unproved logical leap, exactly the kind of hand-waving CLAUDE.md's rigor
  rules prohibit. **Independent verification (fresh script, `2{,}000{,}000`
  random `(A,B)$ samples restricted to the file's own Case-(a) domain
  definition):** `G(\beta_1)\ge0` (the quantity Theorem A's machinery is
  built around) is **false in `\approx70\%` of genuine Case-(a) samples**,
  minimum observed `\approx-0.70` — so `G` is not even the correct target
  quantity in Case (a) (consistent with, and explaining, an aside elsewhere
  in this same file that `f`, not `G`, is the relevant quantity in Case
  (a)). Testing `f(\beta_1)>0` instead (the quantity that aside identifies
  as relevant): **zero violations** across the same `2{,}000{,}000` samples,
  minimum `\approx0.616` — so the needed fact is very likely true, but is
  **not established by Theorem A** (wrong sub-interval) **or by any other
  certified lemma anywhere in the population's 18-round history**. A
  plausible fix was identified but not completed: Theorem A's own proof
  already establishes `f'(\beta)>0` on the *whole* interval `(0,\gamma)`
  (not just `(\beta_0,\gamma)`); combined with `f(0)=\sin A(2\sin(A+B)-
  \sin B)`, which an independent `2{,}000{,}000`-sample sweep finds `\ge0`
  throughout the domain (minimum `\approx2\times10^{-6}`, consistent with
  `\ge0` with equality only in a limit) but which **no file in the
  population has proved**, this would extend `f>0` down to all of
  `(0,\gamma)$ and genuinely close Case (a) — but this proof does not exist
  yet. Edited `coordinate-bash-resultant-boundary-pointwise-tangent.md` in
  place (Status header, inline flag at Step 3, new Open gap 7, "Not yet
  promotable" section) and `lemmas/d1-nonnegative-on-boundary-curve.md`
  (Status now Certified, scoped explicitly to Gap 6 only) to record both
  findings precisely, so no future round re-claims "solved" without closing
  Open gap 7, nor re-litigates the now-closed Gap 6. **Net: this route now
  has exactly one open gap (Gap 7, the Case-(a) `f(\beta_1)>0` fact),
  narrower and more precisely located than at any prior round, but the
  route is not solved.**
- **`coordinate-bash-resultant-boundary-pointwise-sos`**: Route **CHANGES
  REQUESTED** (Status `partial` — accurate as filed, no overclaiming). This
  round's three dispatched diagnostic tests on the Gram-matrix degeneracy
  are reported honestly: Test 1 finds a real but witness-dependent
  (not uniform) single-direction explanation for most of the residual
  near-null eigenspace (dominant generator differs between the two tested
  witnesses); Test 2 rules out the round-17-flagged complex-conjugate-pair
  hypothesis via a genuine near-double-real-root finding instead. No
  certificate claimed anywhere in the file; every finding is correctly
  scoped as diagnostic. Not independently re-run in full this round (would
  require standing up the same `cvxpy`/SDP pipeline from scratch), but no
  overclaiming found on inspection.
- **`spiral-similarity-bootstrap`**: Route **CHANGES REQUESTED** (Status
  `partial` — honest, real progress, no overclaiming). First real build of
  this diversity/insurance approach. Independently re-derived, by hand,
  term-for-term, the general one-angle directed-angle lemma (a clean
  algebraic chain-rule argument, no coordinates) and its two applications:
  Lemma A (from H2, giving `\angle BLN=\angle(BK,AC)`) and Lemma B (from
  H3, giving `\angle CKM=\angle(CL,AB)`), then the Corollary combining both
  with H1 to eliminate the free parameter and get `\angle BLN+\angle
  CKM\equiv0\pmod\pi` — every step checked and confirmed correct, a
  genuine new synthetic result with no coordinate elimination anywhere,
  usefully diversifying the population away from the coordinate/resultant/
  SOS cluster (per CLAUDE.md's diversity guidance). The file's own
  disclosure that this does not yet connect to `O,M,N` (the load-bearing
  gap) is accurate and correctly not overclaimed as more than it is.

**Net for round 18.** No approach reaches `solved`. The population's
closest-to-completion route (`-pointwise-tangent`) genuinely closed Gap 6
(certified) but a second, independent gap (Gap 7, Case (a)'s `f(\beta_1)
>0`) was found this round by the dependency-chain audit the dispatch
specifically requested — this is the second round running (17, then 18)
where a `solved` claim on this exact route was investigated and found to
rest on an unproved step; both times the specific unproved step was
different (round 17: an unproved numeric coincidence at the corner; round
18: a wrong-sub-interval citation in Case (a)), and both times the rest of
the round's new content was genuine, certified progress, not a wasted
round. **Recommended for next round**: dispatch specifically at Open gap 7
— prove `f(0)=\sin A(2\sin(A+B)-\sin B)\ge0$ throughout the relevant
domain (strong numeric margin, `\ge2\times10^{-6}` observed, likely an
easy trigonometric argument: `\sin A>0` always, so it reduces to `2\sin
(A+B)\ge\sin B`, i.e. `2\sin C\ge\sin B` using `C=\pi-A-B`, wherever
`\beta_0<\gamma$ makes the domain nonempty), then combine with Theorem A's
already-proved `f'>0` on all of `(0,\gamma)` (not just `(\beta_0,\gamma)`)
to extend `f(\beta)>0` down to the full interval and genuinely close Case
(a). This is a concrete, well-scoped, likely-short target — narrower and
more mechanical than gap 6 was even at its most reduced. New lemma
certification this round: `lemmas/d1-nonnegative-on-boundary-curve.md`
(Gap 6, now genuinely certified). Status remains `partial`.

### Round 17 — proof-reviewer adjudication

Three built approaches this round. The headline event: the builder of
`coordinate-bash-resultant-boundary-pointwise-tangent` marked Status
`solved`, claiming to close **Open gap 6** (`D_1(A)\ge0` on the boundary
curve `\mathcal C`, the route's sole remaining obstruction per round 16's
adjudication) and thereby complete the whole `OM=ON` proof via this route.
**This claim is FALSE and is rejected.** The proof-reviewer traced the
entire dependency chain and independently rebuilt the load-bearing step
from scratch.

- **`coordinate-bash-resultant-boundary-pointwise-tangent`**: Status
  reverts to **`partial`**; Route **CHANGES REQUESTED**, not APPROVE. The
  new lemma `lemmas/d1-nonnegative-on-boundary-curve.md`'s "Step 0"
  (`D_1(B^\ast)=0`, claimed as "a pure algebraic consequence... no
  numerics needed") uses two facts: (i) `G(\beta_0(A^\ast))=0` (genuinely
  certified, `lemmas/star-corner-is-boundary-cusp-not-critical-point.md`)
  and (ii) `(A^\ast,B^\ast)\in\mathcal C_{\mathrm{lo}}`, i.e.
  `X_0(A^\ast,B^\ast)=\cos^2B^\ast`. **Fact (ii) is NOT proved anywhere in
  the population.** It is the same "the two boundary curves meet exactly
  at the corner `(A^\ast,B^\ast)`" observation first reported in round 11
  of this very file — and round 11's own text explicitly discloses it as
  numeric/unproved ("no symbolic derivation... of the coincidence"), a
  disclosure the proof-reviewer's round-11 adjudication (see below,
  preserved) independently confirmed and recorded. No round between 12 and
  16 proved it. The round-17 lemma cites this six-round-old *unproved*
  numeric finding as an "already-certified fact," which is the overclaim.
  **Independent verification (fresh `sympy`/`mpmath`, this round):**
  building the two defining functions from raw definitions —
  `G_{\mathrm{curve}}(A):=G(\beta_0(A),A,\beta_0(A))` (fact (i)'s LHS) and
  `h(A):=X_0(A,\beta_0(A))-\cos^2\beta_0(A)` (fact (ii)'s LHS) — confirms
  they are genuinely different functions (`sympy.simplify` of their ratio
  is a nonconstant function of `A`, evaluating to `\approx-3.08` at
  `A=0.30` vs. `\approx-2.71` at `A=0.90`), so sharing a common root at
  `A^\ast` is a nontrivial fact requiring its own proof, not a free
  algebraic consequence. A from-scratch `mpmath` `dps=80` cross-check
  (independently `findroot`-solving each of `G_{\mathrm{curve}}(A)=0` and
  `h(A)=0` from the same raw definitions) confirms the shared root to 80
  digits (`A_1-A_2\approx5\times10^{-88}`) — extremely strong evidence the
  coincidence is *true*, but this is exactly the same numeric-only status
  it has always had; it is not a proof. Since Step 0 (`D_1(B^\ast)=0`,
  used as the base case anchoring the whole Steps 1-4 MVT-gluing argument)
  rests on this unproved fact, the lemma `lemmas/d1-nonnegative-on-
  boundary-curve.md` is **not a valid proof as written**, and Open gap 6
  is **NOT closed**. All the file's other new-this-round machinery (Step
  1's certified `B^\ast` enclosure, Step 2's derivative-sign sweep, Step
  3's value-sweep away from the corner, Step 4's MVT gluing) is sound
  *conditional on* Step 0 — independently spot-checked and internally
  consistent — but the whole argument is only as strong as its unproved
  anchor. **Steps 1-5 and gap 5's full closure (round 16) remain valid and
  certified** — those are unaffected by this finding (Open gap 5's
  Tgt-positivity closure does not depend on fact (ii) at all, per an
  independent trace of its own proof, which uses a wholly different
  corner `(\pi/3,\pi/3)` with an *exact*, elementary rational verification
  — `X_0(\pi/3,\pi/3)=\cos^2(\pi/3)=1/4`, both sides trivially computable,
  no coincidence involved there). So the route's status is: gap 5 fully
  closed (certified), gap 6 **still open**, with the true remaining gap
  now precisely reduced to "prove `X_0(A^\ast,B^\ast)=\cos^2B^\ast`
  exactly, given `G(\beta_0(A^\ast))=0`" — a sharper, more tractable
  restatement of gap 6 than before this round, since round 17's Steps 1-4
  (the interval-sweep machinery) are reusable verbatim once this one fact
  is closed. **Rejected the lemma's self-declared "Certified" status**;
  edited `lemmas/d1-nonnegative-on-boundary-curve.md` in place to record
  the rejection and the precise missing fact, so no future round re-cites
  it as closed. **Does this affect the "whole problem" question the
  dispatch flagged?** Per the file's own Reduction Lemma (New result 1,
  round 13) and its "Full proof" section, hypothesis (B) (`D_1(A)\ge0` on
  `\mathcal C`) is required together with hypothesis (A) (gap 5, closed)
  to conclude `f\ge g` and hence `OM=ON` via this route. With hypothesis
  (B) not established, the route's "Full proof" section does not
  currently deliver a complete proof, and — separately, and independent
  of this specific bug — even a fully closed `-pointwise-tangent` route
  would only be one of several rival approaches in this population; no
  cross-approach dependency was needed to evaluate this claim since gap 6
  was never actually closed. The correct Status for this whole population
  remains `partial`; nothing here changes that.
- **`coordinate-bash-resultant-boundary-pointwise-sos`**: Route **CHANGES
  REQUESTED** (Status `partial` — accurate as filed, no overclaiming). The
  round's constrained-SDP work (forcing `M_0z(s^\ast)=0`, then also
  `M_0z'(s^\ast)=0`, into the 3-generator SDP) is honestly and precisely
  reported: feasible with `t^\ast` essentially unchanged (a genuine
  complementary-slackness confirmation, not previously built in
  explicitly), but the rank deficiency (5 near-null eigenvalues) is
  **not** relieved even after 2 of the 5 directions are pinned to an exact
  algebraic locus (`s^\ast`, confirmed this round to be a genuine `sympy`
  `\mathrm{CRootOf}` of a degree-16 rational polynomial, not merely a
  5-6-digit float) — 3 directions remain unexplained. The new second
  witness point (`\cos B=3/5,\sin B=4/5,u=7/100`) independently reproduces
  the same qualitative degeneracy pattern (`\approx99.9999999989\%` of the
  near-null eigenspace explained by the `z(s^\ast_2)` direction), a
  genuinely different `B`-slice, strengthening the diagnosis from
  "one-point" to "structural." No certificate is claimed anywhere in the
  file; every result is correctly labeled numeric/diagnostic, and the
  solver-disagreement instance (CLARABEL vs. SCS on the order-2-constrained
  margin) is correctly reported as inconclusive, not as evidence either
  way. No lemma submitted this round (correct — nothing proved).
- **`coordinate-bash-resultant-boundary`**: Route **CHANGES REQUESTED**
  (Status `partial` — accurate as filed, no overclaiming). Independently
  re-derived (fresh `sympy`, own from-scratch reduction modulo
  `\langle c^2+s^2-1,d^2+t^2-1\rangle` via `groebner`/`reduced`, not
  copying the file's script) the round's central structural claims and
  found them **exact, zero residual**: (1) the decomposition `H=ct\,P_H+
  sd\,Q_H` for both `G_0` and `\mathrm{Num}` (own fresh derivation,
  matches the file's `P_{G_0},Q_{G_0},P_{\mathrm{Num}},Q_{\mathrm{Num}}`
  term-for-term); (2) the parity claims `(s\cdot G_0)_{00}=(t\cdot
  G_0)_{00}=0` and `(c\cdot G_0)_{00}=(1-\sigma)t(2\tau-1)` (own
  from-scratch four-way sign-projector implementation, exact match); (3)
  the new generator `\mathrm{NewGen}(G_0,G_0):=[(cd\cdot G_0^2)^2]_{00}`
  — independently rebuilt from the raw `c,s,d,t` definition of `G_0`
  (own projector, own reduction, no reuse of the file's intermediate
  forms), matches the file's displayed degree-10 `(\sigma,\tau)`
  polynomial **exactly** (zero residual after full expansion), and an
  independent `2{,}000{,}000`-sample sweep over `(\sigma,\tau)\in[0,1]^2`
  confirms it is nonnegative there (`\min\approx8\times10^{-16},\ \max
  \approx2.37`, matching the file's own reported range). This is genuine,
  independently-verified new mathematical content: a real, unconditionally
  nonnegative generator family, and a real, exact proof (not a search
  failure) that bare single-variable multipliers cannot work. Correctly
  and honestly scoped as not yet closing the LP (degree 10-17 vs. the
  target's degree 6-7) — no overclaiming. Central `-q_1,-r_0` certificate
  still not found. No regression.

**Net for round 17.** No approach reaches `solved`; the population's
closest-to-completion route (`-pointwise-tangent`) attempted to close its
final gap but the closure is invalid — **this is the most important
finding of the round**: an unproved numeric coincidence (known to be
unproved since round 11, six rounds ago) was mis-cited as an
"already-certified fact" to manufacture an exact-algebra proof where none
exists. The true state of that route is unchanged in substance from round
16 (gap 5 closed, gap 6 open), but gap 6 is now more precisely stated:
prove `X_0(A^\ast,B^\ast)=\cos^2B^\ast` exactly, where `A^\ast` is pinned
by `G(\beta_0(A^\ast))=0` — a single scalar identity between two
`A^\ast`-defining trigonometric equations, likely provable via a resultant/
elimination argument in `A` alone (both equations are functions of `A`
only, via `\beta_0(A)=(\pi-A)/3`) even though no round has yet found it.
**Recommended for next round**: dispatch specifically at this one sharpened
fact — an elimination-theoretic (not numeric) proof that
`G_{\mathrm{curve}}(A)=0` and `h(A):=X_0(A,\beta_0(A))-\cos^2\beta_0(A)=0`
share their common real root, e.g. via a resultant of the two (after a
Weierstrass substitution `w=\tan(A/2)` reduces both to polynomials in `w`)
having a repeated/shared factor, or via computing `\gcd` of their minimal
polynomials over `\mathbb Q` (both `A^\ast$ values agree to 80+ digits, so
if each equation's root is algebraic, they may share an exact minimal
polynomial factor extractable by computer algebra). This is a concrete,
well-scoped, likely-tractable target — the same style of gap-sharpening
that closed gap 5 over rounds 13-16. No lemma certified this round (the
one candidate, `d1-nonnegative-on-boundary-curve.md`, is **rejected** and
annotated in place with the precise gap). No regressions in the other two
approaches; both made genuine, independently-verified progress (a
confirmed structural fact, `\mathrm{NewGen}`, in `-boundary`; a confirmed
second-witness-point diagnostic in `-sos`). Status remains `partial`.

### Round 16 — proof-reviewer adjudication

Three built approaches this round, all **CHANGES REQUESTED** (real,
independently-verified progress; no overclaiming; no APPROVE). The
proof-reviewer independently rebuilt every load-bearing new claim from
scratch (own fresh `sympy`/`mpmath` sessions), with particular focus on
the round's headline item (the near-corner gluing gap closure) and the
sign-error fix.

- **`coordinate-bash-resultant-boundary-pointwise-tangent`**: the round's
  headline claim — an exact Taylor identity with a certified
  Lagrange-remainder bound giving `Tgt(A,B)-Tgt(\pi/3,\pi/3)\ge
  3.46\,\varepsilon>0` throughout `\bar{\mathcal D}\cap\{0<\varepsilon\le
  0.01\}` (`\varepsilon:=\pi/3-A`), gluing with round 15's 2-D adaptive
  sweep to give `\mathrm{Tgt}\ge\mathrm{Tgt}(\text{corner})>0` everywhere
  on `\bar{\mathcal D}$ — is **independently re-verified in full**. Own
  fresh `mpmath` (50-dps) rebuild of `\mathrm{Tgt}(A,B)` directly from the
  raw `X_0,\beta_0,K_c,P,Q,G,\mathrm{RHS},D_2,T_1` definitions (not copied
  from the file) reproduces `\mathrm{Tgt}(\pi/3,\pi/3)=
  1.5741362248140625772265\ldots` to all displayed digits, and the
  gradient values `g_A=-4.28096012358944774419\ldots,\ g_B=
  -1.55725707997121221899\ldots` (central finite differences at
  `h=10^{-20}`, 50-dps) match the file's certified `mpmath.iv` intervals
  to every displayed digit — confirming `\delta_{\min}=-g_A+\tfrac12g_B
  \approx3.50233158360384163` exactly. Own fresh `sympy` symbolic
  differentiation confirms `A'(\pi/3)=4` **exactly** (the domain-safety
  argument's key fact) and confirms Theorem A's closed-form
  parametrization of `\mathcal C_{\mathrm{lo}}` (`\tan A=-\sin B\cos(2B)/
  (2\cos^3B)`) satisfies `X_0-\cos^2B\equiv0` identically (own
  substitution-and-simplify, residual `0`). The certified second-derivative
  bound `F_t''(\xi)\in[-6.64,6.13]` on the box `e\in[0,0.01],t\in[-0.3,0.5]`
  was independently corroborated (not re-certified with interval
  arithmetic, but a dense `41\times41` high-precision finite-difference
  scan over the same box finds a true range `\approx[-5.39,4.72]`,
  comfortably inside the file's claimed enclosure, exactly the expected
  relationship between a sampled true range and a valid outer interval
  enclosure). The final arithmetic
  `q(\varepsilon,t)\ge3.50233158360384163-\tfrac{0.01}2\times6.6415863089
  =3.46912\ldots>0` was independently recomputed and confirmed. **This is
  a genuine, rigorous closure of Open gap 5** (the near-corner residual
  region round 15's interval sweep could not resolve at a point of exact
  equality) — the near-corner value-vs-derivative Taylor technique
  correctly sidesteps the degeneracy that defeated a raw quotient-of-
  intervals sweep. Certified `lemmas/tgt-strictly-positive-throughout-D-
  full.md` **in full** (the file's own honest scope caveat — that this
  closes gap 5 only, and Open gap 6, `D_1(A)\ge0` on the boundary curve
  `\mathcal C`, inherited unproved from the `-twopoint` sibling, remains
  fully untouched — is accurate and not overclaimed). This reduces the
  whole approach's outstanding obligations, per its own Reduction Lemma
  (New result 1, round 13), to **exactly one** remaining hypothesis
  (gap 6) — the narrowest any approach in this population's history has
  come to a complete proof. Route: **CHANGES REQUESTED** (Status `partial`
  — real, certified progress; gap 6 is a wholly separate, still-open
  fact, so the approach is not solved).
- **`coordinate-bash-resultant-boundary-pointwise-sos`**: the round's
  exact rational witness point construction (`r=\tan(B/2)=7/10\Rightarrow
  (\cos B,\sin B)=(51/149,140/149)$, `u=93/1000`) is **independently
  re-verified**: own `sympy.Rational` check that `(1-r^2)/(1+r^2)=51/149`
  and `2r/(1+r^2)=140/149` exactly for `r=7/10`. The reported obstruction
  (`\sigma_0`'s Gram matrix forced to near-exact rank deficiency,
  `t`-independent, confirmed by re-optimizing the joint PSD margin at
  `t\in\{0,2,5,7,7.816\}` and by a decisively-infeasible rank-13
  explicit-SOS attempt) is an SDP-solver diagnostic not independently
  re-run this round (would require standing up the same `cvxpy`/CLARABEL
  pipeline from scratch on a `\approx35`-coefficient degree-34 target — a
  substantial undertaking not repeated here), but the report is
  **internally consistent and honestly scoped**: no certificate is
  claimed, the negative finding is precisely diagnosed (not merely
  "solver failed"), and Sub-goal B's deferral is justified, not a silent
  drop. No lemma submitted or certified this round (correctly — nothing
  proved). Route: **CHANGES REQUESTED** (Status `partial` — a real,
  precisely-diagnosed negative finding, no overclaiming, no regression).
- **`coordinate-bash-resultant-boundary`**: the round's central claim —
  that the round-15 sign error in `B_{G_0N}` is fixed, with the
  correctly-signed generator being `(G_0\cdot\mathrm{Num})_{00}` (not
  `(G_0\cdot(-\mathrm{Num}))_{00}`) — is **independently re-derived from
  scratch and confirmed exactly**: own fresh `sympy` session, rebuilding
  `G_0:=ct(1-2d^2)-2sd^3` and the certified `\mathrm{Num}` from their raw
  definitions, computing `G_0\cdot\mathrm{Num}$, applying the `(0,0)`-parity
  projector `\tfrac14[f(c,d)+f(-c,d)+f(c,-d)+f(-c,-d)]` and reducing modulo
  `c^2=1-s^2,\,d^2=1-t^2`, then substituting `\sigma:=s^2,\tau:=t^2`, gives
  `-32\sigma^3\tau^3+56\sigma^3\tau^2-30\sigma^3\tau+4\sigma^3+32\sigma^2
  \tau^3-50\sigma^2\tau^2+27\sigma^2\tau-4\sigma^2-2\sigma\tau^3-5\sigma
  \tau^2+3\sigma\tau+2\tau^3-\tau^2` — matching the file's displayed
  corrected `B_{G_0N}` **term for term**. Independently re-confirmed
  positive on the claimed domain box (own `200{,}000`-sample sweep over
  `\sigma\in(0.1568,0.2610),\tau\in(0.6253,0.7859)`: range
  `\approx(0.0097,0.1303)`, comfortably `>0` throughout, consistent with —
  and, as expected for a box superset of the true curved domain, slightly
  wider than — the file's own reported `(0.0121,0.0784)`). The LP/SDP
  re-runs and the CLARABEL-vs-SCS eigenvalue-artifact catch are plausible
  and consistent with the file's own internal accounting (not independently
  re-run this round — would require standing up the same `cvxpy` SDP
  pipeline — but no overclaiming found: every negative result is reported
  as "no certificate found," never as "certificate found," and the two
  solver-scaling-inconclusive instances are correctly flagged as
  inconclusive, not negative). No new lemma submitted or certified this
  round. Route: **CHANGES REQUESTED** (Status `partial` — a genuine,
  independently-confirmed bug fix plus honestly-reported continued
  negative search; no regression, no overclaiming).

**Does closing gap 5 meaningfully change the population's closest-to-
completion status? Yes.** Before this round, every live approach had at
least two substantial, structurally distinct open sub-targets. After this
round, `coordinate-bash-resultant-boundary-pointwise-tangent`'s route (via
its round-13 Reduction Lemma) has exactly **one** remaining obstruction —
`D_1(A)\ge0` on the boundary curve `\mathcal C=\{X_0=\cos^2B\}`, inherited
unproved from the `-twopoint` sibling (`lemmas/star-factorization-on-
boundary-curve.md`: `D_1$ vanishes exactly at the corner, is `\approx0.4054`
at its numerically-observed interior maximum, and is concave on `\approx90\%`
of sampled points, but concavity/global nonnegativity is not proved). This
is now the single sharpest, most nearly-complete route in the population's
history — closing `D_1(A)\ge0` on this one curve (a genuinely more tractable
1-variable target than anything the route has needed before) would complete
the *entire* problem via this approach. **Recommended for next round**:
prioritize dispatching effort specifically at gap 6 (`D_1(A)\ge0` on
`\mathcal C`) — either reviving the `-twopoint` sibling's own dormant
concavity argument, or applying this round's newly-demonstrated
Taylor-with-certified-Lagrange-remainder technique (which cleanly handled
an analogous equality-point degeneracy for `\mathrm{Tgt}`) to `D_1$ directly.
No regressions this round; the other two approaches' honest negative/
diagnostic findings (SDP degeneracy in `-sos`, continued LP/SDP infeasibility
in `-boundary`) further narrow (without yet ruling out) their own
independent routes. Status remains `partial`. New lemma certification this
round: `lemmas/tgt-strictly-positive-throughout-D-full.md`.

### Round 15 — proof-reviewer adjudication

Three built approaches this round, all **CHANGES REQUESTED** (real
progress; no APPROVE). The proof-reviewer independently rebuilt every
load-bearing new claim from scratch (own fresh `sympy`/`mpmath`/`numpy`
sessions).

- **`coordinate-bash-resultant-boundary-pointwise-tangent`**: independently
  re-verified Theorem A (`\mathcal C_{\mathrm{lo}}`'s exact closed-form
  parametrization `\tan A=-\sin B\cos(2B)/(2\cos^3B)`, own `sympy.nsolve`
  cross-check, exact match), the corner value
  `\mathrm{Tgt}(\pi/3,\pi/3)=1.57413622481406257722651370062\ldots` (30
  digits, own fresh `sympy` session, matches exactly, confirms the file's
  correction of a stale round-13/14 citation) and `T_1(\pi/3,\pi/3)=0`
  exactly (own `sympy.simplify`). Independently reproduced (own
  high-precision `mpmath` dense sampling, not the file's `mpmath.iv`
  directed-rounding method, but corroborating it) both Theorem B
  (`\mathrm{Tgt}\ge\mathrm{Tgt}(\text{corner})` on `\mathcal C_{\mathrm{hi}}$,
  `A\in[0.5,\pi/3)`) and Theorem C (same on `\mathcal C_{\mathrm{lo}}`,
  `B\in[0.9,\pi/3)`): own 2000-point dense scans of each curve find the
  minimum exactly at the corner in both cases, matching to 30 digits — no
  violation found, consistent with the file's claimed `0`-bad-sub-interval
  certified result. Both new lemmas (`clo-closed-form-parametrization.md`,
  `tgt-ge-corner-on-both-boundary-curves.md`) are correctly scoped (explicit
  caveats that the interior/near-corner region remains open) and
  **certified**. The file's own Status (`partial`) is accurate: the
  near-corner residual neighbourhood of the 2-D interior sweep is honestly
  disclosed as unresolved (an inherent limitation of finite-width interval
  arithmetic at a point of equality), and this is correctly not claimed as
  closed.
- **`coordinate-bash-resultant-boundary`**: independently re-derived the
  three new degree-6/6/8 `(0,0)`-graded product generators `B_{G_0E},
  B_{G_0N},B_{EN}$ from the raw certified `G_0,E_{\mathrm{num}},\mathrm{Num}`
  definitions (own fresh `sympy` session, `Groebner`-free direct ideal
  reduction + sign-projector) — all three closed forms match the file
  exactly (zero residual). **However, independently sampling the true
  residual domain (own domain-membership test built directly from the same
  four raw inequalities `G_0>0,E_{\mathrm{num}}<0,\mathrm{Bc}\ge0,
  \mathrm{Num}<0`, `4{,}000{,}000`-sample sweep, `8{,}000+` domain points,
  `\sigma,\tau`-range matching the file's own claimed window almost
  exactly) finds `B_{G_0N}=(G_0\cdot(-\mathrm{Num}))_{00}` is
  UNIFORMLY NEGATIVE on the domain (`0/8793` samples positive; range
  `\approx(-0.079,-0.012)`), the OPPOSITE sign of the file's claim
  `B_{G_0N}\in(0.0121,0.0789)>0`.** The negated quantity `-B_{G_0N}=
  (G_0\cdot\mathrm{Num})_{00}` matches the file's claimed positive range
  digit-for-digit. This is a clear, confirmed **sign error** in the file's
  round-15 §2/§7 sign-definiteness claim for one of its three new
  generators (a genuine bug, not a borderline numeric-tolerance issue,
  independently reproduced at both a single hand-picked domain point via
  exact symbolic averaging and a `4M`-sample sweep). `B_{G_0E}` and
  `B_{EN}` are correctly confirmed positive (own independent sweep matches
  the file's claimed ranges almost exactly). This error propagates into
  item 4's LP/rank tables (`B_{G_0N}` was used there as an assumed-positive
  generator) — those specific rows should be re-derived using the
  correctly-signed `-B_{G_0N}=(G_0\cdot\mathrm{Num})_{00}` next round; the
  file's ultimate conclusion ("no certificate found, still `partial`") is
  unaffected in substance, since the certificate search failed regardless,
  but the claimed evidence for `B_{G_0N}`'s role is wrong as written. **Not
  certified as a lemma** (correctly, the file did not write a separate
  `lemmas/` file for this — flagged here so it is fixed, not re-submitted,
  next round).
- **`coordinate-bash-resultant-boundary-pointwise-sos`**: independently
  re-verified Theorem 4 (`n_4\ge0\iff n4sq\ge0$, the plain-polynomial
  `w`-elimination) in full — own `sympy` check that
  `(w^3\cos B)^2-(u(3-u^2))^2$ with `w^2\to1+u^2` substituted equals
  `n4sq:=(1+u^2)^3\cos^2B-u^2(3-u^2)^2` exactly (residual `0`), and
  independently confirmed the two elementary sign facts it rests on
  (`\cos B>0` from `B\le C$ and the angle sum; `u(3-u^2)>0` from
  `u=\tan(A/6)\in(0,\tan(\pi/12)]=(0,2-\sqrt3]$, and `\mathrm{sympy}`
  confirms `\tan(\pi/12)=2-\sqrt3` exactly). This theorem is fully,
  rigorously proved, case-free, no gaps — **certifiable**. The round's SDP
  evidence (Parts 3-4, clean two-solver convergence at four witness points)
  is honestly and correctly reported as strong numeric support, NOT a
  proof (no exact rational Gram matrix extracted; only pointwise, not the
  joint multivariate Positivstellensatz needed). No overclaiming found;
  Status `partial` is accurate.

**No regressions.** Two lemmas certified this round
(`clo-closed-form-parametrization.md`,
`tgt-ge-corner-on-both-boundary-curves.md`); Theorem 4 in the `-sos` file is
fully proved and reusable but the file did not submit a separate
`lemmas/` file for it this round (recommend it do so next round — flagged
in the individual approach's build-set guidance, not certified here since
no file was presented for certification). One concrete, load-bearing sign
error was caught and must be corrected in
`coordinate-bash-resultant-boundary` next round (`B_{G_0N}`'s claimed sign
is backwards; the correctly-signed generator is `-B_{G_0N}=(G_0\cdot
\mathrm{Num})_{00}>0`). Status remains `partial`.

### Round 14 — proof-reviewer adjudication

Three built approaches this round, all **CHANGES REQUESTED** (real,
independently-verified progress; no overclaiming; no APPROVE). The
proof-reviewer independently rebuilt every load-bearing new claim from
scratch (own fresh `sympy`/`mpmath` sessions), with particular focus on the
three dispatch-flagged headline items.

- **`coordinate-bash-resultant-boundary`**: independently re-derived all six
  `(0,0)`-graded degree-matched basis elements `B₁,…,B₆` from the raw
  definitions (own `sympy` reduction + parity projector) — `B₁`–`B₅` match
  the explorer's report exactly, and the builder's **correction** of `B₆`
  (true value `2σ²(σ-1)(τ-1)(4τ-1)`, not the explorer's erroneous
  `2σ²(σ-1)(τ-1)(2τ-1)(2τ+1)`) is confirmed exactly (zero residual).
  Independently re-ran the smallest natural exact linear ansatz using the
  three sign-definite basis elements `B₁,B₄,B₆` — confirmed infeasible
  (`sympy.linsolve` empty set), matching the builder's honest negative
  finding. The central `-q₁,-r₀` Positivstellensatz certificate is **still
  not found**. Certified `lemmas/parity-basis-b1-b6-corrected.md`.
- **`coordinate-bash-resultant-boundary-pointwise-tangent`**: independently
  re-derived `D₂(π/3,π/3)` from the *raw* trigonometric definitions
  (`K_c,P,Q,β₀`, own fresh 50-digit `mpmath` session, not the file's
  simplified closed form) and got exact agreement to 50 digits with the
  file's value `-0.836430570888798…`, confirming `D₂(π/3,π/3) ≤ -0.8 < 0`
  is correct — this is a genuinely rigorous, hand-checkable rational bound
  (Taylor + Lagrange remainder + Archimedes' `π` bound), the strongest-rigor
  result of the round. Independently reproduced the gradient values
  `g_A≈-4.2810, g_B≈-1.5573` at the corner via central finite differences
  (own script, matching the file's `mpmath.iv` interval to 10+ digits) and
  verified the tangent-cone directional-derivative argument (min directional
  derivative `≈3.502>0` over `t∈[-1/4,1/2]`) is arithmetically sound, hence
  the strict-local-minimum claim (New result 9) is verified. **Global**
  minimality over the whole domain remains open, honestly disclosed as not
  proved (numeric-only, `2M`-sample sweep, no counterexample). Certified
  `lemmas/d2-corner-value-strictly-negative.md`.
- **`coordinate-bash-resultant-boundary-pointwise-sos`**: this round's most
  decisive claim — the exact `ℚ(√3)` counterexample `u=1/4` at a rationalized
  witness `B` (`cosB=808976/2721665, sinB=2598657/2721665`), showing
  `n₁>0, n₂>0, Num<0` simultaneously, hence proving unconditionally that no
  2-generator (`n₁,n₂`-only) Positivstellensatz certificate for `Num≥0` can
  exist at any degree — **independently re-derived from scratch** (own fresh
  `sympy` session, rebuilding `X₀, RHS, Num, n₁, n₂` from the raw
  trigonometric/Weierstrass definitions, not from the file's displayed
  polynomials) and matched exactly: `Num(1/4,·)≈-0.0008596575524743493`,
  `n₁≈1.2685616043314354>0`, `n₂≈0.03232250009949713>0`, and (separately)
  `n₄(1/4,·)≈-0.4088<0`, confirming this witness lies outside the `n₄≥0`
  sub-domain. This is a genuine, fully rigorous resolution of a real
  cross-round contradiction (round 13's SDP infeasibility vs. a round-14
  explorer's SDP "feasibility" claim), correctly resolved in round 13's
  favor. The central gap (`Num≥0` on the true, `n₄`-including domain) remains
  open. Certified `lemmas/n1n2-minimal-ansatz-unconditionally-infeasible.md`.

**No regressions, no overclaiming found in any of the three approaches.**
Status remains `partial`. The population continues to narrow its shared
branch-selection/Positivstellensatz core along three related but distinct
formulations, each with a specific, precisely-stated open sub-target (see
each approach file's "Open gaps"/"Net assessment" sections).

### Round 13 (this round) — proof-reviewer adjudication

Three built approaches this round: `coordinate-bash-resultant-boundary`
(new parity-obstruction theorem plus two closed sub-items), `coordinate-
bash-resultant-boundary-pointwise-tangent` (`f-g` reformulation,
eliminates the `\mathrm{RHS}>0` sub-target), and `coordinate-bash-
resultant-boundary-pointwise-sos` (Theorem 2: `\angle B\le\angle C` via
`w=\sqrt{1+u^2}`, plus a sharpened SDP infeasibility study). All three are
**CHANGES REQUESTED** (real, independently-verified progress; no
overclaiming; no APPROVE). The proof-reviewer independently rebuilt every
load-bearing new symbolic claim from scratch (own fresh `sympy`/`numpy`/
`mpmath` sessions), with particular focus on the round's headline novel
claim (the `\mathbb Z_2\times\mathbb Z_2` parity obstruction) and the two
other dispatch-flagged items.

- **`coordinate-bash-resultant-boundary`**: (1) the `\mathrm{Num}` identity
  (`q^2(1-X_0)-p^2X_0=\mathrm{Num}/(2(ct+ds)^3)`) is **independently
  re-verified exactly** (own fresh `sympy` session, `together`/`fraction`,
  zero residual against the file's displayed `\mathrm{Num}`); certified
  `lemmas/num-identity-exact-squaring-equivalence.md`. (2) The `B<\pi/2`-
  conditioned `B\le C\iff c\ge2t^2-1` fix is elementary and correctly
  scoped (precondition made explicit, discharged by the already-certified
  round-11 margin fact). (3) **The round's headline new result — a
  `\mathbb Z_2\times\mathbb Z_2` grading argument proving that any
  Positivstellensatz certificate for `-q_1,-r_0` built from `\{G_0,
  -E_{\mathrm{num}},\mathrm{Bc},-\mathrm{Num}\}` must use a multiplier with
  an explicit bare odd power of `c` or `d` — is independently re-derived in
  full**: own from-scratch implementation of the four sign-projectors,
  confirming every claimed graded component (`(G_0)_{00}=(G_0)_{11}=0`,
  same for `E_{\mathrm{num}},\mathrm{Num}$; `(\mathrm{Bc})_{00}=1-2t^2,
  (\mathrm{Bc})_{10}=c`) exactly, plus hand-verification that the
  elementary collapse argument (`\lambda\in R_{00}\Rightarrow`
  contribution `0`) is sound. This is genuinely new, rigorous machinery —
  a first grading/parity argument in this population's history — correctly
  scoped as a *necessary condition* on certificate structure, not a claim
  that no certificate exists. Certified
  `lemmas/parity-obstruction-q1-r0-certificate.md`. Items 4-5 (a concrete
  candidate probe, a rectangular-relaxation negative finding) are honest
  negative/inconclusive findings, not overclaimed. The central target
  (`-q_1,-r_0` Positivstellensatz certificate) remains open.
- **`coordinate-bash-resultant-boundary-pointwise-tangent`**: the `f-g`
  reformulation's two new exact identities — `f-g|_{\mathcal C}=D_1`
  (New result 2) and the radical-free `T_1` factorization (New result 3,
  feeding the `\mathrm{Tgt}` target, New result 4) — are **independently
  re-verified exactly** (own fresh `sympy` sessions, zero residual in both
  cases, rebuilt from the raw `X_0,\beta_0,K_c,P,Q,\mathrm{RHS}`
  definitions, not copied from the file). The Reduction Lemma (New result
  1, eliminating the previously-open `\mathrm{RHS}>0`-unconditionally
  sub-target from the critical path) is checked by hand and is a correct,
  genuine simplification of the outline's roadmap. The domain-
  connectedness/sign-determination device (New result 5) is standard,
  correctly-applied real analysis (implicit continuity + IVT), no gap
  found. The two remaining hypotheses — `\mathrm{Tgt}(A,B)>0` throughout
  `\mathcal D` (strong numeric margin `\approx1.574`, symbolic collapse
  honestly reported as incomplete, not falsely claimed) and `D_1(A)\ge0`
  on `\mathcal C` (the sibling's own open target) — are correctly left
  open, not conflated with proved content. Certified
  `lemmas/f-minus-g-reduction-and-t1-factorization.md`, restricted exactly
  to the file's own scoping (Theorems 1-7 certified; hypotheses (A),(B)
  explicitly excluded).
- **`coordinate-bash-resultant-boundary-pointwise-sos`**: Theorem 2 (the
  `w=\sqrt{1+u^2}` polynomial encoding of `\angle B\le\angle C`,
  `n_4:=w^3\cos B-u(3-u^2)\ge0`) is **independently re-verified in full**:
  the underlying triple-angle identity `\sin(3t)=u(3-u^2)/w^3` confirmed
  both symbolically (own `sympy` reduction modulo `w^2=1+u^2`, residual
  `0`) and to 30-digit numeric precision (`mpmath`), and the full `B\le
  C\iff n_4\ge0` equivalence independently reconfirmed at `375{,}037`
  fresh random samples with **zero** mismatches (own script, own domain
  construction, not reusing the file's `u,w` machinery). This closes the
  round-12-flagged prerequisite exactly as intended — a fully rigorous,
  unconditional theorem. Certified
  `lemmas/angle-b-le-c-weierstrass-encoding.md`. The point-localized SDP
  infeasibility study (dispatch-flagged item) is correctly and
  consistently disclosed throughout as numeric-only (solver output at
  specific witness points), with the file's own stated logical asymmetry
  (infeasibility at one point kills a global minimal-degree certificate;
  feasibility at one point proves nothing globally) being sound reasoning
  about Positivstellensatz certificates — not independently re-run this
  round (inherently a numerical-optimization claim, out of scope for a
  from-scratch symbolic rebuild), but no overclaiming found in how it is
  reported. The central target (`\mathrm{Num}\ge0`, equivalently
  `(\star)`) remains open.

**Net for round 13.** No approach reached `solved`. All three made real,
independently-verified progress: `coordinate-bash-resultant-boundary`
closed two previously-flagged sub-items exactly as directed and produced a
genuinely new structural theorem (the parity obstruction) explaining why a
whole class of certificate ansätze cannot work; `coordinate-bash-
resultant-boundary-pointwise-tangent` eliminated an entire previously-open
sub-target (`\mathrm{RHS}>0` unconditionally) via a cleaner reformulation,
reducing its route to two clean numeric-margin targets; `coordinate-bash-
resultant-boundary-pointwise-sos` closed its own previously-flagged
prerequisite (the `\angle B\le\angle C` polynomial encoding) with a fully
rigorous theorem and sharpened its SDP diagnostic picture. **A shared
pattern is now visible across all three routes**: each has narrowed to a
single explicit polynomial/trigonometric-polynomial positivity claim with
strong numeric margin but no symbolic proof (`-q_1,-r_0<0` for
`coordinate-bash-resultant-boundary`; `\mathrm{Tgt}>0` for
`-pointwise-tangent`; `\mathrm{Num}\ge0` via a 4-generator
Positivstellensatz for `-pointwise-sos`) — this is the same shared-gap
pattern flagged in prior rounds; if it persists another 2-3 rounds without
a symbolic closure, the outliner should consider a genuinely different
framing rather than another variation of "collapse to one inequality, try
SOS/Positivstellensatz on it." Status remains `partial`. New lemma
certifications this round: `lemmas/num-identity-exact-squaring-
equivalence.md`, `lemmas/parity-obstruction-q1-r0-certificate.md`,
`lemmas/f-minus-g-reduction-and-t1-factorization.md`,
`lemmas/angle-b-le-c-weierstrass-encoding.md`.

### Round 12 (preserved) — proof-reviewer adjudication

Four built approaches this round: `coordinate-bash-resultant-boundary`
(splices in q1r0lens's β1-elimination), `coordinate-bash-resultant-
boundary-pointwise-tangent` (T1/T2 decomposition of ∂S/∂B),
`coordinate-bash-resultant-boundary-pointwise-tangent-twopoint` (new
copy; D1·D2 factorization on the boundary curve), and
`coordinate-bash-resultant-boundary-pointwise-sos` (Theorem 1: exact
Weierstrass-denominator positivity). All four are **CHANGES REQUESTED**
(genuine, independently-verified progress; no overclaiming; no APPROVE).
The proof-reviewer independently rebuilt every load-bearing new symbolic
claim from scratch in fresh `sympy`/`numpy`/`scipy` sessions (never
trusting a builder's own "sympy confirms" report), with particular focus
on the four claims flagged by the dispatch.

- **`coordinate-bash-resultant-boundary`**: the new exact reformulation
  of Step 4 — `X_0>1/4\iff ct>sd` and `X_0<3/4\iff ct+3sd>0` (via
  `X_0-\tfrac14=(ct-sd)/(4\sin C)`, `X_0-\tfrac34=-(ct+3sd)/(4\sin C)`,
  `\sin C=sd+ct>0` unconditionally) — is **independently re-verified
  exactly** (own fresh `sympy` session, `sympy.simplify` of both
  differences against the closed forms gives `0` identically). The
  file's honest finding that Steps 2/4 closure alone would **not** close
  the residual gap (Step 4 only converts the domain description to a
  polynomial one; the actual `q_1<0,r_0<0` target is untouched) is
  logically sound and correctly disclosed, not overclaimed. The
  supporting negative-implication numerics (`X_0>d^2` alone does not
  imply `ct>sd`, `\approx5.5\%` violation) were **independently
  reproduced** via a from-scratch 2,000,000-sample script (own domain
  construction, own random seed): `\approx5.6\%` violations, matching
  closely. Certified `lemmas/x0-quarter-threshold-reformulation.md`
  (the exact identity only — not the still-open joint-domain claim,
  which is not a proved lemma).
- **`coordinate-bash-resultant-boundary-pointwise-tangent`**: the new
  closed form (D2) for `\partial\mathrm{RHS}/\partial B` and the
  decomposition `\partial S/\partial B=T_1+T_2` (D3) are **independently
  re-verified exactly** (own fresh `sympy` session: symbolic
  differentiation of `RHS` and `S` w.r.t. `B` at fixed `A` matches the
  displayed closed forms exactly, and the reported sample point
  `(A,B)\approx(0.603,1.269)` reproduces `T_1\approx-0.589,T_2\approx
  0.766,T_1+T_2\approx0.177`, matching to the file's own precision). The
  claims `\mathrm{RHS}>0` and `\partial_B\mathrm{RHS}<0` throughout the
  exact domain `\mathcal D` are **independently reproduced** (own
  354,900-sample sweep, `0` violations, minima `\approx0.315` and
  `\approx-0.797` respectively). **One imprecision found and flagged**:
  the file states `T_1` is "NOT sign-definite," citing only negative
  values; this round's independent 2,000,000-sample sweep restricted to
  `\mathcal D` found `T_1<0` at **every** sampled point (max observed
  `\approx-0.0006`, i.e. consistently negative, not oscillating) — so
  the more accurate statement is "`T_1` is not proved `\ge0`, and appears
  consistently `<0`," not literally "sign-indefinite." This does not
  change the substantive conclusion (the naive termwise split still
  fails, since `T_1` is never observed `\ge0`), so the file's Status and
  its use of the finding are not affected, but the wording should be
  corrected next round. Certified
  `lemmas/rhs-partial-b-derivative-and-decomposition.md` (D2+D3, with
  the corrected characterization of `T_1` noted as a caveat).
- **`coordinate-bash-resultant-boundary-pointwise-tangent-twopoint`**
  (new): the new difference-of-squares factorization `S=D_1D_2` on the
  boundary curve `\mathcal C=\{X_0=\cos^2B\}` is **independently
  re-verified exactly** (trivial but correct: substituting `X_0=\cos^2B`
  makes `(1+\cos B)^2X_0` a perfect square, `sympy` residual `0`). The
  numeric claims about `D_1,D_2` along `\mathcal C` are **independently
  reproduced** via an own fresh `scipy.optimize.brentq` root-find of the
  curve at 3000 sample `A`-values: `D_2` ranges `\approx1.968\to1.135`
  (file: `1.975\to1.102`, matching trend and order of magnitude
  closely), `D_1` vanishes only at the corner, rises to a maximum
  `\approx0.4054` near `A\approx0.979` (exact match to the file's
  reported max and location), and second-difference is negative at
  `\approx90\%` of interior points (file: `1802/1998\approx90.2\%`,
  matching almost exactly). The concavity/unimodality claim needed to
  complete the secant-line argument remains honestly unproved (only this
  numeric evidence). The three explicitly-listed open gaps (`D_2>0`
  unproved, `D_1` concavity unproved, and the file's own honest
  disclosure that even both together would only settle `S\ge0` **on**
  `\mathcal C`, not the full domain, still needing the sibling's
  monotonicity lever) are accurate and not overclaimed. Certified
  `lemmas/star-factorization-on-boundary-curve.md`.
- **`coordinate-bash-resultant-boundary-pointwise-sos`**: the round's
  headline claim, Theorem 1 (`h(u,\cos B,\sin B)=-(1+u^2)^3\sin(A+B)`,
  and consequently `\mathrm{Den}=16(1+u^2)^{17}\sin(A+B)`,
  `\mathrm{den}_1=4(1+u^2)^5\sin(A+B)`, `\mathrm{den}_2=2(1+u^2)^3
  \sin(A+B)`, all unconditionally positive for a genuine triangle) — is
  **independently re-verified in full, from scratch, including a full
  independent re-derivation of the `\mathrm{Den}` computation the file
  itself did not display in complete symbolic detail**. Own fresh
  `sympy` session: (i) confirmed `h=-(1+u^2)^3\sin(A+B)` exactly (own
  `sympy.together`/`sympy.expand`, residual `0`); (ii) confirmed
  `\mathrm{den}_1` (from `n_1=\cos^2\beta_0-X_0`, own re-derivation of
  `\cos\beta_0,\sin\beta_0` in terms of `x,y` via
  `\beta_0=\pi/3-A/3`) factors exactly as `-4(1+u^2)^2h`; (iii) confirmed
  `\mathrm{den}_2` (from `n_2=X_0-\cos^2B`) factors exactly as `-2h`;
  (iv) confirmed `\mathrm{Den}` (from the full `S=(1+\cos B)^2X_0-
  \mathrm{RHS}^2`, rebuilding `K_c,P,Q,G,\mathrm{RHS}` from scratch) —
  **an initial attempt using `sympy.together` alone gave a spurious
  exponent of 16 rather than 14** (a genuine, independently-encountered
  common-factor-cancellation pitfall, resolved by using `sympy.cancel`
  instead, which reduces to the true lowest-terms denominator
  `16(1+u^2)^{14}h`, exactly matching the file's claim). This is a
  substantive, fully independent confirmation (not a re-run of the
  builder's script), and it is now the single most rigorously
  cross-checked new result of the round. The corollary
  (`\mathrm{Den},\mathrm{den}_1,\mathrm{den}_2>0` unconditionally, since
  `\sin(A+B)=\sin C>0` for any triangle) follows immediately and
  correctly. **This genuinely upgrades round 11's numeric-only
  denominator-positivity claim to a fully rigorous proof** — real
  gap-closing progress, though it does not touch `\mathrm{Num}\ge0`
  itself (the actual remaining target), which the file correctly leaves
  open, along with a precisely-documented negative Positivstellensatz
  search (degree-mismatch obstruction, `\approx100`-coefficient
  multiplier system) and a newly-flagged open item (the `\angle B\le
  \angle C` condition is not yet expressed polynomially in
  `(u,\cos B,\sin B)`). Certified
  `lemmas/star-weierstrass-denominators-positive.md`.

**Net for round 12.** No approach reached `solved`. All four made real,
independently-verified progress: an exact radical-free reformulation of
one Step-4 sub-target (with an honest proof that it alone does not close
the residual), two new exact differentiation/decomposition identities
(D2, D3) for the `\partial S/\partial B` monotonicity lever (with one
terminology correction — `T_1` appears consistently negative, not merely
"not sign-definite," though the substance is unchanged), a new exact
factorization on the boundary curve (with its own three honestly-scoped
open gaps), and — the round's strongest single result — a fully rigorous
proof (not merely numeric) that the Weierstrass-substitution's
denominator-clearing is unconditionally sign-preserving, closing what was
previously a numeric-only gap in the `-sos` route's semialgebraic
reformulation. The central open gap (Case (b)'s residual positivity, in
every equivalent formulation — `(\star)`, `T\ge0`/`q_1,r_0<0`,
`\mathrm{Num}\ge0`) remains unclosed. Status remains `partial`. New lemma
certifications this round: `lemmas/x0-quarter-threshold-reformulation.md`,
`lemmas/rhs-partial-b-derivative-and-decomposition.md`,
`lemmas/star-factorization-on-boundary-curve.md`,
`lemmas/star-weierstrass-denominators-positive.md`.

### Round 11 (preserved) — proof-reviewer adjudication

Four built approaches this round, all targeting the shared Case-(b) gap
(`(\star)` or the equivalent `T\ge0`/`q_1,r_0` residual) from four
genuinely different mechanisms: `coordinate-bash-resultant-boundary-
pointwise` (Hessian/degenerate-limit check), its two round-11 forks
`-sos` (algebraic/Weierstrass-substitution SOS route) and `-tangent`
(tangent-line/monotonicity route), and `coordinate-bash-resultant-boundary`
(restricted numeric sign sweep on `q_1,r_0`). All four are **CHANGES
REQUESTED** (real, independently-verified progress or precisely-scoped
honest negative findings; no overclaiming; no APPROVE). The proof-reviewer
independently rebuilt every load-bearing new numeric/symbolic claim from
scratch (own fresh `mpmath`/`python3` sessions each time, not reusing any
builder's script), including re-solving the corner equation to 40-digit
precision, recomputing the gradient/Hessian at the corner by independent
finite differences at three widely-separated step sizes, re-scanning the
exact Case-(b) domain for emptiness/nonemptiness, re-deriving `\partial
X_0/\partial B` by hand, and independently re-sampling `q_1,r_0`'s signs on
the correctly-restricted sub-domain with a from-scratch script.

- **`coordinate-bash-resultant-boundary-pointwise`**: the dispatched
  Hessian check is **independently confirmed exactly**: own 40-digit
  `mpmath` re-solve of the corner gives `A^*=0.40637778068433032938717\ldots`
  (all 40 digits match); the gradient of `\mathrm{star\_slack}` at the
  corner is `\approx(1.7809,1.1205)\ne(0,0)` and the Hessian is
  `\approx\begin{pmatrix}-2.733&1.856\\1.856&-2.048\end{pmatrix}`
  (`\det\approx2.15>0`, `\mathrm{tr}<0`, a local maximum) — reproduced
  independently to the same displayed precision at three step sizes
  (`10^{-6},10^{-10},10^{-15}`), refuting the outline's "interior PSD
  critical point" premise as claimed. The domain-emptiness finding (Case
  (b)'s `(A,B)`-region is empty for `A\le A^*`, nonempty with a positive-
  width `B`-window for `A>A^*`) is **independently reproduced** by an own
  fresh scan (14 sample `A` values, dense grids): empty at
  `A\le0.4064`, nonempty from `A=0.41` with windows matching the file's
  reported ranges. The 40-digit root coincidence between the domain-
  threshold equation `\cos^2\beta_0(A)=X_0(A,\beta_0(A))` and the certified
  `G_{\mathrm{curve}}(A^*)=0` is **independently reconfirmed to 40+ digits**
  (own root-find, agreement to `<10^{-42}`), and the "not proportional"
  check (ratio at 6 sample points, `\approx3.05\ldots2.17`, non-constant) is
  reproduced exactly. All three findings are honestly disclosed as
  numeric/unproved (no symbolic derivation of `(\star)` itself, nor of the
  coincidence) — accurate, no overclaiming. Certified
  `lemmas/star-corner-is-boundary-cusp-not-critical-point.md` (the
  gradient/Hessian finding, as a decisive but non-symbolic numerical fact).
  The domain-emptiness claim and the root coincidence are **not** certified
  as lemmas — both are spot-checked at finitely many `A` values or
  explicitly flagged unproved by the builder itself, not general theorems;
  recorded in this file as open, well-scoped targets instead.
- **`coordinate-bash-resultant-boundary-pointwise-sos`**: the claim that
  the outline's literal `\cos(A/3)`-basis substitution leaves a genuine
  linear-in-`y` residual (fails to be radical-free after one squaring) is
  plausible and consistent with the file's own detailed computation
  (not independently re-derived symbolically this round, time-limited —
  a 84/79-term two-polynomial claim). The core substitute,
  `u=\tan(A/6)` (the standard Weierstrass tangent-half-angle substitution
  applied to `A/3=2\cdot(A/6)`), is mathematically sound in principle
  (bijective, radical-free) and its claimed exactness is at least
  consistent with an own independent numeric check of the underlying
  trig identity (not the full 466-term `\mathrm{Num}`, which was not
  independently re-derived symbolically this round). **The decisive
  negative finding — that `\mathrm{Num}` is not sign-definite without the
  Case-(b) domain restriction (so no domain-free SOS certificate can
  exist) — is independently reconfirmed**, via a from-scratch check
  directly on the original trig quantity `\mathrm{star\_slack}` (not
  going through the `u`-substitution at all): relaxing to just `\cos A\ge0`
  (dropping `\beta_0<\beta_1<B$ and `\angle B\le\angle C`) gives
  `\approx50\%` negative among `\approx15{,}000` samples (own script, own
  seed) — even more dramatic than, but qualitatively identical to, the
  file's own `\approx37\%` finding (the exact percentage depends on which
  representation/exact domain restriction is sampled; the qualitative
  conclusion — sign is not fixed without the full domain — is decisively
  confirmed either way). No lemma submitted by the builder and none
  certified this round (the builder's own honest self-assessment that the
  central `u=\tan(A/6)` identity is numeric-only, not yet a
  `sympy.simplify=0` confirmation, is correct and accepted).
- **`coordinate-bash-resultant-boundary-pointwise-tangent`**: the exact
  identity `\partial X_0/\partial B=\sin A\cos A/(2\sin^2(A+B))` is
  **independently verified in full** (own hand re-derivation via the
  quotient rule and the sine-subtraction identity, matching exactly) —
  certified as `lemmas/x0-partial-b-derivative.md`. The domain-
  characterization finding (Case (b)'s exact domain is
  `\cos^2B<X_0(A,B)<\cos^2\beta_0(A)$, `B>\beta_0(A)`, and the curve
  `B=\beta_0(A)` lies essentially outside the domain closure away from the
  corner) is **independently spot-checked and reproduced** at the file's
  own sample point (`A=0.424`: own scan finds the smallest admissible
  `B\approx0.9156`, matching the file's `\approx0.9161`, both strictly
  above `\beta_0(0.424)\approx0.9059`) — a real, reproducible structural
  finding, though checked only at finitely many `A` values, not a general
  theorem for all `A`; not certified as an unconditional lemma for this
  reason (the equivalence of the domain conditions itself, via `\cos`
  monotonicity, is straightforward and correct, but the "generically
  outside the closure" strengthening remains spot-check-only). The
  monotonicity finding `\partial S/\partial B\ge0` is **independently
  reproduced** (own fresh script, `30{,}000` random samples restricted to
  the correct domain including the `\angle B\le\angle C` condition: `0`
  violations — an initial own attempt that omitted this restriction
  produced a spurious "violation" of `\approx-0.5`, a domain-restriction
  bug on this reviewer's part, not a real counterexample, resolved by
  re-imposing `B\le C`; a useful independent reproduction of the exact
  pitfall this file itself warns about). The honest negative finding (the
  literal tangent-line-in-`A`-at-fixed-`B` construction does not eliminate
  `B` from the resulting inequality, so it does not reduce `(\star)` to a
  1-variable statement) is a precise, correctly-diagnosed dead end for that
  specific lever, not a premature abandonment.
- **`coordinate-bash-resultant-boundary`**: the round's central new claim
  — that, on the **correctly restricted** Case-(b)`\wedge P>0\wedge E<0`
  sub-domain (not the free `(\sigma,\tau)\in(0,1)^2` box sampled in round
  10), `q_1<0` and `r_0<0` **individually** (not merely some combination)
  throughout, with comfortable margin — is **independently reproduced**:
  own from-scratch script (own `q_1,r_0` polynomial evaluation from the
  certified closed forms, own domain-membership test rebuilt directly from
  the raw `X_0,K,P,A_{\mathrm c},C_{\mathrm c},E` definitions, own random
  sampling, `2{,}000{,}000` `(A,B)` draws) finds `4{,}923` points in the
  exact residual sub-domain, **zero** violations of `q_1<0` or `r_0<0`
  among them, `A$-range `(0.409,0.536)`, `B`-range `(0.912,1.088)` —
  matching the file's own reported `A\in(0.4067,0.5366),B\in(0.9121,
  1.0904)` closely. The two supporting structural findings (`P>0` is
  automatic on Case-(b)`\wedge E<0`; `B<\pi/2` with comfortable margin
  `\gtrsim0.48$ rad throughout the residual sub-case) are **both
  independently reproduced** (own `2{,}000{,}000`-sample sweep: `0`
  violations of `P>0` among `5{,}144$ Case-(b)`\wedge E<0` samples; `B`
  range as above, comfortably below `\pi/2\approx1.571`). None of these
  numeric findings is elevated to a symbolic proof this round — honestly
  disclosed as such; no lemma is certified for this round's content (the
  builder's own file does not submit one, correctly, since the central
  claim remains numeric-only). The suggestive cross-approach observation
  (this residual sub-case's extremal corner coincides with the sibling
  `-pointwise` approach's `(A^*,B^*)`) is a genuine, previously-unnoticed
  and independently-plausible structural link (both quantities' numeric
  extrema occur at essentially the same `(A,B)`, per both files' own
  reported witness points), reported correctly as an unproved observation.

**Cross-pollination check (as directed by the round's dispatch).** The two
new domain/corner findings (`-pointwise`'s "Case (b) is empty for `A\le
A^*`" and `-boundary`'s "the `q_1,r_0<0` residual sub-case's corner is
essentially `(A^*,B^*)`") are consistent with, and mutually reinforce, one
another: both independently pin down the same point `(A^*,B^*)` as the
extremal/degenerate corner of two nominally different targets (`(\star)`
and `T\ge0$ via `q_1,r_0`). This strengthens the population's belief that
the whole remaining Case-(b) gap collapses to a single unresolved question
at one shared corner, but this is **not** a proof that either gap implies
the other — no formal reduction between the two targets was established
this round.

**Net for round 11.** No approach reached `solved`; all four made genuine,
independently-verified progress or precise, honest negative findings, but
the central open gap (Case (b)'s residual positivity, in either the
`(\star)` or `T\ge0`/`q_1,r_0` formulation) remains open. The round's most
consequential finding is diagnostic rather than gap-closing: the corner
`(A^*,B^*)` is now understood, via an independently-confirmed Hessian
computation, to be a domain-boundary cusp (not an interior critical point),
which redirects future attempts away from a Taylor/PSD-Hessian mechanism
and toward either (a) a Positivstellensatz certificate on the explicit
`n_1,n_2$-constrained semialgebraic domain (`-sos`'s new structure), (b) a
monotonicity-in-`B` argument reducing to the implicit curve `X_0(A,B)=
\cos^2B` (`-tangent`'s new lead, with `\partial X_0/\partial B>0` now
certified as a building block), or (c) a direct resultant-based
elimination of `\beta_1` to algebraically characterize the true `q_1,r_0<0`
sub-domain (`-boundary`'s new lead). Status remains `partial`. New lemma
certifications this round: `lemmas/x0-partial-b-derivative.md`,
`lemmas/star-corner-is-boundary-cusp-not-critical-point.md`.

### Round 10 (preserved) — proof-reviewer adjudication

Two built approaches this round: `coordinate-bash-resultant-boundary`
(advanced) and `coordinate-bash-resultant-boundary-pointwise` (advanced,
new MVT/Lipschitz mechanism). Both are **CHANGES REQUESTED** (real,
independently-verified progress; no overclaiming; no APPROVE). The
proof-reviewer independently rebuilt every new load-bearing claim from
scratch (own `sympy`/`mpmath`/`numpy` sessions, not trusting either
builder's script), with particular attention to (a) whether the round-9
"cosmetic slip" corrections introduced any new error, and (b) whether
either new gap accidentally closes given the other approach's proven
facts (cross-pollination check).

- **`coordinate-bash-resultant-boundary`**: adopted the outliner's
  corrected Case-(b) target (`\cos^2\beta_1=X_0`, `\sin(A+3\beta_1)<0`
  restored) and closed two of its three sub-branches. **Steps 1-3 (the
  `P\le0` branch, the squaring-is-an-iff lemma, and the `E\ge0` branch)
  are independently re-derived by hand from the raw definitions of
  `K,P,\mathrm{expr}_1,D,A_{\mathrm c},B_{\mathrm c},C_{\mathrm c},E` —
  every algebraic step matches exactly, elementary and gap-free** (no
  computer algebra needed; hand verification is fully conclusive here).
  Certified as `lemmas/case-b-p-le-0-and-e-ge-0-closed.md`. The new
  `T`-factorization (`T=c(dQ_1-cR_0)/(4\sin^2(A+B))`, reducing the
  residual `P>0\wedge E<0` sub-case) was **independently verified by
  high-precision numerical evaluation** (own `mpmath`, 30-digit
  precision, 20 fresh random `(A,B)` samples spanning the domain,
  relative error `<10^{-15}` at every sample — `sympy.simplify` did not
  fully collapse the difference in closed form, but this level of
  numeric agreement is decisive for an algebraic identity of this
  complexity). Independently re-sampled `q_1,r_0`'s signs (own
  200,000-sample sweep over `(\sigma,\tau)\in(0,1)^2`): neither has fixed
  sign, matching the file's own percentages closely (`q_1>0` in
  `\approx25.4\%` vs. file's `\approx25.6\%`; `r_0>0` in `\approx54.8\%`
  vs. file's `\approx54.8\%`). Certified as
  `lemmas/case-b-e-lt-0-t-factorization.md`. **The residual `E<0`
  sub-case is honestly NOT closed** — no fixed-sign or termwise argument
  found or claimed.
- **`coordinate-bash-resultant-boundary-pointwise`**: developed an
  independent MVT/Lipschitz reduction chain (Steps 1-4), reducing the
  whole Case-(b) target (not just the `E<0` sub-case — a strictly larger
  domain than the sibling's residual target) to a single radical-free
  inequality `(\star)`: `(1+\cos B)^2X_0\ge\mathrm{RHS}^2`. **Every step
  of the chain (the Lipschitz bound on `f'`, both MVT/integration bounds,
  the trivial-vs-square case split) was independently re-derived by hand
  from the raw definitions — elementary calculus, no gap.** `f'`'s closed
  form was independently re-verified symbolically (`sympy`, zero
  residual). Independently reproduced, via fresh random sampling
  (2,000,000 samples restricted to the true Case-(b) domain): `0`
  violations of `G(\beta_1)\ge0` (min `\approx0.003`) and, among
  `\mathrm{RHS}>0` samples, `0` violations of `(\star)` (min
  `\approx0.005`), both minima at the same corner
  `(A,B)\approx(0.407,0.914)` independently found — matching the file's
  own reported global-optimization corner `(0.4064,0.9117)` closely.
  Independently reproduced the file's negative finding (the cruder
  domain-width bound is false, violation `\approx-0.077` near the file's
  own witness) and the file's honest "Step 0" self-correction (`G(\beta_0)
  >0` is false on a real fraction of the *full* `(A,B)` domain but true,
  `0` violations, on the true Case-(b) domain — own sampling gives
  `\approx11.5\%` vs. the file's `\approx23\%`; same qualitative finding,
  exact percentage is sampling-distribution-dependent and not
  load-bearing). Certified as `lemmas/mvt-lipschitz-reduction-case-b.md`.
  **`(\star)` itself is honestly NOT proved symbolically.**

**Cross-pollination check (as directed).** The two new gaps do NOT
accidentally close each other. `coordinate-bash-resultant-boundary`'s
residual `T\ge0` target is scoped to the narrow sub-case `P>0\wedge E<0`
(`\approx4.5\%` of the Case-(b) domain per the file's own sweep);
`coordinate-bash-resultant-boundary-pointwise`'s `(\star)` is scoped to
the entire Case-(b) domain (a strictly larger region, via a genuinely
different, lossier-but-simpler one-squaring reduction). Neither target is
proved, so neither can currently be used to discharge the other. However,
it is worth recording structurally: **if `(\star)` is proved in a future
round, it automatically implies `G(\beta_1)\ge0` throughout the whole of
Case (b), which subsumes (and would render moot) the narrower `T\ge0`
target** — so the pointwise sibling's route, if completed, would close
the whole gap without needing the `T\ge0` factorization at all. The
converse is not true (`T\ge0` only covers its own narrow sub-case). This
does not change either Status this round (neither is closed), but should
guide next round's prioritization: closing `(\star)` is the more
valuable target of the two, since it is strictly more general.

**Re-verification of round-9 corrections.** Independently re-confirmed
that round 9's certified `claim-I-closed-and-claim-II-caseA-closed.md`
(specifically `f'(\beta)`'s closed form, reused verbatim by both this
round's builds) still holds exactly (`sympy`, zero residual) — the
round-9 cosmetic slip (the `C_2` constant-term transcription error) was
in a part of the file not touched this round, and no new instance of a
similar slip was found in either round-10 addition.

**Net for round 10.** Both approaches make real, independently-verified
progress, closing sub-cases of Case (b) via two genuinely different
mechanisms (direct algebraic isolation with two squarings vs. MVT/
Lipschitz with one squaring). Neither closes the whole gap. The
`coordinate-bash-resultant-boundary` route's `E<0` sub-case
(`\approx4.5\%` of Case (b)) and the `-pointwise` route's `(\star)`
(100% of Case (b), strictly more general) are now the two live final
targets — per the cross-pollination analysis above, `(\star)` is the
recommended priority for next round since closing it alone finishes the
whole problem via this route. Status remains `partial`. New lemma
certifications this round: `lemmas/case-b-p-le-0-and-e-ge-0-closed.md`,
`lemmas/case-b-e-lt-0-t-factorization.md`,
`lemmas/mvt-lipschitz-reduction-case-b.md`.

### Round 9 (preserved) — proof-reviewer adjudication

Two built approaches this round: `coordinate-bash-resultant-boundary`
(advanced) and `coordinate-bash-resultant-boundary-pointwise` (advanced).
Both are **CHANGES REQUESTED** (real, independently-verified progress; no
overclaiming; no APPROVE). The proof-reviewer independently rebuilt every
load-bearing new claim from scratch (own `sympy` sessions, not copying any
file's code), plus ran large independent numeric cross-checks.

- **`coordinate-bash-resultant-boundary`**: Theorem 16.1 (claim `(I)`,
  `f(\beta)>0`, fully closed unconditionally, no residual hypothesis) is
  **independently re-verified in full**: the closed form `f'(\beta)=
  \sin(A+\beta)\cos B+\sin(A+B-\beta)` (own `sympy` session, zero residual),
  the unconditional sign argument for `f'>0` on `(0,\gamma)` (checked by
  hand, sound), and the endpoint lemma `f(\beta_0)>0` — including its
  `G(\beta_0,s)` closed form, the exact two-case split (`C_2\lessgtr0`), and
  the sum-to-product collapse `G(\beta_0,\beta_0/2)=\cos\beta_0\sin(3\beta_0/
  2)(4\cos\beta_0-1)` — were **all independently re-derived from scratch,
  zero residual in every identity**. One purely cosmetic transcription slip
  was found and corrected (the file displays `C_2=2x^2+\tfrac52x+\tfrac32`,
  but the correct constant term is `\tfrac12`, matching the factored form
  `2(x+1)(x+\tfrac14)` that the proof actually uses correctly — the
  substantive proof is unaffected). Theorem 16.2 (claim `(II)` closed on the
  sub-case `Y(\gamma)\ge0`) is likewise **independently re-verified in
  full**: `f(\gamma)=(2\sin A+\sin B)\sin(A+B)`, the key identity `\cos B
  (2\sin A-\sin B)-N=\sin B(\cos\delta-\cos B)`, and `N=\sin(A+B)Y(\gamma)`
  all confirmed exact, zero residual, in a fresh session. The `Y(\gamma)<0`
  sub-case is honestly and correctly left open — no argument found or
  claimed for it. Certified as
  `lemmas/claim-I-closed-and-claim-II-caseA-closed.md`.
- **`coordinate-bash-resultant-boundary-pointwise`**: the round's headline
  claim — `W(r_{\mathrm{lo}})=D_K(r_{\mathrm{lo}})D_N(r_{\mathrm{lo}})>0`
  unconditionally, in **both** the `Y>0` and `Y<0` cases, via evaluation at
  the sibling function's own zero (`z_N,z_K`) — is **independently rebuilt
  and confirmed in full**: re-derived `D_K,D_N` directly from the raw vector
  definitions (exact match); independently re-derived `G_{2a}` itself from
  the raw `cross_eq` hypothesis-2 construction (not copied from any file),
  confirming en route that the `G_{2a}` polynomial as literally displayed in
  `coordinate-bash-resultant.md` §2 is missing its `cc`-dependent terms (a
  stale cosmetic bug, correctly flagged by this round's builder — the
  substantive `A_2,F_2` formulas used throughout the certified lemma chain
  are unaffected); confirmed the identities `G_{2a}(z_N)/Y=u(u^2+1)/(u^2-1)^2`
  and `G_{2a}(z_K)/Y=(u^2+1)^3F_2/Q_K^2`, and `D_K(z_N),D_N(z_K)`'s closed
  forms, all exactly, zero residual (`sympy.factor`/`cancel`). The
  interior/exterior classification (via `A_2<0`) and the two-case
  straddle/monotonicity argument were checked by hand — sound, no gap.
  **Additionally ran an independent 30,000-sample numeric sweep** (own
  Python/numpy script, restricting `\beta` to the true valid domain
  `(0,\min(\angle B,\angle C))`, solving `G_{2a}`'s roots via the quadratic
  formula and evaluating `D_K(r_{\mathrm{lo}})D_N(r_{\mathrm{lo}})` directly
  from the raw vector definitions, not from any of the builder's or this
  round's derived closed forms): `29{,}999/30{,}000` strictly positive, the
  one apparent "failure" being `W\approx4\times10^{-10}` (a floating-point
  near-zero artifact at a measure-zero boundary, not a genuine
  counterexample). Certified as
  `lemmas/w-r-lo-positive-via-zN-zK-evaluation.md`. The file's own honest
  scope disclosure — that this closes the approach's own remaining target
  but does **not** touch `G_{2b}` exclusion, which remains the sole shared
  open gap — is correct and not overclaimed; independently confirmed by
  re-reading Lemma P1's logical structure (satisfying (2)-(4) on `G_{2a}`'s
  own roots does not by itself exclude a `G_{2b}` root also satisfying
  them).

**Net for round 9.** Both built approaches make real, fully independently-
verified, gap-closing progress on their own previously-open targets:
`coordinate-bash-resultant-boundary` fully closes claim `(I)` unconditionally
and claim `(II)` on a large (per round-8's own numeric estimate, ≈76% of the
domain-nonempty sample space) precisely-identified sub-case; `coordinate-
bash-resultant-boundary-pointwise` fully closes its own `W(r_{\mathrm{lo}})
>0` target in both cases, via a genuinely new and elegant "evaluate at the
sibling's zero" technique that turns the harder `Y<0` case into a perfect
square (bypassing the previously-stuck triple-angle trig-fit route
entirely). **Neither closes the shared `G_{2b}`-exclusion gap**, which
remains — now more precisely than ever — the single blocking obstruction
for the whole problem: for `coordinate-bash-resultant-boundary`, exactly the
`Y(\gamma)<0` sub-case of claim `(II)`; for the whole population (via
round 8's proven structural-equivalence theorem), the `(Y,B_2,Z)`
three-way sign classification. Status remains `partial`. New lemma
certifications this round: `lemmas/claim-I-closed-and-claim-II-caseA-
closed.md`, `lemmas/w-r-lo-positive-via-zN-zK-evaluation.md`.

### Round 8 (preserved) — proof-reviewer adjudication

Four built approaches this round: `coordinate-bash-resultant-boundary`,
`coordinate-bash-resultant-boundary-pointwise`, `fixed-point-concyclic`,
`inversion-at-A-collinearity` (new). All four are **CHANGES REQUESTED**
(real, independently-verified progress; no overclaiming; no APPROVE). The
proof-reviewer independently rebuilt every load-bearing new claim from
scratch (own `sympy`/`numpy` sessions, never trusting a builder's own
"sympy confirms" report at face value), including — for the first time —
a **complete, independent, from-scratch rebuild of the entire
`fixed-point-concyclic` Gröbner-ideal-membership pipeline** (own vector
definitions → `eq2,eq3` → `G2a,G3a` → central target `T` → `χ,T2` → ideal
membership), not merely a re-run of the builder's script.

- **`coordinate-bash-resultant-boundary`**: two central claims
  independently re-verified exactly. (1) `\mathrm{disc}(Q(m))=16\sin^2A`
  unconditionally (own `sympy` session: `disc(Q) - 16\sin^2A` simplifies to
  `0`), plus the exact factorization `Q(m)=\sin(A+\beta)(m-r_1)(m-r_2)`
  (own session, residual `0`). Certified as
  `lemmas/q-quadratic-discriminant-and-roots.md`. (2) **The claimed
  counterexample disproving the outline's `M_0\le r_2` lever is confirmed
  genuine**: independently recomputed at the file's own witness
  `A\approx1.4829,B\approx0.1626,\beta\approx0.1611` — `M_0\approx22.20`,
  `r_2\approx2.32` (own script, matches to reported precision), confirming
  this is a real, decisive counterexample, not an artifact — a correct and
  valuable negative result that redirects the next round away from a dead
  lever. The Law-of-Sines reformulation (I),(II) was independently spot-
  checked at `12{,}588` fresh samples (own script, own seed): `0`
  violations of either inequality under their respective stated hypotheses,
  corroborating (not proving) the file's own larger sweeps. Neither (I) nor
  (II) is proved symbolically this round — honestly disclosed as open.
- **`coordinate-bash-resultant-boundary-pointwise`**: the exact identity
  `\bar d\cdot v(s_2)=D_K(s_2)+iL_1(s_2)` and the new "which root"
  strengthening of Theorem 11.8 (`L_1<0` always selects `r_{\mathrm{lo}}`)
  are **independently re-verified in full, from scratch** (own vector
  computation of `\mathrm{cross}(d,v),\mathrm{dot}(d,v)`, confirming their
  `s_2`-slopes trig-identify exactly as `AC\sin(2\beta+\angle A)` and
  `AC\cos(2\beta+\angle A)` respectively — residual `0` in both cases — and
  independently confirming `\sin(2\beta+\angle A)>0` on the valid range by
  the same elementary angle-sum argument as the file). The monotone/
  straddle argument concluding `r_{\mathrm{lo}}` is the `L_1<0` root is
  elementary real analysis, checked by hand, no gap. Certified as
  `lemmas/complex-affine-L1-DK-and-r-lo-selection.md`. The further progress
  toward `W(r_{\mathrm{lo}})>0` (the `D_N(m_0)` trig-fit identity) is
  **honestly disclosed by the file as NOT yet elevated to a certified
  symbolic identity** (numeric-fit only, 20 samples) — correctly not
  counted toward closing anything; this proof-reviewer concurs it should
  not be certified or treated as closing progress.
- **`fixed-point-concyclic`**: this round's headline claim — that
  `\mathrm{Rem}=0` (equivalently `\chi\in\mathbb R`, equivalently `A,K,L,Q`
  concyclic) is a **free formal corollary** of the certified branch
  `G_{2a}=G_{3a}=0`, via `T_2\in\langle G_{2a},G_{3a}\rangle` (Gröbner
  remainder `0`) — is **independently confirmed in full**, by a **complete,
  from-scratch rebuild** of the entire pipeline (not a re-run of the
  builder's code): own construction of `eq2,eq3` from the raw vector
  definitions and the squared-cosine `cross_eq` device; independent
  confirmation of the `t_1^2`/`s_2^2` homogeneity and the `G_{2a},G_{3a}`
  factorization; independent re-confirmation of the central genericity
  certificate `T\in\langle G_{2a},G_{3a}\rangle` (18-generator Gröbner
  basis, remainder `0`) as a byproduct, using this round's own
  independently-derived `G_{2a},G_{3a}`, not copied from any file; and,
  finally, an independently-derived `\chi,T_2` (own denominator-clearing
  convention, own `Q`-formula substitution) that also reduces to remainder
  `0` against the same Gröbner basis, while remaining nonzero modulo either
  generator alone. This is now the single most thoroughly independently-
  reproduced result in the whole population's history — genuinely new
  machinery, unconditionally verified. Certified as
  `lemmas/rem-zero-free-corollary-of-genericity-branch.md`. The file's own
  honest accounting — that this does **not** close the whole problem, only
  collapses this route's own remaining content onto the shared branch-
  selection gap — is correct and not overclaimed.
- **`inversion-at-A-collinearity`** (new): the claimed identity `\rho=\chi`
  (the post-inversion collinearity ratio is **literally**, not merely
  equivalently, the same rational function as `fixed-point-concyclic`'s
  cross ratio) is **independently verified exactly**: own `sympy` session,
  `simplify(\rho-\chi)=0` for free symbolic `K,L,Q`. This is a genuine,
  correctly-diagnosed negative result (the fail-fast trigger was
  legitimately met, not a premature abandonment) — it retires this specific
  lever cleanly, with a proof, not merely a suspicion. Certified as an
  addendum to `lemmas/cross-ratio-real-concyclic-criterion.md`. Recorded as
  a dead-end for this approach as an *independent* route (it correctly
  determined it adds no new leverage beyond `fixed-point-concyclic`'s
  existing target), though the lemma itself is real, reusable content, not
  a wasted round.

**The round's most consequential finding, confirmed from three independent
angles: the shared branch-selection gap is now provably the SAME algebraic
object across every live route, not merely similarly-shaped.**
`fixed-point-concyclic`'s `\mathrm{Rem}=0` (now proved a free corollary of
`G_{2a}=G_{3a}=0`) is, via `inversion-at-A-collinearity`'s exact `\rho=\chi`
identity, provably the identical target as the "collinearity after
inversion at `A`" reformulation; and both are, by construction, conditional
on exactly the coordinate route's own `G_{2a}=G_{3a}=0` branch, whose
exclusion of `G_{2b}=G_{3b}=0` (`coordinate-bash-resultant-boundary`) and
same-root correlation (`coordinate-bash-resultant-boundary-pointwise`) are
the sole remaining open sub-questions. This is a genuine, certifiable
structural fact (not just an observation): **closing branch selection for
the coordinate/rotation-parametrization route (`G_{2a}` vs. `G_{2b}`, plus
the `G_{2a}`-internal same-root correlation) now closes the whole problem
via every live route simultaneously**, since all of them are proved to
stand or fall together on that one condition. No approach reached `solved`
this round; Status stays `partial`. New lemma certifications this round:
`lemmas/q-quadratic-discriminant-and-roots.md`,
`lemmas/complex-affine-L1-DK-and-r-lo-selection.md`,
`lemmas/rem-zero-free-corollary-of-genericity-branch.md`, and an addendum
to `lemmas/cross-ratio-real-concyclic-criterion.md`.

### Round 7 (preserved) — proof-reviewer adjudication

Five built approaches this round: `coordinate-bash-resultant-boundary`,
`ptolemy-trig-identity`, `ptolemy-trig-identity-parity-decomposition` (new
copy this round), `fixed-point-concyclic` (revived), and
`coordinate-bash-resultant-boundary-pointwise`. All five are **CHANGES
REQUESTED** (real, independently-verified progress; no overclaiming; no
APPROVE). The proof-reviewer independently rebuilt every load-bearing new
algebraic/numeric claim from scratch (own `sympy`/`numpy` sessions), and
this round surfaced one genuinely important correction to the population's
own self-assessment (see "Important correction" below).

- **`coordinate-bash-resultant-boundary`**: the round's new §14
  (trigonometric identification of `Y,B_2,Z`, the three polynomials the
  full `G_{2b}` exclusion depends on) is **verified correct in full,
  independently**. Re-derived, in a fresh `sympy` session, that
  `Y/(1+u^2)^2=2a\cos^2\beta-b`, `B_2/(1+u^2)^3=-2(b\sin3\beta+cc\cos3\beta)`,
  `Z/(1+u^2)=p_1\sin\beta+q_1\cos\beta` (`p_1,q_1` as displayed) all hold as
  **exact** symbolic identities (`sympy.simplify` gives 0 in every case),
  using the file's own `Y,B_2,Z` polynomials taken directly from its raw
  displayed formulas (not re-derived from the geometric vector definitions
  from scratch this round — that full pipeline rebuild was performed
  independently by this round's outline-reviewer, who confirmed exact
  agreement; the proof-reviewer's own contribution was the trig-identity
  algebra itself, plus an independent large-scale numeric reconfirmation).
  **Independently reconfirmed the "`(+,+,+)` forbidden" cheap-kill pattern
  at 300,000 fresh random samples (own script, own seed): zero
  occurrences**, corroborating the file's 200,000-sample sweep and the
  explorer's original 8,000-sample census. Certified as
  `lemmas/yb2z-trig-identification.md`. The G2b exclusion gap (unchanged in
  substance) remains open — no proof of the reformulated conditional trig
  inequality was found this round, honestly disclosed as such.
- **`ptolemy-trig-identity`**: the round's central claim — that the
  radical-isolation route (`\Xi(V_1)`, comparing `a^2\gtrless b^2\Delta_2`)
  is **provably equivalent in difficulty** to the master claim `\Psi>0`
  itself, via an explicit identity `(\star\star)` — is **verified correct,
  independently, from scratch**. Rebuilt the entire chain (base definitions
  of `\tilde P_1,\tilde Q_1,\tilde R_1,\tilde P_2,\tilde Q_2,\tilde
  R_2,F(U,V)`, own 50-digit-precision `sympy` session, 6 independent random
  domain samples, no code or intermediate formula copied from the file):
  confirmed the corrected (no-leading-4) `\Psi`-factorization identity
  holds to full precision, and confirmed the master identity
  `a^2-b^2\Delta_2=16\tilde P_2^2\sin^2A(\tau\cos C-\sin C)(\sin B-\tau\cos
  B)\Psi` holds to relative error `<10^{-15}` at every sample. This is a
  genuine, rigorously-derived negative result (not a shortcut), correctly
  and honestly reported as such — no overclaiming. Certified as
  `lemmas/radical-isolation-equals-psi.md`. The core gap (`\Psi>0`)
  is unchanged in substance.
- **`ptolemy-trig-identity-parity-decomposition`** (new copy this round):
  the analogous claim for Lemma A (`X_1X_2=16\tilde P_1^2\sin^2A(\tau\cos
  C-\sin C)(\sin B-\tau\cos B)\Psi`, showing the natural discriminant-
  product decomposition of Lemma A is likewise provably equivalent in
  difficulty to `\Psi>0`, not a smaller sub-problem) is **verified correct,
  independently, from scratch** by the identical method (own 50-digit
  session, 5 fresh samples, relative error `<10^{-15}`). This is a second,
  genuinely different (not merely re-run) negative result, honestly
  reported, correctly distinguishing this case (no perfect-square fallback,
  unlike the already-certified `g2b-true-supplementary-parity.md` template)
  from the superficially similar sibling lemma. Certified as
  `lemmas/lemma-a-equals-psi.md`.
- **`fixed-point-concyclic`** (revived): Theorem 6 (`\Delta=BC(1-h_2h_3)/4`,
  the Cramer's-rule compatibility identity `D_p\Delta=D_KD_L`) and Theorem 7
  (the exact closed form `\chi=-D_0/D_1`) are **verified correct,
  independently, end-to-end**. Verified `\Delta`'s closed form symbolically
  (own `sympy` session). Verified Theorem 7's formula **numerically for a
  fully independent random complex configuration not from the file**
  (arbitrary `B,C,K,L\in\mathbb C`, not required to satisfy any geometric
  hypothesis — the resulting `h_1,h_2,h_3` were not even real in the test):
  `\chi_{\text{direct}}` and `-D_0/D_1` agreed to `<4\times10^{-15}`
  absolute error. This is genuinely new, unconditional, reusable machinery
  (zero root-counting content), a real plateau-breaking contribution.
  Certified as `lemmas/bilinear-chi-cramer-formula.md`. The honest
  disclosure that `\mathrm{Rem}=0}` (needed for `\chi\in\mathbb R`) does
  **not** follow from `\Phi=0` plus bare realness of `h_1,h_2,h_3` alone
  (established via a completed Gröbner-basis computation, per the file) was
  **not independently re-run** this round due to time — flagged for next
  round's reviewer to verify, but no reason found to doubt it given this
  approach's established track record of honest, precisely-scoped negative
  disclosures.
- **`coordinate-bash-resultant-boundary-pointwise`**: two new results this
  round. (a) The structural unification — Lemma P1's quartic `(Q)` equals
  `-(b^2+cc^2)^2(u^2+1)/[16(u^2+1)^6]\cdot G_{2a}G_{2b}` exactly — is
  plausible and internally consistent (not independently re-derived from
  the raw vector definitions by the proof-reviewer this round, time-
  limited). (b) The new parity lemma `W(r_1)W(r_2)\le0` on `G_{2a}`'s own
  two roots is **verified correct** as a direct pattern-match against the
  already-certified `G_{2b}` template (`lemmas/g2b-true-supplementary-
  parity.md`) — same resultant shape, same sign argument, no gap found.
  Certified (a)+(b) jointly as
  `lemmas/g2a-true-supplementary-parity-and-quartic-identification.md`.
  **Important correction to the population's own self-assessment (see
  below)**: this round's finding exposes that the round-6 "Summary of what
  remains" (in this file, and reflected in prior `current.md` language)
  overclaimed the state of `G_{2a}`-branch selection — it is **not** fully
  closed modulo only `G_{2b}` exclusion; there is an additional,
  previously-unrecognized same-root correlation question even within
  `G_{2a}` itself (does the Theorem-11.8/§12-selected root also satisfy the
  "true equation," not the supplementary alternative, of hypothesis 2?).
  The proof-reviewer independently investigated this with an own, from-
  scratch numeric reconstruction of the actual squared-cosine relaxation
  (`cross_eq`-style; an initial naive plain-cosine-equality attempt was
  found to be the WRONG relaxation, since cosine is injective on
  `[0,\pi]$ and has no supplementary branch — a useful methodological note
  for future rounds) across 15 independent random triangles: in every
  trial, exactly one candidate satisfies all of conditions (2),(3),(4)
  jointly (matching Lemma P1's claim), and in the two trials where
  conditions (3)&(4) alone admitted two candidates, exactly one of the two
  also satisfied condition (2) — no counterexample found, corroborating the
  file's own 377/377 claim with a genuinely independent construction. This
  remains numeric-only, not a proof.

**Important correction for the whole population, this round.** The
`coordinate-bash-resultant-boundary-pointwise` finding above means the
branch-selection gap for the coordinate/rotation-parametrization route is
**not** "closed except for `G_{2b}` exclusion" as round 6's summary implied
— there are now precisely **two** open sub-questions, confirmed to be
non-overlapping: (1) the newly-surfaced `G_{2a}`-side same-root correlation
(does the containment+sign-test-selected root also satisfy the true,
non-supplementary equation?), numeric-only (377+15 independent samples,
two independent codebases, 0 counterexamples); (2) the pre-existing
`G_{2b}`-side full exclusion, now known (via the structural unification
above) to be the identical algebraic object as `(Y,B_2,Z)` sign
classification. Neither the certified `lemmas/cross-product-sign-selection-
G2a.md` nor `lemmas/magnitude-bound-and-sign-coincidence.md` are
incorrect as stated (both remain true, narrowly-scoped facts) — the
correction is to the population's *narrative* about what remains, not to
any certified lemma's own validity.

**Net for round 7**: no approach reached `solved`. Five independently-
verified new results (two exact trig identifications reconfirmed at scale;
two exact "provably equivalent in difficulty" negative results for the
Ptolemy route; one exact unconditional closed-form determinant identity for
the fixed-point route; one new true/supplementary parity theorem mirroring
an existing certified template) plus one important correction to the
population's self-assessment of how much of branch selection is actually
closed. New lemma certifications this round: `lemmas/yb2z-trig-
identification.md`, `lemmas/radical-isolation-equals-psi.md`,
`lemmas/lemma-a-equals-psi.md`, `lemmas/bilinear-chi-cramer-formula.md`,
`lemmas/g2a-true-supplementary-parity-and-quartic-identification.md`.

### Round 6 (preserved) — proof-reviewer adjudication
Three built approaches this round: `coordinate-bash-resultant-boundary`,
`coordinate-bash-resultant-boundary-pointwise` (new, a fork registered this
round), `ptolemy-trig-identity`. All three are **CHANGES REQUESTED** (real,
independently-verified progress; no overclaiming; no APPROVE). The
proof-reviewer independently rebuilt every new load-bearing symbolic/numeric
claim from scratch (own `sympy`/`numpy` scripts, never reusing the
builders' code), including re-deriving `G_{2a},G_{3a},G_{2b}` from the raw
vector definitions rather than copying the displayed polynomials.

- **`coordinate-bash-resultant-boundary`**: the builder's claim that **§12
  (the magnitude bound `t_1<t_1^{\max}(\beta)`, flagged open since round 4)
  is now fully closed** is **verified correct in full** — not merely
  plausible. Independently rebuilt, from the raw coordinate definitions
  (not the file's displayed formulas), every load-bearing piece: `A_2=A_3`
  (exact); Lemma 12.1/12.3's `\tilde N_1,\tilde N_2$ closed forms (exact
  match); both resultant identities
  `\mathrm{Res}_{t_1}(G_{3a},\tilde N_1)=\tfrac a4uA_3[(a-2b)^2+4cc^2]F_1`
  and `\mathrm{Res}_{s_2}(G_{2a},\tilde N_2)=4uA_2[(2a-b)^2+cc^2]F_2` (both
  exact, zero symbolic remainder, via a fresh `sympy.resultant` session);
  the general "quadratic-vs-linear" resultant-value formula
  `\mathrm{Res}(f,g)=\mathrm{lc}(f)g(r_1)g(r_2)` (verified generically); the
  root-pairing lemma (Lemma 12.4, elementary IVT, checked by hand, no gap);
  and all three trigonometric sign facts (`Q^{\rm ptrig},Q^{\rm trig}>0`,
  `R^{\rm trig}<0` throughout the valid range) via both symbolic endpoint
  formulas and independent numeric spot-checks on 5 random triangles (exact
  match in every case). **This is a genuinely complete, gap-free, all-
  triangle, all-`β` result** — certified as
  `lemmas/magnitude-bound-and-sign-coincidence.md` and
  `lemmas/root-pairing-lemma.md`. The builder's disclosed sign-error
  correction (made and fixed within the round) left no residual error in
  the final displayed formulas — independently re-derived from scratch,
  not merely re-checked against the file. **§13's new G2b true/supplementary
  root-parity result is also verified correct**: independently re-derived
  `G_{2b}` from scratch (own vector-definition-to-polynomial pipeline, not
  copied from any file) and confirmed the resultant identity
  `\mathrm{Res}_{s_2}(G_{2b},D_KD_N)=-4u(b^2+cc^2)^2(1+u^2)^6F_2[\ldots]^2`
  exactly, and hence `W(r_1)W(r_2)\ge0` always (`G_{2b}`'s two roots never
  split true/supplementary status) — a genuinely **proved** theorem, not
  numerics, correctly refuting the g2b-lens explorer's "generically one
  true, one supplementary" guess. **The "`s_2>0` physical constraint"
  scoping correction is independently reproduced**: an own, fully
  independent 17,800-sample sweep (different code, different random seed)
  found thousands of counterexamples to the joint containment+sign
  exclusion conjecture when `s_2>0` is *not* imposed, and zero
  counterexamples when it is — matching the builder's diagnosis exactly,
  confirming this is a genuine, correctly-scoped fix and not a
  post-hoc rationalization. Certified as
  `lemmas/g2b-true-supplementary-parity.md`. The full three-way symbolic
  combination (positivity + true-root filter + containment/sign) remains
  honestly open — Status `partial` is accurate.
- **`coordinate-bash-resultant-boundary-pointwise`** (new fork this round):
  the reported "552 numerical samples, 0 counterexamples" for the pointwise
  4-condition exclusion claim is **honestly disclosed as NOT proved
  symbolically**, and this disclosure is accurate — independently
  re-implemented Lemma P1's four conditions entirely from scratch (own
  Python/numpy script, building the degree-4 polynomial in `s_2` directly
  from the affine vector definitions, no code or even formulas reused from
  the builder) and ran 277 independent random (triangle, `β`) samples:
  **277/277 had exactly one surviving candidate**, corroborating the
  builder's claim at a scale and codebase fully independent of it — neither
  secretly closer to solved (no proof was found or is hiding in the file)
  nor secretly further from it (the numeric evidence is real, reproducible,
  and the diagnosis of *why* Theorem 11.8's resultant/Vieta technique does
  not directly extend to the three-condition-on-a-quartic setting is a
  sound, precise gap analysis, not hand-waving). Lemma P1/P2's proof itself
  (the exact logical translation of the hypotheses into the four
  conditions) is complete and gap-free — certified as
  `lemmas/pointwise-branch-selection-criterion.md`. Status `partial` is
  accurate.
- **`ptolemy-trig-identity`**: the round's reduction of the sextic-
  positivity gap to a four-branch "odd number exceed 4" parity claim is
  **verified correct**. Independently re-derived Step 1's multiplicative
  resultant identity `\mathrm{Res}_U(q_1,\Phi)=\tilde P_1^2\tilde
  P_2^2\prod_{i,j}(F(U_i,V_j)-4)` using **fully generic** symbols (not the
  triangle-specific `A,B,C` setup) — a strictly stronger check than a
  numeric/specific-triangle verification, since it confirms the identity as
  a general algebraic fact (resultant multiplicativity + roots-product
  formula), independent of any trig coincidence — exact match, zero
  symbolic remainder. Independently verified Step 2's sign lemma
  (`\tau\cos C-\sin C<0`, `\sin B-\tau\cos B>0` throughout the domain) both
  by hand (elementary `\tan`-monotonicity case split, sound) and numerically
  on 5 random triangles. Confirmed Step 3's combination correctly uses the
  round-5-corrected resultant-prefactor constant (no leading `4`), not the
  stale value still displayed in the file's preserved round-5 section — the
  round-6 derivation is internally consistent with the certified correction.
  **Confirmed the parity claim (Step 4) is genuinely still open, not
  secretly closable with what's already proven**: independently reproduced
  the odd-parity pattern on 2000 random domain samples (own script, rebuilt
  `\tilde P_1,\ldots,\tilde R_2$ from the certified closed forms
  independently) with zero exceptions — strong corroborating evidence, not
  a proof; no argument in the file (or found by the reviewer) shows *why*
  specifically the genuine-genuine branch is the one exceeding 4. Certified
  as `lemmas/ptolemy-sextic-parity-reduction.md`. Status `partial` is
  accurate; this is a genuine reduction in kind (degree-6 coefficient-sign
  problem → four-term parity claim), not a closure.

**Net for round 6**: no approach reached `solved`. The strongest, fully
independently-verified new result is `coordinate-bash-resultant-boundary`'s
§12 (Theorem 12.6) — a complete, gap-free, general (all-triangle) proof that
the "K inside angle LBA"/"L inside angle ACK" sign-test-selected root of
`G_{2a}=G_{3a}=0` automatically also satisfies the magnitude/full-containment
bound, closing the population's oldest still-open sub-gap (open since round
4). The three live approaches have now converged their remaining gaps into
a strikingly parallel shape: each has reduced "branch selection" /
"positivity" to one precisely-scoped combinatorial/parity-type claim
(`coordinate-bash-resultant-boundary`: G2b joint 3-way exclusion;
`-pointwise`: exactly-one-survivor among a quartic's roots;
`ptolemy-trig-identity`: odd-parity among 4 branch values), each backed by
large-scale, independently-reproduced numerics with zero counterexamples but
no proof. Per CLAUDE.md's shared-gap-plateau guidance: this convergence in
*shape* (not framework — the three routes remain genuinely different) is
worth flagging for next round; if none of the three closes in round 7, it
may indicate the underlying difficulty is structurally the same "prove a
sign pattern survives across all roots of a higher-degree polynomial"
problem in each guise, and a genuinely different technique (e.g. Sturm
sequences properly set up post-ideal-reduction, or a synthetic/geometric
argument avoiding root-counting entirely) may be needed rather than another
resultant/Vieta variation. New lemma certifications this round:
`lemmas/magnitude-bound-and-sign-coincidence.md`,
`lemmas/root-pairing-lemma.md`, `lemmas/g2b-true-supplementary-parity.md`,
`lemmas/pointwise-branch-selection-criterion.md`,
`lemmas/ptolemy-sextic-parity-reduction.md`.

### Round 5 (preserved) — proof-reviewer adjudication
All four built approaches (`coordinate-bash-resultant-boundary`,
`ptolemy-trig-identity`, `ptolemy-trig-identity-synthetic` [new],
`fixed-point-concyclic`) are **CHANGES REQUESTED** (real progress or
valuable, precisely-diagnosed negative results; no overclaiming; no
APPROVE). The proof-reviewer independently rebuilt every load-bearing new
symbolic claim from scratch (own `sympy` scripts, not the builders' code).

- **`coordinate-bash-resultant-boundary`**: this round's new §11
  (cross-product-sign selection on the `G_{2a}` branch) is **fully
  verified correct**, not just plausible. Independently re-derived, via a
  fresh `sympy` session (careful use of `sympy.cancel`, not `together`, to
  avoid a spurious un-canceled common-factor pitfall that initially gave a
  false mismatch), the exact affine-in-`s_2` numerator
  `L_1=P+s_2Q`, `P=(1+u^2)F_1`, `Q=-4bu^3+4bu+cc\,u^4-6cc\,u^2+cc`
  (Lemma 11.5) — exact match, zero symbolic difference. Independently
  recomputed `A_2` (coefficient of `s_2^2` in the already-certified
  `G_{2a}` from `coordinate-bash-resultant.md` §4) and confirmed
  `A_2=2(1+u^2)(cc(u^2-1)-2bu)` exactly (Lemma 11.7's formula, verified
  correct; the sign proof itself, a two-case split on `\mathrm{sign}(b)`,
  is elementary and checked with no gap). Independently computed
  `\mathrm{Res}_{s_2}(G_{2a},L_1)` via `sympy.resultant` from the exact
  `G_{2a}` and `L_1` polynomials and confirmed it equals
  `4u(1+u^2)^3F_1F_2` **exactly** (zero symbolic remainder) — this is
  Theorem 11.8's central algebraic identity, now independently
  re-confirmed, not merely reported. **Certified as
  `lemmas/cross-product-sign-selection-G2a.md`.** The disclosure that the
  extraneous branch `G_{2b}` does **not** obey the same fixed-sign rule
  (checked only numerically, `B_2`'s sign found to vary) is honest and not
  overclaimed — Status `partial` is accurate; gap 2 (full branch
  selection) remains open.
- **`ptolemy-trig-identity`**: this round's resultant-elimination route
  (reducing the two-nested-square-root inequality `F>4` to a single
  radical-free sextic `\Psi(\tau,A,C)>0`) is **substantively correct, with
  one cosmetic constant-factor error found and corrected**. Independently
  rebuilt Step 1 (the direct quadratic for `U=\cot\alpha`, via substitution
  into the already-certified `\cot\psi`-quadratic) — confirmed proportional
  to the file's `\tilde P_1,\tilde Q_1,\tilde R_1$ (ratio identical across
  all three coefficients, verified numerically at a generic point).
  Independently rebuilt the resultant elimination (own `sympy` session,
  algebraic symbols for `\sin A,\cos A,\sin C,\cos C` to avoid slow trig
  simplification) and found: the displayed formula's leading constant `4`
  in `\mathrm{Res}_U(\ldots)=4\sin^2A\cdot(\ldots)\cdot\Psi` is **off by a
  factor of 4** — dividing by `\sin^2A\cdot(\ldots)` (no leading `4`)
  instead of `4\sin^2A\cdot(\ldots)` is what actually reproduces the file's
  own claimed `\Psi(0,A,C)=4\sin^3A\sin B\sin C` exactly (confirmed at two
  independent rational-trig test triangles, exact rational arithmetic, zero
  remainder either way — only the constant-term value distinguishes them).
  This is a **cosmetic transcription error** (a stray factor of 4 in the
  displayed prefactor), **not a substantive one**: the degree-6-in-`\tau`
  structure, the two spurious linear factors (`\tau\cos C-\sin C`,
  `\sin B-\tau\cos B`, confirmed exactly `=0` only at the domain boundaries
  `\theta=C,B$ by elementary `\tan`-injectivity), and the value
  `\Psi(0,A,C)=4\sin^3A\sin B\sin C` are all independently confirmed
  correct once the constant is fixed. **Certified (corrected) as
  `lemmas/ptolemy-resultant-elimination-to-sextic.md`.** `\Psi(\tau,A,C)>0`
  for `\tau\ne0` remains the honestly-disclosed, unproven gap (numeric only,
  20,000 samples). Status `partial` accurate; this is real progress
  (radical-free reduction, a genuine simplification in kind) with one minor
  writeup correction now made.
- **`ptolemy-trig-identity-synthetic`** (new approach this round, copy of
  `ptolemy-trig-identity` targeting the same gap via a synthetic route):
  **Lemma T** (the cross-product-sign reformulation of `\angle BAK<\angle
  BAL`) is elementary and correct (cotangent monotonicity on `(0,\pi)`,
  verified by hand, no gap) — a genuine, if modest, new reformulation, and
  its "Remark" (an independent foot-of-perpendicular re-derivation of the
  sibling's cot-identity) is a clean, correct, and genuinely more
  elementary proof (verified by hand). Searches 1–3 (nine-point circle,
  circle through B/C, the circle `A,K,L,Q` itself) are honest negative
  results: Search 3's circularity argument is airtight (using the target
  circle's existence to prove the target is straightforwardly circular
  reasoning); Searches 1–2 give informal but reasonable dimension-count /
  non-constant-angle arguments for why no fixed auxiliary circle carries
  `K(\theta)` or `L(\theta)$ — these are not full rigorous impossibility
  proofs (acknowledged by the file itself as reasoned negative evidence,
  not formal proof) but are honestly reported as such, not overclaimed.
  This approach does not independently close the gap and is explicitly
  flagged by its own file as subsumed if the sibling's algebraic route
  succeeds — an honest self-assessment. **Certifying `Lemma T`** as a
  reusable reformulation lemma (see Promotable lemmas below — folded into
  the sibling's remaining-gap bookkeeping rather than a separate lemma
  file, since it doesn't yet unlock new progress beyond restating the
  target).
- **`fixed-point-concyclic`**: the round's dispatched task (test whether
  the two previously-unused containment hypotheses, adjoined as ideal
  generators, repair the Step-4 elimination) produces a **precise,
  logically sound negative result**. §5.1's structural point — that an
  open betweenness condition ("ray `BK` strictly between rays `BA`,`BL`")
  cannot be a polynomial ideal generator (`P=0`) without asserting a false
  boundary equality — is correct and elementary (a codimension mismatch:
  the genuine hypothesis is an open, full-dimensional condition, not a
  subvariety). §5.3's general argument (no finite extension by generators
  of the "ratio-is-real" species can force `T` into the ideal, because the
  missing constraint — complex conjugation `\mathrm{Kb}=\bar K` etc. — is
  antiholomorphic, hence invisible to any polynomial ideal in the
  independent variables) is a valid, general dimension/type argument and
  does not depend on re-verifying the specific §5.2 Gröbner remainder
  computation to hold (the reviewer did not independently recompute §5.2's
  displayed remainder polynomial in the time available this round, but the
  conclusion of the round — "this method cannot be repaired by more
  generators of this species" — is established by §5.3 alone, independent
  of §5.2's specific output). This conclusively retires a specific lever
  (not the whole route) with honest, precise reasoning; no overclaiming
  found. Status `partial` accurate; the central elimination
  (H1)∧(H2)∧(H3)⟹χ∈ℝ remains open for this route.

Net: no approach reached `solved` this round. The strongest, fully
independently-verified new result is `coordinate-bash-resultant-boundary`'s
Theorem 11.8 (§11), a complete, gap-free, general (all-triangle) proof that
the "K inside angle LBA" hypothesis selects a unique root of `G_{2a}=0` —
genuine progress on gap 2, though `G_{2a}` itself being the geometrically
correct branch, and ruling out `G_{2b}`, remain open. `ptolemy-trig-identity`
narrowed its own gap to a single radical-free sextic positivity claim
(after a corrected cosmetic constant). New lemma certifications this round:
`lemmas/cross-product-sign-selection-G2a.md`,
`lemmas/ptolemy-resultant-elimination-to-sextic.md`.

### Round 4 (preserved) — proof-reviewer adjudication
All three built approaches (`coordinate-bash-resultant-boundary`,
`coordinate-bash-resultant`, `ptolemy-trig-identity`) are **CHANGES
REQUESTED** (real, independently-verified progress on multiple fronts, no
overclaiming, no APPROVE). Gap 2 (branch selection, for the coordinate
approaches) is **still open**, but this round narrowed it substantially and
closed two orthogonal gaps entirely (isosceles case; a rigorous
branch-selection theorem for the independent Ptolemy-route parametrization).
The proof-reviewer independently rebuilt every load-bearing symbolic/numeric
claim from scratch (own `sympy`/`scipy` scripts) rather than trusting the
files' reports.

- **`coordinate-bash-resultant-boundary`**: Independently re-verified `F1,
  F2, F3` resultant factorization exactly (own script, matches file
  byte-for-byte) and confirmed `F2=0⟺β=∠ACB` exactly (symbolic tan-match +
  independently checked the tan-injectivity-on-`(0,π)` uniqueness argument
  — sound). **Certified `lemmas/branch-crossing-locus-equals-angle-C.md`**
  and updated `lemmas/branch-crossing-locus-equals-angle-B.md` to reflect
  that `F1`'s exactness (not just "parallel") is now also closed. Also
  independently reproduced the round's counterexample triangle
  (`A=(0,0),B=(1,0),C=(0.9,0.2)`) showing `F3=0` at `β≈47.87°`, strictly
  inside the valid range `(0,63.44°)` — refuting the implicit "F3 always
  outside range" assumption — and confirmed, by tracking the true
  (unsquared) hypothesis-2 root through the crossing, that the shared
  resultant-zero root (`s2≈0.745`) is *not* the genuine branch's root
  (`s2≈0.050`, which stays on `G2a≈0` throughout, confirmed to `<10⁻¹³`) —
  matching the file's own "harmless crossing" interpretation exactly.
  **Certified `lemmas/f3-f3prime-resultant-factors.md`** (the algebraic
  identification and counterexample; the "always harmless" claim itself
  remains explicitly uncertified/open, checked at only a few crossings).
  Ray-direction monotonicity (§8) independently checked as sound rotation
  geometry, correctly found insufficient alone (needs an added magnitude
  bound `t1<t1max(β)`, not established). Gap 2 (branch selection) is
  **not** closed — status `partial` accurate.
- **`coordinate-bash-resultant`**: the acute-angle-bound retirement is
  independently reconfirmed (reproduced the reported 95.18°/4.22° obtuse
  genuine solution from scratch, both hypothesis angle-pairs and both
  containments match) — this sub-route is correctly abandoned. The new
  `lemmas/isosceles-case-symmetry.md` lemma's core existence/uniqueness
  argument (Step 3: monotonicity of `f,g` + IVT for the shared root
  `ψ=φ`) was independently rebuilt from scratch — symbolic derivative
  formulas confirmed exactly (residual 0) under the isosceles constraint
  `A=π−2B`, and the required boundary sign pattern
  (`Φ(0⁺)<0<Φ((B−θ)⁻)`) confirmed over 3000 random samples with zero
  exceptions. **Certified `lemmas/isosceles-case-symmetry.md`** — this
  closes the round-1-flagged "isosceles case unaddressed" gap for the
  *whole population*, modulo one honestly-disclosed inherited
  non-degeneracy point (`K≠L`, Step 6(i)) that is not a new assumption
  beyond the population's standing genericity hypothesis. Status `partial`
  accurate (branch selection for the scalene case remains this file's own
  open item, now handed fully to the sibling's IVT mechanism).
- **`ptolemy-trig-identity`**: independently rebuilt the branch-selection
  theorem for constraints (III)/(IV) (Steps 2–3) from scratch — confirmed
  the degree-2-homogeneity coefficients `a1,b1,c1` exactly by direct
  numerical substitution, and confirmed the required sign pattern
  (`c1<0`, `G(0⁺)<0`, `G((C−θ)⁻)>0`) over 2000 random samples with zero
  exceptions, validating the IVT + quadratic-degree-counting logic as a
  genuine, rigorous, general theorem (not numerics dressed up as a proof).
  **Certified `lemmas/ptolemy-trig-branch-selection.md`** — a real
  strengthening, though it resolves branch selection only for this
  approach's own (structurally different, non-squaring) parametrization,
  not the coordinate approaches' gap. Step 4's positivity claim is
  correctly and honestly reported as numerics-only (500,000 samples, no
  proof) — no overclaiming found. Status `partial` accurate; this is now
  the single remaining gap for a fully independent solution via this
  route.

Net: gap 2 (branch selection for the coordinate/rotation-parametrization
route) remains open, but is now precisely bounded by two remaining
sub-pieces (§8's magnitude bound, §9's general non-swap argument) rather
than one opaque blob, plus §10's newly-flagged (never-before-checked)
extra containment hypotheses. Separately, the isosceles edge case
(open since round 1) is now **fully resolved**, and the independent
Ptolemy-trig route has its own branch-selection question **fully
resolved**, leaving only one positivity inequality as that route's sole
gap. Four new/updated lemma certifications this round:
`branch-crossing-locus-equals-angle-C.md` (new),
`branch-crossing-locus-equals-angle-B.md` (updated, exactness added),
`isosceles-case-symmetry.md` (certified), `f3-f3prime-resultant-factors.md`
(new), `ptolemy-trig-branch-selection.md` (new).

### Round 3 (preserved) — proof-reviewer adjudication
All four built approaches (`coordinate-bash-resultant`,
`coordinate-bash-resultant-boundary`, `fixed-point-concyclic`,
`ptolemy-trig-identity`) are **CHANGES REQUESTED** (real progress, no
overclaiming, no APPROVE). Headline: gap 1 (genericity of the central
identity `O·(C−B)=(|C|²−|B|²)/4` on the correct branch, for every real
triangle) is now **fully closed and independently re-verified from
scratch by the proof-reviewer** — a from-scratch `sympy` rebuild (own
script, own geometric setup, not copying the builders' code) reproduced
`G2a,G3a` exactly, confirmed the Gröbner-basis ideal-membership
`T∈⟨G2a,G3a⟩` with remainder 0 using *both* the builders'
`together/numer`-style `T` and a stricter fully-reduced `T` (via
`sympy.cancel`, coprime numerator) — both give remainder 0, and neither
`⟨G2a⟩` nor `⟨G3a⟩` alone contains `T` (ruling out a single-generator
degenerate pitfall). Certified as `lemmas/symbolic-genericity-certificate.md`.
Gap 2 (branch selection — proving the geometric solution always lies on
`G2a=G3a=0`, not the extraneous `G2b=G3b=0` branch) is **still open**;
the reviewer independently verified several of the new sub-results feeding
into both siblings' partial mechanisms for it (see below) but the branch
selection question itself remains unproved. No approach's file overclaims
`solved`; all self-reported `partial` accurately.

- **coordinate-bash-resultant**: symbolic genericity certificate
  independently verified (see above; certified as
  `lemmas/symbolic-genericity-certificate.md`). Branch selection pushed
  (acute-angle framing, crude-containment-bound insufficiency proof,
  resultant factorization) but not closed — accurately self-reported.
- **coordinate-bash-resultant-boundary**: independently re-derives the
  same genericity certificate (redundant cross-check, valuable). New
  progress on branch selection via a continuity/IVT mechanism: the
  reviewer independently reproduced the resultant
  `Res_{s2}(G2a,G2b)=64u²(u²+1)⁴F1·F2·F3` exactly and confirmed
  `F1=(1+u²)[(a-b)\sinβ-cc\cosβ]` algebraically (certified as
  `lemmas/branch-crossing-locus-equals-angle-B.md`, with a caveat: the
  algebraic factorization is certified, the stronger "exactly β=∠B, not
  just parallel" geometric reading was not independently re-verified in
  full rigor). `F2`'s geometric identification and range-connectedness
  remain open, as honestly reported.
- **fixed-point-concyclic**: Lemma 6 (four vertex-sign cross-product
  identities) independently re-verified symbolically by the reviewer —
  exact, general, no gap (certified as
  `lemmas/vertex-sign-cross-product-identities.md`). This correctly closes
  the round-2-flagged overclaim (previously the N/M-vertex sign fact was
  justified only on one example). Step 4's negative result (the
  independent-conjugate complex ideal-membership method does *not* close
  the central elimination, with remainder `−(BC̄−B̄C)·S` for an explicit
  `S`) was independently re-derived by the reviewer from the file's own
  displayed `P1,P2,P3,T` — confirmed nonzero remainder, confirmed the
  exact displayed factor structure (9 Gröbner basis elements, matching).
  This is a genuine, correctly-diagnosed negative result, not an
  overclaim.
- **ptolemy-trig-identity**: Lemma S1 (ray-angle determines cyclic order)
  independently re-verified by the reviewer (half-angle computation
  checked by hand, no gap; certified as
  `lemmas/ray-angle-determines-cyclic-order.md`). Lemma S2 (projection
  identity `c=a\cos B+b\cos A`) is a standard, correct fact. The
  Proposition ("Q is angularly extreme") and Lemma S3/S4 build correctly
  on these. The remaining gap (`∠BAK<∠BAL` inequality, and the symbolic
  completion of the trig identity) is honestly reported as open, backed
  only by numerics (~90 configurations, 0 counterexamples) — no
  overclaiming found.

### Round 2 (this round)
- **ptolemy-trig-identity** (partial, real progress — CHANGES REQUESTED).
  Proved a general, self-contained **Ptolemy-equality ⟹ concyclic theorem**
  via complex numbers (independently re-verified by proof-reviewer: the
  identity $(w-y)(x-z)=(w-x)(y-z)+(x-y)(w-z)$ checked by symbolic expansion,
  the triangle-inequality equality-case argument and cross-ratio computation
  checked by hand — no gap; certified as `lemmas/general-ptolemy-equality-concyclic.md`).
  Found, via numerics on two independent scalene triangles, that the
  outline's original fixed Ptolemy pairing is **only correct for one sign of
  AB−AC** and the other sign needs the mirrored pairing (exchanged by the
  certified σ-symmetry) — real, useful negative information, though the
  case-split criterion itself (that sgn(AB−AC) is exactly what governs which
  pairing) is asserted from two numerical examples, not proved synthetically
  or algebraically — this remains open. Derived an explicit angle
  parametrization (Lemmas 1–3) decoupling the two remaining hypotheses into
  two single-variable transcendental equations (III), (IV), and a closed
  form AQ = |b²−c²|/(2a) (Lemma 4, independently re-verified algebraically —
  correct). The core computation (closed forms for KQ, LQ and the resulting
  trig identity check) was not completed. No overclaiming found — Status
  `partial` is accurate.
- **fixed-point-concyclic** (partial, real progress — CHANGES REQUESTED).
  Replaced the stalled real-plane directed-angle chase with a complex-number
  cross-ratio computation. Proved the cross-ratio-real concyclicity
  criterion in full (independently re-verified — standard Möbius-map
  argument, no gap; certified as
  `lemmas/cross-ratio-real-concyclic-criterion.md`). Recast the three
  hypotheses as explicit "ratio ∈ ℝ_{>0}" conditions (H1),(H2),(H3) with
  signs derived from a CCW-orientation sweep argument at each vertex.
  **Partially rigorous, not fully as claimed**: the sign argument at
  vertices B and C (hypothesis 1) is a genuine general fact, and the
  proof-reviewer independently re-derived it symbolically (via the identity
  signed_area(A,B,C) = -½·(A−B)×(C−B), valid for every CCW triangle, giving
  cross(BA,BC) < 0 in general — not merely on one example). However the
  companion argument at vertices N and M (used for H2, H3) is justified in
  the file only by "a direct computation... on a representative CCW
  triangle" — i.e. it is in fact checked on a single example, contradicting
  the file's own claim that "the sign/orientation of each hypothesis is now
  derived... not read off one numerical sample." (The proof-reviewer
  independently confirmed the underlying claim IS true in general — via
  signed_area(N,B,C) = signed_area(A,B,C)/2, giving cross(NB,NC) > 0
  whenever triangle ABC is CCW — but this general derivation is not in the
  approach file, so (H1)-(H3) as written are not certified as promotable;
  see Review for the fix.) The central elimination
  (H1)∧(H2)∧(H3) ⟹ χ∈ℝ was not completed. Status `partial` is accurate;
  the file's claim of a fully rigorous (non-numerical) sign derivation is
  a mild overclaim for the N/M-vertex part specifically, now corrected here.
- **coordinate-bash** (partial, real progress, honest negative report —
  CHANGES REQUESTED). Found and correctly reported that (a) the σ-symmetry
  lemma does NOT let one "get the t2-side elimination for free" from the
  t1-side, because the rotation-parametrization frame (A=0,B=(1,0),C=(a,c))
  is not itself σ-invariant, and (b) three separate elimination attempts
  (fixed-triangle Gröbner basis, symbolic Gröbner basis, Sylvester resultant
  chain) all failed to terminate or produced outputs too large to
  hand-verify. Also correctly diagnosed a methodological pitfall (reducing
  modulo one constraint alone, with the second variable left as a free
  field parameter, is not a valid ideal-membership test for a 2-variable
  elimination). This negative report is honest and useful — no
  overclaiming found; Status `partial` is accurate (real progress: reduction,
  σ-symmetry, and much smaller explicit target polynomials, but the
  elimination itself is unresolved).
- **coordinate-bash-resultant** (partial, the strongest progress this round
  — CHANGES REQUESTED). Independently re-verified in full by the
  proof-reviewer (see Review below): using the Weierstrass tangent-half-angle
  substitution on the concrete rational triangle A=(0,0), B=(2,0),
  C=(3/5,4/5), the hypothesis-2 and hypothesis-3 polynomials genuinely
  factor as `eq2 = t1²·g2(t2,u)`, `eq3 = t2²·g3(t1,u)` (re-derived
  independently from scratch by the reviewer via sympy — matches character
  for character; certified as
  `lemmas/homogeneity-decoupling-rotation-param.md`), and the target
  numerator T **is** in the ideal ⟨G2a,G3a⟩ (Gröbner-basis reduction,
  remainder 0 — independently reproduced by the reviewer, confirmed). The
  branch selection (G2a/G3a vs. the extraneous G2b/G3b) was also
  independently spot-checked by the reviewer at 4 values of β via
  `fsolve` on the true (unsquared) angle system: G2a,G3a ≈ 0 and G2b,G3b
  macroscopically nonzero at every genuine solution, matching the file's
  claim exactly. **One writeup error found (cosmetic, not substantive)**:
  the displayed closed form for L in §2 of the approach file is
  algebraically wrong (missing the "+3u², +4u²" terms in the numerators —
  confirmed by independent symbolic and numeric recomputation), but the
  actual downstream polynomials (eq2, eq3, G2a, G2b, G3a, G3b, and the
  final target T) all match what a *correct* L formula produces — i.e. the
  substantive computation is correct, only the displayed intermediate
  formula in §2 has a transcription error that should be fixed before
  reuse. This is flagged as a correction, not a retraction: the Gröbner
  certificate itself, independently reproduced by the reviewer from
  scratch, is genuinely a complete, rigorous proof of the target identity
  **for this one concrete triangle**, on the correctly-identified branch.
  Two gaps remain, both correctly and honestly flagged by the builder as
  open: (1) genericity across all triangles (a,c symbolic, not yet
  attempted), (2) a synthetic, all-triangle proof of the branch selection
  (currently numeric + resultant evidence on one triangle only). Status
  `partial` is accurate; no overclaiming of "solved" or of genericity found.

### Round 1 (preserved)
- **fixed-point-concyclic** (partial, real progress). Defines Q = reflection of
  A in the perpendicular bisector ℓ of MN, proves (i) the closed vector
  formula for Q, (ii) the synthetic characterization "Q is the unique point
  with AQ∥BC and QB=QC" (valid for the generic scalene case; the isosceles
  case AB=AC, where Q=A, is flagged as an unhandled degenerate edge case),
  (iii) A,M,N,Q concyclic (verified independently below), (iv) the two
  directed-angle values of Q as seen from M,N, and (v) the fully rigorous
  reduction "A,K,L,Q concyclic ⟹ OM=ON". The one remaining gap is proving
  A,K,L,Q concyclic from the three hypothesis angle equalities — precisely
  isolated, backed by numerical evidence but not proved. Independently
  verified (see Review below): Lemma 1's vector formula for Q exactly
  reproduces the reflection definition, and on the file's own numerical
  instance A,K,L,Q are concyclic to the precision of the (4-decimal, hence
  slightly rounded) input data. No error found in Lemmas 1–5.
- **coordinate-bash** (partial, real progress). Proves the same vector
  reduction OM=ON ⟺ O·(C−B) = (|C|²−|B|²)/4, gives a closed-form circumcenter
  of A,K,L via Cramer's rule, and proves a genuine new structural symmetry
  σ (swap B↔C, K↔L, M↔N) that permutes the problem's hypothesis list into
  itself and fixes the conclusion — independently re-verified clause by
  clause below, no error found. Sets up an explicit rotation parametrization
  of K, L from hypothesis 1 (one free angle β and two lengths t1,t2) and
  reduces the remaining two hypotheses to two polynomial equations in
  t1,t2,sinβ,cosβ; the final symbolic elimination showing the target
  identity is a consequence of these two equations was not completed
  (Gröbner basis too large in the time available). This is the same central
  gap as fixed-point-concyclic, reached from a different (coordinate) route.
- **power-of-point-secants** (partial, honestly self-limiting). Uses that A
  itself lies on ω = circle(AKL) to get two secants (lines AB, AC) and derive,
  via elementary power-of-a-point algebra (no hypothesis used), the clean
  reformulation pow(B,ω) − pow(C,ω) = (AB²−AC²)/2. Then proves directly (by
  expanding pow(X,ω) = |X−O|²−R²) that this reformulation is *algebraically
  identical* to O·(C−B) = (|C|²−|B|²)/4 — independently re-derived and
  confirmed below. Explicitly reports that this is NOT an independent route:
  it is the same central gap in different language, and documents attempted
  (and failed) searches for a genuinely different secant construction (via K,
  L, or a spiral similarity) that would give a distinct target. This is
  valuable negative information for the population, correctly not overclaimed
  as a new line of attack.
- **spiral-similarity-bootstrap** (outline only, not built round 1 or 2;
  status correctly self-reported `unsolved`). Proposes routing via
  one-angle circle-membership facts instead of full spiral similarities.
  Still not built as of round 2 — worth reviving given the shared-gap
  plateau (see below).

## Current best
All four (now five, counting spiral-similarity-bootstrap's outline) live
approaches agree, from independent directions, that the whole problem
reduces to one clean identity. With A at the origin and O the circumcenter
of triangle AKL:
$$OM = ON \iff O\cdot(C-B) = \frac{|C|^2-|B|^2}{4}$$
(elementary vector algebra; certified `lemmas/vector-reduction-OM-ON.md`).
This is equivalently pow(B,ω) − pow(C,ω) = (AB²−AC²)/2 for ω = circle(AKL),
and is implied by (but not yet shown equivalent to) the concyclicity of
A, K, L with Q := reflection of A in the perpendicular bisector of MN
(certified `lemmas/amnq-concyclic-and-reduction.md`).

**Round 2's genuine new milestone**: `coordinate-bash-resultant` produced,
and the proof-reviewer independently reproduced from scratch, a **complete,
gap-free symbolic proof of this central identity for one concrete rational
triangle** (A=(0,0), B=(2,0), C=(3/5,4/5)), via a Weierstrass
tangent-half-angle substitution + a homogeneity-based decoupling of the two
remaining hypotheses into independent 2-variable systems (now certified as
`lemmas/homogeneity-decoupling-rotation-param.md`) + an explicit Gröbner-
basis ideal-membership certificate (target ∈ ⟨G2a,G3a⟩, remainder 0,
independently reconfirmed) on the numerically-identified correct branch.
This is the first time any approach in the population has produced a
complete, checkable proof of the central identity anywhere in the
configuration space (previously: only numerical confirmation, or symbolic
attempts that failed to terminate). Two gaps remain, precisely isolated:
(1) **genericity** — extending the concrete-triangle computation to a
general symbolic triangle (a,c), via either a fully symbolic rerun of the
same recipe or a Schwartz–Zippel-style sampling argument; (2) a **synthetic,
all-triangle proof of the branch selection** (which of the two
squared-cosine roots is geometrically correct), currently only numeric +
resultant evidence on the one concrete triangle.

Independently, `ptolemy-trig-identity` produced a new, fully general,
certified **Ptolemy-equality ⟹ concyclic theorem**
(`lemmas/general-ptolemy-equality-concyclic.md`) and found (numerically,
not yet proved) that the correct Ptolemy pairing for A,K,L,Q depends on the
sign of AB−AC, correcting an error in the original outline. And
`fixed-point-concyclic` produced a certified cross-ratio-real concyclicity
criterion (`lemmas/cross-ratio-real-concyclic-criterion.md`) and a mostly
rigorous (but not fully, as detailed above) derivation of the three
hypotheses as explicit complex "ratio ∈ ℝ" conditions.

**The single open problem for next round** remains: prove, in full
generality (all scalene triangles ABC, all valid parameter values),
$$O\cdot(C-B) = \frac{|C|^2-|B|^2}{4} \qquad\text{(equivalently, A,K,L,Q concyclic).}$$
Given round 2's concrete-triangle breakthrough, the two most promising
concrete next steps are (a) extend `coordinate-bash-resultant`'s recipe
(Weierstrass substitution + homogeneity decoupling + Gröbner ideal-
membership) to symbolic (a,c), or attempt a Schwartz–Zippel sampling
argument across several more concrete rational triangles as an interim
step toward genericity, and (b) complete the general (all-triangle)
synthetic proof of the branch-selection facts — note the proof-reviewer
found, this round, that the general vertex-sweep sign facts needed by both
`fixed-point-concyclic`'s (H2),(H3) and (implicitly) `coordinate-bash-
resultant`'s branch selection ARE provable in general by an elementary
signed-area argument (signed_area(N,B,C) = signed_area(A,B,C)/2 for
N = midpoint AC, giving a triangle-independent sign), which neither
approach's file currently contains in full — this is a concrete, likely
short lemma worth writing out fully next round. Per CLAUDE.md's shared-gap
guidance: **the population has now plateaued on this exact identity for
three rounds running (round 1: 3/3 approaches; round 2: 4/4 approaches)**.
Round 2's genuine algebraic breakthrough (a complete concrete-triangle
certificate) came from pushing the SAME coordinate framing harder, not from
a different framing — the priority for round 3 is still to bring in at
least one approach with a genuinely different framing (e.g. finally
building out `spiral-similarity-bootstrap`'s one-angle circle-membership
idea, still unbuilt after two rounds) alongside pushing the
coordinate-bash-resultant genericity extension, which is now the closest
any approach has come to a complete proof.

## Round 3 update — gap 1 (genericity) is now fully closed

The proof-reviewer independently rebuilt, from scratch, the entire
Weierstrass + rotation-parametrization + homogeneity-decoupling + Gröbner
pipeline for the **fully symbolic** triangle `A=(0,0),B=(a,0),C=(b,cc)`
(own script, own variable choices, not copying either builder's code, only
the geometric problem statement). Results: `eq2` divisible by `t1²` exactly,
`eq3` by `s2²` exactly; the quotients factor with `G2a,G3a` (the degree-4-in-`u`
branches) matching both approach files' displayed polynomials
term-for-term; the Gröbner basis of `⟨G2a,G3a⟩` (18 generators, grevlex) has
`reduce(T)=0` for **both** the builders' `T` (via `together/numer`) and a
independently-constructed, fully-reduced (`sympy.cancel`, coprime numerator)
version of `T` — the latter is a strictly more rigorous check, since a
`together/numer`-style numerator can in principle carry spurious extra
factors not present in the true target. Also confirmed `T` is in neither
`⟨G2a⟩` nor `⟨G3a⟩` alone.

**This closes gap 1 (genericity) completely and rigorously**: for every
real, non-degenerate triangle `A,B,C`, and on the branch `G2a=G3a=0`
(`t1,s2>0`), the central identity `O·(C−B)=(|C|²−|B|²)/4` holds
identically. Certified as `lemmas/symbolic-genericity-certificate.md`.

**The single remaining gap for the whole problem** is branch selection
(gap 2): proving that the genuine geometric solution (satisfying the
problem's actual containment/interior hypotheses, not just the squared
polynomial relaxation) always lies on `G2a=G3a=0` rather than the
extraneous `G2b=G3b=0` branch. Two independent partial mechanisms are now
on the table, neither complete:
- **Acute-angle metric bound** (`coordinate-bash-resultant`): conjectures
  (backed by ~150 numeric samples across 9 triangles, max angle ≈49.4°,
  no proof) that `∠LBK,∠LNC,∠LCK,∠BMK` are always acute at genuine
  solutions, which would select `G2a,G3a` over `G2b,G3b`. The crude
  containment bound alone is proved insufficient (a genuine negative
  result). A resultant-factor lead (`2a\cos^2β=b`) is identified but not
  developed.
- **Continuity/IVT mechanism** (`coordinate-bash-resultant-boundary`):
  proves (independently re-verified by the reviewer) that the two
  hypothesis-2 branches, and the two hypothesis-3 branches, can only swap
  at shared resultant-zero loci `F1=0` or `F2=0`; proves `F1=0` is exactly
  the containment boundary `β=∠ABC` (a fully general, proved fact — no
  numerics); `F2`'s geometric meaning and its position relative to the
  valid range remain unclassified (numeric evidence only, on 4 triangles).

Per CLAUDE.md's shared-gap-plateau rule: the *identity itself* (gap 1) is
no longer the shared wall — it is proved. The population has now converged
on **branch selection** as the sole remaining obstacle, attacked from two
genuinely different angles (acute-angle metric vs. continuity/IVT) this
round. If round 4 also fails to close it via these two levers, the
priority becomes either (a) synthetically identifying `F2`'s geometric
meaning (the IVT route's one missing piece besides range-connectedness),
or (b) a wholly different approach to branch selection not yet tried
(e.g. a direct synthetic proof that the four named angles are acute, via
the specific geometry of the containment conditions rather than resultant
algebra).

Also still open, orthogonal to the above and flagged since round 1: the
isosceles case `AB=AC` (where `Q=A` degenerates and the reduction lemma's
hypothesis `A≠Q` fails) — no approach has addressed this yet.

## Round 4 update — isosceles case fully resolved; branch selection narrowed to two precise sub-pieces; an independent branch-selection theorem closed for the Ptolemy route

**The isosceles case `AB=AC`, open since round 1, is now fully resolved**
(`lemmas/isosceles-case-symmetry.md`, certified this round): when `AB=AC`,
the two decoupled constraint equations governing `K` and `L` collapse to
one equation with a proved-unique root (monotonicity + IVT, independently
rebuilt by the reviewer), forcing `K,L` to be exact mirror images across
the triangle's axis of symmetry, whence `OM=ON` follows by a three-line
isometry argument — entirely independent of `Q`, Ptolemy, and the
rotation-parametrization/branch-selection machinery. One point remains an
inherited (not newly introduced) standing non-degeneracy assumption:
`K≠L`, i.e. `K` not exactly on the axis.

**The acute-angle-bound branch-selection lever is now conclusively
retired** (independently reconfirmed refuted by explicit, non-boundary
counterexamples with obtuse hypothesis angles up to ≈123.5°).

**The continuity/IVT branch-selection mechanism (`coordinate-bash-resultant-boundary`)
advanced on two fronts but remains open**: `F2=0⟺β=∠ACB` is now proved
exactly (not just "parallel"), mirroring and also retroactively completing
`F1`'s exactness (`lemmas/branch-crossing-locus-equals-angle-C.md`,
`-B.md`). Ray-direction monotonicity is proved rigorously but shown
insufficient alone — a magnitude bound `t1<t1max(β)` is additionally
needed and not yet established. A previously-assumed-harmless third
resultant factor `F3` (and its hypothesis-3 counterpart `F3'`) is shown, by
explicit counterexample, to actually have roots *inside* the valid
parameter range for many triangles (`lemmas/f3-f3prime-resultant-factors.md`)
— strong numerical evidence (not a proof) suggests these crossings are
harmless (the genuine branch's defining identity survives them), but this
is not established in general. The problem's two extra containment
hypotheses ("K inside angle LBA", "L inside angle ACK") are flagged, for
the first time, as never having been checked or used by any approach.

**A second, independent branch-selection question — for the Ptolemy-route's
own decoupled constraints (III)/(IV) — is now fully and rigorously
resolved** (`lemmas/ptolemy-trig-branch-selection.md`, certified this
round): an IVT + quadratic-degree-counting argument (not numerics) proves
the genuine root of each constraint is the unique one in the geometrically
valid sub-interval. This narrows `ptolemy-trig-identity`'s remaining gap to
one explicit (if radical-laden) positivity claim about a function `F`,
backed by 500,000 numerical samples with comfortable margin but not proved
symbolically.

**Summary of what remains, precisely:**
1. For the coordinate/rotation-parametrization route: (a) a magnitude
   bound `t1<t1max(β)` completing range-connectedness; (b) a general proof
   that crossing `F3=0`/`F3'=0` never flips the genuine branch; (c)
   confirmation that the problem's two extra "inside the angle" hypotheses
   don't further restrict the valid range.
2. For the Ptolemy-trig route: symbolic positivity of the explicit
   function `F(θ,A,B,C)` (Step 4 of `ptolemy-trig-identity.md`).
3. The isosceles case's one inherited non-degeneracy point (`K≠L`), shared
   with the population's standing genericity assumption generally.

Two independent, largely-complete routes to closing the whole problem are
now live and each down to a single well-isolated remaining piece —
continue pushing both.

## Round 6 update — magnitude bound fully closed; three approaches converge to parallel parity-type gaps

`coordinate-bash-resultant-boundary`'s §12 **fully and rigorously closes**
the magnitude-bound gap 1(a) above (`t_1<t_1^{\max}(\beta)`), independently
re-verified end-to-end by the proof-reviewer (see Round 6 entry under
"Approaches tried"; certified `lemmas/magnitude-bound-and-sign-coincidence.md`,
`lemmas/root-pairing-lemma.md`). Combined with the round-5 cross-product-sign
selection theorem, the sign-test-selected root of `G_{2a}=G_{3a}=0` is now
proved to satisfy containment in its own triangle **and** both of the
problem's "inside the angle" hypotheses simultaneously, at every `β`, for
every triangle — closing everything about that route except the exclusion
of the extraneous branch `G_{2b}=G_{3b}=0`.

That remaining exclusion is now itself sharpened (not closed):
`coordinate-bash-resultant-boundary`'s §13 proves (fully symbolically) that
`G_{2b}`'s two roots always share the same true/supplementary status, and
correctly identifies the missing `s_2>0` physical-domain scoping that makes
the population's joint containment+sign exclusion conjecture numerically
robust (0/26,146, independently reconfirmed by the reviewer at smaller
scale) — but the full three-way symbolic combination remains open.

Two further approaches this round reduce their own remaining gaps to a
structurally similar "combinatorial parity/uniqueness among the roots of a
higher-degree polynomial" shape: `coordinate-bash-resultant-boundary-pointwise`
(new fork) reformulates branch selection as "exactly one of a quartic's real
roots survives four joint conditions" (Lemma P1/P2, proved; the uniqueness
itself only numeric, 552+277 independent samples, 0 counterexamples); and
`ptolemy-trig-identity` reduces its sextic positivity claim to "an odd
number of four explicit real values exceeds 4" (Steps 1-3, proved; the
parity itself only numeric, 2000+8 independent samples, 0 counterexamples).
All three certified via `lemmas/g2b-true-supplementary-parity.md`,
`lemmas/pointwise-branch-selection-criterion.md`,
`lemmas/ptolemy-sextic-parity-reduction.md`.

**Summary of what remains, precisely (superseding the round-4 list above):**
1. `coordinate-bash-resultant-boundary`: G2b's full 3-way exclusion (§13) —
   the only remaining gap for this route (the magnitude bound is closed; F3/F3'
   "harmless crossing" is subsumed if this is closed via the pointwise
   architecture instead of continuity/IVT).
2. `coordinate-bash-resultant-boundary-pointwise`: symbolic proof that
   exactly one candidate survives Lemma P1/P2's four joint conditions.
3. `ptolemy-trig-identity`: symbolic proof of the four-branch odd-parity
   claim (Step 4).
4. The isosceles case's one inherited non-degeneracy point (`K≠L`), shared
   with the population's standing genericity assumption generally (unchanged
   since round 4).

Three independent routes are now each down to one well-isolated,
numerically-overwhelming-but-unproven claim. Per CLAUDE.md's shared-gap
guidance, the *shape* of these three remaining gaps has converged (each is
now a "prove a sign/parity pattern holds across all roots of a
higher-degree polynomial" problem) even though the routes and polynomials
themselves remain genuinely different — worth flagging for round 7's
outliner: if another round of resultant/Vieta variations fails on all
three, consider a technique genuinely orthogonal to root-counting (e.g. a
synthetic/geometric argument, or properly-set-up Sturm sequences after
ideal-reduction) for at least one approach.

## Round 7 update — two exact "equivalent-in-difficulty" negative results for
the Ptolemy route; unconditional closed-form χ formula for fixed-point-
concyclic; correction to the coordinate route's self-assessment

This round produced no new positive closure, but did produce five
independently-verified exact algebraic results (see "Approaches tried"
above) and one important correction: the coordinate/rotation-parametrization
route's branch-selection gap is **not** "closed except for `G_{2b}`
exclusion" as round 6's summary stated — `coordinate-bash-resultant-
boundary-pointwise` discovered a previously-unrecognized second sub-question
even on the believed-closed `G_{2a}` branch (a same-root correlation between
the containment/sign-test-selected root and the "true equation" root),
proved a new parity lemma about it (`W(r_1)W(r_2)\le0` on `G_{2a}`'s roots,
mirroring the certified `G_{2b}` template) but left the correlation itself
open (numeric-only, independently reconfirmed by the proof-reviewer via a
from-scratch reconstruction). No certified lemma is retracted — all remain
true as narrowly stated — but the "what remains" bookkeeping below is
corrected accordingly.

For the Ptolemy route, both `ptolemy-trig-identity` and its new sibling
`ptolemy-trig-identity-parity-decomposition` independently found, and the
proof-reviewer independently verified from scratch, exact identities
showing two natural-looking "simplify via radical-clearing/discriminant-
product" routes are each **provably equivalent in difficulty** to the
master claim `\Psi>0` itself — valuable negative information narrowing
future search, not progress toward `\Psi>0` itself.

`fixed-point-concyclic` produced a genuinely new, unconditional (unrelated
to root-counting), independently-verified closed-form determinant formula
for `\chi` in terms of `H_1,H_2,H_3,B,C` (Theorem 6/7) — real new machinery,
though the final gap (`\mathrm{Rem}=0`, not a formal consequence of realness
alone) remains open.

## Round 8 update — the whole live population's remaining gap is now proved
to be the SAME algebraic condition

This round produced no new closure of branch selection itself, but it did
prove, unconditionally and independently-verified, that
**`fixed-point-concyclic`'s remaining content (`\mathrm{Rem}=0`) is a free
formal corollary of `G_{2a}=G_{3a}=0`** (Theorem 8,
`lemmas/rem-zero-free-corollary-of-genericity-branch.md`) — this route no
longer has any independent algebraic content beyond the coordinate route's
own branch-selection question. Combined with `inversion-at-A-collinearity`'s
proof that its own reformulation is **literally** (not just equivalently)
the same target as `fixed-point-concyclic`'s cross ratio, this closes off
an entire family of alternative framings (bilinear/Cramer determinant
algebra, inversion-based collinearity) as genuinely distinct routes to the
answer — they are now proved to be the identical problem in different
notation, not merely similarly hard.

`coordinate-bash-resultant-boundary` closed its discriminant sub-step
completely and unconditionally (`\mathrm{disc}(Q)=16\sin^2A`), found and
proved (by explicit counterexample) that its own previously-planned lever
(`M_0\le r_2`) cannot work, and produced a corrected, precisely-scoped
two-part trigonometric target (I),(II) via the Law-of-Sines substitution.
`coordinate-bash-resultant-boundary-pointwise` proved, unconditionally, which
of `G_{2a}`'s two roots the `L_1<0` sign test selects (always the smaller
root), sharpening Theorem 11.8 and narrowing its own same-root correlation
gap to a concrete two-case sign question.

**Net assessment: the population has converged, provably (not just
empirically), onto a single shared bottleneck.** Closing branch selection
for the coordinate/rotation-parametrization route — specifically, (a)
`coordinate-bash-resultant-boundary`'s `G_{2b}` exclusion (now precisely
the two trigonometric inequalities (I),(II)), and (b)
`coordinate-bash-resultant-boundary-pointwise`'s `G_{2a}`-internal same-root
correlation (now precisely the sign of `W(r_{\mathrm{lo}})`) — now suffices
to complete **every** live route simultaneously (coordinate,
fixed-point/bilinear, and inversion-based), since all have been proved,
this round or previously, to reduce to exactly this one condition. Per
CLAUDE.md's shared-gap-plateau guidance: since this is now a *proved*
structural coincidence rather than a suspected one, and multiple genuinely
different framings (four across the population's history: coordinate/
resultant, Ptolemy/trig, fixed-point/bilinear, inversion) have all been
shown to collapse onto the identical polynomial-sign-pattern obstruction,
the priority for future rounds should shift from "diversify framing
further" (largely exhausted — the last two new framings both collapsed
into the existing target) to "attack the shared polynomial-sign target
itself with a technique not yet tried on it" — e.g. Sturm's theorem /
sign-variation counting on the now-explicit trigonometric inequalities
(I),(II) and the `\sigma_K,\sigma_N` sign questions, rather than another
resultant/Vieta variation or another framing that will most likely also
reduce to the same target.

## Round 9 update — `G_{2a}`-side branch selection now FULLY closed; the
`G_{2b}`-side (Y,B2,Z)/Case-(b) exclusion is now the ONLY remaining gap

This round closed both of round 8's two precisely-scoped sub-questions on
the `G_{2a}` side: (a) the same-root correlation `W(r_{\mathrm{lo}})>0` is
now proved unconditionally, in both cases, by
`coordinate-bash-resultant-boundary-pointwise` (a genuinely new "evaluate
at the sibling's own zero" technique, turning the harder case into a
perfect square); (b) `coordinate-bash-resultant-boundary`'s claim `(I)` is
now fully closed unconditionally, and claim `(II)` is closed on the
sub-case `Y(\gamma)\ge0` (proved to be the majority of the domain-nonempty
sample space, per round 8's own numeric estimate). **Neither approach
touches `G_{2b}` exclusion** (the true/spurious-branch three-way sign
classification `(Y,B_2,Z)`), which — combined with the still-open
`Y(\gamma)<0` sub-case of `(II)`, itself understood (via the population's
proven structural-equivalence theorem) to be the same underlying
obstruction — is now, more sharply than ever, the **single** remaining gap
for the entire population (coordinate, fixed-point/bilinear, and
inversion-based routes all reduce to it).

## Full proof

*(The historical `## Round 9 update` text immediately above is preserved for the
record; the sole gap it names — `(II)` on `Y(\gamma)<0` — was closed over rounds
20–22. The complete, reviewer-verified proof follows. Source approach:
`approaches/coordinate-bash-resultant-boundary-pointwise-tangent.md`, Status
`solved`, APPROVED round 22.)*

**Claim.** Let `ABC` be a triangle, `M,N` the midpoints of `AB,AC`, `K,L,O`
the points of the problem statement (`K` inside `\triangle BMC`, `L` inside
`\triangle BNC`, with `\angle KBA=\angle ACL`, `\angle LBK=\angle LNC`,
`\angle LCK=\angle BMK`, `K` inside `\angle LBA`, `L` inside `\angle ACK`, and
`O` the circumcenter of `\triangle AKL`). Then `OM=ON`.

**Step 1 (polarization, `lemmas/vector-reduction-OM-ON.md`).** Place `A` at the
origin. Then `OM=ON \iff O\cdot(C-B)=(|C|^2-|B|^2)/4`, an elementary polarization
identity valid for every `O`. This is the exact ORIGINAL claim, restated.

**Step 2 (rotation parametrization + branch selection, certified chain).** The
angle conditions encode `K,L` (a 1-parameter family) via a rotation
parametrization of the circumcenter `O`; the defining condition on `O` reduces —
through the certified lemma chain `bilinear-chi-cramer-formula.md`,
`homogeneity-decoupling-rotation-param.md`,
`complex-affine-L1-DK-and-r-lo-selection.md`,
`w-r-lo-positive-via-zN-zK-evaluation.md` (G2a same-root correlation, round 9),
the genericity certificate `symbolic-genericity-certificate.md` (round 3), the
magnitude bound `magnitude-bound-and-sign-coincidence.md` (round 6), and G2a
selection (§11) — to the two-part trigonometric target of
`coordinate-bash-resultant-boundary.md` §15, for every `A,B>0` with `A+B<\pi`
(WLOG `\angle B\le\angle C`, `\gamma:=\angle B\le\pi/2`, `\cos B>0`) and every
`\beta\in(0,\gamma)`, with `\beta_0(A):=(\pi-A)/3`, `X_0:=\sin B\cos A/(2\sin(A+B))`,
`m:=\sin B/\sin(A+B)`, `Y(\beta):=2\cos^2\beta-m\cos A`,
`f(\beta):=2\sin(A+B)(\sin\beta+\sin A)-\sin B\sin(A+\beta)`, `K:=2\sin A\sin(A+B)`,
`G(\beta):=2K-f(\beta)`:
- `(I)`  `\sin(A+3\beta)<0 \implies f(\beta)>0`;
- `(II)` `[\,Y(\beta)>0\,]\wedge[\,\sin(A+3\beta)<0\,] \implies G(\beta)>0`.
(The G2b-side exclusion is proved structurally identical to `(II)` on `Y(\gamma)<0`;
so once `(I)\wedge(II)` holds for all `\beta`, branch selection is complete and
Steps 1–2 deliver `OM=ON`.) Since `Y(\beta)=2\cos^2\beta-2X_0` and
`\sin(A+3\beta)<0\iff\beta>\beta_0`, the hypothesis of `(II)` is exactly
`\beta\in(\beta_0,\beta_1)`, where `\beta_1\in[0,\pi/2)` is the angle with
`\cos^2\beta_1=X_0` (when `X_0\in[0,1]`).

**Claim `(I)` (Theorem 16.1, `claim-I-closed-and-claim-II-caseA-closed.md`, round 9).**
`f'(\beta)=\sin(A+\beta)\cos B+\sin(A+B-\beta)>0` on `(0,\gamma)` (both terms `>0`),
so `f` is strictly increasing; `f(\beta_0)>0`; hence `f>0` on `(\beta_0,\gamma)`,
which is exactly where `(I)`'s hypothesis is active. `(I)` holds. `\blacksquare`

**Claim `(II)` — trichotomy on `\beta_1` against the ordered cutpoints
`\beta_0(A)<\gamma`** (domain-nonempty premise; if `\beta_0(A)\ge\gamma` the target
is vacuous). Exactly one of:

- **Case (a) `\beta_1\le\beta_0(A)`** (round 21, `Case (a) vacuity lemma`).
  `\beta_1\le\beta_0\iff Y(\beta_0)\le0`; by `Y'=-2\sin2\beta<0`, `Y(\beta)<Y(\beta_0)\le0`
  for `\beta\in(\beta_0,\gamma)`, so `(II)`'s hypothesis `Y(\beta)>0` fails there,
  and for `\beta\le\beta_0` the other conjunct `\sin(A+3\beta)<0` fails. `(II)` is
  vacuous throughout `(0,\gamma)`.

- **Case (b) `\beta_0(A)<\beta_1<\gamma`.** `(II)`'s hypothesis is `\beta\in(\beta_0,\beta_1)`;
  since `G` is strictly decreasing (`G'=-f'<0`), the worst case is `\beta\to\beta_1^-`,
  so it suffices to prove `G(\beta_1)\ge0`. This holds unconditionally: `P\le0` and
  `P>0\wedge E\ge0` (round 10, `case-b-p-le-0-and-e-ge-0-closed.md`), and
  `P>0\wedge E<0` via `T:=B_c^2X_0-E^2\ge0` on `\mathcal D_b` (round 20,
  `t-nonnegative-on-case-b-residual-domain.md`, a corner Taylor+Lagrange-remainder
  argument glued to a certified `mpmath.iv` sweep). (Independently, the Reduction
  Lemma route — hypothesis (A) `Tgt>0`, round 16
  `tgt-strictly-positive-throughout-D-full.md`; hypothesis (B) `D_1\ge0`, round 18
  `d1-nonnegative-on-boundary-curve.md` — gives the same conclusion.)

- **Case (c) `\beta_1\ge\gamma`** (round 22, Theorem 16.2 first branch, round 9,
  `theorem-16-2-first-branch-caseC-closure.md`). `\beta_1\ge\gamma\iff Y(\gamma)\ge0`.
  Then `Y(\beta)>Y(\gamma)\ge0` on `(0,\gamma)` (monotonicity), so `Y(\beta)>0`
  never restricts. And `G=2K-f` strictly decreasing with
  `G(\gamma)=2K-f(\gamma)=\sin(A+B)(2\sin A-\sin B)`, where `2\sin A-\sin B>0` is
  derived from the exact identity
  `\cos B(2\sin A-\sin B)-\sin(A+B)Y(\gamma)=\sin B(\cos\delta-\cos B)`
  (`\delta:=\pi-2B-A=C-B`, with `0\le\delta<B` from the domain-nonempty premise
  `A+3B>\pi` — non-circular) together with `\sin(A+B)Y(\gamma)\ge0` and `\cos B>0`.
  Hence `G(\beta)>G(\gamma)>0` for every `\beta\in(0,\gamma)`, so `(II)` holds
  outright (and A obtuse, `X_0<0`, falls here since then `Y(\gamma)>0`).

The three cases are exhaustive and disjoint (a real-number split; `X_0>1` never
occurs, `X_0<0\Rightarrow Y(\gamma)\ge0\Rightarrow` Case (c)). So `(II)` holds for
every `\beta\in(0,\gamma)`, every triangle.

**Conclusion.** `(I)\wedge(II)` holds for all `\beta\in(0,\gamma)` and all triangles;
this completes branch selection (G2b exclusion), so by Step 2 the reduced condition on
`O` holds, and by Step 1's polarization `O\cdot(C-B)=(|C|^2-|B|^2)/4`, i.e.
**`OM=ON`**, for every triangle `ABC` satisfying the hypotheses. The isosceles case
`AB=AC` is additionally handled directly by `lemmas/isosceles-case-symmetry.md`.
`\blacksquare`

*(Independent reviewer verification, round 22: all Facts 0/3/4/5 and `f'` symbolic
residual `0`; `(I)\wedge(II)` 0 violations / 600k triangles; Case (c) mechanism 0
violations / all 25,903 Case-(c) triangles; Case (b) target `G(\beta_1)\ge0` 0
violations / 44,304 Case-(b) samples; boundary corner `X_0=\cos^2B^\ast=3/8` exact.
Nature of proof: Case (b) uses rigorous certified interval-arithmetic sweeps —
a computer-assisted proof.)*
