# Proof review — round 3, imo-2026-03

Build set reviewed: `dyadic-cascade-induction`, `potential-weighting-upper-bound`,
`concavity-minimax-duality`. All claims below were independently re-derived (exact
`fractions.Fraction` / hand algebra, Python scripts in `/tmp/verify*.py`), not trusted from
prose.

---

## 1. `dyadic-cascade-induction`

**Verdict: CHANGES REQUESTED. True Status: `partial`.**

### What's correct, independently re-verified

- **Sub-case B fix (a1>2/3) in §2d.** Re-derived from scratch: the inequality chain
  `e_{m-1}\le1/2^{m-1}` (`⟺ 2^m-1\ge2^{m-1}⟺m\ge1`) and `e_{m-1}/3\le e_m` (`⟺2+e_{m-1}\le3`)
  both check out exactly (verified for `m=1..7` via exact fractions). Correctly closes with
  strict inequality; this really was a genuine gap in the prior skeleton (only `a_2\le a_1/2`
  was checked before, not `a_2\le1-a_1`), and the fix is airtight for what it claims.
- **Sub-case A's crossing-point argument.** Re-derived the crossing point `a_1^*=e_{m-1}/(e_{m-1}+2^{-m})`
  and confirmed algebraically and via exact-fraction substitution for `m=1..9` that it equals
  `2^m/(2^{m+1}-1)` exactly, with `\varphi(a_1^*)=e_m` exactly, and that `a_1^*\le2/3` holds
  for every `m\ge1`. The "min of decreasing+increasing is maximized at the crossing" lemma is
  correctly and rigorously proved in-line (three-line case split). All correct.
- **Branch A of the lower bound.** Re-verified the dominance claim `a_1>\sum_{i\ge2}a_i`
  (`⟺2^m>2^m-1`, trivially true) for the dyadic sequence at `m=1..5`, and the final bound
  `e(\text{final})\ge a_1-a_2=2^{m-1}/(2^{m+1}-1)\ge e_m`. This argument is self-contained
  (uses only the newly-certified Facts 1/2, `e\ge0` and `e\le\max`, both independently
  re-verified here on 2000 random sorted multisets with zero violations) and does **not**
  depend on Case (ii)'s open status anywhere — correct and unconditional for every `m`.
- **Case B1/B2 of the lower bound.** B1's claim that the residual after bisecting `a_1`
  rescales to exactly `D_{m-1}` was checked directly; B2's exact inequality
  `(a_1-a_i)-a_2\ge e_m\iff2^{m-1}-2^{m+1-i}\ge1$, tight only at `m=2,i=3`, was re-derived and
  matches. Both are self-contained (recurse on the *specific* dyadic input, not an arbitrary
  residual), so — unlike the Case (i) upper-bound argument below — these do **not** inherit
  Case (ii)'s open-general-`m` problem. Correct, for every `m`.
- **Rule-1-style Case (i)/(ii) recursion, spot-checked against the D/M framework.** Ran an
  independent exhaustive D/M-operation search (bounded, exact) on several Case-(i)-with-
  Case-(ii)-residual configurations at `m=3,4` (including a systematic 300-trial randomized
  batch at `m=4`); found no violation of form A anywhere tested. This is *evidence* the
  underlying claim is likely true in general, not a proof — see the gap below.

### The load-bearing flaw found

**§2d's claim "Case (i)'s form-A gap is now FULLY, RIGOROUSLY CLOSED for every `m`" is an
overclaim; the file does not disclose this.** The inductive step at level `m` reads: "By the
strong induction hypothesis at level `m-1` applied to the residual, **both forms hold**:
`e(residual)\le e_{m-1}(1-a_1)` [form A, IH], `e(residual)\le a_2/2^{m-1}` [form B, IH]." The
residual `\{a_2,\dots,a_k\}` is an *arbitrary* sorted multiset (Case (i)'s hypothesis
constrains only `a_1$ vs `a_2`, nothing about `a_2` vs `a_3`), so this residual may itself be
a **Case (ii)** configuration at level `m-1`. But Case (ii) at general `m` is explicitly
**open** beyond `m=2` — stated repeatedly elsewhere in the very same file ("Case (ii) at
general `m` needs a genuinely different mechanism... confirmed a dead end at `m=3`"). So the
"strong induction hypothesis... both forms" invoked at level `m-1` is *not actually
established* whenever the residual falls into Case (ii) of level `m-1`.

Tracing the actual chain of validity: level 0,1,2 are fully established (both cases, `n=2`'s
upper bound proof from round 2). Level 3's Case (i) step, using level 2's *fully* established
IH, is therefore **validly proved** — a genuine new result. But level 4's Case (i) step would
need level 3's *full* claim (both cases) as IH, and level 3's Case (ii) is open — so level 4's
Case (i) is **not** actually established by this argument, contrary to the "for every `m`"
claim. I verified this is a real (not merely pedantic) dependency by constructing an explicit
level-4 Case-(i) configuration whose residual is a genuine level-3 Case-(ii) configuration
(e.g. `a=(0.5,0.2,0.15,0.1,0.05)` normalized: `a_1\ge2a_2` holds, and the residual
`(0.2,0.15,0.1,0.05)/0.5=(0.4,0.3,0.2,0.1)` satisfies `a_2<2a_3`, i.e. Case ii) — for this
specific residual, an independent exhaustive D/M search happens to find `e=0` (comfortably
under target), so the *conclusion* is not violated here, but the point is the *proof as
written* does not establish it; it merely got lucky that D/M search corroborates it
numerically on the cases tried (a broader 300-trial randomized check at `m=4` also found no
violation — see `/tmp/verify3.py`). **This is a rigor gap, not (as far as tested) a falsity.**

**Correct scope, going forward:** Case (i) of the upper bound is rigorously closed through
`m=3` (an actual improvement over `n=2`-only), not "for every `m`" as headlined. Extending
further requires either (a) closing Case (ii) at every intervening level first, or (b) a
genuinely different argument for Case (i) that doesn't recurse through an unconstrained
residual. I've annotated this precisely in the approach file and in `current.md`.

### Remaining gaps (unaffected by the above)
- Case (ii) at general `m\ge3`: fully open (tracked in `potential-weighting-upper-bound`).
- Lower bound §5.2 (`\ge2` cuts inside a dominant piece): open, strong numerical support only,
  documented negative result on the "merging monotonicity" candidate fix (independently
  re-verified plausible — this is a real, non-trivial finding worth keeping).

### Certification
- **Facts 1 & 2 ("dominant extraction")**: certified, `lemmas/dominant-extraction.md`. Fully
  general, re-derived and re-verified (2000 random trials, zero violations).

---

## 2. `potential-weighting-upper-bound`

**Verdict: CHANGES REQUESTED. True Status: `partial`** (matches the builder's own claim).

### Verified from scratch
- **Lemma D/M.** Re-derived the single-operation argument for both `D(x)` and `M(x,y)`
  independently (applying Lemma P exactly as described) and confirmed the composability-by-
  induction argument is valid, with no gap. Independently implemented an exhaustive D/M search
  in Python (exact fractions) and reproduced the file's own worked traces exactly.
- **Rule 1 counterexample.** Traced by hand and by code: `A=(239/500,112/500,75/500,74/500)`,
  Rule 1 gives exactly `37/500=0.074`, target `e_3=1/15\approx0.0667`; `37/500=111/1500 >
  100/1500=1/15` **strictly**, confirmed exactly. The claimed better D/M sequence
  `D(239/500)\to D(112/500)\to M(75/500,74/500)` was independently re-run and gives exactly
  `1/500`, confirmed.
- **Rule 2 counterexample.** Re-derived (with the same approximate decimals the file uses,
  which is appropriate since the file itself calls this "exact-to-3-decimal"): confirms `D(a_1)`-
  branch gives `\approx0.1664`, `M`-on-smallest-gap branch gives `\approx0.1667`, Rule 2 picks
  `0.1664 > e_2=1/7\approx0.1429` — genuine failure. Also confirmed the claimed superior move
  (`M` on the *larger*-gap pair `(a_1,a_2)`, giving residual `\approx(0.1675,0.1664)$ whose
  level-1 value is `\approx0.0011`) is indeed dramatically better, corroborating the
  "non-local effect" diagnosis.

### Assessment
Genuine, well-verified progress: a new general lemma (certified below) plus two precisely
falsified candidate policies that meaningfully narrow the search space for the actual open
problem (Case (ii) at general `m`). The central goal (a provably-correct policy) remains
unmet, honestly reported as such — not a hidden gap.

### Certification
- **Lemma D/M**: certified, `lemmas/dm-operation-reformulation.md`.

---

## 3. `concavity-minimax-duality`

**Verdict: RETHINK. True Status: `unsolved`** (downgraded from the builder's self-reported
`partial` — see rationale below and the note added directly to the approach file).

### Verified from scratch
- **Region table and edge-normal checks.** Independently re-derived all 9 regions' affine
  formulas from `dyadic-cascade-induction`'s own case split (not merely trusted): confirmed
  `F_{\text{II-1}}=a_1-a_2`, `F_{\text{II-2}}=1-2a_1`, `F_{\text{II-3}}=2a_1-1`,
  `F_{\text{II-4}}=1-a_1-a_2` all match by direct re-derivation from the `level1`/sign-regime
  definitions. Independently recomputed all 4 boundary conditions (I-A/I-B, II-1/II-2,
  II-2/II-3, II-3/II-4) including tangent/normal vectors and the dot-product inequality:
  **all four numeric results match exactly** (three pass, II-2/II-3 fails with gradients
  `\mp2` in the normal direction — an unambiguous, exact sign flip, re-derived independently,
  not a rounding artifact).
- **Claim A (the dip, `g=0`).** Re-derived: at `a_1=1/2=a_2+a_3`, XY's single-cut split into
  `(a_2,a_3)` gives final sorted `a_2,a_2,a_3,a_3`, `e=0` exactly — confirmed by direct
  computation for `t=3/10`.
- **Claim B (`g(p_1)=g(p_2)=1/25` exactly).** Independently re-ran the full `k=0,1,2`
  exhaustive case analysis: `k=0` gives `e=2/5` (confirmed); `k=1`'s two possible "tie
  patterns" (bisection needs equal untouched pair — fails since `a_1,a_2,a_3` pairwise
  distinct; "sum" pattern checked for all 3 candidate cut pieces — all 3 fail) correctly rules
  out `e=0` at `k=1`; the exhaustive breakpoint enumeration over all 3 possible cut targets
  (re-implemented independently, not copied) gives exact minimum `1/25` for both `p_1,p_2`,
  matching the file precisely. A 200,000-trial random search over `k=2` two-cut configurations
  found no value below `1/25`, corroborating (not merely trusting) the claimed infimum
  argument.
- **Claim C (violation).** `0 \ge 1/25` is false — confirmed, this is a genuine, exact,
  non-numerical counterexample to concavity of the *true* value function `g` (not a proxy).

### Assessment: this genuinely kills the approach's central mechanism
This is not an unproven-but-plausible gap — it is a complete, correct, independently-
reproduced *proof* that global concavity of `g` at n=2 is false. The approach's entire plan
("prove `g` concave ⟹ promote `elementary-exchange-smoothing`'s local certificate to a global
maximum, bypassing casework entirely") cannot be executed as conceived. Per `CLAUDE.md`'s
routing rubric, this is exactly the RETHINK case ("the approach itself is wrong or fatally
broken... must go back to the proof-outliner for a different strategy"), not CHANGES
REQUESTED (which is for "the technique is right and there is real progress ... a gap remains
to close") — there is no gap left to close in *this* framing; the framing itself is refuted.
I downgraded the builder's self-reported `partial` to `unsolved` for this reason (the negative
result, while correct and valuable, is not progress on the theorem's actual claim — no bound,
construction, or reduction was advanced).

### Cross-check requested by dispatch: does this affect the siblings?
- **`elementary-exchange-smoothing`'s certificate: NOT invalidated**, but the file's own
  phrasing ("the failing line sits outside `a_1\ge1/2`") is imprecise — I checked directly:
  `a_1=1/2` actually satisfies `a_1\ge1/2` (it's the boundary, not outside it), and the
  specific counterexample triple `(p_1,M,p_2)` has `p_1$'s `a_1=12/25<1/2`, which *is*
  outside `elementary-exchange-smoothing`'s domain. The real reason the certificate survives
  is that its concavity claim is about a **different function**, `h:=\min(f_1,f_2,f_3)` (three
  globally-fixed affine formulas upper-bounding `g`, not equal to `g`), which is honestly
  concave by the elementary "min of affine is concave" fact — independent of whatever happens
  to the true `g`. I independently re-verified this numerically: 200,000 random points inside
  `h`'s claimed domain, max value found `\approx0.1418<1/7=0.1429`, no violation, consistent
  with the dyadic point being `h`'s unique max there. I corrected the imprecise phrasing but
  confirmed the substantive conclusion.
- **`dyadic-cascade-induction`'s n=2 upper-bound proof: unaffected**, since it never invokes
  concavity of anything (pure exact casework).

### Certification
- **Non-concavity of `g` at n=2** (negative result): certified, `lemmas/non-concavity-of-g-at-n2.md`.
  A genuinely reusable "known dead end" fact preventing future re-attempts of the same
  mechanism, with the caveat (documented in the lemma file) that a domain-restricted version
  (`a_1\ge1/2`) is *not* refuted and remains open for a future, differently-scoped approach.
- The "edge-normal concave-kink condition" itself (a restatement of a standard convex-analysis
  fact) was **not** certified as a separate lemma — it is correct but sufficiently standard
  (equivalent to the textbook condition for a polyhedral subdivision's concavity) that a
  separate lemma file adds little beyond what's already inside the certified non-concavity
  write-up, which states and uses it precisely.

---

## Files written/updated this round
- `results/imo-2026-03/current.md` — rewritten to reflect the corrected true state (n=3 Case
  (i) validly proved; lower-bound Branch A/B proved for every `m`; Case (i)'s "every m"
  overclaim corrected to "through m=3"; concavity approach's negative result folded in;
  D/M framework and its two refutations folded in).
- `results/imo-2026-03/approaches/dyadic-cascade-induction.md` — added a reviewer note at the
  top correcting the "every m" overclaim, Status kept `partial`.
- `results/imo-2026-03/approaches/concavity-minimax-duality.md` — Status downgraded from the
  builder's `partial` to `unsolved`, with a note explaining the RETHINK verdict.
- `results/imo-2026-03/lemmas/dm-operation-reformulation.md` — new certified lemma.
- `results/imo-2026-03/lemmas/dominant-extraction.md` — new certified lemma (Facts 1 & 2).
- `results/imo-2026-03/lemmas/non-concavity-of-g-at-n2.md` — new certified negative-result
  lemma.
- Ranker `record_outcome` calls made for all three slugs (see tool outputs): `advanced` for
  `dyadic-cascade-induction` and `potential-weighting-upper-bound`, `dead-end` for
  `concavity-minimax-duality`.

## Verdicts summary
- `dyadic-cascade-induction`: **CHANGES REQUESTED** (Status: `partial`). Real progress (n=3
  Case i, full lower-bound Branch A/B, 2 new certified lemmas), but the "for every m" framing
  of Case (i)'s closure needs correcting to "through m=3," and Case (ii) general-m + the
  multi-cut lower-bound gap remain the primary blockers.
- `potential-weighting-upper-bound`: **CHANGES REQUESTED** (Status: `partial`). Lemma D/M
  certified; two policies conclusively refuted; central policy-search goal still open.
- `concavity-minimax-duality`: **RETHINK** (Status: `unsolved`). Central mechanism (global
  concavity of `g` at n=2) definitively disproved; approach cannot proceed as conceived. A
  restricted-domain variant is a genuinely different, unexplored possible future approach.
