## Status
partial

## Approach: hypergraph-transversal (intersecting-family / minimal-antichain, monovariant potential)

### Target
The full problem claim: there exist positive integers T, L such that a_{n+T} = a_n + L
for every positive integer n.

### Technique
Encode each term by its set of prime divisors P(a_i) ⊆ primes. The defining rule says
P(a_{n+1}) must be a **transversal** (hitting set) of the hypergraph whose edges are
{P(a_1),...,P(a_n)}. Reduce this hypergraph to its **antichain of inclusion-minimal
edges** M_n (a set B is redundant once a subset A ⊆ B with A also an edge appears,
since hitting A automatically hits B). Argue M_n stabilizes to a FIXED finite antichain
M using a monovariant/potential-function argument (extremal set theory), then finish by
pigeonhole on a finite state space (residues mod L = product of the primes that ever
appear in M).

### Skeleton
1. **Free fact**: for every n ≥ 2, gcd(a_n, a_1) > 1 (take i = 1 in the hypothesis
   applied at step n−1). Hence P(a_n) ∩ Q ≠ ∅ where Q := P(a_1), a *fixed finite* set
   (|Q| ≤ log2 a_1). — by definition of the recurrence, immediate.
2. Define the minimal antichain M_n = the inclusion-minimal elements of
   {P(a_1),...,P(a_n)} (as sets of primes). Show: (a) a candidate integer m > a_n is a
   legal choice for a_{n+1} iff P(m) hits every set in M_n (transversal property, since
   hitting the minimal sets hits all supersets too); (b) M_{n+1} is obtained from M_n by
   either leaving it unchanged, or inserting P(a_{n+1}) as a new minimal element and
   deleting any old elements of M_n that are supersets of P(a_{n+1}) — by set inclusion
   logic alone, no analytic input needed.
3. **Key Lemma (finiteness of the eventual prime support) — THE GAP.** Claim: there is
   a finite set S of primes and an index n_0 such that for all n ≥ n_0, every element of
   M_n is a subset of S, and M_n = M is a single fixed antichain over S for n ≥ n_0.
   Proposed mechanism: define the potential Φ_n = Σ_{B ∈ M_n} 2^{-min(B)} (min(B) = the
   smallest prime in B, under an enumeration of all primes). Since inserting a new
   minimal set P(a_{n+1}) can only delete supersets (never create new small-prime
   elements without deleting the sets they now dominate) and Q act as a fixed "floor,"
   argue Φ_n is bounded and takes finitely many distinct values reachable via legal
   moves from Φ_{n_0}; combine with a counting bound on how many times a set B ∈ M_n
   can be replaced by a proper subset before it is minimal within Q's bound (chains in
   the subset lattice of Q ∪ (primes used) have length ≤ |Q|+|S|, finite once S is
   posited finite) to close the circularity — this direction of the argument alone does
   NOT yet prove S is finite a priori; it only shows *if* S is finite, M_n stabilizes in
   finite time. The actual finiteness of S needs an auxiliary growth argument (not
   supplied by this framing alone): if infinitely many distinct primes were ever forced
   into M_n's elements, then infinitely often the smallest valid candidate a_{n+1} must
   be a multiple of a *fresh* prime not related to S so far — this should be excluded by
   comparing against the density of already-known-good integers (a hand-off to a
   sieve/counting estimate is unavoidable here; flag as the true crux).
4. **Given** the Key Lemma, let L = ∏_{p ∈ S} p (squarefree). For n ≥ n_0, whether an
   integer m is a legal successor of a_n depends only on m mod L (since P(m) ∩ S is
   determined by m mod L, and M is fixed) — by CRT (`knowledge_base.md` "Modular
   arithmetic, CRT").
5. Consider the deterministic map f: (residue class mod L) ↦ (next larger legal
   residue mod L, cyclically wrapping with +L). This is a well-defined function on the
   finite set of "good" residues G = {r mod L : r hits every set in M} (G is nonempty
   since a_{n_0+1} mod L ∈ G). Enumerate G = {r_1 < r_2 < ... < r_T} (T = |G|); the
   greedy process for n ≥ n_0 visits r_1, r_2, ..., r_T, r_1+L, r_2+L, ... in order —
   by determinism (choose smallest legal integer > a_n) and periodicity of "legal" mod L
   — by construction of G and f. Conclude a_{n+T} = a_n + L for all n ≥ n_0.
6. **Extend periodicity back to n = 1:** the finitely many terms a_1,...,a_{n_0} are not
   automatically covered by step 5's conclusion (which only starts at n_0); note that
   eventual periodicity a_{n+T} = a_n + L for n ≥ n_0 is what the problem asks (T, L
   fixed positive integers with the identity holding "for every positive integer n" —
   re-read the problem statement: it demands the identity for EVERY n ≥ 1, not just
   eventually). **This is a second gap**: need to show the periodic pattern, run
   backwards, already started at n=1, i.e. that a_1,...,a_{n_0} sit inside the same
   cyclic pattern (or re-derive T,L so equality truly holds from n=1). Likely resolved
   by re-indexing: once the tail is periodic with step L over a window of size T, check
   by direct (finite) computation that the same T, L work from n=1 — this is a finite
   verification, not a new proof idea, but must be flagged.

### Key lemmas (claim + mechanism)
- **Free bound on Q = P(a_1)** — because gcd(a_n,a_1) > 1 holds definitionally for all
  n ≥ 2 (case i=1 of the recurrence's hypothesis).
- **Minimal-antichain transversal equivalence** — because a hitting set for the minimal
  elements of a family automatically hits every element (superset closure of "shares an
  element").
- **Finiteness of eventual prime support S (THE GAP)** — conjectured mechanism: a
  potential/monovariant on the antichain structure combined with a density argument
  ruling out infinitely many fresh-prime recruitments; not yet proven.
- **CRT reduction to residues mod L, then cyclic pigeonhole on finite good-residue set
  G** — because divisibility by primes in S depends only on residue mod L = ∏S, and a
  deterministic successor rule on a finite cyclic set is periodic with period |G| and
  step L.

### Open gaps
- Step 3 (finiteness of S) is NOT proved — this is the true crux of the whole problem;
  the antichain/monovariant framing organizes the claim but does not by itself supply
  the growth/density argument needed to rule out infinitely many prime recruitments.
- Step 6 (extending periodicity to hold from n=1, not just eventually) needs an explicit
  finite check/argument, not just an appeal to "eventually."

### Cases to cover
- Base case Q singleton (a_1 a prime power): S = Q = {p}, M = {{p}}, trivial — every
  term after a_1 is a multiple of p. Should reduce cleanly from the general lemma.
- General case |Q| ≥ 2: the genuinely hard case, where helper primes outside Q may be
  recruited (as seen with a_1=15 recruiting 2, or a_1=1001 recruiting 2 but not 3).

### Watch out for
- The antichain M_n can grow in *complexity* (more elements) even while individual
  elements shrink; don't conflate "M_n has bounded elements" with "M_n has bounded
  underlying prime support" — these are different finiteness claims and only the latter
  is what's needed.
- The problem's period T from the population's numerics (e.g. T=282 for a_1=1001) is
  NOT simply φ(L) or |G| computed naively as "multiples of any prime in S" — G is the
  set of residues hitting the *minimal* antichain M, a strict subset in general.
