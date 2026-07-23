import sympy

def gen(a1, N):
    a = [None, a1]
    rad = [None, set(sympy.primefactors(a1))]
    for n in range(1, N):
        x = a[n] + 1
        while True:
            rx = set(sympy.primefactors(x))
            ok = all(rx & rad[i] for i in range(1, n+1))
            if ok:
                a.append(x)
                rad.append(rx)
                break
            x += 1
    return a, rad

a1 = 247
N = 4000
a, rad = gen(a1, N)
P1 = {13,19}
G = [None]+[frozenset(rad[n] & P1) for n in range(1,N+1)]

# find minimal period via brute force scan on prefix (small N check only, not claiming full T=1806 here, just sanity)
def is_period(T, n0, upto):
    for n in range(n0+1, upto-T):
        if G[n] != G[n+T]:
            return False
    return True

# check T=1806 works from n0=0 up to N-1806
T = 1806
ok = is_period(T, 0, N)
print("period 1806 holds up to N=4000 check:", ok)

# max run avoiding S'={13}
def max_run_avoiding(S):
    best = 0
    cur = 0
    for n in range(1,N+1):
        if G[n] != frozenset(S):
            cur += 1
            best = max(best,cur)
        else:
            cur = 0
    return best

r13 = max_run_avoiding({13})
r19 = max_run_avoiding({19})
print("max run avoiding {13}:", r13, " avoiding {19}:", r19)
print("predicted bound R = n0+T =", 0+1806, " (should be >= actual max run)")
