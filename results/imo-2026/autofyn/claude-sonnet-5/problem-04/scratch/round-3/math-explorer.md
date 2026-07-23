## imo-2026-04

- Candidate technique(s): Invariants/monovariants on the angle-triple (α,β,γ),
  α+β+γ=180°; forced deterministic reductions (a "credible-threat" move removes
  Shan-Yu's real choice); dynamics of repeated θ-subtraction viewed as a
  rotation/token-redistribution on the circle ℝ/180°ℤ — this connects directly to
  KB's **Three-gap/Steinhaus theorem** and **Kronecker/Weyl equidistribution**
  entries (rational vs. irrational θ/180° likely governs termination).

- Cheap-kill candidates: a triangle's max angle is always ≥60°, giving a natural
  threshold at θ=60° (see new idea below) — cheap structural fact, not yet a
  full obstruction either way.

- Knowledge-base entries to use: **Invariants & monovariants** (Combinatorics);
  **Three-gap/Steinhaus theorem** and **Kronecker/Weyl equidistribution**
  (Number Theory) — highly relevant if the game's long-run dynamics reduce to
  tracking {kθ mod 180°}; **constructive vs. existence / find-all needs upper
  bound + construction** (General Proof Methods), since `answer_type:
  characterization` needs both a Mulan-strategy set and a Shan-Yu-survival set.

- Analogous past problems (cruxes): none. Re-confirmed round-1's corpus search
  (games-and-strategy subtopic, plus triangle/angle/cevian keyword scan) — no
  entry has a continuous-parameter pursuit game with adversarial discard on a
  geometric angle triple. Do not force-fit `aimo-0236`/`aimo-0631`/`aimo-0445`
  (pairing/token games, no geometry) or `aimo-0439`/`aimo-0965` (triangulation
  counting, no adversary).

- Prior progress: Confirmed correct (checked the algebra myself, matches):
  splitting formulas `L(t)=(t,β,α+γ−t)`, `R(t)=(α−t,γ,β+t)`; the
  **guaranteed-bisection lemma** (t=α/2 forces α/2 into both branches, so an
  angle equal to 2ⁿθ is a forced n-move win, no real adversarial choice); the
  **double-threat dead end** (matching θ in both L(t) and R(t) simultaneously
  is only possible at α=2θ — correctly rules out a universal one-shot
  construction, confirmed by re-deriving the coordinate-matching equations).

- Dead ends (do not retry): "aim directly for θ" from a generic triangle
  (dodgeable, per round-1's (30,60,90)→θ=40° hand trace) — still valid, but see
  below, this dead end is superseded by the new mechanism, which is a different
  and stronger move.

- Small-case / intuition notes (mine, new this round — labeled conjecture where
  not fully verified):
  **New forced-reduction mechanism (verified algebraically via sympy, exact,
  not numeric):** if the attacked angle α > θ (strict), Mulan sets t=θ. Then
  L(θ)=(θ,β,α+γ−θ) already contains angle θ — an *immediate win threat* — so
  Shan-Yu is not really choosing adversarially, he is *forced* to discard L and
  keep R(θ)=(α−θ,γ,β+θ), else the game ends in his very next check. Symmetrically,
  setting t=α−θ forces the complementary keep L=(α−θ,β,γ+θ). So whenever some
  current angle exceeds θ, Mulan can force the deterministic transition
  (α,β,γ) → (α−θ, X, Y+θ) for either choice of {X,Y}={β,γ} — no real
  adversarial step at all. This is strictly stronger than the bisection lemma
  (which only fires at α=2θ); it fires for *any* α>θ.
  Since every triangle has max angle ≥60°, if θ<60° strictly, this move is
  available on Shan-Yu's very first triangle (attack the max angle) and,
  conjecturally, can be iterated to termination — but **whether iterating this
  θ-subtraction always hits exactly θ in finitely many steps, or can cycle
  forever without ever landing exactly on θ, is the still-open crux question**.
  This is exactly a repeated "subtract θ, redistribute" process conserving the
  180° sum — structurally similar to Kronecker sequences {kθ mod 180°}: if
  θ/180° is irrational, exact equality with any target is never hit by a naive
  orbit unless the *redistribution* choice (which of β,γ absorbs +θ) is used
  adaptively to force it — this adaptive control is what needs to be shown, not
  a passive equidistribution argument. Conjecture, not proven: θ≤60° is won by
  Mulan via this route; θ>60° needs the case where Shan-Yu opens with a
  triangle whose *max* angle is already <θ (e.g. near-equilateral), so the
  forced-subtraction is unavailable move 1, and a genuine multi-round adaptive
  argument (or a Shan-Yu survival invariant) is needed — this, not the
  bisection lemma, is where the outliner should focus.
