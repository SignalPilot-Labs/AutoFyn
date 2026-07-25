# Round 18 — proof-outliner field

**Note on inputs.** `/tmp/round-18/math-explorer-diversity.md` does not
exist on disk (only `math-explorer-gap6.md` was found) despite being
named in this round's dispatch. I have reconstructed the diversity
report's two claimed findings — (a) the SOS route's 3 concrete
diagnostic next-tests, (b) `spiral-similarity-bootstrap` as an untried,
genuinely-different framing — from the orchestrator's own summary of it
in the dispatch prompt, cross-checked against `current.md`'s round-17
entry for `-sos` (which independently corroborates the SDP-degeneracy
diagnosis: 3 of 5 near-null eigenvalues still unexplained after pinning
2 to `s^\ast`) and by reading `spiral-similarity-bootstrap.md` directly.
The SOS outline below is written from that reconstruction; flag to the
outline-reviewer that the underlying report should be re-generated if
finer diagnostic detail is needed before dispatch.

---

## 1. TOP PRIORITY — `coordinate-bash-resultant-boundary-pointwise-tangent` (revise)

**Current state (verified by reading `current.md` round 17 + the live
file + `lemmas/d1-nonnegative-on-boundary-curve.md`).** The route's
Reduction Lemma (New result 1, round 13, certified) needs exactly two
hypotheses to conclude `f\ge g` throughout `\mathcal D`, hence `OM=ON`:
- **(A)** `\partial(f-g)/\partial B>0` on `\mathcal D` — **closed**,
  round 16, via `lemmas/tgt-strictly-positive-throughout-D-full.md`
  (Open gap 5). Independently re-verified twice since (rounds 16, 17
  reviewer passes). Not touched by anything this round — do not re-open.
- **(B)** `D_1(A)\ge0` on the boundary curve `\mathcal C` — **open**
  (Open gap 6). `lemmas/d1-nonnegative-on-boundary-curve.md` proves this
  in Steps 1-4 (certified `mpmath.iv` MVT-gluing machinery, independently
  reviewed and found sound) **conditional on Step 0**
  (`D_1(B^\ast)=0`), which itself rests on two facts: (i)
  `G(\beta_0(A^\ast))=0` (already certified,
  `lemmas/star-corner-is-boundary-cusp-not-critical-point.md`) and (ii)
  `X_0(A^\ast,B^\ast)=\cos^2B^\ast` (i.e. `h(A^\ast)=0` in the gap6-lens
  report's notation) — **this was the one fact the round-17 reviewer
  found unproved** (a six-round-old numeric-only coincidence, first
  disclosed as such in round 11), and is the sole reason the lemma was
  rejected and the route's Status reverted from the builder's false
  `solved` claim back to `partial`.

**This round's find.** `/tmp/round-18/math-explorer-gap6.md` reports an
exact, independently-double-checked (fresh `sympy.expand_trig`+
`simplify`→literal `0`, plus 40-digit `mpmath` residual checks at 5
points including `A^\ast` itself) symbolic identity
$$G_{\mathrm{curve}}(A)=-8\sin(u)\cos^2(u)\cdot h(A),\qquad u:=A/3+\pi/6,$$
proved by hand via the classical multiple-angle expansions
`\sin3u=3\sin u-4\sin^3u`, `\sin5u=16\sin^5u-20\sin^3u+5\sin u`,
`\cos2u=1-2\sin^2u`, reducing both sides to the identical degree-5
polynomial `-16s^5+22s^3-6s` in `s:=\sin u` — fully hand-checkable, not a
black-box `simplify`. Combined with the already-certified `0<A<\pi/2` on
the relevant domain `\mathcal D` (round 11 of
`coordinate-bash-resultant-boundary-pointwise.md`, giving
`u\in(\pi/6,\pi/3)\subset(0,\pi/2)` hence `\sin u,\cos u>0` strictly, no
case split), the cofactor `-8\sin u\cos^2u` is nonzero at `A=A^\ast`, so
`G_{\mathrm{curve}}(A^\ast)=0\iff h(A^\ast)=0`. Given the already-certified
`G_{\mathrm{curve}}(A^\ast)=0`, this yields `h(A^\ast)=0` — **exactly
fact (ii)**, by genuine elimination-style algebra (a common-factor
argument via multiple-angle substitution), not a numeric coincidence.
This is precisely the "resultant/elimination proof that the two
`A^\ast`-defining equations share their root" that round 17's own
`current.md` recommendation asked for, delivered in closed form.

**Sanity check on the claim before trusting it (done here, not just
deferred to the builder).** I re-derived the two defining functions
independently from the raw definitions in `coordinate-bash-resultant-
boundary-pointwise-tangent.md` (`X_0,\beta_0,K_c,P,Q,G`) myself using
`sympy`, confirmed `G_curve(u)` and `h(u)` collapse to the report's
claimed closed forms `h(u)=3/4-2\sin^2u` and
`G_curve(u)=(1-\cos2u)^2\sin u-2\sin u+\tfrac34\sin3u-\tfrac54\sin5u`
under `A=3u-\pi/2`, and that
`sympy.expand(G_curve(u) - (-8*sin(u)*cos(u)**2*h(u)))` returns `0`
after `expand_trig`. This matches the report. The identity is real
algebra, not a numerical artifact — **but it is still only a scouted
finding, not a certified lemma**: it has not gone through outline-review
or been written up by a builder as a from-scratch, fully-cited proof
step, and per the standing dispatch note this must NOT be marked solved
by the outliner. It is flagged as this round's highest-value build
target.

### Outline for the builder

1. **Splice into `lemmas/d1-nonnegative-on-boundary-curve.md`'s Step 0.**
   Replace the round-17-rejected citation to "the two boundary curves
   meet at the corner" (fact (ii), previously asserted without proof)
   with:
   (a) the exact substitution `u:=A/3+\pi/6` and the closed forms
   `h(u)=3/4-2\sin^2u`, `G_{\mathrm{curve}}(u)=(1-\cos2u)^2\sin u-2\sin
   u+\tfrac34\sin3u-\tfrac54\sin5u$, each *re-derived from the raw
   definitions* (not copied) — this is required by the "adapt, don't
   cite" rule even though the identity is now known;
   (b) the multiple-angle expansion reducing both to the polynomial
   `-16s^5+22s^3-6s` in `s=\sin u`, shown as explicit hand arithmetic
   (this is the part that must be checkable without a CAS, since the
   round-17 rejection specifically called out an opaque `simplify`-to-
   `0` as insufficiently rigorous evidence last time; the polynomial
   form sidesteps that criticism entirely);
   (c) the domain fact `0<A<\pi/2\Rightarrow u\in(\pi/6,\pi/3)
   \Rightarrow\sin u,\cos u>0`, citing round 11 of
   `coordinate-bash-resultant-boundary-pointwise.md` for `0<A<\pi/2` on
   `\mathcal D`;
   (d) the conclusion `G_{\mathrm{curve}}(A^\ast)=0\iff h(A^\ast)=0`
   (an iff, since the cofactor is nonzero), applied with the
   already-certified `G_{\mathrm{curve}}(A^\ast)=0`
   (`lemmas/star-corner-is-boundary-cusp-not-critical-point.md`) to get
   `h(A^\ast)=0`, i.e. fact (ii), i.e. `X_0(A^\ast,B^\ast)=\cos^2B^\ast`
   **exactly**.
2. **Re-verify Step 0's final line** (`D_1(B^\ast)=0`) now goes through
   cleanly with fact (ii) actually proved — it was already correct
   *algebra* conditional on (i)+(ii); only the justification of (ii)
   changes, so Steps 1-4 of the lemma (the certified `mpmath.iv`
   enclosure of `B^\ast`, the derivative-sign sweep, the value sweep,
   the MVT gluing) do **not** need to be redone, only re-cited.
3. **Trace the full chain once more for any OTHER silent gap** before
   the file's "Full proof" section can legitimately claim `solved` —
   the dispatch explicitly requires this. Concretely the builder should
   check, and record explicitly in the approach file:
   - Does anything else in the Reduction Lemma's hypothesis (A) or (B)
     derivation implicitly use the same "coincidence" fact (ii) or any
     other unproved numeric coincidence? (Round 17's reviewer explicitly
     checked hypothesis (A)/gap 5 and found it independent, via a
     *different*, exactly-computable corner `(\pi/3,\pi/3)` — re-confirm
     this remains true, it should still be a one-line citation, not new
     work.)
   - Does `lemmas/star-corner-is-boundary-cusp-not-critical-point.md`
     itself rest on anything unproved? (It was independently certified
     already — re-cite, don't re-derive, but the builder must state this
     check was made.)
   - Does the branch/domain characterization `0<A<\pi/2` used in step
     1(c) above hold on the *exact* sub-locus of `\mathcal D` where
     `D_1(A)\ge0` is being invoked (not just "somewhere")? — confirm the
     citation's scope matches exactly.
   - Any other place in `coordinate-bash-resultant-boundary-pointwise-
     tangent.md`'s full dependency chain (Theorem A/B/C, the domain
     characterization, the two-hypothesis Reduction Lemma itself) that
     was flagged provisional/numeric anywhere in rounds 11-17 and never
     definitively closed. A full grep of the file for "numeric",
     "unproved", "conjectur", "not proved" is a cheap, worthwhile check.
4. If all of this holds up, the builder may propose Status `solved` —
   but the proof-reviewer, not the builder or outliner, makes that call
   final. If the reviewer finds a further silent gap, the route reverts
   to `partial` as it did last round; that is an acceptable, expected
   outcome and should be reported honestly either way.

**This is the round's clear top build priority**: if it holds, it
completes the entire problem via this route. If it doesn't, the precise
failure mode (which sub-step broke) sharpens the gap further, as has
happened every round on this route since round 11.

---

## 2. `coordinate-bash-resultant-boundary-pointwise-sos` (advance, insurance route)

**Current state.** Constrained-SDP work has pinned 2 of 5 near-null
eigenvalues of the Gram matrix to the exact algebraic locus `s^\ast` (a
genuine `sympy` `CRootOf` of a degree-16 polynomial, confirmed not a
low-precision float) but 3 directions remain structurally unexplained,
now confirmed at a second, independent witness point (`\cos B=3/5,\sin
B=4/5,u=7/100`) reproducing the same `\approx99.9999999989\%`
one-direction-dominance pattern. No certificate claimed anywhere;
honestly scoped throughout (round 17 reviewer confirmed no
overclaiming).

**Outline for the builder — the 3 concrete diagnostic tests** (per the
diversity report's reconstructed recommendation, aimed at explaining the
remaining 3 null directions rather than continuing to search blind):

1. **Real-root test on `n2`/`n4sq` at the witness point.** At the fixed
   witness `(\cos B,\sin B,u)=(3/5,4/5,7/100)$ (and re-run at the
   original witness for cross-check), compute the real roots of `n2(s)`
   and `n4sq(s)` (the two degree-`\le5`-ish polynomials in `s=\tan(A/6)`
   or the file's own root variable — pull the exact definitions from
   `coordinate-bash-resultant-boundary-pointwise-sos.md`'s own Theorem 4
   apparatus) and check whether any of the 3 unexplained null directions
   correspond to an additional *real* shared root beyond `s^\ast` — i.e.
   whether `n2` and `n4sq` (or their relevant factors) have a second
   common real zero on the domain that the SDP is "seeing" but the
   population hasn't yet identified algebraically.
2. **Conjugate-pair root check.** For each of the 3 unexplained
   directions, check whether they instead correspond to a *complex
   conjugate pair* of roots of the same polynomial(s) (which would not
   show up as a real vanishing locus but can still force near-null
   directions in a real SDP's Gram matrix via a real quadratic factor
   with small discriminant) — compute the discriminant of the relevant
   quadratic factor(s) numerically at both witness points and see if any
   is anomalously close to `0` (a near-double-root signature).
3. **`z''(s^\ast)` test.** Having already pinned `M_0z(s^\ast)=0` and
   `M_0z'(s^\ast)=0` (round 17), test whether `M_0z''(s^\ast)=0` also
   holds (i.e. whether the null space is explained by vanishing to
   *third* order at `s^\ast`, not just first/second) — if so, this
   reframes the whole degeneracy as "the Gram matrix's kernel is exactly
   the 3-jet of `z` at `s^\ast`," a clean structural explanation that
   would finally close the rank-deficiency diagnosis (though not by
   itself produce a certificate).

Report results honestly whichever way they land — a clean explanation of
all 5 null directions would be genuine progress even without a
certificate; a fourth still-unexplained direction is also useful
information. Status should remain `partial` regardless unless an actual
SOS certificate is found.

---

## 3. `coordinate-bash-resultant-boundary` — SKIP this round; open `spiral-similarity-bootstrap` instead

**Judgment call, with justification.** `coordinate-bash-resultant-
boundary`'s last state (round 17): `\mathrm{NewGen}(G_0,G_0)`, a genuine
unconditionally-nonnegative degree-10 generator family, independently
verified exact and nonnegative on the full unit square — real progress,
but by the file's own honest accounting the degree (10-17) is far above
the target `-q_1,-r_0`'s degree (6-7), so this generator structurally
cannot close the LP no matter how the search is re-run; the central
certificate has been sought for 15 rounds (`expanded: 15`) without
closing. Nothing in this round's explorer reports supplies a new lever
for this route (neither report touches it), so a bare "keep searching
the same LP" instruction would not meaningfully advance it and risks
another round of no-progress "expanded" churn on an approach that is
`stale: true` in the ranker sidecar already.

Meanwhile, the diversity report (per the dispatch's summary) found that
4 of the population's "synthetic" framings collapse into the same target
as coordinate-bash, i.e. the live population is heavily concentrated on
one underlying algebraic target (the coordinate-bash resultant chain and
its many pointwise/SOS/boundary children) — a textbook case of the
CLAUDE.md "population too close together" risk, made sharper this round
precisely because gap6-lens's finding, if it holds, would complete the
*whole problem* via that one framing: a single-point-of-failure outcome
for the run if the reviewer finds one more silent gap in it next round.
`spiral-similarity-bootstrap.md` is confirmed (I read it directly) to be
a genuinely different, synthetic framing — homothety `h(A,1/2)` sending
`B,C\mapsto M,N`, reducing `O\in\ell` via one-angle circle-membership
lemmas rather than any resultant/coordinate machinery — and has never
been built (`selected` field absent from `.ranking.json`, i.e. not yet
registered/built this run). Its own file already flags real risk (steps
4-5's "O = fixed point" framing may be false as stated, since O provably
moves along `\ell`; the file itself suggests a corrected target: "`\ell`
is `h(A,1/2)` of perp-bisector(`BC`)", already free from step 6, with
the real remaining content being a route to `O\in\ell` via the auxiliary
circles directly).

**Decision: open `spiral-similarity-bootstrap` for a real build this
round**, revising its own outline per its file's already-recorded
self-correction (drop the false "O = fixed point" framing; target
`O\in\ell` via steps 1-3's one-angle circle-membership lemmas
`+` step 6's already-free homothety fact, expressing `O\cdot(C-B)` via
those circle memberships and showing it equals `(|C|^2-|B|^2)/4`
directly, per the file's own "Open gaps" section). This is diversity
insurance, not a demotion of `-boundary` — `-boundary`'s file and Elo
(1663, highest non-`-tangent` in the field) are untouched and it can
resume next round if `-tangent` stalls or a fresh lever appears for it.

---

## Recommendation to outline-reviewer

Register/advance no new coordinate-family approaches this round (field
is already saturated there); the priority split is: maximum effort on
closing `-tangent`'s gap 6 for real (top build target), continued
honest diagnostic work on `-sos` (useful either as the route itself or
as informative negative results), and opening `spiral-similarity-
bootstrap` as the round's diversity insurance against the field's
concentration risk. `-boundary` sits out this round without prejudice.

**build set: coordinate-bash-resultant-boundary-pointwise-tangent, coordinate-bash-resultant-boundary-pointwise-sos, spiral-similarity-bootstrap**
