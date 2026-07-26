import sympy

def track(a1, N):
    a=[a1]; minimal=[frozenset(sympy.primefactors(a1))]
    M1 = sympy.prod(sorted(set(sympy.primefactors(a1))))
    big=[]; adds=0
    for step in range(N-1):
        cur=a[-1]; m=cur+1
        while True:
            ms=frozenset(sympy.primefactors(m))
            if all(ms&S for S in minimal):
                a.append(m)
                if not any(S<=ms for S in minimal):
                    minimal=[S for S in minimal if not(ms<=S)]; minimal.append(ms)
                    adds+=1
                    if max(ms) > M1: big.append((step+2, sorted(ms), max(ms)))
                break
            m+=1
    return minimal, adds, big, M1

# Non-LOCK cases (squarefree a_1 with >=2 primes, not prime-power, not locking)
cases = [(2*3*5*7*11*13, 3000), (2*3*5*7*11*17, 3000), (2*3*5*7*13, 3000),
         (3*5*7*11, 3000), (2*5*7*11, 3000), (2*3*5*11, 3000), (2*3*7*11, 3000),
         (2*3*5*7*11, 4000), (13*17*19, 3000), (2*3*5*7*11*13*17, 2000)]
for a1, N in cases:
    minimal, adds, big, M1 = track(a1, N)
    print(f"a1={a1} (M1={M1}): #adds={adds}, #big_transient={len(big)}")
    if big: print(f"  first 3 big: {big[:3]}")
    print(f"  final MS primes max: {max(max(s) for s in minimal)} (<=M1? {max(max(s) for s in minimal)<=M1})")
