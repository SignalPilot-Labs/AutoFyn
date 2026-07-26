## Status
partial

## Approaches tried
- `deviation-index-descent` (round 5, build) — Minimal-index descent on the first index where the increment-word $d_n$ deviates from a candidate period $P_0$, mounted on the CERTIFIED Steps 1–6 of `minimal-criminal-schur-contradiction` (re-targeted from the prime $q$ to the deviation index; NOT a Schur/cofactor argument). **Partial — CHANGES REQUESTED.** B1 (candidate period from pigeonhole on the finite alphabet $\{1,\dots,M_1\}$) is proved cleanly and is genuinely non-circular. The mount (Steps 1–6) is imported unchanged; the well-ordering transfers from governing primes to deviation-indices by the natural well-ordering of $\mathbb N$. The collapse step (no deviation $\Rightarrow$ $d_n$ is $P_0$-periodic $\Rightarrow$ $a_{n+T}=a_n+L$ via the certified `cyclic-successor-bijection`) is clean. BUT the load-bearing B2 (greedy local rewriting turns a deviation at index $n$ into a deviation at a SMALLER index) is an EXPLICIT GAP, with a SHARP OBSTRUCTION: the descent cannot be a uniform mechanism in the candidate period $P_0$, because for small window-lengths $w$ the pigeonhole offset $P_0(w)$ is NOT a period of $d$ (verified $a_1=35$, $w=2$: $P_0=5$, but the true period is $T=34$, and a real deviation at $n_0=8$ exists — $d_8=4\neq10=d_{13}$). Hence B2 would have to falsely conclude periodicity for wrong candidates if it were uniform; for B2 to have a chance, $w$ must satisfy $w\ge w_{\min}$ (the minimal window-length recovering the true period), but $w_{\min}$ is UNBOUNDED in $M_1$ (the round-4 `ergodic-window-state / increment-window-automaton` fence). So B2 reduces to a fenced quantity and cannot close. The greedy forced-increment identity $d_{m-1}=q-(a_{m-1}\bmod q)$ at $q$-multiple steps (the one genuine greedy-specific ingredient from the mount) does NOT rescue B2: it determines $d$ forward at $q$-multiple steps but provides no backward-propagation of deviations, and it does not identify which $w$ yields the true period. Verdict: CHANGES REQUESTED — B1 + mount + collapse are rigorous and reusable; B2 is an explicit gap with a sharp, computationally-verified obstruction (reduces to the increment-window fence, NOT to the cofactor-bound fence the reviewer warned about).

## Current best
The honest furthest progress: B1 (candidate-period existence) is proved and certified-sound by the reviewer; the mount (Steps 1–6 of `minimal-criminal-schur-contradiction`) is imported as a reusable well-ordering infrastructure; the collapse-to-endgame is a clean conditional. The open gap is B2, the descent step, and it is **structurally blocked**: the descent requires the candidate offset $P_0(w)$ to be the true period, which holds only for $w\ge w_{\min}$, and $w_{\min}$ is the round-4 fenced quantity (unbounded in $M_1$). This is a DIFFERENT fence from the cofactor-bound fence the reviewer flagged — it is the increment-window-automaton fence — but it is fenced nonetheless. The approach therefore does NOT close Gap A, and the descent mechanism (B2) is certified here as unprovable in this framing without first breaking the $w_{\min}$-unbounded fence.

## Full proof
Not yet complete. Gap A remains the single open wall. Below is the rigorous development of THIS approach: B1 proved, the mount imported, the collapse-to-endgame conditional, and the honest negative resolution of B2 (the descent is blocked by a sharp, computationally-verified obstruction).

---

### Setup and notation

Let $a_1,a_2,\dots$ be the greedy sequence: $a_{n+1}$ is the smallest integer $>a_n$ with $\gcd(a_{n+1},a_i)>1$ for every $i\le n$. Let $P_1$ be the set of prime divisors of $a_1$ and $M_1:=\operatorname{rad}(a_1)=\prod_{p\in P_1}p$. Let $d_n:=a_{n+1}-a_n$ (the $n$-th increment); by the certified `linchpin-and-gap-bound`, $d_n\in\{1,\dots,M_1\}$ for every $n$, so the **increment-word** $(d_n)_{n\ge1}$ is an infinite word over the finite alphabet $\Sigma:=\{1,\dots,M_1\}$.

### Target

Prove the whole theorem ($\exists\,T,L$ with $a_{n+T}=a_n+L$ eventually). The approach's distinctive route: **a minimal-counterexample descent on the first index where $d_n$ deviates from a candidate period $P_0$**, where $P_0$ is produced by pigeonhole-existence on the finite alphabet $\Sigma$ (NOT presupposing periodicity). The descent is mounted on the certified Steps 1–6 of `minimal-criminal-schur-contradiction`, but with the descent TARGET changed from the smallest governing prime $q>M_1$ (fenced: Schur/minimal-criminal-cofactor) to the smallest deviation-index.

### Imported certified lemmas (not re-proved)

- **`linchpin-and-gap-bound`** (round 1, unconditional): every $a_n$ is divisible by some $p\in P_1$; $d_n\le M_1$ for all $n$. Gives the finite alphabet $\Sigma=\{1,\dots,M_1\}$.
- **`binfinity-divisibility-progression-structure`** (round 3, unconditional): $\mathcal B_\infty=\bigcup_{T\in\operatorname{MT}(\mathcal F_\infty)}\operatorname{rad}(T)\mathbb Z$.
- **`greedy-equals-cyclic-successor`** (round 1) and **`cyclic-successor-bijection`** (round 1): once $\mathcal B_\infty$ is $L$-periodic, $a_{n+T}=a_n+L$ for all $n\ge1$ (the certified endgame).
- **`syndetic-divisible-closed-not-periodic`** (round 3, negative guardrail): pure statics (divisibility-closure + syndeticity) do NOT force periodicity — any viable periodicity proof MUST use a greedy-specific dynamic property.
- The **Steps 1–6 mount** of `minimal-criminal-schur-contradiction` (round 4, reviewer-certified SOUND): if Gap A fails, let $q$ be the smallest governing prime $>M_1$; then $q\mid a_n$ for infinitely many $n$, at each such index $a_{n-1}\bmod q\in[q-M_1,q-1]$ with $d_{n-1}=q-(a_{n-1}\bmod q)$ FORCED, and $P_1$ always provides a small-prime transversal of the prior non-$q$-multiple supports.

---

### Step 1 — Restate the ported crux templates (`aimo-0077`, `aimo-0009`) precisely

The two crux templates the approach adapts (per the round-5 crux-corpus pull, `/tmp/round-5/math-explorer-crux-corpus-pull.md`):

**`aimo-0077` (Germany TST 2010) — minimal-index-on-state-cycle descent.** *Original crux move.* Assume nontermination forces a repeating state-cycle; take the minimal-index object acted on within that cycle, and show restoring it would require a forbidden smaller-index action. *Ported form (re-proved from scratch below).* Suppose an infinite word $w=(w_n)_{n\ge1}$ over a finite alphabet has a "candidate period" $P_0$ (an offset at which a length-$k$ window coincides with a later copy). Suppose further that the word is NOT eventually $P_0$-periodic. Let $n_0$ be the smallest index at which $w_{n_0+P_0}\neq w_{n_0}$ (well-ordering of $\mathbb N$). A descent is a mechanism that, from the deviation at $n_0$, produces a deviation at some $m<n_0$, contradicting minimality. If the descent mechanism is valid, no deviation exists and $w$ is $P_0$-periodic.

**`aimo-0009` (IMO-SL 2013 A4) — modular-exclusion-jump template.** *Original crux move.* Take the smallest counterexample $i$ to a self-referential index bound, use periodicity to forbid a residue window, force the value to jump into the next period, collapse via minimality. *Ported form (template only; the literal use is circular since it presupposes periodicity).* The "exclude-a-block + force-a-jump + collapse" SHAPE pairs with `aimo-0077`: at the deviation index $n_0$, the greedy rule excludes a block of would-be continuations (the integers in $(a_{n_0}, a_{n_0+1})$ are all inadmissible), forcing the increment to jump to $d_{n_0}$; minimality then collapses the jump backward. **The literal `aimo-0009` mechanism requires a pre-existing period to run the residue-exclusion; we are trying to PROVE periodicity, so only the template's SHAPE is borrowed, and every borrowed step must be re-proved from scratch (per CLAUDE.md).** The re-proof is the content of Step 4 (B2) below — and it FAILS (see the honest obstruction there).

**Concrete meaning of "deviation from a candidate period."** Given the increment-word $(d_n)$ and a candidate period $P_0$ (an offset produced by pigeonhole-existence, see Step 2), the word **deviates from $P_0$ at index $n$** iff $d_{n+P_0}\neq d_n$. The word is **$P_0$-periodic from index $i_0$ onward** iff $d_{n+P_0}=d_n$ for all $n\ge i_0$. The **first deviation** (if any) is $n_0:=\min\{n\ge i_0+w : d_{n+P_0}\neq d_n\}$, where $w$ is the coincidence-window length and $i_0$ is the coincidence start (see Step 2); by the well-ordering of $\mathbb N$, $n_0$ exists iff the word is not $P_0$-periodic from $i_0$ onward.

### Step 2 — B1: the candidate period from pigeonhole-existence (PROVED, non-circular)

**Lemma (B1 — candidate-period existence, non-circular).** For every window length $w\ge1$, there exist indices $i<j$ with $d_{i+k}=d_{j+k}$ for $k=0,\dots,w-1$. The offset $P_0:=j-i$ is a **candidate period** of the increment-word. This existence is NON-circular: it uses only the finiteness of the alphabet $\Sigma=\{1,\dots,M_1\}$ (certified by `linchpin-and-gap-bound`) and the infiniteness of the word; it does NOT presuppose that $d$ is eventually periodic, and it does NOT bound $P_0$ a priori (the bound, if any, is the descent's job to supply — and see Step 4 for why it cannot).

*Proof.* Fix $w\ge1$. The word $(d_n)_{n\ge1}$ is infinite, and each $d_n\in\Sigma$ where $|\Sigma|=M_1<\infty$. The number of distinct length-$w$ blocks over $\Sigma$ is at most $M_1^w<\infty$. Consider the infinite sequence of length-$w$ windows $B_i:=(d_i,\dots,d_{i+w-1})$ for $i=1,2,3,\dots$. By the (infinite) pigeonhole principle, some two of these windows coincide: $\exists\,i<j$ with $B_i=B_j$, i.e. $d_{i+k}=d_{j+k}$ for $k=0,\dots,w-1$. Set $P_0:=j-i>0$. ∎

**Non-circularity check (explicit).** The lemma's hypothesis is "$d$ is an infinite word over a finite alphabet" — both unconditional facts (the word is infinite because the greedy never terminates, $a_n\to\infty$ by $d_n\ge1$; the alphabet is finite by `linchpin-and-gap-bound`). The conclusion is "a coincidence exists." No hypothesis or conclusion mentions periodicity of $d$, finiteness of governing primes, $\mathcal B_\infty$, or any Gap-A-adjacent quantity. The candidate $P_0$ is some positive integer produced by pigeonhole; it is NOT assumed to be a period (the descent, Step 4, is supposed to prove it is — or rather, prove some candidate is). This is option (b) of the outline; options (a) (couple to `two-coincidence-periodicity`'s abstraction — single-gap-trap risk) and (c) (use `block-index-advance`'s conditional period — circular, since `block-index-advance` carries no periodicity content and the conditional period is Gap-A-dependent) are correctly barred. ∎_(non-circularity verified.)

**The candidate $P_0$ depends on $w$.** The lemma supplies, for EACH $w$, SOME offset $P_0(w)$. Different $w$'s give different offsets in general (verified $a_1=35$: $w=2\Rightarrow P_0=5$, $w=4\Rightarrow P_0=14$, $w=8\Rightarrow P_0=34$, etc.). The descent (Step 4) must work for the chosen $w$; this is where the obstruction bites (see Step 4).

### Step 3 — Import the mount (Steps 1–6 of `minimal-criminal-schur-contradiction`)

The certified Steps 1–6 of `minimal-criminal-schur-contradiction` are imported VERBATIM as the well-ordering infrastructure. We cite them by name and do NOT re-derive the (fenced) Schur cofactor Step 7 — that is certified dead by `schur-cofactor-premise-fails-in-periodic-regime`.

**Mount summary (reviewer-certified, round 4).** If Gap A fails, the set of governing primes is unbounded, so by the well-ordering of $\mathbb N$ there is a smallest governing prime $q>M_1$. Then:
- (Step 2) every prime $p\in(M_1,q)$ is MT-transient;
- (Step 3) $q\mid a_n$ for infinitely many $n$;
- (Step 4) at each $q$-multiple step $a_n$ (with $n\ge2$), the gap bound $d_{n-1}\le M_1<q$ forces $d_{n-1}=q-(a_{n-1}\bmod q)$, so $a_{n-1}\bmod q\in\{q-M_1,\dots,q-1\}$ (the "top window" of size $M_1$);
- (Step 5) the cofactor $k_i=a_{n_i}/q$ has $\operatorname{primefactors}(k_i)$ transversing the prior non-$q$-multiple supports;
- (Step 6) $P_1$ always provides a small-prime transversal of those supports (so a $P_1$-smooth cofactor is always admissible).

**How the well-ordering transfers from primes to deviation-indices.** The mount well-orders the governing primes $>M_1$ (Step 1 of the mount). The deviation-index descent well-orders a DIFFERENT set: the set of deviation-indices $\{n\ge i_0+w : d_{n+P_0}\neq d_n\}$ (Step 1 of THIS proof). Both well-orderings are instances of the well-ordering of $\mathbb N$ — they are the SAME well-ordering principle, applied to different sets. The transfer is: the mount gives us the infrastructure (the smallest governing $q>M_1$, the forced-increment identity at $q$-multiple steps, the cofactor-transversal structure); the deviation descent USES this infrastructure (specifically the forced-increment identity) as a candidate "forbidden smaller-index action" mechanism. The descent's target is the deviation-index, NOT the prime $q$ — this is the re-targeting the outline mandates, and it does NOT re-walk the fenced Schur Step 7.

**The forced-increment identity is the genuine greedy-specific ingredient.** Among the mount's ingredients, only Step 4's forced-increment identity $d_{n-1}=q-(a_{n-1}\bmod q)$ at $q$-multiple steps is a greedy-DYNAMIC property (it uses the gap bound $d_{n-1}\le M_1<q$ AND the greedy rule's selection of a $q$-multiple). The other ingredients (well-ordering, transience, cofactor-transversal, $P_1$-transversal) are STATIC. Per the `syndetic-divisible-closed-not-periodic` guardrail, only a dynamic property can force periodicity — so the forced-increment identity is the only mount ingredient that could, in principle, power the descent. (Step 4 below shows it does NOT suffice.)

### Step 4 — B2: the descent (EXPLICIT GAP — sharp obstruction)

**The descent goal (B2).** Suppose $d$ is NOT $P_0$-periodic from $i_0$ onward. Let $n_0$ be the first deviation (Step 1). Exhibit a greedy local rewriting: from the deviation at $n_0$, produce a deviation at some $m<n_0$, contradicting the minimality of $n_0$. Collapse by well-ordering $\Rightarrow$ no deviation $\Rightarrow$ $d$ is $P_0$-periodic.

**The shift-by-$C$ structure (precise setup).** Let $i_0<j_0$ be the coincidence pair from B1 (so $d_{i_0+k}=d_{j_0+k}$ for $k=0,\dots,w-1$, and $P_0=j_0-i_0$). Define the shift $C:=a_{j_0}-a_{i_0}=\sum_{k=i_0}^{j_0-1}d_k$. **Claim (telescoping).** If $d_{m+P_0}=d_m$ for all $m\in[i_0,n_0-1]$ (the "no deviation before $n_0$" hypothesis), then $a_{m+P_0}=a_m+C$ for all $m\in[i_0,n_0]$. *Proof.* $a_{m+P_0+1}-a_{m+P_0}=d_{m+P_0}=d_m=a_{m+1}-a_m$, so the difference $a_{m+P_0}-a_m$ is constant on $[i_0,n_0]$, equal to its value at $m=i_0$, namely $a_{i_0+P_0}-a_{i_0}=a_{j_0}-a_{i_0}=C$. ∎

So on the range $[i_0,n_0]$, thread $B:=(a_{i_0+P_0},\dots,a_{n_0+P_0})$ equals thread $A:=(a_{i_0},\dots,a_{n_0})$ shifted by $C$: $a_{m+P_0}=a_m+C$. The deviation at $n_0$ ($d_{n_0+P_0}\neq d_{n_0}$) is equivalent to $a_{n_0+1+P_0}\neq a_{n_0+1}+C$ — the shift-by-$C$ symmetry breaks at $n_0+1$.

**The deviation means the admissibility structures mismatch.** By the greedy rule:
- $a_{n_0+1}=a_{n_0}+d_{n_0}$ is the smallest integer $>a_{n_0}$ admissible against $\{a_1,\dots,a_{n_0}\}$;
- $a_{n_0+1+P_0}=a_{n_0+P_0}+d_{n_0+P_0}=a_{n_0}+C+d_{n_0+P_0}$ is the smallest integer $>a_{n_0+P_0}=a_{n_0}+C$ admissible against $\{a_1,\dots,a_{n_0+P_0}\}$.

If $d_{n_0+P_0}>d_{n_0}$ (Case i), then $a_{n_0}+C+d_{n_0}=a_{n_0+1}+C$ is NOT admissible against $\{a_1,\dots,a_{n_0+P_0}\}$ (else it would be $a_{n_0+1+P_0}$, since $d_{n_0}<d_{n_0+P_0}$). So $\exists\,j\le n_0+P_0$ with $\gcd(a_{n_0+1}+C,a_j)=1$. But $a_{n_0+1}$ IS admissible against $\{a_1,\dots,a_{n_0}\}$, so $\gcd(a_{n_0+1},a_k)>1$ for all $k\le n_0$.

The "bad" index $j$ (with $\gcd(a_{n_0+1}+C,a_j)=1$) cannot be in $[i_0,n_0]$ AND be a shift-image of a "good" index — because for $j\in[i_0+P_0,n_0+P_0]$ (the shift-image range), $a_j=a_{j-P_0}+C$, and $\gcd(a_{n_0+1}+C,a_{j-P_0}+C)$ has NO forced relation to $\gcd(a_{n_0+1},a_{j-P_0})$ (adding $C$ to both arguments of a gcd does not preserve it). **The shift-by-$C$ does NOT preserve the admissibility structure unless $C$ is divisible by every prime appearing in any $a_k$ for $k\in[i_0,n_0]$** — i.e. unless $C$ is a multiple of every governing prime, which is a COFACTOR-TYPE bound (certified fenced by `window-uniqueness-reduces-to-cofactor` and `lemma-C-strip-no-go`). 

Symmetrically for $d_{n_0+P_0}<d_{n_0}$ (Case ii): $a_{n_0}+d_{n_0+P_0}$ is NOT admissible against $\{a_1,\dots,a_{n_0}\}$, so $\exists\,k\le n_0$ with $\gcd(a_{n_0}+d_{n_0+P_0},a_k)=1$; but $a_{n_0}+C+d_{n_0+P_0}=a_{n_0+P_0+1}$ IS admissible against $\{a_1,\dots,a_{n_0+P_0}\}$, and in particular $\gcd(a_{n_0}+C+d_{n_0+P_0},a_{k+P_0})>1$ for $k\in[i_0,n_0]$ (shift-image range), i.e. $\gcd(a_{n_0}+C+d_{n_0+P_0},a_k+C)>1$. Again, no forced relation to $\gcd(a_{n_0}+d_{n_0+P_0},a_k)$ unless $C$ is a multiple of all governing primes (cofactor-type, fenced).

**Neither case yields a smaller-index deviation.** The mismatch between thread $A$'s admissibility and thread $B$'s admissibility is caused by "extra" terms in thread $B$ (the indices $j\in\{1,\dots,i_0+P_0-1\}\cup\{n_0+1,\dots,n_0+P_0\}$ not covered by the shift relation on $[i_0,n_0]$) and by the shift-$C$'s failure to preserve gcd. To turn this mismatch into a deviation at $m<n_0$, we would need EITHER:
- **(B2-a)** the shift-$C$ to preserve admissibility globally — i.e. $C$ divisible by all governing primes (COFACTOR-TYPE, fenced by `window-uniqueness-reduces-to-cofactor`, `lemma-C-strip-no-go`, `schur-cofactor-premise-fails-in-periodic-regime`); OR
- **(B2-b)** the shift relation $a_{m+P_0}=a_m+C$ to hold for ALL $m\ge1$ (not just $m\in[i_0,n_0]$) — which requires the coincidence window to extend back to $m=1$, i.e. $d_{1+P_0}=d_1,\dots,d_{P_0+P_0-1}=d_{P_0-1}$; this is a STRONGER coincidence than pigeonhole supplies, and is in fact CIRCULAR (it presupposes the periodicity we are trying to prove).

**(B2-a) and (B2-b) are both unavailable.** (B2-a) is the cofactor-bound fence the outline-reviewer explicitly warned about ("the `window-uniqueness-reduces-to-cofactor` fence warns that B2 must NOT reduce to cofactor-prime bounding"). (B2-b) is circular. **The descent cannot be mounted.**

### Step 4' — A SHARPER obstruction: B2 cannot be a uniform mechanism in $w$ (computational refutation)

The above shows the descent mechanism, as stated, requires a fenced or circular ingredient. There is a SHARPER, computationally-verified obstruction: the descent **cannot be a uniform mechanism in the window-length $w$**, because for small $w$ the pigeonhole offset $P_0(w)$ is NOT a period of $d$, and a real deviation exists (no contradiction is possible).

**Lemma (B2 non-uniformity — computational refutation).** The pigeonhole offset $P_0(w)$ depends on $w$, and for small $w$ it is NOT a period of the increment-word. Consequently, the descent (which concludes "no deviation exists, hence $d$ is $P_0$-periodic") would FALSELY conclude periodicity if it were a uniform mechanism in $w$.

*Computational witness ($a_1=35$, $M_1=35$).*$\ $The greedy sequence has true period $T=34$, $L=210$ (verified $1200$ terms). Applying B1 with $w=2$: the first coincidence of length-$2$ windows is at $i_0=5$, $j_0=10$, giving candidate $P_0(2)=5$. But $d_{n+5}\neq d_n$ at $n_0=8$: $d_8=4$ while $d_{13}=10$ (verified directly: $d_{5..14}=(10,5,5,4,6,10,5,5,10,6)$). So $P_0(2)=5$ is NOT a period; a real deviation exists at $n_0=8$; the descent's conclusion ("no deviation") is FALSE for $w=2$.

Applying B1 with $w=8$: the first coincidence is at $i_0=0$, $j_0=34$, giving $P_0(8)=34=T$, and NO deviation exists in the computed range (verified $1200$ terms). So the descent's conclusion is TRUE for $w=8$.

**Consequence.** If the descent mechanism (B2) were a valid uniform argument, it would conclude "no deviation, $d$ is $P_0$-periodic" for EVERY $w$ — including $w=2$, where the conclusion is false. Hence B2 is NOT a valid uniform mechanism. For B2 to have a chance, the window-length $w$ must satisfy $w\ge w_{\min}$, where $w_{\min}$ is the minimal window-length recovering the true period. But $w_{\min}$ is **UNBOUNDED in $M_1$** — this is precisely the round-4 `ergodic-window-state / increment-window-automaton` fence (verified $a_1=847$, $M_1=77$: $w_{\min}>24$; $a_1=385$, $M_1=385$: $w_{\min}\approx100$, state size $\approx T=5088$). **B2 therefore reduces to the increment-window-automaton fence, a fenced quantity.**

This is a DIFFERENT fence from the cofactor-bound fence the outline-reviewer flagged (Step 4's (B2-a)), but it is fenced nonetheless. The descent cannot be mounted without first breaking the $w_{\min}$-unbounded fence, which is a certified dead end (round 4).

### Step 4'' — The forced-increment identity does NOT rescue B2

The mount's only greedy-DYNAMIC ingredient (per the `syndetic-divisible-closed-not-periodic` guardrail) is the forced-increment identity $d_{m-1}=q-(a_{m-1}\bmod q)$ at $q$-multiple steps (where $q$ is the smallest governing prime $>M_1$, IF Gap A fails). Could this identity supply the "forbidden smaller-index action" without reducing to a fenced quantity?

**No — and here is the precise reason.** The forced-increment identity determines $d$ FORWARD at $q$-multiple steps: given $a_{m-1}\bmod q$ and the fact $q\mid a_m$, the value $d_{m-1}$ is forced. The deviation descent requires a BACKWARD-propagation: from a deviation at $n_0$, produce a deviation at $m<n_0$. The forced-increment identity gives no backward propagation, for two independent reasons:

1. **It does not identify the deviation index as a $q$-multiple step.** For the forced-increment identity to constrain $d_{n_0}$ or $d_{n_0+P_0}$, we would need $a_{n_0+1}$ or $a_{n_0+1+P_0}$ to be a $q$-multiple — but the deviation index $n_0$ is determined by the d-word's coincidence structure, NOT by the $q$-multiple pattern. We have no control over whether $a_{n_0+1}$ is a $q$-multiple.

2. **Even if both $a_{n_0+1}$ and $a_{n_0+1+P_0}$ are $q$-multiples**, the forced-increment identity gives $d_{n_0}=q-(a_{n_0}\bmod q)$ and $d_{n_0+P_0}=q-(a_{n_0+P_0}\bmod q)=q-((a_{n_0}+C)\bmod q)$ (using the shift relation on $[i_0,n_0]$). The deviation $d_{n_0+P_0}\neq d_0$ becomes $(a_{n_0}+C)\bmod q\neq a_{n_0}\bmod q$, i.e. $q\nmid C$. This is a STATEMENT about $C$ and $q$, not a smaller-index deviation. To turn "$q\nmid C$" into a deviation at $m<n_0$ would require $d_m$ and $d_{m+P_0}$ to also be forced (both $q$-multiples) AND to differ — which requires the $q$-multiple pattern to itself deviate from $P_0$-periodicity, i.e. requires the very periodicity we are trying to prove.

**The forced-increment identity is forward and local; the descent needs backward and global.** The two do not connect. ∎_(B2 is an explicit gap; the forced-increment identity does not close it.)

### Step 5 — The collapse (CONDITIONAL on B2 — clean, but B2 is blocked)

IF B2 were proved (the descent succeeds), then no deviation exists, i.e. $d_{n+P_0}=d_n$ for all $n\ge i_0$. The increment-word is eventually $P_0$-periodic. Summing one period: $\sum_{k=0}^{P_0-1}d_{n_0+k}=L_0$ (constant for all $n\ge i_0$), so $a_{n+P_0}=a_n+L_0$ for all $n\ge i_0$, with $T=P_0$, $L=L_0$. This is the theorem (eventual AP). Moreover, by the certified `greedy-equals-cyclic-successor` + `cyclic-successor-bijection`, the periodicity extends to $n=1$ (pure-from-start). ∎_(conditional on B2; B2 is blocked, so this collapse is NOT achieved.)

### Honest status of this approach

- **B1 (candidate period)** is proved and non-circular (Step 2).
- **The mount (Steps 1–6)** is imported unchanged (Step 3); the well-ordering transfers from primes to deviation-indices by the same well-ordering principle.
- **The collapse (Step 5)** is clean and conditional on B2.
- **B2 (the descent)** is an EXPLICIT GAP, blocked by TWO independent obstructions:
  - **(B2-a)** the shift-by-$C$ does not preserve admissibility unless $C$ is divisible by all governing primes (COFACTOR-TYPE, fenced — the fence the reviewer warned about); AND
  - **(B2- Sharp)** B2 cannot be a uniform mechanism in $w$, because for small $w$ the pigeonhole offset $P_0(w)$ is NOT a period (verified $a_1=35$, $w=2\Rightarrow P_0=5\neq T=34$, real deviation at $n_0=8$); for B2 to have a chance, $w\ge w_{\min}$, and $w_{\min}$ is UNBOUNDED in $M_1$ (the round-4 increment-window-automaton fence).
- The forced-increment identity (the mount's only dynamic ingredient) does NOT rescue B2 (Step 4''): it is forward and local, the descent needs backward and global.

The approach therefore does NOT close Gap A. B2 is a genuine open gap with a sharp, computationally-verified obstruction, and the obstruction is a fenced quantity (two fences, in fact: the cofactor-bound fence and the increment-window-automaton fence).

### Cases covered

- **LOCK sub-case** ($a_n$ prime-power term): certified by `lock-lemma` ($T=1,L=p$). The deviation-index descent is for the NON-LOCK case; no conflict.
- **$|P_1|=2$ NON-LOCK** (e.g. $a_1=15,35,77,91$): the descent obstruction (B2-Sharp) is verified computationally on $a_1=35$ ($|P_1|=2$, $M_1=35$, $w=2$ gives wrong candidate $P_0=5$). No advantage here.
- **$|P_1|\ge3$ NON-LOCK**: general case; the obstruction is the same (B1 holds for any $M_1$, B2 fails for the same two reasons).

### Watch out for (transmitted to future builders)

- B1 (candidate period from pigeonhole on the finite alphabet) is SOUND and non-circular — do NOT re-derive it; reuse it.
- B2 (the descent) is BLOCKED by two fences: the cofactor-bound fence (B2-a, the shift-by-$C$ must preserve admissibility, requiring $C$ divisible by all governing primes) AND the increment-window-automaton fence (B2-Sharp, $w_{\min}$ unbounded in $M_1$). Do NOT retry the descent without first breaking ONE of these fences.
- The forced-increment identity $d_{m-1}=q-(a_{m-1}\bmod q)$ at $q$-multiple steps is the mount's only dynamic ingredient, but it is FORWARD and LOCAL; it does not supply a backward-propagation of deviations.
- Do NOT couple to `two-coincidence-periodicity` for the candidate period (single-gap-trap risk; the outline explicitly bars option (a)).
- Do NOT use `block-index-advance`'s conditional period (option (c), circular — `block-index-advance` carries no periodicity content, only the trivial $b_{n+1}-b_n\in\{0,1\}$ consequence of the gap bound).

## Promotable lemmas

- **`candidate-period-pigeonhole-existence`** (positive, unconditional). *Statement.* For the increment-word $(d_n)_{n\ge1}$ over the finite alphabet $\Sigma=\{1,\dots,M_1\}$ (certified by `linchpin-and-gap-bound`), for every window-length $w\ge1$ there exist indices $i<j$ with $d_{i+k}=d_{j+k}$ for $k=0,\dots,w-1$. The offset $P_0:=j-i$ is a candidate period. This existence is non-circular (uses only the finiteness of $\Sigma$ and the infiniteness of the word; presupposes no periodicity, bounds $P_0$ a priori by nothing). *Caveat:* the candidate $P_0(w)$ is NOT necessarily a period of $d$ for small $w$; the descent must prove it is (or prove some candidate is), and this is blocked (see B2 obstruction). Proved in Step 2 above. Proposed for certification into `results/imo-2026-06/lemmas/` as a reusable sound ingredient (the pigeonhole-existence half of any deviation-descent route).

- **`deviation-descent-blocked-by-wmin-fence`** (negative, structural). *Statement.* The deviation-index descent (B2 of `deviation-index-descent`) cannot be a uniform mechanism in the window-length $w$: for small $w$ the pigeonhole offset $P_0(w)$ is not a period of $d$ (computational witness: $a_1=35$, $w=2\Rightarrow P_0=5\neq T=34$, real deviation at $n_0=8$). For the descent to have a chance, $w\ge w_{\min}$ (the minimal window-length recovering the true period), but $w_{\min}$ is UNBOUNDED in $M_1$ (the round-4 increment-window-automaton fence). Moreover, the shift-by-$C$ does not preserve admissibility unless $C$ is divisible by all governing primes (cofactor-type, fenced by `window-uniqueness-reduces-to-cofactor`). Consequently the deviation-descent route is blocked by two fences (cofactor-bound AND increment-window-automaton), and the forced-increment identity (forward, local) does not rescue it. Proved in Steps 4, 4', 4'' above. Proposed for certification as a negative lemma fencing off future deviation-descent retries that do not first break one of the two fences.
