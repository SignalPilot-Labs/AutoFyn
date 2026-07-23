import sympy

def gen_seq(a1, n_terms):
    seq=[a1]
    while len(seq)<n_terms:
        x = seq[-1]+1
        while True:
            ok=True
            for a in seq:
                if sympy.gcd(x,a)==1:
                    ok=False
                    break
            if ok:
                seq.append(x)
                break
            x+=1
    return seq

def rad(x):
    return frozenset(sympy.primefactors(x))

if __name__=="__main__":
    import sys
    a1=int(sys.argv[1])
    n=int(sys.argv[2])
    seq=gen_seq(a1,n)
    for i,a in enumerate(seq,1):
        print(i,a,sorted(rad(a)))
