import numpy as np
from scipy.optimize import linprog
import itertools, random

random.seed(2)

def true_min_phi(vals):
    # vals: list of 4 base pieces (p,q,r,s), not necessarily sorted, sum=1
    # Xiang Yu chooses up to 3 further cut points total (cuts can go anywhere within the 4 base intervals,
    # multiple cuts within one interval allowed). We approximate the true min via considering
    # all "compositions" (c1,c2,c3,c4) with sum<=3 cuts distributed among the 4 pieces,
    # and for each composition, all permutations (orderings) of the resulting up to 7 fragments,
    # solve LP for the worst distribution of cut positions (since Phi is piecewise-linear in cut
    # positions for a FIXED ordering, at a fixed composition & ordering we can put nonneg fragment
    # variables with linear constraint sum=piece value, ordered decreasing weakly, and Phi = sum of ranked ones
    # -- take min over orderings & positions).
    # We just do a fine random+local search here (heuristic) since exact LP-per-permutation for m up to 7
    # elements is expensive combinatorially but let's just do random sampling of cut positions many times
    # combined with a local refine (Nelder-Mead-like) -- heuristic only, for exploration.
    from scipy.optimize import minimize
    p,q,r,s = vals
    base = [p,q,r,s]
    best = None
    # enumerate all ways to distribute up to 3 cuts among 4 pieces: compositions (c1,c2,c3,c4), sum<=3
    comps = [c for c in itertools.product(range(4),repeat=4) if sum(c)<=3]
    for comp in comps:
        # cut piece i into (c_i+1) fragments; parametrize fragment lengths as random splits summing to base[i]
        # use scipy.optimize with random multi-start to find min Phi over free split ratios
        idxs = []
        sizes = []
        for i,c in enumerate(comp):
            k = c+1
            idxs.append(k)
        nvars = sum(idxs) - 4  # each piece with k fragments has k-1 free split fractions in (0,1) simplex; we'll just use k-1 free vars via cumulative
        def unpack(x):
            frags=[]
            pos=0
            for i,k in enumerate(idxs):
                if k==1:
                    frags.append(base[i])
                else:
                    # x gives k-1 numbers in (0,1), sort them to get k intervals of base[i]
                    xs = x[pos:pos+k-1]
                    pos += k-1
                    xs = np.sort(np.clip(xs,1e-6,1-1e-6))
                    prev=0
                    parts=[]
                    for v in xs:
                        parts.append((v-prev)*base[i])
                        prev=v
                    parts.append((1-prev)*base[i])
                    frags += parts
            return frags
        def phi_of(x):
            frags = unpack(x)
            frags_sorted = sorted(frags, reverse=True)
            return sum(frags_sorted[j] for j in range(0,len(frags_sorted),2))
        if nvars==0:
            val = phi_of(np.array([]))
            if best is None or val<best[0]:
                best=(val,comp,[])
            continue
        # multi-start random search + simple local refine
        bestlocal=None
        for trial in range(6):
            x0 = np.random.rand(nvars)
            res = minimize(phi_of, x0, method='Nelder-Mead', options={'xatol':1e-9,'fatol':1e-12,'maxiter':2000})
            if bestlocal is None or res.fun<bestlocal[0]:
                bestlocal=(res.fun,res.x)
        if best is None or bestlocal[0]<best[0]:
            best=(bestlocal[0],comp,bestlocal[1])
    return best

# quick test at the n=3 ladder point to confirm true min ~ 8/15
ladder = [8/15,4/15,2/15,1/15]
res = true_min_phi(ladder)
print("ladder true min:", res[0], "target", 8/15)

# test at the tricky point found earlier where T/D templates only got 9/16
pt = [3/8, 1/4, 1/4, 1/8]
res = true_min_phi(pt)
print("tricky point true min:", res[0], "comp:", res[1], "target 8/15=",8/15)
