"""Count conflict states for forward-determinism of residue statistic a_n mod m.

A residue value r mod m is a "conflict state" if there exist two positions
n < n' with a_n == a_{n'} == r (mod m) but d_{n+1} != d_{n'+1}.
The statistic a_n mod m is forward-deterministic iff conflicts == 0.

We also report: realized = number of distinct residues actually visited,
and pairs = number of (n,n') pairs with n<n', a_n==a_{n'} mod m, d_{n+1}!=d_{n'+1}.
"""
import sys
sys.path.insert(0, '/tmp/round-6')
from mt_greedy import greedy_mt, rad, sieve_primes


def run(a1, N, mod_label, m):
    M1 = rad(a1)
    maxval = a1 + (N + 5) * M1 + 50
    small_limit = min(maxval, 5_000_000)
    sp = sieve_primes(small_limit)
    a = greedy_mt(a1, N, sp)
    d = [a[i+1] - a[i] for i in range(N-1)]
    # Map residue r -> list of successor increments d_{n+1} for positions n with a_n == r
    succ = {}
    for n in range(N-1):
        r = a[n] % m
        succ.setdefault(r, []).append(d[n])
    conflict_states = 0
    pairs = 0
    realized = len(succ)
    for r, ds in succ.items():
        # number of (n<n') pairs with same r but different d: total pairs minus pairs-with-equal-d
        # easier: conflict state iff len(set(ds)) >= 2
        if len(set(ds)) >= 2:
            conflict_states += 1
        # count pairs with distinct d values
        from collections import Counter
        cnt = Counter(ds)
        total = len(ds)
        eq_pairs = sum(c*(c-1)//2 for c in cnt.values())
        pairs += total*(total-1)//2 - eq_pairs
    print(f"a1={a1}, N={N}, m={m} ({mod_label}): realized={realized}, "
          f"conflict_states={conflict_states}, conflict_pairs={pairs}, "
          f"fwd_det={'YES' if conflict_states==0 else 'NO'}")


if __name__ == '__main__':
    # Primary witness: a1=175, m = a1^2 = 30625
    run(175, 50000, 'a1^2', 175*175)
    # also m = a1
    run(175, 50000, 'a1', 175)
    # also m = M1 = rad(a1) = 35
    run(175, 50000, 'M1', rad(175))
    # smaller witness a1=77 (rad-77 pair member)
    run(77, 5000, 'a1^2', 77*77)
    run(77, 5000, 'a1', 77)
    # a1=91
    run(91, 5000, 'a1^2', 91*91)
    run(91, 5000, 'a1', 91)
    # a1=847: state space 717409 >> N, but still report honestly
    run(847, 50000, 'a1^2', 847*847)
