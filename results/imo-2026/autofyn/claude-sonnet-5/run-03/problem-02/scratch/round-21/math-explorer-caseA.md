## imo-2026-02 (lens: Case (a) domain structure)

### Summary of the key finding

Case (a) (`β1≤β0(A)`, in `coordinate-bash-resultant-boundary-pointwise-tangent.md`'s
naming) is **very likely a phantom gap** — a target that was never actually
established as necessary by the population's own rounds 8-10 derivation, but was
silently over-generalized into a universal claim by round-13's "Step 2" write-up
in the `-tangent` file. I could not fully close it in the time budget (that is
outliner/builder work), but I found a precise, well-evidenced structural reason
to suspect it, tracing definitions back through 3 generations of the "Case (a)/(b)"
naming (which the population has recycled with **three different meanings**,
which I believe is the actual source of round 18-20's confusion).

### The three different "Case (a)/(b)" splits in this population (a naming collision)

1. **Theorem 16.2's split** (`coordinate-bash-resultant-boundary.md` §16, line
   3297): `Y(γ)≥0` (Case (a), globally closed, Theorem 16.2) vs `Y(γ)<0` (Case
   (b), the hard case, split further into P/E sub-branches in round 10). Here
   `Y(β):=2cos²β − (sinB cosA/sin(A+B))`, strictly decreasing in `β`.
2. **`-pointwise.md` round 10's "Case (b)"** (line 916-921, its own words: "**the
   open sub-case is**: given `cos²β1=X0`, ... `β1∈(β0,γ)` (Case (b): `β1<γ`;
   corrected domain-nonemptiness ... `β1>β0`) — prove `G(β1)≥0`.") — i.e. round
   10 **explicitly scopes the entire `G(β1)≥0` claim to `β0<β1<γ`** and calls
   *that* "Case (b)". It never claims or attempts anything for `β1≤β0`.
   Crucially, round 10 **found empirically that dropping the `β1>β0` restriction
   is not merely inconvenient but makes the claim FALSE**: "restoring the
   domain-nonempty hypothesis `sin(A+3β1)<0`, i.e. `β1>β0` ... shown genuinely
   necessary, not optional — `8218/25123` violations without it, `0/572,351`
   with it" (`coordinate-bash-resultant-boundary.md` line 3326-3330). This is a
   ~33% violation rate essentially identical in kind to the ~70% violation rate
   round 18-20 rediscovered for their own "Case (a)" ten rounds later — the
   same fact, found once, forgotten, and rediscovered as if new.
3. **`-tangent.md`'s "Case (a)/(b)"** (current, `β1≤β0(A)` vs `β1>β0(A)`,
   introduced at Step 2, line 2142-2143): this treats **both halves as needing
   the same target `G(β1)≥0`** ("the target for every `β1∈(0,γ)` is
   `G(β1)≥0`, no case split in the target itself" — line 51-53, 1975).
   **This is the unjustified step.** No citation anywhere in the population
   (rounds 1-10, nor any lemma file) ever proves or even asserts that
   `G(β1)≥0` is the relevant quantity when `β1≤β0`; round 10's own scoping
   (#2 above) is the only place the claim's domain of applicability is stated,
   and it explicitly excludes `β1≤β0`.

### Why (II)'s original conditional form is vacuous exactly on Case (a)

Round 8's original two-part reformulation (`coordinate-bash-resultant-boundary.md`
§15, line 1917-1934) states (II) as a **conditional on a free variable `β`**, not
a claim about the fixed value `β1`:
```
(II)  [2cos²β > m·cosA]  AND  [sin(A+3β)<0]  ⟹  (G-type conclusion at β)
```
i.e. `Y(β)>0 ∧ β>β0(A) ⟹ conclusion`. Since `Y` is strictly decreasing with
unique zero at `β1` (`Y(β)>0 ⟺ β<β1`), (II)'s hypothesis set is exactly
`β∈(β0,β1)` (intersected with `β0<β<γ`) — **which is empty whenever `β1≤β0`**.
So (II), read literally as the round-8/9 conditional it originally was, is
**vacuously true** in Case (a) — there is no `β` to check.

Round 10 then converted (II) into the single-point claim `G(β1)≥0`
(sufficient by `G`'s monotonicity, `G'=-f'<0` unconditionally: `G` decreasing
means `G(β1)≥0` on the right endpoint suffices for all `β<β1` in the interval)
— but this conversion is *only valid/meaningful when `(β0,β1)` is nonempty*,
i.e. when `β1>β0`. I verified numerically (mpmath, dps=30) at the round-20
counterexample witness `A=0.02, B=1.5`: `Y(β0)≈-0.487<0` already (recall
`sin(A+3β0)=0` exactly by `β0`'s own definition, and `Y` decreasing), so
`Y(β)<0` for **all** `β∈(β0,γ)` at this witness — (II)'s hypothesis
`Y(β)>0` is satisfied by *no* `β` in the relevant range there. This is exactly
the situation round 10 flagged as "outside scope."

### What this does NOT yet resolve (the real remaining question for the builder)

This does not, by itself, prove Case (a) is closed — it only shows the
*specific derivation chain* that produced `G(β1)≥0` never actually obligates
proving it there. Two live possibilities, both unexplored by any round:

- **(a) `β1≤β0(A)` may not be geometrically reachable at all** for a
  configuration satisfying every one of the problem's stated hypotheses (not
  just `A≤π/2, B≤C`) — i.e. the *free rotation parameter* `β` of the `K,L`
  family (as it appears in `complex-affine-L1-DK-and-r-lo-selection.md`,
  ranging over `(0,min(∠B,∠C))`) is itself constrained by `sin(A+3β)<0` (the
  "domain-nonempty" condition tied to existence of a valid configuration at
  all, cf. `claim-I-closed-and-claim-II-caseA-closed.md`'s Setup: "the
  domain where `sin(A+3β)<0`"). If the geometrically-selected `β1` (pinned
  by the certified `r_lo`/`G2a`/branch-selection chain in
  `bilinear-chi-cramer-formula.md`, `w-r-lo-positive-via-zN-zK-evaluation.md`)
  is *itself* only ever produced for `β1` satisfying `sin(A+3β1)<0`, i.e.
  `β1>β0`, then Case (a) never arises for genuine configurations — round
  20's witness `(A,B)=(0.02,1.5)` would correspond to *some* `X0`/`β1` value
  algebraically, but not to an actually-realizable `K,L` configuration.
  **This is exactly what round 20's own "Next" section recommended and no
  round has attempted**: re-derive Steps 1-2 (not the `-tangent` restatement)
  to check reachability.
- **(b) Even if `(A,B)` with `β1≤β0` is reachable**, the true target there
  might not be `G(β1)≥0` at all but something else entirely (a different
  branch of the `G2a`/`r_lo` selection machinery, or simply nothing — since
  (I) alone, already unconditionally proved for all of `(β0,γ)` via Theorem
  16.1 / Sub-result A, may be the *entire* content needed when `Y(β)<0`
  throughout `(β0,γ)`).

### Cheap-kill candidates
- Cheapest possible test: pick the round-20 witness `(A,B)=(0.02,1.5)` and
  try to **explicitly construct valid `K,L`** (satisfying every containment
  and angle hypothesis of the original problem, not just the reduced
  algebraic chain) using the certified `r_lo` closed-form machinery
  (`complex-affine-L1-DK-and-r-lo-selection.md`, `cross-product-sign-selection-G2a.md`,
  the magnitude bound `t_1<t_1^{max}`). If no valid `s_2=r_{lo}` /
  `t_1` pair exists satisfying every hypothesis simultaneously at this
  `(A,B)`, Case (a) as literally stated is vacuous and the whole route is
  essentially done (modulo write-up). This is a concrete, bounded numeric
  experiment (reuse existing certified closed forms, plug in `A=0.02,B=1.5`,
  check every inequality chain: `L_1<0`, `W(r_lo)>0`, magnitude bound,
  `0<t_1<t_1^{max}`, and finally `sin(A+3β)<0` at the resulting `β`).
- If that witness DOES yield a fully valid configuration, then (b) above is
  the fallback: since `Y(β)<0` throughout `(β0,γ)` at every genuine Case-(a)
  point (verified at the one witness; should be checked more broadly), it
  is worth testing whether **`f(β1)` alone (not `G(β1)`) is actually what
  the O·(C−B) identity reduces to when `Y<0` throughout** — i.e. re-derive,
  from the raw `O·(C−B)=(|C|²−|B|²)/4` identity and the rotation
  parametrization, what quantity is literally being bounded, rather than
  trusting the `f`/`G`-based (I)/(II) split (which was itself a round-8/9
  simplification, possibly also only valid contingent on `Y(β)>0` regions).

### Small-case / intuition notes (numeric, not proof)
- At `A=0.02,B=1.5`: `X0≈0.4993`, `β0≈1.0405`, `β1≈0.7861` (`β1<β0`,
  confirms Case (a)), `Y(β0)≈-0.487<0`, `Y(γ)=Y(B)≈-0.989<0` — `Y` is
  negative throughout the entire interval `[β0,γ]`, i.e. (II)'s hypothesis
  set is empty at this witness (conjecture-supporting, not proof: only one
  witness checked in this session; the outliner should re-run this over the
  full sampled Case-(a) domain used by round 20, replacing the `G(β1)≥0`
  membership test with a `∃β∈(β0,γ): Y(β)>0` test, to confirm the emptiness
  pattern holds population-wide, not just at this one point).
- The round-10 "8218/25123 vs 0/572,351" finding (violations of `G(β1)≥0`
  with vs without the `β1>β0` restriction) is essentially a smaller-scale
  historical rediscovery of round 18-20's ~70%/2,000,000-sample finding —
  worth flagging explicitly to the outliner as a case of "this population
  already found this exact fact once, ten rounds ago, and it should update
  the *scope of the theorem*, not be treated as evidence Case (a) is a new,
  separate open inequality."

### Candidate technique(s)
Re-derivation (not restatement) of Steps 1-2's rotation/Cramer chain at a
concrete Case-(a) witness, to test domain-reachability directly — this is a
finite computation (plug numbers into already-certified closed forms), not a
new proof technique, and should be quick for a builder to attempt before any
further SOS/Positivstellensatz/corner-Taylor effort is spent on `T`/`G(β1)`
in Case (a) (all of which implicitly assume `G(β1)≥0` is even the right
target — an assumption this report casts real doubt on).

### Knowledge-base entries to use
Not KB-generic; this is entirely population-internal citation tracing. No new
`knowledge_base.md` entries identified as directly relevant beyond what's
already in use (MVT/Lipschitz, resultant/branch-selection).

### Analogous past problems (cruxes)
Not applicable — this is a population-internal logic/citation-tracing finding,
not a new external technique; did not query the crux corpus this round (out
of scope for this lens per dispatch — the dispatch asked specifically to
re-derive the domain from the original reduction chain, not to search for new
external analogues).

### Dead ends (do not retry)
- Do NOT keep attacking `T≥0`/`G(β1)≥0` globally in Case (a) via SOS/corner-
  Taylor techniques (as done for Case (b)) without FIRST resolving whether
  `G(β1)≥0` is even the correct target there — round 20's own certified
  lemma (`t-nonnegative-on-case-b-residual-domain.md`) already shows `T<0`
  genuinely (not just unproved) at ordinary Case-(a) points, so any further
  positivity-certificate search on the *same* quantity `T`/`G(β1)` restricted
  to Case (a) is doomed to fail exactly as Case (b)'s techniques would predict
  (there is no sign-definite certificate for a quantity that is genuinely
  sometimes negative on the literal algebraic domain `X0>cos²β0(A)`).
- Do NOT re-run more sampling to reconfirm `G(β1)<0` happens in Case (a) —
  this is already independently confirmed to 50 digits by 3 separate rounds
  (18,19,20); further sampling adds nothing. The open question is reachability
  /correctness-of-target, not the sign fact itself.
