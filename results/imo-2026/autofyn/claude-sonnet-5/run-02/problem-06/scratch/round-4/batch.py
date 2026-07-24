import sys, io, contextlib
from sim4 import process

seeds = [int(x) for x in open('seedlist.txt').read().split()]
results = {}
for a1 in seeds:
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            rounds, converged = process(a1, length=2500, max_rounds=6)
        results[a1] = (rounds, converged)
    except Exception as e:
        results[a1] = ('ERR', str(e))
    print(a1, results[a1])
