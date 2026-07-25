## Status
unsolved

## Approaches tried
(none yet — first outline, round 1)

## Current best

### Setup (shared crux move, same as all approaches)
For a prime `p`, a move on positions with `v_p`-values `(a,b)` replaces them by
`(\min(a,b),|a-b|)`. Two identities: (I2) `\gcd(\min(a,b),|a-b|)=\gcd(a,b)` (used for
part b, identical to the other approaches) and here, for part (a), a **linear** (not
quadratic) potential:

### Part (a): termination via `\Omega` (total prime factors with multiplicity)
For a positive integer `x`, let `\Omega(x) = \sum_p v_p(x)` (with multiplicity). Define
the board total `T = \sum_{i=1}^{2026} \Omega(a_i) = \sum_p \sum_i v_p(a_i)` — a single
linear count, easier to compute/verify than a sum of squares.

Claim (exact identity, not just an inequality, at the level of the touched pair): for a
chosen pair `(m,n)` with `g=\gcd(m,n), q=lcm(m,n)/\gcd(m,n)`,
`\Omega(g)+\Omega(q) = \sum_p \big(\min(v_p(m),v_p(n)) + |v_p(m)-v_p(n)|\big)
 = \sum_p \max(v_p(m),v_p(n))`.
Since `\max(a,b) = a+b-\min(a,b) \le a+b`, with equality iff `\min(a,b)=0`:
`\Omega(g)+\Omega(q) \le \Omega(m)+\Omega(n)`, equality **iff no prime divides both
`m` and `n`, i.e. iff `\gcd(m,n)=1`.**

So `T` is non-increasing under every move, and strictly decreases by exactly
`\sum_{p \mid \gcd(m,n)} \min(v_p(m),v_p(n)) = \Omega(\gcd(m,n)) \ge 1` whenever
`\gcd(m,n)>1`.

This alone doesn't finish termination (a run could in principle always choose coprime
pairs, holding `T` fixed forever). Pair `T` with `N` = number of board entries `>1`
exactly as in the sibling lex-potential approach: `N` never increases and strictly
decreases by exactly 1 whenever `\gcd(m,n)=1` (via the "not both g,q=1" lemma:
`gq=mn>1$ for `m,n>1$, so if `g=1` then `q=mn>1$, giving exactly one survivor `>1$).

So: **every move strictly decreases the lexicographic pair `(N,T)`** — `T` drops
(N possibly unchanged) when `\gcd(m,n)>1`; `N` drops by 1 (T possibly unchanged) when
`\gcd(m,n)=1`. `(N,T) \in \mathbb{N}\times\mathbb{N}$ is well-founded, so the process
terminates. As in the sibling approach, `N` cannot skip `2\to 0$, and the process only
stops once `N\le 1$, so terminal `N` is exactly 1 — completing part (a).

(This `T`-based potential is organizationally cleaner than sum-of-squares: `T` is
literally the total factor count on the board, an additive/linear quantity with a direct
combinatorial meaning ("total number of prime-factor tokens on the board never increases,
and strictly drops whenever the chosen pair shares a factor"), which may be easier for a
reviewer to verify at a glance than a sum-of-squares computation.)

### Part (b): identical to the invariant argument used by the primary approach
`G_p = \gcd(v_p(a_1),\dots,v_p(a_{2026}))` is invariant under every move (via (I2) +
gcd-associativity over a multiset), and at the terminal state `v_p(M)=G_p$ for all `p`,
giving `M = \prod_p p^{G_p}$. (No new content here vs. the sibling approach — this
approach's distinguishing content is purely the part (a) potential.)

## Key lemmas
- `\Omega(g)+\Omega(q) = \sum_p \max(v_p(m),v_p(n))$, an EXACT identity (not just an
  inequality) — because `\min+|diff|=\max$ pointwise per prime.
- `\max(a,b) \le a+b$, equality iff `\min(a,b)=0$ — elementary, because
  `a+b-\max(a,b)=\min(a,b)\ge 0$.
- "Not both g,q=1" lemma (shared with sibling approach): `gq=mn>1$ for `m,n>1$.
- (I2) `\gcd(\min(a,b),|a-b|)=\gcd(a,b)$ for part (b), identical to sibling approach.

## Open gaps
- The termination argument via `(N,T)$ is complete on paper above but needs the builder
  to write the full case split (`\gcd(m,n)=1$ vs `>1$) and confirm well-foundedness of
  lex order on `\mathbb{N}^2$ explicitly.
- Should explicitly verify `T` is always a finite integer (only finitely many primes
  divide any given `a_i$, and there are 2026 of them, so `T$ is a finite sum) — trivial
  but should be stated.
- Part (b) content is identical to the sibling `lex-potential-gcd-invariant` approach;
  if that approach's part (b) write-up is certified first, this approach can directly
  import it as a certified shared lemma from `results/imo-2026-01/lemmas/` rather than
  re-deriving.

## Cases to cover
- Same two cases as sibling approach: `\gcd(m,n)=1$ (N drops) vs `\gcd(m,n)>1$ (T drops).

## Watch out for
- `\Omega(g)+\Omega(q)=\Omega(m)+\Omega(n)$ is NOT always true (only when `\gcd(m,n)=1$)
  — don't mistake this for an invariant; it's the monovariant identity's equality case,
  not a general identity. The general fact is `\Omega(g)+\Omega(q) \le \Omega(m)+\Omega(n)$
  with the stated equality condition.
- This approach's termination proof is structurally a near-twin of the sum-of-squares
  version (both are lex pairs pairing `N` with a per-move-nondecreasing... — i.e.
  non-increasing — secondary quantity); the reviewer should judge it on presentation
  clarity, not treat it as independent evidence of correctness beyond the primary
  approach (a shared underlying mechanism, deliberately offered as an alternate
  write-up per the round's diversification request).
