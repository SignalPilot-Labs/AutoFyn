import random
def c(n): return 2**n/(2**(n+1)-1)
n=6; target_c=c(n)
base = [0.3306,0.2791,0.1501,0.1162,0.0904,0.0208,0.0128]

def greedy_T(pi, others_sorted_desc):
    T=0
    for x in others_sorted_desc:
        if T+x<=pi: T+=x
    return T

def exact_T(pi, others):
    best=0
    for mask in range(1<<len(others)):
        s=sum(others[b] for b in range(len(others)) if mask&(1<<b))
        if s<=pi and s>best: best=s
    return best

def best_over_i(p, mode):
    k=len(p)
    vals=[]
    for i in range(k):
        pi=p[i]
        others=[p[m] for m in range(k) if m!=i]
        if mode=='greedy':
            T=greedy_T(pi, sorted(others, reverse=True))
        else:
            T=exact_T(pi, others)
        r=pi-T
        vals.append(0.5*(1+r))
    return min(vals), vals

random.seed(2)
results_g=[]; results_e=[]
trials=800
for _ in range(trials):
    noise=[random.uniform(-3e-4,3e-4) for _ in range(7)]
    pert=[base[i]+noise[i] for i in range(7)]
    s=sum(pert); pert=[x/s for x in pert]
    pert.sort(reverse=True)
    if pert[-1]<=0: continue
    if not all(pert[i]-pert[i+1] > 1/(2**(n+1)-1) for i in range(6)): continue
    if pert[0]>=0.5: continue
    bg,_=best_over_i(pert,'greedy')
    be,_=best_over_i(pert,'exact')
    results_g.append(bg); results_e.append(be)

print("greedy: min/mean/max over trials:", min(results_g), sum(results_g)/len(results_g), max(results_g))
print("beats c(n) fraction (greedy):", sum(1 for v in results_g if v<=target_c), "/", len(results_g))
print("exact:  min/mean/max over trials:", min(results_e), sum(results_e)/len(results_e), max(results_e))
print("beats c(n) fraction (exact):", sum(1 for v in results_e if v<=target_c), "/", len(results_e))
print("c(n)=",target_c)
