import math, sys
sys.path.insert(0, '/tmp/round-3')
from probe_fs import spf_table, factor, run, minimal_family_inc, mtp_of, common

N = 600000
spf = spf_table(N)

# Q3: Examine a1=1001 large-prime transients. Does 97 enter a minimal support, and when does it leave?
print("=== Q3a: a1=1001 entering log (large primes) ===")
r = run(1001, 1500, spf)
for step, nm, ent in r['entering_log']:
    s = sorted(nm)
    if any(p > 20 for p in s):
        print(f"  n={step}: new_minimal={s} entered={sorted(ent)}")
print(f"  final M: {[sorted(m) for m in r['M_final']]}, Pess_final={sorted(r['Pess_final'])}")
print(f"  mtp_final={mtp_of(sorted(r['Pess_final']), r['M_final'])}, max_gap={max(r['gaps'])}")

# Q3b: Does a_n mod rad(a1) stabilize BEFORE M stabilizes?
# Track the step at which M stabilizes vs the step at which a_n mod rad(a1) enters a periodic cycle.
from itertools import combinations
def run_full_trace(a1, Nmax, spf):
    a = [a1]
    P1 = factor(a1, spf)
    M = [P1]
    Pess = set(P1)
    gaps = []
    M_repr_list = []
    mtp_cached = None
    rad = 1
    for p in P1: rad *= p
    residues_mod_rad = []
    residues_mod_small = {2:[],6:[],30:[],210:[]}
    for n in range(1, Nmax):
        an = a[-1]
        if mtp_cached is None:
            mtp_cached = mtp_of(sorted(Pess), M)
        mtp = mtp_cached
        m_search = an+1
        bound = an + (mtp if mtp else an)
        while m_search <= bound:
            Pm = factor(m_search, spf)
            if all(Pm & Mm for Mm in M):
                break
            m_search += 1
        a.append(m_search)
        gaps.append(m_search - an)
        residues_mod_rad.append(an % rad)
        for mod in residues_mod_small:
            residues_mod_small[mod].append(an % mod)
        M_repr_list.append(tuple(sorted([tuple(sorted(s)) for s in M])))
        new_P = factor(m_search, spf)
        new_M = minimal_family_inc(M, new_P)
        if set(new_M) != set(M):
            Pess = set()
            for S in new_M: Pess |= set(S)
            mtp_cached = None
        M = new_M
    return a, gaps, M_repr_list, residues_mod_rad, residues_mod_small, rad

def first_periodic(arr, max_period=200):
    """Find smallest N0, T such that arr[N0:N0+T] repeats for the rest. Return (N0, T) or (None,None)."""
    L = len(arr)
    for N0 in range(L):
        for T in range(1, min(max_period, L-N0)+1):
            ok = True
            for i in range(N0, L):
                if arr[i] != arr[N0 + ((i-N0)%T)]:
                    ok = False; break
            if ok and L - N0 >= 2*T:
                return N0, T
    return None, None

def M_stabilization_step(M_repr_list):
    """Step after which M_repr never changes."""
    L = len(M_repr_list)
    for N0 in range(L-1, -1, -1):
        if N0 > 0 and M_repr_list[N0] != M_repr_list[N0-1]:
            return N0
    return 0

print("\n=== Q3c: residue stabilization vs M stabilization ===")
for a1 in [15, 105, 385, 1001, 429, 175, 221, 323, 667, 187]:
    a, gaps, M_repr, res_rad, res_small, rad = run_full_trace(a1, 1500, spf)
    N0_M = M_stabilization_step(M_repr)
    N0_rad, T_rad = first_periodic(res_rad)
    info = []
    for mod in [2,6,30,210]:
        N0_s, T_s = first_periodic(res_small[mod])
        info.append(f"mod{mod}:(N0={N0_s},T={T_s})")
    N0_g, T_g = first_periodic(gaps)
    print(f"a1={a1}: M_stab@{N0_M}, gaps_periodic@(N0={N0_g},T={T_g}), res_mod_rad(N0={N0_rad},T={T_rad}), {info}")
