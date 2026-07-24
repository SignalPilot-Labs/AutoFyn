## imo-2026-06 (fresh whole-problem framing lens, round 14)

- **Distinct openings surfaced** (each examined and diagnosed, none survives as a
  genuine bypass of the existence-vs-identity wall — reported honestly per the
  dispatch instructions):

  1. **Generating-function / transfer-operator framing.** Encode the sequence via
     A(x) = Σ x^{a_n}; eventual gap-periodicity ⟺ A(x) eventually matches a rational
     function with denominator (1 − x^L) (up to a polynomial remainder for the
     transient). This is literally a restatement of Lemma A (Gap-Periodicity
     Equivalence, already certified `lemmas/gap-periodicity-equivalence.md`) in
     analytic vocabulary — no new leverage: proving "eventually rational" still
     needs a deterministic finite-state recursion on the coefficients, which is
     exactly the automaton/EEA framing already shown (round 11's automaton lens,
     round 12's Theorem C) to be equivalent-difficulty to FAH. Not a new opening.

  2. **Direct p-adic valuation tracking, v_p(a_n) as a sequence per p ∈ S₀.**
     Considered whether tracking the vector (v_p(a_n))_{p∈S₀} directly (rather than
     just the Boolean "does p divide a_n" used by the existing extended-type
     machinery) gives extra leverage — e.g. via a Legendre-formula/LTE-style
     argument forcing monotonicity or eventual stabilization of some v_p. Checked
     concretely: the greedy legality rule (`gcd(c,a_i)>1`) is completely insensitive
     to any exponent, only to whether a prime divides at all — so refining the
     Boolean state to a valuation-vector state adds strictly more bookkeeping with
     zero new constraining information about which candidate gets chosen. This
     collapses back to the same automaton-shaped wall, now with a larger (still
     finite, still not provably deterministic) state space. Not a new opening —
     confirmed by direct inspection of the legality predicate, not just prior-round
     citation.

  3. **Van der Waerden / direct 2-coloring finite-Ramsey argument on residues.**
     Color integers mod L by extended type (finite coloring since S₀ is finite);
     ask whether van der Waerden's theorem (or a direct finite-coloring pigeonhole)
     forces something about which color class a_n's value falls in. This is
     structurally the same shape as round 13's Central-Sets/idempotent-ultrafilter
     attempt (RETHINK'd pre-build, confirmed dead: "some cell of a finite partition
     recurs" is not "the SPECIFIC target cell recurs"). vdW gives arbitrarily long
     monochromatic APs in SOME color, never pins the color to the one FAH needs.
     Same wall, different Ramsey vocabulary — do not re-propose.

  4. **Induction on ω(a_1) via reduction to rad(a_1) (squarefree seed), distinct
     from the two dead seed-coupling attempts (round 8: single-prime removal,
     falsified; round 12: aggregate/set-level Base-Type Correspondence, falsified).**
     This is the angle the dispatch specifically asked me to probe: since the
     legality predicate `gcd(c,a_i)>1` depends only on the RADICAL (prime support)
     of each term, not on multiplicities, one might hope a_1 and rad(a_1) generate
     "qualitatively" the same eventual dynamics, reducing the general case to
     squarefree a_1 and disposing of exponents as a separate, easier bookkeeping
     layer. I checked this directly: a_1 = 105 = 3·5·7 (squarefree) vs
     a_1 = 315 = 3²·5·7 (same radical) — confirmed by fresh simulation (see below)
     that their greedy trajectories diverge from the very first few terms (105 →
     108,110,112,... recruiting 2 immediately at a_2=108=2²·27; 315 → 318,320,...
     also recruiting 2 immediately but at different residues), and — per the
     workspace's existing Rule (round 12, calibration note) — a_1 = 315 fails to
     stabilize even within 15,000 sampled terms while a_1 = 105 stabilizes at
     T=58 within ~1000 terms. This is not just slower convergence to the SAME
     answer; it means the finite core S recruited, and possibly the eventual L
     itself, are exponent-sensitive, not purely radical-sensitive. So "reduce to
     rad(a_1)" is not sound as a value-preserving reduction — the multiplicities
     genuinely participate in determining WHICH primes get recruited into the
     core (an identity-level fact, not just magnitude), so this reduction does not
     evade the wall; it would need its own separate proof that periodicity
     transfers between a_1 and rad(a_1), which is at least as hard as the direct
     problem and has no obvious handle. I flag this as a checked-and-rejected
     opening, not an untested one — do not re-dispatch without a concrete
     mechanism for coupling the exponent-1 and general cases.

  5. **Crux-corpus check (this lens): p-adic-valuation subtopic (57 cruxes,
     number_theory) and processes-and-algorithms subtopic (48 cruxes,
     combinatorics)**, specifically hunting for a "greedy process forced into
     eventual periodicity via valuation/bit-structure" analog not yet cited in
     current.md. Found `aimo-0964` ("force a periodic orbit by choosing size one
     larger than a self-terminating one so a reflecting boundary bounces state
     back into a cycle skipping the trivial state") as a superficially interesting
     "reflecting-boundary-forces-cycle" idea, but its mechanism is specific to a
     bounded discrete dynamical system with a hard reflecting wall (not present
     here — our state space via S₀ is finite only CONDITIONAL on FAH, which is
     exactly the open point) — not a transplantable technique. No p-adic-valuation
     crux in the 57 scanned matches this problem's shape (all rely on an explicit
     algebraic recurrence or equation to extract valuations from, which this
     problem's existential/minimality-defined a_{n+1} does not have — consistent
     with round 10's confirmed disanalogy for the whole "algebraic-recurrence
     induction" family). Confirms no new corpus match beyond what's already
     documented in the workspace's Rules (round 10 rule 27, round 8/9 rules on
     aimo-0477/aimo-0680/aimo-0016).

- **Candidate technique(s):** none pass the "supplies IDENTITY-level, not just
  existence/magnitude-level, information about an arbitrary intermediate term's
  factorization" bar that 15 prior mechanisms have failed on. This round's honest
  finding: I could not find a 16th distinct mechanism that dodges this wall.

- **Cheap-kill candidates:** none new. (The exponent-sensitivity finding in opening
  4 is itself a cheap structural fact worth recording as a negative constraint —
  it rules out one entire reduction strategy cheaply, before any heavy build.)

- **Knowledge-base entries to use:** no new entries beyond what's already in the
  certified lemma stack (Free Facts, Bounded Gap Lemma / Generalized Bounded Gap
  Lemma, Persistent-Type Pigeonhole, Finite Core Theorem, Generalized Bounded
  Witness Lemma, Extended Persistent-Type Pigeonhole, Confined-GCD Lemma, No-Restart
  Lemma, Gap-Periodicity Equivalence / Lemma A, Right-Extension Determinism /
  Lemma B, EEA-implies-periodicity / Theorem C). `knowledge_base.md`'s generic
  entries on pigeonhole/CRT/finite automata are all already in use; nothing in it
  supplies an identity-pinning tool this workspace hasn't already tried.

- **Analogous past problems (cruxes):** none newly found this round that are
  genuinely analogous beyond what's already cited in current.md's Rules (aimo-0514,
  aimo-0477, aimo-0680, aimo-0016, aimo-0030). `aimo-0964`'s reflecting-boundary
  cycle-forcing idea was checked and rejected as non-transplantable (see opening 5).

- **Prior progress:** unchanged from round 13 — FAH/Symmetric FAH (equivalently
  Cofinite FAH / EEA) is the sole open crux, 15 mechanisms confirmed dead, No-Restart
  Lemma certified (round 13), Self-Absorbing Core Theorem's conclusion correct but its
  written proof has an identified repairable gap in the "combining both parts" step
  (round 13, fix path already specified in current.md — a live, concrete, in-progress
  target independent of this round's fresh-framing search).

- **Dead ends (do not retry):** all 15 previously-confirmed-dead mechanisms (see
  current.md Rules, rounds 6-13) — pigeonhole/dichotomy, exchange/minimality,
  CRT-glue/competitor-construction (all moduli, round 11's Minimal-Modulus
  Generalization), sieve/density (round 11's Density-Argument Vacuity Corollary),
  automaton/graph-walk (round 11), Central-Sets/idempotent-ultrafilter (round 13),
  Morse-Hedlund/subword-complexity as a bypass (round 12, equivalent-difficulty not
  easier). This round adds, as newly-checked-and-rejected (not previously
  explicitly ruled out in this exact form): generating-function/transfer-operator
  framing (collapses to automaton=FAH), direct valuation-vector state refinement
  (adds bookkeeping, zero new constraint, same wall), van der Waerden/direct
  finite-coloring Ramsey (same "some cell not the target cell" wall as Central Sets),
  and rad(a_1)-reduction induction on ω(a_1) (exponent-sensitive core recruitment
  makes the reduction unsound, confirmed numerically on a_1=105 vs 315).

- **Small-case / intuition notes (conjectural, not proof):** fresh simulation this
  round (`sympy` gcd/factorint greedy loop) reconfirms a_1=105 and a_1=315 — same
  radical {3,5,7}, different exponent on 3 — diverge from their very first
  recruited term (a_2 = 108 = 2²·3³ for 105; a_2 = 318 = 2·3·53 for 315), consistent
  with the workspace's standing round-12 finding that 315 has a much longer
  transient. This is evidence (not proof) that the eventual core S / period L is a
  function of a_1's full factorization (including exponents), not just its radical —
  strengthens the case against any rad(a_1)-based reduction strategy without
  claiming a general theorem.
