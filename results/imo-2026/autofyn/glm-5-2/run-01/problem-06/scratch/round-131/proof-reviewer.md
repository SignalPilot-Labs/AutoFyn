# Proof-reviewer — Round 131

**Target:** `results/imo-2026-06/self-contained-solution.md` — re-packaging of the SOLVED IMO 2026 P6 proof with every lemma inlined.

## Verdict: APPROVE
## Status: solved (unchanged — this was re-packaging, not a new attempt)

---

## 1. Self-containment (the user's actual request) — PASS

`grep` for surviving imports:
- `lemmas/`, `approaches/` appear ONLY in the §0 purpose-statement (lines 3, 280), which *declares* self-containment and explicitly notes that `knowledge_base.md` is a reference catalogue, not a proof-step import. No proof step says "import", "see lemma", "as proved in", "cite lemma", or "do not re-prove".
- The sole external citation is `knowledge_base.md` for the **Chinese Remainder Theorem** in §6.2 — explicitly permitted by the review brief and the rigor rules ("Name your tools ... cite the relevant entry in `knowledge_base.md`").

Every lemma (A, B, the descent + 4 sub-lemmas, the Corollary, and the six Finish lemmas §6.1–§6.5) is proved inline. **Zero surviving proof-step imports.** Self-containment requirement met.

## 2. Correctness of the inlined Finish (§6) — VERIFIED

I cross-checked each inlined lemma against its certified original in `lemmas/*.md` and re-derived the load-bearing steps independently.

**§6.1 Pairwise intersection (unconditional).** Sound. From the greedy rule at index $j$: $\gcd(a_j,a_i)>1$ for $i<j$. Each $M'\in\mathcal M$ equals some $P(a_j)$ (minimals are members of $\mathcal F$), so $P(a_n)\cap M'\neq\emptyset$. Matches `pairwise-intersection.md`.

**§6.2 Transversal residue characterization.** Sound. The chain
$$\gcd(m,a_i)>1\,\forall i \iff P(m)\cap P(a_i)\neq\emptyset\,\forall i \iff P(m)\text{ transversal of }\mathcal F \iff P(m)\text{ transversal of }\mathcal M$$
is correct (hitting all members = hitting all minimal members, since every non-minimal member contains a minimal one). Free-rider invisibility: $q\mid m, q\notin P$ lies in no $M'\subseteq P$, so irrelevant. CRT over squarefree $L$ makes $\{p\in P:p\mid m\}$ depend only on $m\bmod L$. Matches `transversal-residue-characterization.md`. CRT cited by name to `knowledge_base.md` — rigor rule satisfied.

**§6.3 Universal membership / no transient.** Sound. Trichotomy on $j$ vs $n$ (where $M'=P(a_j)$): $j<n$ uses admissibility of $a_n$; $j>n$ uses admissibility of $a_j$ against the past including $a_n$; $j=n$ trivial ($a_n>1$). All three cases settled, disjoint, exhaustive. Matches `universal-membership-no-transient.md`.

**§6.4 Greedy = cyclic successor — BOTH containments justified (the previously-imported part).** I scrutinized this hardest.
- *$V\subseteq V_n$ (upper bound on $a_{n+1}$):* Take $M'\in\mathcal M_n$. In $\mathcal F$: either $M'$ stays minimal ($M'\in\mathcal M$, hit directly) or some $M\in\mathcal M$ has $M\subseteq M'$ (since $M'$ not minimal in $\mathcal F$ ⟹ chains down to a minimal $M\subsetneq M'$); hitting $M$ ⟹ hitting $M'\supseteq M$. So every $V$-element (hits $\mathcal M$) hits $\mathcal M_n$, i.e. $V\subseteq V_n$, giving $a_{n+1}=\min(V_n\cap(a_n,\infty))\le\min(V\cap(a_n,\infty))$. **Both sub-cases (equal / strict) covered.** Correct.
- *Lower bound:* By §6.3 (which holds for all $n\ge1$, so applies at $n+1$), $a_{n+1}\bmod L\in V$ and $a_{n+1}>a_n$, so $a_{n+1}$ is itself in $\{m>a_n:m\bmod L\in V\}$, giving $a_{n+1}\ge\min$ of that set. Correct — not a hand-wave; genuinely invokes §6.3.
- Equality combines both. The cyclic-successor identification $r_{n+1}=\varphi(r_n)$ is the standard residue-class argument (next $V$-element $>r_n$ in current block, else wrap to $\min V=v_0=0$ in next block). Correct.
- *Corollary $a_{n+1}-a_n\le L$:* the next multiple of $L$ above $a_n$ has residue $0\in V$ (every prime divides $0$ ⟹ $\{p\in P:p\mid 0\}=P$ is a transversal), so it is $V$-admissible; the smallest admissible is at most it, within $L$. Correct.

Minor phrasing: §6.4 attributes $a_{n+1}=\min\{m\in V_n:m>a_n\}$ to "Lemma A applied at time $n$". This is a slight over-credit (the actual reduction is the elementary "hits all members ⟺ hits all minimal members", not Lemma A's $\prec$-minimal-chain reduction), but the doc immediately gives the correct elementary justification inline ("a candidate $m>a_n$ is admissible iff $P(m)$ hits every $P(a_i),i\le n$, iff $P(m)$ hits the $\subseteq$-minimal members $\mathcal M_n$"). Not a defect.

Matches `greedy-equals-cyclic-successor.md`.

**§6.5 Single cycle, period-sum $L$.** Sound. $v_0=0\in V$ (justified in §6 preamble). $\varphi(v_i)=v_{i+1}$ ($i<k-1$), $\varphi(v_{k-1})=v_0$ (wrap to $\min V=0$). Single $k$-cycle. Telescope: $(v_1-v_0)+\cdots+(v_{k-1}-v_{k-2})+(L-v_{k-1}+v_0)=v_{k-1}+(L-v_{k-1})=L$ using $v_0=0$. Matches `cyclic-successor-single-cycle.md`.

**§6.6 Conclusion.** §6.3 ⟹ $a_n\bmod L\in V$ from $n=1$ (no transient); §6.4 ⟹ $r_{n+1}=\varphi(r_n)$; §6.5 ⟹ after $T=|V|$ steps residue returns and total increment is $L$. So $a_{n+T}=a_n+L$ for every $n\ge1$. Constructive pair $(T,L)=(|V|,\prod_{p\in\bigcup\mathcal M}p)$ exhibited. Correct.

## 3. Correctness of the descent (§3–§5) — INTACT

Already reviewer-certified round 130. I confirmed the inlining dropped no step:
- **Lemma A (§3):** (i)$\iff$(ii) via no-skip greedy (the $a_n<x<a_{n+1}$ contradiction); (ii)$\iff$(iii) via the $\prec$-minimal chain (indices strictly decrease ⟹ terminates). Unconditional flag correct. No circularity (§6 lemmas not invoked).
- **Lemma B / Direction B (§4):** first-appearance index $i$ for support $M$; if $a_m\prec a_i$ with $m<i$ then $P(a_m)\subseteq M$ forces $P(a_m)=M$ (by $\subseteq$-minimality of $M$ in $\mathcal F$), contradicting first-appearance. Direction A flagged false and unused. Correct.
- **Descent (§5):** all four sub-lemmas present and correct:
  - *Landing ($q^k c\in[a_1,a_n)$):* load-bearing inequality $a_n/a_1\ge p/a_1>a_1\ge q$ (i.e. $p>a_1^2$, tight). $k=0$ corner: $c\ge a_1$ and $c<a_n=pc$ ($p>1$). $k\ge1$: $q^{k-1}c<a_1\Rightarrow q^k c<q a_1\le a_1^2<a_n$. Both cases land in $[a_1,a_n)$.
  - *Shared-prime transfer:* IH$_n$ ⟹ $p\nmid a_i$ for $\prec$-minimal $a_i<i<n$; admissibility gives $\gcd(a_n,a_i)>1$; pick $r\mid\gcd$, $r\neq p$ ⟹ $r\mid c\mid q^k c$.
  - *Index-descent:* $q^k c<a_n\Rightarrow\mathrm{idx}<n$ by strict increase.
  - *Rad-divisibility:* $q\mid c\Rightarrow P(q^k c)=P(c)\subseteq P(c)\cup\{p\}=P(a_n)$.
  - *IH closure:* contrapositive gives $\prec$-minimal $a_n$ ⟹ $a_1^2$-smooth ⟹ (IH$_{n+1}$). Base $n=1$ vacuous + $a_1$ carries no large prime ($p\le a_1<a_1^2$).
- **Corollary:** descent ⟹ every $\prec$-minimal term $a_1^2$-smooth; Direction B ⟹ every $M\in\mathcal M$ is such a support ⟹ $M\subseteq P_0$ ⟹ $\mathcal M\subseteq 2^{P_0}$ finite. Wall closed.

## 4. Rigor rules — PASS

- No skipped cases: induction base+step, chain-termination (Lemma A (ii)⟹(iii)), $k=0$ corner, trichotomy $j$ vs $n$ — all explicit.
- No hand-waving: the two containments in §6.4 are each justified (not "similarly"); the telescope in §6.5 is spelled out; the $V\subseteq V_n$ sub-case split (equal/strict) is given.
- Tools named: CRT cited to `knowledge_base.md` ("Number Theory — Modular arithmetic, CRT"). No other external theorem invoked.
- Prove-don't-conjecture: Direction A falsified (not asserted); no unproven claims presented as established.
- Numerical sanity checks (§7) correctly labelled "confirmations, not proof steps"; I independently reproduced $a_1=15$: $\mathcal M=\{\{2,3\},\{2,5\},\{3,5\}\}$, $L=30$, $V=\{0,6,10,12,15,18,20,24\}$, $T=8$, $a_{n+8}=a_n+30$ for $n\ge1$. Matches §7.

## 5. Overclaim check — Status `solved` is correct

The document's claim of self-containment is honest: every lemma is genuinely proved inline, the only external reference is `knowledge_base.md` for CRT (permitted), and the proof is complete and rigorous. Status `solved` matches reality.

## Scores
- Correctness: 10/10
- Completeness/rigor: 10/10 (all cases, both containments, no hand-waving, CRT cited)
- Progress: N/A (re-packaging; full solution already SOLVED round 130)

## Outcome recorded
`record_outcome` on `large-prime-descent`, round 131, outcome `verified-milestone` (self-contained re-packaging APPROVED; Status solved).
