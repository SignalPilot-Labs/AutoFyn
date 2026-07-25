## imo-2026-06

active-set-stabilization: new
Target: exist T, L with a_{n+T} = a_n + L for all n.
Technique: Two-phase structural proof — (1) prove the "active prime set"
S = {p : p | a_n for infinitely many n} is finite and nonempty via a
density/threshold argument (once primes already in play give a covering
density high enough, no fresh prime is ever competitive under the greedy
minimal-choice rule); (2) pigeonhole on a finite state (a_n mod L, coverage
window) to get eventual exact periodicity, then extend to a global (T,L)
covering the finite prefix too.
Skeleton:
  1. Basic facts: a_n strictly increasing; gcd(a_i,a_j) | a_j-a_i (KB: Divisor
     analysis).
  2. Define S = primes dividing infinitely many a_n.
  3. Lemma 1: S finite & nonempty, via density/threshold argument (crux gap).
  4. Lemma 2: gap bound g(S) finite once S fixed (Jacobsthal-style, CRT).
  5. Lemma 3: pigeonhole on finite state (a_n mod L, window-coverage) gives
     n1<n2 with equal state ⟹ shift-invariance ⟹ T=n2-n1, L=a_{n2}-a_{n1}.
  6. Extend to cover finite prefix via multiples of T.
Key lemmas:
  - S finite — because once covering density from S_n crosses a threshold, a
    smaller S-only candidate always beats any fresh-prime candidate under the
    greedy minimality rule.
  - Finite state ⟹ shift-invariance — because the greedy rule is a
    deterministic function of (residue mod L, coverage state).
Open gaps: Lemma 1 (S finite) is the central unproved gap — the threshold
argument and the induction showing it's reached in finite time are only
sketched. Lemma 3's precise state definition and the claim it's a pure
function of state also need work.
Cases to cover: a_1 prime-power (trivial collapse, T=1) vs a_1 multi-prime
(generic, real difficulty).
Watch out for: don't assume L = ∏S without proof; don't hand-wave state
finiteness before invoking pigeonhole.

growth-rate-contradiction: new
Target: same as above.
Technique: Direct quantitative counting/growth-rate contradiction (extremal
principle) attacking the S-finiteness lemma via an explicit inequality instead
of a density threshold — assume infinitely many fresh primes q_k are ever
recruited, derive that a_n must grow faster than a competing linear upper
bound from already-active small primes, contradiction.
Skeleton:
  1. Monotonicity + gcd-divides-difference (KB: Divisor analysis).
  2. Crude upper bound attempt via Bertrand's postulate (KB: Bertrand's
     postulate) — insufficient alone, motivates Lemma A.
  3. Lemma A: once some primes cover density ≥ threshold, a_{n+1}-a_n is
     bounded by a constant (not growing with n).
  4. Lemma B (key counting contradiction): if infinitely many fresh primes
     q_k → ∞ are each forced, each creates a gap ≥ ~q_k, so a_{n_k} grows at
     least like sum q_j; but Lemma A/step-2-style bound gives a_n = O(n);
     these contradict once made precise since q_j → ∞ forces
     super-linear growth.
  5. Conclude S finite from Lemma B; finish via the same pigeonhole-on-state
     machinery as active-set-stabilization's Lemma 3.
Key lemmas:
  - Fresh primes can't be recruited infinitely often — because each creates
    an unboundedly growing gap while a competing density argument caps a_n
    linearly in n.
  - Shared finish with active-set-stabilization (pigeonhole on state mod
    L=∏S).
Open gaps: Lemma A and Lemma B are only sketched; the inclusion-exclusion
counting estimate bounding window length vs. number of "bad" constraints from
earlier terms is not worked out. The a_n=O(n) base bound (step 2/3) needs its
own proof that two small primes become active quickly — overlaps with
active-set-stabilization's Lemma 1; if either nails this shared sub-lemma,
extract it to results/imo-2026-06/lemmas/.
Cases to cover: a_1 prime power (Lemma B vacuous) vs multi-prime a_1 (Lemma B
must bind).
Watch out for: gap ≥ q_k is a lower bound only, not equality; distinguish "q
divides a_{n+1}" from "q is the sole reason some specific earlier constraint
is satisfied" (need the right notion of load-bearing prime for the counting
argument).

state-compactness-pigeonhole: new
Target: same as above.
Technique: Compactness/pigeonhole on an EXPLICIT finite state space fixed a
priori (K primes, primorial L_0), without first isolating "the" active prime
set — a genuinely different architecture (state-first, S-second) from
active-set-stabilization (S-first, state-second). Finish borrows aimo-0680's
"divisibility forces a bounded difference to be exactly zero" trick.
Skeleton:
  1. Reformulate greedy rule as a sieve: Bad_n = integers excluded by some
     earlier term's coprimality.
  2. Lemma 1 (permanently-dead invariant): whether integer m is blocked by a_i
     never changes once a_i is fixed (R(a_i) fixed) — monotone one-way
     structure.
  3. Lemma 2: fix K, L_0 = primorial of first K primes; encode state v_n =
     (a_n mod L_0, which of first K primes have appeared, alive/dead status of
     each residue mod L_0) — finitely many possible values.
  4. Lemma 3: pigeonhole gives n1<n2 with v_{n1}=v_{n2}.
  5. Lemma 4 (crux gap): large prime factors (> P_K) of individual a_i's are
     eventually irrelevant — a density/sparseness argument, same core
     difficulty as the other approaches' S-finiteness lemma, just deferred.
  6. Finish: equal states ⟹ shift-invariance via divisibility-forces-equality
     induction (aimo-0680-style) ⟹ T=n2-n1, L=a_{n2}-a_{n1}.
Key lemmas:
  - Permanently-dead invariant — because R(a_i) is fixed forever once i is
    fixed.
  - Finite a priori state space — because K, L_0 are fixed constants.
  - Large primes eventually irrelevant (Lemma 4) — same crux as other
    approaches' S-finiteness lemma, sparse primes block a density-zero set of
    candidates.
Open gaps: Lemma 4 is exactly as hard as proving S stabilizes in the other
approaches — this framing doesn't avoid the hard lemma but makes the FINISH
rigorous independent of pinning down S exactly. Precise existence of
sufficient K is not shown (only that some K works, not computed).
Cases to cover: prime-power a_1 (trivial) vs multi-prime a_1 (needs Lemma 4).
Watch out for: state must not depend on unbounded history (truncate to primes
≤ P_K); "permanently dead" tracking must reduce to a single bit per residue,
not which specific a_i killed it.

jacobsthal-covering-bound: new
Target: same as above.
Technique: Explicit/constructive covering-system argument (Jacobsthal-function
style) via induction on "phases" of prime-set growth, aiming to construct L
explicitly (L = ∏ S) with a concrete self-sufficiency stopping criterion,
rather than a soft pigeonhole/density argument for S's finiteness. Falls back
to pigeonhole only for pinning T (which computational evidence shows is NOT a
function of S/L alone).
Skeleton:
  1. Define g(S) = max gap between consecutive integers divisible by some
     prime in S; g(S) ≤ min(S) always (crude bound).
  2. Phase induction: S_0 = prime factors of a_1; at each step either S_j is
     "self-sufficient" (g(S_j) beats any outside-prime alternative) or some
     earlier a_i forces a new prime into S_{j+1}.
  3. Lemma A: bound the number of phases (reduces to bounding either the size
     of recruited primes, shared with growth-rate-contradiction's Lemma B, or
     the phase count directly) — crux gap, not closed here.
  4. Once phases exhaust, L = ∏_{p∈S} p by CRT/self-sufficiency.
  5. T is NOT computable from S/L alone (confirmed by computational evidence:
     a_1=35 and a_1=105 share L=210 but T=34 vs T=58) — must be obtained via
     the pigeonhole-on-state finish (import from active-set-stabilization
     Lemma 3), using L as input.
Key lemmas:
  - g(S) finite for any finite S — trivial (≤ min(S)).
  - Self-sufficiency criterion — because greedy always picks smallest valid
    candidate, and S-covered candidates within g(S) beat any fresh-prime
    alternative once self-sufficient.
  - L = ∏_{p∈S} p — because once every term is divisible by some p∈S and S
    is exactly the infinitely-recurring primes, residues mod L determine
    membership by CRT.
Open gaps: Lemma A does not close on its own (same core difficulty as the
other approaches' S-finiteness lemma). T's closed-form construction attempt
fails per computational evidence and must fall back to pigeonhole.
Cases to cover: prime-power a_1 (0 phases) vs multi-prime a_1 (≥1 phase,
verify self-sufficiency criterion on small cases: 15, 35, 105).
Watch out for: don't conflate "S self-sufficient" with "every term divisible
by a prime in S" (needs a short separate argument); justify L = ∏S is exact
(not a proper multiple) by showing every prime in S is individually necessary
in the eventual cycle.

Notes for outline-reviewer: all four approaches converge on ONE genuinely hard
shared lemma — "only finitely many primes are ever load-bearing for the
greedy process" (equivalently: the active prime set stabilizes / no
infinite recruitment of fresh primes) — stated with different flavors
(density threshold in active-set-stabilization, quantitative counting in
growth-rate-contradiction, deferred-and-wrapped in state-compactness-pigeonhole,
phase-count in jacobsthal-covering-bound). This is expected and matches all
three explorers' independent convergence on this being THE hard step; it is
NOT a same-framing collapse, since the four approaches use genuinely different
mechanisms to attack it and different architectures for the finish (pure
pigeonhole vs. constructive phase induction vs. a priori fixed state space).
Recommend the build set include at least 2 of these (e.g.
active-set-stabilization + growth-rate-contradiction, or +
state-compactness-pigeonhole) to see which mechanism cracks the shared lemma
first; if one succeeds, its lemma should be extracted to
results/imo-2026-06/lemmas/ for the others to import (per CLAUDE.md's shared
lemma cache).
