from sympy import *
import numpy as np

u, v, a, b, g = symbols('u v a b g')

Kx = g*(a*v + u)/(a + g); Ky = g*(v - a*u)/(a + g)
Lx = (-a*b*v + 2*a + b*u + b)/(a + b); Ly = b*(a*(u-1) + v)/(a + b)

F1 = (a**2*b**2*u**2 - a**2*b**2*u + a**2*b**2*v**2 - a**2*b*v - 2*a**2*u
      - 2*a*b*u**2 - 2*a*b*u - 2*a*b*v**2 + 2*a*v - b**2*u**2 - b**2*u - b**2*v**2 + b*v)
F2 = (a**2*g**2*u**2 - a**2*g**2*u + a**2*g**2*v**2 - a**2*g*v + 2*a**2*u - 2*a**2
      - 2*a*g*u**2 + 6*a*g*u - 2*a*g*v**2 - 4*a*g + 2*a*v - g**2*u**2 + 3*g**2*u - g**2*v**2 - 2*g**2 + g*v)

Ox = u + Rational(1,2)
Oy = symbols('Oy')
eqK = expand((Ox-Kx)**2 + (Oy-Ky)**2 - ((Ox-2*u)**2 + (Oy-2*v)**2))
y = solve(eqK, Oy)[0]
eqL = expand((Ox-Lx)**2 + (y-Ly)**2 - ((Ox-2*u)**2 + (y-2*v)**2))
P = expand(fraction(cancel(eqL))[0])

# Compute the Groebner basis and the reduction with quotients
G = groebner([F1, F2], u, v, a, b, g, order='grlex')
quots, rem = G.reduce(P)
print("remainder is zero:", expand(rem)==0)
nG = len(G)

# Also express each Groebner element in terms of F1,F2 via spoly reduction
# Build the conversion: for each G[i], find c1,c2 with G[i]=c1*F1+c2*F2 by reducing F1,F2 and tracking
# Easier: directly verify P = sum quots[i]*G[i] AND that the ideal membership holds, which we have.
# For the cleanest certificate, let me reconstruct Q1,Q2 s.t. P=Q1*F1+Q2*F2 using linear algebra:
# reduce F1 and F2 with the GB and express everything... 
# Actually the simplest independent certificate is just: store GB + quotients, since 
#   P = sum(quots[i]*G[i])  is a concrete polynomial identity.

recon = expand(P - sum(quots[i]*G[i] for i in range(nG)))
print("P = sum(q_i G_i) verified symbolically:", recon == 0)

# Definitive numerical test of the certificate
f = lambdify((u,v,a,b,g), recon, 'numpy')
rng = np.random.RandomState(0)
vals = [rng.uniform([0.1,0.1,0.1,0.05,0.05],[2,3,3,1.5,1.5]) for _ in range(10000)]
maxerr = max(abs(f(*p)) for p in vals)
print(f"numerical max|P - sum(q_i G_i)| over 10000 random pts: {maxerr:.2e}")

# Save full certificate
with open('/tmp/certificate.txt','w') as f_out:
    f_out.write("=== CERTIFICATE OF PROOF ===\n")
    f_out.write("Claim: P lies in ideal <F1,F2>, where P, F1, F2 are polynomials in (u,v,a,b,g).\n\n")
    f_out.write("F1 = "+str(F1)+"\n\n----\n\n")
    f_out.write("F2 = "+str(F2)+"\n\n----\n\n")
    f_out.write("P  = "+str(P)+"\n\n----\n\n")
    for i in range(nG):
        f_out.write(f"G[{i}] (Groebner basis elt) = {G[i]}\n")
        f_out.write(f"q[{i}] (quotient) = {quots[i]}\n\n")
    f_out.write(f"Symbolic check P == sum(q_i G_i): {recon==0}\n")
    f_out.write(f"Numerical max error over 10000 pts: {maxerr}\n")
print("saved /tmp/certificate.txt")
print("\nGroebner basis size:", nG)
