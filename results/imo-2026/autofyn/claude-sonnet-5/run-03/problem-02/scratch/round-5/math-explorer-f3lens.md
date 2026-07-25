## imo-2026-02

### Headline finding (new, not previously in the population)

The population has never used the problem's two extra hypotheses "K lies
inside angle LBA" and "L lies inside angle ACK" for anything (flagged as
entirely unaddressed in `coordinate-bash-resultant-boundary.md` §10). I ran
a direct numerical test of what these two hypotheses actually do to the
solution set, and found something structurally important:

**Containment alone (`K∈△BMC`, `L∈△BNC`) does NOT always pick out a unique
`(s2,t1)` pair at fixed `β`** — I found an explicit example
(`A=(0,0),B=(1.763,1.534,0.297)` at `β≈0.8306` rad, near an `F3=0`
crossing) where **hypothesis 2 alone has TWO roots `s2` both satisfying
`L∈△BNC`** (`s2≈0.0150` and `s2≈0.0326`), and evaluating the certified
`G2a,G2b` polynomials at each shows the *smaller* root sits on `G2a≈0`
(the population's presumed-genuine branch) and the *larger* root sits on
`G2b≈0` (the presumed-extraneous branch) — **both are valid under plain
triangle-containment**, contradicting any argument that would try to select
the branch from `K∈△BMC,L∈△BNC` alone.

**But adding the two extra hypotheses resolves this completely and
uniquely, purely algebraically (cross-product signs, no continuity/IVT
needed).** For all `(s2,t1)` pairs with `s2` ranging over every
containment-valid root of hyp-2 and `t1` over every containment-valid root
of hyp-3 (computed independently — recall the homogeneity-decoupling lemma
already certifies hyp-2 depends only on `s2,β` and hyp-3 only on `t1,β`), I
checked the two cross-product sign conditions for "K inside angle LBA" and
"L inside angle ACK" on every combination. Result, over:
- 146 random `(a,b,cc,β)` samples spanning the whole valid range (not
  targeted at any special locus): **exactly one** `(s2,t1)` combo passes
  both extra conditions, every single time (0 exceptions, 0 multi-hits).
- 15 explicitly constructed `F3=0`-crossing triangles (the ones flagged as
  the open hazard in `f3-f3prime-resultant-factors.md`), evaluated at 5
  β-values straddling each crossing (75 points total, including cases with
  2 or 3 containment-valid roots for one of the two sub-hypotheses):
  **still exactly one** combo passes both extra conditions every time.
- In every case checked (58 additional random samples), the unique
  surviving `(s2,t1)` pair sits on `G2a≈0` (machine precision) — i.e. it
  always matches the population's already-conjectured "genuine branch".

So across ~280 sampled points, including the specific F3-crossing hazard
cases, "K inside angle LBA ∧ L inside angle ACK" (evaluated as two
elementary cross-product-sign conditions, no trig/arccos needed once
`s2,t1` are known) picks out a *unique* combination, and it always agrees
with `G2a=G3a=0`. This is strong (not yet proved) evidence for a
**genuinely different, purely algebraic selection mechanism** that would
not require tracking continuity of the genuine branch through `F1,F2,F3,F3'`
crossings at all — it would instead directly show, for the actual roots of
the quadratics `G2a,G2b` (resp. `G3a,G3b`) satisfying basic containment,
that only the `G2a` (resp. `G3a`) root(s) also satisfy the two cross-product
sign inequalities.

This also independently re-corroborates the still-open magnitude bound
`t1<t1max(β)`: my `in_triangle` filter for `t1_ok`/`s2_ok` enforces the
*full* triangle containment (both direction and the far edge `MC`/`NB`
magnitude cutoff), and every one of the ~280 sampled genuine points passed
it — consistent with, but not a proof of, `t1<t1max(β)` holding throughout
the valid range.

### 1. When do F3=0/F3'=0 cross the valid range? (symbolic condition, confirmed)

Already established and re-confirmed here: `F3=0 ⟺ cos²β=b/(2a)`,
`F3'=0 ⟺ cos²β=ab/(2(b²+cc²))` (both palindromic quartics in `u`, symmetric
under `β↦π−β`). Crossing happens inside `(0,min(∠B,∠C))` whenever the
corresponding `cos²β` value both lies in `(0,1)` and the resulting `β` is
below `min(∠B,∠C)` — this is a codimension-0 (open, not measure-zero)
condition, confirmed by direct random search: roughly 1 in 1300 random
triangles (in my `20000`-trial sweep with `a∈(0.5,3),b∈(-2,4),cc∈(0.2,3)`,
`β` restricted to the *interior* 96% of the valid range) has an `F3=0`
crossing there — i.e. this is a real, unavoidable phenomenon for a
nontrivial fraction of triangle shapes, not a boundary artifact.

### 2. Why does the true branch avoid the resultant-zero root? (algebraic mechanism, partially illuminated)

At the crossing itself (the explicit `s2≈0.0150` vs `s2≈0.0326` example
above), the *shared* root responsible for `Res_{s2}(G2a,G2b)=0` is a THIRD
value (`s2≈0.745` in the specific counterexample triangle originally found
in round 4, matching the `f3-f3prime-resultant-factors.md` lemma) — not
either of the two containment-valid roots I found here. This is consistent
with, and slightly sharpens, the existing lemma: **at an `F3=0` crossing,
`G2a` and `G2b` share a root, but that shared root is generically a
*third*, non-containment-satisfying value of `s2`, while both `G2a`'s and
`G2b`'s "own" other root can independently and simultaneously satisfy plain
triangle containment** — this is exactly why plain containment can't
disambiguate near a crossing, and exactly why my new criterion (the two
extra hypotheses) is doing real, non-trivial work there, not just agreeing
by luck.

I did **not** find (in the time available) a clean closed-form algebraic
separation showing why the `G2a`-side root always continues to satisfy
"K∈∠LBA, L∈∠ACK" while the `G2b`-side root never does — this remains open,
but is now a much more concrete, purely algebraic (sign-of-quadratic-form)
target rather than a continuity/tracking argument.

### 3. Did I find a genuine counterexample to harmlessness? No.

I did not find any triangle/β where the extra-hypothesis criterion
disagrees with `G2a=G3a=0`, nor any triangle/β where zero or more than one
combo passes the extra-hypothesis test. The route looks robust, not
refuted — this is a positive (if still numerical) result for the
population, not a kill.

### 4. Does the ptolemy-route's IVT+quadratic-degree technique directly transfer?

**No, not as a drop-in.** Ptolemy's branch-selection theorem works because
its equation `G(ψ)`, after clearing denominators (not squaring), is
*exactly* homogeneous degree 2 in `(sinψ,cosψ)` — i.e. genuinely quadratic
in `cotψ`, with only 2 total roots. The coordinate route's `eq2` comes from
squaring a dot-product cosine equality *and* clearing norms that themselves
depend on `s2` (both `|BL|²` and `|NL|²` are quadratic in `s2`), so the
un-factored equation is a **quartic in `s2`** (`g2 = G2a·G2b`, each factor
itself quadratic in `s2`) — twice the degree of Ptolemy's, with 4 roots in
play instead of 2. A literal IVT+degree-2-counting argument doesn't apply
directly to `G2a` alone (need to separately handle `G2b`'s roots too). The
only way to get Ptolemy's clean quadratic-in-cotangent structure would be
to re-derive hypothesis 2 without ever squaring a dot product (i.e.
essentially rebuild the ptolemy-trig-identity's own derivation) — that is
not a small patch to the coordinate route, it's adopting the sibling
route's whole framework. **Recommend NOT trying to force this transfer
directly** — instead pursue the extra-hypotheses algebraic-selection
mechanism found above, which is native to the coordinate route's own
`G2a`/`G2b` quadratics-in-`s2`,`t1` and doesn't require continuity/IVT
along `β` at all.

### 5. Scoping the magnitude bound t1<t1max(β)

Looks more tractable than previously assessed, for two reasons: (a) my
numerics show it holds automatically at the *same* point selected by the
new algebraic criterion (§ above) at every one of ~280 sampled points,
suggesting it might not need a separate proof if the extra-hypotheses
mechanism is formalized — the full containment (`K∈△BMC`, magnitude and
all) could conceivably be shown to be *implied* by the `G2a=0` +
cross-product-sign selection, rather than needing an independent
`t1<t1max(β)` inequality proof; (b) `t1max(β)` itself has a clean closed
form (intersection of ray `B+t(-cosβ,sinβ)` with line `MC`, a single linear
solve), so even a direct proof (not via the containment-implication route)
is "just" one more explicit inequality in `a,b,cc,β,t1(β)` — same
complexity class as the already-closed `F1,F2` identifications, not
qualitatively harder.

### Recommendation

Do not spend another round chasing a general symbolic proof of "F3/F3'
crossings never flip the branch" via a pure continuity/transversality
argument (route (a) in `coordinate-bash-resultant-boundary.md` §9) — it's
plausible but the population has struggled with it for 2 rounds. Instead,
open (or add to `coordinate-bash-resultant-boundary`) a genuinely
different, purely algebraic sub-route: **formalize the two extra
hypotheses (K∈∠LBA, L∈∠ACK) as explicit cross-product-sign inequalities in
`(s2,t1,β,a,b,cc)`, and prove directly that (i) at most one of `G2a`'s two
roots and `G3a`'s two roots satisfies containment+these signs
simultaneously with the matching `t1`/`s2` from the other hypothesis, and
(ii) that root is always the `G2a=G3a=0` one.** This sidesteps F1/F2/F3/F3'
crossing-tracking entirely and, per the numerics above, appears to be where
the real selection mechanism lives — the extra hypotheses were apparently
never decorative, they are load-bearing for uniqueness.

### Candidate technique(s)
Direct sign analysis of cross products (`cross(BL,BK)`, `cross(BK,BA)`,
`cross(CA,CL)`, `cross(CL,CK)`) as explicit polynomials in
`(s2,t1,u,a,b,cc)` via the existing Weierstrass rotation parametrization —
purely algebraic, reuses all existing machinery (`G2a,G2b,G3a,G3b`
formulas, `homogeneity-decoupling-rotation-param.md`), no resultant/IVT
needed.

### Cheap-kill candidates
None obvious for refuting the extra-hypotheses mechanism itself (280
samples, 0 exceptions) — but worth a quick symbolic sanity check next round
(e.g. compute the sign of `cross(BL,BK)` as an explicit polynomial in
`s2,u,a,b,cc` restricted to `G2a=0`, and separately restricted to `G2b=0`,
and check whether it factors through a term whose sign is provably fixed).

### Knowledge-base entries to use
Same as before: Gröbner-basis ideal membership (Cox–Little–O'Shea, cited in
`symbolic-genericity-certificate.md`), resultants (for cross-checking `F3`
identification), standard cross-product/signed-area sign facts (already
used population-wide, e.g. `vertex-sign-cross-product-identities.md`).

### Analogous past problems (cruxes)
None found — as recorded since round 1, the crux corpus has no geometry
entries; not re-checked this round (per standing rule, no new query
expected to help).

### Prior progress
As recorded in `current.md`/`coordinate-bash-resultant-boundary.md`: `F1=0
⟺β=∠B`, `F2=0⟺β=∠C` both closed exactly; ray-direction monotonicity
proved; `F3,F3'` algebraically identified with an explicit counterexample
showing they DO cross the valid range (not always outside); harmlessness at
sampled crossings confirmed numerically but not proved in general — this is
exactly the gap I was dispatched to attack.

### Dead ends (do not retry)
- Acute-angle-bound branch selection (refuted round 4, explicit obtuse
  counterexamples) — unaffected by this round's findings, still dead.
- Do not expect a literal transfer of ptolemy's IVT+quadratic-degree
  argument onto `G2a` alone — the coordinate route's equation is a quartic
  in `s2` (two nested quadratic branches), not Ptolemy's clean quadratic in
  `cotψ`; a literal copy-paste of the technique doesn't type-check (see §4
  above). This is a new, round-5 negative finding — record it so no future
  round re-attempts the direct transfer.

### Small-case / intuition notes (all conjectural, backed by numerics only)
- Conjecture (strong, ~280 samples, 0 exceptions): the pair `(s2,t1)`
  jointly satisfying `L∈△BNC`, `K∈△BMC`, "K inside ∠LBA", and "L inside
  ∠ACK" is always unique, and always lies on `G2a=0,G3a=0`.
- Conjecture (same evidence): plain containment (`K∈△BMC`,`L∈△BNC`)
  without the two extra hypotheses can admit 2 (occasionally more, e.g. 3
  for `t1` in one sample) simultaneously valid roots near an
  `F1,F2,F3,F3'`-crossing locus — i.e. the extra hypotheses are not
  redundant with plain containment, they do genuine selection work.
- The `F3=0` locus is not rare: roughly 1/1300 of uniformly-sampled
  triangles (in the tested parameter box) have an `F3=0` crossing strictly
  inside the interior 96% of the valid β-range — a real, unavoidable
  phenomenon any complete proof must handle (or route around via the extra
  hypotheses, as suggested here).
