import sys
sys.path.insert(0,'/tmp/round-5')
from probe2_lib import ladder, A_min_for_c, build_fragments, eval_frag

n=3
p, D = ladder(n)
print(f"--- n={n} D={D} ---")
for c in range(0, n+1):
    best, info = A_min_for_c(n, c, p)
    comp, pt = info
    frags, d = build_fragments(p, comp)
    vals = [eval_frag(f, pt) if pt else eval_frag(f, ()) for f in frags]
    vals_sorted = sorted(vals, reverse=True)
    print(f"c={c} comp={comp} A_min={best} fragments(sorted desc)={vals_sorted}")
