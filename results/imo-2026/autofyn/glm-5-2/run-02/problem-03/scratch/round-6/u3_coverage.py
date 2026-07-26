#!/usr/bin/env python3
"""Check coverage of 7-cap family on full d<1/2 regime.
Also test realizability of |b+c-d| cap.
"""
from fractions import Fraction as F
import random

alpha = F(1,15)

def uvw_to_abcd(u,v,w):
    z = alpha - 7*u - 4*v - 2*w
    a = alpha+u; b=2*alpha+u+v; c=4*alpha+2*u+v+w; d=7*alpha+3*u+2*v+w+z
    return a,b,c,d,z

def is_sorted(a,b,c,d): return a<=b<=c<=d and a>0

def min7(a,b,c,d):
    return min(a, b-a, c-b, d-c, abs(a+b-c), abs(a+c-d), abs(a+b-d))

random.seed(7)
viol_extreme=0; n_extreme=0; worst=F(0); wcfg=None
viol_full=0; n_full=0; worst_full=F(0); wcfg_full=None
viol_ne=0; n_ne=0; worst_ne=F(0); wcfg_ne=None
viol_gap=0; n_gap=0
def rand_config():
    # 4 pieces summing to 1, sorted a<=b<=c<=d, d<1/2
    # generate 3 cut points in (0,1), sort
    xs=sorted([random.random() for _ in range(3)])
    a=F(xs[0]).limit_denominator(2000)
    b=F(xs[1]-xs[0]).limit_denominator(2000)
    c=F(xs[2]-xs[1]).limit_denominator(2000)
    d=1-a-b-c
    return a,b,c,d
for _ in range(400000):
    a,b,c,d = rand_config()
    if not is_sorted(a,b,c,d): continue
    if not (d < F(1,2)): continue
    u=a-alpha; v=b-a-alpha; w=c-a-b-alpha; z=d-b-c-alpha
    in_gap = (u>0 and v>0 and w>0 and z>0)
    extreme = (w < -2*alpha) or (z < -2*alpha)
    nonextreme = (not extreme) and (not in_gap)
    m = min7(a,b,c,d)
    n_full+=1
    if m > alpha: viol_full+=1
    if m > worst_full: worst_full=m; wcfg_full=(a,b,c,d,u,v,w,z)
    if extreme:
        n_extreme+=1
        if m > alpha: viol_extreme+=1
        if m > worst: worst=m; wcfg=(a,b,c,d,u,v,w,z)
    if nonextreme:
        n_ne+=1
        if m > alpha: viol_ne+=1
        if m > worst_ne: worst_ne=m; wcfg_ne=(a,b,c,d,u,v,w,z)
    if in_gap:
        n_gap+=1
        if m > alpha: viol_gap+=1

print(f"full d<1/2: {n_full} configs, violations(min7>alpha)={viol_full}, worst={worst_full}={float(worst_full):.6f}")
print(f"  extreme (w<-2a or z<-2a): {n_extreme} cfg, viol={viol_extreme}, worst={worst}={float(worst):.6f}")
print(f"  non-extreme non-gap: {n_ne} cfg, viol={viol_ne}, worst={worst_ne}={float(worst_ne):.6f}")
print(f"  gap G (all u,v,w,z>0): {n_gap} cfg, viol(min7>alpha)={viol_gap}")
if wcfg_ne:
    print("  non-extreme worst cfg:", wcfg_ne)

# Also check the |b+c-d| value vs realizability: in z in [-2a,0], is min7<=alpha?
viol_z=0; n_z=0; worst_z=F(0)
for _ in range(400000):
    a,b,c,d = rand_config()
    if not is_sorted(a,b,c,d): continue
    if not (d < F(1,2)): continue
    u=a-alpha; v=b-a-alpha; w=c-a-b-alpha; z=d-b-c-alpha
    # z in [-2a, 0], w >= -2a, u,v,w > 0 (so not covered by u<=0/v<=0/w-extreme)
    if not (z <= 0 and z >= -2*alpha and w >= -2*alpha and u>0 and v>0 and w>0): continue
    n_z+=1
    m=min7(a,b,c,d)
    if m > alpha: viol_z+=1
    if m > worst_z: worst_z=m
print(f"z in [-2a,0] sub-case (u,v,w>0, w>=-2a): {n_z} cfg, 7cap-viol={viol_z}, worst={worst_z}={float(worst_z):.6f}")
