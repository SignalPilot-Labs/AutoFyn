## imo-2026-06 — round 19 outline review

Context checked: `results/imo-2026-06/current.md` (rounds 1–18, 19+ confirmed-dead
FAH mechanisms, refuted a_1=p·q "clean threshold" family, exhausted H2
counting/pigeonhole corridor), `results/imo-2026-06/approaches/{n1-periodicity-
reconciliation,triangle-consistency-pigeonhole,core-growth-monotonicity,
self-absorbing-by-construction}.md`, `approaches/.ranking.json`, and all three
round-19 math-explorer reports. All four outline claims were cross-checked
against the source explorer reports and found to accurately reflect them (no
fabricated evidence, no silently-dropped caveat).

---

### 1. n1-periodicity-reconciliation (revise) — APPROVE

- Step 1 is pure citation of the already-certified Master Conditional Theorem
  chain — no new risk.
- Step 2's **Generalized Class-Blindness Obstruction** is a genuine strict
  generalization of the certified Density-Argument Vacuity Corollary /
  Selection-Rule Class-Blindness finding, and its mechanism ("a function of a
  Boolean-outcome window carries no finer information than that window") is
  sound and matches exactly what `math-explorer-fresh-framing.md` independently
  derived (item 3/4: second-moment, Borel–Cantelli, and finite-Fourier/
  character-sum methods all reduce to the same class-blind statistic). This is
  a real, citable strengthening — worth certifying, not just a relabeling.
- Step 3/4 (write-up of the two solved subfamilies, honest "still conditional"
  framing) is bookkeeping — low risk, valuable for the run's floor deliverable.
- No overclaim risk: the outline explicitly instructs the builder not to let
  the write-up imply Status is more than `partial`.

Verdict: **APPROVE**.

---

### 2. triangle-consistency-pigeonhole (revise) — APPROVE, with a required scoping check

- Correctly targets the one open residual of the round-18-certified Two-Sided
  Singleton Witness Theorem (existence of matching singleton witnesses on both
  sides) — verified this is genuinely the theorem's own stated open hypothesis
  by rereading `approaches/triangle-consistency-pigeonhole.md` §4, not a
  restatement invented by the outline.
- The proposed technique (anatomy-of-integers / sieve-style density argument on
  the VALUES a_n, not a statistic of the legality-Boolean history) is a
  genuinely different proof *style* from all confirmed-dead FAH mechanisms and
  is correctly argued to fall outside the scope of the (freshly strengthened)
  Class-Blindness Obstruction: whether `a_n`'s out-of-core cofactor has exactly
  one prime factor is an arithmetic property of the integer `a_n` itself, not
  a function computed from a window of past Boolean legality outcomes. This
  distinction is real, not hand-waved — checked it holds up.
- The outline is admirably honest about the risk: `math-explorer-singleton-
  witness.md` reports the phenomenon is common (85–92% singleton rate) only at
  *easy, under-recruited* cores, and rare (5–37%) at the two known genuinely
  hard, properly-recruited cores — exactly the regime the open hypothesis must
  survive in. No density LOWER BOUND is claimed or assumed; the outline
  correctly directs the builder to attempt the weaker "infinitely often"
  target first, and to treat this as a real, unresolved gap that may turn out
  false, not a target to force through.
- Step 5's "third pigeonhole layer" (forcing `F' ∩ F'' ≠ ∅` with a *shared*
  recurring witness) is honestly flagged as having no argument yet — good,
  this is the second genuinely open ingredient, not smuggled as solved.
- One scoping requirement for the builder (already present in the outline's
  own "Watch out for," but worth restating as a gate condition): the FIRST
  deliverable must be the direct computational check of whether singleton
  occurrences are genuinely unbounded in count on the two hard seeds (not just
  present at low rate in one finite window) — if that check fails outright,
  the approach should report a clean RETHINK rather than force a patch.

Verdict: **APPROVE**, conditional on the builder actually running the mandated
pre-build computational check first (already specified in the outline; not a
new requirement).

---

### 3. core-growth-monotonicity (revise) — APPROVE

- Correctly targets the weaker H2 sub-target ("some self-absorbing S* exists,"
  not full NTBT/S*=Q and not N(S*)=0) — this is genuinely the only untried H2
  angle per `math-explorer-h2-subfamily.md` (prong 1's own recommendation).
- Verified against the approach file's own certified content
  (`Binary Refinement Lemma`, `Threshold Recursion Bound Lemma`, `Proposition 3
  Non-Constructivity of M_B`): the outline's Step 3 ("Non-Recurrence of
  Refinement Primes") is explicitly checked by the outline itself against
  Proposition 3's obstruction and is honestly reported as NOT yet evading it in
  its naive form — the outline does not claim a bypass, it flags the exact
  place a sharper invariant is needed and instructs the builder to report a
  clean dead end if none is found. This matches memory rule 28's mandate (do
  the equivalence/evasion check at review time) — I re-verified: mere
  *existence* of S* (an existential claim) is not obviously the same object as
  *boundedness of N(S_k)* (a numeric-bound claim, refuted at the M_B level by
  Prop 3), so it is legitimate to attempt as logically distinct, but the
  outline is right that this must be checked, not assumed, by the builder.
- No risk of resurrecting the exhausted counting/pigeonhole corridor — this
  targets prime-non-recurrence + fixed base-type alphabet, a different pair of
  facts than the N(S_k)/|𝒫'(S)| counting attempts already killed.

Verdict: **APPROVE**, with the outline's own honesty requirement (report a
clean negative if Step 3 doesn't evade Prop 3) treated as mandatory, not
optional.

---

### 4. self-absorbing-by-construction (advance) — APPROVE

- Pure numeric hardening, no new mechanism proposed or implied solved. Cross-
  checked against `math-explorer-h2-subfamily.md` prong 1: the two new seeds
  (a_1=510510, |Q|=7, largest tested; a_1=209370, skewed one-huge-prime shape)
  and their window-artifact resolutions (200,000 and 300,000 respectively) are
  accurately reported, matching the explorer's own numbers exactly.
- Correctly scoped: explicitly instructed not to imply progress toward a proof,
  and to record the standing "resolved window artifact" pattern explicitly so
  future rounds don't have to rediscover it (matches memory rule 29's own
  mandate).
- Cheap to build (already-computed data, write-up only); worth the slot to keep
  this deliverable's record airtight, per the run's floor-deliverable
  precedent (2|a_1, a_1=p^k theorems already APPROVEd).

Verdict: **APPROVE**.

---

### Diversity / plateau assessment

The four approaches are NOT variations of one framing: (1) is pure
consolidation/bookkeeping plus a genuinely new closed-family lemma; (2) is a
new proof *style* (arithmetic/anatomy-of-integers on values, not a statistic of
the selection process) attacking H1's narrowest-yet open residual; (3) attacks
H2 via a different existential target than the exhausted counting corridor;
(4) is pure numeric record-keeping. This is reasonable diversity for a round
explicitly split between hedging the run's floor deliverable (1, 4) and two
genuinely distinct attempts at the two remaining open hypotheses (2 for H1, 3
for H2) — not four variants hitting the same wall. No repackaging of any of
the 19+ dead FAH mechanisms or the refuted a_1=p·q family was found in any of
the four outlines (verified against `current.md`'s dead-end list and both
math-explorer reports).

### Ranking

Registered slugs: all four (n1-periodicity-reconciliation,
triangle-consistency-pigeonhole, core-growth-monotonicity,
self-absorbing-by-construction) already exist in the population — no new
registration needed this round (all are `revise`/`advance` of existing slugs).

Ran `update_ranking` anchoring this round's more-active approaches against
established peers and against each other, clearing all stale flags:
n1-periodicity-reconciliation and triangle-consistency-pigeonhole (both
actively narrowing content, round 18) beat the long-inactive
covering-system-construction/greedy-exchange-cost-potential/
cofinite-window-capacity-bound (untouched since rounds 9–12); core-growth-
monotonicity (certified lemmas, real structural content) beats
self-absorbing-by-construction (pure numeric hardening this round, no new
lemma) and sieve-density-exception-bound (dead-end); the two verified-milestone
sub-family theorems (prime-power-seed, even-a1) both beat self-absorbing-by-
construction (a completed proof outranks an open-conjecture numeric record);
n1-periodicity-reconciliation and triangle-consistency-pigeonhole are scored a
draw (comparably strong, different roles — consolidation vs. new positive
mechanism). Updated Elo (post-round): covering-system-construction ~1849
(still leader but ahead by less), greedy-exchange-cost-potential ~1761,
n1-periodicity-reconciliation ~1656, prime-power-seed-periodicity-theorem
~1530, even-a1-full-periodicity-theorem ~1530, triangle-consistency-pigeonhole
~1519, cofinite-window-capacity-bound ~1508, core-growth-monotonicity ~1489,
self-absorbing-by-construction ~1466, sieve-density-exception-bound ~1443
(dead-end, unchanged rank position).

build set: n1-periodicity-reconciliation, triangle-consistency-pigeonhole, core-growth-monotonicity, self-absorbing-by-construction
