import sys, time
sys.path.insert(0, '/tmp/round-6')
from driver import run_one
for a1,N,mr in [(187, 20000, 4000), (209, 20000, 4000), (247, 20000, 4000)]:
    t0=time.time()
    r = run_one(a1, N, mr)
    dt=time.time()-t0
    print(f"a1={r['a1']:6d} M1={r['M1']:5d} N={N:5d} T={str(r['T']):>6s} L={str(r['L']):>7s} govmax={str(r['gov_max']):>4s} {r['status']:>20s} fac={r.get('Lfac','-')} ({dt:.0f}s)", flush=True)
