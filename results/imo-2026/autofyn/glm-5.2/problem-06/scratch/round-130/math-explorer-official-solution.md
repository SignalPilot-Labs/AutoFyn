# IMO 2026 Problem 6 — official-solution retrieval & mechanism mapping

## Source identification (correction of the dispatch attribution)

The dispatch says "IMO 2024 Problem 6." That is **wrong**. IMO 2024 P6 was the *aquaesulian function* problem ($f:\mathbb Q\to\mathbb Q$, $f(x+f(y))=f(x)+y$ or $f(f(x)+y)=x+f(y)$) — confirmed by the official IMO 2024 Shortlist PDF (`IMO2024SL.pdf`, problem A7/N-series) and the Google DeepMind IMO-2024 P6 page (which solves the aquaesulian problem). The greedy-gcd problem is **NOT** in the IMO 2024 shortlist (I scanned all of N1–N8 and the full shortlist text for `gcd`, `common divisor`, `n+T`, `T,L` — no match).

The actual source, from `problems.jsonl`:
- `problem_id`: `imo-2026-06`, `source`: `IMO`, `year`: **2026**, `country`: International, AoPS thread `c6h3866890`.

This is **IMO 2026 Problem 6**, proposed by **Hung-Hsun Hans Yu (TWN)**, sat at IMO 2026 (Bath, July 2026). Today is 2026-07-24; the IMO ended ~10 days ago. I retrieved **Evan Chen's "IMO 2026 Solution Notes"** (`web.evanchen.cc/exams/IMO-2026-notes.pdf`, dated **23 July 2026** — yesterday). Chen writes that his notes mix "the solutions provided by the competition organizers, and solutions found by the community," all rewritten by him. This is the authoritative published solution available; the official IMO 2026 Shortlist booklet is **confidential until IMO 2027** and is NOT on `imo-official.org` (I checked `/problems/2026/` — only problem statements, no shortlist PDF).

AoPS itself (both the wiki and the community thread `c6h3866890`) is behind a Cloudflare JS challenge from this network; the Wayback snapshot of the thread captured only the page shell, not the rendered posts. So **Evan Chen's PDF is the single load-bearing source I could fully read.** I cross-checked his P6 statement against `problems.jsonl` — exact match (word-for-word, including the "Note that $\gcd(x,y)$ denotes…" parenthetical which Chen's statement omits but is cosmetic).

I also confirmed the mechanism numerically (see *Small-case verification* below).

---

## The ACTUAL mechanism of the published solution (mapped to this run's vocabulary)

Chen's proof has three pieces. I label them against the run's existing assets.

### Piece A — a different partial order + the "appears ⟺ valid against all terms" lemma  [the run ALREADY HAS this — it is δ]

Chen defines a partial order on the terms:
$$a_m \prec a_n \iff m<n \ \text{and}\ \mathrm{rad}(a_m)\mid \mathrm{rad}(a_n) \quad(\text{i.e. } P(a_m)\subseteq P(a_n),\ m<n).$$
(Equivalently: $a_n$ is *irrelevant* if some earlier term's prime-set already sits inside $P(a_n)$.) A term is **$\prec$-minimal** if no earlier term subsumes it.

**Trivial claim (Chen).** For $x\ge a_1$, the following are equivalent: $x$ appears in the sequence; $\gcd(x,a_i)>1$ for every $i$; …; $\gcd(x,a_i)>1$ for every $\prec$-minimal $a_i$ with $a_i<x$.

The proof of "appears ⟺ valid against all terms": the greedy $a_{n+1}=\min\{>a_n\text{ valid vs.\ }a_1,\dots,a_n\}$ never permanently skips a globally-valid integer, because any skipped valid integer would have a smaller valid integer appear instead, which is still valid w.r.t.\ it; iterating, every $x\ge a_1$ valid against all terms eventually appears. **This is exactly the run's `universal-membership-no-transient` + `transversal-residue-characterization` + `greedy-equals-cyclic-successor` lemmas** (the δ machinery, certified, verified-milestone). The $\prec$-minimal supports are precisely the run's $\mathcal M=\min_\subseteq\{P(a_i)\}$ (the final minimal-support family). So **Piece A is already done in the field.**

### Piece B — the LARGE-PRIME DESCENT  [the run does NOT have this. It is the missing wall-closer.]

Define a prime **large** if $p>a_1^2$; **small** otherwise. Let $P=\{$primes $\le a_1^2\}$ (finite).

> **Claim (the heart).** If $a_n$ is divisible by a large prime, then $a_n$ is **not** $\prec$-minimal.

*Proof (by induction on $n$).* Write $a_n=p\,c$ with $p>a_1^2$ large. Since $a_n$ appears in the sequence, $\gcd(a_1,a_n)>1$; pick any prime $q\mid\gcd(a_1,a_n)$. Then $q\le a_1$ (as $q\mid a_1$) and $q\neq p$ (as $p>a_1^2\ge a_1\ge q$), hence $q\mid c$. Consider the geometric chain $c,\, qc,\, q^2c,\dots$. Because
$$\frac{a_n}{a_1}=\frac{pc}{a_1}\ge\frac{p}{a_1}>a_1\ge q,$$
the half-open interval $[a_1,\,a_n)$ has ratio $>q$, so it contains some $q^k c$ (take the smallest $k$ with $q^k c\ge a_1$; then $q^k c<q\,a_1<a_n$).

We show $q^k c$ appears in the sequence. By the Piece-A claim it suffices that $\gcd(q^k c,\,a_i)>1$ for every $\prec$-minimal $a_i<q^k c$. Such $a_i$ satisfy $a_i<a_n$, hence $i<n$, so by the induction hypothesis **no $\prec$-minimal $a_i$ with $i<n$ is divisible by a large prime** — in particular $p\nmid a_i$. Now $a_n$ appears after $a_i$, so $\gcd(a_n,a_i)>1$; pick a prime $r\mid\gcd(a_n,a_i)$. Since $p\nmid a_i$, $r\neq p$, so $r\mid c$, hence $r\mid q^k c$, giving $\gcd(q^k c,a_i)\ge r>1$.

So $q^k c$ is in the sequence, with $q^k c<a_n$ (earlier index) and $\mathrm{rad}(q^k c)=\mathrm{rad}(c)\mid\mathrm{rad}(pc)=\mathrm{rad}(a_n)$ (using $q\mid c$). Thus $a_{\mathrm{idx}(q^k c)}\prec a_n$, so $a_n$ is **not** $\prec$-minimal. ∎

**Corollary (the wall, closed).** Every $\prec$-minimal term — equivalently every member of the run's $\mathcal M$ — is $a_1^2$-smooth (all prime factors $\le a_1^2$). Hence $P_{\mathrm{ess}}=\bigcup\mathcal M\subseteq\{p:p\le a_1^2\}$ is finite, and $\mathcal M\subseteq 2^{P}$ is finite.

Chen adds (Remark): "with a little bit of additional care one can show in fact that when $a_n$ is $\prec$-minimal, its prime divisors are actually at most $a_1$ (rather than just less than $a_1^2$)." So the clean bound is $a_1^2$; the tightened bound is $a_1$.

### Piece C — bookkeeping to periodicity  [the run ALREADY HAS this — it is δ's finish]

With $P=\{p\le a_1^2\}$ and $\mathcal F=\{$small-prime support-sets that hit every member of $\mathcal M\}\subseteq 2^P$ (finite), membership in the sequence (for $a\ge a_1$) depends only on $\bigl(a\bmod\prod_{p\in P}p\bigr)$. Take $L=\prod_{p\in P}p$ (squarefree) and $T=$ the number of admissible residues. Then $a_{n+T}=a_n+L$.

**This is exactly the run's `post-stabilization-theorem`** (composing the transversal-residue set $V$, squarefree $L=\prod P$, single-cycle / period-sum $=L$), certified and verified on $a_1=15\to T=8,L=30$. Chen's example $a_1=15$: sequence $=15,18,20,24,30,36,40,42,45,\dots$ = "integers $\ge15$ divisible by at least one of $\{2{\cdot}3,\,3{\cdot}5,\,2{\cdot}5\}$," $L=30$, $T=8$ — **identical** to the run's δ verification. So **Piece C is already done.**

---

## Answers to the dispatch's specific questions

1. **How does it prove the set of primes that ever appear is FINITE (the run's open wall)?**
   By the large-prime descent (Piece B). It shows every minimal-support term is $a_1^2$-smooth, so the essential-prime set $P_{\mathrm{ess}}\subseteq\{p\le a_1^2\}$ is finite. **No density, no regime split, no smooth-number estimate.**

2. **Freeze/saturated regime split? common-prime argument? smooth-number density (Dickman/de Bruijn)? descent/minimal-criminal? pigeonhole on small primes? bounded-promotion-count?**
   **None of these.** It is a single uniform **descent**: a minimal-criminal carrying a large prime $p$ is contradicted by substituting $p$ out for a power of a small prime $q\mid a_1$, producing an earlier term with a subset support. No freeze-lock, no saturated regime, no self-blocking fixed point, no Cov, no mtp, no window, no Dickman/de Bruijn, no promotion count. The "regime split (F)/(S)" that the entire run is organized around is **not used by the official solution** — the descent handles freeze and saturated cases identically.

3. **Does it prove SPT ("every minimal contains a prime $\le p^*:=\min P(a_1)$")? Or bypass it?**
   **It bypasses SPT entirely.** The official bound is "$a_1^2$-smooth" (clean) / "$a_1$-smooth" (tightened) — i.e. *every* prime in a minimal is $\le a_1^2$ (or $\le a_1$), a **stronger and different** statement than SPT's "*some* prime $\le p^*$." Crucially the official bound closes **GAP-3** (the run's $\{2,q\}$ obstruction: $q$ is forced $\le a_1^2$, so the antichain is finite), which SPT does *not* close. The run has spent 4+ rounds chasing the **wrong, harder-than-necessary** target $p^*$; the official solution never needs $p^*$.

4. **Does it prove W2 (the "crash"/strict-beat smooth-density step)?**
   **No, and it does not need it.** There is no "crash," no mtp-multiple window, no equality/strict-beat promotion dichotomy, no "smallest valid below the window" step. The descent is global on any minimal candidate carrying a large prime, independent of where it sits relative to the mtp-multiple. **The entire W1/W2/SPT edifice the field built is orthogonal to the official route.**

5. **Post-stabilization / eventual-periodicity argument — does it match the run's δ?**
   **Yes, identically.** $L=\prod P$ (squarefree), $T=|\{$admissible residues$\bmod L\}|$ (= $|V|$, the transversal-residue count), period-sum $=L$. This is the run's certified `post-stabilization-theorem`. The official solution and δ are the same finish; the official solution just supplies a clean wall-proof that δ hypothesizes.

---

## CRUX EXTRACTION (hints to adapt — every step still proven from scratch)

**Crux 1 (THE missing move) — large-prime descent by $a_1$-factor substitution.** *The published solution substitutes a large prime $p\mid a_n$ (minimal candidate) by a power of a small prime $q\mid\gcd(a_1,a_n)$ to manufacture an earlier sequence term $q^k c$ with $\mathrm{rad}(q^k c)\mid\mathrm{rad}(a_n)$, proving $a_n$ non-minimal — to achieve "every minimal is $a_1^2$-smooth," which is the finiteness wall.* **The field has NOT tried this.** The run's framings are: SPT/$p^*$-bound (α, smooth-window-crash, γ), Cov-monovariant (pstar), mtp-monovariant (γ), Bertrand eviction (β, dead). None uses the rad-divisibility partial order or the $q^k$-substitution descent. The closest field artifact — the saturated "bounded-entering-prime $\le a_1/p_{\min}$" conjecture (round 3) — is a *value bound on entering primes via free-rider structure*, a different and weaker mechanism; the official descent gives a *value bound on primes inside minimals* ($\le a_1^2$) directly, for free, in one inductive step.

**Crux 2 — the "appears ⟺ valid against all (minimal) terms" lemma.** *The published solution proves the greedy never permanently skips a globally-valid integer, reducing the whole sequence to "integers $\ge a_1$ hitting every minimal support."* **The field ALREADY has this** (`universal-membership-no-transient`, `transversal-residue-characterization`, `greedy-equals-cyclic-successor`, δ verified-milestone). No re-proof needed; import.

**Crux 3 — squarefree-$L$, $T=|V|$ periodicity finish.** *The published solution takes $L=\prod\{$small primes$\}$, $T=\#$admissible residues, done.* **The field ALREADY has this** (`post-stabilization-theorem`, `cyclic-successor-single-cycle`, verified $a_1=15\to T=8,L=30$). Import.

So **only Crux 1 is new.** Pieces A and C are done; the field is missing exactly the descent.

---

## VERDICT — genuinely different mechanism; OPEN A NEW APPROACH, do not fold into the field's existing framings

The official finiteness mechanism **does NOT correspond to W2 (smooth-density, the field's current bet)**, nor to SPT, nor to the Cov-monovariant. It is a **clean elementary descent** (substitute large prime → power of an $a_1$-factor), giving a uniform $a_1^2$-smooth bound on minimals. It:
- closes **GAP-1** ($\mathrm{mtp}\le\prod_{p\le a_1^2}p$, finite — a *weaker but sufficient* bound than the field's $\mathrm{primorial}(p^*)$);
- closes **GAP-3** ($P_{\mathrm{ess}}\subseteq\{p\le a_1^2\}$ finite — kills the $\{2,q\}$ obstruction directly, since $q\le a_1^2$ is forced);
- closes **GAP-S / GAP-S'** (the whole saturated wall, *without* the freeze/saturated regime split, *without* crash-inevitability, *without* Cov-stabilization);
- makes the run's **freeze regime machinery** (`freeze-lock`, `singleton-freeze`, common-primes-bounded, the (F)/(S) case split) **unnecessary** — the descent is uniform.

The outliner should **open a NEW approach** (`large-prime-descent` or similar) built around Crux 1, importing δ for Pieces A and C. It should **NOT** try to fold this into `density-promotion-bound`, `smooth-window-crash`, or `pstar-core-straggler`: those framings' load-bearing machinery (mtp-window, equality/strict-beat dichotomy, W1/W2, SPT/$p^*$, Cov) is *not used* by the official route, and grafting the descent onto them would re-impose the regime split and the W2 smooth-density step that the official solution precisely avoids. A descent-based approach is also **far more likely to reach APPROVE** than the field's current bets, because it is the actual published mechanism and is elementary (no analytic estimates, no open conjectures).

One caveat for the builder: the descent's induction is on $n$ with the partial order $a_m\prec a_n$ ($m<n$, $\mathrm{rad}(a_m)\mid\mathrm{rad}(a_n)$). The run's $\mathcal M_n$ is the *current* $\subseteq$-minimal family (supports removed as subsets arrive later); the descent's "$\prec$-minimal" is a *per-term, index-ordered* notion. These coincide on the final family $\mathcal M$ (the supports of $\prec$-minimal terms $=$ members of $\mathcal M$), but the builder should phrase the descent in Chen's $\prec$ order to keep the induction clean, then map back to $\mathcal M$ for the δ finish.

## Small-case verification (conjecture-grade numerical check of the official claim)

Computed (sympy) the $\prec$-minimal terms and the maximum prime appearing in any minimal support, vs the official $a_1^2$ bound:
- $a_1=15$: 3 minimals $\{3,5\},\{2,3\},\{2,5\}$; max prime $5\le a_1^2{=}225$. (Matches Chen's example exactly.)
- $a_1=30$: minimals $\{2,3,5\},\{2\}$; max prime $5\le 900$.
- $a_1=175$: 5 minimals; max prime $13\le 30625$.
- $a_1=429$: 13 minimals; max prime $43\le 184041$.
- $a_1=273$: max prime in any minimal $=241\le 273^2{=}74529$.

All satisfy the official bound (in fact all satisfy the tightened $\le a_1$ bound). This is **evidence the descent is correct**, not a proof (the proof is the induction above, taken from Chen). Note: $a_1=273$ did *not* exhibit the run's claimed "freeze at $3^6{=}729$" within 300 terms in my run — it accumulated 58 minimals carrying primes up to 241 (all co-occurring with 3 as free riders). This is a **run-internal discrepancy** worth the builder/reviewer re-checking, but it does **not** affect the official solution, which is uniform across freeze and saturated regimes. Flagging it only because the run_state's "273 → freeze-lock → $3^6$" empirical claim may need re-verification.

## Knowledge-base entries to use
- `knowledge_base.md` — the official solution uses only: the radical $\mathrm{rad}$, basic multiplicative order/geometric-step counting (powers of $q$ land in a length-ratio-$>q$ interval), and induction. **No heavy theorem.** No Dickman/de Bruijn (KB has no such entry anyway), no Bertrand, no LLL, no Mertens. The KB candidate most relevant is whatever generic "induction / descent / minimal criminal" entry exists; otherwise the proof is self-contained. (I did not re-open `knowledge_base.md` this round since the official mechanism needs no named external theorem — worth the outliner confirming, but the descent is elementary.)

## Analogous past problems (cruxes)
- The crux move "a minimal criminal carrying a large prime $p$ is contradicted by substituting $p\to q^k$ ($q$ a small prime of $a_1$) to land an earlier subset-support term" is a **radical/rad-divisibility descent**. I did not run a crux-corpus query this round (focused on retrieval); the outliner may query the corpus subtopic `descent` / `radical` / `smooth` if it wants prior analogues, but the move is standard enough to prove from scratch.

## Prior progress
- δ (`transversal-single-cycle-finish`) conditional post-stabilization theorem = Pieces A+C of the official solution, certified, verified-milestone. **Directly reusable as the finish of the new descent approach.** No re-work needed.
- The freeze-regime proof (α) is a valid special case but is subsumed/made unnecessary by the uniform descent.
- The mtp-monovariant, Cov-monovariant, SPT/W1/W2 machinery is **not on the official route**; it can stay as dead-end documentation but should not be grafted onto the new approach.

## Dead ends (do not retry, relative to the official route)
- **SPT ($\min(M)\le p^*$) as the wall target** — wrong target: stronger than necessary and insufficient for GAP-3 (the $\{2,q\}$ obstruction). The official solution replaces it with the *correct* target "every prime in every minimal $\le a_1^2$." Drop SPT/W1/W2 as the wall-closing program.
- **W2 (strict-beat smooth/short-interval density)** — not needed; the official solution has no window, no mtp-multiple, no equality/strict-beat dichotomy. Do not pursue analytic smooth-number density for the wall.
- **Cov-monovariant / crash-inevitability / GAP-S' (termination after Cov stabilizes)** — not needed; the descent closes the wall without any crash or Cov stabilization.
- **Freeze/saturated regime split (F)/(S)** — not needed; the descent is uniform. (The freeze lemma stays valid but is a detour.)
- **Bertrand eviction (β)** — already dead; still dead.
- **ω-only induction (ε)** — already dead; still dead.

## Distinct openings for the outliner
1. **`large-prime-descent` (NEW, headline)** — reproduce Chen's Crux 1 (induction on $n$; large prime $p\mid a_n\Rightarrow q^k c$ earlier with $\mathrm{rad}\mid\mathrm{rad}$), conclude minimals $a_1^2$-smooth, import δ for the finish. Single uniform proof, no regimes. Highest probability of APPROVE.
2. **(Optional) `large-prime-descent-tightened`** — the same with the tightened $\le a_1$ bound (Chen's Remark). Slightly more delicate (the $a_1^2\to a_1$ sharpening needs the "additional care" Chen mentions); only worth a separate slug if the clean version stalls.
3. The existing approaches (α, pstar, smooth-window-crash, γ) should be **retired or frozen** — the official mechanism is not a refinement of any of them; keeping them alive as parallel bets is a single-variant-of-the-wrong-idea trap. Recommend the outliner field = {`large-prime-descent`} (plus δ as the imported finish) for the wall, retaining the existing certified lemmas (δ chain, pairwise-intersection, universal-membership) as imports.
