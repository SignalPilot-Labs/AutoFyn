import numpy as np

def rand_triangle():
    while True:
        A = np.random.uniform(0.05, np.pi-0.1)
        C = np.random.uniform(0.05, np.pi-0.1)
        B = np.pi - A - C
        if B > 0.05:
            break
    theta = np.random.uniform(0.001, min(B,C)-0.001)
    return A,B,C,theta

for trial in range(5):
    A,B,C,theta = rand_triangle()
    tau = np.tan(theta)
    sA,cA = np.sin(A),np.cos(A)
    sB,cB = np.sin(B),np.cos(B)
    sC,cC = np.sin(C),np.cos(C)

    P1 = sA*tau*(tau*cC - sC)
    Q1 = sA*sC*(tau**2+1) + 2*tau*sB
    R1 = -2*tau**2*sC*cA - tau*sA*sC + sA*cC

    P2 = sA*tau*(tau*cB - sB)
    Q2 = sA*sB*(tau**2+1) + 2*tau*sC
    R2 = -2*tau**2*sB*cA - tau*sA*sB + sA*cB

    D1 = Q1**2 - 4*P1*R1
    D2 = Q2**2 - 4*P2*R2

    U1 = (-Q1 - np.sqrt(D1))/(2*P1)
    U2 = (-Q1 + np.sqrt(D1))/(2*P1)
    V1 = (-Q2 - np.sqrt(D2))/(2*P2)
    V2 = (-Q2 + np.sqrt(D2))/(2*P2)

    def F(U,V):
        return sA*U*V - cA*(U+V) - sA

    def Xi(V):
        m = sA*V - cA
        n = -cA*V - sA - 4
        return P1*n**2 - Q1*n*m + R1*m**2

    Xi_V1 = Xi(V1)
    Xi_V2 = Xi(V2)

    # check Xi(V) = P1*(F(U1,V)-4)(F(U2,V)-4)
    check1 = P1*(F(U1,V1)-4)*(F(U2,V1)-4)
    print("Xi(V1) vs P1*prod check:", Xi_V1, check1, abs(Xi_V1-check1))

    # a,b decomposition
    c2 = P1 - Q1*sA + R1*sA**2  # not used directly; compute via formula below instead
    # Instead directly extract via symbolic-like numeric fit: Xi(V)=c2 V^2+c1 V+c0
    # compute c2,c1,c0 numerically via finite differences using three V points
    Vs = [0.3, 1.7, -0.5]
    import numpy.linalg as la
    Amat = np.array([[v**2, v, 1] for v in Vs])
    bvec = np.array([Xi(v) for v in Vs])
    c2n,c1n,c0n = la.solve(Amat, bvec)

    a_ = c2n*(Q2**2+D2) - 2*P2*Q2*c1n + 4*P2**2*c0n
    b_ = 2*c2n*Q2 - 2*P2*c1n

    lhs1 = a_ + b_*np.sqrt(D2)
    rhs1 = 4*P2**2*Xi_V1
    lhs2 = a_ - b_*np.sqrt(D2)
    rhs2 = 4*P2**2*Xi_V2
    print("check a+b*sqrt(D2) vs 4P2^2 Xi(V1):", lhs1, rhs1)
    print("check a-b*sqrt(D2) vs 4P2^2 Xi(V2):", lhs2, rhs2)

    aa_bb = a_**2 - b_**2*D2
    prodXi = 16*P2**4*Xi_V1*Xi_V2
    print("a^2-b^2D2 vs 16P2^4 Xi(V1)Xi(V2):", aa_bb, prodXi)
    print("---")
