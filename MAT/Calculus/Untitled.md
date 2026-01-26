# Vlastní limita v nevlastním bodě
```tikz
\begin{document}
\begin{tikzpicture}[scale=2]
    % Oříznutí, aby graf nepřetékal přes osy
    \clip (-3.5, -4.5) rectangle (3.5, 4.5);

    % Mřížka
    \draw[very thin, gray!20] (-3,-4) grid (3,4);

    % Asymptoty (čárkovaně)
    \draw[gray, dashed] (-3,-2) -- (5,-2); % vodorovná y = -2
    \draw[gray, dashed] (1,-5) -- (1,2);   % svislá x = 1

    % Osy
    \draw[->] (-3,0) -- (5,0) node[right] {$x$};
    \draw[->] (0,-5) -- (0,2) node[above] {$y$};

    % Funkce y = 1/(x-1) - 2
    % Levá větev (x < 1)
    \draw[orange, thick, samples=100, domain=-3:0.8] plot (\x, {1/(\x-1) - 2});
    % Pravá větev (x > 1)
    \draw[orange, thick, samples=100, domain=1.2:5] plot (\x, {1/(\x-1) - 2});

    % Popis důležitých bodů
    \node[orange, below left] at (0,-3) {$[0, -3]$};
    \filldraw[orange] (0,-3) circle (1.5pt);
\end{tikzpicture}
\end{document}
```
# Nevlastní v nevlastním bodě
```tikz
\begin{document}
\begin{tikzpicture}[scale=1.2]
    % Mřížka
    \draw[very thin, gray!20] (-5,-1) grid (5,5);

    % Osy
    \draw[->] (-5.2,0) -- (5.2,0) node[right] {$x$};
    \draw[->] (0,-0.5) -- (0,5.5) node[above] {$y$};

    % Funkce y = 0.2 * x^2
    % Doména od -5 do 5 (v -5 a 5 je y = 5)
    \draw[purple, thick, samples=100, domain=-5:5] plot (\x, {0.2 * \x^2});

    % Významné body pro kontrolu
    \filldraw[purple] (0,0) circle (1.5pt) node[below left, black, font=\scriptsize] {0};
    \filldraw[purple] (5,5) circle (1.5pt) node[right, black, font=\scriptsize] {[5, 5]};
    \filldraw[purple] (-5,5) circle (1.5pt) node[left, black, font=\scriptsize] {[-5, 5]};

    % Popisek funkce
    \node[purple, above] at (2.5, 1.25) {$y = 0.2x^2$};
\end{tikzpicture}
\end{document}
```

