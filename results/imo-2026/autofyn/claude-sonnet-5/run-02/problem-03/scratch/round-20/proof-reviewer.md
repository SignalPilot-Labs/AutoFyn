# Round 20 proof-reviewer report — imo-2026-03

Two slugs reviewed independently: `rank-pigeonhole-budget` and
`greedy-halving-adversary`. Both were checked by hand-rederivation of the
key algebraic identities plus fresh, independently-written exact-`Fraction`
scripts (not the builders' own scripts, per the standing rule).

---

## 1. `rank-pigeonhole-budget` — §7.5 n=3 middle-band boundary fix

**Claim under review.** "Fixed the §7.5 n=3 middle-band v2=p4 boundary case
relabel (pure case-boundary fix, no new inequality)" — closing the flagged
round-19 non-fatal bug: at v2=p4, the old case split wrongly computed
τ_{>v2}=τ (both p3,p4 "exceed" v2) when the file's own strict-`>` convention
requires τ_{>p4}={p3} only.

### 1a. The narrow claim: case split exhaustive/disjoint, boundary correct

Verified independently, by hand and by script:

- New split: `v2>=p3`, `v2∈[p4,p3)`, `v2<p4`. Since p4<p3 (ladder), this is
  exhaustive and pairwise disjoint on [0,s) with no gap or overlap, matching
  the file's strict-`>` convention for τ_{>v2} at both boundary points.
- Re-derived every one of the three cases' formulas from scratch:
  - v2>=p3: τ_{>v2}=∅, Δ=A(τ)=p4=f(3). Bound s-(v1-v2) > f(3) — confirmed by
    hand algebra (uses v1<p2, v2>=p3, and Lemma 24's p2-s=f(3)).
  - v2∈[p4,p3) (the fixed case, including its new left endpoint v2=p4):
    τ_{>v2}={p3} uniformly, Δ=p4-2p3=-3p4. Confirmed directly at v2=p4
    exactly by script: `Delta=-1/5=-3p4` (D=15 ladder), matching the
    formula, not the old (wrong) `-p4`.
  - v2<p4: τ_{>v2}=τ, Δ=-A(τ)=-p4. Confirmed by hand.
- Independent 200,000-trial exact-`Fraction` script over the full domain
  (v1∈(s,p2), v2∈(p2-v1,s)): zero violations of (♯), min margin
  ≈0.000278>0, matching the file's own claimed slack.

**This narrow claim is correct.** The relabel is exactly as described: a
pure case-boundary fix, no new inequality invoked, and it genuinely
resolves the round-19-flagged bug (previously it "accidentally" proved a
stronger bound at that one point; now the boundary is handled by its
correct, weaker-but-still-sufficient formula).

### 1b. A deeper, PRE-EXISTING gap found in $(\sharp)$'s own definition (new finding, not addressed this round)

While re-deriving the bridge from $(\sharp)$ to the actual game target
$A(F\cup G')\ge f(n)$ from scratch (to independently confirm §7.5's
significance, not just its internal algebra), I found that $(\sharp)$ as
stated in this file —
$$\Delta(n,v_2)\ \le\ s-(v_1-v_2)$$
— is **not** the exact necessary-and-sufficient condition for the true
target. Re-deriving `greedy-halving-adversary`'s own exact identity (Theorem
34 corrected, "the reduction to Δ(n,v)") from scratch gives the precise
condition
$$\Delta(n,v_2)\ \le\ s-(v_1-v_2)-2v_2\,\epsilon(v_2),\qquad
\epsilon(v_2)=\mathbb1[|R'_{>v_2}|\text{ odd}],$$
i.e. exactly the sibling's own $(\Diamond')$ (in this file's $s$-based
normalization). $(\sharp)$ as written **omits the $-2v_2\epsilon(v_2)$
term**, so it is strictly weaker than the true requirement whenever
$\epsilon(v_2)=1$ — the same epsilon-bridge gap `greedy-halving-adversary`'s
own file explicitly and honestly flags for its own Theorem 34/35 (this file
never states or acknowledges this caveat for $(\sharp)$ anywhere in §7).

**This gap is not vacuous at n=3.** I checked directly: in §7.5's own
"middle" sub-case $v_2\in[p_4,p_3)$, $\tau_{>v_2}=\{p_3\}$ has size 1
(odd) — so $\epsilon(v_2)=1$ **throughout that entire sub-case**, not at
isolated points. Proving $(\sharp)$ there does *not* logically establish
the exact epsilon-aware target.

I then checked whether the true target nonetheless holds in this zone (it
might, even though the written proof doesn't establish it): by hand,
$s-(v_1-v_2)-2v_2 \ge \Delta=-3p_4$ reduces to $v_1+v_2\le6p_4$, which does
follow (strictly) from $v_1<p_2=4p_4$ and $v_2<p_3=2p_4$ in this sub-case.
I confirmed this both algebraically and with an independent
end-to-end script that builds the actual game state
$F=\{v_1,v_2,w,w\}$ ($w=(p_1-v_1-v_2)/2$, the pair forced by mass
conservation at the n=3 budget) and $G'=\{p_3,p_4\}$ (untouched, forced),
computing $A(F\cup G')$ directly (not via the $\Delta$ shortcut): over
~122,000 trials restricted to the $\epsilon=1$ sub-case, **zero violations**
of $A(F\cup G')\ge f(3)$ (min margin ≈0.000136 > 0).

**Net verdict on this point:** the true mathematical claim (n=3's middle
band closes) does hold, but **§7.5's written proof does not establish it**
— it proves $(\sharp)$, which is strictly weaker than the true requirement
in exactly the sub-case that occupies the whole "middle" interval. Calling
this "unconditional exact closure at n=3, no numerics needed" is an
overclaim: it should read "closes the sufficient-when-$\epsilon=0$ condition
$(\sharp)$ unconditionally; the $\epsilon=1$ instance (which is the *entire*
middle sub-range $v_2\in[p_4,p_3)$) is verified only numerically, mirroring
the sibling's own honestly-flagged bridge gap, not yet proved algebraically
here." This is a real, previously-uncaught gap (round 19's reviewer only
caught the relabel bug, not this deeper issue in $(\sharp)$'s own
derivation) — it does not undo the round-20 relabel fix (which is correct
on its own narrow terms), but it means the round-20 header's framing of
§7.5 as a complete, gap-free closure is not accurate.

### 1c. Effect on the file's own Status

Per this file's own scope note (repeated every round since round 5/8),
§7 is explicitly *outside* Claim (A) — the file's own declared target,
which remains fully proved (achievability + Case I + Case II, all
previously reviewer-APPROVEd and unaffected by anything in §7). The
Status header "solved" (scoped to Claim A) is accurate and unaffected by
the §7.5 gap found above.

**Verdict: APPROVE** for the file's own Status (`solved`, scoped to Claim
(A) — unaffected, already-terminal). **The §7.5 contribution itself is
downgraded from "closed" to "partial"** in `current.md`: the boundary
relabel is a genuine, correct fix, but the underlying $(\sharp)$ target
inherited from round 19 is missing the epsilon-correction term, so the true
n=3 middle-band closure is not yet algebraically complete (numerically
confirmed only). Next round should either (a) redo §7.5 with the
epsilon-aware target $\Delta(n,v_2)\le s-(v_1-v_2)-2v_2\epsilon(v_2)$
directly (the n=3 case looks tractable — the ε=1 sub-case's slack, ≈0.06 in
absolute terms, is not razor-thin), or (b) explicitly adopt
`greedy-halving-adversary`'s own end-to-end verification style (bypass the
$\Delta$ abstraction entirely and bound $A(F\cup G')$ directly) to sidestep
the bridge issue altogether.

**Promotable lemmas.** The `truncated-alternating-sum-ceiling` lemma
(§7.1, $A(S)-2A(S_{>v})\le v$ for any nonnegative multiset $S$, any
$v\ge0$) is correct, general, and elementary — independently re-derived and
re-verified (300,000+ trials, zero violations, equality case confirmed at
$S=\{v\}$). **CERTIFIED** — write to `lemmas/truncated-alternating-sum-ceiling.md`
if not already present (already listed as certified in round-19 current.md
notes; confirming it remains valid). The §7.5 n=3 "closure" itself is
**NOT** certified as a standalone lemma (it proves $(\sharp)$, a
non-equivalent, weaker statement, not the true middle-band target) —
flagged, not promoted.

---

## 2. `greedy-halving-adversary` — Theorem 36: Case (b) closed at n=3, n=4

**Claim under review.** Theorem 35's "$p_3$ is cut" branch (Case (b)) is
closed unconditionally at n=3 (vacuous, budget=0) and n=4 (new Theorem 36,
direct finite computation, budget=1).

### 2a. n=3 vacuity

Independently re-derived: at n=3 the corrected Theorem-34 cap gives $R'$ at
most $n-3=0$ cuts. Splitting $p_3=\{a,b\}$ with $a,b>0$ requires $\ge1$
cut. **Confirmed: Case (b) cannot occur at n=3** — every legal $R'$ has
$p_3$ untouched (in fact $R'=\{p_3,p_4\}=\tau$ exactly, forced). This
matches `rank-pigeonhole-budget`'s own independent §7.5 finding (same n-3=0
forcing), a good cross-consistency check between siblings. **Correct.**

### 2b. n=4 case split and Δ(4,v)≤v-f(4) — independently re-derived from scratch (not the builder's script)

At n=4, budget for $R'$ is $n-3=1$, so Case (b) forces the single cut onto
$p_3$ (splitting it into $\{a,b\}$, $a\ge b>0$, $a+b=p_3$) and $T'=\{p_4,
p_5\}$ untouched — I re-derived this forcing directly (splitting into 3+
pieces needs $\ge2$ cuts on $p_3$ alone, exceeding the budget of 1; using
the 1 cut elsewhere on $p_4$ or $p_5$ instead would leave $p_3$ untouched,
i.e. Case (a), not Case (b)). Correct and exhaustive.

Normalizing $u:=f(4)=p_5$ ($D=31$, $p_3=4u,p_4=2u,p_5=u$), I wrote a fresh
verification script (structurally independent of the builder's — I
re-derived and checked every one of the ten closed-form sub-range formulas
against a direct sort-and-alternate computation of $A(R')-2A(R'_{>v})$,
20,000 trials per sub-case, using the file's own exact sub-range
boundaries, not just random $v$):

- Sub-case (I) $b\in[u,2u]$: `A(R')=u` (constant); the five $v$-range
  formulas ($u$, $u-2a$, $5u-2a$, $-3u$, $-u$) all matched exactly, 0
  mismatches over 20,000 trials.
- Sub-case (II) $b\in(0,u)$: `A(R')=3u-2b`; the five $v$-range formulas
  ($3u-2b$, $-5u$, $-u$, $-3u$, $-3u+2b$) all matched exactly, 0 mismatches.
- Checked the boundary tie $a=b=2u$ (at $b=2u$, the two sub-cases meet)
  explicitly: $A(R')=u$ matches sub-case (I)'s formula at that exact point,
  and $\Delta(4,v)\le v-u$ holds with exact equality at $v=2u$
  ($\Delta=1/31=v-u$) — confirms this is a genuine equality/vertex point,
  consistent with the file's own claim of tightness there.
- A separate, finer, fully-random independent script (not restricted to the
  file's own breakpoints; 500,000 trials, $b$ and $v$ both continuous
  uniform over their full legal ranges): **zero violations**, minimum
  margin $77/31{,}000{,}000\approx2.5\times10^{-6}>0$ — small but strictly
  positive, consistent with the equality case found above.

**Every one of the ten sub-range inequalities checked out (both the closed
forms and the final $\Delta\le v-f(4)$ bound), matching the file's proof
exactly.** Theorem 36's n=4 closure is correct.

### 2c. Multi-cut-on-$p_3$ disposal

n=3 (budget 0): no cuts of any kind possible, so trivially disposed —
correct. n=4 (budget 1): splitting $p_3$ into 3+ pieces needs $\ge2$ cuts,
exceeding the budget of 1 — correct, this rules out multi-cut-on-$p_3$ at
n=4 by a direct budget count, independently confirmed.

### 2d. Honesty of scope — the $(\Diamond)$ vs $(\Diamond')$ distinction

Unlike the sibling (§1b above), this file is **explicit and consistent**
throughout (round 19's carried-over text and round 20's new "Current best"
and "Approaches tried" entries) that Theorem 35/36 close $(\Diamond)$
($\Delta(n,v)\le v-f(n)$) specifically, **not** the strictly stronger
epsilon-aware target $(\Diamond')$ needed when $\epsilon(v)=1$ — this
residual bridge gap is honestly flagged as still open (not resolved this
round, not silently assumed closed). I did not find any place in the file
where the Case (b) n=3/n=4 closure is oversold as closing the *actual*
end-to-end middle-band target; every "Corollary"/header statement names
$(\Diamond)$ explicitly. No overclaim found on this front.

**What remains open (correctly scoped, matches my own re-check):**
general $n\ge5$ (Case (b)'s budget $n-3\ge2$ allows $T'$ to carry cuts and
allows multi-cut-on-$p_3$, neither reached by this round's mechanism), and
— across both fronts — the epsilon=1 bridge from $(\Diamond)$/$(\sharp)$ to
the true two-variable target, which after §1b above is now known to be
load-bearing not just for $n\ge5$ but for the *existing* n=3/n=4 "closures"
in both sibling files.

**Verdict: CHANGES REQUESTED.** Status `partial` (as self-reported) is
correct — real, independently-verified, correctly-scoped progress (Case
(b) genuinely closed at n=3,4 for the named target $(\Diamond)$), with the
gap precisely and honestly stated (general $n\ge5$; the $(\Diamond)$ vs
$(\Diamond')$ epsilon bridge, now confirmed to matter even at the levels
already "closed"). No overclaim found in this file.

**Promotable lemmas.** Theorem 36 itself (Case (b) at n=3,4) is a
legitimate, unconditional (modulo the $(\Diamond)$-vs-$(\Diamond')$ scoping,
which is explicit in its own statement) closed-form result — **CERTIFY**
as `theorem-36-case-b-n3-n4-closure.md`, explicitly scoped to $(\Diamond)$
only (not the full two-variable middle-band target), per the file's own
honest framing.

---

## 3. Cross-cutting finding: the epsilon-bridge gap is now the single shared
   crux for BOTH fronts' n=3/n=4 "closures"

Section 1b's discovery generalizes: `rank-pigeonhole-budget`'s $(\sharp)$
and `greedy-halving-adversary`'s $(\Diamond)$ are both special (weaker,
epsilon=0) cases of the same exact bridge target ($(\Diamond')$ in the
sibling's notation). Both sibling closures at n=3 (rank-pigeonhole-budget,
§7.5) and n=4 (greedy-halving-adversary, Theorem 36, when combined with
Theorem 35 at $n=4$) are numerically confirmed true end-to-end but **not
yet algebraically established** in the $\epsilon(v)=1$ zone. This is a
genuine, precisely-located, single remaining obstruction for the entire
middle-band front at every level checked so far — recommend round 21
attack $(\Diamond')$'s $\epsilon=1$ case directly (not re-derive $(\sharp)$/
$(\Diamond)$ again), since the $\epsilon=0$ special case is now closed
(mod this fix) at $n=3,4$ on both fronts.

---

## Summary table

| Slug | Builder Status | Reviewer-verified Status | Verdict |
|---|---|---|---|
| `rank-pigeonhole-budget` | solved (scoped: Claim A) | solved (Claim A, unaffected); §7.5 downgraded partial→partial (real fix, but pre-existing $(\sharp)$-vs-$(\Diamond')$ gap found, not previously caught) | APPROVE (file's own Status target) |
| `greedy-halving-adversary` | partial | partial, confirmed correct and honestly scoped | CHANGES REQUESTED |
