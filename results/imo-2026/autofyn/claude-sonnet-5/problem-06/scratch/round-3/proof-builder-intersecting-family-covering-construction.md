# proof-builder report — intersecting-family-covering-construction (round 3)

## Task
Close Gap 2 (periodicity from `n=1`) for IMO 2026 P6, conditional on `(\dagger')`
(a finite covering set `H` exists — treated as a hypothesis this round, its proof
assigned to sibling approaches). The outline split this into two obstructions:
(1) the "coincidence lemma" `\min\{x>a_n:\text{hits }\Sigma_n\}=\min\{x>a_n:
\text{hits }\Sigma_\infty\}`, and (2) no-pre-period / injectivity of the transition
map `G`, via an adapted `aimo-0577`-style mechanism.

## Result: both obstructions fully closed

**Obstruction 1** turned out to have a much shorter proof than the outline's
sketched strong-induction/density mechanism: since `(\dagger')` (the covering
hypothesis) quantifies over **every** pair `i<j` of the whole infinite sequence
(not just pairs bounded by some index `n`), applying it with one index fixed at
`n+1` and the other ranging over ALL other indices `j` (both `j<n+1` and `j>n+1`)
directly shows `a_{n+1}` hits the *full* `\Sigma_\infty`, not merely the partial
`\Sigma_n` it was defined against. This is **Lemma A (Universal Hitting)**, a
three-line consequence of the definitions, and it immediately gives
**Corollary 3.1 (Coincidence Lemma)**: `a_{n+1}=\min\{x>a_n:\text{hits
}\Sigma_\infty\}` for every `n\ge1`, no induction needed. This removes the
`\Sigma_n\subsetneq\Sigma_\infty` "transient" from the construction entirely.

**Obstruction 2**: I first checked (and refuted, via a 4-element toy example
`\mathrm{Good}=\{0,5\}\subset\mathbb Z/10\mathbb Z`) that the transition map `G`
is injective on *all* of `\mathbb Z/L\mathbb Z` — it is not, in general. The
correct, provable claim is narrower: `G` restricted to `\mathrm{Good}` (the set
of residues that actually hit `\Sigma_\infty`) is a bijection, in fact a single
`|\mathrm{Good}|`-cycle (**Lemma B**), proved directly from the elementary
combinatorics of "next marked point on a finite cycle" — no citation needed
beyond that. Combined with Lemma A showing `r_1\in\mathrm{Good}` from the start
(a genuinely new observation: `a_1` itself hits `\Sigma_\infty`, by the same
Universal Hitting argument), this gives periodicity of the residue sequence
`(r_n)` with **zero pre-period**, from `n=1`.

Combining both via a telescoping-sum argument gives the **Master Conditional
Theorem (5.1)**: if `(\dagger')` holds, then `a_{n+T}=a_n+L` for **every**
`n\ge1` (not merely eventually), with `T=|\mathrm{Good}|\le L=\mathrm{lcm}(H)`
and — a bonus exact closed form not anticipated by the outline —
`L_{\mathrm{per}}=L` exactly (proved via a telescoping "sum of gaps around a
finite cycle = circumference" identity).

This strictly supersedes the previously-certified Theorem 2.4 (which only gave
eventual periodicity, `T\le L` a mere bound, `L_{\mathrm{per}}` unspecified) and
fully closes Gap 2. It does **not** need Lemma 2.3 (`\Sigma_n` stabilization) at
all — that machinery is superseded by the more direct Lemma A/Corollary 3.1
argument.

## Numerical corroboration (not a proof step, per CLAUDE.md)
Verified via Python (exact `gcd` simulation + `sympy.primefactors`) on 8 values of
`a_1` spanning Case I and genuine Case II — `9, 15, 35, 65, 105, 143, 221, 1001` —
including the two cases (`35, 65`) that broke round 2's naive mechanism (traced
to round 2 using the *wrong*, non-covering `H=\mathrm{rad}(a_1)`; confirmed here
directly, e.g. for `a_1=35`, `\mathrm{rad}(42)\cap\mathrm{rad}(45)\cap\{2,5,7\}
=\varnothing`, so `\{2,5,7\}` is not even a valid covering set). Using a genuine
candidate covering set (constructed via the bug-fixed "minimal-radical frontier"
method flagged by this round's math-explorer, spot-checked covering for many
pairs), all 8 cases show: `r_1\in\mathrm{Good}`, exact periodicity from `n=1`,
and `L_{\mathrm{per}}=L` exactly — zero exceptions, matching the proof.

## Status: partial (unchanged label, but Gap 2 now fully closed)
Per CLAUDE.md, Status remains `partial` since `(\dagger')` (existence of the
covering set `H`) is not proved in this file — that is the sole gap left, and
it is explicitly assigned to sibling approaches this round
(`persistent-backbone-monovariant`, `forced-primes-well-ordering`,
`explicit-window-backbone-construction`). But the file now contains a complete,
gap-free, unconditional-modulo-`(\dagger')` proof of the problem's *exact*
conclusion for Case II. The moment any sibling approach establishes `(\dagger')`,
Theorem 5.1 here can be cited directly to finish the whole problem (combined
with the already-fully-solved Case I via Lemma S′).

## File written
`/home/agentuser/repo/results/imo-2026-06/approaches/intersecting-family-covering-construction.md`
(full rewrite/extension, Parts 0–2 restated for self-containedness, new
Parts 3–7 with Lemma A, Corollary 3.1, Lemma B, Theorem 4.1, Theorem 5.1 (Master
Conditional Theorem), numerical verification table, and updated "what remains"
section).

## Promotable lemmas (for the reviewer to certify)
- **Lemma A (Universal Hitting)** — Part 3, three-line proof from `(\dagger')`.
- **Corollary 3.1 (Coincidence Lemma)** — Part 3, closes Obstruction 1.
- **Lemma B (single-cycle structure of `\mathrm{Good}` under `G`)** — Part 4,
  closes Obstruction 2 (with an explicit correction of the outline's stronger,
  false "G injective everywhere" framing, replaced by the correct, narrower,
  provable claim).
- **Theorem 5.1 (Master Conditional Theorem)** — Part 5, the main new result:
  `(\dagger')\Rightarrow a_{n+T}=a_n+L` for every `n\ge1`, exact `T,L`. This is
  the highest-value result to certify — it is the exact statement any sibling
  approach needs to cite the instant `(\dagger')` is proved, to finish the
  entire problem.
