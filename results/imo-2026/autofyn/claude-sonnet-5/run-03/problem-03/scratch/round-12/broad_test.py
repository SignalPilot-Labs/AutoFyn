import random
def c(n): return 2**n/(2**(n+1)-1)

def greedy_T(pi, others_sorted_desc):
    T=0
    for x in others_sorted_desc:
        if T+x<=pi: T+=x
    return T

def min_over_i_greedy(p):
    k=len(p)
    vals=[]
    for i in range(k):
        pi=p[i]
        others=sorted([p[m] for m in range(k) if m!=i], reverse=True)
        T=greedy_T(pi, others)
        r=pi-T
        vals.append(0.5*(1+r))
    return min(vals)

def sample_balanced(n, rng):
    k=n+1
    gamma=1/(2**(n+1)-1)
    # sample random simplex point via exponential/Dirichlet, then sort desc, check region membership; retry
    for _ in range(2000):
        x=[rng.expovariate(1.0) for _ in range(k)]
        s=sum(x)
        p=sorted([xi/s for xi in x], reverse=True)
        if p[0]>=0.5: continue
        if all(p[i]-p[i+1] > gamma for i in range(k-1)):
            return p
    return None

random.seed(42)
worst_ratio = 0
worst_info = None
fails = 0
total = 0
for n in range(2,10):
    cn = c(n)
    trials = 3000
    local_fail=0
    local_min_margin = None
    for _ in range(trials):
        p = sample_balanced(n, random)
        if p is None: continue
        total += 1
        v = min_over_i_greedy(p)
        margin = cn - v  # positive means beats c(n)
        if local_min_margin is None or margin < local_min_margin:
            local_min_margin = margin
        if v > cn:
            local_fail += 1
            fails += 1
    print(f"n={n}: c(n)={cn:.6f}  worst-case margin (c(n)-v) = {local_min_margin:.6f}  fails={local_fail}")
print("total trials:", total, "total fails:", fails)
