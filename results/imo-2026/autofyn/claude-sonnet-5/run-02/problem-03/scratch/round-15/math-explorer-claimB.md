# Round 15 scouting report — Claim (B) / greedy-halving-adversary

Scope: scouted (did not attempt full proofs) the four remaining open items in
the ℓ(F)≤2 + ℓ(F)≥3 induction for restricted Claim (B), per the round-15
assignment. All numerics below use exact `Fraction` arithmetic
(`/tmp/round-15/explore3.py`, `explore4.py`, `check_thm29_shortcut.py`);
floats are only used for display.

## Headline finding: items 1 and 2 are the same gap, not two gaps

Round 11's proof of ℓ(F)=2 sub-case (b) (`Lemma 25`, certified, no gap)
shows **exactly**: for `v1,v2<p2`,
$$A(\{v_1,v_2\}\cup P\cup G')=A(G')+A(\{v_1\}\cup P\cup G')-A(\{v_2\}\cup P\cup G'),$$
i.e. sub-case (b) is an *exact* algebraic combination of **two** instances of
the still-open ℓ(F)=1, `v<p_2` problem. Since Proposition 24 already closes
the `v∈[s,p_2)` half of that problem, sub-case (b) is open **only** insofar as
`v<s` is open. **Closing item 1 (`v<s`) closes item 2 (sub-case (b)) for
free**, with zero extra work — this is not a new reduction, it's already
proved and certified (Lemma 25), just not spelled out as "items 1≡2" in
`current.md`. This should be the top-priority framing for round 15: attack
`v<s` once, get two closed items.

Numerically this claim is corroborated, not just cited: sub-case (b)'s own
worst-case margin (below) tracks item 1's margin closely and is in fact the
*tightest* of all four items, consistent with it inheriting item 1's
difficulty rather than adding new difficulty of its own.

## Numeric slack (exact Fraction, `n=3..6`, thousands of random legal
configurations per item, cut budgets correctly capped per item — see "budget
bugs found and fixed" below)

| item | n=3 | n=4 | n=5 | n=6 | relative slack trend |
|---|---|---|---|---|---|
| 1. ℓ(F)=1, `v<s` | slack 0.0667 (rel. 1.00×f(n)) | 0.0326 (1.02×) | 0.0287 (1.81×) | 0.0220 (2.79×) | grows relatively with n |
| 2. ℓ(F)=2 (b) | 0.0037 (**0.055×f(n)**) | 0.0046 (0.14×) | 0.0148 (0.93×) | 0.0151 (1.92×) | tightest at small n |
| 3. ℓ(F)=2, P≠∅, τ_P≥p3 | 0.0754 (1.13×) | 0.1123 (3.48×) | 0.1311 (8.26×) | 0.1373 (17.4×) | very comfortable, grows fast |
| 4. ℓ(F)≥3 | **0.0000 (exact tie)** | 0.0072 (0.22×) | 0.0076 (0.48×) | 0.0183 (2.32×) | tight only at n=3, then comfortable |

(f(n)=1/(2^{n+1}-1): 0.0667, 0.0323, 0.0159, 0.00787 for n=3..6.)

Reading: item 3 has by far the most slack (comfortable, target inequality far
from tight even before a proof exists) — it's the "easy in principle, needs a
new mechanism" case. Item 2 (sub-case (b)) is genuinely the tightest at
n=3,4, confirming it is exactly as hard as item 1 (its parent), not harder or
easier. Item 4 hits an *exact* equality at n=3 — a real boundary case worth
noting (likely the same "cascading tie-vertex" phenomenon already seen
elsewhere in this population, e.g. round 4's n=1 tie, round 6's cascading
family) — then has real slack for n≥4.

## Does Theorem 29 (Half-Dominance Split Bound) directly close item 1 or item 3? No — checked and refuted, not just assumed

**Item 1 (v<s):** wrong direction categorically. Theorem 29 proves an
**upper** bound, $A(F_2\cup R)\le M-A(R)$; item 1 needs a **lower** bound,
$A(F\cup G')\ge f(n)$. There is no way to instantiate Theorem 29 (for any
choice of $M$, $F_2$, $R$) to produce a lower bound on $A$ — its proof
mechanism (Lemma 29a + cross-term-identity-threshold) is inherently
one-directional. Not applicable, not a near-miss.

**Item 3 (τ_P≥p3):** checked whether the *general* theorem (not just the
`sharp-dominant-removal-identity` route Prop 29b already used) could close
the complementary range by instantiating $M:=t^*=p_2-\tau_P$, $F_2:=\{t^*\}$
(a trivial 1-part split), $R:=G'$. This requires the hypothesis
$\max(G')\le t^*/2$. Since $\tau_P\ge p_3=p_2/2$, $t^*\le p_2-p_3=p_3$, so
the hypothesis needs $\max(G')\le p_3/2$ — but $G'$ is a legal refinement of
$\{p_3,\dots,p_{n+1}\}$ and can leave $p_3$ itself untouched, giving
$\max(G')=p_3$, which is **double** the required bound. The hypothesis fails
by a factor of 2, not a corner case. Confirmed this isn't just a hypothesis
formality by testing the theorem's *conclusion* directly outside its
hypothesis: for random legal $t^*\in(0,p_3]$ and random legal $G'$
(`/tmp/round-15/check_thm29_shortcut.py`, exact Fraction, 3000 trials/$n$,
$n=3,\dots,6$), the naive conclusion $A(\{t^*\}\cup G')\le t^*-A(G')$ is
**violated in ~92% of trials**, with violation margins up to ~0.26 (not
epsilon-small) — e.g. at $n=3$: violated 2808/3000 times, worst margin
0.261. **This is a confirmed false shortcut, not merely an unproven one** —
flagging so no future round wastes time trying to force Theorem 29's general
form onto item 3's open range. Item 3 genuinely needs a different mechanism
than either `sharp-dominant-removal-identity` or `half-dominance-split-bound`
in the $\tau_P\ge p_3$ regime.

## Budget bugs found and fixed (recorded so no future round repeats them)

Two bugs surfaced and were fixed during this scouting, both of the same
"illegal extra freedom" flavor the population has hit before (round 10's
"forgot to cap cut budget" near-misses, explicitly recorded in
`current.md`):
1. An `exact_pair_set` helper initially returned pairs summing to **2×** the
   intended total mass (each pair $(v,v)$ contributes $2v$, and the helper's
   fraction-of-total-mass parameterization didn't divide by 2) — this
   silently gave item 3 and item 4 too much/wrong mass in `P`, which
   would have invalidated any conclusion drawn from the first pass.
2. The first item-4 script omitted $p_2$ from the tail entirely (used
   `pieces[2:]` instead of `pieces[1:]`), so the constructed multiset didn't
   sum to 1 — this produced a spurious "violation" (slack -0.05 at n=3) that
   vanished once $p_2$ was correctly included in the refinable tail. Both are
   fixed in `/tmp/round-15/explore4.py`; the corrected item-4 numbers in the
   table above are the ones to trust. This is exactly the kind of
   scripting trap `current.md` already warns about (round 10's two
   self-caught bugs) — worth re-emphasizing to round 15's builder: always
   verify `sum(constructed multiset) == 1` as a sanity assert before trusting
   any exact-Fraction search on this problem.

## Recommendation for round 15

**Top priority: item 1 (ℓ(F)=1, `v<s`).** Highest leverage — proving it
closes item 2 (sub-case (b)) simultaneously via the already-certified Lemma
25 identity, at zero extra cost. It is not the most numerically comfortable
of the four, but it is the most load-bearing (it gates two of the four open
items). Round 9/10's own diagnosis of why the existing mechanism breaks here
is precise: Proposition 24's proof needs `[0,v)` to contain all of $R'$'s
support, which needs $v\ge s$; for $v<s$, $R'$ has mass beyond $v$, and
$\int_0^v u_{R'}$ is a genuine partial integral, not the full $A(R')$ — the
same shape of problem recursed one level down. A rescaling argument at the
$(n-2)$-level sub-tail (analogous to Proposition 24's own $(\star_{n-2})$
but now needing to handle a *partial* window) is the natural next thing to
try; it was flagged but not attempted in depth in prior rounds.

**Second priority: item 3 (τ_P≥p3), if item 1 doesn't yield this round.**
Numerically the most comfortable inequality of the four (slack growing to
17× f(n) by n=6) — meaning whatever mechanism eventually closes it has a lot
of room, so a cruder/weaker sufficient bound than the sharp identity used for
τ_P<p3 may well suffice (e.g., a bound using only $\max(G')\le p_3$ crudely
combined with $A(G')\ge f(n)$, rather than an exact peel identity). This is
speculative — not verified as a working proof route — but the generous
numeric margin makes it a good round-15 bet given it's cheap to try before
committing to item 1's harder recursive argument.

**Lower priority: item 4 (ℓ(F)≥3).** Comfortably satisfied numerically for
n≥4 (exact tie only at the n=3 boundary, consistent with other known tie
cases in this population), so it is *not* a red flag, but it is completely
untouched machinery-wise and is the largest scope item (needs a Lemma-25-style
exact decomposition generalized to 3+ residuals, i.e., essentially the
still-unproved `ℓ(F)`-Collapse Lemma or a fresh induction on `ℓ(F)`). Good
candidate for a dedicated future round, not this one, given items 1–3 are
more surgically scoped.

## Files
- `/tmp/round-15/explore3.py` — items 1, 2b, 3 (budget-correct versions).
- `/tmp/round-15/explore4.py` — item 4 (budget- and mass-correct version;
  supersedes the buggy first pass).
- `/tmp/round-15/check_thm29_shortcut.py` — the Theorem-29-shortcut
  refutation for item 3.
