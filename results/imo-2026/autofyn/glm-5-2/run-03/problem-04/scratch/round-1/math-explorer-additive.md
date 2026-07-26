## imo-2026-04 (route: additive/number-theoretic structure & small-case computation)

## ANSWER (conjectured with full computational + algebraic verification)

**Mulan can guarantee victory ⟺ θ = 180°/n for some integer n ≥ 2** (equivalently 180°/θ ∈ ℤ, i.e. θ divides 180°). The set is {90, 60, 45, 36, 30, 22.5, 20, 18, 15, 12, 10, …} (all the way down as n→∞; θ=180° itself is excluded by 0<θ<180°).

## The key invariant — the lattice L_θ

Define `L_θ := { angle-triples (a,b,c) with some angle ∈ θ·ℤ }` (some angle is a positive integer multiple of θ). This single object drives BOTH directions.

**Game move under the lattice:** cut at vertex with angle a (param x). Children
- C1 = (x, b, 180−b−x) = (x, b, a+c−x)
- C2 = (a−x, c, b+x)
Note `180−b−x` and `b+x` are the "third" angles; `b+x = (a+b+c)−kθ... ` in general.

The four-channel intersection lemma (the heart of the proof). If the current state s has NO angle a multiple of θ (s ∉ L_θ), and Mulan wants BOTH children to land in L_θ, then x must satisfy
  C1∈L_θ ⟺ [x ∈ θℤ] ∨ [x ∈ (a+c − θℤ)]   (b is not a mult)
  C2∈L_θ ⟺ [x ∈ (a − θℤ)] ∨ [x ∈ (−b + θℤ)]   (c is not a mult)
The four pairwise intersections yield:
  (1) θℤ ∩ (a−θℤ)  → forces a ∈ θℤ  ✗ (a not a mult)
  (2) θℤ ∩ (−b+θℤ) → forces b ∈ θℤ  ✗
  (3) (a+c−θℤ) ∩ (a−θℤ) → forces c ∈ θℤ  ✗
  (4) (a+c−θℤ) ∩ (−b+θℤ) → forces (a+b+c) = 180 ∈ θℤ, i.e. θ = 180/n
So if θ ≠ 180/n, **no x makes both children land in L_θ**: every move from a state ∉ L_θ leaves ≥1 child ∉ L_θ. (Numerically verified for θ ∈ {40,50,72,80,89,91,100,110,70}: from equilateral and random non-L states, no move forces both children into L.)

## Necessity (θ ≠ 180/n) — Shan-Yu's defense

- For θ ≠ 180/n, note 180/θ ∉ ℤ, so θ ∤ 60; hence the equilateral (60,60,60) has NO angle a multiple of θ, i.e. (60,60,60) ∉ L_θ.
- By the four-channel lemma, L_θ is **closed under Shan-Yu's defense**: from any state ∉ L_θ, every Mulan move leaves at least one child ∉ L_θ; Shan-Yu keeps that child.
- Shan-Yu opens with the equilateral triangle and maintains state ∉ L_θ forever. Since θ ∈ θℤ, a state ∉ L_θ in particular has no angle equal to θ. Mulan never wins.
- This covers ALL non-forceable θ in one argument: irrational θ/180, rational non-unit-fractions θ = (p/q)·180 with p≥2, and every θ>90 (where 2θ>180 so the only multiple of θ below 180 is θ itself; L_θ = "states containing θ", and the defense is even simpler — confirmed: winning set = W0 exactly for θ ∈ {91,100,110,120,130,140,150}).

## Sufficiency (θ = 180/n, n≥2) — Mulan's strategy (two phases)

**Phase 1 — enter L_θ in one move.** From state s=(a,b,c) with θ∉s (else done), let A = max(a,b,c), and let c' = min of the other two angles. Mulan cuts at vertex A. The open interval (c', A+c') has length A. Claim: it contains a multiple kθ (1≤k≤n−1). Reason:
  - n≥3 ⟹ θ ≤ 60 ≤ A. If A = θ then θ present (done); else A > θ, and an open interval of length > θ strictly contains a lattice point of the θ-spaced lattice.
  - n=2 (θ=90): the only multiple below 180 is 90 itself; 90 ∈ (c', 180−b') iff c'<90<b'-compl, which holds whenever 90∉s (all-acute ⟹ all of b',c' <90; one-obtuse ⟹ b',c'<90<A). ✓
Set x = A + c' − kθ ∈ (0, A). Then:
  C1's third angle = 180−b'−x = 180−b'−(A+c'−kθ) = kθ ∈ L_θ ✓
  C2's third angle = b'+x = b'+A+c'−kθ = 180−kθ = (n−k)θ ∈ L_θ ✓
So **both children are in L_θ** after one move, regardless of Shan-Yu's discard. (Numerically verified 200/200 for n ∈ {2,3,4,5,6,7,8,9,10,11,13,17,23,60,180}.)

**Phase 2 — descent within L_θ.** State has an angle = kθ, 1≤k≤n−1. If k=1, θ present, done. If k≥2, Mulan cuts at the vertex with angle kθ, choosing x = θ (valid since θ < kθ). Children:
  C1 = (θ, *, *) contains θ ✓ (Mulan wins if kept).
  C2 = ((k−1)θ, *, *) contains (k−1)θ ✓.
Shan-Yu must keep C2 (to avoid losing immediately). The "multiple index" drops k → k−1. The two carried angles evolve as (b,c) → (b+θ, c) — bounded, since b + (k−1)θ ≤ 180 − θ − c < 180. After at most k−1 ≤ n−2 descents, the index reaches 1 ⟹ θ appears. Total: ≤ 1 + (n−2) = n−1 moves.

(Discrete-grid DP confirms: every state winning in ≤ n−1-ish moves; e.g. θ=60 (n=3) depth ≤2, θ=30 (n=6) depth ≤3, θ=3 (n=60) depth ≤6 on the lattice game.)

## Distinct openings (for the outliner)
- **Lattice-invariant opening (necessity)** — the four-channel intersection lemma + equilateral start. This is the clean necessity proof; it unifies irrational, rational-non-unit-fraction, and θ>90 cases.
- **Max-angle entry + descent opening (sufficiency)** — cut at the maximum angle, exploit interval length ≥ θ to find kθ inside (c', A+c'), then halve the multiple index by cutting at kθ with x=θ. Bounded by n−1 moves.
- **Direct 1-move win sub-lemma** — if some angle = 2θ, Mulan cuts there with x=θ and both children contain θ immediately (the n=2 case is exactly this with the special 90° channel). Useful as the base case of the descent.
- **θ>90 trivial-obtuse opening** — for θ>90, 2θ>180 so no 1-move win is ever possible from a θ-free state; L_θ collapses to "states containing θ" and Shan-Yu just keeps a θ-free child every turn. (Subsumed by the lattice opening, but worth stating because it explains why the boundary is at 90° = 180/2.)

## Candidate technique(s)
- **Invariant / monovariant** (knowledge_base "Invariants & monovariants"): L_θ membership is the invariant for necessity; the multiple-index k is the monovariant (strictly decreases) for sufficiency.
- **Lattice-point / pigeonhole argument**: "an open interval of length > θ contains a multiple of θ" (θ-spaced lattice) — drives Phase 1.
- **Euclidean-style descent** on the multiple index.

## Cheap-kill candidates
- The whole necessity direction is a one-paragraph pigeonhole-on-four-cosets kill once L_θ is identified; no heavy computation.
- Upper bound θ≤90: since the forceable set is {180/n : n≥2} ⊂ (0,90], any θ>90 is immediately excluded by "2θ>180 ⟹ no 1-move bootstrapping, L_θ = θ-present-only, equilateral defends". This is the cheapest size kill.
- Symmetry: the game is permutation-symmetric in the three angles, so WLOG cut at the max — halves the casework.

## Knowledge-base entries to use
- **Invariants & monovariants** (Combinatorics) — L_θ invariant (necessity) and k-monovariant (sufficiency).
- **Pigeonhole / extremal principle** — lattice-point-in-interval and "cut at the max" WLOG.
- **Induction / structural** (General Proof Methods) — descent on k.
- Pólya heuristics "Solve a simpler / special case" — θ=90, θ=60 first, then generalize.

## Analogous past problems (cruxes)
Filter combinatorics / games-and-strategy subtopic. The structural analog is "maintain an invariant set closed under the opponent's replies, plus a strictly-decreasing index for the winner." I did not retrieve a specific crux that maps 1-to-1 (the problem is unusual: a continuous-parameter game with a lattice invariant). The outliner should query `past_crux_moves_database.json` with domain=combinatorics, subtopic=games-and-strategy, and look for "invariant + monovariant descent" cruxes; the closest techniques are likely the "coloring/parity invariant" and "Euclidean descent" patterns. (I did not run the corpus query this round — flagging for the outliner rather than forcing a false match.)

## Prior progress
Round 1, no prior approaches. This report establishes the answer AND a complete proof mechanism for both directions (verified computationally across all 17 integer divisors of 180, all tested non-divisors, and non-integer θ=180/n for n ∈ {7,8,11,13,17,23} via scaled-grid DP, plus continuous Monte-Carlo checks of both the one-move-to-L lemma and the four-channel closure).

## Dead ends (do not retry)
- "θ rational multiple of 180°" is too broad: θ=72° (=2/5·180) is rational but NOT forceable. Reject.
- "θ ≤ 90°" is too broad: θ=80°, 89° are ≤90 but not forceable. Reject.
- "θ = 180°/n for n a power of 2" too narrow: θ=60 (n=3), 36 (n=5), 30 (n=6) are forceable with non-power-of-2 n. Reject.
- "θ divides 60°" confuses the test state with the answer: θ=45, 36, 30, 20, … forceable but don't divide 60. Reject.
- Brute-force minimax on the full continuous game without the L_θ reduction — intractable; the lattice invariant is the only known clean route.

## Small-case / intuition notes (labeled CONJECTURE until proven, but proof mechanism identified above)
- CONJECTURE (strong): forceable set = {180/n : n≥2 integer}. Verified exhaustively on integer grid for every divisor and non-divisor of 180 in (0,180), and via scaled grids for non-integer θ=180/n.
- The equilateral (60,60,60) is the canonical boundary state: it is LOSING iff θ∤180 (θ≠180/n), WINNING iff θ=180/n (in which case every state is winning). This is because 60∉θℤ ⟺ θ∤60 ⟺ θ∤180 ⟺ θ≠180/n (using θ|60 ⟹ θ|180).
- Within L_θ for non-forceable θ, the winning set is exactly L_θ itself (Mulan wins from L_θ-states by descent, loses from non-L_θ states by closure). Confirmed by inspecting the winning sets of θ=40 (mults {40,80,120,160}), θ=72 (mults {72,144}), θ=80 (mults {80,160}), θ=100 (mult {100} only → W0=W1=…).
- Depth (moves to win) for θ=180/n is small: n=2→1, n=3→2, n=4→2, n=5→3, n=6→3, … grows ~logarithmically in the lattice game, ≤ n−1 by the simple descent.

## Files
- Simulation source: `/tmp/sim.py`, `/tmp/sim2.py`, `/tmp/sim3.py` (grid DP), `/tmp/strategy.py`, `/tmp/strat2.py` (move extraction), `/tmp/inv.py` (winning-set inspection), plus the inline Monte-Carlo verification of the four-channel lemma and the one-move-to-L lemma.
