## Status
partial

## Approaches tried
- Round 1: Fixed the circularity flagged by the outline reviewer in the
  a_n = O(n) upper bound. Found and fully proved an UNCONDITIONAL bound
  a_{n+1} - a_n ≤ rad(a_1) for every n ≥ 1 (Key Lemma below), using only the
  observation that a_1 is a member of every constraint list (since 1 ≤ n for
  all n ≥ 1) — not a density/threshold assumption. This resolves the
  circularity completely: the O(n) bound on a_n no longer presupposes any part
  of the "active prime set stabilizes" lemma. Verified numerically for
  a_1 ∈ {6, 12, 15, 21, 33, 35, 105, 210} that max gap ≤ rad(a_1) always holds
  (equality/near-equality attained in several cases), confirming the bound is
  both correct and essentially tight.
  Then attempted to run the original Lemma B (growth/counting contradiction
  ruling out infinitely many "fresh" primes) on top of this fixed bound, and
  found IT DOES NOT CLOSE: the argument "q_k = O(n_k)" that falls out of the
  bound is not a contradiction, because a freshly-recruited prime q_k need not
  be the cause of a large gap — it can ride along as an incidental extra
  factor of a term whose gap was already forced small by other, non-fresh
  primes. So a fresh prime being merely "large" is fully consistent with the
  bounded-gap lemma; no purely quantitative counting contradiction follows.
  This is a genuine, checked dead end for Lemma B as originally conceived
  (recorded below so it is not retried), not a hand-wave: see "Why Lemma B's
  original mechanism fails" for the demonstration. The remaining content
  needed to finish the problem (finiteness of the active prime set, or an
  equivalent) is the same core difficulty isolated by active-set-stabilization
  and state-compactness-pigeonhole, and — as anticipated by the outline
  reviewer — this approach's honest conclusion is that it does not offer an
  independent route around that lemma, but it DOES supply a genuinely useful,
  now fully rigorous, non-circular growth bound that those approaches can use
  as an ingredient (see Promotable lemmas).

## Current best

**Fully proved, unconditionally (no circularity):**

*Key Lemma (bounded gap).* Let R = rad(a_1) = product of the distinct primes
dividing a_1. Then for every n ≥ 1,
  a_{n+1} - a_n ≤ R,
and consequently a_n ≤ a_1 + (n-1)R for all n ≥ 1, i.e. a_n = O(n).

Proof is given in full below under "Full argument, Part 1." This is a
complete, self-contained, non-circular derivation — it uses nothing beyond
the problem's own definition and does not assume any density threshold or
any property of an "active set" that has not already been established.

**Not established (open gap):** finiteness of the set of primes that divide
infinitely many terms of the sequence (equivalently, the "active prime set"
stabilizes). This is the same core lemma that active-set-stabilization and
state-compactness-pigeonhole are working on; this approach's own candidate
mechanism for it (Lemma B, growth/counting) is shown below to fail as
originally conceived, and no replacement mechanism was found this round. The
gap is therefore: **prove that only finitely many primes ever divide
infinitely many terms of (a_n)**, from which the pigeonhole-on-finite-state
finish (shared machinery, see active-set-stabilization Lemma 3 /
state-compactness-pigeonhole) yields T, L.

## Full argument, Part 1 (fully proved — resolves the circularity)

**Setup and elementary facts.**

The sequence (a_n) is strictly increasing by construction: a_{n+1} > a_n is
part of the definition.

**Fact 0 (a_1 is always a live constraint).** For every n ≥ 1, since 1 ≤ n,
the defining condition on a_{n+1} includes the requirement
  gcd(a_{n+1}, a_1) > 1.
This is immediate from the problem statement: a_{n+1} is required to satisfy
gcd(a_{n+1}, a_i) > 1 for all i ≤ n, and i = 1 is one of these indices for
every n ≥ 1. In particular, **every term a_m with m ≥ 2 shares a common prime
factor with a_1.**

Let p_1 < p_2 < ... < p_r be the distinct prime factors of a_1 (r = ω(a_1) ≥
1, since a_1 > 1), and let P = {p_1,...,p_r} and R = rad(a_1) = p_1 p_2 ⋯ p_r.
By Fact 0, for every m ≥ 2, a_m is divisible by at least one prime in P.
Also a_1 itself is (trivially) divisible by every prime in P, since P is
exactly the set of a_1's prime factors and R = rad(a_1) | a_1. So:

**Fact 1.** For every n ≥ 1, a_n is divisible by at least one prime of P.

**Key Lemma (bounded gap).** For every n ≥ 1,
  a_{n+1} - a_n ≤ R.

*Proof.* Fix n ≥ 1. Let M be the smallest multiple of R that is strictly
greater than a_n; explicitly M = R · (⌊a_n/R⌋ + 1). Since M is obtained by
rounding a_n up to the next multiple of R, and consecutive multiples of R
differ by exactly R,
  M ≤ a_n + R.               (†)
(If a_n itself happens to be a multiple of R, M = a_n + R exactly; otherwise
M is strictly closer, so the inequality (†) holds in all cases — it is the
standard "rounding up to the next multiple" bound.)

We claim M is a valid choice for a_{n+1}, i.e. M > a_n (clear, by
construction of M) and gcd(M, a_i) > 1 for every i = 1,...,n.

Fix any i with 1 ≤ i ≤ n. By Fact 1, a_i is divisible by some prime p ∈ P.
Since R = p_1 p_2 ⋯ p_r is divisible by every prime in P (in particular by
p), and M is by construction a multiple of R, M is also divisible by p.
Hence p divides both M and a_i, so
  gcd(M, a_i) ≥ p > 1.
Since i was arbitrary in {1,...,n}, M satisfies gcd(M, a_i) > 1 for every
i ≤ n, and M > a_n. Thus M is a legal candidate for a_{n+1} in the greedy
definition.

Because a_{n+1} is defined as the *smallest* integer exceeding a_n satisfying
all these gcd conditions, and M is one such integer,
  a_{n+1} ≤ M ≤ a_n + R
by (†). This proves the Key Lemma. ∎

**Corollary (linear growth, unconditional).** For all n ≥ 1,
  a_n ≤ a_1 + (n-1)R.

*Proof.* Immediate by summing the Key Lemma's bound over the n-1 steps from
a_1 to a_n: a_n = a_1 + Σ_{k=1}^{n-1} (a_{k+1}-a_k) ≤ a_1 + (n-1)R. ∎

This Corollary is exactly the a_n = O(n) bound that the outline originally
needed for Lemma B, but it is now derived **without** any appeal to a density
threshold being reached, or to any property of primes beyond those dividing
a_1 itself — so the circularity flagged by the outline review is resolved.

## Full argument, Part 2 (why the original Lemma B does not close, and what
remains)

**Setup for Lemma B.** Say a prime q is *freshly recruited at step n+1* if
q | a_{n+1} but q does not divide any of a_1,...,a_n. Suppose, toward a
contradiction (as the outline proposed), that infinitely many distinct primes
are ever freshly recruited: there are indices n_1 < n_2 < ... and pairwise
distinct primes q_1, q_2, ... with q_k freshly recruited at step n_k + 1.

The outline's intended mechanism was: a fresh prime q_k forces a large gap
a_{n_k+1} - a_{n_k}, and summing these forced-large gaps would make a_{n_k}
grow faster than the linear bound from the Corollary, a contradiction.

**Why this fails.** The Key Lemma shows every gap a_{n+1}-a_n, fresh prime or
not, is already bounded by the *fixed* constant R = rad(a_1), independent of
n. So the mere fact that a_{n_k+1} is divisible by a large fresh prime q_k
does NOT force the gap a_{n_k+1}-a_{n_k} to be large: q_k can divide
a_{n_k+1} while a_{n_k+1} still satisfies a_{n_k+1} - a_{n_k} ≤ R, provided
some other, already-active prime (e.g. one in P, or a previously-recruited
prime) is simultaneously responsible for keeping a_{n_k+1} close to a_n_k
(i.e. keeping all r + (previously active) constraints satisfied), while q_k
is present in a_{n_k+1}'s factorization purely incidentally (a_{n_k+1} can be
composite with several prime factors; only one of them needs to be "doing
the work" for each constraint i ≤ n_k, and q_k need not be doing any work at
all — it can be a totally extraneous factor).

Concretely: numerically (a_1 = 15 example, computed this round) every term
a_n for n ≥ 2 in fact carries a large collection of prime factors beyond the
minimum needed (e.g. a_25 = 105 = 3·5·7, a_53 = 210 = 2·3·5·7,
a_60 = 234 = 2·3^2·13): "fresh" primes such as 7, 11, 13, 17, 19, 23, ...
appear over and over as one-off extra factors of otherwise cheaply-satisfied
terms, without ever forcing those specific terms' gaps to be unusually large.
So q_k = O(a_{n_k+1}) is true (trivially, since q_k | a_{n_k+1}) but there is
no accompanying LOWER bound forcing q_k to be comparable to the gap
a_{n_k+1}-a_{n_k}; the gap is controlled entirely by R regardless of which
fresh prime, if any, happens to also divide a_{n_k+1}. Hence no counting or
averaging argument purely on gap sizes can rule out infinitely many fresh
primes: the mechanism the outline proposed conflates "a fresh prime appears"
with "a fresh prime is forced by a large gap," and these are different
statements — only the latter would contradict the bounded-gap Key Lemma, and
we have not been able to establish the latter (indeed the numeric evidence
above suggests it is false: fresh primes typically appear as incidental
extra factors of terms with already-small, R-bounded gaps).

**Conclusion on Lemma B.** We record this as a genuine, checked dead end: the
purely quantitative growth/counting mechanism for proving "only finitely many
primes are ever freshly recruited" does not work, because infinitely many
distinct fresh primes recruited as *incidental* factors is fully consistent
with the bounded-gap Key Lemma. Ruling out infinitely many *permanently
load-bearing* primes (primes that must keep recurring to satisfy constraints
against a growing set of earlier terms) requires tracking something finer
than gap size — specifically, which prime is actually doing the covering
work for each constraint, and whether the total constraint-load can be
absorbed by a bounded set of primes. This is exactly the density/threshold
mechanism used in active-set-stabilization and the state-based mechanism in
state-compactness-pigeonhole; this approach does not supply an independent
alternative to it.

## Round 2 revision — REJECTED by outline-reviewer (do not build as stated)

The outliner proposed (transcribed from /tmp/round-2/proof-outliner.md, never persisted
here) a new "quantitative threshold" mechanism: fix finite Q known to cover a_1..a_n, let
M_Q = next multiple of ∏Q after a_n (≤ a_n+g(Q)); claim "**p_0 < g(Q_j) is a necessary
condition for a fresh prime p_0∉Q_j to ever be recruited**," i.e. if a fresh candidate
m < M_Q is divisible by p_0 with a_n < m < a_n+g(Q), then p_0 ≤ m-a_n < g(Q).

**This claim is FALSE in general, not merely under-tightened.** Counterexample to the
underlying inequality: take any prime p_0 and set a_n ≡ -1 (mod p_0). Then the very
FIRST multiple of p_0 exceeding a_n is a_n+1 — distance 1 from a_n — regardless of how
large p_0 is. E.g. p_0=97, a_n=96: next multiple of 97 is 97, distance 1, while p_0=97
can be arbitrarily larger than any fixed g(Q). (Verified numerically.) So "p_0 divides an
integer close to a_n" carries NO upper bound on p_0 — a huge prime can have its first
multiple land arbitrarily close to a_n purely by residue alignment. The outline's own
self-flagged caveat ("needs p_0|m to force p_0≤m-a_n only when m is the FIRST multiple of
p_0" ) does not rescue the argument, since the counterexample above already uses the
first multiple. **Do not attempt to "tighten" this inequality — it is false as a general
statement about integers, so no amount of tightening produces a valid necessary
condition of this shape.** If a correct version exists it must exploit something beyond
"p_0 divides some integer in a short window" (e.g. a genuine constraint from the FULL
history, not just window position) — but no such argument was found or attempted this
round, and this approach has now failed twice (round 1's counting mechanism, round 2's
window-position mechanism) with no independent route to the central gap remaining.
**Recommend this approach be treated as exhausted for the central gap** unless a
genuinely different mechanism is proposed; do not re-dispatch a builder on this specific
skeleton. The certified bounded-gap lemma (Promotable lemmas, below) remains valid and
useful; only the "S/Q finiteness via window-position" idea is dead.

## Open gaps

- **Finiteness of the "active prime set."** Not proved by this approach.
  What IS proved (Key Lemma + Corollary) is a legitimate, reusable ingredient
  toward it: it establishes a_n = O(n) unconditionally, which the density
  approaches can use as a clean starting point instead of re-deriving their
  own (potentially circular) growth bound.
- **The finish (pigeonhole → periodicity, and prefix extension to hold for
  all n, not just eventually).** Not attempted in this file; shared with
  sibling approaches.

## Cases to cover
- a_1 a prime power (r = 1, P = {p_1}, R = p_1): the Key Lemma still applies
  verbatim and gives the sharpest form of the bound (gap ≤ p_1). No special
  case is needed; the proof of the Key Lemma did not assume r ≥ 2.
- a_1 with multiple prime factors (r ≥ 2): also covered verbatim by the Key
  Lemma's proof, which works for any r ≥ 1.
  (No case split was actually needed in the Key Lemma's proof — it is
  uniform in r. The case split matters only for the still-open finiteness
  lemma, where it was hoped, but not established, that some interaction
  between a_1's own primes and freshly recruited primes could be exploited.)

## Watch out for
- Do not conflate "a_{n+1} is divisible by a fresh prime q" with "the gap
  a_{n+1}-a_n is caused by q" — Part 2 shows these are genuinely different
  and conflating them is exactly the error in the original outline's Lemma B.
- The Key Lemma's bound a_{n+1}-a_n ≤ R = rad(a_1) is about ALL gaps, not
  just those where a fresh prime appears; it holds even at steps where no
  fresh prime is ever recruited.

## Promotable lemmas

**Bounded-gap lemma (fully proved, non-circular).**
*Statement:* For the greedy sequence (a_n) of the problem, let
R = rad(a_1) = product of the distinct primes dividing a_1. Then
a_{n+1} - a_n ≤ R for every n ≥ 1, and hence a_n ≤ a_1 + (n-1)R for all n ≥ 1.
*Where proved:* This file, section "Full argument, Part 1" above, in full
(the "Key Lemma" and its "Corollary").
*Why it's useful to certify:* It gives an unconditional a_n = O(n) growth
bound derived from nothing but Fact 0 (a_1 is a constraint for every n) —
no density-threshold assumption is used. Both active-set-stabilization
(which needs a non-circular growth bound as a base case / normalizing tool)
and state-compactness-pigeonhole (which needs to show a "sufficient" K, L_0
exist) can cite this instead of re-deriving their own version, closing one
of the issues flagged in the outline review for those two approaches.
