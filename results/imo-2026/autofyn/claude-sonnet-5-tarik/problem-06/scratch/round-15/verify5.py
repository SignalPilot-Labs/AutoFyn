import time
from math import gcd
from sympy import factorint

def generate(a1, N):
    seq = [a1]
    while len(seq) < N:
        cand = seq[-1] + 1
        while True:
            if all(gcd(cand, x) > 1 for x in seq):
                seq.append(cand)
                break
            cand += 1
    return seq

a1 = 21528751
t0=time.time()
seq = generate(a1, 1200)
maxterm = seq[-1]
termset = set(seq)
print("gen done", time.time()-t0, "maxterm", maxterm, "range", maxterm-a1)

t0=time.time()
sig_to_status = {}
violations = []
n_checked = 0
for n in range(a1, maxterm+1):
    facs = factorint(n)
    sig = frozenset(p for p in facs if p <= a1)
    status = n in termset
    n_checked += 1
    if sig in sig_to_status:
        if sig_to_status[sig][1] != status:
            violations.append((sig_to_status[sig][0], sig_to_status[sig][1], n, status, sig))
    else:
        sig_to_status[sig] = (n, status)
    if n_checked % 20000 == 0:
        print(n_checked, "done,", time.time()-t0, "s elapsed")

print(f"checked {n_checked} integers, distinct signatures {len(sig_to_status)}, violations {len(violations)}")
if violations:
    print("SAMPLE VIOLATIONS:", violations[:5])
print("total time", time.time()-t0)
