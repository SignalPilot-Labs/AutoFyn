from fractions import Fraction as Fr
import random

def gamma(n):
    return Fr(1, 2**(n+1)-1)

def c(n):
    return Fr(2**n, 2**(n+1)-1)

def oddsum_list(vals):
    s = sorted(vals, reverse=True)
    return sum(s[i] for i in range(0, len(s), 2))

def consecutive_pairing_oddsum(p):
    # p: list of n+1 positive values, descending, sum=1
    n1 = len(p)
    k = n1 // 2
    ls = [p[2*m] - p[2*m+1] for m in range(k)]  # l_m = p_{2m-1}-p_{2m} in 1-indexed -> 0-indexed pairs (2m,2m+1)
    total = sum(p)
    val = Fr(1,2)*(1 - sum(ls)) + oddsum_list(ls)
    return val

def random_region_point(n, seed=None):
    rnd = random.Random(seed)
    K = Fr(n-1,2) - Fr(n*(n+1),2)*gamma(n)
    # random positive weights summing to K on (a,g1,...,gn), a coefficient n+1, g_i coefficient (n+1-i)
    coeffs = [n+1] + [n+1-i for i in range(1,n+1)]
    # random positive reals via random floats -> fractions
    xs = [rnd.random()+0.01 for _ in range(n+1)]
    s = sum(c_*x for c_,x in zip(coeffs,xs))
    scale = float(K)/s
    xs = [x*scale for x in xs]
    a = Fr(xs[0]).limit_denominator(10**6)
    gs = [Fr(x).limit_denominator(10**6) for x in xs[1:]]
    # recompute exactly to satisfy K constraint using fractions directly (avoid float drift)
    # Just use floats->p directly, construct p via formula, then adjust p_{n+1} to fix sum exactly
    p1 = Fr(1,2) - a
    p = [p1]
    cur = p1
    for gi in gs:
        cur = cur - gamma(n) - gi
        p.append(cur)
    # fix rounding: rescale slightly isn't valid (breaks structure); instead solve exactly:
    return p

def check(n, trials=2000, seed=0):
    rnd = random.Random(seed)
    worst = None
    K = Fr(n-1,2) - Fr(n*(n+1),2)*gamma(n)
    coeffs = [n+1] + [n+1-i for i in range(1,n+1)]
    cn = c(n)
    fails=0
    for t in range(trials):
        # sample random positive a,g1..gn (rational) satisfying sum coeff*x = K exactly:
        # generate n+1 random positive rationals as weights, normalize
        raw = [Fr(rnd.randint(1,1000)) for _ in range(n+1)]
        s = sum(c_*r for c_, r in zip(coeffs, raw))
        scale = K / s
        xs = [r*scale for r in raw]
        a = xs[0]; gs = xs[1:]
        p1 = Fr(1,2) - a
        p = [p1]
        cur = p1
        for gi in gs:
            cur = cur - gamma(n) - gi
            p.append(cur)
        assert len(p) == n+1
        assert abs(sum(p) - 1) < Fr(1,10**9)
        val = consecutive_pairing_oddsum(p)
        if val > cn:
            fails += 1
            if worst is None or (val-cn) > worst[0]:
                worst = (val-cn, p, val)
    return fails, trials, worst, cn

for n in range(2, 9):
    fails, trials, worst, cn = check(n, trials=3000, seed=n)
    print(f"n={n}: fails={fails}/{trials}, c(n)={float(cn):.6f}", 
          f"worst excess={float(worst[0]):.6e} at p={[float(x) for x in worst[1]]}" if worst else "NO FAILURES")
