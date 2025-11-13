#MAT #MAT/Příklady
# 1. Napište obecnou a parametrickou rovnici přímky, která prochází průsečíkem přímek $p:2x+y=4, ~q:2x+3y= - 5$, a dále:
## je kolmá k přímce $r:4x - 5y=20$
$$
\begin{align}
2x+y=4 \\
2x+3y=-5 \\
 \\
2y=-9 \\
y=-4.5 \\
x=4.25 \\
P=[4.25,-4.5] \\ \\

\vec{n}=(5,4)  \\
\vec{s}=(4,-5)\\
\boxed{\begin{matrix}
s:&5x+4y-3.25=0 \\
s:&\begin{matrix}
x=&4.25+4t \\
y=&-4.5-5t
\end{matrix}
\end{matrix}}
\end{align}
$$
## je rovnoběžná s přímkou $r$.
$$
\begin{align} 
\vec{n}=(4,-5) \\
\vec{s}=(5,4) \\
\boxed{\begin{matrix}
s:&4x-5y-39.5=0 \\
s:&\begin{matrix}
x=&4.25+5t \\
y=&-4.5+4t
\end{matrix}
\end{matrix}}
\end{align}
$$

# 2. Jsou dány body $A [3;2],~B [-1;-1]$. Určete souřadnice bodu $C$, je-li $\vec{BC}=(12,-5)$. Dokažte, že body $A,~B,~C$ jsou vrcholy trojúhelníku. Napište parametrické i obecné rovnice přímek, na nichž leží :
$$
\begin{align}
C=B+\vec{BC} \\
\boxed{C=[11,-6]} \\
\vec{AB}=(-4,-3) \\
\vec{BC}=(12,-5) \\
\vec{CA}=(8,-8) \\
\end{align}
$$
## strany trojúhelníku,
$$
\begin{align}
\boxed{\begin{matrix}
a:&5x+12y+17=0 \\
a:&\begin{matrix}
x=&-1+12t \\
y=&-1-5t
\end{matrix}
\end{matrix}} \\
\boxed{\begin{matrix}
b:&x+y-5=0 \\
b:&\begin{matrix}
x=&3+8t \\
y=&2-8t
\end{matrix}
\end{matrix}} \\
\boxed{\begin{matrix}
c:&3x-4y-1=0 \\
c:&\begin{matrix}
x=&-1-4t \\
y=&-1-3t
\end{matrix}
\end{matrix}}
\end{align}
$$
## výšky trojúhelníku,
$$
\begin{align} 
\boxed{\begin{matrix}
v_a:&12x-5y-26=0 \\
v_a:&\begin{matrix}
x=&3+5t \\
y=&2+12t
\end{matrix}
\end{matrix}} \\
\boxed{\begin{matrix}
v_b:&x-y=0 \\
v_b:&\begin{matrix}
x=&-1+8t \\
y=&-1+8t
\end{matrix}
\end{matrix}} \\
\boxed{\begin{matrix}
v_c:&4x+3y-26=0 \\
v_c:&\begin{matrix}
x=&11+3t \\
y=&-6-4t
\end{matrix}
\end{matrix}}
\end{align}
$$
## těžnice,
$$
\begin{align} 
S_{a}=[5,-3.5] \\
\vec{t_{a}}=(-2,5.5) \\
\boxed{\begin{matrix}
t_a:&5.5x+2y-20.5=0 \\
t_a:&\begin{matrix}
x=&5-2t \\
y=&-3.5+5.5t
\end{matrix}
\end{matrix}} \\

S_{b}=[7, -2] \\
\vec{t_{b}}=(-8, 1) \\
\boxed{\begin{matrix}
t_b:&x+8y+9=0 \\
t_b:&\begin{matrix}
x=&7-8t \\
y=&-2+t
\end{matrix}
\end{matrix}}  \\

S_{c}=[1, 0.5]  \\
\vec{t_{c}}=(10, -6.5)\\
\boxed{\begin{matrix}
t_c:&6.5x+10y-11.5=0 \\
t_c:&\begin{matrix}
x=&1+10t \\
y=&0.5-6.5t
\end{matrix}
\end{matrix}}
\end{align}
$$
## osy stran trojúhelníku.
$$
\begin{align} 
&\boxed{\begin{matrix}
o_a:&12x-5y-77.5=0 \\
o_a:&\begin{matrix}
x=&5+5t \\
y=&-3.5+12t
\end{matrix}
\end{matrix}}  \\

&\boxed{\begin{matrix}
o_b:&x-y-9=0 \\
o_b:&\begin{matrix}
x=&7+8t \\
y=&-2+8t
\end{matrix}
\end{matrix}}\begin{matrix}
\leftarrow \text{tohle maj taky blbě} \\
 \\
 \\
\end{matrix} \\

&\boxed{\begin{matrix}
o_c:&4x+3y-5.5=0 \\
o_c:&\begin{matrix}
x=&1+3t \\
y=&0.5-4t
\end{matrix}
\end{matrix}}
\end{align}
$$

## Dále určete vnitřní úhly trojúhelníku $ABC$ a souřadnice těžiště.
$$
\begin{align}
\vec{b}=\left(-8,8\right) \\
\vec{c}=\left(4,3\right) \\
\alpha=\arccos\left( \frac{\vec{b}\cdot \vec{c}}{||\vec{b}||\cdot||\vec{c}||} \right) \\
\alpha=\arccos\left( \frac{-32+24}{\sqrt{ 128 }\cdot \sqrt{ 25 }} \right) \\
\alpha=\arccos\left( \frac{-8}{8\sqrt{ 2 }\cdot5} \right) \\
\boxed{\alpha=98.1301023542° } \\
 \\
\vec{a}=\left(12,-5\right) \\
\vec{c}=\left(4,3\right) \\
\beta=\arccos\left( \frac{\vec{a}\cdot \vec{c}}{||\vec{a}||\cdot||\vec{c}||} \right) \\
\boxed{\beta=59.4897625939° } \\
 \\
\vec{a}=\left(-12,5\right) \\
\vec{b}=\left(-8,8\right) \\
\gamma=\arccos\left( \frac{\vec{a}\cdot \vec{b}}{||\vec{a}||\cdot||\vec{b}||} \right) \\
\boxed{\gamma=22.380135052° } \\
 \\
S_{a}=[5,-3.5] \\
\vec{t_{a}}=(-2,5.5) \\
T=S_{a}+\frac{1}{3}t_{a} \\
\boxed{T=[\frac{13}{3}, -\frac{5}{3}]}
\end{align}
$$


# 3. Jsou dány body $K  [1;3  ],~L  [5; - 2  ]$. Napište rovnici přímky $KL$ ve všech tvarech, které znáte. Vypočtěte souřadnice průsečíků přímky s osami soustavy souřadnic. Určete směrnici přímky a její směrový úhel.
$$
\begin{align}
\vec{s}=\left(-4,5\right) \\
\boxed{KL:\begin{matrix}
x=1-4t \\
y=3+5t
\end{matrix}} \\
\vec{n}=(5,4) \\
\boxed{KL:5x+4y-17=0} \\
\boxed{KL:y=-\frac{5}{4}x+\frac{17}{4}} \\
\boxed{\begin{matrix}
P_{y}=\left[ 0, \frac{17}{4} \right] \\
P_{x}=\left[ \frac{17}{5},0 \right]
\end{matrix}} \\
\boxed{\text{směrnice}=-\frac{5}{4}} \\
\tan(\alpha)=-\frac{5}{4} \\
\boxed{\text{směrový úhel}=\arctan\left( -\frac{5}{4} \right)\approx-51.3401917459°}
\end{align}
$$
  

# 4. Napište rovnici strany $a$, výšky $v_a$ a těžnice $t_a$ trojúhelníku $ABC$, kde $A  [2;4  ],B  [ - 1;3  ],C  [1;0 ]$.

$$
\begin{align}
\vec{a}=(-2,3) \\
\boxed{a:3x+2y-3=0} \\
\vec{v_{a}}=(3,2) \\
\boxed{v_{a}:-2x+3y-8=0} \\
S_{a}=[0,1.5] \\
\vec{t_{a}}=(2,2.5) \\
\boxed{t_{a}:2.5x-2y+3=0}
\end{align}
$$

# 5. Napište rovnice stran a těžnic trojúhelníku $KLM$: $K  [1;4; - 7 ],L [ - 5; - 2;1 ],M [7; - 6;3 ]$.  
$$
\begin{align} 
\vec{k}=\left(-12,4,-2\right) \\
\vec{l}=(-6,10,-10) \\
\vec{m}=(6,6,-8) \\
\boxed{\begin{matrix}
k:&\begin{pmatrix}
x=&7-12t \\
y=&-6+4t \\
z=&3-2t
\end{pmatrix} \\ \\

l:&\begin{pmatrix}
x=&7-6s \\
y=&-6+10s \\
z=&3-10s
\end{pmatrix} \\ \\

m:&\begin{pmatrix}
x=&1+6r \\
y=&4+6r \\
z=&-7-8r
\end{pmatrix}
\end{matrix}}\\ \\

S_{k}=\left(1,-4,2\right) \\
S_{l}=\left(4,-1,-2\right) \\
S_{m}=\left(-2,1,-3\right) \\
\vec{t_k}= \left(0,-8,9\right)\\
\vec{t_l}= \left(9,1,-3\right)\\
\vec{t_m}= \left(-9,7,-6\right)\\
\boxed{\begin{matrix}
t_k:&\begin{pmatrix}
x=&1 \\
y=&-4-8t \\
z=&2+9t
\end{pmatrix} \\ \\

t_l:&\begin{pmatrix}
x=&4+9s \\
y=&-1+s \\
z=&2-3s
\end{pmatrix} \\ \\

t_m:&\begin{pmatrix}
x=&-2-9r \\
y=&1+7r \\
z=&-3-6r
\end{pmatrix}
\end{matrix}}
\end{align}
$$
  

# 6. Napište rovnici přímky $q$, která prochází bodem $M [ - 4;6; - 15 ]$ a je rovnoběžná s přímkou $p:x= - 1 - t;y=5 - 2t;z= - 7+5t$. Jaká je poloha přímky $q$ vzhledem k ose $x$?

$$
\begin{align}
\vec{p}=(-1,-2,5) \\
\boxed{Q:\begin{matrix}
x=&-4-s \\
y=&6-2s \\
z=&-15+5t
\end{matrix}} \\
 \\
y=0 \\
0=6-2s \\
s=3 \\
x=-7 \\
z=0\implies\boxed{\text{různoběžné}} \\
\boxed{P_{x}=[-7,0,0]}
\end{align}
$$  

# 7. Určete vzájemnou polohu přímek a u různoběžných přímek určete jejich společný bod:

## 1. $AB$, $CD$ jestliže: $A [0;0;2],~B[3;2;5 ];~C  [4;1;5  ];~D  [0;4;2  ]$
$$
\begin{align}
\vec{AB}=(3,2,3) \\
\vec{CD}=(-4, 3, -3) \\
AB:\begin{pmatrix}
x=&3t \\
y=&2t \\
z=&2+3t
\end{pmatrix} \\
CD:\begin{pmatrix}
x=&4-4r \\
y=&1+3r \\
z=&5-3r
\end{pmatrix} \\
3t=4-4r \\
2t=1+3r \\
2+3t=5-3r \\
 \\
3t=3-3r \\
 \\
3-3r=4-4r \\
r=1 \\
t=0 \\
 \\
2\cdot 0\neq1+3\cdot 1 \implies \boxed{\text{mimoběžný}}
\end{align}
$$
## 2. KL, MN jestliže  $K[3;1;6  ],~L  [4;0;8  ];~M  [1;5;7  ];~N  [0;8;10 ]$.
$$
\begin{align}
\vec{KL}=(1,-1,2) \\
\vec{MN}=(-1,3,3) \\
KL:\begin{pmatrix}
x=&3+1t \\
y=&1-1t \\
z=&6+2t
\end{pmatrix} \\
MN:\begin{pmatrix}
x=&1-1r \\
y=&5+3r \\
z=&7+3r
\end{pmatrix} \\
3+t=1-r \\
1-t=5+3r \\
6+2t=7+3r \\
 \\
t=-4-3r \\
 \\
3-4-3r=1-r \\
r=-1 \\
t=-1 \\
 \\
6-2=7-3 \implies \boxed{\text{různoběžný}} \\
P=[3+t,1-t,6+2t] \\
P=[3-1, 1+1, 6-2] \\
\boxed{P=[2,2,4]}
\end{align}
$$
## 3. $p:x=2+4t,~y=3 - t,~z= - 1+t$; $q:x= - 2+12r,~y=4 - 3r,~z= - 2+3r$
$$
\begin{align}
\vec{p}=(4,-1,1) \\
\vec{q}=(12,-3,3) \\
\vec{p}=\frac{1}{3}\vec{q}\implies\boxed{robnoběžný} \\
 \\
x=0 \\
t=-0.5 \\
r=\frac{1}{6} \\
\begin{matrix}
P=[0,3.5,-1.5] \\
Q=[0,3.5,-1.5]
\end{matrix}\implies\boxed{splývající}
\end{align}
$$
## 4. $a:x=1+3t,y=2 - t,z=t;$ $b:x=1 - 6r,y=2+2r,z=3 - 2r$
$$
\begin{align}
\vec{a}=(3,-1,1) \\
\vec{b}=(-6,2,-2) \\
\vec{a}=-\frac{1}{2}\vec{b}\implies\boxed{robnoběžný} \\
 \\
x=0 \\
t=-\frac{1}{3} \\
r=\frac{1}{6} \\
\begin{matrix}
P=\left[ 0, \frac{7}{3}, -\frac{1}{3} \right] \\
Q=\left[ 0, \frac{7}{3}, \frac{8}{3} \right]
\end{matrix}\implies\boxed{různé}
\end{align}
$$
  

# 8. Napište parametrické vyjádření přímky $q$, která prochází bodem $Q [4;6; - 15 ]$ a je rovnoběžná s přímkou $p:\begin{matrix}x=&1+t\\y=&5 - 2t\\z=& - 7+5t\end{matrix}$.
$$
\begin{align}
\vec{p}=(1,-2,5) \\
\boxed{q:\begin{matrix}
x=&4+s \\
y=&6-2s \\
z=&-15+5s
\end{matrix}}
\end{align}
$$
