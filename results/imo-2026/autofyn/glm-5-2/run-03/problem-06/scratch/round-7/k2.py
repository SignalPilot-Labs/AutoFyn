import sys, time
sys.path.insert(0, '/tmp/round-6')
from driver import run_one
# Small-rad-large-value: a1 = p·q^e (e>=3), tiny M1=pq vs huge a1
specs = [
    (375, 4000, 1000),    # 3·5^3, M1=15
    (1875, 4000, 1000),   # 3·5^4, M1=15
    (9375, 3000, 800),    # 3·5^5, M1=15  TIGHT
    (46875, 2000, 500),   # 3·5^6, M1=15  VERY TIGHT
    (1029, 4000, 1000),   # 3·7^3, M1=21
    (7203, 3000, 800),    # 3·7^4, M1=21
    (1715, 4000, 1000),   # 5·7^3, M1=35
    (12005, 3000, 800),   # 5·7^4, M1=35
    (3993, 3000, 800),    # 3·11^3, M1=33
    (43923, 2000, 500),    # 3·11^4, M1=33 TIGHT
    (10985, 3000, 800),   # 5·13^3, M1=65
    (9317, 3000, 800),    # 7·11^3, M1=77
]
for a1,N,mr in specs:
    t0=time.time()
    r = run_one(a1, N, mr)
    dt=time.time()-t0
    print(f"a1={r['a1']:6d} M1={r['M1']:5d} N={N:5d} T={str(r['T']):>6s} L={str(r['L']):>7s} govmax={str(r['gov_max']):>4s} {r['status']:>20s} fac={r.get('Lfac','-')} ({dt:.0f}s)", flush=True)
