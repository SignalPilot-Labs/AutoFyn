#!/usr/bin/env python3
"""Find supremum of min(7 caps) over the extreme regime (float, then refine)."""
import random
from fractions import Fraction as F

alpha = 1.0/15.0

def caps_f(u,v,w):
    z = alpha - 7*u - 4*v - 2*w
    a = alpha + u; b = 2*alpha+u+v; c = 4*alpha+2*u+v+w; d = 7*alpha+3*u+2*v+w+z
    return a,b,c,d, z

def mincap_f(u,v,w):
    a,b,c,d,z = caps_f(u,v,w)
    C1=a; C2=b-a; C3=c-b; C4=d-c
    C5=abs(a+b-c); C6=abs(a+c-d); C7=abs(a+b-d)
    return min(C1,C2,C3,C4,C5,C6,C7), (C1,C2,C3,C4,C5,C6,C7)

def is_extreme(u,v,w):
    a,b,c,d,z = caps_f(u,v,w)
    if not (a<=b<=c<=d): return False
    if a<=0: return False
    if not (d < 0.5): return False
    w_ = (c-a-b)-alpha
    return (w_ < -2*alpha) or (z < -2*alpha)

random.seed(0)
best = -1.0; bestc=None
for _ in range(2000000):
    u = random.uniform(-0.07, 0.06)
    v = random.uniform(-0.07, 0.06)
    w = random.uniform(-0.10, 0.02)
    if not is_extreme(u,v,w): continue
    m,caps = mincap_f(u,v,w)
    if m > best:
        best = m; bestc = (u,v,w, caps)

print("float best:", best, "alpha=", alpha)
print("cfg u,v,w=", bestc[:3])
print("caps=", bestc[3])

# local refinement: random walk
import copy
u,v,w,caps = bestc
step=0.001
for it in range(200000):
    du = random.uniform(-step,step); dv=random.uniform(-step,step); dw=random.uniform(-step,step)
    nu,nv,nw = u+du, v+dv, w+dw
    if not is_extreme(nu,nv,nw): continue
    m,_ = mincap_f(nu,nv,nw)
    if m > best:
        best=m; u,v,w=nu,nv,nw
print("after refine:", best, "u,v,w=",u,v,w)
a,b,c,d,z = caps_f(u,v,w)
print("a,b,c,d=",a,b,c,d, "d<.5?", d<0.5, "w<-2a?", (c-a-b)<-2*alpha, "z<-2a?", z<-2*alpha)
mc, caps = mincap_f(u,v,w)
print("caps:", caps, "argmin=", min(range(7), key=lambda i: caps[i]))

# Convert to Fraction and verify exactly
def to_frac(x): return F(x).limit_denominator(10**6)
uF,vF,wF = to_frac(u),to_frac(v),to_frac(w)
zF = F(1,15) - 7*uF - 4*vF - 2*wF
aF = F(1,15)+uF; bF=F(2,15)+uF+vF; cF=F(4,15)+2*uF+vF+wF; dF=F(7,15)+3*uF+2*vF+wF+zF
print("exact a,b,c,d=", (aF,bF,cF,dF), "sum=",aF+bF+cF+dF)
print("sorted?", aF<=bF<=cF<=dF, "d<1/2?", dF<F(1,2))
print("w<-2a?", (cF-aF-bF) < F(-2,15), "z<-2a?", zF < F(-2,15))
capsE = (aF, bF-aF, cF-bF, dF-cF, abs(aF+bF-cF), abs(aF+cF-dF), abs(aF+bF-dF))
print("exact caps:", capsE)
print("exact min:", min(capsE), "vs alpha", F(1,15))
