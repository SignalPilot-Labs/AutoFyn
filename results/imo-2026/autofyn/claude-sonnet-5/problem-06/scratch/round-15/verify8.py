import random
from math import gcd

def generate(a1, N):
    seq = [a1]
    while len(seq) < N:
        cand = seq[-1] + 1
        while True:
            if all(gcd(cand, x) > 1 for x in seq):
                seq.append(cand)
                break
            cand += 1
    return seq

def check_lemma_rec(a1, N, seed=3):
    random.seed(seed)
    seq = generate(a1, N)
    maxterm = seq[-1]
    termset = sorted(seq)  # increasing
    termset_set = set(seq)
    k = a1
    # For n in [k, maxterm], determine "term or non-term", and 'earlier terms' = terms < n
    # earlier terms in sorted order up to but not including position where term>=n
    import bisect
    violations_forward = 0  # term n has an earlier-term-coprime witness (shouldn't)
    violations_backward = 0 # non-term n has NO earlier-term-coprime witness (shouldn't)
    checked = 0
    sample_ns = random.sample(range(k, maxterm+1), min(3000, maxterm-k+1))
    for n in sample_ns:
        idx = bisect.bisect_left(termset, n)  # number of terms < n
        earlier_terms = termset[:idx]
        has_coprime_witness = any(gcd(m, n) == 1 for m in earlier_terms)
        is_term = n in termset_set
        checked += 1
        if is_term and has_coprime_witness:
            violations_forward += 1
            print("VIOLATION: term with coprime witness", n)
        if (not is_term) and (not has_coprime_witness) and n>k:
            violations_backward += 1
            print("VIOLATION: non-term with no coprime witness", n)
    print(f"a1={a1}: checked {checked}, term-side violations {violations_forward}, nonterm-side violations {violations_backward}")

check_lemma_rec(247, 6000)
check_lemma_rec(2747, 4000)
check_lemma_rec(21528751, 1200)
