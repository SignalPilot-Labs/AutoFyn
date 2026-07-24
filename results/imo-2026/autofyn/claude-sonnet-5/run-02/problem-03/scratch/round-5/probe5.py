import sys
sys.path.insert(0,'/tmp/round-5')
from probe2_lib import ladder, vertex_min_for_composition, build_fragments, eval_frag

n=3
p, D = ladder(n)
for comp in [(1,0,0,0),(1,1,0,0),(0,1,0,0),(1,0,1,0),(1,2,0,0)]:
    val, comp_, pt = vertex_min_for_composition(p, comp)
    frags,d = build_fragments(p, comp)
    vals = sorted([eval_frag(f,pt) if pt else eval_frag(f,()) for f in frags], reverse=True)
    print(comp, "min A=", val, "vertex frags:", vals)
