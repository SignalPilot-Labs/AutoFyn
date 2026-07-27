"""W2 mechanism probe: at each strict-beat promotion, dump the structure of M_n,
witnesses, the slack (mu - a_next), and which small primes divide a_next.
Also test mechanism (a): among the integers in (a_n, mu), is there always an
even valid number BELOW a_next? (if yes, contradiction since a_next is smallest)"""
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
def mtp_wits(Pess,M):
    Ts=transversals(Pess,M)
    if not Ts: return None,None
    best=min(math.prod(T) for T in Ts)
    return best,[T for T in Ts if math.prod(T)==best]
def is_valid(m,M):
    Pm=P(m)
    return all(Pm&S for S in M)
def probe(a1,Nsteps=80,maxPess=14):
    pstar=min(P(a1))
    a=[a1];F=[P(a1)];M=minimal_supports(F)
    for step in range(1,Nsteps):
        an=a[-1]
        Pess=set()
        for S in M: Pess|=S
        mtp_val,wits=(mtp_wits(Pess,M) if len(Pess)<=maxPess else (None,None))
        if mtp_val:
            mu=(an//mtp_val+1)*mtp_val
            if mu<=an: mu+=mtp_val
        else: mu=None
        # greedy
        m=an+1
        while not is_valid(m,M):
            m+=1
            if m>an+10**6: raise RuntimeError
        anext=m
        Panext=P(anext)
        dominated=any(S<=Panext for S in M)
        is_promo=not dominated and (Panext not in M)
        is_strictbeat=(mu is not None and anext<mu and is_promo)
        if is_strictbeat:
            slack=mu-anext
            # check: is there a valid even number in (an, anext)?
            # by definition no (anext is smallest valid). so check divisibility of anext by small primes
            smalls=[p for p in [2,3,5,7,11] if p<=pstar and p in Pess]
            divsmall=[p for p in smalls if anext%p==0]
            # also: enumerate the valid numbers in (an, mu) - should be just anext and maybe mu
            valid_in_win=[]
            m2=an+1
            while m2<=mu:
                if is_valid(m2,M): valid_in_win.append(m2)
                m2+=1
            print(f'a1={a1} step{step}: a_n={an} mu={mu} a_next={anext} slack={slack}')
            print(f'  Pess={sorted(Pess)} |M|={len(M)} mtp={mtp_val} wits={sorted(sorted(w) for w in wits)}')
            print(f'  M_n={sorted(sorted(s) for s in M)}')
            print(f'  P(a_next)={sorted(Panext)} minp={min(Panext)} p*={pstar}')
            print(f'  small primes in Pess (<=p*): {smalls}; dividing a_next: {divsmall}')
            print(f'  valid nums in (a_n,mu]: {valid_in_win}')
            print()
        a.append(anext);F.append(Panext);M=minimal_supports(F)
        if step>10 and len(set(a[-5:]))==1: break
    return
for a1 in [15,35,175,429,899,1147]:
    print('#'*70);print('a1=',a1,'p*=',min(P(a1)));probe(a1)
