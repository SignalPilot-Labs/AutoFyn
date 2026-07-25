## Third-Term Dichotomy Lemma

**Setup.** Let $a_1=pq$ with $p<q$ primes ($\omega(a_1)=2$, squarefree).
Since $R(a_1)=\{p,q\}$, for any $m>0$: $\gcd(m,a_1)>1\iff p\mid m$ or
$q\mid m$.

**Lemma ($a_2$ formula).** $a_2=a_1+p$. (Proof: no integer strictly
between $a_1$ and $a_1+p$ is divisible by $p$ or by $q$, since $p<q$; the
first candidate divisible by $p$ is $a_1+p$.)

Write $k:=q+1$, so $a_2=pk$. Let $e:=v_p(k)$ and $k':=k/p^e$ (so
$p\nmid k'$).

**Statement (Third-Term Dichotomy).** Define
$$m^\ast:=\begin{cases}\text{least multiple of }q\text{ exceeding }a_2
\text{ with }\gcd(m^\ast,k')>1,&k'>1\\+\infty,&k'=1.\end{cases}$$
Then $a_3=\min(a_2+p,\ m^\ast)$.

**Proof.** Classify every integer $m>a_2$ by whether $p\mid m$.
*Type P* ($p\mid m$): since $p\mid a_1$ and $p\mid a_2$, $(\ast)$ gives
$\gcd(m,a_1)\ge p>1$ and $\gcd(m,a_2)\ge p>1$ automatically; the least
such $m$ is $a_2+p$.
*Type non-P* ($p\nmid m$): validity against $a_1$ forces $q\mid m$ (the
only other disjunct of $(\ast)$). Writing $a_2=p^{e+1}k'$ ($p\nmid k'$),
since $p\nmid m$, $\gcd(m,p^{e+1})=1$, so $\gcd(m,a_2)=\gcd(m,k')$: given
$q\mid m,\ p\nmid m$, validity against $a_2$ is exactly $\gcd(m,k')>1$.
The least such $m$ is $m^\ast$ by definition. Since every $m>a_2$ falls
into exactly one type, and $a_3$ is the least valid candidate, $a_3=
\min(a_2+p,m^\ast)$. $\blacksquare$

**Instances (both hand-verified and independently re-simulated).**
- $a_1=35=5\cdot7$: $a_3=42$ (Type non-P wins; the lock on $p=5$ breaks at
  the very next step).
- $a_1=65=5\cdot13$: $a_3=75$ (Type P wins, the lock on $p=5$ survives the
  third-term race) — but the *next* term is $a_4=78\ne a_3+5=80$: the
  lock breaks one step later, showing "wins the race against $a_2$ alone"
  does not certify permanent locking. See `bounded-lookahead-insufficiency.md`.

### Provenance
Proved in `approaches/renormalization-induction-on-seed.md` (round 4/5,
§4.1–4.2). Cross-checked by the builder against direct simulation for all
$66$ squarefree pairs $p<q\le37$: zero mismatches. Independently
re-verified by the proof-reviewer (round 4) via a fresh brute-force
comparison of the closed form against exact simulation for the same $66$
pairs: zero mismatches confirmed.

### Status
Unconditional, fully general for all squarefree two-prime seeds $a_1=pq$.
Does not extend (as proved) beyond the third term or beyond $\omega(a_1)
=2$; see `bounded-lookahead-insufficiency.md` for a proof that no fixed
bounded lookahead suffices to certify permanent locking even within this
restricted family.
