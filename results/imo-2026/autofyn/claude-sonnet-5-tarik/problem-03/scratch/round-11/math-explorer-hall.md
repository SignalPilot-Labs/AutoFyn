## imo-2026-03 — Hall's-theorem / defect-Hall reformulation of the Match-Recovery Lemma: verdict

**Scope (per dispatch):** investigate whether `OPT(Y,p-1)=NC(Y,p-1)` (equivalently the unified
Match-Recovery Lemma of `potential-weighting-upper-bound.md` §13.3/§14) can be genuinely
reformulated as a bipartite-matching-feasibility question solvable via Hall's theorem, per the
`aimo-0063` lead flagged in `/tmp/round-10/math-explorer-crux-search.md`. Retrieval + reformulation
attempt + computational stress test only — no proof attempted.

### 1. The actual aimo-0063 mechanism (pulled from the corpus, not just the crux stub)

`aimo-0063` = USAMO 2025/6 (cupcakes on a circle). Full statement and solution read from
`past_problems_database.json`; both of its two cruxes read from `past_crux_moves_database.json`.
Precise mechanism:

- **Bipartite graph.** Left side = the `n` **people**. Right side = the `n` **arcs of one fixed
  person Pip's own valid partition** of the circle. Edge `(person, arc)` iff that person's score
  of that arc is `\ge 1` ("compatible"/"happy").
- **Hall step.** If a perfect matching exists, done. If not, Hall's condition fails: some set
  `B_1` of people has fewer than `|B_1|` compatible arcs. **Delete `B_1` and its whole
  neighborhood** (those arcs), leaving a smaller circle with fewer people and fewer arcs. Iterate.
  Pip is a **universal vertex** (compatible with all `n` of her own arcs, by definition), so `{Pip}`
  can never be part of a deficient set — this guarantees the terminal matching `\mathcal M` is
  nonempty, hence progress, hence termination.
- **Second crux (the part that makes the induction actually close, and the part most people
  forget when summarizing this problem as "just Hall"):** for an unmatched person `Q`, every
  deleted/committed arc has `Q`-value `<1`, hence (since each of `Q`'s own parts is worth `\ge1`)
  a deleted arc can never contain a *whole* part of `Q`'s own partition — it can only touch at
  most one endpoint. So deleting it merges at most two of `Q`'s adjacent parts into one, of value
  `\ge(\ge1)+(\ge1)-(<1)>1`. This is what lets the induction on the shrunk circle go through for
  every still-unmatched person, not just the deleted set.

Two structural facts about *why* Hall's theorem is the right tool here: (a) the target is a
genuine **`n`-way simultaneous assignment** (every one of the `n` people needs their own arc, all
at once) — Hall's theorem is precisely the tool for "does a system of `n` simultaneous choices,
each independently checkable, admit a witness"; (b) the compatibility relation is **separable**:
whether person `P` likes arc `A` depends only on `P` and `A`, never on what any other person gets.

### 2. Attempted reformulation for Match-Recovery, and why it collapses

Match-Recovery's statement (§13.3): fix background `B`, sorted `Z=(z_1\ge\dots\ge z_q)`. If the
unrestricted-match minimum `\min_k \mathrm{OPT}_{+1}(B\cup\{z_1-z_k\}, Z\setminus\{z_1,z_k\})`
strictly beats DELETE/KEEP, some `k` has `\mathrm{TAGGED}_{+1}(\dots,k-1)\le` that minimum.

**First obstruction — the wrong arity.** aimo-0063 needs Hall's theorem because it has `n`
*simultaneous* decisions (all people at once) whose joint feasibility is the question. Match-
Recovery, at a single recursion level, has exactly **one** decision: which `k\in\{2,\dots,q\}` is
`z_1`'s partner. "Does some `k` satisfy a scalar inequality" is a plain existential quantifier
over one variable, not a system-of-representatives question. Specializing Hall's theorem to a
bipartite graph with a single right-vertex (the "target achieved" slot) and left-vertices `k`
degenerates Hall's condition to "at least one edge exists" — i.e. it becomes a verbatim restatement
of the thing to be proved, with zero mechanism supplied. This is not a minor technical gap; it is
definitional: Hall's theorem only has content when there are `\ge2` simultaneous slots to fill.

**Second obstruction — even the natural multi-way version has no deficiency to exploit.** One
might instead try to Hall-ify the *whole* non-crossing-matching question at once: does a
non-crossing perfect matching of some fixed support `S` (the index set actually used by an
`OPT`-achieving selection) exist that reproduces (or beats) the optimal value? I checked this
directly: **existence of a non-crossing completion for a fixed choice of who is paired with whom
is never the obstruction.** For any point set of even size, some non-crossing perfect matching
always exists (e.g. the nested/nearest-neighbor construction) — there is no analogue of a Hall
deficient set here, because "pair index `0` with index `k`, complete the rest non-crossingly" is
always achievable (finish the two side-intervals independently, e.g. by nested pairing or
KEEP/DELETE). Ran this as an exact check (code below): across every instance tested, including
every instance where `OPT\ne\mathrm{TAGGED}`/`NC`, **the existence side never once failed** — the
gap is 100% a **value** (optimality) gap, never an **existence** (feasibility) gap.

**Third, structural, obstruction (the real reason, not just an empirical correlation).**
aimo-0063's Hall step works because "person `P` likes arc `A`" is checked **independently per
edge** — no interaction between different people's assignments. `e()`'s alternating sum is the
opposite: it depends on the **joint sorted rank** of *all* currently-selected values (`K`-values
and `M`-differences together) — this is exactly why the population's actual load-bearing tools are
Fact 3 / the General Rank-Extraction Identity (`e(F)=e(\mathrm{head})+(-1)^{r-1}x+(-1)^r
e(\mathrm{tail})`), which explicitly tracks how one element's rank among *all* others flips signs
throughout the whole multiset. There is no way to assign a per-edge (per-candidate-`k`) binary
"compatible/incompatible" label whose Hall-feasibility would be *equivalent* to the needed
inequality, because whether partner `k` "works" depends on the ranks of every other selected value
too, not on `k` in isolation. Hall's theorem is a tool for **separable, existence-only** feasibility;
Match-Recovery's difficulty is **globally coupled, value-only** optimality. These are different
mathematical objects, not two framings of the same fact.

### 3. Computational stress test (exact integer arithmetic, `p/q\le8`)

Script: brute-force enumeration of all `(K,D,M)` selections (`|D|+|M|\le` budget), `e()` as the
alternating sum of sorted values, non-crossing check on `M`'s index pairs.

**Round-10 counterexample, `B={2,4}`, `Z=(6,3,2,1)`, budget=4 (i.e. `|B|=2` regime where
`OPT\ne\mathrm{TAGGED}`):**
```
OPT = 0   TAGGED(untagged, s=0) = 1   (confirms file's claim exactly)

k   exists a non-crossing completion using pair (0,k)?   unrestricted min via (0,k)   NC-restricted min via (0,k)
1                     True                                        1                            1
2                     True                                        0                            1
3                     True                                        1                            1
```
Every candidate partner `k` **can** be completed non-crossingly — existence is never in question.
The failure is that partner `k=2` achieves the unrestricted global minimum `0`, but *no*
non-crossing completion through `k=2` (nor any other `k`) reaches `0` — a pure value gap.

**Top-level instance `Y=(7,5,4,4,3,1)`, `p=6`, `b=5` (the theorem's own target regime, `B=\emptyset`):**
```
OPT = 0 = NC   (equality holds here, consistent with the theorem's own claim at b=p-1)
```
All partners `k=1..5` non-crossingly completable, no existence issue, consistent with case above.

**Systematic sweep** (`/tmp/hall_sweep2.py`, exact integers, `q=2..7`, `|B|=0..3`, full slack
budget `=q`, 2000 trials): **26/2000 mismatch instances (`OPT\ne NC`)**, consistent with the file's
own reported failure rates at `|B|\ge2`; **0/2000 existence failures**, including inside every one
of the 26 mismatch instances — i.e. in every single case where the aggregate equality fails, every
candidate match partner was still non-crossingly *realizable*; the shortfall is always a strictly
worse *value*, never an unreachable partner.

### 4. Honest verdict

**Not viable — this collapses, not a genuinely usable alternative shape.** Working out the
translation precisely (per the dispatch) rather than leaving it at the "structurally similar
existential claim" level shows two independent, decisive reasons Hall's theorem does not transfer:

1. Match-Recovery's per-level decision is a **single** existential quantifier (one `k` among
   several), not a simultaneous multi-way system; Hall's theorem specialized to one slot is
   vacuous (restates the claim, proves nothing).
2. Even generalized to "does some non-crossing completion of the whole matching achieve the
   target value," the **existence** half is always trivially true (0 failures across 2000+ exact
   trials, including every known counterexample instance on file) — there is no deficient set for
   Hall's theorem to find, because the actual difficulty is a numerical **optimality** gap in a
   **globally rank-coupled** objective (`e()`'s alternating sum over joint sorted rank), which is
   structurally the opposite of the **separable, per-edge** compatibility relation Hall's theorem
   requires to have any content.

This is a clean, structural mismatch, not merely "harder than it looked" — recommend **not**
opening an approach around this specific mechanism. This does not touch the two other openings
already surfaced in `/tmp/round-10/math-explorer-crux-search.md` (`aimo-0043`'s obstacle-
charging/resource-transfer between branches, and `aimo-0558`'s greedy+injective-charge), which
remain the more structurally apt leads for the Match-Recovery Lemma's actual difficulty (an
aggregation/compensation fact, not an existence-feasibility fact) — and does not touch the live
§14 Fixed-Support Uncrossing route currently being pursued for `OPT(Y,p-1)=NC(Y,p-1)` at `b=p-1`,
whose open Single-Swap Non-Increase Lemma is a value-sign question (exactly matching the
diagnosis above: the content is about how `e()`'s value changes under a rank-preserving local
swap, not about whether some assignment exists).

### Dead end to record
- **Hall's theorem / defect-Hall reformulation of the Match-Recovery Lemma (or of
  `OPT(Y,p-1)=NC(Y,p-1)` generally) as a bipartite-matching-feasibility claim — RULED OUT.**
  Reason (structural, not just empirical): the claim's difficulty is a value/optimality gap in a
  globally rank-coupled objective; Hall's theorem only has content for separable multi-way
  existence questions, and in this problem existence of a non-crossing completion for any
  candidate partner is always trivial (0/2000+ exact-trial failures, including on file's own
  counterexample instances). Do not re-attempt this specific translation in future rounds.

### Files
- Computation: `/tmp/hall_check2.py` (single-instance analyzer), `/tmp/hall_sweep.py` /
  `/tmp/hall_sweep2.py` (systematic sweeps, exact-integer, `q\le7`, `|B|\le3`).
- Read in full: `results/imo-2026-03/current.md`,
  `results/imo-2026-03/approaches/potential-weighting-upper-bound.md` §13.1–§13.6, §14,
  `crux_moves_documentation.md`, `/tmp/round-10/math-explorer-crux-search.md`,
  `past_crux_moves_database.json` / `past_problems_database.json` entries for `aimo-0063`.
