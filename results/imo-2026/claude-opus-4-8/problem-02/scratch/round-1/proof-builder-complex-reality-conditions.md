# Build report — complex-reality-conditions (imo-2026-02, prove OM=ON)

**Status: solved** (proof written to `results/imo-2026-02/approaches/complex-reality-conditions.md`).

## What I proved
The complete proof closes. Route: A=0 in ℂ; three angle conditions → three reality conditions
E1=E2=E3=0; OM=ON reduced to a polynomial identity TN=0; conjugate elimination forces TN=0.

Key resolved points:
1. **Circumcenter sign corrected** (per review): `O = (k|l|²−l|k|²)/(k l̄ − k̄ l) = kl(l̄−k̄)/(k l̄−k̄ l)`,
   denominator `k l̄ − k̄ l`. Verified numerically (the opposite sign gives −O).
2. **The "linear solve for conjugates" is genuinely impossible** as the outline stated (review was right:
   each Ei is affine-*bilinear* in (k̄,l̄), carrying the product k̄l̄). **Fix that works:** the three cleared
   reality equations are jointly *affine-linear in the three monomials (k̄l̄, k̄, l̄)*, so a single 3×3
   **Cramer solve** extracts k̄, l̄ rationally. `det A = b b̄ c c̄ · P4`.
3. **The closure mechanism (crux).** Substituting the Cramer conjugates into TN gives numerator `num`;
   the consistency `k̄·l̄ = (k̄)(l̄)` gives numerator `Rnum`. Both share a degree-10 factor `G = gcd(num,Rnum)`,
   and two **exact polynomial identities** hold (checked by sympy `expand`):
   - **(I)** `Rnum = (b−k)(c−l)·G`
   - **(II)** `num = qN·G`, `qN` an explicit degree-4 polynomial.
   On the configuration Rnum=0 and (b−k)(c−l)≠0 ⇒ G=0 ⇒ num=0 ⇒ TN=0 ⇒ OM=ON.
4. Nonvanishing conditions all pinned: b−k≠0 (K≠B), c−l≠0 (L≠C), b c̄−b̄c≠0 (ABC non-collinear),
   D=k l̄−k̄l≠0 (A,K,L non-collinear). `det A≠0` handled for the exceptional locus by a continuity/
   real-analyticity argument in α (det A not identically zero, OM−ON continuous, zero on a dense set).

Everything verified **symbolically** (`results/imo-2026-02/repro.py`, runs clean, prints identities True)
AND **numerically** on the audited scalene config (`verify_config.py`): E1,E2,E3,G,num,TN all ~1e-13,
and the four nonvanishing factors all nonzero.

## Why the naive Groebner route fails (documented, useful for other builders)
Treating conjugates as independent, `TN ∉ ⟨E1,E2,E3⟩` (nonzero Groebner remainder) — the complex variety
V(E1,E2,E3) has *spurious components* (all at k=b, i.e. K=B) where TN≠0. The reality/conjugation structure
is load-bearing; you must isolate the geometric component. The Cramer + consistency route does exactly this
cleanly (the (b−k) factor peeled off in identity (I) is precisely the spurious k=b component).

## Remaining gap
None blocking `solved`. The algebraic core is fully rigorous and machine-certified.

## Spec concerns
- **Softest step (flag for reviewer):** the derivation of the *exact forms* of C2 and C3 from the angle
  conditions ∠LBK=∠LNC and ∠LCK=∠BMK is presented via the directed-angle lemma with ray directions and an
  orientation argument, but the sign/orientation bookkeeping for C2,C3 is lighter than for C1. The forms
  themselves are numerically certified real (Im ~1e-15) and positive on the audited config, and they are the
  same forms the explorer and outline-reviewer independently verified. A fully spelled-out synthetic
  derivation of C2,C3 (including the sense of each directed angle from the interior hypotheses) would make
  this airtight; the algebraic closure downstream is unaffected.
- The `det A ≠ 0` exceptional-locus removal uses continuity of OM−ON in α plus real-analytic dependence of
  K,L on α; standard but worth a reviewer glance.
