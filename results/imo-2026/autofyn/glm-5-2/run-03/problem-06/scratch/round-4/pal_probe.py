import sys
sys.path.insert(0, '/tmp/round-3')
from sim import greedy_seq
from sympy import primefactors

def detect_period_from_start(seq, maxT=None):
    diffs = [seq[i+1]-seq[i] for i in range(len(seq)-1)]
    N = len(diffs)
    if maxT is None: maxT = min(N//3, 6500)
    for T in range(1, maxT+1):
        ok = all(diffs[k] == diffs[k+T] for k in range(N-T))
        if ok and N-T >= T:
            return T, sum(diffs[:T]), diffs[:T]
    return None

def is_palindrome(w):
    return all(w[i]==w[len(w)-1-i] for i in range(len(w)//2))

for a1 in [15, 35, 65, 77, 91, 105, 143, 1001, 1309, 2085]:
    M1 = 1
    for p in primefactors(a1): M1 *= p
    N = 14000 if a1 in (1309,2085) else (6000 if a1 in (1001,143) else 4000)
    seq = greedy_seq(a1, N)
    res = detect_period_from_start(seq)
    if res is None:
        print(f"a1={a1}: no period"); continue
    T, L, w = res
    print(f"a1={a1} T={T}: period palindrome? {is_palindrome(w)}")
    # also check: is it a double-palindrome or has reflection symmetry w[i]=w[T-i]?
    # check anti-palindrome: w[i] + w[T-1-i] = const?
    s = w[0]+w[-1]
    anti = all(w[i]+w[T-1-i]==s for i in range(T))
    print(f"   anti-palindrome (w[i]+w[T-1-i]=const={s})? {anti}")
    # check if w[T//2] (middle) equals s/2 when T odd
