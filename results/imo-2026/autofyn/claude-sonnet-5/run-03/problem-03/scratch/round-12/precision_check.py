p = [0.3306,0.2791,0.1501,0.1162,0.0904,0.0208,0.0128]
# check subset for i=1
others_idx = [2,3,4,5,6]
print(p[2]+p[3]+p[6], "vs p[1]=", p[1])
import itertools
for r in range(1,6):
    for combo in itertools.combinations(others_idx, r):
        s = sum(p[i] for i in combo)
        if abs(s - p[1]) < 1e-9:
            print("exact match subset", combo, s)
