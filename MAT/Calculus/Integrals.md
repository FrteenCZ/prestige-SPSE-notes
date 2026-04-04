#MAT #MAT/Calc
# **Integrals Basic Data**
| ![](../../Images/Pasted%20image%2020260318104358.png)                                                                                | *Definite integral* <br> The definite integral of a function from point $a$ to point $b$ is equivalent to the area between the graph and the $x$ axis. <br> The integral can be calculated by finding the sum of each rectangle area: <br> First rectangle area is: $\quad f\left(\varepsilon_1\right) \cdot\left(x_1-a\right)$ <br> Second rectangle area is: $f\left(\varepsilon_2\right) \cdot\left(x_2-x_1\right)$ <br> If $\Delta x_k=x_k-x_{k-1}$ then the area is: $\text { area }=\lim _{\Delta x_k \rightarrow 0} \sum_{k=1}^n f\left(\varepsilon_k\right) \cdot \Delta x_k=\int_a^b f(x) d x$ |
| :----------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| If $f=f(x)$ and $g=g(x)$ then:                                                                                                       | $$\int_a^b(f(x) \pm g(x)) d x=\int_a^b f(x) d x \pm \int_a^b g(x) d x$$                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| If $f=f(x)$ is defined in the range $a$ to $b$ and $c$ is a point inside this range then:                                            | $$\int_a^b f(x) d x=\int_a^c f(x) d x+\int_c^b f(x) d x$$                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| If $C$ is a constant then:                                                                                                           | $$\int_a^b C f(x) d x=C \int_a^b f(x) d x$$                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Integration ranges can be changed according to the rule:                                                                             | $$\int_a^b f(x) d x=-\int_b^a f(x) d x$$                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| To the value received after integration always add a term of a constant $C$ (this term is omitted in the following integral tables). | $$\int a d x=a x+C$$                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Integration between two equals points are zero.                                                                                      | $$\int_a^a f(x) d x=0$$                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

| Integration by parts: because $d(u v)=u d v+v d u$ we can integrate both sides: | $$\int u d v=u v-\int v d u$$                                                                                                                                                                                                                                     |
| :------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Example: find the integral $$\int x e^x d x$$                                   | Write this integral in the form $\int u d v$ $\begin{aligned} u & =x \text { and } d v=e^x d x \\ \text { then } d u & =d x \text { and } v=e^x \\ \text { The integration is: } & \int x e^x d x=x e^x-\int e^x d x \\ =x e^x-e^x & +C=e^x(x-1)+C \end{aligned}$ |

| Integration by substitution: If $f$ is a continuous function, then:        | $$\int_a^b f(g(t)) g^{\prime}(t) d t=\int_{g(a)}^{g(b)} f(x) d x$$                                                                                                                                                                                                                                                                                                             |
| :------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Example: find the integral $$\int_0^2 \frac{(2 x+1) d x}{\sqrt{x^2+x+1}}$$ | Substitute: $\quad u=x^2+x+1$ <br> Then $\quad d u=(2 x+1) d x$ $\int_1^7\left(\frac{(2 x+1) d u}{\sqrt{u}(2 x+1)}\right)=\int_1^7 \frac{d u}{\sqrt{u}}=\left.2 \sqrt{u}\right\|_0 ^7=2(\sqrt{7}-1)$ <br> The new integration limits are: <br> $u(x=0)=1 \quad$ and $\quad u(x=2)=7$ <br> Note: we could resubstitute the $u=u(x)$ value and leave the old integration limits. |

| Integration contains the function and its derivative in the numerator: | $$\int \frac{f^{\prime}(x)}{f(x)}=\ln \|f(x)\|$$                                                                                                                                  |
| :--------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Example: find the integral $$\int \frac{\cos x}{\sin x+2} d x$$        | We see that $\frac{d(\sin x+2)}{d x}=\cos x$ <br> According to the above rule the integral is simple: $\int \frac{\cos x}{\sin x+2} d x=\ln \|\sin x+2\|+C$                       |
| Example: find the integral $$\int \frac{3 x^2}{x^3+2} d x$$            | Because: $\quad \frac{d\left(x^3+2\right)}{d x}=3 x^2$ is the same as the numerator then the result of the integral is: $\int \frac{3 x^2}{x^3+2} d x=\ln \left\|x^3+2\right\|+C$ |

---
# Tables

| $$\int 1 dx=x+c$$                 | $$\int x^n=\frac{x^{n+1}}{n+1}+c$$ | $$\int 0dx=c$$              | $$\int e^xdx=e^x+c$$                    |
| --------------------------------- | ---------------------------------- | --------------------------- | --------------------------------------- |
| $$\int \frac{1}{x}dx=\ln\|x\|+c$$ | $$\int a^xdx=\frac{a^x}{\ln a}+c$$ | $$\int \sin xdx=-\cos x+c$$ | $$\int\frac{1}{\cos ^{2}x}dx=\tan x+c$$ |

---
# Určitý integrál
$$
\begin{gathered}
f(x) \text{ spojitá v } \langle a,b \rangle \\
I=\int_{a}^b f(x)dx=\text{určitý integrál} \\
\int_{a}^b f(x)dx=[F(x)]_{a}^b =F(b)-F(a)
\end{gathered}
$$

---

# ILATE (nebo LIATE) priority list
$$
\int u \cdot v' dx=uv-\int u'vdx
$$
Vyber $u$ podle listu (první nahoře)

| **I** | **Inverse Trigonometric** | $$\sin^{-1}x,~\tan^{-1}x,~\dots$$        |
| ----- | ------------------------- | ---------------------------------------- |
| **L** | **Logarithmic**           | $$ \log_{3}x,~\log x,~\ln x,~\dots $$    |
| **A** | **Algebraic**             | $$ x^{3},~\sqrt[3]{ x },~x^{2},~\dots $$ |
| **T** | **Trigonometric**         | $$ \sin x,~\tan x,~\csc x,~ \dots$$      |
| **E** | **Exponential**           | $$ 3^x,~e^x,~\dots $$                    |


---
# Příklady
$$
\begin{align}
\int (x^{3}-6x^{2}+5x-4)dx=\frac{x^4}{4}-2x^{3}+5 \frac{x^{2}}{2}-4x+c \\
 \\
\int (4-4x^{0.5} +x)dx=4x-\frac{4x^{1.5}}{1.5}+\frac{x^{2}}{2}+c \\
 \\
\int (x^{-2}-4x^{-2/3})=-\frac{1}{x}-12\sqrt[3]{ x }+c
\end{align}
$$
---
$$
\begin{align}
\int x^{3}+3\sqrt{ x }+x^{-5}dx=\frac{x^4}{4}+2 \sqrt{ x^{3} }-\frac{1}{4x^4}+c \\
 \\
\int(x^{2}-x^{-3}+5x)dx=\frac{x^{3}}{3}+\frac{1}{2x}+\frac{5}{2}x^{2}+c \\
 \\
\int \frac{(\sqrt{ x }-1)^{2}}{x}dx=\int \frac{x-2\sqrt{ x }+1}{x}dx=\int(1-2x^{-1/2}+x^{-1})dx=x-\frac{2\sqrt{ x }}{\frac{1}{2}}+\ln|x|= \\
x-4\sqrt{ x }+\ln |x|+c \\
 \\
\int \frac{x^{2}\sqrt{ x }}{x^5}dx=\int x^{-2.5}dx=\frac{x^{-3/2}}{-\frac{3}{2}}=-\frac{2}{3\sqrt{ x^{3} }}+c \\
 \\
\int (x^{2}-1)(x+2)^{2}dx=\int(x^{2}-1)(x^{2}+4x+4)dx=\int(x^4-x^{2}+4x^{3}-4x+4x^{2}-4)dx= \\
=\frac{x^{5}}{5}-x+x^4-2x^{2}+\frac{4x^{3}}{3}-4x+c \\
 \\
\int x^{3}\sqrt[5]{ x^{2} }dx=\int x^{3.4}dx=\frac{x^{4.4}}{4.4}+c \\
 \\
\int \tan ^{2}xdx=\int \frac{\sin ^{2}x}{\cos ^{2}x}dx=\int \frac{1-\cos ^{2}x}{\cos ^{2}x}dx=\int\left( \frac{1}{\cos ^{2}x}-1 \right)dx=\tan x-x+c \\
 \\
\int \cot ^{2}xdx=-\cot x-x+c \\
 \\
\int \frac{\sin 2x}{\sin x}dx=\int \frac{2\sin x\cdot\cos x}{\sin x}dx=-2\cos x+c \\
 \\
\int \frac{\cos2x}{\cos ^{2}x}dx=\int \left( 1-\frac{1}{\cos ^{2}x}+1 \right)dx=2x-\tan x+c \\
 \\
 \\
\int (2e^x)-\frac{2}{x})dx=2e^x-2\ln|x|+c
\end{align}
$$---
$$
\begin{align}
\int 2x\cdot \sin (x^{2}+3)dx \\
u=x^{2}+3 \\
du=2xdx \\
dx=\frac{du}{2x} \\
\int2x\cdot \sin u\frac{du}{2x} \\
\int \sin (u) du=-\cos u+c=-\cos(x^{2}+3)+c
\end{align}
$$
$$
\begin{align}
\int \frac{2x}{\sqrt{ x^{2}-2 }}dx=2\sqrt{ x^{2}-2 }+c \\
u=2x^{2}-2 \\
dx=\frac{du}{2x} \\
\int \frac{2xdu}{\sqrt{ u }2x}=\int u^{-1/2}du=2\sqrt{ u }=2\sqrt{ x^{2}-2 }+c
\end{align}
$$
$$
\begin{align}
\int x^{2}\cdot \sqrt{ x^{3}-1 }dx=\frac{1}{3}\int 3x^{2}\sqrt{ x^{3}-1 }dx= \frac{2(x^{3}-1)^{3/2}}{9} +c \\ \\

\int \sin 3xdx=\frac{1}{3}\int3\sin3xdx=\boxed{-\frac{1}{3}\cos(3x) +c}  \\
\int \sqrt{ 1+3x }dx=\frac{1}{3}\int 3\sqrt{ 1+3x }dx=\boxed{\frac{2}{9}(1+3x)^{3/2}+c}  \\
\int \frac{1}{\sqrt{ x-3 }}dx=\boxed{2\sqrt{ x-3 }+c} 
\end{align}
$$
$$
\begin{align}
\int e^{-3x}dx=-\frac{1}{3}e^{-3x}+c \\
\int \frac{1}{x+3}dx=\ln|x+3|+c \\
\int \tan x dx= \int \sin x(\cos x)^{-1}dx=\int \sin x(u)^{-1}\frac{du}{-\sin x}=-\ln|u|=-\ln|\cos x|+c
\end{align}
$$---
$$
\begin{align}
\int xe^xdx = xe^x-\int e^xdx=xe^x-e^x+c \\
u'=e^x\quad u=e^x \\
v=x \quad v'=1 \\
 \\
\int x\sin xdx=-x\cos x-\int -\cos xdx=\sin x-x\cos x+c \\
\end{align}
$$

---
$$
\begin{align}
\int(x^{2}+7x-5)\cos xdx=\sin x(x^{2}+7x-5)-\int 2x\sin xdx-\int7\sin xdx= \\
=(x^{2}+7x-5)\sin x+7\cos x+2x\cos x+2\sin x=(x^{2}+7x-7)\sin x+(2x+7)\cos x+c \\
 \\
\int x^{3}\cos xdx=x^{3}\sin x-\int 3x^{2}\sin xdx=x^{3}\sin x+3x^{2}\cos x-\int 6x\cos xdx= \\
=x^{3}\sin x+3x^{2}\cos x-6x\sin x+\int6\sin xdx=x^{3}\sin x+3x^{2}\cos x-6x\sin x-6\cos x= \\
=\boxed{(x^{3}-6x)\sin x+(3x^{2}-6)\cos x+c}
\end{align}
$$

---
$$
\begin{align}
\int \sin x \cos ^{3}xdx \\
u'=\sin x \\
u=-\cos x \\
v=\cos ^{3}x \\
v'=-3\cos ^{2}x\cdot \sin x \\
 \\
- \cos ^{4} x-3\int\cos ^{3} x\sin xdx=\int \cos ^{3}x\sin xdx \\
-\cos^4x=4\int \cos ^{3}x\sin xdx \\
c-\frac{\cos^4x}{4}=\int \cos ^{3}x\sin xdx
\end{align}
$$
---
$$
\begin{align}
\int (3x^{2}+4x-3)\sin xdx=-(3x^{2}+4x-3)\cos x+\int(6x+4)\cos xdx= \\
=-(3x^{2}+4x-3)\cos x+(6x+4)\sin x-\int6\sin xdx= \\
=\boxed{-(3x^{2}+4x-3)\cos x+(6x+4)\sin x+6\cos x+c} 
\end{align}
$$
---
$$
\begin{align}
\int(5x-2)\sqrt[3]{ 5x^{2}-4x }dx=\frac{1}{2}\int  u^{1/3}du=-\frac{3(5x^{2}-4x)^{4/3}}{4}+c \\
\int \frac{e^x}{e^x+1}dx=\int \frac{1}{u}du
=\ln|e^x+1|+c\end{align}
$$
---
$$
\begin{align}
\int_{-1}^2 3x^{2}dx=[x^{3}]_{-1}^2=2^3-(-1)^3=9 \\
\int_{1}^2(x^{2}-3x+2)dx=\left[ \frac{x^{3}}{3}-\frac{3x^{2}}{2}+2x \right]_{1}^2=-\frac{1}{6} \\
\int_{1}^34x^{3}dx=[x^4]_{1}^3=80 \\
\int_{0}^{2\pi}(1-\cos x)dx=[x-\sin x]_{0}^{2\pi}=(2\pi-0)-(0-0)=2\pi \\
 \\
\int_{1}^2\frac{x+1}{x}dx=[x+\ln|x|]_{1}^2\approx1.69 \\
\int_{0}^4 \frac{1}{x}dx=\emptyset \\
\int_{1}^4\sqrt{ x }(1+2\sqrt{ x })=\int_{1}^4 (\sqrt{ x }+2x)dx=\left[ \frac{2x^{3/2}}{3}+x^{2} \right]_{1}^4=\frac{59}{3} \\
 \\
\int_{1}^e \frac{\ln x}{x}dx=[\ln x\cdot \ln|x|]_{1}^e-\int_{1}^e\frac{\ln x}{x}dx=\frac{[\ln x\cdot \ln |x|]_{1}^e}{2}=0.5 \\
\int_{0}^{\pi/2} e^{\cos x}\sin xdx\dots -\int e^u du=-e^{\cos x}+c\dots[-e^{\cos x}]_{0}^{\pi/2}=e-1
\end{align}
$$
---

## Obsah rovinného obrazce
![](../../Images/Pasted%20image%2020260401111705.png)

$$
\begin{align}
f(x)=x^{2}+1
\end{align}
$$