from fractions import Fraction as F
import itertools

def A(ms):
    s=sorted(ms, reverse=True)
    tot=F(0)
    for i,v in enumerate(s):
        tot += v if i%2==0 else -v
    return tot

def qmax(j):
    # largest integer <= j+1 -- but must match parity? We'll just enumerate all valid q separately per parity branch
    return j+1

results_checked=0
violations=[]
tau1=F(11)
for m in range(1,11):
    tau=[tau1/F(2)**i for i in range(m)]
    taum=tau[-1]
    idxs=list(range(m))
    for r in range(0, m+1):
        for combo in itertools.combinations(idxs, r):
            X=[tau[i] for i in combo]
            TotX=sum(X)
            j=r
            qmx=j+1
            for q in range(1, qmx+1):
                if q%2==0: 
                    continue # only test odd branch here matching sec 5.7 (q odd)
                v = (taum+TotX)/F(q)
                if v>tau1:
                    continue # sub-case b, tested separately
                # sub-case a: verify A(X U {v}) >= taum  (eq 5.6)
                val = A(X+[v])
                results_checked+=1
                if val < taum:
                    violations.append((m,combo,q,v,val,taum))

print("checked (q-odd, sub-case a) configs:", results_checked, "violations:", len(violations))
for v in violations[:5]: print(v)

# sub-case (b): q=1, v=tau1, check A(X U {tau1}) >= tau1 - Total(X)
results_checked2=0
violations2=[]
for m in range(1,11):
    tau=[tau1/F(2)**i for i in range(m)]
    idxs=list(range(m))
    for r in range(0, m+1):
        for combo in itertools.combinations(idxs, r):
            X=[tau[i] for i in combo]
            TotX=sum(X)
            val=A(X+[tau1])
            target = tau1-TotX
            results_checked2+=1
            if val<target:
                violations2.append((m,combo,val,target))
print("checked (sub-case b) configs:", results_checked2, "violations:", len(violations2))

# q-even branch: A(X) >= taum for nonempty X
results3=0
violations3=[]
for m in range(1,11):
    tau=[tau1/F(2)**i for i in range(m)]
    taum=tau[-1]
    idxs=list(range(m))
    for r in range(1,m+1):
        for combo in itertools.combinations(idxs,r):
            X=[tau[i] for i in combo]
            results3+=1
            if A(X) < taum:
                violations3.append((m,combo,A(X),taum))
print("checked (q-even branch) configs:", results3, "violations:", len(violations3))
