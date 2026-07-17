# Build report — per-prime-valuation-descent (imo-2026-01), round 1

**Status: solved.** Both parts (a) and (b) proven in full, gap-free.

## What was built
- Led with the direct lexicographic descent (extremal fallback dropped as redundant, per outline-reviewer).
- Cleaned the scratch clutter from step 3: final orientation stated cleanly as Φ=(Ω,N), Ω primary, N secondary.
- Noted finiteness of relevant primes P before summing over primes; showed no move introduces a new prime, so Ω is a well-defined finite sum.

## Gaps closed
- **T1**: Ω non-increasing with strict-drop criterion ⇔ gcd>1 (via min+|a−b|=max ≤ a+b, equality iff min=0); coprime move keeps Ω fixed and drops N by exactly 1; non-coprime move drops Ω and never raises N; no move fixes both. Lex descent airtight; explicit bound (Ω₀+1)·2026 moves.
- **B1**: gcd(min(a,b),|a−b|)=gcd(a,b) for all a,b≥0, all boundaries (a=b, b=0, a=b=0) checked, via common-divisor-set equality (subtractive Euclid).
- **B2**: gcd determined pairwise over a zero-containing multiset, via the universal (common-divisor) property of gcd; single-pair change preserves whole-tuple gcd.
- **B3**: some g_{p₀}>0 (initial entry >1 gives a valuation ≥1; gcd of not-all-zero valuations is positive), invariant ⇒ terminal M>1, excluding N=0.
- Terminal read-off: v_p(M)=g_p ⇒ M=∏_p p^{g_p}, choice-independent.

## No circularity
Part (b)'s g_p invariance is proved without reference to termination; Part (a) step 5 imports it to exclude N=0. Noted explicitly in the proof.

## Named theorems
Fundamental Theorem of Arithmetic; Well-Ordering Principle / lexicographic well-foundedness on ℕ×ℕ; subtractive Euclidean identity; universal property of gcd; invariant/monovariant technique (knowledge_base.md).

## Residual gaps
None. Included a small sanity example ({4,6}→M=6=∏p^{g_p}) as illustration, flagged as not load-bearing.

Distinct from sibling global-lex-monovariant: per-prime valuation-mass potential Ω rather than global product P; the two termination engines do not share a wall.
