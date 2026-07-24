## imo-2026-02

Opening the field (round 1, empty population). Three rival attempts at the whole claim
`OM = ON`, deliberately FAR APART in framing so they do not share one wall:
(1) brute metric identity, (2) synthetic symmetry+spiral, (3) power-of-a-point.
All three adopt the free reduction `OM=ON ⟺ OB²−OC²=(AB²−AC²)/2 ⟺ O∈perp-bisector(MN)`
(explorer-verified) but diverge completely on the engine that proves it.

Shared verified facts (grounding, re-checked numerically this round):
- `OM=ON`, `pow_M(⊙AKL)=pow_N(⊙AKL)`, and `OB²−OC²=(AB²−AC²)/2` all hold to 1e-15.
- Hypotheses are invariant under the formal involution `σ:(B↔C, M↔N, K↔L, A↦A)`:
  condition 1 is σ-fixed, conditions 2 and 3 swap into each other (hand-derived,
  directed angles). This is the deepest structural clue; approach 2 is built on it.
- Ruled OUT for all: `AK=AL`, `∠BAK=∠CAL`, spiral-sim centred at A, concyclicity of
  {A,K,L,B,C}, `BK` tangent to ⊙AKL, constant ratios `AK/AB`. Any approach hitting one
  of these is over-specifying the 1-parameter family and is wrong.

---

trig-metric-identity: new
Target: `OM = ON` (whole claim), for the entire 1-parameter family.
Technique: direct computation — law of sines / trig to pin triangle AKL in the free
parameter θ=∠KBA=∠ACL, then verify `AO·BC = (AC²−AB²)/4` as an identity in θ.
Skeleton:
  1. Goal reduction `OM=ON ⟺ OB²−OC²=(AB²−AC²)/2` — vector algebra, A as origin.
  2. Parametrize family by θ; K,L on rotated rays at B,C with free radii r_K,r_L.
  3. Law of sines in △ABK, △ACL → AK, AL, base angles in θ,r_K,r_L.
  4. Conditions ∠LBK=∠LNC, ∠LCK=∠BMK → 2×2 system solved for r_K(θ),r_L(θ)
     (using ∠LCN=θ, NC=b/2 in △LNC; ∠MBK=θ, MB=c/2 in △BMK).
  5. Circumcenter O of AKL; extract projection AO·(C−B).
  6. Show `AO·(C−B) − (b²−c²)/4 ≡ 0` in θ — the crux identity.
Key lemmas: L1 goal reduction (telescoping midpoint vector identity); L2 unique
positive (r_K,r_L) per θ by monotonicity; L3 the θ-identity collapses via sine-rule
product-to-sum cancellation.
Open gaps: GAP-A closed-form r_K(θ),r_L(θ); GAP-B the identity vanishes (fallback:
exact symbolic sympy verification with A,B,C symbolic and θ a symbol — legitimate,
certifies the whole family).
Cases to cover: scalene (main); isosceles consistency; correct angle branches from
the region hypotheses.
Watch out for: angle sign/branch (that is what the containment hypotheses fix); do NOT
lean on any of the ruled-out symmetry shortcuts.

spiral-involution: new
Target: `OM = ON` (whole claim).
Technique: pure synthetic — the formal involution σ + two spiral similarities read off
conditions 2,3, forcing O onto the σ-fixed line perp-bisector(MN). Never solves for K,L,
so the free parameter never appears.
Skeleton:
  1. Prove σ:(B↔C,M↔N,K↔L) maps the hypothesis set to itself (cond 1 fixed, 2↔3).
  2. Angle-sum identities: `∠LBA=∠ACL+∠LNC`, giving `∠LBA+∠NLC=π` (via △LNC);
     σ-image `∠KCA+∠MKB=π`.
  3. Read condition 3 as base-angle equality of spiral sim S_K (K: L↦B, C↦M); cond 2
     as its σ-image S_L (L: K↦C, B↦N). Upgrade each to a GENUINE spiral similarity
     using the Step-2 supplementary relation for the second angle.
  4. Miquel/second-intersection concyclicities from S_K, S_L involving M (line AB),
     N (line AC).
  5. `pow_M(⊙AKL)=pow_N(⊙AKL)` by σ-conjugacy of the two secant products ⇒ OM=ON.
Key lemmas: L1 σ-invariance (directed-angle relabel); L2 `∠LBA+∠NLC=π`; L3 upgrade to
genuine spiral similarity (HARD); L4 equal σ-conjugate powers.
Open gaps: GAP-1 (crux) — is one base-angle equality + Step-2 enough for a GENUINE
spiral similarity (need the second angle or the ratio KL/KC=KB/KM)? Explorers warn one
angle alone is insufficient; if L2 does not supply the second, this route may be a true
dead end → RETHINK. GAP-2 the power computation from the concyclicities.
Cases to cover: scalene (main); isosceles (σ becomes literal reflection — check only).
Watch out for: σ is FORMAL, not an isometry when AB≠AC — it licenses "prove one side,
relabel for the other," not "O fixed by reflection." Operative spirals are at K,L NOT A.

equal-power-secants: new
Target: `OM = ON` (whole claim).
Technique: power of a point / radical axis — recast as `pow_M(⊙AKL)=pow_N(⊙AKL)`
(verified 1e-15 this round) and compute each power along a secant through M / N whose
second intersection is controlled by the angle conditions. Never computes O.
Skeleton:
  1. `OM=ON ⟺ pow_M=pow_N` (both = OX²−R²).
  2. Pick secants: (a) lines AB,AC through A (second pts P,Q; goal AB·MP=AC·NQ), or
     (b) lines MK, NL through K,L∈⊙AKL.
  3. Inscribed-angle translation: ∠BMK=∠LCK ties the direction of secant MK at M to
     an inscribed angle at C subtending chord KL on ⊙AKL, controlling the 2nd
     intersection; σ-symmetrically ∠LNC=∠LBK controls the N-side secant.
  4. Equal-product identity using MA=AB/2, NA=AC/2 and condition 1 ⇒ pow_M=pow_N.
Key lemmas: L1 power reformulation (trivial, the framing); L2 second-intersection
control via inscribed angle (HARD — bridge "direction at M" ↔ "inscribed angle at C"
on the same circle); L3 equal products.
Open gaps: GAP-1 (crux) make L2 precise — pin the second intersection as an explicit
arc/inscribed-angle relation. GAP-2 signed-length equal-product algebra.
Cases to cover: scalene (main); isosceles; sign of power (M,N inside vs outside ⊙AKL)
handled by signed lengths, not case-split.
Watch out for: B,C are NOT on ⊙AKL and no secant is a tangent (both explorer-refuted);
B,C only fix secant directions. Keep every length signed.

Registration note: the ranker `register_approach` is outline-reviewer-owned and not in
the outliner toolset — the three new slugs above need registering by the reviewer.

field: trig-metric-identity, spiral-involution, equal-power-secants (all NEW this round)
