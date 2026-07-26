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
seq = greedy_seq(385, 30000)
res = detect_period_from_start(seq, maxT=6500)
if res:
    T, L, w = res
    M1=385
    print(f"a1=385 T={T} L={L} gov={sorted(__import__('sympy').factorint(L).keys())} pal={is_palindrome(w)}")
    s=w[0]+w[-1]
    print(f"  anti-pal const={s}: {all(w[i]+w[T-1-i]==s for i in range(T))}")
else:
    print("a1=385: no period found in 30000 terms (T>6500?)")
