

import sys

def format_latex_source(content):
    paragraphs = content.split('\n\n')
    new_paragraphs = []
    for p in paragraphs:
        lines = p.split('\n')
        is_simple_paragraph = True
        for line in lines:
            stripped = line.strip()
            if stripped.startswith('\\') or stripped.startswith('%') or stripped.startswith('@') or '&' in stripped or '\\\\' in stripped:
                is_simple_paragraph = False
                break
        
        if is_simple_paragraph:
            if not lines:
                new_paragraphs.append(p)
                continue

            first_line_index = -1
            for i, line in enumerate(lines):
                if line.strip():
                    first_line_index = i
                    break
            
            if first_line_index == -1:
                 new_paragraphs.append(p)
                 continue

            first_line = lines[first_line_index]
            indent_len = len(first_line) - len(first_line.lstrip())
            indent = first_line[:indent_len]
            
            joined_paragraph = indent + ' '.join(l.strip() for l in lines if l.strip())
            new_paragraphs.append(joined_paragraph)
        else:
            new_paragraphs.append(p)
            
    return '\n\n'.join(new_paragraphs)

input_content = sys.stdin.read()
reformatted_content = format_latex_source(input_content)
print(reformatted_content)

