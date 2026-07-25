# Proof-reviewer report — imo-2026-02 (IMO 2026 P2), round 2

Two slugs reviewed. Verdicts: **coordinate-identity = APPROVE (solved)**;
**pow-reduction-trig = CHANGES REQUESTED (partial)**.

---

## SLUG 1 — coordinate-identity  ·  VERDICT: APPROVE  ·  Status: solved

Scores — Correctness 10/10 · Completeness/rigor 9.5/10 · Progress: closes the round-1 gap,
first full solve.

### The round-1 gap is genuinely closed (no numeric appeal)
Round 1 died on ONE overclaim: the directed equations FK=FL=0 were justified by numerics, not
proved from interiority (θ=0.8 counterexample where unsigned matched but OM≠ON). This round installs
a from-scratch, coordinate-free **Orientation Lemma** (`lemmas/orientation-sign.md`). I re-derived
every load-bearing step independently:

- **Lemma I (interior ⟹ positive barycentric):** signed-area barycentrics α+β+γ=1, strict interior
  ⟹ all three areas share sign of [VYZ] ⟹ β,γ>0. Correct standard fact.
- **Lemma B (betweenness sign):** bilinearity of cross. Correct.
- **Fact 0 (midpoint area-halving)** ⟹ the four fixed reference signs. Correct.
- **Four target signs**, each a Lemma I → Lemma B chain, checked by hand:
  * cross(BK,BL)<0: from K∈int△BMC (gives cross(BA,BK)<0) then K inside ∠LBA (transports to
    cross(BK,BL)<0). Correct, no circularity — cross(BA,BL)<0 is *derived*, not assumed.
  * cross(NC,NL)<0: L∈int△BNC, Lemma I at N. Correct.
  * cross(CL,CK)>0: L∈int△BNC (cross(CA,CL)>0) then L inside ∠ACK. Correct.
  * cross(MB,MK)>0: K∈int△BMC, Lemma I at M. Correct.
- **Condition-B pair NOT transported through σ.** The proof explicitly derives cross(CL,CK)>0,
  cross(MB,MK)>0 DIRECTLY at vertices C and M (σ is a reflection, orientation-reversing). No silent
  sign transport — the exact failure mode I flagged in round 1 is avoided.
- **Directed upgrade:** sign α = sign cross(BK,BL), |α|=unsigned angle in (0,π); two numbers in
  (−π,0) with equal magnitude are equal. I re-derived Im[z₂conj(z₁)]=cross(z₁,z₂); signs and
  magnitudes all match. Valid. This is a genuine proof, not a numeric assertion.

### Algebra re-verified from scratch (my own sympy, not the builder's scripts)
- EA = u·FL with FL a quadratic in **v only**; EB = v·FK with FK a quadratic in **u only**
  (decoupling). Confirmed.
- Leading coefficients (8): a_L−½(c²+s²)|CA|²W = 0 and a_K+½(c²+s²)|AB|²W = 0. Confirmed.
- **Ideal identity (9):** I did not merely rerun the builder's pseudo-division. I computed the
  normal form of T modulo ⟨FK,FL⟩ over the field ℚ(a,p,q,h,c,s) (reduce u²,v² via FK=FL=0). It is
  **identically 0** ⟹ T ∈ ⟨FK,FL⟩. So FK=FL=0 (with a_K·a_L≠0) forces T=0.

### The §6 exceptional set is empty (soft spot has no teeth)
The one thin argument is the continuity fallback for a_K·a_L=0 (i.e. W=0). I probed it: over 60,000
samples, **min|W| on the admissible set = 0.25** — bounded away from 0. So W=0 never occurs at an
admissible configuration; the continuity remark covers a non-occurring case and cannot introduce an
error. At every admissible config a_K·a_L≠0 and T=0 directly from (9).

### End-to-end sanity
Built 11,739 genuinely admissible configurations (interiority + both betweenness conditions solved
for positive roots of FK,FL): all four cross signs uniformly (−,−,+,+); the three unsigned
hypotheses hold to 1e-15; **OM=ON to max 1.9e-14**. The round-1 counterexample root fails
interiority, exactly as the Orientation Lemma predicts.

### Verdict
Complete and rigorous: certified reduction + proved orientation (no numerics) + verified decoupling
+ verified ideal identity + empty exceptional set ⟹ T=0 ⟹ OM=ON. The builder's Status=solved is
**correct**. Full proof written into `current.md`. Orientation Lemma **certified** in
`lemmas/orientation-sign.md`.

---

## SLUG 2 — pow-reduction-trig  ·  VERDICT: CHANGES REQUESTED  ·  Status: partial

Scores — Correctness 9/10 (what's written is exact) · Completeness 5/10 (real gap) · Progress: good.

- Lemmas 4–5 are **symbolic/exact**, as claimed: constraint normal form C1(γ) affine in
  (cos2γ,sin2γ) with C1−residual=0 verified symbolically; the cleared residual Ẽ is exactly bilinear
  in (cos2γ,sin2γ)×(cos2δ,sin2δ). This is genuine structural progress: the balance identity is
  reduced from a transcendental claim to a finite 3×3 bilinear-form membership.
- **Gap GAP-2′ remains and is honestly flagged:** the explicit cofactors f,g for Ẽ=f·C1+g·C2 were
  not extracted; consistency (rank-5=rank-5) is currently numeric-at-generic-point, not a
  from-scratch symbolic certificate. Per the run-state rule (no numeric-only load-bearing step) this
  is correctly NOT a solve. The builder's Status=partial is accurate — no overclaim.
- Independent framing (trig, not coordinate), so it remains valuable insurance and can now import the
  certified Orientation Lemma for its sign steps.

Next round: extract f,g explicitly (report's finish (a): factor M = c1·aᵀ + b·c2ᵀ), then verify
Ẽ−f·C1−g·C2 ≡ 0 mod sin²+cos²=1. One small linear-algebra computation from a second full solve.

---

## Certification actions
- `lemmas/orientation-sign.md` — **CERTIFIED** (header updated). Held to full bar; every load-bearing
  step re-derived, no numeric/continuity dependence. Importable by synthetic-sigma-spiral.
- `lemmas/reduction-OMeqON.md` — already certified (round 1); used correctly in §1.
- Decoupling lemma (FL v-only, FK u-only) — verified correct; lives inside coordinate-identity §4.
