import numpy as np
from probe import xy_best_response

# n=3, k=4 pieces, budget=3
c3 = 8/15
configs = [
    (8/15,4/15,2/15,1/15),  # exact geometric
    (0.5,0.25,0.15,0.10),
    (0.4,0.3,0.2,0.1),
    (0.4,0.4,0.15,0.05),   # near-tie top two
    (0.3,0.3,0.3,0.1),
    (0.6,0.2,0.15,0.05),
    (0.35,0.3,0.2,0.15),
]
for p in configs:
    p=list(p); s=sum(p); p=[x/s for x in p]
    val, info = xy_best_response(p, 3)
    print(f"p={[round(x,4) for x in p]} val={val:.5f} target={c3:.5f} {'OK' if val<=c3+2e-3 else 'VIOLATION'} dist={info[0]}")
