# Round 22 proof-reviewer report — imo-2026-03

Scope: adversarial, independent re-verification of round-22 additions to
`greedy-halving-adversary.md`, `rank-pigeonhole-budget.md`, and
`lp-duality-certificate.md`, plus the lemmas proposed for certification.
All numeric claims below were re-checked with fresh scripts written by
this reviewer (`/tmp/round-22/verify_gha.py`, `verify_rpb_77.py`,
`verify_lpd_r22b.py`), not the builders' own.

## 1. `greedy-halving-adversary`

**General Cross-Level Rescaling Lemma.** Statement:
$p_{k+i}=\lambda_kq_i^{(m)}$, $\lambda_k=f(n)/f(m)$, $m=n-k$. Re-derived
the algebra by hand (matches) and re-verified exactly with a fresh script
for $n=2,\dots,9$, all $k=0,\dots,n-1$ — zero discrepancies. Correct,
general, no gap.

**Theorem 36b** ($A(R')\ge f(n)$, conditional on $(\star_{n-2})$, for the
*whole* $R'$ uniformly across Case (a)/(b)). Checked the proof step by
step: applies the Rescaling Lemma at $k=2$, uses $n-3<n-2$ to stay within
budget, invokes $(\star_{n-2})$ (the standing hypothesis, applied to the
whole rescaled object, not a two-variable statement one level down), and
homogeneity (certified Lemma 9). Confirmed this correctly sidesteps the
two-variable circularity Round 20 flagged (that circularity required the
*full* $\Delta$-curve one level down; Theorem 36b only needs the
one-variable lower bound). Independently re-verified the *conclusion*
numerically with a freshly-written random-legal-refinement generator
(distinct composition-and-cut-point sampler from the builder's own):
$n=4,\dots,8$, minimum sampled margin $0,0,\approx0.0001,\approx0.0003,
\approx0.0045$ — all $\ge0$, matching the builder's reported order of
magnitude. No gap found.

**Corollary 36c.** Trivial two-line consequence ($v<\min(R')\Rightarrow
R'_{>v}=R'\Rightarrow\Delta(n,v)=-A(R')$); matches the file's own
definition $\Delta(n,v):=A(R')-2A(R'_{>v})$ exactly. Correct, closes a
genuinely new sub-range for $n\ge5$ (honestly scoped: does NOT close
Case (b) in full for any $n\ge5$).

**Insert-Element Identity.** $A(\{b\}\cup T')=2A(T'_{>b})-A(T')+(-1)^jb$.
Independently re-derived the rank-shift proof from scratch (matches the
builder's) and independently re-verified with $20{,}000$ fresh
exact-`Fraction` trials (random multisets, sizes 0–6) — zero mismatches.
Confirmed: this is a genuinely general, proved identity, **not** merely a
numerically-checked conjecture (task instruction 1 specifically asked for
this distinction). Its diagnostic use (no one-sided lower bound on
$A(T')$ can close the "$v\ge a$" branch, since $A(T')$ enters with a minus
sign) is a correct, general structural argument.

**Theorem 35b fix + Theorem 35b$'$.** The Round-22 fix correctly replaces
a false "$D_{n-3}f(n-3)=2^{n-3}$" step with the trivial-but-correct
$D_{n-3}f(n-3)=1$ (immediate from $f(m):=1/D_m$) — re-derived and
confirmed, no downstream consequence (the file's own honest account is
accurate). Theorem 35b$'$ then correctly observes Theorem 35b's own proof
already forces $R'_{>v}=\varnothing$ for all $v\ge p_3$ (re-traced this
line-by-line: the argument never actually used $v=p_3$, only $v\ge p_3$),
so $\epsilon\equiv0$ there and $(\Diamond')$ trivially coincides with the
already-proved $(\Diamond)$. Correct, closes "step 4" as claimed, no gap.

**Verdict: CHANGES REQUESTED.** Genuine, verified, honestly-scoped
progress; no RETHINK-triggering issue found; target not closed.

5 lemmas certified: `general-cross-level-rescaling-lemma`,
`insert-element-identity`, `theorem-36b-whole-r-prime-lower-bound`
(Theorem 36b + Corollary 36c bundled), `theorem-35b-prime-epsilon-
vanishing`.

## 2. `rank-pigeonhole-budget`

**§7.7 equivalence $(\sharp')\iff(\Diamond')$ at fixed $v_2$.** Re-derived
the algebraic identity $\mathrm{marg}_{\sharp'}(v_1,v_2)-\mathrm{marg}_{
\Diamond'}(v_2)=s-v_1+f(n)=p_2-v_1$ (using $s+f(n)=p_2$) by hand — matches
exactly. Checked **both** directions of the claimed "iff," per the task's
specific instruction:

- ($\Leftarrow$): trivial, since $p_2-v_1>0$ strictly on the whole domain
  ($v_1<p_2$). Correct.
- ($\Rightarrow$): the substantive direction — given $(\sharp')$ holds for
  *every* admissible $v_1$ at fixed $v_2$, and the identity
  $\mathrm{marg}_{\Diamond'}(v_2)=\mathrm{marg}_{\sharp'}(v_1,v_2)-(p_2-v_1)$
  holds for *every* individual $v_1$ (it is an identity, not an
  inequality), taking $v_1\to p_2^-$ gives $\mathrm{marg}_{\Diamond'}(v_2)
  =\lim_{v_1\to p_2^-}\mathrm{marg}_{\sharp'}(v_1,v_2)\ge0$ since it's a
  limit of a quantity that is $\ge0$ throughout an interval approaching
  the limit point. This is a valid, non-circular limiting argument (the
  admissible $v_1$-domain genuinely approaches $p_2$, since $v_1\in
  (s,p_2)$ is open at $p_2$). Correct.

Independently re-verified identity (7.7.1) itself with a fresh
$50{,}000$-trial exact-`Fraction` script at $n=4$ (random legal
budget-1 refinements, random admissible $v_1,v_2$): zero mismatches
between the computed difference and the predicted $p_2-v_1$; also
independently confirmed both sampled margins stay non-negative (min
$\mathrm{marg}_{\Diamond'}\approx8\times10^{-8}$, min $\mathrm{marg}_
{\sharp'}\approx6\times10^{-4}$), consistent with (not a substitute for)
the still-open target.

**Verdict: CHANGES REQUESTED.** A genuine, correctly-proved-both-
directions equivalence — real content, honestly not claimed to close
anything. Claim (A) remains `solved`/APPROVE, unaffected. No lemma
certified this round (§7.7 is explicitly a conditional stub).

## 3. `lp-duality-certificate`

**$p$-space Chamber-Vertex Theorem (Lemma R22.1 + Theorem R22.2, items
1–2).** The polyhedral characterization of $U$ and the vertex-attainment
argument (Minkowski–Weyl + convex combination) are standard and correctly
executed; the file honestly flags the one real subtlety (condition (c)'s
justification against a competing type $\tau'$ with singular $M(\tau')$,
inherited from R20.4's unresolved "residual coincidence" sub-case) rather
than hiding it. Certified as a conditional theorem.

**R22.3 refutation of the box-corner $\times$ tail-vertex decomposition.**
Independently re-implemented the $n=3$ comparison from scratch with a
different parameterization (sigmoid-mapped split ratios, Nelder–Mead, 12
restarts/composition) and the correct transform $\Phi_{\min}=(A+T)/2$
(cross-checked against the builder's own worked example, $\tau^\star$'s
closed form $p_1/2+p_3+p_4$ — exact match at the given point). Result:
unrestricted-box witness $\Phi_{\min}\approx0.5128$ (margin
$\approx0.02053$), corner-restricted witness $\Phi_{\min}\approx0.5020$
(margin $\approx0.03133$) — matching the builder's reported values to
full precision and confirming the corner is genuinely **not** the worst
case (margin strictly smaller off-corner). Also independently
cross-checked the two cited exact-`Fraction` values ($641/1250$,
$5159/10001$) against $a_3=8/15$ exactly. **Correct, honestly scoped**
(explicitly limited to $n=3,4$). Certified as the ninth confirmed-dead
mechanism.

**R22.2 "strict-Box compactness fix" Corollary (item 3) — genuine
overclaim found.** Per the task's specific instruction to scrutinize this
polyhedron/compactness argument hard: the Corollary claims all three Box
walls ($p_1=T/2$, $p_2=a_nT/2$, $p_2=T/D_n$) are boundaries of
"already-unconditionally-closed adjacent region[s]," and states this fix
is "unconditional and general... it does not depend on $n$." **This is
false**, confirmed by cross-referencing the *same approach file's own*
earlier, repeatedly-stated record:

- `lp-duality-certificate.md` §4 ("$p_1\ge T/2$ closed rigorously and
  unconditionally for $n\le3$") and its Round-9 write-up explicitly state
  "giving a genuine, complete closure of $p_1\ge T/2$ **only for
  $n\le3$**" — extending past $n=3$ requires the $p_1<T/2$ regime (case
  (b2) itself!) closed one level down first, a genuine coupling the file
  itself diagnosed and never retracted.
- The same file's Round-19 re-confirmation list labels case (a)'s closure
  ($p_2\ge a_nT/2$) explicitly as resting on "the **actual** induction
  hypothesis value $\Phi_{\min}(S')\le a_{m-2}T'$" — i.e. conditional on
  the same standing strong-induction hypothesis as everything else, not
  "already-unconditionally-closed" at every $n$ in an absolute sense.
- Only the third wall (case (b1), $p_2\le T/D_n$, via the fully general,
  elementary Max Domination Lemma) is genuinely unconditional for every
  $n$.

So the Corollary, and the certified-lemma draft `lemmas/p-space-chamber-
vertex-theorem.md` (item 3, and its "Honest scope" paragraph's
"unconditional and general" sentence) both overclaim. This does **not**
invalidate items 1–2 (the vertex theorem itself, which I certify as
correct and conditional as stated), and it is a **non-fatal**,
easily-fixed citation-consistency bug (the Corollary's mechanism —
boundary-sharing — is the right idea; it just needs its two borrowed
inputs correctly scoped as "$n\le3$ unconditional, else conditional")
rather than a flaw in any new mathematics this round. This is exactly the
kind of "looks standard but has a subtle gap" issue this project watches
for, caught here by cross-referencing the file's own prior sections
rather than by finding an error in the new proof text itself.

**Action taken:** appended a reviewer correction note to
`lemmas/p-space-chamber-vertex-theorem.md` (not deleted — items 1–2
certified, item 3 flagged and rescoped) recommending the round-23 fix;
fully certified `lemmas/box-corner-tail-vertex-decomposition-refuted.md`
with an added verification note.

**Verdict: CHANGES REQUESTED.** Real, mostly-correct progress with one
genuine overclaim found and corrected; target (case (b2), hence the
general upper bound) not closed.

## `current.md` updates

Appended a Round 22 entry (at the true end of the file, after Round 20 —
Round 21's own entry was already misplaced earlier in the file by a prior
round, between Round 14 and Round 15; not re-ordered here to keep the
diff minimal and avoid touching content outside this round's scope).
`## Status` remains `partial` (no change — the whole `imo-2026-03`
problem, general $n$ both directions, is not solved; only $n=1,2$ in full
and Claim (A) in full are closed). Recorded all three round-22 outcomes
via `record_outcome` (all `partial`).

## Summary table

| Slug | Verdict | Notes |
|---|---|---|
| `greedy-halving-adversary` | CHANGES REQUESTED | 5 new lemmas certified, no gaps found, genuine new Case (b) sub-range progress for $n\ge5$ |
| `rank-pigeonhole-budget` | CHANGES REQUESTED | §7.7 equivalence verified both directions, correct; conditional stub, no lemma to certify |
| `lp-duality-certificate` | CHANGES REQUESTED | Chamber-Vertex Theorem sound (conditional); R22.3 refutation independently confirmed correct; **found and corrected a genuine overclaim** in the compactness-fix Corollary (item 3) via cross-reference to the file's own prior record — non-fatal, flagged not deleted |

No RETHINK, no APPROVE this round. `imo-2026-03` overall status remains
`partial`.
