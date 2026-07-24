import sys, time

def sieve_primes(limit):
    is_c = bytearray(limit+1)
    primes = []
    for i in range(2, limit+1):
        if not is_c[i]:
            primes.append(i)
            for j in range(i*i, limit+1, i):
                is_c[j] = 1
    return primes

def factor(m, primes):
    f = set()
    x = m
    for p in primes:
        if p*p > x:
            break
        while x % p == 0:
            f.add(p)
            x //= p
    if x > 1:
        f.add(x)
    return frozenset(f)

def run(a1, N, prime_limit=20000):
    primes = sieve_primes(prime_limit)
    P1 = factor(a1, primes)

    a = a1
    rad1 = factor(a1, primes)
    antichain = [rad1]

    # store companion (rad - core) for members of the two tracked cores
    S_target  = frozenset({103,197})
    Sp_target = frozenset({1061})
    S_members  = []   # (index, companion_frozenset)
    Sp_members = []

    t0 = time.time()
    n = 1
    while n < N:
        cand = a + 1
        while True:
            ok = True
            for C in antichain:
                if not any(cand % p == 0 for p in C):
                    ok = False
                    break
            if ok:
                break
            cand += 1
        a = cand
        n += 1
        rad = factor(a, primes)
        dominated_by_rad = any(C < rad for C in antichain)
        if not dominated_by_rad:
            antichain = [C for C in antichain if not (rad < C)]
            if rad not in antichain:
                antichain.append(rad)

        core = rad & P1
        if core == S_target:
            S_members.append((n, rad - core))
        elif core == Sp_target:
            Sp_members.append((n, rad - core))

        if n % 200000 == 0:
            print(f"n={n} a_n={a} elapsed={time.time()-t0:.1f}s |I_S|={len(S_members)} |I_S'|={len(Sp_members)}")

    return S_members, Sp_members

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--a1", type=int, default=21528751)
    ap.add_argument("--N", type=int, default=1000000)
    args = ap.parse_args()

    S_members, Sp_members = run(args.a1, args.N)
    print("Total |I_S|=", len(S_members), " |I_S'|=", len(Sp_members))

    W = {2,3,5,7,11,97}
    # check every member's companion intersects W
    bad_S  = [(i,c) for i,c in S_members if not (c & W)]
    bad_Sp = [(i,c) for i,c in Sp_members if not (c & W)]
    print("members of S with companion disjoint from W:", len(bad_S), bad_S[:5])
    print("members of S' with companion disjoint from W:", len(bad_Sp), bad_Sp[:5])

    # direct full cross check (companion intersection) -- may be O(|S|*|S'|); guard size
    print("Doing full cross-pair companion-intersection check...")
    Sp_companions = [c for i,c in Sp_members]
    bad_pairs = 0
    checked = 0
    first_bad = None
    for i, c in S_members:
        for j, c2 in Sp_members:
            checked += 1
            if not (c & c2):
                bad_pairs += 1
                if first_bad is None:
                    first_bad = (i, c, j, c2)
    print(f"checked {checked} cross pairs, bad (no shared companion prime): {bad_pairs}")
    if first_bad:
        print("first bad pair:", first_bad)

    # report freeze / min companion index details
    print("First 10 S members:", S_members[:10])
    print("First 10 S' members:", Sp_members[:10])
