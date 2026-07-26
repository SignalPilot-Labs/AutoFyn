"""Clean grid-only 1-cut-per-piece sweep over ALL 4 triples (incl. degenerate beta=0).
No buggy refine. Settles whether the lp-dual-region framing (1-cut-per-piece) suffices
to reach <= 1/15 on n=3 Case-C, and inspects the achieving vertex structure."""
import numpy as np, itertools, time

def Df(pieces):
    s=sorted(pieces,reverse=True); return sum(((-1)**k)*s[k] for k in range(len(s)))

def onecut_grid_min(p, grid=24):
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
    return best, bb

def classify_vertex(p, bb):
    cutp, c = bb
    P=list(p)
    tags=[]
    for k,i in enumerate(cutp):
        b=c[k]; pi=P[i]
        if abs(b)<1e-6: tag="cut=0(none)"
        elif abs(b-pi/2)<1e-4: tag=f"EH p{i+1}"
        else:
            mtch=None
            for j in range(4):
                if j==i: continue
                if abs(b-P[j])<1e-4: mtch=f"peel p{i+1}->p{j+1}"; break
                if abs(b-P[j]/2)<1e-4: mtch=f"half-of p{j+1}"; break
            if mtch: tag=mtch
            else: tag=f"free b{i+1}={b:.4f}"
        tags.append(tag)
    return ";".join(tags)

def main():
    t0=time.time()
    rnd=np.random.default_rng(99)
    cfgs=[]
    while len(cfgs)<400:
        x=rnd.dirichlet([4,3,2,1.5]); x=-np.sort(-x)
        if x[1]<4/15 and x[2]<4/15 and x[3]>1/15: cfgs.append(tuple(x))
    print(f"# {len(cfgs)} Case-C configs, grid=24, 1-cut-per-piece over all 4 triples")
    nexceed=0; worst=[]; vhist={}
    for p in cfgs:
        d,bb=onecut_grid_min(p,grid=24)
        if d>1/15+1e-6:
            nexceed+=1; worst.append((p,d,bb))
        else:
            tag=classify_vertex(p,bb)
            vhist[tag]=vhist.get(tag,0)+1
    print(f"# exceed 1/15: {nexceed}/{len(cfgs)}")
    print(f"# vertex-structure histogram (achieving-strategy tags):")
    for tag,c in sorted(vhist.items(),key=lambda z:-z[1])[:15]:
        print(f"#   {c:4d}  {tag}")
    if worst:
        print("# worst exceeders:")
        for p,d,bb in worst[:6]:
            print(f"#   p={[round(x,4) for x in p]} D={d:.5f} bb={bb}")
    print(f"# elapsed {time.time()-t0:.1f}s")

if __name__=="__main__":
    main()
