from fractions import Fraction as F
def A(vals):
    s=sorted(vals,reverse=True)
    a=F(0); sign=1
    for v in s:
        a+=sign*v; sign=-sign
    return a
# try to make A very negative
S = [10] + [1]*9  # sorted desc
print(sorted(S,reverse=True), A([F(x) for x in S]))
S2 = [10,9,1,1,1,1,1,1,1,1]
print(S2, A([F(x) for x in S2]))
S3 = [10,10,1,1,1,1,1,1,1,1]
print(S3, A([F(x) for x in S3]))
S4=[10]+[9]*20
print(S4[:5],'...',len(S4), A([F(x) for x in S4]))
