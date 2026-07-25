import numpy as np
from probe import xy_best_response

# n=2, k=3: fix p3, vary (p1,p2) with p1+p2 = 1-p3 fixed, sweep ratio
c2=4/7
p3 = 1/7
S = 1 - p3  # =6/7
print("sweeping p1 in (S/2, S) with p2=S-p1, p3 fixed=",p3)
for frac in [0.5,0.55,0.6,0.6667,0.7,0.75,0.8,0.9]:
    p1 = frac*S
    p2 = S-p1
    p = sorted([p1,p2,p3], reverse=True)
    val, info = xy_best_response(p, 2)
    print(f"p1={p1:.4f} p2={p2:.4f} p3={p3:.4f}  val={val:.5f}  (target {c2:.5f})")
