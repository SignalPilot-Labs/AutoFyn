import sys, time
from sim import gen

def test_H_sufficiency(a1, M, H, report_every=2000):
    terms, rads = gen(a1, M)
    H = set(H)
    failures = []
    t0 = time.time()
    for j in range(1, M):
        rj = rads[j]
        rjH = rj & H
        if not rjH:
            continue  # no chance any pair (i,j) can be covered by H via j's own H-primes... still need i side
        for i in range(j):
            if not (rads[i] & rjH):
                failures.append((i, j, sorted(rads[i]), sorted(rj)))
                if len(failures) >= 20:
                    return failures, time.time()-t0
    return failures, time.time()-t0

if __name__ == "__main__":
    a1 = int(sys.argv[1])
    M = int(sys.argv[2])
    H = set(int(x) for x in sys.argv[3].split(","))
    failures, elapsed = test_H_sufficiency(a1, M, H)
    print(f"a1={a1}, M={M}, H={sorted(H)}: elapsed={elapsed:.1f}s, #failures found={len(failures)}")
    for f in failures[:10]:
        print("  FAIL:", f)
