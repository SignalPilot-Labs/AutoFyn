import json, sys
from sympy import factorint
from itertools import combinations

def rad(x, cache={}):
    if x in cache:
        return cache[x]
    r = frozenset(factorint(x).keys())
    cache[x] = r
    return r

def load(a1, path):
    with open(path) as f:
        arr = json.load(f)
    # arr[0] = a_1, arr[k-1] = a_k
    return arr

def analyze(a1, seq, S):
    """S: frozenset, proper nonempty subset of P1=rad(a1)."""
    P1 = rad(a1)
    assert S < P1 and len(S) > 0
    n = len(seq)
    G = [None] + [rad(seq[i-1]) & P1 for i in range(1, n+1)]
    comp = [None] + [rad(seq[i-1]) - P1 for i in range(1, n+1)]
    RAD = [None] + [rad(seq[i-1]) for i in range(1, n+1)]
    I_S = [i for i in range(1, n+1) if G[i] == S]
    # witnesses: j with G_j disjoint from S
    witnesses = [j for j in range(1, n+1) if G[j] & S == set()]
    # find all disjoint-companion witness PAIRS (j1<j2) among witnesses with nonempty comp
    good_witnesses = [j for j in witnesses if len(comp[j]) > 0]
    disjoint_pairs = []
    for idx1 in range(len(good_witnesses)):
        for idx2 in range(idx1+1, len(good_witnesses)):
            j1, j2 = good_witnesses[idx1], good_witnesses[idx2]
            if comp[j1] & comp[j2] == set():
                disjoint_pairs.append((j1, j2))
    return {
        "P1": P1, "S": S, "n": n,
        "I_S_count": len(I_S),
        "I_S_first10": I_S[:10],
        "witness_count": len(witnesses),
        "good_witness_count": len(good_witnesses),
        "num_disjoint_pairs": len(disjoint_pairs),
        "disjoint_pairs_sample": disjoint_pairs[:20],
        "G": G, "comp": comp, "RAD": RAD, "I_S": I_S,
    }

def bucket_report(a1, seq, S, j1, j2, verbose=True):
    P1 = rad(a1)
    n = len(seq)
    G = [None] + [rad(seq[i-1]) & P1 for i in range(1, n+1)]
    comp = [None] + [rad(seq[i-1]) - P1 for i in range(1, n+1)]
    RAD = [None] + [rad(seq[i-1]) for i in range(1, n+1)]
    I_S = [i for i in range(1, n+1) if G[i] == S]

    c1, c2 = comp[j1], comp[j2]
    assert c1 & c2 == set()
    buckets = [frozenset({p, q}) for p in c1 for q in c2]
    bare_values = [S | b for b in buckets]

    realized_at = {}
    for bv in bare_values:
        realized_at[bv] = None
    for i in range(1, n+1):
        if RAD[i] in bare_values and realized_at[RAD[i]] is None:
            realized_at[RAD[i]] = i

    blocked_at = {}
    for bv in bare_values:
        blocked_at[bv] = None
    # find earliest j3 with RAD[j3] disjoint from bv
    for bv in bare_values:
        for j3 in range(1, n+1):
            if RAD[j3] & bv == set():
                blocked_at[bv] = j3
                break

    if verbose:
        print(f"S={set(S)}, j1={j1} comp={set(c1)}, j2={j2} comp={set(c2)}")
        print(f"  {len(buckets)} coarse buckets:")
        for bv in bare_values:
            r = realized_at[bv]
            b = blocked_at[bv]
            print(f"    bare={sorted(bv)}: realized_at={r}  first_blocked_by_index={b}")
    return {"buckets": buckets, "bare_values": bare_values,
            "realized_at": realized_at, "blocked_at": blocked_at}

def check_supersets_of_blocked(a1, seq, S, bv_blocked, block_idx):
    """Look for any term whose radical is a PROPER superset of bv_blocked
    (i.e. rad(a_i) ⊋ bv_blocked), at any index, and report whether/when."""
    P1 = rad(a1)
    n = len(seq)
    hits = []
    for i in range(1, n+1):
        r = rad(seq[i-1])
        if r > bv_blocked:  # proper superset
            hits.append((i, sorted(r)))
    return hits

if __name__ == "__main__":
    pass
