import sys, itertools, math, signal
from sympy import factorint, primerange, prime
exec(open('/tmp/round-2/sweep3.py').read().split("if __name__")[0])

print("=== omega=3 (small prime triples) ===")
sp = list(primerange(2, 30))
for p,q,r in itertools.combinations(sp, 3):
    a1 = p*q*r
    res = run(a1, max_rounds=200, max_Pess=24, time_limit=20)
    flag = 'STABLE' if res['stable'] else ('CAP' if res['stable'] is None else 'UNST')
    print(f"a1={a1} ({p},{q},{r}): {flag} |Pess|={len(res['P_ess'])} |M|={len(res['M'])} {res.get('reason')}")

print()
print("=== omega=4 (small) ===")
sp4 = list(primerange(2,16))
for p,q,r,s in itertools.combinations(sp4,4)[:14]:
    a1=p*q*r*s
    res = run(a1, max_rounds=120, max_Pess=20, time_limit=18)
    flag = 'STABLE' if res['stable'] else ('CAP' if res['stable'] is None else 'UNST')
    print(f"a1={a1} ({p},{q},{r},{s}): {flag} |Pess|={len(res['P_ess'])} |M|={len(res['M'])} {res.get('reason')}")

print()
print("=== verbose history: a1=19549 (113,173), omega=2, |Pess|=32 ===")
res = run(19549, max_rounds=400, max_Pess=40, time_limit=60)
print("final |Pess|",len(res['P_ess']),"|M|",len(res['M']),"stable",res['stable'])
for h in res['history']:
    print(f"  a={h['a']} |M|={h['M']} |Pess|={h['Pess']} T*={h['Tstar']} new={h['newpr']}")
