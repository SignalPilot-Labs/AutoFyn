from math import gcd

def primefactors(n):
    s = set(); d = 2
    while d*d <= n:
        while n % d == 0: s.add(d); n //= d
        d += 1
    if n > 1: s.add(n)
    return s

def seq_plain(a1, N):
    a = [a1]
    while len(a) < N:
        m = a[-1] + 1
        while any(gcd(m, x) == 1 for x in a): m += 1
        a.append(m)
    return a

def minimal_sets(sets):
    out = []
    for s in sets:
        if any(t <= s for t in out): continue
        out = [t for t in out if not (s < t)]
        out.append(s)
    return out

def pi(A):
    r = 1
    for p in A: r *= p
    return r

# Test Lemma 3: every non-member m in (a1, a_N] has a coprime term below it
# Test Lemma 4: for B in Bfam, p in B with pi(B\{p}) > a1, exists B' in Bfam
#               with B' ∩ B = {p} and pi(B') < pi(B)/p
for a1, N in [(35, 600), (221, 700), (1001, 700), (15, 400)]:
    a = seq_plain(a1, N)
    aset = set(a)
    Bfam = [frozenset(b) for b in minimal_sets([primefactors(x) for x in a])]
    # Lemma 3 check
    bad3 = 0
    for m in range(a1+1, a[N//2]):
        if m in aset: continue
        if not any(gcd(s, m) == 1 for s in a if s < m): bad3 += 1
    # Lemma 4 check
    bad4 = []
    for B in Bfam:
        for p in B:
            if pi(B - {p}) > a1:
                ok = any((Bp & B == {p}) and pi(Bp) < pi(B)//p for Bp in Bfam)
                if not ok: bad4.append((sorted(B), p))
    print(f"a1={a1}: Bfam={sorted(map(sorted,Bfam))}")
    print(f"   Lemma3 violations={bad3}, Lemma4 violations={bad4}")
