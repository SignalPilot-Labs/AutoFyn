import itertools
from fractions import Fraction as F

def e_of(vals):
    vals = sorted(vals, reverse=True)
    s = 0; sign=1
    for v in vals:
        s += sign*v; sign=-sign
    return s

def all_noncrossing_matchings(lst):
    if not lst:
        yield []
        return
    first = lst[0]; rest = lst[1:]
    if not rest: return
    for k in range(len(rest)):
        partner = rest[k]
        inside = rest[:k]; outside = rest[k+1:]
        if len(inside)%2!=0: continue
        for in_match in all_noncrossing_matchings(inside):
            for out_match in all_noncrossing_matchings(outside):
                yield [(first,partner)]+in_match+out_match

def value_of_config(Y, deleted, kept, pairing):
    vals = [Y[i] for i in kept]
    for (i,j) in pairing:
        a,b = Y[i], Y[j]
        if a<b: a,b=b,a
        vals.append(a-b)
    return e_of(vals)

def noncrossing_search_argmin(Y, budget):
    n=len(Y); idxs=list(range(n))
    best=None; bestcfg=None
    for delete_mask in itertools.product([0,1], repeat=n):
        remaining=[idxs[i] for i in range(n) if delete_mask[i]==0]
        deleted=[idxs[i] for i in range(n) if delete_mask[i]==1]
        ndel=len(deleted)
        if ndel>budget: continue
        m=len(remaining)
        for match_subset_mask in itertools.product([0,1], repeat=m):
            matched_idxs=[remaining[i] for i in range(m) if match_subset_mask[i]==1]
            kept_idxs=[remaining[i] for i in range(m) if match_subset_mask[i]==0]
            if len(matched_idxs)%2!=0: continue
            nmatch=len(matched_idxs)//2
            if ndel+nmatch>budget: continue
            if nmatch==0:
                v=value_of_config(Y,deleted,kept_idxs,[])
                if best is None or v<best: best,bestcfg=v,(deleted,kept_idxs,[])
                continue
            matched_sorted=sorted(matched_idxs)
            for pairing in all_noncrossing_matchings(matched_sorted):
                v=value_of_config(Y,deleted,kept_idxs,pairing)
                if best is None or v<best: best,bestcfg=v,(deleted,kept_idxs,pairing)
    return best,bestcfg

Y=[F(x) for x in [43,33,20,16,11,8,2]]
val,cfg = noncrossing_search_argmin(Y,2)
print("noncrossing b=2 optimum:",val,"config:",cfg)
