import itertools, random

def e(vals):
    vals = sorted(vals, reverse=True)
    s = 0
    for i,v in enumerate(vals):
        s += v if i%2==0 else -v
    return s

def value(Y, K,D,M):
    vals = [Y[k] for k in K] + [Y[i]-Y[j] for (i,j) in M]
    return e(vals)

def crosses(M):
    for a in range(len(M)):
        for bb in range(a+1,len(M)):
            i,j = M[a]; ii,jj = M[bb]
            if i>j: i,j=j,i
            if ii>jj: ii,jj=jj,ii
            if (i<ii<j<jj) or (ii<i<jj<j):
                return True
    return False

def all_matchings_on_support(support):
    if not support:
        yield ()
        return
    a = support[0]
    rest = support[1:]
    for k in range(len(rest)):
        b_ = rest[k]
        remaining = rest[:k]+rest[k+1:]
        for m in all_matchings_on_support(remaining):
            yield ((a,b_),) + m

# Test THE KNOWN p=7,b=3 counterexample's own OPT-winning fixed support.
Y = [39,36,30,28,22,18,14]  # already sorted descending
K = (6,)  # kept 14 (index6)
support = [0,2,1,4,3,5]  # matched indices from the OPT winning selection (39,30),(36,22),(28,18)
support_sorted = sorted(support)
print("Testing fixed support", support_sorted, "kept", K)
best = None
worst = None
for m in all_matchings_on_support(support_sorted):
    v = value(Y, K, (), m)
    tag = "NC" if not crosses(m) else "CROSS"
    print(m, tag, v)
