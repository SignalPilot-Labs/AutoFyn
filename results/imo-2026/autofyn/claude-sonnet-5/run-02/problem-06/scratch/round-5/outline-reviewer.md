## imo-2026-06 — outline review, round 5

### 0. Independent verification of the round's governing claim (before trusting anything else)

Round 4 closed on "V=∅ always with minimal witnesses, 18/18 seeds." This round's outline
is entirely predicated on math-explorer-singleton-hypothesis's claim that this is FALSE,
with 4 fresh counterexamples (a_1 = 187, 209, 247, 385). Given round 3/4's history of a
witness-selection bug in exactly this computation, I did **not** trust this claim from the
report — I reimplemented the whole pipeline from scratch (fresh trial-division sequence
generator, fresh τ/ρ computation, fresh minimal-witness search scanning n=1..N directly,
not from a tail window) and reran all four seeds independently.

Result: **independently confirmed, not a repeat of the round-3/4 bug.**

- a_1=187: my S₀={2,3,11,17} (matches explorer). Rogue pair ({17,2},{11,3}) found. Earliest
  witnesses n_A=6 (a_6=238=2·7·17), n_B=5 (a_5=231=3·7·11) — exact match to the explorer's
  reported indices/factorizations. F'={7} on both sides (Singleton Hypothesis holds).
- a_1=209: my S₀={2,3,5,11,19} (matches). |V|=6 rogue pairs (matches "6 rogue pairs"
  claim). Checked one pair: n=4 (a_4=231=3·7·11) vs n=70 (a_70=1330=2·5·7·19), F'={7} both
  sides — matches explorer's data exactly.
- a_1=247: my S₀={2,5,7,13,19} (matches). |V|=14 (matches). Checked one pair: F'={3} both
  sides, singleton — matches explorer's finding (different specific witness indices within
  the pair set, same prime, same conclusion).
- a_1=385: my S₀={2,3,5,7,11,13} (matches exactly). V≠∅ confirmed (I found a different
  specific rogue pair than the explorer's, but same conclusion: V≠∅, singleton F'={19}).

**Conclusion: round 4's "V=∅ always" is genuinely, independently reconfirmed false.** This
is not the round-3/4 witness-selection bug — my minimal-witness search scans the full
index range from n=1, matching the certified Finite Core Theorem convention exactly. The
outliner's governing correction is sound and every downstream approach correctly builds on
"V≠∅ in general; recruitment is genuinely sometimes needed" rather than re-chasing the
false "zero rounds" target. Good catch by the explorer, good judgment by the outliner not
to repeat round 4's mistake of pinning "solved" on a lucky small sample.

### 1. covering-system-construction (revise) — APPROVE (build)

Correctly re-scopes to process-termination (not "V=∅ always"). Step 4's "Simultaneous
Resolution Lemma" attempt (one recruited prime resolves ALL currently-rogue pairs, so ≤1
round ever suffices) is honestly framed as new/unproved, with a concrete mechanism sketch
(shared small-index witnesses) and explicit small-sample caveat (2/2 multi-pair instances).
This is a legitimate, testable target — my own recomputation above adds one more
consistent instance (a_1=247: single prime 3 resolves all 14 pairs) without contradicting
it, so its empirical support actually got stronger this round, not weaker. Step 5's
fallback (bound total rounds via a monovariant) is appropriately flagged as unexplored, not
hand-waved as automatic. No missing cases beyond what's flagged (2+ rounds genuinely
unobserved but honestly left open, not assumed impossible). No dead-end reuse.

### 2. greedy-exchange-cost-potential (revise) — APPROVE (build)

Correctly drops the a_1=175 citation (per round 4's correction) and replaces it with the
freshly-reverified 187/209/247/385 data (which I independently reconfirmed above). Step 3's
Singleton Hypothesis attempt is a genuinely new mechanism (index-minimality of n_B, not
value-minimality of a_{n_B} — explicitly distinguished from the failed rounds-2/3 exchange
attempts). The stated gap ("showing no smaller legal integer exists" for the witness index)
is precise, not hand-waved. Fallback (Step 5, bounded-but-not-1 F') is a reasonable
degradation path if Step 3 only partially succeeds. This directly complements
covering-system-construction (Singleton-Hypothesis-in-general vs. simultaneous-resolution)
— genuinely different sub-targets on the same reopened crux, not a restated duplicate.

### 3. witness-index-descent (new) — APPROVE (build)

Genuinely different proof STYLE (well-ordering/minimal-counterexample descent over ALL
rogue pairs across the whole process, vs. forward round-by-round induction in the other two
approaches) — this is real technique diversity per CLAUDE.md, not a same-gap bypass wearing
a new label (checked against memory rule 11's warning: the target object here, "the minimal
rogue pair over the whole eventual process," is not the same skeleton as covering-system-
construction's stage-indexed recruitment, since it never fixes a stage in advance). Step 2
(ordering sub-lemma) and Step 3 (descent contradiction) are both honestly flagged as
unproved, with Step 3 explicitly disclosed as "the crux, genuinely unfinished — explorer
could not complete it." This is acceptable for a build-set entry per CLAUDE.md (an
incomplete approach with explicit gaps is a valid population member) as long as the
skeleton up to the gap is sound, which it is: Steps 1 (well-ordering setup) and the
WLOG relabeling are standard and correct. Does not reuse the documented dead-end
(|A'|+|B'| size-measure descent, round 3) — uses witness-index min(n_A,n_B) instead, a
genuinely different well-ordering.

One instruction to the builder: Step 2's claim "min(n_A,n_B) ≥ max(m_A,m_B)" needs to be
checked against a seed where a canonical witness is NOT small — the outline only cites 2
tested seeds (small sample, per memory rule on cardinality-only/small-sample claims) and
"empirically m_B=1-4 in every tested seed" is exactly the kind of claim that has been
falsified before in this project when tested on a wider seed set (e.g. memory rule 8). This
is a CHANGES-REQUESTED-level caveat within an otherwise approvable outline — record it, do
not treat Step 2 as safe until re-tested on 5+ more seeds including some with larger |Q|.

### 4. reversible-transition-map (new) — CHANGES REQUESTED (build, with a mandatory first checkpoint)

I independently probed whether Step 3 (injectivity of the "smallest legal successor" map on
the finite state σ(n) = (a_n mod M, small-prime-membership)) is secretly gap (†) restated,
per the outliner's own flagged risk. My assessment: this risk is real and probably
underestimated by the outline. Legality of a candidate at index n depends, in the greedy
rule's literal definition, on gcd > 1 with EVERY prior term a_1,...,a_{n-1} — the entire
content of the Finite Core Theorem / recruitment machinery exists precisely to show this
reduces to a FINITE, state-summarizable condition once n is large. Whether σ(n) as defined
(a fixed finite window of prime-membership plus a residue) actually IS a sufficient
statistic for legality is not a lesser question than gap (†) — it plausibly requires knowing
that two extended-persistent types with different σ cannot mimic each other's future
legality, which is close to reconciliation/intersection content. The outline itself flags
this ("must be checked explicitly, not assumed favorable") which is the right level of
honesty, but I want to raise the bar: the builder's FIRST deliverable, before writing any
further steps, must be a direct comparison — spell out concretely whether "σ(n) determines
the legality set" is logically equivalent to, strictly harder than, or strictly easier than
V=∅ / gap (†) as certified. If it turns out equivalent or harder, this slug should self-
report a RETHINK-level finding next round rather than continue polishing a restatement.
Keeping this in the build set is worthwhile because of the two-birds payoff (would also
resolve the untouched "periodicity from n=1 literally" secondary gap) and because CLAUDE.md
explicitly calls for a genuinely different framing when a field plateaus on one shared gap
(true here — gap † / its descendants have been the sole crux since round 1). But this is
CHANGES REQUESTED, not a clean APPROVE, because of the disambiguation obligation above.

### 5. Population notes (unchanged from outliner, confirmed correct)

- witness-depth-bound: RETHINK stands (proven scope-mismatch from round 3, no new
  information this round) — correctly excluded from build set.
- amortized-charging-budget, density-sieve-contradiction, hypergraph-transversal: correctly
  left stale/untouched; no new mechanism surfaced for them this round.
- No approach in this round's field repeats a documented dead end (checked against: round-2
  universal-glue-prime/cost≤1 — not reused; round-3 |A'|+|B'| descent — not reused by
  witness-index-descent; round-4 PUCL / "V=∅ always" — explicitly retracted and not
  restated by any of the four).
- No copy_approach needed this round — no approach proposed branching one line into two
  sibling paths on the same gap.

### 6. Diversity assessment

The four build candidates are NOT all variations of one framing: covering-system-
construction and greedy-exchange-cost-potential share the recruitment-process target but
attack complementary sub-claims (simultaneous-resolution vs. singleton-hypothesis-in-
general) with different mechanisms; witness-index-descent uses a structurally different
proof architecture (global well-ordering vs. staged induction); reversible-transition-map
is the furthest from the pack (bijection/state-space, no recruitment language at all) but
carries a real risk of collapsing into the same gap, flagged above. This is a healthy,
non-collapsed field — better diversity than round 4's two-approach population.

### Ranking

Registered `witness-index-descent` and `reversible-transition-map` (cold start). Ranked the
full field head-to-head via `update_ranking`, anchoring: the dead-end `witness-depth-bound`
loses to every live sibling; `covering-system-construction` and `greedy-exchange-cost-
potential` (both revived/strengthened this round, highest development) draw with each other
and beat the two new entries and the stale trio; `witness-index-descent` (more concrete
partial mechanism, lower circularity risk) edges out `reversible-transition-map` (higher
risk, entirely open). Resulting Elo: covering-system-construction ~1688 (leader),
greedy-exchange-cost-potential ~1651, witness-index-descent ~1521, reversible-transition-map
~1493, witness-depth-bound ~1437 (dead-end), amortized-charging-budget ~1426,
density-sieve-contradiction ~1398, hypergraph-transversal ~1387.

### Build set rationale

All four candidate approaches are legitimate, non-duplicate, adversarially checked, and
target genuinely different sub-problems or framings of the reopened crux — no wasted build
slot on a repeated dead end or fake-diversity technique variant. Given CLAUDE.md's explicit
instruction to counter a multi-round shared-gap plateau (true here) by putting at least one
genuinely-different-framing approach on the table, and given the population here has only 4
live, well-differentiated candidates (the other 3 are correctly stale), I am recommending
all 4 for this round's build rather than trimming to the "normally 1-3" default — trimming
would mean either dropping the plateau-breaking reversible-transition-map (against the
explicit CLAUDE.md guidance) or dropping one of the two complementary, freshly-revived
recruitment-process attacks (wasteful given this round's correction just re-validated both
as directly load-bearing).

build set: covering-system-construction, greedy-exchange-cost-potential, witness-index-descent, reversible-transition-map
