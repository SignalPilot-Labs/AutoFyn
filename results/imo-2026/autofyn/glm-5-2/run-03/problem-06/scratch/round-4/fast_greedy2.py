import sympy
from math import gcd

def fast_greedy(a1, N):
    a = [a1]
    minimal = [set(sympy.primefactors(a1))]  # inclusion-minimal supports (LIVE constraints)
    for _ in range(N-1):
        cur = a[-1]; m = cur + 1
        while True:
            ms = set(sympy.primefactors(m))
            if all(ms & S for S in minimal):  # hits every live constraint
                a.append(m)
                # update minimal: ms is live. Remove supports that are SUPERSETS of ms (now redundant).
                # ms itself: is it a superset of an existing minimal? then ms redundant (don't add).
                if not any(S <= ms for S in minimal):  # ms not a superset of any existing -> ms is new-minimal
                    minimal = [S for S in minimal if not (ms <= S)]  # drop supersets of ms
                    minimal.append(ms)
                break
            m += 1
    return a

# correctness check
for a1,N in [(15,12),(77,22),(35,40)]:
    a = fast_greedy(a1,N)
    print(f"a1={a1}:", a[:14])
