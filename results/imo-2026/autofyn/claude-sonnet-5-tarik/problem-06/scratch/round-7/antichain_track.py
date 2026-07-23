import json, sys
from bucket_analysis import rad, load

def track_antichain(a1, seq, S, checkpoints=None):
    P1 = rad(a1)
    n = len(seq)
    RAD = [None] + [rad(seq[i-1]) for i in range(1, n+1)]
    G = [None] + [rad(seq[i-1]) & P1 for i in range(1, n+1)]
    I_S = [i for i in range(1, n+1) if G[i] == S]
    history = []  # (n_checkpoint, antichain_set)
    cur_antichain = []  # list of radicals, kept minimal
    idx_ptr = 0
    sizes = []
    for i in I_S:
        r = RAD[i]
        # remove any existing element that is a superset of r (dominated by r)
        cur_antichain = [x for x in cur_antichain if not (r <= x and r != x)]
        # check if r is already dominated by something smaller/equal present
        dominated = any(x <= r for x in cur_antichain)
        if not dominated:
            cur_antichain.append(r)
        sizes.append((i, len(cur_antichain), set(cur_antichain) if len(cur_antichain) <= 6 else None))
    return sizes

if __name__ == "__main__":
    import sys
    a1 = int(sys.argv[1])
    path = sys.argv[2]
    S = frozenset(int(x) for x in sys.argv[3].split(","))
    seq = load(a1, path)
    sizes = track_antichain(a1, seq, S)
    # print whenever size OR value changes
    prev = None
    for i, sz, ac in sizes:
        key = (sz, frozenset(ac) if ac is not None else None)
        if key != prev:
            print(i, sz, ac)
            prev = key
