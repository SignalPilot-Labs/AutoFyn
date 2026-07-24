import random

def E_val(multiset):
    s = sorted(multiset, reverse=True)
    return sum(v for i,v in enumerate(s) if i%2==1)

def A_val(multiset):
    s = sorted(multiset, reverse=True)
    tot=0
    for i,v in enumerate(s):
        tot += v if i%2==0 else -v
    return tot

random.seed(2)

worst_margin = 1e9
worst_config = None

for trial in range(3000):
    m = random.randint(1,6)
    tau1 = random.uniform(1,30)
    tau = [tau1/(2**i) for i in range(m)]
    R = sum(tau)
    s = random.uniform(1e-6, 2*tau1)
    k = random.randint(1, m+1)
    # random init partition
    def rand_partition():
        cuts = sorted([random.random() for _ in range(k-1)])
        pts=[0]+cuts+[1]
        parts=[(pts[i+1]-pts[i])*s for i in range(k)]
        # clip to tau1 and renormalize crudely by redistributing excess -- just reject if invalid after small iters
        return parts

    best = None
    for restart in range(6):
        parts = None
        for _ in range(500):
            p = rand_partition()
            if all(x<=tau1+1e-9 for x in p):
                parts = p
                break
        if parts is None:
            continue
        cur = parts[:]
        curE = E_val(cur+tau)
        # coordinate ascent: repeatedly perturb two coords i,j (transfer mass) to increase E, keep sum fixed and bounds
        for it in range(3000):
            i,j = random.sample(range(k),2) if k>=2 else (0,0)
            if k<2: 
                break
            step = random.uniform(-1,1)*random.choice([0.5,0.1,0.02,0.005,0.001])*tau1
            newp = cur[:]
            newp[i]+=step
            newp[j]-=step
            if newp[i]<0 or newp[i]>tau1 or newp[j]<0 or newp[j]>tau1:
                continue
            newE = E_val(newp+tau)
            if newE > curE:
                cur, curE = newp, newE
        if best is None or curE>best:
            best=curE
    if best is None:
        continue
    margin = R - best  # should be >=0
    if margin < worst_margin:
        worst_margin = margin
        worst_config = (m, tau1, s, k, cur, best, R)

print("worst margin (R - maxE found) =", worst_margin)
print(worst_config)
