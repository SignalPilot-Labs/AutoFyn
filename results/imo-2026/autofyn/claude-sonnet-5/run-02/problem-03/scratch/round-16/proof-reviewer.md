# Round 16 adversarial review — imo-2026-03

Reviewer independently re-derived/re-verified every load-bearing new claim
below with fresh exact-`Fraction` scripts written from scratch (not the
builders' own scripts), and re-read the full text of both approach files
(not just the build reports) to check for overclaiming.

## 1. `approaches/greedy-halving-adversary.md`

**Verdict: partial / CHANGES REQUESTED.**

### New lemma: Truncated Alternating Sum Floor (`lemmas/truncated-alternating-sum-floor.md`)

Statement: for any finite multiset $S$ (total $T$) and any $v\in[0,T]$,
$$A(S)-2A(S_{>v})+2v\epsilon(v)\ge v-T.$$

Re-derived the proof line by line:
1. $A(S)=\int_0^v u_S+\int_v^T u_S$ (support argument, trivial).
2. `upper-truncation-identity` (certified round 15, and its own proof
   re-checked here too: a clean two-case argument on $N_S(x)=N_{S_{>v}}(x)$
   for $x\ge v$ and constancy of $N_{S_{>v}}$ on $[0,v)$ — correct) gives
   $\int_v^T u_S = A(S_{>v})-v\epsilon(v)$.
3. Substituting, $\int_0^v u_S = A(S)-A(S_{>v})+v\epsilon(v)$.
4. $\int_0^v u_S - \int_v^T u_S = A(S)-2A(S_{>v})+2v\epsilon(v)$ (direct
   algebra, correct).
5. Bounding via $\{0,1\}$-valuedness: $\int_0^v u_S\ge0$, $\int_v^T u_S\le
   T-v$, so the difference is $\ge 0-(T-v)=v-T$.

This is correct and genuinely elementary — no gap. Independently
re-verified with a fresh script (`/tmp/round-16-review/verify_floor.py`,
50,000 trials, random multisets $n=1,\dots,8$, random thresholds): zero
violations, matching the proof.

### Theorem 31 (closes the $\ell(F)=1$, $v<p_2$, $p_2$-untouched branch unconditionally)

Re-derived the application to Proposition 30's formula
$A(F\cup G')=p_2-v+\Psi(v)$, $\Psi(v)=A(R')-2A(R'_{>v})+2v\epsilon(v)$:
substituting $\Psi(v)\ge v-s$ (Floor lemma with $T=s$) gives
$A(F\cup G')\ge p_2-v+(v-s)=p_2-s=f(n)$ by the already-certified Lemma 24.
The algebra is exactly right and needs no hidden assumption.

I did not just re-check the algebra — I wrote an independent, from-scratch
verification of *both* Proposition 30 (round 15's identity, which Theorem
31 depends on) and Theorem 31 itself, using **generic** (non-ladder)
multisets subject only to the dominance hypothesis $p_2>\mathrm{Total}(R')$
that the proof actually uses (i.e. not restricted to the specific ladder
values, to stress-test whether the identity/inequality secretly needs more
structure than claimed):
(`/tmp/round-16-review/verify_prop30_thm31.py`, 20,000 trials each) —
**zero violations in both.** This is a stronger check than re-running the
builder's own ladder-restricted script, since it confirms the results hold
in the generality the proofs actually claim.

**Conclusion: Theorem 31 is correct, unconditional, and closes exactly what
is claimed** (items 1 and 2 of the round-15 diagnosis, upgrading
Proposition 24 to hypothesis-free as a byproduct).

### Correction to round 15's "one unified obstruction" framing

The file's round-16 addendum retracts round 15's claim that Target B (item
3, $\ell(F)=2$, $\tau_P\ge p_3$) is "the same obstruction" as items 1/2.
I checked the diagnosis: Target B's reduction needs a bound on
$\psi(t)=A(\{t\}\cup G')$ where $G'$ ranges over refinements of the **full**
tail $\{p_2,\ldots,p_{n+1}\}$ (total $r=p_2+s$), not just
$\{p_3,\ldots,p_{n+1}\}$ (total $s$) as in Theorem 31. Repeating the
Floor-lemma derivation with $S=G'$, $T=r$ gives only $\psi(t)\lesssim
2p_2$-scale slack instead of $f(n)$-scale slack — i.e. the same elementary
trick, applied to an object one level "higher" (a bigger total), produces
a bound too weak by an order of magnitude. This is worked through
algebraically in the file, not merely asserted, and I re-derived it myself
by substitution — **the diagnosis is correct**: Target B genuinely is not
closed by this mechanism, and round 15's unification claim was an
overclaim, now honestly retracted rather than repeated. The suggested
restart (peel $p_2$ first via `dominant-element-removal-identity` to
reduce Target B to a Theorem-31-shaped sub-problem on the remaining tail)
is a reasonable, concrete next step, not yet executed.

### Verdict

No gap found in any new claim. Theorem 31 is a genuine, unconditional
closure of a real branch of the lower bound's restricted Claim (B)
recursion. The whole problem remains unsolved (Target B, the general
$\ell(F)\ge2$ collapse, the $v<p_2$-with-$G'$-cutting-$p_2$ branches, and
the general upper bound are all still open, exactly as the file states).
**Status: partial. Verdict: CHANGES REQUESTED** (real progress, re-dispatch
the slug to attack Target B next, per its own recorded restart point).

## 2. `approaches/lp-duality-certificate.md`

**Verdict: partial / CHANGES REQUESTED.**

### Task 1 — sign-bug fix to `alternating-gap-cross-lemma`

The round-16 outline prescribed a one-line fix (relabel the tail prefactor
$(-1)^j\to(-1)^{j'}$). The builder found this insufficient — re-testing the
round-15 counterexample $(45,45,31,27)$ (equal pair $(45,45)$, split pair
$31\to(30,1)$ sandwiching $27$, empty tail) shows the tail-prefactor
relabeling changes nothing when the tail is empty, yet the bug persists.
The actual fix needed: the gap-sum's own per-pair sign must be indexed by
a split pair's **rank among split pairs** ($s(i_k)=k$), not its raw pair
index.

I independently reconstructed the exact counterexample
(`/tmp/round-16-review/verify_altgapcross.py`): direct computation gives
$A(M)=4$; the corrected (split-rank-indexed) formula predicts $4$; the old
buggy (raw-index) formula predicts $-4$. Matches the file's claims exactly.

I then wrote a broader, independent stress test
(`/tmp/round-16-review/verify_altgapcross_random.py`, 20,000 trials)
constructing random chains of split pairs (via the sandwich-interval
construction) with a random number of equal pairs inserted at **arbitrary**
positions in the sorted order (including interleaved inside the split
chain's value range, not just appended outside it, to stress the claim that
equal pairs are fully positionally harmless) — **zero mismatches** between
the corrected formula and direct computation. This is a stronger test than
the builder's own (which uses a specific sequential construction order);
it independently confirms the corrected identity, not just the one
counterexample.

**Conclusion: the fix is correct**, and the file's claim that it is
"deeper than the outline anticipated" is accurate, not a face-saving
excuse — I confirmed the tail-prefactor-only fix genuinely fails on the
cited witness.

### Task 2 — `recursive-image-escape-dead-end`

The argument: substituting "case (a)/(b1) holds for the recursed image
$S'$" into Theorem C′/B$_k$ gives exactly the ceiling $a_{n-1}T'$ — the
identical value the unrestricted induction hypothesis would supply —
because that ceiling is *tight* (attained with equality by genuine
instances at every level, traced to the fully-closed $P(2)$ base case via
the telescoping-threshold identity $a_{n-1}=a_n/(2(1-a_n))$, already
certified in round 9). I independently re-derived this telescoping identity
and confirmed the corollary's algebra
($a_nT/2+a_{n-1}T(1-a_n)=a_nT \iff a_{n-1}(1-a_n)=a_n/2 \iff
a_{n-1}=a_n/(2(1-a_n))$) reproduces exactly the cited identity — consistent
with the already-certified `bisect-containment-dead-end` and
`peel-zero-slack-dead-end`. The logical structure of Step 2 (a ceiling that
is attained with equality cannot, by that fact alone, be strengthened) is
valid reasoning, not hand-waving. This is a genuine, sound generalization
of two previously known specific dead ends into a whole-family negative
result. No gap found.

### Task 3 — grid check honesty

Checked the claim that the 212/214-point grid check is not oversold
anywhere. Grepped the full approach file (not just the build report): every
occurrence of this result (the "Approaches tried" summary, §R16.3, §R16.4)
consistently uses language like "non-rigorous", "not a proof",
"does not close case (b2)", "offered only as mild additional (non-rigorous)
corroboration". The file explicitly flags the caveat that "uncovered" grid
points are not proof of a gap (midpoint parameter choice, not optimized)
and that "covered" points only prove a lower bound on coverage, not an
upper bound on the true minimum. No location oversells this as a closure.
**Confirmed: not oversold.**

### Verdict

All three tasks' claims verified correct and honestly scoped. Open Gap 1
(case (b2), the general upper bound) remains open — neither task claims
otherwise. **Status: partial. Verdict: CHANGES REQUESTED** (genuine
progress: a correctly-fixed lemma and a new sound negative result that
forecloses a whole mechanism family; case (b2) still needs a genuinely new
idea, as the file itself states — R11.5/R12.5/R14.3's joint vertex
fixed-point obstruction is unresolved).

## Outcomes recorded

- `greedy-halving-adversary`: `verified-milestone` (Theorem 31 fully closes
  a named branch unconditionally, independently re-verified; round-15
  overclaim correctly self-corrected).
- `lp-duality-certificate`: `partial` (correct fix + sound new negative
  lemma; no new coverage of case (b2)).

Both recorded via `mcp__approach-ranker__record_outcome` for round 16.

## `current.md` update

Added a Round 16 entry to `results/imo-2026-03/current.md` summarizing both
builds' verified content, the correction to round 15's Target-B framing,
and the honest scope of all new claims. Status remains `partial` at the
whole-problem level — no overclaim found in either build that would change
this.
