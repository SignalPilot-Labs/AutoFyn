"""Simulate greedy P6 and track M_n evolution + candidate rank measures."""
import sys
from itertools import combinations
from math import gcd
from sympy import factorint

def P(m):
    """set of prime divisors of m"""
    return frozenset(factorint(m).keys())

def is_transversal(T, family):
    """T hits every member of family"""
    Tset = set(T)
    return all(Tset & set(M) for M in family)

def all_transversals_brute(Pess, family):
    """Full 2^|Pess| subset enumeration of transversals of family over prime-universe Pess."""
    Pl = sorted(Pess)
    trans = []
    for k in range(1, len(Pl)+1):
        for combo in combinations(Pl, k):
            if is_transversal(set(combo), family):
                trans.append(frozenset(combo))
    # transversals are upward closed: add supersets? Actually for mtp we only need minimal-cardinality
    # but for COUNT of all transversals, we need all subsets that are transversals. Use 2^|Pess| full.
    return trans

def count_transversals_full(Pess, family):
    """Full 2^|Pess| count of transversals (including non-minimal)."""
    Pl = sorted(Pess)
    n = len(Pl)
    cnt = 0
    for mask in range(1, 1<<n):
        s = set()
        for i in range(n):
            if mask & (1<<i):
                s.add(Pl[i])
        if is_transversal(s, family):
            cnt += 1
    return cnt

def mtp_value(Pess, family):
    """min product of a transversal (over Pess universe). Full subset enum."""
    Pl = sorted(Pess)
    n = len(Pl)
    best = None
    for mask in range(1, 1<<n):
        s = set()
        for i in range(n):
            if mask & (1<<i):
                s.add(Pl[i])
        if is_transversal(s, family):
            prod = 1
            for p in s:
                prod *= p
            if best is None or prod < best:
                best = prod
    return best

def minimal_supports(family_list):
    """family_list: list of frozensets P(a_i). Return min-under-inclusion family."""
    # remove duplicates, sort by size
    fam = list(set(family_list))
    minimals = []
    for S in fam:
        if not any(other < S or (other == S) for other in fam if other is not S):
            pass
    # proper: S is minimal if no other T in fam with T proper-subset S
    minimals = []
    for S in fam:
        if not any(T < S for T in fam):
            minimals.append(S)
    return frozenset(minimals)

def simulate(a1, N=4000, verbose=False):
    """Run greedy. Track M_n at every step where a new minimal enters (promotion).
    Return list of (step, M_n family, a_n). Also return final stabilized M and the diff period."""
    seq = [a1]
    fam_list = [P(a1)]
    Mn = minimal_supports(fam_list)
    promotions = [(1, Mn, a1)]  # initial
    for step in range(2, N+1):
        an = seq[-1]
        # find smallest m > an with P(m) transversal of Mn (hits all minimal supports)
        # equivalently hits all P(a_i) for i<step
        m = an + 1
        while True:
            pm = P(m)
            # hits all minimal supports?
            if all(set(pm) & set(M) for M in Mn):
                break
            m += 1
            if m > an + 100000:
                # safety
                break
        seq.append(m)
        fam_list.append(P(m))
        new_Mn = minimal_supports(fam_list)
        if new_Mn != Mn:
            promotions.append((step, new_Mn, m))
            Mn = new_Mn
        # stop if no promotions for a long stretch & we've seen enough
    return seq, promotions

# verify minimal_supports
def test_minimal():
    fam = [frozenset({2,3,5}), frozenset({2}), frozenset({3,7})]
    m = minimal_supports(fam)
    print("minimals:", [set(x) for x in m])
    assert frozenset({2}) in m
    assert frozenset({3,7}) in m
    assert frozenset({2,3,5}) not in m
    print("OK")

test_minimal()

# small test: a1=15
seq, prom = simulate(15, N=60)
print("a1=15 first 20 terms:", seq[:20])
print("num promotions:", len(prom))
for s, mn, an in prom:
    print(f"  step {s}: |M|={len(mn)} a_n={an} M={[set(x) for x in mn]}")
