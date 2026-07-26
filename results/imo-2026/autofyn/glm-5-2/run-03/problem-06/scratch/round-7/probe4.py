"""Find the D_n-window conflict pair for a_1=175; check if transient."""
import math
from collections import defaultdict


def sieve(limit):
    s = bytearray([1]) * (limit + 1)
    s[0] = s[1] = 0
    for i in range(2, int(limit ** 0.5) + 1):
        if s[i]:
            for j in range(i * i, limit + 1, i):
                s[j] = 0
    return [i for i in range(2, limit + 1) if s[i]]


def naive_greedy(a1, N):
    a = [a1]
    for n in range(N - 1):
        m = a[n] + 1
        while True:
            ok = True
            for ai in a:
                if math.gcd(m, ai) == 1:
                    ok = False
                    break
            if ok:
                break
            m += 1
        a.append(m)
    return a


def compute_Dn(a, n, M1):
    an = a[n]
    Dn = []
    for d in range(1, M1 + 1):
        m = an + d
        ok = True
        for ai in a[:n + 1]:
            if math.gcd(m, ai) == 1:
                ok = False
                break
        if ok:
            Dn.append(d)
    return frozenset(Dn)


a1 = 175
N = 1200
M1 = 35
a = naive_greedy(a1, N)
d = [a[i+1]-a[i] for i in range(N-1)]
Nc = 600
Ds = {n: compute_Dn(a, n, M1) for n in range(Nc)}

# Find conflict pairs at k=1: D_n == D_m but d[n+1] != d[m+1]
print("k=1 conflicts (D_n==D_m, d_{n+1}!=d_{m+1}):")
seen = {}
for n in range(Nc - 2):
    Dn = Ds[n]
    dnext = d[n+1]
    if Dn in seen:
        for m in seen[Dn]:
            if d[m+1] != dnext:
                print(f"  CONFLICT: n={n}, m={m}, D_n=D_m={set(Dn)}, d_{{n+1}}={dnext}, d_{{m+1}}={d[m+1]}")
                # check backward history
                print(f"    n: a[n]={a[n]}, a[n-1]={a[n-1] if n>0 else 'NA'}")
                print(f"    m: a[m]={a[m]}, a[m-1]={a[m-1] if m>0 else 'NA'}")
                # check how far back the D-history matches
                match_back = 0
                for j in range(1, min(n, m)+1):
                    if Ds.get(n-j) == Ds.get(m-j):
                        match_back = j
                    else:
                        break
                print(f"    backward D-match depth: {match_back}")
                # check forward: do they separate?
                sep_at = None
                for j in range(2, min(Nc-n, Nc-m)):
                    if Ds.get(n+j) != Ds.get(m+j):
                        sep_at = j
                        break
                print(f"    forward D-separation at: {sep_at}")
    else:
        seen[Dn] = []
    seen[Dn].append(n)

# preperiod: find where d becomes 274-periodic
for T in [274]:
    for start in range(0, Nc - 2*T):
        if all(d[start+i] == d[start+i+T] for i in range(T)):
            print(f"  d is {T}-periodic from index {start}")
            break
