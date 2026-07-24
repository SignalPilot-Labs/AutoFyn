from fractions import Fraction as F
import random

def a_n(n):
    return F(2**n, 2**(n+1)-1)

random.seed(5)
# Dead end 1: threshold from peel+IH is p2 >= a_n*T/2 (exactly)
# derive algebraically: bound = p2 + a_{n-1}(T-2p2) <= a_n T
# solve for p2: p2*(1-2a_{n-1}) <= (a_n - a_{n-1})*T
# => p2 >= (a_n-a_{n-1})/(1-2a_{n-1}) * T   [inequality flips since 1-2a_{n-1}<0]
for n in range(1,15):
    an = a_n(n); anm1 = a_n(n-1)
    coeff = (an-anm1)/(1-2*anm1)
    target = an/2
    print(n, coeff, target, coeff==target)
