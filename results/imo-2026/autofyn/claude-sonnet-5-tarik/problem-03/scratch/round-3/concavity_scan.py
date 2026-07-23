import random
exec(open('/tmp/round-3/concavity_test.py').read().split("# sanity")[0])  # reuse functions

def random_simplex_pt(rng):
    while True:
        x,y = rng.random(), rng.random()
        if x>y: x,y = y,x
        a1,a2,a3 = 1-y, y-x, x
        if a1>=a2>=a3>=0:
            return (a1,a2,a3)

rng = random.Random(42)
violations = 0
trials = 25
for i in range(trials):
    p1 = random_simplex_pt(rng)
    p2 = random_simplex_pt(rng)
    mid = tuple((p1[j]+p2[j])/2 for j in range(3))
    mid = tuple(sorted(mid, reverse=True))
    g1 = g_numeric(*p1, ntrials=40000, seed=1000+i)
    g2 = g_numeric(*p2, ntrials=40000, seed=2000+i)
    gm = g_numeric(*mid, ntrials=40000, seed=3000+i)
    avg=(g1+g2)/2
    ok = gm >= avg - 3e-3
    if not ok:
        violations += 1
    print(f"{i}: p1={tuple(round(v,3) for v in p1)} p2={tuple(round(v,3) for v in p2)} g1={g1:.4f} g2={g2:.4f} avg={avg:.4f} gmid={gm:.4f} {'OK' if ok else 'VIOLATION'}")
print("violations:", violations, "/", trials)

print("\n--- targeted boundary-crossing tests ---")
# crossing a1=2a2 boundary near the dyadic pt but staying at fixed a3
test_concavity((0.65,0.325,0.025+0.0), (0.5,0.25,0.25), ntrials=80000, label="cross a1=2a2 boundary far from dyadic")
test_concavity((0.6,0.3,0.1), (0.56,0.28,0.16), ntrials=80000, label="near a1=2a2, both sides")
# near a3=0 boundary (degenerate, fewer pieces)
test_concavity((0.9,0.1,0.0), (0.5,0.3,0.2), ntrials=80000, label="near-degenerate a3=0 vs interior")
# crossing a2=2a3
test_concavity((0.5,0.34,0.16), (0.5,0.30,0.20), ntrials=80000, label="cross a2=2a3 at fixed a1")
