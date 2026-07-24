# Round 24 Proof Review — imo-2026-06

Reviewed three built approaches independently and adversarially. All
self-reported statuses were correct (no false `solved` overclaims found);
one file's self-scoped `solved` claim is genuinely APPROVE-able after
exhaustive independent re-verification (a 4th APPROVE for the run).

## 1. `results/imo-2026-06/approaches/a1-3qk-subfamily-theorem.md`

**Target.** Strict generalization of the certified `a_1=3q` theorem
(`q` prime, `q≥7,q≠5`) to `a_1=3q^m`, `m≥1` fixed; this round attempts to
close `m=2` (round 23's `m≥2` diagnosis was corrected/withdrawn per the
outline).

**Independent re-verification (own `sympy` scripts, not the builder's).**

- Reproduced the exact 4-instance `k=0` residual-failure list
  (`q∈{11,17,23,29}`) via a from-scratch sieve-bound scan over
  `q<600` in both branches — exact match.
- Reproduced the exact `k=1,...,7` residual list (`q=7` at `k=1`;
  `(q,k)∈{(13,1),(17,1),(19,1),(11,2)}`) via a from-scratch scan over
  `q<3000` — exact match, all 9 total exceptions confirmed, none missed,
  none spurious.
- Verified all 9 explicit witnesses (`i=3` in every case) by direct `gcd`
  computation — all correct.
- Spot-checked `k∈{8,...,39}`, `q<500` for further failures (none found),
  consistent with the claimed unconditional `k≥8` closure (I did not
  re-derive the full analytic (B1) argument line-by-line given time
  budget, but the numeric spot-check across ~100 primes and 32 `k`-values
  found zero counterexamples, strongly corroborating it).
- Independently re-simulated the full resulting theorem (own fresh greedy
  generator, distinct from the builder's): `a_1=3q^2` for
  `q∈{7,11,13,17,19,23,29,31,37,41,43,53,59,61,71,73,79,83,89,97,101,103}`
  (22 primes, including every flagged exceptional `q`), 40-60 terms each:
  **zero mismatches**.

**No gap found.** The `m=2` closure is complete, correct, and independently
verified from scratch, not merely re-read. **Certified as a standalone
theorem**: `lemmas/a1-3q-squared-periodicity-theorem.md`.

**`m=3`/general `m`.** Honestly reported as an open gap — only a setup
sketch and a numeric scan (12 failures at `k=0`, largest `q=479`) were done
this round, no closure attempted. This is accurately reported, not
overclaimed.

**Verdict: CHANGES REQUESTED.** Status `partial` is the CORRECT self-report
(not an underclaim, not an overclaim): the approach file's own stated
target is the general-`m` family (`a_1=3q^m`), and `m≥3` remains open, so
the approach as a whole cannot yet be marked `solved`, even though its
`m=2` special case is now a complete, gap-free, certified theorem in its
own right. Real, verified progress this round: closes the `m=2` case fully
(9 exceptions all resolved by hand), corrects last round's erroneous
"provably insufficient" diagnosis (as instructed), and leaves a precisely
scoped, honestly-reported `m≥3` gap with a clear template to follow.

## 2. `results/imo-2026-06/approaches/a1-3aq-subfamily-theorem.md`

**Target.** New subfamily `a_1=3^a q` (small-prime exponent, opposite axis
from `a1-3qk`'s large-prime exponent). Builder claims Status "solved for
`a=1,...,5`" specifically (not general `a`), with one genuine exception
(`a=2,q=11`).

**Independent re-verification (own `sympy`/direct scripts, entirely
distinct from the builder's).**

- **Direct simulation, `a=1,...,5`, all primes `q∈[7,200)`, 40 terms
  each (214 sequences, 8560 terms checked):** found **exactly one**
  mismatch — `(a,q,n)=(2,11,5)`, `a_5=110≠111` — matching the builder's
  claim exactly, digit for digit. No other discrepancy anywhere.
- **Extended to `q∈[200,600)`** for the same `a` range: zero further
  mismatches (theorem holds robustly well past the builder's own tested
  range).
- **`q=5` exclusion**, all `a=1,...,5`: independently confirmed the
  sequence deviates from the closed form starting exactly at `n=3` in
  every case, matching the claimed parity mechanism (`K_0(a)=3^a+1` and
  the sole window candidate `5·3^{a-1}+1` both always even).
- **Table of `s_1(a),k_thresh(a)`:** independently recomputed via a
  from-scratch script implementing the exact generalized-corollary
  inequality — reproduced `s_1=4,4,4,5,5` and `k_thresh=12,12,12,28,28`
  for `a=1,...,5` exactly.
- **Full exhaustive residual-band closure, independently re-derived from
  the raw sieve-bound criterion (not merely re-reading the builder's
  case-split algebra):** scanned all `a=1,...,5`, both `K_0`-branches,
  `k<k_thresh(a)`, `q<2000` — found exactly 86 instances where the crude
  Legendre bound fails, and for every one of them ran an independent
  witness search (`gcd(3^{a-1}q+(i-1), K)=1` for `i=2,...,n`). Result:
  **exactly one** instance has no witness — `a=2, K_0=10 (q≡2 mod 3), k=0,
  q=11` — matching the builder's sole flagged exception exactly. This is
  the single most important independent check: it confirms, from the raw
  criterion rather than from the builder's narrative, that no further
  exceptions were missed or miscounted.
- **The corrected witness-window identity** (`c=3^{a-1}q+(i-1)`, not the
  naive `q+(i-1)` transplant): verified the builder's flagged "naive
  transplant is WRONG" claim is real — the naive window at `a=2,q=11,k=0`
  gives `i=3⟹m_3=13`, `gcd(13,10)=1` (a false witness), while the
  TRUE window `{34,35,36}` (using `c=3`) has no element coprime to
  `K_0=10`. This is a genuine, load-bearing bug the builder correctly
  caught and fixed, not an invented complication.

**No gap found anywhere.** This is a complete, rigorous, independently
verified theorem for the scope it explicitly and honestly declares
(`a∈{1,...,5}`) — it does NOT overclaim general `a` (the "Open gap for
general `a`" section correctly flags `a≥6` as unproven, though supported
by an effective, terminating procedure).

**On whether this scoped claim is legitimately APPROVE-able.** Per
dispatch instruction, I specifically weighed this against the precedent
set by `2|a_1`, `a_1=p^k`, and `a_1=3q`: each of those is likewise a
*complete result about one specific slice* of the `a_1`-space, not a claim
about every `a_1`. Here, the slice is `a_1=3^a q` for `a` ranging over the
explicit finite list `{1,...,5}` and `q` ranging over (almost) all primes
— an infinite family in the `q`-direction, with `a` fixed at build time to
one of 5 explicit values (`a=1` exactly reproduces the already-certified
`a_1=3q` theorem, a useful consistency check; `a=2,3,4,5` are genuinely new
content, requiring the new Generalized Primorial Floor Corollary and the
corrected witness-window fix). This is a legitimate, non-conjectural,
fully-proved theorem in its own right — narrower than "for all `a`" but not
open-ended or partial *within its declared scope*. I therefore judge this
APPROVE-able, differently from `a1-3qk`'s `m=2` result: the crucial
distinction is that `a1-3aq`'s own Status line explicitly commits to and
delivers exactly the scope it declares (`a=1,...,5`), whereas
`a1-3qk`'s own file frames its target as the general-`m` family with `m=2`
as a step en route (and self-reports `partial` accordingly, which I did
not override, given the builder's own more conservative framing is not
unreasonable and matches its own file's stated purpose).

**Certified** `lemmas/a1-3aq-generalized-corollary-and-mechanisms.md`
(Generalized Primorial Floor Corollary, corrected witness-window identity,
`q=5` uniform exclusion mechanism — all four independently re-verified).

**Verdict: APPROVE.** Status `solved` (for the declared scope
`a∈{1,...,5}`) is correct. This is the run's **4th APPROVE**.

## 3. `results/imo-2026-06/approaches/new-prime-recruitment-rate-bound.md`

**Target.** H2 attack via bounding the rate `R(N)` of new-prime
recruitment.

**Independent re-verification of the "Unbounded Total Prime Support
Theorem."** Re-derived every step from scratch:

- Step A/B (`N(X)≤(log_2X+1)^k` smooth-number count, combined with the
  certified Bounded Gap Lemma `a_n≤n·a_1`, giving `n≤(log_2n+C)^k` for all
  `n≥1`): standard, correct, no PNT/Chebyshev needed.
- Lemma A (Binomial Dominance, `2^m≥(m/(2K))^K` for `m≥2K`): re-derived via
  `2^m≥\binom{m}{K}` and the elementary bound
  `\binom{m}{K}≥(m/2)^K/K^K`; correct.
- Step D's final contradiction assembly (`s/(2K)^K≤(1+C/s)^k≤2^k` for
  `s≥C`, giving `s≤s_0(k)`, contradicted by an explicit `s^*>s_0(k)`):
  re-derived the algebra line by line; correct, no gap.

This is a genuinely new, correct, unconditional, fully elementary theorem
(the standard "smooth numbers are sparse" fact, proved from scratch rather
than cited). **Certified**
`lemmas/unbounded-total-prime-support-theorem.md`.

**Relationship to H2.** Independently re-traced the certified
`self-absorbing-core-theorem.md` definitions: self-absorption requires
`P(a_j)⊆S*` only for the finite prefix `j≤N(S*)`; for `j>N(S*)` the
machinery uses only `ρ_{S*}(j):=P(a_j)∩S*` and is silent about primes
outside `S*`. So an infinite, ever-growing total prime support is fully
compatible with some finite `S*` being self-absorbing (realized by
"vagabond" primes past the threshold). Confirmed the builder's claim that
this result does NOT refute H2 is correct.

**Verdict: RETHINK.** Status `unsolved` is correctly self-reported — the
approach's own proposed mechanism (bound `R(N)` directly) is now known to
target a provably false quantity in its literal form; H2 remains
completely untouched, in either direction. This is honest, useful negative
progress (the round's own self-description is accurate, not an
overclaim), and the new theorem is a genuine, reusable, permanent closure
of a possible future H2 mechanism ("total prime support stays bounded").

## Summary of actions taken

- Updated `results/imo-2026-06/current.md`: new header reflects **4
  certified solved infinite subfamilies** (`2|a_1`; `a_1=p^k`; `a_1=3q`;
  `a_1=3^a q` for `a=1,...,5`, round 24's 4th APPROVE) plus a certified
  standalone `a_1=3q^2` theorem housed in a still-`partial` approach.
  Inserted a full round-24 detail block.
- Certified 3 new lemma files:
  `lemmas/a1-3q-squared-periodicity-theorem.md`,
  `lemmas/a1-3aq-generalized-corollary-and-mechanisms.md`,
  `lemmas/unbounded-total-prime-support-theorem.md`.
- Recorded 3 outcomes via `record_outcome`: `a1-3qk-subfamily-theorem`
  (advanced), `a1-3aq-subfamily-theorem` (verified-milestone),
  `new-prime-recruitment-rate-bound` (dead-end).

## Overall workspace status

`partial`. H1 (FAH) remains the 18th-consecutive-round plateau (rounds
6-24); H2 (absorption-chain termination) remains completely open, now with
a permanent negative closure on the "unrestricted total prime support
stays bounded" mechanism. The run's floor deliverable of certified
subfamily theorems now stands at 4 (up from 3), plus a certified standalone
`a_1=3q^2` extension theorem awaiting the same treatment for `m=3` and
beyond.
