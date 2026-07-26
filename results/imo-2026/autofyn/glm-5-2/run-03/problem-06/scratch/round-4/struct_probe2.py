import sys
sys.path.insert(0, '/tmp/round-3')
from sim import greedy_seq
from sympy import primefactors
from collections import Counter

def detect_period_from_start(seq, maxT=None):
    diffs = [seq[i+1]-seq[i] for i in range(len(seq)-1)]
    N = len(diffs)
    if maxT is None: maxT = min(N//3, 6500)
    for T in range(1, maxT+1):
        ok = all(diffs[k] == diffs[k+T] for k in range(N-T))
        if ok and N-T >= T:
            return T, sum(diffs[:T]), diffs[:T]
    return None

def primitive_period_len(w):
    """Smallest m | len(w) such that w = u^k with |u|=m."""
    T = len(w)
    for m in range(1, T+1):
        if T % m == 0:
            if all(w[i]==w[i % m] for i in range(T)):
                return m
    return T

def cyclic_letter_perm_invariance(w):
    """Is w invariant under a nontrivial cyclic permutation of its alphabet (length-1 substitution = letter perm)?"""
    alpha = sorted(set(w))
    n = len(alpha)
    if n < 2: return None
    inv = {c:i for i,c in enumerate(alpha)}
    # try every permutation sigma of the alphabet; check w fixed as a word
    from itertools import permutations
    for perm in permutations(range(n)):
        if perm == tuple(range(n)): continue
        sigma = {alpha[i]: alpha[perm[i]] for i in range(n)}
        if all(sigma[w[i]] == w[i] for i in range(len(w))):
            return perm
    return None

for a1 in [15, 35, 77, 91, 105, 143, 1309, 2085, 65, 1001]:
    M1 = 1
    for p in primefactors(a1): M1 *= p
    N = 14000 if a1 in (1309,2085) else (4000 if a1!=1001 else 6000)
    seq = greedy_seq(a1, N)
    res = detect_period_from_start(seq)
    if res is None:
        print(f"a1={a1}: no period (need more terms)"); continue
    T, L, w = res
    m = primitive_period_len(w)
    alpha = sorted(set(w))
    perm = cyclic_letter_perm_invariance(w) if len(alpha)<=8 else "skip"
    print(f"a1={a1} T={T}: primitive |u|={m} (so w=u^{T//m}); alphabet={alpha}, "
          f"letter-perm-invariant: {perm}")
    if m <= 40:
        print(f"   u={w[:m]}")
