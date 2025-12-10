#MAT #MAT/Pravděpodobnosti 
- získávání statických údajů
- jejich zpracování - třídění, výpočet charakteristik
- hodnocení


- **Statistický soubor** 
	- množina všech objektů statistického pozorování
	- skládá se ze **statistických jednotek**
	- u každé jednotky vyřešujeme jeden nebo více **znaků**
		- **Kvantitativní znaky** - *int* / *float* (výška, počet)
		- **Kvalitativní znaky** - *string* (povolání, značka auta)
			- **Alternativní** - *bool* (ano/ne)

$$
\begin{align}
\text{četnost znaku}&& n&=\sum_{i=1}^{r}n_{i} \\
\text{relativní četnost} && v_{i}&=\frac{n_{i}}{n}
\end{align}
$$
# Charakteristiky
## Aritmetický průměr
$$
\overline{x}=\frac{1}{n}\sum _{i=1}^n x_{i}
$$
$n$ - počet znaků
$x$ - znaky
## Vážený průměr
$$
 \overline{x}=\frac{1}{n}\sum_{i=1}^nx_{i}\cdot y_{i}
$$
$n$ - počet znaků
$x$ - znaky
$y$ - váhy

## Geometrický průměr
$$
\overline{Z}_{G}= \left( \prod_{i=1}^nZ_{i} \right)^n
$$
$Z$ - růst

## Modus `mod(x)`
- hodnota x s nejvyšší četností

## Medián `med(x)`
- prostřední hodnota

## Rozptyl
$$
\begin{align}
s_{x}^2=\frac{1}{n}\sum_{i=1}^n(x_{i}-\overline{x})^{2} && s_{x}^{2}=\frac{1}{n}\sum_{i=1}^n(x_{i}-\overline{x})^{2}\cdot y_{i}
\end{align}
$$
## Směrodatná odchylka
$$
s_{x}=\sqrt{ \frac{1}{n}\sum_{i=1}^n(x_{i}-\overline{x})^{2} }
$$
## Variační koeficient
$$
v_{x}=\frac{s_{x}}{\over{x}}
$$---
