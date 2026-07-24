## imo-2026-03

Shared certified imports (all three approaches use these; do NOT re-prove):
`lemmas/endgame-greedy.md` (Lemma 0: LB payoff = Odd(P) = sum of odd-ranked pieces; greedy
optimal), `lemmas/layer-cake-alt-sum.md` (f(P)=Σ(-1)^{i+1}a_i = M(P)=measure{t:c_P(t) odd};
P1 matched-pair invisibility; Lemma 3 single-cut parity-flip; matching-cost form). Reduction
`c(n)=(1+V_n)/2`, `c(n)=2^n/D_n ⇔ V_n:=max_LB min_XY f = 1/D_n`, `D_n=2^{n+1}-1`. Already
certified: n=1 both bounds; LB Case 1 (top uncut) `f=2^n-f(R')≥1`; Case-2 decoupling
`f=(s_1-2^{n-1})^+ + f(Q)`.

Field rationale (breaking the single-gap trap): all three round-1 approaches shared BOTH
gaps and the same closer-less reduction. This round each approach closes GAP-L and GAP-U by a
**different mechanism** — (1) induction on cut-budget via the telescoping cascade, (2)
one-shot min-weight-matching certificates (no induction), (3) a turn-by-turn game-value
recursion via strategy-stealing (no scalar-minimax reduction at all). Different walls.

---

self-similar-recursion: revise
Target: Prove c(n) = 2^n/(2^{n+1}-1) (both bounds).
Technique: Strong induction on the **cut-budget k**. Spine = the telescoping bisection
cascade `min_{≤k cuts on W_m} f = f(W_{m-k})` (numerically exact n≤4, all k; verified this
round: f(W_m)=2^m−f(W_{m-1}), f(W_0)=f(W_1)=1,3,5,11,21…), which unifies LB Case 1 and Case 2
into ONE induction (no top-vs-R split), plus a dominant/balanced **regime-split** recursion
for the upper bound.
Skeleton (LOWER BOUND — closes GAP-L):
  1. Restate scaled goal: for W_n={1,2,…,2^n}, every ≤n-cut XY response has f≥1 — by Lemma 0
     reduction (certified).
  2. Strengthened invariant (CASCADE): for W_m and any placement of ≤k cuts anywhere,
     f(final) ≥ f(W_{max(m-k,0)}). Setting m=k=n gives f ≥ f(W_0)=1, closing Case 1 AND
     Case 2 simultaneously.
  3. Prove step 2 by induction on k (m fixed, then induction on m). Base k=0: equality.
     Inductive step reduces via the EXCHANGE LEMMA (key lemma below): XY's cut-minimizing
     first move is to bisect the current top 2^m, which by P1 collapses
     `{2^m}∪W_{m-1} → W_{m-1}` (three copies of 2^{m-1}, two cancel) at cost 1 cut, leaving a
     W_{m-1}-shaped multiset with budget k−1; apply IH: f ≥ f(W_{(m-1)-(k-1)}) = f(W_{m-k}).
  4. Conclude V_n ≥ 1/D_n.
Skeleton (UPPER BOUND — closes GAP-U):
  5. For any LB multiset P_0 (≤n+1 pieces, sum 1), XY forces f ≤ 1/D_n. Strong induction on
     budget b (=n down to 0), strategy defined by a REGIME SPLIT on the top piece a_1:
       - DOMINANT regime (a_1 ≥ Σ(rest)): a_1 stays rank-1 whatever is done below it, and
         f = a_1 − f(rest_final). XY must CUT a_1 (breaking dominance) — bisect a_1 if
         a_1 > 2·a_2 (P1 deletes it, f = f(rest)), or top-match a_1→(a_2,a_1−a_2) if
         a_1 ≤ 2a_2 (P4 replaces {a_1,a_2} by {a_1−a_2}); recurse on the residual, budget b−1.
       - BALANCED regime (a_1 < Σ(rest)) with the residual already ≤ 1/D_b: STOP (spend no
         cut) — the untouched remainder already meets the cap.
  6. The adaptive stopping test is keyed to the target 1/D_b: stop the moment the current
     achievable f of the untouched remainder is ≤ 1/D_b (do not over-cut — fixed "bisect n
     times" overshoots, recorded dead end).
  7. Verify the recursion's residual bound closes to exactly 1/D_n at the dyadic worst case
     (a_1 = 2^n/D_n), the unique maximizer.
Key lemmas (claim + mechanism):
  - EXCHANGE LEMMA (the GAP-L crux): For W_m (and any partially-cascaded odd-multiplicity
    dyadic staircase), among all first-cut placements the one minimizing min-over-remaining-
    budget f is bisecting the current top piece, and it yields continuation value equal to the
    (m−1)-level problem — because a cut only flips c(t)'s parity on the flip-set [0,x)∪[p−x,p)
    (Lemma 3, measure ≤ piece length), and only a cut of the top piece reaches the high
    thresholds t∈[2^{m-1},2^m) that carry the top odd-band; cutting anything smaller leaves the
    top band intact so cannot reduce f below what a top-cut achieves (verified: bisecting a
    non-top piece of W_3 gives f≥5 vs the top-cut's 3). This is the load-bearing step and the
    honest remaining gap; the target statement and extremal line are now pinned.
  - CASCADE COLLAPSE (mechanism, from P1): bisecting 2^m in {2^m}∪W_{m-1} makes three 2^{m-1}'s;
    two cancel by matched-pair invisibility → W_{m-1}. Verified digit-for-digit n≤4.
  - REGIME DICHOTOMY (GAP-U): if a_1 ≥ Σ(rest) then a_1 is rank-1 under every refinement of the
    rest (every sub-piece ≤ Σ(rest) ≤ a_1), so XY cannot cancel it without cutting it — forcing
    the cut-top branch; else the top pair can be matched/left. Explains why global bisect-all
    overshoots (it cancels inside dominant sub-blocks where a single cut can INCREASE local M).
Open gaps: the EXCHANGE LEMMA (GAP-L step 3) and the residual-accounting closure of the
regime-split recursion to exactly 1/D_n (GAP-U steps 5–7).
Cases to cover: LB — none beyond the single cascade induction (Case 1/2 now unified). UB —
dominant (a_1>2a_2), dominant (a_1≤2a_2, top-match), balanced/stop; base b=0 (≤1 piece over
budget ⇒ f=0).
Watch out for: f(W_0)=f(W_1)=1 (non-strict — do NOT assume each extra cut strictly lowers f);
the n-th cut is redundant at the LB floor. Do NOT cite the blanket "non-max cut never helps"
(FALSE, 28k counterexamples) — the exchange lemma is the RESTRICTED, provable version.

---

alternating-sum-threshold-potential: revise
Target: Prove c(n) = 2^n/(2^{n+1}-1) (both bounds).
Technique: **Min-weight perfect-matching duality** (Lemma 2, certified: f(P) = cost of adjacent
pairing = min-weight perfect matching on the line, phantom 0 if odd count). Both bounds become
one-shot certificate statements — NO induction on budget. GAP-L: a feasible dual (LP lower
bound) forcing every matching ≥ 1. GAP-U: an EXPLICIT sufficient matching of cost ≤ 1/D_n
(existence, not optimality — the easier direction of duality).
Skeleton (LOWER BOUND — GAP-L via dual certificate):
  1. GAP-L ⇔ every ≤n-cut refinement of W_n={1,…,2^n} has min-weight perfect matching cost ≥ 1
     (Lemma 2).
  2. Exhibit dual potentials: assign every real length ℓ a node-price φ(ℓ) with
     φ(u)+φ(v) ≤ |u−v| for all pairs u,v present, and Σ_pieces φ ≥ 1 for every refinement.
     Candidate: φ built from the dyadic threshold levels {2^{n-1},…,2,1} — φ(ℓ) counts a +1
     credit each time ℓ crosses a dyadic level, normalized so the geometric level-gaps sum to 1.
     Weak LP-duality (Σφ ≤ matching cost when φ dual-feasible) then gives cost ≥ Σφ ≥ 1.
  3. Feasibility must hold uniformly over ALL ≤n-cut refinements: cutting only splits a piece
     into two smaller ones, which can only ADD level-crossings (φ non-decreasing under
     refinement in total), so Σφ is monovariant-up under cuts ⇒ ≥ Σφ(W_n) = 1.
Skeleton (UPPER BOUND — GAP-U via explicit matching, opening 3):
  4. GAP-U ⇔ for any ≤n+1 pieces summing to 1, XY cuts ≤n times so SOME perfect matching of the
     result has cost ≤ 1/D_n.
  5. Constructive slotting: assign each LB piece to a canonical dyadic-scale target slot
     2^j/D_n; with one cut per piece (≤n cuts, leaving one piece unmatched-to-phantom) shave/
     split it so its matched partner differs by ≤ its slot gap; total matching cost telescopes
     to the geometric sum ≤ 1/D_n. Direct existence — never needs the optimal matching.
Key lemmas (claim + mechanism):
  - DUAL FEASIBILITY + MONOVARIANCE (GAP-L crux): the dyadic-level price φ is dual-feasible
    (φ(u)+φ(v) ≤ |u−v| by counting the levels strictly between u and v) and Σφ only increases
    under cutting (a cut of ℓ into x,ℓ−x adds the levels newly crossed, never removes any),
    so Σφ ≥ Σφ(W_n) = Σ_{j=1}^{n} (2^j−2^{j-1})/D_n = 1. This replaces induction-on-budget with
    a single global certificate — the reason to keep this approach far from self-similar.
  - EXPLICIT SLOT MATCHING (GAP-U crux): the cost of the constructed matching is
    Σ (slot gaps) = (2^n−2^{n-1}+…)/D_n handled so residual = 1/D_n; because a self-chosen
    (not optimal) matching only needs an UPPER bound, the re-sorting kinks that block LP duality
    on cut positions never appear.
Open gaps: constructing φ so that Σφ(W_n)=1 AND dual-feasibility holds for every refinement
(GAP-L); proving the slot construction's total cost ≤ 1/D_n for every LB marking, incl.
top-heavy configs [1,ε,…] where iterated-top-match failed (GAP-U).
Cases to cover: odd vs even piece count (phantom 0); GAP-U top-heavy vs near-equal markings.
Watch out for: Lemma 2 gives f = matching cost, so "matching ≥ 1" is literally "f ≥ 1" — the
value added here is a CERTIFICATE (dual weights / explicit primal), not a new inequality; if
the dual φ collapses to just re-deriving f by induction, this approach is not far enough from
self-similar and should pivot to the explicit-primal GAP-U half only. Do NOT pursue bare LP
duality on cut POSITIONS (payoff non-concave, re-sorting kinks — recorded dead end); duality is
applied to the fixed post-cut multiset only.

---

game-value-recursion: new
Target: Prove c(n) = 2^n/(2^{n+1}-1) (both bounds), directly as a recursion in the GAME VALUE.
Technique: **Strategy-stealing / self-similar scaling on the sub-stick**, proving a recursion
c(n) = φ(c(n−1)) with fixed point 2^n/D_n — a genuinely different top-level target that never
reduces to the scalar minimax f and never uses the layer-cake integral. Confronts the
budget-fungibility obstruction (the real combinatorial content flagged by the new-framing
explorer) head-on with an "adaptivity-across-regions gains nothing" lemma.
Skeleton:
  1. Split the stick into the top region (LB's top mark at 2^n/D_n, piece length 2^n/D_n) and
     the remainder [0, D_{n-1}/D_n], which LB marks as a SCALED copy of the budget-(n−1) dyadic
     game (relative sizes {2^0,…,2^{n-1}}/D_{n-1}).
  2. Turn-by-turn dominance invariant (replaces the global integral): as XY's cuts arrive one
     at a time in any adversarial order, maintain "the largest not-yet-subdivided dyadic value
     strictly exceeds the sum of all currently-smaller pieces" (the arithmetic fact
     2^j > Σ_{i<j} 2^i, the aimo-0117 dyadic-domination crux). This keeps LB's greedy claim of
     the current top piece guaranteed and yields f ≥ 2·max − Σ locally at each level.
  3. Budget-non-fungibility lemma (the key gap): XY spending a cut on the top piece vs. on the
     sub-stick can be decoupled — an optimal XY response spends greedily on the current largest
     piece, so the n-budget game value = (top-piece contribution) + (scaled (n−1)-budget game
     value on the remainder). This reduces the coupled game to the recursion.
  4. Solve the recursion: c(n) = 2^n/D_n · [stuff] with fixed point exactly 2^n/D_n; both the LB
     guarantee and the XY cap fall out of the SAME recursion (no separate GAP-L/GAP-U split),
     because the recursion is an equality in the game value.
  5. Verify base c(1)=2/3 (certified) and the fixed-point algebra 2·2^n/D_n − 1 = 1/D_n.
Key lemmas (claim + mechanism):
  - BUDGET NON-FUNGIBILITY (the crux, genuinely new content): an adaptive XY who watches one
    region before allocating cuts to another gains nothing over an XY who greedily attacks the
    current largest piece — because by Lemma 0 only "take/attack the current largest" is ever
    optimal, and the dyadic domination invariant (step 2) guarantees the top piece is always the
    unique largest until subdivided, so cross-region look-ahead cannot change the optimal cut
    target. This is the "adaptivity doesn't help" lemma every framing needs; proving it as a
    game-value statement (not a scalar-f statement) is what makes this approach far from the
    other two.
  - DYADIC DOMINATION INVARIANT (from aimo-0117): 2^j > Σ_{i<j} 2^i makes the top value
    unbeatable by the entire tail, so LB's greedy grab is safe turn-by-turn; the recursion
    inherits this at every scale.
Open gaps: the BUDGET NON-FUNGIBILITY lemma (step 3) — proving the coupled two-region game
decouples into top-piece + scaled sub-game; and closing the recursion φ to the fixed point
(step 4). Note f ≥ 2max−Σ alone is too weak once the top is subdivided — the invariant must be
tracked recursively per dyadic level, not once globally (recorded: do not resubmit bare
2max−Σ for Case 2).
Cases to cover: XY cuts land entirely in top region / entirely in remainder / split across both
(the fungibility case — the one step 3 must handle); base n=1.
Watch out for: this is the highest-risk approach (the decoupling may genuinely fail — the
explorer flagged budget-fungibility as the true obstruction). Its value even if it stalls: it
isolates the "adaptivity gains nothing" lemma as a named target that the other two approaches
also implicitly need. Keep it far from self-similar-recursion: that one inducts on a FIXED cut
count reducing to scalar f; this one recurses on the GAME VALUE with an adversarial move
ordering and never leaves game-space.

---

majorization-smoothing: retire (do not advance)
No new lead; one-shot majorization certificate provably non-monotone (round-1 dead end). Its
toolkit (P1–P4) is fully absorbed into the two revised approaches above. Recommend dropping from
the build set unless the reviewer wants it kept as a certified-lemma host.
