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

def primes_of(n):
    return set(factorint(n).keys())

def prec_minimals(a):
    supp = [primes_of(x) for x in a]
    n = len(a)
    mins = []
    for i in range(n):
        is_min = True
        for m in range(i):
            if supp[m] <= supp[i]:
                is_min = False; break
        if is_min: mins.append(i)
    return mins, supp

# Lemma A test: for x>=a1, x appears iff gcd(x,a_i)>1 for every prec-minimal a_i < x
def test_lemmaA(a1, N, ntest=200):
    a = gen_seq(a1, N)
    mins, supp = prec_minimals(a)
    aset = set(a)
    min_terms = [(a[i], supp[i]) for i in mins]  # (value, support)
    violations = 0
    import random
    rng = random.Random(42)
    for _ in range(ntest):
        x = rng.randint(a1, a[-1]+5)
        appears = x in aset
        # prec-minimal terms with value < x
        ok = all(gcd(x, mv) > 1 for mv, _ in min_terms if mv < x)
        if appears != ok:
            violations += 1
            if violations <= 5:
                print(f"  a1={a1} x={x} appears={appears} ok={ok} VIOLATION")
    return violations

for a1 in [15,30,175,429,273,210,323,385]:
    v = test_lemmaA(a1, 400)
    print(f"a1={a1}: LemmaA violations={v}")

# Verify L,T for a1=15 and a1=429
def compute_LT(a1, N):
    a = gen_seq(a1, N)
    supp = [primes_of(x) for x in a]
    uniq=[]
    for s in supp:
        if s not in uniq: uniq.append(s)
    M=[]
    for s in uniq:
        if not any(t < s for t in uniq): M.append(s)
    P=set()
    for m in M: P|=m
    L=1
    for p in P: L*=p
    V=[r for r in range(L) if all(any(p in m and r%p==0 for p in m) for m in M)]
    return len(M), sorted(P), L, len(V)

print("a1=15:", compute_LT(15,200))
print("a1=429:", compute_LT(429, 6000))
print("a1=30:", compute_LT(30,200))
