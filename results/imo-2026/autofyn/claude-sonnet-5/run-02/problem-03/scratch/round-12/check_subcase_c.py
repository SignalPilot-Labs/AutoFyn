from fractions import Fraction as F
import random

def f_of(n):
    return F(1, 2**(n+1)-1)

def ladder(n):
    fn = f_of(n)
    return [F(2)**(n+1-i)*fn for i in range(1,n+2)]  # p_1..p_{n+1}

def A(multiset):
    s = sorted(multiset, reverse=True)
    total = F(0)
    sign = 1
    for x in s:
        total += sign*x
        sign *= -1
    return total

def random_refine(pieces, cuts):
    # pieces: list of Fraction values (current fragments)
    pieces = list(pieces)
    for _ in range(cuts):
        idx = random.randrange(len(pieces))
        val = pieces[idx]
        # random split point using a random fraction with small denominator
        num = random.randint(1, 999)
        t = F(num, 1000) * val
        if t <= 0 or t >= val:
            continue
        pieces[idx] = t
        pieces.append(val - t)
    return pieces

random.seed(1)
violations = 0
trials_per_n = 400
for n in range(2, 7):
    p = ladder(n)  # p[0]=p1,...
    p1 = p[0]; p2 = p[1]
    tail = p[1:]  # p2..p_{n+1}
    fn = f_of(n)
    for _ in range(trials_per_n):
        # choose v2 in (0,p2) randomly (P = empty, c=1 case)
        num = random.randint(1, 999)
        v2 = F(num, 1000) * p2
        v1 = p1 - v2
        # tail refinement with budget <= n-1
        cuts = random.randint(0, n-1)
        Gp = random_refine(tail, cuts)
        # check A(G') >= f(n)  [this is what L(n-1) should give, sanity-check the ingredient]
        AG = A(Gp)
        # full check: A({v1,v2} U G') >= f(n)
        full = A([v1, v2] + Gp)
        if full < fn:
            violations += 1
            print("VIOLATION full", n, v2, cuts, full, fn)
        if AG < fn:
            violations += 1
            print("VIOLATION AG", n, cuts, AG, fn)
        # check exact identity: A(F union G') == v1 - A({v2} union G')
        Fv2G = A([v2]+Gp)
        pred = v1 - Fv2G
        if pred != full:
            violations += 1
            print("IDENTITY MISMATCH", n, v2, full, pred)
print("total violations:", violations, "out of", trials_per_n*5*3)

print("--- boundary identity check: A({p2} U G') == p2 - A(G') ---")
violations2 = 0
for n in range(2,7):
    p = ladder(n); p1=p[0]; p2=p[1]; tail=p[1:]
    for _ in range(200):
        cuts = random.randint(0, n-1)
        Gp = random_refine(tail, cuts)
        lhs = A([p2]+Gp)
        rhs = p2 - A(Gp)
        if lhs != rhs:
            violations2 += 1
            print("mismatch", n, lhs, rhs)
print("boundary violations:", violations2)

print("--- monotonicity D(t) check ---")
viol3 = 0
for n in range(2,7):
    p = ladder(n); p1=p[0]; p2=p[1]; tail=p[1:]
    fn = f_of(n)
    for _ in range(200):
        cuts = random.randint(0, n-1)
        Gp = random_refine(tail, cuts)
        # sample increasing t values in (0,p2)
        ts = sorted([F(random.randint(1,999),1000)*p2 for _ in range(6)])
        Dvals = []
        for t in ts:
            v1t = p1 - t
            psi = A([t]+Gp)
            D = (v1t - fn) - psi
            Dvals.append(D)
        # check non-increasing
        for i in range(len(Dvals)-1):
            if Dvals[i+1] > Dvals[i]:
                viol3+=1
                print("non-monotone", n, ts, Dvals)
print("monotonicity violations:", viol3)
