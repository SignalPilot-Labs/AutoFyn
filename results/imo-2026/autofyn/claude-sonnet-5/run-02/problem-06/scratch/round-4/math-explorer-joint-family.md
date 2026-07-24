## imo-2026-06

### Distinct openings (joint/simultaneous-family lens, as dispatched)

1. **"Infinitely-many → cofinitely-many" upgrade, via an aimo-0680-style divisibility
   squeeze.** The IMO functional-equation problem `aimo-0680` (crux: "Upgrade a
   relation known only along an infinite index subset to all indices") proves that a
   relation holding for infinitely many indices `d ∈ Y` actually holds for **every**
   index `j`, by picking `y ∈ Y` with `y − j` larger than a fixed bound and noting two
   quantities are both divisible by `y − j` while their difference is smaller than
   `y − j`, forcing the difference to vanish. This is *exactly* the shape of mechanism
   this round's dispatch is fishing for: a simultaneous/joint argument over an entire
   infinite family that upgrades a pigeonhole-only conclusion ("some prime recurs
   infinitely often," certified here as the Single-Witness-Prime Pigeonhole
   Refinement / Recruitment Corollary) into a conclusion about *all* sufficiently
   large occurrences, not just an infinite subset. **Caveat, stated honestly:** the
   crux's engine is the FE's built-in hypothesis `n | f^n(m) − m` (an exact
   divisibility scaling with the index gap) — our problem has no literal analogue of
   this. Porting the technique requires first manufacturing an analogous "exact
   divisibility that scales with the gap between two occurrences of the same
   extended type" from the certified toolkit (Free Facts + Bounded Gap Lemma /
   Generalized Bounded Gap Lemma), which is not yet available. This is a genuine new
   candidate technique, not yet reducible to a plan — flagging it as the most
   promising unexplored opening from this lens.

2. **Direct computational probe of whether "infinitely many" is secretly "cofinitely
   many" in a concrete rogue instance (a_1 = 175).** Built the actual sequence (3000
   terms) and checked, at S₀ = {2,3,5,7,11} (the original Finite Core Theorem pool,
   no recruitment), the exact rogue pairs flagged in round 3: extended types
   `{2,7}` (refining base `{7}`) vs. `{3,5}` and `{3,11,5}` (refining base `{5}`), and
   `{2,11,7}` vs `{3,5}` — confirmed disjoint, i.e. genuine members of `V` at this
   level, reproducing round 3's finding. Then checked the recruited prime 13 (from
   the Generalized Bounded Witness Corollary) against *all* 67 tail occurrences of
   `{2,7}` and all 50 tail occurrences of `{3,5}` (n ranging 500–3000, well inside the
   confirmed exact period T=274, L=2730=2·3·5·7·13): **13 divides every single one of
   both families, with zero exceptions** — not just "infinitely many." This is
   stronger than what the certified Corollary proves (which only guarantees
   infinitely many). **But** independently verifying the sequence is exactly periodic
   with T=274 from n≈500 onward (checked directly, holds with zero mismatches out to
   n≈2700+T) shows this "all, not just infinitely many" phenomenon is *already a
   direct consequence of periodicity itself* in this window (once periodic, each
   coarse extended type is a union of finitely many exact residue classes mod L,
   each of which trivially always carries every prime of L including 13). So this
   computational finding is **consistent with, but does not independently
   establish**, the joint-family strengthening — it is likely to be circular if used
   naively (assuming periodicity to prove the ingredient periodicity itself needs).

   **Follow-up check that partly defuses the circularity worry.** I re-ran the same
   check restricted to n < 500 (well before, and including, the very first
   occurrences of each type) instead of the confirmed-periodic tail: **still 13
   divides every occurrence, with zero exceptions, all the way back to the first
   occurrence of each type** — `{2,7}` first occurs at n=3 (a_3 = 182 = 2·7·13) and
   every one of its 13 pre-n=500 occurrences carries 13; `{3,5}` first occurs at n=5
   (a_5 = 195 = 3·5·13) and likewise every one of its 10 pre-n=500 occurrences
   carries 13. Since n=3 and n=5 are far too early for any "already periodic"
   argument to explain the pattern (the true period only sets in empirically well
   after n≈500), this is **not** simply a restatement of periodicity — it looks like
   a genuine early-onset phenomenon. This raises the possibility that "infinitely
   many → all, from the first occurrence" may be provable directly (not merely
   observed post-hoc), which would be exactly the joint-family fact needed to close
   route 2 of the minimal-counterexample attack in `covering-system-construction.md`
   Step 4f. **This remains empirical evidence on one seed, not a proof — but it is
   the single most promising concrete lead this lens turned up**, and is a much
   better candidate for the next round to attack directly (e.g., try to prove: "the
   prime q recruited by the Generalized Bounded Witness Corollary against a specific
   witness m of B' in fact already appears in *every* A'-type term after m, not just
   infinitely many" — a strengthening of the Corollary itself, provable or refutable
   by revisiting its proof mechanism rather than needing new machinery).

3. **Why re-using multiple B'-witnesses (rather than one) adds nothing on the
   already-covered side.** Checked directly: the certified Bounded Witness Lemma /
   Generalized Bounded Witness Lemma already use the *earliest* available witness of
   type B, and their conclusion already covers *every* later occurrence of type A
   (not just infinitely many) — see `bounded-witness-lemma.md` and
   `generalized-bounded-witness-lemma.md`, both proved with "for every n > m with
   τ(n)=A" not "for infinitely many n." So a joint argument that tries to use
   *multiple* witnesses of B (rather than the single earliest one) to strengthen the
   A-side conclusion is redundant — the single-earliest-witness argument already
   exhausts what pairwise gcd (Free Fact 2) can give on that side. The genuine open
   question is symmetric and one-sided: does the *recruited* prime q, shown (Corollary)
   to hit infinitely many A'-occurrences, also hit (all, or even just some/enough)
   B'-occurrences? This confirms round 3's Step 4f diagnosis is the correct
   localization of where a joint-family argument needs to bite — not "more witnesses
   on the known side," but "propagate the conclusion to the *other*, fixed-witness
   side."

4. **A pigeonhole/density argument over the whole family, tested and found NOT to
   have an obvious form here.** Considered whether "every B'-type term must avoid a
   finite obstruction set, and infinitely many terms can't all avoid it" (the
   dispatch's suggested shape) has a home. The obstruction here would have to be
   "not containing q" — but there is no certified reason ruling out an extended type
   B' having infinitely many occurrences that avoid an arbitrary externally-recruited
   prime q (nothing in the Free Facts / Bounded Witness machinery bounds *how many*
   distinct primes outside S₀ can divide different occurrences of the same fixed
   S₀-level type — this is exactly Lemma F's diagnosis in
   `greedy-exchange-cost-potential.md`, that minimality controls magnitude, not prime
   content). Positive density of B' is also not established (only "infinitely often,"
   per Persistent-Type Pigeonhole and its extended-level analogue) so a genuine
   density-based pigeonhole (e.g. "two disjoint infinite sets of positive density
   inside a bounded modulus must overlap") does not have a certified foothold either.
   This specific shape of argument looks like a dead end absent a new density lemma.

5. **Second seed, cleaner confirmation (a_1 = 35, Q = {5,7}, known extra-prime pool
   {2,3}, T=34, L=210).** Checked, over the full 2500-term simulation (not just a
   tail), whether base type `{7}` and base type `{5}` always carry a reconciling
   subset of `{2,3}` — with **zero exceptions from the very first occurrence of each
   type** (`{7}` first occurs at n=3; `{5}` first occurs at n=2): every one of the
   295 occurrences of base type `{7}` contains **both** 2 and 3 (not just "eventually,"
   literally always in the tested range); every one of the 1764 occurrences of base
   type `{5}` contains **at least one** of {2, 3} (varying between {2,5}, {3,5},
   {2,3,5}, {2,5,11}, ... — so `{5}` is genuinely non-uniform, ruling out a single
   universal glue prime as in the retracted Step 4b — but always hits `{2,3}` in some
   combination). Since `{7}`'s occurrences always carry both members of {2,3}, they
   trivially intersect *any* nonempty subset of {2,3}, so this one-sided uniformity
   (on the {7} side) is enough by itself to force every disjoint pair to intersect —
   an asymmetric, not symmetric, mechanism. This is a second independent seed
   (different from a_1=175, tested from n=1 not just a late tail) exhibiting the same
   qualitative phenomenon as opening 2's follow-up: **an exactly-uniform-from-the-start
   membership fact on (at least) one side of a disjoint pair**, which is stronger than,
   and would immediately imply, the pairwise-intersection gap (†). This is the
   strongest concrete lead this lens produced: the actual mechanism reconciling
   disjoint types may not be "some shared prime recurs infinitely often" (the
   certified pigeonhole lemmas' conclusion) but rather **"one persistent type is
   always (from its first occurrence) a superset of a small fixed core relative to
   each disjoint partner"** — a strictly stronger, and structurally different, claim
   that the certified toolkit's pigeonhole lemmas do not currently state or prove,
   but which both tested seeds satisfy with zero exceptions.

### Candidate technique(s)
- The `aimo-0680` "infinite-index-set + divisibility-squeeze forces exact relation"
  pattern (see opening 1) — the best structural analogue found, but requires
  constructing an analogous scaling-divisibility fact from this problem's own
  hypotheses (not yet available; a genuinely new lemma would be needed, likely built
  from the Bounded Gap / Generalized Bounded Gap Lemmas' "smallest multiple of a
  fixed modulus" mechanism, reinterpreted as a index-gap-vs-value-gap relation).
- Standard tools already in play and still correctly load-bearing: infinite
  pigeonhole (`knowledge_base.md` "Pigeonhole / extremal principle"), CRT
  (`knowledge_base.md` "Modular arithmetic, CRT").

### Cheap-kill candidates
None obvious from this lens specifically — the "multiple witnesses on the known
side" idea (opening 3) was the natural cheap structural check and it cleanly rules
itself out (redundant with the certified single-witness lemmas) rather than killing
anything new.

### Knowledge-base entries to use
- "Pigeonhole / extremal principle" (`knowledge_base.md`) — already the engine
  behind every certified lemma in this workspace; any joint-family strengthening
  will still need it as the base mechanism.
- "Modular arithmetic, CRT" (`knowledge_base.md`) — needed for Step 5's finish,
  unaffected by this round's findings.
- No new knowledge_base.md entry looks like a ready-made fit for the
  "cofinitely-many, not just infinitely-many" upgrade; this appears to be a genuine
  gap in the current toolkit, not a retrieval failure.

### Analogous past problems (cruxes)
- **`aimo-0680`** (IMO-level FE periodicity problem, `number_theory` /
  `sequences-and-recurrences` domain, crux: "Upgrade a relation known only along an
  infinite index subset to all indices"). Strongest structural analogue found: the
  problem's overall shape (classify indices into finitely many "rows"/types, show
  each is eventually periodic, combine via lcm) is essentially the same architecture
  as this problem's Step 3–5 (persistent types → periodicity via CRT/lcm). Its Step 2
  is precisely the missing joint-family mechanism this round's dispatch asked about,
  but its engine (`n | f^n(m) − m`) does not have a certified analogue here yet —
  adapting it is a genuine open task for the next round, not a plug-in.
- **`aimo-0477`** (gcd-chain-stabilizes problem) — checked, not a good match: its
  divisor-chain-must-stabilize mechanism relies on a fixed reference term's gcd being
  monotonically non-decreasing and bounded above by that fixed term, which does not
  obviously map onto this problem's "which extra primes get recruited" question
  (round 3's Step 4c already tried and rejected several monovariant candidates of
  this general "monotone + bounded ⟹ stabilizes" shape; see
  `covering-system-construction.md` Step 4c "Monovariant candidates tried").
- No other crux in `sequences-and-recurrences`, `pigeonhole`,
  `modular-arithmetic-and-CRT`, or `divisibility-and-gcd` (number_theory) found in a
  targeted search for "period"/"eventually" keywords looked like a closer match than
  these two.

### Prior progress
See `current.md` for full detail. Summary relevant to this lens: gap (†) is
localized to residual set `V` (rogue pairs, both sides non-canonical
S₀-refinements of disjoint base types). Certified: Free Facts, Bounded Gap Lemma,
Generalized Bounded Gap Lemma, Persistent-Type Pigeonhole, Bounded Witness Lemma,
Finite Core Theorem, Generalized Bounded Witness Lemma (S₀-level) + Recruitment
Corollary, Extended Persistent-Type Pigeonhole, Canonical-Refinement Lemma,
F_A∩F_B≠∅. All of these already fully use the "single earliest witness controls all
later occurrences on one side" argument (opening 3 above confirms there is no slack
left to extract there). The open content is specifically the other-side
propagation, matching round 3's own diagnosis.

### Dead ends (do not retry)
- "Universal glue prime" (retracted round 2, falsified by a_1=35).
- "cost(n) ≤ 1 in sparse-Q regime" (retracted round 3, falsified by a_1=35).
- "Zero further recruitment rounds needed" (falsified this-run round 3 by a_1=175 —
  do not re-test as if computationally unrefuted).
- Minimal-counterexample / well-ordering attack on `V` using only the certified
  magnitude lemmas (Step 4f, both routes fail for documented structural reasons —
  Lemma F: minimality bounds magnitude, not type).
- (New, this lens) "Use multiple B'-witnesses instead of one to strengthen the A'-side
  conclusion" — confirmed redundant; the single canonical/earliest witness already
  gives the strongest available statement on that side (opening 3).
- (New, this lens) Naive density/obstruction-avoidance pigeonhole across the whole
  B'-family (dispatch's suggested shape) — no certified foothold; positive density of
  a persistent type is not established, and nothing bounds how many external primes
  can appear across different occurrences of a fixed S₀-level type (opening 4).

### Small-case / intuition notes (labeled as conjecture / empirical only)
- For a_1 = 175 (the round-3 rogue instance), computationally confirmed (not proved):
  once past n ≈ 500 (deep inside the eventual exact period T=274, L=2730), the
  recruited prime 13 divides **every** occurrence of both flagged rogue types
  `{2,7}` and `{3,5}` (67/67 and 50/50 respectively), not merely infinitely many.
  This is consistent with — and, per opening 2's analysis, likely just a restatement
  of — full periodicity already holding in this window, so it should be treated as
  weak/circular evidence, not as free support for a non-circular joint-family lemma.
  A genuinely useful test for the next round would be to check this same
  "infinitely-many → all" question in a regime *known* not yet to be exactly
  periodic (e.g. very early indices, before the true period stabilizes) to see
  whether the "all" property already holds pre-periodicity (which would be real,
  non-circular evidence) or only emerges once periodicity has already set in (which
  would confirm the circularity concern and rule this route out cleanly).
