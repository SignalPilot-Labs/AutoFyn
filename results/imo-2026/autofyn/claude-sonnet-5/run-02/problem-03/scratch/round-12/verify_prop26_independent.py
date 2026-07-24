from fractions import Fraction as F
import random

def A(multiset):
    s = sorted(multiset, reverse=True)
    total = F(0)
    sign = 1
    for x in s:
        total += sign*x
        sign = -sign
    return total

def ladder(n):
    # p_i = 2^{n+1-i} / (2^{n+1}-1), i=1..n+1
    D = 2**(n+1)-1
    return [F(2**(n+1-i), D) for i in range(1, n+2)]

def f(n):
    return F(1, 2**(n+1)-1)

def random_legal_refinement(pieces, cuts_budget):
    """pieces: list of Fraction piece lengths. Apply up to cuts_budget random cuts,
    each splitting a randomly chosen current piece at a random rational point strictly inside it."""
    pieces = list(pieces)
    ncuts = random.randint(0, cuts_budget)
    for _ in range(ncuts):
        idx = random.randrange(len(pieces))
        p = pieces[idx]
        # random rational split point
        num = random.randint(1, 999)
        frac = F(num, 1000)
        a = p*frac
        b = p - a
        if a == 0 or b == 0:
            continue
        pieces[idx] = a
        pieces.append(b)
    return pieces

random.seed(12345)

# Verify Proposition 26 directly: F = {v1, v2}, v1+v2 = p1, v1>=p2>v2 automatic since p1=2p2
# G' = legal refinement of tail using <= n-1 cuts
# Check A(F union G') >= f(n)

violations = 0
trials_total = 0
for n in range(2, 7):
    L = ladder(n)
    p1 = L[0]
    p2 = L[1]
    tail = L[1:]  # p2..p_{n+1}
    fn = f(n)
    for trial in range(1500):
        # random v2 in (0, p2), v1 = p1 - v2
        num = random.randint(1, 999)
        v2 = p2 * F(num, 1000)
        v1 = p1 - v2
        assert v1 >= p2 and v2 < p2  # automatic per doubling identity check
        Gp = random_legal_refinement(tail, n-1)
        S = [v1, v2] + Gp
        val = A(S)
        trials_total += 1
        if val < fn:
            violations += 1
            print("VIOLATION", n, v2, val, fn)

print("Prop26 direct check: trials=", trials_total, "violations=", violations)

# Verify the exact identity: A({v1,v2}∪G') = v1 - A({v2}∪G')  (sub-case c identity)
viol2 = 0
tot2 = 0
for n in range(2,7):
    L = ladder(n)
    p1, p2 = L[0], L[1]
    tail = L[1:]
    for trial in range(1000):
        num = random.randint(1,999)
        v2 = p2*F(num,1000)
        v1 = p1 - v2
        Gp = random_legal_refinement(tail, n-1)
        lhs = A([v1,v2]+Gp)
        rhs = v1 - A([v2]+Gp)
        tot2 += 1
        if lhs != rhs:
            viol2 += 1
            print("IDENTITY VIOLATION", n, v2, lhs, rhs)
print("sub-case c identity: trials=",tot2,"violations=",viol2)

# Verify phi(t) closed form and endpoint identity phi(p2) = p2 - A(G')
viol3 = 0
tot3 = 0
for n in range(2,7):
    L = ladder(n)
    p1, p2 = L[0], L[1]
    tail = L[1:]
    for trial in range(500):
        Gp = random_legal_refinement(tail, n-1)
        AGp = A(Gp)
        phi_p2 = A([p2]+Gp)
        tot3+=1
        if phi_p2 != p2 - AGp:
            viol3+=1
            print("ENDPOINT VIOLATION", n, phi_p2, p2-AGp)
print("endpoint identity: trials=",tot3,"violations=",viol3)

# Verify monotonicity of D(t) := (p1-t-f(n)) - phi(t) is nonincreasing by checking many sample points
viol4 = 0
tot4 = 0
for n in range(2,5):
    L = ladder(n)
    p1,p2 = L[0],L[1]
    tail = L[1:]
    fn = f(n)
    for trial in range(200):
        Gp = random_legal_refinement(tail, n-1)
        ts = sorted([p2*F(random.randint(1,999),1000) for _ in range(8)])
        prevD = None
        for t in ts:
            phit = A([t]+Gp) # treat t as abstract element combined with Gp
            Dt = (p1-t-fn) - phit
            tot4+=1
            if prevD is not None and Dt > prevD:
                viol4+=1
                print("MONOTONICITY VIOLATION", n, t, Dt, prevD)
            prevD = Dt
print("monotonicity check: trials=",tot4,"violations=",viol4)
