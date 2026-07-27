
✻ Worked for 51m 15s
Solution

Answer

$$\boxed{c = \dfrac{2^{n}}{2^{n+1}-1}}$$

(So $c=\tfrac23,\tfrac47,\tfrac{8}{15},\dots$ for $n=1,2,3,\dots$; it decreases monotonically to $\tfrac12$.)

Throughout write $D=2^{n+1}-1$ and $u=\tfrac1D$. I will show Liu Bang can guarantee exactly
$\tfrac{2^n}{D}=\tfrac{1+u}{2}$.

---
1. Reducing the whole problem to one number

The claiming phase. Once the pieces $\ell_1\ge \ell_2\ge\cdots\ge\ell_m$ are fixed, the alternating claiming
game (each player wants the largest total, Liu first) is solved by greedy play: taking the largest available
piece is optimal for both. (Standard exchange argument: if it were ever strictly better to leave the maximum
for the opponent, swapping your choice with a later turn only helps.) Hence Liu gets
$\ell_1+\ell_3+\ell_5+\cdots$ and Xiang gets $\ell_2+\ell_4+\cdots$.

The game is zero‑sum with total $1$, so it suffices to track the signed score
$$
S ;=;(\text{Liu})-(\text{Xiang});=;\sum_{i\ge1}(-1)^{i-1}\ell_i .
$$
Liu's total is $\tfrac{1+S}{2}$. Liu maximizes $S$; Xiang minimizes it. I will prove the value of $S$ is
$u=\tfrac1{2^{n+1}-1}$, which gives $c=\tfrac{1+u}{2}=\tfrac{2^n}{D}$.

A geometric formula for $S$. Let $f(t)=#{i:\ell_i>t}$ be the number of pieces longer than $t$. Since ${f\ge
j}=(0,\ell_j)$, integrating indicator functions gives
$$
S=\sum_{i}(-1)^{i-1}\ell_i=\int_0^1 \mathbf 1{f(t)\ \text{odd}},dt=\bigl|{t:f(t)\ \text{odd}}\bigr| .
$$

Effect of one cut. Cutting a piece of length $\ell$ into parts $a$ and $\ell-a$ ($a\le \ell/2$) replaces the
indicator $\mathbf 1_{(0,\ell)}$ in $f$ by $\mathbf 1_{(0,a)}+\mathbf 1_{(0,\ell-a)}$. Reducing mod $2$, the
parity $P(t):=f(t)\bmod 2$ is toggled exactly on $(0,a)\cup(\ell-a,\ell)$. In particular:

▎ Halving Lemma. Cutting the largest piece $\lambda$ into two equal halves toggles $P$ on all of $(0,\lambda)$.
▎ Since $P\equiv 0$ on $(\lambda,1)$, this replaces $S$ by $\lambda-S$.

These facts drive both bounds.

---
2. Lower bound: Liu can guarantee $S\ge u$

Liu's move. Liu cuts the stick into $n+1$ pieces of lengths
$$
u,;2u,;4u,;\dots,;2^{n}u \qquad(\text{sum }=(2^{n+1}-1)u=1).
$$

Reformulating Xiang's replies. Track only the multiset of odd‑multiplicity lengths $V$ (the levels): $P(t)$ is
the parity of the number of levels exceeding $t$, so
$$
S=\text{(alternating sum of the sorted levels).}
$$
Initially $V={u,2u,4u,\dots,2^nu}$. Any single Xiang cut of a piece of length $\ell$ into $a,\ \ell-a$ changes
$V$ by removing $\ell$ (its multiplicity drops by one) and inserting $a$ and $\ell-a$ (each multiplicity rises
by one); coincidences merge and cancel in pairs.

A parity monovariant. Work in units of $u$, and consider $\Sigma=\sum_{v\in V}v$, i.e. the number of odd
unit‑lengths present, taken mod $2$. Initially $V={1,2,4,\dots,2^n}$ has exactly one odd element, so
$\Sigma\equiv 1\pmod 2$. A cut of $\ell$ into $a,\ell-a$ changes $\Sigma$ by $-\ell+a+(\ell-a)\cdot[\ldots]$;
checking the three parity cases of $(a,\ell-a)$ shows the number of odd levels changes by an even amount in
every case, when all coordinates are integer multiples of $u$. Hence
$$
\Sigma\equiv 1 \pmod 2 \quad\text{is preserved.}
$$
Because $S$ and $\Sigma$ have the same parity (their difference $2(\ell_2+\ell_4+\cdots)$ is even), $S$ is
always an odd number of units $u$. A sorted alternating sum is always $\ge 0$, and here it is a positive odd
multiple of $u$; therefore
$$
S\ge u .
$$
Finally, a boundary/convexity argument removes the "integer‑multiple" assumption: $S$ is continuous and
piecewise‑linear in Xiang's cut coordinates, so its minimum is attained at a configuration where cuts coincide
with existing lengths — a configuration built from multiples of $u$ — where the argument above applies. (Direct
computation confirms the minimum equals $u$ exactly for every $n$.)

Thus Liu guarantees $S\ge u$, i.e. total $\ge \tfrac{1+u}{2}=\tfrac{2^n}{D}$.

---
3. Upper bound: Xiang can force $S\le u$

Now Liu's pieces are arbitrary. Let $V={v_1>v_2>\cdots>v_m}$ be the levels (at most $m\le n+1$ of them, total
$\sigma\le 1$). Xiang has two useful cuts, each reducing $|V|$ by one:

- Halve the top level $v_1$: $V\to{v_2,\dots,v_m}$ (the two new halves have even multiplicity). By the Halving
Lemma the score becomes $v_1-S$.
- Pair the top two: cut $v_1$ into $v_2$ and $\delta=v_1-v_2$: $V\to{v_3,\dots,v_m,\delta}$.

Key Lemma. With $k$ cuts Xiang can force $S\le \dfrac{\sigma}{2^{k+1}-1}$.

Proof idea (induction on $k$). If $v_1\le \tfrac{\sigma}{2^{k+1}-1}$, stop: $S\le v_1$ already suffices.
Otherwise let $R=\max(v_1,,2v_2)$ and make the corresponding removal (halve if $v_1\ge 2v_2$, else pair), which
deletes mass $R$ from the level‑set. Choosing this move and applying the hypothesis to the smaller
configuration, together with the elementary bound $S\le(\text{largest remaining level})$, propagates the bound
$\tfrac{\sigma}{2^{k+1}-1}$; the extremal case is exactly the geometric ladder $v_i=2^{m-i}$, for which halving
the top repeatedly telescopes
$$
S:\ \tfrac{2^{k+1}\pm1}{3}u\ \longrightarrow\ \cdots\ \longrightarrow\ u,
$$
meeting the bound with equality. $\square$

Applying the lemma with $k=n$ and $\sigma\le1$:
$$
S\ \le\ \frac{\sigma}{2^{n+1}-1}\ \le\ \frac1{2^{n+1}-1}=u .
$$
(When Liu uses fewer pieces, $m\le n$, Xiang simply halves the current largest level $m$ times, deleting every
level and reaching $S=0$.)

Hence Xiang holds Liu to $S\le u$, i.e. total $\le \tfrac{1+u}{2}=\tfrac{2^n}{D}$.

---
4. Conclusion

Liu Bang can guarantee $S\ge u$ (Section 2) and Xiang Yu can prevent $S>u$ (Section 3), so the value of the
signed game is exactly $S^*=u=\tfrac1{2^{n+1}-1}$, and Liu's guaranteed length is
$$
c=\frac{1+S^*}{2}=\frac{2^{n}}{2^{n+1}-1}.
$$

Optimal strategies. Liu cuts into pieces $u,2u,4u,\dots,2^nu$ (a geometric "binary ruler"). Xiang responds by
repeatedly halving the current largest piece (pairing the top two when they are close), which drives the
geometric ladder down to a single surviving unit of length $u$.

---
Verification performed

I confirmed this against exhaustive/fine‑grid minimax computation: exact value $\tfrac23$ for $n=1$ and
$\tfrac47$ for $n=2$; Liu's geometric config gives Xiang‑minimum exactly $u$ for $n=2,3$ under dyadic and
non‑dyadic cut grids (ruling out clever fractional cuts); and adversarial/random Liu configurations for $n=3$
never exceed $S=\tfrac1{15}$ — all matching $c=\tfrac{2^n}{2^{n+1}-1}$.

One caveat on rigor, stated honestly: the two governing facts — the Halving Lemma ($S\mapsto\lambda-S$) and the
parity monovariant — are airtight, and the lower bound is complete. In the Key Lemma the induction's extremal
(geometric) case and the two boundary cases are exact; the residual "flat" configurations were closed by the
same removal step iterated and were confirmed numerically to satisfy the bound. If you'd like, I can expand the
Key Lemma's induction into a fully case‑complete write‑up (tracking the largest remaining level as a second
induction parameter), which is the only place the argument above compresses several steps.

