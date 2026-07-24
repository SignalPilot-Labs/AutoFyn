# Outline review — round 8 (imo-2026-06)

Crux unchanged in substance for 3 rounds: FAH / Symmetric FAH (= Joint FAH for
q* := min(F'∩F'')). This round's field: two scoped revisions of the FAH mechanism plus
one genuinely new top-level framing (seed-coupling-induction), per the plateau rule.

## 1. covering-system-construction — Fixed-Witness Divisor-Chain (scoped)

**Verdict: CHANGES REQUESTED** (approved to build).

Checked the scoping is real, not a repackage of the falsified blanket claim or of any
dead mechanism.

- Numerically re-derived the falsification context: on a_1=175's non-rogue type
  {2,3,5} (S₀={2,3,5,7,13}), gcd(witness, later same-type term) takes 4 distinct
  values {30,60,90,180} over 788 occurrences — confirms the blanket "a_{n_A} | a_n"
  claim really is false on generic types, so the outline's own disclaimer is accurate,
  not a strawman excuse to justify rescoping.
- Independently tested the SCOPED claim on three actual rogue-pair witnesses
  (a_1=187: A'={3,11}, witness a_5=231, q=7 → 99/99 later occurrences have
  gcd(a_5,a_n)=231 exactly, zero exceptions; a_1=4807: A'={3,5,19}, witness a_6=4845,
  q=17 → 6/6 exceptions-free; a_1=209: A'={3,11}, witness a_4=231, q=7 → 205/205
  exceptions-free). In all three, d_n is not just divisible by q* but literally
  CONSTANT = a_{n_A} — stronger than the outline even claims. This is real,
  reproducible support for the scoped mechanism and clearly distinguishes it from the
  falsified blanket version (which fails precisely on non-rogue types where no single
  recruited prime is forced).
- Checked against the three named dead mechanisms: this pigeonhole is over divisors
  of a FIXED early integer a_{n_A} (never varies with n) — structurally distinct from
  joint Lemma-H branch analysis (dead: no link between two branch-(b) witnessing
  indices), Two-Witness Uniqueness (dead, same reason, retracted round 7), and
  Blocking-Data Bridging (dead: competitor's factorization uncontrolled relative to
  witness). Here the competitor object (d_n, a divisor of the SAME fixed a_{n_A}) has
  an exact, controlled relationship to the witness by construction — this is
  precisely the missing ingredient Lemma I's round-6 diagnosis called for. Not a
  repackaged dead mechanism.
- **Remaining risk (flag, not fatal):** the "open gaps" canonicality sub-step — ruling
  out an alternative prime r<q* as a genuine Joint-FAH candidate — is not obviously
  easier than FAH itself. As stated, Step 3 only shows r shares infinitely many
  A'-type terms; it does NOT yet show r is actually in F'∩F'' (i.e. also persistent on
  the B' side) — that half of "genuine alternative candidate" is asserted, not
  derived. Require the builder to either derive r ∈ F'' explicitly or narrow the claim
  to what's actually proved. This is real, non-trivial content, but the builder must
  not present it as closing the gap merely by producing r — treat it as still open
  until r's B'-side membership and the r-vs-q* ordering are both nailed down.

## 2. greedy-exchange-cost-potential — Occurrence-Order Induction

**Verdict: CHANGES REQUESTED** (technique direction sound, one concrete soundness gap
must be fixed before/while building).

- Confirms it genuinely sidesteps the certified Witness Discontinuity Obstruction:
  WDO is specifically about continuity of witness selection ACROSS recruitment stages
  (enlarging S₀); this induction never changes S₀ or the type A' — only the occurrence
  index k grows within one fixed core/type. No hidden recruitment-stage change found.
- **Found a real technical gap in the induction step**, distinct from (and in addition
  to) the shared canonicality question: Step 3 says the possible r_j values are
  "bounded (divisors of a_{m_{k+1}} itself, a FIXED finite integer for this step)" and
  then pigeonholes "since k can be taken arbitrarily large ... for large enough k
  pigeonhole forces some SINGLE prime r shared with infinitely many earlier a_{m_j}."
  This does not follow as stated: a_{m_{k+1}} is a DIFFERENT, growing integer for each
  k, so its divisor set is not a fixed universe across different k — pigeonholing
  across k requires a single fixed pool of candidate primes, which this construction
  does not supply (unlike the sibling's Fixed-Witness version, which correctly anchors
  to ONE unchanging a_{n_A} for all n). As stated this risks re-manufacturing a
  discontinuity issue (the repeated r could differ from step to step). The outline
  itself flags this exact risk under "Open gaps" ("verify Lemma J's exact statement
  actually supports being applied to bound {r_j} in this way ... don't cite blindly")
  — good, this was not glossed over, but it must be the builder's FIRST checkpoint,
  and the fix is straightforward: anchor to the fixed a_{m_1} (already available in the
  induction's own hypothesis j=1) rather than the growing a_{m_{k+1}}, which converges
  this mechanism onto the sibling's cleaner one.
- Confirmed the canonicality sub-step is IDENTICAL to covering-system-construction's
  (both files say so explicitly). Per memory rule #2/#7, do not have both approaches
  independently re-derive this same lemma this round — it wastes a build slot.

## 3. seed-coupling-induction (new) — plateau-breaking framing

**Verdict: APPROVE** (as the mandated genuinely-different framing this round).

- Confirmed genuinely different top-level route: induction on ω(a_1) across the
  family of seeds, not a reroute of FAH/Symmetric FAH. Base case (|Q|=1) is already
  fully certified. Induction is well-founded (ω(a_1') = ω(a_1) − 1 strictly, bottoms
  out at k=1) — no circularity.
- Ran the outline's own mandated cheap-kill check (Step 4) myself, one level further
  than "not obviously broken": for a_1=15 (Q={3,5}) vs the Q'={3}-projection, the
  divisible-by-3 subsequence of a_1=15's terms is NOT literally identical to a_1'=3's
  trivial sequence (a_{n+1}=a_n+3 always) — it has NON-constant gaps (3,6,6,6,6
  repeating with period 5) rather than a_1'=3's constant gap 3. This is exactly the
  qualitative shape the Seed-Coupling Lemma predicts (an eventually-periodic
  correction on top of the reduced sequence, not literal identity) — the toy example
  is consistent with the claim, not a counterexample. This does not prove the lemma
  (sample size is tiny, only ~30 terms) but clears the mandatory pre-build sanity gate
  the outline itself set — do not send to RETHINK on this evidence.
- The Seed-Coupling Lemma itself (Step 3) is not vacuous: its mechanism (Free Facts
  restricted to Q'-primes agrees between the two sequences except on a
  bounded-frequency p_k-dependent exception set, via the already-certified
  Generalized Bounded Gap Lemma) is a real, checkable claim, not a bare label.
  Untried anywhere in the corpus per the explorer — genuinely new content, worth a
  build slot.
- Caution for the builder: Step 4's cheap-kill check must be the FIRST deliverable,
  on at least 2-3 seeds with |Q|≥3 (not just the |Q|=2 toy case above) before
  investing in the general proof, exactly as the outline demands. If the collapsing
  correspondence breaks down on a larger example, report RETHINK honestly rather than
  forcing it.

## 4. Is the shared canonicality gap (approaches 1 & 2) secretly FAH restated?

Partially yes, and this should be tracked explicitly. The pigeonhole step in both
approaches only converts "FAH could fail" into "some specific alternate prime r
persistently shares with A'" — but ruling out r (showing q* is forced, or that no
smaller/independent alternative survives) is very close in strength to proving FAH's
own uniqueness content directly: if you could show "no prime other than q* can
persistently divide infinitely many A'-type terms," that is nearly equivalent to
proving Full Absorption for q* by elimination. This is genuine forward progress (it
localizes the open content to a crisp two-prime dichotomy using a new, correctly
anchored pigeonhole object — real value per Lemma I's diagnosis) but the builders must
not present closing the canonicality sub-step as a "smaller" task than FAH — budget
it as comparably hard, and report honestly if it turns out to require re-deriving FAH
in substance.

## Population housekeeping

- Registered `seed-coupling-induction` (new, cold-start Elo).
- Ranked the whole field via `update_ranking`: covering-system-construction and
  greedy-exchange-cost-potential remain the two strongest (both "advanced" last
  round, real certified content), covering-system-construction edges ahead this round
  because its Step 3 pigeonhole is correctly anchored while the sibling's has an
  unresolved anchoring gap (see §2). seed-coupling-induction anchored above all
  confirmed dead-end approaches (recruitment-round-charging, reversible-transition-map,
  scalar-well-ordering-lock-in, witness-depth-bound, witness-index-descent) and above
  the long-stale never-rebuilt approaches (amortized-charging-budget,
  density-sieve-contradiction, hypergraph-transversal), but below the two live
  leaders (it is untested beyond a toy cheap-kill check).
- No copy_approach requested this round — no approach proposed branching into two
  viable sub-routes.
- Confirmed `recruitment-round-charging` and `density-sieve-contradiction` correctly
  stay out of the build set (per outline's own "do not advance" note and round 6/7
  verdicts).

## Build set

Two build slots this round: the strongest live mechanism revision, plus the mandatory
new framing. `greedy-exchange-cost-potential`'s occurrence-order induction is held out
of THIS round's build set — its target open question (the canonicality sub-lemma) is
identical to covering-system-construction's, and it additionally needs the anchor fix
in §2 before its own pigeonhole is even sound; building both this round would
duplicate effort on the same lemma. It stays live in the ranking (CHANGES REQUESTED,
not RETHINK) and should be revisited once the anchor is fixed or once
covering-system-construction's canonicality sub-step is resolved (import, don't
re-derive).

build set: covering-system-construction, seed-coupling-induction
