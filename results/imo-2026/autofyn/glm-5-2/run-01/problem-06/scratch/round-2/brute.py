from sympy import factorint
import math

def primes_of(n): return set(factorint(n).keys())

def brute(a1, max_terms=40000, max_a=2_000_000):
    P=[primes_of(a1)]
    a=a1
    M=[frozenset(P[0])]
    Peset=set(M[0])
    # for admissibility we need gcd(m, a_i)>1 for all i<=n  <=> P(m) hits every P(a_i)... 
    # use: m admissible iff P(m) hits every minimal support M
    Mlist=[set(M[0])]
    terms=[a1]
    for step in range(max_terms):
        # find smallest m>a valid: P(m) hits every M in Mlist
        m=a+1
        while True:
            Pm=primes_of(m)
            ok=all((Pm & mm) for mm in Mlist)
            if ok: break
            m+=1
            if m>max_a:
                return None
        a=m
        terms.append(a)
        Pm=primes_of(m)
        # promotion?
        if not any(set(mm)<=Pm for mm in Mlist):
            # new minimal
            newM=[mm for mm in Mlist if not (Pm<=mm)]
            newM.append(Pm)
            Mlist=newM
            Peset=Peset|Pm
    return dict(a=a, Pess=sorted(Peset), M=[sorted(x) for x in Mlist], terms=terms, n=len(terms))

for a1 in [15, 187, 221, 35, 65]:
    r=brute(a1)
    if r is None:
        print(f"a1={a1}: max_a exceeded"); continue
    print(f"a1={a1}: |Pess|={len(r['Pess'])} |M|={len(r['M'])} final_a={r['a']} n_terms={r['n']}")
    print(f"  Pess={r['Pess']}")
    print(f"  M={r['M']}")
