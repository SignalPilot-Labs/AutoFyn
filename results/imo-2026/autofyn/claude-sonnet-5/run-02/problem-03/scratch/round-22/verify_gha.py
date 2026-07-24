from fractions import Fraction as F
import random

def A(S):
    # S: list of values (not necessarily sorted)
    S = sorted(S, reverse=True)
    total = F(0)
    for i, v in enumerate(S):
        sign = 1 if i % 2 == 0 else -1
        total += sign * v
    return total

def test_insert_identity(trials=20000):
    random.seed(1)
    fails = 0
    for _ in range(trials):
        k = random.randint(0, 6)
        Tp = [F(random.randint(1,1000), random.randint(1,1000)) for _ in range(k)]
        b = F(random.randint(0,1000), random.randint(1,1000))
        j = sum(1 for t in Tp if t > b)
        lhs = A([b] + Tp)
        Tgt_b = [t for t in Tp if t > b]
        rhs = 2*A(Tgt_b) - A(Tp) + ((-1)**j) * b
        if lhs != rhs:
            fails += 1
            if fails < 5:
                print("FAIL", Tp, b, lhs, rhs)
    print(f"Insert-Element Identity: {trials} trials, fails={fails}")

test_insert_identity()

def ladder(n):
    D = 2**(n+1)-1
    f = F(1, D)
    return [F(2**(n+1-i))*f for i in range(1, n+2)]  # p_1..p_{n+1}

def test_rescaling_lemma():
    fails = 0
    for n in range(2, 10):
        p = ladder(n)  # p[0]=p_1 ... p[n]=p_{n+1}, length n+1
        f_n = F(1, 2**(n+1)-1)
        for k in range(0, n):
            m = n - k
            f_m = F(1, 2**(m+1)-1)
            lam = f_n / f_m
            qm = ladder(m)  # q_1..q_{m+1}, length m+1
            for i in range(1, m+2):
                lhs = p[k+i-1]  # p_{k+i}, p indexed 1..n+1 -> p[idx-1]
                rhs = lam * qm[i-1]
                if lhs != rhs:
                    fails += 1
                    print("FAIL rescaling", n, k, i, lhs, rhs)
            # check lam*f_m == f_n
            if lam*f_m != f_n:
                fails += 1
                print("FAIL lam*f_m", n, k)
    print(f"Rescaling lemma: fails={fails}")

test_rescaling_lemma()

def random_legal_refinement(pieces, budget):
    # distribute `budget` cuts among len(pieces) pieces randomly (0..budget each, sum<=budget)
    r = len(pieces)
    # random composition of budget into r nonneg parts summing to <= budget
    cuts = [0]*r
    remaining = budget
    for i in range(r):
        c = random.randint(0, remaining)
        cuts[i] = c
        remaining -= c
    out = []
    for i, piece in enumerate(pieces):
        c = cuts[i]
        if c == 0:
            out.append(piece)
        else:
            # random cut points strictly inside (0, piece)
            pts = sorted(F(random.randint(1, 999999), 1000000) * piece for _ in range(c))
            prev = F(0)
            for pt in pts:
                out.append(pt - prev)
                prev = pt
            out.append(piece - prev)
    return out

def test_theorem36b(trials=4000):
    for n in range(4, 9):
        D = 2**(n+1)-1
        f_n = F(1, D)
        p = ladder(n)
        R_pieces = p[2:]   # p_3 .. p_{n+1} (0-indexed p[2]..p[n])
        budget = n - 3
        minA = None
        random.seed(n)
        for _ in range(trials):
            Rp = random_legal_refinement(R_pieces, budget)
            a = A(Rp)
            if minA is None or a < minA:
                minA = a
        margin = minA - f_n
        print(f"n={n}: min A(R') over {trials} trials = {float(minA):.6f}, f(n)={float(f_n):.6f}, margin={float(margin):.6f}")

test_theorem36b()
