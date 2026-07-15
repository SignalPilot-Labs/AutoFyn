# Proof-outliner report — round 1

## imo-2026-02

Field of 4 new rival approaches, all files written under `results/imo-2026-02/approaches/`. Key round-1 discoveries (all numerically verified this round, two identities also CAS-certified):

1. **Decoupling.** With α = ∠KBA = ∠ACL, β = ∠LBK = ∠LNC, γ = ∠LCK = ∠BMK, the three hypothesis equalities split into two *independent* one-sided constraints: a quadratic q_K(τ) = 0 in τ = cot(α+γ) involving only (α, angles A, C), and its exact B↔C mirror q_L(σ) = 0 in σ = cot(α+β). K and L have explicit closed forms: K = (c/2)(cos α − τ sin α)e^{i(B−α)}, L = C + (b/2)(cos α − σ sin α)e^{i(π−C+α)}.
2. **Fixed point.** There is an explicitly computable point T (two linear equations, closed form) such that the power-expression E(T;τ) equals m·q_K(τ) *identically in τ* — so T lies on the perpendicular bisector of AK for every admissible configuration; by mirror symmetry T also lies on the perpendicular bisector of AL; hence O = T. Two trig identities (sympy-certified: simplify → 0) give T_x = midpoint(MN)_x and the B↔C symmetry. Verified: T = O to 1e-15 across triangles and α; moreover OM = ON holds even at the *spurious* roots of the quadratics, and all four root combinations give the SAME O = T.
3. **Reformulation.** OM = ON ⟺ A, K, L, W concyclic, where W = (perp bisector of BC) ∩ (parallel to BC through A) — because the perp bisector of AW *is* the perp bisector of MN. Also verified: ∠AKW = ∠ALW exactly.

---

fixed-point-t: new
Target: OM = ON (the full claim), end to end.
Technique: complex/trig coordinates + explicit fixed point on a pencil of perpendicular bisectors (no solving for O; T is constructed and shown to lie on both perpendicular bisectors, forcing O = T).
Skeleton:
  1. Angle bookkeeping (∠LBA = α+β, ∠ACK = α+γ, ray directions, positivity) — by the interiority hypotheses.
  2. Parametrization Lemma: BK = (c/2)sin γ/sin(α+γ), K = (c/2)(cos α − τ sin α)e^{i(B−α)}; mirrored L — by sine rule in BMK / CNL.
  3. Constraint Lemma: q_K(τ) = 0, q_L(σ) = 0 (decoupled quadratics) — by equating BK from triangles BMK and BKC, product-to-sum, cot-substitution.
  4. Fixed Point Lemma: explicit T with E(T;τ) ≡ m·q_K(τ) ⟹ T on perp bisector of AK — because E is quadratic in τ with constant leading coefficient, so matching to m·q_K is two linear conditions defining T.
  5. Mirror: T' on perp bisector of AL — same computation with B↔C.
  6. Claims A & B: T_x = (2A_x+B_x+C_x)/4 and T = T' — pure trig identities in (α,B,C), CAS-certified, hand proofs pending.
  7. O = T (two distinct perpendicular bisectors share T and O) ⟹ O on perp bisector of MN ⟹ OM = ON.
Key lemmas (claim + mechanism): see approach file; all mechanisms named and verified.
Open gaps: prose rigor of steps 1, 3, 4; hand proofs of Claims A/B; K ≠ L nondegeneracy.
Cases to cover: none beyond configuration checks (α+γ = π/2, isosceles, sin(A+α) ≠ 0 — all benign).
Watch out for: orientation/sign conventions in e^{i(B−α)}; builders must numerically re-verify each displayed formula.

quadratic-ideal-certificate: new
Target: OM = ON (the full claim), end to end.
Technique: same parametrization, brute algebraic finish — OM = ON ⟺ 3×3 determinant Δ(τ,σ) = 0, and Δ = G·q_K + H·q_L (polynomial ideal-membership certificate, bidegree (2,2)).
Skeleton:
  1–3. Shared with fixed-point-t (prove once, certify in lemmas/).
  4. Determinant reduction: OM = ON ⟺ O_x = x₀ ⟺ Δ = 0 — by consistency of three linear equations in O (needs A,K,L non-collinear, given).
  5. Certificate Δ = G·q_K + H·q_L — by polynomial division; existence guaranteed (Δ vanishes at ALL four root pairs, verified at 40 digits); exact cofactors to be produced.
  6. Conclude.
Open gaps: exact-arithmetic cofactors displayed in human-checkable form.
Cases to cover: none.
Watch out for: float contamination in CAS; unreadably large expansions (organize by factored sub-identities).

concyclic-with-w: new
Target: OM = ON (the full claim), end to end.
Technique: reformulation to the concyclicity A, K, L, W (W = perp bisector of BC ∩ parallel to BC through A), then decoupled equal-angle claim ∠AKW = ∠ALW via resultant symmetry or direct angle chase.
Skeleton:
  1. Reformulation Lemma: perp bisector of AW = perp bisector of MN, so OM = ON ⟺ AKLW concyclic — by reflection of A in that line.
  2. Concyclicity ⟺ ∠AKW = ∠ALW (same side of AW).
  3. K-side eliminant: tan∠AKW satisfies an explicit quadratic Φ(t; α,B,C) = 0 — by resultant of q_K with the tangent formula; claim: Φ is B↔C symmetric, so tan∠ALW satisfies the same Φ.
  4. Root selection — by continuity from the limit K→M, L→N where (AKL)→(AMN) ∋ W (homothety at A, ratio 1/2, of the circumcircle fact that the reflection of A in the perp bisector of BC lies on (ABC)).
  5. Conclude.
Open gaps: resultant symmetry (mechanical), root selection (real content). Highest upside for a short synthetic proof; also the natural place to hunt a pure angle chase.
Watch out for: silently assuming the root pairing — that is the gap.

power-point-trig: new
Target: OM = ON (the full claim), end to end.
Technique: power of a point, coordinate-free trig: OM = ON ⟺ pow(B) − pow(C) = (c²−b²)/2 (midpoint power formula), reduced via second intersections and product-to-sum to the mirror-symmetric identity (♦) c²·sin(γ−λ)/(sin(α+γ) sin λ) = b²·sin(β−μ)/(sin(α+β) sin μ), λ = ∠ALK, μ = ∠AKL.
Skeleton: in file; Steps 1–4 verified, Step 5 (closing (♦)) genuinely open.
Open gaps: the (♦) identity; configuration of second intersections.
Watch out for: λ = γ / μ = β are FALSE (would put M, N on the circle — refuted numerically).

---

## Nominations (suggested build set)

1. **fixed-point-t** — primary. Every step has a verified mechanism; the only mathematical gaps are prose rigor and hand-expansion of two CAS-certified trig identities. Realistic shot at a full proof this round.
2. **quadratic-ideal-certificate** — robust fallback, independent builder. Shares Steps 1–3 (builders should coordinate via `lemmas/`: whoever proves the Parametrization and Constraint Lemmas first files them for certification).
3. **concyclic-with-w** — build only if a third builder is available; otherwise keep live for next round (its Reformulation Lemma is also worth certifying as a shared lemma — it is short, complete, and gives every future approach a cleaner target: "show A, K, L, W concyclic").

Hold: power-point-trig (live, no builder this round; its Step 5 has no verified mechanism yet).

Note for the outline-reviewer: the four slugs share the coordinate setup and Steps 1–3 lemmas but differ in the finishing mechanism (fixed point vs. ideal certificate vs. concyclicity/resultant vs. trig identity (♦)). The shared Steps 1–3 are *verified* (numerically exact and derived, not conjectural), so this is not a single-line trap on an unproven shared step; still, if Steps 1–3 somehow failed, all four die — the reviewer should weight the certification of those lemmas as the round's first priority.
