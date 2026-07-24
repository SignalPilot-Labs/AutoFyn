# Lemma J: a tie-free non-degenerate minimizer of f is monochromatic

**Status: CERTIFIED (round 3, reviewer). From `self-similar-recursion`.**
Reviewer verified the derivative logic (via certified Lemma I `cut-slide-derivative.md`) and the
monochromatic conclusion.

## Setup
Fix a cut pattern on `W_n = {2^0,…,2^n}`: original piece `2^k` is split into `r_k` sub-pieces
whose lengths are `≥0` and sum to `2^k`. `f = Σ_i σ_i b_i` (alternating sum) is affine on each
sort-chamber and continuous on the compact domain `K` (product of simplices), so `min_K f` is
attained (Weierstrass). Call a point **non-degenerate** if all sub-pieces are `>0` (interior of
`K`) and **tie-free** if all sub-piece values are distinct.

## Statement
If a local minimizer `P*` of `f` (over a fixed cut pattern) is non-degenerate and tie-free, then
every original piece is **monochromatic** (all its sub-pieces carry the same sign in `f`), whence
```
    f(P*) = Σ_{k=0}^n ε_k 2^k ∈ ℤ,   ε_k ∈ {±1}.
```

## Proof
Tie-free ⇒ every tie-block has size 1 ⇒ `s^↑(q)=s^↓(q)=σ(q)` (Lemma I). Non-degeneracy ⇒ every
cut is interior, so each can be slid both ways within `K`; at a local minimum both one-sided
derivatives are `≥0`. For adjacent sub-pieces `q_i,q_{i+1}` of one piece, Lemma I gives the
right-slide slope `σ(q_i)−σ(q_{i+1})≥0` and the left-slide slope `σ(q_{i+1})−σ(q_i)≥0`, forcing
`σ(q_i)=σ(q_{i+1})`. Chaining along the whole original piece, all its sub-pieces share one sign
`ε_k`. Their lengths sum to `2^k`, so their signed total is `ε_k·2^k`, independent of the
(possibly irrational) offsets; summing over `k` gives `f(P*)=Σ_k ε_k 2^k`. ∎

## Consequence (GAP-L, monochromatic case)
`f(P*)=Σ ε_k 2^k` has parity `ε_0 ≡ 1 (mod 2)` (all `k≥1` terms even), so it is an odd integer;
with `f≥0` (each sorted bracket `≥0`), an odd integer `≥0` is `≥1`. Hence `f(P*)≥1`.
This closes GAP-L on every **tie-free non-degenerate** minimizer; degenerate minimizers drop the
cut count (strong induction), and the remaining open case is a **non-degenerate minimizer pinned
at a rank tie** (stable P1 matched pair of arbitrary real value).
