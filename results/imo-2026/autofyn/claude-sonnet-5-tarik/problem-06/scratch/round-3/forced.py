import sys, time
from sim import gen

def forced_primes_growth(a1, M, checkpoints):
    terms, rads = gen(a1, M)
    forced = set()
    W = set()
    growth = {}
    ck_idx = 0
    checkpoints = sorted(checkpoints)
    t0 = time.time()
    for j in range(1, M):
        rj = rads[j]
        for i in range(j):
            inter = rads[i] & rj
            if not inter:
                continue
            w = min(inter)
            W.add(w)
            if len(inter) == 1:
                forced.add(w)
        # checkpoint after processing all pairs with second index <= j (i.e. all pairs among first j+1 terms)
        while ck_idx < len(checkpoints) and j + 1 == checkpoints[ck_idx]:
            growth[checkpoints[ck_idx]] = (len(forced), sorted(forced), len(W))
            ck_idx += 1
    print(f"a1={a1}: total elapsed {time.time()-t0:.1f}s", file=sys.stderr)
    return growth, forced, W

if __name__ == "__main__":
    a1 = int(sys.argv[1])
    M = int(sys.argv[2])
    checkpoints = [c for c in [50,100,200,400,600,800,1000,1500,2000,2500,3000,3500,4000] if c<=M]
    if M not in checkpoints:
        checkpoints.append(M)
    growth, forced, W = forced_primes_growth(a1, M, checkpoints)
    print(f"=== a1={a1} ===")
    for ck in sorted(growth):
        nforced, flist, nW = growth[ck]
        print(f"  M={ck}: #forced-primes={nforced}, #W(all witnesses)={nW}, forced={flist}")
