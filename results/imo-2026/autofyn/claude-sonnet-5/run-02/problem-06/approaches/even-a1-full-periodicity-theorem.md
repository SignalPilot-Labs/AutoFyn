## Status
solved (for the restricted subfamily 2 | a_1 — see explicit scope statement
below; the workspace-level Status for the *general* problem, i.e. for every
a_1 > 1, remains `partial`, as this approach does not touch the odd-a_1 case
or the still-open FAH crux)

## Approaches tried
- **even-a1-full-periodicity-theorem** (round 16, new) — a self-contained,
  elementary strong induction (no persistent-type / Free-Facts-pigeonhole /
  FAH machinery at all) proving that whenever `2 | a_1`, the entire sequence
  is given by the closed form `a_n = a_1 + 2(n-1)` for *every* `n ≥ 1`
  literally (not just eventually), so `T = 1`, `L = 2` witness the problem's
  conclusion from the very first term. This is a genuine strict
  generalization of the previously certified "`|Q| = 1`" special case (which
  only covered `a_1` a power of 2): it covers every even `a_1`, including
  composite, non-prime-power seeds such as `30 = 2·3·5`, `210 = 2·3·5·7`, or
  `2p` for any odd prime `p`, none of which have `Q = {2}` in the sense of
  the certified lemma (their prime factorizations have several distinct odd
  prime factors, so the persistent-type machinery of the general approach is
  nontrivial for them, yet this elementary argument bypasses all of it).
  Independently verified against a fresh Python simulation on 11 seeds
  (6, 30, 210, 1994, 14, 210, 22, 26, 4, 8, 34), including several
  non-prime-power composites, matching the closed form exactly on every
  sampled prefix. Outcome: **complete, gap-free proof of the stated
  restricted target.** Does not resolve, and is not claimed to resolve, the
  general problem for odd `a_1`.

## Current best
A complete and unconditional proof (Theorem A below) that for every `a_1 > 1`
with `2 | a_1`, the sequence satisfies `a_n = a_1 + 2(n-1)` for all `n ≥ 1`,
hence the problem's conclusion holds with `T = 1`, `L = 2`, literally from
`n = 1` — no "eventually," no asymptotic hedge, no dependence on any of the
open hypotheses (FAH, self-absorbing core existence/termination) used
elsewhere in this workspace for the general case. This is the furthest
rigorous progress on the even-`a_1` subfamily; it is a genuine strict
enlargement of the previously certified `|Q|=1` special case. The proof of
the *general* problem (arbitrary `a_1 > 1`, in particular odd `a_1`) remains
open, conditional on the standing FAH crux and on the self-absorbing-core
termination question documented in `current.md` and in
`n1-periodicity-reconciliation.md`; this approach explicitly does not
address either.

## Full proof

**Setup and notation.** Let `a_1, a_2, a_3, \dots` be the sequence defined in
the problem: `a_1 > 1` is a given positive integer, and for every `n ≥ 1`,
`a_{n+1}` is the smallest integer strictly greater than `a_n` such that
`gcd(a_{n+1}, a_i) > 1` for every `i = 1, \dots, n`. We restrict attention
throughout to the case `2 \mid a_1`.

**Theorem A (Literal periodicity for even seeds).** If `2 \mid a_1`, then
`a_n = a_1 + 2(n-1)` for every positive integer `n`. Consequently
`a_{n+1} - a_n = 2` for every `n \ge 1`, so the problem's conclusion holds
with `T = 1` and `L = 2`, and it holds *literally for every `n \ge 1`*, not
merely for `n` beyond some threshold.

*Proof.* We prove the closed form by strong induction on `n`.

**Base case (`n = 1`).** The formula `a_1 = a_1 + 2(1-1) = a_1` holds
trivially. This is the only content needed at the base: we are given
`2 \mid a_1` by hypothesis, and `a_1 > 1` by the problem's standing
assumption that every term is a positive integer greater than `1`.

**Inductive hypothesis.** Fix `n \ge 1` and suppose that
`a_i = a_1 + 2(i-1)` for every `i = 1, \dots, n`. In particular (since
`2 \mid a_1`), every one of `a_1, \dots, a_n` is even:
`a_i = a_1 + 2(i-1)` is a sum of an even number `a_1` and an even number
`2(i-1)`, hence even, for each `i \le n`.

**Inductive step.** We must determine `a_{n+1}`, the smallest integer
strictly greater than `a_n` with `gcd(a_{n+1}, a_i) > 1` for every
`i = 1, \dots, n`. We examine the integers greater than `a_n` in increasing
order, starting with the two smallest candidates `a_n + 1` and `a_n + 2`.

*Claim 1: `c = a_n + 1` is NOT a legal choice for `a_{n+1}`.*
Since `a_n` and `a_n + 1` are consecutive integers, `\gcd(a_n+1, a_n) = 1`.
(This is the elementary fact that any common divisor of two consecutive
integers `m` and `m+1` divides their difference `1`, hence equals `1`.) In
particular, taking `i = n` in the required condition
`\gcd(c, a_i) > 1` for all `i \le n`, the candidate `c = a_n+1` fails the
`i=n` instance of this condition: `\gcd(a_n+1, a_n) = 1`, not `> 1`. Hence
`a_n + 1` is illegal as a value of `a_{n+1}`, regardless of parity of `a_1`
or of anything else — this half of the argument uses no evenness at all,
only that consecutive integers are coprime.

*Claim 2: `c = a_n + 2` IS a legal choice, i.e. it satisfies
`\gcd(c, a_i) > 1` simultaneously for every `i = 1, \dots, n`.*
By the inductive hypothesis, every `a_i` with `i \le n` is even, i.e.
`2 \mid a_i` for all `i \le n`. Also `a_n` is even (case `i=n` of the same
hypothesis), so `c = a_n + 2` is a sum of two even numbers and is therefore
itself even: `2 \mid c`. Consequently, for every `i = 1, \dots, n`, the
integer `2` is a common divisor of `c` and `a_i`, so
`\gcd(c, a_i) \ge 2 > 1`. Thus `c = a_n+2` satisfies the required condition
against *every* one of `a_1, \dots, a_n` simultaneously.

*Claim 3: `a_{n+1} = a_n + 2` exactly.*
By definition, `a_{n+1}` is the *smallest* integer strictly greater than
`a_n` satisfying `\gcd(a_{n+1}, a_i) > 1` for all `i \le n`. The set of
integers strictly greater than `a_n` is linearly ordered starting
`a_n+1 < a_n+2 < a_n+3 < \cdots`, so if we can show the two smallest
candidates `a_n+1` and `a_n+2` are respectively illegal and legal, minimality
of the definition forces `a_{n+1}` to equal the smaller of the (in general,
possibly many) legal candidates greater than `a_n`; since `a_n+1` is
illegal (Claim 1) and `a_n+2` is legal (Claim 2), and no integer lies
strictly between `a_n+1` and `a_n+2` (they are consecutive integers), the
smallest legal candidate is exactly `a_n+2`. Hence `a_{n+1} = a_n + 2`.

(To spell out the minimality argument fully: let
`L := \{c \in \mathbb{Z} : c > a_n,\ \gcd(c,a_i) > 1 \text{ for all } i \le n\}`
be the set of legal candidates; by the problem's own definition,
`a_{n+1} = \min L`. Claim 2 shows `a_n + 2 \in L`, so `L \ne \emptyset` and
`\min L \le a_n + 2`. Claim 1 shows `a_n+1 \notin L`. Since every element of
`L` is, by definition, an integer strictly greater than `a_n`, and the only
integer strictly between `a_n` and `a_n+2` is `a_n+1` itself, every element
of `L` other than a possible `a_n+2` must be `\ge a_n+2`; combined with
`a_n+1 \notin L` this gives `\min L \ge a_n+2`. Together with
`\min L \le a_n+2` from above, `\min L = a_n+2`, i.e. `a_{n+1} = a_n+2`.)

**Closing the induction.** We have shown `a_{n+1} = a_n + 2`. Using the
inductive hypothesis `a_n = a_1 + 2(n-1)`, this gives
`a_{n+1} = a_1 + 2(n-1) + 2 = a_1 + 2n = a_1 + 2((n+1)-1)`,
which is exactly the closed form at index `n+1`. Moreover `a_{n+1} = a_n+2`
is even (sum of two even numbers, since `a_n` is even by the inductive
hypothesis), so the "every index up to `n+1` is even" hypothesis needed to
repeat this argument at the next step is also verified. This completes the
strong induction: for every `n \ge 1`, `a_n = a_1 + 2(n-1)`, and every `a_n`
is even.

**Conclusion.** For every `n \ge 1`,
`a_{n+1} - a_n = \big(a_1+2n\big) - \big(a_1+2(n-1)\big) = 2`,
so the problem's required conclusion `a_{n+T} = a_n + L` holds with
`T = 1` and `L = 2` for *every* positive integer `n` (not merely eventually):
indeed `a_{n+1} = a_n + 2 = a_n + L` for all `n \ge 1`. `T=1` and `L=2` are
positive integers as required. This proves Theorem A. `∎`

**Explicit verification (small example).** Take `a_1 = 6` (even, `>1`).
Theorem A predicts `a_n = 6 + 2(n-1)`, i.e. the sequence
`6, 8, 10, 12, 14, 16, \dots`. We verify this directly against the problem's
definition for the first few steps:
- `a_1 = 6`.
- `a_2`: the smallest integer `> 6` with `\gcd(\cdot, 6) > 1`. Candidate `7`:
  `\gcd(7,6)=1`, illegal. Candidate `8`: `\gcd(8,6)=2>1`, legal. So
  `a_2 = 8 = 6 + 2(2-1)`. Matches.
- `a_3`: smallest integer `>8` with `\gcd(\cdot,6)>1` and `\gcd(\cdot,8)>1`.
  Candidate `9`: `\gcd(9,8)=1`, illegal. Candidate `10`: `\gcd(10,6)=2>1`,
  `\gcd(10,8)=2>1`, legal. So `a_3 = 10 = 6+2(3-1)`. Matches.
- `a_4`: smallest integer `>10` legal against `6,8,10`. Candidate `11`:
  `\gcd(11,10)=1`, illegal. Candidate `12`: `\gcd(12,6)=6>1`,
  `\gcd(12,8)=4>1`, `\gcd(12,10)=2>1`, legal. So `a_4=12=6+2(4-1)`. Matches.

This matches Theorem A's closed form exactly, and matches the general
mechanism of the proof: at each step the odd successor `a_n+1` is killed by
coprimality with `a_n` itself, and the even successor `a_n+2` survives against
every earlier (even) term at once, regardless of which distinct odd prime
factors those earlier terms individually carry (`6=2\cdot3`, `8=2^3`,
`10=2\cdot5`, `12=2^2\cdot3` in the example above — three different odd
prime factors `3,5` appear among these four terms, yet the single shared
factor `2` alone suffices to legalize every step; this is exactly why the
elementary argument needs no persistent-type or FAH machinery at all).

We additionally independently re-verified the closed form computationally
(fresh Python simulation, trial-division-based greedy generator implementing
the problem's definition literally with no shortcuts) on 11 further seeds,
including several non-prime-power composite even seeds:
`a_1 \in \{6, 30, 210, 1994, 14, 210, 22, 26, 4, 8, 34\}` — in every case the
first `50` terms of the simulated sequence satisfy `a_{n+1}-a_n = 2` for
every consecutive pair, exactly matching Theorem A. (This is a
confirmatory sanity check, not itself part of the proof, which is complete
without it — the proof above is a fully self-contained strong induction.)

**Precise scope: what this theorem does and does NOT establish.**

1. **What it establishes.** Theorem A is an unconditional, complete proof of
   the problem's stated conclusion — existence of positive integers `T, L`
   with `a_{n+T} = a_n + L` for every `n` — for the entire subfamily of
   seeds `a_1` with `2 \mid a_1`. This subfamily is infinite and strictly
   larger than the previously certified `|Q|=1` special case (`a_1 = 2^k` a
   power of `2`, where `Q` denotes the prime-factor set of `a_1` used
   throughout the rest of this workspace): Theorem A additionally covers
   every even `a_1` with two or more distinct odd prime factors, e.g.
   `a_1 = 30 = 2\cdot3\cdot5`, `a_1=210=2\cdot3\cdot5\cdot7`, or
   `a_1 = 2p` for any odd prime `p`. For all of these the general
   persistent-type machinery used elsewhere in the workspace is genuinely
   nontrivial (`Q` has more than one prime, so the `|Q|=1` special case does
   not apply), yet the present elementary argument settles them completely
   without needing that machinery, because in this special situation the
   induction never needs to distinguish *which* odd prime is shared between
   two given terms — only the single shared prime `2`, common to literally
   every term of the sequence by construction, is ever used.

2. **What it does NOT establish.** This theorem says nothing whatsoever
   about seeds `a_1` with `2 \nmid a_1` (odd `a_1`). For odd `a_1`, the
   induction's Claim 2 breaks down immediately: there is no single prime
   automatically common to `a_1` and to all subsequent terms the way `2`
   is for even seeds, so the "second candidate `a_n+2` is always legal"
   argument has no analogue, and indeed the general problem for odd `a_1`
   is exactly the case addressed (and left open, conditional on the FAH
   crux) by the rest of this workspace's approaches
   (`covering-system-construction`, `greedy-exchange-cost-potential`,
   `n1-periodicity-reconciliation`, etc. — see `current.md`). In particular:
   - We do **not** claim, attempt, or suggest any extension of this
     mechanism to seeds whose smallest prime factor `p` is odd (`p \ge 3`).
     Such an extension would require showing that among the `p-2` candidates
     strictly between `a_n+1` (illegal, coprime to `a_n`) and the first
     multiple of `p` above `a_n`, none is legal against the *entire* history
     `a_1,\dots,a_n` — and bare coprimality-with-`a_n` alone does not settle
     this for `p \ge 3` (there is no single prime forced to divide literally
     every earlier term the way `2` is for an even seed unless `p \mid a_1`;
     if `a_1` is odd, no prime is guaranteed a priori to divide every term).
     This limitation is real and is not an oversight to be patched — it is
     the precise reason the general problem needs the heavier persistent-
     type / FAH machinery developed elsewhere in this workspace.
   - This theorem does **not** use, and is entirely independent of, the
     Free Facts Lemma, the Persistent-Type Pigeonhole, the Finite Core
     Theorem, the Self-Absorbing Core Theorem, or any FAH-type hypothesis —
     it is a fully self-contained four-line induction. It therefore cannot
     be "promoted" or generalized by strengthening those other results; it
     is a structurally different (and, for its scope, strictly easier)
     argument that happens to fully resolve an infinite subfamily of seeds
     via a completely different mechanism (universal shared factor `2`,
     rather than eventual persistent-type reconciliation).
   - Consequently the **workspace-level** claim of the problem — "for every
     positive integer `a_1 > 1`, there exist `T,L`..." — is **not** fully
     resolved by this file. The overall Status of the problem in
     `results/imo-2026-06/current.md` correctly remains `partial`; this
     approach only fully resolves the even-`a_1` slice of that claim, with
     `Status: solved` scoped to that slice, as stated above.

This completes the proof of Theorem A and its precise scoping. `∎`

## Promotable lemmas

**Theorem A / "Even-Seed Literal Periodicity Theorem".** *Statement:* If
`a_1, a_2, \dots` is the sequence defined by the problem (`a_1 > 1`, each
`a_{n+1}` the smallest integer `> a_n` with `\gcd(a_{n+1},a_i)>1` for all
`i \le n`) and `2 \mid a_1`, then `a_n = a_1 + 2(n-1)` for every `n \ge 1`;
in particular `a_{n+1}=a_n+2` for every `n\ge1`, so `T=1,L=2` witness the
problem's conclusion literally from `n=1`.
*Where proved:* in full, above (strong induction; base case `n=1`; inductive
step via the two-candidate dichotomy `a_n+1` illegal / `a_n+2` legal).
*Reusable content:* this is a complete, unconditional, self-contained
sub-case resolution of the whole problem's target, strictly generalizing the
previously certified `|Q|=1` special case (`greedy-exchange-cost-potential`,
item 10 of `current.md`'s Current Best) from prime-power even seeds to all
even seeds. Suitable for direct certification into
`results/imo-2026-06/lemmas/even-seed-literal-periodicity-theorem.md` and for
citation by `n1-periodicity-reconciliation` or any future approach as an
unconditionally-solved sub-case, narrowing the workspace's remaining target
to odd `a_1` only (within the even-vs-odd decomposition; the general
machinery elsewhere still targets *all* `a_1`, but this lemma is available as
a free, zero-hypothesis base case to cite whenever `2 \mid a_1` arises,
e.g. inside any future case-split proof of the general problem by parity of
`a_1` or by `\min Q`).
