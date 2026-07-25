## Status
partial

## Approaches tried
- (new, round 1) Midpoint-doubling / phantom-point reframe: reflect K over M and L over N to eliminate the two midpoint-angle conditions, recasting the whole problem as angles at A, B, C and revealing the equidistance OM=ON as an equal-power statement about the reflected configuration.

## Current best
- M,N are midpoints, and OM=ON is a statement about distances from the circumcenter of AKL to the two midpoints — a "midpoint + circumcenter" pattern where the reflection-through-midpoint (parallelogram) trick is the classical lever.
- Reflection K′ = 2M − K makes BK′AK a parallelogram (M bisects both AB and KK′): AK′ ∥ BK, AK′ = BK, and ∠BMK = ∠(K′ at ...) — the midpoint-angle condition (4) ∠LCK=∠BMK becomes an angle at A/K′. Symmetrically L′ = 2N − L.

## Target
OM = ON for every admissible configuration.

## Technique (spine)
Reflection through a midpoint to build parallelograms (phantom points K′, L′), converting the two midpoint-angle hypotheses into vertex-A angle conditions, then a spiral-similarity / equal-power argument on the cleaned configuration. Named tools: KB "Synthetic toolkit" (spiral similarity, power of a point), central symmetry.

## Skeleton
1. Define K′ = 2M − K, L′ = 2N − L (central reflections through the midpoints). Then BK′AK and CL′AL are parallelograms: AK′ = BK, AK′ ∥ BK; AL′ = CL, AL′ ∥ CL. — midpoint bisects both diagonals.
2. Translate the midpoint-angle conditions: ∠BMK is the angle at M in triangle BMK; under the reflection, ∠BMK = ∠AMK′ and relates to the angle ∠(AK′, ...) at A. Rewrite hypothesis (4) ∠LCK=∠BMK and hypothesis (3) ∠LBK=∠LNC purely in terms of angles at A, B, C and the phantom points K′, L′. — central symmetry preserves angles/lengths.
3. Key distance identity: OM and ON, with M=(A+K K′ midpoint) i.e. M is the midpoint of KK′, so OM² = (OK²+OK′²)/2 − KK′²/4 (median/parallelogram law in triangle OKK′). Since OK=R (K on ⊙AKL), OM² = (R²+OK′²)/2 − |MK|²... — parallelogram law / median length formula.
   Equivalently OM² − R² = pow(M,⊙AKL) and M is the midpoint of chord-related segment; use OK=OL=OA=R.
4. Reduce OM=ON to OK′² − 4|MK|²·(…) = OL′² − 4|NL|²·(…): a relation between the phantom points K′, L′ and the circle. Show OK′ = OL′ (i.e. K′, L′ equidistant from O) together with |MK|=|NL|-type balancing — driven by the rewritten conditions from step 2. — algebra + step 2.
5. Prove the needed equal-power/equal-distance via the phantom configuration and the σ symmetry (B↔C, M↔N, K↔L ⟹ K′↔L′). — σ transport.

## Key lemmas (claim + mechanism)
- Lemma P (parallelogram): AK′ = BK and AK′ ∥ BK (resp. AL′=CL, AL′∥CL) — because M is the common midpoint of diagonals AB and KK′, so ABK′... is a parallelogram; central symmetry through M.
- Lemma D (median distance): OM² = (OK² + OK′²)/2 − |KK′|²/4 with OK=R — because M is the midpoint of KK′ and the median-length (parallelogram) identity relates the median OM to the sides OK, OK′ of triangle OKK′.
- Lemma B (balance): OK′ = OL′ — because the rewritten hypotheses (from step 2) make K′, L′ related to A by AK′=BK, AL′=CL with matched angles, and the σ symmetry forces their distances to the σ-fixed point O to coincide. [This is the crux; see gap.]

## Open gaps (builder fills)
- GAP-1 (step 2): the exact translation of ∠BMK, ∠LNC into vertex-A angle statements via the reflection. Must be done with directed angles and verified numerically (compute K′,L′, check the claimed angle equalities).
- GAP-2 (steps 4–5, THE crux): prove OK′ = OL′ (Lemma B), or the correct balancing relation, from the rewritten conditions. Numerically test OK′ =? OL′ FIRST — if false, replace Lemma B with the correct balancing identity that Lemma D needs (OM=ON does NOT require OK′=OL′ alone; it requires (OK′²−|KK′|²/... ) to match the N-side). Builder must derive the precise target from Lemma D before proving it.

## Cases to cover
- Orientation of reflections (K′ may fall outside the triangle) — irrelevant to the algebraic identities but state directed conventions.

## Watch out for
- This is a genuinely different framing from the other three: it INTRODUCES the phantom points K′,L′ as the primary objects (neither the pow(M)=pow(N) chord route, nor coordinates, nor the raw synthetic circle). Keep it distinct.
- VERIFY Lemma B numerically before building on it — it is a plausible guess, not confirmed; the median-law reduction (Lemma D) is the solid part, the balancing target must be pinned by numerics first.
- Explorer confirmed KM ≠ LN and ∠KOM ≠ ∠LON — so there is NO termwise congruence ΔOMK≅ΔONL; the balance in step 4 is genuinely a summed/median identity, not a congruence. Do not attempt SAS congruence.
