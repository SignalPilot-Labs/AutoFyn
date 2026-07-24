## imo-2026-04 (Mulan's Triangle Game) — survival/impossibility (⊆) lens

### FLAG: difficulty mismatch
`problems.jsonl` lists this as `difficulty_level: "medium"`, `difficulty_rating: 7` (not one of
the 39 "hard" problems CLAUDE.md says to target). Both round-1 explorers flagged this too. The
run has clearly committed to it anyway; I explored as dispatched, but the orchestrator should
confirm this is intentional.

### HEADLINE FINDING: the prior conjecture {90°/2^k} is WRONG — corrected to {90°/n : n ∈ ℤ⁺}

Both round-1 reports (forcing lens, adversary lens) concluded the winning set is
{90/2^k : k≥0} and treated the ⊆ direction as "prove nothing else is forceable." **This is
false — the actual constructive family is strictly larger: θ = 90°/n for EVERY positive
integer n (90, 45, 30, 22.5, 18, 15, 90/7, ...), not just powers of 2.** I found and verified
(exact `sympy.Rational` arithmetic, exhaustively simulating *all* of Shan-Yu's branch choices,
not just one line of play) a "peel" gadget that both prior explorers missed because they only
considered bisection (halving) as the choice-immune move.

**The peel gadget.** Split vertex A (other two angles B, C) at parameter x = θ (not x = A/2).
Using the standard cevian formula `child1 = (x, B, 180−x−B)`, `child2 = (A−x, C, x+B)`:
- child1 = (θ, B, 180−θ−B) — **always contains θ literally**, for ANY B. Shan-Yu will never
  pick this (it's an instant loss), so he is forced to child2.
- child2 = (A−θ, C, θ+B). If A = mθ for an integer m ≥ 2, this is **(  (m−1)θ, C, θ+B )** —
  contains (m−1)θ, again regardless of C, B.

So: if the *current* triangle has any vertex equal to mθ (m a positive integer ≥ 2), Mulan can
split it at x = θ and force Shan-Yu — no matter what he does — into a triangle containing
(m−1)θ. Iterating, m → m−1 → ... → 1, this reaches θ itself in exactly m−1 more moves,
**completely independent of the other two angles' values** (the gadget never needs to know or
control B, C).

**Bootstrapping from an arbitrary triangle.** The θ=90° one-move universal fork (proved
correct in both round-1 reports: pick any vertex whose other two angles are both acute — always
exists since a triangle has at most one angle ≥90° — cut at x=90°−B) forces angle 90° into the
surviving triangle from **any** starting triangle whatsoever, no assumptions needed.

**Chaining:** for θ = 90°/n (n a positive integer), first force 90° = n·θ (1 move, universal),
then peel n−1 times. Total ≤ n moves, **fully deterministic, works against every possible
starting triangle and every possible sequence of Shan-Yu discards.**

**Verified numerically** (exact rational arithmetic, full game-tree enumeration over all of
Shan-Yu's 2^(moves−1) choices, not sampling): confirmed for n = 1,2,3,4,5,6,7,10 against four
very different starting triangles — (97,51,32) generic, (170,7,3) very obtuse/skewed,
(60,60,60) equilateral, (1/3, 2/3, 179) near-degenerate — **every single leaf of the full game
tree contains θ exactly.** This is strong (though still finite-case, not a general-n proof)
confirmation that the peel+bootstrap construction is correct and n-independent in its
mechanism (the proof of the gadget itself is fully algebraic/exact, not numerical — the
numerics are a sanity check on the chaining/bookkeeping, not the core claim).

Also noted: peeling doesn't have to remove exactly 1·θ per step — splitting A=mθ at x=jθ (any
0<j<m) sends BOTH children to (jθ, ...) and ((m−j)θ, ...), i.e. both branches are themselves
still integer multiples of θ and both continue to reduce recursively — so Mulan can finish in
O(log m) moves via a "binary" splitting strategy instead of linear peeling. Doesn't change the
achievable set, just makes the strategy faster; worth a one-line remark in the write-up but not
essential to the characterization.

### A REAL (fully rigorous) impossibility result: θ > 90° is NEVER forceable

I found and verified a clean, complete inductive proof — not conjecture — that Mulan can
**never** force any θ > 90° (for any starting triangle that doesn't already trivially contain
θ, which Shan-Yu of course avoids):

**Lemma (complete classification of "1-move direct wins").** Given a triangle with a vertex A
(others B, C, none currently equal to θ — else the game already ended), there exists x ∈ (0,A)
making BOTH children `(x,B,180−x−B)` and `(A−x,C,x+B)` contain θ **iff** θ = 90° (works for any
B,C — the two "new" P-angles across the two children are always supplementary, and θ=90° is the
unique self-supplementary value) **or** A = 2θ (a specific, pre-existing angle requirement).
This is a complete case analysis: θ can enter child1 via x=θ or 180−x−B=θ, and child2 via
A−x=θ or x+B=θ (excluding B=θ, C=θ, already ruled out); the 4 combinations reduce to exactly
these two cases, the other two being degenerate (force a zero or negative angle). I checked
all 4 combinations by hand.

**Induction.** Define W₀(θ) = {triangles already containing θ}, and
W_{n+1}(θ) = W_n(θ) ∪ {T : ∃ split with both children ∈ W_n(θ)}; W(θ) = ∪ₙ Wₙ(θ) is exactly
Mulan's winning set (standard AND-OR reachability: Mulan picks the split, Shan-Yu picks which
child survives). For **θ > 90°**: the state-independent device (θ=90°) is unavailable, and the
state-dependent device (A=2θ) needs a pre-existing angle 2θ > 180°, impossible for any actual
triangle angle. So the Lemma gives W₁(θ) = W₀(θ). By induction, if Wₙ(θ)=W₀(θ) then
W_{n+1}(θ) also needs "both children ∈ Wₙ(θ) = W₀(θ)", i.e. both children directly contain θ —
the same Lemma, same conclusion, still impossible. Hence **Wₙ(θ) = W₀(θ) for all n**, so
**W(θ) = W₀(θ): a triangle can be forced to reach θ>90° only if it already contains θ.** Since
Shan-Yu is free to pick any starting triangle, he trivially avoids ever having θ present
(e.g. pick an equilateral triangle if θ≠60°, or any triangle avoiding θ), and this property is
preserved forever (the argument shows literally NO sequence of moves, however long, however
adaptive, can create θ>90° from a triangle that doesn't already have it). **This closes the
θ>90° case completely, rigorously, no gaps.**

This also explains, as a side effect, why 120°, 135°, etc. can never even serve as *intermediate*
targets (e.g. as the "A=2θ" precursor for some other target θ'=60°): 120°>90° is itself
unreachable, so it can never appear as a "gift" angle either. This closes off one obvious
loophole (an indirect two-hop construction 60° ← needs 120° ← needs ... ) automatically.

### The open sub-case: θ < 90°, θ ≠ 90°/n — still conjectural, but the mechanism is now clear

The SAME two-device Lemma applies for θ<90° too, except now A=2θ<180° is a legitimate,
achievable angle, so the induction does NOT trivially collapse — growth is possible, and DOES
happen (that's exactly the peel/bootstrap chain, which is precisely repeated application of the
"A=2θ" device with A itself obtained by recursively applying the SAME two devices). The natural
conjecture, strongly supported by the structure (not yet a complete proof):

**Claim:** Starting from a "sufficiently generic" triangle (e.g. two of Shan-Yu's angles chosen
to be algebraically independent transcendentals, unrelated to θ), the only way ANY sequence of
forced (both-branches) moves can ever pin an angle to a value related to θ is by routing
through the 90°-seed and peeling by positive integer multiples — i.e., every element of W(θ)
not already containing θ must arise from a chain of applications of {θ=90°-device, A=2θ-device}
composed with each other, and I checked (partially, algebraically) that composing them from a
FULLY GENERIC start cannot manufacture any target besides {90°/n}:
  - The θ=90°-device is available from ANY state (doesn't need anything pre-established).
  - The A=2θ-device needs a PRE-EXISTING angle 2θ; the only way to guarantee angle 2θ
    (regardless of the adversarial/generic other two angles) is if 2θ ITSELF is already
    forceable, i.e., 2θ ∈ {90°/n} inductively — giving θ ∈ {90°/2n} ⊆ {90°/n} — no new ground.
  - I checked explicitly (by hand, substituting A=90° as a KNOWN fixed value and re-solving
    the same "universal in remaining free variable" equation) that trying to bootstrap a
    SECOND fresh device off of an already-pinned 90°-vertex's *neighbors* fails: those
    neighbors (β, 90°−β) are Shan-Yu-controlled/generic, and the "acute-both-neighbors"
    precondition for a second 90°-fork FAILS there (one neighbor is exactly 90°, not <90°,
    which the fork's algebra needs strictly), and no OTHER universal-in-β device exists (the
    same uniqueness argument as before, now with A fixed at 90° instead of free, still only
    reproduces θ=45°=90°/2, nothing new).

This is a genuine, close-to-complete heuristic argument, but **not yet a fully written proof**:
the outliner/builder still needs a clean well-founded/strong induction (on the AND-OR game rank,
or on a suitable measure of "algebraic complexity relative to Shan-Yu's generic seed") showing
that composing the two devices in ANY order, starting from a fully generic (A₀,B₀,C₀) never
yields a target outside {90°/n}. This is the single remaining gap for a complete ⊆ proof.

### Distinct openings for the outliner

1. **(REVISED constructive claim — replaces prior round's {90/2^k}):** state and prove
   "θ=90°/n forceable in ≤n moves for every positive integer n" via the 90°-fork +
   peel-by-θ chain above. This is solid, verified both algebraically (exact case
   classification) and numerically (full game-tree check for several n and triangle shapes).
   **This should replace the {90/2^k} claim in `current.md` and any approach files — the old
   claim is a strict subset of the true constructive family and should not be presented as the
   final answer.**
2. **θ>90° impossibility (COMPLETE, rigorous, ready to write up as-is):** the induction
   argument above. This is a genuinely finished half-lemma the outliner can drop straight into
   an approach file with essentially no further work — just needs the case-classification
   algebra written out cleanly and the W_n induction stated formally.
3. **θ<90°, θ∉{90°/n} impossibility (the real remaining gap):** needs a rigorous
   "genericity/transcendence" argument — pick Shan-Yu's starting triangle with two angles
   algebraically independent transcendentals over ℚ(θ), then argue by strong induction (on
   number of moves, or on a well-chosen complexity/rank measure) that every triangle reachable
   in the game either (a) still has two "generic" angles unrelated to θ by any finite algebraic
   relation Mulan could exploit, or (b) is confined to the 90°-seed lineage, in which case only
   {90°/n} values are reachable by the device analysis above. This needs formalizing what
   "exploitable relation" means precisely (probably: an angle equal to jθ for integer j, or
   equal to 90°, or reachable from those by the two devices) and showing Mulan's OTHER possible
   moves (arbitrary x, not θ-related) never help her (any x she picks either keeps a branch
   "generic → still safe" for Shan-Yu, or sacrifices nothing since Shan-Yu just avoids picking
   that branch when it's not literally forced).
4. **Formal AND-OR game framing:** cast the whole problem as: W(θ) = closure under
   T ↦ {both children ∈ W} of {T: θ∈T}; combined with the complete 2-device classification of
   "what makes both children ∈ W₀" — this reduces the ENTIRE problem (both directions) to
   understanding closure of {device: universal-90, device: A=2θ} starting from an arbitrary
   triangle. This is probably the cleanest single framing to hand the outliner — it already
   unifies both the ⊇ (found: gives exactly 90°/n) and ⊆ (needs: prove closure gives no more)
   halves under one lens, is fully rigorous for the θ>90° sub-case, and pinpoints exactly what's
   missing (closure-completeness for θ<90°, θ∉90°/n) as a single well-defined lemma to prove.

### Cheap-kill candidates
- **θ>90° ⟹ Shan-Yu always survives.** FULLY PROVEN above (not conjecture) via the W_n
  induction. This is a strong, ready-to-use partial result — cuts the problem's domain in half
  immediately and should anchor the impossibility half of the outline.
- **θ=90° is a trivial base case** (1-move universal win) — already established by both round-1
  reports, reconfirmed here.
- Parity/multiplicity is NOT the right cheap kill for θ<90° (I initially expected a 2-adic
  valuation argument matching {90/2^k}, but that's now known to be WRONG — the real invariant
  is closer to "n = 90/θ must be an arbitrary positive integer", i.e. an integrality/divisibility
  condition on 90/θ, not a 2-adic one). Flag to outliner: do not import a 2-adic/dyadic-flavored
  invariant template (e.g. naively adapting aimo-0236's p-adic valuation machinery) without
  re-deriving it for the correct {90/n} family — the natural invariant here is closer to
  "is 90/θ a positive integer" (ordinary integrality), not "is it a power of 2."

### Knowledge-base entries to use
- **Invariants & monovariants** (combinatorics section) — for the genericity/survival argument
  (θ<90°, θ∉90/n case).
- **Synthetic toolkit: angle chasing / cevians** (geometry section) — for the cevian-split
  angle formulas (already algebraically verified independently here, consistent with both
  round-1 reports).
- No KB entry for AND-OR game-tree / forcing-set closure arguments; this needs to be built from
  scratch (standard combinatorial game theory, but not templated in the KB).

### Analogous past problems (cruxes)
Re-checked the corpus per round-1's search (games-and-strategy, processes-and-algorithms
subtopics; no geometry cruxes exist).
- `aimo-0236` — "two-phase invariant, defender stays one step ahead via a valuation witness."
  STILL structurally relevant as a *template for how to write* the θ<90° survival invariant
  (maintain an algebraic-independence / non-relation invariant that is self-restoring after each
  of Shan-Yu's choices), but flag explicitly: **do not import the specific 2-adic valuation
  content** — the actual quantity to track here is closer to "n=90/θ ∈ ℤ⁺ or not", not a p-adic
  order.
- `aimo-0445` (fork/double-threat pattern) — matches the "universal 90°-fork" mechanism
  structurally (still relevant, as round-1 forcing report noted).
- No new closer matches found; geometry-flavored forcing games are absent from the corpus.

### Prior progress
`current.md` is still empty/unsolved (first outline round). Round-1 explorers established the
⊇ direction for {90/2^k} (now shown to be an understated subset — true family is {90/n}) and
the θ=90° base case. This report adds: (1) the corrected/broader constructive family {90/n},
verified; (2) a complete, rigorous proof that θ>90° is never forceable; (3) a precise
mechanism-level account of why θ<90°∉{90/n} is conjecturally impossible, reducing the remaining
gap to one well-defined genericity/closure lemma.

### Dead ends (do not retry)
- **Presenting {90/2^k} as the final answer** — this is WRONG (strictly smaller than the true
  constructive family {90/n} exhibited above); any approach file claiming this as the complete
  characterization should be revised, not built on top of.
- **2-adic/dyadic-flavored invariant for the impossibility half** — the natural invariant
  is ordinary integrality of 90/θ, not a power-of-2 condition; don't force the aimo-0236
  p-adic template onto this problem verbatim.
- Round-1's "pure bait" dead end (mod-θ invariant defeats naively always-threatening x=θ) is
  still valid and still relevant: it's exactly why the peel gadget needs the 90°-bootstrap
  first (peeling alone, without ever landing on a multiple of θ, does nothing — you need the
  universal 90° seed to guarantee SOME multiple of θ exists in the first place, for generic θ
  where the starting triangle has no exploitable structure).

### Small-case / intuition notes
- **Proved, not conjecture:** θ=90°/n forceable in ≤n moves, for n=1..7,10 checked exhaustively
  (all Shan-Yu branches) against 4 structurally different starting triangles; algebraic
  mechanism (peel + bootstrap) is exact and n-general, not just verified for tested n.
- **Proved, not conjecture:** θ>90° is never forceable (full induction, no numerics needed).
- **Conjecture (mechanism-supported, not fully proven):** θ<90° with θ∉{90/n} — Shan-Yu
  survives forever against a genericity-based invariant; the outliner's top priority should be
  turning the "device-closure never escapes {90/n}" heuristic into a rigorous strong induction.
- Suggested final answer for `current.md`: **θ ∈ {90°/n : n = 1, 2, 3, ...}**, i.e. Mulan wins
  exactly when 90°/θ is a positive integer.
