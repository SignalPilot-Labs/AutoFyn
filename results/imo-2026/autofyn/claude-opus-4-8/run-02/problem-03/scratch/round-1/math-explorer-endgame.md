## imo-2026-03 (lens: claiming-game endgame)

### Setup recap
Liu Bang marks ≤n points, then Xiang Yu marks ≤n points (all distinct), stick is cut
into pieces, players alternately claim a whole unclaimed piece (Liu Bang first),
each maximizing his own total length. Find the largest c Liu Bang can guarantee.

### The endgame lemma (proved, not just conjectured)

**Lemma.** Fix any multiset of nonnegative reals (the final pieces) summing to S.
Sort them descending a_1 ≥ a_2 ≥ … ≥ a_m. In the alternating-claim sub-game (mover
picks any unclaimed piece, both maximize their own eventual total — equivalently,
since the total is fixed at S, each is also minimizing the opponent's total, so
it is a genuine adversarial/zero-sum game), the **unique game value** is: the
first-to-move player receives exactly a_1+a_3+a_5+… (odd ranks) and the second
receives a_2+a_4+… (even ranks). Greedy ("always take the currently-largest
remaining piece") is optimal for BOTH players, and it is essentially the only
optimal first move whenever a_1 is a strict max (ties don't matter — any tied
piece is interchangeable).

**Proof sketch (induction on m, exchange argument).**
- Base case m=0,1 trivial.
- Let V(L) = value to the mover of sorted list L. If mover takes a_1, by
  induction on the (m−1)-list {a_2,…,a_m} the opponent (now mover) gets
  a_2+a_4+…, so the original mover's total is a_1+(S−a_1)−(a_2+a_4+…) =
  a_1+a_3+a_5+…, matching the claim.
- To show taking a_1 is optimal (not just *a* consistent value), one needs the
  monotonicity sub-lemma: **if a multiset M' is obtained from M by increasing
  one element by δ ≥ 0, then V(M) ≤ V(M') ≤ V(M)+δ** (itself a short induction:
  case on whether the mover takes the increased element or not). Applying this
  to compare "mover takes a_1" vs "mover takes a_k" (k>1) — the two resulting
  (m−1)-element sub-games differ by exactly one entry increased from a_k to a_1
  — gives a_1 − V(L\{a_1}) ≥ a_k − V(L\{a_k}) for every k, i.e., taking a_1 first
  weakly dominates every other choice. This closes the induction.
- **I did not find this exact lemma verbatim in the crux corpus** (see below),
  but it is completely elementary and I verified it computationally: exhaustive
  backward-induction game-tree DP on 2000 random multisets of size ≤ 6 matches
  the greedy closed form to machine precision in every case (script:
  `/tmp/verify_endgame.py`, all 2000 trials pass). Treat the lemma as **proved**,
  not conjectured — the outliner can write the induction above directly; only
  the monotonicity sub-lemma needs a half-page write-out.

### Translating the lemma to the whole problem

- Liu Bang's n cuts alone produce n+1 pieces. If Xiang Yu then uses all n of his
  cuts, each strictly inside some existing piece and at a fresh point, the final
  piece count is exactly **m = 2n+1** (odd) — assuming general position (no
  coincidental alignment; Xiang Yu never benefits from *fewer* effective cuts,
  see below). So generically the game reduces to: Liu Bang picks the initial
  (n+1)-part composition, Xiang Yu picks how to further cut it into 2n+1 parts
  (subject to "each new cut lies inside one current piece"), then apply the
  Lemma: **Liu Bang's total = sum of the n+1 largest-ranked pieces at odd
  positions 1,3,…,2n+1 in the final sorted list of 2n+1 pieces.**
- Structural fact from piece count alone: with m=2n+1 odd, the first player
  always ends up with exactly n+1 of the 2n+1 pieces (one more piece than
  Xiang Yu), by the parity of rank positions — this holds regardless of the
  actual sizes. But **this is a count fact, not a value fact**: it does NOT
  by itself give Liu Bang more than half the *length*, because Xiang Yu
  controls which pieces occupy which size-ranks.
- **Key subtlety I found (important — corrects a naive guess):** the natural
  first guess is that Liu Bang should aim to force the final 2n+1 pieces to be
  *equal* (each 1/(2n+1)), which by the Lemma would hand him (n+1)/(2n+1).
  Concretely for n=1, cutting at x=2/3 (pieces 1/3,2/3) forces Xiang Yu's best
  response (bisect the 2/3 piece) into three equal 1/3 pieces, giving Liu Bang
  2/3. I verified this is the true n=1 optimum by full calculus (see below):
  **c(1) = 2/3 exactly**, matching (n+1)/(2n+1) for n=1.
  However, for n=2 I built the natural generalization (Liu cuts to get pieces
  1/5, 2/5, 2/5, anticipating Xiang Yu bisecting each 2/5 piece into two 1/5's
  to reach five equal 1/5 pieces, which would give Liu Bang 3/5=0.6). **This
  construction FAILS badly**: Xiang Yu's actual best response is not to
  bisect both 2/5 pieces — it is to dump *both* of his cuts onto the smallest
  piece (the 1/5 one) and cut it into three pieces sized so that its own
  "half" (one particular sub-piece, positioned at an even rank) captures
  almost exactly half of that small piece's mass, while contributing a
  near-zero "dust" sub-piece that Liu Bang is left holding at the very bottom
  rank. Net effect (numerically verified, exact grid search over both of
  Xiang Yu's cut placements): Liu Bang's total collapses to **≈0.502**, barely
  above half — because the two 2/5 pieces, being **equal to each other**, are
  a wash (Liu gets one, Xiang Yu gets the other, no edge from them at all),
  and Xiang Yu neutralizes essentially all of the value hidden in the small
  piece too. So "equalize all final pieces" is the WRONG heuristic for n≥2;
  Liu Bang must avoid creating equal/duplicate large pieces (they cancel his
  first-move edge) and must protect small pieces from this
  "shred-to-near-bisect" attack.
- I then searched (numerically, grid + randomized local search, not exhaustive)
  for a better n=2 construction for Liu Bang and found configurations reaching
  **≈0.57–0.58** (e.g., pieces roughly (0.14, 0.28, 0.58) or (0.27,0.58,0.14)-type
  splits), still below the naive 0.6 guess but well above the degenerate 0.502.
  I could not pin an exact closed form for c(2) in the time available — this is
  a genuine open computation for the outliner/builder, not a proved value.
  **Do not assume c(n) = (n+1)/(2n+1) for n ≥ 2** — it is unverified and my
  n=2 evidence suggests it is very likely too high (the true value is probably
  strictly below 3/5, closer to 0.57 based on search, but not confirmed exact).

### What remains (translation gaps for the outliner)
1. Formalize why Xiang Yu, in general position, always uses all n cuts and
   never benefits from making fewer cuts or from placing a cut exactly at an
   existing boundary (should be an easy monotonicity/continuity argument once
   the Lemma is in hand — more cuts weakly help the second cutter since it
   only gives him more freedom in the sub-game, i.e. a "more options can't
   hurt" argument, but this should be checked, not assumed).
2. Characterize Xiang Yu's optimal response to a *general* (n+1)-piece Liu
   Bang composition — the "shred-to-bisect" phenomenon needs to be understood
   in full generality (how does the optimal split of a chosen sub-piece behave
   as a function of the other 2n pieces already fixed? It looks like an
   optimization "give away the top rank of the split, keep the rest" pattern).
3. Find Liu Bang's actual optimal composition (the analogue of x=1/3 for n=1)
   for general n, and prove optimality both directions (upper bound via
   Xiang Yu's best-response argument + matching Liu Bang construction).
4. Nail down whether ties / boundary configurations (equal pieces) ever help
   Liu Bang, given the observed cancellation effect for n=2.

### Cheap-kill / structural facts
- Piece count is always ≤ 2n+1, and Xiang Yu will make it exactly 2n+1 in an
  optimal line (more cuts = more control, this should be checkable early).
- Any pair of exactly-equal pieces in the final configuration contributes
  *zero net edge* to whichever player would "expect" to benefit from the pair
  ranking — one goes to each player, canceling out. This means Liu Bang's
  advantage must come entirely from asymmetry, not from symmetric bulk. This
  is a clean structural fact worth stating and using directly as a bound tool
  (e.g., to show Xiang Yu can always force the top pieces into matched pairs).
- n=1 closed form: c(1) = 2/3, with explicit optimal Liu Bang cut x=1/3 (giving
  pieces 1/3, 2/3) and explicit Xiang Yu best response (bisect the 2/3 piece);
  verified by full one-variable calculus optimization over Liu's cut point and
  Xiang Yu's cut point (case analysis on median position), not just numerics —
  see derivation below.

### Small-case derivation (n=1, done by hand + checked numerically)
Liu Bang cuts at x ∈ [1/2,1) giving pieces (1−x, x). Xiang Yu cuts the larger
piece x into (y, x−y). With m=3 pieces, Liu Bang (mover) gets ranks 1,3 and
Xiang Yu gets rank 2 (the median) by the Lemma; Liu Bang's total = 1 − median.
Case x < 2/3: Xiang Yu's best is y=1−x, giving median=1−x exactly (pieces
1−x, 1−x, 2x−1), so Liu Bang gets x.
Case x ≥ 2/3: Xiang Yu's best is the equal split y=x/2, giving median=x/2, so
Liu Bang gets 1−x/2.
Liu Bang then picks x to maximize min(x, 1−x/2): the two branches meet at
x=2/3 with value 2/3, and this is the max (branch 1 increasing in x, branch 2
decreasing). **c(1)=2/3, attained at the fully-symmetric endpoint where the
final three pieces are all equal to 1/3.** (Numerically reconfirmed via
`/tmp/game.py`: random/grid search over Liu's cut and Xiang Yu's response gives
≈0.665–0.668, consistent with 2/3.)

### Knowledge-base entries to use
I did not find an existing "alternating claim game" theorem in
`knowledge_base.md` (grepped for game/greedy/alternat/claim/stick/cut — nothing
directly on point). The Lemma above should probably be recorded as a new
reusable fact once certified, since it is the backbone of both the upper and
lower bound halves of this problem.

### Analogous past problems (cruxes)
Searched crux corpus, `domain=combinatorics`, `subtopic=games-and-strategy`
(39 entries) plus a keyword scan for "greedy"+"alternat/turn/pick/claim/largest"
combinations. **None are genuinely analogous.** The corpus's games-and-strategy
entries are mostly pairing/invariant/parity strategies for board/token games
(e.g. aimo-0461 knight-placement pairing, aimo-0117 dyadic-sequence game,
aimo-0596 XOR-pairing card game) — structurally different from a
continuous-length alternating-claim allocation game with a minimax adversarial
pre-cutting phase. aimo-0117 ("assign values as a dyadic sequence so the
largest strictly exceeds the sum of all others") is the closest in flavor
(extreme-value domination in an alternating-turn setting) but is not a genuine
match — it's a different game structure (choose-and-place, not claim-a-fixed-
piece). I recommend **not forcing a match**; this endgame lemma is elementary
enough to prove from scratch (as above) rather than borrowed.

### Dead ends (do not retry)
- "Equalize the final 2n+1 pieces" as Liu Bang's target construction — proven
  (numerically, exact grid search) to fail for n=2, collapsing his guarantee
  to ≈0.502 instead of the hoped 3/5, because equal pieces cancel the
  first-move edge and Xiang Yu's shred-to-bisect attack neutralizes the
  remaining small piece. Any approach that assumes c(n)=(n+1)/(2n+1) without
  re-deriving Xiang Yu's true best response is very likely wrong beyond n=1.

### Prior progress
None (no workspace existed before this round).
