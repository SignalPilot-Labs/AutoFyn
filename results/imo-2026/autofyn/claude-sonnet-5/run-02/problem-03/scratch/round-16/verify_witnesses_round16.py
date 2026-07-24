from fractions import Fraction as F
import sys
sys.path.insert(0,'/tmp/round-16')
from verify_altgapcross_fixed2 import construct, A_of

# n=3 witness
vals = [F(4468,10001), F(2591,10001), F(2251,10001), F(691,10001)]
res = construct(vals, 2)
print("n=3 witness construct:", res)
final, gap_sum, jprime = res
A_direct = A_of(final)
tail = vals[4:]
A_tail = A_of(tail)
predicted = gap_sum + (F(-1)**jprime)*A_tail
print("A_direct=", A_direct, "predicted=", predicted)
T = sum(vals)
Phi = (T + A_direct)/2
a3T = F(8,15)*T
print("Phi=", Phi, float(Phi), "a3T=", float(a3T), "closed:", Phi < a3T)
