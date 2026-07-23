import time
from sim import gen_sequence

a1 = 21528751
N = 30000
t0=time.time()
a, history = gen_sequence(a1, N)
print("gen time", time.time()-t0)

prev=None
chain_events=[]
for n in range(1,N+1):
    cur = history[n]
    if prev is not None and len(cur)<len(prev):
        removed = prev-cur
        added = cur-prev
        chain_events.append((n, added, removed))
    prev = cur

addedcores = {}
for n, added, removed in chain_events:
    for c in added:
        addedcores[c] = n

nested = []
for n, added, removed in chain_events:
    for r in removed:
        if r in addedcores and addedcores[r] < n:
            nested.append((tuple(sorted(r)), addedcores[r], n))

print('Nested (core added then later itself absorbed):')
for c, n1, n2 in nested:
    print(f'  core {c}: added at n={n1}, absorbed at n={n2}  (lived {n2-n1} steps)')
print('total nesting chain links:', len(nested))
print('total collapse events:', len(chain_events))
