# Round 13 proof-reviewer report — imo-2026-03

Reviewed both built slugs (`greedy-halving-adversary`, `lp-duality-certificate`)
and their round-13 new lemma candidates. All new claims independently
re-verified with freshly written exact-`Fraction` scripts (not the
builders' own scripts): `/tmp/round-13/verify.py` (Max Domination, Triangle
Bound, R13.2 threshold closure) and `/tmp/round-13/verify_prop28.py`
(Proposition 28's dominant-fragment case). No overclaims found in either
approach file; both Status headers (`partial`) match reality.

## Slug: greedy-halving-adversary — CHANGES REQUESTED (Status: partial)

**New claims this round:**

1. **Lemma 27 (Triangle Bound for A)**: for any two finite multisets
   $X,Y$ of positive reals, $A(X)-A(Y)\le A(X\cup Y)\le A(X)+A(Y)$.
   Proof derives cleanly from the already-certified
   `cross-term-identity-threshold` (Lemma 8) plus the trivial bound
   $0\le A(Y)\le\mathrm{Total}(Y)$ (itself immediate from Lemma 2). I
   re-derived the proof independently and cross-checked the final
   inequality directly (bypassing the cross-term machinery, computing
   $A$ by direct sort-and-alternating-sum on $X$, $Y$, $X\cup Y$) with a
   fresh 20,000-trial exact-`Fraction` script: **zero violations**. Sound,
   general, no gap. **Certified** (`lemmas/triangle-bound-for-a.md`,
   reviewer certification note appended).

2. **Proposition 28 (Dominant-Fragment closure of p2's own split)**: if
   $p_2$'s own induced split $F_2$ has a fragment $f_1$ dominating
   everything else combined ($f_1\ge\mathrm{Total}(F_2\setminus\{f_1\})+
   \mathrm{Total}(R)$ for the rest of the tail refinement $R$), then
   unconditionally (no induction hypothesis) $A(F_2\cup R)\le p_2-A(R)$.
   Proof: dominant-element-removal (Lemma 7) plus the new Triangle Bound.
   I independently verified with a fresh 30,000-trial exact-`Fraction`
   script generating random splits of $p_2$ and random legal-shaped
   refinements $R$, filtering to the 4,820 trials that actually satisfy
   the dominance hypothesis: **zero violations**. Sound as stated.

   **Scoping is honest, not overclaimed.** The builder's own text
   explicitly states that turning this into a *complete* closure of the
   corresponding branch of $(\dagger)$'s $p_2$-cut complement still needs
   one more bookkeeping step (combining with the $(\star_{n-2})$-style
   recursive argument Proposition 22 already uses, to convert
   $A(G')\le p_2-A(R)$ into the needed $A(G')\le p_2-f(n)$) — and that
   this step, while "mechanically identical" to Proposition 22's own
   proof, was **not** carried out symbolically this round. I confirm this
   residual step is real (the bound proved, $A(G')\le p_2-A(R)$, is
   strictly weaker than what's needed unless $A(R)\ge f(n)$ is separately
   established) and correctly flagged as open, not silently assumed. The
   builder correctly did **not** request standalone certification of
   Proposition 28 for exactly this reason (see the file's own "Promotable
   lemmas" section) — matches my independent assessment; I concur with
   leaving it uncertified as a standalone closure.

3. **No-dominant-fragment branch**: honestly reported open, with a
   concrete non-vacuous witness (symmetric bisection of $p_2$ always
   violates the dominance hypothesis whenever the rest of the tail is
   nonempty) and a precise diagnosis (same difficulty as Claim (A)'s Case
   I, but `ratio-2-spacing-lemma`/`last-element-bound` do not transfer
   verbatim since the reference set here is itself already refined, not
   raw ratio-2). This diagnosis is correct — those two certified lemmas'
   proofs do rely on an unrefined ratio-2 spacing structure that a cut
   reference multiset need not retain. No overclaim.

4. **ℓ(F)=2, P≠∅ shifted-reference sub-case**: honestly reported as
   attempted-but-not-completed (ran out of round budget before the
   shifted dominance threshold, which must add Total(P) to both sides,
   could be carried through to a full statement). Correctly not claimed
   as progress.

**Verdict rationale.** Real, unconditional, reviewer-verified new
machinery (Triangle Bound) and one genuinely new closed sub-case
(Proposition 28's dominant-fragment branch, modulo the flagged residual
bookkeeping step) — this is real progress, not a reformulation. But
$(\dagger)$'s $p_2$-cut complement is not closed, the ℓ(F)=2 P≠∅ item is
untouched, and the pre-existing $v<p_2$ open branch remains — the Status
header `partial` is accurate; no gap to solved was overlooked. **CHANGES
REQUESTED.**

## Slug: lp-duality-certificate — CHANGES REQUESTED (Status: partial)

**New claims this round:**

1. **Max Domination Lemma (R13.1)**: for any sorted multiset
   $S=\{b_1\ge\cdots\ge b_r\}$, $A(S)\le b_1=\max(S)$. Proof is a clean
   two-case telescoping regroup (odd/even $r$) using only sortedness and
   nonnegativity — fully general, no dependence on any prior lemma in this
   project. I independently re-derived the proof and re-verified with a
   fresh 20,000-trial exact-`Fraction` script over random sorted
   multisets of size 1–10: **zero violations**. Sound, no gap.
   **Certified** (`lemmas/max-domination-lemma.md`, reviewer certification
   note appended).

2. **R13.2 (Unconditional p2-Threshold Closure)**: if $p_2\le T/D_n$,
   bisecting $p_1$ alone (Theorem C, already certified) gives
   $\Phi\le a_nT$ with **zero induction hypothesis** anywhere. Proof
   substitutes Max Domination's bound $A(\text{tail})\le p_2$ into
   Theorem C's exact identity, then uses the already-certified
   Telescoping Threshold Lemma ($2a_n-1=1/D_n$) to solve the threshold
   algebra. I independently re-verified with a fresh 20,000-trial
   exact-`Fraction` script computing $\Phi$ directly via the certified
   $\Phi=(T+A)/2$ formula (not reusing the builder's script): 2,374
   trials satisfied $p_2\le T/D_n$, and the bound held in **every one**,
   zero violations. Sound, no gap. **Certified**
   (`lemmas/unconditional-p2-threshold-closure.md`).

3. **Trichotomy restatement (R13.3)**: correctly restates the outline's
   binary dichotomy (case (a) qualifying-peel-target vs. case (b)
   no-qualifying-peel-target) as an honest trichotomy: case (a)
   [conditional on IH, already known — re-verified the transfer claim
   directly by re-reading the cited Corollary's proof, which indeed never
   specializes to $k=2$], case (b1) [new, unconditional, via R13.2],
   case (b2) [genuinely open]. The claimed disjointness/genuinely-new
   status of case (b1) relative to every prior sufficient region (Theorem
   A's band, Theorem B's IH-conditional region, Equal-Pieces Closure,
   Spare-Cut Bisection Corollary) is a reasonable characterization — I
   did not find a contradiction (none of those other regions constrain
   $p_2$ alone against $T/D_n$ independent of $p_1$'s value).

4. **Case (b2) witness and peel-then-dominate refutation**: the witness
   $(0.45,0.15,0.25,0.15)T$ at $n=3$ is checked directly against both
   thresholds (case (a): $p_2\ge a_3T/2=4T/15\approx0.267T$, fails since
   $p_2=0.15T$; case (b1): $p_2\le T/D_3=T/15\approx0.067T$, fails since
   $0.15T>0.067T$) — arithmetic checks out, genuinely in the open region.
   The "peel-then-dominate" 2-cut construction's refutation is reported
   with an explicit 3000-trial exact-`Fraction` stress test finding
   ~10% failure rate including large overshoots — this is a negative
   result, correctly not promoted to a positive claim, and is a
   structurally distinct construction from round 12's refuted
   "bisect-largest-cascade" (peel-then-bisect vs. cascading bisection),
   so it is not redundant negative content.

**Verdict rationale.** Two new, fully general, unconditional, reviewer-
verified lemmas that are genuinely disjoint from every prior sufficient
region for the general upper bound — real progress, not a
reformulation. Open Gap 1 (the general upper bound $c(n)\le a_nT$ for
arbitrary markings) is honestly reported as **not** closed, with case
(b2) left as a real, explicit, non-vacuous open region. No overclaim.
**CHANGES REQUESTED.**

## Lemma certification summary

- **`triangle-bound-for-a`** — CERTIFIED (was previously submitted,
  uncertified; now certified after independent re-verification).
- **`max-domination-lemma`** — CERTIFIED.
- **`unconditional-p2-threshold-closure`** — CERTIFIED.
- Proposition 28 (greedy-halving-adversary) — **not** promoted to a
  standalone lemma file, matching the builder's own request; it is a
  documented partial result within the approach file only, correctly
  scoped.

## current.md

Updated `results/imo-2026-03/current.md` with a new "Round 13" entry
under "Approaches tried" summarizing both builds' verified content and
scoping, consistent with the file's running narrative style. `## Status`
remains `partial` (unchanged) — neither built slug reaches `solved`, and
no prior claim in the file needed correction this round (no overclaim
found).

## Outcomes recorded

- `greedy-halving-adversary`: `record_outcome` → `partial`.
- `lp-duality-certificate`: `record_outcome` → `partial`.

## Overall verdicts

- `greedy-halving-adversary`: **CHANGES REQUESTED** (Status: partial).
- `lp-duality-certificate`: **CHANGES REQUESTED** (Status: partial).

## Notes for next round (handed to run_state, not authoritative here)

- greedy-halving-adversary's most surgical restart point: finish the one
  flagged bookkeeping step turning Proposition 28's dominant-fragment
  bound into a complete closure (combine with the $(\star_{n-2})$-style
  recursive argument, exactly as Proposition 22 does) — this is a
  precise, narrow, likely-mechanical task, not a new mechanism.
- lp-duality-certificate's case (b2) is now the sharpest remaining
  open region for the general upper bound: $p_1<T/2$ and
  $T/D_n<p_2<a_nT/2$ (a real, order-$T$-wide band, not a corner case).
  peel-then-dominate is refuted; next round should look for a genuinely
  different (not incrementally-more-cuts) mechanism, or attempt a
  recursive (IH-dependent) argument specifically tuned to case (b2)
  rather than another unconditional-construction attempt.
