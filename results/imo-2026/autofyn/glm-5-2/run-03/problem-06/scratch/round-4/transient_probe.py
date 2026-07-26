import sympy

def fast_greedy_track(a1, N):
    a=[a1]; minimal=[frozenset(sympy.primefactors(a1))]
    history=[]  # (step, action, support, max_prime_in_it)
    M1 = sympy.prod(sorted(set(sympy.primefactors(a1))))
    for step in range(N-1):
        cur=a[-1]; m=cur+1
        while True:
            ms=frozenset(sympy.primefactors(m))
            if all(ms&S for S in minimal):
                a.append(m)
                # check if ms changes the minimal family
                if not any(S<=ms for S in minimal):
                    # ms is a new minimal; remove supersets
                    removed=[S for S in minimal if ms<=S]
                    minimal=[S for S in minimal if not(ms<=S)]; minimal.append(ms)
                    mx = max(ms)
                    history.append((step+2, "ADD", sorted(ms), mx, mx>M1, removed))
                break
            m+=1
    return a, minimal, history, M1

for a1, N in [(15, 300), (77, 300), (35, 500), (175, 2000), (847, 4000)]:
    a, minimal, hist, M1 = fast_greedy_track(a1, N)
    print(f"\na1={a1} (M1={M1}): #minimal_final={len(minimal)}")
    # Any transient minimal support with a prime > M1?
    big_transient = [h for h in hist if h[4]]
    print(f"  total minimal-additions: {len(hist)}")
    print(f"  minimal-additions with prime > M1: {len(big_transient)}")
    if big_transient:
        print(f"  sample (first 5): {big_transient[:5]}")
    # final state
    final_max = max(max(s) for s in minimal)
    print(f"  final minimal supports: {sorted([sorted(s) for s in minimal])}")
    print(f"  final max prime: {final_max} (<=M1? {final_max<=M1})")
