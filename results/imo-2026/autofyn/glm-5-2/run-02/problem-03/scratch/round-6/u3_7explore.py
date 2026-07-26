#!/usr/bin/env python3
"""Explore the 7-cap contradiction for U(3) extreme sub-cases.

Caps (a<=b<=c<=d, a+b+c+d=1, alpha=1/15):
  C1 = a
  C2 = b-a
  C3 = c-b
  C4 = d-c
  C5 = |a+b-c|
  C6 = |a+c-d|
  C7 = |a+b-d|

Chain excesses: u=a-a, v=(b-a)-a, w=(c-a-b)-a, z=(d-b-c)-a
  a = alpha+u; b = 2a+u+v; c = 4a+2u+v+w; d = 7a+3u+2v+w+z
  identity: 7u+4v+2w+z = alpha
  d<1/2  <=>  u>z  <=>  8u+4v+2w > alpha
  w<-2a  <=>  c < a+b-2a
  z<-2a  <=>  d < b+c-2a

Express caps in (u,v,w) [with z=alpha-7u-4v-2w]:
  C1 = alpha+u
  C2 = alpha+v
  C3 = 2a+u+w
  C4 = 3a+u+v+z = 3a+u+v+alpha-7u-4v-2w = 4a-6u-3v-2w
  C5 = |alpha+w|
  C6 = |2a+v+z| = |2a+v+alpha-7u-4v-2w| = |3a-7u-3v-2w|
  C7 = |4a+u+v+w+z| = |4a+u+v+w+alpha-7u-4v-2w| = |5a-6u-3v-w|
"""
from fractions import Fraction as F
import itertools, random

alpha = F(1, 15)

def caps_from_uvw(u, v, w):
    z = alpha - 7*u - 4*v - 2*w
    a = alpha + u
    b = 2*alpha + u + v
    c = 4*alpha + 2*u + v + w
    d = 7*alpha + 3*u + 2*v + w + z
    # sanity
    assert a+b+c+d == 1
    return {
        'a': a, 'b': b, 'c': c, 'd': d, 'u':u, 'v':v, 'w':w, 'z':z,
        'C1': a,
        'C2': b-a,
        'C3': c-b,
        'C4': d-c,
        'C5': abs(a+b-c),
        'C6': abs(a+c-d),
        'C7': abs(a+b-d),
    }

# Generate extreme-regime configs: d<1/2 and (w<-2a or z<-2a), with a<=b<=c<=d.
# We sample (u,v,w) and filter.
def is_valid_config(uvw):
    C = caps_from_uvw(*uvw)
    a,b,c,d = C['a'],C['b'],C['c'],C['d']
    if not (a<=b<=c<=d): return False
    if not (a>0): return False
    if not (d < F(1,2)): return False
    if not (C['w'] < -2*alpha or C['z'] < -2*alpha): return False
    return True

random.seed(12345)
extreme_configs = []
# random reals
for _ in range(200000):
    u = F(random.randint(-100,100), 1500)
    v = F(random.randint(-100,100), 1500)
    w = F(random.randint(-300,100), 1500)
    if is_valid_config((u,v,w)):
        extreme_configs.append((u,v,w))
    if len(extreme_configs) >= 5000: break

# grid (coarse to keep runtime bounded)
N = 24
for iu in range(-3*N, 3*N+1, 2):
    u = F(iu, 15*N)
    for iv in range(-3*N, 3*N+1, 2):
        v = F(iv, 15*N)
        for iw in range(-3*N, N+1, 2):
            w = F(iw, 15*N)
            if is_valid_config((u,v,w)):
                extreme_configs.append((u,v,w))

print("total extreme configs:", len(extreme_configs))

# Check 7-cap claim
viol = 0
worst = F(0)
worst_cfg = None
for uvw in extreme_configs:
    C = caps_from_uvw(*uvw)
    m = min(C['C1'],C['C2'],C['C3'],C['C4'],C['C5'],C['C6'],C['C7'])
    if m > alpha:
        viol += 1
    if m > worst:
        worst = m
        worst_cfg = (uvw, C)
print("violations (min>alpha):", viol)
print("worst min-cap:", worst, " = float", float(worst))
print("alpha =", float(alpha), "margin =", float(alpha - worst))
if worst_cfg:
    uvw, C = worst_cfg
    print("worst cfg u,v,w,z =", (C['u'],C['v'],C['w'],C['z']))
    print("  a,b,c,d =", (C['a'],C['b'],C['c'],C['d']))
    for k in ['C1','C2','C3','C4','C5','C6','C7']:
        print(f"  {k} = {C[k]} = {float(C[k]):.5f}")

# Check drop-one 6-cap subsets
caps_keys = ['C1','C2','C3','C4','C5','C6','C7']
for drop in caps_keys:
    keys = [k for k in caps_keys if k!=drop]
    wmax = F(0)
    wcfg = None
    nviol = 0
    for uvw in extreme_configs:
        C = caps_from_uvw(*uvw)
        m = min(C[k] for k in keys)
        if m > alpha: nviol += 1
        if m > wmax:
            wmax = m; wcfg = (uvw, C)
    print(f"drop {drop}: violations={nviol}, worst={float(wmax):.5f} (alpha={float(alpha):.5f})")
