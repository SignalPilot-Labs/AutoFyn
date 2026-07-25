import sympy as sp
from sympy import symbols, expand, factor, simplify, groebner, Rational

p,q = symbols('p q')
A,P,G = symbols('A P G')
def rot_half(v, t):
    x,y = v; c=(1-t**2); s=2*t
    return (expand(c*x - s*y), expand(s*x + c*y))
BA = (sp.Integer(-1), sp.Integer(0)); CA = (-p,-q)
dir_BK = rot_half(BA, A); dir_BL = rot_half(BA, P)
dir_CL = rot_half(CA, A); dir_CK = rot_half(CA, G)
def cross(u,v): return expand(u[0]*v[1]-u[1]*v[0])
def dot(u,v): return expand(u[0]*v[0]+u[1]*v[1])
W=(p-1,q)
def get_point(d1,d2,W):
    tn=cross(W,d2); td=cross(d1,d2)
    return expand(td+tn*d1[0]), expand(tn*d1[1]), td
Kx,Ky,Kden = get_point(dir_BK,dir_CK,W)
Lx,Ly,Lden = get_point(dir_BL,dir_CL,W)

# Points (over common denoms): K=(Kx/Kden, Ky/Kden), L=(Lx/Lden, Ly/Lden).
# M=(1/2,0), N=(p/2,q/2).
# Condition1: ang LNC = beta. beta = (alpha+beta)-alpha, where tan((alpha+beta)/2)=P, tan(alpha/2)=A.
#   tan(beta) = tan((alpha+beta)-alpha). Use formula with half-angles: 
#   Let u=alpha/2 (=arctan A), v=beta/2... no. alpha=2 arctan A, alpha+beta=2 arctan P.
#   beta = 2(arctan P - arctan A). tan(beta/2) = tan(arctan P - arctan A) = (P-A)/(1+AP).
#   So tan(beta) = 2*tan(beta/2)/(1-tan^2(beta/2)) = 2*(P-A)/(1+AP) / (1 - ((P-A)/(1+AP))^2)
#                = 2(P-A)(1+AP) / ((1+AP)^2 - (P-A)^2)
#   = 2(P-A)(1+AP)/((1+AP)-(P-A))((1+AP)+(P-A)) = 2(P-A)(1+AP)/((1+A^2)(1+P^2))? 
#   (1+AP-P+A)(1+AP+P-A) = (1+A)(1+P)*? let me just compute: =1+A^2? 
#   (1+AP)^2-(P-A)^2 = 1+2AP+A^2P^2 - P^2+2AP-A^2 = 1 - A^2 - P^2 + A^2P^2 + 4AP = (1-A^2)(1-P^2)+4AP. 
#   Hmm that's (1-A^2)(1-P^2)+4AP. Keep symbolic.
def tan_of_diff(P,A):
    # tan(2(arctan P - arctan A)) rational
    half = (P-A)/(1+A*P)
    return 2*half/(1-half**2)
tan_beta = tan_of_diff(P,A)
tan_gamma = tan_of_diff(G,A)
tan_beta = expand(tan_beta); tan_gamma=expand(tan_gamma)
# Clear: tan_beta = num_b/den_b
nb = expand(sp.numer(sp.together(tan_beta))); db = expand(sp.denom(sp.together(tan_beta)))
ng = expand(sp.numer(sp.together(tan_gamma))); dg = expand(sp.denom(sp.together(tan_gamma)))
print("tan_beta num/den:", factor(nb), "/", factor(db))
print("tan_gamma num/den:", factor(ng), "/", factor(dg))

# Condition ang LNC = beta: cross(NL,NC) = dot(NL,NC)*tan(beta).
# NL = L - N, NC = C - N = (p/2,q/2). Work with cleared denoms.
# L=(Lx/Lden,Ly/Lden). NL = (Lx/Lden - p/2, Ly/Lden - q/2).
# Multiply through by 2*Lden to clear: 
# NL' = (2*Lx - p*Lden, 2*Ly - q*Lden). NC' = (p,q) (scaled by Lden*... wait NC=(p/2,q/2), 
# cross(NL,NC) = cross(NL', (p,q)) /(2 Lden * 2)? Let me just compute with NL',NC'=(p,q) and 
# tan equality up to scaling: cross(NL,NC)/dot(NL,NC)=tan_b. 
# cross(NL,NC)=cross(NL',(p,q))/(2 Lden * 1) * (1/?)... NL=NL'/(2Lden), NC=(p/2,q/2)=(p,q)/2.
# cross(NL,NC)=cross(NL',(p,q))/(4 Lden). dot(NL,NC)=dot(NL',(p,q))/(4 Lden). Ratio cancels. 
NLp = (expand(2*Lx - p*Lden), expand(2*Ly - q*Lden))
NCp = (p, q)
crA = cross(NLp, NCp); dtA = dot(NLp, NCp)
# crA/dtA = nb/db  =>  crA*db - dtA*nb = 0
condA = expand(crA*db - dtA*nb)
condA = expand(condA)  # polynomial
print("condA factored:", factor(condA))

# Condition ang BMK = gamma. M=(1/2,0). MB=B-M=(1/2,0). MK=K-M=(Kx/Kden-1/2, Ky/Kden).
# MB=(1/2,0), MK = (Kx/Kden-1/2, Ky/Kden). cross(MB,MK)=(1/2)*(Ky/Kden). dot(MB,MK)=(1/2)(Kx/Kden-1/2).
# ratio = (Ky/Kden)/(Kx/Kden - 1/2) = Ky/(Kx - Kden/2) = 2 Ky/(2 Kx - Kden).
MKx = expand(2*Kx - Kden); MKy = expand(2*Ky)  # so ratio cross/dot = MKy/MKx (MB along x)
crB = MKy; dtB = MKx
condB = expand(crB*dg - dtB*ng)
print("condB factored:", factor(condB))
print()
print("condA is polynomial in A,P,G,p,q:", condA.free_symbols)
print("condB is polynomial in A,P,G,p,q:", condB.free_symbols)

import pickle
with open('/tmp/geom/conds.pkl','wb') as f:
    pickle.dump(dict(condA=condA,condB=condB,Kx=Kx,Ky=Ky,Kden=Kden,Lx=Lx,Ly=Ly,Lden=Lden), f)
print("saved conds")
