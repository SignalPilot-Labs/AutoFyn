## imo-2026-03 (lens: construct the induction-on-|rest| breakpoint proof for Gap 1b, the Sum Bound)

### Setup used (verified against the file, not re-derived blind)

Implemented an independent exact-`Fraction` harness (`OPT_sigma(B,Z)` via the certified
Generalized Multi-Background Peeling Lemma's DELETE/KEEP/MATCH trichotomy, §13.2) and
cross-checked it against a from-scratch brute-force enumeration of all `(K,D,M)` selections:
**800/800 matches, 0 mismatches** — the harness is trustworthy. Also implemented the base
generator exactly per §17.2 item 1 (`B_0`, `Z_0`, `A_1`, `A_{3,l}`, trigger `M<A_1`, global
argmin `k^*`, `C=B_0\cup\{d_{k^*}\}`, `W=Z_1`) and DELETE-closure, and generated genuine
`\mathcal F`-provenance instances at `|\mathrm{rest}|=0,1,2,3` for concrete experiments.

### What the induction should look like (precise statement worked out)

**Induction hypothesis, stated precisely:** For every `k\ge0`, `P(k)`: "for every genuine
`\mathcal F`-provenance node `(C,W,+1)` with `C=\{c_1,c_2\}`, `h=0` (i.e. `|C_{\mathrm{lo}}|=2`),
and `|\mathrm{rest}|:=|W|-1=k` (`\mathrm{rest}:=W\setminus\{w_1\}`, `w_1:=\max W`), the Sum
Bound `w_1\ge\mathrm{OPT}_{+1}(C,\mathrm{rest})+\mathrm{OPT}_{-1}(C,\mathrm{rest})` holds."
Prove `P(k)` for all `k` by strong induction.

**Base case `k=0` (`\mathrm{rest}=\emptyset`).** Reduces to the fully explicit claim
`w_1\ge2|c_1-c_2|` for genuine triggered `(b_0,d_{k^*})` pairs (`c_1=b_0`, `c_2=d_{k^*}`).
**Important finding: this base case is NOT actually proved anywhere on file** — round 13/14
only computationally corroborated it (found the ratio's asymptotic infimum is exactly `2`,
never below, via the family `Z_0=(n,n,n+1),b_0=n/2`) but no rigorous proof of `w_1\ge2|c_1-c_2|`
using the trigger `M<A_1` and `k^*`'s global-argmin property has been attempted. **Any builder
who starts the induction-on-`|\mathrm{rest}|` strategy must first close this base case as its
own lemma** — it is the anchor, and it is honestly still open, not just "the easy case."

**Inductive step, mechanism confirmed viable but genuinely harder than a flat 3-type check.**
Freeze every coordinate of the *original* `(B_0,Z_0)` except one (a single `z_i\in Z_0`), and
let `x` vary continuously. `C`, `W`, `w_1`, `\mathrm{rest}` are then themselves piecewise-linear
(in fact piecewise-*combinatorially-determined*) functions of `x`, because they are built by
composing several nested `\min`/`\max`/argmin operations (`A_1`, each `A_{3,l}`, the trigger
comparison, DELETE/KEEP closure) — each individually piecewise-linear by the certified Vertex
Lemma's own mechanism, and a **composition of piecewise-linear maps is piecewise-linear**, so
`G(x):=w_1-\mathrm{OPT}_{+1}(C,\mathrm{rest})-\mathrm{OPT}_{-1}(C,\mathrm{rest})` is genuinely
piecewise-linear in `x`. This is the correct generalization of the Vertex Lemma to this setting
— confirmed computationally (see below), not merely asserted.

### Computational findings (new this round)

1. **Shallow case (`|\mathrm{rest}|=1`) exactly matches the hoped-for picture.** Concrete
   instance: `B_0=(3),Z_0=(12,8,7,7)` gives `C=(3,5),W=(7,7)`, tight (`w_1=7=\mathrm{OPT}_{+1}+
   \mathrm{OPT}_{-1}=1+6`). Sweeping the perturbed coordinate `x` (originally `8`) over `[0,12]`
   in `1/4`-steps: `G(x)` is a genuine zigzag, **touching exactly `0` only where `x` ties an
   element of `C` (`x=3` or `x=5`, a Lemma-P duplicate) or `x` ties `w_1$ itself (`x=7`)**, and
   strictly positive everywhere else in the sampled range. This is exactly breakpoint type (i)
   from §21.2 — validates the mechanism at this shallowest nontrivial level.

2. **Deeper case (`|\mathrm{rest}|=2`) surfaces two new, previously-unflagged subtleties, not a
   dead end but real extra bookkeeping a builder must handle:**
   - **Argmin ties spawn multiple simultaneous live branches of `\mathcal F` at one base
     generator, some in-scope (`h=0`) and some NOT (`h=1`, background dominates).** At one swept
     `x`, three/four values of `l` tied for the argmin simultaneously; two of the resulting
     branches had `C` containing an element `>w_1$ (`h=1`, e.g. `C=(2,11),w_1=10`) and showed
     `G=-2` and `G=-4$ — these LOOK like Sum Bound violations but are simply **out of the Sum
     Bound's declared scope** (`h=0` required) — confirmed by re-checking: restricting to
     genuine `h=0` branches only, **0/100 violations** in this sweep. **Lesson for the builder:**
     any computational or inductive argument that walks argmin-tie branches must filter `h=0`
     explicitly at *every* branch, not just the "main" one — it is easy to mistake an
     out-of-scope dominated branch for a counterexample.
   - **A genuine continuous SUB-INTERVAL of exact equality (`G\equiv0`), not just isolated
     points.** For fixed `c_1=2`, fixed `\mathrm{rest}=(10,0)`, `w_1=10`, sweeping `c_2=11-x`
     over `x\in[8.25,9.75]` (equivalently `c_2\in[5/4,11/4]`... concretely `c_2\in\{11/4,\dots,
     5/4\}` sampled densely including non-grid points `c_2=101/100$ etc.) gives `G=0` **exactly**
     throughout, not approximately. This is a **sharper tightness finding than round 14's**
     (which found isolated finite-rational equality witnesses, `\approx2.5\%` of triggered
     checks) — here a whole *interval* of the Sum Bound is tight. This does not break the
     breakpoint/Vertex-Lemma mechanism (a flat, zero-slope affine piece is still "affine,
     extremum realized throughout," consistent with induction logic) but it does mean the
     tightness structure is richer than a discrete set of witnesses — a proof must handle
     flat zero pieces, not assume finitely many isolated tie points.

3. **Tested and REFUTED a natural potential shortcut identity** (would have been a big
   simplification if true): "`\mathrm{OPT}_{+1}(C,\mathrm{rest})+\mathrm{OPT}_{-1}(C,\mathrm{
   rest})=\max(\mathrm{rest})` whenever `C` is dominated by `\mathrm{rest}` (both `C`-elements
   `\le\max(\mathrm{rest})`)." This held in the one example that surfaced the flat interval above,
   but is **FALSE in general**: `306/1888` violations on arbitrary such `(C,\mathrm{rest})` (both
   directions of failure, sum above and below `\max(\mathrm{rest})`) — **do not pursue this as a
   shortcut**, it was a coincidence of that specific `(2,t),(10,0)` shape (small `\mathrm{rest}`,
   a duplicated/degenerate element), not a real lemma.

### Where the induction genuinely gets harder than the certified Vertex Lemma

The Vertex Lemma's breakpoint argument is clean because the varying quantity (a cut position
`t`) is a **directly free parameter of a real player's move**, with "everything else" held
literally fixed by hypothesis. Here, `C`, `\mathrm{rest}`, `w_1` are all **derived** quantities —
outputs of the argmin/trigger/DELETE-KEEP-closure pipeline applied to the true free parameters
`(B_0,Z_0)`. Freezing "everything except one coordinate" must be done at the `(B_0,Z_0)` level,
and the induced deformation of `(C,\mathrm{rest},w_1)` passes through several nested `\min`/`\max`
layers before reaching the Sum Bound's own two recursive calls `\mathrm{OPT}_{\pm1}(C,\mathrm{
rest})` — each of which is *itself* the same DELETE/KEEP/MATCH recursion one level down, so
breakpoints can arise **inside that inner recursion** too (confirmed: the `|\mathrm{rest}|=1`
zigzag's slope changes came from `x` crossing values inside the inner `e(\cdot)` computation, not
only from the three named outer types). The outline-reviewer's round-14 precision note ("the
three breakpoint types are the BASE CASE classification only, not the full enumeration") is
correct and is exactly what this round's `|\mathrm{rest}|=2` sweep independently confirms: a
correct inductive step needs to classify breakpoints **recursively** (by strong induction on the
depth of the DELETE/KEEP/MATCH recursion generating `\mathrm{OPT}_{\pm1}(C,\mathrm{rest})`
itself, not just on the outer `|\mathrm{rest}|`), and at each such inner breakpoint, show the
resulting configuration is either (a) a genuine value-tie reducible via Lemma P/Rank-Extraction to
a strictly smaller Sum-Bound instance (apply IH), or (b) an argmin/trigger-boundary event that
changes *which* `\mathcal F`-branch is live but does not itself require the Sum Bound at that
exact point (a bookkeeping case, not a new inequality to prove).

### Verdict on viability

The induction-on-`|\mathrm{rest}|` strategy is **structurally sound and not obviously doomed** —
every breakpoint found in these experiments (both the shallow `|\mathrm{rest}|=1$ and the deeper
`|\mathrm{rest}|=2` sweep) was traceable to either a Lemma-P-style duplicate/tie (reducible) or an
out-of-scope (`h\ne0`) branch (irrelevant, must be filtered), never to an unexplained residual —
but it requires **two concrete, currently-missing pieces of work**, not yet attempted by any
builder: (1) a rigorous proof of the base case `w_1\ge2|c_1-c_2|` using the trigger and
`k^*`'s global-argmin property directly (currently only numerically corroborated); (2) the
inductive step must be phrased as an induction on the *recursion depth of the DELETE/KEEP/MATCH
evaluation itself* (equivalently, a nested/strong induction that also handles breakpoints
strictly inside `\mathrm{OPT}_{\pm1}(C,\mathrm{rest})`'s own computation), not a single outer
`|\mathrm{rest}|`-indexed case check — a flat enumeration at the outer level alone (as originally
sketched in §21.2 before its own precision-note correction) will miss real breakpoints, confirmed
computationally this round.

### Cheap-kill candidates
- Filter branches by `h=0` explicitly whenever walking argmin-tie sets — an easy source of false
  "counterexamples" (confirmed: 2 apparent violations in this round's sweep were both `h=1`,
  out of scope, not real).
- The "`\mathrm{OPT}_{+1}+\mathrm{OPT}_{-1}=\max(\mathrm{rest})`" shortcut is dead (306/1888
  failures) — do not re-propose.

### Knowledge-base entries to use
- **General Proof Methods — Induction** (`knowledge_base.md` §"General Proof Methods"): "pick the
  right variable to induct on" — this round's finding is precisely that the "right variable" is
  not simply `|\mathrm{rest}|` at the outer level but effectively the recursion depth of the whole
  nested DELETE/KEEP/MATCH evaluation; a flat single-index induction is insufficient.
- **Pigeonhole / extremal** and **Invariant/monovariant** entries are the same family already
  underlying the certified Vertex Lemma (piecewise-linear, extremum at breakpoint) — reuse that
  lemma's proof shape directly, not a new technique.
- No new crux-corpus match beyond what's already on file for this problem (the corpus is
  disjoint from imo-2026-03 and no subtopic search this round turned up anything closer than the
  already-cited "extremal witness + secondary tie-break + local rewrite" shape from round 13 for
  Gap 1c — not directly relevant to Gap 1b's breakpoint mechanism, which is purely internal to
  this problem's own recursive value functions).

### Analogous past problems (cruxes)
None newly found this round specific to Gap 1b's breakpoint/induction mechanism — it is an
internal structural argument about this problem's own `OPT_\sigma` recursion (piecewise-linearity
composed through nested argmin/trigger machinery), not a pattern with an obvious external
crux-corpus analog beyond the Vertex Lemma machinery already imported.

### Prior progress
`lemmas/vertex-lemma.md` (certified, the base mechanism this induction generalizes);
`potential-weighting-upper-bound.md` §21.2 (round-14 outline, breakpoint mechanism proposed but
not built, with the outline-reviewer's own precision note already correctly flagging the
"3 types is base-case-only" issue that this round's computation independently confirms).

### Dead ends (do not retry)
- "`\mathrm{OPT}_{+1}(C,\mathrm{rest})+\mathrm{OPT}_{-1}(C,\mathrm{rest})=\max(\mathrm{rest})`
  whenever `C` is `h=0`-dominated by `\mathrm{rest}`" — FALSE in general, 306/1888 failures
  (new this round).

### Small-case / intuition notes (all labeled conjecture/corroboration, not proof)
- Base case (`\mathrm{rest}=\emptyset`) ratio `w_1/|c_1-c_2|\to2`, asymptotically tight, matches
  round 13/14 — reconfirmed structurally via the `|\mathrm{rest}|=1$ sweep's zigzag touching zero
  at `x=3$ (a value equal to `c_1`) and `x=7` (equal to `w_1`), i.e. duplicate-tie mechanism is
  the source of tightness, consistent with the `Z_0=(n,n,n+1)` family's own duplicate-driven
  degeneration.
- New, sharper-than-round-14 finding: exact equality can hold over a **continuous interval**, not
  just isolated points (`|\mathrm{rest}|=2` example, `c_2\in[5/4,11/4]$ with `c_1=2,\mathrm{rest}=
  (10,0),w_1=10` all fixed) — flag this explicitly to whichever builder attempts the base case or
  inductive step, since it means "the Sum Bound has zero slack along a whole sub-locus," a
  stronger structural fact than "finitely many exact-equality witnesses."
