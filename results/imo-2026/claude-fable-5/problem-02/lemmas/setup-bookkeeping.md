# Lemma: Setup & angle bookkeeping (CERTIFIED)

**Status: CERTIFIED by proof-reviewer, round 1. Full proof in `results/imo-2026-02/approaches/fixed-point-t.md`, §0–§1 (Sector Lemma = Lemma 0, Bookkeeping = Lemma 1). Reviewer checks: Sector Lemma half-plane argument and Lemma 1 interiority/direction-angle derivations read line by line — sound, hypotheses "K inside ∠LBA" / "L inside ∠ACK" used exactly where the orderings θ_L < θ_K, θ'_L < θ'_K are needed; statement independently confirmed numerically on 18 configurations (incl. obtuse at A, B, C) constructed directly from the problem hypotheses.**

## Setting
Problem imo-2026-02. Coordinates: B = (0,0), C = (a,0), A = c·e^{iB} in the open upper half-plane, where e^{iθ} := (cos θ, sin θ); a = BC, b = CA, c = AB; A, B, C also denote the angles. M = (A+B)/2, N = (A+C)/2. Define
α := ∠KBA = ∠ACL, β := ∠LBK = ∠LNC, γ := ∠LCK = ∠BMK (hypothesis equalities).
"Inside a triangle" = all three barycentric coefficients positive.

## Statement
1. A − C = b·e^{i(π−C)}, and a = b cos C + c cos B (projection formula).
2. K and L lie strictly inside triangle ABC; in particular they avoid the lines AB, BC, CA and the vertices.
3. Direction angles of rays: BA: B; BK: B − α; BL: B − α − β; CA: π − C; CL: π − C + α; CK: π − C + α + γ.
4. α > 0, β > 0, γ > 0, α + β < B, α + γ < C; hence sin(A + α) > 0.

## Proof
See `approaches/fixed-point-t.md` §0 (coordinates, Angle Fact, interiors), Lemma 0 (Sector Lemma, proved via half-plane cross-product computation) and Lemma 1 (proved via the barycentric inclusion int(BMC), int(BNC) ⊆ int(ABC) and the Sector Lemma applied at B and C, using the hypotheses "K inside angle LBA", "L inside angle ACK" for the angle additions ∠LBA = α + β, ∠ACK = α + γ).

## Numerical check
Verified during build: 5 triangles × several α, all direction angles and bounds consistent to ≤ 5e-15.
