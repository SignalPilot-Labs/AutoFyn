from fractions import Fraction as F

def A(multiset):
    s = sorted(multiset, reverse=True)
    total = F(0); sign=1
    for x in s:
        total += sign*x; sign=-sign
    return total

def a_n(n):
    return F(2**n, 2**(n+1)-1)

# Equal pieces closure check
for n in range(0, 8):
    m = n+1
    T = F(1)
    pieces = [T/m]*m
    if m % 2 == 0:
        final = pieces
    else:
        if m == 1:
            final = pieces
        else:
            final = pieces[1:] + [pieces[0]/2, pieces[0]/2]
    Phi = (A(final)+T)/2 if False else None
    # Phi = sum over odd rank = (Total + A)/2 since A = sum odd - sum even, Total=sum odd+sum even
    Aval = A(final)
    Phi = (T + Aval)/2
    an = a_n(n)
    ok = Phi <= an*T
    print(n, m, "Phi=",Phi, "a_n*T=", an*T, "Phi<=a_n*T:", ok, "strict" if Phi<an*T else "")
