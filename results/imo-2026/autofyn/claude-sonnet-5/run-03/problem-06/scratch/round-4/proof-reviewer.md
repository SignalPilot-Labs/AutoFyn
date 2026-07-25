# Proof review — imo-2026-06, round 4

Reviewed 4 built approaches per dispatch: `state-compactness-pigeonhole.md`
(new §11), `active-set-stabilization.md` (Nec-Necessity Lemma),
`jacobsthal-covering-bound.md` (bounded-enlargement Λ^(K)),
`renormalization-induction-on-seed.md` (Third-Term Dichotomy Lemma).

All 4 self-report `Status: partial`. Independent verdict for all 4:
**correct self-assessment** — none overclaims, none is fatally broken.
Verdicts below, one per approach.

---

## 1. state-compactness-pigeonhole — Verdict: CHANGES REQUESTED (Status: partial, confirmed)

**§10 (Hitting-Set Lemma).** Reframes the Unified Central Claim as: $Q$
works iff $Q$ hits every $W(i,j):=R(a_i)\cap R(a_j)$. Re-derived by hand —
correct, a one-line unwinding of definitions, no gap. Free corollary
(index-1 pairs always hit) also checked and correct.

**§11.1 special cases** (index-1 pairs, adjacent pairs both hit by
$[2,\mathrm{rad}(a_1)]$): re-derived from `adjacent-link-lemma.md` and
`prime-factors-a1-cover-forever.md`; both correct, short, no gap.

**§11.3 — the load-bearing claim: $a_1=375$ refutes $Q^\star=\{p\le
\mathrm{rad}(a_1)\}$.** This is the round's most consequential specific
claim (a counterexample that kills a promising-looking universal
candidate), so I independently re-derived the sequence from scratch in
Python (exact integer arithmetic, greedy simulation, no reliance on the
builder's arithmetic):
```
a1..a7 = 375, 378, 380, 384, 390, 396, 399
factorizations: 375=3·5^3, 378=2·3^3·7, 380=2^2·5·19, 384=2^7·3,
                390=2·3·5·13, 396=2^2·3^2·11, 399=3·7·19
gcd(a3,a7) = gcd(380,399) = 19
```
This matches the builder's hand-computation term-for-term, including every
intermediate rejected candidate's factorization. $19 > \mathrm{rad}(375)=
15$, and the primes $\le15$ dividing $a_3$ ($\{2,5\}$) and $a_7$
($\{3,7\}$) are disjoint. **The counterexample is correct and rigorous** —
a genuine, checked negative result, not overclaimed (it does not refute
the general existence of *some* finite $Q$, only this specific closed
form; the builder is explicit about this in §11.4, and I confirm this
distinction is accurately drawn).

**§11.5(b) Chain-Transitivity Obstruction.** Pure set theory
($\sigma_1\cap\sigma_2\ne\emptyset$, $\sigma_2\cap\sigma_3\ne\emptyset$
does not imply $\sigma_1\cap\sigma_3\ne\emptyset$); the 3-set
counterexample $\{1,2\},\{2,3\},\{3,4\}$ is elementary and correct.

**Gap remaining.** The central existence question (does *some* finite
self-sufficient $Q$ exist, for every $a_1$?) is completely untouched —
correctly and explicitly acknowledged by the builder. Status `partial` is
correct; no overclaim.

**Certified 4 new lemmas:** `hitting-set-lemma.md`,
`bounded-radical-special-cases.md`, `bounded-radical-refutation.md`
(negative), `chain-transitivity-obstruction.md` (negative).

---

## 2. active-set-stabilization — Verdict: CHANGES REQUESTED (Status: partial, confirmed)

**Nec-Necessity Lemma.** Definition: $p\in\mathrm{Nec}$ iff some pair
$i<j$ has $R(a_i)\cap R(a_j)=\{p\}$ (unique common prime). Claim: any
finite self-sufficient $Q$ must contain $\mathrm{Nec}$.

*Independent re-derivation:* if $Q$ is self-sufficient, $a_i,a_j$ (the
witnessing pair for $p\in\mathrm{Nec}$) share a prime $q\in Q$; but
$R(a_i)\cap R(a_j)=\{p\}$ has only one element, forcing $q=p$, so $p\in
Q$. This is correct, exactly as stated — a genuine two-line argument.
**Non-circularity check:** the lemma is conditional on "*if* a finite
self-sufficient $Q$ exists," never assumes it does, never assumes
periodicity, and $\mathrm{Nec}$ is defined purely from the true sequence
with no reference to any candidate $Q$. No circularity found.

**Monotonicity of self-sufficiency under enlargement** — trivial,
correct, one line.

**$Q_{\min}:=\mathrm{Nec}\cup R(a_1)$ stress test at $a_1=194287=
37\cdot59\cdot89$.** Independently re-simulated from scratch in Python
(greedy simulation to 300 terms, `sympy.primefactors`, exhaustive
all-pairs check, not sampled):
```
R(a1) = {37, 59, 89}
Nec   = {2, 3, 17, 37, 59, 89, 103}   (matches table exactly)
bad pairs among 44850 pairs checked = 0
```
Also re-verified the smaller-seed rows of the table ($a_1=35,65,99,77,
15,21$) — all match the builder's stated $\mathrm{Nec}$ sets and
zero-bad-pairs claims exactly. The claim that the recruited prime $103$
exceeds $89=\max R(a_1)$ (refuting a size-bound conjecture) is also
confirmed correct.

**Gap remaining.** The assigned Sperner-exchange step from round 3 is
left explicitly open (honestly reported as neither proved nor refuted).
The central question — is $\mathrm{Nec}$ always finite, and is
$Q_{\min}$ always self-sufficient? — remains fully open; only numerical
evidence given, correctly flagged as such. Status `partial` correct.

**Certified 1 new lemma file** (bundling both results):
`nec-necessity.md`.

---

## 3. jacobsthal-covering-bound — Verdict: CHANGES REQUESTED (Status: partial, confirmed — correctly NOT solved, and correctly NOT overclaiming the Λ^(K) mechanism)

Confirmed the builder does not overclaim: §7.2's own text explicitly
states neither an a priori bound on $K(a_1)$ nor a stabilization criterion
was found, and explicitly distinguishes this ("not falsified... but not a
closing argument") from the three previously-refuted mechanisms. This
honest framing is accurate; the file's own `## Status` is `partial`, not
`solved` — no gate violation.

**§7.0 counterexamples re-checked.** $a_1=35$: $\Lambda=\{2,3,5\}$ vs
$Q_0=\{5,7\}$, $7\notin\Lambda$ — correct, trivial. $a_1=99$: I
re-simulated the sequence independently:
```
a1..a5 = 99, 102, 105, 108, 110
```
**Found an error:** the builder writes the witnessing pair as
"$(a_2,a_4)=(105,110)$", but $105=a_3$ and $110=a_5$ in 1-indexed terms
(not $a_2=102$, $a_4=108$; indeed $\gcd(a_2,a_4)=\gcd(102,108)=6$, *not*
a counterexample). The underlying mathematical content — $\gcd(105,110)=
5\notin\Lambda\cup Q_0=\{2,3,11\}$ — is correct, just mislabeled by
index. This is a transcription error, not a logical flaw: it does not
change any conclusion drawn from it (the claim "$\Lambda\cup Q_0$ fails
for $a_1=99$" survives with the corrected indices $(a_3,a_5)$). I
certified the corrected version as `adjacent-link-neighborhood-insufficient.md`
and flagged the error explicitly in `current.md` so the source approach
file can be fixed next round.

**§7.1 numerics** (search $3\le a_1\le1500$, stress to $30030$, finding
some finite $K\le8$ works in every tested case) — a computational claim
I did not fully reproduce (would require re-running the full sweep,
outside this review's scope), but it is reported honestly as evidence,
not proof, consistent with rubric.

**Gap remaining.** No a priori bound on $K(a_1)$; no stabilization
criterion. The Λ^(K) mechanism is *not* proven to work and *not* proven
to fail — this is accurately reflected in the file's own `Status:
partial` and the "Full proof" section correctly states "Not present."
No RETHINK warranted (unrefuted candidate, real narrowing of the search,
not a dead mechanism), but also no forward lever found this round beyond
what round 3 already had — closest to a plateau among the four.

**No new lemma certified from this file beyond the index-corrected one
above** (§7.1's numerics are evidence, not a provable lemma yet).

---

## 4. renormalization-induction-on-seed — Verdict: CHANGES REQUESTED (Status: partial, confirmed)

**§3 base case (prime-power seeds).** Induction proof that $a_1=p^k
\Rightarrow T=1,L=p$. Re-derived by hand: correct, elementary, no gap —
the key step (any candidate not divisible by $p$ is invalid because
$R(a_1)=\{p\}$ singly determines validity against $a_1$; any multiple of
$p$ is automatically valid against every earlier term, all of which are
multiples of $p$ by IH) is airtight.

**§4.2 Third-Term Dichotomy Lemma — the load-bearing claim.**
Independently re-derived the case split (Type P / Type non-P via
$p\mid m$ or not) from scratch: matches the builder's proof exactly, and
I additionally ran an independent brute-force check comparing the
closed-form prediction against direct greedy simulation for **all 66
squarefree pairs $p<q\le37$**:
```
mismatches = 0  (fresh Python re-implementation of both the formula
                  and the simulator, not reusing the builder's code)
```
This confirms the formula is correct, not merely "checked by the
builder."

**§4.3 instances.** Re-simulated $a_1=35$ (sequence
$35,40,42,45,50,60,70,75$) and $a_1=65$ (sequence $65,70,75,78,80,90,
100,105$) from scratch — both match exactly, including the claimed
$a_4=78\ne a_3+5=80$ for $a_1=65$ (independently verified: $78=2\cdot3
\cdot13$ passes $\gcd$ against all of $65,70,75$; $76,77$ both fail
against $65$). This is a correct, new, decisive negative instance.

**Gap remaining.** The general inductive step (arbitrary $\omega(a_1)$,
arbitrary index) is honestly left open; both a naive and a
bounded-lookahead strengthening are proved false by explicit instance,
not by unfounded assertion. §5's "revised, still-open target" is
correctly flagged as unproved, not conflated with a result. Status
`partial` correct.

**Certified 3 new lemmas:** `prime-power-base-case.md`,
`third-term-dichotomy-lemma.md`, `bounded-lookahead-insufficiency.md`
(negative).

---

## Overall

No approach reaches `solved` this round; no approach is fatally broken
(`RETHINK`) — all four made real, independently-verified progress and are
routed `CHANGES REQUESTED`. Genuine highlights: (a) state-compactness's
$a_1=375$ refutation closes off the single most promising-looking
closed-form shortcut population-wide; (b) active-set-stabilization's
Nec-Necessity Lemma gives, for the first time, a fully explicit
(non-existential) candidate $Q_{\min}$ for the central gap; (c)
renormalization-induction-on-seed (a genuinely different architecture,
opened last round per the plateau-break rule) now has real machinery
(exact third-term formula) rather than only a refuted naive idea. One
transcription error was found and corrected (jacobsthal-covering-bound's
mislabeled $a_1=99$ witness indices) — mathematically inconsequential but
worth fixing in the source file next round.

`results/imo-2026-06/current.md` updated: `## Status` remains `partial`;
`## Approaches tried` appended with round-4 entries for all four
approaches; `## Current best` updated to the sharper $Q_{\min}=
\mathrm{Nec}\cup R(a_1)$ formulation of the central gap plus the two new
confirmed-dead routes (bounded-radical closed form, chain-transitivity
induction); `## Full proof` still absent (correctly, since unsolved), now
restated in the sharper $\mathrm{Nec}$/$Q_{\min}$ terms.

9 new lemma files certified in `results/imo-2026-06/lemmas/`:
`hitting-set-lemma.md`, `bounded-radical-special-cases.md`,
`bounded-radical-refutation.md` (negative),
`chain-transitivity-obstruction.md` (negative), `nec-necessity.md`,
`prime-power-base-case.md`, `third-term-dichotomy-lemma.md`,
`bounded-lookahead-insufficiency.md` (negative),
`adjacent-link-neighborhood-insufficient.md` (negative, index-corrected
from the source approach file).

Ranker outcomes recorded (round 4): state-compactness-pigeonhole
(advanced, Elo→~1606), active-set-stabilization (advanced, Elo→~1571),
jacobsthal-covering-bound (partial, Elo→~1450), renormalization-induction-on-seed
(advanced, Elo→~1489).

**Recommendation for round 5:** the central gap is now sharpest in the
$Q_{\min}=\mathrm{Nec}\cup R(a_1)$ formulation (active-set-stabilization).
Two closed-form/induction shortcuts are now confirmed dead
(bounded-radical, adjacent-chaining) — do not retry either. The
renormalization architecture is the most promising source of a *genuinely
different* lever (not more Q-construction variants) if the general
inductive step can be attacked; jacobsthal's Λ^(K) mechanism, while not
dead, has gone two rounds with no forward lever and should either get a
sharply new idea (e.g. attacking finite-stabilization directly) or be
deprioritized relative to the other three.
