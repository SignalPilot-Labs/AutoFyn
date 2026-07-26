import math
from collections import Counter

def naive_greedy(a1, N):
    a=[a1]
    while len(a)<N:
        x=a[-1]+1
        while True:
            ok=all(math.gcd(x,ai)>1 for ai in a)
            if ok: break
            x+=1
        a.append(x)
    return a

# Verify a1=375: naive O(N^2) greedy, check period T=852, L=3990, gov prime 19
for a1 in [375]:
    N=3000
    a=naive_greedy(a1,N)
    d=[a[i+1]-a[i] for i in range(len(a)-1)]
    # check periodicity of d with T=852
    T=852; L=3990
    viol=sum(1 for i in range(len(d)-T) if d[i]!=d[i+T])
    print(f"a1={a1}: naive greedy N={N}")
    print(f"  d[0:8]={d[:8]}")
    print(f"  d[-8:]={d[-8:]}")
    print(f"  T=852 violations over {len(d)-T} offsets: {viol}")
    # check a_{n+T}=a_n+L
    viol2=sum(1 for i in range(len(a)-T) if a[i+T]-a[i]!=L)
    print(f"  a[n+852]-a[n]==3990 violations: {viol2}")
    # check 19 governs: count terms divisible by 19
    c19=sum(1 for x in a if x%19==0)
    print(f"  terms div by 19: {c19}/{len(a)} = {c19/len(a):.3f}")
    # factor L
    def fact(n):
        f={};x=2
        while x*x<=n:
            while n%x==0: f[x]=f.get(x,0)+1; n//=x
            x+=1
        if n>1: f[n]=f.get(n,0)+1
        return f
    print(f"  L=3990 factors={fact(3990)}; rad(a1=375)={fact(375)}")
    print(f"  CONJECTURE q<=rad(a1)=15: largest gov prime = 19 > 15 -> REFUTED" if 19>15 else "holds")
