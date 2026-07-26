from math import gcd
def greedy(a1, N):
    a = [a1]
    for _ in range(N-1):
        cur = a[-1]; m = cur + 1
        while True:
            if all(gcd(m, x) > 1 for x in a):
                a.append(m); break
            m += 1
    return a

# big N for a1=65
a = greedy(65, 20000)
d = [a[i+1]-a[i] for i in range(len(a)-1)]
# strict period: find T such that d[n0+T]==d[n0] for ALL n>=n0, with longest run
# scan for the true eventual period using autocorrelation
n = len(d)
for T in range(1, 300):
    # count max run of equality starting from the tail
    run = 0
    i = n - 1
    while i - T >= 0 and d[i] == d[i-T]:
        run += 1; i -= 1
    if run >= 1000:
        L = sum(d[i:i+T])
        print(f"T={T}, tail-run={run}, L={L}, n0~={i}, L factors: ", end='')
        import sympy
        print(sympy.factorint(L))
