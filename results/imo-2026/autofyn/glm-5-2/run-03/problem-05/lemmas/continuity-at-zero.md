# continuity-at-zero (IMO 2026 P5)

**Statement.** Under the master bound (★) of this problem (with `g:=f−id`, `g≥0`): if `g(a)=0` for some `a>0`, then `g(x)→0` as `x→a`. Concretely, `g(x) ≤ (x−a)²/(3a)` for `|x−a|<a/2`.

**Proof.** Set `y=a` in (★): `|g(x)−0|·(2x+2a+g(x)+0) ≤ (x−a−0)²=(x−a)²`. For `|x−a|<a/2` we have `x>a/2>0`, so `2x+2a+g(x) ≥ 2x+2a > a+2a = 3a` (using `g(x)≥0`). Hence `0 ≤ g(x) ≤ (x−a)²/(3a)→0`. ∎

**Certified:** round 1, proof-reviewer. Used in `diagonal-diophantine-kill` §3 (edge case `d₁=0`) and in `lipschitz-connectedness` §5 (openness of `Z`). Note this is the `O(h²)` *local* case of (★), not the main Diophantine kill — no circularity.
