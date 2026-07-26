"""
LP-dual scout for n=3 Case-C (imo-2026-03).
For each sampled Case-C Liu config p=(p1>=p2>=p3>=p4, sum=1, p2,p3<4/15, p4>1/15):
  - compute D_finite = min over the certified finite strategy family
        {EH-n-largest (D=p4), two-cut corollary (D=|p1-p2-p3|),
         pairwise-diff (D=p_i-p_j for all pairs), peel-complement |2(pi+pj)-1|}.
  - compute D_cont = continuous min of D(beta) over the 3-independent-cuts
        structure (one cut on each of pieces 1,2,3) via dense grid + local refine.
  - also enumerate candidate DEGENERATE vertices (cross-piece equalities) and eval D.
  - record which vertex achieves D_cont, and whether D_cont < D_finite.
Target: confirm min <= 1/15 on all, inspect dual/vertex structure.
"""
import numpy as np
from fractions import Fraction as F
import random, itertools, time

def D_of_multiset(pieces):
    """Alternating sum of descending sort (exact rational)."""
    s = sorted((F(x).limit_denominator(10**9) for x in pieces), reverse=True)
    return sum(((-1)**k)*s[k] for k in range(len(s)))

def D_of_float(pieces):
    s = sorted(pieces, reverse=True)
    return sum(((-1)**k)*s[k] for k in range(len(s)))

def case_c_configs(n=400, seed=1):
    rnd = np.random.default_rng(seed)
    cfgs=[]
    while len(cfgs)<n:
        x = rnd.dirichlet([4,3,2,1.5])  # bias toward p1>=p2>=p3>=p4
        x = -np.sort(-x)  # descending
        p1,p2,p3,p4 = x
        if p2<4/15 and p3<4/15 and p4>1/15:
            cfgs.append((p1,p2,p3,p4))
    return cfgs

def finite_strategies(p):
    p1,p2,p3,p4 = p
    vals=[]
    vals.append(p4)                              # EH-n-largest
    vals.append(abs(p1-p2-p3))                   # two-cut corollary
    # pairwise diffs
    for i in range(4):
        for j in range(i+1,4):
            vals.append(p[i]-p[j])
    # peel-complement |2(pi+pj)-1| for n=3 (3-mark peel)
    for i in range(4):
        for j in range(i+1,4):
            vals.append(abs(2*(p[i]+p[j])-1))
    return min(vals)

def cont_min_3cuts(p, grid=18, refine=True):
    """Continuous min of D over 3-independent-cuts structure (cut pieces 1,2,3 once each).
    beta_i in (0, p_i/2]. Final pieces: b1,p1-b1,b2,p2-b2,b3,p3-b3,p4."""
    p1,p2,p3,p4 = p
    best=1e9; best_beta=None
    # grid
    b1s = np.linspace(0, p1/2, grid)
    b2s = np.linspace(0, p2/2, grid)
    b3s = np.linspace(0, p3/2, grid)
    for b1 in b1s:
        for b2 in b2s:
            for b3 in b3s:
                pieces=[b1,p1-b1,b2,p2-b2,b3,p3-b3,p4]
                d=D_of_float(pieces)
                if d<best: best=d; best_beta=(b1,b2,b3)
    # local refine (coordinate pattern search)
    if refine and best_beta is not None:
        b=np.array(best_beta,dtype=float)
        step=np.array([p1/2,p2/2,p3/2])/grid
        for _ in range(200):
            improved=False
            for k in range(3):
                for sgn in (+1,-1):
                    bb=b.copy(); bb[k]+=sgn*step[k]
                    if 0<=bb[0]<=p1/2 and 0<=bb[1]<=p2/2 and 0<=bb[2]<=p3/2:
                        pieces=[bb[0],p1-bb[0],bb[1],p2-bb[1],bb[2],p3-bb[2],p4]
                        d=D_of_float(pieces)
                        if d<best-1e-12: best=d; b=bb; improved=True; break
                if improved: break
            if not improved: step*=0.5
            if step.max()<1e-10: break
    return best, best_beta

def vertex_candidates(p):
    """Enumerate degenerate cut configurations (cross-piece equalities) for
    3-independent-cuts structure and a few 2-cut structures; return list of
    (D_value, description, beta) candidates. These are the sort-region vertices."""
    p1,p2,p3,p4 = p
    cands=[]
    # 3-independent-cuts: beta1,beta2,beta3 in (0,pi/2]. Vertices where pairs coincide:
    # equalities among {b1,p1-b1,b2,p2-b2,b3,p3-b3,p4}. We enumerate a finite set of
    # candidate equations fixing beta values: beta_i = beta_j, beta_i = p_j - beta_j,
    # beta_i = p_j (cut at a piece boundary), beta_i = p_j - beta_k, beta_i = p_j/2 (EH).
    def eval3(b1,b2,b3):
        if b1<0 or b1>p1/2 or b2<0 or b2>p2/2 or b3<0 or b3>p3/2: return None
        pieces=[b1,p1-b1,b2,p2-b2,b3,p3-b3,p4]
        return D_of_float(pieces)
    # EH on all three (b_i = p_i/2)
    v=eval3(p1/2,p2/2,p3/2)
    if v is not None: cands.append((v,"EH all 3",(p1/2,p2/2,p3/2)))
    # peel-style: b1 = p2 (split p1 into p2 + p1-p2), b2,b3 = EH or 0
    for b1 in [p2,p3,p4,p1-p2,p1-p3,p1-p4, p1/2]:
        for b2 in [0,p2/2,p2,p3,p4,p2-p3]:
            for b3 in [0,p3/2,p3,p4,p2-p3]:
                v=eval3(b1,b2,b3)
                if v is not None: cands.append((v,f"b1={b1:.4f},b2={b2:.4f},b3={b3:.4f}",(b1,b2,b3)))
    # cross-piece equalities b1=b2, b1=p2-b2, b1=p3-b3, b1=p4, etc.
    for b1 in [p2,p3,p4,p2/2,p3/2,p4/2,p1/2,p1-p2,p1-p3,p1-p4]:
        for b2 in [b1, p2-b1 if 0<=p2-b1<=p2/2 else -1, p2/2, 0, p2-b1] :
            if b2<0 or b2>p2/2: continue
            for b3 in [b1, b2, p3-b1 if 0<=p3-b1<=p3/2 else -1, p3-b2 if 0<=p3-b2<=p3/2 else -1, p3/2, 0, p4, p3-b1, p3-b2]:
                if b3<0 or b3>p3/2: continue
                v=eval3(b1,b2,b3)
                if v is not None: cands.append((v,f"b1={b1:.4f},b2={b2:.4f},b3={b3:.4f}",(b1,b2,b3)))
    return cands

def main():
    t0=time.time()
    cfgs = case_c_configs(n=300, seed=7)
    print(f"# sampled {len(cfgs)} Case-C configs")
    n_exceed=0; n_cont_beats=0; n_tie=0
    vert_hist={}
    worst=[]
    for ci,p in enumerate(cfgs):
        Df = finite_strategies(p)
        Dc, beta = cont_min_3cuts(p, grid=14, refine=True)
        vcs = vertex_candidates(p)
        Dv = min(v[0] for v in vcs) if vcs else 1e9
        Dmin = min(Df, Dc, Dv)
        thresh = 1/15 + 1e-9
        if Dmin > thresh:
            n_exceed+=1
            worst.append((p, Df, Dc, Dv, Dmin))
        # does continuous beat finite?
        if Dc < Df - 1e-6:
            n_cont_beats+=1
        elif abs(Dc-Df)<1e-6: n_tie+=1
        # which vertex achieves Dv?
        if vcs:
            best_v = min(vcs, key=lambda z:z[0])
            tag=best_v[1].split(",")[0][:25]
            vert_hist[tag]=vert_hist.get(tag,0)+1
    print(f"# exceed 1/15: {n_exceed}/{len(cfgs)}")
    print(f"# continuous < finite (strictly): {n_cont_beats}; tie: {n_tie}; finite<cont: {len(cfgs)-n_cont_beats-n_tie}")
    print(f"# vertex-histogram (top tags achieving Dv):")
    for tag,c in sorted(vert_hist.items(), key=lambda z:-z[1])[:12]:
        print(f"#   {c:4d}  {tag}")
    print(f"# worst exceeders (p, Df, Dc, Dv, Dmin):")
    for w in worst[:8]:
        print(f"#   p={[round(x,4) for x in w[0]]} Df={w[1]:.5f} Dc={w[2]:.5f} Dv={w[3]:.5f} Dmin={w[4]:.5f}")
    print(f"# elapsed {time.time()-t0:.1f}s")

if __name__=="__main__":
    main()
