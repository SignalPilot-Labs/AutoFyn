"""
Exact verification for IMO Problem 4 (Shan-Yu / Mulan triangle-cutting game).

Claimed answer:  Mulan can guarantee victory in finitely many steps
                 iff theta = 180/n degrees for some integer n >= 2.

Model (proved equivalent to the game in problem4_solution.md, Setup):
  state = unordered triple of positive reals summing to 180;
  Mulan destroys an angle alpha choosing x in (0, alpha); pieces are
      T1 = (x, beta, 180-beta-x),   T2 = (alpha-x, gamma, beta+x);
  Shan-Yu keeps one piece. Mulan wins when the state contains theta exactly.

Protocols (all exact arithmetic; no floating-point equality tests):
  1. Lattice fixpoint: solve EVERY rational instance (angles = integers summing
     to N, theta = t units) by least-fixpoint reachability, for all N <= NMAX,
     all t. Check:  t|N  -> Mulan wins from every state;
                    t!|N -> Mulan wins exactly from states containing a
                            positive multiple of t.
  2. Mulan's explicit strategy (Lemmas 1-2) for theta=180/n, n=2..NSTRAT:
     exact Fraction / Q(sqrt2) arithmetic, exhaustive Shan-Yu branching,
     random + adversarial starts; assert victory on every branch within n cuts.
  3. Shan-Yu's closure (Lemma 3) for theta with 180/theta not an integer,
     rational AND irrational (Q(sqrt2)): random triples in N with random plus
     ALL "critical" cuts (those putting a multiple of theta in a piece);
     assert some piece stays multiple-free.

Full-scale results recorded in problem4_verification.md (runs of 2026-07-22):
  Protocol 1: ALL CHECKS PASSED for N=6..52, all t.
  Protocol 2: all branches win in <= n cuts, n=2..12.
  Protocol 3: 5,476,840 cut instances, closure never violated.
Defaults below are scaled down to finish in ~1 minute; raise NMAX etc. to
reproduce the full runs.
"""
from fractions import Fraction as F
import random

NMAX = 30      # Protocol 1: full run used 52
NSTRAT = 8     # Protocol 2: full run used 12
NTRIALS = 60   # Protocol 2 starts per n / Protocol 3 triples per theta (full: 400 / 3000)

random.seed(20260722)

# ---------------------------------------------------------------- Q(sqrt2)
class Q2:
    """Exact numbers p + q*sqrt(2), p,q rational."""
    __slots__ = ('p', 'q')
    def __init__(self, p, q=0): self.p = F(p); self.q = F(q)
    def __add__(s, o): o = q2(o); return Q2(s.p+o.p, s.q+o.q)
    def __radd__(s, o): return s + o
    def __sub__(s, o): o = q2(o); return Q2(s.p-o.p, s.q-o.q)
    def __rsub__(s, o): return q2(o) - s
    def __mul__(s, o): o = q2(o); return Q2(s.p*o.p+2*s.q*o.q, s.p*o.q+s.q*o.p)
    def __rmul__(s, o): return s*o
    def __eq__(s, o): o = q2(o); return s.p == o.p and s.q == o.q
    def __hash__(s): return hash((s.p, s.q))
    def __float__(s): return float(s.p) + float(s.q)*2**0.5
    def _sign(s):
        # exact sign of p + q*sqrt(2)
        if s.q == 0: return (s.p > 0) - (s.p < 0)
        if s.p == 0: return (s.q > 0) - (s.q < 0)
        if s.p > 0 and s.q > 0: return 1
        if s.p < 0 and s.q < 0: return -1
        d = s.p*s.p - 2*s.q*s.q          # sign(p+q√2) = sign(p)*sign(p²−2q²) here
        return (1 if s.p > 0 else -1) * ((d > 0) - (d < 0))
    def __lt__(s, o): return (s - q2(o))._sign() < 0
    def __le__(s, o): return (s - q2(o))._sign() <= 0
    def __gt__(s, o): return (s - q2(o))._sign() > 0
    def __ge__(s, o): return (s - q2(o))._sign() >= 0
def q2(x): return x if isinstance(x, Q2) else Q2(x)

def children(alpha, beta, gamma, x):
    return (x, beta, q2(180)-beta-x), (alpha-x, gamma, beta+x)

# ---------------------------------------------------------------- Protocol 1
def solve_lattice(N, t):
    states = [(a, b, N-a-b) for a in range(1, N-1)
              for b in range(a, N) if N-a-b >= b]
    stset = set(states)
    moves = {}
    for s in states:
        mv = []
        for idx in range(3):
            alpha = s[idx]
            beta, gamma = [s[j] for j in range(3) if j != idx]
            for x in range(1, alpha):
                T1 = tuple(sorted((x, beta, N-beta-x)))
                T2 = tuple(sorted((alpha-x, gamma, beta+x)))
                assert T1 in stset and T2 in stset
                mv.append((T1, T2))
        moves[s] = mv
    W = set(s for s in states if t in s)
    changed = True
    while changed:
        changed = False
        for s in states:
            if s not in W and any(a in W and b in W for (a, b) in moves[s]):
                W.add(s); changed = True
    return states, W

def protocol1():
    for N in range(6, NMAX + 1):
        for t in range(1, N):
            states, W = solve_lattice(N, t)
            if N % t == 0:
                assert len(W) == len(states), (N, t, "Mulan should win everywhere")
            else:
                expect = set(s for s in states if any(x % t == 0 for x in s))
                assert W == expect, (N, t, "winning set != contains-multiple set")
    print(f"Protocol 1 PASSED: all N=6..{NMAX}, all t (t|N -> all states win; "
          f"t!|N -> exactly the multiple-containing states win)")

# ---------------------------------------------------------------- Protocol 2
def mulan_step(A, theta, n):
    A = list(A)
    for i, a in enumerate(A):                        # Lemma 1 case
        k = 2
        while float(k*theta) < 180.001:
            if a == k*theta:
                beta, gamma = [A[j] for j in range(3) if j != i]
                return a, beta, gamma, q2(theta)
            k += 1
    A.sort(key=float)                                # Lemma 2 case
    gamma, beta, alpha = A
    b = int(float(beta) // float(theta)); c = int(float(gamma) // float(theta))
    assert b*theta < beta and beta < (b+1)*theta     # floors exact (no multiples)
    assert c*theta < gamma and gamma < (c+1)*theta
    assert b + c <= n - 2, (A, b, c, n)              # Lemma 2 claim
    k = b + 1
    x = k*theta - beta
    assert 0 < float(x) < float(alpha) and x != q2(0) and x != alpha
    return alpha, beta, gamma, x

def verify_mulan(A, theta, n, depth):
    if any(a == theta for a in A):
        return 0
    assert depth > 0, ("no win within bound", A)
    alpha, beta, gamma, x = mulan_step(A, theta, n)
    T1, T2 = children(alpha, beta, gamma, x)
    for T in (T1, T2):
        assert all(float(t) > 0 for t in T) and sum(T, q2(0)) == q2(180)
    return 1 + max(verify_mulan(T1, theta, n, depth-1),
                   verify_mulan(T2, theta, n, depth-1))

def rand_tri_rat():
    while True:
        a = F(random.randint(1, 178*12), 12); b = F(random.randint(1, 178*12), 12)
        if float(a+b) < 179.5:
            return [q2(a), q2(b), q2(F(180)-a-b)]

def rand_tri_irr():
    while True:
        a = Q2(F(random.randint(1, 100)), F(random.randint(1, 40), 3))
        b = Q2(F(random.randint(1, 100)), F(-random.randint(1, 40), 7))
        if 0.5 < float(a) < 178 and 0.5 < float(b) < 178 and float(a)+float(b) < 179:
            return [a, b, q2(180)-a-b]

def protocol2():
    for n in range(2, NSTRAT + 1):
        theta = Q2(F(180, n))
        for trial in range(NTRIALS):
            A = rand_tri_rat() if trial % 2 == 0 else rand_tri_irr()
            steps = verify_mulan(A, theta, n, depth=n+2)
            assert steps <= n
        eps = Q2(F(1, 997))
        for A in ([q2(60)]*3,
                  [theta+eps, theta-eps, q2(180)-2*theta],
                  [q2(179)-eps, eps, q2(1)]):
            if all(float(t) > 0 for t in A) and sum(A, q2(0)) == q2(180):
                verify_mulan(A, theta, n, depth=n+2)
        print(f"Protocol 2: n={n} (theta=180/{n}) — every Shan-Yu branch loses in <= {n} cuts")

# ---------------------------------------------------------------- Protocol 3
def protocol3():
    thetas = [q2(F(v)) for v in (72, 80, 100, 40, 135, 7, 179)] + \
             [Q2(0, 45), Q2(10, 20), Q2(0, 1)]      # 45*sqrt2, 10+20*sqrt2, sqrt2
    checked = 0
    for theta in thetas:
        mults = set(); k = 1
        while float(k*theta) < 180 - 1e-9:
            mults.add(k*theta); k += 1
        assert q2(180) not in set(k2*theta for k2 in range(1, 400)
                                  if float(k2*theta) < 180.5)   # theta does not divide 180
        free = lambda T: all(a not in mults for a in T)
        done = 0
        while done < NTRIALS:
            A = rand_tri_rat() if done % 2 == 0 else rand_tri_irr()
            if not free(A):
                continue
            done += 1
            for idx in range(3):
                alpha = A[idx]
                others = [A[j] for j in range(3) if j != idx]
                for (beta, gamma) in (others, others[::-1]):
                    xs = [alpha*F(random.randint(1, 999), 1000) for _ in range(3)]
                    for m in mults:
                        xs += [m, alpha-m, m-beta, q2(180)-beta-m]  # all critical cuts
                    for x in xs:
                        if 0 < float(x) < float(alpha) and x != q2(0) and x != alpha:
                            T1, T2 = children(alpha, beta, gamma, x)
                            assert free(T1) or free(T2), (float(theta), A, x)
                            checked += 1
        print(f"Protocol 3: theta={float(theta):9.4f} — closure held on all cuts")
    print(f"Protocol 3 PASSED: {checked} exact cut instances, zero violations")

if __name__ == '__main__':
    protocol1()
    protocol2()
    protocol3()
    print("ALL PROTOCOLS PASSED — answer verified: Mulan wins iff theta = 180/n, n >= 2")
