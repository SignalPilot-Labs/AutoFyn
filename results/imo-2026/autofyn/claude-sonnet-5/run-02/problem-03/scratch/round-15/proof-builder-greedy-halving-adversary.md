# Round 15 build report — greedy-halving-adversary

## Status: partial (unchanged)

## What was attempted

Per the round-15 outline and the outline-reviewer's correction note:
- **Target A (primary):** close the "$v<s$" branch of the $\ell(F)=1$,
  $v<p_2$, $p_2$-untouched sub-case (which, via certified Lemma 25, also
  closes $\ell(F)=2$ sub-case (b) "for free" — this part of the reduction
  is fine and unaffected by the reviewer's correction).
- **Target B (secondary, time-boxed):** close item 3 ($\ell(F)=2$,
  $P\ne\varnothing$, $\tau_P\ge p_3$) via a cruder
  `triangle-bound-for-a`/`max-domination-lemma` combination.

## What was actually established

**New general lemma (certified-quality, not yet reviewer-certified):**
`lemmas/upper-truncation-identity.md` — for any finite multiset $S$ and
threshold $v\ge0$, $\int_v^\infty u_S = A(S_{>v}) - v\cdot\epsilon(v)$
where $\epsilon(v)$ is the parity of $|S_{>v}|$. Proved from scratch,
verified 3000 exact-`Fraction` trials, zero mismatches; also confirmed the
parity-correction term is load-bearing (a naive parity-free guess produces
mismatches whenever $|S_{>v}|$ is odd).

**New Proposition 30** (in `approaches/greedy-halving-adversary.md`): using
the Upper-Truncation Identity, extended Proposition 24's exact formula
$A(F\cup G')=p_2-v+A(R')$ (previously only valid for $v\ge s$) to an exact
formula valid for **every** $v\in(0,p_2)$:
$$A(F\cup G') = p_2-v+A(R')-2A(R'_{>v})+2v\,\epsilon(v).$$
Verified 12000 exact-`Fraction` trials (`/tmp/round-15/check_prop30.py`),
zero mismatches; consistency-checked against Proposition 24 in the $v\ge s$
limit (reduces exactly, since $R'_{>v}=\varnothing$ there). This directly
answers the reviewer's Route (i) request — a genuine exact-closed-form
extension, not a re-hash of the "two lower bounds don't combine" mistake.

**What remains open (Target A):** the formula reduces the whole item to
bounding $A(R'_{>v})$ from above — a new, precisely-named open sub-problem
("bound the alternating sum of the top-truncated portion of a legal
$(n-2)$-ladder response"), not an instance of any existing certified lemma.
Showed by direct computation that the trivial `max-domination-lemma` route
($A(R'_{>v})\le\max(R')\le s$) is far too weak (gives a negative, useless
lower bound on $A(F\cup G')$ for small $v$). **Not closed.**

**Target B: negative/diagnostic result, not a closure.** The outline's
suggested crude combination fails: found a concrete $n=3$ counterexample to
its key sub-bound ($\psi(p_3)=1/5>p_3=2/15$ when $G'=\tau$ is left
untouched), traced this to a likely **notational inconsistency in the
existing certified `proposition-29b-partial-closure.md`** (its proof's "$G'$"
appears to silently exclude $p_2$, contradicting the surrounding setup where
$G'$ is the full tail refinement) — flagged for a future audit, not
retracted (no counterexample to Prop 29b's actual stated conclusion was
found). A minimum-margin numeric search
(`/tmp/round-15/margin_check.py`) found the outline's "$17\times f(n)$
generous slack" claim is inaccurate at small $n$: margins as small as
$0.002$–$0.004\times f(n)$ at $n=3,4$ (only growing for $n\ge5$). Two
further mechanisms were tried (Theorem-29-style enlarged-split bound; the
Proposition-26-style monotonicity/shift argument) and both were shown to
reduce to the **same** unresolved "top-truncated upper bound" fact as
Target A's open item — a genuine structural finding: items 1, 2, and 3 are
one obstruction, not three. **Not closed this round**, time-boxed per the
outline's own instruction.

## Recommendation for round 16

Focus the whole population's Claim-(B) effort on the single isolated
target: an upper bound on $A(S_{>v})$ for $S$ a legal $(n-2)$-ladder
response and $v\in(0,\mathrm{Total}(S))$ arbitrary (equivalently, on
$A(R'_{>v})$ in Proposition 30's notation). Resolving this is now known to
close items 1, 2 (via certified Lemma 25), and 3 (via the reductions traced
this round) simultaneously. A secondary, lower-priority item: audit
`proposition-29b-partial-closure.md`'s proof for the flagged $G'$/$p_2$
notational inconsistency (does not currently threaten its certified
conclusion, but the stated mechanism looks locally inapplicable as written
when $p_2$ remains part of the refined tail).

## Files changed
- `results/imo-2026-03/approaches/greedy-halving-adversary.md` — new
  "Approaches tried" entry, new "Current best" round-15 update, new
  "Proposition 30" and "Target B" write-up sections.
- `results/imo-2026-03/lemmas/upper-truncation-identity.md` — new general
  lemma (not yet reviewer-certified).

## Scripts (exact-Fraction verification, not proofs)
- `/tmp/round-15/check_upper_truncation.py` — Upper-Truncation Identity,
  3000 trials, 0 mismatches.
- `/tmp/round-15/check_prop30.py` — Proposition 30's formula, 12000 trials,
  0 mismatches (with parity term); 3585/12000 mismatches confirming the
  parity term is load-bearing (without it).
- `/tmp/round-15/check_target_b3.py` — Target B's target inequality itself
  (correct cut-budget respected), 20000 trials, 0 violations (supports the
  conjecture, does not prove it).
- `/tmp/round-15/margin_check.py` — minimum-margin search for Target B,
  found tight margins at $n=3,4$ contradicting the outline's slack claim.
