# Approach: midpoint-reflection-isogonal

## Status
partial

## Approaches tried
- (round 1, outliner) Naive synthetic objects in the reflected picture — REFUTED
  numerically: {A,K,L,K\*}, {A,K,L,L\*}, {K,L,K\*,L\*}, {B,C,K\*,L\*} not concyclic;
  ⊙(AK\*L\*) does not have the OM = ON property; AK·CL ≠ AL·BK.
- (round 1, builder; probe `/tmp/round-1/scratch/builder_mri_probe.py`, two
  unrelated scalene triangles, two φ each) **Candidate Γ₁ = circle through K\*
  tangent to AB at M, Γ₂ = circle through L\* tangent to AC at N — REFUTED as
  carriers of the identity.** None of L\*, K, L, C, N, P, P₁ lies on Γ₁ (deviations
  O(1)); symmetrically for Γ₂. Γ₁, Γ₂ are not orthogonal to ω; their radical axis
  passes through none of A, O, mid(MN), K, L, K\*, L\*; centers O, O₁, O₂ not
  collinear; R₁ ≠ R₂. Only trivial facts hold: pow(A,Γ₁) = AM² = c²/4 and
  pow(B,Γ₁) = BM² = c²/4 (immediate from tangency of line AB at M — content-free).
- (round 1, builder, same probe) **Candidate Γ₁ᵇ = circle through K tangent to AB
  at M (tangent–chord reading of ∠BMK), Γ₂ᵇ = circle through L tangent to AC at N
  — REFUTED.** B, C, K, L, K\*, L\*, P₁, P₂ memberships all fail; no orthogonality
  to ω; radical axis hits nothing tested.
- (round 1, builder, same probe) **Spiral-similarity candidates at A — REFUTED.**
  The spiral at A carrying K\* ↦ L\* does not carry B ↦ C (b·BK ≠ c·CL); also
  AK\*·AP₁ ≠ AL\*·AP₂, AK\*/AK ≠ AL\*/AL, AP₁ ≠ AP₂, AK\*·AK ≠ AL\*·AL, and
  BK·CL ≠ AK·AL. P₁ ∉ {Q, L}, P₂ ∉ {P, K} (distances O(1)).
- (round 1, builder; probe `/tmp/round-1/scratch/builder_mri_probe2.py`) **More
  candidates — REFUTED:** with K₂, L₂ the second meets of lines KK\* (= KM) and
  LL\* (= LN) with ω: K₂ ∉ {L, Q, P₂}, L₂ ∉ {K, P, P₁}; K₂, L₂, A not collinear;
  K₂L₂ not parallel to MN; KL₂ ≠ LK₂ (deviation ~1e-3 ≫ solver precision 1e-13 —
  a near-miss, not a theorem). Lines K\*L\* have NO fixed point as φ varies
  (pairwise intersections spread over O(10²)); same for lines KL.
- (round 1, builder) **True but content-free observation:** chord P₁Q = chord PP₂
  holds exactly — but it is automatic from isogonality: ∠P₁AQ = ∠A − φ = ∠PAP₂
  are equal inscribed angles in ω, hence equal chords. Carries no information
  about the hypotheses at M, N.
- (round 1, builder) **Rigorous reduction completed** (Lemmas 1–4 below): the
  reflection dictionary and the equivalence OM = ON ⟺ boxed identity (I) are now
  fully proved with directed lengths — worked; this is the approach's certified
  trunk. The remaining gap is deriving (I) from the two transferred angle
  conditions.

## Current best

Lemmas 1–4 below are proved rigorously (directed-length safe, no configuration
hand-waving). They reduce the problem, exactly and unconditionally, to:

> **(I)  BK·AP₁ + AK² − CL·AP₂ − AL² = (c² − b²)/2,**

where P₁, P₂ are the second meets of rays AK\*, AL\* with ω = ⊙(AKL) and AP₁, AP₂
are directed lengths along those rays. (I) is verified numerically to machine
precision on two unrelated scalene triangles across the φ-family.

**Open gap (load-bearing):** derive (I) from the two transferred hypotheses
∠AMK\* = ∠LCK and ∠ANL\* = ∠LBK. Every natural synthetic carrier tested so far is
refuted (see Approaches tried) — the bounded candidate hunt mandated by the
round-1 outline review came back empty. Per the review, this approach does NOT
fall back to the trig elimination (that is the sibling `secant-trig-identity`);
if the sibling's identity closes, this file's Lemmas 1–4 give an independent,
fully synthetic reduction whose endpoint identity is equivalent to the sibling's.

---

## Setup and notation

Triangle ABC with M, N the midpoints of AB, AC; write b = CA, c = AB,
∠A = ∠BAC. K lies in the interior of triangle BMC, L in the interior of triangle
BNC, K inside ∠LBA and L inside ∠ACK, with

- (H1) ∠KBA = ∠ACL =: φ,
- (H2) ∠LBK = ∠LNC,
- (H3) ∠LCK = ∠BMK.

ω = ⊙(AKL) with centre O and radius R; A, K, L are not collinear (else O is
undefined), so ω exists. Define the point reflections

- K\* := 2M − K (reflection of K in M),  L\* := 2N − L (reflection of L in N).

All angles ∠XYZ are unsigned angles in (0, π) unless stated otherwise; directed
lengths are used only where explicitly declared, along a fixed oriented line.

## Lemma 1 (reflection dictionary)

**(a)** AKBK\* and ALCL\* are parallelograms; in particular AK\* = BK,
AK\* ∥ BK, AL\* = CL, AL\* ∥ CL.

**(b)** ∠K\*AB = ∠KBA = φ and ∠L\*AC = ∠ACL = φ, and K\* lies strictly on the
opposite side of line AB from C, L\* strictly on the opposite side of line AC
from B. Thus AK\* and AL\* form an isogonal pair of rays exterior to ∠A: the four
rays AK\*, AB, AC, AL\* are symmetric in pairs about the internal bisector of ∠A,
with ∠K\*AL\* = ∠A + 2φ.

**(c)** ∠AMK\* = ∠BMK = ∠LCK and ∠ANL\* = ∠CNL = ∠LBK.

*Proof.* (a) An interior point of a triangle lies on none of its three side
lines. Line AB is the side line BM of triangle BMC (it contains the two vertices
B and M), so K ∉ AB; likewise line AC is the side line NC of triangle BNC, so
L ∉ AC. In particular A, K, B are not collinear. M is the midpoint of AB by
hypothesis and of KK\* by construction of K\*, so the (non-degenerate)
quadrilateral AKBK\* has diagonals AB and KK\* bisecting each other, and a
quadrilateral with mutually bisecting diagonals is a parallelogram. Hence
opposite sides satisfy AK\* = KB, AK\* ∥ KB and AK = K\*B. Identically ALCL\* is
a parallelogram with AL\* = LC, AL\* ∥ LC, AL = L\*C.

(b) By definition of K\*,
K\* − A = 2M − K − A = (A + B) − K − A = B − K. Hence ∠K\*AB, the unsigned angle
between the vectors K\* − A = B − K and B − A, equals the unsigned angle between
the vectors −(B − K) = K − B and −(B − A) = A − B (the angle between two vectors
is unchanged when both are negated), and that is exactly ∠KBA = φ. Likewise
L\* − A = C − L gives ∠L\*AC = ∠ACL = φ.

Side of the line: K lies strictly on the C-side of line AB (interior of BMC).
The point reflection σ_M fixes line AB (as M ∈ AB) and is a homeomorphism of the
plane mapping each open half-plane bounded by AB onto the other; hence
K\* = σ_M(K) lies strictly on the non-C side of AB. Same for L\* about AC. The
isogonality statement is then immediate: ray AK\* makes angle φ with ray AB on
the outside of the triangle at AB, ray AL\* makes angle φ with ray AC on the
outside at AC, so both are obtained from the sides of ∠A by reflecting the pair
(interior cevian directions) outward symmetrically; ∠K\*AL\* = φ + ∠A + φ.

(c) σ_M maps ray MA onto ray MB (both are the two rays of line AB from M, and
σ_M swaps A and B) and maps ray MK\* onto ray MK (σ_M swaps K and K\*, fixes M).
A point reflection is an isometry, so it preserves unsigned angles:
∠AMK\* = ∠(σ_M(MA), σ_M(MK\*)) = ∠BMK. By (H3), ∠BMK = ∠LCK. Identically at N:
∠ANL\* = ∠CNL = ∠LNC = ∠LBK by (H2). ∎

**Transferred problem.** By Lemma 1 the hypotheses are equivalent to: K\*, L\* on
the exterior isogonal rays at A (angle φ each, per (b)), with K = 2M − K\*,
L = 2N − L\*, subject to the two coupling conditions ∠AMK\* = ∠LCK and
∠ANL\* = ∠LBK.

## Lemma 2 (median formula reduction)

OM = ON ⟺ pow(K\*, ω) − KK\*²/2 = pow(L\*, ω) − LL\*²/2.

*Proof.* For any points O, K, K\* with M the midpoint of KK\*, writing vectors
from O: OK = OM + MK and OK\* = OM + MK\* = OM − MK, so
OK² + OK\*² = 2·OM² + 2·MK² = 2·OM² + KK\*²/2 (Apollonius' median formula, here
proved as a two-line vector identity; KK\* = 2·MK). Since K ∈ ω, OK = R, so
OM² = (R² + OK\*²)/2 − KK\*²/4; and by definition pow(K\*, ω) = OK\*² − R², i.e.
OK\*² = R² + pow(K\*, ω), whence

  OM² = R² + pow(K\*, ω)/2 − KK\*²/4.

The same computation at N (L ∈ ω, N midpoint of LL\*) gives
ON² = R² + pow(L\*, ω)/2 − LL\*²/4. Subtracting, OM² − ON² =
(pow(K\*,ω) − KK\*²/2 − pow(L\*,ω) + LL\*²/2)/2, and OM, ON ≥ 0, so OM = ON is
equivalent to the stated identity. ∎

## Lemma 3 (parallelogram law)

KK\*² = 2AK² + 2BK² − c²  and  LL\*² = 2AL² + 2CL² − b².

*Proof.* Set u = A − K, v = B − K. Then K\* = A + B − K gives
K\* − K = u + v and B − A = v − u, so
KK\*² + AB² = |u+v|² + |v−u|² = 2|u|² + 2|v|² = 2AK² + 2BK², i.e.
KK\*² = 2AK² + 2BK² − c². (This is the parallelogram law for AKBK\*: the sum of
the squares of the diagonals equals the sum of the squares of the four sides.)
Identically for ALCL\* with A − L, C − L and CA = b. ∎

## Lemma 4 (power along the isogonal secants; the boxed identity)

Orient the line AK\* positively from A towards K\* and let P₁ be the second
intersection point of line AK\* with ω (P₁ = A if the line is tangent at A), with
AP₁ the **directed** length. Define P₂ and AP₂ likewise on line AL\*. Then

  pow(K\*, ω) = BK² − BK·AP₁,  pow(L\*, ω) = CL² − CL·AP₂,

and consequently, combining with Lemmas 2 and 3:

  **OM = ON ⟺ BK·AP₁ + AK² − CL·AP₂ − AL² = (c² − b²)/2.  (I)**

*Proof.* K\* ≠ A because AK\* = BK > 0 (K is interior to triangle BMC, hence
K ≠ B). The line through K\* and A meets ω at A and at one further point P₁
(counted with tangency: if the line is tangent to ω at A, set P₁ = A). By the
power of a point along a secant (directed form; knowledge_base.md, power of a
point): for any line through K\* meeting ω at points U, V,
pow(K\*, ω) = →K\*U · →K\*V as a product of directed lengths, independent of the
line. With U = A, V = P₁ and the chosen orientation, →K\*A = −AK\* = −BK and
→K\*P₁ = →K\*A + →AP₁ = −BK + AP₁. Hence

  pow(K\*, ω) = (−BK)(−BK + AP₁) = BK² − BK·AP₁,

valid in all positions of P₁ (including the tangent case AP₁ = 0, where
pow(K\*,ω) = K\*A² holds since the tangent length from K\* along this line is
K\*A). Identically pow(L\*, ω) = CL² − CL·AP₂.

Substitute this and Lemma 3 into Lemma 2:

  BK² − BK·AP₁ − (2AK² + 2BK² − c²)/2 = CL² − CL·AP₂ − (2AL² + 2CL² − b²)/2.

The left side simplifies: BK² − BK·AP₁ − AK² − BK² + c²/2 =
−BK·AP₁ − AK² + c²/2; the right side likewise equals −CL·AP₂ − AL² + b²/2.
Multiplying by −1 and rearranging gives exactly (I). ∎

**Remark (orientation of P₁, P₂ in the valid configuration).** Numerically, in
every valid configuration probed, P₁ and P₂ lie on the rays AK\*, AL\* themselves
(AP₁, AP₂ > 0), and (I) holds with ordinary lengths; but Lemma 4 as stated needs
no such case analysis — the directed form is unconditional.

**Remark (equivalent forms of the goal).** pow(M, ω) = OM² − R² and
pow(N, ω) = ON² − R², so the target is also equivalent to
pow(M, ω) = pow(N, ω); and since line MN ∥ BC meets ω in a chord XY (when it
does), the target says M and N are symmetric about the midpoint of the chord XY.
These restatements were checked numerically and are trivially equivalent — they
are recorded for the next candidate hunt, not as progress.

## Step 5 — the open gap

**Gap:** prove identity (I) from the transferred hypotheses of Lemma 1, i.e.
from: K\*, L\* on the exterior isogonal rays at A with ∠K\*AB = ∠L\*AC = φ, and
∠AMK\* = ∠LCK, ∠ANL\* = ∠LBK (K = 2M − K\*, L = 2N − L\*).

State of the hunt for the synthetic carrier (all numerical, two unrelated
scalene triangles, machine precision — see Approaches tried for the full list):
tangent circles at M/N through K\*, L\* or K, L — refuted; spiral similarity at A
pairing the isogonal chords — refuted in every tested ratio form; second
intersections K₂, L₂ of lines KM, LN with ω — no incidence found; no fixed point
on lines K\*L\* or KL across the φ-family. The equal-chord relation P₁Q = PP₂ is
exact but is a consequence of isogonality alone (equal inscribed angles
∠P₁AQ = ∠PAP₂ = ∠A − φ) and carries none of the M/N-hypothesis content.

What remains untried within this framing (next-round leads, in decreasing
promise):
1. Read ∠AMK\* = ∠LCK as a **directed** angle equality and hunt for the carrier
   in the *directed* category (a circle through K\* and C, or through M and the
   intersection point line MK\* ∩ line CL); unsigned probes can miss a directed
   coincidence only if a reflection intervenes — low probability but cheap.
2. Trig form of the transferred conditions: in triangle AMK\*, by the law of
   sines AK\*/sin∠AMK\* = AM/sin∠AK\*M with AM = c/2 and ∠MAK\* = φ (Lemma 1b —
   note ray AM = ray AB). So sin∠AMK\* = AK\*·sin(φ + ∠AMK\*)/(c/2)-type relations
   reproduce exactly the sibling's E3 with the factor 2 from AM = c/2. Grinding
   this out IS the sibling approach (`secant-trig-identity`) — per the round-1
   review this file must not duplicate it; if the sibling closes, prune this
   slug or keep Lemmas 1–4 as its synthetic preamble.
3. Inversion at A (radius √(AK·AP₁)-type) swapping K ↔ P₁-related points: not
   yet probed; an inversion at A maps ω to a line and the isogonal rays to
   themselves, so (I) becomes a statement about distances to a line — one more
   bounded numeric probe next round before any proof effort.

## Cases to cover
None in Lemmas 1–4 (all proofs are directed-length/vector identities plus the
two non-collinearity facts K ∉ AB, L ∉ AC established in Lemma 1a). All
configuration content is concentrated in the open Step 5.

## Watch out for
- The refuted list above — do not rebuild on any of it.
- K\* is on the non-C side of AB, L\* on the non-B side of AC (Lemma 1b); any
  future tangent–chord or inscribed-angle reading at M or N must check the arc
  side against this.
- ∠ANL\* = ∠LBK pairs an angle at N with an angle at B; any cyclic reading must
  use exactly these vertices.
- AP₁, AP₂ in (I) are directed; keep them directed until a final configuration
  argument pins their signs.

## Promotable lemmas
- **Reflection reduction for imo-2026-02** (Lemmas 1–4 above, proved in full in
  this file): with K\* = 2M − K, L\* = 2N − L, one has AK\* = BK, AL\* = CL,
  ∠K\*AB = ∠L\*AC = φ (exterior isogonal rays), ∠AMK\* = ∠BMK, ∠ANL\* = ∠CNL,
  and OM = ON ⟺ BK·AP₁ + AK² − CL·AP₂ − AL² = (c² − b²)/2 with AP₁, AP₂ the
  directed second-intersection abscissae of rays AK\*, AL\* with ω = ⊙(AKL).
  Reusable by any approach wanting a midpoint-free restatement of the goal.
