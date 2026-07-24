from fractions import Fraction as F
import random

def f_of(n): return F(1, 2**(n+1)-1)
def ladder(n):
    fn=f_of(n)
    return [F(2)**(n+1-i)*fn for i in range(1,n+2)]
def A(ms):
    s=sorted(ms,reverse=True); tot=F(0); sign=1
    for x in s: tot+=sign*x; sign*=-1
    return tot

n=3
p=ladder(n); p1,p2,p3,p4=p
tail=[p2,p3,p4]
fn=f_of(n)
print("p1,p2,p3,p4",p1,p2,p3,p4,"fn",fn)

random.seed(3)
worst=None
for _ in range(200000):
    a_num = random.randint(1, 4999)
    a = F(a_num,10000)*p2/2  # a in (0,p2/2)
    if 2*a>=p2: continue
    v2max = p2-2*a
    v2_num = random.randint(1,9999)
    v2 = F(v2_num,10000)*v2max
    if v2<=0 or v2>=v2max: continue
    v1 = p1-v2-2*a
    F_ = [v1,v2,a,a]
    val = A(F_+tail)
    if worst is None or val<worst[0]:
        worst=(val,v1,v2,a)
print("worst found:", worst, "target fn=",fn)
