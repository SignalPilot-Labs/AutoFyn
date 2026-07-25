## imo-2026-02

coordinate-bash-resultant-boundary: advance
Target: For triangle ABC with M,N midpoints of AB,AC and K,L,O as defined
in the problem (K∈△BMC, L∈△BNC, the three angle hypotheses), prove OM=ON.
Technique: Coordinate/rotation parametrization (A=origin, Weierstrass
substitution u=tan(β/2)) + Gröbner-basis genericity certificate (already
closed) + resultant/Vieta/IVT branch-selection on the two-root quadratics
G2a,G2b (in s2) and G3a,G3b (in t1). This round's spine for the remaining
gap is a single-frequency-sinusoid threshold argument (endpoint evaluation
+ single-crossing lemma, the same template that already closed
branch-crossing-locus-equals-angle-B/C and the disc(Q) sign facts).
Skeleton:
  1. [ALREADY CLOSED, import] Genericity: OM=ON is equivalent to
     T∈⟨G2a,G3a⟩ — certified `lemmas/symbolic-genericity-certificate.md`.
  2. [ALREADY CLOSED, import] disc(Q(m))=16sin²A>0 with explicit roots
     r1,r2 — certified `lemmas/q-quadratic-discriminant-and-roots.md`.
  3. [ALREADY CLOSED, import] Magnitude bound + G2a root selection —
     certified `lemmas/magnitude-bound-and-sign-coincidence.md`,
     `lemmas/cross-product-sign-selection-G2a.md`.
  4. Restate the remaining gap in the unified offset-sinusoid form found by
     this round's rem-zero-lens: with P=sin(A−B)/2+3sin(A+B)/2,
     Q=−sinA·sinB, K=2sinA·sin(A+B), define f(β)=K+P sinβ+Q cosβ. Then
     (I)∧(II) ⟺ 0<f(β)<2K on the effective domain (the sub-arc of
     β∈(0,min(∠B,∠C)) where the hypotheses B2>0 (⟺sin(A+3β)<0) and Y>0
     jointly hold). Verify this restatement by exact sympy re-derivation
     of g=2K−f (zero-residual check) before building on it — do not just
     trust the explorer's report, re-derive independently.
  5. CROSS-CHECK STEP (do this FIRST, cheap, high leverage): test via
     sympy whether f(β)−K (equivalently P sinβ+Q cosβ) is proportional to,
     or simply related to, the `coordinate-bash-resultant-boundary-
     pointwise` approach's "num" quantity from its Y<0 case (num =
     AC[cos(2β+∠A)sinβ(1−2cosβ)+sin(2β+∠A)cos2β]). Both are late-stage
     trig expressions arising from the same G2a/G2b branch-selection core
     (per round 8's proven structural fact that all live gaps are the same
     algebraic object). If proportional (or one is a clean multiple of
     the other under the substitution m=sinB/sin(A+B)), closing either
     closes both — report this explicitly regardless of outcome, since a
     negative result here also has value (confirms genuinely different
     sub-targets, so both builds remain independently necessary).
  6. Identify the true right endpoint γ=min(∠B,∠C) case-split
     (WLOG ∠B≤∠C, so γ=∠B — use the certified F1=0⟺β=∠B fact to justify
     this is exactly where the domain closes) and evaluate f(γ) exactly
     via sympy (not the simpler β=B reference point already computed —
     that was f(β=B)=γ in the WLOG case, so may already suffice; check
     which).
  7. Evaluate f at the actual left endpoint of the *effective* domain
     (where B2=sin(A+3β) first becomes negative moving up from β=0, i.e.
     the crossing point identified by the already-certified `branch-
     crossing-locus-equals-angle-B/C.md`-style single-crossing lemma
     applied to sin(A+3β) itself — a degree-3-in-β sinusoid, k=3 in the
     single-crossing lemma's terms) — this determines the actual
     left endpoint β0(A,B) of the sub-arc where (I)'s hypothesis holds.
  8. Apply the already-certified single-crossing lemma (§12 of this file,
     reusable: "h(β)=p sin(kβ)+q cos(kβ) on (0,γ), γ<π/k, h(0)>0∧h(γ)>0
     ⟹ h>0 throughout") to f(β)−0 and 2K−f(β) separately on the correct
     restricted sub-interval [β0,γ] (k=1 here, so this only needs γ<π,
     always true) — this is the mechanical closure step once steps 6-7
     give sign-correct endpoint values.
  9. Combine: (I)∧(II) on the effective domain ⟹ G2b excluded ⟹ branch
     selection closed ⟹ (via the population's proven structural
     equivalence, round 8) the whole problem is solved.
Key lemmas (claim + mechanism):
  - g(β) = 2K − f(β) exactly — because both (I) and (II), expanded via
    product-to-sum on 2sin(A+B)(sinβ±sinA) and sinB·sin(A+β), collect to
    the same P,Q,K coefficients with the sinusoidal part negated between
    the two.
  - R²−K² = sin²(2A+B) ≥ 0 — because R²=P²+Q² and K² both expand via the
    same sinA,sinB,sin(A+B) product identities; this PROVES no global
    (full-period) certificate can exist, so the endpoint+single-crossing
    restriction to the effective sub-domain is not optional busywork but
    structurally necessary.
  - Single-crossing lemma (already certified, §12 of this file) — because
    a pure sinusoid of frequency k has zeros exactly π/k apart, so an
    interval shorter than π/k contains at most one zero, forcing a sign
    change only if the endpoints already disagree.
Open gaps: exact endpoint value of f at the TRUE effective-domain
boundaries (not yet computed — β=B reference point was computed but is
not proven to be the actual endpoint of the restricted-by-hypotheses
domain); the B2>0 crossing point β0(A,B) is not yet symbolically located.
Cases to cover: WLOG ∠B≤∠C (γ=∠B) vs ∠C≤∠B (γ=∠C), handled by the
existing σ-symmetry (swap B↔C).
Watch out for: do not mistake f(0)≤0 (true in ~25% of samples) for a
counterexample — β=0 is outside the effective domain since B2>0 generically
fails there; always check the hypothesis (I)'s domain restriction before
evaluating f at any β.

coordinate-bash-resultant-boundary-pointwise: advance
Target: Same as above (OM=ON for the full problem) via the pointwise
per-β architecture (avoiding the F3/F3' continuity question entirely).
Technique: Complex-affine reframing (L1,DK are Re/Im of one complex-affine
function of s2; DN is a second, independently-derived affine function) +
Vieta-midpoint sign comparison, same family as coordinate-bash-resultant-
boundary's resultant/sign toolkit but applied pointwise per fixed β rather
than via a continuity/IVT argument across β.
Skeleton:
  1. [ALREADY CLOSED, import] L1<0 always selects r_lo (the algebraically
     smaller root of G2a) — certified
     `lemmas/complex-affine-L1-DK-and-r-lo-selection.md`.
  2. [ALREADY CLOSED, import] G2a·G2b ∝ Lemma P1's quartic; W(r1)W(r2)≤0
     on G2a's own roots — certified `lemmas/g2a-true-supplementary-parity-
     and-quartic-identification.md`.
  3. [THIS ROUND'S NEW, import as working hypothesis, VERIFY before use]
     DN(s2) = (b²+cc²)/4·(1−2s2·cosβ) exactly (new closed form from this
     round's complex-affine-transfer-lens) — re-derive independently via
     sympy from the raw vector definitions V3=L−N, V4=C−N before building
     on it (the explorer's derivation used V4=C/2, dot(v1,C)=−|C|²cosβ;
     confirm this matches the file's existing DN conventions exactly,
     including sign/normalization, since a mismatched convention would
     silently invalidate downstream work).
  4. Split on sign(Y) (Y = 2a(u²−1)²−b(u²+1)², the sibling's already-
     certified branch factor): the round's new result is G2a(s2*) is an
     exact positive multiple of Y where s2* = 1/(2cosβ) is DN's zero —
     re-verify this exact identity symbolically before relying on it.
  5. Y>0 case (dominant, ~84% of configuration space numerically): close
     the two remaining short symbolic confirmations —
       (a) sign(DK(r_lo)) = sign(sin(2β+∠A)) exactly (currently only
           16,756-sample numeric match) — prove via the same slope/
           zero-crossing method already used for L1's Q(u) coefficient
           (compare DK's affine zero to G2a's Vieta midpoint m0, the
           identical method as step 3 above, applied to DK instead of DN).
       (b) sign(DN(r_lo)) = sign(1−u²) exactly (currently only numeric
           match) — likely follows directly from DN(s2)'s NEW exact
           linear closed form in step 3 (if DN is truly linear in s2 with
           the stated closed form, this reduces to comparing r_lo against
           s2*=1/(2cosβ) directly, no further sign-fitting needed — check
           whether step 3's closed form alone already proves this, making
           it a corollary rather than a separate confirmation).
     Once both hold: sin(2β+∠A)>0 (already certified, part (b) of
     `complex-affine-L1-DK-and-r-lo-selection.md`) and u=tan(β/2)<1
     (elementary, β<π/2 always since β<min(∠B,∠C)≤(∠B+∠C)/2<π/2) give
     W(r_lo)=DK(r_lo)·DN(r_lo)>0 unconditionally in this case — DONE for
     Y>0.
  6. Y<0 case (~16% of space): the harder remaining target. Prove
     sign(cos(2β+∠A)·num) ≥ 0, where
     num = AC[cos(2β+∠A)sinβ(1−2cosβ) + sin(2β+∠A)cos2β]
     (this round's new symbolic — not numeric-fit — closed form, replacing
     the previously-uncertified triple-angle trig-fit identity). Attempt,
     in order of cheapness:
       (a) product-to-sum expand cos(2β+A)·num fully and check whether it
           collects into a manifest sum-of-nonnegative-terms or a single
           signed sinusoid amenable to the single-crossing lemma
           (import from coordinate-bash-resultant-boundary, step 8/9,
           k≤4 here since the expansion mixes 2β,3β terms) on the actual
           domain β∈(0,γ), γ=min(∠B,∠C);
       (b) if (a) doesn't collapse cleanly, run the CROSS-CHECK from the
           sibling approach's step 5 (is num proportional to f(β)−K from
           coordinate-bash-resultant-boundary's unified target?) — a
           positive answer would let a single symbolic proof close both
           approaches' gaps simultaneously.
  7. Combine Y>0 (step 5) and Y<0 (step 6) cases: W(r_lo)>0 unconditionally
     ⟹ branch selection closed ⟹ (via the population's proven structural
     equivalence, round 8) the whole problem is solved.
Key lemmas (claim + mechanism):
  - DN(s2) = (b²+cc²)/4·(1−2s2 cosβ) — because V4=C/2 exactly (N is
    midpoint of AC, so N=C/2, and V4=C−N=C/2) and dot(v1,C)=−|C|²cosβ by
    the definition of the rotation direction v1=R(β)(A−C)=−R(β)C.
  - u=tan(β/2)<1 unconditionally — because β<min(∠B,∠C)≤(∠B+∠C)/2<π/2
    (angle sum <π), and tan is increasing and =1 exactly at π/2.
  - G2a(s2*) is a positive multiple of Y — because Y is (per round 8's
    proven structural fact) the shared branch-selection object across all
    routes, and s2* (DN's zero, a natural interior reference point of the
    quadratic G2a) evaluating G2a there ties the sign-classification
    directly to the already-certified branch factor rather than to a new,
    independent quantity.
Open gaps: (a) the two Y>0 sub-confirmations (currently 16,756-sample
numeric only) not yet turned into sympy.simplify=0 certificates; (b) the
Y<0 case's sign(cos(2β+∠A)·num)≥0 claim, only 692-sample numeric so far,
no algebraic proof attempt has yet succeeded.
Cases to cover: Y>0 and Y<0 (exhaustive since Y is a single real quantity;
Y=0 is measure-zero degenerate, handle by continuity/limiting argument if
it arises, or note it coincides with a boundary already excluded by
genericity).
Watch out for: do not conflate this approach's "num" (Y<0 case sign
quantity) with the sibling coordinate-bash-resultant-boundary's f(β) −
they are DIFFERENT derivations (one from DN's Vieta-midpoint comparison,
one from the (I)/(II) threshold reformulation) and must be independently
verified equal (or not) rather than assumed identical — see step 6(b)
cross-check. Also do not re-derive DN's new closed-form denominator/sign
convention loosely; a mismatched sign convention here would silently flip
the whole Y-split's conclusion.

fixed-point-concyclic: advance (dormant this round, no build slot)
Target: Same as above via the bilinear/Cramer's-rule Rem=0 route.
Technique: unchanged from round 7-8 (bilinear forms in K,L + Cramer's rule
closed form χ=−D0/D1).
Skeleton: unchanged — Rem=0 is now a PROVEN free corollary of ⟨G2a,G3a⟩
(certified `lemmas/rem-zero-free-corollary-of-genericity-branch.md`), so
this approach's own algebraic content is fully closed and it has zero
remaining independent work; it inherits a solve automatically the moment
either sibling above closes branch selection.
Key lemmas: none new needed.
Open gaps: none of its own — entirely inherits the shared branch-selection
gap.
Cases to cover: none.
Watch out for: do NOT dispatch a builder to this file this round (per
rem-zero-lens and orthogonal-framing-lens, both confirm no independent
lever remains) — it would just re-derive the identical target under
different notation, as already happened once with inversion-at-A-
collinearity (retired round 8 for exactly this reason). Revive only if
both siblings above stall for another 2+ rounds and a genuinely new idea
for the shared gap surfaces.

ptolemy-trig-identity: advance (dormant this round, no build slot)
Target: Same as above via Ψ(τ,A,C)>0 sextic positivity.
Technique: unchanged — resultant elimination to a radical-free sextic,
reduced (round 6-7) to a four-branch odd-parity claim, with two reduction
levers (radical-isolation; Lemma A resultant route) already proven
equivalent-in-difficulty and pruned.
Skeleton: unchanged from round 6-7's file.
Key lemmas: none new needed.
Open gaps: the four-branch odd-parity claim itself (2000+ sample numeric,
no proof), unchanged since round 6.
Cases to cover: none new.
Watch out for: do NOT dispatch a builder here this round — it is a
genuinely different technique (independent value for diversity if the
coordinate routes stall), but no new lever surfaced this round to justify
spending a build slot on it; its own reduction levers are exhausted absent
a fresh idea. Keep it alive in the population (do not retire) as the
population's technique-diverse fallback per round 8's rules.

build set: coordinate-bash-resultant-boundary, coordinate-bash-resultant-boundary-pointwise
