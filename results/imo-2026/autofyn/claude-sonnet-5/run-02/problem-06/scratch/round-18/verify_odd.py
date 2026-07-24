import math

def gcd(a,b):
    return math.gcd(a,b)

def gen(a1, N):
    seq=[a1]
    used=set([a1])
    while len(seq)<N:
        n=seq[-1]
        c=n+1
        while True:
            if c not in used and any(gcd(c,x)>1 for x in seq):
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
    seq = gen(a1, 4000)
    Q = P(a1)
    print("a1=",a1,"Q=",Q)
    # base type tau(n) = P(a_n) & Q
    types = [P(x)&Q for x in seq]
    # print first 20 types
    print([sorted(t) for t in types[:20]])
    # count fraction divisible by 3 (if 3 in Q)
    if 3 in Q:
        frac3 = sum(1 for x in seq if x%3==0)/len(seq)
        print("frac div by 3:", frac3)
    if 5 in Q:
        frac5 = sum(1 for x in seq if x%5==0)/len(seq)
        print("frac div by 5:", frac5)
    # check period-4 alternation pattern in types, find indices where type == {3} vs {5}
    idx3 = [i+1 for i,t in enumerate(types) if t=={3}]
    idx5 = [i+1 for i,t in enumerate(types) if t=={5}]
    print("count type{3}:", len(idx3), "first 10:", idx3[:10])
    print("count type{5}:", len(idx5), "first 10:", idx5[:10])
    print()
