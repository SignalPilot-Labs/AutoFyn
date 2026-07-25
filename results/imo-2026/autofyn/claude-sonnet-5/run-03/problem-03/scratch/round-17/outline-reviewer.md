Review of `/tmp/round-17/proof-outliner.md` for `imo-2026-03`.

## self-similar-induction-on-n — CHANGES REQUESTED

Steps 1-4 of the outline are sound and I independently re-verified them:

- Step 1 (scope correction): confirmed. Round 16's refuting counterexample has
  `|D|=5 > m+1=3`, outside GT(m)'s own hypothesis `|D|<=m+1`. Correctly
  flagged as a scope-correction, not a re-opening of a settled falsehood.
- Step 2 (coupled single-step alternation): I coded `OddSum`/`EvenSum` over
  `D ∪ Γ_{j-1}` (Γ_t := {2^0,...,2^t}, matching the file's own worked
  example `OddSum(Γ_6)=85`) and ran 20,000 exact-`Fraction` trials of
  `O_j = 2^{j-1} + E_{j-1}` and `E_j = O_{j-1}` whenever `max(D) <= 2^{j-1}`
  (q=0 at level j). Zero mismatches. This is also exactly consistent with
  round 16's own independently re-derived two-step relation
  `O_j = 2^{j-1} + O_{j-2}` (substituting `E_{j-1}=O_{j-2}` recovers it) —
  a good sign this round's mechanism is the correct fix, not a repeat of
  round 16's collapsed-to-one-quantity error.
- Steps 3-4 (chaining to level k, Even-target twin): plausible mechanical
  consequences of step 2; not independently re-derived in full but nothing
  in them contradicts step 2's verified identity.

**Step 5 is the problem.** The outline asserts the e-fold chain "telescopes
to exactly `2^m - 2^k`" (i.e., that the sum of `2^{j-1}` terms for
`j=k+1,...,m` all appear). I chained the *verified* step-2 identity by hand
and in code (`/tmp/test_chain.py`) for `D=∅` (isolating the pure telescoping
coefficient) across `k=1..4, e=1..6`:

```
k=1 e=1 m=2 coeff=2   2^m-2^k=2   match
k=1 e=2 m=3 coeff=4   2^m-2^k=6   MISMATCH
k=1 e=3 m=4 coeff=10  2^m-2^k=14  MISMATCH
k=2 e=2 m=4 coeff=8   2^m-2^k=12  MISMATCH
k=3 e=2 m=5 coeff=16  2^m-2^k=24  MISMATCH
k=4 e=5 m=9 coeff=336 2^m-2^k=496 MISMATCH
```

The claimed identity holds **only at `e=1`** and is false for every
`e>=2` tested (20+ cases, exact arithmetic, zero exceptions to the
mismatch). The actual coefficient is a ratio-4 geometric series
(`2^{m-1}+2^{m-3}+...`, only `ceil(e/2)` terms, not `e` terms), because the
coupled alternation only adds a fresh `2^{j-1}` term every *other* step —
the intervening step converts `O<->E` without adding a new power of 2. This
is the same failure mode as round 16's headline error (an "Odd stays Odd
every step" over-count), just one level more subtle: here it's "every step
contributes its own power of 2," when only alternating steps do. The
explorer's "numerically confirmed" claim for step 5 was evidently checked
only at `e=1` (or not checked at all in exact arithmetic) — this is exactly
the pattern flagged in `/tmp/memory/outline-reviewer.md`'s standing rule
("stress-test any explicit numeric claim, don't just read for plausibility").

This is **not fatal** to the approach: steps 1-4 are real, and the
"deficit" relative to `2^m-2^k` may well still be covered by the Half-Sum /
Large-Sum Closure Theorem's base term at level k (which has independently
certified positive slack) — the builder has not actually shown this fails,
only that the outline's stated intermediate identity is wrong. But the
builder must **not** write the false `2^m-2^k` closed form into the proof;
it must (a) derive the correct ratio-4 closed form explicitly (I've given
the exact coefficients above as a starting point), and (b) re-check whether
`(corrected coefficient) + (O_k or E_k lower bound from the certified
Large-Sum Closure / Even-target twin)` still meets `2^m`. If it does not
meet `2^m` for some `(k,e)`, that is a genuine new obstruction, not a
"numerically confirmed" closure — report honestly either way.

Verdict: **CHANGES REQUESTED**, not RETHINK — the technique (coupled
alternation) is now correctly identified and verified; only the final
algebraic step needs re-derivation with the corrected closed form before
any closure claim is written.

## global-lp-vertex-sufficiency — APPROVE

Diagnostic-first plan is well-gated: step 1 (mandatory cheap-kill of the
aimo-0119-style exchange mechanism on the 8 catalogued hard points) must run
before any proof investment, matching project rule. Step 2's
sharp-kink-vs-flat-interval classification is a genuinely new diagnostic
(not a repeat of the 4 already-refuted tie-topologies — I checked the file's
own "refuted" log at lines ~1624-1672, 2163-2403, 2520-2784: Self-Bisection-
Crossover and Flat-Edge are structurally distinct joint mechanisms, correctly
distinguished from those). Steps 3/4 correctly treat the two classes as
separate formal objects (vertex vs. degenerate-basis/face) rather than
conflating them, and step 4 explicitly requires exact `Fraction` arithmetic
before trusting the Flat-Edge endpoint claim — appropriately paranoid given
round 16's own documented float-optimizer artifact. No circularity, no
skipped cases (explicit "classify all 8 before writing narrative" gate).

## lp-duality-split-polytope — APPROVE

Correctly scoped as secondary/non-critical-path (per its own "Watch out"
note), asking only for an exact-arithmetic re-run of a float-sourced numeric
lead plus an optional necessity-direction counting argument mirroring the
already-certified Mass-Constraint Theorem technique. No new unverified
mechanism is asserted as fact; this is exactly the right size of ask for
spare capacity. No overlap/circularity with the other two approaches (this
is upper-bound necessity at a single vertex `e_0`, distinct target from
both siblings).

## Diversity check

The three approaches remain a genuinely diverse field: self-similar attacks
the **lower bound** via an induction/peeling recursion; global-lp and
lp-duality both attack the **upper bound** but via different objects
(global vertex-enumeration/classification vs. a single-vertex necessity
question) — not the same wall. No consolidation needed this round.

## Ranking

Registered slugs unchanged (all three already in the population; no new
slug this round). Ran `update_ranking` with:
- global-lp-vertex-sufficiency beats self-similar-induction-on-n (honest
  diagnostic progress this round vs. a caught false central claim)
- lp-duality-split-polytope beats self-similar-induction-on-n (same reason)
- global-lp-vertex-sufficiency beats lp-duality-split-polytope (primary
  upper-bound path vs. explicitly secondary/spare-capacity task)
- greedy-reduction-geometric (established, highest-Elo live approach, real
  window-closure progress) beats self-similar-induction-on-n (anchors the
  newcomer-adjacent result to the established field, per the standard
  rule — self-similar has now twice produced a headline claim that didn't
  survive independent re-derivation)

This clears the `stale` flag on all four touched approaches.

build set: self-similar-induction-on-n, global-lp-vertex-sufficiency, lp-duality-split-polytope
