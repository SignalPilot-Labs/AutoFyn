from fractions import Fraction as F
import random
import sys
sys.path.insert(0,'/tmp/round-12')
exec(open('/tmp/round-12/check_subcase_c.py').read().split("print(\"total violations")[0])

random.seed(2)
violations = 0
trials = 300
for n in range(3, 7):
    p = ladder(n); p1=p[0]; p2=p[1]; tail=p[1:]
    fn = f_of(n)
    for _ in range(trials):
        # P = one pair {a,a}, plus residuals v1,v2, using c=3 cuts total on p1
        a = F(random.randint(1,999),2000) * p1  # a small enough
        num = random.randint(1,999)
        v2 = F(num,1000) * (p2 - 2*a) if p2 - 2*a > 0 else None
        if v2 is None or v2<=0:
            continue
        v1 = p1 - v2 - 2*a
        if v1 < p2:
            continue
        cuts = random.randint(0, n-3) if n-3>=0 else 0
        Gp = random_refine(tail, cuts)
        F_ = [v1,v2,a,a]
        full = A(F_+Gp)
        if full < fn:
            violations += 1
            print("VIOLATION", n, v1,v2,a, full, fn)
print("P-nonempty violations:", violations)
