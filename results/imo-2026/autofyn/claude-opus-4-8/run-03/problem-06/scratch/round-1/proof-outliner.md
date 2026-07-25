## imo-2026-06

Round 1 — opening the initial field. No prior approaches. Three rival attempts, each a complete
end-to-end attempt at the actual claim (∃ T,L: a_{n+T}=a_n+L ∀n≥1). All share two RIGOROUS, provable
free lemmas (verified numerically this round); the real difficulty is periodicity, attacked by three
genuinely different mechanisms.

SHARED FREE LEMMAS (rigorous, no gap — seed all three):
- Anchor: the i=1 clause holds for all n ⇒ every term is divisible by a prime of P=primes(a_1); so
  spf(a_n) ≤ P_max := max P for all n.
- Gap/Primorial: M := ∏_{p≤P_max} p; every multiple of M is admissible (each a_i has spf ≤ P_max | M),
  so a_{n+1}−a_n ≤ M. Verified: max gap ≤ M for a_1∈{15,35,77,105,143}.
NEW THIS ROUND (empirical, drives the design): (1) large primes (>P_max) NEVER change the greedy minimum
(0 counterexamples over 7 seeds × 400 terms); (2) periodicity holds from n=1 in every tested case, with
L a product of recruited primes dividing M. So the gap bound is EASY; the crux is periodicity + taming
large-prime history + no transient.

---

prime-support-reduction: new
File: results/imo-2026-06/approaches/prime-support-reduction.md
Target: ∃ T,L with a_{n+T}=a_n+L for all n≥1.
Technique: reduce to a STATIC finite transversal problem on primes ≤ P_max; finite constraint family ⇒
  greedy successor is a function of a_n mod M ⇒ pigeonhole eventual periodicity ⇒ bijection upgrade.
Skeleton: Anchor → Gap≤M → [CRUX] Reduction Lemma (replace "gcd>1" by "shares a prime ≤ P_max") →
  constraint family {T(a_i)}⊆2^{primes≤P_max} stabilizes → g:Z/MZ→Z/MZ transition → eventual periodicity
  → [CRUX-2] no-transient upgrade to all n.
Key lemmas: Reduction — the minimal admissible successor is always "small-admissible" (never needs a
  large prime); because the primorial competitor bounds the search and greedy minimality forces small
  coverage. Finite family stabilizes — finite lattice + monotonicity.
Crux gap: GAP-3 Reduction Lemma (large primes irrelevant); secondary GAP-7 no-transient upgrade.
Cases: single-prime collapse (T=1,L=p); multi-prime recruited (105→210, 15→30); must not assume 2 recruited.
Watch out: L ≠ ∏P and ≠ spf(a_1); "all n" needs the bijection step, eventual periodicity is not enough.

bounded-gap-finite-memory: new
File: results/imo-2026-06/approaches/bounded-gap-finite-memory.md
Target: same claim, end to end.
Technique: dynamical-systems / bounded-MEMORY. Gap bound free; show only the last W(a_1) terms matter ⇒
  finite state machine s_n→s_{n+1}=Φ(s_n); then Φ INJECTIVE (reversible) ⇒ pure periodicity from n=1
  (aimo-0577 bijection transplant). Tames large primes by "each old constraint is refreshed by a recent one."
Skeleton: Anchor+Gap → [CRUX] Finite-memory Lemma (window W bounded) → finite state (a_n mod M, recent
  supports, recent gaps) → Φ deterministic ⇒ eventual periodicity → [CRUX-2] reversibility ⇒ all n.
Key lemmas: Finite-memory — old constraints dominated/refreshed by recent terms within bounded distance
  (finite coverage-types + gap bound). Reversibility — greedy machine invertible on its recurrent set ⇒
  finite-set injection is a bijection ⇒ no transient.
Crux gap: GAP-2 Finite-memory (bound W independent of n); headline GAP-5 reversibility ⇒ all n.
Cases: single-prime (W≈1); multi-prime orbits (105→58, 15→8, 35→34) — W uniform, Φ injective.
Watch out: W must be n-independent (else circular); state rich enough to reconstruct predecessor.

covering-ap-union: new
File: results/imo-2026-06/approaches/covering-ap-union.md
Target: same claim, end to end.
Technique: extremal-COUNTING + explicit CONSTRUCTION (orthogonal to the two dynamical routes). aimo-0447
  witnessing-prime pigeonhole bounds critical primes ⇒ no prime > P_max is ever the unique witness; then
  GUESS-AND-VERIFY: exhibit the eventual admissible set as an explicit union of APs mod M and prove greedy
  = its increasing enumeration by strong induction. Periodicity is built and verified, not pigeonholed.
Skeleton: Anchor+Gap (⇒ a_n=Θ(n)) → [CRUX-A] witnessing-prime count ⇒ coverage only via primes ≤ P_max →
  support family stabilizes ⇒ admissible set = fixed residue union U mod M → [CRUX-B] greedy = enumeration
  of U (strong induction) ⇒ explicit (T,L) → [CRUX-C] extend match to n=1.
Key lemmas: No large critical prime — a q>P_max is never the sole witness because the primorial competitor
  covers via small primes at bounded cost (aimo-0447 assignment + ⌈N/p⌉ interval-divisor count). Greedy =
  enumeration of U — least admissible integer above a_n IS least element of U above a_n once U fixed.
Crux gap: GAP-A no large critical prime (pure counting); GAP-B strong-induction verification; GAP-C n=1.
Cases: single-AP U (T=1); multi-class U (105→58 residues, 35→34) — construction must PRODUCE the actual U.
Watch out: a_n=Θ(n) must be gap-lemma-derived (non-circular); Jacobsthal/covering bound re-proved not cited.

---

SHARED-WALL NOTE (for the reviewer / next round): all three ultimately must tame large-prime (>P_max)
history — the deep crux of the problem. They attack it by three genuinely different mechanisms: a static
REDUCTION lemma (approach 1), a bounded-MEMORY state machine (approach 2), and an extremal COUNTING bound
(approach 3); and the "all n / no transient" endgame differs too (g-bijection vs Φ-reversibility vs
constructive enumeration). This is honest diversity of mechanism, but if all three stall on "large primes
irrelevant/never-critical," next round should push a 4th framing even further out (e.g. a direct
minimal-counterexample on the first step where periodicity-from-n=1 would fail, or an averaging/growth-rate
argument on ∑1/q over primes q dividing terms). Build set should include all three so the reviewer can rank
which mechanism for the shared crux is most tractable.

build set: prime-support-reduction, bounded-gap-finite-memory, covering-ap-union
