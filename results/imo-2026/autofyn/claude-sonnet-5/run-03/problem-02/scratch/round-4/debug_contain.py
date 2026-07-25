import numpy as np

def angle(v1,v2):
    n1=np.linalg.norm(v1); n2=np.linalg.norm(v2)
    c = np.dot(v1,v2)/(n1*n2)
    c = max(-1,min(1,c))
    return np.arccos(c)

def inside_triangle(P,X,Y,Z):
    def sign(p1,p2,p3):
        return (p1[0]-p3[0])*(p2[1]-p3[1])-(p2[0]-p3[0])*(p1[1]-p3[1])
    d1=sign(P,X,Y); d2=sign(P,Y,Z); d3=sign(P,Z,X)
    has_neg = (d1<0) or (d2<0) or (d3<0)
    has_pos = (d1>0) or (d2>0) or (d3>0)
    return not (has_neg and has_pos)

a,b,cc=2.0,0.6,0.8
A=np.array([0,0.]); B=np.array([a,0.]); C=np.array([b,cc])
M=(A+B)/2; N=(A+C)/2
t1,t2,beta = 0.92281377,0.21180624,0.22671518
def K_of(t1,beta): return B + t1*np.array([-np.cos(beta), np.sin(beta)])
def L_of(t2,beta):
    AC=A-C; ell=np.linalg.norm(AC); d=AC/ell
    R=np.array([[np.cos(beta),-np.sin(beta)],[np.sin(beta),np.cos(beta)]])
    return C + t2*(R@d)
K=K_of(t1,beta); L=L_of(t2,beta)
print("K",K,"L",L)
print("M",M,"N",N)
print("inside BMC:", inside_triangle(K,B,M,C))
print("inside BNC:", inside_triangle(L,B,N,C))
print("angleABC deg", np.degrees(angle(A-B,C-B)))
print("beta deg", np.degrees(beta))
