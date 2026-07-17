# Safe-child nonintegrality lemma

## Statement
Let real numbers $a,b,c,s,x$ satisfy $a+b+c=s$ and $0<x<a$. Suppose $a,b,c,s$ are all nonintegral. For the two triples
\[
(x,b,a+c-x),\qquad (a-x,c,b+x),
\]
at least one triple has all three coordinates nonintegral.

## Proof
The first triple already has the nonintegral coordinate $b$, so if it is not entirely nonintegral, then either $x$ or $a+c-x$ is integral. Similarly, the second triple already has the nonintegral coordinate $c$, so if it is not entirely nonintegral, then either $a-x$ or $b+x$ is integral.

If neither triple were entirely nonintegral, one of four pairs would therefore consist of integers. The pair $(x,a-x)$ has sum $a$; the pair $(x,b+x)$ has difference $b$; the pair $(a+c-x,a-x)$ has difference $c$; and the pair $(a+c-x,b+x)$ has sum $a+b+c=s$. Each possibility would make one of $a,b,c,s$ integral, contrary to the hypotheses. Hence at least one triple is entirely nonintegral. $\square$
