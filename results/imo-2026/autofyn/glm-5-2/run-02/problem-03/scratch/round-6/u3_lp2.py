#!/usr/bin/env python3
"""Extract exact optimal vertex per sub-case via LP, identify active constraints,
then verify with fractions. Use scipy for the LP, then rationalize."""
from scipy.optimize import linprog
import numpy as np
from fractions import Fraction as F

alpha_f = 1.0/15.0
EPS = 1e-12

def solve_lp(subregime, s5, s6, s7, want_active=True):
    # maximize t s.t. caps >= alpha+t, sign-consistency, sub-regime strict (use eps), sort, d<1/2 strict
    # vars [u,v,w,t]; minimize -t
    c = np.array([0,0,0,-1.0])
    A=[]; b=[]; names=[]
    def add(row, rhs, name):
        A.append(row); b.append(rhs); names.append(name)
    # C1>=alpha+t: u-t>=0 -> -u+t<=0
    add([-1,0,0,1], 0.0, 'C1>=a+t')
    # C2>=alpha+t: -v+t<=0
    add([0,-1,0,1], 0.0, 'C2>=a+t')
    # C3=2a+u+w>=a+t: u+w-t>=-a -> -(u+w)+t<=a
    add([-1,0,-1,1], alpha_f, 'C3>=a+t')
    # C4=4a-6u-3v-2w>=a+t: 6u+3v+2w+t<=3a
    add([6,3,2,1], 3*alpha_f, 'C4>=a+t')
    # C5
    if s5==1:
        # alpha+w>=a+t: w-t>=0 -> -w+t<=0
        add([0,0,-1,1], 0.0, 'C5+>=a+t')
        # sign: alpha+w>=0 -> -w<=alpha
        add([0,0,-1,0], alpha_f, 'sign C5+')
    else:
        # -alpha-w>=a+t: -w-t>=2a -> w+t<=-2a
        add([0,0,1,1], -2*alpha_f, 'C5->=a+t')
        # sign: alpha+w<=0 -> w<=-alpha
        add([0,0,1,0], -alpha_f, 'sign C5-')
    # C6
    if s6==1:
        add([7,3,2,1], 2*alpha_f, 'C6+>=a+t')
        add([7,3,2,0], 3*alpha_f, 'sign C6+')  # 3a-7u-3v-2w>=0 -> 7u+3v+2w<=3a
    else:
        add([-7,-3,-2,1], -4*alpha_f, 'C6->=a+t')  # 7u+3v+2w-3a>=a+t -> -7u-3v-2w+t<=-4a
        add([-7,-3,-2,0], -4*alpha_f, 'sign C6-')  # 7u+3v+2w>=3a -> -7u-3v-2w<=-3a... wait sign s6=-1: 3a-7u-3v-2w<=0 -> 7u+3v+2w>=3a -> -7u-3v-2w<=-3a
        # fix:
        A[-2]=np.array([-7,-3,-2,0]); b[-2]=-3*alpha_f; names[-2]='sign C6-'
    # C7
    if s7==1:
        add([6,3,1,1], 4*alpha_f, 'C7+>=a+t')  # 5a-6u-3v-w>=a+t -> 6u+3v+w+t<=4a
        add([6,3,1,0], 5*alpha_f, 'sign C7+')  # 5a-6u-3v-w>=0 -> 6u+3v+w<=5a
    else:
        add([-6,-3,-1,1], -6*alpha_f, 'C7->=a+t')  # 6u+3v+w-5a>=a+t -> -6u-3v-w+t<=-6a
        add([-6,-3,-1,0], -5*alpha_f, 'sign C7-')  # 6u+3v+w>=5a -> -6u-3v-w<=-5a
    # sub-regime strict
    if subregime==1:
        add([0,0,1,0], -2*alpha_f - 1e-9, 'S1 w<-2a')
    else:
        add([-7,-4,-2,0], -3*alpha_f - 1e-9, 'S2 z<-2a')
    # d<1/2 strict
    add([-8,-4,-2,0], -alpha_f - 1e-9, 'd<1/2')
    # sort
    add([0,-1,0,0], alpha_f, 'a<=b')
    add([-1,0,-1,0], 2*alpha_f, 'b<=c')
    add([6,3,2,0], 4*alpha_f, 'c<=d')
    add([-1,0,0,0], alpha_f - 1e-9, 'a>0')
    A=np.array(A); b=np.array(b)
    res = linprog(c, A_ub=A, b_ub=b, bounds=[(None,None)]*4, method='highs')
    if not res.success: return None
    u,v,w,t = res.x
    active = [names[i] for i in range(len(A)) if abs(A[i]@res.x - b[i])<1e-7]
    return {'t':t, 'u':u,'v':v,'w':w, 'mincap':alpha_f+t, 'active':active}

for subregime in [1,2]:
    s5list = [-1] if subregime==1 else [1,-1]
    for s5 in s5list:
        for s6 in [1,-1]:
            for s7 in [1,-1]:
                r = solve_lp(subregime,s5,s6,s7)
                if r is None:
                    print(f"S{subregime} s5={s5:+d} s6={s6:+d} s7={s7:+d}: INFEASIBLE")
                else:
                    print(f"S{subregime} s5={s5:+d} s6={s6:+d} s7={s7:+d}: t={r['t']:.6f} mincap={r['mincap']:.6f} (alpha={alpha_f:.6f})")
                    print(f"    u={r['u']:.6f} v={r['v']:.6f} w={r['w']:.6f}")
                    print(f"    active: {r['active']}")
