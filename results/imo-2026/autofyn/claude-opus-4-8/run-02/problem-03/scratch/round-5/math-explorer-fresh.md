## imo-2026-03

### Framing goal
Both live routes (`self-similar-recursion`, `block-recursion-tievertex`) attack the residual by
proving **integrality of the minimizer's sub-piece values** (via a forest/unimodularity argument
on the tied vertex, differing only in *which* square 0/1 system they show is unimodular). Both are
stuck because a genuine continuum of non-integer f=1 minimizers exists, so "integer at THIS
selected vertex" keeps needing ad hoc restriction (Φ-maximality, cross-tie-only). Below are
openings that try to prove `f≥1` **without ever concluding any sub-piece is an integer**.

### Distinct openings

**A. Per-cut amortized budget / discrete monovariant induction on cut count (top candidate).**
Do NOT characterize the argmin's algebraic structure at all. Instead define
`v(b) := min over all ≤b-cut refinements of the CURRENT worst-case configuration of f`, and prove
directly, cut by cut, that XY cannot decrease `f` by more than `f(W_{n-k+1}) − f(W_{n-k})` on the
`k`-th cut, so that after `n` cuts `f ≥ f(W_0) = 1` (Jacobsthal: `f(W_m) = (2^{m+1}+(−1)^m)/3`,
verified `f(W_0..5) = 1,1,3,5,11,21`). The per-cut decrease bound is available from the **already
certified** `cut-slide-derivative` (Lemma I) in its exact "two-band" form: splitting a piece of
value `V` into `V1,V2` flips the odd/even-count parity indicator (Lemma L) on two disjoint bands,
each of length `min(V1,V2)`, one at the LOW end of the piece's occupied `t`-range and one at the
HIGH end; `f` changes by `±(band1 length) ± (band2 length)` depending on the CURRENT parity in
each band (independent signs). This gives an *exact per-cut identity*, not just a bound, and is a
genuinely different top-level target: an induction on the ADVERSARY'S MOVE SEQUENCE (a discrete DP
value function on cut budget) rather than on the geometry of the final vertex. It reuses the exact
same "delete/subtract via reachability" flavor of argument that closed GAP-U — never invokes
integrality at all.
*Why it might work:* GAP-U's successful proof (`delete-subtract-reachability` + `subset-sum-
pigeonhole`) is a nearly verbatim structural template — it proved an UPPER invariant `g_b(P)≤s/D_b`
by amortized per-cut accounting; this opening seeks the mirror LOWER invariant
`h_b(P) ≥ f(W_{n-b})`-type bound via the same style of induction on cut budget `b`, using the
certified two-band derivative instead of a new tool.
*Main obstruction:* the sign of the parity flip in each band depends on the GLOBAL configuration
of already-placed cuts (not just the piece being cut), so bounding "worst case single-cut
decrease" requires controlling which piece XY cuts and in what order — this is exactly the
difficulty that forced round 1's Case-1/Case-2 split and that self-similar-recursion's induction on
`N` also had to face. The opening does NOT trivially dissolve the hard part; but it changes the
proof's OBJECT from "classify the minimizer" to "bound the recursion," which may admit an
adversary argument (show: XY's single best cut, against ANY current configuration reachable with
`b−1` more cuts pending, is dominated by cutting whichever piece currently plays the role of the
top dyadic piece) instead of vertex/LP machinery.

**B. Generalized top-band peeling via Lemma BD applied recursively (peel by "current rank-1 piece"
identity, not by cut count).** `Lemma BD` (block-decomposition, ALREADY PROVEN in full in
`block-recursion-tievertex.md` §2 — a rank-contiguous run of one original piece's sub-pieces
contributes `σ_a · f_block(own values)`) currently is used only to eliminate WITHIN-piece ties.
Push it further: whichever original piece is CURRENTLY the largest (occupies rank 1) after XY's
cuts, its sub-pieces are NOT guaranteed rank-contiguous in general (this is exactly why round 1's
Case 2 was hard), but *if* one can show XY's optimal disruption never benefits from breaking
contiguity of the top piece (a structural/exchange claim about WHERE cuts go, provable purely by a
rearrangement argument on Lemma L's count function, no integrality), Lemma BD gives an exact
recursive identity `f(P) = σ_1·f_block(top piece's own sub-pieces) + f(rest)` peeling one dyadic
level per application, closing the induction purely combinatorially.
*Why it might work:* it reuses a lemma the field has ALREADY certified as sound (Lemma BD, distinct
from the rejected Lemmas W/S/T), just aimed at a different target (top-level recursion instead of
within-piece elimination).
*Main obstruction:* the contiguity-preservation claim ("XY never gains by scattering the top
piece's sub-pieces among other ranks") is exactly the open combinatorial content and is not yet
proven — it may be false in general (needs the same stress-testing discipline as the round-1
"blanket domination" claims that were disproved with counterexamples).

**C. Direct explicit adversary/pairing strategy for Liu Bang bypassing `f` entirely.** Use
`Lemma 0` (endgame-greedy: LB's payoff = sum of odd-ranked pieces) directly: construct an EXPLICIT
injection `φ` from XY's claimed (even-rank) pieces to LB's claimed (odd-rank) pieces with
`φ(x) ≥ x` for every `x`, using the ORIGINAL dyadic block labels (not rank position) as the pairing
key — e.g. pair each even-rank sub-piece with an odd-rank sub-piece descended from the SAME or an
ADJACENT dyadic block `2^k`. If such an injection exists with strict inequality except on a
residual mass of ≤ 1 (in D_n-scaled units), `Odd(P) ≥ Even(P)` plus the residual gives
`f = Odd−Even ≥ 1` directly, with no vertex/minimizer language at all.
*Why it might work:* this is the genuinely different top-level target CLAUDE.md/round-4 dispatch
asks for — game-strategy-level, not potential-minimization. It parallels crux `aimo-0596`'s
"partner-mirroring... seed the responder with one floating card" pairing template (a take-turns
game where an explicit involution/pairing certificate settles the outcome without computing an
extremal function) — genuinely analogous IN STRUCTURE (pairing certificate for an alternating-turn
game), though the game mechanics differ (here pieces, there cards).
*Main obstruction:* no candidate injection has been constructed or tested; rank order (not piece
origin) determines who claims what, so building an origin-based injection that provably respects
the actual claim order is nontrivial — this is a fresh construction task, not a known dead end.

**D. Quadratic (SOS-style) dual certificate on `f`, distinguished from the killed LINEAR dual.**
Round 2 proved a *linear, length-only* dual price is dead (forced ≤0 by equal-piece feasibility).
Untried: a certificate of the form `f(P)·D_n − 1 ≥ Σ_k λ_k·(x_k − 2^k/D_n)^2 ≥ 0` or similar
quadratic-in-cut-position identity, i.e. show `4·D_n·f(P) − 4 = (\text{explicit sum of squares in
the cut coordinates})` directly from the piecewise-affine formula for `f`, so nonnegativity is
manifest algebraically without any minimizer classification.
*Why it might work:* SOS certificates prove global inequalities over compact semialgebraic sets
without needing to locate or classify the minimizer at all — directly targets "prove `f≥1`
everywhere," sidestepping integrality completely.
*Main obstruction:* `f` is only piecewise affine (not smooth, not obviously polynomial in a useful
sense across sort-chambers), so an SOS decomposition would have to be chamber-by-chamber, likely
reintroducing the same case explosion the vertex-based routes already hit; no partial computation
done yet — purely speculative, higher risk than A–C.

### Candidate technique(s)
Discrete/amortized induction (à la GAP-U's delete-subtract-reachability), recursive block-
decomposition peeling (Lemma BD), explicit pairing/injection certificate on the endgame-greedy
claim order (Lemma 0), speculative SOS certificate.

### Cheap-kill candidates
- For opening A: before building the full DP, cheaply verify (already partially done, see memory)
  that `min_{k cuts total, any placement} f(W_n) = f(W_{n-k})` EXACTLY for small `n` via brute
  force LP/rational-vertex enumeration (not just descent-heuristic search) — if a *counterexample*
  configuration beats `f(W_{n-k})` for some `k<n`, opening A is dead immediately, cheaply.
- For opening C: cheaply test candidate pairings (e.g. "pair even-rank piece with the odd-rank
  piece from the nearest dyadic block below it") against the known residual example
  `{4/3,4/3,4/3,2,1}` (`f=5/3`) and `{2,3,3}` (n=3 case) by hand/script before investing in a
  general proof — quick pass/fail on 2 known hard instances.
- Parity/size check: any opening claiming a clean recursion should reproduce the EXACT Jacobsthal
  values `f(W_0..5)=1,1,3,5,11,21` (verified above) as its base/reduced cases — a fast sanity gate.

### Knowledge-base entries to use
`knowledge_base.md` was not yet consulted in depth by me this round (time budget); the certified
in-repo lemma cache functions as the operative "knowledge base" here: `layer-cake-alt-sum`,
`endgame-greedy`, `cut-slide-derivative` (Lemma I, exact two-band mechanism for opening A),
`delete-subtract-reachability` + `subset-sum-pigeonhole` (GAP-U's template, to mirror for opening
A/B), and the (already-certifiable, not yet formally certified) **Lemma BD** in
`block-recursion-tievertex.md` §2 (block-decomposition identity, for opening B).

### Analogous past problems (cruxes)
- `aimo-0596` (combinatorics, games-and-strategy) — "partner-mirroring pairing strategy... seed the
  responder with one floating card so the final invariant lands on a card it already holds."
  Genuinely analogous IN STRUCTURE to opening C: an alternating-turn claiming game settled by an
  explicit pairing/involution certificate rather than computing an extremal potential. Worth
  reading in full if opening C is pursued.
- `aimo-0003` (combinatorics, invariants-and-monovariants) — "running ±1 tally, minimum value ever
  recorded equals an invariant count; proved by induction deleting an innermost matched pair."
  Loosely analogous (a running-tally / matched-pair-deletion induction resembling `Lemma L`'s
  count function and `P1`), but the field already uses this exact technique (matched-pair
  invisibility) — not a new lever, just confirms the existing toolkit is the right genre.
- No corpus entry matches the SPECIFIC "prove global min of an alternating-sum-of-sorted-values
  functional over a cut-refinement polytope is ≥ a threshold" shape; nothing closer than the two
  above was found.

### Prior progress
Upper bound (GAP-U) fully proven and certified (not touched by this lens). Lower bound (GAP-L)
proven for all cases except the tied non-degenerate minimizer. See `current.md` and both live
approach files for full detail — not re-summarized here since the dispatch focused me on fresh
openings, not re-verifying the existing 90% (which I did read and did not find inconsistent with
`run_state.md`'s account).

### Dead ends (do not retry)
- Global integrality of the minimizer (continuum of non-integer f=1 minimizers, round 4).
- Odd-integer-floor / parity argument at tied real vertices (fails, round 3).
- Linear length-only LP dual certificate on `f` (round 2, proven dead — opening D explicitly avoids
  this by going quadratic; if opening D is attempted, do NOT collapse it back to a linear price).
- Assuming within-piece ties vanish at minimizers (`{2,3,3}` counterexample, round 4).
- "P1-cancel any two equal-valued pieces regardless of origin, repeatedly, to reach a tie-free
  core" — I verified this reduction is real (`f(P)=f(P̃)`, `P̃`= odd-multiplicity value core, a
  direct corollary of Lemma L/P1) but it breaks the dyadic sum conservation `Σ=2^k` needed to tie
  `P̃` back to `D_n`/parity (this is the exact wall already flagged in `current.md`'s residual
  description) — do not re-propose this as a fresh idea, it is the SAME wall in new clothes.

### Small-case / intuition notes
Jacobsthal values `f(W_m) = (2^{m+1}+(−1)^m)/3` for `m=0..5`: `1,1,3,5,11,21` (computed exactly,
matches memory's round-2 note) — this is the conjectured floor `min_{k cuts} f(W_n) = f(W_{n−k})`,
strongly supporting opening A's target identity but NOT yet proven as an exact per-cut recursion
(only as an endpoint numeric match). All of this is corroborating/conjectural, not new proof.
