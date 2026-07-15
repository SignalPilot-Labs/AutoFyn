## product-support-descent — APPROVE

This is a complete end-to-end route to both requested parts. The scalar monovariant is valid: if the chosen pair has \(d=\gcd(m,n)>1\), its product changes from \(mn\) to \(mn/d\), while the number of nonunits cannot increase, so \(2^rP\) strictly decreases; if \(d=1\), the output is \((1,mn)\), so the product is fixed and \(r\) decreases by exactly one. Terminality then gives at most one nonunit. The positive-exponent gcd invariant is the right complete invariant at a terminal board and is supported by the subtractive Euclidean identity, not assumed circularly.

Builder requirements:
- In Step 2, state that both outputs are positive integers and check \(r'\le r\) when \(d>1\), including \(m=n\), where the second output is 1.
- In Step 6, treat \((0,0)\), exactly one zero, unequal positives, and equal positives explicitly. Formulate the invariant as the gcd of the nonempty set of positive valuations for an initially occurring prime. (The outline's warning about a gcd over all exponents is unnecessarily restrictive: ordinary gcd is unchanged by adjoining zeros, but the positive-set convention is harmless and makes support persistence explicit.)
- In Step 8, first prove no prime outside the initial finite support can appear, then use unique factorization to identify the terminal integer.

No fatal gap or repeated dead end was found. This is the shortest and least encumbered presentation in the field.

## omega-lexicographic-euclid — APPROVE

This is also a whole proof of (a) and (b). The exact multiplicity calculation is sound:
\[
\Omega(d)+\Omega(\operatorname{lcm}(m,n)/d)
=\Omega(m)+\Omega(n)-\Omega(d).
\]
Thus \(S\) loses \(\Omega(d)\); when that loss is zero, \(d=1\) and two nonunits become \(1,mn\), so the second lexicographic coordinate drops. The same coordinatewise Euclidean invariant correctly determines the survivor.

Builder requirements:
- Spell out the displayed \(\Omega\) identity using complete additivity and \(\operatorname{lcm}(m,n)=mn/d\); do not merely assert it.
- State why lexicographic order on \(\mathbb N^2\) is well-founded, for example by observing that the first coordinate can fall only finitely often and, while fixed, the bounded second coordinate falls.
- Cover all valuation zero/equality cases and support persistence exactly as required in the first approach.

This route is essentially the additive logarithmic version of product-support-descent rather than a substantially different mathematical attack, but it remains a self-contained rival whole attempt and has a clean termination calculation. It ranks approximately level with the scalar route.

## colored-prime-piles — APPROVE

The reformulation is faithful and the argument reaches both claims. For each color the total atom loss in the selected places is \(\min(x,y)\), so total atom mass falls exactly when the selected integers share a prime. If they share none, their supports are disjoint, gcd is 1, and the quotient output carries their union, reducing two occupied places to one. The per-color positive-pile gcd is preserved by the Euclidean replacement and completely determines the terminal occupied place.

Builder requirements:
- Derive the pile update from both integer outputs: the gcd has exponent \(\min(x,y)\), while \(\operatorname{lcm}/\gcd\) has exponent \(\max(x,y)-\min(x,y)=|x-y|\).
- Make explicit that “share an atom color” means some selected-coordinate minimum is positive, so summing the coordinate losses gives strict global atom descent; otherwise all minima vanish and occupied-place count drops exactly one.
- Treat both-empty, one-empty, equal-positive, and unequal-positive piles in the color invariant. Keep one common selected pair for every color.
- Translate empty/nonempty places back to integers 1/>1 and invoke unique factorization at the end.

This is rigorous in principle but more verbose than the two arithmetic routes, so it ranks below them. It remains worth retaining as a genuinely different presentation, but not in the initial build set.

## rewrite-normal-form — APPROVE

The rewrite-system skeleton is logically sound and does not rely on an invalid confluence assertion. Termination follows from the same coordinate-mass/support lexicographic descent as the colored route. Reachable normal forms have at most one nonzero vector; coordinatewise positive-entry gcd labels are invariant and retain nonempty support, excluding the all-zero state. On a one-vector normal form the labels equal that vector, so all reachable normal forms coincide up to permutation. This correctly proves choice independence without a diamond lemma.

Builder requirements:
- In Step 3, separate overlapping supports (at least one positive coordinate minimum, hence strict mass loss) from disjoint supports (all coordinate minima zero, mass fixed, and two nonzero vectors replaced by zero and their coordinatewise sum, hence support count drops one).
- In Step 5, prove both label invariance and support persistence coordinatewise in all zero/equal/unequal cases; finite support follows from the finite set of primes occurring initially.
- Define normal form relative to legal moves: since moves require two nonunits, it is exactly a state with at most one nonzero vector.
- Do not infer local confluence or commutation of overlapping moves. The only uniqueness claim justified is that every reachable normal form has the invariant label vector.

This is a valid whole route, but it adds rewrite-system terminology without shortening either load-bearing argument and ranks last in the current field. It should remain registered but is not selected for the first build.

## Ranking rationale

All four approaches are new and were registered. With no prior outcomes to anchor against, comparisons use proof economy and distance from a polished Olympiad proof: product-support-descent and omega-lexicographic-euclid are effectively tied as the cleanest routes; colored-prime-piles is sound but translation-heavy; rewrite-normal-form is sound but adds abstraction and normal-form bookkeeping. No branch copy is warranted because no existing approach has split into two distinct gap-closing paths.

build set: product-support-descent, omega-lexicographic-euclid
