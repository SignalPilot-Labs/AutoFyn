# Lemma: euclid-identity-with-zeros

**Status: certified (proof-reviewer, round 1)** — proved in full in `approaches/star-monoid-product-descent.md`, Step 2 (Lemma 3 there). Statement checked against the proof — no overclaim; all zero/equality cases (b = 0, a = b) explicitly present, identity re-derived independently.

## Statement

With gcd on ℤ≥0 defined by the multiset-gcd characterization (gcd(k,0) = k, gcd(0,0) = 0; see lemma `multiset-gcd-characterization`):

**Lemma.** For all a, b ∈ ℤ≥0: gcd(a, b) = gcd( min(a,b), |a − b| ).

All cases covered: a ≥ b vs a < b (both sides symmetric in a, b), b = 0 (both sides equal a), a = b (both sides equal a).

## Where proved

`results/imo-2026-01/approaches/star-monoid-product-descent.md`, Step 2, Lemma 3: WLOG a ≥ b; the common-divisor sets of {a, b} and {b, a − b} coincide (d | a, d | b ⟹ d | a−b; d | b, d | a−b ⟹ d | a), and equal common-divisor sets force equal gcd by the characterization.

## Reuse notes

This is the per-prime engine of move-invariance for imo-2026-01: a move sends the p-exponent pair (a, b) = (v_p m, v_p n) to (min(a,b), |a−b|) = (v_p gcd(m,n), v_p (lcm/gcd)), and this lemma says the exponent-pair gcd is preserved. Shared core of both invariant approaches.
