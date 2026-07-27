"""
Probe smallest-first dynamics of IMO 2026 P6 greedy sequence.

a_{n+1} = min{m>a_n : gcd(m,a_i)>1 for all i<=n}
Track:
  M_n   = inclusion-minimal members of {P(a_1),...,P(a_n)}
  P_ess,n = union of M_n
  C_n   = intersection of M_n (common primes)
  mtp(M_n) = min over transversals T of prod_{p in T} p
  Entering essential primes (the primes that newly enter P_ess at a promotion)
  Largest entering prime vs a_1, vs mtp_final

Correct transversal enumeration = full 2^|P_ess| subset check.
"""
import math
from itertools import combinations

def primes(n):
    s=set()
    d=2
    while d*d<=n:
        while n%d==0:
            s.add(d); n//=d
        d+=1
    if n>1: s.add(n)
    return s

def minimal_family(family):
    """family: list of frozensets of primes. Return inclusion-minimal members as sorted list of frozensets."""
    fam=list(dict.fromkeys(family))  # dedupe
    res=[]
    for S in fam:
        if not any(other < S for other in fam if other != S):
            # S is minimal: no other is a proper subset
            res.append(S)
    # proper minimal: S minimal iff no T in fam with T < S (proper subset)
    res=[]
    for S in fam:
        is_min = True
        for T in fam:
            if T < S:  # proper subset
                is_min=False; break
        if is_min: res.append(S)
    return sorted(res, key=lambda s:(len(s),sorted(s)))

def transversals(Pess, M):
    """Enumerate all transversals (hitting sets) of M using subsets of Pess. Return list of frozensets."""
    Pess=list(Pess)
    res=[]
    n=len(Pess)
    for k in range(1,n+1):
        for combo in combinations(range(n),k):
            T=frozenset(Pess[i] for i in combo)
            if all(T & M for M in M):
                res.append(T)
    return res

def mtp(Pess, M):
    Pess=list(Pess)
    best=None; bestT=None
    n=len(Pess)
    for k in range(1,n+1):
        for combo in combinations(range(n),k):
            T=frozenset(Pess[i] for i in combo)
            if all(T & Mm for Mm in M):
                prod=1
                for p in T: prod*=p
                if best is None or prod<best:
                    best=prod; bestT=T
        if best is not None and k>0:
            # can't early break easily (smaller card doesn't mean smaller product), but for speed once we have min over all of card k, larger cards only help if they include a small prime... we still must check. Keep simple.
            pass
    return best, bestT

def common_primes(M):
    if not M: return set()
    c=set(M[0])
    for s in M[1:]: c&=s
    return c

def run(a1, Nmax=20000, verbose=False, track_promos=True):
    """Generate greedy sequence up to Nmax terms or until M stabilizes for STABLE_WINDOW consecutive steps."""
    a=[a1]
    Pfam=[frozenset(primes(a1))]
    M=minimal_family(Pfam)
    Pess=set(Pfam[0])
    entering_log=[]  # (step_index, new_minimal, primes_entered)
    stable_window=200
    last_M_repr=None
    stable_count=0
    mtp_prev=None
    entering_primes_total=set()
    for n in range(1, Nmax):
        # find smallest m > a[-1] with P(m) hitting all M
        # brute force m upward
        m=a[-1]+1
        # current M:
        while True:
            Pm=primes(m)
            # is Pm a transversal? hits every Mm in M?
            if all(Pm & Mm for Mm in M):
                break
            m+=1
        a.append(m)
        Pfam.append(frozenset(primes(m)))
        # update M
        new_Pm=frozenset(primes(m))
        old_M=set(M)
        # new minimal family
        oldM=M
        # recompute minimal of Pfam (could be slow if Pfam huge; but we track incrementally)
        # incremental: a set is removed if new_Pm is a proper subset; new_Pm is minimal if no existing is subset of it
        is_new_minimal = True
        removed=[]
        new_M=[]
        for S in oldM:
            if new_Pm < S:  # new_Pm proper subset of S -> S removed
                removed.append(S); continue
            if S < new_Pm or S==new_Pm:  # S proper subset of new_Pm -> new_Pm not minimal
                is_new_minimal=False
                new_M.append(S); continue
            new_M.append(S)
        if is_new_minimal and not any(S==new_Pm for S in new_M):
            new_M.append(new_Pm)
        new_M=sorted(new_M, key=lambda s:(len(s),sorted(s)))
        promotion = (is_new_minimal and new_Pm not in oldM) or len(removed)>0
        if promotion:
            entered = set(new_Pm) - Pess
            if entered:
                entering_log.append((n, frozenset(new_Pm), frozenset(entered)))
                entering_primes_total |= entered
            Pess = set()
            for S in new_M: Pess|=set(S)
        else:
            # Pess unchanged unless removals (but removals imply promotion above)
            pass
        M=new_M
        # stability check
        reprM=tuple(sorted([tuple(sorted(s)) for s in M]))
        if reprM==last_M_repr:
            stable_count+=1
        else:
            stable_count=0; last_M_repr=reprM
        if stable_count>=stable_window:
            break
    return {
        'a1':a1, 'a':a, 'M_final':M, 'Pess_final':set().union(*M) if M else set(),
        'entering_log':entering_log, 'entering_primes_total':entering_primes_total,
        'C_final':common_primes(M), 'n_terms':len(a),
    }

def mtp_final(M):
    Pess=set().union(*M) if M else set()
    if not Pess: return None,None
    best,bestT=mtp(list(Pess), [set(s) for s in M])
    return best,bestT

if __name__=='__main__':
    import sys
    seeds=[15,21,105,175,187,221,231,385,429,1001,19549,323,667,113*173,23*89,17*19*23]
    for s in seeds:
        r=run(s, Nmax=5000)
        Mf=r['M_final']
        Pess=r['Pess_final']
        m,bt=mtp_final(Mf)
        print(f"a1={s} ({primes(s)}): n_terms={r['n_terms']}, |M_final|={len(Mf)}, Pess_final={sorted(Pess)}, max_entering_prime={max(r['entering_primes_total']) if r['entering_primes_total'] else None}, mtp_final={m}, C_final={r['C_final']}")
        # max prime in Pess vs a1
        maxp=max(Pess) if Pess else None
        print(f"   max(Pess)={maxp}, a1={s}, max(Pess)<=a1? {maxp<=s if maxp else None}; entering primes: {sorted(r['entering_primes_total'])}")
        print(f"   entering_log (step, new_minimal, entered):")
        for step,nm,ent in r['entering_log']:
            print(f"      n={step}: new_min={sorted(nm)} entered={sorted(ent)}")
