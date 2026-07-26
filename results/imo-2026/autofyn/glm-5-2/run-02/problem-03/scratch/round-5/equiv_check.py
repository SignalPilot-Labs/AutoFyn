from fractions import Fraction
# n=2 (level 3), Branch 2: m=(3,3,1,1)/15, a1=4, R=(4,2,1), total_R=7, alpha=1
a1=4; R=[4,2,1]; total_R=7; alpha=1; M=8
m=[3,3,1,1]  # m1<m2? no, sorted desc: [3,3,1,1], m1=3<a1=4 -> Branch 2
rest=sorted(m+[2,1],reverse=True)  # {a2=2,a3=1} + M-subs
A_rest=sum((-1)**i*v for i,v in enumerate(rest))  # t1-t2+...
A=a1-A_rest
oddsum=sum(rest[i] for i in range(0,len(rest),2))  # t1+t3+t5
rest_total=sum(rest)
print("rest:",rest,"A_rest=",A_rest,"A=",A,"oddsum=",oddsum,"total_R=",total_R)
print("A>=alpha:",A>=alpha," | oddsum<=total_R:",oddsum<=total_R," | (equiv)", (A>=alpha)==(oddsum<=total_R))
# also check the formula A_rest = 2*oddsum - rest_total
print("2*oddsum-rest_total =",2*oddsum-rest_total,"== A_rest",A_rest)
