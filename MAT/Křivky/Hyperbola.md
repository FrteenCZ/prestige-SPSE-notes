#MAT #MAT/Křivky
![[Pasted image 20250516100756.png]]


- $a$ – hlavní poloosa
- $b$ – vedlejší poloosa
- $c = e$ – excentricita (výstřednost)

- **Vztah mezi poloosami a excentricitou:**
$$
e^2 = a^2 + b^2
$$

---

# 🧾 Rovnice hyperboly

## Se středem v počátku $(S = [0, 0])$:

- **hlavní osa $x$**:
  $$
  H: \frac{x^2}{a^2} - \frac{y^2}{b^2} = 1
  $$

- **hlavní osa $y$**:
  $$
  H: -\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1
  $$

## Se středem v bodě $S = [m, n]$:

- **hlavní osa $x$**:
  $$
  H: \frac{(x - m)^2}{a^2} - \frac{(y - n)^2}{b^2} = 1
  $$

- **hlavní osa $y$**:
  $$
  H: -\frac{(x - m)^2}{a^2} + \frac{(y - n)^2}{b^2} = 1
  $$

---

# 📌 Příklad

Zadaná obecná rovnice:
$$
9x^2 - 90x - 16y^2 - 64y + 17 = 0
$$

## 📚 Postup:

1. Úprava pomocí doplnění na čtverec:
   $$
   9(x^2 - 10x) - 16(y^2 + 4y) + 17 = 0
   $$
   $$
   9(x - 5)^2 - 225 - 16(y + 2)^2 + 64 + 17 = 0
   $$

2. Úprava do kanonického tvaru:
   $$
   9(x - 5)^2 - 16(y + 2)^2 = 144
   $$
   $$
   \frac{(x - 5)^2}{16} - \frac{(y + 2)^2}{9} = 1
   $$

## 📌 Výsledek:
- Střed: $S = [5, -2]$
- $a = 4$
- $b = 3$
- $e = 5$ (protože $e^2 = 4^2 + 3^2 = 25$)

# asymptoty
$$y=\pm\frac{b}{a}x$$
# vzájemná poloha s přímkou
- kvadratická rovnice
	- D = 0 - tečna
	- D > 0 - sečna
	- D < 0 - vnější přímka

---
$$
\begin{align}
H:3x^{2}-6x-y^{2}+4y=4 \\
H:3(x^{2}-2x)-(y^{2}-4y)=4 \\
H:3((x-1)^{2}-1)-((y-2)^{2}-4)=4 \\
H:3(x-1)^{2}-3-(y-2)^{2}+4=4 \\
H:3(x-1)^{2}-(y-2)^{2}=3 \\
H:(x-1)^{2}-\frac{(y-2)^{2}}{3}=1
\end{align}
$$