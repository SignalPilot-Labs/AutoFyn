import sys, time
from sim import gen_sequence
from sympy import primefactors

a1 = int(sys.argv[1])
N = int(sys.argv[2])
t0=time.time()
a, history = gen_sequence(a1, N)
print(f"gen time {time.time()-t0:.1f}s")
P1 = frozenset(primefactors(a1))
print("P1=", sorted(P1))

# print full antichain state whenever it changes
prev = None
changes = []
for n in range(1, N+1):
    cur = history[n]
    if cur != prev:
        changes.append((n, cur))
        prev = cur
print(f"total distinct antichain STATES (changes) = {len(changes)}")
for n, st in changes:
    print(f"n={n}: size={len(st)} :: " + ", ".join(str(sorted(s)) for s in sorted(st, key=lambda x:(len(x),sorted(x)))))
