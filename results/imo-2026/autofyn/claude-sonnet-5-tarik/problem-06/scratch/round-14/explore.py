import time
from gen import gen_sequence

def analyze(a1, P1, N):
    t0=time.time()
    terms, rads = gen_sequence(a1, N)
    print(f"a1={a1}, generated {N} terms in {time.time()-t0:.1f}s, last value={terms[-1]}")
    P1set = set(P1)
    data = []  # (index(1-based), value, S(i), comp(i))
    for idx, (v, R) in enumerate(zip(terms, rads), start=1):
        S = frozenset(R & P1set)
        comp = frozenset(R - P1set)
        data.append((idx, v, S, comp))
    return data

if __name__ == "__main__":
    for a1, P1 in [(2747, (41,67)), (4087, (61,67))]:
        data = analyze(a1, P1, 3000)
        # find low-index members of each singleton core class
        for p in P1:
            members = [(idx,v,comp) for (idx,v,S,comp) in data if S == frozenset([p])]
            print(f"  a1={a1} core {{{p}}}: {len(members)} members in first 3000 terms; first 8:")
            for m in members[:8]:
                print("    ", m)
