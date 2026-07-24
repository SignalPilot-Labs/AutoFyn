from fractions import Fraction as F

def A(S):
    S = sorted(S, reverse=True)
    return sum((-1)**i * S[i] for i in range(len(S)))

def ladder(n):
    D = 2**(n+1)-1
    return [F(2**(n+1-i), D) for i in range(1, n+2)]  # p[0]=p1 ... p[n]=p_{n+1}

# Verify §5.3 formula: S_j = {x, p_j} ∪ T,  x=p1-p_j, T={p2..p_{n+1}} untouched
# check A(S_j) >= f(n), strict for n>=3, for j=3..n+1
for n in range(1,8):
    p = ladder(n)
    fn = F(1, 2**(n+1)-1)
    T = p[1:]
    for j in range(3, n+2):  # j from 3 to n+1 (1-indexed)
        pj = p[j-1]
        x = p[0]-pj
        S = [x, pj] + T
        Aj = A(S)
        rel = "==" if Aj==fn else (">" if Aj>fn else "<")
        if Aj < fn:
            print("VIOLATION", n, j, Aj, fn)
    print(n, "done, min over j:", min(A([p[0]-p[j-1], p[j-1]]+T) for j in range(3,n+2)) if n>=2 else None, "target", fn)
