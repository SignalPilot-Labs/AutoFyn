from fractions import Fraction as F

D3 = 15
a3 = F(8,15)

def A_of(vals):
    s = sorted(vals, reverse=True)
    tot = F(0)
    for i,v in enumerate(s):
        tot += v if i%2==0 else -v
    return tot

def phi_of(vals):
    T = sum(vals)
    return (T + A_of(vals))/2

def strategies(p1,p2,p3,p4):
    T = p1+p2+p3+p4
    results = []
    # Bisect-top-k, k=0..3
    pieces = [p1,p2,p3,p4]
    for k in range(0,4):
        final = []
        for i in range(4):
            if i < k:
                final += [pieces[i]/2, pieces[i]/2]
            else:
                final.append(pieces[i])
        results.append(('bisect-top-%d'%k, phi_of(final)))
    # Theorem A (full match) if p1>=T/2
    if p1 >= T/2:
        v = p1 - (p2+p3+p4)
        final = [p2,p2,p3,p3,p4,p4]
        if v>0: final.append(v)
        results.append(('thmA', phi_of(final)))
    # Theorem D: bisect p1,p4, leave p2,p3
    final = [p1/2,p1/2,p2,p3,p4/2,p4/2]
    results.append(('thmD', phi_of(final)))
    # Theorem E: bisect p1,p2, leave p3,p4
    final = [p1/2,p1/2,p2/2,p2/2,p3,p4]
    results.append(('thmE', phi_of(final)))
    # Peel p1 vs pk (k=2,3,4 i.e. p2,p3,p4), then bisect residual max (2 remaining cuts: bisect residual once, then bisect result's max again if budget allows -- simplistic: just bisect residual once)
    for k, pk in enumerate([p2,p3,p4], start=2):
        w = p1-pk
        if w<0: continue
        rest = [x for j,x in enumerate([p2,p3,p4],start=2) if j!=k]
        # residual multiset: {w}+pk(untouched, already counted as pair with new frag)+rest
        residual = [w]+rest
        final = [pk,pk]+residual  # 1 cut used
        # now bisect the max of residual with 1 more cut (2 total), then optionally one more (3 total) bisect new max
        residual_sorted = sorted(residual, reverse=True)
        # bisect max once
        mx = residual_sorted[0]
        rest2 = residual_sorted[1:]
        final2 = [pk,pk, mx/2, mx/2] + rest2
        results.append(('peel%d-then-bisect1'%k, phi_of(final2)))
        # bisect again the new max among final2's non-pk part with 3rd cut
        cand = [mx/2, mx/2] + rest2
        cand_sorted = sorted(cand, reverse=True)
        mx2 = cand_sorted[0]
        rest3 = cand_sorted[1:]
        final3 = [pk,pk, mx2/2, mx2/2] + rest3
        results.append(('peel%d-then-bisect2'%k, phi_of(final3)))
    # Iterated greedy peel construction
    W = sorted([p1,p2,p3,p4], reverse=True)
    cuts = 0
    while len(W) >= 2 and cuts <= 3:
        a,b = W[0], W[1]
        if a == b:
            W = W[2:]
        else:
            if cuts >= 3:
                break
            W = sorted([a-b]+W[2:], reverse=True)
            cuts += 1
    vfinal = W[0] if W else F(0)
    results.append(('greedy-peel', (T+vfinal)/2))
    # Cross-piece / alternating-gap-cross with j=1 (split p1 sandwich p2), j=2 (split p1 sandwich p2, split p3 sandwich p4)
    # j=1: split p1 into (a,b) with a>p2>b, if feasible (p1>p2)
    if p1 > p2:
        # choose a,b sandwiching p2, e.g. a = (p1+p2)/2 if that's >p2 and b=p1-a <p2 ... simplest: a=p2+eps... use exact midpoint of (p2,p1)
        a1 = (p1+p2)/2
        b1 = p1-a1
        if a1>p2 and 0<b1<p2:
            final = [a1,p2,b1,p3,p4]
            results.append(('gapcross-j1', phi_of(final)))
    # j=2: split p1 sandwich p2, split p3 sandwich p4 (need p1>p2, p3>p4, and feasibility gamma condition)
    if p1>p2 and p3>p4:
        gamma1 = min(p1-p2,p2)
        # pair2: a2 in (max(p4,p3-p4), min(p3,gamma1))
        lower2 = max(p4,p3-p4)
        upper2 = min(p3,gamma1)
        if lower2 < upper2:
            a2 = (lower2+upper2)/2
            b2 = p3-a2
            lower1 = max(p2,p1-p2)
            upper1 = p1  # ceiling infinite at top
            # need a1 < p1's own bound and a1 > lower1, plus b1 (=p1-a1) > a2 (chain requires a2 < b1)
            # b1 > a2  <=> a1 < p1-a2
            upper1 = min(upper1, p1-a2)
            if lower1 < upper1:
                a1 = (lower1+upper1)/2
                b1 = p1-a1
                final = [a1,p2,b1,a2,p4,b2]
                results.append(('gapcross-j2', phi_of(final)))
    return results

# grid search over case (b2) box at n=3: p1<1/2, p2 in (1/15,4/15), p1>=p2>=p3>=p4>0, sum=1
best_margin = None
worst = None
count = 0
uncovered = []
N = 30
for i1 in range(1, N):
    p1 = F(i1, 2*N)  # up to just under 1/2
    if p1 <= 0: continue
    for i2 in range(1, N):
        p2 = F(1,15) + (F(4,15)-F(1,15))*F(i2,N)
        if p2 <= 0 or p2 >= p1:
            continue
        for i3 in range(1, N, 3):
            p3 = p2*F(i3,N)
            if p3 <= 0 or p3 > p2:
                continue
            p4 = 1 - p1 - p2 - p3
            if p4 <= 0 or p4 > p3:
                continue
            count += 1
            res = strategies(p1,p2,p3,p4)
            vals = [v for name,v in res]
            m = min(vals)
            margin = a3 - m
            if worst is None or margin < worst:
                worst = margin
                worst_point = (p1,p2,p3,p4,m)
            if m > a3:
                uncovered.append((p1,p2,p3,p4,m, [n for n,v in res]))

print("count tested:", count)
print("worst margin (a3 - min_achieved):", worst, float(worst) if worst is not None else None)
print("worst point:", worst_point)
print("num uncovered (min > a3):", len(uncovered))
if uncovered:
    for u in uncovered[:5]:
        print(u)
