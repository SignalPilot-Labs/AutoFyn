# Build report — sunflower-bundle-closure (round 8)

**File written:** `results/imo-2026-06/approaches/sunflower-bundle-closure.md`
(overwritten in place with the full build; Status: `partial`).

## What I did

Read the round-8 outline (`sunflower-bundle-closure.md`, freshly written this
round), the outline-reviewer's independent verification of its four flagged
claims, `current.md`, and the relevant certified lemma files (`lemma-ER-
eventual-realization-dichotomy.md`, `lemma-escape-confinement.md`, `lemma-
lambda-S-reduction-and-single-companion-finiteness.md`, `theorem-CD-core-
decomposition-and-lemma-TC.md`, `theorem-V-veto-finite-iff-MRS.md`, `lemma-
MS-minimal-radical-stabilization-sufficiency.md`, `lemma-permanent-bundle.md`,
`lemma-P-prime-pairwise-intersecting.md`, `lemma-permanent-inadmissibility.md`,
`lemma-C-global-intersection-collapse.md`, `lemma-C-generalized-subsequence.md`,
`lemma-omega-bound-key-lemma.md`).

Filled in the outline's Δ-system mechanism completely, and in the process
found and closed a gap the outline itself had flagged as open ("Open gap 1":
existence of a core-avoiding witness for the Escape-Confinement Corollary).

**Key new construction: Lemma ERD-C** (Eventual Realization Dichotomy for
radical classes). The certified Lemma ER is stated for a single integer `y`;
I proved a genuine upgrade — for any nonempty finite set of primes `C`,
*exactly* one of (i) `C` is realized as some actual term's exact radical, or
(ii) `C` is permanently blocked by a witness and *never* realized at any
index — by applying Lemma ER to the canonical test integer `T_C:=\min\{x>a_1:
\mathrm{rad}(x)=C\}` and combining with Lemma P′ and the Permanent-
Inadmissibility Lemma for the mutual-exclusion direction. This dichotomy,
applied to `C:=S` (the core itself), turns out to *dissolve* the outline's
"Open gap 1" rather than requiring it be separately assumed: either `S` is
realized (in which case a new short lemma I call **Lemma SR** shows `𝓥_S` is
automatically finite via the certified No-Resurrection Lemma, with **no**
need for `(UB_S)` at all), or `S` is blocked (in which case the blocking
witness is *exactly* the `j_3` the outline's Escape-Confinement Corollary
needed — supplied for free, not assumed). I also checked "Open gap 2" (does
the argument secretly need `I_S` infinite?) and found it doesn't: `𝓥_S`
infinite forces `I_S` infinite automatically (since `𝓥_S⊆\{P_i:i\in I_S\}`),
so the finite-`I_S` case is handled as an immediate trivial sub-case with no
separate hypothesis.

With both gaps dissolved, I wrote out the full Δ-system (sunflower) dichotomy
from scratch (proved by induction on the size bound `M`, confirmed by the
outline-reviewer to be absent from the KB/crux corpus) and carried out the
outline's Step 4 case analysis in full rigor: pairwise-disjoint case via the
pigeonhole/injection Corollary; sunflower case split via Lemma ERD-C applied
to the coarsened bare value `S\cup Y`, with a subtlety I had to resolve
carefully — the "petal" pigeonhole argument in sub-case (b-ii) needs the
witness element supplied by Escape-Confinement to land in the petal
`Q_l\setminus Y`, not the sunflower's core `Y`; I proved this holds
automatically because `Y` is itself part of the blocked bare value
`\kappa'=S\cup Y`, so `Y\cap\mathrm{comp}(a_{j_3'})=\varnothing` is forced by
the blocking condition itself.

**Result: a complete, unconditional proof of `(UB_S)\Rightarrow\Lambda_S`
finite for every proper core `S`.** Combined with the already-certified
reduction chain (Theorem 5.1 ← Lemma MS ← Theorem V + Theorem CD/Lemma TC ←
Λ_S-Reduction Lemma), this closes the *entire remaining problem* down to a
single hypothesis: `(UB_S)` for every one of the finitely many proper cores
— equivalently `\sup\{\omega(a_n):n\notin I_{P_1}\}<\infty` (a weaker
requirement than round 3's global `\omega(a_n)=O(1)`, since indices with the
top-core imprint `P_1` impose no constraint at all, by Lemma TC). I proved
this equivalence explicitly (not just asserted it) via a short two-direction
argument using the finiteness of the core family.

**Attempted, and honestly report as not closed:** `(UB_S)`/`\omega(a_n)=O(1)`
itself (§5 of the file). Tried the outline's suggested lever (combine the
pigeonhole Corollary with a bundle-shape count) and found precisely why it
fails: the Corollary bounds *how many* pairwise-disjoint bundles exist, not
*how large* any single bundle is — a structurally different question the
Δ-system machinery cannot answer. Cross-checked with a classical
divisor-count argument (any bound from `a_n`'s magnitude alone gives
`O(\log n/\log\log n)`, not `O(1)`), confirming a true `O(1)` bound (if it
holds) needs a combinatorial argument tied to the greedy recursion itself. Ran
a fresh independent numerical check (own Python generator + `sympy`) of
`\omega(a_n)` on three mandated hard cases (`a_1=247,2747,21528751`) up to
`N=1200`–`3000`, confirming single-digit `\omega` throughout (max 6, 6, 7
respectively) — consistent with, but not proof of, the hypothesis.

## Verification performed

- Re-derived every step of Lemma ERD-C, Lemma SR, the Δ-system dichotomy, and
  the Main Theorem's case analysis by hand, checking each cited lemma's exact
  certified statement against how I used it (Escape-Confinement's `κ=S\cup Q`
  form, No-Resurrection's `P_k\subsetneq C` hypothesis, Lemma P′'s pairwise
  form).
- Caught and fixed a subtle base-case wrinkle in the Δ-system induction (at
  `M=1`, the "process terminates" branch can never actually trigger, by a
  distinctness argument) — added an explicit clarifying remark so a reviewer
  does not mistake this for circularity.
- Ran Python (`sympy.primefactors`, own greedy generator) to sanity-check: (a)
  that observed proper cores in `a_1=247,2747` are indeed "blocked" (Case ii)
  with small witness indices (2–4), matching the theory; (b) `\omega(a_n)`
  growth stays single-digit on three hard cases, consistent with the open
  hypothesis. These are supporting checks, not proof steps, and are labeled
  as such in the file.
- Cleaned up a batch of stray `$`-vs-backtick typos from drafting (cosmetic
  markdown fix only, no content change).

## Honest status

Status: `partial`. The file's Main Theorem
(`(UB_S)\Rightarrow\Lambda_S` finite, unconditionally beyond `(UB_S)`) is a
complete, gap-free proof — a genuine tightening beyond the outline, since it
eliminates both flagged open sub-gaps rather than leaving them as additional
standing hypotheses. The sole remaining open content, precisely stated, is
`(UB_S)` itself (equivalently `\omega(a_n)=O(1)$ off the top core) — this
round did not close it, and §5 explains precisely why the tools built this
round cannot (they answer a "how many objects" question, not a "how large is
each object" question).

## Promotable lemmas (see file's "Promotable lemmas" section for full
statements)

- Lemma ERD-C (Eventual Realization Dichotomy for radical classes)
- Lemma SR (Self-Realized core shortcut)
- Δ-system (sunflower) dichotomy for uniformly bounded finite-set families
- Escape-Confinement Pairwise-Disjoint-Bundle-Count Corollary
- Main Theorem: `(UB_S)\Rightarrow\Lambda_S` finite (the file's central,
  fully proved result)
