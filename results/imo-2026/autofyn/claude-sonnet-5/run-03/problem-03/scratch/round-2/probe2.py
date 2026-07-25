import numpy as np
from probe import xy_best_response, oddsum

c2 = 4/7
print("c(2) =", c2)

configs = [
    (0.5,0.3,0.2),
    (0.4444,0.3333,0.2222),  # near geometric-ish (4,3,2)/9 not exact
    (4/7,2/7,1/7),  # exact geometric
    (0.6,0.25,0.15),
    (0.6,0.3,0.1),
    (0.45,0.45,0.1),
    (0.5,0.4,0.1),
    (0.7,0.2,0.1),
    (0.34,0.33,0.33),
    (0.9,0.06,0.04),
    (0.55,0.35,0.10),
    (0.5,0.35,0.15),
]
for p in configs:
    p = list(p)
    s = sum(p)
    p = [x/s for x in p]
    val, info = xy_best_response(p, 2)
    print(f"p={[round(x,4) for x in p]} val={val:.5f} target={c2:.5f} {'<=OK' if val<=c2+1e-4 else 'VIOLATION'} dist={info[0]} splits={[round(x,4) for x in info[1]]}")
