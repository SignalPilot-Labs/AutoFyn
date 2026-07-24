import sys
sys.path.insert(0,'/tmp/round-23')
exec(open('/tmp/round-23/search_b2_n3.py').read().split("random.seed(1)")[0])

p = (0.44, 0.2666, 0.14667, 0.14663)  # tweak slightly inside box (p2 just under 4/15)
val, comp, vals = true_phi_min(p, comps)
print("true phi_min=", val, "comp=", comp, "margin=", 8/15-val)
print("vals=", sorted(vals, reverse=True))

# also check chamber A's own formula value there
p1,p2,p3,p4 = p
phiA = p2 + (p1+p4)/2
print("chamberA formula phi =", phiA, "margin=", 8/15-phiA)
