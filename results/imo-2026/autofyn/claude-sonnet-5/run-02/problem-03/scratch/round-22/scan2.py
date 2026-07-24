import numpy as np
from phimin2 import phi_min

def sample_case_b2(n, m, rng):
    an = 2**n/(2**(n+1)-1)
    Dn = 2**(n+1)-1
    for _ in range(500):
        lo, hi = 1.0/Dn, an/2
        p2 = rng.uniform(lo, hi)
        p1 = rng.uniform(p2, 0.5)
        rem = 1 - p1 - p2
        if rem <= 0: continue
        k = m-2
        if k==0:
            if abs(rem)<1e-9: return [p1,p2]
            continue
        cuts = sorted(rng.uniform(0,1,k-1)) if k>1 else []
        bounds = [0]+cuts+[1]
        parts = [ (bounds[i+1]-bounds[i])*rem for i in range(k)]
        parts.sort(reverse=True)
        if parts[0] > p2 + 1e-9: continue
        p = [p1,p2]+parts
        return p
    return None

if __name__=="__main__":
    rng = np.random.default_rng(2)
    for n in [3,4]:
        m = n+1
        an = 2**n/(2**(n+1)-1)
        results=[]
        ntrials = 6 if n==3 else 4
        for trial in range(ntrials):
            p = sample_case_b2(n, m, rng)
            if p is None: continue
            val, comp = phi_min(p, n, restarts=2)
            margin = an - val
            results.append((margin,p,comp,val))
        results.sort()
        print(f"n={n}:")
        for margin,p,comp,val in results:
            print(f"  margin={margin:.5f} phimin={val:.5f} p={['%.4f'%x for x in p]} comp={comp}")
