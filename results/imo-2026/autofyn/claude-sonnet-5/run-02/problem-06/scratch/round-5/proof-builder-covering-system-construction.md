## imo-2026-06 — proof-builder round 5 — covering-system-construction

Status: partial (unchanged classification, but the gap is now sharpened significantly).

### What was done this round

Per the outline-reviewer's dispatch, retargeted the approach from round 4's retracted
"V=∅ always" claim (independently reconfirmed false this round via 4 fresh
counterexamples a_1=187,209,247,385 — not re-litigated) back to the recruitment-
process-termination framing, and attempted the dispatched "Simultaneous Resolution
Lemma": that one recruited prime resolves ALL currently-rogue pairs at a round, not
just the one witnessed pair.

New content (Step 7 of the approach file), all fully proved:

1. **Monotonicity of Resolution Lemma** (new, unconditional): once two extended-
   persistent types share a prime in S₀, every further refinement of them at every
   later recruitment stage still shares that prime — resolution is permanent. Makes
   rigorous what round 2 only checked informally.

2. **Conditional Single-Pair Permanent Resolution Theorem**: using the certified
   Lemma G (Extended Earliest-Witness Intersection, new since round 4) together with
   the certified Generalized Bounded Witness Lemma, if BOTH sides of a rogue pair are
   "singleton" (their own earliest-occurrence witness has exactly one prime outside
   S₀), the two sides' forced recruited primes are automatically EQUAL (via Lemma G),
   and — because singleton collapses "some prime of a finite set" to "the one prime"
   in the Generalized Bounded Witness Lemma, eliminating the need for pigeonhole
   entirely — BOTH extended types persist with the new prime attached, so they
   intersect permanently. This is the precise repair of round 3's documented "route 2"
   obstruction (the recruited prime was previously only certified on the reconciled
   side, not the fixed witness side).

3. **Conditional Simultaneous Resolution Theorem** (batch form): if every type in 𝒫'
   with a rogue partner is singleton (the "Universal Singleton Hypothesis"), a single
   finite recruitment round — one prime per connected component of the rogue-partner
   relation, collapsing to literally one prime when that relation is connected —
   permanently resolves every currently-rogue pair at once. This is exactly the
   dispatched target, established conditionally.

4. Verified computationally (fresh from-scratch script, not reusing prior rounds'
   code) that this predicted structure holds exactly in all four known nonzero-round
   seeds (187, 209, 247, 385): every rogue pair's F' sets are literal singletons, and
   the singleton prime is identical across every pair sharing a type (Q_R collapses to
   {7}, {7}, {3}, {19} respectively) — strong corroborating evidence, not a proof, for
   both the mechanism and the (separately open) Singleton Hypothesis.

### What remains open (honestly documented, not papered over)

- The **Singleton Hypothesis** itself — owned by the sibling approach
  `greedy-exchange-cost-potential`, not attempted here.
- If Singleton fails for some type, the **bounded-total-rounds fallback** was
  attempted and shown to reduce to the same still-missing "joint pigeonhole across a
  whole base type's infinite family of occurrences at once" ingredient flagged in
  rounds 2–3 (not supplied this round).
- Whether the rogue-partner relation graph is always connected (needed for the
  strongest "exactly one prime" form rather than "a bounded finite batch") is a
  separate, unexamined combinatorial question — not needed for the finish (a bounded
  batch suffices equally well for Step 6's CRT argument), but flagged as unresolved.

### Bottom line

The recruitment/CRT machinery itself is now fully conditional-complete: given the
Singleton Hypothesis, the whole problem is solved (Step 6's CRT + cyclic-pigeonhole
finish is unconditional given a finite terminal S₀). The sole remaining gap for this
approach is now exactly the Singleton Hypothesis (or, failing that, the joint-
pigeonhole ingredient for the fallback) — not any defect in the recruitment mechanism.
Status: `partial`. File updated:
`/home/agentuser/repo/results/imo-2026-06/approaches/covering-system-construction.md`.

### Promotable lemmas proposed for certification
- Monotonicity of Resolution (unconditional).
- Conditional Single-Pair Permanent Resolution Theorem / Conditional Simultaneous
  Resolution Theorem (certify as conditional implications, so a future proof of the
  Singleton Hypothesis immediately finishes the whole problem).
