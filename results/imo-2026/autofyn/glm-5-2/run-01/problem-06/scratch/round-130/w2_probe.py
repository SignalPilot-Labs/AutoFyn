"""W2 probe: for each seed a1 (odd, >=2 distinct prime factors, saturated regime),
generate the greedy gcd sequence, track M_n (minimal supports), and at every step
record:
  - mtp(M_n), witness T* (all minima), mtp-multiple mu_n
  - greedy pick a_{n+1}, gap, promotion? (new minimal enters)
  - equality vs strict-beat
  - smallest STRICT-BEAT candidate (smallest valid integer in (a_n, mu_n)) and its
    prime factors (this is what W2 is about: does it carry a prime <= p*?)
  - primes of a_{n+1}, min prime of a_{n+1}, p*
"""
import sys, math
from sympy import factorint, isprime, nextprime
from functools import lru_cache

def P(m):
    return set(factorint(m).keys())

def gen_sequence(a1, N):
    """Generate a_1..a_N (or until stabilized long enough)."""
    a=[a1]
    for _ in range(N-1):
        # find smallest m>a_n with gcd(m,a_i)>1 for all i<=n
        an=a[-1]
        m=an+1
        while True:
            if all(math.gcd(m,x)>1 for x in a):
                a.append(m); break
            m+=1
            if m> an+ 10**7:
                raise RuntimeError("too far")
    return a

def minimal_supports(F):
    """F = list of sets; return subset of inclusion-minimal sets."""
    M=[]
    for S in F:
        # keep S if no other T in F with T subset S
        keep=True
        for T in F:
            if T<S: keep=False; break
        if keep: M.append(S)
    # dedupe preserving distinct sets
    out=[]
    seen=[]
    for S in M:
        if S not in seen:
            seen.append(S); out.append(S)
    return out

def transversals(Pess, M):
    """All hitting sets (subsets of Pess) meeting every M. Full 2^|Pess| enumeration."""
    Pess=list(Pess)
    n=len(Pess)
    res=[]
    for mask in range(1,1<<n):
        T=set(Pess[i] for i in range(n) if mask&(1<<i))
        if all(T & S for S in M):
            res.append(T)
    return res

def mtp_and_witnesses(Pess,M):
    Ts=transversals(Pess,M)
    if not Ts: return None,None
    best=min(math.prod(T) for T in Ts)
    wits=[T for T in Ts if math.prod(T)==best]
    return best,wits

def smallest_valid_above(an, M):
    """smallest m>an with P(m) hitting every M in M (the admissible set)."""
    m=an+1
    while True:
        Pm=P(m)
        if all(Pm & S for S in M):
            return m
        m+=1
        if m>an+10**7: raise RuntimeError("far")

def probe(a1, Nsteps=60, maxPess=14):
    a=[a1]
    pstar=min(P(a1))
    F=[P(a1)]
    M=minimal_supports(F)
    rows=[]
    for step in range(1, Nsteps):
        an=a[-1]
        Pess=set()
        for S in M: Pess|=S
        if len(Pess)<=maxPess:
            mtp_val, wits = mtp_and_witnesses(Pess, M)
        else:
            mtp_val, wits = None, None
        if mtp_val:
            mu = ((an+1 + mtp_val-1)//mtp_val)*mtp_val  # smallest multiple of mtp > an... need strictly > an
            if mu<=an: mu+=mtp_val
            # smallest multiple strictly above an:
            mu = (an//mtp_val + 1)*mtp_val
            if mu<=an: mu+=mtp_val
        else:
            mu=None
        # greedy pick
        m=an+1
        while True:
            Pm=P(m)
            if all(Pm & S for S in M):
                break
            m+=1
            if m>an+10**6: raise RuntimeError
        anext=m
        # strict-beat candidate: smallest valid in (an, mu) if mu exists
        if mu:
            sb=an+1
            while sb<mu:
                Psb=P(sb)
                if all(Psb & S for S in M):
                    break
                sb+=1
            else:
                sb=None
        else:
            sb=None
        gap=anext-an
        is_equality = (mu is not None and anext==mu)
        is_strictbeat = (mu is not None and anext<mu)
        # promotion? new minimal?
        Panext=P(anext)
        # is Panext a new minimal? i.e. no M in M with M subset Panext, and Panext not already in M
        dominated = any(S<=Panext for S in M)
        is_promo = not dominated and (Panext not in M)
        # min prime of anext
        minp_anext=min(Panext)
        sb_minp = min(P(sb)) if sb else None
        # witness carries small prime?
        wit_small = None
        if wits:
            wit_small = any(any(p<=pstar for p in T) for T in wits)
        row=dict(step=step, an=an, anext=anext, gap=gap, mtp=mtp_val, mu=mu,
                 is_equality=is_equality, is_strictbeat=is_strictbeat,
                 is_promo=is_promo, Panext=sorted(Panext), minp_anext=minp_anext,
                 pstar=pstar, sb=sb, sb_primes=sorted(P(sb)) if sb else None,
                 sb_minp=sb_minp, wits=wits, wit_small=wit_small, nM=len(M),
                 Pess=sorted(Pess))
        rows.append(row)
        a.append(anext)
        F.append(Panext)
        M=minimal_supports(F)
        if step>10 and len(set(a[-5:]))==1: break
    return a, rows

if __name__=='__main__':
    for a1 in [15,35,175,429]:
        print('='*75)
        print('a1=',a1,'p*=',min(P(a1)))
        try:
            a,rows=probe(a1, Nsteps=80)
        except Exception as e:
            print('ERR',e); continue
        # show promotions only, focus on strict-beat
        promos=[r for r in rows if r['is_promo']]
        print(f'#steps generated={len(rows)}, #promotions={len(promos)}')
        # strict-beat promotions
        sbs=[r for r in promos if r['is_strictbeat']]
        eqs=[r for r in promos if r['is_equality']]
        print(f'  equality-promos={len(eqs)}, strict-beat-promos={len(sbs)}')
        # W2 check on strict-beat promotions
        w2viol=[r for r in sbs if r['minp_anext']>r['pstar']]
        print(f'  W2 violations (strict-beat promo with minP(a_next)>p*): {len(w2viol)}')
        # examine the strict-beat candidate (smallest valid below mu) vs a_next
        print('  --- strict-beat promotions detail ---')
        for r in sbs[:25]:
            print(f"  step{r['step']}: a_n={r['an']} a_next={r['anext']} mu={r['mu']} "
                  f"sb_cand={r['sb']} sb_primes={r['sb_primes']} sb_minp={r['sb_minp']} "
                  f"P(a_next)={r['Panext']} minp={r['minp_anext']} p*={r['pstar']} "
                  f"wit_small={r['wit_small']}")
        # also: is a_next always == sb candidate when strict-beat? (should be by definition of greedy)
        agree=sum(1 for r in sbs if r['sb']==r['anext'])
        print(f'  (sb_cand==a_next in {agree}/{len(sbs)} strict-beat promos)')
