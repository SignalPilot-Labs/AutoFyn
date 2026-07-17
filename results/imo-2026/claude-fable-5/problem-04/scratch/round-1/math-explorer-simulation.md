## imo-2026-04 (lens: computational experiment / conjecture-hunting)

### Cut model (derived from the statement)
Triangle has angles (α at A, β at B, γ at C), α+β+γ=180°. "Cut from P on the
perimeter (≠ vertex) to the opposite vertex" means: P lies on one side, say BC,
and the cevian goes to the OPPOSITE vertex A. This is a cevian from A, so it
splits **A's own angle** α into two parts α₁+α₂=α (α₁ = the choice, continuous,
Mulan picks the side ⇒ which vertex's angle gets split, AND the continuous split
ratio t=α₁/α∈(0,1)). The two children are:
- Triangle 1 = (β, α₁, 180−β−α₁)  [B kept whole; new "point angle" at P]
- Triangle 2 = (γ, α−α₁, 180−γ−(α−α₁))
Note the two point-angles at P sum to 180° (angles on a line), consistent check
passed. So Mulan's move = (choice of vertex to split) × (continuous split point).
Shan-Yu then keeps one child. This matches the problem statement exactly (P on a
side, cut to the opposite vertex, Shan-Yu discards one piece).

### Analytic pre-computation (single-move double-threat, done by hand before simulating)
Solved "for which (α,β,γ,θ) does SOME split of vertex A make BOTH children
contain angle θ instantly" (assuming θ∉{α,β,γ}, i.e. game hasn't already ended).
Four sign combinations of the θ-hit equations reduce to only two non-degenerate
solutions:
- **(A) α = 2θ** (split the vertex with angle exactly 2θ exactly in half:
  α₁=α₂=θ). Requires 2θ<180 i.e. θ<90°, plus mild positivity conditions.
- **(B) θ = 90° exactly**, independent of the triangle's other angles as long as
  the two non-split angles β,γ are both <90° — always arrangeable (only one
  angle of a triangle can be ≥90°, so split at that vertex, or any vertex if the
  triangle is acute). This gives a **universal one-move win at θ=90°** from
  literally any starting triangle not already right-angled.
No other single-move double-threat mechanism exists (the other 2 sign cases force
a degenerate 0° angle). This is a clean structural fact, not just conjecture.

### Computational method
Value iteration on a discretized grid of (sorted) angle triples: Win₀ = {states
containing θ}; Winₖ = Winₖ₋₁ ∪ {states with some vertex/split t s.t. BOTH children
land in Winₖ₋₁} (children looked up by nearest-grid-point after canonical
sorting). Ran with grid resolution 1° and 0.5°, t sampled at 90–400 points,
depth up to 10. Code in /tmp/sim2.py, /tmp/sim3.py, /tmp/sim4.py (not part of the
repo; scratch only).

### Findings (numeric, degree grid)
- **θ = 90°**: full win (2700/2700 grid states) already at depth 1, confirming
  mechanism (B) — universal single-move win, matches the analytic result exactly.
- **θ < 90° (integer)**: at coarse resolution (1°) many odd integers (47,49,...,89)
  appeared "STUCK" (fixed point reached at low depth, no further growth even to
  depth 10) while even integers kept "GROWING" toward full win. **This parity
  split is a discretization artifact, not real**: re-running θ=55, 85, 89 at
  finer resolution (0.5°) shows they are NOT stuck — they keep growing toward
  full win (e.g. θ=55 grows 125→301→544→1075→2177→4190 over 5 depths at 0.5°,
  vs. falsely "stuck at 103" on the 1° grid). Lesson: coarse-grid apparent dead
  ends near odd/half-integer values are rounding artifacts of the
  nearest-grid-point lookup, not genuine obstructions.
- **θ > 90°**: robustly, cleanly STUCK at both 1° and 0.5° resolution, with the
  win-count identical from depth 1 through depth 10 (e.g. θ=120°: exactly 60/10800
  states win, unchanged for 5+ depths at 0.5° resolution; θ=135°, 150° similarly
  frozen). This is **not** a resolution artifact — the count is bit-for-bit
  static across many depths and two independent resolutions. Structurally this
  matches mechanism (A) being impossible for θ>90° (needs 2θ<180°) and no other
  single-move mechanism existing; multi-move attempts don't seem to unstick it.
- **Boundary near 90° exactly**: θ=89.5° and θ=90.5° both showed a STUCK count in
  the 0.5°-grid run (91 and 89 states respectively, static over 5 depths) — this
  conflicts with the "θ<90 always wins" trend and needs more careful checking
  (could be a genuine subtlety right at the boundary, or still a resolution/
  t-sampling artifact — TSAMPLES=120 may be too coarse to find the precise split
  needed near this boundary). Flag this as an open point, not resolved by this
  round's numerics.

### Conjectured answer
**Mulan wins for θ ∈ (0°, 90°], and Shan-Yu can survive forever for θ ∈ (90°,180°).**
Confidence: HIGH on the θ>90° branch (clean analytic obstruction — 2θ>180° kills
mechanism A, and θ=90° is the only universal mechanism — plus robust,
resolution-stable numerics). MEDIUM on θ<90° always winning — numerics trend
that direction for all tested values once resolution is fine enough and depth
large enough, but convergence is slow for some θ (up to depth 8–9 needed) and the
89.5°/90.5° anomaly means the "always wins below 90°" claim is not yet airtight;
it is plausible the true statement has a further exception or that 89.5/90.5
would also resolve to "win" with even finer sampling — this needs an *analytic*
argument for the closing case, not more brute force.

### Distinct openings for the outliner
1. **θ = 90° special-case-first**: prove the universal 1-move win directly (clean,
   already essentially done above) and set it aside; treat it as the "seed" case.
2. **θ > 90° impossibility via monovariant/obstruction**: try to find an exact
   invariant proving Shan-Yu can always avoid θ for θ>90° — candidate: at most one
   angle of any current triangle can exceed 90°, and the two mechanisms above are
   the *only* single-move double threats, so induct on "no single move creates a
   double threat" — but multi-move strategies need ruling out too (this is the
   real gap; a full impossibility proof needs an explicit Shan-Yu strategy/
   invariant, not just "no 1-move win").
3. **θ ≤ 90° doubling-strategy construction**: build Mulan's explicit winning
   strategy using mechanism (A) recursively — force an angle 2θ to appear
   (recursing the same game with target 2θ), bottoming out either at 2^kθ=90° or
   using the flexibility from the *carried* angles β,γ (not just pure doubling)
   to reach a state with an angle exactly 2θ in finitely many moves, for ANY
   starting triangle. This is likely the real crux — needs a clean argument for
   why carried angles give enough freedom (this is exactly why non-dyadic θ like
   33°, 55°, 70° still won in the simulation, contradicting pure-doubling-only
   intuition).
4. **Direct construction avoiding recursion**: since the point-angle at P can be
   tuned to (almost) any value in an interval depending on β, Mulan may have a
   more direct 2-or-3-move forced win not requiring the "reach angle 2θ first"
   framing at all — worth checking whether a simpler uniform argument exists
   (e.g., splitting to guarantee one child always has an angle >θ while shrinking
   Shan-Yu's escape set, cornering him in ≤3 moves for ANY θ≤90°).

### Cheap-kill candidates
- Parity/size check ruled out (θ>90 case is the real one, not integer parity —
  that was a grid artifact, see above; do NOT use "odd/even integer θ" as a real
  distinguishing criterion, it is a numerical artifact).
- The "≤1 obtuse angle per triangle" fact is a genuine and useful structural
  observation (used in deriving mechanism B) — worth stating explicitly in the
  proof.
- Sum-of-angles=180° is the basic constraint throughout; no parity/mod argument
  found to short-circuit the θ>90° impossibility beyond the direct mechanism
  case analysis above.

### Knowledge-base entries to use
- No entry in `knowledge_base.md` is a direct hit (it's algebra/NT/linear-algebra
  focused); closest in spirit is general "invariant / monovariant" reasoning style
  (not a named KB entry here) for the θ>90° impossibility direction.

### Analogous past problems (cruxes)
Searched `combinatorics` × `games-and-strategy` subtopic (39 cruxes). Genuinely
relevant flavor (not exact match — no geometry cruxes exist in the corpus):
- **aimo-0445** (hexagon-grid counter game, k-in-a-row): crux move "Create a
  double threat where the opponent's single allowed response cannot block both
  winning lines simultaneously (a fork)" — directly the same idea as our
  "double threat" mechanism (both children hit θ so Shan-Yu's one discard can't
  save him). Adapt the *fork* framing, not any technical machinery.
- **aimo-0236** (blackboard token game, +a vs /2 moves): crux moves about
  "driving a valuation strictly above/below a threshold" via a two-phase
  invariant — structurally analogous to the "drive an angle above θ, or force it
  toward 90°" recursive-doubling flavor we found, though the actual mechanics
  (angles, not integers/valuations) are unrelated. Use only as a pattern for how
  to structure an induction on "the survivor can't escape a shrinking region."
- No other crux in the corpus is a real match; this is a continuous
  geometric game, and the corpus has no geometry-domain cruxes at all.

### Prior progress
None — `results/imo-2026-04/` was empty before this round (confirmed: only empty
`approaches/` and `lemmas/` directories existed).

### Dead ends (do not retry)
- **"Max angle is a monovariant that never increases"** — FALSE, disproven by
  direct computation: the point-angle 180−β−α₁ created at the cut point P can
  exceed all of the original triangle's angles (as α₁→0, point-angle→180−β,
  which can be much larger than any original angle, e.g. from an equilateral
  triangle (60,60,60) one can create a point-angle up to just under 120°). Do
  not use "angles only shrink" as an invariant — it's wrong.
- **Coarse-grid (1°) "odd integer θ ⇒ stuck" pattern** — this looked like a real
  dead end in the raw data but is a nearest-grid-point rounding artifact; do not
  cite it as evidence that odd-degree θ cannot be forced. Verified false at 0.5°
  resolution for θ=55°, 85°, 89°.

### Small-case / intuition notes (all conjecture, numeric evidence only)
- θ=90°: proven analytically (not just conjectured) to be a universal 1-move win.
- θ>90° (tested 91,95,100,105,110,115,120,135,150): consistently, robustly stuck
  at a small fixed win-region across resolutions/depths — conjectured genuinely
  unwinnable for Mulan.
- θ<90° (tested broadly 1–89 in various depths/resolutions): trend toward full
  win as depth/resolution increase; convergence is slower the closer θ gets to
  the "hard" values that needed doubling depth ~4 (like θ=25,33,50,55 needing
  depth 6–7) or ~9 (θ=70,72,80). The θ≈89.5/90.5 boundary numeric anomaly is
  unresolved and flagged for analytic (not further brute-force) attention.
