from math import gcd
from sympy import factorint, isprime

# Independently re-derive the descent's mechanism on a concrete case:
# take a1=46189 (the largest seed), find a prec-minimal term carrying the max prime,
# and check the descent produces an earlier q^k c with rad|rad.
def gen_seq(a1, N):
    a=[a1]
    for _ in range(N-1):
        an=a[-1]; c=an+1
        while True:
            if all(gcd(c,x)>1 for x in a):
                a.append(c); break
            c+=1
    return a

def primes_of(n): return set(factorint(n).keys())

def prec_minimals(a):
    supp=[primes_of(x) for x in a]; n=len(a); mins=[]
    for i in range(n):
        if not any(supp[m]<=supp[i] for m in range(i)): mins.append(i)
    return mins, supp

a1=46189
a=gen_seq(a1, 400)
mins,supp=prec_minimals(a)
# find the prec-minimal carrying the largest prime
maxp=max(p for i in mins for p in supp[i])
# find which prec-minimal term carries maxp
target=[i for i in mins if maxp in supp[i]]
print("maxp=",maxp,"a1^2=",a1*a1,"target idxs=",target[:3])
for i in target[:2]:
    an=a[i]; p=maxp; c=an//p
    assert an==p*c
    # pick q | gcd(a1, an), q prime
    g=gcd(a1,an)
    qs=[pp for pp in primes_of(g)]
    q=qs[0]
    print(f"  a_n=a[{i}]={an}, p={p}, c={c}, q={q}, q<=a1:{q<=a1}, q!=p:{q!=p}, q|c:{c%q==0}")
    # smallest k with q^k c >= a1
    k=0; val=c
    while val < a1:
        val*=q; k+=1
    print(f"  k={k}, q^k c={val}, in [a1,a_n): {a1<=val<an}, rad(q^k c)|rad(a_n): {primes_of(val)<=supp[i]}")
    # check q^k c actually appears in sequence with idx < i
    if val in a:
        j=a.index(val)
        print(f"  q^k c={val} appears at idx {j} < {i}: {j<i}, rad(q^k c) subset P(a_n): {primes_of(val)<=supp[i]}")
