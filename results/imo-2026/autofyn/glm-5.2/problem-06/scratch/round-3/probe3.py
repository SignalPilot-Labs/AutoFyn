"""Detailed probe: for saturated seeds, track at each promotion the introducing term a_{n+1},
the new minimal, the entering prime q, q vs a_{n+1}/p_min, q vs a1/p_min, and whether q is a
free-rider (i.e. M' = new minimal contains a smaller transversal subset already).
Also test conjecture: max_entering <= a1/p_min(a1) across many seeds."""
import math
from itertools import combinations

def primes(n):
    s=set(); d=2
    while d*d<=n:
        while n%d==0: s.add(d); n//=d
        d+=1
    if n>1: s.add(n)
    return s

def mtp_val(Pess_list, M_sets):
    best=None; bestT=None
    n=len(Pess_list)
    for k in range(1,n+1):
        early=best
        for combo in combinations(range(n),k):
            T=set(Pess_list[i] for i in combo)
            if all(T & Mm for Mm in M_sets):
                prod=1
                for p in T: prod*=p
                if best is None or prod<best:
                    best=prod; bestT=frozenset(T)
    return best,bestT

def is_transversal(T, M_sets):
    return all(T & Mm for Mm in M_sets)

def run_detail(a1, Nmax=8000, stable_window=250):
    a=[a1]
    Pfam=[frozenset(primes(a1))]
    M=[Pfam[0]]
    Pess=set(Pfam[0])
    promos=[]
    last_repr=None; stable=0
    for n in range(1,Nmax):
        m=a[-1]+1
        while True:
            Pm=primes(m)
            if all(Pm & set(Mm) for Mm in M): break
            m+=1
        a.append(m)
        new_Pm=frozenset(primes(m))
        mb,_ = mtp_val(list(Pess), [set(s) for s in M]) if len(Pess)<=16 else (None,None)
        is_new=True; new_M=[]
        removed=[]
        for S in M:
            if new_Pm < S: removed.append(S); continue
            if S < new_Pm or S==new_Pm: is_new=False; new_M.append(S); continue
            new_M.append(S)
        if is_new and not any(S==new_Pm for S in new_M):
            new_M.append(new_Pm)
        new_M=sorted(new_M, key=lambda s:(len(s),sorted(s)))
        promotion = (is_new and new_Pm not in [frozenset(s) for s in M]) or len(removed)>0
        if promotion:
            entered = set(new_Pm)-Pess
            if entered:
                # is the new minimal a free-rider? i.e. does new_Pm contain a proper subset that is a transversal of OLD M?
                freerider_subsets=[]
                Pm_list=sorted(new_Pm)
                for k in range(1,len(Pm_list)):
                    for combo in combinations(range(len(Pm_list)),k):
                        sub=set(Pm_list[i] for i in combo)
                        if is_transversal(sub,[set(s) for s in M]):
                            freerider_subsets.append(sorted(sub)); break
                promos.append((n, m, sorted(new_Pm), sorted(entered), mb, freerider_subsets[:1]))
            Pess=set()
            for S in new_M: Pess|=set(S)
        M=new_M
        reprM=tuple(sorted([tuple(sorted(s)) for s in M]))
        if reprM==last_repr: stable+=1
        else: stable=0; last_repr=reprM
        if stable>=stable_window: break
    return a,M,Pess,promos

def report(a1):
    a,M,Pess,promos=run_detail(a1)
    pmin=min(primes(a1))
    all_ent=set()
    for _,_,_,ent,_,_ in promos: all_ent|=set(ent)
    mx=max(all_ent) if all_ent else 0
    cf=common_primes(M)
    print(f"\n=== a1={a1} ({sorted(primes(a1))}), p_min={pmin}, a1/p_min={a1//pmin} ===")
    print(f"  regime: {'FREEZE' if cf else 'SATURATED'}, |M_final|={len(M)}, Pess_final={sorted(Pess)}, max_entering={mx}, a1/p_min={a1//pmin}, max<=a1/p_min? {mx<=a1//pmin}")
    print(f"  mtp_final={mtp_val(sorted(Pess),[set(x) for x in M])[0] if len(Pess)<=16 else None}, n_promos={len(promos)}, final a_max~{a[-1]}")
    print(f"  promotions (n, a_val, new_min, entered, mtp_before, free_rider_subset):")
    for step,av,nm,ent,mb,fr in promos:
        q=max(ent)
        print(f"    n={step}: a={av}, new_min={nm}, entered={ent}, mtp_before={mb}, q_max={q}, q<=a/p_min={av//pmin}? {q<=av//pmin}, freerider_subset={fr}")

def common_primes(M):
    if not M: return set()
    c=set(M[0])
    for s in M[1:]: c&=s
    return c

if __name__=='__main__':
    for s in [15,105,175,385,429,1001,19549,323,667,187,221,2431,4199,7429,12673]:
        report(s)
    # broad conjecture test
    print("\n\n=== Broad test: max_entering <= a1/p_min ? ===")
    seeds=[3*5,3*7,5*7,3*11,3*13,5*11,5*13,7*11,7*13,11*13,11*17,13*17,17*19,19*23,23*29,29*31,
           3*5*7,3*5*11,3*5*13,3*7*11,3*7*13,3*11*13,5*7*11,5*7*13,5*11*13,7*11*13,7*11*17,11*13*17,13*17*19,17*19*23,19*23*29,23*29*31,
           3*5*7*11,3*5*7*13,3*5*11*13,5*7*11*13,7*11*13*17,11*13*17*19]
    for s in seeds:
        a,M,Pess,promos=run_detail(s,Nmax=4000,stable_window=120)
        all_ent=set()
        for _,_,_,ent,_,_ in promos: all_ent|=set(ent)
        mx=max(all_ent) if all_ent else 0
        pmin=min(primes(s))
        cf=common_primes(M)
        # only saturated
        sat = (not cf)
        bound=a1_over_pmin=s//pmin
        ok = mx<=bound
        print(f"a1={s}({sorted(primes(s))}): regime={'SAT' if sat else 'FRZ'}, max_ent={mx}, a1/p_min={bound}, ok={ok}, n_promos={len(promos)}")
