## Status
partial

## Approach: density-sieve-contradiction (indirect, counting/analytic argument by contradiction)

### Target
The full problem claim: there exist positive integers T, L such that a_{n+T} = a_n + L
for every positive integer n.

### Technique
Proof by contradiction using density/counting estimates (sieve, inclusion–exclusion),
in the style of the "boundedness via contradiction" crux move in `aimo-0886` (assume the
quantity of interest is unbounded, derive a counting contradiction). Unlike the
hypergraph and covering-system approaches (which try to construct/extract the finite
prime core directly), this approach assumes the core is NOT finite (or that gaps
a_{n+1}−a_n are unbounded) and derives a contradiction from comparing the density of
"available" integers against the actual growth rate forced by the greedy rule. This is
an existence-only, indirect argument — genuinely different in spirit from the
constructive/extractive approaches.

### Skeleton
1. **Free fact** (shared): for n ≥ 2, gcd(a_n,a_1) > 1, so every a_n is divisible by
   some prime in the fixed finite set Q = P(a_1). — direct from hypothesis, i=1 case.
2. **Reformulate the target as a boundedness claim.** It suffices to show:
   (a) the sequence of gaps d_n := a_{n+1} − a_n is bounded (say by some constant M);
   and (b) the set of primes that ever divide "the reason a term is legal" — precisely,
   the union over n of (P(a_n) ∩ {primes ≤ M}) — is eventually confined to a fixed
   finite set S. Given (a) and (b), a finite-state pigeonhole argument (state = residue
   of a_n mod L, L = ∏ S, EXACTLY as in the other two approaches' final step) forces
   eventual periodicity — cite `knowledge_base.md` "Linear recurrences: sequences are
   eventually periodic mod m" for the general shape of this last step. **This
   approach's novel content is entirely in proving (a) directly** (gap-boundedness),
   rather than proving finiteness of S first and deriving boundedness as a consequence
   (the order of the other two approaches).
3. **Key Lemma (gap-boundedness by contradiction) — THE GAP.** Claim: d_n =
   a_{n+1} − a_n is bounded over all n. Proof strategy: suppose not — then there is a
   subsequence n_1 < n_2 < ... with d_{n_j} → ∞. For each such j, EVERY integer m in
   the window (a_{n_j}, a_{n_j} + d_{n_j}) fails to hit some earlier term's prime set,
   i.e., is "blocked." Count blocked integers in a window of length W using
   inclusion–exclusion / sieve: an integer m is blocked by term a_i iff gcd(m, a_i) = 1,
   which (for a FIXED finite working set of "currently relevant" primes, i.e. primes
   dividing at least one of a_1,...,a_{n_j} that are ≤ some threshold) happens with
   density ∏_{p | a_i, p ≤ threshold}(1 − 1/p) — summing/union-bounding over the
   (finitely many, since n_j is finite) terms a_1,...,a_{n_j}, the density of integers
   NOT blocked by any is bounded below by a quantity depending on how many *distinct*
   small primes appear among a_1,...,a_{n_j} — this needs an a priori cap on "how many
   distinct small primes can appear among the first n_j terms," which circles back to
   needing a version of the core-finiteness fact; **breaking this circularity via a
   genuinely counting-only argument (not re-invoking core finiteness) is the actual
   crux of this approach** — e.g., bounding the number of distinct primes ≤ x dividing
   some a_i (i ≤ n_j) by comparing n_j (linear count of terms) against the density loss
   each new prime ≤ x contributes (Mertens' estimate ∏_{p≤x}(1−1/p) ~ 1/ln x), which
   could in principle show that using more than O(log n_j / log log n_j) small primes is
   "wasteful" for a greedy-smallest process, but making this rigorous (a genuine
   extremal/greedy-optimality argument, akin to a hitting-set LP relaxation bound) is
   not completed here.
4. **Alternative attack on the Key Lemma via "each new recruited prime pays for
   itself".** A more tractable sub-route: show directly that if the greedy process ever
   needs a prime p ∉ (primes seen among a_1,...,a_n so far, up to bound M) to serve as
   the witness for a_{n+1}, then p must be ≤ a_n + (a small bound depending on n's
   history) — because the greedy rule picks the SMALLEST legal candidate, and a
   candidate using a fresh large prime is only chosen if EVERY smaller candidate using
   only already-established primes fails the hitting condition against some a_i, i ≤ n
   — bound the number of i ≤ n that can simultaneously "block" all smaller candidates
   using established primes only, via the Q-partition from step 1 (each a_i is
   compatible with Q, so at most |Q|-many "independent blocking types" exist) — this is
   a route that avoids raw asymptotic density estimates in favor of a direct
   finite-type-counting bound, and may be more tractable than the sieve computation in
   step 3; flagged as the primary recommended sub-route for the builder to attempt
   first.
5. Once (a) gap-boundedness and (b) confinement of relevant primes to a finite S are
   established, finish exactly as in the other approaches: CRT reduction to residues mod
   L = ∏ S, deterministic cyclic map on the finite set of good residues, pigeonhole
   gives period T = (size of the good-residue set) and step L.
6. Same **back-to-n=1** caveat: verify (or re-derive) that the periodic identity holds
   from n=1, not merely eventually, via a finite check on the (finite) pre-period.

### Key lemmas (claim + mechanism)
- **Free bound on Q** — same as other approaches, direct from hypothesis (i=1 case).
- **Gap-boundedness by contradiction (THE GAP)** — mechanism: a sieve/density count
  showing a window of length W around a_n, if W is large enough relative to the number
  of distinct "load-bearing" primes seen so far, must contain an integer hitting every
  earlier term's prime set (positive relative density of "good" integers in any long
  enough window once the working prime set is fixed) — contradicting an assumed
  unbounded gap; the missing piece is bounding the number of distinct load-bearing
  primes as a function of n without circularity (step 3's genuine crux), with a
  proposed non-circular sub-route via "blocking types are capped by |Q|" (step 4).
- **CRT + finite cyclic pigeonhole finish** — identical mechanism to the other two
  approaches' final step; not itself in dispute.

### Open gaps
- Step 3/4 (gap-boundedness, non-circular) is the true unresolved crux; two candidate
  sub-routes are given (raw sieve/Mertens estimate vs. a finite-blocking-type counting
  argument) — the builder should attempt sub-route 4 first as it seems more tractable
  (a combinatorial bound via |Q|, avoiding analytic number theory machinery).
- Step 6, extending periodicity to n=1, same caveat as the other approaches.

### Cases to cover
- |Q| = 1: trivial, gaps are constant = the prime immediately, no sieve needed.
- |Q| ≥ 2: the sieve/blocking-type argument must be worked out in full for at least the
  |Q|=2 case (a_1=15, 35) as a concrete testbed before attempting the general bound.

### Watch out for
- Sieve/inclusion-exclusion density bounds are notoriously easy to state loosely but
  hard to make rigorous when the "modulus" (working prime set) is itself allowed to grow
  with n — do not let the builder silently assume a FIXED prime set when computing
  densities; the whole difficulty is that the set can (a priori) grow.
- Distinguish "gaps are bounded" (needed) from "gaps are eventually constant-period"
  (the actual, stronger conclusion) — boundedness alone is necessary but not
  sufficient; the finite-state pigeonhole step (step 5) is what upgrades boundedness to
  strict eventual periodicity, and must not be skipped or asserted for free.
