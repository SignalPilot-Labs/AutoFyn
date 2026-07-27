import sys, math, signal
from sympy import factorint, prime
exec(open('/tmp/round-2/sweep3.py').read().split("if __name__")[0])

import itertools
print("=== omega=3 (selected triples) ===")
triples = [(2,3,5),(3,5,7),(5,7,11),(7,11,13),(11,13,17),(13,17,19),(17,19,23),(23,29,31),(29,31,37),(37,41,43),(41,43,47),(53,59,61),(71,73,79),(97,101,103),(113,173,179)]
for t in triples:
    a1=1
    for x in t: a1*=x
    res = run(a1, max_rounds=150, max_Pess=26, time_limit=25)
    flag = 'STABLE' if res['stable'] else ('CAP' if res['stable'] is None else 'UNST')
    print(f"a1={a1} {t}: {flag} |Pess|={len(res['P_ess'])} |M|={len(res['M'])} {res.get('reason')}")

print()
print("=== omega=4 (selected) ===")
quads=[(2,3,5,7),(3,5,7,11),(5,7,11,13),(7,11,13,17),(11,13,17,19),(17,19,23,29),(29,31,37,41),(41,43,47,53)]
for t in quads:
    a1=1
    for x in t: a1*=x
    res = run(a1, max_rounds=100, max_Pess=22, time_limit=20)
    flag = 'STABLE' if res['stable'] else ('CAP' if res['stable'] is None else 'UNST')
    print(f"a1={a1} {t}: {flag} |Pess|={len(res['P_ess'])} |M|={len(res['M'])} {res.get('reason')}")

print()
print("=== verbose history: a1=19549 (113,173) omega=2 ===")
res = run(19549, max_rounds=400, max_Pess=40, time_limit=90)
print("final |Pess|",len(res['P_ess']),"|M|",len(res['M']),"stable",res['stable'],"reason",res.get('reason'))
for h in res['history']:
    print(f"  a={h['a']} |M|={h['M']} |Pess|={h['Pess']} |T*|={len(h['Tstar'])} new={h['newpr']}")
