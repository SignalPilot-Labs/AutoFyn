# direct-four-case-interval

Target: the full characterization (both directions) of `θ` for which Mulan guarantees
victory in finitely many steps. Answer: **Mulan wins ⇔ `180°/θ ∈ ℤ` (integer `≥ 2`),
i.e. `θ = 180°/n` for an integer `n ≥ 2`.**

Technique: four-case closure of the safe set `S_θ` (necessity) + Lemma R (descent of the
multiple index) and Lemma F (an open interval of length `>1` contains an integer)
(sufficiency). All named theorems cited from `knowledge_base.md`.

## Status
solved

## Approaches tried
- (round 1) direct-four-case-interval — APPROVED by outline-reviewer; both engines
  (four-case closure, Lemma R+F) verified algebraically and on the 1° grid. Built into a
  complete proof this round: necessity via four-case closure + equilateral witness;
  sufficiency via the `n=2` special move and the Lemma R + Lemma F induction. All gaps
  closed. Status solved.

## Current best
The complete characterization, both directions, proven below.

## Full proof

We prove:

> **Theorem.** For `0° < θ < 180°`, Mulan can guarantee victory in finitely many steps
> (regardless of how Shan-Yu plays) **if and only if** `180°/θ` is an integer. Since
> `θ < 180°`, an integer value of `180°/θ` is automatically `≥ 2`; equivalently the winning
> angles are exactly `{ 180°/n : n = 2, 3, 4, … }`.

Write angles in degrees. A *triangle* is an ordered triple `(A,B,C)` of positive reals
with `A+B+C = 180`. An angle is a *multiple of `θ`* if it equals `kθ` for some integer
`k ≥ 1`. Define the **bad-angle set**

```
B_θ = { kθ : k ∈ ℤ_{≥1}, 0 < kθ < 180° }
```

(strict upper bound: an angle of a triangle is strictly less than `180°`, so `180°`
itself is **not** in `B_θ`). When `180°/θ = n ∈ ℤ`, `n ≥ 2` (since `θ < 180°` gives
`180°/θ > 1`), and `B_θ = { θ, 2θ, …, (n−1)θ }` (the value `nθ = 180°` is excluded). In
particular `θ = 1·θ ∈ B_θ` always (as `0° < θ < 180°`).

---

### 0. The one-move transition (the core reduction)

Let the current triangle have vertices `X, Y, Z` with angles `A = ∠X, B = ∠Y, C = ∠Z`.
Mulan picks a point `P` on the side `XY` (the side opposite `Z`, i.e. the side not
containing `Z`), `P ≠ X, Y`. She cuts from `P` to `Z`. Write `γ = ∠XZP ∈ (0, C)` for the
piece of `C` adjacent to `X` (so the complementary piece is `∠PZY = C − γ`). Because
`P` lies on segment `XY`, the two angles at `P` are **supplementary** (they form a
straight line):
`∠XPZ + ∠ZPY = 180°`.

The two children are

```
T1 = △XPZ  with angles  (A, γ, 180° − A − γ),
T2 = △YPZ  with angles  (B, C − γ, A + γ).
```

Checks: the angle at `X` is inherited as `A`; at `Y` as `B`; at `Z` the angle `C` is split
into `γ` (in `T1`) and `C−γ` (in `T2`). The angle of `T1` at `P` is
`180° − A − γ` (call it `p1`); the angle of `T2` at `P` is `A + γ` (call it `p2`), since
`B + (C−γ) + (A+γ) = A+B+C = 180°`. Both sums are `180°`, and

```
p1 + p2 = (180° − A − γ) + (A + γ) = 180°.        (supplementary P-angles)
```

So a move is: pick a vertex to split (`Z` above; the others are identical up to relabeling)
and a real `γ ∈ (0, C)`. The four *new* angles created are `γ, p1 = 180°−A−γ, C−γ,
p2 = A+γ`; the angles `A` (in `T1`) and `B` (in `T2`) are inherited unchanged; the angle
`C` does **not** survive whole in either child. Shan-Yu then keeps one child as the new
`T`.

**One-move forced win.** Mulan wins at the next check iff the kept triangle contains
`θ`. Since Shan-Yu chooses the kept triangle, Mulan wins *in one move* iff **both**
children contain an angle that is a multiple of `θ` (so that whichever child is kept, the
next check fires).

---

### I. Necessity: `180°/θ ∉ ℤ` ⇒ Shan-Yu escapes

Define the **safe set**
```
S_θ = { (A,B,C) : no angle of (A,B,C) lies in B_θ }.
```
A safe triangle contains no multiple of `θ`; in particular it contains no `θ` (as
`θ ∈ B_θ`), so a safe triangle has not yet lost.

#### I.1 Closure of `S_θ` (four-case analysis)

**Claim.** If `(A,B,C) ∈ S_θ` and `180°/θ ∉ ℤ`, then for every Mulan cut, at least one of
the two children again lies in `S_θ`.

*Proof.* By relabeling we may assume Mulan cuts at vertex `Z` (angle `C`) with parameter
`γ ∈ (0,C)`, producing `T1 = (A, γ, p1)` and `T2 = (B, C−γ, p2)` as in §0, with
`p1 = 180°−A−γ`, `p2 = A+γ`, `p1+p2 = 180°`. Suppose, for contradiction, that **both**
children leave `S_θ`, i.e. each contains a `B_θ`-angle.

- `T1`'s angles are `A, γ, p1`. Because `(A,B,C) ∈ S_θ`, the inherited angle `A ∉ B_θ`.
  Hence the bad angle of `T1` is either `γ` or `p1`.
- `T2`'s angles are `B, C−γ, p2`. Because `B ∉ B_θ`, the bad angle of `T2` is either
  `C−γ` or `p2`.

(The bad angle, being in `B_θ`, is one specific element `kθ` for a positive integer
`k`.) This gives four disjoint, exhaustive cases (the choice for `T1` crossed with the
choice for `T2`):

**(i)** `γ = k₁θ` and `C−γ = k₂θ` (with `k₁,k₂ ∈ ℤ_{≥1}`). Adding,
`γ + (C−γ) = C = (k₁+k₂)θ`. Since `C` is a positive angle of a safe triangle, `0 < C < 180°`,
so `k₁+k₂ ≥ 1` and `(k₁+k₂)θ = C < 180°`, i.e. `C ∈ B_θ` — contradicting `C ∉ B_θ`.

**(ii)** `γ = k₁θ` and `p2 = A+γ = k₂θ`. Subtracting, `A = p2 − γ = (k₂−k₁)θ`. Since
`A > 0`, `k₂ > k₁`, so `k₂−k₁ ∈ ℤ_{≥1}` and `A = (k₂−k₁)θ`. Also `A < 180°` (it is an
angle), so `A ∈ B_θ` — contradicting `A ∉ B_θ`.

**(iii)** `p1 = 180°−A−γ = k₁θ` and `C−γ = k₂θ`. From `p1 = k₁θ`: `γ = 180°−A−k₁θ`. From
`C−γ = k₂θ`: `γ = C−k₂θ`. Equating,
`180° − A − k₁θ = C − k₂θ`, hence `180° − A − C = (k₁−k₂)θ`. But `180° − A − C = B`, so
`B = (k₁−k₂)θ`. Since `B > 0`, `k₁ > k₂`, i.e. `k₁−k₂ ∈ ℤ_{≥1}`; and `B < 180°`, so
`B ∈ B_θ` — contradicting `B ∉ B_θ`.

**(iv)** `p1 = k₁θ` and `p2 = k₂θ`. Adding (using `p1+p2 = 180°`),
`180° = (k₁+k₂)θ`, i.e. `180°/θ = k₁+k₂ ∈ ℤ_{≥1}`. In fact `k₁+k₂ ≥ 2` (each `kᵢ ≥ 1`).

By hypothesis `180°/θ ∉ ℤ`, so case **(iv)** is impossible; and cases (i)–(iii) each
contradict the safety of `(A,B,C)`. Hence it is impossible for both children to leave
`S_θ`: at least one child lies in `S_θ`. ∎

(Cases (i)–(iv) are exhaustive: each of `T1`'s and `T2`'s bad angle is one of two
explicit new angles, giving `2×2 = 4` combinations; they are disjoint because each names a
distinct pair of new angles. The four linear combinations of `γ` telescope to `C, A, B,
180°` respectively — the four "things that would have to be a multiple of `θ`".)

This uses the **Casework / exhaustion** technique (knowledge_base.md, General Proof
Methods) with **Contradiction** (each case contradicts a known `B_θ`-freeness); the
load-bearing geometric input is the supplementary-`P`-angles identity `p1+p2=180°`.

#### I.2 A safe opening: the equilateral

**Claim.** If `180°/θ ∉ ℤ` then the equilateral triangle `(60°, 60°, 60°)` lies in `S_θ`.

*Proof.* Suppose `60° = kθ` for some `k ∈ ℤ_{≥1}`. Then `θ = 60°/k`, so
`180°/θ = 180°·k/60° = 3k ∈ ℤ`, contradicting `180°/θ ∉ ℤ`. Hence no angle of the
equilateral is a multiple of `θ`; the equilateral is `B_θ`-free, i.e. in `S_θ`. ∎

#### I.3 Shan-Yu's escape strategy

Shan-Yu opens with the equilateral `(60°,60°,60°) ∈ S_θ` (valid by I.2, available because
Shan-Yu chooses the initial triangle). Inductively suppose the current `T ∈ S_θ`. Mulan
cuts; by I.1 at least one child lies in `S_θ`; Shan-Yu keeps that child. Thus the kept
triangle is always in `S_θ`. Since `θ ∈ B_θ` and `S_θ`-triples have no `B_θ`-angle, the
kept triangle never contains `θ`; the stopping condition never fires. Mulan does not win
in any finite number of steps.

This is an **Invariant** argument (knowledge_base.md, *Invariants & monovariants*): the
property "`T ∈ S_θ`" is preserved under Shan-Yu's best response. The escape works
uniformly for every `θ` with `180°/θ ∉ ℤ` — whether `180°/θ` is irrational or a
non-`1/n` rational (e.g. `θ = 50°, 72°, 80°, 100°, 120°`, all `θ > 90°`, etc.); the
four-case closure is purely algebraic and uses no discreteness. This establishes the
necessity direction. ∎

---

### II. Sufficiency: `180°/θ = n ∈ ℤ`, `n ≥ 2` ⇒ Mulan wins in `≤ n−1` moves

Now `θ = 180°/n` with `n ≥ 2` integer, and `B_θ = { θ, 2θ, …, (n−1)θ }`. We give an
explicit Mulan strategy that wins from **every** opening triangle in at most `n−1` moves,
regardless of Shan-Yu. Two lemmas, then the `n=2` special case.

#### II.1 Lemma R (descent of the multiple index)

**Lemma R.** Let `T` be a triangle having an angle equal to `mθ` at one of its vertices,
with `1 ≤ m ≤ n−1`. Then Mulan can force a win in at most `m−1` further moves.

*Proof by induction on `m`.*

**Base `m = 1`.** The triangle already contains `θ`; the stopping check fires
immediately. Mulan has won in `0 = 1−1` moves.

**Inductive step `m ≥ 2`.** Let `V` be a vertex of `T` whose angle is `mθ`; write the
other two angles as `A` and `B` (so `A + B = 180° − mθ = (n−m)θ`, in particular
`n − m ≥ 1`, i.e. `m ≤ n−1`, consistent with the hypothesis). Mulan cuts at `V` with
parameter `γ = θ`. This is a legal cut because `θ < mθ` (since `m ≥ 2`), i.e.
`γ = θ ∈ (0, mθ) = (0, C)`.

Relabeling so that `C = mθ` is the split angle and `A` is the angle at the adjacent
vertex `X`, the children are, by §0,
```
T1 = (A,  γ,       p1)  =  (A,  θ,       180° − A − θ),
T2 = (B,  C−γ,     p2)  =  (B,  (m−1)θ,   A + θ).
```

Legality check for `T2` (the descent child): all three angles are positive. `B > 0`
(inherited). `(m−1)θ > 0` since `m ≥ 2`. `A + θ > 0` since `A > 0, θ > 0`. Moreover
`A + θ < 180°`: from `A + B = (n−m)θ` and `B > 0` we get `A < (n−m)θ`, hence
`A + θ < (n−m)θ + θ = (n−m+1)θ ≤ (n−1)θ < nθ = 180°` (using `m ≥ 2 ⇒ n−m+1 ≤ n−1`). So
`T2` is a genuine triangle.

Now:
- `T1` contains the angle `γ = θ = 1·θ ∈ B_θ`. If Shan-Yu keeps `T1`, the next check
  finds `θ` and Mulan wins (total `1` move from this step).
- `T2` contains the angle `(m−1)θ` at vertex `V` (a genuine vertex angle of `T2`, since
  `V` is a vertex of both children). The index `m−1` satisfies `1 ≤ m−1 ≤ n−2 ≤ n−1`, so
  the induction hypothesis applies to `T2`: if Shan-Yu keeps `T2`, Mulan wins in at most
  `(m−1) − 1 = m−2` further moves, i.e. `≤ m−1` moves total from this step.

Either choice of Shan-Yu gives a win in `≤ m−1` moves. This closes the induction. ∎

(Technique: **Induction** on the multiple index, knowledge_base.md, General Proof Methods.
The angle `(m−1)θ` survives as a clean, splittable *vertex* angle of `T2`, so the
induction iterates; the legality bound `A+θ < 180°` holds at every step because the
inequality `A < (n−m)θ` is re-established at each step with the current `(A, m)`.)

#### II.2 Lemma F (reaching a multiple from a `B_θ`-free triangle, `n ≥ 3`)

**Lemma F.** Let `n ≥ 3` and let `T = (A, B, C)` be a `B_θ`-free triangle (no angle in
`B_θ`). Mulan can make a single move after which **both** children contain a `B_θ`-angle.

*Proof.* Relabel so that `C` is a **largest** angle of `T` (so `C ≥ A` and `C ≥ B`).
Because `A+B+C = 180°` and `C ≥ A, C ≥ B`, we have `3C ≥ 180°`, i.e. `C ≥ 60°`. Since
`n ≥ 3`, `θ = 180°/n ≤ 60°`, hence `C ≥ θ`. Because `T` is `B_θ`-free and `θ ∈ B_θ`,
`C ≠ θ`; therefore `C > θ`, i.e. `C/θ > 1`.

Consider the open interval
```
I = ( A/θ ,  (A+C)/θ ),     length  (A+C)/θ − A/θ = C/θ > 1.
```
**Fact (Pigeonhole / extremal).** *An open real interval of length strictly greater than
`1` contains an integer.* Indeed, for `I = (α, β)` with `β − α > 1`, set
`k = ⌊α⌋ + 1`; then `k` is an integer, `k > α` (since `⌊α⌋ ≤ α < ⌊α⌋+1`), and
`k ≤ α + 1 < β`. So `k ∈ I`. (knowledge_base.md, *Pigeonhole / extremal*.)

Apply this to `I`: there is an integer `k` with `A/θ < k < (A+C)/θ`. Define
`γ := kθ − A`. Then:
- `γ > 0` because `k > A/θ`;
- `γ < C` because `k < (A+C)/θ` gives `kθ < A + C`, i.e. `γ = kθ − A < C`.

So `γ ∈ (0, C)` strictly — the cut is non-degenerate (`P` is interior to the opposite
side, not a vertex). Mulan cuts at vertex `Z` (angle `C`) with this `γ`. The two new
`P`-angles are, by §0,
```
p2 = A + γ = A + (kθ − A) = kθ,
p1 = 180° − A − γ = 180° − (A + γ) = 180° − kθ = (n − k)θ.
```
We verify both are in `B_θ`:
- `k > A/θ > 0` (as `A > 0`) ⇒ `k ≥ 1`.
- `k < (A+C)/θ`. But `A + C = 180° − B < 180° = nθ` (since `B > 0`), so
  `(A+C)/θ < n`, hence `k < n`, i.e. `k ≤ n−1`.

Thus `1 ≤ k ≤ n−1`, so `p2 = kθ ∈ B_θ`. Symmetrically
`n − k ∈ {1, …, n−1}` (as `1 ≤ k ≤ n−1`), so `p1 = (n−k)θ ∈ B_θ`.

Hence `T1` contains the `B_θ`-angle `p1 = (n−k)θ` and `T2` contains the `B_θ`-angle
`p2 = kθ`; both children carry a multiple of `θ`. ∎

(Endpoint exclusion is strict: `k` is strictly inside `I`, which gives `γ ∈ (0, C)`
strictly; the boundary cases `A/θ ∈ ℤ` or `(A+C)/θ ∈ ℤ` are harmless because the
integer chosen is `⌊A/θ⌋+1`, strictly larger than `A/θ`, never equal to it.)

#### II.3 The base case `n = 2` (`θ = 90°`)

Here `B_θ = { 90° }` (since `2·90° = 180° ∉ B_θ`). If the opening `T` already has a
`90°`-angle, it is a right triangle and the game stops at once (Mulan wins in `0` moves).
Otherwise `T` is non-right. Relabel so `C` is the largest angle.

**Triangle fact.** A triangle has at most one angle `≥ 90°` (two angles `≥ 90°` would sum
to `≥ 180°`, leaving no room for the third). Hence the largest angle `C` is the only
candidate to be `≥ 90°`; the other two angles satisfy `A, B < 90°` (they are `≤ 90°` and
not equal to `90°` because `T` is non-right; and they are `> 0°`). This covers both the
acute opening (all angles `< 90°`) and the obtuse opening (`C > 90°`, `A, B < 90°`).

Mulan cuts at vertex `Z` (angle `C`) with `γ = 90° − A`. Legality:
- `γ = 90° − A > 0` since `A < 90°`;
- `γ = 90° − A < C` iff `90° < A + C = 180° − B` iff `B < 90°`, which holds.

So `γ ∈ (0, C)`. The two `P`-angles are
```
p2 = A + γ = A + (90° − A) = 90°,
p1 = 180° − A − γ = 180° − A − (90° − A) = 90°.
```
Both equal `90° = θ ∈ B_θ`. Both children contain `90°`; whichever Shan-Yu keeps, the next
check finds `θ = 90°` and Mulan wins. Total: `1 = n−1` move (or `0` if `T` was already
right). ∎

#### II.4 Combining (`n ≥ 3`)

Let `T` be any opening triangle.
- If `T` already contains `θ` (i.e. some angle `= θ`), the game stops at once: `0` moves.
- If `T` is `B_θ`-free but contains some `mθ` (`2 ≤ m ≤ n−1`): apply **Lemma R** directly;
  Mulan wins in `≤ m−1 ≤ n−2 ≤ n−1` moves.
- If `T` is `B_θ`-free and contains **no** `B_θ`-angle at all: by **Lemma F**, Mulan makes
  one move producing two children each carrying a `B_θ`-angle (`p1 = (n−k)θ`, `p2 = kθ`,
  both with index in `{1,…,n−1}`). Whichever child Shan-Yu keeps has an `m'θ`-angle with
  `1 ≤ m' ≤ n−1`; by **Lemma R** Mulan then wins in `≤ m'−1 ≤ n−2` further moves. Total
  `≤ 1 + (n−2) = n−1` moves.

In every case Mulan wins in at most `n−1` moves, regardless of Shan-Yu's choices. For
`n = 2` this is II.3 (`≤ 1` move). The bound is finite. ∎

(Technique: **Pigeonhole / extremal** for the integer-in-an-interval step;
**Induction** for the descent; **Casework** on the opening — already-`θ`,
`B_θ`-bearing, or fully `B_θ`-free — which is exhaustive and disjoint.)

---

### III. The characterization

Combining I and II:

- (**Necessity**, §I) If `180°/θ ∉ ℤ`, Shan-Yu opens the equilateral and maintains
  `B_θ`-freeness forever (four-case closure); Mulan never wins.
- (**Sufficiency**, §II) If `180°/θ = n ∈ ℤ` (`n ≥ 2`), Mulan wins from every opening in
  at most `n−1` moves, regardless of Shan-Yu's play.

The two cases partition all `θ ∈ (0°, 180°)` (`180°/θ` is either an integer `≥ 2` or
not). Therefore

```
Mulan guarantees victory in finitely many steps  ⇔  180°/θ ∈ ℤ,
```

i.e. the winning angles are exactly

```
θ ∈ { 180°/n : n = 2, 3, 4, … } = { 90°, 60°, 45°, 36°, 30°, … }.
```

**Tightness (both directions).**
- *Attainment.* For each integer `n ≥ 2`, taking `θ = 180°/n` makes Mulan win (§II), so
  every angle in the displayed set is a genuine winning angle.
- *Upper bound.* For every other `θ` (i.e. `180°/θ ∉ ℤ`, which includes all `θ > 90°`
  where `180°/θ ∈ (1,2)` is non-integer, and all `θ < 90°` with non-integer `180°/θ`),
  §I exhibits an explicit Shan-Yu strategy (open equilateral, keep a `B_θ`-free child)
  that prevents Mulan from ever winning. No angle outside the set is winning.

Both halves are constructive (explicit strategies for both players), so there is no
"neither-can-force" middle ground: the explicit Mulan strategy (§II) and the explicit
Shan-Yu strategy (§I) cover all `θ` and give opposite outcomes exactly on the boundary
`180°/θ ∈ ℤ`. ∎
