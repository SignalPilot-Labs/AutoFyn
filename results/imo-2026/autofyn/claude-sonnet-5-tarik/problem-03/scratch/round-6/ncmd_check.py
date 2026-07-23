import itertools, random
from fractions import Fraction as F

def e_of(vals):
    vals = sorted(vals, reverse=True)
    s = 0
    sign = 1
    for v in vals:
        s += sign*v
        sign = -sign
    return s

def all_partitions_into_singles_and_pairs(indices):
    """Yield all ways to partition a subset of `indices` into matched pairs (i<j) plus
    leave the rest alone (as either 'kept' or 'deleted' - handled outside). Actually here
    we yield partitions of the FULL index list into: matched pairs, deleted singles, kept singles.
    We generate all subsets to delete, then all matchings on the remainder, combined with 'kept'."""
    n = len(indices)
    # iterate over all ways to 3-color each index: 0=keep,1=delete,2=match(needs pairing)
    # then for the 'match' colored ones, enumerate perfect matchings among them (any pairing, unrestricted)
    for delete_mask in itertools.product([0,1], repeat=n):
        remaining = [indices[i] for i in range(n) if delete_mask[i]==0]
        deleted = [indices[i] for i in range(n) if delete_mask[i]==1]
        # among remaining, choose a subset to match (must be even-sized groups of pairs), rest kept
        m = len(remaining)
        # enumerate subsets of remaining to be matched (any size, must end up paired), rest kept as-is
        for match_subset_mask in itertools.product([0,1], repeat=m):
            matched_idxs = [remaining[i] for i in range(m) if match_subset_mask[i]==1]
            kept_idxs = [remaining[i] for i in range(m) if match_subset_mask[i]==0]
            if len(matched_idxs) % 2 != 0:
                continue
            if len(matched_idxs) == 0:
                yield (deleted, kept_idxs, [])
                continue
            # enumerate all perfect matchings of matched_idxs (unrestricted, any pairing)
            for pairing in all_perfect_matchings(matched_idxs):
                yield (deleted, kept_idxs, pairing)

def all_perfect_matchings(lst):
    if not lst:
        yield []
        return
    first = lst[0]
    rest = lst[1:]
    for k in range(len(rest)):
        partner = rest[k]
        remaining = rest[:k]+rest[k+1:]
        for sub in all_perfect_matchings(remaining):
            yield [(first,partner)]+sub

def all_noncrossing_matchings(lst):
    """lst is list of original positions (sorted ascending indices), yield all non-crossing
    perfect matchings (pairs (i,j), i<j in position order) using the classical recursion."""
    if not lst:
        yield []
        return
    first = lst[0]
    rest = lst[1:]
    if not rest:
        return  # can't match odd leftover alone -- shouldn't happen since caller filters
    for k in range(len(rest)):
        partner = rest[k]
        inside = rest[:k]      # must be matched among themselves (non-crossing requires inside stays inside)
        outside = rest[k+1:]
        if len(inside) % 2 != 0:
            continue
        for in_match in all_noncrossing_matchings(inside):
            for out_match in all_noncrossing_matchings(outside):
                yield [(first,partner)] + in_match + out_match

def value_of_config(Y, deleted, kept, pairing):
    vals = [Y[i] for i in kept]
    for (i,j) in pairing:
        a,b = Y[i], Y[j]
        if a < b: a,b = b,a
        vals.append(a-b)
    return e_of(vals)

def full_search(Y, budget):
    n = len(Y)
    idxs = list(range(n))
    best = None
    for delete_mask in itertools.product([0,1], repeat=n):
        remaining = [idxs[i] for i in range(n) if delete_mask[i]==0]
        deleted = [idxs[i] for i in range(n) if delete_mask[i]==1]
        ndel = len(deleted)
        if ndel > budget:
            continue
        m = len(remaining)
        for match_subset_mask in itertools.product([0,1], repeat=m):
            matched_idxs = [remaining[i] for i in range(m) if match_subset_mask[i]==1]
            kept_idxs = [remaining[i] for i in range(m) if match_subset_mask[i]==0]
            if len(matched_idxs) % 2 != 0:
                continue
            nmatch = len(matched_idxs)//2
            if ndel + nmatch > budget:
                continue
            if nmatch == 0:
                v = value_of_config(Y, deleted, kept_idxs, [])
                if best is None or v < best: best = v
                continue
            for pairing in all_perfect_matchings(matched_idxs):
                v = value_of_config(Y, deleted, kept_idxs, pairing)
                if best is None or v < best: best = v
    return best

def noncrossing_search(Y, budget):
    n = len(Y)
    idxs = list(range(n))
    best = None
    for delete_mask in itertools.product([0,1], repeat=n):
        remaining = [idxs[i] for i in range(n) if delete_mask[i]==0]
        deleted = [idxs[i] for i in range(n) if delete_mask[i]==1]
        ndel = len(deleted)
        if ndel > budget:
            continue
        m = len(remaining)
        for match_subset_mask in itertools.product([0,1], repeat=m):
            matched_idxs = [remaining[i] for i in range(m) if match_subset_mask[i]==1]
            kept_idxs = [remaining[i] for i in range(m) if match_subset_mask[i]==0]
            if len(matched_idxs) % 2 != 0:
                continue
            nmatch = len(matched_idxs)//2
            if ndel + nmatch > budget:
                continue
            if nmatch == 0:
                v = value_of_config(Y, deleted, kept_idxs, [])
                if best is None or v < best: best = v
                continue
            # matched_idxs are positions in ascending order already (subset of idxs, sorted)
            matched_idxs_sorted = sorted(matched_idxs)
            for pairing in all_noncrossing_matchings(matched_idxs_sorted):
                v = value_of_config(Y, deleted, kept_idxs, pairing)
                if best is None or v < best: best = v
    return best

random.seed(12345)
mismatches = []
trials = 0
for trial in range(400):
    p = random.randint(3,6)
    Y = sorted([F(random.randint(1,200)) for _ in range(p)], reverse=True)
    budget = random.randint(1,p)
    trials += 1
    f = full_search(Y, budget)
    nc = noncrossing_search(Y, budget)
    if f != nc:
        mismatches.append((Y,budget,f,nc))

print("trials:",trials,"mismatches:",len(mismatches))
for m in mismatches[:10]:
    print(m)

print("---- targeted check: Y=(43,33,20,16,11,8,2) ----")
Y = [F(x) for x in [43,33,20,16,11,8,2]]
for b in range(0,7):
    f = full_search(Y,b)
    nc = noncrossing_search(Y,b)
    print("budget",b,"full=",f,"noncrossing=",nc, "match" if f==nc else "MISMATCH")
