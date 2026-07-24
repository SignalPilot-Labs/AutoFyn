from sim_fast import scan_branch_b
import time

t0=time.time()
found=[]
for a1 in range(4, 2000):
    a, hits = scan_branch_b(a1, 800)
    if hits:
        found.append((a1,hits[:5]))
        print("HIT", a1, hits[:5])
print("time", time.time()-t0, "found", len(found))
