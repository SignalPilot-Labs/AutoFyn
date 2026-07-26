import sys
sys.path.insert(0, '/tmp/round-3')
from sim import greedy_seq
import sympy

def detect_period_strict(seq, window, maxT):
    diffs = [seq[i+1]-seq[i] for i in range(len(seq)-1)]
    N = len(diffs)
    for T in range(1, min(maxT, N - window) + 1):
        ok = True
        for k in range(window):
            if diffs[N - window - T + k] != diffs[N - window + k]:
                ok = False; break
        if ok:
            return T, sum(diffs[-T:])
    return None

tests = [75, 175, 245, 275, 425, 539, 845, 1855]
for a1 in tests:
    seq = greedy_seq(a1, 2500)
    res = detect_period_strict(seq, window=600, maxT=600)
    if res:
        T, L = res
        Lf = sympy.factorint(L)
        P1 = sympy.primefactors(a1)
        gov = sorted(Lf.keys())
        nonP1 = [p for p in gov if p not in P1]
        print(f'a1={a1}={sympy.factorint(a1)}: T={T}, L={Lf}, P1={P1}, nonP1-gov={nonP1}, max-nonP1={max(nonP1) if nonP1 else None}')
    else:
        print(f'a1={a1}={sympy.factorint(a1)}: no period in 2500 terms')
