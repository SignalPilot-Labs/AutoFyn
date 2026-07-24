from sympy import isprime, primerange, gcd

# (c) Verify the CRT construction: q=40153, k=3335, K=10010
K = 2*5*7*11*13
print("K =", K, "K mod 3 =", K%3)  # should be K0=5 branch i.e. K0=5 requires K = K0+3k => K mod 3 = K0 mod 3 = 2
q = 40153
print("q prime?", isprime(q))
print("q mod 30030 =", q % 30030)

k = 3335
K0 = 5
Kcheck = K0 + 3*k
print("K0+3k =", Kcheck, "expected K=10010:", Kcheck==10010)

n0_formula = (2*q+1)//3 if q%3==1 else (q+1)//3
print("q mod 3 =", q%3)
n0 = n0_formula
print("n0 =", n0)

n = n0 + k*q
print("n =", n)

# a_n = 3(q+n-1), a_n+2 = 3(q+n)-1
N = 3*(q+n) - 1
print("N = a_n+2 =", N)
print("N == q*K ?", N == q*K, N, q*K)

# find minimal witness offset: candidates i=2,...,n give m = q+i-1, i.e. m ranges q+1,...,q+n-1
# witness means gcd(m, N) == 1 (m = q+i-1, a_i = 3(q+i-1)=3m, gcd(N,3m); N is coprime to 3 since Case b assumed... let's just check gcd(N,a_i))
found = None
for i in range(2, 30):
    m = q + i - 1
    a_i = 3*m
    g = gcd(N, a_i)
    if g == 1:
        found = i
        break
print("minimal witness i (from i=2):", found, "offset from q+1:", (q+found-1) - (q+1) if found else None)

# also check g(K) Jacobsthal-style: find max run of consecutive integers near q+1 sharing factor with K
# integers q+1 .. q+m
start = q+1
runlen = 0
maxrun = 0
run_start = None
for x in range(start, start+30):
    if gcd(x, K) > 1:
        if runlen == 0:
            run_start = x
        runlen += 1
        maxrun = max(maxrun, runlen)
    else:
        runlen = 0
print("first 30 integers from q+1, gcd with K status:")
for x in range(start, start+15):
    print(x, gcd(x,K))
