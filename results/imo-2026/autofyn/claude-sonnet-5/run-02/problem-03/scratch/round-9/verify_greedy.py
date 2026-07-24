from fractions import Fraction as F
import random, itertools

def A(S):
    # S: list of Fraction lengths
    S = sorted(S, reverse=True)
    total = F(0)
    sign = 1
    for x in S:
        total += sign*x
        sign *= -1
    return total

def ladder(n):
    D = 2**(n+1)-1
    return [F(2**(n+1-i), D) for i in range(1, n+2)]  # p_1..p_{n+1}

def f(n):
    return F(2**n, 2**(n+1)-1)

# Test Lemma 19: F = {v} U P, P pairs up exactly -> A(F) = v
random.seed(1)
for trial in range(2000):
    v = F(random.randint(1,50), random.randint(1,50))
    k = random.randint(0,4)
    P = []
    for _ in range(k):
        a = F(random.randint(1,50), random.randint(1,50))
        P += [a,a]
    Fm = [v]+P
    assert A(Fm) == v, (v,P,A(Fm))
print("Lemma 19 (A(F)=v for single residual + pairs): OK")

# Test Proposition 20: A(F U G') = v - A(G') when v>=p2, using actual ladder tail refinements
def refine_random(pieces, cuts):
    # randomly cut 'cuts' times among the pieces (split a random piece into two random positive parts)
    pcs = list(pieces)
    for _ in range(cuts):
        idx = random.randrange(len(pcs))
        x = pcs[idx]
        if x <= 0: continue
        t = F(random.randint(1,999),1000)
        a = x*t
        b = x-a
        if a==0 or b==0: continue
        pcs[idx]=a
        pcs.append(b)
    return pcs

random.seed(2)
for n in [2,3,4,5]:
    p = ladder(n)
    p1 = p[0]
    p2 = p[1]
    tail = p[1:]
    r = sum(tail)
    for trial in range(300):
        # build F with l(F)=1, v>=p2
        # pick v in [p2, p1]
        v = p2 + (p1-p2)*F(random.randint(0,1000),1000)
        rem = p1 - v
        if rem == 0:
            Fm = [v]
        else:
            a = rem/2
            Fm = [v,a,a]
        cuts = random.randint(0, max(0,n-2))
        Gp = refine_random(tail, cuts)
        lhs = A(Fm+Gp)
        rhs = v - A(Gp)
        assert lhs == rhs, (n,v,Fm,Gp,lhs,rhs)
print("Proposition 20 (A(F U G')=v-A(G') for v>=p2): OK")

# Test Proposition 22 bound: max A(G') over refinements of tail with <=n-2 cuts, when G' leaves p2 uncut
random.seed(3)
for n in [3,4,5,6]:
    p = ladder(n)
    p2 = p[1]
    tail = p[1:]
    R = tail[1:]  # tail's own tail (excluding p2)
    r = sum(tail)
    best = F(0)
    for trial in range(3000):
        cuts = n-2
        Gp = refine_random(R, cuts)  # p2 left uncut, refine only R
        full = [p2]+Gp
        val = A(full)
        if val > best: best = val
    bound = p2 - f(n)
    print(n, "max A(G') found:", best, " bound p2-f(n):", bound, "OK" if best<=bound else "VIOLATION")
