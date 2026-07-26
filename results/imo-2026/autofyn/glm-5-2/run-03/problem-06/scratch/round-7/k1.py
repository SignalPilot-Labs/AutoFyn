import sys, time
sys.path.insert(0, '/tmp/round-6')
from driver import run_one
# Killer family a1 = p·q^2 (p<q, NON-LOCK, large T)
specs = [
    (75, 3000, 800), (147, 4000, 1000), (245, 5000, 1500), (363, 5000, 1500),
    (507, 6000, 1800), (845, 6000, 1800), (1183, 7000, 2000), (1445, 7000, 2000),
    (1859, 7000, 2000), (2197, 7000, 2000),
]
for a1,N,mr in specs:
    t0=time.time()
    r = run_one(a1, N, mr)
    dt=time.time()-t0
    print(f"a1={r['a1']:6d} M1={r['M1']:5d} N={N:5d} T={str(r['T']):>6s} L={str(r['L']):>7s} govmax={str(r['gov_max']):>4s} {r['status']:>20s} fac={r.get('Lfac','-')} ({dt:.0f}s)", flush=True)
