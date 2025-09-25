#!/usr/bin/env python3

import re

# Read the file
with open('/home/afonsolelis/pesquisa_modelo_gd_apb/artigos/softwarex/pblrepositoriesmetrics.tex', 'r', encoding='utf-8') as f:
    content = f.read()

# Add newlines before and after LaTeX environments
content = re.sub(r'(\\begin{landscape})', r'\n\n\\1', content)
content = re.sub(r'(\\end{landscape})', r'\\1\n\n', content)
content = re.sub(r'(\\begin{figure[[^]]*]})', r'\n\n\\1', content)
content = re.sub(r'(\\end{figure})', r'\\1\n\n', content)
content = re.sub(r'(\\begin{itemize})', r'\n\n\\1', content)
content = re.sub(r'(\\end{itemize})', r'\\1\n\n', content)
content = re.sub(r'(\\begin{enumerate})', r'\n\n\\1', content)
content = re.sub(r'(\\end{enumerate})', r'\\1\n\n', content)

# Add newlines after section definitions
content = re.sub(r'(\\subsubsection{[^}]*})', r'\\1\n\n', content)

# Add newlines after item definitions
content = re.sub(r'(\\item [^{])', r'\n\\1', content)

# Clean up multiple consecutive newlines
content = re.sub(r'\n{3,}', r'\n\n', content)

# Write the fixed content back to the file
with open('/home/afonsolelis/pesquisa_modelo_gd_apb/artigos/softwarex/pblrepositoriesmetrics.tex', 'w', encoding='utf-8') as f:
    f.write(content)

print("LaTeX file formatting fixed with proper newlines!")