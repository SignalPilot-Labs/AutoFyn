import math

def gcd(a,b):
    return math.gcd(a,b)

def gen(a1, N):
    seq=[a1]
    used=set([a1])
    while len(seq)<N:
        c=seq[-1]+1
        while True:
            if c not in used and all(gcd(c,x)>1 for x in seq):
                break
            c+=1
        seq.append(c)
        used.add(c)
    return seq

def P(n):
    fs=set()
    d=2
    m=n
    while d*d<=m:
        while m%d==0:
            fs.add(d)
            m//=d
        d+=1
    if m>1:
        fs.add(m)
    return fs

for a1 in [15,45]:
    seq = gen(a1, 3000)
    Q = P(a1)
    print("a1=",a1,"Q=",Q, "seq[:20]=", seq[:20])
    types = [P(x)&Q for x in seq]
    print([sorted(t) for t in types[:24]])
    if 3 in Q:
        frac3 = sum(1 for x in seq if x%3==0)/len(seq)
        print("frac div by 3:", frac3)
    if 5 in Q:
        frac5 = sum(1 for x in seq if x%5==0)/len(seq)
        print("frac div by 5:", frac5)
    idx3 = [i+1 for i,t in enumerate(types) if t=={3}]
    idx5 = [i+1 for i,t in enumerate(types) if t=={5}]
    print("count type{3}:", len(idx3), "first 10:", idx3[:10])
    print("count type{5}:", len(idx5), "first 10:", idx5[:10])
    # diffs of idx5 (fail indices, i.e. type {5} not div by 3)
    print("idx5 diffs:", [idx5[i+1]-idx5[i] for i in range(min(10,len(idx5)-1))])
    print()
