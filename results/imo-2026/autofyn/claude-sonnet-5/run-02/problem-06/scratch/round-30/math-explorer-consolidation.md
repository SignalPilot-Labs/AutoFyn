## imo-2026-06 (consolidation/audit lens)

### 1. Master Conditional Theorem chain — re-verified, still gap-free
Traced the full citation chain myself, reading each cited lemma file in full (not
just current.md's prose):

Free Facts (`free-facts-gcd.md`) → Persistent-Type Pigeonhole
(`persistent-type-pigeonhole.md`) → Finite Core Theorem (`finite-core-theorem.md`)
→ Extended Persistent-Type Pigeonhole (`extended-persistent-type-pigeonhole.md`,
re-applicable at any finite core S ⊇ Q, confirmed by its own certification note) →
**Self-Absorbing Core Theorem** (`self-absorbing-core-theorem.md`, conditional on
(i) a self-absorbing S* existing, (ii) FAH holding at level S*) → **Universal Early
Intersection Lemma** (`universal-early-intersection-lemma.md`, unconditional, only
uses Free Facts + the definition of persistence — verified its proof line by line:
"pick m≠j in an infinite index set" is valid, gcd(a_j,a_m)>1 gives the shared
prime, self-absorption puts P(a_j)⊆S*) → **Literal n=1 Periodicity Theorem**
(`literal-n1-periodicity-theorem.md`, extends the conclusion to n≥1 under the
*same* two hypotheses, no new one smuggled in — checked its three sub-steps
(Sufficiency/Landing/Assembling) against the parent theorem's proof and confirm
none silently strengthens the hypothesis). **Termination Criterion Lemma**
(`termination-criterion-lemma.md`) is a fully unconditional iff (absorption
terminates ⟺ (N(S_k)) bounded) — verified both directions myself (⟹ is a
one-line finite-max; ⟸ builds a genuinely k-independent fixed set P*_M from
a_1,...,a_M, so the induction is not circular). **Monotonicity of Resolution**
(`monotonicity-of-resolution.md`) is a correct, one-line permanence-of-intersection
fact used to justify that FAH-resolution achieved at any stage survives to later
stages — it is NOT used to (falsely) derive S*-level FAH from S₀-level FAH; it only
says resolution, once achieved, persists.

**No gap found in the chain.** Every conditional step's hypothesis set is exactly
{H1: FAH holds at level S* (self-absorbing core), H2: the absorption chain
S₀⊆S₁⊆... terminates}, and given both, the Literal n=1 Periodicity Theorem finishes
the proof unconditionally. This matches current.md's own claim and I confirm it
independently re-derives correctly — the "gap-free" characterization is accurate,
not overclaimed. Note H1 as officially defined ("FAH at S*") is proved (in
`self-absorbing-core-theorem.md`'s precision note) to be exactly equivalent to
standard disjoint-base-type FAH — so H1 is genuinely the same crux as the
workspace-wide FAH question, not a disguised stronger/weaker one. This equivalence
argument is itself correct (one line: non-disjoint-base-type pairs intersect for
free via Q⊆S*, ρ_S(n)∩Q=τ(n)).

### 2. Consistency of the 10 certified subfamily theorems + staleness of current.md structured sections
All 10 subfamily theorem files (`2|a_1` via `even-seed-literal-periodicity-theorem`;
`a_1=p^k` via `prime-power-seed-literal-periodicity-theorem`; `a1-3q`; `a1-3q^2`;
`a1-3q^3`; `a1-3aq` a=1..5; `a1-5q`; `a1-7q`; `a1-11q`; `a1-13q`; `a1-17q`) use a
**uniform template**: "literal T=1, L=p periodicity from n=1, for every prime
q > p outside an explicit finite Bad(p)". Checked the Status headers of
a1-5q/7q/11q/13q/17q myself — all state this identically (only Bad(p) and the
bound on q differ), confirming they really are one mechanical template
instantiated at p=5,7,11,13,17, exactly as current.md's Status section (top,
round-27–29 prose) describes. This part is accurate and NOT stale.

However, two of current.md's *other* structured sections ARE stale and should be
flagged:
- **`## Approaches tried`** (line 1704): the entry list is in reverse-chronological
  order but **stops at round 20** — none of the round 21–29 verdicts (7 more
  APPROVEs: a1-7q, a1-11q, a1-13q, a1-17q, plus the Universal Look-Back machinery,
  the two hard-seed closures, the bipartite-network RETHINK) are appended as
  discrete entries in this section. The information exists (in the huge Status
  narrative at the top, lines 1–337), but the dedicated per-round bookkeeping list
  has not been kept current since round 20 — 9 rounds of drift.
- **`## Current best`** (line 2022): explicitly headed "Round 16 update... supersedes
  the framing below" — this section's substantive content (the two-piece split:
  `2|a_1` solved, `a_1=p^k` solved, general case reduced to H1/H2) is still
  *logically* accurate as a top-level picture, but it does not mention or link to
  any of the 7 additional certified subfamily theorems (a1-3q/3q²/3q³/3aq/5q/7q/
  11q/13q/17q) proved in rounds 22–29. A reader consulting only `## Current best`
  would see a 3-item picture (2|a_1, p^k, H1/H2-conditional) and miss that the
  actual certified floor is now 10 named subfamilies. This is a real
  write-up/completeness gap (not a mathematical one) — the accurate up-to-date
  picture only lives in the free-form Status prose, not in the section a future
  reader is directed to by the file's own contract structure.
- There is also no `## Next-round guidance` section past round 14 (last one at
  line 3675) — guidance since round 15 is folded into Status prose only, another
  structural (not mathematical) staleness marker.

### 3. Low-hanging generalization check — a1-pq uniform machinery
Read `approaches/a1-pq-subfamily-theorem.md` in full (1315 lines). The certified
general-`p` machinery (Generalized K₀-Boundedness, gcd-difference Witness Lemma,
Legendre Sieve Gap Bound, Primorial Floor Bound, Universal Look-Back Witness
Identity, Universal Look-Back Closed Form + r=1-Uniqueness Theorem) is genuinely
`p`-uniform and already reduces each new `p`'s closure to: (a) build the
`(s_0,K_0)` table (mechanical, `sympy.mod_inverse`), (b) find below-threshold
`(j,r,q)`/`(j,r,k,q)` candidates via the sieve threshold, (c) resolve each via a
gcd witness, leaving a finite exceptional set `Bad(p)`. This is exactly why
p=5,7,11,13,17 all closed with "the same template, different numbers" — each
required a genuinely new *finite computation* (differing `Bad(p)`, differing
below-threshold cell counts) not covered by any single existing certified
statement.

**Conclusion: there is no free win here.** A "uniform theorem: holds for all
p ≤ N" packaging is NOT available cheaply for two reasons: (i) the two residual
gaps flagged in the file — the `k≥1, gcd(k+1,j)>1` residual for `r=1` (round-27
open), and the general `r≠1` `k=0`-layer closure (needs the same per-p sieve
work as before, not shortcut by the r=1 Uniqueness Theorem) — are open **for
every p simultaneously**, i.e. they are not resolved by doing more p-instances,
they are p-independent algebraic sub-questions still unsolved in general; (ii)
extending the certified floor to a NEW prime (e.g. p=19,23) costs the same
per-p finite-computation effort as p=17 did (a full round each, per the round
26–29 pattern) — it is not "free" relative to what's already been done, just
more of the same repeatable work. So neither "prove uniformly for all small p"
nor "cheaply extend to p=19" is a low-hanging fruit distinct from what rounds
26–29 already executed one at a time.

The one genuinely low-hanging **non-mathematical** consolidation available: the
5 near-identical subfamily-theorem approach files (a1-5q/7q/11q/13q/17q) could be
merged into a single "p-uniform instantiation" write-up citing one shared proof
template plus 5 small per-p data tables — this would improve deliverable
*clarity* but adds no new certified content and does not touch H1/H2.

### 4. Recommendation for round 30 build-slot allocation
Given 23 plateau rounds on H1 with 32+ confirmed-dead FAH mechanisms, and the
staleness identified in point 2 being purely presentational (the Status section
already has the accurate live picture; only two secondary bookkeeping sections
lag), I recommend:
- **Do NOT spend a full build slot purely on housekeeping.** The staleness is
  real but low-stakes (current.md's Status section, which a reviewer/outliner
  reads first, is accurate and current; the lagging sections are secondary
  indices). A light-touch fix (appending the 9 missing round-21–29 entries to
  `## Approaches tried` and updating `## Current best`'s bullet list to name all
  10 subfamilies) could be done as a small addendum by whichever approach's
  builder/reviewer touches current.md next, not as a dedicated slot.
- **Spend the round's real effort on breaking the H1 plateau with a genuinely
  new framing**, per the run's own standing rule (23 consecutive plateau rounds
  is well past the "3+ rounds ⟹ direction is wrong" threshold). The
  `bipartite-network-invariant-fah` RETHINK this round (round 29) is itself
  evidence the graph/network-invariant framing, adapted from crux aimo-1000,
  collapses into already-known-insufficient content — so the next FAH attempt
  should deliberately avoid: (i) any "single shared prime"/graph-connectivity
  reduction (already shown insufficient via Generalized Bounded Witness Lemma),
  (ii) anything reducible to the already-open H2 termination question (the
  now-standard trap this round's Reading β fell into), (iii) integer
  monovariant/difference-identity attempts (16th dead mechanism, round 14,
  diagnosed as structurally poisoned by "class-blindness" for ANY purely
  numeric statistic).
- **A second, smaller build slot on extending the a1-pq per-p floor (e.g. p=19
  or p=23)** remains valid "more of the same" progress but should not be the
  round's sole content, since it does not move the general-case needle at all
  (H1/H2 untouched) — treat it as a background/secondary slot, consistent with
  how rounds 26–29 ran one new-p closure alongside other work.

### Distinct openings surfaced by this audit (for the outliner)
- A structural audit opening: `fah-counterexample-hunt` (round 21+) already
  exists as the workspace's one genuinely different top-level target — hunting
  for an actual FAH counterexample (disprove) rather than another positive
  mechanism (prove). Its Status is `unsolved` and no counterexample has been
  found through round 22+ on `|Q|≥3`/CRT-lopsided/high-`ω(a_1)` seeds, but it
  is under-sampled relative to the ~32 dead positive-mechanism attempts. If
  the field keeps producing dead positive mechanisms, this file (and pushing
  its adversarial search further/deeper, e.g. targeting seeds specifically
  designed to defeat the Self-Absorbing Core/Universal Early Intersection
  machinery's implicit assumptions) is the one existing approach genuinely
  "far from the current field" per the plateau-break rule, rather than a
  brand-new slug.
- A packaging opening (cheap, no new math): unify a1-5q/7q/11q/13q/17q into one
  "p-uniform subfamily instantiation" theorem statement citing the shared
  certified machinery once, with per-p tables as data appendices — improves
  deliverable quality, does not require a dedicated round.

### Candidate technique(s)
No new technique recommended by this audit lens (audit-only); for H1, the
run's own diagnosis stands: the a1-pq machinery is p-uniform but its two open
residuals (general r≠1 k=0 closure; r=1 k≥1 gcd(k+1,j)>1 residual) are
algebraic, not computational-per-p, and remain the correct place to look for a
genuinely new idea (e.g. a symbolic closed form for r≠1 mirroring the certified
r=1 Universal Look-Back Closed Form).

### Cheap-kill candidates
None new found this round (audit lens, not a fresh mechanism hunt).

### Knowledge-base entries to use
Not separately consulted this round (audit lens on current.md/lemmas only, per
dispatch); prior rounds already cite the relevant generic theorems (CRT,
pigeonhole, Legendre sieve) inside the certified lemma files.

### Analogous past problems (cruxes)
Not queried this round (dispatch scope was current.md/lemma audit, not fresh
crux search); the workspace's own citation of aimo-1000 (bipartite-network
lens, round 29) was independently spot-checked against the earlier prose and
found to be accurately characterized as already-known-insufficient — no new
crux recommendation from this audit.

### Prior progress
10 certified subfamily theorems (see above), Master Conditional Theorem
(gap-free, re-verified again this round), H1 (FAH) and H2 (absorption-chain
termination) both open, 23rd/24th consecutive plateau round on H1, 32+
confirmed-dead FAH mechanisms.

### Dead ends (do not retry)
All previously logged dead FAH mechanisms stand (32+, see current.md Status
section for the full enumerated list); the "zero further recruitment rounds"
conjecture (refuted, a_1=175); Minimal-Window Necessity Conjecture (open, not
dead, but stuck); bipartite-network-invariant-fah's two readings (both
collapse to known-insufficient content, round 29, independently re-confirmed
by this audit's reading of the prose — did not re-derive Propositions A–D
myself line-by-line, only cross-checked the citations, so treat that specific
re-derivation as builder/reviewer-verified, not re-verified by this lens).

### Small-case / intuition notes
No new numerics run this round (audit lens); prior rounds' extensive numeric
verification (778+ primes for a1-11q, 2000+/2500+ primes for a1-13q/17q, 45000+
term simulations for the two hard rogue-pair seeds) stands as previously
independently reproduced by the proof-reviewer, per the Status section — I did
not re-run any of these myself this round, only audited the written chain and
cross-references.
