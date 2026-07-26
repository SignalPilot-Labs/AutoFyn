import sys
sys.path.insert(0, '/tmp/round-3')
from sim import greedy_seq
import sympy

def detect_period_strict(seq, window=1500, maxT=1500):
    diffs = [seq[i+1]-seq[i] for i in range(len(seq)-1)]
    N = len(diffs)
    for T in range(1, min(maxT, N - window) + 1):
        ok = True
        for k in range(window):
            if diffs[N - window - T + k] != diffs[N - window + k]:
                ok = False; break
        if ok:
            L = sum(diffs[-T:])
            return T, L
    return None

for a1 in [15, 35, 65, 77, 91, 143, 221, 437, 667, 899, 1147, 1517, 1763, 2491]:
    seq = greedy_seq(a1, 7000)
    res = detect_period_strict(seq, window=1500, maxT=1500)
    if res:
        T, L = res
        Lf = sympy.factorint(L)
        P1 = sympy.primefactors(a1)
        gov = sorted(Lf.keys())
        nonP1 = [p for p in gov if p not in P1]
        ok = all(p <= a1 for p in gov)
        print(f'a1={a1}={sympy.factorint(a1)}: T={T}, L={L}={Lf}, P1={P1}, gov={gov}, nonP1-gov={nonP1}, all<=M1={a1}: {ok}')
    else:
        print(f'a1={a1}={sympy.factorint(a1)}: no period detected in 7000 terms')
