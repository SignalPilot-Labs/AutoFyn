# Round 21 proof-reviewer report — imo-2026-06 (IMO 2026 P6)

Reviewed both built approach files in full, `knowledge_base.md`, and
`lemmas/a1-3q-parity-and-k0-window-lemmas.md` / `lemmas/elementary-omega-bound.md`
(the pre-existing certified lemmas this round's `a1-3q` file builds on).
Independently re-derived algebra and re-ran fresh Python scripts (distinct
from both builders') for every checkable claim in both slugs.

## 1. `a1-3q-subfamily-theorem`

**Claims checked and independently confirmed:**

- **(a) Step-4 uniformity fix.** Recomputed `7k ≥ 2^{ω(K)+2}` for `K=4+3k`
  (K₀=4 branch) and `K=5+3k` (K₀=5 branch), `k=1..30`. Result: fails only at
  `k=1,2` (K=7,10) for K₀=4, and only at `k=1` (K=8) for K₀=5 — matches the
  builder's claim exactly. The sub-case note (`ω(qK) ≤ ω(K)+1` regardless of
  whether `q|K`) is a correct, trivial observation.

- **(b) The `g(M) ≤ 2^{ω(M)}` elementary-proof obstruction.** Tried the two
  natural repair strategies myself: (i) the halving-induction — confirmed it
  has exactly the collision the outline-reviewer's `M=6` example already
  flagged (both half-window IH witnesses can collide on divisibility by the
  new prime, with no guarantee of a *specific* alternate witness); (ii) the
  AP-based peel-one-prime-at-a-time fix — confirmed this only reproduces the
  radical bound (window length forced to `∏p_i = rad(M)`), which the file
  already showed (round 20) is far too weak. Independently sieve-verified
  that the target bound `g(M) ≤ 2^{ω(M)}` is nonetheless true with wide
  margin on primorials and other composites up to `ω(M)=8`
  (`M=9699690`), e.g. `g(30030)=22 ≤ 2^6=64`, `g(10010)=10 ≤ 2^5=32` —
  consistent with known Jacobsthal-function values. So this is a real,
  believable, but genuinely nontrivial classical fact (in the spirit of
  Iwaniec-type sieve results), not a fictitious target and not something
  insufficiently tried — the builder's diagnosis is correct.

- **(c) The `q=40153` CRT construction.** Independently verified: `q=40153`
  is prime; `q ≡ 10123 (mod 30030)`; `K₀+3k = 5+3·3335 = 10010` exactly;
  `n = n₀+kq = 133,937,024`; `N := a_n+2 = 3(q+n)-1 = q·K` exactly
  (`401,931,530 = 40153×10010`). Direct exhaustive search over
  `i=2,…` against the true `N` found the first witness at `i=11`, i.e. offset
  `10` from `q` — matching `g(10010)=10` exactly (confirmed by direct sieve:
  `q+1,…,q+9` all share a factor with `10010`, `q+10` is the first
  coprime). This definitively refutes "a small `q,k`-independent fixed
  window always suffices," exactly as claimed.

- Both pre-existing certified lemmas (`a1-3q-parity-and-k0-window-lemmas.md`)
  that this file's cases (1)-(5) build on remain correct and unconditional
  (re-checked, no change from round 20 certification).

**No error found anywhere in this round's a1-3q build.** Case (b), n even,
k≥1 remains open; Step 1 (the crude prime-gap bound itself) is not proved
elementarily, and I could not find a shortcut either in the time available.
This is a genuine open gap, not a hand-waved one, and the round's negative
findings (two natural repair strategies foreclosed, with a verified
adversarial witness) are real, correct, unconditional contributions.

**No new lemma certified this round** — both (a)-(c) are negative/diagnostic
findings (foreclosing strategies, refuting a fallback), not standalone
positive theorems, matching the workspace's existing "diagnostic, not
portable" precedent (Lemma F/Lemma I style).

**Verdict: CHANGES REQUESTED.** Status stays `partial`. Real, independently
confirmed progress; gap (Step 1) remains and is honestly reported as such.

## 2. `fah-counterexample-hunt`

**Claims checked and independently confirmed:**

- **Period detection.** Wrote a from-scratch naive greedy generator (direct
  gcd against every earlier term — no bitmask optimization, a third
  independent implementation distinct from both of the builder's scripts).
  Confirmed the exact claimed period for `a_1=385`: `T=5088, L=43890`, zero
  mismatches across 26911 checked gap indices (~5 full periods, out to
  n=32000). Also independently confirmed two of the four canonical hard
  seeds from the builder's table: `a_1=187 → (T,L)=(484,7854)` and
  `a_1=221 → (T,L)=(334,6630)`, both exact, zero mismatches over the checked
  range. No discrepancy found with the builder's reported `(T,L)` pairs.

- **Exact one-period FAH check and the "false alarm" resolution.**
  Independently recomputed, with my own script, the base-type and
  extended-type (`P(a_n) ∩ S*`, `S*={2,3,5,7,11,19}`) structure over one full
  period (`n=1..5088`) of `a_1=385`, and exhaustively checked every
  disjoint-base-type pair's extended-variant combinations for a shared
  prime. Result: **zero violations** among all qualifying pairs (all 6
  disjoint-base pairs among the 7 base types, including the flagged
  `{7}`-vs-`{11}` pair with the `{7}` minority variant `{3,19,7}`, which
  intersects every `{11}`-variant via `19` or `3`). This confirms the
  "false alarm" diagnosis is genuine — the apparent non-intersection at the
  whole-base-type level really was an artifact of averaging over several
  extended sub-types, not a hidden real gap.

- The periodicity-implies-exact-check argument (for `p|L`, `p|a_{r+kT}` iff
  `p|a_r`, since `p|kL`) is correct algebra, and the builder's own scope
  claim — that this is a verification tool contingent on already knowing
  `(T,L)`, not a general proof strategy — is accurate and appropriately
  modest; I found no overclaiming here.

- `a_1=105945` is honestly flagged inconclusive (no period found `T<25000`);
  I did not have budget to extend this search, but since it is reported as
  inconclusive rather than as a result, this does not affect the round's
  verdict either way.

**No error found anywhere in this round's FAH build; no hidden counterexample
was missed** in the seeds/technique I independently re-checked.

**Verdict: RETHINK — not a criticism of the work itself (rigorous, honest,
and independently confirmed correct in every particular I checked), but a
routing call on scope.** Status stays `unsolved`: as currently scoped ("hunt
for a genuine FAH counterexample"), this round returned a clean negative
across 11 fresh seeds, exactly the "no refutation, but real evidence"
outcome the round's own outline (§4) anticipated in advance. That is a
legitimate, valuable contribution (broader negative evidence than the
workspace's prior `|Q|=2`-only base, plus a validated, reusable
period-detection technique that gives an exact rather than asymptotic FAH
check for any specific `a_1` once `(T,L)` is found) — but it is not itself
forward motion on a proof of the problem's claim, and simply running more
seed sweeps is diminishing-returns. The outliner should decide the concrete
next move for this line: extend the `105945` search depth, target a
genuinely different class of seed, or pivot to attempting the outline's own
§1.3(a) structural non-intersection-invariant argument (a short proof that
no shared prime can ever be recruited between two disjoint-base types) —
none of which is "more of the same search," and hence a re-plan (RETHINK)
is the correct routing rather than an open-ended CHANGES REQUESTED that
just says "search more."

## Summary verdict line

- `a1-3q-subfamily-theorem`: **CHANGES REQUESTED** (partial — real,
  independently confirmed progress; Step 1's elementary Jacobsthal-type
  bound remains the open gap).
- `fah-counterexample-hunt`: **RETHINK** (unsolved — rigorous, independently
  confirmed clean negative search plus a genuinely reusable technique; needs
  the outliner to set the next concrete target rather than repeat the same
  search).
