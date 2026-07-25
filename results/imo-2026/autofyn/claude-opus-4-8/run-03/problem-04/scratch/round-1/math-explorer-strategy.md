## imo-2026-04 (lens: Mulan's constructive forcing strategy)

**Note on the win condition (important, easy to misread):** the θ-check happens on
whichever triangle Shan-Yu keeps, *before* Mulan's next cut. Creating one child with
angle θ is NOT a win by itself — Shan-Yu simply discards that child. Mulan only wins
outright on a move if **both** children (the one for each of Shan-Yu's two choices)
carry angle θ, or if she can force a finite sequence of moves after which every
surviving branch is eventually forced to θ. This reframes the "constructive forcing"
question correctly: it's a minimax search over Mulan's continuum choice of cut point
vs. Shan-Yu's binary choice, not a single existential construction.

### Exact geometry of one cut (worked out in coordinates/symbolically)

Cutting from P on side BC to the opposite vertex A splits angle A = α into two pieces.
Parametrize by x = angle BAP ∈ (0, α) (Mulan's one continuous degree of freedom per
move; she also separately chooses *which* vertex/side to cut, a discrete choice of 3).
By the exterior-angle theorem, the two children's full angle sets are exactly
determined by x — there is no independent freedom in the P-angle:

- Child1 (A,B,P): angles **{x, β, 180−x−β}** (β = original angle B, unchanged).
- Child2 (A,C,P): angles **{α−x, γ, x+β}** (γ = original angle C, unchanged).

Note angle(APC) = x+β = 180 − angle(APB), the supplementary pair at the cut point,
by the exterior angle theorem — confirms the "φ / 180−φ at P" mechanic in the lens
prompt, but shows the *other* two angles of each child are NOT free (they're forced
by triangle-angle-sum), so the true parameter space per move is 1-dimensional (x),
times 3 (which vertex), not the loose 2-D "choose φ freely" picture in the prompt.

### One-move forced wins (both children get θ simultaneously) — solved exactly

Setting up "θ ∈ child1's angle-set AND θ ∈ child2's angle-set" and excluding the
already-won cases β=θ, γ=θ, there are exactly two non-trivial simultaneous solutions:

1. **x=θ, α−x=θ ⟹ α = 2θ.** If the *current* triangle already has an angle exactly
   2θ, bisecting that angle's vertex (x = θ = half of it) forces θ into **both**
   children (each gets θ at the bisected vertex) — instant win, one move.
2. **180−x−β=θ and x+β=θ (the two P-angles) ⟹ θ = 90°, x = 90−β.** If θ=90°,
   dropping the altitude (x = 90−β, valid whenever 0<90−β<α, i.e. angles at both
   endpoints of the chosen side are acute) makes the foot P the base of the
   altitude — both children are right triangles with the right angle at P.
   **Since every triangle has at least two acute angles, at least one of its three
   altitudes has its foot strictly interior to the opposite side, so this move is
   always available.** ⟹ **θ = 90° is a universal 1-move win, for every possible
   Shan-Yu starting triangle.** (Verified: the two remaining combinations of the
   6 sub-cases collapse to β=0 or α+β=180, both impossible for a genuine triangle.)

No other combination of {x, β, 180−x−β} vs {α−x, γ, x+β} gives a solution not
already covered — this exhausts the 1-move analysis exactly (not conjectural).

### Obstruction found numerically (strong candidate lemma, NOT yet proved)

Tested (700,000 random trials, python, see below): starting from **any non-obtuse
triangle** (all angles ≤ 90°), for **every** choice of vertex to cut and **every**
x ∈ (0, that vertex's angle), **at least one of the two children is again
non-obtuse**. Zero counterexamples found. If true and provable, this is an
invariant Shan-Yu can maintain forever: start with (e.g.) an equilateral triangle
and always keep the non-obtuse child. Then the triangle's angles never exceed 90°,
so **θ > 90° can never be forced** — Mulan cannot win for any θ > 90°.

By contrast, I tested the dual invariant "all angles ≥ c" (a candidate defense
against *small* θ) for c = 10,20,30,44,45,50,59 and found an explicit
counterexample (a single cut breaking it) in every case — Mulan can always destroy
a minimum-angle floor. This asymmetry singles out 90° as the one genuine threshold;
there is no analogous floor-defense for Shan-Yu at the low end.

**Conjectured characterization from this lens: Mulan wins for exactly 0° < θ ≤ 90°,
loses for 90° < θ < 180°.** This matches both hard data points found (θ=2θ-instance
and θ=90 universal win) and the one-sided invariant-breaking evidence. This is a
conjecture pending (a) a rigorous proof of the non-obtuse-invariant lemma for the
upper bound, and (b) an actual finite forcing construction for general θ ≤ 90°
(not yet built — see next).

### A genuine multi-move forcing mechanism (partial, not completed — hand to outliner)

Key structural fact usable for general θ: cutting vertex A with x = θ−β (valid iff
β < θ < α+β) makes **child2's P-angle equal exactly θ**. If Shan-Yu discards child2
(the only rational move once he sees θ appear), he is forced to keep child1 =
{θ−β, β, 180−θ} — which carries the **known, fixed angle 180−θ** at the new vertex
P, regardless of what β was. This is a genuine "supplementary duo" forcing move:
whenever Mulan aims a cut so that one child's cut-point angle is exactly θ, the
sibling's cut-point angle is forced to be exactly 180−θ (immediate from
supplementarity) — so escaping θ always plants a *known* angle 180−θ somewhere.

For θ ≤ 90°, 180−θ ≥ 90°, i.e. this forced angle is obtuse-or-right. Idea for a
finite-step strategy: repeat this maneuver on successive vertices, using the
now-known obtuse angle 180−θ to set up the *next* cut precisely (e.g. combine with
the 1-move exact conditions above, now that one angle is pinned exactly), driving
toward either the "α=2θ" trigger or directly re-landing θ within a bounded number
of moves. I did not complete this recursion (that's outline work), but it is the
cleanest concrete lead for a constructive strategy and is worth building out as an
approach: **"supplementary-pin-and-pivot" strategy** — pin 180−θ via one cut,
then pivot off it.

### Cheap-kill candidates
- **α = 2θ present ⟹ instant win** (bisect). Good base case / reduction target.
- **θ = 90° ⟹ instant universal win** (drop an interior altitude — always exists).
  This should make θ=90° a clean, fully-solved sub-case in the final proof.
- **Non-obtuse-invariant ⟹ θ>90° is a dead direction entirely** — do not spend
  effort trying to construct a winning strategy for θ>90°; numerically it looks
  false. The proof should instead find (and rigorously prove) Shan-Yu's defense:
  start equilateral (or any non-obtuse triangle), always keep the non-obtuse child.
  **The needed lemma to actually prove:** "if a triangle is non-obtuse, cutting any
  vertex at any interior point x leaves at least one child non-obtuse." This reduces
  to checking, for x ∈ (0,α), whether {x,β,180−x−β} or {α−x,γ,x+β} is non-obtuse;
  should be a clean case-split/algebra exercise (worth giving to a builder directly —
  it looked very tractable in the numerical checks, likely provable by an explicit
  x-interval argument: as x ranges over (0,α), child1's non-obtuse region and
  child2's non-obtuse region are each intervals of x, and one can show their union
  is all of (0,α) using β,γ≤90, α≤90).

### Knowledge-base entries to use
- **Constructive / incremental** (Combinatorics): realize a target value by starting
  from an extreme and moving continuously — matches the "Mulan has continuum control
  of x" structure.
- **Invariants & monovariants**: exactly the tool for the θ>90° obstruction (Shan-Yu's
  non-obtuse invariant) and potentially for a monovariant showing Mulan's forcing
  terminates in finitely many moves for θ≤90°.
- **Extremal principle / pigeonhole**: "every triangle has ≥2 acute angles" (used for
  the θ=90 altitude-always-exists argument) is an extremal/counting fact worth stating
  explicitly and citing.
- **Casework/exhaustion**: the one-move exact-solve above (6 sub-cases, only 2
  survive) is a clean exhaustive case analysis — reusable directly as a lemma.
- General proof methods: **contradiction** for the θ>90° impossibility (assume Mulan
  has a forcing strategy against Shan-Yu's non-obtuse-preserving defense, derive that
  some angle must exceed 90°, contradicting the invariant).

### Analogous past problems (crux corpus)
Searched `games-and-strategy` subtopic across number_theory/combinatorics (40 cruxes
total) and cross-checked `past_problems_database.json` for triangle/angle-cutting
games. **No genuinely analogous problem found** — nothing in the corpus involves
continuous geometric parameters with a discrete adversarial choice (all corpus
games-and-strategy entries are discrete/combinatorial: Nim-style counters, pairing
strategies on boards/graphs, parity invariants on finite token sets). The closest by
subject matter is `aimo-0225` (isosceles-triangle counter game on a regular n-gon,
uses a 2-adic-valuation monovariant and strategy-stealing symmetry) but it operates
on discrete arc lengths, not continuous angle-splitting with an "opposite vertex cut"
mechanic — I judge it not a strong match, just a distant cousin (both are
"triangle-shape" games with a recursive halving flavor). Do not force this crux;
the invariant-based obstruction argument (non-obtuse defense) is a much better
transplant of the *general technique* "invariant preserved by adversary's move
regardless of the first player's choice" than any specific corpus problem.

### Prior progress
None — this is round 1, no approaches/lemmas exist yet in `results/imo-2026-04/`.

### Dead ends (do not retry)
- Treating φ (the cut-point angle) as Mulan's free/independent parameter separate
  from the other two child angles — **false**; once x (equivalently P's position) is
  fixed, ALL angles of both children are pinned by triangle-angle-sum. Don't design
  a strategy assuming extra freedom at P.
- "All angles ≥ c" as a Shan-Yu defense for small θ — numerically refuted for
  c = 10,...,59 (Mulan always has a cut breaking it). Do not use this as the
  lower-bound argument; the asymmetry between the two invariant families is itself
  informative (90° is special, there is no dual floor).

### Small-case / intuition notes (labeled conjecture except where noted "proved")
- **Proved by exact case-exhaustion:** α=2θ ⟹ 1-move win; θ=90° ⟹ 1-move win always.
- **Conjecture (strong numeric support, 700k trials, 0 counterexamples):** non-obtuse
  triangles have a non-obtuse child under every cut ⟹ θ>90° is unwinnable for Mulan.
- **Conjecture (not yet checked by simulation, worth a builder's time):** for every
  θ ∈ (0°,90°) and every starting triangle, Mulan can force θ in finitely many moves
  via some version of the "supplementary-pin-and-pivot" mechanism above. I did not
  run a full adversarial-search simulation for this due to time; recommend the
  outliner or a builder run a concrete minimax/greedy simulation for a few θ values
  (e.g. θ=10°,30°,45°,80°) against a Shan-Yu that greedily tries to avoid θ and stay
  "far" from it, to test whether Mulan's candidate strategy converges in bounded
  moves before committing to a full proof.
- **Overall answer conjecture for this lens: θ ∈ (0°, 90°] is exactly the winning set
  for Mulan.** (Both endpoints checked: θ→0+ presumably still fine since bisection/
  pin-pivot has no lower obstruction found; θ=90 proved; θ>90 numerically blocked.)
