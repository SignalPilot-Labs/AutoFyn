import math
from sympy import factorint

def gcd(a,b):
    return math.gcd(a,b)

def build_seq(a1, N):
    a = [None, a1]
    while len(a) <= N:
        prev = a[-1]
        cand = prev + 1
        while True:
            ok = True
            for i in range(1, len(a)):
                if gcd(cand, a[i]) == 1:
                    ok = False
                    break
            if ok:
                a.append(cand)
                break
            cand += 1
    return a  # 1-indexed, a[0] unused

def primeset(m):
    return set(factorint(m).keys())

def analyze(a1, S0, A, B, N):
    a = build_seq(a1, N)
    rho = {}
    for n in range(1, N+1):
        rho[n] = primeset(a[n]) & S0

    # occurrences
    X_A = [n for n in range(1,N+1) if rho[n]==A]
    X_B = [n for n in range(1,N+1) if rho[n]==B]

    results = []
    # for each A occurrence n (skip n=1), look at outside-core primes of a_n
    for n in X_A:
        if n==1: continue
        Pn = primeset(a[n])
        outside = Pn - S0
        for qprime in outside:
            e = 0
            tmp = a[n]
            while tmp % qprime == 0:
                tmp//=qprime
                e+=1
            c = tmp
            branch_a = (c <= a[n-1])
            branch_b_i = None
            if not branch_a:
                # must find earlier i with P(a_i) cap P(a_n) = {qprime}
                for i in range(1, n):
                    Pi = primeset(a[i])
                    if Pi & Pn == {qprime}:
                        branch_b_i = i
                        break
            results.append((n, qprime, branch_a, branch_b_i, rho.get(branch_b_i) if branch_b_i else None))
    return a, rho, X_A, X_B, results

if __name__ == "__main__":
    print("=== a1=4807 ===")
    S0 = {2,3,5,11,19,23}
    A = frozenset({3,5,19})
    B = frozenset({2,11})
    a, rho, X_A, X_B, results = analyze(4807, S0, A, B, 2000)
    for r in results[:60]:
        print(r)
    print("num A occ:", len(X_A), "num B occ:", len(X_B))
