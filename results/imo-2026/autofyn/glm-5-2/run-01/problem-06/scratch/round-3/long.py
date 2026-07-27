import math, sys, time
sys.path.insert(0, '/tmp/round-3')
from probe_fs import spf_table, factor, minimal_family_inc, mtp_of
N = 2000000
spf = spf_table(N)

def cheap_tp(M):
    s=set()
    for mm in M:
        if mm: s.add(min(mm))
    p=1
    for q in s: p*=q
    return p

def run_track(a1, Nmax, spf, sample_every=50):
    a=[a1]; P1=factor(a1,spf); M=[P1]; Pess=set(P1); gaps=[]
    last=tuple(sorted([tuple(sorted(s)) for s in M])); stable=0
    fb=0; maxgap=0
    samples=[]
    for n in range(1,Nmax):
        an=a[-1]; m=an+1; cap=an+a1
        while m<=cap:
            Pm=factor(m,spf)
            if all(Pm & Mm for Mm in M): break
            m+=1
        if m>cap:
            bnd=cheap_tp(M); m=an+1; fb+=1
            while m<=an+bnd:
                Pm=factor(m,spf)
                if all(Pm & Mm for Mm in M): break
                m+=1
        a.append(m); g=m-an; gaps.append(g)
        if g>maxgap: maxgap=g
        new_P=factor(m,spf); new_M=minimal_family_inc(M,new_P)
        if set(new_M)!=set(M):
            Pess=set()
            for S in new_M: Pess|=set(S)
        M=new_M
        r=tuple(sorted([tuple(sorted(s)) for s in M]))
        if r==last: stable+=1
        else: stable=0; last=r
        if n % sample_every == 0 or stable>=200:
            samples.append((n, len(M), len(Pess), maxgap, stable, fb))
        if stable>=300:
            break
    return a,gaps,M,Pess,fb,maxgap,samples

OUT=open('/tmp/round-3/long_out.txt','w')
def P(*a):
    print(*a,file=OUT); OUT.flush()

slow_seeds = [511, 679, 725, 833, 867, 1587, 2023, 2047, 2523, 2783, 4107, 9251, 15341, 26071, 27869]
P(f"Running slow seeds up to 2000 terms, spf={N}")
for a1 in slow_seeds:
    if a1 >= N: continue
    f=sorted(factor(a1,spf))
    t=time.time()
    a,gaps,M,Pess,fb,mg,samples = run_track(a1, 2000, spf, sample_every=100)
    dt=time.time()-t
    P(f"\na1={a1} ({f}): {dt:.1f}s, terms={len(a)}, |M|_final={len(M)}, |Pess|_final={len(Pess)}, maxgap={mg}, fallbacks={fb}, stabilized={'YES' if len(Pess)<=14 else 'NO (still large)'}")
    P(f"  samples (n, |M|, |Pess|, maxgap, stable, fb):")
    for s in samples:
        P(f"    {s}")
