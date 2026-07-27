"""Sweep many odd a1 seeds; hunt for any minAvSz DROP (counterexample to monotonicity)."""
import sys
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
def simulate_fast(a1,Nmax=400):
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

def check(a1,Nmax=400):
    seq,prom=simulate_fast(a1,Nmax)
    trace_mas=[]; trace_tau=[]; trace_mtp=[]
    drops=[]
    for s,mn,an,mtpval,wit in prom:
        Mlist=[set(m) for m in mn]; Pess=set()
        for m in Mlist: Pess|=m
        if Pess and len(Pess)<=14:
            tau,mas=tau_min_card_avoid(Pess,Mlist)
        else: tau,mas=None,None
        trace_mas.append(mas); trace_tau.append(tau); trace_mtp.append(mtpval)
    # detect drops
    for i in range(1,len(trace_mas)):
        a,b=trace_mas[i-1],trace_mas[i]
        if a is not None and b is not None and b<a:
            drops.append(('mas',i,a,b))
        if a is None and b is not None:
            drops.append(('mas-revive',i,a,b))
    for i in range(1,len(trace_tau)):
        a,b=trace_tau[i-1],trace_tau[i]
        if a is not None and b is not None and b<a:
            drops.append(('tau',i,a,b))
    for i in range(1,len(trace_mtp)):
        if trace_mtp[i]<trace_mtp[i-1]:
            drops.append(('mtp',i,trace_mtp[i-1],trace_mtp[i]))
    return prom, drops, trace_mas, trace_tau, trace_mtp

if __name__=='__main__':
    # sweep odd composite a1 in a range
    bad=[]
    for a1 in range(15, 600, 2):
        f=factorint(a1)
        if len(f)<2 or a1 in (1,): continue
        # skip even (handled) ; skip prime powers
        try:
            prom,drops,mas,tau,mtp=check(a1,300)
        except Exception as e:
            continue
        if drops:
            bad.append((a1,drops,mas,tau))
    print(f"swept a1 in [15,600) odd-composite; seeds with drops: {len(bad)}")
    for a1,drops,mas,tau in bad[:20]:
        print(f"  a1={a1} drops={drops} mas={mas} tau={tau}")
    # also a curated list
    for a1 in [1001,2465,3255,4199,5005,323,667,187,221,385,429,175,105,15,231,21]:
        try:
            prom,drops,mas,tau,mtp=check(a1,300)
            status = "CLEAN" if not drops else f"DROPS {drops}"
            print(f"  curated a1={a1}: {status}  mas={mas} tau={tau} mtp={mtp}  prom={len(prom)}")
        except Exception as e:
            print(f"  curated a1={a1}: ERR {e}")
