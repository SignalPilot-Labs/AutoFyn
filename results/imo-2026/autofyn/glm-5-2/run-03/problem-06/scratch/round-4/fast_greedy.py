import sys
from math import gcd

def fast_greedy(a1, N):
    """Greedy with maximal-support tracking for fast admissibility."""
    a = [a1]
    supps = [set(__import__('sympy').primefactors(a1))]  # S(a_i)
    maximal = [supps[0]]  # inclusion-maximal supports (live constraints)
    for _ in range(N-1):
        cur = a[-1]
        m = cur + 1
        while True:
            ms = set(__import__('sympy').primefactors(m))
            # admissible: ms hits every maximal support
            if all(ms & S for S in maximal):
                a.append(m)
                # update maximal: remove subsets of ms, add ms if not subsumed
                new_max = []
                subsumed = False
                for S in maximal:
                    if ms >= S:
                        subsumed = True  # S is subset of ms -> S redundant? no: S subset ms means constraint_S weaker... 
                        # actually if ms >= S then constraint_S = Union_{p in S} pZ subset Union_{p in ms} pZ = constraint_new
                        # so constraint_S is IMPLIED by constraint_new. S is redundant. drop it.
                        continue
                    if S >= ms:
                        # ms subset S -> constraint_ms subset constraint_S -> ms redundant (implied). ms adds nothing.
                        subsumed = True
                    new_max.append(S)
                if not subsumed or True:  # always add ms if it's not a subset of any kept
                    # check: is ms subset of any new_max?
                    if not any(S >= ms for S in new_max):
                        new_max.append(ms)
                maximal = new_max
                break
            m += 1
    return a

# Test correctness on small case first
a_test = fast_greedy(15, 20)
print("a1=15:", a_test[:12])
