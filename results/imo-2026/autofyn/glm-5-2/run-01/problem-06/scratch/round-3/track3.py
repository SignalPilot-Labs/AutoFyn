"""Faster greedy using residue/mtp-cap candidate scan + more measures including trace family."""
import sys
from itertools import combinations
from sympy import factorint

def P(m):
    return frozenset(factorint(m).keys())

def is_transversal(T, family):
    Ts = set(T)
    return all(Ts & set(M) for M in family)

def mtp_and_witness(Pess, family):
    """Return (mtp_value, witness set) via full subset enum."""
    Pl = sorted(Pess); n = len(Pl); best = None; bestset = None
    for mask in range(1, 1<<n):
        s = set()
        for i in range(n):
            if mask & (1<<i): s.add(Pl[i])
        if is_transversal(s, family):
            prod = 1
            for p in s: prod *= p
            if best is None or prod < best:
                best = prod; bestset = frozenset(s)
    return best, bestset

def minimal_supports(fam_list):
    fam = list(set(fam_list))
    return frozenset(S for S in fam if not any(T < S for T in fam))

def greedy_next(an, Mn, mtpval, cap=20000):
    """Find smallest m>an with P(m) hitting every M in Mn. Upper bound an+mtpval."""
    m = an + 1
    hi = an + mtpval  # multiples of mtp-witness are valid -> guaranteed <= an+mtpval
    while m <= hi + 0:
        pm = P(m)
        if all(set(pm) & set(M) for M in Mn):
            return m
        m += 1
        if m - an > cap:
            return None
    return m

def simulate_fast(a1, Nmax=2000, cap=20000):
    seq = [a1]; fam_list = [P(a1)]
    Mn = minimal_supports(fam_list)
    Pess = set()
    for m in Mn: Pess |= set(m)
    mtpval, wit = mtp_and_witness(Pess, [set(m) for m in Mn])
    prom = [(1, Mn, a1, mtpval, wit)]
    for step in range(2, Nmax+1):
        an = seq[-1]
        m = greedy_next(an, Mn, mtpval, cap)
        if m is None:
            break
        seq.append(m); fam_list.append(P(m))
        new_Mn = minimal_supports(fam_list)
        if new_Mn != Mn:
            newPess = set()
            for mm in new_Mn: newPess |= set(mm)
            newmtp, newwit = mtp_and_witness(newPess, [set(mm) for mm in new_Mn])
            prom.append((step, new_Mn, m, newmtp, newwit)); Mn = new_Mn; mtpval = newmtp; wit = newwit
    return seq, prom

def measure_family(Mn, wit):
    Mlist = [set(m) for m in Mn]
    Pess = set();
    for m in Mlist: Pess |= m
    num_min = len(Mlist); sum_sizes = sum(len(m) for m in Mlist); pess = len(Pess)
    mtp, _ = mtp_and_witness(Pess, Mlist) if Pess else (None, None)
    # minimal transversals (inclusion-minimal hitting sets) -- only if pess small
    mintrans = None
    if pess <= 14:
        Pl = sorted(Pess); n = len(Pl)
        cand = []
        for mask in range(1, 1<<n):
            s = set()
            for i in range(n):
                if mask & (1<<i): s.add(Pl[i])
            if is_transversal(s, Mlist): cand.append(frozenset(s))
        # minimal under inclusion
        mintrans = sum(1 for s in cand if not any(t < s for t in cand))
    # avoid count
    avoid = None
    if pess <= 14:
        Pl = sorted(Pess); av = 0
        for mask in range(1, 1<<len(Pl)):
            s = set()
            for i in range(len(Pl)):
                if mask & (1<<i): s.add(Pl[i])
            if is_transversal(s, Mlist) and not any(set(m) <= s for m in Mlist):
                av += 1
        avoid = av
    # trace family wrt witness wit
    trace_fam = frozenset(frozenset(set(m) & set(wit)) for m in Mlist) if wit else None
    trace_cnt = len(trace_fam) if trace_fam is not None else None
    common = set(Mlist[0]) if Mlist else set()
    for m in Mlist[1:]: common &= m
    return dict(num_min=num_min, sum_sizes=sum_sizes, pess=pess, mtp=mtp,
                mintrans=mintrans, avoid=avoid, trace_cnt=trace_cnt, trace_fam=trace_fam,
                common=sorted(common), wit=sorted(wit) if wit else None)

def run_seed(a1, Nmax=2000):
    seq, prom = simulate_fast(a1, Nmax)
    print(f"\n=== a1={a1}  N_final={len(seq)}  num_promotions={len(prom)} ===")
    rows = []
    for s, mn, an, mtpval, wit in prom:
        ms = measure_family(mn, wit)
        rows.append((s, an, ms))
        print(f"  st {s:>4} a={an:>7} |M|={ms['num_min']} sum|M|={ms['sum_sizes']} |Pess|={ms['pess']} mtp={ms['mtp']} mintrans={ms['mintrans']} avoid={ms['avoid']} trace#={ms['trace_cnt']} wit={ms['wit']} common={ms['common']}")
    print(f"  FINAL M: {[set(x) for x in prom[-1][1]]}")
    keys = ['num_min','sum_sizes','pess','mtp','mintrans','avoid','trace_cnt']
    for k in keys:
        vals = [r[2][k] for r in rows if r[2][k] is not None]
        if len(vals) < 2: continue
        mi = all(vals[i] <= vals[i+1] for i in range(len(vals)-1))
        md = all(vals[i] >= vals[i+1] for i in range(len(vals)-1))
        flag = "MONO-INC" if mi else ("MONO-DEC" if md else "NOT-MONO")
        print(f"    {k}: {flag}  distinct={len(set(vals))}  trace={vals}")
    return rows

if __name__ == '__main__':
    a1 = int(sys.argv[1])
    N = int(sys.argv[2]) if len(sys.argv) > 2 else 2000
    run_seed(a1, N)
