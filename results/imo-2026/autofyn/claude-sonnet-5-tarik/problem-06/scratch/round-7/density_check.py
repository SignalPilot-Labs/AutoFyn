import sympy
from sympy import primerange, factorint

def gen_seq(a1, N):
    seq=[a1]
    while len(seq)<N:
        cand = seq[-1]+1
        while True:
            ok=True
            for x in seq:
                from math import gcd
                if gcd(cand,x)==1:
                    ok=False
                    break
            if ok:
                seq.append(cand)
                break
            cand+=1
    return seq

for a1 in [247, 2747, 91]:
    N=1500
    seq = gen_seq(a1, N)
    rad1 = set(factorint(a1).keys())
    k = len(rad1)
    R = seq[-1]-seq[0]
    # m_p(N): count of terms divisible by p, for p in rad1 and some others
    from collections import Counter
    cnt = Counter()
    for x in seq:
        for p in factorint(x).keys():
            cnt[p]+=1
    # total omega sum
    total_omega = sum(len(factorint(x)) for x in seq)
    print(f"a1={a1}, k={k}, N={N}, R={R}, total_omega_sum={total_omega}, N*log2(R)~{N* (R.bit_length())}")
    # dominant prime in P_1
    dom = max(rad1, key=lambda p: cnt[p])
    print(f"  P_1={rad1}, counts in P_1: {[(p,cnt[p]) for p in rad1]}, N/k={N/k:.1f}")
    # top primes overall by count
    top = cnt.most_common(8)
    print(f"  top primes overall by count: {top}")
    # sum_p m_p^2 for p<=200 vs N^2/2
    small_sum = sum(v**2 for p,v in cnt.items() if p<=200)
    print(f"  sum_{{p<=200}} m_p^2 = {small_sum}, N^2/2={N**2/2:.0f}, ratio={small_sum/(N**2/2):.4f}")
