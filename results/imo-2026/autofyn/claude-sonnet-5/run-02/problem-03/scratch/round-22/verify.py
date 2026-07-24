from fractions import Fraction as Fr
import random, itertools

def f(m):
    return Fr(1, 2**(m+1)-1)

def ladder(m):
    # returns p_1..p_{m+1}
    fm = f(m)
    return [Fr(2**(m+1-i))*fm for i in range(1, m+2)]

def A(S):
    S = sorted(S, reverse=True)
    tot = Fr(0)
    for i,x in enumerate(S):
        tot += x if i%2==0 else -x
    return tot

def Asup(S, v):
    return A([x for x in S if x > v])

# Test 1: General cross-level rescaling: {p_{k+1},...,p_{n+1}} / lambda_k == (n-k)-ladder,
# lambda_k = f(n)/f(n-k)
random.seed(1)
maxerr = 0
for n in range(2, 10):
    p = ladder(n)  # p[0]=p_1 .. p[n]=p_{n+1}
    for k in range(0, n):
        m = n-k
        if m < 1: continue
        lam = f(n)/f(m)
        q = ladder(m)
        tail = p[k:]  # p_{k+1}...p_{n+1}
        assert len(tail) == len(q), (n,k,len(tail),len(q))
        for a,b in zip(tail,q):
            diff = a - lam*b
            if abs(diff) > maxerr: maxerr = abs(diff)
            assert a == lam*b, (n,k,a,lam*b)
print("Cross-level rescaling identity: exact match for n=2..9, all k. max abs err:", maxerr)

# Test 2: lambda_k * f(n-k) == f(n)
for n in range(2,10):
    for k in range(0,n):
        m=n-k
        lam = f(n)/f(m)
        assert lam*f(m) == f(n)
print("lambda_k * f(n-k) = f(n): exact for all tested n,k")

import random
random.seed(2)

def random_split(x, rng):
    r = Fr(rng.randint(1,999),1000)
    a = x*r
    b = x-a
    return a,b

def legal_response(pieces, budget, rng):
    pieces = list(pieces)
    cuts_used = 0
    max_cuts = budget
    # randomly decide how many cuts to actually use (<=budget)
    target_cuts = rng.randint(0, max_cuts)
    for _ in range(target_cuts):
        idx = rng.randrange(len(pieces))
        x = pieces.pop(idx)
        a,b = random_split(x, rng)
        pieces.append(a); pieces.append(b)
    return pieces

# Case (b) generator at level n: force p3 cut, then random remaining cuts on {a,b}+T'
def case_b_response(n, rng):
    p = ladder(n)
    p3 = p[2]
    a,b = random_split(p3, rng)
    if a < b: a,b = b,a
    tail = p[3:]  # p4..p_{n+1}
    remaining_budget = (n-3) - 1  # n-4
    if remaining_budget < 0:
        return None
    Tprime = legal_response(tail, remaining_budget, rng)
    Rp = [a,b] + Tprime
    return Rp, a, b, Tprime

rng = random.Random(42)
results = {}
worst = {}
for n in range(3, 9):
    trials = 0
    minAR = None
    minAB = None
    worst_delta_margin = None
    checked_subrange = True
    for t in range(3000):
        res = case_b_response(n, rng)
        if res is None: continue
        Rp, a, b, Tprime = res
        trials += 1
        fn = f(n)
        AR = A(Rp)
        B = [b]+Tprime
        AB = A(B)
        if minAR is None or AR < minAR: minAR = AR
        if minAB is None or AB < minAB: minAB = AB
        # check A(R') >= f(n)
        if AR < fn:
            print("VIOLATION A(R')>=f(n)", n, AR, fn)
        # check sub-range v < min(R'): Delta(n,v) = -A(R') <= v - f(n) for all v in (0,min(Rp))
        minRp = min(Rp)
        # check at v -> 0+ (hardest): need A(R') >= f(n) - v ~ f(n) at v=0
        # check full (Diamond) at several v samples across (0,s)
        s = sum(tail if False else Rp)  # total of R'
        for _ in range(20):
            v = Fr(rng.randint(0,10000),10000) * s
            if v<=0 or v>=s: continue
            delta = AR - 2*Asup(Rp, v)
            margin = (v - fn) - delta  # should be >=0
            if worst_delta_margin is None or margin < worst_delta_margin:
                worst_delta_margin = margin
    if trials == 0:
        print(f"n={n}: no legal Case(b) trials (budget negative)")
        continue
    print(f"n={n}: trials={trials}, min A(R')-f(n) = {float(minAR-f(n)):.4f}, "
          f"min A(B)-f(n) = {float(minAB-f(n)):.4f}, "
          f"worst Delta margin (should be >=0) = {float(worst_delta_margin):.6f}")

print()
print("=== Insert-element formula check: A({b}+T') = 2*A(T'_{>b}) - A(T') + (-1)^j * b ===")
rng2 = random.Random(7)
maxdiff = 0
for trial in range(5000):
    k = rng2.randint(0,6)
    Tp = [Fr(rng2.randint(1,1000),1000) for _ in range(k)]
    b = Fr(rng2.randint(1,1000),1000)
    j = sum(1 for x in Tp if x > b)
    lhs = A([b]+Tp)
    rhs = 2*Asup(Tp,b) - A(Tp) + (Fr(-1)**j)*b
    d = abs(lhs-rhs)
    if d > maxdiff: maxdiff = d
    assert lhs==rhs, (Tp,b,lhs,rhs)
print("Insert-element formula: exact match, 5000 trials. max diff:", maxdiff)

print()
print("=== epsilon(v)=0 on Theorem 35b range v>=p3 (Case a, p3 untouched) ===")
rng3 = random.Random(11)
allzero = True
for n in range(3,9):
    p = ladder(n)
    p3 = p[2]
    tail = p[3:]
    budget = n-3
    for t in range(500):
        Tp = legal_response(tail, budget, rng3)
        Rp = [p3] + Tp
        s = sum(Rp)
        for _ in range(10):
            v = p3 + Fr(rng3.randint(0,10000),10000)*(s-p3) if s>p3 else p3
            Nv = len([x for x in Rp if x>v])
            if Nv != 0:
                allzero = False
                print("nonzero N found", n, v, Nv)
print("R'_{>v} empty (N=0, hence epsilon=0) throughout v>=p3 for all tested n,trials:", allzero)
