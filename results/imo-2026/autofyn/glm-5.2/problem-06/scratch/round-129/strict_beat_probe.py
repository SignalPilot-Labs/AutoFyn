"""Focused: at each promotion, record the mtp-witness, whether it contains 2,
whether a_{n+1} < witness-multiple (strict beat), and the small primes of a_{n+1}.
Test the hypothesis: the witness always contains a prime <= p* (ideally 2),
so the witness-multiple in the window is valid+small-prime; the promotion's a_{n+1}
strictly beats it and the question is WHY a_{n+1} also carries a small prime.
"""
import sympy
from itertools import combinations

def P(m): return set(sympy.primefactors(m))

def minimal_family(fam_list):
    mins=[]
    for S in fam_list:
        if any((other<S) for other in fam_list if other!=S): continue
        mins.append(S)
    out=[]
    for S in mins:
        if S not in out: out.append(S)
    return out

def mtp_and_witness(Mfam, Pess):
    plist=sorted(Pess); n=len(plist)
    if n>16: return (None,None)
    best=None; bestT=None
    for k in range(1,n+1):
        for combo in combinations(range(n),k):
            T=set(plist[i] for i in combo)
            if all(T&Mm for Mm in Mfam):
                prod=1
                for p in T: prod*=p
                if best is None or prod<best:
                    best=prod; bestT=frozenset(T)
    return (best,bestT)

def run(a1, max_steps=4000, stable_window=80):
    a=[a1]; fam=[P(a1)]; Mn=minimal_family(fam); Pess=set(P(a1))
    pstar=min(P(a1)); Pfam1=P(a1)
    promos=[]
    has2_in_witness=0; has2_total=0; computed=0
    for n in range(1,max_steps):
        m=a[-1]+1
        while True:
            Pm=P(m)
            if all(Pm&Mi for Mi in Mn): break
            m+=1
        Pm=P(m)
        mtp_val,Tstar=mtp_and_witness(Mn,Pess)
        is_promo=not any(S<=Pm for S in Mn)
        if Tstar is not None:
            computed+=1
            if 2 in Tstar: has2_in_witness+=1
            has2_total+=1
        if is_promo and Tstar is not None:
            import math
            wmult=((a[-1]//mtp_val)+1)*mtp_val
            strict_beat = (m < wmult)
            small_primes_next=sorted(p for p in Pm if p<=pstar)
            small_primes_T=sorted(p for p in Tstar if p<=pstar)
            promos.append({'n':n,'a_n':a[-1],'a_next':m,'gap':m-a[-1],
                'mtp':mtp_val,'wmult':wmult,'strict_beat':strict_beat,
                'P_next':sorted(Pm),'Tstar':sorted(Tstar),
                'small_next':small_primes_next,'small_T':small_primes_T,
                'Mn_before':[sorted(s) for s in Mn]})
        a.append(m); fam.append(Pm); Mn=minimal_family(fam)
        Pess=set()
        for S in Mn: Pess|=S
        if n>stable_window: break
    regime='freeze' if (len(Mn)==1 and len(list(Mn)[0])==1 and list(list(Mn)[0])[0] in Pfam1) else 'saturated'
    return promos, regime, has2_in_witness, has2_total, computed

seeds=[15,35,105,165,385,429,1001,175,187,221,323,899,1147,1517,1763,667,1591,19549,5183,6161,10403,7387,8633,4199,7429,12673]
print("=== strict-beat & witness-small-prime at promotions (saturated) ===")
agg_strict=0; agg_promo=0; agg_witness_has2=0; agg_witness_total=0
for s in seeds:
    try:
        promos,reg,h2,ht,comp=run(s)
        if reg!='saturated': continue
        if not promos: continue
        ns=[p for p in promos if p['strict_beat']]
        w2=[p for p in promos if p['small_T']]
        wnone=[p for p in promos if not p['small_T']]
        allcarries=all(p['small_next'] for p in promos)
        agg_strict+=len(ns); agg_promo+=len(promos)
        agg_witness_has2+=sum(1 for p in promos if 2 in p['Tstar']); agg_witness_total+=len(promos)
        print(f"  a1={s} p*={min(P(s))}: #promo={len(promos)} strict_beat={len(ns)} witness_has_small={len(w2)} witness_no_small={len(wnone)} all_carry_small={allcarries} | computed_witness_steps={comp} witness_has2={h2}/{ht}")
        if wnone:
            print(f"     !! promotions with witness-NO-small-prime:")
            for p in wnone[:3]:
                print(f"        step{p['n']}: a_next={p['a_next']} P={p['P_next']} Tstar={p['Tstar']} small_next={p['small_next']}")
    except Exception as e:
        print(f"  a1={s} ERROR {e}")
print(f"\nAGG: promos={agg_promo} strict_beat={agg_strict} witness_has2={agg_witness_has2}/{agg_witness_total}")
