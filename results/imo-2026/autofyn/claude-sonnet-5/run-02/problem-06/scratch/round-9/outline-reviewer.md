## Setting

Read: `/tmp/round-9/proof-outliner.md`, `results/imo-2026-06/current.md`, the live
approach files, and the certified lemma chain (`generalized-bounded-witness-lemma.md`,
`collateral-safety-theorem.md`, `singleton-side-fah.md`, `extended-earliest-witness-
intersection.md`). Independently reimplemented the full pipeline from scratch (trial-
division factorizer, no sympy, per standing memory rule) to check the outline's two
load-bearing numeric claims before approving anything: the "cofinite FAH suffices"
derivation, and whether the round's target regime (rogue pairs with |F'| or |F''| ≥ 2
at a **properly recruited** core) is real and what it looks like. Script:
`/tmp/round-9/sim.py` (+ `sim3.py`/`sim4.py`/`sim5.py`), independent of any prior
round's script.

## Critical finding that changes this round's picture (report to builders)

**Round 8's "~6% divisibility, not cofinite" a_1=4807 data point is invalid as
evidence against FAH.** I recomputed it: that number was measured at S₀ = Q, i.e.
*before* the Finite Core Theorem's own recruitment is applied — not a genuine rogue
pair of the recruitment process the theorem chain actually operates on. At a_1=4807's
**properly recruited** core (S₀ = {2,3,5,7,11,19,23,73,127}), there are **zero** rogue
pairs at all — the seed doesn't even reach the open regime once correctly recruited.
I confirmed this and then searched ~100 further seeds for a genuine rogue pair with
|F'| or |F''| ≥ 2 at a properly recruited core (the actual open, non-singleton
regime); only one seed produced one in the range searched: **a_1 = 11305**, rogue
pair A′={3,7} (n_A=4), B′={2,5} (n_B=7), F′={11}, F″={11,103} (|F″|=2, genuinely
open case, canonical prime q*=min(F′∩F″)=11). I directly tested divisibility of the
60 later A′-type occurrences (out of 6000 terms) by q*=11: **60/60 = 100%, zero
exceptions** — literal FAH holds here, not just cofinite, and not anywhere near the
round-8 "6%" figure. (The other prime in the menu, 103, divides only 1/60 — consistent
with the pigeonhole corollary's "some single prime absorbs infinitely many
occurrences" already being q*=11 specifically, from the very first occurrence.)

This is genuinely new, valid computational evidence in the actually-open |F′|,|F″|≥2
regime (previous rounds' positive evidence was all singleton, per Singleton-Side FAH;
the one non-singleton data point on record was measured at the wrong core). It does
**not** prove FAH, but it removes the strongest empirical reason to prefer a weaker
"cofinite" target over literal FAH, and it should be reported to all three builders as
the seed to test against (not a_1=4807 at S₀=Q, which is not a valid instance of the
open problem). Builders should also try to find a genuine counterexample to literal
(zero-exception) FAH at a properly-recruited core before assuming cofinite is strictly
easier — none has been found yet by anyone.

## Per-approach review

### covering-system-construction (revise) — APPROVE (with mandatory first deliverable)
- The "cofinite FAH suffices for Step 8.5" derivation in the outline's preamble is
  logically sound as stated: an S₁-extended-persistent type occurs infinitely often by
  definition, so a finite exceptional subset is not itself persistent and cannot
  register as a competing type — it only delays the "eventually" threshold already
  built into Extended Persistent-Type Pigeonhole. This is a genuine, useful weakening,
  correctly re-derived from certified lemmas, not hand-waved. Good catch by this
  round's explorer/outliner.
- The Recruitment-Budget Lemma (Step 3) is the crux of this revision: every prime ever
  recruited against pair (A,B), at any stage k, lies in the FIXED, Q-level set
  W_{A,B} = P(a_{m_A}) ∪ P(a_{m_B}) (m_A, m_B the *base-type* earliest occurrences, not
  the *extended-type* witnesses n_A, n_B used inside the Generalized Bounded Witness
  Lemma's own corollary). This is exactly the risk the outline itself flags under
  "Watch out for," and it is real: the corollary's proof picks "any witness index m
  with ρ(m) = B′" for the *current-stage* extended type B′, with no guarantee m_B (the
  base-type witness) is itself a valid ρ-witness at every stage — the already-certified
  Witness Discontinuity Obstruction exists precisely to show extended-type witnesses
  can drift when the core grows. I did not have time to reimplement the full iterative
  multi-round recruitment process (my simulation computes the final recruited core in
  one shot, not round-by-round), so I could not confirm or refute the W_{A,B}
  containment claim myself this round. **The outline's own Step 4 (cheap kill first)
  is therefore mandatory, not optional** — the builder's first deliverable must be an
  actual round-by-round simulation checking whether every recruited prime traces back
  to P(a_{m_A}) ∪ P(a_{m_B}) specifically, before investing in Step 3's proof. This
  matches the standing memory rule (never anchor a pigeonhole to a claim not yet
  verified against the certified drift obstruction).
- Diversity: this is a genuinely different mechanism from its two siblings (global
  counting-budget on *which primes* get recruited, across *rounds*), not a rewording.

### cofinite-window-capacity-bound (new) — APPROVE (with the corrected seed)
- This is the plateau-breaking framing CLAUDE.md calls for: a double-counting /
  capacity-bound argument on the SIZE of an exception set, structurally distinct from
  every one of the six dead per-occurrence-absorption mechanisms diagnosed by Lemma I
  (all of which tried to force one witness-level contradiction; this bounds a count
  against an already-certified finite structural ceiling). Genuinely different
  technique, not a relabeling.
- The "cofinite sufficiency" premise it relies on is the same sound derivation checked
  above under covering-system-construction — fine, shared correctly, not duplicated
  proof effort (both approaches import it, as intended).
- However, its own Step 4 self-critique is exactly right and must be enforced: an
  O(1)-per-window bound alone gives density control, not finiteness of the exception
  set — the builder must not stop at "bounded escape rate" and call it done. Flag this
  explicitly as the number-one way this approach could silently fail to close its own
  stated target even if Step 3's counting argument succeeds.
- Given the new a_1=11305 evidence (zero exceptions found, not just few), instruct the
  builder: if the window-capacity argument naturally forces the O(1) bound down to
  literally 0 beyond a finite range, that is a stronger result (equivalent to literal
  FAH) and should not be avoided or downgraded — the outline already says this
  correctly ("Watch out for" section), just reinforcing it given the corrected data.
- Update the outline's Step 4 sanity-check target: retire a_1=4807-at-S₀=Q as a test
  case (invalid, wrong core) and use a_1=11305 (or search for further |F′|/|F″|≥2
  seeds using a properly-recruited core — my `sim.py`/`sim3.py` in `/tmp/round-9/` is
  reusable for this).

### greedy-exchange-cost-potential (revise) — APPROVE (with mandatory cheap-kill first)
- The predecessor-inheritance/transport framing (occurrence j ⟹ occurrence j+1) is a
  third genuinely distinct mechanism — an inductive chaining argument on consecutive
  occurrences of a fixed type, not a counting or budget argument. Good diversity.
- Its own Step 2 mandates a scattered-vs-runs cheap kill before committing to the
  Auxiliary Transport Lemma, and explicitly plans a graceful pivot to the sibling
  cofinite framing if it fails — well-designed, not a doomed line dressed as new.
- On the a_1=11305 data I collected: the 60 A′-occurrences are divisible by q*=11 with
  zero failures, so "scattered failures" cannot be tested on this seed (there are no
  failures at all here) — this seed alone won't discriminate Step 2's branch; the
  builder needs a genuinely rogue seed with actual exceptions (if one exists) to run
  the Step 2 test meaningfully, or note honestly that no exception has yet been found
  anywhere in the open regime (which is itself worth reporting up, since it weakens
  the case that a one-step transport lemma is "false on its face").
- Its outline text correctly avoids re-deriving the already-refuted core-refinement-
  stage recursion (Witness Discontinuity Obstruction) — the object here (occurrence
  index j within one fixed type) is legitimately different from the object that
  obstruction refutes (extended-type witness drift under core refinement). No
  circularity found.

### seed-coupling-induction — correctly left dead
Outliner correctly excludes it; falsification stands (round 8, independently
reconfirmed twice). Not revived, no viable new reduction step proposed. Elo lowered
this round via anchoring comparisons against the two live leaders (was un-updated
since round 8's cold-start registration, `last_outcome` was still null — now cleared
and anchored below the live leaders, above the other confirmed dead-ends given it at
least produced a clean falsification rather than a wasted round).

### density-sieve-contradiction, hypergraph-transversal, amortized-charging-budget,
witness-depth-bound, witness-index-descent, reversible-transition-map,
recruitment-round-charging, scalar-well-ordering-lock-in
Correctly left out of this round's field — all either stale-and-superseded or
already confirmed dead-end/RETHINK in prior rounds; no new content proposed for them
this round.

## Diversity check (CLAUDE.md plateau-breaking requirement)

All three build-set approaches still target the identical certified reduction (the
same shared FAH/cofinite-FAH crux, correctly — this crux has been established as the
*sole* remaining content of the whole problem for 5+ rounds, so this is not the
"one proof split into fragments" trap; each file is a complete top-to-bottom proof of
the actual theorem, differing only in the mechanism for the one open lemma). Within
that, the three mechanisms are genuinely different in kind: (1) global recruitment-
round counting-budget on which primes ever get pulled in, (2) window-capacity double-
counting on the size of one prime's exception set, (3) occurrence-to-occurrence
inductive transport. None is a relabeling of another; none is a restatement of a
mechanism already diagnosed dead by Lemma I (all six dead mechanisms tried a single-
witness existential-to-universal promotion; none of these three do that). This
satisfies the plateau-breaking requirement with real, not cosmetic, diversity.

## Ranking

Registered `cofinite-window-capacity-bound` (new, cold-start). Ran `update_ranking`
anchoring the newcomer against both live leaders and confirmed dead-ends, kept
covering-system-construction narrowly ahead of greedy-exchange-cost-potential
(consistent with its longer certified-lemma lead and Elo history), and cleared the
stale `seed-coupling-induction` entry by anchoring it below both live leaders.
Resulting order (best first): covering-system-construction (~1832), greedy-exchange-
cost-potential (~1762), seed-coupling-induction (~1547, dead-end), cofinite-window-
capacity-bound (~1540, cold-start, new this round), reversible-transition-map
(~1417, dead-end), witness-depth-bound (~1380, dead-end), amortized-charging-budget
(~1378, stale partial).

## What to change before/while building

1. covering-system-construction: builder's FIRST deliverable must be an explicit
   round-by-round simulation of the recruitment process, testing whether every
   recruited prime lies in W_{A,B} = P(a_{m_A}) ∪ P(a_{m_B}) using the fixed
   *base-type* witnesses — not the *extended-type* witnesses the underlying lemma's
   proof actually uses. Do not start Step 5's proof until this is confirmed.
2. cofinite-window-capacity-bound: use a_1=11305 (properly-recruited core) as the
   working example, not a_1=4807 at S₀=Q (invalid/wrong core). Do not stop at an
   O(1)-per-window bound and declare victory — must show finiteness of the total
   exception count, per the outline's own Step 4 warning.
3. greedy-exchange-cost-potential: Step 2's cheap kill needs a seed with actual
   exceptions to be informative; a_1=11305 has none (100% divisibility already found).
   Search for a genuinely rogue seed with q*-exceptions in the |F′|,|F″|≥2 regime, or
   report honestly if none is found after a real search — that finding is itself
   informative for the whole population (it would mean literal FAH may just be true
   and provable, redirecting effort toward finding the right mechanism rather than
   weakening the target).

build set: covering-system-construction, cofinite-window-capacity-bound, greedy-exchange-cost-potential
