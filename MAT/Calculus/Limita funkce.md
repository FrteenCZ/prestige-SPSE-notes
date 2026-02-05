#MAT #MAT/Calc
`Vlastní bod` = $x \in \mathbb{R}$
``Nevlastní bod`` = $x=\infty,-\infty$
`Nevlastní limita` - výsledek limity je $\infty,-\infty$
[Nevlastní bod](Nevlastní%20bod.md)

# Vlastní limita ve vlastním bodě
Funkce $f$ má v bodě $a$ limitu $L$, jestliže libovolnému **okolí bodu $L$** existuje **okolí bodu $a$** tak, že pro všechna $x \neq a$ z tohoto okolí patří funkční hodnoty do zvoleného okolí $L$.
$$
f(x)=\frac{x^{2}-2x}{x-2}
$$
v bodě $x=2$ není definovaná a není spojitá
ale limita jde vypočítat
$$
\lim_{ x \to 2 }f(x)=2 
$$
pokud se nepřibližuje k jedné hodnotě zdola a z hora (zleva a zprava) limita není definována
$$
\lim_{ x \to 0 }sgn(x)= \text{neexistuje}
$$
```tikz
\begin{document}
\begin{tikzpicture}[scale=2]
    % Osy
    \draw[->] (-3.2,0) -- (3.2,0) node[right] {$x$};
    \draw[->] (0,-1.5) -- (0,1.5) node[above] {$sgn(x)$};

    % Mřížka (nepovinné, pro lepší orientaci)
    \draw[very thin, gray!20] (-3,-1) grid (3,1);

    % Popisky na y-ose
    \node[left, font=\scriptsize] at (0,1) {1};
    \node[left, font=\scriptsize] at (0,-1) {-1};

    % Funkce sgn(x)
    \draw[cyan, thick] (0.05,1) -- (3,1);
    \draw[cyan, thick] (-3,-1) -- (-0.05,-1);

    % Body nespojitosti a sgn(0)=0
    \draw[cyan, fill=white] (0,1) circle (2pt);
    \draw[cyan, fill=white] (0,-1) circle (2pt);
    \draw[cyan, fill=cyan] (0,0) circle (2pt);
\end{tikzpicture}
\end{document}
```
# Nevlastní limita ve vlastním bodě
$$
\begin{align}
\lim_{ x \to 0^- }\frac{1}{x} &= -\infty \\
\lim_{ x \to 0^+ }\frac{1}{x} &= \infty \\
\lim_{ x \to 0 }\frac{1}{x} &= \text{neexistuje} 
\end{align}
$$
```tikz
\begin{document}
\begin{tikzpicture}[scale=1.2]
    % Oříznutí, aby graf nepřetékal přes osy
    \clip (-4.5, -4.5) rectangle (5.5, 4.5);

    % Mřížka
    \draw[very thin, gray!20] (-4,-4) grid (4,4);

    % Osy
    \draw[->] (-4.2,0) -- (4.2,0) node[right] {$x$};
    \draw[->] (0,-4.2) -- (0,4.2) node[above] {$y$};

    % Funkce y = x^-2
    % Kreslíme dvě větve odděleně, abychom se vyhnuli nule
    \draw[cyan, thick, samples=100, domain=0.25:4] plot (\x, {1/(\x)});
    \draw[cyan, thick, samples=100, domain=-4:-0.25] plot (\x, {1/(\x)});

    % Popisky
    \node[cyan, right] at (1,1.5) {$y = \frac{1}{x}$};
    \node[below left, font=\scriptsize] at (0,0) {0};
\end{tikzpicture}
\end{document}
```
# Vlastní limita v nevlastním bodě
$$
\begin{align}
\lim_{ x \to \infty } \left( \frac{1}{x-1}-2 \right)=-2 \\
\lim_{ x \to -\infty }\left( \frac{1}{x-1}-2 \right)=-2  
\end{align}
$$
```tikz
\begin{document}
\begin{tikzpicture}[scale=1.2]
    % Oříznutí oblasti viditelnosti
    \clip (-3.5, -5.5) rectangle (5.5, 2.5);

    % Pomocná mřížka
    \draw[very thin, gray!20] (-3,-5) grid (5,2);

    % Asymptoty (čárkovaně)
    \draw[red, thick, dashed] (-3,-2) -- (5,-2); % vodorovná y = -2
    \draw[red, thick, dashed] (1,-5) -- (1,2);   % svislá x = 1

    % Osy
    \draw[->] (-3,0) -- (5,0) node[right] {$x$};
    \draw[->] (0,-5) -- (0,2) node[above] {$y$};

    % Funkce y = 1/(x-1) - 2
    % Levá větev (x < 1)
    \draw[cyan, thick, samples=100, domain=-3:0.8] plot (\x, {1/(\x-1) - 2});
    % Pravá větev (x > 1)
    \draw[cyan, thick, samples=100, domain=1.2:5] plot (\x, {(1/(\x-1)) - 2});

    % Popisky
    \node[below left, font=\scriptsize] at (0,0) {0};
	\node[cyan, right] at (2,-0.5) {$y = \frac{1}{x-1}-2$};
\end{tikzpicture}
\end{document}
```
# Nevlastní v nevlastním bodě
$$
\begin{align}
\lim_{ x \to \infty } 0.2x^{2} &=\infty \\
\lim_{ x \to -\infty }0.2x^{2}&=-\infty  
\end{align}
$$
```tikz
\begin{document}
\begin{tikzpicture}[scale=1.2]
    % Grid and Axes
    \draw[very thin, gray!20] (-5,-1) grid (5,6);
    \draw[->] (-5.2,0) -- (5.2,0) node[right] {$x$};
    \draw[->] (0,-0.5) -- (0,6) node[above] {$y$};

    % The Parabola - explicitly squaring the x
    \draw[cyan, thick, samples=100, domain=-5:5] plot (\x, {0.2 * (\x)^2});


    % Popisky
	\node[cyan, right] at (1,1.5) {$y = 0.2x^2$};
    \node[below left, font=\scriptsize] at (0,0) {0};
\end{tikzpicture}
\end{document}
```
