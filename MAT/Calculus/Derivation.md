#MAT #MAT/Calc
# Basic rules

| If $f$ is a function of the independent variable $x$, the derivative of the function is defined by the equation: | $$f^{\prime}(x)=\lim_{h \rightarrow 0} \dfrac{f(x+h)-f(x)}{h}$$                                                                                                                                                                                                                                                                                                            |
| :--------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![](../../Images/Pasted%20image%2020260217161736.png)                                                            | $f(x+h)-f(x)$ is the height of the triangle. <br> $h$ is the base length of the triangle. $$\text { The slope is: } \quad \tan \alpha=\dfrac{f(x+h)-f(x)}{(x+h)-x}$$<br> So when $h$ tends to zero the expression become: $$f^{\prime}(x)=\lim _{h \rightarrow 0} \dfrac{f(x+h)-f(x)}{h}$$ <br> This is the slope of the tangent line to the function $f(x)$ at point $x$. |
| **Chain rule** <br>$f(x)=u(g(x))$                                                                                | $$f'(x)=u'\cdot g' =u'(g) \cdot g'$$                                                                                                                                                                                                                                                                                                                                       |
| **Multiplication rule**<br>$f(x)=g(x) \cdot u(x)$                                                                | $$f^{\prime}(x)=g^{\prime} u+g u^{\prime}$$                                                                                                                                                                                                                                                                                                                                |
| **Quotient rule**<br>$f(x)=\dfrac{g(x)}{u(x)}$                                                                   | $$f^{\prime}(x)=\dfrac{g^{\prime} \cdot u-g \cdot u^{\prime}}{u^2} \quad u \neq 0$$                                                                                                                                                                                                                                                                                        |
| **Reciprocalrule**<br>$f(x)=\dfrac{1}{u(x)}$                                                                     | $$f^{\prime}(x)=-\dfrac{u^{\prime}}{u^2} \quad u \neq 0$$                                                                                                                                                                                                                                                                                                                  |
| **Addition rule**<br>$f(x)=(a\cdot g(x)+b\cdot u(x))$<br>$a,b \in \mathbb{R}$                                    | $$f'=(a\cdot g + b\cdot u)^{\prime}=a g^{\prime}+b u^{\prime}$$                                                                                                                                                                                                                                                                                                            |
| **Constant rule**<br>$f(x)$ is a constant                                                                        | $$f^{\prime}=0$$                                                                                                                                                                                                                                                                                                                                                           |
| **Notations**<br>all the following notations for derivatives are valid                                           | .   $\text{First derivative:} \quad \dfrac{d f}{d x} \equiv f^{\prime} \equiv \dot{f} \equiv f_x$ <br>$\text{Second derivative:} \quad \dfrac{d^2 f}{d x^2} \equiv \dfrac{d}{d x}\left(\dfrac{d f}{d x}\right) \equiv f^{\prime \prime} \equiv \ddot{f} \equiv f_{x x}$                                                                                                    |

---

# Derivation tables
## Algebric and Logarithmic functions

| $\dfrac{d}{d x}(c)=0$                                                                | $\dfrac{d}{d x}(c x)=c$                                                                     | $\dfrac{d}{d x}\left(x^c\right)=c x^{c-1}$                                                                |
| :----------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------- |
| $\dfrac{d}{d x}\left(c^x\right)=c^x \ln (c) \quad c>0$                               | $\dfrac{d}{d x}\left(x^x\right)=x^x(1+\ln x)$                                               | $\dfrac{d}{d x}\left(e^x\right)=e^x$                                                                      |
| $\dfrac{d}{d x}\left(\dfrac{1}{x}\right)=\dfrac{-1}{x^2}$                            | $\dfrac{d}{d x}\left(\dfrac{1}{x^2}\right)=\dfrac{-2}{x^3}$                                 | $\dfrac{d}{d x}\left(\dfrac{1}{x^n}\right)=\dfrac{-n}{x^{n+1}}$                                           |
| $\dfrac{d}{d x}(\sqrt{x})=\dfrac{1}{2 \sqrt{x}} \quad x>0$                           | $\dfrac{d}{d x}(\sqrt[3]{x})=\dfrac{1}{3 \cdot \sqrt[3]{x^2}}$                              | $\dfrac{d}{d x}(\sqrt[n]{x})=\dfrac{1}{n \cdot \sqrt[n]{x^{n-1}}}$                                        |
| $\dfrac{d}{d x}\left(\dfrac{1}{\sqrt{x}}\right)=\dfrac{-1}{2 \sqrt{x^3}}$            | $\dfrac{d}{d x}\left(\dfrac{1}{\sqrt[3]{x}}\right)=\dfrac{-1}{3 \cdot \sqrt[3]{x^4}}$       | $\dfrac{d}{d x}\left(\dfrac{1}{\sqrt[n]{x}}\right)=\dfrac{-1}{n \cdot \sqrt[n]{x^{n+1}}}$                 |
| $\dfrac{d}{d x}(\ln x)=\dfrac{1}{x} \quad x>0$                                       | $\dfrac{d}{d x}(x \cdot \ln x)=\ln x+1$                                                     | $\dfrac{d}{d x}\left(\log _c x\right)=\dfrac{1}{x \ln c} \quad c>0 \quad c \neq 1$                        |
| $\dfrac{d}{d x}\left(\dfrac{1}{\ln x}\right)=\dfrac{-1}{x(\ln x)^2}$                 | $\dfrac{d}{d x}\left(\dfrac{1}{x \cdot \ln x}\right)=\dfrac{-(\ln x+1)}{(x \cdot \ln x)^2}$ | $\dfrac{d}{d x}\left(\dfrac{1}{\log _c x}\right)=\dfrac{-1}{x \cdot \ln c \cdot\left(\log _c x\right)^2}$ |
| $\dfrac{d}{d x}\left(\dfrac{1}{x+1}\right)=\dfrac{-1}{(x+1)^2}$                      | $\dfrac{d}{d x}\left(\dfrac{1}{(x+1)^2}\right)=\dfrac{-2}{(x+1)^3}$                         | $\dfrac{d}{d x}\left(\dfrac{1}{(x+1)^n}\right)=\dfrac{-n}{(x+1)^{n+1}}$                                   |
| $\dfrac{d}{d x}\left(\frac{1}{\sqrt{x+1}}\right)=\dfrac{-1}{2 \cdot \sqrt{(x+1)^3}}$ | $\dfrac{d}{d x}\left(\frac{1}{\sqrt[3]{x+1}}\right)=\dfrac{-1}{3 \cdot \sqrt[3]{(x+1)^4}}$  | $\dfrac{d}{d x}\left(\frac{1}{\sqrt[n]{x+1}}\right)=\dfrac{-1}{n \cdot \sqrt[n]{(x+1)^{n+1}}}$            |
## Trigonometric Functions

| $\dfrac{d}{d x} \sin x=\cos x$                           | $\dfrac{d}{d x} \sinh x=\cosh x$                                                    |
| :------------------------------------------------------- | :---------------------------------------------------------------------------------- |
| $\dfrac{d}{d x} \cos x=-\sin x$                          | $\dfrac{d}{d x} \cosh x=\sinh x$                                                    |
| $\dfrac{d}{d x} \tan x=\sec ^2 x=\dfrac{1}{\cos ^2 x}$   | $\dfrac{d}{d x} \tanh x=1-\tanh ^2 x=\operatorname{sech}^2 x$                       |
| $\dfrac{d}{d x} \cot x=-\csc ^2 x=-\dfrac{1}{\sin ^2 x}$ | $\dfrac{d}{d x} \operatorname{coth} x=-\operatorname{csch}^2 x$                     |
| $\dfrac{d}{d x} \csc x=-\csc x \cot x$                   | $\dfrac{d}{d x} \operatorname{csch} x=-\operatorname{csch} x \operatorname{coth} x$ |
| $\dfrac{d}{d x} \sec x=\sec x \tan x$                    | $\dfrac{d}{d x} \operatorname{sech} x=-\operatorname{sech} x \tanh x$               |

| $\dfrac{d}{d x} \sin ^{-1} x=\dfrac{1}{\sqrt{1-x^2}}$          $\|x\|<1$  | $\dfrac{d}{d x} \sinh ^{-1} x=\dfrac{1}{\sqrt{1+x^2}}$                       |
| :------------------------------------------------------------------------ | :--------------------------------------------------------------------------- |
| $\dfrac{d}{d x} \cos ^{-1} x=\dfrac{-1}{\sqrt{1-x^2}}$          $\|x\|<1$ | $\dfrac{d}{d x} \cosh ^{-1} x=\dfrac{1}{\sqrt{x^2-1}}$                       |
| $\dfrac{d}{d x} \tan ^{-1} x=\dfrac{1}{1+x^2}$                            | $\dfrac{d}{d x} \tanh ^{-1} x=\dfrac{1}{1-x^2}$      $\|x\|<1$               |
| $\dfrac{d}{d x} \cot ^{-1} x=\dfrac{-1}{1+x^2}$                           | $\dfrac{d}{d x} \operatorname{coth}^{-1} x=\dfrac{1}{1-x^2}$       $\|x\|<1$ |
| $\dfrac{d}{d x} \csc ^{-1} x=\dfrac{-1}{x \sqrt{x^2-1}}$        $\|x\|>1$ | $\dfrac{d}{d x} \operatorname{csch}^{-1} x=\dfrac{-1}{x \sqrt{x^2+1}}$       |
| $\dfrac{d}{d x} \sec ^{-1} x=\dfrac{1}{x \sqrt{x^2-1}}$        $\|x\|>1$  | $\dfrac{d}{d x} \operatorname{sech}^{-1} x=\dfrac{-1}{x \sqrt{x^2-1}}$       |


---

# Příklady
$$
\begin{align}
f_1=&\sin 5x \\
f_{1}'=&5\sin 5x \\
 \\
f_{2}=&\sqrt{ \sin x } \\
f_{2}'=&\frac{\cos x}{2\sqrt{ \sin x }} \\
 \\
f_{3}=&\ln^6x \\
f_{3}'=&\frac{1}{x} \cdot 6 \cdot \ln^5x \\
 \\
f_{4}=&e^\sqrt{ \sin x } \\
f_{4}'=&\cos x \cdot \frac{1}{2\sqrt{ \sin x }}\cdot e^\sqrt{ \sin x }=\frac{\cos x \cdot e^\sqrt{ \sin x }}{2\sqrt{ \sin x }} \\
  \\
f_{5}=& 4^{\sin x^{2}} \\
f_{5}'=&2x\cdot \cos x^{2}\cdot4^{\sin x^{2}} \cdot \ln4 \\
 \\
f_{6}=&(x^{2}+2)^{3}\cdot \cos ^{2}x \\
f_{6}'=&2x\cdot 3 \cdot (x^{2}+2)^{2}\cdot \cos ^{2}x-(x^{2}+2)^{3} \cdot 2 \cdot \cos x \cdot \sin x
\end{align}
$$
## Derivace vyšších řádů
$$
\begin{align}
f_{1}=&4x^5-x^4+3x^{2}-5 \\
f_{1}''''=&480x-24 \\
 \\
f_{2}=&\frac{x-1}{x+1} \\
f_{2}'=& \frac{2}{(x+1)^{2}} \\
f_{2}''=& \frac{0-2\cdot 1\cdot2 \cdot (x+1)}{(x+1)^4}=-\frac{4}{(x+1)^{3}}
\end{align}
$$

# Využití
## Monotónnost
$f:y=f(x)$ ma v každém bodě $(x,f(x))$ derivaci:
- $f'(x)>0$ - rostoucí
- $f'(x)<0$ - klesající
- $f'(x)=0$ - konstantní (*max / min*)
---
$$
\begin{align}
f_{1}=&2x^{3}+3x^{2}-12x-12 \\
f_{1}'=&6x^{2}+6x-12 \\
f_{1}'=&6(x+2)(x-1) \\
f_{1}'>&0 &&x \in \mathbb{R}-\langle-2,1\rangle && \text{rostoucí} \\
f_{1}'<&0
\end{align}
$$
$$
\begin{align}
f_{2}=&\frac{4-3x}{x-x^{2}} \\
f_{2}'=&\frac{-6x+6x^{2}-4+8x+3x-6x^{2}}{(x-x^{2})^{2}} \\
f_{2}'=&\frac{-3x^{2}+8x-4}{(x-x^{2})^{2}} \\
f_{2}'>&0 \quad x \in \left( \frac{2}{3},2 \right) \quad \text{roustoucí}  \\
f_{2}'<&0 \quad x \in \mathbb{R}-\left( \frac{2}{3},2 \right) \quad \text{klesající} 
\end{align}
$$
---
$$
\begin{align}
f_{1}&=x^{3}-x \\
f_{1}'&=3x^{2}-1 \\
f_{1}'&= 3\left( x- \frac{\sqrt{ 3 }}{3} \right)\left( x+\frac{\sqrt{ 3 }}{3} \right) \\
&+ \quad - \quad + \\
 \\
f_{2}&=2\tan x- \frac{x^4}{3}+ \frac{\sqrt[3]{ x }}{x^{2}} \\
f_{2}'&=\frac{2}{\cos ^{2}x}-\frac{4x^{3}}{3}+\frac{-11}{3x^{\frac{2}{3}}} \\
 \\
f_{3}&=\cos x^{3} \\
f_{3}'&=-2x^{2}\sin x^{3} \\
 \\
f_{4}&=\frac{3-x^{3}}{1-\sin x} \\
f_{4}'&=\frac{-3x^{2}\left(1-\sin x\right)+\left(3-x^{3}\right)\cos x}{\left(1-\sin x\right)^{2}}
\end{align}
$$
## Extrémy
$$
\boxed{f'(x)=0} 
$$
$$
\begin{align}
f_{1}&=\frac{1}{3}x^{3} -\frac{1}{2}x^{2}-2x+1 \\
f_{1}'&=x^{2}-x-2=(x-2)(x+1) \\
(-\infty-1)&:+ \\
\langle-1,2\rangle&:- \\
(2,\infty)&:+
\end{align}
$$
## Inflexní bod
$$
\begin{gathered}
\boxed{f'(x)=0 \quad f''(x)=0,\text{neexistuje}}  \\
\boxed{f''(x)>0\implies \text{konvexní}} \quad \boxed{f''(x)<0\implies \text{konkávní}} 
\end{gathered}
$$
---
$$
\begin{align}
f_{1}&=x^4-2x^{2}+5 \\
f_{1}'&=4x^{3}-4x \\
f_{1}''&=12x^{2}-4=4(\sqrt{ 3 }x-1)(\sqrt{ 3 }x+1) \\
\left( -\infty,-\frac{1}{\sqrt{ 3 }} \right)&: \text{convex} \\
\left( -\frac{1}{\sqrt{ 3 }}, \frac{1}{\sqrt{ 3 }} \right)&: \text{concave} \\
\left( \frac{1}{\sqrt{ 3 }},\infty \right)&: \text{convex}
\end{align}
$$
# Průběh funkcí

1. Definiční obor (body nespojitosti)
2. průsečíky s osami
3. sudá nebo lichá funkce
4. intervaly monotónosti
5. extrémy
6. inflexní body
7. konvexnost, konkávnost
8. limity v nevlastních bodech + bodech nespojitosti
9. Sestrojíme graf
10. PROFIT!!!

---
$$
\begin{align}
&&f_{1}(x)=x^{3}+\frac{x^4}{4} \\
 \\
1) && D_{f_{1}}=\mathbb{R} \\
 \\
2) && P_{x_{1}}=[0,0] \\
&& P_{x_{2}}=[-4,0] \\
 \\
3) && \text{sudá} \\
 \\
4) && (-\infty,-3) \quad \text{klesající} \\
&& (-3,0) \quad \text{rostoucí} \\
&& (0,\infty) \quad \text{rostoucí} \\
 \\
5) && f_{1}''=6x+3x^{2} \\
&& f_{1}''(0)=0 \quad \text{není extrém} \\
&& f_{1}''(-3)>0 \quad \text{minimum} \quad [-3,-6.75] \\
 \\
6+7) && (-\infty,2) \quad + \\
&& (-2,0) \quad - \\
&& (0, \infty) \quad + \\
&& [0,0] \quad [-2,-4] \\
 \\
.8) && \lim_{ x \to \infty } \left( x^3+\frac{x^4}{4} \right) = \infty \\
&& \lim_{ x \to -\infty } = \infty
\end{align}
$$---
min $A_{cil}$ 
$V=\text{konst.}$
$$
\begin{align}
V=\pi r^{2}v \\
S=2\pi r^{2}+2\pi rv \\
 \\
S=2\pi r^{2}+2\pi r \cdot \frac{V}{\pi r^{2}} \\
S=2\pi r^{2}+\frac{2V}{r} \\
S'=4\pi r-\frac{2V}{r^{2}} \\
0=\frac{4\pi r^{3}-2V}{r^{2}} \\
0=2\pi r^{3}-V \\
r=\sqrt[3]{ \frac{V}{2\pi} } \\
v=\frac{\sqrt[3]{V  }}{\pi}
\end{align}
$$

---

$V=\pu{ 200m3 }$
$l=4w$
$m^2$ podstavy je $\frac{1}{2}$ než $m^2$ stěny
cena podstavy je 1/2 ceny stěny

$$
\begin{align}
V=l\cdot w\cdot h \\
P=\frac{p}{2}\cdot w\cdot l+p\cdot h\cdot2\cdot(w+l) \\
l=4w \\
 \\
V=4w^{2}h \\
P=2p\cdot w^{2}+10phw \\
 \\
P=2p\cdot w^{2}+\frac{2.5pV}{w} \\
P'=4p\cdot w-\frac{2.5pV}{w^{2}} \\
P'=\frac{4p\cdot w^3-2.5pV}{w^{2}} \\
4\cdot w^3=2.5V \\
w^3=0.625V \\
w=\sqrt[3]{ 0.625V }=5 \\
l=20 \\
h=2
\end{align}
$$
---
$$
\begin{align}
&&f(x)=\frac{x}{x^{2}-1} \\
1)&& D=\mathbb{R}-\{ -1,1 \} \\
2) && P=[0,0] \\
3) && \text{lichá} \\
4) && f'(x)=\frac{(x^{2}-1)-2x^{2}}{(x^{2}-1)^{2}} \\
&& f'(x)=-\frac{x^{2}+1}{x^4-2x^{2}+1} \\
&& D \text{ klesající} \\
5) && \emptyset \\
6) &&f''(x)=-\frac{(2x)(x^{2}-1)^{2}-2(x^{2}-1)(2x)(x^{2}+1)}{(x^{2}-1)^4} \\
&&f''(x)=\frac{2x(x^4+2x^2-3)}{(x^{2}-1)^4} \\
&& \emptyset \\
7) && (-\infty,-1)\text{ concave} \\
&& (-1,0)\text{ convex} \\
&& (0,1)\text{ concave} \\
&& (1,\infty)\text{ convex}
\end{align}
$$