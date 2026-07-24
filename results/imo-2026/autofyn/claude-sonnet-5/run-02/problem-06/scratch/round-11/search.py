import sympy
from sympy import primefactors, gcd, factorint

def gen_sequence(a1, N):
    a = [None, a1]
    while len(a) <= N:
        n = len(a)-1
        prev = a[-1]
        c = prev+1
        while True:
            ok = True
            for i in range(1, n+1):
                if gcd(c, a[i]) == 1:
                    ok = False
                    break
            if ok:
                a.append(c)
                break
            c += 1
    return a

a1 = 4807
N = 2500
a = gen_sequence(a1, N)
S0 = {2,3,5,7,11,19,23,73,127}

def rho(n):
    return frozenset(primefactors(a[n])) & S0

types = {}
for n in range(1, N+1):
    t = rho(n)
    types.setdefault(t, []).append(n)

persistent = {t:occ for t,occ in types.items() if len(occ)>=4 and len(t)>0}
tlist = list(persistent.keys())
print(len(tlist), "persistent types")

best = []
for i in range(len(tlist)):
    for j in range(len(tlist)):
        if i==j: continue
        A, B = tlist[i], tlist[j]
        if A & B: continue
        nA = persistent[A][0]
        nB = persistent[B][0]
        if nA >= nB: continue
        Fp = set(primefactors(a[nA])) - S0
        Fpp = set(primefactors(a[nB])) - S0
        inter = Fp & Fpp
        if not inter: continue
        qstar = min(inter)
        fac_nB = factorint(a[nB])
        b = 1
        for p,e in fac_nB.items():
            if p in Fpp:
                b *= p**e
        divs = sympy.divisors(b)
        bad = [d for d in divs if d>1 and qstar % 1==0 and (qstar not in factorint(d))]
        if len(divs) > 2:  # nontrivial alphabet
            best.append((A,B,nA,nB,Fp,Fpp,qstar,b,divs))

for rec in best[:15]:
    A,B,nA,nB,Fp,Fpp,qstar,b,divs = rec
    print("A'",A,"nA",nA,"B'",B,"nB",nB,"F'",Fp,"F''",Fpp,"q*",qstar,"b",b,"Div(b)",divs)
