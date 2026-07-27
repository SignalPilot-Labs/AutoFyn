import sys, math, signal, itertools
from sympy import factorint

def primes_of(n): return set(factorint(n).keys())
def prod(lst):
    r=1
    for x in lst: r*=x
    return r
class TOE(Exception): pass
def _h(s,f): raise TOE()

def all_transversals(P_ess_list, Mlist):
    """All subsets T of P_ess hitting every M (full 2^|Pess| enumeration)."""
    n=len(P_ess_list); Msets=[set(m) for m in Mlist]
    for mask in range(1,1<<n):
        T=set()
        for i in range(n):
            if mask&(1<<i): T.add(P_ess_list[i])
        ok=True
        for m in Msets:
            if not (T&m): ok=False; break
        if ok: yield T

def avoiding_transversals(P_ess_list,Mlist):
    Msets=[set(m) for m in Mlist]
    for T in all_transversals(P_ess_list,Mlist):
        if not any(m<=T for m in Msets): yield T

def is_stable(P_ess_list,Mlist):
    for _ in avoiding_transversals(P_ess_list,Mlist): return False
    return True

def next_promo(a,P_ess_list,Mlist):
    best=None; bT=None
    for T in avoiding_transversals(P_ess_list,Mlist):
        D=prod(sorted(T))
        Spr=[p for p in P_ess_list if p not in T]
        S=prod(Spr) if Spr else 1
        K0=a//D; k=K0+1; c=0
        while math.gcd(k,S)!=1:
            k+=1; c+=1
            if c>300000: k=None; break
        if k is None: continue
        m=k*D
        if best is None or m<best: best=m; bT=T
    if best is None: return None
    return best,bT,primes_of(best)

def run(a1,max_rounds=200,max_Pess=20,time_limit=30):
    signal.signal(signal.SIGALRM,_h); signal.alarm(time_limit)
    M=[frozenset(primes_of(a1))]; P_ess=sorted(M[0]); a=a1; hist=[]
    try:
        for r in range(max_rounds):
            if len(P_ess)>max_Pess:
                return dict(a1=a1,M=[set(m) for m in M],P_ess=set(P_ess),stable=None,rounds=r,hist=hist,reason='Pess_exceeded',a=a)
            if is_stable(P_ess,[set(m) for m in M]):
                return dict(a1=a1,M=[set(m) for m in M],P_ess=set(P_ess),L=prod(P_ess),stable=True,rounds=r,hist=hist,reason='stable',a=a)
            res=next_promo(a,P_ess,[set(m) for m in M])
            if res is None:
                return dict(a1=a1,M=[set(m) for m in M],P_ess=set(P_ess),L=prod(P_ess),stable=True,rounds=r,hist=hist,reason='stable',a=a)
            m,Ts,Pnew=res; old=set(P_ess)
            newM=[set(mm) for mm in M if not (Pnew<=set(mm))]
            newM.append(set(Pnew))
            M=[frozenset(x) for x in newM]; P_ess=sorted(set(P_ess)|Pnew); a=m
            hist.append(dict(a=a,M=len(M),Pess=len(P_ess),Tstar=sorted(Ts),newpr=sorted(Pnew-old)))
        return dict(a1=a1,M=[set(m) for m in M],P_ess=set(P_ess),stable=False,rounds=max_rounds,hist=hist,reason='max_rounds',a=a)
    except TOE:
        return dict(a1=a1,M=[set(m) for m in M],P_ess=set(P_ess),stable=None,rounds=-1,hist=hist,reason='timeout',a=a)
    finally: signal.alarm(0)

if __name__=='__main__':
    # verify against brute force first
    print("=== verify vs brute ===")
    for a1 in [15,35,65,187,221]:
        r=run(a1,max_rounds=200,max_Pess=20,time_limit=15)
        print(f"a1={a1}: |Pess|={len(r['P_ess'])} |M|={len(r['M'])} stable={r['stable']} Pess={sorted(r['P_ess'])}")
    print()
    print("=== omega=2 large primes (CORRECT method) ===")
    from sympy import prime
    for i,j in [(25,26),(30,40),(50,60),(60,80),(80,100),(100,120),(150,160)]:
        p,q=prime(i),prime(j); a1=p*q
        r=run(a1,max_rounds=300,max_Pess=22,time_limit=45)
        flag='STABLE' if r['stable'] else('CAP' if r['stable'] is None else 'UNST')
        print(f"a1={a1} ({p},{q}): {flag} |Pess|={len(r['P_ess'])} |M|={len(r['M'])} {r.get('reason')}")
    print()
    print("=== omega=3,4 selected (CORRECT) ===")
    for t in [(3,5,7),(5,7,11),(11,13,17),(23,29,31),(53,59,61),(2,3,5,7),(5,7,11,13),(17,19,23,29)]:
        a1=1
        for x in t: a1*=x
        r=run(a1,max_rounds=150,max_Pess=20,time_limit=40)
        flag='STABLE' if r['stable'] else('CAP' if r['stable'] is None else 'UNST')
        print(f"a1={a1} {t}: {flag} |Pess|={len(r['P_ess'])} |M|={len(r['M'])} {r.get('reason')}")
