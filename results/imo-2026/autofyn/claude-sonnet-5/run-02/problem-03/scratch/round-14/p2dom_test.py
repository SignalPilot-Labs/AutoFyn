from fractions import Fraction as F
import itertools, random

def A(S):
    S = sorted(S, reverse=True)
    total = F(0)
    for i,x in enumerate(S):
        if i%2==0: total += x
        else: total -= x
    return total

def ladder(n):
    D = 2**(n+1) - 1
    return [F(2**(n+1-i), D) for i in range(1, n+2)]  # p_1..p_{n+1}

def f_target(n):
    D = 2**(n+1)-1
    return F(1, D)  # f(n) = a_n * T with T=1; a_n = 1/D? check c(n)=2^n/(2^{n+1}-1)... 
