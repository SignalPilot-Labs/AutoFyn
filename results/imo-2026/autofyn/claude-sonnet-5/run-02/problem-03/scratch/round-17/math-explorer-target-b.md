## imo-2026-03 — scouting the "peel p2 first" restart point for Target B

### Setup recap (verified against the files, not re-derived from scratch)
Ladder: $p_i=2^{n+1-i}f(n)$, $f(n)=c(n)=p_1$, $p_1=2p_2$, $p_2=2p_3$, tail-below-$p_2$
total $s=\mathrm{Total}(\{p_3,\dots,p_{n+1}\})=p_2-f(n)$ (`level-2-dominance-identity`).
Target B = item 3 of the round-15/16 breakdown: $\ell(F)=2$, $P\ne\varnothing$
(exact pairing, $\tau_P>0$), sub-case (c), the range $\tau_P\ge p_3$ (equiv.
$t^*:=p_2-\tau_P\le p_3$). Reduces (Prop 26 Steps 2–3, reused verbatim) to
showing $\psi(t^*):=A(\{t^*\}\cup G')\le p_2-f(n)$ where $G'$ is Xiang Yu's
refinement of the tail below $p_1$'s split.

### Is "peel p2 first" algebraically valid? Yes, via a stronger tool than
the ones round 16 named — but it still doesn't close Target B.
- `dominant-element-removal-identity` (needs $p_2>\mathrm{Total}(\text{rest})$)
  and `sharp-dominant-removal-identity` (needs $p_2>\max(\text{rest})$) both
  require **$p_2$ to remain a single unsplit atom** in $G'$ — they cannot
  peel a *split* $p_2$ (a multiset $F_2$ of fragments) off directly, since
  there is no longer a single dominant element to isolate.
- The genuinely correct general peeling tool for a *split* $p_2$ is the
  already-certified **Theorem 29 (`half-dominance-split-bound`)**:
  $A(F_2\cup R)\le M-A(R)$ for *any* split $F_2$ of $M$, whenever
  $\max(R)\le M/2$. With $M=p_2$, $R=$ the sub-tail below $p_2$ (so
  $\max(R)\le p_3=p_2/2$ by `safe-window-lemma` one level down), this holds
  for *every* shape of $p_2$'s split — untouched, dominant-fragment, or
  evenly split — with **no case split**, strictly generalizing what round 16
  flagged as the restart mechanism.
- **I checked both natural ways to fold the extra element $t^*$ into this
  peel, and both fail by a wide (not narrow) margin, matching round 16's own
  "order of magnitude too crude" diagnosis but via an independent,
  structural argument:**
  1. Fold $t^*$ into the reference set: $R'':=\{t^*\}\cup R$ (so
     $\max(R'')\le p_3=p_2/2$ still holds). Theorem 29 gives
     $\psi(t^*)=A(F_2\cup R'')\le p_2-A(R'')$. To reach the target
     $\psi(t^*)\le p_2-f(n)$ this needs $A(R'')=A(\{t^*\}\cup R)\ge f(n)$.
     But $\mathrm{Total}(R'')\le t^*+s\le p_3+s<p_2<f(n)=2p_2$ always (since
     $A(S)\le\mathrm{Total}(S)$, Lemma 2) — **this is provably impossible**,
     not merely numerically weak. (I confirmed the arithmetic:
     $f(n)=2p_2$, and $\mathrm{Total}(R'')<p_2$, so the needed inequality
     can never hold, regardless of $R$'s shape.)
  2. Fold $t^*$ into the split side instead: treat $M':=p_2+t^*$,
     $F_2':=\{t^*\}\cup F_2$ as "a split of $M'$" and apply Theorem 29 with
     reference $R$ alone ($\max(R)\le p_3\le M'/2$ still holds since
     $t^*\ge0$). This gives $\psi(t^*)\le (p_2+t^*)-A(R)$; matching the
     target needs $A(R)\ge t^*+f(n)$. Again $\mathrm{Total}(R)=s=p_2-f(n)<
     f(n)$ for $n$ not too small (and even where $s>f(n)/2$-ish, $s$ never
     reaches $t^*+f(n)\approx f(n)$ since $s=p_2-f(n)<p_2<2p_2=f(n)$
     structurally) — **also provably impossible** by the same mass count.
- **Diagnosis (sharper than round 16's "order of magnitude" phrasing):**
  any strategy that peels $p_2$ (or its split) *off* and then tries to
  recover the needed $f(n)=2p_2$-scale lower bound purely from the
  *residual* tail below $p_2$ (total $s<p_2$) is doomed on a pure mass-count
  argument — the residual physically cannot hold $f(n)$ worth of alternating
  sum. The $p_2$-mass itself must stay "in play" in whatever final bound is
  used, not be subtracted away and then needed again from a strictly
  smaller pool. This is a structural (not just difficulty-level) reason the
  naive restart fails, and it rules out *any* one-shot "peel $p_2$, then
  apply Theorem 31 (or its Floor lemma) to what's left" mechanism, not just
  the specific instances checked in round 16.

### A concrete, apparently unexplored, higher-leverage opening: sub-case (b)
may not actually be closed yet.
Round 15's outline (line ~4036–4050, and its own **reviewer correction**
at line ~4124–4156) established that "$\ell(F)=1,\ v<s$" (items 1≡2) and
"$\ell(F)=2$ sub-case (b)" ($v_1,v_2<p_2$, no dominance) are related via the
**exact** identity (Lemma 25, certified): $A(F\cup G')=A(G')+A(F_1\cup
G')-A(F_2\cup G')$. The reviewer explicitly warned that closing items 1≡2
as a **lower bound only** (which is exactly what Theorem 31, round 16,
does) is *not* sufficient to close sub-case (b), because the second term
enters with a minus sign — you need either (i) an **exact closed-form**
substitution, or (ii) an explicit **upper** bound on $A(F_2\cup G')$, not
just $A(F_2\cup G')\ge f(n)$.
- Checking the round 15/16 write-ups: Theorem 31 (round 16) proves the
  **inequality** $A(F\cup G')\ge f(n)$ via the Truncated Alternating Sum
  Floor — an inequality, not an exact value. Proposition 30 (round 15),
  however, **is** an exact identity:
  $A(F\cup G')=p_2-v+A(R')-2A(R'_{>v})+2v\epsilon(v)$, valid for every
  $v\in(0,p_2)$, unconditionally.
- **I did not find any place in the file where route (i) — plugging
  Proposition 30's exact formula for $v_1$ and $v_2$ into Lemma 25 and
  simplifying — was actually carried out.** Both round 15 and round 16's
  builds focus on closing the $v<s$ inequality target (Theorem 31) and on
  Target B; neither write-up revisits sub-case (b) to check which of routes
  (i)/(ii) it actually used. This looks like a genuine, currently-open gap
  that risks being silently treated as "closed for free" (per the original,
  now-corrected, round-15 outline framing) when the reviewer's own
  correction says it is not. **This is a concrete, well-scoped target with
  all the needed machinery already certified** (Lemma 25, Proposition 30,
  `upper-truncation-identity`) — plugging in and simplifying
  $A(G')+\varphi(v_1)-\varphi(v_2)$ (with $\varphi$ from Prop 30) reduces
  the target to a bound on
  $-2A(R'_{>v_1})+2A(R'_{>v_2})+2v_1\epsilon(v_1)-2v_2\epsilon(v_2)$ — a
  *difference* of two truncations, which is a different (and possibly more
  tractable) shape than either Theorem 31's or Target B's single-truncation
  problem, since $v_1>v_2$ means $R'_{>v_1}\subseteq R'_{>v_2}$ and the
  difference is exactly the truncated alternating sum of the *band*
  $(v_2,v_1]$ — worth trying a two-threshold generalization of the already
  proved Truncated Alternating Sum Floor.

### A previously-flagged bug that overlaps this territory (do not re-derive, just be aware)
`lemmas/proposition-29b-partial-closure.md` carries a round-15 reviewer
correction: Prop 29b's own stated proof treats $G'$ as a refinement of
$\{p_3,\dots,p_{n+1}\}$ **excluding** $p_2$ — but the game-legal $G'$ can
include a split $p_2$. No counterexample to Prop 29b's *conclusion* was
found (adversarial grid search, $n=3$–$7$, tiny positive margins), so the
$\tau_P<p_3$ range is very likely still true, but its **proof** has the
identical "does this $G'$ include $p_2$ or not" ambiguity that also
undermines any naive peel for Target B ($\tau_P\ge p_3$). A future round
repairing Target B should repair this citation at the same time, since both
sit on the same "$G'$ with or without $p_2$" fork.

### Numeric probing — caveat
I ran my own exact-`Fraction` scripts (`/tmp/verify_target_b.py`,
`/tmp/verify_target_b2.py`, `/tmp/verify_subcase_b.py`) to sanity-check the
mass-count argument above, but did **not** carefully reproduce the exact
game-legal cut-budget coupling (this repo has repeatedly caught real bugs
in ad hoc scripts of exactly this kind — round 10's two caught budget bugs,
round 15's two caught scripting bugs). My scripts allow more tail cuts than
the true remaining budget, so raw numeric margins from them are **not**
reliable evidence either way for the true (legal) target inequality — only
the algebraic mass-count argument above (which needs no numerics: it's just
$\mathrm{Total}(R'')<p_2<f(n)$) should be trusted. Flagging this explicitly
so the outliner doesn't cite my scripts' raw margins as corroboration.

### Mixed-regime status check (per current.md, rounds 14–16)
- $\ell(F)=2$, $P\ne\varnothing$, $\tau_P<p_3$: certified **with a flagged
  proof gap** (Prop 29b, see above) — not a clean closure, treat as
  "probably true, proof needs repair," not "done."
- $\ell(F)=2$, $P\ne\varnothing$, $\tau_P\ge p_3$ (Target B): **open**,
  confirmed structurally hard (not just under-worked) by the mass-count
  argument above.
- $\ell(F)=2$ sub-case (b) ($v_1,v_2<p_2$): **status unclear / likely still
  open** — see the concrete route (i) opening above; this is not the same
  as Target B and appears to have fallen through the cracks between rounds
  15 and 16.
- Case (b2) (the general **upper bound**, `lp-duality-certificate`'s
  target): confirmed still open per current.md round 9–16 — unrelated to
  this lower-bound restart point; two dead-end mechanisms already ruled out
  there (`peel-and-bisect-ih-dead-ends`), `bisect-top-k-lemma` covers only a
  partial range.

## Summary for the outliner
- **Distinct openings:**
  1. Direct Target B closure via peel-$p_2$ (Theorem 29 or sharp-removal):
     **ruled out structurally** (mass-count proof above, not just numerics)
     — do not re-attempt any one-shot "peel $p_2$, apply Theorem 31 to the
     residual" mechanism.
  2. **Sub-case (b) via route (i)**: substitute Proposition 30's exact
     formula into Lemma 25's exact identity for both $v_1,v_2$ and simplify
     the resulting *band*-truncation difference
     $A(R'_{>v_2})-A(R'_{>v_1})$ — genuinely new, uses only already-certified
     machinery, not yet attempted as far as the file shows. This looks like
     the single highest-leverage, most concrete opening right now.
  3. A genuine "two-threshold" generalization of the certified Truncated
     Alternating Sum Floor (bounding $A(S_{>v_2})-A(S_{>v_1})$ jointly,
     rather than each $A(S_{>v})$ separately) — a natural, general-purpose
     lemma this population does not yet have, and would directly serve
     opening 2.
  4. If Target B itself is to be attacked head-on (not deferred), the
     needed fact is precisely what round 15/16 isolated: an **upper** bound
     on a *partial/top-truncated* alternating sum of a legal $(n-2)$-ladder
     response, at a scale that must reference the *whole* residual tail
     (including $p_2$'s own split), not just the sub-tail below $p_2$ — a
     genuinely different, harder statement than Theorem 31's, not a
     relabeling of it.
- **Candidate technique(s):** `cross-term-identity-threshold` (Lemma 8),
  `upper-truncation-identity`, `truncated-alternating-sum-floor`,
  `half-dominance-split-bound` (Theorem 29), Lemma 25's exact
  sub-case-(b)/(c) decomposition, `odd-run-reduction-lemma`.
- **Cheap-kill candidate:** the mass-count check
  ("$\mathrm{Total}(\text{peeled-off residual})<f(n)$, so no peel-then-floor
  route can work") is a fast way to rule out any future proposed peel
  mechanism for Target B before spending a build round on it — apply it
  first to any new peel proposal.
- **Knowledge-base entries:** none beyond what's already cited in the
  approach file/lemmas (this is deep in problem-specific machinery by now;
  `knowledge_base.md`'s generic entries — LP duality, extremal
  combinatorics techniques — were already explored by the sibling
  `lp-duality-certificate` approach and are not newly relevant here).
- **Analogous past problems (crux corpus):** not consulted this round —
  this restart point is a narrow, deep continuation of problem-specific
  machinery (7+ rounds of internally-built lemma chains); a crux-corpus
  match at this level of specificity is unlikely to exist and searching it
  would not change the diagnosis above. If the outliner wants a fresh
  framing (not a continuation of this chain), a separate explorer lens
  should search the corpus for a genuinely different attack on the whole
  problem rather than this sub-gap.
- **Prior progress:** Theorem 31 (round 16) fully closes items 1/2
  (`truncated-alternating-sum-floor`, certified). Theorem 29 (round 14,
  `half-dominance-split-bound`) fully closes $(\dagger)$'s $p_2$-cut
  complement for $\ell(F)=1,v\ge p_2$. Proposition 29b closes $\tau_P<p_3$
  with a flagged proof gap (conclusion likely true, mechanism needs repair).
- **Dead ends (do not retry):** any direct "peel $p_2$ (via
  dominant-removal, sharp-dominant-removal, or Theorem 29), then bound the
  residual via Theorem 31/the Floor lemma" mechanism for Target B — proved
  above to fail by a mass-count argument, not just an under-optimized bound;
  this subsumes and sharpens round 16's own "order of magnitude too crude"
  finding.
- **Small-case / intuition notes:** current.md/round 15 numerics (trusted,
  built with correct budget bookkeeping, unlike my own scratch scripts)
  show Target B's true margin is small but positive at $n=3,4$
  ($\approx0.002$–$0.004\times f(n)$, essentially tied with Prop 29b's
  boundary) and grows for $n\ge5$ — consistent with the target being true
  but requiring an argument close to sharp at small $n$, not a crude bound,
  reinforcing that a structurally different (sharper) mechanism than a
  simple peel is needed, matching the mass-count diagnosis above.
