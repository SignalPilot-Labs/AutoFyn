from math import gcd
from sympy import factorint

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

# Test the descent's witness-finding mechanism on every term carrying a large prime
# (p > a1^2). For each such term, the descent constructs q^k c < a_n with rad|rad(a_n),
# so a_n should be non-prec-minimal. Verify ALL such terms are indeed non-prec-minimal
# AND that the constructed q^k c actually appears earlier with rad|rad.
def test_descent(a1, N):
    a=gen_seq(a1,N)
    mins,supp=prec_minimals(a)
    minset=set(mins)
    a1sq=a1*a1
    n_large=0
    for i in range(len(a)):
        an=a[i]; ps=supp[i]
        large=[p for p in ps if p>a1sq]
        if not large: continue
        n_large+=1
        p=large[0]; c=an//p
        assert an==p*c
        # is a_i prec-minimal? should be NO per theorem
        is_min = i in minset
        if is_min:
            print(f"  a1={a1} a[{i}]={an} carries large prime {p}>{a1sq} BUT is prec-minimal — THEOREM VIOLATED")
            return False
        # construct q
        g=gcd(a1,an)
        qs=[pp for pp in primes_of(g)]
        if not qs:
            print(f"  a1={a1} a[{i}]={an}: gcd(a1,a_n)={g} has no prime — cannot pick q")
            # this would be a problem; but per pairwise-intersection gcd>1
            continue
        q=qs[0]
        assert q<=a1 and q!=p and c%q==0, f"q={q} p={p} c={c} q|c failed"
        # smallest k with q^k c >= a1
        k=0; val=c
        while val<a1:
            val*=q; k+=1
        # check val < a_n
        if not (val<an):
            print(f"  a1={a1} a[{i}]={an} p={p} q={q} k={k} q^k c={val} NOT < a_n={an} — LANDING FAILED")
            return False
        # rad(q^k c) | rad(a_n)?
        if not primes_of(val)<=supp[i]:
            print(f"  rad-div FAILED")
            return False
        # q^k c appears earlier? (Lemma A says it must)
        if val not in a:
            print(f"  a1={a1} q^k c={val} does NOT appear in sequence — Lemma A application FAILED")
            return False
        j=a.index(val)
        if not (j<i):
            print(f"  idx not earlier"); return False
    print(f"a1={a1}: {n_large} terms carry large primes (>a1^2={a1sq}); descent mechanism verified on all (none prec-minimal, q^k c lands & appears earlier)")
    return True

for a1,N in [(15,2500),(30,2500),(175,1500),(323,2000),(385,2000)]:
    test_descent(a1,N)
