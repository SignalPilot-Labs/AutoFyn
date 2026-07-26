"""Confirm: for configs where 1-cut-per-piece LP caps above 1/15, the true
continuous optimum (allowing multi-cut-on-one-piece) reaches <= 1/15 via the
Theorem-6 peel+EH-fragment strategies. Also probe n=4 feasibility."""
import numpy as np, itertools, time

def Df(pieces):
    s=sorted(pieces,reverse=True); return sum(((-1)**k)*s[k] for k in range(len(s)))

def onecut_per_piece_min(p, grid=14):
    """1 cut on each of 3 distinct pieces (n=3)."""
    p1,p2,p3,p4=p
    best=1e9; bb=None
    for cutp in itertools.combinations(range(4),3):
        P=[p[i] for i in cutp]; half=[P[k]/2 for k in range(3)]
        def pieces_of(beta):
            out=[p[i] for i in range(4) if i not in cutp]
            for k,b in enumerate(beta): out.append(b); out.append(P[k]-b)
            return out
        g=[np.linspace(0,half[k],grid) for k in range(3)]
        for c in itertools.product(*g):
            d=Df(pieces_of(c))
            if d<best: best=d; bb=(cutp,c)
        # refine
        b=np.array(bb[1],dtype=float); step=np.array(half)/grid
        for _ in range(120):
            imp=False
            for k in range(3):
                for sgn in (+1,-1):
                    bb2=b.copy(); bb2[k]+=sgn*step[k]
                    if all(0<=bb2[k]<=half[k] for k in range(3)):
                        d=Ff(pieces_of(bb2))
                        if d<best-1e-12: best=d; b=bb2; imp=True; break
                if imp: break
            if not imp: step*=0.5
            if step.max()<1e-10: break
    return best

def Ff(pieces): return Df(pieces)

def multicut_min(p, grid=12):
    """Allow up to 3 cuts distributed arbitrarily among 4 pieces (multi-cut on one piece OK).
    A 'structure' = tuple of (piece_idx, cut_position) with positions sorted within piece.
    Enumerate: for each partition of 3 cuts into 4 pieces (stars), grid positions."""
    p1,p2,p3,p4=p; P=list(p)
    best=1e9; best_desc=None
    # enumerate distributions: (k0,k1,k2,k3) with sum<=3
    for k0 in range(4):
     for k1 in range(4-k0):
      for k2 in range(4-k0-k1):
       k3=3-k0-k1-k2
       if k0+k1+k2+k3>3: continue
       ks=(k0,k1,k2,k3)
       if sum(ks)==0:
           d=Df(list(p))
           if d<best: best=d; best_desc=("nocut",)
           continue
       # grid positions for each piece's cuts: k_i cuts in (0, P[i]) sorted
       # for efficiency, grid each cut independently in (0, P[i]/2) (WLOG first half? NO -- multi-cut not symmetric)
       # actually for multi-cut, fragments must be sorted; cut positions c1<=c2<=...<=ck in (0,P[i])
       # grid in (0, P[i]) at resolution grid
       grids=[]
       for i in range(4):
           if ks[i]>0: grids.append([np.linspace(0,P[i],grid) for _ in range(ks[i])])
       # build per-piece cut lists
       def gen():
           idx=0; per=[]
           for i in range(4):
               if ks[i]==0: per.append([])
               else:
                   per.append(grids[idx]); idx+=1
           return per
       per=gen()
       for cuts in itertools.product(*[list(itertools.product(*per[i])) if per[i] else [()] for i in range(4)]):
           # sort each piece's cuts
           out=list(p)
           desc=[]
           for i in range(4):
               cs=sorted(cuts[i])
               frags=[]; prev=0
               for c in cs: frags.append(c-prev); prev=c
               frags.append(P[i]-prev)
               desc.append(frags)
           allp=[]
           for i in range(4): allp+=desc[i]
           d=Ff(allp)
           if d<best: best=d; best_desc=(ks,cuts)
    return best, best_desc

def main():
    t0=time.time()
    tests=[
        (0.50,0.20,0.20,0.10),
        (0.42,0.24,0.20,0.14),
        (0.36,0.26,0.22,0.16),
        (0.45,0.22,0.18,0.15),
    ]
    print("n=3 Case-C: 1-cut-per-piece LP min vs multi-cut true optimum")
    for p in tests:
        s=sorted(p,reverse=True); s=[x/sum(s) for x in s]
        d1=onecut_per_piece_min(s,grid=12)
        dm,desc=multicut_min(s,grid=10)
        print(f"  p={[round(x,3) for x in s]}: 1cut-per-piece={d1:.5f}  multicut={dm:.5f}  1/15={1/15:.5f}  struct={desc[0] if desc else None}")
    print(f"# n=3 elapsed {time.time()-t0:.1f}s")
    # n=4 probe: a few flat configs, multicut (1 cut per piece, 4 cuts on 4 of 5 pieces)
    print("\nn=4 flat probe (1-cut-per-piece, 4 cuts on 4 distinct pieces):")
    t1=time.time()
    rnd=np.random.default_rng(3)
    n4_cfgs=[]
    while len(n4_cfgs)<40:
        x=rnd.dirichlet([5,4,3,2,1.5]); x=-np.sort(-x)
        if x[4]>1/31 and x[1]<8/31: n4_cfgs.append(tuple(x))  # very-flat-ish
    def n4_onecut(p,grid=7):
        P=list(p); best=1e9
        for cutp in itertools.combinations(range(5),4):
            Pc=[P[i] for i in cutp]; half=[Pc[k]/2 for k in range(4)]
            def pieces_of(beta):
                out=[P[i] for i in range(5) if i not in cutp]
                for k,b in enumerate(beta): out.append(b); out.append(Pc[k]-b)
                return out
            g=[np.linspace(0,half[k],grid) for k in range(4)]
            for c in itertools.product(*g):
                d=Ff(pieces_of(c))
                if d<best: best=d
        return best
    nexceed=0
    for p in n4_cfgs:
        d=n4_onecut(p,grid=7)
        if d>1/31+1e-9: nexceed+=1
    print(f"  n=4: {nexceed}/{len(n4_cfgs)} exceed 1/31 (1-cut-per-piece only; Theorem-6 strategies NOT included)")
    print(f"# n=4 elapsed {time.time()-t1:.1f}s")

if __name__=="__main__":
    main()
