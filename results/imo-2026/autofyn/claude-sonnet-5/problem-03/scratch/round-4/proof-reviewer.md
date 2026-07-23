# Round 4 proof review — imo-2026-03

Reviewed all three built approaches (`dyadic-cascade-induction`, `potential-weighting-upper-bound`,
`concavity-minimax-duality`) against `problems.jsonl`, `CLAUDE.md`'s rigor rules, and the
certified lemmas in `results/imo-2026-03/lemmas/`. All key claims were independently
re-derived (not just re-read) using exact `fractions.Fraction` computation, exhaustive/BFS
search, or from-scratch alternative derivations. Full scripts are reproduced inline below for
traceability.

---

## 1. `dyadic-cascade-induction` — verdict: **CHANGES REQUESTED** (Status: `partial`, correctly
self-reported, no overclaim found)

### 1a. The Step-0 fix (dropping D/M-completeness) — SOUND, verified

The round-3/4 skeleton (§5.2') had proposed restating the lower-bound target purely in D/M
operation language, which silently requires "D/M sequences = XY's entire physical strategy
space" (a completeness claim that is *not* established by the certified Lemma D/M — that lemma
proves only *achievability*, `g(A,m) ≤ h(A,m)`, the wrong direction for a lower bound). This
round's builder correctly abandoned that route (§5.2'' Part A) and instead derives the
Branch A / Case B1 / Case B2 / §5.2 case split (0, exactly 1, or ≥2 cuts landing inside `a_1`)
directly from physical cut points, with no completeness assumption:

> "XY's strategy" is fully and simply specified by (a) how many of its cuts land, in the final
> dissection, inside the piece descended from `a_1`, and (b) how many land inside fragments
> descended from `R`.

I independently checked this claim's soundness: since a cut point's effect depends only on
which piece occupies that point of the stick at the time of cutting, and disjoint cuts on
disjoint segments of the (fixed) original stick do not interact, the *final* dissection is
determined by the set of cut points alone, independent of order. This makes the case split by
"how many final cuts are descended-from-`a_1`" exhaustive and well-defined with **zero**
appeal to any operation-sequence formalism. I then re-read §5.1 (Branch A, Case B1, Case B2,
already fully proved, every `m`) line by line and confirmed the claim that it never actually
used D/M language — it uses Lemma P and Fact 2 directly on physical multisets throughout (see
lines 890-1024 of the approach file). **The fix is legitimate and costs nothing**; it is not
a bypass that reintroduces the same gap one step later — it genuinely removes the dependency.

### 1b. Facts 3, 4, 5 — independently re-verified, all correct

- **Fact 3 (block extraction)**: `e(F) = e(X) + (-1)^|X| e(Y)` for a dominance-split `F=X⊔Y`.
  Re-derived from scratch (trivial rank bookkeeping) and confirmed via 2000 random-trial exact
  `Fraction` checks with the dominance constraint enforced — no violation.
- **Fact 4 (single-insertion bound)**: `|e(Y∪{x}) − e(Y)| ≤ x`. Re-derived the head/tail
  decomposition argument by hand, confirmed the algebra is correct, and independently checked
  via 5000 random-trial exact `Fraction` tests — no violation.
- **Fact 5 (chain-cancellation)**: any `L`-element multiset can be driven to `e=0` exactly with
  exactly `L` cuts. This is the file's most consequential new claim ("Fact 5 in particular is
  claimed as a strong new structural result"), so I implemented the induction's construction
  **independently from scratch** (not by reading the proof and checking algebra, but by coding
  the actual recursive cutting procedure it describes) and tested it on 2000 random multisets
  of size 0–7: `e(final) = 0` exactly in every trial, mass conserved. **Confirmed correct.**
  The corollary (ceiling `max(M)` always exactly attainable within budget `K-1`) follows
  immediately and is a genuine, proved (not numerically-observed) diagnostic result: it rules
  out any future Step-4 argument of the shape "the residual provably stays below its ceiling
  within budget" — a real, useful negative finding, correctly not oversold as closing Step 4
  itself.

### 1c. The `m=4, i=3` worked instance — verified exactly

I independently recomputed the full table by exact-fraction grid search (`fractions.Fraction`,
3100 grid points over `g_1∈[6/31,12/31)`): the true minimum is exactly `3/31` (attained on the
plateau `g_1∈[8/31,10/31]`), matching the file's claimed table exactly (boundary values
`7/31, 3/31, 3/31, 3/31, 5/31` all reproduced). `3/31 > 1/31 = e_4` confirmed — no violation.
I also independently verified the two "does not generalize" claims with exact numbers:
Fact-2-alone gives a useless bound `0` at the plateau's left endpoint (true value `3/31`, "far
short" as claimed); Fact 4's insertion bound gives `E_0 - ℓ = 7/31 - 12/31 = -5/31` (negative,
"worse than useless" as claimed) — both concrete numeric witnesses check out exactly. The
"does not generalize" claim is honestly scoped: the file explicitly states only this one
`(m,i)=(4,3)` instance is closed, not the general case, and does not claim otherwise anywhere
in the write-up. **No overclaim found.**

### Assessment

Real, verified progress: a legitimately-fixed gap, 3 new certified general lemmas, one more
concrete instance closed. Step 4 (general-`m` multi-cut lower bound) remains open, correctly
reported as such. Status `partial` is accurate. **Verdict: CHANGES REQUESTED** — continue
attacking Step 4 (the file itself notes Fact 5 redirects future attempts toward a genuine
joint budget-tradeoff argument, since the "bound the residual in isolation" family is now
provably dead).

---

## 2. `potential-weighting-upper-bound` — verdict: **CHANGES REQUESTED** (Status: `partial`,
correctly self-reported)

### 2a. The negative result is genuine, not an artifact of the self-reported bug

The builder reports catching and fixing a real bug (an early lookahead-test version compared
the candidate bound against the *same-parameter* target, making "0 failures" vacuously true by
construction — `min(X,...) ≤ X` always). I independently re-implemented the corrected
full-width-branching lookahead test from scratch (my own code, not theirs) and ran it on fresh
random trials:

```
m=3 levels=1: 62/300 fail (20.7%)      m=4 levels=1: 135/300 fail (45.0%)
m=3 levels=2:  8/300 fail (2.7%)       m=4 levels=3:   0/300 fail (0.0%)
                                        m=4 levels=2:  33/300 fail (11.0%)
```

This independently reproduces the qualitative finding claimed in the file (fixed lookahead
depth `ℓ=2` still fails at a non-negligible, non-shrinking rate as `m` grows — my `11.0%` at
`m=4,ℓ=2` closely matches their reported `12%`; different sampling methodology, same
conclusion). This corroborates the negative result is genuine, **not** a residual artifact of
a second undiagnosed bug.

### 2b. Exact-fraction claims re-verified precisely

- The `m=3` Rule-1 counterexample `A=(239,112,75,74)/500`: I traced Rule 1 by hand-coded exact
  arithmetic and got `e=37/500`, matching the claim exactly; `37/500 > 1/15` confirmed by
  cross-multiplication.
- The true optimum via exhaustive D/M search: I independently implemented a full exhaustive
  search and found `g(A,3)=1/500` exactly, with **exactly the 4 claimed tied optimal first
  moves** — `D(a_1)`, `D(a_2)`, `M(a_1,a_2)`, `M(a_3,a_4)` — matching the file's diagnostic
  claim precisely (my search found these as the unique 4-way tie at the top of the ranked
  first-move list, all others strictly worse).
- The corrected Form-E' arithmetic: scalar fallback `e_2·S(residual) = (1/7)(69/125) = 69/875`
  and the "deeper refinement" `1/500 + (1/3)(127/500) = 13/150` — both re-derived by hand and
  confirmed to match exactly; both exceed the target `1/15`, confirming the claimed failure.
- The sharpened exact `m=2` Rule-2 counterexample `A_2=(1/2,333/1000,167/1000)`: re-derived the
  6-candidate table by hand using the elementary 2-element closed form
  `g({p,q},1)=min(p-q,q)`, confirmed `g(A_2,2)=0` (via `M(a_1,a_2)`) and Rule 2's chosen value
  `83/500 > 1/7` (cross-multiplication `83·7=581>500`) — matches exactly.

All exact claims check out precisely; no arithmetic errors found anywhere in this file.

### Assessment

This is honest, well-corroborated negative-result reporting. Per the per-role rule from prior
rounds (a negative result about a *technique* is not itself theorem progress), the file's
Status was already `partial` from round 3's certified Lemma D/M (a genuine reduction) — this
round's negative result does not need to (and does not) elevate that, and correctly is not
presented as new theorem-level progress. **Verdict: CHANGES REQUESTED** — the central open
gap (a provably-correct Case (ii) policy for general `m`) remains; the file correctly narrows
the search space (ruling out bounded-lookahead scalar-fallback mechanisms entirely) for the
next attempt, which needs a genuinely non-scalar per-state invariant.

---

## 3. `concavity-minimax-duality` — verdict: **CHANGES REQUESTED** (Status: `partial`,
correctly self-reported, upgrade from `unsolved` to `partial` is justified)

### 3a. §8's D/M-completeness argument — checked very carefully, found CORRECT (with a minor
presentational imprecision that does not affect substance)

This is the round's most consequential new claim, so I devoted the most scrutiny here. I
worked through a potential gap in detail: does Step 8.3's peeling induction implicitly need a
bisect-type or tie-to-untouched-original cut to *also* have in-degree 0 (nothing else ties to
its output), contradicting the blanket claim that such cuts are "always safe to peel first"
purely because they have out-degree 0? I constructed a hypothetical scenario (another cut
tying to a bisection's own output value) to stress-test this.

**Resolution, via an independent from-scratch topological-sort/DAG argument:** the correct
general criterion for safely peeling *any* cut (of any type) is in-degree 0 (nothing else
depends on its output) — not out-degree 0. But the substantive conclusion is still correct: a
valid temporal ordering of all `K` genuine cuts (equivalently, a legal D/M sequence realizing
`FINAL`) exists iff the full dependency graph is a DAG. Since every node has out-degree ≤ 1
(a cut ties to at most one target), a standard counting argument (total in-degree = total
out-degree = number of out-degree-1 nodes ≤ total nodes, with equality forcing every node to
have out-degree exactly 1, hence in-degree exactly 1 too) shows: the graph fails to have an
in-degree-0 node **only if every single node has out-degree exactly 1 — i.e. every genuine cut
is a cross-tie (ties to another cut's output), none is a bisection or tie-to-untouched-original
— and the graph is a disjoint union of directed cycles.** This is exactly what the file claims,
and my independent derivation (via topological sort, not by re-reading their proof) reaches the
identical characterization by a different route. The file's literal graph definition ("on the
set of tie-type genuine cuts" as nodes) is a minor imprecision — bisect/tie-to-original cuts
should also be nodes (with out-degree 0) for the counting argument to be airtight as stated —
but this does not change the correct conclusion, which I independently re-derived. **§8's core
claim, `g(A,m)=h(A,m)` modulo the all-cycles case, is correct.**

I also verified Step 8.1 (existence of a global minimizer via compactness/finitely-many-shapes)
and Step 8.2 (the Vertex Lemma import) are both legitimate: Step 8.2's import is checked
directly against `elementary-exchange-smoothing`'s own Step A/Corollary (read in full) — that
lemma's proof is genuinely general (never uses `n=2`-specific structure, only "one background
piece replaced by two, everything else fixed"), so the import is valid, not a crux-move
citation shortcut.

The "honest status of the gap" (§8.4) is correctly and precisely characterized: it is *not*
the vague "re-split a half" scenario the outline-reviewer originally worried about (that case
is fully covered by the peeling induction), and the corroborating evidence (no violation found
by `dyadic-cascade-induction`'s independent exhaustive/broad numeric search) is correctly
hedged as "consistent with, not a proof of" completeness for `D_m` specifically.

### 3b. Consistency with `dyadic-cascade-induction`'s independent Step-0 fix

These two fixes address the *same* flagged issue (D/M-completeness) via genuinely different,
**non-contradictory** routes: `dyadic-cascade-induction` sidesteps the need for D/M
completeness entirely (its Branch A/B1/B2 proofs use only physical reasoning, no D/M
language, so the completeness question is moot for its own proof). `concavity-minimax-duality`
instead directly proves a conditional completeness result, useful to any *future* approach
that wants to reason in D/M language for a lower bound (e.g. a revived §5.2' plan, or
`potential-weighting-upper-bound` if extended to prove a lower bound). I confirmed there is no
tension: neither result depends on or contradicts the other.

### 3c. Candidate potential Φ(M,r)=S(M)/(2^{r+1}-1) — both counterexamples verified exactly

I built an independent exact-`Fraction` BFS over the D/M operation space from `D_2` and `D_3`
and confirmed:
- `D_2`: state `(3,2)` at budget `r=1` is genuinely reachable from `D_2=(4,2,1)` (via `M(4,1)`,
  not via the confusing/garbled parenthetical "D-then-M" path description in the file, which
  appears to be a leftover drafting artifact — but the final cited state and values are
  correct). `Φ(3,2;r=1)=5/3`, and applying `M(3,2)→(1)` gives `Φ(1;r=0)=1`. `5/3>1` confirmed
  — a genuine monovariance failure.
- `D_3`: state `(6,4,1)` at budget `r=2` is reachable (via `M(8,2)` from `D_3=(8,4,2,1)`).
  `Φ(6,4,1;r=2)=11/7`, applying `M(6,4)→(2,1)` gives `Φ(2,1;r=1)=1`. `11/7>1` confirmed.

Both counterexamples are exact and correctly diagnosed (a "big" match drops `S(M)` faster than
the budget-based denominator compensates). My own independent BFS additionally found 2 (at
`D_2`) and 17 (at `D_3`) total monovariance violations, so Candidate 2 is robustly, not
marginally, refuted — consistent with the file's "not salvageable in its current form" verdict.
The follow-up diagnosis (a `max(M)`-aware correction term is the natural next idea, untested
this round) is appropriately flagged as a concrete next step, not oversold as a fix.

### Assessment

A genuinely new, real, independently-reproducible reduction (§8) plus a well-verified negative
result (§9). Status correctly upgraded `unsolved → partial` (§8 is a real theorem-relevant
reduction, not merely a report that a mechanism is dead — matches CLAUDE.md's `partial`
definition and this round's own per-role dead-mechanism-vs-progress distinction). **Verdict:
CHANGES REQUESTED** — the all-cycles case remains open (though narrow and unobserved), and no
working potential Φ has been found yet.

---

## 4. `elementary-exchange-smoothing` — formally retired this round

Per the round-4 outline-reviewer's recommendation, and my own independent comparison of the two
underlying proofs (`dyadic-cascade-induction` §3 vs. `elementary-exchange-smoothing` Step A +
Corollary — read both in full), these are genuinely the same fact, proved twice independently
by two different builders in two different rounds (real cross-validation, not redundant
low-value work). I merged them into a single canonical `lemmas/vertex-lemma.md` and formally
retired `elementary-exchange-smoothing` as an independent whole-attempt slug (its own file now
carries a reviewer note to this effect). I updated all 3 citations inside
`concavity-minimax-duality.md` (§8 intro, Step 8.2, and the Promotable-lemmas entry) to point
to `lemmas/vertex-lemma.md` instead of the retired slug, so the import remains valid/citable
going forward — this directly answers the dispatch's question ("it should point to the lemma
file, not the slug, once merged").

---

## Lemma certification actions taken this round

1. **`lemmas/insertion-and-cascade-facts.md`** (NEW) — Facts 3, 4, 5 from
   `dyadic-cascade-induction`, all independently re-verified (see §1b above). Certified.
2. **`lemmas/vertex-lemma.md`** (NEW) — merges `dyadic-cascade-induction` §3 and
   `elementary-exchange-smoothing` Step A/Corollary. Certified; supersedes both slugs' own
   copies as the canonical citable source.
3. **`lemmas/dm-completeness-partial.md`** (NEW) — `g(A,m)=h(A,m)` modulo the all-cycles case,
   from `concavity-minimax-duality` §8, independently re-derived via topological sort (see §3a
   above). Certified, honestly scoped as *conditional*, not full completeness.

All three pass the "no `sorry`, statement correct and no stronger than proved" bar: each
lemma file states its provided-condition/open-case scope explicitly and does not overclaim.

## `current.md` updated

Status remains `partial`. Rewrote `## Approaches tried` and `## Current best` to reflect this
round's real state: the Step-0 fix, 3 new dyadic-cascade-induction lemmas, the
potential-weighting-upper-bound negative result (well-corroborated, central gap unchanged),
concavity-minimax-duality's new §8 result and §9 negative result, and the formal retirement of
`elementary-exchange-smoothing`. `## Full proof` remains absent (Status is `partial`).

## Summary of verdicts

| Approach | Status | Verdict |
|---|---|---|
| `dyadic-cascade-induction` | `partial` | CHANGES REQUESTED |
| `potential-weighting-upper-bound` | `partial` | CHANGES REQUESTED |
| `concavity-minimax-duality` | `partial` (upgraded from `unsolved`) | CHANGES REQUESTED |

No approach reached `solved` this round — the theorem (`c(n)=2^n/(2^{n+1}-1)` for all `n`,
both directions) remains open. All three built approaches made real, independently-verified
progress with no overclaims found; this is a genuinely productive round (3 new certified
lemmas, one gap soundly fixed without reintroducing a new one, two well-corroborated negative
results narrowing future search, one slug formally retired with its content preserved).

## `record_outcome` calls made

- `dyadic-cascade-induction`: `advanced` — "Fixed the D/M-completeness overclaim soundly...
  Step 4 still open, honestly scoped."
- `potential-weighting-upper-bound`: `partial` — "Genuine, independently-corroborated negative
  result... central gap unresolved."
- `concavity-minimax-duality`: `advanced` — "New real result: proved g(A,m)=h(A,m) modulo the
  all-cycles case... Status correctly upgraded unsolved->partial."
