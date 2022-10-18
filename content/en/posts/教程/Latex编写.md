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

### 旋转图片

```latex
\usepackage{rotating}

\begin{sidewaysfigure}
  \centering
  \includegraphics[width=0.99\textwidth]{./figures.pdf}
  \caption{Caption Here.}
  \label{fig:workflow}
\end{sidewaysfigure}
```

### 表格的大小

1. 调整宽度：设置列间距

```latex
\setlength{\tabcolsep}{7mm}{
    Tabular...
}
```

2. 调整高度：设置行间距

```latex
\begin{table}
    \renewcommand\arraystretch{1.2}
    \begin{tabular}
    \end{tabular}
\end{table}
```

不建议使用，效果不太好，会好多东西挤在一块，字体也会一块缩放

```latex
\begin{adjustbox}{width=.48\textwidth}{
    \begin{tabular}  
    ...
    \end{tabular}  
}
\end{adjustbox}
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

```latex
\usepackage[OT1]{fontenc}
```

> https://tex.stackexchange.com/questions/358261/latex-font-warning-after-updating-to-texlive-2016




### IEEE hyperref 无法链接参考文献

编写Trans.文章的过程中法线，即使添加了hyperref的库，引用仍然是黑色的，并且没有链接

找到原因 <https://blog.csdn.net/nkhgl/article/details/100108833>， 发生在ieeeconf.cls下

解决办法：<https://tex.stackexchange.com/questions/247104/hyperref-doesnt-link-cite-command>

```latex
\makeatletter
\let\NAT@parse\undefined
\makeatother
```

加在\usepackage[colorlinks,citecolor=green]{hyperref}之前





### IEEE 摘要对齐错误

> https://blog.csdn.net/weixin_42998214/article/details/120048716

需要对文本进行两端对齐时：

```latex
\usepackage{ragged2e}
```


在需要对齐的文字前面添加 **\justifying**，如：

```latex
\justifying
\begin{abstract}
...
\end{abstract}
```


### IEEE 引用子图 Fig.1a -> Fig.1(a)

> https://blog.csdn.net/xdzhujy/article/details/120752598

在\begin{document}之前插入以下几句代码：

```latex
\usepackage[labelformat=simple]{subcaption}
\captionsetup[sub]{font=footnotesize}
\captionsetup[figure]{name={Fig.},labelsep=period,font=footnotesize} 
\renewcommand\thesubfigure{(\alph{subfigure})}
```


### Subfigure 错误



IEEE 模板中想要添加子图，使用了\subfigure，想当然的添加了\usepackage{subfigure}，结果导致了下述错误：

```bash
Missing number, treated as zero. <to be read again> 
```

```bash
Illegal unit of measure (pt inserted).
```

<https://xovee.blog.csdn.net/article/details/106600220>

导致的原因貌似是因为*subfigure*包太过久远，解决办法就是把*\usepackage{subfigure}*替换成最新的*\usepackage{subcaption}*就可以了


### ACM Reference Format

ACM 的 Latex 模板会有ACM Reference的信息，所以需要去掉

在 \documentclass[sigconf]{acmart} 下面添加以下字段：

```latex
\settopmatter{printacmref=false} % Removes citation information below abstract
\renewcommand\footnotetextcopyrightpermission[1]{} % removes footnote with conference information in first column
\pagestyle{plain} % removes running headers
```
