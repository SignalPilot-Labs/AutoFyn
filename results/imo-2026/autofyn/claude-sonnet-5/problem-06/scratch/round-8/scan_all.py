import json, sys, itertools
from sympy import factorint
from analyze_dsat import rad, analyze_core

def scan(a1, path):
    seq = json.load(open(path))
    P1 = rad(a1)
    print(f"=== a1={a1} P1={sorted(P1)} n={len(seq)} ===")
    for p in sorted(P1):
        S = frozenset({p})
        res = analyze_core(a1, seq, S)
        if "error" in res:
            print(f"  S={{{p}}}: {res['error']} (I_S={res.get('I_S_count')}, J_S={res.get('J_S_count')})")
            continue
        depths = [b["min_extra_primes"] for b in res["buckets"] if b["min_extra_primes"] is not None]
        maxd = max(depths) if depths else None
        extras = set()
        for b in res["buckets"]:
            if b["min_dominator"]:
                extras |= (set(b["min_dominator"]) - set(b["kappa"]))
        print(f"  S={{{p}}}: D_minus_P1={res['D_minus_P1']} buckets={len(res['buckets'])} "
              f"depths={depths} max={maxd} all_extra_primes_used={sorted(extras)}")

if __name__ == "__main__":
    for a1, path in [(2747,"seq_2747_20k.json"), (21528751,"seq_21528751_32k.json"),
                      (1517,"seq_1517_8k.json"), (4087,"seq_4087_10k.json"), (4199,"seq_4199_10k.json")]:
        scan(a1, path)
