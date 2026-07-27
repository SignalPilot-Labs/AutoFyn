import pickle, sympy as sp

with open('target_cleared.pkl','rb') as f:
    target_cleared, EqK, EqL, pythx, pythy, sx,cx,sy,cy,St,Ct,Sa,Ca,b,c = pickle.load(f)

gens = [sx,cx,sy,cy]
params = [St,Ct,Sa,Ca,b,c]
F = [EqK, pythx, EqL, pythy]
G = sp.groebner(F, *gens, order='grevlex', domain=sp.FractionField(sp.QQ, params))
rem = G.reduce(target_cleared)[1]

theta, alpha0 = sp.symbols('theta alpha0', real=True)
rem_trig = rem.subs({St: sp.sin(theta), Ct: sp.cos(theta), Sa: sp.sin(alpha0), Ca: sp.cos(alpha0)})

rem_trig_simpl = sp.simplify(rem_trig)
print("Simplified remainder (should be 0):")
sp.pprint(rem_trig_simpl)
