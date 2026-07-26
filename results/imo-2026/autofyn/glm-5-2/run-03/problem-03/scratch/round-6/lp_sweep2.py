"""LP-dual scout v2: structural vertex tags + full-structure continuous optimum
vs finite strategy family. Determines whether a unifying dual exists beyond
the finite family."""
import numpy as np, time

def Df(pieces):
    s=sorted(pieces,reverse=True); return sum(((-1)**k)*s[k] for k in range(len(s)))

def finite_strats(p):
    p1,p2,p3,p4=p
    v=[p4, abs(p1-p2-p3)]
    for i in range(4):
        for j in range(i+1,4): v.append(p[i]-p[j])
    for i in range(4):
        for j in range(i+1,4): v.append(abs(2*(p[i]+p[j])-1))
    return min(v)

def grid_min_structure(p, cut_pieces, grid=12):
    """cut_pieces: tuple of piece indices to cut once each. beta_i in (0,p_i/2].
    Returns min D over grid + refine."""
    n=len(cut_pieces)
    P=[p[i] for i in cut_pieces]
    half=[P[k]/2 for k in range(n)]
    def pieces_of(beta):
        out=list(p)  # copy
        # replace each cut piece with its two fragments
        out=[x for k,x in enumerate(p) if k not in cut_pieces]
        for k,b in enumerate(beta):
            out.append(b); out.append(P[k]-b)
        return out
    best=1e9; bestb=None
    grids=[np.linspace(0,half[k],grid) for k in range(n)]
    for comb in itertools.product(*grids):
        d=Df(pieces_of(comb))
        if d<best: best=d; bestb=comb
    # refine
    b=np.array(bestb,dtype=float); step=np.array(half)/grid
    for _ in range(150):
        imp=False
        for k in range(n):
            for sgn in (+1,-1):
                bb=b.copy(); bb[k]+=sgn*step[k]
                if all(0<=bb[k]<=half[k] for k in range(n)):
                    d=Ff(pieces_of(bb))
                    if d<best-1e-12: best=d; b=bb; imp=True; break
            if imp: break
        if not imp: step*=0.5
        if step.max()<1e-10: break
    return best, bestb

import itertools
def Ff(pieces):
    return Df(pieces)

def all_structures_min(p, grid=10):
    """Min over ALL cut structures with <=3 cuts: choose a multiset of pieces to cut
    (each cut once, distinct pieces), up to 3 cuts. Also include 2-cuts-on-1-piece
    is subsumed by 3-distinct for n=3 budget (skip for speed)."""
    best=1e9; best_struct=None; best_beta=None
    idx=list(range(4))
    for k in range(0,4):  # number of cuts
        for cutp in itertools.combinations(idx,k):
            if k==0:
                d=Df(list(p)); bb=()
            else:
                d,bb=grid_min_structure(p,cutp,grid=grid)
            if d<best: best=d; best_struct=cutp; best_beta=bb
    return best, best_struct, best_beta

def structural_vertex(p, beta, cut_pieces):
    """Given the achieving beta, classify the vertex structurally:
    for each cut piece, what is beta_i relative to the OTHER pieces?
    (EH=p_i/2, peel-to-p_j, cross-eq=p_j-beta_k, etc.)"""
    p1,p2,p3,p4=p
    P={i:p[i] for i in range(4)}
    tags=[]
    for k,i in enumerate(cut_pieces):
        b=beta[k] if k<len(beta) else 0
        pi=P[i]
        # compare b to: pi/2 (EH), p_j (peel to j), p_j - b' (cross-eq with another cut), p_j/2
        label=f"cut p{i+1}@{b:.4f}="
        if abs(b-pi/2)<1e-3: label+="EH"
        else:
            matched=False
            for j in range(4):
                if j==i: continue
                if abs(b-P[j])<1e-3: label+=f"peel-to-p{j+1}"; matched=True; break
                if abs(b-P[j]/2)<1e-3: label+=f"half-of-p{j+1}"; matched=True; break
            if not matched:
                # check cross-eq with another cut piece's fragment
                for k2,i2 in enumerate(cut_pieces):
                    if i2==i: continue
                    b2=beta[k2] if k2<len(beta) else 0
                    if abs(b-(P[i2]-b2))<1e-3: label+=f"xpeq-p{i2+1}frag"; matched=True; break
                    if abs(b-b2)<1e-3: label+=f"eqcut-p{i2+1}"; matched=True; break
                if not matched: label+="free"
        tags.append(label)
    return ";".join(tags)

def main():
    t0=time.time()
    rnd=np.random.default_rng(11)
    cfgs=[]
    while len(cfgs)<250:
        x=rnd.dirichlet([4,3,2,1.5]); x=-np.sort(-x)
        if x[1]<4/15 and x[2]<4/15 and x[3]>1/15: cfgs.append(tuple(x))
    print(f"# {len(cfgs)} Case-C configs")
    n_exceed=0; n_cont_beats_finite=0; n_tie=0; n_finite_beats_cont=0
    vert_hist={}
    thresh=1/15+1e-9
    for ci,p in enumerate(cfgs):
        Df_=finite_strats(p)
        Dc,struct,beta=all_structures_min(p,grid=8)
        Dmin=min(Df_,Dc)
        if Dmin>thresh: n_exceed+=1
        if Dc<Df_-1e-6: n_cont_beats_finite+=1
        elif abs(Dc-Df_)<1e-6: n_tie+=1
        else: n_finite_beats_cont+=1
        # tag the continuous-optimum vertex
        if beta is not None and len(beta)>0:
            tag=structural_vertex(p,beta,struct)
            vert_hist[tag]=vert_hist.get(tag,0)+1
    print(f"# exceed: {n_exceed}/{len(cfgs)}")
    print(f"# cont < finite: {n_cont_beats_finite}; tie: {n_tie}; finite < cont: {n_finite_beats_cont}")
    print(f"# structural-vertex histogram (continuous optimum achievers):")
    for tag,c in sorted(vert_hist.items(),key=lambda z:-z[1])[:15]:
        print(f"#   {c:4d}  {tag}")
    print(f"# elapsed {time.time()-t0:.1f}s")

if __name__=="__main__":
    main()
