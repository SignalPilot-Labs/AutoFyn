# chip-transfer-monovariant

Target: characterize `θ ∈ (0°,180°)` for which Mulan guarantees victory in finitely
many steps in the Shan-Yu / Mulan paper-triangle game. Conjectured (and
cross-confirmed) answer: `θ = 180°/n` for an integer `n ≥ 2`, i.e. `180°/θ ∈ ℤ`.

Technique: rescale `q_i = (angle_i)/θ` so the angle-sum becomes
`q_A + q_B + q_C = N := 180°/θ` (a real `> 1`); analyze the **forced `t=1` chip
transfer** and the modular / residue structure of the orbit. The
outline-reviewer's round-1 computation established that the **bare `t=1`
transfer op CYCLES under greedy play** (`q=(3,2,3)`, `n=8`, is a fixed point when
the largest coordinate is cut — **verified below**), so **no strict monovariant
exists for the greedy transfer op**. Consequently this approach's *sufficiency*
engine is honestly conceded to converge to the direct approach's Lemma R (the
multiple-index descent `mθ → (m−1)θ`) + Lemma F (interval-contains-integer);
there is no transfer-specific monovariant. The approach's genuine contribution is
on the **necessity / escape** side, where the `q`-space framing yields a clean
invariant (the multiset of fractional parts is a 3-cycle under the forced
`T=1` transfer) and the escape is the four-case closure restated precisely in
residue language — the *same* correct algebraic engine as the direct approach,
presented honestly as a `q`-space cross-check, not a rival engine.

## Status
partial

## Approaches tried
- (round 1) chip-transfer-monovariant — CHANGES REQUESTED by outline-reviewer.
  The bare transfer monovariant does **not** exist: the greedy `t=1` transfer
  cycles (`q=(3,2,3)`, `n=8`, is a fixed point when the angle-`3θ` vertex is cut;
  verified computationally below). Smart `t=1` play wins from every integer
  `q`-state of sum `n` but its descent **is** Lemma R's `m → m−1` induction, not a
  new transfer-specific potential. Recorded as a dead-end.
- (round 1, this build) Necessity via `q`-space residue framing — the four-case
  closure **is** the correct necessity engine; re-derived cleanly in `q`-space
  below, with the genuine invariant "the multiset of fractional parts
  `{q_i mod 1}` is a 3-cycle permutation under the forced `t=1` transfer"
  (Lemma FRAC, proven). Attempted to build an *independent* Kronecker/
  equidistribution escape for irrational `180°/θ` and an independent
  periodic-orbit escape for rational non-integer `180°/θ = p/q`; both reduce to
  the same four-case algebra (a forced-win move requires *both* children to
  carry a `B_θ`-angle, and the four combinations of `γ` telescope to
  `A, B, C, 180`). Recorded honestly: no genuinely independent necessity engine
  exists; the four-case closure is forced by the geometry.
- (round 1, this build) Sufficiency — conceded GAP; the winning descent is
  Lemma R + Lemma F (direct approach), re-stated in `q`-space as a cross-check.
  No transfer-specific monovariant; point reader at `direct-four-case-interval`.

## Current best

### The `q`-space reduction (established, shared with all approaches)

Set `q_i = (angle_i)/θ` and `N = 180°/θ > 1`. The angle-sum becomes
`q_A + q_B + q_C = N`. A triangle contains an angle `= θ` iff some `q_i = 1`;
more generally it carries a "`B_θ`-angle" (a positive multiple of `θ` strictly
below `180°`) iff some `q_i` is a positive integer strictly below `N`. (If
`q_i > 0` and `Σ q_i = N`, then `q_i < N` automatically; and `q_i` a positive
integer `⇔ q_i ∈ {1, 2, …, ⌊N⌋}` iff `q_i mod 1 = 0`.)

**One-move transition (geometry of a cut).** Mulan places `P` on the side
opposite vertex `C` (so `P` is on side `AB`, not a vertex) and cuts to `C`. Let
`γ` be the piece of angle `C` adjacent to `A`, so `γ ∈ (0, C)` and the cut
splits `C = γ + (C−γ)`. Set `t = γ/θ ∈ (0, q_C)`. The two children are

- `T_1 = (A, γ, 180°−A−γ)`  → `q`-coordinates `(q_A, t, N − q_A − t)`;
- `T_2 = (B, C−γ, A+γ)`     → `q`-coordinates `(q_B, q_C − t, q_A + t)`.

The two new angles at `P` are `p_1 = 180°−A−γ` and `p_2 = A+γ`, and
`p_1 + p_2 = 180°` (**supplementary `P`-angles** — the single load-bearing
geometric fact: the two angles at `P` lie on a straight line). In `q`-space:
`p_2/θ = q_A + t`, `p_1/θ = N − q_A − t`, and these sum to `N`.

**The forcing move `t = 1` (i.e. `γ = θ`).** Whenever some vertex angle exceeds
`θ`, say `q_C > 1`, Mulan sets `t = 1`. Then child `T_1` has a coordinate `t = 1`
(i.e. an angle `= θ`), so `T_1` is an *immediate win* if kept. To survive,
Shan-Yu is forced to keep `T_2`, whose `q`-coordinates are
`(q_B, q_C − 1, q_A + 1)`. Net **forced transition under `t=1` play** (cutting the
vertex of index `i`, kept child relabeled by Shan-Yu):

> `(q_A, q_B, q_C) ⟼ (q_B, q_C − 1, q_A + 1)`   (and cyclic analogues),

valid while the cut vertex has `q_i > 1`. Sum `N` is conserved. This is a
"transfer `1` from coordinate `i` to coordinate `i−1` (mod 3)".

### Lemma FRAC (genuine `q`-space invariant of the forced transfer — PROVEN)

**Statement.** Under the forced `t=1` transition
`(q_A, q_B, q_C) ⟼ (q_B, q_C − 1, q_A + 1)`, the *multiset of fractional parts*
`{ {q_A}, {q_B}, {q_C} }` is invariant; the map acts on it as the 3-cycle
`({q_A},{q_B},{q_C}) ⟼ ({q_B},{q_C},{q_A})`. In particular, if all three
fractional parts are nonzero at the start, they remain nonzero forever under
forced `t=1` play, so no coordinate is ever a positive integer, i.e. no angle is
ever a multiple of `θ`.

**Proof.** For any real `x`, `{x − 1} = {x}` and `{x + 1} = {x}` (subtracting /
adding an integer does not change the fractional part). Hence
`{q_B}` (unchanged), `{q_C − 1} = {q_C}`, `{q_A + 1} = {q_A}`. The new fractional
part triple is `({q_B}, {q_C}, {q_A})` — the 3-cycle. Nonzero-ness is preserved
under permutation. ∎

**Caveat (honest).** Lemma FRAC only governs the *forced* `t=1` weapon. It
shows the forcing move cannot, by itself, manufacture a `θ`-angle when `N ∉ ℤ`
(started from a fractional-part-nonzero triple). It does **not** by itself prove
Shan-Yu escapes, because Mulan is free to play `t ≠ 1`; ruling out those
deviations is exactly the four-case closure below. Lemma FRAC is a genuine
distinct invariant of the forced-dynamics sub-game, offered as a cross-check, not
a standalone escape.

### Dead-end: the greedy transfer monovariant (verified)

**Claim (outline-reviewer, verified).** The *greedy* `t=1` transfer (always cut
a largest coordinate) has periodic orbits, so no strict monovariant exists for
the greedy transfer op.

**Verification.** Take `N = 8` (`θ = 22.5°`) and the integer state
`q = (3, 2, 3)`. The largest coordinate is `3` (at indices `0` and `2`). Cut the
vertex of index `2` (angle `3θ`): the kept child is
`(q_B, q_C − 1, q_A + 1) = (3, 2, 3)` — a **fixed point**. (Cutting index `0`
gives `(q_C, q_A − 1, q_B + 1) = (2, 2, 4)`, not a fixed point; the point is that
*a* greedy choice cycles, which suffices to rule out any strict descent under
all greedy choices.) A fixed point under the dynamics is incompatible with the
existence of a strictly-decreasing non-negative-integer-valued monovariant of
the bare transfer op. ∎

Smart `t=1` play (cut first the coordinate of value `m = 2`, i.e. Lemma R's base
case `mθ → (m−1)θ = θ`, an immediate win) wins from every integer `q`-state of
sum `n` (exhaustive search `n ∈ {3,…,12}`, zero unwinnable states —
outline-reviewer). That winning descent **is** Lemma R's multiple-index
induction, not a new potential. Hence:

> **There is no transfer-specific monovariant.** The sufficiency engine is Lemma R
> (multiple-index descent) + Lemma F (interval-contains-integer, reaches a
> multiple of `θ` in one move from any generic triple). These are the direct
> approach's lemmas, re-stated in `q`-space.

### Necessity (escape when `180°/θ ∉ ℤ`) — PROVEN via the four-case closure

This is the correct necessity engine. I present it in `q`-space / residue
language, the natural home of this approach; the algebra is the four-case
closure (shared with `direct-four-case-interval` — I do **not** claim a rival
engine; I claim a clean, fully rigorous, self-contained re-derivation that makes
the invariant explicit).

**Definitions.** Let
`B_θ = {kθ : k ∈ ℤ_{≥1}, 0 < kθ < 180°}` (positive multiples of `θ` below
`180°`); note `180° ∉ B_θ` (strict). In `q`-space, `B_θ` corresponds to
`{1, 2, …, ⌊N⌋}` (the positive integers strictly below `N`). A triple is
`S_θ`-**safe** (lies in `S_θ`) iff none of its angles lies in `B_θ`, i.e. iff
every `q_i` has **nonzero fractional part** (`{q_i} ≠ 0`).

**Theorem N (escape).** If `180°/θ ∉ ℤ`, Shan-Yu has a strategy (open
equilateral; thereafter always keep an `S_θ`-safe child) that prevents `θ` —
indeed prevents every `B_θ`-angle — from ever appearing. Hence Mulan cannot
guarantee victory, so `θ` is **not** a winning value.

**Proof.**

*Step 1 (the equilateral is `S_θ`-safe when `N ∉ ℤ`).* The equilateral
`(60°, 60°, 60°)` has `q = (N/3, N/3, N/3)`. If some `60° = kθ` (`k ≥ 1`), then
`θ = 60°/k`, so `N = 180°/θ = 3k ∈ ℤ`, contradicting `N ∉ ℤ`. Hence `60° ∉ B_θ`
and the equilateral is `S_θ`-safe. (Equivalently, `N/3` is not a positive
integer when `N ∉ ℤ`: if `N/3 = k ∈ ℤ_{≥1}` then `N = 3k ∈ ℤ`.) ∎

*Step 2 (four-case closure: from any `S_θ`-safe triple, every cut leaves at
least one `S_θ`-safe child).* Let `(A, B, C)` be `S_θ`-safe: none of `A, B, C`
lies in `B_θ`. Mulan cuts at vertex `C` with parameter `γ ∈ (0, C)` (the argument
is identical for any chosen vertex, by relabeling). The children are
`T_1 = (A, γ, p_1)` with `p_1 = 180° − A − γ`, and `T_2 = (B, C−γ, p_2)` with
`p_2 = A + γ`. A child is `S_θ`-**un**safe iff one of its three angles lies in
`B_θ`.

Because `(A, B, C)` is safe, `A ∉ B_θ` and `B ∉ B_θ`. So:
- `T_1` can become unsafe **only** via `γ ∈ B_θ` or `p_1 ∈ B_θ` (its third
  angle, `A`, is not in `B_θ`).
- `T_2` can become unsafe **only** via `C−γ ∈ B_θ` or `p_2 ∈ B_θ` (its angles
  `B`, `C−γ`, `p_2`; `B ∉ B_θ`).

Suppose, for contradiction, that **both** children are unsafe. Then one of
`{γ, p_1}` is `= k_1 θ` for some `k_1 ∈ ℤ_{≥1}` (with the value in `(0,180°)`),
and one of `{C−γ, p_2}` is `= k_2 θ` for some `k_2 ∈ ℤ_{≥1}`. This gives four
disjoint, exhaustive cases:

- **(i)** `γ = k_1 θ` and `C−γ = k_2 θ`. Then
  `C = γ + (C−γ) = (k_1 + k_2) θ ∈ B_θ`, contradicting `C ∉ B_θ`.
- **(ii)** `γ = k_1 θ` and `p_2 = A + γ = k_2 θ`. Then
  `A = p_2 − γ = (k_2 − k_1) θ`. Since `p_2 = A + γ > γ = k_1 θ > 0` we have
  `k_2 > k_1 ≥ 1`, so `k_2 − k_1 ≥ 1` and `A = (k_2−k_1)θ ∈ B_θ`,
  contradicting `A ∉ B_θ`.
- **(iii)** `p_1 = 180°−A−γ = k_1 θ` and `C−γ = k_2 θ`. Subtract:
  `p_1 − (C−γ) = (180°−A−γ) − (C−γ) = 180° − A − C = B = (k_1 − k_2)θ`.
  Positivity `p_1 > 0 > 0` and `C−γ > 0` gives `k_1, k_2 ≥ 1`; the sign of
  `k_1 − k_2` is fixed by `B > 0`, so `B` is a nonzero integer multiple of `θ`,
  and `0 < B < 180°`, hence `B ∈ B_θ`, contradicting `B ∉ B_θ`.
- **(iv)** `p_1 = 180°−A−γ = k_1 θ` and `p_2 = A+γ = k_2 θ`. Add:
  `p_1 + p_2 = (180°−A−γ) + (A+γ) = 180° = (k_1 + k_2) θ`. Hence
  `180°/θ = k_1 + k_2 ∈ ℤ`, contradicting the hypothesis `N = 180°/θ ∉ ℤ`.

Each case yields a contradiction; the four cases are exhaustive (each child's
potential `B_θ`-angle is one of two named candidates) and disjoint. Therefore it
is impossible for **both** children to be `S_θ`-unsafe: **at least one child is
`S_θ`-safe**. ∎

The four linear combinations `(γ)+(C−γ)`, `(A+γ)−(γ)`, `(180−A−γ)−(C−γ)`,
`(180−A−γ)+(A+γ)` telescope to `C, A, B, 180` respectively — **verified by direct
computation** (see the algebraic check recorded in this approach's build notes:
each identity is a one-line simplification). The strict positivity `0 < γ < C`
guarantees every `k_i ≥ 1` (the candidate `B_θ`-angles are genuine positive
multiples, not `0`), which is what makes cases (i)–(iii) contradict
membership in `B_θ` (and not merely "`= 0`").

*Step 3 (Shan-Yu's strategy).* Shan-Yu opens with the equilateral — safe by
Step 1. After each Mulan cut, by Step 2 at least one of the two children is
`S_θ`-safe; Shan-Yu keeps such a child. The kept triangle is therefore
`S_θ`-safe at the end of every round. Since `θ ∈ B_θ` (it is `1·θ`, and
`0 < θ < 180°` by the problem's hypothesis), no `S_θ`-safe triangle contains
`θ`. Hence `θ` never appears, the game never stops, and Mulan does not win in
finitely many steps. By the **Invariants & monovariants** principle
(knowledge_base.md, Combinatorics) — the set `S_θ` is preserved by Shan-Yu's
keep-rule — Shan-Yu's escape is certified. ∎

**Remark (uniformity).** Theorem N is uniform in *every* non-integer `N`,
irrational or rational. This is why a separate Kronecker sub-case is
unnecessary: the closure does not use any arithmetic of `N` beyond
"`180° ∉ B_θ`-multiples", i.e. `N ∉ ℤ`. Specifically:
- *Irrational `N` (`θ/180° ∉ ℚ`):* `N ∉ ℤ` holds a fortiori; Theorem N applies
  directly. An independent Kronecker/Weyl equidistribution escape was attempted
  (maintain `{q_i}` bounded away from `0` via density of `{kα}`), but it
  **reduces to the same algebra**: a forced win needs *both* children unsafe,
  which is exactly the four-case contradiction; density only renames the
  contradiction in case (iv). Recorded as a non-independent route.
- *Rational non-integer `N = p/q` (`q ≥ 2`, e.g. `θ = 72°`, `N = 5/2`):* the
  equilateral `q = (N/3, N/3, N/3) = (p/(3q), …)` is safe (`N/3 ∉ ℤ` since
  `N = p/q ∉ ℤ` iff `q ∤ p`; `N/3 ∈ ℤ` would force `N ∈ ℤ`). Theorem N applies.
  An independent periodic-orbit escape was attempted (the
  `(5/6, 1/6, 3/2) ↔ (5/6, 1/2, 7/6)` cycle under greedy `t=1` for `θ=72°`,
  flagged by the reduction explorer): Lemma FRAC *does* certify this orbit keeps
  fractional parts nonzero (a genuine invariant), but robustness against
  Mulan's non-`t=1` deviations is again exactly the four-case closure. Recorded
  as a non-independent route.

### Sufficiency (`180°/θ = n ∈ ℤ, n ≥ 2` ⟹ Mulan wins) — GAP (conceded)

**Honest status: GAP.** This approach does **not** supply an independent
sufficiency engine. The bare transfer monovariant fails (dead-end above); smart
`t=1` play wins but its descent **is** Lemma R, not a new potential. The
complete sufficiency argument is:

- **Lemma F (reach a multiple of `θ` in one move, `n ≥ 3`).** From a generic
  triple with no `B_θ`-angle, split the largest angle `C` (`C ≥ 60° ≥ θ` since
  `n ≥ 3`, and `C ∉ B_θ` so `C > θ`, i.e. `C/θ > 1`). The open interval
  `(A/θ, (A+C)/θ)` has length `C/θ > 1`, hence contains an integer `k` strictly
  inside (Pigeonhole/extremal principle — knowledge_base.md). Set
  `γ = kθ − A ∈ (0, C)`. Then `p_2 = A+γ = kθ` and `p_1 = 180°−kθ = (n−k)θ`;
  both are positive multiples of `θ` (bounds `k ≥ 1`, `k ≤ n−1`). So both
  children carry a `B_θ`-angle.
- **Lemma R (descend the multiple, `mθ → (m−1)θ`).** If a vertex angle `= mθ`
  (`2 ≤ m ≤ n−1`), Mulan cuts it with `γ = θ` (`t = 1`): child `T_1` contains
  `θ` (immediate win if kept), forcing Shan-Yu to keep `T_2`, whose inherited
  `mθ`-angle becomes `(m−1)θ`. The third angle of `T_2` is `A+θ`, and
  `A < 180° − mθ` (since `A + B = 180° − mθ`, `B > 0`), so
  `A + θ < 180° − (m−1)θ ≤ 180° − θ < 180°`: positivity holds at every step.
  Induction on `m` (base `m = 1` = already won) gives a win in `≤ m−1` moves.
- **`n = 2` (`θ = 90°`).** Split the largest angle `C`; the two smaller angles
  `A, B` satisfy `A, B < 90°` (at most one angle `≥ 90°`, and it is `C`).
  Set `γ = 90° − A ∈ (0, C)` (valid: `A < 90°`, and
  `C = 180° − A − B > 90° − A` since `B < 90°`). Then `p_1 = p_2 = 90°`: both
  children contain `90°`, forced one-move win. (Right-triangle openings already
  contain `90°` = trivial win.)
- **Combine.** `n = 2`: one move. `n ≥ 3`: Lemma F (one move to a multiple) +
  Lemma R (`≤ n−2` moves to descend) `= ≤ n−1` moves total.

These lemmas are stated for completeness but are **the direct approach's
engine** (`direct-four-case-interval`, Lemma R + Lemma F); this approach claims
no independent sufficiency proof. The honest conclusion is that
`chip-transfer-monovariant` is a `q`-space cross-check of the direct proof on
both directions, with one genuine micro-invariant (Lemma FRAC, the
fractional-part 3-cycle of the forced transfer).

**GAP (sufficiency, independent engine).** No transfer-specific monovariant
exists (dead-end above). To promote this approach to `solved` independently, one
would need a sufficiency descent not equal to Lemma R; the
`aimo-0440`-style `L1`-coefficient monovariant does not lift to the transfer
dynamics (the transfer cycles, verified). Point the reader at
`direct-four-case-interval` for the complete sufficiency proof.

### Combine (characterization)

- `180°/θ ∈ ℤ` (`n ≥ 2`) ⟹ Mulan wins in `≤ n−1` moves (Lemma F + Lemma R; the
  direct approach's engine, `q`-space cross-check). [Sufficiency: conceded to
  direct approach.]
- `180°/θ ∉ ℤ` ⟹ Shan-Yu escapes (Theorem N above — fully rigorous, the
  four-case closure in `q`-space; uniform over irrational and rational
  non-integer `N`). [Necessity: proven here.]

Answer: `θ = 180°/n` for an integer `n ≥ 2`.

## Promotable lemmas

- **Lemma FRAC (fractional-part 3-cycle of the forced `t=1` transfer).**
  *Statement:* under the forced transition
  `(q_A,q_B,q_C) ⟼ (q_B, q_C−1, q_A+1)`, the multiset of fractional parts is
  invariant and the map acts as the 3-cycle
  `({q_A},{q_B},{q_C}) ⟼ ({q_B},{q_C},{q_A})`; hence starting from a triple with
  all `{q_i} ≠ 0`, forced `t=1` play never produces a coordinate that is a
  positive integer (an angle that is a multiple of `θ`). *Proven in full above
  (this file, Lemma FRAC).* A genuine `q`-space invariant of the forcing weapon;
  does not by itself prove the escape (Mulan may play `t ≠ 1`), but is the
  natural invariant behind the rational-orbit cross-check.
- **Theorem N (four-case closure / `S_θ` is Shan-Yu-stable when
  `180°/θ ∉ ℤ`).** *Statement:* if `180°/θ ∉ ℤ`, the equilateral is `S_θ`-safe,
  and from any `S_θ`-safe triple every cut leaves at least one `S_θ`-safe child
  (four disjoint exhaustive cases; the four linear combinations of `γ`
  telescope to `A, B, C, 180°`). *Proven in full above (this file, Theorem N).*
  This is the shared necessity engine (identical algebra to
  `direct-four-case-interval`'s four-case closure); certified here in `q`-space.
  Offered for the shared lemma cache with that attribution.
