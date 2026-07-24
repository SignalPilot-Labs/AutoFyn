from fractions import Fraction as F

def A(vals):
    s = sorted(vals, reverse=True)
    a = F(0); sign=1
    for v in s:
        a += sign*v; sign=-sign
    return a

def phi(vals):
    return (sum(vals)+A(vals))/2

p1,p2,p3,p4,p5 = F(2933,10000),F(2514,10000),F(2131,10000),F(1338,10000),F(1085,10000)
T = p1+p2+p3+p4+p5
p1,p2,p3,p4,p5 = [x/T for x in (p1,p2,p3,p4,p5)]
T = p1+p2+p3+p4+p5
a4 = F(16,31)
print("normalized:",p1,p2,p3,p4,p5,"sum",T)

# Construction: split p1 into 3 fragments: one exactly equal to p3 (pinned tie), remaining two equal to each other
# p1 = p3 + 2r  => r = (p1-p3)/2
r = (p1-p3)/2
assert r>0
frag_tie = p3
frag_pair = r
print("p1 frags:", frag_tie, frag_pair, frag_pair, "sum check:", frag_tie+2*frag_pair==p1)

# split p2 into two fragments a,b with a+b=p2, chosen so that a>p4>b (a at odd rank, b at even rank among remaining)
# from the numeric probe: p2 frags approx (0.1405,0.1109). Let's just pick a>p4, b<p4, a+b=p2
# need a in (p4, p2), b=p2-a in (0,p4) i.e. a in (p2-p4, p2)
lo = max(p4, p2-p4)
hi = p2
assert lo<hi
a = (lo+hi)/2
b = p2-a
print("p2 frags a,b:",a,b, "a>p4>b:", a>p4>b)

final = [frag_tie, frag_pair, frag_pair, a, b, p3, p4, p5]
# p3 untouched original value also included (frag_tie ties with it)
Phi = phi(final)
predicted = (T + p2 - p4 - p5)/2   # per our derivation: p1,p3 contribute 0 net; p2 contributes +p2; p4,p5 contribute - each
print("Phi actual=",Phi,float(Phi), " predicted=",predicted,float(predicted), "equal:",Phi==predicted)
print("vs a4T:", float(Phi), float(a4), Phi<a4)
print("sorted final:", sorted([float(x) for x in final], reverse=True))
