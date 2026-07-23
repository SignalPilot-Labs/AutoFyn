# Lemma: median-reduction (certified, round 1)

**Statement.** Let ABC be a triangle with b = CA, c = AB, and M, N the midpoints of AB, AC. For **any** point O:

OM = ON ⟺ OB² − OC² = (c² − b²)/2.

If moreover ω is any circle through A with centre O, then equivalently
pow(B, ω) − pow(C, ω) = (c² − b²)/2, and in coordinates with A at the origin,
⟨O, B − C⟩ = (c² − b²)/4.

**Proof.** Median-length formula 4·OS² = 2·OP² + 2·OQ² − PQ² (two-line vector identity), applied at M and N and subtracted; the power form uses pow(P, ω) = |P|² − 2⟨O, P⟩ for a circle through the origin A. Full details: `approaches/complex-certificate.md`, Parts 1 and 5 (equations (1), (7)); equivalent form in `approaches/secant-trig-identity.md`, Step 1.

**Certification.** sorry-free; re-derived by the proof-reviewer by hand and confirmed numerically (round 1).
