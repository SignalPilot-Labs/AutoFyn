from fractions import Fraction as F
import random

def phi(S):
    S = sorted(S, reverse=True)
    return sum(S[i] for i in range(0,len(S),2))

def a(n):
    return F(2**n, 2**(n+1)-1)

def refine(pcs, cuts, rng):
    pcs = list(pcs)
    for _ in range(cuts):
        idx = rng.randrange(len(pcs))
        x = pcs[idx]
        t = F(rng.randint(1,99),100)
        aa = x*t; bb = x-aa
        if aa==0 or bb==0: continue
        pcs[idx]=aa; pcs.append(bb)
    return pcs

rng = random.Random(7)
# Theorem D' identity
for trial in range(2000):
    m = rng.randint(2,7)
    pieces = sorted([F(rng.randint(1,50),rng.randint(1,50)) for _ in range(m)], reverse=True)
    p1 = pieces[0]; pm = pieces[-1]; mid = pieces[1:-1]
    cuts = rng.randint(0, max(0,len(mid)))
    Mp = refine(mid, cuts, rng)
    combined = [p1/2,p1/2,pm/2,pm/2] + Mp
    lhs = phi(combined)
    rhs = (p1+pm)/2 + phi(Mp)
    assert lhs==rhs, (pieces, Mp, lhs, rhs)
print("Theorem D' identity: OK")

# Theorem E identity
for trial in range(2000):
    m = rng.randint(3,7)
    pieces = sorted([F(rng.randint(1,50),rng.randint(1,50)) for _ in range(m)], reverse=True)
    p1,p2 = pieces[0],pieces[1]; rest = pieces[2:]
    cuts = rng.randint(0, max(0,len(rest)))
    Mp = refine(rest, cuts, rng)
    combined = [p1/2,p1/2,p2/2,p2/2] + Mp
    lhs = phi(combined)
    rhs = (p1+p2)/2 + phi(Mp)
    assert lhs==rhs, (pieces, Mp, lhs, rhs)
print("Theorem E identity: OK")

# Theorem B_k identity (peel p1 against p_k)
for trial in range(2000):
    m = rng.randint(2,7)
    pieces = sorted([F(rng.randint(1,50),rng.randint(1,50)) for _ in range(m)], reverse=True)
    k = rng.randint(1,m-1)  # index 1..m-1 (0-based for p_2..p_m)
    pk = pieces[k]
    wk = pieces[0]-pk
    Sprime = [wk] + [pieces[i] for i in range(1,m) if i!=k]
    cuts = rng.randint(0,max(0,len(Sprime)-1))
    Mp = refine(Sprime, cuts, rng)
    combined = [pk,pk] + Mp
    lhs = phi(combined)
    rhs = pk + phi(Mp)
    assert lhs==rhs, (pieces,k,Mp,lhs,rhs)
print("Theorem B_k identity: OK")

# s* threshold formula and equal-pieces insufficiency check
for n in range(2,20):
    D_n = 2**(n+1)-1
    D_nm2 = 2**(n-1)-1
    a_n = F(2**n, D_n)
    a_nm2 = F(2**(n-2), D_nm2)
    sstar = F(3,2)*a_n
    # derive from scratch: solve a_{n-2} T + s(1/2-a_{n-2}) = a_n T at T=1
    sstar2 = (a_n - a_nm2)/(F(1,2)-a_nm2)
    assert sstar==sstar2, (n,sstar,sstar2)
    # equal pieces test
    s_equal = F(2,n+1)
    assert s_equal < sstar, (n, s_equal, sstar)
print("s* formula and equal-pieces insufficiency: OK n=2..19")

# Theorem A (Full-Match Achievability)
def phi2(S):
    S=sorted(S,reverse=True)
    return sum(S[i] for i in range(0,len(S),2))
for trial in range(2000):
    m = rng.randint(2,7)
    pieces = sorted([F(rng.randint(1,50),rng.randint(1,50)) for _ in range(m)], reverse=True)
    T = sum(pieces)
    p1 = pieces[0]
    if p1 < T-p1: continue
    v = p1 - sum(pieces[1:])
    assert v>=0
    final = pieces[1:]*1 + pieces[1:]*0
    final = []
    for x in pieces[1:]:
        final += [x,x]
    if v>0: final.append(v)
    assert phi2(final)==p1, (pieces, phi2(final), p1)
print("Theorem A identity: OK")
