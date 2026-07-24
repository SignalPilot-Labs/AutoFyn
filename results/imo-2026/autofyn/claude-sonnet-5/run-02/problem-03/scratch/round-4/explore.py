from fractions import Fraction as F
from itertools import product, combinations
import sys

def ladder(n):
    denom = 2**(n+1) - 1
    return [F(2**(n+1-i), denom) for i in range(1, n+2)]  # p_1..p_{n+1}

def A_of(sorted_desc):
    # alternating sum, odd ranks positive (1-indexed)
    s = F(0)
    for idx, v in enumerate(sorted_desc):
        if idx % 2 == 0:
            s += v
        else:
            s -= v
    return s

def brute_min_A(p, total_cuts, grid_points=None):
    """
    p: list of piece lengths (n+1 pieces)
    total_cuts: n
    We search over compositions (c_1..c_{n+1}) summing to <= total_cuts,
    and for each, grid-search fragment positions (using rational grid based on
    subset-sum candidate breakpoints: since ties matter, candidate optimal fragment
    values likely equal some subset-sum of the p_i's / rational combos).
    This is expensive in general; for small n we do a fine grid search with Fractions
    using denominators that are multiples of 2^(n+1)-1.
    """
    pass

