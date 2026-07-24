## imo-2026-04

### Setup / angle algebra (derived from scratch)
If Mulan cuts triangle T=(α,β,γ) (angle α at vertex A, etc., α+β+γ=180°) from a point
P on side BC to vertex A, splitting angle α into (x, α−x) with x∈(0,α) [x = angle APB],
the two resulting triangles are
- T1(x) = {x, β, γ+(α−x)}   (angle β untouched)
- T2(x) = {α−x, γ, β+x}     (angle γ untouched)
Shan-Yu keeps one, discards the other. By symmetry Mulan can equally choose to split
β or γ instead of α (3 vertex choices × continuum of x).

**Key forced primitive ("θ-transfer").** If the split angle α > θ, Mulan can set
x = α−θ. Then T2(x) = {θ, γ, β+α−θ} contains θ exactly, so Shan-Yu (who loses at
once if he keeps a triangle containing θ) is *forced* to keep
T1(x) = {α−θ, β, γ+θ}. This is a fully deterministic move: "transfer θ from α to γ,
leave β untouched" (or symmetrically to β), available whenever some current angle
exceeds θ. Chaining such transfers only ever changes each angle by an **integer
multiple of θ**, so each angle's residue mod θ is invariant under this move alone.
Consequently a pure chain of θ-transfers can produce an angle exactly equal to θ
**iff** the starting configuration already has an angle that is an integer multiple
of θ — a measure-zero condition Shan-Yu can trivially avoid by choosing his initial
triangle. So θ-transfers alone are not enough; Mulan needs a way to *create*
alignment from an arbitrary triangle.

### The universal one-move alignment trick (main structural finding)
Look for a single x making **both** T1(x) and T2(x) contain an angle that is an
exact integer multiple of θ (so that whichever branch Shan-Yu keeps, Mulan can then
finish by chaining θ-transfers down to exactly θ). Checking all combinatorially
possible pairs of coordinates (one from T1, one from T2) that could be forced to
≡0 mod θ by a single choice of x mod θ, exactly one pairing gives a condition that
is **universal in α,β,γ** (not requiring any prior rational relation between the
angles and θ):
requiring T1's third angle (γ+α−x) ≡ 0 and T2's third angle (β+x) ≡ 0 (mod θ)
simultaneously is consistent for every α,β,γ **iff α+β+γ ≡ 0 (mod θ), i.e. iff
180 ≡ 0 (mod θ), i.e. θ divides 180° exactly (θ = 180°/n, n a positive integer).**
All other coordinate pairings force a condition like "β ≡ 0 mod θ" that depends on
the specific (unknown, adversarially chosen) starting triangle and can be avoided
by Shan-Yu.

So: **whenever θ = 180°/n for an integer n ≥ 2**, Mulan has a *single* explicit move
(from ANY starting triangle, using the vertex whose split leaves the right residue
target reachable in range) after which, no matter which of the two pieces Shan-Yu
keeps, the surviving triangle has an angle that is an exact multiple kθ (k≥1
integer, k<n); she then finishes with (k−1) more forced θ-transfers.

### Numerical verification (exact rational arithmetic, sympy/Fraction)
Verified programmatically (`Fraction` exact arithmetic, no floating error) for
n = 2,3,4,5,6,7 (θ = 90°,60°,45°,36°,30°,180/7°) against 5 random rational
triangles each (denominators 13, so angles have no accidental relation to θ): in
every trial some vertex-split gives a valid x∈(0,α) with **both** children carrying
an angle that's an exact multiple of θ. Also stress-tested θ=90° against acute
triangles (89,46,45), (80,60,40), (70,65,45) — worst case for range-existence,
since acute triangles have no angle ≥ 90° to split "big enough" — and in each case
a valid x still exists (in fact for n=2 the aligned angle came out to exactly θ in
one shot: e.g. (89,46,45) → both children contain 90° directly). This is strong
constructive evidence for the **sufficiency** direction: θ=180/n ⟹ Mulan wins,
with an explicit, verifiable one-move-then-chain strategy.

### Necessity (θ ≠ 180/n ⟹ Shan-Yu survives) — NOT yet proven, but strong evidence
For θ that does not divide 180° evenly, the single-move universal trick provably
fails (the only θ,a,b,c-independent alignment identity is 180≡0 mod θ, shown above
by exhausting all coordinate pairings). This suggests Shan-Yu can pick an initial
triangle whose angles are "generic" relative to θ (e.g. ℚ(θ)-linearly independent)
and maintain, via an invariant on residues mod θ, that no angle is ever forced to an
exact multiple of θ. I did **not** verify this multi-move invariant computationally
(would need a full game-tree/minimax search or an algebraic argument) — this is the
key remaining gap. Candidate invariant to try: track (α mod θ, β mod θ, γ mod θ) as
elements of ℝ/θℤ with fixed sum 180 mod θ = S ≠ 0; show Shan-Yu has a response to
any Mulan move keeping all three residues nonzero, using that only one of the two
non-split angles' residues is "free" per move (the untouched one is preserved
exactly, forcing Shan-Yu's real lever).

### Conjectured answer
**Mulan can guarantee victory exactly for θ = 180°/n, n = 2,3,4,5,… (equivalently,
180/θ is an integer ≥ 2).** This is a discrete, countable set {90°, 60°, 45°, 36°,
30°, 180/7°, 22.5°, 20°, …} with only accumulation point 0°. For all other θ
(conjectured) Shan-Yu wins by choosing a generic initial triangle and defending
forever.

### Distinct openings for the outliner
1. **Sufficiency by explicit construction** (strongest, closest to complete): prove
   the one-move alignment lemma in general (not just numerically) — solve the
   congruence x ≡ γ+α ≡ −β (mod θ) for x∈(0,α) [needs a short existence argument:
   among the 3 vertex choices, at least one admits a valid x in range — likely via
   pigeonhole/averaging since the three "ranges" (0,α),(0,β),(0,γ) sum to 180 = nθ]
   then chain θ-transfers down. This gives Status partial→solved for the "if" half.
2. **Necessity via residue invariant**: formalize the ℝ/θℤ argument above to show
   Shan-Yu can defend when θ∤180. This is the harder, currently-open half.
3. **Reformulate as a discrete chip-moving game**: abstract away the geometry —
   angles become 3 nonneg reals summing to 180 = nθ (or not), moves = "transfer θ
   from one pile to another, forced whenever pile > θ, or the universal double-align
   move when nθ=180." This is a cleaner combinatorial object for the invariant
   argument in (2) — may be worth stating as its own reduction lemma.

### Candidate technique(s)
Invariant/monovariant argument (mod-θ residue on ℝ/θℤ, KB entry "Invariants &
monovariants"), explicit forced-strategy construction + case-exhaustion on the
three vertex choices (KB "Casework / exhaustion"), pigeonhole for range-existence
of x (KB "Pigeonhole / extremal principle").

### Cheap-kill candidates
- Immediate structural check: if θ ≥ 180° or θ ≤ 0°, excluded by hypothesis — no
  work needed.
- θ = 90/60/45/... (i.e. any 180/n) — the one-move argument above is a genuine
  "cheap kill" that settles the whole forward direction in one clean lemma, much
  cheaper than a full game-tree analysis.
- For candidate counterexamples to necessity, a fast check is: does 180 mod θ = 0
  in exact rational/algebraic arithmetic? This one Python-line check separates the
  two directions before any heavy casework.

### Knowledge-base entries to use
- "Invariants & monovariants" (Combinatorics section) — for the necessity/defense
  direction (residue mod θ as the invariant).
- "Pigeonhole / extremal principle" — for showing at least one of the 3 vertex
  splits admits a valid x in range.
- "Casework / exhaustion" (General Proof Methods) — the 3-vertex, 2-branch
  case analysis is inherently casework; must be kept exhaustive per CLAUDE.md rules.
- "Constructive vs. existence" (General Proof Methods) — this is a
  "for which θ" characterization problem: needs BOTH a construction (θ=180/n
  ⟹ Mulan wins, explicit strategy) AND an impossibility argument (θ≠180/n ⟹
  Shan-Yu survives forever), matching the rigor rule for "find all" problems.

### Analogous past problems (cruxes)
Searched `combinatorics` subtopic `games-and-strategy` (40 cruxes) in the crux
corpus. No problem is a close geometric analogue (no cevian-cutting / angle game
appears in the corpus). Closest in *spirit* (not close enough to import a move,
but useful pattern-matches):
- `aimo-0236` (blackboard integers, Alice adds `a`, Bob halves evens) — uses a
  p-adic-valuation-style invariant to prove one player can force finite
  termination vs. force it to run forever, structurally similar to the
  "invariant that determines forced-termination vs adversary escape" shape needed
  here, but the mechanics (halving vs additive transfer) don't transfer directly.
- `aimo-0117` (stone game, dyadic sequence trick) — uses a geometric/dyadic
  scaling idea for a two-box game; not angle-related, weak analogy only for the
  general flavor of "engineer both opponent choices to be bad."
None of the games-and-strategy cruxes involve triangle-cutting or angle
partitioning, so this is largely a fresh derivation (see algebra above), not an
import from the corpus.

### Prior progress
None — this is round 1, no `results/imo-2026-04/approaches/` exist yet.

### Dead ends (do not retry)
- Pure θ-transfer chains as the *sole* strategy (no other move type): provably
  insufficient whenever the starting triangle has no angle that is an integer
  multiple of θ, since these moves preserve each angle's residue mod θ exactly.
  Do not present this alone as a winning strategy — it only completes the
  construction *after* the one-move alignment lemma has fired.
- Looking for a per-vertex "self-aligning" trick that doesn't use the global
  angle-sum relation 180=α+β+γ: shown analytically that of the 4 coordinate-pairing
  cases only the one using the sum relation gives an a,b,c-independent condition;
  the other 3 require pre-existing rational alignment of a single angle to θ and
  are useless against an adversarial Shan-Yu.

### Small-case / intuition notes (labeled conjecture where appropriate)
- CONJECTURE, strong constructive evidence: Mulan wins iff θ=180°/n, n≥2 integer.
- VERIFIED (exact arithmetic, not just heuristic): for θ=90°,60°,45°,36°,30°,180/7°,
  a one-move-then-chain strategy exists from every tested starting triangle
  (including adversarial acute cases for θ=90°), giving forced win.
- CONJECTURE, not verified computationally: for θ not of the form 180/n, Shan-Yu
  can always defend forever by picking a "rationally generic" initial triangle
  relative to θ. This is the open half; recommend the outliner target a residue/
  invariant proof here, or at minimum flag it explicitly as the gap if a full
  proof isn't reached this round.
