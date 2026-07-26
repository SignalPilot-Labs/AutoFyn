# nonneg-grid-kronecker (number theory tool)

**Statement.** For irrational `α>0`, the set `{nα − m : n,m ∈ Z_{≥0}}` is dense in R. Moreover, the witnessing pairs can be taken with both `n` and `m` arbitrarily large.

**Proof.** Kronecker/Weyl equidistribution: for irrational `α`, the fractional parts `{{kα}:k≥1}` are dense in `[0,1)`. Fix `T∈R`, `ε>0`, lower bound `M`. Choose arbitrarily large `k` with `|{kα}−{T}|<ε` (circle metric); set `n:=k`, `m:=⌊kα⌋−⌊T⌋`. Then `kα−(⌊kα⌋−⌊T⌋)` is within `ε` of `T`. For `k` large (which equidistribution allows), `⌊kα⌋→∞` (since `α>0`), so `m→∞` and `m≥M`; also `n=k≥M`. ∎

**Certified:** round 1, proof-reviewer. Used in `diagonal-diophantine-kill` §2.1 to drive the RHS of (★★★) to 0 along forward orbits with irrational displacement ratio.
