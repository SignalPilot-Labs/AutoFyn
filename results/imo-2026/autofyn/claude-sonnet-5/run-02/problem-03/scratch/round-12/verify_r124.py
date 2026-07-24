from fractions import Fraction as F

def A(multiset):
    s = sorted(multiset, reverse=True)
    total = F(0); sign=1
    for x in s:
        total += sign*x; sign=-sign
    return total

p1 = F(177)
p2 = F(6,5)
p3 = F(62,123)
T = p1+p2+p3
print("T=",T, float(T))

# bisect largest twice
half1 = p1/2
final = [half1, half1/2 if False else None]
final = [half1/2, half1/2, p2, p3]  # wait: first bisect p1 into 88.5,88.5 then bisect one of them into 44.25,44.25
first_split = [p1/2, p1/2]
# then bisect largest of the current set: largest is p1/2=88.5 (equal, pick either)
second = [first_split[0]/2, first_split[0]/2]
final = second + [first_split[1]] + [p2, p3]
print(final, sum(final)==T)
Aval = A(final)
Phi = (T+Aval)/2
print("Phi=", Phi, float(Phi))
a2 = F(4,7)
print("a2*T=", a2*T, float(a2*T))
