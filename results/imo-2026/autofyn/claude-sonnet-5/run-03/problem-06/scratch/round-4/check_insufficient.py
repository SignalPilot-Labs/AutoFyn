import math
from sympy import primefactors

def gen_sequence(a1, num_terms):
    a = [a1]
    while len(a) < num_terms:
        an = a[-1]
        m = an + 1
        while True:
            ok = True
            for ai in a:
                if math.gcd(m, ai) == 1:
                    ok = False
                    break
            if ok:
                a.append(m)
                break
            m += 1
    return a

def bad_pairs_for_Q(a, Q):
    Qset=set(Q)
    facs=[set(primefactors(x))&Qset for x in a]
    bad=0
    n=len(a)
    for i in range(n):
        for j in range(i+1,n):
            if not (facs[i]&facs[j]):
                bad+=1
    return bad

a1=35
a=gen_sequence(a1, 300)
print("rad(a1) alone:", bad_pairs_for_Q(a, primefactors(a1)))
print("rad(a1)+{2}:", bad_pairs_for_Q(a, primefactors(a1)+[2]))
print("rad(a1)+{2,3}:", bad_pairs_for_Q(a, primefactors(a1)+[2,3]))
print("rad(a1)+{2,3} at n=1000 check subset", a[:20])
