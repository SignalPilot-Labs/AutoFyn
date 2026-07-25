import random
def oddsum(vals):
    s = sorted(vals, reverse=True)
    return sum(s[i] for i in range(0, len(s), 2))
random.seed(5)
worst = 1e9
for _ in range(20000):
    k = random.randint(1,15)
    vals = [random.uniform(0.001,1) for _ in range(k)]
    total = sum(vals)
    v = oddsum(vals)/total
    if v < worst: worst = v
print("min OddSum/sum ratio observed:", worst)
