import math, sys, itertools, time
sys.path.insert(0, '/tmp/round-3')
from probe_fs import spf_table, factor, minimal_family_inc, mtp_of

OUT = open('/tmp/round-3/scan_out.txt','w')
def P(*a):
    print(*a, file=OUT); OUT.flush()

N = 400000
spf = spf_table(N)
P(f"spf built N={N}")

def cheap_tp(M):
    s=set()
    for mm in M:
        if mm: s.add(min(mm))
    p=1
    for q in s: p*=q
    return p

def run_fast(a1, Nmax, spf, stable_window=30):
    a=[a1]; P1=factor(a1,spf); M=[P1]; Pess=set(P1); gaps=[]
    last_repr=tuple(sorted([tuple(sorted(s)) for s in M])); stable=0
    ent_total=set()
    fallback_count=0
    for n in range(1,Nmax):
        an=a[-1]
        # candidate bound: a1 (tests mtp<=a1 conjecture). fallback to cheap_tp if none found.
        m=an+1; cap=an+a1
        while m<=cap:
            Pm=factor(m,spf)
            if all(Pm & Mm for Mm in M): break
            m+=1
        if m>cap:
            # fallback: use cheap_tp bound (rare)
            bnd=cheap_tp(M)
            m=an+1
            while m<=an+bnd:
                Pm=factor(m,spf)
                if all(Pm & Mm for Mm in M): break
                m+=1
            fallback_count+=1
        a.append(m); gaps.append(m-an)
        new_P=factor(m,spf); new_M=minimal_family_inc(M,new_P)
        if set(new_M)!=set(M):
            ent_total |= (set(new_P)-Pess)
            Pess=set()
            for S in new_M: Pess|=set(S)
        M=new_M
        r=tuple(sorted([tuple(sorted(s)) for s in M]))
        if r==last_repr: stable+=1
        else: stable=0; last_repr=r
        if stable>=stable_window: break
    return a,gaps,M,Pess,ent_total,fallback_count

a1s = set()
for p,q in [(3,5),(3,7),(3,11),(3,13),(3,17),(3,19),(3,23),(3,29),(3,31),(3,37),(3,41),(3,43),(3,47),
            (5,7),(5,11),(5,13),(5,17),(5,19),(5,23),(5,29),(5,31),
            (7,11),(7,13),(7,17),(7,19),(7,23),(7,29),
            (11,13),(11,17),(11,19),(11,23),(11,29),
            (13,17),(13,19),(13,23),(17,19),(17,23),(19,23),(19,29),(23,29),(29,31)]:
    a1s.add(p*q); a1s.add(p*p*q); a1s.add(p*q*q)
for p,q,r in [(3,5,7),(3,5,11),(3,7,11),(5,7,11),(3,5,13),(3,7,13),(5,7,13),(3,11,13),(7,11,13),(3,5,17),(3,7,17),(5,7,17),(3,5,19),(11,13,17),(17,19,23)]:
    a1s.add(p*q*r)
for x in [19549,4199,5005,23*89,17*19*23,7*73,7*97,11*97,13*97,3*97,5*97,11*67,3*5*97,3*7*97,5*7*97,3*11*97]:
    if 2<=x<N: a1s.add(x)
a1s = sorted(a1s)
P(f"scanning {len(a1s)} odd composite seeds")
t0=time.time()
max_ratio=0; max_ratio_seed=None
max_mtp=0; max_mtp_seed=None
ratios_le1=0; ratios_gt1=0
extremals=[]
done=0
for a1 in a1s:
    if a1<2 or a1>=N: continue
    f=factor(a1,spf)
    if a1%2==0: continue
    if len(f)<2: continue
    if time.time()-t0>90: P(f"  budget hit at a1={a1}"); break
    ts=time.time()
    a,gaps,M,Pess,ent,fb = run_fast(a1, 200, spf, stable_window=25)
    dt=time.time()-ts
    if not Pess: continue
    if len(Pess) > 14:
        P(f"  LARGE Pess a1={a1} |Pess|={len(Pess)} |M|={len(M)} (not stabilized in 200 terms); mtp skipped")
        continue
    mtp_f = mtp_of(sorted(Pess), M)
    if mtp_f is None: continue
    mg = max(gaps) if gaps else 0
    ratio = mtp_f/a1
    if ratio>max_ratio: max_ratio=ratio; max_ratio_seed=a1
    if mtp_f>max_mtp: max_mtp=mtp_f; max_mtp_seed=a1
    if mtp_f<=a1: ratios_le1+=1
    else: ratios_gt1+=1
    if fb>0: P(f"  FALLBACK a1={a1} fb={fb} (mtp>a1 conjecture may fail here)")
    if ratio>0.25 or mtp_f>40 or mg>mtp_f or dt>1.5 or fb>0:
        extremals.append((a1,sorted(f),mtp_f,mg,len(M),sorted(Pess),max(ent) if ent else 0,ratio,dt))
    done+=1
P(f"scanned {done} seeds in {time.time()-t0:.1f}s")
P(f"max(mtp/a1)={max_ratio:.4f} at a1={max_ratio_seed}")
P(f"max(mtp)={max_mtp} at a1={max_mtp_seed}")
P(f"mtp<=a1: {ratios_le1}, mtp>a1: {ratios_gt1}")
P(f"\nExtremals (ratio>0.25 or mtp>40 or maxgap>mtp or slow):")
P(f"{'a1':>8} {'factors':>22} {'mtp':>5} {'maxgap':>6} {'gap>mtp':>7} {'|M|':>3} {'maxEnt':>6} {'ratio':>6} {'secs':>5}")
for a1,f,mtp,mg,nM,Pess,maxE,ratio,dt in sorted(extremals, key=lambda x:-x[7]):
    P(f"{a1:>8} {str(f):>22} {mtp:>5} {mg:>6} {str(mg>mtp):>7} {nM:>3} {maxE:>6} {ratio:>6.3f} {dt:>5.1f}")
