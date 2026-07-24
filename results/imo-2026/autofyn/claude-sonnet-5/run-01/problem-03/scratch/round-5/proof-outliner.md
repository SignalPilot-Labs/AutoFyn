## imo-2026-03

### dyadic-cascade-induction: revise
Target: the whole theorem — `c(n)=2^n/(2^{n+1}-1)`, both directions, for every `n` (unchanged
top-level target; this round adds a new mechanism for the lower-bound half only).
Technique: (existing, kept) strong induction on cut-count `m`, Case (i)/(ii) split on
`a_1` vs `2a_2` for the upper bound; physical-cut-location casework (Branch A / Branch B1 / B2
/ Step 4) for the lower bound. **NEW this round (§5.3): an integer/superincreasing
"no-early-zero" invariant argument** that, if its one flagged lemma is proved, replaces the
entire lower-bound casework with a single non-vanishing claim.

Skeleton (new §5.3, appended after §5.2''):
  1. Import the now-certified `lemmas/dm-completeness-partial.md` (`g=h` modulo the
     never-observed "all-cycles" case) — this licenses working in D/M language for a
     lower-bound claim, which round 4 could not do (the lemma didn't exist yet).
  2. **Integer Invariant Lemma** (proved in full in the file): every state reachable from the
     raw integer multiset `D_m=(2^m,\dots,2,1)` via D/M operations is all-integer. Trivial
     induction on the operation definitions.
  3. **`e=0` characterization** (proved in full): for nonnegative sorted `M`, `e(M)=0` iff `M`
     reduces to empty/all-zero under repeated duplicate-pair cancellation (Lemma P) — because
     `e` is a sum of nonnegative terms (`x_{2i-1}-x_{2i}\ge0`), zero iff every term is zero.
  4. Combine: `e` is always a nonnegative INTEGER on `D_m`'s D/M-orbit, so `e\ge1 \iff e\ne0`,
     and the raw target `e_m\cdot S(D_m)=1` exactly for every `m` — turning the whole lower
     bound into: **no legal `\le m`-operation D/M sequence from `D_m` reaches `e=0`**
     (equivalently, min ops-to-zero from `D_m` is `m+1`, one more than XY's budget — matches
     the already-certified Fact 5, which shows `m+1` ops DO suffice).
  5. **Numerically confirmed this round, exhaustive exact-integer BFS**: min ops-to-zero from
     `D_m` is exactly `m+1` for `m=1,\dots,5` (zero exceptions); min `e` achievable using
     exactly `m` ops is exactly `1` at every `m` tested. Stress-tested the superincreasing
     hypothesis specifically: 13 random strictly-superincreasing sequences (sizes 3–5) all
     needed exactly `k` ops (matching the pattern); 5 random NON-superincreasing sequences all
     admitted shortcuts (fewer than `k` ops), confirming superincreasing-ness is load-bearing.
  6. **Open gap, precisely stated**: a lemma that no D/M-sequence shorter than `k` can reach
     `e=0` starting from a strictly superincreasing `k`-element sequence. Suggested proof
     strategy: strong induction on operation count, tracking that any value formed from a
     chain of merges restricted to a suffix `\{a_{i+1},\dots,a_k\}` stays strictly below `a_i`
     (by the superincreasing gap, the same mechanism behind Fact 2), so it can never tie an
     untouched or less-processed original — blocking the only route to `e=0` (Step 3). Flagged
     two concrete sub-points the builder must check (handling `D`-operations interleaved with
     `M`-chains; non-contiguous/overlapping index subsets), plus a cheap next verification
     (`m=6,7` exact BFS) before attempting the general proof.
  7. Payoff if closed: subsumes Branch A, Branch B1/B2, AND the open Step 4 multi-cut case at
     once — no more location-based casework needed for the lower bound.
Key lemmas (claim + mechanism):
  - Integer Invariant — because D/M operations map integers to integers by construction.
  - `e=0` characterization — because `e` is literally a sum of nonnegative gap terms.
  - Main Claim (conjectured) — because superincreasing gaps (`a_i>a_{i+1}+\dots+a_k`) prevent
    any merged/processed value from ever tying an untouched or less-processed original,
    blocking the only mechanism (Step 2's characterization) by which `e` could reach `0`.
Open gaps: the Main Claim / Step 3 induction is NOT proved — this is the one hard step, with a
concrete strategy and two flagged sub-points for the builder. Case (ii)'s general-`m` upper
bound is explicitly NOT re-derived here (see potential-weighting-upper-bound); a one-paragraph
pointer was added to the Case (ii) section so the file imports that result rather than
duplicating the chain-prefix skeleton.
Cases to cover: the induction (Step 3) needs to handle bisect-chains, match-chains, and mixed
D/M chains uniformly — not case-split further than that.
Watch out for: the inherited "all-cycles" D/M-completeness caveat (never observed, not
excluded); the raw-integer-to-normalized-fraction rescaling must be made explicit, not left
implicit, when the builder writes this up as a proof of `e\ge e_m\cdot S`.

### potential-weighting-upper-bound: revise
Target: the theorem's upper-bound direction — Xiang Yu can always force `e\le e_m\cdot S` —
for every `m`, Case (ii) (`a_1<2a_2`) specifically (Case (i) is dyadic-cascade-induction's).
Technique: (existing) D/M operation-language policy search, now with a **new non-adaptive
policy family**: chain-prefix (a fixed-length run of `M`-merges of the running top result
against successive original elements) followed by the EXACT optimum of a static (non-cascading)
one-shot allocation on the residual, scored via the certified Fact 3 block-extraction identity.

Skeleton (new §6):
  1. Define chain-prefix-`c` (achievability free, it's literally `c` certified `M`-operations).
  2. Define the one-shot tail as a finite, non-adaptive combinatorial optimization (matching +
     deletion on `k-c` fixed values, no further cascading) — scoreable via Fact 3 once a
     matching pattern is fixed.
  3. XY's strategy: `min_{0\le c\le m}` of (chain-prefix-`c`, then exact one-shot-tail optimum).
  4. Conjecture (verified 650+ exact-`Fraction` trials, `m=2..6`, zero failures, including a
     genuinely new hard instance `A=(23,12,6,3)`, `m=3`, requiring `c=2`): this always meets
     `\le e_m\cdot S`.
  5. Recorded dead end this round: "pure one-shot allocation alone, no chain-prefix" is
     insufficient (same `A=(23,12,6,3)` counterexample — best one-shot value `3 > 44/15`, true
     optimum `2` needs the 2-deep chain). The chain-prefix component is load-bearing.
  6. Concrete next step: test whether the one-shot tail's optimal matching/deletion pattern is
     always sorted-adjacent (a rearrangement-inequality-style conjecture) — cheap to check on
     the ~15 hardest instances already on file; if true, Fact 3 gives a closed form, collapsing
     Step 3 to a tractable 1-parameter (`c`) optimization.
  7. Secondary, undeveloped opening noted (majorization/Schur-convexity), flagged only in case
     Step 6 fails.
Key lemmas: none new proved this round beyond what's imported (Fact 3, Lemma D/M) — the
achievability of chain-prefix is automatic from certified Lemma D/M.
Open gaps: the sorted-adjacency conjecture (Step 6, cheap to test), then the resulting
closed-form optimization (Step 3); re-verify `c` stays bounded at `m=7,8` before any general
proof attempt (explorer's own flagged caveat).
Cases to cover: none beyond the `c`-parametrization; the one-shot tail's matching search is
itself finite so no unbounded casework.
Watch out for: do NOT let this collapse back into the already-dead bounded-lookahead family —
the distinguishing feature (no lossy fallback, full range of `c` searched exactly) must be
preserved in any write-up. Explicitly differentiated from dyadic-cascade-induction's own
new §5.3 (that one targets the LOWER bound via an integer-invariant argument; this one targets
the UPPER bound via a static-allocation policy) — no duplicated skeleton between the two files;
dyadic-cascade-induction only carries a one-paragraph import pointer to this section.

### concavity-minimax-duality: revise
Target: the theorem's lower-bound direction (`D_m` resists every XY response), for every `m` —
a universal-over-responses claim, attacked via a certificate/dual object rather than casework
or induction-loading (this slug's recurring "find a certificate" spirit).
Technique: **NEW — 1-Lipschitz weak-duality (Kantorovich–Rubinstein-flavored) certificate**,
replacing the abandoned `Φ`-potential search (§9, now formally set aside after 2 refutations:
round 3's mechanism it fed was proven false; round 4's two concrete `Φ` candidates both
refuted by exact counterexamples).

Skeleton (new §10):
  1. **Weak-duality lemma, proved in full** (3-line pairing argument, no OT citation needed):
     for sorted descending `M` and any 1-Lipschitz `g` with `g(0)=0`,
     `e(M)\ge\sum(-1)^{i+1}g(x_i)`, equality at `g=\mathrm{id}`. Independently re-verified this
     round, 3000 exact-`Fraction` trials.
  2. Target: find `g_m` such that this bound is `\ge e_m\cdot S` on every state reachable from
     `D_m` within `\le m` cuts, with equality at `D_m` itself.
  3. Honest gap: `g=\mathrm{id}` gives equality with zero slack (no help); the natural cheap
     candidate `g(t)=\min(t,e_m)` is already refuted (drops to `0` under stress test, too
     lossy) — do not re-propose this clip.
  4. Concrete next step, cheap and decisive: set up a small LP over the finitely many sample
     values appearing in the known hard/tied configurations already on file (the `m=3` tie
     example, the `m=4,i=3` instance), constraints = 1-Lipschitz between samples + `g(0)=0` +
     the target inequality at each known hard configuration; check FEASIBILITY before any
     general symbolic construction. If infeasible, this is a fast, decisive, valuable negative
     result (report exactly which constraints conflict).
Key lemmas: the weak-duality lemma itself (proved, general-purpose, promotable).
Open gaps: the LP feasibility check (untried, cheap); if feasible, constructing and
stress-testing a concrete `g_m`.
Cases to cover: none yet (LP-feasibility is a single bounded computation).
Watch out for: scope the certificate to states reachable from `D_m` under `\le m` cuts, not
"all multisets" (a strictly harder and unnecessary target); §8's D/M-completeness result
(unchanged, still certified/valid) remains this file's most solid standing contribution
regardless of whether §10 succeeds.

### Direct-recursion framing (Opening 2, `c(n)=2c(n-1)/(2c(n-1)+1)`): NOT opened as a new slug
Considered per dispatch item 4, declined. Reasoning: the explorer's own honest assessment is
that the framing's one hard step ("WLOG a single self-similar dominant cut, recursed once, is
optimal for BOTH players at every `n`") is "very likely exactly as hard as the current Case
(i)/(ii) split" — i.e. medium-confidence risk of relocating the same wall under a different
name rather than avoiding it. This round already produced two well-motivated, numerically
strong, genuinely new mechanisms for the population's two live gaps (the integer/superincreasing
invariant for the lower bound, the chain-prefix static-allocation family for the upper bound) —
both concretely checkable and with a clear next step. Per CLAUDE.md's diversity-over-redundancy
guidance, a 5th slot is better spent letting these two develop than opening a framing whose own
proposer flags as likely no easier, especially since it would need its own version of "WLOG
single dominant cut," which is a genuine new proof obligation, not a free reframe. Flagging for
a future round: if BOTH of this round's new mechanisms stall for 2+ more rounds, this recursion
framing becomes a stronger candidate for a genuine reframe-triggered new slug (per the
plateau-break rule), since at that point it would offer real technique diversity rather than a
speculative parallel track competing for build-set slots against two fresh, promising leads.

### elementary-exchange-smoothing: untouched (retired, per dispatch — no revision).

build set candidates: dyadic-cascade-induction, potential-weighting-upper-bound, concavity-minimax-duality
