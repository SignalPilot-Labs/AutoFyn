import sys
from math import gcd
from sympy import primefactors

def gen_seq(a1, length):
    seq = [a1]
    while len(seq) < length:
        cur = seq[-1]
        cand = cur + 1
        while True:
            ok = all(gcd(cand, x) > 1 for x in seq)
            if ok:
                break
            cand += 1
        seq.append(cand)
    return seq

def P(m):
    return frozenset(primefactors(m))

def persistent_types(seq, keyset, tail_frac=0.6):
    n = len(seq)
    start = int(n*tail_frac)
    from collections import Counter
    c = Counter()
    for i in range(start, n):
        t = P(seq[i]) & keyset
        c[t] += 1
    # persistent = appears many times in tail (heuristic: count > 3)
    persistent = set(t for t,cnt in c.items() if cnt >= 3)
    return persistent, c

def analyze(a1, length=3000, tail_frac=0.5, verbose=True):
    seq = gen_seq(a1, length)
    Q = P(a1)
    if verbose: print(f"a1={a1}, Q={sorted(Q)}, seq_len={len(seq)}, last={seq[-1]}")
    # base persistent types
    base_persist, base_counts = persistent_types(seq, Q, tail_frac)
    if verbose:
        print(f"  base persistent types ({len(base_persist)}): {[sorted(t) for t in base_persist]}")
    # canonical witness per base type: smallest index (1-indexed) with tau(n)=B, restrict to n > N0 (use tail_frac*len as proxy for "after transient")
    N0 = int(len(seq)*tail_frac)
    canon_idx = {}
    for i in range(N0, len(seq)):
        t = P(seq[i]) & Q
        if t in base_persist and t not in canon_idx:
            canon_idx[t] = i
    S = set()
    F = {}
    for B, idx in canon_idx.items():
        FB = P(seq[idx]) - Q
        F[B] = FB
        S |= FB
    S0 = Q | S
    if verbose:
        print(f"  S (extra primes)={sorted(S)}, S0={sorted(S0)}")
    return seq, Q, base_persist, canon_idx, F, S, S0

def extended_types(seq, S0, tail_frac=0.5, min_count=3):
    from collections import Counter
    n = len(seq)
    start = int(n*tail_frac)
    c = Counter()
    for i in range(start, n):
        t = P(seq[i]) & S0
        c[t] += 1
    persistent = set(t for t,cnt in c.items() if cnt >= min_count)
    return persistent, c

def find_rogue_pairs(seq, Q, S0, base_persist, tail_frac=0.5):
    ext_persist, ext_counts = extended_types(seq, S0, tail_frac)
    # canonical extended type per base type = the extended type of the canonical witness
    N0 = int(len(seq)*tail_frac)
    canon_ext = {}
    for i in range(N0, len(seq)):
        t = P(seq[i]) & Q
        if t in base_persist and t not in canon_ext:
            canon_ext[t] = P(seq[i]) & S0
    rogue = []
    all_pairs_checked = 0
    violations = []
    for Ap in ext_persist:
        for Bp in ext_persist:
            if Ap == Bp: continue
            A = Ap & Q
            B = Bp & Q
            if A not in base_persist or B not in base_persist: continue
            if A == B: continue
            if len(A & B) != 0: continue  # need disjoint base types
            all_pairs_checked += 1
            if len(Ap & Bp) == 0:
                violations.append((Ap,Bp,A,B))
                Acan = canon_ext.get(A)
                Bcan = canon_ext.get(B)
                is_rogue = (Ap != Acan) and (Bp != Bcan)
                if is_rogue:
                    rogue.append((Ap,Bp,A,B))
    return ext_persist, canon_ext, violations, rogue

if __name__ == "__main__":
    a1 = int(sys.argv[1]) if len(sys.argv)>1 else 175
    length = int(sys.argv[2]) if len(sys.argv)>2 else 3000
    seq, Q, base_persist, canon_idx, F, S, S0 = analyze(a1, length)
    ext_persist, canon_ext, violations, rogue = find_rogue_pairs(seq, Q, S0, base_persist)
    print(f"  #ext_persist={len(ext_persist)}")
    print(f"  violations (disjoint base, disjoint ext) count={len(violations)}")
    for v in violations:
        print("   viol:", sorted(v[0]), sorted(v[1]), "base A,B:", sorted(v[2]), sorted(v[3]))
    print(f"  rogue pairs count={len(rogue)}")
    for r in rogue:
        print("   ROGUE:", sorted(r[0]), sorted(r[1]), "base A,B:", sorted(r[2]), sorted(r[3]))
