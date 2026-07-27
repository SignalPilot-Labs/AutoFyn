import math, sys
sys.path.insert(0, '/tmp/round-3')
from probe_fs import spf_table, factor, run, minimal_family_inc, mtp_of, common

N = 300000
spf = spf_table(N)

# Broad scan: odd a1 with >=2 distinct prime factors, a1 <= 1000ish.
# Find max(mtp_final), max(mtp_final/a1), extremal seeds.
print("=== Broad scan: mtp_final vs a1 (odd, >=2 distinct primes) ===")
results = []
primes_list = [3,5,7,11,13,17,19,23,29,31]
# semiprimes and 3-products (curated)
import itertools
a1s = set()
for p,q in itertools.combinations(primes_list,2):
    a1s.add(p*q)
for p,q in itertools.combinations(primes_list[:7],2):
    if p<q: a1s.add(p*p*q)
for p,q,r in itertools.combinations(primes_list[:7],3):
    a1s.add(p*q*r)
# also add the requested extremal-style
for a1 in [19549, 4199, 5005, 113*173, 23*89, 17*19*23, 7*73, 7*97, 11*97, 13*97, 3*97, 5*97]:
    if a1 < N: a1s.add(a1)

a1s = sorted(x for x in a1s if x >= 2 and x < 200000)
print(f"scanning {len(a1s)} seeds...")

max_ratio = 0; max_ratio_seed = None
max_mtp = 0; max_mtp_seed = None
ratios_le1 = 0; ratios_gt1 = 0
extremals = []
for a1 in a1s:
    f = factor(a1, spf)
    if a1 % 2 == 0:  # even -> freeze, skip
        continue
    if len(f) < 2:  # single prime power -> freeze
        continue
    r = run(a1, 250, spf, stable_window=50)
    Pess = r['Pess_final']
    if not Pess: continue
    mtp_f = mtp_of(sorted(Pess), r['M_final'])
    if mtp_f is None: continue
    mg = max(r['gaps']) if r['gaps'] else 0
    ratio = mtp_f / a1
    if ratio > max_ratio:
        max_ratio = ratio; max_ratio_seed = a1
    if mtp_f > max_mtp:
        max_mtp = mtp_f; max_mtp_seed = a1
    if mtp_f <= a1: ratios_le1 += 1
    else: ratios_gt1 += 1
    if ratio > 0.3 or mtp_f > 40:
        extremals.append((a1, sorted(f), mtp_f, mg, len(r['M_final']), sorted(Pess), max(r['entering_total']) if r['entering_total'] else 0, ratio))

print(f"\nSummary over scanned seeds:")
print(f"  max(mtp_final/a1) = {max_ratio:.4f} at a1={max_ratio_seed}")
print(f"  max(mtp_final) = {max_mtp} at a1={max_mtp_seed}")
print(f"  #seeds with mtp<=a1: {ratios_le1}, mtp>a1: {ratios_gt1}")
print(f"\nExtremals (ratio>0.3 or mtp>40):")
print(f"{'a1':>8} {'factors':>22} {'mtp':>5} {'maxgap':>6} {'|M|':>3} {'Pess_final':>20} {'maxEnter':>8} {'ratio':>6}")
for a1,f,mtp,mg,nM,Pess,maxE,ratio in sorted(extremals, key=lambda x:-x[7]):
    print(f"{a1:>8} {str(f):>22} {mtp:>5} {mg:>6} {nM:>3} {str(Pess):>20} {maxE:>8} {ratio:>6.3f}")
