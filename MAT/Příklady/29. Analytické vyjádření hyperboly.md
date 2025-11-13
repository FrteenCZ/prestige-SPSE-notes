#MAT #MAT/Příklady
[[MAT/Křivky/Hyperbola|Hyperbola]]
# 1. Najděte rovnici hyperboly, která prochází bodem $M[10,2]$ a jejíž asymptoty mají rovnice $y=\pm2x$
$$
\begin{align}
y=\pm 2x \\
y=\pm \frac{b}{a}x \\
\frac{a}{b}=2  \\
a=2b \\
 \\
S[0,0] \\
H: \frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1 \\
\frac{x^{2}}{4b^{2}}-\frac{y^{2}}{b^{2}}=1 \\
x^{2}-4y^{2}=4b^{2} \\
10^{2}-4\cdot2^{2}=4b^{2} \\
b^{2}=21 \\
a^{2}=84 \\
 \\
\boxed{H:\frac{x^{2}}{84}-\frac{y^{2}}{21}=1}
\end{align}
$$

# 2. Vypočtěte délku tětivy, která prochází pravým ohniskem hyperboly $16x^{2}-25y^{2}=400$ kolmo k ose $x$ soustavy souřadnic.

$$
\begin{align}
\frac{x^{2}}{5^{2}}-\frac{y^{2}}{4^{2}}=1 \\
e^{2}= 5^{2}+4^{2} \\
e=\sqrt{ 41 } \\
 \\
x=\sqrt{ 41 } \\
16\cdot 41-25y^{2}=400  \\
25y^{2}=656-400 \\
25y^{2}=256 \\
y^{2}=10.24 \\
y=\pm3.2 \\
\boxed{2\cdot3.2=6.4}
\end{align}
$$

# 3. Vypočtěte souřadnice průsečíků hyperboly $3x^{2}-y^{2}-6x+4y-4=0$ a přímky, která prochází bodem $A[2,0]$ kolmo k přímce $x-y=7$.

$$
\begin{align}
x-y=a \\
2-0=a \\
a=2 \\
 \\
x-y=2 \\
3x^{2}-y^{2}-6x+4y-4=0 \\
 \\
x=2-y \\
3x^{2}-y^{2}-6x+4y-4=0 \\
 \\
3\cdot(2-y)^{2}-y^{2}-6\cdot(2-y)+4y-4=0 \\
3\cdot(4-4y+y^{2})-y^{2}-12+6y+4y-4=0 \\
12-12y+3y^{2}-y^{2}-12+6y+4y-4=0 \\
2y^{2}-2y-4=0 \\
y=\{ -1,2 \} \\
x=\{ 3,0 \} \\
\boxed{H=\{ [3,-1],[0,2] \}}
\end{align}
$$

# 4. Napište rovnici hyperboly, která je určena ohnisky $F_{1}[-14,-5]$, $F_{2}[-14,5]$ a prochází bodem $A[6,-20]$.

$$
\begin{align}
S[-14,0]\\
e=5 \\
e^{2}=a^{2}+b^{2} \\
a^{2}=25-b^{2} \\
 \\
\frac{(x+14)^{2}}{25-b^{2}}-\frac{y^{2}}{b^{2}}=1 \\
\frac{(6+14)^{2}}{25-b^{2}}-\frac{20^{2}}{b^{2}}=1 \\
20^{2}\cdot b^{2}-20^{2}\cdot(25-b^{2})=(25-b^{2})\cdot b^{2} \\
400b^{2}-10000+400b^{2}=25b^{2}-b^4 \\
b^4+775b^2=10000 \\
u=b^{2} \\
u^{2}+775u-10000=0 \\
u=\{ 12.69526, -787.69526 \} \\
b=\pm \sqrt{ u } \\
b=\{ 3.56304084, -3.56304084, 28.0659092i, -28.0659092i \} \\
b= [3.56304084, -3.56304084, 28.0659092i, -28.0659092i]  \\
b \in \mathbb{C} \implies \text{kružnice} \\
\boxed{H:\frac{(x+14)^{2}}{12.30473997249209}-\frac{y^{2}}{12.69526002750791}=1}
\end{align}
$$

# 5. Napište rovnici tečny hyperboly $4x^{2}-5y^{2}-20=0$ v jejím bodě $T[x_{T},4]$ .

$$
\begin{align}
4x^{2}-5y^{2}-20=0 \\
5y^{2}+20=4x^{2}  \\
1.25y^{2}+5=x^{2} \\
x=\pm \sqrt{ 1.25y^{2}+5 } \\
f(y)=\pm \sqrt{ 1.25y^{2}+5 } \\
f'(y) = \pm\frac{\sqrt{5} y}{2\sqrt{y^2 + 4}} \\
p:x=my-k  \\
f(y)=f(y)'y-k  \\
k=f(y)y-f(y) \\
p:x=f(Y)'y-f(Y)'Y+f(Y)\\
\boxed{p:x=y+1} \\
\boxed{p:-x=y+1}
\end{align}
$$
