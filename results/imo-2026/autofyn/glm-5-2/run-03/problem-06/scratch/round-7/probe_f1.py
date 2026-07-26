import sys, math
sys.path.insert(0, '/tmp/round-6')
from mt_greedy import sieve_primes, prime_factors, rad, add_set_to_MT, prune_minimal

def greedy_mt_tracked(a1, N, small_primes):
    a = [0]*N
    a[0] = a1
    P0 = prime_factors(a1, small_primes)
    MT = prune_minimal([{p} for p in P0])
    stats = []
    mt_primes = set()
    for t in MT:
        mt_primes |= set(t)
    stats.append({
        'n':0, 'a':a1, 'mt_size':len(MT), 'mt_primes':sorted(mt_primes),
        'sum_1_over_q':sum(1/q for q in mt_primes),
        'sum_abs_T':sum(len(t) for t in MT),
        'max_T_len':max(len(t) for t in MT) if MT else 0,
        'mt_primes_count':len(mt_primes),
        'mt_primes_gt_M1':sorted(q for q in mt_primes if q > rad(a1)),
    })
    for step in range(1, N):
        prev = a[step-1]
        m = prev+1
        while True:
            Pm = prime_factors(m, small_primes)
            ok = any(t <= Pm for t in MT)
            if ok: break
            m += 1
        a[step] = m
        S_new = prime_factors(m, small_primes)
        MT = add_set_to_MT(MT, S_new)
        mt_primes = set()
        for t in MT: mt_primes |= set(t)
        stats.append({
            'n':step, 'a':m, 'mt_size':len(MT), 'mt_primes':sorted(mt_primes),
            'sum_1_over_q':sum(1/q for q in mt_primes),
            'sum_abs_T':sum(len(t) for t in MT),
            'max_T_len':max(len(t) for t in MT) if MT else 0,
            'mt_primes_count':len(mt_primes),
            'mt_primes_gt_M1':sorted(q for q in mt_primes if q > rad(a1)),
        })
    return a, stats

# First verify small cases with naive greedy
def naive_greedy(a1, N):
    a=[0]*N; a[0]=a1
    for i in range(1,N):
        m=a[i-1]+1
        while True:
            if all(math.gcd(m,a[j])>1 for j in range(i)):
                break
            m+=1
        a[i]=m
    return a

# Verify on a1=15
a_naive = naive_greedy(15, 30)
print("naive a1=15 first 15:", a_naive[:15])
sp = sieve_primes(200000)
a, stats = greedy_mt_tracked(15, 30, sp)
print("mt   a1=15 first 15:", a[:15])
print("match:", a[:15]==a_naive[:15])

