## imo-2026-01

product-support-descent: new
Target: Prove that every legal play from the 2026 initial integers terminates with exactly one entry greater than 1, that its value is independent of all choices, and more precisely that the survivor is \(M=\prod_{p\in P}p^{g_p}\), where \(P\) is the finite set of primes occurring initially and \(g_p=\gcd\{v_p(a_i):v_p(a_i)>0\}\).
Technique: Direct proof by the Knowledge Base's **Invariant / monovariant** method: a factorization-free scalar descent \(2^rP_B\) for termination, followed by **Divisor analysis** and a prime-valuation Euclidean invariant for uniqueness. This is the cheapest structural route; product alone was rejected because it stalls on coprime pairs. It adapts the integral-descent crux of `aimo-0440` (but here every legal move decreases one fixed potential) and the prime-data compression principle of `aimo-0324`.
Skeleton:
  1. For a board \(B\), define \(P_B\) as the product of its 2026 entries, \(r_B\) as the number of entries greater than 1, and \(F(B)=2^{r_B}P_B\) — by the Invariant / monovariant method.
  2. For a move on \(m,n\), put \(d=\gcd(m,n)\); the selected pair's new product is \(\operatorname{lcm}(m,n)=mn/d\), so if \(d>1\), \(P_B\) falls by the factor \(d\) and \(r_B\) does not increase, whereas if \(d=1\), the new pair is \((1,mn)\), so \(P_B\) is fixed and \(r_B\) falls by one — by \(mn=d\operatorname{lcm}(m,n)\) and exhaustive gcd casework.
  3. Hence \(F(B)\) is a strictly decreasing positive integer at every move, so no play is infinite — by well-ordering/infinite descent.
  4. When play stops, there are at most one nonunit, because any two entries greater than 1 would constitute a legal move — by the definition of terminality.
  5. Fix a prime \(p\). Under a move, the selected valuation pair \((x,y)=(v_p(m),v_p(n))\) becomes \((\min(x,y),|x-y|)\) — by the elementary valuation formulas for gcd and lcm.
  6. Define \(I_p(B)\) as the gcd of the positive members of \(\{v_p(b):b\in B\}\), leaving zero valuations out. Show that \(I_p\) is invariant whenever \(p\) occurs, including the cases one valuation is zero and \(x=y\) — by the Euclidean identity \(\gcd(x,y)=\gcd(\min(x,y),|x-y|)\) after deleting zeros.
  7. Since every prime in the initial finite set \(P\) retains at least one positive valuation, the terminal board cannot be all ones; together with Step 4 it has exactly one nonunit \(M\) — by Step 6 (or just preservation of nonempty prime support).
  8. At the terminal board the only positive \(p\)-valuation is \(v_p(M)\), so invariance gives \(v_p(M)=g_p\) for each \(p\in P\), while primes outside \(P\) never appear. Unique factorization yields the displayed formula, hence choice independence — by the Fundamental Theorem of Arithmetic under Divisor analysis.
Key lemmas (claim + the one-line mechanism that makes it true):
  - \(F(B)=2^{r_B}P_B\) strictly decreases — because a noncoprime move divides the product by \(d\ge2\) without increasing support, while a coprime move preserves the product but removes one of the two nonunit positions.
  - The gcd of the positive \(p\)-adic exponents is invariant — because zero paired with \(y\) stays \((0,y)\), while two positive exponents undergo one subtractive-Euclidean step, with an equal pair producing one zero that is omitted.
  - The terminal survivor is nontrivial and uniquely specified — because every initially occurring prime continues to have a positive exponent somewhere, and at a one-nonunit state every coordinate invariant is precisely the survivor's exponent.
Open gaps: Builder must fully formalize Steps 2, 6, and 8, especially the exact behavior of \(r_B\) when \(d>1\), all zero/equal valuation subcases, and the convention that the gcd is over positive valuations rather than over all 2026 valuations. All mechanisms are supplied; no conceptual lemma is missing.
Cases to cover: \(d=1\) versus \(d>1\); for each fixed prime, \((x,y)=(0,0)\), exactly one of \(x,y\) zero, unequal positive exponents, and equal positive exponents.
Watch out for: The explorer reports disagreed about zeros: including zero in the ordinary gcd would incorrectly give zero whenever a prime is absent from one place. Do not claim \(\gcd(e,0)=e\) allows a gcd over all 2026 exponents in the multi-entry sense; ordinary \(\gcd(e,0,0)=e\), but the presence of another positive exponent is handled by the positive-set formulation. Do not cite LTE. Do not assert product alone is strict.

omega-lexicographic-euclid: new
Target: Prove both parts for every play and identify the same explicit choice-independent survivor \(M=\prod_{p\in P}p^{\gcd\{v_p(a_i):v_p(a_i)>0\}}\).
Technique: Prime-factor multiplicity descent using the Knowledge Base's **Invariants & monovariants**, followed by **Reformulate** / **change of variables** to subtractive-Euclidean valuation coordinates. Unlike the first route, termination is additive and lexicographic rather than based on board product. It directly adapts the \(L^1\)-norm descent move from `aimo-0440`; `aimo-0516` supports localizing a global gcd structure prime-by-prime, though every transferred valuation statement is proved here.
Skeleton:
  1. Let \(S(B)=\sum_i\Omega(a_i)\), where \(\Omega\) counts prime factors with multiplicity, and let \(r(B)=\#\{i:a_i>1\}\) — by prime factorization.
  2. For a move on \(m,n\) with \(d=\gcd(m,n)\), compute that the new pair contributes \(\Omega(m)+\Omega(n)-\Omega(d)\) to \(S\) — by \(\operatorname{lcm}(m,n)=mn/d\) and complete additivity of \(\Omega\).
  3. If \(d>1\), then \(\Omega(d)>0\), so \(S\) strictly falls; if \(d=1\), then \(S\) is unchanged but \((m,n)\) becomes \((1,mn)\), so \(r\) falls by one. Thus \((S,r)\), lexicographically ordered, strictly decreases at every move — by exhaustive casework.
  4. The lexicographic order on \(\mathbb N^2\) is well-founded, so play terminates; terminality gives at most one nonunit — by infinite descent and the move definition.
  5. For every prime \(p\), pass to exponent piles and prove invariance of the gcd of the positive exponents under \((x,y)\mapsto(\min(x,y),|x-y|)\) — by the elementary valuation identities and the Euclidean algorithm.
  6. Every prime initially present remains represented by a positive exponent, so the terminal state has at least one nonunit and hence exactly one — by the nonempty positive-exponent invariant.
  7. Read each invariant at the terminal state to obtain the explicit exponent of the sole survivor and invoke unique factorization to prove choice independence — by Divisor analysis / Fundamental Theorem of Arithmetic.
Key lemmas (claim + the one-line mechanism that makes it true):
  - \((S,r)\) strictly descends — because the exact loss in \(S\) is \(\Omega(d)\), and the only zero-loss regime \(d=1\) merges two nonunits into one.
  - Positive-exponent gcds survive each move — because the exponent operation is precisely a subtractive Euclidean step, with zeros merely transferred and discarded from the gcd list.
  - A terminal board is not all ones — because for any initially occurring prime, invariance leaves a positive exponent somewhere throughout play.
Open gaps: Builder must expand the exact \(\Omega\) calculation, explicitly justify well-founded lexicographic descent, and prove the valuation lemma in every zero/equality subcase. No appeal to independently chosen primewise moves is permitted.
Cases to cover: \(d=1\) and \(d>1\); the four valuation configurations listed in the first approach.
Watch out for: Do not use the scalar \(S+r\): although it also works here, changing to it would collapse this rival into the same scalar-potential presentation. Ensure \(\Omega(1)=0\). The second output can equal 1 when \(m=n\), which only makes \(r\) fall further.

colored-prime-piles: new
Target: Give an elementary colored-multiset proof that every play terminates at exactly one nonempty place and that the integer encoded there is independent of the play, with each color's final multiplicity equal to the gcd of its positive initial pile sizes.
Technique: **Reformulate** the integers as colored prime atoms and use a combinatorial token monovariant plus a per-color Euclidean invariant. This route avoids formal \(p\)-adic notation in its main presentation and transfers the state-encoding idea of `aimo-0324` and `aimo-0440`, while proving the new pile laws from scratch.
Skeleton:
  1. Assign one color to each prime initially occurring, and represent a board number by a place containing \(e\) atoms of color \(p\) when \(p^e\) exactly divides that number — by unique factorization and Reformulate.
  2. Show directly that a move on two places sends each color's two pile sizes \((x,y)\) to \((\min(x,y),|x-y|)\), all colors using the same chosen pair of places — by comparing common atoms (gcd) and unmatched atoms (the quotient of lcm by gcd).
  3. Let \(A\) be the total number of colored atoms and \(r\) the number of nonempty places. Prove lexicographic descent of \((A,r)\): if the chosen integers share an atom color, at least one common atom is deleted from total multiplicity; if they share none, no atom is deleted but the two occupied places become one empty and one occupied place — by the pile description.
  4. Conclude finite termination and at most one nonempty place — by well-foundedness and terminality.
  5. For each color, prove that the gcd of all its positive pile sizes is preserved by the pile operation — by the subtractive Euclidean identity, separately handling empty piles.
  6. Since each initial color always has at least one nonempty pile, the terminal board has a nonempty place; hence exactly one place remains nonempty — by Step 5.
  7. At that place, each color's multiplicity is forced to be its initial positive-pile gcd, so the encoded integer is uniquely forced and is independent of the sequence — by unique factorization.
Key lemmas (claim + the one-line mechanism that makes it true):
  - Common colored atoms are exactly what the move deletes from total atom count — because the old total exponent \(x+y\) becomes \(\min(x,y)+|x-y|=\max(x,y)\), a loss of \(\min(x,y)\) in each color.
  - If no atom is shared, two occupied places merge into one — because gcd is the empty pile/integer 1 and all atoms move into the second output.
  - Each color has a Euclidean gcd invariant — because replacing two positive pile sizes by their minimum and difference preserves their gcd, while empty piles do not enter the gcd.
Open gaps: Builder must rigorously connect the simultaneous colored operation to the original integer outputs, prove lexicographic descent after summing over colors, and write the zero-pile cases for the color invariant. The approach is otherwise end-to-end.
Cases to cover: Selected places share at least one color versus share no color; per color, both empty, one empty, two unequal nonempty piles, and two equal nonempty piles.
Watch out for: Different colors cannot choose different pairs or different move sequences; only invariant analysis is colorwise. “Occupied place” means the encoded integer exceeds 1. The final proof must translate all token statements back into integer statements.

rewrite-normal-form: new
Target: Prove that the blackboard operation is a terminating rewrite relation whose every reachable normal form is the same one-nonunit board (up to place permutation), thereby proving (a) and (b) and identifying its sole nonunit explicitly.
Technique: Terminating rewrite systems and unique normal form via a **complete invariant**, not via local confluence: exponent-vector embedding, a well-founded order, and invariant-labelled normal forms. This distinct top-level route packages all primes simultaneously. The closest retrieved analogy is `aimo-0678`, whose useful transferable principle is to first control a gcd/lcm process by a global monovariant and only then classify its eventual state; its recurrence-specific least-nondivisor machinery is rejected.
Skeleton:
  1. Embed every positive integer as its finite-support vector of prime exponents and a whole board as an unordered multiset of 2026 such vectors — by change of variables and unique factorization.
  2. Express one rewrite on vectors as coordinatewise \((x_p,y_p)\mapsto(\min(x_p,y_p),|x_p-y_p|)\) — by elementary gcd/lcm valuation laws.
  3. Order states lexicographically by \((A,r)\), where \(A\) is total coordinate mass and \(r\) the number of nonzero vectors. Prove every legal rewrite strictly lowers this order: a shared positive coordinate lowers \(A\), while disjoint supports preserve \(A\) and lower \(r\) — by the identity \(x+y-[\min(x,y)+|x-y|]=\min(x,y)\).
  4. Therefore every rewrite sequence reaches a normal form in finitely many steps; characterize normal forms as boards with at most one nonzero exponent vector — by well-founded descent and the definition of a legal pair.
  5. For each coordinate \(p\), attach the label \(g_p\), the gcd of all positive entries in that coordinate. Prove the whole label vector \(g=(g_p)\) is invariant under rewrites and has the same finite support as the union of current coordinate supports — by the Euclidean identity with zero entries omitted.
  6. Since the initial label has nonempty support, a reachable normal form cannot be the all-zero-vector board. Hence each normal form contains exactly one nonzero vector — by Step 5.
  7. In a one-vector normal form, its nonzero vector must equal the invariant label vector coordinatewise. Thus there is exactly one invariant-compatible normal form up to permutation, so every play has the same survivor — by completeness of the label on the classified normal forms, without any diamond lemma.
Key lemmas (claim + the one-line mechanism that makes it true):
  - Every rewrite lowers \((A,r)\) — because overlap of supports deletes coordinate mass, and lack of overlap merges two nonzero vectors without deleting mass.
  - Labels \(g_p\) are invariant — because every coordinate undergoes a subtractive Euclidean replacement and zeros carry no prime multiplicity.
  - The label is complete on normal forms — because a normal form has one nonzero vector, whose \(p\)-coordinate is then the sole positive input to \(g_p\).
Open gaps: Builder must prove the state-order descent coordinatewise, formalize the finite-support label and its support preservation, and carefully distinguish “unique normal form up to board-place permutation” from local confluence. No local diamond check is required.
Cases to cover: Overlapping versus disjoint supports for descent; zero/equal/unequal coordinate pairs for label invariance; zero versus one nonzero vector in the normal-form classification.
Watch out for: Do not invoke the diamond lemma or assert overlapping moves commute. The operation is not ordinary gcd/lcm sorting. This is a whole alternative proof, not a sublemma for another slug. Ensure the normal-form argument proves exactly one nonunit, not merely at most one.
