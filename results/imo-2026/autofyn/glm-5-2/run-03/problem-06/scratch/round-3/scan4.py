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

# |P1|=3 cases — run longer
for a1 in [105, 385, 1001, 1309, 2431, 2485, 3233, 4199, 5183, 7429]:
    seq = greedy_seq(a1, 12000)
    res = detect_period_strict(seq, window=2000, maxT=3000)
    if res:
        T, L = res
        Lf = sympy.factorint(L)
        P1 = sympy.primefactors(a1)
        gov = sorted(Lf.keys())
        nonP1 = [p for p in gov if p not in P1]
        ok = all(p <= a1 for p in gov)
        print(f'a1={a1}={sympy.factorint(a1)}: T={T}, L={Lf}, P1={P1}, nonP1-gov={nonP1}, max-nonP1={max(nonP1) if nonP1 else None}, all<=M1={a1}: {ok}')
    else:
        print(f'a1={a1}={sympy.factorint(a1)}: no period in 12000 terms')
