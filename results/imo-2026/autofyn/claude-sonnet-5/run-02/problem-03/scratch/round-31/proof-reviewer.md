# Proof-reviewer report, round 31, imo-2026-03

Reviewed 3 independently-built approaches. Each verdict is per-approach,
per CLAUDE.md's routing rules. All independent verification scripts were
written from scratch (not copied from builders' scripts) — see below.

## 1. rank-pigeonhole-budget — VERDICT: CHANGES REQUESTED (approach Status:
partial overall / verified-milestone on the sub-target)

**Claim reviewed.** §7.18.4–7.18.5: the last 2 of 6 residual shapes of
$(\star_3)=\mathrm{MinFloor}(4)$, shapes $(1,2,0,0)$ and $(2,1,0,0)$, are
fully closed ($A(U)\ge1$) via exhaustive exact-rational vertex enumeration
(36 and 27 vertices respectively, licensed by the already-certified
`vertex-minimum-theorem`), completing $(\star_3)=\mathrm{MinFloor}(4)$'s
full closure across all 20 maximal shapes.

**Independent verification performed.**
- Re-derived, from scratch, the complete hyperplane families for both
  shapes directly from their defining constraints (not transcribed from
  the file) — 18 hyperplanes for $(2,1,0,0)$ (free coords $f_2,f_3,c$),
  21 for $(1,2,0,0)$ (free coords $a,h,i$).
- Solved every triple ($\binom{18}3=816$, $\binom{21}3=1330$) in exact
  `Fraction`/`sympy` arithmetic, filtered for feasibility. Got **exactly**
  36 and 27 feasible vertices, matching the file's counts exactly, with
  minimum $A(U)=1$ in both cases, matching every tight row in the file's
  tables (verified numerically, not just by count).
- Ran a 2,000,000-trial continuum (non-vertex-restricted) random search
  over each shape's full feasible region (uniform sampling of the free
  parameters within the defining inequalities). No point beats $A(U)=1$
  in either shape (observed minima $\approx1.0000006$ and
  $\approx1.0000151$). This independently corroborates that restricting
  to the theorem-guaranteed finite vertex family is itself valid here —
  not just that the claimed vertex list is internally self-consistent.

**No gap found.** The hyperplane-completeness argument (every possible
type-(I)/(II) tie or zero event for these two shapes' fixed-sum
constraints) checks out under independent re-derivation, and the
vertex-minimum-theorem being invoked was itself certified in round 3 with
no scope restriction that would exclude this use (general $n$, general
composition).

**Status-header honesty check.** The file's own Status header says
`solved` but explicitly scopes this to "this approach's own target,
Claim (A)" — which was established in earlier rounds, not this round.
This round's $(\star_3)=\mathrm{MinFloor}(4)$ closure is presented, both
in the "Approaches tried" entry and in §7.18.5, as a side-closure that
"does not touch Claim A's own status" and explicitly notes the
general-$n$ obstruction remains open. No overclaim found — the scoping
is honest and consistent throughout the file.

**Verdict rationale.** The specific sub-target built this round
(closing the last 2 shapes) is complete, correct, and rigorous — this
merits `verified-milestone` in the ranker. But the approach's own overall
target (Claim A, general $n$) was already solved in a prior round, and
the file is honest that the general-$n$ $(\star_k)$, $k\ge3$ obstruction
remains open project-wide, so CHANGES REQUESTED remains the correct
routing label for continued work on adjacent open items (there is no
"this exact target is now fully closed and the file should stop" signal
— the file itself recommends moving to the general-$n$ pattern next).

**Lemma certified:** `minfloor-4-full-closure.md` — certified in full
(see updated Certification note in the lemma file itself, upgraded from
the builder's own uncertified self-check note).

## 2. greedy-halving-adversary — VERDICT: CHANGES REQUESTED (Status:
partial, correctly scoped)

**Claim reviewed.** New §"Round 31" section: closes $h(m)$'s "simultaneous
$q_1$-cut and tail-refinement" piece's vertices $c=q_1-x,c=q_1$
unconditionally at $m=3$ (conditional on $IH(m-1)$ for $m\ge4$) via a new
strong-induction-on-$h(m-1)$ mechanism; cites `rank-pigeonhole-budget`'s
$\mathrm{MaxCeil}(m)$ (closed for $m\le4$) as term-for-term identical to
the $c=x$ vertex's own needed inequality; partially advances the new
$c=t\in S''$ vertex (fully closes the "$t=q_2$, untouched" sub-case,
leaves "split-rung fragment removed" and "$q_2$ untouched, $t\ne q_2$"
open).

**Independent verification performed.**
- Wrote a fresh exact-`Fraction` script generating random legal
  $S''\subset$ tail (composed via random cut-budget distributions and
  split points, $\le m-2=1$ cuts at $m=3$) and random $x\in(0,q_1/2]$,
  checking $A(\{c\}\cup S)\ge f(3)$ for $c\in\{q_1-x,q_1\}$. **First draft
  had a self-inflicted scaling bug** (used the normalized target
  $f(3)=1/15$ against the unnormalized ladder $q_1=8,\dots,q_4=1$, sum
  $15$; the correct unnormalized target is $q_{m+1}=1$, by the Lemma-9
  scaling identity $A(\lambda S)=\lambda A(S)$ applied with $\lambda=15$)
  — corrected and re-ran: 400 randomized trials plus a deterministic
  extreme/boundary stress test (near-degenerate $x$ near $0,q_1/2$;
  near-degenerate rung splits), zero violations against the corrected
  target.
- Cross-checked the "$c=x\equiv\mathrm{MaxCeil}(m)$" citation by tracing
  both definitions independently from their own files: `MaxCeil(\ell)`
  (length-$\ell$ ratio-2 tail, top $\sigma_1$, bottom $\sigma_\ell$, every
  legal $\le(\ell-2)$-cut refinement, target $A(S)\le\sigma_1-\sigma_\ell$)
  matches $c=x$'s own needed inequality $A(S'')\le q_2-f(m)$ exactly under
  $\ell=m$, $\sigma_1=q_2$, $\sigma_\ell=f(m)$ — genuinely identical
  statements, confirmed also by the outline-reviewer's own independent
  trace (`/tmp/round-31/outline-reviewer.md`, "Focus check").
- Confirmed the honest scoping of the still-open sub-cases: "split-rung
  fragment removed" is correctly described as an incomplete reduction
  (only handles $x_1=q_2/2$, not the general case), and "$q_2$ untouched,
  $t\ne q_2$" is correctly left fully open with no false claim of
  progress.

**No gap found** in the closed portions; the induction step's honest
scope note ("$IH(m-1)$ ... currently established unconditionally only for
$m-1\in\{1,2\}$ ... conditional schema for $m\ge4$") is accurate and
matches the file's own citation trail (h(2) closed round 25; h(3) itself
not fully closed since $c=t\in S''$ remains open even at $m=3$).

**Verdict rationale.** Real, verified progress narrowing $h(m)$'s open
territory, but $h(m)$ for any $m\ge3$ remains unclosed (by the file's own
honest admission) — CHANGES REQUESTED, continue on $c=t\in S''$'s
remaining sub-cases and the shared $\mathrm{MaxCeil}(m\ge5)$ item.

**Lemma not separately certified this round:** the builder flagged "1 new
lemma" (the $h(m-1)$-as-IH induction step) but did not extract it as a
standalone lemma file; it remains embedded in the approach file's own
narrative. Recommend extracting and certifying on a future round once
stated as an independent, reusable statement.

## 3. lp-duality-certificate — VERDICT: CHANGES REQUESTED (Status: partial,
correctly scoped)

**Claim reviewed.** §R31.1–R31.5: new general Half-Complement Pin Theorem
(for any $m$ pieces, pinning $q_1$ against all-but-one of the rest with
one piece left untouched gives $\Phi=\max(q_1,T-q_1)$ whenever feasible,
value independent of which piece is left untouched); §R31.2 corollary at
$m=5$ ($n=4$): closes $p_1\in[15T/31,T/2)$ unconditionally for arbitrary
$p_2,p_3,p_4,p_5$ satisfying the residual $\mathcal R$'s bounds
($p_2>T/31$).

**Independent verification performed.**
- Re-derived the theorem's algebra by hand from the raw substitution
  $\rho=2q_1+q_j-T$, matching the file's derivation term for term.
- Went further than re-deriving the file's own reduced-to-2-elements
  shortcut: built the **actual full 8-element fragment multiset** the
  $m=5$ strategy produces ($\{p_3,p_4,p_5,\rho\}\cup\{p_2,p_3,p_4,p_5\}$)
  and computed its alternating sum directly by full sorting — confirming
  from scratch that the true, un-reduced multiset's $A$ matches the
  claimed reduced formula (i.e. that the pair-cancellation step the
  theorem relies on via `partition-chamber-theorem` is not silently
  hiding an error) — across 11,625 exact-`Fraction` trials targeted
  specifically inside the claimed region ($p_1\in[15T/31,T/2)$,
  $T/31<p_2<8T/31$, sorted, summing to $T$). Zero mismatches: feasibility
  held throughout, the full and reduced $A$ values matched, and
  $\Phi\le a_4T$ held throughout.
- Checked the "no overlap/miscount" claim explicitly: the two
  previously-known hard witnesses ($p_1/T\approx0.379$ and $\approx
  0.467$) both lie strictly below $15/31\approx0.4839$ (direct
  arithmetic), confirming this strip is disjoint from prior closures —
  genuinely new territory, not inflated coverage.

**No gap found.** The theorem is a correct, general consequence of the
already-certified `partition-chamber-theorem`; the corollary's algebra
(feasibility from $p_1\ge15T/31$ and $p_2>T/31$, hence $\Phi=T-p_1\le
a_4T$) is exact and matches independent re-derivation.

**Status-header honesty check.** The file's Status header and the
"What is NOT established" / "Honest conclusion" sections explicitly and
correctly state that $\mathcal R':=\{p_2\le p_1<15T/31,\ T/31<p_2<8T/31\}$
remains open, that no Farkas-style covering argument exists yet, and that
$n=4$'s general upper bound is not solved this round. Matches reality —
no overclaim.

**Verdict rationale.** Genuine new region-closure (not a point), fully
verified independently — CHANGES REQUESTED to continue covering
$\mathcal R'$.

**Lemmas certified:** `half-complement-pin-theorem.md` and
`n4-strip-closure-corollary.md` — both created and certified in full
(new lemma files written; the round's build had proposed but not
separately filed them).

## Summary

All three approaches: **CHANGES REQUESTED** (no APPROVE, no RETHINK).
No overclaims found in any of the three files. `current.md`'s `## Status`
remains `partial` for the whole `imo-2026-03` problem (unchanged); its
`## Approaches tried` section has been extended with a new "Round 31"
entry recording all three fronts' verified findings, per the established
convention of prior rounds. 3 lemmas certified this round:
`minfloor-4-full-closure` (upgraded builder self-check to full
certification), `half-complement-pin-theorem` (new file), and
`n4-strip-closure-corollary` (new file).
