"""Probe: tau (min transversal cardinality), min avoiding-transversal size, fixed-witness trace family."""
import sys
from itertools import combinations
from sympy import factorint

def P(m): return frozenset(factorint(m).keys())

def is_transversal(T, family):
    Ts=set(T); return all(Ts & set(M) for M in family)

def mtp_and_witness(Pess, family):
    Pl=sorted(Pess); n=len(Pl); best=None; bestset=None
    for mask in range(1,1<<n):
        s=set()
        for i in range(n):
            if mask&(1<<i): s.add(Pl[i])
        if is_transversal(s,family):
            prod=1
            for p in s: prod*=p
            if best is None or prod<best: best=prod; bestset=frozenset(s)
    return best,bestset

def tau_min_card_avoid(Pess,family):
    """tau = min cardinality of transversal; min_avoid_size = min |T| over AVOIDING transversals (None if self-blocking)."""
    Pl=sorted(Pess); n=len(Pl)
    tau=None; mas=None
    fam_sets=[set(m) for m in family]
    for mask in range(1,1<<n):
        s=set()
        for i in range(n):
            if mask&(1<<i): s.add(Pl[i])
        if is_transversal(s,fam_sets):
            cs=len(s)
            if tau is None or cs<tau: tau=cs
            # avoiding? contains no member of family as subset
            if not any(m <= s for m in fam_sets):
                if mas is None or cs<mas: mas=cs
    return tau,mas

def minimal_supports(fam_list):
    fam=list(set(fam_list))
    return frozenset(S for S in fam if not any(T<S for T in fam))

def greedy_next(an,Mn,mtpval,cap=20000):
    m=an+1; hi=an+mtpval
    while m<=hi:
        pm=P(m)
        if all(set(pm)&set(M) for M in Mn): return m
        m+=1
        if m-an>cap: return None
    return m

def simulate_fast(a1,Nmax=2000):
    seq=[a1]; fam_list=[P(a1)]; Mn=minimal_supports(fam_list)
    Pess=set()
    for m in Mn: Pess|=set(m)
    mtpval,wit=mtp_and_witness(Pess,[set(m) for m in Mn])
    prom=[(1,Mn,a1,mtpval,wit)]
    for step in range(2,Nmax+1):
        an=seq[-1]; m=greedy_next(an,Mn,mtpval)
        if m is None: break
        seq.append(m); fam_list.append(P(m))
        new_Mn=minimal_supports(fam_list)
        if new_Mn!=Mn:
            newPess=set()
            for mm in new_Mn: newPess|=set(mm)
            newmtp,newwit=mtp_and_witness(newPess,[set(mm) for mm in new_Mn])
            prom.append((step,new_Mn,m,newmtp,newwit)); Mn=new_Mn; mtpval=newmtp; wit=newwit
    return seq,prom

def run(a1,Nmax=2000):
    seq,prom=simulate_fast(a1,Nmax)
    print(f"\n=== a1={a1}  N={len(seq)}  prom={len(prom)} ===")
    rows=[]
    final_wit=prom[-1][4]
    for s,mn,an,mtpval,wit in prom:
        Mlist=[set(m) for m in mn]
        Pess=set()
        for m in Mlist: Pess|=m
        if Pess and len(Pess)<=14:
            tau,mas=tau_min_card_avoid(Pess,Mlist)
        else:
            tau,mas=None,None
        # fixed-witness trace family against FINAL witness
        fwt=set(final_wit) if final_wit else set()
        trace_fam=frozenset(frozenset(m&fwt) for m in Mlist)
        rows.append((s,an,tau,mas,mtpval,len(trace_fam),trace_fam,wit))
        print(f"  st {s:>4} a={an:>7} tau={tau} minAvSz={mas} mtp={mtpval} fixTr#={len(trace_fam)} wit={sorted(wit) if wit else []}")
    print(f"  FINAL M: {[set(x) for x in prom[-1][1]]}  final_wit={sorted(final_wit)}")
    for k,name in [(2,'tau'),(3,'minAvSz'),(4,'mtp'),(5,'fixTr#')]:
        vals=[r[k] for r in rows if r[k] is not None]
        if len(vals)<2: continue
        mi=all(vals[i]<=vals[i+1] for i in range(len(vals)-1))
        md=all(vals[i]>=vals[i+1] for i in range(len(vals)-1))
        flag="MONO-INC" if mi else ("MONO-DEC" if md else "NOT-MONO")
        print(f"    {name}: {flag} distinct={len(set(vals))} trace={vals}")
    return rows

if __name__=='__main__':
    a1=int(sys.argv[1]); N=int(sys.argv[2]) if len(sys.argv)>2 else 2000
    run(a1,N)
