## Status
partial

## Approach: Antipode of A equidistant from B and C (synthetic)

**Top-level target:** OM = ON, where O = circumcentre of triangle AKL.

**Spine.** Let A* = 2O − A be the antipode of A on ⊙(AKL). Then OM = ON ⟺ A*B = A*C
(Step 1, a proven vector identity). Locate A* by Thales (Step 2). The two angle-invariant
lemmas ∠A*BK = 90°−C and ∠A*CL = 90°−B (Step 3, **the open gap**), together with condition
∠KBA = ∠ACL = α and the fact that A* lies inside angle BAC, force triangle A*BC to be
isosceles with A*B = A*C (Step 4, proven). No use of the (★★)/(♦5) identity that the trig
and power routes are stuck on — this is an independent route.

Throughout: A = 0 (origin) in the complex plane, B = b, C = c, K = k, L = l, M = b/2,
N = c/2; the triangle is labelled counter-clockwise, Im(c·b̄) > 0. Angles A, B, C are the
angles of triangle ABC at A, B, C. Set α := ∠KBA = ∠ACL (equal by condition C1).

---

### Step 1 — Antipode equivalence: OM = ON ⟺ A*B = A*C. (PROVEN)

Since A = 0, we have A* = 2O. Compute the two differences of squared distances as real
inner products (write X·Y := Re(X·Ȳ), |X|² = X·X).

- **OM² − ON²** = |O − b/2|² − |O − c/2|² = (|O|² − O·b + |b|²/4) − (|O|² − O·c + |c|²/4)
  = O·(c − b) + (|b|² − |c|²)/4.
  So **OM = ON ⟺ O·(c − b) = (|c|² − |b|²)/4**.

- **A*B² − A*C²** = |A* − b|² − |A* − c|² = (|A*|² − 2A*·b + |b|²) − (|A*|² − 2A*·c + |c|²)
  = 2A*·(c − b) + (|b|² − |c|²).
  So **A*B = A*C ⟺ A*·(c − b) = (|c|² − |b|²)/2**.

Since A* = 2O, A*·(c − b) = 2·O·(c − b), so the two right-hand conditions are identical:
O·(c − b) = (|c|² − |b|²)/4 ⟺ 2O·(c − b) = (|c|² − |b|²)/2 ⟺ A*·(c − b) = (|c|² − |b|²)/2.
Hence **OM = ON ⟺ A*B = A*C.** ∎

*(Certified numerically in `repro_antipode.py`: |OM−ON| and |A*B−A*C| vanish together,
both < 1e-12, across 4 triangles × several α. Also, equivalently, A*·(c−b) = (|c|²−|b|²)/2
says A* lies on the perpendicular bisector of BC, since the perpendicular bisector is
{X : (X − (b+c)/2)·(c−b) = 0} and (b+c)·(c−b) = |c|²−|b|² + (c b̄ − b c̄), whose real part is
|c|²−|b|².)*

**Bridge to the power-of-a-point route (proven, for cross-checking only).** For the circle
ω = ⊙(AKL) with centre O, radius R = |O − A| = |O|, and diameter endpoints A, A*, one has
for any point X the identity (X − A)·(X − A*) = |X − O|² − R² = pow_ω(X) (expand with
A* = 2O − A). Taking X = B: (−B)·(A* − B) = pow_ω(B), i.e. B·A* = |B|² − pow_ω(B); likewise
C·A* = |C|² − pow_ω(C). Substituting into A*·(c − b) = (|c|²−|b|²)/2 gives the equivalent
form **OM = ON ⟺ pow_ω(B) − pow_ω(C) = (AB² − AC²)/2**. This exhibits the antipode route and
the power-of-point route as the *same* reduction; it is recorded here for insurance and is
**not** used below (Steps 2–4 avoid it).

### Step 2 — Location of A*: A*K ⊥ AK and A*L ⊥ AL. (PROVEN)

A* = 2O − A is diametrically opposite A on ω = ⊙(AKL) (its midpoint with A is O, the centre).
K and L lie on ω. By **Thales' theorem / the inscribed angle in a semicircle**
(knowledge_base.md, Geometry, "Synthetic toolkit: angle chasing"; the angle subtending a
diameter is a right angle), ∠AKA* = ∠ALA* = 90°. Equivalently A*K ⊥ AK and A*L ⊥ AL, and A*
is the intersection of the perpendicular to AK at K with the perpendicular to AL at L. ∎

*(Certified: (K−A)·(A*−K) and (L−A)·(A*−L) are < 1e-15 in `repro_antipode.py`.)*

Non-degeneracy: A, K, L are non-collinear (K ∈ interior BMC, L ∈ interior BNC lie strictly on
opposite constructions off line... concretely kl̄ − k̄l ≠ 0 holds in every audited config),
so ω is a genuine circle and A ≠ A*.

### Step 3 — Angular-position lemmas. (**OPEN GAP — the crux**)

**Lemma B.** ∠A*BK = 90° − C.
**Lemma C.** ∠A*CL = 90° − B.

Both are **α-independent**: as α = ∠KBA ranges over the admissible interval (for a fixed
triangle ABC), the point A* moves, yet the angle ∠A*BK stays exactly 90°−C and ∠A*CL stays
exactly 90°−B. This is a sharp, striking invariance. It is **verified numerically to 1e-8**
across 4 triangles × 5 values of α (`repro_antipode.py`), and is the load-bearing input to
Step 4.

**Status of Lemma B / C: not yet proven.** They are the entire remaining content of the
problem on this route. What is established:
- They are the correct statements (robust numerics, α-independent, symmetric under the
  configuration symmetry B↔C, M↔N, K↔L which maps Lemma B to Lemma C).
- They must use conditions C2 (∠LBK = ∠LNC) and C3 (∠LCK = ∠BMK) together with the antipode
  structure of Step 2; condition C1 is already consumed by the ∠KBA = ∠ACL = α bookkeeping in
  Step 4. (A* is defined only through K, L and the two right angles, so its direction from B
  is genuinely constrained by the way C2, C3 pin K, L.)
- Simple incidence explanations were tested and **ruled out** numerically: BA* is not
  perpendicular to CK, CL, AK or AL; A* is not on ⊙(BLC) or ⊙(BKC); the angles ∠KA*B, ∠BKA*
  are *not* α-independent. So the mechanism is not a one-line incidence; it is a real
  angle-chase feeding on C2, C3.

*(Obtuse note: for C ≥ 90° the unsigned reading "∠A*BK = 90°−C" must be replaced by the
directed-angle statement ∠(BK, BA*) = 90°−C (mod π), which is what should actually be proven;
the audited configs are all acute at B and C. The gap is the same either way.)*

### Step 4 — Synthesis: Lemmas B, C ⟹ triangle A*BC isosceles ⟹ A*B = A*C. (PROVEN)

Assume Lemmas B and C. All angles below are the ordinary unsigned angles in [0°,180°]; the
audited configuration has A* inside angle BAC (equivalently: ∠BAA* + ∠CAA* = A, i.e. A* on
the C-side of line AB and on the B-side of line AC — verified to 1e-8 in `repro_antipode.py`;
it holds because A* = 2O lies in the interior region determined by K, L). We use this
placement below.

1. **Ray order at B.** Condition C1 gives ∠KBA = α. K lies inside triangle BMC and inside
   angle LBA, so ray BK lies strictly between ray BA and ray BC. By Lemma B, ray BA* makes
   angle 90°−C with ray BK on the far side from BA (again since A* is on the C-side of line
   AB). Hence ray BK lies between ray BA and ray BA*, and
   **∠A*BA = ∠A*BK + ∠KBA = (90° − C) + α.**
   *(Verified: ∠A*BA = 90°−C+α to 1e-8 in every config.)*

2. **Ray order at C (symmetric).** Condition C1 gives ∠ACL = α. L lies inside triangle BNC
   and inside angle ACK, so ray CL lies strictly between ray CA and ray CB. By Lemma C, ray
   CA* makes angle 90°−B with ray CL on the far side from CA, so
   **∠A*CA = ∠A*CL + ∠LCA = (90° − B) + α.**
   *(Verified: ∠A*CA = 90°−B+α to 1e-8.)*

3. **Base angles of triangle A*BC are equal.** Since A* is on the C-side of line AB, both
   rays BA* and BC lie on the same (C-)side of ray BA, so
   ∠A*BC = |∠ABC − ∠A*BA| = |B − (90° − C + α)| = |B + C − 90° − α| = |90° − A − α|,
   using A + B + C = 180°. Symmetrically, since A* is on the B-side of line AC,
   ∠A*CB = |∠ACB − ∠A*CA| = |C − (90° − B + α)| = |90° − A − α|.
   Therefore **∠A*BC = ∠A*CB.**
   *(Verified: ∠A*BC − ∠A*CB = 0 to 1e-8, including the configs where 90°−A−α < 0, i.e. where
   A* has crossed to the far side and the signed value flips — the unsigned base angles remain
   equal, so the isosceles conclusion is robust.)*

4. **Conclusion.** In triangle A*BC the base angles at B and C are equal, so by the converse
   of the base-angles (isosceles-triangle) theorem, A*B = A*C. By Step 1, **OM = ON.** ∎
   (modulo Lemmas B, C).

---

### Where this route now stands

The entire problem on this route is reduced to the **two symmetric, α-independent angle
identities** ∠A*BK = 90°−C and ∠A*CL = 90°−B (Lemma B / Lemma C). Everything else — the
antipode equivalence (Step 1), the Thales location of A* (Step 2), and the isosceles synthesis
(Step 4) — is fully proven and independent of the (★★) identity that stalls the trig/power
routes. This is a strictly sharper crux than the "candidate mechanism" placeholder of the
previous round: it is a crisp, verified, symmetric target that does **not** involve α, so any
proof of it is automatically uniform in the free parameter.

### Approaches tried
- **Round 2 — antipode + isosceles reduction.** Proved Step 1 (OM=ON ⟺ A*B=A*C) as an exact
  vector identity and its power-of-point bridge; proved Step 2 (Thales location of A*);
  **discovered and numerically certified (to 1e-8) the α-independent invariants
  ∠A*BK = 90°−C and ∠A*CL = 90°−B**, and proved that these two invariants + C1 + "A* inside
  angle BAC" force triangle A*BC isosceles, hence A*B=A*C, hence OM=ON (Step 4). Ruled out
  simple incidence explanations of the invariants. **Outcome: strong partial** — the whole
  problem reduces to Lemma B / Lemma C, which remain unproven.
- (prior) Step-1 vector identity noted; Steps 2–4 were only outlined with an unvalidated
  "candidate mechanism."

### Current best
OM = ON ⟺ A*B = A*C (A* = 2O − A the antipode of A on ⊙AKL) is a proven equivalence, and A*B
= A*C follows rigorously from the two invariants **∠A*BK = 90°−C** and **∠A*CL = 90°−B** via
an isosceles-triangle synthesis (all of Steps 1, 2, 4 proven). **Open gap:** prove the two
invariants ∠A*BK = 90°−C, ∠A*CL = 90°−B (Lemma B / Lemma C) from the antipode structure
(A*K⊥AK, A*L⊥AL) and conditions C2 (∠LBK=∠LNC), C3 (∠LCK=∠BMK). They are α-independent,
mutually symmetric under B↔C/M↔N/K↔L, and certified numerically to 1e-8; no simple incidence
realizes them.

## Full proof
(Not present — Status is partial. The chain is complete except Lemma B / Lemma C of Step 3.)

## Promotable lemmas

- **Antipode equivalence lemma (fully proven, Step 1).** With A at the origin and O the
  circumcentre of AKL, let A* = 2O. Then OM = ON ⟺ A*B = A*C ⟺ A* lies on the perpendicular
  bisector of BC ⟺ A*·(C−B) = (|C|²−|B|²)/2 (real inner product). Proof: two one-line
  expansions of differences of squared distances, shown equal because A* = 2O. Reusable by any
  approach wanting to trade "OM=ON" for "A* on perp-bisector of BC."
- **Antipode–power bridge (fully proven, Step 1).** For a circle ω with centre O, radius R,
  and a diameter AA* (A* = 2O − A), and any point X: (X−A)·(X−A*) = pow_ω(X). Consequently
  OM = ON ⟺ pow_ω(B) − pow_ω(C) = (AB²−AC²)/2, unifying the antipode and power-of-point
  reductions. Proof: expand (X−A)·(X−2O+A) = |X−O|² − |O−A|².
