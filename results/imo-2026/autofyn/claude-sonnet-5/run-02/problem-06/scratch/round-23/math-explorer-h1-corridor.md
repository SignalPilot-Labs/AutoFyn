## imo-2026-06 (H1/FAH corridor-hunt lens, round 23)

- **Distinct openings checked this round (all against the full 30+ dead-mechanism
  list in `/tmp/memory/math-explorer.md` and `current.md`'s round-by-round
  history before proposing):**
  1. **Dirichlet's theorem on primes in APs** (used constructively to *force*
     recruitment of a specific new prime into a core) — checked against the
     certified **Selection-Rule Class-Blindness** / **Ambient-Statistic
     Obstruction** finding (rules 7, current.md round 19-20): the obstruction
     is not "not enough primes exist," it's that the greedy legality rule only
     ever consults the Boolean predicate `gcd(c,a_i)>1`, never *which* prime
     realizes it. Dirichlet supplies existence of primes in a residue class;
     it says nothing about which of several already-available legal primes the
     *deterministic* greedy process will actually recruit at a given step.
     Orthogonal to the actual obstruction — not a new corridor, not proposed
     further.
  2. **Zsigmondy / primitive-divisor theorems** (crux subtopic
     `zsigmondy-and-primitive-divisors`, e.g. `aimo-0611`) — these need an
     explicit exponential/multiplicative recurrence (`a_{n+1}=f(a_n)` with
     growth like `x^n`) to produce a "term exceeds product of all earlier
     terms" argument. This problem's recursion is existential/greedy
     (`a_{n+1}` = smallest legal integer, additive not multiplicative growth,
     `a_n ~ a_1 + O(n)` by the certified Bounded Gap Lemma) — Zsigmondy's
     structural precondition is absent, same disanalogy already recorded for
     the whole "algebraic-recurrence induction" family (rule 12). Dead on
     arrival, not pursued.
  3. **`processes-and-algorithms` crux subtopic (combinatorics)** — scanned
     for a "greedy fill / charge against surplus" template (e.g. `aimo-0012`'s
     amortized charge against a per-part capacity surplus). This is
     structurally the same shape as the already-built and killed
     `amortized-charging-budget` approach (round 1) and the certified
     Escape-Cost Vacuity / Sandwich Genericity Theorems (round 10) that show
     ANY class-blind cost/charge statistic built from the recursion's own
     legality Boolean is provably uninformative about *which* prime
     eventually wins. No genuinely new instantiation found.
  4. **Keyword sweep of the full 2434-crux corpus** for "greedy", "periodic",
     "absorb", "covering system", "eventual" (183 hits) — cross-checked every
     number_theory hit against current.md's citation history. The only
     structurally close matches (`aimo-0477`, `aimo-0678`, `aimo-0680`,
     `aimo-0682`, `aimo-0016`, `aimo-0051`, `aimo-0421`) were **already
     imported in rounds 7–10 and 18** and are recorded dead/exhausted (rules
     9, 11, 12, 18). No unmined close analog remains in the corpus for this
     exact problem shape (existential/greedy selection + eventual arithmetic
     periodicity).

- **Candidate technique(s):** none new found. The corridor genuinely appears
  exhausted for *generic, top-down* H1/FAH mechanisms — every classical
  proof-technique family in the knowledge base and crux corpus (pigeonhole,
  CRT/sieve, density/second-moment/Borel–Cantelli, finite-Fourier/character
  sums, generating functions, LP-duality, Ramsey/idempotent-ultrafilters,
  nonstandard analysis/model theory, transfer-operator/spectral,
  o-minimality, computability/priority arguments, Kolmogorov complexity,
  martingale/renewal, Rauzy graphs/return-words, coding theory,
  combinatorial-game theory, extremal graph theory, additive-combinatorics/
  Schur, Morse-Hedlund/subword-complexity, orbit-merging/offset-dichotomy,
  Dirichlet-in-APs, Zsigmondy, amortized-charging/processes-and-algorithms)
  has now been tried and killed at the same underlying wall: the certified
  **Ambient-Statistic Obstruction** — any statistic that doesn't read the
  *realized*, path-dependent occupancy/legality history of the specific
  sequence is provably powerless to distinguish which prime the greedy rule
  will lock onto (existential-to-universal / class-blind-to-class-sensitive
  promotion gap).

- **Cheap-kill candidates:** none obvious beyond what's already certified
  (Selection-Rule Class-Blindness, Ambient-Statistic Obstruction, Universal
  Branch-(a) Dominance Theorem all already serve as pre-screens — any new
  H1 proposal should be run through these three before build).

- **Knowledge-base entries to use:** none new surfaced; the workspace's own
  certified lemma library (`lemmas/ambient-statistic-obstruction.md`,
  `lemmas/two-sided-singleton-witness-theorem.md`,
  `lemmas/self-absorbing-core-theorem.md`) remains the relevant toolkit for
  H1, plus the generic KB entries already cited in prior rounds
  (pigeonhole/CRT under "General Proof Methods", invariants/monovariants).

- **Analogous past problems (cruxes):** none genuinely new. The closest
  matches in the corpus (`aimo-0477`, `aimo-0678`, `aimo-0680`, `aimo-0682`,
  `aimo-0016`, `aimo-0051`, `aimo-0421`) are all already transplanted and
  dead per rules 9, 11, 12, 18 in `/tmp/memory/math-explorer.md`. Recommend
  none for this round's build.

- **Prior progress:** H1/FAH is the 17-consecutive-round plateau (rounds
  6–22) on the general claim; the workspace's real forward progress has come
  entirely from **bespoke subfamily theorems that sidestep H1 by direct
  induction reading realized occupancy data at each step**, not from a
  general FAH mechanism: `2|a_1` (APPROVE, round 16), `a_1=p^k` (APPROVE,
  round 18), `a_1=3q` for prime `q≥7,q≠5` (APPROVE, round 22). This is a
  real pattern: every genuinely successful attack in 22 rounds has been an
  ad hoc small-`|Q|` induction, never a general-mechanism promotion.

- **Dead ends (do not retry):** the full list is already exhaustively
  recorded in `/tmp/memory/math-explorer.md` rules 1–31 and in
  `results/imo-2026-06/current.md`'s round histories (30+ named mechanisms
  across 7 prior dedicated fresh-framing sweeps, rounds 8,9,10,11,13,15,17,
  19,20,22). This round adds 4 more explicitly-checked-and-rejected
  candidates (Dirichlet-in-APs, Zsigmondy, amortized-charging/
  processes-and-algorithms crux template, full corpus keyword sweep) to that
  list — record these as dead-on-arrival too so future rounds don't
  re-propose them.

- **Small-case / intuition notes:** no new numerics run this round (no new
  mechanism reached the point of needing a computational check). The
  standing computational record (12/12 FAH seeds with no counterexample
  through round 22, exact periods known for several) is unchanged and still
  only conjectural support for FAH, not proof.

- **Explicit recommendation:** **do NOT dispatch another generic/top-down H1
  mechanism-hunt this round.** This is the 8th dedicated fresh-framing sweep
  (after rounds 8,9(partial),11,13,15,17,19,20,22) to return empty, and this
  round additionally confirms via direct corpus/technique-family cross-check
  that the remaining unmined KB/crux territory (Zsigmondy,
  Dirichlet-density-style constructive arguments, processes-and-algorithms
  greedy-charge templates) is either structurally inapplicable or a
  disguised instance of an already-certified dead pattern. The productive
  use of this round's outliner/builder slots is almost certainly to **extend
  the bespoke-subfamily-induction track** (the only technique family with 3
  APPROVEs in 22 rounds) — e.g. `a_1 = p*q` for small fixed `p` (the 3q
  success pattern suggests fixing a *small* prime factor, not a general
  `p*q` with both free, which round 19 already refuted), or `a_1 = 3^k*q`,
  or tightening/finishing the still-open Case-(b) Jacobsthal-style gap
  pattern for a 4th subfamily — rather than a 9th generic H1 sweep.
