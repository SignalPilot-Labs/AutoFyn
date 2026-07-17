## imo-2026-01

Two rival complete attempts at the WHOLE problem (parts a + b). Both share the forced part-(b) invariant g_p = gcd of p-valuations (no false diversity manufactured there); they diverge on the genuine choice — the termination argument for part (a).

---

global-lex-monovariant: new
Target: (a) regardless of choices the process terminates with exactly one entry M>1; (b) M is choice-independent. The whole problem.
Technique: GLOBAL lexicographic monovariant Φ=(N,P) = (#entries>1, product of all entries) for termination; per-prime exponent-gcd invariant g_p for the value.
Skeleton:
  1. Product P: one move gives P_new = P_old/gcd(m,n) (since gcd·lcm=mn), non-increasing, strictly down iff gcd>1 — by gcd·lcm=mn.
  2. Count N=#{>1}: coprime move {m,n}→{1,mn} drops N by 1; non-coprime move never raises N — by case split.
  3. Φ=(N,P) strictly lex-decreases every move (N primary): coprime ⇒ N drops; non-coprime ⇒ N non-increasing and P strictly drops — by 1–2.
  4. ℕ×ℕ_{≥1} lex is well-founded ⇒ finitely many moves — well-ordering.
  5. Terminal state has N∈{0,1} — move-availability.
  6. N=0 excluded: some initial g_p>0 is invariant, so a final valuation is >0 ⇒ not all ones ⇒ N=1 — invariant positivity.
  7. g_p = gcd(v_p over board), invariant since (a,b)→(min,|a−b|) preserves pairwise gcd — Euclidean step + gcd associativity.
  8. Terminal read-off: v_p(M)=gcd(v_p(M),0,…,0)=g_p ⇒ M=∏_p p^{g_p}, choice-independent — invariance + terminal structure.
Key lemmas (claim + mechanism):
  - P_new=P_old/gcd(m,n) — because lcm/(mn)=1/gcd(m,n); so P non-increasing, UNCHANGED on coprime moves (not increased), strictly down iff gcd>1.
  - gcd(min(a,b),|a−b|)=gcd(a,b) for all a,b≥0 — one subtractive Euclidean step; boundary a=0,b=0,a=b included.
  - g_p is a whole-multiset invariant — because gcd is associative and only the chosen pair changes, with its gcd preserved.
  - M>1 — because the board starts all >1, so some prime p has gcd of initial exponents e>0, forcing v_p(M)=g_p>0.
Open gaps: A1 (exact per-move behavior of P and airtight lex descent — confirm no move fixes both N and P; the coprime case keeps P constant, N drops); A2 (well-foundedness / finite move bound); B1 (gcd identity all boundary cases); B2 (gcd associativity over zero-containing multiset); B3 (N=0 exclusion via some g_p>0).
Cases to cover: gcd(m,n)=1 vs >1; a=0,b=0,a=b in gcd identity; terminal N=0 vs 1.
Watch out for: total SUM Σx_i is NOT monotone (coprime pair can raise it) — use (N,P). Primes are NOT independent processes — only the per-move update rule is prime-local. State gcd(0,0)=0, gcd(0,e)=e. Prove M>1, don't assume it.

---

per-prime-valuation-descent: new
Target: same whole problem (a)+(b).
Technique: termination argued INSIDE the per-prime decomposition — a valuation potential Φ=(Ω,N) with Ω=Σ_i Ω(x_i)=Σ_p S_p, plus a genuinely different fallback engine: a minimal-Ω extremal / minimal-counterexample descent (borrowed framing from corpus aimo-0836's minimal-sum counterexample on a replace-a-pair board process). Part (b) identical g_p invariant.
Skeleton:
  1. S_p=Σ_i v_p(x_i): a move sends pair a+b → max(a,b) ≤ a+b, strict iff min(a,b)>0; so Ω=Σ_p S_p non-increasing, strict iff gcd(m,n)>1 — by max<sum ⇔ min>0.
  2. Coprime move keeps Ω fixed but drops N by 1 ({m,n}→{1,mn}) — coprime structure.
  3. Φ=(Ω,N) lex (Ω primary, N secondary) strictly decreases every move — by 1–2.
  4. ℕ×ℕ lex well-founded ⇒ termination.
  5. Terminal N∈{0,1}; N≠0 via invariant g_p>0 ⇒ exactly one survivor M.
  5'. ALTERNATIVE engine: minimal-Ω counterexample — a board admitting infinite play with least Ω; any non-coprime move lowers Ω (smaller counterexample), coprime moves are bounded by N, forcing a halt — contradiction. (aimo-0836 analogy.)
  6–8. g_p=gcd(v_p over board) invariant (Euclidean step + associativity) ⇒ v_p(M)=g_p ⇒ M=∏_p p^{g_p}; some g_p>0 ⇒ M>1.
Key lemmas (claim + mechanism):
  - Ω non-increasing, S_p drops iff both chosen entries divisible by p — because min(a,b)+|a−b|=max(a,b).
  - Ω alone canNOT force termination — coprime moves leave Ω fixed; the N secondary component (or extremal descent) is essential.
  - gcd(min(a,b),|a−b|)=gcd(a,b) — subtractive Euclid step (shared with sibling).
  - Minimal-Ω board admitting infinite play is contradictory — non-coprime move strictly lowers Ω, coprime moves bounded by N.
Open gaps: T1 (fix lex orientation of (Ω,N); prove strict descent both move types; no move fixes both; S_p monotonicity + strict criterion); T2 (if extremal route built: existence of minimum, smaller-board step, coprime-run bound); B1/B2/B3 as in sibling.
Cases to cover: coprime vs non-coprime move; a=0,b=0,a=b in gcd identity; terminal N=0 vs 1.
Watch out for: only finitely many primes appear (E_p≡0 for others) — note finiteness before summing over primes. Ω unchanged on coprime moves — do not claim Ω alone terminates. Position choice shared across primes. gcd(0,0)=0.

---

Diversity note for the reviewer: the two approaches share the (forced, essentially one-line-given-(a)) part-(b) invariant but attack part (a) — the real difficulty — from different framings: a GLOBAL scalar product monovariant vs. a per-prime valuation-mass potential with an extremal-descent fallback. If both stall it would be on the SAME wall (the lex well-foundedness / N=0 exclusion), so I have deliberately given approach 2 a second, structurally different termination engine (minimal-counterexample) so the field does not collapse to one framing. Recommend advancing both; if the lex descent proves fragile, the extremal route in per-prime-valuation-descent is the hedge.

build set: global-lex-monovariant, per-prime-valuation-descent
