## imo-2026-03 (lens: upper bound — Xiang Yu's strategy, the shared crux)

### Distinct openings

1. **Huffman-tree / bottom-up-merge reframing (genuinely new, unverified).**
   The min-pairing identity L4 says β (matched-smaller-mass) is realized by pairing
   *consecutive* elements of the sorted final multiset — i.e. the optimal pairing is
   exactly the one a bottom-up greedy-merge (Huffman) construction would produce if you
   think of XY's job in reverse: instead of "cut A into B, then pair," think of building
   B from the bottom by repeatedly combining the two smallest surviving masses into a
   matched pair, charging the *difference* to the next round. The dyadic target profile
   {2^n,…,2,1}/D_n is exactly the classical fact that Huffman-coding a geometric-ratio-2
   weight sequence produces a **caterpillar (chain) tree**, not a balanced tree — matching
   the peel/chain structure every current approach already uses informally. This
   reframing's payoff would be to import a *known, general* exchange lemma ("in an optimal
   merge tree the two smallest weights are combined first, and merges can be swapped
   without increasing cost" — the standard Huffman-optimality exchange argument) to justify
   the match/bisect choice *structurally*, rather than by an ad hoc per-cut case split. I
   did not verify a precise correspondence between "≤n cuts" and "≤n merge operations" in
   the time budget — the correspondence is suggestive (each cut ~ each internal tree node)
   but the objective being optimized (weighted path length in Huffman vs. alternating-sum
   S here) is NOT literally the same functional, so this needs a genuine translation step
   before it can be called equivalent. Flag as a promising but unverified new angle, not a
   proof.

2. **Direct induction on the β-potential instead of on S (algebraically the same DP —
   checked, does NOT dodge the crux).** One might hope stating the induction target as
   "β ≥ s·(2^k−1)/D_k for any A with sum s and ≤k parts/cuts" (rather than S ≤ s/D_k) gives
   a cleaner inductive step. Since S = 1−2β exactly (L4), this is a pure relabeling of the
   same recursion that induction-peel's Sub-claim B and alternating-sum-potential's Lemma D
   already attempt — the same "IH bound at k−1 is too weak by exactly the amount 2^{k−1}
   vs 2^k in the denominator" obstruction recurs verbatim. **This does not open new
   terrain**; I checked the algebra and it collapses to the identical inequality. Do not
   present this as a distinct approach — it is a notational variant of the existing
   induction-peel / alternating-sum-potential attempts.

3. **Hall's-theorem / bipartite-matching framing — checked, does NOT help.** One might hope
   to sidestep constructing an explicit pairing by invoking Hall's marriage theorem
   (knowledge_base.md "Hall's marriage theorem / SDR", line ~122) to prove *existence* of a
   good pairing without exhibiting it. But L4 already gives the optimal pairing in closed
   form (consecutive elements of the sorted final list) — there is no matching-existence
   question left to resolve; the entire difficulty is which final *sorted list* (i.e. which
   cuts) XY should produce, not whether some pairing of it is good. Hall's theorem answers a
   question this problem doesn't have. **Blocked — this framing has no traction here.**

4. **LP/calculus reduction of the per-allocation inner problem (partial reduction, not a
   full escape).** For a *fixed* choice of how many sub-cuts go to each original piece of A
   (a fixed combinatorial "allocation" c_j per piece a_j), the inner minimization of S(B)
   over the continuous split points is a piecewise-linear/order-statistics functional of the
   split ratios. Standard calculus (or the envelope theorem, as already used in the
   smoothing-extremal approach's Berge-continuity argument) shows the minimum over split
   points is attained where new sub-parts exactly hit an existing rank-boundary value — i.e.
   at "match against an existing piece exactly" or "bisect exactly in half" configurations.
   This would justify, ex ante, why match/bisect are the *only* candidate optimal moves (a
   real structural simplification of the case analysis), but it does **not** resolve the
   combinatorial outer question of *which* allocation across pieces / *what order* to spend
   the n cuts — that remains the genuine multi-step lookahead problem (F1). Worth having a
   builder state this reduction explicitly (it legitimizes restricting attention to
   match/bisect moves, closing a possible reviewer objection "why only these two move
   types?"), but it is a lemma *inside* the existing induction-peel route, not a rival
   top-level target.

5. **Charging/amortized-argument reframe borrowed from bin-packing greedy proofs (crux
   `aimo-0012`, technique analog only).** aimo-0012 (IMO-style: partition [0,1]-bounded
   reals summing to n into ≤2n−1 groups each summing ≤1) proves its bound via "greedy fill
   forces each closed group past a threshold, then charge the total against the per-group
   surplus" — a clean charging/potential scheme quite different in content but structurally
   similar in shape to what Sub-claim B needs: an accounting argument that charges each cut
   against the "surplus" it recovers, summing to the exact 1/D_n deficiency, rather than a
   case-by-case ratio threshold (r = a_1/ρ) as induction-peel currently frames it. This is
   a technique suggestion, not a solved analog — the objective functions differ (bin
   capacity vs. alternating-sum), so the charging scheme would need to be built from
   scratch, but it is a genuinely different bookkeeping style worth trying on Sub-claim B /
   Lemma D before falling back to raw ratio casework.

### Numeric probe this round (new negative result, rules out one more candidate rule)

Tested the **simplest possible universal XY rule**: ignore "match" entirely; for each of
the n cuts, find the current single largest piece anywhere in the multiset and bisect it
in half; repeat n times, independent of A's shape. This is a genuinely different
(dumber, global, no case-split) candidate than any rule tried in prior rounds.

Result (2000 random LB partitions per n, n=1..4): **fails badly and often** — 17–75% of
trials exceed the target, with the worst failures on the *simplest* inputs: a single
piece A={1} with n cuts gives S=0.5 (n=2, target 1/7) or S=0.25 (n=4, target 1/31) instead
of the ≈1/D_n needed, because pure bisection without ever "matching" wastes every cut
re-halving the same piece instead of pairing off a companion original piece. This
reconfirms (via yet another concrete rule) the field's F1 finding: **any surviving rule
must include a genuine "match against a specific other piece" option, not just
bisection**, and must decide when to stop spending cuts — a decision that needs knowing
the whole remaining piece list, not just the current largest piece. Do not propose
"repeatedly bisect the global max" as a strategy; it is now a confirmed dead end.

### Candidate techniques

- Genuine backward-induction / DP on the full recursion V_k(A) (induction-peel's stated
  plan) — still the most concrete route, needs the two branch inequalities of Sub-claim B
  actually proved (this is the real remaining work, not sidestepped by any framing found
  this round).
- Huffman/merge-tree exchange lemma (opening 1) — worth a dedicated approach slot to see
  if the correspondence can be made rigorous; genuinely different bookkeeping from
  match/bisect casework even if it likely proves the same underlying fact.
- Charging/amortized argument in the style of aimo-0012 (opening 5) — worth trying as the
  proof *style* for closing Sub-claim B, rather than the current ratio-threshold casework.

### Cheap-kill candidates

None new. Reconfirmed existing ones: tied largest pieces cancel for free (β gains their
full mass at zero cost); a single unmarked piece (A={1}) is never a tight case (XY reaches
≈1/2 ≪ 1/D_n with one bisect, confirmed again this round).

### Knowledge-base entries to use

- "Invariants & monovariants" (line 117) and "Pigeonhole / extremal principle" (line 108)
  — generic pointers, already used by the field.
- "Hall's marriage theorem / SDR" (line 122–124) — checked and does **not** apply here (see
  opening 3); flag so no future round wastes a round rediscovering this dead end.
- No KB entry names Huffman coding / merge-tree exchange arguments; would need to be
  stated and proved from scratch if opening 1 is pursued.

### Analogous past problems (cruxes)

- `aimo-0012` (combinatorics, bin-packing/greedy-charging): "greedy fill forces each
  closed part past a threshold, charge the total against the per-part surplus" — a
  technique analog (amortized charging argument) for closing Sub-claim B's accounting, not
  a content analog (different objective functional). Best candidate found this round.
- Reconfirming round-2's finding: no crux under `games-and-strategy` or
  `processes-and-algorithms` in combinatorics is a genuine continuous-value optimization
  analog to this stick game; searched again this round (434 cruxes across
  processes-and-algorithms/games-and-strategy/invariants-and-monovariants/extremal-principle),
  found nothing closer than aimo-0012's charging-style technique.
- `aimo-0117` (dyadic/superincreasing extremal construction) remains the best analog for
  *why* dyadic is the extremal LB profile, already flagged in round 2 — still not a proof
  technique for the upper-bound construction itself.

### Prior progress

L0–L4 fully certified (see `lemmas/`). Lower bound proven when XY leaves the top dyadic
piece uncut (Case 1 / case (i)); binding case (XY cuts the top piece) is open (G1). Upper
bound is open in general (G2 / Sub-claim B / Lemma D) — the shared crux across
induction-peel and alternating-sum-potential. smoothing-extremal is RETHINK (Lemma G
numerically refuted; its surviving weaker claim re-imports the crux). No approach this
round or last has closed either remaining gap; all genuinely new framings tried either
collapse notationally onto the existing DP (opening 2) or don't apply (opening 3).

### Dead ends (do not retry)

- Any one-pass/local match-vs-bisect rule comparing only carry to the next piece — 15–30%
  failure rate, established round 2 (finding F1).
- "Concentrate cuts on the largest part only" — refuted round 1 (counterexample
  {0.428,0.410,0.162}).
- Sum-preserving consecutive-pair smoothing toward ratio 2 (Lemma G) — refuted round 2
  (7/20 sampled moves decrease S* instead of increasing it; structurally can't even connect
  generic A to G_n since it fixes each pair's sum).
- **NEW this round: "repeatedly bisect the current global-largest piece, ignore
  matching"** — refuted (17–75% failure rate across n=1..4, worst case a single unmarked
  piece A={1}, where pure bisection wastes cuts re-halving the same piece instead of
  matching a companion). Confirms matching is not optional machinery — it is essential.
- Hall's marriage theorem / bipartite-matching-existence framing — does not apply; L4
  already gives the optimal pairing in closed form (consecutive sorted elements), so there
  is no existence-of-matching question left open; the difficulty is entirely in choosing
  the cuts, not the pairing.
- β-potential induction as a literal restatement of the S-induction — algebraically
  identical to the existing DP (S=1−2β), inherits the exact same "IH too weak by a factor"
  obstruction; not a new opening.

### Small-case / intuition notes (conjecture unless marked exact)

- Exact (symbolic, not just numeric): the dyadic fixed point matches the match-every-step
  recursion for n=1,2,3 (2/3, 4/7, 8/15) — internal consistency check, not new evidence of
  the general bound.
- Conjecture (strong, thousands of trials across rounds): for every tested LB partition
  some ≤n-cut response reaches S ≤ 1/D_n; the bound itself is not in doubt, only the clean
  explicit-strategy proof.
- New this round: pure-bisection-only strategies are uniformly and badly wrong (worst
  observed: S=0.5 vs target 1/7 at n=2, a factor-3.5 miss) — strengthens the case that any
  valid proof of the upper bound must explicitly use the match operation and must decide,
  based on global information (the whole remaining multiset), when to stop spending cuts —
  i.e. genuine lookahead/backward induction is not just sufficient but *necessary*
  machinery; no shortcut framing found this round avoids it.
