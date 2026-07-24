## imo-2026-06 (lens: crux-corpus mining, outside number_theory only)

**Scope of this pass.** Per dispatch, I did NOT read the number_theory crux subtopics
(divisibility-and-gcd, p-adic-valuation, etc. — already mined exhaustively in rounds
1–14, see notes #3, #10, #13, #18–#22, #25, #27–#28 in `/tmp/memory/math-explorer.md`).
I queried `past_crux_moves_database.json` filtered to `domain in {combinatorics,
algebra}` across the subtopics most likely to carry an existential-to-universal /
identity-promotion mechanism: `processes-and-algorithms`, `invariants-and-monovariants`,
`extremal-principle`, `double-counting`, `bijections-and-encoding`,
`coloring-and-parity`, `pigeonhole`, `sequences-and-recurrences` (algebra),
`size-bounding-and-descent`. I searched by keyword clusters: (i) eventual-periodicity /
cofinite / tail language, (ii) "forces every/all" / "must divide every" / "pins down"
identity-promotion language, (iii) "largest exception" / "finitely many exceptions" /
maximal-counterexample language (a genuinely different promotion mechanism than
pigeonhole).

**What the exact target gap is** (for calibration, from `current.md`/round-14): FAH
(Full Absorption Hypothesis) — a single fixed prime forced to divide EVERY sufficiently
large occurrence of a given extended-persistent type, not just some/infinitely-many —
is the sole open primary crux, now with 16 confirmed-dead mechanisms, all diagnosed
(round 6's Lemma I, reconfirmed rounds 9/10/12/14) as failing because every certified
tool in this workspace produces existence/magnitude information (∃ a prime, ∃ a bound)
but never IDENTITY-level information tying a specific far-away term's divisibility back
to a fixed witness.

### Findings

**1. `aimo-0016` (IMO SL C5, combinatorics/pigeonhole+induction-and-construction) —
already tried in this workspace, confirmed dead.** Crux: "Upgrade an 'equal
infinitely often' shift relation on state-tuples to 'holds for all indices' by a
one-step downward induction, using an auxiliary windowed-sum sequence to transport the
relation one index earlier." This is the single closest structural match in the whole
corpus to the exact promotion this workspace needs (infinitely-often ⟹ for-all via
one-step transport, not counting). It was already flagged as the best candidate back in
round 9 (note #25) and actually **attempted** that same round by
`greedy-exchange-cost-potential` as the "Successor-Transport Reduction Lemma" /
"predecessor inheritance" mechanism. Verified in `approaches/greedy-exchange-cost-
potential.md` (lines ~1920–1970): the transplant reduces the Successor Claim to
checking whether q*-failures come in scattered singletons or runs among consecutive
same-extended-type occurrences; on the one on-record genuinely open instance
(a_1=11305) it found literal zero-exception FAH already (no failures to transport
between), so the mechanism was never even engaged in anger, and a ~270-seed sweep
found no |F'|,|F''|≥2 rogue instance to test it on at all. `lemmas/successor-transport-
reduction-lemma.md` records this. **Verdict: this crux is a genuine structural analog
but the transplant is already exhausted in this workspace — not a fresh opening.**

**2. `aimo-0051` (USA TST 6, algebra/functional-equations) — already tried in this
workspace, confirmed dead.** Crux: "Upgrade a finite-orbit bound to a single cofinite
orbit by counting how many index-window outputs each length-(B-A) window can miss" — a
genuine window-capacity counting argument that promotes an infinite/dense fact to a
cofinite one by bounding the number of possible "bad" window slots. This is exactly
the technique `cofinite-window-capacity-bound` imported in round 9 (see
`lemmas/cofinite-sufficiency-lemma.md`, `lemmas/confined-gcd-lemma.md`): it correctly
weakens the target from literal FAH to Cofinite FAH (finitely many exceptions), which
is real, certified, unconditional progress — but the resulting window-capacity counting
bound was found (round 9, reconfirmed round 10/12) to stall at the identical
"existential-to-universal promotion" wall, now phrased in divisor-class language: the
counting bound gives SOME infinite divisor class, never provably the ONLY one. Also
already dead.

**3. `aimo-1019` (IMO SL C4, combinatorics/double-counting) — examined, NOT
transplantable, genuinely different obstacle shape.** Crux: "Force a divisibility
condition by equating two double-count totals modulo the per-cell multiplicity." I read
the full problem+solution: it counts a FINITE n×n grid's occurrences of letter M along
two disjoint families of lines two different ways, getting `4k² ≡ 3k² (mod 3)`, forcing
`3 | k`. This is a real "counting promotion to a specific identity" mechanism, but it
critically depends on (a) a FINITE, exactly-known total count of the tracked object
(occurrences of M) that can be computed two ways, and (b) both countings being over a
FIXED, already-known finite index set (the vital lines). Our problem has no such finite
global sum: the greedy sequence is infinite, unboundedly growing, and the "which prime
recurs" question has no known conserved additive total to double-count. Certified
`escape-cost-vacuity`/`sandwich-genericity-theorem` (round 10) already prove, generally,
that any argument built only from the certified class-blind magnitude facts (the only
"global sums" available here, e.g. `n-m ≤ a_n-a_m ≤ (n-m)a_1`) cannot discriminate
between divisor classes — a double-counting argument needs exactly such a class-
discriminating global quantity to work, and none is known to exist for this problem.
Not recommending transplant; flagging as examined-and-rejected so no future round
re-mines it under "double-counting" without this note.

**4. Maximal-counterexample / "largest exception index" promotion family** (searched
specifically per dispatch item (c)) — only 3 hits in the whole corpus
(`aimo-0660` ×2, `aimo-0768`), all finite-object "take the largest element between two
candidates, it wins a confrontation" arguments on STATIC finite configurations (bulldozer
towns, commuting finite sets). None involve an infinite process or an eventual/cofinite
target; the "largest object between two fixed points" template has no analog here since
there is no natural pair of fixed bracketing objects for our target. Not transplantable.

**5. No compactness-argument crux found.** Searched explicitly for "compactness",
"infinite pigeonhole to a fixed point", "limit configuration" language across
combinatorics/algebra — nothing beyond what's already in the certified toolkit
(Extended Persistent-Type Pigeonhole, itself already a compactness-flavored argument
and already fully exploited).

### Overall verdict for this lens

After a deliberately broad, keyword-clustered sweep of combinatorics and algebra
(excluding number_theory), **no genuinely new, transplantable crux move was found for
the exact existence→universal/identity-promotion gap.** The two closest structural
analogs in the ENTIRE corpus (`aimo-0016`, `aimo-0051`) have both already been
transplanted into this workspace (rounds 9) and both independently died at the same
wall Lemma I first diagnosed in round 6 — this is now a THIRD confirmation (after the
16 number-theory-family mechanisms) that this specific promotion gap is not solved by
any pigeonhole/window-counting/one-step-transport shape, regardless of which domain the
technique is borrowed from. The one domain-different mechanism that IS structurally
capable of forcing an exact identity (double-counting a global sum, `aimo-1019`-style)
requires a conserved finite/global additive quantity that provably does not exist for
this problem (certified Escape-Cost Vacuity / Sandwich Genericity already rule out any
class-discriminating use of the only available global sums).

### Recommendation to the outliner

Do not dispatch another crux-transplant search for this specific promotion gap without
a genuinely new ingredient first — specifically, a class-DISCRIMINATING quantity (one
that is NOT a function purely of index/magnitude, unlike everything certified so far).
If no such ingredient can be identified from the problem's own structure (not
borrowed), the crux corpus is very unlikely to supply one either, based on this
exhaustive-as-feasible sweep. The one avenue not yet fully closed off: a genuinely
different TOP-LEVEL target that avoids proving FAH/Cofinite-FAH/EEA altogether (as
`subword-complexity-periodicity`'s EEA reduction already showed is hard — EEA IS
equivalent-difficulty to FAH) — i.e., the field needs a route that never needs to know
"which specific prime," not a smarter way to prove which one. No such route was found
in the crux corpus this round either.

## Distinct openings / structured summary

- **Candidate technique(s):** None new found; confirms `aimo-0016`-style transport and
  `aimo-0051`-style window-counting (both already tried, both dead) exhaust the
  corpus's closest analogs.
- **Cheap-kill candidates:** none obvious beyond what's already certified
  (Escape-Cost Vacuity / Sandwich Genericity already rule out double-counting via any
  class-blind global sum).
- **Knowledge-base entries to use:** n/a this pass (crux-only lens); existing certified
  lemmas already cover the relevant machinery (`sandwich-genericity-theorem.md`,
  `cofinite-sufficiency-lemma.md`, `confined-gcd-lemma.md`,
  `successor-transport-reduction-lemma.md`).
- **Analogous past problems (cruxes):** `aimo-0016` (IMO SL C5) — closest structural
  match, already transplanted and dead (round 9). `aimo-0051` (USA TST 6) — second
  closest, already transplanted and dead (round 9). `aimo-1019` (IMO SL C4) — examined
  this round, genuinely different double-counting mechanism but requires a conserved
  finite global sum this problem provably lacks; not transplantable.
- **Prior progress:** unchanged from round 14 — Status `partial`; FAH/Symmetric
  FAH/Cofinite FAH/EEA remains the sole open primary crux with 16 confirmed-dead
  mechanisms; secondary n=1 gap has the conditional Self-Absorbing Core Theorem
  (certified) narrowing it, with two open sub-gaps (existence of S*, N(S*)=0).
- **Dead ends (do not retry):** all 16 previously-documented FAH mechanisms (see
  `current.md` rounds 6–14); the `aimo-0016` transport mechanism (already tried, round
  9, `successor-transport-reduction-lemma.md`); the `aimo-0051` window-capacity
  mechanism (already tried, round 9, `cofinite-sufficiency-lemma.md` /
  `confined-gcd-lemma.md`); any double-counting argument built from the certified
  class-blind magnitude facts (ruled out generally by `sandwich-genericity-theorem.md`
  / `escape-cost-vacuity.md`).
- **Small-case / intuition notes:** none new computed this round (pure corpus-mining
  lens); prior rounds' extensive computational evidence (16+ mechanisms, ~270+ seeds
  across sweeps) stands unchanged — no FAH counterexample has ever been found, only
  failed proof mechanisms.
