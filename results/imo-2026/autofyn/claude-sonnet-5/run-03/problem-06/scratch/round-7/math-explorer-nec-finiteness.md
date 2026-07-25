## imo-2026-06 (lens: central gap — Nec finiteness / Q_min self-sufficiency via sieve/covering techniques)

### Distinct openings surfaced

1. **Sieve/CRT positive-density argument for uncontaminated multiples (new, not yet tried by any approach).**
   Fix a candidate prime r and a finite "avoid set" E (the contaminant primes from a fixed reference term a_i,
   per `contamination-dichotomy-and-reduction.md`). By CRT, since r ∉ E (E finite, r prime not dividing any
   element trivially arranged), the multiples of r that are divisible by NO prime of E have density
   ∏_{s∈E}(1−1/s) > 0 among all integers, hence among multiples of r. This is elementary CRT/inclusion–exclusion,
   not deep sieve theory, but it is a genuinely different lever from anything in the population: it shows
   uncontaminated CANDIDATES (as integers) are never sparse — the real difficulty (already flagged correctly by
   `contamination-dichotomy-and-reduction.md`'s caveat) is entirely about whether the GREEDY SEQUENCE actually
   realizes one of these uncontaminated integers as an accepted term at bounded index, not whether such integers
   exist. This reframes "is contamination unbounded" as "is there a realization-lemma for primes outside rad(a_1),
   analogous to the certified `multiple-of-r-realization.md` (which only covers primes dividing rad(a_1))." A
   genuinely new, concrete sub-target: **prove or refute a Multiple-of-r Realization Lemma for r ∉ R(a_1)** (does
   every sufficiently large multiple of r that avoids some finite exclusion set eventually get accepted?). I did
   not attempt this proof (out of scope for exploration), but it is a clean, well-posed, previously-unstated
   question distinct from the reduction already on file.

2. **Counting/second-moment argument bounding |Nec| directly (not per-prime).** Instead of asking per-prime
   "does r eventually get an uncontaminated witness," bound the total number of primes that can EVER become
   Nec elements using the bounded-gap lemma (`bounded-gap-via-rad-a1.md`: a_{n+1}−a_n ≤ rad(a_1)) to get
   a_N = O(N), then a counting argument on how many distinct singleton-gcd events can occur among O(N^2) pairs
   with values O(N) — analogous in spirit to Zsigmondy/primitive-divisor counting arguments in the KB
   (`Zsigmondy's theorem` entry), though Zsigmondy itself doesn't directly transplant (it's about a^n−b^n, no
   multiplicative recursion here). This is a genuinely different top-level target (bound |Nec| as a global
   count, not close each prime's window individually) — no approach in the population has tried a counting/
   averaging argument on Nec as a whole. Promise: unclear, flagged as untried rather than validated.

3. **Reframe away from Nec/Q entirely: attack "is the sequence realizes-all-sufficiently-large-multiples-of-r"
   for the recruited primes directly, bypassing Nec.** If one could show that once a prime r is recruited
   (first divides some a_j), ALL sufficiently large multiples of r are eventually accepted terms (generalizing
   `multiple-of-r-realization.md` beyond rad(a_1)), self-sufficiency of Q_min would likely follow by a density
   argument (positive density of multiples of any q ∈ Q_min hit every long-enough window, forcing coverage).
   This is the strongest candidate lever found this round, but note it is essentially the generalization
   needed for opening (1) above — same target, restated.

### Candidate technique(s)
- Elementary CRT / inclusion–exclusion (finite avoid-set ⟹ positive density of avoiders) — standard, not deep
  sieve theory (Selberg/Brun sieves are overkill and don't obviously help since we need *realization*, not just
  existence of good integers).
- Counting/second-moment style argument (Zsigmondy-flavor "primitive divisor" counting), applied to bound
  |Nec| globally rather than per-prime.
- Extending the certified Multiple-of-R Realization Lemma (`multiple-of-r-realization.md`) from
  r ∈ R(a_1)-generated (r | rad(a_1)) to arbitrary recruited primes — this is the single most concrete
  actionable next step I found.

### Cheap-kill candidates
- None found that immediately kill the central gap. One useful negative-leaning structural note: the
  positive-density CRT fact (opening 1) is too weak by itself to bound witness index — density existing among
  *integers* says nothing about the *greedy sequence's* selection order, so a naive "just cite CRT density and
  declare done" attempt would be circular/incomplete in exactly the way `contamination-dichotomy-and-reduction.md`
  already warns against. Flagging this explicitly so the outliner doesn't waste a round on the naive version.

### Knowledge-base entries to use
- `knowledge_base.md`'s **Modular arithmetic, CRT** entry (line ~59) — directly underlies opening (1)'s
  density-of-avoiders computation.
- `knowledge_base.md`'s **Pigeonhole / extremal principle** entries — already exhausted per the Monotonicity
  Obstruction Lemma; not a new lever for this gap.
- `knowledge_base.md`'s **Zsigmondy's theorem** entry — inspiration only for opening (2)'s counting flavor;
  does NOT transplant directly (no exponential-sequence structure here), flag as "inspiration, not applicable
  literally."
- No **covering-system** or **sieve-theory** (Selberg/Brun) entry exists in `knowledge_base.md` — confirmed by
  grep; this is a real gap in the KB relative to what the dispatch asked me to scout, not a missed search.

### Analogous past problems (cruxes)
Searched the crux corpus (`past_crux_moves_database.json`) filtered by `domain=number_theory` across
subtopics `sequences-and-recurrences`, `modular-arithmetic-and-CRT`, `divisibility-and-gcd`,
`size-bounding-and-descent`, `pigeonhole`, with keyword filters for "covering system", "covering congruence",
"greedy", "residue class", "density", "unique common prime" etc.
- **aimo-0680** (IMO-SL 2015 N6, already the population's known closest analog, re-checked this round): its
  finishing move ("divisible + bounded ⟹ zero") requires a Markov/unconditional-divisibility hypothesis that
  `active-set-stabilization.md` already proved does NOT hold for our sequence (round 3, re-confirmed by reading
  its file this round) — still not transplantable for the contamination gap specifically.
- **aimo-0727** (IMO 2020 N5-flavor, `divisibility-and-gcd`): "if the multiplier sequence b_k were bounded, the
  prime factors of the whole sequence would be confined to a finite set {primes ≤ B+2} ∪ (primes of a_1,a_2),
  contradicting infinitely-many-primes-divide hypothesis." Structurally *inverse* to what we need (there, a
  finite-prime-set consequence is used to derive a CONTRADICTION from an assumed infinitude of prime divisors;
  here we'd want to directly construct/bound a finite set). Not a genuine match for the contamination
  mechanism, but worth noting as the nearest "finite prime set ⟺ bounded auxiliary sequence" crux move found —
  no exploitable structural overlap (their recursion is fixed-formula/additive, ours is greedy-minimum), so I
  do **not** recommend transplanting it.
- **No genuine covering-congruence-style crux found.** The corpus (searched via "covering system", "covering
  congruence", "avoid a congruence class", "greedy", "residue class", "jacobsthal") returned no problem whose
  crux move is a covering-congruence / Jacobsthal-function argument on a self-generated greedy sequence. This
  confirms round 4's finding (`math-explorer.md` rule 22): "No crux in the corpus attacks a genuine
  greedy-minimum-over-growing-constraint-set recurrence." Treat this as a corpus gap, not a missed search —
  do not keep re-querying the corpus for this specific shape.

### Prior progress
`Q_min := Nec ∪ R(a_1)` (Nec-Necessity Lemma, `nec-necessity.md`) is the sharpest necessary-condition
candidate; the Contamination Dichotomy Lemma + Reduction Proposition
(`contamination-dichotomy-and-reduction.md`) localizes the Bounded-Witness-Index question to a per-prime
search, but both builder and reviewer correctly assessed this reduction as not strictly easier than the
original gap (no unconditional independence/density statement bridges the localized question). Nothing in the
population has yet attempted the specific CRT-positive-density framing (opening 1 above) or the
generalized Multiple-of-r Realization Lemma for r ∉ R(a_1).

### Dead ends (do not retry)
All prior dead mechanisms from run_state.md's Rules stand (10 total): S-finiteness, bare pigeonhole on σ(1),
g(Q)-threshold, prime-size threshold, Λ-split tautology, windowed-ε automaton, Q={p≤rad(a_1)} closed form,
chain-transitivity, Redundancy Growth Lemma (ρ(n)≥2), odd-anchor + weak-fallback parity mechanisms,
single-affine-rate majorization. Additionally this round: **do not propose "positive CRT density of
uncontaminated multiples of r" as a finishing move by itself** — it is a real, correct fact (elementary), but
it only speaks to integers, not to which integers the GREEDY rule actually selects and at what index; treating
it as a proof without a realization lemma bridging it to the actual sequence would repeat exactly the
circularity `contamination-dichotomy-and-reduction.md` already flagged.

### Small-case / intuition notes (all conjecture/evidence, not proof)
- Ran fresh independent numeric sweeps (Python, exact-integer greedy simulation + `sympy.primefactors`,
  20 random 2–5-prime seeds up to 4400 terms deep for Nec-stabilization, 60 more random 4-prime seeds for
  witness-index tail behavior): confirms round 5–6's finding that |Nec\R(a_1)| is small (0–3) in typical
  cases and Nec stabilizes early and does not regrow between 200 and 400 terms in any of the 20 seeds tested
  this round (reproducing, not just citing, the prior "stabilizes early" pattern).
- **New finding (heavier tail than previously recorded):** a systematic random search over 4-prime squarefree
  seeds found **a1 = 35409 = 3·11·29·37** with witness index **95** for the recruited prime **23** (verified
  directly: `first-witness-indices` computation, seq[:10] and factorizations checked programmatically) —
  **larger than the previously-recorded worst case a1=20735 (index 69)**. This is evidence (not proof) that
  the tail of the witness-index distribution is heavier than round 6's numerics suggested, and that a
  "small/bounded-by-a-simple-function-of-ω(a1)" closed form for the Bounded-Witness-Index Conjecture is
  increasingly implausible — worth flagging explicitly to the outliner: **do not assume the witness-index tail
  is short just because most random seeds give small values; the maximum found is still growing as search
  effort increases (69 → 95 across two rounds of ad hoc + randomized search), which is itself mild evidence
  against any simple uniform bound N(a_1) existing at all** (though it remains equally consistent with a bound
  that just grows slowly/adversarially with ω(a_1) or similar — not disproof of the Conjecture, just evidence
  against an easy closed form).
- Nec\R(a_1) size shows no clean correlation with ω(a_1) in this round's data (ranges 0–3 regardless of
  ω(a_1) ∈ {2,...,5}), consistent with round 6's finding that no simple closed-form N(a_1)=f(ω(a_1)) holds.
