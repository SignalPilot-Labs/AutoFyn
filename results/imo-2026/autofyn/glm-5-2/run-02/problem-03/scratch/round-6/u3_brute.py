#!/usr/bin/env python3
"""Brute-force: for configs in z in [-2a,0] (d<1/2, w>=-2a, u,v,w>0),
enumerate all <=3-mark placements on a grid; find min A. Is min A <= alpha?
Also test if |b+c-d| is achievable as a cap value.
"""
from fractions import Fraction as F
import itertools, random

alpha = F(1,15)

def alt_sum(pieces):
    s=sorted(pieces, reverse=True)
    A=F(0)
    for i,p in enumerate(s):
        if i%2==0: A+=p
        else: A-=p
    return A

def strategies_abcd(a,b,c,d, Ngrid=20):
    """Yield final multisets from <=3 marks placed inside pieces a,b,c,d.
    Each mark inside a piece splits it. We grid the split fractions.
    Marks can be in same piece (multiple splits)."""
    # piece boundaries: [0,a), [a,a+b), [a+b, a+b+c), [a+b+c, 1]
    # a mark at position x in piece P splits P at fraction f in (0,1).
    # We generate marks as (piece_index, fraction). Up to 3 marks.
    pieces_list = [a,b,c,d]
    # fractions grid
    fracs = [F(i, Ngrid) for i in range(1, Ngrid)]
    # 0 marks: original
    yield [a,b,c,d]
    # 1 mark: choose piece, fraction
    for pi in range(4):
        for f in fracs:
            L = pieces_list[pi]*f; R = pieces_list[pi]-L
            new = [pieces_list[k] for k in range(4) if k!=pi] + [L,R]
            yield new
    # 2 marks
    for m1 in itertools.product(range(4), range(len(fracs))):
        for m2 in itertools.product(range(4), range(len(fracs))):
            if m1>m2: continue
            # apply both marks (could be same piece -> 3 sub-pieces)
            ps = list(pieces_list)
            # split piece m1[0] at frac fracs[m1[1]], and piece m2[0] at fracs[m2[1]]
            # build multisets: handle same-piece case
            p1, f1 = m1[0], fracs[m1[1]]
            p2, f2 = m2[0], fracs[m2[1]]
            if p1==p2:
                # two marks in same piece -> 3 sub-pieces
                L1 = pieces_list[p1]*f1; R1 = pieces_list[p1]-L1
                # split R1 (or L1) at f2 -- marks at two positions; assume f1<f2 region
                # Actually two marks in one piece: positions t1<t2 -> (t1, t2-t1, 1-t2)
                # use fractions f1, f2 as positions
                pos = sorted([f1,f2])
                s1=pieces_list[p1]*pos[0]
                s2=pieces_list[p1]*(pos[1]-pos[0])
                s3=pieces_list[p1]*(1-pos[1])
                new=[pieces_list[k] for k in range(4) if k!=p1]+[s1,s2,s3]
                yield new
            else:
                L1=pieces_list[p1]*f1; R1=pieces_list[p1]-L1
                L2=pieces_list[p2]*f2; R2=pieces_list[p2]-L2
                new=[pieces_list[k] for k in range(4) if k!=p1 and k!=p2]+[L1,R1,L2,R2]
                yield new
    # 3 marks (limit grid for tractability): pick 3 (piece,frac) with distinct-ish
    for combo in itertools.combinations(itertools.product(range(4), range(0,len(fracs),2)), 3):
        # apply 3 marks; handle grouping by piece
        from collections import defaultdict
        by_piece=defaultdict(list)
        for (pi,fi) in combo:
            by_piece[pi].append(fracs[fi])
        new=[]
        for k in range(4):
            if k not in by_piece:
                new.append(pieces_list[k])
            else:
                pts=sorted(by_piece[k])
                prev=0; parts=[]
                for p in pts:
                    parts.append(pieces_list[k]*(p-prev)); prev=p
                parts.append(pieces_list[k]*(1-prev))
                new.extend(parts)
        yield new

# Test a config in z in [-2a,0]
random.seed(1)
def find_config():
    for _ in range(100000):
        xs=sorted([random.random() for _ in range(3)])
        a=F(xs[0]).limit_denominator(200)
        b=F(xs[1]-xs[0]).limit_denominator(200)
        c=F(xs[2]-xs[1]).limit_denominator(200)
        d=1-a-b-c
        if not (a<=b<=c<=d and a>0 and d<F(1,2)): continue
        u=a-alpha; v=b-a-alpha; w=c-a-b-alpha; z=d-b-c-alpha
        if z<=0 and z>=-2*alpha and w>=-2*alpha and u>0 and v>0 and w>0:
            return a,b,c,d,u,v,w,z
    return None

cfg = find_config()
print("config:", cfg)
a,b,c,d,u,v,w,z = cfg
print(f"a={a} b={b} c={c} d={d}")
print(f"|b+c-d| = {abs(b+c-d)} = {float(abs(b+c-d)):.6f}, alpha={float(alpha):.6f}")
print(f"is |b+c-d|<=alpha? {abs(b+c-d)<=alpha}")

best=None; best_strat=None; nstrat=0
for ms in strategies_abcd(a,b,c,d, Ngrid=14):
    A=alt_sum(ms)
    nstrat+=1
    if best is None or A<best:
        best=A; best_strat=ms
print(f"brute-force min A over {nstrat} strategies (grid 14) = {best} = {float(best):.6f}")
print(f"min A <= alpha? {best<=alpha}")
print(f"best multiset: {sorted(best_strat,reverse=True)}")

# Also test: is the cap |b+c-d| achievable exactly?
target = abs(b+c-d)
close_strats=[]
for ms in strategies_abcd(a,b,c,d, Ngrid=20):
    A=alt_sum(ms)
    if abs(A-target) < F(1,10000):
        close_strats.append((A,ms))
print(f"strategies with A within 1e-4 of |b+c-d|={target}: {len(close_strats)}")
if close_strats:
    print("  example:", close_strats[0])
