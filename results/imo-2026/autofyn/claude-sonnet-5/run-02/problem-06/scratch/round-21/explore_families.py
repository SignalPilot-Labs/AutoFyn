import sympy
from sympy import factorint

def greedy_seq_fast(a1, n_terms, max_candidate_search=2_000_000):
    seq=[a1]
    used={a1}
    prime_mask={}  # prime -> bitmask of indices (0-indexed) with that prime dividing a_i
    def add_term(idx, val):
        for p in factorint(val):
            prime_mask[p] = prime_mask.get(p,0) | (1<<idx)
    add_term(0, a1)
    full_mask = 1  # mask of all covered indices so far (bit i set means index i covered... but we need "all indices from 0..len-1 must be covered")
    n_indices = 1
    cur = a1
    while len(seq) < n_terms:
        c = cur+1
        while True:
            if c in used:
                c+=1
                continue
            facs = factorint(c)
            m = 0
            for p in facs:
                m |= prime_mask.get(p,0)
            need_mask = (1<<n_indices)-1
            if (m & need_mask) == need_mask:
                break
            c+=1
        seq.append(c)
        used.add(c)
        add_term(n_indices, c)
        n_indices += 1
        cur = c
    return seq

def analyze(a1, n_terms):
    seq = greedy_seq_fast(a1, n_terms)
    Q = set(factorint(a1).keys())
    types=[frozenset(p for p in Q if s%p==0) for s in seq]
    return seq, Q, types

from collections import Counter

def summarize(a1, n_terms=1500):
    seq, Q, types = analyze(a1, n_terms)
    c = Counter(types)
    return Q, c

if __name__=="__main__":
    # p^2 q family
    print("=== p^2*q family ===")
    for (p,q) in [(2,3),(2,5),(3,5),(3,7),(5,7),(2,7),(5,11)]:
        a1 = p*p*q
        Q,c = summarize(a1, 1200)
        print(f"a1={a1} p={p}^2 q={q} Q={Q} counts={dict(c)}")

def check_first_lone(a1, target_prime, n_terms):
    seq, Q, types = analyze(a1, n_terms)
    for i,t in enumerate(types):
        if t == frozenset({target_prime}):
            return i+1, seq[i]
    return None
