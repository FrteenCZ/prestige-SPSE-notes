#MAT #MAT/Příklady 
# 1. Vypočti obsah trojúhelníku ABC, jehož dvě strany tvoří vektory $\vec{a}=(1,1,-2), \vec{b}=(-1,2,-1)$. Urči vektor, který tvoří třetí stranu.
$$
\begin{align}
S=\frac{||\vec{a}\times \vec{b}||}{2} \\

S=\frac{||(3,3,3)||}{2} \\
\boxed{S=\frac{3\sqrt{ 3 }}{2}} \\
 \\
\vec{c}=\vec{a}-\vec{b} \\
\boxed{\vec{c}=(2,-1,-1)}
\end{align}
$$


# 2. Jsou dány body $A[-2,1],~B[-4,2],~C[-3,-1]$. Dokažte, že body $A,~B,~C$ jsou vrcholy trojúhelníku. Vypočtěte velikost strany $AB$. Vypočtěte velikost úhlu $\gamma$.
$$
\begin{align} \\
\vec{CA}=(-1,-2) \\
\vec{CB}=(1,-3)\\
\gamma=\arccos\left( \frac{\vec{CA}\cdot \vec{CB}}{|CA|\cdot|CB|} \right) \\
\gamma=\arccos\left( \frac{5}{\sqrt{ 5 }\cdot \sqrt{ 10 }} \right) \\
\gamma=\arccos\left( \frac{\sqrt{ 2 }}{2} \right) \\
\boxed{\gamma=\frac{\pi}{4}} ~\text{takže je trojúhelník}
\end{align}
$$

  

# 3. Body $A[3,6,0],~B[1,4,5],~C[5,2,7]$ tvoří vrcholy trojúhelníku. Vypočtěte velikost těžnice $t_{a}$ a obsah trojúhelníku.
$$
\begin{align}
S_{a}=[3,3,6] \\
t_{a}=||(0,3,-6)|| \\
\boxed{t_{a}=3\sqrt{ 5 }} \\ \\

\vec{a}=(4,-2,2) \\
\vec{b}=(2,-4,7)\\
S=\frac{\vec{a}\times \vec{b}}{2} \\
S=\frac{||(-6,-24,-12)||}{2} \\
S=\frac{\sqrt{ 36+576+144 }}{2} \\
S=\frac{\sqrt{ 756 }}{2} \\
S=3\sqrt{ 21 } \\
\boxed{S\approx13.75}
\end{align}
$$
  
# 4. Body $A[-2,1],~B[1,3],~C[-2,-4]$ tvoří vrcholy trojúhelníku. Určete souřadnice těžiště tohoto trojúhelníku.

$$
\begin{align}
S_{a}= [-0.5, -0.5]\\
t_{a}=(-1.5,1.5) \\
\frac{1}{3}t_{a}=( -0.5,0.5) \\
T=S_{a}+\frac{1}{3}t_{a} \\
\boxed{T=\left[ -1,0 \right]} \\
\end{align}
$$

# 5. Vypočtěte velikost úhlu, který svírá těžnice $t_{c}$ se stranou $a$ v trojúhelníku $ABC$, je-li $A[1 ;-5 ; 5], B[3 ; 1 ; 1], C[5 ;-3 ; 3]$.
$$
\begin{align} 
S_{c}=[2,-2,3] \\
t_{c}=(3,-1,0) \\
a=(2,-4,2) \\
\theta = \arccos\left( \frac{t_{c} \cdot a}{||t_{a}||\cdot||a||} \right) \\
\theta=\arccos \left( \frac{10}{\sqrt{ 10 }\cdot\sqrt{ 24 }} \right)  \\
\theta=\arccos\left(\frac{\sqrt{ 15 }}{6} \right)\\
\boxed{\theta=\pu{0.869122203007  rad } = 49.7970341134°}
\end{align}
$$

  

# 6. V trojúhelníku $ABC$ je $A[3,2],~B[-1,-1]$, souřadnice vektoru $\vec{a}=\vec{BC}=(12,-5)$. Určete souřadnice bodu $C$ a vypočtěte velikosti stran a úhlů tohoto trojúhelníku.  
$$
\begin{align}
C=B+\vec{a} \\
\boxed{C=[11,-6]}
\end{align}
$$

  

# 7. Je dán vektor $\vec{a}=(3,5)$. Určete vektor $\vec{d}$, který je kolmý k vektoru $\vec{a}$ a velikost vektoru $|\vec{d}|=2\sqrt{ 17 }$.
$$
\begin{align}
\vec{n}=(-5,3) \\
||\vec{n}||=\sqrt{ 2 }\cdot \sqrt{ 17 } \\
\vec{d}=\sqrt{ 2}\cdot \vec{n} \\
\boxed{\vec{d}=(-5\sqrt{ 2 },3\sqrt{ 2 })}
\end{align}
$$