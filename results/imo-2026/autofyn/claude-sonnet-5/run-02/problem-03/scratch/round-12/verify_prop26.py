from fractions import Fraction as F
import random, itertools

def A(multiset):
    # alternating sum: sort descending, sum odd-indexed (1-based odd rank)
    s = sorted(multiset, reverse=True)
    return sum(s[i] for i in range(0,len(s),2)) - sum(s[i] for i in range(1,len(s),2))
    # Actually A(S) per convention = sum_{odd rank} L_i - sum_{even rank} L_i? Let's check knowledge base convention.

