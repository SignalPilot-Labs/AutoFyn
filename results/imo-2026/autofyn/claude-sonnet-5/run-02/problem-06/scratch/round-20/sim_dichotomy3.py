from sim_dichotomy import build_seq, primeset

def scan_branch_b(a1, N):
    a = build_seq(a1, N)
    for n in range(2, N+1):
        Q = primeset(a[1])
        Pn = primeset(a[n])
        outside = Pn - Q
        for qprime in outside:
            e=0; tmp=a[n]
            while tmp % qprime==0:
                tmp//=qprime; e+=1
            c = tmp
            if c <= a[n-1]:
                continue
            for i in range(1,n):
                Pi = primeset(a[i])
                if Pi & Pn == {qprime}:
                    return (a1, n, qprime, i)
    return None

found_any = []
for a1 in list(range(4,60)) :
    r = scan_branch_b(a1, 400)
    if r:
        found_any.append(r)
print("found branch-b instances (small a1, N=400, core=Q):")
for f in found_any:
    print(f)
print("count", len(found_any), "out of", len(range(4,60)))
