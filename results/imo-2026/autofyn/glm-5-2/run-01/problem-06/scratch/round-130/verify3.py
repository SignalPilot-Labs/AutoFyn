from math import gcd
from sympy import factorint

def gen_seq(a1, N):
    a = [a1]
    for _ in range(N-1):
        an = a[-1]; cand = an+1
        while True:
            if all(gcd(cand, x)>1 for x in a):
                a.append(cand); break
            cand += 1
    return a

# verify a_{n+T}=a_n+L for all n in range
for a1, N in [(15,120),(30,50),(175,300),(323,300),(385,300)]:
    a = gen_seq(a1, N)
    supp=[set(factorint(x).keys()) for x in a]
    uniq=[]
    for s in supp:
        if s not in uniq: uniq.append(s)
    M=[s for s in uniq if not any(t<s for t in uniq)]
    P=set()
    for m in M: P|=m
    L=1
    for p in P: L*=p
    V=[r for r in range(L) if all(any(p in m and r%p==0 for p in m) for m in M)]
    T=len(V)
    ok=all(a[n+T]==a[n]+L for n in range(len(a)-T))
    print(f"a1={a1}: L={L} T={T} period-holds-for-all-n={ok} (N={N})")
