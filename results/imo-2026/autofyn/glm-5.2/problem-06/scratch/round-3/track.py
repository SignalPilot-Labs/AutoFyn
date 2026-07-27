"""Track candidate rank measures across M_n evolution for many seeds."""
from sim import simulate, P, minimal_supports, mtp_value, count_transversals_full, is_transversal
import json

def measure_family(Mn):
    """Compute all candidate measures on family Mn (frozenset of frozensets of primes)."""
    Mlist = [set(m) for m in Mn]
    Pess = set()
    for m in Mlist:
        Pess |= m
    num_minimals = len(Mlist)
    sum_sizes = sum(len(m) for m in Mlist)
    pess_size = len(Pess)
    prod_ess = 1
    for p in Pess:
        prod_ess *= p
    # mtp
    try:
        mtp = mtp_value(Pess, Mlist) if Pess else None
    except Exception:
        mtp = None
    # count of transversals (full 2^|Pess|)
    if pess_size <= 14:
        ntrans = count_transversals_full(Pess, Mlist)
    else:
        ntrans = None  # too big
    # avoiding transversals (transversals containing no member of Mn)
    # only compute if Pess small
    avoid = None
    if pess_size <= 14:
        Pl = sorted(Pess)
        av = 0
        for mask in range(1, 1<<len(Pl)):
            s = set()
            for i in range(len(Pl)):
                if mask & (1<<i):
                    s.add(Pl[i])
            if is_transversal(s, Mlist):
                if not any(set(m) <= s for m in Mlist):
                    av += 1
        avoid = av
    # common primes
    if Mlist:
        common = set(Mlist[0])
        for m in Mlist[1:]:
            common &= m
    else:
        common = set()
    return {
        'num_min': num_minimals,
        'sum_sizes': sum_sizes,
        'pess': pess_size,
        'prod_ess': prod_ess,
        'mtp': mtp,
        'ntrans': ntrans,
        'avoid': avoid,
        'common': len(common),
        'common_set': sorted(common),
    }

seeds = [15, 105, 175, 187, 221, 231, 385, 429, 1001, 323, 667, 21, 19549,
         33, 35, 39, 45, 51, 55, 57, 65, 69, 77, 85, 91, 93, 95, 273, 4199, 5005, 1043, 2465, 3255]

def run_seed(a1, Nmax=3000):
    seq, prom = simulate(a1, N=Nmax)
    print(f"\n=== a1={a1}  N_final={len(seq)}  num_promotions={len(prom)} ===")
    print(f"    final a_n={seq[-1]}")
    # track measures at each promotion
    rows = []
    for s, mn, an in prom:
        ms = measure_family(mn)
        rows.append((s, an, ms))
        print(f"  step {s:>4} a={an:>6} |M|={ms['num_min']} sum|M|={ms['sum_sizes']} |Pess|={ms['pess']} mtp={ms['mtp']} prod_ess={ms['prod_ess']} ntrans={ms['ntrans']} avoid={ms['avoid']} common={ms['common_set']}")
    # final stabilized family
    print(f"  FINAL M: {[set(x) for x in prom[-1][1]]}")
    # check monotonicity of each measure
    keys = ['num_min','sum_sizes','pess','prod_ess','mtp','ntrans','avoid']
    for k in keys:
        vals = [r[2][k] for r in rows if r[2][k] is not None]
        if len(vals) < 2:
            continue
        mono_inc = all(vals[i] <= vals[i+1] for i in range(len(vals)-1))
        mono_dec = all(vals[i] >= vals[i+1] for i in range(len(vals)-1))
        bounded = len(set(vals))
        flag = "MONO-INC" if mono_inc else ("MONO-DEC" if mono_dec else "NOT-MONO")
        print(f"    {k}: {flag}  distinct_vals={bounded}  trace={vals}")
    return rows

for a1 in seeds:
    try:
        run_seed(a1)
    except Exception as e:
        print(f"  a1={a1} ERROR: {e}")
