from fractions import Fraction as F
import random, itertools

def A(multiset):
    s = sorted(multiset, reverse=True)
    total = F(0)
    for i,v in enumerate(s):
        if i%2==0: total += v
        else: total -= v
    return total

def E_val(multiset):
    s = sorted(multiset, reverse=True)
    total = F(0)
    for i,v in enumerate(s):
        if i%2==1: total += v
    return total

random.seed(1)

def rand_frac(lo=1, hi=50):
    return F(random.randint(lo,hi), random.randint(1,50))

violations = []
tested = 0

for trial in range(20000):
    m = random.randint(1,6)
    tau1 = rand_frac(1,30)
    tau = [tau1 / (2**i) for i in range(m)]  # tau_1..tau_m
    R = sum(tau)
    # s in (0, 2 tau1]
    s = F(random.randint(1,200), 200) * 2*tau1
    if s<=0: continue
    k = random.randint(1, m+1)
    # generate random partition of s into k nonneg parts each <= tau1, via stick breaking + rejection
    ok=False
    for attempt in range(200):
        cuts = sorted(F(random.randint(0,10000),10000) for _ in range(k-1))
        pts = [F(0)]+cuts+[F(1)]
        parts = [ (pts[i+1]-pts[i])*s for i in range(k) ]
        if all(p <= tau1 for p in parts):
            ok=True
            break
    if not ok: continue
    F_multiset = parts
    S = F_multiset + tau
    Aval = A(S)
    target = s - R
    tested += 1
    if Aval < target - F(1,10**9):
        violations.append((m, tau1, s, k, parts, Aval, target))

print("tested", tested, "violations", len(violations))
for v in violations[:10]:
    print(v)
