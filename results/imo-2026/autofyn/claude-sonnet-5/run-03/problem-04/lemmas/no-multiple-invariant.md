# Lemma: "No angle is a θ-multiple" defense invariant (closes the "only if" direction)

**Source.** Two independent, essentially equivalent proofs exist in the population:
`approaches/ngon-arc-reduction.md` (Theorem 2, "disjoint bad-sets" argument, stated for real
θ and real cut parameter t) and `approaches/mod-theta-invariant.md` (Lemma 1, "property P",
a clean 4-case algebraic proof). Both are certified here as they prove the same statement by
genuinely different (though related) case-splits; either is a legitimate standalone citation.

**Statement.** Let θ ∈ (0,180) with θ ≠ 180/n for every integer n≥2 (equivalently, writing
r₀ = 180 mod θ, the hypothesis is r₀ ≠ 0). Say a triangle (A,B,C) has property 𝓘 ("no angle
is a θ-multiple") if none of A,B,C is a positive-integer multiple of θ. If the current
triangle has property 𝓘, then for every legal move (any vertex, any real cut parameter
t ∈ (0,X)), at least one of the two resulting children again has property 𝓘. Moreover a
triangle with property 𝓘 exists for every θ ∈ (0,180) (countable-bad-set / uncountable-
interval argument). Consequently Shan-Yu can open with such a triangle and always keep a
child retaining 𝓘, so no angle is ever exactly θ and Mulan never wins: **θ ≠ 180/n for any
integer n≥2 ⟹ Shan-Yu wins.**

**Proof (mod-theta-invariant's version, reproduced).** Write child1=(B,t,180−B−t),
child2=(C,A−t,B+t) via the Cut Formula. If both children failed 𝓘, one of {t≡0, 180−B−t≡0}
(mod θ, meaning "is a positive-integer θ-multiple") holds together with one of
{A−t≡0, B+t≡0}. The four resulting combinations force, respectively, A, B, C, or (180 mod θ)
to be ≡0 mod θ with a strictly-positive coefficient — contradicting either 𝓘 of the parent
(for A,B,C) or the hypothesis r₀≠0 (for the fourth case, 180=(a+b)θ). Full case algebra: see
`approaches/mod-theta-invariant.md` Lemma 1, or the equivalent "disjoint bad sets" computation
in `approaches/ngon-arc-reduction.md` Theorem 2.

**Status.** No gap in either write-up; reviewer independently re-verified the disjointness
claim by randomized exact-`Fraction` simulation over all 6 vertex/labelling permutations,
for random non-divisor θ both above and below 90°, thousands of trials, zero violations; also
verified end-to-end (60 trials × 40 random moves each, θ non-divisor) that the induced
Shan-Yu strategy survives indefinitely. Certified for reuse.
