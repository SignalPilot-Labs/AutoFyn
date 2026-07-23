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

def run(a1, N, prime_limit=20000, report_every=50000, log=None):
    primes = sieve_primes(prime_limit)
    P1 = factor(a1, primes)
    assert len(P1) >= 2, f"a1={a1} P1={P1} not multi-prime top core"

    a = a1
    seq = [a1]
    rad1 = factor(a1, primes)
    # global minimal-radical antichain (list of frozensets)
    antichain = [rad1]

    # per-core local antichains: dict core(frozenset) -> list of frozensets (local antichain)
    local_antichain = {}
    # track history of local antichain "signature" (frozenset of frozensets) changes: last-changed n, count of changes
    local_last_change_n = {}
    local_change_count = {}
    local_history_sizes = {}  # core -> list of (n, size) whenever size changes (sampled sparsely)

    core1 = rad1 & P1
    if core1 and core1 != P1:
        local_antichain[core1] = [rad1]
        local_last_change_n[core1] = 1
        local_change_count[core1] = 1

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
        seq_last = rad
        # update global antichain: remove dominated (rad subset of existing -> those existing removed), add rad if not superset of any existing
        # rad is guaranteed to intersect every antichain elt (by construction), so rad could be a superset of some, equal, or incomparable
        dominated_by_rad = [C for C in antichain if C < rad]  # existing strict subset of rad -> rad is dominated, don't add
        if dominated_by_rad:
            pass  # rad is a (non-strict?) superset of an existing minimal elt -> not added
        else:
            # remove any existing elt that is a strict superset of rad
            antichain = [C for C in antichain if not (rad < C)]
            if rad not in antichain:
                antichain.append(rad)

        core = rad & P1
        if core and core != P1:  # proper core (nonempty proper subset)
            la = local_antichain.get(core)
            if la is None:
                local_antichain[core] = [rad]
                local_last_change_n[core] = n
                local_change_count[core] = 1
            else:
                dom = [C for C in la if C < rad]
                if not dom:
                    new_la = [C for C in la if not (rad < C)]
                    if rad not in new_la:
                        new_la.append(rad)
                    if new_la != la:
                        local_antichain[core] = new_la
                        local_last_change_n[core] = n
                        local_change_count[core] = local_change_count.get(core,0) + 1

        if n % report_every == 0:
            elapsed = time.time() - t0
            msg = f"n={n} a_n={a} elapsed={elapsed:.1f}s antichain_size={len(antichain)}"
            print(msg)
            if log:
                log.write(msg + "\n")
                log.flush()

    return {
        "P1": P1,
        "local_antichain": local_antichain,
        "local_last_change_n": local_last_change_n,
        "local_change_count": local_change_count,
        "final_n": n,
        "final_a": a,
        "global_antichain": antichain,
    }

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--a1", type=int, default=21528751)
    ap.add_argument("--N", type=int, default=1000000)
    ap.add_argument("--prime_limit", type=int, default=20000)
    ap.add_argument("--out", type=str, default=None)
    args = ap.parse_args()

    logf = open(args.out, "w") if args.out else None
    res = run(args.a1, args.N, prime_limit=args.prime_limit, log=logf)
    print("=== FINAL ===")
    print("P1=", res["P1"])
    for core, la in sorted(res["local_antichain"].items(), key=lambda x: -len(x[0])):
        print(f"core={set(core)} size(local_antichain)={len(la)} last_change_n={res['local_last_change_n'][core]} change_count={res['local_change_count'][core]}")
        for C in la:
            print("   ", sorted(C))
    if logf:
        logf.write("=== FINAL ===\n")
        logf.write(f"P1={res['P1']}\n")
        for core, la in sorted(res["local_antichain"].items(), key=lambda x: -len(x[0])):
            logf.write(f"core={set(core)} size={len(la)} last_change_n={res['local_last_change_n'][core]} change_count={res['local_change_count'][core]}\n")
            for C in la:
                logf.write("   " + str(sorted(C)) + "\n")
        logf.close()
