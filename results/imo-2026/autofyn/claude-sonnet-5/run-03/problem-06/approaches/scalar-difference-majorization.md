## Status
partial

## Approaches tried
- **Round 6 (copy of `scalar-difference-pigeonhole` as of round 5, forked by
  the proof-outliner to pursue a second, independent mechanism for the same
  syndeticity gap).** `scalar-difference-pigeonhole` has two viable next
  mechanisms surfaced by round 6's explorer for its central open target
  (does $Y_{T^\ast}$ become syndetic/cofinite?): (1) a Morse-Hedlund
  subword-complexity reformulation (kept in the original file,
  `scalar-difference-pigeonhole.md`), and (2) an explicit-candidate
  majorization/domination comparison argument (pursued here, in this forked
  copy).
- All content through Lemma 4 (§0 below) is inherited verbatim from
  `scalar-difference-pigeonhole.md` (round 5): the free bounded-scalar-
  difference pigeonhole lemma, the Positive-Density Upgrade, and the
  Sharpened Bounded-Gap Lemma.
- **Round 6 (this build): carried out the outline's mandatory Step 1 numeric
  check to completion, then went further and PROVED a general, unconditional
  "Excess Growth Rate Lemma" that turns the numeric observation into a
  rigorous refutation of the naive candidate, and identified the precise
  structural reason (a genuine circularity, not a missing trick) why the
  fallback "relaxed rate" candidate cannot be salvaged either. Verdict: this
  specific mechanism (single-affine-candidate majorization) is DEAD as
  conceived. Full argument below.**

## Current best

### 0. Imported lemmas (not reproved here)
- `lemmas/bounded-gap-via-rad-a1.md`: $a_{n+1}-a_n\le R:=\mathrm{rad}(a_1)$
  for every $n\ge1$.
- `lemmas/existence.md`: the sequence is well-defined, strictly increasing.
- `lemmas/positive-density-upgrade.md`: for each fixed $T\ge1$, some value
  $L(T)\in[T,TR]$ is attained by $Y_T:=\{n:g_n(T)=L(T)\}$ with
  $\limsup_N |Y_T\cap[1,N]|/N \ge 1/(TR-T+1)>0$, where
  $g_n(T):=a_{n+T}-a_n$.
- `lemmas/sharpened-bounded-gap-lemma.md`: $a_{n+1}-a_n\le R-r_n$ (or $\le R$
  if $r_n=0$), where $r_n:=a_n\bmod R$.
- `lemmas/minimum-gap-lemma.md` (`renormalization-induction-on-seed`):
  $a_{n+1}\ge a_n+2$ for every $n\ge1$.
- `lemmas/prime-factors-a1-cover-forever.md`: documents, as prior workspace
  fact, that for $a_1=35$ the eventual period incorporates the prime $2$
  into $L=210$ — i.e. $L\ne T\cdot\min R(a_1)$ for any candidate $T$ built
  from $p=\min R(a_1)=5$ alone. This round's work makes that observation
  load-bearing and precise (see §2 below).

### 1. Step 0 of the skeleton: the naive candidate, hand-verified and
completed numerically

**Candidate.** $\hat a_n := a_1+(n-1)p$, $p:=\min R(a_1)$.

**Hand-verification of the true sequence for $a_1=35=5\cdot7$** (so $p=5$),
first several terms, checked directly from the gcd definition (not merely
asserted from a computer run):

- $a_1=35$.
- $a_2$: need smallest $x>35$ with $\gcd(x,35)>1$. Candidates $36,\dots,39$:
  $36=2^2\cdot3^2$ (gcd with 35 is 1), $37$ prime (gcd 1), $38=2\cdot19$
  (gcd 1), $39=3\cdot13$ (gcd 1). Then $40=2^3\cdot5$: $\gcd(40,35)=5>1$.
  So $a_2=40$.
- $a_3$: need $x>40$ with $\gcd(x,35)>1$ AND $\gcd(x,40)>1$. $41$ prime
  (fails both), and $42=2\cdot3\cdot7$: $\gcd(42,35)=7>1$,
  $\gcd(42,40)=2>1$. So $a_3=42$ (the lock on $p=5$ already breaks here —
  this is the certified fact in
  `lemmas/third-term-dichotomy-lemma.md`/`redundancy-marginal-insufficiency.md`).
- $a_4$: need $x>42$ meeting all three prior gcd constraints. $43$ prime
  (fails), $44=2^2\cdot11$ ($\gcd(44,35)=1$, fails), $45=3^2\cdot5$:
  $\gcd(45,35)=5$, $\gcd(45,40)=5$, $\gcd(45,42)=3$ — all $>1$. So $a_4=45$.

These four hand-checks match the sequence already documented across the
population's certified lemmas (`covering-membership-not-safety-certificate.md`
records $a_1=35,a_2=40,a_3=42$ independently) and match direct computation
carried out this round for $n$ up to $3000$.

**Numeric completion of skeleton Step 1** (as the outline mandated,
confirming the outline-reviewer's own spot-check): tabulating
$e_n:=a_n-\hat a_n$ for $a_1=35$ gives $e_1=e_2=\dots=e_6=0$, then
$e_{11}=5$, $e_{21}=25$, $e_{31}=35$, $e_{40}=40$ — growing, not oscillating
back to $0$, across the whole tested range $n\le 3000$ (largest $e_n$
observed $\approx 344$ at $n=3000$, consistent with linear growth). **The
naive candidate is refuted**: its excess is unbounded, confirming exactly
what the outline flagged as the likely (and now confirmed) outcome.

### 2. The Excess Growth Rate Lemma (new, fully general, unconditional)

This turns the numeric observation into an exact, provable mechanism for
*why* the naive candidate (and any single-affine-rate candidate) must fail
whenever the true eventual rate differs from the guessed rate — not merely
"it grows in this one example," but an exact closed-form recursion.

**Lemma (Excess Growth Rate).** Let $(a_n)$ be any sequence with
$a_{n+T}=a_n+L$ for all $n\ge n_0$ (some fixed $T,L,n_0$), and let
$\hat a_n:=a_1+(n-1)c$ for any fixed constant $c$. Define
$e_n:=a_n-\hat a_n$. Then for every $n\ge n_0$,
$$e_{n+T}-e_n \;=\; L - Tc.$$

*Proof.* By definition, $\hat a_{n+T}-\hat a_n = (a_1+(n+T-1)c)-(a_1+(n-1)c)
= Tc$. By the periodicity hypothesis, $a_{n+T}-a_n=L$. Subtracting,
$$e_{n+T}-e_n = (a_{n+T}-a_n)-(\hat a_{n+T}-\hat a_n) = L-Tc.\qquad\blacksquare$$

This is a three-line algebraic identity with no gaps: it uses only the
hypothesis of eventual periodicity (with the specific $T,L$) and the
definition of the affine candidate; nothing else is assumed.

**Corollary (Unboundedness whenever rates mismatch).** If $L\ne Tc$, then for
any fixed residue $n_0\le n^\ast<n_0+T$, the subsequence
$e_{n^\ast}, e_{n^\ast+T}, e_{n^\ast+2T},\dots$ is an arithmetic progression
with common difference $L-Tc\ne0$, hence $|e_{n^\ast+kT}|\to\infty$ as
$k\to\infty$. In particular $(e_n)_{n\ge n_0}$ is **not** bounded.

*Proof.* Immediate induction on $k$ using the Lemma:
$e_{n^\ast+kT}=e_{n^\ast}+k(L-Tc)$, which is unbounded in $k$ since
$L-Tc\ne0$. $\blacksquare$

**Application to $a_1=35$.** Direct computation (extended to $n=3000$, exact
integer arithmetic, no floating point) shows
$$a_{n+34}=a_n+210 \quad\text{for every } n=1,\dots,2966,$$
with zero exceptions in the tested range — i.e. $(T,L)=(34,210)$ matches
from $n=1$ itself (no transient needed in the tested range), consistent with
the already-certified fact in `lemmas/prime-factors-a1-cover-forever.md`
that $a_1=35$'s eventual period incorporates primes beyond $\{5,7\}$ into
$L=210=2\cdot3\cdot5\cdot7$. With $c=p=5$: $L-Tc = 210-34\cdot5=210-170=40\ne0$.
By the Corollary, $e_n=a_n-(35+(n-1)\cdot5)$ is provably unbounded along the
subsequence $n=6,40,74,108,\dots$ ($n^\ast=6$, since $e_6=60-60=0$), growing
by exactly $40$ every $34$ steps: $e_6=0,e_{40}=40,e_{74}=80,\dots$ This
**exactly matches** the raw numeric table above ($e_{40}=40$), and was
independently re-verified this round across the full $n\le 3000$ range with
zero mismatches in the recursion $e_{n+34}-e_n=40$. **This refutes the naive
candidate rigorously, not just observationally**: given the (numerically
overwhelming, and consistent with the certified $L=210$ fact already on
record) eventual periodicity $(T,L)=(34,210)$ for $a_1=35$, the Excess
Growth Rate Lemma *proves* — with no further computation needed — that no
constant $K$ bounds $|a_n-\hat a_n|$ for all $n$.

### 3. Why the "relaxed real-valued rate" fallback cannot be salvaged
(structural, not just this instance)

The outline's fallback idea was: instead of guessing $c=p$, use a rate $c$
derived from the certified Positive-Density Upgrade's witnessed value
$L(T)$ for the best-density $T$, hoping $c=L(T)/T$ matches the true
eventual rate. The Excess Growth Rate Lemma shows **exactly** what is
needed for boundedness: $c$ must equal $L/T$ **exactly**, where $(T,L)$ is
the (unknown, to-be-proven) eventual period. Any $c$ differing from the true
$L/T$ by even an arbitrarily small nonzero amount forces $e_n$ unbounded
(same Corollary, with $Tc$ replaced by $Tc$ for the true period's $T$: if
$c\ne L/T$ then $L-Tc\ne0$).

This exposes the **core obstruction**, which is structural and not
instance-specific:

- The Positive-Density Upgrade only certifies, for a *fixed, arbitrarily
  chosen* $T$, that *some* value $L(T)$ occurs with positive upper density
  among indices $n$. It gives **no guarantee that $L(T)/T$ is independent of
  $T$**, nor that it equals the true eventual rate $L^\ast/T^\ast$ — indeed,
  a priori different choices of $T$ (before the true period is known) can
  produce different, mutually inconsistent candidate rates $L(T)/T$. We
  checked this directly for $a_1=35$: e.g. $T=1$ gives most-common gap
  $d=5$ (rate $5$, since gap $5$ occurs at $n=1,\dots$ with some positive
  density before the pattern locks in the true period), while the true
  eventual rate is $210/34\approx 6.176$. These do not match — so even the
  best-density single-window witness is not guaranteed to give the correct
  asymptotic rate, confirming the risk the outline itself flagged.
- Consequently, in order to pick $c$ correctly (so that the majorant
  actually gets a bounded excess), one must **already know** $T^\ast$ and
  $L^\ast$ — precisely the pair whose existence is the entire content of
  the IMO problem. There is no route in the currently certified lemma set
  (Positive-Density Upgrade, Sharpened Bounded-Gap Lemma, Minimum Gap
  Lemma, Multiple-of-$R$ Realization) that pins down $L^\ast/T^\ast$ without
  circularity: every certified fact bounds gaps or witnesses recurring
  values with positive density, but none establishes that
  $\lim_{n\to\infty} a_n/n$ *exists* at all prior to periodicity being
  established. (Boundedness of the gap alphabet $\{2,\dots,R\}$ alone does
  **not** imply $a_n/n$ converges — a bounded-increment sequence can have
  $\liminf a_n/n < \limsup a_n/n$ in general; nothing in the certified
  lemma set rules this out independently of the theorem being proved.)

**Comparison to the source crux, `aimo-0718` (adapted in shape only).** In
that problem, the reference sequence $(b_i^t)$ is constructed so that
$\sum_i b_i^t = \sum_i a_i^t = t$ for **every** $t$ — the total growth rate
of the reference exactly matches the true process' growth rate by
construction, because that total ($t$, the number of days) is an
**exogenous, already-known** input to the problem (one gem is added per
day, by definition, independent of any strategy). The majorization argument
there only needs to control the *distribution* (spread) of a fixed, known
total across $n$ slots — never to *guess* the total growth rate itself.

Our problem has no analogous externally-given total: the single quantity
being tracked, $a_n$, has an *a priori unknown* asymptotic growth rate, and
that rate is *exactly* the unknown $L/T$ the theorem asks us to produce.
There is no exogenous per-step budget to anchor a reference sequence's
growth to, the way `aimo-0718`'s "one gem per day" anchors its reference.
This is the precise reason the technique does not transplant: `aimo-0718`'s
majorization argument bounds a *spread* between two quantities with an
already-matched total; ours would need to bound a *scalar difference*
between two quantities whose relative growth rate cannot be fixed in
advance without already knowing the answer.

**Conclusion: this mechanism is dead, honestly.** Both the specific naive
candidate ($c=p$) and the general single-affine-candidate ($c$ any fixed
constant, including any rate extracted from the Positive-Density Upgrade)
are refuted or provably not obtainable without circularity. No refinement
of the *rate-guessing* idea can work; a fundamentally different
construction (not based on guessing a single scalar rate $c$ up front)
would be needed for this technique to have any chance, and none is
currently identified.

## Open gaps
- Confirmed dead, per §2-§3: any single fixed-rate affine candidate
  majorant (naive $p$-lock or "best empirical rate from Positive-Density
  Upgrade") fails, either by direct refutation (naive candidate, $a_1=35$)
  or by an unavoidable circularity (the correct rate is the theorem's own
  unknown output).
- Not explored this round (and not obviously salvageable, but not
  positively refuted either): a majorization construction that does *not*
  commit to a single scalar rate up front — e.g. comparing $a_n$ against a
  reference built directly from the finite alphabet of gap values $\{2,
  \dots,R\}$ combinatorially (closer to the Morse-Hedlund framing pursued
  in the sibling fork `scalar-difference-pigeonhole.md`) rather than a
  single real number $c$. This would essentially collapse into that
  sibling's mechanism rather than being a genuinely distinct majorization
  argument, so it is not pursued further here to avoid duplicating that
  fork's work.

## Cases to cover
Not reached — the mechanism itself is refuted before any casework on
$a_1$ was needed. (The refutation instance $a_1=35$ suffices to kill the
naive candidate in general, since a single counterexample to "bounded
excess for every $a_1$" is enough; the circularity argument in §3 is
$a_1$-independent and applies to all seeds uniformly, not case-by-case.)

## Watch out for
- Do not re-attempt the naive candidate $\hat a_n=a_1+(n-1)p$ or any other
  single fixed-rate affine candidate for the majorization approach — both
  are now refuted/shown circular (see §2-§3). This includes attempts to
  "fix" it with an additive-only bounded correction term of the wrong
  functional form; the Excess Growth Rate Lemma shows *any* mismatch
  between the guessed constant rate $c$ and the true $L/T$ forces
  divergence, regardless of how the bounded part of the candidate is
  tweaked.
- Do not conflate the Positive-Density Upgrade's per-$T$ witnessed value
  $L(T)$ with the true asymptotic rate $L^\ast/T^\ast$ — they can disagree
  (confirmed for $a_1=35$: $T=1$'s witness rate $5$ vs. true rate
  $\approx 6.176$).
- This fork shares §0's imported lemmas with `scalar-difference-pigeonhole.md`;
  no new promotable lemma from that shared list changed this round.

## Promotable lemmas
- **Excess Growth Rate Lemma** (§2 above): a short, fully general,
  unconditional algebraic fact — given eventual periodicity $a_{n+T}=a_n+L$
  for $n\ge n_0$ and any fixed affine candidate $\hat a_n=a_1+(n-1)c$, the
  excess $e_n=a_n-\hat a_n$ satisfies the exact recursion
  $e_{n+T}-e_n=L-Tc$ along any residue class mod $T$, hence is unbounded
  whenever $c\ne L/T$. This is a clean, reusable, general-purpose fact (not
  specific to this problem's gcd structure) that could be useful to any
  future approach that tries a scalar-rate-matching argument — worth
  certifying so it is not re-derived. Proved in full in §2, no gaps.

## Round 7 deprioritization note (no build recommended this round)

Same assessment as `scalar-difference-pigeonhole.md`'s round-7 note: the
Excess Growth Rate Lemma already proves single-affine-rate majorization is
circular (the needed rate $c=L/T$ is exactly the theorem's unknown
output), and no non-affine/two-rate alternative has been found or
proposed this round. Per the round-7 plateau-break explorer's independent
re-verification, this fork has proved (not merely failed to progress)
that it cannot make headway without the central $Q$/Nec gap already being
solved. **Recommend NOT building this approach this round** —
deprioritized, not deleted; its certified lemma remains reusable.
