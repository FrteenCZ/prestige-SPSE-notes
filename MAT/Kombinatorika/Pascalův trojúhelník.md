#MAT #MAT/Kombinatorika 

číslo je rovný součtu dvou čísel nad ním
$$
\begin{gathered}
0 &&&&&&&1&&&&&&\\
1 &&&&&&1&&1&&&&&\\
2 &&&&&1&&2&&1&&&&\\
3 &&&&1&&3&&3&&1&&&\\
4 &&&1&&4&&6&&4&&1&&\\
5 &&1&&5&&10&&10&&5&&1&\\
6 &1&&6&&15&&20&&15&&6&&1\\
\vdots & \vdots&&\vdots&&\vdots&&\vdots&&\vdots&&\vdots&&\vdots
\end{gathered}
$$

pomocí [kombinací](Combination)
$$
\begin{gathered}
0 &&&&&&&\begin{pmatrix}
0 \\
0
\end{pmatrix}&&&&&&\\
1 &&&&&&\begin{pmatrix}
1 \\
0
\end{pmatrix}&&\begin{pmatrix}
1 \\
1
\end{pmatrix}&&&&&\\
2 &&&&&\begin{pmatrix}
2 \\
0
\end{pmatrix}&&\begin{pmatrix}
2 \\
1
\end{pmatrix}&&\begin{pmatrix}
2 \\
2
\end{pmatrix}&&&&\\
3 &&&&\begin{pmatrix}
3 \\
0
\end{pmatrix}&&\begin{pmatrix}
3 \\
1
\end{pmatrix}&&\begin{pmatrix}
3 \\
2
\end{pmatrix}&&\begin{pmatrix}
3 \\
3
\end{pmatrix}&&&\\
4 &&&\begin{pmatrix}
4 \\
0
\end{pmatrix}&&\begin{pmatrix}
4 \\
1
\end{pmatrix}&&\begin{pmatrix}
4 \\
2
\end{pmatrix}&&\begin{pmatrix}
4 \\
3
\end{pmatrix}&&\begin{pmatrix}
4 \\
4
\end{pmatrix}&&\\
5 &&\begin{pmatrix}
5 \\
0
\end{pmatrix}&&\begin{pmatrix}
5 \\
1
\end{pmatrix}&&\begin{pmatrix}
5 \\
2
\end{pmatrix}&&\begin{pmatrix}
5 \\
3
\end{pmatrix}&&\begin{pmatrix}
5 \\
4
\end{pmatrix}&&\begin{pmatrix}
5 \\
5
\end{pmatrix}&\\
6 &\begin{pmatrix}
6 \\
0
\end{pmatrix}&&\begin{pmatrix}
6 \\
1
\end{pmatrix}&&\begin{pmatrix}
6 \\
2
\end{pmatrix}&&\begin{pmatrix}
6 \\
3
\end{pmatrix}&&\begin{pmatrix}
6 \\
4
\end{pmatrix}&&\begin{pmatrix}
6 \\
5
\end{pmatrix}&&\begin{pmatrix}
6 \\
6
\end{pmatrix}\\
\vdots & \vdots&&\vdots&&\vdots&&\vdots&&\vdots&&\vdots&&\vdots
\end{gathered}
$$
