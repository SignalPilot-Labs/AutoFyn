import io, contextlib
from sim4 import process

seeds = [int(x) for x in open('seedlist3.txt').read().split()]
for a1 in seeds:
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            rounds, converged = process(a1, length=3000, max_rounds=6)
    except Exception as e:
        rounds, converged = ('ERR', str(e))
    print(a1, rounds, converged)
