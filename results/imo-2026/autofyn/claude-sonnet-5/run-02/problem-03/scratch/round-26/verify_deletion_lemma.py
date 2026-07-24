from fractions import Fraction as Fr
import random

def f(n):
    return Fr(1, 2**(n+1)-1)

def ladder(n):
    fn = f(n)
    return [2**(n+1-i)*fn for i in range(1, n+2)]  # p_1..p_{n+1}

def A(S):
    S = sorted(S, reverse=True)
    total = Fr(0)
    sign = 1
    for x in S:
        total += sign*x
        sign *= -1
    return total

def random_legal_refinement(pieces, max_cuts):
    # pieces: list of Fractions (the original tail pieces)
    # perform up to max_cuts random cuts distributed among pieces
    frags = list(pieces)
    cuts = random.randint(0, max_cuts)
    for _ in range(cuts):
        # pick a fragment with positive length to split
        idx = random.randrange(len(frags))
        v = frags[idx]
        if v <= 0:
            continue
        r = Fr(random.randint(1,999),1000)
        a = v*r
        b = v-a
        frags[idx] = a
        frags.append(b)
    return frags

random.seed(0)
violations = 0
trials_total = 0
min_slack = None
for n in range(5, 10):
    p = ladder(n)  # p[0]=p_1 ... p[n]=p_{n+1}
    p4 = p[3]
    tail = p[4:]  # p_5 .. p_{n+1}
    fn = f(n)
    for trial in range(3000):
        Tpp = random_legal_refinement(tail, n-4)  # T'' : legal refinement of tail with <= n-4 cuts
        # pick t* as an element of Tpp with multiplicity 1 (simple tie): just pick a random element,
        # check its multiplicity in Tpp (exact equality check)
        if not Tpp:
            continue
        idx = random.randrange(len(Tpp))
        tstar = Tpp[idx]
        mult = sum(1 for x in Tpp if x == tstar)
        if mult % 2 == 0:
            continue  # skip even-multiplicity case, out of scope for this check
        trials_total += 1
        B = [tstar, p4] + Tpp  # b=tstar, plus p4, plus T''
        AB = A(B)
        bound = fn + tstar
        slack = AB - bound
        if slack < -Fr(1,10**12):
            violations += 1
            print("VIOLATION", n, tstar, AB, bound)
        if min_slack is None or slack < min_slack:
            min_slack = slack

print("trials checked (odd-mult only):", trials_total)
print("violations:", violations)
print("min slack (AB - (f(n)+t*)):", min_slack, float(min_slack))

# debug: check whether A(T''\{t*}) == Total(T''\{t*}) always
random.seed(1)
n=6
p = ladder(n); p4=p[3]; tail=p[4:]; fn=f(n)
for trial in range(5):
    Tpp = random_legal_refinement(tail, n-4)
    if not Tpp: continue
    idx = random.randrange(len(Tpp))
    tstar = Tpp[idx]
    mult = sum(1 for x in Tpp if x==tstar)
    if mult%2==0: continue
    rest = list(Tpp)
    rest.remove(tstar)
    print("Tpp=",Tpp)
    print("rest=",rest, "A(rest)=",A(rest), "Total(rest)=",sum(rest))
