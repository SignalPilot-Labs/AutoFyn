## imo-2026-06 (alternative-framing scout, round 3)

Read: `current.md`, all 4 approach files (summaries via `current.md`'s per-approach
history), all 12 certified lemmas (`monotonicity-obstruction`,
`set-theoretic-acceptance-characterization`, `eventual-periodicity-given-hypothesis-ss`,
`prime-factors-a1-cover-forever`, `minimal-type-reduction`, `bounded-gap-via-rad-a1`,
plus the rest listed in `current.md`), `/tmp/memory/math-explorer.md`,
`/tmp/memory/run_state.md`. Ran new numerical experiments (below). Searched the
crux corpus by `subtopic` across NT (`invariants-and-monovariants`,
`sequences-and-recurrences`) and free-text over `technique`/`how_used` for
"periodic", "greedy", "covering", "sieve", "density".

### Distinct openings scouted (all three requested framings tried; verdict below)

**1. Sieve/density framing — REJECTED empirically, not just "not tried."**
Tested directly whether the greedy acceptance rule reduces to a *bounded
memory window*: for several `a_1` (15,35,65,99,105), at each step I computed
the candidate that a **width-W window** (last W=30 terms only) would pick,
vs. the true `a_{n+1}` (which must satisfy `gcd>1` against **all** earlier
terms). Result: for `a_1=15` the window-only rule matches the true rule on
all 349 tested steps (locking case, see below), but for `a_1=35,65,99,105`
the window-only rule is **wrong 3, 62, 53, 98 times respectively out of 349**
— i.e. old, far-back terms genuinely and frequently bind. This kills any
hope of a density/sieve argument that only tracks "recent" residue coverage;
the true state is not window-local, confirming (independently, via a
different method) why every existing approach needed a *type*-based
(unbounded-lookback) state instead. **This closes off, rather than opens,
framing 1 as literally stated — report this as a verified negative finding,
not a live opening**, so the outliner does not waste a round on it.

**2. Direct-construction / reverse-engineer-L(a_1) framing — extends existing
negative finding with a sharper counterexample.** Computed exact `(T,L,Q)`
triples for 17 values of `a_1` (see table below). Reconfirms
`math-explorer.md` rule 9 (no closed form for `Q(a_1)` from `rad(a_1)`
alone) but with a much sharper witness pair: **`a_1=33` (primes `{3,11}`)
locks trivially with `T=1, L=3` (i.e. `a_{n+1}=a_n+3` from `n=2` on,
period-1 immediately), while `a_1=99` — same radical `{3,11}`, only the
exponent of 3 differs (`3^2` vs `3^1`, which is irrelevant to every gcd
condition in the problem, since gcd conditions only ever see `rad`) —
recruits primes `2,5` and needs `T=72, L=330`.** I traced *why*: at `a_1=99`,
step 4→5 the term `110 = 2·5·11` beats the "expected" next multiple of 3
(`111`) purely because `11 | 110` happens to land at that exact residue
near the trajectory (a coincidence of *where* multiples of 11 fall near the
current value of `a_n`, not any algebraic property of `99` itself), whereas
for `a_1=33` no such coincidence ever occurs near `36`. **Conclusion: the
recruitment/non-recruitment dichotomy is governed by proximity of alternate
covering primes' multiples to the trajectory — a genuinely Diophantine
(distance-to-nearest-multiple) phenomenon, not an algebraic one.** This is
useful framing vocabulary (a "race" between the locked prime's next multiple
and alternative-prime shortcuts) but I could not turn it into a monovariant
in the time available; flag it as a possible angle (bound how often a
"shortcut" can beat the default step, via some Dirichlet/three-distance-type
argument on how densely multiples of *any* fixed prime `q` can approach an
arithmetic progression) rather than a finished mechanism.

**3. Automaton/shift-invariance framing — partially attempted, same wall as
population.** Tried to see whether the map on "type" could be shown
shift-invariant *without* first fixing `Q`, using the extremal-orbit idea
from crux `aimo-0896` ("take the minimal element of a forward orbit, force
equality of factors ≥ it"). The analogy doesn't transfer cleanly: `aimo-0896`
has a genuine algebraic identity (`m^2 = f^2(m)·f^{f(m)}(m)`) forcing
equality once minimality is invoked; imo-2026-06 has no such multiplicative
identity between the "state" and its update — the greedy step is a
minimum-of-a-set operation, not an iterate of a fixed function, so there is
no orbit-square identity to exploit. I do not recommend pursuing this
specific transfer further; noting it here so it isn't re-tried blind.

### Cheap-kill candidates
None found beyond what's already certified (`bounded-gap-via-rad-a1`,
`prime-factors-a1-cover-forever`). The single-prime "locking" sub-case (found
above: whenever the smallest prime `p | a_1` never gets pre-empted by a
shortcut, `T=1, L=p` trivially, closing BOTH the central gap and the
prefix-extension gap at once in that sub-case) is a genuine easy special
case, but it does not reduce the general (non-locking) problem — it is a
strict sub-case of Hypothesis SS with `Q=\{p\}`, and the interesting content
of the problem is entirely in when/why locking *fails*.

### Knowledge-base entries
Re-checked `knowledge_base.md` for anything not yet cited by the population
(Jacobsthal function, covering systems, three-distance theorem, CRT compactness
arguments) — nothing beyond what `jacobsthal-covering-bound.md` already used
(and refuted as a termination mechanism) appears applicable. No new KB entry
to add to the population's toolkit from this pass.

### Analogous past problems (cruxes)
Re-searched beyond the population's prior finding of `aimo-0680`
(IMO-SL 2015 N4, cited by memory rules 1–2, still the closest analog for the
*finishing* technique "divides + bounded-below-modulus ⟹ pinned exactly").
New candidates checked this round, both rejected as not genuinely
analogous:
- `aimo-0982` (digit subsequence sampled at moving indices, eventually
  periodic via `2^n mod d`): superficially similar conclusion shape, but the
  periodicity there is handed to you by a known eventually-periodic decimal
  expansion (Fermat–Euler on the modulus) — no analog of "which primes ever
  matter" gap exists; the hard part of THIS problem (Hypothesis SS) has no
  counterpart there. Not a genuine match.
- `aimo-0611` (Zsigmondy/primitive-divisor growth argument, "term grows
  larger than the product of all earlier terms"): this is exactly the
  mechanism `growth-rate-contradiction` already tried and had **twice
  refuted** (see `/tmp/memory/math-explorer.md` rule on
  growth-rate-contradiction dead ends) — do not resurrect it under a new name.
- No crux in `sequences-and-recurrences` (NT, 6 entries) or
  `invariants-and-monovariants` (NT, 2 entries) resembles the greedy-covering
  structure of this problem. **Verdict: no new genuinely analogous crux found
  this round; `aimo-0680` (already known to the population) remains the best
  match, only for the finishing/pinning step, not for Hypothesis SS.**

### Prior progress
No change to the certified facts; see `current.md` — unconditional: existence,
bounded-gap O(n), prime-factors-of-a_1-cover-forever, pairwise
non-coprimality, every-term-meets-recurring-set. Conditional (on unproved
Hypothesis SS): eventual periodicity of the tail. Two gaps open: Hypothesis
SS (self-sufficiency of finite active prime set Q) and prefix-extension
(periodicity from n=1, not just eventually).

### Dead ends (do not retry)
- Fixed-width bounded-memory / sliding-window automaton (this round,
  verified false computationally: window of 30 terms gives wrong next-term
  in up to 98/349 steps for some `a_1`).
- Any closed-form `Q(a_1)` or `L(a_1)` from `rad(a_1)` alone (round 2,
  reconfirmed sharper this round: `a_1=33` vs `a_1=99`, same radical,
  wildly different `Q,T,L`).
- Growth-rate/Zsigmondy-style "term exceeds product of earlier terms" bound
  (round 1–2, refuted twice; also the closest-looking crux `aimo-0611` uses
  exactly this refuted mechanism — do not resurrect).
- Orbit-square / minimal-forward-orbit transfer from `aimo-0896` (this round;
  no algebraic identity in imo-2026-06 for it to exploit).
- Covering-gap threshold `g(Q)` and prime-size threshold mechanisms
  (round 2, already dead per `current.md`/`jacobsthal-covering-bound.md`).
- "S := primes recurring infinitely often is finite" (round 1, proven false
  in round 2 — do not re-target).

### Small-case / intuition notes (all labeled conjecture except the raw computed data)
Computed exact `(T, L, Q\setminus R(a_1))` for 17 seeds (all confirmed by
direct simulation up to the periods found, capped at 900 terms / 1e6 value;
`a_1 ∈ {255, 385}` did not stabilize within this budget, consistent with
memory rule 9's finding that transient length is not boundedly small):

| a_1 | R(a_1) | T | L | extra primes recruited |
|---|---|---|---|---|
|15|{3,5}|8|30|{2}|
|21|{3,7}|1|3|{}|
|33|{3,11}|1|3|{}|
|35|{5,7}|34|210|{2,3}|
|55|{5,11}|1|5|{}|
|63|{3,7}|1|3|{}|
|65|{5,13}|58|390|{2,3}|
|77|{7,11}|18|154|{2}|
|91|{7,13}|20|182|{2}|
|99|{3,11}|72|330|{2,5}|
|105|{3,5,7}|58|210|{2}|
|143|{11,13}|64|858|{2,3}|
|165|{3,5,11}|86|330|{2}|
|195|{3,5,13}|100|390|{2}|
|231|{3,7,11}|1|3|{}|

Conjecture (new, this round): a `T=1` "locking" outcome occurs precisely
when the smallest prime `p` dividing `a_1` is never pre-empted near the
trajectory by a smaller number built from a different prime combination
that also satisfies every earlier constraint — a Diophantine
proximity/coincidence condition on where multiples of *other* covering
primes fall relative to the arithmetic progression `a_1, a_1+p, a_1+2p, ...`,
not an algebraic property of `rad(a_1)` (witnessed by `a_1=33` vs `a_1=99`,
identical radical, opposite outcomes). This is evidence for, not a proof of,
the general shape of Hypothesis SS, and I was not able to convert it into a
monovariant or termination bound in the time budget — flagging it as raw
material for the next attempt rather than a finished mechanism.

**Bottom line for the outliner:** none of the three prescribed alternative
framings (sieve/density, automaton-without-Q-first, orbit-square transfer)
produced a working mechanism; framing 1 is now a *verified* dead end (not
just unexplored), and framing 3's specific crux transfer is a verified dead
end. The one genuinely new material this round is the sharp `a_1=33` vs
`a_1=99` counterexample pinning the recruitment mechanism to Diophantine
proximity of alternate-prime multiples rather than any algebraic function of
`a_1` — this is a candidate *vocabulary* for a future monovariant (e.g. "how
close can a multiple of an outside prime `q` get to a fixed arithmetic
progression, and how often", possibly via three-distance-theorem-style
reasoning) but is not itself a proof route yet, and no approach in the
population currently uses this framing — it is genuinely distant from the
existing field's Q-finiteness-first mechanisms.
