import numpy as np, random
from phimin import phi_min
import sys
sys.path.insert(0,'/tmp/round-22')

def sample_case_b2(n, m, rng):
    an = 2**n/(2**(n+1)-1)
    Dn = 2**(n+1)-1
    # T=1. Need p1<1/2, T/Dn < p2 < an/2, p1>=p2>=...>=pm>0, sum=1
    for _ in range(2000):
        lo, hi = 1.0/Dn, an/2
        p2 = rng.uniform(lo, hi)
        p1 = rng.uniform(p2, 0.5)  # p1 in [p2, 0.5)
        rem = 1 - p1 - p2
        if rem <= 0: continue
        k = m-2
        if k==0:
            if abs(rem)<1e-9:
                return [p1,p2]
            continue
        # generate k values <= p2, positive, summing to rem, sorted desc
        # use dirichlet then scale, reject if any > p2
        cuts = sorted(rng.uniform(0,1,k-1)) if k>1 else []
        bounds = [0]+cuts+[1]
        parts = [bounds[i+1]-bounds[i] for i in range(k)]
        parts = [x*rem for x in parts]
        parts.sort(reverse=True)
        if parts[0] > p2 + 1e-9:
            continue
        p = [p1,p2]+parts
        if abs(sum(p)-1)>1e-6: continue
        return p
    return None

if __name__=="__main__":
    rng = np.random.default_rng(1)
    for n in [3,4,5]:
        m = n+1
        an = 2**n/(2**(n+1)-1)
        best_margin = None
        best_p = None
        results=[]
        for trial in range(15):
            p = sample_case_b2(n, m, rng)
            if p is None: continue
            val, comp = phi_min(p, n)
            margin = an*1.0 - val
            results.append((margin,p,comp,val))
            if best_margin is None or margin < best_margin:
                best_margin = margin
                best_p = (p,comp,val)
        results.sort()
        print(f"n={n}: {len(results)} samples, worst 5 margins:")
        for margin,p,comp,val in results[:5]:
            print(f"  margin={margin:.5f} phimin={val:.5f} p={['%.4f'%x for x in p]} comp={comp}")
