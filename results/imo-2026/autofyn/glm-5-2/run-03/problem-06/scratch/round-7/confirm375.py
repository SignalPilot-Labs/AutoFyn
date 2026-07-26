import sys, math
sys.path.insert(0, '/tmp/round-6')
from fast_greedy_correct import greedy_fast, rad, sieve_primes, prime_factors

a1=375; N=20000
a=greedy_fast(a1,N)
d=[a[i+1]-a[i] for i in range(N-1)]
# find fundamental period: smallest T with d[k]==d[k+T] for all k in [0, N-1-T)
sp=sieve_primes(200000)
def is_period(d,T):
    return all(d[k+T]==d[k] for k in range(len(d)-1-T))
fund=None
for T in range(1, N//2):
    if is_period(d,T):
        fund=T; break
print(f"Fundamental period T = {fund}")
L=sum(d[0:fund])
print(f"L = {L} = {sorted(prime_factors(L,sp))} (product check: {math.prod(sorted(prime_factors(L,sp)))})")
print(f"M1 = rad({a1}) = {rad(a1)}")
gov=sorted(prime_factors(L,sp))
print(f"Governing primes (factors of L) = {gov}")
print(f"gov_max = {max(gov)} ; M1 = {rad(a1)} ; VIOLATION: {max(gov) > rad(a1)}")
# verify 19 divides some terms (it should, since 19|L and sequence periodic)
terms_div19 = [a[i] for i in range(N) if a[i]%19==0]
print(f"terms divisible by 19: first few = {terms_div19[:6]}, count in {N} terms = {len(terms_div19)}")
# verify 7 divides some terms (7 in L)
terms_div7 = [a[i] for i in range(N) if a[i]%7==0]
print(f"terms divisible by 7: count = {len(terms_div7)}, first = {terms_div7[:3]}")
# also check largest prime factor of ANY term to distinguish governing vs transient
max_term_pf = max((max(prime_factors(a[i],sp)) for i in range(N)))
print(f"largest prime factor appearing in any of {N} terms = {max_term_pf} (transient can be huge)")
