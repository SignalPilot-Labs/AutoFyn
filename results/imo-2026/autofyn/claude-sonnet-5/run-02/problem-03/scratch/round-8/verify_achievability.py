from fractions import Fraction as F

def A(ms):
    s=sorted(ms, reverse=True)
    tot=F(0)
    for i,v in enumerate(s):
        tot += v if i%2==0 else -v
    return tot

def ladder(n):
    D = 2**(n+1)-1
    return [F(2**(n+1-i), D) for i in range(1, n+2)]

for n in range(1,10):
    p = ladder(n)
    tail = p[1:]  # p2..p_{n+1}
    if n==1:
        Fstar = [p[0]]  # tail={p2}
    else:
        Fstar = p[1:n] + [p[-1], p[-1]]  # p2..pn once, p_{n+1} twice
    assert sum(Fstar)==p[0], (n, sum(Fstar), p[0])
    val = A(Fstar+tail)
    a_n = F(1, 2**(n+1)-1)
    n_cuts = len(Fstar)-1
    print(n, "A=",val, "a_n=",a_n, "match" if val==a_n else "MISMATCH", "cuts=",n_cuts, "budget n=",n)
