import sys
sys.path.insert(0,'/tmp/round-14')
from gen import gen_sequence
from sympy import factorint

# Quick sanity: does a moderately hard class have recurring small |comp| members?
a1 = 21528751
N = 8000
terms, rads = gen_sequence(a1, N)
P1 = set(factorint(a1).keys())
print("P1=",P1)
from collections import defaultdict
by_core = defaultdict(list)
for idx,(v,R) in enumerate(zip(terms,rads), start=1):
    core = frozenset(R & P1)
    comp = R - P1
    by_core[core].append((idx, len(comp)))

for core, lst in sorted(by_core.items(), key=lambda x: -len(x[1]))[:6]:
    sizes = [s for _,s in lst]
    small_count = sum(1 for s in sizes if s<=2)
    print(f"core={set(core)}, |class|={len(lst)}, #comp<=2: {small_count}, last 10 sizes: {sizes[-10:]}")
