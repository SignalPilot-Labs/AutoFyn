# Scouting report: closing case (a) at n=3, and n=4 feasibility for the covering-family technique

## Headline finding: case (a) at n=3 is already unconditionally closed by
## existing certified lemmas — round 25's gap is a citation/assembly bug,
## not a missing piece of mathematics.

### The three-way partition (recap, resolved)

`lp-duality-certificate` partitions every $n=3$ marking purely by the value
of $p_2$ (no dependence on $p_1$, despite round 25's confused final
paragraph which wrongly relabeled case (a) as "$p_1\ge T/2$" — that is a
different, weaker sufficient condition, Theorem A, not what closes case
(a)):

- **case (b1):** $p_2\le T/D_3=T/15$ — closed **unconditionally for every
  $n$** via `lemmas/unconditional-p2-threshold-closure.md` (bisect $p_1$,
  Max-Domination Lemma on the untouched tail). No gap, no dependency.
- **case (b2):** $T/15<p_2<a_3T/2=4T/15$ (the open "box") — closed **at
  $n=3$ specifically** by round 25's `lemmas/case-b2-n3-covering-closure.md`:
  a 5-chamber family (Bisect{1,4}, Bisect{1,2}, DS-Above, Triple-Pin,
  R22.1.1) with six exact Farkas/Fourier–Motzkin infeasibility certificates
  proving the family covers the whole box, reviewer-reverified line by line
  plus 23,880 random exact-`Fraction` samples, zero uncovered points. This
  part is solid and does not need to be redone.
- **case (a):** $p_2\ge a_3T/2$ — closed via the **Corollary (Theorem B,
  recursive sufficient condition)** in `approaches/lp-duality-certificate.md`
  (§ "Proven sufficient conditions", around line 1037): if $p_2\ge a_nT/2$
  and the reduced 3-element instance $S'=\{w,p_3,p_4\}$ ($w=p_1-p_2$)
  satisfies $\Phi_{\min}(S')\le a_{m-2}T'$ (here $m=4$, so $a_{m-2}=a_2$),
  then $\Phi_{\min}(p)\le a_3T$. This Corollary is proved in full generality
  (any $m$), unconditionally, **except** that it needs the general
  ($S'$ can be *any* 3-element marking) upper bound $c(2)\le a_2T'=\frac47T'$
  as its hypothesis.

### Why case (a) at n=3 needs no new work

That hypothesis — "$c(2)\le\frac47T'$ for every Liu Bang marking with
$\le2$ cuts, not just the ladder" — is **exactly**
`lemmas/n2-upper-bound-lp-argument.md`: the round-1 six-template
LP-contradiction argument, proved for *every* 0/1/2-point configuration at
$n=2$, fully rigorous, zero numerics (numerics used only as an independent
reviewer cross-check). This is one of the two oldest, most solid results in
the whole project.

`lemmas/p-space-chamber-vertex-theorem.md` (item 3, the round-23-corrected
text) already states this explicitly:

> "at $n\le3$, all three walls are unconditionally closed (since 'one level
> down' from $n\le3$ is $n\le2$, already fully closed in this project), so
> the corollary below applies with zero caveats; at $n\ge4$, the corollary
> is conditional..."

So **the machinery to close case (a) at $n=3$ unconditionally is already on
file and already certified** — it's just never been explicitly assembled
into one citation chain in `lp-duality-certificate.md`'s final combination
paragraph. Round 25's write-up cited the wrong theorem (Theorem A /
$p_1\ge T/2$, which does *not* cover all of $p_2\ge a_3T/2$) instead of the
right one (Theorem B's recursive Corollary + `n2-upper-bound-lp-argument`).

**Concrete smallest next step for round 26:** have the `lp-duality-certificate`
builder rewrite the final "Conclusion of R25.1" combination paragraph
(approaches/lp-duality-certificate.md, ~line 5841–5862) to:
1. State case (a) as $p_2\ge a_3T/2$ (not $p_1\ge T/2$).
2. Cite the Corollary (Theorem B, recursive sufficient condition) with
   $m=4$, $S'=\{p_1-p_2,p_3,p_4\}$, invoking `n2-upper-bound-lp-argument`
   (general $n=2$ upper bound, unconditional) to discharge the Corollary's
   hypothesis.
3. Verify the three regions partition $p_2\in(0,T]$ with no gap/overlap:
   $p_2\le T/15$, $T/15<p_2<4T/15$, $p_2\ge4T/15$ — a trivial real-line
   partition, but should be stated explicitly (and the closed/open
   endpoints matched: case (b1) and case (a) are each closed/inclusive at
   their shared boundary with case (b2)'s open box, so no boundary point is
   double-covered or dropped — also double-check the box's own excluded
   boundary vertex $p^*=(2/5,4/15,1/5,2/15)T$, already resolved in round 25
   as lying on the case-(a) boundary $p_2=4/15$ and covered there).
4. State the combined conclusion: $c(3)\le a_3=8/15$ for *every* legal
   marking at $n=3$, both directions now closed (lower bound direction is a
   separate, still-open front — do not conflate; this only closes the
   upper bound).

This is essentially a **writing/assembly task plus one reviewer
double-check**, not new mathematics — no new lemma should be needed. It is
very likely gettable to a genuine APPROVE-scoped "$n=3$ upper bound: solved"
result in one more round, closing a real, long-standing headline item
(the project has been chasing exactly this since round ~13).

One thing genuinely worth re-verifying (not just re-citing) rather than
taking on faith: that $S'=\{p_1-p_2,p_3,p_4\}$, which need not be sorted
(e.g. $w=p_1-p_2$ could be smaller than $p_4$), is still covered by
`n2-upper-bound-lp-argument`'s "for every configuration" claim. Reading
that lemma's proof (six templates covering both $p\ge1/2$ and $p\le1/2$
sub-regions of the $n=2$ simplex, degenerate 0/1-point cases handled
separately) — it is stated for an arbitrary positive triple with no
sortedness assumption baked into the argument beyond WLOG-labeling, so this
should be a non-issue, but the round-26 builder should say so explicitly
rather than silently assume it.

## Question 2: does the covering-family technique generalize to n=4?

**Partial yes for the infrastructure, open/risky for the actual chamber
enumeration.**

- `lemmas/unconditional-p2-threshold-closure.md` (case b1) is already
  general-$n$, no work needed at $n=4$.
- Case (a) at $n=4$ uses the *same* Corollary (Theorem B, recursive
  sufficient condition), now needing $c(3)\le a_3T'$ for an **arbitrary**
  (not just ladder) 4-element $S'$ — i.e., exactly the general $n=3$ upper
  bound closure that round 26 is being asked to assemble. If round 26
  succeeds, **case (a) at $n=4$ becomes free** (no new work, same
  Corollary, new base case). This is a genuine inductive bootstrap worth
  flagging to future rounds: closing $n=3$'s upper bound in full doesn't
  just finish $n=3$, it unlocks $n=4$'s case (a) for free.
- Case (b2) at $n=4$ (the box $T/D_4<p_2<a_4T/2$) is the real open
  question. The chamber infrastructure itself
  (`within-chamber-affinity-theorem`, `p-space-chamber-vertex-theorem`,
  `vertex-minimum-theorem`) is proved for **general $n$**, not just $n=3$ —
  the polyhedral/vertex-attainment argument doesn't reference $n=3$
  anywhere in its proof. So the *method* (characterize each type's chamber
  as a $p$-space polyhedron, evaluate $g=a_nT-\Phi_{\min}$ at finitely many
  vertices, Farkas-certify infeasibility of "uncovered" regions) is not
  n=3-specific in principle.
- **But the actual chamber census is not general-$n$, and there is a
  documented amber-flag risk signal**: `within-chamber-affinity-theorem.md`
  explicitly records "chamber/type density growing from $\approx28\%$ at
  $n=3$ to $\approx64\%$ at $n=4$ inside case (b2)'s box, composition-level
  sampling" — meaning as $n$ grows, a much larger fraction of sampled
  points in the box are *not* explained by any currently-known chamber
  formula, so a naive extrapolation of "find a few more chambers" is not
  obviously going to terminate quickly. Compounding this, round 23 already
  found that even at $n=3$ a single composition, $(2,0,0,0)$, can host
  **two** distinct optimal chamber types (Chamber A and Chamber A2) in
  different sub-regions — so "one composition = one chamber" is false even
  at $n=3$, and the true chamber count at $n=4$ (5 pieces, more
  compositions, more possible tie-vertex configurations per composition)
  should be expected to be considerably larger than 5, not a modest bump.
- No lemma file yet gives a bound (even conjectural) on the number of
  chambers needed at $n=4$; this is a genuinely unquantified combinatorial
  blow-up risk, not yet a proven obstruction.

**Feasibility assessment:** the *method* (Farkas-certificate covering
families over $p$-space chambers, built on `within-chamber-affinity-theorem`
+ `p-space-chamber-vertex-theorem`) is mechanically applicable at $n=4$ with
no new theory needed — it is "just" a bigger finite case-enumeration problem.
But "just bigger" is doing real work: round 22–25 needed ~4 rounds and
multiple new chamber families to nail down 5 chambers for $n=3$'s much
smaller box; the documented density signal suggests $n=4$ will need
substantially more chambers, and there is no proof yet that the chamber
count stays polynomial (vs. blowing up) as $n\to\infty$ — the project's own
"amber-flag" language is an honest acknowledgment of this. This is not a
dead end, but it is not close to "solved in one more round" the way case (a)
now is.

## Recommended next step for round 26

1. **Cheap, high-value, likely-closeable this round:** assign
   `lp-duality-certificate` to fix the case(a)/case(b1)/case(b2) citation
   as described above and assemble the complete $n=3$ general-marking upper
   bound $c(3)\le8/15$ proof (verified, no new lemmas needed beyond
   re-citing `n2-upper-bound-lp-argument`, the Corollary, and the two
   already-certified round-25 lemmas). This should be pushed hard — it is
   the closest the upper-bound front has ever been to a genuine, complete,
   reviewer-certifiable per-$n$ result.
2. **Separately, and lower-priority/slower:** if pushing to $n=4$, the
   right framing is "start the chamber census for $n=4$'s box, expect it to
   be substantially larger than 5 chambers, and track whether the
   28%→64% density signal keeps worsening" — this is exploratory,
   multi-round work, not a quick follow-on. Do not expect a repeat of the
   5-chamber-in-one-round result; budget for it as its own multi-round
   sub-arc, and consider whether a genuinely different mechanism (not
   per-composition chamber enumeration) might be needed to avoid the
   apparent combinatorial growth before committing many rounds to brute
   enumeration.

## Files consulted

- `/home/agentuser/repo/results/imo-2026-03/current.md` (rounds 8–25 history,
  esp. lines 751–800, 1095–1146, 1766–1927, 2020–2153)
- `/home/agentuser/repo/results/imo-2026-03/approaches/lp-duality-certificate.md`
  (lines 730–806, 1000–1070, 5790–5886)
- `/home/agentuser/repo/results/imo-2026-03/lemmas/n2-upper-bound-lp-argument.md`
- `/home/agentuser/repo/results/imo-2026-03/lemmas/unconditional-p2-threshold-closure.md`
- `/home/agentuser/repo/results/imo-2026-03/lemmas/p-space-chamber-vertex-theorem.md`
- `/home/agentuser/repo/results/imo-2026-03/lemmas/within-chamber-affinity-theorem.md`
- `/home/agentuser/repo/results/imo-2026-03/lemmas/case-b2-n3-covering-closure.md`
- `/home/agentuser/repo/results/imo-2026-03/lemmas/generalized-peel-identity.md`
