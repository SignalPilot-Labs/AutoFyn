import sympy

def fast_greedy_track(a1, N):
    a=[a1]; minimal=[frozenset(sympy.primefactors(a1))]
    big_transient=[]
    M1 = sympy.prod(sorted(set(sympy.primefactors(a1))))
    adds=0
    for step in range(N-1):
        cur=a[-1]; m=cur+1
        while True:
            ms=frozenset(sympy.primefactors(m))
            if all(ms&S for S in minimal):
                a.append(m)
                if not any(S<=ms for S in minimal):
                    minimal=[S for S in minimal if not(ms<=S)]; minimal.append(ms)
                    adds+=1
                    mx = max(ms)
                    if mx > M1:
                        big_transient.append((step+2, sorted(ms), mx, m))
                break
            m+=1
    return minimal, adds, big_transient, M1

for a1, N in [(385, 12000), (1309, 12000), (2085, 12000), (116, 1500), (145, 3000)]:
    minimal, adds, big, M1 = fast_greedy_track(a1, N)
    print(f"a1={a1} (M1={M1}): #adds={adds}, #big_transient(prime>M1)={len(big)}")
    if big: print(f"  first 5 big: {big[:5]}")
    print(f"  final MS: {sorted([sorted(s) for s in minimal])}")
