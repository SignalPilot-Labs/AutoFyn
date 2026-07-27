import sys, math, signal
from sympy import factorint
exec(open('/tmp/round-2/sweep3.py').read().split("if __name__")[0])

# final M structure for small saturated cases
for a1 in [15, 35, 65, 187, 221]:
    res = run(a1, max_rounds=200, max_Pess=30, time_limit=20)
    print(f"a1={a1}: |M|={len(res['M'])} |Pess|={len(res['P_ess'])} Pess={sorted(res['P_ess'])}")
    print("  M =", [sorted(m) for m in res['M']])
    # verify saturation: every transversal contains some M
    # check the smallest transversals avoiding M is empty
    print("  stable check:", is_stable(sorted(res['P_ess']), [set(m) for m in res['M']]))

# confirm large omega=2 case fully stabilizes (push cap)
print()
print("=== push: a1=3499271 (113,173,179) omega=3 with higher cap ===")
res = run(3499271, max_rounds=300, max_Pess=45, time_limit=100)
print(f"  |Pess|={len(res['P_ess'])} |M|={len(res['M'])} stable={res['stable']} reason={res.get('reason')}")

print("=== push: a1=4391633 (41,43,47,53) omega=4 higher cap ===")
res = run(4391633, max_rounds=200, max_Pess=40, time_limit=90)
print(f"  |Pess|={len(res['P_ess'])} |M|={len(res['M'])} stable={res['stable']} reason={res.get('reason')}")
