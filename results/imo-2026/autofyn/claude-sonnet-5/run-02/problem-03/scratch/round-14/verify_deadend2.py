from fractions import Fraction as F

def a_n(n):
    return F(2**n, 2**(n+1)-1)

for n in range(1,15):
    an = a_n(n); anm1 = a_n(n-1)
    coeff = (an-anm1)/(F(1,2)-anm1)
    print(n, coeff, an, coeff==an)
