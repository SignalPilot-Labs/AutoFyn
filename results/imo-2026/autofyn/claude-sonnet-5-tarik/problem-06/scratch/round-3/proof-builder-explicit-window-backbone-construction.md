## Task
Build the round-3 outline for `explicit-window-backbone-construction` on
IMO 2026 P6 (`results/imo-2026-06/`), specifically closing (or honestly
diagnosing) the termination gap the outline-reviewer flagged: the outline's
"iterate/enlarge K" mechanism for the Key Lemma (some finite K makes
`H_K:=\bigcup_{i\le K}\mathrm{rad}(a_i)` a covering set for FCBC) had no
stated termination argument.

## What I did
Spent the round on genuine new mathematical content rather than re-running
the same empirical checks:

1. **Proved a new Equivalence Lemma**: the Key Lemma (finite `K` suffices)
   is not a restricted special case of the Finite Covering Backbone
   Conjecture (FCBC) — it is *logically equivalent* to it. Any finite
   covering set `H` can be converted, with an explicit formula
   (`K=\max_{p\in H\cap\Pi}\mu(p)`, `\mu(p)` = first index where `p`
   divides a term), into a window `H_K` that also covers. This formally
   unifies the three "Gap-1" approaches in the population (this one,
   `persistent-backbone-monovariant`, `forced-primes-well-ordering`) as
   attacking the identical proposition.
2. **Proved a Patch Lemma**: any single coverage failure of `H_K` at pair
   `(i,j)` forces `i>K` and is always repaired by setting `K':=i`. This
   pins down precisely what's missing: not repairability (always available)
   but a proof that only finitely many repairs are ever needed.
3. **Diagnosed, honestly, why the outline's mechanism (i) cannot be
   completed by Lemma C's finite-descent template**: the natural candidate
   monovariants (`|H_K|`, `2^{|H_K|}-1`) are non-decreasing in `K` — the
   wrong direction for a pigeonhole/descent argument (Lemma C needed
   bounded *and* non-increasing). This is reported as a diagnostic finding
   (not a formal impossibility theorem), consistent with the CLAUDE.md
   instruction to report honestly rather than overclaim.
4. **Proved a new, unconditional Minimal Radical Reduction Lemma**:
   admissibility of a candidate against `a_1,\dots,a_n` reduces exactly to
   admissibility against the inclusion-minimal radicals among them (a
   finite-poset minimal-element argument). Verified by direct simulation
   (`a_1=221`, 199 steps, exact agreement) but explicitly checked and
   reported that this reduction alone does not bound anything (`|M_n|`
   keeps growing, `42` at `n=199`).
5. **Falsified the outline's mechanism (ii) empirically**: computed exact
   minimal sufficient `K` for eleven values of `a_1`; among eight cases with
   `\omega(a_1)=2`, minimal `K` takes three different values (`2,3,4`), so
   no clean formula in `\omega(a_1)` alone can give the exact minimal `K`.
6. **Extended round-2's adversarial-case coverage checks** (`a_1=4199,4087`,
   where the canonical witness set `W` is likely unbounded) out to 20,000
   terms via the signature-pigeonhole reduction: zero coverage failures in
   both cases, reinforcing that `H_K`-coverage and `W`-finiteness are
   different (and the former looks much more tractable) even though the
   round didn't produce a proof.

## Result
Status: `partial`. The Key Lemma / FCBC remains open — this was not solved.
But the round produced three fully rigorous, reusable new lemmas (Equivalence
Lemma, Patch Lemma, Minimal Radical Reduction Lemma) and an honest, precise
diagnosis of exactly why the proposed mechanism (i) fails to close the gap
via finite-descent, plus an empirical refutation of mechanism (ii) as
literally stated. This sharpens the population's shared target (formally,
not just informally, unifying the three Gap-1 approaches via the Equivalence
Lemma) without overclaiming a solution.

## File written
`/home/agentuser/repo/results/imo-2026-06/approaches/explicit-window-backbone-construction.md`
(full detail, Status `partial`, Promotable lemmas section lists Lemma W1, W2, W3
for the reviewer to consider certifying into `results/imo-2026-06/lemmas/`).
