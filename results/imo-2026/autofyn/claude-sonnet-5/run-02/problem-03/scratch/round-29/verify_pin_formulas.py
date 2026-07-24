import random
from fractions import Fraction as F

def A(sorted_desc):
    s=F(0)
    for i,v in enumerate(sorted_desc):
        s += v if i%2==0 else -v
    return s

def direct_phi(frags):
    T=sum(frags)
    sd=sorted(frags,reverse=True)
    return (T+A(sd))/2

def rand_p(maxden=300):
    vals=[random.randint(1,maxden) for _ in range(5)]
    vals.sort(reverse=True)
    return [F(v) for v in vals]

random.seed(1)
bad=0
for _ in range(5000):
    p=random.choice([rand_p()])
    p1,p2,p3,p4,p5=p
    T=sum(p)
    # Chamber 1: bisect p1,p4; pin p2->p3 (cut p2 into p3, p2-p3), need p2>=p3 (always true, sorted)
    frags1 = [p1/2,p1/2, p4/2,p4/2, p3, p2-p3, p3, p5]
    phi1_direct = direct_phi(frags1)
    phi1_formula = (T + abs(p2-p3-p5))/2
    if phi1_direct != phi1_formula:
        print("mismatch1", p, phi1_direct, phi1_formula); bad+=1

    # Chamber 2: bisect p1,p2; pin p3->p4
    frags2 = [p1/2,p1/2, p2/2,p2/2, p4, p3-p4, p4, p5]
    phi2_direct = direct_phi(frags2)
    phi2_formula = (T + abs(p3-p4-p5))/2
    if phi2_direct != phi2_formula:
        print("mismatch2", p, phi2_direct, phi2_formula); bad+=1

    # Chamber 3: bisect p1,p3; pin p2->p4
    frags3 = [p1/2,p1/2, p3/2,p3/2, p4, p2-p4, p4, p5]
    phi3_direct = direct_phi(frags3)
    phi3_formula = (T + abs(p2-p4-p5))/2
    if phi3_direct != phi3_formula:
        print("mismatch3", p, phi3_direct, phi3_formula); bad+=1

print("bad:", bad, "out of 5000 (x3 formulas)")
