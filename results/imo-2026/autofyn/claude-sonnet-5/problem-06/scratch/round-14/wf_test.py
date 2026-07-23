import itertools, time
from gen import gen_sequence

def get_classes(a1, P1, N):
    terms, rads = gen_sequence(a1, N)
    P1set = set(P1)
    classes = {p: [] for p in P1}
    for idx, (v, R) in enumerate(zip(terms, rads), start=1):
        S = frozenset(R & P1set)
        if len(S) == 1:
            p = next(iter(S))
            comp = frozenset(R - P1set)
            classes[p].append((idx, v, comp))
    return classes

def minimal_transversals(clauses):
    """clauses: list of frozensets (each a small prime set). Return all
    minimal hitting sets (transversals) that intersect every clause,
    using only primes appearing in the clauses. Brute force via
    incremental transversal construction (Berge-style), small scale."""
    universe = sorted(set().union(*clauses)) if clauses else []
    # simple algorithm: start with transversals = {frozenset()}, for each
    # clause, if a candidate transversal already hits it, keep; else branch
    # by adding each element of the clause; then minimize.
    transversals = {frozenset()}
    for cl in clauses:
        new_transversals = set()
        for t in transversals:
            if t & cl:
                new_transversals.add(t)
            else:
                for p in cl:
                    new_transversals.add(t | {p})
        transversals = new_transversals
        # prune non-minimal
        transversals = {t for t in transversals
                         if not any(t2 < t for t2 in transversals)}
    return transversals

def cross_check(transA, transB):
    """Check every pair (one from A, one from B) shares a prime."""
    bad = []
    for ta in transA:
        for tb in transB:
            if not (ta & tb):
                bad.append((ta, tb))
    return bad

def run(a1, P1, N, n_witness):
    classes = get_classes(a1, P1, N)
    p1, p2 = P1
    print(f"\n=== a1={a1}, P1={P1}, N={N} ===")
    for p in P1:
        print(f"  class {{{p}}}: {len(classes[p])} members found, using first {n_witness}")
    # witnesses from class p1 constrain class p2, and vice versa
    clauses_for_p2 = [comp for (idx, v, comp) in classes[p1][:n_witness]]
    clauses_for_p1 = [comp for (idx, v, comp) in classes[p2][:n_witness]]
    t0=time.time()
    transA = minimal_transversals(clauses_for_p1)  # patterns forced on class p1 (from p2 witnesses)
    transB = minimal_transversals(clauses_for_p2)  # patterns forced on class p2 (from p1 witnesses)
    print(f"  transversals for class {{{p1}}} (from {{{p2}}} witnesses): {len(transA)} : {sorted(transA, key=lambda s:(len(s),sorted(s)))[:10]}")
    print(f"  transversals for class {{{p2}}} (from {{{p1}}} witnesses): {len(transB)} : {sorted(transB, key=lambda s:(len(s),sorted(s)))[:10]}")
    bad = cross_check(transA, transB)
    print(f"  cross-check bad pairs: {len(bad)}  (time {time.time()-t0:.2f}s)")
    if bad:
        print("   examples:", bad[:5])
    return transA, transB, bad

if __name__ == "__main__":
    run(2747, (41,67), 3000, 8)
    run(4087, (61,67), 3000, 8)
