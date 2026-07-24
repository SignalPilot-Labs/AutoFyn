# Outline review — round 23 (imo-2026-06)

Note on process: none of the three named new/lower-priority approaches
(`a1-3qk-subfamily-theorem`, `direct-s0-self-absorption`,
`a1-5q-subfamily-theorem`) had a physical `approaches/<slug>.md` file — the
outliner's report described them but did not write them (per standing rule
31, this recurs; the reviewer must seed the files itself). I transcribed
the vetted outline content into all three files before registering/ranking
them, so the builder has real context to start from.

## a1-3qk-subfamily-theorem — new — APPROVE (build this round)

Target: strict generalization of the certified, APPROVE'd `a1-3q-subfamily-
theorem` (a_1=3q) to `a_1=3q^m` for any fixed m>=1, same literal T=1,L=3
periodicity. The claimed mechanism is a near-verbatim transplant: the
certified proof only ever used `3|a_1` and `P(a_1)={3,q}`, both of which
hold identically for a_1=3q^m since `P(q^m)={q}` for every m>=1.

Checked:
- Technique is sound and is a genuine transplant, not a restatement of an
  already-solved case — m=1 is the certified theorem, m>=2 is new content.
- Case coverage matches the certified sibling exactly (odd n / even n Case
  (a) / Case (b) k=0 / Case (b) k>=1) — no missing case, and the outline
  correctly flags which steps are truly m-independent (2,3,4 — depend only
  on P(a_1)) versus which require genuine re-derivation because the actual
  integer values a_n depend on m even when the residue-class bookkeeping
  does not (steps 5,6,7 — the parity witness, the k=0 hand-checks at q=7,
  q=11, and the k>=1 residual table). This distinction is correct and the
  outline explicitly warns the builder not to skip the re-derivation —
  good, since a lazy "just replace q by q^m" pass would be a silent gap.
- I independently ran a fresh trial-division simulation of the TRUE greedy
  sequence (not reusing any outline-reported number) for a_1=3q^m at
  q in {7,11,13,17,19,23,29,31,37,41,43}, m in {2,3} (22 pairs, 150-250
  terms each): literal match against a_n=a_1+3(n-1) in every single case,
  zero exceptions. Extended spot-check to m in {4,5} for q in {7,11,13}:
  also exact match (6/6). Confirmed the q=5 exclusion persists for m=1,2,3
  (a_1=15,75,375 all correctly fail literal periodicity, matching the
  certified m=1 theorem's own documented exclusion mechanism). This is
  strong numeric support for the theorem statement itself; per this
  workspace's standing rule it does not substitute for the required
  re-derivation of steps 5-7, which the outline correctly still demands.
- Genuinely lower risk than most H1/FAH corridor attempts in this
  workspace's history: it needs zero new machinery (both cited lemmas,
  Legendre Sieve Gap Bound and Primorial Floor Bound, are already
  certified and stated generically in the modulus, with no a_1-specific
  content) and the only real work is bookkeeping re-derivation, not a
  fresh proof search.

No fatal flaw found. Open gaps are exactly what the outline states: (i)
re-verify the two k=0 hand-checks for general m, (ii) recompute the
residual k>=1 table for general m and confirm it is empty (or resolve any
nonempty entries by hand as the m=1 proof did), (iii) spot-check m=4,5
before finalizing the statement — already partially done above (6/6
clean), builder should extend a bit further if convenient but this is not
blocking.

**Verdict: APPROVE.**

## direct-s0-self-absorption — new — APPROVE (build this round)

Target: prove H2's existence hypothesis directly on the canonical core S₀
itself (plus a finite, explicit transient enlargement S₀'), rather than
via the confirmed-dead one-prime-at-a-time inductive chain
(`core-growth-monotonicity`'s Proposition 3, independently reverified dead
in round 16/19 — bounding M_B inductively hits the same non-constructivity
wall as N(S) itself).

Checked:
- Genuinely different framing from the dead chain-induction mechanism: the
  Proposition-3 impossibility is specifically about inductively bounding a
  quantity built up one recruitment step at a time from an a priori
  unknown starting point ("two consistent finite-prefix extensions" —
  applies to ANY inductive-in-k bounding attempt). This approach instead
  works directly on the single, already-fully-specified, finite set S₀' —
  a structurally distinct argument shape, not a relabeled instance of the
  dead mechanism. Confirmed by rereading the certified Prop-3 text (per
  memory rule 30's instruction to diff moving parts, not just names).
- Also targets H2, not H1/FAH — a genuine diversification of the field,
  which per CLAUDE.md matters: every other live approach this round
  (a1-3qk, a1-5q, covering-system-construction) either targets a
  restricted subfamily or the H1 corridor; this is the only H2-framed
  candidate on the table, and the field needs it (H1 has had 17+
  consecutive plateau rounds; an H2-side attack is a different wall).
- The outline is scrupulously honest about the central gap: step 4 openly
  states the natural mechanism (Bounded Witness Lemma) gives only "shares
  at least one prime with each disjoint witness," explicitly NOT "confined
  entirely to S₀'" — and flags this exact trap by name, citing the
  round-2/round-22 precedent. This self-disclosure is the correct posture
  (per memory rule 11: escalate self-disclosed risk, don't just approve on
  the strength of a hedge) — but here the hedge is doing real work: the
  outline does not pretend step 4 closes the gap, and step 5 gives an
  honest, graceful, non-overclaiming fallback (report the precise residual
  question) if the direct route fails. This matches the workspace's
  established diagnostic-lemma precedent (Lemma F/Lemma I) — a legitimate,
  low-risk-of-wasted-effort shape for a new approach, since either outcome
  (real proof or precise negative diagnosis) is genuine progress.
- Step 2 (S₀' closes j<=N_0 trivially by construction) is correct and
  low-risk — a one-line unpacking of definitions, no gap.
- I did not attempt to independently pre-test step 3/4 numerically this
  round (it requires reconstructing the full S₀/N_0/N(S) apparatus from
  several chained certified lemmas — not a 10-minute check, unlike the
  a1-3qk/a1-5q numeric sanity checks above) — flagging this as the
  builder's first real task rather than something the reviewer could
  cheaply falsify pre-build.

No fatal flaw found; the approach is honestly scoped with a sound
fallback. **Verdict: APPROVE.**

## covering-system-construction — advance — APPROVE, not in this round's build set

Target unchanged: finish the concretely-scoped |F''|=2, multiplicity-1
divisor-class residual (`D_bad(q*)` collapsing to one class in the
standing test seeds, per the certified Reduced-Alphabet Corollary). This
is a legitimate, well-scoped continuation of the workspace's highest-Elo,
most-developed approach (11 rounds, Elo 1864.6) — no red flags in the
advance instructions, and the outline correctly warns the builder not to
let this turn into a 9th generic FAH-mechanism hunt if the divisor-class
question itself resists direct casework.

Given the round's ~2-approach build budget, I am prioritizing the two
approaches most likely to yield a concrete certified result this round
(a1-3qk, very close to a 4th APPROVE; direct-s0, the field's needed H2
diversification) over this incremental single-divisor-class finishing
task, which has been narrowed steadily for several rounds without
resolving the core FAH crux and is not itself flagged this round as
"nearly done." Kept live in the ranking (no penalty for being held out —
its Elo already reflects 11 rounds of real, verified progress); recommend
it for next round's build set if a1-3qk and direct-s0 both land cleanly,
or immediately if either stalls.

## a1-5q-subfamily-theorem — new (lower priority) — CHANGES REQUESTED, not in build set

Target: a second restricted subfamily, a_1=5q with q not in the excluded
set {7,13,19}, T=1,L=5 literal periodicity, via a structurally similar but
more complex (triple-band) generalization of the a1-3q mechanism.

Checked:
- I independently simulated the true greedy sequence for a_1=5q at q in
  {7,11,13,17,19,23,29,31,37,41,43,47,53} (13 primes, 250 terms each):
  literal periodicity fails at EXACTLY q in {7,13,19} and holds at every
  other tested prime — an exact match to the outline's claimed exclusion
  set, zero false positives/negatives. This is a real, useful pre-build
  confirmation (the outline's headline numeric claim is not a guess).
- The mechanism (Generalized Parity/gcd Witness across j=2,3,4, each
  needing its own residue-condition derivation, plus the same certified
  sieve/floor lemmas for the residual bands) is sound in shape and is a
  genuine, non-duplicate triple-band generalization — not the same content
  as a1-3q or a1-3qk under a different name (a1-3q/a1-3qk have exactly one
  intermediate offset to rule out since P(a_1)={3,q} leaves only j=2; a1-5q
  has three since P(a_1)={5,q} leaves j=2,3,4). Genuine extra casework, not
  a relabeling.
- However: the exclusion set was only confirmed to q=53; the outliner's
  own recommendation (a deeper sweep to q<300 before finalizing the
  theorem statement) is not yet done, and per rule 6 (bounded-by-parameter
  claims can hide magnitude-dependent surprises), a sweep to only 13 primes
  is thin evidence for "these are ALL the bad primes."
  This does not sink the approach, but it is a real open item, not a
  formality — three bad primes with no yet-stated explanatory mechanism
  (why exactly {7,13,19}?) is a weaker footing than a1-3q's fully-explained
  q=5 exclusion (window-size-1 argument).
- The approach is explicitly and correctly flagged by the outliner as
  lower priority relative to a1-3qk, and I agree: it needs 3x the fresh
  casework (three bands, each needing its own derivation) versus a1-3qk's
  near-verbatim transplant of already-proved machinery, for comparable
  eventual payoff (one more certified restricted subfamily). Not worth a
  build slot this round given the ~2-approach budget.

**Verdict: CHANGES REQUESTED** (viable, real content, registered and
ranked, held out of this round's build set for capacity reasons — build
next round if a1-3qk lands and a slot frees up, after first extending the
exclusion-set sweep to q<300 as the outline itself recommends).

## Diversity note

The build set (a1-3qk-subfamily-theorem, direct-s0-self-absorption) is
genuinely diverse in framing: one is a restricted-subfamily elementary
induction (no FAH/H1/H2 machinery at all, extending the run's floor
deliverable toward a 4th APPROVE), the other is a direct H2-only attack
using a fundamentally different argument shape than the dead inductive
chain. Neither shares a wall with the other, and neither shares the H1
corridor's 17-round plateau. This is a good round shape per CLAUDE.md's
plateau-breaking guidance — it does not merely bypass H1's wall in the
same framing, it opens ground on two orthogonal fronts (a concrete new
solved subfamily, and H2's existence half) while keeping the H1 leader
(covering-system-construction) alive in the ranking for next round.

## Ranking

Registered the three new approaches (a1-3qk-subfamily-theorem,
direct-s0-self-absorption, a1-5q-subfamily-theorem) at cold-start Elo
1500. Ran update_ranking anchoring each newcomer against established
approaches with clear evidence: a1-3qk beat triangle-critical-dichotomy-
witness (confirmed dead-end) and a1-5q (explicit lower-priority, more
casework for comparable payoff); a1-3q-subfamily-theorem (verified-
milestone, the certified sibling it generalizes) still edges a1-3qk
(unproved extension, real gaps remain) — correct, since a1-3qk is not yet
verified. direct-s0-self-absorption beat core-growth-monotonicity
(confirmed dead-end, same H2 target, inferior mechanism) and drew with
a1-5q-subfamily-theorem (both new, unproven, comparable risk profile,
different targets). a1-5q beat scalar-well-ordering-lock-in (confirmed
dead-end). All stale flags on touched approaches cleared.

build set: a1-3qk-subfamily-theorem, direct-s0-self-absorption
