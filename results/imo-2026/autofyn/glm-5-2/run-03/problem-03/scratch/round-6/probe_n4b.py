import sys, time, random
from fractions import Fraction as F

def f2(pieces):
    a, b, c = sorted(pieces, reverse=True)
    T = a + b + c
    return min(c, abs(2*a - T), a - b, b - c)

def f3(pieces):
    ps = sorted(pieces, reverse=True); n=len(ps); best=None
    for i in range(n):
        for j in range(n):
            if i==j or ps[i]<ps[j]: continue
            rest=[ps[i]-ps[j]]+[ps[k] for k in range(n) if k!=i and k!=j]
            v=f2(rest)
            if best is None or v<best: best=v
    return best

def f4(pieces):
    ps = sorted(pieces, reverse=True); n=len(ps); best=None
    for i in range(n):
        for j in range(n):
            if i==j or ps[i]<ps[j]: continue
            rest=[ps[i]-ps[j]]+[ps[k] for k in range(n) if k!=i and k!=j]
            v=f3(rest)
            if best is None or v<best: best=v
    return best

D4=31; target=F(1,D4); g3=F(8,D4); g0=F(1,D4)
dyadic=[F(16,D4),F(8,D4),F(4,D4),F(2,D4),F(1,D4)]
print("f4(dyadic) =", f4(dyadic), "=", float(f4(dyadic)), "target", float(target))
assert f4(dyadic)==target

t0=time.time()
worst_val=None; worst_cfg=None; n_esc=0; esc_list=[]
n=0

# Fine grid with den = 31*8 = 248, but PRUNE heavily.
den = 248
def near_dyadic_corner():
    # sample points approaching dyadic from interior: p2->8/31-, p5->1/31+
    res=[]
    for eps2_den in range(1,9):
        for eps5_den in range(1,9):
            # p2 = 8/31 - eps2, p5 = 1/31 + eps5, keep dyadic ratios for p3,p4
            eps2 = F(eps2_den, 248)
            eps5 = F(eps5_den, 248)
            p2 = F(8,31) - eps2
            p5 = F(1,31) + eps5
            # p3 = 4/31, p4 = 2/31 (dyadic middle), p1 = 1 - rest
            p3 = F(4,31); p4 = F(2,31)
            p1 = F(1) - p2 - p3 - p4 - p5
            if p1 < p2 or p2 < p3 or p3 < p4 or p4 < p5: continue
            if not (p2 < g3 and p5 > g0): continue
            res.append([p1,p2,p3,p4,p5])
    return res

for cfg in near_dyadic_corner():
    v = f4(cfg); n+=1
    if worst_val is None or v>worst_val:
        worst_val=v; worst_cfg=cfg[:]
    if v > target:
        n_esc+=1
        if len(esc_list)<20: esc_list.append((cfg[:],v))
print(f"corner grid {n} t={time.time()-t0:.1f}s worst={float(worst_val):.5f} esc={n_esc}")
for c,v in esc_list[:5]:
    print("  ESC", [str(x) for x in c], "v=",str(v),float(v))
sys.stdout.flush()

# Random interior sweep
random.seed(2024)
nrand=0
for _ in range(6000):
    for _try in range(60):
        nums=sorted([random.randint(1,den-1) for _ in range(5)],reverse=True)
        if sum(nums)!=den: continue
        ps=[F(x,den) for x in nums]
        p1,p2,p3,p4,p5=ps
        if not(p2<g3 and p3<g3 and p4<g3 and p5>g0): continue
        break
    else:
        continue
    v=f4(ps); nrand+=1
    if worst_val is None or v>worst_val:
        worst_val=v; worst_cfg=ps[:]
    if v>target:
        n_esc+=1
        if len(esc_list)<20: esc_list.append((ps[:],v))
    if nrand%1000==0:
        print(f"  rand {nrand} t={time.time()-t0:.1f}s worst={float(worst_val):.5f} esc={n_esc}")
        sys.stdout.flush()

print("=== FINAL ===")
print("total configs:", n+nrand)
print("worst_val =", worst_val, "=", float(worst_val), " target 1/31 =", float(target))
print("worst_cfg =", [str(x) for x in worst_cfg])
print("worst_cfg floats =", [float(x) for x in worst_cfg])
print("is dyadic:", worst_cfg==dyadic)
print("total escapes (f4 > 1/31):", n_esc)
for c,v in esc_list[:10]:
    print("  ESC cfg=", [str(x) for x in c], "v=", str(v), float(v))
print("elapsed", round(time.time()-t0,1),"s")
