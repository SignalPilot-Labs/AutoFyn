"""Track candidate rank measures across M_n evolution for many seeds. Optimized + per-seed."""
import sys
from itertools import combinations
from sympy import factorint

def P(m):
    return frozenset(factorint(m).keys())

def is_transversal(T, family):
    Ts = set(T)
    return all(Ts & set(M) for M in family)

def count_transversals_full(Pess, family):
    Pl = sorted(Pess); n = len(Pl); cnt = 0
    for mask in range(1, 1<<n):
        s = set()
        for i in range(n):
            if mask & (1<<i): s.add(Pl[i])
        if is_transversal(s, family): cnt += 1
    return cnt

def mtp_value(Pess, family):
    Pl = sorted(Pess); n = len(Pl); best = None
    for mask in range(1, 1<<n):
        s = set()
        for i in range(n):
            if mask & (1<<i): s.add(Pl[i])
        if is_transversal(s, family):
            prod = 1
            for p in s: prod *= p
            if best is None or prod < best: best = prod
    return best

def minimal_supports(fam_list):
    fam = list(set(fam_list))
    minimals = [S for S in fam if not any(T < S for T in fam)]
    return frozenset(minimals)

def simulate_track(a1, Nmax=1500):
    seq = [a1]; fam_list = [P(a1)]
    Mn = minimal_supports(fam_list)
    prom = [(1, Mn, a1)]
    for step in range(2, Nmax+1):
        an = seq[-1]
        # need to find next valid. Upper bound: smallest multiple of mtp-witness.
        # just scan up to an+2000 (cap)
        m = an + 1
        while True:
            pm = P(m)
            if all(set(pm) & set(M) for M in Mn):
                break
            m += 1
            if m - an > 5000:
                break
        seq.append(m); fam_list.append(P(m))
        new_Mn = minimal_supports(fam_list)
        if new_Mn != Mn:
            prom.append((step, new_Mn, m)); Mn = new_Mn
    return seq, prom

def measure_family(Mn):
    Mlist = [set(m) for m in Mn]
    Pess = set();
    for m in Mlist: Pess |= m
    num_min = len(Mlist); sum_sizes = sum(len(m) for m in Mlist); pess = len(Pess)
    prod_ess = 1
    for p in Pess: prod_ess *= p
    mtp = mtp_value(Pess, Mlist) if Pess else None
    if pess <= 14:
        ntrans = count_transversals_full(Pess, Mlist)
    else:
        ntrans = None
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
    common = set(Mlist[0]) if Mlist else set()
    for m in Mlist[1:]: common &= m
    return dict(num_min=num_min, sum_sizes=sum_sizes, pess=pess, prod_ess=prod_ess,
                mtp=mtp, ntrans=ntrans, avoid=avoid, common=sorted(common))

def run_seed(a1, Nmax=1500):
    seq, prom = simulate_track(a1, Nmax)
    print(f"\n=== a1={a1}  N_final={len(seq)}  num_promotions={len(prom)} ===")
    rows = []
    for s, mn, an in prom:
        ms = measure_family(mn)
        rows.append((s, an, ms))
        print(f"  step {s:>4} a={an:>6} |M|={ms['num_min']} sum|M|={ms['sum_sizes']} |Pess|={ms['pess']} mtp={ms['mtp']} prod_ess={ms['prod_ess']} ntrans={ms['ntrans']} avoid={ms['avoid']} common={ms['common']}")
    print(f"  FINAL M: {[set(x) for x in prom[-1][1]]}")
    keys = ['num_min','sum_sizes','pess','prod_ess','mtp','ntrans','avoid']
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
    N = int(sys.argv[2]) if len(sys.argv) > 2 else 1500
    run_seed(a1, N)
