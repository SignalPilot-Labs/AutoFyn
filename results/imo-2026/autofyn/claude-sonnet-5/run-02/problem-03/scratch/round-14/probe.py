from fractions import Fraction as F
import itertools, random

def A(S):
    S = sorted(S, reverse=True)
    tot = F(0)
    for i,x in enumerate(S):
        tot += x if i%2==0 else -x
    return tot

def ladder(n):
    D = 2**(n+1)-1
    return [F(2**(n+1-i), D) for i in range(1, n+2)]

def f_target(n):
    return F(1, 2**(n+1)-1)

def legal_splits(piece, max_cuts, denom_choices=8):
    # generate all "legal" splits of piece into 1..max_cuts+1 positive fragments
    # using rational fractions with small denominators for search
    results = [(piece,)]  # 0 cuts
    # random search of compositions
    for cuts in range(1, max_cuts+1):
        parts_count = cuts+1
        for _ in range(30):
            # random composition using random breakpoints
            bp = sorted(random.sample(range(1, denom_choices*parts_count), parts_count-1))
            # build fractions summing to 1 then scale
            cuts_pos = [F(0)] + [F(b, denom_choices*parts_count) for b in bp] + [F(1)]
            frac = [cuts_pos[i+1]-cuts_pos[i] for i in range(len(cuts_pos)-1)]
            results.append(tuple(x*piece for x in frac))
    return results

def legal_refinement(pieces, total_cuts):
    # pieces: list of piece values (like tail pieces p3..p_{n+1})
    # distribute total_cuts cuts among pieces (each piece can get 0..total_cuts cuts)
    # returns a random legal refinement (list of fragments) using AT MOST total_cuts cuts total
    m = len(pieces)
    if m==0:
        return []
    cuts_alloc = [0]*m
    budget = random.randint(0, total_cuts)
    for _ in range(budget):
        cuts_alloc[random.randrange(m)] += 1
    frags = []
    for piece, c in zip(pieces, cuts_alloc):
        frags.extend(legal_splits(piece, c)[-1] if c>0 else (piece,))
        # actually need to pick one split with exactly c cuts; simplify:
    return frags

def one_split(piece, cuts):
    if cuts==0:
        return (piece,)
    parts_count = cuts+1
    bp = sorted(random.sample(range(1, 100*parts_count), parts_count-1))
    cutpos = [0] + bp + [100*parts_count]
    frac = [F(cutpos[i+1]-cutpos[i], 100*parts_count) for i in range(len(cutpos)-1)]
    return tuple(x*piece for x in frac)

def random_legal_refinement(pieces, total_cuts):
    m = len(pieces)
    if m==0:
        return []
    cuts_alloc = [0]*m
    budget = random.randint(0, total_cuts)
    for _ in range(budget):
        cuts_alloc[random.randrange(m)] += 1
    frags = []
    for piece, c in zip(pieces, cuts_alloc):
        frags.extend(one_split(piece, c))
    return frags

random.seed(1)

# Test the ell(F)=2, P!=empty subcase: psi(t*) <= p2 - f(n)
for n in [4,5]:
    lad = ladder(n)
    p1,p2 = lad[0], lad[1]
    tail = lad[2:]  # p3..p_{n+1}
    fn = f_target(n)
    worst = None
    trials=0
    for _ in range(4000):
        # P: pairs summing arbitrary total tau_P < p1 (approx), let's pick tau_P in (0, p1-p2) roughly
        tau_P = F(random.randint(1,50), random.randint(51,300))
        if tau_P <= 0: continue
        tstar = p2 - tau_P
        if tstar <= 0: continue
        # remaining cut budget for G': n - (cuts used on v1,v2 + P). Just try various budgets 0..n
        budget = random.randint(0, n)
        Gp = random_legal_refinement(tail, budget)
        psi = A([tstar]+Gp)  # using Lemma19 identity: A({t*}u P u G') = A(G') + t* - 2*int_0^t* v_G'
        # but let's directly compute via actual multiset {t*} U P U G' is NOT valid since P must be
        # legal fragments of p1 too and pair up; but psi(t*) as DEFINED = A({t*}∪G') per the derived formula
        # (P's presence invisible). So this test literally uses psi(t) := A({t}∪G') formula.
        target = p2 - fn
        trials += 1
        slack = target - psi
        if worst is None or slack < worst[0]:
            worst = (slack, tau_P, tstar, budget, Gp)
    print(n, "trials", trials, "worst slack", worst[0], "at tau_P=",worst[1],"t*=",worst[2],"budget=",worst[3])

print()
print("=== detail worst n=4 case ===")
