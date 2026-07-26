## imo-2026-03 (Chu-Han war, IMO 2026 P3)

### Distinct openings (retrieval route)
- **Opening A — Greedy-alternating lemma + rank reformulation.** The claim phase (alternating picks, Liu Bang first, both maximize own length, identical additive valuations) is a standard alternating draft. Key lemma (must prove from scratch): greedy (always pick the largest available piece) is a dominant strategy for both players; hence Liu Bang's payoff = sum of pieces at odd ranks (1st, 3rd, 5rd, ...) after sorting descending. This collapses the whole game to: *Liu Bang places ≤n marks, then Xiang Yu places ≤n marks; payoff = sum of odd-ranked pieces (desc sort)*. Everything downstream hangs on this lemma. A second universal lemma falls out for free: since a₁≥a₂, a₃≥a₄, …, we always have S_odd ≥ S_even = 1 − S_odd, so **S_odd ≥ 1/2 always** — a universal lower bound c(n) ≥ 1/2, and equality S_odd = 1/2 iff pieces pair up (a₁=a₂, a₃=a₄, …). This is the floor the upper bound pushes toward.
- **Opening B — Dyadic/geometric construction (Liu Bang lower bound).** The optimal Liu Bang strategy is **place marks at cumulative dyadic positions** (2^k−1)/D for k=1..n, where D = 2^{n+1}−1. This creates pieces 1/D, 2/D, 4/D, …, 2^n/D (powers of 2 summing to D). Conjectured (verified exactly for n=1,2,3): this guarantees S_odd ≥ 2^n/D = **2^n/(2^{n+1}−1)**. Xiang Yu's best response to these pieces (verified exact, e.g. n=3: Xiang marks at 4/15 and 11/15) achieves exactly 2^n/D by splitting the largest pieces into equal halves to create pairs. The "one largest piece exceeds the sum of all smaller ones" property (2^n > 2^n−1) is what prevents Xiang Yu from fully pairing everything away — a dyadic tower.
- **Opening C — Xiang Yu upper bound via surrogate adversary.** The hard half: for *arbitrary* Liu Bang marks, exhibit Xiang Yu's strategy holding Liu Bang to ≤ 2^n/D. The retrieved crux move **"replace the adversary with a strictly stronger surrogate whose reply is pointwise at least as damaging, so a win against the surrogate transfers down"** (aimo-0560, gardener/lumberjack) is the template: design a relaxed/stronger Xiang Yu surrogate whose best achievable S_odd is provably ≤ 2^n/D, then argue the real Xiang Yu (fewer constraints) does at least as well. Pairing/involution mirroring (aimo-0115 domino pairing, aimo-0596 involution-partner) is the engine: Xiang Yu answers each large Liu-Bang piece by inserting a mark that pairs it with an equal neighbor, collapsing S_odd toward 1/2 + the un-pairable dyadic surplus 2^n/D − 1/2.
- **Opening D — Self-reproducing invariant (Cinderella template).** aimo-0262's crux "hand the defender a self-reproducing invariant family of configurations and show each legal move can restore it" adapts as: Liu Bang maintains the invariant "the piece-length multiset is dyadic {1,2,4,…,2^n}/D" *after* Xiang Yu's response is accounted for, by an invariant on the rank-weighted sum. This is essentially the inductive engine for the lower-bound half: show that whatever ≤n marks Xiang Yu inserts among the dyadic pieces, the odd-rank sum stays ≥ 2^n/D by an invariant restored at each Xiang Yu move.

### Candidate technique(s)
- **Alternating-draft greedy lemma** (dominant strategy, identical valuations) — the linchpin; prove by induction on item count.
- **Pairing inequality / rank-pairing**: a₁≥a₂ etc. gives S_odd ≥ 1/2; equality characterization drives both bounds.
- **Dyadic (geometric-ratio) construction**: pieces in ratio 1:2:4:…:2^n; the largest exceeds the sum of all smaller (2^n > 2^{n+1}−1 − 2^n = 2^n − 1), the load-bearing structural fact.
- **Surrogate adversary** for the upper bound (minimax upper bound via a stronger opponent).
- **Self-reproducing invariant** for the lower bound (Cinderella-style).
- **Strong induction on n** with the dyadic recursion c(n) = 2^n/(2^{n+1}−1) satisfying c(n) = 2·c(n−1)·(something); the natural recursion is D_n = 2D_{n−1}+1, c(n)=2c(n−1)·D_{n−1}/D_n, suggesting an inductive construction that appends a doubled piece.

### Cheap-kill candidates
- **Universal floor S_odd ≥ 1/2** (rank-pairing) — free, gives the asymptote and the floor the upper bound chases.
- **"Largest exceeds sum of smaller" (2^n > 2^n−1)** — the single dyadic inequality that stops Xiang Yu from pairing everything away; one-line but load-bearing.
- **Symmetry / WLOG ordering of marks** — halves the casework in the upper bound.

### Knowledge-base entries to use
- **Invariants & monovariants** (combinatorics) — the self-reproducing invariant for the lower bound.
- **Extremal principle / pigeonhole** — for the upper-bound counting/pairing argument.
- **Induction (structural) / infinite descent** — recursion D_n = 2D_{n−1}+1.
- **Constructive vs existence** (General Proof Methods) — must give BOTH Liu Bang construction (lower bound) and Xiang Yu strategy (upper bound) for compute_and_prove.
- **Pólya: specialize / check the answer** — verify c(n)=2^n/(2^{n+1}−1) at n=1,2,3 (done, exact).
- (No knowledge_base entry for alternating-draft games or cake-cutting exists; the greedy lemma must be proved from scratch.)

### Analogous past problems (cruxes)
- **aimo-0262 (Cinderella/Stepmother, games-and-strategy)** — *closest structural analog*. Adversary (Stepmother) distributes 1 unit over a cyclic structure, defender (Cinderella) responds with a localized move to maintain a self-reproducing invariant. Crux: "self-reproducing invariant family of configurations, each legal move can restore it." Adapts to imo-2026-03 as Liu Bang's lower-bound invariant: the dyadic piece-ratio multiset is the self-reproducing family; show each Xiang Yu mark can be answered (in the payoff accounting) without dropping S_odd below 2^n/D. *Caution*: Cinderella's move is *active* (she empties buckets), whereas Liu Bang's marks are all placed *before* Xiang Yu moves — the invariant must be front-loaded, not reactive. So the adaptation is an *a priori* invariant on rank-weights, not a turn-by-turn response.
- **aimo-0560 (gardener/lumberjack, games-and-strategy + coloring-and-parity)** — surrogate adversary crux: "replace the adversary with a strictly stronger surrogate whose reply is pointwise at least as damaging, so a win against the surrogate transfers down." Adapts directly to the Xiang Yu upper bound: design a surrogate-Xiang-Yu with extra power (e.g. allowed to re-pick, or to insert marks at arbitrary dyadic offsets) that provably caps S_odd at 2^n/D; real Xiang Yu is weaker, but the cap still holds because the surrogate's strategy is a restriction of the real strategy space. Also borrows the periodic-coloring-per-window-budget move (aimo-0560 coloring-and-parity) as a way to define the rank-pairing budget.
- **aimo-0117 (Jesse/Tjeerd dyadic stones, games-and-strategy)** — crux: "assign the played values as a two-sided geometric (dyadic) sequence so that the single largest value strictly exceeds the sum of all the others." This is the *exact* structural reason the dyadic construction works here: piece 2^n/D exceeds the sum of all smaller pieces (2^n−1)/D, so it can never be fully paired away — it always lands at an odd rank. Strongest analog for the lower-bound engine.
- **aimo-0115 (domino pairing, games-and-strategy)** and **aimo-0596 (involution-partner mirroring)** — pairing/involution strategies for the second (responding) player. Relevant as the *form* of Xiang Yu's upper-bound response: answer each large Liu piece by pairing it. But these are responder-acts-after games; here Xiang Yu also acts after Liu Bang's marks, so the form transfers, but Liu Bang does NOT get to respond to Xiang Yu in the marking phase (only in the claim phase, where greedy is forced) — so the mirroring applies to the *marking* phase from Xiang Yu's side.

**Dead-end cruxes (look related, do NOT transfer):**
- aimo-0663 (no-consecutive picks, component-counting) — different game (selection constraint, not piece-claiming); the component-count liveness argument has no analog here.
- aimo-0461 (knight conflict-cycle partition) — conflict-graph pairing; the 4-cycle structure is board-specific, no interval analog.
- aimo-0019 (paintful dyadic covering) — dyadic intervals appear, but the game is cooperative-covering with a fixed ink budget; the *move* (look-ahead painting beyond the frontier) does not map to mark-then-claim.

### Prior progress
- Round 1, workspace empty — no prior approaches.

### Dead ends (do not retry)
- (none yet — round 1.)

### Small-case / intuition notes (CONJECTURE, labeled)
- **Conjectured answer: c(n) = 2^n / (2^{n+1} − 1).** Equivalently 1/(2 − 2^{−n}). Tends to 1/2 from above.
- Verified **exactly** (rational arithmetic) for n=1,2,3:
  - n=1: c=2/3. Liu marks {1/3}; pieces 1/3, 2/3. Xiang's best (split 2/3→1/3+1/3) gives 3 equal pieces, S_odd=2/3.
  - n=2: c=4/7. Liu marks {1/7,3/7}; pieces 1/7,2/7,4/7. Xiang's best (split 4/7→2/7+2/7) gives S_odd=4/7.
  - n=3: c=8/15. Liu marks {1/15,3/15,7/15}; pieces 1/15,2/15,4/15,8/15. Xiang's best (marks {4/15,11/15}) gives S_odd=8/15. Confirmed by continuous differential evolution that no off-grid Xiang response beats 8/15, and that perturbations of Liu's dyadic marks give strictly less (0.53, 0.528, 0.5), i.e. the dyadic construction is at least a local maximum.
- **Universal lower bound S_odd ≥ 1/2** (proved, not conjecture) — confirms c(n)≥1/2 for all n, ruling out the tempting-but-wrong formula 2n/(2^{n+1}−1) which dips below 1/2 at n≥3.
- **Liu Bang optimal strategy = dyadic construction** (marks at (2^k−1)/D, pieces 2^k/D): strongly supported for n≤3, conjectured for all n. Lower-bound proof engine = "largest piece 2^n/D exceeds sum of all smaller pieces (2^n−1)/D, so it always survives at an odd rank."
- **Xiang Yu upper-bound strategy** (conjectured form): pair-up response — split each large piece into equal halves to create a₁=a₂ pairs, driving S_odd toward 1/2 + (un-pairable dyadic surplus). The general-arbitrary-Liu-Bang-marks version is the open proof gap; the surrogate-adversary crux (aimo-0560) is the suggested engine.
