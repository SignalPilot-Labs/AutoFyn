import sympy, sys
from seqgen import gen_seq, rad

def local_antichain_events(a1, S, n_terms):
    seq = gen_seq(a1, n_terms)
    P1 = rad(a1)
    antichain = []  # list of frozensets, pairwise incomparable
    events = []
    for idx, a in enumerate(seq, 1):
        r = rad(a)
        imprint = r & P1
        if imprint != S:
            continue
        # check domination
        dominated_by = [t for t in antichain if t < r]  # t proper subset of r? use issubset and !=
        dominated_by = [t for t in antichain if t.issubset(r) and t != r]
        if dominated_by:
            continue  # r is dominated, no change
        if r in antichain:
            continue
        # r is not dominated; does it dominate existing elements?
        dominates = [t for t in antichain if r.issubset(t) and r != t]
        old = list(antichain)
        antichain = [t for t in antichain if t not in dominates] 
        antichain.append(r)
        events.append((idx, sorted(r), 'removed:'+str([sorted(t) for t in dominates]) if dominates else 'growth', sorted([sorted(t) for t in antichain])))
    return events

if __name__=="__main__":
    a1=int(sys.argv[1]); Sset=frozenset(int(x) for x in sys.argv[2].split(',')); n=int(sys.argv[3])
    for e in local_antichain_events(a1,Sset,n):
        print(e)
