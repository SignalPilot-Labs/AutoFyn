## imo-2026-03 — lens: the aggregated Small-Gap Crossing-Domination Lemma gap

### Exact statement of the target (from `potential-weighting-upper-bound.md` §11.1/§11.4)

Fix sorted `Y=(y_1\ge\dots\ge y_p)`. For `j\in\{2,\dots,p\}` let `Z_j:=Y\setminus\{y_1,y_j\}`
(order preserved), tagged with an inside/outside split at `s=j-2` (ranks `2,\dots,j-1` inside,
`j+1,\dots,p` outside). Define (§11.1) `INSERT_OPT(v^\dagger,Z,b')` = min over selections of
`Z`'s own index set (cost `\le b'`) of `e(\{v^\dagger\}\cup\text{kept}\cup\text{matched diffs})`,
`v^\dagger` itself never selectable; `INSERT_NC` = same restricted to (i) self-non-crossing AND
(ii) no matched pair spanning the inside/outside split. **Aggregated lemma (open):**
```
min_{j=2}^p INSERT_OPT(y_1-y_j, Z_j, p-2) = min_{j=2}^p INSERT_NC(y_1-y_j, Z_j, p-2)
```
(plus the `max`-over-`j` companion at gap `0`, `MAXOPT`/`MAXNC`). This is the last piece needed
(via the already-certified Extreme-Element Peeling Lemma) to close `OPT(Y,p-1)=NC(Y,p-1)` and
hence the whole upper-bound Case (ii) at general `m`. **The per-fixed-`j` form (same equality
without the `min_j`) is a proven DEAD END** — exact counterexample `Y=(92,89,77,73)`, `j=3`:
`INSERT_OPT=1` (via crossing match `(89,73)`) vs `INSERT_NC=15`. Do not re-attempt that form.

I independently reimplemented `OPT`, `NC`, `INSERT_OPT`, `INSERT_NC` from scratch (exact Python
`int`, full exhaustive enumeration, no heuristics; `/tmp/round-9/work/explore.py`) and reproduced
the file's `p=4,j=3` counterexample exactly (indices `0`-based: mismatch at `j=2` = file's
"`j=3`"), and reproduced `OPT(Y,p-1)=NC(Y,p-1)` on 240 fresh trials (`p=3..6`, zero mismatches)
and the aggregated lemma on 500 fresh trials (`p` up to `8`, zero mismatches) — consistent with,
independent confirmation of, the file's 2060+-trial claim.

### New structural finding (not in the file; solid, reproducible, likely provable outright)

**"Degenerate-split" sub-lemma, verified 1300 zero-failure trials.** Whenever the inside/outside
split is degenerate — `j=1$ (inside empty) or `j=p` (outside empty) — `INSERT_OPT=INSERT_NC`
holds **unconditionally** (not just in the aggregate): `400/400` trials at `j=1`, `400/400` at
`j=p-1$ (`p` up to `8`). More strongly, I isolated *why*: at `j=1$ or `j=p`, the sub-budget passed
to `INSERT_OPT/INSERT_NC` always equals `|Z_j|` exactly (**full slack**, since `|Z_j|=p-2` and the
sub-budget is `p-2`). Testing this **budget-only** condition in full generality — arbitrary
inserted `v^\dagger`, arbitrary `Z` (no relation to `y_1-y_j`), budget `=|Z|` exactly, and *no*
inside/outside split at all — gives `INSERT_OPT=INSERT_NC` in `500/500` fresh trials (`q` up to
`7`), zero exceptions. So: **full slack + no genuine split ⟹ equality always; the discrepancy is
caused entirely by a genuine (both-sides-nonempty) split, not by budget scarcity.** This gives an
unconditional "for free" anchor for 2 of the `p-1` candidate partners (`j=1,p`) — but they do
**not** always carry the global aggregate optimum (see next finding), so this alone is a base
case / building block, not a full proof.

**Candidate technique this suggests (not attempted, a lead for the outliner):** since
`INSERT_OPT(v^\dagger,Z,b'=|Z|)` behaves like a *frozen-extra-element* variant of the very same
`OPT`/`NC` machinery, apply the already-certified Extreme-Element Peeling Lemma **recursively
inside** the `INSERT_OPT/INSERT_NC` computation itself (peel `Z`'s own first element, carrying
`v^\dagger` along as an inert background element throughout every level) and attempt strong
induction on `p`. This is structurally self-similar to the main induction and hasn't been tried.

### The "re-route to an endpoint of the crossing arc" lead — tested, genuinely fails as a one-step surgery

Per dispatch, I tested this concrete lead directly: for every per-`j` mismatch (`INSERT_OPT(j) <
INSERT_NC(j)`), take the crossing arc `(a,c)` used by the winning `OPT` selection (`a` inside,
`c` outside) and check whether switching the partner of `y_1` to `j'=a` or `j'=c` recovers
`INSERT_NC(j')=` the global aggregate optimum. **Result (400 random trials, `p` up to `7`, 347
observed per-`j` mismatches): succeeds in `297/347` (`~86%`) but genuinely FAILS in `50/347`
(`~14%`)** — a real, reproducible refutation of the literal one-step form of this lead. Concrete
failing example: `Y=(463,461,372,291,237,180)`, `p=6`, mismatch at `j=4` (crossing arc uses
indices `{2,5}`); neither `j'=2` nor `j'=5` recovers the optimum (`3`, `≠2`) — instead the true
compensating partner is `j'=1$ (match `y_1,y_2$), whose winning `NC` selection (`D={2,3,4,5}`,
`M=()`, pure deletion) is **structurally unrelated to the crossing arc entirely**. Three more
such examples on file in `/tmp/round-9/work/explore.py`'s output. Diagnosis: the compensating
partner is not reliably an endpoint of the *specific* crossing arc that caused the local failure
— it can be a globally different, often much simpler (pure-deletion) selection at a distant `j'`.
A stronger simplification, "the two extremes `j=1,p` always suffice for the aggregate," was also
tested and also fails (`95/500`, `~19%`) — the winning partner is genuinely allowed to be any
interior `j`, confirmed by explicit counterexamples in the script output. **Recommendation: do
not pursue "re-route to an endpoint of the offending crossing arc" as a single local-surgery
step; if revived, it would need to be a fully recursive/inductive re-routing (potentially
re-routing through a chain of several arcs), not a one-shot swap** — and even then the observed
compensating structures (pure deletion at a distant `j'`) suggest the real mechanism may be
closer to a global counting/injection argument than a local exchange.

Additional numeric fact: the aggregate optimum is witnessed by a pure-deletion (`M=()`) NC
selection at *some* winning `j'` in `194/300` trials, but genuinely requires an actual (non-empty)
non-crossing match at *every* winning `j'` in `106/300` (`~35%`) — so "just delete" is not a
universal escape hatch either.

### Sign-dominance technique (from `lemmas/all-cycles-resolution.md`) — likely not directly transferable

That lemma's mechanism is: expand a closing linear system via a token invariant, find a
closed-form solution, and show the coefficient on the *most-significant participating index*
flips sign across blocks while superincreasing dominance forces that block negative (a domain
violation). This crucially exploits `D_m`'s **strict superincreasing structure** (`a_i` exceeds
the sum of all smaller `a_j`'s) to force the dominance/sign argument. The Case (ii) `Y` here is
Liu Bang's **arbitrary** opening residual (no superincreasing assumption at all — `Y` can be
near-uniform, as the `m=3` near-uniform counterexample elsewhere in the file shows). So the
literal dominance mechanism does not transfer; only the loose "expand an invariant, find a term
whose sign is structurally forced" flavor might inspire an analogous argument for `e`'s layer-cake
(threshold-counting) representation — untested, flagged as weak/speculative, not a concrete lead.

### Candidate techniques for the outliner (ranked by promise)

1. **Recursive/self-similar strong induction** using the full-slack "degenerate-split" anchor
   (new finding above) as a base case, peeling `Z_j`'s own first element via the *already-
   certified* Extreme-Element Peeling Lemma applied one level deeper, carrying `v^\dagger` as an
   inert element. Most promising untried lead from this session.
2. **Layer-cake / threshold-counting reformulation** (`lemmas/layer-cake-and-noncrossing-
   independence.md`) applied specifically to the aggregated `\min_j` statement — turn the
   equality into a statement about `N(t)` parity across all `j` simultaneously; untested this
   round but a natural fit given the already-certified layer-cake identity is in the KB for this
   exact problem.
3. Global counting/injection argument directly on selections (since the compensating structure is
   often a totally different, simpler selection at a distant `j'`, an injective map from
   "OPT-optimal selections using a genuine crossing" to "NC selections at some other `j'` with
   equal or better value" might exist even though no *local* surgery captures it).

### Cheap-kill candidates
- None found this round that immediately close the gap. The two negative results above (per-
  fixed-`j` dead end already known; naive endpoint-reroute now also shown to fail as a one-step
  argument; extremes-only shortcut also fails) are useful **prunes**, not cheap kills of the whole
  problem.

### Knowledge-base entries to use
- Extreme-Element Peeling Lemma (§11.2, certified, general — reusable recursively per lead #1).
- Layer-cake identity / Non-crossing inside/outside independence
  (`lemmas/layer-cake-and-noncrossing-independence.md`).
- Fact 3 (block extraction) and Fact 5 (chain-cancellation/full-slack) — Fact 5's "full budget
  forces achievability" flavor is exactly the mechanism likely underlying the new degenerate-split
  finding above; worth re-deriving explicitly for `INSERT_OPT`.
- Slack Collapse Lemma — same full-slack family, may generalize to the frozen-`v^\dagger` setting.

### Analogous past problems (cruxes)
Not queried this round — my lens was a deep, code-verified structural probe of the specific gap
per dispatch instructions, which took the full scouting budget productively. A crux-corpus search
for "non-crossing partition DP optimality" / "matching + deletion optimization" analogues is a
reasonable task for a parallel explorer or next round if this technique search stalls.

### Prior progress
`potential-weighting-upper-bound` §11 (round 8): Extreme-Element Peeling Lemma fully proved and
certified; per-fixed-`j` Small-Gap Crossing-Domination refuted; aggregated form isolated as the
sole remaining gap, 2060+ trials support, unproved. This round adds: independent reproduction,
one new unconditional structural sub-lemma (degenerate-split ⟹ equality, likely provable), and a
decisive negative result on the specific "re-route to endpoint" lead (works ~86% but not always,
with concrete counterexamples), ruling out treating it as a one-step surgical proof technique.

### Dead ends (do not retry)
- Per-fixed-`j` Small-Gap Crossing-Domination Lemma (exact counterexample, `p=4`, `Y=(92,89,77,73)`,
  `j=3`) — already recorded, reconfirmed.
- "Re-route to nearest endpoint of the offending crossing arc" as a **single local-surgery step**
  — now shown to fail on `~14%` of mismatch cases with concrete counterexamples (this round). Any
  future use of this idea must be recursive/global, not a one-shot swap.
- "The two extreme partners `j=1,p` always suffice for the aggregate" — fails on `~19%` of trials
  (this round), concrete counterexamples on file.
- Sorted-adjacency conjecture, local pairwise uncrossing-exchange, per-partner form, non-crossing
  matching+deletion at general `b` — all previously dead, unchanged, not re-tested this round.

### Small-case / intuition notes (all conjecture, backed by exact-integer computation)
- The aggregated equality (`OPT(Y,p-1)=NC(Y,p-1)`, equivalently the aggregated crossing-domination
  lemma) holds in every one of ~1000+ fresh trials this round (`p` up to `8`) — strong conjectural
  support, not a proof.
- The mechanism compensating a per-`j` crossing advantage is **not local**: the winning alternate
  partner's optimal selection is frequently a completely different structure (often near-total
  deletion) unrelated to the specific crossing arc that caused the original mismatch — this is the
  main new qualitative insight from this round's probing, and it argues for a global/counting or
  recursive-induction technique over a local-exchange one.
- Degenerate splits (`j\in\{1,p\}`, equivalently "full slack, no real inside/outside split")
  behave like a strictly easier sub-case where equality is unconditional — a natural anchor/base
  case for any inductive attempt.
