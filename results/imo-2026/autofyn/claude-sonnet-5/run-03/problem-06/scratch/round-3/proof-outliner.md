## imo-2026-06

Context: round 1-2 population converged on two open gaps (Hypothesis SS —
self-sufficiency of a finite active prime set $Q$/$L$ — and prefix
extension to $n=1$). Round 2's two candidate termination mechanisms for
Hypothesis SS (`g(Q)`-threshold, prime-size threshold) are BOTH proven
unsound — a 2-round plateau on the "fix $Q$ first, pigeonhole/cover"
framing. Round 3 explorers supply three genuinely new ingredients: (1) an
unconditional bounded-adjacent-link fact confining `gcd(a_n,a_{n+1})` to a
fixed finite set for every $n$ with no transient (explorer
minimality-recruitment); (2) confirmation that sieve/window and orbit-square
transfer framings are dead, plus a sharp Diophantine-proximity
counterexample ($a_1=33$ vs $a_1=99$) showing no closed form for $L(a_1)$
exists (explorer alt-framing); (3) a new unconditional Self-Type-
Compatibility Lemma showing $n=1$ is never itself an obstruction to prefix
extension, motivating a UNIFIED target "Hypothesis SS with $n^*=1$" instead
of two separate gaps (explorer prefix-extension).

All revisions below are persisted directly into
`results/imo-2026-06/approaches/*.md` (verified by re-reading after edit,
per round-2's outline-reviewer correction).

---

active-set-stabilization: revise
Target: the problem's actual claim, via the UNIFIED reformulation —
there exists a finite $Q\supseteq R(a_1)$ such that for **every** $n\ge1$,
$a_{n+1}=\min\{m>a_n:\mathrm{Good}_Q(m)\}$ (no separate "extend to $n=1$"
step).
Technique: Self-Type-Compatibility propagation (new, non-pigeonhole) +
Lemma M (minimal-type reduction, certified) to localize failure points, plus
a candidate "divisible + bounded $\Rightarrow$ zero" finishing move adapted
from crux `aimo-0680` on a discrepancy sequence $e_n:=a_n-b_n$ (true vs.
stabilized-rule sequence).
Skeleton:
  1. Certify Self-Type-Compatibility Lemma (pairwise-non-coprimality +
     containment) — proves $\mathrm{Good}_Q(a_1)$ unconditionally for every
     valid $Q$, and its propagation corollary (an index with
     $R(a_i)\subseteq Q$ automatically witnesses every other index).
  2. Apply Lemma M: acceptance depends only on $\subseteq$-minimal types;
     localize possible failures to "outside-prime" indices with
     $R(a_i)\not\subseteq Q$ whose type is minimal and unwitnessed elsewhere.
  3. Attempt the aimo-0680-style finish: show $L\mid e_n$ (via certified
     Lemma T, translation compatibility) while $|e_n|$ is bounded (via
     bounded-gap-via-rad-a1), forcing $e_n=0$ for all $n$.
Key lemmas (claim + mechanism):
  - Self-Type-Compatibility Lemma — because pairwise-non-coprimality forces
    a shared prime, which lies in $Q$ whenever the witnessing index's full
    factorization does.
  - Lemma M (already certified) — poset argument: meeting all types reduces
    to meeting the minimal ones.
  - (Attempted, open) $L\mid e_n$ — the concrete new divisibility claim
    needed to import the aimo-0680 finishing pattern; not yet derived.
Open gaps: Hypothesis SS's core self-sufficiency (which $Q$, and why it's
finite) is deferred to jacobsthal-covering-bound's revision by explicit
division of labor; the divisibility claim in step 3 is unproven and may be
false.
Cases to cover: none beyond the single unified statement.
Watch out for: do not resurrect the certified Monotonicity Obstruction
Lemma's refuted family (state-recurrence pigeonhole from $n=1$) — this
revision's mechanism must stay non-recurrence (propagation/divisibility).

state-compactness-pigeonhole: advance (with new mechanism)
Target: same unified statement as above, attacked from the complement-set/
Proposition-B framework instead.
Technique: Self-Type-Compatibility Lemma (shared ingredient, certify once)
applied inside Proposition B's static characterization, aiming to push the
transient index $n^*$ in $(\ast)$ (the tail-equals-$Q$-Good-set identity,
already proved conditionally in this file) down to $a_1$ directly, then
finish with the already-certified Lemma P (exact periodicity of a
residue-class-union listing) in one shot — collapsing central + prefix gaps
together, via a DIFFERENT route from active-set-stabilization's discrepancy-
sequence argument.
Skeleton:
  1. Certify Self-Type-Compatibility Lemma (coordinate so it's certified
     only once across the two files using it).
  2. Re-derive $(\ast)$ with $n^*=1$: use Proposition B + propagation to show
     $\mathrm{Good}$ and $\mathrm{Good}_Q$ agree on realized constraints
     except at outside-prime indices; check/bound these one at a time using
     the numerical worked examples ($a_1=35$'s indices $14,17,22,\dots$).
  3. If $(\ast)$ holds with $n^*=1$: apply certified Lemma P with $c=a_1$ to
     get exact periodicity for all $n\ge1$ directly.
Key lemmas: Self-Type-Compatibility Lemma (as above); Proposition B and
Lemma P (already certified, reused as-is).
Open gaps: which finite $Q$ makes Hypothesis SS true at all (shared central
gap, deferred); whether outside-prime indices are always harmless for
$(\ast)$ with $n^*=1$ — open, untried in this exact form.
Cases to cover: none beyond existing.
Watch out for: keep independent from active-set-stabilization's mechanism —
both use the shared lemma but diverge in how they close the remaining gap;
don't let one subsume the other prematurely.

jacobsthal-covering-bound: revise
Target: same problem statement, attacking Hypothesis SS's central
self-sufficiency gap via a genuinely new mechanism (both prior mechanisms —
$g(Q)$-threshold and prime-size threshold — are proven unsound; this is not
a third variant of "find a threshold on $Q$").
Technique: bounded-adjacent-link invariant (new, unconditional) to split
$Q=\Lambda\cup(Q\setminus\Lambda)$, where $\Lambda$ (all-time adjacent-link
primes) is proved finite by a genuinely obstruction-free pigeonhole (fixed
universe $\{p\le R\}$, unlike $Q$'s a priori unbounded universe), reducing
the central gap to the strictly narrower claim "$Q\setminus\Lambda$ is
finite."
Skeleton:
  1. Certify the Adjacent-Link Lemma: $\gcd(a_n,a_{n+1})\mid(a_{n+1}-a_n)\le
     R=\mathrm{rad}(a_1)$ for every $n\ge1$ (elementary $\gcd(x,x+d)\mid d$
     + certified bounded-gap lemma).
  2. Certify $\Lambda$-stabilization: $\Lambda_n$ (link primes seen by index
     $n$) is monotone in the FIXED finite set $\{p\le R\}$, so it stabilizes
     after $\le\pi(R)$ growth steps — a genuine, obstruction-free pigeonhole
     (unlike every previous attempt to pigeonhole $Q$ or $S$ directly, whose
     universe is a priori unbounded).
  3. Note explicitly (refuted, do not retry): $\Lambda\ne\mathrm{rad}(L)$ in
     general ($a_1=35$: $7\in\mathrm{rad}(L)$ but never an adjacent link).
  4. Attempt to bound $|Q\setminus\Lambda|$: any candidate at step $n+1$
     must share an adjacent-link prime ($\le R$) with $a_n$ specifically
     (the ever-present $i=n$ constraint), so a prime in $Q\setminus\Lambda$
     can only ever be recruited for a non-adjacent, older constraint —
     combine with Lemma M (minimal-type reduction, certified) to try to cap
     the number of such primes. This is the concrete, still-open new gap.
Key lemmas (claim + mechanism):
  - Adjacent-Link Lemma — $\gcd(x,x+d)\mid d$, elementary.
  - $\Lambda$-stabilization — monotone subset sequence in a genuinely fixed
    finite universe, so pigeonhole here has no obstruction.
  - (Open) $Q\setminus\Lambda$ finiteness — sharper reformulation of
    Hypothesis SS; the new central target, unproved.
Open gaps: $Q\setminus\Lambda$ finiteness (step 4) — the genuine new central
gap.
Cases to cover: none beyond existing.
Watch out for: do not conflate $\Lambda$ with $Q$ (refuted); do not
resurrect $g(Q)$-threshold or prime-size-threshold mechanisms (both dead).

bounded-link-invariant: new
Target: the problem's actual claim, proved via a genuinely different
primary object — the gap sequence $d_n:=a_{n+1}-a_n$ and link sequence
$\ell_n:=\gcd(a_n,a_{n+1})$ directly, rather than via any finite prime set
$Q$ at all. This is the plateau-break approach: far from the
state-pigeonhole/covering-on-$Q$ framing shared by the other three, since it
requires NO hypothesis and NO prior determination of $Q$ to get a bounded
finite alphabet.
Technique: direct construction via a finite-alphabet local recurrence (an
automaton attempt on the compressed statistic $(d_n,\ell_n,\epsilon_n)$,
where $\epsilon_n$ is a new binary "exceptional step" invariant), aiming for
periodicity of $(d_n)$ itself (equivalent in strength to the problem's
conclusion, since $a_{n+T}=a_n+L\iff\sum_{k=n}^{n+T-1}d_k=L$ for all $n$).
Skeleton:
  1. Adjacent-Link Lemma (shared with jacobsthal-covering-bound, certify
     once): $(d_n,\ell_n)\in\{1,\dots,R\}^2$ for every $n\ge1$, unconditional.
  2. Define baseline step $b_n:=\min\{d\ge1:\gcd(a_n+d,a_1)>1\}\le R$
     (well-defined via certified `prime-factors-a1-cover-forever.md`), and
     $\epsilon_n:=\mathbb 1[d_n\ne b_n]$ (exceptional-step indicator).
  3. Attempt: test computationally, then try to prove, whether
     $\epsilon_{n+1}$ is determined by a bounded-length suffix of
     $(d_k,\ell_k)_{k\le n}$ (a bounded-order automaton on the *compressed*
     statistic — explicitly NOT the raw-term sliding window that explorer
     alt-framing already verified false for width 30).
  4. Fallback if step 3 fails: bound the density of exceptional steps
     instead of full periodicity, as a weaker but still useful structural
     fact.
Key lemmas (claim + mechanism):
  - Adjacent-Link Lemma (as above).
  - Baseline-step well-definedness — because $R(a_1)$ covers every term
    forever (certified), so a next-multiple-of-an-$R(a_1)$-prime candidate
    is always legal, bounding $b_n\le R$.
  - (Open, central) bounded-order determinacy of $(\epsilon_n)$ — may be
    false; a careful negative result here (in the style of
    jacobsthal-covering-bound's round-2 findings) is an acceptable, honest
    outcome, and would itself be new information (showing even a compressed
    local statistic, not just raw terms, is insufficient).
Open gaps: step 3 (bounded-order determinacy) and step 4 (fallback density
bound) — both entirely untried by the population so far.
Cases to cover: none beyond the general argument; any case split (locking
vs. non-locking $a_1$) would emerge from step 3's computational testing.
Watch out for: must not repeat the refuted raw-window mechanism (explorer
alt-framing's framing 1); must not claim periodicity of $(\epsilon_n)$
without computational verification on non-locking cases ($a_1=35,65,99$)
first — repeating an unverified-mechanism mistake here would be the third
such incident in this population.

build set: active-set-stabilization, state-compactness-pigeonhole, jacobsthal-covering-bound, bounded-link-invariant
