import sympy
from sympy import factorint
from collections import Counter

def greedy_seq(a1, N):
    """Generate N terms of greedy sequence starting at a1."""
    a = [a1]
    # support = set of primes dividing each a_i
    supports = [set(factorint(a1).keys())]
    for n in range(N-1):
        an = a[-1]
        m = an + 1
        while True:
            ok = True
            for s in supports:
                # gcd(m, a_i) > 1  iff shares a prime
                # m shares a prime with a_i iff m mod p == 0 for some p in s
                shared = False
                for p in s:
                    if m % p == 0:
                        shared = True
                        break
                if not shared:
                    ok = False
                    break
            if ok:
                break
            m += 1
        a.append(m)
        supports.append(set(factorint(m).keys()))
    return a, supports

def detect_period(a, min_match=200):
    """Detect period T of increment sequence d_n = a_{n+1}-a_n.
    Require min_match consecutive matches. Returns T or None."""
    d = [a[i+1]-a[i] for i in range(len(a)-1)]
    n = len(d)
    for T in range(1, n//2):
        # check d[i]==d[i+T] for a run
        ok = True
        for i in range(min_match):
            if d[n-1-min_match+i] != d[n-1-min_match+i-T]:
                ok = False
                break
        if ok:
            return T
    return None

def test_stats(a1, N=700):
    a, sup = greedy_seq(a1, N)
    M1 = 1
    for p in factorint(a1):
        M1 *= p
    d = [a[i+1]-a[i] for i in range(len(a)-1)]
    # statistic c_n = M1*floor((a_n-a1)/M1) - (a_n - a1)  (shortfall below block ceiling)
    # = (- (a_n - a1)) mod M1
    c = [(M1 - ((a[i]-a1) % M1)) % M1 for i in range(len(a))]
    # running gap average (integer part) b_n = floor(sum d_0..d_{n-1} / n) = floor((a_{n+1}-a1)/n)... use sum/n
    # number of distinct values
    n_distinct_c = len(set(c))
    n_distinct_d = len(set(d))
    # is c eventually constant? check tail
    tail = c[-100:]
    c_eventual_const = len(set(tail)) == 1
    # is d eventually constant?
    d_tail = d[-100:]
    d_eventual_const = len(set(d_tail)) == 1
    # |S(a_n)| sizes
    sizes = [len(s) for s in sup]
    n_distinct_sizes = len(set(sizes))
    sizes_eventual_const = len(set(sizes[-100:]))==1
    T = detect_period(a, min_match=min(200, len(a)//3))
    L = None
    if T:
        L = sum(d[:T]) if T < len(d) else None
    print(f"a1={a1} M1={M1} N={len(a)} T={T} L={L} |d|distinct={n_distinct_d} d_ev_const={d_eventual_const} |c|distinct={n_distinct_c} c_ev_const={c_eventual_const} |sizes|distinct={n_distinct_sizes} sizes_ev_const={sizes_eventual_const}")
    return a, d, c, sup, T, M1

if __name__ == '__main__':
    for a1 in [6, 15, 35, 77, 91, 105, 143, 385, 1309, 2085, 145, 116, 1001, 847, 175]:
        try:
            test_stats(a1, N=600)
        except Exception as e:
            print(f"a1={a1} ERROR {e}")
