# Round 12 math-explorer report: testing the queued `aimo-0198` averaging-over-all-options
technique against Sharp Argmin Recovery (SAR)

**Verdict up front: DEAD END, precisely diagnosed — both quantitatively (the averaged bound is
too weak, and gets *worse*, not better, as `q` grows) and structurally (even where it happens to
work numerically, it can only ever reach the weaker existential RDRC, never SAR itself, whose
same-index quantifier is exactly the information averaging discards).** Do not dispatch a
proof-builder against this technique for SAR. This is a genuinely different mechanism from round
11's already-dead "average the Forced Swap Inequality's two uncrossing alternatives" (§16.3.1) —
confirmed distinct, tested separately, and also found insufficient, by a different and sharper
argument than round 11's.

All computation below is exact-integer Python (no floats needed beyond forming an average, which
was cross-checked with `fractions.Fraction` on a subsample — no discrepancy), fresh code
independent of the builder's/reviewer's prior harnesses, in `/tmp/round-12/aimo0198-work/`
(`defs.py`, `averaging_test.py`) — kept in its own subdirectory because another parallel explorer
was concurrently writing to the shared `/tmp/round-12/work/`.

## 1. `aimo-0198`'s actual averaging argument, retrieved from the crux corpus

Queried `past_crux_moves_database.json` for `problem_id=aimo-0198` (IMO 2012 P3, "Liar's guessing
game"). Three cruxes on file; the load-bearing one for this lens (`subtopic=probabilistic-method`):

> "Bound a greedy minimizer's outcome by the average of its two available options,
> `min(A,B) <= (A+B)/2`, to get a clean recursive bound on the potential." **How used:** Amy
> (the adversary) maintains potential `phi = sum_i lambda^{m_i}` over `n+1` candidates, `m_i` =
> candidate `i`'s current run-length of answers inconsistent with it. For a query, the two
> hypothetical new potentials `phi_1` (if she answers yes) and `phi_2` (if no) satisfy, **exactly,
> for every state**: `phi_1 + phi_2 = lambda*phi + (n+1)` — because each candidate contributes `1`
> to whichever of the two answers is consistent with it and `lambda^{m_i+1}` to the other,
> summing to a state-independent linear identity. Since Amy picks the min,
> `new_phi <= (phi_1+phi_2)/2 <= (lambda*phi+n+1)/2`, closing the induction **without ever
> identifying which answer she actually picks**.

The essential mechanism, stated generally: a minimizer facing several options can be bounded by
their *average* whenever the **sum of the options has a clean, state-independent closed form** —
the power is entirely in that sum identity, not in "averaging" per se (averaging alone is the
trivial fact `min <= mean`).

## 2. Adaptation attempted, written down explicitly

SAR's setting (restating the file's own §16.1 notation): background `B` (`|B|<=1`), sorted
`Z=(z_1>=...>=z_q)`, `A_1 = OPT_{+1}(B, Z\{z_1})`, and for each partner `k=2,...,q`:
`d_k = z_1-z_k`, `A_{3,k} = OPT_{+1}(B∪{d_k}, Z\{z_1,z_k})`, `B_{3,k} = TAGGED_{+1}(B∪{d_k},
Z\{z_1,z_k}, k-1)`. `M_opt = min_k A_{3,k}`, achieved at `k^*`. SAR claims: `M_opt<A_1 ⟹
B_{3,k^*} = A_{3,k^*}`.

The direct transplant of the crux's mechanism, adapted to a minimizer with `q-1` options
(partners `k`) instead of `2`:

- **(a) Sum identity, sought:** does `sum_k A_{3,k}` (or `sum_k B_{3,k}`) equal a clean,
  easily-computed closed form in `B,Z` — mirroring `phi_1+phi_2 = lambda*phi+(n+1)` — independent
  of which `k` is the argmin?
- **(b) Existential-recovery bound, sought (the most faithful transplant of "bound the min by the
  average, don't identify the argmin"):** does `mean_k(B_{3,k}) <= M_opt` hold, which would prove
  the *existential* RDRC (**some** `k` recovers, not necessarily `k^*`) via pure averaging, with no
  argmin identification at all — a genuinely different route from every recovery mechanism tried
  so far (exact matching, Forced Swap Inequality, local repair)?

Note explicitly, per the dispatch's own caution: this is **not** the round-11 dead end, which
averaged only the *two* uncrossing alternatives of one already-chosen crossing pair
(`e(R∪{z_1-z_i,z_{k^*}-z_j})` vs. `e(R∪{z_1-z_j,z_i-z_{k^*}})`); here the average is taken over
**all** `q-1` match partners `k`, before any crossing pair is even chosen.

## 3. Computational test

Fresh harness `defs.py`: brute-force `OPT_sigma`/`TAGGED_sigma` over the full finite selection
space (all partial matchings + independent K/D on singles for `OPT`; non-crossing + no-arc-spans-
split restriction for `TAGGED`), re-derived independently from the file's §13.2 definitions (not
copied from any prior round's code). **Sanity check:** reproduces the file's own certified
`|B|=2` counterexample exactly: `B={2,4}, Z=(6,3,2,1)` gives `OPT_{+1}=0`, `TAGGED_{+1}(·,0)=1`,
matching the file bit-for-bit.

**(3a) SAR reconfirmed (baseline sanity, fresh code, `q=3..6`, `|B|∈{0,1}`, 320 instances, 34
triggered):** `34/34` SAR successes, `0` violations — consistent with, and independently
reproducing, prior rounds' extensive corroboration.

**(3b) Sum identity (a): does NOT hold beyond a degenerate boundary case.**
`sum_k A_{3,k}` vs. `sum_k B_{3,k}`, `q=3,...,6`, 120 trials per `q`:

| `q` | trials | `sum(A_3) ≠ sum(B_3)` |
|---|---|---|
| 3 | 120 | **0** |
| 4 | 120 | 14 |
| 5 | 120 | 29 |
| 6 | 120 | 52 |

At `q=3` the sums always agree — but this is a **trivial degeneracy, not a real identity**: with
`q=3`, removing `z_1` and any partner `z_k` leaves exactly **one** element, which can never
participate in a crossing regardless of the split point, so `A_{3,k}=B_{3,k}` **pointwise** for
every individual `k` (verified directly), not just in aggregate. As soon as `q>=4` (so the
residual after removing `z_1,z_k` has `>=2` elements and a genuine crossing constraint can bind),
the sums diverge in a growing fraction of instances (12%, 24%, 43% at `q=4,5,6`). **No clean
closed-form sum identity survives past the case where it would be forced for a vacuous reason** —
unlike `phi_1+phi_2=lambda*phi+(n+1)`, which holds unconditionally by construction of `phi`. This
already rules out route (a): there is no aimo-0198-style state-independent sum formula to average
over here.

**(3c) Existential-averaging bound (b): fails in the overwhelming majority of triggered instances,
and gets *worse*, not better, as `q` grows** (fresh random trials, `q` fixed, `|B|∈{0,1}` uniform,
1500 trials at `q<=5`, 400 at `q=6,7`):

| `q` | triggered (`M_opt<A_1`) | `mean_k(B_{3,k}) <= M_opt` (averaging succeeds) | rate |
|---|---|---|---|
| 3 | 232 | 41 | 17.7% |
| 4 | 200 | 3 | 1.5% |
| 5 | 171 | 3 | 1.8% |
| 6 | 33 | 0 | 0.0% |
| 7 | 26 | 0 | 0.0% |

Even the modest `q=3` success rate is the same degenerate boundary artifact as (3b) (only 2
partners, both automatically crossing-free), not real leverage. For `q>=4` — the regime where the
technique would actually need to do work — it succeeds only **~1–2% of the time**, trending to
**0%** by `q=6,7`. Quantifying the typical shortfall on the *failing* instances (`q=3..7` pooled,
61 triggered samples): `mean_k(B_{3,k}) - M_opt` ranges from `0` to `3`, mean `≈1.3`; as a ratio
(`M_opt>0` only), `mean_k(B_{3,k})/M_opt` ranges from `1.0` to `3.67`, mean `≈1.8` — **the
averaged bound typically overshoots the target it would need to beat by roughly 80%, and the
"too weak by X" is `X≈1.8×` on average, worsening (not improving) with instance size.**

**Diagnosis of *why* it is this weak.** `M_opt=A_{3,k^*}` is (by definition) the single smallest
value among `q-1` numbers `A_{3,2},...,A_{3,q}` that are otherwise essentially uncorrelated with
which `k` is "close" — most partners `k` give a large `A_{3,k}` (a bad match), and only one or a
few give the small `M_opt`. Averaging over **all** partners is dominated by the bad ones and
converges to something close to a "typical" `A_{3,k}`, not the extremal one — exactly the opposite
of what SAR/RDRC need. This is structurally different from `aimo-0198`'s setting, where the
average is over only **two** options at every step (so the "bad" option can inflate the average by
at most a bounded factor per step, and the recursion is applied `k+1` times, not once) — a
mechanism that depends on the branching factor being small and fixed, which is exactly not the
case here (branching factor `q-1`, growing with the instance).

## 4. Structural off-target diagnosis (independent of the numeric weakness)

Even granting a hypothetical future fix to (3c)'s numeric gap (e.g. some yet-unfound reweighting
making `mean_k(B_{3,k}) <= M_opt` true always), **this would only ever establish the weaker
existential RDRC — never SAR.** SAR's content is precisely that recovery happens **at the same
`k^*`** that achieves `M_opt`, a same-index equality claim. An averaging bound is, by construction,
blind to *which* index achieves anything — it only ever certifies "the aggregate/some index is
small enough," never "this specific, externally-determined index is exactly right." So even in
the best case this route could ever offer only a second, independent proof route to the *already
existentially-supported* RDRC, not a proof of SAR, and per the numbers above it does not even
achieve that except in a residual, structurally-degenerate sliver of instances (`q=3` only, and
even there, only ~18% of triggered cases, i.e. it would need to be paired with an exhaustive
covering argument for the rest, defeating its own purpose as an argmin-free shortcut).

## 5. Recommendation

**Do not dispatch a proof-builder against the `aimo-0198`-style averaging-over-all-options
technique, for either SAR or the weaker RDRC.** Record this as a second, precisely-diagnosed dead
end for "averaging" as a proof architecture in this problem (distinct from, and independent of,
round 11's dead "average the two uncrossing alternatives" result) — the common root cause across
both averaging attempts is now clear: **this problem's recovery phenomenon is inherently an
extremal/argmin-specific fact, and every averaging-based bound tried so far converges to a
typical-case estimate that the true extremal quantity beats by a growing margin as the instance
size increases.** Future proof attempts for SAR should continue to pursue argmin-specific
mechanisms (as `lemmas/forced-swap-inequality.md` already does, correctly, by reasoning about
`k^*` directly rather than an aggregate) rather than any further variant of "bound the minimum by
an aggregate of all options."

## Appendix: reproducibility

- `/tmp/round-12/aimo0198-work/defs.py` — independent `OPT_sigma`/`TAGGED_sigma` brute force,
  self-check against the file's `|B|=2` counterexample (`python3 defs.py`).
- `/tmp/round-12/aimo0198-work/averaging_test.py` — builds `A_1,A_3[k],B_3[k]` per instance,
  reports SAR reconfirmation, the sum-identity check (3b), and the existential-averaging check
  (3c) (`python3 averaging_test.py`, and the ad-hoc follow-up snippets used for the per-`q`
  tables above, run inline via `python3 -c "..."` importing `build_instance` from this module).
