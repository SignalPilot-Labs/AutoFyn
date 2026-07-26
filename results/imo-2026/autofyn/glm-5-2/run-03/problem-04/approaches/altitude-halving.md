# altitude-halving — IMO 2026 P4 (Mulan's triangle game)

Target answer: **Mulan can guarantee victory in finitely many steps if and only if
θ = 180°/n for some integer n ≥ 2** (equivalently, 180°/θ is a positive integer
≥ 2, i.e. 0° < θ ≤ 90°).

This proof follows Evan Chen's canonical route: the **halving lemma** and an
**altitude round-up cut** for sufficiency, and the **safe/unsafe dichotomy**
via the external-angle identities for necessity. Both directions are proven in
full below; the necessity closure is written as an exhaustive four-case
contradiction.

---

## Status
solved

## Approaches tried
- (round 1) altitude-halving — built the full Evan-Chen route end to end: angle-game reduction + cut-geometry lemma (proven), halving lemma (proven by strong induction on k), altitude round-up sufficiency for n ≥ 3 plus the n = 2 boundary (proven, k-existence verified, angle chase verified), safe/unsafe necessity with the four-case external-angle closure (proven exhaustively), Shan-Yu equilateral-opening strategy (proven). Computations sanity-checked with numpy. Outcome: complete, both directions, characterization stated and verified.

## Current best
Complete proof of the characterization θ = 180°/n ⟺ Mulan wins. No gaps.

## Full proof

### 0. Notation and conventions

Angles are in degrees. Throughout, a "positive multiple of θ" means an angle
of the form mθ with m a positive integer (m ≥ 1). The value 0 is **not** an
angle and is **not** counted as a multiple of θ. All triangle angles lie in
the open interval (0°, 180°), so a positive multiple of θ that is an angle
satisfies 1 ≤ m ≤ ⌊(180°−ε)/θ⌋.

We write the angle triple of a triangle, sorted or labelled as convenient,
always summing to 180°.

### 1. Reduction to the angle game (cut-geometry lemma)

**Lemma 1 (cut geometry).** Let △ABC have angles (A, B, C) with A+B+C = 180°.
Let P be a point in the interior of side BC, and let the cut from P to the
opposite vertex A be made. Write α = ∠BAP ∈ (0, A). Then the two resulting
triangles have angle triples

  △ABP = (α, B, 180° − B − α),   △ACP = (A − α, C, B + α).

Conversely, every α ∈ (0, A) is realised by exactly one such point P on the
open segment BC.

*Proof.* In △ABP the angle at B is ∠ABP = B (P lies on BC, so BP ⊂ BC), the
angle at A is ∠BAP = α, and the third angle is 180° − B − α. In △ACP the
angle at C is ∠ACP = C, the angle at A is ∠CAP = A − α, and the third angle
is 180° − C − (A − α) = 180° − A − C + α = B + α (using A + B + C = 180°).
The two angles at P are supplementary:

  (180° − B − α) + (B + α) = 180°,

as they must be, since P lies on the segment BC.

For the converse, as P travels along the open segment BC from B to C, the
angle ∠BAP =: f(P) is continuous (it is the angle subtended at A by the
segment BP), with f → 0 as P → B and f → A as P → C. By the Intermediate
Value Theorem every value α ∈ (0, A) is attained. ∎

**Corollary (angle-game reduction).** The state of play is completely captured
by the angle triple (A, B, C) of the current triangle (side lengths are
irrelevant): a move consists of choosing a vertex (say A) and a parameter
α ∈ (0, A), producing the two children above; Shan-Yu discards one. The win
condition (some angle equals θ) depends only on the triple. Henceforth we
reason purely about angle triples, and we may relabel vertices freely.

### 2. The halving lemma (sufficiency core)

**Lemma 2 (halving lemma).** Suppose the current triangle has an angle equal
to kθ for some integer k ≥ 1. Then Mulan can force a win in at most k − 1
further moves.

*Proof.* Strong induction on k.

*Base k = 1:* the angle kθ = θ is already present, so the game stops at the
next check; 0 = k − 1 further moves.

*Inductive step, k ≥ 2:* Let the angle kθ sit at vertex A, so the current
triple is (kθ, B, C) with kθ + B + C = 180°. Mulan cuts at vertex A with
parameter α = θ (Lemma 1). This is a legal cut because 0 < θ < kθ (using
k ≥ 2 and θ > 0). The two children are

  △ABP = (θ, B, 180° − B − θ),   △ACP = (kθ − θ, C, B + θ) = ((k−1)θ, C, B + θ).

Both are valid triangles:
- △ABP contains θ as an angle; its third angle is 180° − B − θ = (kθ − θ) + C = (k−1)θ + C > 0, and B > 0, θ > 0.
- △ACP has angles ((k−1)θ, C, B + θ). Positivity: (k−1)θ > 0 (k ≥ 2), C > 0, and B + θ > 0; the sum is (k−1)θ + C + B + θ = kθ + B + C = 180°. ✓

The first child △ABP already contains θ, so if Shan-Yu keeps it, the game
stops and Mulan wins. To delay the loss, Shan-Yu must keep △ACP, which
contains the angle (k−1)θ. By the inductive hypothesis (with k replaced by
k − 1 ≥ 1), Mulan then wins in at most (k − 1) − 1 = k − 2 further moves. In
total at most 1 + (k − 2) = k − 1 further moves. ∎

### 3. Sufficiency — forcing a multiple of θ

Assume θ = 180°/n for an integer n ≥ 2. We give Mulan a strategy that, from
**any** initial triangle, wins in finitely many (in fact ≤ n) moves.

If the current triangle already contains the angle θ, Mulan wins in 0 moves;
assume henceforth that no angle equals θ.

#### 3a. Mulan's first move: produce a right triangle

**Claim.** In at most one move, Mulan can ensure the current triangle is
right-angled (has a 90° angle).

*Proof.* If the current triangle already has a 90° angle, there is nothing
to do. Otherwise:

- If the triangle is **acute** (all angles < 90°): drop the altitude from any
  vertex V to the opposite side. Since the triangle is acute, the foot F of
  this altitude lies in the interior of the opposite side. (Indeed, F lies
  on the segment iff both angles at the endpoints of that side are ≤ 90°, which
  holds for every side of an acute triangle.) The two children △VBF and △VCF
  are right-angled at F (since VF ⊥ BC).
- If the triangle is **obtuse**, let the obtuse angle be at vertex V
  (V-angle > 90°, the other two angles < 90°). Drop the altitude from V to
  the opposite side. The foot F lies on the segment: F lies on the opposite
  side iff the two remaining angles (both acute here) are ≤ 90°, which holds.
  The two children △VBF, △VCF are right-angled at F.

In both cases Mulan's altitude cut produces two right-angled children.
Whichever Shan-Yu keeps is a right triangle, so after this move the state is
a right triangle. ∎

Relabel the resulting right triangle as △ABC with ∠A = 90°, and the two
remaining angles ∠B, ∠C satisfying B + C = 90°. Relabel B, C if necessary so
that B ≤ C; then

  B ≤ 45°.                                                    (∗)

(For if B > 45°, then C = 90° − B < 45°, and we swap the names B ↔ C.)

#### 3b. The boundary n = 2 (θ = 90°)

If n = 2 then θ = 90°. After step 3a the current (right) triangle already
contains the angle 90° = θ, so the game stops at the next check and Mulan
wins. Total: ≤ 1 move. ✓

(If Shan-Yu happened to open with a right triangle, Mulan wins in 0 moves.
In all cases ≤ 1 move.)

#### 3c. The case n ≥ 3 (θ = 180°/n ≤ 60°): the round-up cut

We now choose an integer k with

  45° < kθ ≤ 90°.                                            (∗∗)

**Existence of k.** Set L = 45°/θ, R = 90°/θ = 2L; we seek an integer in
the half-open interval (L, 2L].

- If L < 1 (equivalently θ > 45°, i.e. 45° < θ ≤ 60° since n ≥ 3 ⟹ θ ≤ 60°):
  then 2L ∈ [1, 2), and 1 ∈ (L, 2L] because L < 1 ≤ 2L (the latter as
  L ≥ 0.75 > 0.5, since θ ≤ 60°). Take k = 1.
- If L = 1 (θ = 45°, n = 4): the interval is (1, 2], which contains 2. Take
  k = 2.
- If L > 1 (θ < 45°, equivalently n ≥ 5): the interval (L, 2L] has length
  L > 1, hence contains an integer (any interval of length strictly greater
  than 1 contains an integer: ⌈L⌉ satisfies L < ⌈L⌉ < L + 1 < 2L, so
  ⌈L⌉ ∈ (L, 2L]; if L is itself an integer use L + 1, which satisfies
  L < L + 1 and L + 1 ≤ L + 1 < 2L since L > 1).

Thus (∗∗) always has a solution when n ≥ 3.

**Bounding k.** From kθ ≤ 90° = nθ/2 we get k ≤ n/2, so in particular
k ≤ n/2 < n (n ≥ 3), whence

  n − k ≥ n/2 ≥ 3/2 > 1,  so  n − k ≥ 1  and  (n − k)θ > 0.

Also k ≥ 1 (by construction). Hence both kθ and (n − k)θ are positive
multiples of θ.

**The cut.** Mulan cuts at the right-angle vertex A with parameter

  α = kθ − B = ∠BAP,   where P ∈ BC.

We verify α is a legal parameter (Lemma 1 requires 0 < α < A = 90°):
- α > 0: by (∗∗), kθ > 45° ≥ B (the latter by (∗)), so α = kθ − B > 0.
- α < 90°: kθ ≤ 90° and B > 0, so α = kθ − B < 90°.

**Angle chase.** By Lemma 1 the two children are

  △ABP = (α, B, 180° − B − α) = (kθ − B,  B,  180° − kθ),
  △ACP = (A − α, C, B + α)     = (90° − kθ + B,  C,  kθ).

Using 180° = nθ:
- △ABP's third angle is 180° − kθ = (n − k)θ, a positive multiple of θ.
- △ACP's third angle is kθ, a positive multiple of θ.

Both children's angle triples are valid (all entries positive):
- △ABP: kθ − B = α > 0, B > 0, (n − k)θ > 0 (shown above); sum = nθ = 180°. ✓
- △ACP: 90° − kθ + B ≥ B > 0 (since kθ ≤ 90°), C > 0, kθ > 0; sum = 90° − kθ + B + C + kθ = 90° + (B + C) = 180°. ✓

**Conclusion of the round-up.** Whichever of △ABP, △ACP Shan-Yu keeps, it
contains a positive multiple of θ (namely (n − k)θ or kθ respectively).

**Note on the boundary kθ = 90°.** This occurs exactly when k = n/2 (so n is
even). Then △ABP's marked angle is (n − n/2)θ = (n/2)θ = 90°, and △ACP's
marked angle is kθ = 90°; both are the positive multiple (n/2)θ of θ. The
argument above is unaffected.

#### 3d. End of sufficiency

Combining: in at most one altitude move (0 if the initial triangle is already
right) Mulan obtains a right triangle; in at most one further round-up move
(0 if n = 2, since then the right triangle already contains θ) Mulan ensures
the current triangle contains a positive multiple mθ of θ, with m ∈ {k, n − k}
and 1 ≤ m ≤ n − 1. By the halving lemma (Lemma 2), Mulan then wins in at most
m − 1 ≤ n − 2 further moves. In total Mulan wins in at most

  1 (altitude, if needed) + 1 (round-up, if n ≥ 3) + (n − 2) ≤ n

moves. In particular she wins in finitely many moves, regardless of Shan-Yu's
play. Hence

  θ = 180°/n (n ≥ 2)  ⟹  Mulan can guarantee victory.                   (⇒)

### 4. Necessity — Shan-Yu's safe-angle invariant

Assume henceforth that θ ≠ 180°/n for every integer n ≥ 2; equivalently,
**180° is not a positive multiple of θ** (i.e. 180°/θ is not an integer ≥ 2,
which, given 0° < θ < 180°, is the same as saying 180°/θ ∉ {2, 3, 4, …}).

#### 4a. Safe and unsafe angles; the sum/difference lemma

Call an angle x **θ-unsafe** (or *marked*) if x = mθ for some positive
integer m ≥ 1; otherwise call x **θ-safe**. In particular θ itself is unsafe.
A triangle is **safe** if all three of its angles are θ-safe; it is **unsafe**
if at least one of its angles is θ-unsafe.

**Lemma 3 (safe ± unsafe = safe).** Let s be a θ-safe angle and u = mθ
(m ≥ 1) a θ-unsafe angle.
- If s + u is a valid angle (0° < s + u < 180°), then s + u is θ-safe.
- If s > u (so 0° < s − u), then s − u is θ-safe.

*Proof.* Suppose, for a contradiction, that s + u = ℓθ with ℓ ≥ 1. Then
s = (ℓ − m)θ. Since s > 0 we have ℓ > m, so ℓ − m ≥ 1, making s a positive
multiple of θ — contradicting s being θ-safe. The case s − u = ℓθ (ℓ ≥ 1)
gives s = (ℓ + m)θ with ℓ + m ≥ 2 ≥ 1, again a positive multiple —
contradiction. ∎

#### 4b. The external-angle identities

Let △ABC be safe, and let Mulan cut from vertex A to a point D in the
interior of side BC (we relabel the vertices so that the cut vertex is A).
Write α = ∠BAD ∈ (0, A); then ∠DAC = A − α. The two children are △ABD and
△ACD. Their "new" angles (those at D, and the two pieces of A) are:

  ∠ADB = 180° − α − B,      ∠ADC = B + α,            (†)
  ∠BAD = α,                ∠DAC = A − α.

The two identities in (†) are the standard **exterior-angle theorem** for
triangles (an exterior angle of a triangle equals the sum of the two
opposite interior angles):
- ∠ADC is the exterior angle of △ABD at D, so ∠ADC = ∠BAD + ∠ABD = α + B.
- ∠ADB is the exterior angle of △ACD at D, so ∠ADB = ∠DAC + ∠ACD = (A − α) + C = (180° − B) − α = 180° − α − B.

Both identities are consistent with ∠ADB + ∠ADC = 180° (D lies on segment
BC).

#### 4c. Closure lemma: a safe triangle cannot split into two unsafe children

**Lemma 4 (closure).** Let θ be such that 180° is θ-safe (i.e. θ ≠ 180°/n).
Let △ABC be a safe triangle, and let Mulan make any cut from a vertex to a
point on the opposite side. Then **at least one of the two children is safe**.

*Proof.* Relabel so the cut is from A to D ∈ BC, with parameter α = ∠BAD ∈
(0, A). The children are

  △ABD = (α, B, ∠ADB),     △ACD = (A − α, C, ∠ADC),

with ∠ADB, ∠ADC as in (†). The original angles A, B, C are θ-safe by
hypothesis. Hence:

- △ABD can be unsafe only through one of its **new** angles α or ∠ADB being
  a positive multiple of θ (the angle B is θ-safe by hypothesis).
- △ACD can be unsafe only through one of its new angles (A − α) or ∠ADC being
  a positive multiple of θ (C is θ-safe by hypothesis).

Suppose, for a contradiction, that **both** children are unsafe. We split
into four cases according to which new angle is unsafe in each child (the
choice is one of two per child, giving 2 × 2 = 4 exhaustive cases).

Write p, q, r, s ≥ 1 for the (positive integer) multiple indices.

**Case (i): α is unsafe and (A − α) is unsafe.**
Then α = pθ and A − α = qθ. Summing: A = (p + q)θ with p + q ≥ 2 ≥ 1, so A
is a positive multiple of θ — contradicting A being θ-safe. ✗

**Case (ii): α is unsafe and ∠ADC is unsafe.**
Then α = pθ and ∠ADC = qθ. By (†), ∠ADC = B + α, so
  B = ∠ADC − α = qθ − pθ = (q − p)θ.
Since B > 0 we have q > p, so q − p ≥ 1, making B a positive multiple of θ —
contradicting B being θ-safe. ✗

**Case (iii): ∠ADB is unsafe and (A − α) is unsafe.**
Then ∠ADB = pθ and A − α = qθ. By (†), ∠ADB = (A − α) + C, so
  C = ∠ADB − (A − α) = pθ − qθ = (p − q)θ.
Since C > 0 we have p > q, so p − q ≥ 1, making C a positive multiple of θ —
contradicting C being θ-safe. ✗

**Case (iv): ∠ADB is unsafe and ∠ADC is unsafe.**
Then ∠ADB = pθ and ∠ADC = qθ. Since D lies on segment BC, the two angles at
D are supplementary:
  180° = ∠ADB + ∠ADC = (p + q)θ,   with p + q ≥ 2 ≥ 1.
So 180° is a positive multiple of θ, i.e. θ = 180°/n for some integer
n = p + q ≥ 2 — contradicting the standing hypothesis that 180° is θ-safe
(θ ≠ 180°/n). ✗

The four cases are exhaustive (each child's unsafety is forced by exactly one
of its two new angles), and each leads to a contradiction. Hence it is
impossible for both children to be unsafe; at least one child is safe. ∎

#### 4d. Shan-Yu's strategy

Shan-Yu opens with the **equilateral** triangle (60°, 60°, 60°).

**The opening is safe.** If 60° were a positive multiple of θ, say 60° = mθ
(m ≥ 1), then 180° = 3·60° = 3mθ would also be a positive multiple of θ,
i.e. θ = 180°/(3m) with 3m ≥ 3 ≥ 2 — contradicting θ ≠ 180°/n. By
contrapositive, since 180° is θ-safe, 60° is θ-safe; the equilateral
triangle is safe.

**Shan-Yu maintains safety forever.** We prove by induction that after each
of Shan-Yu's replies, the current triangle is safe.

- *Base:* the opening equilateral triangle is safe (shown above).
- *Step:* suppose the current triangle T is safe. Mulan makes a cut from a
  vertex to a point on the opposite side (Lemma 1; this is the general form
  of a move). By the closure lemma (Lemma 4) — applicable because T is safe
  and 180° is θ-safe (the global hypothesis θ ≠ 180°/n) — at least one of the
  two children is safe. Shan-Yu discards the other and keeps a safe child as
  the new T.

By induction the current triangle is safe after every Shan-Yu reply.

**Mulan never wins.** A safe triangle has no angle that is a positive
multiple of θ; in particular no angle equals θ = 1·θ. Hence at every check
the current triangle fails to contain θ, the game does not stop, and Mulan
never wins. Therefore Shan-Yu has a strategy that avoids Mulan's victory
forever. Hence

  θ ≠ 180°/n (for every n ≥ 2)  ⟹  Mulan cannot guarantee victory.       (⇐)

### 5. Conclusion

Combining (⇒) of §3 and (⇐) of §4:

  **Mulan can guarantee her victory in finitely many steps if and only if
  θ = 180°/n for some integer n ≥ 2** (equivalently, 180°/θ is an integer with
  180°/θ ≥ 2, i.e. 0° < θ ≤ 90°).

The sufficiency strategy is explicit (altitude → round-up cut → halving
descent) and wins in at most n moves; the necessity strategy is the
equilateral opening plus the safe-angle invariant maintained by the
external-angle closure (Lemma 4). ∎

---

## Promotable lemmas

- **Halving lemma** (Lemma 2, this file, §2). *If the current triangle has an
  angle equal to kθ for some integer k ≥ 1, Mulan can force a win in at most
  k − 1 further moves.* Proven by strong induction on k; the cut α = θ at the
  kθ-vertex produces one child containing θ (immediate win if kept) and one
  containing (k−1)θ, on which induction applies. Reusable by any approach
  that needs the descent-within-θℤ step.

- **Cut-geometry / angle-game lemma** (Lemma 1, this file, §1). *Cut at
  vertex A (angle A), parameter α = ∠BAP ∈ (0, A), produces children
  (α, B, 180°−B−α) and (A−α, C, B+α); every α ∈ (0, A) is realised (IVT).*
  Reusable as the standard reduction to the angle game.

- **External-angle closure / four-case necessity lemma** (Lemma 4, this
  file, §4c). *If 180° is θ-safe and △ABC is safe, then any cut from a vertex
  to the opposite side leaves at least one safe child.* Proven by exhaustive
  four-case contradiction using the exterior-angle identities
  ∠ADC = B + α and ∠ADB = (A − α) + C. Reusable as the necessity spine
  (equivalent to the four-coset intersection lemma of the
  lattice-coset-descent approach).
