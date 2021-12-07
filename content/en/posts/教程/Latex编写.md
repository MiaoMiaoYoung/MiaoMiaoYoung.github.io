---
title: "Latex编写指南"
date: 2021-04-10T10:37:48+08:00
draft: False
categories:
    - 教程
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






## ERROR

### IEEE Template Xlatex 字体警告

最开始没发现这个问题，论文初稿也是这么提交的。结果文章中了之后在提交Camera Ready的时候感觉模板中的标题和自己文章的标题总感觉不是一个字体，这才发现了这个警告：

```
Font shape `TU/ptm/b/it' undefined (Font)	using `TU/ptm/bx/it' instead.
```

原因是xelatex缺少了某些字体，导致编译后的文章出现了字体错误

网上的解决办法大多是使用pdflatex，但是这里因为字符编码原因没办法使用pdflatex

然后找到了原因和解决办法，上述报错的这个字体是pdflatex中独有的，所以换成xelatex的就可以了，使用库：

'''
\usepackage[OT1]{fontenc}
'''

> https://tex.stackexchange.com/questions/358261/latex-font-warning-after-updating-to-texlive-2016

