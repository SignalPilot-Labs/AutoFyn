## Lemma (Same-Class-Free / Class-Partition Reduction)

Let $P:=R(a_1)$. By `lemmas/prime-factors-a1-cover-forever.md`,
$R(a_n)\cap P\ne\emptyset$ for every $n\ge1$; define the **owning prime**
$\pi(n):=\min(R(a_n)\cap P)$ and classes $C_p:=\pi^{-1}(p)$ for $p\in P$
(partitioning $\mathbb Z_{\ge1}$).

**Same-Class-Free Lemma.** For any finite $Q\supseteq P$ and any $i\ne j$
with $\pi(i)=\pi(j)$, the pair is automatically hit:
$W(i,j):=R(a_i)\cap R(a_j)$ satisfies $W(i,j)\cap Q\ne\emptyset$.

*Proof.* Let $p:=\pi(i)=\pi(j)\in P$; then $p\mid a_i,a_j$, so $p\in
W(i,j)$, and $p\in P\subseteq Q$. $\blacksquare$

**Corollary.** If $p\in\mathrm{Nec}\setminus P$ (witnessed by pair $i,j$
with $R(a_i)\cap R(a_j)=\{p\}$), then $\pi(i)\ne\pi(j)$.

*Proof.* If $\pi(i)=\pi(j)=q\in P$, the Same-Class-Free argument (with
$Q=P$) gives $q\in R(a_i)\cap R(a_j)=\{p\}$, so $q=p\in P$, contradicting
$p\notin P$. $\blacksquare$

### Consequence (Class-Partition Reduction)
The only pairs $(i,j)$ that can (a) fail to be $Q_{\min}$-hit, or (b) force
a new element into $\mathrm{Nec}\setminus P$, are **cross-class** pairs
($\pi(i)\ne\pi(j)$). Same-class pairs are unconditionally safe for any
finite $Q\supseteq P$, with no density/recurrence argument needed.

### Caveat (insufficient by itself)
Defining $\mathcal P:=\{(i,j):R(a_i)\cap R(a_j)\cap P=\emptyset\}$ (a subset
of cross-class pairs), the remaining difficulty is confined to $\mathcal P$
— but $\mathcal P$ is **not** shown finite; a computational check
(evidence only) found $\mathcal P$ non-shrinking as a fraction of all pairs
for $a_1\in\{15,35,375\}$ over 400 terms (20000, 13488, 6024 out of 79800
total pairs respectively). This reduction narrows but does not close the
central gap.

### Provenance
Proved in `approaches/state-compactness-pigeonhole.md`, §12.2–12.3, round 5.
Independently re-derived by the proof-reviewer; no gap found in the
positive lemma. The insufficiency claim is reported as numerical evidence,
correctly labeled as such (not claimed as a proof).
