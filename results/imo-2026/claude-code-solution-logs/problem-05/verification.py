"""Verification script for IMO Problem 5 solution (f(x) = x + c, c >= 0).

Run: python3 problem5_verification.py
Verified run: 2026-07-22 ~16:04 PDT (all checks pass).
"""
import random, math

# ---------------------------------------------------------------
# 1) Sufficiency: f(x) = x + c satisfies the full chain
#    sqrt((x^2+f(y)^2)/2) >= (f(x)+y)/2 >= sqrt(x f(y))
#    for 200,000 random (c, x, y) samples.
# ---------------------------------------------------------------
random.seed(1)
for trial in range(200000):
    c = random.uniform(0, 10)
    x = random.uniform(0.001, 100)
    y = random.uniform(0.001, 100)
    f = lambda t: t + c
    L = math.sqrt((x * x + f(y) ** 2) / 2)
    M = (f(x) + y) / 2
    R = math.sqrt(x * f(y))
    assert L >= M - 1e-12 and M >= R - 1e-12, (c, x, y, L, M, R)
print("1) sufficiency: f(x)=x+c satisfies the chain on 200k samples  -- OK")

# ---------------------------------------------------------------
# 2) The equality-case constraint bites for non-solutions:
#    at x = f(y), the chain forces f(f(y)) = 2 f(y) - y.
#    f(x) = kx with k > 1 must FAIL the chain there.
# ---------------------------------------------------------------
for k in [1.1, 1.5, 2.0]:
    y = 1.0
    x = k * y  # x = f(y)
    f = lambda t: k * t
    L = math.sqrt((x * x + f(y) ** 2) / 2)
    M = (f(x) + y) / 2
    R = math.sqrt(x * f(y))
    assert not (L >= M >= R), f"k={k} unexpectedly passed"
print("2) non-solutions f(x)=kx (k>1) violate the chain at x=f(y)     -- OK")

# ---------------------------------------------------------------
# 3) Algebraic identities used in Step 3 of the proof,
#    checked by random substitution (100,000 trials):
#    (a) 2f(z)-z+y == A + B + delta   where A=f(z), B=f(y),
#        delta = g(z)-g(y), g = f - id
#    (b) 2A^2+2B^2-(A+B+d)^2 == (A-B)^2 - 2(A+B)d - d^2
#    (c) A + B - (z-y) == 2y + g(y) + g(z)
# ---------------------------------------------------------------
random.seed(7)
for _ in range(100000):
    z, y, Fz, Fy = [random.uniform(0.01, 50) for _ in range(4)]
    assert abs((2 * Fz - z + y) - (Fz + Fy + (Fz - z) - (Fy - y))) < 1e-9

    A, B, d = (random.uniform(-30, 30) for _ in range(3))
    assert abs((2 * A * A + 2 * B * B - (A + B + d) ** 2)
               - ((A - B) ** 2 - 2 * (A + B) * d - d * d)) < 1e-6

    gz, gy = random.uniform(0, 20), random.uniform(0, 20)
    Ae, Be = z + gz, y + gy
    assert abs((Ae + Be - (z - y)) - (2 * y + gy + gz)) < 1e-9
print("3) Step-3 algebraic identities (100k random substitutions)     -- OK")

# ---------------------------------------------------------------
# 4) Step-4 telescoping demo: the bound
#    |g(z)-g(y)| <= (z-y)^2 / (4 min(y,z))
#    telescoped over n equal steps on [a,b] tends to 0.
# ---------------------------------------------------------------
a, b = 2.0, 7.0
prev = float("inf")
for n in [1, 10, 100, 10000]:
    h = (b - a) / n
    bound = n * h * h / (4 * a)
    assert bound < prev
    prev = bound
    print(f"   n={n:6d}: telescoped bound on |g(b)-g(a)| = {bound:.6f}")
print("4) telescoping bound -> 0, forcing g constant                  -- OK")

print("\nALL CHECKS PASSED")
