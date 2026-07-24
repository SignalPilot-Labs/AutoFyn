# Round 19 proof-reviewer report (SECOND PASS) — imo-2026-03

## Scope
Re-review of the fix a proof-builder applied to `pigeonhole-subset-sum-upper-bound`'s Step 2 Case
A, in response to this round's first-pass review (`/tmp/round-19/proof-reviewer.md`), which found
one genuine gap: the WLOG sentence "replace `\varepsilon^*` by `-\varepsilon^*` throughout ...
without changing `M`" is false whenever `M\ne0` (witness `X=(10,9,9)`, where the actual optimal
signing has the global max `10` carrying sign `-1`, so the flip is triggered and gives `-8\ne+8`).
Builder report: `/tmp/round-19/proof-builder-pigeonhole-fix.md`. Updated approach file:
`results/imo-2026-03/approaches/pigeonhole-subset-sum-upper-bound.md`.

**Verdict: APPROVE. True Status: `solved` — for the entire theorem, both directions.**

This is treated as the most consequential check of the run per the dispatch; every item below was
independently re-derived/re-tested from scratch, not by trusting the builder's or the first pass's
own scripts or self-report.

## 1. The one-line identity, re-derived symbolically from scratch

Independently confirmed via `sympy` (treating `s` as a *free symbol*, not substituting `\pm1`, so
the check is genuinely sign-agnostic, not two separate numeric checks):

```
Sigma_rest = M - s*xstar + s*y            (solving M = Sigma_rest + s*(xstar-y) for Sigma_rest)
V_prime    = Sigma_rest + s*(xstar-y)  =>  simplifies to exactly M
```

This matches the file's derivation exactly: `V(\varepsilon')=\Sigma_{\rm rest}+s(x^*-y)=M`,
holding *verbatim* for either `s=+1` or `s=-1` — no case split reintroduced, no case silently
dropped. This closes the exact gap the first pass identified: the old version needed
`V(\varepsilon^*)` to specifically equal `+M` (true only pre-flip), while this version only needs
`V(\varepsilon^*)=M` for *whichever* sign `s` actually is, which is definitionally true by
construction (`\varepsilon^*` was fixed to have `V(\varepsilon^*)=M\ge0` at the very start of the
inductive step, once, via the *magnitude*-preserving negation `-\varepsilon^*` — a legitimate,
different kind of move from the flawed one, discussed in §5 below).

## 2. Fresh, independent computational verification

Wrote a new harness from scratch, `/tmp/round-19-review2/fresh_verify2.py` — not reusing the
original builder's `/tmp/round-19-build/`, the fix-builder's `/tmp/round-19-build-2/`, or the
first-pass review's `/tmp/round-19-review/` code. Implements the algorithm literally as newly
written (global max `x^*`, actual current sign `s`, arbitrary opposite-sign partner `y`, same-sign
sub-lemma peeling a zero), checked against an independently coded brute-force `\mathrm{OPT}`
oracle, with a per-step optimality-invariant check (recomputes true brute-force `OPT` of the
*current* active multiset at every intermediate step, not just the final answer — this directly
tests the proof's central "optimality is preserved by the merge" claim).

Results, `2{,}095+` trials total, **0 failures, 0 invariant violations, 0 "stuck" states**:
- **The exact witness `X=(10,9,9)`** (true `OPT=8`, optimal signing `(-1,+1,+1)` — the global max
  `10` carries sign `s=-1`, exactly the branch that broke the earlier draft) and **all 6
  permutations**, each with **5 random tie-break seeds**: `30` checks, all PASS.
- Wide random integer sweep, sizes `1`-`13`: `500` trials.
- Tie-heavy small-alphabet (`0`-`5`), sizes `2`-`13`: `400` trials.
- Zero-heavy (`~50%` zeros), sizes `2`-`12`: `300` trials.
- Fractional-valued instances, sizes `2`-`11`: `300` trials.
- All-same-value instances (forces the same-sign sub-lemma branch heavily): `150` trials.
- Larger sizes `14`-`15` (beyond the fix-builder's own tested range up to `14`): `15` trials
  (final-value check; invariant check disabled here only for runtime, final value still
  cross-checked against independent brute force).
- `5` explicit edge cases (`p=1`, all-zero, tied pair, zero pair).
- `3` independent repetitions with different random tie-break seeds per instance (`600` more
  trials), confirming correctness does not depend on a specific tie-break policy — matches the
  proof's "any `y`" / "any global max representative" claims.

Separately re-verified **Lemma 1 (Pigeonhole Margin Lemma)** fresh (`/tmp/round-19-review2/
verify_lemma1.py`): `640` trials, sizes `1`-`8`, `0` failures — this step was unchanged by the fix
but is part of the full chain being re-traced this pass.

## 3. The "unmerge" contradiction argument — unaffected, composes correctly

Re-read and re-derived symbolically: the argument is phrased purely in terms of an arbitrary
`\tau:=\varepsilon''(x^*-y)\in\{\pm1\}` — the sign a *hypothetical* better signing of `X'` assigns
the merged token — and never references `s` or the specific claimed value of `V(\varepsilon^*)`.
`V(\varepsilon''')=\tau x^*+(-\tau)y=\tau(x^*-y)=V(\varepsilon'')`, so a strictly-better signing of
`X'` would "unmerge" into a strictly-better signing of the original `X`, contradicting
`M=\mathrm{OPT}(X)`. This paragraph is textually **unchanged** by the fix (confirmed by diff) and
was already fully sign-agnostic before this round's fix — it never depended on the flawed WLOG
sentence, exactly as both the first-pass review and the builder claimed. It composes correctly
with the newly-fixed Case A: the two pieces (the identity establishing `V(\varepsilon')=M`, and
the unmerge argument establishing `\mathrm{OPT}(X')=M`) are logically independent and both
correct, together giving `\varepsilon'` is a value-`M`, globally-optimal signing of `X'`, ready for
the induction hypothesis.

## 4. No stale references to the old `i^*\in P`/`j\in N` framing

Grepped the entire approach file for `i^*\in P`, `i^*\in N`, `j\in N`, hardcoded `:=+1`, and the
old WLOG sentence. All remaining occurrences are inside clearly-labeled historical sections (the
first-pass reviewer's own verdict note, and this round's "second-build addendum," both preserved
per the project's append-don't-rewrite convention, both explicitly recounting the *old, now-fixed*
text as history). The live **Full proof** section (§2 Case A) and its Remark are fully migrated to
the sign-agnostic `s`/`\varepsilon^*(y)=-s` framing; no live inconsistency found anywhere the
framing is actually used (Case A itself, the Remark explaining why this avoids the falsified
same-sign-tied mechanism, and §3's citation of the Signed-Sum Realizability Lemma, which only uses
the Theorem's *statement*, not Case A's internal machinery).

## 5. The sub-lemma's own "WLOG, negate for the N=all case" — checked it is NOT the same bug

The sub-lemma states: "WLOG `P`=all (the `N`=all case is identical after negating)." This looks
superficially similar to the earlier flawed move, so it was specifically re-examined for the same
kind of error. It is **not** the same bug: here, `M` in context is `\mathrm{OPT}(X)`, a
sign-independent *magnitude* (the sub-lemma's proof explicitly concludes "contradicting
`M=\mathrm{OPT}(X)`"), and negating `\varepsilon^*` trivially preserves `|V(\cdot)|` — a
genuinely true, unconditional fact. The earlier bug was different in kind: it conflated "flipping
preserves the *magnitude*" (true) with "flipping preserves *this specific signed value*
`V(\varepsilon^*)`, needed exactly as `+M` (not `-M`) by a downstream algebraic identity" (false).
No analogous gap exists in the sub-lemma's WLOG step.

Additionally worth noting: under the top-level induction's fixed convention (`V(\varepsilon^*)=M
\ge0`, established once at the very top of the inductive step, before Case A/B are entered), if
`N`=all actually occurred it would force `M=0` (since `V(\varepsilon^*)=-\sum x_i\le0` must equal
`M\ge0`), an even more degenerate sub-case than the sub-lemma's general "negate and reduce to
`P`=all" argument needs to handle — consistent, no contradiction, no gap.

## 6. Full end-to-end retrace

- **Step 1 (Pigeonhole Margin Lemma):** re-verified fresh this pass (§2 above), no change from
  last pass, no gap.
- **Step 2 (Signed-Sum Realizability Lemma):** base case, sub-lemma, Case A (fixed, re-verified
  above), Case B (unchanged, textually identical to the pre-fix version, re-confirmed correct) —
  cases exhaustive, no gap.
- **Step 3 (Combination):** unchanged; re-traced the operation count `(k-|T|)+(|T|-1)=k-1=m`
  matches XY's budget exactly, and the `|T|=1` degenerate sub-case is correctly absorbed by the
  Theorem's own base case — no gap.
- **Step 4 (Conclusion + final answer):** unchanged; the algebra `c(n)=(1+e_n)/2=2^n/(2^{n+1}-1)`
  re-verified by hand; re-confirmed the imports (Lemma D/M, Slack Collapse, the lower bound) are
  all present and certified in `results/imo-2026-03/lemmas/` (`dm-operation-reformulation.md`,
  `slack-collapse.md`, `all-cycles-resolution.md`, `superincreasing-no-early-zero.md`,
  `greedy-reduction.md`), matching the same `e_m\cdot S` target as this proof's construction.
- **No new loose thread found anywhere else in the file.**

## 7. Two independent, proof-machinery-free numerical validations of the final answer

Beyond re-checking the proof's internal algebra, ran two from-scratch brute-force validations of
the *actual continuous game* against the claimed answer, using no part of the proof's own
apparatus (only a from-scratch spot-check that greedy-claiming matches true backward-induction
alternating-pick game values, on 20 random small cases, to validate the game solver itself):

- **`n=1`** (`/tmp/round-19-review2/verify_n1_n2.py`): grid search over Liu Bang's single cut
  point `p`, with Xiang Yu's best single-cut response computed by brute-force backward induction
  over all candidate cut positions on either resulting piece. Best guaranteed value found:
  `\approx0.6660` at `p\approx0.668` (coarse grid), refining to `\approx0.66662` at `p\approx
  0.66677` (finer grid near `2/3`) — matches the claimed `c(1)=2/3=0.66667` to grid resolution.
- **`n=2`** (`/tmp/round-19-review2/verify_n2.py`): at the specific dyadic-shaped opening
  `(4/7,2/7,1/7)`, a grid search over Xiang Yu's best response using up to 2 further cuts (on any
  of the current pieces, any split point, searched over a 25-point-per-cut grid, which includes
  the exact bisection points) gives exactly `4/7=0.57143` — **exact match** to the claimed
  `c(2)=4/7`. Nearby candidate openings (`(0.6,0.25,0.15)`, `(0.55,0.3,0.15)`) give strictly worse
  guaranteed values (`0.55`), consistent with `(4/7,2/7,1/7)` being (at least locally) optimal for
  Liu Bang.

This is strong independent corroboration that the final answer is not just internally consistent
with the proof's own machinery, but is the actually-correct answer to the real combinatorial game.

## Conclusion

After a genuinely adversarial re-attempt — re-deriving the load-bearing identity symbolically from
first principles, writing an entirely fresh verification harness (not reusing any prior round's
code), specifically re-testing the exact witness that broke the earlier draft, checking the
"unmerge" argument still composes correctly, checking for stale references to the old framing,
distinguishing the sub-lemma's superficially-similar WLOG step from the actual earlier bug, and
independently validating the final numeric answer against the real game by an entirely different
computational method for two values of `n` — **no remaining gap was found.**

The proof is complete and rigorous: every case is exhaustively covered (Case A vs. Case B, with
Case A itself requiring no internal case split on `s`), every theorem invoked is named and cited
correctly (Lemma G, Lemma D/M, Slack Collapse, the certified lower bound), and the final answer
`c(n)=2^n/(2^{n+1}-1)` is stated explicitly and verified by direct substitution at `n=1,2`, the
general recursion, and (this pass) two independent from-scratch game-solver checks — satisfying
the `compute_and_prove`/`answer_type: expression` requirement in full.

## Actions taken
- **`results/imo-2026-03/current.md`**: `## Status` raised `partial`→`solved`; a new top-of-list
  entry added to `## Approaches tried` documenting this second-pass re-verification in full; the
  `## Full proof` section (previously "not present") replaced with the complete, self-contained
  proof (Setup, Pigeonhole Margin Lemma, Signed-Sum Realizability Lemma, Combination, Conclusion,
  final-answer verification).
- **`results/imo-2026-03/approaches/pigeonhole-subset-sum-upper-bound.md`**: appended a "Round 19
  (second-pass) proof-reviewer verdict — APPROVE" section documenting this review's findings.
- **Certified** `results/imo-2026-03/lemmas/signed-sum-realizability.md` (new) — the Signed-Sum
  Realizability Lemma, general and reusable, `sorry`-free, statement matching exactly what was
  proved (no stronger claim).
- **Ranker outcome recorded:** `pigeonhole-subset-sum-upper-bound` → `verified-milestone`.

## Files touched
- `/home/agentuser/repo/results/imo-2026-03/current.md`
- `/home/agentuser/repo/results/imo-2026-03/approaches/pigeonhole-subset-sum-upper-bound.md`
- `/home/agentuser/repo/results/imo-2026-03/lemmas/signed-sum-realizability.md` (new)
- Review scripts: `/tmp/round-19-review2/fresh_verify2.py`, `/tmp/round-19-review2/verify_lemma1.py`,
  `/tmp/round-19-review2/verify_n1_n2.py`, `/tmp/round-19-review2/verify_n2.py`

## Headline result
**`imo-2026-03` (IMO 2026 P3) is SOLVED.** `c(n)=2^n/(2^{n+1}-1)` for every positive integer `n`,
proved in full (upper bound: this approach; lower bound: already-certified `all-cycles-resolution.md`
+ `superincreasing-no-early-zero.md`). This is the headline result of the run.
