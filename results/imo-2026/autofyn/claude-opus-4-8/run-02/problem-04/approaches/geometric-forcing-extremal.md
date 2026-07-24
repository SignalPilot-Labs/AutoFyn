# Approach: geometric-forcing-extremal (raw angle arithmetic, no quotient group)

## Status
solved

## Answer
Mulan can guarantee victory **iff** θ = 180°/n for some integer n ≥ 2; equivalently iff
180/θ is an integer ≥ 2, i.e. iff θ divides 180 an integral number of times. Since
0° < θ < 180°, this forces θ ∈ {90°, 60°, 45°, 36°, 30°, …} = {180°/n : n = 2, 3, 4, …},
so all such θ satisfy θ ≤ 90°.

## Approaches tried
- (this file) raw-degree constructions + extremal covering; deliberately avoids the quotient
  group so it is an independent check on the residue route. — **worked**: necessity closed by
  the raw-degree complementarity Lemma D (covers *all* θ∤180 in one stroke, θ>90 and θ≤90
  alike), with the non-obtuse survival invariant kept as an independent second proof for θ>90;
  sufficiency closed by the extremal alignment Lemma E (cut from the largest vertex, whose two
  P-angle ranges union to (α_min, 180−α_min)) followed by the peel Lemma F. All gaps
  G1/G2/G3 closed.

## Current best
Full solution (both directions), below.

## Full proof

Throughout, work in degrees. A *triangle* is an unordered triple of positive reals summing to
180 (its angle measures). The game position is such a triple; Mulan wins the instant some entry
equals θ.

### 0. The move algebra

Let the current triangle have vertices A, B, C with angle measures α, β, γ at A, B, C
respectively (α + β + γ = 180). Mulan picks a point P on the perimeter, other than a vertex,
and cuts to the opposite vertex. Say P lies on the open segment BC, so the cevian is AP and the
opposite vertex is A ("apex"). Let x = ∠BAP; as P ranges over the open segment BC, x ranges over
the open interval (0, α), and every value in (0, α) is attained exactly once (∠BAP is a
continuous strictly increasing function of the position of P from B to C, from 0 up to α). The
cevian creates two supplementary angles at P: ∠APB and ∠APC with ∠APB + ∠APC = 180.

The two child triangles are:
- **T₁ = ABP**, with angles x (at A), β (at B), and ∠APB = 180 − β − x (at P);
- **T₂ = ACP**, with angles α − x (at A), γ (at C), and ∠APC at P.

Using γ = 180 − α − β, the P-angle of T₂ is ∠APC = 180 − γ − (α − x) = β + x. Hence

  **T₁ = {x, β, 180 − β − x},  T₂ = {α − x, γ, β + x}.** (★)

Consistency checks: each triple sums to 180; the two P-angles 180 − β − x and β + x sum to 180
(supplementary, as they must be); β is retained untouched in T₁, γ in T₂, and the apex angle α
is split as x + (α − x). By relabeling A, B, C, formula (★) describes a cut from *any* chosen
apex, and letting x range over (0, α) describes *every* choice of P on the opposite side. So (★)
covers every legal Mulan move.

We will invoke two named tools from `knowledge_base.md`:
- **Pigeonhole / extremal principle** (KB, "Combinatorics" and "Pigeonhole / extremal"): take
  the extremal — here largest / smallest — angle and argue from it.
- **Invariants & monovariants** (KB, "Invariants & monovariants"): a property preserved across
  moves proves unreachability.
We also use the **Intermediate Value Theorem** (standard real analysis; not in KB, invoked by
name): a continuous function on an interval attains every value between two of its values.

---

### 1. Necessity: if θ does not divide 180, Shan-Yu survives forever

Fix θ with 180/θ ∉ ℤ (equivalently θ ∤ 180). All congruences below are **modulo θ**.

**Definition.** A triangle is *good* if none of its three angles is an integer multiple of θ
(i.e. no angle ≡ 0 (mod θ)). A good triangle in particular has no angle equal to θ (θ ≡ 0), so
the game does not stop at a good position.

#### Lemma D (fixed-sum covering).
*If T is good and θ ∤ 180, then for every legal Mulan cut of T at least one of the two child
triangles is good.*

*Proof.* Take the cut in the form (★): apex angle α, retained base angles β (in T₁) and γ (in
T₂), split parameter x ∈ (0, α). Since T is good, α, β, γ ≢ 0 (mod θ).

Read off from (★) when a child is *bad* (has an angle ≡ 0):

- **T₁ = {x, β, 180 − β − x}.** Here β ≢ 0. So T₁ is bad ⟺ x ≡ 0, or 180 − β − x ≡ 0.
  That is, T₁ bad ⟺ x ≡ 0 or x ≡ 180 − β (mod θ). Call this set S₁ = {0, 180 − β} (mod θ).

- **T₂ = {α − x, γ, β + x}.** Here γ ≢ 0. So T₂ is bad ⟺ α − x ≡ 0, or β + x ≡ 0.
  That is, T₂ bad ⟺ x ≡ α or x ≡ −β (mod θ). Call this set S₂ = {α, −β} (mod θ).

For a *single* x to make **both** children bad we would need x ∈ S₁ ∩ S₂ (mod θ), i.e. some
element of S₁ is congruent to some element of S₂. There are exactly four pairings; we show each
one contradicts the hypotheses. This is an exhaustive case split (KB, "Casework / exhaustion").

  (i) 0 ≡ α (mod θ): then α ≡ 0, contradicting goodness (α is an angle of T).
  (ii) 0 ≡ −β (mod θ): then β ≡ 0, contradicting goodness.
  (iii) 180 − β ≡ α (mod θ): then 180 ≡ α + β = 180 − γ, so γ ≡ 0, contradicting goodness.
  (iv) 180 − β ≡ −β (mod θ): then 180 ≡ 0 (mod θ), i.e. θ ∣ 180, contradicting θ ∤ 180.

All four pairings are impossible, so S₁ ∩ S₂ = ∅ (mod θ). Therefore no value of x makes both
children bad: whichever x Mulan chose, at least one child is good. Because this argument used
only that all three of α, β, γ are ≢ 0 and that θ ∤ 180 — facts symmetric in the three vertices
— it holds for every choice of apex, hence for every legal Mulan move. ∎ (Lemma D)

#### Necessity, concluded.
Because θ ∤ 180, only finitely many multiples of θ lie in (0, 180); call this finite set M.
Shan-Yu can choose a good initial triangle: pick α₀ ∈ (0, 60) with α₀ ∉ M (the interval (0, 60)
minus the finite set M is nonempty), then pick β₀ ∈ (0, 60) with β₀ ∉ M and 180 − α₀ − β₀ ∉ M
(this excludes β₀ from the two finite sets M and (180 − α₀ − M), still leaving infinitely many
choices in (0, 60)); set γ₀ = 180 − α₀ − β₀ ∈ (60, 180). Then α₀, β₀, γ₀ are three positive
angles summing to 180, none a multiple of θ — a good triangle, and no angle equals θ.

Now Shan-Yu plays the **invariant strategy** (KB, "Invariants & monovariants"): whenever Mulan
cuts, keep a good child, which exists by Lemma D. By induction the position is good after every
move, so no angle ever equals θ and the game never stops. Hence for θ ∤ 180 Mulan cannot force a
win. This covers **all** θ with 180/θ ∉ ℤ, whether θ ≤ 90 or θ > 90. ∎

#### Independent second proof for θ > 90 (non-obtuse survival invariant).
For robustness we record a self-contained argument, disjoint from Lemma D, that kills every
θ > 90 directly. (Every θ ∈ (90, 180) has 180/θ ∈ (1, 2) ∉ ℤ, so this range is already inside
the case above; the point is that this proof does not use residues at all.)

Shan-Yu starts with the equilateral triangle {60, 60, 60} and maintains the invariant

  **(NO): every angle of the current triangle is ≤ 90.**

Initially max = 60 ≤ 90. Suppose (NO) holds and Mulan cuts as in (★) with apex α ≤ 90 and base
angles β, γ ≤ 90. The children's angles are:
- T₁ = {x, β, 180 − β − x}: here x < α ≤ 90 and β ≤ 90.
- T₂ = {α − x, γ, β + x}: here α − x < α ≤ 90 and γ ≤ 90.
So the only angles that could exceed 90 are the two P-angles 180 − β − x (in T₁) and β + x
(in T₂). They sum to 180, so at most one of them exceeds 90. If 180 − β − x ≤ 90, keep T₁: all
its angles are ≤ 90. Otherwise 180 − β − x > 90, whence β + x = 180 − (180 − β − x) < 90, so
keep T₂: all its angles are ≤ 90. Either way Shan-Yu keeps a child satisfying (NO), so (NO) is
preserved. By induction every angle stays ≤ 90 forever; since θ > 90, no angle ever equals θ,
and the game never stops. ∎

*(Remark on gap G2: no "gluing at 90°" is needed. Lemma D is one uniform proof valid for every
θ ∤ 180. The non-obtuse invariant is an optional independent confirmation on the sub-range
θ > 90, where it happens to be especially transparent.)*

---

### 2. Sufficiency: if θ = 180/n (n ≥ 2 integer), Mulan wins

Assume 180 = nθ with n ≥ 2 an integer. The positive multiples of θ inside (0, 180) are exactly
θ, 2θ, …, (n − 1)θ. Mulan's plan: (E) one *alignment* cut installs a multiple of θ into
whichever child Shan-Yu keeps; (F) a *peel* chain drives that multiple down to a forced
double-θ fork. We may assume the current triangle has no angle equal to θ (else Mulan has
already won).

#### Lemma E (alignment from the largest vertex).
*Let T be any triangle with smallest angle α_min. Cutting from a vertex of largest angle, Mulan
can realize, as the angle at P of one child, any prescribed value v with α_min < v < 180 − α_min.
Consequently, since some multiple of θ lies strictly between α_min and 180 − α_min, Mulan can
make one P-angle equal to a multiple kθ (1 ≤ k ≤ n − 1); the other P-angle is then the
supplement 180 − kθ = (n − k)θ, also a multiple of θ. Thus **both** children carry a P-angle
that is a positive multiple of θ.*

*Proof.* Label so that C is a vertex of largest angle γ, and the two remaining (smaller) angles
are α ≤ β at A, B; so γ ≥ β ≥ α and α = α_min. Cut from apex C with P on segment AB. By (★)
with the roles (apex = C, bases A and B), as P sweeps the open side AB the P-angle on the A-side
ranges over the open interval (β, 180 − α) and the P-angle on the B-side ranges over the open
interval (α, 180 − β); each is a continuous, strictly monotone image of P's position, so by the
**Intermediate Value Theorem** every value in the respective open interval is attained by some
interior P (a legal cut).

The union of the two attainable ranges is (α, 180 − β) ∪ (β, 180 − α). Since β is not the
largest angle, β < 90 (if β ≥ 90 then also γ ≥ β ≥ 90, forcing α = 180 − β − γ ≤ 0, impossible).
Hence β < 90 < 180 − β, so the two intervals overlap (their intersection (β, 180 − β) is
nonempty), and

  (α, 180 − β) ∪ (β, 180 − α) = (α, 180 − α) = (α_min, 180 − α_min).

Thus every value v ∈ (α_min, 180 − α_min) is a realizable P-angle for some interior cut from C.
This proves the first sentence (this is the extremal step — cut from the *largest* angle; KB,
"Pigeonhole / extremal principle").

It remains to exhibit a multiple of θ inside (α_min, 180 − α_min). The interval is symmetric
about 90 with radius 90 − α_min, and α_min ≤ 60 (the smallest angle of any triangle is ≤ 60).

- If n is even, then 90 = (n/2)θ is a multiple of θ, and 90 ∈ (α_min, 180 − α_min) because
  α_min ≤ 60 < 90. Take kθ = 90.
- If n is odd, the multiples of θ nearest 90 are (n∓1)/2·θ = 90 ∓ θ/2 = 90 ∓ 90/n, at distance
  90/n from 90. One of them lies in the interval provided 90/n < 90 − α_min, i.e.
  α_min < 90 − 90/n = 90(n − 1)/n. For n ≥ 5, 90(n − 1)/n ≥ 90·(4/5) = 72 > 60 ≥ α_min, so this
  holds. For n = 3 the bound is 90·(2/3) = 60, so we need α_min < 60; and α_min = 60 forces
  α = β = γ = 60 (equilateral), which for n = 3 (θ = 60) means an angle equals θ — a position
  already won, excluded by assumption. Hence α_min < 60 strictly at any live n = 3 position, and
  again a nearest multiple lies in the interval.

In all cases a multiple kθ with 1 ≤ k ≤ n − 1 lies in (α_min, 180 − α_min); realize it as one
P-angle. The supplementary P-angle equals 180 − kθ = (n − k)θ, a multiple of θ with
1 ≤ n − k ≤ n − 1. So both children of this cut have a P-angle that is a positive multiple of θ.
∎ (Lemma E)

After the alignment cut, whichever child Shan-Yu keeps has an angle equal to some mθ with
1 ≤ m ≤ n − 1. If m = 1 that angle is θ and Mulan has already won. Otherwise 2 ≤ m ≤ n − 1, and
Mulan peels.

#### Lemma F (peel to a double-θ fork).
*Suppose the current triangle has an angle equal to mθ with 2 ≤ m ≤ n − 1. Then Mulan can, in
finitely many forced moves, reach a position with an angle equal to θ (a win).*

*Proof.* Let the vertex carrying angle mθ be the apex; call its two base angles β, γ (so
β + γ = 180 − mθ = (n − m)θ > 0). Mulan cuts from this apex with x = (m − 1)θ. This is legal
because 0 < (m − 1)θ < mθ (as m ≥ 2), so x ∈ (0, apex). By (★) the children are

  T₁ = {(m − 1)θ, β, 180 − β − (m − 1)θ},  T₂ = {mθ − (m − 1)θ, γ, β + (m − 1)θ} = {θ, γ, β + (m − 1)θ}.

(Both are genuine triangles produced by a real cevian, so all their entries are automatically
positive and sum to 180.)

- If m = 2: then T₁ = {θ, β, 180 − β − θ} also contains θ (since (m − 1)θ = θ). So **both**
  children contain the angle θ — a double fork. Whichever child Shan-Yu keeps has an angle equal
  to θ, and Mulan wins on this move.

- If m ≥ 3: child T₂ contains the angle θ, so if Shan-Yu kept T₂ Mulan would win immediately;
  to survive, Shan-Yu is forced to keep T₁, which contains the angle (m − 1)θ with
  2 ≤ m − 1 ≤ n − 2. The invariant "current triangle has an angle equal to m′θ, 2 ≤ m′ ≤ n − 1"
  is thus restored with m′ = m − 1, a strictly smaller value.

Since m decreases by exactly 1 each peel and stays ≥ 2, after exactly m − 2 forced peels Mulan
reaches the case m = 2, where the double fork wins on the next move. The total number of moves is
finite (at most m − 1 ≤ n − 2). ∎ (Lemma F)

#### Sufficiency, concluded.
From Shan-Yu's live triangle (no angle = θ), Mulan applies Lemma E: after one cut, whatever
Shan-Yu keeps has an angle mθ, 1 ≤ m ≤ n − 1. If m = 1 she has already won; otherwise Lemma F
forces a win in finitely many further moves. Hence for θ = 180/n, n ≥ 2, Mulan wins in finitely
many steps regardless of Shan-Yu's play. ∎

---

### 3. Answer and verification

Combining Sections 1 and 2: Mulan can force a win **iff** θ = 180°/n for an integer n ≥ 2.
(If 180/θ ∉ ℤ, Section 1 gives Shan-Yu an eternal-survival strategy; if 180 = nθ with n ≥ 2,
Section 2 gives Mulan a forced win. Since 0 < θ < 180, θ = 180/n requires n ≥ 2, and every such
θ satisfies θ = 180/n ≤ 90.)

Spot-checks of the winning constructions:

- **θ = 90° (n = 2).** For any live triangle, α_min < 90, so 90 ∈ (α_min, 180 − α_min); the
  alignment cut from the largest vertex with P-angle = 90 is precisely the *altitude* from that
  vertex (AP ⊥ AB), and it makes both P-angles equal to 90 = θ. Mulan wins in **one** move.
  (Here 90 = 1·θ, so m = 1, no peel needed.)

- **θ = 60° (n = 3).** Take Shan-Yu's live triangle {32, 51, 97} (no angle is 60). Largest angle
  97 at apex; α_min = 32, interval (32, 148) contains the multiple 120 = 2θ (and 60 = θ). Cut
  from the 97-vertex to realize P-angle 120; the other child's P-angle is 60 = θ. Shan-Yu must
  discard the 60-child, keeping one with angle 120 = 2θ (m = 2). Peel with x = θ = 60 from the
  120-vertex: both children then carry a 60 = θ angle (double fork). Mulan wins within **two**
  moves.

- **θ = 45° (n = 4).** For a live triangle, 90 = 2θ ∈ (α_min, 180 − α_min) (α_min < 90). Align
  from the largest vertex to get a child with angle 90 = 2θ (m = 2), then peel with x = 45: both
  children carry 45 = θ. Mulan wins within **two** moves.

These agree with the general argument. ∎

## Promotable lemmas

- **Lemma D (fixed-sum covering / raw-degree necessity).** *If a triangle has no angle equal to
  a multiple of θ and 180 is not a multiple of θ, then any cevian cut leaves at least one child
  with no angle a multiple of θ.* Proved in full in Section 1 by the four-pairing case check on
  S₁ = {0, 180 − β}, S₂ = {α, −β} (mod θ); the only pairing that could coincide without an
  angle ≡ 0 forces 180 ≡ 0 (mod θ). (Raw-degree twin of residue-invariant's Lemma A.)

- **Lemma E (extremal alignment from the largest vertex).** *Cutting from a largest-angle vertex,
  every P-angle value in (α_min, 180 − α_min) is realizable, because the two orientation-ranges
  (α, 180 − β) and (β, 180 − α) overlap (β < 90) and union to (α_min, 180 − α_min); when
  180 = nθ this interval always contains a multiple of θ, whose supplement is also a multiple, so
  one cut puts a multiple of θ into both children.* Proved in full in Section 2.

- **Lemma F (peel to double-θ fork).** *An angle mθ (2 ≤ m ≤ n − 1), cut with x = (m − 1)θ,
  forces Shan-Yu to keep an (m − 1)θ child; iterating reaches m = 2, a double fork on θ.* Proved
  in full in Section 2. (Same as residue-invariant's Lemma C.)
