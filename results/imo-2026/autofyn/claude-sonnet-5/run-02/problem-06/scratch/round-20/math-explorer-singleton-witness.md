## imo-2026-06 (lens: mechanisms for the Two-Sided Singleton Witness Theorem's
existence hypothesis, NOT via sieve/density)

### Distinct openings

1. **Constrained Singleton Coherence (new, numerically verified, structurally
   provable — the most promising lead found this pass).** Fix ANY witness
   `m_A` of type `A'` (need not itself be a singleton witness). By the
   certified **Confined-GCD Lemma** / **Double-Witness Nested Pigeonhole
   Lemma** machinery, pigeonholing `d(x):=\gcd(a_{m_A},a_x)` over
   `x\in X_{B'}` against the finite divisor set of `a_{m_A}` gives an
   infinite subset `X_{B'}^{(0)}` on which `d(x)=d^*` is constant, with every
   prime factor of `d^*` confined to `F'_{m_A}:=P(a_{m_A})\setminus S_0`
   (already certified content — this is exactly `lemmas/double-witness-
   nested-pigeonhole.md`'s first pass, or even the plainer `lemmas/confined-
   gcd-lemma.md`). **New observation, proved on the spot (elementary, not
   sieve-based) and checked computationally**: if `x\in X_{B'}^{(0)}` is
   itself a singleton-signature occurrence (`P(a_x)\setminus S_0=\{q_x\}`),
   then since `d^*\mid a_x` and `d^*`'s prime factors all lie outside `S_0`,
   `d^*` must be a **power of `q_x` alone** — i.e. `d^*` can have *at most
   one* distinct prime factor. Two immediate corollaries, both unconditional:
   (a) **if `d^*` has ≥2 distinct prime factors, ZERO elements of
   `X_{B'}^{(0)}` can be singleton** — a clean structural exclusion, pruning
   entire pigeonhole classes from ever containing a witness; (b) **if `d^*`
   is a prime power `q^k`, every singleton `x\in X_{B'}^{(0)}` (if any exist)
   has `q_x=q` — the same prime** — i.e. singleton occurrences, when they
   occur inside a given pigeonhole class, automatically COHERE onto one
   shared prime, with no search over "does side A's prime match side B's
   prime" needed. This directly narrows the Two-Sided Singleton Witness
   Theorem's existence hypothesis from "two independent matching-prime
   searches" to "does the (fixed, `m_A`-determined) prime-power pigeonhole
   class ever contain a singleton at all." **Verified numerically** on
   `a_1=4807`: (i) at the recruited core `S_0=\{2,3,5,11,19,23\}` with
   `m_A=6` (already singleton, `F'_{m_A}=\{17\}`) the pigeonholed `d^*=17`
   trivially, all 18 sampled singletons in `X_{B'}^{(0)}` have `q=17` —
   reproduces the known Singleton-Side-FAH-driven case, no new information
   here. (ii) At the **un-recruited** core `S_0=Q=\{11,19,23\}`, with a
   **genuinely non-singleton** witness `m_A=2` (`a_{m_A}=4818`,
   `F'_{m_A}=\{2,3,73\}`, three primes — NOT reducible to Singleton-Side FAH
   directly), the dominant pigeonhole class is `d^*=2` (1577/2406
   occurrences), prime; within it, 13 sampled occurrences are singleton, and
   **all 13 have `q=2`** exactly as predicted. A second, smaller class
   `d^*=6` (785/2406 occurrences, `d^*` composite, factors `{2,3}`) was
   checked and, exactly as predicted by the exclusion claim, contains
   **zero** singleton occurrences among all 785 sampled. Script:
   `/tmp/verify2.py` (also `/tmp/verify_singleton.py` for case (i)). This is
   a genuinely new, fully elementary, unconditional lemma (not sieve/density
   — pure gcd/pigeonhole, matching the dispatch's mandate to avoid the
   confirmed-dead sieve style) — **worth writing up and certifying**, though
   it does NOT by itself prove existence: it only shows (a) most pigeonhole
   mass may sit in classes that are structurally *excluded* from ever
   containing a witness, and (b) conditional on the *dominant* class being a
   prime power, singleton search is free (any singleton found there
   automatically gives a matching pair). The residual open question this
   opens is sharper and more concrete than the original: **is there always
   SOME `m_A` (over all witnesses of `A'`, not just one fixed choice) whose
   dominant/majority pigeonhole class `d^*(m_A)` is a prime power?** This is
   a finite combinatorial question about a specific fixed integer's divisor
   lattice (`\mathrm{Div}(a_{m_A})`), not a density question about an
   infinite index set — it may be far more tractable than the original sieve
   target, though this pass did not attempt to resolve it (would require
   either an inductive/exchange argument over the choice of `m_A`, or a
   further structural fact about which divisors of `a_{m_A}` the recursion's
   minimality rule favors — untried here).

2. **Recursive/inductive pigeonhole via core-enlargement — checked, appears
   to collapse into the crux itself, not a bypass.** The natural idea: take
   the Generalized Bounded Witness Lemma's Corollary output (some prime
   `q\in F'_{A',B'}` divides infinitely many `A'`-occurrences), enlarge
   `S_0` to `S_1:=S_0\cup(F'_{A',B'}\setminus\{q\})`, and hope the *new*
   outside-core factor sets shrink toward singleton under re-application.
   Traced this through: enlarging the core this way is *exactly* the
   Finite-Core-Theorem-style recruitment step already in the certified
   toolkit, and whether it terminates in a state where every witness is a
   true singleton is *exactly* H1/H2's own open content (a same-shape
   restatement, structurally identical to round 12's independently-certified
   finding that EEA — a different reformulation attempt — reduces to the
   same wall via `lemmas/confined-gcd-lemma.md`). **Do not re-attempt this in
   isolation** — it is very likely a disguised restatement, exactly the
   pattern flagged by 20+ prior dead mechanisms in `current.md`. Flagging
   this now so the outliner does not spend a round re-discovering it.

3. **Weaker "infinitely often" existence — checked, does NOT suffice on its
   own, but the search above (opening 1) shows why the *pigeonhole class
   structure* matters more than the raw "infinitely often" count.** The
   round-19 approach already tried "infinitely often" as a first goal and
   hit the sieve obstruction because it tried to prove `\omega(w_n)=1`
   infinitely often directly via density. Opening 1 reframes this: instead
   of asking "is `w_n` prime infinitely often" (needs density over an
   implicit sequence — confirmed dead, §5.3 of the approach file), ask "is
   there SOME witness `m_A` whose *induced pigeonhole class* is a prime
   power" (a question about one fixed integer's divisor structure, not an
   infinite density statement) — this reframing is the main new terrain
   found this pass.

### Candidate technique(s)
- Pure elementary gcd/pigeonhole exchange arguments (Confined-GCD Lemma,
  Double-Witness Nested Pigeonhole, Divisor-Restricted Pigeonhole), NOT
  sieve/density — matches the dispatch's mandate.
- Possibly an extremal/exchange argument over the *choice* of witness `m_A`
  (varying which occurrence of `A'` is used as the fixed witness in the
  pigeonhole, to try to force the induced `d^*(m_A)` to be a prime power for
  at least one choice) — untried, flagged as the sharpest concrete open
  sub-question from this pass.
- Critical Prime Dichotomy Lemma (`lemmas/critical-prime-dichotomy.md`) —
  gives a genuine necessary condition on any outside-core prime dividing a
  witness (either stripping it drops below the previous term, or it's the
  sole rescuer of some earlier index's legality). This has NOT yet been
  combined with the Constrained Singleton Coherence finding above; branch
  (b) of that dichotomy (`q'` is the sole rescuer, i.e. `P(a_i)\cap
  P(a_n)=\{q'\}` for some `i<n`) produces a DIFFERENT kind of singleton-like
  fact (a singleton *intersection* with a specific earlier term, not a
  singleton outside-core factor set) that is worth exploring as an
  alternative route to a matching-witness argument, but was not developed
  further this pass (time-boxed).

### Cheap-kill candidates
- The composite-`d^*`-exclusion half of Constrained Singleton Coherence
  (opening 1(a)) is itself a cheap structural pruning step: before searching
  a pigeonhole class for singleton witnesses, check whether `d^*` (or `D^*`
  from Divisor-Restricted Pigeonhole) is a prime power; if not, skip that
  class entirely — provably no witness lives there. Cheap and rigorous.

### Knowledge-base entries to use
- `lemmas/confined-gcd-lemma.md`, `lemmas/double-witness-nested-pigeonhole.md`,
  `lemmas/divisor-restricted-pigeonhole.md`, `lemmas/generalized-bounded-
  witness-lemma.md`, `lemmas/singleton-side-fah.md`,
  `lemmas/two-sided-singleton-witness-theorem.md`,
  `lemmas/critical-prime-dichotomy.md`, `lemmas/elementary-omega-bound.md`
  (bounds `|F'_{m_A}|`, hence the divisor lattice size, to `O(\log n)`,
  making the "search over witnesses `m_A` for a prime-power pigeonhole
  class" finite-and-small at each fixed `m_A`, though still infinite over
  the choice of `m_A`).
- `knowledge_base.md`'s generic pigeonhole/extremal-principle entry (already
  the basis of all of the above certified lemmas).

### Analogous past problems (cruxes)
Not re-run this pass in full (round 19's explorer already searched
`knowledge_base.md` and the crux corpus for sieve/density tools applicable
to an implicitly/adaptively-defined sequence and reported empty — confirmed
plausible on a scan of the subtopics index, which lists only generic
`pigeonhole`, `p-adic-valuation`, `modular-arithmetic-and-CRT`,
`zsigmondy-and-primitive-divisors` as number-theory subtopics relevant to
greedy/recursive sequences, none of which include a crux move for
"adaptively-defined index sets with no closed form"). None found genuinely
analogous to the specific existence-hypothesis question here; no forced
match reported.

### Prior progress
See `results/imo-2026-06/approaches/triangle-consistency-pigeonhole.md` §1–5:
Double-Witness Nested Pigeonhole Lemma, Same-Type Triangle Vacuity, Two-Sided
Singleton Witness Theorem, elementary `ω(a_n)=O(\log n)` bound — all
certified. The existence hypothesis of the Two-Sided Singleton Witness
Theorem remains the sharpest open residual.

### Dead ends (do not retry)
- Sieve/Selberg/Brun/Erdős–Kac density arguments on `X_A`/`w_n` — confirmed
  structurally inapplicable (round 19, §5.3): no closed form, no
  independent local-density control, adaptively/path-dependently defined.
- The outline's original triangle mechanism (`e:=\gcd(a_{m_A},a_{m_A'})`
  for two same-type witnesses) — proved vacuous (Same-Type Free-Facts
  Vacuity / Same-Type Triangle Vacuity, round 18, §2 of the approach file):
  carries no outside-core information beyond what the shared type's own
  in-core primes already force.
- Naive core-enlargement recursion as a "bypass" of FAH (opening 2 above) —
  traced through this pass and found to structurally collapse into the same
  crux (matches round 12's independently-certified EEA finding). Not a new
  mechanism; do not re-propose as if it were a fresh route.

### Small-case / intuition notes (conjecture, not proof)
- On both known hard rogue-pair seeds (`a_1=4807`, `a_1=11305`), the
  pigeonhole class induced by a well-chosen witness (in particular, the
  canonical/earliest witness, which happens to already be singleton on one
  side in both known seeds) IS a prime power, and singleton witnesses
  observed within it always match its prime — consistent with, but not
  proof of, the conjecture that "some witness's induced pigeonhole class is
  always a prime power." No seed tested (here or in prior rounds) exhibits a
  case where the *only* available pigeonhole classes are all composite.
  This conjecture, if provable, would be a strictly more concrete and
  more tractable (finite, single-integer-divisor-lattice) target than the
  original existence hypothesis, and avoids sieve/density entirely — flagged
  as the most promising concrete next step for the outliner to consider,
  while being explicit that it is NOT yet reduced to something proven, and
  that even if proved it would only give "a prime power pigeonhole class
  exists," not automatically "a singleton witness exists within it" (opening
  1 only shows singletons, if any exist in a prime-power class, cohere —
  existence within that class is still open, though now a narrower
  sub-question).
