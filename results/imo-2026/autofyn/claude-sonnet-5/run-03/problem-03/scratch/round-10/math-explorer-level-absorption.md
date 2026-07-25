## imo-2026-03 — lens: Level-Absorption / re-splitting-degradation (greedy-reduction-geometric)

### Distinct openings
1. **Direct exchange-smoothing on P (per the dispatch's lead 2).** Try to show
   that among all admissible splits $P=\{\mu_1\}\cup R_1$ of $2^{m-1}$ (fixed
   $\mathrm{sum}=2^{m-1}$, $\mu_1<b_2$, cut-budget-limited piece count), the
   one that minimizes $\mathrm{OddSum}(M'\cup P)$ can be pushed by a local
   unit-exchange move toward a canonical shape without *decreasing* the
   adversary's (XY's) achieved value — i.e. reduce XY's infinite continuum of
   responses to a finite family of "extremal profiles," then check the target
   inequality only on that finite family (the aimo-0146 pattern). **This is
   viable as a target shape, but the direct transfer of aimo-0146's argument
   does *not* work off the shelf** — see Candidate technique(s) below for why,
   and Small-case notes for what the numerically-found near-extremal profiles
   actually look like.
2. **Attack via $B''$/$S'''$'s own slack instead of $P$'s shape (lead (b) of
   round 9's own diagnosis, Section 13.2).** Rather than bounding the
   degradation abstractly (which the round-9 file already proved is
   insufficient whenever $k\ge3$), use the *already known* fact
   $\mathrm{OddSum}(B''\cup S''')\ge\mathrm{sum}(B'')$ (this is exactly
   Theorem 7a/7 applied one level down, since $B''$ itself has the
   Dominance-Chain property at level $m-2$) to recover the missing $b_2$ worth
   of gain directly from $B''$'s own structure, instead of trying to extract
   it from $P$ alone. This has not been attempted in any round file; it is a
   genuinely different route from both round-9 leads (it decomposes the target
   $b_2+\mathrm{sum}(B'')$ asymmetrically: get $\mathrm{sum}(B'')$ "for free"
   from $B''$'s own slack and reduce the residual burden on $P$ to just
   supplying $b_2$ against a *smaller* effective baseline).
3. **A cut-budget/pigeonhole counting argument directly on the abstract
   worst-case profile ("many exact ties").** Round 9 diagnosed precisely that
   the abstract Split-Degradation bound's own worst case is a "many exact
   ties" configuration (Section 13.2's example: $M=\{5,5,5,5\},g=10,P=\{5,5\}$
   type ties). Since the real level structure is dyadic (powers of $2$) with
   at most one exact tie generically per level, and the cut budget caps how
   many pieces can be forced into ties, a combinatorial argument bounding
   "how many exact ties the cut budget can actually buy against a dyadic
   skeleton" (rather than a continuous inequality) may close the gap between
   the abstract worst case (tight) and the real worst case (strictly
   positive, per every numeric search this round). This is lead (a) of
   round 9's own diagnosis, not yet attempted.

### Candidate technique(s)
- **aimo-0146's exchange-smoothing pattern is a genuine structural analogy,
  but does not transfer directly.** aimo-0146's crux works because its
  objective is *linear* in a finite set of coordinates with a fixed,
  position-independent coefficient vector ($A=\sum a_i x_i$, $a_i\le i-1$
  fixed once the sorted degree sequence is fixed), so "move one unit from a
  low-coefficient position to a high-coefficient position" is a
  well-defined, always-available, always-improving local move, and repeated
  application forces a small number of survivor profiles. **Here,
  $\mathrm{OddSum}(M'\cup P)$ is *not* linear in $P$'s shape**: which
  "coefficient" (odd vs. even sorted rank) a piece of $P$ gets depends on
  the interleaved sort order of $P$ with the *fixed but structured* multiset
  $M'$ (powers of two and $B''$'s fragments), and that assignment changes
  *discontinuously* (rank crossings) as $P$'s shape varies continuously. So
  a first task for whoever pursues opening 1 is to find the right
  *linearization*: e.g., fix which "slot" (odd/even rank, or which power-of-two
  band) each unit of $P$'s mass falls into, the way aimo-0146's charging
  argument fixes $a_i\le i-1$ before smoothing — this reformulation step is
  itself nontrivial and is the actual gap, not a mechanical copy of the crux.
- **General Insertion Monotonicity (Theorem 13, already certified,
  `lemmas/insertion-monotonicity-theorems-12-13.md`)** and **Theorem 7a**
  (already certified) remain the only proved tools; Lemma L
  (`lemmas/unsplit-baseline-lemma-L.md`) is the correct anchor — any new
  attempt should still route through it (it is fully proved, not to be
  re-derived).
- **Prefix-Run Peeling Decomposition Lemma (certified, Section 7.3)** may be
  worth revisiting as a *linearization* tool for opening 1/3: it already
  gives an exact decomposition of $\mathrm{OddSum}$ of a merge by peeling a
  known run of tail values, which is closer to the kind of "fixed coefficient
  per slot" structure aimo-0146's argument needs than a raw inequality is.

### Cheap-kill candidates
- None found this round beyond the already-established (round 7) cut-budget
  necessity. No new parity/pigeonhole shortcut located specifically for
  Level-Absorption.

### Knowledge-base entries to use
- (Consult `knowledge_base.md` directly — this round's exploration worked
  entirely from the approach file's own already-certified internal lemmas,
  which are the load-bearing tools here: Theorem 7a, Theorem 13/General
  Insertion Monotonicity, Companion Peeling, Global-max Peeling. No new
  generic knowledge-base theorem was identified as directly applicable beyond
  what prior rounds already cite.)

### Analogous past problems (cruxes)
Filtered `combinatorics` domain, subtopics `extremal-principle`,
`games-and-strategy`, `invariants-and-monovariants` for split/partition/
adversary/tie keywords (`crux_moves_documentation.md` field names verified:
`technique`, `how_used`, `domain`, `subtopic`).
- **`aimo-0146`** (flagged by the dispatch) — exchange-smoothing of a fixed
  weighted sum over a sorted bounded sequence, driving to a handful of
  survivor profiles. Genuinely the closest structural analogy in spirit
  (adversary's continuum of splits reduced to finitely many checkable
  profiles), but — as discussed above — its linear-objective machinery does
  not transfer as-is; it is a **pattern to adapt after finding the right
  linearization**, not a directly pluggable lemma.
- **`aimo-0117`** — "assign values as a two-sided geometric (dyadic)
  sequence so the largest strictly exceeds the sum of the rest," a
  strategy-game crux built on exactly the dyadic-domination fact
  ($2^j>2^{j-1}+\cdots+2^{-i}$) that underlies this whole approach's
  Dominant-Chain/Theorem 7a machinery. Worth noting as independent
  confirmation that the "single dominant dyadic value beats the rest of a
  dyadic tail" idea (Lemma 3/Global-max Peeling here) is a recurring,
  reliable crux move in this genre — reinforces confidence in Lemma L's
  mechanism but offers no new technique for the actual gap.
- **`aimo-0425`** — exchange-smoothing (swap the heaviest top-group item
  against the lightest bottom-group item) to bound a max−min spread. Same
  family as aimo-0146 but for a *different* (spread, not weighted-sum)
  objective; less directly analogous than aimo-0146 since it doesn't need a
  fixed coefficient vector, but its swap move ("heaviest against lightest")
  is a candidate concrete local move to test for opening 1 if a
  linearization is found — noted as a secondary reference, not a strong
  match.
No other corpus entries found that combine "adversarial resource-splitting"
with "finite extremal-family reduction" as closely as these three; nothing
else surfaced by the keyword sweep resembled this problem's specific
combinatorial-game-value structure closely enough to report.

### Prior progress
- **Lemma L (Unsplit-Baseline)** — certified, `lemmas/unsplit-baseline-lemma-L.md`.
  Gives $\mathrm{OddSum}(M'\cup\{2^{m-1}\})\ge2^{m-1}\ge b_2+\mathrm{sum}(B'')$
  with explicit slack $\Sigma=2^{m-1}-b_2-\mathrm{sum}(B'')\ge0$, i.e. the
  whole remaining task is bounding how much re-splitting $2^{m-1}$ into
  $P=\{\mu_1\}\cup R_1$ can erode that slack.
- Round 9's **Candidate Split-Degradation bound** (degradation $\le g-q_1$,
  evidenced not proved) was shown, *precisely*, to be insufficient whenever
  $k\ge3$: it discards exactly $\Sigma$ and recovers nothing from $B''$'s own
  structure. This is a correct, load-bearing negative finding — confirmed by
  re-reading the algebra in Section 13.2, no error found.

### Dead ends (do not retry)
- **Unbudgeted Level-Absorption** (round 7): false, exact margin $-1/2$ for
  every $m\ge3$ via the specific $m+1$-cut construction. Verified this round
  by direct reproduction of that construction (`/tmp/verify_round7.py`,
  matches the file's claimed $-1/2$ exactly for $m=3,\dots,9$) — confirmed,
  not to be revisited.
- **The abstract Split-Degradation candidate bound used alone** (round 9,
  Section 13.2): proved (conditionally, given the candidate bound) to be
  insufficient whenever $k\ge3$; re-verified the algebra this round, holds up.
  Do not re-attempt closing via this bound in isolation; any future use of it
  must be *combined* with $B''$/$S'''$'s own slack (opening 2 above).
- **Static "Q-priority" LB strategies** (round 2): refuted by exact
  game-tree computation, unrelated mechanism but recorded here again since
  it is the same "avoid the real interleaving" trap that a naive
  linearization attempt for opening 1 could fall back into.

### Small-case / intuition notes (all labeled conjecture/numeric evidence)
- **Reproduced round 7's exact k=2 tight construction** exactly
  (`/tmp/verify_round7b.py`): with $b_1=b_2=2^{m-1}$, level $m-1$ split as
  $\{\mu_1{=}2^{m-2}, R_1{=}\{2^{m-2}\}\}$ (single-piece, budget-respecting),
  level $m-2$ unsplit, all free levels bisected — margin is exactly
  $2^{m-3}-\tfrac12$ for $m=3,\dots,10$, matching the file's claim to the
  digit.
- **Generalized this exact construction to $k=3,4,5$** (DC-minimal $B''$
  chain, $b_2$ pushed to the DC sum-cap, level $m-1$ split tied against
  $b_2$, all free levels bisected): margin stays strictly positive for
  every $(m,k)$ tested, $m=6,\dots,13$, $k=2,\dots,5$, and does **not**
  shrink toward $0$ as $k$ grows at fixed $m$ (e.g. $m=8$: margins
  $31.5,47.5,39.5,51.5$ for $k=2,3,4,5$) — conjecture: the naturally
  DC-minimal-chain-plus-tie construction is not close to the true worst
  case for $k\ge3$ (consistent with round 9's diagnosis that the abstract
  worst case needs *more* structure than this hand-built family supplies).
- **Broader continuous random search** (200,000 trials/config, uniform
  random cut placement and mass split, sampling near $\mu_1\to b_2^-$
  organically) finds smaller margins than the hand construction (e.g.
  $m{=}8,k{=}3$: margin $\approx2.3$ vs. the hand construction's $47.5$),
  confirming the hand-built family under-explores the true adversarial
  space — but **still finds zero violations**, margin always strictly
  positive across all $(m,k)$ tried.
- **A further local-search (random-restart + jitter) pass**, targeting
  near-tie configurations more aggressively, found margins around
  $6\%$–$10\%$ of $2^{m-3}$ at $k=3,4,5$ ($m=8,10,12$), still always
  positive and apparently growing roughly linearly in $2^m$ (not vanishing).
  This is fresh numeric evidence *this round*, independent of round 7's and
  round 9's own searches, that the corrected Level-Absorption claim is very
  likely still true for $k\ge3$, with a margin that shrinks in *relative*
  terms as $k$ grows but not toward zero in absolute terms at fixed $m$ in
  the ranges tested. **This is conjecture/numeric evidence only — no proof.**
- **Conclusion for the outliner:** no evidence this round that
  Level-Absorption is false at $k\ge3$; the open task remains finding the
  *proof mechanism*, not further stress-testing (the claim is now quite
  heavily numerically corroborated across three independent search
  methodologies: round 7's exact search, round 9's hand examples, and this
  round's random/annealed search). The likely proof shape, per the numeric
  pattern (margins scaling with $2^{m-3}$, i.e. surviving from Lemma L's own
  baseline scale, not vanishing), is that the true degradation bound must be
  *strictly* sharper than $g-q_1$ specifically by an amount recoverable from
  $B''/S'''$ — supporting opening 2 as the most promising concrete next
  step, with opening 1 (exchange-smoothing) as a valuable complementary
  route once a correct linearization of $\mathrm{OddSum}$ in $P$'s shape is
  found.
