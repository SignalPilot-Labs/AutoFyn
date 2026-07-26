import sys, time
sys.path.insert(0, '/tmp/round-6')
from fast_greedy_correct import greedy_fast, rad
for a1, N in [(847, 4000), (175, 3000), (385, 15000)]:
    t0=time.time()
    a=greedy_fast(a1, N)
    dt=time.time()-t0
    print(f"a1={a1} N={N} time={dt:.1f}s M1={rad(a1)} last={a[-1]}", flush=True)
