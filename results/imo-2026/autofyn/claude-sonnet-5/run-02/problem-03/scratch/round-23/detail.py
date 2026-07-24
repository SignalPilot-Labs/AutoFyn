import sys
sys.path.insert(0,'/tmp/round-23')
exec(open('/tmp/round-23/search_b2_n3.py').read().split("print(\"\\n--- detailed")[0])

seen = {}
for r in results:
    p, comp, val, margin = r
    if comp not in seen:
        seen[comp] = (p, val, margin)

for comp,(p,val,margin) in seen.items():
    v, vals = phi_min_for_composition(p, comp, restarts=15)
    print(comp, "p=",[round(x,5) for x in p])
    print("   frags sorted:", sorted([round(x,5) for x in vals], reverse=True))
