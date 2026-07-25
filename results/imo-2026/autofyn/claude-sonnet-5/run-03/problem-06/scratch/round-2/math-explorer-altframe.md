## imo-2026-06

### Mandate
Round 1's entire population (3 built approaches) converged on one framing:
"identify a finite active prime set S, then pigeonhole mod L = prod(S)."
This report scouts genuinely different top-level framings that do NOT
require first proving S finite by a counting/pigeonhole argument on primes.

### Distinct openings (new framings, not variants of the shared-gap route)

1. **Reframe as a covering-system / sieve problem, not a prime-counting
   problem.** The acceptance rule says: candidate m is admissible past index n
   iff for every i ≤ n, m lies in ∪_{p | a_i} pℤ (m shares *some* prime factor
   with a_i). So the "excluded/forbidden" set contributes an arithmetic
   progression-union per term, and the whole sequence is exactly an
   inclusion-exclusion / covering-system construction: {a_n} is precisely the
   greedy enumeration of ℤ_{>1} sieved by a *growing* system of congruence
   unions ∪_p pℤ, one union added per accepted term (with the finitely many
   primes of that term). Instead of asking "is the set of eventually-recurring
   primes S finite?" (a statement about *primes*), ask the dual/covering-system
   question: "does the union of forbidden-residue classes stabilize to a
   fixed union of arithmetic progressions?" This is the natural home of the
   **Erdős covering-system literature** (finite covering systems of
   congruences, minimum modulus, density of the union) — not currently in
   knowledge_base.md; flag as a candidate to add. The reformulation doesn't
   solve the gap by itself, but it changes the target from "prime set finite"
   to "union-of-APs density saturates to 1 using finitely many moduli," which
   may admit density/measure tools (e.g. a positive-density argument like the
   crux move in aimo-0680 below) instead of pure prime-counting.

2. **Profinite-compactness framing (topological, not counting).** Consider
   the sequence (a_n mod m!)_{m≥1} as defining, via compatible reductions, an
   element of the profinite completion $\hat{\mathbb Z} = \varprojlim
   \mathbb Z/m!\mathbb Z$ — a *compact* space. Any infinite sequence of
   integers has (by compactness / a diagonal argument, i.e. König's lemma on
   the tree of residues) a subsequence along which the reductions mod every
   fixed modulus stabilize. The idea: don't try to *identify* S combinatorially;
   instead extract a limit object ρ ∈ ẑ from the gcd-defining property itself
   (using that gcd(a_j,a_i)>1 is a mod-a_i statement) and argue algebraically
   that this limit must be *rational* (i.e. correspond to an honest integer
   or eventually-periodic residue pattern) — because the defining rule is a
   *first-order, decidable, monotone* condition on residues, so the limit
   configuration can't be "generic" (an irrational profinite element would
   correspond to a residue pattern with no periodic witness, contradicting
   minimality/greediness at each finite stage). This is a genuinely different
   top-level target — a compactness/topological rigidity statement rather
   than a prime-recruitment count — but is speculative; the "must be
   rational" step is the new gap it would introduce, not yet shown easier
   than the original.

3. **Density/cost argument on SMALL primes specifically (numerically
   motivated — see below).** Numerical experiments (this round) show that
   primes *not dividing a_1 at all* (e.g. 2, when a_1 = 15 or 35) get
   recruited into the high-frequency ("above-baseline") tier of the sequence,
   often with the *highest* observed frequency of all primes. This suggests
   attacking finiteness of S from the "cheap primes always win" side rather
   than the "bound the primes recruited" side: argue directly that small
   primes (2, 3, and finitely many more, determined by a computable threshold
   depending only on a_1) *must* eventually be used with density approaching
   1, because using a large one-off prime q to satisfy a constraint requires
   waiting for a specific multiple of q, and the greedy rule will almost
   always find a cheaper candidate using an already-established small prime
   first once enough small primes have been "unlocked" — a quantitative
   "cost comparison" (jacobsthal-covering-bound's self-sufficiency criterion
   already gestures at this) but reframed as **a lower bound on density of
   coverage by an EXPLICIT small set of primes** (2, 3, 5, ... up to a
   threshold computable from a_1 alone) rather than an abstract existence
   claim about S. This still needs a real quantitative lemma (not found this
   round) but is a different attack surface: instead of bounding *how many*
   primes are recruited, directly show the *density contributed by small
   primes* saturates.

4. **Reverse the roles: work with the complement set B = ℤ_{>1} \ {a_n} (the
   "skipped" integers) and its structure**, rather than the sequence itself.
   By the certified bounded-gap lemma, B has bounded gaps too (every window
   of length rad(a_1) contains an accepted term), so B is a "thin" set with
   an explicit density bound. If one could show B is eventually a union of
   finitely many full residue classes mod some L (i.e. B is eventually
   periodic as a set), periodicity of {a_n} follows immediately without ever
   separately establishing "S". This swaps the target from "prove S finite"
   to "prove the *complement* stabilizes" — plausibly no easier, but it is a
   different induction variable (density of B in windows, rather than
   identity of recruited primes), and might combine better with the already-
   proved bounded-gap lemma (which is a statement purely about B's gap
   structure).

### Why these might avoid the current wall
Round 1's three approaches all reduce the problem to "count/bound the primes
ever recruited into S" and this round independently confirmed (twice) that
naive counting mechanisms (bounding ω(a_n), bounding gaps via rad(a_1),
counting freshly-recruited primes) are *provably insufficient in isolation*.
Framings 1 and 4 change the object of study from "a set of primes" to "a
union of arithmetic progressions / a density," which may be attackable by
covering-system or density tools that don't reduce to raw prime-counting.
Framing 3 flips the direction of attack (show small primes dominate, rather
than showing large primes don't accumulate) — a different inequality
direction than growth-rate-contradiction's failed attempt. Framing 2 is the
most speculative (introduces a new, unverified "must be rational" gap) and
should be considered lowest priority unless the others also stall.

### Candidate technique(s)
- Covering systems of congruences (Erdős-style) — not in knowledge_base.md;
  worth adding.
- Density / positive-density-of-a-union arguments (crux move in aimo-0680,
  see below).
- Profinite compactness / König's lemma on residue trees (speculative).
- Cost/frequency comparison between a "small prime" candidate and a
  "large one-off prime" candidate at a fixed step (extends
  jacobsthal-covering-bound's self-sufficiency criterion, reframed
  quantitatively).

### Cheap-kill candidates
None obvious beyond what's already found (bounded-gap lemma, S-covering
lemma). No parity/pigeonhole shortcut spotted that bypasses the central gap
entirely in one step.

### Knowledge-base entries to use
- **Pigeonhole / extremal principle**, **Bertrand's postulate**, **Dirichlet's
  theorem** (all already considered by round-1 approaches) — still relevant
  background but not the missing ingredient.
- **NOT currently in knowledge_base.md but worth requesting**: covering
  systems of congruences (Erdős/Selfridge-style results on minimum modulus
  and density of unions) — closest fit to framing 1.

### Analogous past problems (cruxes)
Searched `past_crux_moves_database.json` across number_theory, combinatorics,
algebra for keywords {greedy, gcd, coprime, eventually periodic, covering
system, density, profinite, compactness, sieve}. No crux is a close
structural match to "greedy gcd-linked sequence is eventually an AP." Closest
loose analogies (none load-bearing-identical, use with caution):
- `aimo-0680` (number_theory, size-bounding-and-descent): "When finitely many
  rows are known arithmetic progressions, subtract their predictable
  per-window element counts from each fixed-length window to show the
  remaining rows jointly have constant positive density, pinning a linear
  growth bound." — Analogous *shape* to framing 1/4: once some structure is
  known to be periodic/AP, the "remainder" is shown to have a stable density
  by subtraction. Could inspire a density-subtraction argument once even a
  few primes of S are confirmed, to bound what's left. Not a direct crux for
  this problem (different combinatorial setup), flagged as inspiration only.
- `aimo-0212` (number_theory, divisibility-and-gcd): "Show every prime
  dividing a polynomial's values lies in a fixed finite set, then invoke that
  a polynomial with finitely many prime divisors over the integers must be
  constant." — Not directly applicable (our object is a sequence, not a
  polynomial), but the underlying rigidity principle ("finitely many prime
  divisors forces very restricted structure") is thematically close to what
  we need to prove about S; worth keeping in mind as the *flavor* of rigidity
  result we're trying to establish, even though the polynomial-specific proof
  doesn't transfer.
- `aimo-0648` (algebra, sequences-and-recurrences): "Show an order statistic
  (max/min) of the terms is preserved by the recurrence to confine the
  sequence to a bounded interval, forcing eventual periodicity of an integer
  sequence." — Same *spirit* as the round-1 shared framing (bounded state ⇒
  finite-state ⇒ eventual periodicity), but its mechanism relies on the
  recurrence depending only on a *bounded window* of prior terms, which is
  exactly what fails here (our rule depends on ALL prior terms, i=1..n). This
  is why the direct transfer doesn't work — it independently confirms that
  the central gap is precisely "reduce the unbounded-history dependency to a
  bounded/finite-state one," not a new route around it.
No crux move found that resolves an "unbounded-history-dependent" greedy gcd
process directly; if the outliner wants a structurally novel resolution, it
will likely have to be original rather than adapted wholesale from the corpus.

### Prior progress
As recorded in `results/imo-2026-06/current.md`: two certified unconditional
lemmas (every term meets a recurring prime; bounded-gap a_{n+1}-a_n ≤
rad(a_1), hence a_n = O(n)). Central gap (finiteness of S) and secondary gap
(extend eventual periodicity down to n=1) both open, confirmed unclosed by
three independent round-1 approaches.

### Dead ends (do not retry)
- Bounding ω(a_n) directly (active-set-stabilization): produces inequality
  K² ≤ N log₂(a_N), never a contradiction — confirmed insufficient.
- Counting "freshly recruited" primes against the bounded-gap bound
  (growth-rate-contradiction): a fresh large prime need not cause a large
  gap, so this mechanism cannot bound the number of freshly recruited
  primes — confirmed insufficient.
- Any attempt to pin down L = rad(a_1) (primes of a_1 only) as the eventual
  modulus: **numerically refuted this round** (see below) — S provably
  contains primes not dividing a_1 (e.g. 2 for a_1=15, 35), so L cannot be
  computed from a_1's factorization alone; any approach assuming L = rad(a_1)
  is wrong and should not be pursued.

### Small-case / intuition notes (conjecture, from this round's numerics)
Simulated the greedy sequence for a_1 ∈ {15, 35, 105} out to 3000 terms (fast
sieve-based factorization, not sympy — sympy's `factorint` was too slow for
this many candidates and timed out once).
- For a_1 = 15 (P = {3,5}): observed prime frequencies over 3000 terms:
  2 → 87.5%, 3 → 75%, 5 → 50%, 7 → 14.3% (≈ baseline 1/7, i.e. NOT
  above-baseline), 11 → 9.1% (≈ baseline 1/11). This strongly suggests
  (conjecturally) S = {2,3,5} for a_1=15 — note **2 ∈ S despite 2 ∤ 15**,
  confirming S is not simply rad(a_1)'s prime factors.
- For a_1 = 35 (P={5,7}): 2 → 73.5%, 3 → 52.9%, 5 → 88.2%, 7 → 29.4%, all
  clearly above their baselines (1/2, 1/3, 1/5, 1/7 respectively); 11 → 9.1%
  (baseline). Conjecturally S = {2,3,5,7}, L = 210 — matches the
  jacobsthal-covering-bound file's empirical L=210 for a_1=35.
- For a_1 = 105 (P={3,5,7}): 2 → 98.3% (nearly saturating!), 3 → 62%,
  5 → 37.9% (just above baseline 20%), 7 → 27.6% (above baseline 14.3%).
  Conjecturally S = {2,3,5,7} again, L=210, consistent with jacobsthal file.
- Even out to 3000 terms, ODD terms still occur near the very end of the
  simulated range (last odd-indexed term at index ~2990+ of 3000 for all
  three a_1 values) — i.e. no observed finite cutoff within this range after
  which ALL terms share prime 2. This is consistent with S being finite
  (odd terms are fine as long as divisible by some other S-prime like 3,5,7)
  but shows convergence to the "final" periodic regime is slow — the
  transient could be long, so any argument for periodicity must not assume
  a fast/explicit stabilization index.
- Overall numeric conjecture: **S always contains 2 and 3** (in these three
  examples) regardless of whether 2, 3 divide a_1, suggesting the true
  mechanism for finiteness of S may hinge on showing small primes are
  "irresistible" to the greedy rule once the sequence is dense enough —
  supporting framing 3 above as the most numerically-grounded new angle.
