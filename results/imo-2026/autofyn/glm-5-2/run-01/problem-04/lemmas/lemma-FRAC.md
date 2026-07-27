# Lemma FRAC: fractional-part 3-cycle of the forced t=1 transfer

**Statement.** In the `q`-space framing (`q_i = angle_i / θ`,
`N = 180°/θ = q_A + q_B + q_C`), the forced `t = 1` transition
(Shan-Yu keeps the child without the immediate `θ`-angle) acts as
```
(q_A, q_B, q_C)  ⟼  (q_B, q_C − 1, q_A + 1)
```
(and cyclic analogues), valid while the cut vertex has `q_i > 1`. Under this
transition the *multiset of fractional parts* `{{q_A}, {q_B}, {q_C}}` is
invariant; the map acts on the ordered triple of fractional parts as the
3-cycle `({q_A},{q_B},{q_C}) ⟼ ({q_B},{q_C},{q_A})`. In particular, if all
three fractional parts are nonzero at the start, they remain nonzero forever
under forced `t = 1` play, so no coordinate is ever a positive integer (no
angle is ever a multiple of `θ`).

**Proof.** For any real `x`, `{x − 1} = {x}` and `{x + 1} = {x}` (adding /
subtracting an integer does not change the fractional part). The image triple
is `(q_B, q_C − 1, q_A + 1)`, whose fractional-part triple is
`({q_B}, {q_C − 1}, {q_A + 1}) = ({q_B}, {q_C}, {q_A})` — the 3-cycle. Nonzero
fractional parts are preserved under permutation. ∎

**Caveat (important).** Lemma FRAC governs **only** the forced `t = 1` weapon.
It shows that the forcing move cannot, by itself, manufacture a `θ`-angle when
`N ∉ ℤ` (started from a triple with all fractional parts nonzero). It does
**not** by itself prove Shan-Yu escapes, because Mulan is free to play `t ≠ 1`.
Ruling out those deviations is exactly the four-case closure
(`four-case-closure.md`). Lemma FRAC is a genuine invariant of the
forced-dynamics sub-game, offered as a cross-check, not a standalone escape.

Source: `chip-transfer-monovariant`, Lemma FRAC.
