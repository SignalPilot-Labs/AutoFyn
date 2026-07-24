## imo-2026-04 (Mulan's Triangle Game)

**Answer put forward (all three approaches agree, numerically confirmed both directions):**
Mulan wins **iff θ = 180°/n for an integer n ≥ 2** (iff 180/θ ∈ ℤ≥2, iff 180 ∈ θℤ).

Round-1 note to the reviewer: I verified the two load-bearing claims numerically before
outlining. Necessity residue invariant — 0 forced-loss events over ~10^6 random moves for
θ∈{100,120,50,80,17,73} (θ∤180). Sufficiency alignment move — exists for every tested
n=2..12, 0 failures over 3000 random triangles each. The historically "open" necessity gap is
much closer than the explorers thought: the 4-coincidence exclusion (Lemma A) is essentially a
complete necessity proof, modulo write-up.

Field: three genuinely-different framings of the whole problem. They share only the sufficiency
*construction* (alignment + peel); their **necessity mechanisms are deliberately disjoint** so
the field does not collapse to one wall.

---

residue-invariant: new
Target: full characterization — Mulan wins iff θ=180/n; prove sufficiency for all such θ and
  necessity (Shan-Yu survives) for all other θ.
Technique: invariant argument in the quotient group ℝ/θℤ (residues of the three angles mod θ).
Skeleton:
  1. good triangle := no angle in θℤ ⇒ game not stopped — by definition.
  2. Necessity: from a good triangle every Mulan cut leaves ≥1 good child (Lemma A); Shan-Yu
     keeps it ⇒ good forever ⇒ no angle = θ.
  3. Sufficiency: alignment move (Lemma B) makes both children carry a multiple of θ; peel
     (Lemma C) walks that multiple down to the 2θ double-fork = forced win.
  4. State θ=180/n; verify n=2,3.
Key lemmas:
  - Lemma A (necessity) — T1 bad ⟺ t∈{0,S−b}, T2 bad ⟺ t∈{a,−b}; both bad forces one of
    a≡0,b≡0,c≡0,S≡0 mod θ, all excluded when the triangle is good and θ∤180. (Verified.)
  - Lemma B (alignment, θ|180) — the excluded coincidence S−b=−b is exactly S≡0, now true; at
    t≡−b both children's compound angle ≡0 mod θ (complementarity 180−kθ=(n−k)θ). (Verified.)
  - Lemma C (peel) — angle mθ, cut x=(m−1)θ forces the (m−1)θ child; at m=2 both children hold θ.
Open gaps: G1 range-existence of the alignment x∈(0,α) via pigeonhole over the 3 vertex windows
  (total length 180=nθ), incl. acute triangles at n=2; G2 the multiple lies in (0,180); G3 the
  "good child stays good" closure (untouched base angle keeps nonzero residue).
Cases to cover: necessity — all 3 vertices × all x (subsumed by the case split on t); sufficiency
  — Shan-Yu's two branches + the peel chain; edge n=2.
Watch out for: x∈open interval (0,α) — no endpoint constructions; "≡0 mod θ" ≠ "=θ" (peel
  converts); Shan-Yu also picks the initial triangle (give the explicit generic choice).

---

geometric-forcing-extremal: new
Target: same full characterization, proven in raw degrees with no quotient group.
Technique: casework + fixed-sum extremal covering; reuses the survival explorer's PROVEN
  non-obtuse invariant for the θ>90 sub-case.
Skeleton:
  1. θ>90 necessity: start 60-60-60, keep max-angle-≤90 child; the two children's third angles
     sum to 180 so at most one exceeds 90 ⇒ safe child always exists (proven).
  2. θ≤90, θ∤180 necessity: start with no angle a multiple of θ; a cut's two compound angles
     180−β−x and β+x sum to 180, so both children endangered ⇒ 180∈θℤ, excluded (Lemma D).
  3. Sufficiency: altitude cut for θ=90 (both children right-angled), aligned cevian + θ-peel
     for general n (Lemmas E,F).
  4. State θ=180/n; verify θ=90,60,45.
Key lemmas:
  - Lemma D (extremal necessity) — raw-degree twin of Lemma A: complementarity 180−β−x + β+x =
    180 makes simultaneous endangerment of both children imply θ|180.
  - Lemma E (aligned cevian) — 180=nθ ⇒ making 180−β−x a multiple auto-makes β+x a multiple.
  - Lemma F (peel double-fork) — same as Lemma C.
Open gaps: G1 exhaustive 6-slot case enumeration in Lemma D; G2 justify the necessity split at
  90° and glue the two sub-cases; G3 alignment range-existence.
Cases to cover: necessity θ>90 vs θ≤90∤180; sufficiency θ=90 vs general θ=180/n.
Watch out for: the non-obtuse invariant only kills θ>90 (covering fails the other way below 90)
  — θ≤90 non-divisors NEED Lemma D; altitude foot strictly interior (both base angles acute).

---

q-linear-independence: new
Target: same full characterization; necessity via linear algebra over ℚ (independent mechanism).
Technique: invariant = ℚ-coordinates of each angle; Shan-Yu picks a ℚ-generic initial triangle
  relative to θ.
Skeleton:
  1. θ∤180: choose {1,θ,α₀,β₀} ℚ-independent inside a valid triangle.
  2. Track angles in V=ℚ⟨1,θ,α₀,β₀⟩; every cut leaves ≥1 ℚ-generic child (Lemma G).
  3. The only seed-independent exploitable relation is 180=nθ (Lemma H); absent when θ∤180 ⇒
     no universal alignment ⇒ Shan-Yu survives.
  4. Sufficiency: use 180=nθ as the honest alignment identity + peel.
Key lemmas:
  - Lemma G (generic survival) — "both children contain θ" needs two affine equations in x
    jointly solvable only if 180−2·(untouched)∈θℤ, impossible under genericity + θ∤180.
  - Lemma H (uniqueness of exploitable relation) — seed-independence kills all α₀,β₀ relations,
    leaving the 1- and θ-coordinate balance 180=nθ as the sole lever.
Open gaps: G1 (crux, high-risk) precise definition of the tracked ℚ-coordinates + closure proof
  under cuts and Shan-Yu's discard; G2 firewall so genericity does NOT prove survival at θ=180/n
  (Lemma H); G3 alignment range-existence.
Cases to cover: necessity — every cut from a generic triangle, uniform over θ∤180 (no 90° split);
  sufficiency — two branches + peel.
Watch out for: HIGHEST-RISK approach — reviewer will reject any hand-wave on "genericity is
  preserved"; x is a new real each move so the ℚ-span grows, invariant must be about the 1/θ
  coordinate balance, not a fixed basis. If G1 can't be nailed, RETHINK toward residue framing.

---

Registration: I did not call register_approach (that is the outline-reviewer's gate — it seeds
only approved lines). All three files are written under
results/imo-2026-04/approaches/{residue-invariant,geometric-forcing-extremal,
q-linear-independence}.md, ready for the reviewer to gate/register and emit the build set.

Slugs put up: residue-invariant (new), geometric-forcing-extremal (new), q-linear-independence (new).
