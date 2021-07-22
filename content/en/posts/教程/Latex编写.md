---
title: "Latex编写指南"
date: 2021-04-10T10:37:48+08:00
draft: False
categories:
    - work
    - paper
tags:
    - latex
---


## Trick

### 引用子图片

[https://wenda.latexstudio.net/q-1405.html]

使用**subfig**宏包的办法：

```latex
\documentclass[journal]{IEEEtran}
\usepackage{graphicx}

\usepackage{subfig}
\captionsetup[subfigure]{labelformat=simple}
\renewcommand\thesubfigure{(\alph{subfigure})}

\usepackage{hyperref}
\newcommand{\subfigureautorefname}{Fig.} % the name is sub-figure-auto-ref-name

\usepackage{mwe}  % for use of sample images
\begin{document}
\begin{figure}[!t]
    \centering
    \subfloat[]{\includegraphics[width=2.5in]{example-image-a}\label{A}}
    \\
    \subfloat[]{\includegraphics[width=2.5in]{example-image-b}\label{B}}
    \caption{LETTER }
    \label{LETTER}
\end{figure}  

The letter A is shown in \autoref{A}
\end{document}
```

使用**subcaption**宏包：

```latex
\documentclass[journal]{IEEEtran}
\usepackage{graphicx}

% ref: https://tex.stackexchange.com/a/512010
\usepackage{subcaption}
\renewcommand\thesubfigure{(\alph{subfigure})}
\captionsetup[sub]{labelformat=simple}

\usepackage{hyperref}
\renewcommand{\figureautorefname}{Fig.}

\usepackage{mwe}  % for use of sample images
\begin{document}
\begin{figure}[!t]
 \centering
 \subfloat[]{\includegraphics[width=2.5in]{example-image-a}\label{A}}
 \\
 \subfloat[]{\includegraphics[width=2.5in]{example-image-b}\label{B}}
 \caption{LETTER }
 \label{LETTER}
\end{figure}  

The letter A is shown in \autoref{A}
\end{document}
```



