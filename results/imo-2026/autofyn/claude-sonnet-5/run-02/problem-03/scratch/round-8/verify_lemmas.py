from fractions import Fraction as F
import itertools, random

def A(ms):
    s=sorted(ms, reverse=True)
    tot=F(0)
    for i,v in enumerate(s):
        tot += v if i%2==0 else -v
    return tot

def check_identity_54(m, tau1):
    tau=[tau1/F(2)**i for i in range(m)]
    R=sum(tau)
    taum=tau[-1]
    return R+taum == 2*tau1

def check_last_element_bound(taus_idx_list, tau1):
    # taus_idx_list: list of exponents i (0-indexed tau_1..tau_m), X = {tau_1/2^i : i in list}
    pass

ok=True
for m in range(1,9):
    tau1=F(random.randint(1,20))
    if not check_identity_54(m, tau1):
        print("IDENTITY 5.4 FAILS", m, tau1); ok=False
print("Identity 5.4 (R+tau_m=2tau1) holds for m=1..8:", ok)

# Last-Element Bound: for every nonempty subset X of {tau_1,...,tau_m} (m up to 10), A(X) >= min(X)
ok=True
for m in range(1,11):
    tau1=F(7)
    tau=[tau1/F(2)**i for i in range(m)]
    idxs=list(range(m))
    for r in range(1, m+1):
        for combo in itertools.combinations(idxs, r):
            X=[tau[i] for i in combo]
            a=A(X)
            mn=min(X)
            if a < mn:
                print("LAST ELEMENT BOUND FAILS", m, combo, a, mn); ok=False
print("Last-Element Bound holds exhaustively for m<=10:", ok)
