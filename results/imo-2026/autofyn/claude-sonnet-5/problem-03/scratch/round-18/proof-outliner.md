## imo-2026-03

Single live approach, one nominated build (advance, no new slug — per CLAUDE.md single-gap-trap and
the dispatch instruction). Wrote new §29 into
`results/imo-2026-03/approaches/potential-weighting-upper-bound.md` reconciling the three round-18
explorer reports (`match-branch`, `gap1c-case-a`, `touch-dependency`).

### What I added (§29, ~4 subsections)

**§29.1 — Match-Branch-Domination-via-Per-Partner-Domination (ready to certify).** Formalized the
`match-branch` explorer's headline finding as an explicit 3-line lemma: Two-Touch's own MATCH branch
value `MATCH_j` is *literally* Gap 1a's `A_{3,j}` under variable renaming, and both ingredients needed
to invoke Per-Partner Domination (`A_1 >= TT` via the already-certified DELETE branch; `D_j >= TT`
trivially, by definition of the max) are already in hand. Stated exactly what's unconditionally proved
now (Two-Touch fully closed for `|W|<=3`, a genuine new result) vs. what still depends on Per-Partner
Domination's own open general-`q` gap (everything at `q>=4`). Recommended retiring "Match-Branch
Domination" as a separately-tracked open item — it's subsumed by Gap 1a's existing top-priority gap, not
independent content.

**§29.2 — Three-Touch MATCH Sibling-Domination Lemma (`sigma=-1` only, new candidate, not yet proved).**
Formalized the `touch-dependency` explorer's finding: `MATCH_val <= max(DELETE_val, KEEP_val)` using the
*true* recursive sibling branch values (not closed-form candidates), 0/28,500 including inside Two-Touch's
own genuine `b_0<=w_1` recursive-call scope. If proved, closes Three-Touch's MATCH branch in 2 lines
(no candidate-shape casework) and, via the already-established non-circular mutual induction, Two-Touch's
remaining KEEP `b_0<=w_1` sub-case too. **Explicitly flagged the asymmetry three ways** so it can't be
conflated: (i) the naive `sigma=+1` mirror of sibling-domination is FALSE (~13% failure — this is Two-Touch's
own already-documented dead-end MATCH problem, correctly handled instead by §29.1's reduction, not by
sibling-domination); (ii) a weaker `sigma=-1` "Mirror Per-Partner Domination" using a bare scalar proxy
`D'_l=|c-d_l|` instead of the true `KEEP_val` is ALSO false (~7-15%) — this is the match-branch explorer's
own secondary finding, a different (weaker, refuted) claim; (iii) only the true-branch-value version in
§29.2 (this section) survives 0/28,500. Recorded the refuted "background-value monotonicity" proof route
and the recommended (untested) exchange-argument shape instead.

**§29.3 — Gap 1c case (a) narrowed to `delta_c` alone.** Restated the case-(a) setup and the
Insertion-Difference-Identity decomposition `e(M∪{c,d})-e(M) = delta_d + delta_c`. Isolated `delta_d>=0`
as a new, apparently tie-break-independent (both nearest and farthest `c` tested, 0/1800), self-contained
sub-target — strictly smaller than any route tried in rounds 16-17. Named `delta_c`'s magnitude bound
(negative ~94% of the time, so nearness of `c` to `d` must be doing real quantitative work, not just a
sign flip) as the genuinely hard residual once `delta_d>=0` is granted. Recorded two ruled-out leads
(rank-adjacency of `c,d` — false; the "free bound via the unaugmented problem" chaining — provably wrong
monotonicity direction via Shrink-List Monotonicity) so neither is re-attempted. Also recorded the
never-observed exact-tie diagnostic (margin never 0 in case (a), unlike (b)/(c)) as a sanity-check data
point, not yet load-bearing.

**§29.4 — reconciled priority order / build recommendation** (see below).

### Recommendation: closest to a real proof this round

Priority order, closest-to-done first:
1. **§29.1 (certify now)** — this is not a conjecture, it's a proof from already-certified/trivial
   ingredients; near-zero cost, and delivers a genuine new unconditional result (Two-Touch closed for
   `|W|<=3`) as a side effect. Should be written up formally and certified this round.
2. **§29.2 (best risk-adjusted payoff)** — the closest any MATCH-branch angle has come to a real proof
   mechanism (not just corroboration): a concrete recommended proof shape (exchange argument: MATCH
   witness vs. an explicit KEEP-side witness built from it) exists, and 0/28,500 with zero adversarial
   failures despite real effort (engineered duplicate-cancellation cases included) is the strongest
   corroboration any single MATCH-branch claim has had to date. If it closes, it finishes Three-Touch
   AND Two-Touch's last remaining branch in one shot.
3. **§29.3 sub-target 1 (`delta_d>=0`)** — independent of items 1-2, low-risk, can run as a third parallel
   builder thread on the same slug; looks like a clean, self-contained, tie-break-independent fact worth
   a dedicated symbolic attempt before touching the harder `delta_c` residual.
4. Per-Partner Domination general-`q` (standing top priority, now doing quadruple duty per §29.1) remains
   the highest-total-leverage but hardest target — not the "closest to done" this round, still the
   long-term must-close item.

**Build set:** `potential-weighting-upper-bound` only (sole live slug). Recommend the builder split effort
across §29.1 (write-up + certify, cheap), §29.2 (attempt the exchange-argument proof), and §29.3
sub-target 1 (`delta_d>=0`) in that priority order if time allows more than one; §29.1 should not be
skipped even if time is short, since it's a real result at near-zero cost. dyadic-cascade-induction and
concavity-minimax-duality remain benched — no new leverage found or claimed this round, not re-examined
beyond confirming the dispatch's own framing (no genuinely new angle surfaced for either).

File: `results/imo-2026-03/approaches/potential-weighting-upper-bound.md` (new §29, lines ~6737 onward).
