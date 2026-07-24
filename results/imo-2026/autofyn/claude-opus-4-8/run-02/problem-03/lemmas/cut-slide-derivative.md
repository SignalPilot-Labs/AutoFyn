# Lemma I: exact one-sided cut-slide derivative of the alternating sum (valid at ties)

**Status: CERTIFIED (round 3, reviewer). From `self-similar-recursion`.**
Reviewer re-derived the block-contribution algebra from scratch and confirmed the one-sided
slopes numerically (increase/decrease a tied piece: measured slopes `−1`, `+1` match
`s^↑=σ_{a_l}`, `−s^↓=−σ_{b_l}`).

## Setup
For a finite multiset sorted descending `b_1≥b_2≥…`, `f = Σ_i σ_i b_i` with `σ_i=(−1)^{i+1}`.
Group equal values into **tie-blocks**; block `l` occupies ranks `[a_l,b_l]`. For a piece `q` of
value `x` in block `l`, set `s^↑(q):=σ_{a_l}` (sign at the top rank of the block) and
`s^↓(q):=σ_{b_l}` (sign at the bottom rank).

## Statement
Holding all other pieces fixed, `f` has one-sided derivatives
`∂f/∂(increase q) = s^↑(q)` and `∂f/∂(decrease q) = −s^↓(q)`.
Consequently, sliding the cut between spatially-adjacent sub-pieces `q_i` (left), `q_{i+1}`
(right) of one original piece **right** by `ε` (grow `q_i`, shrink `q_{i+1}`) changes `f` by
`(s^↑(q_i) − s^↓(q_{i+1}))ε`, and **left** by `(s^↑(q_{i+1}) − s^↓(q_i))ε`.

## Proof
Increase `q=x` by `ε`: it rises to the top of its block (rank `a_l`), the other block members
keep value `x` at ranks `a_l+1,…,b_l`. The block's contribution changes from
`Σ_{i=a_l}^{b_l} σ_i x` to `σ_{a_l}(x+ε) + Σ_{i=a_l+1}^{b_l} σ_i x`, a net change `σ_{a_l}ε`.
Decreasing `q` by `ε` sends it to rank `b_l`: change `σ_{b_l}(x−ε) − σ_{b_l}x = −σ_{b_l}ε`, i.e.
`∂f/∂(decrease) = −σ_{b_l} = −s^↓`. The two-sided slide slopes add the two single-piece changes. ∎
