import sys
sys.path.insert(0,'.')
from lp_search2 import ladder, build_elems, min_phi_for_composition, describe_vertex
from fractions import Fraction as F

n = int(sys.argv[1])
comp = tuple(int(x) for x in sys.argv[2].split(','))
p = ladder(n)
val, info = min_phi_for_composition(p, comp)
print("n=",n,"comp=",comp,"val=",val, "target=", 2**n/(2**(n+1)-1))
elems, nvars = build_elems(p, comp)
# print first unique-value result
seen=set()
for perm, x, v in info:
    vals, labels = describe_vertex(elems, perm, x, p)
    key = tuple(round(vv,6) for vv in vals)
    if key in seen: continue
    seen.add(key)
    print("vals:", [round(vv,6) for vv in vals])
    print("labels:", labels)
    denom = 2**(n+1)-1
    print("as fractions of 1/%d:"%denom, [round(vv*denom,4) for vv in vals])
