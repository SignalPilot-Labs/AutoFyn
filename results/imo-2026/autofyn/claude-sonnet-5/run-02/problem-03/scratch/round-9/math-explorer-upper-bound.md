## imo-2026-03 (lens: general upper bound c(n) <= a_n for arbitrary Liu Bang markings, n>=3)

### What `lp-duality-certificate` actually has on file
Four **exact, unconditional, fully proved** closed-form identities for an
arbitrary marking $p_1\ge\cdots\ge p_m>0$ ($m=n+1$ pieces, total $T$), each a
single legal Xiang-Yu move whose resulting $\Phi$ is computed exactly via the
certified `pair-cancellation-identity`/`leftover-formula` (no case
restriction in the *derivation* — restrictions only appear when asking
whether the value meets target $a_nT$, $a_n=2^n/(2^{n+1}-1)$):

- **Theorem A (Full-Match)**: if $p_1\ge T/2$, split $p_1$ to match
  $p_2,\dots,p_m$ exactly (uses all $m-1$ cuts) $\Rightarrow\Phi=p_1$ exactly.
- **Theorem B (One-Step-Peel)**: cut $p_1\to(p_2,w{=}p_1-p_2)$ (1 cut), then
  apply *any* further strategy to $\{w,p_3,\dots,p_m\}$ with the remaining
  budget: $\Phi = p_2+\Phi'$ **exactly**, for *any* sub-strategy including
  the optimal one — this is already, as stated, a genuine recursive
  inequality $\Phi_{\min}(p_1,\dots,p_m)\le p_2+\Phi_{\min}(S')$, unconditional.
- **Theorem C (Bisect-Top)**: bisect $p_1$ only (1 cut), leave the *rest of
  the tail untouched* (0 further cuts spent) $\Rightarrow \Phi = p_1/2 +
  \Phi_{\mathrm{tail}}$ where $\Phi_{\mathrm{tail}}$ is literally the tail's
  own odd-rank sum in its **untouched** sorted order (a fixed constant, not
  a recursively-minimized quantity — this wastes the remaining $n-1$ cuts).
- **Theorem D (Bisect-Top-and-Bottom)**: bisect $p_1$ and $p_m$ (2 cuts),
  leave the middle untouched (0 further cuts spent on the middle) $\Rightarrow
  \Phi=p_1/2+p_m/2+\Phi_{\mathrm{mid}}$, same "wastes remaining budget" issue
  as C.

Combining these four (numerically, taking the pointwise min at every
config) passes 150k+ random trials and adversarial `differential_evolution`
search up to $n=6$ with **zero violations**, including both on-file hard
witnesses ($n{=}3$: $(3/8,1/4,1/4,1/8)$ solved by Theorem D exactly;
$(6,2,2,1)/11$ solved by Theorem D exactly). But **no general-$n$ proof**
that the combination suffices exists — only three individually-proved,
individually-crude sufficient conditions (Corollaries to A/B/D) covering
$\approx16$–$20\%$ of random configs.

### What exactly is missing (diagnosed precisely, not vaguely)
The gap is **not** "need more strategies" — it is that **Theorems C and D
throw away the remaining cut budget** instead of recursing with it, unlike
Theorem B which already recurses (and whose recursive sufficient condition,
$p_2\ge a_nT/2$, is the ONE fully successful derivation on file). C and D's
existing "proven sufficient conditions" use the *crude* bound
$A(\text{untouched block})\le\mathrm{Total}$ in place of the tail's actual
value — this is exactly the same "floor vs. exact value" failure mode
already diagnosed on the **lower-bound** side in rounds 7–8
(`case-ii-exact-peel-identity`'s note that the true value can exceed the
inductive floor). The upper-bound front has an unrecognized structural
mirror of that same obstruction.

### Concrete mechanism found this round (scouting-level algebra, exact-Fraction/sympy-checked, NOT a proof)
Define **Theorem C′ (Bisect-Top, Recursive)**: bisect $p_1$ (1 cut), then
apply the *optimal* strategy to the untouched tail $\{p_2,\dots,p_m\}$ using
the *remaining* $n-1$ cuts (matching a smaller instance of the same problem,
$m-1$ pieces, budget $n-1$). By the same `pair-cancellation-identity`
argument as Theorem C, this is an **exact identity**
$$\Phi = p_1/2 + \Phi_{\min}(\{p_2,\dots,p_m\},\,n-1\text{ cuts})$$
(unconditionally, for any sub-strategy — same status as Theorem B). Plugging
in the strong-induction hypothesis $\Phi_{\min}(\text{tail})\le a_{n-1}T'$
($T'=T-p_1$) and solving for when $p_1/2+a_{n-1}(T-p_1)\le a_nT$ gives, after
exact algebra (verified symbolically with `sympy`/exact `Fraction` for
$n=1,\dots,8$, not just floats — see computation below), the threshold
$$p_1 \ge a_n T \quad\text{(exactly)}.$$
This is a clean, striking finding: **Theorem A covers $p_1\in[T/2,a_nT]$
exactly, and Theorem C′ (with the inductive ceiling, not the crude bound)
covers $p_1\ge a_nT$ exactly** — the two intervals meet with no gap,
together covering the *entire* region $p_1\ge T/2$ by strong induction on
$m$, IF this can be formalized as an actual induction (base case $m=1$
trivial, $\Phi=T=a_0T$). This looks like a genuinely promising, nearly-formal
next step — the algebra is exact and the threshold match ($p_1\ge a_nT$
falling out cleanly, matching $a_n$ itself with no slop) is a strong signal
it is the "intended" mechanism, not a coincidence.

Verification snippet (exact `Rational` arithmetic, $n=1..7$):
threshold $=(a_{n-1}-a_n)/(a_{n-1}-1/2)$ computed exactly equals $a_n$ for
every $n=1,\dots,7$ tested.

**However — the residual $p_1<T/2$ case (no piece dominates) is where the
real difficulty survives**, and it is exactly where both on-file hard
witnesses live in spirit (the $(3/8,1/4,1/4,1/8)$ witness has $p_1=3/8<1/2$).
I checked whether the analogous **Theorem D′ (Bisect-Top-and-Bottom,
Recursive)** — bisect $p_1,p_m$ (2 cuts), recurse on the middle
$\{p_2,\dots,p_{m-1}\}$ with the inductive ceiling $a_{n-2}T''$ — closes this
corner. Its exact threshold works out (again exact `Rational` algebra,
$n=2,\dots,8$) to $p_1+p_m \ge \tfrac{3}{2}a_nT$, a real improvement over the
crude Theorem-D threshold $p_1+p_m\ge2(1-a_n)T$ for $n\ge3$ — but I checked
it directly against the $(3/8,1/4,1/4,1/8)$ witness ($n=3$) and **it still
fails**: $p_1+p_m=1/2$, threshold $=1.5\cdot8/15=0.8$, $0.5<0.8$. The
inductive-ceiling version of D also fails here even though the **exact**
(non-recursive-ceiling) Theorem D value succeeds at this witness
($\Phi=1/2<8/15$) — because the middle block $\{1/4,1/4\}$'s *actual*
$\Phi_{\min}=1/4$ is well below its inductive ceiling $a_1\cdot(1/2)=1/3$,
and the ceiling substitution alone is too lossy. **This is the same
floor-vs-exact-value obstruction recurring one level down** — strong
evidence this is the real crux, not a one-off Theorem-D artifact.

### Distinct openings / candidate mechanisms for the outliner
1. **Formalize Theorem C′ + Theorem A as a full closed sub-proof for
   $p_1\ge T/2$** — this appears close to complete and mechanical (mirrors
   the already-certified Theorem B derivation almost exactly); a builder
   should attempt to write this as a rigorous strong induction on $m$ with
   the base case $m=1$, closing HALF the marking space unconditionally.
   This is the single most promising concrete lead from this round.
2. **Strengthen the induction hypothesis to close the floor-vs-exact gap.**
   Instead of inducting on the bare statement "$\Phi_{\min}\le a_nT$," carry
   a sharper two-part inductive invariant (e.g. an exact characterization of
   *when* $\Phi_{\min}(S)$ is close to its ceiling $a_nT$ — likely only near
   the ladder-shaped extremal configurations — paired with a quantitative
   slack bound elsewhere). This is the standard fix for "recursion loses too
   much slack" failures, and is structurally the same fix the **lower-bound**
   front needs (round 7's `case-ii-exact-peel-identity` diagnosis) — a
   genuine opportunity to attack both fronts with one sharpened tool.
3. **Case-split on $p_1<T/2$ directly by exhausting a small number of
   "no-dominant-piece" strategies** rather than only bisection-recursion —
   e.g. a genuinely new move (three-way split of $p_1$, or a
   simultaneously-bisect-top-two-pieces move) analogous to round 4's ad hoc
   "trisect $p_1$" fix that solved $(3/8,1/4,1/4,1/8)$ before Theorem D was
   found. Worth surveying whether a **Theorem E (Bisect-Top-Two)** — bisect
   both $p_1,p_2$ simultaneously (2 cuts) and recurse on
   $\{p_3,\dots,p_m\}$ — gives yet another exact identity via
   `pair-cancellation-identity` with a cleaner threshold in the $p_1<T/2$
   regime (untested this round — flagged as next concrete thing to try, not
   attempted here per scouting-only mandate).
4. **Exploit that $p_1<T/2$ forces spread-out mass**: since no single piece
   dominates, a pigeonhole/pairing argument bounding how many pieces can
   simultaneously be "large" (e.g. at most $O(\log(1/a_n))$ pieces exceed
   any fixed threshold) might bound the case-split's branching factor,
   turning the $p_1<T/2$ residual into a *finite* case analysis per $n$
   rather than a continuum — worth exploring given the population's existing
   `vertex-minimum-theorem`/LP-vertex machinery (already certified,
   reusable) applies just as well to the upper-bound side's minimization
   over Xiang Yu's strategy, not just the lower-bound side.

### Cheap-kill candidates
- Before formalizing Theorem C′/D′ in full, cheaply verify the exact
  threshold algebra (`sympy` exact fractions, already done here for
  $n\le8$) generalizes to a clean closed form for **all** $n$ by induction
  on the algebraic identity itself (it telescopes via
  $a_{k-1}-a_k=2^{k-1}/(D_{k-1}D_k)$, $D_k=2^{k+1}-1$ — same telescoping
  machinery already used and certified in Theorem B's proof) — this is a
  five-line algebraic induction, not a search, and should be nearly free to
  nail down before spending a full builder round on it.
- Quickly check (exact `Fraction`, no need for `differential_evolution`)
  whether **every** numerically-found hard witness so far has $p_1<T/2$ —
  if so, that is strong structural confirmation that $p_1\ge T/2$ is a
  genuinely "easy" half and all remaining difficulty concentrates in the
  $p_1<T/2$ regime, focusing the next round's entire effort there instead of
  re-verifying the (likely fine) $p_1\ge T/2$ side.

### Knowledge-base entries to use
- `knowledge_base.md`'s generic strong-induction / extremal-principle
  entries (cited already by every approach in this population) apply
  directly to formalizing Theorem C′.
- The already-certified project lemmas `pair-cancellation-identity`,
  `leftover-formula`, `integral-alternating-sum-formula` are the load-bearing
  tools for Theorem C′/D′/E's exact-identity derivations (same tools used
  for A–D, no new tool needed).
- `vertex-minimum-theorem` / `odd-run-reduction-lemma` (already certified
  from the lower-bound side) are candidates to characterize the $p_1<T/2$
  residual's minimizing Xiang-Yu response exactly, rather than only via
  bounded strategy families — worth cross-pollinating from the lower-bound
  population into this front.

### Analogous past problems (cruxes)
Checked `combinatorics` / `games-and-strategy` (39 cruxes) and skimmed
`extremal-principle`/`induction-and-construction`. Nothing is a close
structural analog (this project's own round-1 finding — "no strong direct
analog" — still holds for this specific upper-bound sub-target). Closest
loose parallel: **aimo-0560** ("replace the adversary with a strictly
stronger surrogate whose reply is pointwise at least as damaging, so a win
against the surrogate transfers down") — matches the flavor of "take the min
of several concrete strategies as a surrogate for the true optimal
adversary," which is exactly what the combined-4-strategy approach already
does; it does not supply a new technique but does validate that
"min-of-explicit-strategies as surrogate for true minimax" is a recognized,
sound proof pattern in this corpus, worth citing as justification for the
overall approach shape (not a source of the missing induction step itself).
No other crux in `games-and-strategy`, `extremal-principle`, or
`induction-and-construction` (skimmed) resembles a continuous/geometric
"arbitrary instance, prove upper bound via case-split + recursion" pattern
closely enough to adapt directly.

### Prior progress
Current best on this front (per `lp-duality-certificate.md` and
`current.md` round 8): 4 exact identities (Theorems A–D), 3 individually
proved but crude sufficient conditions covering ~16–20% of configs,
150k+-trial + adversarial-search empirical support for the combined
strategy with zero violations, both known hard witnesses solved. No
general-$n$ proof. This round's new (unverified beyond scouting-level exact
algebra) finding: Theorem C′ (recursive bisect-top) plausibly closes the
entire $p_1\ge T/2$ half exactly and cleanly; the $p_1<T/2$ half is where
the real, still-unresolved difficulty concentrates, and the floor-vs-exact
gap re-appears there one level down (checked concretely against the
$(3/8,1/4,1/4,1/8)$ witness).

### Dead ends (do not retry)
- Direct generalization of the $n=2$ six-template case-analysis mechanism
  to $n=3$ — already confirmed dead (round 4, `smoothing-compactness-
  certificate`): fails at $(3/8,1/4,1/4,1/8)$, needs an ad hoc 7th strategy.
- Using Theorem C or D's **crude** bound ($A\le\mathrm{Total}$) as the final
  word — confirmed too weak at both on-file hard witnesses (this round's
  analysis); any future work must use either the exact value or a sharper
  inductive ceiling (per opening 2 above), not the crude bound.

### Small-case / intuition notes (conjectural, not proved)
- Conjecture (numeric + this round's algebra): $p_1\ge T/2$ is a genuinely
  "solved" half of the marking space once Theorem C′ is formalized —
  strongly suggested by the exact threshold match $p_1\ge a_nT$ with zero
  slack, but not yet formally proved as an induction.
- Conjecture: the two known hard witnesses, and likely all hard witnesses in
  general, satisfy $p_1<T/2$ (no dominant piece) — worth a cheap exact-
  `Fraction` check across the existing 150k-trial data before the next
  round, to confirm the case-split "p1>=T/2 easy / p1<T/2 hard" actually
  matches where the adversarial search concentrates its found near-misses.
