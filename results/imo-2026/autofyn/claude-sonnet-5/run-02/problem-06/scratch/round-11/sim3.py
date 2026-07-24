import math
from sympy import factorint
from collections import Counter

_pcache = {}
def primeset(x):
    if x in _pcache: return _pcache[x]
    s = set(factorint(x).keys())
    _pcache[x] = s
    return s

def gen_seq(a1, N):
    a = [None, a1]
    for _ in range(N-1):
        an = a[-1]
        c = an + 1
        while True:
            ok = True
            for prev in a[1:]:
                if math.gcd(c, prev) == 1:
                    ok = False
                    break
            if ok:
                a.append(c)
                break
            c += 1
    return a

def analyze(a1, N, tailfrac=0.5):
    a = gen_seq(a1, N)
    Q = primeset(a1)
    tau = [None]*(N+1)
    for n in range(1, N+1):
        tau[n] = frozenset(primeset(a[n]) & Q)
    tailstart = int(N*tailfrac)
    persistent = set(tau[n] for n in range(tailstart, N+1))
    witness = {}
    for n in range(1, N+1):
        if tau[n] in persistent and tau[n] not in witness:
            witness[tau[n]] = n
    S = set()
    for t, m in witness.items():
        S |= (primeset(a[m]) - Q)
    S0 = Q | S
    rho = [None]*(N+1)
    for n in range(1, N+1):
        rho[n] = frozenset(primeset(a[n]) & S0)
    ext_persistent = set(rho[n] for n in range(tailstart, N+1))
    ext_witness = {}
    for n in range(1, N+1):
        if rho[n] in ext_persistent and rho[n] not in ext_witness:
            ext_witness[rho[n]] = n
    return dict(a=a, Q=Q, tau=tau, persistent=persistent, S0=S0, rho=rho,
                ext_persistent=ext_persistent, ext_witness=ext_witness, N=N)

def find_rogue_pairs(res):
    ext_persistent = res['ext_persistent']
    lst = list(ext_persistent)
    pairs = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i==j: continue
            A,B = lst[i], lst[j]
            baseA = A & res['Q']; baseB = B & res['Q']
            if baseA != baseB and (baseA & baseB)==frozenset() and (A&B)==frozenset():
                pairs.append((A,B))
    return pairs

def walk_analysis(res, A, B):
    a = res['a']; N = res['N']; S0 = res['S0']; rho = res['rho']
    ew = res['ext_witness']
    nA = ew[A]; nB = ew[B]
    if nA > nB:
        A,B = B,A; nA,nB = nB,nA
    Fpp = primeset(a[nB]) - S0
    Fp = primeset(a[nA]) - S0
    common = Fp & Fpp
    qstar = min(common) if common else None
    fac = factorint(a[nB])
    b = 1
    for p,e in fac.items():
        if p in Fpp: b *= p**e
    occ = [n for n in range(nB+1, N+1) if rho[n]==A]
    gs = [math.gcd(a[n], a[nB]) for n in occ]
    return dict(nA=nA, nB=nB, Fp=Fp, Fpp=Fpp, qstar=qstar, b=b, occ=occ, gs=gs)
