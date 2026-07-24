## imo-2026-03 — lens: "T'-cuts-p4" sub-case of Case (b)'s "v>=a" branch

### Setup recap (verified by hand against the file)
Case (b)'s "v>=a" branch needs $A(B)\ge f(n)$ for $B=\{b\}\cup T'$, where
$p_3$ is split into $(a,b)$, $a\ge b\in(0,p_4]$, and $T'$ is a legal
refinement of $\{p_4,\dots,p_{n+1}\}$ using $\le n-4$ cuts. The correct
project normalization is $f(n)=1/(2^{n+1}-1)$ (NOT $2^n/(2^{n+1}-1)$,
which is $c(n)$/the *Phi*-side target — I initially used the wrong one
and it produced a spurious huge "violation" via the excluded $b\to0^+$
boundary; see Small-case notes). Theorem 37 (round 23) proves the
specific vertex $b=p_4$, $T'=\{p_4\}\cup T''$ ($T'$ leaves $p_4$
untouched) gives $A(B)=A(T'')\ge f(n)$ via the Cross-Level Rescaling
Lemma + $(\star_{n-4})$. Round 24's Theorem 38 closes the *complementary*
sub-case ($T'$ cuts $p_4$) fully only at $n=5$ ($m=1$), via a standalone
induction target $h(m)=\inf A(\{c\}\cup S)$.

### 1. Can "b tied to a non-maximal element of T'" be ruled out by an exchange/domination argument specific to this structure?

**No clean argument found, and the file's own material already shows why
not.** The Insert-Element Identity gives $A(B)$ as piecewise-linear in
$b$ with slope $(-1)^{j(b)}$, $j(b)=|T'_{>b}|$ — so for *fixed* $T'$, the
minimum over $b$ is indeed always at a breakpoint (0, $p_4$, or some
element of $T'$), matching general LP-vertex theory. But *which*
breakpoint is worst depends on the parity pattern of $T'$'s own sorted
values, which is exactly what varies once $T'$ is allowed to cut pieces
below $p_4$ — round 23's own diagnostic already showed the "$b$ ties
$T'$'s top fragment" candidate is forced to a *residual* object
$\{c_2\}\cup T'''$ that is **structurally the same shape** as the
original problem one level down (not a simplification), and round 24's
own 3000-trial search found deeper ties (3rd, 5th, â€¦ largest element of
an arbitrary reference multiset) beat the "base trio" $\{0,\max(S),q_1\}$
in $\approx46\%$ of arbitrary-multiset trials and $\approx3.7\%$ even
under the genuine legal-ladder-refinement constraint. This is a real,
not merely hypothetical, phenomenon — I would not expect a
structure-specific "top-tie always dominates" lemma to exist here; the
project's own material has already twice failed to find one (round 22's
Insert-Element-slope route, round 23-24's odd-run-cancellation route),
and the $3.7\%$ empirical rate is a genuine signal, not noise.

### 2. What would the Theorem-38-style exhaustive extension look like, and is it tractable?

It is **not obviously tractable by literal enumeration for general $m$**.
At $m=1$ it worked because the tail-refinement budget was $0$, forcing
$S$ to be the entire untouched ladder — collapsing the "which element
does $c$ tie to" enumeration down to exactly 2 candidates. At $m=2$,
round 24 could only hand-close the $q_1$-split branch (one of 3 possible
single-piece-cut branches, $q_2$- and $q_3$-split are still open), and
for $m\ge3$ multiple pieces can be split *simultaneously*, so the number
of legal cut-compositions of $S$ grows combinatorially (roughly the
number of ways to distribute $\le m-1$ cuts across $m+1$ pieces, times
the split-point continuum per piece, times the number of odd-rank
breakpoint candidates for $c$ within each such $S$ — this product grows
at least like a partition count in $m$, not a fixed small constant). A
literal "enumerate every vertex type by hand for every $m$" proof plan
does not scale; the file's own honest scoping ("general $m\ge3$... open")
reflects this correctly. A more promising direction (one-line idea, not
developed): treat $h(m)$ itself as a disguised instance of the *whole*
project's already-general lower bound $L(m)$ — i.e. check whether
$\{c\}\cup S$, for the worst legal $c,S$, is literally a legal Xiang-Yu
response to some *other* Liu-Bang-type marking, so that $h(m)\ge f(m)$
would follow as a corollary of $(\star_m)$ itself rather than a fresh
vertex enumeration — worth a quick feasibility check next round rather
than continuing the case-by-case Theorem-38 extension.

### 3. Crux corpus check

Searched `combinatorics`/`extremal-principle` and `games-and-strategy`
subtopics for exchange/tie-breaking techniques on geometric/superincreasing
sequences. The closest analog is **`aimo-0146`** (2017-mathematicians
degree problem): its crux is "exchange-smoothing forces a bounded weighted
sum's free coordinates to equalize until only a few surviving profiles
remain, then enumerate by hand" — methodologically similar in *shape*
(smooth to a small vertex family, then hand-check the survivors) to what
Theorem 37/38 are already doing, but the objective there is a weighted
**sum** with fixed positive coefficients (no sign alternation), so the
smoothing direction is monotone and single-signed — it does not carry
the alternating-sign / rank-parity structure that makes *this* problem's
tie-vertex family multi-modal (deep ties beating top ties). I judge this
**not a genuine transplant candidate**, only a weak structural echo; no
crux in the corpus directly addresses "which tie-vertex of an alternating
odd/even-rank sum over a geometric ladder is globally worst." Recommend
not chasing this corpus lead further.

### 4. Numeric verification (exact Fraction, own independent script — not reusing round-23/24's scripts)

Corrected the target constant first: $f(n)=1/(2^{n+1}-1)$ (my first pass
used $2^n/(2^{n+1}-1)$ by mistake and got a spurious huge "violation" at
the excluded $b\to0^+$ boundary — that boundary is Case (a), out of
scope, not a real counterexample; flagging this as a trap for future
verification scripts).

With the corrected target, ran a fresh random-composition exact-`Fraction`
search over the **full** legal $(b,T')$ space (random cut-distribution
across $T'$'s pieces, random split points, and $b$ tested at $p_4$, at
*every* element of $T'$ including deep/non-maximal ones, and at a random
interior point) at $n=5,6,7,8$ (25k–60k trials each):

- **Zero violations of $A(B)\ge f(n)$ found at any $n$ tested** —
  corroborating (not proving) the underlying claim, consistent with the
  proof-reviewer's own 400k-trial finding at $n=5$.
- **New finding, worth relaying to the outliner:** at $n=6$, Theorem 37's
  own literal vertex ($b=p_4$, $T'=\{p_4\}\cup T''$ with $T''$ completely
  untouched) gives $A(B)=3/127$, strictly **above** the target
  $f(6)=1/127$. The true minimum *within Theorem 37's own family*
  ($b=p_4$, $p_4$ left untouched by $T'$) is only reached when $T''$
  itself is pushed to *its own* worst legal refinement (cutting $p_5$
  with 2 cuts) — reaching exactly $f(6)$. This means Theorem 37 combined
  with $(\star_{n-4})$ applied at *its own* tight point already
  witnesses the global minimum at $n=6$, **without needing any vertex
  where $b$ ties to a non-$p_4$ element of $T'$.** This is evidence (not
  proof) that the deep-tie concern may be moot specifically *for the
  $b=p_4$ family*, though it does not rule out that other ($b\ne p_4$)
  vertices also attain $f(n)$ (tied minimizers, harmless) or, for larger
  untested $n$, dip below it (not observed).
- At $n=8$ the search (fewer trials, 15k) did not find the exact tight
  value (best found $\approx0.002546 > f(8)\approx0.001957$) — consistent
  with needing either more trials or an exact vertex search rather than
  random sampling to hit tightness at higher $n$; not a red flag, just a
  sampling-density limitation.

### Distinct openings for the outliner
1. **Give up on ruling out deep ties structurally; instead directly prove
   $h(m)\ge f(m)$ for the *specific* legal-ladder-refinement domain**
   (not the arbitrary-multiset domain where deep ties provably win
   46% of the time) — the 3.7% legal-domain rate plus my $n=6$ finding
   suggest the ladder's own self-similar structure may make the deep-tie
   phenomenon harmless (always ties, never strictly beats, the target),
   even though it is NOT harmless for generic multisets. This reframes
   the target from "rule out the vertex type" to "show every vertex type,
   deep or shallow, evaluates to $\ge f(m)$" — closer to what round 24
   already outlined, but explicitly abandoning the "only two vertex types
   matter" simplification.
2. **Check the $h(m)$-as-disguised-$L(m)$-instance idea** (item 2 above)
   as a cheap feasibility probe before committing to more case-by-case
   extension — if it works, it could close the general $h(m)\ge f(m)$
   claim as a corollary rather than needing per-$m$ vertex casework.
3. **Do not re-attempt the corpus transplant from `aimo-0146`** — checked
   and it is only a weak methodological echo, not a real technique match
   (see item 3).

### Dead ends (confirmed, do not retry)
- Cross-Level Rescaling Lemma applied directly to $\{c\}\cup S$ (needs
  the whole refined object to already be a rescaled ladder; $c$ is an
  arbitrary fragment, not a ladder value) — confirmed dead by rounds
  23–24, re-confirmed by my own re-derivation.
- "Top-tie / boundary vertex always dominates" as a general fact for
  arbitrary reference multisets — false (46% counterexample rate,
  round 24's own numeric finding, re-derivable trivially since it's just
  parity of the number of elements exceeding the tie value).

### Prior progress (unchanged from round 24)
Theorem 37 (conditional on $(\star_{n-4})$, unconditional $n\le6$) closes
the "$T'$ leaves $p_4$ untouched, $b=p_4$" vertex. Theorem 38 closes
$h(1)$ exactly (hence the "$T'$ cuts $p_4$" sub-case fully at $n=5$) and
the $m=2$ $q_1$-split branch by hand; $m=2$'s $q_2/q_3$-split branches and
general $m\ge3$ remain open. No approach has yet produced a full,
non-numeric closure of the whole "$v\ge a$" branch for general $n$.
