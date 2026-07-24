import sympy
from sympy import factorint, primefactors
from math import gcd

def seq(a1, N):
    a=[None,a1]
    terms=[a1]
    while len(terms)<N:
        an=terms[-1]
        c=an+1
        while True:
            ok=all(gcd(c,t)>1 for t in terms)
            if ok:
                break
            c+=1
        terms.append(c)
    return terms

def Qof(a1):
    return set(primefactors(a1))

def analyze(a1, N=3000):
    terms = seq(a1, N)
    Q = Qof(a1)
    types = [frozenset(primefactors(t)) & Q for t in terms]
    return terms, types

pairs = [(15,45),(15,225),(6,12),(6,24),(6,72),(105,315),(105,11025)]
for a,b in pairs:
    ta,tya = analyze(a, 1500)
    tb,tyb = analyze(b, 1500)
    # compare type sequences (as base-type strings) for first 60 terms
    sa=[''.join(str(x) for x in sorted(t)) for t in tya[:40]]
    sb=[''.join(str(x) for x in sorted(t)) for t in tyb[:40]]
    match = sa==sb
    print(a,b,"Q equal?",Qof(a)==Qof(b), "type-seq match first40:",match)
    if not match:
        for i,(x,y) in enumerate(zip(sa,sb)):
            if x!=y:
                print("  first diff at n=",i+2, x, y)
                break

def find_period(terms, minT=1,maxT=60):
    N=len(terms)
    for T in range(1,maxT):
        Ls=set()
        ok=True
        for n in range(N-T-1-400, N-T-1):
            if n<1: continue
            L=terms[n+T]-terms[n]
            Ls.add(L)
        if len(Ls)==1:
            return T, list(Ls)[0]
    return None,None

for a1 in [105,315,11025]:
    terms,_=analyze(a1,4000)
    T,L=find_period(terms)
    print(a1,"T,L=",T,L)
