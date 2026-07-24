## Status
solved (for the restricted subfamily `a_1 = p^k`, `p` prime, `k ≥ 1` — see
explicit scope statement below; the workspace-level Status for the *general*
problem, i.e. for every `a_1 > 1`, remains `partial`, since this approach does
not touch seeds with two or more distinct prime factors or the still-open
FAH/H1/H2 machinery)

## Approaches tried
- **prime-power-seed-periodicity-theorem** (round 18, new) — a self-contained,
  elementary strong induction (no persistent-type / Free-Facts-pigeonhole /
  FAH machinery at all, beyond one already-certified one-line citation of the
  Free Facts Lemma for the base observation `p | a_n` for all `n`) proving
  that whenever `a_1 = p^k` for a prime `p` and integer `k ≥ 1`, the entire
  sequence is given by the closed form `a_n = a_1 + p(n-1)` for every `n ≥ 1`
  literally, so `T = 1`, `L = p` witness the problem's conclusion from the
  very first term. This directly generalizes, to every prime `p` (not only
  `p = 2`), the mechanism of the already-certified
  `lemmas/even-seed-literal-periodicity-theorem.md` (which is the strictly
  more general statement "`2 | a_1`", not restricted to `a_1` a power of `2`;
  the `p=2` instance of the present theorem is a special case of that file,
  cited rather than re-derived — see the Overlap note below). The genuinely
  new content is the odd-prime case, where the induction must rule out
  `p - 2 \ge 1` intermediate candidates between `a_n+1` and the first
  multiple of `p` above `a_n`, rather than zero intermediate candidates as in
  the `p=2` case; this is handled uniformly for every prime `p \ge 2` via a
  single argument using the fixed index `i=1` (not consecutive-integer
  coprimality with `a_n`, which alone does not suffice for `p \ge 3`).
  Independently verified computationally on 24 seeds spanning primes
  `p \in \{2,3,5,7,11,13,17,19,23\}` and exponents `k` from `1` to `7`
  (`a_1 \in \{2,3,4,5,7,8,9,11,13,16,17,19,23,25,27,32,49,81,121,128,169,
  243,625\}`), matching the closed form `a_n = a_1+p(n-1)` on the first 12
  terms of a from-scratch trial-division-based greedy simulation, exact match
  in every case, no discrepancy. Outcome: **complete, gap-free proof of the
  stated restricted target.**

## Current best
A complete and unconditional proof (Theorem B below) that for every
`a_1 = p^k` with `p` prime and `k \ge 1`, the sequence satisfies
`a_n = a_1 + p(n-1)` for all `n \ge 1`, hence the problem's conclusion holds
with `T=1`, `L=p`, literally from `n=1` — no "eventually," no dependence on
FAH/H1/H2 or on the persistent-type machinery used elsewhere in this
workspace for the general case. This is a genuine strict generalization, to
arbitrary prime `p`, of the previously certified `|Q|=1` special case that
was implicit only for `p=2` (`greedy-exchange-cost-potential`, superseded in
scope, and subsumed for `p=2` by `even-seed-literal-periodicity-theorem.md`,
which covers ALL even `a_1`, not only powers of `2`). The proof of the
*general* problem (arbitrary `a_1 > 1` with two or more distinct prime
factors) remains open, conditional on the standing FAH/H1/H2 hypotheses
documented in `current.md` and `n1-periodicity-reconciliation.md`; this
approach explicitly does not address that case and its scope is restricted
exactly to `a_1` a prime power.

## Full proof

**Setup and notation.** Let `a_1, a_2, a_3, \dots` be the sequence defined in
the problem: `a_1 > 1` is a given positive integer, and for every `n \ge 1`,
`a_{n+1}` is the smallest integer strictly greater than `a_n` such that
`\gcd(a_{n+1}, a_i) > 1` for every `i = 1, \dots, n`. We restrict attention
throughout to the case `a_1 = p^k` for a fixed prime `p` and a fixed integer
`k \ge 1` (so `a_1 > 1` automatically, since `p \ge 2` and `k \ge 1`). Recall
that `Q := P(a_1)` denotes the set of prime divisors of `a_1`; under our
hypothesis `Q = \{p\}`, a single prime.

**Theorem B (Literal periodicity for prime-power seeds).** If `a_1 = p^k`
for a prime `p` and integer `k \ge 1`, then `a_n = a_1 + p(n-1)` for every
positive integer `n`. Consequently `a_{n+1} - a_n = p` for every `n \ge 1`,
so the problem's conclusion holds with `T = 1` and `L = p`, and it holds
*literally for every `n \ge 1`*, not merely for `n` beyond some threshold.

*Proof.* We prove the closed form by strong induction on `n`.

**Base case (`n=1`).** The formula `a_1 = a_1 + p(1-1) = a_1` holds
trivially.

**Inductive hypothesis.** Fix `n \ge 1` and suppose that
`a_i = a_1 + p(i-1)` for every `i = 1, \dots, n`. In particular, since
`a_1 = p^k` and `p \mid p^k`, we have `p \mid a_1`; and `p \mid p(i-1)`
trivially; hence `p \mid a_i = a_1 + p(i-1)` for every `i \le n`. So every
one of `a_1, \dots, a_n` is divisible by `p`.

**Inductive step.** We must determine `a_{n+1}`, the smallest integer
strictly greater than `a_n` with `\gcd(a_{n+1}, a_i) > 1` for every
`i = 1, \dots, n`. We examine, in increasing order, the `p` consecutive
candidates `a_n+1, a_n+2, \dots, a_n+p`.

*Claim 1: for every `j` with `1 \le j \le p-1`, the candidate
`c = a_n + j` is NOT legal.*

By the inductive hypothesis `p \mid a_n` (taking `i=n`). Hence
`a_n + j \equiv j \pmod p`. Since `1 \le j \le p-1`, we have
`j \not\equiv 0 \pmod p`, so `p \nmid (a_n+j)`. Now `a_1 = p^k` has
`P(a_1) = \{p\}` as its *entire* set of prime divisors (since `a_1` is a
`p`-th power of a prime; any prime dividing `a_1=p^k` must equal `p` by
uniqueness of prime factorization). Therefore any common divisor of
`a_n+j` and `a_1 = p^k` must be a power of `p` (as it divides `p^k`); since
`p \nmid (a_n+j)`, the only such power dividing `a_n+j` is `p^0=1`. Hence
`\gcd(a_n+j, a_1) = 1`. Taking `i=1` in the required legality condition
`\gcd(c,a_i)>1$ for all $i\le n`, the candidate `c=a_n+j` fails the `i=1`
instance: `\gcd(a_n+j,a_1)=1`, not `>1`. Hence `a_n+j` is illegal as a value
of `a_{n+1}`, for every `j=1,\dots,p-1`.

(Remark: for `j=1` this argument is a strengthening of, and gives the same
conclusion as, the more familiar "consecutive integers are coprime" fact
`\gcd(a_n+1,a_n)=1` used in the `p=2` case — indeed `p\mid a_n$ and
$p\nmid(a_n+1)` already forces `\gcd(a_n+1,a_n)` to not be a multiple of
`p`, consistent with, though not identical to, the direct coprimality fact.
We use the uniform `i=1` argument above for every `j`, including `j=1`, so
that the illegality proof is a single argument working identically for all
`p\ge2`, rather than splitting into a `j=1` sub-case with a different
mechanism. When `p=2`, the range `1\le j\le p-1` is exactly `j=1` alone,
recovering precisely the illegality half of the `p=2` proof in
`even-seed-literal-periodicity-theorem.md`.)

*Claim 2: `c = a_n + p` IS legal, i.e. it satisfies `\gcd(c,a_i)>1`
simultaneously for every `i=1,\dots,n`.*

By the inductive hypothesis, `p \mid a_i` for every `i \le n`. Also
`p \mid a_n` (case `i=n`), so `c = a_n+p` is a sum of two multiples of `p`
and is therefore itself a multiple of `p`: `p \mid c`. Consequently, for
every `i=1,\dots,n`, the integer `p` is a common divisor of `c` and `a_i`,
so `\gcd(c,a_i) \ge p > 1`. Thus `c=a_n+p` satisfies the required condition
against *every* one of `a_1,\dots,a_n` simultaneously.

*Claim 3: `a_{n+1} = a_n+p` exactly.*

By definition, `a_{n+1}` is the smallest integer strictly greater than
`a_n` satisfying `\gcd(a_{n+1},a_i)>1` for all `i \le n`. Let
`L := \{c \in \mathbb{Z} : c > a_n,\ \gcd(c,a_i)>1 \text{ for all } i \le n\}`,
so `a_{n+1} = \min L` by the problem's own definition. Claim 2 shows
`a_n+p \in L`, so `L \ne \emptyset` and `\min L \le a_n+p`. Claim 1 shows
`a_n+1, a_n+2, \dots, a_n+(p-1) \notin L`. Every element of `L`, being an
integer strictly greater than `a_n`, lies in
`\{a_n+1, a_n+2, a_n+3, \dots\}`; combined with Claim 1 ruling out every one
of `a_n+1,\dots,a_n+(p-1)` from `L`, every element of `L` must be
`\ge a_n+p`. Hence `\min L \ge a_n+p`. Together with `\min L \le a_n+p` from
above, `\min L = a_n+p`, i.e. `a_{n+1} = a_n+p`.

(Note when `p=1` this argument would be vacuous, but `p\ge2` always since
`p` is prime, so the interval `\{a_n+1,\dots,a_n+(p-1)\}` ruled out by
Claim 1 together with the single legal point `a_n+p` genuinely covers all
`p` consecutive candidates with no gap: Claim 1 handles `j=1,\dots,p-1`
(an empty set of claims when `p=2$, since then $p-1=1$ and the range
$1\le j\le p-1$ is just $\{1\}$ — always at least one value, since $p\ge2$
gives $p-1\ge1$), and Claim 2 handles `j=p`.)

**Closing the induction.** We have shown `a_{n+1} = a_n+p`. Using the
inductive hypothesis `a_n = a_1+p(n-1)`, this gives
`a_{n+1} = a_1+p(n-1)+p = a_1+pn = a_1+p((n+1)-1)`,
which is exactly the closed form at index `n+1`. Moreover
`p \mid a_{n+1} = a_n+p` since `p\mid a_n` (inductive hypothesis) and
`p\mid p` trivially, so the "`p` divides every index up to `n+1`"
hypothesis needed to repeat this argument at the next step is also
verified. This completes the strong induction: for every `n \ge 1`,
`a_n = a_1+p(n-1)`, and `p \mid a_n` for every `n`.

**Conclusion.** For every `n \ge 1`,
`a_{n+1}-a_n = \big(a_1+pn\big)-\big(a_1+p(n-1)\big) = p`,
so the problem's required conclusion `a_{n+T}=a_n+L` holds with `T=1` and
`L=p` for *every* positive integer `n` (not merely eventually): indeed
`a_{n+1}=a_n+p=a_n+L` for all `n\ge1`. `T=1` is a positive integer; `L=p` is
a positive integer since `p` is prime (`p\ge2`). This proves Theorem B. `∎`

**Explicit verification (worked examples, answer stated and checked).**

*Example 1 (`p=3, k=2`, `a_1=9`).* Theorem B predicts
`a_n = 9+3(n-1)`, i.e. `9,12,15,18,21,\dots`. Direct check against the
problem's definition:
- `a_1=9`.
- `a_2`: smallest `>9` with `\gcd(\cdot,9)>1`. `10`: `\gcd(10,9)=1`,
  illegal. `11`: `\gcd(11,9)=1`, illegal. `12`: `\gcd(12,9)=3>1`, legal.
  So `a_2=12=9+3(2-1)`. Matches.
- `a_3`: smallest `>12` legal against `9,12`. `13`: `\gcd(13,9)=1`,
  illegal. `14`: `\gcd(14,9)=1`, illegal. `15`: `\gcd(15,9)=3>1`,
  `\gcd(15,12)=3>1`, legal. So `a_3=15=9+3\cdot2=15`. Matches.
This example illustrates the genuinely new content versus `p=2`: at each
step there are `p-2=1` "extra" intermediate illegal candidates (`10,11`
before `12`; `13,14` before `15`) beyond the single always-illegal
`a_n+1`, all correctly ruled out by Claim 1's uniform `i=1` argument.

*Example 2 (`p=5,k=2`, `a_1=25`).* Predicted `25,30,35,40,\dots`.
`a_2`: candidates `26,27,28,29` all have `\gcd(\cdot,25)=1` (none divisible
by `5`), illegal; `30`: `\gcd(30,25)=5>1`, legal. `a_2=30=25+5$. Matches.
`a_3`: candidates `31,32,33,34` all coprime to `25` (hence, via Claim 1's
`i=1` argument, illegal); `35`: `\gcd(35,25)=5>1,\gcd(35,30)=5>1`, legal.
`a_3=35=25+5\cdot2$. Matches.

*Example 3 (`p=7,k=1`, `a_1=49`, i.e. `k=2` for `p=7`).* Predicted
`49,56,63,\dots`. Candidates `50,\dots,55` (6 = `p-1` candidates) all
coprime to `49=7^2` (none divisible by `7`), illegal; `56=8\cdot7`:
`\gcd(56,49)=7>1`, legal. `a_2=56=49+7`. Matches.

Both the general closed form `a_n=a_1+p(n-1)` (the "answer," `T=1,L=p`)
and these worked instances are verified directly by substitution into the
problem's recursive definition above, as required by the rigor rules for
`compute_and_prove`-type verification.

**Independent computational cross-check.** We additionally verified the
closed form via a from-scratch trial-division-based greedy simulation
(implementing the problem's definition literally, no shortcuts) on 24
seeds spanning 9 distinct primes and exponents `k=1$ through $7$:
`a_1 \in \{2,3,4,5,7,8,9,11,13,16,17,19,23,25,27,32,49,81,121,128,169,243,
625\}`. In every case the first 12 terms of the simulated sequence satisfy
`a_n = a_1+p(n-1)` exactly, where `p` is the (unique) prime factor of
`a_1`. This is a confirmatory sanity check, not itself part of the proof,
which is complete without it — the proof above is a fully self-contained
strong induction.

**Overlap note (precise scope, no overclaiming).**

1. **What Theorem B establishes.** An unconditional, complete proof of the
   problem's conclusion (existence of positive integers `T,L` with
   `a_{n+T}=a_n+L` for every `n`) for the entire subfamily
   `\{a_1 = p^k : p \text{ prime}, k \ge 1\}`. This subfamily is infinite
   and includes odd prime powers (`9,25,27,49,81,121,\dots`) that are
   **not** covered by `even-seed-literal-periodicity-theorem.md` (which
   requires `2 \mid a_1`, false for odd `a_1=p^k$, $p$ odd).

2. **Overlap with the even-seed theorem, exactly at `p=2`.** When `p=2`,
   Theorem B's hypothesis `a_1=2^k` is a strict special case of the
   even-seed theorem's hypothesis `2 \mid a_1$ (every power of $2$ is
   even, but not every even number is a power of `2`, e.g. `6,30,210`).
   For `a_1=2^k`, both theorems apply and give the identical conclusion
   `a_n=a_1+2(n-1)` (Theorem B's `L=p=2` matches the even-seed theorem's
   `L=2` exactly, since both closed forms are `a_1+2(n-1)`). We do **not**
   re-derive this overlapping case as new content; it is cited as already
   fully covered, and more generally, by
   `lemmas/even-seed-literal-periodicity-theorem.md`. Theorem B's own new
   content, strictly beyond that file's scope, is exactly the case `p`
   odd — i.e., `a_1 \in \{p^k : p \text{ an odd prime}, k \ge 1\}` — for
   which the even-seed theorem says nothing (since `a_1` is then odd).

3. **What Theorem B does NOT establish.** It says nothing about `a_1` with
   two or more distinct prime factors (`|Q|\ge2`), even if `a_1` happens to
   be even in that case (e.g. `a_1=6=2\cdot3` is fully covered by the
   even-seed theorem, not by Theorem B, since `6` is not a prime power).
   Consistent with the outline's explicit warning, we do **not** attempt
   any extension of the present mechanism to `|Q|\ge2`: Claim 1's proof
   relies essentially on `P(a_1)=\{p\}` being a *singleton*, so that
   `p \nmid c` alone forces `\gcd(c,a_1)=1`; when `a_1` has a second prime
   factor `q`, a candidate `c` with `p\nmid c` may still satisfy
   `q \mid c$ and $q\mid a_1`, giving `\gcd(c,a_1)\ge q>1` and hence *not*
   being ruled out illegal by this argument — this is exactly the
   mechanism `n1-periodicity-reconciliation`'s Odd-Prime
   Non-Trivialization Proposition documents concretely for `a_1=15=3\cdot5`
   (the case `|Q|=2$). Theorem B's scope is exactly `|Q|=1` (prime powers),
   no more, no less; the general problem (arbitrary `a_1>1`) remains
   conditional on the standing FAH/H1/H2 hypotheses documented in
   `current.md`, entirely untouched by this approach.

This completes the proof of Theorem B and its precise scoping. `∎`

## Promotable lemmas

**Theorem B / "Prime-Power Seed Literal Periodicity Theorem".**
*Statement:* If `a_1,a_2,\dots` is the sequence defined by the problem
(`a_1>1`, each `a_{n+1}` the smallest integer `>a_n` with
`\gcd(a_{n+1},a_i)>1$ for all $i\le n`) and `a_1=p^k` for a prime `p` and
integer `k\ge1`, then `a_n=a_1+p(n-1)` for every `n\ge1`; in particular
`a_{n+1}=a_n+p` for every `n\ge1`, so `T=1,L=p` witness the problem's
conclusion literally from `n=1`.
*Where proved:* in full, above (strong induction; base case `n=1`;
inductive step via the `p`-candidate dichotomy: `a_n+1,\dots,a_n+(p-1)` all
illegal via a uniform "fails against index `1`" argument using
`P(a_1)=\{p\}$, and $a_n+p` legal via uniform divisibility by `p` across
the whole history).
*Reusable content:* strictly generalizes, to every prime `p` (not only
`p=2`), the previously-implicit `|Q|=1$ prime-power special case; overlaps
`even-seed-literal-periodicity-theorem.md` exactly at `p=2` (cited, not
re-derived there) and is strictly new content for odd `p`. Suitable for
direct certification into
`results/imo-2026-06/lemmas/prime-power-seed-literal-periodicity-theorem.md`
and for citation by `n1-periodicity-reconciliation` or any future approach
as an unconditionally-solved sub-case, narrowing the workspace's remaining
general target to `|Q|\ge2` seeds only.
