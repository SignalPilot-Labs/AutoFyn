"""Search for seeds where an entering essential prime EXCEEDS a1.
Also track, at each promotion: the introducing term a_{n+1}, its value, the new minimal, the entering prime q, and q vs a_{n+1}/smallest_cofactor, q vs a1, q vs mtp_at_entry."""
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
        for combo in combinations(range(n),k):
            T=set(Pess_list[i] for i in combo)
            if all(T & Mm for Mm in M_sets):
                prod=1
                for p in T: prod*=p
                if best is None or prod<best:
                    best=prod; bestT=frozenset(T)
    return best,bestT

def run(a1, Nmax=8000, stable_window=250):
    a=[a1]
    Pfam=[frozenset(primes(a1))]
    M=[Pfam[0]]
    Pess=set(Pfam[0])
    promos=[]  # (step, a_val, new_minimal, entered_primes, mtp_before)
    last_repr=None; stable=0
    for n in range(1,Nmax):
        m=a[-1]+1
        while True:
            Pm=primes(m)
            if all(Pm & set(Mm) for Mm in M):
                break
            m+=1
        a.append(m)
        new_Pm=frozenset(primes(m))
        # mtp before update (i.e., of current M)
        mb,_ = mtp_val(list(Pess), [set(s) for s in M]) if len(Pess)<=18 else (None,None)
        is_new=True; new_M=[]
        for S in M:
            if new_Pm < S: continue  # removed
            if S < new_Pm or S==new_Pm: is_new=False; new_M.append(S); continue
            new_M.append(S)
        if is_new and not any(S==new_Pm for S in new_M):
            new_M.append(new_Pm)
        new_M=sorted(new_M, key=lambda s:(len(s),sorted(s)))
        promotion = (is_new and new_Pm not in [frozenset(s) for s in M]) or len(new_M)<len(M)
        if promotion:
            entered = set(new_Pm)-Pess
            if entered:
                promos.append((n, m, sorted(new_Pm), sorted(entered), mb))
            Pess=set()
            for S in new_M: Pess|=set(S)
        M=new_M
        reprM=tuple(sorted([tuple(sorted(s)) for s in M]))
        if reprM==last_repr: stable+=1
        else: stable=0; last_repr=reprM
        if stable>=stable_window: break
    return a,M,Pess,promos

def search_max_entering(seeds):
    print("=== Per-seed max entering prime vs a1 ===")
    for s in seeds:
        a,M,Pess,promos=run(s)
        all_entered=set()
        for _,_,_,ent,_ in promos: all_entered|=set(ent)
        mx=max(all_entered) if all_entered else 0
        mf,_=mtp_val(sorted(Pess),[set(x) for x in M]) if len(Pess)<=20 else (None,None)
        print(f"a1={s}({sorted(primes(s))}): max_entering={mx}, a1={s}, ratio={mx/s if s else 0:.3f}, max_entering>a1? {mx>s}, |M_final|={len(M)}, Pess_final={sorted(Pess)}, mtp_final={mf}, n_promos={len(promos)}")
        # report large entering primes
        big=[p for p in all_entered if p>s//2]
        if big: print(f"    entering primes > a1/2: {sorted(big)}")

if __name__=='__main__':
    seeds=[15,21,105,175,187,221,231,385,429,1001,19549,323,667,113*173,23*89,17*19*23,
           7*11,7*13,11*13,5*7*11,5*7*13,5*11*13,7*11*13,3*5*7*11,3*5*7*13,
           3*5*11,3*7*11,3*7*13,3*11*13,5*7,5*11,5*13,7*17,11*17,11*19,13*17,13*19,17*19,17*23,19*23,23*29,
           2*3*5*7*11,3*5*7*11*13,3*5*7*11*13*17]
    search_max_entering(seeds)
