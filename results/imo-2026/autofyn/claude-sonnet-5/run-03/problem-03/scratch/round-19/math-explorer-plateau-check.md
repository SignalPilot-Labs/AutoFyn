## imo-2026-03 (plateau-check / fresh-framing lens)

### 1. Plateau-check: are gaps (1) GT(m) general-k Half-Sum Lemma and (2) Sigma-shape
Existence Theorem secretly the same obstruction?

**Verdict: still genuinely different obstructions in their literal content** (confirms
rounds 13/14/17/18's repeated finding — no reversal here), but I found a concrete,
previously-only-vaguely-flagged **structural bridge** worth exploiting, not just a
coincidence to note:

- Gap (1)'s residual (round 18) is now precisely: prove, for `R` with `max(R)<=2^{k-1}`,
  `|R|<=k+1`, `sum(R)=S in [2^k,2^k+1)`, that `OddSum(R∪Γ_{k-1}) >= (S+2^k)/2` (equivalently
  `AltSum(R∪Γ_{k-1})>=1`). The builder's own diagnosis (Step 3 of round 18's file) is that
  the natural induction-on-`k` fails because peeling the tied-top pair keeps `cap=2^{k-1}`
  fixed while the Γ-index drops — i.e. it needs a **two-parameter family** `GCH(j,cap,b;S)`.
  The k=2 proof case-splits by count `n=|R|` and by whether `a_1` ties the cap `2^{k-1}`, with
  equality attained exactly at a **symmetric tie configuration** (`b=c`).
- Gap (2)'s residual is: for a fixed `p` in the balanced region, show every legal
  cut-allocation/tie-shape `sigma` gives `OddSum<=c(n)` — i.e. enumerate/bound the
  (unboundedly many, per round 11's Stirling-number count) Sigma-shapes. `global-lp-vertex-
  sufficiency`'s whole certified machinery (Affine-Rank Lemma, Vertex-Attainment Lemma, Global
  Vertex Lemma) is precisely: *fix an interleaving/rank pattern, the payoff is affine in the
  free split coordinates, so extrema over a compact polytope occur at vertices* — and its
  Flat/Kink Parity Lemma (round 17) computes exactly when perturbing a split is flat (tie of
  same parity) vs. a kink (opposite parity), i.e. exactly the same "tie-vs-non-tie" dichotomy
  that closed GT(m)'s k=2 case by hand.

**The bridge**: Gap (1)'s target — minimize `AltSum(R∪Γ_{k-1})` subject to `sum(R)=S`,
`0<r_i<=cap`, `|R|<=k+1` — is *literally* a linear program: for a fixed sorted-order pattern
(a fixed interleaving of `R`'s elements among `Γ_{k-1}`'s dyadic values), `AltSum` is affine in
the `r_i` (coefficient `+-1` by rank parity, exactly the mechanism of the Flat/Kink Parity
Lemma). Minimizing a linear functional over the polytope `{sum=S, 0<=r_i<=cap}` (a box
intersected with a hyperplane) forces the minimizer to a **vertex** — a point where all but at
most one coordinate sits at `0` or `cap` — which is *exactly* the case-split the k=2 proof
does by hand (tie-at-cap vs. strictly-below, `b=c` at the symmetric point). This means the
general Cardinality-Constrained Half-Sum Lemma is very likely provable by **importing**
`global-lp-vertex-sufficiency`'s already-certified Affine-Rank Lemma / Vertex-Attainment
Lemma machinery (treating `R`'s box-simplex as the polytope, instead of the Sigma-shape
cut-allocation polytope it was built for) rather than by a bespoke induction on `k`. This is a
genuinely new, concrete top-level idea — not previously stated this explicitly (round 11 only
flagged a vague "possible deep correspondence" for the unrelated j>=2 trichotomy, and it was
never revisited for the current residual). It does not make gaps (1) and (2) the same problem
(different polytopes, different target constants), but it means **the same certified tool**
could close (1) if imported correctly — a real, actionable opening for the outliner, distinct
from "just keep inducting on k."

Caveat to flag to the outliner: the LP-vertex argument only pins down the minimizer's *shape*
(vertex of the box), not automatically the count `n=|R|` or which sub-case is worst across
varying rank-order cells as `S`, `k` vary — that part still needs the kind of case-enumeration
the k=2 proof did (finitely many vertex "shapes" per fixed `n`, but `n` itself ranges over
`2..k+1`). So this is a promising **method import**, not a free closure.

### 2. Fresh-framing / crux corpus search

Searched `combinatorics` subtopic `linear-algebra-method` (16 cruxes) — all are `F_2`/linear-
algebra-over-a-finite-field arguments (dimension counting, XOR bases, DFT-mod-p), none are
real-valued LP/vertex-of-a-polytope arguments; no match for the "affine functional extremized
at a box vertex" technique used throughout this run's `global-lp-vertex-sufficiency` and now
proposed for gap (1) above. Searched all cruxes for `polytope`/`linear program`/`alternating
sum`/`extreme point` keywords — no genuine hit (closest, `aimo-0970`, is a double-counting
edge-count argument on a polytope's 2-faces, unrelated in mechanism). Searched for
`two-parameter`/`strengthen the induction hypothesis` — found `aimo-0291` (combinatorics,
`induction-and-construction`): "strengthen the induction by conjecturing the exact multiset
of the whole initial segment rather than the asked-for property, then carry that multiset
forward" — a generic reinforcement of the standing diagnosis (gap (1) needs a *stronger*,
two-parameter induction hypothesis, not the literal statement being inducted on), but it is
not a specific technique transplant, just confirms the right instinct.

**Conclusion, per CLAUDE.md's "don't force a wrong match" instruction: no crux gives a ready-
made technique for either gap.** This matches round 6's and round 13's own prior findings
(no viable entropy/generating-function/rearrangement/LP-duality crux exists for this problem's
specific split-and-claim structure) — the corpus has been searched from several angles across
rounds now (games-and-strategy in round 6, double-counting mechanisms in round 18, linear-
algebra-method this round) with consistently negative results. I recommend the outliner stop
dispatching further corpus searches for this specific pair of gaps unless a genuinely new
angle (e.g. `probabilistic-method` or `generating-functions`, untried as of this report) is
proposed — those two subtopics remain unexplored in this run's history and could be worth one
more try, but I did not find time to search them this round; flagging as a residual lead.

**Is `lp-duality-split-polytope` worth reviving?** Its own file (round 18) proves the
Mass-Constraint technique structurally caps at `s ~ N/2`, strictly below the needed `s>=n-1`
necessity bound — a *proved* ceiling, not just an unlucky numeric run. Round 18 also checked
two crux double-counting mechanisms (`aimo-0091`, `aimo-0178`) and found both fail to
transplant for identifiable structural reasons. I found no new mechanism this round either.
**Recommendation: do not revive with "more of the same technique."** It is not yet dead (its
certified Perfect-Tie-Family Characterization and Generalized Mass-Constraint Theorem remain
correct, reusable results, and its necessity conjecture itself is not refuted) — but per Rule
30 of `/tmp/memory/math-explorer.md`, stop asking it to refine the capped technique. If revived
at all, it should be given a **genuinely different counting mechanism** (not mass-summation,
not double-counting-family transplant) — I did not find one; suggest keeping it light/dormant
(current status) rather than actively building, unless another explorer surfaces a fresh idea.

### 3. Sanity check: read the problem fresh

Re-read the reduction chain: (i) alternating claim-from-a-sorted-multiset game reduces via
the certified greedy-optimality lemma to "first mover gets odd sorted-ranks" — this is a
standard, solid argument (I re-derived it mentally: since both players are indifferent to
*which* piece as long as size is fixed, and claiming the largest available piece is a dominant
strategy for whoever moves, by a straightforward exchange argument) — no crack found here.
(ii) The two-sided minimax (LB picks a partition to maximize the worst-case OddSum, XY refines
it to minimize OddSum) is the actual open combinatorial core. I did not find any simpler
top-level reformulation that the 18 rounds of work have missed: the AltSum reformulation
(`OddSum=(sum+AltSum)/2`, Lemma AS) is already the cleanest available monovariant, and the
LP/vertex reduction (fixed rank-pattern => affine => vertex-extremal) is already the natural
"right" structural fact for the upper-bound side. One thing that struck me as possibly
under-leveraged: the problem is symmetric in a specific way — LB's OPTIMAL partition is
(conjecturally, established at least at small n and via the Twin-Anchor/Top-Duplication
witnesses) the *geometric* partition `1/2,1/4,...,1/2^n,1/2^n`, and essentially **all** of the
approaches' hardest cases (GT(m), the Perfect-Tie-Family at `e_0`) arise near-uniform/AP
partitions, i.e. the boundary of the balanced region — not the geometric partition itself. This
is already implicitly known (the "two remaining gaps" are both about the boundary/AP
structure, not the geometric witness), but I want to flag it explicitly: **no approach is
currently trying to prove the Existence Theorem is easiest (or reduces) at genuinely
non-AP-like points and only needs the hard work exactly at/near the boundary** — if a future
round can show `V(p)<=c(n)` degrades continuously and its supremum over the whole balanced
region is *attained* at (or is a limit of) exactly the AP-structured boundary points
`global-lp-vertex-sufficiency` already fully closed (`Q_region`), that would let the Sigma-shape
classification be bypassed entirely via a boundary-continuity/compactness squeeze instead of
enumerated case-by-case — this is essentially what round 10's Boundary Continuity Theorem did
for the region-only candidates, and might generalize to the Sigma-shape candidates too. I did
not verify this (no time, and it would require developing a semicontinuity argument, which is
outline-outliner work, not scouting) — flagging as a possible under-exploited lead, not a
finding.

## Summary for outliner

- Distinct openings: (a) import `global-lp-vertex-sufficiency`'s Affine-Rank/Vertex-Attainment
  machinery to close the general Cardinality-Constrained Half-Sum Lemma (gap 1) by recognizing
  it as an LP over `R`'s box-simplex polytope, rather than continuing the bespoke
  induction-on-k that's diagnosed as needing a two-parameter family; (b) explicit reminder
  that gap (1)'s fix needs a genuinely *strengthened* induction hypothesis (per aimo-0291's
  generic pattern), tracking `(j,cap,b)` jointly, not a single-parameter `k`; (c) possible
  boundary-continuity/compactness squeeze to bypass full Sigma-shape enumeration for gap (2)
  (unverified lead, not yet attempted by any approach).
- Candidate technique(s): LP-vertex/affine-cell extremization (already certified machinery,
  new target); two-parameter strengthened induction; boundary-continuity/semicontinuity
  argument (speculative).
- Cheap-kill candidates: before committing to the LP-vertex-import idea, cheaply check (via
  `scipy.optimize.minimize` with explicit `LinearConstraint`+`Bounds`, per this file's own
  Rule 31 methodology) that the general Cardinality-Constrained Half-Sum Lemma's minimizer,
  across `k=2..8` and several `n=|R|`, always sits at a box-vertex (all-but-one coordinate at
  `0` or `cap`) — if some minimizer is NOT vertex-shaped, the LP-import idea is dead cheaply,
  before any proof investment.
- Knowledge-base entries to use: none new identified beyond what's already cited in the
  approach files (Lemma AS / OddSum-AltSum identity; the general greedy-optimality reduction).
  Recommend re-skimming `knowledge_base.md`'s LP-duality/extremal-principle entries for a
  formal "affine function on polytope attains extrema at vertices" citation to name explicitly
  when the outliner writes this up (I did not have time to open the file this round — flag for
  the outliner to check knowledge_base.md directly for a citable vertex-extremization theorem).
- Analogous past problems (cruxes): none found. Searched `combinatorics/linear-algebra-method`
  (16 entries, all F_2 linear algebra, no real-LP match), keyword search for
  `polytope`/`alternating sum`/`extreme point` (no genuine match), and
  `two-parameter`/`strengthen the induction` (found `aimo-0291`, a generic
  strengthen-the-induction-hypothesis pattern, not a specific technique transplant — useful as
  a reminder, not a worked template). `probabilistic-method` and `generating-functions`
  subtopics remain unsearched as of this report — a residual lead for a future explorer.
- Prior progress: see `results/imo-2026-03/current.md` round 18 entry (full detail already in
  that file) — GT(m) sub-case(i) e=1 residual is exactly `a_1 in (2^k-1,2^k]`, k=2 instance
  fully closed, general-k left as a precisely-stated (not proved) conjecture; upper-bound
  n=2 shape not yet fully closed (round-18 dispatch bug caught: a candidate near-maximizer was
  outside the balanced region; a narrow branch-specific closed form proved always exceeds
  c(2); true sup at valid points not yet established in exact arithmetic).
- Dead ends (do not retry): `lp-duality-split-polytope`'s Mass-Constraint-refinement family
  (proved to structurally cap at `s~N/2`, cannot reach `s>=n-1` by any refinement — round 18);
  the two crux double-counting mechanisms `aimo-0091`/`aimo-0178` (checked round 18, both fail
  to transplant for named structural reasons); all previously-listed dead ends in
  `current.md` (naive priority-order strategies, Lemma X', cyclic/star/tree tie topologies,
  region-boundary path-monotonicity, concavity/quasi-concavity of V(p), structured
  randomization schemes, reciprocal-potential pointwise recursion) — none newly revisited this
  round, all still stand as recorded.
- Small-case / intuition notes: the LP-vertex bridging idea is a structural observation, not
  yet numerically tested by me this round (time-constrained) — the cheap-kill above (vertex-
  shape check via constrained `scipy` optimization at several `k`) should be the very first
  thing done before any proof effort, consistent with this run's own standing methodology
  rules. All other numeric findings in this report are drawn from re-reading already-certified
  round-17/18 content (re-verified consistent, not independently re-run by me this round given
  time budget) — treat any numbers herein as reported-and-trusted from the workspace files, not
  freshly recomputed.
