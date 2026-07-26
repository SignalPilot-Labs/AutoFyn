#!/usr/bin/env python3
"""For each of the 8 sub-cases, check feasibility of 'all 7 caps > alpha'
via LP. If max-t < 0, the sub-case yields contradiction.

Variables: u, v, w (z = alpha - 7u - 4v - 2w).
We MAXIMIZE t subject to:
  each cap >= alpha + t   (we want to know the largest achievable min-cap-minus-alpha)
  sub-regime constraint (S1: w <= -2a-eps; S2: 7u+4v+2w >= 3a+eps -- use strict -> non-strict with small eps)
  sign constraints from the sub-case (signs of C5,C6,C7)
  sort constraints (implied, but enforce a<=b<=c<=d, a>0)
Use scipy.linprog (minimize -t).
"""
from scipy.optimize import linprog
import numpy as np
from fractions import Fraction as F

alpha = 1.0/15.0
EPS = 1e-9

# variable order: [u, v, w, t]
def cap_exprs(u,v,w):
    z = alpha - 7*u - 4*v - 2*w
    a = alpha + u; b = 2*alpha+u+v; c = 4*alpha+2*u+v+w; d = 7*alpha+3*u+2*v+w+z
    return a,b,c,d,z

# We express each cap as a linear function of (u,v,w) given the sign s5,s6,s7 in {+1,-1}:
# C5_signed = alpha + w        (this is -(a+b-c) = c-a-b... wait a+b-c = -(alpha+w). So a+b-c = -(alpha+w). |a+b-c|=|alpha+w|. With sign s5: if s5=+1 means alpha+w>=0 (cap = alpha+w); if s5=-1 means alpha+w<=0 (cap = -(alpha+w)=-alpha-w).
# C6_signed = 2*alpha+v+z = 3*alpha-7u-3v-2w   (a+c-d = -(2a+v+z), so |a+c-d|=|2a+v+z|=|3a-7u-3v-2w|)
# C7_signed = 4*alpha+u+v+w+z = 5*alpha-6u-3v-w  (a+b-d = -(4a+u+v+w+z), so |a+b-d| = |4a+u+v+w+z| = |5a-6u-3v-w|)

def solve(subregime, s5, s6, s7):
    # subregime: 1 or 2
    # maximize t s.t. caps >= alpha+t, sign constraints, subregime, sort, d<1/2 strict->eps
    # linprog minimizes c^T x. We minimize -t (x4).
    c = np.array([0.0,0.0,0.0,-1.0])
    A_ub=[]; b_ub=[]
    # cap lower bounds: cap >= alpha+t  ->  -(cap) <= -alpha - t
    # C1 = alpha+u
    A_ub.append([-1,0,0, 1]); b_ub.append(-alpha)  # -(alpha+u) <= -alpha-t -> -u + t <= 0? Let me redo.
    # We want: alpha+u >= alpha+t  -> u - t >= 0  -> -u + t <= 0
    A_ub[-1] = np.array([-1,0,0,1]); b_ub[-1]=0.0
    # C2 = alpha+v >= alpha+t -> v - t >= 0 -> -v+t<=0
    A_ub.append(np.array([0,-1,0,1])); b_ub.append(0.0)
    # C3 = 2a+u+w >= alpha+t -> u + w - t >= alpha - 2a+alpha... wait: 2a+u+w >= a+t -> u+w - t >= -a -> -(u+w)+t <= a
    A_ub.append(np.array([-1,0,-1,1])); b_ub.append(alpha)  # -(u+w) + t <= alpha
    # C4 = 3a+u+v+z = 4a-6u-3v-2w >= a+t -> -6u-3v-2w - t >= -3a -> 6u+3v+2w + t <= 3a
    A_ub.append(np.array([6,3,2,1])); b_ub.append(3*alpha)
    # C5 signed: s5*(alpha+w) >= alpha+t  (s5=+1: alpha+w>=a+t; s5=-1: -alpha-w>=a+t i.e. -w-t>=2a)
    if s5==1:
        A_ub.append(np.array([0,0,-1,1])); b_ub.append(0.0)  # w-t>=0? wait alpha+w>=a+t -> w - t >= 0 -> -w+t<=0
        A_ub[-1]=np.array([0,0,-1,1]); b_ub[-1]=0.0
    else:
        # -alpha - w >= alpha+t -> -w - t >= 2alpha -> w + t <= -2alpha
        A_ub.append(np.array([0,0,1,1])); b_ub.append(-2*alpha)
    # C6 signed: 3a-7u-3v-2w with sign s6
    if s6==1:
        # 3a-7u-3v-2w >= a+t -> -7u-3v-2w - t >= -2a -> 7u+3v+2w+t <= 2a
        A_ub.append(np.array([7,3,2,1])); b_ub.append(2*alpha)
    else:
        # -(3a-7u-3v-2w) >= a+t -> 7u+3v+2w - t >= 4a -> -7u-3v-2w+t <= -4a
        A_ub.append(np.array([-7,-3,-2,1])); b_ub.append(-4*alpha)
    # C7 signed: 5a-6u-3v-w with sign s7
    if s7==1:
        # 5a-6u-3v-w >= a+t -> -6u-3v-w -t >= -4a -> 6u+3v+w+t <= 4a
        A_ub.append(np.array([6,3,1,1])); b_ub.append(4*alpha)
    else:
        # -(5a-6u-3v-w) >= a+t -> 6u+3v+w - t >= 6a -> -6u-3v-w+t <= -6a
        A_ub.append(np.array([-6,-3,-1,1])); b_ub.append(-6*alpha)
    # sub-regime:
    if subregime==1:
        # w < -2a (strict) -> w <= -2a - eps
        A_ub.append(np.array([0,0,1,0])); b_ub.append(-2*alpha - EPS)
    else:
        # z < -2a -> alpha-7u-4v-2w < -2a -> 7u+4v+2w > 3a -> 7u+4v+2w >= 3a+eps
        A_ub.append(np.array([-7,-4,-2,0])); b_ub.append(-3*alpha - EPS)
    # d < 1/2 strict: 8u+4v+2w > a -> 8u+4v+2w >= a+eps  (u>z)
    A_ub.append(np.array([-8,-4,-2,0])); b_ub.append(-alpha - EPS)
    # sort: a<=b<=c<=d, a>0 -- these are implied but enforce to keep LP bounded
    # a<=b: v>=-a (v+alpha>=0) -> -v <= alpha
    A_ub.append(np.array([0,-1,0,0])); b_ub.append(alpha)
    # b<=c: u+w >= -2a -> -u-w <= 2a
    A_ub.append(np.array([-1,0,-1,0])); b_ub.append(2*alpha)
    # c<=d: 6u+3v+2w <= 4a
    A_ub.append(np.array([6,3,2,0])); b_ub.append(4*alpha)
    # a>0: u > -a -> -u < a -> -u <= a - eps
    A_ub.append(np.array([-1,0,0,0])); b_ub.append(alpha - EPS)

    A_ub = np.array(A_ub); b_ub=np.array(b_ub)
    # bounds: u,v,w unbounded; t unbounded (but we expect t<alpha)
    bounds=[(None,None)]*4
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')
    if not res.success:
        return None  # infeasible
    return res.fun  # = -t (we minimize -t, so t = -res.fun)

print("alpha =", alpha)
# Sub-regime 1: s5 forced +1 (since w<-2a -> alpha+w<0 -> |a+b-c| = -alpha-w, so s5=-1!! )
# Wait: w<-2a means alpha+w < -a <0, so |alpha+w| = -(alpha+w) = -alpha-w. So s5 = -1 (the negative branch).
# Let me recompute the explorer's claim. The explorer said w<-2a forces the |a+b-c| branch.
# C5 = |alpha+w|. If w<-2a then alpha+w<-a<0 so C5 = -alpha-w. Sign s5=-1.
# The branch is determined (s5=-1), and the condition C5>a is -alpha-w>a -> -w>2a (automatic from w<-2a).
# So in S1, s5 is FIXED to -1.
# In S2 (z<-2a), what's forced? Let me check: the explorer said for S2, combine with d>c+a.
# Let me first just brute force all 8 combos for each sub-regime and see which are feasible.

for subregime in [1,2]:
    print(f"--- sub-regime {subregime} ---")
    for s5 in [1,-1]:
        for s6 in [1,-1]:
            for s7 in [1,-1]:
                r = solve(subregime, s5, s6, s7)
                if r is None:
                    print(f"  s5={s5:+d} s6={s6:+d} s7={s7:+d}: INFEASIBLE (contradiction)")
                else:
                    t = -r
                    print(f"  s5={s5:+d} s6={s6:+d} s7={s7:+d}: feasible, max t = {t:.6f} (min-cap = {alpha+t:.6f})")
