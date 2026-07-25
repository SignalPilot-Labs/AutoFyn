## imo-2026-04 (shape-space / similarity-class + parametrization lens)

### Setup and exact cut formulas (derived, not conjectural)

Model a triangle by its angle-triple (A,B,C), A+B+C=180°, a point in the open
2-simplex (shape space — the game is similarity-invariant, so this loses no
information). A cut is: pick a vertex, say the one with angle A, and a point P
on the opposite side BC. Let t = ∠BAP ∈ (0,A) (so ∠CAP = A−t). By the exterior
angle / straight-angle relation at P (∠APB + ∠APC = 180°, both triangles share
side AP):

- **Child1 = △ABP**, angles = {B, t, 180−B−t}  (B unchanged from parent)
- **Child2 = △APC**, angles = {C, A−t, B+t}  (C unchanged from parent)

Sanity check: sums are 180 in each; ∠APB=180−B−t and ∠APC=B+t are supplementary. Cutting from B or C gives the same formula with roles permuted.

As t ranges over (0,A):
- Child1's third angle 180−B−t sweeps the open interval (C, 180−B), monotonically decreasing.
- Child2's third angle B+t sweeps the open interval (B, A+B) = (B,180−C), monotonically increasing.
- So the set of new angle-values reachable in **one child** (not necessarily both) from a single A-cut is (0,A) ∪ (C,180−B) ∪ (B,180−C) (plus the trivial carried-over values B, C).

### When can ONE cut force a win outright (both children get angle θ)?

Since Shan-Yu picks which child survives, a single cut is an immediate forced win **only if both children simultaneously get an angle = θ**. Matching the four combinations of {t, 180−B−t} (child1) against {A−t, B+t} (child2) gives exactly two nontrivial solvable cases (the other two force a degenerate 0-angle):

1. **t = θ and A−t = θ simultaneously** ⟺ **A = 2θ**, with t = θ = A/2. This is just: *bisect a vertex whose angle equals exactly 2θ*; then both children get angle θ at that vertex, unconditionally (t=A/2 is automatically in (0,A)). This is the master "double-win" mechanism, but it needs the **current** triangle to already have an angle = 2θ.
2. **180−B−t = θ−B** (child1 third angle) and **... ** — working through all four cross-matches, the *only* self-consistent one besides (1) forces **θ = 90°** exactly (t = 90−B, need 0<90−B<A, i.e. B<90 and C<90). This is just: *drop the altitude foot from the vertex opposite the two acute angles*; both children get a right angle at the foot. Since any triangle has at most one angle ≥90°, at least one vertex has both other angles acute, so **this always works** — θ=90° is a forced win in exactly one move from ANY starting triangle. This is a clean, fully-proved sub-result (not just numeric).

So: **θ = 90° is solved outright** (1-move universal win), and **whenever a live triangle has some angle = 2θ, Mulan wins in her next move** (mechanism (1), the "bisector trick").

### Multi-move dynamics: recursive escape looks like a Euclidean algorithm on (180, θ)

Beyond the immediate double-win, a single cut can plant an angle θ in **one** child only (Shan-Yu discards it) — but this constrains the *other* surviving child. E.g. cutting vertex A with t = 180−B−θ (so child1 gets a P-angle of exactly θ, discarded by Shan-Yu) forces the survivor child2 to have angles {C, θ−C, 180−θ} (needs θ>C). So Shan-Yu's escape carries a **180−θ angle forward**. Iterating this kind of forced trade (Mulan offers θ, Shan-Yu is pushed toward carrying 180−θ, or multiples/combinations of θ and 180−θ) smells exactly like a **continued-subtraction / Euclidean-algorithm process on the pair (180, θ)**, terminating in the mechanism-(1) double win precisely when the process closes up — i.e. when θ divides 180 evenly. This is a plausible mechanism explaining the numeric pattern below, but I have NOT verified it rigorously — flagging it as the most promising *proof* idea for "if θ = 180/n then Mulan wins," to be developed by the outliner/builder.

### Numeric experiment (strong conjecture, NOT a proof)

I implemented an exact fixed-point / backward-induction solver on an integer-degree grid (angles are integers 1..179, cuts restricted to integer split points, and I compute U = the set of triangles from which Mulan can force a win in a bounded number of moves, via monotone BFS: a triangle joins U if some vertex/cut gives **both** children in U ∪ {have angle θ}). This is a proxy (integer cuts only) but should already reveal the right structure since the "bisector"/"altitude" mechanisms above only ever need rational/integer cut points when θ is an integer.

Result, testing every integer θ from 1 to 179 (grid step 1, all ~2700 triangles with integer angles, sum 180, excluding any that already contain θ):

- **full=True (Mulan forces a win from EVERY triangle)** for θ ∈ {1,2,3,4,5,6,9,10,12,15,18,20,30,36,45,60,90} — i.e., **exactly the divisors of 180 that are < 180.**
- **full=False** for every non-divisor tested (19,21,25,35,37,40,41,44,50,55,59,61,65,72,73,75,80,85,89,91,95,100,105,110,115,120,125,135,145,150,155,165,170,175,179 — checked exhaustively), even values very close to a divisor (19, 21 fail; 20 works; 72 fails despite 180/72=2.5 being close to an integer).

**Conjecture (strong numeric evidence, not proved): Mulan can force a win iff θ = 180°/n for some integer n ≥ 2.** Equivalently 180/θ ∈ ℤ, θ<180 ⟹ n≥2. This is a clean, IMO-plausible characterization and should be the target answer the outliner states and both directions (construction for θ=180/n; a Shan-Yu-invariant defense for θ≠180/n) should be built around.

Caveat: this grid search uses only integer cut points, so it is a *necessary*-condition check for "full=False" cases only in the weak sense that failing on the grid doesn't strictly rule out a real-valued strategy succeeding off-grid; but the "full=True" cases are fully constructive (an explicit finite BFS witness), so those ARE genuine (grid-realizable) forced wins. The interesting risk is a false negative (some non-divisor θ might still be winnable via irrational cut points that the integer grid can't see) — the outliner/builder should keep this in mind, though the cleanness of the pattern (exact divisors, no off-by-one noise) makes a false negative unlikely.

### Distinct openings for the outliner
1. **Direct double-win construction for θ=180/n:** try to build an explicit finite sequence of cuts (using the mechanism-(1) bisector trick recursively, or the "Euclidean algorithm on (180,θ)" idea above) that is forced regardless of Shan-Yu's choices, terminating after ≤ n−1 or so moves.
2. **θ=90° as a fully solved base case** (already rigorously shown above) — a good sanity-check/template for how a "both-children-hit-θ" forced win looks, to generalize.
3. **Shan-Yu's defense for θ ≠ 180/n:** look for an invariant Shan-Yu can maintain forever — e.g., all angles of the surviving triangle lie in a set closed under the child-angle formulas above and avoiding θ; likely related to residues mod θ or to the fact that 180 mod θ ≠ 0 leaves an unremovable "slack" angle that can always be routed away from θ.
4. **Reachable-angle interval bookkeeping:** the explicit formulas (0,A)∪(C,180−B)∪(B,180−C) for one-cut single-child reachability could be used to bound, for a fixed θ, exactly which triangles are "immediately vulnerable" (one move from mechanism-1), building the induction Shan-Yu-safe region from the outside in.

### Cheap-kill candidates
- θ=90° needs no induction at all — full 1-move proof already available (altitude-foot construction); use it as a template/lemma but not as a proxy for the general answer.
- Parity/counting: none obviously killing a swath of θ; the divisor-of-180 structure is multiplicative, not parity-based.

### Knowledge-base entries to use
- `knowledge_base.md` has an "Invariants & monovariants" strategy (search hit at line ~117, ~191) — directly relevant to constructing Shan-Yu's defense for non-divisor θ (find a preserved/monotone quantity that stays away from θ).
- No geometry-specific game entries found in knowledge_base.md; the games-and-strategy content there is generic (minimax framing, invariant search) — useful as vocabulary, not as a specific applicable theorem.

### Analogous past problems (crux corpus)
- Queried `domain=combinatorics`, `subtopic ∈ {games-and-strategy, processes-and-algorithms}` (87 cruxes) via `past_crux_moves_database.json`/`past_problems_database.json` per `crux_moves_documentation.md` field names.
- **Best analog: `aimo-0225` (RMM 2015, "counters on an n-gon" game).** Crux move: "Determine the game value by recursing on the 2-adic valuation of a difference that exactly halves at each relevant step, so the P/N status flips with each halving and depends only on the valuation's parity." The solution reduces a triangle-area game on a regular n-gon to an isosceles-triangle normal form, then to a halving recursion on arc-length differences (a,a,b) → (a, a±|a−b|/2, a±|a−b|/2), governed by v₂ of the difference. This is structurally the closest available crux to our shape-space dynamics: both games reduce a triangle-shaped state to a **halving/doubling recursion**, and both have answers governed by a clean divisibility/valuation condition on an integer parameter (there: v₂(n−3) odd; here, conjecturally: θ | 180). It is a genuine hint for proof technique (isolate a "canonical"/symmetric sub-family of states, e.g. isosceles-like configurations, then do an exact halving/doubling induction) but the game mechanics differ enough (turn structure, win condition) that no step is directly transferable — must be reproved from scratch.
- No triangle-cutting or angle-hitting game with a directly matching mechanic was found elsewhere in the corpus; geometry has no cruxes at all (per `crux_moves_documentation.md`), so this is a combinatorics-flavored analogy only.

### Prior progress
None — round 1, no `results/imo-2026-04/approaches/` entries yet (confirmed via `current.md`, Status: unsolved, "(none yet)").

### Dead ends (do not retry)
- None recorded yet (first round). Note for future rounds: my grid search treats non-divisor θ as universally losing for Mulan based on an *integer-cut* proxy; if a later approach claims a real-valued (irrational cut point) construction wins for some non-divisor θ, that should be checked very carefully against this numeric evidence before trusting it — the clean divisor pattern with no exceptions across 30+ tested non-divisors is strong counter-evidence.

### Small-case / intuition notes (all conjecture unless flagged "proved")
- **Proved:** θ=90° is a forced win in exactly one cut from any starting triangle whose angles are all ≠90° (altitude-foot construction, both children get right angle at the foot; always exists since a triangle has ≤1 angle ≥90°).
- **Proved (mechanism, not full solve):** if the *current* triangle has an angle exactly 2θ, Mulan forces a win in one more cut by bisecting that angle.
- **Conjectured (strong numeric evidence, exact-grid search, no exceptions found):** Mulan can force a win overall iff θ = 180°/n for some integer n≥2. This should be the outliner's target answer to prove in both directions.
- **Intuition for the "only if" direction:** since (0,A)∪(C,180−B)∪(B,180−C) never covers a full neighborhood of every possible target off a generic triangle (gaps exist for scalene triangles, confirmed by direct interval computation for e.g. (30,50,100): reachable single-child set = (0,30)∪(50,80)∪(100,130), with real gaps), Shan-Yu likely has room to always pick the "more balanced"/gap-preserving child when θ isn't a clean divisor of 180, but proving a clean invariant witnessing this is the open gap for the outliner.
