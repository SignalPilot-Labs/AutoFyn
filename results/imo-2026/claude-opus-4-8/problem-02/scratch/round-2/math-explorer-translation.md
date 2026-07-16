## imo-2026-02 — geometry→algebra translation / directed-angle bookkeeping for `complex-reality-conditions`

### The gap and its resolution

The three "reality conditions" C1, C2, C3 are asserted in the current approach and verified numerically, but not proved from the unsigned angle equalities and interior conditions. Below is the complete rigorous derivation.

---

### 1. Precise machinery: unsigned angle equality → reality condition

**Setup.** Place A = 0 in ℂ; B = b, C = c, K = k, L = l, M = b/2, N = c/2. CCW orientation means Im(c·b̄) > 0.

**Directed-angle framework.** For distinct P, Q, R ∈ ℂ, define the directed angle at Q from ray QP to ray QR as:
```
∢(QP, QR) = arg((R−Q)/(P−Q))   ∈ ℝ/πℤ
```
This is a standard Olympiad tool (knowledge_base.md, Geometry "Synthetic toolkit: angle chasing"). The key fact: a complex number z = X/Y is real iff arg(z) ≡ 0 (mod π) iff ∢(...) from the numerator direction to the denominator direction is 0 mod π.

**The translation lemma (the exact mechanical step):**

For each Ci, compute arg(Ci) in terms of two directed angles:

- C1 = bc/((k−b)(l−c)). Then:
  ```
  arg(C1) ≡ arg(−b/(k−b)) + arg(−c/(l−c)) (mod π)
           ≡ ∢(BK, BA) + ∢(CL, CA) (mod π)
           = ∢(BK, BA) − ∢(CA, CL) (mod π)
  ```
  So **C1 ∈ ℝ ⟺ ∢(BK, BA) ≡ ∢(CA, CL) (mod π)**.

- C2 = (k−b)(2l−c)/(c(l−b)). Then:
  ```
  arg(C2) ≡ arg((k−b)/(l−b)) + arg((2l−c)/c) (mod π)
           = ∢(BL, BK) − ∢(NL, NC) (mod π)
  ```
  [Use N = c/2: direction NL = (2l−c)/2, direction NC = c/2; so ∢(NL,NC) = arg(c/(2l−c)) = −arg((2l−c)/c).]
  So **C2 ∈ ℝ ⟺ ∢(BL, BK) ≡ ∢(NL, NC) (mod π)**.

- C3 = b(k−c)/((l−c)(2k−b)). Then:
  ```
  arg(C3) ≡ arg(b/(2k−b)) + arg((k−c)/(l−c)) (mod π)
           = −∢(MB, MK) + ∢(CL, CK) (mod π)
  ```
  [Use M = b/2: direction MB = b/2, direction MK = (2k−b)/2; ∢(MB,MK) = arg((2k−b)/b).]
  So **C3 ∈ ℝ ⟺ ∢(CL, CK) ≡ ∢(MB, MK) (mod π)**.

These three equivalences are exact: no approximation, no continuity, no mod-π ambiguity introduced yet. The directed-angle equalities mod π are the exact algebraic content of the three Ei = 0 equations.

---

### 2. Resolving the sign ambiguity using interior/orientation conditions

**The key step:** The unsigned equality ∠XYZ = ∠PQR says both directed angles have the same absolute value, but they could have opposite signs (supplementary). The interior conditions eliminate the supplementary case by pinning both to the SAME sign.

**Fundamental sign lemma (used in all three):** If α₁, α₂ ∈ ℝ/πℤ both have representatives in (0°, 180°) and |α₁| = |α₂| as unsigned angles, then either α₁ = α₂ (C real) or α₁ + α₂ = π (C not real, supplementary). The interior conditions force the first case.

**C1: ∠KBA = ∠ACL → C1 ∈ ℝ**

Let α₁ = ∢(BK, BA) and α₂ = ∢(CA, CL). C1 ∈ ℝ iff α₁ ≡ α₂ (mod π).

- **α₁ > 0:** K is inside triangle BMC. That triangle is CCW (since ABC is CCW and M = midpoint AB). K inside the CCW triangle BMC means K is on the C-side of line BA (positive signed area of B,K,C > 0, verified: 0.374). This places the ray BK in the interior of angle ∠CBA, giving ∢(BK, BA) = arg(−b/(k−b)) ∈ (0°, ∠CBA) ⊂ (0°, π). So α₁ > 0.

- **α₂ > 0:** L is inside triangle BNC. That triangle is CCW (verification: signed area(B,N,C) > 0). L inside CCW BNC means L is on the B-side of NC, i.e., signed area(N,C,L) > 0. This gives ∢(CA, CL) = arg((l−c)/(−c)) ∈ (0°, ∠BCA) ⊂ (0°, π). Numerically: signed_area(N,C,L) = 0.113 > 0. So α₂ > 0.

- Both α₁, α₂ ∈ (0°, π) and equal as unsigned angles → **α₁ = α₂ as real numbers** → C1 ∈ ℝ.

**C2: ∠LBK = ∠LNC → C2 ∈ ℝ**

Let β₁ = ∢(BL, BK) and β₂ = ∢(NL, NC). C2 ∈ ℝ iff β₁ ≡ β₂ (mod π).

- **β₁ > 0:** The hypothesis "K inside angle LBA" means ray BK lies strictly inside the angular region bounded by rays BL and BA at B. In directed-angle terms: 0 < ∢(BL, BK) < ∢(BL, BA). So β₁ = ∢(BL, BK) ∈ (0°, ∠LBA) ⊂ (0°, π). Numerically: β₁ = 38.82° > 0.

- **β₂ > 0:** L inside CCW triangle BNC → L is on the B-side of segment NC (positive signed area of NLC sub-triangle). Concretely: signed_area(N, C, L) = Im((C−N)·conj(L−N))/2 = Im(c/(2l−c))·|L−N|²/2 > 0, hence Im(c/(2l−c)) > 0, hence β₂ = arg(c/(2l−c)) ∈ (0°, π). Numerically: signed_area(N,C,L) = 0.113 > 0, β₂ = 38.82°.

- Both in (0°, π) and equal as unsigned angles → **β₁ = β₂** → C2 ∈ ℝ.

**C3: ∠LCK = ∠BMK → C3 ∈ ℝ**

Let γ₁ = ∢(CL, CK) and γ₂ = ∢(MB, MK). C3 ∈ ℝ iff γ₁ ≡ γ₂ (mod π).

- **γ₁ > 0:** The hypothesis "L inside angle ACK" means ray CL lies strictly inside the angle ACK at C: 0 < ∢(CA, CL) < ∢(CA, CK). Then γ₁ = ∢(CL, CK) = ∢(CA, CK) − ∢(CA, CL) > 0, and γ₁ < ∢(CA, CK) < π. Numerically: γ₁ = 17.96° > 0.

- **γ₂ > 0:** K inside triangle BMC, with M = b/2. The triangle BMC is CCW (signed_area(B,M,C) = 0.75 > 0 numerically). K inside BMC means K is on the C-side of segment BM, i.e., Im((K−M)·conj(B−M)) > 0. In our notation: Im((k−b/2)·conj(b/2)) = Im((k−b/2)·b̄/2) > 0. This gives Im((2k−b)/b) > 0, hence γ₂ = arg((2k−b)/b) ∈ (0°, ∠BMC) ⊂ (0°, π). Numerically: Im((K−M)·conj(B−M)) = 0.0917 > 0, γ₂ = 17.96°.

- Both in (0°, π) and equal as unsigned angles → **γ₁ = γ₂** → C3 ∈ ℝ.

---

### 3. Which condition is cleanest and which has the most subtlety

**C1 is cleanest.** Both directed angles are directly ∢(BK,BA) and ∢(CA,CL), which are the literal angles mentioned in condition 1. The interior conditions K ∈ BMC and L ∈ BNC directly ensure both are positive. No auxiliary point calculation needed.

**C2 is the most subtle** and introduces the main sign challenge. The condition ∠LBK = ∠LNC involves the angle at N = c/2, and the direction NL becomes (2l−c)/2 and NC becomes c/2, so the directed angle is arg(c/(2l−c)) — the factor 2l−c is the algebraic artifact of N = c/2 being a midpoint. The sign of β₂ is not immediately obvious from the original geometry: it requires the signed-area argument that L ∈ BNC (CCW) places L on the B-side of segment NC, making Im(c/(2l−c)) > 0. Without this argument, one might mistakenly allow the supplementary case (β₁ + β₂ = π), which would give a DIFFERENT and WRONG reality condition.

**C3 is intermediate.** γ₂ = arg((2k−b)/b) — again a midpoint artifact (M = b/2 gives 2k−b in the numerator). The sign is fixed by K ∈ BMC implying K is on the C-side of BM, which gives Im((K−M)·conj(B−M)) > 0.

---

### 4. Exact steps the builder must establish

**Step 1 — Confirm CCW orientation and sub-triangle CCW-ness.**
State: with A=0, the CCW condition on ABC is Im(c·b̄) > 0. Then prove:
- Triangle BMC is CCW: signed_area(B, M, C) = Im((M−B)·conj(C−B))/2 > 0. (This is Im((−b/2)·conj(c−b))/2 = Im(b̄(c−b))/4, which equals Im(b̄c)/4 > 0 since Im(b̄c) = Im(c·b̄) > 0.) ✓ One line.
- Triangle BNC is CCW: signed_area(B, N, C) = Im((N−B)·conj(C−B))/2 = Im((c/2−b)·conj(c−b))/2. This equals Im((c̄−b̄)(c−b)/2)/4 + ... easier: expand Im((c/2−b)(c̄−b̄))/2 = (Im(c·c̄/2) − Im(b·c̄/2) − Im(c·b̄/2) + Im(|b|²))/2 = (−Im(b·c̄)/2 − Im(c·b̄)/2)/2... let me just note: signed_area(BNC) = signed_area(ABC)/2 > 0 (by the midpoint formula; N = midpoint(AC) cuts off exactly half the area from vertex B). ✓

**Step 2 — C1.** K ∈ interior(BMC) → positive signed sub-area SA(B,K,C) > 0 → K on C-side of line BA → ∢(BK,BA) ∈ (0°, π). Similarly L ∈ interior(BNC) → SA(N,C,L) > 0 → ∢(CA,CL) ∈ (0°, π). Unsigned equality ∠KBA = ∠ACL then gives C1 ∈ ℝ. (No use of the "K inside angle LBA" hypothesis for C1 — only the interior-triangle conditions.)

**Step 3 — C2.** "K inside angle LBA" directly gives ∢(BL,BK) ∈ (0°, ∠LBA) ⊂ (0°, π). For ∢(NL,NC): L ∈ interior(BNC) → SA(N,C,L) > 0 → Im((C−N)·conj(L−N)) > 0 → Im(c/(2l−c)) > 0 → ∢(NL,NC) = arg(c/(2l−c)) ∈ (0°, π). Unsigned equality ∠LBK = ∠LNC → C2 ∈ ℝ.

Pitfall to call out explicitly: the directed angle of interest at N is ∢(NL, NC) = arg((C−N)/(L−N)) = arg(c/(2l−c)), NOT arg(c/(l−c)) or arg((2l−c)/c). The factor 2l−c (not l−c or 2l) comes from L−N = l − c/2 = (2l−c)/2. The builder must write this step explicitly to avoid a sign error.

**Step 4 — C3.** "L inside angle ACK" gives ∢(CL,CK) ∈ (0°, π). For ∢(MB,MK) = arg((K−M)/(B−M)) = arg((2k−b)/b): K ∈ interior(BMC) with BMC CCW → K on C-side of BM at M → Im((K−M)·conj(B−M)) = Im((k−b/2)·b̄/2) > 0 → ∢(MB,MK) ∈ (0°, π). Unsigned equality ∠LCK = ∠BMK → C3 ∈ ℝ.

Pitfall: ∢(MB,MK) = arg((2k−b)/b), which comes from K−M = (2k−b)/2 and B−M = b/2. Writing (2k−b)/b clearly (not k/b or (k−b/2)/(b/2) in a muddled form) is load-bearing.

**Step 5 — Each Ci ∈ ℝ means the corresponding Ei = 0.** This is immediate: Ei is the numerator of Ci − conj(Ci), so Ci ∈ ℝ ↔ Ci = conj(Ci) ↔ Ei = 0.

---

### 5. Knowledge-base entries

- **"Synthetic toolkit: angle chasing"** (knowledge_base.md, Geometry section): the directed-angle mod π framework is the engine.
- **"Coordinates / complex / barycentric"** (knowledge_base.md, Geometry section): the A=0 setup and arg(ratio) = directed angle.

No crux corpus entries are relevant (geometry is not in the corpus: crux_moves_documentation.md, last line).

---

### 6. Analogous past problems

None in the corpus. The closest structural analogue from the round-1 analogy scout (aimo-0068) uses power-of-a-point at a midpoint, not directed-angle algebra.

---

### 7. What "asserted+numeric" vs. "rigorously derived" means for the proof

The current approach says "Fix the orientation so A, B, C are CCW... the hypotheses fix the sense... so each unsigned-angle equality is equivalent to the stated reality condition" and then verifies numerically. This is asserted, not proved.

The rigorous proof needs exactly the five steps above. None require heavy computation — each is one or two lines of signed-area algebra. The only non-obvious step is Step 3 (C2): showing L ∈ interior(BNC) forces Im(c/(2l−c)) > 0 via the signed-area formula.

Once Steps 1–5 are done, the rest of the proof (Sections 4–6 of the approach file: Cramer solve, factorizations I and II, continuity) is already rigorous (symbolically certified by repro.py) and needs no changes.

---

### Summary table

| Condition | Reality cond Ci | Both directed angles positive from... | Pitfall |
|---|---|---|---|
| C1: ∠KBA = ∠ACL | bc/((k−b)(l−c)) ∈ ℝ | K ∈ BMC (SA>0) + L ∈ BNC (SA>0) | None; cleanest case |
| C2: ∠LBK = ∠LNC | (k−b)(2l−c)/(c(l−b)) ∈ ℝ | K inside ∠LBA + L ∈ BNC (SA(N,C,L)>0) | Factor 2l−c not l−c; sign of β₂ most subtle |
| C3: ∠LCK = ∠BMK | b(k−c)/((l−c)(2k−b)) ∈ ℝ | L inside ∠ACK + K ∈ BMC (Im((K−M)conj(B−M))>0) | Factor 2k−b in γ₂; verify via signed-area of BMC |
