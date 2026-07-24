import math, time

def factorize(n, cache={}):
    if n in cache:
        return cache[n]
    orig = n
    fac = set()
    d = 2
    while d*d <= n:
        if n % d == 0:
            fac.add(d)
            while n % d == 0:
                n //= d
        d += 1 if d==2 else 2
    if n > 1:
        fac.add(n)
    cache[orig] = fac
    return fac

def gen_sequence(a1, N):
    a = [a1]
    primes_list = [factorize(a1)]
    while len(a) < N:
        an = a[-1]
        c = an + 1
        while True:
            ok = True
            pc = factorize(c)
            for pf in primes_list:
                if pc.isdisjoint(pf):
                    ok = False
                    break
            if ok:
                a.append(c)
                primes_list.append(pc)
                break
            c += 1
    return a, primes_list

def extended_persistent_types_and_N(primes_list, S, tail_frac=0.3, min_count=5):
    # ρ(n) = P(a_n) ∩ S for n=1..len
    N = len(primes_list)
    rho = [frozenset(pf & S) for pf in primes_list]
    tail_start = int(N*(1-tail_frac))
    from collections import Counter
    cnt = Counter(rho[tail_start:])
    # persistent types = those appearing in tail with count >= min_count (proxy for "infinitely often")
    persistent = set(t for t,c in cnt.items() if c >= min_count)
    if not persistent:
        # fallback: most common type
        persistent = set([cnt.most_common(1)[0][0]]) if cnt else set()
    # N(S) proxy = last index (1-based) where rho[n] not in persistent
    Nthresh = 0
    for i in range(N-1, -1, -1):
        if rho[i] not in persistent:
            Nthresh = i+1
            break
    return persistent, Nthresh

def absorb(primes_list, S, Nthresh):
    Snew = set(S)
    for j in range(Nthresh):  # j=0..Nthresh-1 corresponds to a_1..a_Nthresh
        Snew |= primes_list[j]
    return Snew

def run(a1, N, rounds=5, tail_frac=0.3, min_count=8):
    print(f"=== a1={a1}, N={N} terms ===")
    a, primes_list = gen_sequence(a1, N)
    Q = factorize(a1)
    S = set(Q)
    for k in range(rounds):
        persistent, Nthresh = extended_persistent_types_and_N(primes_list, S, tail_frac, min_count)
        print(f" round {k}: |S|={len(S)} S={sorted(S)[:15]}{'...' if len(S)>15 else ''}  N(S)proxy={Nthresh}  #persistent_types={len(persistent)}")
        Snew = absorb(primes_list, S, Nthresh)
        if Snew == S:
            print(f"  -> FIXED POINT reached at round {k} (self-absorbing), |S*|={len(S)}")
            break
        S = Snew
    else:
        print("  -> did not visibly reach fixed point within rounds budget")

t0=time.time()
run(175, 4000, rounds=6)
run(4807, 4000, rounds=6)
run(11305, 4000, rounds=6)
run(35, 3000, rounds=6)
print("elapsed", time.time()-t0)

print("\n=== bigger sample for 4807/11305 ===")
run(4807, 15000, rounds=4, tail_frac=0.2, min_count=15)
run(11305, 15000, rounds=4, tail_frac=0.2, min_count=15)
