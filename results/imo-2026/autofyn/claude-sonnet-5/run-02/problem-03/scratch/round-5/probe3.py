import importlib.util, time
spec = importlib.util.spec_from_file_location("probe2", "/tmp/round-5/probe2.py")
mod = importlib.util.module_from_spec(spec)
import sys
sys.modules["probe2"]=mod
# avoid running the bottom loop: monkeypatch by reading source minus loop
src = open("/tmp/round-5/probe2.py").read()
# cut off the trailing for-loop block
idx = src.index("for n in [4]:")
src2 = src[:idx]
exec(src2, mod.__dict__)

n=5
p, D = mod.ladder(n)
fn = mod.F(1,D)
print(f"n={n} D={D} target={fn}")
t0=time.time()
for c in [0,1]:
    best, info = mod.A_min_for_c(n, c, p)
    print(f" c={c}: A_min={best} target={fn} comp={info[0] if info else None}  t={time.time()-t0:.1f}s")
