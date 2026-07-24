from sim_fast import build_seq_fast
import time
t0=time.time()
maxratio = 0
worst = None
for a1 in range(4, 3000):
    a = build_seq_fast(a1, 200)
    for n in range(2, 201):
        r = a[n]/a[n-1]
        if r > maxratio:
            maxratio = r
            worst = (a1, n, a[n-1], a[n])
print("maxratio", maxratio, worst, "time", time.time()-t0)
