---
title: "Hugo" # Title of the blog post.
date: 2021-04-25T14:24:29+08:00 # Date of post creation.
description: "Hugo Setting." # Description used for search engine.
featured: true # Sets if post is a featured post, making appear on the home page side bar.
draft: false   # Sets whether to render this page. Draft of true will not be rendered.
toc: false     # Controls if a table of contents should be generated for first-level links automatically.

# menu: main
featureImage: "nichijou.jpg"            # Sets featured image on blog post.
# thumbnail: "post.png" # Sets thumbnail image appearing inside card on homepage.
# shareImage: "post.png"    # Designate a separate image for social media sharing.
codeMaxLines: 10                        # Override global value for how many lines within a code block before auto-collapsing.
codeLineNumbers: true                   # Override global value for showing of line numbers within code block.
figurePositionShow: true                # Override global value for showing the figure label.
categories:
  - Code
tags:
  - Hugo
  - Blog
# comment: false # Disable comment if false.
---

## Math Support (KaTex)

几乎所有的Hugo添加Math支持都是如下四部：

1. Create a partial under /layouts/partials/math.html

   这个/layouts/partials/math.html一般在主题当中就有提供，不需要自己再另行创建

2. Within this partial reference the Auto-render Extension or host these scripts locally.
   
   同上，查看主题当中的这个math.html文件，里面添加KaTex支持，一般是如下语句：
   ```html
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.13.3/dist/katex.min.css" integrity="sha384-ThssJ7YtjywV52Gj4JE/1SQEDoMEckXyhkFVwaf4nDSm5OBlXeedVYjuuUd0Yua+" crossorigin="anonymous">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.13.3/dist/katex.min.js" integrity="sha384-Bi8OWqMXO1ta+a4EPkZv7bYGIes7C3krGSZoTGNTAnAn5eYQc7IIXrJ/7ck1drAi" crossorigin="anonymous"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.13.3/dist/contrib/auto-render.min.js" integrity="sha384-vZTG03m+2yp6N6BNi5iM4rW4oIwk5DfcNdFfxkk9ZWpDriOkXX8voJBFrAO7MpVl" crossorigin="anonymous" onload="renderMathInElement(document.body);"></script>
   ```
   同样，一般不需要自己创建

3. Include the partial in your templates like so:
   
   ```html
    {{ if or .Params.math .Site.Params.math }}
    {{ partial "math.html" . }}
    {{ end }}
   ```

   这一步需要自己加入，一般是在**主题中的/layouts/partials/**找到文章的模板，在文章的模板里加入上述语句。

   如此模板，在**themes\hugo-clarity\layouts\_default\baseof.html**中，加入上述语句：
   ```html
    {{- $s := .Site.Params }}
    {{- $p := .Params }}
    <!DOCTYPE html>
    <html lang="{{ .Lang }}" data-figures="{{ $p.figurePositionShow }}"{{ if .IsPage }} class="page"{{ end }}{{ if .IsHome }} class="home"{{ end }}{{ with $s.enforceLightMode }} data-mode="lit"{{ end }}{{ with $s.enforceDarkMode }} data-mode="dim"{{ end }}>
      <head>
        {{- partial "head" . }}
        <!-- styles definition-->
        {{- $options := (dict "targetPath" "css/styles.css" "outputStyle" "compressed" "enableSourceMap" "true") -}}
        {{ $mainSassFile :=  "sass/main.sass" }}
        {{- $styles := resources.Get $mainSassFile | resources.ExecuteAsTemplate $mainSassFile . | resources.ToCSS $options | resources.Fingerprint "sha512" }}

        {{ if or .Params.math .Site.Params.math }}
        {{ partial "math.html" . }}
        {{ end }}
    
        ......
   ```

4. To enable KaTex globally set the parameter math to true in a project's configuration
   
   To enable KaTex on a per page basis include the parameter math: true in content files

## 添加.pdf支持


- hugo pdf支持：https://github.com/anvithks/hugo-embed-pdf-shortcode

- 分别将layouts\shortcodes和static\js\pdf-js拷贝到主目录对应位置中
