from fractions import Fraction as F

def A(pieces):
    """Alternating advantage sum of sorted-descending pieces."""
    s = sorted(pieces, reverse=True)
    return sum((F(1) if i%2==0 else F(-1))*v for i,v in enumerate(s))

# ---- Balanced config (n=3): (1/4,1/4,1/4,1/4), w=1/4 ----
# n odd -> sliver-only: cut sliver s from each of n pieces
w = F(1,4); s = F(1,1000)
# 1 untouched w, n=3 of (w-s), n=3 of s
pieces = [w] + [w-s]*3 + [s]*3
print("balanced n=3 sliver-only A =", A(pieces), "= 2s?", A(pieces)==2*s)

# ---- Balanced config (n=4): (1/5,..,1/5), w=1/5 ----
# n even -> bisect one (w/2,w/2) + sliver from n-1=3 pieces
w = F(1,5); s = F(1,1000)
pieces = [w] + [w-s]*3 + [s]*3 + [w/2, w/2]  # 1 untouched, 3 (w-s), 3 s, 2 (w/2)
print("balanced n=4 bisect+sliver A =", A(pieces), "= 2s?", A(pieces)==2*s)

# ---- Balanced n=5 sliver-only ----
w = F(1,6); s = F(1,1000)
pieces = [w] + [w-s]*5 + [s]*5
print("balanced n=5 sliver-only A =", A(pieces), "= 2s?", A(pieces)==2*s)

# ---- Balanced n=2 (bisect+sliver, n even) ----
w = F(1,3); s = F(1,1000)
pieces = [w] + [w-s]*1 + [s]*1 + [w/2, w/2]
print("balanced n=2 bisect+sliver A =", A(pieces), "= 2s?", A(pieces)==2*s, "alpha(2)=1/7", F(1,7))

# ---- Two-dyadic n=3: (0.5, 0.25, 0.125, 0.125) ----
# Strategy: cut 0.5 -> (0.25,0.25) [1 mark]; cut one 0.25 -> (0.125,0.125) [1 mark]; cut sliver from one 0.125 [1 mark]
p = [F(1,2), F(1,4), F(1,8), F(1,8)]
s = F(1,1000)
# after cuts: 0.25,0.25 (from 0.5), original 0.25, 0.125,0.125 (from cut 0.25), original 0.125, (s, 0.125-s) from sliver cut
pieces = [F(1,4), F(1,4), F(1,4), F(1,8), F(1,8), F(1,8), F(1,8)-s, s]
print("two-dyadic n=3 strategy A =", A(pieces), "= 2s?", A(pieces)==2*s, "alpha(3)=1/15", F(1,15))

# ---- Dominant n=3: (L, t, t, t), L>4/5, cut L into 4 equal ----
for L in [F(9,10), F(5,6), F(4,5)]:
    t = (1 - L)/3
    pieces = [L/4]*4 + [t]*3
    a = A(pieces)
    print(f"dominant L={float(L):.3f}: cut-4-equal A={a}={float(a):.5f}, t={t}={float(t):.5f}, alpha(3)={F(1,15)}, A<alpha? {a < F(1,15)}, L/4>t? {L/4 > t}")

# ---- Verify the odd/even sign pattern claim for balanced general ----
# n odd sliver-only: pieces = [w] + [w-s]*n + [s]*n, total 2n+1
def balanced_sliver_only_A(n, w, s):
    pieces = [w] + [w-s]*n + [s]*n
    return A(pieces)
for n in [1,3,5,7,2,4,6]:
    w = F(1, n+1); s=F(1,10**6)
    print(f"  n={n} odd={n%2==1}: balanced sliver-only A = {balanced_sliver_only_A(n,w,s)}, 2s={2*s}")

def balanced_bisect_sliver_A(n, w, s):
    # n even: bisect one (w/2,w/2), sliver from n-1 pieces
    pieces = [w] + [w-s]*(n-1) + [s]*(n-1) + [w/2, w/2]
    return A(pieces)
for n in [2,4,6]:
    w = F(1, n+1); s=F(1,10**6)
    print(f"  n={n} even: balanced bisect+sliver A = {balanced_bisect_sliver_A(n,w,s)}, 2s={2*s}")

# alpha check
for n in [1,2,3,4,5]:
    print(f"  n={n}: alpha(n)=1/{2**(n+1)-1} = {F(1,2**(n+1)-1)}")
