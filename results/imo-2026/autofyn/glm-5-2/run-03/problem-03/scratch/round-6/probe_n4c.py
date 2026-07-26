import sys, time, random
from fractions import Fraction as F

def f2(pieces):
    a,b,c = sorted(pieces, reverse=True); T=a+b+c
    return min(c, abs(2*a-T), a-b, b-c)
def f3(pieces):
    ps=sorted(pieces,reverse=True); n=len(ps); best=None
    for i in range(n):
        for j in range(n):
            if i==j or ps[i]<ps[j]: continue
            rest=[ps[i]-ps[j]]+[ps[k] for k in range(n) if k!=i and k!=j]
            v=f2(rest)
            if best is None or v<best: best=v
    return best
def f4(pieces):
    ps=sorted(pieces,reverse=True); n=len(ps); best=None
    for i in range(n):
        for j in range(n):
            if i==j or ps[i]<ps[j]: continue
            rest=[ps[i]-ps[j]]+[ps[k] for k in range(n) if k!=i and k!=j]
            v=f3(rest)
            if best is None or v<best: best=v
    return best

D4=31; target=F(1,D4); g3=F(8,D4); g0=F(1,D4)
dyadic=[F(16,D4),F(8,D4),F(4,D4),F(2,D4),F(1,D4)]
assert f4(dyadic)==target
print("f4(dyadic)=1/31 confirmed")

t0=time.time()
worst_val=None; worst_cfg=None; n_esc=0; esc_list=[]
N=0

random.seed(7)
# sample 5 positive ints summing to den via "stars and bars" cut positions
def sample_config(den):
    cuts=sorted(random.sample(range(1,den),4))
    parts=[cuts[0]]+[cuts[i+1]-cuts[i] for i in range(3)]+[den-cuts[3]]
    parts.sort(reverse=True)
    return [F(p,den) for p in parts]

nrand=0; tries=0
while nrand<8000 and tries<60000:
    tries+=1
    den=random.choice([31*8, 31*12, 31*16, 31*24])
    ps=sample_config(den)
    p1,p2,p3,p4,p5=ps
    # very-flat interior: p2,p3,p4<8/31, p5>1/31
    if not(p2<g3 and p3<g3 and p4<g3 and p5>g0): continue
    nrand+=1
    v=f4(ps)
    if worst_val is None or v>worst_val:
        worst_val=v; worst_cfg=ps[:]
    if v>target:
        n_esc+=1
        if len(esc_list)<30: esc_list.append((ps[:],v))
    if nrand%1000==0:
        print(f"  rand {nrand} t={time.time()-t0:.1f}s worst={float(worst_val):.5f} esc={n_esc} tries={tries}")
        sys.stdout.flush()

print("=== FINAL ===")
print("rand configs:", nrand, "tries:", tries)
print("worst_val =", worst_val, "=", float(worst_val), " target=", float(target))
print("worst_cfg =", [str(x) for x in worst_cfg], " floats=", [float(x) for x in worst_cfg])
print("is dyadic:", worst_cfg==dyadic)
print("total escapes (f4 > 1/31):", n_esc)
for c,v in esc_list[:15]:
    print("  ESC cfg=", [str(x) for x in c], "v=", str(v), float(v))
print("elapsed", round(time.time()-t0,1),"s")
