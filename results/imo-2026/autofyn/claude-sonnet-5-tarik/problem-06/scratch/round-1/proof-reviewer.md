# Proof review — imo-2026-06 (IMO 2026 P6), round 1

Reviewed three built approaches. Problem: prove existence of `T,L` positive
integers with `a_{n+T}=a_n+L` for every `n`, for the greedy sequence defined by
`a_{n+1}` = least integer `>a_n` with `\gcd(a_{n+1},a_i)>1` for all `i\le n`.

All three approach files honestly self-report `Status: partial`. I independently
re-derived the load-bearing steps of each (by hand and, where a computation was
involved, with a Python greedy simulation) rather than trusting the write-ups.
None is complete; none overclaims `solved`. Verdicts below are per-approach and
independent, per CLAUDE.md's routing rule.

---

## 1. `backbone-existence-crt.md` — Verdict: **CHANGES REQUESTED** (Status: partial, confirmed correct)

**What I verified as correct, gap-free:**
- Lemma P (`\gcd(a_n,a_1)>1` for `n\ge2`): one line from the problem's own
  definition. Correct.
- Lemma P′ (`\gcd(a_i,a_j)>1` for all `i<j`, i.e. `\{P_n\}` pairwise
  intersecting): same argument applied at general `i` instead of only `i=1`.
  Correct, and a genuine (if easy) strengthening — I checked it is actually used
  downstream (Lemma R in the sibling file implicitly needs exactly this, not just
  Lemma P).
- Lemma Q (prime-power base case, `a_1=p^e\Rightarrow a_n=a_1+p(n-1)`): induction
  argument checked line by line — admissibility of `a_n+p` and inadmissibility of
  everything strictly between `a_n` and `a_n+p` are both correctly justified.
  Correct.
- **Domination Lemma** (new this round): `\sum_j D_n(q_j)\ge n` via a union bound
  (every `i\le n` is admissibility-witnessed by some prime factor of
  `x=a_{n+1}`), then averaging pigeonhole gives `\max_jD_n(q_j)\ge n/\omega(x)`,
  and `\omega(x)\le\log_2x` since `x\ge2^{\omega(x)}`. I re-derived this from
  scratch independently and it matches exactly; fully correct, no gaps, purely
  elementary.

**The single load-bearing gap, re-derived and confirmed genuinely open:** the
approach itself identifies two sub-gaps, (a) growth control on `a_n` and (b)
concentration of "dominance" onto finitely many primes. I checked whether (a) is
really open — **it is not**, once you import `bounded-gap-density-covering`'s
Lemma 1 (`a_{n+1}-a_n\le\mathrm{rad}(a_1)`, unconditional, no backbone assumption).
I verified numerically (a_1=247, n up to 1999) that `n/\log_2 a_{n+1}\to\infty`,
confirming that combining Lemma 1 with the Domination Lemma unconditionally
resolves gap (a). This is a genuine finding that neither builder made explicitly
(backbone-existence-crt's own file says gap (a) is "precisely the open content of
the sibling approach," but that's not accurate — the sibling's already-*proven*
Lemma 1, not its unresolved Step 3, suffices). **Gap (b)** — showing only finitely
many distinct primes are ever dominant across all `n` — is genuinely unaddressed
by anything in this file or the other two; this is the real remaining content.
Section 6's "injectivity of the eventual finite-state map" target for
periodicity-from-`n=1` is correctly flagged as unproved, not smuggled in as
established. No overclaiming found.

**Gap to close next round:** prove concentration (gap b): only finitely many
primes are ever "dominant" in the Domination Lemma's sense across the whole
sequence. Then construct the finite covering backbone and prove the injectivity
(or an equivalent) needed for periodicity from `n=1`, not just eventually.

---

## 2. `intersecting-family-covering-construction.md` — Verdict: **CHANGES REQUESTED** (Status: partial, confirmed correct after a fix)

**What I verified as correct, gap-free:**
- Lemma P, Lemma Q: same as above, correct.
- **Lemma R** (eternal witness per index): for fixed `i`, `\varphi(n)=\min(P_n\cap
  P_i)` for `n>i` is a well-defined function into the finite set `P_i`
  (well-definedness uses `\gcd(a_n,a_i)>1` for all `n>i`, which the file derives
  correctly inline — this is exactly Lemma P′, proved independently in the sibling
  file). Infinite pigeonhole (partition an infinite index set into finitely many
  classes, one class is infinite) is applied correctly. Correct, no gaps.
- **Proposition D (dichotomy)**: "every `a_1` either has a single prime dividing
  every term, or it doesn't" is a tautology (law of excluded middle on the
  predicate), correctly noted as exhaustive and disjoint by construction. Fine.
- Case I numerics: I independently simulated `a_1\in\{21,33,39,55,57,69,85\}` and
  confirmed each matches `a_1+p(n-1)` exactly with the claimed saturating prime
  (`p=3` for `21,33,39,57,69`; `p=5` for `55,85`). I also independently simulated
  `a_1=15` and confirmed Case II is genuinely non-vacuous: `2\nmid15`, `5\nmid
  a_2=18`, `3\nmid a_3=20` — no single prime saturates all of the first 200 terms.
  I also verified the specific claim about `a_1=33`: the candidate `44` (strictly
  between `a_4=42` and `a_5=45`) is admissible against `a_1=33` (`\gcd=11`) and
  `a_2=36` (`\gcd=4`) but fails against `a_3=39` (`\gcd(44,39)=1`) — exactly as
  the file claims, confirming even the "easy" solved case needs multi-term
  bookkeeping, not just an `a_1`-check.

**A genuine error I found and fixed:** **Lemma S′'s proof, as originally written,
has an invalid step.** The text argues: "if `x` [with `a_n<x<a_n+p`] were
admissible it would have to equal `a_{n+1}` by minimality of the true `a_{n+1}`
among admissible candidates greater than `a_n` — contradiction." This is **not**
a valid inference: minimality of `a_{n+1}` only gives `a_{n+1}\le x` when `x` is
admissible, not `x=a_{n+1}` (a priori a different, smaller admissible candidate
could exist strictly between `a_n` and `x`). As literally written, this step does
not establish what it claims. However, the *lemma's statement is true* and I
found a correct short repair using only tools already present elsewhere in the
same file (the "no multiple of `p` strictly between consecutive multiples of `p`"
fact from Lemma Q's own proof): from admissibility of `a_n+p` we get `a_{n+1}\le
a_n+p` (a legitimate use of minimality, giving `\le`, not `=`); if this were
strict, `a_n<a_{n+1}<a_n+p` forces `p\nmid a_{n+1}`, contradicting the global
saturation hypothesis `p\mid a_{n+1}`. I certified the corrected proof into
`lemmas/lemma-S-prime-saturation-AP.md`, with the fix clearly flagged. The lemma
**statement** is unchanged and no stronger than what was claimed; only the proof
needed repair, and the repair needed no new mathematical content.

**What remains open, confirmed genuinely unresolved:** Case II (`a_1=15` etc.) —
no finite covering set `H`, no periodic residue pattern, and (per point 3 of the
file's own honest self-assessment, which I independently confirmed via the `44`
computation above) no strong-induction-from-`n=1` invariant. The `a_1=247` stress
test (no periodicity detected in 15000 simulated terms, per the file) is a real,
unresolved difficulty, not a hypothetical one.

**Gap to close next round:** construct, for general Case-II `a_1` (or at least
prove existence of, without needing an explicit formula), a finite helper prime
set `E` such that `H=P_1\cup E` permanently covers the sequence, and prove the
resulting periodic pattern holds from `n=1`.

---

## 3. `bounded-gap-density-covering.md` — Verdict: **CHANGES REQUESTED** (Status: partial, confirmed correct), with a strong dead-end flag on its core strategy

**What I verified as correct, gap-free:**
- Lemma P, Lemma Q: correct, as above.
- **Lemma 1** (`a_{n+1}-a_n\le\mathrm{rad}(a_1)` for every `n`, unconditionally):
  I re-derived this independently. Let `L=\mathrm{rad}(a_1)` and `x_0` the least
  multiple of `L` exceeding `a_n`. For `i=1`: `a_1`'s prime factors are exactly
  `P_1\subseteq` primes of `L`, so some `p_j\mid a_1` and `p_j\mid L\mid x_0`,
  giving `\gcd(x_0,a_1)\ge p_j>1`. For `2\le i\le n`: Lemma P gives
  `\gcd(a_i,a_1)>1`, so some prime `p_j` divides both, and since `p_j\mid a_1`,
  `p_j\in P_1`, so `p_j\mid L\mid x_0`, giving `\gcd(x_0,a_i)\ge p_j>1`. So `x_0`
  is admissible, forcing `a_{n+1}\le x_0\le a_n+L`. This matches the file's proof
  exactly; correct, no gaps. I additionally verified numerically (Python greedy
  simulation) that the observed max gap never exceeds `\mathrm{rad}(a_1)` for
  `a_1\in\{15,65,105,143,247\}` (e.g. `a_1=247`: `\mathrm{rad}=247`, observed max
  gap `78` over 400 terms) — consistent, though this is only a sanity check, the
  proof itself is self-contained and doesn't need it.

**The approach's own central claim about its Step 3 idea is correct as a negative
result.** The "trace/hitting-set" refinement is presented honestly as reducing to
exactly the same backbone-finiteness question the sibling approaches face,
illustrated concretely with `a_1=65` (I independently re-simulated `a_1=65` and
confirmed the sequence is not the crude `L=65` fallback pattern — the actual
sequence uses smaller gaps via primes 2 and 3 not in `P_1=\{5,13\}`, consistent
with the file's claim). This is a genuine, rigorously-supported negative finding:
the approach's distinguishing promise ("bound first, without ever identifying the
backbone") does not survive past Lemma 1. I found no flaw in this negative
argument, and no way to route around it that the file missed.

**Judgment call on routing:** per CLAUDE.md, verdict is tied to Status
(`partial`→CHANGES REQUESTED, `unsolved`→RETHINK), and this file's Status is
honestly `partial` (Lemma 1 is real, correct, reusable progress), not
`unsolved` — so I am not using RETHINK here despite the approach's own strategy
being a demonstrated dead end. I flag explicitly for the orchestrator/outliner:
**re-dispatching this exact slug to push further on its original Step 3 idea
(density-only, backbone-agnostic finite state) is very unlikely to produce
anything new** — the builder already rigorously closed off that route. If this
slug is kept alive, it should pivot to a different mechanism (e.g. combine Lemma 1
directly with the Domination Lemma from `backbone-existence-crt`, as I did above)
rather than repeat the trace/hitting-set refinement.

---

## Certified promotable lemmas

Wrote to `results/imo-2026-06/lemmas/`:
- `lemma-P-permanent-hub.md` — Lemma P, certified as-is.
- `lemma-P-prime-pairwise-intersecting.md` — Lemma P′, certified as-is (strictly
  stronger than Lemma P; both builders effectively used it).
- `lemma-Q-prime-power-base-case.md` — Lemma Q, certified as-is (all three files
  proved this identically).
- `lemma-1-uniform-gap-bound.md` — Lemma 1 from `bounded-gap-density-covering`,
  certified as-is, plus a new cross-approach consequence note (combined with the
  Domination Lemma, resolves growth-control gap (a) of `backbone-existence-crt`).
- `domination-lemma.md` — Domination Lemma from `backbone-existence-crt`,
  certified as-is.
- `lemma-R-eternal-witness.md` — Lemma R from `intersecting-family-covering-construction`,
  certified as-is.
- `lemma-S-prime-saturation-AP.md` — Lemma S′ from
  `intersecting-family-covering-construction`, certified **with a reviewer-repaired
  proof** (the original minimality step was invalid as written; statement
  unchanged, repair uses only tools already present in the same file).

## Overall round-1 assessment

No approach is `solved`; no APPROVE issued. All three make genuine, verified,
non-overlapping progress (Lemma S′'s dichotomy is the most advanced single result —
it fully solves a strictly larger sub-case than Lemma Q from `n=1`), and I found one
real cross-approach synergy (Lemma 1 + Domination Lemma jointly close half of
`backbone-existence-crt`'s stated gap) that none of the three builders identified on
their own. All three approaches, despite different entry points (CRT/finite-state,
explicit covering construction, density/counting), converge on the **same** core
open problem: proving "backbone finiteness" — that only finitely many primes beyond
`\mathrm{rad}(a_1)` are ever needed to keep the greedy process covered — for the
genuine multi-prime case (Case II, witnessed non-vacuous and hard by `a_1=15` and
`a_1=247`). This convergence across three structurally different framings is a
signal worth flagging to the outline-reviewer: the field may benefit from at least
one genuinely different framing next round (e.g. attacking backbone finiteness via
a second-moment/Turán-type bound on `\sum_pD_n(p)^2`, as `backbone-existence-crt`
speculates but does not attempt, or a direct explicit-construction attack on
`a_1=247` specifically, rather than further variations on density/covering/CRT
machinery that all three current approaches already share).

`current.md` created at `/home/agentuser/repo/results/imo-2026-06/current.md` with
Status `partial`, all three approaches recorded under "Approaches tried," and
"Current best" combining the certified lemmas plus the cross-approach synergy
finding, with the shared open gap (Case II backbone finiteness + periodicity from
`n=1`) stated precisely.
