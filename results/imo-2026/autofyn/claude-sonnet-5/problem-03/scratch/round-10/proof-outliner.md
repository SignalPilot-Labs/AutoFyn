## imo-2026-03

potential-weighting-upper-bound: revise
Target: The whole theorem's upper-bound direction — for every positive integer `m` and every
Liu Bang opening `A` (sorted, `|A|=m+1`, the tight case isolated by the already-certified Slack
Collapse Lemma), Xiang Yu has a response forcing `e(A,\text{final}) \le e_m\cdot S(A)`. Combined
with the already-fully-closed lower bound against `D_m` (round 8) and the chain-prefix+tail
rescoping (§9.4), this closes `c(n)=2^n/(2^{n+1}-1)` for all `n` once the remaining gap below is
proved.
Technique: (unchanged spine) chain-prefix+tail construction (§6/§7, certified Slack Collapse)
reduces the whole induction to proving `OPT(Y,p-1)=NC(Y,p-1)` for every sorted `Y` of size `p`.
Round 9's route to this (recursive strong induction on `p` with a growing flat background set,
§12/§13) is now REFUTED at `|B|\ge2` (see below) — round 10 replaces it with a genuinely different,
non-recursive local-exchange technique: the Fixed-Support Uncrossing Conjecture (new §14), strong
induction on the NUMBER OF CROSSINGS in an `OPT`-achieving matching, not on list size.
Skeleton:
  1. (certified, unchanged) Slack Collapse (`lemmas/slack-collapse.md`) reduces the whole
     upper-bound induction to the tight case `k=m+1` — by direct corollary of certified Fact 5.
  2. (certified, unchanged) Chain-prefix+tail rescoping (§9.4): within the tight case, after any
     chain-prefix of length `c\in\{0,\dots,m\}`, the residual tail has `p=k-c` elements and budget
     exactly `p-1` — by a direct algebraic identity `m=k-1`.
  3. (§13.6, formally retired this round) The recursive strong-induction-on-`p` route with a flat
     growing background `B` (§12.2) is FALSE at `|B|\ge2` — counterexample below. DEAD END, do not
     re-attempt in this form.
  4. (NEW, §14, open) Fixed-Support Uncrossing: take any `OPT(Y,p-1)`-achieving selection; if its
     matching `M` crosses, re-pair the SAME support into a non-crossing matching `M'` without
     increasing value, by a bounded sequence of pairwise uncrossing swaps — by the certified
     General Rank-Extraction Identity tracking the exact sign change of `e()` under one swap. This
     directly gives `NC(Y,p-1)\le OPT(Y,p-1)`, hence (with the trivial reverse direction, §9.2)
     equality.
Key lemmas (claim + mechanism):
  - Slack Collapse (certified) — `k\le m` lets Xiang Yu force `e=0` outright via Fact 5's
    chain-cancellation, trivially beating any positive target.
  - General Rank-Extraction Identity (certified) — `e(F)=e(\text{head})+(-1)^{r-1}x+(-1)^r
    e(\text{tail})` for `x` at general sorted rank `r`; the tool for computing the EXACT sign
    change of `e()` when two matched values are swapped for their nested non-crossing alternative.
  - **DEAD (formally retired, §13.6): the generalized Full-Slack Insertion Lemma /
    `\mathrm{OPT}_\sigma(B,Z)=\mathrm{TAGGED}_\sigma(B,Z,0)` for arbitrary flat background `B`,
    `|B|\ge2`** — counterexample `B=\{2,4\}, Z=(6,3,2,1)`: `OPT_{+1}=0\ne1=TAGGED_{+1}(\cdot,0)`,
    confirmed by two independent codebases, by hand, and by a fresh 500-trial sweep (22/500
    mismatches, contradicting round 9's own claimed 0/500). Mechanism of failure: `B` as a flat
    value set has no memory of whether its own generating arcs cross each other — exactly the
    information the winning selection needs at `|B|\ge2`.
  - **NEW, open: Single-Swap Non-Increase Lemma** — one uncrossing swap (replace crossing pairs
    `(i,j),(i',j')`, `i<i'<j<j'`, by the nested non-crossing alternative `(i,i'),(j,j')`) never
    increases `e()` of the resulting merged multiset — because the General Rank-Extraction
    Identity expresses the exact rank/sign contribution of each swapped value, turning "does this
    swap help" into a concrete two-term sign computation, not yet carried out.
  - **NEW, open: Bounded Termination Lemma** — a crossing matching on `2r` points can be sorted
    into a non-crossing one in at most `O(|M|)` (plausibly `\lfloor|M|/2\rfloor`) swaps — a
    classical chord-diagram/interval-sorting fact, elementary but not yet written down here.
Open gaps:
  1. Single-Swap Non-Increase Lemma (§14 Step 3) — the actual hard content, computationally
     supported (204+ zero-failure crossing-optimal instances at `b=p-1`, 109 at `b=p-2`; sharp
     breakdown at `b=p-3`, 25/78 failures) but not proved.
  2. Exact swap-depth bound (§14 Steps 1/4) — termination itself is elementary, the precise bound
     is not yet derived.
  3. Cheap diagnostics to run FIRST (flagged by the explorer, before any general-`|M|` write-up):
     (a) does a single swap always suffice, or is genuine induction on crossing-count needed for
     `|M|\ge3`? (b) is `|M|=2` a clean, fully hand-provable base case, or does it turn out to
     already carry the full difficulty (as §12.1's "easier base case" assumption wrongly did) —
     check for this trap explicitly, do not assume `|M|=2` is easy just because it's small.
  4. If Single-Swap Non-Increase needs amortized (not purely local) accounting: two untested
     crux leads to adapt — `aimo-0043`'s obstacle-charging/resource-transfer between branches
     (closest structural fit if some swaps are locally value-increasing but compensated later),
     or `aimo-0558`'s greedy+injective-charge-to-a-distinct-witness (if the proof goes
     constructive instead of existential).
Cases to cover: base case `|M|=2` (Step 2); general inductive step `|M|\ge3` with an explicit rule
for WHICH crossing pair to swap first (classical uncrossing lemmas typically pick the
"most-nested"/"leftmost" crossing to guarantee progress — not yet pinned down here); confirm no
swap ever needs to move an element between `K`/`D` and `M` (would break the "same support" framing
and collapse back into the already-dead round-6/7 general-budget mechanism).
Watch out for: (1) do not conflate "crossing count strictly decreases" (termination, Step 1) with
"`e()` weakly decreases" (value bound, Step 3) — these are logically independent, both must be
proved. (2) The sharp empirical cutoff at `b=p-3` (25/78 failures) is real signal — scope every
lemma explicitly to `b\ge p-2`, do NOT attempt the general/loose-budget form (that is exactly the
already-dead round-6/7 local-exchange claim, which the round-6 counterexample instance itself was
re-tested against at `b=p-1` this round and found to survive/not-fail there — confirming the two
claims are genuinely different in scope, not a rehash). (3) All `b=p-3` failures found used
strictly less than full budget — check whether "the optimal selection uses the full budget
exactly" needs to be a stated, proved hypothesis, not just an empirical correlation.

concavity-minimax-duality: advance (benched, no build task this round)
Target: (unchanged) an independent 1-Lipschitz-certificate proof that `e_{g^*}(D_m,m)\ge1` for
every `m`, via the Local Claim (§15.4: `bucket(x-y)>bucket(z)` for one `M`-operation's output vs.
a specific comparison element).
Technique: (unchanged) token/dominant-index bookkeeping specific to `D_m`-reachable
(superincreasing-base) states.
Skeleton: unchanged from round 9 (§14/§15); no new content this round.
Key lemmas: unchanged — Superincreasing Preservation, Slot-Replacement, Value-Order=Dominant-
Index-Order (all certified); Local Claim itself still open, 13507 zero-violation transitions
through `m=6`.
Open gaps: the Local Claim (§15.4) remains unproved.
Cases to cover: none new this round.
Watch out for: **independently re-confirmed this round (not merely trusted from round 9) that even
a full closure of the Local Claim gives ZERO leverage on the Match-Recovery/upper-bound gap** —
its entire machinery only concerns states reachable from a superincreasing base via legal D/M
sequences, and the upper bound needs a bound valid for an ARBITRARY (non-superincreasing) Liu Bang
opening. Do not put this back in the build set unless a future round finds a genuinely new
generalization beyond `D_m`-reachable states, or for final theorem synthesis once the upper bound
closes elsewhere. Benched alongside `dyadic-cascade-induction` this round — do not treat "benched"
as "dead," just as "no leverage on the critical path right now."

dyadic-cascade-induction: advance (benched, unchanged from round 9 — no new task)
Target: (unchanged) the full theorem; this slug's substantive content (lower bound against `D_m`,
fully unconditional since round 8) is complete and requires no further work.
Technique: (unchanged) D/M-operation reformulation + all-cycles resolution.
Skeleton: unchanged; no gaps remain in its own scope.
Key lemmas: all already certified (Superincreasing No-Early-Zero, all-cycles-resolution).
Open gaps: none within this slug's own scope — the theorem's remaining gap lives entirely in
`potential-weighting-upper-bound`'s upper-bound direction.
Cases to cover: none.
Watch out for: re-confirmed this round (via explicit grep by `math-explorer-plateau-check.md`) that
this file has no unused machinery applicable to Match-Recovery/Fixed-Support Uncrossing — its
token/dominant-index tools are D/M-reachability-from-`D_m`-specific, the same limitation diagnosed
for `concavity-minimax-duality`. Keep benched; re-activate only for final synthesis once the upper
bound closes, or a genuinely new angle surfaces.

(elementary-exchange-smoothing remains formally RETIRED, unchanged since round 4 — its content
lives in `lemmas/vertex-lemma.md`; no further builds against this slug.)

build set: potential-weighting-upper-bound
