# Proof-reviewer report — round 12, imo-2026-03

All 5 round-12 builds independently re-verified with from-scratch exact
`Fraction` Python scripts (not the builders' scripts). Summary of method
and findings per slug below; certified lemmas listed at the end.

## 1. `self-similar-induction-on-n` — CHANGES REQUESTED

**Claim reviewed:** General Theorem GT($m$) — for $D$ with $|D|\le m+1$,
$\max(D)\le2^m$: $\mathrm{OddSum}(D\cup\Gamma_{m-1})\ge\min(\mathrm{sum}
(D),2^m)$ — proved for $m=0,1,2,3$ via a case split on $p=\#\{a_i>
2^{m-1}\}$ (further split by $r$ when $p=0$), with a corollary closing
gap (a) of the shared Branch-I.A window (endpoint value, all admissible
$D$) at $\ell=1,2,3,4$.

**Independent verification.** Random uniform-$D$ tests ($m=0..4$, 3000
trials each): 0 violations. Adversarial search biased near the $p$/$r$
thresholds ($m=1..5$): 0 violations, minimum margin exactly 0 (tight).
Exact gap-(a)-regime tests (random admissible $D$ with $\mathrm{sum}(D)=
2^m+\varepsilon$, exact composition sampling, $m=0..3$): 3150/5771/7089
admissible instances at $m=1/2/3$ respectively, 0 violations. All
individual peeling identities (P2, P1, R2, R1, the $p=0$ base identity)
re-derived and confirmed algebraically.

**Gap found (real, but narrow — does not affect the corollary).** The
file's boxed GT($m$) *statement* has no bound on $\mathrm{sum}(D)$, but
its proof's "Feasibility bound $p\le2$" is, by the file's own honest
admission ("not asserted globally"), only justified when
$\mathrm{sum}(D)<3\cdot2^{m-1}$. Outside that zone $p\ge3$ (or $r\ge3$)
is possible and genuinely uncovered by the case split. My own stress
test (D with $\mathrm{sum}(D)$ up to $\approx3\cdot2^m$) found zero
violations there either — the theorem is very likely true in full
generality — but this is not established by the given proof. I certified
a **scoped, corrected version** (adds the hypothesis $\mathrm{sum}(D)<
3\cdot2^{m-1}$) into `lemmas/general-peeling-theorem-and-window-endpoint-
closure.md`. Crucially, every actual use of GT($m$) in this file — the
top-level gap-(a) call and every recursive call — has $\mathrm{sum}(D)$
strictly inside this safe zone (verified explicitly by tracing the
recursion's sum bounds at each level), so **the corollary (window's gap
(a) closed for $\ell=1,2,3,4$) is fully valid and independently
reconfirmed**, unaffected by the correction.

**Verdict rationale:** genuine, substantial, correctly-verified new
content (the corollary), with one real completeness gap in the general
lemma's literal statement, caught and fixed via a scoped certification
rather than blocking the round. Status `partial` correct.

## 2. `greedy-reduction-geometric` — CHANGES REQUESTED

**Claims reviewed:** Elementwise Monotonicity Lemma (OddSum monotone in
one coordinate, $N$ fixed), Transfer Monotonicity Theorem (moving mass
from a $D$-coordinate into the window's $c_1$ never decreases OddSum,
under stated hypotheses), Window Reduction Theorem (gap (b) — both the
piece-cap-unsaturated sub-case (b)(i), previously covered by Lemma TPI,
and the piece-cap-saturated sub-case (b)(ii), previously open — fully
closed, reducing the whole window to the single Endpoint Statement).
Special attention per the dispatch: the "$|D|=1$ headroom short by
exactly $\varepsilon$" subtlety and its fix.

**Independent verification.** Elementwise Monotonicity: 5000 exact
trials, $|N|=0..8$, 0 violations. Transfer Monotonicity: 2000 trials per
mechanism (a)/(b), built from window-specific data, 0 violations. Full
Window Reduction chain: 2259 randomly generated admissible window
instances ($\ell=2..6$), literal reconstruction of the reduction sequence
per the mechanism-selection rule (mechanism (b) if $k<\ell$, else
mechanism (a)), directly checking $\mathrm{OddSum}(D\cup\{c_1\}\cup
\Gamma_{\ell-1})\ge\mathrm{OddSum}(D_0\cup\{\mathrm{cap}\}\cup
\Gamma_{\ell-1})$: 0 violations.

**Headroom-fix soundness check (the round's specific caution).** Verified
the algebra directly: $H-\Delta=(k-1)\mathrm{cap}-\varepsilon$; for
$k\ge2$ this is $\ge\mathrm{cap}-\varepsilon\ge2-1>0$ (using $\ell\ge2
\Rightarrow\mathrm{cap}\ge2$, $\varepsilon<1$), so mechanism (a) alone
suffices; for $k=1$ it is $-\varepsilon<0$, genuinely short, and the file
correctly switches to mechanism (b) (fresh slot, needs no headroom,
valid whenever $k<\ell$, which holds for the tight $k=1$ case since
$\ell\ge2$). This is a real fix, not a rebranding — the "insert a fresh
slot" route is a structurally different (and here, necessary) mechanism,
not the same computation dressed up.

**No gap found.** All identities, both monotonicity theorems, and the
chained reduction argument check out. Combined with slug 1's GT($m$)
corollary, **the shared window is now fully closed (every gap) at
$\ell=1,2,3,4$** — strictly stronger than either file's own standalone
claim (the sibling file's own round-12 corollary explicitly still lists
gap (b)(ii) as open; this file's Window Reduction Theorem closes it).
Certified `lemmas/window-reduction-theorem-and-elementwise-monotonicity.md`.

**Verdict rationale:** complete, gap-free, independently re-verified
positive result; gap (a) (the endpoint statement itself, beyond
$\ell=1..4$) remains open, so `partial` is correct.

## 3. `lp-duality-split-polytope` — CHANGES REQUESTED

**Claims reviewed:** Integer-Alternating-Sum Lower Bound Lemma
($\mathrm{AltSum}$ of $m$ distinct nonnegative integers $\ge\lfloor m/2
\rfloor$); Perfect-Tie-Family Exact Characterization Theorem at $e_0$
(only $s=n-1$ active pieces ever attain $c(n)$, exactly, among
zero-residual self-/fragment-tie constructions).

**Independent verification.** Brute-force exact `Fraction` script:
literal $e_0$ coordinates computed from the certified formula; for
$n=2,\dots,12$, every active-set size $s=0,\dots,n$ (all $\binom{n+1}{s}$
choices per size, not sampled), the true minimum $\mathrm{OddSum}(M)$
matches the closed-form prediction exactly, and the theorem's three
consequences (odd-parity always fails, only even $m=2$ i.e. $s=n-1$
clears $c(n)$, and does so with exact equality) hold with zero exceptions
across all 117 tested $(n,s)$ pairs. Also independently confirmed Lemma
12.1's underlying identity ($\mathrm{OddSum}(M)=\tfrac12+\tfrac12
\mathrm{AltSum}(U)$) against a literal bisection construction (not just
the closed-form shortcut), $n=4,6,8$, 30 random active sets each, exact
match. Re-derived the odd-parity-always-fails inductive proof
($2^{n+1}>2n+3$) from scratch — correct.

**No gap found.** This is a clean, elementary, fully general lemma plus a
correctly and completely proved theorem for the stated (zero-residual)
sub-family, honestly scoped as not covering the general
nonzero-residual fragment-vs-fragment family. Certified
`lemmas/integer-altsum-lower-bound-and-perfect-tie-characterization.md`.

**Verdict rationale:** genuine, disjoint-technique, independently
verified negative result strengthening the case against a bounded
construction at $e_0$; does not resolve the Existence Theorem, so
`partial` is correct.

## 4. `global-lp-vertex-sufficiency` — CHANGES REQUESTED

**Claims reviewed:** (a) Region-Boundary Monotonicity as literally
proposed (fixed-vertex straight-line path monotonicity) — refuted at
$n=3$ (numerical, noise-controlled: re-run at $3\times$ restart count,
same sign-change pattern persists). (b) Transplanting the exact
$e_0$-closing $k$-Anchor-Merge construction unchanged to every region
point — refuted in exact `Fraction` arithmetic, $n=2,\dots,8$.

**Assessment.** (a) is honestly and correctly labeled as numerical
evidence, not a proof, with an explicit noise-control step distinguishing
a genuine finding from optimizer jitter (restart-count tripling
preserving the qualitative sign-change pattern is reasonable evidence of
a real, not spurious, effect) — appropriately not certified. (b) uses the
already-certified Theorem 10 closed form and exact rational arithmetic
throughout, with a documented and fixed bug (missing $p_k\ge0$
region-membership filter) before the final numbers were reported —
good practice; I spot-checked Theorem 10's formula against a small
literal example and found it consistent with prior certified use
elsewhere in the corpus. Neither finding is proposed for lemma
certification by the builder, correctly (both are point/family-specific
negative results tied to fixed numerical experiments, not general
theorems) — I agree and certify neither.

**No lemma certified this round for this slug** (per builder's own
correct assessment). The two findings meaningfully narrow the search
space (ruling out two concrete bypass mechanisms) without resolving the
Existence Theorem's $\Sigma$-shape residual.

**Verdict rationale:** genuine narrowing progress, honestly scoped,
`partial` correct.

## 5. `structured-randomization-upper-bound` — RETHINK

**Claims reviewed:** OddSum Floor Lemma ($\mathrm{OddSum}(M)\ge
\mathrm{sum}(M)/2$); Expectation Obstruction Theorem (any structured
randomization scheme with $n$-independent "mediocre-mass" $(\delta,
\varepsilon)$ fails to certify the upper bound once $n$ exceeds an
explicit threshold).

**Independent verification.** Both proofs are short, elementary, and
re-derived from scratch — correct. The Floor Lemma is a standard sorted
telescoping-pair argument. The Expectation Obstruction Theorem's algebra
($\mathbb E\ge\tfrac12+\varepsilon\delta$, compared against the certified
$c(n)=\tfrac12+\tfrac1{2(2^{n+1}-1)}$) checks out exactly, and the stated
threshold matches. Cross-checked against the round's two numerical
experiments (random-matching Anchor-Merge, random-index Subset-Tie):
both are explicitly diagnosed by the theorem as being far past the
threshold, matching the observed expectation failures quantitatively —
this is a real explanatory theorem, not post-hoc curve-fitting.

**Status assessment (per the round's specific question).** "Unsolved" is
correct, not an underclaim or overclaim: the Expectation Obstruction
Theorem is a genuine, general, correctly proved fact — but it is a
structural *impossibility* result about this approach's own mechanism
(expectation over a fixed discrete randomization), not a positive step
toward bounding $V(p)$ or constructing anything. Per CLAUDE.md, `partial`
requires "a correct reduction or a proven key lemma" toward the
problem's actual claim; this lemma instead rules out an entire class of
future attempts along this approach's stated line, which is valuable but
is not progress on the target inequality itself. I certified both
lemmas anyway (general-purpose, reusable, and directly useful to warn
off future rounds from re-discovering this) into
`lemmas/oddsum-floor-and-expectation-obstruction.md`.

**Verdict rationale for RETHINK (not just CHANGES REQUESTED):** the
approach's own file states the only way to evade the theorem is a
"concentrating" distribution requiring the same combinatorial
classification the deterministic approaches already attack — i.e. the
approach as framed (expectation over structured randomization) cannot
succeed without first solving the problem it was meant to avoid. This
matches CLAUDE.md's RETHINK criterion ("the approach can't work as set
up") rather than CHANGES REQUESTED (real progress, gap remains along the
same line). A future round should either find a genuinely different,
concentrating design (a substantively new framing, not a variant of
"randomize a discrete tie choice and average") or treat this direction
as exhausted.

## Lemmas certified this round

1. `lemmas/general-peeling-theorem-and-window-endpoint-closure.md` — GT($m$)
   for $m=0,1,2,3$ (scope-corrected: adds $\mathrm{sum}(D)<3\cdot2^{m-1}$,
   met at every actual use in the file) and its corollary, gap (a) of the
   shared window closed for $\ell=1,2,3,4$.
2. `lemmas/window-reduction-theorem-and-elementwise-monotonicity.md` —
   Elementwise Monotonicity Lemma, Transfer Monotonicity Theorem, Window
   Reduction Theorem (gap (b) fully closed, all $\ell\ge2$), plus the
   combined consequence that the shared window is fully closed at
   $\ell=1,2,3,4$.
3. `lemmas/integer-altsum-lower-bound-and-perfect-tie-characterization.md`
   — Integer-Alternating-Sum Lower Bound Lemma and the Perfect-Tie-Family
   Exact Characterization Theorem at $e_0$.
4. `lemmas/oddsum-floor-and-expectation-obstruction.md` — OddSum Floor
   Lemma and the Expectation Obstruction Theorem.

## `current.md` updated

- New "Approaches tried (round 12)" section (all 5 slugs, verdicts and
  key findings as above).
- "Current best" updated with a "Round 12 additions" summary paragraph
  and a corrected "Lower-bound direction" bullet reflecting the window's
  full closure at $\ell=1,2,3,4$ (previously stale, describing round 10's
  partial state).
- "Open" section updated to reflect the narrowed window gap (general
  $\ell\ge5$ only) and the three converging negative results at $e_0$.
- Status remains `partial` overall (headline claim — the general
  Existence Theorem / general lower bound for all $n$ — is not proved).

## Per-slug verdict summary

| Slug | Verdict | Status field |
|---|---|---|
| `self-similar-induction-on-n` | **CHANGES REQUESTED** | `partial` |
| `greedy-reduction-geometric` | **CHANGES REQUESTED** | `partial` |
| `lp-duality-split-polytope` | **CHANGES REQUESTED** | `partial` |
| `global-lp-vertex-sufficiency` | **CHANGES REQUESTED** | `partial` |
| `structured-randomization-upper-bound` | **RETHINK** | `unsolved` |

No `APPROVE` this round (problem not solved). All outcomes recorded via
`mcp__approach-ranker__record_outcome`.
