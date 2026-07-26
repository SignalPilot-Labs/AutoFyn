#!/usr/bin/env python3
"""Exact vertex enumeration per sub-case: find max of min(7 caps) as LP vertex.
For each sub-regime + sign-combo, enumerate vertices of the arrangement
(active = 3 of the boundary hyperplanes) and report min-cap at each.
We use fractions for exactness.
"""
from fractions import Fraction as F
from itertools import combinations

alpha = F(1,15)

# Variables (u,v,w). z = alpha - 7u - 4v - 2w.
# Each constraint is a linear half-space:  A*u + B*v + C*w  (op)  D
# We represent as (A,B,C, op, D, name).
# Boundaries (equalities) we can activate:
def make_boundaries(subregime, s5, s6, s7):
    # cap > alpha boundaries (cap = alpha) -- these are the "tight" faces:
    # C1 = alpha+u = alpha -> u = 0
    # C2 = alpha+v = alpha -> v = 0
    # C3 = 2a+u+w = alpha -> u+w = -alpha
    # C4 = 4a-6u-3v-2w = alpha -> 6u+3v+2w = 3a
    # C5: depends on sign. C5 = |alpha+w|. s5=+1: alpha+w (>=0) -> alpha+w=alpha -> w=0. s5=-1: -alpha-w -> -alpha-w=alpha -> w=-2a.
    # C6: |3a-7u-3v-2w|. s6=+1: 3a-7u-3v-2w=alpha -> 7u+3v+2w=2a. s6=-1: -(3a-7u-3v-2w)=alpha -> 7u+3v+2w=4a.
    # C7: |5a-6u-3v-w|. s7=+1: 5a-6u-3v-w=alpha -> 6u+3v+w=4a. s7=-1: -(5a-6u-3v-w)=alpha -> 6u+3v+w=6a.
    bnds = []
    bnds.append((1,0,0,'=',0,'C1=alpha:u=0'))
    bnds.append((0,1,0,'=',0,'C2=alpha:v=0'))
    bnds.append((1,0,1,'=',-alpha,'C3=alpha:u+w=-a'))
    bnds.append((6,3,2,'=',3*alpha,'C4=alpha:6u+3v+2w=3a'))
    if s5==1:
        bnds.append((0,0,1,'=',0,'C5+:w=0'))
    else:
        bnds.append((0,0,1,'=',-2*alpha,'C5-:w=-2a'))
    if s6==1:
        bnds.append((7,3,2,'=',2*alpha,'C6+:7u+3v+2w=2a'))
    else:
        bnds.append((7,3,2,'=',4*alpha,'C6-:7u+3v+2w=4a'))
    if s7==1:
        bnds.append((6,3,1,'=',4*alpha,'C7+:6u+3v+w=4a'))
    else:
        bnds.append((6,3,1,'=',6*alpha,'C7-:6u+3v+w=6a'))
    # sub-regime boundary
    if subregime==1:
        bnds.append((0,0,1,'=',-2*alpha,'S1:w=-2a'))
    else:
        bnds.append((7,4,2,'=',3*alpha,'S2:7u+4v+2w=3a'))
    # d=1/2 boundary
    bnds.append((8,4,2,'=',alpha,'d=1/2:8u+4v+2w=a'))
    # sort boundaries
    bnds.append((0,1,0,'=',-alpha,'a=b:v=-a'))
    bnds.append((1,0,1,'=',-2*alpha,'b=c:u+w=-2a'))
    bnds.append((6,3,2,'=',4*alpha,'c=d:6u+3v+2w=4a'))
    bnds.append((1,0,0,'=',-alpha,'a=0:u=-a'))
    return bnds

def solve3(b1,b2,b3):
    # solve (A1,B1,C1)u+(A2,B2,C2)v+(A3,B3,C3)w = (D1,D2,D3)
    import numpy as np
    M = [[b1[0],b1[1],b1[2]],[b2[0],b2[1],b2[2]],[b3[0],b3[1],b3[2]]]
    det = M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1]) - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0]) + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0])
    if det==0: return None
    # Cramer's rule with fractions
    def det3(m):
        return m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1]) - m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0]) + m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0])
    Mf = [[F(x) for x in row] for row in M]
    D = [b1[4], b2[4], b3[4]]
    sol=[]
    for col in range(3):
        Mc = [row[:] for row in Mf]
        for r in range(3):
            Mc[r][col]=D[r]
        sol.append(det3(Mc)/det3(Mf))
    return sol

def caps_at(u,v,w):
    z = alpha - 7*u - 4*v - 2*w
    a = alpha+u; b=2*alpha+u+v; c=4*alpha+2*u+v+w; d=7*alpha+3*u+2*v+w+z
    return a,b,c,d,z

def mincap(u,v,w):
    a,b,c,d,z = caps_at(u,v,w)
    return min(a, b-a, c-b, d-c, abs(a+b-c), abs(a+c-d), abs(a+b-d))

def feasible(u,v,w, subregime, s5,s6,s7, strict_caps=True):
    a,b,c,d,z = caps_at(u,v,w)
    if not (a<=b<=c<=d): return False
    if a<=0: return False
    if not (d < F(1,2)): return False
    caps = (a, b-a, c-b, d-c, abs(a+b-c), abs(a+c-d), abs(a+b-d))
    # all caps >= alpha (for vertex enumeration of the LP max-t, we want caps>=alpha feasible region)
    if strict_caps and any(c2 < alpha for c2 in caps): return False
    # sign consistency
    if s5==1 and (alpha+w) < 0: return False
    if s5==-1 and (alpha+w) > 0: return False
    if s6==1 and (3*alpha-7*u-3*v-2*w) < 0: return False
    if s6==-1 and (3*alpha-7*u-3*v-2*w) > 0: return False
    if s7==1 and (5*alpha-6*u-3*v-w) < 0: return False
    if s7==-1 and (5*alpha-6*u-3*v-w) > 0: return False
    # sub-regime (strict)
    if subregime==1 and not (w < -2*alpha): return False
    if subregime==2 and not (z < -2*alpha): return False
    return True

# For each sub-regime & sign combo, enumerate vertices = intersection of 3 boundary planes,
# keep those feasible (caps>=alpha, sign-consistent, sub-regime interior), compute min-cap.
for subregime in [1,2]:
    # determine which s5 values are sign-consistent with the sub-regime
    s5vals = [1,-1]
    for s5 in s5vals:
        for s6 in [1,-1]:
            for s7 in [1,-1]:
                # quick sign-consistency pre-check against sub-regime
                if subregime==1 and s5==1: continue  # w<-2a forces alpha+w<0 -> s5=-1
                bnds = make_boundaries(subregime,s5,s6,s7)
                best=None
                for idx in combinations(range(len(bnds)),3):
                    b1,b2,b3 = bnds[idx[0]],bnds[idx[1]],bnds[idx[2]]
                    sol = solve3(b1,b2,b3)
                    if sol is None: continue
                    u,v,w = sol
                    # check feasibility with caps>=alpha (LP max-t feasible region vertices)
                    if not feasible(u,v,w,subregime,s5,s6,s7, strict_caps=True):
                        continue
                    mc = mincap(u,v,w)
                    if best is None or mc > best[0]:
                        best=(mc, u,v,w, (b1[5],b2[5],b3[5]))
                if best is None:
                    print(f"S{subregime} s5={s5:+d} s6={s6:+d} s7={s7:+d}: NO feasible vertex with caps>=alpha  -> contradiction (max t<0)")
                else:
                    mc,u,v,w,active = best
                    print(f"S{subregime} s5={s5:+d} s6={s6:+d} s7={s7:+d}: max min-cap = {mc} = {float(mc):.6f}  (alpha={float(alpha):.6f}, margin={float(alpha-mc):.6f})")
                    print(f"     vertex u={u} v={v} w={w}; active={active}")
                    a,b,c,d,z = caps_at(u,v,w)
                    print(f"     a,b,c,d = {a},{b},{c},{d}; z={z}")
                    caps = (a, b-a, c-b, d-c, abs(a+b-c), abs(a+c-d), abs(a+b-d))
                    print(f"     caps = {caps}")
