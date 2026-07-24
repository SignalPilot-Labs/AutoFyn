from fractions import Fraction as F
import random

def A(vals):
    s = sorted(vals, reverse=True)
    total = sum(s)
    a = F(0)
    sign = 1
    for v in s:
        a += sign*v
        sign = -sign
    return a

def odd_run_reduce(vals):
    # count multiplicities, keep 1 copy if odd mult, 0 if even
    from collections import Counter
    c = Counter(vals)
    out = []
    for v,mult in c.items():
        if mult % 2 == 1:
            out.append(v)
    return out

def phi(vals):
    total = sum(vals)
    return (total + A(vals))/2

# Test 1: verify A(M) = A(odd_run_reduce(M)) directly (sanity of certified lemma)
random.seed(1)
for trial in range(2000):
    n = random.randint(1,8)
    vals = [F(random.randint(1,50), random.randint(1,20)) for _ in range(n)]
    # inject some duplicates
    if random.random()<0.6 and len(vals)>=2:
        i,j = random.sample(range(len(vals)),2)
        vals[j]=vals[i]
    a1 = A(vals)
    a2 = A(odd_run_reduce(vals))
    assert a1==a2, (vals,a1,a2)
print("Test1 (odd-run-reduction sanity) passed: 2000 trials")

