## imo-2026-03 — round 2 outline review

### greedy-halving-adversary (revise) — APPROVE (with directed fixes)
Verified independently:
- **Self-similarity check (Key lemma 2)**: computed $p_i/r$ for $i=2,\dots,n+1$ symbolically — matches the
  $(n-1)$-ladder formula exactly for all $n$ tested. Correct, safe to build on as stated.
- **"At most one fragment of $p_1$ exceeds $r$" (Key lemma 1)**: checked $p_1 \le 2r$ for $n=1,\dots,5$ — holds
  with **equality at $n=1$** (not strict, as the outline's parenthetical implies), and strict for $n\ge2$. The
  outline's mechanism ("$f_1+f_2>2r\ge p_1$, contradiction") still goes through even at equality (two strictly-$>r$
  fragments still sum strictly $>2r=p_1$), so the lemma is fine — but flag for the builder that the outline's
  claim "$p_1<2/3$ true" is imprecise at $n=1$ (it's equality, not strict); don't let that slip into a false
  "strict" citation later.
- The repair genuinely targets the identified crux gap (the general lower/upper bound) via a mechanism
  (integral-splitting + induction with a threshold argument), not a bare "then it follows." Cases $c=0,\dots,n$
  are enumerated for the budget split. This is a real repair of the round-1 gap, not a resurrection of the
  refuted "bisect the max" rule — the outline explicitly separates this from that dead end (per the Rules memo).
- Remaining open gaps (explicit bound on $A_1$ as function of $c$; monotonicity-in-budget lemma; uniqueness/
  strictness in step 4) are honestly flagged, not hidden. Proceed to build.

### smoothing-compactness-certificate (revise) — APPROVE
- Scope this round is appropriately bounded and concrete: close the 3 remaining $n=2$ lower-bound compositions
  symbolically, using the exact method that already worked on 7/10 cases (same mechanism, not a new unproven
  one). Low risk, high value — de-risks any future induction base case.
- Correctly refuses to let the builder fall back on "numerically confirmed" (explicit rigor-rule callout).
  General-$n$ generalization is marked stretch-goal, appropriately deprioritized behind closing $n=2$ fully.

### self-similar-potential-certificate (new) — CHANGES REQUESTED, register but flag a probable arithmetic failure
This is a genuinely different framing (single self-similar certificate vs. named-adversary-strategy vs.
finite-template-enumeration) — good diversity pick, matches CLAUDE.md's push for framing diversity.
However, I ran the outline's own "telescoping check" (Key lemma 1) numerically/symbolically before approving:
```
p1 - r * Psi_{n-1}(ladder)   where Psi_{n-1}(ladder) is naively taken as 1/(2^n - 1)
```
gives $(2^n-1)/(2^{n+1}-1)$, **not** the target $1/(2^{n+1}-1)$, for every $n\ge2$ (only coincidentally equal at
$n=1$, since $2^n-1=1$ there). This confirms the outline's own stated worry ("must confirm it lands on
$1/(2^{n+1}-1)$, not merely something proportional to it") — the naive recursive definition $\Psi_n(S) := M -
\Psi_{n-1}(S')$ as literally written does **not** reproduce the target constant. The outline already built in
the correct safety valve for this ("if the arithmetic telescoping check fails, do NOT patch with a case-by-case
correction — report the failure honestly as a refutation of this specific certificate shape"), so this is not a
fatal flaw in the outline itself, but the builder must be told explicitly, up front, that the naive form is
already known to fail (skip re-deriving it, go straight to either fixing the recursion's normalization — e.g.
possibly $\Psi_n(S) := M - r\cdot\Psi_{n-1}(S'/r)$, a rescaled version, which the mechanism sketch in step 2/3
seems to actually intend but the "Key lemma" arithmetic didn't carry the rescaling through — or report the
refutation and stop). This saves the builder from re-discovering the same failure from scratch.

### integer-lattice-reduction (new) — CHANGES REQUESTED, register as a bounded feasibility probe
Genuinely different top-level reduction (discrete/integer recast before attacking, vs. working in $\mathbb R$
throughout) — good diversity. But the outline itself is candid that step 1 (rational-vertex reduction) is
significant overhead that may add no leverage, since the discrete core in step 3 is admittedly "the same
subset-sum/matching difficulty already identified by both live approaches." This is the weakest of the four:
not wrong, but its expected marginal value this round is lower than the other three, since two established
approaches are already directly attacking that same combinatorial core with more developed machinery. Approved
to register (not RETHINK — the reduction is technically sound, cites standard rational-polytope-vertex theory
correctly), but not selected for this round's build set; worth sampling again once the core combinatorial
difficulty is better understood from the other approaches' progress.

### Diversity assessment
Round 1 had 2 approaches sharing an "explicit strategy vs static extremizer" split, both hitting the same
general-$n$ combinatorial wall (subset-sum/matching-domination of superincreasing sequences). This round adds
two more genuinely distinct framings (self-similar certificate; discrete/integer reduction) — good, this is the
CLAUDE.md-recommended response to a shared wall, done proactively rather than after 3 rounds of stalling. All
four approaches, however, ultimately still reduce to variants of the same core fact (superincreasing sequences
uniquely resist splitting/matching under a one-cut-short budget) — that's expected, since it's very likely the
true mathematical crux of the problem, not an artifact of narrow framing. No approach should be cut for sharing
this target; they differ in mechanism for proving it, which is the relevant kind of diversity here.

### Population actions taken
- Registered `self-similar-potential-certificate` (new).
- Registered `integer-lattice-reduction` (new).
- `induction-first-move-reduction` remains unregistered (round-1 RETHINK, not renominated this round — correct,
  left alone).
- Ranked all four head-to-head via `update_ranking`, anchoring the two cold-start newcomers against the two
  established approaches using the evidence above (greedy-halving-adversary's verified algebra and
  smoothing-compactness-certificate's bounded closable task both outrank the newcomers' as-yet-unverified/
  higher-risk mechanisms; self-similar-potential-certificate outranks integer-lattice-reduction since it has a
  more concrete, if currently-broken, recursive mechanism vs. integer-lattice's admitted "may add no leverage"
  risk).

### Build set rationale
Both established approaches have concrete, bounded, well-verified near-term tasks and should continue. Of the
two new approaches, self-similar-potential-certificate is included in the build set as this round's diversity
pick — but the builder must be told up front (see above) that the naive telescoping formula is already known to
fail, so it should immediately move to fixing the normalization (rescaled recursion) or report a clean
refutation, not re-derive the same failing check. integer-lattice-reduction is registered but deferred — its
own outline flags it as likely redundant with the existing core difficulty; better to sample it next round once
we know whether the rescaled self-similar certificate or the repaired adversary strategy cracks the core lemma,
which would directly inform whether integer-lattice's reduction is worth the overhead.

build set: greedy-halving-adversary, smoothing-compactness-certificate, self-similar-potential-certificate
