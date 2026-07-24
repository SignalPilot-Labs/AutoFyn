from sim import *
from collections import Counter

def recruit(seq, S0, Aprime, Bprime, tail_frac=0.5):
    n=len(seq); start=int(n*tail_frac)
    # find witness m with ext type = Bprime
    m = None
    for i in range(start, n):
        t = P(seq[i]) & S0
        if t == Bprime:
            m = i
            break
    if m is None:
        return None, None
    Fprime = P(seq[m]) - S0
    # now find which prime in Fprime recurs across occurrences of Aprime after m
    c = Counter()
    occ = 0
    for i in range(m+1, n):
        t = P(seq[i]) & S0
        if t == Aprime:
            occ += 1
            common = P(seq[i]) & Fprime
            for p in common:
                c[p]+=1
    return c, occ

seq, Q, base_persist, canon_idx, F, S, S0 = analyze(175, 4000)
ext_persist, canon_ext, violations, rogue = find_rogue_pairs(seq, Q, S0, base_persist)
Aprime = frozenset({2,7})
Bprime = frozenset({3,5})
c, occ = recruit(seq, S0, Aprime, Bprime)
print("occurrences of A'=[2,7] after witness m:", occ)
print("prime recurrence counts (candidates for q):", c)
