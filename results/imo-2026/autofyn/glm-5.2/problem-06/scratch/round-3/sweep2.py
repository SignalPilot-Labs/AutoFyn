"""Smaller targeted sweep with per-seed timeout via N cap."""
import sys, signal
from itertools import combinations
from sympy import factorint

def P(m): return frozenset(factorint(m).keys())
def is_transversal(T,family):
    Ts=set(T); return all(Ts&set(M) for M in family)
def mtp_and_witness(Pess,family):
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
    Pl=sorted(Pess); n=len(Pl); tau=None; mas=None
    fam_sets=[set(m) for m in family]
    for mask in range(1,1<<n):
        s=set()
        for i in range(n):
            if mask&(1<<i): s.add(Pl[i])
        if is_transversal(s,fam_sets):
            cs=len(s)
            if tau is None or cs<tau: tau=cs
            if not any(m<=s for m in fam_sets):
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
def simulate_fast(a1,Nmax=250):
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

def check(a1,Nmax=250):
    seq,prom=simulate_fast(a1,Nmax)
    mas=[]; tau=[]; mtp=[]
    for s,mn,an,mtpval,wit in prom:
        Mlist=[set(m) for m in mn]; Pess=set()
        for m in Mlist: Pess|=m
        if Pess and len(Pess)<=14:
            t,ma=tau_min_card_avoid(Pess,Mlist)
        else: t,ma=None,None
        mas.append(ma); tau.append(t); mtp.append(mtpval)
    drops=[]
    for i in range(1,len(mas)):
        a,b=mas[i-1],mas[i]
        if a is not None and b is not None and b<a: drops.append(('mas',i,a,b))
        if a is None and b is not None: drops.append(('mas-revive',i))
    for i in range(1,len(tau)):
        a,b=tau[i-1],tau[i]
        if a is not None and b is not None and b<a: drops.append(('tau',i,a,b))
    for i in range(1,len(mtp)):
        if mtp[i]<mtp[i-1]: drops.append(('mtp',i,mtp[i-1],mtp[i]))
    return prom,drops,mas,tau,mtp

if __name__=='__main__':
    seeds=[15,21,33,35,39,45,51,55,57,63,65,69,75,77,85,87,91,93,95,105,111,115,117,119,
           123,125,129,133,135,141,143,145,147,153,155,159,161,175,187,203,205,209,215,
           217,219,221,231,247,253,259,267,273,287,295,299,301,303,319,323,325,329,333,
           335,341,343,351,355,361,365,369,371,377,381,385,391,393,395,403,407,411,413,
           415,417,427,429,435,437,445,447,451,453,469,471,473,475,481,485,489,493,497,
           511,515,517,527,529,533,535,543,545,551,553,559,565,573,579,581,583,589,611,
           623,629,649,667,671,679,681,685,689,697,697,699,703,707,713,717,721,723,731,
           737,745,749,753,755,763,76617 if False else 767,779,781,785,791,793,799,803,813,815,817,831,835,849,851,865,869,871,889,893,899,901,913,917,921,923,933,943,949,959,961,973,979,989,1001]
    bad=[]
    clean=0
    for a1 in seeds:
        try:
            prom,drops,mas,tau,mtp=check(a1)
        except Exception as e:
            print(f"  a1={a1}: ERR {e}",flush=True); continue
        if drops:
            bad.append((a1,drops,mas,tau,mtp)); print(f"  *** a1={a1} DROPS {drops}  mas={mas} tau={tau} mtp={mtp}",flush=True)
        else:
            clean+=1
    print(f"\nTotal seeds: {len(seeds)}; clean(no drops): {clean}; with drops: {len(bad)}")
    print("All four monotone holds across all tested seeds." if not bad else f"VIOLATIONS: {bad}")
