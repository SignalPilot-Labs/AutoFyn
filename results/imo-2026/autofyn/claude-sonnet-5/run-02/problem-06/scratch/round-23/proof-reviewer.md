# Round 23 Proof Review — imo-2026-06

Reviewed two built approaches independently and adversarially. Both
self-reported Status `partial`; both self-reports are correct (no false
`solved` overclaim), but the first has a genuine, load-bearing mathematical
error in its central negative diagnosis that I found and corrected via
independent computation extended well past the builder's own tested range.

## 1. `results/imo-2026-06/approaches/a1-3qk-subfamily-theorem.md`

**Target.** Strict generalization of the certified `a_1=3q` (`q` prime,
`q≥7,q≠5`) literal `T=1,L=3` periodicity theorem to `a_1=3q^m`, `m≥1` fixed.

**Part I (base case; `a_n+1` illegality; Case (a) `q∤(a_n+2)`; Case (b)
odd-`n` Parity Witness) — re-derived from scratch, correct.** All four
steps genuinely transplant to arbitrary `m` as claimed, using only
`P(a_1)={3,q}` (true for any `m≥1`) and the elementary fact that an odd
prime to any positive power is odd. One cosmetic issue found and fixed: the
approach file's own derivation of the odd-`n` Parity Witness contains an
internally inconsistent intermediate clause ("So `q^m+n` is even iff `n` is
even" — this should read "iff `n` is **odd**", since `q^m` is odd and
odd+odd=even). The chain as literally written does not even entail its own
stated conclusion. However the **final stated conclusion** ("`N` odd iff
`n` odd") **is correct** — I re-derived it cleanly and verified numerically
(`q=7,m=1`: `n=1`→`N=23` odd, `n` odd — consistent; `n=2`→`N=26` even — n
even — consistent). This is a write-up slip, not a proof error; I certify
the corrected version (see lemma file below).

**Part II (`n_0,s_0` formulas; `K_0(q,m)=3q^{m-1}+s_0`) — re-derived,
correct.** Independently confirmed algebraically (`a_n+2 =
q(3q^{m-1}+s_0+3k)`) and by direct `sympy` computation across many `(q,m)`
pairs, including the `m=1` reduction (`K_0∈{4,5}`, matching the certified
theorem exactly).

**Part III/IV — the load-bearing error, found by this review.** The
builder computes, for primes `q∈[7,200)` and `m∈{2,3}`, whether the
certified Legendre Sieve Gap Bound's sufficient condition (`L≥2^r(r+1)`,
`r:=ω(qK_0)`) holds at `k=0`. I **independently reproduced this exactly**
(`sympy`): `m=2` fails at 18/43 primes in `[7,200)` — the builder's own
list of 18 failing primes matches mine exactly; `m=3` fails at 27/43 (the
builder says "28", off by one, minor). But the builder then reports this
range-limited finding as **"no sign of a small finite exceptional set...a
systematic mismatch of growth rates, not a routine finite check"** and
concludes the certified sieve tools are **"provably insufficient"** for
`m≥2` — i.e. a claim of *structural*, asymptotic failure, stated as
established fact.

**I extended the exact same computation to `q∈[200,20000)`** (own script)
and found this claim is **false**: for `m=2`, only 3 more failures occur
(`q=227,233,443`), then **zero** failures among the next several thousand
primes tested (`q∈[500,20000)`, all pass). For `m=3`, failures continue a
bit longer (`q` up to `1103`) but again **zero** failures for
`q∈[2000,20000)`, over 1000+ primes. This is exactly the signature of a
**finite residual band** — structurally the same phenomenon that the
certified `m=1` theorem already closed (there, the residual band was 18
`(k,K_0)` pairs, closed by hand plus threshold monotonicity) — not a
"genuine change in asymptotic regime" requiring new machinery, as claimed.

The mathematical reason the builder's diagnosis is wrong: the builder's
`L/K_0→` fixed constant `<1` computation (correct arithmetic) does **not**
control whether the certified bound `L≥2^r(r+1)` holds, because `r=ω(qK_0)`
has a slow-growing (`~log log`) normal order — `2^r(r+1)` is typically far
smaller than the linearly-growing `L` for large `q`, so the bound should
hold for *almost all* large `q`, exactly matching what my extended
computation shows. The builder only tested `q<200` and extrapolated a
false asymptotic conclusion from a range too small to see the residual
band's boundary.

**This is a genuine, load-bearing error** — it is the round's own
self-described "substantive result of this round's build" — and it must be
corrected before being trusted by a future round: the honest open-gap
diagnosis should read "the certified sieve tools were checked only for
`q<200` and found to have a substantial exceptional set there, but an
extended check (`q<20000`) finds no further failures past `q≈1103`,
strongly suggesting (not yet proving) the same certified machinery closes
`m≥2` with a larger but still finite residual band — future work should
prove the residual band is genuinely finite (e.g. by a growth-rate argument
on `ω(K_0(q,m))` vs. `q`) rather than assume new tools are required."

**No promotable-lemma overclaim**: the two lemmas the builder actually
offers for certification (Part I item 4's Parity Witness; Part II's
`n_0,K_0` bookkeeping) are both correct and are certified below (with the
Parity Witness write-up corrected).

**Verdict: CHANGES REQUESTED.** Status `partial` is correct (no false
`solved` claim), but Part IV's central diagnosis is mathematically wrong and
must be corrected. Real, certified progress: Part I/II generalize cleanly;
the two sub-lemmas are genuine and reusable. The `m≥2` extension theorem
itself remains open, but the true obstruction is much weaker than reported
— likely closable by the same style of finite-residual-band closure that
took `m=1` three rounds, not new machinery.

## 2. `results/imo-2026-06/approaches/direct-s0-self-absorption.md`

**Target.** A "direct, non-inductive" attack on H2's existence hypothesis
using the canonical core `S_0` from the certified Finite Core Theorem,
avoiding the dead one-prime-at-a-time chain induction.

**Propositions 1–2 (S_0' = S_{N_0}, reduction to the certified Monotone
Chain Reformulation Lemma at `M=N_0`) — re-derived from the definitions,
correct.** I confirmed `S_0' := S_0 ∪ ⋃_{j=1}^{N_0}P(a_j)` is literally the
`M=N_0` member of the already-certified monotone family `S_M`, so
`N(S_0')≤N_0 ⟹ S_0'` self-absorbing follows immediately by direct citation
— no new mathematical content, exactly as the builder honestly reports.

**Proposition 3 (Bounded Witness Lemma insufficiency for full containment)
— re-derived, correct.** I checked the certified `bounded-witness-lemma.md`
statement and confirmed its proof only lower-bounds the *shared* part of
`P(a_j)∩S`, saying nothing about primes of `a_j` outside `S`; the two facts
("shares a prime with S" vs. "confined entirely to S") are logically
independent under the certified stack. Short, correct, self-contained —
**certified** (`lemmas/bounded-witness-insufficiency-for-containment.md`).

**Section 4 (fresh 20,500-term simulation, both mandated hard seeds) — I
independently reproduced EVERY reported number exactly**, using my own
from-scratch simulator (a distinct-factor-set dedup method, different from
the builder's implementation): `Q={11,19,23}` / `{5,7,17,19}`; base-type
persistence pattern (all `2^{|Q|}-1` subsets occurring, last occurrence
within the final ~2-4% of the window, e.g. `{5,7,17,19}` count 15, last at
`n=19644` — exact match); the constructed `S_0` sets
`{2,3,5,7,11,19,23,73,127}` and `{2,3,5,7,13,17,19,23,29,37,43,101}` (exact
match); the containment-violation counts `18501/20500` and `17865/20500`
(exact match); the distinct-extended-type counts `129` and `317`, the
quartile-arrival breakdowns `94,16,8,11` and `199,55,37,26`, and the exact
indices of the brand-new types arriving in the final 5% of the window on
both seeds (exact match down to the specific `n` values and prime sets).
This is a genuinely, fully independently reproduced computational finding —
no error found anywhere.

**The citation correction** ("round-17's 'N(S₀)=0 on 9/9 seeds' finding is
about `S_0=Q`, not the Finite Core Theorem's enlarged core") — I traced
this to `/tmp/memory/math-explorer.md` line 18, which literally reads
"...stabilizes immediately at S_0=Q" — **confirming the builder's
correction is accurate**, not a misreading. This is a genuine, valuable,
verified correction to a citation multiple past rounds (and this round's
own outline) relied on as numeric support.

**Verdict: CHANGES REQUESTED.** Status `partial`, correctly self-reported.
Real progress: confirms the "direct" framing adds no leverage beyond the
existing lemma stack (an honest, useful negative finding, not a restatement
dressed as new); a new, correct, certified insufficiency lemma; and a fully
independently reproduced, load-bearing citation correction that changes the
numeric picture for H2's existence question from "trivially supported" to
"actively still producing new candidate types at the 95th percentile of a
20,500-term window on both hard seeds." H2's existence hypothesis itself
remains open.

## Lemma certification

- **Certified** `lemmas/a1-3qm-parity-and-k0-bookkeeping-lemmas.md`
  (`m`-generalized Parity Witness, write-up corrected; `m`-generalized
  `n_0,K_0` bookkeeping, including the `K_0(q,m)=3q^{m-1}+s_0` growth
  formula) — from `a1-3qk-subfamily-theorem`.
- **Certified** `lemmas/bounded-witness-insufficiency-for-containment.md`
  (Proposition 3) — from `direct-s0-self-absorption`.

## `current.md`

Updated (reviewer-owned) with a new round-23 entry at the top of the
history block, recording both verdicts, the Part-IV error and its
correction, the exact-match computational re-verification of
`direct-s0-self-absorption`, and the two newly certified lemma files.
Overall workspace Status remains `partial` — H1 (FAH) and H2 both remain
open for the general problem; the run's floor deliverable (3 solved
infinite subfamilies: `2|a_1`; `a_1=p^k`; `a_1=3q`) is unchanged.

## Outcomes recorded

- `a1-3qk-subfamily-theorem`: `partial` — "Part I/II verified and
  certified; Part IV's central claim of structural insufficiency refuted by
  extended computation (finite residual band found instead), same style of
  closure as m=1 likely works."
- `direct-s0-self-absorption`: `partial` — "Reduces to existing Monotone
  Chain lemma at M=N0 (no new leverage); new Prop 3 certified; corrected a
  genuine round-17 terminology-collision citation error, all numerics
  independently reproduced exactly; H2 existence remains open."

## Recommendation for next round

For `a1-3qk-subfamily-theorem`: do NOT pursue "new machinery"
(Chebyshev/Jacobsthal-strength `ω` bounds) as the file currently suggests —
instead extend the residual-band approach that closed `m=1`: prove
`K_0(q,m)=3q^{m-1}+s_0`'s residual failure set (where the certified
Legendre bound fails) is genuinely finite for each fixed `m`, then hand-
resolve the (larger, but still finite) residual table, mirroring the
`m=1` theorem's 3-round closure pattern. The needed ingredient is likely a
bound on `ω(qK_0(q,m))` growing slower than `log(L)`, true for all but a
finite/sparse set of `q` by a Robin/Nicolas-Robin-style highly-composite-
number bound (worth checking the crux corpus / knowledge base for this,
rather than assuming it's absent as this round's file states).

For `direct-s0-self-absorption`/H2: the "direct S₀" line is now confirmed
to be a dead end in the sense of adding no new leverage; any future H2
attempt needs either (i) a genuinely new mechanism bounding the *absence*
of primes outside a fixed core in specific low-index terms (not just
presence of a shared prime), or (ii) a much larger-window numeric study
(200,000+ terms) to see whether the new-extended-type arrival rate at the
correct `S_0` core genuinely tapers to zero — the round-17 citation that
many past rounds relied on for optimism here has now been corrected and no
longer supports "H2 trivially resolves."
