# Foundation F-neg — boundary sign of `g` in bucket (iii)

**Status:** CERTIFIED (round 12, `ll-dyadic-symdiff`; reviewer re-derived + verified 1548/1548).

## Statement
In bucket (iii) of the dyadic-symdiff framework (XY-partition `Q` of the interval, `R` a refinement of
`G_{n−1} = {1,2,…,2^{n−1}}` by `c_R ≥ 1` cuts, joint cut budget `c_Q + c_R ≤ n`),
`g(0⁺) := N_Q(0⁺) − N_R(0⁺) = c_Q − c_R − (n−1) ≤ −1`.

## Proof
`N_Q(0⁺) = |Q|` and `N_R(0⁺) = |R|` (every part is positive). With `|Q| = c_Q + 1` and
`|R| = n + c_R` (refining the `n`-piece `G_{n−1}` by `c_R` cuts),
`g(0⁺) = (c_Q+1) − (n+c_R) = c_Q − c_R − (n−1)`.
The budget `c_Q + c_R ≤ n` with `c_R ≥ 1` gives `c_Q ≤ n − 1`, so
`g(0⁺) ≤ (n−1) − 1 − (n−1) = −1`. ∎

## Scope
Foundation for the `Sub-3a` dichotomy: `g` is `≤ −1` on a right-neighbourhood of `0` while `∫g = 1 > 0`,
so `g` attains a positive value somewhere. NOT sufficient on its own for the `+1` (the abstract profile
`g=(−1,+2,0)` satisfies F-neg with `∫g=1` yet `A = ε < 1`); the residual needs the `ΣQ=2^n`
dyadic-staircase geometry.
