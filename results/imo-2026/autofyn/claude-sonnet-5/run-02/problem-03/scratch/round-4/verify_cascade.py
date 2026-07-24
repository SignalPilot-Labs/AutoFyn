from fractions import Fraction as F

def ladder(n):
    D = 2**(n+1)-1
    return [F(2**(n+1-i), D) for i in range(1, n+2)]  # p_1..p_{n+1}

def phi(pieces):
    s = sorted(pieces, reverse=True)
    return sum(s[i] for i in range(0, len(s), 2))

def cascade_k(pl, k):
    n = len(pl)-1
    # cut p_1..p_k each into (p_{i+1},p_{i+1}); leave p_{k+1..n+1} untouched
    out = []
    for i in range(1, k+1):
        out += [pl[i], pl[i]]   # p_{i+1} is pl[i] (0-indexed: pl[0]=p_1,... pl[i]=p_{i+1})
    out += pl[k:]  # p_{k+1},...,p_{n+1} untouched  (0-indexed pl[k] = p_{k+1})
    return out

for n in range(1, 9):
    pl = ladder(n)
    target = F(2**n, 2**(n+1)-1)
    for k in [n-1, n]:
        if k < 0: continue
        mset = cascade_k(pl, k)
        val = phi(mset)
        assert len(mset) == (n+1) + k
        status = "MATCH" if val == target else f"MISMATCH got {val}"
        print(f"n={n} k={k}: phi={val}  target={target}  {status}")
