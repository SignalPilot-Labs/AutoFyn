import sys, time, json
sys.path.insert(0, '/tmp/round-6')
from driver import run_one

# Format: (a1, N, min_run)
specs = [
    # squarefree NON-LOCK pq baseline (small T expected)
    (15, 100, 30), (35, 400, 80), (77, 200, 40), (91, 200, 40), (143, 800, 200),
    (187, 800, 200), (209, 800, 200), (221, 800, 200), (247, 800, 200), (253, 1500, 400),
    (299, 1500, 400), (323, 1500, 400), (391, 1500, 400), (437, 2000, 500), (493, 2000, 500),
    (551, 2000, 500), (667, 2000, 500), (713, 2500, 600), (899, 3000, 800),
    # known reliable witnesses
    (741, 3000, 800), (1001, 4000, 1000), (105, 800, 200), (1309, 6000, 2000), (2431, 6000, 2000),
]
for a1,N,mr in specs:
    r = run_one(a1, N, mr)
    print(f"a1={r['a1']:6d} M1={r['M1']:5d} N={N:5d} T={str(r['T']):>5s} L={str(r['L']):>6s} govmax={str(r['gov_max']):>4s} {r['status']:>22s} fac={r.get('Lfac','-')}", flush=True)
