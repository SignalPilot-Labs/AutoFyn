"""Probe for the two-coincidence-periodicity approach (IMO 2026 P6).

For each a_1 in a small test set, compute the greedy sequence, detect period T,L,
and test candidate abstractions alpha_n for:
  (A) forward-determinism: is alpha_{n+1} a single-valued function of alpha_n?
  (B) determining: does alpha_n determine d_{n+1} = a_{n+2}-a_{n+1}?
  (C) self-coincidences of the d-word at two different offsets (Fine-Wilf style).
"""
import math
from collections import defaultdict


def small_primes(a1):
    fs = set()
    x = a1
    d = 2
    while d * d <= x:
        while x % d == 0:
            fs.add(d)
            x //= d
        d += 1
    if x > 1:
        fs.add(x)
    return tuple(sorted(fs))


def greedy(a1, N):
    a = [a1]
    for _ in range(N - 1):
        an = a[-1]
        m = an + 1
        while True:
            ok = all(math.gcd(m, x) > 1 for x in a)
            if ok:
                a.append(m)
                break
            m += 1
    return a


def detect_period(d):
    """d = increment word. Find minimal eventual period T (tail period)."""
    n = len(d)
    for start in range(0, n // 2):
        for T in range(1, (n - start) // 2):
            ok = True
            for i in range(start, n - T):
                if d[i] != d[i + T]:
                    ok = False
                    break
            if ok:
                return start, T
    return None, None


def conflicts(alpha, d, lag=0):
    """Map alpha_n -> set of d_{n+1+lag} values; count conflicts (states with >1 d)."""
    M = defaultdict(set)
    for n in range(len(alpha) - 1 - lag):
        M[alpha[n]].add(d[n + 1 + lag - 1] if False else d[n + 1 + lag])
    # fix indexing: d[n] = a_{n+1}-a_n; alpha_n is a function of a_1..a_{n+1}.
    return M


def forward_det(alpha):
    """Is alpha_{n+1} a single-valued function of alpha_n? Return conflict count and realized states."""
    succ = defaultdict(set)
    for n in range(len(alpha) - 1):
        succ[alpha[n]].add(alpha[n + 1])
    conflicts = sum(1 for k, v in succ.items() if len(v) > 1)
    return conflicts, len(succ)


def determines(alpha, dnext):
    """Does alpha_n determine dnext_n? dnext_n is the value to predict at index n."""
    M = defaultdict(set)
    for n in range(len(alpha)):
        M[alpha[n]].add(dnext[n])
    conflicts = sum(1 for k, v in M.items() if len(v) > 1)
    return conflicts, len(M)


def witness_prime(a, P1):
    """For increment d_n = a_{n+1}-a_n, return tuple of small primes p in P1 dividing d_n."""
    out = []
    for n in range(len(a) - 1):
        dn = a[n + 1] - a[n]
        divs = tuple(p for p in P1 if dn % p == 0)
        out.append(divs)
    return out


def main():
    cases = [15, 35, 77, 91, 175, 385]
    for a1 in cases:
        P1 = small_primes(a1)
        M1 = 1
        for p in P1:
            M1 *= p
        N = 400 if a1 <= 91 else (2000 if a1 <= 385 else 4000)
        # cap for speed
        if a1 == 385:
            N = 1500
        a = greedy(a1, N)
        d = [a[n + 1] - a[n] for n in range(len(a) - 1)]
        start, T = detect_period(d)
        L = sum(d[start:start + T]) if T else None
        print(f"\n=== a1={a1}  P1={P1}  M1={M1}  N={N} ===")
        print(f"  period: start={start}, T={T}, L={L}, d_n<=M1? {max(d) <= M1} (max d={max(d)})")
        # candidate abstractions on the PERIODIC TAIL (from `start` onward)
        tail_a = a[start:]
        tail_d = d[start:]
        # alpha1 = witness-prime-tuple of d_n
        wp = witness_prime(a, P1)  # length len(a)-1, indexed by n (d_n)
        alpha1 = wp[start:]
        # alpha2 = d_n itself (finite alphabet {1..M1})
        alpha2 = [(dn,) for dn in tail_d]
        # alpha3 = (a_n mod M1) -- the fenced residue statistic
        alpha3 = [a[n] % M1 for n in range(start, len(a))]
        for name, alpha in [("wp(tup)", alpha1), ("d_n", alpha2), ("a mod M1", alpha3)]:
            cfd, rs = forward_det(alpha)
            # align: predict d_{n+1} = tail_d[n+1] from alpha_n; need n+1 < len(tail_d)
            dn1 = tail_d[1:]  # d_{n+1} for n in 0..len-2
            alpha_aligned = alpha[:len(dn1)]
            cdet, rdet = determines(alpha_aligned, dn1)
            print(f"  alpha={name:10s}: fwd-det conflicts={cfd:4d} realized={rs:4d} | determines d_n? conflicts={cdet} (realized alpha states={rdet})")


if __name__ == "__main__":
    main()
