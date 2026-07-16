# Approach: force-2theta-bisect

## Status
solved

## Approaches tried
- (round 1, initial outline) — Complete-attempt skeleton with gaps G1–G4; same answer
  θ = 180/N as safe-set-invariant, winning side reframed as "reach an angle 2θ, then bisect."
- (round 1, this build) — Closed all gaps. The winning side is unified into a single
  repeated move ("cut θ off a marked multiple vertex"); chain entry proven from an arbitrary
  Shan-Yu start via the largest-angle > θ argument; impossibility reproven in full via the
  safe-set closure lemma (4-case split). **Complete, gapless.** Status: solved.

## Current best
Full two-sided proof below. Answer: **Mulan wins iff θ = 180°/N for some integer N ≥ 2.**
No remaining gap.

---

## Full proof

### 0. Setup and cut arithmetic

We measure all angles in degrees. A triangle is an unordered triple of positive angles
summing to `180`. We denote a triangle by its multiset of angles `(A, B, C)`.

**Cut Lemma (mechanics of one move).**
Let `T = (A, B, C)`. Suppose Mulan places `P` on the side opposite the vertex of angle `A`
and cuts from `P` to that vertex. Writing the two parts of the split angle `A` as `x` and
`A − x` with `x ∈ (0, A)`, the two resulting triangles are
```
    Child1 = ( x ,  B ,  A + C − x ),      Child2 = ( A − x ,  C ,  x + B ).
```

*Proof.* Let the vertices carrying angles `A, B, C` be `V_A, V_B, V_C`, and let `P` lie on
side `V_B V_C` (the side opposite `V_A`). The segment `V_A P` splits `T` into triangles
`V_A V_B P` and `V_A P V_C`.

- In `V_A V_B P`: the angle at `V_A` is the part of `A` on the `V_B` side, call it `x`; the
  angle at `V_B` is the full `B` (the side `V_A V_B` is uncut); the angle at `P` is
  `180 − x − B`. Since `A + B + C = 180`, we have `180 − B = A + C`, so the `P`-angle equals
  `A + C − x`. Thus `Child1 = (x, B, A + C − x)`.
- In `V_A P V_C`: the angle at `V_A` is the remaining part `A − x`; the angle at `V_C` is the
  full `C`; the angle at `P` is `180 − (A − x) − C = (180 − C) − A + x = (A + B) − A + x
  = x + B`. Thus `Child2 = (A − x, C, x + B)`.

Each triple sums to `180` (`x + B + A + C − x = A + B + C = 180`, and
`A − x + C + x + B = A + B + C = 180`) and, for `x ∈ (0, A)`, all six entries are positive,
so both children are genuine triangles. Finally note the two newly created `P`-angles are
**supplementary**: `(A + C − x) + (x + B) = A + B + C = 180`. ∎

We record two immediate consequences used throughout:

- **(Supplement identity.)** The two `P`-angles at any cut sum to `180`.
- **(Inheritance.)** Cutting the `A`-vertex leaves the other two vertex angles `B, C`
  untouched; they reappear (one in each child).

The analogous formulas for cutting the `B`- or `C`-vertex are obtained by permuting the roles
of `A, B, C`; we invoke this symmetry freely.

Throughout, set `N := 180 / θ` when convenient; then **`θ = 180/N` is equivalent to
`N ∈ ℤ`, `N ≥ 2`** (the constraint `0 < θ < 180` forces `N > 1`, and `N ≥ 2` since a triangle
angle `θ < 180`).

**Claimed answer.** *Mulan can force a win iff `θ = 180°/N` for some integer `N ≥ 2`,
equivalently `180/θ ∈ ℤ`.*

We prove sufficiency (Part I) and necessity (Part II) separately.

---

### Part I — Sufficiency: `θ = 180/N` (integer `N ≥ 2`) ⟹ Mulan wins

Fix `θ = 180/N`, `N ≥ 2` integer, so `Nθ = 180`. Shan-Yu makes some initial triangle `T₀`.
If `T₀` already has an angle equal to `θ`, the game stops immediately and Mulan wins with `0`
moves. So assume no angle of `T₀` equals `θ`.

We will exhibit an explicit Mulan strategy. Call an angle a **`k`-multiple** if it equals
`kθ` for a positive integer `k`. Because every triangle angle lies in `(0, 180) = (0, Nθ)`,
any multiple angle `kθ` present in a triangle satisfies `1 ≤ k ≤ N − 1`.

#### Lemma I.1 (Descent / terminal move).

*Let `T` be a triangle that has an angle exactly `kθ` for some integer `k` with `2 ≤ k ≤
N − 1`, and no angle equal to `θ`. Then Mulan can, in at most `k − 1` moves, force the game
into a triangle having an angle `θ` — i.e. she wins.*

*Proof.* We describe one move (the **descent move**) and iterate.

Let the marked vertex angle be `kθ`, and let the other two angles of `T` be `B'` and `C'`
(so `kθ + B' + C' = 180`). Mulan cuts the marked (`kθ`) vertex with `x = θ`. This is legal:
`x = θ ∈ (0, kθ)` because `k ≥ 2` gives `kθ > θ > 0`. By the Cut Lemma,
```
    Child1 = ( θ ,  B' ,  kθ + C' − θ ) = ( θ , B' , (k−1)θ + C' ),
    Child2 = ( kθ − θ , C' , θ + B' )   = ( (k−1)θ , C' , θ + B' ).
```
Both are valid triangles: their entries are positive (using `k ≥ 2`, so `(k−1)θ ≥ θ > 0`)
and each triple sums to `180` (`θ + B' + (k−1)θ + C' = kθ + B' + C' = 180`, and
`(k−1)θ + C' + θ + B' = kθ + B' + C' = 180`).

Now consider Shan-Yu's discard:

- **`Child1` has angle `θ`.** So if Shan-Yu keeps `Child1`, the new `T` has an angle `θ`,
  the game stops, and Mulan wins.
- **If Shan-Yu keeps `Child2`,** the new `T` has the marked angle `(k−1)θ`.
  - If `k = 2`: `(k−1)θ = θ`, so `Child2` *also* has an angle `θ`; the game stops and Mulan
    wins. (Thus for `k = 2` **both** children carry `θ` — this is the terminal "bisection"
    of a `2θ` angle: `θ + θ = 2θ`.)
  - If `k ≥ 3`: `(k−1)θ ≥ 2θ`, and the survivor is a triangle with a marked `(k−1)`-multiple
    (with `2 ≤ k−1 ≤ N−2`), and — since its angles are `(k−1)θ, C', θ+B'` — it has an angle
    `θ` only if Shan-Yu had already been handed a win; in the continuing branch we simply
    repeat the descent move on the new marked vertex `(k−1)θ`.

In the continuing branch the marked multiplicity strictly decreases: `k → k−1`. This is a
**monovariant** (knowledge_base.md, *General Proof Methods → Invariant / monovariant*)
bounded below by `2`. Hence after at most `k − 2` further descent moves the multiplicity
reaches `2`, at which point (the `k = 2` case above) **both** children carry `θ` and Shan-Yu
is forced to return a triangle with angle `θ`. In every branch the game stops with an angle
`θ` present, so Mulan wins, in at most `(k − 2) + 1 = k − 1` moves. ∎

#### Lemma I.2 (Chain entry from an arbitrary start, `N ≥ 3`).

*Let `N ≥ 3` and let `T` be any triangle with no angle equal to `θ`. Then Mulan has a single
legal cut after which, no matter which child Shan-Yu keeps, the surviving triangle has an
angle equal to some multiple `kθ` with `1 ≤ k ≤ N − 1`.*

*Proof.* Let `A` be a largest angle of `T`, and let `B, C` be the other two.

**Step 1: `A > θ` strictly.** Since the three angles sum to `180`, the largest satisfies
`A ≥ 60` (if all three were `< 60` the sum would be `< 180`), with equality iff all three
equal `60`. Because `N ≥ 3` we have `θ = 180/N ≤ 60`. Hence `A ≥ 60 ≥ θ`. Suppose `A = θ`.
Then `A = 60` and `θ = 60`, forcing `N = 3`; and `A = 60` being the largest angle forces all
angles to equal `60` (a largest angle equal to `60` in a triangle summing to `180` leaves the
other two summing to `120` with each `≤ 60`, hence each `= 60`). But then every angle equals
`60 = θ`, contradicting the hypothesis that no angle equals `θ`. Therefore `A > θ`.

**Step 2: a multiple lies strictly inside `(C, A + C)`.** Consider the open interval
`(C, A + C)`, of length `A > θ`. We claim it contains an integer multiple of `θ`.
Let `m := ⌊C/θ⌋ + 1`, the least integer with `mθ > C`. By minimality `(m−1)θ ≤ C`, so
`mθ ≤ C + θ`. Combining, `C < mθ ≤ C + θ < C + A` (the last inequality is `θ < A` from Step
1). Hence `n := m` satisfies
```
    C < nθ < A + C,        n a positive integer.
```
(Positivity of `n`: `nθ > C > 0`.)

**Step 3: the both-multiples cut.** Set `x := A + C − nθ`. Then `x ∈ (0, A)` because
`0 < A + C − nθ < A ⟺ C < nθ < A + C`, which is Step 2. Mulan cuts the `A`-vertex with this
`x`. By the Cut Lemma,
```
    Child1 = ( x , B , A + C − x ) = ( x , B , nθ ),
    Child2 = ( A − x , C , x + B ).
```
`Child1` carries the `P`-angle `A + C − x = nθ`. By the Supplement identity, the other
`P`-angle is `x + B = 180 − nθ = Nθ − nθ = (N − n)θ`, so
```
    Child2 = ( A − x , C , (N − n)θ ).
```
Thus **both** children carry a multiple of `θ`: `Child1` has `nθ`, `Child2` has `(N − n)θ`.
Since `nθ ∈ (C, A+C) ⊂ (0, 180) = (0, Nθ)`, we get `1 ≤ n ≤ N − 1`, and likewise
`1 ≤ N − n ≤ N − 1`. Whatever Shan-Yu discards, the survivor has an angle `kθ` with
`k ∈ {n, N − n} ⊆ {1, …, N − 1}`. ∎

#### Completing sufficiency.

**Case `N ≥ 3`.** Starting from `T₀` (no angle `θ`), Mulan plays the chain-entry cut of
Lemma I.2. The survivor has an angle `kθ`, `1 ≤ k ≤ N − 1`.
- If `k = 1`, that angle is `θ`, the game has already stopped, and Mulan has won.
- If `k ≥ 2`, the survivor satisfies the hypothesis of Lemma I.1 (angle `kθ`, `2 ≤ k ≤ N−1`;
  and it has no angle `θ`, else the game already stopped in Mulan's favour), so Mulan wins in
  at most `k − 1 ≤ N − 2` further moves.

Total: at most `1 + (N − 2) = N − 1` moves, finite. Mulan wins.

**Case `N = 2` (`θ = 90`).** Here `2θ = 180` is not a triangle angle, so Lemma I.1 does not
apply; we give a direct one-move win. Let `A` be a largest angle of `T₀`, `B, C` the others.
We claim `90 ∈ (C, A + C)`:
- `C < 90`: the two non-largest angles of a triangle are both `< 90` unless the triangle is
  right or obtuse at them — but `C ≤ A` and if `C ≥ 90` then `A ≥ 90` too, forcing
  `A + C ≥ 180`, impossible for a triangle with a positive third angle; so `C < 90`. (Equally
  `C ≠ 90` since no angle equals `θ = 90`.)
- `A + C > 90`: `A + C = 180 − B > 90 ⟺ B < 90`, and `B < 90` holds since `B ≤ A` and, if
  `B ≥ 90`, then `A ≥ 90` and `A + B ≥ 180`, impossible. (And `B ≠ 90`.)

So take `n = 1` (`nθ = 90 ∈ (C, A + C)`) and cut the `A`-vertex with `x = A + C − 90 ∈
(0, A)`. By the Cut Lemma and the Supplement identity,
```
    Child1 = ( x , B , 90 ),      Child2 = ( A − x , C , 180 − 90 ) = ( A − x , C , 90 ).
```
Both children have an angle `90 = θ`. Whatever Shan-Yu keeps, the new `T` has an angle `θ`,
the game stops, and Mulan wins in one move.

This proves: **for every integer `N ≥ 2`, `θ = 180/N` ⟹ Mulan wins.** ∎ (Part I)

---

### Part II — Necessity: `θ ≠ 180/N` ⟹ Shan-Yu survives forever

Assume `θ` is **not** of the form `180/N`, i.e. `180/θ ∉ ℤ`; equivalently `180` is not an
integer multiple of `θ`. (This includes all `θ > 90`, all irrational `θ`, and rationals such
as `72°` where `180/72 = 2.5 ∉ ℤ`.) We show Shan-Yu can prevent any angle from ever equalling
`θ`, so Mulan never wins.

**Safe set.** Call a triangle **safe** if none of its three angles is a positive integer
multiple of `θ`, i.e. no angle lies in `{θ, 2θ, 3θ, …}`. Let `S` be the set of safe
triangles. Note a safe triangle in particular has no angle equal to `θ = 1·θ`, so on a safe
triangle the game does not stop.

**Shan-Yu's opening.** Shan-Yu builds the initial triangle `(θ/2, θ/2, 180 − θ)`. It is a
valid triangle: all angles positive (`θ/2 > 0`, and `180 − θ > 0` since `θ < 180`) and their
sum is `θ/2 + θ/2 + (180 − θ) = 180`. It is safe:
- `θ/2 = (1/2)θ` is not an integer multiple of `θ` (the coefficient `1/2 ∉ ℤ`).
- `180 − θ` is a multiple of `θ` iff `180 − θ = mθ` for some positive integer `m`, iff
  `180 = (m + 1)θ`, iff `180/θ = m + 1 ∈ ℤ` — excluded by hypothesis. So `180 − θ` is not a
  multiple of `θ`.

Hence the opening triangle is in `S`.

#### Lemma II.1 (Closure of `S` under any cut).

*Let `θ` satisfy `180/θ ∉ ℤ`, and let `T = (A, B, C) ∈ S`. Then for every legal cut Mulan
can make, at least one of the two children is again in `S`.*

*Proof.* By the vertex symmetry noted in §0 it suffices to treat a cut at the `A`-vertex; the
cases for `B`- and `C`-vertices are identical after relabeling. Let `x ∈ (0, A)` and, by the
Cut Lemma,
```
    Child1 = ( x , B , A + C − x ),      Child2 = ( A − x , C , x + B ).
```
Suppose, for contradiction, that **both** children are non-safe, i.e. each has an angle that
is a positive integer multiple of `θ`.

Because `T ∈ S`, the inherited angles `B` (in `Child1`) and `C` (in `Child2`) are *not*
multiples of `θ`. Hence:

- `Child1` non-safe forces a multiple among its remaining angles: `x = pθ` **or**
  `A + C − x = qθ`, for positive integers `p, q`.
- `Child2` non-safe forces a multiple among its remaining angles: `A − x = rθ` **or**
  `x + B = sθ`, for positive integers `r, s`.

This gives `2 × 2 = 4` combinations; we derive a contradiction in each.

**(i) `x = pθ` and `A − x = rθ`.** Adding: `A = x + (A − x) = (p + r)θ`. Then `A` is a
positive integer multiple of `θ`, contradicting `T ∈ S`.

**(ii) `x = pθ` and `x + B = sθ`.** Subtracting: `B = (x + B) − x = (s − p)θ`. Since
`B > 0` and `B = sθ − pθ`, we have `s > p`, so `s − p ≥ 1` is a positive integer; thus `B` is
a multiple of `θ`, contradicting `T ∈ S`.

**(iii) `A + C − x = qθ` and `A − x = rθ`.** Subtracting:
`C = (A + C − x) − (A − x) = (q − r)θ`. Since `C > 0`, `q > r`, so `q − r ≥ 1`; thus `C` is a
multiple of `θ`, contradicting `T ∈ S`.

**(iv) `A + C − x = qθ` and `x + B = sθ`.** Adding:
`(A + C − x) + (x + B) = A + B + C = 180`, and the right side is `qθ + sθ = (q + s)θ`. Hence
`180 = (q + s)θ`, i.e. `180/θ = q + s ∈ ℤ`, contradicting `180/θ ∉ ℤ`.

All four cases are impossible, so both children cannot be non-safe. Therefore at least one
child is safe. ∎

*(Remark on exhaustiveness. The only angles of the two children that are not inherited safe
angles are exactly `x, A − x` (the two parts of the split vertex) and the two supplementary
`P`-angles `A + C − x, x + B`. A child is non-safe iff one of *its* two such new angles is a
multiple of `θ`. The four combinations above therefore exhaust every way both children could
be non-safe, and the same list arises verbatim for cuts at `B` or `C` after relabeling. In
each, the two equations either force a parent vertex angle to be a multiple of `θ`
(cases i–iii) or force `180` to be a multiple of `θ` (case iv). This is the crux identity:
the two `P`-angles are supplementary, so demanding both be multiples of `θ` forces their sum
`180` to be a multiple of `θ`.)*

#### Concluding necessity.

Shan-Yu plays as follows: open with `(θ/2, θ/2, 180 − θ) ∈ S`; thereafter, whenever Mulan
makes a cut, keep a child that lies in `S` (one exists by Lemma II.1). By induction on the
move number, the triangle `T` is safe before every move
(knowledge_base.md, *General Proof Methods → Induction*):
the base case is the safe opening, and the inductive step is exactly Lemma II.1. A safe
triangle never has an angle equal to `θ`, so the stopping condition is never met and the game
continues forever without Mulan winning. Hence Mulan cannot force a win when `θ ≠ 180/N`.
∎ (Part II)

---

### Conclusion and verification of the answer

Combining Part I and Part II:

> **Mulan can guarantee a win if and only if `θ = 180°/N` for some integer `N ≥ 2`**
> (equivalently `180/θ ∈ ℤ`).

**Verification / sanity checks.**

- *`θ = 90°` (`N = 2`).* By Part I (`N = 2` case): from any triangle without a `90°` angle,
  the single cut `x = A + C − 90` on the largest vertex yields two children each with a `90°`
  angle; Mulan wins in one move. E.g. from `(40, 60, 80)` (largest `A = 80`, take `C = 60`):
  `x = 80 + 60 − 90 = 50 ∈ (0, 80)`, giving `Child1 = (50, 60, 90)` and
  `Child2 = (30, 40, 90)`; both have `90°`. ✓
- *`θ = 60°` (`N = 3`).* From, say, `(50, 60?, …)` — take a triangle with no `60°`, e.g.
  `(50, 55, 75)`. Largest `A = 75`, `C = 55`, interval `(55, 130)` of length `75 > 60`
  contains `n·60 = 60` (`n = 1`): `x = 75 + 55 − 60 = 70 ∈ (0, 75)`, giving
  `Child1 = (70, 55, 60)` — already a `θ = 60°` angle, immediate win. ✓ (If instead a higher
  multiple appears, e.g. `nθ = 120`, Lemma I.1 descends `120° = 2θ → θ` in one bisecting cut.)
- *`θ = 72°` (`180/72 = 2.5 ∉ ℤ`).* By Part II, Shan-Yu opens with `(36, 36, 108)`; it is
  safe (`36 = θ/2`, `108 = 180 − 72` not a multiple of `72`). By the closure lemma every cut
  leaves a safe child (any attempt to make both children non-safe would force `180 = (q+s)·72`,
  i.e. `2.5 ∈ ℤ`, false), so Mulan never produces a `72°` angle. Mulan loses. ✓ This is the
  decisive discriminator against the rival "rational `≤ 90°`" answer.
- *`θ > 90°` and irrational `θ`.* Both satisfy `180/θ ∉ ℤ`, so Part II applies uniformly;
  Mulan loses. ✓

This establishes the full characterization, Mulan's explicit winning strategy for
`θ = 180/N`, and Shan-Yu's explicit surviving strategy for all other `θ`. ∎

---

## Promotable lemmas

- **Cut Lemma (move mechanics).** Cutting vertex-angle `A` of `(A,B,C)` at `x ∈ (0,A)` yields
  `Child1 = (x, B, A+C−x)` and `Child2 = (A−x, C, x+B)`; the two `P`-angles `A+C−x` and `x+B`
  are supplementary, and `B, C` are inherited. Proved in full in §0.
- **Safe-set Closure Lemma.** If `180/θ ∉ ℤ` and `(A,B,C)` has no angle a positive integer
  multiple of `θ`, then every cut leaves at least one child with the same property. Proved in
  full as Lemma II.1 (4-case split, crux identity: supplementary `P`-angles ⟹ their sum `180`
  must be a multiple of `θ`). This is the shared impossibility lemma for the whole field.
- **Descent/terminal move.** A triangle with an angle `kθ` (`2 ≤ k ≤ N−1`, `Nθ=180`) and no
  angle `θ` is a forced win for Mulan in ≤ `k−1` moves via repeatedly cutting `θ` off the
  marked vertex (`x = θ`); at `k = 2` both children carry `θ`. Proved as Lemma I.1.
- **Chain-entry cut.** For `N ≥ 3`, from any triangle with no angle `θ`, cutting the largest
  vertex `A` (`> θ`) at `x = A + C − nθ` with the integer `n ∈ (C/θ, (A+C)/θ)` forces both
  children to carry multiples `nθ` and `(N−n)θ`. Proved as Lemma I.2.
