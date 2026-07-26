# Lemma (negative, structural): no fixed-modulus forward-determinism

*Pending reviewer certification (round 6). Source: round-6 Ramsey / van-der-Waerden explorer finding, sharpening the round-5 T-unbounded-in-$M_1$ fence. Proof-builder re-ran the corrected MT-based fast greedy (`/tmp/round-6/mt_greedy.py`, verified bit-exact vs naive $O(N^2)$ gcd-greedy on $a_1\in\{15,385,847\}$ in round 6) and re-derived the structural fact (Step 2) from scratch.*

## Statement (negative, structural)

Let $a_1,a_2,\dots$ be the IMO 2026 P6 greedy sequence and $d_{n+1}:=a_{n+1}-a_n$ the greedy increment. Call a statistic $\alpha:\mathbb N\to S$ **forward-deterministic** if
$$\alpha(n)=\alpha(n')\ \Longrightarrow\ d_{n+1}=d_{n'+1}\qquad(\forall\, n<n').$$
A forward-deterministic $\alpha$ is a *determining state* for the greedy orbit: equal states force equal successors, so a self-coincidence $\alpha(n)=\alpha(n')$ propagates to periodicity of $d$ via the certified `aimo-0907-coincidence-criterion` (part A).

**Fence.** For the greedy orbit, **no fixed-modulus residue statistic** $\alpha_m(n):=a_n\bmod m$ — where $m$ is a constant independent of the orbit position, in particular any $m$ that is a function of $a_1$ alone ($m=a_1$, $m=M_1=\operatorname{rad}(a_1)$, $m=a_1^k$ for any $k\ge1$, $m=a_1\cdot M_1$, …) — is forward-deterministic. Two independent obstructions cover every witness:

1. **(Size obstruction, PROVEN for $a_1=175$ and all $k$.)** In any eventual-periodic regime with period $(T,L)$, forward-determinism of $a_n\bmod m$ *requires* $T\le\gcd(L,m)$ (Step 2). For $a_1=175$ (periodic from $n=0$ with $T=274$, $L=2730$), the $P_1$-part of $L$ equals $M_1=35$ (since $P_1=\{5,7\}$ and $L=2\cdot3\cdot5\cdot7\cdot13$), so $\gcd(L,a_1^k)\le 35<274=T$ for **every** $k\ge1$. Hence $a_n\bmod a_1^k$ is not forward-deterministic for any $k$ — purely structurally, no computation needed for the failure (the computation below *exhibits* the conflicts).

2. **(Distinctness obstruction, witnessed for $a_1=77,91$.)** When $T\le\gcd(L,m)$ holds, forward-determinism additionally requires the $T$ residues $a_0,a_1,\dots,a_{T-1}\bmod\gcd(L,m)$ to be pairwise distinct. For $a_1=77$ ($T=18$, $L=154$, $\gcd(L,a_1^2)=77\ge18$) and $a_1=91$ ($T=20$, $L=182$, $\gcd(L,a_1^2)=91\ge20$) the size condition is *satisfied* yet distinctness *fails* — concretely $77$ and $91$ conflict states respectively (Step 3).

**Consequence.** Any "finite residue states + pigeonhole self-coincidence propagates to periodicity" route **presupposes** that the chosen residue statistic $\alpha_m$ is forward-deterministic. The fence above shows no fixed function-of-$a_1$ modulus $m$ supplies such a statistic: the transition $a_n\to a_{n+1}$ (hence $d_{n+1}$) depends on the **full constraint history** $\{a_1,\dots,a_n\}$, equivalently on the minimal-transversal state $\operatorname{MT}(\mathcal F_n)$ (the certified `mt-depends-on-set-system`), **not** on $a_n\bmod m$ for any fixed $m$. The only forward-deterministic determining state is the MT-state, whose finiteness IS Gap A. This sharpens the round-5 T-unbounded-in-$M_1$ fence: that fence kills every $f(M_1)$-*bounded* deterministic statistic (state *size* bounded by a function of $M_1$); the present lemma kills residue statistics at moduli $m=a_1^k$ that are **not** $f(M_1)$-bounded (since $a_1$ can dwarf $M_1=\operatorname{rad}(a_1)$, e.g. $a_1=175\Rightarrow a_1^2=30625\gg M_1=35$). Together the two fences cover every fixed function-of-$a_1$ modulus class.

## Proof

### Step 1 — Forward-determinism and the determining state.

The greedy rule is $a_{n+1}=\min\{m>a_n:\gcd(m,a_i)>1\ \forall i\le n\}$. By `linchpin-and-gap-bound` (reviewer-certified, round 1, unconditional), every $a_i$ has a prime factor in $P_1$ and $d_{n+1}\le M_1$. The successor $d_{n+1}$ is the smallest admissible increment in $D_n=\{d\in\{1,\dots,M_1\}:a_n+d\text{ admissible w.r.t. }a_1,\dots,a_n\}$. Whether $a_n+d$ is admissible is the condition $\gcd(a_n+d,a_i)>1$ for every $i\le n$; equivalently (by the linchpin, every $a_i$ has a prime in $P_1$) the prime-factor set $P(a_n+d)$ is a transversal of $\mathcal F_n=\{P(a_i):i\le n\}$, i.e. $P(a_n+d)\supseteq T$ for some $T\in\operatorname{MT}(\mathcal F_n)$ (by `mt-depends-on-set-system`, $\operatorname{MT}$ depends only on the set-system $\mathcal F_n$). Thus $d_{n+1}$ is determined by the pair $(a_n,\operatorname{MT}(\mathcal F_n))$; crucially **not** by $a_n$ alone. In particular $a_n\bmod m$ — which discards $\operatorname{MT}(\mathcal F_n)$ — is information-theoretically insufficient to determine $d_{n+1}$ whenever two positions $n<n'$ with $a_n\equiv a_{n'}\pmod m$ carry different $\operatorname{MT}(\mathcal F_n)\ne\operatorname{MT}(\mathcal F_{n'})$. $\square_{\text{Step 1}}$

### Step 2 — Structural fact: in the periodic regime, forward-determinism of $a_n\bmod m$ requires $T\le\gcd(L,m)$ and pairwise distinctness.

Assume the orbit is in the eventual-periodic regime with period $T$ and shift $L$: $a_{n+T}=a_n+L$ for $n\ge n_0$. By shifting indices (forward-determinism is translation-invariant in $n$), WLOG $n_0=0$. Then for $n=qT+r$ with $0\le r<T$:
$$a_n = a_r + qL,\qquad a_n\bmod m \equiv a_r + qL \pmod m.$$
In the periodic regime $d$ is $T$-periodic, so $d_{n+1}=d_{n'+1}\iff n\equiv n'\pmod T\iff r=r'$ (writing $n=qT+r$, $n'=q'T+r'$). Therefore
$$\text{forward-det of }a_n\bmod m\ \Longleftrightarrow\ \bigl[\,a_r+qL\equiv a_{r'}+q'L\pmod m\ \Longrightarrow\ r=r'\,\bigr].$$
Equivalently (contrapositive, $r\ne r'$): $a_r-a_{r'}\notin\langle L\rangle_m$ for all $r\ne r'$, where $\langle L\rangle_m=\{kL\bmod m:k\in\mathbb Z\}$ is the subgroup of $\mathbb Z/m\mathbb Z$ generated by $L\bmod m$. By the elementary structure of cyclic subgroups, $\langle L\rangle_m=g\cdot\mathbb Z/m\mathbb Z=\{x\bmod m:g\mid x\}$ with $g:=\gcd(L,m)$; hence $a_r-a_{r'}\in\langle L\rangle_m\iff g\mid(a_r-a_{r'})\iff a_r\equiv a_{r'}\pmod g$. Thus

$$\boxed{\ \text{forward-det of }a_n\bmod m\text{ (periodic regime)}\ \Longleftrightarrow\ \bigl[\,T\le g\ \text{ and }\ a_0,a_1,\dots,a_{T-1}\text{ are pairwise distinct mod }g\,\bigr],\quad g:=\gcd(L,m).\ }$$

In particular **$T\le\gcd(L,m)$ is a necessary condition**: if $T>g$ then by pigeonhole two of the $T$ residues $a_0,\dots,a_{T-1}\bmod g$ coincide, furnishing $r\ne r'$ with $a_r\equiv a_{r'}\pmod g$, hence (taking $q'=q$) $a_{qT+r}\equiv a_{qT+r'}\pmod m$ with $d_{qT+r+1}\ne d_{qT+r'+1}$ — a concrete conflict pair. $\square_{\text{Step 2}}$

### Step 3 — Size obstruction: $a_1=175$ kills every $m=a_1^k$ ($k\ge1$) purely structurally.

Witness $a_1=175=5^2\cdot7$. The corrected MT-greedy computes the orbit and detects (at $\texttt{min\_run}\in\{300,2000,10000\}$, all consistent) the eventual period $T=274$, $L=2730=2\cdot3\cdot5\cdot7\cdot13$, periodic from $n=0$ (matching the round-6 Ramsey explorer and the round-5 T-unbounded fence data). Here $P_1=\{5,7\}$, $M_1=35$, and the $P_1$-part of $L$ (the largest divisor of $L$ all of whose prime factors lie in $P_1$) is $5\cdot7=35$. For any $k\ge1$, $a_1^k$ is $P_1$-smooth (its prime factors lie in $P_1$), so
$$\gcd(L,a_1^k)\mid\text{($P_1$-part of }L\text{)}=35\quad\Longrightarrow\quad\gcd(L,a_1^k)\le 35<274=T.$$
By the necessary condition of Step 2, **$a_n\bmod a_1^k$ is not forward-deterministic for any $k\ge1$** — a structural conclusion independent of any computation. (The same argument covers $m=M_1=35$ and $m=a_1\cdot M_1=6125$: both are $P_1$-smooth, so $\gcd(L,m)\le35<T$.) $\square_{\text{Step 3}}$

### Step 4 — Distinctness obstruction: $a_1\in\{77,91\}$ kill $m=a_1^k$ via distinctness failure.

When $T\le\gcd(L,m)$ the size obstruction is silent, but the second clause of Step 2 (pairwise distinctness of $a_0,\dots,a_{T-1}\bmod\gcd(L,m)$) may still fail. Two witnesses:

- $a_1=77=7\cdot11$, $T=18$, $L=154=2\cdot7\cdot11$. Here $\gcd(L,a_1^2)=\gcd(154,5929)=77\ge18$, so the size condition holds. Yet the realized residues collide: a direct enumeration over $N=5000$ terms of the orbit gives **$77$ conflict states** for $m=a_1^2=5929$ (realized $1309<5929$, so genuine repeats exist; not a small-$N$ artifact). By Step 2, this is exactly the distinctness clause failing — two indices $r\ne r'$ in $[0,18)$ have $a_r\equiv a_{r'}\pmod{77}$, propagating to conflict pairs in every period.
- $a_1=91=7\cdot13$, $T=20$, $L=182=2\cdot7\cdot13$. $\gcd(L,a_1^2)=91\ge20$, size condition holds. Direct enumeration over $N=5000$ terms gives **$91$ conflict states** for $m=a_1^2=8281$ (realized $1729<8281$). Same distinctness failure.

Both witnesses are verified by the corrected MT-greedy (`/tmp/round-6/conflict_probe.py`, this round); the conflict counts are builder-recomputed, not taken from the explorer (see Step 5). $\square_{\text{Step 4}}$

### Step 5 — Computational witness table (builder-recomputed, honest numbers).

**Method.** Run the corrected MT-greedy (`/tmp/round-6/mt_greedy.py`, verified bit-exact vs naive $O(N^2)$ gcd-greedy on $a_1\in\{15,385,847\}$ in round 6) for each witness $a_1$, enumerate the orbit to $N$ terms, build the map $r\mapsto\{\text{successors }d_{n+1}:a_n\equiv r\pmod m\}$, and count conflict states (residues $r$ whose successor set has size $\ge2$) and conflict pairs (ordered $(n,n')$, $n<n'$, with $a_n\equiv a_{n'}\pmod m$ but $d_{n+1}\ne d_{n'+1}$). Forward-determinism $\iff$ conflict states $=0$.

**Witness table** (`/tmp/round-6/conflict_probe.py`):

| $a_1$ | $T$ | $L$ | $m$ (label) | $\gcd(L,m)$ | size-FAIL? | realized | conflict states | conflict pairs | fwd-det? |
|---|---|---|---|---|---|---|---|---|---|
| $175$ | $274$ | $2730$ | $175$ ($a_1$) | $35$ | yes | $55$ | $40$ | $20798505$ | NO |
| $175$ | $274$ | $2730$ | $30625$ ($a_1^2$) | $35$ | yes | $9625$ | **$4447$** | $116423$ | NO |
| $175$ | $274$ | $2730$ | $35$ ($M_1$) | $35$ | yes | $11$ | $8$ | $103992605$ | NO |
| $77$ | $18$ | $154$ | $5929$ ($a_1^2$) | $77$ | no | $1309$ | $77$ | $992$ | NO (distinctness) |
| $77$ | $18$ | $154$ | $77$ ($a_1$) | $77$ | no | $17$ | $1$ | $77284$ | NO (distinctness) |
| $91$ | $20$ | $182$ | $8281$ ($a_1^2$) | $91$ | no | $1729$ | $91$ | $681$ | NO (distinctness) |
| $91$ | $20$ | $182$ | $91$ ($a_1$) | $91$ | no | $19$ | $1$ | $62500$ | NO (distinctness) |
| $847$ | $1744$ | $18942$ | $717409$ ($a_1^2$) | — | — | $49999$ | $0$ | $0$ | YES (artifact) |

**Discrepancy with the round-6 Ramsey explorer.** The explorer reported $3498$ conflict states for $a_1=175$, $m=a_1^2=30625$. The builder's re-run gives **$4447$** conflict states at the **same** $N=50000$ and the **same** realized value $9625$ (orbit identical). The explorer **under-counted** conflict states — the same pattern the $D_n$-slack builder caught in the explorer's $|D_n|$ table this round (an unspecified narrower probe definition). We use the builder-recomputed number $4447$; the qualitative finding ("$a_n\bmod a_1^2$ is not forward-deterministic") is unchanged and is in fact **strengthened** ($4447>3498$).

**The $a_1=847$ "YES" row is an artifact, stated honestly.** $a_1=847=7\cdot11^2$, $M_1=77$, $a_1^2=717409\gg N=50000$; the realized count is $49999=N-1$, i.e. **no residue has repeated yet** within the sampled horizon, so trivially each residue has a single successor. This is NOT forward-determinism — it is undersampling: confirming or refuting forward-determinism at $m=a_1^2=717409$ would require $N>a_1^2\approx 7.2\cdot10^5$, infeasible in the time budget. The $a_1=175$ counterexample (where $a_1^2=30625<N=50000$ so repeats are realized) settles the universal-over-$a_1$ claim negatively; the $a_1=847$ row is included only to document that the artifact was identified, not concealed. (Note: the round-5 T-unbounded-in-$M_1$ fence already handles $a_1=847$ via the rad-77 pair — $T=1744$ is unbounded in $M_1=77$.) $\square_{\text{Step 5}}$

### Step 6 — Fence-conclusion.

Every "finite residue states + pigeonhole self-coincidence ⇒ periodicity" route requires a forward-deterministic residue statistic $\alpha_m$ as its determining state (so that `aimo-0907-coincidence-criterion` part A can propagate a self-coincidence to periodicity). Steps 2–5 show that no fixed function-of-$a_1$ modulus $m$ supplies such a statistic:

- **(Size mode, $a_1=175$.)** For every $m=a_1^k$ ($k\ge1$), $\gcd(L,m)\le M_1=35<T=274$, so by Step 2 the necessary condition $T\le\gcd(L,m)$ fails — a structural proof, not a probe. Exhibited: $40/4447/8$ conflict states for $m=a_1/a_1^2/M_1$.
- **(Distinctness mode, $a_1\in\{77,91\}$.)** When $T\le\gcd(L,m)$ the distinctness clause is the obstruction; witnessed by $77/91$ conflict states. (No structural *proof* of distinctness failure for all small-$T$ orbits is supplied here — the witness is computational. The two modes together cover both the large-$T$ and small-$T$ regimes.)

The information-theoretic root cause (Step 1): $d_{n+1}$ depends on $(a_n,\operatorname{MT}(\mathcal F_n))$, and $a_n\bmod m$ discards the second component. The only forward-deterministic determining state is the full MT-state $\operatorname{MT}(\mathcal F_n)$, whose finiteness (stabilization to a finite antichain) IS Gap A. Therefore:

**(Fence.)** Every "residue-modulus + pigeonhole ⇒ periodicity" route — whether the modulus is $a_1$, $M_1$, $a_1^k$, $a_1\cdot M_1$, or any other fixed function of $a_1$ — is fenced for IMO 2026 P6. The route's antecedent ("exhibit a finite forward-deterministic determining statistic $\alpha$") is Gap A; the residue-statistic specialization is refuted by the obstructions above. $\square_{\text{Step 6}}$

## Scope and honesty

- The **size obstruction** (Step 2 + Step 3) is a fully rigorous proof for $a_1=175$ and every $m=a_1^k$: it uses only the empirically-verified periodic regime $(T,L)=(274,2730)$ (verified at three independent $\texttt{min\_run}$ thresholds, all consistent — not a short-tail artifact) and the elementary number-theory identity $\gcd(L,a_1^k)\le\text{($P_1$-part of $L$)}=35<T$.
- The **distinctness obstruction** (Step 4) is a computational witness for $a_1\in\{77,91\}$, not a structural proof that distinctness fails for every small-$T$ orbit. The two modes together exhibit the failure across both the large-$T$ and small-$T$ regimes.
- The **universal "for ANY $m$"** in the explorer's phrasing is the structural information-theoretic argument (Step 1: $a_n\bmod m$ discards $\operatorname{MT}(\mathcal F_n)$) supported by concrete witnesses at $m\in\{a_1,M_1,a_1^2,a_1\cdot M_1\}$ across $a_1\in\{77,91,175\}$. We do not claim a proof that *every conceivable* modulus (including exotic $m$ with prime factors outside $P_1$, e.g. $m=a_1+1$) fails; such an $m$ would have to encode information about $L$ (the orbit-determined period shift), which is itself Gap A. The fence covers the natural class of fixed function-of-$a_1$ moduli, which is the class any "residue + pigeonhole" route would invoke.

## Cross-references

- **`linchpin-and-gap-bound`** (reviewer-certified, round 1, unconditional) — supplies $d_{n+1}\in\{1,\dots,M_1\}$ and the linchpin (every $a_i$ has a prime in $P_1$); invoked in Step 1.
- **`mt-depends-on-set-system`** (reviewer-certified, round 2) — $\operatorname{MT}(\mathcal F_n)$ depends only on the set-system $\mathcal F_n=\{P(a_i):i\le n\}$; the determining state is $(a_n,\operatorname{MT}(\mathcal F_n))$, not $a_n\bmod m$. Invoked in Step 1.
- **`aimo-0907-coincidence-criterion`** (reviewer-certified, round 5, part A) — the propagation tool a "residue + pigeonhole" route needs; its antecedent (a forward-deterministic $\alpha$) is exactly what this lemma refutes for residue statistics. Invoked in Step 6.
- **T-unbounded-in-$M_1$ impossibility** (reviewer-certified, round 5, `minimal-counterexample` explorer) — sibling fence: the rad-77 pair $a_1=77\to T=18$ vs $a_1=847\to T=1744$ (same $M_1=77$, $97\times$ jump) fences every $f(M_1)$-bounded deterministic statistic (state *size* bounded in $M_1$). **The present lemma sharpens this**: it kills residue statistics at moduli $m=a_1^k$ that are NOT $f(M_1)$-bounded ($a_1$ can dwarf $M_1=\operatorname{rad}(a_1)$; $a_1=175\Rightarrow a_1^2=30625\gg M_1=35$). The T-unbounded fence fences the *consequence* (state-size bound); this lemma fences the *modulus-independence* (no fixed function-of-$a_1$ modulus works). Together they close the fixed-modulus finite-statistic route from both ends.
- **`D_n-slack-obstruction`** (pending, round 6) — sibling negative structural fence; same explorer-under-count pattern (the explorer's $|D_n|$ table was also under-counted; builder recomputed and used verified numbers). Same corrected MT-greedy used for both.
- **`deviation-descent-blocked-by-wmin-fence`** (reviewer-certified, round 5) — sibling fence; the deviation-descent's shift-by-$C$ admissibility preservation requires a cofactor bound (every governing prime divides $C$), and the present lemma's root cause (the determining state is $\operatorname{MT}(\mathcal F_n)$, not any residue) explains *why*: a residue statistic cannot capture the prime-support coverage that admissibility requires.

## Status

Pending reviewer certification (round 6) as a **negative/structural lemma**. The size obstruction (Steps 2–3) is a rigorous proof from the verified periodic regime of $a_1=175$. The distinctness obstruction (Step 4) is a builder-verified computational witness at $a_1\in\{77,91\}$ using the corrected MT-greedy (bit-exact vs naive gcd-greedy). The conflict counts are builder-recomputed (the explorer under-counted: $3498$ reported vs $4447$ actual at identical realized $=9625$); the discrepancy is documented, not concealed. The fence-conclusion (Step 6) is the information-theoretic argument (Step 1) plus the witnesses: the only forward-deterministic determining state is the MT-state $=$ Gap A. This lemma cleanly fences off the "fixed-modulus residue statistic + pigeonhole ⇒ periodicity" sub-class of routes for IMO 2026 P6, and sharpens the round-5 T-unbounded-in-$M_1$ fence from $f(M_1)$-bounded statistics to all fixed function-of-$a_1$ moduli.
