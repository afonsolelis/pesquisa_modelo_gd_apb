#!/usr/bin/env python3

import re

# Read the file
with open('/home/afonsolelis/pesquisa_modelo_gd_apb/artigos/softwarex/pblrepositoriesmetrics.tex', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the formatting issues
# Replace the incorrectly formatted commands
content = re.sub(r'\\ref{', r'\\ref{', content)
content = re.sub(r'\\textwidth', r'\\textwidth', content)
content = re.sub(r'\\centering', r'\\centering', content)
content = re.sub(r'\\includegraphics', r'\\includegraphics', content)
content = re.sub(r'\\caption', r'\\caption', content)
content = re.sub(r'\\label', r'\\label', content)
content = re.sub(r'\\begin{landscape}', r'\\begin{landscape}', content)
content = re.sub(r'\\end{landscape}', r'\\end{landscape}', content)
content = re.sub(r'\\begin{figure', r'\\begin{figure', content)
content = re.sub(r'\\end{figure', r'\\end{figure', content)
content = re.sub(r'\\subsubsection', r'\\subsubsection', content)
content = re.sub(r'\\textbf', r'\\textbf', content)
content = re.sub(r'\\begin{itemize}', r'\\begin{itemize}', content)
content = re.sub(r'\\end{itemize}', r'\\end{itemize}', content)
content = re.sub(r'\\item', r'\\item', content)

# Fix the newlines
lines = content.split('\n')
fixed_lines = []
for line in lines:
    # Replace the incorrectly handled newlines
    line = line.replace('^^^begin', '\\begin')
    line = line.replace('^^^end', '\\end')
    fixed_lines.append(line)

content = '\n'.join(fixed_lines)

# Write the fixed content back to the file
with open('/home/afonsolelis/pesquisa_modelo_gd_apb/artigos/softwarex/pblrepositoriesmetrics.tex', 'w', encoding='utf-8') as f:
    f.write(content)

print("LaTeX file formatting fixed!")