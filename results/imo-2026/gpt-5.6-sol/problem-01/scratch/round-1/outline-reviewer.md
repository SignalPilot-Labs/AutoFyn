## arithmetic-product-content — APPROVE

This is a whole end-to-end attempt and its central claims are sound. For a selected pair, writing `g=gcd(m,n)`, the replacement product is `g*(lcm(m,n)/g)=lcm(m,n)=mn/g`. If `g>1`, the ordinary board product falls by at least a factor `2`, while the number of nonunits does not increase; if `g=1`, the pair becomes `1,mn`, so the product is fixed and the nonunit count falls by one. Thus `2^k P` is a valid strict positive-integer monovariant. The valuation update `(r,s)->(min(r,s),|r-s|)` preserves the gcd of the selected exponents and consequently the gcd of the whole column. Because every initially occurring prime has a nonzero exponent column, its column gcd is positive even though zeros are included; this rules out an all-unit terminal board and yields the stated explicit formula.

Builder requirements: write the strict inequalities explicitly; handle `m=n` (where the outputs are `m,1`) rather than relying on a generic phrase; prove the whole-column gcd identity, not just the two-coordinate identity; and define the finite prime set as the divisors of the initial board product. Cite the knowledge-base entries on invariants/monovariants and divisor analysis. This route ranks first because it stays in integer arithmetic and has the shortest termination proof.

## valuation-vector-normal-form — APPROVE

This is also a complete route. The exponent-vector translation is exact. For selected vectors `x,y`, their contribution to `E` changes from `sum_p(x_p+y_p)` to `sum_p(max(x_p,y_p))`, so the loss is exactly `sum_p min(x_p,y_p)`. Hence overlap gives a strict `E` loss, while disjoint support gives `(0,x+y)` and drops `k`; `E+k` is strict. The coordinate subgroup mechanism is valid: for each prime separately, `min(r,s)` and `|r-s|` lie in `<r,s>`, and after ordering that coordinate, the smaller and difference recover the larger. At irreducibility there is at most one nonzero vector, while each prime in the chosen finite universe has positive invariant generator, so there is exactly one and its coordinates are forced.

Builder requirements: state that the coordinate ordering may depend on `p`; prove both subgroup inclusions; quantify the `E` loss; and avoid claiming invariance of a full vector lattice. Cite the knowledge-base invariant/monovariant entry. It ranks behind the direct route only because it introduces more notation for the same core mechanism, but it remains rigorous and readily buildable.

## colored-stack-euclidean — RETHINK

The mathematics described is not false, but this is not a genuinely rival approach: token colors and occupied boxes are exactly the exponent vectors, `T+B` is exactly `E+k`, and the per-color “common step” is exactly the same column-gcd invariant. The outline itself admits this correlation. Registering/building it would violate the one-slug/whole-rival diversity rule without closing a different gap. If retained in a later round, it should be treated as an exposition of `valuation-vector-normal-form`, not a separate population member.

## squarefree-layers-lift — RETHINK

The squarefree prelude does not establish the general problem, and the proposed multiplicity lift simply reintroduces the synchronized exponent-vector argument. Step 3 expressly leaves open whether it can avoid circularly importing the complete vector proof; no independent induction parameter and induction statement are supplied. Thus it is both under-specified at its load-bearing step and correlated with the same valuation-normal-form route. A genuinely distinct replacement would need a different global invariant or confluence mechanism rather than squarefree notation followed by the same coordinate gcd proof.

## Field assessment

The two survivors are sound but still strongly correlated: both terminate by a two-part mass/occupancy descent and identify the result by prime-exponent column gcds. For this relatively direct problem that shared core appears decisive rather than a current technical wall, so building both is reasonable as an arithmetic proof and a normal-form proof. If neither closes, the next round should demand a genuinely different framing rather than another colored/layered renaming.

build set: arithmetic-product-content, valuation-vector-normal-form