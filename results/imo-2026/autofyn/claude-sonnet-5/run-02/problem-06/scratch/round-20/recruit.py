import math
from sympy import factorint
from collections import defaultdict

def gen_sequence(a1, N):
    a = [a1]
    while len(a) < N:
        an = a[-1]
        cand = an + 1
        while True:
            ok = True
            for x in a:
                if math.gcd(cand, x) == 1:
                    ok = False
                    break
            if ok:
                a.append(cand)
                break
            cand += 1
    return a

def recruit(a1, N=4000, iters=6, min_occ=8, tail_frac=0.6):
    a = gen_sequence(a1, N)
    fac = [set(factorint(v).keys()) for v in a]
    Q = set(factorint(a1).keys())
    S = set(Q)
    history=[]
    for it in range(iters):
        occ = defaultdict(list)
        for i,f in enumerate(fac):
            n=i+1
            rho = frozenset(f & S)
            if rho:
                occ[rho].append(n)
        persistent = [t for t,ns in occ.items() if len(ns)>=min_occ and ns[-1] > N*tail_frac]
        newS = set(S)
        for t in persistent:
            m = occ[t][0]
            newS |= (fac[m-1] - S)
        history.append((it, sorted(S), sorted(newS)))
        if newS == S:
            break
        S = newS
    # final analysis
    occ = defaultdict(list)
    for i,f in enumerate(fac):
        n=i+1
        rho = frozenset(f & S)
        if rho:
            occ[rho].append(n)
    persistent = [t for t,ns in occ.items() if len(ns)>=min_occ and ns[-1] > N*tail_frac]
    results=[]
    for i in range(len(persistent)):
        for j in range(i+1,len(persistent)):
            A,B = persistent[i], persistent[j]
            if A & B: continue
            nA=occ[A][0]; nB=occ[B][0]
            fA = fac[nA-1]-S; fB= fac[nB-1]-S
            results.append((A,B,len(fA),len(fB),fA,fB,len(occ[A]),len(occ[B])))
    return S, results, history

for a1 in [4807, 11305]:
    S, res, hist = recruit(a1, N=6000, iters=6)
    print(f"a1={a1} final S={sorted(S)}")
    for r in res:
        print("  ", r)
