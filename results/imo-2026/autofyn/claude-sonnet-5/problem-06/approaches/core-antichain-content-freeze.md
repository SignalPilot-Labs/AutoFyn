## Status
unsolved

## Round 13 Outline (proof-outliner directive — NEW approach, opened this
round: attack `𝓥_S`-finiteness / global Hypothesis (MRS) DIRECTLY, via a
genuinely new mechanism, NOT the dead bundle-size route — flagged for
mandatory outline-reviewer verification of Step 0 before any builder
effort proceeds beyond it)

**Why this approach exists, and why it is genuinely diverse from the 4
live approaches.** The 4 live approaches (`sunflower-inadmissibility-
toolkit`, `forced-primes-well-ordering`, `sunflower-bundle-closure`,
`intersecting-family-covering-construction`) all attack FCBC via Theorem
SW, reduced to the Stabilization Conjecture, reduced further to one of
three sub-questions — Conjecture (JW)/Backbone Permanence, `(PD_{S,S'})`,
or local `(MRS_S)` — all of which (per the certified Subset Lemma,
`lemmas/lemma-local-equivalence-and-no-shortcut.md`) target the LOCAL,
`I_S`-restricted antichain `𝓥_S^{\mathrm{loc}}`, proven **strictly
harder** than the plain (non-local) `𝓥_S` (`𝓥_S\subseteq𝓥_S^{\mathrm{loc}}`
always). This approach targets `𝓥_S` itself (equivalently, via the
already-certified Theorem CD + Theorem V, global Hypothesis (MRS)) — a
provably WEAKER, hence meaningfully different, target: if closed, it is
**unconditionally sufficient for the ENTIRE problem** via the already-
certified chain `𝓥_S` finite for every proper core `⟹` (Theorem CD +
Lemma TC) `𝓥` finite `⟹` (Theorem V) (MRS) `⟹` (Lemma MS) FCBC `⟹`
(Theorem 5.1) `a_{n+T}=a_n+L` for every `n\ge1` — bypassing Conjecture
(JW), Backbone Permanence, `(PD_{S,S'})`, and `(MRS_S)` entirely, for
EVERY instance at once (not just Case A or Case B pairs).

**MANDATORY Step 0 — logical audit (read before anything else; do not let
a builder proceed past Step 1 until the outline-reviewer has independently
confirmed this).** This workspace has a standing Round-9 Rule: *"NEVER
re-attempt to prove (MRS)/`𝓥_S`-finiteness/(UB_S) ... — DEFINITIVELY
REFUTED in Case II ... This retires the ENTIRE target family pursued
rounds 4-8 under 3 successive names ((MRS)→`𝓥_S`-finiteness→(UB_S))."* I
(the outliner) independently re-read the actual certified proof, not just
the Rule's summary text, and believe this Rule's phrasing over-states what
was proven — but I am not fully confident, so this is flagged, not
asserted, exactly per this round's dispatch caution. The precise chain:

1. `lemmas/theorem-UBS-sufficiency.md` proves **only** `(UB_S)⟹𝓥_S`
   finite (a ONE-DIRECTIONAL sufficiency, stated explicitly as `⟹` in its
   own Statement section, never claimed as `⟺`).
2. `lemmas/theorem-UBS-false-case-II.md`'s Main Theorem (§5) proves `(UB_S)`
   itself is impossible (for every proper core simultaneously, in Case
   II), by contradiction: *assuming* `(UB_S)`-for-every-`S` derives BOTH
   (a) a uniform bound `B:=\sup_{n\notin I_{P_1}}\omega(a_n)<\infty`
   **directly from `(UB_S)`'s own definition** (not derived independently
   from `𝓥_S` finiteness), and (b) exact periodicity (via the full
   certified chain, which passes through `𝓥_S` finite as an intermediate
   step) — then shows `(a)` and `(b)` are jointly inconsistent (Landau
   Count Lemma + density argument). **The contradiction is reached using
   the extra hypothesis `B<\infty`, which is literal content of `(UB_S)`
   itself and does NOT follow merely from `𝓥_S` (or `𝓥`, or (MRS)) being
   finite** — `𝓥_S`-finiteness (equivalently FCBC-sufficiency) only needs
   a finite prime set to intersect every pair; it places NO bound on
   individual `\omega(a_n)`, since a term's full radical can still be
   arbitrarily large as long as some fixed covering-set prime is present
   (Lemma W1, round 3, already certified — FCBC is strictly weaker than a
   companion-bundle-size bound). **Conclusion of this audit: the theorem's
   own proof only refutes `(UB_S)` itself; it neither states nor uses
   anything that would refute `𝓥_S`-finiteness (equivalently (MRS)) taken
   as a free-standing target attacked by a mechanism OTHER than `(UB_S)`.**
   The Round-9 Rule's "equivalently" and "3 successive names for the same
   family" phrasing appears to conflate a proof ROUTE (bundle-size
   boundedness, i.e. `(UB_S)`) with the TARGET itself (`𝓥_S`-finiteness) —
   exactly the necessary-vs-sufficient conflation this workspace's own
   Rules (round 9: *"NEVER assume a hypothesis being false threatens the
   approach built on top of it without first checking whether that
   hypothesis was proven necessary or merely sufficient"*) warn against.
3. Separately: round 7's `global-recruiter-finiteness` dead-end
   (`results/imo-2026-06/approaches/global-recruiter-finiteness.md`) does
   **not** block this either — that approach's refuted premise was a
   single core-INDEPENDENT global set `W(a_1)`, proven (its own §3)
   logically EQUIVALENT to — not easier than — "`\Lambda_S` finite for
   every proper core `S`" (the exact per-core statement). This approach
   attacks the per-core statement `𝓥_S`-finiteness DIRECTLY (the same
   target rounds 6–8 attacked, using the already-certified Theorem CD
   per-core decomposition, not a "one global set independent of `S`"
   framing) — it is the productive per-core direction round 7 itself
   pointed to, not the dead reformulation.
4. **What this Step-0 audit does NOT establish**: that `𝓥_S`-finiteness is
   TRUE, or that a new mechanism to prove it exists — only that the
   target itself has not been logically refuted, and remains open, exactly
   as it was left at the end of round 8 (before the population moved on to
   the harder local `𝓥_S^{\mathrm{loc}}` reformulation in round 9+, not
   because `𝓥_S` was refuted, but because its one attempted proof
   mechanism, bundle-size boundedness, died and no replacement mechanism
   was tried).

**If the outline-reviewer confirms this audit, proceed; if it finds a
flaw, this approach should get RETHINK immediately (cheap kill, no build
effort wasted) and the Round-9 Rule should stand as originally written.**

**Motivating numerics (round 13's gn-periodicity explorer, not a proof):**
the GLOBAL minimal-radical antichain `𝓜_n` (comparisons against ALL of
`[1,n]`, no per-core/per-class restriction — the object Hypothesis (MRS)
is literally about) freezes **content-identically** (exact set equality,
re-checked, not just cardinality) for **all 6 tested `a_1`** — 5 cases
freeze by `n\le163`, and even the hardest known case (`a_1=21528751`)
freezes by `n=44{,}967` and stays bit-for-bit frozen through
`n=25{,}000{,}000` (555× past its own freeze point), recovering the exact
already-certified `H` sets in every tractable case
(`4087\to\{2,61,67\}`, `4199\to\{2,3,13,17,19,83\}`). This is strong
evidence, not a proof — this workspace has repeatedly (rounds 2, 5/7, 9)
found "looks frozen/bounded numerically" claims later reversed at much
larger scale, so no numeric range here should be treated as more than
motivation.

**Target: the whole problem**, via `𝓥_S` finite for every proper core `S`
`⟹` `𝓥` finite (Theorem CD) `⟹` (MRS) (Theorem V) `⟹` FCBC (Lemma MS)
`⟹` exact periodicity from `n=1` (Theorem 5.1) — every arrow already
certified; the entire content of this approach is proving `𝓥_S` finite for
an arbitrary proper core `S`.

**Technique:** extend the already-certified single-family toolkit — Lemma
FOM (First-Occurrence Minimality: a radical value's first-ever occurrence
always equals the explicit minimum `T_C`), the No-Resurrection Lemma
(`lemmas/theorem-V-veto-finite-iff-MRS.md`), and the Realized–Blocked
Dichotomy (Lemma ERD-C) — to the GLOBAL antichain directly, exploiting a
structural asymmetry the local `𝓥_S^{\mathrm{loc}}` object provably lacks:
the global antichain's domination candidates are drawn from **all** of
`[1,n]`, not just same-class members, giving vastly MORE potential
dominators per step (this is exactly why `𝓥_S\subseteq𝓥_S^{\mathrm{loc}}`,
Subset Lemma) — a genuinely different combinatorial regime from the
local, class-starved one every live approach currently wrestles with.

**Skeleton:**
1. Restate `𝓥_S`-finiteness precisely (already-certified definition,
   Theorem CD) and confirm, via a fresh small worked example (e.g.
   `a_1=247` or `a_1=2747`), that it matches the numerics above — a cheap
   sanity check before further work (per this workspace's standing rule
   to numerically test any reused/repositioned definition).
2. Formalize the "domination abundance" asymmetry precisely: state and
   prove a lemma bounding, for a candidate value `C` with core `S`, how
   quickly an out-of-class dominator becomes available, using the Growth
   Lemma (`a_n=O(n)`) and the fact that ANY index `m` (not just `m\in I_S`)
   with `\mathrm{rad}(a_m)\subsetneq C` or `\mathrm{rad}(a_m)\cap
   \mathrm{comp\ of\ }C\ne\varnothing` in the appropriate sense can
   dominate — this is the genuinely open, load-bearing content; a
   from-scratch counting/well-ordering argument, NOT bundle-SIZE bounding
   (the dead route) — attempt to bound the NUMBER of ever-realized
   distinct global-antichain values via generation-index counting (Lemma
   FOM gives each value `C` a distinct, strictly increasing "birth index"
   `T_C`; try to show only finitely many births can ever go permanently
   un-dominated, using the abundance of candidate dominators, rather than
   bounding any single value's size).
3. If Step 2 succeeds for a fixed proper core `S`, generalize over the
   (fixed, finite, `\le2^k-2`) family of proper cores of a given `a_1` —
   a routine finite conjunction, already licensed by Theorem CD, not new
   content.
4. Close with the already-certified chain (Theorem CD/Lemma TC → Theorem
   V → Lemma MS → Theorem 5.1) to conclude the whole problem.

**Key lemmas needed (state as open, with the mechanism direction, not a
completed proof):**
- **Domination Abundance Lemma (open, the crux)** — for a candidate global
  antichain value `C` (core `S\subsetneq P_1`) realized at some index, the
  number of indices `m\le N` (drawn from the WHOLE prefix `[1,N]`, not
  restricted to `I_S`) that could serve as a dominating witness grows
  with `N` in a way that, combined with the Growth Lemma's `O(N)` bound on
  `a_N`, forces domination within a bounded number of steps — because the
  global antichain draws candidate dominators from every index, not just
  same-class ones (the source of the Subset Lemma's strict containment,
  hence of the genuine extra leverage this approach has over the local
  `𝓥_S^{\mathrm{loc}}` route every live approach is currently stuck on).
- **Finite-Birth-Survivor Bound (open)** — using Lemma FOM's strictly
  increasing birth-index embedding `C\mapsto T_C`, only finitely many
  births can permanently survive (never be dominated) — this is the
  genuine content that would need the Domination Abundance Lemma as an
  ingredient, not a restatement of it.

**Open gaps:** both key lemmas above are fully open; this is a from-
scratch attempt, honestly scoped as high-risk/high-value (if it works, it
solves the WHOLE problem for every instance, bypassing all 4 live
approaches' target entirely). Step 0's logical audit is itself an open
item requiring outline-reviewer sign-off before further investment.

**Cases to cover:** none beyond the standard Case I/Case II split already
handled unconditionally by existing certified lemmas (Case I: `k=|P_1|=1`,
already fully closed by Theorem CI) — this approach only needs to close
Case II's proper cores, same scope as rounds 6–8.

**Watch out for:** (a) do not let this collapse back into the dead
bundle-SIZE-boundedness mechanism — the whole point of targeting `𝓥_S`
(not `𝓥_S^{\mathrm{loc}}`) directly is that it does NOT require a
companion-bundle-size bound, only a finite VALUE-SET bound, a structurally
different (and per Lemma W1, strictly weaker) requirement; (b) numeric
"looks frozen" evidence must not be mistaken for a proof (see this
workspace's rounds 2, 5/7, 9 precedent, and round 13's own explicit
caution about this exact object); (c) if Step 0's audit is found flawed by
the outline-reviewer, do not silently continue — record the correction
and revert to treating `𝓥_S`/(MRS) as dead, per the original Round-9 Rule.

## Approaches tried
(none yet — new approach)

## Current best
Nothing proved yet. Motivating numerics (content-level antichain freeze,
6/6 tested `a_1`, up to 555× past freeze point with zero exceptions) and a
precise logical audit distinguishing this target from the definitively-
dead `(UB_S)` route are recorded above; both need independent verification
before being treated as established.

## Full proof
(Not present — Status is `unsolved`.)
