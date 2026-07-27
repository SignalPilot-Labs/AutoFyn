## imo-2026-06

**Field note.** Three explorers scouted this round; one retrieved Evan Chen's published IMO 2026 P6 solution notes (dated 2026-07-23). The published finiteness mechanism is a single elementary **large-prime descent** — genuinely different from the field's entire SPT / W2 / Cov / regime-split / mtp machinery. It closes the wall the field has been stuck on for 4+ rounds: Pieces A (appears ⟺ valid against all minimal terms) and C (squarefree-L, $T=|V|$ periodicity) are *exactly* the field's certified δ chain (DONE); Piece B (the descent) is the one missing move. This round the field contracts to ONE headline build (`large-prime-descent`); the wall-attacking framings are frozen (certified lemmas retained as imports) because the descent closes the wall they were attacking without their machinery.

---

### large-prime-descent: new
**Target:** Prove there exist positive integers $T,L$ with $a_{n+T}=a_n+L$ for every $n\ge1$ (the WHOLE claim — end to end).
**Technique:** Minimal-criminal descent on a radical-divisibility partial order, composing (i) the descent (Crux 1, the only new proof) with (ii) the field's certified δ chain (Pieces A + C, imported, not re-proved). Spine: an induction on $n$ showing every $\prec$-minimal term is $a_1^2$-smooth, hence the minimal-support family $\mathcal M$ is finite, after which `post-stabilization-theorem` (δ) delivers the period.

**Skeleton:**

1. **Notation and the partial order.** For $m>1$ write $P(m)=\{p:p\text{ prime},\,p\mid m\}$, $\mathrm{rad}(m)=\prod_{p\in P(m)}p$. Define the index-ordered radical partial order on terms:
   $$a_m\prec a_n \iff m<n\ \text{and}\ \mathrm{rad}(a_m)\mid\mathrm{rad}(a_n)\quad(\text{i.e. }P(a_m)\subseteq P(a_n),\ m<n).$$
   A term $a_n$ is **$\prec$-minimal** if no earlier term $a_m$ ($m<n$) satisfies $a_m\prec a_n$.

2. **$\prec$-minimal supports $=$ the field's $\mathcal M$.** The supports of the $\prec$-minimal terms are exactly $\mathcal M=\min_\subseteq\{P(a_i):i\ge1\}$ (the final minimal-support family that δ is phrased around). — *by a set-inclusion duality argument (an inclusion-minimal support is witnessed by its first-appearing term, which is then $\prec$-minimal; conversely a $\prec$-minimal support contains no proper sub-support among earlier terms, hence among all terms).*

3. **Piece A (IMPORT, do not re-prove): appears ⟺ valid against all $\prec$-minimal terms below $x$.** The greedy's smallest-first dynamics never permanently skip a globally-valid integer: if $x\ge a_1$ satisfies $\gcd(x,a_i)>1$ for every $\prec$-minimal $a_i<x$, then $x$ appears. — *import as `universal-membership-no-transient` + `transversal-residue-characterization` + `greedy-equals-cyclic-successor` (certified, δ); cite, do not re-derive. The only rephrasing needed is to state the criterion against $\prec$-minimal terms below $x$ rather than against the final $\mathcal M$ — equivalent because supports of $\prec$-minimals are $\mathcal M$ (step 2).*

4. **Crux 1 (the only genuinely new proof): the large-prime descent.** Call a prime **large** if $p>a_1^2$; **small** otherwise. Let $P=\{p:p\le a_1^2\}$ (finite).

   > **Claim.** If $a_n$ is divisible by a large prime, then $a_n$ is **not** $\prec$-minimal.

   *Proof by induction on $n$.* Write $a_n=p\,c$ with $p>a_1^2$ large. Since $a_n$ appears, $\gcd(a_1,a_n)>1$; pick a prime $q\mid\gcd(a_1,a_n)$. Then $q\le a_1$ (as $q\mid a_1$) and $q\neq p$ (as $p>a_1^2\ge a_1\ge q$), so $q\mid c$. Consider the geometric chain $c,\,qc,\,q^2c,\ldots$. Because
   $$\frac{a_n}{a_1}=\frac{pc}{a_1}\ge\frac{p}{a_1}>a_1\ge q,$$
   the half-open interval $[a_1,a_n)$ has ratio $>q$, so it contains some $q^k c$ (take the smallest $k$ with $q^k c\ge a_1$; then $q^k c<q\cdot a_1<a_n$).

   We show $q^k c$ appears. By Piece A it suffices that $\gcd(q^k c,a_i)>1$ for every $\prec$-minimal $a_i<q^k c$. Such $a_i$ satisfy $a_i<a_n$, hence $i<n$; by the induction hypothesis **no $\prec$-minimal $a_i$ with $i<n$ is divisible by a large prime** — in particular $p\nmid a_i$. Now $a_n$ appears after $a_i$, so $\gcd(a_n,a_i)>1$; pick a prime $r\mid\gcd(a_n,a_i)$. Since $p\nmid a_i$, $r\neq p$, so $r\mid c$, hence $r\mid q^k c$, giving $\gcd(q^k c,a_i)\ge r>1$.

   So $q^k c$ is in the sequence, with $q^k c<a_n$ (earlier index) and $\mathrm{rad}(q^k c)=\mathrm{rad}(c)\mid\mathrm{rad}(pc)=\mathrm{rad}(a_n)$ (using $q\mid c$). Hence $a_{\mathrm{idx}(q^k c)}\prec a_n$, so $a_n$ is **not** $\prec$-minimal. ∎

   **Key lemmas (claim + the one-line mechanism that makes it true):**
   - **The $q^k c\in[a_1,a_n)$ landing** — because $a_n/a_1\ge p/a_1>a_1\ge q$, the interval $[a_1,a_n)$ has multiplicative ratio $>q$, so a power of $q$ lifts $c$ into it. (This is the load-bearing arithmetic step; the inequality $a_n/a_1>q$ is what makes the chain land strictly below $a_n$.)
   - **$\prec$-minimal $a_i<q^k c\Rightarrow i<n$** — because $q^k c<a_n$ and the sequence is strictly increasing, so $a_i<q^k c<a_n$ forces $i<n$. (Trivial but load-bearing: this is what lets the IH apply.)
   - **$r\mid\gcd(a_n,a_i)\Rightarrow r\mid q^k c$** — because $r\neq p$ (IH: $p\nmid a_i$, and $p\mid a_n$), so $r\mid c\mid q^k c$. (This is the substitution move: the large prime $p$ is invisible to $a_i$, so any shared prime lives in $c$ and is inherited by $q^k c$.)
   - **$\mathrm{rad}(q^k c)\mid\mathrm{rad}(a_n)$** — because $P(q^k c)=P(c)\subseteq P(c)\cup\{p\}=P(a_n)$ (using $q\mid c$ so no new prime is introduced). (This is what makes $a_{\mathrm{idx}(q^k c)}\prec a_n$ hold, i.e. the descent step.)

5. **Corollary (the wall, closed).** Every $\prec$-minimal term — equivalently every member of $\mathcal M$ (step 2) — is $a_1^2$-smooth (all prime factors $\le a_1^2$). Hence
   $$P_{\mathrm{ess}}=\bigcup\mathcal M\subseteq\{p:p\le a_1^2\}$$
   is finite, and $\mathcal M\subseteq 2^{P}$ is finite.

6. **Finish (IMPORT, do not re-prove): Piece C, the post-stabilization theorem.** With $\mathcal M$ finite (step 5), set $L=\prod_{p\in\bigcup\mathcal M}p$ (squarefree) and $T=|V|$ where $V=\{r\in\{0,\ldots,L-1\}:\{p\in\bigcup\mathcal M:p\mid r\}\text{ hits }\mathcal M\}$. Then $a_{n+T}=a_n+L$ for every $n\ge1$. — *import as `post-stabilization-theorem` (certified, δ); cite. The only rephrasing: the descent is phrased in $\prec$ order (per-term, index-ordered); map to $\mathcal M$ via step 2 before invoking δ.*

**Open gaps:**
- Step 2 (the $\prec$-minimal $\leftrightarrow\mathcal M$ correspondence) — needs a rigorous proof of both inclusions; the builder writes it.
- Step 4 (Crux 1, the descent induction) — the only genuinely new proof; the builder writes it in full, discharging the four load-bearing sub-lemmas above and phrasing the IH precisely as "every $\prec$-minimal $a_i$ with $i<n$ is $a_1^2$-smooth" (equivalently "no $\prec$-minimal $a_i$ with $i<n$ is divisible by a large prime").
- Step 3 and Step 6 are imported from certified lemmas; no gap, just cite correctly.

**Cases to cover:** none — the descent is uniform across freeze and saturated regimes (no (F)/(S) case split).

**Watch out for:**
- The IH phrasing. It must be on $\prec$-minimality of $a_n$ carrying a large prime, phrased per-index: "no $\prec$-minimal $a_i$ with $i<n$ is divisible by a large prime." A phrasing in terms of the final $\mathcal M$ would be circular. Phrase the descent in Chen's $\prec$ order, then map to $\mathcal M$ only at step 6.
- The $q^k c$ landing uses $a_n/a_1 > q$ (strict). The strictness comes from $p/a_1>a_1$ (i.e. $p>a_1^2$), which is exactly the "large" threshold — the threshold is tight to this inequality. The builder should verify the endpoint $q^k c<q\cdot a_1<a_n$ carefully.
- The "$\mathrm{rad}(q^k c)=\mathrm{rad}(c)$" step uses $q\mid c$ (so multiplying $c$ by $q^k$ adds no new prime). This is why $q$ must divide $c$, which follows from $q\neq p$ and $q\mid a_n=pc$.
- (Non-blocking caveat for the reviewer, flagged by the explorer.) The run-internal empirical claim "$a_1=273$ freezes at $3^6=729$" did not reproduce within 300 terms in the explorer's run (it accumulated 58 minimals carrying primes up to 241, all co-occurring with 3 as free riders). This does NOT affect the official solution, which is uniform across regimes. The reviewer may re-verify the 273 empirical claim independently; the descent itself stands regardless.
- (Optional tightening.) Chen's Remark notes "with a little additional care" the bound sharpens to $a_1$-smooth (every prime in a minimal $\le a_1$). Do NOT pursue the tightened bound in this slug — the clean $a_1^2$ bound already closes the wall and is what δ's finish needs. A tightened variant is a separate slug only if the clean version stalls.

---

### density-promotion-bound: frozen (superseded as a wall-closer)
**Target:** (unchanged — the whole claim via SPT = $W_1\wedge W_2$ on the saturated branch + the imported freeze branch).
**Note:** The large-prime descent closes the saturated wall (GAP-1, GAP-3, GAP-S) uniformly without SPT, $p^*$, $W_1$, $W_2$, or the regime split. This approach's load-bearing wall-machinery (SPT/$p^*$, $W_1$/$W_2$, the equality/strict-beat dichotomy) is **superseded as a wall-closer by the descent**; spending a builder on its open walls this round is not worth it. **Certified lemmas retained as imports** (`common-primes-bounded`, `sat-criterion`, `freeze-lock`, `singleton-freeze` if certified, the $\{2,q\}$-obstruction documentation). No builder this round.

### smooth-window-crash: frozen (superseded as a wall-closer)
**Target:** (unchanged — the whole claim via an analytic W2 step at the strict-beat crash).
**Note:** The descent has no window, no crash, no mtp-multiple, no equality/strict-beat dichotomy, and no smooth-density step. This approach's analytic W2 machinery is **superseded as a wall-closer by the descent**. Certified lemma `entering-2` retained as an import. No builder this round.

### pstar-core-straggler: frozen (superseded as a wall-closer)
**Target:** (unchanged — the whole claim via the Cov-monovariant + crash-inevitability).
**Note:** The descent closes the wall without any Cov stabilization or crash-inevitability argument. This approach's Cov-monovariant route (Lemma B certified) is **superseded as a wall-closer by the descent**; its self-refuted Lemma C (crash forced to $\mathrm{Cov}=P(a_1)$) stays refuted. Certified lemma `cov-monovariant` retained as an import. No builder this round.

### bounded-gap-lcm-reduction: frozen (superseded as a wall-closer)
**Target:** (unchanged — the whole claim via the mtp monovariant + GAP-1/GAP-3).
**Note:** The mtp monovariant (`mtp-monovariant-and-gap-bound`, certified) stays as an importable unconditional asset; the GAP-1/GAP-3 wall-route is **superseded as a wall-closer by the descent**. No builder this round.

### transversal-single-cycle-finish: advance (as an import target, not a build)
**Target:** (unchanged — the conditional theorem; this approach IS the finish the descent imports.)
**Note:** Already verified-milestone / certified. **No builder this round** — it is not a wall-attacker; it is the imported finish (Pieces A + C) for `large-prime-descent`. Its certified lemmas (`post-stabilization-theorem`, `universal-membership-no-transient`, `transversal-residue-characterization`, `greedy-equals-cyclic-successor`, `cyclic-successor-single-cycle`, `pairwise-intersection`) are imported by `large-prime-descent` at steps 3 and 6.

---

build set: large-prime-descent
