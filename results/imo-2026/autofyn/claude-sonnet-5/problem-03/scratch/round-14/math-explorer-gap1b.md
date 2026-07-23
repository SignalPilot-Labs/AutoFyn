## imo-2026-03 — Gap 1b (Sum Bound conjecture)

### Setup reconstructed and independently re-verified
Built a from-scratch exact-`Fraction` implementation of: `e(multiset)` (sorted-descending
alternating sum), the recursive DELETE/KEEP/MATCH `OPT_σ(C,W)` (brute-force over every way of
partitioning `W` into deleted/kept/matched-pairs, not merely a re-implementation of the file's own
peeling code — this is the literal definition, used as an independent sanity check on the peeling
recursion too), and the base-generator construction (`A_1`, `M=A_{3,k*}`, trigger `M<A_1`, `k*` a
global argmin) exactly as specified in `potential-weighting-upper-bound.md` §17.2/§19.3. Reproduced
the round-13 reviewer's extremal family `Z_0=(n,n,n+1), b_0=n/2` bit-for-bit (`n=4..100`: ratio
`w_1/|c_1-c_2| = 2n/(n-2)`, trigger holds every time) — confirms the reviewer's correction (asymptotic
infimum exactly `2`, not the builder's wrongly-claimed "`≥3`") is right.

### New finding 1 (sharper than round 13): the bound is tight in an ABSOLUTE sense too, not just in ratio
Round 13 only exhibited a family where the ratio `→2` while the additive gap `w_1-2|c_1-c_2|` stayed
at a constant `2` (never shrinking). I found a genuinely sharper 2-parameter family: fix
`Z_0=(n+t,n,n)` (a near-tie, `t>0` small) and push `b_0\to n/2^-` (the point where `A_1=\min(b_0,n-b_0)`'s
two branches cross). At this configuration the trigger `M<A_1` holds for **every** `b_0<n/2` (since
`M=b_0-t<b_0=A_1` automatically, for any `t>0`), so `b_0` can be pushed all the way to `n/2^-`, giving
`\mathrm{gap}=w_1-2|c_1-c_2|\to 2t`. Taking `t\to0^+` as well drives the gap to `0`. Verified exactly:
```
n=100,  t=1/5,  b0=n/2-1/100:  gap=0.420,  ratio=2.0084
n=100,  t=1/10, b0=n/2-1/1000: gap=0.202,  ratio=2.0040
n=1000, t=1/20, b0=n/2-1/1000: gap=0.102,  ratio=2.0002
n=10000,t=1/50, b0=n/2-1/10000:gap=0.040,  ratio=2.0000
```
So the true infimum of `w_1-2|c_1-c_2|` over the `\mathrm{rest}=\emptyset` sub-case is **`0`**, not any
positive constant — there is **no uniform additive slack at all**, only the multiplicative constant
`2` survives. Any proof of this sub-case must be an essentially-tight inequality (no room for a lossy
intermediate bound), and the extremal limit is exactly the **fully-degenerate triple tie**
`Z_0\to(n,n,n)` combined with `b_0\to n/2` — i.e. the point where **two structural things
simultaneously degenerate**: (a) the matched partner `z_{k^*}` becomes an exact duplicate of the
surviving element `w_1` (a Lemma-P-style duplicate-pair configuration), and (b) `b_0` sits exactly at
the *tie point* of `A_1`'s own two candidate branches (delete-vs-keep the duplicated pair).

### New finding 2 (stronger, general, non-asymptotic): exact equality is attained at genuine finite instances of the FULL Sum Bound, not just approached in a limit
Ran a broader random search (not restricted to `rest=∅`, checking the literal Sum Bound
`w_1\ge\mathrm{OPT}_{+1}(C,\mathrm{rest})+\mathrm{OPT}_{-1}(C,\mathrm{rest})` at every DELETE-closure
depth reachable from random base generators, `q\le5$–$6`, rational entries, ~1500 combined
triggered checks): **found exact equality (`w_1 = \mathrm{OPT}_{+1}+\mathrm{OPT}_{-1}$ exactly, zero
slack) at genuine finite `\mathcal F`-provenance instances**, and it is not rare — `21/822` triggered
checks in one sweep hit exact equality (`\approx2.6\%`). Concrete witness (independently verified,
exact fractions):
```
Z_0 = (8, 25/4, 25/4, 55/12, 13/3),  b_0 = 23/6
 -> A_1=1/2, M=1/6, trigger M<A_1 holds (1/6<1/2)
 -> k* gives C = (23/6, 11/3), diff = 1/6
 -> W = (25/4, 25/4, 55/12), w_1 = 25/4, rest = (25/4, 55/12)
 -> OPT_{+1}(C,rest) = 1/6,  OPT_{-1}(C,rest) = 73/12
 -> sum = 1/6 + 73/12 = 75/12 = 25/4 = w_1   EXACTLY.
```
**Diagnosis of the mechanism at this witness:** `\mathrm{OPT}_{+1}(C,\mathrm{rest})=1/6=e(C)` (i.e.
deleting all of `rest` is already optimal for the MIN direction), and by the certified Rank-Extraction
identity `\mathrm{KEEP}=w_1-\mathrm{OPT}_{-1}(C,\mathrm{rest})=25/4-73/12=1/6=\mathrm{DEL}`. **So this
equality witness is precisely a node where `\mathrm{KEEP}=\mathrm{DEL}` exactly** — a genuine *tie*
between the two branches one level up, not a coincidence of the specific numbers. This is exactly the
shape of degeneracy the population's own certified **Vertex Lemma** (`lemmas/vertex-lemma.md`,
piecewise-linear single-cut optimum + tie/bisect/degenerate classification) was built to handle
elsewhere in this problem, and matches the "extremal case = duplicate/tie configuration" pattern
already flagged in `/tmp/memory/math-explorer.md` rule 14 (round 6) and rule 21 (round 8).

### Candidate proof mechanism (recommended to the outliner — NOT attempted here)
Both findings point to the **same** technique: treat `w_1-\mathrm{OPT}_{+1}(C,\mathrm{rest})-
\mathrm{OPT}_{-1}(C,\mathrm{rest})` as a function of one continuously-varying real parameter (e.g.
`b_0`, or any single `z_i`, with everything else in `Z_0` frozen). Since `\mathrm{OPT}_{+1}` is a min
and `\mathrm{OPT}_{-1}` is a max of finitely many affine functions of that parameter (this is exactly
what the DELETE/KEEP/MATCH recursion computes — a finite case split, each case affine in any single
frozen-shape coordinate), the difference is **piecewise-linear**, hence its minimum over any
interval is attained either (i) in the interior of a linear piece — impossible for a non-constant
affine function unless the whole piece is constant — or (ii) at a **breakpoint**, where two
candidate branches of some `\min`/`\max` tie. This is the exact mechanism that already closed the
"all-cycles" gap (Shared-Value Cycle-Breaking Lemma, rounds 6-7) and underlies the Vertex Lemma
itself. **Concretely recommended next step:** enumerate the finitely many breakpoint TYPES for the
Sum Bound's defining recursion (tie between `A_1`'s own branches; tie between `\mathrm{OPT}_{+1}`'s
delete/keep/match branches at the top of `\mathrm{rest}`; the matched partner `d_{k^*}` colliding
with another `z`-value) and show the Sum Bound reduces, AT each breakpoint, to a lower-dimensional
identity that is either (a) a genuine duplicate/tie configuration handled by Lemma P (as in finding 1)
or (b) exactly the `\mathrm{KEEP}=\mathrm{DEL}` tie condition (as in finding 2) — which may connect
directly to the already-open "No-Second-Trigger"/SAR machinery in §17-18, since both concern exactly
when two of `\{\mathrm{DEL},\mathrm{KEEP},\mathrm{MATCH}\}$ tie for the optimum. **This is a genuine
lead, not a proof** — the breakpoint enumeration and the reduction-at-each-breakpoint step have not
been attempted, only the extremal witnesses that motivate them.

### Cheap-kill candidates
- None found that dispatch the whole Sum Bound cheaply — the generic dominance facts (Facts 1&2,
  `e(M)\ge0`, `e(M)\le\max(M)`) are already known (round 13, file §19.5(a)) to be too weak (the Sum
  Bound fails 4-12% of the time for arbitrary same-shape backgrounds, so any correct argument must
  use the trigger/argmin provenance, confirmed again here: my searches only ever found violations
  attempted-and-failed within genuine `\mathcal F`-provenance, 0/~2300 combined checks this round).
- One structural pruning that IS cheap: whenever `\mathrm{OPT}_{+1}(C,\mathrm{rest})=e(C)` exactly
  (i.e. "delete everything" already optimal for MIN), the Sum Bound reduces immediately to
  `\mathrm{KEEP}\ge\mathrm{DEL}` at the level above via the Rank-Extraction identity — worth checking
  whether this sub-case ("delete-rest already optimal") is provably EASIER or even always true when
  `C`'s two elements are both `<\min(\mathrm{rest})$ (a size/dominance pre-check), before attempting
  the general case.

### Knowledge-base / crux corpus
No new generic KB entry fits better than what's already in play. The relevant "knowledge base" for
this specific mechanism is internal to the population itself: `lemmas/vertex-lemma.md` (piecewise
linearity + tie/degenerate classification — exactly the shape needed here) and
`lemmas/general-rank-extraction-identity.md` (already used above to interpret the equality witness as
a KEEP=DEL tie). Per CLAUDE.md's crux-corpus instruction: did not find a subject-matter match beyond
what round 13's `math-explorer-crux-search.md` already reported (extremal-witness + secondary
tie-break + local-rewrite shape, `aimo-0960`/`aimo-0438`/`aimo-0666`) — that shape is for Gap 1c
(MATCH-vs-DEL/KEEP), not this piecewise-linear/breakpoint mechanism for Gap 1b, which is better
matched by the population's own internal Vertex Lemma technique than by any external crux; did not
force a new crux match for Gap 1b specifically.

### Dead ends (do not retry)
- A fully general, provenance-free Sum Bound (arbitrary `C`, arbitrary background shape) is already
  confirmed FALSE by round 13 (4-12% failure) — reconfirmed indirectly here (every violation-free
  result required genuine `\mathcal F` base-generator provenance).
- Do NOT report the `\mathrm{rest}=\emptyset` sub-case as having "comfortable slack" of any kind —
  confirmed this round that the slack (both additive and, in a stronger sense, exact-equality
  instances of the FULL Sum Bound) can be driven to exactly `0`. Any future round's proof attempt
  must target a **tight, no-slack** inequality, not a loose one.

### Prior progress (context)
- Gap 1a (No-Gap Lemma base case) and Gap 1c (MATCH-vs-DEL/KEEP) remain untouched by this round —
  out of this lens's scope (dispatched specifically to Gap 1b). See `current.md`/§19-20 for their
  status.
- Gap 1b itself: still unproved. This round's contribution is (i) a corrected, sharper
  characterization of exactly how tight it is (ratio `\to2` AND additive gap `\to0`, plus literal
  exact-equality at finite instances — strictly sharper diagnosis than round 13's), and (ii) a
  concrete, not-yet-attempted candidate proof MECHANISM (piecewise-linear/breakpoint argument via the
  already-certified Vertex Lemma technique, with the KEEP=DEL tie as the concrete breakpoint
  condition) — not a proof.

### Small-case / intuition notes (all labeled conjecture, not proof)
- Conjecture: the Sum Bound's extremal/tight instances are always characterized by a tie somewhere in
  the DELETE/KEEP/MATCH decomposition one level up (either `A_1`'s own branches tying, as in finding
  1, or `\mathrm{KEEP}=\mathrm{DEL}` exactly, as in finding 2) — i.e. genuine slack exists strictly
  away from all such ties, and a breakpoint/vertex argument localizes all the hard content to these
  finitely-many tie configurations. Corroborated by 2 independently-constructed witnesses (one
  asymptotic family, one exact finite instance) but not tested systematically enough to call more
  than a strong hunch.
- Numerically, exact-equality instances of the Sum Bound are not rare (~2.5% of triggered `\mathcal
  F`-checks in a modest random sweep) — this is evidence the tight constant `2` (i.e. the Sum Bound as
  literally stated, with no room to spare) is the *correct* target to prove, not a coarser fallback
  like "`\ge1.5\times$" or similar with slack.
