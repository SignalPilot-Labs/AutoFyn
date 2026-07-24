## imo-2026-06 — round 2 outline review

### Key finding first (affects both build-set verdicts below)

I ran an independent numerical check of the round's central new claim — the
**Universal Glue Prime Lemma** (`covering-system-construction`, Step 4b, Case (i)):
"for n large with τ(n) ⊊ Q, p* := smallest prime not in Q divides a_n." The outline
and math-explorer reports claim this is "near-100% confirmed on 6+ seeds." Testing a
wider set of seeds (a_1 = 15, 35, 21, 33, 45, 105, 30, 210, 1001), I found it is **false**
for a_1 = 35 (Q = {5,7}, p* = 2): deep in the tail (checked n = 2000..4000), the
persistent proper-base-type {5} occurs with ODD terms hundreds of times (e.g. a_153 =
975 = 3·5²·13, a_157 = 1005 = 3·5·67, a_163 = 1035 = 3²·5·23, ... — a recurring,
non-transient pattern, not early exceptions). Same failure for a_1 = 21 (Q={3,7}) and
a_1 = 33 (Q={3,11}). I also confirmed the eventual period for a_1=35 is T=34, L=210 =
2·3·5·7 — i.e. the actual reconciling core needs **two** extra primes {2,3}, not one
universal glue prime. So the "sparse Q ⟹ single universal glue prime" dichotomy that
Step 4b proposes to prove is mathematically false as stated, not merely unproved. (The
seeds that "confirmed" it — 15, 45, 105, 1001 — apparently only worked because their
extra core S happened to have size 1; that is not the general sparse-Q behavior.)

This is important: it means the round's most-developed proposed *mechanism* for closing
(†) is a dead end, but it does NOT retire `covering-system-construction` as an approach
— Steps 1–3 (Free Facts, Bounded Witness Lemma, Finite Core Theorem) are untouched,
correct, and remain the strongest certified content in the population, and (†) itself
(the abstract intersecting-extended-types claim) is not refuted by this — only the
proposed "single prime" shortcut to it is.

### covering-system-construction — CHANGES REQUESTED

- Steps 1–3 (Free Facts, Bounded Witness Lemma, Finite Core Theorem): sound, unchanged
  from round 1, correctly certified — no new issues.
- **Step 4b Case (i), Universal Glue Prime Lemma: REFUTED by explicit counterexample**
  (see above, a_1 = 35/21/33). The builder must NOT attempt to prove this lemma as
  stated — it is false, not merely open. Drop the "sparse Q ⟹ one universal prime"
  claim entirely.
- The sparse/dense split itself (Case i vs Case ii) is consequently unmotivated as a
  clean dichotomy — a_1 = 35 has Q missing 2 (nominally "sparse" per the outline's own
  definition) yet needs 2 extra primes, behaving like the "dense" fallback. The
  dichotomy variable should be "how many extra primes are eventually needed," not
  "whether Q contains small primes" — these are not the same thing, as the
  counterexample shows.
- What to do instead this round: attack (†) directly, using the concrete data point
  that a_1=35's actual finish uses S_0={2,3,5,7}, L=210, T=34 — i.e. the correct
  invariant is that the FULL finite set 𝒫' of extended-persistent types (not a single
  prime) must pairwise intersect, and the builder should look for why the *cyclic
  residue structure mod L* forces this (e.g. via the CRT + cyclic-pigeonhole finish
  itself, which already stitches together whichever primes get recruited) rather than
  hunting for a distinguished single prime. This is a fix-in-place, not a full RETHINK,
  since the underlying (†) target and Steps 1–3 remain valid and this is the sharpest
  base in the population.
- Secondary open gap (n=1 boundary) unchanged, still untouched, correctly flagged.

### greedy-exchange-cost-potential — CHANGES REQUESTED (new approach, verified sound
after its self-correction)

- The self-reported retraction (dropping the false "cost(n) ≤ |𝒫|-1" claim in favor of
  the trivial "|P(a_n)∩S| ≤ |S|" bound) is verified correct: the Finite Core Theorem
  only gives "at least one shared S-prime per disjoint type," which indeed does not
  imply a global bound on distinct extra primes recruited; the corrected, weaker
  statement is the right one and is soundly derived. Good catch by the outliner, and
  the correction is not a re-introduction of hand-waving — it's an honest downgrade to
  what's actually provable.
- The **Generalized Bounded Gap fact** (a_{n+1} ≤ a_n + a_1·p for any prime p) is
  correct and unconditional: the proof is literally the certified Bounded Gap Lemma's
  argument with a_1 replaced by a_1·p (a_1·p is still divisible by every prime of Q, so
  every earlier term shares a Q-prime with it). This is real, new, promotable content —
  no gap.
- The conjectured "C=1 in the sparse regime" (cost(n) ≤ 1 eventually when Q is
  sparse) is explicitly hedged as a conjecture, not asserted as proved — good, this
  respects CLAUDE.md's "prove, don't conjecture" rule. However, my counterexample above
  (a_1=35 needs 2 extra primes, and individual terms like a_153=975 even have a THIRD,
  incidental large prime 13 outside {2,3,5,7} entirely, i.e. cost(153) = |{3,13}| = 2 by
  the literal definition) shows this conjecture is in fact false as stated too. This
  should be dropped from the approach's target list next round — flag it as refuted,
  not just "open," so no future round wastes a builder slot chasing it.
- The approach's honest core claim — that its Step 5 finish, on inspection, needs
  essentially the same content as (†) — is correct and appropriately disclosed; this is
  not a wasted population slot, it's legitimate diversity (a per-term counting framing)
  even though it converges on the same crux. Its unconditional deliverables
  (Generalized Bounded Gap fact) justify keeping it as a live population member.

### amortized-charging-budget, density-sieve-contradiction, hypergraph-transversal —
left ADVANCE / stale, not rebuilt this round (agree with outliner)

- Unchanged from round 1; the outliner's reasoning for leaving them stale (all three
  either duplicate the shared crux with less precision, or — per the round-1 rule
  in memory — name a mechanism without a working proof) still holds. No new issues to
  report since nothing changed in these files this round. Correctly not touched by the
  outliner and correctly excluded from the build set — building any of them in
  parallel with the two above would burn a slot re-deriving the same crux from a
  strictly worse starting point.

### Diversity assessment

The field still converges on one crux (†) / its equivalents — this is expected and
was flagged in round 1 as the genuine mathematical difficulty, not an artifact of
insufficient framing diversity (three independently-conceived framings — covering
systems, charging budgets, cost potentials — all reduce to the same content, which is
reasonably strong evidence (†) really is the hard core of the problem, not a
by-product of narrow exploration). No action needed beyond what's already planned;
continuing to diversify framings around the SAME crux (as greedy-exchange-cost-potential
does) is valuable, but a genuinely orthogonal idea (e.g. a full case-enumeration proof
for a fixed small family of a_1's, or a structural argument about why L must contain
every prime that is EVER a bottleneck) would be worth a fresh math-explorer pass next
round if this round's builders also stall on (†).

### Registration / ranking

- Registered `greedy-exchange-cost-potential` (new this round).
- Ranked the full field head-to-head (comparisons anchored the newcomer against all
  four established approaches, plus reaffirmed covering-system-construction's lead
  and the stale trio's lower standing; one draw between the two least-developed stale
  approaches). Updated Elo: covering-system-construction 1582.6 (top), greedy-exchange-
  cost-potential 1531.7, amortized-charging-budget 1510.1, density-sieve-contradiction
  1453.8, hypergraph-transversal 1421.8.

### Build set rationale

Both `covering-system-construction` and `greedy-exchange-cost-potential` are approved
to build this round, per the outliner's recommendation, WITH the corrections above:
the builder for `covering-system-construction` must drop the falsified Universal Glue
Prime Lemma and attack (†) directly using the multi-prime data point (a_1=35 example);
the builder for `greedy-exchange-cost-potential` must drop the falsified "C=1 sparse
regime" conjecture and focus on the finite-enumeration reframing or the general (†).
The stale trio stays out of this round's build set.

build set: covering-system-construction, greedy-exchange-cost-potential
