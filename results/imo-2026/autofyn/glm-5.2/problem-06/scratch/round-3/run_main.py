import math, sys
sys.path.insert(0, '/tmp/round-3')
from probe_fs import spf_table, factor, run, minimal_family_inc, all_transversals, mtp_of, common

N = 600000
spf = spf_table(N)

seeds = [15, 21, 105, 175, 187, 221, 231, 385, 429, 1001, 323, 667]

print("=== Q1+Q2: max_gap, mtp_final, entering primes vs a1 ===")
print(f"{'a1':>8} {'factors':>20} {'n_terms':>8} {'max_gap':>8} {'mtp_fin':>8} {'|M|':>4} {'|Pess|':>6} {'maxPess':>8} {'maxEnter':>8} {'C_final':>10} {'a1?':>6}")
rows = []
for a1 in seeds:
    r = run(a1, 1500, spf)
    mg = max(r['gaps']) if r['gaps'] else 0
    Pess = r['Pess_final']
    maxPess = max(Pess) if Pess else 0
    maxEnt = max(r['entering_total']) if r['entering_total'] else 0
    # mtp_final
    Pess_list = sorted(Pess)
    mtp_f = mtp_of(Pess_list, r['M_final']) if Pess_list else None
    Cf = sorted(r['C_final'])
    f = sorted(factor(a1, spf))
    print(f"{a1:>8} {str(f):>20} {r['n_terms']:>8} {mg:>8} {mtp_f:>8} {len(r['M_final']):>4} {len(Pess):>6} {maxPess:>8} {maxEnt:>8} {str(Cf):>10} {maxPess<=a1:>6}")
    rows.append((a1, f, r['n_terms'], mg, mtp_f, len(r['M_final']), len(Pess), maxPess, maxEnt, Cf, r))

# Q2 specifics: mtp_final vs a1, vs pmax(a1)^2
print("\n=== mtp_final vs a1, pmax, pmax^2 ===")
for a1, f, nt, mg, mtp_f, nM, nP, maxP, maxE, Cf, r in rows:
    pmax = max(f)
    print(f"a1={a1}: mtp_final={mtp_f}, a1={a1} (mtp<=a1? {mtp_f<=a1}), pmax={pmax} (mtp<=pmax? {mtp_f<=pmax}), pmax^2={pmax*pmax} (mtp<=pmax^2? {mtp_f<=pmax*pmax}), max_entering={maxE}")
    print(f"   entering primes: {sorted(r['entering_total'])}")
