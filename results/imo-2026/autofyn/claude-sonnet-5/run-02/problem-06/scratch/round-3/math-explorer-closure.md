## imo-2026-06

### Lens
Structural/direct-proof lens: does the Finite Core Theorem's original S already
certify gap (†) for EXTENDED types via a self-referential/closure argument, so the
recruitment process (`covering-system-construction` Step 4c) needs zero further
rounds beyond S₀^(0) = Q ∪ S — with no genuinely new argument needed?

### Verdict up front
**The naive/trivial closure argument is FALSE and I can show exactly why it breaks.**
But a *sharpened* version of the "zero further rounds" conjecture is now much more
strongly supported computationally than before (13 seeds, |Q| up to 7, hundreds of
pairs including **non-canonical-vs-non-canonical** refinement pairs, zero violations)
— strong enough that the outliner should treat it as the primary target, but the
mechanism that would prove it is NOT simple inclusion/closure; a real, currently
unknown argument is still needed. I isolate one genuinely new, easy, unconditional
sub-lemma (F_{A,B} ∩ F_{B,A} ≠ ∅, proved below) that is real progress but — verified
computationally — is not strong enough by itself to force the result.

### How S is built (re-derivation, to locate exactly where closure could/couldn't work)
S = ⋃_{B∈𝒫} F_{A,B}-type witness sets, one canonical witness m_B per **base** type
B ∈ 𝒫 (`finite-core-theorem.md`). For a disjoint pair of base types A, B, the
Bounded Witness Lemma (applied with the *canonical* witness m_B) gives: every n with
τ(n) = A (base level, ANY extended refinement of A) has a_n divisible by some prime
of F_{A,B} := P(a_{m_B}) \ Q, fixed and ⊆ S. Since F_{A,B} ⊆ S ⊆ S₀ = Q∪S, this prime
lies in S₀, so it lies in ρ(n) = P(a_n) ∩ S₀ — i.e. **every** extended-persistent
refinement A' of A satisfies A' ∩ F_{A,B} ≠ ∅ (this exact deduction is already spelled
out in `covering-system-construction.md` Step 4, "What is fully proved at this
level" — I re-derived it independently and confirm it is correct). This is real,
already-certified content, symmetric in A,B: also B' ∩ F_{B,A} ≠ ∅ for every extended
refinement B' of B, where F_{B,A} = P(a_{m_A}) \ Q from A's canonical witness.

### Where the naive closure argument breaks
The tempting "self-referential" step would be: since F_{A,B} ⊆ S already reconciles
A (any refinement) with B's canonical witness, and F_{B,A} ⊆ S already reconciles B
(any refinement) with A's canonical witness, "S already contains everything needed"
and A' ∩ B' ≠ ∅ should follow "by closure." **This does not follow logically**: A'
meeting F_{A,B} and B' meeting F_{B,A} are two separate facts about two possibly
DIFFERENT primes; nothing forces the specific prime in A' ∩ F_{A,B} to also lie in
B', or vice versa, unless F_{A,B} (or F_{B,A}) is a singleton. I checked computationally
(`/tmp/sim3.py`) that |F_{A,B}| averages ~2–2.5 across all tested seeds (never
literally 1 in general), so the singleton shortcut is not available.

**New unconditional lemma found this round (easy, worth certifying):**
For disjoint persistent base types A, B with canonical witnesses m_A, m_B:
F_{A,B} ∩ F_{B,A} ≠ ∅. *Proof:* By Free Facts, gcd(a_{m_A}, a_{m_B}) > 1, so some prime
p divides both. If p ∈ Q, then p ∈ τ(m_A) ∩ τ(m_B) = A ∩ B = ∅, contradiction. So
p ∉ Q, hence p ∈ P(a_{m_B})\Q = F_{A,B} and p ∈ P(a_{m_A})\Q = F_{B,A}, giving
p ∈ F_{A,B} ∩ F_{B,A}. ∎ — I verified this holds with zero exceptions across 12 seeds
(`/tmp/sim3.py`, up to |Q|=7, 164 pairs for a1=4849845). **However**, this fact alone
still does NOT force A'∩B'≠∅ for arbitrary refinements: it only shows the two
*canonical-witness-derived* sets overlap, not that an arbitrary A' (which may pick up
a *different* element of F_{A,B} than the shared prime p) actually contains p, or that
an arbitrary B' contains p. I could not extend this to a full proof; flagging it as
the closest "almost-works" partial result I found.

### Direct computational test of the closure question itself
I ran a more targeted, larger-scale check than round 2's 10-seed pass — reused/
extended a script found cached in the environment and independently re-verified its
logic — that specifically isolates **non-canonical-vs-non-canonical** extended-type
pairs (i.e. pairs A', B' where NEITHER equals the extended type actually realized by
the canonical witnesses m_A, m_B — the hardest case for any "trivial closure via the
canonical witness" argument, since by construction the canonical witness pair is
automatically fine):
- 13 seeds, a_1 ∈ {1155, 2145, 3003, 15015, 255255, 35, 105, 15, 1001, 30, 210, 2310,
  4849845}, up to |Q| = 7 (a_1 = 4849845 = 3·5·7·11·13·17·19).
- Total non-canonical-vs-non-canonical pairs checked across all seeds: **~2500+**
  (e.g. 454 for a_1=1155, 424 for a_1=2145, 382 for a_1=1001, 218 for a_1=4849845).
- **Zero violations found in every case**, including the hardest |Q|=7 case.
- I also tested the literal "inclusion/closure" hypothesis directly — "does F_{A,B}
  (the set that certifies the BASE-type pair) sit inside every extended refinement
  A' of A?" — and it **fails the vast majority of the time** (e.g. 27/32 failures for
  a_1=1155, 26/26 for a_1=255255, 20/20 for a_1=4849845). This conclusively shows the
  literal/trivial closure mechanism (inclusion of the base-pair witness set in every
  refinement) is false as a proof method, even though the top-level conclusion (†)
  keeps holding anyway — meaning if (†) is true, it is true for a *different*,
  currently-unidentified reason, not because the base-type argument trivially lifts.
- I confirmed genuine refinement multiplicity is real (not a threshold artifact): for
  a_1=1155, base type {3} has 4 distinct extended-persistent refinements
  {2,3},{2,3,13},{2,3,37},{2,3,19}; for a_1=35, base type {5} has 9 distinct
  refinements including some without prime 2 (e.g. {3,5}, {19,3,5}). These are
  genuinely different S-subsets recurring, not junk-prime noise (junk primes outside
  S₀ are excluded by ρ's definition).

### Distinct openings for the outliner
1. **Sharper "zero-round" conjecture, now much better evidenced** — target (b) from
   `current.md`: prove S from the Finite Core Theorem needs literally zero
   recruitment rounds. Now supported by ~2500 non-canonical pair checks up to |Q|=7,
   not just the original 10-seed/|Q|≤4 evidence. Still not proved; the mechanism is
   NOT simple inclusion (disproved above), so a real argument is needed — possibly a
   *simultaneous* multi-way pigeonhole across ALL disjoint partners of a type at once
   (rather than one witness per pair) that forces some invariant subset of F_{A,B}
   across ALL of B's own disjoint partners to coincide with what A's refinements pick
   up — this is speculative, not derived, but is the shape of argument that would be
   needed given the data (a "majority/robust glue" phenomenon: in the a_1=35 test,
   every refinement of every proper-base type contained at least one of {2,3}, and one
   base type's refinements always contained BOTH — worth checking whether that
   asymmetry is itself forced).
2. **F_{A,B} ∩ F_{B,A} ≠ ∅ lemma** (proved above, unconditional, certifiable) — real
   new content, a genuine (if insufficient alone) piece of the puzzle; recommend
   certifying it as a lemma so future rounds don't have to re-derive it, and so a
   future attempt to strengthen it (e.g. show the shared prime p is *always* the one
   picked up by every refinement, which computational spot-checks above suggest is
   FALSE in general since |F_{A,B}|>1 refinements can use different primes) is not
   wasted re-deriving the base fact.
3. **Give up on trivial closure, attack termination via a genuine counting/exchange
   argument** instead, using the newly confirmed fact that refinement multiplicity is
   bounded (|𝒫'| / |𝒫| ratios observed: 70/15, 41/17, 35/11, 39/15 — roughly a
   constant multiplicative factor of 2–4, not exploding factorially) — this bounded
   "branching factor" might be the right quantity to feed into an exchange/counting
   argument for why non-canonical refinements can't actually escape the canonical
   linking prime, rather than trying to prove literal inclusion.

### Candidate technique(s)
Pigeonhole (already exhausted at the base-type/witness level); the remaining gap
needs either (a) a genuinely new double/simultaneous pigeonhole across all of a
type's disjoint partners jointly, or (b) an exchange/minimality argument showing a
"rogue" non-canonical refinement lacking a common prime with some partner would
force a contradiction via the Bounded Gap Lemma (candidate integers of the missing
combination would have to be systematically skippable, contradicting minimality of
the greedy choice) — this exchange-style idea was NOT explored by either built
approach this round and might be worth a dedicated approach.

### Cheap-kill candidates
None obvious for disproving (†) — the data now strongly disfavors a counterexample.
For proving it: check whether |F_{A,B}| = 1 in some restricted regime (disproved in
general, avg ~2); check whether the "majority glue prime" (e.g. one fixed prime
dividing EVERY extended-persistent type, not just proper-base ones) might hold even
though the OLDER "universal glue prime for proper types" claim was refuted — in the
a_1=1155 test all 20 persistent extended types (including ones with base type = full
Q) contained prime 2, but in the a_1=35 test this failed (several persistent extended
types of base type {5} did NOT contain 2, e.g. {3,5}, {19,3,5}) — so a universal
single glue prime across the WHOLE extended-type family is also not a safe bet in
general; do not resurrect that exact claim (already refuted once this run for the
base-type version).

### Knowledge-base entries to use
Pigeonhole / extremal principle; Modular arithmetic, CRT (for Step 5's finish, already
in use). No new KB entry identified as a silver bullet for the closure/termination
gap specifically.

### Analogous past problems (cruxes)
Searched `number_theory` subtopics `pigeonhole`, `divisibility-and-gcd`,
`sequences-and-recurrences`, `invariants-and-monovariants` for "covering system /
witness / closure / fixed-point" flavored cruxes.
- **aimo-0447** ("gcd(a+i,b+j)>1 for all i,j in a grid ⟹ min(a,b) large"): uses a
  prime-covering-grid pigeonhole (each cell gets a prime dividing the pairwise gcd,
  then bounds how many cells one prime can cover) — same *flavor* as our "type =
  divisibility pattern" bookkeeping, but its crux move (bounding grid coverage by
  prime density / PNT estimates) targets a **size** bound, not a **periodicity/
  closure** question, so it is analogous only in general technique family (gcd-driven
  covering by primes), not in the specific gap. Worth reviewing if the outliner wants
  a density-style fallback, but does not directly solve (†).
- **aimo-0421** (infinite set with a pairwise-gcd anomaly ⟹ find a specific gcd
  pattern among 3 elements): uses "gcd with a fixed element takes finitely many
  values, pigeonhole over an infinite family" — same base mechanism as our
  Persistent-Type Pigeonhole, already fully exploited by the existing approaches; not
  a new lever for the closure question.
- **aimo-0212** (rad(f(n)) | rad(f(n^rad(n)))): its crux "every prime dividing a
  polynomial's values lies in a fixed finite set, hence the polynomial is constant" is
  structurally the closest thing to a "finite core forces global behavior" argument
  in the corpus, but it is a fundamentally different setting (polynomial values, not
  a greedy gcd-legality sequence) and its finiteness-forces-triviality mechanism does
  not transfer.
- **Conclusion: no crux in the corpus directly resembles the specific closure/
  termination question about witness-recruitment for a greedy pairwise-gcd sequence.**
  This appears to be a genuinely novel argument that must be constructed from
  scratch, not adapted from a known crux.

### Prior progress
See `current.md` — Finite Core Theorem, Generalized Bounded Witness Lemma (S₀-level)
and its Recruitment Corollary are certified and unconditional. Gap (†) reformulated as
recruitment-process termination; conjectured (not proved) to terminate in zero further
rounds.

### Dead ends (do not retry)
- "Universal Glue Prime Lemma" (single prime dividing all proper-base-type terms) —
  refuted (a_1=35, `{5}` type has infinitely many odd terms).
- "cost(n) ≤ 1 in sparse regime" — refuted, same counterexample.
- **NEW this round:** the literal "F_{A,B} (base-pair witness set) ⊆ every extended
  refinement of A" inclusion hypothesis — refuted computationally (fails 80–100% of
  the time across all 8 tested seeds); do not attempt to prove (†) via this specific
  mechanism.
- **NEW this round:** "a single universal prime lies in every extended-persistent type
  of the whole family" (stronger version of the already-refuted proper-type-only
  claim) — also fails (a_1=35 case has extended-persistent types without prime 2).

### Small-case / intuition notes (all conjectural)
- Refinement multiplicity (|𝒫'| vs |𝒫|) is real and empirically bounded by roughly a
  factor of 2–4, not exploding — consistent with the certified (but directionally
  unhelpful for termination) bound |𝒫'_{k+1}| ≤ 2|𝒫'_k| noted in
  `covering-system-construction.md`.
- Despite genuine refinement multiplicity and the failure of the literal inclusion
  mechanism, (†) has now survived ~2500+ non-canonical pair checks up to |Q|=7 with
  zero violations — the strongest evidence yet for the "zero further rounds"
  conjecture, but the mechanism proving it remains unknown; treat as conjecture, not
  established.
- F_{A,B} ∩ F_{B,A} ≠ ∅ (proved above) is a genuine small piece of unconditional
  progress, worth certifying, but confirmed (via the inclusion-failure data) to be
  insufficient alone to close (†).
