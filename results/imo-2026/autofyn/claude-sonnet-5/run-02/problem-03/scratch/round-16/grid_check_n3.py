from fractions import Fraction as F
import itertools

D = {0:1,1:3,2:7,3:15,4:31}
def a(k): return F(2**k, D[k])

n = 3
D3 = D[3]
a3 = a(3)

def A_of(vals):
    s = sorted(vals, reverse=True)
    tot = F(0)
    for i,v in enumerate(s):
        tot += v if i%2==0 else -v
    return tot

def phi_bisect_top_k(pieces, k):
    # bisect top k, leave rest; Phi = (T + A(tail))/2
    tail = pieces[k:]
    T = sum(pieces)
    return (T + A_of(tail))/2

def phi_theoremA(pieces):
    p1 = pieces[0]
    T = sum(pieces)
    if p1 >= T - p1:
        return p1
    return None

def phi_theoremD_exact(pieces):
    # bisect p1,p4 (top and bottom), exact middle value via odd-run
    if len(pieces) < 2: return None
    p1, pm = pieces[0], pieces[-1]
    mid = pieces[1:-1]
    T = sum(pieces)
    # exact Phi_mid = A(mid) computed directly (mid untouched, sorted already)
    Amid = A_of(mid)
    return (p1+pm)/2 + (T - p1 - pm + Amid)/2 - (T-p1-pm)/2 + Amid  # simplify below
