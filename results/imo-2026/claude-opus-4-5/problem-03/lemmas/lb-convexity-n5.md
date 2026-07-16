# Lemma: LB(x,T) Convexity (n=5)

## Statement

For n=5 and any fixed (2,1,1) or (2,2,1) template T, the function LB(x,T) = (sum of 5 largest of 10 pieces after XY's cuts) is convex in the configuration x = (P_1, ..., P_6).

## Proof

**Step 1: Piece sizes are linear in x.**

Each output piece after XY's template T is applied is a linear function of the input piece sizes (P_1, ..., P_6). Specifically:
- Halving: P_H/2 is linear in P_H
- Cutting at position c (where c is linear in piece sizes): creates pieces c and P_i - c, both linear in x
- Unchanged pieces: P_i is trivially linear

For (2,1,1) templates with "copy" cut positions (cutting at positions equal to other piece sizes), all 10 output pieces are linear in (P_1, ..., P_6).

**Step 2: LB = sum of 5 largest of 10 pieces.**

After XY's template creates 10 pieces, LB picks the 5 largest by greedy optimality. Thus:

LB(x,T) = max_{S subset of {1,...,10}, |S|=5} sum_{i in S} piece_i(x)

where the max is over all C(10,5) = 252 subsets S of size 5.

**Step 3: Maximum of linear functions is convex.**

Each sum_{i in S} piece_i(x) is a linear function of x (sum of linear functions is linear).

The function LB(x,T) = max over 252 such linear functions is convex, because the pointwise maximum of any family of convex (in particular, linear) functions is convex.

*Formal justification:* For convex functions f_1, ..., f_k, the function f(x) = max_i f_i(x) satisfies the convexity condition:

f(lambda*x + (1-lambda)*y) = max_i f_i(lambda*x + (1-lambda)*y)
                          <= max_i [lambda*f_i(x) + (1-lambda)*f_i(y)]     (by convexity of each f_i)
                          <= lambda*max_i f_i(x) + (1-lambda)*max_i f_i(y)  (standard max inequality)
                          = lambda*f(x) + (1-lambda)*f(y)

QED.

## Corollary

For each template T, the coverage set C_T = {x : LB(x,T) <= c(5)} is convex (sublevel set of a convex function).

## Where Proved

n5-lp-direct.md and n5-convex-coverage.md (Round 17)

## Certified

Round 17 by proof-reviewer. Mathematically sound - maximum of affine functions is convex is a standard result in convex analysis.
