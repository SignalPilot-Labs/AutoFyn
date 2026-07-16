import sympy as sp

# 8 independent indeterminates: k,l,b,c and their conjugates kb,lb,bb,cb
k,l,b,c,kb,lb,bb,cb = sp.symbols('k l b c kb lb bb cb')

# Reality conditions cleared of denominators
E1 = b*c*(kb-bb)*(lb-cb) - bb*cb*(k-b)*(l-c)
E2 = (k-b)*(2*l-c)*cb*(lb-bb) - (kb-bb)*(2*lb-cb)*c*(l-b)
E3 = b*(k-c)*(lb-cb)*(2*kb-bb) - bb*(kb-cb)*(l-c)*(2*k-b)

# Circumcenter O = kl(lb-kb)/D, Ob = kb lb(k-l)/D, D = k lb - kb l
D = k*lb - kb*l
O_num = k*l*(lb-kb)   # O = O_num/D
Ob_num = kb*lb*(k-l)  # Ob = Ob_num/D

# Target T*D = TN:
TN = 2*O_num*(cb-bb) + 2*Ob_num*(c-b) - (c*cb - b*bb)*D
TN = sp.expand(TN)

# numeric check
import numpy as np
vals = {b:complex(-0.5,-1.5), c:complex(1.5,-1.5),
        k:complex(-0.2531182195716988,-1.1260806200681075),
        l:complex(0.7866438932120947,-1.0881436597179395)}
vals[kb]=vals[k].conjugate(); vals[lb]=vals[l].conjugate()
vals[bb]=vals[b].conjugate(); vals[cb]=vals[c].conjugate()
def ev(expr):
    return complex(expr.subs(vals))
print("E1=",ev(E1),"E2=",ev(E2),"E3=",ev(E3))
print("TN=",ev(TN))

print("=== attempt: solve E2,E3 for kb,lb ===")
sol = sp.solve([E2,E3],[kb,lb],dict=True)
print("num solutions:",len(sol))
for i,s in enumerate(sol):
    print("solution",i)
    print(" kb=",sp.simplify(s[kb]))
    print(" lb=",sp.simplify(s[lb]))
