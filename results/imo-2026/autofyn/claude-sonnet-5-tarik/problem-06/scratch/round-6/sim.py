import sys
from sympy import primefactors

def gen_sequence(a1, N, verbose_every=None):
    """Generate the greedy sequence using the minimal-antichain speedup.
    Returns (a_list (1-indexed, a_list[0] unused), antichain_history)
    where antichain_history[n] = frozenset of frozensets = 𝓜_n after appending a_n.
    """
    a = [None, a1]
    R1 = frozenset(primefactors(a1))
    antichain = {R1}
    history = {1: frozenset(antichain)}
    n = 1
    while n < N:
        cur = a[n]
        cand = cur + 1
        while True:
            radc = frozenset(primefactors(cand))
            if all(radc & s for s in antichain):
                break
            cand += 1
        n += 1
        a.append(cand)
        R = radc
        # Step 1: remove all s' that are proper supersets of R (dominated by new witness)
        antichain = {s for s in antichain if not (R < s)}
        # Step 2: add R unless dominated by some remaining s (s proper subset of R, or equal already present)
        dominated = any(s <= R and s != R for s in antichain) or (R in antichain)
        if not dominated:
            antichain.add(R)
        history[n] = frozenset(antichain)
    return a, history

if __name__ == "__main__":
    import time
    a1 = int(sys.argv[1])
    N = int(sys.argv[2])
    t0 = time.time()
    a, history = gen_sequence(a1, N)
    t1 = time.time()
    print(f"a1={a1} N={N} time={t1-t0:.1f}s")
    P1 = frozenset(primefactors(a1))
    print("P1 =", sorted(P1))
    Mfinal = history[N]
    print(f"|M_{N}| = {len(Mfinal)}")
    for s in sorted(Mfinal, key=lambda x: (len(x), sorted(x))):
        print("  ", sorted(s))
