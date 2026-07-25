# Build report — per-prime-gcd-invariant (imo-2026-01), round 1

Status: **solved**. Complete rigorous proof of both parts written to
`results/imo-2026-01/approaches/per-prime-gcd-invariant.md`.

## What was closed (all outline gaps)
- **Step 1 primewise action**: proved v_p(gcd)=min, v_p(lcm)=max via a from-scratch
  valuation argument (V1/V2), hence v_p(ℓ)=max−min, a valid nonneg exponent (ℓ integer).
- **Lemma A (g_p exact invariant)**: full proof with the Euclidean subtractive identity (E)
  proved from scratch AND the multiset-gcd associativity gcd(A⊔B)=gcd(gcd A,gcd B) stated
  explicitly (G1), plus the gcd(0,x)=x, gcd(0,0)=0 conventions (G0) for exponent-0 slots and
  the n=2 / empty-rest boundary.
- **Lemma B (termination)**: Ω(g)+Ω(ℓ)=Ω(m)+Ω(n)−Ω(gcd) derived from complete additivity of
  Ω and lcm·gcd=mn; identity (†) ΔΩ_total=−Ω(gcd); both cases (gcd>1 → Ω drops; gcd=1 → g=1,
  K drops by exactly 1) and the m=n subcase (g=m, ℓ=1) handled. Well-ordering of
  (ℤ≥0 × {0..n}, lex) justified via the explicit embedding (n+1)Ω_total+K into ℕ.
- **Lemma C (non-collapse)**: g·ℓ=lcm≥max(m,n)>1 ⇒ outputs never both 1 ⇒ K≥1 always.
- **Step 5 (≤1)**: purely definitional from move-legality (needs K≥2), contrapositive.
- **Step 8 (value/part b)**: gcd of {one e_p, 2025 zeros}=e_p via (G0); same-slot noted as
  FORCED by K=1 (not a separate hard fact); finiteness of the product argued; conclusion
  M=∏ p^{g_p} depends only on the initial board.
- **Concrete verification**: {12,18,20}→M=30 by explicit play and by formula; also the
  M≠gcd caution {4,8}→2 (gcd=4) with a clean play and Ω_total descent.

## Numeric checks (as checks, not proof steps)
- python3: 2000 random plays on {12,18,20} all end at 30; formula ∏ p^{g_p}=30. Match.

## Spec concerns
- None material. The problem is `proof_only`, `answer_type: none`; no final numeric answer
  required, but the proof still produces the closed form M=∏ p^{g_p} as a bonus and verifies
  it. n=2026 is not load-bearing (works for any n≥2); this is noted, not assumed.
- The move-legality reading ("two integers m>1 and n>1 from different places") is taken as
  "two distinct slots each holding a value >1"; equal values in different slots are allowed
  (m=n subcase covered). This matches the standard interpretation.

## Promotable lemmas (for certification)
Lemma A (per-prime gcd invariant), Lemma B (lex monovariant/termination), Lemma C
(non-collapse), and the closed form M=∏ p^{g_p}. All proved in full in the approach file.
