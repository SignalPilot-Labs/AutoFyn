"""Transversal-product RACE probe: at each strict-beat promotion, find WHICH
transversal T'' (product L'') the pick a_next is a multiple of (L'' | a_next),
and whether T'' contains a small prime (<=p*). Rank transversals by product to
see if all-large transversals ever come close to winning."""
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
    Pm=P(m);return all(Pm&S for S in M)
def probe(a1,Nsteps=60,maxPess=12):
    pstar=min(P(a1))
    F=[P(a1)];M=minimal_supports(F);a=[a1]
    for step in range(1,Nsteps):
        an=a[-1]
        Pess=set()
        for S in M: Pess|=S
        if len(Pess)>maxPess:
            a.append(an+1);F.append(P(an+1));M=minimal_supports(F);continue
        Ts=transversals(Pess,M)
        if not Ts:
            m=an+1
            while not is_valid(m,M): m+=1
            a.append(m);F.append(P(m));M=minimal_supports(F);continue
        # mtp/witness
        prods=[(math.prod(T),T) for T in Ts]
        prods.sort()
        mtp_val,witT=prods[0]
        mu=(an//mtp_val+1)*mtp_val
        if mu<=an: mu+=mtp_val
        # greedy pick
        m=an+1
        while not is_valid(m,M): m+=1
        anext=m
        # is anext a promotion (new minimal)?
        Panext=P(anext)
        is_promo = not any(S<=Panext for S in M) and (Panext not in M)
        is_sb = (anext<mu) and is_promo
        if is_sb:
            # which transversals T'' divide anext?
            divT=[(math.prod(T),sorted(T)) for T in Ts if math.prod(T)>0 and anext%math.prod(T)==0]
            divT.sort()
            # smallest-product transversal dividing anext
            # does the smallest such contain a small prime?
            if divT:
                smallest_prod,smallest_T=divT[0]
                has_small=any(p<=pstar for p in smallest_T)
                all_large_winners=[T for _,T in divT if not any(p<=pstar for p in T)]
                print(f'a1={a1} step{step}: a_n={an} a_next={anext} mu={mu} mtp={mtp_val} wit={sorted(witT)}')
                print(f'  P(a_next)={sorted(Panext)} p*={pstar}')
                print(f'  transversals dividing a_next (prod,T): {divT[:5]}{"..." if len(divT)>5 else ""}')
                print(f'  smallest dividing T={smallest_T} has_small_prime={has_small}; all-large dividers={all_large_winners}')
        a.append(anext);F.append(Panext);M=minimal_supports(F)
        if step>10 and len(set(a[-5:]))==1: break
for a1 in [1155,1365,2145,5005,385,175,899]:
    print('#'*70);print('a1=',a1,'p*=',min(P(a1)));probe(a1)
