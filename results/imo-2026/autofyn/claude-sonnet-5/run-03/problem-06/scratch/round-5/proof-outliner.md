## imo-2026-06

**Plateau diagnosis.** `state-compactness-pigeonhole`, `active-set-stabilization`,
and `jacobsthal-covering-bound` are all variants of the SAME framing (construct
a finite prime set $Q$ that is self-sufficient for the whole sequence) and have
shared one wall — the central existence gap for such a $Q$ — for 3+ rounds. Per
CLAUDE.md's plateau-break rule, this round advances the two strongest members of
that framing (real forward progress, sharper reformulations), REVISES
`renormalization-induction-on-seed` (its core notion "locked forever" is now
proven to be the wrong target, diagnosed by the round-5 explorer), and OPENS TWO
genuinely different framings that touch none of the $Q$/Good$_Q$ machinery:
a scalar-arithmetic pigeonhole (no primes at all) and a monovariant/well-founded
descent architecture (adapted from crux `aimo-0678`). `jacobsthal-covering-bound`,
`bounded-link-invariant`, and `growth-rate-contradiction` are not nominated this
round — each has explicitly reported no remaining untried mechanism (see their
files); re-running them without a new idea would waste a build slot.

---

state-compactness-pigeonhole: advance
Target: the problem's full claim — every valid greedy sequence $(a_n)$ is
eventually periodic with a shift $(T,L)$: $a_{n+T}=a_n+L$ for all large $n$.
Technique: construct a finite self-sufficient prime set $Q$ (equivalently, via
the certified Reduction Lemma, show $\mathrm{Good}_Q(a_n)$ for every $n\ge1$),
then finish via the certified Transient-free finishing theorem.
Skeleton:
  1. Reduce the Unified Central Claim to a hitting-set problem: $Q$ works iff
     $Q$ hits every $W(i,j):=R(a_i)\cap R(a_j)$ — certified `hitting-set-lemma.md`.
  2. Combine with `nec-necessity.md`: any valid $Q$ must contain
     $Q_{\min}=\mathrm{Nec}\cup R(a_1)$; test whether $Q_{\min}$ itself is
     self-sufficient (hits every $W(i,j)$).
  3. Attack the still-open direction: for each pair $(i,j)$ with
     $|W(i,j)\cap Q_{\min}|=0$ hypothetically, derive a contradiction from the
     already-certified `bounded-radical-special-cases.md` (index-1 and
     adjacent pairs are always hit for free) plus a NEW counting argument on
     how many "far apart" pairs can simultaneously avoid $Q_{\min}$ — use the
     `nec-finiteness` explorer's opening 3 (redundant-covering density): show
     that once each prime $p\in Q_{\min}$'s recruiting index set has "enough"
     members, every later pair is automatically hit with multiplicity $\ge2$,
     ruling out any future singleton-intersection (Nec-growing) pair.
  4. If self-sufficiency of $Q_{\min}$ is established, finish via
     `transient-free-finishing-theorem.md` (no further gap).
Key lemmas:
  - Hitting-Set Lemma (certified) — because self-sufficiency is defined
    exactly as "$Q$ meets every pairwise intersection set."
  - Nec-Necessity Lemma (certified) — because a prime witnessing a singleton
    pairwise intersection must lie in every valid $Q$, giving the unique
    minimal candidate.
  - NEW target lemma (open): "redundant-covering density" — because once a
    prime $p$'s divisibility-index set among the first $n$ terms is dense
    enough (bounded gaps between consecutive multiples), every future pair of
    terms sharing $p$ automatically also shares a second element of
    $Q_{\min}$, so no NEW singleton pair (hence no new Nec element) can ever
    form beyond some finite index.
Open gaps: existence of $Q_{\min}$'s self-sufficiency (equivalently
finiteness+eventual-redundancy of Nec) — step 3's redundant-covering density
lemma is the concrete new target, currently unproven.
Cases to cover: none beyond the general pair $(i,j)$ argument.
Watch out for: `chain-transitivity-obstruction.md` already rules out proving
self-sufficiency by chaining adjacent pairs transitively — the redundancy
argument in step 3 must work pair-by-pair directly (via index density), not
via transitive chaining, or it silently reproduces the killed mechanism.

---

active-set-stabilization: advance
Target: same as above — full eventual periodicity.
Technique: same $Q_{\min}$/Nec machinery, attacked via a direct combinatorial
count on witness-pair indices rather than the hitting-set reformulation.
Skeleton:
  1. Import `nec-necessity.md`: $\mathrm{Nec}\subseteq Q$ necessary; work with
     the explicit candidate $Q_{\min}=\mathrm{Nec}\cup R(a_1)$.
  2. NEW (this round's target, from `nec-finiteness` explorer opening 1/2):
     define, for each term $a_n$, its **redundancy count** against the
     "generic" class of $Q_{\min}$-Good terms: $\rho(n):=|R(a_n)\cap Q_{\min}|$.
     Show $\rho(n)$ is eventually $\ge2$ for all sufficiently large $n$ — i.e.
     beyond some $N^\ast$, every term carries at least TWO primes of
     $Q_{\min}$, so no future pair of terms can have a singleton intersection
     (hence Nec cannot grow past $N^\ast$, proving Nec finite).
  3. Prove $N^\ast$ exists via an explicit induction that tracks, for each
     prime $p\in Q_{\min}$, the density of its divisibility index set among
     the first $n$ terms (using `bounded-gap-via-rad-a1.md`'s bounded-gap
     structure to lower-bound how often each fixed prime must recur).
  4. Once Nec finite + $Q_{\min}$ self-sufficient (redundancy $\ge2$
     everywhere large enough, plus the finite prefix checked directly), reuse
     the certified finish (shared with `state-compactness-pigeonhole`).
Key lemmas:
  - Nec-Necessity Lemma (certified).
  - NEW: Redundancy Growth Lemma (open) — because if a prime's divisibility
    index set among the first $n$ terms has bounded gaps (a consequence of
    the bounded-gap lemma applied to multiples of that prime specifically),
    then any two terms both divisible by TWO fixed primes of $Q_{\min}$
    automatically share $\ge2$ elements, blocking new Nec growth.
Open gaps: the Redundancy Growth Lemma itself — no proof yet, only numerical
support (Nec stabilizes early in every tested seed, even the slow $a_1=375$
case recruiting prime 7 only at witness index 26).
Cases to cover: the argument must separately handle "small" primes already in
$R(a_1)$ (which recur with bounded gap by the base bounded-gap lemma) versus
"recruited" primes outside $R(a_1)$ (e.g. 7 for $a_1=375$, 103 for
$a_1=194287$) which have NO a priori bound on their first recurrence gap —
this split is exactly where the $a_1=375$ (recruitment delayed to witness
index 26) and $a_1=194287$ (recruited prime 103 exceeds every prime factor of
$a_1$) counterexamples bite; do not assume a uniform bound across both cases.
Watch out for: any conjectured closed-form bound on $|\mathrm{Nec}|$ or the
recruitment index in terms of $\omega(a_1)$ or $\mathrm{rad}(a_1)$ alone is
REFUTED by $a_1=375$ (7 recruited at witness index 26 despite
$\mathrm{rad}(375)=15,\omega(375)=2$) — do not propose such a bound.

---

renormalization-induction-on-seed: revise (core notion redefined)
Target: same — full eventual periodicity, via strong induction on
$\omega(a_1)$ with an explicit smaller-instance reduction (architecturally
distinct from the $Q$-construction framing above).
Technique: induction on $\omega(a_1)$, but with the induction's core notion
of "locked prime" REPLACED — the old notion ("$p$ divides every term from
some index on") is now diagnosed, via fresh computation on $a_1=35$'s full
eventual period ($L=210=2\cdot3\cdot5\cdot7$, found only after running
$N=20000$ terms), as PROVABLY FALSE in general: $p=5$ stops dividing every
term after index 2, yet $5$ remains a permanent factor of the eventual period
sum $L$ via periodic (not universal) recurrence. Every prior attempt at this
approach's inductive step targeted a false statement.
Skeleton (revised, persisted in the approach file §"Round 5 revision"):
  1. Keep the certified free base case (§3, prime-power seeds: $T=1,L=p$)
     and the certified Third-Term Dichotomy Lemma (§4.2, exact closed-form
     for $a_3$ of any squarefree two-prime seed) — both unconditional,
     unaffected by the diagnosis.
  2. Redefine: a prime $p$ is **periodically active** if there exist $n_0,M$
     and $\emptyset\ne S_p\subseteq\mathbb Z/M\mathbb Z$ with $p\mid a_n \iff
     (n\bmod M)\in S_p$ for all $n\ge n_0$ (the old notion is the special
     case $M=1$). This is the *correct* necessary property (if the sequence
     is eventually periodic with shift $T$, every prime dividing $L$
     automatically has this property with $M=T$, by
     `periodicity-of-residue-class-union.md`), unlike the old notion.
  3. New inductive target: show $p:=\min R(a_1)$ becomes periodically active
     for SOME finite $M$, independent of already knowing the global period.
  4. If 3 succeeds, reduce the remaining "positions not covered by $p$'s
     residue set $S_p$" to a covering problem on the finite group
     $\mathbb Z/M\mathbb Z$ — a genuinely smaller (finite, not infinite)
     sub-instance, to be covered by the remaining primes.
Key lemmas:
  - Prime-power base case (certified, §3).
  - Third-Term Dichotomy Lemma (certified, §4.2).
  - NEW target: periodic-activity of $\min R(a_1)$ (open) — because if
    eventual global periodicity holds, this property is forced with $M=T$;
    proving it directly (without first knowing $T$) is the honest new gap.
Open gaps: step 3 (periodic activity of a single fixed prime, established
independently of the global period) is completely open; step 4's covering
reduction has an acknowledged circularity risk (the modulus $M$ must not be
chosen post hoc from already-known period data) — flagged explicitly in the
approach file, not glossed over.
Cases to cover: none new beyond the already-solved base case and third-term
formula; the general step is stated uniformly for any $\omega(a_1)\ge2$.
Watch out for: do NOT let any downstream argument silently substitute back
the old $M=1$ notion (e.g. "the complement of $S_p$ is empty") — this
reproduces the refuted mechanism and the two already-certified negative
results (`bounded-lookahead-insufficiency.md`,
`windowed-epsilon-automaton-failure.md`) apply immediately.

---

scalar-difference-pigeonhole: new
Target: same — full eventual periodicity $a_{n+T}=a_n+L$ for large $n$, some
$T,L$.
Technique: pigeonhole on a bare scalar arithmetic difference (no prime-set
bookkeeping at all), then an ISL-2015-N6-style extension argument. Genuinely
different framing: works entirely with integer values of $(a_n)$, never
constructs a prime set $Q$ or type/state object.
Skeleton:
  1. For fixed $T\ge1$, define $g_n(T):=a_{n+T}-a_n\in[T,TR]$
     ($R=\mathrm{rad}(a_1)$), by telescoping the certified
     `bounded-gap-via-rad-a1.md`.
  2. Pigeonhole (finite range, infinite domain): some value $L(T)$ is
     attained by an infinite index set $Y_T$ — free, unconditional, proved
     in full in the approach file.
  3. OPEN central step: show that for some $T=T^\ast$, $Y_{T^\ast}$ is not
     just infinite but has BOUNDED GAPS (syndetic) — candidate mechanism A.
     If true, combined with `periodicity-of-residue-class-union.md`'s exact
     finite-alphabet finish, this closes the theorem with zero reference to
     $Q$ or $\mathrm{Nec}$.
  4. Fallback candidate mechanism B: adapt the ISL 2015 N6 sandwich-divisibility
     trick (from `aimo-0680`), but this requires first deriving a substitute
     divisibility fact specific to this recurrence (ISL's precondition
     $d\mid f^d(m)-m$ does not hold here and has no known substitute yet) —
     explicitly flagged as harder, attempt only if mechanism A stalls.
Key lemmas:
  - Bounded scalar difference + pigeonhole (proved in full, free): because
    each of the $T$ individual gaps is bounded by $R$, their sum over a fixed
    window is bounded, giving a finite alphabet for pigeonhole with no
    reference to primes.
  - NEW target (open): syndeticity of $Y_{T^\ast}$ — because eventual
    periodicity IS exactly "$Y_{T^\ast}$ is cofinite," so proving bounded
    gaps (a weaker, more tractable intermediate target) is a natural
    stepping stone that does not presuppose the answer.
Open gaps: mechanism A (syndeticity) is entirely open; mechanism B requires
an undeveloped substitute divisibility fact. Also open: which $T$ to use is
not handed to us a priori.
Cases to cover: none — the construction is uniform in $T$.
Watch out for: do NOT re-attempt "two consecutive matching indices propagate
forever" — proven false by direct computation ($a_1=99$, $T=1$, breaks at
$n=5$); any extension argument needs a genuinely global ingredient.

---

frozen-invariant-monovariant: new
Target: same — full eventual periodicity.
Technique: well-founded descent (monovariant) on a scalar quantity tied to an
evolving empirical invariant, adapted from crux `aimo-0678`'s coupled-recurrence
proof shape (a min-of-a-set statistic frozen against an auxiliary quantity,
shown non-increasing, hence eventually constant by well-ordering). Genuinely
different proof architecture: neither prime-set construction nor seed
induction, but descent on a single integer sequence.
Skeleton:
  1. Free cheap lemma: $U_n:=\{p\in R(a_1): p\mid a_i\ \forall i\le n\}$ is
     non-increasing in $n$ (a subset chain of the finite set $R(a_1)$), hence
     stabilizes at $U_\infty$ for $n\ge n_0$ — proved in full, unconditional,
     no circularity.
  2. Diagnosis (imported from the renormalization revision above): $U_\infty$
     alone is known insufficient ($a_1=35$'s prime 5 drops out of $U_n$ yet
     remains a permanent factor of the eventual period $L=210$ via periodic
     recurrence) — so §1 alone does not finish the problem.
  3. OPEN central construction: build a residue-aware analogue of
     `aimo-0678`'s $w_n=\min\{m\ge a_n: m\nmid s_n\}$, tracking an
     empirical divisibility pattern $D_n(p,M)$ per prime $p$ and trial
     modulus $M$, and attempt to show a suitably-defined $w_n(M)$ is
     eventually non-increasing for the correct $M$ — modeled on but NOT
     transplanted from `aimo-0678` (no companion sequence or frozen sum
     exists in our problem; must be built from scratch).
  4. If 3 succeeds and yields a well-defined, eventually-constant
     monovariant, show the stabilized value certifies exact eventual
     periodicity via `periodicity-of-residue-class-union.md`.
Key lemmas:
  - Universally-dividing prime set stabilizes (proved in full, free) —
    because it is a non-increasing chain of subsets of the finite set
    $R(a_1)$.
  - NEW target (open, not yet even rigorously specified): the residue-aware
    monovariant $w_n(M)$ — because eventual periodicity forces every
    relevant prime's divisibility pattern to become an exact periodic
    residue-class union (matches `periodicity-of-residue-class-union.md`'s
    conclusion shape), so a monovariant detecting "pattern has stabilized"
    is the natural non-circular target, PROVIDED $M$ is not chosen post hoc.
Open gaps: step 3's construction needs a precise, checkable definition before
any proof is attempted (currently only a sketch); monotonicity (the hardest
step) is completely untouched; the circularity risk in choosing $M$ must be
resolved via one of the two routes flagged in the approach file (uniform
argument over a fixed a-priori range of $M\le\mathrm{lcm}(1,\dots,R)$, or an
$M$-independent reformulation closer to `aimo-0678`'s original single-frozen-
sum shape).
Cases to cover: none yet — no case split has been reached.
Watch out for: `windowed-epsilon-automaton-failure.md` already proves no
bounded window of recent history determines the exceptional-step indicator —
any "boring vs. exceptional" classifier used inside step 3's monotonicity
proof must NOT reduce to a bounded-window statistic, or it inherits that
certified negative result immediately. Also do not let $M$ be picked from
already-observed periodicity data (reproduces the population's existing
circularity risk under new notation).

---

**Build-set recommendation:** advance `state-compactness-pigeonhole` and
`active-set-stabilization` (both have live, concretely stated next targets on
the shared framing); build the revised `renormalization-induction-on-seed`
(new, non-circular target replacing the refuted one); build both new
approaches `scalar-difference-pigeonhole` and `frozen-invariant-monovariant`
to seed genuinely far framings per the plateau-break rule. This gives the
outline-reviewer 5 candidates spanning 4 distinct architectures (global-$Q$
construction ×2, seed induction ×1 revised, scalar pigeonhole ×1 new,
monovariant descent ×1 new).
