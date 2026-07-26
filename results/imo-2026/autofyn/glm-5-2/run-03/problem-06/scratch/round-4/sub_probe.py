import sys, math
sys.path.insert(0, '/tmp/round-3')
from sim import greedy_seq
from sympy import factorint, primefactors
from collections import Counter

def detect_period_from_start(seq, maxT=None):
    """Detect period (T,L) with d_n periodic from n=1 (a_{n+T}=a_n+L for all n>=1)."""
    diffs = [seq[i+1]-seq[i] for i in range(len(seq)-1)]
    N = len(diffs)
    if maxT is None: maxT = min(N//3, 6000)
    for T in range(1, maxT+1):
        # check d_n == d_{n+T} for all n in [0, N-1-T)
        ok = True
        for k in range(N - T):
            if diffs[k] != diffs[k+T]:
                ok=False; break
        if ok and N-T >= T:  # at least ~2 periods seen
            L = sum(diffs[:T])
            return T, L, diffs[:T]
    return None

def is_power_of_smaller_word(w):
    """Is w = u^k for some smaller u, k>=2? Return (u,k) or None."""
    T = len(w)
    for k in range(2, T+1):
        if T % k == 0:
            m = T // k
            u = w[:m]
            if all(w[i]==u[i % m] for i in range(T)):
                return u, k
    return None

def subword_complexity(w, maxL=None):
    """Number of distinct factors of each length. Bounded => automatic-ish."""
    if maxL is None: maxL = min(len(w)//2, 30)
    out = []
    for L in range(1, maxL+1):
        factors = set()
        for i in range(len(w)-L+1):
            factors.add(tuple(w[i:i+L]))
        out.append((L, len(factors)))
    return out

for a1 in [6, 15, 21, 35, 65, 77, 91, 105, 143, 385, 1309, 741, 145, 116, 2085]:
    M1 = 1
    for p in primefactors(a1): M1 *= p
    N = 14000 if a1 in (385,1309,2085) else 4000
    seq = greedy_seq(a1, N)
    res = detect_period_from_start(seq, maxT=min(N//3,6500))
    if res is None:
        print(f"a1={a1}: no period from n=1 found in {N} terms (maxT={min(N//3,6500)})")
        continue
    T, L, w = res
    pw = is_power_of_smaller_word(w)
    pwstr = f"  = u^{pw[1]}, |u|={len(pw[0])}, u_comp={is_power_of_smaller_word(pw[0])}" if pw else ""
    gov = sorted(factorint(L).keys())
    print(f"a1={a1} (M1={M1}): T={T}, L={L}={factorint(L)}, gov-primes={gov}, "
          f"all-gov<=M1: {all(q<=M1 for q in gov)}{pwstr}")
    # alphabet of d
    alpha = sorted(set(w))
    print(f"    alphabet of d: {alpha} (max possible 1..{M1})")
    # subword complexity (first few)
    sc = subword_complexity(w, maxL=min(20, T//2))
    print(f"    subword_complexity (L,|Factors|): {sc[:12]}{'...' if len(sc)>12 else ''}")
    # letter frequencies
    cnt = Counter(w)
    # is the word a fixed point of a uniform substitution? Check if each letter appears with rational freq = c/T
    print(f"    letter freqs: {dict(sorted(cnt.items()))}  (period T={T})")
