## imo-2026-06 — lens: contradiction/obstruction via GREEDY REALIZABILITY (self-blocking)

- Distinct openings surfaced (all checked against forbidden-lever rules):
  1. **"Self-blocking as a fixed-point closure, not a statistic."** A is *not* built incrementally
     from a growing finite prefix — the certified no-transient lemma defines `A = {c : c meets every
     G ∈ 𝓐_∞}` once, from n=1, w.r.t. the *full* (possibly infinite) 𝓐_∞. This means "self-blocking"
     is really a global self-referential fixed-point condition (𝓐_∞ is exactly the ⊆-minimal-support
     family of the process that A itself generates). I looked for a genuinely new invariant living in
     this fixed-point structure (distinct from density/max-gap/spread) — did not find one; every
     concrete instantiation I could write down (interval-covering at formation time, recruit-order
     accounting, incremental-D_n modulus growth) reduces to either RBT/RBD (aggregate rejection budget,
     already certified-dead R6) or to the anchor-partition Collapse mechanism (already certified-dead
     R4) once you unpack it. Reported honestly as *not* a new lever, only a sharper restatement of why
     self-blocking is hard to leverage: its content is already fully absorbed into E1/E2(⇒)/E2(⇐)+R1.
  2. **Emergence-order / recursive-growth numeric probe** (see data table below): tracked, for each
     seed, the sequence of ⊆-minimal supports **in order of first realization** (= value order, since
     A is enumerated increasingly) and the ratio of the newly-introduced max prime q to the product
     D_prev of all primes seen in supports realized so far. Finding: q/D_prev is NOT bounded below by
     anything informative — it can be large at first recruitment (q/D_prev ≈ 5–11 for the very first
     new support) but collapses toward 0 for later recruitments once an anchor prime (e.g. 3 in
     a₁=9375, dividing a₁ itself) gets "locked in" as its own singleton minimal support {p*} (since
     (p*)^k ≥ a₁ eventually realizes {p*} itself, per the prime-power lock already in TAS). This
     confirms — numerically, on top of the existing R4 anchor-partition proof — that once an anchor
     prime p* dividing a₁ stabilizes as its own singleton support, essentially all subsequent large
     primes q recur ONLY paired with p* (companion set shrinks to {p*, q}), exactly the anchor-fiber
     picture already certified (Lemma A / TAS). No new invariant found here either — it's the same
     wall re-derived from the value-emergence angle instead of the term-index angle.
  3. **Re-examined the "exhaustion of the periodicity-without-Π-finite" argument (R6, item ii) for a
     loophole where witness primes themselves recur periodically.** Checked carefully: NO loophole.
     The key point (item 1 above) is that A is defined w.r.t. the TRUE FULL 𝓐_∞ from n=1, not built up
     over time — so "Π infinite" means infinitely many DISTINCT primes genuinely occur as members of
     minimal supports of A ITSELF (not of some transient finite-prefix approximation). If A were
     periodic mod a fixed K, membership in A would depend only on residues mod primes dividing K (a
     FINITE set). E3 (private witness) then produces, for any prime q∤K with q ∈ some G ∈ 𝓐_∞, two
     integers t≡t' (mod K) with F(t)∩F(t')={q} (or more precisely a private witness argument forcing
     q to be load-bearing for distinguishing membership) — since q∤K, t and t' agree on every residue
     that governs mod-K periodicity but must differ in A-membership status by construction of the
     private witness, a genuine contradiction. The idea that "the witnesses cycle back so only
     finitely many ever matter" cannot rescue periodicity: if Π is infinite, INFINITELY MANY distinct
     primes q are each, individually, load-bearing (each is the max of some minimal support, each has
     E3 private witnesses), and periodicity mod any FIXED K only has room for the finitely many primes
     dividing K. This is watertight; the exhaustion argument in R6 has no loophole from "recurring
     witnesses" — the witnesses are witnesses to DISTINCT primes q, not a single recurring pattern.
     CONFIRMS: route (ii) direct-periodicity-without-Π-finite remains certified-exhausted; do not
     reopen.

- Candidate technique(s): none new. Every self-blocking instantiation collapses onto RBT/RBD
  (rejection-budget dichotomy, R6) or Collapse/anchor-partition (R4) or JSC (R5). Self-blocking's
  full logical content for this problem is already captured by the certified E1 (Enumeration) + E2(⇒)
  (minimal supports are ⊆-minimal transversals) + E2(⇐)/R1 (realizability: G-supported m≥a₁ is a
  term) triple — there is no additional "greedy choice" leverage beyond what these three already give.
  This matches the R3 certified finding (§ "greedy minimality gives NO extra leverage over is-c-in-A
  once A is fixed") — my numeric/structural probes reproduce and reinforce that finding rather than
  refuting it.

- Cheap-kill candidates: none obvious beyond what's certified. Tried: (a) interval-covering at
  formation time (self-blocking ⇒ all integers strictly between consecutive terms are blocked by
  SOME earlier support) — this is exactly RBT's Φ_N identity, already certified and already shown to
  bound rate not count (RBD). (b) incremental-modulus ratio q_new/D_prev — numerically unbounded
  below (can be large at first recruitment), no cheap contradiction.

- Knowledge-base entries to use: none beyond what's already cited by the leader chain (Order of an
  element / Fermat-Euler periodicity entry, KB lines 65–66, already used for the endgame). No new KB
  entry surfaced as relevant to closing E5″ — this remains a bespoke combinatorial-number-theory gap
  not covered by a named generic KB technique.

- Analogous past problems (cruxes): none beyond the already-recorded aimo-0678 (two-stage monovariant,
  exhausted R3), aimo-0447 (realizer-value pincer, already fully mined R4), aimo-0648 (near-miss,
  window size a-priori given, R6), aimo-0421 (recursive dichotomy, vacuous, R5). I did not find a new
  corpus analog specific to "self-blocking realizability contradiction" — did not do a fresh corpus
  query this round (given the dispatch's numerical/structural focus and time budget); if the
  outliner wants a corpus sweep specifically for "greedy selection forces a finite generating set"
  shaped problems, that is untried but I could not fit it in this lens's time budget.

- Prior progress: whole theorem certified-equivalent to the single open arrow **E5″**: every
  ⊆-minimal support G with ∏G ≥ a₁ satisfies ∏(G∖{p_max}) < a₁. (See
  `results/imo-2026-06/lemmas/realizer-value-pincer.md`.) Nothing in this lens moves that gap.

- Dead ends (do not retry) — reconfirmed, not newly discovered:
  - Any lever bounding ∏G / p_max / |t−t'| via a₁-only spread (JSC, R5) — my emergence-order ratio
    probe independently reconfirms this is a dead angle (ratio collapses to 0 once anchor locks in,
    giving no usable UPPER bound direction).
  - Aggregate rejection-budget / disjoint per-recruit cost accounting (RBD, R6) — self-blocking's
    "interval covering" content is exactly this tautology; re-derived independently this round, forks
    identically.
  - Common-sub-support-realization / anchor-fiber collapse (R4 Collapse) — the emergence-order
    numerics for a₁=9375 (67 recurring only with the locked anchor 3) is a fresh numeric instance of
    exactly this certified mechanism.
  - Direct-periodicity-without-Π-finite (R6 route ii) — re-examined for a loophole (recurring witness
    primes), found none; certified-exhausted stands.

- Small-case / intuition notes (all labeled CONJECTURE/numeric-only, N capped per seed so possibly
  not fully converged per the standing convergence caveat):
  - Data table (max over ⊆-minimal supports found in a finite-prefix simulation; NOT proof, matches
    prior rounds' numerics):
    ```
    a1=375   (N=1500): #minsup=5,  max pmax=19,  max ∏G/a1=1.064
    a1=385   (N=1500): #minsup=7,  max pmax=19,  max ∏G/a1=1.086
    a1=867   (N=1500): #minsup=1,  max pmax=3,   max ∏G/a1=0.003
    a1=105   (N=1500): #minsup=4,  max pmax=7,   max ∏G/a1=1.000
    a1=9375  (N=800):  #minsup=5,  max pmax=67,  max ∏G/a1=0.500
    a1=15015 (N=800):  #minsup=73, max pmax=1249,max ∏G/a1=1.165
    a1=255255(N=800):  #minsup=482,max pmax=42953,max ∏G/a1=1.010
    ```
    Reconfirms (independently) the standing conjecture ∏G/a₁ stays close to 1 (≤~1.2) while p_max(G)
    itself is essentially unbounded relative to a₁ in absolute terms but always paired with small
    companions keeping the RADICAL near a₁ — i.e. the E5″ inequality's numeric signature is exactly
    what's already certified, no sharper pattern found. NOTE per standing rule (round 3 memory), the
    larger-a₁ seeds (15015, 255255) at N=800 are likely NOT fully converged (shallow-scan noise), so
    their #minsup/pmax lists include probably-transient entries; treat only the ∏G/a₁ ratio as
    corroborating (consistent with the converged seeds 375/385/105/867), not the raw counts.
  - Emergence-order probe (a₁=9375) is the one qualitatively new observation this round: once the
    anchor prime dividing a₁ (here 3) locks in as its own singleton minimal support, essentially every
    subsequently-recruited large prime q's minimal support is exactly {p*, q} (companion set doesn't
    grow) — a clean numeric picture of the anchor-fiber mechanism, but it is the SAME mechanism R4
    already proved forces a collapse to E5, not a new lever.

**Bottom line for this lens:** self-blocking's logical content for THIS problem is already fully
absorbed into the certified E1/E2/R1 apparatus; every concrete instantiation of "derive a contradiction
from realizability" that I could construct or probe numerically reduces to one of the three certified
negative guardrails (JSC, RBD, Collapse). I found no genuinely new invariant. The periodicity-exhaustion
argument (R6, route ii) was re-examined for the specific loophole requested (recurring witness primes)
and found watertight — no loophole. This lens does not open a new route; it reinforces that the
plateau is structural, consistent with all three prior explorers' route-family conclusions.
