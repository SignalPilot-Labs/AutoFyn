# Build report — antipode-perp-bisector (imo-2026-02), Round 2

**Status: partial (strong).** Independent synthetic route; does NOT touch (★★).

## What is now proven (rigorous)
- **Step 1 — Antipode equivalence:** with A=0 and A*=2O, `OM=ON ⟺ A*B=A*C ⟺ A* on perp-bisector of BC`. Two one-line expansions of differences of squared distances, equal because A*=2O. Also proved the **antipode–power bridge** `(X−A)·(X−A*)=pow_ω(X)`, giving `OM=ON ⟺ pow_ω(B)−pow_ω(C)=(AB²−AC²)/2` — shows antipode and power-of-point routes are the same reduction.
- **Step 2 — Location of A*:** `A*K⊥AK`, `A*L⊥AL` by Thales (A* antipode of A on ⊙AKL). Machine-exact.
- **Step 4 — Isosceles synthesis (proven, assuming Step 3):** C1 gives ∠KBA=∠ACL=α; ray orders + Lemma B/C give ∠A*BA=90°−C+α, ∠A*CA=90°−B+α; with A* inside angle BAC, ∠A*BC=|90°−A−α|=∠A*CB, so triangle A*BC isosceles ⟹ A*B=A*C ⟹ OM=ON. Robust including the α>90°−A sign-flip case (unsigned base angles stay equal).

## The advance this round (new)
Discovered and certified (to 1e-8, 4 triangles × 5 α) the **α-independent invariants**
- **Lemma B: ∠A*BK = 90°−C**
- **Lemma C: ∠A*CL = 90°−B**

The whole problem on this route reduces to these two crisp, mutually symmetric (B↔C/M↔N/K↔L) identities. They are strictly sharper than last round's "candidate mechanism" placeholder: they contain no free parameter, so any proof is automatically uniform in α.

## The remaining gap (precisely stated)
Prove Lemma B / Lemma C from the antipode structure (A*K⊥AK, A*L⊥AL) + conditions C2 (∠LBK=∠LNC), C3 (∠LCK=∠BMK). C1 is already consumed by Step 4. Ruled out numerically: BA* ⊥ CK/CL/AK/AL (no), A* on ⊙BKC or ⊙BLC (no), ∠KA*B α-independent (no). So it is a genuine angle-chase feeding on C2, C3, not a one-line incidence. Obtuse-at-B/C needs the directed-angle reading ∠(BK,BA*)≡90°−C (mod π).

## Artifacts
- Approach file: `results/imo-2026-02/approaches/antipode-perp-bisector.md`
- Verification: `results/imo-2026-02/repro_antipode.py` (all checks OK; run prints per-identity max residuals).

## For next round
Attack Lemma B / Lemma C directly. Because they are α-independent and symmetric, a proof of one gives the other for free. This is the natural next crux and is independent of the (★★)/(♦5) obstruction blocking the trig/power/complex closure — a real breadth hedge.
