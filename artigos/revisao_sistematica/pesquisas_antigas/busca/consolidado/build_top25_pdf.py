#!/usr/bin/env python3
import os
import re

BASE_DIR = os.path.dirname(__file__)
SUMMARY = os.path.join(BASE_DIR, 'strict_selection_top25_summary.txt')
OUT_TEX = os.path.join(BASE_DIR, 'relatorio_top25.tex')

header = r"""
\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{geometry}
\usepackage{longtable}
\usepackage{array}
\usepackage{hyperref}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{caption}
\usepackage{ragged2e}
\geometry{margin=2.5cm}
\captionsetup{font=small}
\hypersetup{colorlinks=true,linkcolor=black,urlcolor=blue}
\setlength{\parskip}{0.6em}
\setlength{\parindent}{0pt}

\begin{document}

\begin{center}
{\LARGE Seleção Final (Top 25) – Avaliação em PBL/PbL no Ensino Superior}\\[6pt]
{\large Corte 2018+, critérios Kitchenham, foco avaliativo}
\end{center}

\section*{Critérios aplicados}
\begin{itemize}
  \item Inclusão: Project-Based ou Problem-Based no título/keywords; foco em avaliação; Ensino Superior; ano $\ge$ 2018; apenas estudos primários.
  \item Qualidade: avaliação processual, colaboração/contribuição, competências, feedback formativo, escalabilidade/objetividade; instrumento/tecnologia descritos; validação empírica; contexto HE.
  \item Exclusão: K–12; menção tangencial a PBL/PbL; revisões; duplicados; pré‑2018.
\end{itemize}

\section*{Top 25 selecionados}
"""

table_begin = r"""
\setlength\extrarowheight{2pt}
\begin{longtable}{@{}r>{\RaggedRight\arraybackslash}p{1.2cm}>{\RaggedRight\arraybackslash}p{8.6cm}>{\RaggedRight\arraybackslash}p{1.2cm}>{\RaggedRight\arraybackslash}p{5.2cm}@{}}
\toprule
\# & Ano & Título & Score & Motivos \\
\midrule
\endfirsthead
\toprule
\# & Ano & Título & Score & Motivos \\
\midrule
\endhead
\bottomrule
\endfoot
"""

footer = r"""
\end{longtable}

\vspace{0.5em}
\emph{Geração: } script automático a partir de `strict\_selection\_top25\_summary.txt`.

\end{document}
"""


def parse_summary(path):
    items = []
    if not os.path.exists(path):
        return items
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    blocks = [b.strip() for b in content.strip().split("\n\n") if b.strip()]
    for b in blocks:
        lines = [l for l in b.splitlines() if l.strip()]
        if not lines:
            continue
        m = re.match(r"^\s*(\d+)\. \[(\d{4})\]\s*(.+)$", lines[0])
        if not m:
            continue
        rank = int(m.group(1))
        year = m.group(2)
        title = m.group(3).strip()
        score, reasons = '', ''
        for l in lines[2:]:
            if l.strip().lower().startswith('score:'):
                sm = re.match(r"^Score:\s*(\d+)\s*\|\s*Reasons:\s*(.+)$", l.strip(), re.IGNORECASE)
                if sm:
                    score = sm.group(1)
                    reasons = sm.group(2)
                    break
        items.append((rank, year, title, score, reasons))
    items.sort(key=lambda x: x[0])
    return items


def tex_escape(s: str) -> str:
    repl = {
        '&': r'\&', '%': r'\%', '$': r'\$', '#': r'\#', '_': r'\_', '{': r'\{', '}': r'\}',
        '~': r'\textasciitilde{}', '^': r'\textasciicircum{}', '\\': r'\textbackslash{}'
    }
    out = ''
    for ch in s:
        out += repl.get(ch, ch)
    return out


def main():
    items = parse_summary(SUMMARY)
    rows_tex = []
    for rank, year, title, score, reasons in items:
        title_tex = tex_escape(title)
        reasons_tex = tex_escape(reasons)
        rows_tex.append(f"{rank} & {year} & {title_tex} & {score} & {reasons_tex} \\ ")

    with open(OUT_TEX, 'w', encoding='utf-8') as f:
        f.write(header)
        f.write(table_begin)
        for row in rows_tex:
            f.write(row + "\n")
        f.write(footer)

    print(f"Wrote LaTeX: {OUT_TEX}")


if __name__ == '__main__':
    main()

