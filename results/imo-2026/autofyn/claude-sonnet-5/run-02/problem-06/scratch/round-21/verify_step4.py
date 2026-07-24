import sympy

def omega(n):
    return len(sympy.factorint(n))

# K0=4 branch
print("K0=4 branch:")
for k in range(1, 30):
    K = 4 + 3*k
    w = omega(K)
    lhs = 7*k
    rhs = 2**(w+2)
    ok = lhs >= rhs
    if not ok or k<=5:
        print(f"k={k} K={K} omega(K)={w} 7k={lhs} 2^(w+2)={rhs} holds={ok}")

print("K0=5 branch:")
for k in range(1, 30):
    K = 5 + 3*k
    w = omega(K)
    lhs = 7*k
    rhs = 2**(w+2)
    ok = lhs >= rhs
    if not ok or k<=5:
        print(f"k={k} K={K} omega(K)={w} 7k={lhs} 2^(w+2)={rhs} holds={ok}")
