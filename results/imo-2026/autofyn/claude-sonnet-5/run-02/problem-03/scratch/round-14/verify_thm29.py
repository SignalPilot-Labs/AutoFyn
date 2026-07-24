import random
from fractions import Fraction as F

def A(S):
    # alternating sum of sorted descending
    s = sorted(S, reverse=True)
    total = F(0)
    sign = 1
    for x in s:
        total += sign*x
        sign *= -1
    return total

def integral_indicator_up_to(S, cap):
    # int_0^cap of u_S(x) dx where u_S(x)=1 if #{elements > x} is odd
    # breakpoints: sorted descending values, plus 0 and cap
    s = sorted(set(S), reverse=True)
    # build list of (interval_start, interval_end, count_of_elements_greater_than_x_in_interval)
    # For x in (v_{k+1}, v_k) with elements sorted descending v_1>=v_2>=..., N(x) = k where v_k>x>=v_{k+1}
    # We'll just do a general algorithm with multiplicities
    vals = sorted(S, reverse=True)
    # points where N(x) changes: each element value
    breakpoints = sorted(set(vals + [F(0), cap]))
    total = F(0)
    for i in range(len(breakpoints)-1):
        lo, hi = breakpoints[i], breakpoints[i+1]
        if lo >= cap: break
        hi = min(hi, cap)
        if hi <= lo: continue
        mid = (lo+hi)/2  # use midpoint conceptually but count exactly: use lo+epsilon => count elements > lo
        # N(x) for x in (lo,hi) = number of elements > lo (since no breakpoints strictly between)
        cnt = sum(1 for v in vals if v > lo)
        if cnt % 2 == 1:
            total += (hi - lo)
    return total

random.seed(1)

def rand_frac(lo=1, hi=1000):
    return F(random.randint(lo,hi), random.randint(1,50))

# Test Lemma 29a
viol = 0
trials = 20000
for _ in range(trials):
    k = random.randint(1,6)
    parts = [rand_frac(1,50) for _ in range(k)]
    M = sum(parts)
    a = integral_indicator_up_to(parts, M/2)
    Aval = A(parts)
    b = Aval - a
    if a < b:
        viol += 1
        print("LEMMA29a VIOLATION", parts, a, b)
print("Lemma29a trials", trials, "violations", viol)

# Test Theorem 29
viol2 = 0
trials2 = 20000
for _ in range(trials2):
    M = rand_frac(10,200)
    k = random.randint(1,5)
    # random split of M into k positive parts
    cuts = sorted(F(random.randint(1,999),1000)*M for _ in range(k-1))
    parts = []
    prev = F(0)
    for c in cuts:
        parts.append(c-prev)
        prev = c
    parts.append(M-prev)
    parts = [p for p in parts if p>0]
    if not parts: continue
    # random R with max(R) <= M/2
    kr = random.randint(1,5)
    R = [rand_frac(1, int(M/2*100)+1) for _ in range(kr)]
    # scale down to ensure max<=M/2
    R = [min(r, M/2) * F(random.randint(1,99),100) for r in R]
    if max(R) > M/2:
        continue
    lhs = A(parts + R)
    rhs = M - A(R)
    if lhs > rhs:
        viol2 += 1
        print("THEOREM29 VIOLATION", M, parts, R, lhs, rhs)
print("Theorem29 trials", trials2, "violations", viol2)

# check counterexample scope: tau = {49, 2/5}, m = 203/4
tau = [F(49), F(2,5)]
m = F(203,4)
print("counterexample check: max(tau)=", max(tau), "m/2=", m/2, "hypothesis holds?", max(tau)<=m/2)
