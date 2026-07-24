# Proof-builder report, round 6 — `integer-lattice-reduction` (IMO-2026-03)

## What was done
Filled the round-6 outline into a complete write-up in
`results/imo-2026-03/approaches/integer-lattice-reduction.md`, executing
Steps 1–2 fully and Step 3 as far as it goes (which is: refuted, not
completed). **Status: unsolved.** No claim of progress toward $(\star\star)$
itself is made — this round's real contribution is two reusable lemmas plus
two honest, computation-backed refutations that redirect future rounds away
from dead ends.

## Results

1. **Step 1 (integer rescaling)** — routine, done: $D=2^{n+1}-1$ turns the
   ladder into $\{2^n,\dots,1\}$; homogeneity of $A$/$\Phi$ makes this a
   pure change of units.

2. **Step 2 (rationality sub-lemma) — proved a correct general version,
   REFUTED the outline's sharper conjectured version.**
   - **Lemma R1 (proved):** every vertex of the polyhedral cell
     decomposition (per `vertex-minimum-theorem`) has rational fragment
     coordinates — a clean Cramer's-rule argument, fully general (not
     ladder-specific, not restricted to minimizers).
   - **Refutation:** the outline's stronger claim ("denominator dividing
     $D$") is **false**. Fully worked counterexample: $n=2$, both of Xiang
     Yu's cuts spent on $p_1=4/7$, splitting it into three equal fragments
     $4/21$ each (a genuine vertex per `vertex-minimum-theorem`'s own
     definition — two independent type-(II) ties, matching the piece's
     2-dimensional simplex). $21\nmid7$. Root cause identified precisely: a
     $k$-way tie within one piece divides by $k$, and $k$ need not be a
     power of $2$ or a divisor of the Mersenne number $D$ (e.g. $k=3$,
     $D=7$, coprime).
   - **Lemma R2 (repaired, proved):** the correct denominator bound is
     $D\cdot L$, $L=\mathrm{lcm}$ of the vertex's tie-block sizes. This is
     offered as a reusable correction for `rank-tie-vertex-reduction` and
     `rank-pigeonhole-budget`, which may have been implicitly assuming the
     stronger, false form.

3. **Step 3 (digit/carry evaluation) — attempted, refuted on its own most
   favorable sub-case, exact computation, no positive result.**
   Restricted to "binary-tree" refinements (all ties powers of 2, the best
   case for the outline's hoped-for popcount transplant from
   `aimo-0917`/`aimo-0141`). The natural first attempt — bisecting a tail
   piece never changes the parity of $N_{G'}(x)$, hence never changes
   $(\star\star)$'s window integral relative to the unrefined tail — is
   **false**, verified by an exact-`Fraction` computation on a concrete
   $n=4$ instance: bisecting different single tail pieces of
   $\{8,4,2,1\}/31$ moves the window integral from $5/31$ to $3/31$,
   $7/31$, $5/31$, or $6/31$ depending on which piece is split — sometimes
   strictly *increasing* it, which is the dangerous direction for
   $(\star\star)$. So even the best-case restriction doesn't reduce to the
   already-solved base case. No digit/carry formula for $(\star\star)$ was
   obtained, restricted or general.

4. **Step 4 (achievability):** not reached, since it presupposes a working
   Step 3.

## Bottom line for the orchestrator / outline-reviewer
This slug did not close, or make progress narrowing, $(\star\star)$ itself.
It produced two reusable structural lemmas (R1, R2) and two clean,
computation-verified negative findings that should prevent future rounds
from re-attempting (a) the "denominator divides $D$" shortcut or (b) the
bisection-parity-invariance shortcut for the digit/carry transplant. My
honest recommendation: don't re-build this exact slug's digit/carry
technique again without a genuinely new idea (e.g. a majorization/exchange
argument establishing which refinement is worst-case for the window
integral) — the crux-corpus transplant this round was built on
(`aimo-0917`, `aimo-0141`, `aimo-0764`) does not carry over as hoped.
Verdict this slug should expect: **RETHINK or CHANGES-REQUESTED-with-no-
further-build-of-this-exact-technique**, at the proof-reviewer's judgment —
the lemmas (R1, R2) are worth certifying/promoting regardless of the
approach's overall fate.
