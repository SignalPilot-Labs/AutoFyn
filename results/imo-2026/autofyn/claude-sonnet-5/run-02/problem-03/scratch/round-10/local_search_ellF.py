import random
from collections import Counter

def phi(marks_all, total=1.0):
    # marks_all: sorted list of internal cut points in (0,1), full multiset of piece lengths
    pts = [0.0]+sorted(marks_all)+[total]
    pieces = [pts[i+1]-pts[i] for i in range(len(pts)-1)]
    pieces.sort(reverse=True)
    return sum(pieces[i] for i in range(0,len(pieces),2)), pieces

def ladder(n):
    D = 2**(n+1)-1
    vals = [2**(n+1-i)/D for i in range(1,n+2)]
    marks = []
    c=0.0
    for v in vals[:-1]:
        c+=v
        marks.append(c)
    return marks, vals

random.seed(42)
for n in [3,4,5]:
    lb_marks, ladder_vals = ladder(n)
    p1 = ladder_vals[0]
    a_n = p1
    best_global = None
    for restart in range(40):
        # init: xy marks random in (0,1)
        xy = sorted(random.random() for _ in range(n))
        def full_marks(xy): return lb_marks+xy
        curphi,_ = phi(full_marks(xy))
        for it in range(4000):
            i = random.randrange(n)
            step = random.uniform(-1,1)*random.choice([0.2,0.05,0.01,0.002,0.0005])
            newxy = xy[:]
            newxy[i] = min(0.999999, max(0.000001, newxy[i]+step))
            newphi,_ = phi(full_marks(newxy))
            if newphi < curphi:
                xy, curphi = newxy, newphi
        if best_global is None or curphi < best_global[0]:
            best_global = (curphi, xy[:])
    curphi, xy = best_global
    pieces_all = sorted(full := ([0.0]+sorted(lb_marks+xy)+[1.0]))
    # figure out ell(F): fragments of p1 = pieces coming from xy marks that fall within [0,p1]
    xy_sorted = sorted(xy)
    frag_bounds = [0.0]+[m for m in xy_sorted if m < p1]+[p1]
    frags = [frag_bounds[i+1]-frag_bounds[i] for i in range(len(frag_bounds)-1)]
    c = Counter(round(f,6) for f in frags)
    ellF = sum(1 for v,m in c.items() if m%2==1)
    print(f"n={n}: min phi found={curphi:.8f}, a_n={a_n:.8f}, margin={curphi-a_n:.2e}, "
          f"p1-fragments={sorted(frags,reverse=True)}, ellF~{ellF}, num_xy_cuts_in_p1={len(xy_sorted)-sum(1 for m in xy_sorted if m>=p1)}")
