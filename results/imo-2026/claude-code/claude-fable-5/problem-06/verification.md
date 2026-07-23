# Problem 6 — Verification Log

**Solution file:** `problem6_solution.md`
**Solution finalized & verified:** 2026-07-22 16:43:32 PDT

## Verification record

### 1. Adversarial proof review (independent reviewer pass)

Verdict: **SOUND** — no fatal or fixable gaps found; two cosmetic notes
(duplicate definition of $U$ in Steps 4/5 under different logical contexts;
Lemma 4 cites (F4) where the pairwise-intersection clause, i.e. (F1) restricted
to $\mathfrak{B}$, is the content used).

Points explicitly audited and confirmed:
- Lemmas 1–3: no circularity; existence of the index $n$ with $a_n < m < a_{n+1}$
  justified; strictness of inequalities for non-terms.
- (F3): finite transversal $A \neq \emptyset$; representative $(\prod A)^k > a_1$
  has prime set exactly $A$; forced into the sequence by Lemma 2.
- Well-definedness of minimal members $\mathfrak{B}$ when $\mathcal{F}$ is infinite
  (each $F$ is finite, so an inclusion-minimal member inside $F$ exists).
- Lemma 4: $A = B \setminus \{p\}$ non-transversal follows from minimality of $B$;
  $\pi(B') \mid \operatorname{rad}(s) \le s < \pi(A)$ chain valid; singleton edge
  case never reaches Lemma 4.
- Lemma 5: stop condition tested before each application of Lemma 4; $p$ persists
  in every iterate; strict decrease of $\pi(B^{(i)})$ gives termination.
- Main Lemma pigeonhole: $D_p \subseteq \{\text{primes} \le a_1\}$, infinite fiber
  $\mathcal{Q}$ exists; both cases ($D = \emptyset$, $D \neq \emptyset$) yield
  genuine contradictions (disjoint members / antichain violation).
- Final counting: bijection $x \mapsto x - L$ valid in both directions via $(\ast)$;
  identity $\#(S \cap [a_1, a_n)) = n-1$ holds for all $n \ge 1$ including $n = 1$;
  $T \ge 1$, $L \ge 2$; conclusion holds for **every** $n \ge 1$, not just eventually.

### 2. Numerical verification (`problem6_verification.py` + simulation)

Direct greedy simulation (gcd checked against *all* previous terms), for
$a_1 \in \{2,3,4,5,6,9,10,14,15,21,22,25,33,35,49,77,105,143,165,195,221,231,255,899,1001,1155,46189\}$:

- **Structure theorem (Lemma 2):** terms coincide exactly with the increasing
  enumeration of $\{m \ge a_1 : P(m) \text{ hits every minimal member}\}$ — all cases.
- **Exact periodicity from $n = 1$:** with $L = \prod_{p \in \cup\mathfrak{B}} p$ and
  $T = \#(S \cap [a_1, a_1+L))$, checked $a_{n+T} = a_n + L$ for all computed $n$
  (all cases where $L$ fits in the computed range). Examples:
  $a_1{=}15$: $\mathfrak{B} = \{\{2,3\},\{2,5\},\{3,5\}\}$, $L=30$, $T=8$;
  $a_1{=}105$: $\mathfrak{B} = \{\{2,3\},\{2,5\},\{2,7\},\{3,5,7\}\}$, $L=210$, $T=58$;
  $a_1{=}1001$: $\mathfrak{B} = \{\{2,7\},\{2,11\},\{2,13\},\{7,11,13\}\}$, $L=2002$, $T=282$.
- **Lemma 3** (coprime term below every non-member $m > a_1$): 0 violations
  ($a_1 = 15, 35, 221, 1001$; all non-terms up to mid-range).
- **Lemma 4** (descent: $B' \cap B = \{p\}$, $\pi(B') < \pi(B)/p$ whenever
  $\pi(B \setminus \{p\}) > a_1$): 0 violations on all computed minimal families.
