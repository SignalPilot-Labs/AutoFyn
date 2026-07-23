import sympy
from sympy import primerange, factorint

def gen_sequence(a1, N, prime_cap=None):
    """Generate first N terms of the sequence starting at a1, using the
    minimal-radical-antichain fast method (per workspace's certified rule).
    Returns list of (value, radical_frozenset)."""
    terms = [a1]
    rad1 = frozenset(factorint(a1).keys())
    rads = [rad1]
    front = [rad1]  # minimal antichain of radicals under inclusion

    def admissible(c):
        # c admissible iff for every front element F, some prime in F divides c
        for F in front:
            if not any(c % p == 0 for p in F):
                return False
        return True

    cur = a1
    while len(terms) < N:
        c = cur + 1
        while not admissible(c):
            c += 1
        cur = c
        R = frozenset(factorint(c).keys())
        terms.append(c)
        rads.append(R)
        # update front: remove strict supersets of R, then add R if not a
        # (non-strict) superset of some remaining element
        new_front = [F for F in front if not R < F]  # remove strict supersets of R (F ⊋ R)
        # check if R is already dominated (some remaining F ⊆ R, F != R covered by <=)
        dominated = any(F <= R for F in new_front)
        if not dominated:
            new_front.append(R)
        front = new_front
    return terms, rads

if __name__ == "__main__":
    # sanity check against brute force for a1=15
    def brute(a1, N):
        terms = [a1]
        while len(terms) < N:
            c = terms[-1] + 1
            while not all(sympy.gcd(c, t) > 1 for t in terms):
                c += 1
            terms.append(c)
        return terms
    t1, _ = gen_sequence(15, 40)
    t2 = brute(15, 40)
    print("match:", t1 == t2)
