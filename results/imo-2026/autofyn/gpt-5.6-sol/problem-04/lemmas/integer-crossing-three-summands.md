# Integer crossing for three positive summands

## Statement
If positive nonintegral real numbers $a,b,c$ have integral sum $n=a+b+c\ge2$, then they can be ordered so that there is an integer $r$ satisfying
\[
b<r<a+b.
\]

## Proof
If one coordinate exceeds $1$, call it $a$ and call either of the other coordinates $b$. Because $b$ is nonintegral, $r=\lfloor b\rfloor+1$ obeys
\[
b<r<b+1<a+b.
\]

Otherwise every coordinate is less than $1$. Their positive integral sum is then less than $3$ and at least $2$, so $n=2$. For any choice of two coordinates as $a,b$, leaving $c$ third, $b<1$ and $a+b=2-c>1$, so $r=1$ works. $\square$
