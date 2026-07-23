Let (A=a_1), and for an integer (m>1), let
[
\pi(m)={p:p\text{ is prime and }p\mid m}
]
be its prime support.

The recurrence is equivalent to scanning the integers (A,A+1,A+2,\ldots), accepting (A), and thereafter
accepting an integer precisely when it has gcd greater than (1) with every previously accepted integer. Indeed,
the accepted integers are exactly (a_1,a_2,\ldots).

The sequence is unbounded: every accepted integer has gcd greater than (1) with (A), so every sufficiently
large multiple of (A) is compatible with all previously accepted integers.

For every finite nonempty set (S) of primes, define
[
c(S)=\min{m\geq A:\pi(m)=S}.
]
This exists, for instance by taking a sufficiently large power of (\prod_{p\in S}p).

We first observe that either every integer (m\geq A) with (\pi(m)=S) is accepted, or none is.

Indeed, if (c(S)) is rejected, it is coprime to some earlier accepted integer, which is then also coprime to
every integer having prime support (S). Conversely, suppose (c(S)) is accepted, and let (m>c(S)) have support
(S). Every accepted integer preceding (c(S)) meets (S), since it has gcd greater than (1) with (c(S)). Every
accepted integer between (c(S)) and (m) also meets (S), since it was required to have gcd greater than (1) with
(c(S)). Thus (m) is accepted.

Let (\mathcal F) be the family of finite nonempty prime sets (S) for which (c(S)) is accepted. Two members of
(\mathcal F) always intersect, because any two accepted integers have gcd greater than (1).

Moreover, if (S\notin\mathcal F), then when (c(S)) is rejected there is an accepted integer (b<c(S)) such that
[
\pi(b)\cap S=\varnothing. \tag{1}
]
In particular, (\mathcal F) is upward-closed. For if (X\in\mathcal F), (X\subseteq Y), and (Y\notin\mathcal F),
then (1) would give a member of (\mathcal F) disjoint from (Y), hence disjoint from (X), contradicting the
pairwise-intersection property.

Call (M\in\mathcal F) minimal if no proper subset of (M) belongs to (\mathcal F). Every member of (\mathcal F)
contains such a minimal member. We prove that only finitely many primes can occur in minimal members.

For a finite prime set (S), write
[
d(S)=\prod_{p\in S}p.
]

Fix a prime (q) occurring in some minimal member. Among all minimal members containing (q), choose (M) for
which (d(M)) is smallest.

If (M={q}), then ({q}) must intersect (\pi(A)\in\mathcal F), so (q\mid A), and hence (q\leq A<A^2).

Now suppose (|M|>1), and put
[
S=M\setminus{q}.
]
By minimality, (S\notin\mathcal F). Therefore there is an accepted integer (b<c(S)) such that
[
\pi(b)\cap S=\varnothing.
]
Let (B=\pi(b)). Since (B,M\in\mathcal F), they intersect. As (B) is disjoint from (S=M\setminus{q}), we must
have
[
B\cap M={q}. \tag{2}
]

Choose a minimal member (N\in\mathcal F) contained in (B). Since (N) and (M) intersect, (2) implies (q\in N).
By the choice of (M),
[
d(M)\leq d(N)\leq d(B)\leq b<c(S). \tag{3}
]

We claim that (d(S)<A). Otherwise (d(S)\geq A), and because every integer with prime support (S) is divisible
by (d(S)), we would have
[
c(S)=d(S).
]
But (d(M)=q,d(S)>d(S)=c(S)), contradicting (3).

Thus (d(S)<A). Choose any (r\in S), and let (k\geq1) be minimal such that
[
d(S)r^k\geq A.
]
This number has prime support (S), and minimality of (k) gives
[
d(S)r^k<Ar<A^2,
]
because (r\leq d(S)<A). Consequently,
[
c(S)<A^2.
]
Since (q\mid b), we have by (b<c(S))
[
q\leq b<c(S)<A^2.
]

We have proved that every prime occurring in any minimal member of (\mathcal F) is less than (A^2). Hence there
are only finitely many possible minimal members. Denote their collection by
[
\mathcal M={M_1,\ldots,M_s}.
]
Because (\mathcal F) is upward-closed and every member contains a minimal member,
[
S\in\mathcal F
\quad\Longleftrightarrow\quad
M_j\subseteq S\text{ for some }j. \tag{4}
]

Let
[
D_j=\prod_{p\in M_j}p,
\qquad
L=\operatorname{lcm}(D_1,\ldots,D_s).
]
By (4), an integer (m\geq A) occurs in the sequence exactly when
[
D_j\mid m
\quad\text{for at least one }j. \tag{5}
]
Since every (D_j\mid L), condition (5) is invariant under replacing (m) by (m+L).

Let (T) be the number of sequence terms in the half-open interval
[
[A,A+L).
]
This is positive because (A=a_1) lies there. For every (n), translation by (L) gives a bijection between the
sequence terms in ([A,a_n]) and those in ([A+L,a_n+L]). There are exactly (T) additional terms in ([A,A+L)).
Therefore (a_n+L) is the ((n+T))-th term of the sequence. Hence
[
\boxed{a_{n+T}=a_n+L}
]
for every positive integer (n).

─ Worked for 9m 56s ─────────────────────────────────────────────────────────────────────────────────────────────

