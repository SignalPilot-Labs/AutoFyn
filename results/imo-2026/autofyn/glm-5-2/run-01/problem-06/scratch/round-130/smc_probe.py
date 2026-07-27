"""SMC probe: at every step of every seed, check whether SOME minimal M in M_n
satisfies M ⊆ S = {p : p <= p*}. If always true, W2 (and W1) hold trivially
because every transversal must then meet S (every valid number is
small-prime-divisible). Also check the stronger 'every minimal has a prime<=p*'
(SPT) and the witness-small-prime (W1) for cross-reference.
Also look for the WEAKEST invariant: is {2,p*} in M_n? (then SMC trivial)"""
import math
from sympy import factorint
def P(m): return set(factorint(m).keys())
def minimal_supports(F):
    out=[]
    for S in F:
        if any(T<S for T in F): continue
        out.append(S)
    seen=[];r=[]
    for S in out:
        if S not in seen: seen.append(S);r.append(S)
    return r
def transversals(Pess,M):
    Pess=list(Pess);n=len(Pess);res=[]
    for mask in range(1,1<<n):
        T=set(Pess[i] for i in range(n) if mask&(1<<i))
        if all(T&S for S in M): res.append(T)
    return res
def is_valid(m,M):
    Pm=P(m)
    return all(Pm&S for S in M)
def probe(a1,Nsteps=80,maxPess=14):
    pstar=min(P(a1))
    F=[P(a1)];M=minimal_supports(F);a=[a1]
    smc_fail=[]; spt_fail=[]; cov_hist=[]
    for step in range(1,Nsteps):
        an=a[-1]
        Pess=set()
        for S in M: Pess|=S
        Sset={p for p in Pess if p<=pstar}
        # SMC: some minimal subseteq Sset
        smc=any(Mi<=Sset for Mi in M)
        # SPT: every minimal has a prime in Sset
        spt=all(Mi&Sset for Mi in M)
        # {2,p*} in M?
        has2pstar = ({2,pstar} in M)
        if not smc: smc_fail.append((step,sorted(sorted(s) for s in M),sorted(Sset)))
        if not spt: spt_fail.append((step,sorted(sorted(s) for s in M),sorted(Sset)))
        cov_hist.append(('2,p*?' ,has2pstar, 'smc',smc,'spt',spt))
        # advance greedy
        m=an+1
        while not is_valid(m,M):
            m+=1
            if m>an+10**6: raise RuntimeError
        anext=m
        a.append(anext);F.append(P(anext));M=minimal_supports(F)
        if step>10 and len(set(a[-5:]))==1: break
    return smc_fail,spt_fail,cov_hist
seeds=[15,35,77,91,105,143,175,195,323,385,899,1147,1365,2145,4199,5005,1001,1155]
for a1 in seeds:
    try:
        smc,spt,ch=probe(a1,Nsteps=60)
    except Exception as e:
        print(a1,'ERR',e);continue
    print(f'a1={a1} p*={min(P(a1))}: SMC_fails={len(smc)} SPT_fails={len(spt)} steps_run={len(ch)}')
    if smc:
        print('  ALL SMC fails:',smc[:8])
