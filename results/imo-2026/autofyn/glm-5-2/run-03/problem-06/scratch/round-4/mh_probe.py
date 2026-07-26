import sys
sys.path.insert(0, '/tmp/round-3')
from sim import greedy_seq
from sympy import factorint, primefactors

def detect_period_from_start(seq, maxT=None):
    diffs = [seq[i+1]-seq[i] for i in range(len(seq)-1)]
    N = len(diffs)
    if maxT is None: maxT = min(N//3, 6500)
    for T in range(1, maxT+1):
        ok = True
        for k in range(N - T):
            if diffs[k] != diffs[k+T]:
                ok=False; break
        if ok and N-T >= T:
            L = sum(diffs[:T])
            return T, L, diffs[:T]
    return None

def subword_complexity_full(w, maxL):
    out = []
    for L in range(1, maxL+1):
        factors = set()
        for i in range(len(w)-L+1):
            factors.add(tuple(w[i:i+L]))
        out.append((L, len(factors)))
    return out

# For small-T cases, find the first n where p(n) <= n (Morse-Hedlund threshold)
for a1 in [15, 35, 77, 91, 105, 143]:
    M1 = 1
    for p in primefactors(a1): M1 *= p
    seq = greedy_seq(a1, 4000)
    res = detect_period_from_start(seq)
    T, L, w = res
    # double the word to get wraparound factors
    wext = w + w + w
    sc = subword_complexity_full(wext, min(T+5, 40))
    # find first n with p(n) <= n
    first_mh = None
    for (n, pn) in sc:
        if pn <= n:
            first_mh = (n, pn); break
    print(f"a1={a1} T={T}: first n with p(n)<=n: {first_mh} (sc={sc[:min(len(sc),15)]})")
