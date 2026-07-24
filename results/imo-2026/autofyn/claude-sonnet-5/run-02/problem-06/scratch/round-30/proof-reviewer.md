# Round 30 proof-review — imo-2026-06

## Slug 1: `a1-19q-subfamily-theorem` — Status claimed `solved`

**Verdict: APPROVE.**

### What I independently re-derived (all via fresh Python/sympy scripts, not the builder's)

- **306-cell `(s_0,K_0)` table.** Recomputed `s_0(j,r)=pow(r,-1,19)*j mod 19`,
  `K_0=19+s_0`, for all `j∈{2,...,18}, r∈{1,...,18}`. Confirmed diagonal
  `j=r ⇒ s_0=1,K_0=20` for every cell, and max `K_0=37`. Matches the file's
  table exactly.
- **The 260 below-threshold `k=0` candidates and the 7 exceptions.** Using
  the builder's exact `Q_1(j,r)=(19(K_0+1)+j)/s_0` formula, independently
  enumerated primes `q≡r (mod 19)` below threshold: got exactly **260**
  triples (byte-for-byte the same list as the file, verified programmatically,
  not just by count). Resolved each by direct witness search
  (`gcd(N,a_i)` for `a_i=19(q+i-1)`, `i=1..n_0`): **253 resolve, exactly 7
  do not** — `(4,4,23),(5,5,43),(10,10,29),(12,12,31),(15,15,53),(16,16,73),
  (18,18,37)` — identical to the file's list and to `Bad(19)`.
  *Side note (not an error, recorded for the record):* the builder's `Q_1`
  formula uses `K_0+1` rather than the tight sufficiency bound `K_0`; the
  tight criterion (`n_0-1≥K_0`) actually yields only 250 below-threshold
  candidates. The extra 10 the builder's looser formula pulls in are simply
  also resolved by witness search, so this costs nothing and introduces no
  gap — flagged only for precision, not as a defect.
- **`s^*=5` threshold.** Verified `(s+1)! ≥ 37 + (19/23)·2^(s+1)·(s+2)`
  numerically for `s=5..30` — holds with wide margin throughout (e.g.
  `s=5`: `720 ≥ 407.09`). The induction step's algebra
  (`s^2+2s-2≥0` for `s≥1`) is elementary and correct.
- **`k≥9` generic closure and the residual `k∈{1,...,8}` band.** Recomputed,
  from scratch, the exact per-cell threshold `q_thresh(j,r,k)` for all
  `306×8=2448` `(j,r,k)` combinations using `bound=2^{ω(K)+1}(ω(K)+2)` with
  `K=K_0+19k` (note `K` is independent of `q`, so this is a single
  per-cell computation, not per-`q`) — found exactly **25**
  below-threshold `(j,r,k,q)` quadruples, byte-for-byte identical to the
  file's list. Split: **21 moot** (`q∈{23,29,31,37}⊂Bad(19)`), **4
  non-moot** (`q∈{41,47,59,61}`) — matches exactly. Independently verified
  all 4 non-moot witnesses by direct integer computation: `(8,2,1,59)→i=3`,
  `(12,3,1,41)→i=3`, `(16,4,1,61)→i=5`, `(17,9,1,47)→i=7` — exact match on
  `n_0,n,K,N` and the witness index in every case.
- **The new Diagonal Window-Parity/Mod-5 Lemma (§6) — scrutinized as the
  load-bearing new step.** Re-derived Steps A–E independently:
  - Step A is a correct, general instantiation of the §2 Case-(a) argument
    at the specific window `i=1,...,j-1` below the diagonal candidate —
    algebra (`a_{n_0}+i ≡ q-(j-i) (mod q)`, `≡ i (mod 19)`) checks out.
  - Step B is a correct instantiation of the §2 Case-(b) reduction at
    `k=0`, diagonal `K_0=20` — the `\gcd(N,19)=1` and `n_0≤q ⇒ q∤m` facts
    both verified.
  - Step C ("window length 1 is automatic since `q` is odd ⇒ `q+1` even")
    is an unconditional one-line fact, correctly used to dispatch
    `q∈{23,29,31,37}` (all of `19+r` for `r∈{4,10,12,18}` independently
    confirmed prime).
  - Steps D–E's explicit checks were independently verified by direct
    arithmetic: `24,34` composite (forcing the next residue-class
    candidates `43,53`, both prime, both with `q+2` divisible by 5:
    `45=3^2·5`, `55=5·11`); `35,54` composite (forcing `73`, prime, with
    window `{74,75,76}`, `74=2·37`, `75=3·5^2`, `76=2^2·19`, all sharing a
    factor with 20). All confirmed exactly.
  - Step E's exhaustiveness (no 8th exception exists) is corroborated by
    the independent from-scratch full witness search above, which found
    exactly the same 7 exceptions and no more.
  This lemma is rigorous and non-circular — a genuine, uniform mechanism,
  not 7 disguised ad hoc checks (though it does still bottom out in
  checking specific small numbers' primality/factorizations — this is
  legitimate direct computation, not hand-waving).
- **Independent from-scratch greedy resimulation**, `q∈(19,6000)` (all
  primes), literal legality rule (`gcd(candidate,a_i)>1` for every prior
  `i`): zero mismatches for `q∉Bad(19)`; exact match on
  `Bad(19)={23,29,31,37,43,53,73}` and every claimed deviation
  index/value (`a_3=460,580,620,740` for `q=23,29,31,37`; `a_4=860,1060`
  for `q=43,53`; `a_5=1460` for `q=73`).

**No gap found anywhere.** This is the 7th successful instantiation of an
already-6-times-certified machinery (Generalized `K_0`-Boundedness,
gcd-difference Witness Lemma, Legendre Sieve Gap Bound, Primorial Floor
Bound, Universal Look-Back Witness Identity), plus a genuinely new and
correctly-proved uniform mechanism for the diagonal exceptions. Every
numeric claim reproduced exactly by independent scripts.

**Promotable lemmas:** the p=19-specific table/threshold and the
p=19-instantiated Diagonal Window-Parity/Mod-5 Lemma are NOT certified as
separate reusable lemma files — consistent with precedent (the p=11/13/17
instantiations' analogous per-`p` tables were likewise not split into
separate `lemmas/` files; only the fully `p`-independent machinery already
lives there). The file's own text correctly frames the diagonal lemma as
"reusable in shape, not as stated" (its K_0=20=2^2·5 factorization is
`p=19`-specific) — so no over-certification risk here; declined as a
separate lemma file, matching workspace convention.

## Slug 2: `fah-counterexample-hunt` — Status claimed `unsolved`

**Verdict: CHANGES REQUESTED** (real, correct negative work on Prong (b);
Prong (a)'s headline finding is independently found to be **factually
wrong**, not merely budget-limited, and must be corrected next round).

### Prong (b) — invariant refutations: CONFIRMED CORRECT

- **Introduction-order permutation**, `a_1=4807=11·19·23`: independently
  resimulated; confirmed `73` and `127` are the 6th/7th new primes
  introduced (indices 5,6 in 0-indexed new-prime order), strictly before
  `5,7,17,13` (indices 7,8,9,10) — exact match to the file's claim.
- **Residue-vector-mod-core-prime**, `a_1=187`: independently resimulated
  2000 terms; `a_n mod 11` and `a_n mod 17` each hit **every** possible
  residue (11 and 17 respectively) — even stronger than the file's "10+
  distinct values" claim, confirming definitively not conserved.

Both refutations are genuine, concrete, data-backed, and correctly
reported. This is real, additive negative work.

### Prong (a) — the `a_1=7402395` "six-singleton near-miss": REPRODUCED
### AS FALSE, not merely inconclusive

I built an independent bitmask-based greedy simulator, validated it two
ways before trusting it on the new seed: (1) exact agreement with a
from-scratch naive `gcd`-based generator on `a_1=7402395` itself for its
first 2000 terms; (2) exact, zero-violation reproduction of this same
approach file's own already-established `a_1=385`, `T=5088,L=43890`
periodicity claim. Having confirmed the methodology, I ran it to
`n=520{,}000` on `a_1=7402395=3·5·7·11·13·17·29`.

**Result:** the file's claim ("six distinct types ... occurring exactly
once each," at indices `114808,160731,185459,219179,344423,482192`) does
**not** hold as stated:

- 4 of the 6 claimed indices match up to a constant `+1` (harmless
  indexing-convention offset): `185459→185460`, `219179→219180`,
  `344423→344424`, `482192→482193` — genuinely singleton through
  `n=520{,}000`.
- The other 2 are **wrong, not just off by a constant**. The type meant by
  claimed index `114808` (`{3,5,7,11,13,17}`, "omit 29") actually first
  occurs at `n=83139` and **recurs twice more**, at `n=249410` and
  `n=415686` — three occurrences total, not one, well within the same
  500k-term window the builder used. The type meant by claimed index
  `160731` (`{3,5,7,11,13,29}`, "omit 17") first occurs at `n=141823` and
  recurs at `n=425466` — two occurrences, not one.
- The 7th possible "omit-one" type (`{5,7,11,13,17,29}`, "omit 3") never
  occurs at all through `n=520{,}000` in my resimulation — consistent with
  the file finding only "six" occupied types (a plausible reason there
  were only 6, not 7, candidates to report).

**This means the round's headline finding is an outright numerical error**
(2 of the 6 "singletons" are not singletons; their reported indices don't
correspond to any real occurrence), not the "compute-budget-limited,
honestly inconclusive" framing the file gives it. The file's Status
(`unsolved`) itself is not an overclaim — no counterexample was asserted as
proven — but the specific finding must not be carried forward as "the
sharpest, largest-scale near-miss this workspace has produced" without
correction, and must not be handed to a future round as a ready-to-run
target in its current (incorrect) form.

**Gap to close next round:** re-simulate `a_1=7402395` correctly (my
occurrence data above can be reused/cross-checked) and either (a) retract
the "six simultaneous singleton" framing and report the corrected picture
(at most 4 genuine singletons through 520k terms, one type absent so far,
two types that recur and are therefore not near-misses at all), or (b) if
a future, larger-window resimulation is wanted, base it on a
methodology cross-validated the way I did here (naive-gcd spot check +
reproduction of an already-established period) before trusting a novel
large-seed run.

## `current.md` housekeeping check

Verified via `git diff` that this round's `a1-19q` builder's edit to
`current.md`'s `## Approaches tried` / `## Current best` sections only
touched those two sections (confirmed by diffing against the pre-round
commit) — it did not touch the reviewer-owned `## Status` / `## Full
proof` sections. Content spot-checked and factually accurate (round
21–29 summaries match the corresponding round entries already in the
file).

## `current.md` updates made by this review

- Updated `## Status` (top) to record the round's 11th APPROVE
  (`a1-19q`) with full independent-verification detail, and to record the
  `fah-counterexample-hunt` Prong (a) correction (factually incorrect
  near-miss data) alongside the confirmed-correct Prong (b) refutations.
- Added a new `## ROUND 30` section (before `## Round 27 lemma
  certifications`) with full verdict detail for both slugs.
- No new lemma files certified this round (matches precedent: per-`p`
  instantiation tables/thresholds are not separately certified; the new
  Diagonal Window-Parity/Mod-5 Lemma is `p=19`-specific in its stated form
  and the file itself does not claim full generality).

## Outcomes recorded via `record_outcome`

- `a1-19q-subfamily-theorem`: `verified-milestone` — 11th APPROVE, 7th
  `p`-instantiation of the certified machinery, new diagonal mechanism
  independently verified rigorous.
- `fah-counterexample-hunt`: `partial` — Prong (b) invariant refutations
  confirmed correct (real negative work); Prong (a)'s headline near-miss
  finding independently reproduced as factually wrong (2 of 6 claimed
  singletons actually recur within the same window) and must be corrected,
  not merely extended, next round.
