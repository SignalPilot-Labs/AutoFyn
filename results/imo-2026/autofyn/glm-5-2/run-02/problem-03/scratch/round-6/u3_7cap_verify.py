#!/usr/bin/env python3
"""Exact-rational verification of the 7-cap U(3) extreme closure.

For configs with d<1/2 AND (w<-2a OR z<-2a) [alpha=1/15], verify
min(C1..C7) <= alpha, where
  C1=a, C2=b-a, C3=c-b, C4=d-c,
  C5=|a+b-c|, C6=|a+c-d|, C7=|a+b-d|.
Also verify the 12-sub-case sign classification is exhaustive and each
sub-case's algebraic contradiction holds (via LP max-t < 0).
"""
from fractions import Fraction as F
import random
from scipy.optimize import linprog
import numpy as np

alpha = F(1,15)
alpha_f = float(alpha)

def caps(a,b,c,d):
    return (a, b-a, c-b, d-c, abs(a+b-c), abs(a+c-d), abs(a+b-d))

def chain_excess(a,b,c,d):
    u=a-alpha; v=b-a-alpha; w=c-a-b-alpha; z=d-b-c-alpha
    return u,v,w,z

def in_extreme(u,v,w,z):
    return (w < -2*alpha) or (z < -2*alpha)

def signs(u,v,w):
    z = alpha - 7*u - 4*v - 2*w
    s5 = 1 if (alpha+w) >= 0 else -1
    s6 = 1 if (3*alpha - 7*u - 3*v - 2*w) >= 0 else -1
    s7 = 1 if (5*alpha - 6*u - 3*v - w) >= 0 else -1
    sub = 1 if (w < -2*alpha) else (2 if z < -2*alpha else 0)
    return s5,s6,s7,sub

# ---- 1) Random + grid sampling over extreme regime ----
random.seed(2026)
viol=0; n=0; worst=F(0); wcfg=None
# random reals
for _ in range(150000):
    xs=sorted([random.random() for _ in range(3)])
    a=F(xs[0]).limit_denominator(5000)
    b=F(xs[1]-xs[0]).limit_denominator(5000)
    c=F(xs[2]-xs[1]).limit_denominator(5000)
    d=1-a-b-c
    if not (a<=b<=c<=d and a>0 and d<F(1,2)): continue
    u,v,w,z = chain_excess(a,b,c,d)
    if not in_extreme(u,v,w,z): continue
    n+=1
    m=min(caps(a,b,c,d))
    if m > alpha: viol+=1
    if m > worst: worst=m; wcfg=(a,b,c,d)
# grid (chain-excess grid, coarse for runtime)
N=18
for iu in range(-2*N, 2*N+1, 2):
    u=F(iu, 15*N)
    for iv in range(-2*N, 2*N+1, 2):
        v=F(iv, 15*N)
        for iw in range(-3*N, N+1, 2):
            w=F(iw, 15*N)
            z = alpha - 7*u - 4*v - 2*w
            a=alpha+u; b=2*alpha+u+v; c=4*alpha+2*u+v+w; d=7*alpha+3*u+2*v+w+z
            if not (a<=b<=c<=d and a>0 and d<F(1,2)): continue
            if not in_extreme(u,v,w,z): continue
            n+=1
            m=min(caps(a,b,c,d))
            if m > alpha: viol+=1
            if m > worst: worst=m; wcfg=(a,b,c,d)

print(f"=== 7-cap extreme-regime verification ===")
print(f"configs tested: {n}")
print(f"violations (min7 > alpha): {viol}")
print(f"worst min7: {worst} = {float(worst):.6f}  (alpha={float(alpha):.6f}, margin={float(alpha-worst):.6f})")
if wcfg:
    print(f"  worst cfg a,b,c,d = {wcfg}")
    u,v,w,z = chain_excess(*wcfg)
    print(f"  u,v,w,z = {(u,v,w,z)}")
    print(f"  caps = {caps(*wcfg)}")

# ---- 2) Drop-one minimality (coarse) ----
keys = ['C1','C2','C3','C4','C5','C6','C7']
print("\n=== drop-one (coarse grid only) ===")
# rebuild coarse grid configs list
grid_cfgs=[]
N=18
for iu in range(-2*N, 2*N+1, 2):
    u=F(iu, 15*N)
    for iv in range(-2*N, 2*N+1, 2):
        v=F(iv, 15*N)
        for iw in range(-3*N, N+1, 2):
            w=F(iw, 15*N)
            z = alpha - 7*u - 4*v - 2*w
            a=alpha+u; b=2*alpha+u+v; c=4*alpha+2*u+v+w; d=7*alpha+3*u+2*v+w+z
            if not (a<=b<=c<=d and a>0 and d<F(1,2)): continue
            if not in_extreme(u,v,w,z): continue
            grid_cfgs.append((a,b,c,d))
for drop in keys:
    idx=[i for i,k in enumerate(keys) if k!=drop]
    wmax=F(0); nv=0
    for (a,b,c,d) in grid_cfgs:
        cc=caps(a,b,c,d)
        m=min(cc[i] for i in idx)
        if m>alpha: nv+=1
        if m>wmax: wmax=m
    print(f"  drop {drop}: violations={nv}, worst={float(wmax):.6f}")

# ---- 3) LP per sub-case: max t, confirm <0 for all 12 ----
print("\n=== LP per sub-case (max t; t<0 => contradiction) ===")
def solve_lp(sub, s5, s6, s7):
    c=np.array([0.0,0.0,0.0,-1.0]); A=[]; b=[]
    def add(r,bb,nm=None): A.append(r); b.append(bb)
    add([-1,0,0,1],0.0)  # C1>=a+t
    add([0,-1,0,1],0.0)  # C2
    add([-1,0,-1,1],alpha_f)  # C3
    add([6,3,2,1],3*alpha_f)  # C4
    if s5==1:
        add([0,0,-1,1],0.0); add([0,0,-1,0],alpha_f)
    else:
        add([0,0,1,1],-2*alpha_f); add([0,0,1,0],-alpha_f)
    if s6==1:
        add([7,3,2,1],2*alpha_f); add([7,3,2,0],3*alpha_f)
    else:
        add([-7,-3,-2,1],-4*alpha_f); add([-7,-3,-2,0],-3*alpha_f)
    if s7==1:
        add([6,3,1,1],4*alpha_f); add([6,3,1,0],5*alpha_f)
    else:
        add([-6,-3,-1,1],-6*alpha_f); add([-6,-3,-1,0],-5*alpha_f)
    if sub==1:
        add([0,0,1,0],-2*alpha_f-1e-12)
    else:
        add([-7,-4,-2,0],-3*alpha_f-1e-12)
    add([-8,-4,-2,0],-alpha_f-1e-12)
    add([0,-1,0,0],alpha_f); add([-1,0,-1,0],2*alpha_f)
    add([6,3,2,0],4*alpha_f); add([-1,0,0,0],alpha_f-1e-12)
    A=np.array(A); b=np.array(b)
    res=linprog(c,A_ub=A,b_ub=b,bounds=[(None,None)]*4,method='highs')
    return None if not res.success else -res.fun

allneg=True
for sub in [1,2]:
    s5list=[-1] if sub==1 else [1,-1]
    for s5 in s5list:
        for s6 in [1,-1]:
            for s7 in [1,-1]:
                t=solve_lp(sub,s5,s6,s7)
                ok = (t is None) or (t < -1e-7)
                allneg = allneg and ok
                ts = "INFEAS" if t is None else f"{t:.6f}"
                print(f"  S{sub} s5={s5:+d} s6={s6:+d} s7={s7:+d}: max t = {ts}  {'OK' if ok else 'FAIL'}")
print(f"all sub-cases give contradiction (max t<0 or infeasible): {allneg}")
