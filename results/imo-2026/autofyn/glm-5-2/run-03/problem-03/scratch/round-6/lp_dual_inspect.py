"""Per-region LP dual inspection (n=3, 3-independent-cuts structure).
Enumerate sort-regions of the 7 final pieces via permutations; for each feasible
region solve the LP (min signed-sum of pieces subject to ordering + box); take
global min; print the binding region's dual weights. Look for a uniform pattern."""
import numpy as np, itertools, time
from scipy.optimize import linprog

def D_desc(pieces):
    s=sorted(pieces,reverse=True); return sum(((-1)**k)*s[k] for k in range(len(s)))

def solve_regions(p, cut=(0,1,2)):
    p1,p2,p3,p4=p
    P=[p1,p2,p3,p4]
    cut=list(cut); uncut=[i for i in range(4) if i not in cut]
    # final pieces as functions of beta (len=cut): for cut piece i, frag = beta_i (small) & P[i]-beta_i (large)
    # We index final pieces: for each cut piece -> (large=P[i]-b_i, small=b_i); uncut -> P[i].
    # beta in [0, P[i]/2] so large>=small.
    n=len(cut)
    # piece descriptor: list of (kind, piece_idx) where kind in {'L'(large),'S'(small),'U'(uncut)}
    descs=[]
    for i in cut: descs.append(('L',i)); descs.append(('S',i))
    for i in uncut: descs.append(('U',i))
    m=len(descs)  # 7 for n=3, 3 cuts
    # value of piece r as linear function of beta: coeff vector (length n) + const
    def val(r,beta):
        kind,i=descs[r]
        if kind=='U': return P[i]
        if kind=='L': return P[i]-beta[cut.index(i)]
        if kind=='S': return beta[cut.index(i)]
    # objective: min signed sum; sign depends on sort order (rank). rank 0 (largest) -> +, rank1 -> -, ...
    # We enumerate permutations of {0..m-1} giving the sort order (perm[k] = piece at rank k, largest first).
    best=1e9; best_perm=None; best_beta=None; best_dual=None
    seen=set()
    for perm in itertools.permutations(range(m)):
        # feasibility: val(perm[0],b) >= val(perm[1],b) >= ... >= val(perm[m-1],b), 0<=b_i<=P[i]/2
        # build as A_ub b_ub <= 0:  val(perm[k]) - val(perm[k+1]) >= 0  =>  -(val_k - val_{k+1}) <= 0
        A=[]; b=[]
        for k in range(m-1):
            r1=perm[k]; r2=perm[k+1]
            # val(r1)-val(r2) >= 0  =>  -(coeff_r1 - coeff_r2) . beta <= -(const_r1-const_r2)
            c1=np.zeros(n); c2=np.zeros(n)
            const1=0; const2=0
            kind1,i1=descs[r1]; kind2,i2=descs[r2]
            def fill(kind,i,c,const):
                if kind=='U': const+=P[i]
                elif kind=='L': c[cut.index(i)] += -1; const+=P[i]
                elif kind=='S': c[cut.index(i)] += +1
                return c,const
            c1,const1=fill(kind1,i1,c1,const1)
            c2,const2=fill(kind2,i2,c2,const2)
            row=-(c1-c2); rhs=(const1-const2)
            A.append(row); b.append(rhs)
        # box: 0<=b<=half
        A_ub=np.array(A) if A else np.zeros((0,n))
        b_ub=np.array(b) if b else np.zeros(0)
        bounds=[(0,P[i]/2) for i in cut]
        # objective: signed sum = sum_k (-1)^k val(perm[k]) -> minimize
        # = sum_k (-1)^k (c_{perm[k]} . b + const_{perm[k]})
        cobj=np.zeros(n); objconst=0
        for k in range(m):
            r=perm[k]; kind,i=descs[r]
            cc=np.zeros(n); cnst=0
            if kind=='U': cnst=P[i]
            elif kind=='L': cc[cut.index(i)]=-1; cnst=P[i]
            elif kind=='S': cc[cut.index(i)]=+1
            sign=(-1)**k
            cobj+=sign*cc; objconst+=sign*cnst
        # skip if obj is degenerate (no beta term) -> just a point? still solve
        res=linprog(cobj, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')
        if not res.success: continue
        val=res.fun+objconst
        if val<best-1e-12:
            best=val; best_perm=perm; best_beta=res.x
            # dual of A_ub (the ordering constraints) and bounds
            # linprog highs: res.ineqlin.marginals for A_ub, res.ineqlin.upper for bounds? Use res.eqlin/ineqlin
            try:
                dual_ineq=res.ineqlin.marginals  # length = #rows in A_ub
            except: dual_ineq=None
            best_dual=dual_ineq
    return best, best_perm, best_beta, best_dual, descs

def report(p):
    p1,p2,p3,p4=p
    print(f"p=({p1:.4f},{p2:.4f},{p3:.4f},{p4:.4f}) 1/15={1/15:.5f}")
    best,perm,beta,dual,descs=solve_regions(p)
    print(f"  min D = {best:.5f}  perm={perm}")
    print(f"  beta = {[round(x,4) for x in beta] if beta is not None else None}")
    if beta is not None:
        # describe each piece's value
        P=[p1,p2,p3,p4]
        vals=[]
        for k,r in enumerate(perm):
            kind,i=descs[r]
            if kind=='U': v=P[i]; nm=f"p{i+1}={v:.4f}"
            elif kind=='L': v=P[i]-beta[[0,1,2].index(i) if i in [0,1,2] else 0]; nm=f"p{i+1}-b={v:.4f}"
            else: v=beta[i]; nm=f"b{i+1}={v:.4f}"
            vals.append((k,nm,v))
        print(f"  sort: " + " >= ".join(nm for _,nm,_ in vals))
    if dual is not None:
        # count nonzero dual weights
        nz=[(perm[k],perm[k+1],round(d,3)) for k,d in enumerate(dual) if abs(d)>1e-6]
        print(f"  nonzero dual weights (rank-edge (k,k+1)->weight): {nz}")

def main():
    t0=time.time()
    # a few representative Case-C configs
    tests=[
        (0.50,0.20,0.20,0.10),  # |p1-p2-p3|=0.1>1/15
        (0.42,0.24,0.20,0.14),
        (0.36,0.26,0.22,0.16),
        (0.40,0.22,0.20,0.18),
        (0.45,0.22,0.18,0.15),
    ]
    for p in tests:
        # normalize & sort desc
        s=sorted(p,reverse=True); s=[x/sum(s) for x in s]
        if s[1]<4/15 and s[2]<4/15 and s[3]>1/15:
            report(s)
    print(f"# elapsed {time.time()-t0:.1f}s")

if __name__=="__main__":
    main()
