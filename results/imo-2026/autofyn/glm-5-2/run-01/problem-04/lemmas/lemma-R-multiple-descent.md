# Lemma R: multiple-index descent

**Statement.** Let `θ ∈ (0°,180°)`. Let `T` be a triangle having an angle equal
to `mθ` at one of its vertices, with `m ≥ 1` an integer and `mθ < 180°`. Then
Mulan can force a win from `T` in at most `m−1` further moves, regardless of
how Shan-Yu plays. In particular `T` lies in `W_{m−1}` (the `≤ (m−1)`-move
winning region).

(Note: uses only `mθ < 180°`; applies whether or not `180°/θ ∈ ℤ`.)

**Proof by induction on `m`.**

*Base `m = 1`.* `T` already contains `θ`; the stopping check fires immediately.
Mulan wins in `0 = 1−1` moves.

*Inductive step `m ≥ 2`.* Relabel so `C = mθ` is the split vertex and `A, B` are
the other two angles, so `A + B = 180° − mθ`. Mulan cuts at `C` with `γ = θ`.
This is legal: `m ≥ 2 ⇒ θ < mθ = C`, so `γ = θ ∈ (0, C)`.

Children (one-move transition, see the one-move lemma):
```
T₁ = (A, θ, 180° − A − θ),     T₂ = (B, (m−1)θ, A + θ).
```
- `T₁` contains `θ` (the angle `γ`); if Shan-Yu keeps `T₁`, the next check
  finds `θ`: Mulan wins in `1` move from this step.
- `T₂` contains `(m−1)θ` at vertex `C` (a vertex angle of `T₂`). The index
  `m−1` satisfies `1 ≤ m−1 ≤ m−1`, so the induction hypothesis applies to
  `T₂`: if Shan-Yu keeps `T₂`, Mulan wins in at most `(m−1)−1 = m−2` further
  moves, i.e. `≤ m−1` total.

Either choice of Shan-Yu gives a win in `≤ m−1` moves.

*Validity of `T₂` (all angles positive and `< 180°`).* `B > 0` (inherited);
`(m−1)θ > 0` (since `m ≥ 2`); `A + θ > 0`. For the upper bound:
`A < 180° − mθ` (from `A + B = 180° − mθ` with `B > 0`), hence
`A + θ < 180° − (m−1)θ ≤ 180° − θ < 180°` (using `m ≥ 2`). So `T₂` is a genuine
triangle. The same positivity bound is re-established at each induction level
(the two non-split angles of a level-`j` child sum to `180° − jθ`, so each is
`< 180° − jθ`, and adding `θ` keeps it `< 180°`). ∎

**Technique.** Induction on `m` (knowledge_base.md, General Proof Methods). The
angle `(m−1)θ` survives as a clean splittable vertex angle of `T₂`, so the
induction iterates down to `m = 1`.

Source: `direct-four-case-interval` §II.1 / `attractor-level-fixpoint` §3.
