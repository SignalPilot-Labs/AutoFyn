## imo-2026-06 — proof-reviewer, round 5

### 0. Independent spot-check of this round's governing correction (mandatory per dispatch)

Before trusting anything downstream, I independently re-implemented the whole pipeline
a THIRD time (distinct from the explorer's and outline-reviewer's own reimplementations)
— fresh trial-division sequence generator, fresh τ/ρ computation, literal global-minimum
witness search scanning n=1..1400 directly (no tail-window shortcuts) — and reran
a_1=187. Result: S₀={2,3,11,17}, rogue pair ({17,2},{11,3}), witnesses n_A=6 (a_6=238=
2·7·17), n_B=5 (a_5=231=3·7·11), shared outside-core prime {7} on both sides. This
matches the explorer's and outline-reviewer's numbers exactly. **Round 4's "V=∅ always,
18/18 seeds" is genuinely, triple-independently retracted.** This is NOT the round-3/4
witness-selection bug — all three independent implementations this round use the
literal, global-minimum witness convention. I additionally spot-checked
`covering-system-construction`'s Conditional Single-Pair Resolution Theorem's central
claim on this same seed: computed that literally every A'={17,2}-type occurrence with
index > n_B = 5 has 7 | a_n (58/58 checked instances, 0 exceptions) — the mechanism, not
just the abstract statement, checks out.

I also went one step further than any builder attempted this round: I checked whether
recruiting S₁ = S₀ ∪ Q_R (as the Conditional Simultaneous Resolution Theorem produces)
actually leaves a globally rogue-pair-free extended-type family, or whether refining the
core can spawn brand-new rogue pairs among previously-non-rogue base types. On all 3
available multi-round-eligible seeds (187, 209, 247 — 385 has zero S₀-level rogue
pairs), I found **zero new rogue pairs at S₁**. This is reassuring but not a proof, and
— importantly — **it is a gap the covering-system-construction builder's own "Bottom
line" claim silently assumed away** (see verdict below). I record this as a genuinely
new, previously-unflagged open item for next round.

### 1. covering-system-construction — Status: partial. Verdict: CHANGES REQUESTED

**Correct, unconditional, newly certified:** Monotonicity of Resolution Lemma. I
re-derived this from scratch: if S₀ ⊆ S₁ and A', B' (S₀-persistent) share a prime p ∈ S₀,
then for any S₁-refinement A'', B'' with A''∩S₀=A', B''∩S₀=B', p ∈ A'' and p ∈ B'', so
p ∈ A''∩B''. One paragraph, no gap. Certified to
`lemmas/monotonicity-of-resolution.md`.

**Correct, but CONDITIONAL (not certified as unconditional):** the Conditional
Single-Pair Permanent Resolution Theorem and its batch form, the Conditional
Simultaneous Resolution Theorem, both conditional on the (still fully open) "Universal
Singleton Hypothesis." I checked the proof line by line: it correctly uses the certified
Lemma G (Extended Earliest-Witness Intersection) to get a SHARED prime q on both sides
of a rogue pair when both sides are singleton, then correctly observes the Generalized
Bounded Witness Lemma's conclusion ("for every n > m", not merely "infinitely many via
pigeonhole") collapses to an exact, no-pigeonhole statement when the target finite set
has size 1 — this is a genuine, correct repair of round 3's documented "route 2"
obstruction (previously the recruited prime was only certified on one side). I
independently verified the mechanism numerically (58/58 A'-type occurrences past n_B all
divisible by 7, for a_1=187) — matches exactly.

**A gap the builder did not flag, which I consider load-bearing.** The file's "Bottom
line" states "given the Singleton Hypothesis, the whole problem is solved," treating
S₁ = S₀ ∪ Q_R as a terminal core. But the Conditional Simultaneous Resolution Theorem
only proves that pairs ALREADY rogue at S₀ get resolved at S₁ — it says nothing about
whether refining S₀ → S₁ can spawn NEW S₁-extended-persistent types (by splitting a
previously-non-rogue base type's occurrences by divisibility by the newly recruited
prime(s)) that form new disjoint pairs not present at S₀. This is exactly the same
"refinement manufactures new classes" phenomenon `witness-index-descent` independently
documented this round (for its own well-ordering's non-monotonicity) — a real, general
concern about the recruitment process, not a nitpick. I spot-checked this on all 3
available multi-round seeds and found no counterexample, but it is unproved and was not
even acknowledged by the builder. This does not undo the real progress made (the
Monotonicity Lemma and Conditional Theorems are correctly proved as stated), but it does
mean the "given Singleton Hypothesis ⟹ problem solved" claim is currently an overclaim;
the true reduction needs one more ingredient ("no collateral rogue pairs" or an
equivalent "closed under recruitment" strengthening of the Singleton Hypothesis).

**Verdict: CHANGES REQUESTED.** Real, substantial progress (2 new results, 1 certified
unconditionally); the crux is narrowed to the Singleton Hypothesis PLUS the newly
identified collateral-rogue-pair gap. Neither closed.

### 2. greedy-exchange-cost-potential — Status: partial. Verdict: CHANGES REQUESTED

**New unconditional lemma, correct modulo one wording fix:** Lemma H (Critical Prime
Dichotomy). I re-derived the proof from scratch: writing a_n = q'^e·c with
gcd(c,q')=1, if c > a_{n-1} then by the greedy rule's minimality, c must be illegal
against some earlier a_i, and since P(a_n) = P(c) ⊔ {q'}, the only possible common prime
of a_n and a_i (guaranteed to exist by Free Facts) is q' itself. Correct, and a genuinely
new proof mechanism (stripping a prime from the actual witness, not bounding a
competing-candidate's magnitude as round 3's Lemma F did).

**Wording issue found and corrected upon certification.** The source states the two
branches are mutually exclusive ("exactly one holds"). The proof only establishes ¬(a)
⟹ (b), i.e. the inclusive "(a) or (b)" — nothing rules out both holding simultaneously.
This does not affect the file's own use of the lemma (every application only needs "(a)
or (b)"), so it is a wording overclaim, not a substantive error. Certified with the
corrected ("at least one") statement to `lemmas/critical-prime-dichotomy.md`.

**Honest, correctly-documented failure to close the Singleton Hypothesis.** The file
correctly shows Lemma H gives a necessary-but-not-sufficient condition per prime: two
distinct primes q', q'' ∈ F' could each independently satisfy branch (b) via different
earlier witnessing indices i ≠ i', and nothing certified forces a contradiction (Free
Facts and its descendants are pairwise-intersection existence statements, never
statements bounding the total number of distinct primes across many such pairwise
intersections for one fixed integer). The attempted repair (forcing i = i') is
correctly shown to have no supporting mechanism. This is genuine, precisely-located
progress on the exact remaining obstruction, honestly reported as unresolved.

**Verdict: CHANGES REQUESTED.** Genuine new certified lemma; core target (Singleton
Hypothesis) still fully open, correctly disclosed as such.

### 3. witness-index-descent — Status: partial. Verdict: RETHINK

I verified the **Same-Side Ordering Lemma** from scratch: trivial but correct (every
occurrence of an S₀-extended-persistent type A' refining base type A is, by definition,
an occurrence of base type A, so its earliest index is ≥ the earliest index of base type
A overall). No gap. Certified to `lemmas/same-side-ordering-lemma.md`.

However, the approach's actual mission (a well-ordering descent proving recruitment-
process termination) is shown by the file's own honest analysis to fail for two
independent reasons, and I could not find a repair in the time available: (a) the only
coherent single-stage target ("no rogue pair exists") is demonstrably false — rogue
pairs provably exist at S₀ for a_1=187 etc.; (b) reformulated across the increasing
chain of recruitment stages, the natural monovariant (smallest rogue-pair witness index
at any stage) is not stage-monotone: I confirm this is structurally identical to round
3's finding for the |A'|+|B'| size measure — a second, independently-chosen well-ordering
hitting the same "refinement manufactures new small-index classes" wall. The file's own
point 3 additionally shows that even a full proof of the ordering sub-lemma (Step 2 of
the outline) would supply no logical leverage the certified Lemma G doesn't already have
unconditionally (Free Facts' shared-prime conclusion holds for every index pair
regardless of ordering). Given two independent obstructions, no fix identified for
either, and the certified engine (Lemma G) already superseding the tool this descent
would have supplied even if completed, I judge this specific approach's core mechanism
dead as scoped — matching the CLAUDE.md/precedent bar for RETHINK (compare round 3's
witness-depth-bound). The Same-Side Ordering Lemma survives as a certified byproduct but
is explicitly, by the builder's own analysis, not load-bearing for closing (†).

**Verdict: RETHINK.** If revived, needs a genuinely different (not merely
re-parametrized) well-ordering that is provably robust to partition refinement — not
supplied this round.

### 4. reversible-transition-map — Status: partial. Verdict: RETHINK (for its stated
primary goal; disambiguation task itself executed well)

I checked the (⇐) direction of the "S-sufficiency ⟺ V=∅ at level S" claim: it is a
direct restatement of the already-certified Step-5 CRT+cyclic-pigeonhole finish,
correct. The (⇒) direction's argument (if V≠∅ at level S, legality of a future candidate
genuinely depends on a prime outside S, so the S-signature state is not a sufficient
statistic) is directionally sound but written informally (a "consider two histories"
narrative rather than a crisp, fully formalized argument), and "S-sufficiency" itself is
not given a fully formal definition in the file. I believe the conclusion — this framing
is equivalent to, not a bypass of, gap (†) — is correct, and it directly confirms the
outline-reviewer's own flagged risk. This is the important finding: the "finite
automaton" framing the approach was built around cannot be used to circumvent the
recruitment-process termination question; it is the same content in different notation.
Per CLAUDE.md, a target that (even if fully solved) provably cannot close the gap it was
proposed to address is a RETHINK, not a CHANGES REQUESTED (matches round 3's
witness-depth-bound precedent exactly).

The file's Step 3 (backward-injectivity, aimed at the secondary "periodicity from n=1"
gap) is a genuinely separate, legitimate, still-unresolved target, but it is conditional
on (†) already being closed and is not attempted to completion this round. This narrower
target could be revived standalone in a future round.

**Not certified**, pending a tighter, fully formal restatement: "S-sufficiency ⟺ V=∅ at
level S." The mathematical content is recorded in current.md as a population-wide
caution (do not re-attempt a "finite automaton bypass" of (†) without checking this
equivalence first) even though the lemma itself is not certified verbatim.

**Verdict: RETHINK** for the primary-gap framing; the secondary-gap obstruction it
surfaced is a legitimate separate, narrower target for a future round if desired.

### 5. Lemma certification summary

- Certified: `lemmas/monotonicity-of-resolution.md` (covering-system-construction,
  unconditional, verified).
- Certified: `lemmas/same-side-ordering-lemma.md` (witness-index-descent,
  unconditional, verified).
- Certified (wording corrected from "exactly one" to "at least one"):
  `lemmas/critical-prime-dichotomy.md` (greedy-exchange-cost-potential).
- NOT certified: Conditional Single-Pair / Simultaneous Resolution Theorems
  (covering-system-construction) — correct but conditional on the unproved Universal
  Singleton Hypothesis (and, per my finding above, also implicitly on the unaddressed
  "no collateral rogue pairs" gap); kept in-file, matching the round-4 precedent for
  conditional results (Round Resolution Lemma was likewise not certified).
- NOT certified: "S-sufficiency ⟺ V=∅ at level S" (reversible-transition-map) — likely
  correct but not written with the rigor bar required for the permanent shared cache
  (informal (⇒)-direction argument, undefined "S-sufficiency"); recommend a future round
  tighten and resubmit if this framing is revisited.

### 6. current.md

Updated `results/imo-2026-06/current.md`: Status remains `partial`; added a "ROUND 5
CORRECTION" section documenting the triple-independent reconfirmation that "V=∅ always"
is false; a "ROUND 5 progress" section merging the 3 new certified lemmas, the verified-
correct-but-conditional theorems, and (new, reviewer-found) the collateral-rogue-pairs
gap; a "ROUND 5 — approach verdicts" section giving each slug's verdict and reasoning;
a lemma-certification summary; and updated next-round guidance prioritizing (1) the
Universal Singleton Hypothesis, (2) the new collateral-rogue-pairs gap, (3) graph
connectivity (not required for the finish). Prior rounds' sections kept for audit trail.

### 7. Ranking

Called `record_outcome` once per slug: covering-system-construction → advanced;
greedy-exchange-cost-potential → partial; witness-index-descent → dead-end;
reversible-transition-map → dead-end.

### Summary verdicts

1. covering-system-construction — Status: partial — Verdict: **CHANGES REQUESTED**
2. greedy-exchange-cost-potential — Status: partial — Verdict: **CHANGES REQUESTED**
3. witness-index-descent — Status: partial — Verdict: **RETHINK**
4. reversible-transition-map — Status: partial — Verdict: **RETHINK**

No approach reached `solved` this round. The problem remains `partial` overall.
