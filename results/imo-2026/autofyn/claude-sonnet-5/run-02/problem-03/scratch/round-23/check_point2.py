import sys
sys.path.insert(0,'/tmp/round-23')
exec(open('/tmp/round-23/search_b2_n3.py').read().split("random.seed(1)")[0])

p = (0.45714286, 0.26666667, 0.18095238, 0.0952381)
val, comp, vals = true_phi_min(p, comps)
print("true phi_min=", val, "comp=", comp, "margin=", 8/15-val)
print("vals=", sorted(vals, reverse=True))
